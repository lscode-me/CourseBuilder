# Engineering Strategy
## Стратегическое планирование и организационное развитие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь опыт управления несколькими командами
- Понимать основы предыдущих модулей курса
- Интересоваться стратегической работой в engineering

**Recommended prior modules:**

- [17_SeniorLeadership](../17_SeniorLeadership/) — senior leadership
- [12_ScalingTeams](../12_ScalingTeams/) — scaling teams

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Разрабатывать и артикулировать engineering strategy
- Связывать техническую работу с business goals
- Создавать roadmaps и планировать по quarters
- Принимать стратегические технические решения
- Измерять и коммуницировать прогресс

---

## 1. What is Engineering Strategy?

### 1.1 Definition

```

Engineering Strategy = 
  How engineering will achieve business goals
  + What technical investments to make
  + How to organize engineering work
  + Trade-offs we're making and why

```

### 1.2 Strategy vs Tactics

| Strategy | Tactics |
|----------|---------|
| Why и What | How |
| Quarters/Years | Weeks/Months |
| Direction | Execution |
| Choices | Actions |
| Trade-offs | Implementation |

### 1.3 Components of Eng Strategy

```

1. Vision: Where we're going
2. Principles: How we make decisions
3. Investments: Where we put resources
4. Organization: How we structure teams
5. Roadmap: Sequence of work

```

---

## 2. Connecting to Business

### 2.1 Business → Engineering

```

Company Strategy
     ↓
Business Goals (revenue, growth, efficiency)
     ↓
Product Strategy (what to build)
     ↓
Engineering Strategy (how to build it)
     ↓
Team Plans (who builds what)

```

### 2.2 Understanding Business Goals

**Questions to ask:**
```

- What are company's top 3 priorities?
- What metrics matter most?
- What's the growth plan?
- What's the competitive landscape?
- What bets are we making?

```

### 2.3 Translating to Engineering

**Business goal:** Increase revenue 50%

**Engineering questions:**
```

- Can current system scale 50%?
- What bottlenecks exist?
- What features drive revenue?
- What speed of delivery is needed?
- What reliability is required?

```

**Engineering strategy might include:**
```

- Scale infrastructure 2x
- Improve deployment speed 3x
- Invest in revenue-driving features
- Reduce incidents by 50%

```

---

## 3. Strategic Decision Making

### 3.1 Framework: Build vs Buy

```

Consider:

- Core competency? → Build
- Commodity? → Buy
- Time to market critical? → Buy
- Long-term cost? → Calculate TCO
- Strategic importance? → Build if yes

```

### 3.2 Technical Debt Decisions

```

When to pay down:

- Blocking feature development
- Causing reliability issues
- Slowing velocity significantly
- Creating security risks

When to accept:

- One-time feature
- Short-lived system
- Speed matters more
- Will be replaced anyway

```

### 3.3 Platform vs Product

```

Platform investment когда:

- Multiple teams need similar capabilities
- Consistency matters (security, compliance)
- Scale benefits exceed build cost
- Clear internal customers exist

```

### 3.4 Decision Document Template

```markdown
## Decision: [Name]

### Context
What's the situation?

### Decision
What we're choosing

### Alternatives Considered
What else we looked at

### Trade-offs
What we're gaining and giving up

### Consequences
What changes because of this

```

---

## 4. Planning Cycles

### 4.1 Annual Planning

**Typical timeline:**
```

Q4: Planning for next year
- Review current year
- Define themes and goals
- Rough headcount plan
- Major investments

Output:

- Annual goals
- Investment areas
- Headcount plan
- Major milestones

```

### 4.2 Quarterly Planning

```

6 weeks before quarter:

- Review roadmap
- Capacity planning
- Dependencies identified

2 weeks before:

- Commitments finalized
- Resources allocated
- Risks identified

During quarter:

- Weekly progress tracking
- Adjustments as needed
- Mid-quarter review

```

