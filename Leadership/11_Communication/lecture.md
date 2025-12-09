# Коммуникация
## Stakeholder Management, Reporting и Influence

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать роль лидера в организации
- Иметь опыт взаимодействия с разными stakeholders
- Быть готовым развивать навыки влияния

**Recommended prior modules:**
- [05_Feedback](../05_Feedback/) — коммуникация через feedback
- [10_Culture](../10_Culture/) — культура коммуникации

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Идентифицировать и управлять stakeholders
- Адаптировать коммуникацию под аудиторию
- Эффективно делать reporting "наверх"
- Влиять без формального авторитета
- Вести сложные разговоры и переговоры

---

## 1. Stakeholder Management

### 1.1 Кто такие stakeholders

**Stakeholder** — любой, кто влияет на вашу работу или на кого влияет ваша работа.

**Типичные stakeholders Team Lead:**
```
Internal:

- Ваш руководитель (EM, Director)
- Ваша команда
- Другие команды
- Product Manager
- Дизайнеры
- QA
- DevOps/SRE

External:

- Клиенты/пользователи
- Vendors
- Partners
```

### 1.2 Stakeholder Mapping

**Power/Interest Grid:**

```
              High Power
                  │
      ┌───────────┼───────────┐
      │   KEEP    │   MANAGE  │
      │ SATISFIED │  CLOSELY  │
      │           │    ★      │
──────┼───────────┼───────────┼──────
      │  MINIMAL  │   KEEP    │
      │  EFFORT   │ INFORMED  │
      │           │           │
      └───────────┼───────────┘
                  │
              High Interest
              
★ = Top priority stakeholders
```

**Категории:**
- **Manage Closely:** Высокая власть + высокий интерес (ваш руководитель)
- **Keep Satisfied:** Высокая власть + низкий интерес (executives)
- **Keep Informed:** Низкая власть + высокий интерес (команда)
- **Minimal Effort:** Низкая власть + низкий интерес

### 1.3 Stakeholder Communication Plan

```markdown
## Stakeholder: [Name/Role]

### Profile:

- Power: High/Medium/Low
- Interest: High/Medium/Low
- Attitude: Supportive/Neutral/Resistant

### Needs:

- Какая информация нужна?
- Какой уровень детализации?
- Какие concerns?

### Communication:

- Channel: Email/Slack/Meeting/Report
- Frequency: Daily/Weekly/Monthly/As needed
- Format: Brief/Detailed/Technical/Business
```

---

## 2. Адаптация коммуникации

### 2.1 Принцип аудитории

> **💡 Key Insight:**  
> Один и тот же message нужно доносить по-разному разным аудиториям.

**Пример — тот же проект:**

**Для CEO:**
```
"Мы запустим платформу в Q2, это увеличит retention на 15% 
и принесёт $2M ARR."
```

**Для Engineering Director:**
```
"Платформа требует 3 месяца, команду из 5 человек, 
есть риск с интеграцией legacy системы."
```

**Для команды:**
```
"Новый проект! Интересный technical challenge с микросервисами, 
timeline 3 месяца, начинаем с design phase."
```

### 2.2 Уровни детализации

```
Executive Level:

- Impact на бизнес
- High-level timeline
- Key risks
- Decisions needed

Management Level:

- Status и progress
- Resource needs
- Dependencies
- Detailed risks

Team Level:

- Technical details
- Implementation decisions
- Day-to-day blockers
- Learning opportunities
```

### 2.3 BLUF: Bottom Line Up Front

**Военный принцип:** Главное — в начале.

```markdown
❌ Poor:
"We've been working on the new authentication system. 
The team has explored several options including OAuth, SAML, 
and custom solutions. After extensive research..."
[5 paragraphs later]
"We need additional budget for Auth0 integration."

✅ Good (BLUF):
"We need $15K additional budget for Auth0. 
Here's why this is the best option for our auth system..."
```

---

## 3. Reporting "наверх"

### 3.1 Зачем reporting важен

**Для вашего руководителя:**
- Понимание status без микроменеджмента
- Раннее предупреждение о рисках
- Информация для их reporting выше
- Доверие через прозрачность

