# Linux Containers
## Курс по контейнеризации в Linux

---

## 📚 О курсе

Этот курс охватывает все аспекты контейнеризации в Linux — от низкоуровневых механизмов ядра до оркестрации в production. Курс построен по принципу "снизу вверх": начиная с понимания основ изоляции процессов и заканчивая Kubernetes.

### Целевая аудитория

- DevOps инженеры
- Системные администраторы
- Backend разработчики
- SRE специалисты
- Все, кто хочет глубоко понимать контейнеры

### Предварительные требования

- Базовые знания Linux (командная строка, процессы)
- Понимание основ сетей (IP, routing, NAT)
- Опыт работы в терминале

---

## 🗺️ Структура курса

### Раздел 1: Основы изоляции

| Модуль | Тема | Описание |
|--------|------|----------|
| [01_Intro](./01_Intro/) | Process Isolation | История изоляции: от chroot к контейнерам |
| [02_Namespaces](./02_Namespaces/) | Linux Namespaces | PID, NET, MNT, UTS, IPC, USER, CGROUP namespaces |
| [03_Cgroups](./03_Cgroups/) | Control Groups | Управление ресурсами: CPU, Memory, I/O |

### Раздел 2: Технологии контейнеров

| Модуль | Тема | Описание |
|--------|------|----------|
| [04_FileSystem](./04_FileSystem/) | Union Filesystems | OverlayFS, AUFS, слои образов |
| [05_OCI](./05_OCI/) | OCI Standards | Runtime Spec, Image Spec, runC, unshare, nsenter |
| [06_Runtimes](./06_Runtimes/) | Container Runtimes | containerd, Podman, CRI-O, Buildah |

### Раздел 3: Docker и сети

| Модуль | Тема | Описание |
|--------|------|----------|
| [07_Networking](./07_Networking/) | Container Networking | Bridge, overlay, CNI, veth, DNS |
| [08_Docker](./08_Docker/) | Docker | CLI, Dockerfile, images, volumes, security |

### Раздел 4: Оркестрация

| Модуль | Тема | Описание |
|--------|------|----------|
| [09_Compose](./09_Compose/) | Docker Compose & Swarm | Multi-container apps, Docker Swarm |
| [10_Kubernetes](./10_Kubernetes/) | Kubernetes | Pods, Deployments, Services, kubectl |

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                     Linux Containers Course                      │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │  Intro  │─────────│Namespaces│─────────│ Cgroups │
    │(chroot) │         │         │         │         │
    └─────────┘         └─────────┘         └─────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │  Union  │─────────│   OCI   │─────────│Runtimes │
    │   FS    │         │Standards│         │         │
    └─────────┘         └─────────┘         └─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
         ┌─────────┐    ┌─────────┐    ┌─────────┐
         │Networking│────│ Docker  │────│ Compose │
         │         │    │         │    │ & Swarm │
         └─────────┘    └─────────┘    └─────────┘
                              │
                              ▼
                        ┌───────────┐
                        │Kubernetes │
                        │           │
                        └───────────┘
```

---

## 📋 Формат модуля

Каждый модуль содержит:

```
XX_ModuleName/
├── lecture.md    # Основной материал лекции
└── quiz.md       # Вопросы для самопроверки
```

### Структура лекции

- **Prerequisites** — что нужно знать перед началом
- **Learning Objectives** — цели обучения
- **Основной материал** — теория с практическими примерами
- **Key Takeaways** — главные выводы
- **Next Steps** — что изучить дальше
- **Additional Resources** — дополнительные материалы

### Quiz

- 20 вопросов с множественным выбором
- Ответы с пояснениями
- Рекомендации по результатам

---

## 🛠️ Практические требования

### Рекомендуемое окружение

- Linux (Ubuntu 22.04+ / Fedora 38+ / Debian 12+)
- Минимум 8GB RAM
- Docker или Podman
- Root доступ для низкоуровневых экспериментов

### Для локальной практики с Kubernetes

- Minikube или kind
- kubectl

### Установка необходимых инструментов

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y \
    docker.io \
    podman \
    buildah \
    skopeo \
    lxc \
    bridge-utils \
    jq

# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```

---

## ⏱️ Время прохождения

| Раздел | Модули | Время чтения | Время практики |
|--------|--------|--------------|----------------|
| Основы изоляции | 1-3 | 2-3 часа | 3-4 часа |
| Технологии контейнеров | 4-6 | 2-3 часа | 4-5 часов |
| Docker и сети | 7-8 | 2-3 часа | 4-5 часов |
| Оркестрация | 9-10 | 2-3 часа | 4-5 часов |

**Общее время:** ~25-30 часов (включая практику)

---

## 🎓 После прохождения курса

Вы будете уметь:

✅ Объяснять механизмы изоляции Linux (namespaces, cgroups)

✅ Создавать контейнеры "с нуля" через низкоуровневые инструменты

✅ Писать оптимизированные Dockerfiles

✅ Работать с различными container runtimes

✅ Настраивать сеть контейнеров

✅ Развёртывать многоконтейнерные приложения

✅ Понимать архитектуру Kubernetes

---

## 📚 Дополнительные ресурсы

### Книги

- "Container Security" by Liz Rice
- "Docker Deep Dive" by Nigel Poulton
- "Kubernetes in Action" by Marko Lukša

### Онлайн-ресурсы

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [OCI Specifications](https://opencontainers.org/)
- [CNCF Landscape](https://landscape.cncf.io/)

### Сертификации

- [CKA (Certified Kubernetes Administrator)](https://www.cncf.io/certification/cka/)
- [CKAD (Certified Kubernetes Application Developer)](https://www.cncf.io/certification/ckad/)
- [CKS (Certified Kubernetes Security Specialist)](https://www.cncf.io/certification/cks/)

---

## 📝 Версия и обновления

**Версия:** 1.0  
**Дата создания:** Декабрь 2024  
**Последнее обновление:** Декабрь 2024

Курс поддерживается в актуальном состоянии. При обнаружении устаревшей информации создайте issue или pull request.

---

