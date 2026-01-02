# CTE и рекурсивные запросы
## WITH, читаемость SQL, рекурсивные CTE, иерархические данные

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать работу с подзапросами
- Иметь представление о JOIN

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [07_Subqueries](../07_Subqueries/) — Подзапросы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать CTE (Common Table Expressions) для улучшения читаемости
- Создавать рекурсивные CTE для иерархических данных
- Применять множественные CTE в одном запросе
- Заменять сложные подзапросы на CTE
- Решать задачи с иерархическими структурами

---

## 1. Введение в CTE

### 1.1 Что такое CTE

**CTE (Common Table Expression)** — именованное временное выражение, существующее только в рамках одного запроса.

**Синтаксис:**

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT ... FROM cte_name;
```

**Преимущества:**

- ✅ Улучшает читаемость сложных запросов
- ✅ Можно использовать несколько раз в запросе
- ✅ Альтернатива подзапросам и временным таблицам

### 1.2 Простой пример

**Без CTE (подзапрос):**

```sql
SELECT * FROM (
    SELECT user_id, SUM(amount) AS total
    FROM orders
    GROUP BY user_id
) user_totals
WHERE total > 1000;
```

**С CTE (читаемее):**

```sql
WITH user_totals AS (
    SELECT user_id, SUM(amount) AS total
    FROM orders
    GROUP BY user_id
)
SELECT * FROM user_totals
WHERE total > 1000;
```

---

## 2. Множественные CTE

### 2.1 Несколько CTE в одном запросе

```sql
WITH 
    active_users AS (
        SELECT id, name FROM users WHERE is_active = true
    ),
    user_orders AS (
        SELECT user_id, COUNT(*) AS orders_count
        FROM orders
        GROUP BY user_id
    )
SELECT 
    u.name,
    COALESCE(o.orders_count, 0) AS orders_count
