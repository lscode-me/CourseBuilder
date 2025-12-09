# Cloud Native Development - Quiz
## DynamoDB: NoSQL Database

---

## Question 1: Primary Key


Какие варианты Primary Key поддерживает DynamoDB?

A) Partition Key only ИЛИ Partition Key + Sort Key

B) Любые три атрибута

C) Только Partition Key

D) Только Partition Key + Sort Key

---

## Question 2: GSI vs LSI


Какое ключевое отличие GSI от LSI?

A) GSI поддерживает strongly consistent reads

B) GSI быстрее

C) GSI может иметь другой Partition Key, LSI — только другой Sort Key

D) LSI можно создать в любое время

---

## Question 3: Query vs Scan


Почему Query предпочтительнее Scan?

A) Query поддерживает SQL синтаксис

B) Scan не работает в production

C) Query читает только нужные items по индексу, Scan читает всю таблицу

D) Query дешевле в 10 раз

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

A) Мониторинг DynamoDB

B) Инструмент для миграции данных

C) In-memory cache для DynamoDB с микросекундной latency

D) DynamoDB Access Extension

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

A) Никогда, Provisioned всегда лучше

B) Для непредсказуемой или переменной нагрузки

C) Только для тестирования

D) Для постоянной высокой нагрузки

---

## Question 8: Global Tables


Какая модель репликации у Global Tables?

A) Single-master

B) No replication

C) Read replica only

D) Multi-master

---

## Question 9: DynamoDB Streams


Сколько времени хранятся записи в DynamoDB Stream?

A) 7 дней

B) 24 часа

C) 30 дней

D) 1 час

---

## Question 10: RCU Calculation


1 RCU позволяет прочитать сколько данных strongly consistent?

A) 1 KB per second

B) 4 KB per second

C) Зависит от item size

D) 1 MB per second

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | DynamoDB поддерживает: только Partition Key (simple) ИЛИ Partition Key + Sort Key (composite). |
| 2 | C | GSI позволяет задать другой Partition Key. LSI использует тот же PK, но другой Sort Key. |
| 3 | C | Query использует индексы и читает только matching items. Scan читает всю таблицу — очень дорого. |
| 4 | C | Hot partition возникает когда большинство запросов попадают на один PK (например, status = "active"). |
| 5 | C | DAX (DynamoDB Accelerator) — in-memory cache, снижающий latency до микросекунд. |
| 6 | B | Максимальный размер item — 400 KB включая все атрибуты и их имена. |
| 7 | B | On-Demand идеален для непредсказуемой нагрузки, новых приложений, переменного трафика. |
| 8 | D | Global Tables — multi-master: можно писать в любой регион, изменения реплицируются. |
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
