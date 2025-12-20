# Антипаттерны SQL
## SELECT *, N+1 queries, отсутствие индексов, сложные нечитаемые запросы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SQL
- Понимать работу с индексами
- Иметь представление о производительности запросов

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [09_Indexes](../09_Indexes/) — Индексы
- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Избегать антипаттернов SELECT *
- Понимать проблему N+1 queries и способы решения
- Создавать индексы для критичных запросов
- Писать читаемые и поддерживаемые SQL запросы
- Оптимизировать запросы, избегая антипаттернов

---

## 1. SELECT * — антипаттерн

### 1.1 Проблемы SELECT *

**❌ Проблемы:**

- ❌ Возвращает все столбцы, даже ненужные
- ❌ Медленнее (больше данных)
- ❌ Скрывает реальные зависимости
- ❌ Ломается при изменении структуры таблицы

**Пример:**

```sql

-- ❌ Плохо
SELECT * FROM users WHERE id = 1;

-- ✅ Хорошо
SELECT id, name, email FROM users WHERE id = 1;
```

### 1.2 Когда SELECT * допустим

**Допустимо в:**

- ✅ Интерактивных запросах для исследования
- ✅ Тестировании
- ✅ Когда действительно нужны все столбцы

**Не допустимо в:**

- ❌ Production коде
- ❌ API endpoints
- ❌ Приложениях

---

## 2. N+1 queries проблема

### 2.1 Что такое N+1 queries

**Проблема:** Выполнение множества запросов вместо одного.

**Пример:**

```sql

-- ❌ Плохо: N+1 queries
-- 1 запрос для пользователей
SELECT * FROM users;

-- Затем для каждого пользователя отдельный запрос
SELECT * FROM orders WHERE user_id = 1;
SELECT * FROM orders WHERE user_id = 2;
SELECT * FROM orders WHERE user_id = 3;
-- ... N запросов
```

**✅ Решение: один запрос с JOIN**

```sql

-- ✅ Хорошо: 1 запрос
SELECT 
    u.id,
    u.name,
    o.id AS order_id,
    o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### 2.2 В приложениях

**❌ Плохо (Python пример):**

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

---

## 3. Отсутствие индексов

### 3.1 Проблема

**❌ Без индексов:**

```sql

-- Seq Scan (медленно на больших таблицах)
SELECT * FROM users WHERE email = 'ivan@example.com';
```

**✅ С индексами:**

```sql

CREATE INDEX idx_users_email ON users(email);
-- Index Scan (быстро)
SELECT * FROM users WHERE email = 'ivan@example.com';
```

### 3.2 Где нужны индексы

**Создавайте индексы для:**

- ✅ Столбцов в WHERE (часто используемых)
- ✅ Внешних ключей (для JOIN)
- ✅ Столбцов в ORDER BY
- ✅ Уникальных столбцов

---

## 4. Сложные нечитаемые запросы

### 4.1 Проблема сложности

**❌ Плохо: слишком сложный запрос**

```sql

SELECT u.id, u.name, 
    (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id AND o.status = 'completed') AS completed_orders,
    (SELECT SUM(amount) FROM orders o WHERE o.user_id = u.id) AS total_spent,
    (SELECT AVG(amount) FROM orders o WHERE o.user_id = u.id AND o.order_date > CURRENT_DATE - INTERVAL '30 days') AS avg_recent
FROM users u
WHERE u.id IN (SELECT user_id FROM orders WHERE amount > 100)
AND EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.order_date > CURRENT_DATE - INTERVAL '7 days');
```

**✅ Хорошо: разбить на CTE**

```sql

WITH user_orders AS (
    SELECT 
        user_id,
        COUNT(*) FILTER (WHERE status = 'completed') AS completed_orders,
        SUM(amount) AS total_spent,
        AVG(amount) FILTER (WHERE order_date > CURRENT_DATE - INTERVAL '30 days') AS avg_recent
    FROM orders
    GROUP BY user_id
),
active_users AS (
    SELECT DISTINCT user_id
    FROM orders
    WHERE amount > 100
    AND order_date > CURRENT_DATE - INTERVAL '7 days'
)
SELECT 
    u.id,
    u.name,
    COALESCE(o.completed_orders, 0) AS completed_orders,
    COALESCE(o.total_spent, 0) AS total_spent,
    o.avg_recent
FROM users u
INNER JOIN active_users a ON u.id = a.user_id
LEFT JOIN user_orders o ON u.id = o.user_id;
```

### 4.2 Best Practices для читаемости

**Рекомендации:**

- ✅ Используйте CTE для сложных запросов
- ✅ Давайте понятные алиасы
- ✅ Форматируйте код (отступы, переносы строк)
- ✅ Комментируйте сложную логику
- ✅ Разбивайте на логические части

---

## 5. Другие антипаттерны

### 5.1 WHERE с функциями

**❌ Плохо:**

```sql

