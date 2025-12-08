# Cloud Native Development - Quiz
## Containers: ECS, EKS, Fargate

---

## Question 1: ECS vs EKS

Какое ключевое отличие EKS от ECS?

A) EKS дешевле
B) EKS — managed Kubernetes, ECS — AWS-native orchestrator
C) ECS не поддерживает Fargate
D) EKS не поддерживает EC2

---

## Question 2: Fargate

Что такое AWS Fargate?

A) Container registry
B) Serverless compute для контейнеров
C) Kubernetes distribution
D) CI/CD сервис

---

## Question 3: ECS Control Plane Cost

Сколько стоит ECS control plane?

A) $0.10 per hour
B) $73/month
C) Бесплатно
D) $0.05 per task

---

## Question 4: Task Definition

Что определяет Task Definition в ECS?

A) Количество запущенных контейнеров
B) Конфигурацию контейнеров (image, CPU, memory, ports, etc.)
C) Billing information
D) VPC configuration

---

## Question 5: awsvpc Network Mode

Что происходит при использовании awsvpc network mode?

A) Все tasks делят один IP
B) Каждая task получает свой ENI и private IP
C) Tasks общаются только через public IP
D) Networking отключён

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | EKS — managed Kubernetes (CNCF стандарт). ECS — собственный AWS orchestrator с simpler API. |
| 2 | B | Fargate — serverless compute для ECS и EKS. AWS управляет EC2 instances за вас. |
| 3 | C | ECS control plane бесплатен. EKS control plane стоит $0.10/hour (~$73/month). |
| 4 | B | Task Definition — blueprint для контейнеров: image, CPU, memory, ports, env vars, IAM role, logs. |
| 5 | B | awsvpc даёт каждой task отдельный ENI с private IP в VPC subnet и собственные Security Groups. |

---
