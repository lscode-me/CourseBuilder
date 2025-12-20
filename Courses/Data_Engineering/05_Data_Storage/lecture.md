# Data Engineering
## Хранилища данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать типы данных (модуль 03)
- Знать основы data modeling (модуль 04)
- Иметь представление о жизненном цикле данных (модуль 02)

**Recommended prior modules:**

- [03_Data_Types](../03_Data_Types/) — типы данных
- [04_Data_Modeling](../04_Data_Modeling/) — основы data modeling
- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать типы хранилищ данных: databases, data warehouses, data lakes, lakehouse
- Выбирать подходящее хранилище для конкретных задач
- Понимать trade-offs между различными подходами к хранению
- Проектировать архитектуру хранения данных

---

## 1. Введение в хранилища данных

Выбор правильного хранилища данных критичен для производительности, масштабируемости и стоимости системы. Различные типы хранилищ оптимизированы для разных паттернов доступа и использования.

**Основные типы хранилищ:**

- **Databases** — для операционных данных (OLTP)

- **Data Warehouses** — для аналитических данных (OLAP)

- **Data Lakes** — для сырых данных различных форматов

- **Lakehouse** — гибридный подход, объединяющий lake и warehouse

---

## 2. Databases (Базы данных)

Databases — это системы управления данными, оптимизированные для операционных транзакций и быстрого доступа к отдельным записям.

### 2.1 Реляционные базы данных (RDBMS)

**Характеристики:**

- Структурированные данные в таблицах
- ACID транзакции
- SQL для запросов
- Нормализованная структура

**Примеры:**

- PostgreSQL, MySQL, Oracle
- SQL Server, SQLite

**Use cases:**

- Операционные системы (OLTP)
- Транзакционные данные
- Данные с высокой целостностью

**Example: Реляционная база данных**

```python
# Симуляция работы с реляционной БД
class RelationalDB:
    def __init__(self):
        self.tables = {}
    
    def create_table(self, name, schema):
        """Создаёт таблицу с определённой схемой"""
        self.tables[name] = {
            "schema": schema,
            "data": []
        }
        print(f"✅ Таблица '{name}' создана со схемой: {schema}")
    
    def insert(self, table, record):
        """Вставляет запись с проверкой схемы"""
        if table not in self.tables:
            raise ValueError(f"Таблица {table} не существует")
        
        # Проверка схемы
        schema = self.tables[table]["schema"]
        if set(record.keys()) != set(schema.keys()):
            raise ValueError("Запись не соответствует схеме")
        
        self.tables[table]["data"].append(record)
        print(f"✅ Запись добавлена в '{table}'")
    
    def query(self, table, condition=None):
        """Выполняет запрос"""
        if table not in self.tables:
            return []
        
        data = self.tables[table]["data"]
        if condition:
            data = [r for r in data if condition(r)]
        
        return data

# Использование
db = RelationalDB()

# Создание таблицы с фиксированной схемой
db.create_table("users", {
    "user_id": "INT",
    "name": "VARCHAR(100)",
    "email": "VARCHAR(255)"
})

# Вставка данных
db.insert("users", {
    "user_id": 1,
    "name": "Alice",
    "email": "alice@example.com"
})

# Запрос
users = db.query("users")
print(f"\nПользователи в БД: {len(users)}")
```

**Output:**
```

✅ Таблица 'users' создана со схемой: {'user_id': 'INT', 'name': 'VARCHAR(100)', 'email': 'VARCHAR(255)'}
✅ Запись добавлена в 'users'

Пользователи в БД: 1
```

### 2.2 NoSQL базы данных

**Типы NoSQL:**

- **Document** (MongoDB, CouchDB) — JSON-подобные документы

- **Key-Value** (Redis, DynamoDB) — простые пары ключ-значение

- **Column-family** (Cassandra, HBase) — колоночные хранилища

- **Graph** (Neo4j) — графовые структуры

**Характеристики:**

- Гибкая схема
- Горизонтальное масштабирование
- Высокая производительность для специфических use cases

**Example: Document база данных**

