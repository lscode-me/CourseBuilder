# Cloud Native Development - Quiz
## DynamoDB: NoSQL Database

---

## Question 1: Primary Key

Какие варианты Primary Key поддерживает DynamoDB?

A) Только Partition Key

B) Только Partition Key + Sort Key

C) Любые три атрибута

D) Partition Key only ИЛИ Partition Key + Sort Key

---

## Question 2: GSI vs LSI

Какое ключевое отличие GSI от LSI?

A) GSI быстрее

B) GSI может иметь другой Partition Key, LSI — только другой Sort Key

C) GSI поддерживает strongly consistent reads

D) LSI можно создать в любое время

---

## Question 3: Query vs Scan

Почему Query предпочтительнее Scan?

A) Query поддерживает SQL синтаксис

B) Query дешевле в 10 раз

C) Query читает только нужные items по индексу, Scan читает всю таблицу

D) Scan не работает в production

---

## Question 4: Hot Partition

Что вызывает "hot partition" проблему?

A) Слишком большие items

B) Использование On-Demand режима

C) Неравномерное распределение данных по Partition Key

D) Слишком много GSI

---

## Question 5: DAX

Что такое DAX?

A) DynamoDB Access Extension

B) Инструмент для миграции данных

C) Мониторинг DynamoDB

D) In-memory cache для DynamoDB с микросекундной latency

---

## Question 6: Item Size Limit

Какой максимальный размер одного item в DynamoDB?

A) 64 KB

B) 5 MB

C) 400 KB

D) 1 MB

---

## Question 7: Capacity Mode

Когда лучше использовать On-Demand capacity?

A) Только для тестирования

B) Никогда, Provisioned всегда лучше

C) Для непредсказуемой или переменной нагрузки

D) Для постоянной высокой нагрузки

---

## Question 8: Global Tables

Какая модель репликации у Global Tables?

A) No replication

B) Multi-master

C) Read replica only

D) Single-master

---

## Question 9: DynamoDB Streams

Сколько времени хранятся записи в DynamoDB Stream?

A) 24 часа

B) 7 дней

C) 1 час

D) 30 дней

---

## Question 10: RCU Calculation

1 RCU позволяет прочитать сколько данных strongly consistent?

A) Зависит от item size

B) 1 KB per second

C) 4 KB per second

D) 1 MB per second

---

## Question 11: WCU Calculation

1 WCU позволяет записать сколько данных?

A) 1 MB per second

B) 10 KB per second

C) 1 KB per second

D) 4 KB per second

---

## Question 12: Eventually Consistent

Сколько RCU нужно для eventually consistent read?

A) Такое же как strong

B) Бесплатно

C) 0.5 RCU (в 2 раза меньше)

D) 2 RCU

---

## Question 13: TTL

Для чего используется TTL в DynamoDB?

A) Для шифрования

B) Для резервного копирования

C) Для индексации

D) Для автоматического удаления устаревших items

---

## Question 14: Backup

Какие типы backup поддерживает DynamoDB?

A) Только PITR

B) On-demand и Point-in-Time Recovery (PITR)

C) Только manual

D) Нет backup

---

## Question 15: DAX

Что такое DAX?

A) Data Analysis eXtension

B) Database Access eXecution

C) Backup сервис

D) In-memory caching для DynamoDB

---

## Question 16: Batch Operations

Какой лимит items для BatchWriteItem?

A) 100

B) 1000

C) 10

D) 25

---

## Question 17: Query vs Scan

Чем Query отличается от Scan?

A) Ничем

B) Scan быстрее

C) Query использует partition key, Scan читает всю таблицу

D) Query дороже

---

## Question 18: Projection Expression

Что делает Projection Expression?

A) Сортирует данные

B) Фильтрует результаты

C) Выбирает только нужные атрибуты (экономит RCU)

D) Создаёт index

---

## Question 19: Condition Expression

Для чего используется Condition Expression?

A) Для шифрования

B) Для conditional write (write только если условие true)

C) Для сортировки

D) Для индексации

---

## Question 20: PartiQL

Что такое PartiQL в DynamoDB?

A) Partition manager

B) Backup tool

C) SQL-compatible query language для DynamoDB

D) Monitoring service

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | DynamoDB поддерживает: только Partition Key (simple) ИЛИ Partition Key + Sort Key (composite). |
| 2 | B | GSI позволяет задать другой Partition Key. LSI использует тот же PK, но другой Sort Key. |
| 3 | C | Query использует индексы и читает только matching items. Scan читает всю таблицу — очень дорого. |
| 4 | C | Hot partition возникает когда большинство запросов попадают на один PK (например, status = "active"). |
| 5 | D | DAX (DynamoDB Accelerator) — in-memory cache, снижающий latency до микросекунд. |
| 6 | C | Максимальный размер item — 400 KB включая все атрибуты и их имена. |
| 7 | C | On-Demand идеален для непредсказуемой нагрузки, новых приложений, переменного трафика. |
| 8 | B | Global Tables — multi-master: можно писать в любой регион, изменения реплицируются. |
| 9 | A | DynamoDB Streams хранит записи 24 часа. После этого они удаляются. |
| 10 | C | 1 RCU = 1 strongly consistent read до 4 KB/sec (или 2 eventually consistent reads). |
| 11 | C | 1 WCU = 1 write до 1 KB/sec |
| 12 | C | Eventually consistent read = 0.5 RCU |
| 13 | D | TTL автоматически удаляет устаревшие items |
| 14 | B | On-demand и PITR для backups |
| 15 | D | DAX — in-memory caching для DynamoDB |
| 16 | D | BatchWriteItem: максимум 25 items |
| 17 | C | Query использует partition key, Scan читает всё |
| 18 | C | Projection Expression выбирает нужные атрибуты |
| 19 | B | Condition Expression для conditional writes |
| 20 | C | PartiQL — SQL-compatible query language |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **9-10 (90-100%)** | 🏆 Отлично! |
| **7-8 (70-89%)** | ✅ Хорошо |
| **5-6 (50-69%)** | ⚠️ Удовлетворительно |
| **< 5 (<50%)** | 📚 Нужно повторить |

---

