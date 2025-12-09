# Эффективные митинги
## Planning, Retro, Standup и Decision-making

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Agile/Scrum
- Иметь опыт участия в командных митингах
- Понимать роль лида в координации команды

**Recommended prior modules:**
- [07_TeamProcesses](../07_TeamProcesses/) — построение процессов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проводить эффективные standups, planning и retro
- Структурировать митинги для конкретных целей
- Фасилитировать обсуждения и принимать решения
- Сокращать количество и длительность митингов
- Создавать культуру продуктивных встреч

---

## 1. Стоимость митингов

### 1.1 Реальная цена

**Формула:**
```
Стоимость митинга = (Число участников × Длительность × Hourly rate) 
                   + Opportunity cost (потерянная продуктивность)
```

**Пример:**
```
5 человек × 1 час × $75/час = $375
+ Context switch overhead ≈ $500 за митинг

10 митингов в неделю = $5,000/неделю
```

> **💡 Key Insight:**  
> Каждый митинг — это инвестиция. Задайте вопрос: "Стоит ли эта встреча своих денег?"

### 1.2 Death by meetings

**Симптомы meeting overload:**
- Дни полностью забиты митингами
- Реальная работа — вечером и в выходные
- "Митинг о митингах"
- Никто не помнит, о чём договорились
- Люди приходят неподготовленными

### 1.3 Принцип минимальных митингов

**Правило:** Если что-то можно решить без митинга — решите без митинга.

```
Эскалация (от простого к сложному):

1. Async message (Slack, email)
2. Quick sync (5 min call)
3. Working session (2-3 people)
4. Team meeting (full team)
```

---

## 2. Анатомия хорошего митинга

### 2.1 Три обязательных элемента

**Каждый митинг должен иметь:**

1. **Clear Purpose**
   - Зачем мы собрались?
   - Какой outcome ожидаем?

2. **Agenda**
   - Что обсуждаем?
   - В каком порядке?
   - Сколько времени на каждый пункт?

3. **Action Items**
   - Что делаем после?
   - Кто ответственный?
   - Когда deadline?

### 2.2 Типы митингов

| Тип | Цель | Формат |
|-----|------|--------|
| **Information** | Передать информацию | Презентация, мало обсуждения |
| **Discussion** | Обсудить тему | Brainstorm, debate |
| **Decision** | Принять решение | Структурированное обсуждение |
| **Coordination** | Синхронизироваться | Status updates, planning |
| **Creative** | Генерировать идеи | Brainstorm, workshop |

### 2.3 Подготовка к митингу

**До митинга (организатор):**
```markdown
1. Определить цель и outcome
2. Создать agenda (в invite!)
3. Пригласить только необходимых людей
4. Разослать pre-read материалы
5. Забукировать комнату/zoom
```

**До митинга (участники):**
```markdown
1. Прочитать agenda
2. Подготовить input
3. Если не нужен — отказаться/спросить
```

### 2.4 Во время митинга

**Начало:**
- Начинайте вовремя (не ждите опоздавших)
- Озвучьте цель и agenda
- Определите note-taker

**Середина:**
- Следите за временем
- Возвращайте к agenda при отвлечениях
- Паркуйте off-topic вопросы (parking lot)
- Вовлекайте молчаливых

**Конец:**
- Резюмируйте action items
- Уточните owners и deadlines
- Заканчивайте вовремя (или раньше!)

### 2.5 После митинга

```markdown
1. Разослать meeting notes (в течение 24 часов)
2. Track action items
3. Follow up на невыполненные
```

---

## 3. Daily Standup

### 3.1 Цель

**Standup нужен для:**
- Синхронизации команды
- Выявления блокеров
- Awareness о том, кто над чем работает

**Standup НЕ для:**
- Status reports менеджеру
- Детальных технических обсуждений
- Problem solving

### 3.2 Формат

**Классический (Three Questions):**
```
Каждый отвечает:

1. Что сделал вчера?
2. Что буду делать сегодня?
3. Есть ли блокеры?
```

**Walk the Board:**
```
Идём по задачам на доске слева направо:

- Что блокирует завершение?
- Кто может помочь?
```

**Async Standup:**
```
Написать в Slack до 10:00:

- Done: [список]
- Today: [план]
- Blockers: [если есть]
```

### 3.3 Anti-patterns

**Что делает standup плохим:**
- ❌ Длиннее 15 минут
- ❌ Детальные технические обсуждения
- ❌ Отчёт менеджеру, а не команде
- ❌ Нет follow-up на блокеры
- ❌ Опоздания и ожидание всех

**Как исправить:**
- ✅ Таймер на 15 минут
- ✅ "Take it offline" для обсуждений
- ✅ Фокус на блокерах
- ✅ Начинать без опоздавших
- ✅ Стоять (для коротких встреч)

---

## 4. Sprint Planning

### 4.1 Цель

