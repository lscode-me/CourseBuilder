# Cloud Native Development - Quiz
## S3: Simple Storage Service

---

## Question 1: Durability


Какова durability S3 Standard?

A) 99.999999999% (11 nines)

B) 99.9%

C) 99.99%

D) 100%

---

## Question 2: Storage Classes


Какой storage class рекомендуется для данных с неизвестным паттерном доступа?

A) S3 Glacier

B) S3 One Zone-IA

C) S3 Intelligent-Tiering

D) S3 Standard

---

## Question 3: Object Size


Какой максимальный размер одного объекта в S3?

A) 100 GB

B) Unlimited

C) 5 TB

D) 5 GB

---

## Question 4: Bucket Names


Какое утверждение о bucket names ВЕРНО?

A) Могут быть изменены после создания

B) Глобально уникальны во всём AWS

C) Могут начинаться с цифры

D) Могут содержать заглавные буквы

---

## Question 5: Versioning


Что происходит при "удалении" объекта в bucket с включённым versioning?

A) Удаляются все версии объекта

B) Создаётся delete marker, старые версии сохраняются

C) Versioning автоматически отключается

D) Объект полностью удаляется

---

## Question 6: Encryption


Какой тип шифрования S3 использует по умолчанию с 2023 года?

A) Client-side encryption

B) SSE-S3 (AES-256)

C) Нет шифрования

D) SSE-KMS

---

## Question 7: Glacier Retrieval


Какое минимальное время retrieval для S3 Glacier Deep Archive (Standard retrieval)?

A) 1-5 минут

B) Мгновенно

C) 12-48 часов

D) 1-12 часов

---

## Question 8: Lifecycle


Что можно настроить через S3 Lifecycle Policy?

A) Переход между storage classes и expiration

B) Только удаление объектов

C) Только репликацию

D) Только шифрование

---

## Question 9: Block Public Access


На каком уровне можно настроить Block Public Access?

A) На уровне bucket и аккаунта

B) Только на уровне bucket

C) На уровне объекта

D) Только на уровне аккаунта

---

## Question 10: Presigned URLs


Для чего используются Presigned URLs?

A) Для временного доступа без IAM credentials

B) Для версионирования

C) Для шифрования данных

D) Для постоянного публичного доступа

---

## Question 11: Cross-Region Replication


Что требуется для настройки S3 Cross-Region Replication?

A) Premium support plan

B) Versioning включён на source bucket

C) Только destination bucket

D) Оба bucket в одном регионе

---

## Question 12: Multipart Upload


Для файлов какого размера рекомендуется Multipart Upload?

A) > 1 GB

B) > 50 MB

C) > 5 MB

D) > 100 MB

---

## Question 13: Pricing


За что НЕ нужно платить в S3?

A) PUT requests

B) Storage (GB/month)

C) Data transfer IN

D) GET requests

---

## Question 14: S3 Select


Что позволяет S3 Select?

A) Выбирать тип шифрования

B) Выполнять SQL запросы к данным без скачивания объекта

C) Выбирать регион bucket

D) Выбирать storage class

---

## Question 15: Event Notifications


Куда S3 может отправлять event notifications?

A) Lambda, SQS, SNS, EventBridge

B) Только в SNS

C) Только в Lambda

D) Только в CloudWatch

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | S3 Standard обеспечивает 99.999999999% (11 nines) durability — данные практически невозможно потерять. |
| 2 | C | S3 Intelligent-Tiering автоматически перемещает данные между классами на основе паттернов доступа. |
| 3 | C | Максимальный размер объекта — 5 TB. Для загрузки используйте Multipart Upload. |
| 4 | B | Bucket names глобально уникальны во всём AWS. Должны быть lowercase, 3-63 символа. |
| 5 | B | При versioning "удаление" создаёт delete marker. Старые версии сохраняются и могут быть восстановлены. |
| 6 | B | С января 2023 все новые объекты автоматически шифруются SSE-S3 (AES-256). |
| 7 | C | S3 Glacier Deep Archive Standard retrieval: 12-48 часов. Bulk: до 48 часов. Expedited недоступен. |
| 8 | A | Lifecycle Policy настраивает transitions между storage classes и expiration (автоудаление). |
| 9 | A | Block Public Access можно настроить на уровне bucket и на уровне всего аккаунта. |
| 10 | A | Presigned URLs предоставляют временный доступ к объекту без необходимости IAM credentials у получателя. |
| 11 | B | Для CRR требуется versioning на source bucket. Destination bucket может быть в другом регионе и аккаунте. |
| 12 | D | AWS рекомендует Multipart Upload для файлов > 100 MB. Обязательно для файлов > 5 GB. |
| 13 | C | Data transfer IN (загрузка в S3) бесплатна. Платите за storage, requests, и data transfer OUT. |
| 14 | B | S3 Select позволяет выполнять SQL запросы (SELECT) к CSV, JSON, Parquet файлам без полного скачивания. |
| 15 | A | S3 Event Notifications можно отправлять в Lambda, SQS, SNS, и Amazon EventBridge. |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **14-15 (90-100%)** | 🏆 Отлично! |
| **11-13 (70-89%)** | ✅ Хорошо |
| **8-10 (50-69%)** | ⚠️ Удовлетворительно |
| **< 8 (<50%)** | 📚 Нужно повторить |

---

