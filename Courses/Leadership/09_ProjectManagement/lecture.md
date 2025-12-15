# Team Leading vs Project Management
## Различия ролей и взаимодействие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать роль Team Lead / Engineering Manager
- Иметь опыт работы в проектах с deadlines
- Понимать основы Agile/Scrum

**Recommended prior modules:**

- [01_Transition](../01_Transition/) — переход в лидерство
- [07_TeamProcesses](../07_TeamProcesses/) — процессы в команде

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать роли Team Lead и Project Manager
- Понимать, когда нужен отдельный PM, а когда нет
- Эффективно взаимодействовать с PM
- Управлять delivery как Team Lead
- Балансировать people leadership и delivery

---

## 1. Роли в командах

### 1.1 Зоопарк ролей

В IT командах часто встречается путаница с ролями. Одни и те же названия могут означать разное в разных компаниях.

**Основные роли:**

| Роль | Главный фокус | Ключевые вопросы |
|------|---------------|------------------|
| **Product Manager (PdM)** | WHAT & WHY | Что строить? Для кого? Почему? |
| **Project Manager (PM)** | WHEN & HOW (process) | Когда готово? Какие риски? |
| **Team Lead (TL)** | HOW (technical) | Как построить? Какая архитектура? |
| **Engineering Manager (EM)** | WHO | Кто делает? Как развивать людей? |
| **Scrum Master (SM)** | PROCESS | Как улучшить процесс? |
| **Tech Lead** | HOW (deep technical) | Как решить сложную техническую проблему? |

> **💡 Key Insight:**  
> Важнее понимать **responsibilities**, чем titles. В разных компаниях "Team Lead" может означать совершенно разное.

### 1.2 Детальное сравнение ролей

**Product Manager (PdM):**

| Responsibility | Описание |
|----------------|----------|
| Product Vision | Куда движется продукт на 1-3 года |
| Roadmap | Что делаем в ближайшие кварталы |
| Prioritization | Что важнее: Feature A или B? |
| Customer Research | Что нужно пользователям? |
| Go-to-Market | Как запускаем и продвигаем? |
| Metrics | Product metrics (retention, conversion) |

**Project Manager (PM):**

| Responsibility | Описание |
|----------------|----------|
| Planning | Когда будет готово? Какие milestones? |
| Tracking | Где мы сейчас vs plan? |
| Risk Management | Что может пойти не так? |
| Stakeholder Comm | Информирование всех заинтересованных |
| Resource Allocation | Достаточно ли людей? Budget? |
| Dependencies | Кто от нас зависит? От кого мы? |
| Process | Какой процесс используем? |

**Team Lead / Engineering Manager:**

| Responsibility | Описание |
|----------------|----------|
| Technical Direction | Как строить? Какие технологии? |
| Code Quality | Ревью, стандарты, архитектура |
| Team Health | Мотивация, развитие, retention |
| Estimation | Сколько времени займёт? |
| Blocker Removal | Что мешает команде? |
| Hiring | Кого нанимать? |
| Performance | Как работает каждый человек? |

### 1.3 Пересечения ролей

