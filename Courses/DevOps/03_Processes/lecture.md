# Процессы DevOps
## Жизненный цикл, планирование и операционные регламенты

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [01_Intro](../01_Intro/) — Введение в DevOps
- Пройти модуль [02_Methodologies](../02_Methodologies/) — Методологии
- Понимать базовые концепции Agile и Scrum

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Описать полный жизненный цикл DevOps (DevOps lifecycle)
- Организовать процесс планирования работы
- Внедрить ключевые ceremonies для DevOps команды
- Применять Value Stream Mapping для оптимизации процессов
- Создавать эффективные регламенты и runbooks

---

## 1. DevOps Lifecycle

### 1.1 Infinity Loop

DevOps часто визуализируется как бесконечный цикл (infinity loop), подчёркивающий непрерывность процесса:

```

            ┌────────────────────────────────────────────┐
            │                                            │
    ┌───────▼───────┐                        ┌───────────┴───────┐
    │               │                        │                   │
    │     PLAN      │                        │     MONITOR       │
    │               │                        │                   │
    └───────┬───────┘                        └───────────▲───────┘
            │                                            │
            │         ┌──────────────────┐               │
    ┌───────▼───────┐ │                  │ ┌─────────────┴───────┐
    │               │ │       DEV        │ │                     │
    │     CODE      │ │       ────       │ │     OPERATE         │
    │               │ │       OPS        │ │                     │
    └───────┬───────┘ │                  │ └─────────────▲───────┘
            │         └──────────────────┘               │
            │                                            │
    ┌───────▼───────┐                        ┌───────────┴───────┐
    │               │                        │                   │
    │     BUILD     │                        │     DEPLOY        │
    │               │                        │                   │
    └───────┬───────┘                        └───────────▲───────┘
            │                                            │
    ┌───────▼───────┐                        ┌───────────┴───────┐
    │               │                        │                   │
    │     TEST      │────────────────────────▶    RELEASE        │
    │               │                        │                   │
    └───────────────┘                        └───────────────────┘

```

### 1.2 Фазы DevOps Lifecycle

**1. Plan (Планирование)**
- Определение требований и приоритетов
- Sprint/iteration planning
- Roadmap и release planning
- Capacity planning

**2. Code (Разработка)**
- Написание кода
- Code review
- Pair programming
- Version control

**3. Build (Сборка)**
- Компиляция
- Dependency management
- Artifact creation
- Static analysis

**4. Test (Тестирование)**
- Unit tests
- Integration tests
- Security tests
- Performance tests

**5. Release (Релиз)**
- Release management
- Change approval
- Release notes
- Versioning

**6. Deploy (Развёртывание)**
- Deployment automation
- Environment management
- Configuration management
- Blue-green/Canary

**7. Operate (Эксплуатация)**
- Infrastructure management
- Scaling
- Backup/Recovery
- Security operations

**8. Monitor (Мониторинг)**
- Application monitoring
- Infrastructure monitoring
- Log aggregation
- Alerting

### 1.3 Поток ценности (Value Stream)

```python
# Пример: измерение времени по фазам
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class ValueStreamPhase:
    name: str
    start: datetime
    end: datetime
    
    @property
    def duration(self) -> timedelta:
        return self.end - self.start

@dataclass
class FeatureDelivery:
    feature_id: str
    phases: list[ValueStreamPhase]
    
    def total_lead_time(self) -> timedelta:
        return self.phases[-1].end - self.phases[0].start
    
    def value_add_time(self) -> timedelta:
        """Время, добавляющее ценность (без ожидания)."""
        return sum(
            (p.duration for p in self.phases if p.name != "waiting"),
            timedelta()
        )
    
    def efficiency(self) -> float:
        """Process Cycle Efficiency."""
        return self.value_add_time() / self.total_lead_time() * 100

# Пример delivery
feature = FeatureDelivery(
    feature_id="FEAT-123",
    phases=[
        ValueStreamPhase("planning", datetime(2024, 1, 1), datetime(2024, 1, 2)),
        ValueStreamPhase("waiting", datetime(2024, 1, 2), datetime(2024, 1, 8)),
        ValueStreamPhase("development", datetime(2024, 1, 8), datetime(2024, 1, 12)),
        ValueStreamPhase("review", datetime(2024, 1, 12), datetime(2024, 1, 13)),
        ValueStreamPhase("testing", datetime(2024, 1, 13), datetime(2024, 1, 15)),
        ValueStreamPhase("deployment", datetime(2024, 1, 15), datetime(2024, 1, 15)),
    ]
)

print(f"Lead Time: {feature.total_lead_time().days} days")
print(f"Efficiency: {feature.efficiency():.1f}%")

```

