# Staff Engineering
## Путь технического лидерства без управления людьми

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать различия между IC и Management треками (модуль 02)
- Иметь опыт работы Senior Engineer
- Интересоваться путём технического лидерства

**Recommended prior modules:**

- [02_CareerTracks](../02_CareerTracks/) — IC vs Management: выбор пути

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать роль и обязанности Staff Engineer
- Различать архетипы Staff Engineers и их сильные стороны
- Развивать навыки, необходимые для перехода на Staff уровень
- Демонстрировать Staff-level impact в повседневной работе
- Создавать visibility своей работы для продвижения

---

## 1. Что такое Staff Engineer

### 1.1 Определение роли

Staff Engineer — это технический лидер, который:

- Решает проблемы, выходящие за рамки одной команды
- Определяет технические стандарты и практики
- Влияет на технологическую стратегию организации
- Менторит Senior Engineers

> **💡 Key Insight:**  
> Staff Engineer — не "очень хороший Senior Engineer". Это качественно другая роль с другим scope влияния.

### 1.2 Staff vs Senior: ключевые различия

| Аспект | Senior Engineer | Staff Engineer |
|--------|-----------------|----------------|
| Scope | Команда | Несколько команд / Area |
| Решения | Тактические | Стратегические |
| Код | Много, в одном проекте | Меньше, cross-team |
| Влияние | Через свой код | Через код других |
| Проблемы | Определённые | Ambiguous |
| Stakeholders | Команда, PM | Директора, VP |

### 1.3 Формула Staff-level impact

```

Staff Impact = Technical Depth × Scope × Influence

```

**Technical Depth** — насколько глубоко вы понимаете технологии
**Scope** — насколько широко ваши решения влияют на организацию  
**Influence** — насколько эффективно вы можете убедить других следовать

Все три фактора должны быть высокими.

---

## 2. Четыре архетипа Staff Engineers

Will Larson выделяет четыре архетипа. Большинство Staff Engineers — комбинация нескольких архетипов.

### 2.1 Tech Lead

**Описание:**

- Партнёрство с Engineering Manager команды
- Владение технической стратегией проекта/продукта
- 50-70% времени в одной команде

**Характерные активности:**

- Принятие технических решений для команды
- Code review и стандарты качества
- Technical mentoring членов команды
- Планирование технических работ
- Разблокирование технических препятствий

**Подходит, если:**

- Вам нравится глубоко погружаться в один продукт
- Вы хотите видеть результат своих решений
- Вам важен баланс coding/leadership

**Пример дня:**
```

09:00-10:00  Code review PR от команды
10:00-11:00  Technical design discussion
11:00-12:00  Coding (critical path)
12:00-13:00  Lunch
13:00-14:00  1-on-1 с junior engineer
14:00-16:00  Deep work: architecture document
16:00-17:00  Sync с EM команды
17:00-18:00  Отвечаю на технические вопросы

```

### 2.2 Architect

**Описание:**

- Фокус на дизайне и архитектуре систем
- Работа с критичными, масштабными системами
- Меньше кода, больше документов и спецификаций

**Характерные активности:**

- Написание Architecture Decision Records (ADR)
- Design review для нескольких команд
- Технические спецификации и RFC
- Прототипирование архитектурных решений
- Evaluation технологий и инструментов

**Подходит, если:**

- Вам нравится думать о системах в целом
- Вы умеете балансировать trade-offs
- Вы можете объяснять сложные концепции простыми словами

**Пример дня:**
```

09:00-10:30  Работа над RFC: новая система кэширования
10:30-11:30  Architecture review для Team A
11:30-12:30  Lunch
12:30-14:00  Design doc: migration plan
14:00-15:00  Meeting с vendors (оценка технологий)
15:00-16:00  1-on-1 с senior engineer
16:00-18:00  Прототип нового подхода

```

### 2.3 Solver

**Описание:**

- Решает самые сложные технические проблемы
- Перемещается между командами по мере необходимости
- Глубокая экспертиза в специфических областях

**Характерные активности:**

- "Тушение пожаров" — критичные инциденты
- Debugging сложнейших проблем
- Оптимизация производительности
- Due diligence для M&A
- Миграции и большие технические проекты

