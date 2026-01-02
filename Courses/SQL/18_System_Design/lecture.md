# SQL как часть system design
## SQL и API, SQL и кэширование, когда SQL не подходит, границы реляционных БД

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы SQL и баз данных
- Иметь представление о архитектуре приложений
- Знать концепции производительности и масштабирования

**Recommended prior modules:**

- [13_Transactions](../13_Transactions/) — SQL и транзакции
- [14_Performance](../14_Performance/) — Производительность и масштабирование
- [17_Antipatterns](../17_Antipatterns/) — Антипаттерны SQL

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать роль SQL в архитектуре приложений
- Применять кэширование для оптимизации SQL запросов
- Определять, когда SQL не подходит для задачи
- Понимать границы реляционных баз данных
- Проектировать системы с учётом ограничений SQL

---

## 1. SQL и API

### 1.1 SQL в backend приложениях

**Типичная архитектура:**

```
Client → API → Application → SQL Database
```

**Роль SQL:**

- Хранение структурированных данных
- Обеспечение целостности данных
- Выполнение бизнес-логики (частично)

**Пример:**

```sql
-- API endpoint: GET /users/{id}/orders
-- SQL запрос в backend
SELECT 
    o.id,
    o.amount,
    o.order_date
FROM orders o
WHERE o.user_id = $1
ORDER BY o.order_date DESC;
```

### 1.2 ORM vs Raw SQL

**ORM (Object-Relational Mapping):**

- ✅ Абстракция от SQL
- ✅ Безопасность (защита от SQL injection)
- ❌ Может генерировать неоптимальные запросы

**Raw SQL:**

- ✅ Полный контроль
- ✅ Оптимизация запросов
- ❌ Больше кода
- ❌ Риск SQL injection (если не использовать параметры)

---

## 2. SQL и кэширование

### 2.1 Зачем кэшировать SQL результаты

**Проблема:** Частые запросы к базе данных медленные.

**Решение:** Кэширование результатов запросов.

**Стратегии:**

### 2.2 Cache-Aside (Lazy Loading)

**Алгоритм:**

1. Проверить кэш
2. Если нет в кэше → запрос к БД
3. Сохранить результат в кэш
4. Вернуть результат

**Пример:**

```python
# Псевдокод

def get_user(user_id):
    # 1. Проверить кэш
    cached = cache.get(f"user:{user_id}")
    if cached:
        return cached
    
    # 2. Запрос к БД
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    
    # 3. Сохранить в кэш
    cache.set(f"user:{user_id}", user, ttl=3600)
    
    return user
```

### 2.3 Write-Through

**Алгоритм:**

1. Запись в БД
2. Одновременно обновление кэша

### 2.4 Инвалидация кэша

**Проблема:** Кэш может устареть.

**Решения:**

- TTL (Time To Live) — автоматическое истечение
- Инвалидация при обновлении данных
- Версионирование ключей кэша

---

## 3. Когда SQL не подходит

### 3.1 Очень высокая скорость записи

**Проблема SQL:**

- Транзакции замедляют запись
- ACID гарантии требуют синхронизации
- Ограничения целостности проверяются

**Альтернативы:**

- NoSQL (MongoDB, Cassandra)
- Message queues (Kafka)
- In-memory хранилища (Redis)

### 3.2 Неструктурированные данные

**Проблема SQL:**

- Жёсткая схема
- Сложно хранить JSON, документы
- Нет гибкости

**Альтернативы:**

- Document databases (MongoDB)
- Key-value stores (Redis, DynamoDB)

### 3.3 Горизонтальное масштабирование записи

**Проблема SQL:**

- Реляционные БД сложно масштабировать горизонтально
- Master-slave репликация для чтения
- Sharding сложен

**Альтернативы:**

- NoSQL с нативной поддержкой sharding
- Distributed systems

### 3.4 Очень большие объёмы данных

**Проблема SQL:**

- Ограничения размера таблиц
- Медленные запросы на терабайтах

**Альтернативы:**

- Data Warehouses (BigQuery, Snowflake)
- Колоночные хранилища (ClickHouse)
- Hadoop экосистема

---

## 4. Границы реляционных БД

### 4.1 Когда SQL идеален

**SQL подходит для:**

- ✅ Структурированные данные
- ✅ Сложные запросы и связи
- ✅ Транзакции и целостность данных
- ✅ Отчёты и аналитика
- ✅ Средние объёмы данных

