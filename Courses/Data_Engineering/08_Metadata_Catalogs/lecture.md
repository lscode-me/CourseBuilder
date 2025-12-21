# Метаданные и каталоги данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы data modeling (модуль 04)
- Знать хранилища данных (модуль 05)
- Иметь представление о жизненном цикле данных (модуль 02)

**Recommended prior modules:**

- [04_Data_Modeling](../04_Data_Modeling/) — основы data modeling
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять роль метаданных в data-системах
- Проектировать схемы данных и управлять ими
- Использовать data catalog для discovery данных
- Отслеживать lineage данных от источников до потребления

---

## 1. Введение в метаданные

Метаданные — это "данные о данных". Они описывают структуру, происхождение, качество и использование данных. Без метаданных данные становятся бесполезными.

**Типы метаданных:**

- **Schema** — структура данных

- **Lineage** — происхождение и преобразования данных

- **Quality** — метрики качества данных

- **Usage** — кто и как использует данные

---

## 2. Schema (Схема данных)

Schema определяет структуру данных: какие поля есть, их типы, ограничения.

### 2.1 Типы схем

**Explicit Schema:**

- Схема определена заранее
- Валидация при записи
- Примеры: SQL таблицы, Avro, Parquet

**Implicit Schema:**

- Схема выводится из данных
- Валидация при чтении
- Примеры: JSON, CSV

**Example: Schema определение**

```python
# Explicit schema (Avro-подобный)
avro_schema = {
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "age", "type": ["int", "null"]}  # Optional
    ]
}

# Implicit schema (выводится из данных)
json_data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}  # age отсутствует
]

def infer_schema(data):
    """Выводит схему из данных"""
    if not data:
        return {}
    
    schema = {}
    for record in data:
        for key, value in record.items():
            if key not in schema:
                schema[key] = type(value).__name__
            elif schema[key] != type(value).__name__:
                schema[key] = "mixed"  # Разные типы
    
    return schema

print("Explicit schema (Avro):")
print(f"  {avro_schema}")

print("\nImplicit schema (выведенная):")
inferred = infer_schema(json_data)
print(f"  {inferred}")
```

**Output:**
```

Explicit schema (Avro):
  {'type': 'record', 'name': 'User', 'fields': [{'name': 'id', 'type': 'int'}, {'name': 'name', 'type': 'string'}, {'name': 'email', 'type': 'string'}, {'name': 'age', 'type': ['int', 'null']}]}

Implicit schema (выведенная):
  {'id': 'int', 'name': 'str', 'email': 'str', 'age': 'int'}
```

### 2.2 Schema Evolution

Schema evolution — это изменение схемы со временем при сохранении совместимости.

**Типы изменений:**

- **Backward compatible**: Старый код читает новые данные

- **Forward compatible**: Новый код читает старые данные

- **Breaking changes**: Несовместимые изменения

**Example: Schema Evolution**

```python
# Версия 1 схемы
schema_v1 = {
    "id": "int",
    "name": "string",
    "email": "string"
}

# Версия 2: добавлено поле (backward compatible)
schema_v2 = {
    "id": "int",
    "name": "string",
    "email": "string",
    "age": "int?"  # Optional, backward compatible
}

# Версия 3: удалено поле (forward compatible если optional)
schema_v3 = {
    "id": "int",
    "name": "string",
    "age": "int"
}

def check_compatibility(old_schema, new_schema):
    """Проверяет совместимость схем"""
    # Упрощённая проверка
    old_fields = set(old_schema.keys())
    new_fields = set(new_schema.keys())
    
    removed = old_fields - new_fields
    added = new_fields - old_fields
    
    backward_compatible = len(removed) == 0  # Не удаляем поля
    forward_compatible = all(f in old_schema for f in new_fields)  # Новые поля optional
    
    return {
        "backward_compatible": backward_compatible,
        "forward_compatible": forward_compatible,
        "removed_fields": removed,
        "added_fields": added
    }

# Проверка совместимости

compat = check_compatibility(schema_v1, schema_v2)
print("Schema v1 -> v2:")
print(f"  Backward compatible: {compat['backward_compatible']}")
print(f"  Forward compatible: {compat['forward_compatible']}")
print(f"  Added fields: {compat['added_fields']}")
```

