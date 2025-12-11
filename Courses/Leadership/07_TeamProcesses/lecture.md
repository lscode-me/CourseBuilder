# Построение процессов в команде
## От хаоса к системе

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать роль Team Lead / Engineering Manager
- Иметь базовое представление о Agile/Scrum
- Работать в команде разработки

**Recommended prior modules:**

- [01_Transition](../01_Transition/) — переход в лидерство

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять, какие процессы нужны команде
- Внедрять процессы постепенно без сопротивления
- Создавать эффективные workflows для разных активностей
- Документировать и поддерживать процессы живыми
- Балансировать между порядком и гибкостью

---

## 1. Зачем нужны процессы

### 1.1 Процессы как инфраструктура

> **💡 Key Insight:**  
> Хорошие процессы — как инфраструктура: невидимы, когда работают, и заметны, когда ломаются.

**Без процессов:**

- Каждый делает по-своему
- Нет предсказуемости
- Знания в головах людей
- Зависимость от ключевых людей
- Много ручной координации

**С правильными процессами:**

- Предсказуемость результатов
- Знания документированы
- Новые люди быстрее онбордятся
- Меньше ошибок
- Меньше overhead на координацию

### 1.2 Опасность чрезмерных процессов

```

          Хаос ←───────────────────────────────► Бюрократия
            │                                       │
     Нет процессов                           Слишком много
     • Непредсказуемо                        • Медленно
     • Нет standards                         • Frustration
     • Зависимость от людей                  • Creativity убита
                               │
                               │
                        ┌──────┴──────┐
                        │   Баланс    │
                        │             │
                        │ Минимально  │
                        │ достаточно  │
                        └─────────────┘

```

> **⚠️ Warning:**  
> Процесс ради процесса — вред. Каждый процесс должен решать конкретную проблему.

### 1.3 Принципы хороших процессов

1. **Solve real problems** — решает реальную, а не гипотетическую проблему
2. **Minimal viable process** — минимум, который работает
3. **Observable** — легко понять, соблюдается ли
4. **Evolvable** — можно улучшать с опытом
5. **Documented** — записан, а не "все знают"

---

## 2. Категории процессов

### 2.1 Development Processes

**Работа с кодом:**

- Code review workflow
- Branching strategy
- CI/CD pipeline
- Testing requirements
- Release process

**Пример: Code Review Process:**
```markdown
## Code Review Policy

### When PR is Ready:

- [ ] All tests pass
- [ ] Self-review completed
- [ ] Description explains WHY, not just WHAT

### Review Requirements:

- 1 approval required (2 for critical paths)
- Review within 24h
- No "LGTM" without reading code

### Merge Policy:

- Squash and merge
- Author merges after approval
- Delete branch after merge

```

### 2.2 Planning Processes

**Работа с задачами:**

- Sprint planning
- Backlog grooming
- Estimation
- Prioritization
- Roadmap updates

### 2.3 Communication Processes

**Командная коммуникация:**

- Standup format
- Status updates
- Escalation paths
- Cross-team sync
- Documentation practices

### 2.4 Operational Processes

**Поддержка production:**

- On-call rotation
- Incident response
- Post-mortem process
- Monitoring alerts
- Deployment checklist

---

## 3. Внедрение процессов

### 3.1 Framework для внедрения

```

1. IDENTIFY  — Найти проблему
2. DESIGN    — Спроектировать решение  
3. PILOT     — Попробовать на части команды
4. ITERATE   — Улучшить по feedback
5. ROLL OUT  — Внедрить полностью
6. MAINTAIN  — Поддерживать и эволюционировать

```

### 3.2 Identify: Найти проблему

**Как находить проблемы:**

- Retro: "Что мешает работать?"
- 1-on-1: "Какие процессы фрустрируют?"
- Наблюдение: Где происходят ошибки?
- Данные: Где bottlenecks в метриках?

**Не внедряйте процесс без проблемы:**
```

❌ "В Google так делают"
❌ "Я прочитал в книге"
❌ "Может пригодиться"

✅ "Мы 3 раза за месяц сломали prod из-за X"
✅ "Команда жалуется на Y"
✅ "Мы тратим Z часов на ручную работу"

```

### 3.3 Design: Спроектировать решение

**Принципы дизайна:**

1. **Start small**
   - Минимальный набор правил
   - Можно добавить позже

2. **Involve the team**
   - Обсудите с командой
   - Учтите их input
   - Ownership важен для adoption

3. **Be explicit**
   - Чёткие критерии
   - Примеры хорошего/плохого
   - Документация

### 3.4 Pilot: Попробовать

**Зачем pilot:**

- Найти проблемы до полного rollout
- Собрать feedback
- Скорректировать процесс

