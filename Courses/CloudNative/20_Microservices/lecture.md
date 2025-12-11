# Микросервисная архитектура

---

## 📋 Prerequisites

- Понимание Cloud Native принципов
- Знакомство с 12-Factor App
- Опыт разработки web-приложений

---

## 🎯 Learning Objectives

- Понимать преимущества и недостатки микросервисов
- Проектировать границы сервисов
- Выбирать паттерны коммуникации
- Применять паттерны отказоустойчивости

---

## 1. Монолит vs Микросервисы

### 1.1 Сравнение

```

┌────────────────────────────────────────────────────────────────────┐
│              Monolith vs Microservices                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  MONOLITH                        MICROSERVICES                     │
│  ────────                        ─────────────                     │
│  ┌──────────────────┐           ┌─────┐ ┌─────┐ ┌─────┐          │
│  │                  │           │ Svc │ │ Svc │ │ Svc │          │
│  │   All features   │           │  A  │ │  B  │ │  C  │          │
│  │   in one app     │           └──┬──┘ └──┬──┘ └──┬──┘          │
│  │                  │              │       │       │              │
│  │  ┌────────────┐  │              ▼       ▼       ▼              │
│  │  │  Single    │  │           ┌────┐  ┌────┐  ┌────┐           │
│  │  │  Database  │  │           │ DB │  │ DB │  │ DB │           │
│  │  └────────────┘  │           │  A │  │  B │  │  C │           │
│  │                  │           └────┘  └────┘  └────┘           │
│  └──────────────────┘                                             │
│                                                                     │
│  Pros:                          Pros:                              │
│  • Simple deployment            • Independent deployment           │
│  • Simple debugging             • Technology diversity             │
│  • No network overhead          • Scalability per service          │
│  • ACID transactions            • Team autonomy                    │
│                                                                     │
│  Cons:                          Cons:                              │
│  • Scaling is all-or-nothing   • Distributed complexity           │
│  • Tight coupling              • Network latency                   │
│  • Long deployment cycles      • Data consistency challenges       │
│  • Technology lock-in          • Operational overhead              │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 1.2 Когда выбирать микросервисы

```python

microservices_indicators = {
    "good_fit": [
        "Большая команда (можно разделить на squad'ы)",
        "Разные части системы требуют разного масштабирования",
        "Нужна технологическая гибкость",
        "Частые независимые релизы",
        "Bounded Contexts чётко определены (DDD)"
    ],
    "bad_fit": [
        "Маленькая команда (< 5 человек)",
        "Startup/MVP стадия",
        "Нет DevOps культуры и инструментов",
        "Домен плохо понят",
        "Tight deadlines"
    ]
}

print("Microservices Good Fit:")
for case in microservices_indicators['good_fit']:
    print(f"  ✅ {case}")

print("\nMicroservices Bad Fit:")
for case in microservices_indicators['bad_fit']:
    print(f"  ❌ {case}")

```

---

## 2. Проектирование сервисов

### 2.1 Domain-Driven Design

```

┌────────────────────────────────────────────────────────────────────┐
│              Bounded Contexts → Microservices                       │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  E-commerce Domain                                                 │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                                                              │  │
│  │  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │  │
│  │  │   Catalog    │   │    Order     │   │   Shipping   │    │  │
│  │  │   Context    │   │   Context    │   │   Context    │    │  │
│  │  │              │   │              │   │              │    │  │
│  │  │ • Products   │   │ • Orders     │   │ • Shipments  │    │  │
│  │  │ • Categories │   │ • Cart       │   │ • Tracking   │    │  │
│  │  │ • Inventory  │   │ • Payments   │   │ • Carriers   │    │  │
│  │  │              │   │              │   │              │    │  │
│  │  └──────────────┘   └──────────────┘   └──────────────┘    │  │
│  │         │                  │                  │             │  │
│  │         ▼                  ▼                  ▼             │  │
│  │  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │  │
│  │  │ Catalog Svc  │   │  Order Svc   │   │ Shipping Svc │    │  │
│  │  │   + DB       │   │    + DB      │   │    + DB      │    │  │
│  │  └──────────────┘   └──────────────┘   └──────────────┘    │  │
│  │                                                              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Each Bounded Context = potential Microservice                     │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 2.2 Размер сервиса

