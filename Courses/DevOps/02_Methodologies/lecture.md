# Методологии разработки
## Agile, Scrum, Kanban и ITIL в контексте DevOps

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [01_Intro](../01_Intro/) — Введение в DevOps
- Иметь опыт работы в команде разработки
- Понимать базовый цикл разработки ПО

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы Agile и их связь с DevOps
- Применять Scrum framework для организации работы команды
- Использовать Kanban для визуализации и оптимизации потока
- Понимать роль ITIL в enterprise окружении
- Выбирать подходящую методологию для конкретного контекста

---

## 1. Agile и DevOps

### 1.1 От Waterfall к Agile

**Waterfall (каскадная модель):**
```

┌─────────────┐
│ Requirements│
└──────┬──────┘
       ▼
┌─────────────┐
│   Design    │
└──────┬──────┘
       ▼
┌─────────────┐
│Implementatio│
└──────┬──────┘
       ▼
┌─────────────┐
│   Testing   │
└──────┬──────┘
       ▼
┌─────────────┐
│ Deployment  │
└──────┬──────┘
       ▼
┌─────────────┐
│ Maintenance │
└─────────────┘

Проблемы:

- Долгий цикл (6-18 месяцев)
- Поздняя обратная связь
- Сложно реагировать на изменения
- "Big bang" релизы

```

**Agile:**
```

    Sprint 1         Sprint 2         Sprint 3
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Plan→Build→ │  │ Plan→Build→ │  │ Plan→Build→ │
│ Test→Deploy │  │ Test→Deploy │  │ Test→Deploy │
└─────────────┘  └─────────────┘  └─────────────┘
       ▼                ▼                ▼
   Working          Working          Working
   Software         Software         Software
   
Преимущества:

- Короткие итерации (1-4 недели)
- Частая обратная связь
- Гибкость к изменениям
- Инкрементальная доставка

```

### 1.2 Agile Manifesto (2001)

Четыре ценности:

| Ценим больше | Чем |
|--------------|-----|
| **Люди и взаимодействие** | Процессы и инструменты |
| **Работающий продукт** | Исчерпывающая документация |
| **Сотрудничество с заказчиком** | Согласование условий контракта |
| **Готовность к изменениям** | Следование первоначальному плану |

**12 принципов Agile:**

1. Удовлетворение клиента через раннюю и непрерывную поставку
2. Приветствие изменений требований даже на поздних стадиях
3. Частая поставка работающего ПО (недели, не месяцы)
4. Ежедневное сотрудничество бизнеса и разработчиков
5. Проекты строятся вокруг мотивированных людей
6. Face-to-face коммуникация — самый эффективный способ
7. Работающий продукт — главный показатель прогресса
8. Устойчивый темп разработки
9. Постоянное внимание к техническому совершенству
10. Простота — искусство максимизации несделанной работы
11. Лучшие архитектуры и требования рождаются в самоорганизующихся командах
12. Регулярные ретроспективы для повышения эффективности

### 1.3 Связь Agile и DevOps

```

┌───────────────────────────────────────────────────────────────┐
│                          DevOps                               │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                         Agile                            │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │ Development (Plan → Code → Build → Test)            │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ Operations (Release → Deploy → Operate → Monitor)        │ │
│  └──────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────┘

Agile оптимизировал Development.
DevOps расширил эту оптимизацию на весь цикл доставки.

```

**Agile останавливался на границе с Operations:**

- Sprint закончился → код "готов"
- Но... когда он попадёт к пользователям?
- Release management — отдельный (и медленный) процесс

**DevOps закрывает этот gap:**

- Continuous Integration
- Continuous Delivery/Deployment
- Общая ответственность за весь lifecycle

---

## 2. Scrum Framework

### 2.1 Обзор Scrum

Scrum — это фреймворк для разработки, доставки и поддержки сложных продуктов. Создан Кеном Швабером и Джеффом Сазерлендом в 1990-х.

**Ключевые характеристики:**

- Итеративный и инкрементальный
- Эмпирический подход (inspect & adapt)
- Фиксированные по времени спринты (1-4 недели)
- Самоорганизующиеся команды

### 2.2 Scrum Roles

**Product Owner (PO):**

- Отвечает за Product Backlog
- Приоритизирует работу
- Представляет интересы stakeholders
- Принимает/отклоняет результаты

