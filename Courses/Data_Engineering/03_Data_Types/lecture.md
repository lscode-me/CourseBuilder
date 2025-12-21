# Типы данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Data Engineering (модуль 01)
- Знать жизненный цикл данных (модуль 02)
- Иметь представление о базах данных и структурах данных

**Recommended prior modules:**

- [01_What_Is_Data_Engineering](../01_What_Is_Data_Engineering/) — основы Data Engineering
- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать structured, semi-structured и unstructured данные
- Понимать разницу между operational и analytical данными
- Объяснять различия между OLTP и OLAP системами
- Выбирать подходящий тип данных для конкретных задач

---

## 1. Введение в типы данных

В Data Engineering данные классифицируются по различным критериям: структуре, назначению, паттернам доступа. Понимание типов данных помогает выбрать правильные инструменты и архитектуру.

**Основные классификации:**

- По структуре: Structured, Semi-structured, Unstructured
- По назначению: Operational vs Analytical
- По паттернам доступа: OLTP vs OLAP

---

## 2. Structured Data (Структурированные данные)

Структурированные данные имеют чёткую, заранее определённую схему. Все записи следуют одной и той же структуре.

### 2.1 Характеристики

**Схема:**

- Строгая, внешняя схема
- Определена до записи данных
- Не может изменяться без миграции

**Структура:**

- Табличная форма (rows и columns)
- Фиксированные типы данных
- Связи между таблицами (foreign keys)

**Example: Structured Data**

```python
# Структурированные данные в виде таблицы
import pandas as pd

structured_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'email': ['alice@example.com', 'bob@example.com', 
              'charlie@example.com', 'diana@example.com', 'eve@example.com'],
    'age': [30, 25, 35, 28, 32],
    'created_at': ['2024-01-01', '2024-01-02', '2024-01-03', 
                   '2024-01-04', '2024-01-05']
})

print("Structured Data:")
print(structured_data)
print(f"\nSchema: {list(structured_data.columns)}")
print(f"Data types: {structured_data.dtypes.to_dict()}")
```

**Output:**
```

Structured Data:
   user_id    name              email  age  created_at
0        1   Alice   alice@example.com   30  2024-01-01
1        2     Bob     bob@example.com   25  2024-01-02
2        3 Charlie  charlie@example.com   35  2024-01-03
3        4   Diana   diana@example.com   28  2024-01-04
4        5     Eve     eve@example.com   32  2024-01-05

Schema: ['user_id', 'name', 'email', 'age', 'created_at']
Data types: {'user_id': dtype('int64'), 'name': dtype('O'), 'email': dtype('O'), 'age': dtype('int64'), 'created_at': dtype('O')}
```

### 2.2 Примеры structured данных

**Реляционные базы данных:**

- PostgreSQL, MySQL, Oracle
- Таблицы с фиксированными колонками
- Связи через foreign keys

**Файловые форматы:**

- CSV с заголовками
- Excel таблицы
- Parquet (columnar format)

**Example: SQL таблица**

```sql

-- Structured data в реляционной БД
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    age INT,
    created_at DATE
);

-- Все записи следуют одной схеме
INSERT INTO users VALUES 
    (1, 'Alice', 'alice@example.com', 30, '2024-01-01'),
    (2, 'Bob', 'bob@example.com', 25, '2024-01-02');
```

### 2.3 Преимущества structured данных

**Легко запрашивать:**

- SQL запросы
- Индексы для быстрого поиска
- Оптимизация запросов

**Легко валидировать:**

- Типы данных проверяются автоматически
- Constraints обеспечивают целостность
- Схема документирует структуру

**Эффективное хранение:**

- Компактное представление
- Оптимизация для чтения/записи
- Сжатие данных

---

## 3. Semi-structured Data (Полуструктурированные данные)

Полуструктурированные данные имеют гибкую схему, встроенную в сами данные. Разные записи могут иметь разные поля.

### 3.1 Характеристики

**Схема:**