```

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                          PdM                                    │
│                    (WHAT & WHY)                                 │
│                    ┌─────────┐                                  │
│                    │ Product │                                  │
│                    │ Vision  │                                  │
│                    └────┬────┘                                  │
│                         │                                       │
│         ┌───────────────┼───────────────┐                       │
│         │               │               │                       │
│         ▼               ▼               ▼                       │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐                   │
│    │   PM    │◄───│  TL/EM  │───►│   SM    │                   │
│    │  WHEN   │    │ WHO/HOW │    │ PROCESS │                   │
│    └─────────┘    └─────────┘    └─────────┘                   │
│                                                                 │
│    GREY ZONES (need explicit agreement):                        │
│    • Estimation: PM needs, TL/EM provides                       │
│    • Scope changes: PdM decides, PM tracks, TL assesses         │
│    • Risk communication: PM process, TL technical               │
│    • Team capacity: TL/EM owns, PM needs to know                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.4 RACI Matrix для типичных ситуаций

**RACI:**

- **R**esponsible — делает работу

- **A**ccountable — несёт ответственность за результат

- **C**onsulted — консультируется

- **I**nformed — информируется

| Активность | PdM | PM | TL/EM | Team |
|------------|-----|-----|-------|------|
| Product roadmap | A, R | I | C | I |
| Sprint planning | C | C | A | R |
| Technical estimation | I | C | A | R |
| Timeline commitment | A | R | C | I |
| Technical decisions | I | I | A, R | C |
| Risk identification | C | A | R | C |
| Stakeholder updates | C | R | C | I |
| Hiring decisions | C | I | A, R | C |
| Performance reviews | I | I | A, R | - |
| Scope changes | A | R | C | I |

> **💡 Pro Tip:**  
> Создайте RACI для вашей команды и согласуйте со всеми. Это предотвратит многие конфликты.

---

## 2. Когда нужен Project Manager

### 2.1 Матрица принятия решения

```

                    HIGH COMPLEXITY
                         │
    PM HELPFUL           │        PM ESSENTIAL
    ─────────────        │        ────────────
    • 2-3 teams          │        • 4+ teams involved
    • Medium scope       │        • Large scope (6+ months)
    • Some stakeholders  │        • Many stakeholders
    • Flexible deadline  │        • Hard deadline (contract)
                         │
    ─────────────────────┼─────────────────────
                         │
    PM NOT NEEDED        │        PM HELPFUL
    ─────────────        │        ────────────
    • 1 team             │        • 1-2 teams
    • Small scope        │        • Medium scope
    • Few stakeholders   │        • Regulatory requirements
    • Internal only      │        • External visibility
                         │
                    LOW COMPLEXITY
    ────────────────────────────────────────────
    LOW                 CROSS-TEAM              HIGH
                       DEPENDENCIES
```

### 2.2 Когда PM необходим

| Фактор | Threshold для PM | Почему |
|--------|-----------------|--------|
| **Количество команд** | 3+ команд | Coordination overhead |
| **Длительность** | 6+ месяцев | Long-term tracking |
| **Stakeholders** | 5+ stakeholders | Communication management |
| **Зависимости** | Много внешних | Dependency tracking |
| **Deadline тип** | Контрактный, регуляторный | Risk management critical |
| **Budget** | > $500K | Financial tracking |

**Примеры проектов, требующих PM:**

| Тип проекта | Почему нужен PM |
|-------------|-----------------|
| Enterprise Integration | Много систем, stakeholders, контракты |
| Product Launch с Marketing | Координация с non-eng командами |
| Compliance (SOC2, GDPR) | Регуляторные deadlines, documentation |
| Large Migration | Много команд, risks, downtime planning |
| M&A Integration | Cross-company, legal, timeline-driven |
| Multi-region Launch | Time zones, localization, dependencies |

### 2.3 Когда PM не нужен

| Ситуация | Почему можно без PM |
|----------|---------------------|
| Маленькая команда (3-7 человек) | TL может справиться |
| Стабильный backlog, routine work | Нет coordination complexity |
| Одна команда, нет внешних deps | Нет cross-team overhead |
| Agile команда с опытным PO | PO + TL покрывают нужды |
| Internal tools, flexible timeline | Low stakes |

### 2.4 "TL как PM" — распространённая практика

В стартапах и небольших командах TL часто совмещает роли.

**Когда это работает:**

| Условие | Почему работает |
|---------|-----------------|
| Маленькая команда (< 7) | Управляемый overhead |
| Один проект в фокусе | Нет context switching |
| TL имеет PM навыки | Может делать обе роли |
| Минимум stakeholders | Меньше communication |
| Гибкие deadlines | Меньше pressure |

**Trade-offs:**

```

┌─────────────────────────────────────────────────────────────────┐
│               TL КАК PM: TRADE-OFFS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ПЛЮСЫ                              МИНУСЫ                      │
│  ─────                              ──────                      │
│  • Меньше overhead                  • Перегрузка TL             │
│  • Техническое понимание рисков     • Меньше времени на людей   │
│  • Быстрее решения                  • Меньше времени на технику │
│  • Единая точка контакта            • Burnout риск              │
│  • Меньше miscommunication          • Bottleneck на TL          │
│                                                                 │
│  РИСКИ:                                                         │
│  • Ни одна роль не делается хорошо                              │
│  • Technical debt накапливается (нет времени)                   │
│  • Team development страдает                                    │
│  • TL burnout                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Сигналы, что пора добавить PM:**

```

🚨 Пора искать PM когда:
□ TL тратит > 50% времени на coordination
□ Команда растёт > 7-8 человек
□ Появляются значительные внешние зависимости
□ Stakeholders жалуются на communication
□ TL не успевает на technical leadership
□ Проект становится cross-team
```

---

## 3. Team Lead и Delivery

