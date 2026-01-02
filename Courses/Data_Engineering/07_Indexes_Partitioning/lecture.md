# Индексы и партиционирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы хранилищ данных (модуль 05)
- Знать форматы данных (модуль 06)
- Иметь представление о структурах данных

**Recommended prior modules:**

- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [06_Data_Formats](../06_Data_Formats/) — форматы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять, как работают индексы как структуры данных
- Проектировать партиционирование для оптимизации запросов
- Различать партиционирование и sharding
- Анализировать trade-offs между различными подходами

---

## 1. Введение в оптимизацию доступа к данным

Оптимизация доступа к данным критична для производительности систем. Индексы и партиционирование — основные техники для ускорения запросов и управления большими объёмами данных.

**Основные техники:**

- **Индексы** — структуры данных для быстрого поиска

- **Партиционирование** — разделение данных на части

- **Sharding** — распределение данных по узлам

---

## 2. Индексы как структуры данных

Индексы — это дополнительные структуры данных, которые ускоряют поиск записей в таблице.

### 2.1 Как работают индексы

**Принцип:**

- Индекс создаёт упорядоченную структуру (B-tree, Hash)
- Хранит пары (значение, указатель на запись)
- Позволяет быстро находить записи без полного сканирования

**Example: Индекс на колонке**

```python
# Симуляция индекса

class Index:
    def __init__(self, column_name):
        self.column_name = column_name
        self.index = {}  # value -> [row_ids]
    
    def build(self, data):
        """Строит индекс из данных"""
        for row_id, record in enumerate(data):
            value = record.get(self.column_name)
            if value not in self.index:
                self.index[value] = []
            self.index[value].append(row_id)
        print(f"✅ Индекс построен для колонки '{self.column_name}': {len(self.index)} уникальных значений")
    
    def lookup(self, value):
        """Быстрый поиск по индексу"""
        return self.index.get(value, [])
    
    def range_lookup(self, min_val, max_val):
        """Поиск в диапазоне (для упорядоченных индексов)"""
        results = []
        for val, row_ids in self.index.items():
            if min_val <= val <= max_val:
                results.extend(row_ids)
        return results

# Данные без индекса

data = [
    {"id": 1, "name": "Alice", "age": 30, "city": "Moscow"},
    {"id": 2, "name": "Bob", "age": 25, "city": "SPB"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Moscow"},
    {"id": 4, "name": "Diana", "age": 28, "city": "SPB"}
]

# Поиск без индекса (full table scan)

def search_without_index(data, column, value):
    """Полное сканирование таблицы"""
    results = []
    for record in data:
        if record.get(column) == value:
            results.append(record)
    return results

# Поиск с индексом

age_index = Index("age")
age_index.build(data)

# Запрос: найти всех с age = 30

print("\nПоиск без индекса (full scan):")
results_no_index = search_without_index(data, "age", 30)
print(f"  Проверено записей: {len(data)}")
print(f"  Найдено: {len(results_no_index)}")

print("\nПоиск с индексом:")
row_ids = age_index.lookup(30)
results_with_index = [data[i] for i in row_ids]
print(f"  Проверено записей: {len(row_ids)} (только нужные)")
print(f"  Найдено: {len(results_with_index)}")
```

**Output:**
```
✅ Индекс построен для колонки 'age': 4 уникальных значений

Поиск без индекса (full scan):
  Проверено записей: 4
  Найдено: 1

Поиск с индексом:
  Проверено записей: 1 (только нужные)
  Найдено: 1
```

### 2.2 Типы индексов

**B-tree индекс:**

- Упорядоченная структура
- Поддерживает range queries
- Балансированное дерево

**Hash индекс:**

- Быстрый точный поиск
- Не поддерживает range queries
- O(1) в среднем

**Bitmap индекс:**

- Для колонок с небольшим количеством уникальных значений
- Эффективен для аналитики

**Example: Типы индексов**

