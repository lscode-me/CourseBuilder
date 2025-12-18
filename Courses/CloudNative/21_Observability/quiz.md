# Cloud Native Development - Quiz
## Observability

---

## Question 1: Три столпа

Какие три столпа observability?

A) Logs, Alerts, Dashboards

B) CPU, Memory, Network

C) Logs, Metrics, Traces

D) Monitoring, Alerting, Logging

---

## Question 2: Structured Logging

Почему structured logging (JSON) лучше plain text?

A) Быстрее пишется

B) Требуется по compliance

C) Меньше размер логов

D) Легче парсить и искать, можно добавлять metadata

---

## Question 3: Trace vs Log

Что уникального предоставляют distributed traces?

A) Агрегированные метрики

B) Путь запроса через несколько сервисов с timing

C) Автоматические алерты

D) Больше деталей об ошибках

---

## Question 4: RED Method

Что означает RED в контексте метрик сервисов?

A) Request, Error, Data

B) Read, Edit, Delete

C) Rate, Errors, Duration

D) Real-time, Exact, Distributed

---

## Question 5: X-Ray Annotation vs Metadata

В чём разница между X-Ray Annotation и Metadata?

A) Annotations дороже

B) Разницы нет

C) Annotations индексируются и searchable, Metadata — нет

D) Metadata только для errors

---

## Question 6: USE Method

Для каких ресурсов применяется USE Method?

A) Для hardware/infrastructure resources (CPU, memory, disk)

B) Только для databases

C) Только для APIs

D) Только для networks

---

## Question 7: CloudWatch Logs Insights

Для чего используется CloudWatch Logs Insights?

A) Только для storage

B) Только для alerting

C) Для query и analysis логов с SQL-like синтаксисом

D) Только для metrics

---

## Question 8: Container Insights

Что предоставляет Container Insights?

A) Только traces

B) Только billing

C) Metrics и logs для ECS и EKS clusters

D) Только logs

---

## Question 9: CloudWatch Dashboards

Для чего используются CloudWatch Dashboards?

A) Для визуализации metrics и logs

B) Только для automation

C) Только для хранения метрик

D) Только для alerting

---

## Question 10: Embedded Metric Format

Что такое Embedded Metric Format?

A) Логи со structured metrics для автоматического извлечения

B) Формат для dashboards

C) Формат для logs

D) Формат для traces

---

## Question 11: X-Ray Sampling

Зачем нужен sampling в X-Ray?

A) Для красоты

B) Для снижения overhead и стоимости

C) Для compliance

D) Для security

---

## Question 12: ServiceLens

Что такое CloudWatch ServiceLens?

A) Только logging

B) Только alerting

C) Только monitoring

D) Unified view: metrics, traces, logs для service health

---

## Question 13: Anomaly Detection

Что делает CloudWatch Anomaly Detection?

A) ML-based обнаружение аномальных значений metrics

B) Удаляет аномалии

C) Создаёт аномалии

D) Только для security

---

## Question 14: Contributor Insights

Для чего используется CloudWatch Contributor Insights?

A) Только для security

B) Только для logs

C) Только для billing

D) Для анализа top contributors (top IPs, users, etc.)

---

## Question 15: Synthetics

Что делает CloudWatch Synthetics?

A) Synthetic metrics

B) Synthetic logs

C) Canary scripts для proactive monitoring endpoints

D) Создаёт synthetic data

---

## Question 16: Application Insights

Что делает CloudWatch Application Insights?

A) Автоматический setup monitoring для .NET/SQL Server apps

B) Только tracing

C) Только metrics

D) Только logging

---

## Question 17: Log Retention

Как настроить log retention?

A) Автоматически

B) Невозможно

C) Только через S3

D) Retention policy per log group

---

## Question 18: Metric Math

Для чего используется Metric Math?

A) Для создания derived metrics из других метрик

B) Только для billing

C) Калькулятор

D) Только для алертов

---

## Question 19: Alarms Actions

Какие actions поддерживают CloudWatch Alarms?

A) Только SNS

B) Только SMS

C) SNS, Lambda, EC2 actions, Auto Scaling, Systems Manager

D) Только email

---

## Question 20: Cross-Account Observability

Как реализовать cross-account observability?

A) Только через S3

B) CloudWatch cross-account observability или centralized logging account

C) Только вручную

D) Невозможно

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Три столпа observability: Logs (события), Metrics (числа), Traces (путь запроса). |
| 2 | D | Structured logging позволяет легко парсить, искать по полям, добавлять context (request_id, user_id). |
| 3 | B | Traces показывают как запрос проходит через сервисы с timing каждого компонента. |
| 4 | C | RED = Rate (requests/sec), Errors (failed/sec), Duration (latency distribution). |
| 5 | C | Annotations индексируются — можно искать traces по ним. Metadata не индексируется, для дополнительной информации. |
| 6 | A | USE для hardware resources (CPU, memory, disk) |
| 7 | C | Logs Insights: SQL-like query для logs |
| 8 | C | Container Insights: metrics и logs для ECS/EKS |
| 9 | A | Dashboards для визуализации |
| 10 | A | EMF: logs со structured metrics |
| 11 | B | Sampling снижает overhead и cost |
| 12 | D | ServiceLens: unified view health |
| 13 | A | Anomaly Detection: ML для аномалий |
| 14 | D | Contributor Insights: top contributors |
| 15 | C | Synthetics: canary scripts для proactive monitoring |
| 16 | A | Application Insights: auto-setup для .NET/SQL |
| 17 | D | Retention policy per log group |
| 18 | A | Metric Math для derived metrics |
| 19 | C | Alarms: SNS, Lambda, EC2, ASG, SSM actions |
| 20 | B | Cross-account observability или centralized account |

---

