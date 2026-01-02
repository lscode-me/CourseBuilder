# Engineering Strategy
## Стратегическое планирование и организационное развитие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь опыт управления несколькими командами
- Понимать основы предыдущих модулей курса
- Интересоваться стратегической работой в engineering

**Recommended prior modules:**

- [17_SeniorLeadership](../17_SeniorLeadership/) — senior leadership
- [12_ScalingTeams](../12_ScalingTeams/) — scaling teams

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Разрабатывать и артикулировать engineering strategy
- Связывать техническую работу с business goals
- Создавать roadmaps и планировать по quarters
- Принимать стратегические технические решения
- Измерять и коммуницировать прогресс

---

## 1. What is Engineering Strategy?

### 1.1 Definition

> **💡 Key Insight:**  
> Strategy — это не план. Strategy — это **набор интегрированных решений**, которые создают устойчивое конкурентное преимущество.

**Engineering Strategy отвечает на вопросы:**

| Вопрос | Что определяет |
|--------|----------------|
| **Куда идём?** | Vision, target state |
| **Почему туда?** | Connection to business goals |
| **Чем жертвуем?** | Trade-offs, что НЕ делаем |
| **Как узнаем, что дошли?** | Metrics, success criteria |
| **Как идём?** | Roadmap, milestones |

**Формула:**

```
Engineering Strategy = 
  Business Goals (what we're trying to achieve)
  + Technical Bets (how technology helps)
  + Organizational Model (how we work)
  + Trade-offs (what we're NOT doing)
```

### 1.2 Strategy vs Tactics

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   STRATEGY                              TACTICS                 │
│   ────────                              ───────                 │
│   "Win the war"                         "Win the battle"        │
│                                                                 │
│   • Why и What                          • How                   │
│   • Quarters и Years                    • Weeks и Months        │
│   • Irreversible/Expensive              • Reversible/Cheap      │
│   • Direction                           • Execution             │
│   • Trade-offs visible                  • Implementation        │
│                                                                 │
│   Examples:                             Examples:               │
│   "Migrate to microservices"            "Deploy service X"      │
│   "Build internal platform"             "Add feature Y"         │
│   "Invest in ML capabilities"           "Train model Z"         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Ключевой тест стратегичности:**

- Если решение легко отменить → это тактика
- Если решение меняет направление организации → это стратегия
- Если "а давайте сделаем и то, и другое" работает → это не стратегия (нет trade-off)

### 1.3 Components of Eng Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENGINEERING STRATEGY                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 1. VISION                                                 │  │
│  │    Where are we going? What does "done" look like?        │  │
│  │    Example: "Best-in-class developer platform by 2026"    │  │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 2. PRINCIPLES                                             │  │
│  │    How do we make decisions? What do we value?            │  │
│  │    Example: "Build for scale, buy commodities"            │  │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 3. INVESTMENTS                                            │  │
│  │    Where do we put resources? What bets are we making?    │  │
│  │    Example: "60% product, 25% platform, 15% innovation"   │  │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 4. ORGANIZATION                                           │  │
│  │    How do we structure teams? What capabilities need?     │  │
│  │    Example: "Stream-aligned teams + Platform team"        │  │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 5. ROADMAP                                                │  │
│  │    Sequence of work. When do we expect what?              │  │
│  │    Example: "Q1: Foundation, Q2: Migration, Q3: Scale"    │  │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.4 Пример: Engineering Strategy Statement

**Плохой пример:**

```
"Мы будем использовать современные технологии и best practices,
чтобы делать качественные продукты быстро."

Почему плохо:
- Нет конкретики (какие технологии?)
- Нет trade-offs (что мы НЕ делаем?)
- Нет измеримости (как узнаем успех?)
- Любая компания может сказать то же самое
```

**Хороший пример:**

```
Engineering Strategy 2025:

Vision: Стать платформенной компанией с 10x скоростью
delivery новых продуктов.

Core Bets:
1. Microservices architecture (вместо monolith evolution)
2. Internal Developer Platform (вместо self-service tools)
3. ML-first features (вместо rules-based)

Trade-offs we're making:
- Инвестируем в platform → меньше capacity на features в Q1-Q2
- Standardize на Kubernetes → отказываемся от serverless
- Hire senior → меньше headcount, выше планка

Success Metrics:
- Lead time: 2 weeks → 2 days
- Deployment frequency: weekly → daily
- New product launch: 6 months → 6 weeks
```

---

## 2. Connecting to Business

Engineering strategy не существует в вакууме — она должна **обслуживать бизнес**. Если ваша стратегия не connected к business goals, это просто wish list технических проектов.

### 2.1 Strategy Cascade

```
┌────────────────────────────────────────────────────────────────┐
│                      STRATEGY CASCADE                          │
└────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────┐
    │         COMPANY STRATEGY            │  "Стать #1 в рынке"
    │  Mission, Vision, 3-5 year plan     │
    └─────────────────┬───────────────────┘
                      │
    ┌─────────────────▼───────────────────┐
    │         BUSINESS GOALS              │  "Revenue $100M, 
    │  Revenue, Growth, Efficiency        │   Growth 50% YoY"
    └─────────────────┬───────────────────┘
                      │
    ┌─────────────────▼───────────────────┐
    │        PRODUCT STRATEGY             │  "Expand to Enterprise,
    │  What to build, for whom            │   Launch Mobile app"
    └─────────────────┬───────────────────┘
                      │
    ┌─────────────────▼───────────────────┐
    │       ENGINEERING STRATEGY          │  "Platform for speed,
    │  How to build, architecture, org    │   SOC2, Scale infra 3x"
    └─────────────────┬───────────────────┘
                      │
    ┌─────────────────▼───────────────────┐
    │          TEAM PLANS                 │  "Team A: Auth, Team B:
    │  Who builds what, when              │   Mobile, Team C: Infra"
    └─────────────────────────────────────┘
```