**Output:**
```

Schema v1 -> v2:
  Backward compatible: True
  Forward compatible: False
  Added fields: {'age'}
```

---

## 3. Data Catalog (Каталог данных)

Data Catalog — это централизованный реестр метаданных о данных в организации.

### 3.1 Компоненты Data Catalog

**Метаданные:**

- Схемы таблиц и полей
- Описания и документация
- Теги и категории

**Lineage:**

- Откуда пришли данные
- Какие трансформации применены
- Куда данные используются

**Quality:**

- Метрики качества
- Профилирование данных
- Валидация

**Example: Data Catalog**

```python

class DataCatalog:
    def __init__(self):
        self.tables = {}
        self.lineage = {}
    
    def register_table(self, name, schema, description, owner):
        """Регистрирует таблицу в каталоге"""
        self.tables[name] = {
            "schema": schema,
            "description": description,
            "owner": owner,
            "tags": [],
            "last_updated": "2024-01-01"
        }
        print(f"✅ Таблица '{name}' зарегистрирована в каталоге")
    
    def add_lineage(self, table, sources, transformations):
        """Добавляет lineage информацию"""
        self.lineage[table] = {
            "sources": sources,
            "transformations": transformations,
            "downstream": []
        }
        print(f"✅ Lineage для '{table}' добавлен")
    
    def search(self, query):
        """Поиск в каталоге"""
        results = []
        for name, info in self.tables.items():
            if (query.lower() in name.lower() or 
                query.lower() in info["description"].lower()):
                results.append(name)
        return results
    
    def get_table_info(self, name):
        """Получает информацию о таблице"""
        if name not in self.tables:
            return None
        
        info = self.tables[name].copy()
        if name in self.lineage:
            info["lineage"] = self.lineage[name]
        return info

# Использование
catalog = DataCatalog()

# Регистрация таблиц
catalog.register_table(
    "users",
    {"id": "int", "name": "string", "email": "string"},
    "Таблица пользователей системы",
    "data_team"
)

catalog.register_table(
    "orders",
    {"order_id": "int", "user_id": "int", "amount": "decimal"},
    "Таблица заказов пользователей",
    "data_team"
)

# Lineage
catalog.add_lineage(
    "orders",
    sources=["raw_orders_api", "users"],
    transformations=["clean", "join", "enrich"]
)

# Поиск

results = catalog.search("user")
print(f"\nПоиск 'user': {results}")

# Информация о таблице
info = catalog.get_table_info("orders")
print(f"\nИнформация о 'orders':")
print(f"  Описание: {info['description']}")
print(f"  Lineage sources: {info['lineage']['sources']}")
```

**Output:**
```

✅ Таблица 'users' зарегистрирована в каталоге
✅ Таблица 'orders' зарегистрирована в каталоге
✅ Lineage для 'orders' добавлен

Поиск 'user': ['users']

Информация о 'orders':
  Описание: Таблица заказов пользователей
  Lineage sources: ['raw_orders_api', 'users']
```

### 3.2 Преимущества Data Catalog

**Discovery:**

- Поиск данных по описанию
- Понимание что доступно
- Нахождение нужных данных

**Governance:**

- Контроль доступа
- Документация
- Compliance

**Collaboration:**

- Общие знания о данных
- Документация от пользователей
- Рейтинги и отзывы

---

## 4. Lineage (Происхождение данных)

Lineage отслеживает происхождение данных: откуда они пришли, какие трансформации прошли, куда используются.

### 4.1 Типы Lineage

**Upstream Lineage:**

- Откуда пришли данные
- Источники данных
- Предыдущие трансформации

**Downstream Lineage:**

- Куда используются данные
- Зависимые таблицы
- Потребители данных

**Example: Lineage отслеживание**