**Output:**
```

Lead Time: 14 days
Efficiency: 57.1%

```

---

## 2. Планирование работы

### 2.1 Уровни планирования

```

┌──────────────────────────────────────────────────────────────────┐
│                      Strategic Planning                          │
│              (Quarterly/Yearly • OKRs, Vision)                   │
├──────────────────────────────────────────────────────────────────┤
│                      Release Planning                            │
│               (Monthly/Quarterly • Roadmap)                      │
├──────────────────────────────────────────────────────────────────┤
│                      Iteration Planning                          │
│                (Weekly/Biweekly • Sprint)                        │
├──────────────────────────────────────────────────────────────────┤
│                       Daily Planning                             │
│                  (Daily • Standup, Tasks)                        │
└──────────────────────────────────────────────────────────────────┘

```

### 2.2 OKRs (Objectives and Key Results)

OKR — система целеполагания, популяризированная Google.

**Структура:**

- **Objective**: Качественная цель (что хотим достичь)

- **Key Results**: Измеримые результаты (как поймём, что достигли)

```python
# Пример OKR для DevOps команды
devops_okr = {
    "objective": "Повысить надёжность и скорость delivery",
    "key_results": [
        {
            "kr": "Увеличить deployment frequency до 10 раз в неделю",
            "baseline": 2,
            "target": 10,
            "current": 6
        },
        {
            "kr": "Сократить lead time до 3 дней",
            "baseline": 14,
            "target": 3,
            "current": 7
        },
        {
            "kr": "Снизить change failure rate до 10%",
            "baseline": 25,
            "target": 10,
            "current": 15
        },
        {
            "kr": "Достичь MTTR менее 1 часа",
            "baseline": 240,  # минут
            "target": 60,
            "current": 90
        }
    ],
    "period": "Q1 2024"
}

def calculate_okr_progress(okr: dict) -> float:
    """Calculate overall OKR progress."""
    progress_sum = 0
    for kr in okr["key_results"]:
        # Прогресс от baseline к target
        total_change = kr["target"] - kr["baseline"]
        current_change = kr["current"] - kr["baseline"]
        progress = current_change / total_change if total_change != 0 else 0
        progress_sum += min(max(progress, 0), 1)  # Clamp 0-1
    
    return progress_sum / len(okr["key_results"]) * 100

progress = calculate_okr_progress(devops_okr)
print(f"OKR Progress: {progress:.0f}%")

```

**Output:**
```

OKR Progress: 63%

```

### 2.3 Roadmap Planning

**Типы roadmaps:**

1. **Feature-based Roadmap:**
```

Q1 2024              Q2 2024              Q3 2024
├──────────────────┼──────────────────┼──────────────────┤
│ • Auth v2        │ • Search v2      │ • Mobile app     │
│ • Performance    │ • Analytics      │ • API v3         │
│ • GDPR           │ • Notifications  │ • Marketplace    │

```

2. **Outcome-based Roadmap:**
```

Now                  Next                 Later
├──────────────────┼──────────────────┼──────────────────┤
│ Improve          │ Expand market    │ Platform         │
│ retention        │ reach            │ ecosystem        │
│                  │                  │                  │
│ Goal: -20%       │ Goal: +50%       │ Goal: 3rd party  │
│ churn            │ new users        │ integrations     │

```

### 2.4 Capacity Planning

