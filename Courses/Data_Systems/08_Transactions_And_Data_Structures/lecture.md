# Транзакции и структуры данных
## WAL, Undo/Redo Logs, MVCC и блокировки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать, что такое транзакция (ACID)
- Знать устройство B-tree и LSM-tree
- Понимать разницу между диском и памятью

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять, какие структуры данных обеспечивают ACID
- Понимать роль WAL (Write-Ahead Log)
- Разбираться в механике Undo/Redo логов
- Понимать, как работает MVCC (Multiversion Concurrency Control)

---

## 1. ACID и структуры данных

При работе баз данных мы ожидаем выполнения свойств **ACID**:

*   **Atomicity** (Атомарность): Всё или ничего.

*   **Consistency** (Согласованность): Данные корректны.

*   **Isolation** (Изоляция): Транзакции не мешают друг другу.

*   **Durability** (Долговечность): Сохранение после сбоя.

Какие структуры данных за это отвечают?

| Свойство | Основная структура / Механизм |
| :--- | :--- |
| **A**tomicity | Undo Log |
| **C**onsistency | Constraints (проверяются при вставке) |
| **I**solation | Lock Manager (Hash Table), MVCC (Versioning) |
| **D**urability | WAL (Redo Log) |

---

## 2. Durability: Write-Ahead Log (WAL)

### 2.1 Проблема

Запись на диск (fsync) медленная. Если писать в B-tree на диск при каждом `INSERT`, будет очень медленно (Random I/O). Мы хотим писать в буфер (RAM), но если питание пропадет — данные исчезнут.

### 2.2 Решение: WAL

**Правило WAL**: Никакие изменения не должны попасть в основной файл данных на диске до того, как они будут записаны в лог (журнал).

**WAL (Redo Log)** — это append-only файл.
1. При изменении данных, сначала формируем запись лога: `LSN: 101, Op: UPDATE, Page: 5, Old: A, New: B`.
2. Последовательно пишем эту запись в конец файл WAL на диске. Это быстро (Sequential I/O).
3. Меняем страницу данных в **памяти** (Buffer Pool).
4. Подтверждаем транзакцию пользователю (Commit).
5. Страница данных на диске может быть обновлена позже (Lazy write).

Если происходит сбой (Crash): при перезапуске БД читает WAL и "проигрывает" (Redo) все операции, которые не успели попасть в файлы данных.

```python

class SimulatedWAL:
    def __init__(self, filename="wal.log"):
        self.filename = filename
        
    def log_transaction(self, tx_id, operation, data):
        """Append-only запись в лог."""
        entry = f"TX:{tx_id}|OP:{operation}|DATA:{data}\n"
        with open(self.filename, 'a') as f:
            f.write(entry)
            # В реальной БД здесь вызывается fsync, чтобы гарантировать запись на физический диск
            # os.fsync(f.fileno()) 
        print(f"Logged to WAL: {entry.strip()}")

# Эмуляция

wal = SimulatedWAL()
wal.log_transaction(1, "UPDATE_BALANCE", "User:1, Amount:100")
# Теперь можно менять данные в памяти...

```

---

## 3. Atomicity: Undo Log

### 3.1 Проблема

Транзакция может выполнить половину операций и упасть (или пользователь нажмет Rollback).
Например:

1. Снять $100 со счета А (Сделано)
2. Добавить $100 на счет Б (Ошибка!)
Нужно отменить шаг 1.

### 3.2 Решение: Undo Log

**Undo Log** хранит информацию о том, как **отменить** действие.
*   При `INSERT` -> Undo Log хранит удаление этой записи.
*   При `DELETE` -> Undo Log хранит вставку удаленной записи.
*   При `UPDATE` -> Undo Log хранит старое значение.

Если транзакцию нужно откатить, БД читает Undo Log в обратном порядке и применяет "анти-действия".

---

## 4. Isolation: Блокировки (Locks)

### 4.1 Lock Manager

Чтобы две транзакции не меняли одну запись одновременно, используются блокировки.

**Lock Manager** — это обычно хеш-таблица в памяти.
Key: ID ресурса (Table ID, Page ID, Row ID).
Value: Очередь транзакций, ожидающих этот ресурс.

Типы блокировок:

*   **Shared (S)**: Для чтения. Несколько транзакций могут держать S-lock.

*   **Exclusive (X)**: Для записи. Только одна транзакция может держать X-lock.

