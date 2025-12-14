# Продвинутый Prompt Engineering
## Chain of Thought, декомпозиция, self-reflection и guardrails

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [05_Prompt_Basics](../05_Prompt_Basics/) — базовые принципы
- Уметь составлять структурированные промпты
- Иметь опыт работы с few-shot примерами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять Chain of Thought для сложных задач
- Декомпозировать сложные задачи на подзадачи
- Использовать self-reflection для улучшения ответов
- Контролировать формат вывода (structured output)
- Внедрять guardrails для безопасности

---

## 1. Chain of Thought (CoT)

### 1.1 Что такое Chain of Thought

Chain of Thought — техника, заставляющая модель рассуждать пошагово:

```
┌─────────────────────────────────────────────────────────────┐
│                   Chain of Thought                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Без CoT:                                                   │
│  Q: Сколько будет 17 × 23?                                  │
│  A: 391 ✓ (или ошибка)                                      │
│                                                              │
│  С CoT:                                                     │
│  Q: Сколько будет 17 × 23? Рассуждай пошагово.              │
│  A: Разобью на части:                                       │
│     17 × 23 = 17 × 20 + 17 × 3                              │
│     17 × 20 = 340                                           │
│     17 × 3 = 51                                             │
│     340 + 51 = 391 ✓                                        │
│                                                              │
│  Пошаговое рассуждение улучшает точность!                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Почему CoT работает

```python
# Гипотезы, почему CoT улучшает результаты:

cot_hypotheses = {
    "Computation offloading": """
        Модель "думает" в токенах. Больше токенов = больше вычислений.
        CoT увеличивает количество токенов между вопросом и ответом.
    """,
    
    "Error correction": """
        При пошаговом рассуждении модель может заметить ошибку
        на промежуточном шаге и исправить её.
    """,
    
    "Pattern matching": """
        Модель видела много примеров рассуждений в training data.
        CoT активирует эти паттерны.
    """
}
```

### 1.3 Способы вызвать CoT

```python
# Способ 1: Zero-shot CoT
zero_shot_cot = """
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
Each can has 3 tennis balls. How many tennis balls does he have now?

Let's think step by step.
"""

# Способ 2: Few-shot CoT
few_shot_cot = """
Q: There are 15 trees in the grove. Workers will plant trees today.
After they are done, there will be 21 trees. How many trees did they plant?
A: We start with 15 trees. After planting, we have 21 trees.
So they must have planted 21 - 15 = 6 trees.
The answer is 6.

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
Each can has 3 tennis balls. How many tennis balls does he have now?
A:
"""

# Способ 3: Явная инструкция
explicit_cot = """
Solve the following problem. Show your reasoning step by step.
After showing the steps, provide the final answer on a new line 
starting with "Answer: ".

Problem: [problem]
"""
```

### 1.4 Когда использовать CoT

```python
cot_effectiveness = {
    "Хорошо работает": [
        "Математические задачи",
        "Логические головоломки",
        "Многошаговые рассуждения",
        "Анализ причин и следствий",
        "Планирование"
    ],
    "Менее полезно": [
        "Простые фактические вопросы",
        "Креативное письмо",
        "Перевод",
        "Суммаризация"
    ]
}
```

---

## 2. Декомпозиция задач

### 2.1 Принцип декомпозиции

Сложные задачи разбиваются на простые подзадачи:

```
┌─────────────────────────────────────────────────────────────┐
│                    Декомпозиция                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Сложная задача                                             │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Подзадача A    →  Результат A                   │   │
│  │  2. Подзадача B(A) →  Результат B                   │   │
│  │  3. Подзадача C(B) →  Финальный результат           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Каждая подзадача проще и надёжнее                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Пример: анализ документа

```python
# Вместо одного сложного промпта
bad_approach = """
Analyze this document, extract key entities, summarize it,
identify sentiment, and generate action items.
Document: {document}
"""

# Декомпозиция на подзадачи
step_1 = """
Extract all named entities (people, organizations, dates) from this document.
Return as JSON: {"people": [], "organizations": [], "dates": []}
Document: {document}
"""

step_2 = """
Summarize this document in 3 bullet points.
Document: {document}
"""

step_3 = """
Based on this document, what is the overall sentiment?
Options: Positive, Negative, Neutral, Mixed
Document: {document}
"""

step_4 = """
Based on this document summary, generate 3 action items.
Summary: {summary}
"""

# Объединяем результаты
def analyze_document(document):
    entities = call_llm(step_1.format(document=document))
    summary = call_llm(step_2.format(document=document))
    sentiment = call_llm(step_3.format(document=document))
    actions = call_llm(step_4.format(summary=summary))
    
    return {
        "entities": entities,
        "summary": summary,
        "sentiment": sentiment,
        "actions": actions
    }
```

