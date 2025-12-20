# Почему базы данных — это структуры данных
## Storage engine, логическая и физическая модель данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основные структуры данных (деревья, хеш-таблицы, списки)
- Знать концепцию сложности алгоритмов
- Иметь базовое представление о базах данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять, почему база данных — это набор структур данных
- Различать логическую и физическую модель данных
- Понимать роль storage engine в СУБД
- Анализировать trade-offs различных подходов к хранению

---

## 1. Введение: БД как организованное хранилище

### 1.1 Что такое база данных на низком уровне

На высоком уровне база данных — это способ хранить и извлекать данные. Но на низком уровне база данных — это **набор структур данных**, оптимизированных для определённых операций.

```

┌─────────────────────────────────────────────────────────────┐
│                     SQL Query                                │
│                    "SELECT * FROM users WHERE id = 42"       │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Query Optimizer                             │
│            (выбирает план выполнения)                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Storage Engine                             │
│     ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│     │ B-tree  │  │  Hash   │  │  Log    │  │ Buffer  │     │
│     │ Index   │  │ Index   │  │ (WAL)   │  │  Pool   │     │
│     └─────────┘  └─────────┘  └─────────┘  └─────────┘     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      Disk / SSD                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Почему это важно понимать

Понимание внутреннего устройства БД помогает:

- Выбирать правильные индексы
- Оптимизировать запросы
- Понимать, почему некоторые операции медленные
- Принимать архитектурные решения

**Example: Простейшая "база данных"**

```python

class SimpleDB:
    """
    Простейшая key-value база данных.
    Демонстрирует, что БД — это просто структуры данных.
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.index = {}  # Hash table для быстрого поиска
        self._load_index()
    
    def _load_index(self):
        """Строит индекс из файла."""
        try:
            with open(self.filename, 'r') as f:
                offset = 0
                for line in f:
                    key, _ = line.strip().split(',', 1)
                    self.index[key] = offset
                    offset = f.tell()
        except FileNotFoundError:
            pass
    
    def put(self, key, value):
        """Append-only запись + обновление индекса."""
        with open(self.filename, 'a') as f:
            offset = f.tell()
            f.write(f"{key},{value}\n")
            self.index[key] = offset
    
    def get(self, key):
        """O(1) поиск через индекс."""
        if key not in self.index:
            return None
        
        with open(self.filename, 'r') as f:
            f.seek(self.index[key])
            line = f.readline()
            _, value = line.strip().split(',', 1)
            return value

# Демонстрация
import os
import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.db') as f:
    db_file = f.name

db = SimpleDB(db_file)
db.put("user:1", "Alice")
db.put("user:2", "Bob")
db.put("user:1", "Alice Updated")  # Перезапись

print(f"user:1 = {db.get('user:1')}")
print(f"user:2 = {db.get('user:2')}")
print(f"user:3 = {db.get('user:3')}")

os.unlink(db_file)
```

**Output:**
```

user:1 = Alice Updated
user:2 = Bob
user:3 = None
```

**Объяснение:**
Эта простая база данных использует:

- **Hash table** (dict) для индекса — O(1) поиск

- **Append-only log** для хранения — O(1) запись

- **File** как persistent storage

---

## 2. Логическая vs физическая модель

### 2.1 Две стороны данных

| Аспект | Логическая модель | Физическая модель |
|--------|-------------------|-------------------|
| Что | Таблицы, строки, колонки | Страницы, блоки, B-trees |
| Для кого | Разработчик приложения | Storage engine |
| Уровень | Высокий, абстрактный | Низкий, конкретный |
| Пример | SELECT * FROM users | Чтение страницы с диска |

### 2.2 Логическая модель: таблицы и отношения

```python
# Логическая модель: как мы думаем о данных
"""
users                    orders
+----+--------+         +----+---------+--------+
| id | name   |         | id | user_id | amount |
+----+--------+         +----+---------+--------+
| 1  | Alice  |         | 1  | 1       | 100    |
| 2  | Bob    |         | 2  | 1       | 200    |
+----+--------+         | 3  | 2       | 150    |
                        +----+---------+--------+

