# Агентные системы: основы
## Что такое AI-агент и как он работает

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [08_Tools](../08_Tools/) — понимать function calling
- Пройти модуль [07_RAG](../07_RAG/) — понимать RAG

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить, что такое AI-агент и чем он отличается от LLM
- Описать ключевые компоненты агента
- Понимать цикл работы агента
- Оценивать типичные проблемы агентных систем

---

## 1. Что такое AI-агент

### 1.1 Определение

AI-агент — это система, использующая LLM для автономного выполнения задач через итеративный цикл:

```

┌─────────────────────────────────────────────────────────────┐
│                    AI Agent vs LLM                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LLM (без агента):                                          │
│  User Question → LLM → Single Answer                        │
│  Один запрос = один ответ                                   │
│                                                             │
│  AI Agent:                                                  │
│  Goal → [Think → Act → Observe → Think → Act...] → Result   │
│  Многошаговое выполнение с использованием инструментов      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Ключевые характеристики

```python

agent_characteristics = {
    "Автономность": "Агент сам решает, какие шаги предпринять",
    "Итеративность": "Может выполнять много шагов до достижения цели",
    "Tool use": "Использует инструменты для взаимодействия с миром",
    "Memory": "Помнит контекст и результаты предыдущих действий",
    "Goal-oriented": "Работает над достижением конкретной цели"
}
```

---

## 2. Компоненты агента

### 2.1 Архитектура

```

┌───────────────────────────────────────────────────────────┐
│                   Компоненты AI Agent                     │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                    AI Agent                          │ │
│  │                                                      │ │
│  │   ┌─────────┐  ┌─────────┐  ┌─────────────────┐    │   │
│  │   │  LLM    │  │ Memory  │  │     Tools       │    │   │
│  │   │ (Brain) │  │         │  │                 │    │   │
│  │   └────┬────┘  └────┬────┘  │ • search()      │    │   │
│  │        │            │       │ • calculate()   │    │   │
│  │        ▼            ▼       │ • browse()      │    │   │
│  │   ┌────────────────────┐    │ • code_exec()   │    │   │
│  │   │    Planning &      │    └─────────────────┘    │   │
│  │   │    Reasoning       │                           │   │
│  │   └────────────────────┘                           │   │
│  │                                                      │ │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

### 2.2 Компоненты детально

```python

agent_components = {
    "LLM (Brain)": {
        "role": "Принятие решений, рассуждения",
        "input": "Цель + контекст + история",
        "output": "Следующее действие или ответ"
    },
    
    "Memory": {
        "short_term": "Текущий контекст диалога",
        "long_term": "Сохранённые факты между сессиями",
        "working": "Промежуточные результаты"
    },
    
    "Tools": {
        "role": "Взаимодействие с внешним миром",
        "examples": ["Web search", "Code execution", "API calls", "File I/O"]
    },
    
    "Planning": {
        "role": "Разбиение задачи на шаги",
        "approaches": ["ReAct", "Plan-and-Execute", "Tree of Thoughts"]
    }
}
```

---

## 3. Цикл работы агента

### 3.1 Базовый цикл

```

┌─────────────────────────────────────────────────────────────┐
│                   Agent Loop (ReAct)                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. THOUGHT (Размышление)                                   │
│     "Мне нужно найти информацию о погоде в Москве"          │
│                    │                                        │
│                    ▼                                        │
│  2. ACTION (Действие)                                       │
│     get_weather(city="Moscow")                              │
│                    │                                        │
│                    ▼                                        │
│  3. OBSERVATION (Наблюдение)                                │
│     {"temp": 15, "condition": "sunny"}                      │
│                    │                                        │
│                    ▼                                        │
│  4. THOUGHT (Следующее размышление)                         │
│     "Получил данные, могу сформировать ответ"               │
│                    │                                        │
│                    ▼                                        │
│  5. FINAL ANSWER                                            │
│     "В Москве сейчас 15°C, солнечно"                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Реализация цикла

```python

def agent_loop(goal: str, max_iterations: int = 10):
    messages = [{"role": "user", "content": goal}]
    
    for i in range(max_iterations):
        # Получаем решение от LLM
        response = llm.generate(
            messages=messages,
            tools=available_tools
        )
        
        # Проверяем, есть ли tool calls
        if response.tool_calls:
            for call in response.tool_calls:
                # Выполняем инструмент
                result = execute_tool(call.name, call.arguments)
                
                # Добавляем результат в контекст
                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                })
        else:
            # Нет tool calls = финальный ответ
            return response.content
    
    return "Max iterations reached"
