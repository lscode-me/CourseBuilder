# Основы data modeling

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать типы данных (модуль 03)
- Знать основы реляционных баз данных
- Иметь представление о SQL и таблицах

**Recommended prior modules:**

- [03_Data_Types](../03_Data_Types/) — типы данных
- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать Entity-Relationship модели для проектирования баз данных
- Применять нормализацию для устранения избыточности данных
- Понимать когда использовать денормализацию
- Анализировать trade-offs между нормализацией и денормализацией

---

## 1. Введение в data modeling

Data modeling — это процесс проектирования структуры данных для эффективного хранения и доступа. Правильное моделирование критично для производительности, целостности данных и масштабируемости системы.

**Основные концепции:**

- Entity-Relationship модели для представления структуры
- Нормализация для устранения избыточности
- Денормализация для оптимизации запросов
- Trade-offs между различными подходами

---

## 2. Entity-Relationship (ER) модели

ER модели — это способ визуального представления структуры данных через сущности (entities) и связи между ними (relationships).

### 2.1 Основные понятия

**Entity (Сущность):**

- Объект или концепция, о которой хранятся данные
- Представляется таблицей в БД
- Примеры: User, Product, Order

**Attribute (Атрибут):**

- Свойство сущности
- Представляется колонкой в таблице
- Примеры: name, email, price

**Relationship (Связь):**

- Связь между сущностями
- Типы: One-to-One, One-to-Many, Many-to-Many

**Example: ER модель для E-commerce**

```python
# ER модель: Users, Products, Orders

entities = {
    "User": {
        "attributes": ["user_id", "name", "email", "created_at"],
        "primary_key": "user_id"
    },
    "Product": {
        "attributes": ["product_id", "name", "price", "category"],
        "primary_key": "product_id"
    },
    "Order": {
        "attributes": ["order_id", "user_id", "total_amount", "order_date"],
        "primary_key": "order_id",
        "foreign_keys": {"user_id": "User.user_id"}
    },
    "OrderItem": {
        "attributes": ["order_id", "product_id", "quantity", "price"],
        "primary_key": ["order_id", "product_id"],
        "foreign_keys": {
            "order_id": "Order.order_id",
            "product_id": "Product.product_id"
        }
    }
}

print("ER Model для E-commerce:")
for entity, info in entities.items():
    print(f"\n{entity}:")
    print(f"  Attributes: {', '.join(info['attributes'])}")
    print(f"  Primary Key: {info['primary_key']}")
    if 'foreign_keys' in info:
        print(f"  Foreign Keys: {info['foreign_keys']}")
```

**Output:**
```

ER Model для E-commerce:

User:
  Attributes: user_id, name, email, created_at
  Primary Key: user_id

Product:
  Attributes: product_id, name, price, category
  Primary Key: product_id

Order:
  Attributes: order_id, user_id, total_amount, order_date
  Primary Key: order_id
  Foreign Keys: {'user_id': 'User.user_id'}

OrderItem:
  Attributes: order_id, product_id, quantity, price
  Primary Key: ['order_id', 'product_id']
  Foreign Keys: {'order_id': 'Order.order_id', 'product_id': 'Product.product_id'}
```

### 2.2 Типы связей

**One-to-One (1:1):**

- Одна запись в одной таблице связана с одной записью в другой
- Пример: User ↔ UserProfile
- Реализация: Foreign key в одной из таблиц

**One-to-Many (1:N):**

- Одна запись связана со многими записями
- Пример: User ↔ Orders (один пользователь, много заказов)
- Реализация: Foreign key на стороне "многих"

**Many-to-Many (M:N):**

- Много записей связаны со многими записями
- Пример: Products ↔ Orders (много продуктов в много заказов)
- Реализация: Junction table (связующая таблица)

**Example: Типы связей**

