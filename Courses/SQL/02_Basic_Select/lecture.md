# Базовый SELECT
## Выборка данных: SELECT, FROM, WHERE, ORDER BY, LIMIT

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать, что такое реляционные базы данных и таблицы
- Знать структуру таблицы (строки, столбцы)
- Иметь доступ к SQL-совместимой СУБД (PostgreSQL, MySQL, SQLite)

**Recommended prior modules:**

- [01_Intro](../01_Intro/) — Введение в SQL и реляционные базы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Писать базовые SELECT запросы для выборки данных
- Применять условия WHERE для фильтрации строк
- Сортировать результаты с помощью ORDER BY
- Ограничивать количество результатов через LIMIT
- Понимать порядок выполнения операций в SQL запросе

---

## 1. Структура SELECT запроса

**SELECT** — это основная команда SQL для выборки данных из таблиц. Это самая часто используемая операция в SQL.

### 1.1 Базовый синтаксис

**Минимальный SELECT запрос:**

```sql
SELECT column1, column2, ...
FROM table_name;
```

**Пример: получить все данные из таблицы**

```sql
-- Получить все столбцы
SELECT * FROM users;
```

**Output:**
```
id | name  | email              | age
---+-------+--------------------+-----
1  | Иван  | ivan@example.com   | 25
2  | Мария | maria@example.com  | 30
3  | Петр  | petr@example.com   | 28
```

> **⚠️ Warning:**  
> Использование `SELECT *` в production коде — антипаттерн. Всегда указывайте конкретные столбцы.

**Пример: получить конкретные столбцы**

```sql
-- Получить только имя и email
SELECT name, email FROM users;
```

**Output:**
```
name  | email
------+--------------------
Иван  | ivan@example.com
Мария | maria@example.com
Петр  | petr@example.com
```

### 1.2 Порядок выполнения операций

Важно понимать порядок выполнения операций в SQL:

```
1. FROM    — определяем таблицу
2. WHERE   — фильтруем строки
3. SELECT  — выбираем столбцы
4. ORDER BY — сортируем
5. LIMIT   — ограничиваем количество
```

**Это НЕ порядок написания!** Порядок написания: SELECT → FROM → WHERE → ORDER BY → LIMIT

---

## 2. FROM — выбор таблицы

**FROM** указывает, из какой таблицы выбирать данные.

### 2.1 Простой FROM

```sql
SELECT name, age
FROM users;
```

**Output:**
```
name  | age
------+-----
Иван  | 25
Мария | 30
Петр  | 28
```

### 2.2 FROM с несколькими таблицами

Пока мы рассматриваем только одну таблицу. Работа с несколькими таблицами (JOIN) будет в [лекции 06](../06_Joins/).

---

## 3. WHERE — фильтрация строк

**WHERE** позволяет фильтровать строки по условиям. Это одна из самых важных частей SQL.

### 3.1 Операторы сравнения

**Базовые операторы:**

| Оператор | Описание | Пример |
|----------|----------|--------|
| `=` | Равно | `age = 25` |
| `<>` или `!=` | Не равно | `age <> 25` |
| `<` | Меньше | `age < 30` |
| `>` | Больше | `age > 20` |
| `<=` | Меньше или равно | `age <= 30` |
| `>=` | Больше или равно | `age >= 18` |

**Пример: пользователи старше 25 лет**

```sql
SELECT name, age
FROM users
WHERE age > 25;
```

**Output:**
```
name  | age
------+-----
Мария | 30
Петр  | 28
```

### 3.2 Логические операторы

**AND, OR, NOT:**

```sql
-- Пользователи от 25 до 30 лет
SELECT name, age
FROM users
WHERE age >= 25 AND age <= 30;
```

**Output:**
```
name  | age
------+-----
Иван  | 25
Мария | 30
Петр  | 28
```

**Пример с OR:**

```sql
-- Пользователи младше 20 или старше 30
SELECT name, age
FROM users
WHERE age < 20 OR age > 30;
```