### 2.2 Understanding Business Goals

**Вопросы для понимания бизнес-контекста:**

| Категория | Вопросы | Почему важно |
|-----------|---------|--------------|
| **Priorities** | Какие топ-3 приоритета компании на год? | Alignment eng работы |
| **Metrics** | Какие метрики определяют успех? | Что оптимизируем |
| **Growth** | Какой план роста? | Capacity planning |
| **Competition** | Кто конкуренты? Чем побеждаем? | Where to invest |
| **Risks** | Какие главные риски бизнеса? | What to protect |
| **Bets** | Какие ставки делает компания? | Where to innovate |

**Как получить эту информацию:**

```
1. Company all-hands и strategy presentations
2. 1-on-1 с вашим руководителем
3. Разговоры с Product leadership
4. Board presentations (если доступны)
5. Investor communications (если публичная компания)
6. Прямой вопрос CEO/leadership
```

### 2.3 Translating Business to Engineering

**Пример перевода:**

| Business Goal | Engineering Questions | Engineering Strategy |
|---------------|----------------------|---------------------|
| **Revenue +50%** | Выдержит ли система нагрузку? Что блокирует sales? | Scale infra 2x, Improve reliability to 99.9% |
| **Launch Enterprise** | Что нужно для enterprise? Security, compliance? | SOC2 certification, SSO, Audit logs |
| **Faster time-to-market** | Что замедляет delivery? | Platform investment, CI/CD improvement |
| **Expand internationally** | Localization? Data residency? Latency? | Multi-region, i18n framework |
| **Cost reduction** | Где inefficiencies? | Infra optimization, automation |

### 2.4 Детальный пример: From Business to Engineering

**Ситуация:**

```
Company: B2B SaaS product
Business Goal: Grow from $10M to $25M ARR in 2 years
Strategy: Expand to Enterprise customers
```

**Шаг 1: Понять что нужно Enterprise**

| Enterprise Need | Current State | Gap |
|-----------------|---------------|-----|
| Security (SOC2) | ❌ No certification | Major investment |
| SSO/SAML | ❌ Only username/password | Build or buy |
| Audit Logs | ❌ None | Build |
| 99.9% SLA | 99.5% actual | Reliability work |
| Custom deployment | ❌ Multi-tenant only | Architecture decision |

**Шаг 2: Quantify engineering investment**

```
SOC2 Certification:
- Eng work: 3 months, 2 engineers
- External audit: $50K
- Ongoing: 0.5 engineer

SSO/SAML:
- Option A (Build): 2 months, 2 engineers
- Option B (Buy Auth0): $30K/year, 2 weeks integration
- Recommendation: Buy (not core competency)

Reliability to 99.9%:
- Current: 43 hours downtime/year
- Target: 8.7 hours/year
- Investment: 2 engineers for 6 months + ongoing SRE
```

**Шаг 3: Engineering Strategy for Enterprise**

```markdown
## Engineering Strategy: Enterprise Readiness

### Business Context

Expand from SMB to Enterprise to reach $25M ARR.
Enterprise requires: SOC2, SSO, SLA guarantees.

### Strategic Priorities (in order)

1. Security & Compliance (SOC2) — gate for enterprise deals
2. SSO Integration — top requested feature
3. Reliability improvements — SLA commitments

### Investment

- Q1-Q2: 40% capacity on Enterprise readiness
- Q3-Q4: 20% (maintenance + new compliance needs)

### Trade-offs

- ❌ Fewer new features for SMB in H1
- ❌ Delay mobile app by 6 months
- ✅ Enterprise deals unlock 5x ACV

### Success Metrics

- SOC2 Type 2 by Q2
- SSO live by end of Q1
- 99.9% uptime from Q3
- 3 Enterprise deals closed with new capabilities
```

---

## 3. Strategic Decision Making

Стратегические решения отличаются от тактических тем, что они **дорого стоят если ошибиться**. Поэтому нужны frameworks для структурированного принятия решений.

### 3.1 Framework: Build vs Buy vs Partner

**Матрица принятия решения:**

| Фактор | Build | Buy | Partner |
|--------|-------|-----|---------|
| **Core competency?** | ✅ Да, build | ❌ Нет | Depends |
| **Commodity?** | ❌ Нет | ✅ Да, buy | ✅ Да |
| **Time critical?** | ❌ Медленно | ✅ Быстро | ✅ Быстро |
| **Long-term cost** | Variable | Predictable | Shared |
| **Control needed** | ✅ Полный | ❌ Limited | Partial |
| **Expertise available?** | ✅ Нужна | ❌ Не нужна | Partial |

**Decision Tree:**

```
                    Это core competency?
                    /              \
                  Yes               No
                   |                 |
              Есть время?      Commodity?
              /        \        /       \
            Yes        No     Yes        No
             |          |       |          |
          BUILD    Consider    BUY     PARTNER
                     BUY
```

**Пример: Authentication System**

```
Question: Build custom auth или использовать Auth0?

Analysis:
- Core competency? No (мы не auth company)
- Commodity? Yes (стандартная проблема)
- Time critical? Yes (нужно SSO для enterprise deal)
- Long-term cost: Auth0 $30K/year vs Build $200K + maintenance
- Control: Auth0 достаточно flexible

Decision: BUY (Auth0)

Trade-off: Vendor dependency, но saves 6 months и ongoing work
```

