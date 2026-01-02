# Типы данных и NULL
## Числовые, строковые типы, даты и время, NULL и трёхзначная логика

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать структуру таблиц (строки, столбцы)
- Иметь опыт работы с типами данных в программировании

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать числовые типы данных и выбирать подходящий тип
- Работать со строковыми типами и понимать различия между ними
- Использовать типы даты и времени для работы с временными данными
- Понимать концепцию NULL и трёхзначной логики в SQL
- Правильно обрабатывать NULL значения в запросах

---

## 1. Введение в типы данных

**Тип данных** определяет, какие значения может хранить столбец и какие операции с ним можно выполнять. Правильный выбор типа данных критичен для производительности и целостности данных.

### 1.1 Зачем нужны типы данных

**Преимущества типизации:**

- ✅ **Валидация данных** — СУБД проверяет корректность значений
- ✅ **Эффективное хранение** — оптимизация размера и скорости
- ✅ **Производительность** — индексы и операции работают быстрее
- ✅ **Семантика** — код становится понятнее

**Пример проблемы без типов:**

```sql
-- Если age хранится как строка
SELECT * FROM users WHERE age > 25;  -- Может работать неправильно!
-- "30" > "25" = true, но "9" > "25" = false (лексикографическое сравнение)
```

---

## 2. Числовые типы данных

### 2.1 Целые числа (INTEGER)

**Основные типы:**

| Тип | Размер | Диапазон (PostgreSQL) | Когда использовать |
|-----|--------|----------------------|-------------------|
| `SMALLINT` | 2 байта | -32,768 до 32,767 | Ограниченные значения (возраст, год) |
| `INTEGER` или `INT` | 4 байта | -2,147,483,648 до 2,147,483,647 | Большинство случаев (ID, счётчики) |
| `BIGINT` | 8 байт | -9,223,372,036,854,775,808 до 9,223,372,036,854,775,807 | Большие числа (timestamp, большие ID) |

**Пример:**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    age SMALLINT,
    views_count BIGINT
);

INSERT INTO users VALUES (1, 25, 1000000);
```

**Output:**
```
id | age | views_count
---+-----+------------
1  | 25  | 1000000
```

### 2.2 Числа с плавающей точкой

**Типы:**

| Тип | Размер | Точность | Когда использовать |
|-----|--------|----------|-------------------|
| `REAL` | 4 байта | ~6 знаков | Быстрые вычисления, не критична точность |
| `DOUBLE PRECISION` | 8 байт | ~15 знаков | Научные вычисления |
| `NUMERIC` или `DECIMAL` | Переменный | Точная | Деньги, точные расчёты |

**Пример:**

```sql
CREATE TABLE products (
    id INTEGER,
    price DECIMAL(10, 2),  -- 10 цифр всего, 2 после запятой
    weight REAL,
    rating DOUBLE PRECISION
);

INSERT INTO products VALUES 
    (1, 99.99, 1.5, 4.56789012345);
```

**Output:**
```
id | price | weight | rating
---+-------+--------+---------------
1  | 99.99 | 1.5    | 4.56789012345
```

> **⚠️ Warning:**  
> Для денег всегда используйте `DECIMAL` или `NUMERIC`, не `REAL` или `DOUBLE PRECISION`. Плавающая точка может давать ошибки округления.

**Пример проблемы с плавающей точкой:**

```sql
-- Проблема точности
SELECT 0.1 + 0.2;  -- Может быть не 0.3!

-- Решение: DECIMAL
SELECT CAST(0.1 AS DECIMAL(10,2)) + CAST(0.2 AS DECIMAL(10,2));  -- 0.30
```

### 2.3 SERIAL и AUTO_INCREMENT

**Автоинкремент для первичных ключей:**

**PostgreSQL:**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- Автоматически увеличивается
    name VARCHAR(100)
);

INSERT INTO users (name) VALUES ('Иван');
INSERT INTO users (name) VALUES ('Мария');
```

**MySQL:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

**Output:**
```
id | name
---+-------
1  | Иван
2  | Мария
```

---

## 3. Строковые типы данных

