# Transactions & Data Structures
## ACID, Isolation Levels, MVCC и Concurrency Control

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **Storage**: Понимать, как базы данных пишут страницы на диск (B-Trees, WAL) — Модуль 07.

- **Python**: Уметь читать код с обработкой исключений (`try/except/finally`) и работать со словарями.

- **SQL Basics**: Знать, что такое `BEGIN`, `COMMIT`, `ROLLBACK`.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **ACID**: Объяснять каждое свойство ACID на примере конкретных сбоев (выдернули шнур, гонка потоков).

- **Isolation**: Различать Dirty Read, Non-Repeatable Read и Phantom Read. Понимать, какой уровень изоляции их предотвращает.

- **Concurrency**: Сравнивать пессимистичную (2PL) и оптимистичную (MVCC) блокировки. Понимать, почему `SELECT COUNT(*)` в Postgres такой медленный.

- **Deadlocks**: Диагностировать взаимные блокировки и реализовывать алгоритм обнаружения циклов в графе ожиданий.

- **Implementation**: Написать простейший Lock Manager на Python.

- **Operations**: Находить и убивать блокирующие запросы в production-базах (PostgreSQL, MySQL).

---

## 1. Введение: Почему транзакции — это сложно?

Мир полон хаоса.

1.  Жесткий диск может отказать в момент записи.
2.  Свет могут отключить посередине операции перевода денег.
3.  Сеть может порваться.
4.  Другой пользователь может попытаться купить тот же билет на самолет одновременно с вами.

Без транзакций разработчику пришлось бы обрабатывать все эти сценарии вручную в коде приложения ("Если упало тут, удали ту запись, а если там — верни деньги"). Это ад.

**Транзакция** — это абстракция, которая превращает хаос в порядок. Она дает гарантию: **"Всё или ничего"**.

---

## 2. ACID: Четыре всадника надежности

В 1983 году Тео Хардер и Андреас Рейтер придумали акроним ACID.

### 2.1 A - Atomicity (Атомарность)

*   **Определение**: Транзакция неделима. Либо выполняются все операции, либо ни одной. Промежуточных состояний не существует для внешнего мира.

*   **Пример**: Перевод денег.
    1.  `UPDATE accounts SET balance = balance - 100 WHERE id = 'Alice'`
    2.  *СБОЙ ПИТАНИЯ!*
    3.  `UPDATE accounts SET balance = balance + 100 WHERE id = 'Bob'`
    *   **Без атомарности**: Алиса потеряла деньги, Боб не получил. Деньги исчезли.
    *   **С атомарностью**: При рестарте база видит, что транзакция не завершена, и делает **Rollback** (отменяет списание у Алисы).
*   **Реализация**: Write Ahead Log (WAL) и Undo Log. Перед изменением данных мы пишем "как было".

### 2.2 C - Consistency (Согласованность)

*   **Определение**: Транзакция переводит базу из одного валидного состояния в другое. Инварианты (Constraints) не нарушаются.

*   **Пример**:
    *   `CHECK (balance >= 0)`.
    *   Если транзакция пытается сделать баланс `-50`, база прерывает транзакцию ошибкой.
*   **Нюанс**: Это **единственное** свойство ACID, которое зависит от приложения, а не только от базы данных. Если вы переведете деньги не тому человеку, база не узнает, что это ошибка, если все типы данных совпали.

### 2.3 I - Isolation (Изоляция)

*   **Определение**: Результат выполнения транзакций параллельно должен быть таким же, как если бы они выполнялись последовательно (одна за другой).

*   **Проблема**: Идеальная изоляция (Serializability) очень медленная. Поэтому мы идем на компромиссы (уровни изоляции).

### 2.4 D - Durability (Долговечность)

*   **Определение**: Если база сказала `COMMIT OK`, данные сохранены на диске навсегда. Даже если через миллисекунду сгорит сервер.

*   **Реализация**: `fsync()`. Мы принудительно сбрасываем кэш ОС на диск перед ответом клиенту.

---

## 3. Проблемы конкурентного доступа (Race Conditions)

Когда несколько транзакций работают с одними данными, возникают аномалии.

### 3.1 Dirty Read (Грязное чтение)

*   **Сценарий**:
    1.  Транзакция А пишет `x = 10` (но еще не делает Commit).
    2.  Транзакция Б читает `x` и видит `10`.
    3.  Транзакция А делает **Rollback**.
    4.  **Итог**: Транзакция Б работает с данными, которых никогда не существовало ("грязными").

