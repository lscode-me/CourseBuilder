# Cloud Native Development
## От облачных вычислений к современной архитектуре приложений

---

## 📚 О курсе

Этот курс охватывает все аспекты разработки приложений для облака — от базовых концепций облачных вычислений до продвинутых паттернов Cloud Native архитектуры. Курс построен на примере AWS как наиболее зрелой облачной платформы, но принципы применимы к любому облаку.

### Целевая аудитория

- Backend-разработчики, переходящие в облачную разработку
- DevOps-инженеры, желающие глубже понять облачные сервисы
- Архитекторы, проектирующие облачные решения
- Team Leads, принимающие технические решения
- Все, кто хочет понимать современную облачную инфраструктуру

### Предварительные требования

- Опыт разработки на любом языке программирования
- Базовое понимание сетей (TCP/IP, HTTP, DNS)
- Знакомство с Linux/Unix командной строкой
- Понимание основ баз данных (SQL)
- Желательно: опыт работы с Docker

---

## 🗺️ Структура курса

### Раздел 1: Основы облачных вычислений

| Модуль | Тема | Описание |
|--------|------|----------|
| [01_Intro](./01_Intro/) | Введение в облака | История, эволюция, зачем нужны облака, основные провайдеры |
| [02_ServiceModels](./02_ServiceModels/) | Модели сервисов | IaaS, PaaS, SaaS, FaaS, *aaS — что выбрать и когда |
| [03_Architecture](./03_Architecture/) | Архитектура облаков | Регионы, Availability Zones, Edge Locations, глобальная инфраструктура |

### Раздел 2: Базовые сервисы AWS

| Модуль | Тема | Описание |
|--------|------|----------|
| [04_IAM](./04_IAM/) | Identity & Access Management | Пользователи, роли, политики, SSO, Federation, OIDC |
| [05_EC2](./05_EC2/) | Elastic Compute Cloud | Инстансы, типы, AMI, EBS, Auto Scaling, Spot/Reserved |
| [06_S3](./06_S3/) | Simple Storage Service | Buckets, классы хранения, lifecycle, версионирование, безопасность |
| [07_VPC](./07_VPC/) | Virtual Private Cloud | Сети, подсети, маршрутизация, NAT, Security Groups, NACLs |
| [08_RDS](./08_RDS/) | Relational Database Service | Движки БД, Multi-AZ, Read Replicas, Aurora, резервное копирование |

### Раздел 3: Расширенные сервисы

| Модуль | Тема | Описание |
|--------|------|----------|
| [09_DynamoDB](./09_DynamoDB/) | NoSQL база данных | Модель данных, ключи, индексы, DAX, DynamoDB Streams |
| [10_Lambda](./10_Lambda/) | Serverless вычисления | Функции, триггеры, слои, холодный старт, лимиты |
| [11_Containers](./11_Containers/) | Контейнеры в облаке | ECS, EKS, Fargate, ECR, оркестрация |
| [12_Messaging](./12_Messaging/) | Очереди и события | SQS, SNS, EventBridge, паттерны интеграции |
| [13_APIGateway](./13_APIGateway/) | API Gateway | REST API, HTTP API, WebSocket, авторизация, throttling |
| [14_CDN](./14_CDN/) | CloudFront и Edge | CDN, Edge Locations, Lambda@Edge, кеширование |
| [15_DataServices](./15_DataServices/) | Аналитика данных | Redshift, Athena, Kinesis, Glue, озёра данных |

### Раздел 4: Инфраструктура и автоматизация

| Модуль | Тема | Описание |
|--------|------|----------|
| [16_IaC](./16_IaC/) | Infrastructure as Code | CloudFormation, Terraform, CDK, Pulumi — сравнение и практика |
| [17_CICD](./17_CICD/) | CI/CD в облаке | CodeCommit, CodeBuild, CodePipeline, CodeDeploy |

### Раздел 5: Cloud Native Development

| Модуль | Тема | Описание |
|--------|------|----------|
| [18_CloudNativeIntro](./18_CloudNativeIntro/) | Введение в Cloud Native | CNCF, принципы, отличия от традиционной разработки |
| [19_TwelveFactorApp](./19_TwelveFactorApp/) | The Twelve-Factor App | 12 принципов современных приложений с примерами |
| [20_Microservices](./20_Microservices/) | Микросервисы в облаке | Паттерны, коммуникация, service mesh, API design |
| [21_Observability](./21_Observability/) | Наблюдаемость | CloudWatch, X-Ray, логирование, метрики, трейсы |

### Раздел 6: Продвинутые темы

