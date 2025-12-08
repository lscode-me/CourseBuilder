# Cloud Native Development - Quiz
## RDS: Relational Database Service

---

## Question 1: Multi-AZ Replication

Какой тип репликации используется в Multi-AZ deployment?

A) Asynchronous

B) Synchronous

C) Semi-synchronous

D) No replication

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

A) 2 копии в 1 AZ

B) 3 копии в 2 AZ

C) 6 копий в 3 AZ

D) 9 копий в 3 AZ

---

## Question 4: Read Replica Promotion

Что происходит при promote Read Replica?

A) Replica удаляется

B) Replica становится standalone primary DB

C) Ничего не меняется

D) Создаётся новый standby

---

## Question 5: Encryption

Когда можно включить encryption at rest для RDS?

A) В любое время

B) Только при создании instance

C) Только после первого backup

D) Только для Aurora

---

## Question 6: Backup Retention

Какой максимальный retention period для automated backups?

A) 7 дней

B) 14 дней

C) 35 дней

D) 365 дней

---

## Question 7: Aurora Serverless

Что такое ACU в Aurora Serverless?

A) Aurora Compute Unit (единица вычислительной мощности)

B) Aurora Cache Unit

C) Aurora Connection Unit

D) Aurora Capacity Unit

---

## Question 8: Failover Time

Какое примерное время failover для Multi-AZ?

A) 1-5 секунд

B) 60-120 секунд

C) 5-10 минут

D) 30+ минут

---

## Question 9: Cross-Region

Какая функция RDS позволяет репликацию в другой регион?

A) Multi-AZ

B) Read Replica

C) Automated Backup

D) Parameter Group

---

## Question 10: IAM Authentication

Какой сервис используется для IAM Database Authentication?

A) IAM напрямую

B) STS для генерации token

C) Secrets Manager

D) Cognito

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Multi-AZ использует synchronous replication для гарантии durability. Read Replicas — async. |
| 2 | C | Standby в Multi-AZ не доступен для чтения — только для failover. Для чтения нужны Read Replicas. |
| 3 | C | Aurora хранит 6 копий данных в 3 AZ (по 2 копии на AZ) для высокой durability. |
| 4 | B | При promote Read Replica становится независимым primary DB, разрывая связь с источником. |
| 5 | B | Encryption at rest можно включить только при создании. Для existing DB: snapshot → copy encrypted → restore. |
| 6 | C | Максимальный retention period для automated backups — 35 дней. Manual snapshots хранятся до удаления. |
| 7 | D | ACU = Aurora Capacity Unit. 1 ACU ≈ 2 GB RAM. Aurora Serverless масштабируется в ACU. |
| 8 | B | Multi-AZ failover занимает 60-120 секунд. Aurora — быстрее (<30 секунд). |
| 9 | B | Cross-Region Read Replica позволяет реплицировать данные в другой регион для DR или локализации. |
| 10 | B | IAM Database Auth использует STS (Security Token Service) для генерации временного token вместо пароля. |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **9-10 (90-100%)** | 🏆 Отлично! |
| **7-8 (70-89%)** | ✅ Хорошо |
| **5-6 (50-69%)** | ⚠️ Удовлетворительно |
| **< 5 (<50%)** | 📚 Нужно повторить |

---
