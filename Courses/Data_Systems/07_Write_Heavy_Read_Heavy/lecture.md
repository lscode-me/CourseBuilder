# Write-Heavy vs Read-Heavy структуры
## LSM-tree, SSTables, Memtables и оптимизация под нагрузку

---

## 📋 Prerequisites

Перед началом этого модуля вы должны обладать следующими знаниями:

- **Hardware**: Понимать физическую разницу между оперативной памятью (RAM) и дисковыми накопителями (Disk/SSD), особенно в контексте Random vs Sequential Access.

- **Data Structures**: Знать, как работают классические B-tree индексы, используемые в реляционных базах данных, и их фундаментальные ограничения.

- **IO Metrics**: Понимать концепцию пропускной способности (throughput, MB/s) и задержки (latency, ms).

- **OS Internals**: Иметь базовое представление о работе файловой системы (syscalls: open, seek, write, fsync) и Page Cache.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Architecture**: Различать write-heavy и read-heavy нагрузки и выбирать подходящую архитектуру базы данных (LSM vs B-Tree).

- **Implementation**: Реализовать простую, но рабочую версию LSM-tree движка на Python с использованием Memtable и WAL.

- **Internals**: Детально понимать внутреннюю структуру SSTable, включая Sparse Index и Bloom Filter.

- **Production**: Настраивать RocksDB для высоконагруженных систем (Block Cache, Write Buffers, Level Multiplier).

- **Debugging**: Диагностировать и устранять проблемы "Write Stalls" в LSM-движках.

- **Math**: Рассчитывать Write Amplification (WA) и Read Amplification (RA) для разных стратегий Compaction.

---

## 1. Введение: Почему запись — это сложно?

В мире баз данных существует фундаментальный компромисс между скоростью чтения и скоростью записи. Классические реляционные базы данных (PostgreSQL, MySQL, Oracle), разработанные в 80-х и 90-х годах, были оптимизированы для **Read-Heavy** нагрузок. Они используют структуру данных B-Tree (или B+ Tree).

### 1.1 Как работает B-Tree (кратко)

B-Tree хранит данные в отсортированном виде на страницах (Pages), обычно размером 4KB, 8KB или 16KB. Эти страницы образуют дерево. Листья дерева содержат сами данные.

Главное преимущество B-Tree:

*   **Быстрое чтение**: Поиск любого ключа занимает `O(log N)` операций диска.

*   **Range Scan**: Данные отсортированы, поэтому `SELECT * FROM users WHERE age > 20` работает эффективно.

### 1.2 Random I/O — убийца производительности записи

Однако, когда дело доходит до записи, B-Tree начинает страдать.

**Проблема 1: Update-in-place**
Представьте, что вы хотите изменить всего 10 байт (например, обновить баланс пользователя). В B-Tree вы не можете записать только 10 байт. Вы должны:

1.  Прочитать всю страницу (8KB) с диска в память.
2.  Изменить 10 байт в памяти.
3.  Записать всю страницу (8KB) обратно на диск.

Это явление называется **Write Amplification (Усиление записи)**. В данном случае WA = 8192 / 10 = 819. Вы нагружаете SSD в 800 раз больше, чем нужно!

**Проблема 2: Random Writes (Случайная запись)**
Если вы вставляете новых пользователей с UUID в качестве ключа, эти вставки будут попадать в случайные листья дерева.

*   UUID `a1...` попадет в страницу 50.
*   UUID `b7...` попадет в страницу 1200.
*   UUID `1c...` попадет в страницу 3.

Для жестких дисков (HDD) это катастрофа. Головка диска должна физически перемещаться (Seek) для каждой записи. Предел HDD — около 100-200 IOPS (операций в секунду).
Для SSD это тоже плохо. Внутренняя структура SSD (NAND Flash) работает гораздо быстрее на последовательной записи, чем на случайной, из-за необходимости стирать блоки (Erase Cycles) и переписывать страницы.

**Проблема 3: Fragmentation (Фрагментация)**
Со временем страницы B-tree становятся полупустыми из-за сплитов (разделения страниц при переполнении) и удалений. Это пустая трата места и кэша.

---

## 2. Benchmark: Sequential vs Random I/O

Слова — это дешево. Давайте на цифрах.
Предположим, у нас есть обычный SATA SSD.

*   **Random Write 4KB**: ~50 MB/s (12,000 IOPS).

*   **Sequential Write**: ~500 MB/s.

Разница в **10 раз**! Если мы сможем превратить Random Writes нашего приложения в Sequential Writes на диске, мы ускорим базу данных на порядок.
Именно это и делает LSM-Tree (Log-Structured Merge-Tree).