| Модуль | Тема | Описание |
|--------|------|----------|
| [22_Security](./22_Security/) | Безопасность в облаке | Shared Responsibility, шифрование, WAF, Shield, best practices |
| [23_CostManagement](./23_CostManagement/) | Управление затратами | Cost Explorer, Budgets, Reserved/Spot, оптимизация |
| [24_MultiCloud](./24_MultiCloud/) | Multi-cloud стратегии | Cloud Agnostic, абстракции, когда это нужно |
| [25_CaseStudies](./25_CaseStudies/) | Практические кейсы | Реальные архитектуры, разбор решений, anti-patterns |

---

## 🎯 Learning Path

```

┌─────────────────────────────────────────────────────────────────────┐
│                    Cloud Native Development                          │
└─────────────────────────────────────────────────────────────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
    ┌──────────┐          ┌──────────┐          ┌──────────┐
    │  Intro   │─────────▶│ Service  │─────────▶│  Cloud   │
    │  Cloud   │          │  Models  │          │   Arch   │
    └──────────┘          └──────────┘          └──────────┘
                                │
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
┌────────┐    ┌────────┐   ┌────────┐   ┌────────┐    ┌────────┐
│  IAM   │───▶│  EC2   │──▶│   S3   │──▶│  VPC   │───▶│  RDS   │
└────────┘    └────────┘   └────────┘   └────────┘    └────────┘
                                │
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
┌────────┐    ┌────────┐   ┌────────┐   ┌────────┐    ┌────────┐
│Dynamo  │───▶│ Lambda │──▶│Contain-│──▶│Messag- │───▶│  API   │
│  DB    │    │        │   │  ers   │   │  ing   │    │Gateway │
└────────┘    └────────┘   └────────┘   └────────┘    └────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
         ┌─────────┐      ┌──────────┐     ┌──────────┐
         │   CDN   │─────▶│  Data    │────▶│   IaC    │
         │         │      │ Services │     │          │
         └─────────┘      └──────────┘     └──────────┘
                                │
                                ▼
                          ┌──────────┐
                          │  CI/CD   │
                          └──────────┘
                                │
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
┌────────────┐          ┌──────────────┐          ┌────────────┐
│Cloud Native│─────────▶│ 12-Factor    │─────────▶│Microservic-│
│   Intro    │          │    App       │          │    es      │
└────────────┘          └──────────────┘          └────────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │ Observability│
                        └──────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
    ┌──────────┐          ┌──────────┐          ┌──────────┐
    │ Security │─────────▶│   Cost   │─────────▶│  Multi-  │
    │          │          │ Managmnt │          │  Cloud   │
    └──────────┘          └──────────┘          └──────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │ Case Studies │
                        └──────────────┘
```

---

## 📋 Ключевые темы по модулям

| Модуль | Ключевые концепции |
|--------|-------------------|
| Intro | История AWS/GCP/Azure, on-premise vs cloud, TCO |
| ServiceModels | IaaS, PaaS, SaaS, FaaS, Shared Responsibility |
| Architecture | Regions, AZs, Edge, Global Accelerator, PoPs |
| IAM | Users, Groups, Roles, Policies, STS, OIDC, SAML |
| EC2 | Instance types, AMI, EBS, Auto Scaling, Placement Groups |
| S3 | Storage classes, Lifecycle, Versioning, Replication |
| VPC | CIDR, Subnets, Route Tables, IGW, NAT, VPN, Peering |
| RDS | Engines, Multi-AZ, Read Replicas, Aurora, Snapshots |
| DynamoDB | Partition/Sort keys, GSI/LSI, DAX, Streams |
| Lambda | Handlers, Triggers, Layers, Concurrency, Destinations |
| Containers | ECS Tasks/Services, EKS, Fargate, Service Discovery |
| Messaging | SQS FIFO/Standard, SNS Topics, EventBridge Rules |
| APIGateway | REST vs HTTP API, Authorizers, Stages, Caching |
| CDN | Distributions, Behaviors, Origins, Lambda@Edge |
| DataServices | Data Lake, ETL, Streaming, Analytics |
| IaC | Declarative, State, Modules, Drift Detection |
| CICD | Pipelines, Build Specs, Deploy Strategies |
| CloudNativeIntro | CNCF Trail Map, Cloud Native Patterns |
| TwelveFactorApp | Codebase, Dependencies, Config, Backing Services... |
| Microservices | Decomposition, Communication, Resilience |
| Observability | Logs, Metrics, Traces, Correlation, Alerting |
| Security | Encryption, KMS, Secrets Manager, WAF, GuardDuty |
| CostManagement | RI, Savings Plans, Spot, Right-sizing, Budgets |
| MultiCloud | Abstraction layers, Kubernetes, Terraform |
| CaseStudies | Real architectures, Trade-offs, Lessons learned |

