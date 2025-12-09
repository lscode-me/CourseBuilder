# VPC: Virtual Private Cloud
## Проектирование и управление сетевой инфраструктурой в AWS

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать основы сетей (IP-адресация, subnets, routing, TCP/IP)
- Понимать архитектуру AWS (регионы, Availability Zones)
- Иметь базовое представление о firewall и сетевой безопасности
- Уметь работать с AWS Console или CLI

**Recommended prior modules:**
- [03_Architecture](../03_Architecture/) — архитектура AWS
- [05_EC2](../05_EC2/) — работа с EC2 инстансами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проектировать VPC с public/private subnets в нескольких AZ
- Настраивать Security Groups и Network ACLs для защиты ресурсов
- Понимать и настраивать NAT Gateway, Internet Gateway, Route Tables
- Использовать VPC Endpoints для приватного доступа к AWS сервисам
- Настраивать VPC Peering и Transit Gateway для связи между VPC

---

## 1. Введение в VPC

### 1.1 Что такое VPC

**Amazon Virtual Private Cloud (VPC)** — это логически изолированная виртуальная сеть в облаке AWS, которая даёт вам полный контроль над сетевым окружением:

- **Диапазон IP-адресов** — вы определяете CIDR блок
- **Подсети** — разделение на public/private
- **Маршрутизация** — Route Tables для управления трафиком
- **Безопасность** — Security Groups и Network ACLs
- **Шлюзы** — Internet Gateway, NAT Gateway, VPN Gateway

**Ключевые концепции:**

```
VPC = Ваш собственный виртуальный дата-центр в AWS

┌─────────────────────────────────────────────────────────────────────────────┐
│                          AWS Region (us-east-1)                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                        VPC: 10.0.0.0/16                                │  │
│  │                        (65,536 IP addresses)                           │  │
│  │                                                                         │  │
│  │  ┌─────────────────────────┐    ┌─────────────────────────┐           │  │
│  │  │    Availability Zone A   │    │    Availability Zone B   │           │  │
│  │  │                          │    │                          │           │  │
│  │  │  ┌────────────────────┐  │    │  ┌────────────────────┐  │           │  │
│  │  │  │ Public Subnet      │  │    │  │ Public Subnet      │  │           │  │
│  │  │  │ 10.0.1.0/24        │  │    │  │ 10.0.2.0/24        │  │           │  │
│  │  │  │ • NAT Gateway      │  │    │  │ • ALB              │  │           │  │
│  │  │  │ • Bastion Host     │  │    │  │ • Web Servers      │  │           │  │
│  │  │  └────────────────────┘  │    │  └────────────────────┘  │           │  │
│  │  │                          │    │                          │           │  │
│  │  │  ┌────────────────────┐  │    │  ┌────────────────────┐  │           │  │
│  │  │  │ Private Subnet     │  │    │  │ Private Subnet     │  │           │  │
│  │  │  │ 10.0.11.0/24       │  │    │  │ 10.0.12.0/24       │  │           │  │
│  │  │  │ • EC2 App Servers  │  │    │  │ • EC2 App Servers  │  │           │  │
│  │  │  │ • Lambda Functions │  │    │  │ • Lambda Functions │  │           │  │
│  │  │  └────────────────────┘  │    │  └────────────────────┘  │           │  │
│  │  │                          │    │                          │           │  │
│  │  │  ┌────────────────────┐  │    │  ┌────────────────────┐  │           │  │
│  │  │  │ Data Subnet        │  │    │  │ Data Subnet        │  │           │  │
│  │  │  │ 10.0.21.0/24       │  │    │  │ 10.0.22.0/24       │  │           │  │
│  │  │  │ • RDS Primary      │  │    │  │ • RDS Standby      │  │           │  │
│  │  │  │ • ElastiCache      │  │    │  │ • ElastiCache      │  │           │  │
│  │  │  └────────────────────┘  │    │  └────────────────────┘  │           │  │
│  │  │                          │    │                          │           │  │
│  │  └─────────────────────────┘    └─────────────────────────┘           │  │
│  │                                                                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Default VPC vs Custom VPC

AWS автоматически создаёт Default VPC в каждом регионе:

| Характеристика | Default VPC | Custom VPC |
|----------------|-------------|------------|
| **CIDR** | 172.31.0.0/16 | Вы определяете (10.0.0.0/16, etc.) |
| **Subnets** | 1 public subnet в каждой AZ | Вы создаёте |
| **Internet Gateway** | Уже подключен | Создаёте и подключаете |
| **DNS** | Включен | Настраиваете |
| **Использование** | Quick start, development | Production workloads |

**Рекомендация:** Для production всегда используйте Custom VPC с продуманной архитектурой.

### 1.3 CIDR Planning

**CIDR (Classless Inter-Domain Routing)** определяет диапазон IP-адресов для вашей сети.

```python
# CIDR примеры и расчёт доступных адресов
cidr_examples = {
    "/16": {
        "total_hosts": 65536,
        "usable_hosts": 65531,  # AWS резервирует 5 адресов
        "use_case": "Large VPC — основной блок",
        "example": "10.0.0.0/16"
    },
    "/20": {
        "total_hosts": 4096,
        "usable_hosts": 4091,
        "use_case": "Medium VPC или large subnet",
        "example": "10.0.0.0/20"
    },
    "/24": {
        "total_hosts": 256,
        "usable_hosts": 251,
        "use_case": "Standard subnet",
        "example": "10.0.1.0/24"
    },
    "/28": {
        "total_hosts": 16,
        "usable_hosts": 11,
        "use_case": "Minimum subnet (для ELB, NAT Gateway)",
        "example": "10.0.1.0/28"
    }
}

