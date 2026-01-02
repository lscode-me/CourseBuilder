# OCI Standards
## Open Container Initiative и низкоуровневые инструменты

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать Linux namespaces и cgroups
- Знать основы работы с Docker
- Иметь представление о файловых системах контейнеров

**Recommended prior modules:**

- [Linux Namespaces](../02_Namespaces/)
- [Cgroups](../03_Cgroups/)
- [Union Filesystems](../04_FileSystem/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить структуру OCI спецификаций
- Использовать низкоуровневые инструменты: unshare, nsenter, runc
- Создавать OCI-совместимые bundles вручную
- Понимать как высокоуровневые инструменты используют OCI runtime

---

## 1. Open Container Initiative

OCI (Open Container Initiative) — организация, создающая открытые стандарты для контейнеров.

### 1.1 История OCI

| Год | Событие |
|-----|---------|
| 2013 | Docker выпускает первую версию |
| 2014 | CoreOS создаёт альтернативный runtime (rkt) |
| 2015 | Docker и CoreOS основывают OCI |
| 2015 | Docker передаёт libcontainer → runC |
| 2017 | OCI Runtime Spec v1.0, Image Spec v1.0 |
| 2021 | OCI Distribution Spec v1.0 |

### 1.2 Зачем нужна стандартизация

**До OCI:**

- Vendor lock-in (только Docker)
- Несовместимые форматы образов
- Разные способы запуска контейнеров

**После OCI:**

- Взаимозаменяемые runtime (runc, crun, kata, gvisor)
- Единый формат образов
- Портируемость между платформами

### 1.3 OCI спецификации

```
┌─────────────────────────────────────────────────────────┐
│                    OCI Specifications                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐               │
│  │  Runtime Spec   │  │   Image Spec    │               │
│  │                 │  │                 │               │
│  │  - config.json  │  │  - Layers       │               │
│  │  - Lifecycle    │  │  - Manifest     │               │
│  │  - Operations   │  │  - Config       │               │
│  └─────────────────┘  └─────────────────┘               │
│                                                         │
│  ┌─────────────────────────────────────────┐            │
│  │         Distribution Spec               │            │
│  │                                         │            │
│  │  - Registry API                         │            │
│  │  - Push/Pull operations                 │            │
│  └─────────────────────────────────────────┘            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 2. OCI Runtime Specification

Runtime Spec определяет как создавать и запускать контейнеры.

### 2.1 OCI Bundle

OCI Bundle — директория с файловой системой контейнера и конфигурацией:

```
mycontainer/
├── config.json      # Конфигурация контейнера
└── rootfs/          # Корневая файловая система
    ├── bin/
    ├── etc/
    ├── lib/
    ├── usr/
    └── ...
```

### 2.2 Структура config.json

```json
{
    "ociVersion": "1.0.2",
    "process": {
        "terminal": true,
        "user": {
            "uid": 0,
            "gid": 0
        },
        "args": [
            "/bin/sh"
        ],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "TERM=xterm"
        ],
        "cwd": "/",
        "capabilities": {
            "bounding": ["CAP_AUDIT_WRITE", "CAP_KILL", "CAP_NET_BIND_SERVICE"],
            "effective": ["CAP_AUDIT_WRITE", "CAP_KILL", "CAP_NET_BIND_SERVICE"],
            "permitted": ["CAP_AUDIT_WRITE", "CAP_KILL", "CAP_NET_BIND_SERVICE"]
        },
        "rlimits": [
            {
                "type": "RLIMIT_NOFILE",
                "hard": 1024,
                "soft": 1024
            }
        ]
    },
    "root": {
        "path": "rootfs",
        "readonly": false
    },
    "hostname": "mycontainer",
    "mounts": [
        {
            "destination": "/proc",
            "type": "proc",
            "source": "proc"
        },
        {
            "destination": "/dev",
            "type": "tmpfs",
            "source": "tmpfs",
            "options": ["nosuid", "strictatime", "mode=755", "size=65536k"]
        },
        {
            "destination": "/sys",
            "type": "sysfs",
            "source": "sysfs",
            "options": ["nosuid", "noexec", "nodev", "ro"]
        }
    ],
    "linux": {
        "namespaces": [
            {"type": "pid"},
            {"type": "network"},
            {"type": "ipc"},
            {"type": "uts"},
            {"type": "mount"}
        ],
        "resources": {
            "memory": {
                "limit": 536870912
            },
            "cpu": {
                "quota": 50000,
                "period": 100000
            }
        }
    }
}
```

### 2.3 Жизненный цикл контейнера

```
┌─────────┐    create    ┌─────────┐    start     ┌─────────┐
│ (none)  │ ──────────►  │ created │ ──────────►  │ running │
└─────────┘              └─────────┘              └─────────┘
                                                       │
                              ┌───────────────────────┘
                              │ exit/kill
                              ▼
                         ┌─────────┐    delete    ┌─────────┐
                         │ stopped │ ──────────►  │ (none)  │
                         └─────────┘              └─────────┘
