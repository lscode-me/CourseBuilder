# Индексы как структуры данных
## B-tree, B+ tree, Hash index, Bitmap index и их trade-offs

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать, почему база данных — это набор структур данных
- Знать концепцию Big-O и сложности операций
- Иметь базовое представление о деревьях и хеш-таблицах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять устройство B-tree и B+ tree индексов
- Понимать trade-offs различных типов индексов
- Выбирать правильный тип индекса для конкретной задачи
- Анализировать, когда индекс помогает, а когда мешает

---

## 1. Зачем нужны индексы

### 1.1 Проблема без индексов

Без индекса любой поиск требует **Full Table Scan** — чтения всех страниц таблицы.

```python
import time
import random

# Симуляция таблицы без индекса

class TableWithoutIndex:
    def __init__(self):
        self.rows = []
    
    def insert(self, row):
        self.rows.append(row)
    
    def find_by_id(self, target_id):
        """O(n) — проверяем все записи."""
        for row in self.rows:
            if row['id'] == target_id:
                return row
        return None

# Симуляция таблицы с индексом

class TableWithIndex:
    def __init__(self):
        self.rows = []
        self.id_index = {}  # Hash index
    
    def insert(self, row):
        self.rows.append(row)
        self.id_index[row['id']] = len(self.rows) - 1
    
    def find_by_id(self, target_id):
        """O(1) — прямой доступ через индекс."""
        if target_id not in self.id_index:
            return None
        return self.rows[self.id_index[target_id]]

# Сравнение

n = 100000
data = [{'id': i, 'name': f'User_{i}', 'email': f'user{i}@example.com'} for i in range(n)]

table_no_idx = TableWithoutIndex()
table_with_idx = TableWithIndex()

for row in data:
    table_no_idx.insert(row)
    table_with_idx.insert(row)

target = n - 1

start = time.perf_counter()
table_no_idx.find_by_id(target)
time_no_idx = time.perf_counter() - start

start = time.perf_counter()
table_with_idx.find_by_id(target)
time_with_idx = time.perf_counter() - start

print(f"Без индекса: {time_no_idx*1000:.3f} мс")
print(f"С индексом: {time_with_idx*1000:.6f} мс")
print(f"Ускорение: {time_no_idx/time_with_idx:.0f}x")
```

**Output:**
```
Без индекса: 5.234 мс
С индексом: 0.000234 мс
Ускорение: 22367x
```

### 1.2 Что такое индекс

**Индекс** — это дополнительная структура данных, которая:
- Хранит ссылки на записи таблицы
- Упорядочена или хеширована для быстрого поиска
- Занимает дополнительное место
- Замедляет вставку/обновление (нужно обновлять индекс)

---

## 2. B-tree индекс

### 2.1 Почему B-tree

**B-tree** (Balanced tree) — основная структура для индексов в реляционных БД:
- Сбалансированное дерево → гарантированная высота O(log n)
- Узлы оптимизированы под размер страницы диска
- Поддерживает range queries эффективно
- Данные отсортированы

```
                    [50, 100]
                   /    |    \
         [10, 25]    [75]    [125, 150]
         /  |  \      |       /   |   \
       [5] [15] [30] [60,80] [110] [130] [160]
```

### 2.2 Свойства B-tree

| Свойство | Значение |
|----------|----------|
| Поиск | O(log n) |
| Вставка | O(log n) |
| Удаление | O(log n) |
| Range query | O(log n + k) |
| Пространство | O(n) |

### 2.3 Реализация B-tree индекса

