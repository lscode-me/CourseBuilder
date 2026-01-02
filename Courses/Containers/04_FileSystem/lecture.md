# Union Filesystems
## Слои образов и Copy-on-Write

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы файловых систем Linux
- Знать mount namespaces
- Иметь базовое представление о Docker-образах

**Recommended prior modules:**

- [Linux Namespaces](../02_Namespaces/) — mount namespace
- [Cgroups](../03_Cgroups/) — управление ресурсами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принцип работы union filesystems
- Настраивать и использовать OverlayFS
- Понимать структуру слоёв Docker-образов
- Диагностировать проблемы с файловыми системами контейнеров

---

## 1. Зачем нужны Union Filesystems

Union filesystem объединяет несколько директорий (слоёв) в единое представление. Это фундамент для эффективной работы контейнерных образов.

### 1.1 Проблема без union filesystems

**Традиционный подход:**
```
Container 1: Ubuntu 20.04 + Python + App1  →  3GB
Container 2: Ubuntu 20.04 + Python + App2  →  3GB
Container 3: Ubuntu 20.04 + Python + App3  →  3GB
─────────────────────────────────────────────────
Total: 9GB
```

**С union filesystem:**
```
Layer 4: App1          ─┐
Layer 4: App2          ─┼─ Unique layers (~100MB each)
Layer 4: App3          ─┘
Layer 3: Python        ─── Shared (~500MB)
Layer 2: Ubuntu base   ─── Shared (~200MB)
Layer 1: Root FS       ─── Shared (~100MB)
─────────────────────────────────────────────────
Total: ~1.1GB (вместо 9GB!)
```

### 1.2 Ключевые концепции

**Copy-on-Write (CoW):**

- Слои нижнего уровня доступны только для чтения
- При модификации файл копируется в верхний (writable) слой
- Оригинал остаётся неизменным

**Layered Architecture:**

- Образ состоит из стека слоёв
- Каждый слой — результат одной инструкции Dockerfile
- Слои могут переиспользоваться между образами

### 1.3 История union filesystems

| Год | Файловая система | Статус |
|-----|------------------|--------|
| 2004 | UnionFS | Первая реализация |
| 2006 | AUFS | Популярна в ранних Docker |
| 2010 | OverlayFS | Включена в mainline kernel |
| 2014 | overlay2 | Улучшенная версия Overlay |
| 2020+ | OverlayFS | Стандарт де-факто |

---

## 2. OverlayFS — современный стандарт

OverlayFS — union filesystem, включённая в mainline Linux kernel начиная с версии 3.18.

### 2.1 Архитектура OverlayFS

```
┌─────────────────────────────────────────────┐
│              Merged View                    │
│         (то, что видит процесс)             │
│    /merged                                  │
└─────────────────────────────────────────────┘
                    │
         ┌──────────┴──────────┐
         │                     │
         ▼                     ▼
┌─────────────────┐   ┌─────────────────────┐
│   Upper Layer   │   │    Lower Layer(s)   │
│   (read-write)  │   │    (read-only)      │
│   /upper        │   │    /lower           │
└─────────────────┘   └─────────────────────┘
```

**Компоненты:**

- **lowerdir** — нижние слои (read-only), может быть несколько

- **upperdir** — верхний слой (read-write)

- **workdir** — рабочая директория для атомарных операций

- **merged** — точка монтирования с объединённым view

### 2.2 Базовое использование OverlayFS

```bash
# Создаём структуру директорий

mkdir -p /tmp/overlay/{lower,upper,work,merged}

# Создаём файлы в нижнем слое

echo "File from lower layer" > /tmp/overlay/lower/file1.txt
echo "Another file" > /tmp/overlay/lower/file2.txt
mkdir /tmp/overlay/lower/dir1
echo "Nested file" > /tmp/overlay/lower/dir1/nested.txt

# Монтируем OverlayFS

sudo mount -t overlay overlay \
    -o lowerdir=/tmp/overlay/lower,upperdir=/tmp/overlay/upper,workdir=/tmp/overlay/work \
    /tmp/overlay/merged

# Проверяем содержимое

ls -la /tmp/overlay/merged/
```

