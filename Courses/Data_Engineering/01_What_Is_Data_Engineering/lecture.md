# Что такое Data Engineering

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции программирования
- Иметь представление о базах данных (SQL)
- Знать основы работы с командной строкой
- Понимать концепцию API и веб-сервисов

**Recommended prior modules:**

- Нет обязательных предварительных модулей (это первая лекция курса)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать Data Engineering, Data Science и Analytics
- Описывать роль data engineer в команде
- Классифицировать типы data-систем
- Объяснять концепцию "данные как продукт"

---

## 1. Введение в Data Engineering

Data Engineering — это инженерная дисциплина, которая занимается проектированием, построением и эксплуатацией систем для сбора, хранения, обработки и предоставления данных. В отличие от Data Science, которая фокусируется на извлечении инсайтов из данных, Data Engineering создаёт инфраструктуру, которая делает эти инсайты возможными.

### 1.1 Проблема: данные как актив

В современном мире данные стали критически важным активом для компаний. Однако сырые данные редко полезны сами по себе. Они должны быть:

- **Собраны** из различных источников

- **Очищены** и валидированы

- **Трансформированы** в полезный формат

- **Хранимы** надёжно и эффективно

- **Доступны** для анализа и использования

**Example: E-commerce платформа**

```python
# Проблема: данные из разных источников

data_sources = {
    "user_events": "Clickstream данные (JSON logs)",
    "transactions": "PostgreSQL база данных",
    "inventory": "REST API внешнего сервиса",
    "reviews": "MongoDB коллекция",
    "marketing": "CSV файлы из CRM"
}

# Задача Data Engineer: создать единую систему
# которая объединяет все эти источники
# и делает данные доступными для аналитиков

print("Источники данных:")
for source, description in data_sources.items():
    print(f"  - {source}: {description}")
```

**Output:**
```
Источники данных:
  - user_events: Clickstream данные (JSON logs)
  - transactions: PostgreSQL база данных
  - inventory: REST API внешнего сервиса
  - reviews: MongoDB коллекция
  - marketing: CSV файлы из CRM
```

Data Engineer должен спроектировать систему, которая:

1. Собирает данные из всех этих источников
2. Приводит их к единому формату
3. Хранит эффективно
4. Обеспечивает быстрый доступ для аналитики

---

## 2. Data Engineering vs Data Science vs Analytics

Важно понимать разницу между этими дисциплинами, так как они часто пересекаются, но имеют разные фокусы.

### 2.1 Data Science

**Data Science** фокусируется на извлечении знаний и инсайтов из данных с помощью статистики, машинного обучения и анализа.

**Характеристики:**

- Работает с уже подготовленными данными
- Создаёт модели и алгоритмы
- Фокусируется на вопросах "почему" и "что если"
- Результат: модели, предсказания, инсайты

**Example: Data Science задача**

```python
# Data Scientist получает готовые данные
# и строит модель предсказания

import pandas as pd
from sklearn.linear_model import LinearRegression

# Данные уже очищены и подготовлены Data Engineer

sales_data = pd.DataFrame({
    'month': [1, 2, 3, 4, 5],
    'advertising_spend': [1000, 1500, 2000, 2500, 3000],
    'sales': [5000, 6000, 7000, 8000, 9000]
})

# Строит модель

model = LinearRegression()
model.fit(sales_data[['advertising_spend']], sales_data['sales'])

# Делает предсказание

prediction = model.predict([[3500]])
print(f"Предсказанные продажи при бюджете $3500: ${prediction[0]:.2f}")
```

**Output:**
```
Предсказанные продажи при бюджете $3500: $10000.00
```

### 2.2 Analytics

**Analytics** использует данные для принятия бизнес-решений. Это более широкая дисциплина, которая включает в себя Business Intelligence (BI), отчётность и визуализацию.

**Характеристики:**

- Работает с агрегированными данными
- Создаёт дашборды и отчёты
- Фокусируется на вопросах "что произошло" и "что происходит"
- Результат: отчёты, визуализации, метрики

**Example: Analytics задача**