```python
# Демонстрация типов связей

relationships = {
    "One-to-One": {
        "example": "User ↔ UserProfile",
        "implementation": "FK в UserProfile на User.user_id",
        "sql": """
        CREATE TABLE users (user_id INT PRIMARY KEY, name VARCHAR(100));
        CREATE TABLE user_profiles (
            profile_id INT PRIMARY KEY,
            user_id INT UNIQUE REFERENCES users(user_id),
            bio TEXT
        );
        """
    },
    "One-to-Many": {
        "example": "User ↔ Orders",
        "implementation": "FK в Orders на User.user_id",
        "sql": """
        CREATE TABLE users (user_id INT PRIMARY KEY, name VARCHAR(100));
        CREATE TABLE orders (
            order_id INT PRIMARY KEY,
            user_id INT REFERENCES users(user_id),
            total_amount DECIMAL
        );
        """
    },
    "Many-to-Many": {
        "example": "Products ↔ Orders",
        "implementation": "Junction table OrderItems",
        "sql": """
        CREATE TABLE products (product_id INT PRIMARY KEY, name VARCHAR(100));
        CREATE TABLE orders (order_id INT PRIMARY KEY);
        CREATE TABLE order_items (
            order_id INT REFERENCES orders(order_id),
            product_id INT REFERENCES products(product_id),
            quantity INT,
            PRIMARY KEY (order_id, product_id)
        );
        """
    }
}

print("Типы связей в ER моделях:")
for rel_type, info in relationships.items():
    print(f"\n{rel_type}:")
    print(f"  Пример: {info['example']}")
    print(f"  Реализация: {info['implementation']}")
```

**Output:**
```

Типы связей в ER моделях:

One-to-One:
  Пример: User ↔ UserProfile
  Реализация: FK в UserProfile на User.user_id

One-to-Many:
  Пример: User ↔ Orders
  Реализация: FK в Orders на User.user_id

Many-to-Many:
  Пример: Products ↔ Orders
  Реализация: Junction table OrderItems
```

---

## 3. Normalization (Нормализация)

Нормализация — это процесс организации данных для минимизации избыточности и аномалий. Цель: каждая часть данных должна храниться только в одном месте.

### 3.1 Проблемы без нормализации

**Избыточность данных:**

- Одни и те же данные хранятся в нескольких местах
- Увеличивает размер БД
- Риск неконсистентности

**Аномалии:**

- **Update anomaly**: Изменение в одном месте требует изменений везде

- **Insert anomaly**: Невозможно добавить данные без связанных данных

- **Delete anomaly**: Удаление одной записи удаляет связанные данные

**Example: Проблемы без нормализации**

```python
# Плохая структура: все данные в одной таблице
bad_design = {
    "order_id": [1001, 1002, 1003],
    "user_name": ["Alice", "Alice", "Bob"],
    "user_email": ["alice@example.com", "alice@example.com", "bob@example.com"],
    "product_name": ["Laptop", "Mouse", "Keyboard"],
    "product_price": [999.99, 29.99, 79.99],
    "quantity": [1, 2, 1],
    "order_date": ["2024-01-01", "2024-01-01", "2024-01-02"]
}

print("Проблемы без нормализации:")
print("1. Избыточность: user_name и user_email дублируются для Alice")
print("2. Update anomaly: Изменение email Alice требует обновления всех её заказов")
print("3. Delete anomaly: Удаление заказа 1001 не удалит пользователя, но данные будут неконсистентны")
print("\nПример данных:")
for i in range(3):
    print(f"  Order {bad_design['order_id'][i]}: {bad_design['user_name'][i]} - {bad_design['product_name'][i]}")
```

**Output:**
```

Проблемы без нормализации:

1. Избыточность: user_name и user_email дублируются для Alice
2. Update anomaly: Изменение email Alice требует обновления всех её заказов
3. Delete anomaly: Удаление заказа 1001 не удалит пользователя, но данные будут неконсистентны

Пример данных:
  Order 1001: Alice - Laptop
  Order 1002: Alice - Mouse
  Order 1003: Bob - Keyboard
```

### 3.2 Нормальные формы

**1NF (First Normal Form):**

- Атомарные значения (одно значение в ячейке)
- Нет повторяющихся групп
- Уникальные строки

**2NF (Second Normal Form):**

- 1NF +
- Нет частичных зависимостей (все неключевые атрибуты зависят от всего первичного ключа)

**3NF (Third Normal Form):**

- 2NF +
- Нет транзитивных зависимостей (неключевые атрибуты не зависят от других неключевых атрибутов)

**Example: Нормализация до 3NF**