### 3.1 VARCHAR и CHAR

**VARCHAR (Variable Character):**

- Хранит строки переменной длины
- Экономит место (хранит только реальную длину)
- Максимальная длина указывается: `VARCHAR(n)`

**CHAR (Character):**

- Хранит строки фиксированной длины
- Всегда занимает указанное количество символов
- Дополняется пробелами справа

**Пример:**

```sql
CREATE TABLE test_strings (
    id INTEGER,
    var_col VARCHAR(10),
    char_col CHAR(10)
);

INSERT INTO test_strings VALUES (1, 'Hi', 'Hi');
```

**Размер в памяти:**

```sql
SELECT 
    id,
    var_col,
    LENGTH(var_col) AS var_length,
    char_col,
    LENGTH(char_col) AS char_length
FROM test_strings;
```

**Output:**
```
id | var_col | var_length | char_col | char_length
---+---------+------------+----------+------------
1  | Hi      | 2          | Hi       | 10
```

> **💡 Pro Tip:**  
> Используйте `VARCHAR` в большинстве случаев. `CHAR` полезен только для фиксированных форматов (коды, статусы).

### 3.2 TEXT

**TEXT** — для длинных строк без ограничения длины (или очень больших).

**PostgreSQL:**
```sql
CREATE TABLE articles (
    id INTEGER,
    title VARCHAR(200),
    content TEXT  -- Может быть очень длинным
);
```

**MySQL:**

- `TEXT` — до 65,535 символов
- `MEDIUMTEXT` — до 16,777,215 символов
- `LONGTEXT` — до 4,294,967,295 символов

### 3.3 Сравнение VARCHAR и TEXT

| Критерий | VARCHAR(n) | TEXT |
|----------|-----------|------|
| Максимальная длина | Ограничена (n) | Очень большая |
| Индексация | Полная поддержка | Ограниченная (первые N символов) |
| Производительность | Быстрее для коротких строк | Медленнее |
| Когда использовать | Известна максимальная длина | Длинный контент |

---

## 4. Типы даты и времени

### 4.1 DATE

**DATE** — хранит только дату (без времени).

```sql
CREATE TABLE events (
    id INTEGER,
    event_name VARCHAR(100),
    event_date DATE
);

INSERT INTO events VALUES 
    (1, 'Конференция', '2024-12-25'),
    (2, 'Встреча', '2024-01-15');
```

**Формат:** `'YYYY-MM-DD'` (ISO 8601)

**Операции с датами:**

```sql
-- Разница в днях
SELECT 
    event_name,
    event_date,
    event_date - CURRENT_DATE AS days_until
FROM events;
```

**Output:**
```
event_name  | event_date | days_until
------------+------------+-----------
Конференция | 2024-12-25 | 15
Встреча     | 2024-01-15 | -344
```

### 4.2 TIME

**TIME** — хранит только время (без даты).

```sql
CREATE TABLE schedule (
    id INTEGER,
    task VARCHAR(100),
    start_time TIME
);

INSERT INTO schedule VALUES 
    (1, 'Завтрак', '08:00:00'),
    (2, 'Обед', '13:30:00');
```

**Формат:** `'HH:MM:SS'` или `'HH:MM:SS.microseconds'`

### 4.3 TIMESTAMP

**TIMESTAMP** — дата и время вместе.

**PostgreSQL:**
```sql
CREATE TABLE logs (
    id INTEGER,
    message TEXT,
    created_at TIMESTAMP
);

INSERT INTO logs VALUES 
    (1, 'User logged in', '2024-12-10 14:30:00');
```

**TIMESTAMP WITH TIME ZONE (TIMESTAMPTZ):**

```sql
CREATE TABLE events_tz (
    id INTEGER,
    event_name VARCHAR(100),
    event_time TIMESTAMPTZ  -- С учётом часового пояса
);

INSERT INTO events_tz VALUES 
    (1, 'Webinar', '2024-12-10 15:00:00+03:00');
```

> **💡 Pro Tip:**  
> В PostgreSQL предпочитайте `TIMESTAMPTZ` для хранения времени с учётом часового пояса.