-- Индекс не используется
SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';
```

**✅ Хорошо:**

```sql

-- Функциональный индекс
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
SELECT * FROM users WHERE LOWER(email) = 'ivan@example.com';
```

### 5.2 LIKE с начальным %

**❌ Плохо:**

```sql

-- Индекс не используется
SELECT * FROM users WHERE email LIKE '%@example.com';
```

**✅ Хорошо:**

```sql

-- Если возможно, используйте префикс
SELECT * FROM users WHERE email LIKE 'user%@example.com';
-- Или полнотекстовый поиск
```

### 5.3 Неиспользование LIMIT

**❌ Плохо:**

```sql

-- Может вернуть миллионы строк
SELECT * FROM orders ORDER BY order_date;
```

**✅ Хорошо:**

```sql

-- Ограничение результата
SELECT * FROM orders ORDER BY order_date LIMIT 100;
```

### 5.4 Игнорирование NULL

**❌ Плохо:**

```sql

-- Может пропустить NULL значения
SELECT * FROM users WHERE age != 25;
```

**✅ Хорошо:**

```sql

-- Явная обработка NULL
SELECT * FROM users WHERE age IS NULL OR age != 25;
```

---

## 6. Производительность

### 6.1 Медленные JOIN

**❌ Плохо:**

```sql

-- CROSS JOIN на больших таблицах
SELECT * FROM users CROSS JOIN orders;
```

**✅ Хорошо:**

```sql

-- Правильные JOIN с условиями
SELECT * FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 6.2 Избыточные подзапросы

**❌ Плохо:**

```sql

SELECT 
    (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS orders_count,
    (SELECT SUM(amount) FROM orders WHERE user_id = u.id) AS total
FROM users u;
```

**✅ Хорошо:**

```sql

SELECT 
    u.id,
    COUNT(o.id) AS orders_count,
    SUM(o.amount) AS total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

### 6.3 Неоптимальные агрегаты

**❌ Плохо:**

```sql

SELECT 
    user_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > (
    SELECT AVG(order_count) 
    FROM (
        SELECT COUNT(*) AS order_count 
        FROM orders 
        GROUP BY user_id
    ) sub
);
```

**✅ Хорошо:**

```sql

WITH user_order_counts AS (
    SELECT user_id, COUNT(*) AS order_count
    FROM orders
    GROUP BY user_id
)
SELECT user_id, order_count
FROM user_order_counts
WHERE order_count > (SELECT AVG(order_count) FROM user_order_counts);
```

---

## 7. Антипаттерны с NULL

### 7.1 NOT IN с NULL

**❌ Проблема:**

```sql

-- Если подзапрос вернёт NULL, результат может быть пустым
SELECT * FROM users
WHERE id NOT IN (SELECT user_id FROM orders);
-- Если user_id содержит NULL, результат пустой!
```

**✅ Решение:**

```sql

-- Используйте NOT EXISTS
SELECT * FROM users u
WHERE NOT EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id
);
```

### 7.2 Сравнение с NULL

**❌ Плохо:**

```sql

SELECT * FROM users WHERE email = NULL;  -- Не работает!
SELECT * FROM users WHERE email != NULL;  -- Не работает!
```

**✅ Хорошо:**

```sql

SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

### 7.3 Агрегаты и NULL

**Проблема с COUNT:**

```sql

-- COUNT(*) считает все строки, включая NULL
SELECT COUNT(*) FROM users;  -- Все строки

-- COUNT(column) не считает NULL
SELECT COUNT(email) FROM users;  -- Только строки с email
```

---

## 8. Антипаттерны с датами

### 8.1 Функции в WHERE

**❌ Плохо:**

```sql

-- Индекс не используется
SELECT * FROM orders 
WHERE DATE(order_date) = '2024-01-01';
```

**✅ Хорошо:**

```sql

-- Использует индекс
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2024-01-02';
```

### 8.2 Сравнение дат

**❌ Плохо:**

```sql

-- Может не использовать индекс
SELECT * FROM orders 
WHERE EXTRACT(YEAR FROM order_date) = 2024;
```

**✅ Хорошо:**

```sql

-- Использует индекс
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';
```

---

## 9. Антипаттерны с агрегатами

### 9.1 Агрегаты в WHERE

**❌ Плохо:**

```sql

-- Ошибка: агрегаты нельзя использовать в WHERE
SELECT user_id, COUNT(*) 
FROM orders 
WHERE COUNT(*) > 5
GROUP BY user_id;
```

**✅ Хорошо:**

```sql

-- Используйте HAVING
SELECT user_id, COUNT(*) 
FROM orders 
GROUP BY user_id
HAVING COUNT(*) > 5;
```

### 9.2 DISTINCT с агрегатами

**❌ Избыточный DISTINCT:**

```sql

-- DISTINCT не нужен, GROUP BY уже обеспечивает уникальность
SELECT DISTINCT user_id, COUNT(*)
FROM orders
GROUP BY user_id;
```