# AWS резервирует 5 IP в каждой подсети:
reserved_ips = """
.0   - Network address (адрес сети)
.1   - VPC router (маршрутизатор)
.2   - DNS server (Amazon DNS)
.3   - Reserved for future use
.255 - Broadcast (broadcast запрещён в VPC, но адрес зарезервирован)
"""

print("CIDR Planning Guide:")
print("=" * 60)
for cidr, info in cidr_examples.items():
    print(f"\n{cidr}:")
    print(f"  Total IPs:  {info['total_hosts']:,}")
    print(f"  Usable IPs: {info['usable_hosts']:,}")
    print(f"  Use case:   {info['use_case']}")
    print(f"  Example:    {info['example']}")
```

**Output:**
```
CIDR Planning Guide:
============================================================

/16:
  Total IPs:  65,536
  Usable IPs: 65,531
  Use case:   Large VPC — основной блок
  Example:    10.0.0.0/16

/24:
  Total IPs:  256
  Usable IPs: 251
  Use case:   Standard subnet
  Example:    10.0.1.0/24
```

**Пример планирования для production:**

```
VPC: 10.0.0.0/16 (65,536 IPs)
│
├── Public Subnets (для ресурсов с public IP)
│   ├── AZ-a: 10.0.1.0/24  (251 usable)
│   ├── AZ-b: 10.0.2.0/24  (251 usable)
│   └── AZ-c: 10.0.3.0/24  (251 usable)
│
├── Private Subnets (для application servers)
│   ├── AZ-a: 10.0.11.0/24 (251 usable)
│   ├── AZ-b: 10.0.12.0/24 (251 usable)
│   └── AZ-c: 10.0.13.0/24 (251 usable)
│
├── Data Subnets (для databases)
│   ├── AZ-a: 10.0.21.0/24 (251 usable)
│   ├── AZ-b: 10.0.22.0/24 (251 usable)
│   └── AZ-c: 10.0.23.0/24 (251 usable)
│
└── Reserved (для будущего роста)
    └── 10.0.100.0/24 - 10.0.255.0/24