### 4.4 Функции работы с датами

**Текущая дата и время:**

```sql
-- Текущая дата
SELECT CURRENT_DATE;

-- Текущее время
SELECT CURRENT_TIME;

-- Текущая дата и время
SELECT CURRENT_TIMESTAMP;
SELECT NOW();  -- Альтернатива
```

**Извлечение частей даты:**

```sql
SELECT 
    created_at,
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    EXTRACT(DAY FROM created_at) AS day
FROM logs;
```

**Арифметика с датами:**

```sql
-- Добавить интервал
SELECT CURRENT_DATE + INTERVAL '7 days' AS next_week;

-- Вычесть интервал
SELECT CURRENT_DATE - INTERVAL '1 month' AS last_month;
```

---

## 5. BOOLEAN тип

**BOOLEAN** — логический тип (true/false).

**PostgreSQL:**
```sql
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    is_active BOOLEAN,
    is_verified BOOLEAN DEFAULT false
);

INSERT INTO users VALUES 
    (1, 'Иван', true, true),
    (2, 'Мария', false, false);
```

**MySQL:**

- Использует `TINYINT(1)` или `BOOLEAN` (синоним)

**Запросы:**

```sql
-- Найти активных пользователей
SELECT name FROM users WHERE is_active = true;
-- Или просто:
SELECT name FROM users WHERE is_active;
```

---

## 6. NULL — отсутствие значения

### 6.1 Что такое NULL

**NULL** — это специальное значение, означающее "отсутствие данных" или "неизвестное значение".

**NULL ≠ 0, NULL ≠ пустая строка, NULL ≠ false**

```sql
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(100)
);

INSERT INTO users VALUES 
    (1, 'Иван', 25, 'ivan@example.com'),
    (2, 'Мария', NULL, 'maria@example.com'),  -- Возраст неизвестен
    (3, 'Петр', 30, NULL);  -- Email неизвестен
```

**Output:**
```
id | name  | age | email
---+-------+-----+--------------------
1  | Иван  | 25  | ivan@example.com
2  | Мария |     | maria@example.com
3  | Петр  | 30  |
```

### 6.2 Проверка на NULL

**IS NULL и IS NOT NULL:**

```sql
-- Пользователи без указанного возраста
SELECT name FROM users WHERE age IS NULL;
```

**Output:**
```
name
-----
Мария
```

```sql
-- Пользователи с указанным возрастом
SELECT name FROM users WHERE age IS NOT NULL;
```

**Output:**
```
name
-----
Иван
Петр
```

> **⚠️ Warning:**  
> Нельзя использовать `= NULL` или `!= NULL`. Всегда используйте `IS NULL` или `IS NOT NULL`.

### 6.3 Трёхзначная логика

**В SQL логика трёхзначная:**

- `TRUE` — истина
- `FALSE` — ложь
- `UNKNOWN` — неизвестно (когда участвует NULL)

**Примеры:**

```sql
-- NULL в сравнениях
SELECT 
    NULL = NULL,      -- NULL (не true!)
    NULL != NULL,     -- NULL
    5 = NULL,         -- NULL
    5 != NULL;        -- NULL
```

**Output:**
```
?column? | ?column? | ?column? | ?column?
---------+---------+---------+---------
         |         |         |
```

**Логические операции с NULL:**

```sql
-- AND
SELECT 
    TRUE AND NULL,    -- NULL
    FALSE AND NULL,   -- FALSE
    NULL AND NULL;    -- NULL

-- OR
SELECT 
    TRUE OR NULL,     -- TRUE
    FALSE OR NULL,    -- NULL
    NULL OR NULL;     -- NULL
```

### 6.4 COALESCE — замена NULL

**COALESCE** возвращает первое не-NULL значение:

```sql
SELECT 
    name,
    age,
    COALESCE(age, 0) AS age_or_zero,
    COALESCE(email, 'No email') AS email_or_default
FROM users;
```

**Output:**
```
name  | age | age_or_zero | email_or_default
------+-----+-------------+-----------------
Иван  | 25  | 25          | ivan@example.com
Мария |     | 0           | maria@example.com
Петр  | 30  | 30          | No email
```