**✅ Хорошо:**

```sql

SELECT user_id, COUNT(*)
FROM orders
GROUP BY user_id;
```

---

## 10. Антипаттерны с JOIN

### 10.1 Неявные JOIN (старый синтаксис)

**❌ Плохо:**

```sql

-- Старый синтаксис, не рекомендуется
SELECT * 
FROM users u, orders o
WHERE u.id = o.user_id;
```

**✅ Хорошо:**

```sql

-- Явный JOIN
SELECT * 
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 10.2 CROSS JOIN по ошибке

**❌ Плохо:**

```sql

-- Забыли условие JOIN
SELECT * 
FROM users u
JOIN orders o;  -- CROSS JOIN! Огромное количество строк
```

**✅ Хорошо:**

```sql

SELECT * 
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

---

## 11. Антипаттерны производительности

### 11.1 Отсутствие индексов на внешних ключах

**❌ Плохо:**

```sql

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
-- Нет индекса на user_id!

-- Медленный JOIN
SELECT * FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**✅ Хорошо:**

```sql

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX idx_orders_user_id ON orders(user_id);  -- Индекс!
```

### 11.2 Избыточные вычисления

**❌ Плохо:**

```sql

-- Вычисление повторяется для каждой строки
SELECT 
    name,
    LENGTH(name) AS name_length,
    LENGTH(name) * 2 AS double_length
FROM users;
```

**✅ Хорошо:**

```sql

-- Вычисление один раз
SELECT 
    name,
    name_length,
    name_length * 2 AS double_length
FROM (
    SELECT name, LENGTH(name) AS name_length
    FROM users
) sub;
```

---

## 12. Антипаттерны читаемости

### 12.1 Отсутствие форматирования

**❌ Плохо:**

```sql

SELECT u.id,u.name,o.amount FROM users u JOIN orders o ON u.id=o.user_id WHERE u.age>25 ORDER BY o.amount DESC;
```

**✅ Хорошо:**

```sql

SELECT 
    u.id,
    u.name,
    o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE u.age > 25
ORDER BY o.amount DESC;
```

### 12.2 Непонятные алиасы

**❌ Плохо:**

```sql

SELECT 
    u.id AS a,
    u.name AS b,
    o.amount AS c
FROM users u
JOIN orders o ON u.id = o.user_id;
```

**✅ Хорошо:**

```sql

SELECT 
    u.id AS user_id,
    u.name AS user_name,
    o.amount AS order_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 12.3 Отсутствие комментариев

**❌ Плохо:**

```sql

-- Сложная логика без объяснений
SELECT ... FROM ... WHERE ...;
```

**✅ Хорошо:**

```sql

-- Найти пользователей с заказами больше среднего
-- Используем подзапрос для вычисления среднего
WITH avg_order AS (
    SELECT AVG(amount) AS avg_amount FROM orders
)
SELECT u.*, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
CROSS JOIN avg_order ao
WHERE o.amount > ao.avg_amount;
```

---

## 13. Обнаружение антипаттернов

### 13.1 Автоматические проверки

**SQL linting инструменты:**

- **sqlfluff** — форматирование и проверка SQL

- **sqlcheck** — обнаружение антипаттернов

- **pg_stat_statements** — поиск медленных запросов

### 13.2 Code Review чеклист

**Что проверять:**

- ✅ Нет SELECT *
- ✅ Нет N+1 queries
- ✅ Есть индексы на внешних ключах
- ✅ Нет функций в WHERE (если возможно)
- ✅ Используется LIMIT для больших результатов
- ✅ Запросы читаемы и отформатированы

---

## 💡 Key Takeaways

- **SELECT *** — антипаттерн в production, указывайте конкретные столбцы

- **N+1 queries** — выполняйте один запрос с JOIN вместо множества

- **Индексы** — создавайте для часто используемых столбцов в WHERE и JOIN

- **Читаемость** — используйте CTE, форматирование, комментарии

- **Производительность** — избегайте функций в WHERE, используйте LIMIT, правильные JOIN

---

## 🚀 Next Steps

**Related Modules:**

- [18_System_Design](../18_System_Design/) — SQL как часть system design
- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов

**Practice Ideas:**

1. Найдите антипаттерны в вашем коде
2. Рефакторите сложные запросы с использованием CTE
3. Оптимизируйте N+1 queries
4. Создайте индексы для критичных запросов

**Going Deeper:**

- Изучите профилирование запросов
- Изучите автоматическое обнаружение антипаттернов
- Изучите best practices для вашей СУБД

---

## 📚 Additional Resources

**Documentation:**

- [SQL Antipatterns Book](https://pragprog.com/titles/bksqla/sql-antipatterns/) — книга об антипаттернах
- [PostgreSQL Performance](https://www.postgresql.org/docs/current/performance-tips.html) — советы по производительности

---