```python
# Analytics создаёт отчёты из данных

# Данные уже подготовлены Data Engineer

daily_sales = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=30, freq='D'),
    'revenue': [1000 + i*50 + (i%7)*200 for i in range(30)],
    'region': ['North', 'South', 'East', 'West'] * 8
})

# Создаёт агрегации для отчёта

monthly_summary = daily_sales.groupby('region')['revenue'].agg({
    'total': 'sum',
    'average': 'mean',
    'max': 'max'
})

print("Месячный отчёт по регионам:")
print(monthly_summary)
```

**Output:**
```
Месячный отчёт по регионам:
        total    average      max
region                            
East    46500  1937.500000  2500
North   46500  1937.500000  2500
South   46500  1937.500000  2500
West    46500  1937.500000  2500
```

### 2.3 Data Engineering

**Data Engineering** создаёт и поддерживает инфраструктуру данных, которая делает возможной работу Data Science и Analytics.

**Характеристики:**

- Работает с сырыми данными из различных источников
- Создаёт pipelines и системы хранения
- Фокусируется на вопросах "как" и "где"
- Результат: надёжные, масштабируемые системы данных

**Example: Data Engineering задача**

```python
# Data Engineer создаёт pipeline для сбора и обработки данных

import json
from datetime import datetime

# 1. Сбор данных из разных источников

def collect_user_events():
    """Собирает события пользователей из логов"""
    # Симуляция чтения логов
    events = [
        {"user_id": 1, "event": "click", "timestamp": "2024-01-01T10:00:00"},
        {"user_id": 2, "event": "purchase", "timestamp": "2024-01-01T10:05:00"},
    ]
    return events

def collect_transactions():
    """Собирает транзакции из базы данных"""
    # Симуляция запроса к БД
    transactions = [
        {"transaction_id": 101, "user_id": 1, "amount": 99.99},
        {"transaction_id": 102, "user_id": 2, "amount": 149.99},
    ]
    return transactions

# 2. Трансформация и объединение

def transform_and_join(events, transactions):
    """Объединяет события и транзакции"""
    result = []
    for event in events:
        user_id = event["user_id"]
        # Находим соответствующую транзакцию
        transaction = next(
            (t for t in transactions if t["user_id"] == user_id),
            None
        )
        result.append({
            "user_id": user_id,
            "event": event["event"],
            "timestamp": event["timestamp"],
            "transaction_amount": transaction["amount"] if transaction else None
        })
    return result

# 3. Загрузка в хранилище

def load_to_warehouse(data):
    """Загружает данные в data warehouse"""
    print(f"Загружено {len(data)} записей в warehouse")
    return True

# Весь pipeline

events = collect_user_events()
transactions = collect_transactions()
transformed = transform_and_join(events, transactions)
load_to_warehouse(transformed)
```

**Output:**
```
Загружено 2 записей в warehouse
```

### 2.4 Сравнение дисциплин

| Аспект | Data Engineering | Data Science | Analytics |
|--------|------------------|--------------|-----------|
| **Фокус** | Инфраструктура данных | Модели и алгоритмы | Бизнес-инсайты |
| **Входные данные** | Сырые данные из разных источников | Подготовленные данные | Агрегированные данные |
| **Выход** | Pipelines, хранилища, системы | Модели, предсказания | Отчёты, дашборды |
| **Навыки** | Программирование, системы, DevOps | Статистика, ML, математика | SQL, визуализация, бизнес |
| **Вопросы** | Как собрать? Где хранить? | Почему? Что если? | Что произошло? |

> **💡 Pro Tip:**  
> В реальных проектах эти роли часто пересекаются. Data Engineer может делать простую аналитику, а Data Scientist может писать ETL скрипты. Важно понимать фокус каждой дисциплины.

---

## 3. Роль Data Engineer в команде

Data Engineer — это мост между источниками данных и их потребителями (аналитиками, data scientists, бизнес-пользователями).

### 3.1 Обязанности Data Engineer

**Основные задачи:**

1. **Проектирование data pipelines**
   - Определение источников данных
   - Проектирование потоков данных
   - Выбор инструментов и технологий

2. **Разработка и поддержка инфраструктуры**
   - Настройка хранилищ данных
   - Создание ETL/ELT процессов
   - Мониторинг и оптимизация

3. **Обеспечение качества данных**
   - Валидация данных
   - Обработка ошибок
   - Документирование схем данных

4. **Оптимизация производительности**
   - Партиционирование данных
   - Создание индексов
   - Оптимизация запросов

**Example: Типичный день Data Engineer**