```

**Операции:**

- `create` — создать контейнер (но не запускать процесс)
- `start` — запустить процесс контейнера
- `kill` — послать сигнал процессу
- `delete` — удалить контейнер

---

## 3. runC — референсный OCI runtime

runC — низкоуровневый runtime, создающий и запускающий контейнеры по OCI спецификации.

### 3.1 Установка runC

```bash
# Ubuntu/Debian

apt install runc

# Или скачать бинарник

curl -LO https://github.com/opencontainers/runc/releases/download/v1.1.9/runc.amd64
chmod +x runc.amd64
sudo mv runc.amd64 /usr/local/bin/runc

# Проверка версии

runc --version
```

**Output:**
```
runc version 1.1.9
commit: v1.1.9-0-gccaecfc
spec: 1.0.2-dev
go: go1.20.8
libseccomp: 2.5.4
```

### 3.2 Создание OCI bundle вручную

```bash
# Создаём структуру

mkdir -p mycontainer/rootfs

# Экспортируем rootfs из Docker-образа

docker export $(docker create alpine) | tar -C mycontainer/rootfs -xf -

# Генерируем config.json

cd mycontainer
runc spec

# Смотрим сгенерированный config

cat config.json | head -50
```

### 3.3 Запуск контейнера через runC

```bash
# Запуск интерактивного контейнера

sudo runc run mycontainer

# В другом терминале — проверяем статус

sudo runc list
```

**Output:**
```
ID            PID         STATUS      BUNDLE                    CREATED
mycontainer   12345       running     /home/user/mycontainer   2024-01-01T12:00:00Z
```

```bash
# Выполнение команды в работающем контейнере

sudo runc exec mycontainer ps aux

# Получение состояния

sudo runc state mycontainer
```

**Output:**
```json
{
  "ociVersion": "1.0.2",
  "id": "mycontainer",
  "pid": 12345,
  "status": "running",
  "bundle": "/home/user/mycontainer",
  "rootfs": "/home/user/mycontainer/rootfs",
  "created": "2024-01-01T12:00:00.000000000Z"
}
```

### 3.4 Операции runC

```bash
# Создать контейнер (без запуска)

sudo runc create -b /path/to/bundle mycontainer

# Запустить созданный контейнер

sudo runc start mycontainer

# Приостановить контейнер

sudo runc pause mycontainer

# Возобновить

sudo runc resume mycontainer

# Послать сигнал

sudo runc kill mycontainer SIGTERM

# Удалить

sudo runc delete mycontainer

# Удалить принудительно (если не остановлен)

sudo runc delete --force mycontainer
```

### 3.5 Минимальный config.json

```json
{
    "ociVersion": "1.0.2",
    "process": {
        "terminal": true,
        "user": {"uid": 0, "gid": 0},
        "args": ["/bin/sh"],
        "cwd": "/"
    },
    "root": {
        "path": "rootfs",
        "readonly": false
    },
    "linux": {
        "namespaces": [
            {"type": "pid"},
            {"type": "mount"}
        ]
    }
}
```

---

## 4. Инструменты для работы с namespaces

### 4.1 unshare — создание namespaces

`unshare` — утилита для запуска программы в новых namespaces.

```bash
# Справка

unshare --help
```

**Основные флаги:**

| Флаг | Namespace |
|------|-----------|
| -m, --mount | Mount |
| -u, --uts | UTS (hostname) |
| -i, --ipc | IPC |
| -n, --net | Network |
| -p, --pid | PID |
| -U, --user | User |
| -C, --cgroup | Cgroup |
| -T, --time | Time |

```bash
# Создание изолированного окружения