```python
class BTreeIndex:
    """
    Упрощённый B-tree индекс.
    В реальных БД узлы соответствуют страницам диска.
    """
    
    def __init__(self, order=100):
        self.order = order  # Максимум ключей в узле
        self.root = {'keys': [], 'children': [], 'values': [], 'leaf': True}
    
    def search(self, key):
        """Поиск ключа: O(log n)."""
        return self._search(self.root, key)
    
    def _search(self, node, key):
        i = 0
        while i < len(node['keys']) and key > node['keys'][i]:
            i += 1
        
        if i < len(node['keys']) and key == node['keys'][i]:
            return node['values'][i] if node['leaf'] else self._search(node['children'][i], key)
        
        if node['leaf']:
            return None
        
        return self._search(node['children'][i], key)
    
    def range_search(self, low, high):
        """Range query: O(log n + k) где k — количество результатов."""
        results = []
        self._range_search(self.root, low, high, results)
        return results
    
    def _range_search(self, node, low, high, results):
        i = 0
        while i < len(node['keys']) and node['keys'][i] < low:
            i += 1
        
        while i < len(node['keys']) and node['keys'][i] <= high:
            if node['leaf']:
                results.append((node['keys'][i], node['values'][i]))
            else:
                self._range_search(node['children'][i], low, high, results)
            i += 1
        
        if not node['leaf'] and i < len(node['children']):
            self._range_search(node['children'][i], low, high, results)
    
    def insert(self, key, value):
        """Вставка: O(log n)."""
        # Упрощённая вставка для демонстрации
        self._insert_leaf(self.root, key, value)
    
    def _insert_leaf(self, node, key, value):
        if node['leaf']:
            # Вставляем в отсортированном порядке
            i = 0
            while i < len(node['keys']) and key > node['keys'][i]:
                i += 1
            node['keys'].insert(i, key)
            node['values'].insert(i, value)
        else:
            # Находим нужного ребёнка
            i = 0
            while i < len(node['keys']) and key > node['keys'][i]:
                i += 1
            self._insert_leaf(node['children'][i], key, value)

# Демонстрация

index = BTreeIndex()

# Вставка данных

for i in range(1000):
    index.insert(i, f"row_pointer_{i}")

# Точечный поиск

print(f"Search 500: {index.search(500)}")
print(f"Search 9999: {index.search(9999)}")

# Range query

range_results = index.range_search(10, 15)
print(f"Range [10, 15]: {range_results}")
```

**Output:**
```
Search 500: row_pointer_500
Search 9999: None
Range [10, 15]: [(10, 'row_pointer_10'), (11, 'row_pointer_11'), (12, 'row_pointer_12'), (13, 'row_pointer_13'), (14, 'row_pointer_14'), (15, 'row_pointer_15')]
```

---

## 3. B+ tree индекс

### 3.1 Отличия от B-tree

**B+ tree** — модификация B-tree, используемая в большинстве СУБД:

| Аспект | B-tree | B+ tree |
|--------|--------|---------|
| Данные | В любых узлах | Только в листьях |
| Листья | Не связаны | Связанный список |
| Range queries | Медленнее | Быстрее |
| Дублирование ключей | Нет | Да (в листьях) |

```
B+ tree структура:

Internal nodes (только ключи для навигации):
                    [50, 100]
                   /    |    \
Internal:    [25, 35]  [75]  [125, 150]

Leaf nodes (данные + связанный список):
[10,20,25] → [30,35,40] → [50,60,75] → [80,90,100] → [110,125,130] → [150,160]
```

### 3.2 Почему B+ tree лучше для БД

```python
class BPlusTreeLeaf:
    """Лист B+ дерева со ссылкой на следующий лист."""
    
    def __init__(self):
        self.keys = []
        self.values = []
        self.next = None  # Ссылка на следующий лист

class SimpleBPlusTree:
    """
    Упрощённая демонстрация B+ tree.
    Показывает преимущество связанных листьев для range queries.
    """
    
    def __init__(self, leaf_size=10):
        self.leaf_size = leaf_size
        self.leaves = []
        self.current_leaf = BPlusTreeLeaf()
        self.leaves.append(self.current_leaf)
    
    def insert(self, key, value):
        """Вставка (упрощённая)."""
        if len(self.current_leaf.keys) >= self.leaf_size:
            new_leaf = BPlusTreeLeaf()
            self.current_leaf.next = new_leaf
            self.current_leaf = new_leaf
            self.leaves.append(new_leaf)
        
        self.current_leaf.keys.append(key)
        self.current_leaf.values.append(value)
    
    def range_scan(self, start_key, end_key):
        """
        Range scan: O(log n) для нахождения начала + O(k) для сканирования.
        Благодаря связанным листьям не нужно возвращаться к родителям.
        """
        results = []
        
        # Находим начальный лист (упрощённо — линейный поиск)
        current = self.leaves[0]
        for leaf in self.leaves:
            if leaf.keys and leaf.keys[0] <= start_key:
                current = leaf
        
        # Сканируем листья последовательно
        while current:
            for i, key in enumerate(current.keys):
                if start_key <= key <= end_key:
                    results.append((key, current.values[i]))
                elif key > end_key:
                    return results
            current = current.next
        
        return results

# Демонстрация

bplus = SimpleBPlusTree(leaf_size=5)

for i in range(50):
    bplus.insert(i * 2, f"data_{i*2}")

# Range scan — очень эффективен благодаря связанным листьям

results = bplus.range_scan(10, 30)
print(f"Range [10, 30]:")
for key, value in results:
    print(f"  {key}: {value}")
```

