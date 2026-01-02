# SQL и транзакции
## ACID, BEGIN/COMMIT/ROLLBACK, уровни изоляции, блокировки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовые операции INSERT, UPDATE, DELETE
- Понимать концепцию транзакций (из лекции 04)
- Иметь представление о конкурентном доступе к данным

**Recommended prior modules:**

- [04_Insert_Update_Delete](../04_Insert_Update_Delete/) — INSERT, UPDATE, DELETE
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать свойства ACID транзакций
- Использовать BEGIN, COMMIT, ROLLBACK для управления транзакциями
- Различать уровни изоляции транзакций
- Понимать работу блокировок в СУБД
- Решать проблемы конкурентного доступа

---

## 1. ACID свойства

### 1.1 Atomicity (Атомарность)

**Все или ничего** — либо все операции выполняются, либо ни одна.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- Если что-то пошло не так:
ROLLBACK;  -- Откатываем всё
-- Или:
COMMIT;    -- Сохраняем всё
```

### 1.2 Consistency (Согласованность)

**Данные остаются валидными** — ограничения целостности соблюдаются.

```sql
BEGIN;
INSERT INTO orders (user_id, amount) VALUES (999, 100);  -- user_id не существует
-- Ошибка: нарушение внешнего ключа
ROLLBACK;  -- Транзакция откатывается, данные остаются согласованными
```

### 1.3 Isolation (Изоляция)

**Транзакции не мешают друг другу** — каждая транзакция видит согласованное состояние.

### 1.4 Durability (Долговечность)

**Изменения сохраняются** — после COMMIT данные гарантированно записаны на диск.

---

## 2. Уровни изоляции

### 2.1 Read Uncommitted

**Самый низкий уровень:**

- ✅ Нет блокировок на чтение
- ❌ Видны незакоммиченные изменения (dirty reads)
- ❌ Не рекомендуется использовать

### 2.2 Read Committed (по умолчанию в PostgreSQL)

**Чтение только закоммиченных данных:**

- ✅ Нет dirty reads
- ❌ Возможны non-repeatable reads (повторное чтение даёт другой результат)
- ❌ Возможны phantom reads

**Пример non-repeatable read:**

```sql
-- Транзакция 1
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- Транзакция 2
BEGIN;
UPDATE accounts SET balance = 900 WHERE id = 1;
COMMIT;

-- Транзакция 1 (продолжение)
SELECT balance FROM accounts WHERE id = 1;  -- 900 (изменилось!)
COMMIT;
```

### 2.3 Repeatable Read

**Повторяемое чтение:**

- ✅ Нет dirty reads
- ✅ Нет non-repeatable reads
- ❌ Возможны phantom reads

### 2.4 Serializable

**Самый высокий уровень:**

- ✅ Нет dirty reads
- ✅ Нет non-repeatable reads
- ✅ Нет phantom reads
- ❌ Самый медленный

### 2.5 Установка уровня изоляции

```sql
-- PostgreSQL
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- или
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## 3. Блокировки

### 3.1 Типы блокировок

**Shared Lock (блокировка на чтение):**

- Несколько транзакций могут читать одновременно
- Блокирует запись

**Exclusive Lock (блокировка на запись):**

- Только одна транзакция может писать
- Блокирует чтение и запись

### 3.2 Deadlock

**Взаимная блокировка:**

```sql
-- Транзакция 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;  -- Блокирует id=1
-- Ждёт разблокировки id=2

-- Транзакция 2
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 2;  -- Блокирует id=2
-- Ждёт разблокировки id=1

-- DEADLOCK! Одна из транзакций будет отменена
```

**Решение:**

- Всегда блокировать ресурсы в одинаковом порядке
- Использовать таймауты
- СУБД автоматически обнаруживает и разрешает deadlock

---

## 4. Практические примеры

### 4.1 Безопасный перевод денег

```sql
BEGIN;
-- Блокируем обе записи
SELECT * FROM accounts WHERE id IN (1, 2) FOR UPDATE;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
```

**FOR UPDATE** — блокирует строки для обновления.

### 4.2 Оптимистичная блокировка

**Использование версий:**

```sql
CREATE TABLE accounts (
    id INTEGER,
    balance DECIMAL(10, 2),
    version INTEGER  -- Версия для оптимистичной блокировки
);

-- Обновление с проверкой версии
UPDATE accounts 
SET balance = balance - 100, version = version + 1
WHERE id = 1 AND version = 5;  -- Проверяем версию

-- Если версия изменилась, обновление не произойдёт
-- Проверка: сколько строк обновлено
SELECT ROW_COUNT();  -- Если 0, значит версия изменилась
```

**Преимущества оптимистичной блокировки:**

