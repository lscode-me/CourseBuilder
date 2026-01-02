# Process Isolation
## От chroot к современным контейнерам

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции Unix/Linux (процессы, файловая система)
- Уметь работать в командной строке Linux
- Иметь базовое представление о системных вызовах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить эволюцию технологий изоляции процессов
- Использовать `chroot` для создания изолированного окружения
- Понимать ограничения `chroot` и причины появления контейнеров
- Описать ключевые компоненты современной контейнеризации

---

## 1. Зачем нужна изоляция процессов

Изоляция процессов — фундаментальная потребность в многопользовательских системах. Она решает несколько критических задач:

### 1.1 Безопасность

Изоляция предотвращает несанкционированный доступ процессов к ресурсам других процессов или системы в целом.

**Сценарии:**

- Веб-сервер не должен иметь доступа к домашним директориям пользователей
- Скомпрометированный процесс не должен влиять на остальную систему
- Пользовательские процессы не должны модифицировать системные файлы

### 1.2 Управление ресурсами

Изоляция позволяет контролировать потребление ресурсов:

- CPU time
- Память
- Disk I/O
- Network bandwidth

### 1.3 Воспроизводимость окружения

Изолированные окружения обеспечивают:

- Консистентное поведение приложений
- Независимость от host-системы
- Упрощение развертывания

### 1.4 Мультитенантность

В облачных средах изоляция позволяет:

- Запускать приложения разных клиентов на одном сервере
- Гарантировать отсутствие взаимного влияния
- Оптимизировать использование оборудования

---

## 2. chroot — первый шаг к изоляции

`chroot` (change root) — системный вызов и утилита, появившаяся в Unix Version 7 (1979). Это простейший механизм изоляции файловой системы.

### 2.1 Принцип работы chroot

`chroot` изменяет корневую директорию для процесса и его потомков. После вызова `chroot("/new/root")` процесс видит `/new/root` как `/`.

```c
#include <unistd.h>
#include <stdio.h>

int main() {
    // Изменяем корневую директорию
    if (chroot("/var/chroot/jail") != 0) {
        perror("chroot failed");
        return 1;
    }
    
    // Переходим в новый корень
    if (chdir("/") != 0) {
        perror("chdir failed");
        return 1;
    }
    
    // Теперь "/" указывает на /var/chroot/jail
    printf("Now in chroot jail\n");
    
    // Запускаем shell
    execl("/bin/sh", "sh", NULL);
    
    return 0;
}
```

### 2.2 Практическое использование chroot

Создадим минимальное chroot-окружение:

```bash
# Создаем структуру директорий

mkdir -p /var/chroot/jail/{bin,lib,lib64,usr/lib}

# Копируем bash и необходимые библиотеки

cp /bin/bash /var/chroot/jail/bin/

# Определяем зависимости bash

ldd /bin/bash
```

**Output:**
```
linux-vdso.so.1 (0x00007ffcc3bfe000)
libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
/lib64/ld-linux-x86-64.so.2
```

```bash
# Копируем библиотеки

cp /lib/x86_64-linux-gnu/libtinfo.so.6 /var/chroot/jail/lib/
cp /lib/x86_64-linux-gnu/libdl.so.2 /var/chroot/jail/lib/
cp /lib/x86_64-linux-gnu/libc.so.6 /var/chroot/jail/lib/
cp /lib64/ld-linux-x86-64.so.2 /var/chroot/jail/lib64/

# Копируем дополнительные утилиты

for cmd in ls cat echo; do
    cp /bin/$cmd /var/chroot/jail/bin/
    # Копируем зависимости каждой утилиты
    ldd /bin/$cmd | grep "=>" | awk '{print $3}' | \
        xargs -I {} cp {} /var/chroot/jail/lib/ 2>/dev/null
done

# Входим в chroot

sudo chroot /var/chroot/jail /bin/bash
```

**Output (внутри chroot):**
```bash
bash-5.1# pwd
/
bash-5.1# ls
bin  lib  lib64  usr
bash-5.1# cat /etc/passwd
cat: /etc/passwd: No such file or directory
```

### 2.3 Автоматизация создания chroot

Скрипт для создания минимального chroot-окружения:

```bash
#!/bin/bash
# create_chroot.sh - создание базового chroot окружения

CHROOT_DIR="${1:-/var/chroot/minimal}"
COMMANDS="bash ls cat echo pwd mkdir rm cp mv"

# Создаем структуру директорий

mkdir -p "$CHROOT_DIR"/{bin,lib,lib64,etc,tmp,proc,dev}
chmod 1777 "$CHROOT_DIR/tmp"

# Функция для копирования команды с зависимостями

copy_command() {
    local cmd="$1"
    local cmd_path=$(which "$cmd" 2>/dev/null)
    
    if [ -z "$cmd_path" ]; then
        echo "Warning: $cmd not found"
        return 1
    fi
    
    # Копируем исполняемый файл
    cp "$cmd_path" "$CHROOT_DIR/bin/"
    
    # Копируем библиотеки
    ldd "$cmd_path" 2>/dev/null | while read line; do
        lib=$(echo "$line" | grep -oP '/\S+\.so\S*')
        if [ -n "$lib" ] && [ -f "$lib" ]; then
            dir=$(dirname "$lib")
            mkdir -p "$CHROOT_DIR$dir"
            cp -n "$lib" "$CHROOT_DIR$dir/" 2>/dev/null
        fi
    done
}

# Копируем команды

for cmd in $COMMANDS; do
    echo "Copying $cmd..."
    copy_command "$cmd"
done

# Копируем динамический линкер

cp /lib64/ld-linux-x86-64.so.2 "$CHROOT_DIR/lib64/" 2>/dev/null

# Создаем базовые файлы

echo "root:x:0:0:root:/root:/bin/bash" > "$CHROOT_DIR/etc/passwd"
echo "root:x:0:" > "$CHROOT_DIR/etc/group"

echo "Chroot environment created at $CHROOT_DIR"
echo "Enter with: sudo chroot $CHROOT_DIR /bin/bash"
```

---

## 3. Ограничения chroot

Несмотря на простоту, `chroot` имеет серьёзные ограничения, делающие его непригодным для надёжной изоляции.

### 3.1 Побег из chroot (chroot escape)

Процесс с правами root может легко выйти из chroot:

```c
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int dir_fd;
    
    // Создаем временную директорию
    mkdir("escape_dir", 0755);
    
    // Открываем дескриптор на неё
    dir_fd = open("escape_dir", O_RDONLY);
    
    // Делаем chroot в эту директорию
    chroot("escape_dir");
    
    // Используем fchdir для возврата
    fchdir(dir_fd);
    
    // Поднимаемся вверх по дереву
    for (int i = 0; i < 100; i++) {
        chdir("..");
    }
    
    // Делаем chroot в реальный корень
    chroot(".");
    
    // Теперь мы вне jail
    execl("/bin/sh", "sh", NULL);
    
    return 0;
}
```

### 3.2 Отсутствие изоляции процессов

Процессы внутри chroot видят процессы всей системы:

```bash
# Внутри chroot (если /proc примонтирован)

ps aux  # Покажет ВСЕ процессы системы
```

### 3.3 Отсутствие изоляции сети

Сетевой стек общий для всей системы:

```bash
# Внутри chroot

netstat -tlnp  # Покажет все сетевые соединения host-системы
```

### 3.4 Отсутствие ограничения ресурсов

chroot не ограничивает:

- Использование CPU
- Потребление памяти
- Дисковые операции
- Количество процессов

### 3.5 Таблица ограничений chroot

| Аспект | Изоляция в chroot | Комментарий |
|--------|-------------------|-------------|
| Файловая система | Частичная | Можно выйти с root-правами |
| Процессы | Нет | Видны все процессы системы |
| Сеть | Нет | Общий сетевой стек |
| IPC | Нет | Общие семафоры, shared memory |
| Пользователи | Нет | Общий /etc/passwd |
| Hostname | Нет | Общее имя хоста |
| Ресурсы | Нет | Нет ограничений |

---

## 4. FreeBSD Jails — развитие идеи

FreeBSD Jails (2000) стали значительным шагом вперёд, добавив изоляцию, которой не хватало chroot.

### 4.1 Возможности Jails

FreeBSD Jails обеспечивают:

- Изоляцию файловой системы (усиленная версия chroot)
- Изоляцию процессов (jail видит только свои процессы)
- Изоляцию сети (собственный IP-адрес)
- Ограничение привилегий root внутри jail