---

## 3. Архитектура LSM-Tree

LSM-Tree используется в самых нагруженных системах мира:

*   **BigTable / LevelDB / RocksDB** (Google/Facebook)

*   **Cassandra / ScyllaDB**

*   **HBase**

*   **ClickHouse** (MergeTree Family)

*   **Kafka** (по сути Log — это вырожденный LSM)

Идея проста: **Никогда не меняйте данные на месте на диске. Всегда дописывайте новые данные в конец файла (Append Only).**

### Компонент 1: Memtable (Память)

Все входящие записи (`PUT`, `DELETE`) сначала попадают в структуру в оперативной памяти, называемую **Memtable**.
Memtable обычно реализована как сбалансированное дерево (Red-Black Tree или SkipList).
В памяти Random Writes не страшны — RAM работает одинаково быстро для любого адреса.
Данные в Memtable хранятся **отсортированными** по ключу.

### Компонент 2: WAL (Write Ahead Log)

Но что если выключат свет? Данные в RAM пропадут.
Поэтому перед записью в Memtable мы пишем операцию в **WAL (журнал предзаписи)** на диск.
WAL — это простой Append-Only файл. Писать в него очень быстро (Sequental Write).
При старте база читает WAL и восстанавливает Memtable.

### Компонент 3: SSTable (Sorted String Table) (Диск)

Когда Memtable вырастает до определенного размера (например, 64MB), она становится "Immutable" (неизменяемой) и сбрасывается на диск.
Содержимое Memtable записывается в новый файл — **SSTable**.
Так как данные в Memtable были отсортированы, SSTable тоже получается отсортированной.

**Важно**: Мы пишем SSTable последовательно, одним махом. Никаких Random Seeks. Это максимально эффективно.

### Компонент 4: Compaction (Сжатие)

Со временем у нас на диске накапливаются тысячи SSTables: `SST_1`, `SST_2`, `SST_3`...
Чтобы прочитать ключ `user:123`, нам пришлось бы искать его во всех файлах. Это медленно.
Фоновый процесс **Compaction** берет несколько SSTables, сливает их (Merge Sort), выбрасывает дубликаты и удаленные ключи, и создает одну новую, большую SSTable.

---

## 4. Глубокое погружение: SSTable Structure

SSTable — это не просто список "ключ-значение". Это индексированная структура.

Файл SSTable состоит из блоков (обычно 4KB):
```text
[Block 1: keys a..d] [Block 2: keys e..h] ... [Meta Block] [Footer]
```

Также в файле (обычно в конце) хранится **Sparse Index (Разреженный индекс)**:
```text
Key "a" -> offset 0
Key "e" -> offset 4096
Key "i" -> offset 8192
```
Этот индекс загружается в RAM.
Когда мы ищем `get("curry")`:

1.  Смотрим в индекс в RAM. Видим, что "curry" между "a" и "e".
2.  Значит, если ключ есть, он точно в **Block 1**.
3.  Делаем ОДИН seek на диск к offset 0 и читаем 4KB.
4.  Ищем внутри блока.

---

## 5. Optimization: Bloom Filters

Даже с индексом, если у нас 7 уровней файлов (L0..L6), нам может потребоваться проверить много файлов.
Если ключа НЕТ в базе, поиск будет самым дорогим (мы проверим все уровни и ничего не найдем).

**Bloom Filter** решает эту проблему.
Это битовый массив. Хеш-функции мапят ключ в биты.

*   Если фильтр говорит "НЕТ" — ключа **точно нет** в SSTable (вероятность 100%). Мы даже не лезем на диск.
*   Если фильтр говорит "ДА" — ключ **возможно есть**. Тогда читаем блок.

Bloom Filter экономит 99% ненужных чтений. Обычно настраивается 10 бит на ключ (1% False Positive Rate).

---

## 6. Implementation: LSM Engine in Python

Давайте напишем игрушечную БД за 5 минут.