**Для вас:**
- Visibility вашей работы
- Support в нужный момент
- Career advancement

### 3.2 Формат Weekly Update

```markdown
## Weekly Update: [Team Name]
## Week of: [Date]

### TL;DR (1-2 sentences)
[Самое важное за неделю]

### Highlights ✅
- [Achievement 1]
- [Achievement 2]

### In Progress 🔄
- [Project A] — 70% complete, on track
- [Project B] — delayed, see Risks

### Risks ⚠️
- [Risk 1]: [Impact, Mitigation]
- [Risk 2]: [Impact, Mitigation]

### Needs from You 🙏
- [Decision needed by Friday]
- [Resource request]

### Team Notes 👥
- [Vacation, new hire, etc.]
```

### 3.3 Типичные ошибки

```
❌ Too much detail:
Никто не прочитает 10 страниц

❌ Only good news:
Риски выплывут позже, хуже будет

❌ Surprises:
"Мы опаздываем на 2 месяца" — уже поздно

❌ No asks:
Не используете возможность получить help

✅ Right balance:
Concise, balanced, actionable
```

---

## 4. Influence без авторитета

### 4.1 Почему это важно

Как лидер, вы часто должны влиять на людей, которые вам не подчиняются:

- Другие команды
- Stakeholders
- Executives
- Cross-functional partners

### 4.2 Building Influence

**Credibility:**
```
- Expertise: знайте своё дело
- Track record: результаты говорят
- Integrity: делайте что обещаете
```

**Relationships:**
```
- Invest time в отношения
- Help others (give before ask)
- Network активно
- Be visible
```

**Communication:**
```
- Listen more than talk
- Understand their perspective
- Frame in their terms
- Show mutual benefit
```

### 4.3 Techniques для влияния

**1. Finding Common Ground:**
```
"Я понимаю, что для вас важно X. 
Мой proposal также помогает достичь X, потому что..."
```

**2. Building Coalition:**
```
Найдите allies → согласуйте с ними → придите к decision-maker вместе
```

**3. Reciprocity:**
```
Помогите им сначала → они более склонны помочь вам
```

**4. Social Proof:**
```
"Team A уже использует этот подход и видит результаты..."
```

**5. Data over Opinion:**
```
"По данным за Q3, подход X на 30% эффективнее..."
```

---

## 5. Difficult Conversations

### 5.1 Типы сложных разговоров

- Performance issues
- Conflict resolution
- Delivering bad news
- Negotiating resources
- Saying "no" to stakeholders
- Addressing behavior problems

### 5.2 Framework для сложных разговоров

**Prepare:**
```
1. What outcome do I want?
2. What are the facts (not interpretations)?
3. What might be their perspective?
4. What emotions might come up?
5. What's my backup if doesn't go well?
```

**During:**
```
1. State your intent upfront
   "I want to discuss X because I care about Y"

2. Share observations (facts)
   "I noticed that..."

3. Invite their perspective
   "How do you see it?"

4. Listen actively
   Understand before responding

5. Problem-solve together
   "How can we address this?"

6. Agree on next steps
   Specific, time-bound
```

**After:**
```
1. Follow up в writing
2. Check in на progress
3. Recognize improvement
```

### 5.3 Пример сложного разговора

**Ситуация:** Разработчик систематически опаздывает на митинги.

```
Prepare:

- Outcome: Приходить вовремя
- Facts: Опоздал на 5 из 8 standups
- Their perspective: Может есть причина?

During:
"Я хочу поговорить о standup митингах. 
Я заметил, что за последние 2 недели ты опоздал на 5 из 8. 
Это влияет на команду, потому что мы ждём или пересказываем.
Расскажи, что происходит?"

[Listen to their response]

"Понимаю. Как мы можем решить это?"

After:

- Договорились о конкретном плане
- Check-in через неделю
```

---

## 6. Written Communication

### 6.1 Email Excellence

**Structure:**
```
Subject: [Action Required] [Topic] by [Date]

Hi [Name],

[1 sentence: why writing]

[Body: key points]

[Ask: what you need]

[Timeline: when you need it]

Best,
[Name]
```

**Tips:**
- Subject line is everything
- One email = one topic
- Front-load the ask
- Be concise
- Use formatting (bullets, bold)

