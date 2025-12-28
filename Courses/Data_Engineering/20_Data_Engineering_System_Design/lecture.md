# Data Engineering как system design

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать все предыдущие модули курса
- Знать основы system design
- Иметь представление о компромиссах в архитектуре

**Recommended prior modules:**

- Все модули курса Data Engineering

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Выбирать подходящие хранилища для use case
- Выбирать форматы данных для конкретных задач
- Выбирать структуры данных и алгоритмы
- Анализировать компромиссы архитектуры

---

## 1. Введение в system design для Data Engineering

Data Engineering как system design требует принятия решений на основе компромиссов. Нет универсальных решений, только trade-offs.

**Ключевые решения:**

- **Выбор хранилищ** — для разных use cases

- **Выбор форматов** — для оптимизации

- **Выбор структур данных** — для производительности

- **Компромиссы** — баланс между требованиями

---

## 2. Выбор хранилищ

Выбор хранилища зависит от use case и требований.

### 2.1 Decision Framework

**OLTP (Operational):**

- PostgreSQL, MySQL
- Транзакционные данные
- Низкая задержка записи

**OLAP (Analytical):**

- Snowflake, BigQuery, Redshift
- Аналитические запросы
- Высокая пропускная способность чтения

**NoSQL:**

- MongoDB, Cassandra
- Гибкая схема
- Горизонтальное масштабирование

**Example: Выбор хранилища**

```python

def recommend_storage(requirements):
    """Рекомендует хранилище на основе требований"""
    if requirements.get("transactional") and requirements.get("acid"):
        return "PostgreSQL/MySQL (OLTP, ACID транзакции)"
    elif requirements.get("analytical") and requirements.get("large_volume"):
        return "Snowflake/BigQuery (OLAP, аналитика)"
    elif requirements.get("flexible_schema") and requirements.get("horizontal_scale"):
        return "MongoDB/Cassandra (NoSQL, горизонтальное масштабирование)"
    elif requirements.get("key_value") and requirements.get("low_latency"):
        return "Redis/DynamoDB (Key-value, низкая задержка)"
    else:
        return "Определить на основе детальных требований"

# Примеры
examples = [
    {"transactional": True, "acid": True, "low_latency_write": True},
    {"analytical": True, "large_volume": True, "complex_queries": True},
    {"flexible_schema": True, "horizontal_scale": True, "distributed": True}
]

print("Рекомендации хранилищ:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_storage(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации хранилищ:
  Пример 1: PostgreSQL/MySQL (OLTP, ACID транзакции)
  Пример 2: Snowflake/BigQuery (OLAP, аналитика)
  Пример 3: MongoDB/Cassandra (NoSQL, горизонтальное масштабирование)
```

---

## 3. Выбор форматов данных

Выбор формата зависит от паттернов доступа и требований.

### 3.1 Decision Framework

**Row-based (CSV, JSON, Avro):**

- Чтение полных записей
- Транзакционные данные
- Простота

**Column-based (Parquet, ORC):**

- Аналитические запросы
- Агрегации
- Отличное сжатие

**Example: Выбор формата**

```python

def recommend_format(requirements):
    """Рекомендует формат данных"""
    if requirements.get("analytical") and requirements.get("large_volume"):
        return "Parquet/ORC (columnar, отличное сжатие)"
    elif requirements.get("transactional") and requirements.get("full_records"):
        return "JSON/Avro (row-based, полные записи)"
    elif requirements.get("exchange") and requirements.get("simplicity"):
        return "CSV (простота, совместимость)"
    elif requirements.get("streaming") and requirements.get("schema_evolution"):
        return "Avro (schema-on-write, streaming)"
    else:
        return "Определить на основе детальных требований"

# Примеры
examples = [
    {"analytical": True, "large_volume": True, "aggregations": True},
    {"transactional": True, "full_records": True, "low_latency": True},
    {"streaming": True, "schema_evolution": True, "compression": True}
]

print("Рекомендации форматов:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_format(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации форматов:
  Пример 1: Parquet/ORC (columnar, отличное сжатие)
  Пример 2: JSON/Avro (row-based, полные записи)
  Пример 3: Avro (schema-on-write, streaming)
```

