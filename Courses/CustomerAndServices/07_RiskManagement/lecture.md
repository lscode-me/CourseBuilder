# Управление рисками и эскалациями
## Идентификация рисков, эскалации и Root Cause Analysis

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать процессы ITSM ([02_ITSM](../02_ITSM/))
- Знать основы коммуникации с клиентом ([03_Communication](../03_Communication/))
- Иметь опыт работы на проектах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Идентифицировать и классифицировать риски в сервисных проектах
- Применять модель Risk = Likelihood × Impact
- Распознавать ранние сигналы недовольства клиента
- Правильно проводить эскалации
- Защищать команду при сохранении отношений с клиентом
- Проводить Root Cause Analysis (RCA)

---

## 1. Типичные риски в сервисных проектах

### 1.1 Категории рисков

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RISK CATEGORIES                                      │
└─────────────────────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────────────┐
  │                        DELIVERY RISKS                                │
  │  • Scope creep                    • Tech debt accumulation          │
  │  • Missed deadlines               • Quality issues                   │
  │  • Underestimation                • Integration problems            │
  └──────────────────────────────────────────────────────────────────────┘
  
  ┌──────────────────────────────────────────────────────────────────────┐
  │                        PEOPLE RISKS                                  │
  │  • Key person dependency          • Burnout                         │
  │  • Attrition / turnover           • Skill gaps                      │
  │  • Team conflicts                 • Performance issues              │
  └──────────────────────────────────────────────────────────────────────┘
  
  ┌──────────────────────────────────────────────────────────────────────┐
  │                        CLIENT RISKS                                  │
  │  • Changing requirements          • Stakeholder changes             │
  │  • Budget cuts                    • Strategic pivot                 │
  │  • Communication breakdown        • Unrealistic expectations        │
  └──────────────────────────────────────────────────────────────────────┘
  
  ┌──────────────────────────────────────────────────────────────────────┐
  │                        EXTERNAL RISKS                                │
  │  • Vendor/3rd party issues        • Regulatory changes              │
  │  • Market changes                 • Force majeure                   │
  │  • Technology obsolescence        • Security threats                │
  └──────────────────────────────────────────────────────────────────────┘