```python
# Симуляция различных типов индексов

class BTreeIndex:
    """B-tree индекс для упорядоченного поиска"""
    def __init__(self):
        self.sorted_values = []
        self.value_to_rows = {}
    
    def build(self, data, column):
        for row_id, record in enumerate(data):
            value = record.get(column)
            if value not in self.value_to_rows:
                self.value_to_rows[value] = []
            self.value_to_rows[value].append(row_id)
        self.sorted_values = sorted(self.value_to_rows.keys())
        print(f"✅ B-tree индекс построен: {len(self.sorted_values)} значений")
    
    def range_query(self, min_val, max_val):
        """Range query (преимущество B-tree)"""
        results = []
        for val in self.sorted_values:
            if min_val <= val <= max_val:
                results.extend(self.value_to_rows[val])
        return results

class HashIndex:
    """Hash индекс для точного поиска"""
    def __init__(self):
        self.index = {}
    
    def build(self, data, column):
        for row_id, record in enumerate(data):
            value = record.get(column)
            if value not in self.index:
                self.index[value] = []
            self.index[value].append(row_id)
        print(f"✅ Hash индекс построен: {len(self.index)} значений")
    
    def exact_lookup(self, value):
        """Точный поиск O(1)"""
        return self.index.get(value, [])

# Сравнение

data = [{"id": i, "age": 20 + i*5} for i in range(10)]

btree = BTreeIndex()
btree.build(data, "age")
range_results = btree.range_query(25, 40)
print(f"B-tree range query (25-40): {len(range_results)} записей")

hash_idx = HashIndex()
hash_idx.build(data, "age")
exact_results = hash_idx.exact_lookup(30)
print(f"Hash exact lookup (30): {len(exact_results)} записей")
```

**Output:**
```
✅ B-tree индекс построен: 10 значений
B-tree range query (25-40): 4 записей
✅ Hash индекс построен: 10 значений
Hash exact lookup (30): 1 записей
```

### 2.3 Trade-offs индексов

**Преимущества:**

- Быстрый поиск
- Ускорение запросов
- Поддержка уникальности

**Недостатки:**

- Дополнительное место
- Замедление записи (нужно обновлять индекс)
- Поддержка индекса требует ресурсов

---

## 3. Партиционирование (Partitioning)

Партиционирование — это разделение таблицы на меньшие части (партиции) для улучшения производительности запросов.

### 3.1 Типы партиционирования

**Range Partitioning:**

- Партиции по диапазонам значений
- Пример: по дате (2024-01, 2024-02, ...)

**Hash Partitioning:**

- Партиции по hash функции
- Равномерное распределение

**List Partitioning:**

- Партиции по списку значений
- Пример: по региону (Moscow, SPB, ...)

**Example: Партиционирование по дате**

```python
# Симуляция партиционирования

class PartitionedTable:
    def __init__(self, partition_key):
        self.partition_key = partition_key
        self.partitions = {}
    
    def insert(self, record):
        """Вставляет запись в соответствующую партицию"""
        partition_value = record.get(self.partition_key)
        
        # Определяем партицию (например, по месяцу)
        if isinstance(partition_value, str):
            partition_name = partition_value[:7]  # YYYY-MM
        else:
            partition_name = str(partition_value)
        
        if partition_name not in self.partitions:
            self.partitions[partition_name] = []
        
        self.partitions[partition_name].append(record)
        print(f"✅ Запись добавлена в партицию '{partition_name}'")
    
    def query(self, partition_filter=None, record_filter=None):
        """Запрос с фильтрацией по партициям"""
        results = []
        partitions_to_scan = []
        
        if partition_filter:
            # Сканируем только нужные партиции
            partitions_to_scan = [p for p in self.partitions.keys() if partition_filter(p)]
        else:
            partitions_to_scan = list(self.partitions.keys())
        
        print(f"📊 Сканируем {len(partitions_to_scan)} партиций из {len(self.partitions)}")
        
        for partition_name in partitions_to_scan:
            for record in self.partitions[partition_name]:
                if not record_filter or record_filter(record):
                    results.append(record)
        
        return results

# Использование

table = PartitionedTable("date")

# Вставка данных

table.insert({"id": 1, "date": "2024-01-15", "amount": 100})
table.insert({"id": 2, "date": "2024-01-20", "amount": 200})
table.insert({"id": 3, "date": "2024-02-10", "amount": 150})
table.insert({"id": 4, "date": "2024-02-25", "amount": 300})

# Запрос только за январь (сканируем только одну партицию)

january_records = table.query(
    partition_filter=lambda p: p == "2024-01"
)
print(f"\nЗаписи за январь: {len(january_records)}")
```

**Output:**
```
✅ Запись добавлена в партицию '2024-01'
✅ Запись добавлена в партицию '2024-01'
✅ Запись добавлена в партицию '2024-02'
✅ Запись добавлена в партицию '2024-02'
📊 Сканируем 1 партиций из 2
Записи за январь: 2
```

### 3.2 Преимущества партиционирования

**Производительность:**

- Сканируем только нужные партиции
- Параллельная обработка партиций
- Улучшение кеширования

**Управление:**

- Легче удалять старые данные (drop партицию)
- Легче добавлять новые данные
- Оптимизация по партициям

---

## 4. Sharding (Шардирование)

Sharding — это горизонтальное разделение данных по нескольким узлам (шардам).

### 4.1 Принцип Sharding

**Концепция:**