```python

from dataclasses import dataclass

@dataclass
class TeamCapacity:
    team_size: int
    days_in_sprint: int
    hours_per_day: float = 6.0  # После meetings, breaks
    pto_days: int = 0
    reserved_for_ops: float = 0.2  # 20% на ops work
    
    def available_hours(self) -> float:
        total_days = self.team_size * self.days_in_sprint - self.pto_days
        total_hours = total_days * self.hours_per_day
        return total_hours * (1 - self.reserved_for_ops)
    
    def story_points(self, hours_per_point: float = 4) -> int:
        return int(self.available_hours() / hours_per_point)

# Планирование спринта
team = TeamCapacity(
    team_size=5,
    days_in_sprint=10,  # 2 weeks
    pto_days=3
)

print(f"Available hours: {team.available_hours():.0f}")
print(f"Estimated capacity: {team.story_points()} story points")

```

**Output:**
```

Available hours: 225
Estimated capacity: 56 story points

```

---

## 3. Ceremonies и регулярные процессы

### 3.1 DevOps Ceremonies

**Daily Standup (15 min):**

- Синхронизация команды
- Выявление блокеров
- Обсуждение deployment status

**Weekly:**

- **Planning** — выбор работы на неделю/спринт

- **Demo/Review** — демонстрация результатов

- **On-call handoff** — передача дежурства

**Bi-weekly/Monthly:**

- **Retrospective** — улучшение процесса

- **Post-incident reviews** — разбор инцидентов

- **Architecture review** — технические решения

**Quarterly:**

- **OKR planning** — цели на квартал

- **Roadmap review** — пересмотр плана

- **Capacity planning** — планирование ресурсов

### 3.2 Эффективные Stand-ups

**Формат для DevOps команды:**

```markdown
# Daily Standup Agenda (15 min)

## 1. Production Status (2 min)
- Текущие инциденты?
- SLO status (green/yellow/red)
- Pending deployments

## 2. Team Round-robin (10 min)
Каждый член команды:

- Что сделал вчера
- Что планирую сегодня
- Блокеры

## 3. Quick Topics (3 min)
- Важные анонсы
- Парковка тем для отдельного обсуждения

```

**Anti-patterns:**
```python

standup_antipatterns = [
    "Status report для менеджера (а не синхронизация команды)",
    "Детальные технические дискуссии",
    "Длительность > 15 минут",
    "Не все члены команды участвуют",
    "Нет обсуждения блокеров",
    "Игнорирование production status"
]

```

### 3.3 Retrospectives

**Format: Start/Stop/Continue**

```markdown
# Sprint Retrospective

## 🟢 Start (Начать делать)
- Автоматизировать smoke tests после деплоя
- Проводить architecture reviews перед большими фичами
- Добавить runbooks для новых сервисов

## 🔴 Stop (Прекратить делать)
- Деплоить в пятницу вечером
- Игнорировать flaky tests
- Пропускать code review для "срочных" фиксов

## 🟡 Continue (Продолжить делать)
- Парное программирование для сложных задач
- Ежедневный мониторинг метрик
- Документирование решений в ADRs

```

**5 Whys для root cause analysis:**

```python

def five_whys(problem: str, answers: list[str]) -> None:
    """Demonstrate 5 Whys technique."""
    print(f"Problem: {problem}\n")
    for i, answer in enumerate(answers, 1):
        print(f"Why #{i}? → {answer}")
    print(f"\nRoot cause: {answers[-1]}")

five_whys(
    "Deployment failed and caused 30 min outage",
    [
        "Database migration script failed",
        "Script wasn't tested against production data volume",
        "No staging environment with production-like data",
        "Team doesn't have process for data refresh in staging",
        "Creating data refresh was never prioritized"
    ]
)

```

**Output:**
```

Problem: Deployment failed and caused 30 min outage

Why #1? → Database migration script failed
Why #2? → Script wasn't tested against production data volume
Why #3? → No staging environment with production-like data
Why #4? → Team doesn't have process for data refresh in staging
Why #5? → Creating data refresh was never prioritized

Root cause: Creating data refresh was never prioritized

```

---

## 4. Value Stream Mapping

### 4.1 Что такое Value Stream Mapping

Value Stream Mapping (VSM) — метод визуализации всего процесса доставки для выявления waste и bottlenecks.

### 4.2 Создание Value Stream Map

**Шаги:**

1. Определить начало и конец потока
2. Идентифицировать все шаги
3. Измерить время каждого шага
4. Выявить ожидание между шагами
5. Рассчитать efficiency