```python

class LineageTracker:
    def __init__(self):
        self.lineage_graph = {}
    
    def add_transformation(self, output_table, input_tables, transformation):
        """Добавляет информацию о трансформации"""
        if output_table not in self.lineage_graph:
            self.lineage_graph[output_table] = {
                "inputs": [],
                "transformations": [],
                "outputs": []
            }
        
        self.lineage_graph[output_table]["inputs"].extend(input_tables)
        self.lineage_graph[output_table]["transformations"].append(transformation)
        
        # Обновляем downstream для input таблиц
        for input_table in input_tables:
            if input_table not in self.lineage_graph:
                self.lineage_graph[input_table] = {
                    "inputs": [],
                    "transformations": [],
                    "outputs": []
                }
            self.lineage_graph[input_table]["outputs"].append(output_table)
        
        print(f"✅ Lineage обновлён: {input_tables} -> {output_table}")
    
    def get_upstream(self, table):
        """Получает upstream lineage"""
        if table not in self.lineage_graph:
            return []
        
        upstream = []
        for input_table in self.lineage_graph[table]["inputs"]:
            upstream.append(input_table)
            upstream.extend(self.get_upstream(input_table))  # Рекурсивно
        
        return list(set(upstream))  # Уникальные
    
    def get_downstream(self, table):
        """Получает downstream lineage"""
        if table not in self.lineage_graph:
            return []
        
        return self.lineage_graph[table]["outputs"]

# Использование

tracker = LineageTracker()

# Построение lineage
tracker.add_transformation("cleaned_users", ["raw_users_api"], "clean")
tracker.add_transformation("user_profiles", ["cleaned_users"], "enrich")
tracker.add_transformation("analytics_users", ["user_profiles", "orders"], "join")

# Upstream для analytics_users
upstream = tracker.get_upstream("analytics_users")
print(f"\nUpstream для 'analytics_users': {upstream}")

# Downstream для cleaned_users

downstream = tracker.get_downstream("cleaned_users")
print(f"Downstream для 'cleaned_users': {downstream}")
```

**Output:**
```

✅ Lineage обновлён: ['raw_users_api'] -> cleaned_users
✅ Lineage обновлён: ['cleaned_users'] -> user_profiles
✅ Lineage обновлён: ['user_profiles', 'orders'] -> analytics_users

Upstream для 'analytics_users': ['user_profiles', 'cleaned_users', 'raw_users_api', 'orders']
Downstream для 'cleaned_users': ['user_profiles']
```

### 4.2 Использование Lineage

**Impact Analysis:**

- Что сломается при изменении источника
- Какие таблицы зависят от данных

**Debugging:**

- Отслеживание проблем до источника
- Понимание трансформаций

**Documentation:**

- Автоматическая документация потока данных
- Визуализация зависимостей

---

## 5. Data Discovery (Поиск данных)

Data Discovery — это процесс поиска и понимания доступных данных.

### 5.1 Методы Discovery

**Поиск по метаданным:**

- Название таблицы
- Описание
- Теги и категории

**Поиск по содержимому:**

- Полнотекстовый поиск
- Профилирование данных
- Семантический поиск

**Example: Data Discovery**

```python

class DataDiscovery:
    def __init__(self, catalog):
        self.catalog = catalog
        self.search_index = {}
    
    def index_table(self, table_name, metadata):
        """Индексирует таблицу для поиска"""
        # Простая индексация
        keywords = (
            table_name + " " + 
            metadata.get("description", "") + " " +
            " ".join(metadata.get("tags", []))
        ).lower()
        
        self.search_index[table_name] = {
            "keywords": keywords,
            "metadata": metadata
        }
    
    def search(self, query):
        """Поиск по индексу"""
        query_lower = query.lower()
        results = []
        
        for table_name, index_data in self.search_index.items():
            if query_lower in index_data["keywords"]:
                results.append({
                    "table": table_name,
                    "description": index_data["metadata"].get("description"),
                    "relevance": index_data["keywords"].count(query_lower)
                })
        
        # Сортировка по релевантности
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results

# Использование

discovery = DataDiscovery(catalog)

# Индексация
discovery.index_table("users", {
    "description": "Таблица пользователей системы",
    "tags": ["user", "profile", "authentication"]
})

discovery.index_table("orders", {
    "description": "Таблица заказов пользователей",
    "tags": ["order", "transaction", "ecommerce"]
})

# Поиск

results = discovery.search("user")
print("\nРезультаты поиска 'user':")
for result in results:
    print(f"  {result['table']}: {result['description']}")
```

**Output:**
```

Результаты поиска 'user':
  users: Таблица пользователей системы
  orders: Таблица заказов пользователей
```

---

## 6. Управление метаданными

Эффективное управление метаданными критично для успешной data-платформы.

### 6.1 Best Practices

**Документация:**