**Output:**
```
total 12
drwxr-xr-x 3 root root 4096 Dec  1 12:00 .
drwxr-xr-x 6 root root 4096 Dec  1 12:00 ..
drwxr-xr-x 2 root root 4096 Dec  1 12:00 dir1
-rw-r--r-- 1 root root   22 Dec  1 12:00 file1.txt
-rw-r--r-- 1 root root   13 Dec  1 12:00 file2.txt
```

### 2.3 Copy-on-Write в действии

```bash
# Изменяем файл через merged view

echo "Modified content" > /tmp/overlay/merged/file1.txt

# Проверяем — файл скопирован в upper layer

cat /tmp/overlay/upper/file1.txt
```

**Output:**
```
Modified content
```

```bash
# Оригинал в lower layer не изменился!

cat /tmp/overlay/lower/file1.txt
```

**Output:**
```
File from lower layer
```

### 2.4 Удаление файлов (Whiteout)

При удалении файла из lower layer создаётся специальный whiteout-файл:

```bash
# Удаляем файл

rm /tmp/overlay/merged/file2.txt

# Проверяем merged — файла нет

ls /tmp/overlay/merged/
```

**Output:**
```
dir1  file1.txt
```

```bash
# В upper layer создан whiteout (character device 0,0)

ls -la /tmp/overlay/upper/
```

**Output:**
```
total 8
drwxr-xr-x 2 root root 4096 Dec  1 12:01 .
c--------- 1 root root 0, 0 Dec  1 12:01 file2.txt
-rw-r--r-- 1 root root   17 Dec  1 12:00 file1.txt
```

```bash
# Файл в lower layer всё ещё существует

cat /tmp/overlay/lower/file2.txt
```

**Output:**
```
Another file
```

---

## 3. Множественные lower layers

OverlayFS поддерживает несколько нижних слоёв — это основа для Docker-образов.

### 3.1 Создание многослойной структуры

```bash
# Создаём несколько lower layers

mkdir -p /tmp/multilayer/{layer1,layer2,layer3,upper,work,merged}

# Layer 1 — базовая система

echo "base config" > /tmp/multilayer/layer1/config.txt
mkdir /tmp/multilayer/layer1/bin
echo "#!/bin/bash\necho base" > /tmp/multilayer/layer1/bin/app

# Layer 2 — runtime

echo "runtime config" > /tmp/multilayer/layer2/config.txt
mkdir /tmp/multilayer/layer2/lib
echo "library v1" > /tmp/multilayer/layer2/lib/mylib.so

# Layer 3 — application

mkdir /tmp/multilayer/layer3/app
echo "app code" > /tmp/multilayer/layer3/app/main.py

# Монтируем с несколькими lower layers (порядок важен!)
# Первый в списке — верхний lower layer

sudo mount -t overlay overlay \
    -o lowerdir=/tmp/multilayer/layer3:/tmp/multilayer/layer2:/tmp/multilayer/layer1,upperdir=/tmp/multilayer/upper,workdir=/tmp/multilayer/work \
    /tmp/multilayer/merged

# Результат — объединённое представление

find /tmp/multilayer/merged -type f
```

**Output:**
```
/tmp/multilayer/merged/config.txt
/tmp/multilayer/merged/bin/app
/tmp/multilayer/merged/lib/mylib.so
/tmp/multilayer/merged/app/main.py
```

### 3.2 Приоритет слоёв

```bash
# config.txt есть в layer1 и layer2
# Какой будет виден?

cat /tmp/multilayer/merged/config.txt
```

**Output:**
```
runtime config
```

Файлы из верхних lower layers перекрывают файлы из нижних (layer2 перекрывает layer1).

### 3.3 Диаграмма приоритетов

```
              ▲ Visibility Priority
              │
┌─────────────┴─────────────┐
│      Upper (writable)     │  ← Highest priority
├───────────────────────────┤
│      Layer 3 (app)        │
├───────────────────────────┤
│      Layer 2 (runtime)    │
├───────────────────────────┤
│      Layer 1 (base)       │  ← Lowest priority
└───────────────────────────┘
```

---

## 4. AUFS — историческая перспектива

AUFS (Another Union File System) была первой широко используемой union filesystem в Docker.

### 4.1 Особенности AUFS

**Преимущества:**

- Зрелая и стабильная (с 2006)
- Хорошая поддержка множества слоёв
- Эффективное использование памяти