sudo unshare --mount --uts --ipc --net --pid --fork --mount-proc /bin/bash

# Внутри — проверяем изоляцию

hostname isolated-host
hostname  # isolated-host (не влияет на host)
ps aux    # видим только процессы namespace
ip link   # только loopback
```

### 4.2 Создание мини-контейнера через unshare

```bash
#!/bin/bash
# mini_container.sh

ROOTFS="${1:-/var/lib/containers/alpine}"
HOSTNAME="${2:-container}"

# Создаём все namespaces

exec unshare \
    --mount \
    --uts \
    --ipc \
    --net \
    --pid \
    --fork \
    --mount-proc \
    --root="$ROOTFS" \
    --wd=/ \
    /bin/sh -c "
        hostname $HOSTNAME
        exec /bin/sh
    "
```

### 4.3 nsenter — вход в существующие namespaces

`nsenter` позволяет войти в namespaces уже запущенного процесса.

```bash
# Вход во все namespaces процесса

sudo nsenter --target <PID> --all /bin/bash

# Вход в конкретные namespaces

sudo nsenter --target <PID> --mount --uts --ipc --net --pid /bin/bash

# Вход в namespace контейнера Docker

CONTAINER_PID=$(docker inspect --format '{{.State.Pid}}' mycontainer)
sudo nsenter --target $CONTAINER_PID --mount --uts --ipc --net --pid /bin/bash
```

### 4.4 Практический пример: отладка контейнера

```bash
# Запускаем "проблемный" контейнер

docker run -d --name debug-me alpine sleep 3600

# Получаем PID

PID=$(docker inspect --format '{{.State.Pid}}' debug-me)

# Входим в namespaces с инструментами с хоста
# Network namespace контейнера, но с mount namespace хоста

sudo nsenter --target $PID --net /bin/bash

# Теперь можем использовать tcpdump с хоста внутри сети контейнера

tcpdump -i eth0

# Или полный вход

sudo nsenter --target $PID --all /bin/sh
```

---

## 5. OCI Image Specification

Image Spec определяет формат образов контейнеров.

### 5.1 Структура OCI Image

```
image/
├── blobs/
│   └── sha256/
│       ├── <config-hash>        # Image config JSON
│       ├── <layer1-hash>        # Layer 1 (tar.gz)
│       ├── <layer2-hash>        # Layer 2 (tar.gz)
│       └── <manifest-hash>      # Image manifest
├── index.json                   # Image index
└── oci-layout                   # Version marker
```

### 5.2 Image Manifest

```json
{
    "schemaVersion": 2,
    "mediaType": "application/vnd.oci.image.manifest.v1+json",
    "config": {
        "mediaType": "application/vnd.oci.image.config.v1+json",
        "digest": "sha256:abc123...",
        "size": 1470
    },
    "layers": [
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "digest": "sha256:def456...",
            "size": 2789670
        },
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "digest": "sha256:ghi789...",
            "size": 1234567
        }
    ]
}
```

### 5.3 Image Config

```json
{
    "architecture": "amd64",
    "os": "linux",
    "config": {
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": ["/bin/sh"],
        "WorkingDir": "/",
        "Labels": {
            "maintainer": "example@example.com"
        }
    },
    "rootfs": {
        "type": "layers",
        "diff_ids": [
            "sha256:abc...",
            "sha256:def..."
        ]
    },
    "history": [
        {
            "created": "2024-01-01T00:00:00.000000000Z",
            "created_by": "/bin/sh -c #(nop) ADD file:... in /",
            "empty_layer": false
        }
    ]
}
```

### 5.4 Работа с образами через skopeo

```bash
# Установка skopeo

apt install skopeo

# Копирование образа в OCI layout

skopeo copy docker://alpine:latest oci:alpine-oci:latest

# Просмотр структуры

tree alpine-oci/
```

**Output:**
```
alpine-oci/
├── blobs
│   └── sha256
│       ├── 2b5c67...  # layer
│       ├── 7e01a0...  # config
│       └── c1aabb...  # manifest
├── index.json
└── oci-layout
```

```bash
# Просмотр index.json

cat alpine-oci/index.json | jq
```

**Output:**
```json
{
  "schemaVersion": 2,
  "manifests": [
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:c1aabb...",
      "size": 585,
      "annotations": {
        "org.opencontainers.image.ref.name": "latest"
      }
    }
  ]
}
```

### 5.5 Конвертация образов

```bash
# Docker → OCI

