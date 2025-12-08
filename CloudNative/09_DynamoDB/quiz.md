# Cloud Native Development - Quiz
## DynamoDB: NoSQL Database

---

## Question 1: Primary Key

Какие варианты Primary Key поддерживает DynamoDB?

A) Только Partition Key

B) Только Partition Key + Sort Key

C) Partition Key only ИЛИ Partition Key + Sort Key

D) Любые три атрибута

---

## Question 2: GSI vs LSI

Какое ключевое отличие GSI от LSI?

A) GSI быстрее

B) GSI может иметь другой Partition Key, LSI — только другой Sort Key

C) LSI можно создать в любое время

D) GSI поддерживает strongly consistent reads

---

## Question 3: Query vs Scan

Почему Query предпочтительнее Scan?

A) Query читает только нужные items по индексу, Scan читает всю таблицу

B) Query дешевле в 10 раз

C) Scan не работает в production

D) Query поддерживает SQL синтаксис

---

## Question 4: Hot Partition

Что вызывает "hot partition" проблему?

A) Слишком большие items

B) Неравномерное распределение данных по Partition Key

C) Использование On-Demand режима

D) Слишком много GSI

---

## Question 5: DAX

Что такое DAX?

A) DynamoDB Access Extension

B) In-memory cache для DynamoDB с микросекундной latency

C) Инструмент для миграции данных

D) Мониторинг DynamoDB

---

## Question 6: Item Size Limit

Какой максимальный размер одного item в DynamoDB?

A) 64 KB

B) 400 KB

C) 1 MB

D) 5 MB

---

## Question 7: Capacity Mode

Когда лучше использовать On-Demand capacity?

A) Для постоянной высокой нагрузки

B) Для непредсказуемой или переменной нагрузки

C) Никогда, Provisioned всегда лучше

D) Только для тестирования

---

## Question 8: Global Tables

Какая модель репликации у Global Tables?

A) Single-master

B) Multi-master

C) Read replica only

D) No replication

---

## Question 9: DynamoDB Streams

Сколько времени хранятся записи в DynamoDB Stream?

A) 1 час

B) 24 часа

C) 7 дней

D) 30 дней

---

## Question 10: RCU Calculation

1 RCU позволяет прочитать сколько данных strongly consistent?

A) 1 KB per second

B) 4 KB per second

C) 1 MB per second

D) Зависит от item size

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | DynamoDB поддерживает: только Partition Key (simple) ИЛИ Partition Key + Sort Key (composite). |
| 2 | B | GSI позволяет задать другой Partition Key. LSI использует тот же PK, но другой Sort Key. |
| 3 | A | Query использует индексы и читает только matching items. Scan читает всю таблицу — очень дорого. |
| 4 | B | Hot partition возникает когда большинство запросов попадают на один PK (например, status = "active"). |
| 5 | B | DAX (DynamoDB Accelerator) — in-memory cache, снижающий latency до микросекунд. |
| 6 | B | Максимальный размер item — 400 KB включая все атрибуты и их имена. |
| 7 | B | On-Demand идеален для непредсказуемой нагрузки, новых приложений, переменного трафика. |
| 8 | B | Global Tables — multi-master: можно писать в любой регион, изменения реплицируются. |
| 9 | B | DynamoDB Streams хранит записи 24 часа. После этого они удаляются. |
| 10 | B | 1 RCU = 1 strongly consistent read до 4 KB/sec (или 2 eventually consistent reads). |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **9-10 (90-100%)** | 🏆 Отлично! |
| **7-8 (70-89%)** | ✅ Хорошо |
| **5-6 (50-69%)** | ⚠️ Удовлетворительно |
| **< 5 (<50%)** | 📚 Нужно повторить |

---