### 4.2 Создание jail в FreeBSD

```bash
# Создание базовой структуры jail

mkdir -p /jails/www
cd /jails/www

# Распаковка базовой системы

tar -xf /path/to/base.txz -C /jails/www

# Конфигурация jail в /etc/jail.conf

cat << 'EOF' >> /etc/jail.conf
www {
    host.hostname = "www.jail";
    ip4.addr = 192.168.1.100;
    path = "/jails/www";
    exec.start = "/bin/sh /etc/rc";
    exec.stop = "/bin/sh /etc/rc.shutdown";
    mount.devfs;
}
EOF

# Запуск jail

jail -c www

# Вход в jail

jexec www /bin/sh
```

### 4.3 Сравнение chroot и Jails

| Функция | chroot | FreeBSD Jail |
|---------|--------|--------------|
| Изоляция FS | Слабая | Сильная |
| Изоляция процессов | Нет | Да |
| Изоляция сети | Нет | Да |
| Ограничение root | Нет | Да |
| Escape возможен | Да | Сложно |

---

## 5. Solaris Zones и Containers

Solaris 10 (2005) представил Zones — ещё более продвинутую технологию контейнеризации.

### 5.1 Типы Zones

**Global Zone:**

- Основная операционная система
- Имеет доступ ко всему оборудованию
- Управляет non-global zones

**Non-Global Zones:**

- Изолированные экземпляры Solaris
- Могут быть sparse (разделяют /usr с global zone) или whole-root

### 5.2 Особенности Solaris Zones

```bash
# Создание зоны

zonecfg -z myzone << EOF
create
set zonepath=/zones/myzone
set autoboot=true
add net
    set physical=e1000g0
    set address=192.168.1.50/24
end
verify
commit
EOF

# Установка зоны

zoneadm -z myzone install

# Запуск зоны

zoneadm -z myzone boot

# Вход в зону

zlogin myzone
```

### 5.3 Resource Management в Solaris

Solaris предоставлял продвинутое управление ресурсами:

```bash
# Ограничение CPU для зоны

zonecfg -z myzone << EOF
add dedicated-cpu
    set ncpus=2
end
commit
EOF

# Ограничение памяти

zonecfg -z myzone << EOF
add capped-memory
    set physical=2G
    set swap=4G
end
commit
EOF
```

---

## 6. Linux: путь к контейнерам

Linux пошёл другим путём — вместо монолитного решения были созданы отдельные механизмы, которые вместе обеспечивают контейнеризацию.

### 6.1 Эволюция технологий в Linux

| Год | Технология | Назначение |
|-----|------------|------------|
| 1979 | chroot | Изоляция файловой системы |
| 2002 | Linux namespaces (mount) | Изоляция точек монтирования |
| 2006 | cgroups (Process Containers) | Управление ресурсами |
| 2008 | LXC | Первые Linux-контейнеры |
| 2013 | Docker | Удобная работа с контейнерами |
| 2014 | Kubernetes | Оркестрация контейнеров |
| 2015 | OCI | Стандартизация |

### 6.2 Компоненты контейнеризации в Linux

Современный контейнер в Linux — это комбинация:

1. **Namespaces** — изоляция видимости ресурсов
   - PID namespace — изоляция процессов
   - NET namespace — изоляция сети
   - MNT namespace — изоляция файловой системы
   - UTS namespace — изоляция hostname
   - IPC namespace — изоляция межпроцессного взаимодействия
   - USER namespace — изоляция пользователей
   - CGROUP namespace — изоляция cgroups

2. **Cgroups** — управление ресурсами
   - CPU limits
   - Memory limits
   - I/O bandwidth
   - Device access

3. **Union Filesystems** — эффективные образы
   - OverlayFS
   - AUFS (устарел)

4. **Seccomp** — ограничение системных вызовов

5. **Capabilities** — гранулярные привилегии

### 6.3 Почему Linux, а не BSD/Solaris?

Linux стал платформой для контейнеров благодаря:

- **Открытость**: Полностью open source

- **Модульность**: Отдельные механизмы можно комбинировать

- **Сообщество**: Активная разработка и поддержка

- **Облака**: Доминирование Linux в cloud-инфраструктуре