- Гибкая, встроенная в данные
- Может изменяться без миграции
- Самоописывающиеся данные

**Структура:**

- Иерархическая (деревья, вложенные объекты)
- Могут отсутствовать некоторые поля
- Массивы и вложенные структуры

**Example: Semi-structured Data**

```python

import json

# Semi-structured данные в JSON
semi_structured_data = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "SQL"],
        "address": {
            "city": "Moscow",
            "zip": "101000"
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 25,
        "skills": ["Java", "JavaScript"],
        "address": {
            "city": "Saint Petersburg",
            "zip": "190000"
        },
        "phone": "+7-999-123-4567"  # Дополнительное поле
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 35,
        "skills": ["Python", "Go"],
        # address отсутствует
        "metadata": {
            "source": "api",
            "version": "1.0"
        }
    }
]

print("Semi-structured Data (JSON):")
print(json.dumps(semi_structured_data, indent=2, ensure_ascii=False))

# Разные записи имеют разные поля
print(f"\nПоля в записи 1: {set(semi_structured_data[0].keys())}")
print(f"Поля в записи 2: {set(semi_structured_data[1].keys())}")
print(f"Поля в записи 3: {set(semi_structured_data[2].keys())}")
```

**Output:**
```

Semi-structured Data (JSON):
[
  {
    "id": 1,
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"],
    "address": {
      "city": "Moscow",
      "zip": "101000"
    }
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 25,
    "skills": ["Java", "JavaScript"],
    "address": {
      "city": "Saint Petersburg",
      "zip": "190000"
    },
    "phone": "+7-999-123-4567"
  },
  {
    "id": 3,
    "name": "Charlie",
    "age": 35,
    "skills": ["Python", "Go"],
    "metadata": {
      "source": "api",
      "version": "1.0"
    }
  }
]

Поля в записи 1: {'id', 'name', 'age', 'skills', 'address'}
Поля в записи 2: {'id', 'name', 'age', 'skills', 'address', 'phone'}
Поля в записи 3: {'id', 'name', 'age', 'skills', 'metadata'}
```

### 3.2 Примеры semi-structured данных

**JSON:**

- REST API responses
- Configuration files
- Logs в структурированном формате

**XML:**

- Web services (SOAP)
- Document formats
- Configuration files

**YAML:**

- Configuration files
- CI/CD pipelines
- Infrastructure as Code

**Example: XML данные**

```xml

<!-- Semi-structured данные в XML -->
<users>
    <user id="1">
        <name>Alice</name>
        <age>30</age>
        <skills>
            <skill>Python</skill>
            <skill>SQL</skill>
        </skills>
        <address city="Moscow" zip="101000"/>
    </user>
    <user id="2">
        <name>Bob</name>
        <age>25</age>
        <skills>
            <skill>Java</skill>
            <skill>JavaScript</skill>
        </skills>
        <address city="Saint Petersburg" zip="190000"/>
        <phone>+7-999-123-4567</phone>
    </user>
</users>
```

### 3.3 Преимущества semi-structured данных

**Гибкость:**

- Легко добавлять новые поля
- Разные записи могут иметь разную структуру
- Адаптация к изменяющимся требованиям

**Самоописывающиеся:**

- Схема встроена в данные
- Не нужна внешняя документация схемы
- Легко понимать структуру

**Легко расширяемые:**

- Новые поля не требуют миграции
- Обратная совместимость
- Версионирование через поля

---

## 4. Unstructured Data (Неструктурированные данные)

Неструктурированные данные не имеют предопределённой модели или схемы. Это самый распространённый тип данных в мире.

### 4.1 Характеристики

**Схема:**

- Отсутствует
- Нет фиксированной структуры
- Требуется обработка для извлечения структуры

**Структура:**

- Свободная форма
- Может содержать любую информацию
- Требует специальных методов анализа

**Example: Unstructured Data**

