# Архитектура облаков: Регионы, Availability Zones, Edge

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать базовые концепции облачных вычислений
- Знать модели сервисов (IaaS, PaaS, SaaS)
- Иметь представление о сетях и латентности

**Recommended prior modules:**
- [Введение в облака](../01_Intro/)
- [Модели сервисов](../02_ServiceModels/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить глобальную инфраструктуру AWS (регионы, AZ, Edge)
- Выбирать правильный регион для развёртывания
- Проектировать отказоустойчивые архитектуры с использованием Multiple AZ
- Понимать роль Edge Locations и CDN

---

## 1. Глобальная инфраструктура AWS

### 1.1 Обзор

AWS имеет самую обширную глобальную инфраструктуру среди облачных провайдеров:

```
┌────────────────────────────────────────────────────────────────────┐
│                   AWS Global Infrastructure (2024)                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   🌍 33 Regions                                                    │
│      └── Географически изолированные локации                       │
│      └── Каждый регион независим                                   │
│                                                                     │
│   🏢 105+ Availability Zones                                       │
│      └── Физически изолированные дата-центры внутри региона       │
│      └── 3+ AZ в большинстве регионов                             │
│                                                                     │
│   📡 600+ Edge Locations / PoPs                                    │
│      └── CloudFront CDN                                            │
│      └── Route 53 DNS                                              │
│      └── AWS Global Accelerator                                    │
│                                                                     │
│   🏠 29 Local Zones                                                │
│      └── Расширение регионов ближе к пользователям                │
│                                                                     │
│   📦 17 Wavelength Zones                                           │
│      └── 5G edge computing                                         │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 Иерархия инфраструктуры

```
┌─────────────────────────────────────────────────────────────────┐
│                    Infrastructure Hierarchy                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  AWS Global                                                      │
│  │                                                               │
│  ├── Region (us-east-1)                                         │
│  │   │                                                           │
│  │   ├── Availability Zone (us-east-1a)                         │
│  │   │   └── Data Center(s)                                     │
│  │   │       └── Racks                                          │
│  │   │           └── Servers                                    │
│  │   │                                                           │
│  │   ├── Availability Zone (us-east-1b)                         │
│  │   │   └── Data Center(s)                                     │
│  │   │                                                           │
│  │   ├── Availability Zone (us-east-1c)                         │
│  │   │   └── Data Center(s)                                     │
│  │   │                                                           │
│  │   └── ... (up to 6 AZs)                                      │
│  │                                                               │
│  ├── Region (eu-west-1)                                         │
│  │   ├── AZ (eu-west-1a)                                        │
│  │   ├── AZ (eu-west-1b)                                        │
│  │   └── AZ (eu-west-1c)                                        │
│  │                                                               │
│  └── ... (33 regions)                                           │
│                                                                  │
│  Edge Network (отдельно от регионов)                            │
│  │                                                               │
│  ├── Edge Locations (CloudFront PoPs)                           │
│  ├── Regional Edge Caches                                       │
│  └── Local Zones                                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Регионы (Regions)

### 2.1 Что такое регион

**Region** — это географически изолированная локация, состоящая из нескольких Availability Zones. Каждый регион полностью независим от других.

```python
import boto3

# Получение списка всех регионов
ec2 = boto3.client('ec2', region_name='us-east-1')
regions = ec2.describe_regions()

# Фильтруем включённые регионы
enabled_regions = [
    r['RegionName'] for r in regions['Regions']
    if r['OptInStatus'] in ['opt-in-not-required', 'opted-in']
]

print(f"Количество регионов: {len(enabled_regions)}")
print("\nПримеры регионов:")
for region in enabled_regions[:10]:
    print(f"  • {region}")
```

**Output:**
```
Количество регионов: 27
Примеры регионов:
  • us-east-1
  • us-east-2
  • us-west-1
  • us-west-2
  • eu-west-1
  • eu-west-2
  • eu-central-1
  • ap-southeast-1
  • ap-northeast-1
  • sa-east-1
```

### 2.2 Карта регионов AWS

```
┌────────────────────────────────────────────────────────────────────┐
│                       AWS Regions Map                               │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│    NORTH AMERICA                  EUROPE                           │
│    • us-east-1 (N. Virginia)      • eu-west-1 (Ireland)            │
│    • us-east-2 (Ohio)             • eu-west-2 (London)             │
│    • us-west-1 (N. California)    • eu-west-3 (Paris)              │
│    • us-west-2 (Oregon)           • eu-central-1 (Frankfurt)       │
│    • ca-central-1 (Canada)        • eu-central-2 (Zurich)          │
│    • ca-west-1 (Calgary)          • eu-north-1 (Stockholm)         │
│                                   • eu-south-1 (Milan)             │
│    SOUTH AMERICA                  • eu-south-2 (Spain)             │
│    • sa-east-1 (São Paulo)                                         │
│                                                                     │
│    ASIA PACIFIC                   MIDDLE EAST & AFRICA             │
│    • ap-east-1 (Hong Kong)        • me-south-1 (Bahrain)           │
│    • ap-south-1 (Mumbai)          • me-central-1 (UAE)             │
│    • ap-south-2 (Hyderabad)       • af-south-1 (Cape Town)         │
│    • ap-southeast-1 (Singapore)   • il-central-1 (Tel Aviv)        │
│    • ap-southeast-2 (Sydney)                                       │
│    • ap-southeast-3 (Jakarta)     SPECIAL                          │
│    • ap-southeast-4 (Melbourne)   • us-gov-east-1 (GovCloud)       │
│    • ap-northeast-1 (Tokyo)       • us-gov-west-1 (GovCloud)       │
│    • ap-northeast-2 (Seoul)       • cn-north-1 (Beijing)           │
│    • ap-northeast-3 (Osaka)       • cn-northwest-1 (Ningxia)       │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 2.3 Выбор региона

**Факторы выбора:**

```python
region_selection_criteria = {
    "latency": {
        "description": "Близость к пользователям",
        "example": "Пользователи в Европе → eu-west-1 или eu-central-1",
        "priority": "HIGH"
    },
    "compliance": {
        "description": "Законодательные требования к хранению данных",
        "example": "GDPR → данные в EU регионах, ФЗ-152 → нет AWS в России",
        "priority": "HIGH"
    },
    "service_availability": {
        "description": "Не все сервисы доступны во всех регионах",
        "example": "Новые сервисы появляются сначала в us-east-1",
        "priority": "MEDIUM"
    },
    "pricing": {
        "description": "Цены различаются между регионами",
        "example": "us-east-1 обычно дешевле, São Paulo дороже",
        "priority": "MEDIUM"
    },
    "disaster_recovery": {
        "description": "Географическое распределение для DR",
        "example": "Primary: eu-west-1, DR: eu-central-1",
        "priority": "MEDIUM"
    }
}

print("Критерии выбора региона:\n")
for criterion, details in region_selection_criteria.items():
    print(f"[{details['priority']}] {criterion.upper()}")
    print(f"    {details['description']}")
    print(f"    Example: {details['example']}\n")
```

**Output:**
```
Критерии выбора региона:

[HIGH] LATENCY
    Близость к пользователям
    Example: Пользователи в Европе → eu-west-1 или eu-central-1

[HIGH] COMPLIANCE
    Законодательные требования к хранению данных
    Example: GDPR → данные в EU регионах, ФЗ-152 → нет AWS в России

[MEDIUM] SERVICE_AVAILABILITY
    Не все сервисы доступны во всех регионах
    Example: Новые сервисы появляются сначала в us-east-1

[MEDIUM] PRICING
    Цены различаются между регионами
    Example: us-east-1 обычно дешевле, São Paulo дороже

[MEDIUM] DISASTER_RECOVERY
    Географическое распределение для DR
    Example: Primary: eu-west-1, DR: eu-central-1
```

### 2.4 Сравнение цен по регионам

```python
# Примерные цены EC2 t3.medium (Linux) по регионам
ec2_pricing_t3_medium = {
    "us-east-1": 0.0416,      # N. Virginia (базовая цена)
    "us-east-2": 0.0416,      # Ohio
    "us-west-2": 0.0416,      # Oregon
    "eu-west-1": 0.0456,      # Ireland (+10%)
    "eu-central-1": 0.0480,   # Frankfurt (+15%)
    "ap-northeast-1": 0.0544, # Tokyo (+31%)
    "ap-southeast-1": 0.0528, # Singapore (+27%)
    "sa-east-1": 0.0680,      # São Paulo (+63%)
    "ap-south-1": 0.0416,     # Mumbai (дешёвый)
}

base_price = ec2_pricing_t3_medium["us-east-1"]

print("EC2 t3.medium hourly pricing by region:\n")
for region, price in sorted(ec2_pricing_t3_medium.items(), key=lambda x: x[1]):
    diff = ((price - base_price) / base_price) * 100
    sign = "+" if diff > 0 else ""
    print(f"  {region:18} ${price:.4f}/hr  ({sign}{diff:.0f}%)")
```

**Output:**
```
EC2 t3.medium hourly pricing by region:

  us-east-1          $0.0416/hr  (+0%)
  us-east-2          $0.0416/hr  (+0%)
  us-west-2          $0.0416/hr  (+0%)
  ap-south-1         $0.0416/hr  (+0%)
  eu-west-1          $0.0456/hr  (+10%)
  eu-central-1       $0.0480/hr  (+15%)
  ap-southeast-1     $0.0528/hr  (+27%)
  ap-northeast-1     $0.0544/hr  (+31%)
  sa-east-1          $0.0680/hr  (+63%)
```

---

## 3. Availability Zones (AZ)

### 3.1 Что такое Availability Zone

**Availability Zone** — это один или несколько физически изолированных дата-центров внутри региона с независимым питанием, охлаждением и сетью.

```
┌────────────────────────────────────────────────────────────────────┐
│                    Availability Zone Design                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Region: us-east-1 (N. Virginia)                                   │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                                                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │  │
│  │  │ AZ: 1a      │  │ AZ: 1b      │  │ AZ: 1c      │  ...    │  │
│  │  │             │  │             │  │             │         │  │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────┐ │         │  │
│  │  │ │  DC 1   │ │  │ │  DC 1   │ │  │ │  DC 1   │ │         │  │
│  │  │ └─────────┘ │  │ └─────────┘ │  │ └─────────┘ │         │  │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────┐ │         │  │
│  │  │ │  DC 2   │ │  │ │  DC 2   │ │  │ │  DC 2   │ │         │  │
│  │  │ └─────────┘ │  │ └─────────┘ │  │ └─────────┘ │         │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘         │  │
│  │         │                │                │                 │  │
│  │         └────────────────┼────────────────┘                 │  │
│  │                          │                                  │  │
│  │              High-bandwidth, low-latency                    │  │
│  │              private fiber connections                      │  │
│  │              (< 2ms latency between AZs)                   │  │
│  │                                                              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Физическая изоляция между AZ:                                    │
│  • Отдельные здания (разные улицы/районы)                        │
│  • Независимое электропитание                                     │
│  • Независимое охлаждение                                         │
│  • Отдельные сетевые подключения                                  │
│  • Расстояние: несколько километров до ~100 км                   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 AZ Naming

```python
# AZ названия уникальны для каждого аккаунта!
# us-east-1a в вашем аккаунте может быть физически другой AZ,
# чем us-east-1a в другом аккаунте

import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
azs = ec2.describe_availability_zones()

print("Availability Zones in us-east-1:\n")
for az in azs['AvailabilityZones']:
    print(f"  Name: {az['ZoneName']}")
    print(f"  Zone ID: {az['ZoneId']}")  # Уникальный ID (одинаков везде)
    print(f"  State: {az['State']}")
    print()
```

**Output:**
```
Availability Zones in us-east-1:

  Name: us-east-1a
  Zone ID: use1-az1
  State: available

  Name: us-east-1b
  Zone ID: use1-az2
  State: available

  Name: us-east-1c
  Zone ID: use1-az4
  State: available

  Name: us-east-1d
  Zone ID: use1-az6
  State: available

  Name: us-east-1e
  Zone ID: use1-az3
  State: available

  Name: us-east-1f
  Zone ID: use1-az5
  State: available
```

> **💡 Pro Tip:**  
> При координации между аккаунтами используйте Zone ID (use1-az1), а не Zone Name (us-east-1a), так как маппинг может отличаться.

### 3.3 Multi-AZ архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│               Multi-AZ High Availability Architecture               │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                        ┌─────────────────┐                         │
│                        │   Route 53      │                         │
│                        │   (DNS)         │                         │
│                        └────────┬────────┘                         │
│                                 │                                   │
│                        ┌────────▼────────┐                         │
│                        │ Application     │                         │
│                        │ Load Balancer   │                         │
│                        │ (cross-AZ)      │                         │
│                        └────────┬────────┘                         │
│                                 │                                   │
│            ┌────────────────────┼────────────────────┐             │
│            │                    │                    │             │
│  ┌─────────▼─────────┐ ┌───────▼────────┐ ┌────────▼────────┐    │
│  │   AZ: us-east-1a  │ │  AZ: us-east-1b│ │  AZ: us-east-1c │    │
│  │                   │ │                │ │                 │    │
│  │  ┌─────────────┐  │ │ ┌────────────┐ │ │ ┌─────────────┐ │    │
│  │  │   EC2 ASG   │  │ │ │  EC2 ASG   │ │ │ │   EC2 ASG   │ │    │
│  │  │  (2 inst)   │  │ │ │  (2 inst)  │ │ │ │  (2 inst)   │ │    │
│  │  └─────────────┘  │ │ └────────────┘ │ │ └─────────────┘ │    │
│  │                   │ │                │ │                 │    │
│  │  ┌─────────────┐  │ │ ┌────────────┐ │ │                 │    │
│  │  │ RDS Primary │◄─┼─┼─│RDS Standby │ │ │                 │    │
│  │  │  (writer)   │  │ │ │  (failover)│ │ │                 │    │
│  │  └─────────────┘  │ │ └────────────┘ │ │                 │    │
│  │                   │ │                │ │                 │    │
│  │  ┌─────────────┐  │ │ ┌────────────┐ │ │ ┌─────────────┐ │    │
│  │  │ ElastiCache │  │ │ │ElastiCache │ │ │ │ ElastiCache │ │    │
│  │  │   (node)    │  │ │ │  (node)    │ │ │ │   (node)    │ │    │
│  │  └─────────────┘  │ │ └────────────┘ │ │ └─────────────┘ │    │
│  │                   │ │                │ │                 │    │
│  └───────────────────┘ └────────────────┘ └─────────────────┘    │
│                                                                     │
│  Benefits:                                                         │
│  • Устойчивость к отказу целого AZ                                │
│  • Автоматический failover                                         │
│  • Low latency между AZ (< 2ms)                                   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.4 Latency между AZ

```python
# Типичная латентность между компонентами

latency_measurements = {
    "same_az": {
        "description": "EC2 to EC2 в одном AZ",
        "latency_ms": "< 0.5",
        "use_case": "Низкая латентность критична"
    },
    "cross_az": {
        "description": "EC2 to EC2 в разных AZ",
        "latency_ms": "1-2",
        "use_case": "High availability"
    },
    "cross_region": {
        "description": "EC2 to EC2 в разных регионах",
        "latency_ms": "50-200+",
        "use_case": "Disaster recovery"
    }
}

print("Network Latency in AWS:\n")
for scenario, data in latency_measurements.items():
    print(f"{scenario.upper()}")
    print(f"  {data['description']}")
    print(f"  Latency: ~{data['latency_ms']} ms")
    print(f"  Use case: {data['use_case']}\n")
```

**Output:**
```
Network Latency in AWS:

SAME_AZ
  EC2 to EC2 в одном AZ
  Latency: ~< 0.5 ms
  Use case: Низкая латентность критична

CROSS_AZ
  EC2 to EC2 в разных AZ
  Latency: ~1-2 ms
  Use case: High availability

CROSS_REGION
  EC2 to EC2 в разных регионах
  Latency: ~50-200+ ms
  Use case: Disaster recovery
```

---

## 4. Edge Locations и CloudFront

### 4.1 Что такое Edge Location

**Edge Location** — это точка присутствия (Point of Presence, PoP) для сервисов доставки контента. AWS имеет 600+ Edge Locations по всему миру.

```
┌────────────────────────────────────────────────────────────────────┐
│                    Edge Network Architecture                        │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  User Request Flow:                                                │
│                                                                     │
│  👤 User (Moscow)                                                  │
│    │                                                                │
│    │ 1. DNS lookup (Route 53)                                      │
│    ▼                                                                │
│  ┌─────────────────────┐                                           │
│  │   Edge Location     │  ◄── Closest PoP (Moscow)                 │
│  │   (CloudFront)      │                                           │
│  └──────────┬──────────┘                                           │
│             │                                                       │
│             │ Cache HIT? ──► Return cached content (fast!)         │
│             │                                                       │
│             │ Cache MISS ▼                                         │
│  ┌──────────▼──────────┐                                           │
│  │  Regional Edge      │  ◄── Larger cache, fewer locations        │
│  │  Cache              │                                           │
│  └──────────┬──────────┘                                           │
│             │                                                       │
│             │ Cache MISS ▼                                         │
│  ┌──────────▼──────────┐                                           │
│  │   Origin Server     │  ◄── S3, EC2, ALB, etc.                  │
│  │   (eu-west-1)       │      (может быть далеко от пользователя) │
│  └─────────────────────┘                                           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 4.2 Сервисы на Edge

```python
edge_services = {
    "CloudFront": {
        "type": "CDN",
        "description": "Content Delivery Network",
        "use_cases": ["Static content", "Dynamic content", "Video streaming"],
        "edge_locations": "600+"
    },
    "Route 53": {
        "type": "DNS",
        "description": "Managed DNS service",
        "use_cases": ["DNS resolution", "Health checks", "Traffic routing"],
        "edge_locations": "All edge locations"
    },
    "AWS WAF": {
        "type": "Security",
        "description": "Web Application Firewall",
        "use_cases": ["DDoS protection", "SQL injection", "XSS prevention"],
        "edge_locations": "With CloudFront"
    },
    "Lambda@Edge": {
        "type": "Compute",
        "description": "Run code at edge locations",
        "use_cases": ["A/B testing", "Auth", "URL rewriting"],
        "edge_locations": "CloudFront edge locations"
    },
    "Global Accelerator": {
        "type": "Networking",
        "description": "Improve availability and performance",
        "use_cases": ["Gaming", "IoT", "VoIP"],
        "edge_locations": "AWS edge network"
    }
}

print("AWS Edge Services:\n")
for service, details in edge_services.items():
    print(f"📡 {service} ({details['type']})")
    print(f"   {details['description']}")
    print(f"   Use cases: {', '.join(details['use_cases'][:2])}")
    print()
```

**Output:**
```
AWS Edge Services:

📡 CloudFront (CDN)
   Content Delivery Network
   Use cases: Static content, Dynamic content

📡 Route 53 (DNS)
   Managed DNS service
   Use cases: DNS resolution, Health checks

📡 AWS WAF (Security)
   Web Application Firewall
   Use cases: DDoS protection, SQL injection

📡 Lambda@Edge (Compute)
   Run code at edge locations
   Use cases: A/B testing, Auth

📡 Global Accelerator (Networking)
   Improve availability and performance
   Use cases: Gaming, IoT
```

### 4.3 CloudFront Distribution

```bash
# Создание CloudFront distribution через CLI
aws cloudfront create-distribution \
    --distribution-config '{
        "CallerReference": "my-distribution-2024",
        "Origins": {
            "Quantity": 1,
            "Items": [
                {
                    "Id": "myS3Origin",
                    "DomainName": "my-bucket.s3.amazonaws.com",
                    "S3OriginConfig": {
                        "OriginAccessIdentity": ""
                    }
                }
            ]
        },
        "DefaultCacheBehavior": {
            "TargetOriginId": "myS3Origin",
            "ViewerProtocolPolicy": "redirect-to-https",
            "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
            "Compress": true
        },
        "Enabled": true,
        "Comment": "My CloudFront Distribution"
    }'