```

> **⚠️ Важно:** Планируйте CIDR заранее! Изменить CIDR существующего VPC невозможно. Убедитесь, что ваши диапазоны не пересекаются с on-premise сетями.

---

## 2. Компоненты VPC

### 2.1 Internet Gateway (IGW)

**Internet Gateway** — шлюз, обеспечивающий связь между VPC и интернетом. Без него ресурсы в VPC не могут выходить в интернет.

```
┌─────────────────────────────────────────────────┐
│                   INTERNET                       │
└─────────────────────────────────────────────────┘
                        │
                        ▼
            ┌───────────────────┐
            │  Internet Gateway │
            │    (igw-xxxxx)    │
            └───────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│                     VPC                          │
│  ┌─────────────────────────────────────────┐    │
│  │           Public Subnet                  │    │
│  │  Route: 0.0.0.0/0 → igw-xxxxx           │    │
│  │  • EC2 with public IP                    │    │
│  │  • NAT Gateway                           │    │
│  └─────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

**Создание и настройка:**

```bash
# 1. Создание Internet Gateway
aws ec2 create-internet-gateway \
    --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=prod-igw}]'

# Output: InternetGatewayId: igw-0123456789abcdef0

# 2. Присоединение к VPC
aws ec2 attach-internet-gateway \
    --internet-gateway-id igw-0123456789abcdef0 \
    --vpc-id vpc-0123456789abcdef0

# 3. Добавление маршрута в Route Table
aws ec2 create-route \
    --route-table-id rtb-0123456789abcdef0 \
    --destination-cidr-block 0.0.0.0/0 \
    --gateway-id igw-0123456789abcdef0
```

**Характеристики IGW:**
- Horizontally scaled, redundant, highly available
- Не создаёт bandwidth bottleneck
- Один IGW на VPC
- Бесплатный (платите только за data transfer)

### 2.2 NAT Gateway

**NAT Gateway** позволяет ресурсам в private subnet выходить в интернет, но блокирует входящие соединения из интернета.

```
┌─────────────────────────────────────────────────────────────────┐
│                          INTERNET                                │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
                    ┌───────────────────┐
                    │  Internet Gateway │
                    └───────────────────┘
                               │
┌──────────────────────────────┼──────────────────────────────────┐
│                            VPC                                   │
│                              │                                   │
│  ┌───────────────────────────┼───────────────────────────┐      │
│  │      PUBLIC SUBNET        │                            │      │
│  │      10.0.1.0/24          │                            │      │
│  │                           │                            │      │
│  │    ┌──────────────────────┴──────────┐                │      │
│  │    │         NAT Gateway              │                │      │
│  │    │      (Elastic IP attached)       │                │      │
│  │    │        203.0.113.50              │                │      │
│  │    └──────────────────────────────────┘                │      │
│  │                    ▲                                   │      │
│  └────────────────────┼───────────────────────────────────┘      │
│                       │                                          │
│  ┌────────────────────┼───────────────────────────────────┐      │
│  │      PRIVATE SUBNET                                    │      │
│  │      10.0.11.0/24                                      │      │
│  │      Route: 0.0.0.0/0 → nat-xxxxx                     │      │
│  │                                                        │      │
│  │    ┌─────────────────┐  ┌─────────────────┐           │      │
│  │    │  App Server 1   │  │  App Server 2   │           │      │
│  │    │  10.0.11.10     │  │  10.0.11.11     │           │      │
│  │    └─────────────────┘  └─────────────────┘           │      │
│  │                                                        │      │
│  └────────────────────────────────────────────────────────┘      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Создание NAT Gateway:**

```bash
# 1. Allocate Elastic IP
aws ec2 allocate-address --domain vpc
# Output: AllocationId: eipalloc-0123456789abcdef0

# 2. Create NAT Gateway in public subnet
aws ec2 create-nat-gateway \
    --subnet-id subnet-public-1a \
    --allocation-id eipalloc-0123456789abcdef0 \
    --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=prod-nat-1a}]'

# 3. Add route in private subnet route table
aws ec2 create-route \
    --route-table-id rtb-private \
    --destination-cidr-block 0.0.0.0/0 \
    --nat-gateway-id nat-0123456789abcdef0
