# Site Reliability Engineering
## Инженерный подход к операциям от Google

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули по мониторингу и observability
- Понимать принципы DevOps
- Иметь опыт работы с production системами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы и практики SRE
- Определять и устранять toil
- Применять принцип error budgets
- Проектировать системы с учётом надёжности
- Организовать on-call процесс

---

## 1. Что такое SRE?

### 1.1 Определение

**Site Reliability Engineering (SRE)** — дисциплина, которая применяет аспекты software engineering к операциям инфраструктуры.

> "SRE is what happens when you ask a software engineer to design an operations team."
> — Ben Treynor, VP of Engineering at Google

### 1.2 SRE vs DevOps

```python
comparison = {
    "DevOps": {
        "type": "Культура и философия",
        "focus": "Collaboration Dev + Ops",
        "origin": "Community (2009)",
        "approach": "General principles"
    },
    "SRE": {
        "type": "Конкретная реализация",
        "focus": "Reliability engineering",
        "origin": "Google (2003)",
        "approach": "Specific practices and metrics"
    }
}

# Google's view:
# "class SRE implements DevOps"
```

### 1.3 Ключевые принципы SRE

```python
sre_principles = [
    "Embracing risk — баланс надёжности и скорости развития",
    "SLOs — измеримые цели надёжности",
    "Eliminating toil — автоматизация рутины",
    "Monitoring — три столпа observability",
    "Automation — software engineering для ops",
    "Release engineering — безопасные релизы",
    "Simplicity — простота систем"
]
```

---

## 2. Embracing Risk

### 2.1 Стоимость надёжности

```python
# Добавление каждой "девятки" экспоненциально дороже

reliability_cost = {
    "99%": {
        "downtime_per_year": "3.65 days",
        "effort": "Basic monitoring",
        "cost_multiplier": 1
    },
    "99.9%": {
        "downtime_per_year": "8.76 hours",
        "effort": "Redundancy, automated failover",
        "cost_multiplier": 10
    },
    "99.99%": {
        "downtime_per_year": "52.6 minutes",
        "effort": "Multi-region, extensive testing",
        "cost_multiplier": 100
    },
    "99.999%": {
        "downtime_per_year": "5.26 minutes",
        "effort": "Massive engineering investment",
        "cost_multiplier": 1000
    }
}
```

### 2.2 Error Budget

**Error Budget** = допустимое количество ошибок/даунтайма.

```python
# Error Budget = 1 - SLO

# Если SLO = 99.9%

slo = 0.999
error_budget = 1 - slo  # 0.1% = 0.001

# За 30 дней (43,200 минут):

minutes_per_month = 30 * 24 * 60  # 43,200
allowed_downtime = minutes_per_month * error_budget  # 43.2 минуты

print(f"Error budget: {allowed_downtime:.1f} minutes per month")
# Output: Error budget: 43.2 minutes per month
```

### 2.3 Использование Error Budget

```python
error_budget_policies = {
    "budget_available": {
        "description": "Error budget не исчерпан",
        "actions": [
            "Можно деплоить новые фичи",
            "Можно экспериментировать",
            "Фокус на development"
        ]
    },
    "budget_exhausted": {
        "description": "Error budget исчерпан",
        "actions": [
            "Остановить feature releases",
            "Фокус на reliability",
            "Исправление root causes",
            "Добавление мониторинга"
        ]
    }
}
```

---

## 3. Toil

### 3.1 Определение Toil

**Toil** — работа, которая:

- Manual (ручная)
- Repetitive (повторяющаяся)
- Automatable (автоматизируемая)
- Tactical (тактическая, не стратегическая)
- No enduring value (не добавляет долгосрочной ценности)
- Scales linearly with service growth

### 3.2 Примеры Toil

```python
toil_examples = {
    "is_toil": [
        "Ручной перезапуск сервиса при сбое",
        "Ручная проверка логов каждое утро",
        "Ручное масштабирование при нагрузке",
        "Ручная очистка диска",
        "Ручное создание пользователей"
    ],
    "not_toil": [
        "Написание автоматизации",
        "Планирование capacity",
        "Design reviews",
        "Postmortem analysis",
        "On-call (если не чрезмерно)"
    ]
}
```

### 3.3 Измерение и устранение Toil

```python
# Цель Google: SRE тратит максимум 50% времени на toil

MAX_TOIL_PERCENTAGE = 50

def calculate_toil_percentage(toil_hours: float, total_hours: float) -> float:
    return (toil_hours / total_hours) * 100

def should_automate(
    time_spent_weekly: float,  # часов в неделю на задачу
    automation_time: float,     # часов на автоматизацию
) -> dict:
    """Determine if task should be automated."""
    
    # Если автоматизация окупится за 6 месяцев
    weeks_to_roi = automation_time / time_spent_weekly
    months_to_roi = weeks_to_roi / 4
    
    return {
        "weeks_to_roi": weeks_to_roi,
        "months_to_roi": months_to_roi,
        "should_automate": months_to_roi <= 6,
        "annual_savings": time_spent_weekly * 52 - automation_time
    }

# Пример

result = should_automate(
    time_spent_weekly=2,      # 2 часа в неделю
    automation_time=16        # 16 часов на автоматизацию
)
print(f"Should automate: {result['should_automate']}")
print(f"ROI in {result['months_to_roi']:.1f} months")
print(f"Annual savings: {result['annual_savings']:.0f} hours")
```