### 3.1 Delivery Responsibilities TL

Даже без PM, Team Lead отвечает за:

```

Planning:

- Участие в estimation
- Декомпозиция работы
- Выявление технических рисков

Execution:

- Убирание блокеров
- Technical decisions
- Code review bottlenecks

Tracking:

- Progress monitoring
- Risk communication
- Scope discussions

```

### 3.2 Planning как TL

**Estimation:**

- Участвуйте в estimation, не навязывайте оценки
- Учитывайте неопределённость (добавляйте buffer)
- Декомпозируйте большие задачи

**Risk identification:**
```

Технические риски:

- Незнакомые технологии
- Интеграции с внешними системами
- Performance concerns
- Security requirements

Organizational риски:

- Зависимости от других команд
- Key people отпуска/уход
- Changing requirements

```

### 3.3 Execution

**Убирание блокеров:**
```

1. Daily standup: выявить блокеры
2. После standup: immediately action
3. Escalate если не можете решить
4. Follow up до разрешения

```

**Technical decisions:**

- Быстро принимайте routine decisions
- Вовлекайте команду в значимые
- Документируйте важные (ADR)

### 3.4 Communication

**Status updates:**
```markdown
## Weekly Status: [Project Name]

### Progress
- [x] Feature A — done
- [ ] Feature B — in progress (70%)
- [ ] Feature C — blocked

### Risks
- Integration with System X delayed (mitigation: parallel work on Y)

### This Week
- Complete Feature B
- Start Feature D

### Needs Decision

- Approach for caching: Option A vs B (need input by Friday)

```

---

## 4. Работа с Project Manager

### 4.1 Разделение responsibilities: детальный RACI

**Здоровое разделение:**

| Aspect | PM | TL | Комментарий |
|--------|-----|-----|-------------|
| Timeline planning | **A** | C, R | PM commits, TL provides estimates |
| Technical estimates | I | **A, R** | TL owns, PM uses |
| Stakeholder comms | **A, R** | C | PM leads, TL provides tech input |
| Process risks | **A, R** | C | PM identifies, TL helps |
| Technical risks | C | **A, R** | TL identifies, PM tracks |
| Team capacity | I | **A** | TL knows, PM needs awareness |
| Technical decisions | I | **A, R** | PM should be informed |
| Process | **A, R** | C | PM proposes, team inputs |
| People issues | I | **A** | TL or EM handles |
| Scope changes | **A** | C | PM tracks, TL assesses impact |

### 4.2 Типичные конфликты и как решать

**Конфликт 1: "PM давит на сроки"**

```

Ситуация:
PM: "Нам нужно сделать это к пятнице."
TL: (понимает, что это невозможно качественно)

Плохой ответ:
"Невозможно." (без alternatives)

Хороший ответ:
"Давай обсудим. К пятнице мы можем сделать [scope A],
но полный scope займёт [N дней].

Варианты:
1. Делаем [scope A] к пятнице, [scope B] на следующей неделе
2. Сдвигаем deadline на [дата] для полного scope
3. Добавляем людей (если есть) — риск: onboarding overhead

Какой вариант лучше для бизнеса?"
```

**Конфликт 2: "PM не понимает complexity"**

```

Ситуация:
PM: "Это же просто добавить кнопку, почему 2 недели?"

Плохой ответ:
"Ты не понимаешь технику." (dismissive)

Хороший ответ:
"Кнопка — это UI часть, она займёт 1 день.
Но эта кнопка запускает процесс, который:
- Требует изменения 3 сервисов
- Должен быть надёжным (retry logic, error handling)
- Требует интеграции с [System X], у них API quirks

Вот breakdown:
- UI: 1 день
- Backend logic: 3 дня
- Integration: 4 дня
- Testing: 2 дня
- Buffer: 1 день

Если хочешь быстрее — можем упростить [X]."
```

**Конфликт 3: "PM микроменеджит команду"**

```

Ситуация:
PM ходит к разработчикам напрямую, спрашивает статус,
даёт задачи минуя TL.

Разговор с PM:
"Я заметил, что ты общаешься с командой напрямую 
по задачам и статусам.

Это создаёт путаницу — люди не знают, кого слушать.
И я теряю картину происходящего.

Давай договоримся:
- Для статуса проекта — спрашивай меня или на standup
- Для технических деталей — я организую нужного человека
- Если срочно — напиши мне, я быстро найду ответ

Так мы оба будем в курсе. Работает?"
```