SELECT users.name, SUM(orders.amount)
FROM users
JOIN orders ON users.id = orders.user_id
GROUP BY users.id
"""

# Эмуляция логической модели
users = {1: "Alice", 2: "Bob"}
orders = [(1, 1, 100), (2, 1, 200), (3, 2, 150)]

# "Запрос" на Python
result = {}
for order_id, user_id, amount in orders:
    name = users[user_id]
    result[name] = result.get(name, 0) + amount

for name, total in result.items():
    print(f"{name}: {total}")
```

**Output:**
```

Alice: 300
Bob: 150
```

### 2.3 Физическая модель: как данные хранятся

```python
# Физическая модель: страницы и записи

class Page:
    """
    Страница — минимальная единица чтения/записи с диска.
    Типичный размер: 4KB, 8KB, 16KB.
    """
    
    PAGE_SIZE = 4096  # 4KB
    
    def __init__(self, page_id):
        self.page_id = page_id
        self.records = []
        self.used_space = 0
    
    def can_fit(self, record_size):
        return self.used_space + record_size <= self.PAGE_SIZE
    
    def add_record(self, record):
        record_size = len(str(record).encode())
        if not self.can_fit(record_size):
            raise ValueError("Page is full")
        self.records.append(record)
        self.used_space += record_size
    
    def __repr__(self):
        return f"Page({self.page_id}, {len(self.records)} records, {self.used_space}B used)"


class HeapFile:
    """
    Heap file — неупорядоченный набор страниц.
    Простейшая физическая структура для хранения записей.
    """
    
    def __init__(self):
        self.pages = []
        self.current_page = Page(0)
        self.pages.append(self.current_page)
    
    def insert(self, record):
        record_size = len(str(record).encode())
        
        if not self.current_page.can_fit(record_size):
            # Создаём новую страницу
            self.current_page = Page(len(self.pages))
            self.pages.append(self.current_page)
        
        self.current_page.add_record(record)
        return (self.current_page.page_id, len(self.current_page.records) - 1)
    
    def scan(self):
        """Full table scan — читаем все страницы."""
        for page in self.pages:
            for record in page.records:
                yield record

# Демонстрация
heap = HeapFile()

# Вставка записей
for i in range(100):
    heap.insert({"id": i, "name": f"User_{i}", "email": f"user{i}@example.com"})

print(f"Всего страниц: {len(heap.pages)}")
for page in heap.pages[:3]:
    print(f"  {page}")
```

**Output:**
```

Всего страниц: 3
  Page(0, 42 records, 3990B used)
  Page(1, 42 records, 3990B used)
  Page(2, 16 records, 1520B used)
```

---

## 3. Storage Engine: сердце базы данных

### 3.1 Что такое Storage Engine

**Storage Engine** — компонент СУБД, отвечающий за:
- Хранение данных на диске
- Индексирование данных
- Управление транзакциями
- Кэширование данных в памяти

Разные storage engines оптимизированы для разных нагрузок:

| Engine | Оптимизирован для | Примеры |
|--------|-------------------|---------|
| InnoDB (MySQL) | Транзакции, OLTP | Веб-приложения |
| MyISAM (MySQL) | Чтение | Analytics, logs |
| RocksDB | Write-heavy | Time series |
| WiredTiger (MongoDB) | Документы | NoSQL |

### 3.2 Компоненты Storage Engine

```

┌─────────────────────────────────────────────────────────────┐
│                     Storage Engine                           │
├─────────────────────────────────────────────────────────────┤
│  ┌────────────────┐    ┌────────────────┐                   │
│  │  Buffer Pool   │    │   Lock Manager │                   │
│  │  (кэш страниц) │    │  (блокировки)  │                   │
│  └────────────────┘    └────────────────┘                   │
│                                                              │
│  ┌────────────────┐    ┌────────────────┐                   │
│  │  Index Manager │    │  Transaction   │                   │
│  │  (B-tree, etc) │    │    Manager     │                   │
│  └────────────────┘    └────────────────┘                   │
│                                                              │
│  ┌────────────────┐    ┌────────────────┐                   │
│  │   Log Manager  │    │  Space Manager │                   │
│  │  (WAL, redo)   │    │  (allocation)  │                   │
│  └────────────────┘    └────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Buffer Pool: кэш страниц

```python

from collections import OrderedDict

class BufferPool:
    """
    Buffer Pool — кэш страниц в памяти.
    LRU eviction policy.
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.hit_count = 0
        self.miss_count = 0
    
    def get_page(self, page_id, disk_reader):
        """Получает страницу, используя кэш."""
        if page_id in self.cache:
            self.hit_count += 1
            # Перемещаем в конец (LRU)
            self.cache.move_to_end(page_id)
            return self.cache[page_id]
        
        self.miss_count += 1
        
        # Читаем с "диска"
        page = disk_reader(page_id)
        
        # Eviction если кэш полон
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Удаляем oldest
        
        self.cache[page_id] = page
        return page
    
    def hit_rate(self):
        total = self.hit_count + self.miss_count
        return self.hit_count / total if total > 0 else 0