```python
# Симуляция Document DB (MongoDB-подобная)
class DocumentDB:
    def __init__(self):
        self.collections = {}
    
    def create_collection(self, name):
        """Создаёт коллекцию (аналог таблицы)"""
        self.collections[name] = []
        print(f"✅ Коллекция '{name}' создана")
    
    def insert(self, collection, document):
        """Вставляет документ (гибкая схема)"""
        if collection not in self.collections:
            self.create_collection(collection)
        
        # Добавляем _id если нет
        if "_id" not in document:
            document["_id"] = len(self.collections[collection]) + 1
        
        self.collections[collection].append(document)
        print(f"✅ Документ добавлен в '{collection}'")
    
    def find(self, collection, query=None):
        """Находит документы"""
        if collection not in self.collections:
            return []
        
        docs = self.collections[collection]
        if query:
            # Простая фильтрация
            docs = [d for d in docs if all(d.get(k) == v for k, v in query.items())]
        
        return docs

# Использование
doc_db = DocumentDB()

# Гибкая схема - разные документы могут иметь разные поля
doc_db.insert("users", {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
})

doc_db.insert("users", {
    "name": "Bob",
    "email": "bob@example.com",
    "skills": ["Python", "SQL"],  # Дополнительное поле
    "address": {
        "city": "Moscow",
        "zip": "101000"
    }
})

users = doc_db.find("users")
print(f"\nПользователи в коллекции: {len(users)}")
print(f"Разные схемы документов: {[set(u.keys()) for u in users]}")
```

**Output:**
```

✅ Коллекция 'users' создана
✅ Документ добавлен в 'users'
✅ Документ добавлен в 'users'

Пользователи в коллекции: 2
Разные схемы документов: [{'_id', 'name', 'email', 'age'}, {'_id', 'name', 'email', 'skills', 'address'}]
```

---

## 3. Data Warehouses (Хранилища данных)

Data Warehouses — это специализированные хранилища, оптимизированные для аналитических запросов и отчётов.

### 3.1 Характеристики Data Warehouses

**Оптимизация:**

- Columnar storage для быстрых агрегаций
- Денормализованная структура
- Оптимизация для чтения
- Масштабирование для больших объёмов

**Примеры:**

- Snowflake, BigQuery, Redshift
- Azure Synapse, Databricks SQL

**Use cases:**

- Business Intelligence
- Аналитические отчёты
- Data Science
- Исторические данные

**Example: Data Warehouse запрос**

```python
# Симуляция Data Warehouse (columnar storage)
class DataWarehouse:
    def __init__(self):
        self.tables = {}
    
    def load_data(self, table_name, data):
        """Загружает данные в warehouse"""
        # В реальности используется columnar формат (Parquet)
        self.tables[table_name] = data
        print(f"✅ Данные загружены в '{table_name}': {len(data)} записей")
    
    def analytical_query(self, table, aggregations):
        """Выполняет аналитический запрос"""
        if table not in self.tables:
            return {}
        
        data = self.tables[table]
        results = {}
        
        for agg in aggregations:
            field = agg["field"]
            operation = agg["operation"]
            
            if operation == "sum":
                results[f"sum_{field}"] = sum(r.get(field, 0) for r in data)
            elif operation == "avg":
                values = [r.get(field, 0) for r in data if field in r]
                results[f"avg_{field}"] = sum(values) / len(values) if values else 0
            elif operation == "count":
                results[f"count_{field}"] = len([r for r in data if field in r])
        
        return results

# Использование
warehouse = DataWarehouse()

# Загрузка данных (денормализованные)
sales_data = [
    {"date": "2024-01-01", "product": "Laptop", "revenue": 999.99, "quantity": 10},
    {"date": "2024-01-01", "product": "Mouse", "revenue": 29.99, "quantity": 50},
    {"date": "2024-01-02", "product": "Laptop", "revenue": 999.99, "quantity": 15},
    {"date": "2024-01-02", "product": "Keyboard", "revenue": 79.99, "quantity": 30}
]

warehouse.load_data("sales", sales_data)

# Аналитический запрос
results = warehouse.analytical_query("sales", [
    {"field": "revenue", "operation": "sum"},
    {"field": "quantity", "operation": "sum"},
    {"field": "revenue", "operation": "avg"}
])

print("\nАналитические результаты:")
for key, value in results.items():
    print(f"  {key}: {value:.2f}" if isinstance(value, float) else f"  {key}: {value}")
```

**Output:**
```

✅ Данные загружены в 'sales': 4 записей

Аналитические результаты:
  sum_revenue: 2109.96
  sum_quantity: 105
  avg_revenue: 527.49
```

### 3.2 Преимущества Data Warehouses

**Производительность:**

- Columnar storage ускоряет агрегации
- Оптимизация для сложных аналитических запросов
- Параллельная обработка

**Масштабирование:**

- Горизонтальное масштабирование
- Отделение compute от storage
- Эластичное масштабирование

---

## 4. Data Lakes (Озёра данных)

Data Lakes — это хранилища сырых данных в их нативном формате без предварительной обработки.

