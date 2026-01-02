# Мониторинг систем
## Prometheus, Grafana и практики мониторинга

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули по CI/CD и IaC
- Понимать основы Linux metrics (CPU, memory, disk, network)
- Иметь базовые знания о Kubernetes

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы эффективного мониторинга
- Настроить Prometheus для сбора метрик
- Создавать дашборды в Grafana
- Настроить алертинг с Alertmanager
- Применять RED и USE методы для мониторинга

---

## 1. Основы мониторинга

### 1.1 Зачем нужен мониторинг?

```python
monitoring_purposes = {
    "alerting": "Узнать о проблеме раньше пользователей",
    "debugging": "Понять, что пошло не так",
    "trending": "Предсказать будущие проблемы (capacity planning)",
    "visibility": "Понимать состояние системы в реальном времени",
    "business_insights": "Связать технические метрики с бизнес-результатами"
}
```

### 1.2 Виды мониторинга

```
┌──────────────────────────────────────────────────────────────────┐
│                     Monitoring Stack                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Infrastructure Monitoring                                       │
│  ├── Hardware (CPU, Memory, Disk, Network)                       │
│  ├── Operating System metrics                                    │
│  └── Container metrics (Docker, K8s)                             │
│                                                                  │
│  Application Monitoring                                          │
│  ├── Application metrics (requests, latency, errors)             │
│  ├── Business metrics (orders, revenue, users)                   │
│  └── Custom metrics                                              │
│                                                                  │
│  Network Monitoring                                              │
│  ├── Bandwidth, latency, packet loss                             │
│  └── DNS, SSL certificates                                       │
│                                                                  │
│  Synthetic Monitoring                                            │
│  ├── Uptime checks                                               │
│  └── User journey simulation                                     │
│                                                                  │
│  Real User Monitoring (RUM)                                      │
│  └── Actual user experience metrics                              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 1.3 Метрики: типы данных

```python
metric_types = {
    "counter": {
        "description": "Монотонно возрастающее значение",
        "examples": ["http_requests_total", "errors_total"],
        "use_case": "Подсчёт событий"
    },
    "gauge": {
        "description": "Значение, которое может расти и уменьшаться",
        "examples": ["temperature", "active_connections", "memory_usage"],
        "use_case": "Текущее состояние"
    },
    "histogram": {
        "description": "Распределение значений по bucket'ам",
        "examples": ["request_duration_seconds", "response_size_bytes"],
        "use_case": "Latency, размеры"
    },
    "summary": {
        "description": "Похож на histogram, но считает квантили на клиенте",
        "examples": ["request_duration_quantiles"],
        "use_case": "Percentiles (P50, P99)"
    }
}
```

---

## 2. Prometheus

### 2.1 Архитектура Prometheus

```
┌─────────────────────────────────────────────────────────────────┐
│                    Prometheus Architecture                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   Target 1   │    │   Target 2   │    │   Target 3   │       │
│  │  /metrics    │    │  /metrics    │    │  /metrics    │       │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘       │
│         │                   │                   │               │
│         └───────────────────┼───────────────────┘               │
│                             │                                   │
│                      ┌──────▼──────┐                            │
│                      │  Prometheus │                            │
│                      │   Server    │                            │
│                      │             │                            │
│                      │ ┌─────────┐ │                            │
│                      │ │ TSDB    │ │◀── Storage                 │
│                      │ └─────────┘ │                            │
│                      │             │                            │
│                      │ ┌─────────┐ │                            │
│                      │ │ PromQL  │ │◀── Query Language          │
│                      │ └─────────┘ │                            │
│                      └──────┬──────┘                            │
│                             │                                   │
│         ┌───────────────────┼───────────────────┐               │
│         │                   │                   │               │
│         ▼                   ▼                   ▼               │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │   Grafana   │    │ Alertmanager│    │    API      │          │
│  │             │    │             │    │  Clients    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Установка Prometheus

```yaml
# prometheus-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
        - name: prometheus
          image: prom/prometheus:v2.47.0
          args:
            - '--config.file=/etc/prometheus/prometheus.yml'
            - '--storage.tsdb.path=/prometheus'
            - '--storage.tsdb.retention.time=15d'
            - '--web.enable-lifecycle'
          ports:
            - containerPort: 9090
          volumeMounts:
            - name: config
              mountPath: /etc/prometheus
            - name: storage
              mountPath: /prometheus
      volumes:
        - name: config
          configMap:
            name: prometheus-config
        - name: storage
          persistentVolumeClaim:
            claimName: prometheus-pvc
```

### 2.3 Конфигурация Prometheus

