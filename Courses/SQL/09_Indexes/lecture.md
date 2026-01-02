# Индексы
## Назначение индексов, B-tree индексы, Hash индексы, компромиссы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать структуру таблиц и работу SELECT запросов
- Знать базовые концепции производительности
- Иметь представление о том, как СУБД выполняет запросы

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать назначение индексов и как они ускоряют запросы
- Различать типы индексов (B-tree, Hash)
- Создавать индексы для оптимизации запросов
- Понимать компромиссы использования индексов
- Выбирать правильные столбцы для индексации

---

## 1. Что такое индексы

### 1.1 Аналогия с книгой

**Индекс в базе данных** похож на алфавитный указатель в книге:

- Без индекса: нужно просмотреть все страницы (полное сканирование)
- С индексом: сразу находим нужную страницу (быстрый поиск)

### 1.2 Зачем нужны индексы

**Индексы ускоряют:**

- ✅ Поиск по условию WHERE
- ✅ JOIN операции
- ✅ Сортировку (ORDER BY)
- ✅ Группировку (GROUP BY)

**Пример:**

```sql
-- Без индекса: полное сканирование таблицы (Seq Scan)
SELECT * FROM users WHERE email = 'ivan@example.com';
-- Время: O(n) — нужно проверить все строки

-- С индексом: быстрый поиск (Index Scan)
CREATE INDEX idx_users_email ON users(email);
SELECT * FROM users WHERE email = 'ivan@example.com';
-- Время: O(log n) — бинарный поиск по индексу
```

---

## 2. B-tree индексы

### 2.1 Что такое B-tree

**B-tree (B-дерево)** — сбалансированное дерево поиска, наиболее распространённый тип индекса.

**Структура:**

```
        [50]
       /    \
    [25]    [75]
   /   \    /   \
[10] [30] [60] [90]
```

**Преимущества:**

- ✅ Логарифмическое время поиска O(log n)
- ✅ Поддерживает диапазонные запросы (BETWEEN, >, <)
- ✅ Поддерживает сортировку
- ✅ Эффективен для большинства случаев

### 2.2 Создание B-tree индекса

```sql
-- Простой индекс
CREATE INDEX idx_users_email ON users(email);

-- Составной индекс (несколько столбцов)
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- Уникальный индекс
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);
```

### 2.3 Когда использовать B-tree

**B-tree подходит для:**

- ✅ Равенство (=)
- ✅ Диапазоны (>, <, BETWEEN)
- ✅ Сортировка (ORDER BY)
- ✅ Префиксы строк (LIKE 'prefix%')

**Не подходит для:**

- ❌ Поиск по шаблону (LIKE '%suffix')
- ❌ Полнотекстовый поиск

---

## 3. Hash индексы

### 3.1 Что такое Hash индекс

**Hash индекс** использует хеш-таблицу для быстрого поиска по равенству.

**Особенности:**

- ✅ O(1) время поиска по равенству
- ❌ Не поддерживает диапазоны
- ❌ Не поддерживает сортировку
- ❌ Только для оператора =

### 3.2 Создание Hash индекса

```sql
-- PostgreSQL
CREATE INDEX idx_users_email_hash ON users USING HASH (email);
```

**Когда использовать:**

- ✅ Только поиск по равенству
- ✅ Очень большие таблицы
- ✅ Частые запросы WHERE column = value

---

## 4. Компромиссы индексов

### 4.1 Преимущества

**Индексы ускоряют:**

- Поиск данных
- JOIN операции
- Сортировку и группировку

### 4.2 Недостатки

**Индексы замедляют:**

- ❌ INSERT — нужно обновлять индекс
- ❌ UPDATE — нужно обновлять индекс
- ❌ DELETE — нужно обновлять индекс
- ❌ Занимают место на диске

**Пример:**

```sql
-- Без индекса: быстрая вставка
INSERT INTO users (name, email) VALUES ('Новый', 'new@example.com');
-- Время: O(1)

-- С индексом: медленнее вставка
CREATE INDEX idx_users_email ON users(email);
INSERT INTO users (name, email) VALUES ('Новый', 'new@example.com');
-- Время: O(log n) — нужно обновить индекс
```

