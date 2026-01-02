# Планы выполнения запросов
## EXPLAIN, EXPLAIN ANALYZE, Seq Scan vs Index Scan, оптимизатор запросов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу SELECT запросов
- Знать, что такое индексы
- Иметь представление о производительности запросов

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [09_Indexes](../09_Indexes/) — Индексы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать EXPLAIN для анализа планов выполнения
- Применять EXPLAIN ANALYZE для реального времени выполнения
- Различать Seq Scan и Index Scan
- Понимать работу оптимизатора запросов
- Оптимизировать медленные запросы на основе планов

---

## 1. Что такое план выполнения

**План выполнения (Query Plan)** — это последовательность операций, которую СУБД использует для выполнения запроса.

### 1.1 Зачем нужен EXPLAIN

**EXPLAIN показывает:**

- Как СУБД планирует выполнить запрос
- Какие индексы будут использованы
- Оценку стоимости операций
- Порядок выполнения операций

**Пример:**

```sql
EXPLAIN SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Output:**
```
Seq Scan on users  (cost=0.00..25.00 rows=1 width=64)
  Filter: (email = 'ivan@example.com'::text)
```

---

## 2. EXPLAIN

### 2.1 Базовое использование

```sql
EXPLAIN SELECT * FROM users WHERE age > 25;
```

**Что показывает:**

- **cost** — оценка стоимости (startup..total)

- **rows** — оценка количества строк

- **width** — средний размер строки

### 2.2 Форматы вывода

**Текстовый формат (по умолчанию):**

```sql
EXPLAIN SELECT * FROM users;
```

**JSON формат:**

```sql
EXPLAIN (FORMAT JSON) SELECT * FROM users;
```

**Визуальный формат:**

```sql
EXPLAIN (FORMAT TEXT) SELECT * FROM users;
```

---

## 3. EXPLAIN ANALYZE

### 3.1 Реальное выполнение

**EXPLAIN ANALYZE** реально выполняет запрос и показывает фактические метрики:

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Output:**
```
Index Scan using idx_users_email on users  (cost=0.42..8.44 rows=1 width=64) (actual time=0.123..0.124 rows=1 loops=1)
  Index Cond: (email = 'ivan@example.com'::text)
Planning Time: 0.234 ms
Execution Time: 0.456 ms
```

**Метрики:**

- **actual time** — реальное время выполнения

- **rows** — фактическое количество строк

- **loops** — количество итераций

- **Planning Time** — время планирования

- **Execution Time** — время выполнения

### 3.2 Когда использовать

**EXPLAIN:**

- ✅ Быстро, не выполняет запрос
- ✅ Показывает план без реальных данных
- ✅ Безопасно для production

**EXPLAIN ANALYZE:**

- ✅ Показывает реальные метрики
- ⚠️ Реально выполняет запрос
- ⚠️ Может быть медленным

---

## 4. Seq Scan vs Index Scan

### 4.1 Seq Scan (Sequential Scan)

**Полное сканирование таблицы:**

```sql
EXPLAIN SELECT * FROM users WHERE name LIKE '%Иван%';
```

**Output:**
```
Seq Scan on users  (cost=0.00..25.00 rows=1000 width=64)
  Filter: (name ~~ '%Иван%'::text)
```

**Когда используется:**

- ✅ Нет подходящего индекса
- ✅ Нужно прочитать большую часть таблицы
- ✅ Индекс неэффективен (низкая селективность)

**Характеристики:**

- Читает все строки таблицы
- O(n) сложность
- Медленно на больших таблицах

### 4.2 Index Scan

**Использование индекса:**

```sql
CREATE INDEX idx_users_email ON users(email);
EXPLAIN SELECT * FROM users WHERE email = 'ivan@example.com';
```

**Output:**
```
Index Scan using idx_users_email on users  (cost=0.42..8.44 rows=1 width=64)
  Index Cond: (email = 'ivan@example.com'::text)
```

**Когда используется:**

- ✅ Есть подходящий индекс
- ✅ Высокая селективность условия
- ✅ Быстрый поиск

**Характеристики:**

- Использует индекс для поиска
- O(log n) сложность
- Быстро даже на больших таблицах

### 4.3 Index Only Scan

**Только индекс, без обращения к таблице:**

```sql
CREATE INDEX idx_users_email_name ON users(email, name);
EXPLAIN SELECT email, name FROM users WHERE email = 'ivan@example.com';
```

**Output:**
```
Index Only Scan using idx_users_email_name on users  (cost=0.42..4.44 rows=1 width=64)
  Index Cond: (email = 'ivan@example.com'::text)
