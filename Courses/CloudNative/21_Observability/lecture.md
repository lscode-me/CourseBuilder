# Observability: Logs, Metrics, Traces

---

## 📋 Prerequisites

- Понимание distributed systems
- Знакомство с CloudWatch
- Базовые знания микросервисов

---

## 🎯 Learning Objectives

- Понимать три столпа observability
- Настраивать structured logging
- Собирать и визуализировать метрики
- Использовать distributed tracing

---

## 1. Три столпа Observability

### 1.1 Обзор

```

┌───────────────────────────────────────────────────────────────────┐
│              Three Pillars of Observability                       │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │    LOGS      │  │   METRICS    │  │   TRACES     │             │
│  │              │  │              │  │              │             │
│  │ What         │  │ What is      │  │ How does     │             │
│  │ happened?    │  │ happening?   │  │ request flow?│             │
│  │              │  │              │  │              │             │
│  │ Events,      │  │ Numbers,     │  │ Request path │             │
│  │ errors,      │  │ aggregates,  │  │ across       │             │
│  │ details      │  │ trends       │  │ services     │             │
│  │              │  │              │  │              │             │
│  │ High volume, │  │ Low volume,  │  │ Sampled,     │             │
│  │ detailed     │  │ aggregated   │  │ contextual   │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
│                                                                   │
│  AWS Services:                                                    │
│  CloudWatch Logs   CloudWatch       X-Ray                         │
│                    Metrics                                        │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

### 1.2 Observability vs Monitoring

```python

comparison = {
    "Monitoring": {
        "approach": "Known unknowns",
        "questions": "Is X working? Is latency high?",
        "method": "Predefined dashboards and alerts",
        "reactive": True
    },
    "Observability": {
        "approach": "Unknown unknowns",
        "questions": "Why is this happening? What caused it?",
        "method": "Ad-hoc exploration of telemetry",
        "reactive": False
    }
}

print("Monitoring vs Observability:\n")
for approach, details in comparison.items():
    print(f"{approach}:")
    print(f"  Questions: {details['questions']}")
    print(f"  Method: {details['method']}\n")

```

---

## 2. Logging

### 2.1 Structured Logging

```python

import json
import logging
import sys
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "service": "order-service",
            "version": "1.2.3"
        }
        
        # Add extra fields if present
        if hasattr(record, 'request_id'):
            log_data['request_id'] = record.request_id
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
            
        return json.dumps(log_data)

# Setup
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("Order created", extra={"request_id": "abc-123", "user_id": "user-456"})

```

**Output:**
```json

{"timestamp": "2024-01-15T10:30:00.000Z", "level": "INFO", "logger": "__main__", "message": "Order created", "service": "order-service", "version": "1.2.3", "request_id": "abc-123", "user_id": "user-456"}

```

### 2.2 CloudWatch Logs

```bash
# Создание Log Group
aws logs create-log-group --log-group-name /app/order-service

# Log retention
aws logs put-retention-policy \
    --log-group-name /app/order-service \
    --retention-in-days 30

# Log Insights query
aws logs start-query \
    --log-group-name /app/order-service \
    --start-time $(date -d '1 hour ago' +%s) \
    --end-time $(date +%s) \
    --query-string 'fields @timestamp, @message
        | filter level = "ERROR"
        | sort @timestamp desc
        | limit 20'

```

### 2.3 Log Insights Query Examples

```sql

-- Errors by service
fields @timestamp, @message, service
| filter level = "ERROR"
| stats count(*) as error_count by service
| sort error_count desc

-- Latency percentiles
fields @timestamp, latency_ms
| stats avg(latency_ms) as avg,
        pct(latency_ms, 50) as p50,
        pct(latency_ms, 95) as p95,
        pct(latency_ms, 99) as p99
  by bin(5m)

-- Find slow requests
fields @timestamp, @message, latency_ms, request_id
| filter latency_ms > 1000
| sort latency_ms desc
| limit 10

```

---

## 3. Metrics

### 3.1 Типы метрик

```python

