# Облачные вычисления и датацентры
## От серверов под столом к глобальной инфраструктуре

---

## 📋 Prerequisites

- Понимание виртуализации
- Базовые знания о сетях
- Представление о современных архитектурах

**Recommended prior modules:**
- [17_Networks](../17_Networks/)
- [11_VirtualMachines](../16_VirtualMachines/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять концепцию облачных вычислений и их преимущества
- Понимать архитектуру датацентров
- Анализировать различия между IaaS, PaaS, SaaS
- Различать контейнеризацию и виртуализацию
- Понимать serverless computing

---

## 1. Что такое облако

### 1.1 Определение

**Cloud Computing** — предоставление вычислительных ресурсов через интернет

**Ключевые характеристики (NIST):**
1. **On-demand self-service:** Пользователь сам создаёт ресурсы
2. **Broad network access:** Доступ из любого места
3. **Resource pooling:** Ресурсы shared между клиентами
4. **Rapid elasticity:** Масштабирование за минуты
5. **Measured service:** Оплата за использование

### 1.2 Преимущества облака

**Для бизнеса:**
- CapEx → OpEx (покупка → аренда)
- Быстрое масштабирование
- Глобальное присутствие
- Меньше инфраструктурных проблем

**Trade-offs:**
- Vendor lock-in
- Latency
- Privacy/security concerns
- Долгосрочно может быть дороже

---

## 2. Модели обслуживания

### 2.1 IaaS (Infrastructure as a Service)

**Что предоставляется:** Виртуальные машины, сети, storage

**Примеры:**
- AWS EC2
- Azure Virtual Machines
- Google Compute Engine

**Контроль пользователя:**
```
[User управляет]
  ↓ Operating System
  ↓ Applications
  ↓ Data
[Provider управляет]
  ↓ Virtualization
  ↓ Servers
  ↓ Storage
  ↓ Networking
```

### 2.2 PaaS (Platform as a Service)

**Что предоставляется:** Платформа для разработки и деплоя

**Примеры:**
- Heroku
- Google App Engine
- Azure App Service

**Контроль:**
```
[User]
  ↓ Applications
  ↓ Data
[Provider]
  ↓ Runtime
  ↓ OS
  ↓ Infrastructure
```

### 2.3 SaaS (Software as a Service)

**Что предоставляется:** Готовые приложения

**Примеры:**
- Gmail, Office 365
- Salesforce
- Dropbox

**Контроль:**
```
[User]
  ↓ Data
[Provider]
  ↓ Everything else
```

---

## 3. Архитектура датацентра

### 3.1 Физическая структура

**Типичный датацентр:**

```
Building
├── Cooling Systems (огромные кондиционеры)
├── Power (резервные генераторы, UPS)
├── Rows of Racks
│   ├── Top of Rack (ToR) Switch
│   ├── Servers (40-50 на rack)
│   │   ├── CPU (2x Xeon/EPYC)
│   │   ├── RAM (256-512 GB)
│   │   ├── Storage (SSD/NVMe)
│   │   └── Network (10-100 Gbps)
└── Security (biometrics, guards)
```

### 3.2 Network Topology

**Three-tier архитектура:**

```
Core Routers (internet connectivity)
    ↓
Aggregation Switches
    ↓
Top of Rack Switches
    ↓
Servers
```

**Современность: Spine-Leaf (Clos network):**
- Меньше latency
- Лучше для east-west traffic (server-to-server)

### 3.3 Энергопотребление

**PUE (Power Usage Effectiveness):**
```
PUE = Total Power / IT Equipment Power
```

- Плохо: PUE = 2.0 (50% на охлаждение, overhead)
- Хорошо: PUE = 1.2 (Google, Facebook)
- Идеал: PUE = 1.0 (невозможен)

**Охлаждение:**
- Air cooling
- Liquid cooling
- Free cooling (использование наружного воздуха)

---

## 4. Виртуализация и контейнеры

### 4.1 Виртуальные машины

**Hypervisor:**

**Type 1 (Bare-metal):**
```
Hardware
  ↓
Hypervisor (ESXi, Hyper-V, KVM)
  ↓
VM1     VM2     VM3
(Guest OS на каждой)
```

**Type 2 (Hosted):**
```
Hardware
  ↓
Host OS
  ↓
Hypervisor (VMware Workstation, VirtualBox)
  ↓
VM1     VM2
```

**Overhead:**
- Каждая VM = полная OS
- Больше памяти, медленнее старт

### 4.2 Контейнеры (Docker)

**Идея:** Изоляция на уровне процессов, не отдельные OS

```
Hardware
  ↓
Host OS (Linux)
  ↓
Container Runtime (Docker, containerd)
  ↓
Container1  Container2  Container3
(shared kernel!)
```

**Преимущества:**
- Лёгкие (МБ vs ГБ для VM)
- Быстрый старт (секунды vs минуты)
- Higher density (больше контейнеров на сервер)

**Недостатки:**
- Меньше изоляции, чем VM
- Только Linux (хотя Windows поддержка есть)

### 4.3 Kubernetes

**Orchestration platform для контейнеров:**

**Задачи:**
- Scheduling (какой контейнер на каком узле)
- Load balancing
- Auto-scaling
- Self-healing (перезапуск упавших)
- Rolling updates

**Стал de-facto стандартом для cloud-native apps**

---

## 5. Serverless Computing

### 5.1 Концепция

**Serverless ≠ без серверов**  
Серверы есть, но вы о них не думаете.

**Function as a Service (FaaS):**
- Вы пишете функцию
- Provider запускает её по событию
- Оплата за execution time (миллисекунды!)

**Примеры:**
- AWS Lambda
- Azure Functions
- Google Cloud Functions

### 5.2 Характеристики

**Event-driven:**
```
HTTP request → Lambda function
S3 upload → Process image
Database change → Update cache
```

**Stateless:**
- Функция не хранит состояние между вызовами
- State в databases, caches

**Автомасштабирование:**
- 0 requests → 0 running instances (экономия)
- 10,000 requests → 10,000 instances (масштаб)

### 5.3 Trade-offs

**Плюсы:**
- Нет управления серверами
- Автоматическое масштабирование
- Оплата за использование

**Минусы:**
- Cold start (первый запуск медленный)
- Ограничения (timeout, memory)
- Vendor lock-in
- Сложность debugging

---

## 6. Объектные хранилища

### 6.1 S3 Model

**Key-Value store для файлов:**

```
Bucket: my-photos
  Key: "vacation/IMG_001.jpg" → Object (binary data)
  Key: "vacation/IMG_002.jpg" → Object
```

**Не filesystem:**
- Нет иерархии (ключи могут выглядеть как пути, но это просто строки)
- Нет POSIX операций (rename, append)

**Преимущества:**
- Unlimited scale
- Durability (11 девяток: 99.999999999%)
- HTTP API

### 6.2 CDN (Content Delivery Network)

**Идея:** Кэшировать статику близко к пользователям

```
User (Москва) → Edge location (Москва) → Origin (US East)
                ↑
         Кэшируется локально
```

**Примеры:**
- CloudFront (AWS)
- Cloudflare
- Akamai

---

## 7. Гибридное и мультиоблако

### 7.1 Hybrid Cloud

**Комбинация on-premise + cloud:**

```
On-Premise DC ←→ Public Cloud
(sensitive data)  (burst capacity)
```

**Применение:**
- Compliance requirements
- Legacy systems
- Cost optimization

### 7.2 Multi-Cloud

**Использование нескольких провайдеров:**

```
AWS (compute) + Azure (databases) + GCP (ML)
```

**Причины:**
- Избежать vendor lock-in
- Best-of-breed подход
- Redundancy

**Сложности:**
- Управление
- Интеграция
- Expertise в нескольких платформах

---

## 💡 Key Takeaways

- **Облако** — не про технологию, а про модель предоставления услуг (on-demand, self-service, pay-as-you-go)
- **IaaS/PaaS/SaaS** — разные уровни абстракции и контроля
- **Контейнеры** легче VM, но VM предоставляют сильнее изоляцию
- **Serverless** упрощает разработку, но имеет ограничения
- **Датацентры** — огромные инвестиции в infrastructure, энергопотребление, охлаждение

---

## 🚀 Next Steps

- [26_ModernComputing](../26_ModernComputing/) — Как облако встраивается в современную картину
- [27_FutureTrends](../27_FutureTrends/) — Будущее облачных вычислений

---

## 📚 Additional Resources

- **"Designing Data-Intensive Applications"** — Martin Kleppmann (distributed systems)
- **"Site Reliability Engineering"** — Google (SRE practices)
- AWS/Azure/GCP documentation

---