### 3.2 Technical Debt: Strategic Framework

**Типы технического долга:**

| Тип | Описание | Пример | Приоритет |
|-----|----------|--------|-----------|
| **Deliberate-prudent** | Знаем, что debt, осознанно взяли | "Ship now, refactor later" | Low (planned) |
| **Deliberate-reckless** | Знаем лучший путь, игнорируем | "Нет времени на design" | High (risky) |
| **Inadvertent-prudent** | Узнали лучший путь после | "Теперь понимаем лучше" | Medium |
| **Inadvertent-reckless** | Не знали что делаем плохо | "Juniors без review" | High (risky) |

**Tech Debt Decision Matrix:**

| Когда ПЛАТИТЬ | Когда ПРИНЯТЬ |
|---------------|---------------|
| Блокирует feature development | One-time feature |
| Вызывает reliability issues | Short-lived system |
| Замедляет velocity significantly | Speed важнее quality сейчас |
| Создаёт security risks | Система будет заменена |
| Отталкивает engineers | Isolated, contained area |
| Растёт exponentially | Stable, not growing |

**Tech Debt Prioritization:**

```
Tech Debt Score = Impact × Frequency × Effort_Ratio

Impact: 1-5 (how much it hurts when triggered)
Frequency: 1-5 (how often triggered)
Effort_Ratio: 1-5 (5 = easy to fix, 1 = hard)

Priority order: highest score first
```

**Пример Tech Debt Backlog:**

| Debt Item | Impact | Freq | Effort | Score | Priority |
|-----------|--------|------|--------|-------|----------|
| Legacy auth module | 5 | 4 | 2 | 40 | P1 |
| Old API versioning | 3 | 3 | 4 | 36 | P2 |
| Inconsistent logging | 2 | 5 | 5 | 50 | P1 |
| Manual deployments | 4 | 3 | 3 | 36 | P2 |

### 3.3 Platform vs Product Investment

**Когда инвестировать в Platform:**

```
Platform ROI = (Time_Saved × Num_Teams × Duration) - Build_Cost

Example:
- 2 weeks saved per team
- 5 teams would use it
- Used for 2 years (8 quarters)
- Build cost: 3 months, 2 engineers

ROI = (2 weeks × 5 teams × 8 quarters) - (3 months × 2 engineers)
    = 80 team-weeks saved - 6 engineer-months invested
    = Strong positive ROI after 6 months
```

**Platform Readiness Checklist:**

| Criteria | Ready | Not Ready |
|----------|-------|-----------|
| Multiple teams need it | ✅ 3+ teams | ❌ Only 1 team |
| Problem well-understood | ✅ Solved 2+ times | ❌ First time solving |
| Clear interface | ✅ Can define API | ❌ Fuzzy requirements |
| Team to own it | ✅ Dedicated team | ❌ "Everyone's job" |
| Customers willing | ✅ Committed users | ❌ "Maybe we'll use" |

### 3.4 Architecture Decision Records (ADR)

**Формат ADR:**

```markdown
# ADR-001: Use PostgreSQL as Primary Database

## Status

Accepted (2024-01-15)

## Context

We need to choose a primary database for our new service.
Requirements: ACID transactions, JSON support, scaling to 1M records.

## Decision

We will use PostgreSQL 15.

## Alternatives Considered

### MySQL 8

- Pros: Team familiarity, performance
- Cons: Weaker JSON support, licensing concerns

### MongoDB

- Pros: Flexible schema, JSON native
- Cons: No ACID transactions across documents

## Consequences

### Positive

- Strong consistency guarantees
- Excellent JSON support (JSONB)
- Rich ecosystem, good tooling
- Team can leverage existing knowledge

### Negative

- Need to manage schema migrations
- Horizontal scaling more complex than MongoDB
- Some team members need training

## Trade-offs

We're choosing consistency and reliability over schema flexibility.
This aligns with our principle "data integrity first."
```

### 3.5 Strategic Decision Checklist

Перед принятием стратегического решения:

```
□ Понимаю ли я ЗАЧЕМ это нужно бизнесу?
□ Рассмотрел ли я альтернативы? (минимум 2-3)
□ Записал ли я trade-offs?
□ Кого затрагивает это решение?
□ Обсудил ли я с affected parties?
□ Какой worst case? Survivable?
□ Можно ли откатить если ошибусь?
□ Как измерю успех?
□ Когда пересмотрю решение?
```

---

## 4. Planning Cycles

Стратегия без planning cycles остаётся документом на полке. Нужны **ритмы** для review, adjustment и execution.

### 4.1 Planning Rhythm Overview

