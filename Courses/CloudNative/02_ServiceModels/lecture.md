# Модели облачных сервисов: IaaS, PaaS, SaaS, FaaS

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции облачных вычислений
- Знать, что такое виртуализация и контейнеризация
- Иметь представление о компонентах IT-инфраструктуры

**Recommended prior modules:**

- [Введение в облака](../01_Intro/) — основы облачных вычислений

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать модели сервисов: IaaS, PaaS, SaaS, FaaS
- Понимать Shared Responsibility Model для каждой модели
- Выбирать правильную модель для конкретного use case
- Объяснять концепцию XaaS (Everything as a Service)

---

## 1. Обзор моделей сервисов

### 1.1 Pizza as a Service: аналогия

Популярная аналогия для понимания облачных моделей:

```

┌────────────────────────────────────────────────────────────────────────┐
│                        Pizza as a Service                               │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   On-Premise      IaaS           PaaS           SaaS                   │
│   (Made at Home)  (Take & Bake)  (Delivery)     (Dine Out)             │
│                                                                         │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐            │
│   │ Dining  │    │ Dining  │    │ Dining  │    │░░░░░░░░░│ ◄─ Vendor  │
│   │ Table   │    │ Table   │    │░░░░░░░░░│    │░░░░░░░░░│             │
│   ├─────────┤    ├─────────┤    │░░░░░░░░░│    │░░░░░░░░░│             │
│   │ Plates  │    │ Plates  │    │░░░░░░░░░│    │░░░░░░░░░│             │
│   ├─────────┤    ├─────────┤    │░░░░░░░░░│    │░░░░░░░░░│             │
│   │ Drinks  │    │ Drinks  │    │░░░░░░░░░│    │░░░░░░░░░│             │
│   ├─────────┤    ├─────────┤    ├─────────┤    │░░░░░░░░░│             │
│   │ Pizza   │    │ Pizza   │    │ Pizza   │    │░░░░░░░░░│             │
│   ├─────────┤    ├─────────┤    │░░░░░░░░░│    │░░░░░░░░░│             │
│   │ Oven    │    │░░░░░░░░░│    │░░░░░░░░░│    │░░░░░░░░░│             │
│   ├─────────┤    │░░░░░░░░░│    │░░░░░░░░░│    │░░░░░░░░░│             │
│   │Electric │    │░░░░░░░░░│    │░░░░░░░░░│    │░░░░░░░░░│             │
│   └─────────┘    └─────────┘    └─────────┘    └─────────┘            │
│                                                                         │
│   █ You manage   ░ Vendor manages                                      │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘

```

### 1.2 Реальные компоненты IT-стека

```

┌────────────────────────────────────────────────────────────────────────┐
│              Cloud Service Models: Responsibility Layers                │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│          On-Prem    IaaS       PaaS       FaaS       SaaS              │
│                                                                         │
│         ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐              │
│ App     │  You │  │  You │  │  You │  │  You │  │██████│              │
│         ├──────┤  ├──────┤  ├──────┤  ├──────┤  │██████│              │
│ Data    │  You │  │  You │  │  You │  │  You │  │██████│              │
│         ├──────┤  ├──────┤  ├──────┤  ├──────┤  │██████│              │
│ Runtime │  You │  │  You │  │██████│  │██████│  │██████│              │
│         ├──────┤  ├──────┤  │██████│  │██████│  │██████│              │
│ Middle- │  You │  │  You │  │██████│  │██████│  │██████│              │
│ ware    ├──────┤  ├──────┤  │██████│  │██████│  │██████│              │
│ OS      │  You │  │  You │  │██████│  │██████│  │██████│              │
│         ├──────┤  ├──────┤  │██████│  │██████│  │██████│              │
│ Virtual-│  You │  │██████│  │██████│  │██████│  │██████│              │
│ ization ├──────┤  │██████│  │██████│  │██████│  │██████│              │
│ Servers │  You │  │██████│  │██████│  │██████│  │██████│              │
│         ├──────┤  │██████│  │██████│  │██████│  │██████│              │
│ Storage │  You │  │██████│  │██████│  │██████│  │██████│              │
│         ├──────┤  │██████│  │██████│  │██████│  │██████│              │
│ Network │  You │  │██████│  │██████│  │██████│  │██████│              │
│         └──────┘  └──────┘  └──────┘  └──────┘  └──────┘              │
│                                                                         │
│   █ Cloud Provider manages                                              │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘

```