**Scrum Master (SM):**

- Фасилитатор процесса
- Устраняет impediments
- Защищает команду от внешнего давления
- Коучит команду по Scrum

**Development Team:**

- Кросс-функциональная команда (3-9 человек)
- Самоорганизующаяся
- Отвечает за доставку инкремента

```

┌────────────────────────────────────────────────────────┐
│                    Scrum Team                          │
│                                                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │   Product   │  │   Scrum     │  │  Development    │ │
│  │   Owner     │  │   Master    │  │     Team        │ │
│  │             │  │             │  │                 │ │
│  │ • Backlog   │  │ • Process   │  │ • Cross-func    │ │
│  │ • Priorities│  │ • Coaching  │  │ • Self-org      │ │
│  │ • Vision    │  │ • Impediments│ │ • Delivery      │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
└────────────────────────────────────────────────────────┘

```

### 2.3 Scrum Events

**Sprint:**

- Фиксированный период (обычно 2 недели)
- Содержит все остальные события
- Результат — потенциально готовый к релизу инкремент

**Sprint Planning:**

- В начале спринта
- Команда выбирает работу из Backlog
- Определяет Sprint Goal
- Создаёт Sprint Backlog

```python
# Пример: структура Sprint Planning
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SprintPlanningOutput:
    sprint_goal: str
    sprint_backlog: list[str]
    team_capacity: int  # story points
    committed_points: int
    
# Sprint Planning результат
sprint_3 = SprintPlanningOutput(
    sprint_goal="Реализовать авторизацию через OAuth",
    sprint_backlog=[
        "PROJ-101: Интеграция с Google OAuth",
        "PROJ-102: UI страницы логина",
        "PROJ-103: Token refresh механизм",
        "PROJ-104: Logout flow",
    ],
    team_capacity=40,
    committed_points=35
)

```

**Daily Standup (Daily Scrum):**

- 15 минут, каждый день
- Синхронизация команды
- Три вопроса:
  - Что сделал вчера?
  - Что буду делать сегодня?
  - Есть ли блокеры?

```python
# Анти-паттерн: Status report для менеджера
# Паттерн: Синхронизация между членами команды

# Плохо:
bad_standup = """
Developer: Вчера работал над PROJ-101. Сегодня продолжу.
           Блокеров нет.
Manager: Хорошо, следующий...
"""

# Хорошо:
good_standup = """
Developer: Вчера закончил интеграцию с Google OAuth API.
           Сегодня начну UI страницы логина.
           Мне нужна помощь с дизайном — Аня, можем 
           синхронизироваться после стендапа?
Аня: Да, у меня есть 30 минут после обеда.
"""

```

**Sprint Review:**

- В конце спринта
- Демонстрация инкремента stakeholders
- Получение feedback
- Обновление Product Backlog

**Sprint Retrospective:**

- После Review, до следующего Planning
- Команда рефлексирует о процессе
- Что было хорошо? Что улучшить?
- Action items для следующего спринта

```

┌────────────────────────────────────────────────────────┐
│                    Sprint Cycle                        │
│                                                        │
│    Planning ─────▶ Development ─────▶ Review           │
│        │               │                 │             │
│        │          Daily Standup          │             │
│        │           (каждый день)         │             │
│        │               │                 │             │
│        └───────────────┼─────────────────┘             │
│                        │                               │
│                        ▼                               │
│                  Retrospective                         │
│                        │                               │
│                        ▼                               │
│                 Next Sprint Planning                   │
└────────────────────────────────────────────────────────┘

```

### 2.4 Scrum Artifacts

**Product Backlog:**

- Упорядоченный список всей работы
- Принадлежит Product Owner
- Постоянно уточняется (grooming/refinement)

**Sprint Backlog:**

- Работа, выбранная на спринт
- Принадлежит Development Team
- Включает план достижения Sprint Goal

**Increment:**

- Сумма всех завершённых Product Backlog Items
- Должен быть "Done" (соответствовать Definition of Done)
- Потенциально готов к релизу

```python
# Пример: Definition of Done
definition_of_done = [
    "Код написан и прошёл code review",
    "Unit tests написаны и проходят",
    "Integration tests проходят",
    "Документация обновлена",
    "Задеплоено на staging",
    "QA проверил на staging",
    "Performance не деградировал",
    "Security review пройден (если применимо)",
]

def is_done(task: dict) -> bool:
    return all(
        task.get(criterion, False) 
        for criterion in definition_of_done
    )

```

