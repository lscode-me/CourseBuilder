# Обучение моделей
## Pretraining, Fine-tuning, RLHF и Alignment

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [03_LLM_Basics](../03_LLM_Basics/) — как работают LLM
- Понимать концепцию токенизации и генерации
- Иметь базовое представление о нейронных сетях

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить три этапа обучения LLM: pretraining, SFT, RLHF
- Описать процесс предобучения и его требования
- Понимать разницу между fine-tuning подходами
- Объяснить роль RLHF в alignment моделей
- Оценивать, когда нужен fine-tuning, а когда достаточно prompting

---

## 1. Обзор процесса обучения LLM

### 1.1 Три этапа обучения

Современные LLM проходят через несколько этапов обучения:

```

┌─────────────────────────────────────────────────────────────┐
│              Этапы обучения LLM                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Этап 1: Pretraining (предобучение)                         │
│  ─────────────────────────────────                          │
│  Что: Обучение на огромном корпусе текста                   │
│  Цель: "Выучить" язык и знания о мире                       │
│  Ресурсы: Терабайты данных, тысячи GPU, месяцы              │
│  Результат: Base model (GPT-4 base, LLaMA base)             │
│                                                              │
│  Этап 2: Supervised Fine-tuning (SFT)                       │
│  ─────────────────────────────────────                      │
│  Что: Дообучение на примерах "вопрос-ответ"                 │
│  Цель: Научить модель следовать инструкциям                 │
│  Ресурсы: Тысячи примеров, десятки GPU, дни                 │
│  Результат: Instruction-tuned model                         │
│                                                              │
│  Этап 3: RLHF (Reinforcement Learning from Human Feedback)  │
│  ─────────────────────────────────────────────────────      │
│  Что: Оптимизация на основе человеческих предпочтений       │
│  Цель: Alignment — модель полезная, безопасная, честная     │
│  Ресурсы: Оценки людей, сотни GPU, недели                   │
│  Результат: Aligned model (ChatGPT, Claude)                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Почему три этапа?

```python
# Каждый этап решает свою задачу

training_stages = {
    "Pretraining": {
        "problem": "Модель не знает язык",
        "solution": "Обучить на огромном количестве текста",
        "output": "Модель, которая хорошо предсказывает текст"
    },
    "SFT": {
        "problem": "Модель продолжает текст, а не отвечает на вопросы",
        "solution": "Показать примеры диалогов и инструкций",
        "output": "Модель, которая следует инструкциям"
    },
    "RLHF": {
        "problem": "Модель может быть вредной или бесполезной",
        "solution": "Оптимизировать на предпочтения людей",
        "output": "Модель, которая полезна и безопасна"
    }
}
```

---

## 2. Pretraining (Предобучение)

### 2.1 Цель предобучения

Цель pretraining — научить модель предсказывать следующий токен:

```python
# Задача предобучения: Language Modeling

# Input: "The quick brown fox jumps over the"
# Target: "lazy"

# Модель учится предсказывать следующее слово
# на ОГРОМНОМ количестве текста

# Loss function: Cross-entropy
loss = -log(P(next_token | previous_tokens))

# Минимизируя loss на триллионах токенов,
# модель "выучивает" паттерны языка
```

### 2.2 Данные для предобучения

```

┌─────────────────────────────────────────────────────────────┐
│            Источники данных для pretraining                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Common Crawl                                               │
│  └── Огромный архив веб-страниц                             │
│      ~250 миллиардов страниц                                │
│      Требует тщательной фильтрации!                         │
│                                                              │
│  Wikipedia                                                  │
│  └── Высококачественный, структурированный контент          │
│      ~60 миллионов статей на разных языках                  │
│                                                              │
│  Books                                                      │
│  └── Художественная и научная литература                    │
│      Books1, Books2, Books3 datasets                        │
│                                                              │
│  Academic Papers                                            │
│  └── arXiv, PubMed, Semantic Scholar                        │
│                                                              │
│  Code                                                       │
│  └── GitHub, Stack Overflow                                 │
│      Миллиарды строк кода                                   │
│                                                              │
│  Curated Sources                                            │
│  └── News articles, forums, Q&A sites                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Масштаб предобучения

