# Prompt Engineering: базовые принципы
## Промпт как интерфейс программирования LLM

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [03_LLM_Basics](../03_LLM_Basics/) — как работают LLM
- Понимать токенизацию и генерацию текста
- Иметь доступ к ChatGPT, Claude или другому LLM

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить роли System, User и Assistant в диалоге
- Составлять эффективные промпты с чёткими инструкциями
- Применять zero-shot и few-shot подходы
- Избегать типичных ошибок промптинга
- Структурировать промпты для разных задач

---

## 1. Что такое Prompt Engineering

### 1.1 Промпт как интерфейс

Prompt engineering — это искусство и наука составления инструкций для LLM. Промпт — это интерфейс между человеком и моделью:

```

┌─────────────────────────────────────────────────────────────┐
│                   Prompt Engineering                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Традиционное программирование:                             │
│  Код → Компилятор → Результат                               │
│                                                              │
│  Программирование LLM:                                      │
│  Промпт → LLM → Результат                                   │
│                                                              │
│  Промпт = программа на естественном языке                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Почему это важно

```python
# Один и тот же вопрос, разные промпты → разные результаты

# Плохой промпт
prompt_bad = "напиши про питон"
# Результат: непредсказуемый, может быть о змее или языке

# Хороший промпт
prompt_good = """
Напиши краткое введение в язык программирования Python для начинающих.
Формат: 3 абзаца по 2-3 предложения.
Тон: дружелюбный, но профессиональный.
Включи: историю создания, основные преимущества, области применения.
"""
# Результат: структурированный, предсказуемый
```

### 1.3 Принципы эффективных промптов

```python

principles = {
    "Clarity": "Будь конкретен и однозначен",
    "Context": "Дай достаточно контекста",
    "Constraints": "Укажи ограничения и формат",
    "Examples": "Покажи примеры желаемого результата",
    "Iteration": "Улучшай промпт итеративно"
}
```

---

## 2. Структура диалога: System, User, Assistant

### 2.1 Три роли

Современные chat-модели работают с тремя ролями:

```

┌─────────────────────────────────────────────────────────────┐
│              Роли в Chat Completion API                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  System (системное сообщение)                               │
│  └── Задаёт поведение, роль, ограничения ассистента         │
│      Пользователь обычно не видит                           │
│      Устанавливается один раз в начале                      │
│                                                              │
│  User (пользователь)                                        │
│  └── Сообщения пользователя                                 │
│      Вопросы, запросы, данные                               │
│                                                              │
│  Assistant (ассистент)                                      │
│  └── Ответы модели                                          │
│      Можно включать в историю для контекста                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 System prompt

System prompt задаёт "персону" и правила для ассистента:

```python
# Пример system prompt для разных задач

# Для кодинг-ассистента
system_coding = """
You are an expert Python developer. 
Follow these rules:
- Write clean, idiomatic Python code
- Include type hints
- Add docstrings to functions
- Prefer simple solutions over clever ones
- If the question is unclear, ask for clarification
"""

# Для customer support бота
system_support = """
You are a friendly customer support agent for TechCorp.
Rules:
- Be polite and empathetic
- If you don't know the answer, say so
- Never make up product information
- Offer to escalate to human if needed
- Keep responses concise (max 3 sentences)
"""

# Для переводчика
system_translator = """
You are a professional translator from English to Russian.
Rules:
- Preserve the tone and style of the original
- Keep technical terms in English with Russian explanation
- If a phrase is ambiguous, provide alternatives
"""
```

### 2.3 Эффективный system prompt

```python
# Структура хорошего system prompt

system_template = """
# Роль
You are [ROLE] with expertise in [DOMAIN].

# Цель
Your goal is to [PRIMARY OBJECTIVE].

# Правила
Follow these rules:
- [Rule 1]
- [Rule 2]
- [Rule 3]

# Формат ответа
[Describe expected format]

# Ограничения
- [What NOT to do]
- [Boundaries]
"""
```

### 2.4 Пример полного диалога

```python

from openai import OpenAI
client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a helpful coding assistant. Be concise."
    },
    {
        "role": "user",
        "content": "How do I read a JSON file in Python?"
    },
    {
        "role": "assistant",
        "content": "```python\nimport json\n\nwith open('file.json') as f:\n    data = json.load(f)\n```"
    },
    {
        "role": "user",
        "content": "How do I handle if the file doesn't exist?"
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)
```

---