metric_types = {
    "Counter": {
        "description": "Монотонно растущее значение",
        "examples": ["requests_total", "errors_total", "bytes_sent"],
        "operations": ["rate()", "increase()"]
    },
    "Gauge": {
        "description": "Значение, которое может расти и уменьшаться",
        "examples": ["temperature", "active_connections", "queue_length"],
        "operations": ["current value", "avg", "min", "max"]
    },
    "Histogram": {
        "description": "Распределение значений (latency, size)",
        "examples": ["request_duration_seconds", "response_size_bytes"],
        "operations": ["percentiles (p50, p95, p99)", "avg"]
    },
    "Summary": {
        "description": "Похож на histogram, но вычисляет percentiles на клиенте",
        "examples": ["request_latency"],
        "operations": ["quantiles"]
    }
}

print("Metric Types:")
for metric_type, details in metric_types.items():
    print(f"\n{metric_type}:")
    print(f"  {details['description']}")
    print(f"  Examples: {', '.join(details['examples'][:2])}")

```

### 3.2 CloudWatch Metrics

```python

import boto3

cloudwatch = boto3.client('cloudwatch')

# Custom metric
cloudwatch.put_metric_data(
    Namespace='MyApp/OrderService',
    MetricData=[
        {
            'MetricName': 'OrderProcessingTime',
            'Dimensions': [
                {'Name': 'Environment', 'Value': 'production'},
                {'Name': 'OrderType', 'Value': 'standard'}
            ],
            'Value': 150.5,
            'Unit': 'Milliseconds'
        }
    ]
)

# Embedded Metric Format (EMF) - логи с метриками
import json

emf_log = {
    "_aws": {
        "Timestamp": 1705312200000,
        "CloudWatchMetrics": [{
            "Namespace": "MyApp/OrderService",
            "Dimensions": [["Environment", "OrderType"]],
            "Metrics": [{"Name": "ProcessingTime", "Unit": "Milliseconds"}]
        }]
    },
    "Environment": "production",
    "OrderType": "standard",
    "ProcessingTime": 150.5,
    "message": "Order processed"
}

print(json.dumps(emf_log))  # CloudWatch автоматически создаст метрику

```

### 3.3 RED Method

```python
# RED Method for microservices
red_metrics = {
    "Rate": "Requests per second",
    "Errors": "Failed requests per second", 
    "Duration": "Latency distribution (p50, p95, p99)"
}

# USE Method for resources (CPU, memory, disk)
use_metrics = {
    "Utilization": "Percentage of time resource is busy",
    "Saturation": "Amount of work queued",
    "Errors": "Count of error events"
}

print("RED Method (Services):")
for metric, desc in red_metrics.items():
    print(f"  {metric}: {desc}")

print("\nUSE Method (Resources):")
for metric, desc in use_metrics.items():
    print(f"  {metric}: {desc}")

```

---

## 4. Distributed Tracing

### 4.1 AWS X-Ray

```

┌────────────────────────────────────────────────────────────────────┐
│              X-Ray Trace                                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Trace ID: 1-abc-def                                               │
│  ─────────────────────────────────────────────────────────────     │
│                                                                    │
│  Segment: API Gateway                                              │
│  │─────────────────────│ 200ms                                     │
│       │                                                            │
│       ▼                                                            │
│  Segment: Lambda/OrderService                                      │
│       │──────────────│ 150ms                                       │
│       │   │                                                        │
│       │   ├── Subsegment: DynamoDB GetItem                         │
│       │   │   │────│ 20ms                                          │
│       │   │                                                        │
│       │   ├── Subsegment: External API Call                        │
│       │   │   │──────│ 50ms                                        │
│       │   │                                                        │
│       │   └── Subsegment: DynamoDB PutItem                         │
│       │       │───│ 15ms                                           │
│       │                                                            │
│       ▼                                                            │
│  Segment: SNS Publish                                              │
│       │──│ 10ms                                                    │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

### 4.2 X-Ray SDK

