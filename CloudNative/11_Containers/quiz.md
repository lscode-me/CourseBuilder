# Cloud Native Development - Quiz
## Containers: ECS, EKS, Fargate

---

## Question 1: ECS vs EKS


Какое ключевое отличие EKS от ECS?

A) EKS дешевле

B) EKS — managed Kubernetes, ECS — AWS-native orchestrator

C) EKS не поддерживает EC2

D) ECS не поддерживает Fargate

---

## Question 2: Fargate


Что такое AWS Fargate?

A) CI/CD сервис

B) Serverless compute для контейнеров

C) Kubernetes distribution

D) Container registry

---

## Question 3: ECS Control Plane Cost


Сколько стоит ECS control plane?

A) $0.10 per hour

B) $73/month

C) $0.05 per task

D) Бесплатно

---

## Question 4: Task Definition


Что определяет Task Definition в ECS?

A) Количество запущенных контейнеров

B) VPC configuration

C) Конфигурацию контейнеров (image, CPU, memory, ports, etc.)

D) Billing information

---

## Question 5: awsvpc Network Mode


Что происходит при использовании awsvpc network mode?

A) Tasks общаются только через public IP

B) Networking отключён

C) Все tasks делят один IP

D) Каждая task получает свой ENI и private IP

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | EKS — managed Kubernetes (CNCF стандарт). ECS — собственный AWS orchestrator с simpler API. |
| 2 | B | Fargate — serverless compute для ECS и EKS. AWS управляет EC2 instances за вас. |
| 3 | D | ECS control plane бесплатен. EKS control plane стоит $0.10/hour (~$73/month). |
| 4 | C | Task Definition — blueprint для контейнеров: image, CPU, memory, ports, env vars, IAM role, logs. |
| 5 | D | awsvpc даёт каждой task отдельный ENI с private IP в VPC subnet и собственные Security Groups. |

---