### 4.2 Когда SQL не идеален

**SQL не подходит для:**

- ❌ Очень высокая скорость записи (миллионы в секунду)
- ❌ Неструктурированные данные
- ❌ Простые key-value операции
- ❌ Очень большие объёмы (петабайты)
- ❌ Горизонтальное масштабирование записи

### 4.3 Гибридные подходы

**Комбинация SQL и NoSQL:**

```
SQL Database (основные данные)
    ↓
Message Queue (события)
    ↓
NoSQL (кэш, аналитика)
```

**Пример архитектуры:**

- **PostgreSQL** — основная база данных (транзакции, структурированные данные)

- **Redis** — кэш и сессии

- **MongoDB** — документы и логи

- **Kafka** — потоковая обработка событий

---

## 5. SQL в микросервисах

### 5.1 Database per Service

**Паттерн:**

- Каждый микросервис имеет свою базу данных
- Нет прямого доступа между базами
- Коммуникация через API

**Преимущества:**

- ✅ Независимость сервисов
- ✅ Разные технологии БД
- ✅ Изоляция данных

**Недостатки:**

- ❌ Сложнее транзакции между сервисами
- ❌ Дублирование данных
- ❌ Сложнее отчёты

### 5.2 Saga Pattern

**Для распределённых транзакций:**

- Компенсирующие транзакции вместо ACID
- Каждый сервис выполняет свою часть
- При ошибке — откат через компенсацию

---

## 6. CQRS (Command Query Responsibility Segregation)

### 6.1 Что такое CQRS

**CQRS** — разделение команд (запись) и запросов (чтение).

**Архитектура:**

```
Commands (Write) → SQL Database (Write Model)
Queries (Read)   → Read Model (SQL или NoSQL)
```

**Пример:**

```sql
-- Write Model (SQL для команд)
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount DECIMAL(10, 2),
    status VARCHAR(20)
);

-- Read Model (оптимизирован для чтения)
CREATE MATERIALIZED VIEW order_summary AS
SELECT 
    user_id,
    COUNT(*) AS order_count,
    SUM(amount) AS total_spent
FROM orders
GROUP BY user_id;
```

### 6.2 Преимущества CQRS

- ✅ Оптимизация чтения и записи независимо
- ✅ Масштабирование чтения отдельно
- ✅ Разные модели для разных задач

---

## 7. Event Sourcing

### 7.1 Что такое Event Sourcing

**Event Sourcing** — хранение событий вместо текущего состояния.

**Традиционный подход:**

```sql
-- Храним текущее состояние
UPDATE accounts SET balance = 900 WHERE id = 1;
```

**Event Sourcing:**

```sql
-- Храним события
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    aggregate_id INTEGER,
    event_type VARCHAR(50),
    event_data JSONB,
    timestamp TIMESTAMP
);

INSERT INTO events (aggregate_id, event_type, event_data)
VALUES (1, 'AccountDebited', '{"amount": 100}');
```

### 7.2 Восстановление состояния

**Из событий можно восстановить состояние:**

```sql
-- Восстановление баланса из событий
SELECT 
    aggregate_id,
    SUM(CASE 
        WHEN event_type = 'AccountCredited' 
        THEN (event_data->>'amount')::DECIMAL
        WHEN event_type = 'AccountDebited' 
        THEN -(event_data->>'amount')::DECIMAL
        ELSE 0
    END) AS balance
FROM events
WHERE aggregate_id = 1
GROUP BY aggregate_id;
```

---

## 8. Read Replicas

### 8.1 Что такое Read Replicas

**Read Replicas** — копии базы данных только для чтения.

**Архитектура:**

```
Master (Write) → Replica 1 (Read)
              → Replica 2 (Read)
              → Replica 3 (Read)
```

**Использование:**

```python
# Запись на master

write_db.execute("INSERT INTO users ...")

# Чтение с replica

read_db = get_read_replica()
users = read_db.query("SELECT * FROM users")
```

### 8.2 Преимущества

- ✅ Масштабирование чтения
- ✅ Распределение нагрузки
- ✅ Географическое распределение

---

## 9. Best Practices

### 9.1 Проектирование с SQL

**Рекомендации:**

- ✅ Используйте SQL для структурированных данных
- ✅ Кэшируйте частые запросы
- ✅ Мониторьте производительность
- ✅ Используйте connection pooling
- ✅ Ограничивайте время выполнения запросов
- ✅ Используйте read replicas для масштабирования чтения
- ✅ Рассмотрите CQRS для сложных систем