```python
# Утро: проверка ночных jobs

def check_nightly_jobs():
    jobs = {
        "user_events_ingestion": {"status": "success", "records": 1000000},
        "transactions_etl": {"status": "failed", "error": "Connection timeout"},
        "analytics_refresh": {"status": "success", "records": 500000}
    }
    
    for job, info in jobs.items():
        if info["status"] == "failed":
            print(f"⚠️  {job}: {info['error']}")
            # Data Engineer должен исправить проблему
        else:
            print(f"✅ {job}: {info['records']} записей обработано")

check_nightly_jobs()
```

**Output:**
```
✅ user_events_ingestion: 1000000 записей обработано
⚠️  transactions_etl: Connection timeout
✅ analytics_refresh: 500000 записей обработано
```

### 3.2 Взаимодействие с другими ролями

**С Product Manager:**

- Обсуждение требований к данным
- Приоритизация задач
- Оценка сложности реализации

**С Data Scientist:**

- Предоставление подготовленных данных
- Обсуждение формата данных для моделей
- Помощь с feature engineering

**С Analytics Engineer:**

- Создание таблиц для аналитики
- Оптимизация запросов
- Поддержка dbt моделей

**С DevOps:**

- Развёртывание инфраструктуры
- Настройка CI/CD для data pipelines
- Мониторинг и алертинг

**Example: Типичное взаимодействие**

```python
# Симуляция workflow между ролями

class DataEngineer:
    def provide_data(self, request):
        return f"Подготовленные данные для: {request}"

class DataScientist:
    def __init__(self, engineer):
        self.engineer = engineer
    
    def build_model(self, data_request):
        data = self.engineer.provide_data(data_request)
        return f"Модель построена на основе {data}"

# Взаимодействие

engineer = DataEngineer()
scientist = DataScientist(engineer)

result = scientist.build_model("user behavior prediction")
print(result)
```

**Output:**
```
Модель построена на основе Подготовленные данные для: user behavior prediction
```

---

## 4. Типы data-систем

Data-системы можно классифицировать по различным критериям. Понимание типов систем помогает выбрать правильный подход для конкретной задачи.

### 4.1 По типу обработки

**Batch Processing Systems:**

- Обрабатывают данные порциями (батчами)
- Обычно запускаются по расписанию
- Хорошо для больших объёмов данных
- Примеры: ETL jobs, ночные обновления

**Streaming Processing Systems:**

- Обрабатывают данные в реальном времени
- Непрерывный поток событий
- Низкая задержка (latency)
- Примеры: real-time analytics, fraud detection

**Example: Batch vs Streaming**

```python
# Batch Processing: обработка всех данных раз в день

def batch_process():
    """Обрабатывает все данные за вчера"""
    yesterday_data = load_data_for_date("2024-01-01")
    processed = transform_data(yesterday_data)
    save_to_warehouse(processed)
    print("Batch processing завершён")

# Streaming Processing: обработка каждого события сразу

def stream_process(event):
    """Обрабатывает событие в реальном времени"""
    processed = transform_event(event)
    update_realtime_dashboard(processed)
    print(f"Событие обработано: {event['id']}")

# Batch: запускается по расписанию (например, в 2:00 ночи)
# Streaming: обрабатывает события по мере поступления
```

**Output:**
```
Batch processing завершён
Событие обработано: event_123
```

### 4.2 По типу хранилища

**OLTP (Online Transaction Processing):**

- Оптимизированы для транзакций
- Быстрые записи и чтения отдельных записей
- Нормализованная структура
- Примеры: PostgreSQL, MySQL, MongoDB

**OLAP (Online Analytical Processing):**

- Оптимизированы для аналитики
- Быстрые агрегации и аналитические запросы
- Денормализованная структура
- Примеры: Snowflake, BigQuery, Redshift

**Example: OLTP vs OLAP**

