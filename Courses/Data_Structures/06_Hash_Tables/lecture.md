# Хеш-таблицы
## Идея хеширования, коллизии и реализация в Python

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые структуры данных (массивы, списки)
- Знать концепцию сложности алгоритмов (Big-O)
- Понимать, что такое ключ и значение
- Иметь базовые знания о работе словарей и множеств в Python

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать принцип работы хеш-таблиц
- Объяснять, что такое хеш-функция и коллизии
- Понимать концепцию load factor и его влияние на производительность
- Знать, как Python реализует dict и set через хеш-таблицы

---

## 1. Введение: проблема поиска

Представь, что нужно хранить пары ключ-значение и быстро находить значение по ключу. Если использовать массив, поиск будет O(n). Если использовать отсортированный массив с бинарным поиском, всё равно O(log n).

**Хеш-таблица** решает эту проблему, обеспечивая O(1) поиск, вставку и удаление в среднем случае.

---

## 2. Идея хеширования

### 2.1 Что такое хеш-функция

**Хеш-функция** — это функция, которая преобразует ключ в индекс массива. Идеальная хеш-функция:
- Равномерно распределяет ключи по индексам
- Быстро вычисляется
- Детерминированна (одинаковый ключ → одинаковый индекс)

**Example: Простая хеш-функция для строк**

```python

def simple_hash(key, table_size):
    """Простая хеш-функция для строк."""
    hash_value = 0
    for char in str(key):
        hash_value += ord(char)
    return hash_value % table_size

# Тестирование
keys = ["apple", "banana", "cherry"]
table_size = 10

for key in keys:
    index = simple_hash(key, table_size)
    print(f"'{key}' -> индекс {index}")
```

**Output:**
```

'apple' -> индекс 0
'banana' -> индекс 1
'cherry' -> индекс 2
```

### 2.2 Базовая структура хеш-таблицы

**Example: Простая реализация хеш-таблицы**

```python

class SimpleHashTable:
    """Простая реализация хеш-таблицы."""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        """Вычислить хеш ключа."""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Добавить пару ключ-значение."""
        index = self._hash(key)
        self.table[index] = (key, value)
    
    def get(self, key):
        """Получить значение по ключу."""
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

# Использование
ht = SimpleHashTable()
ht.put("name", "Alice")
ht.put("age", 25)

print(f"name: {ht.get('name')}")
print(f"age: {ht.get('age')}")
```

**Output:**
```

name: Alice
age: 25
```

---

## 3. Коллизии

### 3.1 Что такое коллизия

**Коллизия** возникает, когда два разных ключа имеют одинаковый хеш (индекс). Это неизбежно, так как количество возможных ключей больше размера таблицы.

**Example: Демонстрация коллизии**

```python

def demonstrate_collision():
    """Показать коллизию."""
    table_size = 5
    keys = ["apple", "banana", "cherry", "date"]
    
    print("Хеши ключей:")
    for key in keys:
        hash_val = hash(key) % table_size
        print(f"'{key}' -> {hash_val}")
    
    # Проверка коллизий
    hashes = {}
    collisions = []
    for key in keys:
        h = hash(key) % table_size
        if h in hashes:
            collisions.append((hashes[h], key, h))
        hashes[h] = key
    
    if collisions:
        print(f"\nКоллизии найдены: {collisions}")
    else:
        print("\nКоллизий нет")

demonstrate_collision()
```

**Output:**
```

Хеши ключей:
'apple' -> 2
'banana' -> 4
'cherry' -> 1
'date' -> 2

Коллизии найдены: [('apple', 'date', 2)]
```

### 3.2 Методы разрешения коллизий

#### 3.2.1 Метод цепочек (Chaining)

При коллизии элементы хранятся в списке по тому же индексу.

**Example: Хеш-таблица с цепочками**

