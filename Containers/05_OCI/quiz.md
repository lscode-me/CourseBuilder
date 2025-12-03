# OCI Standards - Quiz

Проверьте свои знания по теме "Open Container Initiative и низкоуровневые инструменты".

---

## Question 1: История OCI

В каком году была основана Open Container Initiative?

A) 2013

B) 2015

C) 2017

D) 2019

---

## Question 2: OCI спецификации

Сколько основных спецификаций определяет OCI?

A) 2 (Runtime и Image)

B) 3 (Runtime, Image и Distribution)

C) 4 (Runtime, Image, Distribution и Security)

D) 1 (только Runtime)

---

## Question 3: OCI Bundle

Что входит в состав OCI Bundle?

A) Только config.json

B) rootfs и config.json

C) Docker image и Dockerfile

D) Только rootfs

---

## Question 4: runC

Что такое runC?

A) Container registry

B) Референсная реализация OCI runtime

C) Графический интерфейс для Docker

D) Сетевой плагин для контейнеров

---

## Question 5: config.json

Какой раздел config.json определяет ограничения ресурсов?

A) process

B) root

C) linux.resources

D) mounts

---

## Question 6: Жизненный цикл контейнера

Какие состояния проходит контейнер по OCI спецификации?

A) created → running → stopped

B) building → running → exited

C) init → active → terminated

D) pending → running → completed

---

## Question 7: unshare

Для чего используется утилита unshare?

A) Для sharing файлов между контейнерами

B) Для создания новых namespaces

C) Для удаления namespaces

D) Для мониторинга namespaces

---

## Question 8: nsenter

Какую функцию выполняет nsenter?

A) Создание нового namespace

B) Вход в существующие namespaces процесса

C) Выход из namespace

D) Перечисление всех namespaces

---

## Question 9: OCI Image Manifest

Что содержит manifest образа OCI?

A) Исходный код приложения

B) Ссылки на config и layers с их digest'ами

C) Логи сборки образа

D) Конфигурацию сети

---

## Question 10: skopeo

Для чего используется утилита skopeo?

A) Запуск контейнеров

B) Копирование и анализ образов без Docker daemon

C) Мониторинг контейнеров

D) Создание Dockerfile

---

## Question 11: crun

В чём преимущество crun над runC?

A) Лучшая безопасность

B) Более высокая производительность (написан на C)

C) Больше функций

D) Поддержка Windows

---

## Question 12: Kata Containers

Какой тип изоляции использует Kata Containers?

A) Только namespaces

B) Легковесные виртуальные машины

C) Userspace kernel

D) Шифрование

---

## Question 13: gVisor

Как gVisor обеспечивает изоляцию?

A) Через namespaces

B) Через VM

C) Перехват syscalls в userspace

D) Через шифрование

---

## Question 14: OCI Distribution API

Какой endpoint используется для получения manifest образа?

A) /v2/<name>/blobs/<digest>

B) /v2/<name>/manifests/<ref>

C) /v2/<name>/layers/<ref>

D) /v2/<name>/config/<ref>

---

## Question 15: Операции runC

Какая команда создаёт контейнер без запуска процесса?

A) runc run

B) runc start

C) runc create

D) runc init

---

## Question 16: Capabilities в config.json

Для чего используется раздел capabilities в config.json?

A) Определение capabilities Linux для процесса контейнера

B) Описание возможностей runtime

C) Список поддерживаемых команд

D) Возможности сети

---

## Question 17: maskedPaths

Что делает параметр maskedPaths в config.json?

A) Скрывает пути в логах

B) Делает указанные пути в /proc недоступными

C) Шифрует файлы по указанным путям

D) Добавляет пути в PATH

---

## Question 18: containerd и runC

Какова роль containerd-shim между containerd и runC?

A) Шифрование трафика

B) Позволяет containerd перезапускаться без остановки контейнеров

C) Логирование

D) Управление сетью

---

## Question 19: OCI версия

Какое поле в config.json указывает версию OCI спецификации?

A) version

B) ociVersion

C) specVersion

D) apiVersion

---

## Question 20: Альтернативные runtime в Docker

Как запустить контейнер с альтернативным runtime в Docker?

A) docker run --engine=kata

B) docker run --runtime=kata

C) docker run --use-runtime kata

D) docker --runtime kata run

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | OCI была основана в 2015 году Docker и CoreOS |
| 2 | B | OCI определяет 3 спецификации: Runtime, Image и Distribution |
| 3 | B | OCI Bundle состоит из директории rootfs и файла config.json |
| 4 | B | runC — референсная реализация OCI runtime specification |
| 5 | C | Ресурсы определяются в секции linux.resources (memory, cpu, pids) |
| 6 | A | Контейнер проходит состояния: created → running → stopped |
| 7 | B | unshare создаёт новые namespaces для запускаемого процесса |
| 8 | B | nsenter позволяет войти в namespaces существующего процесса по PID |
| 9 | B | Manifest содержит ссылки на config и layers с их digest'ами и размерами |
| 10 | B | skopeo позволяет копировать, инспектировать образы без Docker daemon |
| 11 | B | crun написан на C (не Go), поэтому быстрее и использует меньше памяти |
| 12 | B | Kata запускает каждый контейнер в легковесной VM для сильной изоляции |
| 13 | C | gVisor перехватывает syscalls и обрабатывает их в userspace (Sentry) |
| 14 | B | Manifest получается через GET /v2/<name>/manifests/<ref> |
| 15 | C | runc create создаёт контейнер, runc start запускает его процесс |
| 16 | A | Capabilities определяют Linux capabilities (bounding, effective, permitted) |
| 17 | B | maskedPaths делает указанные пути (обычно в /proc) недоступными для контейнера |
| 18 | B | shim позволяет containerd перезапускаться без влияния на работающие контейнеры |
| 19 | B | Поле ociVersion указывает версию OCI спецификации |
| 20 | B | docker run --runtime=<name> запускает контейнер с указанным runtime |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете OCI стандарты. Переходите к изучению container runtimes. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про config.json и альтернативные runtime. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про OCI спецификации и практику с runC. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется выполнить практические примеры с runC и skopeo. |

---