- Описывать все таблицы и поля
- Обновлять документацию при изменениях
- Использовать стандартизированные описания

**Lineage:**

- Автоматически отслеживать lineage
- Визуализировать зависимости
- Использовать для impact analysis

**Governance:**

- Контролировать доступ к метаданным
- Тегировать данные (PII, sensitive)
- Управлять жизненным циклом метаданных

**Example: Управление метаданными**

```python

class MetadataManager:
    def __init__(self):
        self.metadata = {}
        self.policies = {}
    
    def add_metadata(self, table, metadata):
        """Добавляет метаданные с валидацией"""
        required_fields = ["description", "owner", "schema"]
        if not all(field in metadata for field in required_fields):
            raise ValueError(f"Отсутствуют обязательные поля: {required_fields}")
        
        self.metadata[table] = {
            **metadata,
            "created_at": "2024-01-01",
            "updated_at": "2024-01-01",
            "version": 1
        }
        print(f"✅ Метаданные для '{table}' добавлены")
    
    def tag_data(self, table, tags):
        """Тегирует данные"""
        if table not in self.metadata:
            raise ValueError(f"Таблица {table} не найдена")
        
        if "tags" not in self.metadata[table]:
            self.metadata[table]["tags"] = []
        
        self.metadata[table]["tags"].extend(tags)
        print(f"✅ Теги добавлены к '{table}': {tags}")
    
    def apply_policy(self, table, policy_name):
        """Применяет политику к данным"""
        if table not in self.metadata:
            raise ValueError(f"Таблица {table} не найдена")
        
        policy = self.policies.get(policy_name)
        if not policy:
            raise ValueError(f"Политика {policy_name} не найдена")
        
        self.metadata[table]["policy"] = policy_name
        print(f"✅ Политика '{policy_name}' применена к '{table}'")

# Использование

manager = MetadataManager()

# Добавление метаданных

manager.add_metadata("users", {
    "description": "Таблица пользователей",
    "owner": "data_team",
    "schema": {"id": "int", "name": "string"}
})

# Тегирование

manager.tag_data("users", ["PII", "sensitive"])

# Политики

manager.policies["retention_1year"] = {"retention_days": 365}
manager.apply_policy("users", "retention_1year")
```

**Output:**
```

✅ Метаданные для 'users' добавлены
✅ Теги добавлены к 'users': ['PII', 'sensitive']
✅ Политика 'retention_1year' применена к 'users'
```

---

## 💡 Key Takeaways

- **Метаданные критичны**: Без метаданных данные становятся бесполезными. Schema, lineage, quality — всё это метаданные.

- **Data Catalog**: Централизованный реестр метаданных помогает находить, понимать и использовать данные. Критичен для больших организаций.

- **Lineage**: Отслеживание происхождения данных помогает в debugging, impact analysis и документации. Автоматизация lineage важна.

- **Schema Evolution**: Схемы меняются со временем. Важно поддерживать совместимость (backward/forward) для стабильности систем.

- **Data Discovery**: Поиск данных должен быть простым. Индексация метаданных, теги, описания — всё это помогает находить нужные данные.

---

## 🚀 Next Steps

**Related Modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing и ETL
- [11_Data_Quality](../11_Data_Quality/) — качество данных
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных

**Practice Ideas:**

1. Создайте простой data catalog для вашего проекта: задокументируйте таблицы и их схемы
2. Отследите lineage для ваших данных: откуда приходят, какие трансформации проходят
3. Проанализируйте schema evolution: как менялись ваши схемы со временем

**Going Deeper:**

- Изучите инструменты data catalog: Apache Atlas, DataHub, Collibra
- Погрузитесь в автоматическое отслеживание lineage: как инструменты это делают
- Изучите data governance: политики, контроль доступа, compliance

---

## 📚 Additional Resources

**Books:**

- "The Data Catalog" by Bonnie O'Neil — практическое руководство по data catalog
- "Data Governance" by John Ladley — управление данными

**Articles:**

- "What is Data Lineage?" — объяснение lineage
- "Data Catalog Best Practices" — рекомендации

**Documentation:**

- Apache Atlas: https://atlas.apache.org/
- DataHub: https://datahubproject.io/
- Great Expectations: https://greatexpectations.io/ (data quality)

---