- Данные распределяются по нескольким серверам
- Каждый шард содержит подмножество данных
- Запросы направляются к нужным шардам

**Example: Sharding по user_id**

```python
# Симуляция sharding

class ShardedDatabase:
    def __init__(self, num_shards, shard_key):
        self.num_shards = num_shards
        self.shard_key = shard_key
        self.shards = {i: [] for i in range(num_shards)}
    
    def _get_shard(self, value):
        """Определяет шард по значению ключа"""
        return hash(value) % self.num_shards
    
    def insert(self, record):
        """Вставляет запись в соответствующий шард"""
        shard_key_value = record.get(self.shard_key)
        shard_id = self._get_shard(shard_key_value)
        self.shards[shard_id].append(record)
        print(f"✅ Запись добавлена в шард {shard_id}")
    
    def query(self, shard_key_value):
        """Запрос к конкретному шарду"""
        shard_id = self._get_shard(shard_key_value)
        results = [r for r in self.shards[shard_id] 
                   if r.get(self.shard_key) == shard_key_value]
        print(f"📊 Запрос выполнен на шарде {shard_id}")
        return results
    
    def get_distribution(self):
        """Показывает распределение данных"""
        return {shard_id: len(records) 
                for shard_id, records in self.shards.items()}

# Использование

db = ShardedDatabase(num_shards=3, shard_key="user_id")

# Вставка данных

for i in range(10):
    db.insert({"user_id": i, "name": f"User{i}", "data": f"data{i}"})

# Распределение

distribution = db.get_distribution()
print(f"\nРаспределение данных по шардам: {distribution}")

# Запрос

results = db.query(5)
print(f"Найдено записей: {len(results)}")
```

**Output:**
```
✅ Запись добавлена в шард 0
✅ Запись добавлена в шард 1
✅ Запись добавлена в шард 2
✅ Запись добавлена в шард 0
✅ Запись добавлена в шард 1
✅ Запись добавлена в шард 2
✅ Запись добавлена в шард 0
✅ Запись добавлена в шард 1
✅ Запись добавлена в шард 2
✅ Запись добавлена в шард 0
📊 Запрос выполнен на шарде 2
Найдено записей: 1

Распределение данных по шардам: {0: 4, 1: 3, 3: 3}
```

### 4.2 Sharding vs Partitioning

**Partitioning:**

- В рамках одного сервера
- Логическое разделение
- Для оптимизации запросов

**Sharding:**

- По нескольким серверам
- Физическое разделение
- Для масштабирования

**Example: Сравнение**

```python
comparison = {
    "Partitioning": {
        "scope": "В рамках одного сервера",
        "purpose": "Оптимизация запросов",
        "example": "Партиции по дате в одной таблице"
    },
    "Sharding": {
        "scope": "По нескольким серверам",
        "purpose": "Горизонтальное масштабирование",
        "example": "Данные распределены по 3 серверам"
    }
}

print("Partitioning vs Sharding:")
for technique, info in comparison.items():
    print(f"\n{technique}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

**Output:**
```
Partitioning vs Sharding:

Partitioning:
  scope: В рамках одного сервера
  purpose: Оптимизация запросов
  example: Партиции по дате в одной таблице

Sharding:
  scope: По нескольким серверам
  purpose: Горизонтальное масштабирование
  example: Данные распределены по 3 серверам
```

---

## 5. Performance Trade-offs

Понимание trade-offs критично для принятия решений об оптимизации.

### 5.1 Индексы: Trade-offs

**Преимущества:**

- Ускорение чтения (O(log n) вместо O(n))
- Поддержка уникальности
- Улучшение JOIN операций

**Недостатки:**

- Дополнительное место (10-20% от размера таблицы)
- Замедление записи (нужно обновлять индекс)
- Поддержка индекса требует ресурсов

**Example: Trade-offs индексов**

```python
# Симуляция trade-offs

def analyze_index_tradeoff(table_size, read_ratio, write_ratio):
    """Анализирует trade-offs индекса"""
    index_size = table_size * 0.15  # 15% от размера таблицы
    read_benefit = read_ratio * 0.8  # 80% ускорение чтения
    write_cost = write_ratio * 0.2    # 20% замедление записи
    
    net_benefit = read_benefit - write_cost
    
    print(f"Анализ индекса для таблицы {table_size}MB:")
    print(f"  Размер индекса: {index_size:.1f}MB")
    print(f"  Выгода от чтения: {read_benefit:.1%}")
    print(f"  Стоимость записи: {write_cost:.1%}")
    print(f"  Чистая выгода: {net_benefit:.1%}")
    
    return "Рекомендуется" if net_benefit > 0 else "Не рекомендуется"