---

## 4. SRE Practices

### 4.1 Capacity Planning

```python
def capacity_planning(
    current_usage: float,      # Текущее использование (%)
    growth_rate: float,        # Месячный рост (%)
    provision_threshold: float = 70,  # Порог для provision
    lead_time_months: int = 2  # Время на provision
) -> dict:
    """Calculate when to provision more capacity."""
    
    months_to_threshold = 0
    usage = current_usage
    
    while usage < provision_threshold:
        usage *= (1 + growth_rate / 100)
        months_to_threshold += 1
        if months_to_threshold > 24:  # Safety limit
            break
    
    provision_at_month = months_to_threshold - lead_time_months
    
    return {
        "current_usage": current_usage,
        "months_to_threshold": months_to_threshold,
        "provision_at_month": max(0, provision_at_month),
        "urgency": "high" if provision_at_month <= 1 else "normal"
    }

# Пример

result = capacity_planning(
    current_usage=55,
    growth_rate=5,
    provision_threshold=70,
    lead_time_months=2
)
print(f"Provision in {result['provision_at_month']} months")
```

### 4.2 Release Engineering

```python
release_engineering_practices = {
    "hermetic_builds": "Воспроизводимые сборки",
    "progressive_rollouts": "Постепенное развёртывание",
    "automated_testing": "Автоматические тесты всех уровней",
    "feature_flags": "Контроль над новым функционалом",
    "quick_rollback": "Быстрый откат (< 5 минут)",
    "canary_releases": "Тестирование на части трафика"
}
```

### 4.3 On-Call Best Practices

```python
on_call_best_practices = {
    "rotation": {
        "primary_secondary": "Primary + Secondary on-call",
        "rotation_length": "1 неделя обычно",
        "handoff": "Документированный handoff",
        "equal_distribution": "Справедливое распределение"
    },
    "alerts": {
        "actionable": "Только actionable алерты",
        "documented": "Runbook для каждого алерта",
        "severity_levels": "P1-P4 с разным SLA",
        "low_noise": "< 2 pages за on-call shift"
    },
    "support": {
        "escalation_path": "Чёткий путь эскалации",
        "expert_access": "Доступ к экспертам",
        "postmortem": "Blameless postmortem после инцидентов"
    }
}
```

---

## 5. SRE Team Structure

### 5.1 Модели организации

```python
sre_team_models = {
    "embedded": {
        "description": "SRE встроен в product team",
        "pros": ["Глубокое понимание продукта", "Быстрая коммуникация"],
        "cons": ["Может терять SRE экспертизу", "Нет community"],
        "when": "Небольшие организации"
    },
    "dedicated": {
        "description": "Отдельная SRE команда",
        "pros": ["Сильная экспертиза", "Стандарты", "Community"],
        "cons": ["Может быть bottleneck", "Меньше контекста продукта"],
        "when": "Крупные организации"
    },
    "consulting": {
        "description": "SRE как внутренние консультанты",
        "pros": ["Масштабируемость", "Best practices"],
        "cons": ["Меньше ownership", "Медленнее реагирование"],
        "when": "Много продуктовых команд"
    }
}
```

### 5.2 SRE Responsibilities

```python
sre_responsibilities = {
    "50_percent_engineering": [
        "Разработка инструментов автоматизации",
        "Улучшение мониторинга",
        "Capacity planning",
        "Performance optimization"
    ],
    "50_percent_ops": [
        "On-call",
        "Incident response",
        "Change management",
        "Postmortems"
    ]
}
```

---

## 6. Production Readiness

### 6.1 Production Readiness Review (PRR)

```python
prr_checklist = {
    "architecture": [
        "Architecture documented",
        "Dependencies identified",
        "Single points of failure addressed"
    ],
    "reliability": [
        "SLOs defined",
        "Error budget established",
        "Disaster recovery plan"
    ],
    "monitoring": [
        "Metrics instrumented",
        "Alerts configured",
        "Dashboards created",
        "Logs structured"
    ],
    "operations": [
        "Runbooks written",
        "On-call rotation established",
        "Escalation path defined",
        "Capacity planning done"
    ],
    "security": [
        "Security review completed",
        "Access controls configured",
        "Secrets management"
    ]
}
```

---

## 💡 Key Takeaways

- **SRE = Software Engineering для Ops**: Применяем engineering подход к reliability

- **Error Budget**: Баланс между reliability и velocity

- **Toil < 50%**: Автоматизируем рутину, освобождаем время для engineering

- **Измеримые цели (SLOs)**: Без метрик нет управления

- **Blameless culture**: Учимся на ошибках, не ищем виноватых

---

## 🚀 Next Steps

**Related Modules:**

- [11_ServiceLevels](../11_ServiceLevels/) — SLI, SLO, SLA
- [12_Incidents](../12_Incidents/) — Incident Management

**Practice Ideas:**

1. Измерьте процент toil в вашей работе
2. Определите error budget для сервиса
3. Проведите Production Readiness Review

---

## 📚 Additional Resources

**Books:**

- "Site Reliability Engineering" by Google
- "The Site Reliability Workbook" by Google
- "Seeking SRE" by David Blank-Edelman

---