### 4.3 Когда создавать индексы

**Создавайте индексы для:**

- ✅ Столбцов в WHERE (часто используемых)
- ✅ Внешних ключей (для JOIN)
- ✅ Столбцов в ORDER BY
- ✅ Уникальных столбцов (email, username)

**Не создавайте для:**

- ❌ Столбцов, редко используемых в WHERE
- ❌ Столбцов с низкой селективностью (пол, статус)
- ❌ Маленьких таблиц (< 1000 строк)

---

## 5. Составные индексы

### 5.1 Порядок столбцов важен

**Правило левого префикса:**

```sql
-- Индекс: (user_id, order_date)
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- ✅ Использует индекс
SELECT * FROM orders WHERE user_id = 1;
SELECT * FROM orders WHERE user_id = 1 AND order_date = '2024-01-01';

-- ❌ НЕ использует индекс (нет user_id)
SELECT * FROM orders WHERE order_date = '2024-01-01';
```

**Порядок важен!** Ставьте более селективные столбцы первыми.

### 5.2 Выбор порядка

```sql
-- Если user_id более селективен (меньше значений на user_id)
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- Если order_date более селективен
CREATE INDEX idx_orders_date_user ON orders(order_date, user_id);
```

---

## 6. Частичные индексы

### 6.1 Индексы с условием

**Частичный индекс** создаётся только для части данных:

```sql
-- Индекс только для активных пользователей
CREATE INDEX idx_users_active_email ON users(email)
WHERE is_active = true;
```

**Преимущества:**

- ✅ Меньше размер
- ✅ Быстрее обновление
- ✅ Эффективен для фильтрованных запросов

---

## 7. Функциональные индексы

### 7.1 Индексы на выражениях

**Функциональный индекс** создаётся на результате выражения, а не на столбце.

**Пример: поиск по нижнему регистру**

```sql
-- Проблема: индекс не используется
SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';
-- Seq Scan (медленно)

-- Решение: функциональный индекс
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';
-- Index Scan (быстро)
```

### 7.2 Индексы на вычисляемых столбцах

```sql
-- Индекс на вычисляемом столбце
CREATE TABLE orders (
    id INTEGER,
    amount DECIMAL(10, 2),
    tax_rate DECIMAL(5, 2),
    total_amount DECIMAL(10, 2) GENERATED ALWAYS AS (amount * (1 + tax_rate)) STORED
);

CREATE INDEX idx_orders_total ON orders(total_amount);
```

### 7.3 Индексы на датах

```sql
-- Индекс на части даты
CREATE INDEX idx_orders_year ON orders(EXTRACT(YEAR FROM order_date));
CREATE INDEX idx_orders_month ON orders(EXTRACT(MONTH FROM order_date));

-- Поиск по году
SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2024;
-- Использует индекс idx_orders_year
```

---

## 8. Покрывающие индексы (Covering Indexes)

### 8.1 Что такое покрывающий индекс

**Покрывающий индекс** содержит все данные, необходимые для запроса, без обращения к таблице.

**Пример:**

```sql
-- Обычный индекс
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Запрос требует обращения к таблице
SELECT user_id, amount FROM orders WHERE user_id = 1;
-- Index Scan + Heap Fetch (читает таблицу)

-- Покрывающий индекс (включает amount)
CREATE INDEX idx_orders_user_amount ON orders(user_id, amount);

-- Теперь запрос использует только индекс
SELECT user_id, amount FROM orders WHERE user_id = 1;
-- Index Only Scan (не читает таблицу!)
```

### 8.2 Преимущества покрывающих индексов

- ✅ Index Only Scan — быстрее
- ✅ Меньше I/O операций
- ✅ Эффективен для часто используемых запросов

---

## 9. Уникальные индексы и ограничения

### 9.1 UNIQUE индекс

