# Управление командой и Delivery
## Формирование команды, capacity planning и performance management

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать роль Delivery Manager ([01_Intro](../01_Intro/))
- Знать основы ITSM ([02_ITSM](../02_ITSM/))
- Иметь опыт работы в IT-команде

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Формировать эффективные команды под задачи клиента
- Проводить capacity planning для проектов
- Давать структурированную обратную связь (performance review)
- Управлять мотивацией и предотвращать выгорание
- Балансировать интересы клиента и команды
- Обеспечивать стабильность поставки

---

## 1. Формирование команды

### 1.1 Типичные роли в сервисной команде

| Роль | Ответственность | Типичное соотношение |
|------|-----------------|---------------------|
| **Tech Lead (TL)** | Архитектура, code review, технические решения | 1 на 3-7 разработчиков |
| **Senior Developer** | Сложные задачи, менторинг | 20-30% команды |
| **Middle Developer** | Основной объём разработки | 40-50% команды |
| **Junior Developer** | Простые задачи, обучение | 20-30% команды |
| **QA Engineer** | Тестирование, качество | 1 на 3-5 разработчиков |
| **DevOps Engineer** | Инфраструктура, CI/CD | 0.5-1 на команду |

### 1.2 Модели команд

**Dedicated Team (выделенная команда):**
```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DEDICATED TEAM MODEL                                 │
└─────────────────────────────────────────────────────────────────────────┘

          CLIENT A (100%)
               │
               ▼
    ┌─────────────────────┐
    │      TEAM           │
    │  ┌─────┐ ┌─────┐    │
    │  │ Dev │ │ Dev │    │
    │  └─────┘ └─────┘    │
    │  ┌─────┐ ┌─────┐    │
    │  │ Dev │ │ QA  │    │
    │  └─────┘ └─────┘    │
    │       ┌─────┐       │
    │       │ TL  │       │
    │       └─────┘       │
    └─────────────────────┘

Плюсы: Фокус, погружение, стабильность
Минусы: Риски при уходе людей, сложнее масштабировать
```

**Shared Resource Model (разделяемые ресурсы):**
```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SHARED RESOURCE MODEL                                │
└─────────────────────────────────────────────────────────────────────────┘

    CLIENT A (50%)     CLIENT B (30%)     CLIENT C (20%)
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
                 ┌─────────────────────┐
                 │    SPECIALIST       │
                 │    (DevOps, DBA)    │
                 └─────────────────────┘

Плюсы: Эффективность, экспертиза
Минусы: Конфликт приоритетов, context switching
```

### 1.3 Staffing Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STAFFING PROCESS                                     │
└─────────────────────────────────────────────────────────────────────────┘

1. REQUIREMENTS          2. SEARCH              3. SELECTION
   ───────────────          ──────────             ─────────────
   Что нужно клиенту       Где искать            Как выбираем

┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│• Skills needed  │──▶│• Internal pool  │──▶│• Skills match   │
│• Level          │   │• Bench          │   │• Cultural fit   │
│• Start date     │   │• New hire       │   │• Availability   │
│• Duration       │   │• Contractors    │   │• Client intervie│
└─────────────────┘   └─────────────────┘   └─────────────────┘
        │                     │                                       │
        └─────────────────────┼───────────────────────────────────────┘
                              ▼
                    4. ONBOARDING
                       ───────────────────
                    ┌─────────────────┐
                    │• Project intro  │
                    │• Tech setup     │
                    │• Domain training│
                    │• Buddy system   │
                    └─────────────────┘
```

### 1.4 Team Composition Best Practices

**Правило T-shaped:**
```
    ┌───────────────────────────────────────────┐
    │         Широкие базовые знания            │  ←─ Горизонтальная черта T
    └───────────────────────────────────────────┘
                        │
                        │
                        │  ←─ Глубокая экспертиза
                        │      (вертикальная черта)
                        ▼
