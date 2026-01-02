# Масштабирование команд
## От 5 до 50 человек: sub-teams и делегирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь опыт управления командой 5+ человек
- Понимать основы team dynamics
- Быть готовым к организационным изменениям

**Recommended prior modules:**

- [07_TeamProcesses](../07_TeamProcesses/) — процессы в команде
- [10_Culture](../10_Culture/) — культура команды

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять, когда пора масштабировать команду
- Разделять команду на sub-teams эффективно
- Делегировать leadership responsibilities
- Поддерживать культуру при росте
- Избегать типичных проблем масштабирования

---

## 1. Признаки необходимости масштабирования

### 1.1 Когда пора расти

**Количественные сигналы:**

- Команда > 7-8 человек на одного менеджера
- Lead time увеличивается
- Больше coordination overhead
- Bottlenecks в review/approvals

**Качественные сигналы:**

- 1-on-1 становятся поверхностными
- Нет времени на development людей
- Контекст теряется
- Решения замедляются

### 1.2 Dunbar's Numbers в командах

**Исследования показывают оптимальные размеры:**

```
5 — Close team (тесная работа)
15 — Extended team (coordination possible)
50 — Tribe (shared identity)
150 — Organization limit (personal relationships)
```

**Практические выводы:**

- 5-7: Идеальная product team
- 8-10: Maximum для одного менеджера
- 15-20: Нужны sub-teams
- 50+: Нужны leaders of leaders

### 1.3 Warning Signs

```
🚨 Пора масштабировать когда:

Team dynamics:

- Standup занимает > 15 минут
- Люди не знают, над чем работают другие
- Communication gaps между частями команды
- "Мы и они" внутри команды

Leader overload:

- Вы bottleneck для решений
- Нет времени на strategic thinking
- 1-on-1 откладываются или сокращаются
- Burnout у лидера
```

---

## 2. Стратегии разделения

### 2.1 По продукту / Feature

**Когда использовать:**

- Разные части продукта независимы
- Minimal dependencies между частями
- Можно владеть end-to-end

**Пример:**
```
До:    Одна команда "Product"
       
После: Team A — Core Platform
       Team B — User Dashboard
       Team C — API & Integrations
```

**Плюсы:**

- Clear ownership
- End-to-end responsibility
- Faster decision-making

**Минусы:**

- Possible duplication
- Integration challenges
- Knowledge silos

### 2.2 По слоям / Stack

**Когда использовать:**

- Глубокая специализация нужна
- Shared infrastructure
- Много reusable components

**Пример:**
```
До:    Одна команда "Engineering"
       
После: Team Frontend
       Team Backend
       Team Infrastructure
```

**Плюсы:**

- Deep expertise
- Reusable solutions
- Clear technical ownership

**Минусы:**

- Handoffs между командами
- Slower end-to-end delivery
- "Throw over the wall"

### 2.3 По mission / Customer

**Когда использовать:**

- Разные customer segments
- Разные business objectives
- Autonomous teams possible

**Пример:**
```
До:    Одна команда "Development"
       
После: Team Growth (acquisition)
       Team Engagement (retention)
       Team Enterprise (B2B)
```

**Плюсы:**

- Customer-focused
- Aligned with business
- Clear metrics per team

**Минусы:**

- Possible overlap
- Different practices
- Integration needs

### 2.4 Hybrid подходы

В реальности часто используется комбинация:

```
┌─────────────────────────────────────────┐
│            Product Organization         │
├─────────────┬─────────────┬─────────────┤
│   Team A    │   Team B    │   Team C    │
│  (Growth)   │   (Core)    │ (Platform)  │
├─────────────┴─────────────┴─────────────┤
│           Shared Services               │
│     (DevOps, Security, Data)            │
└─────────────────────────────────────────┘
```

---

## 3. Team Topologies

### 3.1 Четыре типа команд

**Stream-aligned Team:**
```
- Aligned with business stream
- End-to-end delivery
- Most teams should be this type
- Example: "Checkout Team", "Search Team"
```

**Enabling Team:**
```
- Helps other teams adopt capabilities
- Temporary support
- Removes blockers
- Example: "DevOps Enablement", "Security Team"
```