skopeo copy docker://nginx:alpine oci:nginx-oci:alpine

# OCI → Docker

skopeo copy oci:nginx-oci:alpine docker-daemon:nginx:from-oci

# Docker → файл

skopeo copy docker://alpine:latest docker-archive:alpine.tar

# Registry → Registry

skopeo copy docker://docker.io/library/nginx:latest \
    docker://myregistry.com/nginx:latest
```

---

## 6. OCI Distribution Specification

Distribution Spec определяет API для работы с registry.

### 6.1 Registry API endpoints

| Endpoint | Метод | Описание |
|----------|-------|----------|
| /v2/ | GET | Проверка версии API |
| /v2/<name>/manifests/<ref> | GET | Получить manifest |
| /v2/<name>/manifests/<ref> | PUT | Загрузить manifest |
| /v2/<name>/blobs/<digest> | GET | Получить blob (layer) |
| /v2/<name>/blobs/uploads/ | POST | Начать upload |
| /v2/<name>/tags/list | GET | Список тегов |

### 6.2 Работа с registry напрямую

```bash
# Получить токен для Docker Hub

TOKEN=$(curl -s "https://auth.docker.io/token?service=registry.docker.io&scope=repository:library/alpine:pull" | jq -r .token)

# Получить manifest

curl -s -H "Authorization: Bearer $TOKEN" \
    -H "Accept: application/vnd.oci.image.manifest.v1+json" \
    "https://registry-1.docker.io/v2/library/alpine/manifests/latest" | jq

# Получить список тегов

curl -s -H "Authorization: Bearer $TOKEN" \
    "https://registry-1.docker.io/v2/library/alpine/tags/list" | jq
```

### 6.3 Локальный OCI registry

```bash
# Запуск локального registry

docker run -d -p 5000:5000 --name registry registry:2

# Push образа в локальный registry

docker tag alpine:latest localhost:5000/alpine:latest
docker push localhost:5000/alpine:latest

# Список репозиториев

curl http://localhost:5000/v2/_catalog

# Теги образа

curl http://localhost:5000/v2/alpine/tags/list
```

---

## 7. Альтернативные OCI runtimes

### 7.1 crun — быстрый runtime на C

```bash
# Установка crun

apt install crun

# Использование

crun --version
```

**Output:**
```
crun version 1.8.5
commit: ...
rundir: /run/crun
spec: 1.0.0
```

**Преимущества crun:**

- Быстрее runC (написан на C, не Go)
- Меньше потребление памяти
- Совместим с OCI

### 7.2 Kata Containers — VM-based runtime

Kata Containers запускает каждый контейнер в легковесной VM:

```
┌─────────────────────────────────────────┐
│              Host System                │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐   │
│  │         Kata Runtime              │  │
│  │  ┌────────────────────────────┐  │   │
│  │  │    Lightweight VM (QEMU)   │  │   │
│  │  │  ┌──────────────────────┐  │  │   │
│  │  │  │   Container Process  │  │  │   │
│  │  │  └──────────────────────┘  │  │   │
│  │  │      Guest Kernel           │  │  │
│  │  └────────────────────────────┘  │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

**Когда использовать:**

- Требуется строгая изоляция
- Multi-tenant среды
- Запуск недоверенного кода

### 7.3 gVisor — userspace kernel

gVisor перехватывает системные вызовы и обрабатывает их в userspace:

```
┌─────────────────────────────────────────┐
│            Container Process            │
│         (thinks it talks to kernel)     │
└───────────────────┬─────────────────────┘
                    │ syscalls
                    ▼
┌─────────────────────────────────────────┐
│              Sentry (gVisor)            │
│        (implements kernel API)          │
└───────────────────┬─────────────────────┘
                    │ limited syscalls
                    ▼
┌─────────────────────────────────────────┐
│              Host Kernel                │
└─────────────────────────────────────────┘
```

**Когда использовать:**

- Запуск недоверенного кода
- Когда VM слишком тяжёлые
- Google Cloud Run использует gVisor

### 7.4 Сравнение runtimes

| Runtime | Изоляция | Производительность | Совместимость |
|---------|----------|-------------------|---------------|
| runc | Namespaces | Отличная | Полная |
| crun | Namespaces | Отличная+ | Полная |
| Kata | VM | Хорошая | Высокая |
| gVisor | Userspace | Средняя | Ограниченная |