```python
# Примерные затраты на pretraining

pretraining_costs = {
    "GPT-3 (175B)": {
        "tokens": "300 billion",
        "compute": "~3,640 petaflop-days",
        "cost": "~$4.6 million (estimate)",
        "time": "~1 month on 1000+ GPUs"
    },
    "LLaMA 2 (70B)": {
        "tokens": "2 trillion",
        "compute": "~1,720,320 GPU-hours",
        "cost": "~$2 million (estimate)",
        "time": "~3 months"
    },
    "GPT-4": {
        "tokens": "~13 trillion (estimate)",
        "compute": "Unknown (much larger)",
        "cost": "$100+ million (estimate)",
        "time": "Several months"
    }
}

# Только крупные компании могут делать pretraining с нуля
```

### 2.4 Качество данных важнее количества

```python
# Фильтрация данных — критически важна

data_quality_steps = {
    "Deduplication": "Удаление дублей (30-40% веба — дубли)",
    "Language filtering": "Фильтрация по языку",
    "Quality filtering": "Удаление низкокачественного контента",
    "Toxicity filtering": "Удаление вредного контента",
    "PII removal": "Удаление персональных данных",
    "Benchmark contamination": "Проверка на утечку тестов"
}

# "Data quality > Data quantity"
# Лучше 1T качественных токенов, чем 10T мусора
```

---

## 3. Supervised Fine-tuning (SFT)

### 3.1 Зачем нужен SFT

После pretraining модель умеет продолжать текст, но не умеет "отвечать":

```python
# Base model (после pretraining только)
prompt = "What is the capital of France?"
# Base model может продолжить:
# "What is the capital of France? This is a common question..."
# или
# "What is the capital of France? (A) Paris (B) London..."

# Instruction-tuned model (после SFT)
# "The capital of France is Paris."

# SFT учит модель следовать формату "вопрос → ответ"
```

### 3.2 Данные для SFT

```

┌─────────────────────────────────────────────────────────────┐
│              Данные для Supervised Fine-tuning               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Формат данных:                                             │
│  {                                                          │
│      "instruction": "Summarize this text",                  │
│      "input": "Long article about AI...",                   │
│      "output": "Brief summary of the article"               │
│  }                                                          │
│                                                              │
│  Источники:                                                 │
│  • Human-written examples (дорого, качественно)             │
│  • Crowdsourcing (Scale AI, Surge AI)                       │
│  • Synthetic data (генерация другими LLM)                   │
│  • Open datasets (FLAN, Alpaca, ShareGPT)                   │
│                                                              │
│  Типичный размер: 10K - 100K примеров                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Процесс SFT

```python
# Концептуально: SFT = обычное обучение на примерах

def sft_training_step(model, example):
    # Формируем input
    prompt = f"Instruction: {example['instruction']}\n"
    prompt += f"Input: {example['input']}\n"
    prompt += f"Output: "
    
    # Target — правильный ответ
    target = example['output']
    
    # Модель учится генерировать target после prompt
    loss = model.compute_loss(prompt, target)
    
    # Обновляем веса
    loss.backward()
    optimizer.step()
    
    return loss

# SFT обычно занимает часы-дни (не месяцы как pretraining)
```

### 3.4 Различные подходы к fine-tuning

```

┌─────────────────────────────────────────────────────────────┐
│              Подходы к Fine-tuning                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Full Fine-tuning                                           │
│  └── Обновляем все параметры модели                         │
│      + Максимальная гибкость                                │
│      - Требует много GPU памяти                             │
│      - Риск catastrophic forgetting                         │
│                                                              │
│  LoRA (Low-Rank Adaptation)                                 │
│  └── Добавляем маленькие "адаптеры" к слоям                 │
│      + Очень эффективно по памяти                           │
│      + Можно хранить много адаптеров                        │
│      - Немного меньше гибкости                              │
│                                                              │
│  QLoRA (Quantized LoRA)                                     │
│  └── LoRA + квантизация базовой модели                      │
│      + Ещё меньше памяти (70B на одной GPU!)                │
│      - Небольшая потеря качества                            │
│                                                              │
│  Prefix Tuning / P-Tuning                                   │
│  └── Обучаем только "prefix" векторы                        │
│      + Очень эффективно                                     │
│      - Ограниченная выразительность                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.5 LoRA — детальнее