```

---

## 5. Local Zones и Wavelength

### 5.1 Local Zones

**Local Zone** — расширение региона AWS, расположенное ближе к конечным пользователям в крупных городах.

```
┌────────────────────────────────────────────────────────────────────┐
│                       Local Zones                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Сценарий: Gaming server для пользователей в Los Angeles          │
│                                                                     │
│  Без Local Zone:                                                   │
│  User (LA) ──► us-west-2 (Oregon) ──► ~30-50ms latency            │
│                                                                     │
│  С Local Zone:                                                     │
│  User (LA) ──► us-west-2-lax-1a ──► ~5-10ms latency               │
│                          │                                          │
│                          └── Local Zone в Los Angeles              │
│                                                                     │
│  Available Local Zones (примеры):                                  │
│  • us-west-2-lax-1a (Los Angeles)                                 │
│  • us-east-1-bos-1a (Boston)                                      │
│  • us-east-1-chi-1a (Chicago)                                     │
│  • us-east-1-mia-1a (Miami)                                       │
│  • eu-central-1-ham-1a (Hamburg)                                  │
│  • ap-northeast-1-tpe-1a (Taipei)                                 │
│                                                                     │
│  Сервисы в Local Zones:                                           │
│  • EC2 (limited instance types)                                    │
│  • EBS                                                             │
│  • VPC (subnets)                                                   │
│  • Application Load Balancer                                       │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 5.2 Wavelength Zones