### 4.1 Характеристики Data Lakes

**Структура:**

- Хранит данные "как есть"
- Различные форматы (CSV, JSON, Parquet, изображения, видео)
- Schema-on-read (схема применяется при чтении)
- Масштабируемое хранилище

**Примеры:**

- AWS S3, Azure Data Lake Storage
- Google Cloud Storage, HDFS

**Use cases:**

- Сырые данные из различных источников
- Большие объёмы данных
- Данные с неизвестной схемой
- Медиа файлы

**Example: Data Lake структура**

```python
# Симуляция Data Lake
class DataLake:
    def __init__(self):
        self.buckets = {}
    
    def store_raw_data(self, bucket, path, data, format_type):
        """Хранит сырые данные в нативном формате"""
        if bucket not in self.buckets:
            self.buckets[bucket] = {}
        
        self.buckets[bucket][path] = {
            "data": data,
            "format": format_type,
            "schema": None  # Schema-on-read
        }
        print(f"✅ Данные сохранены в {bucket}/{path} (формат: {format_type})")
    
    def read_with_schema(self, bucket, path, schema):
        """Читает данные с применением схемы (schema-on-read)"""
        if bucket not in self.buckets or path not in self.buckets[bucket]:
            return None
        
        file_info = self.buckets[bucket][path]
        data = file_info["data"]
        
        # Применяем схему при чтении
        if schema:
            # Симуляция применения схемы
            print(f"📖 Чтение {path} с применением схемы: {schema}")
            return data
        
        return data

# Использование
lake = DataLake()

# Хранение данных в различных форматах
lake.store_raw_data("raw-data", "users/2024-01-01.json", 
                   [{"id": 1, "name": "Alice"}], "JSON")

lake.store_raw_data("raw-data", "logs/2024-01-01.txt",
                   "2024-01-01 10:00:00 ERROR: Connection failed", "TEXT")

lake.store_raw_data("raw-data", "images/product_001.jpg",
                   b"binary_image_data", "BINARY")

print(f"\nФайлы в Data Lake: {len(lake.buckets['raw-data'])}")
for path, info in lake.buckets["raw-data"].items():
    print(f"  {path}: {info['format']}")
```

**Output:**
```

✅ Данные сохранены в raw-data/users/2024-01-01.json (формат: JSON)
✅ Данные сохранены в raw-data/logs/2024-01-01.txt (формат: TEXT)
✅ Данные сохранены в raw-data/images/product_001.jpg (формат: BINARY)

Файлы в Data Lake: 3
  users/2024-01-01.json: JSON
  logs/2024-01-01.txt: TEXT
  images/product_001.jpg: BINARY
```

### 4.2 Преимущества и недостатки Data Lakes

**Преимущества:**

- Гибкость: любые форматы данных
- Масштабируемость: практически неограниченный объём
- Экономичность: дешёвое хранилище
- Schema-on-read: схема определяется при использовании

**Недостатки:**

- Может стать "data swamp" без управления
- Требует обработки для использования
- Нет гарантий качества данных
- Сложность поиска и discovery

---

## 5. Lakehouse (Гибридный подход)

Lakehouse — это современная архитектура, объединяющая преимущества Data Lake и Data Warehouse.

### 5.1 Концепция Lakehouse

**Характеристики:**

- Хранит данные в открытых форматах (Parquet, Delta Lake)
- Поддерживает ACID транзакции
- Schema enforcement и governance
- Единое хранилище для всех типов данных

**Примеры:**

- Databricks Delta Lake
- Apache Iceberg
- Apache Hudi

**Example: Lakehouse архитектура**