```python
# LoRA: Low-Rank Adaptation

# Идея: вместо обновления всей матрицы весов W,
# добавляем низкоранговое приближение

# Оригинальный слой: y = Wx
# С LoRA: y = Wx + BAx
# где B и A — маленькие матрицы (rank << dimension)

class LoRALayer:
    def __init__(self, original_layer, rank=8):
        self.W = original_layer.weight  # Заморожено!
        self.rank = rank
        
        # Обучаемые параметры (очень мало)
        self.A = nn.Parameter(torch.randn(rank, in_dim))
        self.B = nn.Parameter(torch.zeros(out_dim, rank))
    
    def forward(self, x):
        # Оригинальный output + LoRA adaptation
        return self.W @ x + self.B @ self.A @ x

# Для 70B модели:
# Full fine-tuning: ~140GB GPU memory
# LoRA (rank=8): ~20GB GPU memory (!)
```

---

## 4. RLHF (Reinforcement Learning from Human Feedback)

### 4.1 Проблема, которую решает RLHF

SFT делает модель полезной, но не гарантирует качество:

```python
# Проблемы после SFT

sft_problems = {
    "Sycophancy": "Модель соглашается с пользователем, даже если он неправ",
    "Verbosity": "Модель генерирует слишком длинные ответы",
    "Harmful content": "Модель может генерировать вредный контент",
    "Hallucinations": "Модель уверенно врёт",
    "Format issues": "Модель не следует желаемому формату"
}

# RLHF оптимизирует на то, что РЕАЛЬНО хотят пользователи
```

### 4.2 Три шага RLHF

```

┌─────────────────────────────────────────────────────────────┐
│                    Процесс RLHF                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Шаг 1: Собрать предпочтения                                │
│  ───────────────────────────                                │
│  • Показать людям пары ответов (A, B)                       │
│  • Люди выбирают лучший                                     │
│  • Формируется датасет предпочтений                         │
│                                                              │
│  Шаг 2: Обучить Reward Model                                │
│  ───────────────────────────                                │
│  • Reward model учится предсказывать предпочтения           │
│  • Input: prompt + response                                 │
│  • Output: score (чем выше — тем лучше ответ)               │
│                                                              │
│  Шаг 3: Оптимизировать LLM с помощью PPO                    │
│  ─────────────────────────────────────────                  │
│  • LLM генерирует ответы                                    │
│  • Reward model оценивает                                   │
│  • PPO обновляет LLM, чтобы максимизировать reward          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Сбор предпочтений

```python
# Пример сбора предпочтений

prompt = "How can I improve my sleep quality?"

response_a = """
To improve sleep quality:
1. Maintain consistent sleep schedule
2. Create a dark, quiet environment
3. Avoid screens before bed
"""

response_b = """
Well, there are many ways to improve sleep. You could try 
various things like maybe going to bed earlier or something 
like that. Some people find that helps. There's also this 
thing about not using your phone. And exercise might help too.
"""

# Человек выбирает: A лучше B
# Почему? Конкретнее, структурированнее, полезнее
```

### 4.4 Reward Model

```python
# Reward model: предсказывает "качество" ответа

class RewardModel(nn.Module):
    def __init__(self, base_model):
        self.base_model = base_model
        self.reward_head = nn.Linear(hidden_dim, 1)
    
    def forward(self, prompt, response):
        # Получаем эмбеддинг [prompt + response]
        hidden = self.base_model(prompt + response)
        
        # Скаляр — "качество" ответа
        reward = self.reward_head(hidden[:, -1, :])
        return reward

# Обучение: Bradley-Terry loss
def compute_loss(reward_chosen, reward_rejected):
    return -log(sigmoid(reward_chosen - reward_rejected))

# Модель учится давать chosen > rejected
```

### 4.5 PPO оптимизация

```python
# PPO: Proximal Policy Optimization

# Концептуально:
# 1. LLM (policy) генерирует ответы
# 2. Reward model оценивает ответы
# 3. PPO обновляет LLM, чтобы максимизировать reward
# 4. KL penalty предотвращает слишком большие изменения

def ppo_step(policy, reward_model, prompt, reference_policy):
    # Генерируем ответ
    response = policy.generate(prompt)
    
    # Получаем reward
    reward = reward_model(prompt, response)
    
    # KL penalty — не уходим далеко от reference
    kl_penalty = kl_divergence(policy, reference_policy)
    
    # Итоговый reward
    total_reward = reward - beta * kl_penalty
    
    # Обновляем policy
    policy.update(total_reward)