```
┌────────────────────────────────────────────────────────────────┐
│                    PLANNING RHYTHM                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ANNUAL (Q4 для следующего года)                               │
│  ├── Strategy review и update                                  │
│  ├── Headcount planning                                        │
│  ├── Budget allocation                                         │
│  └── Major milestones                                          │
│                                                                │
│  QUARTERLY (6 weeks before)                                    │
│  ├── Roadmap commitments                                       │
│  ├── Capacity planning                                         │
│  ├── Dependencies mapping                                      │
│  └── OKRs/Goals setting                                        │
│                                                                │
│  MONTHLY                                                       │
│  ├── Progress review                                           │
│  ├── Risk assessment                                           │
│  └── Adjustments                                               │
│                                                                │
│  WEEKLY                                                        │
│  ├── Execution tracking                                        │
│  ├── Blocker resolution                                        │
│  └── Team syncs                                                │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 4.2 Annual Planning Deep Dive

**Timeline:**

| When | What | Who | Output |
|------|------|-----|--------|
| Early Q4 | Business context briefing | CEO/Leadership → Eng | Understanding of next year priorities |
| Mid Q4 | Eng strategy draft | Eng Leadership | Strategy document v1 |
| Mid Q4 | Headcount asks | Directors → VP | Headcount requests with justification |
| Late Q4 | Budget negotiation | VP ↔ Finance/CEO | Approved headcount and budget |
| End Q4 | Communicate plan | VP → Org | All-hands, team meetings |

**Annual Planning Template:**

```markdown
# Engineering Plan 2025

## 1. Business Context

- Company goals for 2025
- Key metrics and targets
- Major product initiatives

## 2. Engineering Strategy Recap

- Vision (unchanged or updated?)
- Principles
- Key bets for 2025

## 3. Investment Allocation

| Area | % of Capacity | Key Projects |
|------|---------------|--------------|
| Product | 60% | Feature A, B, C |
| Platform | 25% | Developer Platform, CI/CD |
| Innovation | 10% | ML exploration, new tech |
| Buffer | 5% | Unplanned, support |

## 4. Headcount Plan

| Team | Current | EOY Target | Key Hires |
|------|---------|------------|-----------|
| Product A | 8 | 12 | 2 Sr, 2 Mid |
| Platform | 4 | 6 | 1 Staff, 1 Sr |
| ... | ... | ... | ... |
| Total | 45 | 60 | +15 |

## 5. Major Milestones

| Quarter | Milestone | Owner |
|---------|-----------|-------|
| Q1 | Platform v1 launch | Team X |
| Q2 | SOC2 certification | Security |
| Q3 | Mobile app beta | Mobile team |
| Q4 | International launch | All |

## 6. Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Hiring slower | High | High | Early start, multiple channels |
| Platform delay | Medium | High | Phased approach |
```

### 4.3 Quarterly Planning Deep Dive

**Quarterly Planning Process:**

```
T-6 weeks: PREPARATION
├── Review roadmap status
├── Gather inputs from Product, stakeholders
├── Assess capacity (headcount, skills)
└── Identify dependencies

T-4 weeks: PLANNING
├── Teams draft proposals
├── Cross-team dependency mapping
├── Leadership review и prioritization
└── Trade-off decisions

T-2 weeks: FINALIZATION
├── Commitments locked
├── OKRs finalized
├── Communication to org
└── Kick-off planning

T-0: QUARTER START
├── Sprint planning
└── Execution begins
```

**Capacity Planning Formula:**

```
Available Capacity = 
  (Engineers × Working Days × Focus Factor)
  - Vacations
  - On-call rotation
  - Meetings overhead
  - Buffer for unplanned

Example:
- 5 engineers × 65 days × 0.7 focus = 227.5 eng-days
- Vacations: 25 days
- On-call: 10 days
- Buffer: 20 days
= 172.5 eng-days available for planned work

Convert to story points or project estimates accordingly.
```

### 4.4 Roadmap Best Practices

**Good Roadmap Characteristics:**

| Characteristic | Why | How |
|----------------|-----|-----|
| **Tied to goals** | Avoid random work | Every item links to OKR/goal |
| **Realistic** | Build trust | Use historical velocity |
| **Has slack** | Handle surprises | 20-30% buffer |
| **Dependencies clear** | Avoid blockers | Map cross-team needs |
| **Living document** | Stay relevant | Update monthly |
| **Visible rationale** | Enable decisions | Include "why" for items |

**Roadmap Anti-patterns:**

| Anti-pattern | Symptom | Fix |
|--------------|---------|-----|
| **Everything P0** | No prioritization | Force rank ruthlessly |
| **No slack** | Always behind | Build in buffer |
| **Never updated** | Irrelevant | Monthly reviews |
| **Wishful thinking** | Constant misses | Use data for estimates |
| **No rationale** | Random-looking | Add "why" column |

**Roadmap Format Example:**

```markdown
# Q2 2025 Roadmap: Platform Team

## Theme: Enable 10x deployment frequency

### Committed (80% confidence)

| Project | Owner | Target | Business Value |
|---------|-------|--------|----------------|
| CI/CD Pipeline v2 | Алексей | Mid-Q2 | 5x faster builds |
| Feature Flags | Мария | End-Q2 | Safe rollouts |

### Stretch (50% confidence)

| Project | Owner | Target | Business Value |
|---------|-------|--------|----------------|
| Auto-scaling | TBD | Q2 | Cost optimization |

### Not This Quarter

| Request | Reason |
|---------|--------|
| Kubernetes upgrade | Deferred to Q3, lower priority |
| New monitoring | Waiting for vendor decision |

## Dependencies

| From Team | We Need | By When | Status |
|-----------|---------|---------|--------|
| Security | SSO integration | April 15 | On track |
| Product A | API specs | March 30 | At risk |

## Risks

