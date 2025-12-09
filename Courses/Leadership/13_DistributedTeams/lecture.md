# Распределённые команды
## Часовые пояса, async communication и культурные различия

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы team management
- Иметь опыт remote или hybrid работы
- Понимать важность коммуникации

**Recommended prior modules:**
- [11_Communication](../11_Communication/) — коммуникация
- [12_ScalingTeams](../12_ScalingTeams/) — масштабирование команд

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Организовывать работу в разных часовых поясах
- Выстраивать async-first communication
- Учитывать культурные различия в команде
- Поддерживать team cohesion на расстоянии
- Проводить эффективные distributed meetings

---

## 1. Типы распределённых команд

### 1.1 Модели распределения

**Remote-first:**
```
- Все работают удалённо
- Офис не является центром
- Процессы designed для remote
- Примеры: GitLab, Zapier, Automattic
```

**Hub and Spoke:**
```
- Основной офис + remote сотрудники
- Часть команды в офисе
- Risk: remote = second-class citizens
```

**Multi-office:**
```
- Несколько офисов в разных locations
- Команды spread между офисами
- Часовые пояса как challenge
```

**Hybrid:**
```
- Mix офиса и remote
- Flexible policies
- Сложнее всего управлять consistency
```

### 1.2 Challenges распределённых команд

```
Communication:

- Нет casual conversations
- Harder to read body language
- Information asymmetry
- Time zone gaps

Collaboration:

- Harder to pair/mob
- Delay in responses
- Meeting scheduling hell
- Whiteboarding challenges

Culture:

- Isolation and loneliness
- Us vs Them (office vs remote)
- Different cultural norms
- Trust harder to build

Management:

- Visibility проблема
- Performance оценить сложнее
- Onboarding harder
- Less organic mentoring
```

---

## 2. Async-First Communication

### 2.1 Принцип Async-First

> **💡 Key Insight:**  
> В распределённых командах async должен быть default, sync — exception.

**Почему:**
- Time zones делают sync сложным
- Записанная информация доступна всем
- Меньше прерываний = больше deep work
- Inclusion для всех locations

### 2.2 When Async, When Sync

**Async для:**
```
- Status updates
- Documentation
- Non-urgent questions
- FYI information
- Code reviews
- Most discussions
```

**Sync для:**
```
- Urgent issues
- Complex decisions
- Emotional conversations
- Brainstorming
- Team building
- 1-on-1s
```

### 2.3 Async Communication Best Practices

**Writing:**
```markdown
✅ DO:

- Include all context (receiver doesn't know background)
- State what you need clearly
- Give deadline for response
- Use structured formats
- Over-communicate rather than under

❌ DON'T:

- "Hey, got a minute?" (without context)
- Expect immediate response
- Use sync tools for async
- Bury the ask at the end
```

**Example async message:**
```markdown
Subject: Need input on Auth approach by Thursday

Hi team,

Context: We're deciding on authentication for the new API.

Options:

1. OAuth2 + JWT (recommended) — pros/cons
2. API Keys — pros/cons

Ask: Please review and comment by Thursday EOD.

If I don't hear objections, we'll go with Option 1.

[Link to detailed doc]
```

### 2.4 Tools для async

```
Written communication:

- Slack/Teams (threads!)
- Email (formal)
- Notion/Confluence (documentation)
- Linear/Jira (work tracking)

Video:

- Loom/Vidyard (async video updates)
- Recorded meetings

Collaboration:

- Figma/Miro (async whiteboarding)
- Google Docs (async editing)
- GitHub/GitLab (code async)
```

---

## 3. Working Across Time Zones

### 3.1 Overlap Hours

**Finding overlap:**
```
Example: Team in NYC (EST) and Berlin (CET)

NYC:     9am ───────────────────── 6pm
Berlin:       3pm ─────────────────────── 12am

Overlap:      3pm-6pm NYC / 9pm-12am Berlin
             = 3 hours
```

**Using overlap wisely:**
- Sync meetings только в overlap
- High-value discussions
- Urgent coordination
- Team ceremonies (если возможно)

### 3.3 Follow-the-Sun

