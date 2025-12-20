# INSERT, UPDATE, DELETE
## Модификация данных: INSERT INTO, UPDATE SET, DELETE FROM, введение в транзакции

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис SELECT запросов
- Понимать типы данных в SQL
- Иметь представление о структуре таблиц

**Recommended prior modules:**

- [02_Basic_Select](../02_Basic_Select/) — Базовый SELECT: выборка данных
- [03_Data_Types](../03_Data_Types/) — Типы данных и NULL

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Вставлять данные в таблицы с помощью INSERT
- Обновлять существующие записи с помощью UPDATE
- Удалять записи с помощью DELETE
- Понимать концепцию транзакций и использовать BEGIN/COMMIT/ROLLBACK
- Применять безопасные практики модификации данных

---

## 1. INSERT — вставка данных

**INSERT** позволяет добавлять новые строки в таблицу.

### 1.1 Базовый синтаксис INSERT

**Простая вставка:**

```sql

INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

**Пример:**

```sql

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER
);

INSERT INTO users (id, name, email, age)
VALUES (1, 'Иван', 'ivan@example.com', 25);
```

**Проверка:**

```sql

SELECT * FROM users;
```

**Output:**
```

id | name | email              | age
---+------+--------------------+-----
1  | Иван | ivan@example.com  | 25
```

### 1.2 INSERT без указания столбцов

**Если вставляем значения для всех столбцов в порядке их определения:**

```sql

INSERT INTO users
VALUES (2, 'Мария', 'maria@example.com', 30);
```

> **⚠️ Warning:**  
> Такой подход хрупкий — при изменении структуры таблицы запрос может сломаться. Всегда указывайте столбцы явно.

### 1.3 INSERT нескольких строк

**Вставка нескольких строк за раз:**

```sql

INSERT INTO users (id, name, email, age)
VALUES 
    (3, 'Петр', 'petr@example.com', 28),
    (4, 'Анна', 'anna@example.com', 22),
    (5, 'Сергей', 'sergey@example.com', 35);
```

**Output:**
```

id | name   | email               | age
---+--------+---------------------+-----
1  | Иван   | ivan@example.com   | 25
2  | Мария  | maria@example.com  | 30
3  | Петр   | petr@example.com   | 28
4  | Анна   | anna@example.com   | 22
5  | Сергей | sergey@example.com | 35
```

### 1.4 INSERT с DEFAULT значениями

**Использование DEFAULT:**

```sql

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Использование DEFAULT
INSERT INTO products (name)
VALUES ('Товар 1');

-- Явное указание DEFAULT
INSERT INTO products (name, price)
VALUES ('Товар 2', DEFAULT);
```

**Output:**
```

id | name    | price | created_at
---+---------+-------+----------------------------
1  | Товар 1 | 0.00  | 2024-12-10 14:30:00
2  | Товар 2 | 0.00  | 2024-12-10 14:30:01
```

### 1.5 INSERT с NULL

**Вставка NULL значений:**

```sql

INSERT INTO users (id, name, email, age)
VALUES (6, 'Ольга', 'olga@example.com', NULL);
```

### 1.6 INSERT ... SELECT

**Вставка данных из другой таблицы:**

```sql

-- Создадим таблицу для новых пользователей
CREATE TABLE new_users (
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER
);

INSERT INTO new_users VALUES
    ('Дмитрий', 'dmitry@example.com', 27),
    ('Елена', 'elena@example.com', 29);

-- Вставка из другой таблицы
INSERT INTO users (id, name, email, age)
SELECT 
    7,
    name,
    email,
    age
FROM new_users
WHERE age > 25;
```

**Output:**
```

id | name    | email               | age
---+---------+---------------------+-----
7  | Дмитрий | dmitry@example.com  | 27
8  | Елена   | elena@example.com   | 29
```

### 1.7 INSERT ... RETURNING (PostgreSQL)

**Возврат вставленных данных:**

```sql

INSERT INTO users (id, name, email, age)
VALUES (9, 'Алексей', 'alexey@example.com', 31)
RETURNING id, name;
```

**Output:**
```