```

### 1.2 Top-10 рисков в аутсорсинге

| # | Риск | Вероятность | Impact | Митигация |
|---|------|-------------|--------|-----------|
| 1 | Scope creep | High | High | Change control, clear requirements |
| 2 | Key person leaves | Medium | High | Knowledge sharing, documentation |
| 3 | Underestimation | High | Medium | Buffer, historical data |
| 4 | Client delays | Medium | Medium | Clear dependencies, escalation |
| 5 | Quality issues | Medium | High | QA process, code review |
| 6 | Communication breakdown | Medium | High | Regular sync, documentation |
| 7 | Budget cuts | Low | High | Early warning, value demonstration |
| 8 | Tech debt | High | Medium | Dedicated time, prioritization |
| 9 | Team burnout | Medium | High | Workload management, monitoring |
| 10 | Stakeholder change | Low | High | Multiple relationships, documentation |

---

## 2. Модель оценки рисков

### 2.1 Формула риска

```
Risk Score = Likelihood × Impact
```

### 2.2 Шкала оценки

**Likelihood (Вероятность):**

| Уровень | Значение | Описание |
|---------|----------|----------|
| 1 | Rare | Маловероятно (<10%) |
| 2 | Unlikely | Низкая вероятность (10-25%) |
| 3 | Possible | Средняя вероятность (25-50%) |
| 4 | Likely | Высокая вероятность (50-75%) |
| 5 | Almost certain | Почти наверняка (>75%) |

**Impact (Влияние):**

| Уровень | Значение | Описание |
|---------|----------|----------|
| 1 | Negligible | Минимальное влияние |
| 2 | Minor | Небольшие неудобства |
| 3 | Moderate | Заметное влияние на проект |
| 4 | Major | Значительное влияние на сроки/качество |
| 5 | Catastrophic | Критическое, угроза проекту/отношениям |

### 2.3 Risk Matrix

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RISK ASSESSMENT MATRIX                               │
└─────────────────────────────────────────────────────────────────────────┘

                              IMPACT
              1        2        3        4        5
           Negligible Minor  Moderate  Major  Catastrophic
         ┌────────┬────────┬────────┬────────┬────────┐
    5    │   5    │   10   │   15   │   20   │   25   │  Almost
  Almost │  LOW   │ MEDIUM │  HIGH  │  HIGH  │ CRITICAL│  certain
         ├────────┼────────┼────────┼────────┼────────┤
L   4    │   4    │    8   │   12   │   16   │   20   │  Likely
I Likely │  LOW   │ MEDIUM │ MEDIUM │  HIGH  │  HIGH  │
K        ├────────┼────────┼────────┼────────┼────────┤
E   3    │   3    │    6   │    9   │   12   │   15   │  Possible
L Possible│  LOW  │  LOW   │ MEDIUM │ MEDIUM │  HIGH  │
I        ├────────┼────────┼────────┼────────┼────────┤
H   2    │   2    │    4   │    6   │    8   │   10   │  Unlikely
O Unlikely│  LOW  │  LOW   │  LOW   │ MEDIUM │ MEDIUM │
O        ├────────┼────────┼────────┼────────┼────────┤
D   1    │   1    │    2   │    3   │    4   │    5   │  Rare
    Rare │  LOW   │  LOW   │  LOW   │  LOW   │ MEDIUM │
         └────────┴────────┴────────┴────────┴────────┘

  LEGEND:
  1-4:   LOW      - Monitor, accept
  5-9:   MEDIUM   - Mitigate, regular review
  10-15: HIGH     - Active management, escalate
  16-25: CRITICAL - Immediate action required
```

---

## 3. Risk Register

### 3.1 Структура Risk Register

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RISK REGISTER                                        │
│                    Project: Phoenix App                                 │
│                    Last Updated: December 10, 2024                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ ID   │ Risk Description      │ L │ I │ Score │ Status │ Owner │ Mitigation
│ ─────┼───────────────────────┼───┼───┼───────┼────────┼───────┼──────────
│ R001 │ Key developer leaves  │ 3 │ 4 │  12   │ OPEN   │ DM    │ Knowledge
│      │                       │   │   │ HIGH  │        │       │ sharing,
│      │                       │   │   │       │        │       │ documentation
│ ─────┼───────────────────────┼───┼───┼───────┼────────┼───────┼──────────
│ R002 │ Scope creep from      │ 4 │ 3 │  12   │ OPEN   │ DM    │ Change control
│      │ unclear requirements  │   │   │ HIGH  │        │       │ process, weekly
│      │                       │   │   │       │        │       │ scope review
│ ─────┼───────────────────────┼───┼───┼───────┼────────┼───────┼──────────
│ R003 │ Payment API vendor    │ 2 │ 4 │   8   │ OPEN   │ TL    │ Alternative
│      │ delays integration    │   │   │ MED   │        │       │ vendor eval,
│      │                       │   │   │       │        │       │ buffer in plan
│ ─────┼───────────────────────┼───┼───┼───────┼────────┼───────┼──────────
│ R004 │ Team burnout before   │ 3 │ 3 │   9   │ MITIG  │ DM    │ Monitoring
│      │ Q4 release            │   │   │ MED   │        │       │ workload, no
│      │                       │   │   │       │        │       │ overtime policy
│ ─────┼───────────────────────┼───┼───┼───────┼────────┼───────┼──────────
│ R005 │ Budget cut after Q1   │ 2 │ 5 │  10   │ WATCH  │ AM    │ Demonstrate
│      │                       │   │   │ MED   │        │       │ value, QBR
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Risk Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RISK LIFECYCLE                                       │
└─────────────────────────────────────────────────────────────────────────┘

  IDENTIFY        ASSESS          PLAN           EXECUTE         MONITOR
  ────────        ──────          ────           ───────         ───────
  
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ Discover │──▶│ L × I =  │──▶│ Mitigation│──▶│ Implement│──▶│ Track &  │
│ new risks│   │ Score    │   │ strategy  │   │ controls │   │ review   │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
                    │                             │               │
                    │                             │               │
              ┌─────▼─────┐                 ┌─────▼─────┐   ┌─────▼─────┐
              │ Prioritize│                 │ Update    │   │ Close or  │
              │           │                 │ Register  │   │ Escalate  │
              └───────────┘                 └───────────┘   └───────────┘
