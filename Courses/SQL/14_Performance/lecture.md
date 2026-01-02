# Производительность и масштабирование
## Причины медленных запросов, CPU/память/I/O, партиционирование, sharding

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу индексов
- Знать, как использовать EXPLAIN
- Иметь представление о планах выполнения запросов

**Recommended prior modules:**

- [09_Indexes](../09_Indexes/) — Индексы
- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять причины медленных запросов
- Понимать влияние CPU, памяти и I/O на производительность
- Применять партиционирование для больших таблиц
- Понимать концепцию sharding
- Оптимизировать запросы для лучшей производительности

---

## 1. Причины медленных запросов

### 1.1 Отсутствие индексов

**Проблема:**

```sql
-- Без индекса: Seq Scan (медленно)
SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Решение:**

```sql
CREATE INDEX idx_users_email ON users(email);
-- Теперь: Index Scan (быстро)
```

### 1.2 Неэффективные запросы

**Проблемы:**

- SELECT * вместо конкретных столбцов
- Неоптимальные JOIN
- Отсутствие WHERE условий
- Сложные подзапросы

### 1.3 Большие таблицы

**Проблема:** Полное сканирование больших таблиц медленно.

**Решения:**

- Партиционирование
- Индексы
- Кэширование

---

## 2. CPU, память и I/O

### 2.1 CPU

**CPU используется для:**

- Вычислений (агрегаты, функции)
- Сортировки (ORDER BY)
- JOIN операций

**Оптимизация:**

- Использовать индексы для сортировки
- Избегать сложных вычислений в WHERE
- Использовать материализованные представления

### 2.2 Память

**Память используется для:**

- Кэширования данных
- Сортировки
- JOIN операций

**Настройки (PostgreSQL):**

```sql
-- Увеличить shared_buffers для кэширования
-- В postgresql.conf:
shared_buffers = 256MB
work_mem = 4MB  -- Память для сортировки и JOIN
```

### 2.3 I/O (диск)

**I/O — часто узкое место:**

- Чтение с диска медленнее памяти в 100-1000 раз
- Запись на диск медленнее памяти

**Оптимизация:**

- Использовать SSD вместо HDD
- Увеличить кэш (shared_buffers)
- Использовать индексы для уменьшения I/O

---

## 3. Партиционирование

### 3.1 Что такое партиционирование

**Партиционирование** — разделение большой таблицы на меньшие части (партиции).

**Преимущества:**

- ✅ Быстрее запросы (сканируется только нужная партиция)
- ✅ Проще управление (можно удалять старые партиции)
- ✅ Параллельная обработка

### 3.2 Range Partitioning

**Партиционирование по диапазону:**

```sql
-- PostgreSQL
CREATE TABLE orders (
    id INTEGER,
    order_date DATE,
    amount DECIMAL(10, 2)
) PARTITION BY RANGE (order_date);

-- Партиции по месяцам
CREATE TABLE orders_2024_01 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE orders_2024_02 PARTITION OF orders
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

**Запрос автоматически использует нужную партицию:**

```sql
SELECT * FROM orders WHERE order_date = '2024-01-15';
-- Сканируется только orders_2024_01
```

### 3.3 List Partitioning

**Партиционирование по списку:**

```sql
CREATE TABLE users (
    id INTEGER,
    country VARCHAR(50),
    name VARCHAR(100)
) PARTITION BY LIST (country);

CREATE TABLE users_russia PARTITION OF users
    FOR VALUES IN ('Russia');

CREATE TABLE users_usa PARTITION OF users
    FOR VALUES IN ('USA');
```

---

## 4. Sharding

### 4.1 Что такое sharding

**Sharding** — горизонтальное разделение данных между несколькими базами данных.

**Отличие от партиционирования:**

- **Партиционирование** — одна база, несколько таблиц

- **Sharding** — несколько баз данных

**Когда использовать:**

- ✅ Очень большие объёмы данных
- ✅ Географическое распределение
- ✅ Масштабирование записи

### 4.2 Стратегии sharding

**По диапазону:**

- База 1: user_id 1-1000000
- База 2: user_id 1000001-2000000

**По хешу:**

- user_id % 4 определяет базу данных

**По географии:**

- База для России, база для США

---

## 5. Кэширование

### 5.1 Кэш базы данных

**Shared Buffers (PostgreSQL):**

```sql
-- Настройка размера кэша
-- В postgresql.conf:
shared_buffers = 256MB  -- 25% от RAM для небольших серверов
```