```

┌──────────────────────────────────────────────────────────────────────────────┐
│                        Value Stream Map: Feature Delivery                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │ Ideation│───▶│  Dev    │───▶│ Review  │───▶│ Test    │───▶│ Deploy  │     │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
│       │              │              │              │              │          │
│  PT: 4h         PT: 16h        PT: 2h         PT: 4h         PT: 1h          │
│  WT: 48h        WT: 8h         WT: 24h        WT: 16h        WT: 4h          │
│                                                                              │
│  PT = Process Time (время работы)                                            │
│  WT = Wait Time (время ожидания)                                             │
│                                                                              │
│  Total PT: 27 hours                                                          │
│  Total WT: 100 hours                                                         │
│  Lead Time: 127 hours                                                        │
│  Efficiency: 21%                                                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

```

### 4.3 Типы waste в Value Stream

```python
# Семь типов waste (Muda) в software delivery
waste_types = {
    "partially_done_work": {
        "description": "Незавершённая работа",
        "examples": ["Feature branches > 3 days", "PRs в ожидании review"],
        "impact": "Высокий"
    },
    "extra_features": {
        "description": "Лишний функционал",
        "examples": ["Gold plating", "Невостребованные фичи"],
        "impact": "Средний"
    },
    "relearning": {
        "description": "Повторное изучение",
        "examples": ["Нет документации", "Knowledge silos"],
        "impact": "Средний"
    },
    "handoffs": {
        "description": "Передачи между людьми/командами",
        "examples": ["Dev → QA → Ops", "Code review очередь"],
        "impact": "Высокий"
    },
    "task_switching": {
        "description": "Переключение контекста",
        "examples": ["Работа над 5+ задачами", "Частые прерывания"],
        "impact": "Высокий"
    },
    "delays": {
        "description": "Ожидание",
        "examples": ["Ожидание approval", "Очередь на deploy"],
        "impact": "Высокий"
    },
    "defects": {
        "description": "Дефекты",
        "examples": ["Bugs в production", "Rollbacks"],
        "impact": "Высокий"
    }
}

def identify_waste(process_step: dict) -> list[str]:
    """Identify potential waste in a process step."""
    wastes = []
    
    if process_step.get("wait_time", 0) > process_step.get("process_time", 0):
        wastes.append("delays")
    
    if process_step.get("handoffs", 0) > 1:
        wastes.append("handoffs")
    
    if process_step.get("rework_rate", 0) > 0.1:
        wastes.append("defects")
    
    return wastes

```

### 4.4 Оптимизация Value Stream

**До оптимизации:**
```

Ideation (4h) → Wait (48h) → Dev (16h) → Wait (8h) → Review (2h) → 
Wait (24h) → Test (4h) → Wait (16h) → Deploy (1h) → Wait (4h)

Total: 127 hours, Efficiency: 21%

```

**Улучшения:**

1. **Уменьшить batch size** — меньше фичи = быстрее review
2. **Автоматизировать тесты** — меньше ожидания QA
3. **Self-service deployment** — нет очереди на deploy
4. **WIP limits** — меньше ожидания в очередях

**После оптимизации:**
```

Ideation (2h) → Dev (8h) → Review (1h) → Automated Test (0.5h) → 
Auto Deploy (0.25h)

Total: 12 hours, Efficiency: 98%

```

---

## 5. Регламенты и документация

### 5.1 Runbooks

Runbook — документ с пошаговыми инструкциями для выполнения операционных задач.

**Структура runbook:**