**Конфликт 4: "Мы не можем договориться о приоритетах"**

```

Ситуация:
PM хочет feature A, TL считает нужно сначала 
исправить tech debt B.

Подход:
"У нас разные views на приоритеты. Давай разберём:

Твой view (PM): Feature A важнее потому что [business reason]
Мой view (TL): Tech debt B потому что [technical reason + business impact]

Я понимаю business pressure. Вот что я вижу:
- Если делаем A сейчас: работает, но займёт 3 недели
- Если сначала B (1 неделя), потом A: общее время 3.5 недели,
  но будущие фичи будут быстрее

Trade-off: 0.5 недели сейчас vs [X] недель за год.

Давай обсудим это с [PdM/Director], 
чтобы принять решение вместе."
```

### 4.3 Эффективное партнёрство

**Ключевые принципы:**

| Принцип | Как реализовать |
|---------|-----------------|
| **Aligned goals** | Обсудите shared metrics успеха |
| **Regular sync** | 2-3 раза в неделю, 15-30 мин |
| **No surprises** | Плохие новости сразу, не копите |
| **Mutual respect** | Признавайте expertise друг друга |
| **United front** | Не спорьте при stakeholders |

**Формат PM-TL Weekly Sync (30-45 min):**

```markdown
## PM-TL Weekly Sync

### 1. Progress Review (10 min)
- What was completed this week?
- What's in progress?
- Any delays vs plan?

### 2. Risks & Blockers (10 min)
- New risks identified?
- Blocker status?
- Mitigation updates?

### 3. Upcoming Week (10 min)
- What's planned?
- Any concerns about capacity?
- Dependencies to watch?

### 4. Stakeholder Updates (5 min)
- What do stakeholders need to know?
- Any questions to address?
- Upcoming presentations?

### 5. Decisions Needed (5 min)

- Any decisions pending?
- Who needs to be involved?
```

### 4.4 Building Trust с PM

**Как завоевать trust:**

| Action | Why It Works |
|--------|--------------|
| Deliver on commitments | Trust через reliability |
| Flag risks early | PM can manage expectations |
| Provide options, not just problems | Solution-oriented |
| Explain technical constraints clearly | Educated PM = better PM |
| Respect their expertise | They know things you don't |
| Support them publicly | United front |

---

## 5. Delivery без PM

### 5.1 Self-managing Teams

**Характеристики:**

- Команда сама планирует спринты
- Ownership за delivery
- Прямая коммуникация со stakeholders
- TL фасилитирует, не директивит

### 5.2 Процессы для delivery

**Sprint-based delivery:**
```

Week 1, Monday: Sprint Planning
Week 1-2: Execution
Week 2, Thursday: Demo
Week 2, Friday: Retro + Next planning prep

```

**Kanban-based delivery:**
```

- WIP limits enforced
- Weekly stakeholder sync
- Regular deployment
- Metrics: lead time, throughput

```

### 5.3 Stakeholder Management для TL

**Без PM вы должны:**

- Регулярно информировать stakeholders
- Управлять expectations
- Говорить "нет" или "позже" когда нужно
- Escalate решения если не можете принять

**Формат communication:**
```

For executives: High-level, impact focused
For PdM: Feature progress, scope discussions
For other teams: Dependencies, interfaces

```

---

## 6. Metrics и Tracking

### 6.1 Метрики delivery

**Velocity:**

- Story points за спринт
- Trend over time
- Не для сравнения команд!

**Lead Time:**

- Время от idea до production
- Включает wait time

**Cycle Time:**

- Время активной работы
- Без wait time

**Throughput:**

- Количество items за период

### 6.2 Burndown и Burnup

**Burndown Chart:**
```

Оставшаяся работа vs время
Good: линия идёт вниз к нулю
Bad: плоская или растёт

```

**Burnup Chart:**
```

Сделанная работа vs total scope
Показывает: scope creep visible

```

### 6.3 Как использовать метрики

**DO:**

- Для понимания predictability
- Для выявления проблем в процессе
- Для улучшения estimation

**DON'T:**

- Для сравнения разработчиков
- Для pressure на команду
- Как единственный критерий успеха

---

## 7. Scope Management

### 7.1 Scope Creep

**Признаки:**

- "Ещё одна маленькая штука"
- Requirements меняются в процессе
- Deadline не двигается, scope растёт

**Как управлять:**
```

1. Document original scope
2. Evaluate каждое изменение:
   - Impact на timeline?
   - Impact на другую работу?
3. Trade-offs:
   - Добавляем это → убираем то
   - Добавляем это → двигаем deadline
4. Formal change request для больших изменений

```

