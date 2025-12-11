# Финансовая грамотность менеджера C&S
## P&L, маржинальность, типы контрактов и влияние на прибыль

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать роль Customer & Services ([01_Intro](../01_Intro/))
- Знать основы управления командой ([04_TeamDelivery](../04_TeamDelivery/))
- Базовое понимание бизнес-терминологии

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Понимать финансовую модель аутсорсинговой IT-компании
- Читать и анализировать P&L (Profit & Loss) проекта
- Рассчитывать Gross Margin и Net Margin
- Управлять utilization и понимать его влияние на прибыль
- Различать типы контрактов и их особенности
- Принимать решения, влияющие на прибыльность проекта

---

## 1. Финансовая модель аутсорсинга

### 1.1 Как зарабатывает аутсорсинговая компания

**Базовая формула:**
```
Revenue = Rate × Hours

Profit = Revenue - Costs
```

**Визуализация:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OUTSOURCING BUSINESS MODEL                           │
└─────────────────────────────────────────────────────────────────────────┘

  CLIENT                                              PROVIDER
  ──────                                              ────────
                         SERVICES
              ────────────────────────────▶
  ┌───────┐                                          ┌───────┐
  │Project│                                          │ Team  │
  │ Needs │                                          │       │
  └───────┘                                          └───────┘
                         PAYMENT
              ◀────────────────────────────
              
              $Rate/hour × Hours = Revenue
```

**Ключевые понятия:**

| Термин | Описание | Пример |
|--------|----------|--------|
| **Rate** | Цена за единицу услуги | $50/час, $15,000/месяц |
| **Revenue** | Выручка от клиента | $100,000/месяц |
| **Cost** | Затраты на оказание услуги | Зарплаты, инфраструктура |
| **Profit** | Прибыль (Revenue - Cost) | $25,000/месяц |
| **Margin** | Прибыль в % от выручки | 25% |

### 1.2 Структура затрат

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COST STRUCTURE                                       │
└─────────────────────────────────────────────────────────────────────────┘

  TOTAL COSTS
       │
       ├──► DIRECT COSTS (относятся к проекту)
       │    ├── Зарплаты инженеров на проекте
       │    ├── Инструменты для проекта (лицензии)
       │    └── Субподрядчики
       │
       └──► INDIRECT COSTS / OVERHEAD (общие)
            ├── Менеджмент (DM, AM, executive)
            ├── HR, Finance, Legal
            ├── Офис, инфраструктура
            ├── Обучение, benefits
            └── Sales & Marketing
```

### 1.3 Revenue vs Profit

```
                    REVENUE WATERFALL
                    ─────────────────
                    
Revenue:        $100,000  │████████████████████████████████████████│ 100%
                          │                                        │
Direct Costs:   -$60,000  │████████████████████████                │  60%
                          │                                        │
                ──────────│                                        │
Gross Profit:   $40,000   │                ████████████████        │  40%
                          │                                        │
Overhead:       -$20,000  │                ██████████              │  20%
                          │                                        │
                ──────────│                                        │
Net Profit:     $20,000   │                      ██████████        │  20%
```

---

## 2. P&L проекта

### 2.1 Что такое P&L

**P&L (Profit & Loss Statement)** — отчёт о прибылях и убытках, показывающий финансовый результат за период.

### 2.2 Структура Project P&L