**Planning нужен для:**
- Определить, что команда сделает в спринте
- Декомпозировать задачи
- Выявить риски и зависимости
- Создать commitment команды

### 4.2 Структура (для 2-недельного спринта)

```
Длительность: 2-4 часа

Часть 1: WHAT (1-1.5 часа)
─────────────────────────
• PO представляет приоритеты
• Уточнение requirements
• Acceptance criteria
• Questions & Answers

Часть 2: HOW (1-1.5 часа)
─────────────────────────
• Декомпозиция на задачи
• Estimation
• Распределение работы
• Выявление зависимостей

Output: Sprint Backlog
```

### 4.3 Estimation

**Методы:**

**Story Points:**
```
Относительная оценка сложности:
1 — Trivial (пару часов)
2 — Simple (день)
3 — Medium (2-3 дня)
5 — Large (неделя)
8 — Very Large (разбить!)
13 — Epic (точно разбить!)
```

**T-Shirt Sizing:**
```
XS, S, M, L, XL
Быстрее, менее точно
Хорошо для high-level planning
```

**Planning Poker:**
```
1. PO описывает задачу
2. Все одновременно показывают оценку
3. Обсуждаем крайние значения
4. Re-vote если нужно
```

### 4.4 Capacity Planning

**Формула:**
```
Team Capacity = (Число людей × Дни спринта × Focus Factor)
                - Planned absences
                - Meetings overhead

Focus Factor ≈ 0.6-0.8 (реалистично 60-80% на задачи)
```

---

## 5. Sprint Retrospective

### 5.1 Цель

**Retro нужно для:**
- Рефлексии о прошедшем спринте
- Continuous improvement
- Team building
- Выявления проблем

> **💡 Key Insight:**  
> Retro без action items = потраченное время. Всегда выходите с конкретными улучшениями.

### 5.2 Структура

```
Длительность: 1-1.5 часа

1. Check-in (5 min)
   Как команда себя чувствует?
   
2. Data Gathering (15-20 min)
   Что произошло в спринте?
   
3. Generate Insights (20-30 min)
   Почему это произошло?
   
4. Decide What to Do (15-20 min)
   Что изменим?
   
5. Close (5 min)
   Action items и owners
```

### 5.3 Популярные форматы

**Start / Stop / Continue:**
```
🟢 START: Что начнём делать?
🔴 STOP: Что прекратим делать?
🔵 CONTINUE: Что продолжим делать?
```

**Mad / Sad / Glad:**
```
😡 MAD: Что расстроило/раздражало?
😢 SAD: Что не получилось?
😊 GLAD: Что порадовало?
```

**4Ls:**
```
❤️ LOVED: Что понравилось?
📚 LEARNED: Что узнали?
🤔 LACKED: Чего не хватало?
🙏 LONGED FOR: Чего хотелось бы?
```

**Sailboat:**
```
⛵ Лодка = команда
💨 Ветер = что нас двигает
⚓ Якорь = что тормозит
🌴 Остров = цель
🦈 Акулы = риски
```

### 5.4 Фасилитация retro

**Правила:**
- Safe space — нет blame
- Все голоса равны
- Фокус на системе, не людях
- Конструктивно, не негативно

**Техники вовлечения:**
- Silent brainstorming (стикеры)
- Dot voting для приоритизации
- Small groups для обсуждения
- Round robin для input

### 5.5 Action Items

**Хороший action item:**
```
✅ Конкретный
✅ Имеет owner
✅ Имеет deadline
✅ Измеримый
```

**Пример:**
```
❌ "Улучшить code review"
✅ "Maria: создать checklist для code review до пятницы"
```

---

## 6. Decision-making Meetings

### 6.1 Framework для решений

**RAPID Model:**
- **R**ecommend — кто предлагает решение
- **A**gree — кто должен согласовать
- **P**erform — кто выполняет
- **I**nput — кто даёт input
- **D**ecide — кто принимает финальное решение

### 6.2 Структура Decision Meeting

```
1. Context (10%)
   - Какую проблему решаем?
   - Какие ограничения?

2. Options (30%)
   - Какие варианты?
   - Pros/cons каждого

3. Discussion (40%)
   - Input от участников
   - Clarifying questions

4. Decision (20%)
   - Выбор варианта
   - Обоснование
   - Next steps
```

### 6.3 Методы принятия решений

**Consensus:**
```
+ Все согласны
- Медленно, risk of groupthink
Когда: Важные решения, затрагивающие всех
```

**Majority Vote:**
```
+ Быстро
- Меньшинство может быть недовольно
Когда: Менее критичные решения
```

**Consent:**
```
"Никто не против" (не значит "все за")
+ Быстрее консенсуса
- Требует trust
Когда: Большинство решений
```

**Decision Maker:**
```
Один человек решает (после input)
+ Самое быстрое
- Зависит от качества DM
Когда: Срочные решения, эксперт есть
```