---

## 8. Практика: создание контейнера с нуля

### 8.1 Подготовка rootfs

```bash
#!/bin/bash
# prepare_rootfs.sh

ROOTFS="mycontainer/rootfs"
mkdir -p "$ROOTFS"

# Вариант 1: из Docker

docker export $(docker create alpine) | tar -C "$ROOTFS" -xf -

# Вариант 2: из debootstrap (Debian/Ubuntu)
# sudo debootstrap --variant=minbase focal "$ROOTFS"

# Вариант 3: из архива Alpine
# curl -o alpine.tar.gz https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-minirootfs-3.18.0-x86_64.tar.gz
# tar -xzf alpine.tar.gz -C "$ROOTFS"
```

### 8.2 Создание config.json

```bash
#!/bin/bash
# create_config.sh

cat > mycontainer/config.json << 'EOF'
{
    "ociVersion": "1.0.2",
    "process": {
        "terminal": true,
        "user": {
            "uid": 0,
            "gid": 0
        },
        "args": ["/bin/sh"],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "TERM=xterm",
            "HOME=/root"
        ],
        "cwd": "/",
        "capabilities": {
            "bounding": [
                "CAP_CHOWN",
                "CAP_DAC_OVERRIDE",
                "CAP_FSETID",
                "CAP_FOWNER",
                "CAP_MKNOD",
                "CAP_NET_RAW",
                "CAP_SETGID",
                "CAP_SETUID",
                "CAP_SETFCAP",
                "CAP_SETPCAP",
                "CAP_NET_BIND_SERVICE",
                "CAP_SYS_CHROOT",
                "CAP_KILL",
                "CAP_AUDIT_WRITE"
            ],
            "effective": [
                "CAP_CHOWN",
                "CAP_DAC_OVERRIDE",
                "CAP_FSETID",
                "CAP_FOWNER",
                "CAP_MKNOD",
                "CAP_NET_RAW",
                "CAP_SETGID",
                "CAP_SETUID",
                "CAP_SETFCAP",
                "CAP_SETPCAP",
                "CAP_NET_BIND_SERVICE",
                "CAP_SYS_CHROOT",
                "CAP_KILL",
                "CAP_AUDIT_WRITE"
            ],
            "permitted": [
                "CAP_CHOWN",
                "CAP_DAC_OVERRIDE",
                "CAP_FSETID",
                "CAP_FOWNER",
                "CAP_MKNOD",
                "CAP_NET_RAW",
                "CAP_SETGID",
                "CAP_SETUID",
                "CAP_SETFCAP",
                "CAP_SETPCAP",
                "CAP_NET_BIND_SERVICE",
                "CAP_SYS_CHROOT",
                "CAP_KILL",
                "CAP_AUDIT_WRITE"
            ]
        },
        "rlimits": [
            {
                "type": "RLIMIT_NOFILE",
                "hard": 1024,
                "soft": 1024
            }
        ],
        "noNewPrivileges": true
    },
    "root": {
        "path": "rootfs",
        "readonly": false
    },
    "hostname": "mycontainer",
    "mounts": [
        {
            "destination": "/proc",
            "type": "proc",
            "source": "proc"
        },
        {
            "destination": "/dev",
            "type": "tmpfs",
            "source": "tmpfs",
            "options": ["nosuid", "strictatime", "mode=755", "size=65536k"]
        },
        {
            "destination": "/dev/pts",
            "type": "devpts",
            "source": "devpts",
            "options": ["nosuid", "noexec", "newinstance", "ptmxmode=0666", "mode=0620"]
        },
        {
            "destination": "/dev/shm",
            "type": "tmpfs",
            "source": "shm",
            "options": ["nosuid", "noexec", "nodev", "mode=1777", "size=65536k"]
        },
        {
            "destination": "/sys",
            "type": "sysfs",
            "source": "sysfs",
            "options": ["nosuid", "noexec", "nodev", "ro"]
        }
    ],
    "linux": {
        "resources": {
            "memory": {
                "limit": 268435456
            },
            "cpu": {
                "quota": 100000,
                "period": 100000
            },
            "pids": {
                "limit": 100
            }
        },
        "namespaces": [
            {"type": "pid"},
            {"type": "network"},
            {"type": "ipc"},
            {"type": "uts"},
            {"type": "mount"},
            {"type": "cgroup"}
        ],
        "maskedPaths": [
            "/proc/acpi",
            "/proc/kcore",
            "/proc/keys",
            "/proc/latency_stats",
            "/proc/timer_list",
            "/proc/timer_stats",
            "/proc/sched_debug",
            "/sys/firmware"
        ],
        "readonlyPaths": [
            "/proc/asound",
            "/proc/bus",
            "/proc/fs",
            "/proc/irq",
            "/proc/sys",
            "/proc/sysrq-trigger"
        ]
    }
}
EOF
```