**Модель:**
```
APAC работает → handoff → EMEA работает → handoff → Americas работает
```

**Требует:**
- Excellent documentation
- Clear handoff protocols
- Overlap time для handoff
- Async-first culture

### 3.3 Meeting Rotation

**Problem:**
При фиксированном времени одна timezone всегда страдает.

**Solution:**
Rotate meeting times, чтобы "боль" распределялась.

```
Week 1: 9am PST / 5pm GMT / 1am SGT (US-friendly)
Week 2: 5pm PST / 1am GMT / 9am SGT (APAC-friendly)
Week 3: 12pm PST / 8pm GMT / 4am SGT (EMEA-friendly)
```

### 3.4 Asynchronous Standups

**Вместо sync standup:**
```markdown
## Daily Async Standup

Post in #team-standup by 10am YOUR TIME:

Done yesterday:

- [task 1]
- [task 2]

Today:

- [task 1]
- [task 2]

Blockers:

- [if any]
```

---

## 4. Building Remote Culture

### 4.1 Intentional Relationship Building

**Challenge:** Нет coffee breaks, нет случайных разговоров.

**Solutions:**

```markdown
Virtual Coffee:

- Randomly paired weekly chats
- 15-30 min, no agenda
- Tools: Donut for Slack

Virtual Team Events:

- Online games (Jackbox, Among Us)
- Virtual happy hours (with moderation)
- Shared activities (cooking, trivia)

Interest Channels:

- #random, #pets, #books
- Non-work conversations
- Building human connections
```

### 4.2 Video On Culture

**Recommendation:**
```
- Default: video ON for team meetings
- Acceptable: video OFF for large all-hands
- Respect: sometimes people need video off (that's OK)
```

**Benefits:**
- See faces → build connection
- Better engagement
- Non-verbal communication

### 4.3 In-Person Time

**If possible:**
```
- Team offsites 1-2x per year
- Planning sessions
- Team building
- Just hanging out

Value:

- Accelerates trust
- Recharges relationships
- Creates shared memories
```

---

## 5. Cultural Differences

### 5.1 Hofstede's Dimensions

**Key dimensions relevant for teams:**

**Power Distance:**
```
High: Hierarchy important, defer to authority
Low: Flat, challenge authority OK

Impact: Feedback, decision-making, speaking up
```

**Individualism vs Collectivism:**
```
Individual: Personal achievement, direct communication
Collective: Group harmony, indirect communication

Impact: Recognition, conflict handling
```

**Uncertainty Avoidance:**
```
High: Detailed plans, risk-averse
Low: Comfortable with ambiguity

Impact: Planning, experimentation, change
```

**Direct vs Indirect Communication:**
```
Direct: Say what you mean (Dutch, German, US)
Indirect: Context and hints (Japan, many Asian cultures)

Impact: Feedback, disagreement, requests
```

### 5.2 Practical Implications

**Feedback:**
```
Some cultures: Direct feedback = normal
Other cultures: Direct feedback = offensive

Adaptation:

- Know your team members' preferences
- Private vs public feedback
- Soften language when needed
- Ask how they prefer to receive feedback
```

**Meetings:**
```
Some cultures: Speak up expected
Other cultures: Speaking up = disrespectful

Adaptation:

- Explicitly invite input
- Use written pre-work
- Allow async input after
- Don't interpret silence as agreement
```

**Disagreement:**
```
Some cultures: Debate is healthy
Other cultures: Disagreement = conflict

Adaptation:

- Frame as "exploring options"
- Use data and facts
- Separate idea from person
- Private conversations for sensitive topics
```

### 5.3 Building Cultural Awareness

```
1. Learn basics about team members' cultures
2. Ask individuals (don't assume from culture)
3. Share your own cultural norms
4. Discuss explicitly as a team
5. Be patient and assume good intent
```

---

## 6. Remote Onboarding

### 6.1 Challenges

```
- No physical presence
- Harder to ask "quick questions"
- Isolation from day 1
- Missing context
- Relationship building harder
```

### 6.2 Solutions

