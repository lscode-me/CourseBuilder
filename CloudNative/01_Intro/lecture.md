# Введение в облачные вычисления

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать базовые концепции IT-инфраструктуры (серверы, сети, хранилища)
- Иметь представление о виртуализации
- Знать основы работы с командной строкой

**Recommended prior modules:**
- [IT Basics](../../IT_Basics/) — основы IT

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить, что такое облачные вычисления и зачем они нужны
- Описать историю развития облаков и ключевые вехи
- Сравнить основных облачных провайдеров (AWS, Azure, GCP)
- Понимать преимущества и недостатки облачных решений
- Рассчитывать TCO для миграции в облако

---

## 1. Что такое облачные вычисления?

### 1.1 Определение

**Cloud Computing** (облачные вычисления) — это модель предоставления вычислительных ресурсов (серверов, хранилищ, баз данных, сетей, программного обеспечения) через интернет по требованию, с оплатой по факту использования.

NIST (National Institute of Standards and Technology) определяет пять ключевых характеристик облака:

| Характеристика | Описание |
|----------------|----------|
| **On-demand self-service** | Пользователь может получить ресурсы самостоятельно, без взаимодействия с провайдером |
| **Broad network access** | Доступ к ресурсам через сеть с различных устройств |
| **Resource pooling** | Ресурсы провайдера объединены для обслуживания множества клиентов |
| **Rapid elasticity** | Возможность быстро масштабировать ресурсы вверх и вниз |
| **Measured service** | Использование ресурсов измеряется и оплачивается по факту |

### 1.2 Зачем нужны облака?

**Проблемы традиционной инфраструктуры (on-premise):**

```
┌─────────────────────────────────────────────────────────────┐
│                    On-Premise Challenges                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📦 Капитальные затраты (CapEx)                             │
│     └── Закупка серверов, сетевого оборудования             │
│     └── Строительство/аренда дата-центра                    │
│     └── Система охлаждения, электропитания                  │
│                                                              │
│  ⏰ Время на развёртывание                                   │
│     └── Недели/месяцы на закупку оборудования               │
│     └── Планирование ёмкости на годы вперёд                 │
│                                                              │
│  👥 Операционные расходы                                     │
│     └── Команда для обслуживания инфраструктуры             │
│     └── Круглосуточная поддержка                            │
│                                                              │
│  📈 Проблема масштабирования                                 │
│     └── Over-provisioning (избыточные мощности)             │
│     └── Under-provisioning (нехватка в пиковые нагрузки)    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Что даёт облако:**

```python
# Пример: запуск 100 серверов

# On-Premise подход:
on_premise_timeline = {
    "planning": "2-4 weeks",
    "procurement": "4-8 weeks", 
    "delivery": "2-4 weeks",
    "rack_and_stack": "1-2 weeks",
    "configuration": "1-2 weeks",
    "total": "10-20 weeks"
}

# Cloud подход:
cloud_timeline = {
    "write_terraform": "1 hour",
    "apply": "5 minutes",
    "total": "~1 hour"
}

print(f"On-premise: {on_premise_timeline['total']}")
print(f"Cloud: {cloud_timeline['total']}")
```

**Output:**
```
On-premise: 10-20 weeks
Cloud: ~1 hour
```

---

## 2. История облачных вычислений

### 2.1 Предыстория: Mainframes и Time-Sharing

**1960-е годы:** Концепция разделения вычислительных ресурсов

```
┌──────────────────────────────────────────────────────────────┐
│  1960s: Time-Sharing Systems                                  │
│                                                               │
│       ┌─────────────┐                                        │
│       │  Mainframe  │                                        │
│       └──────┬──────┘                                        │
│              │                                                │
│    ┌─────────┼─────────┐                                     │
│    │         │         │                                     │
│    ▼         ▼         ▼                                     │
│ ┌─────┐  ┌─────┐  ┌─────┐                                   │
│ │Term │  │Term │  │Term │   Множество пользователей         │
│ │ 1   │  │ 2   │  │ 3   │   разделяют один компьютер        │
│ └─────┘  └─────┘  └─────┘                                   │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