### 6.5 NULLIF — преобразование в NULL

**NULLIF** возвращает NULL, если два значения равны:

```sql
SELECT 
    name,
    NULLIF(age, 0) AS age_null_if_zero  -- NULL если age = 0
FROM users;
```

---

## 7. Выбор типа данных

### 7.1 Рекомендации

**Числа:**

- **ID, счётчики** → `INTEGER` или `BIGINT`

- **Деньги** → `DECIMAL(10, 2)` или `NUMERIC(10, 2)`

- **Проценты, рейтинги** → `DECIMAL(5, 2)` или `REAL`

**Строки:**

- **Короткие строки (имя, email)** → `VARCHAR(100)` или `VARCHAR(255)`

- **Длинный текст** → `TEXT`

- **Фиксированные коды** → `CHAR(n)`

**Даты:**

- **Только дата** → `DATE`

- **Дата и время** → `TIMESTAMP` или `TIMESTAMPTZ`

- **Только время** → `TIME`

### 7.2 Частые ошибки

**❌ Слишком большой тип:**

```sql
-- Плохо: BIGINT для возраста
age BIGINT

-- Хорошо: SMALLINT достаточно
age SMALLINT
```

**❌ Неправильный тип для денег:**

```sql
-- Плохо: REAL для денег
price REAL

-- Хорошо: DECIMAL для точности
price DECIMAL(10, 2)
```

**❌ VARCHAR без ограничения:**

```sql
-- Плохо: TEXT для коротких строк
email TEXT

-- Хорошо: VARCHAR с ограничением
email VARCHAR(255)
```

---

## 8. Преобразование типов (CAST)

### 8.1 CAST функция

**Преобразование типов:**

```sql
-- Строка в число
SELECT CAST('123' AS INTEGER);

-- Число в строку
SELECT CAST(123 AS VARCHAR);

-- Дата в строку
SELECT CAST(CURRENT_DATE AS VARCHAR);
```

**Альтернативный синтаксис:**

```sql
-- PostgreSQL, MySQL
SELECT '123'::INTEGER;
SELECT 123::VARCHAR;
```

### 8.2 Автоматическое преобразование

**Некоторые СУБД автоматически преобразуют типы:**

```sql
-- Автоматическое преобразование
SELECT '123' + 5;  -- Может работать в некоторых СУБД
```

> **💡 Pro Tip:**  
> Всегда явно указывайте преобразование типов для ясности и переносимости.

---

## 💡 Key Takeaways

- **Числовые типы**: `INTEGER` для большинства случаев, `DECIMAL` для денег, `BIGINT` для больших чисел

- **Строковые типы**: `VARCHAR(n)` для большинства строк, `TEXT` для длинного контента

- **Даты и время**: `DATE` для дат, `TIMESTAMP` или `TIMESTAMPTZ` для даты и времени

- **NULL** — это отсутствие значения, не 0 и не пустая строка. Используйте `IS NULL` для проверки

- **Трёхзначная логика** — в SQL есть TRUE, FALSE и UNKNOWN (когда участвует NULL)

---

## 🚀 Next Steps

**Related Modules:**

- [04_Insert_Update_Delete](../04_Insert_Update_Delete/) — Модификация данных
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

**Practice Ideas:**

1. Создайте таблицу с разными типами данных и вставьте тестовые данные
2. Экспериментируйте с NULL значениями и трёхзначной логикой
3. Попробуйте преобразование типов с помощью CAST
4. Сравните производительность VARCHAR и TEXT для коротких строк

**Going Deeper:**

- Изучите различия типов данных между PostgreSQL, MySQL и SQLite
- Изучите работу с часовыми поясами в TIMESTAMPTZ
- Изучите JSON и JSONB типы в PostgreSQL

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html) — все типы данных
- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html) — типы данных MySQL

**Articles:**

- [SQL NULL Explained](https://www.sqlshack.com/sql-null-explained/) — подробно о NULL
- [Choosing the Right Data Type](https://www.postgresql.org/docs/current/datatype.html) — выбор типа данных

---


