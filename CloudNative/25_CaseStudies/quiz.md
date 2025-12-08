# Cloud Native Development - Quiz
## Case Studies

---

## Question 1: E-commerce Cart

Какой сервис лучше для хранения shopping cart?

A) Aurora
B) DynamoDB
C) S3
D) ElastiCache

---

## Question 2: Real-time Analytics

Какой сервис использовать для ingestion streaming данных?

A) S3
B) Kinesis Data Streams
C) Athena
D) Redshift

---

## Question 3: Serverless Benefits

Какое главное преимущество serverless архитектуры?

A) Всегда дешевле
B) Scale to zero и pay per use
C) Быстрее контейнеров
D) Проще debugging

---

## Question 4: Microservices Communication

Какой сервис AWS обеспечивает service mesh с mTLS?

A) API Gateway
B) ALB
C) App Mesh (или Istio на EKS)
D) Route 53

---

## Question 5: Architecture Choice

Какая архитектура лучше для MVP/стартапа?

A) Kubernetes с микросервисами
B) Serverless (Lambda + API Gateway + DynamoDB)
C) EC2 с monolith
D) Multi-region active-active

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DynamoDB: низкая latency, auto-scaling, TTL для expiration сессий. Aurora — для транзакционных данных. |
| 2 | B | Kinesis Data Streams: real-time ingestion с sub-second latency. S3/Athena — для batch. |
| 3 | B | Serverless: автоматическое масштабирование до нуля, оплата только за использование. |
| 4 | C | App Mesh (AWS) или Istio (на EKS) обеспечивают service mesh с mTLS, traffic management. |
| 5 | B | Serverless: быстрый старт, минимум ops, дёшево при низком трафике, масштабируется при росте. |

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
