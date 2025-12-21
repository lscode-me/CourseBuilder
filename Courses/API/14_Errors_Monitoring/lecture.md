# Ошибки, логирование и мониторинг
## Стандарты ошибок, Correlation IDs, логирование API, метрики и SLA

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать проектирование API и обработку ошибок
- Знать основы мониторинга и логирования
- Иметь представление о метриках и SLA

**Recommended prior modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [13_API_Security](../13_API_Security/) — безопасность API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать стандартизированные структуры ошибок
- Использовать Correlation IDs для трассировки запросов
- Настраивать логирование API с правильным уровнем детализации
- Собирать и анализировать метрики API
- Определять и отслеживать SLA для API

---

## 1. Стандарты ошибок

Стандартизированная структура ошибок упрощает обработку и отладку.

### 1.1 Структура ошибок

**Example: Стандартизированная структура ошибок**

```python

def error_response(code, message, details=None, correlation_id=None):
    """Стандартизированная структура ошибки"""
    error = {
        "error": {
            "code": code,
            "message": message,
            "timestamp": datetime.utcnow().isoformat(),
            "correlation_id": correlation_id
        }
    }
    if details:
        error["error"]["details"] = details
    return error

# Примеры ошибок
validation_error = error_response(
    "VALIDATION_ERROR",
    "Invalid email format",
    {"field": "email", "value": "invalid-email"},
    correlation_id="req-123"
)

not_found_error = error_response(
    "NOT_FOUND",
    "User not found",
    {"resource": "user", "id": 123},
    correlation_id="req-124"
)
```

### 1.2 Категории ошибок

**Основные категории:**

- **4xx Client Errors**: Ошибки клиента (400, 401, 403, 404, 422, 429)

- **5xx Server Errors**: Ошибки сервера (500, 502, 503, 504)

---

## 2. Correlation IDs

**Correlation ID** — это уникальный идентификатор, связывающий все логи и события одного запроса.

### 2.1 Использование Correlation IDs

**Example: Correlation ID в запросах**

```python

import uuid
from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def set_correlation_id():
    """Установка Correlation ID для каждого запроса"""
    correlation_id = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    g.correlation_id = correlation_id

@app.after_request
def add_correlation_id_header(response):
    """Добавление Correlation ID в заголовок ответа"""
    if hasattr(g, "correlation_id"):
        response.headers["X-Correlation-ID"] = g.correlation_id
    return response

def log_with_correlation(message, level="info"):
    """Логирование с Correlation ID"""
    correlation_id = getattr(g, "correlation_id", "unknown")
    logger.log(level, f"[{correlation_id}] {message}")

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    log_with_correlation(f"Getting user {user_id}")
    user = find_user(user_id)
    if not user:
        log_with_correlation(f"User {user_id} not found", "warning")
        return error_response(
            "NOT_FOUND",
            "User not found",
            correlation_id=g.correlation_id
        ), 404
    return jsonify(user), 200
```

### 2.2 Трассировка запросов

**Correlation ID позволяет:**

- Отслеживать запрос через все системы
- Связывать логи разных компонентов
- Упрощать отладку распределённых систем

---

## 3. Логирование API

Правильное логирование критично для отладки и мониторинга.

### 3.1 Уровни логирования

**Example: Структурированное логирование**

```python

import logging
import json

class APILogger:
    """Структурированное логирование для API"""
    
    def __init__(self):
        self.logger = logging.getLogger("api")
        self.logger.setLevel(logging.INFO)
    
    def log_request(self, method, path, status_code, duration_ms, correlation_id):
        """Логирование запроса"""
        log_entry = {
            "type": "request",
            "method": method,
            "path": path,
            "status_code": status_code,
            "duration_ms": duration_ms,
            "correlation_id": correlation_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.logger.info(json.dumps(log_entry))
    
    def log_error(self, error_code, message, correlation_id, exception=None):
        """Логирование ошибки"""
        log_entry = {
            "type": "error",
            "error_code": error_code,
            "message": message,
            "correlation_id": correlation_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        if exception:
            log_entry["exception"] = str(exception)
        self.logger.error(json.dumps(log_entry))

# Использование

api_logger = APILogger()
api_logger.log_request("GET", "/api/users/123", 200, 45, "req-123")
```

### 3.2 Что логировать

**Обязательно логировать:**

- Входящие запросы (method, path, headers)
- Исходящие ответы (status code, duration)
- Ошибки (код, сообщение, stack trace)
- Correlation ID для всех событий

---

## 4. Метрики и SLA

**Метрики** измеряют производительность API. **SLA** определяет гарантии уровня обслуживания.

### 4.1 Ключевые метрики