```python
# Нормализованная структура

normalized_design = {
    "users": {
        "columns": ["user_id", "name", "email"],
        "pk": "user_id",
        "data": [
            (1, "Alice", "alice@example.com"),
            (2, "Bob", "bob@example.com")
        ]
    },
    "products": {
        "columns": ["product_id", "name", "price"],
        "pk": "product_id",
        "data": [
            (101, "Laptop", 999.99),
            (102, "Mouse", 29.99),
            (103, "Keyboard", 79.99)
        ]
    },
    "orders": {
        "columns": ["order_id", "user_id", "order_date"],
        "pk": "order_id",
        "fk": {"user_id": "users.user_id"},
        "data": [
            (1001, 1, "2024-01-01"),
            (1002, 1, "2024-01-01"),
            (1003, 2, "2024-01-02")
        ]
    },
    "order_items": {
        "columns": ["order_id", "product_id", "quantity"],
        "pk": ["order_id", "product_id"],
        "fk": {
            "order_id": "orders.order_id",
            "product_id": "products.product_id"
        },
        "data": [
            (1001, 101, 1),
            (1002, 102, 2),
            (1003, 103, 1)
        ]
    }
}

print("Нормализованная структура (3NF):")
for table, info in normalized_design.items():
    print(f"\n{table.upper()}:")
    print(f"  Columns: {', '.join(info['columns'])}")
    print(f"  PK: {info['pk']}")
    if 'fk' in info:
        print(f"  FK: {info['fk']}")
```

**Output:**
```

Нормализованная структура (3NF):

USERS:
  Columns: user_id, name, email
  PK: user_id

PRODUCTS:
  Columns: product_id, name, price
  PK: product_id

ORDERS:
  Columns: order_id, user_id, order_date
  PK: order_id
  FK: {'user_id': 'users.user_id'}

ORDER_ITEMS:
  Columns: order_id, product_id, quantity
  PK: ['order_id', 'product_id']
  FK: {'order_id': 'orders.order_id', 'product_id': 'products.product_id'}
```

### 3.3 Преимущества нормализации

**Целостность данных:**

- Данные хранятся в одном месте
- Легче поддерживать консистентность
- Меньше риск ошибок

**Эффективность обновлений:**

- Изменение в одном месте
- Меньше операций записи
- Быстрее обновления

**Гибкость:**

- Легче добавлять новые атрибуты
- Меньше структурных изменений
- Проще масштабировать

---

## 4. Denormalization (Денормализация)

Денормализация — это намеренное добавление избыточности для улучшения производительности чтения. Это trade-off между скоростью чтения и сложностью обновления.

### 4.1 Когда использовать денормализацию

**Оптимизация чтения:**

- Частые сложные запросы с JOIN
- Медленные аналитические запросы
- Real-time dashboards

**OLAP системы:**

- Data warehouses
- Аналитические хранилища
- Чтение преобладает над записью

**Example: Денормализация для аналитики**

```python
# Нормализованная структура (для транзакций)
normalized = {
    "orders": {
        "order_id": 1001,
        "user_id": 1,
        "order_date": "2024-01-01"
    },
    "users": {
        "user_id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    },
    "order_items": [
        {"order_id": 1001, "product_id": 101, "quantity": 1}
    ],
    "products": {
        "product_id": 101,
        "name": "Laptop",
        "price": 999.99
    }
}

# Денормализованная структура (для аналитики)

denormalized = {
    "order_id": 1001,
    "user_name": "Alice",
    "user_email": "alice@example.com",
    "order_date": "2024-01-01",
    "product_name": "Laptop",
    "product_price": 999.99,
    "quantity": 1,
    "total_amount": 999.99
}

print("Сравнение:")
print("\nНормализованная (для транзакций):")
print("  - Нужен JOIN для получения user_name и product_name")
print("  - Эффективна для записей")
print("\nДенормализованная (для аналитики):")
print("  - Все данные в одной строке")
print("  - Нет JOIN, быстрые запросы")
print("  - Эффективна для чтения")
```

**Output:**
```

Сравнение:

Нормализованная (для транзакций):

  - Нужен JOIN для получения user_name и product_name
  - Эффективна для записей
  - Занимает меньше места

Денормализованная (для аналитики):

  - Все данные в одной строке
  - Нет JOIN, быстрые запросы
  - Эффективна для чтения
  - Занимает больше места
```

