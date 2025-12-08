# Cloud Native Development
## Практические примеры архитектур

---

## 📋 Prerequisites

- Завершение предыдущих модулей курса
- Понимание AWS сервисов
- Знание cloud-native принципов

---

## 🎯 Learning Objectives

- Применять знания на практике
- Анализировать архитектурные решения
- Понимать trade-offs разных подходов

---

## 1. Web Application: E-commerce

### 1.1 Архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│              E-commerce Architecture                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Users                                                             │
│    │                                                               │
│    ▼                                                               │
│  ┌─────────────┐                                                   │
│  │ CloudFront  │ ──► S3 (static assets)                           │
│  └──────┬──────┘                                                   │
│         │                                                          │
│         ▼                                                          │
│  ┌─────────────┐                                                   │
│  │ API Gateway │                                                   │
│  │   (REST)    │                                                   │
│  └──────┬──────┘                                                   │
│         │                                                          │
│    ┌────┴────┐                                                    │
│    ▼         ▼                                                    │
│  ┌─────┐  ┌──────────┐                                            │
│  │Cogni│  │  ECS     │                                            │
│  │to   │  │ Fargate  │                                            │
│  └─────┘  └────┬─────┘                                            │
│                │                                                   │
│    ┌───────────┼───────────┐                                      │
│    ▼           ▼           ▼                                      │
│ ┌──────┐  ┌────────┐  ┌─────────┐                                │
│ │Aurora│  │DynamoDB│  │Elasti-  │                                │
│ │(RDS) │  │(cart,  │  │Cache    │                                │
│ │      │  │session)│  │(Redis)  │                                │
│ └──────┘  └────────┘  └─────────┘                                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Background Processing:                                      │  │
│  │  SQS → Lambda (order processing)                            │  │
│  │  EventBridge → Lambda (scheduled tasks)                     │  │
│  │  SNS → multiple subscribers (notifications)                 │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 Компоненты и обоснование

```python
ecommerce_components = {
    "CloudFront + S3": {
        "purpose": "Static assets (React SPA, images)",
        "why": "Global distribution, low latency, cheap"
    },
    "API Gateway + Cognito": {
        "purpose": "API management, authentication",
        "why": "Managed auth, rate limiting, JWT"
    },
    "ECS Fargate": {
        "purpose": "Application containers",
        "why": "Serverless containers, auto-scaling"
    },
    "Aurora": {
        "purpose": "Products, orders, users",
        "why": "ACID transactions, SQL, Aurora Serverless for dev"
    },
    "DynamoDB": {
        "purpose": "Shopping cart, sessions",
        "why": "Low latency, auto-scaling, TTL for sessions"
    },
    "ElastiCache": {
        "purpose": "Caching, rate limiting",
        "why": "Sub-millisecond latency, session store"
    },
    "SQS + Lambda": {
        "purpose": "Order processing, emails",
        "why": "Decoupling, retry logic, scale to zero"
    }
}

print("E-commerce Components:\n")
for component, details in ecommerce_components.items():
    print(f"{component}:")
    print(f"  Purpose: {details['purpose']}")
    print(f"  Why: {details['why']}\n")
```

### 1.3 Cost Estimate (medium traffic)

```python
# Monthly cost estimate for ~100K DAU
ecommerce_costs = {
    "CloudFront": "$50 (1TB data transfer)",
    "API Gateway": "$35 (10M requests)",
    "Cognito": "$55 (10K MAU)",
    "ECS Fargate": "$150 (2 tasks, 0.5 vCPU, 1GB)",
    "Aurora Serverless": "$200 (avg 2 ACU)",
    "DynamoDB": "$50 (On-Demand, ~1M requests/day)",
    "ElastiCache": "$25 (cache.t3.micro)",
    "Lambda": "$5 (1M invocations)",
    "SQS/SNS": "$5",
    "S3": "$10",
    "Total": "~$585/month"
}

print("Monthly Cost Estimate:")
for item, cost in ecommerce_costs.items():
    print(f"  {item}: {cost}")
```

---

## 2. Real-time Analytics Platform

### 2.1 Архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│              Real-time Analytics                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Data Sources                                                      │
│  (Web, Mobile, IoT)                                               │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │   Kinesis    │                                                  │
│  │ Data Streams │                                                  │
│  └──────┬───────┘                                                  │
│         │                                                          │
│    ┌────┴──────────────────────┐                                  │
│    │                           │                                  │
│    ▼                           ▼                                  │
│  ┌──────────────┐      ┌──────────────┐                          │
│  │   Kinesis    │      │    Lambda    │                          │
│  │   Firehose   │      │ (real-time   │                          │
│  │              │      │  processing) │                          │
│  └──────┬───────┘      └──────┬───────┘                          │
│         │                     │                                   │
│         ▼                     ▼                                   │
│  ┌──────────────┐      ┌──────────────┐                          │
│  │      S3      │      │   DynamoDB   │                          │
│  │  (data lake) │      │  (real-time  │                          │
│  │              │      │   counters)  │                          │
│  └──────┬───────┘      └──────────────┘                          │
│         │                                                         │
│    ┌────┴────┐                                                    │
│    ▼         ▼                                                    │
│ ┌──────┐  ┌──────────┐                                           │
│ │Athena│  │ Redshift │                                           │
│ │(SQL) │  │Serverless│                                           │
│ └──────┘  └──────────┘                                           │
│                                                                     │
│  Visualization: QuickSight, Grafana                               │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 2.2 Data Flow