| Risk | Mitigation |
|------|------------|
| Key person vacation | Cross-train by March |
| Vendor delay | Parallel POC with alternative |
```

---

## 5. Resource Allocation

Стратегия — это про выбор. Resource allocation — это **конкретизация выбора** в людях и деньгах.

### 5.1 Portfolio Allocation Framework

**Три модели allocation:**

**Model A: Balanced (typical for growth company)**

```
┌─────────────────────────────────────────────────────────┐
│  PRODUCT/FEATURES         │ 55-65%                      │
│  ─────────────────────────┼──────────────────────────── │
│  New features, improvements, customer requests          │
├─────────────────────────────────────────────────────────┤
│  PLATFORM/INFRA           │ 20-25%                      │
│  ─────────────────────────┼──────────────────────────── │
│  Tech debt, infrastructure, developer experience        │
├─────────────────────────────────────────────────────────┤
│  INNOVATION               │ 5-10%                       │
│  ─────────────────────────┼──────────────────────────── │
│  Experiments, new technologies, R&D                     │
├─────────────────────────────────────────────────────────┤
│  BUFFER                   │ 10-15%                      │
│  ─────────────────────────┼──────────────────────────── │
│  Unplanned, support, oncall, bugs                       │
└─────────────────────────────────────────────────────────┘
```

**Model B: Speed mode (startup / aggressive growth)**

```
Product: 75%, Platform: 15%, Innovation: 5%, Buffer: 5%
Trade-off: Tech debt accumulates, fast now, pay later
```

**Model C: Scale mode (post product-market fit)**

```
Product: 50%, Platform: 35%, Innovation: 10%, Buffer: 5%
Trade-off: Slower features, investing in sustainable speed
```

**Как выбрать модель:**

| Situation | Recommended Model |
|-----------|-------------------|
| Pre-PMF startup | B (Speed) |
| Post-PMF growth | A (Balanced) |
| Scaling challenges | C (Scale) |
| Reliability crisis | 60%+ on Platform |
| New market entry | 80%+ on Product |

### 5.2 Headcount Planning

**Comprehensive Headcount Formula:**

```
Target Headcount = 
    Current Sustainable Work
  + New Initiatives
  + Growth Buffer (usually 10-20%)
  - Efficiency Gains (automation, tools)
  + Attrition Replacement (attrition rate × headcount)
  + Hiring Lead Time Buffer
```

**Пример расчёта:**

```
Current team: 20 engineers
Attrition rate: 15%

Calculation:
├── Current work requires:        20 engineers
├── New product line:             +4 engineers
├── Enterprise features:          +2 engineers
├── 15% attrition replacement:    +3 engineers
├── 10% growth buffer:            +2 engineers
├── Automation efficiency:        -1 engineer
└── Target EOY:                   30 engineers

Hiring plan: +10 engineers (50% growth)
Timeline: Start hiring Q1 to have team by Q3
```

**Headcount Justification Template:**

```markdown
## Headcount Request: +4 Engineers for Platform Team

### Current State

- Team: 4 engineers
- Coverage: CI/CD, Monitoring, Infrastructure
- Current capacity: 100% utilized, no slack

### Request

+2 Senior Engineers, +2 Mid-level Engineers

### Business Justification

| Initiative | Engineers Needed | Business Impact |
|------------|-----------------|-----------------|
| Developer Platform | 2 | 30% faster onboarding |
| Reliability (99.9%) | 1 | Enable Enterprise SLA |
| Tech debt reduction | 1 | 20% velocity improvement |

### ROI

- Investment: ~$600K/year (fully loaded)
- Return: 20% velocity × 20 engineers = 4 engineer-years saved
- Payback: < 1 year

### Alternatives Considered

- Contractors: Higher cost, knowledge loss
- No hire: Continued tech debt, SLA risk
- Offshore: Timezone challenges for platform work
```

### 5.3 Investment Decision Framework

**Portfolio Review Questions:**

| Question | Low Score → | High Score → |
|----------|-------------|--------------|
| Business impact? | Reduce | Invest |
| Strategic importance? | Reduce | Invest |
| Current bottleneck? | Reduce | Invest |
| Team stretched? | OK | Invest |
| Growth area? | Reduce | Invest |
| Mature/stable? | Reduce | Maintain |
| Declining? | Reduce/Sunset | — |

**Team Investment Matrix:**

```
              HIGH BUSINESS IMPACT
                      │
         INVEST       │      INVEST MORE
         (grow 10-20%)│      (grow 30%+)
                      │
    ──────────────────┼──────────────────
                      │
         MAINTAIN     │      INVEST
         (flat)       │      (grow 10-20%)
                      │
              LOW BUSINESS IMPACT

    LOW TEAM HEALTH ────────────── HIGH TEAM HEALTH
```

**Пример Investment Decisions:**

| Team | Business Impact | Team Health | Decision |
|------|-----------------|-------------|----------|
| Product A | High (core revenue) | Stretched | INVEST +3 |
| Product B | Medium (growing) | Healthy | MAINTAIN |
| Legacy | Low (declining) | OK | REDUCE -1 |
| Platform | High (enables all) | Stretched | INVEST +2 |
| Experiment | TBD | New | MONITOR |

---

## 6. Technical Strategy

Technical strategy — это **architecture и technology decisions** на горизонте 2-5 лет. Это не список технологий, а направление движения.

### 6.1 Architecture Strategy Framework

**Шаг 1: Assess Current State**

| Dimension | Questions | How to Assess |
|-----------|-----------|---------------|
| **Scalability** | Какой текущий headroom? Bottlenecks? | Load testing, capacity analysis |
| **Reliability** | Uptime? MTTR? Incident frequency? | Metrics, postmortems |
| **Velocity** | Lead time? Deploy frequency? | DORA metrics |
| **Maintainability** | Tech debt level? Cognitive load? | Developer survey, code metrics |
| **Security** | Known vulnerabilities? Compliance? | Security audits |

**Шаг 2: Define Target State**

```
Example Target Architecture Statement:

"By end of 2026, we will have:
- Microservices architecture with clear domain boundaries
- 99.95% availability (currently 99.5%)
- Daily deployments (currently weekly)
- Self-service developer platform
- Zero-trust security model"
```

**Шаг 3: Migration Path**

```
Current State          Transition              Target State
─────────────────────────────────────────────────────────────
   Monolith      →    Modular Monolith    →    Microservices
   Manual ops    →    CI/CD + IaC         →    Platform/Self-serve
   Shared DB     →    DB per module       →    DB per service
   On-prem       →    Hybrid              →    Cloud-native
```

### 6.2 Technology Radar

**Technology Radar** — инструмент для категоризации технологий:

```
┌─────────────────────────────────────────────────────────────┐
│                    TECHNOLOGY RADAR                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ADOPT                          TRIAL                       │
│  ─────                          ─────                       │
│  Use in production              Try in projects             │
│  • Kubernetes                   • Rust                      │
│  • PostgreSQL                   • GraphQL                   │
│  • React                        • Temporal                  │
│  • Go                           • Feature Flags             │
│                                                             │
│  ASSESS                         HOLD                        │
│  ─────                          ─────                       │
│  Evaluate, POC                  Don't start new             │
│  • WebAssembly                  • MongoDB (for OLTP)        │
│  • Deno                         • PHP                       │
│  • HTMX                         • Angular                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Как использовать:**

| Ring | Meaning | Actions |
|------|---------|---------|
| **ADOPT** | Standard, use widely | Use in new projects, migrate to |
| **TRIAL** | Promising, test in real projects | Limited production use |
| **ASSESS** | Interesting, worth POC | Explore, learn, evaluate |
| **HOLD** | Don't use for new work | Maintain only, plan migration |

### 6.3 Technology Choice Framework

**"Boring Technology" Principle (Dan McKinley):**

> Every company has a limited number of "innovation tokens".  
> Spend them wisely on things that differentiate you.

| Type | Choice | Rationale |
|------|--------|-----------|
| **Core systems** | Boring, proven | Risk minimization |
| **Differentiating** | Best for problem | Competitive advantage |
| **Experiments** | New, promising | Learning, future-proofing |

**Technology Evaluation Criteria:**

| Criterion | Weight | How to Evaluate |
|-----------|--------|-----------------|
| Team expertise | High | Do we know it? Can we hire for it? |
| Community & support | High | Active? Documentation? |
| Long-term viability | Medium | Company stability? Adoption trend? |
| Integration | Medium | Works with our stack? |
| Total Cost of Ownership | High | License + infra + people + migration |
| Performance fit | Medium | Meets our requirements? |

### 6.4 Technical Principles

Technical principles — это **decision-making shortcuts** для команд.

**Как формулировать принципы:**

```
Формула: [Action] + [Rationale]

Example:
"Build for 10x scale" → "потому что re-architecting under load дорого"
"API-first design" → "потому что это enables независимые команды"
```

**Пример набора принципов:**

| # | Principle | Rationale | Implications |
|---|-----------|-----------|--------------|
| 1 | **Own our data** | Data = core asset | No vendor lock-in for data, export capability |
| 2 | **Build for 10x** | Avoid emergency scaling | Design decisions consider growth |
| 3 | **Automate everything** | Manual = error-prone | Invest in CI/CD, IaC, testing |
| 4 | **Security by default** | Bolt-on security fails | Security review in design phase |
| 5 | **Measure to manage** | Can't improve what you can't measure | Observability from day 1 |
| 6 | **Embrace failure** | Failures happen | Design for resilience, blameless postmortems |
| 7 | **Boring technology for core** | Innovation budget is limited | New tech only where it differentiates |

**Как использовать принципы:**

```
Team: "Мы хотим использовать новую database X для core service"

Check against principles:
- Principle 1 (Own our data): ✅ Open source
- Principle 5 (Measure): ⚠️ Limited observability tools
- Principle 7 (Boring for core): ❌ New tech for core system

Decision: No. Use for non-core experiments first.
```

---

## 7. Measuring Progress

Стратегия без metrics — это hope. Metrics без context — это noise. Нужен **balanced set of metrics** tied to strategy.

### 7.1 DORA Metrics Deep Dive

**DORA (DevOps Research and Assessment)** — наиболее validated метрики эффективности engineering:

| Metric | Definition | Elite | High | Medium | Low |
|--------|------------|-------|------|--------|-----|
| **Deployment Frequency** | How often deploy | On-demand (multiple/day) | Weekly-monthly | Monthly-quarterly | < quarterly |
| **Lead Time** | Commit → Production | < 1 hour | 1 day-1 week | 1-6 months | > 6 months |
| **Change Failure Rate** | % deploys causing failure | 0-15% | 16-30% | 16-30% | > 45% |
| **MTTR** | Time to restore | < 1 hour | < 1 day | 1 day-1 week | > 1 week |

**Как измерять:**

```
Deployment Frequency:
- Source: CI/CD system (Jenkins, GitHub Actions, etc.)
- Query: COUNT(deployments) / time period

Lead Time:
- Source: Git + CI/CD
- Calculate: Merge_time - First_commit_time

Change Failure Rate:
- Source: Incident system + deployment logs
- Calculate: Rollbacks / Total_deployments

MTTR:
- Source: Incident management system
- Calculate: Mean(Resolution_time - Detection_time)
```

### 7.2 Comprehensive Metrics Framework

**Balanced Scorecard for Engineering:**