**Wavelength Zone** — инфраструктура AWS внутри 5G сетей операторов для ultra-low latency приложений.

```python
wavelength_use_cases = {
    "mobile_gaming": {
        "latency_requirement": "< 10ms",
        "description": "Cloud gaming на 5G устройствах"
    },
    "augmented_reality": {
        "latency_requirement": "< 20ms",
        "description": "AR/VR приложения с edge processing"
    },
    "connected_vehicles": {
        "latency_requirement": "< 10ms",
        "description": "Автономные автомобили, V2X"
    },
    "smart_factories": {
        "latency_requirement": "< 5ms",
        "description": "Industrial IoT, robotics"
    }
}

print("Wavelength Zone Use Cases:\n")
for use_case, details in wavelength_use_cases.items():
    print(f"📱 {use_case.replace('_', ' ').title()}")
    print(f"   Latency: {details['latency_requirement']}")
    print(f"   {details['description']}\n")
```

**Output:**
```
Wavelength Zone Use Cases:

📱 Mobile Gaming
   Latency: < 10ms
   Cloud gaming на 5G устройствах

📱 Augmented Reality
   Latency: < 20ms
   AR/VR приложения с edge processing

📱 Connected Vehicles
   Latency: < 10ms
   Автономные автомобили, V2X

📱 Smart Factories
   Latency: < 5ms
   Industrial IoT, robotics
```