### 4.3 Roadmap Management

**Good roadmap:**
```

- Tied to business goals
- Realistic commitments
- Flexibility built in
- Dependencies clear
- Regular updates

```

**Bad roadmap:**
```

- Wishful thinking
- No slack
- Never updated
- No rationale
- Everything is P0

```

---

## 5. Resource Allocation

### 5.1 Portfolio Allocation

**Typical split:**
```

60-70% - Product/Feature work
15-25% - Technical debt/Infrastructure
5-10%  - Innovation/Experimentation
5-10%  - Buffer/Unplanned

```

### 5.2 Headcount Planning

**Factors:**
```

- Business growth plans
- System scaling needs
- New product areas
- Attrition rates
- Build vs buy decisions

```

**Planning formula:**
```

Needed headcount = 
  Current work
  + New initiatives
  + Growth buffer
  - Efficiency gains
  + Attrition replacement

```

### 5.3 Team Investment Decisions

```

Where to invest:

- Areas with biggest business impact
- Bottlenecks that limit growth
- Strategic new capabilities
- Teams that are stretched thin

Where to reduce:

- Mature, stable areas
- Declining products
- Areas being deprecated
- Overstaffed teams

```

---

## 6. Technical Strategy

### 6.1 Architecture Strategy

```

Questions:

- What's our target architecture?
- What are current pain points?
- What should we standardize?
- What needs to stay flexible?
- How do we get from here to there?

```

### 6.2 Technology Choices

**Principles:**
```

- Boring technology for core systems
- New tech for isolated experiments
- Standardize where possible
- Support what you adopt

```

**Decision criteria:**
```

- Team expertise
- Community support
- Long-term viability
- Integration with existing systems
- Total cost of ownership

```

### 6.3 Technical Principles

**Example principles:**
```

1. Own our data — we control core data
2. Build for scale — design for 10x growth
3. Automate ops — reduce manual toil
4. Security by default — built in, not added
5. Measure everything — data-driven decisions

```

---

## 7. Measuring Progress

### 7.1 Engineering Metrics

**Delivery:**
```

- Deployment frequency
- Lead time for changes
- Change failure rate
- Time to restore service
(DORA metrics)

```

**Quality:**
```

- Incident rate
- Uptime/SLA
- Bug escape rate
- Customer-reported issues

```

**Productivity:**
```

- Developer satisfaction
- Time spent on toil
- Code review turnaround
- Build/test times

```

### 7.2 OKRs for Engineering

**Good engineering OKRs:**
```

Objective: Scale platform for growth

Key Results:

- Handle 2x current load
- 99.9% uptime
- Deploy 10x per day
- Reduce incidents by 50%

```

### 7.3 Communicating Progress

**To executives:**
```

- Business impact
- Goal progress
- Risks and blockers
- Resource needs

```

**To teams:**
```

- Why we're doing this
- How it connects to goals
- Progress and wins
- What's changing

```

---

## 8. Managing Change

### 8.1 Strategic Initiatives

**Types:**
```

- Technology migrations
- Platform builds
- Org restructures
- Process changes
- Culture shifts

```

### 8.2 Change Management

```

1. Create urgency — why now?
2. Build coalition — key supporters
3. Communicate vision — clear picture
4. Remove obstacles — unblock teams
5. Generate wins — show progress
6. Consolidate — don't declare victory early
7. Anchor in culture — make it stick

```

### 8.3 Common Pitfalls

```

❌ Top-down mandates without buy-in
❌ Changing everything at once
❌ No clear success metrics
❌ Underestimating resistance
❌ Moving on before change sticks

```

---

## 9. Strategic Communication

### 9.1 Engineering Narrative

```

Your narrative explains:

- Where engineering is going
- Why these choices
- What it enables
- How we'll get there

```

### 9.2 Stakeholder Communication