```python
import os
import pickle

class SimpleLSM:
    def __init__(self, data_dir):
        self.memtable = {}
        self.data_dir = data_dir
        self.sst_counter = 0
        self.MEMTABLE_LIMIT = 100 # Маленький лимит для тестов
        os.makedirs(data_dir, exist_ok=True)

    def put(self, key, value):
        # 1. Write to Memtable
        # (В реальной жизни тут нужен WAL)
        self.memtable[key] = value
        
        # 2. Check flush condition
        if len(self.memtable) >= self.MEMTABLE_LIMIT:
            self._flush_memtable()

    def get(self, key):
        # 1. Check Memtable
        if key in self.memtable:
            return self.memtable[key]
        
        # 2. Check SSTables (in reverse order - newest first)
        # В реальности тут сложный поиск, у нас - перебор файлов
        files = sorted(os.listdir(self.data_dir), reverse=True)
        for f in files:
            data = self._read_sst(f)
            if key in data:
                return data[key]
        return None

    def _flush_memtable(self):
        filename = os.path.join(self.data_dir, f"sst_{self.sst_counter}.dat")
        # Сортируем ключи перед записью (S в SSTable значит Sorted)
        sorted_data = dict(sorted(self.memtable.items()))
        
        with open(filename, 'wb') as f:
            pickle.dump(sorted_data, f)
            
        print(f"Flushed {len(sorted_data)} keys to {filename}")
        self.memtable.clear()
        self.sst_counter += 1

    def _read_sst(self, filename):
        with open(os.path.join(self.data_dir, filename), 'rb') as f:
            return pickle.load(f)

# Usage

db = SimpleLSM("mydb_data")
for i in range(1000):
    db.put(f"key{i}", f"value{i}")

print(db.get("key999")) # From SSTable
print(db.get("key1001")) # None
```

Заметьте: простой `put` очень быстрый (вставка в dict). `get` может быть медленным (чтение файлов), но в реальных LSM ему помогают Bloom Filters и Caches.

---

## 7. Compaction Strategies (Leveled vs Tiered)

Как и когда сливать файлы? Есть две главные стратегии.

### 7.1 Leveled Compaction (RocksDB Default)

*   Данные делятся на уровни L0, L1, L2...
*   L0 — это сброшенные Memtables (перекрываются по ключам).
*   L1 и далее — файлы НЕ перекрываются.
*   Размер L(n+1) в 10 раз больше L(n).
*   **Плюс**: Очень быстрое чтение и мало места (минимум дублей).

*   **Минус**: Высокий Write Amplification (при вставке 1 байта он переписывается 10-20 раз, переезжая с уровня на уровень).
*   *Идеально для*: Read-Heavy систем, где нужна экономия места.

### 7.2 Tiered / Universal Compaction (Cassandra Default)

*   Мы просто копим SSTables.
*   Когда накопилось 4 файла одинакового размера, мы сливаем их в один большой.
*   **Плюс**: Офигенно быстрая запись (низкий Write Amplification).

*   **Минус**: Медленное чтение (много файлов проверять) и большой Space Amplification (храним много версий данных до большого слияния).
*   *Идеально для*: Write-Heavy систем (логи, TimeSeries).

---

## 8. Common Pitfalls & Tuning RocksDB

Если вы используете RocksDB (или используете БД на его основе, типа CockroachDB), вам нужно знать ручки.

1.  **Write Stalls**: Если Memtables заполняются быстрее, чем, диск успевает их сбрасывать (Flush), RocksDB **останавливает запись** полностью.
    *   *Fix*: Увеличьте `write_buffer_size` или количество `max_write_buffer_number`. Купите SSD быстрее.
2.  **Block Cache**: RocksDB кэширует разжатые блоки в RAM.
    *   *Fix*: Отдайте под Block Cache 30-50% памяти, но оставьте память OS для Page Cache (он держит сжатые файлы).
3.  **Bloom Filters**: Включите их для всех уровней (кроме последнего, может быть). Это дешево и критично для чтения.

---

## 9. RUM Conjecture

В 2016 году исследователи из Harvard/Stratos сформулировали **RUM Conjecture**.
Вы можете оптимизировать только 2 из 3 параметров Access Method:

1.  **R**ead Overhead (насколько быстро чтение).
2.  **U**pdate Overhead (насколько быстра запись).
3.  **M**emory Overhead (сколько памяти/диска тратим).

*   **B-Tree**: Good Read, Good Memory, Bad Update.

*   **LSM-Tree (Leveled)**: Good Read, Good Memory, Bad Update (из-за compaction).

*   **LSM-Tree (Tiered)**: Bad Read, Bad Memory, Good Update.

*   **Hash Index**: Perfect Read, Perfect Update, Terrible Memory (нужно держать все в RAM или иметь огромный файл).

Серебряной пули нет. Выбирайте под задачу.

---

## 10. Glossary

*   **LSM-tree (Log-Structured Merge-tree)**: Структура данных, оптимизированная для интенсивной записи через Append-only файлы и фоновое слияние.

*   **Memtable**: Буфер в оперативной памяти (обычно SkipList), куда сначала попадают все записи.

