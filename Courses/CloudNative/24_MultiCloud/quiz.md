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

A) Knative на Kubernetes

B) Fargate

C) Step Functions

D) EC2

---

## Question 5: Pragmatic Approach





Какой прагматичный подход к multi-cloud?

A) Всегда дублировать в двух clouds

B) Использовать только open source

C) Никогда не использовать managed services

D) Использовать proprietary сервисы когда value > lock-in risk

---

## Question 6: Terraform Providers




Как Terraform поддерживает multi-cloud?

A) Не поддерживает

B) Через providers для разных clouds (aws, google, azurerm)

C) Только для AWS

D) Только для Azure

---

## Question 7: Container Portability




Почему containers portable?

A) Одинаковый runtime environment везде

B) Дешевле

C) Легче

D) Быстрее

---

## Question 8: Anthos




Что такое Google Anthos?

A) Database

B) Multi-cloud Kubernetes management platform

C) Storage

D) Network

---

## Question 9: Azure Arc




Что делает Azure Arc?

A) Database

B) Network service

C) Storage

D) Управление ресурсами в любом cloud или on-premises через Azure

---

## Question 10: Data Portability




Какой формат данных наиболее portable?

A) Open formats (Parquet, Avro, JSON)

B) DynamoDB format

C) Binary

D) Proprietary formats

---

## Question 11: Cross-Cloud Networking




Как соединить clouds?

A) Только VPN

B) VPN, dedicated connections, third-party solutions

C) Невозможно

D) Только internet

---

## Question 12: Identity Federation




Как управлять identity across clouds?

A) Невозможно

B) Только AWS

C) Отдельные accounts везде

D) Federation через SAML/OIDC, centralized IdP

---

## Question 13: Observability Tools




Какие multi-cloud observability tools?

A) Только CloudWatch

B) Datadog, Grafana, Prometheus — cloud-agnostic

C) Только Azure Monitor

D) Только GCP Operations

---

## Question 14: GitOps for Multi-Cloud




Почему GitOps хорош для multi-cloud?

A) Не подходит

B) Git как единый source of truth для всех clouds

C) Только для AWS

D) Только для on-premises

---

## Question 15: API Gateway Portability




Какой API Gateway наиболее portable?

A) Azure API Management

B) GCP Apigee

C) AWS API Gateway

D) Kong, Istio Gateway — работают везде

---

## Question 16: Cost Management




Как управлять costs across clouds?

A) Невозможно

B) Отдельно для каждого cloud

C) Multi-cloud cost tools (CloudHealth, Spot.io, Kubecost)

D) Только Excel

---

## Question 17: Disaster Recovery




Как multi-cloud помогает с DR?

A) Дороже без benefit

B) DR в другом cloud provider для resilience

C) Увеличивает risk

D) Не помогает

---

## Question 18: Vendor Lock-in Mitigation




Как снизить vendor lock-in?

A) Невозможно

B) Не использовать cloud

C) Использовать один cloud

D) Open standards, abstraction layers, portable formats

---

## Question 19: Crossplane




Что такое Crossplane?

A) Security tool

B) Network tool

C) Kubernetes-native multi-cloud resource provisioning

D) Database

---

## Question 20: Skills Challenge




Какой challenge для multi-cloud teams?

A) Необходимость экспертизы в нескольких clouds

B) Только security

C) Только networking

D) Только cost

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Multi-cloud требует экспертизы в нескольких clouds, сложнее networking, security, operations. |
| 2 | C | Kubernetes API стандартизирован. Те же YAML манифесты работают на любом managed K8s сервисе. |
| 3 | B | DynamoDB имеет proprietary data model и API. Миграция требует переписывания приложения. |
| 4 | A | Knative — CNCF проект для serverless на Kubernetes. Работает на любом K8s кластере. |
| 5 | D | Прагматичный подход: использовать managed сервисы когда их ценность превышает риск lock-in. |
| 6 | B | Terraform providers для разных clouds |
| 7 | A | Containers: одинаковый runtime везде |
| 8 | B | Anthos: multi-cloud Kubernetes management |
| 9 | D | Azure Arc: управление anywhere через Azure |
| 10 | A | Open formats: Parquet, Avro, JSON |
| 11 | B | VPN, dedicated connections, third-party |
| 12 | D | Federation через SAML/OIDC |
| 13 | B | Datadog, Grafana, Prometheus |
| 14 | B | GitOps: единый source of truth |
| 15 | D | Kong, Istio Gateway — работают везде |
| 16 | C | Multi-cloud cost tools |
| 17 | B | DR в другом cloud provider |
| 18 | D | Open standards, abstraction, portable formats |
| 19 | C | Crossplane: K8s-native multi-cloud provisioning |
| 20 | A | Экспертиза в нескольких clouds |

---