## 3. Явные инструкции

### 3.1 Принцип явности

LLM не читают мысли — нужно явно указывать, что вы хотите:

```python
# ❌ Неявно (плохо)
prompt_vague = "Объясни машинное обучение"

# ✅ Явно (хорошо)
prompt_explicit = """
Объясни машинное обучение для аудитории: менеджеры без технического бэкграунда.

Требования:
- Длина: 200-300 слов
- Избегай технических терминов или объясняй их
- Приведи 2-3 примера из бизнеса
- Структура: определение, как работает, примеры применения
"""
```

### 3.2 Компоненты хорошего промпта

```

┌─────────────────────────────────────────────────────────────┐
│          Компоненты эффективного промпта                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Задача (Task)                                           │
│     Что нужно сделать                                       │
│     "Summarize", "Translate", "Explain", "Generate"         │
│                                                              │
│  2. Контекст (Context)                                      │
│     Фоновая информация                                      │
│     "For a technical audience", "In the context of..."      │
│                                                              │
│  3. Входные данные (Input)                                  │
│     Данные для обработки                                    │
│     Текст, код, вопрос                                      │
│                                                              │
│  4. Формат (Format)                                         │
│     Как должен выглядеть ответ                              │
│     "As a bullet list", "In JSON", "In 3 paragraphs"        │
│                                                              │
│  5. Тон (Tone)                                              │
│     Стиль ответа                                            │
│     "Professional", "Friendly", "Technical"                 │
│                                                              │
│  6. Примеры (Examples)                                      │
│     Образцы желаемого результата                            │
│     Few-shot examples                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Примеры явных инструкций

```python
# Пример 1: Суммаризация
summarization_prompt = """
Task: Summarize the following article.

Requirements:
- Length: 2-3 sentences
- Focus on: main findings and conclusions
- Audience: executives without technical background
- Tone: professional

Article:
{article_text}

Summary:
"""

# Пример 2: Код-ревью
code_review_prompt = """
Review the following Python code for:
1. Bugs and potential errors
2. Performance issues
3. Code style (PEP 8 compliance)
4. Security vulnerabilities

For each issue found, provide:
- Location (line number or code snippet)
- Severity (Critical/High/Medium/Low)
- Description
- Suggested fix

Code:
```python
{code}

```

Review:
"""

# Пример 3: Перевод
translation_prompt = """
Translate the following text from English to Russian.

Requirements:
- Preserve technical terminology in English with Russian explanation in parentheses
- Maintain the formal tone of the original
- Keep formatting (bullets, numbering)

Text:
{text}

Translation:
"""
```

---

## 4. Zero-shot и Few-shot

### 4.1 Zero-shot

Zero-shot — выполнение задачи без примеров:

```python
# Zero-shot: просто инструкция
zero_shot_prompt = """
Classify the sentiment of the following review as 
Positive, Negative, or Neutral.

Review: "The product arrived quickly and works great!"

Sentiment:
"""

# Модель должна понять задачу из инструкции
```

### 4.2 Few-shot

Few-shot — демонстрация задачи через примеры:

```python
# Few-shot: инструкция + примеры
few_shot_prompt = """
Classify the sentiment of reviews as Positive, Negative, or Neutral.

Examples:
Review: "Excellent quality, highly recommend!"
Sentiment: Positive

Review: "Product broke after one week. Terrible."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Now classify:
Review: "The product arrived quickly and works great!"
Sentiment:
"""

# Примеры показывают модели ожидаемый формат
```

### 4.3 Когда что использовать

```python

comparison = {
    "Zero-shot": {
        "when": "Простые, стандартные задачи",
        "pros": "Меньше токенов, проще промпт",
        "cons": "Менее надёжно для сложных задач"
    },
    "Few-shot": {
        "when": "Сложные, нестандартные задачи; специфичный формат",
        "pros": "Более надёжно, контроль формата",
        "cons": "Больше токенов, нужны хорошие примеры"
    }
}

# Правило: начни с zero-shot, если не работает — добавь примеры
```

### 4.4 Подбор примеров

```python
# Хорошие примеры для few-shot

example_guidelines = {
    "Разнообразие": "Покрывайте разные случаи (edge cases)",
    "Репрезентативность": "Примеры должны быть похожи на реальные данные",
    "Качество": "Примеры должны быть правильными!",
    "Количество": "Обычно 2-5 примеров достаточно",
    "Порядок": "Последний пример важнее (recency bias)"
}

