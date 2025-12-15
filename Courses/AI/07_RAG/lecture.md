# RAG и работа с внешними данными
## Retrieval-Augmented Generation

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [03_LLM_Basics](../03_LLM_Basics/) — понимать ограничения LLM
- Понимать концепцию embeddings
- Иметь базовое представление о векторных базах данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить, почему LLM нужны внешние данные
- Описать архитектуру RAG системы
- Понимать работу векторных баз данных
- Оценивать, когда RAG нужен, а когда нет
- Проектировать RAG pipeline для своих задач

---

## 1. Почему LLM нужны внешние данные

### 1.1 Ограничения LLM

```

┌─────────────────────────────────────────────────────────────┐
│              Проблемы "чистого" LLM                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Знания заморожены                                       │
│     Модель знает только то, что было до training cutoff     │
│     GPT-4: данные до апреля 2023                            │
│                                                              │
│  2. Галлюцинации                                            │
│     Модель может уверенно генерировать неправду             │
│                                                              │
│  3. Нет доступа к вашим данным                              │
│     Модель не знает вашу документацию, код, базу знаний     │
│                                                              │
│  4. Конфиденциальность                                      │
│     Нельзя включить секретные данные в training             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Решение: RAG

RAG (Retrieval-Augmented Generation) — подход, где LLM дополняется релевантной информацией из внешних источников:

```

┌─────────────────────────────────────────────────────────────┐
│                     RAG Pipeline                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. User Query                                              │
│     "Какова политика возврата товаров?"                     │
│                          │                                   │
│                          ▼                                   │
│  2. Retrieval (поиск)                                       │
│     ┌─────────────────────────────────────┐                 │
│     │  Vector Database                    │                 │
│     │  ┌───┐ ┌───┐ ┌───┐ ┌───┐           │                 │
│     │  │ ▪ │ │ ▪ │ │ ▪ │ │ ▪ │  ...      │                 │
│     │  └───┘ └───┘ └───┘ └───┘           │                 │
│     └─────────────────────────────────────┘                 │
│     → Находим релевантные документы                         │
│                          │                                   │
│                          ▼                                   │
│  3. Augmentation (обогащение)                               │
│     Prompt = Query + Retrieved Documents                    │
│                          │                                   │
│                          ▼                                   │
│  4. Generation                                              │
│     LLM генерирует ответ на основе контекста                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Архитектура RAG

### 2.1 Компоненты системы

```python
# Основные компоненты RAG системы

rag_components = {
    "Document Store": "Хранение исходных документов",
    "Embedding Model": "Преобразование текста в векторы",
    "Vector Database": "Хранение и поиск векторов",
    "Retriever": "Поиск релевантных документов",
    "LLM": "Генерация ответа на основе контекста",
    "Orchestrator": "Координация всех компонентов"
}
```

### 2.2 Indexing Pipeline

```python
# Этап 1: Индексирование документов

def indexing_pipeline(documents):
    chunks = []
    
    # 1. Загрузка документов
    for doc in documents:
        text = load_document(doc)
        
        # 2. Разбиение на чанки
        doc_chunks = split_into_chunks(
            text,
            chunk_size=512,  # токенов
            overlap=50       # перекрытие
        )
        chunks.extend(doc_chunks)
    
    # 3. Создание embeddings
    embeddings = embedding_model.encode(chunks)
    
    # 4. Сохранение в vector DB
    vector_db.insert(
        texts=chunks,
        embeddings=embeddings
    )
    
    return len(chunks)
```

### 2.3 Query Pipeline

```python
# Этап 2: Обработка запроса

def query_pipeline(user_query, k=5):
    # 1. Создаём embedding запроса
    query_embedding = embedding_model.encode(user_query)
    
    # 2. Поиск похожих документов
    results = vector_db.search(
        query_embedding,
        top_k=k
    )
    
    # 3. Формируем промпт с контекстом
    context = "\n\n".join([r.text for r in results])
    
    prompt = f"""
    Answer the question based on the following context.
    If the answer is not in the context, say "I don't know".
    
    Context:
    {context}
    
    Question: {user_query}
    
    Answer:
    """
    
    # 4. Генерируем ответ
    response = llm.generate(prompt)
    
    return response, results  # Возвращаем и источники
```