```

**NAT Gateway vs NAT Instance:**

| Характеристика | NAT Gateway | NAT Instance |
|----------------|-------------|--------------|
| **Управление** | AWS managed | Вы управляете |
| **Availability** | HA в пределах AZ | Single instance |
| **Bandwidth** | До 45 Gbps | Зависит от instance type |
| **Cost** | $0.045/час + $0.045/GB | EC2 pricing |
| **Security Groups** | Нет | Да |
| **Использование** | Production | Dev/Test или когда нужен SG |

**Best Practice:** Создавайте NAT Gateway в каждой AZ для High Availability.

### 2.3 Route Tables

**Route Table** определяет, куда направляется сетевой трафик из подсети.

```python
# Пример Route Tables для трёхуровневой архитектуры

# Public Subnet Route Table
public_route_table = {
    "name": "public-rt",
    "routes": [
        {
            "destination": "10.0.0.0/16",
            "target": "local",
            "description": "Traffic within VPC"
        },
        {
            "destination": "0.0.0.0/0",
            "target": "igw-xxxxx",
            "description": "Internet access via IGW"
        }
    ],
    "associated_subnets": ["public-1a", "public-1b", "public-1c"]
}

# Private Subnet Route Table (AZ-a)
private_route_table_a = {
    "name": "private-rt-1a",
    "routes": [
        {
            "destination": "10.0.0.0/16",
            "target": "local",
            "description": "Traffic within VPC"
        },
        {
            "destination": "0.0.0.0/0",
            "target": "nat-xxxxx-1a",
            "description": "Internet access via NAT Gateway in AZ-a"
        }
    ],
    "associated_subnets": ["private-1a", "data-1a"]
}

# Data Subnet Route Table (no internet access)
data_route_table = {
    "name": "data-rt",
    "routes": [
        {
            "destination": "10.0.0.0/16",
            "target": "local",
            "description": "Traffic within VPC only"
        }
        # No route to 0.0.0.0/0 — полная изоляция от интернета
    ],
    "associated_subnets": ["data-1a", "data-1b", "data-1c"]
}
```

**Создание Route Table через CLI:**

```bash
# Create Route Table
aws ec2 create-route-table \
    --vpc-id vpc-xxxxx \
    --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=private-rt}]'

# Add Route
aws ec2 create-route \
    --route-table-id rtb-xxxxx \
    --destination-cidr-block 0.0.0.0/0 \
    --nat-gateway-id nat-xxxxx

# Associate with Subnet
aws ec2 associate-route-table \
    --route-table-id rtb-xxxxx \
    --subnet-id subnet-xxxxx
```

---

## 3. Security Groups и Network ACLs

### 3.1 Security Groups

**Security Group** — виртуальный firewall на уровне instance (ENI). Работает по принципу whitelist — только разрешённый трафик пропускается.

```
┌────────────────────────────────────────────────────────────────────────┐
│                    Security Groups — Key Concepts                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  • STATEFUL: если разрешён inbound, return traffic автоматически       │
│    разрешён (не нужно явно разрешать outbound для ответов)             │
│                                                                         │
│  • ALLOW ONLY: можно только разрешать, нельзя запрещать                │
│                                                                         │
│  • INSTANCE LEVEL: привязывается к ENI (Elastic Network Interface)     │
│                                                                         │
│  • DEFAULT: deny all inbound, allow all outbound                       │
│                                                                         │
│  • REFERENCE SG: можно ссылаться на другие SG вместо IP-адресов       │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

**Пример конфигурации Security Groups для трёхуровневой архитектуры:**