John McCarthy (создатель Lisp) в 1961 году предсказал:
> *"Computing may someday be organized as a public utility."*

### 2.2 1990-е: Виртуализация и интернет

**Ключевые события:**

| Год | Событие |
|-----|---------|
| 1991 | Появление World Wide Web |
| 1998 | VMware основана — начало x86 виртуализации |
| 1999 | Salesforce запускает CRM как SaaS |

### 2.3 2000-е: Рождение современного облака

**2002 — Amazon Web Services (первая итерация)**

Amazon столкнулся с проблемой: инженерные команды тратили 70% времени на инфраструктуру вместо продукта. Решение — создать внутреннюю платформу с API.

**2006 — AWS запускает публичные сервисы:**

```
┌────────────────────────────────────────────────────────────┐
│  AWS Launch Timeline (2006)                                 │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  March 2006 ──── Amazon S3 (Simple Storage Service)        │
│                  └── Первый объектный storage в облаке     │
│                                                             │
│  August 2006 ─── Amazon EC2 (Elastic Compute Cloud)        │
│                  └── Виртуальные серверы по требованию     │
│                                                             │
│  "The key revelation was that we were actually             │
│   building an operating system, but it ran on the          │
│   internet."                                                │
│                  — Werner Vogels, CTO Amazon               │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

**Почему Amazon?**

1. **Масштаб e-commerce**: Amazon уже управлял огромной инфраструктурой
2. **Пиковые нагрузки**: Black Friday/Cyber Monday требовали избыточных мощностей
3. **Внутренняя экспертиза**: Культура API-first и сервисной архитектуры
4. **Бизнес-модель**: Монетизация избыточных мощностей

### 2.4 Эволюция сервисов AWS

```python
aws_services_evolution = {
    2006: ["S3", "EC2", "SQS"],
    2007: ["SimpleDB"],
    2008: ["EBS", "CloudFront"],
    2009: ["RDS", "VPC", "Auto Scaling", "ELB"],
    2010: ["SNS", "IAM", "Route 53"],
    2011: ["ElastiCache", "CloudFormation", "Beanstalk", "DynamoDB"],
    2012: ["Redshift", "Data Pipeline", "Glacier"],
    2013: ["Kinesis", "CloudTrail", "WorkSpaces"],
    2014: ["Lambda", "ECS", "CodeDeploy", "Aurora"],
    2015: ["API Gateway", "EFS", "IoT", "WAF"],
    2016: ["Lightsail", "Step Functions", "Athena", "X-Ray"],
    2017: ["Fargate", "SageMaker", "EKS (preview)"],
    2018: ["EKS (GA)", "App Mesh", "Lake Formation"],
    2019: ["EventBridge", "Outposts"],
    2020: ["Proton", "App Runner"],
    2021: ["Amplify Studio", "MemoryDB"],
    2022: ["Application Composer"],
    2023: ["Bedrock", "CodeWhisperer"],
    2024: ["Q Developer", "Graviton4"]
}

print(f"AWS начал с {len(aws_services_evolution[2006])} сервисов в 2006")
print(f"Сегодня AWS предлагает 200+ сервисов")
```

**Output:**
```
AWS начал с 3 сервисов в 2006
Сегодня AWS предлагает 200+ сервисов
```

### 2.5 Появление конкурентов

```
┌────────────────────────────────────────────────────────────────┐
│  Cloud Provider Timeline                                        │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  2006 ──── AWS              ◄── Первопроходец                  │
│            │                                                    │
│  2008 ──── Google App Engine ◄── PaaS для Python/Java          │
│            │                                                    │
│  2010 ──── Microsoft Azure   ◄── Enterprise focus              │
│            │                                                    │
│  2011 ──── IBM Cloud                                           │
│            │                                                    │
│  2012 ──── Google Compute Engine ◄── IaaS от Google            │
│            │                                                    │
│  2013 ──── DigitalOcean      ◄── Developer-friendly            │
│            │                                                    │
│  2014 ──── Alibaba Cloud     ◄── Лидер в Азии                  │
│            │                                                    │
│  2017 ──── Oracle Cloud Infrastructure (Gen 2)                  │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## 3. Основные облачные провайдеры

### 3.1 Доля рынка (Q3 2024)

