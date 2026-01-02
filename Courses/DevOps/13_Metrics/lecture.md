# Метрики DevOps
## DORA Metrics и измерение эффективности

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули по CI/CD и Processes
- Понимать DevOps lifecycle
- Иметь опыт работы с Git и deployment pipelines

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить DORA четыре ключевые метрики
- Измерять deployment frequency и lead time
- Отслеживать change failure rate и MTTR
- Использовать метрики для улучшения процессов

---

## 1. DORA Metrics

### 1.1 Что такое DORA?

**DORA (DevOps Research and Assessment)** — исследовательская группа (теперь часть Google Cloud), которая провела многолетнее научное исследование практик DevOps.

### 1.2 Четыре ключевые метрики

```python
dora_metrics = {
    "deployment_frequency": {
        "description": "Как часто организация деплоит в production",
        "category": "Throughput (скорость)",
        "elite": "On-demand (несколько раз в день)",
        "high": "Daily to weekly",
        "medium": "Weekly to monthly",
        "low": "Monthly to yearly"
    },
    "lead_time_for_changes": {
        "description": "Время от commit до production",
        "category": "Throughput (скорость)",
        "elite": "< 1 hour",
        "high": "1 day to 1 week",
        "medium": "1 week to 1 month",
        "low": "1 month to 6 months"
    },
    "change_failure_rate": {
        "description": "Процент деплоев, вызывающих сбои",
        "category": "Stability (стабильность)",
        "elite": "0-15%",
        "high": "16-30%",
        "medium": "16-30%",
        "low": "16-30%"
    },
    "mttr": {
        "description": "Время восстановления после сбоя",
        "category": "Stability (стабильность)",
        "elite": "< 1 hour",
        "high": "< 1 day",
        "medium": "1 day to 1 week",
        "low": "1 week to 1 month"
    }
}
```

### 1.3 Классификация команд

```
┌──────────────────────────────────────────────────────────────────┐
│                    DORA Performance Levels                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ELITE Performers (~7% of organizations)                         │
│  • Deploy: On-demand                                             │
│  • Lead time: < 1 hour                                           │
│  • Change failure: 0-15%                                         │
│  • MTTR: < 1 hour                                                │
│                                                                  │
│  HIGH Performers (~26%)                                          │
│  • Deploy: Daily-Weekly                                          │
│  • Lead time: 1 day - 1 week                                     │
│  • Change failure: 16-30%                                        │
│  • MTTR: < 1 day                                                 │
│                                                                  │
│  MEDIUM Performers (~37%)                                        │
│  • Deploy: Weekly-Monthly                                        │
│  • Lead time: 1 week - 1 month                                   │
│  • Change failure: 16-30%                                        │
│  • MTTR: 1 day - 1 week                                          │
│                                                                  │
│  LOW Performers (~30%)                                           │
│  • Deploy: Monthly-Yearly                                        │
│  • Lead time: 1-6 months                                         │
│  • Change failure: 16-30%                                        │
│  • MTTR: 1 week - 1 month                                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Измерение метрик

### 2.1 Deployment Frequency

```python
from datetime import datetime, timedelta
from collections import defaultdict

def calculate_deployment_frequency(
    deployments: list[dict],
    period_days: int = 30
) -> dict:
    """Calculate deployment frequency."""
    
    cutoff = datetime.now() - timedelta(days=period_days)
    recent = [d for d in deployments if d["timestamp"] > cutoff]
    
    total = len(recent)
    per_day = total / period_days
    
    # Классификация
    if per_day >= 1:
        level = "elite"
    elif per_day >= 0.14:  # ~weekly
        level = "high"
    elif per_day >= 0.03:  # ~monthly
        level = "medium"
    else:
        level = "low"
    
    return {
        "total_deployments": total,
        "deployments_per_day": round(per_day, 2),
        "period_days": period_days,
        "level": level
    }

# Пример использования

deployments = [
    {"timestamp": datetime.now() - timedelta(hours=i*8), "service": "api"}
    for i in range(90)  # 3 деплоя в день за 30 дней
]

