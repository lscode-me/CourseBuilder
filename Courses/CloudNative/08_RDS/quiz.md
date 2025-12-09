# Cloud Native Development - Quiz
## RDS: Relational Database Service

---

## Question 1: Multi-AZ Replication







Какой тип репликации используется в Multi-AZ deployment?

A) Asynchronous

B) Synchronous

C) No replication

D) Semi-synchronous

---

## Question 2: Read Replicas







Можно ли читать данные из Standby instance в Multi-AZ deployment?

A) Да, всегда

B) Да, но только через отдельный endpoint

C) Нет, Standby только для failover

D) Да, но с задержкой 5 минут

---

## Question 3: Aurora Storage







Сколько копий данных хранит Aurora по умолчанию?

A) 3 копии в 2 AZ

B) 9 копий в 3 AZ

C) 6 копий в 3 AZ

D) 2 копии в 1 AZ

---

## Question 4: Read Replica Promotion







Что происходит при promote Read Replica?

A) Replica становится standalone primary DB

B) Ничего не меняется

C) Создаётся новый standby

D) Replica удаляется

---

## Question 5: Encryption







Когда можно включить encryption at rest для RDS?

A) Только для Aurora

B) Только после первого backup

C) Только при создании instance

D) В любое время

---

## Question 6: Backup Retention







Какой максимальный retention period для automated backups?

A) 35 дней

B) 7 дней

C) 14 дней

D) 365 дней

---

## Question 7: Aurora Serverless







Что такое ACU в Aurora Serverless?

A) Aurora Connection Unit

B) Aurora Compute Unit (единица вычислительной мощности)

C) Aurora Capacity Unit

D) Aurora Cache Unit

---

## Question 8: Failover Time







Какое примерное время failover для Multi-AZ?

A) 60-120 секунд

B) 1-5 секунд

C) 5-10 минут

D) 30+ минут

---

## Question 9: Cross-Region







Какая функция RDS позволяет репликацию в другой регион?

A) Parameter Group

B) Automated Backup

C) Read Replica

D) Multi-AZ

---

## Question 10: IAM Authentication







Какой сервис используется для IAM Database Authentication?

A) STS для генерации token

B) Cognito

C) IAM напрямую

D) Secrets Manager

---

## Question 11: Performance Insights






Что показывает RDS Performance Insights?

A) Database load, top SQLs, wait events

B) Только CPU

C) Только network

D) Только storage

---

## Question 12: Enhanced Monitoring






Чем Enhanced Monitoring отличается от стандартного?

A) Ничем

B) Бесплатно

C) Метрики OS уровня (processes, memory details) с 1-sec granularity

D) Только для Aurora

---

## Question 13: Parameter Groups






Для чего используются Parameter Groups?

A) Для networking

B) Для настройки параметров database engine

C) Для backup

D) Для security

---

## Question 14: Option Groups






Что такое Option Groups в RDS?

A) Security options

B) Engine-specific features (Oracle TDE, SQL Server Audit)

C) Billing options

D) Networking options

---

## Question 15: Snapshot






Какой тип snapshot можно копировать между регионами?

A) Никакой

B) Только automated

C) Только encrypted

D) Manual snapshots

---

## Question 16: Encryption






Когда можно включить шифрование для RDS?

A) Только при создании (или через snapshot копию)

B) В любое время

C) Нельзя

D) Только для Enterprise

---

## Question 17: Aurora Serverless






Какое преимущество Aurora Serverless v2?

A) Только дешевле

B) Больше storage

C) Автоматическое масштабирование capacity

D) Быстрее

---

## Question 18: Proxy






Для чего используется RDS Proxy?

A) Для backup

B) Для monitoring

C) Для connection pooling и failover

D) Для encryption

---

## Question 19: Blue/Green Deployment






Что обеспечивает RDS Blue/Green deployment?

A) Шифрование

B) Monitoring

C) Безопасное тестирование изменений с быстрым switchover

D) Backup

---

## Question 20: Reserved Instances






Какая экономия от RDS Reserved Instances?

A) 10%

B) 5%

C) Нет экономии

D) До 72% (1-3 года commitment)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Multi-AZ использует synchronous replication для гарантии durability. Read Replicas — async. |
| 2 | C | Standby в Multi-AZ не доступен для чтения — только для failover. Для чтения нужны Read Replicas. |
| 3 | C | Aurora хранит 6 копий данных в 3 AZ (по 2 копии на AZ) для высокой durability. |
| 4 | A | При promote Read Replica становится независимым primary DB, разрывая связь с источником. |
| 5 | C | Encryption at rest можно включить только при создании. Для existing DB: snapshot → copy encrypted → restore. |
| 6 | A | Максимальный retention period для automated backups — 35 дней. Manual snapshots хранятся до удаления. |
| 7 | C | ACU = Aurora Capacity Unit. 1 ACU ≈ 2 GB RAM. Aurora Serverless масштабируется в ACU. |
| 8 | A | Multi-AZ failover занимает 60-120 секунд. Aurora — быстрее (<30 секунд). |
| 9 | C | Cross-Region Read Replica позволяет реплицировать данные в другой регион для DR или локализации. |
| 10 | A | IAM Database Auth использует STS (Security Token Service) для генерации временного token вместо пароля. |
| 11 | A | Performance Insights показывает database load, top SQLs |
| 12 | C | Enhanced Monitoring — OS метрики с 1-sec granularity |
| 13 | B | Parameter Groups для настройки параметров engine |
| 14 | B | Option Groups — engine-specific features |
| 15 | D | Manual snapshots можно копировать между регионами |
| 16 | A | Шифрование только при создании или через snapshot |
| 17 | C | Aurora Serverless v2 — автоматическое масштабирование |
| 18 | C | RDS Proxy для connection pooling и failover |
| 19 | C | Blue/Green для безопасного тестирования изменений |
| 20 | D | Reserved Instances экономят до 72% |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **9-10 (90-100%)** | 🏆 Отлично! |
| **7-8 (70-89%)** | ✅ Хорошо |
| **5-6 (50-69%)** | ⚠️ Удовлетворительно |
| **< 5 (<50%)** | 📚 Нужно повторить |

---