```python
# Неструктурированные данные
unstructured_examples = {
    "text": """
    Привет! Это обычный текст без структуры.
    Здесь может быть любая информация: email, статья, комментарий.
    Нет фиксированных полей или формата.
    """,
    
    "log_entry": """
    2024-01-01 10:15:23 ERROR [UserService] Failed to authenticate user 
    john.doe@example.com. Reason: Invalid credentials. IP: 192.168.1.100
    """,
    
    "email": """
    From: alice@example.com
    To: bob@example.com
    Subject: Meeting tomorrow
    
    Hi Bob,
    
    Let's meet tomorrow at 3 PM to discuss the project.
    
    Best regards,
    Alice
    """,
    
    "image_path": "/data/images/product_photo_001.jpg",
    "audio_path": "/data/audio/customer_call_20240101.wav",
    "video_path": "/data/video/demo_2024.mp4"
}

print("Unstructured Data Examples:")
for data_type, content in unstructured_examples.items():
    print(f"\n{data_type.upper()}:")
    if isinstance(content, str) and len(content) < 200:
        print(content.strip())
    else:
        print(f"  Path/Length: {content if isinstance(content, str) and content.startswith('/') else len(content)} chars")
```

**Output:**
```

Unstructured Data Examples:

TEXT:
    Привет! Это обычный текст без структуры.
    Здесь может быть любая информация: email, статья, комментарий.
    Нет фиксированных полей или формата.

LOG_ENTRY:
    2024-01-01 10:15:23 ERROR [UserService] Failed to authenticate user 
    john.doe@example.com. Reason: Invalid credentials. IP: 192.168.1.100

EMAIL:
    From: alice@example.com
    To: bob@example.com
    Subject: Meeting tomorrow
    
    Hi Bob,
    
    Let's meet tomorrow at 3 PM to discuss the project.
    
    Best regards,
    Alice

IMAGE_PATH:
  Path/Length: /data/images/product_photo_001.jpg

AUDIO_PATH:
  Path/Length: /data/audio/customer_call_20240101.wav

VIDEO_PATH:
  Path/Length: /data/video/demo_2024.mp4
```

### 4.2 Примеры unstructured данных

**Текст:**

- Emails, статьи, комментарии
- Документы (PDF, Word)
- Сообщения в соцсетях

**Медиа:**

- Изображения (JPG, PNG)
- Аудио (MP3, WAV)
- Видео (MP4, AVI)

**Логи:**

- Application logs
- Server logs
- Error messages

### 4.3 Обработка unstructured данных

**Текст:**

- NLP (Natural Language Processing)
- Токенизация, извлечение сущностей
- Sentiment analysis

**Медиа:**

- Computer Vision для изображений
- Speech recognition для аудио
- Video processing

**Example: Обработка unstructured текста**

```python
# Симуляция обработки unstructured текста
def extract_structured_info(text):
    """Извлекает структурированную информацию из текста"""
    # В реальности используется NLP
    info = {
        "entities": [],
        "sentiment": "neutral",
        "keywords": []
    }
    
    # Простая симуляция извлечения
    if "@" in text:
        info["entities"].append("email")
    if "ERROR" in text or "Failed" in text:
        info["sentiment"] = "negative"
    if "meeting" in text.lower():
        info["keywords"].append("meeting")
    
    return info

# Обработка unstructured данных

unstructured_text = """
2024-01-01 10:15:23 ERROR [UserService] Failed to authenticate user 
john.doe@example.com. Reason: Invalid credentials. IP: 192.168.1.100
"""

structured_info = extract_structured_info(unstructured_text)
print("Извлечённая структурированная информация:")
print(structured_info)
```

**Output:**
```

Извлечённая структурированная информация:
{'entities': ['email'], 'sentiment': 'negative', 'keywords': []}
```

---

## 5. Сравнение типов данных

Понимание различий помогает выбрать правильный подход для хранения и обработки.

### 5.1 Таблица сравнения