---

## 6. Global Services vs Regional Services

### 6.1 Классификация сервисов

```python
service_scope = {
    "global": {
        "description": "Работают глобально, не привязаны к региону",
        "services": [
            "IAM (Identity and Access Management)",
            "Route 53 (DNS)",
            "CloudFront (CDN)",
            "WAF (when used with CloudFront)",
            "Global Accelerator",
            "Organizations",
            "Artifact"
        ]
    },
    "regional": {
        "description": "Работают в конкретном регионе",
        "services": [
            "EC2",
            "RDS",
            "Lambda",
            "S3 (buckets региональные)",
            "VPC",
            "ECS/EKS",
            "DynamoDB",
            "SQS/SNS",
            "API Gateway"
        ]
    },
    "az_specific": {
        "description": "Привязаны к конкретной Availability Zone",
        "services": [
            "EC2 instances",
            "EBS volumes",
            "Subnets",
            "RDS instances (single-AZ)"
        ]
    }
}

for scope, data in service_scope.items():
    print(f"\n{scope.upper()} SERVICES")
    print(f"{data['description']}")
    print("-" * 40)
    for svc in data['services'][:5]:
        print(f"  • {svc}")
    if len(data['services']) > 5:
        print(f"  ... and {len(data['services']) - 5} more")
```

