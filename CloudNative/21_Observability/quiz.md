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

A) Меньше размер логов
B) Легче парсить и искать, можно добавлять metadata
C) Быстрее пишется
D) Требуется по compliance

---

## Question 3: Trace vs Log

Что уникального предоставляют distributed traces?

A) Больше деталей об ошибках
B) Путь запроса через несколько сервисов с timing
C) Агрегированные метрики
D) Автоматические алерты

---

## Question 4: RED Method

Что означает RED в контексте метрик сервисов?

A) Read, Edit, Delete
B) Rate, Errors, Duration
C) Request, Error, Data
D) Real-time, Exact, Distributed

---

## Question 5: X-Ray Annotation vs Metadata

В чём разница между X-Ray Annotation и Metadata?

A) Annotations дороже
B) Annotations индексируются и searchable, Metadata — нет
C) Metadata только для errors
D) Разницы нет

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Три столпа observability: Logs (события), Metrics (числа), Traces (путь запроса). |
| 2 | B | Structured logging позволяет легко парсить, искать по полям, добавлять context (request_id, user_id). |
| 3 | B | Traces показывают как запрос проходит через сервисы с timing каждого компонента. |
| 4 | B | RED = Rate (requests/sec), Errors (failed/sec), Duration (latency distribution). |
| 5 | B | Annotations индексируются — можно искать traces по ним. Metadata не индексируется, для дополнительной информации. |

---