```

**Healthy Team Indicators:**

- [ ] Есть хотя бы один Senior на каждое техническое направление
- [ ] Соотношение Dev:QA не хуже 5:1
- [ ] Нет single points of failure (всё критичное знают 2+ человека)
- [ ] Есть bus factor > 1 для ключевых компонентов
- [ ] Баланс опыта: не только juniors, не только seniors

---

## 2. Взаимодействие с техническими лидерами

### 2.1 Роли и ответственность

| Роль | DM (Delivery Manager) | TL (Tech Lead) |
|------|----------------------|----------------|
| **Фокус** | Клиент, процесс, команда | Технические решения, качество |
| **Decisions** | Scope, сроки, ресурсы | Архитектура, инструменты |
| **Metrics** | Velocity, CSAT, SLA | Code quality, tech debt |
| **Escalation** | Клиентские issues | Технические blockers |

### 2.2 Модель взаимодействия

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DM ↔ TL INTERACTION MODEL                            │
└─────────────────────────────────────────────────────────────────────────┘

            DM                                    TL
            │                                                   │
            │     ┌───────────────────────┐                     │
            │     │    SHARED ZONE        │                     │
            │◀────│  • Sprint planning    │──────▶              │
            │     │  • Risk assessment    │                     │
            │     │  • Team health        │                     │
            │     │  • Estimates          │                     │
            │     └───────────────────────┘                     │
            │                                                   │
     ┌──────▼──────┐                      ┌───────▼──────┐
     │ DM ZONE     │                      │ TL ZONE      │
     │             │                      │              │
     │• Client     │                      │• Architecture│
     │  comms      │                      │• Code review │
     │• Contracts  │                      │• Tech debt   │
     │• Financials │                      │• Mentoring   │
     │• Reporting  │                      │• Tool choice │
     └─────────────┘                      └──────────────┘
```

### 2.3 Синхронизация DM-TL

**Регулярные встречи:**

| Формат | Частота | Agenda |
|--------|---------|--------|
| Quick sync | Daily (5-10 min) | Blockers, urgent items |
| Detailed sync | Weekly (30 min) | Sprint progress, risks, team issues |
| Planning | Bi-weekly | Sprint planning, capacity |
| Retrospective | Bi-weekly | Process improvements |

**Вопросы для weekly sync:**
```
1. Как идёт спринт? Есть ли риски не успеть?
2. Какие технические blockers?
3. Как команда? Есть ли issues с людьми?
4. Нужно ли что-то от меня / клиента?
5. Что планируем на следующую неделю?
```

---

## 3. Capacity Planning

### 3.1 Основные понятия

**Capacity** — сколько работы команда может выполнить за период.

**Utilization** — процент времени, потраченного на billable работу.

```
Utilization = (Billable hours / Available hours) × 100%

Пример:
- Рабочих часов в месяце: 168
- Billable hours: 144
- Utilization = 144 / 168 = 85.7%
```

### 3.2 Факторы, влияющие на capacity

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CAPACITY FACTORS                                     │
└─────────────────────────────────────────────────────────────────────────┘

  TOTAL CALENDAR TIME: 168 hours/month
                │
                ▼
  ─────────────────────────────────
  │ Отпуска, больничные     -16h │  (примерно 10%)
  ─────────────────────────────────
                │
                ▼
  ─────────────────────────────────
  │ Митинги, ceremonies     -16h │  (примерно 10%)
  ─────────────────────────────────
                │
                ▼
  ─────────────────────────────────
  │ Обучение, non-billable  -8h  │  (примерно 5%)
  ─────────────────────────────────
                │
                ▼
  ─────────────────────────────────
  │ Admin, support          -8h  │  (примерно 5%)
  ─────────────────────────────────
                │
                ▼
  EFFECTIVE CAPACITY: ~120h/month (70-75%)