```

---

## 4. Примеры агентных систем

### 4.1 Coding Agent

```python
# Агент для написания кода

coding_agent_tools = [
    {"name": "write_file", "description": "Write code to a file"},
    {"name": "read_file", "description": "Read file contents"},
    {"name": "run_code", "description": "Execute Python code"},
    {"name": "run_tests", "description": "Run test suite"},
    {"name": "search_docs", "description": "Search documentation"}
]

# Пример задачи: "Create a REST API for user management"

# Agent loop:
# 1. THOUGHT: Need to create project structure
# 2. ACTION: write_file("app.py", "from flask import Flask...")
# 3. OBSERVATION: File created
# 4. THOUGHT: Need to add routes
# 5. ACTION: write_file("routes.py", "...")
# ... (продолжает до завершения)
```

### 4.2 Research Agent

```python
# Агент для исследования

research_agent_tools = [
    {"name": "web_search", "description": "Search the web"},
    {"name": "read_page", "description": "Read web page content"},
    {"name": "take_notes", "description": "Save important information"},
    {"name": "summarize", "description": "Summarize findings"}
]

# Пример: "Research the current state of quantum computing"

# Agent iteratively:
# - Searches for recent articles
# - Reads relevant pages
# - Takes notes on key findings
# - Synthesizes into final report
```

---

## 5. Типичные проблемы агентов

### 5.1 Проблемы и решения

```python

agent_problems = {
    "Зацикливание": {
        "problem": "Агент повторяет одни и те же действия",
        "solutions": ["Max iterations", "Loop detection", "Diversified prompting"]
    },
    
    "Галлюцинации": {
        "problem": "Агент выдумывает результаты действий",
        "solutions": ["Ground in tool outputs", "Verify results"]
    },
    
    "Неэффективность": {
        "problem": "Слишком много шагов для простых задач",
        "solutions": ["Better planning", "Caching", "Parallel execution"]
    },
    
    "Потеря контекста": {
        "problem": "Забывает начальную цель",
        "solutions": ["Persistent goal in system prompt", "Summarization"]
    },
    
    "Ненадёжность": {
        "problem": "Разные результаты при повторах",
        "solutions": ["Lower temperature", "Structured outputs", "Validation"]
    }
}
```

### 5.2 Когда агенты работают плохо

```python

agents_struggle_with = [
    "Очень длинные задачи (>20-30 шагов)",
    "Задачи требующие точных вычислений",
    "Задачи с неясными критериями успеха",
    "Real-time задачи (низкая latency)",
    "Задачи требующие human judgment"
]
```

---

## 6. Фреймворки для агентов

### 6.1 Популярные фреймворки

```python

agent_frameworks = {
    "LangChain": {
        "pros": "Большая экосистема, много интеграций",
        "cons": "Сложный, много абстракций",
        "use_for": "Прототипы, эксперименты"
    },
    "LangGraph": {
        "pros": "Граф-based оркестрация, хороший контроль",
        "cons": "Кривая обучения",
        "use_for": "Сложные multi-agent системы"
    },
    "CrewAI": {
        "pros": "Простой API для multi-agent",
        "cons": "Менее гибкий",
        "use_for": "Командная работа агентов"
    },
    "AutoGPT": {
        "pros": "Полная автономность",
        "cons": "Нестабильный, дорогой",
        "use_for": "Демонстрации (не production)"
    }
}
```

---

## 💡 Key Takeaways

- **Агент = LLM + Tools + Memory + Loop** — агент использует LLM для принятия решений и инструменты для действий

- **Итеративный цикл** — Think → Act → Observe → Repeat до достижения цели

- **Агенты нестабильны** — склонны к зацикливанию, галлюцинациям и неэффективности. Требуют тщательного проектирования

- **Не для всех задач** — агенты плохо работают на длинных, неопределённых или realtime задачах

---

## 🚀 Next Steps

**Related Modules:**

- [11_Agents_Architecture](../11_Agents_Architecture/) — Архитектуры агентных систем

---


