# Write-Heavy vs Read-Heavy структуры
## LSM-tree, SSTables, Memtables и оптимизация под нагрузку

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать разницу между памятью (RAM) и диском (Disk/SSD)
- Знать, как работают B-tree индексы и их ограничения
- Понимать концепцию пропускной способности (throughput) и задержки (latency)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать write-heavy и read-heavy нагрузки
- Объяснять принцип работы LSM-tree (Log-Structured Merge-tree)
- Понимать роль Memtable, WAL и SSTable
- Сравнивать B-tree и LSM-tree для различных сценариев

---

## 1. Проблема записи в B-tree

### 1.1 Random I/O — убийца производительности

Классические B-tree индексы (используемые в MySQL, PostgreSQL) отличны для чтения, но могут быть узким местом для интенсивной записи.

**Почему запись в B-tree дорогая:**

1. **Update-in-place**: Для изменения одной строки нужно прочитать страницу (4-16KB), изменить её и записать обратно.
2. **Random Writes**: Вставка в случайное место B-дерева вызывает случайные операции записи на диск. Диски (особенно HDD, но и SSD) гораздо медленнее на случайной записи, чем на последовательной.

```python

import time
import os

# Симуляция случайной vs последовательной записи
def benchmark_io(filename, size_mb=100, block_size=4096):
    file_size = size_mb * 1024 * 1024
    num_blocks = file_size // block_size
    
    # Последовательная запись (Sequential Write)
    start = time.perf_counter()
    with open(filename, 'wb') as f:
        for _ in range(num_blocks):
            f.write(os.urandom(block_size))
    seq_time = time.perf_counter() - start
    
    # Случайная запись (Random Write)
    # Симулируем прыжки по файлу
    start = time.perf_counter()
    with open(filename, 'rb+') as f:
        for _ in range(num_blocks // 10): # Меньше операций, чтобы не ждать вечность
            f.seek(os.urandom(1)[0] * file_size // 256)
            f.write(os.urandom(block_size))
    rand_time = time.perf_counter() - start
    
    print(f"Sequential: {size_mb}MB in {seq_time:.2f}s ({size_mb/seq_time:.2f} MB/s)")
    # Умножаем на 10, так как делали 1/10 операций
    print(f"Random: ~{size_mb}MB in {rand_time*10:.2f}s ({size_mb/(rand_time*10):.2f} MB/s)")
    
# Примечание: В реальной ОС кэширование смажет результаты, 
# но хардварная разница огромна (10x-100x).

```

### 1.2 Решение: Append-Only

Самый быстрый способ записи на диск — это **добавление в конец файла (Append-Only)**. Это всегда последовательная запись.

Но если мы просто пишем всё в лог, как потом читать? Чтение станет O(n).
Нам нужна структура, которая пишет последовательно (как лог), но читает быстро (как дерево). Это **LSM-tree**.

---

## 2. Архитектура LSM-tree

**LSM-tree (Log-Structured Merge-tree)** — это не одна структура данных, а архитектурный подход, использующий иерархию структур.

Используется в: RocksDB, Cassandra, ScyllaDB, LevelDB, InfluxDB, ClickHouse.

### 2.1 Компоненты LSM

1.  **WAL (Write Ahead Log)**: Append-only лог на диске для восстановления после сбоя.
2.  **Memtable**: Структура в памяти (обычно сбалансированное дерево или Skip List).
3.  **SSTable (Sorted String Table)**: Неизменяемый (immutable) файл на диске, где данные отсортированы.

```

Запись (Write Path):
[Client] -> [WAL (Disk)] (для надежности)
         -> [Memtable (RAM)] (для скорости и сортировки)

Чтение (Read Path):
[Client] -> Check [Memtable]
         -> Check [SSTable L0]
         -> ...
         -> Check [SSTable L_max]
```

### 2.2 Процесс записи (Write)

1.  Данные пишутся в **WAL** (последовательно, быстро).
2.  Данные вставляются в **Memtable** (в памяти, быстро).
3.  Когда Memtable заполняется, она **сбрасывается (flushed)** на диск как новый **SSTable**.
    *   Так как Memtable отсортирована, запись SSTable — это чисто последовательная запись!