```bash
# 1. ALB Security Group
aws ec2 create-security-group \
    --group-name alb-sg \
    --description "Application Load Balancer" \
    --vpc-id vpc-xxxxx

aws ec2 authorize-security-group-ingress \
    --group-id sg-alb \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
    --group-id sg-alb \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0

# 2. Web Server Security Group
aws ec2 create-security-group \
    --group-name web-sg \
    --description "Web Servers" \
    --vpc-id vpc-xxxxx

# Allow traffic only from ALB (reference by SG)
aws ec2 authorize-security-group-ingress \
    --group-id sg-web \
    --protocol tcp \
    --port 8080 \
    --source-group sg-alb

# 3. Database Security Group
aws ec2 create-security-group \
    --group-name db-sg \
    --description "Database Servers" \
    --vpc-id vpc-xxxxx

# Allow PostgreSQL only from web servers
aws ec2 authorize-security-group-ingress \
    --group-id sg-db \
    --protocol tcp \
    --port 5432 \
    --source-group sg-web
```

**Визуализация Security Groups chain:**

```
                 Internet
                     │
                     ▼
┌────────────────────────────────────────────┐
│  ALB Security Group (sg-alb)               │
│  ─────────────────────────                 │
│  Inbound:                                  │
│    • HTTPS (443) from 0.0.0.0/0           │
│    • HTTP (80) from 0.0.0.0/0             │
│  Outbound:                                 │
│    • All traffic (stateful return)        │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│  Web Security Group (sg-web)               │
│  ─────────────────────────                 │
│  Inbound:                                  │
│    • Port 8080 from sg-alb                │
│    • SSH (22) from sg-bastion             │
│  Outbound:                                 │
│    • Port 5432 to sg-db                   │
│    • HTTPS (443) to 0.0.0.0/0             │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│  Database Security Group (sg-db)           │
│  ─────────────────────────                 │
│  Inbound:                                  │
│    • PostgreSQL (5432) from sg-web        │
│  Outbound:                                 │
│    • None (или минимально необходимый)    │
└────────────────────────────────────────────┘
```

### 3.2 Network ACLs (NACLs)

**Network ACL** — firewall на уровне subnet. Работает как дополнительный слой защиты.

```
┌────────────────────────────────────────────────────────────────────────┐
│           Security Groups vs Network ACLs                               │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  SECURITY GROUPS                    NETWORK ACLs                       │
│  ─────────────────                  ─────────────                      │
│  • Instance level (ENI)             • Subnet level                     │
│  • Stateful                         • Stateless                        │
│  • Allow rules only                 • Allow AND Deny rules             │
│  • All rules evaluated              • Rules evaluated in NUMBER order  │
│  • Default: deny all inbound        • Default: allow all               │
│                                                                         │
│  Analogy:                           Analogy:                           │
│  Личная охрана у двери квартиры     Охрана на входе в здание          │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

**Пример Network ACL для public subnet:**

```bash
# Создание Network ACL
aws ec2 create-network-acl \
    --vpc-id vpc-xxxxx \
    --tag-specifications 'ResourceType=network-acl,Tags=[{Key=Name,Value=public-nacl}]'

# Inbound Rules
# Rule 100: Allow HTTPS
aws ec2 create-network-acl-entry \
    --network-acl-id acl-xxxxx \
    --rule-number 100 \
    --protocol tcp \
    --port-range From=443,To=443 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow \
    --ingress

# Rule 110: Allow HTTP
aws ec2 create-network-acl-entry \
    --network-acl-id acl-xxxxx \
    --rule-number 110 \
    --protocol tcp \
    --port-range From=80,To=80 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow \
    --ingress

# Rule 120: Allow ephemeral ports (return traffic)
aws ec2 create-network-acl-entry \
    --network-acl-id acl-xxxxx \
    --rule-number 120 \
    --protocol tcp \
    --port-range From=1024,To=65535 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow \
    --ingress

# Rule 130: Allow SSH from corporate network
aws ec2 create-network-acl-entry \
    --network-acl-id acl-xxxxx \
    --rule-number 130 \
    --protocol tcp \
    --port-range From=22,To=22 \
    --cidr-block 203.0.113.0/24 \
    --rule-action allow \
    --ingress