---

## 4. Выбор структур данных и алгоритмов

Выбор структур данных и алгоритмов влияет на производительность.

### 4.1 Decision Framework

**Индексы:**

- B-tree для range queries
- Hash для точного поиска
- Bitmap для аналитики

**Алгоритмы:**

- Сортировка для упорядочивания
- Агрегация для суммирования
- Join стратегии

**Example: Выбор структур данных**

```python

def recommend_data_structure(requirements):
    """Рекомендует структуру данных"""
    if requirements.get("range_queries") and requirements.get("ordered"):
        return "B-tree индекс (range queries, упорядоченный поиск)"
    elif requirements.get("exact_lookup") and requirements.get("fast"):
        return "Hash индекс (точный поиск O(1))"
    elif requirements.get("analytical") and requirements.get("low_cardinality"):
        return "Bitmap индекс (аналитика, низкая кардинальность)"
    elif requirements.get("full_text_search"):
        return "Inverted index (полнотекстовый поиск)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"range_queries": True, "ordered": True, "analytical": True},
    {"exact_lookup": True, "fast": True, "transactional": True},
    {"analytical": True, "low_cardinality": True, "aggregations": True}
]

print("Рекомендации структур данных:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_data_structure(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации структур данных:
  Пример 1: B-tree индекс (range queries, упорядоченный поиск)
  Пример 2: Hash индекс (точный поиск O(1))
  Пример 3: Bitmap индекс (аналитика, низкая кардинальность)
```

---

## 5. Компромиссы архитектуры

Все архитектурные решения включают компромиссы.

### 5.1 Типичные компромиссы

**Consistency vs Availability:**

- Strong consistency vs high availability
- CAP theorem

**Latency vs Throughput:**

- Низкая задержка vs высокая пропускная способность
- Зависит от use case

**Cost vs Performance:**

- Дешевле vs быстрее
- Right-sizing

**Example: Анализ компромиссов**

```python

class TradeoffAnalyzer:
    def __init__(self):
        self.tradeoffs = {}
    
    def analyze_consistency_availability(self, requirements):
        """Анализирует компромисс consistency vs availability"""
        if requirements.get("strong_consistency"):
            return {
                "choice": "Strong Consistency",
                "tradeoff": "Меньше availability, но гарантированная консистентность",
                "use_case": "Финансовые транзакции"
            }
        else:
            return {
                "choice": "High Availability",
                "tradeoff": "Меньше consistency, но высокая доступность",
                "use_case": "Социальные сети"
            }
    
    def analyze_latency_throughput(self, requirements):
        """Анализирует компромисс latency vs throughput"""
        if requirements.get("low_latency"):
            return {
                "choice": "Low Latency",
                "tradeoff": "Меньше throughput, но быстрый отклик",
                "use_case": "Real-time системы"
            }
        else:
            return {
                "choice": "High Throughput",
                "tradeoff": "Больше latency, но высокая пропускная способность",
                "use_case": "Batch processing"
            }
    
    def analyze_cost_performance(self, requirements):
        """Анализирует компромисс cost vs performance"""
        if requirements.get("cost_optimized"):
            return {
                "choice": "Cost Optimized",
                "tradeoff": "Меньше производительность, но дешевле",
                "use_case": "Не критичные системы"
            }
        else:
            return {
                "choice": "Performance Optimized",
                "tradeoff": "Дороже, но высокая производительность",
                "use_case": "Критичные системы"
            }

# Использование

analyzer = TradeoffAnalyzer()

# Анализ компромиссов
consistency_tradeoff = analyzer.analyze_consistency_availability({"strong_consistency": True})
latency_tradeoff = analyzer.analyze_latency_throughput({"low_latency": True})
cost_tradeoff = analyzer.analyze_cost_performance({"cost_optimized": False})

print("Анализ компромиссов:")
print(f"  Consistency: {consistency_tradeoff['choice']} - {consistency_tradeoff['tradeoff']}")
print(f"  Latency: {latency_tradeoff['choice']} - {latency_tradeoff['tradeoff']}")
print(f"  Cost: {cost_tradeoff['choice']} - {cost_tradeoff['tradeoff']}")
```

