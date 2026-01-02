# Подзапросы
## Подзапросы в SELECT и WHERE, EXISTS, IN

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать работу с JOIN
- Иметь представление об агрегатных функциях

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY
- [06_Joins](../06_Joins/) — JOIN и связи между таблицами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать подзапросы в SELECT для вычисления значений
- Применять подзапросы в WHERE для фильтрации данных
- Использовать EXISTS и NOT EXISTS для проверки существования
- Различать коррелированные и некоррелированные подзапросы
- Оптимизировать подзапросы для производительности

---

## 1. Введение в подзапросы

**Подзапрос (subquery)** — это SQL запрос, вложенный в другой запрос.

### 1.1 Зачем нужны подзапросы

**Подзапросы позволяют:**

- Использовать результат одного запроса в другом
- Выполнять сложные фильтрации
- Вычислять значения на основе других таблиц
- Создавать более читаемые запросы

**Пример проблемы без подзапросов:**

```sql
-- Нужно найти пользователей, которые сделали заказы больше среднего
-- Без подзапросов нужны два запроса:
SELECT AVG(amount) FROM orders;  -- Сначала узнаём среднее
-- Затем используем это значение вручную
SELECT * FROM orders WHERE amount > 187.50;
```

**С подзапросом:**

```sql
SELECT * FROM orders 
WHERE amount > (SELECT AVG(amount) FROM orders);
```

---

## 2. Подзапросы в WHERE

### 2.1 Подзапросы с операторами сравнения

**Скалярные подзапросы (возвращают одно значение):**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);

CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    amount DECIMAL(10, 2)
);

INSERT INTO users VALUES
    (1, 'Иван', 25),
    (2, 'Мария', 30),
    (3, 'Петр', 28);

INSERT INTO orders VALUES
    (1, 1, 100.50),
    (2, 1, 200.75),
    (3, 2, 150.00),
    (4, 3, 300.25);

-- Заказы больше среднего
SELECT * FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);
```

**Output:**
```
id | user_id | amount
---+---------+--------
2  | 1       | 200.75
4  | 3       | 300.25
```

### 2.2 Подзапросы с IN

**IN с подзапросом (возвращает список значений):**

```sql
-- Пользователи, которые делали заказы
SELECT * FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);
```

**Output:**
```
id | name  | age
---+-------+-----
1  | Иван  | 25
2  | Мария | 30
3  | Петр  | 28
```

**NOT IN:**

```sql
-- Пользователи без заказов
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM orders WHERE user_id IS NOT NULL);
```

> **⚠️ Warning:**  
> С NOT IN будьте осторожны с NULL. Если подзапрос может вернуть NULL, используйте NOT EXISTS.

### 2.3 Подзапросы с ANY/SOME и ALL

**ANY/SOME — хотя бы одно значение:**

```sql
-- Заказы больше любого заказа пользователя 1
SELECT * FROM orders
WHERE amount > ANY (SELECT amount FROM orders WHERE user_id = 1);
```

**ALL — все значения:**

```sql
-- Заказы больше всех заказов пользователя 1
SELECT * FROM orders
WHERE amount > ALL (SELECT amount FROM orders WHERE user_id = 1);
```

---

## 3. Подзапросы в SELECT

### 3.1 Скалярные подзапросы в SELECT

**Вычисление значений на основе других таблиц:**

```sql
-- Количество заказов для каждого пользователя
SELECT 
    u.name,
    u.age,
    (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS orders_count
FROM users u;
```

**Output:**
```
name  | age | orders_count
------+-----+-------------
Иван  | 25  | 2
Мария | 30  | 1
Петр  | 28  | 1
```

### 3.2 Подзапросы для вычисления агрегатов

**Сумма заказов для каждого пользователя:**

```sql
SELECT 
    u.name,
    (SELECT SUM(amount) FROM orders o WHERE o.user_id = u.id) AS total_spent
FROM users u;
```

**Output:**
```
name  | total_spent
------+-------------
Иван  | 301.25
Мария | 150.00
Петр  | 300.25
```

### 3.3 Подзапросы vs JOIN

**Когда использовать подзапросы в SELECT:**

- ✅ Нужен один агрегат на строку
- ✅ Упрощает логику запроса
- ✅ Легче читать

**Когда использовать JOIN:**

- ✅ Нужно несколько столбцов из связанной таблицы
- ✅ Лучшая производительность на больших данных
- ✅ Нужна фильтрация по связанной таблице

---

## 4. EXISTS и NOT EXISTS

### 4.1 EXISTS

**EXISTS проверяет существование строк:**

```sql
-- Пользователи, которые делали заказы
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id
);
```

**Output:**
```
id | name  | age
---+-------+-----
1  | Иван  | 25
2  | Мария | 30
3  | Петр  | 28
```

**Как работает EXISTS:**

- EXISTS возвращает TRUE, если подзапрос вернул хотя бы одну строку
- Содержимое SELECT в EXISTS не важно (обычно пишут `SELECT 1`)
- EXISTS останавливается при первом совпадении (быстрее, чем COUNT)

### 4.2 NOT EXISTS

**NOT EXISTS — отсутствие строк:**

```sql
-- Пользователи без заказов
SELECT * FROM users u
WHERE NOT EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id
);
```

### 4.3 EXISTS vs IN

**EXISTS обычно быстрее:**

```sql
-- EXISTS (останавливается при первом совпадении)
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);

