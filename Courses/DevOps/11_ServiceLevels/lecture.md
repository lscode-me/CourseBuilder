# Service Levels
## SLI, SLO, SLA и Error Budgets

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [10_SRE](../10_SRE/) — Site Reliability Engineering
- Понимать основы мониторинга
- Знать метрики приложений (latency, availability, errors)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать SLI, SLO и SLA
- Определять правильные SLI для сервиса
- Устанавливать реалистичные SLO
- Рассчитывать и использовать error budgets
- Создавать SLO-based alerts

---

## 1. Определения

### 1.1 SLI (Service Level Indicator)

**SLI** — количественная метрика, описывающая аспект надёжности сервиса.

```python
sli_examples = {
    "availability": {
        "formula": "successful_requests / total_requests",
        "example": "99.5% запросов успешны (status 2xx)"
    },
    "latency": {
        "formula": "requests_under_threshold / total_requests",
        "example": "95% запросов выполняются менее 200ms"
    },
    "throughput": {
        "formula": "successful_operations / time_unit",
        "example": "Система обрабатывает 1000 RPS"
    },
    "error_rate": {
        "formula": "error_requests / total_requests",
        "example": "Менее 0.1% запросов с ошибкой 5xx"
    },
    "freshness": {
        "formula": "data_updated_within_threshold / total_data",
        "example": "95% данных обновлены за последние 5 минут"
    }
}
```

### 1.2 SLO (Service Level Objective)

**SLO** — целевое значение SLI, к которому стремится команда.

```python
# SLO = Target для SLI

slo_examples = {
    "availability_slo": {
        "sli": "Successful requests / Total requests",
        "target": "99.9%",
        "period": "Rolling 30 days"
    },
    "latency_slo": {
        "sli": "Requests < 200ms / Total requests",
        "target": "95%",
        "period": "Rolling 7 days"
    }
}
```

### 1.3 SLA (Service Level Agreement)

**SLA** — юридический контракт с последствиями при невыполнении.

```python
sla_example = {
    "commitment": "99.9% availability",
    "measurement_period": "Monthly",
    "consequences": {
        "99.9% - 99.5%": "10% credit",
        "99.5% - 99.0%": "25% credit",
        "< 99.0%": "50% credit"
    },
    "exclusions": [
        "Scheduled maintenance",
        "Customer-caused issues",
        "Force majeure"
    ]
}
```

### 1.4 Взаимосвязь

```
┌─────────────────────────────────────────────────────────────────┐
│                    SLI → SLO → SLA                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SLI (What we measure)                                          │
│  └── "Successful requests / Total requests"                     │
│                                                                 │
│       ↓                                                         │
│                                                                 │
│  SLO (What we aim for) - внутренняя цель                        │
│  └── "99.95% availability" (более строгий)                      │
│                                                                 │
│       ↓                                                         │
│                                                                 │
│  SLA (What we promise) - внешнее обязательство                  │
│  └── "99.9% availability" (с запасом от SLO)                    │
│                                                                 │
│  SLO > SLA (всегда оставляем buffer)                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Выбор SLI

### 2.1 Категории SLI

```python
sli_categories = {
    "request_driven": {
        "services": ["API", "Web servers", "Microservices"],
        "slis": [
            "Availability (success rate)",
            "Latency (P50, P99)",
            "Quality (correctness)"
        ]
    },
    "pipeline": {
        "services": ["Data pipelines", "ETL jobs"],
        "slis": [
            "Freshness (data age)",
            "Correctness",
            "Throughput"
        ]
    },
    "storage": {
        "services": ["Databases", "Object storage"],
        "slis": [
            "Availability",
            "Durability",
            "Latency"
        ]
    }
}
```

### 2.2 Good SLI Characteristics

```python
good_sli_characteristics = [
    "User-centric — отражает опыт пользователя",
    "Measurable — можно измерить автоматически",
    "Actionable — команда может влиять на него",
    "Stable — не меняется без изменений системы",
    "Simple — легко понять и объяснить"
]

# Хорошие SLI

good_slis = [
    "% HTTP 2xx responses",
    "P99 response time",
    "% successful logins"
]

# Плохие SLI

bad_slis = [
    "CPU usage",  # Не user-centric
    "Number of tickets",  # Не измеримо автоматически
    "Developer happiness"  # Субъективно
]
```

### 2.3 Формулы SLI

```python
# Availability SLI

def availability_sli(
    successful_requests: int,
    total_requests: int
) -> float:
    """
    SLI = (successful requests / total requests) * 100
    """
    if total_requests == 0:
        return 100.0
    return (successful_requests / total_requests) * 100

