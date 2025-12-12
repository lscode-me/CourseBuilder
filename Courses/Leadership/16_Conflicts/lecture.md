# Конфликты и сложные ситуации
## Типы конфликтов, разрешение и сложные разговоры

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь давать feedback (модуль 05)
- Проводить 1-on-1 (модуль 04)
- Понимать командную динамику

**Recommended prior modules:**

- [05_Feedback](../05_Feedback/) — feedback culture
- [11_Communication](../11_Communication/) — коммуникация

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Распознавать типы конфликтов
- Применять frameworks для разрешения конфликтов
- Вести сложные разговоры эффективно
- Медиировать конфликты между членами команды
- Управлять конфликтами с stakeholders

---

## 1. Понимание конфликтов

### 1.1 Конфликт — не всегда плохо

> **💡 Key Insight:**  
> Здоровый конфликт (о идеях) = innovation. Нездоровый конфликт (о людях) = dysfunction.

**Матрица конфликтов:**

```
              КОНСТРУКТИВНЫЙ                  ДЕСТРУКТИВНЫЙ
              ──────────────                  ─────────────
Фокус:        Идеи, проблемы                  Люди, личности
Результат:    Лучшие решения                  Разрушение отношений
Эмоции:       Controlled passion              Anger, resentment
Поведение:    Debate, challenge               Attack, blame
После:        Commitment                       Avoidance
```

**Примеры конструктивного конфликта:**

| Ситуация | Что происходит | Результат |
|----------|----------------|-----------|
| Дебаты о технологии | Два senior'а аргументируют разные подходы | Лучшее решение, обе стороны учатся |
| Оспаривание assumptions | "А почему мы считаем, что это нужно?" | Проверка product direction |
| Design review | Критика архитектуры с конкретными concerns | Улучшенный design |
| Pre-mortem | "Что может пойти не так?" | Risk mitigation |

**Примеры деструктивного конфликта:**

| Ситуация | Что происходит | Последствия |
|----------|----------------|-------------|
| Личные атаки | "Ты некомпетентен" | Разрушение trust, уход человека |
| Blame culture | "Это твоя вина" | Скрытие ошибок, страх |
| Passive-aggression | Молчание, сарказм, sabotage | Toxic atmosphere |
| Избегание | Замалчивание проблем | Накопление resentment, explosion |

### 1.2 Три типа конфликтов

**Type 1: Task Conflict (о работе)**

| Характеристика | Описание |
|----------------|----------|
| О чём | Разногласия о решениях, подходах, приоритетах |
| Примеры | "Какую технологию выбрать?", "Какой scope MVP?" |
| Impact | Может быть **полезен** — приводит к лучшим решениям |
| Риск | Может escalate в relationship conflict если не managed |
| Действие | Поощряйте, но модерируйте |

**Type 2: Relationship Conflict (о людях)**

| Характеристика | Описание |
|----------------|----------|
| О чём | Межличностные tensions, personality clashes |
| Примеры | "Я не могу с ним работать", "Он меня бесит" |
| Impact | **Всегда негативен** — разрушает команду |
| Риск | Распространяется, втягивает других |
| Действие | Решайте быстро и decisively |

**Type 3: Process Conflict (о процессе)**

| Характеристика | Описание |
|----------------|----------|
| О чём | Как делать работу, кто за что отвечает |
| Примеры | "Кто должен делать code review?", "Зачем нам этот митинг?" |
| Impact | Может быть **полезен** — улучшает процессы |
| Риск | Может маскировать relationship conflict |
| Действие | Clarify expectations, document decisions |

### 1.3 Sources конфликтов

**Почему возникают конфликты:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOURCES OF CONFLICT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  RESOURCE SCARCITY                 COMMUNICATION                │
│  ─────────────────                 ─────────────                │
│  • Конкуренция за headcount        • Misunderstandings          │
│  • Приоритизация проектов          • Information gaps           │
│  • Budget allocation               • Different styles           │
│  • Shared resources (oncall,       • Cultural differences       │
│    environments)                   • Remote miscommunication    │
│                                                                 │
│  GOALS & INCENTIVES                PERSONALITIES                │
│  ─────────────────                 ─────────────                │
│  • Misaligned OKRs                 • Working style differences  │
│  • Individual vs team goals        • Value conflicts            │
│  • Short-term vs long-term         • Past history               │
│  • Department silos                • Ego, status                │
│                                                                 │
│  ORGANIZATIONAL                    CHANGE                       │
│  ─────────────────                 ─────────────                │
│  • Unclear roles/responsibilities  • New manager                │
│  • Power struggles                 • Reorg                      │
│  • Political environment           • Strategy shift             │
│  • Lack of process                 • Growth pains               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.4 Конфликт Escalation Model