```

### 3.3 Capacity Planning Template

```
┌─────────────────────────────────────────────────────────────────────────┐
│              CAPACITY PLANNING - JANUARY 2025                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Working days: 22                                                        │
│ Working hours: 176                                                      │
│                                                                         │
│ ┌────────────────────────────────────────────────────────────────────┐  │
│ │ TEAM MEMBER      │ AVAILABLE │ PLANNED PTO │ NET HOURS │ PROJECT  │   │
│ ├──────────────────┼───────────┼─────────────┼───────────┼──────────┤   │
│ │ Alex (TL)        │    176    │      0      │    150    │ Phoenix  │   │
│ │ Maria (Senior)   │    176    │     16      │    136    │ Phoenix  │   │
│ │ John (Middle)    │    176    │      0      │    150    │ Phoenix  │   │
│ │ Kate (Middle)    │    176    │      8      │    143    │ Phoenix  │   │
│ │ Tom (Junior)     │    176    │      0      │    150    │ Phoenix  │   │
│ │ Sarah (QA)       │    176    │     24      │    129    │ Phoenix  │   │
│ ├──────────────────┼───────────┼─────────────┼───────────┼──────────┤   │
│ │ TOTAL            │   1056    │     48      │    858    │          │   │
│ └────────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│ Estimated velocity: ~180 SP (based on 80 SP/4 devs per sprint)          │
│ Risk: QA capacity reduced due to PTO                                    │
│ Mitigation: Shift QA tasks to early in month                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.4 Capacity vs Demand

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CAPACITY vs DEMAND ANALYSIS                          │
└─────────────────────────────────────────────────────────────────────────┘

  CAPACITY                              DEMAND
  (сколько можем)                       (сколько нужно)
       │                                     │
       ▼                                     ▼
  ┌─────────┐                          ┌─────────┐
  │  858 h  │                          │  920 h  │
  └─────────┘                          └─────────┘
       │                                              │
       └──────────────┬───────────────────────────────┘
                      ▼
              ┌─────────────┐
              │   GAP: 62h  │
              └─────────────┘
                      │
                      ▼
            ACTIONS TO CLOSE GAP:
            ─────────────────────
            1. Reduce scope (defer features)
            2. Add resources (hire, contractor)
            3. Increase capacity (overtime - last resort)
            4. Negotiate timeline (extend deadline)
```

---

## 4. Performance Review

### 4.1 Цели Performance Review

- Дать обратную связь о работе
- Определить области роста
- Согласовать цели на период
- Мотивировать и удерживать
- Выявить проблемы рано

### 4.2 Структура Performance Review

```
┌────────────────────────────────────────────────────────────────────────┐
│                    PERFORMANCE REVIEW STRUCTURE                        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│ 1. SELF-ASSESSMENT (от сотрудника)                                     │
│    ─────────────────────────────────                                   │
│    • Что считаю главными достижениями?                                 │
│    • Где вижу области для улучшения?                                   │
│    • Какие цели хочу поставить?                                        │
│                                                                        │
│ 2. MANAGER ASSESSMENT                                                  │
│    ─────────────────────────────────                                   │
│    • Достижения и сильные стороны                                      │
│    • Области для развития                                              │
│    • Оценка по критериям                                               │
│                                                                        │
│ 3. 360° FEEDBACK (опционально)                                         │
│    ─────────────────────────────────                                   │
│    • Обратная связь от коллег                                          │
│    • Feedback от клиента                                               │
│                                                                        │
│ 4. REVIEW MEETING                                                      │
│    ─────────────────────────────────                                   │
│    • Обсуждение всех inputs                                            │
│    • Согласование целей                                                │
│    • Определение плана развития                                        │
│                                                                        │
│ 5. DEVELOPMENT PLAN                                                    │
│    ─────────────────────────────────                                   │
│    • Конкретные цели на период                                         │
│    • Необходимые ресурсы/обучение                                      │
│    • Check-in points                                                   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Техника обратной связи: SBI

**SBI = Situation → Behavior → Impact**

```
❌ Плохо:
"Ты плохо работаешь с командой"

✅ Хорошо (SBI):
"[Situation] На прошлой неделе во время code review
[Behavior] ты отклонил PR без объяснения причин
[Impact] Это расстроило Джона и замедлило его работу на полдня"
```

**Примеры SBI:**

| Тип | Situation | Behavior | Impact |
|-----|-----------|----------|--------|
| Positive | На вчерашнем демо | ты отлично объяснил техническое решение нетехническому клиенту | клиент одобрил подход без дополнительных вопросов |
| Constructive | В sprint planning | ты дал оценку без обсуждения с командой | команда не согласна, и мы рискуем не успеть |

### 4.4 Performance Issues

**Ранние признаки проблем:**

- Снижение velocity
- Увеличение количества багов
- Опоздания на митинги
- Отсутствие инициативы
- Конфликты с коллегами
- Частые отсутствия

**Подход к решению:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PERFORMANCE IMPROVEMENT PROCESS                      │
└─────────────────────────────────────────────────────────────────────────┘

  Step 1              Step 2              Step 3              Step 4
  IDENTIFY            DISCUSS             SUPPORT             MONITOR
  ─────────           ─────────           ─────────           ─────────

┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│ Заметить  │────▶│1-on-1     │────▶│ PIP или   │────▶│ Regular   │
│ симптомы  │     │ разговор  │     │ поддержка │     │ check-ins │
└───────────┘     └───────────┘     └───────────┘     └───────────┘
                        │                                                                 │
                        │                                                                 │
                Понять причину     Дать ресурсы и время
```

**PIP (Performance Improvement Plan):**
```
┌─────────────────────────────────────────────────────────────────────────┐
│              PERFORMANCE IMPROVEMENT PLAN                               │
├─────────────────────────────────────────────────────────────────────────┤
│ Employee: John Smith                                                    │
│ Manager: Alex Johnson                                                   │
│ Period: Jan 15 - Mar 15, 2025 (60 days)                                 │
│                                                                         │
│ CURRENT ISSUES:                                                         │
│ • Velocity below team average (15 SP vs 25 SP target)                   │
│ • 3 critical bugs in last month attributed to code                      │
│ • Missed 2 sprint commitments                                           │
│                                                                         │
│ IMPROVEMENT GOALS:                                                      │
│ 1. Increase velocity to 22+ SP/sprint                                   │
│ 2. Zero critical bugs in code                                           │
│ 3. Meet all sprint commitments                                          │
│                                                                         │
│ SUPPORT PROVIDED:                                                       │
│ • Weekly 1-on-1 with TL (code review, pairing)                          │
│ • Reduced scope for first 2 weeks                                       │
│ • Testing course enrollment                                             │
│                                                                         │
│ CHECK-IN SCHEDULE:                                                      │
│ • Weekly: progress review with TL                                       │
│ • Bi-weekly: 1-on-1 with DM                                             │
│ • Day 30: mid-point assessment                                          │
│ • Day 60: final assessment                                              │
│                                                                         │
│ OUTCOME:                                                                │
│ Goals met → Continue normal work                                        │
│ Goals not met → Further actions to be discussed                         │
│                                                                         │
│ Signatures:                                                             │
│ Employee: ____________  Manager: ____________  Date: ____________       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Мотивация и демотивация

### 5.1 Факторы мотивации (по Herzberg)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    HERZBERG'S TWO-FACTOR THEORY                         │
└─────────────────────────────────────────────────────────────────────────┘

  HYGIENE FACTORS                      MOTIVATORS
  (их отсутствие демотивирует)         (их наличие мотивирует)
  ─────────────────────────            ─────────────────────────
  
  • Зарплата                           • Достижения
  • Условия работы                     • Признание
  • Отношения с коллегами              • Интересная работа
  • Политика компании                  • Ответственность
  • Безопасность                       • Рост и развитие
  • Баланс работа/жизнь               • Карьерный путь
  
  ▲                                    ▲
  │                                    │
  │  Не мотивируют сами по себе,      │  Создают мотивацию
  │  но их отсутствие                 │  и удовлетворение
  │  создаёт недовольство             │
  │                                   │
```

### 5.2 Что мотивирует разработчиков

**Исследование Stack Overflow (топ-5):**

1. Интересные технологии и задачи
2. Возможность учиться и расти
3. Work-life balance
4. Команда и культура
5. Compensation (зарплата, бенефиты)

**Практические действия менеджера:**

| Мотиватор | Действия |
|-----------|----------|
| Интересные задачи | Ротация, разнообразие, новые технологии |
| Рост | Менторинг, конференции, курсы, challenging tasks |
| Признание | Публичная похвала, бонусы, awards |
| Автономия | Доверие, самостоятельность в решениях |
| Влияние | Участие в важных решениях, видимость результата |

### 5.3 Что демотивирует

**Red flags:**

- Микроменеджмент
- Отсутствие feedback
- Непонятные цели
- Токсичные коллеги
- Нереалистичные дедлайны
- Игнорирование идей
- Отсутствие роста
- Unfair treatment

---

## 6. Профилактика выгорания

### 6.1 Признаки выгорания

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BURNOUT WARNING SIGNS                                │
└─────────────────────────────────────────────────────────────────────────┘

  PHYSICAL                EMOTIONAL               BEHAVIORAL
  ─────────────           ─────────────           ─────────────
  
  • Усталость             • Цинизм                • Снижение
  • Бессонница            • Апатия                  производительности
  • Частые                • Раздражительность     • Опоздания
    болезни               • Отстранённость        • Избегание
  • Головные боли         • Чувство               • Прокрастинация
  • Изменение               бессмысленности       • Изоляция
    аппетита              • Anxiety               • Конфликты
```