-- IN (должен собрать весь список)
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders);
```

**Когда использовать EXISTS:**

- ✅ Подзапрос может вернуть много строк
- ✅ Нужна только проверка существования
- ✅ Лучшая производительность

**Когда использовать IN:**

- ✅ Список значений известен и мал
- ✅ Нужны конкретные значения для сравнения

---

## 5. Коррелированные подзапросы

### 5.1 Что такое коррелированный подзапрос

**Коррелированный подзапрос** ссылается на столбцы внешнего запроса.

**Пример:**

```sql
-- Для каждого пользователя найти его самый большой заказ
SELECT 
    u.name,
    (SELECT MAX(amount) 
     FROM orders o 
     WHERE o.user_id = u.id) AS max_order
FROM users u;
```

**Особенности:**

- Подзапрос выполняется для каждой строки внешнего запроса
- Может быть медленным на больших данных
- Полезен для вычислений, специфичных для каждой строки

### 5.2 Некоррелированные подзапросы

**Некоррелированный подзапрос** не зависит от внешнего запроса.

**Пример:**

```sql
-- Заказы больше среднего (среднее вычисляется один раз)
SELECT * FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);
```

**Особенности:**

- Выполняется один раз
- Обычно быстрее коррелированных
- Легче оптимизировать

---

## 6. Подзапросы в FROM

### 6.1 Подзапросы как таблицы

**Подзапросы можно использовать в FROM:**

```sql
-- Статистика по пользователям
SELECT 
    user_stats.name,
    user_stats.orders_count,
    user_stats.total_spent
FROM (
    SELECT 
        u.id,
        u.name,
        COUNT(o.id) AS orders_count,
        SUM(o.amount) AS total_spent
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    GROUP BY u.id, u.name
) AS user_stats
WHERE user_stats.orders_count > 0;
```

**Output:**
```
name  | orders_count | total_spent
------+--------------+-------------
Иван  | 2            | 301.25
Мария | 1            | 150.00
Петр  | 1            | 300.25
```

### 6.2 Алиасы для подзапросов

**Всегда давайте алиасы подзапросам в FROM:**

```sql
-- ✅ Правильно
SELECT * FROM (SELECT ...) AS subquery;

-- ❌ Неправильно (в некоторых СУБД)
SELECT * FROM (SELECT ...);
```

---

## 7. Практические примеры

### 7.1 Топ пользователей

**Пользователи с заказами больше среднего:**

```sql
SELECT 
    u.name,
    SUM(o.amount) AS total_spent
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING SUM(o.amount) > (SELECT AVG(total) FROM (
    SELECT SUM(amount) AS total
    FROM orders
    GROUP BY user_id
) AS user_totals);
```

### 7.2 Сравнение с агрегатами

**Заказы, которые больше среднего заказа пользователя:**

```sql
SELECT 
    o1.id,
    o1.user_id,
    o1.amount
