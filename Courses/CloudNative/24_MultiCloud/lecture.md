# Multi-Cloud и Cloud Agnostic

---

## 📋 Prerequisites

- Опыт работы с AWS
- Понимание cloud-native архитектуры
- Знакомство с IaC

---

## 🎯 Learning Objectives

- Понимать multi-cloud стратегии
- Применять cloud-agnostic подходы
- Использовать абстракции и стандарты
- Избегать vendor lock-in

---

## 1. Multi-Cloud Strategies

### 1.1 Почему Multi-Cloud

```

┌────────────────────────────────────────────────────────────────────┐
│              Multi-Cloud Motivations                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  REASONS FOR                         REASONS AGAINST               │
│  ───────────                         ───────────────               │
│  • Avoid vendor lock-in             • Operational complexity       │
│  • Best-of-breed services           • Highest common denominator   │
│  • Regulatory compliance            • Networking complexity        │
│  • Geographic coverage              • Increased costs              │
│  • Negotiation leverage             • Security surface area        │
│  • Disaster recovery                • Skill requirements           │
│  • M&A (inherited clouds)           • Data egress costs            │
│                                                                     │
│  Reality: Most "multi-cloud" is:                                   │
│  • Primary cloud + secondary for specific use cases               │
│  • DR in different cloud                                          │
│  • SaaS services on various clouds                                │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 1.2 Multi-Cloud Patterns

```python

multicloud_patterns = {
    "Arbitrage": {
        "description": "Use cheapest cloud for each workload",
        "complexity": "Very High",
        "example": "Spot in AWS, Preemptible in GCP"
    },
    "Best of Breed": {
        "description": "Best service from each cloud",
        "complexity": "High",
        "example": "AWS for compute, GCP for ML, Azure for Office 365"
    },
    "Segmentation": {
        "description": "Different clouds for different business units",
        "complexity": "Medium",
        "example": "Acquired company stays on GCP"
    },
    "DR/Backup": {
        "description": "Primary cloud + secondary for disaster recovery",
        "complexity": "Medium",
        "example": "AWS primary, Azure cold standby"
    },
    "Regulatory": {
        "description": "Specific cloud for compliance requirements",
        "complexity": "Low",
        "example": "Azure Government for FedRAMP"
    }
}

for pattern, details in multicloud_patterns.items():
    print(f"\n{pattern}:")
    print(f"  {details['description']}")
    print(f"  Complexity: {details['complexity']}")

```

---

## 2. Cloud Agnostic Approaches

### 2.1 Abstraction Layers

```

┌────────────────────────────────────────────────────────────────────┐
│              Cloud Agnostic Stack                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  APPLICATION LAYER                                                 │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Cloud-native app (stateless, 12-factor)                     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                            │                                       │
│  ABSTRACTION LAYER         ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Kubernetes (EKS / GKE / AKS)                                │ │
│  │  Terraform (multi-cloud IaC)                                 │ │
│  │  Cloud-agnostic databases (PostgreSQL, MongoDB)              │ │
│  │  Standard protocols (S3 API, OpenTelemetry)                  │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                            │                                       │
│  CLOUD LAYER               ▼                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │     AWS     │  │     GCP     │  │    Azure    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 2.2 Kubernetes как абстракция

```python
# Kubernetes — де-факто стандарт для cloud-agnostic compute

k8s_portability = {
    "AWS": "EKS (Elastic Kubernetes Service)",
    "GCP": "GKE (Google Kubernetes Engine)",
    "Azure": "AKS (Azure Kubernetes Service)",
    "On-prem": "OpenShift, Rancher, k3s"
}

# То же YAML работает везде
# Но! Cloud-specific интеграции (LoadBalancer, PV) различаются

# Portable:
# - Deployments, Services, ConfigMaps
# - Helm charts
# - Operators

# Cloud-specific:
# - LoadBalancer annotations
# - Storage classes
# - IAM integration (IRSA vs Workload Identity)
```

### 2.3 Terraform для Multi-Cloud

```hcl
# Terraform поддерживает все major clouds

# AWS provider
provider "aws" {
  region = "us-east-1"
}

# GCP provider
provider "google" {
  project = "my-project"
  region  = "us-central1"
}

# Azure provider
provider "azurerm" {
  features {}
}

# Можно создавать ресурсы в разных clouds одним apply
resource "aws_instance" "web" {
  ami           = "ami-xxx"
  instance_type = "t3.micro"
}

resource "google_compute_instance" "web" {
  name         = "web"
  machine_type = "e2-micro"
  zone         = "us-central1-a"
}

```

---

## 3. Избегание Vendor Lock-in

### 3.1 Уровни Lock-in

```python

lockin_levels = {
    "Low": {
        "examples": ["EC2", "GCE", "Azure VMs"],
        "migration": "Easy - standard VMs",
        "strategy": "Use standard OS, containerize"
    },
    "Medium": {
        "examples": ["RDS", "Cloud SQL", "Azure SQL"],
        "migration": "Moderate - use standard engines (PostgreSQL)",
        "strategy": "Avoid proprietary features (Aurora Serverless)"
    },
    "High": {
        "examples": ["DynamoDB", "Spanner", "Cosmos DB"],
        "migration": "Difficult - proprietary data models",
        "strategy": "Use if benefits outweigh lock-in risk"
    },
    "Very High": {
        "examples": ["Lambda", "Cloud Functions", "Step Functions"],
        "migration": "Very difficult - proprietary APIs",
        "strategy": "Abstract with containers, or accept lock-in"
    }
}

for level, details in lockin_levels.items():
    print(f"\n{level} Lock-in:")
    print(f"  Examples: {', '.join(details['examples'][:2])}")
    print(f"  Strategy: {details['strategy']}")

```

