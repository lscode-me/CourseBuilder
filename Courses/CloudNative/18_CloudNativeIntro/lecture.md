# Введение в Cloud Native

---

## 📋 Prerequisites

- Понимание облачных сервисов
- Опыт разработки приложений
- Базовые знания контейнеров

---

## 🎯 Learning Objectives

- Понимать философию Cloud Native
- Знать основные принципы и паттерны
- Различать Cloud Native от традиционной разработки
- Ориентироваться в CNCF landscape

---

## 1. Что такое Cloud Native

### 1.1 Определение CNCF

> **Cloud native technologies** empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach.
>
> — Cloud Native Computing Foundation

```python

cloud_native_pillars = {
    "Containers": "Упаковка приложений с dependencies",
    "Microservices": "Декомпозиция на независимые сервисы",
    "DevOps": "Культура и практики автоматизации",
    "CI/CD": "Непрерывная интеграция и доставка",
    "Orchestration": "Kubernetes для управления контейнерами",
    "Observability": "Логи, метрики, трейсы",
    "Service Mesh": "Сетевое взаимодействие между сервисами"
}

print("Cloud Native Pillars:")
for pillar, description in cloud_native_pillars.items():
    print(f"  • {pillar}: {description}")

```

### 1.2 Cloud Native vs Traditional

```

┌────────────────────────────────────────────────────────────────────┐
│           Traditional vs Cloud Native                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  TRADITIONAL                    CLOUD NATIVE                       │
│  ───────────                    ────────────                       │
│  Monolithic                     Microservices                      │
│  Physical/VMs                   Containers                         │
│  Manual deployment              CI/CD automation                   │
│  Vertical scaling               Horizontal scaling                 │
│  Stateful                       Stateless (12-factor)              │
│  Long release cycles            Continuous delivery                │
│  Ops managed infra              DevOps/Platform teams              │
│  Pets (named servers)           Cattle (disposable)                │
│  Waterfall/ITIL                 Agile/DevOps                       │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 2. CNCF и Cloud Native Landscape

### 2.1 Cloud Native Computing Foundation

CNCF — часть Linux Foundation, управляет ключевыми open-source проектами:

```python

cncf_graduated_projects = {
    "Kubernetes": "Container orchestration",
    "Prometheus": "Monitoring & alerting",
    "Envoy": "Service proxy",
    "CoreDNS": "DNS server",
    "containerd": "Container runtime",
    "Fluentd": "Log collector",
    "Jaeger": "Distributed tracing",
    "Helm": "Kubernetes package manager",
    "etcd": "Distributed key-value store",
    "Open Policy Agent": "Policy engine",
    "Argo": "GitOps for Kubernetes"
}

print("CNCF Graduated Projects (production-ready):")
for project, description in list(cncf_graduated_projects.items())[:6]:
    print(f"  ✓ {project}: {description}")

```

### 2.2 CNCF Trail Map

```

┌────────────────────────────────────────────────────────────────────┐
│                    CNCF Trail Map                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  1. CONTAINERIZATION                                               │
│     └── Docker, containerd, buildah                                │
│                                                                    │
│  2. CI/CD                                                          │
│     └── Jenkins, GitLab CI, GitHub Actions, Argo CD                │
│                                                                    │
│  3. ORCHESTRATION                                                  │
│     └── Kubernetes (EKS, GKE, AKS)                                 │
│                                                                    │
│  4. OBSERVABILITY                                                  │
│     └── Prometheus, Grafana, Jaeger, ELK                           │
│                                                                    │
│  5. SERVICE MESH                                                   │
│     └── Istio, Linkerd, AWS App Mesh                               │
│                                                                    │
│  6. NETWORKING & POLICY                                            │
│     └── Calico, Cilium, OPA                                        │
│                                                                    │
│  7. DISTRIBUTED DATABASE & STORAGE                                 │
│     └── Vitess, TiKV, Rook                                         │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 3. Cloud Native Principles

### 3.1 Design Principles

```python

cloud_native_principles = {
    "Design for failure": {
        "description": "Assume everything fails",
        "practices": ["Circuit breakers", "Retries", "Timeouts", "Bulkheads"]
    },
    "Design for scale": {
        "description": "Horizontal scaling by default",
        "practices": ["Stateless services", "Auto-scaling", "Load balancing"]
    },
    "Design for automation": {
        "description": "Everything as code",
        "practices": ["IaC", "CI/CD", "GitOps", "Policy as code"]
    },
    "Design for observability": {
        "description": "Know what's happening",
        "practices": ["Structured logging", "Metrics", "Distributed tracing"]
    },
    "Design for security": {
        "description": "Security at every layer",
        "practices": ["Zero trust", "Secrets management", "mTLS"]
    }
}

for principle, details in cloud_native_principles.items():
    print(f"\n{principle.upper()}")
    print(f"  {details['description']}")
    print(f"  Practices: {', '.join(details['practices'][:3])}")

```

### 3.2 Pets vs Cattle