---

## 📋 Формат модуля

Каждый модуль содержит:

```

XX_ModuleName/
├── lecture.md    # Основной материал лекции
└── quiz.md       # Вопросы для самопроверки (15-20 вопросов)
```

### Структура лекции

- **Prerequisites** — что нужно знать перед началом

- **Learning Objectives** — цели обучения (3-5 пунктов)

- **Историческая справка** — как появился сервис/концепция

- **Основной материал** — теория с практическими примерами

- **Hands-on примеры** — CLI команды, код, конфигурации

- **Best Practices** — рекомендации от AWS и сообщества

- **Common Pitfalls** — типичные ошибки и как их избежать

- **Key Takeaways** — главные выводы (3-5 пунктов)

- **Next Steps** — что изучить дальше

- **Additional Resources** — документация, статьи, видео

---

## ⏱️ Время прохождения

| Раздел | Модули | Время чтения | Время практики |
|--------|--------|--------------|----------------|
| Основы облаков | 1-3 | 3-4 часа | 1-2 часа |
| Базовые сервисы | 4-8 | 6-8 часов | 8-10 часов |
| Расширенные сервисы | 9-15 | 8-10 часов | 10-12 часов |
| Инфраструктура | 16-17 | 3-4 часа | 4-5 часов |
| Cloud Native | 18-21 | 5-6 часов | 4-5 часов |
| Продвинутые темы | 22-25 | 5-6 часов | 3-4 часа |

**Общее время:** ~70-85 часов (включая практику)

---

## 🎓 После прохождения курса

Вы будете уметь:

✅ Понимать архитектуру и сервисы современных облаков

✅ Выбирать правильную модель сервиса (IaaS/PaaS/SaaS/FaaS)

✅ Проектировать безопасную сетевую инфраструктуру (VPC)

✅ Настраивать IAM с принципом наименьших привилегий

✅ Работать с compute-сервисами (EC2, Lambda, Containers)

✅ Проектировать системы хранения (S3, EBS, EFS)

✅ Выбирать и настраивать базы данных (RDS, DynamoDB)

✅ Строить event-driven архитектуры (SQS, SNS, EventBridge)

✅ Создавать и управлять API (API Gateway)

✅ Описывать инфраструктуру как код (Terraform, CloudFormation)

✅ Применять принципы 12-Factor App

✅ Проектировать микросервисные архитектуры

✅ Настраивать observability (логи, метрики, трейсы)

✅ Обеспечивать безопасность облачных приложений

✅ Оптимизировать затраты на облако

---

## 📚 Рекомендуемые книги

### Облачная архитектура

- **"Designing Data-Intensive Applications"** by Martin Kleppmann — архитектура данных

- **"Cloud Native Patterns"** by Cornelia Davis — паттерны Cloud Native

- **"Building Microservices"** by Sam Newman — микросервисная архитектура

### AWS специфичные

- **"AWS Certified Solutions Architect Study Guide"** — подготовка к сертификации

- **"Amazon Web Services in Action"** by Wittig & Wittig — практическое руководство

- **"Serverless Architectures on AWS"** by Peter Sbarski — serverless паттерны

### Практика

- **"Infrastructure as Code"** by Kief Morris — IaC паттерны

- **"The Twelve-Factor App"** (https://12factor.net) — обязательное чтение

- **"Release It!"** by Michael Nygard — паттерны надёжных систем

### Безопасность

- **"AWS Security"** by Dylan Shields — безопасность в AWS

- **"Cloud Security and Privacy"** by Tim Mather — общие принципы

---

## 🛠️ Инструменты курса

### CLI и SDK

- AWS CLI v2
- AWS SDK (Python boto3, Node.js, Go)
- Terraform CLI

### Локальная разработка

- LocalStack (эмуляция AWS локально)
- SAM CLI (Serverless Application Model)
- Docker

### Мониторинг и отладка

- AWS CloudWatch
- AWS X-Ray
- CloudWatch Logs Insights

### IDE и расширения

- VS Code + AWS Toolkit
- IntelliJ + AWS Toolkit

---

## 🏆 Сертификации

Курс готовит к сдаче:

- **AWS Certified Cloud Practitioner** (базовый уровень)

- **AWS Certified Solutions Architect – Associate** (средний уровень)

- **AWS Certified Developer – Associate** (средний уровень)

---

## 📝 Версия и обновления

**Версия:** 1.0  
**Дата создания:** Декабрь 2024  
**Последнее обновление:** Декабрь 2024

Курс поддерживается в актуальном состоянии. AWS регулярно обновляет сервисы — мы отслеживаем важные изменения.

---