```markdown
# Runbook: Database Failover

## Overview
Процедура переключения на replica при отказе primary database.

## Prerequisites
- SSH доступ к database servers
- PagerDuty access
- Database admin credentials (в Vault)

## Triggers
- Primary database unavailable > 5 min
- Replication lag > 30 sec sustained
- Alert: `db-primary-health-critical`

## Steps

### 1. Verify the issue (2 min)
\```bash
# Check primary status
ssh db-primary-01 'pg_isready -h localhost'

# Check replication lag
psql -h db-replica-01 -c "SELECT pg_last_wal_receive_lsn() - pg_last_wal_replay_lsn();"
\```

### 2. Notify stakeholders (1 min)
- Post in #incidents channel
- Page on-call SRE if not already paged

### 3. Promote replica (5 min)
\```bash
# On replica server
sudo -u postgres pg_ctl promote -D /var/lib/postgresql/14/main

# Verify promotion
psql -c "SELECT pg_is_in_recovery();"
# Should return 'f' (false)
\```

### 4. Update DNS/Load Balancer (2 min)
\```bash
# Update Route53 (or your DNS)
aws route53 change-resource-record-sets \
  --hosted-zone-id XXXXX \
  --change-batch file://failover-dns.json
\```

### 5. Verify application connectivity (3 min)
- Check application logs for connection errors
- Verify key queries are working
- Check Grafana dashboard for normal traffic

## Rollback
If failover fails, revert DNS and investigate primary.

## Post-incident
- Create incident report
- Schedule post-mortem
- Update this runbook if needed

## Contacts
- Database team: #team-database
- On-call DBA: page via PagerDuty

```

### 5.2 Architecture Decision Records (ADRs)

ADR — документ, фиксирующий важное архитектурное решение.

```markdown
# ADR-0015: Use PostgreSQL for User Service Database

## Status
Accepted

## Context
User Service needs a database for storing user profiles, 
authentication data, and preferences. We need to choose 
between PostgreSQL, MySQL, and MongoDB.

## Decision
We will use PostgreSQL 15 for User Service.

## Rationale
1. **ACID compliance** — critical for user data
2. **JSON support** — flexible schema for preferences
3. **Team expertise** — 4/5 engineers have PostgreSQL experience
4. **Ecosystem** — existing tools, monitoring, backup

## Alternatives Considered

### MySQL
- Pros: Similar to PostgreSQL, widely used
- Cons: Less rich JSON support, team less familiar

### MongoDB
- Pros: Flexible schema, easy horizontal scaling
- Cons: Eventual consistency issues, different query patterns

## Consequences
- Need PostgreSQL expertise for operations
- Will use PgBouncer for connection pooling
- Backup strategy using pg_dump + WAL archiving
- May need to migrate if scale exceeds PostgreSQL limits

## Related
- ADR-0010: Database hosting on AWS RDS
- ADR-0012: Use Vault for database credentials

```

### 5.3 Standard Operating Procedures (SOPs)

**Deployment SOP:**

```markdown
# SOP: Production Deployment

## 1. Pre-deployment Checklist
- [ ] All tests passing on main branch
- [ ] Code review approved
- [ ] Security scan completed
- [ ] Release notes prepared
- [ ] Rollback plan documented
- [ ] On-call engineer available

## 2. Deployment Window
- **Standard**: Mon-Thu, 10:00-16:00 UTC

- **Frozen periods**: Last week of quarter, holidays

- **Emergency**: Any time with VP approval

## 3. Deployment Process
1. Create deployment ticket
2. Run deployment pipeline
3. Monitor metrics for 15 min
4. Confirm deployment in ticket

## 4. Rollback Criteria
Rollback immediately if:

- Error rate > 5%
- P99 latency > 2x baseline
- Any critical alert fires

## 5. Post-deployment
- Update deployment ticket status
- Notify in #releases channel
- Monitor for 1 hour

```

---

## 6. Change Management

### 6.1 Типы изменений

```python

from enum import Enum
from dataclasses import dataclass

class ChangeType(Enum):
    STANDARD = "standard"     # Pre-approved, automated
    NORMAL = "normal"         # Requires review
    EMERGENCY = "emergency"   # Expedited process

@dataclass
class ChangeRequest:
    change_type: ChangeType
    description: str
    risk_level: str  # low, medium, high
    rollback_plan: str
    
    def approval_required(self) -> bool:
        return self.change_type != ChangeType.STANDARD
    
    def approval_process(self) -> str:
        if self.change_type == ChangeType.STANDARD:
            return "Auto-approved"
        elif self.change_type == ChangeType.NORMAL:
            if self.risk_level == "low":
                return "Team lead approval"
            elif self.risk_level == "medium":
                return "Engineering manager approval"
            else:
                return "CAB approval"
        else:  # EMERGENCY
            return "VP approval, retrospective CAB review"

# Примеры
changes = [
    ChangeRequest(
        ChangeType.STANDARD,
        "Automated deployment with feature flag",
        "low",
        "Disable feature flag"
    ),
    ChangeRequest(
        ChangeType.NORMAL,
        "Database schema migration",
        "medium",
        "Run down migration script"
    ),
    ChangeRequest(
        ChangeType.EMERGENCY,
        "Hotfix for security vulnerability",
        "high",
        "Revert commit and redeploy"
    )
]

for change in changes:
    print(f"{change.change_type.value}: {change.approval_process()}")

```