result = calculate_deployment_frequency(deployments)
print(f"Deployment frequency: {result['deployments_per_day']}/day")
print(f"Level: {result['level']}")
```

### 2.2 Lead Time for Changes

```python
def calculate_lead_time(
    changes: list[dict]  # {"commit_time": datetime, "deploy_time": datetime}
) -> dict:
    """Calculate lead time for changes."""
    
    lead_times = []
    for change in changes:
        lt = change["deploy_time"] - change["commit_time"]
        lead_times.append(lt.total_seconds() / 3600)  # hours
    
    if not lead_times:
        return {"error": "No changes"}
    
    avg_hours = sum(lead_times) / len(lead_times)
    median_hours = sorted(lead_times)[len(lead_times) // 2]
    p90_hours = sorted(lead_times)[int(len(lead_times) * 0.9)]
    
    # Классификация (по median)
    if median_hours < 1:
        level = "elite"
    elif median_hours < 24 * 7:  # 1 week
        level = "high"
    elif median_hours < 24 * 30:  # 1 month
        level = "medium"
    else:
        level = "low"
    
    return {
        "avg_hours": round(avg_hours, 2),
        "median_hours": round(median_hours, 2),
        "p90_hours": round(p90_hours, 2),
        "level": level
    }
```

### 2.3 Change Failure Rate

```python
def calculate_change_failure_rate(
    deployments: list[dict]  # {"timestamp": datetime, "caused_incident": bool}
) -> dict:
    """Calculate change failure rate."""
    
    total = len(deployments)
    failures = len([d for d in deployments if d.get("caused_incident", False)])
    
    if total == 0:
        return {"error": "No deployments"}
    
    rate = (failures / total) * 100
    
    # Классификация
    if rate <= 15:
        level = "elite"
    elif rate <= 30:
        level = "high"
    else:
        level = "low"
    
    return {
        "total_deployments": total,
        "failed_deployments": failures,
        "failure_rate_percent": round(rate, 2),
        "level": level
    }
```

### 2.4 Mean Time to Recovery (MTTR)

```python
def calculate_mttr(
    incidents: list[dict]  # {"start": datetime, "resolved": datetime}
) -> dict:
    """Calculate Mean Time to Recovery."""
    
    recovery_times = []
    for inc in incidents:
        rt = inc["resolved"] - inc["start"]
        recovery_times.append(rt.total_seconds() / 3600)  # hours
    
    if not recovery_times:
        return {"error": "No incidents"}
    
    avg_hours = sum(recovery_times) / len(recovery_times)
    
    # Классификация
    if avg_hours < 1:
        level = "elite"
    elif avg_hours < 24:
        level = "high"
    elif avg_hours < 24 * 7:
        level = "medium"
    else:
        level = "low"
    
    return {
        "avg_recovery_hours": round(avg_hours, 2),
        "total_incidents": len(recovery_times),
        "level": level
    }
```

---

## 3. Сбор данных для метрик

### 3.1 Источники данных

```python
data_sources = {
    "deployment_frequency": [
        "CI/CD pipeline (GitHub Actions, GitLab CI)",
        "Kubernetes events",
        "ArgoCD sync events",
        "Deploy tags in Git"
    ],
    "lead_time": [
        "Git commits + deployment timestamps",
        "PR merge time + deploy time",
        "CI/CD pipeline metrics"
    ],
    "change_failure_rate": [
        "Incident management system",
        "Rollback events",
        "Correlation: deploy time + incident start"
    ],
    "mttr": [
        "Incident management system",
        "PagerDuty/OpsGenie",
        "Custom incident tracking"
    ]
}
```

### 3.2 Автоматизация сбора

```yaml
# GitHub Actions для tracking deployments

name: Track Deployment

on:
  workflow_run:
    workflows: ["Deploy"]
    types: [completed]

jobs:
  track:
    runs-on: ubuntu-latest
    steps:
      - name: Record deployment
        run: |
          curl -X POST "$METRICS_API/deployments" \
            -H "Authorization: Bearer ${{ secrets.METRICS_TOKEN }}" \
            -d '{
              "service": "${{ github.repository }}",
              "sha": "${{ github.sha }}",
              "timestamp": "${{ github.event.workflow_run.updated_at }}",
              "status": "${{ github.event.workflow_run.conclusion }}"
            }'