```python

service_sizing_guidelines = {
    "too_small": {
        "signs": ["1-2 API endpoints", "Очень частая коммуникация с другими сервисами"],
        "problem": "Overhead превышает пользу, distributed monolith"
    },
    "right_size": {
        "signs": ["Один bounded context", "Одна команда владеет сервисом",
                  "Независимые релизы", "Минимальные зависимости"],
        "metrics": "2-pizza team (6-8 человек) может поддерживать"
    },
    "too_large": {
        "signs": ["Много команд работают над одним сервисом", 
                  "Частые merge conflicts", "Координация релизов"],
        "problem": "Distributed monolith, теряются преимущества"
    }
}

```

---

## 3. Коммуникация между сервисами

### 3.1 Синхронная vs Асинхронная

```

┌────────────────────────────────────────────────────────────────────┐
│              Communication Patterns                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SYNCHRONOUS (Request/Response)                                    │
│  ─────────────────────────────                                     │
│  ┌────────┐  HTTP/gRPC  ┌────────┐                                │
│  │Service │────────────►│Service │                                │
│  │   A    │◄────────────│   B    │                                │
│  └────────┘   Response  └────────┘                                │
│                                                                     │
│  Pros: Simple, immediate response                                  │
│  Cons: Tight coupling, cascading failures, latency                 │
│  AWS: API Gateway, ALB, App Mesh                                   │
│                                                                     │
│  ASYNCHRONOUS (Event-Driven)                                       │
│  ──────────────────────────                                        │
│  ┌────────┐  Publish   ┌────────┐  Subscribe  ┌────────┐         │
│  │Service │───────────►│ Event  │◄────────────│Service │         │
│  │   A    │            │  Bus   │             │   B    │         │
│  └────────┘            └────────┘             └────────┘         │
│                                                                     │
│  Pros: Loose coupling, resilience, scalability                    │
│  Cons: Eventual consistency, complexity, debugging                 │
│  AWS: SQS, SNS, EventBridge, Kinesis                              │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 3.2 API Design

```python
# REST API conventions
api_design = {
    "resources": {
        "GET /orders": "List orders",
        "GET /orders/{id}": "Get order by ID",
        "POST /orders": "Create order",
        "PUT /orders/{id}": "Update order",
        "DELETE /orders/{id}": "Delete order"
    },
    "versioning": {
        "url_path": "/v1/orders",
        "header": "Accept: application/vnd.myapi.v1+json",
        "query": "/orders?version=1"
    },
    "pagination": {
        "example": "GET /orders?page=2&limit=20",
        "response": {"data": [], "meta": {"page": 2, "total": 100}}
    }
}

# gRPC для внутренней коммуникации
# Преимущества: быстрее REST, typed contracts, streaming
```

---

## 4. Паттерны отказоустойчивости

### 4.1 Circuit Breaker

```python

from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open" # Testing if recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=30):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.state = CircuitState.CLOSED
        self.last_failure_time = None
    
    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

```

### 4.2 Другие паттерны

```

┌────────────────────────────────────────────────────────────────────┐
│              Resilience Patterns                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  RETRY                                                             │
│  └── Повтор запроса при transient failures                        │
│  └── Exponential backoff: 1s, 2s, 4s, 8s...                       │
│                                                                     │
│  TIMEOUT                                                           │
│  └── Не ждать ответ вечно                                         │
│  └── Fail fast, освобождай ресурсы                                │
│                                                                     │
│  BULKHEAD                                                          │
│  └── Изоляция ресурсов (отдельные connection pools)               │
│  └── Сбой одного сервиса не затрагивает другие                    │
│                                                                     │
│  FALLBACK                                                          │
│  └── Альтернативный ответ при сбое                                │
│  └── Cached data, default values, degraded service                │
│                                                                     │
│  RATE LIMITING                                                     │
│  └── Защита от перегрузки                                         │
│  └── Token bucket, sliding window                                 │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 5. Data Management

### 5.1 Database per Service

```python
# Каждый сервис владеет своими данными
# Нет shared database между сервисами!

data_patterns = {
    "Database per Service": {
        "description": "Каждый сервис имеет свою БД",
        "benefit": "Loose coupling, independent scaling",
        "challenge": "Data consistency, joins across services"
    },
    "Saga Pattern": {
        "description": "Распределённые транзакции через события",
        "benefit": "ACID-like behavior across services",
        "types": ["Choreography (events)", "Orchestration (coordinator)"]
    },
    "Event Sourcing": {
        "description": "Хранение событий вместо состояния",
        "benefit": "Audit trail, replay events",
        "challenge": "Query complexity, event schema evolution"
    },
    "CQRS": {
        "description": "Separate read and write models",
        "benefit": "Optimized for different workloads",
        "challenge": "Eventual consistency, complexity"
    }
}

```