**Structured Program:**
```markdown
## Week 1
- [ ] Meet manager (video)
- [ ] Buddy assigned
- [ ] Tool setup
- [ ] Read onboarding docs
- [ ] Meet team (group call)

## Week 2
- [ ] 1-on-1 with each teammate
- [ ] First small task
- [ ] Shadow meetings
- [ ] Q&A with buddy daily

## Week 3-4
- [ ] Independent work
- [ ] Code review participation
- [ ] First demo/presentation
- [ ] Feedback check-in

## Month 1 End
- [ ] 30-day review with manager
- [ ] Goals for month 2
```

**Buddy System:**
```
- Assigned buddy (не manager)
- Daily check-ins first weeks
- Safe space for "dumb" questions
- Social connection
```

**Over-documentation:**
```
- Everything written down
- Searchable wiki
- Video walkthroughs
- FAQs updated from new hire questions
```

---

## 7. Remote Performance

### 7.1 Output vs Presence

> **💡 Key Insight:**  
> В remote work нельзя измерять по "часам в офисе". Измеряйте output и outcomes.

**What to measure:**
```
- Deliverables completed
- Quality of work
- Collaboration effectiveness
- Growth and learning
```

**What NOT to measure:**
```
- Hours online
- Response time (within reason)
- "Activity" metrics
- Presence in office
```

### 7.2 Trust and Autonomy

**Building trust:**
```
1. Clear expectations upfront
2. Regular check-ins (не микроменеджмент)
3. Assume good intent
4. Focus on outcomes
5. Give benefit of doubt
```

**Red flags (legitimate concerns):**
```
- Consistently missing deadlines
- Unreachable for extended periods
- Quality issues
- Team complaints
```

### 7.3 Remote 1-on-1s

**Best practices:**
```
- Video ON
- Protected time (no interruptions)
- More frequent for new people
- Include casual chat
- Address isolation proactively
```

**Questions to add:**
```
- How are you feeling about remote work?
- Are you feeling connected to the team?
- Is there anything making remote hard?
- Do you have what you need to work effectively?
```

---

## 8. Tools and Infrastructure

### 8.1 Essential Tool Stack

```markdown
## Communication
- Slack/Teams: chat
- Zoom/Meet: video
- Loom: async video
- Email: formal

## Documentation
- Notion/Confluence: wiki
- Google Docs: collaborative docs
- Miro/FigJam: whiteboarding

## Work Management
- Linear/Jira: tasks
- GitHub/GitLab: code
- Figma: design

## Social
- Donut: random pairing
- Gather/Teamflow: virtual office
```

### 8.2 Home Office Support

**Company should provide:**
```
- Equipment budget
- Internet stipend
- Ergonomic setup
- Co-working allowance
```

### 8.3 Security Considerations

```
- VPN requirements
- Device management
- Secure communication
- Data handling policies
```

---

## 💡 Key Takeaways

- **Async-first:** Default to async, sync for exceptions
- **Intentional culture:** Remote culture requires explicit effort
- **Time zone fairness:** Rotate meeting times, respect overlap
- **Cultural awareness:** Different cultures have different norms
- **Output over presence:** Measure results, not hours online

---

## 🚀 Next Steps

**Related Modules:**
- [11_Communication](../11_Communication/) — коммуникация basics
- [10_Culture](../10_Culture/) — культура команды

**Practice Ideas:**
1. Audit your team's async/sync balance
2. Create async standup format
3. Schedule virtual coffee pairing

**Going Deeper:**
- Remote company handbooks (GitLab, Basecamp)
- Cross-cultural communication training
- Distributed systems of work

---

## 📚 Additional Resources

**Books:**
- "Remote: Office Not Required" by Basecamp — remote work principles
- "The Culture Map" by Erin Meyer — cultural differences
- "Distributed Teams" by John O'Duinn

**Handbooks:**
- [GitLab Handbook](https://about.gitlab.com/handbook/) — comprehensive remote handbook
- [Basecamp Guide to Remote Work](https://basecamp.com/guides/how-we-communicate)

**Tools:**
- [Timezone.io](https://timezone.io/) — team timezone visualization
- [WorldTimeBuddy](https://www.worldtimebuddy.com/) — meeting planning

---