*   **SSTable (Sorted String Table)**: Неизменяемый файл на диске с отсортированными данными.

*   **WAL (Write Ahead Log)**: Журнал для восстановления Memtable после сбоя.

*   **Compaction**: Процесс слияния SSTables для удаления мусора (старых версий) и оптимизации чтения.

*   **Bloom Filter**: Вероятностная структура данных, позволяющая быстро узнать, что ключа "точно нет" в файле.

*   **Write Amplification (WA)**: Отношение объема записанных на диск данных к объему данных, пришедших от пользователя. (В LSM может быть > 10).

*   **Read Amplification (RA)**: Сколько блоков диска нужно прочитать для одного запроса `get()`.

*   **Space Amplification (SA)**: Отношение занятого места на диске к реальному объему живых данных.

*   **Tombstone**: Специальная запись-маркер для удаления ключа. (Мы не удаляем физически, а пишем "User:Deleted").

*   **Block Cache**: Кэш в оперативной памяти для распарсенных блоков данных.

*   **Minor Compaction**: Сброс Memtable в L0 SSTable.

*   **Major Compaction**: Слияние SSTables между уровнями.

*   **LevelDB**: База данных от Google, популяризировавшая LSM.

*   **RocksDB**: Форк LevelDB от Facebook, де-факто стандарт движка LSM.

*   **Universal Compaction**: Стратегия сжатия с приоритетом скорости записи (меньше мерджей).

*   **Leveled Compaction**: Стратегия сжатия с приоритетом скорости чтения и экономии места.

*   **Point Lookup**: Запрос конкретного ключа `get(k)`.

*   **Range Scan**: Запрос диапазона `scan(k1, k2)`. (LSM хорош в этом благодаря сортировке).

*   **Sparse Index**: Индекс, хранящий смещения только для *некоторых* ключей (начала блоков). Экономит RAM.

---

## 📚 Appendix A: Troubleshooting Guide

В реальном продакшене вы столкнетесь с проблемами LSM. Вот самые частые симптомы и способы их лечения.

### A.1 Symptom: Write Stalls (База зависает на запись)

**Причина**: Скорость поступления данных (Ingest Rate) выше, чем скорость диска. Memtables заполнились, диск не успел сбросить (Flush) или сжать (Compact).
**Лечение**:
1.  **Check SSD**: Вы используете HDD? Переезжайте на NVMe SSD.
2.  **Increase Write Buffers**: Дайте больше памяти под Memtables (`write_buffer_size`). Это сгладит пики (Spikes).
3.  **Parallel Flush**: Настройте RocksDB на использование большего числа тредов для сброса (`max_background_flushes`).
4.  **Rate Limiting**: Если вы не ограничите клиента сами, база ограничит его жестко (Stop). Лучше включить проактивный Rate Limiter на стороне приложения.

### A.2 Symptom: High CPU Usage

**Причина**: Compaction — это Merge Sort. Он жрет CPU.
**Лечение**:
1.  **Rate Limiter for Compaction**: В RocksDB можно ограничить скорость компакшена (`rate_limiter_bytes_per_sec`), чтобы он не съедал 100% CPU.
2.  **Delay Compaction**: Если можно, отложите Major Compaction на ночь.

### A.3 Symptom: Space Amplification (Диск переполнен)

**Причина**: Вы удалили 50% данных, но место не освободилось.
**Объяснение**: В LSM удаление — это запись Tombstone. Данные физически удалятся только при Full Compaction.
**Лечение**:
1.  **Force Compaction**: Запустите ручной компакшен (в RocksDB `CompactRange`). **Осторожно**: это положит диск.
2.  **Tombstone TTL**: Настройте удаление томбстоунов агрессивнее.

---

## 📚 Appendix B: Historical Context

Почему LSM появился именно сейчас?

### 1996: The O'Neil Paper

Патрик О'Нил публикует статью "The Log-Structured Merge-Tree (LSM-Tree)".
Тогда диски были медленными (HDD), а память дорогой. Идея была в том, чтобы кэшировать *записи*, а не *чтения* (как в B-Tree).
Идея была слишком радикальной для Oracle и IBM. Статью забыли на 10 лет.

### 2006: Google BigTable

Google строил индекс интернета. Им нужно было писать петабайты URL в день.
B-Tree не справлялся (случайная запись убивала диски).
Джефф Дин и Санджай Гемават откапали статью О'Нила и построили BigTable на основе LSM.
Это позволило Google масштабироваться до триллионов страниц.

### 2011: LevelDB

Google открыл исходный код движка BigTable под названием LevelDB (реализация на C++).
Это взорвало индустрию.