### 7.2 Saying "No" (или "Yes, but...")

**Вместо "No":**
```

"Да, мы можем это сделать. 
Это займёт X недель и потребует убрать Y из scope.
Или мы можем сделать упрощённую версию за Z дней."

```

**Framework для приоритизации:**
```

Must have  — без этого не запускаемся
Should have — важно, но можно после launch
Could have  — nice to have
Won't have  — не в этом релизе

```

### 7.3 MVP Mindset

**Minimum Viable Product:**

- Что минимально нужно для value?
- Iterate после feedback
- Avoid overengineering

```

❌ "Давайте сделаем идеально"
✅ "Давайте сделаем минимум, который работает, и улучшим по feedback"

```

---

## 8. Risk Management

### 8.1 Risk Identification

**Категории рисков:**

| Категория | Примеры |
|-----------|---------|
| Technical | Неизвестная технология, performance |
| Resource | Ключевой человек уходит, отпуска |
| Dependency | Другая команда delayed |
| Scope | Requirements unclear, changes |
| External | Vendor issues, regulatory changes |

### 8.2 Risk Assessment

**Для каждого риска:**
```

Risk: [описание]
Probability: High / Medium / Low
Impact: High / Medium / Low
Mitigation: [что делаем для снижения]
Contingency: [что делаем если случится]
Owner: [кто следит]

```

### 8.3 Risk Mitigation Strategies

**Avoid:** Изменить план, чтобы исключить риск

**Mitigate:** Снизить вероятность или impact

**Transfer:** Переложить риск (страховка, vendor)

**Accept:** Принять риск, иметь contingency plan

---

## 💡 Key Takeaways

- **Роли не titles:** Важнее agreements о responsibilities. Создайте RACI для вашей ситуации

- **PM нужен когда:** 3+ команды, 6+ месяцев, много stakeholders, hard deadline. Иначе TL справится

- **TL как PM:** Работает в маленьких командах, но watch for burnout и quality tradeoffs

- **Partnership с PM:** Aligned goals, no surprises, mutual respect, united front

- **Конфликты:** Объясняйте в бизнес-терминах, предлагайте варианты, не просто проблемы

- **Scope management:** Каждое изменение имеет cost. "Yes, and..." вместо "No"

- **Risks = your job:** TL owns technical risks, PM owns process risks. Communicate early

- **Metrics для improvement:** Velocity, Lead Time, Cycle Time — для понимания, не для pressure

---

## 🚀 Next Steps

**Related Modules:**

- [07_TeamProcesses](../07_TeamProcesses/) — процессы для delivery
- [08_Meetings](../08_Meetings/) — planning и coordination meetings
- [11_Communication](../11_Communication/) — stakeholder management

**Practice Ideas:**

1. **RACI Matrix:** Составьте для вашей команды и согласуйте со всеми
2. **Risk Register:** Создайте для текущего проекта с mitigation plans
3. **PM Sync:** Установите regular sync format с PM (если есть)
4. **Status Update:** Попробуйте предложенный weekly format
5. **Delivery Metrics:** Настройте tracking Cycle Time и Lead Time

**Going Deeper:**

- Agile project management certifications
- Risk management frameworks (PMBOK)
- Stakeholder management techniques
- Negotiation skills (для scope discussions)

---

## 📚 Additional Resources

**Books:**

- "The Mythical Man-Month" by Fred Brooks — классика о software projects
- "Making Things Happen" by Scott Berkun — PM perspective
- "User Story Mapping" by Jeff Patton — scope management
- "The Phoenix Project" by Gene Kim — DevOps и delivery
- "Accelerate" by Nicole Forsgren — delivery metrics (DORA)

**Articles:**

- [Atlassian: RACI Matrix](https://www.atlassian.com/team-playbook/plays/raci)
- [Product vs Project Management](https://www.productplan.com/glossary/product-manager-vs-project-manager/)
- [Engineering Manager vs Tech Lead](https://www.atlassian.com/engineering/engineering-manager-vs-tech-lead)

**Frameworks:**

- RACI (Responsible, Accountable, Consulted, Informed)
- MoSCoW (Must, Should, Could, Won't)
- RICE scoring (Reach, Impact, Confidence, Effort)
- Eisenhower Matrix (Urgent vs Important)
- DORA Metrics (Deployment Frequency, Lead Time, etc.)

---





