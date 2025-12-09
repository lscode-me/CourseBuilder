# Container Runtimes
## containerd, Podman, CRI-O и архитектура демонов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать OCI спецификации и runC
- Знать основы namespaces и cgroups
- Иметь опыт работы с Docker

**Recommended prior modules:**
- [OCI Standards](../05_OCI/) — основы OCI
- [Namespaces](../02_Namespaces/) и [Cgroups](../03_Cgroups/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать high-level и low-level container runtimes
- Работать с containerd напрямую через ctr и nerdctl
- Использовать Podman как альтернативу Docker
- Понимать архитектуру современных container engines

---

## 1. Иерархия Container Runtimes

### 1.1 Уровни абстракции

```
┌─────────────────────────────────────────────────────────────┐
│                    Container Engines                         │
│              (Docker, Podman, nerdctl)                       │
│         Удобный CLI, сборка образов, networking              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               High-Level Container Runtimes                  │
│              (containerd, CRI-O)                             │
│         Image management, lifecycle, CRI for K8s             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               Low-Level Container Runtimes                   │
│              (runc, crun, kata, gvisor)                      │
│         Непосредственный запуск контейнеров (OCI)            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Linux Kernel                            │
│              (namespaces, cgroups, seccomp)                  │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Сравнение компонентов

| Уровень | Компоненты | Функции |
|---------|------------|---------|
| Engine | Docker, Podman | CLI, build, compose, UX |
| High-level | containerd, CRI-O | Lifecycle, images, CRI |
| Low-level | runc, crun | Создание контейнеров |
| Kernel | Linux | Изоляция, ресурсы |

---

## 2. containerd

containerd — промышленный container runtime, используемый Docker и Kubernetes.

### 2.1 Архитектура containerd

```
┌────────────────────────────────────────────────────────────┐
│                       containerd                            │
├────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Images  │  │Containers│  │  Tasks   │  │ Content  │   │
│  │  Service │  │ Service  │  │ Service  │  │  Store   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Snapshots │  │   Diff   │  │  Events  │  │ Metrics  │   │
│  │ Service  │  │ Service  │  │ Service  │  │ Service  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├────────────────────────────────────────────────────────────┤
│                     Plugins/Shims                          │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              containerd-shim-runc-v2                 │  │
│  └─────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### 2.2 Установка containerd

```bash
# Ubuntu/Debian
apt update && apt install -y containerd

# Или из релизов
VERSION="1.7.8"
curl -LO https://github.com/containerd/containerd/releases/download/v${VERSION}/containerd-${VERSION}-linux-amd64.tar.gz
tar -xzf containerd-${VERSION}-linux-amd64.tar.gz -C /usr/local

# Настройка systemd
curl -LO https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
mv containerd.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now containerd
```

### 2.3 Конфигурация containerd

```bash
# Генерация дефолтной конфигурации
containerd config default > /etc/containerd/config.toml

# Основные параметры
cat /etc/containerd/config.toml
```

```toml
# /etc/containerd/config.toml
version = 2

[plugins]
  [plugins."io.containerd.grpc.v1.cri"]
    sandbox_image = "registry.k8s.io/pause:3.9"
    
    [plugins."io.containerd.grpc.v1.cri".containerd]
      default_runtime_name = "runc"
      
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]
        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
          runtime_type = "io.containerd.runc.v2"
          
          [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
            SystemdCgroup = true

  [plugins."io.containerd.snapshotter.v1.overlayfs"]
    root_path = "/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs"
```

### 2.4 Работа с ctr

`ctr` — CLI для containerd (низкоуровневый, для отладки):

```bash
# Pull образа
ctr images pull docker.io/library/alpine:latest

# Список образов
ctr images list
```

**Output:**
```
REF                            TYPE                                                 DIGEST      SIZE
docker.io/library/alpine:latest application/vnd.docker.distribution.manifest.v2+json sha256:... 3.2 MiB
```

```bash
# Запуск контейнера
ctr run --rm -t docker.io/library/alpine:latest mycontainer /bin/sh

# Создание контейнера (без запуска)
ctr container create docker.io/library/alpine:latest mycontainer

# Запуск task (процесса)
ctr task start -d mycontainer

# Exec в контейнер
ctr task exec --exec-id exec1 -t mycontainer /bin/sh

# Список контейнеров
ctr containers list

# Список tasks
ctr tasks list

# Удаление
ctr task kill mycontainer
ctr task delete mycontainer
ctr container delete mycontainer
```

### 2.5 Namespaces в containerd

containerd использует собственные namespaces (не Linux namespaces!) для изоляции:

```bash
# Список namespaces
ctr namespaces list
```

**Output:**
```
NAME    LABELS
default
k8s.io
moby
```

```bash
# Работа в конкретном namespace
ctr -n k8s.io containers list
ctr -n moby containers list  # Docker контейнеры
```

---

## 3. nerdctl — Docker-совместимый CLI для containerd

nerdctl предоставляет Docker-совместимый интерфейс для containerd.

### 3.1 Установка nerdctl

```bash
# Скачиваем полную версию (с buildkit и CNI)
VERSION="1.7.0"
curl -LO https://github.com/containerd/nerdctl/releases/download/v${VERSION}/nerdctl-full-${VERSION}-linux-amd64.tar.gz
tar -xzf nerdctl-full-${VERSION}-linux-amd64.tar.gz -C /usr/local

# Проверка
nerdctl version
```

### 3.2 Использование nerdctl

```bash
# Почти как Docker!
nerdctl run --rm -it alpine sh

# Pull
nerdctl pull nginx:alpine

# Build
nerdctl build -t myimage:latest .

# Compose
nerdctl compose up -d

# Список контейнеров
nerdctl ps -a

# Логи
nerdctl logs mycontainer
```

### 3.3 Отличия от Docker

| Функция | nerdctl | Docker |
|---------|---------|--------|
| Rootless | Встроенный | Отдельная настройка |
| Lazy pulling | Поддержка | Нет |
| P2P image distribution | Поддержка | Нет |
| Build backend | BuildKit | BuildKit/legacy |

```bash
# Rootless mode
containerd-rootless-setuptool.sh install
nerdctl run --rm alpine cat /etc/os-release
```

---

## 4. CRI-O

CRI-O — container runtime специально для Kubernetes.

### 4.1 Архитектура CRI-O

```
┌─────────────────────────────────────────────────────────┐
│                      Kubernetes                          │
│                        kubelet                           │
└─────────────────────────┬───────────────────────────────┘
                          │ CRI (gRPC)
                          ▼
┌─────────────────────────────────────────────────────────┐
│                        CRI-O                             │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ Image Pull  │  │  Container  │  │   Network   │     │
│  │   (skopeo)  │  │  Lifecycle  │  │    (CNI)    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              conmon (Container Monitor)                  │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  OCI Runtime (runc)                      │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Особенности CRI-O

- **Минимализм** — только то, что нужно для Kubernetes
- **Стабильность** — версионирование синхронизировано с K8s
- **Безопасность** — меньше attack surface
- **Производительность** — оптимизирован для K8s workloads

### 4.3 Конфигурация CRI-O

```bash
# /etc/crio/crio.conf

[crio.runtime]
default_runtime = "runc"
conmon = "/usr/bin/conmon"
conmon_cgroup = "system.slice"

[crio.runtime.runtimes.runc]
runtime_path = "/usr/bin/runc"
runtime_type = "oci"
runtime_root = "/run/runc"

[crio.image]
pause_image = "registry.k8s.io/pause:3.9"

[crio.network]
network_dir = "/etc/cni/net.d/"
plugin_dirs = ["/opt/cni/bin/"]
```

### 4.4 Инструменты CRI-O

```bash
# crictl — CLI для CRI-совместимых runtime
crictl --runtime-endpoint unix:///var/run/crio/crio.sock ps
crictl images
crictl logs <container-id>
crictl exec -it <container-id> /bin/sh

# Проверка конфигурации
crio config --default
```

---

## 5. Podman

Podman — daemonless container engine, совместимый с Docker.

### 5.1 Архитектура Podman

```
┌─────────────────────────────────────────────────────────┐
│                     podman CLI                           │
│                                                          │
│   ┌─────────────────────────────────────────────────┐   │
│   │              libpod (library)                    │   │
│   │  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │   │
│   │  │ Containers│  │  Images  │  │   Pods       │   │   │
│   │  └──────────┘  └──────────┘  └──────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────┘
                          │
           ┌──────────────┼──────────────┐
           │              │              │
           ▼              ▼              ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ conmon   │   │ Buildah  │   │ skopeo   │
    │(monitor) │   │ (build)  │   │(images)  │
    └──────────┘   └──────────┘   └──────────┘
           │
           ▼
    ┌──────────────────────────────────────┐
    │          OCI Runtime (runc/crun)      │
    └──────────────────────────────────────┘
```

### 5.2 Ключевые отличия от Docker

| Аспект | Docker | Podman |
|--------|--------|--------|
| Daemon | dockerd | Нет daemon |
| Rootless | Сложная настройка | Из коробки |
| Socket | /var/run/docker.sock | Нет (или user socket) |
| Pods | Нет | Поддержка |
| systemd | Ограниченная | Полная интеграция |
| CLI | docker | podman (совместим) |

### 5.3 Установка Podman

```bash
# Ubuntu/Debian
apt install podman

# Fedora/RHEL
dnf install podman

# Проверка
podman version
```

**Output:**
```
Client:       Podman Engine
Version:      4.6.1
API Version:  4.6.1
Go Version:   go1.20.6
Built:        Thu Aug 10 15:00:00 2023
OS/Arch:      linux/amd64
```

### 5.4 Использование Podman

```bash
# Идентичный Docker синтаксис
podman pull alpine
podman run --rm -it alpine sh
podman images
podman ps -a

# Совместимость через alias
alias docker=podman
docker run --rm alpine echo "Hello"
```

### 5.5 Rootless Podman

```bash
# Работает от обычного пользователя!
podman run --rm alpine whoami

# Где хранятся данные
echo $HOME/.local/share/containers
ls ~/.local/share/containers/storage/

# Конфигурация
cat ~/.config/containers/registries.conf
```

### 5.6 Pods в Podman

Podman поддерживает концепцию Pod из Kubernetes:

```bash
# Создание pod
podman pod create --name mypod -p 8080:80

# Добавление контейнеров в pod
podman run -d --pod mypod --name web nginx
podman run -d --pod mypod --name app python:alpine sleep 3600

# Список pods
podman pod list
```

**Output:**
```
POD ID        NAME    STATUS   CREATED        INFRA ID      # OF CONTAINERS
abc123def456  mypod   Running  5 seconds ago  def456abc789  3
```

```bash
# Контейнеры в pod разделяют network namespace
podman exec app curl localhost:80

# Генерация Kubernetes YAML из pod
podman generate kube mypod > mypod.yaml
```

### 5.7 Интеграция с systemd

```bash
# Генерация systemd unit
podman generate systemd --new --name mycontainer > ~/.config/systemd/user/mycontainer.service

# Активация
systemctl --user daemon-reload
systemctl --user enable --now mycontainer

# Quadlet — современный способ (Podman 4.4+)
cat > ~/.config/containers/systemd/myapp.container << EOF
[Container]
Image=docker.io/library/nginx:alpine
PublishPort=8080:80

[Service]
Restart=always

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user start myapp
```

---

## 6. Buildah — создание образов

Buildah — инструмент для создания OCI-совместимых образов без daemon.

### 6.1 Buildah vs Docker build

| Аспект | docker build | buildah |
|--------|--------------|---------|
| Daemon | Требуется | Нет |
| Rootless | Сложно | Легко |
| Dockerfile | Да | Да + scripting |
| Shell scripting | Нет | Да |
| Fine control | Ограничен | Полный |

### 6.2 Использование Buildah

```bash
# Создание контейнера из образа
container=$(buildah from alpine)

# Выполнение команд
buildah run $container -- apk add python3

# Копирование файлов
buildah copy $container ./app /app

# Настройка metadata
buildah config --cmd "/app/start.sh" $container
buildah config --env "APP_ENV=production" $container

# Коммит в образ
buildah commit $container myapp:latest

# Push
buildah push myapp:latest docker://registry.example.com/myapp:latest
```

### 6.3 Buildah с Dockerfile

```bash
# Стандартная сборка
buildah bud -t myimage:latest .

# С альтернативным файлом
buildah bud -f Dockerfile.prod -t myimage:prod .
```

### 6.4 Scripted builds

```bash
#!/bin/bash
# build.sh — программная сборка образа

container=$(buildah from golang:1.21-alpine)

# Устанавливаем зависимости
buildah run $container -- apk add --no-cache git

# Монтируем исходники
buildah copy $container . /src

# Компилируем
buildah config --workingdir /src $container
buildah run $container -- go build -o /app/server .

# Создаём финальный образ (multi-stage)
final=$(buildah from alpine:3.18)
buildah run $final -- apk add --no-cache ca-certificates
buildah copy --from $container $final /app/server /server
buildah config --entrypoint '["/server"]' $final

# Коммитим
buildah commit $final myserver:latest

# Очистка
buildah rm $container $final
```

---

## 7. Сравнение архитектур

### 7.1 Docker архитектура

```
┌──────────┐     ┌──────────┐     ┌────────────┐     ┌──────────┐
│ docker   │────►│ dockerd  │────►│ containerd │────►│   runc   │
│   CLI    │     │ (daemon) │     │            │     │          │
└──────────┘     └──────────┘     └────────────┘     └──────────┘
                      │
                      ▼
               /var/run/docker.sock
```

**Преимущества:**
- Единый интерфейс
- Обширная экосистема
- Стабильность

**Недостатки:**
- Daemon с root-правами
- Single point of failure
- Больше overhead

### 7.2 Podman архитектура

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ podman   │────►│  libpod  │────►│   runc   │
│   CLI    │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘
                      │
                      ▼
                   conmon
            (per-container monitor)
```

**Преимущества:**
- Нет daemon
- Rootless из коробки
- Fork-exec модель

**Недостатки:**
- Меньше экосистема
- Некоторые отличия от Docker

### 7.3 Kubernetes с containerd

```
┌──────────┐     ┌────────────┐     ┌──────────────┐     ┌──────┐
│ kubelet  │────►│ containerd │────►│containerd-shim│────►│ runc │
│          │ CRI │            │     │              │     │      │
└──────────┘     └────────────┘     └──────────────┘     └──────┘
```

### 7.4 Kubernetes с CRI-O

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────┐
│ kubelet  │────►│  CRI-O   │────►│  conmon  │────►│ runc │
│          │ CRI │          │     │          │     │      │
└──────────┘     └──────────┘     └──────────┘     └──────┘
```

---

## 8. Выбор runtime

### 8.1 Рекомендации по выбору

| Сценарий | Рекомендация |
|----------|--------------|
| Разработка | Docker или Podman |
| Production Kubernetes | containerd или CRI-O |
| Rootless/Security | Podman |
| CI/CD | Podman, Buildah, Kaniko |
| Edge/IoT | containerd с minimal config |
| Multi-tenant | Kata, gVisor |

### 8.2 Миграция с Docker на Podman

```bash
# 1. Установка Podman
apt install podman

# 2. Создание alias для совместимости
echo "alias docker=podman" >> ~/.bashrc

# 3. Импорт существующих образов
docker save myimage:latest | podman load

# 4. Настройка registries
cat > /etc/containers/registries.conf << EOF
[registries.search]
registries = ['docker.io', 'registry.access.redhat.com']

[registries.insecure]
registries = []
EOF

# 5. Проверка
podman info
podman run --rm alpine echo "Migration successful"
```

### 8.3 Переключение Kubernetes на containerd

```bash
# 1. Установка containerd
apt install containerd

# 2. Конфигурация для Kubernetes
containerd config default > /etc/containerd/config.toml

# Включить SystemdCgroup
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# 3. Перезапуск
systemctl restart containerd

# 4. Настройка kubelet
cat > /etc/default/kubelet << EOF
KUBELET_EXTRA_ARGS=--container-runtime-endpoint=unix:///run/containerd/containerd.sock
EOF

# 5. Перезапуск kubelet
systemctl restart kubelet
```

---

## 9. Практика: запуск приложения

### 9.1 Сравнение запуска одного приложения

```bash
# Docker
docker run -d --name app -p 8080:80 nginx:alpine

# Podman
podman run -d --name app -p 8080:80 nginx:alpine

# containerd (через nerdctl)
nerdctl run -d --name app -p 8080:80 nginx:alpine

# containerd (через ctr) - более низкоуровневый
ctr images pull docker.io/library/nginx:alpine
ctr run -d --net-host docker.io/library/nginx:alpine app
```

### 9.2 Проверка процессов

```bash
# Docker: контейнер — дочерний процесс containerd-shim
ps aux | grep -E "(docker|containerd|nginx)"

# Podman: контейнер — независимый процесс с conmon
ps aux | grep -E "(conmon|nginx)"
```

---

## 💡 Key Takeaways

- **containerd** — промышленный runtime, используется Docker и Kubernetes
- **Podman** — daemonless альтернатива Docker с rootless из коробки
- **CRI-O** — минималистичный runtime специально для Kubernetes
- **Выбор runtime** зависит от сценария: разработка, production, безопасность
- **Миграция** между runtime обычно проста благодаря OCI стандартам

---

## 🚀 Next Steps

**Related Modules:**
- [Networking](../07_Networking/) — сетевая подсистема контейнеров
- [Docker](../08_Docker/) — практическая работа с Docker

**Practice Ideas:**
1. Установите containerd и запустите контейнер через ctr и nerdctl
2. Настройте rootless Podman и создайте pod
3. Используйте Buildah для сборки образа без Dockerfile
4. Сравните время старта контейнера в Docker, Podman и containerd

**Going Deeper:**
- Kata Containers и VM-based isolation
- gVisor для userspace kernel
- Firecracker microVMs

---

## 📚 Additional Resources

**Documentation:**
- [containerd documentation](https://containerd.io/docs/)
- [Podman documentation](https://docs.podman.io/)
- [CRI-O documentation](https://cri-o.io/)
- [Buildah documentation](https://buildah.io/)

**Articles:**
- [Container runtimes comparison](https://www.inovex.de/de/blog/containers-docker-containerd-nabla-kata-firecracker/)
- [Migrating from Docker to Podman](https://www.redhat.com/sysadmin/podman-docker-compose)

**Tools:**
- [nerdctl](https://github.com/containerd/nerdctl)
- [crictl](https://github.com/kubernetes-sigs/cri-tools)
- [skopeo](https://github.com/containers/skopeo)

---