**Пример с NOT:**

```sql
-- Все пользователи, кроме Ивана
SELECT name, age
FROM users
WHERE NOT name = 'Иван';
```

### 3.3 Работа со строками

**LIKE для поиска по шаблону:**

```sql
-- Пользователи с email на @example.com
SELECT name, email
FROM users
WHERE email LIKE '%@example.com';
```

**Символы подстановки:**

- `%` — любая последовательность символов (0 или более)
- `_` — один любой символ

**Примеры:**

```sql
-- Имена, начинающиеся с "И"
SELECT name
FROM users
WHERE name LIKE 'И%';
```

**Output:**
```
name
-----
Иван
```

```sql
-- Email с доменом gmail
SELECT email
FROM users
WHERE email LIKE '%@gmail.com';
```

**ILIKE (PostgreSQL) — регистронезависимый поиск:**

```sql
-- PostgreSQL: регистронезависимый поиск
SELECT name
FROM users
WHERE name ILIKE 'иван%';
```

### 3.4 IN и NOT IN

**IN — проверка принадлежности списку:**

```sql
-- Пользователи с возрастом 25, 28 или 30
SELECT name, age
FROM users
WHERE age IN (25, 28, 30);
```

**Output:**
```
name  | age
------+-----
Иван  | 25
Мария | 30
Петр  | 28
```

**NOT IN — исключение из списка:**

```sql
-- Пользователи с возрастом не 25 и не 30
SELECT name, age
FROM users
WHERE age NOT IN (25, 30);
```

### 3.5 BETWEEN

**BETWEEN — диапазон значений (включительно):**

```sql
-- Пользователи от 25 до 30 лет включительно
SELECT name, age
FROM users
WHERE age BETWEEN 25 AND 30;
```

**Эквивалентно:**

```sql
SELECT name, age
FROM users
WHERE age >= 25 AND age <= 30;
```

> **💡 Pro Tip:**  
> BETWEEN включает границы. `BETWEEN 25 AND 30` эквивалентно `>= 25 AND <= 30`.

### 3.6 NULL значения

**Проверка на NULL:**

```sql
-- Пользователи без указанного возраста
SELECT name, age
FROM users
WHERE age IS NULL;
```

**Проверка на NOT NULL:**

```sql
-- Пользователи с указанным возрастом
SELECT name, age
FROM users
WHERE age IS NOT NULL;
```

> **⚠️ Warning:**  
> Нельзя использовать `= NULL` или `!= NULL`. Всегда используйте `IS NULL` или `IS NOT NULL`.

---

## 4. ORDER BY — сортировка результатов

**ORDER BY** позволяет сортировать результаты по одному или нескольким столбцам.

### 4.1 Сортировка по одному столбцу

**ASC (по возрастанию) — по умолчанию:**

```sql
-- Сортировка по возрасту (от меньшего к большему)
SELECT name, age
FROM users
ORDER BY age;
```

**Output:**
```
name  | age
------+-----
Иван  | 25
Петр  | 28
Мария | 30
```

**DESC (по убыванию):**

```sql
-- Сортировка по возрасту (от большего к меньшему)
SELECT name, age
FROM users
ORDER BY age DESC;
```

**Output:**
```
name  | age
------+-----
Мария | 30
Петр  | 28
Иван  | 25
```

### 4.2 Сортировка по нескольким столбцам

```sql
-- Сначала по возрасту (DESC), затем по имени (ASC)
SELECT name, age, email
FROM users
ORDER BY age DESC, name;
```

**Output:**
```
name  | age | email
------+-----+--------------------
Мария | 30  | maria@example.com
Петр  | 28  | petr@example.com
Иван  | 25  | ivan@example.com
```

### 4.3 Сортировка по номеру столбца

Можно указывать номер столбца вместо имени:

```sql
-- Сортировка по второму столбцу (age)
SELECT name, age
FROM users
ORDER BY 2 DESC;
```

> **💡 Pro Tip:**  
> Сортировка по номеру столбца менее читаема. Используйте имена столбцов для ясности.