```
┌─────────────────────────────────────────────────────────────────────────┐
│              PROJECT P&L - PHOENIX APP                                  │
│              Period: December 2024                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ REVENUE                                                                 │
│ ─────────────────────────────────────────────────────────────────────  │
│ Billable hours:              800 hours                                  │
│ Blended rate:                $65/hour                                   │
│ ─────────────────────────────────────────────────────────────────────  │
│ TOTAL REVENUE:                                          $52,000        │
│                                                                         │
│ DIRECT COSTS                                                            │
│ ─────────────────────────────────────────────────────────────────────  │
│ Alex (TL)      - 160h × $40/h cost                      $6,400         │
│ Maria (Senior) - 160h × $35/h cost                      $5,600         │
│ John (Middle)  - 160h × $28/h cost                      $4,480         │
│ Kate (Middle)  - 160h × $28/h cost                      $4,480         │
│ Sarah (QA)     - 160h × $25/h cost                      $4,000         │
│ Tools & Infrastructure                                   $1,200         │
│ ─────────────────────────────────────────────────────────────────────  │
│ TOTAL DIRECT COSTS:                                     $26,160        │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ GROSS PROFIT:                                           $25,840        │
│ GROSS MARGIN:                                           49.7%          │
│ ═══════════════════════════════════════════════════════════════════════│
│                                                                         │
│ OVERHEAD ALLOCATION (20% of revenue)                    $10,400        │
│                                                                         │
│ ═══════════════════════════════════════════════════════════════════════│
│ NET PROFIT:                                             $15,440        │
│ NET MARGIN:                                             29.7%          │
│ ═══════════════════════════════════════════════════════════════════════│
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Gross Margin vs Net Margin

**Gross Margin (Валовая маржа):**
```
Gross Margin = (Revenue - Direct Costs) / Revenue × 100%

Пример:
Revenue = $52,000
Direct Costs = $26,160
Gross Margin = ($52,000 - $26,160) / $52,000 = 49.7%
```

**Net Margin (Чистая маржа):**
```
Net Margin = (Revenue - Direct Costs - Overhead) / Revenue × 100%

Пример:
Revenue = $52,000
Direct Costs = $26,160
Overhead = $10,400
Net Margin = ($52,000 - $26,160 - $10,400) / $52,000 = 29.7%
```

### 2.4 Benchmark маржинальности

| Показатель | Low | Target | Good |
|------------|-----|--------|------|
| **Gross Margin** | <35% | 40-50% | >55% |
| **Net Margin** | <15% | 20-25% | >30% |

**Интерпретация:**
- Gross Margin < 35%: Проект не окупает себя
- Net Margin < 15%: Нужен пересмотр условий
- Net Margin > 30%: Отличный проект, можно масштабировать

---

## 3. Utilization

### 3.1 Виды utilization

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    UTILIZATION BREAKDOWN                                │
└─────────────────────────────────────────────────────────────────────────┘

  TOTAL AVAILABLE TIME (2080 hours/year per person)
  ──────────────────────────────────────────────
            │
            ├──► BILLABLE (клиент платит)
            │    └── Работа на проекте клиента
            │
            ├──► BENCH (ожидание проекта)
            │    └── Между проектами, нет billable работы
            │
            └──► OVERHEAD (non-billable работа)
                 ├── Обучение
                 ├── Внутренние проекты
                 ├── Митинги, administration
                 └── Больничные, отпуска
```

### 3.2 Расчёт utilization

```
Billable Utilization = Billable Hours / Available Hours × 100%

Пример (за месяц):
Available hours: 168 (21 рабочий день × 8 часов)
Billable hours: 144
Vacation: 8 hours
Training: 8 hours
Internal: 8 hours

Billable Utilization = 144 / 168 = 85.7%
```

### 3.3 Target utilization

| Роль | Target Utilization |
|------|-------------------|
| Junior Developer | 85-90% |
| Middle Developer | 85-90% |
| Senior Developer | 75-85% |
| Tech Lead | 65-75% |
| Delivery Manager | 50-70% |
| Architect | 60-75% |

**Почему разный target?**
- Senior/TL тратят время на менторинг, code review
- DM тратит время на management, не billable
- Junior максимально на проекте для обучения

### 3.4 Влияние utilization на прибыль

