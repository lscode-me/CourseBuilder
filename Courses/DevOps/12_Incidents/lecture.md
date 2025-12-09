# Incident Management
## On-Call, инциденты и Postmortems

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули по SRE и Service Levels
- Понимать основы мониторинга и алертинга
- Иметь опыт работы с production системами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Организовать эффективный on-call процесс
- Классифицировать и реагировать на инциденты
- Проводить blameless postmortems
- Создавать action items для предотвращения повторных инцидентов

---

## 1. Incident Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    Incident Lifecycle                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Detection ──▶ Triage ──▶ Response ──▶ Resolution ──▶ Postmortem│
│      │           │          │            │              │        │
│      ▼           ▼          ▼            ▼              ▼        │
│   Alert      Severity    Mitigation   Root Cause   Lessons      │
│   fires      assigned   deployed      identified   learned      │
│                                                                  │
│  Timeline:                                                       │
│  Minutes    Minutes    Minutes-Hours  Hours-Days   Days-Week    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. On-Call

### 2.1 On-Call Structure

```python
on_call_structure = {
    "primary": {
        "role": "Первая линия реагирования",
        "responsibility": "Реагировать на алерты, triage, mitigation",
        "escalation": "Secondary или team lead"
    },
    "secondary": {
        "role": "Backup для primary",
        "responsibility": "Помощь при сложных инцидентах",
        "escalation": "Team lead или management"
    }
}
```

### 2.2 On-Call Best Practices

```python
on_call_best_practices = {
    "rotation": {
        "length": "1 неделя обычно",
        "overlap": "Handoff meeting в начале смены",
        "distribution": "Равномерное распределение"
    },
    "alerts": {
        "actionable": "Только алерты, требующие действия",
        "documented": "Runbook для каждого алерта",
        "tested": "Регулярное тестирование алертов",
        "low_noise": "< 2 pages за смену в норме"
    },
    "support": {
        "tools": "Доступ ко всем нужным системам",
        "documentation": "Актуальные runbooks",
        "escalation": "Чёткий путь эскалации"
    }
}
```

### 2.3 On-Call Handoff

```markdown
# On-Call Handoff Template

## Outgoing: [Name] → Incoming: [Name]
## Date: [Date]

### Active Issues
- [ ] Issue 1: Description, status, next steps
- [ ] Issue 2: Description, status, next steps

### Recent Incidents
- INC-123 (Date): Brief summary, resolution, follow-up status

### Scheduled Maintenance
- Date/Time: Description, runbook link

### Known Issues / Flaky Alerts
- Alert X: Can be acknowledged, ticket Y tracking fix

### Notes
- Any context-specific information

### Handoff Confirmation
- [ ] Outgoing confirmed
- [ ] Incoming confirmed
```

---

## 3. Incident Classification

### 3.1 Severity Levels

```python
severity_levels = {
    "SEV1": {
        "description": "Critical — сервис недоступен",
        "impact": "Все пользователи затронуты",
        "response_time": "Немедленно",
        "example": "Production down, data loss"
    },
    "SEV2": {
        "description": "Major — значительное degradation",
        "impact": "Большинство пользователей затронуты",
        "response_time": "< 15 минут",
        "example": "Major feature broken, high latency"
    },
    "SEV3": {
        "description": "Minor — ограниченное влияние",
        "impact": "Часть пользователей затронута",
        "response_time": "< 1 час",
        "example": "Non-critical feature broken"
    },
    "SEV4": {
        "description": "Low — минимальное влияние",
        "impact": "Единичные пользователи",
        "response_time": "Next business day",
        "example": "Cosmetic issue, workaround exists"
    }
}
```

### 3.2 Incident Roles

```python
incident_roles = {
    "incident_commander": {
        "responsibility": "Координация response",
        "tasks": [
            "Объявляет severity",
            "Координирует команду",
            "Принимает решения",
            "Коммуницирует со stakeholders"
        ]
    },
    "technical_lead": {
        "responsibility": "Техническое расследование",
        "tasks": [
            "Анализ проблемы",
            "Разработка fix/mitigation",
            "Координация technical work"
        ]
    },
    "communications_lead": {
        "responsibility": "Коммуникации",
        "tasks": [
            "Статус updates для stakeholders",
            "Внутренняя коммуникация",
            "Внешняя коммуникация (если нужно)"
        ]
    },
    "scribe": {
        "responsibility": "Документация",
        "tasks": [
            "Записывает timeline",
            "Документирует решения",
            "Собирает информацию для postmortem"
        ]
    }
}
```