```yaml
# prometheus.yml

global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager:9093

rule_files:
  - /etc/prometheus/rules/*.yml

scrape_configs:
  # Prometheus itself
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node Exporter (host metrics)
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']

  # Kubernetes pods with annotations
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__meta_kubernetes_pod_ip, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: (.+);(.+)
        replacement: $1:$2
        target_label: __address__
```

### 2.4 PromQL — язык запросов

```promql
# Базовые запросы

http_requests_total                           # Все метрики
http_requests_total{status="200"}             # С фильтром
http_requests_total{status=~"2.."}            # Regex

# Rate (скорость изменения counter)

rate(http_requests_total[5m])                 # Requests per second за 5 минут

# Агрегация

sum(rate(http_requests_total[5m]))            # Общий RPS
sum(rate(http_requests_total[5m])) by (service)  # RPS по сервисам

# Percentiles (из histogram)

histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# Алерт-совместимые выражения

rate(http_requests_total{status="500"}[5m]) / rate(http_requests_total[5m]) > 0.05
# Error rate > 5%

# Примеры для troubleshooting
# CPU usage

100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage

(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Disk usage

100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)
```

---

## 3. Grafana

### 3.1 Создание дашбордов

```json
{
  "dashboard": {
    "title": "Application Overview",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m])) by (service)",
            "legendFormat": "{{service}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100"
          }
        ],
        "thresholds": [
          {"value": 0, "color": "green"},
          {"value": 1, "color": "yellow"},
          {"value": 5, "color": "red"}
        ]
      },
      {
        "title": "P99 Latency",
        "type": "stat",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))"
          }
        ]
      }
    ]
  }
}
```

### 3.2 Dashboard as Code

```yaml
# grafana-dashboard.yaml (ConfigMap)

apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-dashboards
  labels:
    grafana_dashboard: "1"
data:
  app-overview.json: |
    {
      "title": "Application Overview",
      "uid": "app-overview",
      "panels": [...]
    }
```

---

## 4. Alerting

### 4.1 Alertmanager

```yaml
# alertmanager.yml

global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'
  slack_api_url: 'https://hooks.slack.com/services/...'

route:
  receiver: 'default'
  group_by: ['alertname', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
      continue: true
    
    - match:
        severity: warning
      receiver: 'slack'

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts'
        send_resolved: true
  
  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: '<pagerduty-key>'
  
  - name: 'slack'
    slack_configs:
      - channel: '#alerts-warning'
        send_resolved: true

inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'service']
```

### 4.2 Alert Rules

```yaml
# prometheus-rules.yml

groups:
  - name: application
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
          /
          sum(rate(http_requests_total[5m])) by (service)
          > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate for {{ $labels.service }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
          runbook_url: "https://wiki.example.com/runbooks/high-error-rate"

      - alert: HighLatency
        expr: |
          histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))
          > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High P99 latency for {{ $labels.service }}"
          description: "P99 latency is {{ $value | humanizeDuration }}"

      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service {{ $labels.job }} is down"

  - name: infrastructure
    rules:
      - alert: HighCPU
        expr: |
          100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
          > 80
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High CPU on {{ $labels.instance }}"

      - alert: DiskSpaceLow
        expr: |
          (node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100 < 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"
```

---

## 5. Методы мониторинга

### 5.1 USE Method (для ресурсов)

**U**tilization, **S**aturation, **E**rrors — для каждого ресурса.

```python
use_method = {
    "CPU": {
        "utilization": "Процент использования CPU",
        "saturation": "Длина очереди runnable процессов",
        "errors": "CPU errors (редко)"
    },
    "Memory": {
        "utilization": "Процент использования памяти",
        "saturation": "Swap usage, OOM events",
        "errors": "ECC errors"
    },
    "Disk": {
        "utilization": "Процент использования дискового пространства",
        "saturation": "I/O wait, queue length",
        "errors": "Disk errors"
    },
    "Network": {
        "utilization": "Bandwidth usage",
        "saturation": "Dropped packets, queue overflow",
        "errors": "Interface errors, CRC errors"
    }
}
```

```promql
# USE Method queries

# CPU Utilization

100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# CPU Saturation (load average)

node_load1 / count by (instance) (node_cpu_seconds_total{mode="idle"})

# Memory Utilization

(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Memory Saturation (swap usage)

node_memory_SwapTotal_bytes - node_memory_SwapFree_bytes

# Disk Utilization

100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)

# Disk Saturation (I/O wait)

rate(node_cpu_seconds_total{mode="iowait"}[5m]) * 100

# Network Utilization

rate(node_network_receive_bytes_total[5m]) + rate(node_network_transmit_bytes_total[5m])
```