**Подходит, если:**

- Вам нравится разнообразие проблем
- Вы любите глубоко погружаться в неизвестное
- Вас не пугает хаос и неопределённость

**Пример дня:**
```

09:00-10:00  Investigation: production issue
10:00-11:30  Deep dive в код Team B
11:30-12:30  Lunch
12:30-14:00  Pair programming с Team C на сложной проблеме
14:00-15:00  Writing postmortem
15:00-17:00  Coding: fix + tests
17:00-18:00  Handoff и документация

```

### 2.4 Right Hand

**Описание:**

- "Правая рука" VP/Director of Engineering
- Делегированное лидерство организационных инициатив
- Проекты с высоким организационным impact

**Характерные активности:**

- Лидирование cross-organizational инициатив
- Представление технической организации
- Организационные изменения с технической стороны
- Помощь в принятии решений на уровне VP

**Подходит, если:**

- Вы умеете работать с неопределённостью
- Вам комфортно в политической среде
- Вы понимаете бизнес, а не только технологии

**Пример дня:**
```

09:00-10:00  1-on-1 с VP Engineering
10:00-11:00  Cross-team sync по initiative X
11:00-12:00  Подготовка presentation для executives
12:00-13:00  Lunch с engineering leads
13:00-15:00  Working session по org restructure
15:00-16:00  Interview debrief
16:00-17:00  Writing: proposal для initiative Y
17:00-18:00  Follow-ups и communication

```

### 2.5 Выбор архетипа

```

Что вам нравится больше?
    │
    ├─ Глубокая работа в одном продукте → TECH LEAD
    │
    ├─ Думать о системах целиком → ARCHITECT
    │
    ├─ Решать разнообразные сложные проблемы → SOLVER
    │
    └─ Организационное влияние → RIGHT HAND

```

> **💡 Pro Tip:**  
> Не пытайтесь быть всеми архетипами. Выберите 1-2 и станьте лучшим в них.

---

## 3. Навыки Staff Engineer

### 3.1 Technical Skills (необходимые, но недостаточные)

**Глубокая экспертиза:**

- Знание систем "под капотом"
- Debugging на любом уровне стека
- Понимание производительности и масштабирования

**Широкий кругозор:**

- Awareness о смежных технологиях
- Способность учиться новому быстро
- Понимание trade-offs разных подходов

### 3.2 Communication Skills (критичные)

**Writing:**

- Design documents и RFC
- Technical specs и ADRs
- Post-mortems и documentation
- Emails и Slack для influence

> **💡 Key Insight:**  
> На Staff уровне ваши документы читают больше людей, чем ваш код. Writing — ключевой навык.

**Speaking:**

- Презентации для разных аудиторий
- Technical discussions и debates
- Объяснение сложного простым языком
- Влияние без авторитета

### 3.3 Leadership Skills

**Influence without authority:**

- Вы не управляете людьми, но влияете на них
- Убеждение через логику и expertise
- Building coalitions

**Mentoring:**

- Развитие Senior Engineers
- Code review как обучение
- Sharing знаний

**Organizational awareness:**

- Понимание политики компании
- Знание stakeholders и их интересов
- Навигация в сложных организациях

### 3.4 Strategic Thinking

**Big picture:**

- Понимание бизнес-целей
- Alignment технических решений с бизнесом
- Долгосрочное мышление

**Prioritization:**

- Фокус на important, не urgent
- Saying "no" нерелевантным запросам
- Time management для high-impact работы

---

## 4. Путь к Staff Level

### 4.1 Gap Analysis

**Оцените себя:**

| Skill | Junior | Senior | Staff | Ваш уровень |
|-------|--------|--------|-------|-------------|
| Technical depth | Basic | Good | Expert | ? |
| Scope of impact | Task | Feature | Area | ? |
| Writing | Reports | Docs | RFCs | ? |
| Speaking | 1-on-1 | Team | Org | ? |
| Mentoring | No | Juniors | Seniors | ? |
| Strategic thinking | No | Some | Yes | ? |

### 4.2 Staff Project

**Что это:**
"Staff Project" — проект, который демонстрирует Staff-level impact.

**Характеристики:**

- Cross-team scope
- Significant business impact
- Technical complexity
- Требует leadership без authority
- Visibility в организации