**Output:**
```
GLOBAL SERVICES
Работают глобально, не привязаны к региону
----------------------------------------
  • IAM (Identity and Access Management)
  • Route 53 (DNS)
  • CloudFront (CDN)
  • WAF (when used with CloudFront)
  • Global Accelerator

REGIONAL SERVICES
Работают в конкретном регионе
----------------------------------------
  • EC2
  • RDS
  • Lambda
  • S3 (buckets региональные)
  • VPC
  ... and 4 more

AZ_SPECIFIC SERVICES
Привязаны к конкретной Availability Zone
----------------------------------------
  • EC2 instances
  • EBS volumes
  • Subnets
  • RDS instances (single-AZ)
```

### 6.2 ARN и регионы

```python
# ARN (Amazon Resource Name) содержит информацию о регионе

arn_examples = {
    "EC2 Instance": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
    "S3 Bucket": "arn:aws:s3:::my-bucket",  # Без региона (глобальное имя)
    "Lambda": "arn:aws:lambda:eu-west-1:123456789012:function:my-function",
    "IAM Role": "arn:aws:iam::123456789012:role/MyRole",  # Без региона (глобальный)
    "DynamoDB Table": "arn:aws:dynamodb:ap-northeast-1:123456789012:table/MyTable"
}

print("ARN Format: arn:aws:service:region:account-id:resource\n")

for resource, arn in arn_examples.items():
    parts = arn.split(":")
    region = parts[3] if parts[3] else "GLOBAL"
    print(f"{resource}:")
    print(f"  ARN: {arn}")
    print(f"  Region: {region}\n")
```