```
┌─────────────────────────────────────────────────────────────────────────┐
│              UTILIZATION IMPACT ON PROFIT                               │
└─────────────────────────────────────────────────────────────────────────┘

  Scenario: Developer with $30/h cost, $60/h rate

  UTILIZATION │ BILLABLE │ REVENUE │  COST  │ PROFIT │ MARGIN
  ────────────┼──────────┼─────────┼────────┼────────┼────────
      100%    │   168h   │ $10,080 │ $5,040 │ $5,040 │  50%
       90%    │   151h   │  $9,072 │ $5,040 │ $4,032 │  44%
       80%    │   134h   │  $8,064 │ $5,040 │ $3,024 │  38%
       70%    │   118h   │  $7,056 │ $5,040 │ $2,016 │  29%
       60%    │   101h   │  $6,048 │ $5,040 │ $1,008 │  17%
       50%    │    84h   │  $5,040 │ $5,040 │     $0 │   0%
    <50%      │   <84h   │ <$5,040 │ $5,040 │  LOSS  │  NEG

  📊 Каждые 10% снижения utilization = ~10% снижения margin
```

### 3.5 Bench Management

**Bench** — сотрудники без текущего billable проекта.

**Bench rate:**
```
Bench Rate = Bench Hours / Total Available Hours × 100%

Target: < 10% в среднем по компании
```

**Стратегии минимизации bench:**
1. **Proactive staffing** — начинать поиск проекта заранее
2. **Internal projects** — использовать для R&D, tooling
3. **Training** — инвестиции в skills (но это cost)
4. **Cross-training** — расширение skills для гибкости
5. **Contractors** — использовать для пиковых нагрузок

---

## 4. Role Rate

### 4.1 Что такое Role Rate

**Role Rate** — цена за час работы специалиста определённого уровня.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ROLE RATE CARD                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ ROLE              │ COST RATE │ BILL RATE │ MARKUP │ MARGIN            │
│ ──────────────────┼───────────┼───────────┼────────┼────────            │
│ Junior Developer  │   $20/h   │   $40/h   │  2.0x  │  50%              │
│ Middle Developer  │   $28/h   │   $55/h   │  2.0x  │  49%              │
│ Senior Developer  │   $35/h   │   $75/h   │  2.1x  │  53%              │
│ Tech Lead         │   $40/h   │   $90/h   │  2.2x  │  56%              │
│ Architect         │   $50/h   │  $120/h   │  2.4x  │  58%              │
│ QA Engineer       │   $25/h   │   $50/h   │  2.0x  │  50%              │
│ DevOps Engineer   │   $35/h   │   $80/h   │  2.3x  │  56%              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Blended Rate

**Blended Rate** — средневзвешенный rate команды.

```
Blended Rate = Total Revenue / Total Billable Hours

Пример:
Team composition:
- 1 TL × $90/h × 160h = $14,400
- 2 Middle × $55/h × 160h × 2 = $17,600
- 1 QA × $50/h × 160h = $8,000

Total Revenue: $40,000
Total Hours: 640h
Blended Rate: $40,000 / 640 = $62.5/h
```

### 4.3 Влияние Team Mix на маржинальность

```
┌─────────────────────────────────────────────────────────────────────────┐
│              TEAM MIX IMPACT ON MARGIN                                  │
└─────────────────────────────────────────────────────────────────────────┘

  SCENARIO A: Senior-heavy team
  ─────────────────────────────
  2 Seniors × $75/h = $150/h revenue
  2 Seniors × $35/h = $70/h cost
  Gross Margin = 53%

  SCENARIO B: Balanced team
  ─────────────────────────────
  1 Senior × $75/h + 1 Middle × $55/h = $130/h revenue
  1 Senior × $35/h + 1 Middle × $28/h = $63/h cost
  Gross Margin = 52%

  SCENARIO C: Junior-heavy team
  ─────────────────────────────
  1 Middle × $55/h + 1 Junior × $40/h = $95/h revenue
  1 Middle × $28/h + 1 Junior × $20/h = $48/h cost
  Gross Margin = 49%

  📊 Senior-heavy = выше margin, но дороже для клиента
  📊 Junior-heavy = ниже margin, требует supervision
```

---

## 5. Типы контрактов

### 5.1 Time & Materials (T&M)

**Суть:** Клиент платит за фактически потраченное время.

```
Revenue = Hours Worked × Rate
```

**Характеристики:**