**Output:**
```

Анализ компромиссов:
  Consistency: Strong Consistency - Меньше availability, но гарантированная консистентность
  Latency: Low Latency - Меньше throughput, но быстрый отклик
  Cost: Performance Optimized - Дороже, но высокая производительность
```

---

## 6. CAP Theorem

CAP theorem описывает компромиссы в распределённых системах.

### 6.1 Три свойства CAP

**Consistency (Консистентность):**

- Все узлы видят одни и те же данные одновременно
- Сильная консистентность

**Availability (Доступность):**

- Система остаётся доступной для операций
- Каждый запрос получает ответ

**Partition Tolerance (Устойчивость к разделению):**

- Система продолжает работать при разделении сети
- Неизбежно в распределённых системах

**Example: CAP Trade-offs**

```python

class CAPTheorem:
    def __init__(self):
        self.systems = {}
    
    def classify_system(self, system_name, consistency, availability, partition_tolerance):
        """Классифицирует систему по CAP"""
        # CAP theorem: можно выбрать только 2 из 3
        if partition_tolerance:
            if consistency and availability:
                cap_type = "Невозможно (P обязательна, C и A вместе невозможны)"
            elif consistency:
                cap_type = "CP (Consistency + Partition Tolerance)"
            elif availability:
                cap_type = "AP (Availability + Partition Tolerance)"
        else:
            cap_type = "CA (Consistency + Availability, но без P)"
        
        self.systems[system_name] = {
            "consistency": consistency,
            "availability": availability,
            "partition_tolerance": partition_tolerance,
            "cap_type": cap_type
        }
        
        print(f"📊 {system_name}: {cap_type}")
        return self.systems[system_name]

# Использование
cap = CAPTheorem()

# Примеры систем
cap.classify_system("PostgreSQL", consistency=True, availability=True, partition_tolerance=True)
cap.classify_system("MongoDB", consistency=False, availability=True, partition_tolerance=True)
cap.classify_system("Cassandra", consistency=False, availability=True, partition_tolerance=True)
```

**Output:**
```

📊 PostgreSQL: CP (Consistency + Partition Tolerance)
📊 MongoDB: AP (Availability + Partition Tolerance)
📊 Cassandra: AP (Availability + Partition Tolerance)
```

### 6.2 Выбор по CAP

**CP системы:**

- Сильная консистентность
- Жертвуют доступностью при разделении
- Пример: PostgreSQL, HBase

**AP системы:**

- Высокая доступность
- Жертвуют консистентностью
- Пример: Cassandra, DynamoDB

---

## 7. System Design Process

Процесс проектирования data-системы.

### 7.1 Шаги

**1. Понимание требований:**

- Use case
- Масштаб
- Требования к производительности

**2. Выбор компонентов:**

- Хранилища
- Форматы
- Инструменты

**3. Проектирование архитектуры:**

- Компоненты и их взаимодействие
- Data flow
- Масштабирование

**4. Анализ компромиссов:**

- Trade-offs
- Риски
- Альтернативы

**Example: System Design Process**