**Output:**
```
ARN Format: arn:aws:service:region:account-id:resource

EC2 Instance:
  ARN: arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0
  Region: us-east-1

S3 Bucket:
  ARN: arn:aws:s3:::my-bucket
  Region: GLOBAL

Lambda:
  ARN: arn:aws:lambda:eu-west-1:123456789012:function:my-function
  Region: eu-west-1

IAM Role:
  ARN: arn:aws:iam::123456789012:role/MyRole
  Region: GLOBAL

DynamoDB Table:
  ARN: arn:aws:dynamodb:ap-northeast-1:123456789012:table/MyTable
  Region: ap-northeast-1
```

---

## 7. Designing for High Availability

### 7.1 Уровни отказоустойчивости

```
┌────────────────────────────────────────────────────────────────────┐
│              Levels of High Availability                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Level 1: Single Instance (NO HA)                                  │
│  ─────────────────────────────────                                 │
│  • Один EC2 в одном AZ                                            │
│  • При отказе AZ — полный outage                                  │
│  • Availability: ~99.5%                                           │
│                                                                     │
│  Level 2: Multi-AZ (Regional HA)                                   │
│  ─────────────────────────────────                                 │
│  • Ресурсы в 2-3 AZ одного региона                               │
│  • Автоматический failover                                        │
│  • Availability: ~99.95%                                          │
│                                                                     │
│  Level 3: Multi-Region (Global HA)                                 │
│  ─────────────────────────────────                                 │
│  • Ресурсы в нескольких регионах                                 │
│  • Disaster Recovery                                               │
│  • Availability: ~99.99%+                                         │
│                                                                     │
│  Level 4: Multi-Cloud (Ultimate HA)                                │
│  ─────────────────────────────────                                 │
│  • Несколько облачных провайдеров                                 │
│  • Защита от outage целого провайдера                            │
│  • Complexity: VERY HIGH                                          │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 7.2 Multi-Region Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                Multi-Region Active-Passive                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                     ┌──────────────────┐                           │
│                     │    Route 53      │                           │
│                     │  (Failover DNS)  │                           │
│                     └────────┬─────────┘                           │
│                              │                                      │
│              ┌───────────────┴───────────────┐                     │
│              │                               │                      │
│              ▼                               ▼                      │
│  ┌─────────────────────┐       ┌─────────────────────┐            │
│  │  PRIMARY REGION     │       │  SECONDARY REGION   │            │
│  │  (eu-west-1)        │       │  (eu-central-1)     │            │
│  │                     │       │                     │            │
│  │  ┌───────────────┐  │       │  ┌───────────────┐  │            │
│  │  │     ALB       │  │       │  │     ALB       │  │            │
│  │  └───────┬───────┘  │       │  └───────┬───────┘  │            │
│  │          │          │       │          │          │            │
│  │  ┌───────▼───────┐  │       │  ┌───────▼───────┐  │            │
│  │  │  EC2 / ECS    │  │       │  │  EC2 / ECS    │  │            │
│  │  │  (active)     │  │       │  │  (standby)    │  │            │
│  │  └───────────────┘  │       │  └───────────────┘  │            │
│  │                     │       │                     │            │
│  │  ┌───────────────┐  │  ───► │  ┌───────────────┐  │            │
│  │  │ Aurora Global │  │ Repl  │  │ Aurora Global │  │            │
│  │  │   (writer)    │  │       │  │   (reader)    │  │            │
│  │  └───────────────┘  │       │  └───────────────┘  │            │
│  │                     │       │                     │            │
│  └─────────────────────┘       └─────────────────────┘            │
│                                                                     │
│  RTO: 1-5 minutes (зависит от автоматизации)                      │
│  RPO: ~1 second (Aurora Global Database async replication)        │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 7.3 RTO и RPO

```python
disaster_recovery_metrics = {
    "RTO": {
        "full_name": "Recovery Time Objective",
        "description": "Максимально допустимое время восстановления",
        "examples": {
            "critical_banking": "< 1 hour",
            "e_commerce": "< 4 hours",
            "internal_tools": "< 24 hours"
        }
    },
    "RPO": {
        "full_name": "Recovery Point Objective",
        "description": "Максимально допустимая потеря данных (в времени)",
        "examples": {
            "financial_transactions": "0 (no data loss)",
            "e_commerce_orders": "< 1 hour",
            "analytics": "< 24 hours"
        }
    }
}