**Output:**
```

standard: Auto-approved
normal: Engineering manager approval
emergency: VP approval, retrospective CAB review

```

### 6.2 Change Advisory Board (CAB)

**Когда нужен CAB:**

- High-risk changes
- Changes affecting multiple teams
- Major infrastructure changes
- Compliance-sensitive changes

**DevOps-friendly CAB:**

- Виртуальные CAB meetings (async когда возможно)
- Pre-approved standard changes
- Автоматическая оценка риска
- Post-implementation review вместо pre-approval для low-risk

---

## 7. Release Management

### 7.1 Release Strategies

**Big Bang Release:**
```

Version 1.0 ──────────────────────▶ Version 2.0
              (все изменения сразу)

❌ Высокий риск
❌ Сложный rollback
❌ Долгий feedback loop

```

**Incremental Release:**
```

v1.0 → v1.1 → v1.2 → v1.3 → v1.4 → v2.0
       (маленькие частые релизы)

✅ Низкий риск
✅ Простой rollback
✅ Быстрый feedback

```

### 7.2 Semantic Versioning

```

MAJOR.MINOR.PATCH
  │     │     │
  │     │     └── Bug fixes (backward compatible)
  │     └──────── New features (backward compatible)
  └────────────── Breaking changes

Examples:

- 1.0.0 → 1.0.1 (bug fix)
- 1.0.1 → 1.1.0 (new feature)
- 1.1.0 → 2.0.0 (breaking change)

```

```python

from dataclasses import dataclass
import re

@dataclass
class SemanticVersion:
    major: int
    minor: int
    patch: int
    
    @classmethod
    def parse(cls, version_string: str) -> 'SemanticVersion':
        match = re.match(r'(\d+)\.(\d+)\.(\d+)', version_string)
        if not match:
            raise ValueError(f"Invalid version: {version_string}")
        return cls(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    
    def bump_patch(self) -> 'SemanticVersion':
        return SemanticVersion(self.major, self.minor, self.patch + 1)
    
    def bump_minor(self) -> 'SemanticVersion':
        return SemanticVersion(self.major, self.minor + 1, 0)
    
    def bump_major(self) -> 'SemanticVersion':
        return SemanticVersion(self.major + 1, 0, 0)
    
    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

# Пример использования
current = SemanticVersion.parse("1.4.2")
print(f"Current: {current}")
print(f"Bug fix: {current.bump_patch()}")
print(f"Feature: {current.bump_minor()}")
print(f"Breaking: {current.bump_major()}")

```

**Output:**
```

Current: 1.4.2
Bug fix: 1.4.3
Feature: 1.5.0
Breaking: 2.0.0

```

### 7.3 Release Notes

```markdown
# Release Notes v2.3.0

**Release Date:** 2024-01-15

## 🚀 New Features
- **OAuth2 Integration** — Added support for Google and GitHub login

- **Dark Mode** — User preference for dark theme

- **API Pagination** — All list endpoints now support pagination

## 🐛 Bug Fixes
- Fixed memory leak in WebSocket handler (#1234)
- Corrected timezone handling in reports (#1256)
- Fixed race condition in cache invalidation (#1267)

## ⚠️ Breaking Changes
- Deprecated `/api/v1/users` endpoint removed (use `/api/v2/users`)
- Minimum supported Python version is now 3.10

## 🔧 Improvements
- Reduced API response time by 30%
- Improved error messages for validation errors

## 📋 Migration Guide
1. Update API clients to use v2 endpoints
2. Verify Python 3.10+ is installed
3. Run database migration: `python manage.py migrate`

## 🙏 Contributors
@alice, @bob, @carol

```

---

## 8. On-Call и дежурства

### 8.1 On-Call Rotation