**Стадии escalation:**

```
Stage 1: DISAGREEMENT (Healthy)
├── Разные мнения
├── Debate о идеях
└── → Resolution: discussion, decision

Stage 2: TENSION (Warning)
├── Эмоции включаются
├── Позиции hardened
├── → Resolution: mediation, facilitation

Stage 3: CONFLICT (Problem)
├── Личные атаки
├── Третьи стороны втягиваются
├── → Resolution: intervention, separation

Stage 4: CRISIS (Urgent)
├── Open hostility
├── Work stops
├── → Resolution: management intervention, HR

Stage 5: BREAKDOWN (Critical)
├── Relationship destroyed
├── Impossible to work together
├── → Resolution: separation (transfer, exit)
```

> **⚠️ Warning:**  
> Чем раньше вмешаетесь, тем легче решить. Stage 1-2 решаете вы, Stage 3+ требует эскалации.

---

## 2. Conflict Resolution Framework

### 2.1 Thomas-Kilmann Model

**Пять стилей разрешения конфликтов:**

```
                    High
          ASSERTIVENESS
                     │
        COMPETING    │    COLLABORATING
        (Win-Lose)   │    (Win-Win)
        "My way"     │    "Our way"
                     │
               ┌─────┼─────┐
               │COMPROMISING│
               │ (Split)    │
               │ "Halfway"  │
               └─────┼─────┘
                     │
       AVOIDING      │    ACCOMMODATING
       (Lose-Lose)   │    (Lose-Win)
       "No way"      │    "Your way"
                     │
                    Low
         ─────────────────────────────────
         Low    COOPERATIVENESS      High
```

**Детальное описание каждого стиля:**

| Стиль | Описание | Фраза | Когда использовать |
|-------|----------|-------|-------------------|
| **Collaborating** | Win-Win: находим решение для обоих | "Давай найдём решение вместе" | Важные issues, есть время, нужен commitment |
| **Competing** | Win-Lose: настаиваю на своём | "Я принял решение" | Crisis, quick decision, unpopular but necessary |
| **Compromising** | Split: каждый уступает | "Давай разделим пополам" | Moderate importance, equal power, deadline |
| **Avoiding** | No engagement: откладываю | "Давай обсудим позже" | Trivial issue, need to cool down, can't win |
| **Accommodating** | Yield: уступаю | "Хорошо, сделаем по-твоему" | You're wrong, relationship > issue, goodwill |

**Примеры применения:**

| Ситуация | Лучший стиль | Почему |
|----------|--------------|--------|
| Критическая production issue | **Competing** | Нет времени на дискуссию |
| Выбор технологии для core system | **Collaborating** | Важное решение, нужен buy-in |
| Спор о дате отпуска | **Compromising** | Moderate importance, можно split |
| Коллега в плохом настроении | **Avoiding** | Лучше подождать, когда успокоится |
| Вы были неправы | **Accommodating** | Признайте и уступите |

### 2.2 Interest-Based Resolution

**Позиции vs Интересы:**

```
ПОЗИЦИЯ:  Что человек говорит, что хочет (surface)
ИНТЕРЕС:  Почему он это хочет (underlying need)

Пример:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Позиция Алексея:    "Хочу использовать React"                 │
│  Позиция Марии:      "Хочу использовать Vue"                   │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Интерес Алексея:    "Важна ecosystem, легче нанять людей"     │
│  Интерес Марии:      "Важна простота для junior developers"    │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Решение:            "React + documentation + onboarding       │
│                       program для juniors"                      │
│                       (addresses both interests)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Как докопаться до интересов:**

| Вопрос | Что узнаёте |
|--------|-------------|
| "Почему это для тебя важно?" | Underlying motivation |
| "Что произойдёт, если мы сделаем X?" | Concerns, fears |
| "Какую проблему это решает?" | Real need |
| "Что для тебя worst case?" | Fears to address |
| "Если бы ты мог получить одну вещь, что бы это было?" | Priority |

### 2.3 Resolution Process: Пошаговый скрипт

**Step 1: Acknowledge (Признать конфликт)**

```
Ваши слова:
"Я вижу, что у нас разные точки зрения на это."
"Похоже, у нас disagreement. Давай разберёмся."
"Я хочу понять обе стороны, прежде чем мы решим."