```python

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# Patch all supported libraries (boto3, requests, etc.)
patch_all()

@xray_recorder.capture('process_order')
def process_order(order_id: str):
    # Create subsegment
    subsegment = xray_recorder.begin_subsegment('validate_order')
    try:
        validate_order(order_id)
    finally:
        xray_recorder.end_subsegment()
    
    # Another subsegment
    with xray_recorder.in_subsegment('save_to_db'):
        # Add annotations (indexed, searchable)
        xray_recorder.put_annotation('order_id', order_id)
        xray_recorder.put_annotation('order_type', 'standard')
        
        # Add metadata (not indexed)
        xray_recorder.put_metadata('order_details', {'items': 5, 'total': 99.99})
        
        save_order(order_id)

# Lambda handler with X-Ray
def lambda_handler(event, context):
    # X-Ray automatically captures Lambda invocation
    return process_order(event['order_id'])

```

### 4.3 Trace Context Propagation

```python
# Propagate trace context between services
import requests

def call_downstream_service(data: dict):
    # Get current trace header
    header = xray_recorder.current_segment().get_origin_trace_header()
    
    # Pass to downstream service
    response = requests.post(
        'https://downstream-service/api',
        json=data,
        headers={'X-Amzn-Trace-Id': header.to_header_str()}
    )
    return response.json()

```

---

## 5. Alerting

### 5.1 CloudWatch Alarms

```python

cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='HighErrorRate',
    MetricName='5XXError',
    Namespace='AWS/ApiGateway',
    Dimensions=[
        {'Name': 'ApiName', 'Value': 'OrderAPI'}
    ],
    Statistic='Sum',
    Period=60,
    EvaluationPeriods=3,
    Threshold=10,
    ComparisonOperator='GreaterThanThreshold',
    AlarmActions=[
        'arn:aws:sns:us-east-1:123456789012:alerts'
    ],
    TreatMissingData='notBreaching'
)

```

### 5.2 Алертинг Best Practices

```python

alerting_practices = [
    "Alert on symptoms, not causes (high latency, not CPU)",
    "Use SLI/SLO for alerting thresholds",
    "Avoid alert fatigue - only actionable alerts",
    "Include runbook links in alert messages",
    "Use severity levels (critical, warning, info)",
    "Set up on-call rotation (PagerDuty, Opsgenie)"
]

print("Alerting Best Practices:")
for practice in alerting_practices:
    print(f"  • {practice}")

```

---

## 6. Dashboards

### 6.1 Структура Dashboard

```python

dashboard_structure = {
    "Top Level KPIs": [
        "Request rate", "Error rate", "Latency p99", "Availability"
    ],
    "Service Health": [
        "Per-service error rates",
        "Per-service latency",
        "Active instances/tasks"
    ],
    "Infrastructure": [
        "CPU utilization", "Memory usage",
        "Network I/O", "Disk I/O"
    ],
    "Dependencies": [
        "Database connections", "Cache hit rate",
        "External API latency"
    ],
    "Business Metrics": [
        "Orders per minute", "Revenue",
        "Active users"
    ]
}

print("Dashboard Structure:")
for section, metrics in dashboard_structure.items():
    print(f"\n{section}:")
    for metric in metrics[:3]:
        print(f"  • {metric}")

```

---

## 💡 Key Takeaways

- **Logs** — events, debugging, high cardinality

- **Metrics** — aggregated numbers, trends, alerting

- **Traces** — request flow across services

- **Structured Logging** — JSON format, correlation IDs

- **RED Method** — Rate, Errors, Duration for services

- **X-Ray** — distributed tracing for AWS

---

## 📚 Additional Resources

- [CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- [X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/)
- "Observability Engineering" by Charity Majors

---

## 🚀 Next Steps

**Следующие модули:**

- [22_Security](../22_Security/) — Security monitoring
- [23_CostManagement](../23_CostManagement/) — Cost observability

**Практика:**

1. Настройте CloudWatch dashboard для приложения
2. Добавьте X-Ray tracing в Lambda функции
3. Создайте алерты на метрики и логи