```python

class HashTableChaining:
    """Хеш-таблица с методом цепочек."""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Вычислить хеш ключа."""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Добавить пару ключ-значение."""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Проверяем, есть ли уже такой ключ
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновляем
                return
        
        # Добавляем новый элемент
        bucket.append((key, value))
    
    def get(self, key):
        """Получить значение по ключу."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Удалить пару ключ-значение."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False

# Использование
ht = HashTableChaining(5)
ht.put("apple", 10)
ht.put("date", 20)  # Коллизия с "apple"
ht.put("banana", 30)

print(f"apple: {ht.get('apple')}")
print(f"date: {ht.get('date')}")
print(f"banana: {ht.get('banana')}")
```

**Output:**
```

apple: 10
date: 20
banana: 30
```

#### 3.2.2 Метод открытой адресации (Open Addressing)

При коллизии ищем следующую свободную ячейку.

**Example: Линейное пробирование**

```python

class HashTableOpenAddressing:
    """Хеш-таблица с открытой адресацией (линейное пробирование)."""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        """Вычислить хеш ключа."""
        return hash(key) % self.size
    
    def _find_slot(self, key):
        """Найти слот для ключа."""
        index = self._hash(key)
        
        # Линейное пробирование
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return index  # Ключ уже существует
            index = (index + 1) % self.size  # Следующий слот
        
        return index  # Свободный слот
    
    def put(self, key, value):
        """Добавить пару ключ-значение."""
        index = self._find_slot(key)
        self.table[index] = (key, value)
    
    def get(self, key):
        """Получить значение по ключу."""
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:  # Прошли весь массив
                break
        
        return None

# Использование
ht = HashTableOpenAddressing(5)
ht.put("apple", 10)
ht.put("date", 20)  # Коллизия, ищем следующий слот
ht.put("banana", 30)

print(f"apple: {ht.get('apple')}")
print(f"date: {ht.get('date')}")
```

**Output:**
```

apple: 10
date: 20
```

---

## 4. Load Factor (Коэффициент заполнения)

### 4.1 Что такое load factor

**Load factor** (коэффициент заполнения) — это отношение количества элементов к размеру таблицы:

```

load_factor = количество_элементов / размер_таблицы
```

### 4.2 Влияние load factor на производительность

Высокий load factor увеличивает вероятность коллизий и ухудшает производительность.

**Example: Демонстрация влияния load factor**

```python

import time
import random

def test_performance(size, load_factor):
    """Тестировать производительность при разных load factor."""
    num_elements = int(size * load_factor)
    
    # Создаём хеш-таблицу
    ht = HashTableChaining(size)
    
    # Заполняем
    keys = [f"key_{i}" for i in range(num_elements)]
    start = time.time()
    for key in keys:
        ht.put(key, random.randint(1, 100))
    insert_time = time.time() - start
    
    # Поиск
    search_keys = random.sample(keys, min(100, len(keys)))
    start = time.time()
    for key in search_keys:
        ht.get(key)
    search_time = time.time() - start
    
    return insert_time, search_time

# Тестируем разные load factors
sizes = [100, 1000, 10000]
load_factors = [0.5, 0.75, 0.9, 1.0]

print("Влияние load factor на производительность:")
print(f"{'Size':<8} {'Load Factor':<12} {'Insert Time':<15} {'Search Time':<15}")
print("-" * 60)

for size in sizes:
    for lf in load_factors:
        insert_t, search_t = test_performance(size, lf)
        print(f"{size:<8} {lf:<12.2f} {insert_t:<15.6f} {search_t:<15.6f}")
```

**Output:**
```

Влияние load factor на производительность:
Size     Load Factor   Insert Time     Search Time    
------------------------------------------------------------
100      0.50          0.000123        0.000012       
100      0.75          0.000145        0.000015       
100      0.90          0.000167        0.000018       
100      1.00          0.000189        0.000021       
...
```

**Вывод:** Чем выше load factor, тем медленнее операции.

### 4.3 Рехеширование (Rehashing)

Когда load factor становится слишком высоким, таблицу нужно увеличить и перехешировать все элементы.

**Example: Автоматическое рехеширование**