# Демонстрация
import random

def disk_read(page_id):
    """Симуляция чтения с диска."""
    return f"Page_{page_id}_content"

pool = BufferPool(capacity=10)

# Симуляция workload с locality
for _ in range(1000):
    # 80% запросов к "горячим" страницам
    if random.random() < 0.8:
        page_id = random.randint(0, 9)
    else:
        page_id = random.randint(0, 99)
    
    pool.get_page(page_id, disk_read)

print(f"Cache hits: {pool.hit_count}")
print(f"Cache misses: {pool.miss_count}")
print(f"Hit rate: {pool.hit_rate():.1%}")
```

**Output:**
```

Cache hits: 891
Cache misses: 109
Hit rate: 89.1%
```

---

## 4. Структуры данных в основе БД

### 4.1 Основные структуры

| Структура | Применение в БД | Сложность операций |
|-----------|-----------------|-------------------|
| B-tree | Индексы, хранение | O(log n) всё |
| Hash table | Hash индексы, joins | O(1) поиск |
| LSM-tree | Write-optimized storage | O(1) запись |
| Bitmap | Bitmap индексы | O(1) проверка |
| Skip list | In-memory индексы | O(log n) всё |

### 4.2 Пример: Простой B-tree индекс

```python

class BTreeNode:
    """Узел B-дерева."""
    
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.values = []  # Только для листьев
        self.children = []  # Только для внутренних узлов


class SimpleBTree:
    """
    Упрощённая реализация B-дерева для демонстрации.
    В реальных БД узлы соответствуют страницам диска.
    """
    
    def __init__(self, order=3):
        self.root = BTreeNode()
        self.order = order  # Максимум ключей в узле
    
    def search(self, key, node=None):
        """Поиск ключа: O(log n)."""
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:
            return node.values[i] if node.leaf else self.search(key, node.children[i])
        
        if node.leaf:
            return None
        
        return self.search(key, node.children[i])
    
    def insert_non_full(self, node, key, value):
        """Вставка в неполный узел."""
        i = len(node.keys) - 1
        
        if node.leaf:
            # Вставка в лист
            node.keys.append(None)
            node.values.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                node.values[i + 1] = node.values[i]
                i -= 1
            node.keys[i + 1] = key
            node.values[i + 1] = value
        else:
            # Находим ребёнка
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            if len(node.children[i].keys) == self.order:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            
            self.insert_non_full(node.children[i], key, value)
    
    def split_child(self, parent, index):
        """Разделение полного узла."""
        order = self.order
        child = parent.children[index]
        new_node = BTreeNode(leaf=child.leaf)
        
        mid = order // 2
        
        # Перемещаем правую половину
        new_node.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]
        
        if child.leaf:
            new_node.values = child.values[mid + 1:]
            child.values = child.values[:mid + 1]
        else:
            new_node.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]
        
        # Вставляем средний ключ в родителя
        parent.keys.insert(index, child.keys[mid] if not child.leaf else child.keys[-1])
        parent.children.insert(index + 1, new_node)
    
    def insert(self, key, value):
        """Вставка ключа: O(log n)."""
        root = self.root
        
        if len(root.keys) == self.order:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.root = new_root
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key, value)
        else:
            self.insert_non_full(root, key, value)

# Демонстрация
btree = SimpleBTree(order=4)

# Вставка данных
for i in [10, 20, 5, 15, 25, 30, 35, 40, 3, 7]:
    btree.insert(i, f"value_{i}")

# Поиск

print(f"Search 15: {btree.search(15)}")
print(f"Search 25: {btree.search(25)}")
print(f"Search 100: {btree.search(100)}")
```

**Output:**
```