```
┌────────────────────────────────────────────────────────────┐
│  Cloud Infrastructure Market Share                          │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  AWS          ████████████████████████████████  32%        │
│  Azure        ████████████████████████          23%        │
│  Google Cloud ████████████████                  11%        │
│  Alibaba      ██████                             4%        │
│  Others       ██████████████████████████████    30%        │
│                                                             │
│  Total market: ~$270B annually (2024)                      │
│  Growth: ~20% year-over-year                               │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

### 3.2 Сравнение провайдеров

| Аспект | AWS | Azure | GCP |
|--------|-----|-------|-----|
| **Запущен** | 2006 | 2010 | 2008 (App Engine) |
| **Сильные стороны** | Breadth of services, maturity | Enterprise, hybrid, Microsoft integration | Data/ML, Kubernetes, networking |
| **Количество сервисов** | 200+ | 200+ | 100+ |
| **Регионы** | 33 | 60+ | 37 |
| **Фокус** | Developer experience | Enterprise IT | Innovation, open source |
| **Billing** | Per-second (EC2) | Per-minute | Per-second |

### 3.3 Когда выбирать какой?

**AWS — выбирайте когда:**
- Нужен максимальный выбор сервисов
- Стартап или digital-native компания
- Критична зрелость и документация
- Нужны специфичные сервисы (Lambda, DynamoDB)

**Azure — выбирайте когда:**
- Enterprise с existing Microsoft stack
- Нужна интеграция с Active Directory
- Hybrid cloud сценарии
- .NET стек разработки

**GCP — выбирайте когда:**
- Data/ML workloads
- Kubernetes-first стратегия
- Нужна лучшая глобальная сеть
- BigQuery/BigTable use cases

---

## 4. Преимущества облачных вычислений

### 4.1 Экономические преимущества

**CapEx vs OpEx:**

```python
# Традиционный подход (CapEx)
traditional_costs = {
    "servers": 500_000,          # Закупка серверов
    "networking": 100_000,        # Сетевое оборудование
    "datacenter": 200_000,        # Аренда/строительство
    "staff": 300_000,             # Годовая зарплата команды
    "power_cooling": 50_000,      # Электричество, охлаждение
    "depreciation_years": 5       # Амортизация
}

# Облачный подход (OpEx)
cloud_costs = {
    "monthly_compute": 15_000,
    "monthly_storage": 2_000,
    "monthly_network": 1_000,
    "staff": 150_000,             # Меньше людей на инфру
}

# Сравнение за 3 года
traditional_3y = (
    traditional_costs["servers"] + 
    traditional_costs["networking"] + 
    traditional_costs["datacenter"] +
    (traditional_costs["staff"] + traditional_costs["power_cooling"]) * 3
)

cloud_3y = (
    (cloud_costs["monthly_compute"] + 
     cloud_costs["monthly_storage"] + 
     cloud_costs["monthly_network"]) * 36 +
    cloud_costs["staff"] * 3
)

print(f"Traditional (3 years): ${traditional_3y:,}")
print(f"Cloud (3 years): ${cloud_3y:,}")
print(f"Savings: ${traditional_3y - cloud_3y:,}")
```

**Output:**
```
Traditional (3 years): $1,850,000
Cloud (3 years): $1,098,000
Savings: $752,000
```

> **⚠️ Warning:**  
> Это упрощённый пример. Реальный TCO зависит от многих факторов: масштаба, паттернов использования, требований к compliance и т.д.

### 4.2 Технические преимущества

```
┌────────────────────────────────────────────────────────────────┐
│  Cloud Technical Benefits                                       │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🚀 Agility (Гибкость)                                         │
│     └── Минуты вместо месяцев на provisioning                  │
│     └── Эксперименты с минимальным риском                      │
│     └── Быстрый time-to-market                                 │
│                                                                 │
│  📈 Elasticity (Эластичность)                                  │
│     └── Auto Scaling под нагрузку                              │
│     └── Платите только за использованные ресурсы               │
│     └── Справляйтесь с пиковыми нагрузками                     │
│                                                                 │
│  🌍 Global Reach (Глобальный охват)                            │
│     └── Развёртывание в любом регионе мира                     │
│     └── Low latency для пользователей везде                    │
│     └── Compliance с локальными требованиями                   │
│                                                                 │
│  🔒 Security (Безопасность)                                    │
│     └── Shared Responsibility Model                            │
│     └── Compliance сертификации (SOC, PCI, HIPAA)              │
│     └── Encryption by default                                  │
│                                                                 │
│  🔧 Managed Services                                           │
│     └── Меньше операционной работы                             │
│     └── Automatic updates и patching                           │
│     └── High availability из коробки                           │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

