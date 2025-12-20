# JOIN и связи между таблицами
## INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, ON vs WHERE

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать работу с несколькими таблицами
- Иметь представление о первичных и внешних ключах

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать INNER JOIN для объединения таблиц
- Применять LEFT, RIGHT и FULL JOIN для различных сценариев
- Различать ON и WHERE при работе с JOIN
- Понимать разницу между типами JOIN
- Решать практические задачи с несколькими таблицами

---

## 1. Введение в JOIN

**JOIN** позволяет объединять данные из нескольких таблиц в одном запросе.

### 1.1 Зачем нужны JOIN

**Проблема без JOIN:**

```sql

-- Две отдельные таблицы
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    country_id INTEGER
);

CREATE TABLE countries (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

-- Чтобы получить имя пользователя и страну, нужны два запроса
SELECT name FROM users WHERE id = 1;
SELECT name FROM countries WHERE id = (SELECT country_id FROM users WHERE id = 1);
```

**Решение с JOIN:**

```sql

-- Один запрос объединяет данные
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
JOIN countries c ON u.country_id = c.id
WHERE u.id = 1;
```

### 1.2 Типы JOIN

**Основные типы:**

- **INNER JOIN** — только совпадающие строки

- **LEFT JOIN** — все строки из левой таблицы + совпадающие из правой

- **RIGHT JOIN** — все строки из правой таблицы + совпадающие из левой

- **FULL JOIN** — все строки из обеих таблиц

- **CROSS JOIN** — декартово произведение

---

## 2. INNER JOIN

**INNER JOIN** возвращает только строки, где есть совпадение в обеих таблицах.

### 2.1 Базовый синтаксис

```sql

SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column;
```

**Пример:**

```sql

INSERT INTO countries VALUES
    (1, 'Russia'),
    (2, 'USA'),
    (3, 'Germany');

INSERT INTO users VALUES
    (1, 'Иван', 1),
    (2, 'Мария', 1),
    (3, 'John', 2),
    (4, 'Петр', NULL);  -- Нет страны

-- INNER JOIN
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
INNER JOIN countries c ON u.country_id = c.id;
```

**Output:**
```

user_name | country_name
----------+--------------
Иван      | Russia
Мария     | Russia
John      | USA
```

**Обратите внимание:** Пользователь "Петр" не попал в результат, так как у него `country_id = NULL`.

### 2.2 JOIN с несколькими условиями

```sql

-- JOIN с несколькими условиями
SELECT 
    u.name,
    c.name AS country,
    o.amount
FROM users u
INNER JOIN countries c ON u.country_id = c.id
INNER JOIN orders o ON u.id = o.user_id
WHERE o.amount > 100;
```

### 2.3 JOIN с алиасами

**Алиасы делают запросы читаемее:**

```sql

-- Без алиасов (менее читаемо)
SELECT users.name, countries.name
FROM users
INNER JOIN countries ON users.country_id = countries.id;

-- С алиасами (читаемее)
SELECT u.name, c.name
FROM users u
INNER JOIN countries c ON u.country_id = c.id;
```

---

## 3. LEFT JOIN

**LEFT JOIN** возвращает все строки из левой таблицы и совпадающие из правой. Если совпадения нет, правые столбцы будут NULL.

### 3.1 Базовый LEFT JOIN

```sql

-- Все пользователи, даже без страны
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id;
```

**Output:**
```

user_name | country_name
----------+--------------
Иван      | Russia
Мария     | Russia
John      | USA
Петр      |              (NULL)
```

**Петр попал в результат**, хотя у него нет страны.

### 3.2 LEFT JOIN для поиска отсутствующих связей

**Найти пользователей без страны:**

```sql

SELECT 
    u.name,
    u.country_id
FROM users u
LEFT JOIN countries c ON u.country_id = c.id
WHERE c.id IS NULL;
```

**Output:**
```

name | country_id

-----+------------
Петр | 
```

### 3.3 LEFT JOIN vs INNER JOIN

**Разница:**

```sql

-- INNER JOIN: только пользователи со страной
SELECT COUNT(*) FROM users u
INNER JOIN countries c ON u.country_id = c.id;
-- Результат: 3

-- LEFT JOIN: все пользователи
SELECT COUNT(*) FROM users u
LEFT JOIN countries c ON u.country_id = c.id;

-- Результат: 4
```

---

## 4. RIGHT JOIN

**RIGHT JOIN** возвращает все строки из правой таблицы и совпадающие из левой.