**Как работает:**

- Часто используемые страницы хранятся в памяти
- Чтение из памяти в 100-1000 раз быстрее диска
- Автоматическое управление (LRU алгоритм)

### 5.2 Query Cache

**Кэширование результатов запросов (MySQL):**

```sql
-- Проверить статус query cache
SHOW VARIABLES LIKE 'query_cache%';

-- Включить query cache
SET GLOBAL query_cache_size = 67108864;  -- 64MB
SET GLOBAL query_cache_type = 1;  -- ON
```

**Ограничения:**

- Работает только для идентичных запросов
- Инвалидируется при изменении данных
- Не всегда эффективен

### 5.3 Application-level кэширование

**Кэширование в приложении (Redis, Memcached):**

```python
# Псевдокод

def get_user(user_id):
    # Проверить кэш
    cached = cache.get(f"user:{user_id}")
    if cached:
        return cached
    
    # Запрос к БД
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    
    # Сохранить в кэш
    cache.set(f"user:{user_id}", user, ttl=3600)
    return user
```

---

## 6. Connection Pooling

### 6.1 Что такое Connection Pool

**Connection Pool** — пул переиспользуемых соединений с БД.

**Проблема без pooling:**

```python
# Каждый запрос создаёт новое соединение

for request in requests:
    conn = connect_to_db()  # Медленно!
    execute_query(conn)
    conn.close()  # Закрываем соединение
```

**С pooling:**

```python
# Соединения переиспользуются

pool = create_connection_pool(size=20)

for request in requests:
    conn = pool.get_connection()  # Быстро!
    execute_query(conn)
    pool.return_connection(conn)  # Возвращаем в пул
```

### 6.2 Настройка пула

**PgBouncer (для PostgreSQL):**

```ini
[databases]
mydb = host=localhost dbname=mydb

[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 25
```

**Преимущества:**

- ✅ Быстрое установление соединений
- ✅ Контроль количества соединений
- ✅ Эффективное использование ресурсов

---

## 7. Материализованные представления

### 7.1 Что такое Materialized View

**Materialized View** — предвычисленное представление, хранящее результаты запроса.

**Пример:**

```sql
-- Создание материализованного представления
CREATE MATERIALIZED VIEW user_order_stats AS
SELECT 
    u.id,
    u.name,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- Использование (быстро!)
SELECT * FROM user_order_stats WHERE total_spent > 1000;
```

### 7.2 Обновление материализованных представлений

```sql
-- Ручное обновление
REFRESH MATERIALIZED VIEW user_order_stats;

-- Автоматическое обновление (через cron или триггеры)
-- Или через pg_cron (PostgreSQL расширение)
```

**Когда использовать:**

- ✅ Сложные агрегации
- ✅ Данные изменяются редко
- ✅ Нужна высокая скорость чтения

---

## 8. Оптимизация запросов

### 8.1 Анализ медленных запросов

**Шаги:**

1. Использовать EXPLAIN ANALYZE
2. Найти узкие места (Seq Scan, медленные JOIN)
3. Создать индексы
4. Оптимизировать запрос

**Пример:**

```sql
-- Медленный запрос
EXPLAIN ANALYZE
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE u.country = 'Russia'
ORDER BY o.order_date DESC
LIMIT 10;

-- Результат показывает Seq Scan
-- Решение: создать индексы
CREATE INDEX idx_users_country ON users(country);
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date DESC);
```

### 8.2 Оптимизация JOIN

**Порядок JOIN важен:**

```sql
-- ❌ Плохо: начинаем с большой таблицы
SELECT * 
FROM large_table l
INNER JOIN small_table s ON l.id = s.large_id
WHERE s.status = 'active';

-- ✅ Хорошо: начинаем с фильтрованной маленькой таблицы
SELECT * 
FROM small_table s
INNER JOIN large_table l ON s.large_id = l.id
WHERE s.status = 'active';
```

### 8.3 Избегайте N+1 queries

**❌ Плохо:**

```python
users = db.query("SELECT * FROM users")
for user in users:
    orders = db.query(f"SELECT * FROM orders WHERE user_id = {user.id}")
    # N+1 queries!
```

**✅ Хорошо:**

```python
# Один запрос с JOIN

result = db.query("""
    SELECT u.*, o.*
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
""")
```

### 8.4 Best Practices

**Рекомендации:**