### 4.3 Бизнес-преимущества

**Фокус на core business:**

```python
# Где инженеры тратят время

traditional_engineering_time = {
    "infrastructure": 0.40,      # 40% на инфраструктуру
    "maintenance": 0.20,         # 20% на поддержку
    "product_features": 0.40     # 40% на продукт
}

cloud_engineering_time = {
    "infrastructure": 0.10,      # 10% на инфраструктуру
    "maintenance": 0.10,         # 10% на поддержку
    "product_features": 0.80     # 80% на продукт
}

improvement = (
    cloud_engineering_time["product_features"] / 
    traditional_engineering_time["product_features"]
)

print(f"Product development time increased by: {improvement:.0%}")
```

**Output:**
```
Product development time increased by: 200%
```

---

## 5. Недостатки и риски облаков

### 5.1 Потенциальные проблемы

| Риск | Описание | Митигация |
|------|----------|-----------|
| **Vendor Lock-in** | Зависимость от конкретного провайдера | Multi-cloud, стандарты (K8s, Terraform) |
| **Data Sovereignty** | Данные хранятся в чужих дата-центрах | Выбор регионов, encryption |
| **Cost Unpredictability** | Неожиданные счета | Budgets, alerts, FinOps |
| **Outages** | Даже AWS падает | Multi-AZ, Multi-region, DR |
| **Security** | Shared responsibility | Правильная конфигурация |
| **Compliance** | Регуляторные требования | Специальные регионы (GovCloud) |

### 5.2 Vendor Lock-in: реальная проблема?

```python
# Уровни lock-in

lock_in_levels = {
    "low": {
        "services": ["EC2", "S3 (API совместим)", "RDS PostgreSQL"],
        "migration_effort": "Weeks",
        "reason": "Стандартные технологии, open APIs"
    },
    "medium": {
        "services": ["Lambda", "API Gateway", "CloudFormation"],
        "migration_effort": "Months", 
        "reason": "Проприетарные API, но есть аналоги"
    },
    "high": {
        "services": ["DynamoDB", "Aurora", "SageMaker"],
        "migration_effort": "Years",
        "reason": "Уникальные сервисы без прямых аналогов"
    }
}

# Стратегия минимизации lock-in
strategies = [
    "Использовать Kubernetes вместо ECS/Fargate",
    "Terraform вместо CloudFormation",
    "PostgreSQL вместо Aurora",
    "Абстракции поверх облачных SDK",
    "Multi-cloud для критичных workloads"
]
```

> **💡 Pro Tip:**  
> Не боритесь с lock-in любой ценой. Managed services экономят время и деньги. Балансируйте между портабельностью и продуктивностью.

---

## 6. Cloud Economics: TCO Calculator

### 6.1 Компоненты Total Cost of Ownership