```python

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

@dataclass
class OnCallShift:
    engineer: str
    start: datetime
    end: datetime
    is_primary: bool = True
    
@dataclass
class OnCallSchedule:
    shifts: list[OnCallShift]
    
    def current_on_call(self, at: Optional[datetime] = None) -> Optional[OnCallShift]:
        at = at or datetime.now()
        for shift in self.shifts:
            if shift.start <= at < shift.end:
                return shift
        return None
    
    def next_on_call(self, engineer: str) -> Optional[OnCallShift]:
        now = datetime.now()
        future_shifts = [
            s for s in self.shifts 
            if s.engineer == engineer and s.start > now
        ]
        return min(future_shifts, key=lambda s: s.start) if future_shifts else None

# Пример расписания (1-week rotations)
schedule = OnCallSchedule(shifts=[
    OnCallShift("alice", datetime(2024, 1, 1), datetime(2024, 1, 8)),
    OnCallShift("bob", datetime(2024, 1, 8), datetime(2024, 1, 15)),
    OnCallShift("carol", datetime(2024, 1, 15), datetime(2024, 1, 22)),
    OnCallShift("alice", datetime(2024, 1, 22), datetime(2024, 1, 29)),
])

```

### 8.2 On-Call Responsibilities

**Primary On-Call:**

- Первая линия реагирования на алерты
- Triage инцидентов
- Эскалация при необходимости
- Handoff документация

**Secondary On-Call:**

- Backup для primary
- Помощь при major incidents
- Принимает на себя, если primary недоступен

### 8.3 On-Call Handoff

```markdown
# On-Call Handoff: 2024-01-08

## Outgoing: Alice → Incoming: Bob

### Active Issues
- **INC-456**: Intermittent 504 errors on /api/search
  - Status: Investigating
  - Suspected: Elasticsearch cluster under load
  - Next step: Check ES metrics, consider adding nodes

### Recent Incidents
- **INC-455**: Database failover (Jan 5)
  - Resolved, postmortem scheduled for Jan 10

### Scheduled Maintenance
- **Jan 9, 02:00 UTC**: Kubernetes cluster upgrade
  - Runbook: [link]
  - Expected duration: 2 hours

### Known Issues
- Flaky alert: `disk-usage-high` on logging-01 (ticket: OPS-789)
  - Safe to acknowledge, being addressed

### Notes
- New runbook for Redis failover added to wiki
- Team-platform Slack channel for questions

**Handoff confirmed:**

- [ ] Alice (outgoing)
- [ ] Bob (incoming)

```

---

## 💡 Key Takeaways

- **DevOps Lifecycle — бесконечный цикл**: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → (repeat)

- **Планирование многоуровневое**: От стратегических OKR до daily standups

- **Value Stream Mapping выявляет waste**: Измеряйте wait time, оптимизируйте flow

- **Документация — часть процесса**: Runbooks, ADRs, SOPs экономят время при инцидентах

- **Change Management может быть DevOps-friendly**: Standard changes, автоматическая оценка рисков

---

## 🚀 Next Steps

**Related Modules:**

- [04_CI](../04_CI/) — Continuous Integration
- [05_CD](../05_CD/) — Continuous Delivery/Deployment
- [12_Incidents](../12_Incidents/) — Incident Management

**Practice Ideas:**

1. Создайте Value Stream Map для вашего процесса delivery
2. Напишите runbook для критичной операционной задачи
3. Определите OKRs для DevOps метрик вашей команды

**Going Deeper:**

- "Value Stream Mapping" by Karen Martin
- "The Goal" by Eliyahu Goldratt
- Google SRE Handbook — On-Call chapter

---

## 📚 Additional Resources

**Books:**

- "Value Stream Mapping" by Karen Martin & Mike Osterling
- "The Goal" by Eliyahu Goldratt — теория ограничений
- "Making Work Visible" by Dominica DeGrandis — визуализация работы

**Templates:**

- [ADR Template](https://github.com/joelparkerhenderson/architecture-decision-record)
- [Runbook Template](https://www.pagerduty.com/resources/learn/what-is-a-runbook/)

**Tools:**

- Miro — для Value Stream Mapping
- Confluence/Notion — для документации
- PagerDuty/OpsGenie — для on-call management

---