### 6.2 Slack/Teams Etiquette

```
✅ DO:

- Thread conversations
- Use @mentions sparingly
- Set status when unavailable
- Edit instead of multiple messages
- Use appropriate channel

❌ DON'T:

- @channel/@here without need
- Send 10 messages instead of 1
- Expect immediate response
- Use for urgent/sensitive topics
```

### 6.3 Documentation

**When to document:**
- Decisions and rationale
- Processes and runbooks
- Architecture and design
- Meeting outcomes
- Status updates

**Principles:**
- Write for the reader, not yourself
- Include context (why, not just what)
- Keep updated or delete
- Make findable (good titles, tags)

---

## 7. Presentations

### 7.1 Структура презентации

**For business audience:**
```
1. Hook (why should they care?)
2. Problem (what's the issue?)
3. Solution (what do you propose?)
4. Evidence (why this will work?)
5. Ask (what do you need?)
```

**For technical audience:**
```
1. Context (problem space)
2. Options considered
3. Recommended approach
4. Trade-offs
5. Implementation plan
6. Questions
```

### 7.2 Tips для presenting

```
Preparation:

- Know your audience
- Practice out loud
- Prepare for questions
- Have backup slides

Delivery:

- Start strong (no "um, so...")
- Maintain eye contact
- Speak slowly
- Use pauses
- Tell stories, not just facts

Handling Questions:

- Repeat/clarify question
- Answer concisely
- "I don't know, I'll find out" is OK
- Offer to follow up offline if needed
```

### 7.3 Executive Presentations

**Differences:**
- Time is scarce (be brief!)
- They want recommendations, not options
- Focus on business impact
- Be ready for any question
- Have data backup

**Format:**
```
Slide 1: Title + TL;DR
Slide 2: Recommendation
Slide 3: Why (key supporting points)
Slide 4: Risk & Mitigation
Slide 5: Ask / Decision needed

[Backup slides with details]
```

---

## 8. Cross-team Communication

### 8.1 Dependencies

**Tracking dependencies:**
```markdown
## Dependency: [Team Name]

What we need: [specific deliverable]
When we need it: [date]
Impact if delayed: [consequences]
Contact: [person]
Status: On track / At risk / Blocked
```

### 8.2 Conflict with Other Teams

**Common causes:**
- Competing priorities
- Resource constraints
- Misaligned goals
- Communication gaps

**Resolution approach:**
```
1. Assume good intent
2. Understand their constraints
3. Find common goals
4. Propose win-win solutions
5. Escalate together if needed
```

### 8.3 Building Relationships

```
- Regular sync meetings
- Help them when you can
- Share credit
- Communicate early about changes
- Say thank you
```

---

## 💡 Key Takeaways

- **Know your audience:** Адаптируйте message под stakeholder
- **BLUF:** Bottom Line Up Front — главное в начале
- **No surprises:** Сообщайте о рисках раньше, не позже
- **Influence ≠ Authority:** Credibility + Relationships + Communication
- **Difficult conversations:** Prepare, state facts, listen, solve together

---

## 🚀 Next Steps

**Related Modules:**
- [05_Feedback](../05_Feedback/) — feedback как коммуникация
- [12_ScalingTeams](../12_ScalingTeams/) — коммуникация в больших командах

**Practice Ideas:**
1. Создайте stakeholder map для вашей роли
2. Напишите weekly update в формате из лекции
3. Подготовьтесь к одному сложному разговору

**Going Deeper:**
- Negotiation skills
- Public speaking
- Executive presence

---

## 📚 Additional Resources

**Books:**
- "Crucial Conversations" by Patterson et al. — difficult conversations
- "Never Split the Difference" by Chris Voss — negotiation
- "Influence" by Robert Cialdini — psychology of persuasion

**Articles:**
- [BLUF: The Military Standard](https://www.animalz.co/blog/bottom-line-up-front/)
- [Stakeholder Management Guide](https://www.pmi.org/learning/library/stakeholder-management-task-project-success-7736)

**Videos:**
- [TED: How to speak so that people want to listen](https://www.ted.com/talks/julian_treasure_how_to_speak_so_that_people_want_to_listen)

---