### 4.4 Сортировка по выражению

```sql
-- Сортировка по длине имени
SELECT name, LENGTH(name) AS name_length
FROM users
ORDER BY LENGTH(name) DESC;
```

**Output:**
```
name  | name_length
------+------------
Мария | 5
Иван  | 4
Петр  | 4
```

---

## 5. LIMIT и OFFSET — ограничение результатов

**LIMIT** ограничивает количество возвращаемых строк.

### 5.1 LIMIT

```sql
-- Первые 2 пользователя
SELECT name, age
FROM users
ORDER BY age
LIMIT 2;
```

**Output:**
```
name  | age
------+-----
Иван  | 25
Петр  | 28
```

### 5.2 LIMIT с OFFSET

**OFFSET** пропускает указанное количество строк:

```sql
-- Пропустить первые 2, взять следующие 2
SELECT name, age
FROM users
ORDER BY age
LIMIT 2 OFFSET 2;
```

**Output:**
```
name  | age
------+-----
Мария | 30
```

**Альтернативный синтаксис (PostgreSQL, MySQL):**

```sql
-- Эквивалентно LIMIT 2 OFFSET 2
SELECT name, age
FROM users
ORDER BY age
LIMIT 2, 2;  -- MySQL синтаксис
```

### 5.3 Пагинация

**LIMIT и OFFSET часто используются для пагинации:**

```sql
-- Страница 1 (первые 10 записей)
SELECT name, age
FROM users
ORDER BY id
LIMIT 10 OFFSET 0;

-- Страница 2 (следующие 10 записей)
SELECT name, age
FROM users
ORDER BY id
LIMIT 10 OFFSET 10;

-- Страница 3 (следующие 10 записей)
SELECT name, age
FROM users
ORDER BY id
LIMIT 10 OFFSET 20;
```

> **💡 Pro Tip:**  
> Для больших OFFSET значения производительность может страдать. Рассмотрите курсоры или другие методы пагинации.

---

## 6. Алиасы (псевдонимы)

**Алиасы** позволяют переименовать столбцы или таблицы в результате запроса.

### 6.1 Алиасы столбцов

**AS ключевое слово (опционально):**

```sql
-- Переименовать столбцы в результате
SELECT 
    name AS user_name,
    age AS user_age,
    email AS user_email
FROM users;
```

**Output:**
```
user_name | user_age | user_email
----------+----------+--------------------
Иван      | 25       | ivan@example.com
Мария     | 30       | maria@example.com
Петр      | 28       | petr@example.com
```

**Без AS (тоже работает):**

```sql
SELECT name user_name, age user_age
FROM users;
```

### 6.2 Алиасы таблиц

**Алиасы таблиц полезны при работе с несколькими таблицами:**

```sql
-- Пока простой пример
SELECT u.name, u.age
FROM users AS u;
```

**Без AS:**

```sql
SELECT u.name, u.age
FROM users u;
```

---

## 7. DISTINCT — уникальные значения

**DISTINCT** убирает дубликаты из результата.

### 7.1 DISTINCT по одному столбцу

```sql
-- Уникальные возрасты
SELECT DISTINCT age
FROM users
ORDER BY age;
```

**Output:**
```
age
-----
25
28
30
```

### 7.2 DISTINCT по нескольким столбцам

```sql
-- Уникальные комбинации имени и возраста
SELECT DISTINCT name, age
FROM users;
```

**DISTINCT применяется ко всей строке**, а не к отдельным столбцам.

---

## 8. Полный пример запроса

**Объединим все изученное:**

```sql
SELECT 
    name AS user_name,
    age AS user_age,
    email
FROM users
WHERE age >= 25 
  AND email LIKE '%@example.com'
ORDER BY age DESC, name
LIMIT 10;
```

**Что делает этот запрос:**

1. Выбирает столбцы `name`, `age`, `email` с алиасами
2. Из таблицы `users`
3. Фильтрует: возраст >= 25 И email содержит '@example.com'
4. Сортирует: сначала по возрасту (DESC), затем по имени
5. Ограничивает результат 10 строками