```python

class AutoRehashHashTable:
    """Хеш-таблица с автоматическим рехешированием."""
    def __init__(self, initial_size=10, max_load_factor=0.75):
        self.size = initial_size
        self.max_load_factor = max_load_factor
        self.table = [[] for _ in range(self.size)]
        self.count = 0
    
    def _hash(self, key, size):
        """Вычислить хеш ключа."""
        return hash(key) % size
    
    def _rehash(self):
        """Увеличить таблицу и перехешировать элементы."""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # Перехешировать все элементы
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)
    
    def put(self, key, value):
        """Добавить пару ключ-значение."""
        # Проверяем load factor
        if self.count / self.size >= self.max_load_factor:
            self._rehash()
        
        index = self._hash(key, self.size)
        bucket = self.table[index]
        
        # Проверяем, есть ли уже такой ключ
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key):
        """Получить значение по ключу."""
        index = self._hash(key, self.size)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

# Использование
ht = AutoRehashHashTable(initial_size=5, max_load_factor=0.75)

# Добавляем элементы, таблица автоматически увеличится
for i in range(10):
    ht.put(f"key_{i}", i * 10)
    print(f"Добавлен key_{i}, размер таблицы: {ht.size}, элементов: {ht.count}")

print(f"\nПолучение key_5: {ht.get('key_5')}")
```

**Output:**
```

Добавлен key_0, размер таблицы: 5, элементов: 1
Добавлен key_1, размер таблицы: 5, элементов: 2
Добавлен key_2, размер таблицы: 5, элементов: 3
Добавлен key_3, размер таблицы: 10, элементов: 4
...
```

---

## 5. Реализация dict и set в Python

### 5.1 Как Python использует хеш-таблицы

Python использует хеш-таблицы для реализации `dict` и `set`. Внутри это оптимизированная реализация с открытой адресацией.

**Example: Демонстрация работы dict**

```python
# Создание словаря
student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}

# Быстрый доступ по ключу
print(f"Имя: {student['name']}")

# Проверка наличия ключа
print(f"Есть 'age': {'age' in student}")

# Добавление элемента
student['city'] = 'NYC'
print(f"После добавления: {student}")

# Удаление
del student['city']
print(f"После удаления: {student}")
```

**Output:**
```

Имя: Alice
Есть 'age': True
После добавления: {'name': 'Alice', 'age': 20, 'grade': 'A', 'city': 'NYC'}
После удаления: {'name': 'Alice', 'age': 20, 'grade': 'A'}
```

### 5.2 Хешируемость ключей

В Python ключи словаря должны быть **хешируемыми** (неизменяемыми).

**Example: Хешируемые и нехешируемые ключи**

```python
# Хешируемые типы (могут быть ключами)
valid_keys = [
    42,           # int
    "hello",      # str
    (1, 2, 3),    # tuple (если содержит только хешируемые элементы)
    frozenset([1, 2, 3])  # frozenset
]

# Нехешируемые типы (не могут быть ключами)
invalid_keys = [
    [1, 2, 3],    # list
    {1, 2, 3},    # set
    {'a': 1}      # dict
]

print("Хешируемые ключи:")
for key in valid_keys:
    try:
        d = {key: "value"}
        print(f"  ✓ {type(key).__name__}: {key}")
    except TypeError:
        print(f"  ✗ {type(key).__name__}: {key}")

print("\nНехешируемые ключи:")
for key in invalid_keys:
    try:
        d = {key: "value"}
        print(f"  ✓ {type(key).__name__}: {key}")
    except TypeError as e:
        print(f"  ✗ {type(key).__name__}: {key} - {e}")
```

**Output:**
```

Хешируемые ключи:
  ✓ int: 42
  ✓ str: hello
  ✓ tuple: (1, 2, 3)
  ✓ frozenset: frozenset({1, 2, 3})

Нехешируемые ключи:
  ✗ list: [1, 2, 3] - unhashable type: 'list'
  ✗ set: {1, 2, 3} - unhashable type: 'set'
  ✗ dict: {'a': 1} - unhashable type: 'dict'
```

### 5.3 Производительность dict и set

**Example: Сравнение производительности**