### 5.2 RED Method (для сервисов)

**R**ate, **E**rrors, **D**uration — для каждого сервиса.

```python
red_method = {
    "rate": "Количество запросов в секунду",
    "errors": "Количество ошибочных запросов",
    "duration": "Время обработки запросов (latency)"
}
```

```promql
# RED Method queries

# Rate

sum(rate(http_requests_total[5m])) by (service)

# Errors

sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)

# Error Rate (%)

sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
/
sum(rate(http_requests_total[5m])) by (service)
* 100

# Duration (P99)

histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))

# Duration (P50)

histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))
```

### 5.3 Four Golden Signals (Google SRE)

```python
golden_signals = {
    "latency": "Время обработки запроса",
    "traffic": "Количество запросов",
    "errors": "Процент неудачных запросов",
    "saturation": "Насколько загружен сервис"
}
```

---

## 6. Application Instrumentation

### 6.1 Python с prometheus_client

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time
import random

# Определение метрик

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

ACTIVE_REQUESTS = Gauge(
    'http_active_requests',
    'Number of active HTTP requests'
)

# Middleware/decorator

def track_request(method: str, endpoint: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ACTIVE_REQUESTS.inc()
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                status = "200"
            except Exception:
                status = "500"
                raise
            finally:
                duration = time.time() - start_time
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
                REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=status).inc()
                ACTIVE_REQUESTS.dec()
            
            return result
        return wrapper
    return decorator

# Использование

@track_request("GET", "/api/users")
def get_users():
    time.sleep(random.uniform(0.01, 0.5))
    return {"users": []}

if __name__ == "__main__":
    # Запуск HTTP сервера для /metrics
    start_http_server(8000)
    
    while True:
        get_users()
        time.sleep(0.1)
```

### 6.2 Kubernetes Pod Annotations

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
        prometheus.io/path: "/metrics"
    spec:
      containers:
        - name: myapp
          ports:
            - containerPort: 8080  # App port
            - containerPort: 8000  # Metrics port
```

---

## 7. Best Practices

### 7.1 Naming Conventions

```python
# Хорошие имена метрик

good_metric_names = [
    "http_requests_total",           # counter с _total
    "http_request_duration_seconds", # histogram с единицами
    "node_memory_bytes",             # gauge с единицами
    "process_open_fds",              # понятное имя
]

# Плохие имена

bad_metric_names = [
    "requests",        # Слишком общее
    "latency",         # Нет единиц
    "MyAppMetric",     # CamelCase
    "cpu-usage",       # Дефисы вместо underscore
]
```

### 7.2 Labels Best Practices

```python
# Хорошо: низкая кардинальность

good_labels = {
    "status": ["200", "201", "400", "404", "500"],  # ~5 значений
    "method": ["GET", "POST", "PUT", "DELETE"],     # ~5 значений
    "service": ["api", "web", "worker"],            # ~10 значений
}

# Плохо: высокая кардинальность (убьёт Prometheus)

bad_labels = {
    "user_id": "millions of values",     # НЕТ!
    "request_id": "unique per request",  # НЕТ!
    "timestamp": "infinite values",      # НЕТ!
}
```

### 7.3 Alert Best Practices

```python
alert_best_practices = [
    "Алерт на симптомы, не причины",
    "Включать runbook URL в аннотации",
    "Использовать 'for' clause (не алертить на кратковременные спайки)",
    "Правильные severity levels",
    "Page только на actionable алерты",
    "Избегать alert fatigue — меньше, но важнее",
]
```

---

## 💡 Key Takeaways

- **RED для сервисов, USE для ресурсов**: Разные методы для разных сущностей

- **Prometheus pull model**: Prometheus сам забирает метрики с /metrics

- **PromQL для анализа**: Мощный язык запросов для агрегации и алертинга

- **Labels важны**: Правильные labels = эффективные запросы

- **Alert on symptoms**: Алертить на симптомы, искать причины при debugging

---

## 🚀 Next Steps

**Related Modules:**

- [09_Observability](../09_Observability/) — Три столпа observability
- [11_ServiceLevels](../11_ServiceLevels/) — SLI/SLO/SLA

**Practice Ideas:**

1. Установите Prometheus + Grafana локально
2. Добавьте метрики в Python приложение
3. Создайте дашборд с RED метриками

---

## 📚 Additional Resources

**Documentation:**

- [Prometheus](https://prometheus.io/docs/)
- [Grafana](https://grafana.com/docs/)

**Books:**

- "Prometheus: Up & Running" by Brian Brazil

---





