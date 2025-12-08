# Cloud Native Development - Quiz
## S3: Simple Storage Service

---

## Question 1: Durability

Какова durability S3 Standard?

A) 99.9%

B) 99.99%

C) 99.999999999% (11 nines)

D) 100%

---

## Question 2: Storage Classes

Какой storage class рекомендуется для данных с неизвестным паттерном доступа?

A) S3 Standard

B) S3 Intelligent-Tiering

C) S3 Glacier

D) S3 One Zone-IA

---

## Question 3: Object Size

Какой максимальный размер одного объекта в S3?

A) 5 GB

B) 100 GB

C) 5 TB

D) Unlimited

---

## Question 4: Bucket Names

Какое утверждение о bucket names ВЕРНО?

A) Могут начинаться с цифры

B) Глобально уникальны во всём AWS

C) Могут содержать заглавные буквы

D) Могут быть изменены после создания

---

## Question 5: Versioning

Что происходит при "удалении" объекта в bucket с включённым versioning?

A) Объект полностью удаляется

B) Создаётся delete marker, старые версии сохраняются

C) Удаляются все версии объекта

D) Versioning автоматически отключается

---

## Question 6: Encryption

Какой тип шифрования S3 использует по умолчанию с 2023 года?

A) Нет шифрования

B) SSE-S3 (AES-256)

C) SSE-KMS

D) Client-side encryption

---

## Question 7: Glacier Retrieval

Какое минимальное время retrieval для S3 Glacier Deep Archive (Standard retrieval)?

A) Мгновенно

B) 1-5 минут

C) 1-12 часов

D) 12-48 часов

---

## Question 8: Lifecycle

Что можно настроить через S3 Lifecycle Policy?

A) Только удаление объектов

B) Переход между storage classes и expiration

C) Только шифрование

D) Только репликацию

---

## Question 9: Block Public Access

На каком уровне можно настроить Block Public Access?

A) Только на уровне bucket

B) Только на уровне аккаунта

C) На уровне bucket и аккаунта

D) На уровне объекта

---

## Question 10: Presigned URLs

Для чего используются Presigned URLs?

A) Для постоянного публичного доступа

B) Для временного доступа без IAM credentials

C) Для шифрования данных

D) Для версионирования

---

## Question 11: Cross-Region Replication

Что требуется для настройки S3 Cross-Region Replication?

A) Versioning включён на source bucket

B) Только destination bucket

C) Оба bucket в одном регионе

D) Premium support plan

---

## Question 12: Multipart Upload

Для файлов какого размера рекомендуется Multipart Upload?

A) > 5 MB

B) > 50 MB

C) > 100 MB

D) > 1 GB

---

## Question 13: Pricing

За что НЕ нужно платить в S3?

A) Storage (GB/month)

B) Data transfer IN

C) PUT requests

D) GET requests

---

## Question 14: S3 Select

Что позволяет S3 Select?

A) Выбирать storage class

B) Выполнять SQL запросы к данным без скачивания объекта

C) Выбирать регион bucket

D) Выбирать тип шифрования

---

## Question 15: Event Notifications

Куда S3 может отправлять event notifications?

A) Только в Lambda

B) Lambda, SQS, SNS, EventBridge

C) Только в CloudWatch

D) Только в SNS

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | S3 Standard обеспечивает 99.999999999% (11 nines) durability — данные практически невозможно потерять. |
| 2 | B | S3 Intelligent-Tiering автоматически перемещает данные между классами на основе паттернов доступа. |
| 3 | C | Максимальный размер объекта — 5 TB. Для загрузки используйте Multipart Upload. |
| 4 | B | Bucket names глобально уникальны во всём AWS. Должны быть lowercase, 3-63 символа. |
| 5 | B | При versioning "удаление" создаёт delete marker. Старые версии сохраняются и могут быть восстановлены. |
| 6 | B | С января 2023 все новые объекты автоматически шифруются SSE-S3 (AES-256). |
| 7 | D | S3 Glacier Deep Archive Standard retrieval: 12-48 часов. Bulk: до 48 часов. Expedited недоступен. |
| 8 | B | Lifecycle Policy настраивает transitions между storage classes и expiration (автоудаление). |
| 9 | C | Block Public Access можно настроить на уровне bucket и на уровне всего аккаунта. |
| 10 | B | Presigned URLs предоставляют временный доступ к объекту без необходимости IAM credentials у получателя. |
| 11 | A | Для CRR требуется versioning на source bucket. Destination bucket может быть в другом регионе и аккаунте. |
| 12 | C | AWS рекомендует Multipart Upload для файлов > 100 MB. Обязательно для файлов > 5 GB. |
| 13 | B | Data transfer IN (загрузка в S3) бесплатна. Платите за storage, requests, и data transfer OUT. |
| 14 | B | S3 Select позволяет выполнять SQL запросы (SELECT) к CSV, JSON, Parquet файлам без полного скачивания. |
| 15 | B | S3 Event Notifications можно отправлять в Lambda, SQS, SNS, и Amazon EventBridge. |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **14-15 (90-100%)** | 🏆 Отлично! |
| **11-13 (70-89%)** | ✅ Хорошо |
| **8-10 (50-69%)** | ⚠️ Удовлетворительно |
| **< 8 (<50%)** | 📚 Нужно повторить |

---