### 2.5 Scrum и DevOps

**Интеграция Scrum с DevOps практиками:**

| Scrum Event | DevOps практика |
|-------------|-----------------|
| Sprint Planning | Включать operations tasks (infrastructure, monitoring) |
| Daily Standup | Обсуждать deployment status, incidents |
| Sprint Review | Demo на production или production-like среде |
| Retrospective | Анализировать deployment failures, incidents |

**Definition of Done с DevOps:**

```python

devops_definition_of_done = [
    # Development
    "Код написан и прошёл code review",
    "Unit tests написаны (coverage > 80%)",
    
    # CI/CD
    "CI pipeline green",
    "Automated security scan passed",
    
    # Deployment
    "Feature flag создан (если нужно)",
    "Задеплоено на staging",
    "Smoke tests на staging прошли",
    
    # Observability
    "Метрики и логи добавлены",
    "Alerts настроены",
    "Runbook обновлён",
    
    # Documentation
    "API documentation обновлена",
    "Architecture Decision Record (если нужно)",
]

```

---

## 3. Kanban

### 3.1 Происхождение Kanban

Kanban (看板, "вывеска") — система, разработанная в Toyota для управления производством. Адаптирована для разработки ПО David J. Anderson.

**Ключевая идея:** визуализировать работу и ограничить Work in Progress (WIP).

### 3.2 Принципы Kanban

**4 базовых принципа:**

1. **Начни с того, что есть** — не требуется радикальных изменений
2. **Соглашайся на эволюционные изменения** — постепенные улучшения
3. **Уважай текущие роли и ответственности** — не ломать существующую структуру
4. **Поощряй лидерство на всех уровнях** — любой может предложить улучшение

**6 практик:**

1. **Визуализация** — Kanban board
2. **Ограничение WIP** — лимиты на колонки
3. **Управление потоком** — оптимизация flow
4. **Явные политики** — чёткие правила перехода
5. **Петли обратной связи** — регулярные review
6. **Совместное улучшение** — эксперименты с процессом

### 3.3 Kanban Board

**Базовая структура:**

```

┌─────────────────────────────────────────────────────────────────┐
│                         KANBAN BOARD                            │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┤
│ Backlog  │ Ready    │ In Dev   │ Review   │ Testing  │ Done     │
│          │          │ WIP: 3   │ WIP: 2   │ WIP: 2   │          │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │
│ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │
│ │-201  │ │ │-198  │ │ │-195  │ │ │-192  │ │ │-188  │ │ │-185  │ │
│ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │
│ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │
│ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │ │PROJ  │ │
│ │-202  │ │ │-199  │ │ │-196  │ │ │-193  │ │ │-189  │ │ │-186  │ │
│ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │ └──────┘ │
│ ┌──────┐ │          │ ┌──────┐ │          │          │ ┌──────┐ │
│ │PROJ  │ │          │ │PROJ  │ │          │          │ │PROJ  │ │
│ │-203  │ │          │ │-197  │ │          │          │ │-187  │ │
│ └──────┘ │          │ └──────┘ │          │          │ └──────┘ │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

```

### 3.4 Work in Progress (WIP) Limits

**Почему ограничивать WIP:**

```python
# Закон Литтла (Little's Law):
# Lead Time = WIP / Throughput

# Пример:
throughput = 5  # задач в неделю
wip_high = 20   # много задач в работе
wip_low = 5     # мало задач в работе

lead_time_high = wip_high / throughput  # 4 недели
lead_time_low = wip_low / throughput    # 1 неделя

print(f"High WIP Lead Time: {lead_time_high} weeks")
print(f"Low WIP Lead Time: {lead_time_low} weeks")

```

**Output:**
```

High WIP Lead Time: 4.0 weeks
Low WIP Lead Time: 1.0 weeks

```

**Эффект WIP лимитов:**

- Задачи завершаются быстрее
- Меньше переключений контекста
- Проблемы выявляются раньше
- Более предсказуемый flow

### 3.5 Kanban Metrics

**Lead Time:**

- Время от появления задачи в системе до её завершения
- Включает время ожидания

**Cycle Time:**

- Время от начала работы над задачей до завершения
- Не включает время в очереди