```python

class SimpleLockManager:
    def __init__(self):
        # Resource ID -> Owner Transaction ID
        self.locks = {} 
        
    def acquire_exclusive(self, resource_id, tx_id):
        if resource_id in self.locks:
            if self.locks[resource_id] == tx_id:
                return True # Уже владеем
            print(f"Tx {tx_id} BLOCKED waiting for {resource_id} (held by Tx {self.locks[resource_id]})")
            return False
        
        self.locks[resource_id] = tx_id
        print(f"Tx {tx_id} acquired lock on {resource_id}")
        return True
        
    def release(self, resource_id, tx_id):
        if self.locks.get(resource_id) == tx_id:
            del self.locks[resource_id]
            print(f"Tx {tx_id} released lock on {resource_id}")

# Демонстрация

lm = SimpleLockManager()
lm.acquire_exclusive("Row:1", "Tx1") # OK
lm.acquire_exclusive("Row:1", "Tx2") # Blocked
lm.release("Row:1", "Tx1") # Release
lm.acquire_exclusive("Row:1", "Tx2") # OK now
```

---

## 5. Isolation: MVCC (Multiversion Concurrency Control)

### 5.1 Проблема блокировок

Блокировки "Readers block Writers" и "Writers block Readers". Это медленно.
Мы хотим, чтобы чтение не блокировало запись.

### 5.2 Решение: MVCC

**MVCC** хранит **несколько версий** одной и той же строки.
*   Writers создают новую версию строки.
*   Readers читают ту версию, которая была актуальна на момент начала их транзакции.

Структура данных дополняется полями:

*   `created_by_tx`: ID транзакции, создавшей версию.
*   `deleted_by_tx`: ID транзакции, удалившей версию.

**Snapshot Isolation:**
Каждая транзакция видит "снэпшот" базы на момент своего старта.

**Пример (PostgreSQL implementation concept):**

| Row ID | Data | xmin (Created By) | xmax (Deleted By) |
| :--- | :--- | :--- | :--- |
| 1 | "Value A" | 100 | 102 |
| 1 | "Value B" | 102 | NULL |

*   Транзакция 101 читает базу.
*   Она видит первую строку (т.к. 100 < 101 и она удалена в 102, что > 101).
*   Она НЕ видит вторую строку (т.к. 102 > 101, это "будущее").
*   Результат: "Value A".

Транзакция 103:

*   Видит, что первая строка удалена в 102 (102 < 103).
*   Видит вторую строку (создана в 102).
*   Результат: "Value B".

### 5.3 Vacuum

Мертвые версии (которые никто уже не увидит) нужно удалять, иначе база раздуется.
В PostgreSQL этим занимается процесс **Vacuum**, в MySQL (InnoDB) — Purge thread.

---

## 6. LSN (Log Sequence Number)

Все структуры связываются через **LSN** — монотонно возрастающий номер записи в логе.
В каждой странице данных (Page Header) хранится `pageLSN`.
Это LSN последней операции, изменившей эту страницу.

Это критично для восстановления (Crash Recovery/ARIES):

*   Если `pageLSN` >= `redoLogLSN`, значит изменение уже на диске, Redo не нужен.
*   Если `pageLSN` < `redoLogLSN`, значит страница на диске "старая", нужно накатить изменения из лога.

---

## 7. Практические выводы

1.  **Почему БД тормозит при записи?**
    Возможно, диск не справляется с записью WAL (fsync latency).

2.  **Почему БД растет, даже если не вставлять данные?**
    MVCC создает версии при UPDATE. Если долгая транзакция держит старый снимок, Vacuum не может удалить мусор (bloat).

3.  **Зачем нужен Commit?**
    Commit — это момент, когда запись лога (всех накопленных изменений) физически сбрасывается на диск (flush). Это самое "узкое" место Durability.

---

## 💡 Key Takeaways

- **ACID** реализуется через комбинацию структур:
    - **A**: Undo Log (отмена действий).
    - **C**: Constraints.
    - **I**: Locks & MVCC (версионность).
    - **D**: WAL (Redo Log) (выживание данных).
- **WAL** превращает Random Write в Sequential Write.

- **MVCC** позволяет читать без блокировок ("Readers don't block Writers").

- **Lock Manager** управляет доступом к ресурсам.

---

## 🚀 Next Steps

**Module 3 Preview:**

- Теперь мы знаем, как работают локальные БД.
- В следующем модуле мы пойдем в **распределенные системы**.
- [CAP теорема](../09_CAP_Theorem/) — начало пути к распределенным данным.

**Practice Ideas:**

1. Изучите `pg_stat_activity` и блокировки в PostgreSQL.
2. Попробуйте сделать `UPDATE` и `ROLLBACK` и представьте, что происходит в Undo Log.
3. Посмотрите файлы WAL (pg_wal) в PostgreSQL, оцените их размер и количество.

---