# beta контролирует баланс между reward и стабильностью
```

### 4.6 Альтернативы RLHF

```python
# DPO (Direct Preference Optimization) — альтернатива RLHF

# Идея: обойтись без Reward Model и PPO
# Напрямую оптимизировать на предпочтениях

# RLHF:
# 1. Собрать предпочтения
# 2. Обучить Reward Model
# 3. PPO с Reward Model

# DPO:
# 1. Собрать предпочтения
# 2. Напрямую fine-tune LLM на предпочтениях

# Преимущества DPO:
# - Проще реализовать
# - Стабильнее обучение
# - Меньше гиперпараметров

# На практике DPO показывает сравнимые результаты с RLHF
```

---

## 5. Alignment

### 5.1 Что такое Alignment

Alignment — это процесс приведения поведения модели в соответствие с человеческими ценностями:

```

┌─────────────────────────────────────────────────────────────┐
│                    AI Alignment                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  HHH Framework (Anthropic):                                 │
│                                                              │
│  Helpful (Полезная)                                         │
│  └── Модель помогает пользователю достичь цели              │
│                                                              │
│  Harmless (Безвредная)                                      │
│  └── Модель не причиняет вред                               │
│      (не генерирует опасный контент)                        │
│                                                              │
│  Honest (Честная)                                           │
│  └── Модель не обманывает                                   │
│      (признаёт неуверенность, не галлюцинирует)             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Проблемы Alignment

```python
# Alignment — сложная проблема с компромиссами

alignment_challenges = {
    "Helpfulness vs Harmlessness": """
        Модель должна быть полезной, но не вредной.
        Но отказ помогать — тоже вред (бесполезность).
        Где грань?
    """,
    
    "Specification": """
        Как точно определить "вред"?
        Разные культуры, контексты, использования.
    """,
    
    "Robustness": """
        Jailbreaks: способы обойти ограничения.
        "Ignore previous instructions..."
    """,
    
    "Generalization": """
        Alignment на тренировке не гарантирует alignment
        на новых, невиданных сценариях.
    """
}
```

### 5.3 Constitutional AI (Anthropic)

```python
# Constitutional AI — альтернативный подход к alignment

# Идея: модель сама критикует и исправляет свои ответы
# на основе набора принципов (constitution)

constitution_example = [
    "Choose the response that is less harmful",
    "Choose the response that is more honest",
    "Choose the response that respects privacy",
    "Choose the response that doesn't encourage illegal activity"
]

# Процесс:
# 1. Модель генерирует ответ
# 2. Модель критикует ответ по принципам
# 3. Модель исправляет ответ
# 4. Используем пары (original, revised) для обучения

# Преимущество: меньше зависимости от человеческой разметки
```

---

## 6. Fine-tuning на практике

### 6.1 Когда нужен fine-tuning

```python
# Решающее дерево: Fine-tuning vs Prompting

decision_tree = {
    "Prompting достаточно если": [
        "Задача хорошо описывается инструкциями",
        "Несколько примеров решают задачу",
        "Нет специфичного домена/стиля",
        "Бюджет на fine-tuning ограничен"
    ],
    
    "Fine-tuning нужен если": [
        "Специфичный стиль/формат ответов",
        "Доменная экспертиза (медицина, юриспруденция)",
        "Большой объём специфичных данных",
        "Высокие требования к latency (меньше prompt)",
        "Частое использование (экономия на токенах)"
    ]
}
```

### 6.2 Пример: fine-tuning с OpenAI

```python
# Fine-tuning через OpenAI API

from openai import OpenAI
client = OpenAI()

# 1. Подготовка данных (JSONL формат)
training_data = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Classify this ticket: ..."},
            {"role": "assistant", "content": "Category: Billing"}
        ]
    },
    # ... больше примеров
]

# 2. Загрузка файла
with open("training.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

file = client.files.create(
    file=open("training.jsonl", "rb"),
    purpose="fine-tune"
)

# 3. Запуск fine-tuning
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18"
)

# 4. Использование fine-tuned модели
response = client.chat.completions.create(
    model=f"ft:gpt-4o-mini:my-org:custom-name:id",
    messages=[...]
)
```