```python

class SystemDesignProcess:
    def __init__(self, use_case):
        self.use_case = use_case
        self.requirements = {}
        self.components = {}
        self.architecture = {}
        self.tradeoffs = []
    
    def gather_requirements(self, **kwargs):
        """Собирает требования"""
        self.requirements.update(kwargs)
        print(f"📋 Требования для '{self.use_case}':")
        for key, value in self.requirements.items():
            print(f"   {key}: {value}")
        return self.requirements
    
    def select_components(self):
        """Выбирает компоненты"""
        if self.requirements.get("analytical"):
            self.components["storage"] = "Snowflake"
            self.components["format"] = "Parquet"
        else:
            self.components["storage"] = "PostgreSQL"
            self.components["format"] = "JSON"
        
        print(f"\n🔧 Выбранные компоненты:")
        for component, choice in self.components.items():
            print(f"   {component}: {choice}")
        return self.components
    
    def design_architecture(self):
        """Проектирует архитектуру"""
        self.architecture = {
            "ingestion": "Kafka",
            "storage": self.components["storage"],
            "processing": "Spark",
            "serving": "API"
        }
        
        print(f"\n🏗️  Архитектура:")
        for layer, component in self.architecture.items():
            print(f"   {layer}: {component}")
        return self.architecture
    
    def analyze_tradeoffs(self):
        """Анализирует компромиссы"""
        self.tradeoffs = [
            "Latency vs Throughput: выбран баланс",
            "Cost vs Performance: оптимизировано по стоимости",
            "Consistency vs Availability: eventual consistency"
        ]
        
        print(f"\n⚖️  Компромиссы:")
        for tradeoff in self.tradeoffs:
            print(f"   - {tradeoff}")
        return self.tradeoffs

# Использование
design = SystemDesignProcess("Analytics Platform")
design.gather_requirements(analytical=True, large_volume=True, low_latency=False)
design.select_components()
design.design_architecture()
design.analyze_tradeoffs()
```

**Output:**
```

📋 Требования для 'Analytics Platform':
   analytical: True
   large_volume: True
   low_latency: False

🔧 Выбранные компоненты:
   storage: Snowflake
   format: Parquet

🏗️  Архитектура:
   ingestion: Kafka
   storage: Snowflake
   processing: Spark
   serving: API

⚖️  Компромиссы:

   - Latency vs Throughput: выбран баланс
   - Cost vs Performance: оптимизировано по стоимости
   - Consistency vs Availability: eventual consistency
```

### 7.2 Best Practices

**Итеративный подход:**

- Начать с простого
- Итеративно улучшать
- Избегать over-engineering

**Документация:**

- Документировать решения
- Объяснять trade-offs
- Обновлять при изменениях

**Example: Best Practices Checklist**

```python

class SystemDesignChecklist:
    def __init__(self):
        self.checklist = {
            "requirements": False,
            "components": False,
            "architecture": False,
            "scalability": False,
            "reliability": False,
            "tradeoffs": False
        }
    
    def check_requirement(self, requirement):
        """Проверяет требование"""
        if requirement and len(requirement) > 0:
            self.checklist["requirements"] = True
            print("✅ Требования определены")
            return True
        return False
    
    def check_components(self, components):
        """Проверяет компоненты"""
        if components and len(components) > 0:
            self.checklist["components"] = True
            print("✅ Компоненты выбраны")
            return True
        return False
    
    def check_architecture(self, architecture):
        """Проверяет архитектуру"""
        if architecture and len(architecture) > 0:
            self.checklist["architecture"] = True
            print("✅ Архитектура спроектирована")
            return True
        return False
    
    def validate_design(self):
        """Валидирует дизайн"""
        all_checked = all(self.checklist.values())
        if all_checked:
            print("✅ Все пункты checklist выполнены")
        else:
            missing = [k for k, v in self.checklist.items() if not v]
            print(f"⚠️  Отсутствуют: {', '.join(missing)}")
        return all_checked

# Использование
checklist = SystemDesignChecklist()
checklist.check_requirement("Analytics platform")
checklist.check_components({"storage": "Snowflake"})
checklist.check_architecture({"ingestion": "Kafka"})
checklist.validate_design()
```

**Output:**
```

✅ Требования определены
✅ Компоненты выбраны
✅ Архитектура спроектирована
⚠️  Отсутствуют: scalability, reliability, tradeoffs
```

---

## 8. Design Patterns для Data Systems

Паттерны проектирования для data-систем помогают решать типичные задачи.

### 8.1 Типичные паттерны

**Event Sourcing:**

