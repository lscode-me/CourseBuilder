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

A) Container registry

B) CI/CD сервис

C) Serverless compute для контейнеров

D) Kubernetes distribution

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

A) Billing information

B) Конфигурацию контейнеров (image, CPU, memory, ports, etc.)

C) Количество запущенных контейнеров

D) VPC configuration

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

A) Мониторинг

B) Создаёт clusters

C) Billing

D) Поддерживает desired count tasks, интегрирует с LB

---

## Question 7: IAM Roles






Какие IAM роли используются в ECS?

A) Только instance role

B) Не использует IAM

C) Task Execution Role (pull images) + Task Role (app permissions)

D) Только task role

---

## Question 8: Auto Scaling






Какие типы auto scaling для ECS Service?

A) Target tracking, step scaling, scheduled scaling

B) Только manual

C) Только target tracking

D) Нет auto scaling

---

## Question 9: ECR






Что такое Amazon ECR?

A) Managed Docker registry для container images

B) Elastic Compute Resource

C) EC2 Container Runtime

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

B) Только с Fargate

C) Только для dev

D) Да, для cost savings (до 90%)

---

## Question 13: Service Discovery






Как работает service discovery в ECS?

A) Только через LB

B) Не поддерживается

C) Cloud Map интеграция (DNS/API)

D) Только manual

---

## Question 14: Capacity Providers






Что делают Capacity Providers?

A) Только logging

B) Управляют capacity для tasks (Fargate/EC2/Spot)

C) Только billing

D) Только monitoring

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

A) В task definition plaintext

B) Secrets Manager или Parameter Store references

C) В S3

D) В environment variables plaintext

---

## Question 17: Logging






Как настроить logging для ECS?

A) awslogs driver → CloudWatch Logs

B) Только в S3

C) Невозможно

D) Только в файлы

---

## Question 18: Health Checks






Какие health checks в ECS?

A) Container health check + LB target health check

B) Только LB

C) Только container health check

D) Нет health checks

---

## Question 19: Proton






Что такое AWS Proton?

A) Platform for infrastructure templates and CI/CD

B) Database service

C) Container runtime

D) Monitoring service

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
| 2 | C | Fargate — serverless compute для ECS и EKS. AWS управляет EC2 instances за вас. |
| 3 | B | ECS control plane бесплатен. EKS control plane стоит $0.10/hour (~$73/month). |
| 4 | B | Task Definition — blueprint для контейнеров: image, CPU, memory, ports, env vars, IAM role, logs. |
| 5 | A | awsvpc даёт каждой task отдельный ENI с private IP в VPC subnet и собственные Security Groups. |
| 6 | D | Service поддерживает desired count, интегрирует с LB |
| 7 | C | Task Execution Role + Task Role |
| 8 | A | Target tracking, step, scheduled scaling |
| 9 | A | ECR — managed Docker registry |
| 10 | C | Managed, Self-managed, Fargate node groups |
| 11 | B | App Runner — fully managed containerized apps |
| 12 | D | Spot Instances с ECS для cost savings |
| 13 | C | Cloud Map для service discovery |
| 14 | B | Capacity Providers управляют capacity |
| 15 | B | CodeDeploy + ALB для Blue/Green |
| 16 | B | Secrets Manager или Parameter Store |
| 17 | A | awslogs driver → CloudWatch Logs |
| 18 | A | Container + LB health checks |
| 19 | A | Proton — infrastructure templates platform |
| 20 | A | Copilot — упрощает deployment на ECS |

---
