# Архитектуры data-платформ

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать batch и streaming обработку (модули 09, 13)
- Знать хранилища данных (модуль 05)
- Иметь представление о масштабировании

**Recommended prior modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing
- [13_Streaming_Model](../13_Streaming_Model/) — streaming модель
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проектировать Lambda архитектуру для batch и streaming
- Применять Kappa архитектуру для упрощения
- Понимать современный data stack
- Выбирать подходящую архитектуру для use case

---

## 1. Введение в архитектуры data-платформ

Архитектура data-платформы определяет, как организованы компоненты для обработки, хранения и предоставления данных. Выбор архитектуры критичен для масштабируемости и надёжности.

**Основные архитектуры:**

- **Lambda** — разделение batch и streaming слоёв

- **Kappa** — единый streaming слой

- **Modern Data Stack** — современный подход с облачными сервисами

---

## 2. Lambda Architecture

Lambda архитектура разделяет обработку на batch и streaming слои.

### 2.1 Компоненты Lambda

**Batch Layer:**

- Обработка всех данных
- Точные результаты
- Высокая задержка

**Speed Layer:**

- Обработка новых данных
- Приблизительные результаты
- Низкая задержка

**Serving Layer:**

- Объединение результатов
- Предоставление данных
- Query interface

**Example: Lambda Architecture**

```python

class LambdaArchitecture:
    def __init__(self):
        self.batch_layer = {}
        self.speed_layer = {}
        self.serving_layer = {}
    
    def batch_process(self, data, computation):
        """Batch layer: обработка всех данных"""
        print("📦 Batch Layer: обработка всех данных")
        result = computation(data)
        self.batch_layer["result"] = result
        self.batch_layer["last_updated"] = "2024-01-01T02:00:00Z"
        print(f"✅ Batch результат: {result}")
        return result
    
    def speed_process(self, new_data, computation):
        """Speed layer: обработка новых данных"""
        print("⚡ Speed Layer: обработка новых данных в реальном времени")
        result = computation(new_data)
        self.speed_layer["result"] = result
        self.speed_layer["last_updated"] = "2024-01-01T10:00:00Z"
        print(f"✅ Speed результат: {result}")
        return result
    
    def serve_query(self, query):
        """Serving layer: объединение результатов"""
        print("🌐 Serving Layer: объединение batch и speed результатов")
        
        batch_result = self.batch_layer.get("result", 0)
        speed_result = self.speed_layer.get("result", 0)
        
        # Объединение: batch (точный) + speed (приблизительный)
        combined = batch_result + speed_result
        
        print(f"✅ Query результат: {combined} (batch: {batch_result}, speed: {speed_result})")
        return combined

# Использование
lambda_arch = LambdaArchitecture()

# Batch processing (все данные)
all_data = [1, 2, 3, 4, 5]
lambda_arch.batch_process(all_data, sum)

# Speed processing (новые данные)

new_data = [6, 7]
lambda_arch.speed_process(new_data, sum)

# Query
result = lambda_arch.serve_query("total_sum")
```

**Output:**
```

📦 Batch Layer: обработка всех данных
✅ Batch результат: 15
⚡ Speed Layer: обработка новых данных в реальном времени
✅ Speed результат: 13
🌐 Serving Layer: объединение batch и speed результатов
✅ Query результат: 28 (batch: 15, speed: 13)
```

### 2.2 Преимущества и недостатки Lambda

**Преимущества:**

- Точные результаты из batch layer
- Низкая задержка из speed layer
- Разделение concerns

**Недостатки:**

- Дублирование логики (batch и speed)
- Сложность поддержки
- Два разных кода для одной задачи

---

## 3. Kappa Architecture

Kappa архитектура использует единый streaming слой для всех данных.

### 3.1 Компоненты Kappa

**Streaming Layer:**

- Единый слой для всех данных
- Обработка в реальном времени
- Replay для переобработки

**Serving Layer:**

- Предоставление данных
- Query interface
- Результаты из streaming

**Example: Kappa Architecture**

