# Container Runtimes - Quiz

Проверьте свои знания по теме "containerd, Podman, CRI-O и архитектура демонов".

---

## Question 1: Уровни runtime







Какой уровень занимает containerd в иерархии container runtimes?

A) Container engine

B) Kernel module

C) Low-level runtime

D) High-level runtime

---

## Question 2: containerd







Какие компании используют containerd в своих продуктах?

A) Только Kubernetes

B) Только Docker

C) Docker и Kubernetes

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

A) Для CI/CD систем

B) Для desktop контейнеров

C) Для Kubernetes

D) Для IoT устройств

---

## Question 5: ctr utility







Что такое ctr?

A) Container registry

B) Container test runner

C) Compression tool

D) CLI для containerd

---

## Question 6: nerdctl







Какое преимущество nerdctl над ctr?

A) Docker-совместимый синтаксис

B) Меньше потребление памяти

C) Работает без containerd

D) Быстрее работает

---

## Question 7: Rootless containers







Какой инструмент лучше всего подходит для rootless контейнеров из коробки?

A) CRI-O

B) Docker

C) Podman

D) containerd

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

A) Мониторинг контейнеров

B) Запуск контейнеров

C) Оркестрация контейнеров

D) Создание OCI-совместимых образов

---

## Question 10: containerd namespaces







Что такое namespaces в контексте containerd (не Linux namespaces)?

A) Сетевая изоляция

B) Пользовательская изоляция

C) Логическое разделение контейнеров и образов

D) Изоляция ресурсов контейнера

---

## Question 11: conmon







Какова роль conmon в Podman/CRI-O?

A) Мониторинг контейнера (держит stdin/stdout)

B) Управление конфигурацией

C) Мониторинг сети

D) Сборка образов

---

## Question 12: containerd-shim







Зачем нужен containerd-shim?

A) Позволяет containerd перезапускаться без остановки контейнеров

B) Для работы с сетью

C) Для шифрования данных

D) Для сборки образов

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

A) Только в rootless режиме

B) Нет, containerd обязателен в современных версиях

C) Только на Windows

D) Да, containerd опционален

---

## Question 15: Выбор runtime для Kubernetes







Какие runtime рекомендуются для production Kubernetes?

A) Buildah и skopeo

B) containerd и CRI-O

C) runc и crun

D) Docker и Podman

---

## Question 16: systemd интеграция Podman







Как сгенерировать systemd unit для Podman контейнера?

A) systemctl create podman

B) podman-systemd create

C) podman generate systemd

D) podman systemd generate

---

## Question 17: containerd конфигурация







Где находится основной файл конфигурации containerd?

A) /var/lib/containerd/config.json

B) /etc/docker/daemon.json

C) /etc/containerd/config.toml

D) /etc/cri-o/config.yaml

---

## Question 18: Buildah vs docker build







Какое преимущество Buildah над docker build?

A) Поддержка Windows

B) Быстрее сборка

C) Лучшее кеширование

D) Возможность скриптовой сборки без Dockerfile

---

## Question 19: crictl







Для чего используется crictl?

A) Мониторинг кластера

B) CLI для CRI-совместимых runtime

C) Создание образов

D) Управление сетью

---

## Question 20: Миграция Docker → Podman







Как проще всего мигрировать с Docker на Podman?

A) Экспорт всех контейнеров

B) Установка специального плагина

C) Полное переписывание конфигурации

D) alias docker=podman и совместимый CLI

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | containerd — high-level runtime, управляет lifecycle, образами, использует runc |
| 2 | C | containerd используется и Docker (под капотом), и Kubernetes напрямую |
| 3 | B | Podman не требует daemon, работает по модели fork-exec |
| 4 | C | CRI-O создан специально для Kubernetes, реализует CRI |
| 5 | D | ctr — низкоуровневый CLI для containerd |
| 6 | A | nerdctl предоставляет Docker-совместимый синтаксис для containerd |
| 7 | C | Podman изначально спроектирован для rootless режима |
| 8 | B | Pod в Podman — группа контейнеров с общим network namespace (как в K8s) |
| 9 | D | Buildah предназначен для создания OCI-совместимых образов |
| 10 | C | Namespaces в containerd — логическое разделение (k8s.io, moby, default) |
| 11 | A | conmon — процесс-монитор, держит stdin/stdout контейнера |
| 12 | A | shim позволяет перезапускать containerd без влияния на работающие контейнеры |
| 13 | A | CRI — Container Runtime Interface, протокол между kubelet и runtime |
| 14 | B | Современный Docker использует containerd как обязательный компонент |
| 15 | B | Для production K8s рекомендуются containerd и CRI-O |
| 16 | C | podman generate systemd создаёт unit-файл для контейнера |
| 17 | C | Конфигурация containerd в /etc/containerd/config.toml |
| 18 | D | Buildah позволяет программную сборку через shell-скрипты |
| 19 | B | crictl — CLI для работы с любым CRI-совместимым runtime |
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