---

## 3. Embeddings и векторные базы данных

### 3.1 Что такое Embeddings

Embedding — это векторное представление текста в многомерном пространстве:

```python
# Концептуально: похожие тексты → близкие векторы

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [
    "Как вернуть товар?",
    "Политика возврата покупок",
    "Прогноз погоды на завтра"
]

embeddings = model.encode(texts)

# embeddings[0] близок к embeddings[1] (похожая тема)
# embeddings[0] далёк от embeddings[2] (разные темы)

# Similarity измеряется косинусным расстоянием
from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity([embeddings[0]], [embeddings[1]]))  # ~0.8
print(cosine_similarity([embeddings[0]], [embeddings[2]]))  # ~0.1
```

### 3.2 Популярные Embedding модели

| Модель | Размерность | Особенности |
|--------|-------------|-------------|
| OpenAI text-embedding-3-small | 1536 | Хорошее качество, платная |
| OpenAI text-embedding-3-large | 3072 | Лучшее качество OpenAI |
| all-MiniLM-L6-v2 | 384 | Бесплатная, быстрая |
| BGE-large | 1024 | Отличное качество, open-source |
| Cohere embed-v3 | 1024 | Мультиязычная |

### 3.3 Векторные базы данных

```python
# Популярные векторные БД

vector_databases = {
    "Pinecone": {
        "type": "Cloud-native",
        "pros": ["Простой старт", "Масштабируемость"],
        "cons": ["Стоимость", "Vendor lock-in"]
    },
    "Weaviate": {
        "type": "Open-source / Cloud",
        "pros": ["Гибкость", "GraphQL API"],
        "cons": ["Сложнее настройка"]
    },
    "Chroma": {
        "type": "Open-source",
        "pros": ["Простота", "Для прототипов"],
        "cons": ["Не для production"]
    },
    "Qdrant": {
        "type": "Open-source / Cloud",
        "pros": ["Производительность", "Фильтры"],
        "cons": ["Меньше документации"]
    },
    "pgvector": {
        "type": "PostgreSQL extension",
        "pros": ["Знакомый PostgreSQL", "Транзакции"],
        "cons": ["Масштабирование"]
    }
}
```

### 3.4 Пример с Chroma

```python

import chromadb
from chromadb.utils import embedding_functions

# Создаём клиент
client = chromadb.Client()

# Используем OpenAI embeddings
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-3-small"
)

# Создаём коллекцию
collection = client.create_collection(
    name="my_docs",
    embedding_function=openai_ef
)

# Добавляем документы
collection.add(
    documents=[
        "Возврат товара возможен в течение 14 дней",
        "Доставка занимает 2-3 рабочих дня",
        "Мы работаем с 9 до 18"
    ],
    ids=["doc1", "doc2", "doc3"]
)

# Поиск
results = collection.query(
    query_texts=["как вернуть покупку"],
    n_results=2
)
print(results['documents'])
# [['Возврат товара возможен в течение 14 дней', ...]]
```

---

## 4. Chunking стратегии

### 4.1 Зачем нужен chunking

Документы разбиваются на части (chunks) потому что:

- Контекстное окно LLM ограничено
- Мелкие chunks дают более точный поиск
- Крупные chunks дают больше контекста

### 4.2 Стратегии chunking

```python
# 1. Fixed-size chunking
def fixed_size_chunks(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# 2. Sentence-based chunking
import nltk
def sentence_chunks(text, sentences_per_chunk=5):
    sentences = nltk.sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = ' '.join(sentences[i:i+sentences_per_chunk])
        chunks.append(chunk)
    return chunks

# 3. Semantic chunking (по смыслу)
# Разбиваем там, где меняется тема

# 4. Document-structure chunking
# Используем структуру документа (заголовки, параграфы)

```

### 4.3 Рекомендации по chunking

```python

chunking_guidelines = {
    "chunk_size": "256-1024 токенов (зависит от задачи)",
    "overlap": "10-20% от chunk_size",
    "metadata": "Сохраняйте источник, страницу, заголовок",
    "experiment": "Тестируйте разные размеры на своих данных"
}
```