```python

class KappaArchitecture:
    def __init__(self):
        self.streaming_layer = []
        self.serving_layer = {}
    
    def stream_process(self, event, computation):
        """Streaming layer: обработка всех данных через streaming"""
        print(f"📡 Streaming Layer: обработка события {event}")
        
        # Обработка события
        result = computation(event)
        
        # Сохранение в log для replay
        self.streaming_layer.append({
            "event": event,
            "result": result,
            "timestamp": "2024-01-01T10:00:00Z"
        })
        
        # Обновление serving layer
        self.serving_layer["current_result"] = self.serving_layer.get("current_result", 0) + result
        
        print(f"✅ Streaming результат: {result}, текущая сумма: {self.serving_layer['current_result']}")
        return result
    
    def replay(self, from_timestamp, computation):
        """Replay: переобработка данных"""
        print(f"🔄 Replay с {from_timestamp}")
        
        # Переобработка событий
        replayed_results = []
        for entry in self.streaming_layer:
            if entry["timestamp"] >= from_timestamp:
                result = computation(entry["event"])
                replayed_results.append(result)
        
        print(f"✅ Replay завершён: {len(replayed_results)} событий переобработано")
        return replayed_results
    
    def serve_query(self, query):
        """Serving layer: предоставление данных"""
        print("🌐 Serving Layer: предоставление результатов")
        result = self.serving_layer.get("current_result", 0)
        print(f"✅ Query результат: {result}")
        return result

# Использование
kappa_arch = KappaArchitecture()

# Streaming processing (все данные через streaming)

kappa_arch.stream_process({"value": 1}, lambda e: e["value"])
kappa_arch.stream_process({"value": 2}, lambda e: e["value"])
kappa_arch.stream_process({"value": 3}, lambda e: e["value"])

# Query
result = kappa_arch.serve_query("total_sum")

# Replay
kappa_arch.replay("2024-01-01T09:00:00Z", lambda e: e["value"])
```

**Output:**
```

📡 Streaming Layer: обработка события {'value': 1}
✅ Streaming результат: 1, текущая сумма: 1
📡 Streaming Layer: обработка события {'value': 2}
✅ Streaming результат: 2, текущая сумма: 3
📡 Streaming Layer: обработка события {'value': 3}
✅ Streaming результат: 3, текущая сумма: 6
🌐 Serving Layer: предоставление результатов
✅ Query результат: 6
🔄 Replay с 2024-01-01T09:00:00Z
✅ Replay завершён: 3 событий переобработано
```

### 3.2 Преимущества и недостатки Kappa

**Преимущества:**

- Единая кодовая база
- Проще в поддержке
- Replay для переобработки

**Недостатки:**

- Требует эффективного replay
- Может быть медленнее для больших объёмов
- Зависимость от streaming инфраструктуры

---

## 4. Modern Data Stack

Modern Data Stack использует облачные сервисы и современные инструменты.

### 4.1 Компоненты Modern Data Stack

**Cloud Data Warehouses:**

- Snowflake, BigQuery, Redshift
- Управляемые сервисы
- Автоматическое масштабирование

**ELT Tools:**

- dbt для трансформаций
- Fivetran, Airbyte для ingestion
- SQL-based подход

**Orchestration:**

- Airflow, Prefect
- Управление workflows
- Мониторинг

**Example: Modern Data Stack**