---

## 2. Infrastructure as a Service (IaaS)

### 2.1 Определение

**IaaS** — предоставление базовой IT-инфраструктуры (compute, storage, networking) как сервиса. Вы получаете виртуальные машины и управляете всем, что на них работает.

### 2.2 AWS IaaS сервисы

```python

aws_iaas_services = {
    "compute": {
        "EC2": "Virtual servers",
        "EC2 Auto Scaling": "Automatic scaling of EC2",
        "EC2 Spot": "Discounted spare capacity"
    },
    "storage": {
        "EBS": "Block storage for EC2",
        "EFS": "Managed NFS file system",
        "S3": "Object storage (также можно считать PaaS)"
    },
    "networking": {
        "VPC": "Virtual Private Cloud",
        "ELB": "Load Balancers",
        "Direct Connect": "Dedicated network connection"
    }
}

for category, services in aws_iaas_services.items():
    print(f"\n{category.upper()}:")
    for name, desc in services.items():
        print(f"  • {name}: {desc}")

```

**Output:**
```

COMPUTE:
  • EC2: Virtual servers
  • EC2 Auto Scaling: Automatic scaling of EC2
  • EC2 Spot: Discounted spare capacity

STORAGE:
  • EBS: Block storage for EC2
  • EFS: Managed NFS file system
  • S3: Object storage (также можно считать PaaS)

NETWORKING:
  • VPC: Virtual Private Cloud
  • ELB: Load Balancers
  • Direct Connect: Dedicated network connection

```

### 2.3 Пример: развёртывание на IaaS

```bash
# Создание EC2 инстанса с нуля
# Вы отвечаете за: ОС, runtime, middleware, app, data

# 1. Запуск инстанса
aws ec2 run-instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --instance-type t3.medium \
    --key-name my-key \
    --security-group-ids sg-12345678 \
    --subnet-id subnet-12345678

# 2. Подключение и настройка (ваша ответственность)
ssh -i my-key.pem ec2-user@<public-ip>

# Установка и настройка всего стека
sudo yum update -y
sudo yum install -y python3 nginx postgresql

# Настройка nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Развёртывание приложения
git clone https://github.com/myapp/myapp.git
cd myapp
pip3 install -r requirements.txt
python3 app.py

```

### 2.4 Когда использовать IaaS

| Use Case | Почему IaaS |
|----------|-------------|
| **Lift and shift migration** | Минимальные изменения в существующих приложениях |
| **Custom OS requirements** | Нужна специфичная ОС или конфигурация |
| **Legacy applications** | Старые приложения, не поддерживающие managed services |
| **High-performance computing** | Нужен полный контроль над hardware |
| **Compliance requirements** | Специфичные требования к настройке системы |

### 2.5 Плюсы и минусы IaaS

```

✅ ПЛЮСЫ                          ❌ МИНУСЫ
─────────────────────────────     ─────────────────────────────
• Полный контроль над ОС          • Вы отвечаете за патчинг ОС
• Гибкость конфигурации           • Сложнее масштабировать
• Знакомая модель для IT          • Больше операционной работы
• Любой софт можно установить     • Нужна экспертиза в Linux/Windows
• Предсказуемая производительность• Дороже при неэффективном использовании

```

---

## 3. Platform as a Service (PaaS)

### 3.1 Определение

**PaaS** — платформа для развёртывания и запуска приложений без управления underlying инфраструктурой. Провайдер управляет ОС, runtime, middleware.

### 3.2 AWS PaaS сервисы