**Output:**
```
Range [10, 30]:
  10: data_10
  12: data_12
  14: data_14
  16: data_16
  18: data_18
  20: data_20
  22: data_22
  24: data_24
  26: data_26
  28: data_28
  30: data_30
```

---

## 4. Hash Index

### 4.1 Принцип работы

**Hash Index** использует хеш-функцию для прямого доступа:
- O(1) для точечных запросов
- Не поддерживает range queries
- Не поддерживает ORDER BY

```python
class HashIndex:
    """
    Hash индекс: O(1) поиск, но только для equality.
    """
    
    def __init__(self, buckets=1024):
        self.buckets = buckets
        self.table = [[] for _ in range(buckets)]
    
    def _hash(self, key):
        return hash(key) % self.buckets
    
    def insert(self, key, value):
        """O(1) вставка."""
        bucket = self._hash(key)
        # Проверяем на обновление
        for i, (k, v) in enumerate(self.table[bucket]):
            if k == key:
                self.table[bucket][i] = (key, value)
                return
        self.table[bucket].append((key, value))
    
    def search(self, key):
        """O(1) поиск."""
        bucket = self._hash(key)
        for k, v in self.table[bucket]:
            if k == key:
                return v
        return None
    
    def range_search(self, low, high):
        """Hash индекс НЕ поддерживает range queries эффективно!"""
        # Приходится проходить все buckets — O(n)
        results = []
        for bucket in self.table:
            for k, v in bucket:
                if low <= k <= high:
                    results.append((k, v))
        return results

# Демонстрация

hash_idx = HashIndex()

for i in range(10000):
    hash_idx.insert(i, f"value_{i}")

import time

# Точечный поиск — O(1)

start = time.perf_counter()
for _ in range(1000):
    hash_idx.search(5000)
time_point = time.perf_counter() - start

# Range query — O(n), очень медленно!

start = time.perf_counter()
hash_idx.range_search(100, 200)
time_range = time.perf_counter() - start

print(f"1000 точечных запросов: {time_point*1000:.2f} мс")
print(f"Один range query: {time_range*1000:.2f} мс")
```

**Output:**
```
1000 точечных запросов: 0.45 мс
Один range query: 2.34 мс
```

### 4.2 Когда использовать Hash Index

| Сценарий | Hash Index | B-tree Index |
|----------|------------|--------------|
| WHERE id = 5 | ✅ O(1) | ⚪ O(log n) |
| WHERE id BETWEEN 1 AND 100 | ❌ O(n) | ✅ O(log n + k) |
| ORDER BY id | ❌ | ✅ |
| GROUP BY | ❌ | ⚪ |
| JOIN по ключу | ✅ | ⚪ |

---

## 5. Bitmap Index

### 5.1 Принцип работы

**Bitmap Index** эффективен для колонок с низкой кардинальностью:
- Каждому значению соответствует битовая маска
- AND/OR операции очень быстрые
- Отлично сжимается

```python
class BitmapIndex:
    """
    Bitmap индекс для колонки с низкой кардинальностью.
    """
    
    def __init__(self):
        self.bitmaps = {}  # value -> bitmap (list of bits)
        self.size = 0
    
    def build(self, data):
        """Строит bitmap индекс из данных."""
        self.size = len(data)
        
        # Находим уникальные значения
        unique_values = set(data)
        
        # Создаём bitmap для каждого значения
        for value in unique_values:
            self.bitmaps[value] = [0] * self.size
        
        # Заполняем bitmaps
        for i, value in enumerate(data):
            self.bitmaps[value][i] = 1
    
    def query_equals(self, value):
        """WHERE column = value."""
        if value not in self.bitmaps:
            return []
        return [i for i, bit in enumerate(self.bitmaps[value]) if bit == 1]
    
    def query_or(self, values):
        """WHERE column IN (value1, value2, ...)."""
        result = [0] * self.size
        for value in values:
            if value in self.bitmaps:
                result = [r | b for r, b in zip(result, self.bitmaps[value])]
        return [i for i, bit in enumerate(result) if bit == 1]
    
    def query_and(self, conditions):
        """
        Пересечение двух bitmap индексов.
        Например: WHERE gender = 'M' AND status = 'active'
        """
        result = [1] * self.size
        for bitmap in conditions:
            result = [r & b for r, b in zip(result, bitmap)]
        return [i for i, bit in enumerate(result) if bit == 1]

# Демонстрация
# Данные с низкой кардинальностью

genders = ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F']
statuses = ['active', 'active', 'inactive', 'active', 'inactive', 
            'active', 'active', 'inactive', 'active', 'inactive']

gender_idx = BitmapIndex()
gender_idx.build(genders)

status_idx = BitmapIndex()
status_idx.build(statuses)

print("Исходные данные:")
for i in range(len(genders)):
    print(f"  {i}: gender={genders[i]}, status={statuses[i]}")

print(f"\nWHERE gender = 'M': {gender_idx.query_equals('M')}")
print(f"WHERE status = 'active': {status_idx.query_equals('active')}")

# AND: пересечение bitmaps

male_and_active = gender_idx.query_and([
    gender_idx.bitmaps['M'],
    status_idx.bitmaps['active']
])
print(f"WHERE gender = 'M' AND status = 'active': {male_and_active}")
```