| Аспект | T&M |
|--------|-----|
| Risk | Низкий для provider, высокий для клиента |
| Flexibility | Высокая — scope может меняться |
| Predictability | Низкая для клиента |
| Billing | Ежемесячно по timesheet |
| Best for | R&D, unclear scope, long-term |

**Пример:**
```
Contract: T&M, 5 developers, $60 blended rate
Monthly hours: 800
Monthly revenue: $48,000
Scope: Flexible, managed via sprints
```

### 5.2 Fixed Price (FP)

**Суть:** Клиент платит фиксированную сумму за определённый scope.

```
Revenue = Fixed Amount (независимо от затраченного времени)
```

**Характеристики:**

| Аспект | Fixed Price |
|--------|-------------|
| Risk | Высокий для provider, низкий для клиента |
| Flexibility | Низкая — scope фиксирован |
| Predictability | Высокая для клиента |
| Billing | По milestones или по завершении |
| Best for | Clear scope, short projects |

**Пример:**
```
Contract: FP, Mobile app MVP
Price: $150,000
Timeline: 4 months
Scope: Strictly defined, change requests = extra cost
```

**Риски FP для провайдера:**
- Неверная оценка → убытки
- Scope creep → работа бесплатно
- Изменения требований → конфликты

### 5.3 Retainer

**Суть:** Клиент платит фиксированную сумму за доступность ресурсов.

```
Revenue = Monthly Fee (независимо от utilization)
```

**Характеристики:**

| Аспект | Retainer |
|--------|----------|
| Risk | Сбалансированный |
| Flexibility | Средняя — в рамках capacity |
| Predictability | Высокая для обеих сторон |
| Billing | Ежемесячно фиксированная сумма |
| Best for | Ongoing support, reserved capacity |

**Пример:**
```
Contract: Retainer, 3 developers
Monthly fee: $45,000 (includes up to 480 hours)
Unused hours: Don't roll over
Additional hours: $100/h
```

### 5.4 Managed Services

**Суть:** Provider управляет функцией или системой целиком.

```
Revenue = Fixed Monthly Fee for Service Level
```

**Характеристики:**

| Аспект | Managed Services |
|--------|------------------|
| Risk | Provider manages operational risk |
| Flexibility | SLA-driven |
| Predictability | High for both |
| Billing | Monthly subscription |
| Best for | Ops, support, DevOps, maintenance |

**Пример:**
```
Contract: Managed DevOps
Monthly fee: $25,000
SLA: 99.9% uptime, 15 min response for P1
Includes: CI/CD, monitoring, on-call, security patching
```

### 5.5 Сравнение контрактов

```
┌─────────────────────────────────────────────────────────────────────────┐
│              CONTRACT COMPARISON                                        │
└─────────────────────────────────────────────────────────────────────────┘

                    PROVIDER RISK                    CLIENT RISK
                         │                                │
  LOW ◄──────────────────┼────────────────────────────────┼──────────► HIGH
                         │                                │
       ┌─────────────────┼────────────────────────────────┼───────────────┐
       │                 │                                │               │
       │     T&M    Retainer    Managed Services    Fixed Price          │
       │                 │                                │               │
       └─────────────────┼────────────────────────────────┼───────────────┘
                         │                                │
                    FLEXIBILITY                    PREDICTABILITY
                    
  HIGH ◄─────────────────────────────────────────────────────────────► LOW
```

---

## 6. Как менеджер влияет на прибыльность

### 6.1 Рычаги влияния DM

```
┌─────────────────────────────────────────────────────────────────────────┐
│              DM INFLUENCE ON PROFITABILITY                              │
└─────────────────────────────────────────────────────────────────────────┘

  1. UTILIZATION MANAGEMENT
     ─────────────────────────
     • Минимизировать bench time
     • Эффективный staffing
     • Планирование capacity

  2. TEAM COMPOSITION
     ─────────────────────────
     • Оптимальный mix ролей
     • Не over-staff seniors
     • Не under-staff for quality

  3. SCOPE MANAGEMENT
     ─────────────────────────
     • Контроль scope creep
     • Change request process
     • Clear requirements

  4. EFFICIENCY
     ─────────────────────────
     • Минимизировать waste
     • Process improvements
     • Automation

  5. PRICING
     ─────────────────────────
     • Rate negotiations
     • Upsell opportunities
     • Value-based pricing
```

