# Cloud Native Development - Quiz
## Multi-Cloud

---

## Question 1: Multi-Cloud Complexity

Какой главный недостаток multi-cloud стратегии?

A) Дешевле single cloud
B) Операционная сложность и требуемые навыки
C) Меньше сервисов доступно
D) Хуже производительность

---

## Question 2: Kubernetes Portability

Почему Kubernetes считается cloud-agnostic?

A) Принадлежит Google
B) Одинаковые манифесты работают на EKS, GKE, AKS
C) Не использует облачные сервисы
D) Бесплатный

---

## Question 3: Lock-in Level

Какой сервис имеет наивысший уровень vendor lock-in?

A) EC2 (виртуальные машины)
B) RDS PostgreSQL
C) DynamoDB
D) S3

---

## Question 4: Portable Alternative

Какая portable альтернатива AWS Lambda?

A) EC2
B) Knative на Kubernetes
C) Fargate
D) Step Functions

---

## Question 5: Pragmatic Approach

Какой прагматичный подход к multi-cloud?

A) Использовать только open source
B) Никогда не использовать managed services
C) Использовать proprietary сервисы когда value > lock-in risk
D) Всегда дублировать в двух clouds

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Multi-cloud требует экспертизы в нескольких clouds, сложнее networking, security, operations. |
| 2 | B | Kubernetes API стандартизирован. Те же YAML манифесты работают на любом managed K8s сервисе. |
| 3 | C | DynamoDB имеет proprietary data model и API. Миграция требует переписывания приложения. |
| 4 | B | Knative — CNCF проект для serverless на Kubernetes. Работает на любом K8s кластере. |
| 5 | C | Прагматичный подход: использовать managed сервисы когда их ценность превышает риск lock-in. |

---