| Характеристика | Structured | Semi-structured | Unstructured |
|----------------|------------|-----------------|--------------|
| **Схема** | Строгая, внешняя | Гибкая, встроенная | Отсутствует |
| **Запросы** | SQL, простые | JSONPath, XPath | Полнотекстовый поиск, NLP |
| **Примеры** | RDBMS, CSV | JSON, YAML, XML | Текст, медиа, логи |
| **Объём в мире** | ~20% | ~10% | ~70% |
| **Анализ** | Простой | Средний | Сложный |
| **Валидация** | Автоматическая | Частичная | Требует обработки |
| **Хранение** | Эффективное | Среднее | Большой объём |

### 5.2 Когда использовать каждый тип

**Structured:**

- Транзакционные данные
- Данные с фиксированной схемой
- Когда нужны сложные запросы и joins
- Высокие требования к целостности

**Semi-structured:**

- API responses
- Configuration files
- Данные с изменяющейся схемой
- Когда нужна гибкость

**Unstructured:**

- Медиа файлы
- Текстовые документы
- Логи
- Когда структура неизвестна заранее

---

## 6. Operational vs Analytical Data

Данные также классифицируются по назначению: operational (операционные) и analytical (аналитические).

### 6.1 Operational Data (Операционные данные)

Операционные данные используются для поддержки текущих бизнес-операций.

**Характеристики:**

- Real-time или near real-time
- Много коротких транзакций
- Требуют быстрых записей и чтений
- Критичны для бизнес-процессов

**Примеры:**

- Транзакции в e-commerce
- Пользовательские сессии
- Инвентарь в реальном времени
- Заказы и платежи

**Example: Operational Data**

```python
# Operational данные: транзакции в реальном времени
operational_transactions = [
    {
        "transaction_id": "tx_001",
        "user_id": 123,
        "product_id": 456,
        "amount": 99.99,
        "timestamp": "2024-01-01T10:00:00Z",
        "status": "completed"
    },
    {
        "transaction_id": "tx_002",
        "user_id": 124,
        "product_id": 789,
        "amount": 149.99,
        "timestamp": "2024-01-01T10:00:01Z",
        "status": "pending"
    }
]

print("Operational Data (Real-time transactions):")
for tx in operational_transactions:
    print(f"  {tx['transaction_id']}: User {tx['user_id']} - ${tx['amount']} - {tx['status']}")
```

**Output:**
```

Operational Data (Real-time transactions):
  tx_001: User 123 - $99.99 - completed
  tx_002: User 124 - $149.99 - pending
```

### 6.2 Analytical Data (Аналитические данные)

Аналитические данные используются для анализа, отчётов и принятия решений.

**Характеристики:**

- Batch обновления
- Много данных, сложные запросы
- Оптимизированы для чтения
- Агрегации и аналитика

**Примеры:**

- Исторические продажи
- Агрегированные метрики
- Отчёты и дашборды
- ML features

**Example: Analytical Data**

```python
# Analytical данные: агрегированные метрики
analytical_metrics = {
    "date": "2024-01-01",
    "total_revenue": 50000.00,
    "total_orders": 1250,
    "average_order_value": 40.00,
    "top_products": [
        {"product_id": 456, "sales": 500, "revenue": 25000},
        {"product_id": 789, "sales": 300, "revenue": 15000}
    ],
    "customer_segments": {
        "new": 400,
        "returning": 850
    }
}

print("Analytical Data (Aggregated metrics):")
print(f"  Date: {analytical_metrics['date']}")
print(f"  Total Revenue: ${analytical_metrics['total_revenue']:,.2f}")
print(f"  Total Orders: {analytical_metrics['total_orders']}")
print(f"  Average Order Value: ${analytical_metrics['average_order_value']:.2f}")
```

**Output:**
```

Analytical Data (Aggregated metrics):
  Date: 2024-01-01
  Total Revenue: $50,000.00
  Total Orders: 1250
  Average Order Value: $40.00
```

### 6.3 Различия