```

**Преимущества:**

- ✅ Ещё быстрее (не читает таблицу)
- ✅ Меньше I/O операций

---

## 5. Оптимизатор запросов

### 5.1 Как работает оптимизатор

**Оптимизатор:**

1. Анализирует запрос
2. Рассматривает разные планы выполнения
3. Оценивает стоимость каждого плана
4. Выбирает самый дешёвый план

**Факторы стоимости:**

- Количество строк
- Размер данных
- Наличие индексов
- Статистика таблиц

### 5.2 Статистика

**Обновление статистики (PostgreSQL):**

```sql
ANALYZE users;  -- Обновить статистику для таблицы
```

**Статистика влияет на:**

- Выбор плана выполнения
- Оценку стоимости
- Использование индексов

---

## 6. Анализ медленных запросов

### 6.1 Типичные проблемы

**Проблема 1: Отсутствие индекса**

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ivan@example.com';
-- Seq Scan (медленно)

-- Решение: создать индекс
CREATE INDEX idx_users_email ON users(email);
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ivan@example.com';

-- Index Scan (быстро)
```

**Проблема 2: Неэффективный индекс**

```sql
-- Индекс не используется из-за функции
EXPLAIN SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';
-- Seq Scan

-- Решение: функциональный индекс
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
EXPLAIN SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';

-- Index Scan
```

### 6.2 Чтение плана выполнения

**Что искать:**

- **Seq Scan** на больших таблицах — возможно нужен индекс

- **Высокая стоимость** — запрос может быть медленным

- **Большая разница** между оценкой и реальностью — обновить статистику

### 6.3 Типичные проблемы и решения

**Проблема 3: Медленный JOIN**

```sql
EXPLAIN ANALYZE
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Результат показывает медленный Hash Join
-- Решение: индексы на ключах JOIN
CREATE INDEX idx_orders_user_id ON orders(user_id);
-- Теперь: быстрый Index Join
```

**Проблема 4: Медленная сортировка**

```sql
EXPLAIN ANALYZE
SELECT * FROM orders ORDER BY order_date DESC;

-- Результат: Sort (медленно)
-- Решение: индекс для сортировки
CREATE INDEX idx_orders_date_desc ON orders(order_date DESC);

-- Теперь: Index Scan (быстро, без сортировки)
```

---

## 7. Другие типы сканирования

### 7.1 Bitmap Scan

**Bitmap Scan** — комбинация индекса и таблицы:

```sql
EXPLAIN SELECT * FROM users WHERE age > 25 AND age < 35;
```

**Результат:**

```
Bitmap Heap Scan on users
  Recheck Cond: ((age > 25) AND (age < 35))

  -> Bitmap Index Scan on idx_users_age
      Index Cond: ((age > 25) AND (age < 35))
```

**Когда используется:**

- ✅ Несколько условий на индексированном столбце
- ✅ Средняя селективность (не очень селективно, но и не все строки)

### 7.2 Bitmap Index Scan

**Создание битовой карты из индекса:**

```sql
-- Bitmap Index Scan создаёт битовую карту строк
-- Затем Bitmap Heap Scan читает только нужные страницы
```

---

## 8. Типы JOIN в планах

### 8.1 Nested Loop Join

**Для маленьких таблиц:**

```sql
EXPLAIN
SELECT * FROM small_table s
INNER JOIN tiny_table t ON s.id = t.id;
```

**Результат:**

```
Nested Loop

  -> Seq Scan on small_table
  -> Index Scan on tiny_table
```

**Характеристики:**

- ✅ Хорош для маленьких таблиц
- ❌ Медленный для больших таблиц (O(n×m))

### 8.2 Hash Join

**Для больших таблиц без индексов:**

```sql
EXPLAIN
SELECT * FROM large_table1 l1
INNER JOIN large_table2 l2 ON l1.id = l2.id;
```

**Результат:**

```
Hash Join
  Hash Cond: (l1.id = l2.id)

  -> Seq Scan on large_table1
  -> Hash
      -> Seq Scan on large_table2
```

**Характеристики:**