```python

aws_paas_services = {
    "application_platforms": {
        "Elastic Beanstalk": "Deploy web apps (Java, .NET, Node, Python, etc.)",
        "App Runner": "Containerized web apps from source code",
        "Lightsail": "Simple virtual servers with bundled resources"
    },
    "databases": {
        "RDS": "Managed relational databases",
        "Aurora": "MySQL/PostgreSQL compatible, cloud-native",
        "DynamoDB": "Managed NoSQL database",
        "ElastiCache": "Managed Redis/Memcached"
    },
    "messaging": {
        "SQS": "Managed message queues",
        "SNS": "Managed pub/sub messaging",
        "EventBridge": "Serverless event bus"
    },
    "containers": {
        "ECS": "Container orchestration",
        "EKS": "Managed Kubernetes",
        "Fargate": "Serverless containers"
    }
}

total_services = sum(len(v) for v in aws_paas_services.values())
print(f"Примеры AWS PaaS сервисов: {total_services} сервисов")

```

**Output:**
```

Примеры AWS PaaS сервисов: 12 сервисов

```

### 3.3 Пример: развёртывание на PaaS

```bash
# Elastic Beanstalk: развёртывание приложения
# Вы отвечаете только за: код приложения и данные

# 1. Инициализация проекта
eb init -p python-3.9 my-flask-app --region us-east-1

# 2. Создание environment
eb create production

# 3. Деплой приложения (всё остальное - забота AWS)
eb deploy

# AWS автоматически:
# - Создаёт EC2 инстансы
# - Настраивает Load Balancer
# - Настраивает Auto Scaling
# - Устанавливает и настраивает Python runtime
# - Управляет патчами ОС
# - Настраивает health checks
```

**application.py для Elastic Beanstalk:**

```python

from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello from PaaS!"

@application.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)

```

### 3.4 Когда использовать PaaS

| Use Case | Почему PaaS |
|----------|-------------|
| **New web applications** | Быстрый старт без настройки инфраструктуры |
| **Microservices** | Managed containers (ECS/EKS) |
| **Databases** | RDS вместо self-managed PostgreSQL |
| **Development/staging** | Быстрое создание окружений |
| **Small teams** | Меньше ops работы |

### 3.5 Сравнение: Self-managed vs Managed Database

```python
# Self-managed PostgreSQL на EC2 (IaaS)
self_managed_tasks = [
    "Установка PostgreSQL",
    "Настройка postgresql.conf",
    "Настройка pg_hba.conf",
    "Создание backup стратегии",
    "Настройка репликации",
    "Мониторинг и алерты",
    "Патчинг PostgreSQL",
    "Патчинг ОС",
    "Расширение дисков",
    "Failover процедуры",
    "Security hardening"
]

# RDS PostgreSQL (PaaS)
rds_tasks = [
    "Выбор instance type",
    "Настройка parameter group",
    "Настройка backup retention",
    "Включение Multi-AZ (один клик)"
]

print(f"Self-managed: {len(self_managed_tasks)} задач")
print(f"RDS (PaaS): {len(rds_tasks)} задач")
print(f"Экономия времени: ~{100 - len(rds_tasks)/len(self_managed_tasks)*100:.0f}%")

```

**Output:**
```

Self-managed: 11 задач
RDS (PaaS): 4 задач
Экономия времени: ~64%

```

---

## 4. Software as a Service (SaaS)

### 4.1 Определение

**SaaS** — готовое программное обеспечение, доступное через интернет. Пользователь не управляет ничем, кроме своих данных и настроек приложения.

### 4.2 Примеры SaaS

```python

saas_examples = {
    "productivity": {
        "Google Workspace": "Docs, Sheets, Gmail",
        "Microsoft 365": "Word, Excel, Outlook",
        "Slack": "Team communication",
        "Zoom": "Video conferencing"
    },
    "crm_erp": {
        "Salesforce": "CRM platform",
        "HubSpot": "Marketing & Sales",
        "SAP": "Enterprise ERP"
    },
    "development": {
        "GitHub": "Code hosting & collaboration",
        "Jira": "Project management",
        "Datadog": "Monitoring & observability",
        "PagerDuty": "Incident management"
    },
    "aws_saas": {
        "AWS Console": "Cloud management UI",
        "AWS WorkMail": "Managed email",
        "Amazon Chime": "Video meetings",
        "Amazon QuickSight": "BI dashboards"
    }
}

print("SaaS — вы просто используете приложение:")
for category, apps in saas_examples.items():
    print(f"\n{category.upper().replace('_', '/')}:")
    for app, desc in list(apps.items())[:2]:
        print(f"  • {app}: {desc}")

```

