# Cloud Native Development
## VPC: Virtual Private Cloud

---

## 📋 Prerequisites

- Базовые знания сетей (IP, subnets, routing)
- Понимание архитектуры AWS (регионы, AZ)

---

## 🎯 Learning Objectives

- Проектировать VPC с public/private subnets
- Настраивать Security Groups и NACLs
- Понимать NAT Gateway, Internet Gateway
- Настраивать VPC Peering и Transit Gateway

---

## 1. Введение в VPC

### 1.1 Что такое VPC

**Amazon Virtual Private Cloud (VPC)** — логически изолированная виртуальная сеть в AWS, где вы запускаете ресурсы.

```
┌────────────────────────────────────────────────────────────────────┐
│                        VPC: 10.0.0.0/16                            │
│                        (65,536 IP addresses)                       │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────┐  ┌─────────────────────────┐         │
│  │    Availability Zone A   │  │    Availability Zone B   │         │
│  │                          │  │                          │         │
│  │  ┌────────────────────┐  │  │  ┌────────────────────┐  │         │
│  │  │ Public Subnet      │  │  │  │ Public Subnet      │  │         │
│  │  │ 10.0.1.0/24        │  │  │  │ 10.0.2.0/24        │  │         │
│  │  │ • NAT Gateway      │  │  │  │ • ALB              │  │         │
│  │  │ • Bastion Host     │  │  │  │                    │  │         │
│  │  └────────────────────┘  │  │  └────────────────────┘  │         │
│  │                          │  │                          │         │
│  │  ┌────────────────────┐  │  │  ┌────────────────────┐  │         │
│  │  │ Private Subnet     │  │  │  │ Private Subnet     │  │         │
│  │  │ 10.0.11.0/24       │  │  │  │ 10.0.12.0/24       │  │         │
│  │  │ • EC2 App Servers  │  │  │  │ • EC2 App Servers  │  │         │
│  │  └────────────────────┘  │  │  └────────────────────┘  │         │
│  │                          │  │                          │         │
│  │  ┌────────────────────┐  │  │  ┌────────────────────┐  │         │
│  │  │ Data Subnet        │  │  │  │ Data Subnet        │  │         │
│  │  │ 10.0.21.0/24       │  │  │  │ 10.0.22.0/24       │  │         │
│  │  │ • RDS              │  │  │  │ • RDS (standby)    │  │         │
│  │  └────────────────────┘  │  │  └────────────────────┘  │         │
│  │                          │  │                          │         │
│  └─────────────────────────┘  └─────────────────────────┘         │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 CIDR Planning

```python
cidr_examples = {
    "/16": {"hosts": 65536, "use_case": "Large VPC"},
    "/20": {"hosts": 4096, "use_case": "Medium VPC"},
    "/24": {"hosts": 256, "use_case": "Subnet"},
    "/28": {"hosts": 16, "use_case": "Small subnet (minimum for some services)"}
}

# AWS резервирует 5 IP в каждой подсети:
# .0 - Network address
# .1 - VPC router
# .2 - DNS
# .3 - Reserved
# .255 - Broadcast

print("CIDR Planning:\n")
for cidr, info in cidr_examples.items():
    usable = info["hosts"] - 5
    print(f"  {cidr}: {info['hosts']} total, {usable} usable - {info['use_case']}")
```

---

## 2. Компоненты VPC

### 2.1 Internet Gateway (IGW)

```bash
# Создание Internet Gateway
aws ec2 create-internet-gateway --tag-specifications \
    'ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]'

# Присоединение к VPC
aws ec2 attach-internet-gateway \
    --internet-gateway-id igw-12345678 \
    --vpc-id vpc-12345678
```

### 2.2 NAT Gateway

```bash
# NAT Gateway позволяет private subnet выходить в интернет
# Но не позволяет входящие соединения

# Создание Elastic IP для NAT Gateway
aws ec2 allocate-address --domain vpc

# Создание NAT Gateway в public subnet
aws ec2 create-nat-gateway \
    --subnet-id subnet-public-1a \
    --allocation-id eipalloc-12345678
```

### 2.3 Route Tables

```python
# Public subnet route table
public_routes = [
    {"destination": "10.0.0.0/16", "target": "local"},      # VPC internal
    {"destination": "0.0.0.0/0", "target": "igw-12345"}     # Internet
]

