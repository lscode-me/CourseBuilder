# Observability
## Три столпа: логи, метрики, трейсы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [08_Monitoring](../08_Monitoring/) — Мониторинг
- Понимать основы HTTP и распределённых систем
- Иметь опыт работы с микросервисами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить разницу между мониторингом и observability
- Применять три столпа observability (logs, metrics, traces)
- Настроить structured logging
- Реализовать distributed tracing
- Коррелировать данные из разных источников

---

## 1. Monitoring vs Observability

### 1.1 Определения

**Monitoring** — сбор предопределённых метрик и алерты на известные проблемы.

**Observability** — способность понять внутреннее состояние системы по её внешним выходам (outputs).

```python

comparison = {
    "monitoring": {
        "approach": "Знаем заранее, что искать",
        "questions": ["Работает ли система?", "Есть ли известные проблемы?"],
        "analogy": "Проверка по чек-листу"
    },
    "observability": {
        "approach": "Можем исследовать неизвестные проблемы",
        "questions": ["Почему это происходит?", "Что именно сломалось?"],
        "analogy": "Детективное расследование"
    }
}

```

### 1.2 Три столпа Observability

```

┌────────────────────────────────────────────────────────────────┐
│                    Three Pillars of Observability              │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │    LOGS     │    │   METRICS   │    │   TRACES    │         │
│  │             │    │             │    │             │         │
│  │ "Что        │    │ "Сколько    │    │ "Где        │         │
│  │  произошло" │    │  и когда"   │    │  было"      │         │
│  │             │    │             │    │             │         │
│  │ • Events    │    │ • Counters  │    │ • Spans     │         │
│  │ • Errors    │    │ • Gauges    │    │ • Context   │         │
│  │ • Debug     │    │ • Histograms│    │ • Timing    │         │
│  └─────────────┘    └─────────────┘    └─────────────┘         │
│                                                                │
│                 Correlation via trace_id, request_id           │
│                                                                │
└────────────────────────────────────────────────────────────────┘

```

---

## 2. Logs (Логи)

### 2.1 Structured Logging

```python
# ❌ Плохо: неструктурированные логи
import logging
logger = logging.getLogger(__name__)

logger.info(f"User {user_id} created order {order_id} for ${amount}")
# Output: "User 123 created order 456 for $99.99"
# Проблема: сложно парсить, искать, агрегировать

# ✅ Хорошо: structured logging (JSON)
import structlog

logger = structlog.get_logger()

logger.info(
    "order_created",
    user_id=user_id,
    order_id=order_id,
    amount=amount,
    currency="USD"
)
# Output: {"event": "order_created", "user_id": 123, "order_id": 456, 
#          "amount": 99.99, "currency": "USD", "timestamp": "..."}
```

### 2.2 Конфигурация structlog

```python

import structlog
import logging

def configure_logging():
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

# Использование с контекстом
logger = structlog.get_logger()

# Добавляем контекст для всех последующих логов
logger = logger.bind(
    service="order-service",
    environment="production"
)

# Добавляем request-specific контекст
def process_request(request):
    log = logger.bind(
        trace_id=request.headers.get("X-Trace-ID"),
        user_id=request.user.id
    )
    
    log.info("request_started", path=request.path)
    # ... process ...
    log.info("request_completed", status=200, duration_ms=45)

```

### 2.3 Log Levels

```python

log_levels = {
    "DEBUG": {
        "purpose": "Детальная отладочная информация",
        "production": False,
        "examples": ["Variable values", "Function entry/exit"]
    },
    "INFO": {
        "purpose": "Нормальные события",
        "production": True,
        "examples": ["Request received", "Task completed"]
    },
    "WARNING": {
        "purpose": "Потенциальные проблемы",
        "production": True,
        "examples": ["Deprecated API used", "Retry attempt"]
    },
    "ERROR": {
        "purpose": "Ошибки, которые не прервали работу",
        "production": True,
        "examples": ["Failed to send email", "Database timeout"]
    },
    "CRITICAL": {
        "purpose": "Критические ошибки",
        "production": True,
        "examples": ["Database connection lost", "Out of memory"]
    }
}

```

