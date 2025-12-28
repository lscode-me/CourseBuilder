# Вендоры, модели и рынок LLM
## Кто делает модели, сравнение провайдеров

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [03_LLM_Basics](../03_LLM_Basics/) — как работают LLM
- Пройти модуль [04_Training](../04_Training/) — обучение моделей

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Описать основных игроков рынка LLM
- Сравнивать модели по характеристикам
- Выбирать модель под конкретную задачу
- Понимать различия open-source и проприетарных моделей

---

## 1. Основные игроки рынка

### 1.1 Проприетарные модели

```

┌─────────────────────────────────────────────────────────────┐
│                 Proprietary LLM Vendors                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  OpenAI (GPT-4, GPT-4o, o1, o3)                             │
│  ├── Лидер рынка, ChatGPT                                   │
│  ├── Сильный reasoning (o1, o3)                             │
│  └── Дорого, закрытые веса                                  │
│                                                             │
│  Anthropic (Claude 3, Claude 3.5, Claude 4)                 │
│  ├── Фокус на безопасности                                  │
│  ├── Длинный контекст (200K)                                │
│  └── Отличное следование инструкциям                        │
│                                                             │
│  Google (Gemini 1.5, Gemini 2.0)                            │
│  ├── Мультимодальность                                      │
│  ├── 1M+ контекст                                           │
│  └── Интеграция с Google Cloud                              │
│                                                             │
│  xAI (Grok)                                                 │
│  ├── Интеграция с X (Twitter)                               │
│  └── Realtime данные                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Open-Source модели

```

┌─────────────────────────────────────────────────────────────┐
│                   Open-Source LLMs                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Meta (Llama 3, Llama 3.1, Llama 3.2, Llama 4)              │
│  ├── Самые популярные open-source                           │
│  ├── Разные размеры: 8B, 70B, 405B                          │
│  └── Можно дообучать и хостить самим                        │
│                                                             │
│  Mistral (Mistral, Mixtral)                                 │
│  ├── Эффективные модели                                     │
│  ├── Mixture of Experts (MoE)                               │
│  └── Хороший баланс качество/скорость                       │
│                                                             │
│  Qwen (Alibaba)                                             │
│  ├── Сильные модели из Китая                                │
│  └── Хорошо работают с азиатскими языками                   │
│                                                             │
│  DeepSeek                                                   │
│  ├── Дешёвые в инференсе                                    │
│  └── DeepSeek R1 с цепочками рассуждений                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Сравнение характеристик

### 2.1 Основные параметры

```python

model_comparison = {
    "GPT-4o": {
        "context": "128K tokens",
        "multimodal": True,
        "price_input": "$2.50/1M tokens",
        "price_output": "$10/1M tokens",
        "strength": "Универсальность"
    },
    "Claude 3.5 Sonnet": {
        "context": "200K tokens",
        "multimodal": True,
        "price_input": "$3/1M tokens",
        "price_output": "$15/1M tokens",
        "strength": "Код, длинный контекст"
    },
    "Gemini 1.5 Pro": {
        "context": "2M tokens",
        "multimodal": True,
        "price_input": "$1.25/1M tokens",
        "price_output": "$5/1M tokens",
        "strength": "Огромный контекст"
    },
    "Llama 3.1 405B": {
        "context": "128K tokens",
        "multimodal": False,
        "price": "Бесплатно (self-host)",
        "strength": "Open-source, контроль"
    }
}
```

### 2.2 Когда какую модель использовать

```python

use_cases = {
    "Простые задачи": "GPT-4o-mini, Claude 3 Haiku, Llama 8B",
    "Сложный reasoning": "o1, o3, Claude 3.5 Sonnet",
    "Длинные документы": "Gemini 1.5, Claude 3",
    "Код": "Claude 3.5 Sonnet, GPT-4o, Codestral",
    "Чувствительные данные": "Llama (self-hosted)",
    "Бюджетные решения": "DeepSeek, Llama, Mixtral"
}
```

---

## 3. Open-Source vs Proprietary

### 3.1 Сравнение