**Example: Сбор метрик**

```python

from collections import defaultdict
import time

class APIMetrics:
    """Сбор метрик API"""
    
    def __init__(self):
        self.request_count = defaultdict(int)
        self.error_count = defaultdict(int)
        self.response_times = defaultdict(list)
        self.status_codes = defaultdict(int)
    
    def record_request(self, endpoint, method, status_code, duration_ms):
        """Запись метрики запроса"""
        key = f"{method} {endpoint}"
        self.request_count[key] += 1
        self.status_codes[status_code] += 1
        self.response_times[key].append(duration_ms)
        
        if status_code >= 400:
            self.error_count[key] += 1
    
    def get_metrics(self):
        """Получение метрик"""
        metrics = {}
        for endpoint, count in self.request_count.items():
            avg_time = sum(self.response_times[endpoint]) / len(self.response_times[endpoint])
            error_rate = self.error_count[endpoint] / count if count > 0 else 0
            
            metrics[endpoint] = {
                "request_count": count,
                "avg_response_time_ms": avg_time,
                "error_rate": error_rate
            }
        return metrics

# Использование
metrics = APIMetrics()
metrics.record_request("/api/users", "GET", 200, 45)
metrics.record_request("/api/users", "GET", 500, 1200)

print(metrics.get_metrics())
```

### 4.2 SLA (Service Level Agreement)

**Example: SLA метрики**

```python

class SLAMonitor:
    """Мониторинг SLA"""
    
    def __init__(self):
        self.sla_targets = {
            "availability": 0.99,  # 99% доступность
            "p95_latency_ms": 500,  # 95% запросов < 500ms
            "error_rate": 0.01  # < 1% ошибок
        }
        self.metrics = APIMetrics()
    
    def check_sla(self):
        """Проверка соответствия SLA"""
        results = {}
        
        # Проверка доступности
        total_requests = sum(self.metrics.request_count.values())
        total_errors = sum(self.metrics.error_count.values())
        availability = 1 - (total_errors / total_requests) if total_requests > 0 else 1
        results["availability"] = {
            "current": availability,
            "target": self.sla_targets["availability"],
            "meets_sla": availability >= self.sla_targets["availability"]
        }
        
        # Проверка latency
        all_times = []
        for times in self.metrics.response_times.values():
            all_times.extend(times)
        
        if all_times:
            sorted_times = sorted(all_times)
            p95_index = int(len(sorted_times) * 0.95)
            p95_latency = sorted_times[p95_index]
            
            results["p95_latency"] = {
                "current_ms": p95_latency,
                "target_ms": self.sla_targets["p95_latency_ms"],
                "meets_sla": p95_latency <= self.sla_targets["p95_latency_ms"]
            }
        
        return results
```

---

## 5. Best Practices

### 5.1 Структурированное логирование

- Используйте JSON формат для логов
- Включайте Correlation ID во все логи
- Логируйте на правильном уровне (INFO, WARNING, ERROR)

### 5.2 Мониторинг

- Отслеживайте ключевые метрики (latency, error rate, throughput)
- Настройте алерты при нарушении SLA
- Используйте dashboards для визуализации

### 5.3 Алерты и уведомления

**Example: Настройка алертов**

```python

class AlertManager:
    """Управление алертами"""
    
    def __init__(self, sla_monitor):
        self.sla_monitor = sla_monitor
        self.alert_thresholds = {
            "error_rate": 0.05,  # 5%
            "p95_latency_ms": 1000,  # 1 секунда
            "availability": 0.95  # 95%
        }
    
    def check_and_alert(self):
        """Проверка метрик и отправка алертов"""
        sla_results = self.sla_monitor.check_sla()
        
        alerts = []
        if not sla_results["availability"]["meets_sla"]:
            alerts.append({
                "type": "availability",
                "severity": "critical",
                "message": f"Availability below SLA: {sla_results['availability']['current']}"
            })
        
        if not sla_results["p95_latency"]["meets_sla"]:
            alerts.append({
                "type": "latency",
                "severity": "warning",
                "message": f"P95 latency above SLA: {sla_results['p95_latency']['current_ms']}ms"
            })
        
        for alert in alerts:
            self.send_alert(alert)
    
    def send_alert(self, alert):
        """Отправка алерта"""
        # Отправка в систему мониторинга (Prometheus, Datadog и т.д.)
        print(f"ALERT: {alert['severity']} - {alert['message']}")
```

### 5.4 Dashboards

**Example: Создание dashboard метрик**