❌ Не говорите:
"Ну вы опять спорите..."
"Это не важно, просто решите"
```

**Step 2: Understand Each Side (Понять обе стороны)**

```
Вопросы стороне A:
"[Имя], помоги мне понять твою позицию."
"Что для тебя важно в этом?"
"Какие concerns у тебя есть?"

*Слушаете, не перебивая*
*Summarize: "Если я правильно понял, для тебя важно..."*

Вопросы стороне B:
"[Имя], теперь твоя очередь. Как ты видишь ситуацию?"
*Repeat process*
```

**Step 3: Find Common Ground (Найти общее)**

```
Ваши слова:
"Что вы оба хотите в итоге?"
"В чём вы согласны?"
"Какая у нас общая цель?"

Фиксируйте:
"Итак, вы оба согласны, что [X] важно. 
Разногласие в том, как достичь."
```

**Step 4: Generate Options (Генерировать варианты)**

```
Ваши слова:
"Какие есть варианты решения?"
"Что если мы попробуем...?"
"Есть ли третий вариант?"

Правила:
- Не критикуйте идеи сразу
- Записывайте все варианты
- Спрашивайте обе стороны
```

**Step 5: Agree on Solution (Договориться)**

```
Ваши слова:
"Какой вариант работает для обоих?"
"Что каждый готов сделать?"
"Давай запишем, о чём договорились."

Формат договорённости:
- Что делает сторона A
- Что делает сторона B
- Когда
- Как проверим
```

**Step 6: Follow Up (Проверить)**

```
"Давай встретимся через неделю и проверим, как работает."
"Если что-то не так — сразу скажите, не копите."
```

---

## 3. Mediation

### 3.1 When to Mediate

**Вмешивайтесь когда:**

- Конфликт влияет на работу
- Стороны не могут решить сами
- Escalation продолжается
- Team morale страдает

**Не вмешивайтесь если:**

- Обычное disagreement
- Стороны могут решить сами
- Conflict is healthy debate

### 3.2 Mediation Process

```

Step 1: Preparation
─────────────────────
- Understand situation (talk to each separately)
- Assess if mediation needed
- Set up neutral meeting

Step 2: Opening
─────────────────────
- Ground rules (respectful, no interrupting)
- Goal: find solution, not assign blame
- Both sides will be heard

Step 3: Each Side's Story
─────────────────────
- Person A speaks uninterrupted
- Person B speaks uninterrupted
- Summarize each perspective

Step 4: Identify Issues
─────────────────────
- What are the key issues?
- What are underlying interests?
- Where is common ground?

Step 5: Generate Solutions
─────────────────────
- Brainstorm options
- Evaluate together
- Find mutually acceptable

Step 6: Agreement
─────────────────────
- Specific commitments
- Follow-up plan
- Document if needed

Step 7: Follow Up
─────────────────────
- Check in after 1-2 weeks
- Ensure agreement holding

```

### 3.3 Mediator Guidelines

```

✅ DO:

- Stay neutral
- Listen actively
- Ask clarifying questions
- Focus on behavior, not personality
- Look for common ground
- Redirect personal attacks

❌ DON'T:

- Take sides
- Impose solution
- Blame either party
- Share confidences
- Rush to judgment
- Allow disrespect

```

---

## 4. Difficult Conversations

Сложные разговоры — часть работы менеджера. Избегать их = накапливать проблемы.

### 4.1 Types of Difficult Conversations

| Тип | Пример | Сложность |
|-----|--------|-----------|
| **Performance issues** | "Качество твоей работы снизилось" | High |
| **Behavioral problems** | "Твоё поведение на митингах мешает команде" | High |
| **Compensation** | "Я не могу одобрить повышение" | Medium |
| **Role change/demotion** | "Мы меняем твою роль" | High |
| **Layoffs/termination** | "Твоя позиция сокращается" | Very High |
| **Personal affecting work** | "Личная ситуация влияет на работу" | High |
| **Conflict with colleague** | "Нужно обсудить ситуацию с [Name]" | Medium |

### 4.2 Framework: DESC с примерами

**D**escribe: Объективно опишите ситуацию (факты, не мнения)
**E**xpress: Выразите impact (на команду, проект, вас)
**S**pecify: Укажите желаемое изменение (конкретно)
**C**onsequences: Объясните последствия (позитивные и/или негативные)

**Пример 1: Плохие code reviews**

```
D: "В последних трёх code review я видел комментарии типа 
    'это плохо' и 'неправильно' без объяснений."