### 4.2 Типы денормализации

**Дублирование данных:**

- Копирование часто используемых полей
- Пример: user_name в orders таблице

**Вычисляемые поля:**

- Предварительно вычисленные значения
- Пример: total_amount в orders

**Сводные таблицы:**

- Агрегированные данные
- Пример: daily_sales_summary

**Example: Типы денормализации**

```python

denormalization_examples = {
    "duplication": {
        "description": "Дублирование user_name в orders",
        "before": "SELECT o.*, u.name FROM orders o JOIN users u ON o.user_id = u.user_id",
        "after": "SELECT * FROM orders WHERE user_name = 'Alice'",
        "tradeoff": "Быстрее чтение, но нужно обновлять при изменении name"
    },
    "computed_fields": {
        "description": "Предвычисленное total_amount",
        "before": "SELECT SUM(quantity * price) FROM order_items WHERE order_id = 1001",
        "after": "SELECT total_amount FROM orders WHERE order_id = 1001",
        "tradeoff": "Быстрее чтение, но нужно пересчитывать при изменении items"
    },
    "summary_tables": {
        "description": "Сводная таблица daily_sales",
        "before": """
        SELECT 
            DATE(order_date) as date,
            SUM(total_amount) as daily_revenue
        FROM orders
        GROUP BY DATE(order_date)
        """,
        "after": "SELECT * FROM daily_sales WHERE date = '2024-01-01'",
        "tradeoff": "Мгновенные запросы, но нужно обновлять при новых заказах"
    }
}

print("Типы денормализации:")
for denorm_type, info in denormalization_examples.items():
    print(f"\n{denorm_type.upper()}:")
    print(f"  {info['description']}")
    print(f"  Trade-off: {info['tradeoff']}")
```

**Output:**
```

Типы денормализации:

DUPLICATION:
  Дублирование user_name в orders
  Trade-off: Быстрее чтение, но нужно обновлять при изменении name

COMPUTED_FIELDS:
  Предвычисленное total_amount
  Trade-off: Быстрее чтение, но нужно пересчитывать при изменении items

SUMMARY_TABLES:
  Сводная таблица daily_sales
  Trade-off: Мгновенные запросы, но нужно обновлять при новых заказах
```

---

## 5. Trade-offs: Normalization vs Denormalization

Выбор между нормализацией и денормализацией — это компромисс между различными требованиями.

### 5.1 Сравнение

| Аспект | Normalization | Denormalization |
|--------|---------------|-----------------|
| **Избыточность** | Минимальная | Высокая |
| **Запись** | Быстрая | Медленная |
| **Чтение** | Требует JOIN | Быстрое |
| **Целостность** | Высокая | Нужна синхронизация |
| **Размер БД** | Меньше | Больше |
| **Сложность** | Проще поддержка | Сложнее обновления |

### 5.2 Когда что использовать

**Используйте Normalization, если:**

- OLTP система (транзакции)
- Много операций записи
- Требуется высокая целостность
- Размер БД критичен

**Используйте Denormalization, если:**

- OLAP система (аналитика)
- Много операций чтения
- Сложные аналитические запросы
- Производительность чтения критична

**Example: Выбор стратегии**

```python

def recommend_strategy(requirements):
    """Рекомендует стратегию моделирования"""
    if requirements.get("oltp") and requirements.get("many_writes"):
        return "Normalization (минимизировать избыточность)"
    elif requirements.get("olap") and requirements.get("analytical_queries"):
        return "Denormalization (оптимизировать чтение)"
    elif requirements.get("hybrid"):
        return "Hybrid (нормализованные операционные данные, денормализованные аналитические)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"oltp": True, "many_writes": True, "transactional": True},
    {"olap": True, "analytical_queries": True, "read_heavy": True},
    {"hybrid": True, "both_needed": True}
]

print("Рекомендации стратегии:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_strategy(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации стратегии:
  Пример 1: Normalization (минимизировать избыточность)
  Пример 2: Denormalization (оптимизировать чтение)
  Пример 3: Hybrid (нормализованные операционные данные, денормализованные аналитические)
```