### 4.1 Базовый RIGHT JOIN

```sql

-- Все страны, даже без пользователей
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
RIGHT JOIN countries c ON u.country_id = c.id;
```

**Output:**
```

user_name | country_name
----------+--------------
Иван      | Russia
Мария     | Russia
John      | USA
          | Germany      (NULL для пользователя)
```

**Germany попала в результат**, хотя у неё нет пользователей.

### 4.2 RIGHT JOIN для поиска неиспользуемых данных

**Найти страны без пользователей:**

```sql

SELECT 
    c.name AS country_name
FROM users u
RIGHT JOIN countries c ON u.country_id = c.id
WHERE u.id IS NULL;
```

**Output:**
```

country_name

------------
Germany
```

> **💡 Pro Tip:**  
> RIGHT JOIN используется реже LEFT JOIN. Обычно можно переписать запрос с LEFT JOIN, поменяв порядок таблиц.

---

## 5. FULL JOIN

**FULL JOIN** возвращает все строки из обеих таблиц. Если совпадения нет, соответствующие столбцы будут NULL.

### 5.1 Базовый FULL JOIN

```sql

-- Все пользователи и все страны
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
FULL JOIN countries c ON u.country_id = c.id;
```

**Output:**
```

user_name | country_name
----------+--------------
Иван      | Russia
Мария     | Russia
John      | USA
Петр      |              (NULL для страны)
          | Germany      (NULL для пользователя)
```

**FULL JOIN включает:**

- Пользователей со странами (совпадения)
- Пользователей без стран (только левая таблица)
- Страны без пользователей (только правая таблица)

### 5.2 FULL JOIN для анализа данных

**Найти все несоответствия:**

```sql

SELECT 
    u.name AS user_name,
    c.name AS country_name,
    CASE 
        WHEN u.id IS NULL THEN 'Страна без пользователей'
        WHEN c.id IS NULL THEN 'Пользователь без страны'
        ELSE 'Связь есть'
    END AS status
FROM users u
FULL JOIN countries c ON u.country_id = c.id;
```

---

## 6. CROSS JOIN

**CROSS JOIN** возвращает декартово произведение — все комбинации строк из обеих таблиц.

### 6.1 Базовый CROSS JOIN

```sql

-- Все комбинации пользователей и стран
SELECT 
    u.name AS user_name,
    c.name AS country_name
FROM users u
CROSS JOIN countries c;
```

**Output:**
```

user_name | country_name
----------+--------------
Иван      | Russia
Иван      | USA
Иван      | Germany
Мария     | Russia
Мария     | USA
Мария     | Germany
John      | Russia
John      | USA
John      | Germany
Петр      | Russia
Петр      | USA
Петр      | Germany
```

**Количество строк:** 4 пользователя × 3 страны = 12 строк

> **⚠️ Warning:**  
> CROSS JOIN может создать огромное количество строк. Используйте осторожно!

### 6.2 Когда использовать CROSS JOIN

**Полезные случаи:**

```sql

-- Генерация всех комбинаций для тестирования
CREATE TABLE sizes (size VARCHAR(10));
CREATE TABLE colors (color VARCHAR(10));

INSERT INTO sizes VALUES ('S'), ('M'), ('L');
INSERT INTO colors VALUES ('Red'), ('Blue'), ('Green');

-- Все комбинации размеров и цветов
SELECT s.size, c.color
FROM sizes s
CROSS JOIN colors c;
```

---

## 7. ON vs WHERE

### 7.1 ON — условие соединения

**ON** определяет, как таблицы соединяются:

```sql

SELECT u.name, c.name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id;
```

**ON используется для:**

- Условий соединения (какие строки соединять)
- Работает ДО фильтрации

### 7.2 WHERE — фильтрация результата

**WHERE** фильтрует результат после соединения:

```sql

SELECT u.name, c.name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id
WHERE c.name = 'Russia';
```

**WHERE используется для:**

- Фильтрации уже соединённых данных
- Работает ПОСЛЕ соединения

### 7.3 Разница в LEFT JOIN

**Важная разница:**

```sql

-- ON: условие соединения (все пользователи, фильтр только по стране)
SELECT u.name, c.name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id AND c.name = 'Russia';
-- Результат: все пользователи, но country_name только для Russia

-- WHERE: фильтрация результата (только пользователи из Russia)
SELECT u.name, c.name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id
WHERE c.name = 'Russia';

-- Результат: только пользователи из Russia (NULL отфильтруются)
```