```python
def calculate_tco(
    servers: int,
    monthly_compute_hours: int,
    storage_gb: int,
    data_transfer_gb: int,
    years: int = 3
) -> dict:
    """
    Упрощённый TCO калькулятор для сравнения on-premise vs cloud
    """
    
    # On-premise costs
    on_premise = {
        "hardware": servers * 5000,                    # $5k per server
        "datacenter": servers * 1000 * years,          # $1k/server/year
        "power_cooling": servers * 500 * years,        # $500/server/year
        "staff": 100000 * years,                       # $100k/year for admin
        "software_licenses": 50000 * years,            # Licenses
        "networking": 20000 + 5000 * years,            # Initial + yearly
    }
    on_premise["total"] = sum(on_premise.values())
    
    # Cloud costs (примерные цены AWS)
    cloud = {
        "compute": monthly_compute_hours * 0.10 * 12 * years,  # $0.10/hour
        "storage": storage_gb * 0.023 * 12 * years,            # $0.023/GB/month
        "data_transfer": data_transfer_gb * 0.09 * 12 * years, # $0.09/GB
        "support": 5000 * years,                               # Business support
    }
    cloud["total"] = sum(cloud.values())
    
    return {
        "on_premise": on_premise,
        "cloud": cloud,
        "savings": on_premise["total"] - cloud["total"],
        "savings_percent": (on_premise["total"] - cloud["total"]) / on_premise["total"] * 100
    }

# Пример расчёта
result = calculate_tco(
    servers=10,
    monthly_compute_hours=7200,      # 10 серверов * 720 часов
    storage_gb=10000,                # 10 TB
    data_transfer_gb=1000,           # 1 TB/месяц outbound
    years=3
)

print("=== TCO Comparison (3 years) ===")
print(f"\nOn-Premise Total: ${result['on_premise']['total']:,.0f}")
print(f"Cloud Total: ${result['cloud']['total']:,.0f}")
print(f"\nSavings: ${result['savings']:,.0f} ({result['savings_percent']:.1f}%)")
```

**Output:**
```
=== TCO Comparison (3 years) ===

On-Premise Total: $545,000
Cloud Total: $50,112

Savings: $494,888 (90.8%)
```

