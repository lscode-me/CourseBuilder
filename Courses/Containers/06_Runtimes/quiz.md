# Container Runtimes - Quiz

Проверьте свои знания по теме "containerd, Podman, CRI-O и архитектура демонов".

---

## Question 1: Уровни runtime


Какой уровень занимает containerd в иерархии container runtimes?

A) Kernel module

B) High-level runtime

C) Low-level runtime

D) Container engine

---

## Question 2: containerd


Какие компании используют containerd в своих продуктах?

A) Docker и Kubernetes

B) Только Docker

C) Только Red Hat

D) Только Kubernetes

---

## Question 3: Podman архитектура


В чём ключевое отличие архитектуры Podman от Docker?

A) Podman не требует daemon

B) Podman быстрее

C) Podman не использует runc

D) Podman не поддерживает Dockerfile

---

## Question 4: CRI-O назначение


Для чего специально разработан CRI-O?

A) Для Kubernetes

B) Для desktop контейнеров

C) Для IoT устройств

D) Для CI/CD систем

---

## Question 5: ctr utility


Что такое ctr?

A) CLI для containerd

B) Compression tool

C) Container test runner

D) Container registry

---

## Question 6: nerdctl


Какое преимущество nerdctl над ctr?

A) Работает без containerd

B) Быстрее работает

C) Docker-совместимый синтаксис

D) Меньше потребление памяти

---

## Question 7: Rootless containers


Какой инструмент лучше всего подходит для rootless контейнеров из коробки?

A) CRI-O

B) containerd

C) Docker

D) Podman

---

## Question 8: Podman pods


Что такое pod в контексте Podman?

A) Тип сетевого драйвера

B) Файл конфигурации

C) Группа контейнеров с общим network namespace

D) Формат образов

---

## Question 9: Buildah


Для чего используется Buildah?

A) Мониторинг контейнеров

B) Создание OCI-совместимых образов

C) Оркестрация контейнеров

D) Запуск контейнеров

---

## Question 10: containerd namespaces


Что такое namespaces в контексте containerd (не Linux namespaces)?

A) Логическое разделение контейнеров и образов

B) Пользовательская изоляция

C) Изоляция ресурсов контейнера

D) Сетевая изоляция

---

## Question 11: conmon


Какова роль conmon в Podman/CRI-O?

A) Сборка образов

B) Мониторинг контейнера (держит stdin/stdout)

C) Мониторинг сети

D) Управление конфигурацией

---

## Question 12: containerd-shim


Зачем нужен containerd-shim?

A) Для шифрования данных

B) Для работы с сетью

C) Для сборки образов

D) Позволяет containerd перезапускаться без остановки контейнеров

---

## Question 13: CRI интерфейс


Что такое CRI?

A) Container Runtime Interface для Kubernetes

B) Container Registry Interface

C) Container Resource Inspector

D) Container Restart Implementation

---

## Question 14: Docker без containerd


Может ли Docker работать без containerd?

A) Нет, containerd обязателен в современных версиях

B) Только на Windows

C) Только в rootless режиме

D) Да, containerd опционален

---

## Question 15: Выбор runtime для Kubernetes


Какие runtime рекомендуются для production Kubernetes?

A) runc и crun

B) Buildah и skopeo

C) containerd и CRI-O

D) Docker и Podman

---

## Question 16: systemd интеграция Podman


Как сгенерировать systemd unit для Podman контейнера?

A) podman generate systemd

B) systemctl create podman

C) podman systemd generate

D) podman-systemd create

---

## Question 17: containerd конфигурация


Где находится основной файл конфигурации containerd?

A) /etc/cri-o/config.yaml

B) /etc/docker/daemon.json

C) /etc/containerd/config.toml

D) /var/lib/containerd/config.json

---

## Question 18: Buildah vs docker build


Какое преимущество Buildah над docker build?

A) Возможность скриптовой сборки без Dockerfile

B) Поддержка Windows

C) Быстрее сборка

D) Лучшее кеширование

---

## Question 19: crictl


Для чего используется crictl?

A) Управление сетью

B) Мониторинг кластера

C) CLI для CRI-совместимых runtime

D) Создание образов

---

## Question 20: Миграция Docker → Podman


Как проще всего мигрировать с Docker на Podman?

A) Установка специального плагина

B) Экспорт всех контейнеров

C) Полное переписывание конфигурации

D) alias docker=podman и совместимый CLI

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | containerd — high-level runtime, управляет lifecycle, образами, использует runc |
| 2 | A | containerd используется и Docker (под капотом), и Kubernetes напрямую |
| 3 | A | Podman не требует daemon, работает по модели fork-exec |
| 4 | A | CRI-O создан специально для Kubernetes, реализует CRI |
| 5 | A | ctr — низкоуровневый CLI для containerd |
| 6 | C | nerdctl предоставляет Docker-совместимый синтаксис для containerd |
| 7 | D | Podman изначально спроектирован для rootless режима |
| 8 | C | Pod в Podman — группа контейнеров с общим network namespace (как в K8s) |
| 9 | B | Buildah предназначен для создания OCI-совместимых образов |
| 10 | A | Namespaces в containerd — логическое разделение (k8s.io, moby, default) |
| 11 | B | conmon — процесс-монитор, держит stdin/stdout контейнера |
| 12 | D | shim позволяет перезапускать containerd без влияния на работающие контейнеры |
| 13 | A | CRI — Container Runtime Interface, протокол между kubelet и runtime |
| 14 | A | Современный Docker использует containerd как обязательный компонент |
| 15 | C | Для production K8s рекомендуются containerd и CRI-O |
| 16 | A | podman generate systemd создаёт unit-файл для контейнера |
| 17 | C | Конфигурация containerd в /etc/containerd/config.toml |
| 18 | A | Buildah позволяет программную сборку через shell-скрипты |
| 19 | C | crictl — CLI для работы с любым CRI-совместимым runtime |
| 20 | D | Podman имеет Docker-совместимый CLI, достаточно alias |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете container runtimes. Переходите к сетевой подсистеме. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про containerd и Podman. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про архитектуры разных runtime. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с разными runtime: containerd, Podman. |

---