**Complicated Subsystem Team:**
```
- Owns complex component
- Specialist expertise
- Reduces cognitive load for others
- Example: "ML Platform", "Video Encoding"
```

**Platform Team:**
```
- Internal product for other teams
- Self-service capabilities
- Reduces duplication
- Example: "Internal Developer Platform"
```

### 3.2 Interaction Modes

```
Collaboration: Teams work together closely (temporary)
X-as-a-Service: One team provides to others
Facilitating: Helping team improves another
```

### 3.3 Cognitive Load

> **💡 Key Insight:**  
> Каждая команда имеет ограниченную cognitive load. Если domain слишком большой — качество страдает.

**Признаки перегрузки:**

- Команда "владеет" слишком многим
- Много context switching
- Shallow understanding всего
- Frequent handoffs внутри команды

---

## 4. Делегирование Leadership

### 4.1 От IC к Manager of Managers

**Эволюция роли:**

```
Team Lead (5-8 direct reports)
        ↓
Senior EM (8-12 + some leads)
        ↓
Manager of Managers (3-5 managers)
        ↓
Director (multiple teams)
```

**Что меняется:**
```
При росте:

- Меньше hands-on
- Больше через других
- Coaching вместо doing
- Systems thinking
- Org design
```

### 4.2 Growing Leaders

**Как развивать будущих лидеров:**

```
1. Identify potential
   - Кто берёт ownership?
   - Кого уважает команда?
   - Кто интересуется people?

2. Give opportunities
   - Lead проект
   - Mentor junior
   - Run процесс
   - Represent команду

3. Coach actively
   - Regular 1-on-1 о leadership
   - Feedback на leadership behaviors
   - Expose to leadership challenges

4. Gradual transition
   - Сначала tech lead
   - Затем team lead
   - Поддержка на каждом шаге
```

### 4.3 Delegation Levels

**Матрица делегирования:**

| Level | Description | When |
|-------|-------------|------|
| 1 | Tell: "Do exactly this" | New/critical tasks |
| 2 | Sell: "Do this because..." | Building understanding |
| 3 | Consult: "I'm thinking X, what do you think?" | Developing judgment |
| 4 | Agree: "Let's decide together" | High trust, complex |
| 5 | Advise: "Here's my input, you decide" | Experienced person |
| 6 | Inquire: "What did you decide? Tell me" | Full delegation |
| 7 | Delegate: "You handle it" | Complete trust |

### 4.4 Отпускать контроль

**Mindset shift:**
```
От: "Я должен контролировать всё"
К:  "Я должен создать системы и развить людей"

От: "Если хочешь сделать хорошо — делай сам"
К:  "Если хочешь масштабироваться — развивай других"
```

**Практические шаги:**

1. Определите что ТОЛЬКО вы можете делать
2. Остальное — делегируйте
3. Примите, что будет 80% вашего качества
4. 80% × 3 людей > 100% × 1 вы

---

## 5. Сохранение культуры при росте

### 5.1 Challenges

```
При росте культура размывается:

- Новые люди не знают "как здесь принято"
- Tribal knowledge теряется
- Subcultures формируются
- Original values забываются
```

### 5.2 Mechanisms сохранения

**Documentation:**
```
- Values и behaviors записаны
- Onboarding включает культуру
- Stories записаны и рассказываются
```

**Rituals:**
```
- Ceremonies остаются или адаптируются
- New team rituals aligned с values
- Cross-team events
```

**Hiring:**
```
- Culture interview в процессе
- Values alignment проверяется
- New hires понимают ожидания
```

**Leadership:**
```
- Leaders модель values
- Promotion criteria включают culture
- Culture discussions regular
```

### 5.3 Communication в scale

**Patterns:**
```
Small team:    Everyone knows everything
Medium team:   Structured updates needed
Large org:     Formal communication channels
```

**Tools:**

- All-hands / Town halls
- Written updates
- Documentation
- Slack channels per topic
- Office hours

---

## 6. Организационные структуры

### 6.1 Functional Structure

```
          CTO
           │
    ┌──────┼──────┐
    │      │      │
 Frontend Backend  QA
```