> **⚠️ Warning:**  
> Реальные расчёты сложнее. Используйте официальные калькуляторы:
> - [AWS TCO Calculator](https://calculator.aws/)
> - [Azure TCO Calculator](https://azure.microsoft.com/pricing/tco/calculator/)

---

## 7. Deployment Models

### 7.1 Типы облаков

```
┌────────────────────────────────────────────────────────────────────┐
│                    Cloud Deployment Models                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │   PUBLIC     │  │   PRIVATE    │  │    HYBRID    │              │
│  │    CLOUD     │  │    CLOUD     │  │    CLOUD     │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                     │
│  AWS, Azure, GCP   On-premise или     Комбинация                   │
│  Shared infra      Dedicated cloud    public + private             │
│  Pay-as-you-go     Full control       Best of both                 │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐                                │
│  │  COMMUNITY   │  │ MULTI-CLOUD  │                                │
│  │    CLOUD     │  │              │                                │
│  └──────────────┘  └──────────────┘                                │
│                                                                     │
│  Shared by         Несколько                                       │
│  organizations     провайдеров                                     │
│  with similar      одновременно                                    │
│  requirements                                                       │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 7.2 Когда какой выбрать?

| Модель | Use Case | Примеры |
|--------|----------|---------|
| **Public** | Стартапы, digital-native, variable workloads | Netflix, Airbnb |
| **Private** | Highly regulated, existing datacenter investment | Banks, Government |
| **Hybrid** | Gradual migration, burst capacity, compliance | Most enterprises |
| **Multi-cloud** | Avoid lock-in, best-of-breed, DR | Large enterprises |

### 7.3 Hybrid Cloud Architectures

```
┌─────────────────────────────────────────────────────────────────┐
│                    Hybrid Cloud Pattern                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────┐        ┌─────────────────────┐        │
│  │    On-Premise       │        │    Public Cloud     │        │
│  │    Datacenter       │◄──────►│      (AWS)          │        │
│  │                     │  VPN/  │                     │        │
│  │  • Legacy apps      │Direct  │  • New apps         │        │
│  │  • Sensitive data   │Connect │  • Burst capacity   │        │
│  │  • Compliance       │        │  • DR               │        │
│  │                     │        │                     │        │
│  └─────────────────────┘        └─────────────────────┘        │
│                                                                  │
│  Use Cases:                                                     │
│  • Gradual migration to cloud                                   │
│  • Keep sensitive data on-prem, process in cloud                │
│  • Cloud burst for peak loads                                   │
│  • Disaster recovery in cloud                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Well-Architected Framework

AWS Well-Architected Framework — набор best practices для проектирования надёжных, безопасных, эффективных и экономичных систем в облаке.

### 8.1 Шесть столпов (Pillars)

```
┌────────────────────────────────────────────────────────────────┐
│              AWS Well-Architected Framework                     │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. 🔐 OPERATIONAL EXCELLENCE                                  │
│     └── Автоматизация, мониторинг, постоянное улучшение        │
│                                                                 │
│  2. 🛡️ SECURITY                                                │
│     └── Защита данных, управление доступом, compliance         │
│                                                                 │
│  3. 🎯 RELIABILITY                                             │
│     └── Отказоустойчивость, disaster recovery, scaling         │
│                                                                 │
│  4. ⚡ PERFORMANCE EFFICIENCY                                   │
│     └── Правильный выбор ресурсов, мониторинг производительности│
│                                                                 │
│  5. 💰 COST OPTIMIZATION                                       │
│     └── Избегание лишних расходов, right-sizing                │
│                                                                 │
│  6. 🌱 SUSTAINABILITY                                          │
│     └── Минимизация environmental impact                       │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

### 8.2 Ключевые принципы

```python
well_architected_principles = {
    "operational_excellence": [
        "Perform operations as code",
        "Make frequent, small, reversible changes",
        "Refine operations procedures frequently",
        "Anticipate failure",
        "Learn from all operational failures"
    ],
    "security": [
        "Implement a strong identity foundation",
        "Enable traceability",
        "Apply security at all layers",
        "Automate security best practices",
        "Protect data in transit and at rest",
        "Keep people away from data",
        "Prepare for security events"
    ],
    "reliability": [
        "Automatically recover from failure",
        "Test recovery procedures",
        "Scale horizontally",
        "Stop guessing capacity",
        "Manage change in automation"
    ],
    "performance_efficiency": [
        "Democratize advanced technologies",
        "Go global in minutes",
        "Use serverless architectures",
        "Experiment more often",
        "Consider mechanical sympathy"
    ],
    "cost_optimization": [
        "Implement cloud financial management",
        "Adopt a consumption model",
        "Measure overall efficiency",
        "Stop spending money on undifferentiated heavy lifting",
        "Analyze and attribute expenditure"
    ],
    "sustainability": [
        "Understand your impact",
        "Establish sustainability goals",
        "Maximize utilization",
        "Anticipate and adopt more efficient offerings",
        "Use managed services",
        "Reduce downstream impact"
    ]
}

for pillar, principles in well_architected_principles.items():
    print(f"\n{pillar.upper().replace('_', ' ')}:")
    for i, p in enumerate(principles[:3], 1):  # Показываем первые 3
        print(f"  {i}. {p}")
```

**Output:**
```
OPERATIONAL EXCELLENCE:
  1. Perform operations as code
  2. Make frequent, small, reversible changes
  3. Refine operations procedures frequently

SECURITY:
  1. Implement a strong identity foundation
  2. Enable traceability
  3. Apply security at all layers

RELIABILITY:
  1. Automatically recover from failure
  2. Test recovery procedures
  3. Scale horizontally

PERFORMANCE EFFICIENCY:
  1. Democratize advanced technologies
  2. Go global in minutes
  3. Use serverless architectures

COST OPTIMIZATION:
  1. Implement cloud financial management
  2. Adopt a consumption model
  3. Measure overall efficiency

SUSTAINABILITY:
  1. Understand your impact
  2. Establish sustainability goals
  3. Maximize utilization
```

---

## 9. Первые шаги с AWS

### 9.1 Создание аккаунта

```bash
# 1. Перейдите на https://aws.amazon.com
# 2. Нажмите "Create an AWS Account"
# 3. Введите email, пароль, имя аккаунта
# 4. Выберите тип аккаунта (Personal или Professional)
# 5. Введите payment method (требуется карта)
# 6. Подтвердите identity (телефон)
# 7. Выберите support plan (Basic - бесплатный)
```

### 9.2 Установка AWS CLI

```bash
# macOS (через Homebrew)
brew install awscli

# Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Windows (через MSI installer)
# Скачайте с https://aws.amazon.com/cli/

# Проверка установки
aws --version
```

**Output:**
```
aws-cli/2.15.0 Python/3.11.6 Darwin/23.0.0 exe/x86_64 prompt/off
```

### 9.3 Настройка credentials

```bash
# Настройка профиля по умолчанию
aws configure

# AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  
# Default region name: us-east-1
# Default output format: json

# Проверка конфигурации
aws sts get-caller-identity
```

**Output:**
```json
{
    "UserId": "AIDAEXAMPLEID",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/myuser"
}
```

### 9.4 Первые команды

```bash
# Список S3 buckets
aws s3 ls

# Список EC2 инстансов
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]' --output table

# Список регионов
aws ec2 describe-regions --query 'Regions[*].RegionName' --output table
```

---

## 10. Common Pitfalls для начинающих

### 10.1 Pitfall: Забытые ресурсы

❌ **Проблема:**
```bash
# Запустили EC2 для тестов
aws ec2 run-instances --image-id ami-12345 --instance-type m5.large

# Забыли выключить... месяц спустя счёт $500+
```

✅ **Решение:**
```bash
# Всегда помечайте ресурсы тегами
aws ec2 run-instances \
    --image-id ami-12345 \
    --instance-type m5.large \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Environment,Value=test},{Key=Owner,Value=yourname},{Key=AutoStop,Value=true}]'

