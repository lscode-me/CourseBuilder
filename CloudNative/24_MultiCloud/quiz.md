# Cloud Native Development - Quiz
## Multi-Cloud

---

## Question 1: Multi-Cloud Complexity


Какой главный недостаток multi-cloud стратегии?

A) Хуже производительность

B) Дешевле single cloud

C) Операционная сложность и требуемые навыки

D) Меньше сервисов доступно

---

## Question 2: Kubernetes Portability


Почему Kubernetes считается cloud-agnostic?

A) Бесплатный

B) Не использует облачные сервисы

C) Одинаковые манифесты работают на EKS, GKE, AKS

D) Принадлежит Google

---

## Question 3: Lock-in Level


Какой сервис имеет наивысший уровень vendor lock-in?

A) EC2 (виртуальные машины)

B) DynamoDB

C) S3

D) RDS PostgreSQL

---

## Question 4: Portable Alternative


Какая portable альтернатива AWS Lambda?

A) Step Functions

B) Knative на Kubernetes

C) EC2

D) Fargate

---

## Question 5: Pragmatic Approach


Какой прагматичный подход к multi-cloud?

A) Всегда дублировать в двух clouds

B) Никогда не использовать managed services

C) Использовать только open source

D) Использовать proprietary сервисы когда value > lock-in risk

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Multi-cloud требует экспертизы в нескольких clouds, сложнее networking, security, operations. |
| 2 | C | Kubernetes API стандартизирован. Те же YAML манифесты работают на любом managed K8s сервисе. |
| 3 | B | DynamoDB имеет proprietary data model и API. Миграция требует переписывания приложения. |
| 4 | B | Knative — CNCF проект для serverless на Kubernetes. Работает на любом K8s кластере. |
| 5 | D | Прагматичный подход: использовать managed сервисы когда их ценность превышает риск lock-in. |

---
