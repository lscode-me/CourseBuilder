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

В IT командах часто встречается путаница с ролями:

```

Product Manager (PdM)    — что делать (product vision, roadmap)
Project Manager (PM)     — как и когда (delivery, timeline)
Team Lead (TL)           — техническое лидерство
Engineering Manager (EM) — people management
Scrum Master (SM)        — процесс и ceremonies
Tech Lead                — техническая экспертиза

```

> **💡 Key Insight:**  
> В разных компаниях одни и те же названия могут означать разное. Важнее понимать responsibilities, чем titles.

### 1.2 Различие ролей

**Product Manager (PdM):**
```

Фокус: WHAT и WHY
- Что строить?
- Для кого?
- Почему это важно?
- Приоритизация features
- Roadmap

```

**Project Manager (PM):**
```

Фокус: WHEN и HOW (процесс)
- Когда будет готово?
- Как организовать работу?
- Risk management
- Stakeholder communication
- Budget и resources

```

**Team Lead / Engineering Manager:**
```

Фокус: WHO и HOW (люди + техника)
- Кто делает?
- Как технически?
- Развитие людей
- Качество кода
- Technical decisions

```

### 1.3 Пересечения

```

               PdM
              /   \
             /     \
          WHAT    WHY
             \     /
              \   /
       ┌───────┼───────┐
       │       │       │
      PM ──── TL/EM ────
       │       │       │
      WHEN   WHO/HOW  PEOPLE

```

В реальности роли пересекаются. Важно чётко договориться о responsibilities.

---

## 2. Когда нужен Project Manager

### 2.1 Когда PM необходим

**Сложные проекты:**

- Много зависимостей между командами
- Большой scope (6+ месяцев)
- Много stakeholders
- Строгие deadlines (регуляторные, контрактные)

**Примеры:**

- Enterprise интеграции
- Product launches с marketing
- Compliance проекты
- Large migrations

### 2.2 Когда PM не нужен

**Простые ситуации:**

- Маленькая команда (3-5 человек)
- Стабильный backlog
- Минимум внешних зависимостей
- Agile команда с опытным PO

### 2.3 "TL как PM" — распространённая практика

В стартапах и небольших командах TL часто совмещает роли:

**Плюсы:**

- Меньше overhead на coordination
- Техническое понимание рисков
- Быстрее принимаются решения

**Минусы:**

- Перегрузка TL
- Меньше времени на people/technical leadership
- Risk: ни одна роль не выполняется хорошо

**Когда работает:**

- Маленькая команда
- Относительно простые проекты
- TL имеет PM навыки

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

### 4.1 Разделение responsibilities

**Здоровое разделение:**

| Aspect | PM | TL |
|--------|-----|-----|
| Timeline planning | Leads | Input |
| Technical estimates | Input | Leads |
| Stakeholder comms | Leads | Technical input |
| Risk management | Process risks | Technical risks |
| Team capacity | Awareness | Leads |
| Technical decisions | Awareness | Leads |
| Process | Leads | Follows/Input |
| People issues | Awareness | Leads (or EM) |

### 4.2 Типичные конфликты

**"PM давит на сроки":**
```

PM: "Нужно сделать к пятнице"
TL: "Это невозможно качественно"

Решение:

- Объясните технические constraints
- Предложите варианты (scope cut, phased delivery)
- Escalate если нет согласия

```

**"PM не понимает technical complexity":**
```

Решение:

- Объясняйте в бизнес-терминах
- Используйте аналогии
- Показывайте риски для пользователей

```

**"PM микроменеджит команду":**
```

Решение:

- Обсудите роли и границы
- Предложите альтернативы (status updates)
- Escalate к общему руководителю если нужно

```

### 4.3 Эффективное партнёрство

**Что работает:**

- Регулярные sync (2-3 раза в неделю)
- Aligned на goals
- Честность о рисках и проблемах
- Mutual respect

**Формат sync:**
```

Weekly PM-TL Sync (30 min)

1. Progress review (10 min)
2. Risks and blockers (10 min)
3. Upcoming decisions (5 min)
4. Stakeholder communications (5 min)

```

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

- **Роли не titles:** Важнее agreements о responsibilities, чем названия

- **TL часто = delivery:** Особенно в маленьких командах

- **Partnership с PM:** Честность, регулярные sync, mutual respect

- **Scope management:** Каждое изменение имеет cost

- **Risks — ваша работа:** Выявлять, коммуницировать, mitigation

---

## 🚀 Next Steps

**Related Modules:**

- [07_TeamProcesses](../07_TeamProcesses/) — процессы для delivery
- [08_Meetings](../08_Meetings/) — planning и coordination meetings

**Practice Ideas:**

1. Составьте RACI матрицу для вашей команды
2. Создайте risk register для текущего проекта
3. Попробуйте weekly status update формат

**Going Deeper:**

- Agile project management
- Risk management frameworks
- Stakeholder management techniques

---

## 📚 Additional Resources

**Books:**

- "The Mythical Man-Month" by Fred Brooks — классика о software projects
- "Making Things Happen" by Scott Berkun — PM perspective
- "User Story Mapping" by Jeff Patton — scope management

**Articles:**

- [Atlassian: RACI Matrix](https://www.atlassian.com/team-playbook/plays/raci)
- [Product vs Project Management](https://www.productplan.com/glossary/product-manager-vs-project-manager/)

**Frameworks:**

- RACI (Responsible, Accountable, Consulted, Informed)
- MoSCoW (Must, Should, Could, Won't)
- RICE scoring (Reach, Impact, Confidence, Effort)

---