### 6.2 Причины выгорания в IT

| Причина | Как проявляется |
|---------|-----------------|
| Workload | Постоянные переработки, unrealistic deadlines |
| Control | Нет влияния на решения, микроменеджмент |
| Reward | Недостаточное признание, unfair compensation |
| Community | Токсичная культура, конфликты |
| Fairness | Политика, несправедливость |
| Values | Конфликт ценностей с компанией/проектом |

### 6.3 Prevention Strategies

**Для менеджера:**
```
✅ DO:
• Следить за workload и overtime
• Регулярные 1-on-1 для check-in
• Обеспечивать чёткие приоритеты
• Защищать от scope creep
• Поощрять отпуска
• Создавать psychological safety

❌ DON'T:
• Игнорировать признаки
• Поощрять героизм
• Ставить нереалистичные дедлайны
• Наказывать за ошибки
• Отменять отпуска
```

**Workload Management:**
```
Sustainable Pace = 40 hours/week
Acceptable Short-term = 45-50 hours (2-3 weeks max)
Danger Zone = 50+ hours sustained
```

---

## 7. Баланс интересов клиента и команды

### 7.1 Типичные конфликты

| Клиент хочет | Команда хочет | Решение |
|--------------|---------------|---------|
| Больше features | Время на рефакторинг | Tech debt budget (20% времени) |
| Faster delivery | Work-life balance | Realistic planning, buffer |
| 24/7 availability | Нормальный график | On-call rotation, clear SLA |
| Specific person | Ротация | Knowledge sharing, backup |

### 7.2 Framework для принятия решений

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DECISION FRAMEWORK                                   │
└─────────────────────────────────────────────────────────────────────────┘

  ВОПРОС: Клиент просит работать в выходные до релиза

  STEP 1: UNDERSTAND
  ─────────────────────
  • Почему это нужно клиенту? (real urgency?)
  • Какие последствия отказа?
  • Есть ли альтернативы?

  STEP 2: ASSESS IMPACT
  ─────────────────────
  • На команду: overtime, burnout risk
  • На проект: quality, sustainability
  • На отношения: trust, precedent

  STEP 3: EXPLORE OPTIONS
  ─────────────────────
  • Волонтёры + компенсация
  • Сократить scope
  • Сдвинуть дедлайн
  • Добавить ресурсы

  STEP 4: NEGOTIATE
  ─────────────────────
  • Представить trade-offs клиенту
  • Согласовать acceptable solution
  • Задокументировать

  STEP 5: PROTECT TEAM
  ─────────────────────
  • Компенсация overtime
  • Recovery time после
  • Не делать привычкой
```

### 7.3 Защита команды

**Когда нужно сказать "нет" клиенту:**

- Нереалистичные сроки угрожают качеству
- Постоянные overtime без компенсации
- Токсичное поведение от клиента
- Scope creep без увеличения ресурсов

**Как защищать:**
```
❌ "Команда не хочет"
✅ "Для обеспечения качества нам нужно..."

❌ "Это невозможно"
✅ "Мы можем сделать X, если Y (trade-off)"

❌ Молча соглашаться и переносить давление на команду
✅ Эскалировать, если клиент неадекватен
```

---

## 8. Стабильность поставки

### 8.1 Метрики delivery

| Метрика | Описание | Target |
|---------|----------|--------|
| Velocity | Story points за спринт | Стабильная ±15% |
| Predictability | % committed vs delivered | >85% |
| Lead Time | Время от начала до done | Зависит от задачи |
| Cycle Time | Время активной работы | Минимизировать |
| Throughput | Задач в единицу времени | Стабильный |

### 8.2 Стабилизация velocity

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    VELOCITY STABILIZATION                               │
└─────────────────────────────────────────────────────────────────────────┘

  UNSTABLE                                    STABLE
  ─────────────                               ─────────────
  
  SP │    *              *                    SP │
  50 │         *                              50 │    ___    ___    ___
  40 │    *         *         *               40 │___│   │__│   │__│   │
  30 │                    *                   30 │
  20 │         *                              20 │
     └───────────────────────                    └───────────────────────
       Sprint 1  2  3  4  5                        Sprint 1  2  3  4  5

  Causes of instability:         Stabilization actions:
  • Unclear requirements         • Better refinement
  • Scope creep                  • Protected sprint scope
  • Interruptions                • Focus time
  • Team changes                 • Knowledge sharing
  • Tech debt                    • 20% maintenance
```

