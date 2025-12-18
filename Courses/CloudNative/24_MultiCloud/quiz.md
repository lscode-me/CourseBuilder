# Cloud Native Development - Quiz
## Multi-Cloud

---

## Question 1: Multi-Cloud Complexity

Какой главный недостаток multi-cloud стратегии?

A) Меньше сервисов доступно

B) Дешевле single cloud

C) Хуже производительность

D) Операционная сложность и требуемые навыки

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

A) DynamoDB

B) S3

C) EC2 (виртуальные машины)

D) RDS PostgreSQL

---

## Question 4: Portable Alternative

Какая portable альтернатива AWS Lambda?

A) EC2

B) Step Functions

C) Fargate

D) Knative на Kubernetes

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

A) Через providers для разных clouds (aws, google, azurerm)

B) Только для Azure

C) Только для AWS

D) Не поддерживает

---

## Question 7: Container Portability

Почему containers portable?

A) Быстрее

B) Легче

C) Дешевле

D) Одинаковый runtime environment везде

---

## Question 8: Anthos

Что такое Google Anthos?

A) Network

B) Database

C) Storage

D) Multi-cloud Kubernetes management platform

---

## Question 9: Azure Arc

Что делает Azure Arc?

A) Управление ресурсами в любом cloud или on-premises через Azure

B) Storage

C) Network service

D) Database

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

A) Только AWS

B) Невозможно

C) Federation через SAML/OIDC, centralized IdP

D) Отдельные accounts везде

---

## Question 13: Observability Tools

Какие multi-cloud observability tools?

A) Только Azure Monitor

B) Datadog, Grafana, Prometheus — cloud-agnostic

C) Только GCP Operations

D) Только CloudWatch

---

## Question 14: GitOps for Multi-Cloud

Почему GitOps хорош для multi-cloud?

A) Только для on-premises

B) Не подходит

C) Только для AWS

D) Git как единый source of truth для всех clouds

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

A) Multi-cloud cost tools (CloudHealth, Spot.io, Kubecost)

B) Только Excel

C) Невозможно

D) Отдельно для каждого cloud

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

A) Только networking

B) Только cost

C) Необходимость экспертизы в нескольких clouds

D) Только security

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Multi-cloud требует экспертизы в нескольких clouds, сложнее networking, security, operations. |
| 2 | C | Kubernetes API стандартизирован. Те же YAML манифесты работают на любом managed K8s сервисе. |
| 3 | A | DynamoDB имеет proprietary data model и API. Миграция требует переписывания приложения. |
| 4 | D | Knative — CNCF проект для serverless на Kubernetes. Работает на любом K8s кластере. |
| 5 | D | Прагматичный подход: использовать managed сервисы когда их ценность превышает риск lock-in. |
| 6 | A | Terraform providers для разных clouds |
| 7 | D | Containers: одинаковый runtime везде |
| 8 | D | Anthos: multi-cloud Kubernetes management |
| 9 | A | Azure Arc: управление anywhere через Azure |
| 10 | A | Open formats: Parquet, Avro, JSON |
| 11 | B | VPN, dedicated connections, third-party |
| 12 | C | Federation через SAML/OIDC |
| 13 | B | Datadog, Grafana, Prometheus |
| 14 | D | GitOps: единый source of truth |
| 15 | D | Kong, Istio Gateway — работают везде |
| 16 | A | Multi-cloud cost tools |
| 17 | B | DR в другом cloud provider |
| 18 | D | Open standards, abstraction, portable formats |
| 19 | C | Crossplane: K8s-native multi-cloud provisioning |
| 20 | C | Экспертиза в нескольких clouds |

---