```python

class MetricsDashboard:
    """Dashboard для визуализации метрик"""
    
    def __init__(self, metrics_collector):
        self.metrics = metrics_collector
    
    def get_dashboard_data(self):
        """Данные для dashboard"""
        return {
            "request_count": self.metrics.get_total_requests(),
            "error_rate": self.metrics.get_error_rate(),
            "avg_latency": self.metrics.get_avg_latency(),
            "p95_latency": self.metrics.get_p95_latency(),
            "status_codes": self.metrics.get_status_code_distribution(),
            "top_endpoints": self.metrics.get_top_endpoints(),
            "sla_status": self.metrics.check_sla()
        }
```

## 6. Distributed Tracing

### 6.1 Трассировка запросов

**Example: Distributed Tracing с Correlation ID**

```python

class DistributedTracer:
    """Трассировка распределённых запросов"""
    
    def __init__(self):
        self.traces = {}
    
    def start_trace(self, correlation_id, service_name, operation):
        """Начало трассировки"""
        trace = {
            "correlation_id": correlation_id,
            "service": service_name,
            "operation": operation,
            "start_time": datetime.utcnow(),
            "spans": []
        }
        self.traces[correlation_id] = trace
        return trace
    
    def add_span(self, correlation_id, span_name, duration_ms):
        """Добавление span в трассировку"""
        if correlation_id in self.traces:
            self.traces[correlation_id]["spans"].append({
                "name": span_name,
                "duration_ms": duration_ms,
                "timestamp": datetime.utcnow().isoformat()
            })
    
    def get_trace(self, correlation_id):
        """Получение полной трассировки"""
        return self.traces.get(correlation_id)

# Использование
tracer = DistributedTracer()
correlation_id = "req-123"

trace = tracer.start_trace(correlation_id, "api-gateway", "get_user")
tracer.add_span(correlation_id, "auth", 5)
tracer.add_span(correlation_id, "user-service", 45)
tracer.add_span(correlation_id, "database", 30)

full_trace = tracer.get_trace(correlation_id)
```

## 7. Common Pitfalls

### 7.1 Pitfall: Отсутствие Correlation ID

❌ **Incorrect:**
```python
# Плохо: Логи без Correlation ID
logger.info("Processing request")
logger.info("Calling service")
# Невозможно связать логи одного запроса
```

✅ **Correct:**
```python
# Хорошо: Correlation ID во всех логах
correlation_id = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
logger.info(f"[{correlation_id}] Processing request")
logger.info(f"[{correlation_id}] Calling service")
```

**Why:** Correlation ID критичен для трассировки.

### 7.2 Pitfall: Неструктурированное логирование

❌ **Incorrect:**
```python
# Плохо: Текстовые логи
logger.info("User 123 created order 456")
# Сложно парсить и анализировать
```

✅ **Correct:**
```python
# Хорошо: Структурированные JSON логи
logger.info(json.dumps({
    "event": "order_created",
    "user_id": 123,
    "order_id": 456,
    "correlation_id": correlation_id,
    "timestamp": datetime.utcnow().isoformat()
}))
```

**Why:** Структурированные логи легче анализировать.

---

## 💡 Key Takeaways

- **Стандарты ошибок**: Стандартизированная структура ошибок с кодом, сообщением, timestamp и correlation_id упрощает обработку и отладку

- **Correlation IDs**: Уникальный идентификатор для каждого запроса позволяет отслеживать запрос через все системы и связывать логи

- **Логирование API**: Структурированное логирование с правильными уровнями (INFO, WARNING, ERROR) и обязательным включением Correlation ID

- **Метрики**: Ключевые метрики (request count, response time, error rate) необходимы для мониторинга производительности API

- **SLA**: Service Level Agreement определяет гарантии (доступность, latency, error rate) и требует мониторинга для обеспечения соответствия

---

## 🚀 Next Steps

**Related Modules:**

- [15_Performance_Scalability](../15_Performance_Scalability/) — производительность и масштабируемость
- [07_API_Design](../07_API_Design/) — проектирование API

**Practice Ideas:**

1. Реализуйте стандартизированную обработку ошибок с Correlation IDs
2. Настройте структурированное логирование для вашего API
3. Создайте систему сбора метрик и мониторинга SLA

**Going Deeper:**

- Distributed Tracing: трассировка в распределённых системах
- Observability Patterns: паттерны observability
- SLA Management: управление SLA

---

## 📚 Additional Resources

**Documentation:**

- [OpenTelemetry](https://opentelemetry.io/) — стандарт для observability
- [Prometheus](https://prometheus.io/) — система мониторинга и метрик

**Articles:**

- "API Error Handling Best Practices" — лучшие практики обработки ошибок
- "Distributed Tracing with Correlation IDs" — трассировка с Correlation IDs

---