---

## 4. Incident Response

### 4.1 Response Procedure

```markdown
# Incident Response Procedure

## 1. Detection & Acknowledgment (0-5 min)
- [ ] Acknowledge alert in PagerDuty/OpsGenie
- [ ] Join incident channel (#incident-YYYYMMDD)
- [ ] Initial assessment of impact

## 2. Triage (5-15 min)
- [ ] Determine severity level
- [ ] Assign incident commander (if SEV1/SEV2)
- [ ] Identify affected services
- [ ] Notify stakeholders

## 3. Investigation (ongoing)
- [ ] Review recent changes (deploys, configs)
- [ ] Check monitoring dashboards
- [ ] Analyze logs
- [ ] Identify root cause or contributing factors

## 4. Mitigation (priority)
- [ ] Implement immediate mitigation
- [ ] Options: rollback, feature flag, scaling, restart
- [ ] Verify mitigation effectiveness

## 5. Resolution
- [ ] Confirm service restored
- [ ] Monitor for regression
- [ ] Update status page

## 6. Follow-up
- [ ] Schedule postmortem (for SEV1/SEV2)
- [ ] Create follow-up tickets
- [ ] Update runbooks if needed
```

### 4.2 Communication Templates

```markdown
# Incident Status Update Template

## Incident: [Brief Title]
## Severity: SEV[1/2/3/4]
## Status: [Investigating/Identified/Monitoring/Resolved]

### Impact
[What services are affected? How many users?]

### Current Status
[What are we doing now?]

### Timeline
- HH:MM — Alert triggered
- HH:MM — Investigation started
- HH:MM — [Latest update]

### Next Update
[When will we provide the next update?]

### Contact
Incident Commander: @name
```

---

## 5. Postmortem

### 5.1 Blameless Culture

```python
blameless_principles = [
    "Люди действуют с лучшими намерениями",
    "Ошибки — результат системных проблем, не людей",
    "Фокус на процессах, не на обвинениях",
    "Безопасность признания ошибок",
    "Цель — улучшение системы, не наказание"
]

# Плохо
blame_language = [
    "Кто это сделал?",
    "Почему вы не проверили?",
    "Это была ошибка [имя]"
]

# Хорошо
blameless_language = [
    "Что в системе позволило этому произойти?",
    "Какие проверки могли бы предотвратить это?",
    "Как можно улучшить процесс?"
]
```

### 5.2 Postmortem Template

