# Cloud Native Development - Quiz
## RDS: Relational Database Service

---

## Question 1: Multi-AZ Replication


Какой тип репликации используется в Multi-AZ deployment?

A) Synchronous

B) Semi-synchronous

C) Asynchronous

D) No replication

---

## Question 2: Read Replicas


Можно ли читать данные из Standby instance в Multi-AZ deployment?

A) Да, но с задержкой 5 минут

B) Да, всегда

C) Да, но только через отдельный endpoint

D) Нет, Standby только для failover

---

## Question 3: Aurora Storage


Сколько копий данных хранит Aurora по умолчанию?

A) 3 копии в 2 AZ

B) 9 копий в 3 AZ

C) 2 копии в 1 AZ

D) 6 копий в 3 AZ

---

## Question 4: Read Replica Promotion


Что происходит при promote Read Replica?

A) Создаётся новый standby

B) Ничего не меняется

C) Replica становится standalone primary DB

D) Replica удаляется

---

## Question 5: Encryption


Когда можно включить encryption at rest для RDS?

A) Только для Aurora

B) Только после первого backup

C) В любое время

D) Только при создании instance

---

## Question 6: Backup Retention


Какой максимальный retention period для automated backups?

A) 35 дней

B) 7 дней

C) 365 дней

D) 14 дней

---

## Question 7: Aurora Serverless


Что такое ACU в Aurora Serverless?

A) Aurora Compute Unit (единица вычислительной мощности)

B) Aurora Capacity Unit

C) Aurora Connection Unit

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

A) Read Replica

B) Parameter Group

C) Multi-AZ

D) Automated Backup

---

## Question 10: IAM Authentication


Какой сервис используется для IAM Database Authentication?

A) Secrets Manager

B) STS для генерации token

C) IAM напрямую

D) Cognito

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Multi-AZ использует synchronous replication для гарантии durability. Read Replicas — async. |
| 2 | D | Standby в Multi-AZ не доступен для чтения — только для failover. Для чтения нужны Read Replicas. |
| 3 | D | Aurora хранит 6 копий данных в 3 AZ (по 2 копии на AZ) для высокой durability. |
| 4 | C | При promote Read Replica становится независимым primary DB, разрывая связь с источником. |
| 5 | D | Encryption at rest можно включить только при создании. Для existing DB: snapshot → copy encrypted → restore. |
| 6 | A | Максимальный retention period для automated backups — 35 дней. Manual snapshots хранятся до удаления. |
| 7 | B | ACU = Aurora Capacity Unit. 1 ACU ≈ 2 GB RAM. Aurora Serverless масштабируется в ACU. |
| 8 | A | Multi-AZ failover занимает 60-120 секунд. Aurora — быстрее (<30 секунд). |
| 9 | A | Cross-Region Read Replica позволяет реплицировать данные в другой регион для DR или локализации. |
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