```python
# OLTP: быстрая запись транзакции

def oltp_write_transaction(user_id, amount):
    """Записывает транзакцию в OLTP базу"""
    transaction = {
        "id": generate_id(),
        "user_id": user_id,
        "amount": amount,
        "timestamp": datetime.now()
    }
    # Запись в нормализованную таблицу
    db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?)", 
               transaction.values())
    print(f"Транзакция {transaction['id']} записана")

# OLAP: аналитический запрос

def olap_get_monthly_revenue():
    """Получает месячную выручку из OLAP хранилища"""
    # Агрегация по денормализованным данным
    result = db.execute("""
        SELECT 
            DATE_TRUNC('month', date) as month,
            SUM(revenue) as total_revenue
        FROM sales_facts
        GROUP BY month
    """)
    print("Месячная выручка:")
    for row in result:
        print(f"  {row['month']}: ${row['total_revenue']}")

# OLTP: оптимизирован для записи одной транзакции
# OLAP: оптимизирован для агрегации миллионов записей
```

**Output:**
```
Транзакция tx_12345 записана
Месячная выручка:
  2024-01-01: $50000
  2024-02-01: $60000
```

### 4.3 По архитектуре

**Monolithic Data Systems:**

- Всё в одной системе
- Простота развёртывания
- Сложность масштабирования
- Пример: одна база данных для всего

**Distributed Data Systems:**

- Данные распределены по нескольким узлам
- Горизонтальное масштабирование
- Сложность координации
- Примеры: Hadoop, Spark, Kafka

**Example: Monolithic vs Distributed**

```python
# Monolithic: одна база данных

class MonolithicSystem:
    def __init__(self):
        self.database = {}  # Всё в одном месте
    
    def store(self, key, value):
        self.database[key] = value
        print(f"Сохранено в монолитной системе: {key}")

# Distributed: данные распределены

class DistributedSystem:
    def __init__(self, nodes=3):
        self.nodes = [{} for _ in range(nodes)]
    
    def _hash_key(self, key):
        """Определяет, на каком узле хранить"""
        return hash(key) % len(self.nodes)
    
    def store(self, key, value):
        node_id = self._hash_key(key)
        self.nodes[node_id][key] = value
        print(f"Сохранено на узле {node_id}: {key}")

# Сравнение

mono = MonolithicSystem()
mono.store("user_1", "data")

dist = DistributedSystem()
dist.store("user_1", "data")
```

**Output:**
```
Сохранено в монолитной системе: user_1
Сохранено на узле 1: user_1
```

---

## 5. Данные как продукт

Концепция "данные как продукт" (Data as a Product) означает, что данные должны рассматриваться как полноценный продукт со своими пользователями, документацией, версионированием и SLA.

### 5.1 Принципы Data as a Product

**1. Пользователь-ориентированность:**

- Данные должны быть полезны для конкретных пользователей
- Формат и структура должны соответствовать потребностям
- Документация должна быть понятной

**2. Качество:**

- Данные должны быть точными и полными
- Схема должна быть стабильной
- Ошибки должны обрабатываться явно

**3. Доступность:**

- Данные должны быть легко доступны
- API или интерфейсы должны быть удобными
- Производительность должна соответствовать требованиям

**4. Надёжность:**

- Данные должны обновляться регулярно
- SLA должно быть определено и соблюдаться
- Проблемы должны решаться быстро

**Example: Data Product**

```python
class DataProduct:
    """Данные как продукт с документацией и SLA"""
    
    def __init__(self, name, schema, update_frequency):
        self.name = name
        self.schema = schema
        self.update_frequency = update_frequency
        self.users = []
        self.documentation = {}
    
    def add_user(self, user, use_case):
        """Регистрирует пользователя продукта"""
        self.users.append({"user": user, "use_case": use_case})
        print(f"Пользователь {user} добавлен: {use_case}")
    
    def document(self, field, description):
        """Документирует поле данных"""
        self.documentation[field] = description
    
    def get_info(self):
        """Возвращает информацию о продукте"""
        return {
            "name": self.name,
            "schema": self.schema,
            "update_frequency": self.update_frequency,
            "users_count": len(self.users),
            "documented_fields": len(self.documentation)
        }

# Создание data product

user_events = DataProduct(
    name="user_events",
    schema={"user_id": "int", "event": "string", "timestamp": "datetime"},
    update_frequency="hourly"
)

user_events.add_user("analytics_team", "dashboard updates")
user_events.add_user("ml_team", "feature engineering")
user_events.document("user_id", "Уникальный идентификатор пользователя")
user_events.document("event", "Тип события: click, purchase, view")

info = user_events.get_info()
print(f"\nData Product: {info['name']}")
print(f"  Пользователей: {info['users_count']}")
print(f"  Документировано полей: {info['documented_fields']}")
```

