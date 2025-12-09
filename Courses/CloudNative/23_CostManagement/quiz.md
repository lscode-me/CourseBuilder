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

B) Нет commitment

C) Гибкость в выборе instance types и regions

D) Больше discount

---

## Question 3: S3 Storage Class





Какой storage class самый дешёвый для архивных данных?

A) Standard-IA

B) Standard

C) Glacier Instant

D) Glacier Deep Archive

---

## Question 4: Right-Sizing





Что такое right-sizing?

A) Использование только small instances

B) Соответствие ресурсов фактическому использованию

C) Увеличение размера instances

D) Удаление всех resources

---

## Question 5: Cost Visibility





Что необходимо для cost allocation по проектам/командам?

A) Tags на ресурсах

B) Budgets

C) Spot Instances

D) Reserved Instances

---

## Question 6: Cost Explorer




Что позволяет Cost Explorer?

A) Только текущие costs

B) Визуализация, анализ и forecasting costs

C) Только billing

D) Только budgets

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

A) Только security

B) Cost optimization, performance, security, fault tolerance, service limits

C) Только costs

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

A) До 40% при лучшей производительности

B) 1%

C) Нет экономии

D) 5%

---

## Question 16: Data Transfer Costs




Как минимизировать data transfer costs?

A) VPC Endpoints, same AZ, CloudFront, compression

B) More regions

C) Больше трафика

D) Bigger instances

---

## Question 17: Billing Conductor




Для чего используется AWS Billing Conductor?

A) Только для reports

B) Только для invoices

C) Custom billing для resellers и showback/chargeback

D) Только для discounts

---

## Question 18: Commitment Discounts




Какие типы commitment discounts в AWS?

A) Reserved Instances, Savings Plans

B) Только free tier

C) Только Spot

D) Только On-Demand

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
| 2 | C | Savings Plans позволяют менять instance type и region, сохраняя discount. RIs привязаны к конкретному типу. |
| 3 | D | Glacier Deep Archive: $0.00099/GB — самый дешёвый, но retrieval занимает 12-48 часов. |
| 4 | B | Right-sizing: выбор размера ресурсов соответственно фактическому использованию (CPU, memory, IOPS). |
| 5 | A | Tags (Environment, Project, Team) позволяют группировать расходы в Cost Explorer по нужным измерениям. |
| 6 | B | Cost Explorer: визуализация и forecasting |
| 7 | B | Budgets: alerting на thresholds |
| 8 | C | Cost Anomaly Detection: ML для spikes |
| 9 | B | Compute Optimizer: right-sizing recommendations |
| 10 | B | Trusted Advisor: cost, performance, security, etc |
| 11 | D | Intelligent-Tiering: auto tier movement |
| 12 | D | Instance Scheduler: start/stop по расписанию |
| 13 | B | Cost Categories: custom grouping rules |
| 14 | A | RI Coverage: % usage covered by RIs |
| 15 | A | Graviton: до 40% savings |
| 16 | A | VPC Endpoints, same AZ, CloudFront, compression |
| 17 | C | Billing Conductor: custom billing |
| 18 | A | RIs и Savings Plans |
| 19 | B | Trusted Advisor, Cost Explorer, scripts |
| 20 | A | FinOps: collaboration engineering и finance |

---