```python

from datetime import datetime, timedelta

def calculate_metrics(task: dict) -> dict:
    """Calculate Kanban metrics for a task."""
    created = task["created_at"]
    started = task["started_at"]
    completed = task["completed_at"]
    
    lead_time = completed - created
    cycle_time = completed - started
    wait_time = started - created
    
    return {
        "lead_time_days": lead_time.days,
        "cycle_time_days": cycle_time.days,
        "wait_time_days": wait_time.days,
        "efficiency": cycle_time / lead_time * 100
    }

# Пример задачи
task = {
    "created_at": datetime(2024, 1, 1),
    "started_at": datetime(2024, 1, 8),
    "completed_at": datetime(2024, 1, 12)
}

metrics = calculate_metrics(task)
print(f"Lead Time: {metrics['lead_time_days']} days")
print(f"Cycle Time: {metrics['cycle_time_days']} days")
print(f"Wait Time: {metrics['wait_time_days']} days")
print(f"Efficiency: {metrics['efficiency']:.1f}%")

```

**Output:**
```

Lead Time: 11 days
Cycle Time: 4 days
Wait Time: 7 days
Efficiency: 36.4%

```

**Cumulative Flow Diagram (CFD):**

```

Items │
  100 ├─────────────────────────────────────────┐ Done
      │                              ┌──────────┤
   80 ├───────────────────┬──────────┤ Testing  │
      │              ┌────┤          │          │
   60 ├─────────┬────┤    │ Review   │          │
      │    ┌────┤    │    │          │          │
   40 ├────┤    │    │    │          │          │
      │    │ Dev│    │    │          │          │
   20 ├────┤    │    │    │          │          │
      │    │    │    │    │          │          │
    0 └────┴────┴────┴────┴──────────┴──────────┘
         Week 1  Week 2  Week 3  Week 4  Week 5

Стабильная ширина полос = стабильный WIP
Сужение = bottleneck
Расширение = накопление работы

```

### 3.6 Kanban и DevOps

**DevOps Kanban Board:**

```

┌────────────────────────────────────────────────────────────────────┐
│                     DevOps Kanban Board                            │
├────────┬────────┬────────┬────────┬────────┬────────┬────────┬─────┤
│Backlog │ Dev    │ Code   │ Build/ │ Deploy │ Monitor│ Done   │     │
│        │ WIP:4  │ Review │ Test   │ Staging│        │        │     │
│        │        │ WIP:3  │ WIP:2  │ WIP:2  │        │        │     │
├────────┼────────┼────────┼────────┼────────┼────────┼────────┼─────┤
│ ┌────┐ │ ┌────┐ │ ┌────┐ │ ┌────┐ │ ┌────┐ │        │ ┌────┐ │     │
│ │AUTH│ │ │API │ │ │FIX │ │ │CI  │ │ │FEAT│ │        │ │OLD │ │     │
│ │-101│ │ │-98 │ │ │-95 │ │ │-92 │ │ │-88 │ │        │ │-85 │ │     │
│ └────┘ │ └────┘ │ └────┘ │ └────┘ │ └────┘ │        │ └────┘ │     │
│        │ ┌────┐ │ ┌────┐ │ ┌────┐ │ ┌────┐ │        │        │     │
│        │ │DB  │ │ │PERF│ │ │SEC │ │ │FIX │ │        │        │     │
│        │ │-99 │ │ │-96 │ │ │-93 │ │ │-89 │ │        │        │     │
│        │ └────┘ │ └────┘ │ └────┘ │ └────┘ │        │        │     │
└────────┴────────┴────────┴────────┴────────┴────────┴────────┴─────┘
         │                          │
         ▼                          ▼
    Pull from left            Automated
    when capacity            transitions

```

---

## 4. Scrum vs Kanban

### 4.1 Сравнение

| Аспект | Scrum | Kanban |
|--------|-------|--------|
| Итерации | Фиксированные спринты | Непрерывный поток |
| Роли | PO, SM, Dev Team | Нет обязательных ролей |
| Изменения | Между спринтами | В любое время |
| Метрики | Velocity | Lead time, Cycle time |
| Commitment | Sprint Backlog | WIP limits |
| Церемонии | Обязательные | По необходимости |

### 4.2 Когда использовать

**Scrum подходит когда:**