# Плохие примеры → плохие результаты!
```

---

## 5. Типичные ошибки

### 5.1 Слишком общий промпт

```python
# ❌ Плохо: слишком общий
bad_prompt = "Write about AI"

# ✅ Хорошо: конкретный
good_prompt = """
Write a 500-word article about AI for:
- Audience: business executives
- Focus: practical applications in retail
- Tone: professional but accessible
- Include: 3 specific use cases with ROI estimates
"""
```

### 5.2 Отсутствие формата

```python
# ❌ Плохо: формат не указан
bad_prompt = "List the benefits of Python"

# ✅ Хорошо: формат указан
good_prompt = """
List the top 5 benefits of Python for beginners.
Format:
1. [Benefit name] - [1-2 sentence explanation]
"""
```

### 5.3 Противоречивые инструкции

```python
# ❌ Плохо: противоречия
bad_prompt = """
Write a detailed technical explanation.
Keep it very brief.
Include all edge cases.
Make it simple for beginners.
"""
# Противоречит само себе!

# ✅ Хорошо: согласованные инструкции
good_prompt = """
Write a technical explanation of REST APIs.
Target audience: junior developers with basic programming knowledge.
Length: 300-400 words.
Include: definition, key concepts, one simple example.
"""
```

### 5.4 Игнорирование структуры

```python
# ❌ Плохо: всё в одном блоке
bad_prompt = "I have this data about sales in Q1 which was 100k and Q2 which was 150k and Q3 which was 120k and I want you to analyze trends and suggest what to do in Q4"

# ✅ Хорошо: структурированный промпт
good_prompt = """
Analyze the following quarterly sales data and provide recommendations.

Data:
- Q1: $100,000
- Q2: $150,000
- Q3: $120,000

Required analysis:
1. Trend analysis (what's the pattern?)
2. Key observations
3. Recommended actions for Q4

Format response as:
- Trend: [brief description]
- Observations: [bullet points]
- Recommendations: [numbered list with explanations]
"""
```

### 5.5 Слишком длинный промпт

```python
# ❌ Плохо: избыточный промпт
bad_prompt = """
I want you to help me with something very important and it's 
really critical that you understand what I'm asking. So basically,
I need you to, you know, take this text and kind of summarize it
in a way that makes sense. It should be clear and concise and
also comprehensive but not too long and also professional...
[продолжается ещё 500 слов]
"""

# ✅ Хорошо: лаконичный промпт
good_prompt = """
Summarize this text in 3 sentences. Be clear and professional.

Text: [text]
"""
```

---

## 6. Итеративное улучшение

### 6.1 Процесс разработки промпта

```

┌─────────────────────────────────────────────────────────────┐
│            Итеративный процесс промптинга                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Начать с простого                                       │
│     └── Базовая инструкция без наворотов                    │
│                                                              │
│  2. Протестировать                                          │
│     └── Попробовать на разных входных данных                │
│                                                              │
│  3. Проанализировать ошибки                                 │
│     └── Где модель ошибается? Почему?                       │
│                                                              │
│  4. Уточнить промпт                                         │
│     └── Добавить инструкции для проблемных случаев          │
│                                                              │
│  5. Повторить                                               │
│     └── Тестировать → улучшать → тестировать                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Пример итерации

```python
# Итерация 1: Базовый промпт
v1 = "Extract names from text: {text}"
# Проблема: модель возвращает все слова с заглавной буквы

# Итерация 2: Уточнение
v2 = "Extract only person names (not places or companies) from text: {text}"
# Проблема: модель иногда возвращает прозвища

# Итерация 3: Формат
v3 = """
Extract person names from the text.
Return as JSON array: ["Name1", "Name2"]
Include only full names, not nicknames or titles.

Text: {text}
"""
# Проблема: иногда пустой массив где должен быть null

# Итерация 4: Edge cases
v4 = """
Extract person names from the text.

Rules:
- Include only full names of real people
- Exclude nicknames, titles, fictional characters
- Return JSON array if names found
- Return null if no names found
- If uncertain, include with "(uncertain)" suffix

Text: {text}

Output (JSON):
"""
```

### 6.3 A/B тестирование промптов