### 6.3 Практические советы

```python
# Советы по fine-tuning

tips = {
    "Данные": [
        "Качество важнее количества",
        "Минимум 50-100 примеров для начала",
        "Разнообразие примеров критично",
        "Проверяйте данные вручную"
    ],
    
    "Процесс": [
        "Начните с prompting — это baseline",
        "Итеративно добавляйте примеры",
        "Тестируйте на held-out set",
        "Следите за overfitting"
    ],
    
    "Оценка": [
        "Определите метрики заранее",
        "Сравнивайте с baseline (prompting)",
        "Тестируйте на edge cases",
        "Получите обратную связь от пользователей"
    ]
}
```

---

## 7. Почему модели ведут себя по-разному

### 7.1 Различия между моделями

```python
# Почему GPT-4, Claude, Gemini отличаются?

model_differences = {
    "Training data": """
        Разные датасеты → разные знания и стили
    """,
    
    "Architecture": """
        Разные размеры, структуры, оптимизации
    """,
    
    "SFT data": """
        Разные примеры для instruction following
    """,
    
    "RLHF/alignment": """
        Разные приоритеты: helpful vs safe
        Anthropic более осторожный
        OpenAI более либеральный
    """,
    
    "System prompts": """
        Разные базовые инструкции (hidden)
    """
}
```

### 7.2 Trade-offs в обучении

```

┌─────────────────────────────────────────────────────────────┐
│              Trade-offs в обучении LLM                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Helpful ◄──────────────────────────────► Safe              │
│  (полезная)                                (безопасная)      │
│                                                              │
│  Больше отвечает ─────────── Больше отказывает              │
│                                                              │
│  Verbose ◄──────────────────────────────► Concise           │
│  (подробная)                               (краткая)         │
│                                                              │
│  Creative ◄─────────────────────────────► Factual           │
│  (креативная)                              (фактическая)     │
│                                                              │
│  Agreeable ◄────────────────────────────► Critical          │
│  (соглашается)                             (критикует)       │
│                                                              │
│  Каждая компания выбирает свою точку на этих осях           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 Key Takeaways

- **Три этапа обучения LLM** — Pretraining (язык + знания), SFT (следование инструкциям), RLHF (alignment). Каждый этап критически важен

- **Pretraining стоит миллионы** — Только крупные компании могут делать pretraining с нуля. Остальные используют готовые базовые модели

- **Fine-tuning стал доступным** — Благодаря LoRA/QLoRA можно дообучать 70B модели на одной GPU. Это демократизирует AI

- **RLHF делает модели полезными** — Без RLHF модели просто продолжают текст. RLHF учит их быть helpful, harmless, honest

- **Fine-tuning не всегда нужен** — Часто хватает промптинга. Fine-tuning оправдан для специфичных доменов и форматов

---

## 🚀 Next Steps

**Related Modules:**

- [05_Prompt_Basics](../05_Prompt_Basics/) — Prompt engineering
- [07_RAG](../07_RAG/) — RAG как альтернатива fine-tuning

**Practice Ideas:**

1. Попробуйте fine-tuning через OpenAI API на простой задаче
2. Сравните качество prompting vs fine-tuning на одной задаче
3. Изучите открытые датасеты для SFT (Alpaca, ShareGPT)

**Going Deeper:**

- Прочитайте статью "Training language models to follow instructions with human feedback" (InstructGPT)
- Изучите LoRA paper: "LoRA: Low-Rank Adaptation of Large Language Models"
- Посмотрите Constitutional AI paper от Anthropic

---

## 📚 Additional Resources

**Papers:**

- [InstructGPT](https://arxiv.org/abs/2203.02155) — RLHF для ChatGPT
- [LoRA](https://arxiv.org/abs/2106.09685) — эффективный fine-tuning
- [DPO](https://arxiv.org/abs/2305.18290) — альтернатива RLHF

**Tutorials:**

- [OpenAI Fine-tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)
- [Hugging Face PEFT](https://huggingface.co/docs/peft) — LoRA и другие методы

**Videos:**

- [Andrej Karpathy — State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) — обзор обучения GPT
- [RLHF explained](https://www.youtube.com/watch?v=2MBJi6mbMO4) — визуальное объяснение

---