```
┌────────────────────────────────────────────────────────────────┐
│                 ENGINEERING METRICS DASHBOARD                  │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  DELIVERY (speed)                 QUALITY (reliability)        │
│  ─────────────────                ───────────────────          │
│  • Deployment frequency           • Uptime / SLA               │
│  • Lead time for changes          • Incident rate (P1/P2)      │
│  • Cycle time                     • Change failure rate        │
│  • Velocity trend                 • Bug escape rate            │
│                                                                │
│  PRODUCTIVITY (efficiency)        HEALTH (sustainability)      │
│  ──────────────────────           ────────────────────         │
│  • Developer satisfaction         • Attrition rate             │
│  • Build/test times               • Engagement score           │
│  • Code review turnaround         • On-call burden             │
│  • Toil percentage                • Tech debt ratio            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Metrics by Audience:**

| Audience | Metrics They Care About |
|----------|------------------------|
| **Board/CEO** | Delivery velocity, uptime, cost efficiency |
| **Product** | Lead time, capacity, roadmap progress |
| **Engineering** | DORA metrics, developer experience, tech debt |
| **Finance** | Cost per transaction, infra spend, headcount efficiency |

### 7.3 OKRs for Engineering

**OKR Structure:**

```
Objective: Qualitative, inspiring goal
Key Results: 3-5 quantitative measures of success
Initiatives: Projects/work that drive Key Results
```

**Example OKRs by Strategic Area:**

**Objective: Enable 10x deployment speed**

```
KR1: Reduce lead time from 5 days to 1 day
KR2: Increase deployment frequency from weekly to daily
KR3: Reduce build time from 30 min to 5 min
KR4: Achieve 95% developer satisfaction with CI/CD

Initiatives:
- CI/CD pipeline overhaul
- Feature flags implementation
- Parallel test execution
```

**Objective: Achieve enterprise-grade reliability**

```
KR1: Improve uptime from 99.5% to 99.9%
KR2: Reduce P1 incidents from 5/month to 1/month
KR3: Reduce MTTR from 4 hours to 30 minutes
KR4: Complete SOC2 Type 2 certification

Initiatives:
- Chaos engineering program
- Improved monitoring & alerting
- Incident response training
```

**Objective: Build high-performing engineering culture**

```
KR1: Improve developer NPS from +20 to +40
KR2: Reduce voluntary attrition from 15% to 10%
KR3: 100% of engineers have development plans
KR4: Reduce toil from 30% to 15% of time

Initiatives:
- Developer experience improvements
- Career framework rollout
- Automation of toil tasks
```

### 7.4 Avoiding Metrics Pitfalls

**Common Mistakes:**

| Mistake | Problem | Better Approach |
|---------|---------|-----------------|
| **Vanity metrics** | Look good, no insight | Focus on actionable metrics |
| **Too many metrics** | No focus, confusion | 3-5 key metrics per area |
| **Measuring individuals** | Gaming, competition | Team-level metrics |
| **Ignoring leading indicators** | React too late | Balance leading/lagging |
| **No context** | Numbers without meaning | Always include trend, target |

**Goodhart's Law:**

> "When a measure becomes a target, it ceases to be a good measure."

**Mitigation:**

- Use multiple metrics together (balanced scorecard)
- Qualitative checks alongside quantitative
- Regularly reassess if metrics still useful
- Focus on outcomes, not just outputs

### 7.5 Communicating Progress

**Executive Update Template:**

```markdown
## Engineering Update - Q2 2025

### TL;DR

On track for annual goals. Platform migration 70% complete.
One risk: Enterprise timeline may slip 3 weeks.

### Key Metrics vs Targets

| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Deployment frequency | 10/day | 8/day | ↑ |
| Lead time | 1 day | 2 days | → |
| Uptime | 99.9% | 99.85% | ↑ |
| Developer NPS | +40 | +35 | ↑ |

### Strategic Initiatives Status

| Initiative | Status | Notes |
|------------|--------|-------|
| Platform Migration | 🟢 On track | 70% complete |
| SOC2 Certification | 🟢 On track | Audit scheduled Q3 |
| Mobile App | 🟡 At risk | 3-week delay, scope reduction option |

### Decisions Needed

1. Mobile app: Accept 3-week delay or reduce scope?
2. Q3 hiring: Approve +3 headcount for platform team?
```

**Team Communication:**

```
1. WHY: Connect to business goals and strategy
2. WHAT: Current progress and upcoming work
3. HOW: How we measure success
4. WINS: Celebrate achievements
5. CHALLENGES: Be honest about difficulties
```

---

## 8. Managing Change

### 8.1 Strategic Initiatives

**Types:**
```
- Technology migrations
- Platform builds
- Org restructures
- Process changes
- Culture shifts
```

### 8.2 Change Management

```
1. Create urgency — why now?
2. Build coalition — key supporters
3. Communicate vision — clear picture
4. Remove obstacles — unblock teams
5. Generate wins — show progress
6. Consolidate — don't declare victory early
7. Anchor in culture — make it stick
```

### 8.3 Common Pitfalls

```
❌ Top-down mandates without buy-in
❌ Changing everything at once
❌ No clear success metrics
❌ Underestimating resistance
❌ Moving on before change sticks
```

---

## 9. Strategic Communication

### 9.1 Engineering Narrative

```
Your narrative explains:

- Where engineering is going
- Why these choices
- What it enables
- How we'll get there
```

### 9.2 Stakeholder Communication

**Different audiences:**
```
Board/Executives:

- Business impact
- ROI of investments
- Risks and mitigations