**UNIQUE индекс** гарантирует уникальность значений:

```sql
-- Создание уникального индекса
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Попытка вставить дубликат
INSERT INTO users (email) VALUES ('ivan@example.com');
-- ✅ Успешно

INSERT INTO users (email) VALUES ('ivan@example.com');
-- ❌ Ошибка: duplicate key value violates unique constraint
```

### 9.2 UNIQUE vs PRIMARY KEY

**Различия:**

- PRIMARY KEY — только один на таблицу, NOT NULL
- UNIQUE — может быть несколько, может содержать NULL

```sql
-- PRIMARY KEY
CREATE TABLE users (
    id INTEGER PRIMARY KEY,  -- Автоматически создаёт уникальный индекс
    email VARCHAR(100)
);

-- UNIQUE индекс
CREATE UNIQUE INDEX idx_users_email ON users(email);
```

---

## 10. Индексы для JOIN

### 10.1 Индексы на внешних ключах

**Внешние ключи часто используются в JOIN:**

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Создайте индекс на внешнем ключе
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- JOIN будет быстрее
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 10.2 Множественные JOIN

```sql
-- Индексы для всех ключей JOIN
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_product_id ON orders(product_id);
CREATE INDEX idx_products_category_id ON products(category_id);

-- Сложный JOIN использует все индексы
SELECT 
    u.name,
    p.name,
    c.name,
    o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN products p ON o.product_id = p.id
INNER JOIN categories c ON p.category_id = c.id;
```

---

## 11. Индексы для сортировки

### 11.1 ORDER BY с индексом

**Индекс может использоваться для сортировки:**

```sql
-- Без индекса: сортировка в памяти
SELECT * FROM users ORDER BY email;
-- Sort (медленно на больших таблицах)

-- С индексом: уже отсортировано
CREATE INDEX idx_users_email ON users(email);
SELECT * FROM users ORDER BY email;
-- Index Scan (быстро, без сортировки)
```

### 11.2 ORDER BY с несколькими столбцами

```sql
-- Составной индекс для сортировки
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);

-- Использует индекс для сортировки
SELECT * FROM orders 
WHERE user_id = 1 
ORDER BY order_date DESC;
-- Index Scan (быстро)
```

---

## 12. Мониторинг индексов

### 12.1 EXPLAIN для проверки

```sql
-- Проверить, используется ли индекс
EXPLAIN SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Результат:**

```
Index Scan using idx_users_email on users
  Index Cond: (email = 'ivan@example.com')
```

**Если индекс не используется:**

```
Seq Scan on users
  Filter: (email = 'ivan@example.com')
```

### 12.2 EXPLAIN ANALYZE для реальных метрик

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Результат:**

```
Index Scan using idx_users_email on users
  (cost=0.42..8.44 rows=1 width=64)
  (actual time=0.123..0.124 rows=1 loops=1)
  Index Cond: (email = 'ivan@example.com')
Planning Time: 0.234 ms
Execution Time: 0.456 ms
```

### 12.3 Неиспользуемые индексы

**Найти неиспользуемые индексы (PostgreSQL):**

```sql
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan AS times_used,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;
```

**Удаление неиспользуемых индексов:**

```sql
-- Проверьте, что индекс действительно не используется
-- Затем удалите
DROP INDEX idx_unused_index;
```

### 12.4 Размер индексов

**Проверить размер индексов:**

```sql
SELECT 
    schemaname,
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size,
    pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) AS table_size
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;
```

---

## 13. Практические примеры

### 13.1 Оптимизация запроса пользователей

**Исходный запрос (медленный):**

```sql
SELECT * FROM users 
WHERE email LIKE '%@example.com' 
ORDER BY created_at DESC 
LIMIT 10;
-- Seq Scan + Sort (медленно)
```

**Оптимизация:**

```sql
-- Индекс для сортировки
CREATE INDEX idx_users_created_at ON users(created_at DESC);

-- Если нужен поиск по домену, используйте другой подход
CREATE INDEX idx_users_email_domain ON users(SUBSTRING(email FROM '@(.*)$'));