### 3.2 Non-Repeatable Read (Неповторяющееся чтение)

*   **Сценарий**:
    1.  Транзакция А читает `x` (видит 10).
    2.  Транзакция Б пишет `x = 20` и делает Commit.
    3.  Транзакция А снова читает `x` (видит 20).
    4.  **Итог**: В рамках одной транзакции данные изменились. Это ломает логику аналитики/отчетов.

### 3.3 Phantom Read (Фантомное чтение)

*   **Сценарий**:
    1.  Транзакция А делает `SELECT COUNT(*) WHERE age > 18` (видит 5 человек).
    2.  Транзакция Б делает `INSERT INTO users (age) VALUES (20)` и Commit.
    3.  Транзакция А снова делает тот же SELECT (видит 6 человек).
    4.  **Итог**: Данные не изменились (старые строки те же), но появились новые "фантомы", влияющие на агрегаты.

---

## 4. Isolation Levels (Уровни изоляции)

Стандарт SQL-92 определяет 4 уровня.

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | 🔴 Yes | 🔴 Yes | 🔴 Yes |
| **Read Committed** (Default in PG/Ora) | 🟢 No | 🔴 Yes | 🔴 Yes |
| **Repeatable Read** (Default in MySQL) | 🟢 No | 🟢 No | 🔴 Yes |
| **Serializable** | 🟢 No | 🟢 No | 🟢 No |

### 4.1 Read Uncommitted

Самый быстрый и опасный.

*   **Как работает**: Читает данные без блокировок, даже незакоммиченные.

*   **Где нужен**: Приближенная аналитика (COUNT(*) на огромной таблице), где скорость важнее точности. В Postgres этот уровень **не реализован** (ведет себя как Read Committed).

### 4.2 Read Committed

Стандарт де-факто.

*   **Как работает**: Читает только закоммиченные данные. Но если читать два раза, данные могут быть разными.

*   **Механизм**: Каждое выражение `SELECT` видит "снимок" данных на момент **начала этого выражения**.

### 4.3 Repeatable Read

*   **Как работает**: Гарантирует, что если вы прочитали строку, она не изменится до конца транзакции.

*   **Механизм**: Транзакция видит "снимок" данных на момент **начала первой команды** в транзакции.

*   **Важно**: В MySQL (InnoDB) он также предотвращает фантомы с помощью Next-Key Locking. В Postgres — нет (для защиты от фантомов нужен Serializable).

### 4.4 Serializable

Полная иллюзия последовательного выполнения.

*   **Механизм**:
    *   **2PL (Strict Two-Phase Locking)**: Блокирует все, что читает. Медленно, мертвые блокировки.
    *   **SSI (Serializable Snapshot Isolation)**: Оптимистичный подход. Следит за графом зависимостей и **убивает** транзакцию при конфликте (`Serialization Error`). Требует `retry` на клиенте.

---

## 5. Concurrency Control: 2PL vs MVCC

Как обеспечить изоляцию технически?

### 5.1 Two-Phase Locking (2PL)

Классический пессимистичный подход (используется в SQL Server, DB2, частично MySQL).

**Правила**:
1.  **Shared Lock (S)**: Нужен для чтения. Несколько транзакций могут держать S-lock на одной строке.
2.  **Exclusive Lock (X)**: Нужен для записи. Только одна транзакция может держать X-lock. Несовместим с S и X.

**Фазы**:
1.  **Growing Phase**: Транзакция набирает замки по мере выполнения (`SELECT`, `UPDATE`).
2.  **Shrinking Phase**: Транзакция отпускает замки (обычно все сразу в момент `COMMIT`).

**Минусы**:
*   **Readers block Writers**: Если я читаю таблицу, никто не может в нее писать.

*   **Writers block Readers**: Если я пишу, никто не может читать.
*   Низкая производительность.

### 5.2 Multi-Version Concurrency Control (MVCC)

Оптимистичный подход (PostgreSQL, Oracle, MySQL/InnoDB).
Главное правило: **"Readers never block Writers, and Writers never block Readers"**.

**Идея**:
Вместо перезаписи строки, мы создаем **новую версию**.
Старая версия остается для тех транзакций, которые начали работу раньше.

**PostgreSQL Implementation (Heap Tuples)**:
Каждая строка имеет скрытые поля:

*   `xmin`: ID транзакции, создавшей версию.
*   `xmax`: ID транзакции, удалившей версию (или 0, если жива).

**Пример**:
Транзакция 100 делает `INSERT`:
`{id:1, val:'A', xmin:100, xmax:0}`

Транзакция 101 делает `UPDATE` (deletes old, inserts new):

1.  Mark old as dead: `{id:1, val:'A', xmin:100, xmax:101}`
2.  Insert new: `{id:1, val:'B', xmin:101, xmax:0}`

Транзакция 102 (Started before 101):

*   Видит версию с `val:'A'`, потому что `xmin=100 < 102` и `xmax=101` (еще не закоммичена или > 102).
*   Версия `val:'B'` невидима (`xmin=101` — из будущего).

**Vacuum**:
Старые версии ("мертвые кортежи"), которые никому не нужны, занимают место.
Процесс **Vacuum** (в Postgres) или **Purge** (в MySQL) ходит и чистит мусор.

---

## 6. Deadlocks (Взаимные блокировки)

**Ситуация**:
*   Транзакция A держит замок на строке 1 и хочет строку 2.
*   Транзакция B держит замок на строке 2 и хочет строку 1.
*   Они будут ждать вечно.

**Решения**:
1.  **Timeout**: Если ждем больше 50с — отмена. (Просто, но неэффективно).
2.  **Deadlock Detection**: База данных строит "Wait-for Graph". Если в графе есть **цикл** (A -> B -> A), база убивает одну из транзакций (обычно ту, которая сделала меньше работы), чтобы спасти другую.

---

## 7. Практическая реализация: Lock Manager (Python)

Давайте напишем примитивный менеджер блокировок, чтобы понять механику.

```python
import threading
import time

class LockManager:
    def __init__(self):
        # Resource ID -> Owner Transaction ID
        self.locks = {} 
        self.mutex = threading.Lock()
        
        # Deadlock detection graph: TrasactionID -> waiting_for_TransactionID
        self.wait_for = {}

    def acquire(self, tx_id, resource):
        with self.mutex:
            if resource not in self.locks:
                # Свободно - забираем
                self.locks[resource] = tx_id
                print(f"Tx {tx_id} acquired {resource}")
                return True
            
            owner = self.locks[resource]
            if owner == tx_id:
                return True # Reentrancy
            
            print(f"Tx {tx_id} waiting for {resource} (held by {owner})")
            
            # Deadlock Check
            if self._detect_deadlock(tx_id, owner):
                print(f"💀 DEADLOCK DETECTED! Tx {tx_id} killed.")
                raise Exception("DeadlockException")
            
            # Record dependency
            self.wait_for[tx_id] = owner
            
        # Wait (Blocking) simulation
        while True:
            with self.mutex:
                if resource not in self.locks:
                    self.locks[resource] = tx_id
                    del self.wait_for[tx_id]
                    print(f"Tx {tx_id} finally acquired {resource}")
                    return True
            time.sleep(0.1)

    def release(self, tx_id, resource):
        with self.mutex:
            if self.locks.get(resource) == tx_id:
                del self.locks[resource]
                print(f"Tx {tx_id} released {resource}")

    def _detect_deadlock(self, start_tx, target_tx):
        # DFS traversal check for cycle
        current = target_tx
        visited = set()
        while current in self.wait_for:
            if current in visited: return True # Cycle
            visited.add(current)
            if current == start_tx: return True
            current = self.wait_for[current]
        return False

# Simulation Scenario

lm = LockManager()

def tx_a():
    try:
        lm.acquire('A', 'Res1')
        time.sleep(0.5)
        lm.acquire('A', 'Res2') # Will block waiting for B
    except:
        print("A rolled back")
        lm.release('A', 'Res1')

def tx_b():
    try:
        lm.acquire('B', 'Res2')
        time.sleep(0.5)
        lm.acquire('B', 'Res1') # Will block waiting for A -> Deadlock
    except:
        print("B rolled back")
        lm.release('B', 'Res2')

t1 = threading.Thread(target=tx_a)
t2 = threading.Thread(target=tx_b)
t1.start(); t2.start()
t1.join(); t2.join()
```

---

## 8. Glossary

*   **ACID**: Atomicity, Consistency, Isolation, Durability. Набор свойств надежных транзакций.