### 3.2 Portable Alternatives

```python

portable_alternatives = {
    "Serverless": {
        "proprietary": "Lambda, Cloud Functions",
        "portable": "Knative, OpenFaaS on Kubernetes"
    },
    "Object Storage": {
        "proprietary": "S3, GCS, Azure Blob",
        "portable": "MinIO (S3-compatible), Ceph"
    },
    "Message Queue": {
        "proprietary": "SQS, Cloud Pub/Sub",
        "portable": "RabbitMQ, Apache Kafka"
    },
    "NoSQL": {
        "proprietary": "DynamoDB, Firestore",
        "portable": "MongoDB Atlas, CockroachDB"
    },
    "Cache": {
        "proprietary": "ElastiCache",
        "portable": "Redis, Memcached (self-managed or Atlas)"
    }
}

print("Portable Alternatives:\n")
for category, options in portable_alternatives.items():
    print(f"{category}:")
    print(f"  Proprietary: {options['proprietary']}")
    print(f"  Portable: {options['portable']}\n")

```

---

## 4. Standards и APIs

### 4.1 Cloud Standards

```python

cloud_standards = {
    "Kubernetes": "Container orchestration standard",
    "OpenTelemetry": "Observability (metrics, traces, logs)",
    "CloudEvents": "Event format specification",
    "OCI": "Container image format",
    "S3 API": "De-facto object storage API",
    "OpenID Connect": "Identity federation",
    "Prometheus": "Metrics format and scraping",
    "Grafana": "Visualization",
    "Terraform HCL": "IaC language (multi-cloud)"
}

print("Cloud-Agnostic Standards:")
for standard, purpose in cloud_standards.items():
    print(f"  • {standard}: {purpose}")

```

### 4.2 CNCF Projects

```

┌────────────────────────────────────────────────────────────────────┐
│              CNCF Graduated Projects (Cloud Native Standards)       │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Orchestration: Kubernetes                                         │
│  Service Mesh: Istio, Linkerd                                      │
│  Observability: Prometheus, Jaeger, Fluentd                        │
│  Storage: Rook, Longhorn                                          │
│  Networking: CoreDNS, Envoy, CNI                                  │
│  Security: Falco, OPA                                             │
│  CI/CD: Argo, Flux                                                │
│  Runtime: containerd, CRI-O                                       │
│                                                                     │
│  Using CNCF projects = more portable cloud-native stack           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 5. Migration Strategies

### 5.1 Cloud-to-Cloud Migration

```python

migration_approaches = {
    "Rehost (Lift & Shift)": {
        "description": "Move VMs as-is",
        "effort": "Low",
        "cloud_native": "No"
    },
    "Replatform": {
        "description": "Minor changes (e.g., managed DB)",
        "effort": "Medium",
        "cloud_native": "Partial"
    },
    "Refactor": {
        "description": "Rewrite for cloud-native",
        "effort": "High",
        "cloud_native": "Yes"
    },
    "Repurchase": {
        "description": "Move to SaaS",
        "effort": "Medium",
        "cloud_native": "N/A"
    }
}

# Data migration challenges:
# - Data egress costs (can be $0.09/GB)
# - Downtime window
# - Data consistency
# - Application cutover coordination
```

---

## 6. Recommendations

```python

recommendations = {
    "Start cloud-native": [
        "Containerize applications (Docker)",
        "Use Kubernetes for orchestration",
        "Design stateless applications",
        "Use managed open-source databases (PostgreSQL)"
    ],
    "Abstract infrastructure": [
        "Use Terraform for IaC",
        "Avoid deep proprietary integrations",
        "Use standard APIs (S3, OpenTelemetry)",
        "Document cloud-specific dependencies"
    ],
    "Be pragmatic": [
        "Don't over-engineer for hypothetical multi-cloud",
        "Use proprietary services when value > lock-in risk",
        "Evaluate actual exit costs before optimizing",
        "Consider: Will you really migrate?"
    ]
}

for category, items in recommendations.items():
    print(f"\n{category.upper()}:")
    for item in items:
        print(f"  • {item}")

```

---

## 💡 Key Takeaways

- **Multi-cloud ≠ cloud-agnostic** — different strategies

- **Kubernetes** — best compute abstraction layer

- **Terraform** — multi-cloud IaC

- **Lock-in trade-off** — managed services vs portability

- **Standards** — CNCF, OpenTelemetry, S3 API

- **Be pragmatic** — don't optimize for unlikely migration

---

## 📚 Additional Resources

- [CNCF Landscape](https://landscape.cncf.io/)
- [Cloud Native Patterns](https://www.cloudnativepatterns.io/)

---

## 🚀 Next Steps

**Следующие модули:**

- [25_CaseStudies](../25_CaseStudies/) — Реальные примеры multi-cloud

**Практика:**

1. Разверните одно приложение в AWS и GCP
2. Настройте Terraform для multi-cloud
3. Реализуйте Kubernetes deployment в EKS и GKE

**Это предпоследний модуль курса Cloud Native.**