- **Экосистема**: Docker, Kubernetes изначально для Linux

---

## 7. LXC — Linux Containers

LXC (2008) — первая полноценная система контейнеризации для Linux, объединившая namespaces и cgroups.

### 7.1 Архитектура LXC

```
┌─────────────────────────────────────────┐
│              Host System                │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  │
│  │Container│  │Container│  │Container│  │
│  │   LXC   │  │   LXC   │  │   LXC   │  │
│  │  (PID,  │  │  (PID,  │  │  (PID,  │  │
│  │  NET,   │  │  NET,   │  │  NET,   │  │
│  │  MNT)   │  │  MNT)   │  │  MNT)   │  │
│  └─────────┘  └─────────┘  └─────────┘  │
├─────────────────────────────────────────┤
│           Linux Kernel                  │
│    (Namespaces + Cgroups + Seccomp)     │
└─────────────────────────────────────────┘
```

### 7.2 Работа с LXC

```bash
# Установка LXC

apt install lxc lxc-templates

# Создание контейнера

lxc-create -t download -n mycontainer -- \
    --dist ubuntu --release focal --arch amd64

# Запуск контейнера

lxc-start -n mycontainer

# Проверка статуса

lxc-info -n mycontainer
```

**Output:**
```
Name:           mycontainer
State:          RUNNING
PID:            12345
IP:             10.0.3.100
CPU use:        0.50 seconds
Memory use:     48.00 MiB
```

```bash
# Вход в контейнер

lxc-attach -n mycontainer

# Выполнение команды в контейнере

lxc-attach -n mycontainer -- ls -la /

# Остановка контейнера

lxc-stop -n mycontainer

# Удаление контейнера

lxc-destroy -n mycontainer
```

### 7.3 Конфигурация LXC

```bash
# /var/lib/lxc/mycontainer/config

# Базовые настройки

lxc.uts.name = mycontainer
lxc.arch = linux64

# Сеть

lxc.net.0.type = veth
lxc.net.0.link = lxcbr0
lxc.net.0.flags = up
lxc.net.0.hwaddr = 00:16:3e:xx:xx:xx

# Ограничение ресурсов (cgroups v1)

lxc.cgroup.memory.limit_in_bytes = 512M
lxc.cgroup.cpu.shares = 512

# Файловая система

lxc.rootfs.path = dir:/var/lib/lxc/mycontainer/rootfs

# Точки монтирования

lxc.mount.auto = proc:mixed sys:ro cgroup:mixed

# Capabilities

lxc.cap.drop = sys_admin net_admin
```

---

## 8. От LXC к Docker: революция в контейнеризации

Docker (2013) не изобрёл контейнеры, но радикально изменил способ их использования.

### 8.1 Что добавил Docker

| LXC | Docker |
|-----|--------|
| Контейнеры как мини-VM | Контейнеры как процессы |
| Сложная настройка | Простой CLI |
| Нет стандартизации образов | Docker Hub, image layers |
| Ручное управление | Dockerfile |
| Локальное использование | Экосистема для deployment |

### 8.2 Ключевые инновации Docker

**1. Image Layers:**
```
┌────────────────────────────┐
│      Application Code      │  ← Layer 4 (your code)
├────────────────────────────┤
│       pip packages         │  ← Layer 3 (dependencies)
├────────────────────────────┤
│         Python 3.11        │  ← Layer 2 (runtime)
├────────────────────────────┤
│       Debian Base          │  ← Layer 1 (base image)
└────────────────────────────┘
```

**2. Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

**3. Docker Hub:**

- Централизованный репозиторий образов
- Версионирование через теги
- Автоматическая сборка

### 8.3 Изначальная архитектура Docker

```
┌──────────────────────────────────────────┐
│                Docker CLI                │
│              docker run ...              │
└─────────────────┬────────────────────────┘
                  │ REST API
                  ▼
┌──────────────────────────────────────────┐
│            Docker Daemon                 │
│            (dockerd)                     │
│  ┌─────────────────────────────────────┐ │
│  │  Image Management                   │ │
│  │  Container Lifecycle                │ │
│  │  Network Management                 │ │
│  │  Volume Management                  │ │
│  └─────────────────────────────────────┘ │
└─────────────────┬────────────────────────┘
                  │ libcontainer (позже runc)
                  ▼
┌──────────────────────────────────────────┐
│              Linux Kernel                │
│      (namespaces, cgroups, etc.)         │
└──────────────────────────────────────────┘
```