### 8.3 Запуск и тестирование

```bash
cd mycontainer

# Запуск через runc

sudo runc run test-container

# В другом терминале

sudo runc list
sudo runc state test-container

# Exec в работающий контейнер

sudo runc exec test-container ls -la /

# Остановка

sudo runc kill test-container SIGKILL
sudo runc delete test-container
```

---

## 9. Интеграция с высокоуровневыми инструментами

### 9.1 Как Docker использует runC

```
┌──────────────────────────────────────────────────────┐
│                     docker CLI                       │
│                    docker run ...                    │
└─────────────────────────┬────────────────────────────┘
                          │ REST API
                          ▼
┌──────────────────────────────────────────────────────┐
│                      dockerd                         │
│                 (Docker Daemon)                      │
└─────────────────────────┬────────────────────────────┘
                          │ gRPC
                          ▼
┌──────────────────────────────────────────────────────┐
│                    containerd                        │
│            (Container Lifecycle Manager)             │
└─────────────────────────┬────────────────────────────┘
                          │ exec
                          ▼
┌──────────────────────────────────────────────────────┐
│                containerd-shim                       │
│            (Per-container process)                   │
└─────────────────────────┬────────────────────────────┘
                          │ exec
                          ▼
┌──────────────────────────────────────────────────────┐
│                       runc                           │
│                  (OCI Runtime)                       │
└──────────────────────────────────────────────────────┘
```

### 9.2 Смена runtime в Docker

```bash
# Конфигурация Docker для использования crun

cat > /etc/docker/daemon.json << EOF
{
    "default-runtime": "crun",
    "runtimes": {
        "crun": {
            "path": "/usr/bin/crun"
        },
        "kata": {
            "path": "/usr/bin/kata-runtime"
        }
    }
}
EOF

systemctl restart docker

# Запуск с конкретным runtime

docker run --runtime=crun alpine echo "Hello from crun"
docker run --runtime=kata alpine echo "Hello from Kata VM"
```

---

## 💡 Key Takeaways

- **OCI** стандартизирует runtime, images и distribution — обеспечивая переносимость

- **runC** — референсная реализация OCI runtime, используется Docker, containerd, CRI-O

- **OCI Bundle** = rootfs + config.json — всё необходимое для запуска контейнера

- **unshare/nsenter** — низкоуровневые инструменты для работы с namespaces

- **Альтернативные runtime** (Kata, gVisor) обеспечивают дополнительную изоляцию

---

## 🚀 Next Steps

**Related Modules:**

- [Container Runtimes](../06_Runtimes/) — containerd, Podman, CRI-O
- [Docker](../08_Docker/) — практическая работа с Docker

**Practice Ideas:**

1. Создайте OCI bundle вручную и запустите через runC
2. Используйте skopeo для анализа структуры образов
3. Настройте Docker для использования crun
4. Войдите в namespaces контейнера через nsenter

**Going Deeper:**

- OCI Artifacts для хранения не только образов
- Image signing и verification
- WASM в OCI (WebAssembly как формат)

---

## 📚 Additional Resources

**Documentation:**

- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)
- [OCI Image Specification](https://github.com/opencontainers/image-spec)
- [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)
- [runC documentation](https://github.com/opencontainers/runc)

**Tools:**

- [skopeo](https://github.com/containers/skopeo) — работа с образами
- [umoci](https://github.com/opencontainers/umoci) — модификация OCI images
- [dive](https://github.com/wagoodman/dive) — анализ слоёв

**Articles:**

- [Understanding the OCI Runtime Specification](https://www.tutorialworks.com/container-runtime/)
- [From Docker to OCI](https://blog.aquasec.com/oci-container-format)

---