**Недостатки:**

- Не включена в mainline kernel
- Требует патчей ядра
- Сложность сопровождения

### 4.2 AUFS vs OverlayFS

| Аспект | AUFS | OverlayFS |
|--------|------|-----------|
| Kernel | Патчи | Mainline (3.18+) |
| Max layers | 127 | Без ограничений |
| Performance | Хорошая | Лучше |
| Memory usage | Больше | Меньше |
| Статус | Устарел | Актуален |

### 4.3 Почему Docker перешёл на OverlayFS

1. **Mainline kernel** — не нужны патчи
2. **Производительность** — меньше overhead
3. **Простота** — проще архитектура
4. **Поддержка** — активная разработка

---

## 5. Docker и storage drivers

Docker использует storage drivers для работы с файловыми системами контейнеров.

### 5.1 Доступные storage drivers

| Driver | Файловая система | Статус |
|--------|------------------|--------|
| overlay2 | OverlayFS | Рекомендуется |
| fuse-overlayfs | FUSE | Для rootless |
| btrfs | Btrfs | Поддерживается |
| zfs | ZFS | Поддерживается |
| devicemapper | Device Mapper | Устарел |
| aufs | AUFS | Устарел |
| vfs | Без CoW | Для тестирования |

### 5.2 Проверка текущего driver

```bash
docker info | grep -i storage
```

**Output:**
```
 Storage Driver: overlay2
```

```bash
# Детальная информация

docker info --format '{{json .Driver}}'
```

### 5.3 Структура overlay2 в Docker

```bash
# Директория хранения Docker

ls -la /var/lib/docker/overlay2/
```

**Output:**
```
total 24
drwx--x--- 6 root root 4096 Dec  1 12:00 .
drwx--x--- 13 root root 4096 Dec  1 11:00 ..
drwx--x--- 4 root root 4096 Dec  1 12:00 abc123...
drwx--x--- 4 root root 4096 Dec  1 12:00 def456...
drwx--x--- 3 root root 4096 Dec  1 12:00 ghi789...-init
drwx--x--- 2 root root 4096 Dec  1 12:00 l
```

```bash
# Структура слоя

ls -la /var/lib/docker/overlay2/abc123.../
```

**Output:**
```
total 16
drwx--x--- 4 root root 4096 Dec  1 12:00 .
drwx--x--- 6 root root 4096 Dec  1 12:00 ..
-rw------- 1 root root   64 Dec  1 12:00 link
-rw------- 1 root root   86 Dec  1 12:00 lower
drwxr-xr-x 2 root root 4096 Dec  1 12:00 diff
drwx------ 2 root root 4096 Dec  1 12:00 work
```