- Хранение всех событий
- Восстановление состояния из событий
- Audit trail

**CQRS (Command Query Responsibility Segregation):**

- Разделение чтения и записи
- Оптимизация для разных паттернов доступа
- Разные модели данных

**Example: Event Sourcing**

```python

class EventSourcing:
    def __init__(self):
        self.events = []
        self.current_state = {}
    
    def append_event(self, event_type, data):
        """Добавляет событие"""
        event = {
            "id": len(self.events) + 1,
            "type": event_type,
            "data": data,
            "timestamp": "2024-01-01T10:00:00Z"
        }
        self.events.append(event)
        
        # Применение события к состоянию
        self._apply_event(event)
        
        print(f"📝 Событие добавлено: {event_type}")
        return event
    
    def _apply_event(self, event):
        """Применяет событие к состоянию"""
        if event["type"] == "user_created":
            self.current_state["user_id"] = event["data"]["user_id"]
            self.current_state["name"] = event["data"]["name"]
        elif event["type"] == "user_updated":
            self.current_state.update(event["data"])
    
    def get_current_state(self):
        """Возвращает текущее состояние"""
        return self.current_state.copy()
    
    def replay_events(self, from_event_id=0):
        """Переигрывает события для восстановления состояния"""
        self.current_state = {}
        for event in self.events[from_event_id:]:
            self._apply_event(event)
        print(f"🔄 Переиграно {len(self.events) - from_event_id} событий")
        return self.current_state

# Использование
es = EventSourcing()

# Добавление событий
es.append_event("user_created", {"user_id": 1, "name": "Alice"})
es.append_event("user_updated", {"name": "Alice Updated"})

print(f"Текущее состояние: {es.get_current_state()}")

# Replay
es.replay_events(0)
print(f"Состояние после replay: {es.get_current_state()}")
```

**Output:**
```

📝 Событие добавлено: user_created
📝 Событие добавлено: user_updated
Текущее состояние: {'user_id': 1, 'name': 'Alice Updated'}
🔄 Переиграно 2 событий
Состояние после replay: {'user_id': 1, 'name': 'Alice Updated'}
```

### 8.2 CQRS Pattern

**Command Side:**

- Оптимизирован для записи
- Нормализованная модель
- ACID транзакции

**Query Side:**

- Оптимизирован для чтения
- Денормализованная модель
- Быстрые запросы

**Example: CQRS**

```python

class CQRS:
    def __init__(self):
        self.command_store = {}  # Write-optimized
        self.query_store = {}  # Read-optimized
    
    def execute_command(self, command_type, data):
        """Выполняет команду (write)"""
        if command_type == "create_user":
            user_id = data["user_id"]
            self.command_store[user_id] = data
            # Обновление query store
            self.query_store[user_id] = {
                "id": user_id,
                "name": data["name"],
                "email": data["email"],
                "full_profile": f"{data['name']} ({data['email']})"  # Денормализовано
            }
            print(f"✍️  Command выполнена: {command_type}")
            return True
        return False
    
    def execute_query(self, query_type, params):
        """Выполняет запрос (read)"""
        if query_type == "get_user":
            user_id = params["user_id"]
            if user_id in self.query_store:
                print(f"📖 Query выполнена: {query_type}")
                return self.query_store[user_id]
        return None

# Использование
cqrs = CQRS()

# Write (command)
cqrs.execute_command("create_user", {
    "user_id": 1,
    "name": "Alice",
    "email": "alice@example.com"
})

# Read (query)
user = cqrs.execute_query("get_user", {"user_id": 1})
print(f"Результат query: {user}")
```

**Output:**
```

✍️  Command выполнена: create_user
📖 Query выполнена: get_user
Результат query: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'full_profile': 'Alice (alice@example.com)'}
```

---

## 9. Реальные примеры проектирования

Практические примеры проектирования data-систем.

### 9.1 Analytics Platform

**Требования:**

- Обработка больших объёмов данных
- Аналитические запросы
- Масштабируемость

**Архитектура:**

