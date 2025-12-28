# Архитектуры агентных систем
## Single-agent, Multi-agent и оркестрация

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [10_Agents_Basics](../10_Agents_Basics/) — основы агентов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать single-agent и multi-agent архитектуры
- Описать паттерны оркестрации агентов
- Понимать проблемы наблюдаемости и стоимости
- Объяснить, почему агенты часто нестабильны

---

## 1. Single-Agent vs Multi-Agent

### 1.1 Single-Agent

```

┌─────────────────────────────────────────────────────────────┐
│                    Single-Agent                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User ──► Agent ──► Result                                  │
│                                                             │
│  Один агент выполняет все задачи.                           │
│                                                             │
│  Плюсы:                                                     │
│  + Простая архитектура                                      │
│  + Легко отлаживать                                         │
│  + Меньше latency                                           │
│                                                             │
│  Минусы:                                                    │
│  - Ограничен возможностями одной модели                     │
│  - Сложно масштабировать                                    │
│  - Один контекст для всего                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Multi-Agent

```

┌─────────────────────────────────────────────────────────────┐
│                    Multi-Agent                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User ──► Orchestrator ──┬──► Agent 1 (Research)            │
│                          ├──► Agent 2 (Code)                │
│                          └──► Agent 3 (Review)              │
│                                    │                        │
│                                    ▼                        │
│                               Aggregated Result             │
│                                                             │
│  Плюсы:                                                     │
│  + Специализация агентов                                    │
│  + Параллельное выполнение                                  │
│  + Разделение ответственности                               │
│                                                             │
│  Минусы:                                                    │
│  - Сложная оркестрация                                      │
│  - Больше API calls = дороже                                │
│  - Сложнее отлаживать                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Паттерны оркестрации

### 2.1 Sequential (Последовательный)

```python
# Агенты работают последовательно
def sequential_agents(task):
    # Каждый агент передаёт результат следующему
    research = research_agent.run(task)
    draft = writer_agent.run(research)
    final = editor_agent.run(draft)
    return final
```

### 2.2 Parallel (Параллельный)

```python
# Агенты работают параллельно
async def parallel_agents(task):
    # Запускаем одновременно
    results = await asyncio.gather(
        agent_a.run(task),
        agent_b.run(task),
        agent_c.run(task)
    )
    # Агрегируем результаты
    return aggregator.combine(results)
```

### 2.3 Hierarchical (Иерархический)

```

┌─────────────────────────────────────────────────────────────┐
│                   Hierarchical Agents                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    Manager Agent                            │
│                         │                                   │
│          ┌──────────────┼──────────────┐                    │
│          ▼              ▼              ▼                    │
│     Team Lead 1    Team Lead 2    Team Lead 3               │
│          │              │              │                    │
│     ┌────┴────┐    ┌────┴────┐    ┌────┴────┐               │
│     ▼         ▼    ▼         ▼    ▼         ▼               │
│  Worker   Worker  Worker  Worker  Worker  Worker            │
│                                                             │
│  Manager делегирует, Team Leads координируют,               │
│  Workers выполняют конкретные задачи.                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.4 Debate (Дебаты)

```python
# Агенты дебатируют для улучшения качества
def debate_agents(question, rounds=3):
    positions = []
    
    for round in range(rounds):
        # Agent A отвечает
        answer_a = agent_a.run(question, opposing_view=positions)
        positions.append(("A", answer_a))
        
        # Agent B критикует и отвечает
        answer_b = agent_b.run(question, opposing_view=positions)
        positions.append(("B", answer_b))
    
    # Judge выбирает лучший ответ
    return judge_agent.decide(positions)
```

---

## 3. Наблюдаемость и отладка

### 3.1 Проблемы

```python

observability_challenges = {
    "Сложные логи": "Много агентов = много логов",
    "Трассировка": "Сложно отследить путь выполнения",
    "Ошибки": "Непонятно, какой агент сломался",
    "Стоимость": "Трудно отследить затраты на каждого агента"
}
```

### 3.2 Инструменты

```python

observability_tools = {
    "LangSmith": "Трассировка LangChain agents",
    "Langfuse": "Open-source observability",
    "Weights & Biases": "ML experiment tracking",
    "Custom logging": "Структурированные логи"
}
```

---

## 4. Стоимость агентных систем

### 4.1 Факторы стоимости

```python

cost_factors = {
    "API calls": "Каждый шаг агента = API call",
    "Iterations": "Больше итераций = больше токенов",
    "Context": "Длинный контекст = дорого",
    "Retries": "Ошибки требуют повторов"
}

# Пример расчёта
example_task = {
    "steps": 15,
    "avg_tokens_per_step": 2000,
    "total_tokens": 30000,
    "cost_gpt4": 30000 / 1000 * 0.03,  # $0.90 input only!
}
```

### 4.2 Оптимизация стоимости

```python

cost_optimization = [
    "Использовать дешёвые модели для простых задач",
    "Кэшировать повторяющиеся запросы",
    "Ограничивать max_iterations",
    "Фильтровать контекст (не передавать всё)"
]
```

---

## 5. Почему агенты нестабильны

### 5.1 Источники нестабильности

```python

instability_sources = {
    "LLM stochasticity": "Вероятностная генерация → разные результаты",
    "Error propagation": "Ошибка на шаге N → ошибки на N+1, N+2...",
    "Prompt sensitivity": "Мелкие изменения промпта → большие изменения поведения",
    "Tool failures": "Внешние API могут падать",
    "Context overflow": "Потеря важной информации при длинном контексте"
}
```

### 5.2 Стратегии повышения стабильности

```python

stability_strategies = [
    "Снизить temperature до 0",
    "Использовать structured outputs",
    "Добавить валидацию на каждом шаге",
    "Ограничить scope задачи",
    "Использовать checkpoints и rollback"
]
```

---

## 💡 Key Takeaways

- **Single vs Multi-agent** — single проще, multi мощнее но сложнее

- **Паттерны оркестрации** — sequential, parallel, hierarchical, debate — выбор зависит от задачи

- **Observability критична** — без трассировки невозможно отлаживать multi-agent системы

- **Стоимость растёт быстро** — каждый шаг агента стоит денег, оптимизируйте

- **Нестабильность — главная проблема** — агенты требуют тщательного проектирования и валидации

---

## 🚀 Next Steps

**Related Modules:**

- [12_Market](../12_Market/) — Вендоры и модели LLM

---


