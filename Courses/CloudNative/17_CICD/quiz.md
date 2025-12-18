# Cloud Native Development - Quiz
## CI/CD

---

## Question 1: CI vs CD

Что означает CI (Continuous Integration)?

A) Контейнеризация приложений

B) Автоматический build и тестирование при каждом commit

C) Infrastructure as Code

D) Автоматический deploy в production

---

## Question 2: Blue/Green Deployment

Какое преимущество Blue/Green deployment?

A) Instant rollback к предыдущей версии

B) Не требует load balancer

C) Самая быстрая стратегия

D) Меньше ресурсов

---

## Question 3: Canary Deployment

Что такое Canary deployment?

A) Постепенный shift трафика с мониторингом

B) Полная замена всех instances сразу

C) A/B тестирование UI

D) Deployment в разные regions

---

## Question 4: CodeBuild

Где определяются build steps в CodeBuild?

A) В консоли AWS

B) В CodePipeline

C) В buildspec.yml файле в репозитории

D) В CloudFormation

---

## Question 5: Pipeline Stages

Какой правильный порядок stages в типичном pipeline?

A) Test → Build → Deploy → Source

B) Build → Source → Deploy → Test

C) Deploy → Build → Test → Source

D) Source → Build → Test → Deploy

---

## Question 6: Artifacts

Куда CodeBuild сохраняет artifacts?

A) EC2

B) S3

C) DynamoDB

D) EFS

---

## Question 7: CodeDeploy

Какие compute platforms поддерживает CodeDeploy?

A) Только Lambda

B) Только ECS

C) EC2, Lambda, ECS

D) Только EC2

---

## Question 8: AppSpec

Для чего используется appspec.yml?

A) Для build

B) Для monitoring

C) Для определения deployment actions и lifecycle hooks

D) Для testing

---

## Question 9: GitHub Actions vs CodePipeline

Какое преимущество GitHub Actions?

A) Дешевле

B) Managed AWS сервис

C) Ближе к коду, marketplace actions, matrix builds

D) Только AWS

---

## Question 10: Rollback

Как работает automatic rollback в CodeDeploy?

A) Только для Lambda

B) На основе CloudWatch alarms или deployment failures

C) Невозможен

D) Всегда manual

---

## Question 11: Multi-Account

Как deploy в multiple accounts?

A) Только через консоль

B) Только вручную

C) Невозможно

D) Cross-account roles, CodePipeline с multiple actions

---

## Question 12: Secrets in Pipeline

Как хранить secrets в CI/CD?

A) В buildspec.yml

B) В git

C) Secrets Manager или Parameter Store references

D) В environment variables plaintext

---

## Question 13: Testing in Pipeline

Какие типы тестов включать в pipeline?

A) Никаких

B) Только manual

C) Только unit

D) Unit, integration, security, performance (по времени/важности)

---

## Question 14: Feature Flags

Для чего используются feature flags?

A) Для logging

B) Для security

C) Для billing

D) Для включения/выключения features без redeploy

---

## Question 15: Trunk-Based Development

Что такое trunk-based development?

A) Все работают с main/trunk, короткие feature branches

B) Git flow

C) Только release branches

D) Много долгоживущих веток

---

## Question 16: GitOps

Что такое GitOps?

A) Git security

B) Инфраструктура и deployments управляются через Git (source of truth)

C) Git hosting

D) Git backup

---

## Question 17: ArgoCD

Для чего используется ArgoCD?

A) Для builds

B) GitOps controller для Kubernetes deployments

C) Для testing

D) Для monitoring

---

## Question 18: Promotion

Как продвигать артефакты между environments?

A) Rebuild для каждого env

B) Один artifact, разные configs per environment

C) Нет стандарта

D) Manual copy

---

## Question 19: Pipeline as Code

Почему Pipeline as Code важен?

A) Быстрее

B) Для красоты

C) Дешевле

D) Версионирование, review, воспроизводимость

---

## Question 20: Zero Downtime

Как обеспечить zero downtime deployment?

A) Невозможно

B) Только maintenance window

C) Blue/Green, Rolling, Canary strategies

D) Только для статики

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CI = автоматический build и test при каждом commit. CD = автоматический deploy. |
| 2 | A | Blue/Green позволяет мгновенно переключить трафик обратно на старую версию при проблемах. |
| 3 | A | Canary: постепенно увеличивающийся % трафика на новую версию с мониторингом между шагами. |
| 4 | C | buildspec.yml в корне репозитория определяет phases, commands, artifacts. |
| 5 | D | Стандартный порядок: Source (код) → Build (компиляция) → Test (проверка) → Deploy (развёртывание). |
| 6 | B | CodeBuild сохраняет artifacts в S3 |
| 7 | C | CodeDeploy: EC2, Lambda, ECS |
| 8 | C | appspec.yml для deployment actions |
| 9 | C | GitHub Actions: marketplace, matrix builds |
| 10 | B | Rollback на основе alarms или failures |
| 11 | D | Cross-account roles, multiple actions |
| 12 | C | Secrets Manager или Parameter Store |
| 13 | D | Unit, integration, security, performance |
| 14 | D | Feature flags включают/выключают features |
| 15 | A | Trunk-based: main branch, короткие feature branches |
| 16 | B | GitOps: Git как source of truth |
| 17 | B | ArgoCD: GitOps для Kubernetes |
| 18 | B | Один artifact, разные configs |
| 19 | D | Pipeline as Code: версионирование, review |
| 20 | C | Blue/Green, Rolling, Canary |

---