### 2013: Facebook RocksDB

Facebook форкнул LevelDB, чтобы оптимизировать его под многоядерные серверы и быстрые Flash-накопители.
Так появился RocksDB — самый популярный в мире LSM-движок. Сейчас он под капотом у CockroachDB, MyRocks, TiKV, Kafka Streams.

---

## 📚 Appendix C: FAQ (Часто задаваемые вопросы)

**Q1: Можно ли использовать LSM для транзакций (OLTP)?**
**A**: Да. CockroachDB и YugabyteDB построены на RocksDB и поддерживают SERIALIZABLE транзакции. LSM обеспечивает Durability и Atomic Writes, а транзакционный слой (2PL/MVCC) строим поверх.

**Q2: Почему Postgres не перейдет на LSM?**
**A**: В Postgres есть проект "zheap" и расширения, но это сложно. B-Tree глубоко интегрировано в архитектуру (Vacuum, WAL, Indexing). Переписать движок хранения — это как заменить фундамент небоскреба.

**Q3: Что лучше для SSD: B-Tree или LSM?**
**A**: SSD *могут* делать Random Read быстро (хорошо для B-Tree и LSM), но Random Write изнашивает их (Write Amplification). LSM пишет последовательно большими блоками, что **значительно продлевает жизнь SSD**.

**Q4: Как работает Range Scan в LSM, если ключи разбросаны по 10 файлам?**
**A**: Мы открываем итераторы по всем 10 файлам (плюс Memtable) и используем структуру данных `MinHeap` (Priority Queue), чтобы сливать потоки на лету. Это работает как Merge Sort. Да, это медленнее, чем в B-Tree (где один файл), но терпимо.

**Q5: Нужен ли мне Bloom Filter, если я делаю только Range Scan?**
**A**: Нет. Bloom Filter работает только для точного поиска (`get(key)`). Для `scan(start, end)` он бесполезен.

**Q6: Что такое Universal Compaction?**
**A**: Также известно как Size-Tiered (используется в Cassandra). Мы не держим уровни разного размера. Мы просто сливаем файлы одинакового размера. Это быстрее для записи, но хуже для чтения.

**Q7: Почему Memtable использует SkipList, а не Red-Black Tree?**
**A**: SkipList проще реализовать Concurrent (lock-free) доступ. В Red-Black Tree перебалансировка затрагивает много узлов, требуя сложных блокировок.

**Q8: Можно ли потерять данные в LSM?**
**A**: Если вы отключили WAL (для скорости) — да, при сбое питания Memtable исчезнет. С включенным WAL гарантии такие же, как в любой другой БД.

**Q9: Я удалил ключ, но он все еще находится в `scan()`. Почему?**
**A**: Скорее всего, вы видите Tombstone (если смотрите на сырые данные) или баг в фильтрации. Обычно движок скрывает удаленные записи.

**Q10: Как мониторить LSM?**
**A**: Смотрите на:
1.  **Memtable Flush Count**: Как часто сбрасываем память.
2.  **L0 Files Count**: Если их много (>4), значит Compaction не справляется. Тормозит чтение.
3.  **Write Stall Duration**: Время, когда база висит. Должно быть 0.

---

## 💡 Key Takeaways

1.  **LSM for Writes**: Если у вас лог событий, чат, метрики — LSM (Cassandra, Clickhouse) уничтожит B-Tree (Postgres) по скорости вставки.
2.  **Sequential I/O is King**: Вся магия LSM — в превращении случайной записи приложения в последовательную запись на диск.
3.  **Tuning is Required**: LSM требует настройки Compaction под вашу нагрузку. Дефолтные настройки RocksDB редко бывают идеальными.
4.  **Deletes are Writes**: Удаление в LSM — это просто запись Tombstone. Место освободится только после Compaction.
5.  **Troubleshooting**: High CPU на LSM — это обычно Compaction. High Disk Usage — это Space Amplification.

---

## 🚀 Next Steps

**Практика:**

1.  Запустите `SimpleLSM` код локально.
2.  Посмотрите на папку `mydb_data`. Откройте файлы `sst_X.dat` (они бинарные, но можно увидеть строки).
3.  Попробуйте удалить ключ: `db.put("key1", None)`. Посмотрите, что `get` вернет None, но файл на диске вырастет (Tombstone).

В следующем модуле мы спустимся еще глубже — к **Транзакциям**. Что такое ACID и как обеспечить изоляцию, когда 1000 клиентов пишут одновременно? [Transactions And Data Structures](../08_Transactions_And_Data_Structures/).