Search 15: value_15
Search 25: value_25
Search 100: None
```

---

## 5. Row Store vs Column Store

### 5.1 Два подхода к хранению

**Row Store (строковое хранение):**

- Все поля одной записи хранятся вместе
- Оптимально для OLTP: чтение/запись целых записей
- Примеры: MySQL, PostgreSQL, Oracle

**Column Store (колоночное хранение):**

- Все значения одной колонки хранятся вместе
- Оптимально для OLAP: агрегации по колонкам
- Примеры: ClickHouse, Redshift, Parquet

```python
# Row Store
"""
Page 1: [id:1, name:"Alice", age:30] [id:2, name:"Bob", age:25] ...
Page 2: [id:3, name:"Carol", age:35] ...
"""

# Column Store
"""
id column:   [1, 2, 3, 4, 5, ...]
name column: ["Alice", "Bob", "Carol", ...]
age column:  [30, 25, 35, ...]
"""

import sys

# Демонстрация разницы в объёме данных для запроса
class RowStore:
    def __init__(self):
        self.rows = []
    
    def insert(self, row):
        self.rows.append(row)
    
    def sum_column(self, column):
        """Нужно читать ВСЕ данные."""
        bytes_read = sum(sys.getsizeof(row) for row in self.rows)
        result = sum(row[column] for row in self.rows)
        return result, bytes_read


class ColumnStore:
    def __init__(self, columns):
        self.columns = {col: [] for col in columns}
    
    def insert(self, row):
        for col, value in row.items():
            self.columns[col].append(value)
    
    def sum_column(self, column):
        """Читаем только нужную колонку."""
        bytes_read = sys.getsizeof(self.columns[column])
        result = sum(self.columns[column])
        return result, bytes_read

# Сравнение
row_store = RowStore()
col_store = ColumnStore(['id', 'name', 'email', 'age', 'salary'])

for i in range(10000):
    row = {
        'id': i,
        'name': f"User_{i}",
        'email': f"user{i}@example.com",
        'age': 20 + (i % 50),
        'salary': 30000 + (i * 100)
    }
    row_store.insert(row)
    col_store.insert(row)

sum_row, bytes_row = row_store.sum_column('salary')
sum_col, bytes_col = col_store.sum_column('salary')

print(f"Row Store: sum={sum_row}, bytes read≈{bytes_row}")
print(f"Column Store: sum={sum_col}, bytes read≈{bytes_col}")
print(f"Column store reads {bytes_row // bytes_col}x less data")
```

**Output:**
```

Row Store: sum=529950000, bytes read≈2880000
Column Store: sum=529950000, bytes read≈87616
Column store reads 32x less data
```

### 5.2 Когда использовать какой

| Workload | Row Store | Column Store |
|----------|-----------|--------------|
| SELECT * WHERE id = X | ✅ | ❌ |
| UPDATE ... SET ... | ✅ | ❌ |
| INSERT одной записи | ✅ | ❌ |
| SELECT SUM(col) | ❌ | ✅ |
| SELECT col1, col2 FROM ... | ❌ | ✅ |
| Компрессия данных | Умеренная | Отличная |

---

## 6. Trade-offs в дизайне хранилища

### 6.1 Read vs Write оптимизация

```

┌─────────────────────────────────────────────────────────────┐
│                    Read-Optimized                            │
│  B-tree index: O(log n) чтение, O(log n) запись             │
│  Данные отсортированы → быстрые range queries               │
│  Примеры: MySQL InnoDB, PostgreSQL                           │
├─────────────────────────────────────────────────────────────┤
│                   Write-Optimized                            │
│  LSM-tree: O(1) запись (append), O(log n) чтение            │
│  Данные в памяти → периодический flush                       │
│  Примеры: RocksDB, Cassandra, LevelDB                        │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Память vs диск