E: "Это frustrating для junior developers. 
    Анна говорила, что не понимает, как исправить."

S: "Я прошу к каждому critical comment добавлять 
    одно предложение — почему это проблема и как лучше."

C: "Это поможет juniors учиться быстрее и улучшит 
    качество кода в следующих PR."
```

**Пример 2: Опоздания на митинги**

```
D: "За последние две недели ты опоздал на 4 из 5 standups. 
    Сегодня на 15 минут."

E: "Когда тебя нет, команда не знает статус твоих задач. 
    Это влияет на планирование дня."

S: "Мне нужно, чтобы ты был на standup вовремя каждый день. 
    Если есть blocker — предупреди заранее."

C: "Если проблема в расписании — давай обсудим. 
    Но опоздания влияют на команду и это нужно исправить."
```

**Пример 3: Отказ в повышении зарплаты**

```
D: "Ты просил повышение на 20%. 
    Я обсудил с HR и руководством."

E: "Я ценю твой вклад, особенно [конкретные примеры]. 
    Мне важно, чтобы ты чувствовал справедливость."

S: "Сейчас я могу одобрить 10%. 
    Для 20% нужны [конкретные достижения] к следующему cycle."

C: "Давай составим план, что нужно для full request. 
    Я буду advocateлить за тебя."
```

### 4.3 Скрипты для разных ситуаций

**Ситуация: Performance Decline**

```
Подготовка:
- Собрать конкретные примеры (даты, факты)
- Подумать о возможных причинах
- Подготовить план улучшения

Разговор:
"[Имя], я хочу обсудить кое-что важное.

За последний месяц я заметил изменения в твоей работе:
- [Пример 1]
- [Пример 2]

Это не похоже на тебя, и я хочу понять, что происходит.
Есть что-то, что мешает тебе работать как раньше?"

*Слушаете*

"Спасибо, что поделился. Вот что я предлагаю:
[План улучшения с конкретными шагами]

Давай встретимся через [неделю/две] и проверим прогресс."
```

**Ситуация: Behavioral Problem (постоянные перебивания)**

```
"[Имя], я хочу дать тебе feedback о митингах.

Я заметил, что на последних нескольких design reviews 
ты перебивал коллег, когда они ещё не закончили мысль.
На сегодняшнем митинге это было 4 раза.

Когда это происходит, люди теряют мысль и 
некоторые перестают высказываться вообще.

Я понимаю, что ты хочешь поделиться идеями — это хорошо.
Можешь ли ты подождать паузы или поднять руку, 
прежде чем начать говорить?

Это позволит всем быть услышанными и 
улучшит качество наших дискуссий."
```

**Ситуация: Layoff Notification**

```
"[Имя], у меня для тебя сложная новость.
Нет хорошего способа это сказать.

Из-за [причина: reorganization/budget cuts/etc.] 
компания приняла решение сократить [N] позиций.
Твоя позиция попала в это сокращение.
Твой последний рабочий день — [дата].

Это не о твоей работе или performance.
Это бизнес-решение.

Вот что мы предлагаем:
- Severance: [детали]
- Health coverage: [детали]
- Reference: Я с удовольствием дам рекомендацию

Сейчас тебе не нужно ничего решать.
Возьми время осмыслить, HR свяжется с деталями.

Есть вопросы, которые я могу ответить сейчас?"
```

### 4.4 Handling Reactions: Подробные скрипты

**Реакция: Defensive (Защита)**

```
Человек: "Это неправда! Я всё делаю правильно!"

Вы: "Я понимаю, что слышать такое неприятно. 
     Я не атакую тебя как человека. 
     Я хочу решить конкретную проблему вместе.
     
     Вот конкретные примеры, которые я записал:
     [Факты без оценок]
     
     Помоги мне понять — что ты видишь по-другому?"
```

**Реакция: Emotional (Слёзы, гнев)**

```
Человек: *Плачет* или *Злится*