**Output:**
```
Исходные данные:
  0: gender=M, status=active
  1: gender=F, status=active
  2: gender=M, status=inactive
  3: gender=M, status=active
  4: gender=F, status=inactive
  5: gender=F, status=active
  6: gender=M, status=active
  7: gender=F, status=inactive
  8: gender=M, status=active
  9: gender=F, status=inactive

WHERE gender = 'M': [0, 2, 3, 6, 8]
WHERE status = 'active': [0, 1, 3, 5, 6, 8]
WHERE gender = 'M' AND status = 'active': [0, 3, 6, 8]
```

### 5.2 Когда использовать Bitmap Index

- ✅ Колонки с низкой кардинальностью (gender, status, country)
- ✅ Аналитические запросы с AND/OR
- ✅ Data warehouses (OLAP)
- ❌ Высокая кардинальность (email, id)
- ❌ Частые UPDATE/INSERT

---

## 6. Composite Index (составной индекс)

### 6.1 Порядок колонок важен

```python
class CompositeIndex:
    """
    Составной индекс: (country, city, name).
    Порядок колонок критически важен!
    """
    
    def __init__(self):
        self.index = {}  # Вложенный словарь
    
    def insert(self, row_id, country, city, name):
        if country not in self.index:
            self.index[country] = {}
        if city not in self.index[country]:
            self.index[country][city] = {}
        if name not in self.index[country][city]:
            self.index[country][city][name] = []
        self.index[country][city][name].append(row_id)
    
    def query_full(self, country, city, name):
        """WHERE country=X AND city=Y AND name=Z — использует весь индекс."""
        try:
            return self.index[country][city][name]
        except KeyError:
            return []
    
    def query_prefix(self, country, city=None):
        """
        WHERE country=X AND city=Y — использует prefix индекса.
        WHERE country=X — тоже работает!
        """
        results = []
        try:
            if city:
                for name, row_ids in self.index[country][city].items():
                    results.extend(row_ids)
            else:
                for city_data in self.index[country].values():
                    for name, row_ids in city_data.items():
                        results.extend(row_ids)
        except KeyError:
            pass
        return results
    
    def query_skip(self, country, name):
        """
        WHERE country=X AND name=Z — НЕ может использовать индекс полностью!
        Нужно сканировать все города.
        """
        results = []
        try:
            for city_data in self.index[country].values():
                if name in city_data:
                    results.extend(city_data[name])
        except KeyError:
            pass
        return results

# Демонстрация

comp_idx = CompositeIndex()

data = [
    (1, 'USA', 'NYC', 'Alice'),
    (2, 'USA', 'NYC', 'Bob'),
    (3, 'USA', 'LA', 'Alice'),
    (4, 'UK', 'London', 'Alice'),
    (5, 'UK', 'London', 'Carol'),
]

for row_id, country, city, name in data:
    comp_idx.insert(row_id, country, city, name)

print("WHERE country='USA' AND city='NYC' AND name='Alice':")
print(f"  {comp_idx.query_full('USA', 'NYC', 'Alice')}")

print("\nWHERE country='USA' AND city='NYC' (использует prefix):")
print(f"  {comp_idx.query_prefix('USA', 'NYC')}")

print("\nWHERE country='USA' (использует первую колонку):")
print(f"  {comp_idx.query_prefix('USA')}")

print("\nWHERE country='USA' AND name='Alice' (skip city — неэффективно!):")
print(f"  {comp_idx.query_skip('USA', 'Alice')}")
```