---

## 5. Когда RAG нужен, а когда нет

### 5.1 RAG нужен

```python

use_rag_when = [
    "Нужны актуальные данные (после training cutoff)",
    "Работа с внутренними документами компании",
    "Требуется цитирование источников",
    "Доменная экспертиза (медицина, право)",
    "Снижение галлюцинаций критично",
    "Данные часто обновляются"
]
```

### 5.2 RAG не нужен

```python

skip_rag_when = [
    "Общие знания, покрытые training data",
    "Креативные задачи (генерация, рерайт)",
    "Простые преобразования (перевод, суммаризация)",
    "Данные умещаются в контекст",
    "Прототип / быстрый тест"
]
```

### 5.3 Альтернативы RAG

```python

alternatives = {
    "Fine-tuning": "Для специфичного стиля или формата",
    "Long context": "Если данные умещаются в 128K+ токенов",
    "Prompt engineering": "Для небольших справочников в промпте"
}
```

---

## 6. Улучшение RAG

### 6.1 Проблемы базового RAG

```python

basic_rag_problems = {
    "Низкое качество retrieval": "Находим не те документы",
    "Lost in the middle": "LLM игнорирует середину контекста",
    "Chunk границы": "Информация разрезана между chunks",
    "Нет reranking": "Первые результаты не лучшие"
}
```

### 6.2 Продвинутые техники

```python
# 1. Reranking — переранжирование результатов
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank_results(query, documents, top_k=3):
    pairs = [[query, doc] for doc in documents]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(documents, scores), key=lambda x: -x[1])
    return [doc for doc, score in ranked[:top_k]]

# 2. Hybrid search — комбинация semantic + keyword
def hybrid_search(query, alpha=0.5):
    semantic_results = vector_search(query)
    keyword_results = bm25_search(query)
    
    # Комбинируем с весами
    combined = merge_with_weights(
        semantic_results, 
        keyword_results,
        alpha=alpha
    )
    return combined

# 3. Query expansion — расширение запроса
def expand_query(query):
    prompt = f"""
    Generate 3 alternative phrasings of this question:
    {query}
    """
    alternatives = llm.generate(prompt)
    return [query] + alternatives
```

### 6.3 Evaluation RAG

```python
# Метрики для оценки RAG

rag_metrics = {
    "Retrieval": {
        "Precision@K": "Доля релевантных среди top-K",
        "Recall@K": "Доля найденных релевантных",
        "MRR": "Mean Reciprocal Rank"
    },
    "Generation": {
        "Faithfulness": "Ответ основан на контексте?",
        "Relevance": "Ответ релевантен вопросу?",
        "Correctness": "Ответ фактически верен?"
    }
}
```

---

## 💡 Key Takeaways

- **RAG решает ключевые проблемы LLM** — устаревшие знания, галлюцинации, отсутствие доступа к вашим данным

- **Архитектура: Index + Retrieve + Generate** — сначала индексируем документы, потом ищем релевантные, потом генерируем ответ

- **Embeddings — ключевой компонент** — качество поиска зависит от качества embeddings. Выбирайте модель под задачу

- **Chunking требует экспериментов** — размер chunks влияет на качество. Тестируйте на своих данных

- **RAG не серебряная пуля** — не нужен для общих знаний или креативных задач. Fine-tuning и long context — альтернативы

---

## 🚀 Next Steps

**Related Modules:**

- [08_Tools](../08_Tools/) — Tool usage и function calling
- [10_Agents_Basics](../10_Agents_Basics/) — AI-агенты с RAG

**Practice Ideas:**

1. Создайте RAG систему для своей документации
2. Сравните разные embedding модели на своих данных
3. Поэкспериментируйте с размерами chunks

---

## 📚 Additional Resources

**Libraries:**

- [LangChain](https://www.langchain.com/) — фреймворк для RAG
- [LlamaIndex](https://www.llamaindex.ai/) — специализирован на RAG
- [Haystack](https://haystack.deepset.ai/) — open-source RAG

**Vector Databases:**

- [Pinecone](https://www.pinecone.io/)
- [Weaviate](https://weaviate.io/)
- [Chroma](https://www.trychroma.com/)

---