```python
# Симуляция Lakehouse
class Lakehouse:
    def __init__(self):
        self.layers = {
            "bronze": {},  # Сырые данные
            "silver": {},  # Очищенные данные
            "gold": {}     # Готовые для потребления
        }
        self.metadata = {}
    
    def store_bronze(self, path, data):
        """Bronze: сырые данные как есть"""
        self.layers["bronze"][path] = data
        print(f"🥉 Bronze: {path} сохранён")
    
    def process_to_silver(self, bronze_path, silver_path, schema):
        """Silver: очищенные данные с схемой"""
        if bronze_path not in self.layers["bronze"]:
            raise ValueError(f"Файл {bronze_path} не найден в Bronze")
        
        raw_data = self.layers["bronze"][bronze_path]
        # Симуляция очистки и применения схемы
        cleaned_data = raw_data  # В реальности: валидация, очистка
        
        self.layers["silver"][silver_path] = {
            "data": cleaned_data,
            "schema": schema
        }
        print(f"🥈 Silver: {silver_path} создан со схемой")
    
    def aggregate_to_gold(self, silver_paths, gold_path, aggregation):
        """Gold: агрегированные данные для потребления"""
        # Симуляция агрегации
        aggregated = {"summary": "aggregated_data"}
        
        self.layers["gold"][gold_path] = aggregated
        print(f"🥇 Gold: {gold_path} создан")
    
    def query(self, layer, path):
        """Запрос к любому слою"""
        if layer not in self.layers:
            return None
        
        if path in self.layers[layer]:
            return self.layers[layer][path]
        return None

# Использование

lakehouse = Lakehouse()

# Bronze: сырые данные

lakehouse.store_bronze("raw/users_2024-01-01.json", 
                       [{"id": "1", "name": "Alice", "email": "alice@example.com"}])

# Silver: очищенные с схемой
lakehouse.process_to_silver(
    "raw/users_2024-01-01.json",
    "cleaned/users_2024-01-01.parquet",
    {"id": "INT", "name": "VARCHAR", "email": "VARCHAR"}
)

# Gold: агрегированные

lakehouse.aggregate_to_gold(
    ["cleaned/users_2024-01-01.parquet"],
    "analytics/daily_users_summary.parquet",
    "daily_summary"
)

print(f"\nСлои Lakehouse:")
for layer, files in lakehouse.layers.items():
    print(f"  {layer}: {len(files)} файлов")
```

**Output:**
```

🥉 Bronze: raw/users_2024-01-01.json сохранён
🥈 Silver: cleaned/users_2024-01-01.parquet создан со схемой
🥇 Gold: analytics/daily_users_summary.parquet создан

Слои Lakehouse:
  bronze: 1 файлов
  silver: 1 файлов
  gold: 1 файлов
```

### 5.2 Преимущества Lakehouse

**Единое хранилище:**

- Все данные в одном месте
- Различные форматы поддерживаются
- Открытые форматы (Parquet, Delta)

**Управление данными:**

- ACID транзакции
- Schema enforcement
- Time travel (версионирование)
- Data governance

**Производительность:**

- Оптимизация запросов
- Кеширование
- Индексы

---

## 6. Сравнение хранилищ

Выбор хранилища зависит от требований к данным, паттернов доступа и использования.

### 6.1 Таблица сравнения

| Характеристика | Database | Data Warehouse | Data Lake | Lakehouse |
|----------------|----------|----------------|-----------|-----------|
| **Назначение** | Операции (OLTP) | Аналитика (OLAP) | Сырые данные | Гибрид |
| **Схема** | Schema-on-write | Schema-on-write | Schema-on-read | Schema-on-write + read |
| **Форматы** | Структурированные | Структурированные | Любые | Открытые (Parquet) |
| **Оптимизация** | Запись | Чтение | Хранение | И то, и другое |
| **Стоимость** | Средняя | Высокая | Низкая | Средняя |
| **Масштабирование** | Вертикальное | Горизонтальное | Горизонтальное | Горизонтальное |

### 6.2 Когда использовать каждое хранилище

**Database:**

- Операционные системы
- Транзакционные данные
- Высокие требования к целостности
- Real-time доступ

**Data Warehouse:**

- Аналитические запросы
- Business Intelligence
- Исторические данные
- Сложные агрегации

**Data Lake:**

- Сырые данные из различных источников
- Большие объёмы данных
- Неизвестная схема
- Медиа файлы

**Lakehouse:**

- Современные data-платформы
- Нужны и операционные, и аналитические данные
- Требуется governance
- Единое хранилище

**Example: Выбор хранилища**

```python

def recommend_storage(requirements):
    """Рекомендует хранилище на основе требований"""
    if requirements.get("operational") and requirements.get("transactions"):
        return "Database (PostgreSQL, MySQL)"
    elif requirements.get("analytical") and requirements.get("bi_reports"):
        return "Data Warehouse (Snowflake, BigQuery)"
    elif requirements.get("raw_data") and requirements.get("various_formats"):
        return "Data Lake (S3, Azure Data Lake)"
    elif requirements.get("hybrid") and requirements.get("governance"):
        return "Lakehouse (Delta Lake, Iceberg)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"operational": True, "transactions": True, "real_time": True},
    {"analytical": True, "bi_reports": True, "historical_data": True},
    {"raw_data": True, "various_formats": True, "large_volume": True},
    {"hybrid": True, "governance": True, "unified_storage": True}
]

print("Рекомендации хранилищ:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_storage(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации хранилищ:
  Пример 1: Database (PostgreSQL, MySQL)
  Пример 2: Data Warehouse (Snowflake, BigQuery)
  Пример 3: Data Lake (S3, Azure Data Lake)
  Пример 4: Lakehouse (Delta Lake, Iceberg)
```