id | name
---+--------
9  | Алексей
```

---

## 2. UPDATE — обновление данных

**UPDATE** позволяет изменять существующие записи в таблице.

### 2.1 Базовый синтаксис UPDATE

**Обновление всех строк (осторожно!):**

```sql

-- Обновить всех пользователей (ОПАСНО!)
UPDATE users SET age = age + 1;
```

> **⚠️ Warning:**  
> Без WHERE условие UPDATE изменит ВСЕ строки в таблице! Всегда проверяйте условие перед выполнением.

### 2.2 UPDATE с WHERE

**Обновление конкретных строк:**

```sql

-- Обновить возраст конкретного пользователя
UPDATE users
SET age = 26
WHERE id = 1;
```

**Проверка:**

```sql

SELECT id, name, age FROM users WHERE id = 1;
```

**Output:**
```

id | name | age
---+------+-----
1  | Иван | 26
```

### 2.3 UPDATE нескольких столбцов

**Обновление нескольких столбцов одновременно:**

```sql

UPDATE users
SET 
    name = 'Иван Иванов',
    email = 'ivan.ivanov@example.com',
    age = 27
WHERE id = 1;
```

### 2.4 UPDATE с выражениями

**Использование выражений в SET:**

```sql

-- Увеличить возраст всех пользователей на 1
UPDATE users
SET age = age + 1
WHERE age IS NOT NULL;

-- Установить дату обновления
ALTER TABLE users ADD COLUMN updated_at TIMESTAMP;

UPDATE users
SET updated_at = CURRENT_TIMESTAMP
WHERE updated_at IS NULL;
```

### 2.5 UPDATE с подзапросами

**Использование подзапросов в UPDATE:**

```sql

-- Обновить цену товара на основе средней цены
CREATE TABLE products (
    id INTEGER,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    category_id INTEGER
);

-- Установить цену равной средней цене в категории
UPDATE products p1
SET price = (
    SELECT AVG(price)
    FROM products p2
    WHERE p2.category_id = p1.category_id
)
WHERE price IS NULL;
```

### 2.6 UPDATE ... RETURNING (PostgreSQL)

**Возврат обновлённых данных:**

```sql

UPDATE users
SET age = 30
WHERE id = 2
RETURNING id, name, age;
```

**Output:**
```

id | name  | age
---+-------+-----
2  | Мария | 30
```

---

## 3. DELETE — удаление данных

**DELETE** позволяет удалять строки из таблицы.

### 3.1 Базовый синтаксис DELETE

**Удаление всех строк (ОПАСНО!):**

```sql

-- Удалить всех пользователей (ОПАСНО!)
DELETE FROM users;
```

> **⚠️ Warning:**  
> Без WHERE условие DELETE удалит ВСЕ строки в таблице! Всегда используйте WHERE.

### 3.2 DELETE с WHERE

**Удаление конкретных строк:**

```sql

-- Удалить пользователя по ID
DELETE FROM users
WHERE id = 9;
```

**Удаление по условию:**

```sql

-- Удалить пользователей младше 18 лет
DELETE FROM users
WHERE age < 18;
```

### 3.3 DELETE с подзапросами

**Использование подзапросов в DELETE:**

```sql

-- Удалить пользователей без заказов
CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    amount DECIMAL(10, 2)
);

DELETE FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM orders
    WHERE user_id IS NOT NULL
);
```

### 3.4 DELETE ... RETURNING (PostgreSQL)

**Возврат удалённых данных:**

```sql

DELETE FROM users
WHERE age > 40
RETURNING id, name, age;
```

**Output:**
```

id | name   | age
---+--------+-----
5  | Сергей | 35
```

---

## 4. Транзакции

**Транзакция** — это последовательность операций, которая выполняется как единое целое. Либо все операции выполняются успешно, либо ни одна.

### 4.1 ACID свойства

**ACID** — основные свойства транзакций:

- **Atomicity (Атомарность)** — все или ничего

- **Consistency (Согласованность)** — данные остаются валидными

- **Isolation (Изоляция)** — транзакции не мешают друг другу

- **Durability (Долговечность)** — изменения сохраняются

### 4.2 BEGIN, COMMIT, ROLLBACK

**BEGIN** — начало транзакции:

```sql