*   **WAL (Write Ahead Log)**: Журнал упреждающей записи. Данные сначала пишутся в лог (последовательно), потом в файлы данных. Гарантирует Durability и Atomicity.

*   **Dirty Read**: Чтение незакоммиченных данных.

*   **Phantom Read**: Появление новых строк, удовлетворяющих условию поиска, внутри транзакции.

*   **Snapshot Isolation**: Уровень изоляции, где каждая транзакция видит консистентный срез данных на момент старта.

*   **2PL (Two-Phase Locking)**: Алгоритм управления конкурентностью через блокировки (Growing/Shrinking фазы).

*   **MVCC (Multi-Version Concurrency Control)**: Алгоритм управления конкурентностью через версионирование строк. Не блокирует чтение записью.

*   **S-Lock (Shared)**: Блокировка для чтения. Совместима с другими S-Lock.

*   **X-Lock (Exclusive)**: Блокировка для записи. Несовместима ни с чем.

*   **Deadlock**: Ситуация циклического ожидания ресурсов.

*   **Livelock**: Ситуация, когда транзакции не блокируются, но постоянно меняют состояние и не могут завершиться (бесконечные retry).

*   **Optimistic Concurrency Control (OCC)**: Подход "сначала делай, потом проверяй". Если при коммите обнаружен конфликт — откат. Хорош для систем с малым числом конфликтов.

*   **Pessimistic Concurrency Control**: Подход "сначала блокируй, потом делай". Хорош для систем с высокой конкуренцией.

*   **Compensating Transaction**: Логическая операция отмены действия (например, "Вернуть деньги"), если технический Rollback невозможен (в распределенных сагах).

*   **Serialization Anomaly**: Ошибка, возникающая при Serializable изоляции, когда порядок транзакций нарушен.

---

## 📚 Appendix A: Troubleshooting Guide

Блокировки — частая причина "зависания" сайта.

### A.1 Postgres: Finding Blocking Queries

Сайт висит. Что делать?
Смотрим в таблицу `pg_stat_activity`.

```sql
-- Кто кого блокирует?
SELECT
    blocking.pid AS blocking_pid,
    blocking.query AS blocking_query,
    blocked.pid AS blocked_pid,
    blocked.query AS blocked_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked ON blocked_locks.pid = blocked.pid
JOIN pg_catalog.pg_locks blocking_locks 
    ON blocking_locks.locktype = blocked_locks.locktype
    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
    AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
    AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
    AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
    AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
    AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
    AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
    AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
    AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted;
```

**Решение**:
1.  Найти `blocking_pid`.
2.  `SELECT pg_terminate_backend(blocking_pid);` (Осторожно! Вы убьете транзакцию).

### A.2 MySQL: InnoDB Status

В MySQL команда:
`SHOW ENGINE INNODB STATUS\G`

Ищите секцию `LATEST DETECTED DEADLOCK`. Она покажет последний дедлок и два SQL запроса, которые в нем участвовали.

**Совет**:
Всегда сортируйте строки при апдейте.
Если одна транзакция делает `UPDATE WHERE id IN (1, 5)`, а другая `UPDATE WHERE id IN (5, 1)`, это дедлок.
Если обе делают `ORDER BY id`, дедлока не будет (вторая просто подождет).

---

## 📚 Appendix B: Historical Context

### 1970s: System R

В IBM Research работали гении (Джим Грей, Франко Путцолу). Они создавали System R — первую реляционную СУБД.
Они поняли, что просто исполнять запросы недостаточно. Нужна защита.
Они:

*   Придумали уровни изоляции (Read Committed, Serializable).
*   Придумали локи (S/X modes).
*   Придумали WAL.
Джим Грей получил премию Тьюринга за транзакции. (К сожалению, он пропал без вести в море в 2007 году).

### Postgres vs MySQL (History of MVCC)

*   **Oracle** первым внедрил MVCC с использованием Undo Segments (откат изменений для читателей).

*   **Postgres** выбрал другой путь: хранить версии прямо в таблице (Heap). Это дало сверхбыстрый Rollback (просто пометить xmax), но породило проблему Vacuum (мусор надо чистить).

*   **InnoDB (MySQL)** пошел путем Oracle: данные перезаписываются (update in-place), а старые версии копируются в Undo Log.

---

## 📚 Appendix C: FAQ (Часто задаваемые вопросы)