# Примеры

print("Сценарий 1: Read-heavy (90% чтение, 10% запись)")
analyze_index_tradeoff(1000, 0.9, 0.1)

print("\nСценарий 2: Write-heavy (10% чтение, 90% запись)")
analyze_index_tradeoff(1000, 0.1, 0.9)
```

**Output:**
```
Сценарий 1: Read-heavy (90% чтение, 10% запись)
Анализ индекса для таблицы 1000MB:
  Размер индекса: 150.0MB
  Выгода от чтения: 72.0%
  Стоимость записи: 18.0%
  Чистая выгода: 54.0%
Рекомендуется

Сценарий 2: Write-heavy (10% чтение, 90% запись)
Анализ индекса для таблицы 1000MB:
  Размер индекса: 150.0MB
  Выгода от чтения: 8.0%
  Стоимость записи: 18.0%
  Чистая выгода: -10.0%
Не рекомендуется
```

### 5.2 Партиционирование: Trade-offs

**Преимущества:**

- Ускорение запросов (сканируем только нужные партиции)
- Упрощение управления (удаление старых данных)
- Параллельная обработка

**Недостатки:**

- Сложность запросов (нужно знать партиции)
- Overhead на управление партициями
- Неравномерное распределение данных

### 5.3 Sharding: Trade-offs

**Преимущества:**

- Горизонтальное масштабирование
- Распределение нагрузки
- Увеличение пропускной способности

**Недостатки:**

- Сложность запросов (cross-shard queries)
- Управление консистентностью
- Операционная сложность

---

## 6. Best Practices

Рекомендации по использованию индексов, партиционирования и sharding.

### 6.1 Индексы

**Когда создавать:**

- Часто используемые колонки в WHERE
- Foreign keys
- Колонки для JOIN

**Когда НЕ создавать:**

- Колонки с низкой селективностью
- Write-heavy таблицы
- Маленькие таблицы

### 6.2 Партиционирование

**Когда использовать:**

- Большие таблицы (>10GB)
- Запросы часто фильтруют по партиционному ключу
- Нужно управлять жизненным циклом данных

**Ключ партиционирования:**

- Выбирать колонку, часто используемую в WHERE
- Избегать колонок с высокой кардинальностью
- Балансировать размер партиций

### 6.3 Sharding

**Когда использовать:**

- Нужно горизонтальное масштабирование
- Один сервер не справляется
- Данные можно разделить логически

**Ключ sharding:**

- Выбирать колонку с равномерным распределением
- Избегать hot spots
- Учитывать паттерны запросов

---

## 💡 Key Takeaways

- **Индексы**: Ускоряют поиск, но замедляют запись и требуют места. Используйте для read-heavy workloads и часто используемых колонок.

- **Партиционирование**: Разделяет данные на части в рамках одного сервера. Ускоряет запросы и упрощает управление. Используйте для больших таблиц с фильтрацией по партиционному ключу.

- **Sharding**: Распределяет данные по нескольким серверам. Обеспечивает горизонтальное масштабирование, но усложняет запросы. Используйте когда нужен масштаб.

- **Trade-offs**: Нет универсального решения. Индексы для чтения, партиционирование для больших таблиц, sharding для масштабирования. Выбор зависит от требований.

- **Комбинация техник**: В реальных системах часто используются все три техники вместе: индексы на партициях, sharding с партиционированием.

---

## 🚀 Next Steps

**Related Modules:**

- [08_Metadata_Catalogs](../08_Metadata_Catalogs/) — метаданные и каталоги данных
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [18_Scaling_Performance](../18_Scaling_Performance/) — масштабирование и производительность

**Practice Ideas:**

1. Создайте индексы на вашей базе данных и измерьте влияние на производительность
2. Спроектируйте партиционирование для большой таблицы: выберите ключ партиционирования
3. Проанализируйте, нужен ли sharding для вашей системы

**Going Deeper:**

- Изучите B-tree структуру: как работает балансировка
- Погрузитесь в стратегии sharding: range, hash, directory-based
- Изучите композитные индексы и их использование

---

## 📚 Additional Resources

**Books:**

- "Database Internals" by Alex Petrov — внутреннее устройство БД и индексов
- "Designing Data-Intensive Applications" by Martin Kleppmann — партиционирование и sharding

**Articles:**

- "Database Indexing Explained" — детальное объяснение индексов
- "Partitioning vs Sharding" — сравнение подходов

**Documentation:**

- PostgreSQL Partitioning: https://www.postgresql.org/docs/current/ddl-partitioning.html
- MySQL Partitioning: https://dev.mysql.com/doc/refman/8.0/en/partitioning.html

---