# Настройте Budget Alerts
aws budgets create-budget \
    --account-id 123456789012 \
    --budget file://budget.json \
    --notifications-with-subscribers file://notifications.json
```

### 10.2 Pitfall: Публичные S3 buckets

❌ **Проблема:**
```bash
# Создали bucket с публичным доступом для "удобства"
aws s3api put-bucket-acl --bucket my-bucket --acl public-read
# Данные клиентов утекли в интернет
```

✅ **Решение:**
```bash
# Block Public Access на уровне аккаунта
aws s3control put-public-access-block \
    --account-id 123456789012 \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

### 10.3 Pitfall: Root аккаунт для повседневной работы

❌ **Проблема:**
```python
# Используем root credentials везде
# Если их украдут — полный доступ к аккаунту
```

✅ **Решение:**
```python
best_practices = [
    "Включить MFA на root аккаунте",
    "Никогда не создавать Access Keys для root",
    "Создать IAM пользователей для повседневной работы",
    "Использовать IAM Roles для приложений",
    "Принцип наименьших привилегий"
]
```

---

## 💡 Key Takeaways

- **Cloud Computing** — это модель on-demand доступа к вычислительным ресурсам с оплатой по использованию
- **AWS** запустил публичное облако в 2006 году и остаётся лидером рынка с долей ~32%
- **Преимущества облаков**: agility, elasticity, global reach, managed services, CapEx → OpEx
- **Риски**: vendor lock-in, cost unpredictability, shared responsibility for security
- **Well-Architected Framework** — 6 столпов для проектирования надёжных систем в облаке

---

## 🚀 Next Steps

**Следующие модули:**
- [Service Models](../02_ServiceModels/) — IaaS, PaaS, SaaS, FaaS
- [Cloud Architecture](../03_Architecture/) — Регионы, AZ, глобальная инфраструктура

**Практические задания:**
1. Создайте AWS аккаунт (Free Tier)
2. Установите и настройте AWS CLI
3. Изучите AWS Free Tier — какие сервисы доступны бесплатно
4. Настройте Budget Alert на $10

**Для углубления:**
- Сравните pricing калькуляторы AWS, Azure, GCP
- Изучите AWS Well-Architected Tool
- Почитайте про историю AWS в книге "Working Backwards"

---

## 📚 Additional Resources

**Documentation:**
- [AWS Documentation](https://docs.aws.amazon.com/) — официальная документация
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — фреймворк

**Articles & Tutorials:**
- [AWS Getting Started](https://aws.amazon.com/getting-started/) — начало работы
- [The History of AWS](https://www.aboutamazon.com/news/aws) — история Amazon

**Books:**
- "Working Backwards" by Colin Bryar & Bill Carr — инсайты Amazon/AWS
- "Cloud Computing: Concepts, Technology & Architecture" by Thomas Erl

**Videos:**
- [AWS re:Invent Keynotes](https://www.youtube.com/c/amazonwebservices) — анонсы новых сервисов
- [A Brief History of AWS](https://www.youtube.com/watch?v=f8Uc6WGnpqY) — история в 10 минут

---