```python
# Сравнение разных версий промптов

def compare_prompts(prompt_a, prompt_b, test_cases):
    results = {"prompt_a": [], "prompt_b": []}
    
    for test in test_cases:
        response_a = call_llm(prompt_a.format(**test))
        response_b = call_llm(prompt_b.format(**test))
        
        # Оцениваем качество (автоматически или вручную)
        score_a = evaluate(response_a, test["expected"])
        score_b = evaluate(response_b, test["expected"])
        
        results["prompt_a"].append(score_a)
        results["prompt_b"].append(score_b)
    
    return {
        "prompt_a_avg": mean(results["prompt_a"]),
        "prompt_b_avg": mean(results["prompt_b"])
    }
```

---

## 7. Шаблоны промптов

### 7.1 Универсальный шаблон

```python

universal_template = """
# Роль (опционально)
You are [role] with expertise in [domain].

# Задача
[Clear task description]

# Контекст
[Background information, constraints]

# Входные данные
[User's input or data to process]

# Формат вывода
[Expected format of the response]

# Примеры (опционально)
[Few-shot examples]
"""
```

### 7.2 Шаблоны для типовых задач

```python
# Суммаризация
summarize_template = """
Summarize the following text in {length} sentences.
Focus on: {focus_points}
Audience: {audience}

Text:
{text}

Summary:
"""

# Классификация
classify_template = """
Classify the following {item_type} into one of these categories:
{categories}

{item_type}: {item}

Category:
"""

# Извлечение данных
extract_template = """
Extract the following information from the text:
{fields}

If a field is not found, write "Not found".
Return as JSON.

Text:
{text}

Extracted data:
"""

# Генерация контента
generate_template = """
Write a {content_type} about {topic}.

Requirements:
- Length: {length}
- Tone: {tone}
- Audience: {audience}
- Include: {must_include}
- Avoid: {avoid}

{content_type}:
"""
```

---

## 8. Практические советы

### 8.1 Чеклист промптинга

```python

checklist = [
    "✅ Задача чётко описана",
    "✅ Указана целевая аудитория/контекст",
    "✅ Формат ответа задан",
    "✅ Нет противоречий в инструкциях",
    "✅ Есть примеры (если нужны)",
    "✅ Промпт протестирован на edge cases",
    "✅ Промпт лаконичен (без лишних слов)"
]
```

### 8.2 Debugging промптов

```python

debugging_strategies = {
    "Проблема: модель не следует формату": [
        "Добавьте примеры",
        "Укажите формат в конце промпта",
        "Используйте JSON mode если доступен"
    ],
    
    "Проблема: ответ слишком длинный": [
        "Укажите явный лимит: 'в 2-3 предложениях'",
        "Добавьте 'Be concise' в system prompt"
    ],
    
    "Проблема: ответ слишком короткий": [
        "Укажите минимальную длину",
        "Попросите 'detailed' или 'comprehensive'"
    ],
    
    "Проблема: галлюцинации": [
        "Добавьте 'If you don't know, say so'",
        "Попросите цитировать источники",
        "Используйте RAG"
    ]
}
```

---

## 💡 Key Takeaways

- **Промпт = программа** — Промпт это интерфейс программирования LLM. Чем лучше промпт, тем лучше результат

- **System/User/Assistant** — Три роли в диалоге. System задаёт поведение, User задаёт вопрос, Assistant отвечает

- **Явность критична** — Не надейтесь, что модель "поймёт". Указывайте задачу, формат, тон, ограничения явно

- **Few-shot помогает** — Примеры показывают модели желаемый формат. Начните с zero-shot, добавьте примеры если нужно

- **Итеративное улучшение** — Разработка промпта это процесс. Тестируйте, анализируйте ошибки, улучшайте

---

## 🚀 Next Steps

**Related Modules:**

- [06_Prompt_Advanced](../06_Prompt_Advanced/) — Продвинутый промптинг (CoT, self-reflection)
- [07_RAG](../07_RAG/) — RAG для работы с данными

**Practice Ideas:**

1. Создайте промпт для суммаризации и протестируйте на 5 разных статьях
2. Сравните zero-shot и few-shot на задаче классификации
3. Возьмите свой старый промпт и улучшите по чеклисту

**Going Deeper:**

- OpenAI Prompt Engineering Guide
- Anthropic Prompt Engineering Guide
- Learn Prompting (learnprompting.org)

---

## 📚 Additional Resources

**Guides:**

- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Learn Prompting](https://learnprompting.org/)

**Tools:**

- [OpenAI Playground](https://platform.openai.com/playground) — тестирование промптов
- [Prompt Perfect](https://promptperfect.jina.ai/) — оптимизация промптов

---