---

## 9. Современный ландшафт контейнеризации

### 9.1 OCI — Open Container Initiative

В 2015 году Docker передал свой формат контейнеров в OCI, что привело к стандартизации:

- **OCI Runtime Specification** — как запускать контейнеры

- **OCI Image Specification** — формат образов

- **OCI Distribution Specification** — как распространять образы

### 9.2 Современная архитектура

```
┌─────────────────────────────────────────────────────────┐
│              High-Level Container Runtimes              │
│    ┌─────────┐  ┌──────────┐  ┌─────────┐  ┌──────────┐ │
│    │ Docker  │  │ Podman   │  │  CRI-O  │  │containerd│ │
│    └────┬────┘  └────┬─────┘  └────┬────┘  └────┬─────┘ │
└─────────┼────────────┼─────────────┼───────────┼────────┘
          │            │             │                              │
          ▼            ▼             ▼           ▼
┌─────────────────────────────────────────────────────────┐
│                Low-Level Container Runtime              │
│                       runc (OCI)                        │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│                      Linux Kernel                       │
│     Namespaces │ Cgroups │ Seccomp │ Capabilities       │
└─────────────────────────────────────────────────────────┘
```

### 9.3 Инструменты экосистемы

| Категория | Инструменты | Назначение |
|-----------|-------------|------------|
| Container Runtime | runc, crun | Запуск контейнеров |
| High-Level Runtime | containerd, CRI-O | Управление lifecycle |
| Container Engine | Docker, Podman | Полный стек для пользователя |
| Orchestration | Kubernetes, Swarm | Управление кластером |
| Image Build | Docker, Buildah, Kaniko | Создание образов |
| Registry | Docker Hub, Harbor, Quay | Хранение образов |

---

## 10. Что будет дальше в курсе

Этот курс построен по принципу "снизу вверх":

### 10.1 Структура курса

1. **Namespaces** — глубокое погружение в механизмы изоляции
2. **Cgroups** — управление ресурсами контейнеров
3. **Union Filesystems** — как работают слои образов
4. **OCI** — стандарты и низкоуровневые инструменты
5. **Container Runtimes** — containerd, podman, runc
6. **Networking** — сеть в контейнерах
7. **Docker** — практическая работа с Docker
8. **Docker Compose** — многоконтейнерные приложения
9. **Kubernetes** — оркестрация в production

### 10.2 Практический фокус

Каждый модуль включает:

- Теоретические основы
- Практические примеры
- Работу с реальными инструментами
- Понимание "как это работает внутри"

---

## 💡 Key Takeaways

- **chroot** — первый механизм изоляции, но небезопасен для production

- **FreeBSD Jails** и **Solaris Zones** — предшественники современных контейнеров

- **Linux контейнеры** — комбинация namespaces, cgroups и других механизмов ядра

- **Docker** революционизировал не технологию, а способ работы с контейнерами

- **OCI** стандартизировал экосистему, сделав её vendor-neutral

---

## 🚀 Next Steps

**Related Modules:**

- [Namespaces](../02_Namespaces/) — детальное изучение Linux namespaces
- [Cgroups](../03_Cgroups/) — управление ресурсами

**Practice Ideas:**

1. Создайте chroot-окружение с минимальным набором утилит
2. Попробуйте "сбежать" из chroot (в тестовой среде!)
3. Установите LXC и создайте первый контейнер
4. Сравните поведение процесса в chroot и LXC-контейнере

**Going Deeper:**

- История Unix и появление многопользовательских систем
- Виртуализация vs контейнеризация
- Kata Containers — гибрид VM и контейнеров

---

## 📚 Additional Resources

**Documentation:**

- [Linux kernel namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- [LXC documentation](https://linuxcontainers.org/lxc/documentation/)
- [OCI specifications](https://opencontainers.org/)

**Articles:**

- [A Brief History of Containers](https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016)
- [The History of Containers](https://www.redhat.com/en/blog/history-containers)

**Books:**

- "Container Security" by Liz Rice — глава 1-2 об основах
- "Docker Deep Dive" by Nigel Poulton — история и архитектура

---