Вы: "Я вижу, что это тебя расстроило. Это нормально.
     Хочешь взять паузу? 
     Мы можем продолжить через 10 минут или завтра.
     
     *Если хотят продолжить:*
     Мне важно, чтобы ты был в состоянии это обсуждать.
     
     *Если нужна пауза:*
     Давай встретимся [когда]. Я буду на связи."
     
*Не торопитесь. Дайте время.*
```

**Реакция: Denial (Отрицание)**

```
Человек: "Такого не было. Ты ошибаешься."

Вы: "Я понимаю, что ты видишь ситуацию иначе.
     У меня есть конкретные примеры — давай посмотрим вместе.
     
     [Показываете документацию]
     
     Расскажи, что ты видишь по-другому.
     Возможно, есть контекст, который я упускаю."
```

**Реакция: Blame (Обвинение других)**

```
Человек: "Это не я, это [другой человек / система / обстоятельства]!"

Вы: "Я слышу, что ты видишь внешние факторы.
     Давай разделим: что контролируют другие и что контролируешь ты.
     
     Сейчас я хочу сфокусироваться на том, 
     что ты можешь сделать по-другому.
     
     Что в твоей власти изменить?"
```

**Реакция: Counter-attack (Контратака)**

```
Человек: "А ты сам...!" или "А почему [другой] не получает такой feedback?"

Вы: "Я понимаю frustration. 
     Сейчас мы говорим о тебе, не о других.
     
     Если у тебя есть feedback для меня — 
     я буду рад услышать его в конце или на отдельной встрече.
     
     Можем мы вернуться к [topic]?"
```

### 4.5 Подготовка к сложному разговору

**Checklist перед разговором:**

```markdown
□ Цель разговора clear?
□ Конкретные примеры собраны?
□ Время и место private?
□ Достаточно времени (не между митингами)?
□ Я calm и ready?
□ DESC prepared?
□ Возможные reactions anticipated?
□ Next steps ready?
```

**Timing Tips:**

| DO | DON'T |
|----|-------|
| Отдельный митинг для сложных тем | В конце regular 1-on-1 "ой, кстати..." |
| Утром или после lunch (fresh) | В пятницу вечером |
| Private room/call | Open office |
| Достаточно времени | 5 минут между митингами |

---

## 5. Specific Situations: Подробные сценарии

### 5.1 Конфликт между двумя членами команды

**Scenario:** Алексей и Мария (оба senior) не могут работать вместе. Постоянные споры на митингах, жалобы друг на друга вам.

**Пошаговый подход:**

**Шаг 1: Говорите с каждым отдельно**

```
С Алексеем:
"Я замечаю tension между тобой и Марией. 
 Помоги мне понять, что происходит с твоей стороны."

*Слушаете без judgment*
*Задаёте уточняющие вопросы*

"Что бы помогло улучшить ситуацию?"
```

**Шаг 2: Идентифицируйте тип конфликта**

| Тип | Признаки | Действия |
|-----|----------|----------|
| Task conflict | Спорят о технических решениях | Установите decision process |
| Process conflict | Кто за что отвечает | Clarify roles |
| Relationship conflict | Личная неприязнь | Mediation, separation |

**Шаг 3: Mediation meeting (если нужно)**

```
"Я пригласил вас обоих, потому что хочу решить ситуацию.
 Мы все хотим, чтобы команда работала хорошо.
 
 Ground rules:
 - Слушаем без перебивания
 - Говорим о поведении, не о личности
 - Цель — найти решение, не виноватого
 
 [Имя], начни — расскажи свою perspective."
 
 *Process each side, find common ground, agree on actions*
```

**Шаг 4: Set Clear Expectations**

```
"Вот что я ожидаю дальше:
 - Профессиональное общение на митингах
 - Если disagreement — говорите о проблеме, не о человеке
 - Если не можете решить — приходите ко мне
 
 Это non-negotiable."
```

### 5.2 Конфликт с другой командой

**Scenario:** Ваша команда и Team B обвиняют друг друга в задержках. "Они нам не дают API" vs "Они меняют requirements".

**Пошаговый подход:**

**Шаг 1: Разговор с другим Team Lead**

```
"Привет [Имя], я заметил tension между нашими командами.
 Хочу понять ситуацию и найти решение вместе.
 Можем созвониться?"

На звонке:
"Расскажи, как ты видишь ситуацию?"