**Примеры Staff Projects:**

- Миграция на новую инфраструктуру
- Внедрение нового технического стандарта
- Performance optimization с измеримым impact
- Создание внутренней платформы
- Архитектурная эволюция системы

### 4.3 Создание Visibility

**Проблема:** На Staff уровне ваша работа менее "видима", чем код Junior/Senior.

**Решения:**

**Writing:**

- Публикуйте внутренние blog posts
- Документируйте принятые решения
- Отправляйте weekly updates stakeholders

**Speaking:**

- Выступайте на внутренних tech talks
- Участвуйте в architecture review meetings
- Представляйте проекты на all-hands

**Networking:**

- Знакомьтесь с людьми из других команд
- Участвуйте в cross-team initiatives
- Будьте helpful — помогайте другим командам

### 4.4 Promotion Process

**Preparation (6-12 месяцев до):**

1. Поговорите с менеджером о ожиданиях
2. Изучите Staff expectations в вашей компании
3. Определите gaps в навыках
4. Начните Staff Project

**Execution (ongoing):**

1. Документируйте свой impact
2. Собирайте feedback от stakeholders
3. Просите sponsorship от senior leaders
4. Демонстрируйте consistent Staff-level work

**Promotion packet:**

- Summary вашего impact
- Примеры Staff-level работы
- Testimonials от peers и stakeholders
- Метрики (если применимо)

---

## 5. Day-to-day работа Staff Engineer

### 5.1 Как распределяется время

**Типичное распределение:**

```

┌─────────────────────────────────────────────────────────┐
│ Coding/Hands-on Technical Work          │ 30-40%       │
├─────────────────────────────────────────────────────────┤
│ Design/Review/Writing                   │ 20-30%       │
├─────────────────────────────────────────────────────────┤
│ Meetings/Communication                  │ 15-25%       │
├─────────────────────────────────────────────────────────┤
│ Mentoring                               │ 10-15%       │
├─────────────────────────────────────────────────────────┤
│ Learning/Exploration                    │ 5-10%        │
└─────────────────────────────────────────────────────────┘

```

### 5.2 Типы встреч

**Technical:**

- Architecture review
- Design discussions
- Code review sync
- Tech debt prioritization

**Strategic:**

- Roadmap planning
- Cross-team coordination
- Stakeholder alignment

**People:**

- Mentoring sessions
- 1-on-1 с менеджером
- Interview debriefs

### 5.3 Что НЕ делает Staff Engineer

- ❌ Не берёт на себя всю работу команды
- ❌ Не решает все проблемы лично
- ❌ Не игнорирует organizational dynamics
- ❌ Не изолируется от бизнеса
- ❌ Не отказывается от communication

---

## 6. Working with Engineering Managers

### 6.1 Partnership Model

Staff Engineer и Engineering Manager — партнёры, не конкуренты.

```

          ┌─────────────────────────────────────┐
          │           SHARED GOALS              │
          │   Team Success / Delivery / Growth  │
          └─────────────────────────────────────┘
                    ▲               ▲
                    │               │
    ┌───────────────┴───┐     ┌─────┴───────────────┐
    │   STAFF ENGINEER  │     │ ENGINEERING MANAGER │
    │                   │     │                     │
    │ ✓ Technical       │     │ ✓ People            │
    │ ✓ Architecture    │     │ ✓ Process           │
    │ ✓ Code quality    │     │ ✓ Career growth     │
    │ ✓ Tech standards  │     │ ✓ Hiring            │
    └───────────────────┘     └─────────────────────┘

```

### 6.2 Разделение ответственности

| Область | Staff Engineer | Engineering Manager |
|---------|---------------|---------------------|
| Технические решения | Leads | Supports |
| Hiring: tech assessment | Leads | Supports |
| Hiring: culture fit | Supports | Leads |
| Performance: tech | Leads | Integrates |
| Performance: overall | Input | Leads |
| Career growth | Tech mentoring | Career coaching |
| Team process | Tech aspects | Overall process |
| Delivery | Tech planning | Overall planning |

### 6.3 Communication Patterns

**Регулярные sync:**

- Еженедельный 1-on-1 со своим менеджером
- Регулярный sync с EM команды (если Tech Lead)

