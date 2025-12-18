# Cloud Native Development - Quiz
## Cost Management

---

## Question 1: Spot Instances

Какой discount можно получить с Spot instances?

A) До 100%

B) До 30%

C) До 50%

D) До 90%

---

## Question 2: Reserved vs Savings Plans

Какое преимущество Savings Plans над Reserved Instances?

A) Только для EC2

B) Гибкость в выборе instance types и regions

C) Больше discount

D) Нет commitment

---

## Question 3: S3 Storage Class

Какой storage class самый дешёвый для архивных данных?

A) Glacier Deep Archive

B) Standard-IA

C) Glacier Instant

D) Standard

---

## Question 4: Right-Sizing

Что такое right-sizing?

A) Использование только small instances

B) Увеличение размера instances

C) Удаление всех resources

D) Соответствие ресурсов фактическому использованию

---

## Question 5: Cost Visibility

Что необходимо для cost allocation по проектам/командам?

A) Reserved Instances

B) Spot Instances

C) Budgets

D) Tags на ресурсах

---

## Question 6: Cost Explorer

Что позволяет Cost Explorer?

A) Только budgets

B) Только текущие costs

C) Только billing

D) Визуализация, анализ и forecasting costs

---

## Question 7: Budgets

Для чего используются AWS Budgets?

A) Только для reports

B) Для alerting при превышении cost/usage thresholds

C) Только для optimization

D) Только для billing

---

## Question 8: Cost Anomaly Detection

Что делает Cost Anomaly Detection?

A) Удаляет ресурсы

B) Оптимизирует costs

C) ML-based обнаружение необычных cost spikes

D) Создаёт бюджеты

---

## Question 9: Compute Optimizer

Что рекомендует Compute Optimizer?

A) Только network

B) Right-sizing recommendations для EC2, Lambda, EBS

C) Только billing plans

D) Только storage

---

## Question 10: Trusted Advisor

Какие проверки включает Trusted Advisor?

A) Только costs

B) Только security

C) Cost optimization, performance, security, fault tolerance, service limits

D) Только limits

---

## Question 11: S3 Intelligent-Tiering

Как работает S3 Intelligent-Tiering?

A) Только для large objects

B) Только для archives

C) Manual tier selection

D) Автоматическое перемещение objects между tiers по access patterns

---

## Question 12: Instance Scheduler

Что делает AWS Instance Scheduler?

A) Создаёт instances

B) Backing up instances

C) Мониторит instances

D) Автоматический start/stop EC2 и RDS по расписанию

---

## Question 13: Cost Categories

Для чего используются Cost Categories?

A) Только для reports

B) Для группировки costs по custom rules (business unit, environment)

C) Только для tags

D) Только для billing

---

## Question 14: RI Coverage

Что показывает RI Coverage report?

A) Какой % usage покрыт Reserved Instances

B) RI pricing

C) RI expiration

D) RI inventory

---

## Question 15: Graviton

Какая экономия от AWS Graviton processors?

A) Нет экономии

B) 5%

C) До 40% при лучшей производительности

D) 1%

---

## Question 16: Data Transfer Costs

Как минимизировать data transfer costs?

A) Bigger instances

B) Больше трафика

C) More regions

D) VPC Endpoints, same AZ, CloudFront, compression

---

## Question 17: Billing Conductor

Для чего используется AWS Billing Conductor?

A) Custom billing для resellers и showback/chargeback

B) Только для discounts

C) Только для reports

D) Только для invoices

---

## Question 18: Commitment Discounts

Какие типы commitment discounts в AWS?

A) Только On-Demand

B) Только Spot

C) Только free tier

D) Reserved Instances, Savings Plans

---

## Question 19: Unused Resources

Как находить unused resources?

A) Manually

B) Trusted Advisor, Cost Explorer, custom scripts

C) Невозможно

D) Только через console

---

## Question 20: FinOps

Что такое FinOps?

A) Практика управления cloud costs с collaboration engineering и finance

B) Финансовый отдел

C) Только accounting

D) Только budgeting

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Spot instances: до 90% discount, но могут быть прерваны с 2-минутным предупреждением. |
| 2 | B | Savings Plans позволяют менять instance type и region, сохраняя discount. RIs привязаны к конкретному типу. |
| 3 | A | Glacier Deep Archive: $0.00099/GB — самый дешёвый, но retrieval занимает 12-48 часов. |
| 4 | D | Right-sizing: выбор размера ресурсов соответственно фактическому использованию (CPU, memory, IOPS). |
| 5 | D | Tags (Environment, Project, Team) позволяют группировать расходы в Cost Explorer по нужным измерениям. |
| 6 | D | Cost Explorer: визуализация и forecasting |
| 7 | B | Budgets: alerting на thresholds |
| 8 | C | Cost Anomaly Detection: ML для spikes |
| 9 | B | Compute Optimizer: right-sizing recommendations |
| 10 | C | Trusted Advisor: cost, performance, security, etc |
| 11 | D | Intelligent-Tiering: auto tier movement |
| 12 | D | Instance Scheduler: start/stop по расписанию |
| 13 | B | Cost Categories: custom grouping rules |
| 14 | A | RI Coverage: % usage covered by RIs |
| 15 | C | Graviton: до 40% savings |
| 16 | D | VPC Endpoints, same AZ, CloudFront, compression |
| 17 | A | Billing Conductor: custom billing |
| 18 | D | RIs и Savings Plans |
| 19 | B | Trusted Advisor, Cost Explorer, scripts |
| 20 | A | FinOps: collaboration engineering и finance |

---