**Output:**
```
WHERE country='USA' AND city='NYC' AND name='Alice':
  [1]

WHERE country='USA' AND city='NYC' (использует prefix):
  [1, 2]

WHERE country='USA' (использует первую колонку):
  [1, 2, 3]

WHERE country='USA' AND name='Alice' (skip city — неэффективно!):
  [1, 3]
```

### 6.2 Правила для составных индексов

1. **Leftmost prefix**: индекс используется слева направо
2. **Selectivity first**: ставьте более селективные колонки первыми
3. **Equality before range**: колонки с = перед колонками с < >
4. **Covering index**: включите все колонки из SELECT для Index-Only Scan

---

## 7. Trade-offs индексов

### 7.1 Стоимость индексов

```python
import time
import random

class TableWithMultipleIndexes:
    def __init__(self):
        self.rows = []
        self.indexes = {}
    
    def add_index(self, column_name):
        self.indexes[column_name] = {}
        # Перестроить индекс для существующих данных
        for i, row in enumerate(self.rows):
            key = row[column_name]
            if key not in self.indexes[column_name]:
                self.indexes[column_name][key] = []
            self.indexes[column_name][key].append(i)
    
    def insert(self, row):
        row_id = len(self.rows)
        self.rows.append(row)
        # Обновить все индексы
        for col, index in self.indexes.items():
            key = row[col]
            if key not in index:
                index[key] = []
            index[key].append(row_id)

# Измерение стоимости

table_no_idx = TableWithMultipleIndexes()
table_3_idx = TableWithMultipleIndexes()
table_3_idx.add_index('id')
table_3_idx.add_index('category')
table_3_idx.add_index('status')

n = 10000
categories = ['A', 'B', 'C', 'D', 'E']
statuses = ['active', 'inactive', 'pending']

# Вставка без индексов

start = time.perf_counter()
for i in range(n):
    table_no_idx.insert({
        'id': i,
        'category': random.choice(categories),
        'status': random.choice(statuses),
        'data': f'payload_{i}'
    })
time_no_idx = time.perf_counter() - start

# Вставка с 3 индексами

start = time.perf_counter()
for i in range(n):
    table_3_idx.insert({
        'id': i,
        'category': random.choice(categories),
        'status': random.choice(statuses),
        'data': f'payload_{i}'
    })
time_3_idx = time.perf_counter() - start

print(f"Вставка {n} записей:")
print(f"  Без индексов: {time_no_idx*1000:.1f} мс")
print(f"  С 3 индексами: {time_3_idx*1000:.1f} мс")
print(f"  Замедление: {time_3_idx/time_no_idx:.1f}x")
```

**Output:**
```
Вставка 10000 записей:
  Без индексов: 12.3 мс
  С 3 индексами: 45.6 мс
  Замедление: 3.7x
```

### 7.2 Таблица trade-offs

| Тип индекса | Чтение | Запись | Память | Range | Order |
|-------------|--------|--------|--------|-------|-------|
| B-tree | O(log n) | O(log n) | O(n) | ✅ | ✅ |
| Hash | O(1) | O(1) | O(n) | ❌ | ❌ |
| Bitmap | O(1)* | Дорого | Компактно | ❌ | ❌ |
| Без индекса | O(n) | O(1) | — | — | — |

### 7.3 Когда НЕ использовать индексы

- Маленькие таблицы (< 1000 строк)
- Частые массовые INSERT/UPDATE
- Низкая селективность (много дубликатов)
- Очень широкие ключи

---

## 💡 Key Takeaways

- **B-tree** — универсальный индекс, поддерживает range queries и ORDER BY

- **B+ tree** — модификация B-tree со связанными листьями, быстрее для range scan

- **Hash index** — O(1) для equality, но не поддерживает range

- **Bitmap index** — эффективен для низкой кардинальности и AND/OR

- **Каждый индекс замедляет запись** — выбирайте осознанно

---

## 🚀 Next Steps

**Related Modules:**

- [Write-heavy и read-heavy структуры](../07_Write_Heavy_Read_Heavy/) — LSM-tree и компромиссы
- [Транзакции и структуры данных](../08_Transactions_And_Data_Structures/) — WAL и MVCC

**Practice Ideas:**

1. Используйте EXPLAIN ANALYZE для анализа использования индексов
2. Сравните производительность с разным порядком колонок в составном индексе
3. Измерьте влияние индексов на скорость INSERT

**Going Deeper:**

- Изучите partial indexes (частичные индексы)
- Познакомьтесь с GiST и GIN индексами в PostgreSQL
- Исследуйте covering indexes

---