# Outbound Rules
# Rule 100: Allow all outbound
aws ec2 create-network-acl-entry \
    --network-acl-id acl-xxxxx \
    --rule-number 100 \
    --protocol -1 \
    --cidr-block 0.0.0.0/0 \
    --rule-action allow \
    --egress
```

> **⚠️ Важно:** NACL stateless — нужно явно разрешать и входящий, и исходящий трафик, включая ephemeral ports (1024-65535) для return traffic.

---

## 4. VPC Endpoints

**VPC Endpoint** позволяет приватно подключаться к AWS сервисам без выхода в публичный интернет.

### 4.1 Gateway Endpoints

Для S3 и DynamoDB — бесплатно, через Route Table.

```bash
# Создание Gateway Endpoint для S3
aws ec2 create-vpc-endpoint \
    --vpc-id vpc-xxxxx \
    --service-name com.amazonaws.us-east-1.s3 \
    --route-table-ids rtb-private-1a rtb-private-1b

# Результат: в Route Table появится маршрут:
# pl-xxxxx (S3 prefix list) → vpce-xxxxx
```

### 4.2 Interface Endpoints

Для большинства AWS сервисов — создаёт ENI в вашей подсети.

```bash
# Создание Interface Endpoint для Secrets Manager
aws ec2 create-vpc-endpoint \
    --vpc-id vpc-xxxxx \
    --vpc-endpoint-type Interface \
    --service-name com.amazonaws.us-east-1.secretsmanager \
    --subnet-ids subnet-private-1a subnet-private-1b \
    --security-group-ids sg-endpoint

# Стоимость: ~$0.01/час/AZ + $0.01/GB processed
```

**Сравнение типов endpoints:**

```python
vpc_endpoint_types = {
    "Gateway Endpoint": {
        "services": ["S3", "DynamoDB"],
        "cost": "Free",
        "implementation": "Route table entry",
        "dns": "Uses public DNS names",
        "security": "VPC Endpoint Policy"
    },
    "Interface Endpoint": {
        "services": ["Secrets Manager", "SSM", "CloudWatch", "SNS", "SQS", "etc."],
        "cost": "$0.01/hour/AZ + $0.01/GB",
        "implementation": "ENI with private IP in subnet",
        "dns": "Private DNS (optional)",
        "security": "Security Groups + VPC Endpoint Policy"
    }
}

# Без VPC Endpoint: 
#   EC2 (private) → NAT Gateway → Internet → S3
#   Проблемы: стоимость NAT, трафик через интернет
#
# С Gateway Endpoint:
#   EC2 (private) → VPC Endpoint → S3
#   Преимущества: бесплатно, не покидает AWS network
```

---

## 5. VPC Peering и Transit Gateway

### 5.1 VPC Peering

**VPC Peering** — соединение между двумя VPC для маршрутизации трафика через приватные IP.

```
┌────────────────────────────────────────────────────────────────────────┐
│                          VPC Peering                                    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│    VPC A (Production)              VPC B (Development)                 │
│    10.0.0.0/16                     10.1.0.0/16                        │
│    ┌─────────────────┐             ┌─────────────────┐                │
│    │                 │             │                 │                │
│    │  ┌───────────┐  │    pcx     │  ┌───────────┐  │                │
│    │  │  Web App  │◄─┼────────────┼─►│  Dev App  │  │                │
│    │  │ 10.0.1.10 │  │  -xxxxx    │  │ 10.1.1.10 │  │                │
│    │  └───────────┘  │             │  └───────────┘  │                │
│    │                 │             │                 │                │
│    └─────────────────┘             └─────────────────┘                │
│                                                                         │
│    Route Table A:                  Route Table B:                      │
│    10.1.0.0/16 → pcx-xxxxx        10.0.0.0/16 → pcx-xxxxx            │
│                                                                         │
│    ⚠️ VPC Peering is NOT transitive:                                   │
│    A ↔ B и B ↔ C не означает A ↔ C                                    │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