### 2.3 Memtable реализация

Обычно используют **Skip List** или **Red-Black Tree**. Skip List популярен из-за простоты реализации конкурентного доступа.

```python

import random

class BuildInMemtable:
    """
    Простейшая эмуляция Memtable с использованием словаря (который в Python 3.7+ упорядочен).
    В реальности используется SkipList или Tree.
    """
    def __init__(self, limit=5):
        self.data = {}
        self.limit = limit
        self.wal = [] # Эмуляция лога
        
    def put(self, key, value):
        # 1. Write to WAL
        self.wal.append((key, value))
        
        # 2. Write to Memtable
        self.data[key] = value
        
        # 3. Check flush condition
        if len(self.data) >= self.limit:
            self.flush()
            
    def flush(self):
        # Сортируем данные перед записью (SSTable должен быть отсортирован)
        sorted_items = sorted(self.data.items())
        filename = f"sstable_{int(time.time())}.db"
        
        print(f"Flushing {len(sorted_items)} items to {filename}...")
        with open(filename, 'w') as f:
            for k, v in sorted_items:
                f.write(f"{k}:{v}\n")
                
        # Очистка Memtable и WAL
        self.data.clear()
        self.wal.clear()

# Демонстрация
memtable = BuildInMemtable(limit=3)
memtable.put("key1", "val1")
memtable.put("key3", "val3")
memtable.put("key2", "val2") # Тут произойдет flush, key2 будет посередине
```

**Output:**
```

Flushing 3 items to sstable_1701234567.db...
(На диске будет: key1:val1, key2:val2, key3:val3)
```

---

## 3. SSTables и Compaction

### 3.1 Структура SSTable

**SSTable (Sorted String Table)** — это файл на диске, содержащий отсортированные пары ключ-значение.
Свойство: **Immutable** (никогда не меняется после записи).

Почему это круто:

*   Нет блокировок на чтение (lock-free reads).
*   Простое кэширование.
*   Отличная компрессия (похожие ключи рядом).

### 3.2 Проблема чтения

Со временем у нас накапливается много SSTables файлов.
Чтобы найти ключ, нужно проверить Memtable, затем SSTable-1, SSTable-2, ..., SSTable-N.
В худшем случае O(N) файлов. Это медленно.

### 3.3 Решение: Compaction

**Compaction (уплотнение)** — фоновый процесс, который объединяет несколько маленьких SSTables в один большой.
Похоже на алгоритм **Merge Sort**.

```python

def compaction(files):
    """
    Эмуляция слияния SSTables.
    Вход: имена файлов с отсортированными данными.
    Выход: один файл с объединенными данными (последняя версия ключа побеждает).
    """
    # Читаем все файлы (упрощенно - целиком в память, реально - стримами/итераторами)
    data_map = {}
    
    # Читаем от старых к новым. Новые перезаписывают старых.
    for filename in files:
        with open(filename, 'r') as f:
            for line in f:
                k, v = line.strip().split(':')
                data_map[k] = v
                
    # Записываем результат
    new_filename = "sstable_merged.db"
    sorted_items = sorted(data_map.items())
    
    with open(new_filename, 'w') as f:
        for k, v in sorted_items:
            f.write(f"{k}:{v}\n")
            
    return new_filename

# файлы от предыдущего шага
# compaction(['sstable_1.db', 'sstable_2.db'])

```

Типы compaction:

1.  **Size-tiered (Cassandra)**: Сливаем файлы одинакового размера. Быстрая запись, медленнее чтение.
2.  **Leveled (RocksDB, LevelDB)**: Уровни L0, L1, L2... Файлы на L1 не пересекаются ключами. Чтение быстрее.

---

## 4. Оптимизация чтения: Bloom Filters

Даже с compaction, проверка дисковых файлов дорога.

**Bloom Filter** — вероятностная структура данных, которая говорит либо "элемента точно нет", либо "возможно есть".
Она маленькая и живет в памяти.

*   Если Bloom Filter говорит "Нет" -> не читаем SSTable (экономия 100% времени).
*   Если Bloom Filter говорит "Да" -> читаем SSTable (проверяем, не ложное ли срабатывание).