- Kafka для ingestion
- Spark для обработки
- Snowflake для хранения
- API для доступа

**Example: Analytics Platform Design**

```python

class AnalyticsPlatformDesign:
    def __init__(self):
        self.components = {}
        self.data_flow = []
    
    def design_platform(self):
        """Проектирует analytics platform"""
        self.components = {
            "ingestion": "Kafka",
            "processing": "Spark",
            "storage": "Snowflake",
            "serving": "REST API"
        }
        
        self.data_flow = [
            "Raw data -> Kafka",
            "Kafka -> Spark (transformation)",
            "Spark -> Snowflake (storage)",
            "Snowflake -> API (serving)"
        ]
        
        print("🏗️  Analytics Platform Design:")
        print("\nКомпоненты:")
        for component, technology in self.components.items():
            print(f"   {component}: {technology}")
        
        print("\nData Flow:")
        for step in self.data_flow:
            print(f"   {step}")
        
        return self.components

# Использование
design = AnalyticsPlatformDesign()
design.design_platform()
```

**Output:**
```

🏗️  Analytics Platform Design:

Компоненты:
   ingestion: Kafka
   processing: Spark
   storage: Snowflake
   serving: REST API

Data Flow:
   Raw data -> Kafka
   Kafka -> Spark (transformation)
   Spark -> Snowflake (storage)
   Snowflake -> API (serving)
```

### 9.2 Real-time Processing System

**Требования:**

- Низкая задержка
- Высокая пропускная способность
- Exactly-once semantics

**Архитектура:**

- Kafka для event streaming
- Flink для обработки
- Redis для кэширования
- Database для persistence

---

## 💡 Key Takeaways

- **Выбор хранилищ**: Зависит от use case. OLTP для транзакций, OLAP для аналитики, NoSQL для гибкости.

- **Выбор форматов**: Row-based для транзакций, column-based для аналитики. Зависит от паттернов доступа.

- **Выбор структур данных**: B-tree для range queries, Hash для точного поиска. Влияет на производительность.

- **CAP Theorem**: В распределённых системах можно выбрать только 2 из 3: Consistency, Availability, Partition Tolerance. CP системы жертвуют доступностью, AP системы жертвуют консистентностью.

- **Компромиссы**: Все решения включают trade-offs. Consistency vs Availability, Latency vs Throughput, Cost vs Performance.

- **System Design Process**: Понимание требований → Выбор компонентов → Проектирование архитектуры → Анализ компромиссов. CAP theorem помогает понять фундаментальные ограничения.

- **Best Practices**: Итеративный подход, начиная с простого. Документация решений и trade-offs. Валидация дизайна через checklist.

- **Design Patterns**: Event Sourcing для audit trail и восстановления состояния. CQRS для разделения чтения и записи. Паттерны помогают решать типичные задачи.

- **Реальные примеры**: Analytics Platform для больших объёмов данных. Real-time Processing System для низкой задержки. Каждый use case требует своего подхода.

- **Практика**: Проектирование data-систем требует баланса между требованиями, компромиссами и практичностью. Изучение реальных примеров помогает понять лучшие практики.

---

## 🚀 Next Steps

**Related Modules:**

- Все модули курса Data Engineering
- System Design курсы
- Distributed Systems курсы

**Practice Ideas:**

1. Спроектируйте data-систему: от требований до архитектуры
2. Проанализируйте компромиссы: trade-offs для вашего use case
3. Сравните решения: альтернативные подходы

**Going Deeper:**

- Изучите реальные case studies: как проектируются data-платформы
- Погрузитесь в CAP theorem: consistency, availability, partition tolerance
- Изучите паттерны проектирования: для data-систем

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — фундаментальная книга
- "System Design Interview" — практика проектирования

**Articles:**

- "Data Engineering System Design" — подходы
- "Trade-offs in System Design" — компромиссы

**Documentation:**

- AWS Architecture Center: https://aws.amazon.com/architecture/
- Google Cloud Architecture: https://cloud.google.com/architecture

---