**Output:**
```

SaaS — вы просто используете приложение:

PRODUCTIVITY:
  • Google Workspace: Docs, Sheets, Gmail
  • Microsoft 365: Word, Excel, Outlook

CRM/ERP:
  • Salesforce: CRM platform
  • HubSpot: Marketing & Sales

DEVELOPMENT:
  • GitHub: Code hosting & collaboration
  • Jira: Project management

AWS/SAAS:
  • AWS Console: Cloud management UI
  • AWS WorkMail: Managed email

```

### 4.3 Характеристики SaaS

```

┌────────────────────────────────────────────────────────────────┐
│                    SaaS Characteristics                         │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🌐 Accessed via browser                                       │
│     └── Нет установки, работает везде                          │
│                                                                 │
│  💳 Subscription model                                         │
│     └── Ежемесячная/годовая подписка                          │
│                                                                 │
│  🔄 Automatic updates                                          │
│     └── Провайдер обновляет для всех                          │
│                                                                 │
│  👥 Multi-tenant architecture                                  │
│     └── Один инстанс обслуживает много клиентов               │
│                                                                 │
│  📊 Built-in analytics                                         │
│     └── Готовые отчёты и дашборды                             │
│                                                                 │
│  🔌 API integrations                                           │
│     └── Возможность интеграции с другими системами            │
│                                                                 │
└────────────────────────────────────────────────────────────────┘

```

### 4.4 Когда использовать SaaS

| Use Case | Почему SaaS |
|----------|-------------|
| **Стандартные бизнес-процессы** | Email, CRM, HR — зачем изобретать велосипед |
| **Быстрый старт** | Регистрация → использование за минуты |
| **Нет IT-команды** | Не нужны специалисты для поддержки |
| **Предсказуемый бюджет** | Фиксированная цена за пользователя |
| **Compliance** | Провайдер обеспечивает сертификации |

---

## 5. Function as a Service (FaaS) / Serverless

### 5.1 Определение

**FaaS** — выполнение кода в ответ на события без управления серверами. Вы платите только за фактическое время выполнения функций.

### 5.2 AWS Lambda — главный FaaS сервис

```python
# AWS Lambda function example
import json
import boto3

def lambda_handler(event, context):
    """
    Простая Lambda функция, обрабатывающая HTTP запрос
    """
    # Получаем параметры из события
    name = event.get('queryStringParameters', {}).get('name', 'World')
    
    # Бизнес-логика
    message = f"Hello, {name}! From Lambda."
    
    # Возвращаем ответ
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': message,
            'function_name': context.function_name,
            'memory_limit': context.memory_limit_in_mb,
            'remaining_time_ms': context.get_remaining_time_in_millis()
        })
    }

```

### 5.3 Характеристики FaaS

```

┌────────────────────────────────────────────────────────────────┐
│                    FaaS / Serverless                            │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  💰 PAY-PER-USE                                                │
│     └── Оплата за: количество вызовов + время выполнения       │
│     └── AWS Lambda: $0.20 за 1M requests                       │
│     └── $0.0000166667 за GB-second                             │
│                                                                 │
│  📈 AUTO-SCALING                                               │
│     └── От 0 до тысяч concurrent executions                    │
│     └── Масштабирование происходит автоматически               │
│                                                                 │
│  ⚡ EVENT-DRIVEN                                                │
│     └── HTTP requests (API Gateway)                            │
│     └── S3 events (upload, delete)                             │
│     └── DynamoDB Streams                                       │
│     └── SQS messages                                           │
│     └── Scheduled (cron)                                       │
│                                                                 │
│  ⏱️ STATELESS                                                   │
│     └── Функция не хранит состояние между вызовами            │
│     └── Состояние — в DynamoDB, S3, ElastiCache               │
│                                                                 │
│  🧊 COLD START                                                 │
│     └── Первый вызов медленнее (инициализация)                │
│     └── Provisioned Concurrency решает проблему               │
│                                                                 │
└────────────────────────────────────────────────────────────────┘

```

### 5.4 Lambda vs EC2: сравнение стоимости