### 2.4 ELK Stack (Elasticsearch, Logstash, Kibana)

```yaml
# filebeat.yml (сбор логов)
filebeat.inputs:
  - type: container
    paths:
      - '/var/lib/docker/containers/*/*.log'
    processors:
      - add_kubernetes_metadata:
          host: ${NODE_NAME}
          matchers:
            - logs_path:
                logs_path: "/var/lib/docker/containers/"

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "logs-%{+yyyy.MM.dd}"

```

---

## 3. Metrics (Метрики)

### 3.1 Типы метрик для Observability

```python
# Рассмотрено в модуле Monitoring, здесь фокус на корреляции

from prometheus_client import Counter, Histogram
import structlog

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

logger = structlog.get_logger()

def handle_request(request):
    trace_id = request.headers.get("X-Trace-ID")
    log = logger.bind(trace_id=trace_id)
    
    with REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).time():
        # Process request
        response = process(request)
    
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    
    # Лог с теми же labels для корреляции
    log.info(
        "request_handled",
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    )
    
    return response

```

---

## 4. Traces (Трейсы)

### 4.1 Distributed Tracing Concepts

```

┌──────────────────────────────────────────────────────────────────┐
│                    Distributed Trace                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Trace ID: abc-123-xyz                                           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │ Span: API Gateway                                        │    │
│  │ Duration: 250ms                                          │    │
│  │ ├──────────────────────────────────────────────────────┤ │    │
│  │ │ Span: Auth Service                                    │ │   │
│  │ │ Duration: 50ms                                        │ │   │
│  │ └──────────────────────────────────────────────────────┘ │    │
│  │ ├──────────────────────────────────────────────────────┤ │    │
│  │ │ Span: Order Service                                   │ │   │
│  │ │ Duration: 150ms                                       │ │   │
│  │ │ ├────────────────────────────────────────────────────┤│ │   │
│  │ │ │ Span: Database Query                               ││ │   │
│  │ │ │ Duration: 80ms                                     ││ │   │
│  │ │ └────────────────────────────────────────────────────┘│ │   │
│  │ │ ├────────────────────────────────────────────────────┤│ │   │
│  │ │ │ Span: Cache Lookup                                 ││ │   │
│  │ │ │ Duration: 5ms                                      ││ │   │
│  │ │ └────────────────────────────────────────────────────┘│ │   │
│  │ └──────────────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                  │
│  Time ──────────────────────────────────────────────────────▶    │
│  0ms                                                    250ms    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

```

### 4.2 OpenTelemetry

```python
# opentelemetry_setup.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

def configure_tracing(service_name: str):
    resource = Resource.create({
        "service.name": service_name,
        "service.version": "1.0.0",
    })
    
    provider = TracerProvider(resource=resource)
    
    # Export to Jaeger/Tempo via OTLP
    otlp_exporter = OTLPSpanExporter(
        endpoint="http://tempo:4317",
        insecure=True
    )
    
    provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    trace.set_tracer_provider(provider)
    
    return trace.get_tracer(__name__)

# Использование
tracer = configure_tracing("order-service")

@tracer.start_as_current_span("process_order")
def process_order(order_id: int):
    current_span = trace.get_current_span()
    current_span.set_attribute("order.id", order_id)
    
    with tracer.start_as_current_span("validate_order"):
        validate(order_id)
    
    with tracer.start_as_current_span("save_to_database") as span:
        span.set_attribute("db.system", "postgresql")
        save_order(order_id)
    
    with tracer.start_as_current_span("send_notification"):
        notify_user(order_id)

```

### 4.3 Автоматическая инструментация

