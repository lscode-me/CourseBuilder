# OCI Standards - Quiz

Проверьте свои знания по теме "Open Container Initiative и низкоуровневые инструменты".

---

## Question 1: История OCI

В каком году была основана Open Container Initiative?

A) 2017

B) 2013

C) 2015

D) 2019

---

## Question 2: OCI спецификации

Сколько основных спецификаций определяет OCI?

A) 1 (только Runtime)

B) 3 (Runtime, Image и Distribution)

C) 2 (Runtime и Image)

D) 4 (Runtime, Image, Distribution и Security)

---

## Question 3: OCI Bundle

Что входит в состав OCI Bundle?

A) Только rootfs

B) rootfs и config.json

C) Только config.json

D) Docker image и Dockerfile

---

## Question 4: runC

Что такое runC?

A) Графический интерфейс для Docker

B) Сетевой плагин для контейнеров

C) Container registry

D) Референсная реализация OCI runtime

---

## Question 5: config.json

Какой раздел config.json определяет ограничения ресурсов?

A) root

B) linux.resources

C) process

D) mounts

---

## Question 6: Жизненный цикл контейнера

Какие состояния проходит контейнер по OCI спецификации?

A) pending → running → completed

B) building → running → exited

C) init → active → terminated

D) created → running → stopped

---

## Question 7: unshare

Для чего используется утилита unshare?

A) Для удаления namespaces

B) Для мониторинга namespaces

C) Для создания новых namespaces

D) Для sharing файлов между контейнерами

---

## Question 8: nsenter

Какую функцию выполняет nsenter?

A) Вход в существующие namespaces процесса

B) Создание нового namespace

C) Перечисление всех namespaces

D) Выход из namespace

---

## Question 9: OCI Image Manifest

Что содержит manifest образа OCI?

A) Конфигурацию сети

B) Логи сборки образа

C) Исходный код приложения

D) Ссылки на config и layers с их digest'ами

---

## Question 10: skopeo

Для чего используется утилита skopeo?

A) Копирование и анализ образов без Docker daemon

B) Создание Dockerfile

C) Мониторинг контейнеров

D) Запуск контейнеров

---

## Question 11: crun

В чём преимущество crun над runC?

A) Поддержка Windows

B) Лучшая безопасность

C) Больше функций

D) Более высокая производительность (написан на C)

---

## Question 12: Kata Containers

Какой тип изоляции использует Kata Containers?

A) Только namespaces

B) Шифрование

C) Легковесные виртуальные машины

D) Userspace kernel

---

## Question 13: gVisor

Как gVisor обеспечивает изоляцию?

A) Перехват syscalls в userspace

B) Через шифрование

C) Через namespaces

D) Через VM

---

## Question 14: OCI Distribution API

Какой endpoint используется для получения manifest образа?

A) /v2/<name>/config/<ref>

B) /v2/<name>/manifests/<ref>

C) /v2/<name>/blobs/<digest>

D) /v2/<name>/layers/<ref>

---

## Question 15: Операции runC

Какая команда создаёт контейнер без запуска процесса?

A) runc create

B) runc run

C) runc init

D) runc start

---

## Question 16: Capabilities в config.json

Для чего используется раздел capabilities в config.json?

A) Описание возможностей runtime

B) Определение capabilities Linux для процесса контейнера

C) Список поддерживаемых команд

D) Возможности сети

---

## Question 17: maskedPaths

Что делает параметр maskedPaths в config.json?

A) Делает указанные пути в /proc недоступными

B) Скрывает пути в логах

C) Добавляет пути в PATH

D) Шифрует файлы по указанным путям

---

## Question 18: containerd и runC

Какова роль containerd-shim между containerd и runC?

A) Управление сетью

B) Логирование

C) Позволяет containerd перезапускаться без остановки контейнеров

D) Шифрование трафика

---

## Question 19: OCI версия

Какое поле в config.json указывает версию OCI спецификации?

A) apiVersion

B) ociVersion

C) version

D) specVersion

---

## Question 20: Альтернативные runtime в Docker

Как запустить контейнер с альтернативным runtime в Docker?

A) docker run --engine=kata

B) docker --runtime kata run

C) docker run --runtime=kata

D) docker run --use-runtime kata

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | OCI была основана в 2015 году Docker и CoreOS |
| 2 | B | OCI определяет 3 спецификации: Runtime, Image и Distribution |
| 3 | B | OCI Bundle состоит из директории rootfs и файла config.json |
| 4 | D | runC — референсная реализация OCI runtime specification |
| 5 | B | Ресурсы определяются в секции linux.resources (memory, cpu, pids) |
| 6 | D | Контейнер проходит состояния: created → running → stopped |
| 7 | C | unshare создаёт новые namespaces для запускаемого процесса |
| 8 | A | nsenter позволяет войти в namespaces существующего процесса по PID |
| 9 | D | Manifest содержит ссылки на config и layers с их digest'ами и размерами |
| 10 | A | skopeo позволяет копировать, инспектировать образы без Docker daemon |
| 11 | D | crun написан на C (не Go), поэтому быстрее и использует меньше памяти |
| 12 | C | Kata запускает каждый контейнер в легковесной VM для сильной изоляции |
| 13 | A | gVisor перехватывает syscalls и обрабатывает их в userspace (Sentry) |
| 14 | B | Manifest получается через GET /v2/<name>/manifests/<ref> |
| 15 | A | runc create создаёт контейнер, runc start запускает его процесс |
| 16 | B | Capabilities определяют Linux capabilities (bounding, effective, permitted) |
| 17 | A | maskedPaths делает указанные пути (обычно в /proc) недоступными для контейнера |
| 18 | C | shim позволяет containerd перезапускаться без влияния на работающие контейнеры |
| 19 | B | Поле ociVersion указывает версию OCI спецификации |
| 20 | C | docker run --runtime=<name> запускает контейнер с указанным runtime |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете OCI стандарты. Переходите к изучению container runtimes. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про config.json и альтернативные runtime. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про OCI спецификации и практику с runC. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется выполнить практические примеры с runC и skopeo. |

---


