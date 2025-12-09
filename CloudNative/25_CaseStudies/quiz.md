# Cloud Native Development - Quiz
## Case Studies

---

## Question 1: E-commerce Cart


Какой сервис лучше для хранения shopping cart?

A) Aurora

B) S3

C) ElastiCache

D) DynamoDB

---

## Question 2: Real-time Analytics


Какой сервис использовать для ingestion streaming данных?

A) S3

B) Redshift

C) Kinesis Data Streams

D) Athena

---

## Question 3: Serverless Benefits


Какое главное преимущество serverless архитектуры?

A) Scale to zero и pay per use

B) Проще debugging

C) Быстрее контейнеров

D) Всегда дешевле

---

## Question 4: Microservices Communication


Какой сервис AWS обеспечивает service mesh с mTLS?

A) App Mesh (или Istio на EKS)

B) ALB

C) Route 53

D) API Gateway

---

## Question 5: Architecture Choice


Какая архитектура лучше для MVP/стартапа?

A) Serverless (Lambda + API Gateway + DynamoDB)

B) Kubernetes с микросервисами

C) EC2 с monolith

D) Multi-region active-active

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | DynamoDB: низкая latency, auto-scaling, TTL для expiration сессий. Aurora — для транзакционных данных. |
| 2 | C | Kinesis Data Streams: real-time ingestion с sub-second latency. S3/Athena — для batch. |
| 3 | A | Serverless: автоматическое масштабирование до нуля, оплата только за использование. |
| 4 | A | App Mesh (AWS) или Istio (на EKS) обеспечивают service mesh с mTLS, traffic management. |
| 5 | A | Serverless: быстрый старт, минимум ops, дёшево при низком трафике, масштабируется при росте. |

---

## 🎓 Congratulations!

Вы завершили курс Cloud Native Development!

Основные темы, которые мы изучили:
- Cloud Architecture и AWS сервисы
- Compute: EC2, Lambda, ECS, EKS
- Storage: S3, EBS, DynamoDB, RDS
- Networking: VPC, API Gateway, CloudFront
- Cloud Native: 12-Factor, Microservices
- DevOps: IaC, CI/CD, Observability
- Security и Cost Management

---