FROM orders o1
WHERE o1.amount > (
    SELECT AVG(o2.amount)
    FROM orders o2
    WHERE o2.user_id = o1.user_id
);
```

### 7.3 Проверка существования

**Пользователи с заказами за последний месяц:**

```sql
ALTER TABLE orders ADD COLUMN order_date DATE;
UPDATE orders SET order_date = CURRENT_DATE - INTERVAL '10 days' WHERE id = 1;
UPDATE orders SET order_date = CURRENT_DATE - INTERVAL '5 days' WHERE id = 2;
UPDATE orders SET order_date = CURRENT_DATE - INTERVAL '40 days' WHERE id = 3;
UPDATE orders SET order_date = CURRENT_DATE - INTERVAL '2 days' WHERE id = 4;

SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.user_id = u.id
    AND o.order_date >= CURRENT_DATE - INTERVAL '30 days'
);
```

---

## 8. Оптимизация подзапросов

### 8.1 Подзапросы vs JOIN

**Часто подзапросы можно переписать как JOIN:**

```sql
-- Подзапрос
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders);

-- JOIN (обычно быстрее)
SELECT DISTINCT u.* FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 8.2 EXISTS vs COUNT

**EXISTS быстрее COUNT:**

```sql
-- ❌ Медленно
SELECT * FROM users u
WHERE (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) > 0;

-- ✅ Быстрее
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### 8.3 Избегайте вложенных подзапросов

**❌ Слишком много вложенности:**

```sql
SELECT * FROM table1
WHERE id IN (
    SELECT id FROM table2
    WHERE col IN (
        SELECT col FROM table3
        WHERE ...
    )
);
```

**✅ Перепишите с JOIN или CTE:**

```sql
-- С JOIN
SELECT t1.* FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id
INNER JOIN table3 t3 ON t2.col = t3.col;
```

---

## 9. Частые ошибки

### 9.1 Подзапрос возвращает несколько строк

**❌ Ошибка:**

```sql
-- Если подзапрос вернёт несколько строк, будет ошибка
SELECT * FROM users
WHERE age = (SELECT age FROM users WHERE name LIKE 'И%');
```

**✅ Решение:**

```sql
-- Используйте IN или ANY
SELECT * FROM users
WHERE age IN (SELECT age FROM users WHERE name LIKE 'И%');
```

### 9.2 NULL в подзапросах

**Проблема с NULL в NOT IN:**

```sql
-- Если подзапрос вернёт NULL, NOT IN может работать неожиданно
SELECT * FROM users
WHERE id NOT IN (SELECT user_id FROM orders);
-- Если user_id содержит NULL, результат может быть пустым
```

**✅ Решение:**

```sql
-- Используйте NOT EXISTS
SELECT * FROM users u
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

---

## 💡 Key Takeaways

- **Подзапросы** — вложенные запросы для сложной логики

- **В WHERE** — фильтрация на основе других таблиц

- **В SELECT** — вычисление значений для каждой строки

- **EXISTS** — проверка существования (обычно быстрее IN)

- **Коррелированные подзапросы** — ссылаются на внешний запрос, могут быть медленными

---

## 🚀 Next Steps

**Related Modules:**

- [11_Window_Functions](../11_Window_Functions/) — Оконные функции (альтернатива подзапросам)
- [12_CTE](../12_CTE/) — CTE для читаемости сложных подзапросов

**Practice Ideas:**

1. Перепишите JOIN запросы как подзапросы и наоборот
2. Попрактикуйтесь с EXISTS и NOT EXISTS
3. Сравните производительность подзапросов и JOIN
4. Решите задачи с коррелированными подзапросами

**Going Deeper:**

- Изучите оптимизацию подзапросов
- Изучите использование CTE вместо подзапросов
- Изучите lateral joins (PostgreSQL)

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Subqueries](https://www.postgresql.org/docs/current/sql-expressions.html#SQL-SYNTAX-EXPRESS-EVAL) — подзапросы в PostgreSQL
- [SQL Subqueries](https://www.postgresql.org/docs/current/tutorial-subqueries.html) — учебник по подзапросам

---