### 5.2 Saga Pattern Example

```

┌────────────────────────────────────────────────────────────────────┐
│              Saga: Order Processing                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Choreography Saga:                                                │
│                                                                     │
│  1. Order Service creates order                                    │
│     → publishes OrderCreated                                       │
│                                                                     │
│  2. Payment Service listens                                        │
│     → processes payment                                            │
│     → publishes PaymentCompleted or PaymentFailed                  │
│                                                                     │
│  3. Inventory Service listens                                      │
│     → reserves items                                               │
│     → publishes ItemsReserved or ItemsUnavailable                  │
│                                                                     │
│  4. Shipping Service listens                                       │
│     → creates shipment                                             │
│     → publishes ShipmentCreated                                    │
│                                                                     │
│  Compensation (rollback):                                          │
│  If PaymentFailed → cancel order                                   │
│  If ItemsUnavailable → refund payment, cancel order                │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 6. Service Mesh

### 6.1 AWS App Mesh

```

┌────────────────────────────────────────────────────────────────────┐
│              Service Mesh                                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │                    Control Plane                            │   │
│  │                 (App Mesh / Istio)                          │   │
│  └────────────────────────────────────────────────────────────┘   │
│                           │                                        │
│          ┌────────────────┴────────────────┐                      │
│          ▼                                 ▼                      │
│  ┌───────────────┐                ┌───────────────┐              │
│  │  Service A    │                │  Service B    │              │
│  │  ┌─────────┐  │    traffic     │  ┌─────────┐  │              │
│  │  │  App    │  │  ◄──────────►  │  │  App    │  │              │
│  │  └────┬────┘  │                │  └────┬────┘  │              │
│  │       │       │                │       │       │              │
│  │  ┌────▼────┐  │                │  ┌────▼────┐  │              │
│  │  │ Envoy   │  │                │  │ Envoy   │  │              │
│  │  │ Sidecar │  │                │  │ Sidecar │  │              │
│  │  └─────────┘  │                │  └─────────┘  │              │
│  └───────────────┘                └───────────────┘              │
│                                                                     │
│  Service Mesh provides:                                            │
│  • mTLS (encryption)                                              │
│  • Traffic management (canary, blue-green)                        │
│  • Observability (metrics, traces)                                │
│  • Circuit breaking, retries                                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 7. AWS Services для Microservices

```python

aws_microservices_stack = {
    "API Gateway": "External API management",
    "ALB": "Internal load balancing",
    "ECS/EKS": "Container orchestration",
    "Lambda": "Serverless functions",
    "App Mesh": "Service mesh",
    "X-Ray": "Distributed tracing",
    "CloudWatch": "Logs and metrics",
    "SQS/SNS/EventBridge": "Async messaging",
    "Step Functions": "Workflow orchestration",
    "Secrets Manager": "Credentials management",
    "Parameter Store": "Configuration"
}

print("AWS Services for Microservices:")
for service, purpose in aws_microservices_stack.items():
    print(f"  • {service}: {purpose}")

```

---

## 💡 Key Takeaways

- **Start with Monolith** — decompose when needed

- **Bounded Context** — natural service boundary

- **Database per Service** — essential for loose coupling

- **Async > Sync** — prefer event-driven communication

- **Resilience Patterns** — circuit breaker, retry, timeout

- **Service Mesh** — cross-cutting concerns (mTLS, observability)

---

## 📚 Additional Resources

- "Building Microservices" by Sam Newman
- "Microservices Patterns" by Chris Richardson
- [AWS Microservices](https://aws.amazon.com/microservices/)

---

## 🚀 Next Steps

**Следующие модули:**

- [21_Observability](../21_Observability/) — Мониторинг микросервисов
- [22_Security](../22_Security/) — Безопасность микросервисов

**Практика:**

1. Разбейте монолит на 2-3 микросервиса
2. Реализуйте коммуникацию через SQS/SNS
3. Настройте service mesh с App Mesh



