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

A) Real-time, Exact, Distributed

B) Request, Error, Data

C) Rate, Errors, Duration

D) Read, Edit, Delete

---

## Question 5: X-Ray Annotation vs Metadata





В чём разница между X-Ray Annotation и Metadata?

A) Metadata только для errors

B) Annotations индексируются и searchable, Metadata — нет

C) Разницы нет

D) Annotations дороже

---

## Question 6: USE Method




Для каких ресурсов применяется USE Method?

A) Только для APIs

B) Для hardware/infrastructure resources (CPU, memory, disk)

C) Только для databases

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

A) Только billing

B) Только traces

C) Только logs

D) Metrics и logs для ECS и EKS clusters

---

## Question 9: CloudWatch Dashboards




Для чего используются CloudWatch Dashboards?

A) Только для alerting

B) Только для хранения метрик

C) Только для automation

D) Для визуализации metrics и logs

---

## Question 10: Embedded Metric Format




Что такое Embedded Metric Format?

A) Формат для traces

B) Формат для logs

C) Формат для dashboards

D) Логи со structured metrics для автоматического извлечения

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

A) Synthetic logs

B) Synthetic metrics

C) Создаёт synthetic data

D) Canary scripts для proactive monitoring endpoints

---

## Question 16: Application Insights




Что делает CloudWatch Application Insights?

A) Только metrics

B) Только logging

C) Автоматический setup monitoring для .NET/SQL Server apps

D) Только tracing

---

## Question 17: Log Retention




Как настроить log retention?

A) Автоматически

B) Retention policy per log group

C) Невозможно

D) Только через S3

---

## Question 18: Metric Math




Для чего используется Metric Math?

A) Калькулятор

B) Для создания derived metrics из других метрик

C) Только для billing

D) Только для алертов

---

## Question 19: Alarms Actions




Какие actions поддерживают CloudWatch Alarms?

A) Только SNS

B) SNS, Lambda, EC2 actions, Auto Scaling, Systems Manager

C) Только email

D) Только SMS

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
| 1 | B | Три столпа observability: Logs (события), Metrics (числа), Traces (путь запроса). |
| 2 | D | Structured logging позволяет легко парсить, искать по полям, добавлять context (request_id, user_id). |
| 3 | B | Traces показывают как запрос проходит через сервисы с timing каждого компонента. |
| 4 | C | RED = Rate (requests/sec), Errors (failed/sec), Duration (latency distribution). |
| 5 | B | Annotations индексируются — можно искать traces по ним. Metadata не индексируется, для дополнительной информации. |
| 6 | B | USE для hardware resources (CPU, memory, disk) |
| 7 | C | Logs Insights: SQL-like query для logs |
| 8 | D | Container Insights: metrics и logs для ECS/EKS |
| 9 | D | Dashboards для визуализации |
| 10 | D | EMF: logs со structured metrics |
| 11 | B | Sampling снижает overhead и cost |
| 12 | D | ServiceLens: unified view health |
| 13 | A | Anomaly Detection: ML для аномалий |
| 14 | D | Contributor Insights: top contributors |
| 15 | D | Synthetics: canary scripts для proactive monitoring |
| 16 | C | Application Insights: auto-setup для .NET/SQL |
| 17 | B | Retention policy per log group |
| 18 | B | Metric Math для derived metrics |
| 19 | B | Alarms: SNS, Lambda, EC2, ASG, SSM actions |
| 20 | B | Cross-account observability или centralized account |

---