### 6.2 Практические действия

**Улучшить Utilization:**
- [ ] Начинать staffing за 30 дней до освобождения ресурса
- [ ] Иметь pipeline возможностей
- [ ] Cross-training для flexibility
- [ ] Использовать bench для internal projects

**Оптимизировать Team Mix:**
- [ ] Анализировать, нужен ли Senior или Middle справится
- [ ] Рассматривать juniors для routine tasks
- [ ] Не бояться upgrade при необходимости

**Контролировать Scope:**
- [ ] Чёткие acceptance criteria
- [ ] Change request process
- [ ] Регулярные scope reviews
- [ ] Говорить "нет" бесплатной работе

### 6.3 Пример: Влияние решений на P&L

```
SCENARIO: Клиент просит добавить фичу бесплатно

Option A: Согласиться (bad)
─────────────────────────────
Additional work: 80 hours
Cost: $2,400 (80h × $30/h)
Revenue: $0
Impact on margin: -$2,400 / $52,000 = -4.6%

Option B: Оценить и предложить как change request (good)
─────────────────────────────
Additional work: 80 hours
Revenue: $5,200 (80h × $65/h)
Cost: $2,400
Impact on margin: +$2,800 / $52,000 = +5.4%

DIFFERENCE: 10% swing in margin!
```

---

## 7. Финансовая отчётность

### 7.1 Метрики для мониторинга

| Метрика | Формула | Частота |
|---------|---------|---------|
| Revenue | Billed amount | Monthly |
| Gross Margin | (Revenue - Direct Costs) / Revenue | Monthly |
| Net Margin | (Revenue - All Costs) / Revenue | Monthly |
| Utilization | Billable hours / Available hours | Weekly |
| Bench Rate | Bench hours / Total hours | Weekly |
| Revenue per head | Revenue / Headcount | Monthly |

### 7.2 Monthly Financial Review

```
┌─────────────────────────────────────────────────────────────────────────┐
│              MONTHLY FINANCIAL REVIEW - DECEMBER 2024                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ PROJECT SUMMARY                                                         │
│ ─────────────────────────────────────────────────────────────────────  │
│                                                                         │
│ Metric              │  Actual  │  Target  │   Δ   │  Status            │
│ ────────────────────┼──────────┼──────────┼───────┼────────            │
│ Revenue             │  $52,000 │  $55,000 │ -$3K  │  🟡 Below          │
│ Gross Margin        │   49.7%  │    50%   │ -0.3% │  🟢 On track       │
│ Net Margin          │   29.7%  │    25%   │ +4.7% │  🟢 Above          │
│ Utilization         │   85.7%  │    85%   │ +0.7% │  🟢 On track       │
│ Headcount           │     5    │     5    │   0   │  🟢 As planned     │
│                                                                         │
│ VARIANCE ANALYSIS                                                       │
│ ─────────────────────────────────────────────────────────────────────  │
│                                                                         │
│ Revenue below target:                                                   │
│ • QA on vacation 3 days (-$1,500)                                      │
│ • Public holiday (-$1,500)                                             │
│                                                                         │
│ Net margin above target:                                                │
│ • Lower than expected tool costs                                       │
│ • No overtime costs                                                     │
│                                                                         │
│ NEXT MONTH FORECAST                                                     │
│ ─────────────────────────────────────────────────────────────────────  │
│ Revenue: $58,000 (full capacity + no holidays)                         │
│ Gross Margin: 51% target                                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Практический кейс

### 8.1 Задача: Расчёт маржинальности

**Исходные данные:**

```
Project: Alpha
Contract: T&M
Team: 4 developers
Duration: 1 month