```python

class ModernDataStack:
    def __init__(self):
        self.components = {
            "data_warehouse": "Snowflake",
            "ingestion": "Fivetran",
            "transformation": "dbt",
            "orchestration": "Airflow",
            "catalog": "DataHub"
        }
    
    def ingest(self, source):
        """Ingestion: загрузка данных"""
        print(f"📥 Ingestion ({self.components['ingestion']}): загрузка из {source}")
        print("✅ Данные загружены в data warehouse")
        return True
    
    def transform(self, models):
        """Transformation: SQL трансформации"""
        print(f"⚙️  Transformation ({self.components['transformation']}): выполнение {len(models)} моделей")
        print("✅ Трансформации выполнены")
        return True
    
    def orchestrate(self, workflow):
        """Orchestration: управление workflow"""
        print(f"🎼 Orchestration ({self.components['orchestration']}): выполнение workflow '{workflow}'")
        print("✅ Workflow выполнен")
        return True
    
    def query(self, sql):
        """Query: запросы к data warehouse"""
        print(f"🔍 Query ({self.components['data_warehouse']}): выполнение SQL")
        print("✅ Результаты получены")
        return {"rows": 1000}

# Использование
stack = ModernDataStack()

# Полный цикл
stack.ingest("postgres://source")
stack.transform(["users", "orders", "analytics"])
stack.orchestrate("daily_etl")
stack.query("SELECT * FROM analytics.users")
```

**Output:**
```

📥 Ingestion (Fivetran): загрузка из postgres://source
✅ Данные загружены в data warehouse
⚙️  Transformation (dbt): выполнение 3 моделей
✅ Трансформации выполнены
🎼 Orchestration (Airflow): выполнение workflow 'daily_etl'
✅ Workflow выполнен
🔍 Query (Snowflake): выполнение SQL
✅ Результаты получены
```

### 4.2 Преимущества Modern Data Stack

**Управляемые сервисы:**

- Меньше операционной нагрузки
- Автоматическое масштабирование
- Встроенная безопасность

**SQL-first:**

- Легко для аналитиков
- Стандартизированный подход
- Широкая поддержка

**Интеграция:**

- Готовая интеграция компонентов
- Экосистема инструментов
- Быстрое развёртывание

---

## 5. Data Mesh Architecture

Data Mesh — это децентрализованный подход к архитектуре data-платформы.

### 5.1 Принципы Data Mesh

**Domain-oriented:**

- Данные принадлежат доменам
- Домены владеют своими данными
- Децентрализация

**Self-serve:**

- Инфраструктура как платформа
- Самообслуживание для команд
- Стандартизация

**Example: Data Mesh концепция**

```python

class DataMeshPlatform:
    def __init__(self):
        self.domains = {}
        self.data_products = {}
    
    def register_domain(self, domain_name, owner):
        """Регистрирует домен"""
        self.domains[domain_name] = {
            "owner": owner,
            "data_products": []
        }
        print(f"🏢 Домен '{domain_name}' зарегистрирован, владелец: {owner}")
        return self.domains[domain_name]
    
    def create_data_product(self, domain_name, product_name, schema):
        """Создаёт data product в домене"""
        if domain_name not in self.domains:
            raise ValueError(f"Домен '{domain_name}' не существует")
        
        data_product = {
            "name": product_name,
            "domain": domain_name,
            "schema": schema,
            "owner": self.domains[domain_name]["owner"]
        }
        
        self.data_products[f"{domain_name}:{product_name}"] = data_product
        self.domains[domain_name]["data_products"].append(product_name)
        
        print(f"📦 Data product '{product_name}' создан в домене '{domain_name}'")
        return data_product
    
    def discover_data_product(self, product_name):
        """Обнаруживает data product"""
        for key, product in self.data_products.items():
            if product["name"] == product_name:
                print(f"🔍 Data product '{product_name}' найден в домене '{product['domain']}'")
                return product
        return None

# Использование
mesh = DataMeshPlatform()

# Регистрация доменов
mesh.register_domain("sales", "Sales Team")
mesh.register_domain("marketing", "Marketing Team")

# Создание data products
mesh.create_data_product("sales", "customer_orders", {"customer_id": "string", "order_id": "string"})
mesh.create_data_product("marketing", "campaign_metrics", {"campaign_id": "string", "impressions": "int"})

# Обнаружение
mesh.discover_data_product("customer_orders")
```

**Output:**
```

🏢 Домен 'sales' зарегистрирован, владелец: Sales Team
🏢 Домен 'marketing' зарегистрирован, владелец: Marketing Team
📦 Data product 'customer_orders' создан в домене 'sales'
📦 Data product 'campaign_metrics' создан в домене 'marketing'
🔍 Data product 'customer_orders' найден в домене 'sales'
```