```

---

## 4. Использование метрик

### 4.1 Dashboard

```python
# Структура DORA dashboard

dashboard_panels = {
    "deployment_frequency": {
        "type": "stat",
        "query": "deployments_per_day",
        "thresholds": {"elite": 1, "high": 0.14}
    },
    "lead_time": {
        "type": "gauge",
        "query": "median_lead_time_hours",
        "thresholds": {"elite": 1, "high": 168}  # hours
    },
    "change_failure_rate": {
        "type": "gauge",
        "query": "failed_deployments_percent",
        "thresholds": {"elite": 15, "acceptable": 30}
    },
    "mttr": {
        "type": "gauge",
        "query": "avg_recovery_hours",
        "thresholds": {"elite": 1, "high": 24}
    },
    "trends": {
        "type": "timeseries",
        "queries": ["df_weekly", "lt_weekly", "cfr_weekly", "mttr_weekly"]
    }
}
```

### 4.2 Improvement Actions

```python
improvement_actions = {
    "low_deployment_frequency": [
        "Уменьшить batch size (меньше изменений за релиз)",
        "Автоматизировать тестирование",
        "Упростить процесс approval",
        "Внедрить feature flags"
    ],
    "high_lead_time": [
        "Оптимизировать CI pipeline",
        "Уменьшить время code review",
        "Автоматизировать тестирование",
        "Trunk-based development"
    ],
    "high_failure_rate": [
        "Улучшить тестирование (coverage, E2E)",
        "Canary deployments",
        "Feature flags",
        "Staging environment parity"
    ],
    "high_mttr": [
        "Улучшить observability",
        "Актуальные runbooks",
        "Тренировки по incident response",
        "Автоматический rollback"
    ]
}
```

---

## 5. Другие важные метрики

### 5.1 Developer Experience Metrics

```python
dx_metrics = {
    "build_time": {
        "description": "Время сборки в CI",
        "target": "< 10 minutes"
    },
    "test_time": {
        "description": "Время выполнения тестов",
        "target": "< 15 minutes for unit + integration"
    },
    "pr_review_time": {
        "description": "Время от PR creation до merge",
        "target": "< 24 hours"
    },
    "onboarding_time": {
        "description": "Время до первого PR для нового разработчика",
        "target": "< 1 week"
    }
}
```

### 5.2 Reliability Metrics

```python
reliability_metrics = {
    "availability": {
        "description": "% времени сервис доступен",
        "calculation": "uptime / total_time * 100"
    },
    "error_budget_remaining": {
        "description": "Оставшийся error budget",
        "calculation": "(allowed_errors - actual_errors) / allowed_errors * 100"
    },
    "incident_count": {
        "description": "Количество инцидентов за период",
        "target": "Trending down"
    }
}
```

---

## 💡 Key Takeaways

- **DORA четыре ключевые метрики**: DF, Lead Time, CFR, MTTR

- **Throughput + Stability**: Скорость и стабильность не противоречат друг другу

- **Elite performers**: Деплоят чаще И имеют меньше проблем

- **Метрики для улучшения**: Измеряем → Анализируем → Улучшаем

- **Автоматизация сбора**: Метрики должны собираться автоматически

---

## 🚀 Next Steps

**Related Modules:**

- [14_DevSecOps](../14_DevSecOps/) — Security metrics
- [04_CI](../04_CI/) — CI optimization

**Practice Ideas:**

1. Измерьте текущие DORA метрики вашей команды
2. Создайте dashboard для tracking
3. Определите топ-3 улучшения

---

## 📚 Additional Resources

**Reports:**

- [State of DevOps Report](https://dora.dev/)
- "Accelerate" by Nicole Forsgren

**Tools:**

- [Four Keys](https://github.com/dora-team/fourkeys) — Open source DORA metrics
- LinearB, Sleuth, Faros.ai

---