Team composition:
• 1 Senior Developer: $75/h bill rate, $35/h cost, 160 billable hours
• 2 Middle Developers: $55/h bill rate, $28/h cost, 160 billable hours each
• 1 QA: $50/h bill rate, $25/h cost, 160 billable hours

Overhead allocation: 18% of revenue
Additional costs: $800 (tools, infrastructure)
```

### 8.2 Решение

```
STEP 1: Calculate Revenue
─────────────────────────────
Senior: 160h × $75 = $12,000
Middle 1: 160h × $55 = $8,800
Middle 2: 160h × $55 = $8,800
QA: 160h × $50 = $8,000
─────────────────────────────
Total Revenue: $37,600


STEP 2: Calculate Direct Costs
─────────────────────────────
Senior: 160h × $35 = $5,600
Middle 1: 160h × $28 = $4,480
Middle 2: 160h × $28 = $4,480
QA: 160h × $25 = $4,000
Tools: $800
─────────────────────────────
Total Direct Costs: $19,360


STEP 3: Calculate Gross Profit & Margin
─────────────────────────────
Gross Profit = $37,600 - $19,360 = $18,240
Gross Margin = $18,240 / $37,600 = 48.5%


STEP 4: Calculate Overhead
─────────────────────────────
Overhead = $37,600 × 18% = $6,768


STEP 5: Calculate Net Profit & Margin
─────────────────────────────
Net Profit = $18,240 - $6,768 = $11,472
Net Margin = $11,472 / $37,600 = 30.5%


RESULT:
─────────────────────────────
Revenue: $37,600
Gross Margin: 48.5% ✓ (target 40-50%)
Net Margin: 30.5% ✓ (target 20-25%, exceeded!)
```

### 8.3 Что если utilization снизится?

```
SCENARIO: QA на больничном 5 дней (40 hours)

QA billable hours: 160 - 40 = 120h
QA revenue: 120h × $50 = $6,000 (was $8,000)
QA cost: 160h × $25 = $4,000 (unchanged - still paying salary)

New Total Revenue: $37,600 - $2,000 = $35,600
New Direct Costs: $19,360 (unchanged)
New Gross Profit: $35,600 - $19,360 = $16,240
New Gross Margin: $16,240 / $35,600 = 45.6% (was 48.5%)

Impact: -2.9% margin drop from one person's absence!
```

---

## 💡 Key Takeaways

- **Profit = Revenue - Costs** — простая формула, но много факторов влияют
- **Gross Margin 40-50%**, **Net Margin 20-25%** — здоровые benchmarks для аутсорсинга
- **Utilization** критично влияет на margin: каждые 10% снижения utilization ≈ 10% снижения margin
- **Team mix** влияет на margin: senior-heavy команда = выше margin, но дороже для клиента
- **T&M** — низкий риск для провайдера; **Fixed Price** — высокий риск
- **Scope management** — ключ к защите маржи; бесплатная работа = прямые убытки
- **DM влияет** на прибыльность через utilization, team mix, scope control и efficiency

---

## 🚀 Next Steps

**Related Modules:**
- [06_Upsell](../06_Upsell/) — Развитие клиента и upsell
- [04_TeamDelivery](../04_TeamDelivery/) — Управление командой

**Practice Ideas:**
1. Рассчитайте P&L для текущего проекта
2. Проанализируйте utilization команды за последний месяц
3. Определите возможности оптимизации team mix

**Going Deeper:**
- "Financial Intelligence for IT Professionals"
- "The Outsourcing Handbook" — финансовая модель аутсорсинга
- Coursera: "Finance for Non-Financial Managers"

---

## 📚 Additional Resources

**Книги:**
- "Financial Intelligence" by Karen Berman — финансы для не-финансистов
- "The Goal" by Eliyahu Goldratt — теория ограничений

**Tools:**
- Excel/Google Sheets — базовый P&L tracking
- Harvest, Toggl — time tracking для utilization
- Float, Resource Guru — capacity planning

**Templates:**
- [P&L Calculator](../templates/pl_calculator.xlsx)
- [Utilization Tracker](../templates/utilization_tracker.xlsx)

---