- Команда новая или незрелая
- Нужна структура и ритм
- Работа хорошо разбивается на итерации
- Есть чёткий Product Owner

**Kanban подходит когда:**

- Непредсказуемый поток работы (поддержка, ops)
- Нужна гибкость в приоритетах
- Команда зрелая и самоорганизованная
- Работа плохо укладывается в спринты

**ScrumBan (гибрид):**

- Спринты Scrum + WIP лимиты Kanban
- Планирование по необходимости (не по расписанию)
- Визуализация на Kanban board

```python
# Выбор методологии
def choose_methodology(context: dict) -> str:
    if context["team_maturity"] == "low":
        return "Scrum"  # Нужна структура
    
    if context["work_type"] == "support_ops":
        return "Kanban"  # Непредсказуемый поток
    
    if context["need_flexibility"]:
        return "Kanban"
    
    if context["want_experiments"]:
        return "ScrumBan"  # Гибрид
    
    return "Scrum"  # По умолчанию

```

---

## 5. ITIL (IT Infrastructure Library)

### 5.1 Что такое ITIL

ITIL — набор лучших практик для управления IT-сервисами (ITSM). Разработан в UK в 1980-х, сейчас в версии ITIL 4.

**Цель ITIL:**

- Стандартизация IT-процессов
- Согласование IT с бизнес-целями
- Улучшение качества сервисов
- Управление рисками

### 5.2 ITIL 4 и DevOps

ITIL 4 (2019) значительно изменился, чтобы соответствовать современным практикам:

**ITIL 4 Guiding Principles:**

1. **Focus on value** — всё ради ценности для клиента
2. **Start where you are** — используй существующее
3. **Progress iteratively with feedback** — звучит знакомо?
4. **Collaborate and promote visibility** — прозрачность
5. **Think and work holistically** — системное мышление
6. **Keep it simple and practical** — простота
7. **Optimize and automate** — автоматизация

> **💡 Заметьте:** Принципы ITIL 4 очень похожи на DevOps!

### 5.3 Ключевые практики ITIL

**Service Desk:**

- Единая точка контакта для пользователей
- Первая линия поддержки
- Маршрутизация запросов

**Incident Management:**

- Восстановление сервиса как можно быстрее
- Минимизация влияния на бизнес
- Классификация по severity

```python
# ITIL Incident Priority Matrix
severity_matrix = {
    ("critical", "high"): "P1",  # Resolve in 1 hour
    ("critical", "medium"): "P1",
    ("critical", "low"): "P2",
    ("major", "high"): "P2",     # Resolve in 4 hours
    ("major", "medium"): "P2",
    ("major", "low"): "P3",
    ("minor", "high"): "P3",     # Resolve in 24 hours
    ("minor", "medium"): "P3",
    ("minor", "low"): "P4",      # Resolve in 72 hours
}

def calculate_priority(impact: str, urgency: str) -> str:
    return severity_matrix.get((impact, urgency), "P4")

```

**Problem Management:**

- Поиск root cause
- Предотвращение повторных инцидентов
- Known Error Database

**Change Management:**

- Контроль изменений в инфраструктуре
- Оценка рисков
- Change Advisory Board (CAB)

```

┌─────────────────────────────────────────────────────────────┐
│                    Change Management Flow                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Request ──▶ Assess ──▶ Authorize ──▶ Plan ──▶ Implement    │
│      │          │           │          │          │         │
│      │          │           │          │          ▼         │
│      │          │           │          │      Review        │
│      │          │           │          │          │         │
│      ▼          ▼           ▼          ▼          ▼         │
│   RFC       Risk        CAB        Schedule    PIR          │
│  Created   Analysis   Approval    Change    (Post Impl      │
│                                              Review)        │
└─────────────────────────────────────────────────────────────┘

```

### 5.4 ITIL и DevOps: интеграция

**Традиционное противостояние:**

```

ITIL:     "Нужен approval от CAB"
DevOps:   "Мы деплоим 50 раз в день!"
ITIL:     "Каждый деплой должен пройти Change Management"
DevOps:   "Это замедлит нас на недели!"

```

**Современный подход — интеграция:**

**Standard Changes:**

- Преапproved changes
- Автоматизированные, низкорисковые
- Не требуют CAB approval каждый раз