**Как делать pilot:**
```

1. Выберите 1-2 человека / один проект
2. Договоритесь о периоде (2-4 недели)
3. Собирайте feedback регулярно
4. Документируйте issues и изменения

```

### 3.5 Iterate и Roll Out

**После pilot:**

1. Соберите feedback от участников
2. Внесите изменения
3. Если серьёзные проблемы — ещё один pilot
4. Если minor — rollout на всю команду

**При rollout:**

- Объясните зачем (контекст проблемы)
- Покажите, как это решает проблему
- Обеспечьте training/documentation
- Определите ответственного
- Запланируйте первый review

### 3.6 Maintain: Поддерживать

**Процессы умирают, если:**

- Никто не следит за соблюдением
- Не обновляются при изменении контекста
- Нет owner'а

**Maintenance practices:**

- Регулярный review (quarterly)
- Update при изменениях
- Удаление устаревших процессов

---

## 4. Ключевые процессы команды

### 4.1 Code Review Process

**Цели:**

- Качество кода
- Knowledge sharing
- Найти баги до production

**Элементы процесса:**
```markdown
## Code Review Guidelines

### Author Checklist:

- [ ] Tests written and passing
- [ ] Self-review done
- [ ] PR description complete
- [ ] Related ticket linked

### Reviewer Checklist:

- [ ] Understand the context
- [ ] Check logic and edge cases
- [ ] Verify tests cover changes
- [ ] Leave actionable comments

### SLA:

- Initial review: 4 hours (business hours)
- Follow-up: 2 hours

### Approval Requirements:

- 1 approval for features
- 2 approvals for critical paths

```

### 4.2 Release Process

**Элементы:**
```markdown
## Release Process

### Pre-release:

1. All PRs merged to main
2. All tests green
3. Changelog updated
4. Version bumped

### Release Steps:

1. Create release branch
2. Run full test suite
3. Deploy to staging
4. Smoke test on staging
5. Get approval from QA
6. Deploy to production
7. Monitor for 30 minutes
8. Announce in #releases

### Rollback Trigger:

- Error rate > 1%
- P1 bug discovered
- Performance degradation > 20%

```

### 4.3 Incident Response

**Элементы:**
```markdown
## Incident Response Process

### Severity Levels:

- P1: Production down, all users affected
- P2: Major feature broken, many users affected
- P3: Minor issue, workaround exists
- P4: Cosmetic, no impact

### Response Times:
| Severity | Response | Resolution Target |
|----------|----------|-------------------|
| P1 | 15 min | 4 hours |
| P2 | 1 hour | 24 hours |
| P3 | 4 hours | 1 week |
| P4 | 1 day | As scheduled |

### Incident Flow:

1. Detect → Alert fires or user report
2. Triage → Assess severity
3. Communicate → Status page, Slack
4. Mitigate → Stop bleeding
5. Fix → Root cause resolution
6. Post-mortem → Learn and prevent

```

### 4.4 On-call Rotation

**Элементы:**
```markdown
## On-call Policy

### Rotation:

- Weekly rotation
- Primary + Secondary on-call
- Handoff: Monday 10:00 AM

### Expectations:

- Response within 15 minutes for P1
- Laptop and internet access required
- No need to be at desk, but reachable

### Compensation:

- [определяется политикой компании]

### Handoff Template:

- Active issues
- Recent deployments
- Upcoming changes
- Known fragile areas

```

### 4.5 Documentation Process

**Принципы:**
```markdown
## Documentation Guidelines

### What to Document:

- Architecture decisions (ADRs)
- Runbooks for operations
- API contracts
- Onboarding guides
- Process descriptions

### Where:

- Architecture: /docs/architecture/
- Runbooks: /docs/runbooks/
- API: Generated from code
- Processes: Confluence/Notion

### When to Update:

- With every significant change
- Owner responsible for keeping current
- Quarterly review of key docs

### Documentation Quality:

- Answer: Why, What, How
- Include examples
- Keep up to date (or delete)

```

---

## 5. Agile в контексте процессов

### 5.1 Scrum Ceremonies

**Sprint Planning:**
```

Частота: Начало каждого спринта
Длительность: 2-4 часа (для 2-недельного спринта)
Участники: Team + PO
Output: Sprint backlog

```

**Daily Standup:**
```

Частота: Ежедневно
Длительность: 15 минут max
Формат: What did / What will / Blockers
Output: Awareness, unblock

```

**Sprint Review (Demo):**
```

Частота: Конец спринта
Длительность: 1-2 часа
Участники: Team + Stakeholders
Output: Feedback, acceptance

```

**Sprint Retrospective:**
```

Частота: Конец спринта
Длительность: 1-1.5 часа
Участники: Team only
Output: Action items for improvement

```

### 5.2 Kanban альтернатива

**Когда Kanban лучше:**

