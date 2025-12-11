# Containers: ECS, EKS, Fargate

---

## 📋 Prerequisites

- Базовые знания Docker
- Понимание контейнеризации
- Знакомство с VPC и IAM

---

## 🎯 Learning Objectives

- Различать ECS и EKS
- Выбирать между EC2 и Fargate launch types
- Создавать Task Definitions и Services
- Понимать networking для контейнеров

---

## 1. Container Services в AWS

### 1.1 Обзор

```

┌────────────────────────────────────────────────────────────────────┐
│                AWS Container Services                               │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ORCHESTRATION (Control Plane)                                     │
│  ┌──────────────────┐    ┌──────────────────┐                     │
│  │       ECS        │    │       EKS        │                     │
│  │ AWS-native       │    │ Managed          │                     │
│  │ orchestrator     │    │ Kubernetes       │                     │
│  └────────┬─────────┘    └────────┬─────────┘                     │
│           │                       │                                │
│           └───────────┬───────────┘                                │
│                       │                                            │
│  COMPUTE (Data Plane) ▼                                           │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                                                               │ │
│  │  ┌──────────────┐              ┌──────────────┐              │ │
│  │  │     EC2      │              │   Fargate    │              │ │
│  │  │ Self-managed │              │  Serverless  │              │ │
│  │  │   instances  │              │  containers  │              │ │
│  │  └──────────────┘              └──────────────┘              │ │
│  │                                                               │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  REGISTRY                                                          │
│  ┌──────────────────┐                                             │
│  │       ECR        │  Private Docker registry                    │
│  └──────────────────┘                                             │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 1.2 ECS vs EKS

```python

comparison = {
    "Learning Curve": {
        "ECS": "Low (AWS-native, simpler API)",
        "EKS": "High (Kubernetes complexity)"
    },
    "Portability": {
        "ECS": "AWS only",
        "EKS": "Multi-cloud (Kubernetes standard)"
    },
    "Ecosystem": {
        "ECS": "AWS integrations",
        "EKS": "CNCF ecosystem, Helm, operators"
    },
    "Cost": {
        "ECS": "Free control plane",
        "EKS": "$0.10/hour per cluster (~$73/month)"
    },
    "Best For": {
        "ECS": "AWS-first teams, simpler workloads",
        "EKS": "K8s expertise, multi-cloud, complex apps"
    }
}

print("ECS vs EKS:\n")
for aspect, values in comparison.items():
    print(f"{aspect}:")
    print(f"  ECS: {values['ECS']}")
    print(f"  EKS: {values['EKS']}\n")

```

---

## 2. Amazon ECS

### 2.1 Core Concepts

```

┌────────────────────────────────────────────────────────────────────┐
│                    ECS Core Concepts                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CLUSTER                                                           │
│  └── Logical grouping of tasks/services                           │
│                                                                     │
│  TASK DEFINITION (blueprint)                                       │
│  ├── Container image(s)                                           │
│  ├── CPU/Memory requirements                                      │
│  ├── Port mappings                                                │
│  ├── Environment variables                                        │
│  ├── IAM role                                                     │
│  └── Logging configuration                                        │
│                                                                     │
│  TASK (running instance)                                          │
│  └── One or more containers from task definition                  │
│                                                                     │
│  SERVICE                                                           │
│  ├── Maintains desired count of tasks                             │
│  ├── Load balancer integration                                    │
│  ├── Auto-scaling                                                 │
│  └── Rolling updates                                              │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 2.2 Task Definition

```json

{
    "family": "my-web-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "512",
    "memory": "1024",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
    "taskRoleArn": "arn:aws:iam::123456789012:role/ecsTaskRole",
    "containerDefinitions": [
        {
            "name": "web",
            "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:v1.0",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 8080,
                    "protocol": "tcp"
                }
            ],
            "environment": [
                {"name": "ENV", "value": "production"}
            ],
            "secrets": [
                {
                    "name": "DB_PASSWORD",
                    "valueFrom": "arn:aws:secretsmanager:us-east-1:123456789012:secret:db-password"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/my-web-app",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                }
            },
            "healthCheck": {
                "command": ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
                "interval": 30,
                "timeout": 5,
                "retries": 3
            }
        }
    ]
}

```

### 2.3 Создание Service

```bash

aws ecs create-service \
    --cluster my-cluster \
    --service-name my-service \
    --task-definition my-web-app:1 \
    --desired-count 3 \
    --launch-type FARGATE \
    --network-configuration "awsvpcConfiguration={subnets=[subnet-1,subnet-2],securityGroups=[sg-123],assignPublicIp=DISABLED}" \
    --load-balancers "targetGroupArn=arn:aws:elasticloadbalancing:...,containerName=web,containerPort=8080" \
    --deployment-configuration "maximumPercent=200,minimumHealthyPercent=100"

```

---

## 3. AWS Fargate

### 3.1 Serverless Containers

```python

fargate_benefits = {
    "No servers": "AWS manages EC2 instances",
    "Right-sizing": "Pay for exact CPU/memory used",
    "Scaling": "Add tasks without capacity planning",
    "Security": "Task-level isolation",
    "Simplicity": "Focus on containers, not infrastructure"
}

fargate_limitations = {
    "No GPU": "GPU instances not supported",
    "No persistent storage": "No EBS (only EFS)",
    "Higher cost": "More expensive than well-utilized EC2",
    "Cold start": "Slight delay for new tasks"
}

print("Fargate Benefits:")
for benefit, description in fargate_benefits.items():
    print(f"  ✅ {benefit}: {description}")

print("\nFargate Limitations:")
for limitation, description in fargate_limitations.items():
    print(f"  ⚠️ {limitation}: {description}")

```