Product:

- What's possible when
- Trade-offs of choices
- Capacity and velocity

Engineering:

- Technical direction
- Career opportunities
- Why decisions were made
```

### 9.3 Building Alignment

```
1. Share context broadly
2. Involve people in planning
3. Explain the "why"
4. Listen to feedback
5. Adjust when wrong
6. Follow through
```

---

## 10. Organizational Development

### 10.1 Team Topology

**Types:**
```
- Stream-aligned teams (features)
- Platform teams (infrastructure)
- Enabling teams (help others)
- Complicated subsystem teams (specialists)
```

### 10.2 Evolution Patterns

```
Early stage:

- Generalist teams
- Less specialization
- Move fast, break things

Growth stage:

- Some specialization
- Platform investment
- Process introduction

Scale stage:

- Specialized teams
- Mature platforms
- Efficient processes
```

### 10.3 Culture Development

```
Engineering culture includes:

- How we make decisions
- How we handle failure
- How we share knowledge
- How we treat each other
- How we grow people
```

---

## 11. Strategy Antipatterns

### 11.1 Common Mistakes

```
❌ Strategy that's not connected to business
❌ Too many priorities (everything is important)
❌ No clear trade-offs
❌ Strategy that never changes
❌ Strategy nobody knows about
❌ All strategy, no execution
```

### 11.2 Signs of Good Strategy

```
✓ Clear choices were made
✓ Trade-offs are explicit
✓ People can explain it
✓ Decisions align with it
✓ It evolved based on learning
✓ Results are tracked
```

---

## 12. Practical Strategy Process

### 12.1 Creating Strategy

```
1. Understand business context
2. Assess current state
3. Identify gaps and opportunities
4. Define principles and priorities
5. Create roadmap
6. Communicate broadly
7. Execute and adapt
```

### 12.2 Strategy Document Outline

```markdown
# Engineering Strategy FY25

## Executive Summary

Key points in 1 page

## Business Context

What business is trying to achieve

## Current State

Where engineering is today

## Strategic Priorities

Top 3-5 focus areas

## Investment Plan

Where resources go

## Roadmap

Major milestones by quarter

## Success Metrics

How we measure progress

## Risks and Mitigations

What could go wrong
```

### 12.3 Keeping Strategy Alive

```
- Quarterly reviews and updates
- Reference in planning decisions
- Celebrate aligned wins
- Learn from misses
- Adjust as business changes
```

---

## 💡 Key Takeaways

- **Strategy ≠ Plan:** Strategy — это интегрированные решения с trade-offs, не wish list проектов

- **Business-first:** Каждый элемент strategy должен connect к business goal. Нет connection = не strategy

- **Trade-offs visible:** Настоящая strategy говорит что вы НЕ делаете. Если "делаем всё" — это не strategy

- **Build vs Buy:** Core competency → Build. Commodity → Buy. Time-critical → Buy. Используйте framework

- **Technical Principles:** Создайте 5-7 принципов как decision-making shortcuts для команд

- **DORA metrics:** Deploy frequency, Lead time, Change failure rate, MTTR — validated метрики эффективности

- **Portfolio thinking:** Balanced allocation: 60% Product, 25% Platform, 10% Innovation, 5% Buffer

- **Living document:** Strategy review quarterly, update based on learning

- **Communicate broadly:** Strategy, которую никто не знает, не работает

---

## 🚀 Next Steps

**Related Modules:**

- [17_SeniorLeadership](../17_SeniorLeadership/) — leadership skills for strategy execution
- [12_ScalingTeams](../12_ScalingTeams/) — org design foundations

**Practice Ideas:**

1. **Strategy assessment:** Напишите текущую strategy в формате из секции 1.4
2. **DORA baseline:** Измерьте текущие DORA metrics для вашей организации
3. **Tech radar:** Создайте technology radar для вашей организации
4. **Principles draft:** Сформулируйте 5-7 технических принципов
5. **Portfolio analysis:** Посчитайте текущее allocation и сравните с target
6. **OKR review:** Проверьте, connected ли ваши OKRs к business goals

**Going Deeper:**

- Strategic planning workshops
- Architecture decision records (ADR) practice
- DORA metrics implementation
- OKR coaching

---

## 📚 Additional Resources

**Books:**

- "Good Strategy Bad Strategy" by Richard Rumelt — главная книга по стратегии
- "The Art of Action" by Stephen Bungay — strategy execution
- "An Elegant Puzzle" by Will Larson — systems for engineering management
- "Staff Engineer" by Will Larson — technical strategy на IC track
- "Accelerate" by Nicole Forsgren — DORA metrics research
- "Team Topologies" by Matthew Skelton — organization design

**Frameworks:**

- DORA metrics for engineering performance
- Team Topologies for organization design
- OKRs for goal setting
- ADRs (Architecture Decision Records) for technical decisions
- Technology Radar for technology choices

**Articles:**

- [Irrational Exuberance](https://lethain.com/) by Will Larson
- [Engineering Strategy](https://lethain.com/engineering-strategy/) — must-read статья
- [Boring Technology Club](https://boringtechnology.club/) — choosing boring technology
- [DORA Research](https://dora.dev/research/) — original DORA research
- [ADR GitHub](https://adr.github.io/) — Architecture Decision Records

**Tools:**

- [Thoughtworks Tech Radar](https://www.thoughtworks.com/radar) — пример tech radar
- [Backstage](https://backstage.io/) — developer portal / platform
- [LinearB](https://linearb.io/) — DORA metrics tracking

---