```

### 3.3 Стратегии митигации

| Стратегия | Описание | Когда использовать |
|-----------|----------|-------------------|
| **Avoid** | Изменить план, чтобы исключить риск | High impact, можно избежать |
| **Mitigate** | Снизить likelihood или impact | Medium-High risks |
| **Transfer** | Передать риск другой стороне | Insurance, contracts |
| **Accept** | Принять риск и его последствия | Low risks, no mitigation possible |

---

## 4. Ранние сигналы недовольства клиента

### 4.1 Warning Signs

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CLIENT DISSATISFACTION SIGNALS                       │
└─────────────────────────────────────────────────────────────────────────┘

  COMMUNICATION SIGNALS:
  ──────────────────────
  ⚠️ Клиент стал отвечать медленнее
  ⚠️ Меньше участвует в митингах
  ⚠️ Тон коммуникации стал формальнее
  ⚠️ Перестал делиться планами
  ⚠️ Задаёт больше контрольных вопросов

  BEHAVIORAL SIGNALS:
  ──────────────────────
  ⚠️ Микроменеджмент (больше контроля)
  ⚠️ Запрашивает detailed reports
  ⚠️ Подключает своё руководство к звонкам
  ⚠️ Параллельно общается с другими vendors
  ⚠️ Просит доступ к системам "для аудита"

  BUSINESS SIGNALS:
  ──────────────────────
  ⚠️ Откладывает expansion discussions
  ⚠️ Не продлевает контракт заранее
  ⚠️ Замораживает scope additions
  ⚠️ Сокращает бюджет
  ⚠️ Упоминает "пересмотр partnership"
```

### 4.2 Escalation Triggers

| Signal | Severity | Action |
|--------|----------|--------|
| Missed deadline | Medium | Immediate update, recovery plan |
| Quality complaint | Medium | RCA, improvement plan |
| Multiple complaints | High | Executive involvement |
| Threat to end contract | Critical | C-level escalation |
| Already talking to competitor | Critical | Retention plan, leadership |

---

## 5. Проведение эскалаций

### 5.1 Типы эскалаций

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ESCALATION TYPES                                     │
└─────────────────────────────────────────────────────────────────────────┘

  FUNCTIONAL (Horizontal)              HIERARCHICAL (Vertical)
  ───────────────────────              ─────────────────────────
  
  К специалистам                       К руководству
  с нужной экспертизой                 для ресурсов/решений
  
  L1 Support ──▶ L2 ──▶ L3             Engineer ──▶ TL ──▶ DM ──▶ Director
  
  Цель: Решить                         Цель: Получить
  технически                           authority, resources
```

### 5.2 Когда эскалировать

**Эскалируй РАНО, если:**
- SLA под угрозой
- Нужны ресурсы вне твоих полномочий
- Конфликт интересов требует decision
- Клиент недоволен и ситуация ухудшается
- Риск репутационного ущерба

**НЕ эскалируй, если:**
- Можешь решить сам
- Это рутинный вопрос
- Просто хочешь снять ответственность

### 5.3 Структура escalation message

```
ESCALATION EMAIL TEMPLATE