```python

class BloomFilter:
    """
    Упрощенный Bloom Filter на битовом массиве.
    """
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.bit_array = [0] * size
        self.hash_count = hash_count
        
    def _hashes(self, item):
        # Эмуляция разных хеш-функций через соль
        result = []
        for i in range(self.hash_count):
            h = hash(item + str(i)) % self.size
            result.append(h)
        return result
        
    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1
            
    def check(self, item):
        for h in self._hashes(item):
            if self.bit_array[h] == 0:
                return False # Точно нет
        return True # Возможно есть

# Демонстрация
bf = BloomFilter()
bf.add("user_123")
bf.add("user_456")

print(f"Contains user_123? {bf.check('user_123')}") # True
print(f"Contains user_999? {bf.check('user_999')}") # False (с большой вероятностью)
```

В LSM-движках каждый SSTable имеет свой Bloom Filter.

---

## 5. Сравнение: B-tree vs LSM-tree

Один из главных вопросов собеседований и архитектуры.

| Характеристика | B-tree (MySQL, Postgres) | LSM-tree (Cassandra, RocksDB) |
| :--- | :--- | :--- |
| **Оптимизация** | **Read-Heavy** | **Write-Heavy** |
| **Write Pattern** | Random In-Place (медленно) | Sequential Append (быстро) |
| **Read Pattern** | Быстрый, детерминированный | Медленнее (нужно проверять уровни), нужен Bloom Filter |
| **Space Amplification** | Среднее (фрагментация страниц) | Может быть высоким (старые версии данных до compaction) |
| **Write Amplification** | Высокое (запись целой страницы ради байта) | Высокое (из-за compaction файлы перезаписываются) |
| **Сценарии** | Транзакции, сложные запросы, консистентность | Логи, аналитика, IoT, высокая нагрузка на запись |

---

## 6. Write Amplification (Усиление записи)

**Write Amplification (WA)** — отношение объема данных, физически записанных на диск, к объему логических данных.
WA = (Bytes written to storage) / (Bytes written by user)

*   В **B-tree**: Меняем 10 байт, пишем страницу 4KB. WA = 4096 / 10 ≈ 400! (Хотя WAL помогает сгладить).
*   В **LSM-tree**: Пишем 10 байт в лог. Но потом при compaction этот файл будет прочитан и переписан много раз на уровни L1, L2...
    *   LSM страдает от WA на этапе compaction.

---

## 7. Практические кейсы

### 7.1 Когда выбирать LSM (RocksDB/Cassandra)?

1.  **Ingestion rate**: Вам нужно писать миллионы событий в секунду (логи, клики, сенсоры).
2.  **Working set**: Данные влезают в память или горячие данные — это последние данные.
3.  **Updates**: Вы часто обновляете данные (в LSM обновление = новая запись, это дешево).

### 7.2 Когда выбирать B-tree (Postgres)?

1.  **Read Heavy**: Читаете чаще, чем пишете.
2.  **Complex Queries**: Нужны сложные joins, транзакции, foreign keys.
3.  **Stability**: Нужна предсказуемая производительность (compaction в LSM может вызывать скачки нагрузки на CPU/Disk).

---

## 💡 Key Takeaways

- **B-tree** — король чтения, **LSM-tree** — король записи.

- **Random I/O** — враг БД. LSM превращает random writes в **sequential writes**.

- **Memtable** буферизирует и сортирует данные в памяти.

- **SSTable** хранит данные неизменяемо на диске.

- **Compaction** чистит мусор и объединяет файлы, но тратит ресурсы.

- **Bloom Filters** спасают производительность чтения в LSM.

---

## 🚀 Next Steps

**Related Modules:**

- [Транзакции и структуры данных](../08_Transactions_And_Data_Structures/) — как обеспечить ACID поверх этих структур.
- [Распределенные хеш-таблицы](../10_Distributed_Hash_Tables/) — как хранить это на кластере (Cassandra).

**Practice Ideas:**

1. Напишите простую LSM-базу на Python: `put` пишет в dict, `flush` пишет в файл, `get` читает из dict потом из файла.
2. Попробуйте вставить 1M строк в SQLite (B-tree) и в файл (Append-only). Сравните время.
3. Изучите настройки RocksDB (уровни compaction, размер memtable).

---