### 5.3 Hybrid подход

В реальных системах часто используется гибридный подход:

**Operational Data (OLTP):**

- Нормализованные структуры
- Для транзакций и операций
- Высокая целостность

**Analytical Data (OLAP):**

- Денормализованные структуры
- Для аналитики и отчётов
- Оптимизация чтения

**Example: Hybrid подход**

```python
# Hybrid архитектура

hybrid_architecture = {
    "operational_layer": {
        "type": "OLTP",
        "normalization": "3NF",
        "purpose": "Транзакции, операции",
        "tables": ["users", "products", "orders", "order_items"],
        "characteristics": "Нормализованные, быстрые записи"
    },
    "analytical_layer": {
        "type": "OLAP",
        "normalization": "Denormalized",
        "purpose": "Аналитика, отчёты",
        "tables": ["sales_facts", "customer_dimensions", "product_dimensions"],
        "characteristics": "Денормализованные, быстрые запросы"
    },
    "etl": {
        "description": "ETL процесс из operational в analytical",
        "frequency": "Daily/hourly",
        "transformation": "Денормализация и агрегация"
    }
}

print("Hybrid подход:")
for layer, info in hybrid_architecture.items():
    print(f"\n{layer.upper()}:")
    if isinstance(info, dict):
        for key, value in info.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {info}")
```

**Output:**
```

Hybrid подход:

OPERATIONAL_LAYER:
  type: OLTP
  normalization: 3NF
  purpose: Транзакции, операции
  tables: ['users', 'products', 'orders', 'order_items']
  characteristics: Нормализованные, быстрые записи

ANALYTICAL_LAYER:
  type: OLAP
  normalization: Denormalized
  purpose: Аналитика, отчёты
  tables: ['sales_facts', 'customer_dimensions', 'product_dimensions']
  characteristics: Денормализованные, быстрые запросы

ETL:
  description: ETL процесс из operational в analytical
  frequency: Daily/hourly
  transformation: Денормализация и агрегация
```

---

## 💡 Key Takeaways

- **ER модели**: Entity-Relationship модели помогают визуализировать структуру данных через сущности и связи. Понимание типов связей (1:1, 1:N, M:N) критично для проектирования.

- **Нормализация**: Устраняет избыточность и аномалии данных. 3NF — стандарт для OLTP систем. Улучшает целостность и упрощает обновления.

- **Денормализация**: Добавляет избыточность для оптимизации чтения. Trade-off между скоростью чтения и сложностью обновления. Подходит для OLAP систем.

- **Trade-offs**: Нет универсального решения. Normalization для транзакций, denormalization для аналитики. Выбор зависит от паттернов доступа.

- **Hybrid подход**: Реальные системы часто используют оба подхода: нормализованные операционные данные и денормализованные аналитические данные.

---

## 🚀 Next Steps

**Related Modules:**

- [05_Data_Storage](../05_Data_Storage/) — хранилища данных (OLTP, OLAP)
- [06_Data_Formats](../06_Data_Formats/) — форматы данных
- [07_Indexes_Partitioning](../07_Indexes_Partitioning/) — индексы и партиционирование

**Practice Ideas:**

1. Спроектируйте ER модель для вашего проекта: определите сущности, связи, атрибуты
2. Нормализуйте существующую структуру данных до 3NF
3. Проанализируйте, где в вашей системе нужна денормализация для оптимизации запросов

**Going Deeper:**

- Изучите продвинутые нормальные формы (BCNF, 4NF, 5NF)
- Погрузитесь в Data Vault modeling для data warehouses
- Изучите Dimensional modeling (Star Schema, Snowflake Schema)

---

## 📚 Additional Resources

**Books:**

- "Database Design for Mere Mortals" by Michael J. Hernandez — практическое руководство по проектированию БД
- "The Data Warehouse Toolkit" by Ralph Kimball — dimensional modeling

**Articles:**

- "Database Normalization Explained" — детальное объяснение нормальных форм
- "When to Denormalize a Database" — практические рекомендации

**Documentation:**

- PostgreSQL: https://www.postgresql.org/docs/current/ddl.html
- MySQL: https://dev.mysql.com/doc/refman/8.0/en/database-design.html

---