```python

def compare_lambda_ec2(
    requests_per_day: int,
    avg_duration_ms: int,
    memory_mb: int = 256
) -> dict:
    """
    Сравнение стоимости Lambda vs EC2 для одинаковой нагрузки
    """
    days_per_month = 30
    
    # Lambda pricing
    lambda_price_per_request = 0.0000002  # $0.20 per 1M
    lambda_price_per_gb_second = 0.0000166667
    
    monthly_requests = requests_per_day * days_per_month
    monthly_duration_seconds = (monthly_requests * avg_duration_ms) / 1000
    monthly_gb_seconds = monthly_duration_seconds * (memory_mb / 1024)
    
    lambda_cost = (
        monthly_requests * lambda_price_per_request +
        monthly_gb_seconds * lambda_price_per_gb_second
    )
    
    # EC2 pricing (t3.micro always on)
    ec2_hourly_rate = 0.0104  # t3.micro
    ec2_cost = ec2_hourly_rate * 24 * days_per_month
    
    return {
        "monthly_requests": monthly_requests,
        "lambda_cost": round(lambda_cost, 2),
        "ec2_cost": round(ec2_cost, 2),
        "winner": "Lambda" if lambda_cost < ec2_cost else "EC2",
        "savings": abs(round(lambda_cost - ec2_cost, 2))
    }

# Сценарий 1: Низкая нагрузка
low_traffic = compare_lambda_ec2(
    requests_per_day=1000,
    avg_duration_ms=100
)

# Сценарий 2: Высокая нагрузка
high_traffic = compare_lambda_ec2(
    requests_per_day=1_000_000,
    avg_duration_ms=100
)

print("=== Low Traffic (1K requests/day) ===")
print(f"Lambda: ${low_traffic['lambda_cost']}/month")
print(f"EC2 (t3.micro 24/7): ${low_traffic['ec2_cost']}/month")
print(f"Winner: {low_traffic['winner']}")

print("\n=== High Traffic (1M requests/day) ===")
print(f"Lambda: ${high_traffic['lambda_cost']}/month")
print(f"EC2 (t3.micro 24/7): ${high_traffic['ec2_cost']}/month")
print(f"Winner: {high_traffic['winner']}")

```

**Output:**
```

=== Low Traffic (1K requests/day) ===
Lambda: $0.01/month
EC2 (t3.micro 24/7): $7.49/month
Winner: Lambda

=== High Traffic (1M requests/day) ===
Lambda: $18.5/month
EC2 (t3.micro 24/7): $7.49/month
Winner: EC2

```

> **💡 Pro Tip:**  
> Lambda выгодна при низких и переменных нагрузках. При постоянной высокой нагрузке EC2 или Fargate могут быть дешевле.

### 5.5 Когда использовать FaaS

| Use Case | Почему FaaS |
|----------|-------------|
| **Event processing** | Обработка S3 uploads, DynamoDB streams |
| **APIs with variable traffic** | Стартапы, внутренние API |
| **Scheduled tasks** | Cron jobs, отчёты |
| **Webhooks** | GitHub/Stripe webhooks |
| **Data transformation** | ETL pipelines |
| **Chatbots** | Low-latency не критична |

---

## 6. Container as a Service (CaaS)

### 6.1 Определение

**CaaS** — запуск контейнеров без управления underlying инфраструктурой. Находится между IaaS и PaaS.

### 6.2 AWS Container Services

```python

aws_container_services = {
    "orchestration": {
        "ECS": {
            "description": "AWS-native container orchestration",
            "complexity": "Medium",
            "best_for": "AWS-first teams"
        },
        "EKS": {
            "description": "Managed Kubernetes",
            "complexity": "High",
            "best_for": "K8s expertise, multi-cloud"
        }
    },
    "compute": {
        "EC2": {
            "description": "Self-managed EC2 instances",
            "you_manage": "EC2 instances, scaling, patching",
            "cost": "Lower per-compute"
        },
        "Fargate": {
            "description": "Serverless containers",
            "you_manage": "Just containers",
            "cost": "Higher per-compute, zero ops"
        }
    },
    "registry": {
        "ECR": "Private container registry"
    }
}

print("Container Compute Options:")
for name, details in aws_container_services["compute"].items():
    print(f"\n{name}:")
    print(f"  {details['description']}")
    print(f"  You manage: {details['you_manage']}")

```