**Q1: Зачем нужен `SELECT ... FOR UPDATE`?**
**A**: Это способ превратить MVCC в 2PL (Pessimistic locking) для конкретных строк.
Пример: Вы хотите проверить баланс `val = SELECT bal FROM acc WHERE id=1` и обновить его.
В обычном транзакционном режиме между SELECT и UPDATE кто-то может изменить баланс.
`SELECT ... FOR UPDATE` берет X-Lock на чтение. Никто другой не сможет прочитать эту строку в `FOR UPDATE` или изменить её, пока вы не закончите.

**Q2: Является ли Redis транзакционным?**
**A**: Частично. Команды внутри `MULTI/EXEC` атомарны и изолированы (никто не вклинится). Но в Redis **нет Rollback** при ошибке внутри транзакции. Если одна команда упала (синтаксис), остальные выполнятся. Это нарушает A (Atomicity) в классическом понимании.

**Q3: Почему NoSQL базы (Mongo, Cassandra) часто не имеют ACID?**
**A**: CAP теорема. Чтобы обеспечить Availability и Partition Tolerance на масштабе 1000 узлов, сложно делать распределенные локи (это убьет latency).
Они предлагают **BASE**: Basically Available, Soft state, Eventual consistency.
(Хотя Mongo 4.0+ добавила поддержку ACID транзакций).

**Q4: Что такое "Lost Update"?**
**A**: Это аномалия, когда `UPDATE` одной транзакции перезаписывает `UPDATE` другой, не зная о нем.
Случается в Read Committed.
Лечится уровнем Repeatable Read или использованием атомарных инкрементов `UPDATE t SET val = val + 1` (вместо read-modify-write на клиенте).

**Q5: Как работают транзакции в MongoDB?**
**A**: Похоже на реляционные. Используется WiredTiger engine (MVCC). Но транзакции ограничены по времени (60с) и размеру (16МБ логов). И они медленнее обычных записей.

**Q6: Что такое Savepoint?**
**A**: "Чекпоинт" внутри транзакции. Можно откатиться не к началу (`ROLLBACK`), а к точке (`ROLLBACK TO SAVEPOINT sp1`). Полезно для обработки ошибок без сброса всей работы.

**Q7: Почему `SERIALIZABLE` часто выдает ошибки?**
**A**: Потому что он использует оптимистичный (или пессимистичный строгий) контроль. В Postgres при Serializable, если транзакции *могли* повлиять друг на друга, база кинет `40001: serialization_failure`. Ваше приложение **обязано** иметь логику retry (повторить транзакцию).

**Q8: Можно ли вложенные транзакции (Nested Transactions)?**
**A**: В стандарте SQL — нет. Некоторые СУБД эмулируют их через Savepoints.

**Q9: Влияют ли индексы на блокировки?**
**A**: Да! Если вы делаете `UPDATE ... WHERE col = 5`, и на `col` нет индекса, бза может заблокировать **ВСЮ ТАБЛИЦУ** (или все строки), потому что ей нужно просканировать их, чтобы найти `col=5`. Всегда индексируйте поля, по которым идет конкурентный доступ!

**Q10: Что такое Predicate Locking?**
**A**: Идеальный механизм защиты от фантомов: блокировка "условия" (WHERE age > 18), а не конкретных строк. Сложно реализуем. Обычно заменяется на Next-Key Locking (блокировка диапазонов индекса) или проверку изменений при коммите (SSI).

---

## 💡 Key Takeaways

1.  **Isolation is expensive**: Чем выше уровень изоляции, тем ниже пропускная способность. Default (Read Committed) — разумный компромисс.
2.  **Locks are dangerous**: Дедлоки случаются. Пишите код так, чтобы порядок захвата ресурсов был всегда одинаковым (сортируйте ID).
3.  **MVCC rules**: Postgres и InnoDB используют версионирование. Читатели не блокируют писателей. Это основа производительности современных БД.

---

## 🚀 Next Steps

**Практика:**

1.  Откройте два терминала `psql` или `mysql`.
2.  Начните транзакцию `BEGIN` в обоих.
3.  Сэмулируйте Deadlock: A лочит 1, B лочит 2, A хочет 2, B хочет 1.
4.  Посмотрите логи базы данных и статус процесса.

В следующем модуле мы выйдем за пределы одной машины и узнаем, как ACID разваливается в **Распределенных Системах**. [Distributed Challenges](../09_Distributed_Challenges/).


