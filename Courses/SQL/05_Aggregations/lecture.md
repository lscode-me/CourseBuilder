# Агрегации и GROUP BY
## COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать работу с WHERE условиями
- Иметь представление о числовых типах данных

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [03_Data_Types](../03_Data_Types/) — Типы данных и NULL

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать агрегатные функции (COUNT, SUM, AVG, MIN, MAX)
- Группировать данные с помощью GROUP BY
- Фильтровать группы с помощью HAVING
- Различать WHERE и HAVING
- Применять агрегации в практических сценариях

---

## 1. Введение в агрегации

**Агрегатные функции** выполняют вычисления над набором строк и возвращают одно значение.

**Зачем нужны агрегации:**

- Подсчёт количества записей
- Вычисление сумм, средних, минимумов, максимумов
- Группировка и анализ данных
- Создание отчётов и статистики

---

## 2. Агрегатные функции

### 2.1 COUNT — подсчёт строк

**COUNT(*)** — считает все строки, включая NULL:

```sql
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    age INTEGER,
    country VARCHAR(50)
);

INSERT INTO users VALUES
    (1, 'Иван', 25, 'Russia'),
    (2, 'Мария', 30, 'Russia'),
    (3, 'Петр', 28, 'USA'),
    (4, 'Анна', NULL, 'USA'),
    (5, 'Сергей', 35, 'Russia');

-- Подсчёт всех пользователей
SELECT COUNT(*) AS total_users FROM users;
```

**Output:**
```
total_users
-----------
5
```

**COUNT(column)** — считает строки, где column не NULL:

```sql
-- Пользователи с указанным возрастом
SELECT COUNT(age) AS users_with_age FROM users;
```

**Output:**
```
users_with_age
--------------
4
```

**COUNT(DISTINCT column)** — считает уникальные значения:

```sql
-- Количество уникальных стран
SELECT COUNT(DISTINCT country) AS unique_countries FROM users;
```

**Output:**
```
unique_countries
---------------
2
```

### 2.2 SUM — сумма значений

**SUM** — суммирует числовые значения:

```sql
CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    amount DECIMAL(10, 2)
);

INSERT INTO orders VALUES
    (1, 1, 100.50),
    (2, 1, 200.75),
    (3, 2, 150.00),
    (4, 3, 300.25);

-- Общая сумма всех заказов
SELECT SUM(amount) AS total_amount FROM orders;
```

**Output:**
```
total_amount
------------
751.50
```

**SUM с NULL:**

```sql
-- NULL значения игнорируются
INSERT INTO orders VALUES (5, 4, NULL);

SELECT SUM(amount) FROM orders;  -- Всё ещё 751.50
```

### 2.3 AVG — среднее значение

**AVG** — вычисляет среднее арифметическое:

```sql
-- Средняя сумма заказа
SELECT AVG(amount) AS avg_amount FROM orders;
```

**Output:**
```
avg_amount
----------
187.875
```

**AVG с NULL:**

```sql
-- NULL значения не учитываются
SELECT AVG(amount) FROM orders;  -- Среднее по 4 заказам, не 5
```

### 2.4 MIN и MAX — минимум и максимум

**MIN** — минимальное значение:

```sql
-- Минимальная сумма заказа
SELECT MIN(amount) AS min_amount FROM orders;
```

**Output:**
```
min_amount
----------
100.50
```

**MAX** — максимальное значение:

```sql
-- Максимальная сумма заказа
SELECT MAX(amount) AS max_amount FROM orders;
```

**Output:**
```
max_amount
----------
300.25
```

**MIN/MAX с датами:**

```sql
ALTER TABLE orders ADD COLUMN order_date DATE;

UPDATE orders SET order_date = '2024-01-15' WHERE id = 1;
UPDATE orders SET order_date = '2024-01-20' WHERE id = 2;
UPDATE orders SET order_date = '2024-01-10' WHERE id = 3;
UPDATE orders SET order_date = '2024-01-25' WHERE id = 4;

-- Самая ранняя и поздняя дата
SELECT 
    MIN(order_date) AS earliest_order,
    MAX(order_date) AS latest_order
FROM orders;
```

**Output:**
```
earliest_order | latest_order
--------------+-------------
2024-01-10    | 2024-01-25
```

### 2.5 Комбинация агрегатных функций

**Несколько агрегаций в одном запросе:**

```sql
SELECT 
    COUNT(*) AS total_orders,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount,
    MIN(amount) AS min_amount,
    MAX(amount) AS max_amount
FROM orders;
```

**Output:**
```
total_orders | total_amount | avg_amount | min_amount | max_amount
------------+--------------+------------+------------+------------
4           | 751.50       | 187.875    | 100.50     | 300.25
```

---

## 3. GROUP BY — группировка данных

**GROUP BY** группирует строки с одинаковыми значениями в указанных столбцах.

### 3.1 Базовый GROUP BY

**Группировка по одному столбцу:**

```sql
-- Количество пользователей по странам
SELECT 
    country,
    COUNT(*) AS users_count
FROM users
GROUP BY country;
```