### 3.2 Fargate Pricing

```python
# Fargate pricing (us-east-1)
# CPU: $0.04048 per vCPU per hour
# Memory: $0.004445 per GB per hour

def calculate_fargate_cost(vcpu: float, memory_gb: float, hours: int) -> float:
    cpu_cost = vcpu * 0.04048 * hours
    memory_cost = memory_gb * 0.004445 * hours
    return round(cpu_cost + memory_cost, 2)

# Example: 0.5 vCPU, 1 GB memory, running 24/7 for a month
monthly_cost = calculate_fargate_cost(0.5, 1, 730)
print(f"Fargate monthly cost (0.5 vCPU, 1GB): ${monthly_cost}")  # ~$18

```

---

## 4. Amazon EKS

### 4.1 Managed Kubernetes

```bash
# Создание EKS кластера
eksctl create cluster \
    --name my-cluster \
    --region us-east-1 \
    --nodegroup-name standard-workers \
    --node-type t3.medium \
    --nodes 3 \
    --nodes-min 1 \
    --nodes-max 5 \
    --managed

# Или с Fargate profile
eksctl create cluster \
    --name my-cluster \
    --fargate

```

### 4.2 EKS Components

```

┌────────────────────────────────────────────────────────────────────┐
│                    EKS Architecture                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │              EKS Control Plane (managed by AWS)             │   │
│  │  • API Server                                               │   │
│  │  • etcd (distributed state)                                 │   │
│  │  • Controller Manager                                       │   │
│  │  • Scheduler                                                │   │
│  └────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ kubectl / API                       │
│                              ▼                                      │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │              Data Plane (your account)                      │   │
│  │                                                             │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │   │
│  │  │   Node 1     │  │   Node 2     │  │   Node 3     │     │   │
│  │  │ (EC2/Fargate)│  │ (EC2/Fargate)│  │ (EC2/Fargate)│     │   │
│  │  │  ┌───────┐   │  │  ┌───────┐   │  │  ┌───────┐   │     │   │
│  │  │  │ Pod   │   │  │  │ Pod   │   │  │  │ Pod   │   │     │   │
│  │  │  │ Pod   │   │  │  │ Pod   │   │  │  │ Pod   │   │     │   │
│  │  │  └───────┘   │  │  └───────┘   │  │  └───────┘   │     │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘     │   │
│  │                                                             │   │
│  └────────────────────────────────────────────────────────────┘   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 5. Amazon ECR

### 5.1 Private Container Registry

```bash
# Создание репозитория
aws ecr create-repository \
    --repository-name my-app \
    --image-scanning-configuration scanOnPush=true

# Login
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com

# Build and push
docker build -t my-app:v1.0 .
docker tag my-app:v1.0 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:v1.0
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:v1.0

```

---

## 6. Networking

### 6.1 awsvpc Network Mode

```

┌────────────────────────────────────────────────────────────────────┐
│                awsvpc Network Mode (Fargate default)                │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Каждая Task получает:                                            │
│  • Собственный ENI (Elastic Network Interface)                    │
│  • Private IP в VPC subnet                                        │
│  • Применяются Security Groups                                    │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                        VPC                                    │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                    Subnet                                │ │ │
│  │  │                                                          │ │ │
│  │  │  ┌────────────┐  ┌────────────┐  ┌────────────┐        │ │ │
│  │  │  │  Task      │  │  Task      │  │  Task      │        │ │ │
│  │  │  │  ENI: 10.0.│  │  ENI: 10.0.│  │  ENI: 10.0.│        │ │ │
│  │  │  │  0.10      │  │  0.11      │  │  0.12      │        │ │ │
│  │  │  │  SG: web   │  │  SG: web   │  │  SG: web   │        │ │ │
│  │  │  └────────────┘  └────────────┘  └────────────┘        │ │ │
│  │  │                                                          │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 7. Когда что выбрать

```python

decision_guide = {
    "ECS + Fargate": {
        "when": [
            "AWS-first, simpler requirements",
            "Don't want to manage servers",
            "Variable or unpredictable workloads"
        ]
    },
    "ECS + EC2": {
        "when": [
            "Need GPU or specific instance types",
            "Cost optimization at scale",
            "Existing EC2 fleet"
        ]
    },
    "EKS + Fargate": {
        "when": [
            "Kubernetes required but no ops capacity",
            "Multi-cloud portability future"
        ]
    },
    "EKS + EC2": {
        "when": [
            "Complex Kubernetes features needed",
            "Have Kubernetes expertise",
            "Need DaemonSets, specific node configs"
        ]
    }
}

for option, details in decision_guide.items():
    print(f"\n{option}:")
    for condition in details['when']:
        print(f"  • {condition}")

```

---

## 💡 Key Takeaways

- **ECS** — AWS-native, simpler, free control plane

- **EKS** — Kubernetes standard, portable, $73/month control plane

- **Fargate** — serverless containers, no EC2 management

- **EC2** — more control, potentially cheaper at scale

- **ECR** — private Docker registry with scanning

- **awsvpc** — each task gets its own ENI and IP

---

## 📚 Additional Resources

- [ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)
- [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/)

---

## 🚀 Next Steps

**Следующие модули:**

- [12_Messaging](../12_Messaging/) — SQS, SNS, EventBridge
- [17_CICD](../17_CICD/) — CI/CD пайплайны для контейнеров

**Практика:**

1. Разверните приложение в ECS Fargate
2. Настройте EKS кластер с eksctl
3. Реализуйте blue/green deployment