-- Или полнотекстовый поиск
CREATE INDEX idx_users_email_gin ON users USING GIN (email gin_trgm_ops);
```

### 13.2 Оптимизация аналитического запроса

```sql
-- Запрос: статистика по пользователям
SELECT 
    u.country,
    COUNT(DISTINCT o.id) AS order_count,
    SUM(o.amount) AS total_revenue
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.country
ORDER BY total_revenue DESC;

-- Индексы для оптимизации
CREATE INDEX idx_users_country_created ON users(country, created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_amount ON orders(amount);
```

### 13.3 Оптимизация поиска

```sql
-- Поиск пользователей по имени
SELECT * FROM users 
WHERE name ILIKE '%Иван%' 
ORDER BY name;

-- Проблема: ILIKE с % в начале не использует индекс

-- Решение 1: полнотекстовый поиск
CREATE INDEX idx_users_name_gin ON users USING GIN (name gin_trgm_ops);
SELECT * FROM users 
WHERE name ILIKE '%Иван%'
ORDER BY name;

-- Решение 2: поиск по префиксу (если возможно)
SELECT * FROM users 
WHERE name LIKE 'Иван%'  -- Индекс используется
ORDER BY name;
```

---

## 14. Частые ошибки

### 14.1 Слишком много индексов

**❌ Проблема:**

```sql
-- Создание индекса на каждом столбце
CREATE INDEX idx_users_id ON users(id);
CREATE INDEX idx_users_name ON users(name);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_age ON users(age);
CREATE INDEX idx_users_country ON users(country);
-- ... и так далее
```

**Проблемы:**

- ❌ Замедляет INSERT/UPDATE/DELETE
- ❌ Занимает много места
- ❌ Не все индексы используются

**✅ Решение:**

Создавайте индексы только для часто используемых столбцов в WHERE и JOIN.

### 14.2 Неправильный порядок в составных индексах

**❌ Плохо:**

```sql
-- Низкая селективность первой
CREATE INDEX idx_orders_status_user ON orders(status, user_id);
-- status имеет мало значений (pending, completed, cancelled)

-- Запрос
SELECT * FROM orders WHERE user_id = 1;
-- Индекс может не использоваться эффективно
```

**✅ Хорошо:**

```sql
-- Высокая селективность первой
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
-- user_id имеет много уникальных значений

-- Запрос
SELECT * FROM orders WHERE user_id = 1;
-- Индекс используется эффективно
```

### 14.3 Индексы на маленьких таблицах

**❌ Не нужно:**

```sql
-- Таблица с 100 строками
CREATE TABLE small_table (id INTEGER, name VARCHAR(100));
CREATE INDEX idx_small_name ON small_table(name);  -- Избыточно
```

**На маленьких таблицах** полное сканирование может быть быстрее, чем использование индекса.

---

## 💡 Key Takeaways

- **Индексы** ускоряют поиск, но замедляют вставку/обновление

- **B-tree** — универсальный тип, поддерживает диапазоны и сортировку

- **Hash** — только для равенства, очень быстрый

- **Составные индексы** — порядок столбцов важен (правило левого префикса)

- **Создавайте индексы** для часто используемых столбцов в WHERE и JOIN

---

## 🚀 Next Steps

**Related Modules:**

- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов
- [14_Performance](../14_Performance/) — Производительность и масштабирование

**Practice Ideas:**

1. Создайте индексы для ваших таблиц
2. Используйте EXPLAIN для проверки использования индексов
3. Сравните производительность с индексами и без
4. Найдите неиспользуемые индексы

**Going Deeper:**

- Изучите GIN, GiST индексы (PostgreSQL)
- Изучите покрывающие индексы (covering indexes)
- Изучите статистику использования индексов

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Indexes](https://www.postgresql.org/docs/current/indexes.html) — документация по индексам
- [Index Types](https://www.postgresql.org/docs/current/indexes-types.html) — типы индексов

---