---

## 6. Сравнение архитектур

Выбор архитектуры зависит от требований.

### 6.1 Decision Matrix

| Аспект | Lambda | Kappa | Modern Data Stack | Data Mesh |
|--------|--------|-------|-------------------|-----------|
| **Сложность** | Высокая | Средняя | Низкая | Высокая |
| **Точность** | Высокая (batch) | Зависит от replay | Высокая | Высокая |
| **Задержка** | Низкая (speed) | Низкая | Средняя | Зависит |
| **Поддержка** | Сложная | Проще | Проще | Сложная |
| **Use case** | Требуется точность | Streaming-first | Облачные решения | Децентрализация |

**Example: Выбор архитектуры**

```python

def recommend_architecture(requirements):
    """Рекомендует архитектуру"""
    if requirements.get("cloud_first") and requirements.get("sql_based"):
        return "Modern Data Stack (облачные сервисы, SQL-first)"
    elif requirements.get("streaming_first") and requirements.get("simplicity"):
        return "Kappa Architecture (единый streaming слой)"
    elif requirements.get("high_accuracy") and requirements.get("low_latency"):
        return "Lambda Architecture (batch + speed слои)"
    elif requirements.get("decentralized") and requirements.get("domain_ownership"):
        return "Data Mesh (децентрализованный подход)"
    else:
        return "Определить на основе детальных требований"

# Примеры
examples = [
    {"cloud_first": True, "sql_based": True, "managed_services": True},
    {"streaming_first": True, "simplicity": True, "replay": True},
    {"high_accuracy": True, "low_latency": True, "batch_and_streaming": True},
    {"decentralized": True, "domain_ownership": True, "self_serve": True}
]

print("Рекомендации архитектур:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_architecture(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации архитектур:
  Пример 1: Modern Data Stack (облачные сервисы, SQL-first)
  Пример 2: Kappa Architecture (единый streaming слой)
  Пример 3: Lambda Architecture (batch + speed слои)
```

### 6.2 Best Practices выбора архитектуры

**Когда использовать Lambda:**

- Требуется высокая точность batch результатов
- Нужна низкая задержка для новых данных
- Готовность поддерживать две кодовые базы

**Когда использовать Kappa:**

- Streaming-first подход
- Хотите упростить поддержку
- Эффективный replay доступен

**Когда использовать Modern Data Stack:**

- Облачные решения предпочтительны
- SQL-first команда
- Хотите минимизировать операционную нагрузку

**Когда использовать Data Mesh:**

- Крупная организация с множеством команд
- Децентрализация желательна
- Domain ownership критичен

**Example: Best Practices выбора**

```python

class ArchitectureBestPractices:
    def __init__(self):
        self.guidelines = {
            "lambda": {
                "when": ["Требуется высокая точность", "Низкая задержка для новых данных"],
                "avoid": ["Простая система", "Ограниченные ресурсы"]
            },
            "kappa": {
                "when": ["Streaming-first", "Упрощение поддержки"],
                "avoid": ["Неэффективный replay", "Требуется высокая точность batch"]
            },
            "modern_data_stack": {
                "when": ["Облачные решения", "SQL-first команда"],
                "avoid": ["On-premise требования", "Сложные трансформации"]
            },
            "data_mesh": {
                "when": ["Крупная организация", "Децентрализация"],
                "avoid": ["Малая команда", "Централизованное управление"]
            }
        }
    
    def get_recommendation(self, architecture, context):
        """Возвращает рекомендации для архитектуры"""
        if architecture not in self.guidelines:
            return None
        
        guidelines = self.guidelines[architecture]
        print(f"📋 Рекомендации для {architecture}:")
        print(f"   Используйте когда: {', '.join(guidelines['when'])}")
        print(f"   Избегайте когда: {', '.join(guidelines['avoid'])}")
        return guidelines

# Использование
practices = ArchitectureBestPractices()
practices.get_recommendation("lambda", {})
practices.get_recommendation("modern_data_stack", {})
```