| Аспект | Operational | Analytical |
|--------|-------------|------------|
| **Назначение** | Поддержка операций | Анализ и отчёты |
| **Обновление** | Real-time | Batch |
| **Паттерн доступа** | Много коротких запросов | Меньше, но сложных запросов |
| **Оптимизация** | Запись и чтение | Чтение и агрегации |
| **Хранение** | Нормализованное | Денормализованное |
| **Примеры** | Транзакции, сессии | Метрики, отчёты |

---

## 7. OLTP vs OLAP

OLTP (Online Transaction Processing) и OLAP (Online Analytical Processing) — это два разных подхода к обработке данных.

### 7.1 OLTP (Online Transaction Processing)

OLTP системы оптимизированы для обработки транзакций в реальном времени.

**Характеристики:**

- Много коротких транзакций
- Быстрые записи и чтения отдельных записей
- Нормализованная структура
- Высокая доступность

**Примеры:**

- PostgreSQL, MySQL
- Банковские транзакции
- E-commerce заказы
- User authentication

**Example: OLTP запрос**

```python
# OLTP: быстрая запись и чтение отдельных записей
oltp_operations = [
    {
        "operation": "INSERT",
        "table": "orders",
        "data": {"order_id": 1001, "user_id": 123, "amount": 99.99},
        "time": "10ms"
    },
    {
        "operation": "SELECT",
        "table": "users",
        "query": "SELECT * FROM users WHERE user_id = 123",
        "time": "5ms"
    },
    {
        "operation": "UPDATE",
        "table": "inventory",
        "query": "UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456",
        "time": "8ms"
    }
]

print("OLTP Operations (Fast individual record operations):")
for op in oltp_operations:
    print(f"  {op['operation']} on {op['table']}: {op['time']}")
```

**Output:**
```

OLTP Operations (Fast individual record operations):
  INSERT on orders: 10ms
  SELECT on users: 5ms
  UPDATE on inventory: 8ms
```

### 7.2 OLAP (Online Analytical Processing)

OLAP системы оптимизированы для аналитических запросов и агрегаций.

**Характеристики:**

- Меньше, но сложных запросов
- Быстрые агрегации
- Денормализованная структура
- Columnar storage

**Примеры:**

- Snowflake, BigQuery, Redshift
- Data warehouses
- Business Intelligence
- Analytics dashboards

**Example: OLAP запрос**

```python
# OLAP: сложные аналитические запросы
olap_queries = [
    {
        "query": """
        SELECT 
            DATE_TRUNC('month', order_date) as month,
            product_category,
            SUM(revenue) as total_revenue,
            COUNT(DISTINCT user_id) as unique_customers,
            AVG(order_value) as avg_order_value
        FROM orders
        WHERE order_date >= '2024-01-01'
        GROUP BY month, product_category
        ORDER BY month, total_revenue DESC
        """,
        "rows_scanned": 1000000,
        "time": "2.5s"
    },
    {
        "query": """
        SELECT 
            customer_segment,
            SUM(lifetime_value) as total_ltv,
            AVG(orders_count) as avg_orders
        FROM customer_analytics
        GROUP BY customer_segment
        """,
        "rows_scanned": 500000,
        "time": "1.2s"
    }
]

print("OLAP Queries (Complex analytical queries):")
for i, q in enumerate(olap_queries, 1):
    print(f"\nQuery {i}:")
    print(f"  Rows scanned: {q['rows_scanned']:,}")
    print(f"  Execution time: {q['time']}")
```

**Output:**
```

OLAP Queries (Complex analytical queries):

Query 1:
  Rows scanned: 1,000,000
  Execution time: 2.5s

Query 2:
  Rows scanned: 500,000
  Execution time: 1.2s
```

### 7.3 Сравнение OLTP vs OLAP

| Аспект | OLTP | OLAP |
|--------|------|------|
| **Назначение** | Транзакции | Аналитика |
| **Паттерн доступа** | Много коротких запросов | Меньше сложных запросов |
| **Оптимизация** | Запись и чтение | Чтение и агрегации |
| **Структура** | Нормализованная | Денормализованная |
| **Storage** | Row-based | Columnar |
| **Примеры** | PostgreSQL, MySQL | Snowflake, BigQuery |