- ✅ Нет блокировок на чтение
- ✅ Высокая производительность при низкой конкуренции
- ❌ Нужна обработка конфликтов в приложении

### 4.3 Пессимистичная блокировка

**FOR UPDATE блокирует строки:**

```sql
BEGIN;
-- Блокируем строку для обновления
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;

-- Другие транзакции не могут изменить эту строку
-- Пока мы не завершим транзакцию

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

**FOR UPDATE NOWAIT** — не ждать, если строка заблокирована:

```sql
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- Если строка заблокирована, получим ошибку сразу
```

**FOR UPDATE SKIP LOCKED** — пропустить заблокированные строки:

```sql
-- Обработка очереди задач
SELECT * FROM tasks 
WHERE status = 'pending' 
FOR UPDATE SKIP LOCKED 
LIMIT 1;
-- Пропустит заблокированные задачи
```

---

## 5. Savepoints (точки сохранения)

### 5.1 Что такое Savepoint

**Savepoint** — точка внутри транзакции, к которой можно откатиться.

```sql
BEGIN;

-- Начальные операции
INSERT INTO accounts (id, balance) VALUES (1, 1000);
SAVEPOINT sp1;

-- Промежуточные операции
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT sp2;

-- Если что-то пошло не так
ROLLBACK TO SAVEPOINT sp1;  -- Откат к sp1

-- Продолжаем транзакцию
COMMIT;
```

### 5.2 Практическое использование

**Обработка ошибок:**

```sql
BEGIN;
INSERT INTO orders (user_id, amount) VALUES (1, 100);
SAVEPOINT before_items;

BEGIN
    INSERT INTO order_items (order_id, product_id, quantity) 
    VALUES (1, 999, 1);  -- product_id не существует
EXCEPTION
    WHEN foreign_key_violation THEN
        ROLLBACK TO SAVEPOINT before_items;
        -- Продолжаем с другими товарами
END;

COMMIT;
```

---

## 6. MVCC (Multi-Version Concurrency Control)

### 6.1 Что такое MVCC

**MVCC** — механизм, позволяющий читать данные без блокировок.

**Как работает:**

- Каждая транзакция видит "снимок" данных на момент начала
- Изменения других транзакций не видны до COMMIT
- Старые версии данных сохраняются для читающих транзакций

**Преимущества:**

- ✅ Чтение не блокирует запись
- ✅ Запись не блокирует чтение
- ✅ Высокая производительность

### 6.2 Пример работы MVCC

```sql
-- Транзакция 1 (начало: 10:00)
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- Транзакция 2 (начало: 10:01)
BEGIN;
UPDATE accounts SET balance = 900 WHERE id = 1;
COMMIT;  -- 10:02

-- Транзакция 1 (продолжение: 10:03)
SELECT balance FROM accounts WHERE id = 1;  -- Всё ещё 1000!
-- Видит снимок на момент 10:00
COMMIT;
```

---

## 7. Phantom Reads

### 7.1 Что такое Phantom Read

**Phantom Read** — появление новых строк при повторном чтении.

**Пример:**

```sql
-- Транзакция 1
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT COUNT(*) FROM orders WHERE user_id = 1;  -- 5 заказов

-- Транзакция 2
BEGIN;
INSERT INTO orders (user_id, amount) VALUES (1, 100);
COMMIT;

-- Транзакция 1 (продолжение)
SELECT COUNT(*) FROM orders WHERE user_id = 1;  -- Всё ещё 5 (в Repeatable Read)
-- Но при SELECT * могут появиться новые строки в некоторых случаях
COMMIT;
```

### 7.2 Защита от Phantom Reads

**Serializable уровень изоляции:**

```sql
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- Гарантирует отсутствие phantom reads
```

---

## 8. Транзакции в приложениях

### 8.1 Автокоммит

**По умолчанию каждая команда — отдельная транзакция:**

```sql
-- Автокоммит включён (по умолчанию)
INSERT INTO users (name) VALUES ('Иван');
-- Автоматически COMMIT

-- Отключить автокоммит
SET autocommit = OFF;
-- Теперь нужно явно COMMIT
```

### 8.2 Транзакции в коде

**Python пример:**

```python
import psycopg2

conn = psycopg2.connect(...)
conn.autocommit = False  # Отключить автокоммит

try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ('Иван',))
    cursor.execute("INSERT INTO orders (user_id) VALUES (%s)", (user_id,))
    conn.commit()  # Сохранить все изменения
except Exception as e:
    conn.rollback()  # Откатить при ошибке
    raise
finally:
    conn.close()