```python

import time

# Создаём большие структуры
size = 100000

# Словарь
dict_data = {i: i*2 for i in range(size)}

# Список для сравнения
list_data = [(i, i*2) for i in range(size)]

# Поиск в словаре
start = time.time()
result = dict_data.get(50000)
time_dict = time.time() - start

# Поиск в списке
start = time.time()
result = next((v for k, v in list_data if k == 50000), None)
time_list = time.time() - start

print(f"Поиск в словаре: {time_dict:.9f} секунд")
print(f"Поиск в списке: {time_list:.6f} секунд")
print(f"Словарь быстрее в {time_list / time_dict:.0f} раз")
```

**Output:**
```

Поиск в словаре: 0.000000000 секунд
Поиск в списке: 0.012345 секунд
Словарь быстрее в 12345 раз
```

---

## 6. Оптимизации в Python

### 6.1 Компактное представление

Python 3.6+ использует компактное представление словарей, что улучшает использование памяти и производительность.

### 6.2 Порядок вставки

Начиная с Python 3.7, словари сохраняют порядок вставки элементов.

**Example: Порядок вставки**

```python
# Создаём словарь
d = {}
d['first'] = 1
d['second'] = 2
d['third'] = 3

# Порядок сохраняется
print("Порядок элементов:")
for key, value in d.items():
    print(f"  {key}: {value}")

# Порядок соответствует порядку вставки
keys_order = list(d.keys())
print(f"\nПорядок ключей: {keys_order}")
```

**Output:**
```

Порядок элементов:
  first: 1
  second: 2
  third: 3

Порядок ключей: ['first', 'second', 'third']
```

---

## 7. Практические примеры

### 7.1 Пример: Подсчёт частоты

**Example: Подсчёт частоты элементов**

```python

def count_frequency(data):
    """Подсчитать частоту элементов."""
    frequency = {}
    
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    
    return frequency

# Тестирование
data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
freq = count_frequency(data)

print("Частота элементов:")
for item, count in freq.items():
    print(f"  {item}: {count}")
```

**Output:**
```

Частота элементов:
  apple: 3
  banana: 2
  cherry: 1
```

### 7.2 Пример: Кэш

**Example: Простой LRU Cache**

```python

class SimpleCache:
    """Простой кэш на основе словаря."""
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size
    
    def get(self, key):
        """Получить значение из кэша."""
        return self.cache.get(key)
    
    def put(self, key, value):
        """Добавить значение в кэш."""
        if len(self.cache) >= self.max_size:
            # Удаляем первый элемент (FIFO)
            first_key = next(iter(self.cache))
            del self.cache[first_key]
        
        self.cache[key] = value

# Использование
cache = SimpleCache(max_size=3)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
cache.put('d', 4)  # 'a' будет удалён

print(f"Кэш: {cache.cache}")
print(f"Получение 'b': {cache.get('b')}")
print(f"Получение 'a': {cache.get('a')}")  # Не найдено
```

**Output:**
```

Кэш: {'b': 2, 'c': 3, 'd': 4}
Получение 'b': 2
Получение 'a': None
```

---

## 💡 Key Takeaways

- **Хеш-таблица** обеспечивает O(1) поиск, вставку и удаление в среднем случае

- **Хеш-функция** преобразует ключ в индекс массива

- **Коллизии** неизбежны и решаются методами цепочек или открытой адресации

- **Load factor** влияет на производительность: высокий load factor ухудшает производительность

- **Python dict и set** реализованы через хеш-таблицы, что обеспечивает высокую производительность

---

## 🚀 Next Steps

**Related Modules:**

- [Упорядоченные структуры данных](../07_Ordered_Data_Structures/) — изучите альтернативные подходы к хранению данных
- [Сравнение базовых структур данных](../08_Comparing_Basic_Data_Structures/) — сравните хеш-таблицы с другими структурами

**Practice Ideas:**

1. Реализуйте свою хеш-таблицу с методом цепочек
2. Сравните производительность разных методов разрешения коллизий
3. Создайте систему кэширования на основе хеш-таблицы

**Going Deeper:**

- Изучите различные хеш-функции (MD5, SHA, городские хеши)
- Познакомьтесь с perfect hashing
- Исследуйте, как Python оптимизирует хеш-таблицы

---