```bash
# Создание VPC Peering
aws ec2 create-vpc-peering-connection \
    --vpc-id vpc-prod \
    --peer-vpc-id vpc-dev \
    --peer-region us-east-1

# Принятие peering request (в другом аккаунте или VPC)
aws ec2 accept-vpc-peering-connection \
    --vpc-peering-connection-id pcx-xxxxx

# Добавление маршрутов в обе стороны
aws ec2 create-route \
    --route-table-id rtb-prod \
    --destination-cidr-block 10.1.0.0/16 \
    --vpc-peering-connection-id pcx-xxxxx

aws ec2 create-route \
    --route-table-id rtb-dev \
    --destination-cidr-block 10.0.0.0/16 \
    --vpc-peering-connection-id pcx-xxxxx
```

### 5.2 Transit Gateway

**Transit Gateway** — региональный hub для соединения множества VPC и on-premise сетей.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Transit Gateway                                  │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                      ┌─────────────────────┐                           │
│                      │   Transit Gateway   │                           │
│                      │     (tgw-xxxxx)     │                           │
│                      └──────────┬──────────┘                           │
│                                 │                                       │
│         ┌───────────────────────┼───────────────────────┐              │
│         │                       │                       │              │
│         ▼                       ▼                       ▼              │
│   ┌──────────┐            ┌──────────┐            ┌──────────┐        │
│   │  VPC A   │            │  VPC B   │            │  VPC C   │        │
│   │  Prod    │            │   Dev    │            │  Shared  │        │
│   │10.0.0/16 │            │10.1.0/16 │            │10.2.0/16 │        │
│   └──────────┘            └──────────┘            └──────────┘        │
│         │                                               │              │
│         │                       ┌───────────────────────┘              │
│         │                       │                                       │
│         ▼                       ▼                                       │
│   ┌────────────────────────────────────────┐                          │
│   │     VPN / Direct Connect               │                          │
│   │     to On-Premises                     │                          │
│   └────────────────────────────────────────┘                          │
│                                                                         │
│   Transit Gateway: $0.05/hour + $0.02/GB                               │
│   Advantages: hub-and-spoke, transitive routing, centralized          │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

**Когда использовать что:**

| Сценарий | Решение |
|----------|---------|
| 2 VPC | VPC Peering (бесплатно) |
| 3+ VPC | Transit Gateway |
| Нужен transitive routing | Transit Gateway |
| Cross-region | VPC Peering или Transit Gateway Peering |
| On-premise + multiple VPCs | Transit Gateway + VPN/Direct Connect |

---

## 6. VPC Flow Logs

**VPC Flow Logs** — мониторинг сетевого трафика на уровне VPC, subnet, или ENI.

```bash
# Создание Flow Log для всего VPC
aws ec2 create-flow-logs \
    --resource-type VPC \
    --resource-ids vpc-xxxxx \
    --traffic-type ALL \
    --log-destination-type cloud-watch-logs \
    --log-group-name /aws/vpc/flowlogs \
    --deliver-logs-permission-arn arn:aws:iam::123456789012:role/flowlogsRole

# Формат записи Flow Log:
# version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
```

**Пример анализа Flow Logs:**

```python
# Пример записи Flow Log
flow_log_record = """
2 123456789012 eni-abc123 10.0.1.10 10.0.2.20 443 49152 6 25 20000 1620140761 1620140821 ACCEPT OK
"""

# Разбор записи
fields = {
    "version": 2,
    "account_id": "123456789012",
    "interface_id": "eni-abc123",
    "src_addr": "10.0.1.10",
    "dst_addr": "10.0.2.20",
    "src_port": 443,
    "dst_port": 49152,
    "protocol": 6,        # 6 = TCP
    "packets": 25,
    "bytes": 20000,
    "start": 1620140761,  # Unix timestamp
    "end": 1620140821,
    "action": "ACCEPT",   # or REJECT
    "log_status": "OK"
}

# Полезные запросы в CloudWatch Logs Insights:
queries = {
    "rejected_traffic": """
        fields @timestamp, srcAddr, dstAddr, srcPort, dstPort
        | filter action = "REJECT"
        | sort @timestamp desc
        | limit 100
    """,
    "top_talkers": """
        fields srcAddr, dstAddr
        | stats sum(bytes) as total_bytes by srcAddr, dstAddr
        | sort total_bytes desc
        | limit 10
    """
}
```