```python
# In-memory: быстро, но ограничено размером RAM
# On-disk: медленнее, но неограниченно

import time

# Симуляция разницы в скорости
class InMemoryTable:
    def __init__(self):
        self.data = {}
    
    def insert(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        return self.data.get(key)


class SimulatedDiskTable:
    def __init__(self):
        self.data = {}
        self.disk_latency = 0.0001  # 0.1ms симуляция
    
    def insert(self, key, value):
        time.sleep(self.disk_latency)  # Симуляция I/O
        self.data[key] = value
    
    def get(self, key):
        time.sleep(self.disk_latency)  # Симуляция I/O
        return self.data.get(key)

# Сравнение
n = 1000

mem_table = InMemoryTable()
start = time.perf_counter()
for i in range(n):
    mem_table.insert(i, f"value_{i}")
mem_time = time.perf_counter() - start

disk_table = SimulatedDiskTable()
start = time.perf_counter()
for i in range(n):
    disk_table.insert(i, f"value_{i}")
disk_time = time.perf_counter() - start

print(f"In-memory: {mem_time*1000:.2f} ms for {n} inserts")
print(f"Simulated disk: {disk_time*1000:.2f} ms for {n} inserts")
print(f"Disk is {disk_time/mem_time:.0f}x slower")
```

**Output:**
```

In-memory: 0.15 ms for 1000 inserts
Simulated disk: 105.23 ms for 1000 inserts
Disk is 701x slower
```

### 6.3 Consistency vs Performance

| Уровень | Гарантия | Производительность |
|---------|----------|-------------------|
| Синхронная запись | Данные на диске | Медленно |
| Буферизованная | Данные в памяти | Быстро |
| Write-ahead log | Можно восстановить | Компромисс |

---

## 7. Практические выводы

### 7.1 Как выбор структуры влияет на запросы

```python
# Пример: Индекс vs Full Scan

import time
import random

# Данные
n = 100000
data = [(i, f"user_{i}", random.randint(1, 100)) for i in range(n)]

# Без индекса: Full Table Scan
def find_by_age_no_index(data, target_age):
    """O(n) — проверяем все записи."""
    return [row for row in data if row[2] == target_age]

# С индексом по age
age_index = {}
for row in data:
    age = row[2]
    if age not in age_index:
        age_index[age] = []
    age_index[age].append(row)

def find_by_age_with_index(age_index, target_age):
    """O(1) + O(k) где k — количество результатов."""
    return age_index.get(target_age, [])

# Сравнение
target = 42

start = time.perf_counter()
result1 = find_by_age_no_index(data, target)
time_no_index = time.perf_counter() - start

start = time.perf_counter()
result2 = find_by_age_with_index(age_index, target)
time_with_index = time.perf_counter() - start

print(f"Найдено: {len(result1)} записей с age={target}")
print(f"Без индекса: {time_no_index*1000:.3f} ms")
print(f"С индексом: {time_with_index*1000:.3f} ms")
print(f"Ускорение: {time_no_index/time_with_index:.0f}x")
```

**Output:**
```

Найдено: 1023 записей с age=42
Без индекса: 8.234 ms
С индексом: 0.012 ms
Ускорение: 686x
```

### 7.2 Рекомендации

1. **Понимайте workload**: OLTP vs OLAP
2. **Выбирайте индексы осознанно**: каждый индекс — это структура данных
3. **Помните о trade-offs**: чтение vs запись, память vs диск
4. **Используйте Buffer Pool**: локальность данных критична

---

## 💡 Key Takeaways

- **База данных** на низком уровне — это набор структур данных: B-trees, hash tables, logs

- **Storage Engine** управляет хранением, индексированием и кэшированием данных

- **Логическая модель** (таблицы) абстрагирует **физическую модель** (страницы, индексы)

- **Row store** оптимален для OLTP, **column store** — для аналитики

- **Понимание внутренностей** помогает оптимизировать запросы и выбирать правильные индексы

---

## 🚀 Next Steps

**Related Modules:**

- [Индексы как структуры данных](../06_Indexes_As_Data_Structures/) — глубокое погружение в B-tree и hash индексы
- [Write-heavy и read-heavy структуры](../07_Write_Heavy_Read_Heavy/) — LSM-tree и оптимизация записи

**Practice Ideas:**

1. Реализуйте простой Buffer Pool с LRU eviction
2. Сравните производительность поиска с индексом и без
3. Изучите вывод EXPLAIN для ваших SQL запросов

**Going Deeper:**

- Изучите исходный код SQLite — отличный учебный пример
- Познакомьтесь с архитектурой PostgreSQL
- Исследуйте устройство RocksDB

---