---

## 8. Множественные JOIN

### 8.1 Цепочка JOIN

```sql

CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    product_id INTEGER,
    amount DECIMAL(10, 2)
);

CREATE TABLE products (
    id INTEGER,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- JOIN нескольких таблиц
SELECT 
    u.name AS user_name,
    p.name AS product_name,
    o.amount
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN products p ON o.product_id = p.id;
```

### 8.2 Смешанные типы JOIN

```sql

-- Комбинация LEFT и INNER JOIN
SELECT 
    u.name AS user_name,
    c.name AS country_name,
    p.name AS product_name
FROM users u
LEFT JOIN countries c ON u.country_id = c.id
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN products p ON o.product_id = p.id;
```

---

## 9. Self JOIN

**Self JOIN** — соединение таблицы с самой собой.

### 9.1 Пример Self JOIN

**Найти менеджеров для сотрудников:**

```sql

CREATE TABLE employees (
    id INTEGER,
    name VARCHAR(100),
    manager_id INTEGER
);

INSERT INTO employees VALUES
    (1, 'Иван', NULL),
    (2, 'Мария', 1),
    (3, 'Петр', 1),
    (4, 'Анна', 2);

-- Self JOIN для получения менеджеров
SELECT 
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**Output:**
```

employee | manager

---------+--------
Иван     |        (NULL - нет менеджера)
Мария    | Иван
Петр     | Иван
Анна     | Мария
```

---

## 10. Практические примеры

### 10.1 Отчёт по заказам с пользователями

```sql

SELECT 
    u.name AS user_name,
    c.name AS country,
    COUNT(o.id) AS orders_count,
    SUM(o.amount) AS total_spent
FROM users u
LEFT JOIN countries c ON u.country_id = c.id
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, c.name
ORDER BY total_spent DESC;
```

### 10.2 Найти пользователей без заказов

```sql

SELECT 
    u.name,
    u.id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

### 10.3 Полный отчёт с FULL JOIN

```sql

SELECT 
    COALESCE(u.name, 'Нет пользователя') AS user_name,
    COALESCE(c.name, 'Нет страны') AS country_name,
    COALESCE(CAST(COUNT(o.id) AS VARCHAR), '0') AS orders_count
FROM users u
FULL JOIN countries c ON u.country_id = c.id
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, c.id, c.name;
```

---

## 11. Производительность JOIN

### 11.1 Индексы для JOIN

**JOIN работает быстрее с индексами:**

```sql

-- Создать индекс для ускорения JOIN
CREATE INDEX idx_users_country_id ON users(country_id);
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### 11.2 Порядок JOIN

**Порядок может влиять на производительность:**

```sql

-- Может быть быстрее, если users меньше
SELECT ...
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Или наоборот, если orders меньше
SELECT ...
FROM orders o
INNER JOIN users u ON o.user_id = u.id;
```

> **💡 Pro Tip:**  
> СУБД обычно оптимизирует порядок JOIN автоматически, но понимание помогает в сложных случаях.

---

## 💡 Key Takeaways

- **INNER JOIN** — только совпадающие строки из обеих таблиц

- **LEFT JOIN** — все строки из левой таблицы + совпадающие из правой

- **RIGHT JOIN** — все строки из правой таблицы + совпадающие из левой

- **FULL JOIN** — все строки из обеих таблиц

- **ON** — условие соединения, **WHERE** — фильтрация результата

---

## 🚀 Next Steps

**Related Modules:**

- [07_Subqueries](../07_Subqueries/) — Подзапросы
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

**Practice Ideas:**

1. Создайте несколько связанных таблиц и попрактикуйтесь с разными типами JOIN
2. Решите задачи: найти пользователей без заказов, страны без пользователей
3. Попробуйте Self JOIN для иерархических данных
4. Экспериментируйте с производительностью JOIN на больших данных

**Going Deeper:**

- Изучите оптимизацию JOIN запросов
- Изучите hash join, merge join, nested loop join
- Изучите использование индексов для JOIN

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL JOIN](https://www.postgresql.org/docs/current/tutorial-join.html) — учебник по JOIN
- [SQL JOIN Types](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-FROM) — типы JOIN

**Articles:**

- [Visual Guide to SQL JOINs](https://www.sqlshack.com/sql-join-types-explained-visually/) — визуальное руководство
- [JOIN Performance](https://www.postgresql.org/docs/current/performance-tips.html) — производительность JOIN

---