### 2.3 Промпт для декомпозиции

```python
decomposition_prompt = """
I need to accomplish the following complex task:
{task_description}

First, break this down into smaller, manageable subtasks.
List each subtask with:
1. Clear objective
2. Required inputs
3. Expected output

Then solve each subtask in order, showing your work.
Finally, combine the results into the final answer.
"""
```

---

## 3. Self-Reflection и Self-Critique

### 3.1 Принцип self-reflection

Модель проверяет и улучшает собственные ответы:

```python
# Базовый паттерн self-reflection

self_reflection_prompt = """
# Initial task
{task}

# Your initial response
{initial_response}

# Self-critique
Now critically review your response:
1. Is it accurate and factually correct?
2. Does it fully address the question?
3. Are there any logical errors?
4. What could be improved?

# Improved response
Based on your critique, provide an improved response:
"""
```

### 3.2 Паттерн "Generate then Refine"

```python
# Шаг 1: Генерация
generation_prompt = """
Write a product description for {product}.
Target audience: {audience}
"""

# Шаг 2: Критика
critique_prompt = """
Review this product description and identify:
1. Strengths (what works well)
2. Weaknesses (what could be improved)
3. Missing elements
4. Factual errors if any

Description: {generated_description}

Critique:
"""

# Шаг 3: Улучшение
refine_prompt = """
Improve this product description based on the critique.

Original: {generated_description}
Critique: {critique}

Improved description:
"""
```

### 3.3 Паттерн Reflection

```python
reflection_prompt = """
You are solving a {task_type} problem.

TASK: {task}

Follow this process:
1. THINK: Write your initial thoughts and approach
2. SOLVE: Provide your solution
3. VERIFY: Check your solution for errors
4. REFLECT: What could be wrong? Any edge cases?
5. FINAL: Your final answer (corrected if needed)

Format your response with these headers.
"""
```

---

## 4. Контроль формата вывода

### 4.1 Structured Output

Контроль формата критичен для интеграции LLM в системы:

```python
# JSON output
json_prompt = """
Extract information from the text and return as JSON.

Required format:
{
    "name": "string",
    "email": "string or null",
    "company": "string or null",
    "sentiment": "positive|negative|neutral"
}

Text: {text}

JSON:
"""

# Markdown output
markdown_prompt = """
Summarize this article.

Format your response as:
# Summary
[2-3 sentence summary]

## Key Points
- [point 1]
- [point 2]
- [point 3]

## Conclusion
[1 sentence conclusion]
"""
```

### 4.2 JSON Mode (OpenAI)

```python
from openai import OpenAI
client = OpenAI()

# Использование JSON mode
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You extract data and respond in JSON format."
        },
        {
            "role": "user", 
            "content": f"Extract name and email from: {text}"
        }
    ]
)

# Гарантированно валидный JSON!
data = json.loads(response.choices[0].message.content)
```

### 4.3 Structured Outputs с Pydantic

```python
from pydantic import BaseModel
from openai import OpenAI

class Person(BaseModel):
    name: str
    age: int
    email: str | None

client = OpenAI()

response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "user", "content": "John is 30 years old, email: john@example.com"}
    ],
    response_format=Person
)

person = response.choices[0].message.parsed
print(person.name)  # "John"
print(person.age)   # 30
```

---

## 5. Guardrails

### 5.1 Что такое Guardrails

Guardrails — ограничения, предотвращающие нежелательное поведение:

```
┌─────────────────────────────────────────────────────────────┐
│                      Guardrails                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Input Guardrails         Output Guardrails                 │
│  ─────────────────        ──────────────────                │
│  • Фильтрация запросов    • Проверка ответа                 │
│  • Определение intent     • Фильтрация контента             │
│  • Rate limiting          • Валидация формата               │
│  • PII detection          • Fact-checking                   │
│                                                              │
│      User Input → [Input Guard] → LLM → [Output Guard] →    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Guardrails в System Prompt

```python
system_with_guardrails = """
You are a customer support assistant for TechCorp.

## What you CAN do:
- Answer questions about our products
- Help with order status
- Provide technical troubleshooting
- Escalate to human support

## What you CANNOT do:
- Discuss competitors
- Make promises about refunds without approval
- Share internal company information
- Provide medical, legal, or financial advice
- Generate harmful, illegal, or inappropriate content

## If asked about something you cannot do:
Politely decline and offer to help with something else.
Example: "I'm not able to help with that, but I can assist you with..."

## Always:
- Be polite and professional
- Admit when you don't know something
- Suggest escalation for complex issues
"""
```

### 5.3 Программные Guardrails

```python
# Пример программных guardrails