**Output:**
```

Container Compute Options:

EC2:
  Self-managed EC2 instances
  You manage: EC2 instances, scaling, patching

Fargate:
  Serverless containers
  You manage: Just containers

```

### 6.3 ECS Task Definition

```json

{
    "family": "my-web-app",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
    "containerDefinitions": [
        {
            "name": "web",
            "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 8080,
                    "protocol": "tcp"
                }
            ],
            "environment": [
                {
                    "name": "ENV",
                    "value": "production"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/my-web-app",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]
}

```

---

## 7. Everything as a Service (XaaS)

### 7.1 Обзор *aaS моделей

```

┌────────────────────────────────────────────────────────────────────┐
│                    XaaS: Everything as a Service                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  BaaS - Backend as a Service                                       │
│  └── AWS Amplify, Firebase — готовый backend для мобильных apps    │
│                                                                     │
│  DBaaS - Database as a Service                                     │
│  └── RDS, DynamoDB, MongoDB Atlas — managed databases              │
│                                                                     │
│  MaaS - Monitoring as a Service                                    │
│  └── Datadog, New Relic — observability platforms                  │
│                                                                     │
│  AIaaS - AI as a Service                                           │
│  └── AWS Bedrock, OpenAI API, SageMaker — ML models               │
│                                                                     │
│  NaaS - Network as a Service                                       │
│  └── AWS Transit Gateway, CloudFlare — managed networking          │
│                                                                     │
│  SECaaS - Security as a Service                                    │
│  └── AWS WAF, Shield, Crowdstrike — managed security              │
│                                                                     │
│  DRaaS - Disaster Recovery as a Service                            │
│  └── AWS Elastic Disaster Recovery                                 │
│                                                                     │
│  STaaS - Storage as a Service                                      │
│  └── S3, EBS, EFS — managed storage                               │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 7.2 Тренд: всё становится сервисом

```python

evolution_timeline = {
    "2006-2010": {
        "focus": "IaaS",
        "examples": ["EC2", "S3", "RDS"],
        "mindset": "Rent servers instead of buying"
    },
    "2011-2015": {
        "focus": "PaaS + Managed Services",
        "examples": ["Elastic Beanstalk", "DynamoDB", "Lambda (2014)"],
        "mindset": "Don't manage infrastructure"
    },
    "2016-2020": {
        "focus": "Serverless + Containers",
        "examples": ["Fargate", "Step Functions", "Aurora Serverless"],
        "mindset": "Focus only on code"
    },
    "2021+": {
        "focus": "AI/ML Services + Low-code",
        "examples": ["Bedrock", "SageMaker", "App Composer"],
        "mindset": "AI-assisted development"
    }
}

for period, data in evolution_timeline.items():
    print(f"\n{period}: {data['focus']}")
    print(f"  Mindset: {data['mindset']}")

```

**Output:**
```

2006-2010: IaaS
  Mindset: Rent servers instead of buying

2011-2015: PaaS + Managed Services
  Mindset: Don't manage infrastructure

2016-2020: Serverless + Containers
  Mindset: Focus only on code

2021+: AI/ML Services + Low-code
  Mindset: AI-assisted development

```

---

## 8. Shared Responsibility Model

### 8.1 Кто за что отвечает

```

┌────────────────────────────────────────────────────────────────────┐
│                AWS Shared Responsibility Model                      │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐    │
│  │                 CUSTOMER RESPONSIBILITY                    │    │
│  │              "Security IN the Cloud"                       │    │
│  ├───────────────────────────────────────────────────────────┤    │
│  │                                                            │    │
│  │  Customer Data                                             │    │
│  │  Platform, Applications, Identity & Access Management      │    │
│  │  Operating System, Network & Firewall Configuration        │    │
│  │  Client-side Data          Server-side          Networking │    │
│  │  Encryption                Encryption           Traffic    │    │
│  │                                                 Protection │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐    │
│  │                   AWS RESPONSIBILITY                       │    │
│  │              "Security OF the Cloud"                       │    │
│  ├───────────────────────────────────────────────────────────┤    │
│  │                                                            │    │
│  │  Software: Compute, Storage, Database, Networking          │    │
│  │  Hardware/AWS Global Infrastructure                        │    │
│  │  Regions, Availability Zones, Edge Locations               │    │
│  │                                                            │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 8.2 Ответственность по моделям сервисов