```

### 8.3 Nested Transactions

**Некоторые СУБД поддерживают вложенные транзакции через savepoints:**

```sql
BEGIN;
-- Внешняя транзакция
SAVEPOINT inner;
-- Внутренняя "транзакция"
ROLLBACK TO SAVEPOINT inner;  -- Откат только внутренней
COMMIT;  -- Коммит внешней
```

---

## 9. Долговечность (Durability)

### 9.1 Гарантии записи

**После COMMIT данные гарантированно сохранены:**

```sql
BEGIN;
UPDATE accounts SET balance = 1000 WHERE id = 1;
COMMIT;
-- Данные записаны на диск, даже при сбое
```

### 9.2 WAL (Write-Ahead Logging)

**PostgreSQL использует WAL для долговечности:**

- Изменения сначала записываются в WAL
- Затем применяются к данным
- При сбое можно восстановить из WAL

### 9.3 Синхронная и асинхронная запись

**Настройки (PostgreSQL):**

```sql
-- Синхронная запись (по умолчанию)
synchronous_commit = on;
-- Гарантирует запись на диск перед возвратом COMMIT

-- Асинхронная запись (быстрее, но риск потери данных)
synchronous_commit = off;
-- COMMIT возвращается быстрее, но данные могут быть потеряны при сбое
```

---

## 10. Практические паттерны

### 10.1 Retry Pattern

**Повтор при deadlock:**

```python
max_retries = 3
for attempt in range(max_retries):
    try:
        conn.begin()
        # ... операции ...
        conn.commit()
        break
    except DeadlockDetected:
        conn.rollback()
        if attempt == max_retries - 1:
            raise
        time.sleep(0.1 * (attempt + 1))  # Экспоненциальная задержка
```

### 10.2 Two-Phase Commit

**Для распределённых транзакций:**

1. **Prepare Phase** — все участники готовы
2. **Commit Phase** — все коммитят или откатывают

### 10.3 Saga Pattern

**Для микросервисов (без распределённых транзакций):**

- Каждый сервис выполняет свою часть
- При ошибке — компенсирующие транзакции
- Нет глобального ACID, но есть согласованность

---

## 11. Мониторинг транзакций

### 11.1 Активные транзакции

**Просмотр активных транзакций (PostgreSQL):**

```sql
SELECT 
    pid,
    usename,
    application_name,
    state,
    query_start,
    state_change,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE state = 'active';
```

### 11.2 Долгие транзакции

**Найти долгие транзакции:**

```sql
SELECT 
    pid,
    now() - xact_start AS duration,
    state,
    query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY duration DESC;
```

### 11.3 Блокировки

**Просмотр блокировок:**

```sql
SELECT 
    blocked_locks.pid AS blocked_pid,
    blocking_locks.pid AS blocking_pid,
    blocked_activity.query AS blocked_query,
    blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity 
    ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks 
    ON blocking_locks.locktype = blocked_locks.locktype
    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
    AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity 
    ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```

---

## 12. Best Practices

### 12.1 Держите транзакции короткими

**❌ Плохо:**

```sql
BEGIN;
-- Долгие вычисления
-- Сетевые запросы
-- Пользовательский ввод
COMMIT;
```

**✅ Хорошо:**

```sql
-- Короткие транзакции
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Долгие операции вне транзакции
-- Затем ещё одна короткая транзакция
BEGIN;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 12.2 Используйте правильный уровень изоляции

**Выбирайте минимально необходимый уровень:**

- Read Committed — для большинства случаев
- Repeatable Read — когда нужна стабильность чтения
- Serializable — только когда критично

### 12.3 Обрабатывайте ошибки

**Всегда обрабатывайте ошибки транзакций:**

```sql
BEGIN;
BEGIN
    -- Операции
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
```

---

## 💡 Key Takeaways

- **ACID** — Atomicity, Consistency, Isolation, Durability — основные свойства транзакций

- **Уровни изоляции** — от Read Uncommitted до Serializable, компромисс между изоляцией и производительностью

- **Блокировки** — Shared для чтения, Exclusive для записи

- **Deadlock** — взаимная блокировка, решается одинаковым порядком блокировок

- **FOR UPDATE** — явная блокировка строк для обновления

---

## 🚀 Next Steps

**Related Modules:**

- [14_Performance](../14_Performance/) — Производительность и масштабирование
- [04_Insert_Update_Delete](../04_Insert_Update_Delete/) — Модификация данных

**Practice Ideas:**

1. Экспериментируйте с разными уровнями изоляции
2. Создайте сценарии с блокировками и deadlock
3. Попрактикуйтесь с FOR UPDATE
4. Реализуйте оптимистичную блокировку

**Going Deeper:**

- Изучите MVCC (Multi-Version Concurrency Control)
- Изучите настройки блокировок в вашей СУБД
- Изучите мониторинг блокировок и deadlock

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) — транзакции
- [Isolation Levels](https://www.postgresql.org/docs/current/transaction-iso.html) — уровни изоляции

---