```markdown
# Postmortem: [Incident Title]

## Incident ID: INC-XXXX
## Date: YYYY-MM-DD
## Duration: X hours Y minutes
## Severity: SEV[1/2/3/4]
## Author: [Name]
## Status: [Draft/In Review/Published]

---

## Summary
[2-3 sentences describing what happened and impact]

---

## Impact
- **Duration**: X hours Y minutes
- **Users affected**: [number or percentage]
- **Revenue impact**: [if applicable]
- **Data loss**: [yes/no, details]

---

## Timeline (all times UTC)

| Time | Event |
|------|-------|
| 14:32 | Alert fired: API error rate > 5% |
| 14:35 | On-call acknowledged, started investigation |
| 14:42 | Identified: database connection exhaustion |
| 14:55 | Mitigation: increased connection pool size |
| 15:19 | Service fully recovered |
| 15:30 | Incident closed |

---

## Root Cause
[Detailed technical explanation of what caused the incident]

A new feature deployed at 14:00 introduced a bug that caused
database connections to not be properly released. Under normal
load, this wasn't noticeable, but during a traffic spike at 14:30,
the connection pool was exhausted.

---

## Contributing Factors
- [ ] Recent change/deploy
- [ ] Configuration issue
- [ ] Capacity/scaling
- [ ] Dependency failure
- [ ] Human error
- [ ] Monitoring gap

**Details:**
1. The code change was not tested under load
2. Connection pool size alert threshold was too high
3. No circuit breaker for database calls

---

## Resolution
[How was the incident resolved?]

1. Temporary fix: Increased connection pool from 50 to 200
2. Restarted affected pods to clear stuck connections
3. Deployed hotfix to properly close connections

---

## Lessons Learned

### What went well
- Alert fired quickly (< 3 min after problem started)
- Team responded promptly
- Clear communication throughout

### What went wrong
- Load testing didn't cover this scenario
- Runbook for connection issues was outdated
- Initial mitigation attempt (restart) didn't help

### Where we got lucky
- Traffic spike was moderate; worse spike would have been worse
- Database itself didn't crash

---

## Action Items

| Action | Owner | Priority | Due Date | Status |
|--------|-------|----------|----------|--------|
| Add load test for connection handling | @dev-lead | P1 | 2024-02-01 | TODO |
| Update connection pool alert threshold | @sre | P1 | 2024-01-20 | TODO |
| Add circuit breaker for DB calls | @dev | P2 | 2024-02-15 | TODO |
| Update runbook | @on-call | P2 | 2024-01-25 | TODO |

---

## Appendix
- [Link to incident channel]
- [Link to relevant dashboards]
- [Link to deploy that caused issue]
```

### 5.3 5 Whys Analysis

```python
def five_whys_example():
    """Example of 5 Whys analysis for root cause."""
    
    problem = "Website was down for 30 minutes"
    
    whys = [
        ("Why was website down?", 
         "Database connections exhausted"),
        
        ("Why were connections exhausted?",
         "Connections weren't being released properly"),
        
        ("Why weren't connections released?",
         "Bug in new feature code"),
        
        ("Why wasn't bug caught before deploy?",
         "No load tests for connection handling"),
        
        ("Why no load tests for this scenario?",
         "Load test coverage requirements not defined")
    ]
    
    root_cause = "Need to define and enforce load test coverage requirements"
    
    return {
        "problem": problem,
        "analysis": whys,
        "root_cause": root_cause
    }
```

---

## 6. Improving Incident Response

### 6.1 Metrics to Track

```python
incident_metrics = {
    "mttd": {
        "name": "Mean Time to Detect",
        "description": "Время от начала проблемы до обнаружения",
        "target": "< 5 minutes"
    },
    "mtta": {
        "name": "Mean Time to Acknowledge",
        "description": "Время от алерта до acknowledge",
        "target": "< 5 minutes"
    },
    "mttr": {
        "name": "Mean Time to Resolve",
        "description": "Время от обнаружения до resolution",
        "target": "< 1 hour for SEV1"
    },
    "incident_count": {
        "name": "Incident Count",
        "description": "Количество инцидентов за период",
        "target": "Trending down"
    }
}
```

### 6.2 Continuous Improvement

```python
improvement_practices = [
    "Регулярный review метрик инцидентов",
    "Quarterly review of top incident causes",
    "Game days / chaos engineering",
    "Regular runbook reviews and updates",
    "Post-postmortem: проверка выполнения action items"
]
```

---

## 💡 Key Takeaways

- **Blameless culture**: Фокус на системах, не на людях

- **Clear roles**: Incident Commander, Tech Lead, Comms, Scribe

- **Documentation**: Timeline, decisions, action items

- **Action items**: Конкретные, с owner и deadline

- **Metrics**: MTTD, MTTA, MTTR для измерения прогресса

---

## 🚀 Next Steps

**Related Modules:**
- [13_Metrics](../13_Metrics/) — DORA Metrics
- [08_Monitoring](../08_Monitoring/) — Alerting

**Practice Ideas:**
1. Создайте incident response runbook
2. Проведите mock incident drill
3. Напишите postmortem по прошлому инциденту

---

## 📚 Additional Resources

**Books:**
- "Site Reliability Engineering" by Google — Incident Management chapter
- "The DevOps Handbook" — Learning from failures

**Tools:**
- PagerDuty
- OpsGenie
- Incident.io

---