**Different audiences:**
```

Board/Executives:

- Business impact
- ROI of investments
- Risks and mitigations

Product:

- What's possible when
- Trade-offs of choices
- Capacity and velocity

Engineering:

- Technical direction
- Career opportunities
- Why decisions were made

```

### 9.3 Building Alignment

```

1. Share context broadly
2. Involve people in planning
3. Explain the "why"
4. Listen to feedback
5. Adjust when wrong
6. Follow through

```

---

## 10. Organizational Development

### 10.1 Team Topology

**Types:**
```

- Stream-aligned teams (features)
- Platform teams (infrastructure)
- Enabling teams (help others)
- Complicated subsystem teams (specialists)

```

### 10.2 Evolution Patterns

```

Early stage:

- Generalist teams
- Less specialization
- Move fast, break things

Growth stage:

- Some specialization
- Platform investment
- Process introduction

Scale stage:

- Specialized teams
- Mature platforms
- Efficient processes

```

### 10.3 Culture Development

```

Engineering culture includes:

- How we make decisions
- How we handle failure
- How we share knowledge
- How we treat each other
- How we grow people

```

---

## 11. Strategy Antipatterns

### 11.1 Common Mistakes

```

❌ Strategy that's not connected to business
❌ Too many priorities (everything is important)
❌ No clear trade-offs
❌ Strategy that never changes
❌ Strategy nobody knows about
❌ All strategy, no execution

```

### 11.2 Signs of Good Strategy

```

✓ Clear choices were made
✓ Trade-offs are explicit
✓ People can explain it
✓ Decisions align with it
✓ It evolved based on learning
✓ Results are tracked

```

---

## 12. Practical Strategy Process

### 12.1 Creating Strategy

```

1. Understand business context
2. Assess current state
3. Identify gaps and opportunities
4. Define principles and priorities
5. Create roadmap
6. Communicate broadly
7. Execute and adapt

```

### 12.2 Strategy Document Outline

```markdown
# Engineering Strategy FY25

## Executive Summary
Key points in 1 page

## Business Context
What business is trying to achieve

## Current State
Where engineering is today

## Strategic Priorities
Top 3-5 focus areas

## Investment Plan
Where resources go

## Roadmap
Major milestones by quarter

## Success Metrics
How we measure progress

## Risks and Mitigations
What could go wrong

```

### 12.3 Keeping Strategy Alive

```

- Quarterly reviews and updates
- Reference in planning decisions
- Celebrate aligned wins
- Learn from misses
- Adjust as business changes

```

---

## 💡 Key Takeaways

- **Business-connected:** Strategy must tie to business goals

- **Clear choices:** Real strategy says what you won't do

- **Trade-offs explicit:** Make the reasoning visible

- **Communicated broadly:** Strategy nobody knows doesn't work

- **Living document:** Update based on learning

---

## 🚀 Next Steps

**Related Modules:**

- [17_SeniorLeadership](../17_SeniorLeadership/) — leadership skills
- [12_ScalingTeams](../12_ScalingTeams/) — scaling foundations

**Practice Ideas:**

1. Draft a 1-page engineering strategy для вашей org
2. Определите топ-3 strategic priorities
3. Review как ваша текущая работа connects to business goals

**Going Deeper:**

- Strategic planning frameworks
- Technology strategy case studies
- Business strategy fundamentals

---

## 📚 Additional Resources

**Books:**

- "Good Strategy Bad Strategy" by Richard Rumelt — strategy fundamentals
- "The Art of Action" by Stephen Bungay — strategy execution
- "An Elegant Puzzle" by Will Larson — engineering management
- "Staff Engineer" by Will Larson — technical strategy

**Frameworks:**

- DORA metrics for engineering performance
- Team Topologies for organization design
- OKRs for goal setting

**Articles:**

- [Irrational Exuberance](https://lethain.com/) by Will Larson
- [Engineering Strategy](https://lethain.com/engineering-strategy/)
- [Carta's Engineering Ladder](https://carta.com/blog/engineering-ladders/)

---