# Private subnet route table
private_routes = [
    {"destination": "10.0.0.0/16", "target": "local"},      # VPC internal
    {"destination": "0.0.0.0/0", "target": "nat-12345"}     # NAT Gateway
]
```

---

## 3. Security Groups vs NACLs

```
┌────────────────────────────────────────────────────────────────────┐
│           Security Groups vs Network ACLs                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SECURITY GROUPS                  NETWORK ACLs                     │
│  ─────────────────                ─────────────                    │
│  • Instance level                 • Subnet level                   │
│  • Stateful                       • Stateless                      │
│  • Allow rules only               • Allow and Deny rules           │
│  • All rules evaluated            • Rules evaluated in order       │
│  • Default: deny all inbound      • Default: allow all             │
│                                                                     │
│  Example SG:                      Example NACL:                    │
│  ALLOW TCP 443 from 0.0.0.0/0     100 ALLOW TCP 443 0.0.0.0/0     │
│  ALLOW TCP 22 from 10.0.0.0/16    110 ALLOW TCP 22 10.0.0.0/16    │
│                                   120 DENY ALL 0.0.0.0/0           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.1 Security Group Example

```bash
# Web server security group
aws ec2 create-security-group \
    --group-name web-sg \
    --description "Web server security group" \
    --vpc-id vpc-12345678

# Allow HTTPS from anywhere
aws ec2 authorize-security-group-ingress \
    --group-id sg-12345678 \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0

# Allow HTTP from ALB security group
aws ec2 authorize-security-group-ingress \
    --group-id sg-12345678 \
    --protocol tcp \
    --port 80 \
    --source-group sg-alb-12345
```

---

## 4. VPC Endpoints

```python
vpc_endpoint_types = {
    "Gateway Endpoint": {
        "services": ["S3", "DynamoDB"],
        "cost": "Free",
        "how": "Route table entry"
    },
    "Interface Endpoint": {
        "services": ["Most AWS services"],
        "cost": "$0.01/hour + data",
        "how": "ENI in subnet with private IP"
    }
}

# Без VPC Endpoint: EC2 → Internet → S3
# С VPC Endpoint: EC2 → Private → S3 (no internet)
```

---

## 5. VPC Peering и Transit Gateway

```
┌────────────────────────────────────────────────────────────────────┐
│                    Transit Gateway                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                    ┌─────────────────┐                             │
│                    │ Transit Gateway │                             │
│                    └────────┬────────┘                             │
│                             │                                       │
│      ┌──────────────────────┼──────────────────────┐               │
│      │                      │                      │               │
│      ▼                      ▼                      ▼               │
│  ┌────────┐            ┌────────┐            ┌────────┐           │
│  │ VPC A  │            │ VPC B  │            │ VPC C  │           │
│  │ Prod   │            │  Dev   │            │ Shared │           │
│  └────────┘            └────────┘            └────────┘           │
│                             │                                       │
│                             ▼                                       │
│                    ┌─────────────────┐                             │
│                    │   VPN / Direct  │                             │
│                    │    Connect      │                             │
│                    └─────────────────┘                             │
│                                                                     │
│  Transit Gateway: hub-and-spoke для многих VPC                    │
│  VPC Peering: point-to-point, не транзитивный                     │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 6. Best Practices

```python
vpc_best_practices = [
    "Планируйте CIDR заранее (избегайте overlap с on-premise)",
    "Используйте несколько AZ для HA",
    "Разделяйте public/private/data subnets",
    "Используйте VPC Flow Logs для мониторинга",
    "Security Groups > NACLs (более гибкие)",
    "VPC Endpoints для AWS сервисов (security + cost)",
    "NAT Gateway per AZ для HA",
    "Документируйте IP allocation"
]
```

---

## 💡 Key Takeaways

- **VPC** — изолированная сеть для ваших ресурсов
- **Public subnet** — имеет route к Internet Gateway
- **Private subnet** — выход через NAT Gateway
- **Security Groups** — stateful, instance level, allow only
- **NACLs** — stateless, subnet level, allow/deny
- **VPC Endpoints** — приватный доступ к AWS сервисам

---

## 📚 Additional Resources

- [VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/)
- [VPC CIDR Calculator](https://www.ipaddressguide.com/cidr)

---