---

## 7. Архитектура хранения данных

В реальных системах часто используется комбинация хранилищ для разных целей.

### 7.1 Многослойная архитектура

**Operational Layer:**

- Databases для транзакций
- Real-time доступ
- Высокая целостность

**Analytical Layer:**

- Data Warehouse для аналитики
- Batch обновления
- Оптимизация чтения

**Raw Data Layer:**

- Data Lake для сырых данных
- Долгосрочное хранение
- Различные форматы

**Example: Многослойная архитектура**

```python

class MultiLayerStorage:
    def __init__(self):
        self.operational = {}  # Database
        self.analytical = {}   # Data Warehouse
        self.raw = {}          # Data Lake
    
    def store_operational(self, data):
        """Хранит операционные данные"""
        self.operational.update(data)
        print("💾 Operational: данные сохранены в Database")
    
    def store_analytical(self, data):
        """Хранит аналитические данные"""
        self.analytical.update(data)
        print("📊 Analytical: данные сохранены в Data Warehouse")
    
    def store_raw(self, path, data):
        """Хранит сырые данные"""
        self.raw[path] = data
        print(f"🌊 Raw: данные сохранены в Data Lake ({path})")
    
    def get_architecture(self):
        """Возвращает описание архитектуры"""
        return {
            "operational": f"{len(self.operational)} записей",
            "analytical": f"{len(self.analytical)} записей",
            "raw": f"{len(self.raw)} файлов"
        }

# Использование

storage = MultiLayerStorage()

# Операционные данные

storage.store_operational({"order_1001": {"user_id": 1, "amount": 99.99}})

# Аналитические данные

storage.store_analytical({"daily_revenue": 50000.00})

# Сырые данные

storage.store_raw("logs/2024-01-01.json", {"events": []})

arch = storage.get_architecture()
print(f"\nАрхитектура хранения:")
for layer, info in arch.items():
    print(f"  {layer}: {info}")
```

**Output:**
```

💾 Operational: данные сохранены в Database
📊 Analytical: данные сохранены в Data Warehouse
🌊 Raw: данные сохранены в Data Lake (logs/2024-01-01.json)

Архитектура хранения:
  operational: 1 записей
  analytical: 1 записей
  raw: 1 файлов
```

---

## 💡 Key Takeaways

- **Типы хранилищ**: Databases для операций, Data Warehouses для аналитики, Data Lakes для сырых данных, Lakehouse как гибрид. Каждый тип оптимизирован для своих задач.

- **Schema-on-write vs Schema-on-read**: Databases и Warehouses применяют схему при записи, Lakes — при чтении. Lakehouse поддерживает оба подхода.

- **Выбор хранилища**: Зависит от назначения данных, паттернов доступа, форматов и требований к масштабированию. Нет универсального решения.

- **Многослойная архитектура**: Реальные системы часто используют комбинацию хранилищ: operational для транзакций, analytical для отчётов, raw для долгосрочного хранения.

- **Lakehouse как будущее**: Современные платформы движутся к Lakehouse архитектуре, объединяющей гибкость Lake с управлением Warehouse.

---

## 🚀 Next Steps

**Related Modules:**

- [06_Data_Formats](../06_Data_Formats/) — форматы данных (Parquet, Avro, ORC)
- [07_Indexes_Partitioning](../07_Indexes_Partitioning/) — индексы и партиционирование
- [09_Batch_Processing](../09_Batch_Processing/) — batch processing и ETL

**Practice Ideas:**

1. Спроектируйте архитектуру хранения для вашего проекта: определите, какие данные где хранить
2. Изучите разницу между Database и Data Warehouse на практике
3. Проанализируйте, подходит ли Lakehouse архитектура для вашей системы

**Going Deeper:**

- Изучите Delta Lake: ACID транзакции в Data Lake
- Погрузитесь в архитектуру Snowflake или BigQuery
- Изучите Data Lakehouse паттерны и best practices

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — главы о хранении данных
- "Fundamentals of Data Engineering" by Joe Reis & Matt Housley — хранилища данных

**Articles:**

- "Data Lake vs Data Warehouse vs Data Lakehouse" — сравнение подходов
- "What is a Data Lakehouse?" — современная архитектура

**Documentation:**

- Delta Lake: https://delta.io/
- Apache Iceberg: https://iceberg.apache.org/
- Snowflake: https://docs.snowflake.com/

---