Subject: [ESCALATION] [Priority] Brief description

SITUATION:
• Что произошло (факты)
• Когда началось
• Кто затронут

IMPACT:
• Влияние на бизнес клиента
• Влияние на наш бизнес
• SLA status

CURRENT STATUS:
• Что уже сделано
• Что делается сейчас
• Текущие blockers

ASK:
• Что конкретно нужно (ресурсы, решение, approval)
• От кого именно

TIMELINE:
• Когда нужно решение
• Когда следующий update
```

### 5.4 Пример эскалации

```
Subject: [ESCALATION P1] Payment service outage - Client Phoenix

Hi Alex,

I'm escalating an ongoing critical incident affecting our client Phoenix.

SITUATION:
• Payment service has been down since 14:30 UTC (2 hours ago)
• Root cause: Database connection pool exhausted
• All payment transactions blocked

IMPACT:
• Client estimates $10,000/hour revenue loss
• SLA breach: P1 target is 4 hours, currently at 2 hours
• Client CEO is aware and requesting update

CURRENT STATUS:
• DBA has identified the issue
• Fix requires config change that needs production access
• We don't have production DB access for this client

ASK:
• Need approval to request emergency production access from client
• Need DBA to be on-call for next 4 hours

TIMELINE:
• Decision needed in next 30 minutes to avoid SLA breach
• Will provide update at 17:00 UTC

Best regards,
John
Delivery Manager
Mobile: +1-555-0123
```

---

## 6. Root Cause Analysis (RCA)

### 6.1 Что такое RCA

**Root Cause Analysis** — систематический процесс выявления корневых причин проблемы для предотвращения её повторения.

### 6.2 Методы RCA

**1. 5 Whys:**
```
Problem: Service was down for 2 hours

Why 1: Why was service down?
→ Database connections exhausted

Why 2: Why were connections exhausted?
→ Connection leak in new code

Why 3: Why was there a connection leak?
→ Connections not properly closed in error path

Why 4: Why wasn't this caught in testing?
→ Load test didn't cover error scenarios

Why 5: Why didn't load test cover error scenarios?
→ No requirement for error path testing in load tests

ROOT CAUSE: Missing load test coverage for error scenarios
ACTION: Add error scenario coverage to load testing requirements
```

**2. Fishbone Diagram (Ishikawa):**
```
                                        ┌────────────────┐
                                        │    PROBLEM:    │
                                        │   Service down │
                                        └───────┬────────┘
                                                │
        ┌───────────────┬───────────────────────┼───────────────────────┬───────────────┐
        │               │                       │                       │               │
   ┌────┴────┐    ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐        │
   │ PEOPLE  │    │  PROCESS  │           │TECHNOLOGY │           │ENVIRONMENT│        │
   │         │    │           │           │           │           │           │        │
   │•No code │    │•No error  │           │•Connection│           │•High load │        │
   │ review  │    │ scenario  │           │ leak      │           │ (peak     │        │
   │ for     │    │ in load   │           │•No conn   │           │  time)    │        │
   │ conn    │    │ tests     │           │ pool      │           │           │        │
   │ mgmt    │    │           │           │ monitoring│           │           │        │
   └─────────┘    └───────────┘           └───────────┘           └───────────┘        │