**Output:**
```
country | users_count
--------+------------
Russia  | 3
USA     | 2
```

**Как это работает:**

1. Строки группируются по значениям `country`
2. Для каждой группы вычисляется агрегат (COUNT)
3. Возвращается одна строка на группу

### 3.2 GROUP BY с несколькими столбцами

**Группировка по нескольким столбцам:**

```sql
-- Количество заказов по пользователю и дате
SELECT 
    user_id,
    order_date,
    COUNT(*) AS orders_count,
    SUM(amount) AS total_amount
FROM orders
GROUP BY user_id, order_date;
```

**Output:**
```
user_id | order_date | orders_count | total_amount
--------+------------+--------------+-------------
1       | 2024-01-15 | 1            | 100.50
1       | 2024-01-20 | 1            | 200.75
2       | 2024-01-10 | 1            | 150.00
3       | 2024-01-25 | 1            | 300.25
```

### 3.3 GROUP BY с агрегатами

**Разные агрегаты для групп:**

```sql
-- Статистика по странам
SELECT 
    country,
    COUNT(*) AS users_count,
    AVG(age) AS avg_age,
    MIN(age) AS min_age,
    MAX(age) AS max_age
FROM users
WHERE age IS NOT NULL
GROUP BY country;
```

**Output:**
```
country | users_count | avg_age | min_age | max_age
--------+-------------+---------+---------+---------
Russia  | 3           | 30.0    | 25      | 35
USA     | 1           | 28.0    | 28      | 28
```

### 3.4 Правила GROUP BY

**Важное правило:** В SELECT можно указывать только:
- Столбцы из GROUP BY
- Агрегатные функции
- Выражения, зависящие только от столбцов GROUP BY

**❌ Неправильно:**

```sql
-- Ошибка: name не в GROUP BY
SELECT country, name, COUNT(*) 
FROM users 
GROUP BY country;
```

**✅ Правильно:**

```sql
SELECT country, COUNT(*) 
FROM users 
GROUP BY country;
```

---

## 4. HAVING — фильтрация групп

**HAVING** фильтрует группы после группировки (аналог WHERE для групп).

### 4.1 WHERE vs HAVING

**WHERE** — фильтрует строки ДО группировки:

```sql
-- Сначала фильтруем (WHERE), потом группируем
SELECT 
    country,
    COUNT(*) AS users_count
FROM users
WHERE age > 25  -- Фильтр строк
GROUP BY country;
```

**HAVING** — фильтрует группы ПОСЛЕ группировки:

```sql
-- Сначала группируем, потом фильтруем группы (HAVING)
SELECT 
    country,
    COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 2;  -- Фильтр групп
```

**Output:**
```
country | users_count
--------+-------------
Russia  | 3
```

### 4.2 HAVING с агрегатами

**HAVING может использовать агрегатные функции:**

```sql
-- Страны со средним возрастом больше 28
SELECT 
    country,
    AVG(age) AS avg_age,
    COUNT(*) AS users_count
FROM users
WHERE age IS NOT NULL
GROUP BY country
HAVING AVG(age) > 28;
```

**Output:**
```
country | avg_age | users_count
--------+---------+-------------
Russia  | 30.0    | 3
```

### 4.3 WHERE и HAVING вместе

**Можно использовать оба:**

```sql
-- Пользователи старше 25, сгруппированные по странам,
-- где в группе больше 1 пользователя
SELECT 
    country,
    COUNT(*) AS users_count,
    AVG(age) AS avg_age
FROM users
WHERE age > 25  -- Фильтр строк ДО группировки
GROUP BY country
HAVING COUNT(*) > 1;  -- Фильтр групп ПОСЛЕ группировки
```

**Порядок выполнения:**

```
1. FROM users
2. WHERE age > 25        (фильтр строк)
3. GROUP BY country      (группировка)
4. HAVING COUNT(*) > 1   (фильтр групп)
5. SELECT                 (выбор столбцов)
```

---

## 5. Практические примеры

### 5.1 Статистика по пользователям

**Топ пользователей по сумме заказов:**

```sql
SELECT 
    user_id,
    COUNT(*) AS orders_count,
    SUM(amount) AS total_spent,
    AVG(amount) AS avg_order_amount
FROM orders
GROUP BY user_id
ORDER BY total_spent DESC;
```

**Output:**
```
user_id | orders_count | total_spent | avg_order_amount
--------+--------------+-------------+-----------------
3       | 1            | 300.25      | 300.25
1       | 2            | 301.25      | 150.625
2       | 1            | 150.00      | 150.00
```

### 5.2 Ежедневная статистика

**Статистика заказов по дням:**

```sql
SELECT 
    order_date,
    COUNT(*) AS orders_count,
    SUM(amount) AS daily_revenue,
    AVG(amount) AS avg_order_amount
FROM orders
GROUP BY order_date
ORDER BY order_date;
```

### 5.3 Группировка по месяцам