print("Disaster Recovery Metrics:\n")
for metric, data in disaster_recovery_metrics.items():
    print(f"{metric} ({data['full_name']})")
    print(f"  {data['description']}")
    print("  Examples:")
    for use_case, value in data['examples'].items():
        print(f"    • {use_case.replace('_', ' ').title()}: {value}")
    print()
```

**Output:**
```
Disaster Recovery Metrics:

RTO (Recovery Time Objective)
  Максимально допустимое время восстановления
  Examples:
    • Critical Banking: < 1 hour
    • E Commerce: < 4 hours
    • Internal Tools: < 24 hours

RPO (Recovery Point Objective)
  Максимально допустимая потеря данных (в времени)
  Examples:
    • Financial Transactions: 0 (no data loss)
    • E Commerce Orders: < 1 hour
    • Analytics: < 24 hours
```

---

## 8. Common Pitfalls

### 8.1 Pitfall: Всё в одном AZ

❌ **Проблема:**
```python
# Все ресурсы в одном AZ для "простоты"
resources = {
    "ec2": "us-east-1a",
    "rds": "us-east-1a",
    "elasticache": "us-east-1a"
}
# При отказе us-east-1a — полный outage!
```

✅ **Решение:**
```python
# Распределение по AZ
resources = {
    "ec2": ["us-east-1a", "us-east-1b", "us-east-1c"],
    "rds": "Multi-AZ (automatic failover)",
    "elasticache": "Cluster mode (multiple nodes in multiple AZs)"
}
```

### 8.2 Pitfall: Hardcoded AZ names

❌ **Проблема:**
```python
# Hardcoded AZ в коде
availability_zone = "us-east-1a"  # Плохо!

# При деплое в другой аккаунт us-east-1a может быть другим физическим AZ
```

✅ **Решение:**
```python
import boto3

def get_available_azs(region: str) -> list:
    """Динамически получаем список доступных AZ"""
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_availability_zones(
        Filters=[{'Name': 'state', 'Values': ['available']}]
    )
    return [az['ZoneName'] for az in response['AvailabilityZones']]

# Terraform подход
# data "aws_availability_zones" "available" {
#   state = "available"
# }
```

### 8.3 Pitfall: Игнорирование cross-AZ traffic costs

❌ **Проблема:**
```python
# Не учитывается стоимость трафика между AZ
# Data transfer between AZs: $0.01/GB в каждую сторону