- Support / maintenance команды
- Непредсказуемый поток работы
- Команды, не готовые к timeboxed sprints

**Ключевые практики:**

- Visualize workflow
- Limit Work in Progress (WIP)
- Measure flow (lead time, throughput)

### 5.3 Hybrid подходы

**Scrumban:**

- Sprints для planning
- Kanban для execution
- WIP limits
- Continuous flow

---

## 6. Работа с сопротивлением

### 6.1 Почему люди сопротивляются

**Причины:**

- "Раньше работало без этого"
- "Это замедлит нашу работу"
- "Не понимаю зачем"
- "Слишком много бюрократии"
- "Нам не доверяют"

### 6.2 Как преодолевать

**Involve early:**
```

❌ "Мы решили, теперь делаем так"
✅ "У нас проблема X. Какие идеи есть у команды?"

```

**Show the problem:**
```

❌ "Нужен процесс code review"
✅ "Мы 3 раза сломали prod. Давайте разберём, как избежать"

```

**Start small:**
```

❌ "Вот 20 новых правил с сегодняшнего дня"
✅ "Попробуем одно изменение на 2 недели"

```

**Measure and share:**
```

❌ "Верьте, это работает"
✅ "После внедрения количество багов снизилось на 30%"

```

### 6.3 Что делать с chronic resisters

1. **1-on-1 разговор:** Понять root cause сопротивления
2. **Address concerns:** Возможно, есть valid points
3. **Set expectations:** Процессы — часть работы команды
4. **Follow through:** Consistency важна

---

## 7. Метрики процессов

### 7.1 Зачем измерять

- Понимать, работает ли процесс
- Находить bottlenecks
- Обосновывать изменения
- Tracking improvement

### 7.2 Примеры метрик

**Code Review:**

- Time to first review
- Time to merge
- Number of review rounds
- Review comments per PR

**Delivery:**

- Lead time (idea → production)
- Deployment frequency
- Change failure rate
- Time to restore

**Quality:**

- Bug escape rate
- Production incidents
- Test coverage
- Technical debt metrics

### 7.3 DORA Metrics

**Four Key Metrics (DORA):**

| Metric | Definition | Elite | Low |
|--------|------------|-------|-----|
| Deployment Frequency | Как часто деплоим | Multiple/day | Monthly |
| Lead Time | Commit → Production | < 1 hour | 1-6 months |
| Change Failure Rate | % деплоев с issues | 0-15% | 46-60% |
| Time to Restore | Время восстановления | < 1 hour | 1-6 months |

---

## 8. Эволюция процессов

### 8.1 Process Review

**Quarterly review:**
```markdown
## Process Review Template

### Process: [название]
### Date: [дата]
### Owner: [имя]

### What's working well:

- [пункт 1]
- [пункт 2]

### What's not working:

- [пункт 1]
- [пункт 2]

### Proposed changes:

- [изменение 1]
- [изменение 2]

### Decision: Keep / Modify / Remove
```

### 8.2 Удаление процессов

**Когда удалять:**

- Проблема, которую решал, больше не существует
- Никто не следует
- Overhead превышает benefit
- Есть лучший способ

**Как удалять:**

1. Announce deprecation
2. Set sunset date
3. Remove and update docs

### 8.3 Scaling процессов

**По мере роста команды:**

- Процессы становятся формальнее
- Больше документации
- Больше automation
- Sub-teams могут иметь variations

---

## 💡 Key Takeaways

- **Solve real problems:** Не внедряйте процесс без проблемы

- **Minimal viable process:** Меньше правил = больше compliance

- **Involve the team:** Ownership через участие в создании

- **Iterate:** Процессы должны эволюционировать

- **Measure:** Без метрик не понять, работает ли процесс

---

## 🚀 Next Steps

**Related Modules:**

- [08_Meetings](../08_Meetings/) — эффективные митинги как процесс
- [09_ProjectManagement](../09_ProjectManagement/) — delivery процессы

**Practice Ideas:**

1. Проведите audit процессов в команде: какие есть, какие нужны?
2. Выберите одну проблему и спроектируйте процесс по framework
3. Запланируйте quarterly process review

**Going Deeper:**

- DORA metrics и DevOps practices
- Lean и Theory of Constraints
- Process automation tools

---

## 📚 Additional Resources

**Books:**

- "Accelerate" by Nicole Forsgren — DORA metrics
- "The Phoenix Project" by Gene Kim — DevOps как процесс
- "Team Topologies" by Matthew Skelton — команды и процессы

**Articles:**

- [DORA Research](https://dora.dev/research/)
- [Atlassian: Team Playbook](https://www.atlassian.com/team-playbook)

**Tools:**

- Jira, Linear, Asana — project management
- GitHub/GitLab — code review workflows
- PagerDuty, Opsgenie — incident management

---