```python

responsibility_matrix = {
    "IaaS (EC2)": {
        "customer": [
            "Guest OS patching",
            "Application security",
            "Security groups",
            "Data encryption",
            "IAM",
            "Network configuration"
        ],
        "aws": [
            "Physical security",
            "Hypervisor",
            "Network infrastructure",
            "Storage infrastructure"
        ]
    },
    "PaaS (RDS)": {
        "customer": [
            "Database users & permissions",
            "Data encryption settings",
            "Security groups",
            "IAM"
        ],
        "aws": [
            "OS patching",
            "Database patching",
            "Backups (automated)",
            "High availability"
        ]
    },
    "FaaS (Lambda)": {
        "customer": [
            "Function code security",
            "IAM roles",
            "Data encryption"
        ],
        "aws": [
            "Everything else",
            "Runtime patching",
            "Scaling",
            "Availability"
        ]
    },
    "SaaS (WorkMail)": {
        "customer": [
            "User access management",
            "Data (emails)"
        ],
        "aws": [
            "Everything else"
        ]
    }
}

for model, resp in responsibility_matrix.items():
    customer_count = len(resp['customer'])
    aws_count = len(resp['aws'])
    print(f"\n{model}:")
    print(f"  Customer responsibilities: {customer_count}")
    print(f"  AWS responsibilities: {aws_count}")

```

**Output:**
```

IaaS (EC2):
  Customer responsibilities: 6
  AWS responsibilities: 4

PaaS (RDS):
  Customer responsibilities: 4
  AWS responsibilities: 4

FaaS (Lambda):
  Customer responsibilities: 3
  AWS responsibilities: 4

SaaS (WorkMail):
  Customer responsibilities: 2
  AWS responsibilities: 1

```

---

## 9. Выбор модели сервиса

### 9.1 Decision Tree

```

┌─────────────────────────────────────────────────────────────────┐
│                 Choosing a Service Model                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Нужен полный контроль над ОС?                                  │
│  │                                                               │
│  ├── ДА ───► IaaS (EC2)                                         │
│  │                                                               │
│  └── НЕТ ──► Нужно запускать контейнеры?                        │
│              │                                                   │
│              ├── ДА ───► CaaS (ECS/EKS + Fargate)               │
│              │                                                   │
│              └── НЕТ ──► Нагрузка event-driven?                 │
│                         │                                        │
│                         ├── ДА ───► FaaS (Lambda)               │
│                         │                                        │
│                         └── НЕТ ──► Web app?                    │
│                                     │                            │
│                                     ├── ДА ───► PaaS (Beanstalk)│
│                                     │                            │
│                                     └── НЕТ ──► SaaS?           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

```

### 9.2 Сравнительная таблица

| Критерий | IaaS | PaaS | FaaS | SaaS |
|----------|------|------|------|------|
| **Контроль** | Максимальный | Средний | Минимальный | Нет |
| **Ops работа** | Много | Средне | Мало | Нет |
| **Скорость старта** | Медленно | Быстро | Очень быстро | Мгновенно |
| **Гибкость** | Максимум | Ограничена | Ограничена | Минимум |
| **Lock-in** | Низкий | Средний | Высокий | Максимальный |
| **Стоимость при низкой нагрузке** | Высокая | Средняя | Очень низкая | Фиксированная |

### 9.3 Реальные сценарии

```python

scenarios = {
    "Стартап MVP": {
        "recommendation": "Lambda + API Gateway + DynamoDB",
        "why": "Минимум ops, pay-per-use, быстрый старт",
        "model": "FaaS + DBaaS"
    },
    "Enterprise migration": {
        "recommendation": "EC2 + RDS",
        "why": "Lift-and-shift, минимум изменений в коде",
        "model": "IaaS + PaaS"
    },
    "Microservices": {
        "recommendation": "EKS/ECS + Fargate",
        "why": "Контейнеры, оркестрация, serverless compute",
        "model": "CaaS"
    },
    "Data processing": {
        "recommendation": "Lambda + S3 + Athena",
        "why": "Event-driven, масштабируемость, serverless analytics",
        "model": "FaaS + STaaS"
    },
    "Email для компании": {
        "recommendation": "AWS WorkMail или Google Workspace",
        "why": "Зачем управлять email серверами?",
        "model": "SaaS"
    }
}

for scenario, details in scenarios.items():
    print(f"\n📋 {scenario}")
    print(f"   Model: {details['model']}")
    print(f"   Services: {details['recommendation']}")

```

