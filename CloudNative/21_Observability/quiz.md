# Cloud Native Development - Quiz
## Observability

---

## Question 1: Три столпа


Какие три столпа observability?

A) Logs, Alerts, Dashboards

B) Logs, Metrics, Traces

C) Monitoring, Alerting, Logging

D) CPU, Memory, Network

---

## Question 2: Structured Logging


Почему structured logging (JSON) лучше plain text?

A) Легче парсить и искать, можно добавлять metadata

B) Требуется по compliance

C) Меньше размер логов

D) Быстрее пишется

---

## Question 3: Trace vs Log


Что уникального предоставляют distributed traces?

A) Агрегированные метрики

B) Больше деталей об ошибках

C) Автоматические алерты

D) Путь запроса через несколько сервисов с timing

---

## Question 4: RED Method


Что означает RED в контексте метрик сервисов?

A) Real-time, Exact, Distributed

B) Request, Error, Data

C) Rate, Errors, Duration

D) Read, Edit, Delete

---

## Question 5: X-Ray Annotation vs Metadata


В чём разница между X-Ray Annotation и Metadata?

A) Annotations индексируются и searchable, Metadata — нет

B) Annotations дороже

C) Metadata только для errors

D) Разницы нет

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Три столпа observability: Logs (события), Metrics (числа), Traces (путь запроса). |
| 2 | A | Structured logging позволяет легко парсить, искать по полям, добавлять context (request_id, user_id). |
| 3 | D | Traces показывают как запрос проходит через сервисы с timing каждого компонента. |
| 4 | C | RED = Rate (requests/sec), Errors (failed/sec), Duration (latency distribution). |
| 5 | A | Annotations индексируются — можно искать traces по ним. Metadata не индексируется, для дополнительной информации. |

---