# Latency SLI

def latency_sli(
    requests_under_threshold: int,
    total_requests: int,
    threshold_ms: int = 200
) -> float:
    """
    SLI = (requests < threshold / total requests) * 100
    """
    if total_requests == 0:
        return 100.0
    return (requests_under_threshold / total_requests) * 100

# PromQL для SLI

sli_promql = {
    "availability": """
        sum(rate(http_requests_total{status=~"2.."}[5m]))
        /
        sum(rate(http_requests_total[5m]))
        * 100
    """,
    "latency_p99": """
        histogram_quantile(0.99,
            sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
        )
    """,
    "latency_sli": """
        sum(rate(http_request_duration_seconds_bucket{le="0.2"}[5m]))
        /
        sum(rate(http_request_duration_seconds_count[5m]))
        * 100
    """
}
```

---

## 3. Error Budget

### 3.1 Расчёт Error Budget

```python
def calculate_error_budget(
    slo_target: float,  # например 99.9
    period_minutes: int  # например 43200 (30 дней)
) -> dict:
    """Calculate error budget in various units."""
    
    error_budget_percentage = 100 - slo_target
    
    # Допустимые "плохие" минуты
    allowed_bad_minutes = period_minutes * (error_budget_percentage / 100)
    
    # Если SLI = requests, то % плохих запросов
    
    return {
        "slo_target": f"{slo_target}%",
        "error_budget_percentage": f"{error_budget_percentage}%",
        "allowed_downtime_minutes": round(allowed_bad_minutes, 1),
        "allowed_downtime_hours": round(allowed_bad_minutes / 60, 2)
    }

# Примеры

budgets = {
    "99%": calculate_error_budget(99.0, 43200),
    "99.9%": calculate_error_budget(99.9, 43200),
    "99.99%": calculate_error_budget(99.99, 43200)
}

for target, budget in budgets.items():
    print(f"{target}: {budget['allowed_downtime_hours']} hours/month")
```

**Output:**
```
99%: 7.2 hours/month
99.9%: 0.72 hours/month (43 minutes)
99.99%: 0.07 hours/month (4.3 minutes)
```

### 3.2 Error Budget Tracking

```python
# PromQL для tracking error budget

# Текущее потребление error budget (за последние 30 дней)

error_budget_consumption = """
    (
        1 - (
            sum(rate(http_requests_total{status=~"2.."}[30d]))
            /
            sum(rate(http_requests_total[30d]))
        )
    )
    /
    (1 - 0.999)  # SLO 99.9%
    * 100
"""

# Если результат > 100%, budget исчерпан
```

### 3.3 Error Budget Policies

```python
error_budget_policy = {
    "budget_healthy": {
        "condition": "consumption < 50%",
        "actions": [
            "Normal feature development",
            "Можно экспериментировать",
            "Допустимы рискованные изменения"
        ]
    },
    "budget_warning": {
        "condition": "50% <= consumption < 100%",
        "actions": [
            "Повысить осторожность",
            "Больше тестирования перед релизами",
            "Начать reliability инициативы"
        ]
    },
    "budget_exhausted": {
        "condition": "consumption >= 100%",
        "actions": [
            "STOP feature releases",
            "Только critical bug fixes",
            "Фокус на reliability",
            "Postmortem для каждого инцидента"
        ]
    }
}
```

---

## 4. SLO Best Practices

### 4.1 Установка SLO

```python
slo_setting_guidelines = {
    "start_conservative": {
        "advice": "Начните с менее строгого SLO",
        "example": "99% вместо 99.9%",
        "reason": "Легче ужесточить, чем ослабить"
    },
    "base_on_current_performance": {
        "advice": "Измерьте текущую reliability",
        "example": "Если сейчас 99.5%, SLO = 99%",
        "reason": "Реалистичные цели"
    },
    "consider_user_expectations": {
        "advice": "Что ожидают пользователи?",
        "example": "Payment API: 99.99%, Internal tool: 99%",
        "reason": "User-centric approach"
    },
    "leave_buffer_for_sla": {
        "advice": "SLO должен быть строже SLA",
        "example": "SLA 99.9% → SLO 99.95%",
        "reason": "Запас для неожиданностей"
    }
}
```

### 4.2 SLO Document Template

```markdown
# Service: Order API

## SLO Summary

| SLI | Target | Period | Priority |
|-----|--------|--------|----------|
| Availability | 99.9% | 30 days | P1 |
| Latency (P99) | < 500ms | 30 days | P1 |
| Latency (P50) | < 100ms | 30 days | P2 |