BEGIN;

INSERT INTO users (id, name, email, age)
VALUES (10, 'Тест', 'test@example.com', 25);

-- Пока не закоммитили, изменения видны только в этой транзакции
SELECT * FROM users WHERE id = 10;
```

**COMMIT** — подтверждение изменений:

```sql

BEGIN;

UPDATE users SET age = 30 WHERE id = 1;
INSERT INTO users (id, name, email, age) VALUES (11, 'Новый', 'new@example.com', 20);

COMMIT;  -- Все изменения сохраняются
```

**ROLLBACK** — откат изменений:

```sql

BEGIN;

UPDATE users SET age = 100 WHERE id = 1;
DELETE FROM users WHERE id = 2;

-- Передумали, откатываем
ROLLBACK;  -- Все изменения отменяются

-- Проверяем, что изменения не применились
SELECT * FROM users WHERE id IN (1, 2);
```

### 4.3 Пример транзакции

**Перевод денег между счетами:**

```sql

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(10, 2)
);

INSERT INTO accounts VALUES
    (1, 'Алиса', 1000.00),
    (2, 'Боб', 500.00);

-- Перевод 200 от Алисы к Бобу
BEGIN;

UPDATE accounts SET balance = balance - 200 WHERE id = 1;
UPDATE accounts SET balance = balance + 200 WHERE id = 2;

-- Проверяем балансы
SELECT * FROM accounts;

-- Если всё правильно, коммитим
COMMIT;
```

**Output после COMMIT:**
```

id | name  | balance
---+-------+--------
1  | Алиса | 800.00
2  | Боб   | 700.00
```

**Если что-то пошло не так:**

```sql

BEGIN;

UPDATE accounts SET balance = balance - 200 WHERE id = 1;
-- Ошибка при обновлении второго счёта
UPDATE accounts SET balance = balance + 200 WHERE id = 999;  -- Несуществующий ID

-- Откатываем всё
ROLLBACK;

-- Балансы не изменились
SELECT * FROM accounts;
```

### 4.4 Автокоммит

**По умолчанию каждая команда — отдельная транзакция:**

```sql

-- Автоматически коммитится
INSERT INTO users (id, name) VALUES (12, 'Авто');

-- Эквивалентно:
BEGIN;
INSERT INTO users (id, name) VALUES (12, 'Авто');
COMMIT;
```

**Отключение автокоммита (зависит от СУБД и клиента):**

```sql

-- PostgreSQL
SET autocommit = off;

-- Теперь нужно явно коммитить
INSERT INTO users (id, name) VALUES (13, 'Ручной');
COMMIT;
```

---

## 5. Безопасные практики

### 5.1 Всегда используйте WHERE

**❌ Опасно:**

```sql

UPDATE users SET age = 0;  -- Обновит всех!
DELETE FROM users;  -- Удалит всех!
```

**✅ Безопасно:**

```sql

UPDATE users SET age = 0 WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

### 5.2 Проверка перед удалением

**Сначала SELECT, потом DELETE:**

```sql

-- 1. Проверяем, что удалим
SELECT * FROM users WHERE age < 18;

-- 2. Если всё правильно, удаляем
DELETE FROM users WHERE age < 18;
```

### 5.3 Использование транзакций

**Обёртывание изменений в транзакции:**

```sql

BEGIN;

-- Все изменения
UPDATE users SET age = age + 1 WHERE id = 1;
INSERT INTO logs (message) VALUES ('User updated');

-- Проверяем результат
SELECT * FROM users WHERE id = 1;

-- Если всё ОК, коммитим
COMMIT;
```

### 5.4 Резервное копирование

**Перед массовыми изменениями:**