- ✅ Использовать индексы для WHERE и JOIN
- ✅ Избегать SELECT *
- ✅ Использовать LIMIT для больших результатов
- ✅ Обновлять статистику (ANALYZE)
- ✅ Мониторить медленные запросы
- ✅ Использовать подготовленные запросы (prepared statements)
- ✅ Избегать функций в WHERE (если возможно)

---

## 9. Мониторинг производительности

### 9.1 Медленные запросы

**Найти медленные запросы (PostgreSQL):**

```sql
-- Включить логирование медленных запросов
-- В postgresql.conf:
log_min_duration_statement = 1000  -- Логировать запросы > 1 секунды

-- Просмотр логов
SELECT * FROM pg_stat_statements 
ORDER BY total_exec_time DESC 
LIMIT 10;
```

### 9.2 Статистика использования таблиц

```sql
-- Найти самые используемые таблицы
SELECT 
    schemaname,
    tablename,
    seq_scan,
    seq_tup_read,
    idx_scan,
    idx_tup_fetch,
    n_tup_ins,
    n_tup_upd,
    n_tup_del
FROM pg_stat_user_tables
ORDER BY seq_scan DESC;
```

### 9.3 Размер таблиц и индексов

```sql
-- Размер таблиц
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

### 9.4 Активные соединения

```sql
-- Количество активных соединений
SELECT 
    count(*) AS total_connections,
    count(*) FILTER (WHERE state = 'active') AS active,
    count(*) FILTER (WHERE state = 'idle') AS idle
FROM pg_stat_activity;
```

---

## 10. Настройки производительности

### 10.1 PostgreSQL настройки

**Основные параметры (postgresql.conf):**

```ini
# Память

shared_buffers = 256MB          # Кэш данных
work_mem = 4MB                   # Память для сортировки и JOIN
maintenance_work_mem = 64MB      # Память для обслуживания

# Проверка точек (checkpoints)

checkpoint_completion_target = 0.9
wal_buffers = 16MB

# Запросы

max_connections = 100
effective_cache_size = 1GB       # Оценка доступной памяти для кэша
```

### 10.2 MySQL настройки

**Основные параметры (my.cnf):**

```ini
[mysqld]
innodb_buffer_pool_size = 1G     # Кэш InnoDB
innodb_log_file_size = 256M
max_connections = 200
query_cache_size = 64M
```

---

## 11. Практические примеры оптимизации

### 11.1 Оптимизация отчёта

**Исходный запрос (медленный):**

```sql
SELECT 
    u.name,
    u.email,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_spent,
    AVG(o.amount) AS avg_order
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.name, u.email
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC
LIMIT 100;
```

**Оптимизация:**

```sql
-- 1. Индексы
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_amount ON orders(amount);

-- 2. Материализованное представление (если данные редко меняются)
CREATE MATERIALIZED VIEW active_user_stats AS
SELECT 
    u.id,
    u.name,
    u.email,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_spent,
    AVG(o.amount) AS avg_order
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.name, u.email
HAVING COUNT(o.id) > 5;

-- 3. Быстрый запрос
SELECT * FROM active_user_stats
ORDER BY total_spent DESC
LIMIT 100;
```

### 11.2 Оптимизация поиска

**Полнотекстовый поиск:**

```sql
-- Создание полнотекстового индекса
CREATE INDEX idx_users_name_gin ON users USING GIN (name gin_trgm_ops);

-- Быстрый поиск
SELECT * FROM users 
WHERE name ILIKE '%Иван%'
ORDER BY name;
```

---

## 💡 Key Takeaways

- **Причины медленных запросов**: отсутствие индексов, неэффективные запросы, большие таблицы

- **CPU/память/I/O**: I/O часто узкое место, используйте кэш и индексы

- **Партиционирование**: разделение больших таблиц на части для ускорения

- **Sharding**: горизонтальное разделение между базами данных для масштабирования

- **Оптимизация**: анализ планов, индексы, мониторинг

---

## 🚀 Next Steps

**Related Modules:**

- [18_System_Design](../18_System_Design/) — SQL как часть system design
- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов

**Practice Ideas:**

1. Найдите медленные запросы в вашей базе данных
2. Попрактикуйтесь с партиционированием
3. Сравните производительность с индексами и без
4. Изучите настройки производительности вашей СУБД

**Going Deeper:**

- Изучите настройки производительности PostgreSQL/MySQL
- Изучите мониторинг производительности
- Изучите стратегии масштабирования баз данных

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Performance](https://www.postgresql.org/docs/current/performance-tips.html) — советы по производительности
- [Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) — партиционирование

---