# При 10TB/месяц между AZ:
monthly_cross_az_traffic = 10 * 1024  # GB
cost_per_gb = 0.01 * 2  # оба направления
monthly_cost = monthly_cross_az_traffic * cost_per_gb
print(f"Cross-AZ traffic cost: ${monthly_cost}")  # $204.80!
```

✅ **Решение:**
```python
strategies = [
    "Размещать взаимодействующие компоненты в одном AZ когда возможно",
    "Использовать compression для уменьшения объёма данных",
    "Кэшировать данные локально (ElastiCache)",
    "Использовать VPC Endpoints для AWS сервисов"
]
```

---

## 9. Практический пример: выбор архитектуры

### 9.1 Сценарий

```python
scenario = {
    "application": "E-commerce website",
    "users": "Primarily in Europe",
    "requirements": {
        "availability": "99.95%",
        "rto": "1 hour",
        "rpo": "5 minutes",
        "compliance": "GDPR (data must stay in EU)"
    },
    "traffic_pattern": "Peaks during Black Friday (10x normal)"
}

print("Scenario Analysis:")
for key, value in scenario.items():
    print(f"  {key}: {value}")
```

**Output:**
```
Scenario Analysis:
  application: E-commerce website
  users: Primarily in Europe
  requirements: {'availability': '99.95%', 'rto': '1 hour', 'rpo': '5 minutes', 'compliance': 'GDPR (data must stay in EU)'}
  traffic_pattern: Peaks during Black Friday (10x normal)
```

### 9.2 Рекомендуемая архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│            Recommended Architecture: E-commerce                     │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Primary Region: eu-west-1 (Ireland)                               │
│  DR Region: eu-central-1 (Frankfurt)                               │
│                                                                     │
│  ┌────────────────────────────────────────────┐                    │
│  │ CloudFront (600+ Edge Locations)           │                    │
│  │ • Static assets caching                    │                    │
│  │ • WAF for DDoS protection                  │                    │
│  └────────────────────┬───────────────────────┘                    │
│                       │                                             │
│  ┌────────────────────▼───────────────────────┐                    │
│  │ Route 53 (Latency-based routing)           │                    │
│  │ • Health checks                             │                    │
│  │ • Automatic failover to DR                  │                    │
│  └────────────────────┬───────────────────────┘                    │
│                       │                                             │
│       ┌───────────────┴────────────────┐                           │
│       ▼                                ▼                           │
│  eu-west-1 (PRIMARY)            eu-central-1 (DR)                  │
│  ┌──────────────────┐          ┌──────────────────┐               │
│  │ ALB (Multi-AZ)   │          │ ALB (Multi-AZ)   │               │
│  │ ECS Fargate      │          │ ECS Fargate      │               │
│  │ (Auto Scaling)   │          │ (scaled down)    │               │
│  │                  │          │                  │               │
│  │ Aurora Global    │ ──────►  │ Aurora Global    │               │
│  │ (Writer)         │  Async   │ (Reader)         │               │
│  │                  │  Repl    │                  │               │
│  │ ElastiCache      │          │ ElastiCache      │               │
│  │ (Multi-AZ)       │          │ (Multi-AZ)       │               │
│  └──────────────────┘          └──────────────────┘               │
│                                                                     │
│  S3: Cross-region replication for static assets                    │
│  Secrets Manager: Multi-region secrets                             │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 💡 Key Takeaways

- **Region** — географически изолированная локация с 3+ Availability Zones
- **Availability Zone** — один или несколько физически изолированных дата-центров
- **Edge Location** — точка присутствия для CDN и DNS (600+ по миру)
- **Multi-AZ** — базовый уровень отказоустойчивости, защита от сбоя одного AZ
- **Multi-Region** — защита от регионального сбоя, требует дополнительной архитектуры
- Выбор региона зависит от: латентности, compliance, стоимости, доступности сервисов

---

## 🚀 Next Steps

**Следующие модули:**
- [IAM](../04_IAM/) — управление доступом
- [VPC](../07_VPC/) — сетевая инфраструктура

**Практические задания:**
1. Используйте AWS CLI для получения списка AZ в вашем регионе
2. Создайте CloudFront distribution для S3 bucket
3. Сравните латентность из вашей локации до разных регионов
4. Изучите AWS Global Infrastructure Map

**Для углубления:**
- Изучите AWS Outposts для hybrid deployments
- Посмотрите на AWS Wavelength для 5G use cases
- Разберитесь с Global Accelerator для non-HTTP workloads

---

## 📚 Additional Resources

**Documentation:**
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

**Tools:**
- [CloudPing](https://www.cloudping.info/) — тест латентности до регионов
- [AWS Global Infrastructure Map](https://infrastructure.aws/)

**Videos:**
- [AWS re:Invent: Global Infrastructure](https://www.youtube.com/results?search_query=aws+reinvent+global+infrastructure)

---