```python
# Автоматическая классификация изменений
def classify_change(change: dict) -> str:
    # Standard: преапproved, автоматизированные
    if change["type"] == "deployment":
        if change["has_feature_flag"]:
            if change["tests_passing"]:
                if change["rollback_tested"]:
                    return "standard"  # Auto-approved
    
    # Normal: требует assessment
    if change["risk_level"] == "low":
        return "normal"  # Quick approval
    
    # Emergency: срочные изменения
    if change["is_incident_fix"]:
        return "emergency"  # Expedited process
    
    # Major: CAB review
    return "major"  # Full CAB approval

```

**DevOps-friendly ITIL:**

| ITIL Process | DevOps Integration |
|--------------|-------------------|
| Change Management | Standard changes для CI/CD |
| Incident Management | Automated alerting, on-call |
| Problem Management | Blameless postmortems |
| Service Desk | ChatOps, self-service |
| Configuration Management | Infrastructure as Code |

---

## 6. Scaled Agile (SAFe, LeSS)

### 6.1 Проблема масштабирования

Agile отлично работает для одной команды (5-9 человек). Но что если:

- 100+ разработчиков?
- Несколько продуктов?
- Сложные зависимости?

### 6.2 SAFe (Scaled Agile Framework)

Самый популярный фреймворк для масштабирования Agile.

**Уровни SAFe:**

```

┌──────────────────────────────────────────────────────────────────┐
│                        Portfolio Level                           │
│  Strategic themes, Portfolio Kanban, Lean budgeting              │
├──────────────────────────────────────────────────────────────────┤
│                        Program Level                             │
│  Agile Release Train (ART), Program Increment (PI)               │
├──────────────────────────────────────────────────────────────────┤
│                         Team Level                               │
│  Scrum / Kanban teams, iterations                                │
└──────────────────────────────────────────────────────────────────┘

```

**Agile Release Train (ART):**

- 50-125 человек
- Работают над общим продуктом
- Синхронизированные Program Increments (PI)
- PI Planning каждые 8-12 недель

### 6.3 LeSS (Large-Scale Scrum)

Более "легкий" подход к масштабированию.

**Принципы LeSS:**

- Один Product Backlog для всех команд
- Один Product Owner (или небольшая группа)
- Общий Sprint Review
- Координация между командами минимальная

```

┌────────────────────────────────────────────────────────────────┐
│                            LeSS                                │
│                                                                │
│                    ┌──────────────────┐                        │
│                    │  Product Owner   │                        │
│                    │  (один backlog)  │                        │
│                    └────────┬─────────┘                        │
│                             │                                  │
│         ┌───────────────────┼───────────────────┐              │
│         ▼                   ▼                   ▼              │
│    ┌─────────┐        ┌─────────┐        ┌─────────┐           │
│    │ Team 1  │        │ Team 2  │        │ Team 3  │           │
│    │(Scrum)  │        │(Scrum)  │        │(Scrum)  │           │
│    └─────────┘        └─────────┘        └─────────┘           │
│         │                   │                   │              │
│         └───────────────────┼───────────────────┘              │
│                             ▼                                  │
│                    ┌──────────────────┐                        │
│                    │ Joint Review     │                        │
│                    │ (общий)          │                        │
│                    └──────────────────┘                        │
└────────────────────────────────────────────────────────────────┘

```

### 6.4 SAFe vs LeSS

| Аспект | SAFe | LeSS |
|--------|------|------|
| Структура | Многоуровневая | Минималистичная |
| Роли | Много новых ролей | Минимум ролей |
| Сложность | Высокая | Низкая |
| Prescription | Детальные правила | Принципы |
| Adoption | Постепенное | Big bang |

---

## 7. Выбор методологии для DevOps команды

### 7.1 Decision Framework

```python

def recommend_methodology(
    team_size: int,
    work_predictability: str,  # "high", "medium", "low"
    org_size: int,
    existing_process: str,
    devops_maturity: str  # "beginning", "intermediate", "advanced"
) -> dict:
    
    recommendations = []
    
    # Для одной команды
    if team_size <= 9:
        if work_predictability == "high":
            recommendations.append({
                "method": "Scrum",
                "reason": "Предсказуемая работа хорошо ложится в спринты"
            })
        else:
            recommendations.append({
                "method": "Kanban",
                "reason": "Непредсказуемый поток требует гибкости"
            })
    
    # Для больших организаций
    if org_size > 50:
        if existing_process == "waterfall":
            recommendations.append({
                "method": "SAFe",
                "reason": "Структурированный переход от waterfall"
            })
        else:
            recommendations.append({
                "method": "LeSS",
                "reason": "Минимальные изменения к существующему Agile"
            })
    
    # DevOps специфика
    if devops_maturity == "advanced":
        recommendations.append({
            "method": "Kanban",
            "reason": "Continuous flow для CD/CD"
        })
    
    return recommendations

```