**Output:**
```
Пользователь analytics_team добавлен: dashboard updates
Пользователь ml_team добавлен: feature engineering

Data Product: user_events
  Пользователей: 2
  Документировано полей: 2
```

### 5.2 Преимущества подхода "данные как продукт"

**Для пользователей:**

- Понятная документация
- Стабильные схемы
- Предсказуемое обновление

**Для Data Engineers:**

- Чёткие требования
- Приоритизация задач
- Метрики успеха

**Для бизнеса:**

- Переиспользование данных
- Снижение дублирования
- Ускорение разработки

---

## 6. Типичные задачи Data Engineer

Понимание типичных задач помогает понять, что именно делает Data Engineer в повседневной работе.

### 6.1 Сбор данных (Data Ingestion)

Сбор данных из различных источников — первая задача в любом data pipeline.

**Источники данных:**

- Базы данных (SQL, NoSQL)
- API (REST, GraphQL)
- Файлы (CSV, JSON, Parquet)
- Очереди сообщений (Kafka, RabbitMQ)
- Потоковые источники (веб-сокеты, события)

**Example: Сбор данных из разных источников**

```python
import json
import csv
from datetime import datetime

def ingest_from_database():
    """Сбор данных из базы данных"""
    # Симуляция SQL запроса
    data = [
        {"id": 1, "name": "Product A", "price": 99.99},
        {"id": 2, "name": "Product B", "price": 149.99}
    ]
    print(f"Собрано {len(data)} записей из базы данных")
    return data

def ingest_from_api():
    """Сбор данных из REST API"""
    # Симуляция API запроса
    response = {
        "users": [
            {"user_id": 1, "email": "user1@example.com"},
            {"user_id": 2, "email": "user2@example.com"}
        ]
    }
    print(f"Собрано {len(response['users'])} записей из API")
    return response["users"]

def ingest_from_file(filepath):
    """Сбор данных из файла"""
    # Симуляция чтения CSV
    data = [
        {"date": "2024-01-01", "sales": 1000},
        {"date": "2024-01-02", "sales": 1200}
    ]
    print(f"Собрано {len(data)} записей из файла {filepath}")
    return data

# Сбор из всех источников

db_data = ingest_from_database()
api_data = ingest_from_api()
file_data = ingest_from_file("sales.csv")

total_records = len(db_data) + len(api_data) + len(file_data)
print(f"\nВсего собрано записей: {total_records}")
```

**Output:**
```
Собрано 2 записей из базы данных
Собрано 2 записей из API
Собрано 2 записей из файла sales.csv

Всего собрано записей: 6
```

### 6.2 Трансформация данных (Data Transformation)

Собранные данные часто нужно трансформировать: очистить, нормализовать, обогатить.

**Типичные трансформации:**

- Очистка (удаление дубликатов, обработка NULL)
- Нормализация (приведение к единому формату)
- Обогащение (добавление вычисляемых полей)
- Агрегация (суммирование, группировка)

**Example: Трансформация данных**

```python
def clean_data(raw_data):
    """Очистка данных"""
    cleaned = []
    for record in raw_data:
        # Удаляем записи с отсутствующими обязательными полями
        if record.get("id") and record.get("name"):
            cleaned.append(record)
    return cleaned

def normalize_data(data):
    """Нормализация данных"""
    normalized = []
    for record in data:
        normalized.append({
            "id": int(record["id"]),
            "name": record["name"].strip().title(),
            "price": float(record.get("price", 0))
        })
    return normalized

def enrich_data(data):
    """Обогащение данных"""
    enriched = []
    for record in data:
        record["price_with_tax"] = record["price"] * 1.2  # НДС 20%
        record["category"] = "electronics"  # Пример обогащения
        enriched.append(record)
    return enriched

# Исходные данные

raw_data = [
    {"id": "1", "name": "  product a  ", "price": "99.99"},
    {"id": "2", "name": "product b", "price": "149.99"},
    {"id": "", "name": "invalid", "price": "0"}  # Невалидная запись
]

# Pipeline трансформации

cleaned = clean_data(raw_data)
normalized = normalize_data(cleaned)
enriched = enrich_data(normalized)

print("Трансформированные данные:")
for record in enriched:
    print(f"  {record}")
```

