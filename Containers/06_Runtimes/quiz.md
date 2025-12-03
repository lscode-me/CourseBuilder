# Container Runtimes - Quiz

Проверьте свои знания по теме "containerd, Podman, CRI-O и архитектура демонов".

---

## Question 1: Уровни runtime

Какой уровень занимает containerd в иерархии container runtimes?

A) Low-level runtime

B) High-level runtime

C) Container engine

D) Kernel module

---

## Question 2: containerd

Какие компании используют containerd в своих продуктах?

A) Только Docker

B) Docker и Kubernetes

C) Только Kubernetes

D) Только Red Hat

---

## Question 3: Podman архитектура

В чём ключевое отличие архитектуры Podman от Docker?

A) Podman быстрее

B) Podman не требует daemon

C) Podman не поддерживает Dockerfile

D) Podman не использует runc

---

## Question 4: CRI-O назначение

Для чего специально разработан CRI-O?

A) Для desktop контейнеров

B) Для CI/CD систем

C) Для Kubernetes

D) Для IoT устройств

---

## Question 5: ctr utility

Что такое ctr?

A) Container registry

B) CLI для containerd

C) Container test runner

D) Compression tool

---

## Question 6: nerdctl

Какое преимущество nerdctl над ctr?

A) Быстрее работает

B) Docker-совместимый синтаксис

C) Меньше потребление памяти

D) Работает без containerd

---

## Question 7: Rootless containers

Какой инструмент лучше всего подходит для rootless контейнеров из коробки?

A) Docker

B) containerd

C) Podman

D) CRI-O

---

## Question 8: Podman pods

Что такое pod в контексте Podman?

A) Файл конфигурации

B) Группа контейнеров с общим network namespace

C) Тип сетевого драйвера

D) Формат образов

---

## Question 9: Buildah

Для чего используется Buildah?

A) Запуск контейнеров

B) Создание OCI-совместимых образов

C) Оркестрация контейнеров

D) Мониторинг контейнеров

---

## Question 10: containerd namespaces

Что такое namespaces в контексте containerd (не Linux namespaces)?

A) Изоляция ресурсов контейнера

B) Логическое разделение контейнеров и образов

C) Сетевая изоляция

D) Пользовательская изоляция

---

## Question 11: conmon

Какова роль conmon в Podman/CRI-O?

A) Мониторинг сети

B) Мониторинг контейнера (держит stdin/stdout)

C) Управление конфигурацией

D) Сборка образов

---

## Question 12: containerd-shim

Зачем нужен containerd-shim?

A) Для шифрования данных

B) Позволяет containerd перезапускаться без остановки контейнеров

C) Для сборки образов

D) Для работы с сетью

---

## Question 13: CRI интерфейс

Что такое CRI?

A) Container Registry Interface

B) Container Runtime Interface для Kubernetes

C) Container Resource Inspector

D) Container Restart Implementation

---

## Question 14: Docker без containerd

Может ли Docker работать без containerd?

A) Да, containerd опционален

B) Нет, containerd обязателен в современных версиях

C) Только на Windows

D) Только в rootless режиме

---

## Question 15: Выбор runtime для Kubernetes

Какие runtime рекомендуются для production Kubernetes?

A) Docker и Podman

B) containerd и CRI-O

C) runc и crun

D) Buildah и skopeo

---

## Question 16: systemd интеграция Podman

Как сгенерировать systemd unit для Podman контейнера?

A) podman systemd generate

B) podman generate systemd

C) systemctl create podman

D) podman-systemd create

---

## Question 17: containerd конфигурация

Где находится основной файл конфигурации containerd?

A) /etc/docker/daemon.json

B) /etc/containerd/config.toml

C) /var/lib/containerd/config.json

D) /etc/cri-o/config.yaml

---

## Question 18: Buildah vs docker build

Какое преимущество Buildah над docker build?

A) Быстрее сборка

B) Возможность скриптовой сборки без Dockerfile

C) Лучшее кеширование

D) Поддержка Windows

---

## Question 19: crictl

Для чего используется crictl?

A) Создание образов

B) CLI для CRI-совместимых runtime

C) Мониторинг кластера

D) Управление сетью

---

## Question 20: Миграция Docker → Podman

Как проще всего мигрировать с Docker на Podman?

A) Полное переписывание конфигурации

B) alias docker=podman и совместимый CLI

C) Экспорт всех контейнеров

D) Установка специального плагина

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | containerd — high-level runtime, управляет lifecycle, образами, использует runc |
| 2 | B | containerd используется и Docker (под капотом), и Kubernetes напрямую |
| 3 | B | Podman не требует daemon, работает по модели fork-exec |
| 4 | C | CRI-O создан специально для Kubernetes, реализует CRI |
| 5 | B | ctr — низкоуровневый CLI для containerd |
| 6 | B | nerdctl предоставляет Docker-совместимый синтаксис для containerd |
| 7 | C | Podman изначально спроектирован для rootless режима |
| 8 | B | Pod в Podman — группа контейнеров с общим network namespace (как в K8s) |
| 9 | B | Buildah предназначен для создания OCI-совместимых образов |
| 10 | B | Namespaces в containerd — логическое разделение (k8s.io, moby, default) |
| 11 | B | conmon — процесс-монитор, держит stdin/stdout контейнера |
| 12 | B | shim позволяет перезапускать containerd без влияния на работающие контейнеры |
| 13 | B | CRI — Container Runtime Interface, протокол между kubelet и runtime |
| 14 | B | Современный Docker использует containerd как обязательный компонент |
| 15 | B | Для production K8s рекомендуются containerd и CRI-O |
| 16 | B | podman generate systemd создаёт unit-файл для контейнера |
| 17 | B | Конфигурация containerd в /etc/containerd/config.toml |
| 18 | B | Buildah позволяет программную сборку через shell-скрипты |
| 19 | B | crictl — CLI для работы с любым CRI-совместимым runtime |
| 20 | B | Podman имеет Docker-совместимый CLI, достаточно alias |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете container runtimes. Переходите к сетевой подсистеме. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про containerd и Podman. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про архитектуры разных runtime. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с разными runtime: containerd, Podman. |

---