### 7.2 Гибридные подходы

**DevOps + Scrum:**
```

Sprint:
├── Feature development (Scrum backlog items)
├── Infrastructure improvements (20% capacity)
├── Tech debt reduction (10% capacity)
└── On-call and incident response (buffer)

```

**DevOps + Kanban:**
```

Swimlanes:
├── Features (WIP: 3)
├── Bugs/Incidents (WIP: 2)
├── Infrastructure (WIP: 2)
└── Expedite (WIP: 1)

```

### 7.3 Anti-patterns

**"Agile Theatre":**

- Церемонии есть, но нет реальных изменений
- Daily standup = status report
- Retrospective без action items

**"Fragile Scrum":**

- Частые изменения scope в спринте
- Sprint commitment не выполняется
- Нет Definition of Done

**"Kanban without limits":**

- Визуализация есть, WIP limits нет
- Задачи застревают на недели
- Нет фокуса на flow

---

## 8. Практические рекомендации

### 8.1 Начало внедрения

**Шаг 1: Оцените текущее состояние**

```python

current_state = {
    "delivery_frequency": "monthly",
    "lead_time": "4-6 weeks",
    "team_collaboration": "silos",
    "automation_level": "low"
}

```

**Шаг 2: Выберите методологию**
- Начните с простого (Scrum или Kanban)
- Не пытайтесь внедрить SAFe сразу

**Шаг 3: Адаптируйте под DevOps**
- Добавьте Ops tasks в backlog
- Включите deployment в Definition of Done
- Измеряйте DORA metrics

### 8.2 Метрики для оценки

```python
# Метрики эффективности методологии
methodology_metrics = {
    "delivery": {
        "deployment_frequency": "weekly target",
        "lead_time": "< 1 week target",
        "cycle_time": "< 3 days target"
    },
    "quality": {
        "change_failure_rate": "< 15%",
        "escaped_defects": "< 5%",
        "mttr": "< 1 hour"
    },
    "team": {
        "velocity_stability": "< 10% variance",
        "predictability": "> 80% commitment met",
        "team_satisfaction": "> 4/5"
    }
}

```

---

## 💡 Key Takeaways

- **Agile — фундамент DevOps**: DevOps расширяет Agile на весь lifecycle

- **Scrum vs Kanban**: Scrum для предсказуемой работы с ритмом, Kanban для непрерывного потока

- **WIP limits критичны**: Ограничение Work in Progress — ключ к быстрой доставке

- **ITIL 4 совместим с DevOps**: Standard changes и автоматизация позволяют соблюдать governance

- **Выбор методологии зависит от контекста**: Нет универсального решения

---

## 🚀 Next Steps

**Related Modules:**

- [03_Processes](../03_Processes/) — Процессы DevOps и жизненный цикл
- [04_CI](../04_CI/) — Continuous Integration
- [13_Metrics](../13_Metrics/) — Метрики DevOps

**Practice Ideas:**

1. Создайте Kanban board для вашей команды с WIP limits
2. Проведите ретроспективу и определите 3 улучшения
3. Измерьте текущий lead time и cycle time

**Going Deeper:**

- Scrum Guide (официальный гайд, бесплатно)
- "Kanban" by David J. Anderson
- ITIL 4 Foundation

---

## 📚 Additional Resources

**Books:**

- "The Scrum Guide" by Ken Schwaber & Jeff Sutherland — официальный гайд
- "Kanban" by David J. Anderson — определяющая книга по Kanban
- "Accelerate" by Nicole Forsgren — научный подход к метрикам

**Certifications:**

- Professional Scrum Master (PSM I, II, III)
- Kanban Management Professional (KMP)
- ITIL 4 Foundation

**Tools:**

- Jira — project management
- Trello — простой Kanban
- Azure DevOps — интегрированная платформа

---





