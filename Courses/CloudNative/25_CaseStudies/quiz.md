# Cloud Native Development - Quiz
## Case Studies

---

## Question 1: E-commerce Cart







Какой сервис лучше для хранения shopping cart?

A) Aurora

B) ElastiCache

C) S3

D) DynamoDB

---

## Question 2: Real-time Analytics







Какой сервис использовать для ingestion streaming данных?

A) Athena

B) S3

C) Kinesis Data Streams

D) Redshift

---

## Question 3: Serverless Benefits







Какое главное преимущество serverless архитектуры?

A) Scale to zero и pay per use

B) Всегда дешевле

C) Проще debugging

D) Быстрее контейнеров

---

## Question 4: Microservices Communication







Какой сервис AWS обеспечивает service mesh с mTLS?

A) ALB

B) Route 53

C) App Mesh (или Istio на EKS)

D) API Gateway

---

## Question 5: Architecture Choice







Какая архитектура лучше для MVP/стартапа?

A) Kubernetes с микросервисами

B) Serverless (Lambda + API Gateway + DynamoDB)

C) Multi-region active-active

D) EC2 с monolith

---

## Question 6: E-commerce Platform






Какие сервисы для high-traffic e-commerce?

A) Только EC2

B) CloudFront, ALB, Auto Scaling, RDS Multi-AZ, ElastiCache

C) Только DynamoDB

D) Только Lambda

---

## Question 7: Data Lake






Какая архитектура для data lake?

A) Только Redshift

B) Только RDS

C) S3 + Glue + Athena + Lake Formation

D) Только DynamoDB

---

## Question 8: Machine Learning Pipeline






Какие сервисы для ML pipeline?

A) SageMaker, S3, Step Functions, Lambda

B) Только EC2

C) Только EMR

D) Только Lambda

---

## Question 9: Multi-Region DR






Как реализовать multi-region DR?

A) Только cold standby

B) Route 53 health checks, Aurora Global, S3 CRR, IaC для быстрого deploy

C) Нет DR

D) Backup только

---

## Question 10: IoT Platform






Какие сервисы для IoT platform?

A) Только RDS

B) Только S3

C) IoT Core, Kinesis, Lambda, DynamoDB, Timestream

D) Только EC2

---

## Question 11: Media Streaming






Какая архитектура для video streaming?

A) Только Lambda

B) Только EC2

C) Только S3

D) S3, CloudFront, MediaConvert, MediaLive

---

## Question 12: SaaS Multi-Tenant






Как реализовать multi-tenancy?

A) Нет изоляции

B) Только отдельные databases

C) Shared infra с tenant isolation (IAM, DynamoDB partition key)

D) Отдельный account для каждого tenant

---

## Question 13: Batch Processing






Какие сервисы для batch processing?

A) Только EC2

B) Только Lambda

C) AWS Batch, Step Functions, S3, Glue

D) Только ECS

---

## Question 14: API Platform






Как построить scalable API platform?

A) Только EC2

B) API Gateway, Lambda/ECS, DynamoDB, CloudFront

C) Только on-premises

D) Только monolith

---

## Question 15: DevOps Pipeline






Какие сервисы для CI/CD pipeline?

A) Только manual

B) Только GitHub Actions

C) Только Jenkins

D) CodePipeline, CodeBuild, CodeDeploy, ECR

---

## Question 16: Compliance Architecture






Как обеспечить compliance (HIPAA, PCI)?

A) Только encryption

B) Только IAM

C) Encryption, logging, access controls, Config Rules, audit trails

D) Только firewall

---

## Question 17: Cost-Optimized Architecture






Как оптимизировать costs для variable workloads?

A) Только On-Demand

B) Reserved Instances только

C) Spot + On-Demand mix, auto-scaling, right-sizing

D) Larger instances

---

## Question 18: Event-Driven Architecture






Какие сервисы для event-driven architecture?

A) Только SQS

B) EventBridge, SNS, SQS, Lambda, Step Functions

C) Только Lambda

D) Только Kinesis

---

## Question 19: Legacy Migration






Как мигрировать legacy application?

A) Оставить on-premises

B) Только containerize

C) Переписать сразу

D) Lift-and-shift → re-platform → refactor (постепенно)

---

## Question 20: High Availability






Как обеспечить 99.99% availability?

A) Только monitoring

B) Multi-AZ, auto-scaling, health checks, redundancy на всех уровнях

C) Single AZ

D) Только backup

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | DynamoDB: низкая latency, auto-scaling, TTL для expiration сессий. Aurora — для транзакционных данных. |
| 2 | C | Kinesis Data Streams: real-time ingestion с sub-second latency. S3/Athena — для batch. |
| 3 | A | Serverless: автоматическое масштабирование до нуля, оплата только за использование. |
| 4 | C | App Mesh (AWS) или Istio (на EKS) обеспечивают service mesh с mTLS, traffic management. |
| 5 | B | Serverless: быстрый старт, минимум ops, дёшево при низком трафике, масштабируется при росте. |
| 6 | B | CloudFront, ALB, ASG, RDS Multi-AZ, ElastiCache |
| 7 | C | S3 + Glue + Athena + Lake Formation |
| 8 | A | SageMaker, S3, Step Functions, Lambda |
| 9 | B | Route 53, Aurora Global, S3 CRR, IaC |
| 10 | C | IoT Core, Kinesis, Lambda, DynamoDB, Timestream |
| 11 | D | S3, CloudFront, MediaConvert, MediaLive |
| 12 | C | Shared infra с tenant isolation |
| 13 | C | AWS Batch, Step Functions, S3, Glue |
| 14 | B | API Gateway, Lambda/ECS, DynamoDB, CloudFront |
| 15 | D | CodePipeline, CodeBuild, CodeDeploy, ECR |
| 16 | C | Encryption, logging, access, Config, audit |
| 17 | C | Spot + On-Demand, auto-scaling, right-sizing |
| 18 | B | EventBridge, SNS, SQS, Lambda, Step Functions |
| 19 | D | Lift-and-shift → re-platform → refactor |
| 20 | B | Multi-AZ, ASG, health checks, redundancy |

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