**Output:**
```

📋 Рекомендации для lambda:
   Используйте когда: Требуется высокая точность, Низкая задержка для новых данных
   Избегайте когда: Простая система, Ограниченные ресурсы
📋 Рекомендации для modern_data_stack:
   Используйте когда: Облачные решения, SQL-first команда
   Избегайте когда: On-premise требования, Сложные трансформации
```

---

## 7. Data Lakehouse

Data Lakehouse объединяет преимущества Data Lake и Data Warehouse.

### 7.1 Концепция Lakehouse

**Характеристики:**

- Открытые форматы (Parquet, Delta)
- ACID транзакции
- Schema enforcement
- Прямой доступ к данным

**Преимущества:**

- Гибкость Data Lake
- Производительность Data Warehouse
- Единое хранилище для всех данных

**Example: Data Lakehouse концепция**

```python

class DataLakehouse:
    def __init__(self):
        self.storage = {}
        self.schemas = {}
        self.transactions = []
    
    def store_data(self, table_name, data, format="parquet"):
        """Сохраняет данные в lakehouse"""
        if table_name not in self.storage:
            self.storage[table_name] = []
        
        self.storage[table_name].append({
            "data": data,
            "format": format,
            "timestamp": "2024-01-01T10:00:00Z"
        })
        print(f"💾 Данные сохранены в '{table_name}' (формат: {format})")
    
    def enforce_schema(self, table_name, schema):
        """Применяет схему к таблице"""
        self.schemas[table_name] = schema
        print(f"📋 Схема применена к '{table_name}': {schema}")
    
    def query(self, table_name, sql_query):
        """Выполняет SQL запрос"""
        if table_name not in self.storage:
            return {"rows": 0}
        
        # Симуляция SQL запроса
        rows = len(self.storage[table_name])
        print(f"🔍 SQL запрос выполнен на '{table_name}': {rows} строк")
        return {"rows": rows, "data": self.storage[table_name]}

# Использование
lakehouse = DataLakehouse()

# Сохранение данных
lakehouse.store_data("users", [{"id": 1, "name": "Alice"}], format="parquet")
lakehouse.store_data("orders", [{"id": 1, "user_id": 1, "amount": 100}], format="delta")

# Применение схемы
lakehouse.enforce_schema("users", {"id": "int", "name": "string"})

# SQL запрос
result = lakehouse.query("users", "SELECT * FROM users")
```

**Output:**
```

💾 Данные сохранены в 'users' (формат: parquet)
💾 Данные сохранены в 'orders' (формат: delta)
📋 Схема применена к 'users': {'id': 'int', 'name': 'string'}
🔍 SQL запрос выполнен на 'users': 1 строк
```

### 7.2 Преимущества Lakehouse

**Единое хранилище:**

- Все данные в одном месте
- Нет дублирования
- Упрощённое управление

**Открытые форматы:**

- Совместимость с инструментами
- Vendor lock-in избежание
- Гибкость

---

## 8. Миграция между архитектурами

Переход от одной архитектуры к другой требует планирования.

### 8.1 Стратегии миграции

**Постепенная миграция:**

- Миграция компонентов по очереди
- Минимальные риски
- Долгий процесс

**Big Bang миграция:**

- Полная замена сразу
- Быстрее, но рискованнее
- Требует тщательного планирования

**Example: План миграции**

```python

class ArchitectureMigration:
    def __init__(self):
        self.migration_plan = []
        self.current_architecture = None
        self.target_architecture = None
    
    def create_migration_plan(self, from_arch, to_arch):
        """Создаёт план миграции"""
        self.current_architecture = from_arch
        self.target_architecture = to_arch
        
        if from_arch == "lambda" and to_arch == "kappa":
            self.migration_plan = [
                "1. Унифицировать логику обработки",
                "2. Настроить replay механизм",
                "3. Мигрировать batch слой в streaming",
                "4. Удалить дублирующий код"
            ]
        elif from_arch == "on_premise" and to_arch == "modern_data_stack":
            self.migration_plan = [
                "1. Выбрать облачные сервисы",
                "2. Мигрировать данные",
                "3. Настроить ELT pipeline",
                "4. Обучить команду SQL-first подходу"
            ]
        
        print(f"📋 План миграции: {from_arch} -> {to_arch}")
        for step in self.migration_plan:
            print(f"   {step}")
        
        return self.migration_plan

# Использование
migration = ArchitectureMigration()
migration.create_migration_plan("lambda", "kappa")
print("\n" + "="*50)
migration.create_migration_plan("on_premise", "modern_data_stack")
```