---

## 7. DNS в VPC

### 7.1 Amazon DNS

```python
# DNS settings в VPC
vpc_dns_settings = {
    "enableDnsSupport": True,    # Включает Amazon DNS (резолвер на .2)
    "enableDnsHostnames": True,  # Присваивает public DNS имена EC2 с public IP
}

# Amazon DNS резолвер: 
# VPC CIDR base + 2
# Для 10.0.0.0/16 → 10.0.0.2

# Резолвит:
# - Публичные домены (google.com)
# - AWS private hostnames (ip-10-0-1-10.ec2.internal)
# - Route 53 Private Hosted Zones
```

### 7.2 Route 53 Private Hosted Zones

```bash
# Создание Private Hosted Zone
aws route53 create-hosted-zone \
    --name internal.mycompany.com \
    --vpc VPCRegion=us-east-1,VPCId=vpc-xxxxx \
    --caller-reference $(date +%s) \
    --hosted-zone-config PrivateZone=true

# Добавление записи
aws route53 change-resource-record-sets \
    --hosted-zone-id Z123456789 \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "db.internal.mycompany.com",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [{"Value": "10.0.21.10"}]
            }
        }]
    }'
```

---

## 8. Best Practices

```python
vpc_best_practices = {
    "planning": [
        "Планируйте CIDR заранее — изменить нельзя",
        "Избегайте overlap с on-premise сетями",
        "Резервируйте IP пространство для роста",
        "Документируйте IP allocation"
    ],
    "architecture": [
        "Используйте минимум 2 AZ для HA",
        "Разделяйте public/private/data subnets",
        "NAT Gateway в каждой AZ для HA",
        "Используйте VPC Endpoints для AWS сервисов"
    ],
    "security": [
        "Security Groups > NACLs (более гибкие)",
        "Reference SG вместо IP где возможно",
        "Минимизируйте разрешения (least privilege)",
        "Включайте VPC Flow Logs для аудита"
    ],
    "connectivity": [
        "VPC Peering для 2 VPC",
        "Transit Gateway для 3+ VPC",
        "Direct Connect для стабильной связи с on-premise",
        "VPN как backup для Direct Connect"
    ]
}
```

---

## 💡 Key Takeaways

- **VPC** — изолированная виртуальная сеть, ваш дата-центр в AWS
- **Public subnet** — имеет route к Internet Gateway, ресурсы получают public IP
- **Private subnet** — выход в интернет только через NAT Gateway
- **Security Groups** — stateful firewall на уровне instance, только allow rules
- **Network ACLs** — stateless firewall на уровне subnet, allow/deny rules
- **VPC Endpoints** — приватный доступ к AWS сервисам без интернета
- **Transit Gateway** — hub для соединения множества VPC и on-premise

---

## 📚 Additional Resources

**AWS Documentation:**
- [VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/)
- [Security Group Rules Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html)
- [VPC Endpoints Documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/)

**Tools:**
- [VPC CIDR Calculator](https://www.ipaddressguide.com/cidr)
- [AWS VPC Designer](https://console.aws.amazon.com/vpc/home#vpcs)

---

## 🚀 Next Steps

**Следующие модули:**
- [08_RDS](../08_RDS/) — Реляционные базы данных в облаке
- [09_DynamoDB](../09_DynamoDB/) — NoSQL база данных DynamoDB

**Практика:**
1. Создайте VPC с 3-tier architecture через Console
2. Настройте Security Groups chain: ALB → Web → DB
3. Создайте Gateway Endpoint для S3 в private subnet
4. Включите VPC Flow Logs и проанализируйте трафик
5. Настройте VPC Peering между двумя VPC

---