- ✅ Эффективен для больших таблиц
- ✅ Строит хеш-таблицу для одной таблицы
- ❌ Требует память для хеш-таблицы

### 8.3 Merge Join

**Для отсортированных данных:**

```sql
EXPLAIN
SELECT * FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id
ORDER BY t1.id;
```

**Результат:**

```
Merge Join
  Merge Cond: (t1.id = t2.id)

  -> Index Scan on table1
  -> Index Scan on table2
```

**Характеристики:**

- ✅ Эффективен, когда данные отсортированы
- ✅ Не требует дополнительной памяти
- ❌ Требует сортировку или индексы

---

## 9. Настройки оптимизатора

### 9.1 Параметры стоимости

**Настройка стоимости операций (PostgreSQL):**

```sql
-- В postgresql.conf или для сессии
SET seq_page_cost = 1.0;      -- Стоимость чтения страницы (Seq Scan)
SET random_page_cost = 4.0;   -- Стоимость случайного чтения
SET cpu_tuple_cost = 0.01;    -- Стоимость обработки строки
SET cpu_index_tuple_cost = 0.005;  -- Стоимость обработки индекса
```

**Влияние на выбор плана:**

- Высокий `random_page_cost` → предпочтение Seq Scan
- Низкий `random_page_cost` → предпочтение Index Scan

### 9.2 effective_cache_size

**Оценка доступной памяти для кэша:**

```sql
SET effective_cache_size = '1GB';
```

**Влияние:**

- Оптимизатор учитывает размер кэша при выборе плана
- Большой кэш → предпочтение индексов

### 9.3 work_mem

**Память для сортировки и JOIN:**

```sql
SET work_mem = '64MB';
```

**Влияние:**

- Больше памяти → больше операций в памяти (быстрее)
- Меньше памяти → больше операций на диске (медленнее)

---

## 10. Профилирование запросов

### 10.1 pg_stat_statements

**Расширение для статистики запросов:**

```sql
-- Включить расширение
CREATE EXTENSION pg_stat_statements;

-- Просмотр статистики
SELECT 
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    max_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

### 10.2 АвтоОбъяснение (auto_explain)

**Автоматическое логирование планов:**

```sql
-- В postgresql.conf
shared_preload_libraries = 'auto_explain'
auto_explain.log_min_duration = 1000  -- Логировать запросы > 1 секунды
auto_explain.log_analyze = true
auto_explain.log_buffers = true
```

---

## 11. Практические примеры оптимизации

### 11.1 Оптимизация сложного запроса

**Исходный запрос:**

```sql
EXPLAIN ANALYZE
SELECT 
    u.name,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC;
```

**Проблемы:**

- Seq Scan на users
- Hash Join без индексов
- Медленная сортировка

**Оптимизация:**

```sql
-- Индексы
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_amount ON orders(amount);

-- Теперь план использует индексы
```

### 11.2 Анализ плана JOIN

**Сравнение планов:**

```sql
-- Без индексов
EXPLAIN SELECT * FROM users u JOIN orders o ON u.id = o.user_id;

-- Hash Join (медленно)

-- С индексами
CREATE INDEX idx_orders_user_id ON orders(user_id);
EXPLAIN SELECT * FROM users u JOIN orders o ON u.id = o.user_id;

-- Nested Loop с Index Scan (быстрее)
```

---

## 💡 Key Takeaways

- **EXPLAIN** показывает план выполнения без реального выполнения

- **EXPLAIN ANALYZE** реально выполняет запрос и показывает метрики

- **Seq Scan** — полное сканирование (медленно), **Index Scan** — использование индекса (быстро)

- **Оптимизатор** выбирает план на основе стоимости и статистики

- **Анализ планов** помогает находить и исправлять медленные запросы

---

## 🚀 Next Steps

**Related Modules:**

- [09_Indexes](../09_Indexes/) — Индексы для производительности
- [14_Performance](../14_Performance/) — Производительность и масштабирование

**Practice Ideas:**

1. Используйте EXPLAIN для анализа ваших запросов
2. Сравните планы с индексами и без
3. Найдите медленные запросы с EXPLAIN ANALYZE
4. Оптимизируйте запросы на основе планов

**Going Deeper:**

- Изучите другие типы сканирования (Bitmap Scan, Merge Join)
- Изучите настройки оптимизатора
- Изучите профилирование запросов

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) — документация EXPLAIN
- [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — использование EXPLAIN

---