FROM active_users u
LEFT JOIN user_orders o ON u.id = o.user_id;
```

**Преимущества:**

- ✅ Логическое разделение этапов запроса
- ✅ Легче читать и понимать
- ✅ Можно переиспользовать CTE

---

## 3. Рекурсивные CTE

### 3.1 Синтаксис рекурсивного CTE

**Рекурсивный CTE состоит из двух частей:**

1. **Anchor (якорь)** — базовый случай
2. **Recursive (рекурсивная)** — рекурсивная часть

```sql
WITH RECURSIVE cte_name AS (
    -- Anchor: базовый случай
    SELECT ...
    UNION ALL
    -- Recursive: рекурсивная часть
    SELECT ... FROM cte_name WHERE ...
)
SELECT * FROM cte_name;
```

### 3.2 Пример: числа от 1 до 10

```sql
WITH RECURSIVE numbers AS (
    -- Anchor: начинаем с 1
    SELECT 1 AS n
    UNION ALL
    -- Recursive: добавляем 1, пока не достигнем 10
    SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT * FROM numbers;
```

**Output:**
```
n
--
1
2
3
...
10
```

---

## 4. Иерархические данные

### 4.1 Структура сотрудников

**Таблица с иерархией:**

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

INSERT INTO employees VALUES
    (1, 'CEO', NULL),
    (2, 'Manager A', 1),
    (3, 'Manager B', 1),
    (4, 'Employee 1', 2),
    (5, 'Employee 2', 2),
    (6, 'Employee 3', 3);
```

### 4.2 Найти всех подчинённых

**Рекурсивный CTE для иерархии:**

```sql
WITH RECURSIVE subordinates AS (
    -- Anchor: начальный менеджер
    SELECT id, name, manager_id, 0 AS level
    FROM employees
    WHERE id = 2  -- Manager A
    
    UNION ALL
    
    -- Recursive: все подчинённые
    SELECT e.id, e.name, e.manager_id, s.level + 1
    FROM employees e
    INNER JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates;
```

**Output:**
```
id | name      | manager_id | level
---+-----------+------------+-------
2  | Manager A | 1          | 0
4  | Employee 1| 2          | 1
5  | Employee 2| 2          | 1
```

### 4.3 Найти всех начальников

**Путь от сотрудника к CEO:**

```sql
WITH RECURSIVE managers AS (
    -- Anchor: начальный сотрудник
    SELECT id, name, manager_id, 0 AS level
    FROM employees
    WHERE id = 4  -- Employee 1
    
    UNION ALL
    
    -- Recursive: все начальники
    SELECT e.id, e.name, e.manager_id, m.level + 1
    FROM employees e
    INNER JOIN managers m ON e.id = m.manager_id
)
SELECT * FROM managers ORDER BY level;
```

---

## 5. Практические примеры

### 5.1 Замена сложных подзапросов

**Сложный запрос с подзапросами:**

```sql
SELECT 
    u.name,
    (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS orders_count,
    (SELECT SUM(amount) FROM orders o WHERE o.user_id = u.id) AS total_spent
FROM users u;
```

**С CTE (читаемее):**

```sql
WITH user_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS orders_count,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY user_id
)
SELECT 
    u.name,
    COALESCE(s.orders_count, 0) AS orders_count,
    COALESCE(s.total_spent, 0) AS total_spent
FROM users u
LEFT JOIN user_stats s ON u.id = s.user_id;
```

### 5.2 Многоэтапные вычисления

```sql
WITH 
    daily_sales AS (
        SELECT 
            DATE(order_date) AS sale_date,
            SUM(amount) AS daily_total
        FROM orders
        GROUP BY DATE(order_date)
    ),
    weekly_totals AS (
        SELECT 
            sale_date,
            daily_total,
            SUM(daily_total) OVER (
                ORDER BY sale_date 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS weekly_total
        FROM daily_sales
    )
SELECT * FROM weekly_totals
WHERE weekly_total > 10000;
```

---

## 6. Ограничения рекурсивных CTE

### 6.1 Защита от бесконечной рекурсии

**PostgreSQL ограничивает глубину рекурсии:**

```sql
-- По умолчанию: 100 уровней
SET max_recursion_depth = 1000;  -- Изменить лимит
```

**Защита в запросе:**

```sql
WITH RECURSIVE hierarchy AS (
    SELECT id, name, manager_id, 0 AS level
    FROM employees WHERE id = 1
    
    UNION ALL
    
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    INNER JOIN hierarchy h ON e.manager_id = h.id
    WHERE h.level < 10  -- Ограничение глубины
)
SELECT * FROM hierarchy;
```

---

## 7. CTE для обновления данных

### 7.1 UPDATE с CTE

**Обновление на основе CTE:**

```sql
WITH user_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS order_count,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY user_id
)
UPDATE users
SET 
    last_order_count = us.order_count,
    last_total_spent = us.total_spent
FROM user_stats us
WHERE users.id = us.user_id;
```

### 7.2 DELETE с CTE

**Удаление на основе CTE:**

```sql
WITH inactive_users AS (
    SELECT id
    FROM users
    WHERE last_login < CURRENT_DATE - INTERVAL '1 year'
    AND NOT EXISTS (
        SELECT 1 FROM orders 
        WHERE user_id = users.id 
        AND order_date > CURRENT_DATE - INTERVAL '1 year'
    )
)
DELETE FROM users
WHERE id IN (SELECT id FROM inactive_users);
```

### 7.3 INSERT с CTE

**Вставка на основе CTE:**

```sql
WITH new_orders AS (
    SELECT 
        user_id,
        product_id,
        amount,
        CURRENT_TIMESTAMP AS order_date
    FROM cart_items
    WHERE user_id = 123
)
INSERT INTO orders (user_id, product_id, amount, order_date)
SELECT * FROM new_orders;
```

---

## 8. Материализация CTE

### 8.1 MATERIALIZED CTE (PostgreSQL 12+)

**Принудительная материализация:**

```sql
WITH MATERIALIZED expensive_cte AS (
    SELECT 
        user_id,
        COUNT(*) AS order_count,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY user_id
    -- Дорогая операция
)
SELECT * FROM expensive_cte
WHERE order_count > 10;
```

**Преимущества:**

- ✅ CTE вычисляется один раз
- ✅ Результат кэшируется
- ✅ Полезно, когда CTE используется несколько раз

### 8.2 Когда материализировать

**Материализуйте когда:**

- ✅ CTE используется несколько раз в запросе
- ✅ CTE содержит дорогие вычисления
- ✅ CTE большой по размеру

**Не материализуйте когда:**

- ❌ CTE используется один раз
- ❌ CTE маленький
- ❌ Нужна актуальность данных

---

## 9. Рекурсивные CTE для графов

### 9.1 Поиск путей в графе

**Найти все пути между узлами:**

```sql
CREATE TABLE graph (
    from_node INTEGER,
    to_node INTEGER,
    weight INTEGER
);

INSERT INTO graph VALUES
    (1, 2, 10),
    (2, 3, 20),
    (1, 3, 30),
    (3, 4, 15);

-- Найти все пути от узла 1
WITH RECURSIVE paths AS (
    -- Anchor: начальный узел
    SELECT 
        from_node AS start_node,
        to_node AS end_node,
        ARRAY[from_node, to_node] AS path,
        weight AS total_weight,
        1 AS depth
    FROM graph
    WHERE from_node = 1
    
    UNION ALL
    
    -- Recursive: продолжение пути
    SELECT 
        p.start_node,
        g.to_node,
        p.path || g.to_node,
        p.total_weight + g.weight,
        p.depth + 1
    FROM paths p
    INNER JOIN graph g ON p.end_node = g.from_node
    WHERE NOT g.to_node = ANY(p.path)  -- Избегаем циклов
    AND p.depth < 10  -- Ограничение глубины
)
SELECT * FROM paths;
```

### 9.2 Поиск кратчайшего пути

**Найти кратчайший путь:**

```sql
WITH RECURSIVE shortest_path AS (
    SELECT 
        from_node,
        to_node,
        weight,
        ARRAY[from_node] AS path,
        0 AS total_weight
    FROM graph
    WHERE from_node = 1
    
    UNION ALL
    
    SELECT 
        sp.from_node,
        g.to_node,
        g.weight,
        sp.path || g.to_node,
        sp.total_weight + g.weight
    FROM shortest_path sp
    INNER JOIN graph g ON sp.to_node = g.from_node
    WHERE NOT g.to_node = ANY(sp.path)
    AND sp.total_weight < 100  -- Ограничение веса
)
SELECT 
    from_node,
    to_node,
    total_weight,
    path
FROM shortest_path
WHERE to_node = 4
ORDER BY total_weight
LIMIT 1;
```

---

## 10. Оптимизация CTE

### 10.1 CTE vs подзапросы

**Сравнение производительности:**

```sql
-- Подзапрос (может выполняться несколько раз)
SELECT * FROM users
WHERE id IN (
    SELECT user_id FROM orders WHERE amount > 100
)
AND id IN (
    SELECT user_id FROM orders WHERE amount > 100  -- Выполняется снова
);

-- CTE (выполняется один раз)
WITH high_value_orders AS (
    SELECT DISTINCT user_id 
    FROM orders 
    WHERE amount > 100
)
SELECT * FROM users
WHERE id IN (SELECT user_id FROM high_value_orders)
AND id IN (SELECT user_id FROM high_value_orders);  -- Использует кэш
```

### 10.2 CTE vs временные таблицы

**CTE:**

- ✅ Не требует создания таблицы
- ✅ Автоматически удаляется после запроса
- ✅ Проще синтаксис
- ❌ Нельзя использовать в нескольких запросах

**Временные таблицы:**

- ✅ Можно использовать в нескольких запросах
- ✅ Можно создать индексы
- ❌ Требует явного создания и удаления
- ❌ Больше кода

---

## 11. Практические примеры

### 11.1 Иерархия категорий

**Дерево категорий с уровнями:**

```sql
WITH RECURSIVE category_tree AS (
    -- Anchor: корневые категории
    SELECT 
        id,
        name,
        parent_id,
        name AS path,
        0 AS level
    FROM categories
    WHERE parent_id IS NULL
    
    UNION ALL
    
    -- Recursive: дочерние категории
    SELECT 
        c.id,
        c.name,
        c.parent_id,
        ct.path || ' > ' || c.name,
        ct.level + 1
    FROM categories c
    INNER JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree
ORDER BY path;
```

### 11.2 Генерация последовательностей

**Генерация дат:**

```sql
WITH RECURSIVE date_series AS (
    SELECT CURRENT_DATE AS date
    UNION ALL
    SELECT date + INTERVAL '1 day'
    FROM date_series
    WHERE date < CURRENT_DATE + INTERVAL '30 days'
)
SELECT * FROM date_series;
```

### 11.3 Развёртка иерархии

**Развёртка всех уровней иерархии:**

```sql
WITH RECURSIVE full_hierarchy AS (
    SELECT id, name, manager_id, 0 AS level
    FROM employees WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.id, e.name, e.manager_id, fh.level + 1
    FROM employees e
    INNER JOIN full_hierarchy fh ON e.manager_id = fh.id
)
SELECT 
    level,
    COUNT(*) AS employees_count
FROM full_hierarchy
GROUP BY level
ORDER BY level;
```

---

## 💡 Key Takeaways

- **CTE (WITH)** — улучшает читаемость сложных запросов

- **Множественные CTE** — логическое разделение этапов запроса

- **Рекурсивные CTE** — для работы с иерархическими данными

- **Anchor + Recursive** — структура рекурсивного CTE

- **CTE** — альтернатива подзапросам и временным таблицам

---

## 🚀 Next Steps

**Related Modules:**

- [11_Window_Functions](../11_Window_Functions/) — Оконные функции
- [07_Subqueries](../07_Subqueries/) — Подзапросы

**Practice Ideas:**

1. Перепишите сложные подзапросы на CTE
2. Решите задачи с иерархическими данными (деревья, графы)
3. Создайте многоэтапные запросы с несколькими CTE
4. Попрактикуйтесь с рекурсивными CTE

**Going Deeper:**

- Изучите оптимизацию рекурсивных CTE
- Изучите использование CTE для обновления данных
- Изучите материализованные CTE

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL WITH Queries](https://www.postgresql.org/docs/current/queries-with.html) — CTE документация
- [Recursive Queries](https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-RECURSIVE) — рекурсивные запросы

---