## SLI Definitions

### Availability

- **Definition**: Percentage of HTTP requests with 2xx status

- **Measurement**: Prometheus query on nginx ingress

- **Exclusions**: Health checks, admin endpoints

### Latency

- **Definition**: Response time measured at ingress

- **Measurement**: histogram_quantile on http_request_duration_seconds

## Error Budget Policy

- Budget > 50%: Normal operations
- Budget 20-50%: Increased caution, more testing
- Budget < 20%: Feature freeze, reliability focus
- Budget exhausted: Only critical fixes

## Stakeholders

- SLO Owner: @sre-team
- Service Owner: @order-team
```

### 4.3 SLO-based Alerting

```yaml
# Prometheus alert rules

groups:
  - name: slo-alerts
    rules:
      # Burn rate alert: быстрое сжигание budget
      - alert: HighErrorBudgetBurn
        expr: |
          (
            1 - (
              sum(rate(http_requests_total{status=~"2.."}[1h]))
              /
              sum(rate(http_requests_total[1h]))
            )
          )
          /
          (1 - 0.999)
          > 14.4  # Burn rate: 14.4x = budget исчерпается за 5 дней
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error budget burn rate"
          description: "At current rate, error budget will be exhausted in ~5 days"

      # Slow burn: медленное, но устойчивое сжигание
      - alert: SlowErrorBudgetBurn
        expr: |
          (
            1 - (
              sum(rate(http_requests_total{status=~"2.."}[6h]))
              /
              sum(rate(http_requests_total[6h]))
            )
          )
          /
          (1 - 0.999)
          > 1  # Burn rate > 1x за 6 часов
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "Elevated error budget consumption"
```

---

## 5. Multi-Window SLO

### 5.1 Burn Rate Alerting

```python
# Multi-window, multi-burn-rate alerting
# Как рекомендует Google SRE Book

burn_rate_windows = {
    "fast_burn": {
        "short_window": "5m",
        "long_window": "1h",
        "burn_rate": 14.4,  # Budget исчерпается за 5 дней
        "severity": "critical",
        "response": "Immediate page"
    },
    "slow_burn": {
        "short_window": "30m",
        "long_window": "6h",
        "burn_rate": 6,  # Budget исчерпается за 5 дней
        "severity": "warning",
        "response": "Investigate soon"
    },
    "gradual_burn": {
        "short_window": "2h",
        "long_window": "24h",
        "burn_rate": 1,  # Budget исчерпается точно в срок
        "severity": "info",
        "response": "Track and plan"
    }
}
```

---

## 6. Практические примеры

### 6.1 E-commerce API

```python
ecommerce_slos = {
    "checkout_api": {
        "availability": {
            "target": "99.99%",
            "reason": "Critical revenue path"
        },
        "latency_p99": {
            "target": "1s",
            "reason": "User experience"
        }
    },
    "product_catalog": {
        "availability": {
            "target": "99.9%",
            "reason": "Important but cacheable"
        },
        "freshness": {
            "target": "95% data < 5min old",
            "reason": "Price/stock updates"
        }
    },
    "recommendations": {
        "availability": {
            "target": "99%",
            "reason": "Graceful degradation possible"
        }
    }
}
```

### 6.2 Internal Tool

```python
internal_tool_slos = {
    "admin_dashboard": {
        "availability": {
            "target": "99%",
            "reason": "Internal use, business hours"
        },
        "latency_p99": {
            "target": "3s",
            "reason": "Complex queries acceptable"
        }
    }
}
```

---

## 💡 Key Takeaways

- **SLI → SLO → SLA**: Метрика → Цель → Контракт

- **User-centric SLIs**: Измеряйте то, что важно пользователям

- **Error Budget = 1 - SLO**: Бюджет на ошибки/эксперименты

- **SLO > SLA**: Внутренняя цель строже внешнего обязательства

- **Burn rate alerting**: Алерты на скорость расходования budget

---

## 🚀 Next Steps

**Related Modules:**

- [12_Incidents](../12_Incidents/) — Incident Management
- [13_Metrics](../13_Metrics/) — DORA Metrics

**Practice Ideas:**

1. Определите SLI для вашего сервиса
2. Рассчитайте текущий error budget
3. Настройте SLO-based alerts

---

## 📚 Additional Resources

**Documentation:**

- Google SRE Book — Chapter on SLOs
- "Implementing Service Level Objectives" by Alex Hidalgo

---