**Topics для обсуждения:**

- Technical risks и blockers
- People concerns (анонимизированно)
- Strategic direction
- Cross-team dependencies

---

## 7. Common Challenges

### 7.1 "Я скучаю по коду"

**Проблема:** На Staff уровне меньше времени на coding.

**Решения:**

- Выделяйте protected time для coding
- Выбирайте высоко-impact coding tasks
- Используйте prototyping для exploration
- Code review как способ оставаться в коде

### 7.2 "Моя работа невидима"

**Проблема:** Impact Staff работы сложнее измерить.

**Решения:**

- Документируйте всё
- Собирайте testimonials
- Связывайте работу с бизнес-метриками
- Регулярно сообщайте о progress

### 7.3 "Я не знаю, над чем работать"

**Проблема:** Нет чёткого assignment, как у IC.

**Решения:**

- Ищите high-impact проблемы сами
- Спрашивайте leadership о болях
- Слушайте жалобы других команд
- Используйте framework:

```

1. Какие проблемы мешают нескольким командам?
2. Какие технические решения принимаются неправильно?
3. Где организация "стреляет себе в ногу"?
4. Какие стратегические инициативы нуждаются в tech leadership?

```

### 7.4 "Я не могу заставить людей делать правильно"

**Проблема:** Influence without authority сложно.

**Решения:**

- Слушайте concerns других
- Показывайте data и evidence
- Начинайте с маленьких wins
- Находите allies и champions
- Будьте терпеливы — изменения требуют времени

---

## 8. Staff Engineer в разных компаниях

### 8.1 Startup (< 50 человек)

**Особенности:**

- Роль может быть неформальной
- Scope охватывает всю компанию
- Много hands-on coding
- Меньше процессов

**Focus:**

- Technical foundations
- Scaling systems
- Building team practices

### 8.2 Growth Company (50-500 человек)

**Особенности:**

- Формализация Staff роли
- Появление специализации (архетипов)
- Balance coding и leadership
- Cross-team coordination important

**Focus:**

- Technical standards
- Platform/infrastructure work
- Mentoring growing team

### 8.3 Enterprise (500+ человек)

**Особенности:**

- Чёткие expectations и ladders
- Больше organizational work
- Меньше coding
- Political navigation important

**Focus:**

- Strategic initiatives
- Organizational influence
- Long-term architecture

---

## 💡 Key Takeaways

- **Качественно другая роль**: Staff — не "super Senior", это смена scope и типа работы

- **Четыре архетипа**: Tech Lead, Architect, Solver, Right Hand — выберите свой

- **Communication критичен**: Writing и speaking важнее, чем pure coding

- **Influence without authority**: Убеждайте через expertise, не через power

- **Visibility важна**: Документируйте и делитесь своей работой

---

## 🚀 Next Steps

**Related Modules:**

- [02_CareerTracks](../02_CareerTracks/) — IC vs Management: контекст выбора
- [07_TeamProcesses](../07_TeamProcesses/) — процессы, которые Staff часто внедряет

**Practice Ideas:**

1. Определите свой архетип (или комбинацию)
2. Найдите потенциальный Staff Project в вашей организации
3. Начните вести "brag document" — записывайте свой impact

**Going Deeper:**

- Writing RFCs и Design Documents
- Organizational dynamics и political navigation
- Technical strategy development

---

## 📚 Additional Resources

**Books:**

- "Staff Engineer" by Will Larson — главная книга по теме
- "The Staff Engineer's Path" by Tanya Reilly
- "Thinking in Systems" by Donella Meadows

**Websites:**

- [StaffEng.com](https://staffeng.com/) — истории Staff Engineers
- [LeadDev](https://leaddev.com/) — статьи о technical leadership

**Articles:**

- [Will Larson: Staff Engineer Archetypes](https://staffeng.com/guides/staff-archetypes)
- [Gergely Orosz: What Staff Engineers Actually Do](https://blog.pragmaticengineer.com/)
- [Tanya Reilly: Being Glue](https://noidea.dog/glue)

**Podcasts:**

- [StaffEng Podcast](https://staffeng.com/podcast)
- [Software Engineering Daily](https://softwareengineeringdaily.com/)

---