```

┌────────────────────────────────────────────────────────────────────┐
│                    Pets vs Cattle                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  PETS (Traditional)              CATTLE (Cloud Native)             │
│  ─────────────────               ─────────────────────             │
│  • Unique names                  • Numbered/random IDs             │
│  • Manually configured           • Automated provisioning          │
│  • Carefully maintained          • Easily replaceable              │
│  • When sick: heal               • When sick: destroy & replace    │
│  • Long-lived                    • Short-lived/ephemeral           │
│  • "We can't lose this server"  • "Just spin up another one"       │
│                                                                    │
│  Example: "prod-db-master"       Example: "pod-abc123-xyz"         │
│                                                                    │
│  "Treat your servers like cattle, not pets."                       │
│                                  — Randy Bias (2011)               │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 4. Cloud Native Architecture Patterns

### 4.1 Microservices

```

┌────────────────────────────────────────────────────────────────────┐
│                    Microservices Architecture                      │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│         ┌──────────────────────────────────────────┐               │
│         │           API Gateway                     │              │
│         └─────────────────┬────────────────────────┘               │
│                           │                                        │
│     ┌─────────────────────┼─────────────────────┐                  │
│     │                     │                     │                  │
│     ▼                     ▼                     ▼                  │
│  ┌──────┐            ┌──────┐            ┌──────┐                  │
│  │User  │            │Order │            │Product│                 │
│  │Svc   │            │Svc   │            │Svc   │                  │
│  └──┬───┘            └──┬───┘            └──┬───┘                  │
│     │                   │                   │                      │
│     ▼                   ▼                   ▼                      │
│  ┌──────┐            ┌──────┐            ┌──────┐                  │
│  │UserDB│            │OrderDB│           │ProductDB│               │
│  └──────┘            └──────┘            └──────┘                  │
│                                                                    │
│  Каждый сервис:                                                    │
│  • Независимо деплоится                                            │
│  • Имеет свою базу данных                                          │
│  • Общается через API (REST/gRPC)                                  │
│  • Может использовать разные технологии                            │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

### 4.2 Event-Driven Architecture

```python

event_driven_patterns = {
    "Event Sourcing": {
        "description": "Store events, not state",
        "aws_services": ["EventBridge", "Kinesis", "DynamoDB Streams"]
    },
    "CQRS": {
        "description": "Separate read and write models",
        "aws_services": ["Lambda", "DynamoDB", "ElastiCache"]
    },
    "Saga Pattern": {
        "description": "Distributed transactions via events",
        "aws_services": ["Step Functions", "SQS", "Lambda"]
    },
    "Pub/Sub": {
        "description": "Loose coupling via message broker",
        "aws_services": ["SNS", "EventBridge", "MSK"]
    }
}

```

---

## 5. Cloud Native on AWS

### 5.1 AWS Services для Cloud Native

```python

aws_cloud_native_stack = {
    "Containers": {
        "runtime": "ECS, EKS, Fargate",
        "registry": "ECR"
    },
    "Serverless": {
        "compute": "Lambda, App Runner",
        "api": "API Gateway",
        "integration": "Step Functions, EventBridge"
    },
    "Data": {
        "sql": "Aurora Serverless, RDS",
        "nosql": "DynamoDB",
        "cache": "ElastiCache, DAX"
    },
    "Messaging": {
        "queues": "SQS",
        "pubsub": "SNS, EventBridge",
        "streaming": "Kinesis, MSK"
    },
    "Observability": {
        "monitoring": "CloudWatch",
        "tracing": "X-Ray",
        "logs": "CloudWatch Logs"
    },
    "CI/CD": {
        "source": "CodeCommit",
        "build": "CodeBuild",
        "deploy": "CodeDeploy, CodePipeline"
    }
}

```

---

## 6. Когда НЕ нужен Cloud Native

```python

when_not_cloud_native = [
    "Простое CRUD приложение",
    "Маленькая команда (1-3 разработчика)",
    "Прототип/MVP",
    "Монолит отлично работает",
    "Нет экспертизы в Kubernetes",
    "Бюджетные ограничения",
    "Регуляторные требования (legacy)"
]

print("Cloud Native НЕ для всех:")
for reason in when_not_cloud_native:
    print(f"  ⚠️ {reason}")

print("\n'You probably don't need microservices'")
print("  — Martin Fowler (MonolithFirst)")

```

---

## 💡 Key Takeaways

- **Cloud Native** — подход к разработке для облачных сред

- **CNCF** — организация, развивающая cloud native экосистему

- **Ключевые практики**: контейнеры, микросервисы, CI/CD, observability

- **Pets vs Cattle** — относитесь к серверам как к заменяемым ресурсам

- **Не всем нужно**: начинайте с простого, усложняйте по необходимости

---

## 🚀 Next Steps

- [Twelve-Factor App](../19_TwelveFactorApp/)
- [Microservices](../20_Microservices/)

---

## 📚 Additional Resources

- [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md)
- [Cloud Native Landscape](https://landscape.cncf.io/)
- "Cloud Native Patterns" by Cornelia Davis

---