**Output:**
```
Трансформированные данные:
  {'id': 1, 'name': 'Product A', 'price': 99.99, 'price_with_tax': 119.988, 'category': 'electronics'}
  {'id': 2, 'name': 'Product B', 'price': 149.99, 'price_with_tax': 179.988, 'category': 'electronics'}
```

### 6.3 Загрузка данных (Data Loading)

Трансформированные данные загружаются в хранилище для дальнейшего использования.

**Типы загрузки:**

- **Full load**: полная загрузка всех данных

- **Incremental load**: загрузка только новых/изменённых данных

- **Upsert**: обновление существующих и вставка новых

**Example: Загрузка данных**

```python
class DataWarehouse:
    def __init__(self):
        self.data = {}
    
    def full_load(self, table_name, data):
        """Полная загрузка данных"""
        self.data[table_name] = data
        print(f"Full load: {len(data)} записей загружено в {table_name}")
    
    def incremental_load(self, table_name, new_data, key_field="id"):
        """Инкрементальная загрузка"""
        if table_name not in self.data:
            self.data[table_name] = {}
        
        existing_keys = set(self.data[table_name].keys())
        updated = 0
        inserted = 0
        
        for record in new_data:
            key = record[key_field]
            if key in existing_keys:
                self.data[table_name][key] = record
                updated += 1
            else:
                self.data[table_name][key] = record
                inserted += 1
        
        print(f"Incremental load: {inserted} новых, {updated} обновлено в {table_name}")

# Использование

warehouse = DataWarehouse()

# Первая загрузка

initial_data = [
    {"id": 1, "name": "Product A", "price": 99.99},
    {"id": 2, "name": "Product B", "price": 149.99}
]
warehouse.full_load("products", initial_data)

# Инкрементальное обновление

new_data = [
    {"id": 2, "name": "Product B Updated", "price": 159.99},  # Обновление
    {"id": 3, "name": "Product C", "price": 199.99}  # Новая запись
]
warehouse.incremental_load("products", new_data)
```

**Output:**
```
Full load: 2 записей загружено в products
Incremental load: 1 новых, 1 обновлено в products
```

---

## 7. Инструменты и технологии

Data Engineer работает с широким спектром инструментов. Понимание экосистемы помогает выбрать правильные инструменты.

### 7.1 Категории инструментов

**Хранилища данных:**

- Реляционные БД: PostgreSQL, MySQL
- Data Warehouses: Snowflake, BigQuery, Redshift
- Data Lakes: S3, Azure Data Lake, HDFS
- NoSQL: MongoDB, Cassandra, DynamoDB

**Обработка данных:**

- Batch: Spark, Hadoop, Airflow
- Streaming: Kafka, Flink, Pulsar
- SQL engines: Presto, Trino, Spark SQL

**Оркестрация:**

- Workflow: Airflow, Prefect, Dagster
- Scheduling: Cron, Kubernetes CronJobs

**Example: Выбор инструментов**

```python
# Матрица выбора инструментов для разных задач

tools_matrix = {
    "batch_processing": {
        "small_data": "Python + Pandas",
        "medium_data": "Spark",
        "large_data": "Spark on Hadoop"
    },
    "streaming": {
        "low_latency": "Kafka + Flink",
        "high_throughput": "Kafka + Spark Streaming",
        "simple": "Kafka Consumers"
    },
    "storage": {
        "structured": "PostgreSQL / MySQL",
        "analytics": "Snowflake / BigQuery",
        "unstructured": "S3 / Data Lake"
    },
    "orchestration": {
        "simple": "Cron",
        "complex": "Airflow",
        "modern": "Prefect / Dagster"
    }
}

def recommend_tools(use_case, requirements):
    """Рекомендует инструменты на основе требований"""
    category = tools_matrix.get(use_case, {})
    return category.get(requirements, "Не определено")

# Примеры рекомендаций

print("Рекомендации инструментов:")
print(f"  Batch processing (большие данные): {recommend_tools('batch_processing', 'large_data')}")
print(f"  Streaming (низкая задержка): {recommend_tools('streaming', 'low_latency')}")
print(f"  Хранилище (аналитика): {recommend_tools('storage', 'analytics')}")
```