**Output:**
```

📋 План миграции: lambda -> kappa
   1. Унифицировать логику обработки
   2. Настроить replay механизм
   3. Мигрировать batch слой в streaming
   4. Удалить дублирующий код

==================================================
📋 План миграции: on_premise -> modern_data_stack
   1. Выбрать облачные сервисы
   2. Мигрировать данные
   3. Настроить ELT pipeline
   4. Обучить команду SQL-first подходу
```

### 8.2 Риски и вызовы

**Технические риски:**

- Потеря данных
- Простой системы
- Проблемы совместимости

**Организационные вызовы:**

- Обучение команды
- Изменение процессов
- Управление изменениями

---

## 💡 Key Takeaways

- **Lambda Architecture**: Разделение на batch и speed слои. Точные результаты из batch, низкая задержка из speed. Сложность в дублировании логики.

- **Kappa Architecture**: Единый streaming слой для всех данных. Проще в поддержке, но требует эффективного replay. Подходит для streaming-first подходов.

- **Modern Data Stack**: Облачные управляемые сервисы, SQL-first подход. Меньше операционной нагрузки, быстрое развёртывание. Популярный современный выбор.

- **Data Mesh**: Децентрализованный подход с domain ownership. Данные принадлежат доменам, самообслуживание через платформу. Для крупных организаций с множеством команд.

- **Выбор архитектуры**: Зависит от требований к точности, задержке, сложности и предпочтений (cloud vs on-premise, SQL vs code, централизация vs децентрализация).

- **Data Lakehouse**: Объединение преимуществ Data Lake и Data Warehouse. Открытые форматы, ACID транзакции, единое хранилище для всех данных.

- **Best Practices**: Правильный выбор архитектуры зависит от требований, размера команды и предпочтений. Каждая архитектура имеет свои сильные стороны.

- **Миграция**: Переход между архитектурами требует планирования. Постепенная миграция безопаснее, но дольше. Big Bang быстрее, но рискованнее.

- **Эволюция**: Архитектуры эволюционируют. Modern Data Stack становится стандартом для многих организаций благодаря простоте и управляемости. Data Mesh набирает популярность для крупных компаний. Data Lakehouse предлагает лучшее из обоих миров.

---

## 🚀 Next Steps

**Related Modules:**

- [18_Scaling_Performance](../18_Scaling_Performance/) — масштабирование и производительность
- [19_Reliability_Operations](../19_Reliability_Operations/) — надёжность и эксплуатация
- [20_Data_Engineering_System_Design](../20_Data_Engineering_System_Design/) — system design

**Practice Ideas:**

1. Спроектируйте Lambda архитектуру: batch и speed слои для вашего use case
2. Изучите Kappa архитектуру: единый streaming слой
3. Исследуйте Modern Data Stack: облачные сервисы и инструменты

**Going Deeper:**

- Изучите реальные примеры архитектур: как они используются в production
- Погрузитесь в Data Mesh: децентрализованный подход к данным
- Изучите Data Lakehouse: объединение Data Lake и Data Warehouse

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — архитектуры систем
- "Fundamentals of Data Engineering" — современный data stack

**Articles:**

- "Lambda Architecture" — детальное объяснение
- "The Modern Data Stack" — обзор инструментов

**Documentation:**

- Snowflake: https://docs.snowflake.com/
- dbt: https://docs.getdbt.com/
- Apache Airflow: https://airflow.apache.org/docs/

---