```python
# Автоматическая инструментация для FastAPI/Flask/requests
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

# После настройки tracing
FastAPIInstrumentor.instrument()
RequestsInstrumentor.instrument()
SQLAlchemyInstrumentor().instrument()

# Теперь все HTTP запросы и DB queries автоматически трейсятся
```

### 4.4 Context Propagation

```python
# Передача trace context между сервисами
from opentelemetry import trace
from opentelemetry.propagate import inject, extract
import requests

def call_downstream_service(url: str, data: dict):
    headers = {}
    
    # Inject current trace context into headers
    inject(headers)
    
    response = requests.post(url, json=data, headers=headers)
    return response

# В downstream сервисе
def handle_request(request):
    # Extract trace context from incoming headers
    context = extract(request.headers)
    
    with tracer.start_as_current_span("handle_request", context=context):
        # Process with parent context
        pass

```

---

## 5. Correlation (Корреляция)

### 5.1 Связывание logs, metrics, traces

```python

import structlog
from opentelemetry import trace

logger = structlog.get_logger()

def process_request(request):
    # Получаем trace context
    span = trace.get_current_span()
    trace_id = span.get_span_context().trace_id
    span_id = span.get_span_context().span_id
    
    # Добавляем в логи
    log = logger.bind(
        trace_id=format(trace_id, '032x'),
        span_id=format(span_id, '016x')
    )
    
    log.info("processing_started")
    
    # Теперь логи можно найти по trace_id в Grafana/Kibana
    # и перейти к трейсу в Jaeger/Tempo
```

### 5.2 Grafana Correlation

```yaml
# grafana datasources
datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    
  - name: Loki
    type: loki
    url: http://loki:3100
    jsonData:
      derivedFields:
        - name: trace_id
          matcherRegex: '"trace_id":"(\w+)"'
          url: 'http://tempo:3200/trace/$${__value.raw}'
          datasourceUid: tempo
    
  - name: Tempo
    type: tempo
    url: http://tempo:3200

```

---

## 6. Практические сценарии

### 6.1 Debugging Slow Request

```

Шаг 1: Алерт "P99 latency > 2s"
        ↓
Шаг 2: Смотрим Grafana → какой endpoint медленный?
        ↓
Шаг 3: Ищем traces с высокой latency
        ↓
Шаг 4: Анализируем spans → какой сервис/операция медленная?
        ↓
Шаг 5: Смотрим логи этого span по trace_id
        ↓
Шаг 6: Находим причину (slow query, external API timeout, etc.)

```

### 6.2 Debugging Error Spike

```

Шаг 1: Алерт "Error rate > 5%"
        ↓
Шаг 2: Смотрим метрики → какой сервис, какой статус код?
        ↓
Шаг 3: Ищем логи с level=ERROR за этот период
        ↓
Шаг 4: Группируем по error message → какая ошибка?
        ↓
Шаг 5: Берём trace_id из лога → смотрим полный trace
        ↓
Шаг 6: Понимаем контекст ошибки (какой запрос, какие данные)

```

---

## 💡 Key Takeaways

- **Observability ≠ Monitoring**: Observability — способность исследовать неизвестные проблемы

- **Три столпа**: Logs (что произошло), Metrics (сколько), Traces (где)

- **Structured logging обязателен**: JSON логи можно парсить и искать

- **Correlation через trace_id**: Связывает logs, metrics, traces

- **OpenTelemetry — стандарт**: Единый API для instrumentation

---

## 🚀 Next Steps

**Related Modules:**

- [10_SRE](../10_SRE/) — Site Reliability Engineering
- [12_Incidents](../12_Incidents/) — Incident Management

**Practice Ideas:**

1. Добавьте structured logging в приложение
2. Настройте OpenTelemetry tracing
3. Создайте correlation в Grafana

---

## 📚 Additional Resources

**Books:**

- "Observability Engineering" by Charity Majors

**Tools:**

- [OpenTelemetry](https://opentelemetry.io/)
- [Jaeger](https://www.jaegertracing.io/)
- [Grafana Tempo](https://grafana.com/oss/tempo/)

---