def apply_guardrails(user_input, llm_output):
    # Input guardrails
    if contains_pii(user_input):
        user_input = redact_pii(user_input)
    
    if is_prompt_injection(user_input):
        return "I cannot process this request."
    
    # Output guardrails
    if contains_harmful_content(llm_output):
        return "I apologize, but I cannot provide that information."
    
    if not is_valid_format(llm_output, expected_format):
        return retry_with_format_instruction()
    
    return llm_output

def is_prompt_injection(text):
    """Детекция попыток prompt injection"""
    suspicious_patterns = [
        "ignore previous instructions",
        "forget your rules",
        "you are now",
        "new instructions:"
    ]
    return any(p in text.lower() for p in suspicious_patterns)
```

### 5.4 NeMo Guardrails (NVIDIA)

```python
# Пример использования NeMo Guardrails

# config.yml
"""
models:
  - type: main
    engine: openai
    model: gpt-4

rails:
  input:
    flows:
      - check jailbreak
      - check toxicity
  output:
    flows:
      - check facts
      - check hallucination
"""

from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(
    messages=[{"role": "user", "content": user_message}]
)
```

---

## 6. Продвинутые техники

### 6.1 Self-Consistency

Генерация нескольких ответов и выбор консенсуса:

```python
def self_consistency(prompt, n=5):
    """Генерируем несколько ответов и выбираем наиболее частый"""
    responses = []
    for _ in range(n):
        response = call_llm(prompt, temperature=0.7)
        answer = extract_answer(response)
        responses.append(answer)
    
    # Голосование
    from collections import Counter
    votes = Counter(responses)
    return votes.most_common(1)[0][0]

# Пример
prompt = "What is 17 * 23? Think step by step and give the answer."
final_answer = self_consistency(prompt, n=5)
# Если 4 из 5 ответов = 391, то 391 — финальный ответ
```

### 6.2 Tree of Thoughts (ToT)

```python
# Tree of Thoughts: исследование нескольких путей рассуждения

tot_prompt = """
Problem: {problem}

Generate 3 different approaches to solve this problem.
For each approach:
1. Describe the approach
2. List pros and cons
3. Estimate likelihood of success (1-10)

Then choose the best approach and execute it.
"""
```

### 6.3 ReAct (Reasoning + Acting)

```python
# ReAct: чередование рассуждений и действий

react_prompt = """
You have access to these tools:
- search(query): Search the web
- calculate(expression): Calculate math
- lookup(term): Look up in knowledge base

Format:
Thought: [your reasoning]
Action: [tool_name(args)]
Observation: [result from tool]
... (repeat as needed)
Final Answer: [your answer]

Question: {question}
"""
```

---

## 7. Best Practices

### 7.1 Чеклист продвинутого промптинга

```python
advanced_checklist = [
    "✅ Используйте CoT для сложных рассуждений",
    "✅ Декомпозируйте сложные задачи",
    "✅ Применяйте self-reflection для важных ответов",
    "✅ Контролируйте формат вывода",
    "✅ Внедряйте guardrails для безопасности",
    "✅ Тестируйте на edge cases",
    "✅ Измеряйте качество систематически"
]
```

### 7.2 Когда что применять

```python
technique_selection = {
    "Chain of Thought": "Математика, логика, многошаговые задачи",
    "Декомпозиция": "Сложные задачи, требующие разных навыков",
    "Self-reflection": "Важные ответы, где нужна точность",
    "Structured output": "Интеграция с системами, парсинг",
    "Guardrails": "Production системы, безопасность",
    "Self-consistency": "Когда нужна высокая уверенность"
}
```

---

## 💡 Key Takeaways

- **Chain of Thought** — заставляет модель рассуждать пошагово. Простое добавление "Let's think step by step" улучшает результаты

- **Декомпозиция** — сложные задачи разбиваются на простые подзадачи. Каждая подзадача решается надёжнее

- **Self-reflection** — модель проверяет и улучшает собственные ответы. Generate → Critique → Refine

- **Structured output** — контроль формата критичен для интеграции. Используйте JSON mode где возможно

- **Guardrails** — защита от нежелательного поведения. Обязательны для production систем

---

## 🚀 Next Steps

**Related Modules:**

- [07_RAG](../07_RAG/) — RAG для работы с данными
- [10_Agents_Basics](../10_Agents_Basics/) — AI-агенты

**Practice Ideas:**

1. Примените CoT к математической задаче и сравните с обычным промптом
2. Декомпозируйте сложную задачу на 3-4 подзадачи
3. Создайте промпт с self-reflection для code review

---

## 📚 Additional Resources

**Papers:**

- [Chain of Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Self-Consistency](https://arxiv.org/abs/2203.11171)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)
- [ReAct](https://arxiv.org/abs/2210.03629)

**Tools:**

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails)

---