---

## 9. Практические примеры

### 9.1 Поиск пользователей по имени

```sql
-- Найти всех пользователей с именем, содержащим "Ив"
SELECT name, email
FROM users
WHERE name LIKE '%Ив%'
ORDER BY name;
```

### 9.2 Пользователи в определённом возрастном диапазоне

```sql
-- Пользователи от 20 до 35 лет, отсортированные по возрасту
SELECT name, age, email
FROM users
WHERE age BETWEEN 20 AND 35
ORDER BY age;
```

### 9.3 Топ-5 самых старых пользователей

```sql
-- 5 самых старых пользователей
SELECT name, age
FROM users
WHERE age IS NOT NULL
ORDER BY age DESC
LIMIT 5;
```

### 9.4 Пользователи с определёнными возрастами

```sql
-- Пользователи возрастом 25, 30 или 35 лет
SELECT name, age
FROM users
WHERE age IN (25, 30, 35)
ORDER BY age, name;
```

---

## 10. Частые ошибки и best practices

### 10.1 SELECT *

**❌ Плохо:**

```sql
SELECT * FROM users WHERE age > 25;
```

**✅ Хорошо:**

```sql
SELECT name, email, age FROM users WHERE age > 25;
```

**Почему:** Явное указание столбцов делает запрос понятнее и может улучшить производительность.

### 10.2 NULL в условиях

**❌ Неправильно:**

```sql
SELECT * FROM users WHERE age = NULL;  -- Не работает!
```

**✅ Правильно:**

```sql
SELECT * FROM users WHERE age IS NULL;
```

### 10.3 Порядок условий WHERE

**❌ Медленно (если age не индексирован):**

```sql
SELECT * FROM users 
WHERE LENGTH(name) > 5 AND age > 25;
```

**✅ Быстрее (если age индексирован):**

```sql
SELECT * FROM users 
WHERE age > 25 AND LENGTH(name) > 5;
```

> **💡 Pro Tip:**  
> Ставьте более селективные условия первыми, особенно если они используют индексы.

### 10.4 LIMIT без ORDER BY

**❌ Непредсказуемый порядок:**

```sql
SELECT * FROM users LIMIT 10;
```

**✅ Предсказуемый порядок:**

```sql
SELECT * FROM users ORDER BY id LIMIT 10;
```

> **⚠️ Warning:**  
> Без ORDER BY порядок строк не гарантирован. Всегда используйте ORDER BY с LIMIT.

---

## 💡 Key Takeaways

- **SELECT** — выборка столбцов, **FROM** — выбор таблицы, **WHERE** — фильтрация строк

- **ORDER BY** — сортировка результатов (ASC по умолчанию, DESC для убывания)

- **LIMIT** — ограничение количества строк, **OFFSET** — пропуск строк

- **WHERE условия**: `=`, `<>`, `<`, `>`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`

- **Всегда указывайте конкретные столбцы** вместо `SELECT *` в production коде

---

## 🚀 Next Steps

**Related Modules:**

- [03_Data_Types](../03_Data_Types/) — Типы данных и работа с NULL
- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY

**Practice Ideas:**

1. Создайте таблицу с данными о сотрудниках и выполните различные SELECT запросы
2. Попробуйте все операторы WHERE на практике
3. Реализуйте пагинацию с LIMIT и OFFSET
4. Экспериментируйте с сортировкой по нескольким столбцам

**Going Deeper:**

- Изучите различия в синтаксисе LIMIT/OFFSET между разными СУБД
- Изучите производительность различных WHERE условий
- Изучите использование индексов для ускорения WHERE условий

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) — документация SELECT
- [MySQL SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html) — документация SELECT

**Articles:**

- [SQL WHERE Clause](https://www.w3schools.com/sql/sql_where.asp) — подробное руководство по WHERE
- [SQL ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp) — сортировка в SQL

---