```

### 6.3 RCA Document Template

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROOT CAUSE ANALYSIS REPORT                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Incident ID: INC-2024-0142                                              │
│ Date: December 10, 2024                                                 │
│ Author: John Smith, Delivery Manager                                    │
│ Status: Final                                                           │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 1. EXECUTIVE SUMMARY                                                    │
│ ─────────────────────────────────────────────────────────────────────  │
│ Payment service experienced 2-hour outage on Dec 10, 2024, affecting   │
│ all payment transactions. Root cause was database connection leak in   │
│ new release. Service was restored at 16:30 UTC.                        │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 2. TIMELINE                                                             │
│ ─────────────────────────────────────────────────────────────────────  │
│ 12:00 - Release 2.3.1 deployed to production                           │
│ 14:25 - First user complaints received                                 │
│ 14:30 - Incident declared, investigation started                       │
│ 15:00 - Root cause identified (connection leak)                        │
│ 15:30 - Decision to rollback made                                      │
│ 16:00 - Rollback completed                                             │
│ 16:30 - Service fully restored, monitoring continues                   │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 3. IMPACT                                                               │
│ ─────────────────────────────────────────────────────────────────────  │
│ • Duration: 2 hours                                                    │
│ • Users affected: All (100%)                                           │
│ • Transactions blocked: ~5,000                                         │
│ • Estimated revenue impact: $20,000                                    │
│ • SLA impact: P1 target met (4h), but close                            │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 4. ROOT CAUSE                                                           │
│ ─────────────────────────────────────────────────────────────────────  │
│                                                                         │
│ DIRECT CAUSE:                                                           │
│ Database connection leak in payment service v2.3.1                     │
│                                                                         │
│ CONTRIBUTING FACTORS:                                                   │
│ • Error handling path didn't close connections properly                │
│ • Code review didn't catch the issue                                   │
│ • Load testing didn't include error scenarios                          │
│ • No connection pool monitoring in place                               │
│                                                                         │
│ ROOT CAUSE:                                                             │
│ Missing error path testing in load test suite                          │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 5. WHAT WENT WELL                                                       │
│ ─────────────────────────────────────────────────────────────────────  │
│ ✅ Quick incident detection (5 minutes from first symptoms)            │
│ ✅ Fast decision to rollback rather than debug in production           │
│ ✅ Good communication with client throughout                           │
│ ✅ SLA target was met                                                   │
│                                                                         │
│ ═══════════════════════════════════════════════════════════────────────│
│ 6. WHAT COULD BE IMPROVED                                               │
│ ─────────────────────────────────────────────────────────────────────  │
│ ❌ Connection leak wasn't caught in code review                        │
│ ❌ Load testing didn't cover error scenarios                           │
│ ❌ No automated monitoring for connection pool                         │
│ ❌ Deploy happened on Friday (high-risk day)                           │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 7. ACTION ITEMS                                                         │
│ ─────────────────────────────────────────────────────────────────────  │
│                                                                         │
│ # │ Action                              │ Owner    │ Due    │ Status   │
│───┼─────────────────────────────────────┼──────────┼────────┼──────────│
│ 1 │ Add error scenario to load tests    │ QA Lead  │ Dec 20 │ Open     │
│ 2 │ Add connection pool monitoring      │ DevOps   │ Dec 15 │ Open     │
│ 3 │ Update code review checklist        │ TL       │ Dec 17 │ Open     │
│ 4 │ No-Friday-deploy policy             │ DM       │ Dec 11 │ Done     │
│ 5 │ Fix connection leak in code         │ Senior   │ Dec 12 │ Done     │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ 8. LESSONS LEARNED                                                      │
│ ─────────────────────────────────────────────────────────────────────  │
│ 1. Error handling paths need same testing rigor as happy paths         │
│ 2. Connection pool monitoring is essential for database-heavy services │
│ 3. Friday deployments carry higher risk                                │
│ 4. Quick rollback capability saved significant impact                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Защита команды

### 7.1 Роль менеджера

**Менеджер как защитник:**
- Фильтрует необоснованное давление от клиента
- Отстаивает реалистичные сроки
- Не передаёт стресс команде
- Берёт ответственность на себя

### 7.2 Баланс защиты и accountability

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROTECTION vs ACCOUNTABILITY                         │
└─────────────────────────────────────────────────────────────────────────┘

  PROTECT TEAM FROM:                    HOLD TEAM ACCOUNTABLE FOR:
  ─────────────────────                 ─────────────────────────
  
  ✓ Unrealistic deadlines              ✓ Commitments they made
  ✓ Scope creep without resources      ✓ Quality of their work
  ✓ Toxic client behavior              ✓ Following processes
  ✓ Blame culture                      ✓ Professional behavior
  ✓ Constant overtime                  ✓ Communication
  ✓ Micromanagement                    ✓ Continuous improvement
```