*Слушаете без defensive*
*Делитесь своей perspective*
```

**Шаг 2: Find Common Ground**

```
"Мы оба хотим [общая цель: доставить feature/избежать задержек].
 Давай посмотрим, где breakdown происходит."
 
 *Рисуете вместе process*
 *Находите bottlenecks*
```

**Шаг 3: Joint Problem-Solving**

```
Варианты:
- Joint planning session с обеими командами
- Shared backlog для dependencies
- Regular sync между командами
- Liaison person на каждой стороне
```

**Шаг 4: Agreement и Follow-up**

```
"Давай договоримся:
 - [Конкретные действия]
 - Встречаемся раз в [период] для sync
 - Если проблема — сразу говорим друг другу, не копим"
```

### 5.3 Конфликт с вашим руководителем

**Scenario:** Ваш Director принял решение, с которым вы не согласны (например, направить ваших людей на другой проект).

**Подход: "Disagree and Commit"**

**Шаг 1: Request 1-on-1**

```
"У меня есть concerns по поводу [решение]. 
 Можем обсудить на нашем следующем 1-on-1?"
```

**Шаг 2: Present Your Case (data-driven)**

```
"Я хочу поделиться моим perspective.
 
 Вот мои concerns:
 1. [Concern 1 + data]
 2. [Concern 2 + data]
 
 Вот что я бы предложил вместо:
 [Alternative with reasoning]
 
 Что я могу упускать?"
```

**Шаг 3: Listen and Understand**

```
*Слушаете их reasoning*
*Возможно, у них есть context, который вы не знаете*

"Понял. Это имеет смысл в свете [context]."
или
"Я всё равно вижу риски, но понимаю твоё reasoning."
```

**Шаг 4: Commit or Escalate**

| Ситуация | Действие |
|----------|----------|
| Понимаете их reasoning | Commit и execute |
| Disagree, но не critical | "Disagree and commit" — выполняете |
| Ethical issue | Escalate выше |
| Fundamental disagreement | Document, reconsider fit |

```
"Ok, я понимаю решение. 
 У меня остаются concerns, но я буду выполнять план.
 Прошу только: если [риск] материализуется, 
 давай пересмотрим."
```

### 5.4 Toxic Team Member

**Scenario:** Пётр создаёт негативную атмосферу — сарказм, жалобы, passive-aggressive поведение. Другие начинают жаловаться.

**Важно понимать:**

```
"Brilliant Jerk" Formula:
High performance + Toxic behavior = NET NEGATIVE

Даже если человек производителен, 
токсичное поведение разрушает команду.
Часто лучше расстаться.
```

**Пошаговый подход:**

**Шаг 1: Document Specific Behaviors**

```
Date       | Behavior                           | Witness
───────────────────────────────────────────────────────────
Jan 15     | Сказал "это идиотское решение"     | Team meeting
Jan 18     | Rolled eyes при выступлении Анны   | Design review
Jan 20     | Email с сарказмом к PM             | Email thread
```

**Шаг 2: Private Conversation — Feedback + Expectations**

```
"[Имя], я хочу обсудить кое-что важное.

Я наблюдаю поведение, которое влияет на команду:
- [Пример 1]
- [Пример 2]

Когда это происходит, люди чувствуют [impact].

Я понимаю, что ты можешь видеть ситуацию иначе.
Расскажи, что происходит?

*Слушаете*

Вот что я ожидаю:
- [Конкретное изменение поведения]
- Это начинается сейчас, не "попробую"

Давай встретимся через неделю и проверим."
```

**Шаг 3: Monitor и Document**

```
Следите за изменениями (или отсутствием).
Документируйте всё.
Собирайте feedback от команды.
```

**Шаг 4: Если нет изменений — Formal Warning**

```
"[Имя], мы говорили об [X] две недели назад.
 Я не вижу изменений. [Конкретные примеры].
 
 Это formal warning. 
 Следующий шаг — PIP или termination.
 
 У тебя есть [срок] показать improvement."

*Документируйте письменно, копия в HR*
```

**Шаг 5: Если всё равно нет изменений — Exit**

```
Работайте с HR.
Процесс зависит от company policy.
Protect остальную команду.
```

> **💡 Key Insight:**  
> Не жертвуйте командой ради одного человека. Tolerance для toxicity = signal всем остальным, что так можно.

---

## 6. Conflict Prevention

### 6.1 Proactive Measures

```