### 8.3 Delivery Best Practices

**Sprint Hygiene:**

- [ ] Backlog refinement до planning
- [ ] Чёткие acceptance criteria
- [ ] No scope changes mid-sprint
- [ ] Daily standups focused
- [ ] Demo готово к концу спринта

**Continuous Improvement:**

- [ ] Retrospectives каждый спринт
- [ ] Action items tracked
- [ ] Metrics reviewed monthly
- [ ] Process improvements implemented

---

## 9. Практический кейс

### 9.1 Сценарий

**Ситуация:** Инженер показывает низкую результативность 2 спринта подряд. Клиент начинает замечать и задаёт вопросы.

### 9.2 Анализ

```
FACTS:
• John - Middle developer, 2 года в компании
• Последние 2 спринта: 15 SP vs обычных 25 SP
• Увеличилось количество багов в его коде
• Клиент заметил и спросил "что с John?"

POSSIBLE CAUSES:
□ Personal issues (family, health)
□ Burnout (работал 3 месяца без отпуска)
□ Skill gap (новая технология)
□ Motivation (boring tasks)
□ Team issues (conflict with colleague)
□ External factors (relocation, visa)
```

### 9.3 Action Plan

```
STEP 1: 1-on-1 с John (сегодня)
─────────────────────────────────
• Спросить как дела (open-ended)
• Выразить concern без обвинений
• Выслушать его perspective
• Понять root cause

STEP 2: Обратная связь клиенту
─────────────────────────────────
• Acknowledge concern
• Сообщить, что работаем над ситуацией
• Не раскрывать personal details

Email to client:
"Thanks for flagging this. We're aware of the situation 
and actively addressing it. I'll update you next week 
on our progress. The team is covering the workload 
in the meantime."

STEP 3: Support Plan (в зависимости от причины)
─────────────────────────────────
If burnout → отпуск, reduced load
If skill gap → training, pairing
If personal → flexibility, EAP
If motivation → task rotation, new challenges

STEP 4: Monitor
─────────────────────────────────
• Weekly check-ins
• Track metrics
• Update client as appropriate
• Adjust plan if needed
```

---

## 💡 Key Takeaways

- **Формирование команды** — баланс уровней (senior/middle/junior), T-shaped skills, bus factor > 1

- **DM-TL партнёрство** — чёткое разделение зон, регулярная синхронизация, shared decisions

- **Capacity planning** — учитывать все факторы (PTO, meetings, training), planning vs demand

- **Performance feedback** — использовать SBI (Situation-Behavior-Impact), регулярные 1-on-1

- **Мотивация** — интересные задачи, рост, признание, автономия важнее денег

- **Burnout prevention** — мониторить workload, защищать от overtime, поощрять отпуска

- **Баланс интересов** — защищать команду, но объяснять trade-offs клиенту

---

## 🚀 Next Steps

**Related Modules:**

- [05_Finance](../05_Finance/) — Финансовая грамотность менеджера
- [03_Communication](../03_Communication/) — Коммуникации с клиентом

**Practice Ideas:**

1. Проведите capacity planning для своей команды на следующий месяц
2. Подготовьте и проведите 1-on-1 с использованием SBI feedback
3. Оцените свою команду по checklist "Healthy Team Indicators"

**Going Deeper:**

- "The Manager's Path" by Camille Fournier
- "Radical Candor" by Kim Scott
- "Drive" by Daniel Pink

---

## 📚 Additional Resources

**Книги:**

- "The Manager's Path" — путь инженерного менеджера
- "Radical Candor" — искусство честной обратной связи
- "An Elegant Puzzle" by Will Larson — системы для engineering management
- "First, Break All the Rules" by Gallup — что делают лучшие менеджеры

**Tools:**

- 15Five, Lattice — для 1-on-1 и performance reviews
- Jira, Monday — capacity planning
- Culture Amp, Officevibe — team health surveys

**Articles:**

- [re:Work by Google](https://rework.withgoogle.com/) — research-based management practices
- [Lara Hogan's blog](https://larahogan.me/) — engineering leadership

---