```python
analytics_flow = {
    "Ingestion": {
        "service": "Kinesis Data Streams",
        "throughput": "1000s events/sec per shard",
        "latency": "Sub-second"
    },
    "Real-time": {
        "service": "Lambda + DynamoDB",
        "use_case": "Live dashboards, counters",
        "latency": "< 1 second"
    },
    "Near real-time": {
        "service": "Kinesis Firehose → S3",
        "use_case": "Data lake, batch analytics",
        "latency": "60 seconds buffer"
    },
    "Batch analytics": {
        "service": "Athena / Redshift",
        "use_case": "Complex queries, reports",
        "latency": "Seconds to minutes"
    }
}
```

---

## 3. Serverless API Backend

### 3.1 Архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│              Serverless API                                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Mobile/Web Client                                                 │
│         │                                                          │
│         ▼                                                          │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                    API Gateway (HTTP API)                     │ │
│  │  • JWT authorizer (Cognito)                                  │ │
│  │  • Rate limiting                                             │ │
│  │  • Request validation                                        │ │
│  └──────────────────────────┬───────────────────────────────────┘ │
│                             │                                      │
│         ┌───────────────────┼───────────────────┐                 │
│         ▼                   ▼                   ▼                 │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐            │
│  │  Lambda    │     │  Lambda    │     │  Lambda    │            │
│  │  Users     │     │  Posts     │     │  Comments  │            │
│  └─────┬──────┘     └─────┬──────┘     └─────┬──────┘            │
│        │                  │                  │                    │
│        └──────────────────┼──────────────────┘                    │
│                           ▼                                        │
│                    ┌────────────┐                                  │
│                    │ DynamoDB   │                                  │
│                    │ (single    │                                  │
│                    │  table)    │                                  │
│                    └────────────┘                                  │
│                                                                     │
│  Async workflows:                                                  │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐            │
│  │ DynamoDB   │────►│  Lambda    │────►│    SES     │            │
│  │ Streams    │     │ (trigger)  │     │  (email)   │            │
│  └────────────┘     └────────────┘     └────────────┘            │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Преимущества Serverless

```python
serverless_benefits = {
    "Cost": "Pay only for invocations, scale to zero",
    "Scaling": "Automatic, from 0 to 1000s concurrent",
    "Operations": "No servers to manage, patch, scale",
    "Speed": "Fast deployment, iterate quickly"
}

serverless_challenges = {
    "Cold starts": "Initial latency (~100-500ms)",
    "Complexity": "Many functions to manage",
    "Debugging": "Distributed tracing needed",
    "Limits": "15 min execution, 10GB memory"
}

print("Serverless Benefits:")
for benefit, description in serverless_benefits.items():
    print(f"  ✅ {benefit}: {description}")

print("\nServerless Challenges:")
for challenge, description in serverless_challenges.items():
    print(f"  ⚠️ {challenge}: {description}")
```

---

## 4. Microservices Platform

### 4.1 Архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│              Microservices on EKS                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                         ALB                                   │ │
│  └────────────────────────────┬─────────────────────────────────┘ │
│                               │                                    │
│  ┌────────────────────────────┴─────────────────────────────────┐ │
│  │                    EKS Cluster                                │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                    Istio Service Mesh                    │ │ │
│  │  │  • mTLS between services                                │ │ │
│  │  │  • Traffic management                                   │ │ │
│  │  │  • Observability                                        │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │ │
│  │  │ User Svc │  │Order Svc │  │ Payment  │  │ Notific. │    │ │
│  │  │          │  │          │  │   Svc    │  │   Svc    │    │ │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │ │
│  │       │             │             │             │           │ │
│  └───────┼─────────────┼─────────────┼─────────────┼───────────┘ │
│          │             │             │             │              │
│          ▼             ▼             ▼             ▼              │
│     ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐        │
│     │RDS     │    │DynamoDB│    │External│    │   SNS  │        │
│     │Postgres│    │        │    │Payment │    │        │        │
│     └────────┘    └────────┘    │  API   │    └────────┘        │
│                                 └────────┘                       │
│                                                                     │
│  Observability:                                                    │
│  • Prometheus + Grafana (metrics)                                 │
│  • X-Ray / Jaeger (traces)                                        │
│  • CloudWatch Logs (logs)                                         │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 5. Выбор архитектуры

```python
architecture_decision_matrix = {
    "Simple web app, MVP": {
        "recommendation": "Serverless (Lambda + API Gateway + DynamoDB)",
        "why": "Fast to build, cheap at low scale, no ops"
    },
    "Complex web app, steady traffic": {
        "recommendation": "Containers (ECS/EKS + RDS)",
        "why": "More control, predictable cost, familiar model"
    },
    "High-scale API": {
        "recommendation": "EKS with auto-scaling",
        "why": "Fine-grained scaling, service mesh, portability"
    },
    "Data pipeline": {
        "recommendation": "Kinesis + Lambda + S3 + Athena",
        "why": "Serverless, scales automatically, pay per use"
    },
    "Real-time processing": {
        "recommendation": "Kinesis + Lambda or ECS",
        "why": "Sub-second latency, event-driven"
    }
}

print("Architecture Decision Guide:\n")
for use_case, details in architecture_decision_matrix.items():
    print(f"{use_case}:")
    print(f"  → {details['recommendation']}")
    print(f"  Why: {details['why']}\n")
```

---

## 💡 Key Takeaways

- **Start simple** — serverless для MVP, усложняйте по мере необходимости
- **Choose the right database** — SQL для транзакций, NoSQL для масштаба
- **Event-driven** — decouple с помощью SQS/SNS/EventBridge
- **Observability first** — logs, metrics, traces с самого начала
- **Security by design** — IAM, encryption, VPC с первого дня
- **Cost awareness** — right-size, use Reserved/Spot, monitor spend

---

## 📚 Next Steps

- Практика на AWS Free Tier
- AWS Well-Architected Framework
- AWS Solutions Library
- Hands-on workshops (workshops.aws)

---