- **diff/** — содержимое этого слоя

- **link** — короткий идентификатор для lowerdir

- **lower** — ссылки на нижние слои

- **work/** — рабочая директория OverlayFS

### 5.4 Анализ слоёв образа

```bash
# Скачиваем образ

docker pull nginx:alpine

# Смотрим слои

docker history nginx:alpine
```

**Output:**
```
IMAGE          CREATED       CREATED BY                                      SIZE
a2d5e8c4f8b2   2 weeks ago   CMD ["nginx" "-g" "daemon off;"]                0B
<missing>      2 weeks ago   STOPSIGNAL SIGQUIT                              0B
<missing>      2 weeks ago   EXPOSE 80                                       0B
<missing>      2 weeks ago   ENTRYPOINT ["/docker-entrypoint.sh"]            0B
<missing>      2 weeks ago   COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB
<missing>      2 weeks ago   COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB
<missing>      2 weeks ago   COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB
<missing>      2 weeks ago   COPY docker-entrypoint.sh /                     1.62kB
<missing>      2 weeks ago   RUN /bin/sh -c set -x     && addgroup -g 101…   7.99MB
<missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1            0B
<missing>      3 weeks ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.25.3     0B
<missing>      3 weeks ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
<missing>      3 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      3 weeks ago   /bin/sh -c #(nop) ADD file:756183bba9c7f4593…   7.34MB
```

### 5.5 Инспекция слоёв контейнера

```bash
# Запускаем контейнер

docker run -d --name test-nginx nginx:alpine

# Получаем информацию о слоях

docker inspect test-nginx --format '{{json .GraphDriver.Data}}' | jq
```

**Output:**
```json
{
  "LowerDir": "/var/lib/docker/overlay2/abc.../diff:/var/lib/docker/overlay2/def.../diff",
  "MergedDir": "/var/lib/docker/overlay2/xyz.../merged",
  "UpperDir": "/var/lib/docker/overlay2/xyz.../diff",
  "WorkDir": "/var/lib/docker/overlay2/xyz.../work"
}
```

---

## 6. Copy-on-Write детально

### 6.1 Операции чтения

При чтении файла OverlayFS:

1. Проверяет наличие в upperdir
2. Если нет — ищет в lowerdirs (сверху вниз)
3. Возвращает первый найденный файл

```bash
# Демонстрация: чтение идёт из lower layer

strace -e openat cat /tmp/overlay/merged/file_from_lower.txt 2>&1 | grep overlay
```

### 6.2 Операции записи

**Изменение существующего файла:**
```
1. Файл целиком копируется из lower в upper (copy-up)
2. Изменения применяются к копии в upper
3. При последующих чтениях файл берётся из upper
```

**Создание нового файла:**
```
1. Файл создаётся напрямую в upper layer
2. Нижние слои не затрагиваются
```

### 6.3 Copy-up overhead

```bash
# Большой файл в lower layer

dd if=/dev/zero of=/tmp/overlay/lower/bigfile bs=1M count=100

# Монтируем overlay

sudo mount -t overlay overlay \
    -o lowerdir=/tmp/overlay/lower,upperdir=/tmp/overlay/upper,workdir=/tmp/overlay/work \
    /tmp/overlay/merged

# Изменение 1 байта вызывает copy-up всего файла!

time echo "x" >> /tmp/overlay/merged/bigfile

# Файл скопирован в upper

ls -la /tmp/overlay/upper/bigfile
```

**Вывод:** Избегайте модификации больших файлов в контейнерах — лучше перезаписать целиком или использовать volumes.

### 6.4 Metacopy

Начиная с kernel 4.19, OverlayFS поддерживает metacopy — при изменении метаданных (permissions, timestamps) копируются только метаданные, не содержимое.

```bash
# Включение metacopy

sudo mount -t overlay overlay \
    -o lowerdir=/lower,upperdir=/upper,workdir=/work,metacopy=on \
    /merged
```

---

## 7. Оптимизация Docker-образов

### 7.1 Минимизация слоёв

```dockerfile
# Плохо: много слоёв

FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install flask
RUN apt-get clean

# Хорошо: объединение команд

FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 7.2 Порядок инструкций

```dockerfile
# Плохо: COPY приложения перед установкой зависимостей

FROM python:3.11-slim
COPY . /app
RUN pip install -r /app/requirements.txt
# Любое изменение кода инвалидирует кеш pip install

# Хорошо: сначала зависимости, потом код

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# pip install кешируется пока requirements.txt не меняется
```

### 7.3 Multi-stage builds

```dockerfile
# Build stage

FROM golang:1.21 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /app/server

# Production stage

FROM alpine:3.18
RUN apk --no-cache add ca-certificates
COPY --from=builder /app/server /server
CMD ["/server"]
# Финальный образ не содержит Go toolchain
```

### 7.4 Анализ размера слоёв

```bash
# Утилита dive для анализа образов

docker run --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    wagoodman/dive nginx:alpine
```

```bash
# Простой анализ

docker history --no-trunc nginx:alpine | awk '{print $NF, $1}'
```

---

## 8. Другие storage backends

### 8.1 Btrfs

Btrfs использует встроенные возможности CoW вместо OverlayFS:

```bash
# Проверка поддержки

docker info | grep -i btrfs

# Создание Docker с Btrfs
# 1. Отформатировать раздел в Btrfs

mkfs.btrfs /dev/sdb1

# 2. Смонтировать в /var/lib/docker

mount /dev/sdb1 /var/lib/docker

# 3. Перезапустить Docker

systemctl restart docker
```

**Преимущества:**

- Нативные snapshots
- Быстрое создание контейнеров
- Дедупликация

### 8.2 ZFS

```bash
# Создание zpool для Docker

zpool create docker-pool /dev/sdb

# Настройка Docker для использования ZFS

cat > /etc/docker/daemon.json << EOF
{
    "storage-driver": "zfs"
}
EOF

systemctl restart docker
```

**Преимущества:**

- Надёжность данных (checksums)
- Compression
- Мощные snapshots

### 8.3 Device Mapper (устарел)

Использует thin provisioning и snapshots на уровне блочных устройств.

```bash
# Исторически использовался в RHEL/CentOS
# Сейчас рекомендуется overlay2
```

---

## 9. Rootless containers и fuse-overlayfs

### 9.1 Проблема с OverlayFS без root

Обычный OverlayFS требует:

- CAP_SYS_ADMIN capability
- Или root-права

### 9.2 fuse-overlayfs

fuse-overlayfs — реализация OverlayFS через FUSE (Filesystem in Userspace):

```bash
# Установка

apt install fuse-overlayfs

# Использование

fuse-overlayfs -o lowerdir=/lower,upperdir=/upper,workdir=/work /merged
```

### 9.3 Rootless Docker/Podman

```bash
# Podman rootless использует fuse-overlayfs по умолчанию

podman info | grep -A5 graphDriverName
```

**Output:**
```
graphDriverName: overlay
graphOptions:
  overlay.mount_program: /usr/bin/fuse-overlayfs
```

---

## 10. Troubleshooting

### 10.1 Распространённые проблемы

**Ошибка: "overlay: upper fs needs to support d_type"**

```bash
# Проверка d_type support

xfs_info / | grep ftype
```

Решение: пересоздать файловую систему с `ftype=1` или использовать ext4.

**Ошибка: "no space left on device"**

```bash
# Проверка использования overlay2

du -sh /var/lib/docker/overlay2/*

# Очистка неиспользуемых данных

docker system prune -a
```

### 10.2 Проверка overlay mount

```bash
# Информация о монтировании

mount | grep overlay

# Или через /proc/mounts

grep overlay /proc/mounts
```

### 10.3 Отладка слоёв контейнера

```bash
# Найти слои конкретного контейнера

CONTAINER_ID=$(docker ps -q --filter name=myapp)
docker inspect $CONTAINER_ID --format '{{.GraphDriver.Data.LowerDir}}' | tr ':' '\n'

# Посмотреть что изменилось в контейнере (upper layer)

docker diff $CONTAINER_ID
```

**Output:**
```
C /var
C /var/log
A /var/log/app.log
C /tmp
A /tmp/cache
D /etc/hosts.backup
```

- **A** — Added

- **C** — Changed

- **D** — Deleted

---

## 💡 Key Takeaways

- **Union filesystems** объединяют слои, экономя место через переиспользование

- **OverlayFS** — стандарт де-факто, включён в mainline kernel

- **Copy-on-Write** копирует файл целиком при изменении — избегайте модификации больших файлов

- **Порядок инструкций в Dockerfile** влияет на кеширование слоёв

- **Multi-stage builds** уменьшают размер финальных образов

---

## 🚀 Next Steps

**Related Modules:**

- [OCI Standards](../05_OCI/) — спецификация образов
- [Container Runtimes](../06_Runtimes/) — как runtime работают со слоями

**Practice Ideas:**

1. Создайте OverlayFS вручную и исследуйте Copy-on-Write
2. Оптимизируйте Dockerfile для минимизации размера образа
3. Используйте `dive` для анализа слоёв образа
4. Сравните размер одного приложения с разными базовыми образами

**Going Deeper:**

- Btrfs subvolumes для контейнеров
- ZFS datasets и Docker
- SquashFS для read-only layers

---

## 📚 Additional Resources

**Documentation:**

- [OverlayFS kernel documentation](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt)
- [Docker storage drivers](https://docs.docker.com/storage/storagedriver/)
- [fuse-overlayfs](https://github.com/containers/fuse-overlayfs)

**Articles:**

- [Understanding Docker's storage drivers](https://www.docker.com/blog/deep-dive-into-docker-storage-drivers/)
- [Docker image layers explained](https://dzone.com/articles/docker-layers-explained)

**Tools:**

- [dive](https://github.com/wagoodman/dive) — анализ слоёв образов
- [skopeo](https://github.com/containers/skopeo) — работа с образами без Docker daemon

---