**Статистика по месяцам (PostgreSQL):**

```sql
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    COUNT(*) AS orders_count,
    SUM(amount) AS monthly_revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
```

### 5.4 Условия в HAVING

**Группы с определёнными характеристиками:**

```sql
-- Страны, где больше 2 пользователей И средний возраст > 28
SELECT 
    country,
    COUNT(*) AS users_count,
    AVG(age) AS avg_age
FROM users
WHERE age IS NOT NULL
GROUP BY country
HAVING COUNT(*) > 2 AND AVG(age) > 28;
```

---

## 6. Частые ошибки и best practices

### 6.1 Забыли GROUP BY

**❌ Ошибка:**

```sql
-- Ошибка: агрегат без GROUP BY
SELECT country, COUNT(*) 
FROM users;
```

**✅ Правильно:**

```sql
SELECT country, COUNT(*) 
FROM users 
GROUP BY country;
```

### 6.2 Столбец не в GROUP BY

**❌ Ошибка:**

```sql
-- Ошибка: name не в GROUP BY
SELECT country, name, COUNT(*) 
FROM users 
GROUP BY country;
```

**✅ Правильно:**

```sql
-- Либо добавить name в GROUP BY
SELECT country, name, COUNT(*) 
FROM users 
GROUP BY country, name;

-- Либо убрать name из SELECT
SELECT country, COUNT(*) 
FROM users 
GROUP BY country;
```

### 6.3 WHERE вместо HAVING

**❌ Неправильно:**

```sql
-- Ошибка: нельзя использовать агрегат в WHERE
SELECT country, COUNT(*) 
FROM users 
WHERE COUNT(*) > 2
GROUP BY country;
```

**✅ Правильно:**

```sql
SELECT country, COUNT(*) 
FROM users 
GROUP BY country
HAVING COUNT(*) > 2;
```

### 6.4 NULL в GROUP BY

**NULL значения группируются вместе:**

```sql
-- Группировка по возрасту (NULL будет отдельной группой)
SELECT 
    age,
    COUNT(*) AS count
FROM users
GROUP BY age;
```

**Output:**
```
age | count
----+-------
25  | 1
28  | 1
30  | 1
35  | 1
    | 1  (NULL)
```

---

## 7. Продвинутые техники

### 7.1 Условные агрегаты

**Использование CASE в агрегатах:**

```sql
-- Количество пользователей по возрастным группам
SELECT 
    country,
    COUNT(*) AS total,
    SUM(CASE WHEN age < 30 THEN 1 ELSE 0 END) AS under_30,
    SUM(CASE WHEN age >= 30 THEN 1 ELSE 0 END) AS over_30
FROM users
WHERE age IS NOT NULL
GROUP BY country;
```

### 7.2 Фильтрация внутри агрегатов

**FILTER clause (PostgreSQL):**

```sql
-- Более читаемый способ условных агрегатов
SELECT 
    country,
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE age < 30) AS under_30,
    COUNT(*) FILTER (WHERE age >= 30) AS over_30
FROM users
WHERE age IS NOT NULL
GROUP BY country;
```

### 7.3 DISTINCT в агрегатах

**COUNT(DISTINCT ...):**

```sql
-- Количество уникальных пользователей, сделавших заказы
SELECT COUNT(DISTINCT user_id) AS unique_customers
FROM orders;
```

---

## 💡 Key Takeaways

- **Агрегатные функции** (COUNT, SUM, AVG, MIN, MAX) вычисляют значения над наборами строк

- **GROUP BY** группирует строки по значениям столбцов

- **HAVING** фильтрует группы после группировки (аналог WHERE для групп)

- **WHERE** фильтрует строки ДО группировки, **HAVING** — группы ПОСЛЕ
- В SELECT с GROUP BY можно указывать только столбцы из GROUP BY и агрегаты

---

## 🚀 Next Steps

**Related Modules:**

- [06_Joins](../06_Joins/) — JOIN и связи между таблицами
- [07_Subqueries](../07_Subqueries/) — Подзапросы

**Practice Ideas:**

1. Создайте таблицу с данными и попрактикуйтесь с агрегациями
2. Попробуйте группировку по разным столбцам
3. Экспериментируйте с WHERE и HAVING
4. Создайте отчёты с несколькими уровнями группировки

**Going Deeper:**

- Изучите оконные функции (агрегаты без GROUP BY)
- Изучите ROLLUP и CUBE для многомерных агрегаций
- Изучите производительность агрегаций на больших данных

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Aggregate Functions](https://www.postgresql.org/docs/current/functions-aggregate.html) — все агрегатные функции
- [PostgreSQL GROUP BY](https://www.postgresql.org/docs/current/sql-select.html#SQL-GROUPBY) — GROUP BY документация

**Articles:**

- [SQL Aggregations](https://www.postgresql.org/docs/current/tutorial-agg.html) — учебник по агрегациям
- [GROUP BY vs HAVING](https://www.sqlshack.com/sql-group-by-clause-explained/) — различия GROUP BY и HAVING

---