```sql

-- Создаём резервную копию
CREATE TABLE users_backup AS SELECT * FROM users;

-- Теперь можно безопасно изменять
BEGIN;
UPDATE users SET age = age + 1;
-- Если что-то не так:
-- ROLLBACK;
-- И восстановить: INSERT INTO users SELECT * FROM users_backup;
COMMIT;
```

---

## 6. Ограничения и ошибки

### 6.1 Ошибки при INSERT

**Нарушение ограничений:**

```sql

-- Попытка вставить дубликат первичного ключа
INSERT INTO users (id, name) VALUES (1, 'Дубликат');
-- Ошибка: duplicate key value violates unique constraint

-- Попытка вставить NULL в NOT NULL столбец
ALTER TABLE users ALTER COLUMN name SET NOT NULL;
INSERT INTO users (id, name) VALUES (14, NULL);

-- Ошибка: null value in column "name" violates not-null constraint
```

### 6.2 Ошибки при UPDATE

**Обновление несуществующих строк:**

```sql

-- UPDATE не выдаёт ошибку, если строки не найдены
UPDATE users SET age = 100 WHERE id = 999;

-- Выполнится успешно, но 0 строк обновлено
```

**Проверка количества обновлённых строк:**

```sql

-- PostgreSQL: использовать RETURNING
UPDATE users SET age = 100 WHERE id = 999
RETURNING *;

-- Вернёт пустой результат, если строка не найдена
```

### 6.3 Ошибки при DELETE

**Каскадное удаление:**

```sql

-- Если есть внешние ключи с ON DELETE CASCADE
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

-- Удаление пользователя удалит и его заказы
DELETE FROM users WHERE id = 1;

-- Автоматически удалятся все заказы этого пользователя
```

---

## 7. UPSERT (INSERT ... ON CONFLICT)

**UPSERT** — вставка или обновление, если запись уже существует.

### 7.1 PostgreSQL: ON CONFLICT

```sql

-- Вставка, если нет, обновление, если есть
INSERT INTO users (id, name, email, age)
VALUES (1, 'Иван Обновлённый', 'ivan.new@example.com', 26)
ON CONFLICT (id) 
DO UPDATE SET 
    name = EXCLUDED.name,
    email = EXCLUDED.email,
    age = EXCLUDED.age;
```

**EXCLUDED** — ссылка на значения из INSERT.

### 7.2 MySQL: INSERT ... ON DUPLICATE KEY UPDATE

```sql

-- MySQL синтаксис
INSERT INTO users (id, name, email, age)
VALUES (1, 'Иван Обновлённый', 'ivan.new@example.com', 26)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    email = VALUES(email),
    age = VALUES(age);
```

---

## 💡 Key Takeaways

- **INSERT** — вставка новых строк. Всегда указывайте столбцы явно

- **UPDATE** — обновление существующих строк. Всегда используйте WHERE!

- **DELETE** — удаление строк. Всегда используйте WHERE!

- **Транзакции** — BEGIN/COMMIT/ROLLBACK для атомарности операций

- **Безопасность** — проверяйте данные перед изменением, используйте транзакции

---

## 🚀 Next Steps

**Related Modules:**

- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY
- [13_Transactions](../13_Transactions/) — SQL и транзакции (детально)

**Practice Ideas:**

1. Создайте таблицу и попрактикуйтесь с INSERT, UPDATE, DELETE
2. Попробуйте транзакции: BEGIN, несколько операций, COMMIT/ROLLBACK
3. Создайте сценарий перевода денег между счетами с транзакциями
4. Попробуйте UPSERT операции

**Going Deeper:**

- Изучите уровни изоляции транзакций
- Изучите блокировки в СУБД
- Изучите триггеры и хранимые процедуры

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL INSERT](https://www.postgresql.org/docs/current/sql-insert.html) — документация INSERT
- [PostgreSQL UPDATE](https://www.postgresql.org/docs/current/sql-update.html) — документация UPDATE
- [PostgreSQL DELETE](https://www.postgresql.org/docs/current/sql-delete.html) — документация DELETE

**Articles:**

- [SQL Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) — транзакции в PostgreSQL
- [UPSERT Patterns](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT) — паттерны UPSERT

---