**Плюсы:** Специализация, career paths
**Минусы:** Handoffs, silos

### 6.2 Product Structure

```
          CTO
           │
    ┌──────┼──────┐
    │      │      │
Product A Product B Product C
(cross-   (cross-   (cross-
functional)functional)functional)
```

**Плюсы:** Ownership, fast delivery
**Минусы:** Duplication, inconsistency

### 6.3 Matrix Structure

```
              Functional Managers
                 │   │   │
Product A  ──────┼───┼───┼────
Product B  ──────┼───┼───┼────
Product C  ──────┼───┼───┼────
```

**Плюсы:** Flexibility
**Минусы:** Complexity, dual reporting

### 6.4 Spotify Model (simplified)

```
Tribe A                    Tribe B
┌─────────────────┐       ┌─────────────────┐
│ Squad 1  Squad 2│       │ Squad 5  Squad 6│
│ Squad 3  Squad 4│       │ Squad 7  Squad 8│
└─────────────────┘       └─────────────────┘
         │                                           │
         └────── Chapters ─────────                  ┘
         └────── Guilds ───────────                  ┘
```

**Squads:** Cross-functional teams
**Tribes:** Collection of squads with related mission
**Chapters:** Same specialty across squads
**Guilds:** Community of interest

---

## 7. Scaling Challenges

### 7.1 Communication Overhead

**Formula (Brooks's Law):**
```
Communication paths = n(n-1)/2

5 people: 10 paths
10 people: 45 paths
20 people: 190 paths
```

**Solutions:**

- Clear interfaces между командами
- Documented APIs и contracts
- Regular sync meetings (limited)
- Async by default

### 7.2 Loss of Context

**Problem:**

- Decisions made без full picture
- Duplicated work
- Inconsistent approaches

**Solutions:**

- Architecture decision records
- Tech radar
- Cross-team forums
- Principal engineers

### 7.3 Us vs Them

**Problem:**

- Teams optimize locally
- Blame other teams
- Competition instead of collaboration

**Solutions:**

- Shared goals и metrics
- Cross-team projects
- Rotation программы
- Joint retros

### 7.4 Slowing Down

**Problem:**

- More process, less delivery
- Bureaucracy creeps in
- "We need a meeting for that"

**Solutions:**

- Minimal viable process
- Regular process audits
- Empower teams to decide
- Reduce approval chains

---

## 8. Metrics при масштабировании

### 8.1 Team Health Metrics

```
- Employee NPS / Engagement
- Turnover rate
- 1-on-1 coverage
- Career progression
```

### 8.2 Delivery Metrics

```
- Velocity per team
- Lead time
- Deployment frequency
- Change failure rate
```

### 8.3 Organization Metrics

```
- Cross-team dependencies
- Time to hire
- Onboarding time
- Decision latency
```

---

## 💡 Key Takeaways

- **7-8 max:** Оптимальный размер для одного менеджера

- **Split wisely:** Product/Feature split обычно лучше layer split

- **Grow leaders:** Инвестируйте в развитие будущих лидов

- **Preserve culture:** Документируйте, нанимайте правильно, модель values

- **Fight bureaucracy:** Minimal process, empower teams

---

## 🚀 Next Steps

**Related Modules:**

- [13_DistributedTeams](../13_DistributedTeams/) — распределённые команды
- [17_SeniorLeadership](../17_SeniorLeadership/) — управление на масштабе

**Practice Ideas:**

1. Оцените текущий размер команды по warning signs
2. Если > 8 людей — draft план разделения
3. Определите потенциальных будущих лидеров

**Going Deeper:**

- Team Topologies book
- Org design frameworks
- Conway's Law implications

---

## 📚 Additional Resources

**Books:**

- "Team Topologies" by Matthew Skelton — команды и их взаимодействие
- "An Elegant Puzzle" by Will Larson — системы в engineering management
- "The Mythical Man-Month" by Fred Brooks — классика о масштабировании

**Articles:**

- [Spotify Engineering Culture](https://engineering.atspotify.com/)
- [Amazon Two Pizza Teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/)

---