### 6.4 Disagree and Commit

**Принцип:**
После обсуждения и решения — все поддерживают, даже если были против.

```
"Я не согласен с решением, но:

- Моё мнение было услышано
- Решение принято процессом
- Я буду его поддерживать"
```

---

## 7. Другие важные митинги

### 7.1 Sprint Review (Demo)

**Цель:** Показать stakeholders результат спринта

**Структура:**
```
Длительность: 1-2 часа

1. Intro (5 min)
   - Sprint goal
   - Что планировали
   
2. Demo (45-60 min)
   - Живая демонстрация
   - Не slides, реальный продукт
   
3. Feedback (20-30 min)
   - Вопросы stakeholders
   - Предложения
   
4. Outlook (10 min)
   - Что дальше?
```

### 7.2 Backlog Grooming (Refinement)

**Цель:** Подготовить backlog к planning

**Что делаем:**
- Уточняем requirements
- Добавляем acceptance criteria
- Estimation
- Разбиваем большие stories
- Приоритизация

**Частота:** 1 раз в неделю, 1 час

### 7.3 All-Hands / Team Meeting

**Цель:** Командный sync, announcements

**Структура:**
```
Частота: Еженедельно или bi-weekly
Длительность: 30-60 min

1. Wins / Highlights
2. Updates / Announcements
3. Upcoming
4. Q&A / Discussion
```

### 7.4 One-on-Ones

Подробно рассмотрены в [модуле 04](../04_OneOnOnes/).

---

## 8. Async-first Culture

### 8.1 Когда async лучше

**Используйте async для:**
- Status updates
- Information sharing
- Non-urgent questions
- Documentation review
- Async standups

**Используйте sync для:**
- Urgent issues
- Complex discussions
- Emotional topics
- Brainstorming
- Team building

### 8.2 Инструменты async

**Written:**
- Slack / Teams — quick updates
- Confluence / Notion — documentation
- Email — formal communication
- Loom — video messages

**Asynchronous Decisions:**
- RFC process с комментариями
- Deadline для feedback
- Default: silence = consent

### 8.3 Best practices

**Для async communication:**
```
1. Be explicit — context, deadline, action needed
2. Use threads — организация обсуждений
3. Set expectations — когда ожидать ответ
4. Document decisions — записывать итоги
```

---

## 9. Meeting-free Time

### 9.1 Защита времени

**Практики:**
- **No-meeting days:** вторник/четверг без митингов
- **Focus blocks:** 2-4 часа защищённого времени
- **Meeting hours:** митинги только 10:00-14:00

### 9.2 Правила для организаторов

```markdown
## Meeting Policy

Before scheduling, ask:

- [ ] Could this be an email/Slack?
- [ ] Who really needs to be there?
- [ ] Is 30 min enough? (default to shorter)

When scheduling:

- [ ] Include agenda in invite
- [ ] Send pre-read 24h before
- [ ] Default to 25/50 min (not 30/60)
```

### 9.3 Отказ от митингов

**Когда можно отказаться:**
- Нет agenda
- Ваш input не нужен
- Conflict с deep work time
- Можно узнать итоги async

**Как отказаться:**
```
"Thanks for the invite. Looking at the agenda, 
I'm not sure my input is needed. 
Can you share notes after, or let me know 
if there's a specific question for me?"
```

---

## 💡 Key Takeaways

- **Каждый митинг = инвестиция:** Purpose, Agenda, Action Items обязательны
- **Default to async:** Митинг — последний вариант, не первый
- **Time-box всё:** 15 мин standup, 25 мин meeting, не больше
- **Retro без action items = waste:** Всегда выходите с улучшениями
- **Disagree and commit:** После решения — все поддерживают

---

## 🚀 Next Steps

**Related Modules:**
- [07_TeamProcesses](../07_TeamProcesses/) — процессы как контекст для митингов
- [11_Communication](../11_Communication/) — коммуникация в команде

**Practice Ideas:**
1. Audit ваши митинги: сколько стоят? все нужны?
2. Внедрите no-meeting day в команде
3. Попробуйте новый формат retro

**Going Deeper:**
- Facilitation skills
- Workshop design
- Remote meeting best practices

---

## 📚 Additional Resources

**Books:**
- "Death by Meeting" by Patrick Lencioni
- "Read This Before Our Next Meeting" by Al Pittampalli
- "The Surprising Science of Meetings" by Steven Rogelberg

**Tools:**
- Miro / Mural — visual collaboration
- Retrium / EasyRetro — retro facilitation
- Notion / Confluence — meeting notes

**Articles:**
- [Shopify: Meeting Cost Calculator](https://shopify.engineering/meeting-cost-calculator)
- [Atlassian: Running Effective Meetings](https://www.atlassian.com/team-playbook/plays/effective-meetings)

---

