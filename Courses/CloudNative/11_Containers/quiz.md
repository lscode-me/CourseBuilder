# Cloud Native Development - Quiz
## Containers: ECS, EKS, Fargate

---

## Question 1: ECS vs EKS





Какое ключевое отличие EKS от ECS?

A) ECS не поддерживает Fargate

B) EKS не поддерживает EC2

C) EKS — managed Kubernetes, ECS — AWS-native orchestrator

D) EKS дешевле

---

## Question 2: Fargate





Что такое AWS Fargate?

A) Serverless compute для контейнеров

B) Kubernetes distribution

C) Container registry

D) CI/CD сервис

---

## Question 3: ECS Control Plane Cost





Сколько стоит ECS control plane?

A) $0.10 per hour

B) Бесплатно

C) $0.05 per task

D) $73/month

---

## Question 4: Task Definition





Что определяет Task Definition в ECS?

A) Конфигурацию контейнеров (image, CPU, memory, ports, etc.)

B) Billing information

C) VPC configuration

D) Количество запущенных контейнеров

---

## Question 5: awsvpc Network Mode





Что происходит при использовании awsvpc network mode?

A) Каждая task получает свой ENI и private IP

B) Networking отключён

C) Все tasks делят один IP

D) Tasks общаются только через public IP

---

## Question 6: Service




Что делает ECS Service?

A) Поддерживает desired count tasks, интегрирует с LB

B) Billing

C) Создаёт clusters

D) Мониторинг

---

## Question 7: IAM Roles




Какие IAM роли используются в ECS?

A) Только instance role

B) Task Execution Role (pull images) + Task Role (app permissions)

C) Только task role

D) Не использует IAM

---

## Question 8: Auto Scaling




Какие типы auto scaling для ECS Service?

A) Только target tracking

B) Target tracking, step scaling, scheduled scaling

C) Только manual

D) Нет auto scaling

---

## Question 9: ECR




Что такое Amazon ECR?

A) EC2 Container Runtime

B) Managed Docker registry для container images

C) Elastic Compute Resource

D) Container orchestrator

---

## Question 10: EKS Node Groups




Какие типы node groups в EKS?

A) Только managed

B) Только Fargate

C) Managed, Self-managed, Fargate

D) Только EC2

---

## Question 11: App Runner




Для чего используется AWS App Runner?

A) Только для Lambda

B) Fully managed service для containerized web apps

C) Только для batch jobs

D) Только для EKS

---

## Question 12: Spot Instances




Можно ли использовать Spot Instances с ECS?

A) Нет

B) Да, для cost savings (до 90%)

C) Только с Fargate

D) Только для dev

---

## Question 13: Service Discovery




Как работает service discovery в ECS?

A) Только через LB

B) Cloud Map интеграция (DNS/API)

C) Только manual

D) Не поддерживается

---

## Question 14: Capacity Providers




Что делают Capacity Providers?

A) Только billing

B) Управляют capacity для tasks (Fargate/EC2/Spot)

C) Только monitoring

D) Только logging

---

## Question 15: Blue/Green




Как реализовать Blue/Green deployment в ECS?

A) Невозможно

B) CodeDeploy + Application Load Balancer

C) Только rolling

D) Только manual

---

## Question 16: Secrets




Как передать secrets в ECS tasks?

A) В environment variables plaintext

B) Secrets Manager или Parameter Store references

C) В task definition plaintext

D) В S3

---

## Question 17: Logging




Как настроить logging для ECS?

A) Только в файлы

B) Невозможно

C) Только в S3

D) awslogs driver → CloudWatch Logs

---

## Question 18: Health Checks




Какие health checks в ECS?

A) Только container health check

B) Container health check + LB target health check

C) Только LB

D) Нет health checks

---

## Question 19: Proton




Что такое AWS Proton?

A) Monitoring service

B) Container runtime

C) Database service

D) Platform for infrastructure templates and CI/CD

---

## Question 20: Copilot




Что делает AWS Copilot CLI?

A) Упрощает deployment containerized apps на ECS/App Runner

B) AI assistant

C) Security scanner

D) Monitoring tool

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | EKS — managed Kubernetes (CNCF стандарт). ECS — собственный AWS orchestrator с simpler API. |
| 2 | A | Fargate — serverless compute для ECS и EKS. AWS управляет EC2 instances за вас. |
| 3 | B | ECS control plane бесплатен. EKS control plane стоит $0.10/hour (~$73/month). |
| 4 | A | Task Definition — blueprint для контейнеров: image, CPU, memory, ports, env vars, IAM role, logs. |
| 5 | A | awsvpc даёт каждой task отдельный ENI с private IP в VPC subnet и собственные Security Groups. |
| 6 | A | Service поддерживает desired count, интегрирует с LB |
| 7 | B | Task Execution Role + Task Role |
| 8 | B | Target tracking, step, scheduled scaling |
| 9 | B | ECR — managed Docker registry |
| 10 | C | Managed, Self-managed, Fargate node groups |
| 11 | B | App Runner — fully managed containerized apps |
| 12 | B | Spot Instances с ECS для cost savings |
| 13 | B | Cloud Map для service discovery |
| 14 | B | Capacity Providers управляют capacity |
| 15 | B | CodeDeploy + ALB для Blue/Green |
| 16 | B | Secrets Manager или Parameter Store |
| 17 | D | awslogs driver → CloudWatch Logs |
| 18 | B | Container + LB health checks |
| 19 | D | Proton — infrastructure templates platform |
| 20 | A | Copilot — упрощает deployment на ECS |

---