### 7.3 Как защищать команду

**Правильно:**
```
Client: "Developer X made a mistake, we want them removed!"

DM Response:
"I understand your frustration with the situation. Let me take 
responsibility for our quality process that allowed this to happen. 
Here's what we're doing to prevent this:
[improvement plan]

Removing team members isn't something we do lightly, as it 
creates knowledge loss and transition costs. Let's give the 
improvement plan 2 weeks to show results. If issues persist, 
we can discuss further options."
```

**Неправильно:**
```
❌ "Да, согласен, X плохо работает, уберём его"
   (предаёт команду, не решает системную проблему)

❌ "Это не наша вина, клиент давал плохие требования"
   (перекладывает ответственность)

❌ "Команда, клиент очень зол на вас!"
   (передаёт стресс команде)
```

---

## 8. Предотвращение повторных инцидентов

### 8.1 Continual Improvement

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    INCIDENT → IMPROVEMENT CYCLE                         │
└─────────────────────────────────────────────────────────────────────────┘

        ┌───────────────┐
        │   INCIDENT    │
        │   OCCURS      │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │   RESOLVE     │─────────────────────────────┐
        │   (ASAP)      │                             │
        └───────┬───────┘                             │
                │                                      │
                ▼                                      ▼
        ┌───────────────┐                     ┌───────────────┐
        │     RCA       │                     │   PREVENT     │
        │  (find cause) │                     │   RECURRENCE  │
        └───────┬───────┘                     └───────────────┘
                │                                      ▲
                ▼                                      │
        ┌───────────────┐                             │
        │ ACTION ITEMS  │─────────────────────────────┘
        │ (implement    │
        │  fixes)       │
        └───────────────┘
```

### 8.2 Tracking Action Items

**Принципы:**
- Каждый action item имеет owner и due date
- Регулярный review (weekly)
- Escalation если не выполняется
- Close only when verified

**Metrics:**
- % action items completed on time
- Days to close action items
- Repeat incidents (same root cause)

---

## 💡 Key Takeaways

- **Risk = Likelihood × Impact** — приоритизируй риски количественно
- **Risk Register** — документируй, отслеживай, регулярно review
- **Early signals** — замедление коммуникации, микроменеджмент, формальный тон = warning signs
- **Escalate early** — лучше рано с планом, чем поздно с проблемой
- **RCA** — 5 Whys для поиска корневой причины, не симптомов
- **Blameless culture** — focus on системе, не на людях; "how", не "who"
- **Protect team** — фильтруй давление, не передавай стресс, бери ответственность

---

## 🚀 Next Steps

**Related Modules:**
- [08_Exam](../08_Exam/) — Финальный практический экзамен
- [02_ITSM](../02_ITSM/) — Процессы Incident/Problem Management

**Practice Ideas:**
1. Создайте Risk Register для текущего проекта
2. Проведите 5 Whys на последнем инциденте
3. Подготовьте RCA document template

**Going Deeper:**
- "The Field Guide to Understanding Human Error" by Sidney Dekker
- "Drift into Failure" by Sidney Dekker
- Google SRE Book — Postmortem Culture

---

## 📚 Additional Resources

**Книги:**
- "The Field Guide to Understanding Human Error" — понимание ошибок
- "Turn the Ship Around" by David Marquet — empowerment и ответственность

**Templates:**
- [Risk Register Template](../templates/risk_register.xlsx)
- [RCA Template](../templates/rca_template.md)
- [Escalation Template](../templates/escalation_email.md)

---


