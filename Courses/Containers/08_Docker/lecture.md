# Docker
## Практическая работа с контейнерами

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Linux namespaces и cgroups
- Знать принципы работы container runtimes
- Иметь представление о сетевой подсистеме контейнеров

**Recommended prior modules:**

- [Container Runtimes](../06_Runtimes/)
- [Container Networking](../07_Networking/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Эффективно работать с Docker CLI
- Создавать оптимизированные Docker образы
- Управлять данными через volumes и bind mounts
- Настраивать Docker daemon

---

## 1. Docker CLI — основы

### 1.1 Структура команд

```bash
docker [OPTIONS] COMMAND [ARG...]

# Примеры

docker run nginx                    # Запуск контейнера
docker container run nginx          # Явный синтаксис
docker image pull nginx             # Скачивание образа
```

### 1.2 Работа с образами

```bash
# Скачивание образа

docker pull nginx:1.25-alpine

# Список локальных образов

docker images
docker image ls
```

**Output:**
```
REPOSITORY   TAG           IMAGE ID       CREATED       SIZE
nginx        1.25-alpine   a2d5e8c4f8b2   2 weeks ago   43.3MB
alpine       latest        05455a08881e   4 weeks ago   7.34MB
```

```bash
# Информация об образе

docker image inspect nginx:1.25-alpine

# История слоёв

docker history nginx:1.25-alpine

# Удаление образов

docker rmi nginx:1.25-alpine
docker image prune -a  # Удалить все неиспользуемые
```

### 1.3 Запуск контейнеров

```bash
# Базовый запуск

docker run nginx

# С параметрами

docker run -d \                      # Detached mode
    --name webserver \               # Имя контейнера
    -p 8080:80 \                     # Port mapping
    -e NGINX_HOST=example.com \      # Environment variable
    -v /data:/usr/share/nginx/html \ # Volume mount
    --restart unless-stopped \       # Restart policy
    nginx:1.25-alpine

# Интерактивный режим

docker run -it --rm alpine sh        # -it = interactive + tty, --rm = удалить после выхода
```

### 1.4 Управление контейнерами

```bash
# Список контейнеров

docker ps           # Запущенные
docker ps -a        # Все
docker ps -q        # Только ID

# Операции с контейнером

docker stop webserver
docker start webserver
docker restart webserver
docker pause webserver
docker unpause webserver

# Удаление

docker rm webserver
docker rm -f webserver              # Принудительно (stop + rm)
docker container prune              # Удалить остановленные
```

### 1.5 Выполнение команд в контейнере

```bash
# Exec в запущенный контейнер

docker exec -it webserver sh
docker exec webserver nginx -t     # Проверка конфига nginx

# Просмотр логов

docker logs webserver
docker logs -f webserver           # Follow mode
docker logs --tail 100 webserver   # Последние 100 строк
docker logs --since 1h webserver   # За последний час

# Копирование файлов

docker cp ./config.conf webserver:/etc/nginx/
docker cp webserver:/var/log/nginx/access.log ./
```

### 1.6 Информация о контейнере

```bash
# Детальная информация

docker inspect webserver

# Конкретные поля

docker inspect -f '{{.State.Status}}' webserver
docker inspect -f '{{.NetworkSettings.IPAddress}}' webserver
docker inspect -f '{{json .Config.Env}}' webserver | jq

# Использование ресурсов

docker stats
docker stats --no-stream webserver
docker top webserver               # Процессы внутри
```

---

## 2. Dockerfile — создание образов

### 2.1 Структура Dockerfile

```dockerfile
# Базовый образ

FROM python:3.11-slim

# Метаданные

LABEL maintainer="dev@example.com"
LABEL version="1.0"

# Environment variables

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

# Рабочая директория

WORKDIR $APP_HOME

# Установка зависимостей (отдельный слой для кеширования)

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода

COPY . .

# Создание пользователя

RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Открытие порта

EXPOSE 8000

# Health check

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Команда запуска

CMD ["python", "app.py"]
```

### 2.2 Инструкции Dockerfile

| Инструкция | Назначение |
|------------|------------|
| FROM | Базовый образ |
| RUN | Выполнить команду (создаёт слой) |
| COPY | Копировать файлы в образ |
| ADD | COPY + распаковка архивов + URL |
| WORKDIR | Рабочая директория |
| ENV | Переменные окружения |
| ARG | Build-time переменные |
| EXPOSE | Документирование портов |
| USER | Пользователь для запуска |
| ENTRYPOINT | Главная команда |
| CMD | Аргументы по умолчанию |
| HEALTHCHECK | Проверка здоровья |
| VOLUME | Точка монтирования |

### 2.3 ENTRYPOINT vs CMD

```dockerfile
# CMD — может быть переопределён

FROM alpine
CMD ["echo", "Hello"]
# docker run myimage         → Hello
# docker run myimage World   → World

# ENTRYPOINT — фиксированная команда

FROM alpine
ENTRYPOINT ["echo"]
CMD ["Hello"]
# docker run myimage         → Hello
# docker run myimage World   → World

# Комбинация

FROM alpine
ENTRYPOINT ["python", "app.py"]
CMD ["--port", "8000"]
# docker run myimage                     → python app.py --port 8000
# docker run myimage --port 9000         → python app.py --port 9000
```

### 2.4 Сборка образа

```bash
# Базовая сборка

docker build -t myapp:1.0 .

# С контекстом из другой директории

docker build -t myapp:1.0 -f Dockerfile.prod ./src

# С build arguments

docker build --build-arg VERSION=1.0 -t myapp:1.0 .

# Без кеша

docker build --no-cache -t myapp:1.0 .

# С выводом build logs

docker build --progress=plain -t myapp:1.0 .
```

---

## 3. Multi-stage builds

### 3.1 Концепция

Multi-stage builds позволяют использовать несколько FROM в одном Dockerfile:

```dockerfile
# Stage 1: Build

FROM golang:1.21 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

# Stage 2: Production

FROM alpine:3.18
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/server .
EXPOSE 8080
CMD ["./server"]
```

### 3.2 Преимущества

```bash
# Размер без multi-stage (с Go toolchain)

golang:1.21   # ~800MB

# Размер с multi-stage

alpine + binary   # ~15MB
```

### 3.3 Несколько build stages

```dockerfile
# Base stage

FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./

# Dependencies stage

FROM base AS deps
RUN npm ci

# Build stage

FROM deps AS build
COPY . .
RUN npm run build

# Test stage

FROM build AS test
RUN npm test

# Production stage

FROM node:20-alpine AS production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/index.js"]
```

```bash
# Сборка до определённого stage

docker build --target test -t myapp:test .
docker build --target production -t myapp:prod .
```

---

## 4. Оптимизация образов

### 4.1 Минимизация размера

```dockerfile
# Плохо

FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install flask
RUN apt-get clean

# Хорошо

FROM python:3.11-slim
RUN pip install --no-cache-dir flask
```

### 4.2 Оптимизация кеширования

```dockerfile
# Плохо: любое изменение кода инвалидирует pip install

COPY . /app
RUN pip install -r requirements.txt

# Хорошо: pip install кешируется пока requirements.txt не меняется

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
```

### 4.3 Уменьшение количества слоёв

```dockerfile
# Плохо: 4 слоя

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean

# Хорошо: 1 слой

RUN apt-get update && \
    apt-get install -y \
        curl \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

### 4.4 .dockerignore

```gitignore
# .dockerignore

.git
.gitignore
Dockerfile
docker-compose.yml
*.md
__pycache__
*.pyc
.env
.venv
node_modules
.npm
dist
build
*.log
.DS_Store
```

### 4.5 Выбор базового образа

| Образ | Размер | Использование |
|-------|--------|---------------|
| scratch | 0MB | Статические бинарники |
| alpine | 7MB | Минимальный Linux |
| distroless | 20MB | Security, без shell |
| debian-slim | 80MB | Совместимость |
| ubuntu | 80MB | Полноценный Linux |

---

## 5. Volumes и Bind Mounts

### 5.1 Типы хранения

```
┌─────────────────────────────────────────────────────────┐
│                     Container                           │
│  ┌────────────────────────────────────────────────────┐ │
│  │              Container Layer (writable)            │ │
│  └────────────────────────────────────────────────────┘ │
│         │               │                │              │
│    ┌────▼────┐    ┌─────▼─────┐    ┌─────▼─────┐        │
│    │ Volume  │    │Bind Mount │    │   tmpfs   │        │
│    │/var/lib │    │ /host/dir │    │  (RAM)    │        │
│    │/docker/ │    │           │    │           │        │
│    │volumes  │    │           │    │           │        │
│    └─────────┘    └───────────┘    └───────────┘        │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Docker Volumes

```bash
# Создание volume

docker volume create mydata

# Список volumes

docker volume ls

# Использование

docker run -d \
    --name db \
    -v mydata:/var/lib/postgresql/data \
    postgres:15

# Анонимный volume

docker run -d -v /data nginx

# Информация

docker volume inspect mydata

# Удаление

docker volume rm mydata
docker volume prune  # Удалить неиспользуемые
```

### 5.3 Bind Mounts

```bash
# Монтирование директории хоста

docker run -d \
    --name dev \
    -v $(pwd)/src:/app/src \
    -v $(pwd)/config.yaml:/app/config.yaml:ro \
    myapp:dev

# Read-only mount

docker run -d \
    -v /etc/localtime:/etc/localtime:ro \
    nginx

# С новым синтаксисом --mount

docker run -d \
    --mount type=bind,source=$(pwd)/src,target=/app/src \
    --mount type=bind,source=$(pwd)/config.yaml,target=/app/config.yaml,readonly \
    myapp:dev
```

### 5.4 tmpfs Mounts

```bash
# Данные в RAM (не сохраняются)

docker run -d \
    --tmpfs /tmp:rw,size=100m,mode=1777 \
    --tmpfs /run:rw \
    myapp
```

### 5.5 Volume drivers

```bash
# Локальный драйвер с NFS

docker volume create \
    --driver local \
    --opt type=nfs \
    --opt o=addr=192.168.1.100,rw \
    --opt device=:/export/data \
    nfs-data
```

---

## 6. Docker Registry

### 6.1 Работа с Docker Hub

```bash
# Логин

docker login

# Push образа

docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0

# Pull

docker pull username/myapp:1.0
```

### 6.2 Private Registry

```bash
# Запуск локального registry

docker run -d \
    -p 5000:5000 \
    --name registry \
    -v /data/registry:/var/lib/registry \
    registry:2

# Push в локальный registry

docker tag myapp:1.0 localhost:5000/myapp:1.0
docker push localhost:5000/myapp:1.0

# Pull

docker pull localhost:5000/myapp:1.0
```

### 6.3 Registry с аутентификацией

```bash
# Создание htpasswd

mkdir -p /auth
docker run --rm \
    --entrypoint htpasswd \
    httpd:2 -Bbn admin password > /auth/htpasswd

# Registry с auth

docker run -d \
    -p 5000:5000 \
    --name registry \
    -v /auth:/auth \
    -e "REGISTRY_AUTH=htpasswd" \
    -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
    -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" \
    registry:2
```

---

## 7. Docker Daemon Configuration

### 7.1 daemon.json

```json
// /etc/docker/daemon.json
{
    "data-root": "/var/lib/docker",
    "storage-driver": "overlay2",
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "10m",
        "max-file": "3"
    },
    "default-address-pools": [
        {"base": "172.30.0.0/16", "size": 24}
    ],
    "dns": ["8.8.8.8", "8.8.4.4"],
    "insecure-registries": ["registry.local:5000"],
    "registry-mirrors": ["https://mirror.gcr.io"],
    "live-restore": true,
    "default-runtime": "runc",
    "runtimes": {
        "crun": {
            "path": "/usr/bin/crun"
        }
    },
    "exec-opts": ["native.cgroupdriver=systemd"],
    "features": {
        "buildkit": true
    }
}
```

### 7.2 Применение конфигурации

```bash
# Проверка синтаксиса

cat /etc/docker/daemon.json | jq

# Перезапуск Docker

sudo systemctl restart docker

# Или reload (если поддерживается)

sudo systemctl reload docker
```

### 7.3 Logging drivers

```bash
# Доступные драйверы: json-file, syslog, journald, fluentd, awslogs, etc.

# Запуск с конкретным драйвером

docker run -d \
    --log-driver syslog \
    --log-opt syslog-address=udp://localhost:514 \
    nginx

# С json-file и лимитами

docker run -d \
    --log-driver json-file \
    --log-opt max-size=10m \
    --log-opt max-file=3 \
    nginx
```

---

## 8. Resource Limits

### 8.1 CPU Limits

```bash
# Ограничение CPU

docker run -d \
    --cpus="1.5" \                   # 1.5 CPU
    --cpu-shares=512 \               # Относительный вес
    --cpuset-cpus="0,1" \            # Конкретные ядра
    myapp
```

### 8.2 Memory Limits

```bash
# Ограничение памяти

docker run -d \
    --memory="512m" \                # Hard limit
    --memory-reservation="256m" \    # Soft limit
    --memory-swap="1g" \             # Memory + swap
    --oom-kill-disable \             # Отключить OOM killer
    myapp
```

### 8.3 I/O Limits

```bash
# Ограничение I/O

docker run -d \
    --device-read-bps=/dev/sda:10mb \
    --device-write-bps=/dev/sda:5mb \
    --device-read-iops=/dev/sda:1000 \
    --device-write-iops=/dev/sda:500 \
    myapp
```

### 8.4 PIDs Limit

```bash
# Ограничение количества процессов

docker run -d --pids-limit=100 myapp
```

---

## 9. Security

### 9.1 Запуск от non-root

```dockerfile
FROM node:20-alpine

# Создаём пользователя

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app
COPY --chown=appuser:appgroup . .

# Переключаемся на пользователя

USER appuser

CMD ["node", "index.js"]
```

### 9.2 Read-only root filesystem

```bash
docker run -d \
    --read-only \
    --tmpfs /tmp \
    --tmpfs /run \
    nginx
```

### 9.3 Capabilities

```bash
# Удаление всех capabilities

docker run --cap-drop=ALL nginx

# Добавление только нужных

docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx
```

### 9.4 Seccomp profiles

```bash
# С дефолтным профилем

docker run --security-opt seccomp=default.json nginx

# Без seccomp (не рекомендуется)

docker run --security-opt seccomp=unconfined nginx
```

### 9.5 AppArmor

```bash
# С конкретным профилем

docker run --security-opt apparmor=docker-nginx nginx

# Без AppArmor

docker run --security-opt apparmor=unconfined nginx
```

---

## 10. Практические паттерны

### 10.1 Healthcheck pattern

```dockerfile
FROM nginx:alpine

# Установка curl для healthcheck

RUN apk add --no-cache curl

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
```

```bash
# Проверка health status

docker inspect --format='{{.State.Health.Status}}' mycontainer
```

### 10.2 Init process

```bash
# Использование init для правильной обработки сигналов

docker run --init myapp

# Или tini в Dockerfile

FROM alpine
RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["myapp"]
```

### 10.3 Graceful shutdown

```dockerfile
FROM python:3.11-slim

COPY app.py .

# SIGTERM по умолчанию, 10 секунд на завершение

STOPSIGNAL SIGTERM
CMD ["python", "app.py"]
```

```bash
# Увеличение времени на остановку

docker stop --time=30 mycontainer
```

### 10.4 Development vs Production

```dockerfile
# Dockerfile.dev

FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--debug"]

# Dockerfile (production)

FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . .
USER nobody
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

---

## 💡 Key Takeaways

- **Docker CLI** имеет новый синтаксис (docker container, docker image) и старый (docker run, docker pull)

- **Multi-stage builds** значительно уменьшают размер production образов

- **Порядок инструкций** в Dockerfile критичен для кеширования

- **Volumes** предпочтительнее bind mounts для production данных

- **Security** требует non-root user, capabilities drop, read-only fs

---

## 🚀 Next Steps

**Related Modules:**

- [Docker Compose](../09_Compose/) — multi-container applications
- [Kubernetes](../10_Kubernetes/) — оркестрация

**Practice Ideas:**

1. Создайте multi-stage Dockerfile для вашего приложения
2. Настройте healthcheck и graceful shutdown
3. Оптимизируйте размер образа с помощью .dockerignore
4. Настройте private registry с аутентификацией

**Going Deeper:**

- BuildKit advanced features
- Docker Content Trust для подписи образов
- Docker contexts для remote Docker hosts

---

## 📚 Additional Resources

**Documentation:**

- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

**Tools:**

- [dive](https://github.com/wagoodman/dive) — анализ слоёв
- [hadolint](https://github.com/hadolint/hadolint) — линтер Dockerfile
- [docker-slim](https://github.com/slimtoolkit/slim) — оптимизация образов

**Articles:**

- [Docker Security Best Practices](https://snyk.io/blog/10-docker-image-security-best-practices/)
- [Optimizing Docker Images](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)

---