---

## 8. Выбор типа данных

Выбор типа данных зависит от требований к данным и использования.

### 8.1 Decision Matrix

**Используйте Structured, если:**

- Схема фиксирована и стабильна
- Нужны сложные запросы и joins
- Требуется высокая целостность данных
- Данные транзакционные

**Используйте Semi-structured, если:**

- Схема может изменяться
- Данные из API или внешних источников
- Нужна гибкость
- Разные записи могут иметь разные поля

**Используйте Unstructured, если:**

- Данные медиа (изображения, видео, аудио)
- Текстовые документы
- Логи без структуры
- Требуется NLP/ML обработка

**Example: Выбор типа данных**

```python

def recommend_data_type(requirements):
    """Рекомендует тип данных на основе требований"""
    if requirements.get("fixed_schema") and requirements.get("complex_queries"):
        return "Structured (RDBMS)"
    elif requirements.get("flexible_schema") or requirements.get("api_source"):
        return "Semi-structured (JSON/NoSQL)"
    elif requirements.get("media") or requirements.get("text_processing"):
        return "Unstructured (Files/Storage)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"fixed_schema": True, "complex_queries": True, "transactional": True},
    {"flexible_schema": True, "api_source": True},
    {"media": True, "text_processing": False},
    {"text_processing": True, "nlp_required": True}
]

print("Рекомендации типа данных:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_data_type(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации типа данных:
  Пример 1: Structured (RDBMS)
  Пример 2: Semi-structured (JSON/NoSQL)
  Пример 3: Unstructured (Files/Storage)
  Пример 4: Unstructured (Files/Storage)
```

---

## 💡 Key Takeaways

- **Три типа данных по структуре**: Structured (фиксированная схема), Semi-structured (гибкая схема), Unstructured (нет схемы). Каждый тип подходит для разных задач.

- **Operational vs Analytical**: Operational данные поддерживают текущие операции (real-time), analytical данные используются для анализа (batch). Разные требования к оптимизации.

- **OLTP vs OLAP**: OLTP оптимизированы для транзакций (много коротких запросов), OLAP для аналитики (сложные агрегации). Разные структуры и storage подходы.

- **Выбор типа данных**: Зависит от требований к схеме, паттернов доступа, типа запросов. Нет универсального решения, нужен осознанный выбор.

- **Гибридные подходы**: Современные системы часто используют комбинацию типов данных. Например, structured для транзакций, semi-structured для API, unstructured для медиа.

---

## 🚀 Next Steps

**Related Modules:**

- [04_Data_Modeling](../04_Data_Modeling/) — моделирование данных и нормализация
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [06_Data_Formats](../06_Data_Formats/) — форматы данных (CSV, JSON, Parquet)

**Practice Ideas:**

1. Создайте примеры structured, semi-structured и unstructured данных для вашего проекта
2. Проанализируйте вашу систему: какие данные operational, какие analytical?
3. Изучите разницу между OLTP и OLAP на практике: создайте простую транзакционную БД и аналитическое хранилище

**Going Deeper:**

- Изучите columnar storage (Parquet, ORC) для аналитики
- Погрузитесь в обработку unstructured данных: NLP, Computer Vision
- Изучите гибридные подходы: Data Lakehouse, который поддерживает все типы данных

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — главы о типах данных и storage
- "Fundamentals of Data Engineering" by Joe Reis & Matt Housley — типы данных в контексте Data Engineering

**Articles:**

- "Structured vs Unstructured Data" — сравнение подходов
- "OLTP vs OLAP: Understanding the Difference" — детальное сравнение

**Documentation:**

- PostgreSQL: https://www.postgresql.org/docs/
- MongoDB: https://docs.mongodb.com/
- Apache Parquet: https://parquet.apache.org/docs/

---