### 9.2 Когда выбирать альтернативы

**Выбирайте NoSQL когда:**

- Очень высокая скорость записи (миллионы в секунду)
- Неструктурированные данные (JSON, документы)
- Простые key-value операции
- Горизонтальное масштабирование записи критично
- Схема часто меняется

**Оставайтесь с SQL когда:**

- Нужны сложные запросы и JOIN
- Транзакции и ACID критичны
- Данные структурированы
- Нужна целостность данных

---

## 10. Архитектурные паттерны

### 10.1 Layered Architecture

**Трёхслойная архитектура:**

```
Presentation Layer (API)
    ↓
Business Logic Layer
    ↓
Data Access Layer (SQL)
```

**SQL в Data Access Layer:**

```python
class UserRepository:
    def get_user(self, user_id):
        return db.query("SELECT * FROM users WHERE id = ?", user_id)
    
    def create_user(self, user_data):
        return db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            user_data['name'], user_data['email']
        )
```

### 10.2 Repository Pattern

**Абстракция доступа к данным:**

```python
class OrderRepository:
    def find_by_user(self, user_id):
        return db.query("""
            SELECT * FROM orders 
            WHERE user_id = ?
            ORDER BY order_date DESC
        """, user_id)
    
    def save(self, order):
        return db.execute("""
            INSERT INTO orders (user_id, amount)
            VALUES (?, ?)
        """, order.user_id, order.amount)
```

---

## 11. Производительность в production

### 11.1 Connection Pooling

**Настройка пула соединений:**

```python
# SQLAlchemy connection pool

engine = create_engine(
    'postgresql://user:pass@localhost/db',
    pool_size=20,
    max_overflow=10,
    pool_timeout=30
)
```

### 11.2 Query Timeouts

**Ограничение времени выполнения:**

```sql
-- PostgreSQL
SET statement_timeout = '30s';

-- В приложении
cursor.execute("SET statement_timeout = '30s'")
cursor.execute("SELECT * FROM large_table")
```

### 11.3 Мониторинг

**Мониторинг медленных запросов:**

```sql
-- Включить логирование
ALTER DATABASE mydb SET log_min_duration_statement = 1000;

-- Просмотр медленных запросов
SELECT * FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

---

## 12. Безопасность

### 12.1 SQL Injection

**❌ Уязвимый код:**

```python
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# SQL Injection!
```

**✅ Безопасный код:**

```python
# Prepared statements

query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

### 12.2 Права доступа

**Ограничение прав:**

```sql
-- Создать пользователя только для чтения
CREATE USER readonly_user WITH PASSWORD 'password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;

-- Пользователь для записи
CREATE USER app_user WITH PASSWORD 'password';
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_user;
```

### 12.3 Шифрование

**Шифрование данных:**

```sql
-- Шифрование на уровне приложения
-- Или использование pgcrypto (PostgreSQL)
CREATE EXTENSION pgcrypto;

INSERT INTO users (email, password_hash)
VALUES ('user@example.com', crypt('password', gen_salt('bf')));
```

---

## 💡 Key Takeaways

- **SQL и API** — SQL используется в backend для хранения и запросов данных

- **Кэширование** — Cache-Aside, Write-Through для оптимизации частых запросов

- **Границы SQL** — не подходит для очень высокой скорости записи, неструктурированных данных, петабайтов

- **Гибридные подходы** — комбинация SQL и NoSQL для разных задач

- **Микросервисы** — Database per Service, Saga Pattern для распределённых транзакций

---

## 🚀 Next Steps

**Related Modules:**

- [14_Performance](../14_Performance/) — Производительность и масштабирование
- [15_Analytics](../15_Analytics/) — SQL в аналитике

**Practice Ideas:**

1. Спроектируйте систему с SQL и кэшированием
2. Изучите гибридные архитектуры (SQL + NoSQL)
3. Попрактикуйтесь с connection pooling
4. Изучите паттерны для микросервисов

**Going Deeper:**

- Изучите архитектурные паттерны (CQRS, Event Sourcing)
- Изучите распределённые системы
- Изучите альтернативы SQL для специфичных задач

---

## 📚 Additional Resources

**Documentation:**

- [System Design Primer](https://github.com/donnemartin/system-design-primer) — основы system design
- [Database per Service](https://microservices.io/patterns/data/database-per-service.html) — паттерн микросервисов

---