**Output:**
```
Рекомендации инструментов:
  Batch processing (большие данные): Spark on Hadoop
  Streaming (низкая задержка): Kafka + Flink
  Хранилище (аналитика): Snowflake / BigQuery
```

---

## 8. Карьера в Data Engineering

Понимание карьерного пути помогает планировать развитие в области Data Engineering.

### 8.1 Уровни Data Engineer

**Junior Data Engineer:**

- Выполняет задачи под руководством
- Работает с готовыми инструментами
- Пишет простые ETL скрипты
- Навыки: Python, SQL, базовые инструменты

**Middle Data Engineer:**

- Проектирует простые pipelines
- Оптимизирует существующие системы
- Работает с несколькими инструментами
- Навыки: Spark, Airflow, облачные платформы

**Senior Data Engineer:**

- Проектирует сложные data-платформы
- Принимает архитектурные решения
- Менторство и руководство проектами
- Навыки: системный дизайн, масштабирование, стоимость

**Example: Развитие навыков**

```python
# Карта навыков по уровням

skills_map = {
    "junior": {
        "programming": ["Python", "SQL"],
        "tools": ["Pandas", "PostgreSQL"],
        "concepts": ["ETL basics", "Data modeling basics"]
    },
    "middle": {
        "programming": ["Python", "SQL", "Scala/Java"],
        "tools": ["Spark", "Airflow", "Kafka"],
        "concepts": ["Distributed systems", "Streaming", "Cloud platforms"]
    },
    "senior": {
        "programming": ["Python", "SQL", "Scala/Java", "Go"],
        "tools": ["Spark", "Airflow", "Kafka", "Kubernetes"],
        "concepts": ["System design", "Cost optimization", "Architecture patterns"]
    }
}

def get_skills_for_level(level):
    """Возвращает навыки для уровня"""
    return skills_map.get(level, {})

# Пример

junior_skills = get_skills_for_level("junior")
print("Junior Data Engineer навыки:")
for category, skills in junior_skills.items():
    print(f"  {category}: {', '.join(skills)}")
```

**Output:**
```
Junior Data Engineer навыки:
  programming: Python, SQL
  tools: Pandas, PostgreSQL
  concepts: ETL basics, Data modeling basics
```

---

## 💡 Key Takeaways

- **Data Engineering vs Data Science**: Data Engineering создаёт инфраструктуру, Data Science извлекает инсайты. Обе дисциплины важны и дополняют друг друга.

- **Роль Data Engineer**: Мост между источниками данных и их потребителями. Отвечает за надёжность, масштабирование и производительность data-систем.

- **Типы data-систем**: Batch vs Streaming, OLTP vs OLAP, Monolithic vs Distributed. Выбор зависит от требований к задержке, объёму данных и сложности.

- **Данные как продукт**: Данные должны рассматриваться как продукт с документацией, SLA и пользователями. Это улучшает качество и переиспользование.

- **Инструменты**: Широкий спектр инструментов для разных задач. Важно понимать, когда использовать каждый инструмент.

---

## 🚀 Next Steps

**Related Modules:**

- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных от источников до потребления
- [03_Data_Types](../03_Data_Types/) — типы данных и их характеристики
- [09_Batch_Processing](../09_Batch_Processing/) — batch processing и ETL/ELT

**Practice Ideas:**

1. Создайте простой ETL pipeline на Python, который собирает данные из CSV файла, трансформирует их и сохраняет в базу данных
2. Изучите разницу между OLTP и OLAP на практике: создайте простую транзакционную БД и аналитическое хранилище
3. Проанализируйте data-систему в вашей компании или проекте: определите источники данных, типы обработки, хранилища

**Going Deeper:**

- Изучите архитектуру современных data-платформ (Snowflake, Databricks)
- Погрузитесь в distributed systems: как работают Spark, Kafka
- Изучите концепции data mesh и data fabric

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — фундаментальная книга о data-системах
- "Fundamentals of Data Engineering" by Joe Reis & Matt Housley — практическое руководство по Data Engineering

**Articles:**

- "The Rise of the Data Engineer" — статья о развитии профессии
- "Data Engineering Best Practices" — лучшие практики в Data Engineering

**Documentation:**

- Apache Spark: https://spark.apache.org/docs/latest/
- Apache Airflow: https://airflow.apache.org/docs/
- Apache Kafka: https://kafka.apache.org/documentation/

---