**Output:**
```

📋 Стартап MVP
   Model: FaaS + DBaaS
   Services: Lambda + API Gateway + DynamoDB

📋 Enterprise migration
   Model: IaaS + PaaS
   Services: EC2 + RDS

📋 Microservices
   Model: CaaS
   Services: EKS/ECS + Fargate

📋 Data processing
   Model: FaaS + STaaS
   Services: Lambda + S3 + Athena

📋 Email для компании
   Model: SaaS
   Services: AWS WorkMail или Google Workspace

```

---

## 10. Common Pitfalls

### 10.1 Pitfall: Выбор IaaS "по привычке"

❌ **Проблема:**
```bash
# "У нас всегда был PostgreSQL на серверах, давайте так же в облаке"
aws ec2 run-instances ... # Установим PostgreSQL сами!

# Результат:
# - Команда тратит время на ops работу
# - Нет автоматических backup
# - Нет Multi-AZ failover
# - Патчинг на нас
```

✅ **Решение:**
```bash
# Используйте RDS PostgreSQL
aws rds create-db-instance \
    --db-instance-identifier mydb \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username admin \
    --master-user-password xxx \
    --multi-az \
    --backup-retention-period 7

# Автоматически:
# - Backup каждый день
# - Multi-AZ failover
# - Патчинг PostgreSQL и ОС
```

### 10.2 Pitfall: Lambda для всего

❌ **Проблема:**
```python
# "Lambda serverless — используем везде!"

# Проблема 1: Long-running процессы
def process_video(event, context):
    # Lambda timeout: 15 минут максимум!
    # Обработка видео может занять часы
    pass

# Проблема 2: Постоянная высокая нагрузка
# Lambda дорогая при 24/7 нагрузке
```

✅ **Решение:**
```python
# Для long-running: ECS/Fargate или Step Functions

# Для high-traffic: EC2 или Fargate
# Lambda: для event-driven и variable traffic

use_cases = {
    "Lambda": ["API < 1M req/day", "S3 triggers", "scheduled tasks"],
    "Fargate": ["Web apps", "background workers", "steady traffic"],
    "EC2": ["High performance", "GPU", "custom OS"]
}

```

---

## 💡 Key Takeaways

- **IaaS** (EC2) — максимальный контроль, но и максимум ops работы

- **PaaS** (Beanstalk, RDS) — баланс контроля и удобства

- **FaaS** (Lambda) — pay-per-use, идеален для event-driven

- **SaaS** — готовые решения, минимум управления

- **Shared Responsibility** — чем выше уровень абстракции, тем меньше ваших обязанностей
- Выбор модели зависит от: требований к контролю, экспертизы команды, характера нагрузки

---

## 🚀 Next Steps

**Следующие модули:**

- [Cloud Architecture](../03_Architecture/) — регионы, AZ, глобальная инфраструктура
- [IAM](../04_IAM/) — управление доступом

**Практические задания:**

1. Разверните простое приложение на Elastic Beanstalk
2. Создайте Lambda функцию через консоль
3. Сравните время развёртывания EC2 vs Beanstalk
4. Изучите AWS Free Tier для каждой модели

**Для углубления:**

- Изучите AWS App Runner как альтернативу Beanstalk
- Попробуйте Fargate для контейнеров
- Исследуйте AWS Amplify для mobile/web приложений

---

## 📚 Additional Resources

**Documentation:**

- [AWS Service Categories](https://aws.amazon.com/products/) — каталог сервисов
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

**Articles:**

- [IaaS vs PaaS vs SaaS](https://aws.amazon.com/types-of-cloud-computing/)
- [When to use Lambda vs EC2](https://aws.amazon.com/lambda/resources/)

**Videos:**

- [AWS re:Invent: Choosing the Right Compute](https://www.youtube.com/watch?v=dPdac4LL884)

---