```

┌─────────────────────────────────────────────────────────────┐
│              Open-Source vs Proprietary                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Критерий        │ Open-Source      │ Proprietary           │
│  ─────────────────────────────────────────────────────────  │
│  Стоимость       │ Бесплатно*       │ Pay-per-token         │
│  Контроль        │ Полный           │ Через API             │
│  Приватность     │ Данные у вас     │ Данные к вендору      │
│  Качество        │ Хорошее          │ Лучшее                │
│  Поддержка       │ Community        │ Enterprise            │
│  Fine-tuning     │ Полный           │ Ограниченный          │
│  Инфраструктура  │ Нужна своя       │ Не нужна              │
│                                                             │
│  * Нужны GPU для хостинга                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Когда выбирать Open-Source

```python

choose_opensource_when = [
    "Строгие требования к приватности данных",
    "Нужен полный контроль над моделью",
    "Требуется fine-tuning под задачу",
    "Высокие объёмы запросов (экономия)",
    "Регуляторные ограничения (данные не покидают периметр)"
]
```

---

## 4. Хостинг моделей

### 4.1 Варианты

```python

hosting_options = {
    "API провайдеров": {
        "examples": ["OpenAI API", "Anthropic API", "Google AI"],
        "pros": "Просто, не нужна инфра",
        "cons": "Зависимость, стоимость"
    },
    "Managed inference": {
        "examples": ["AWS Bedrock", "Azure OpenAI", "Together.ai", "Fireworks"],
        "pros": "Выбор моделей, масштабирование",
        "cons": "Стоимость"
    },
    "Self-hosted": {
        "examples": ["vLLM", "Ollama", "llama.cpp", "TGI"],
        "pros": "Контроль, приватность",
        "cons": "Нужны GPU, эксплуатация"
    }
}
```

### 4.2 Пример развёртывания с Ollama

```bash
# Установка Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Загрузка модели
ollama pull llama3.1:8b

# Запуск
ollama run llama3.1:8b

# API доступен на localhost:11434
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.1:8b",
  "prompt": "Hello, how are you?"
}'
```

---

## 5. Стоимость и экономика

### 5.1 Модели ценообразования

```python

pricing_models = {
    "Pay-per-token": {
        "description": "Платите за использованные токены",
        "when": "Непредсказуемая нагрузка",
        "providers": ["OpenAI", "Anthropic"]
    },
    "Provisioned throughput": {
        "description": "Резервируете capacity",
        "when": "Стабильная высокая нагрузка",
        "providers": ["AWS Bedrock", "Azure"]
    },
    "Self-hosted": {
        "description": "Платите за GPU инфраструктуру",
        "when": "Очень высокие объёмы",
        "calculation": "GPU cost + ops"
    }
}
```

### 5.2 Пример расчёта

```python
# Сравнение стоимости для 1M запросов в месяц
# Средний запрос: 500 input + 500 output tokens

monthly_requests = 1_000_000
input_tokens = 500 * monthly_requests   # 500M
output_tokens = 500 * monthly_requests  # 500M

# GPT-4o
gpt4o_cost = (input_tokens / 1_000_000 * 2.50) + \
             (output_tokens / 1_000_000 * 10)  # $6,250/month

# Claude 3 Haiku
haiku_cost = (input_tokens / 1_000_000 * 0.25) + \
             (output_tokens / 1_000_000 * 1.25)  # $750/month

# Self-hosted Llama 70B (примерно)
# 2x A100 80GB = ~$30,000/month на облаке
# Но обрабатывает миллионы запросов
llama_cost = 30_000  # $30,000/month (фиксированно)
```

---

## 💡 Key Takeaways

- **Рынок разделён** — проприетарные (OpenAI, Anthropic, Google) и open-source (Meta, Mistral, DeepSeek)

- **Выбор зависит от задачи** — простые задачи → дешёвые модели, сложный reasoning → premium модели

- **Open-source для контроля** — когда важна приватность, fine-tuning, или экономия на объёмах

- **Hosted vs Self-hosted** — API проще, self-hosted дешевле при масштабе

- **Цены падают** — рынок становится конкурентнее, модели дешевеют

---

## 🚀 Next Steps

**Related Modules:**

- [13_AGI](../13_AGI/) — AGI: мифы и реальность

---