Clear expectations:

- Roles and responsibilities defined
- Decision-making process clear
- Communication norms established

Regular feedback:

- Issues addressed early
- No buildup of resentment
- Open dialogue encouraged

Team norms:

- How we disagree
- How we make decisions
- How we give feedback

```

### 6.2 Healthy Disagreement

**Encourage:**
```

- "Devil's advocate" role
- Pre-mortem exercises
- Diverse perspectives invited
- Debate ideas, not people

```

**Team agreement:**
```

"We commit to:

- Attack problems, not people
- Listen to understand, not respond
- Assume good intent
- Disagree openly, commit together"

```

---

## 7. Escalation

### 7.1 When to Escalate

```

Escalate to your manager / HR:

- Legal/ethical concerns
- Harassment / discrimination
- Safety issues
- You can't resolve it
- Pattern of behavior despite intervention

```

### 7.2 How to Escalate

```

1. Document everything first
2. Be factual, not emotional
3. Describe what you've tried
4. Be clear about what you need
5. Propose solutions if possible

```

---

## 8. Self-Management

### 8.1 Managing Your Emotions

**Before conflict conversation:**
```

- Take time to calm down
- Separate facts from interpretation
- Consider their perspective
- Plan your key points
- Anticipate reactions

```

**During:**
```

- Breathe
- Pause before responding
- Focus on issue, not person
- Ask questions
- Take breaks if needed

```

### 8.2 After Conflict

**Reflection:**
```

- What went well?
- What would I do differently?
- Did I listen enough?
- What did I learn about them? About myself?

```

---

## 💡 Key Takeaways

- **Not all conflict is bad:** Task conflict improves decisions. Relationship conflict всегда деструктивен

- **Escalation stages:** Чем раньше вмешаетесь, тем легче решить. Stage 1-2 = ваша работа

- **Thomas-Kilmann:** Выбирайте стиль в зависимости от ситуации. Collaborating не всегда лучший

- **Interests > Positions:** Копайте до underlying needs. "Почему это важно?" — ключевой вопрос

- **DESC framework:** Describe → Express → Specify → Consequences. Готовьте перед разговором

- **Handle reactions:** Defensive, Emotional, Denial, Blame — у каждой есть скрипт

- **Toxic members:** Brilliant jerk = net negative. Не жертвуйте командой

- **Disagree and Commit:** Если не ethical issue — выполняйте решение руководства

- **Prevent proactively:** Clear expectations, regular feedback, team norms for disagreement

---

## 🚀 Next Steps

**Related Modules:**

- [05_Feedback](../05_Feedback/) — giving difficult feedback
- [11_Communication](../11_Communication/) — communication skills
- [10_Culture](../10_Culture/) — psychological safety

**Practice Ideas:**

1. **Thomas-Kilmann assessment:** Пройдите assessment, узнайте свой default стиль
2. **DESC preparation:** Подготовьте DESC для следующего сложного разговора
3. **Team norms:** Установите нормы disagreement в команде
4. **Role-play:** Отрепетируйте сложный разговор с коллегой
5. **Conflict log:** Записывайте конфликты и как их решили — для learning

**Going Deeper:**

- Nonviolent Communication (NVC) — Marshall Rosenberg
- Crucial Conversations skills
- Emotional Intelligence
- Mediation certification

---

## 📚 Additional Resources

**Books:**

- "Crucial Conversations" by Patterson et al. — **must-read**, essential for managers
- "Difficult Conversations" by Stone, Patton, Heen — from Harvard Negotiation Project
- "Nonviolent Communication" by Marshall Rosenberg — deeper communication skills
- "Thanks for the Feedback" by Stone & Heen — receiving difficult feedback
- "The Anatomy of Peace" by Arbinger Institute — mindset for conflict

**Models:**

- Thomas-Kilmann Conflict Mode Instrument (TKI)
- Interest-Based Relational Approach
- DESC Framework
- Crucial Conversations model

**Videos:**

- [Crucial Conversations Summary](https://www.youtube.com/watch?v=uc3ARpccRwQ)
- [Thomas-Kilmann Model Explained](https://www.youtube.com/watch?v=PFIeSxC0kxE)

**Tools:**

- [TKI Assessment](https://www.themyersbriggs.com/en-US/Products-and-Services/TKI) — узнайте свой conflict style

---




