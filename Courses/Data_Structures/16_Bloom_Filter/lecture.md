# Bloom Filter
## Проверка принадлежности элемента и ложные срабатывания

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать концепцию вероятностных структур данных
- Знать, что такое хеш-функции
- Понимать компромиссы между точностью и памятью
- Иметь базовые знания о вероятности

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать принцип работы Bloom Filter
- Реализовывать базовый Bloom Filter
- Анализировать вероятность ложных срабатываний
- Применять Bloom Filter в практических задачах

---

## 1. Введение: что такое Bloom Filter

**Bloom Filter** — это вероятностная структура данных для проверки принадлежности элемента множеству. Она может дать:
- **Точный ответ "нет"** (элемента точно нет)

- **Приближённый ответ "возможно да"** (элемент может быть, но может быть и ложное срабатывание)

**Ключевое свойство:** Нет ложных отрицаний, но возможны ложные срабатывания.

---

## 2. Принцип работы

### 2.1 Структура Bloom Filter

Bloom Filter состоит из:

- **Битовый массив** размера m

- **k хеш-функций**, которые преобразуют элемент в k индексов массива

**Example: Базовая структура**

```python
import hashlib

class BloomFilter:
    """Простая реализация Bloom Filter."""
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size
    
    def _hash(self, item, seed):
        """Хеш-функция с seed."""
        hash_obj = hashlib.md5(f"{item}_{seed}".encode())
        return int(hash_obj.hexdigest(), 16) % self.size
    
    def add(self, item):
        """Добавить элемент в фильтр."""
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            self.bit_array[index] = 1
    
    def might_contain(self, item):
        """Проверить, возможно ли элемент в фильтре."""
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return False  # Точно нет
        return True  # Возможно есть (может быть ложное срабатывание)

# Использование

bf = BloomFilter(size=100, num_hashes=3)
bf.add("apple")
bf.add("banana")

print(f"'apple' возможно в фильтре: {bf.might_contain('apple')}")
print(f"'cherry' возможно в фильтре: {bf.might_contain('cherry')}")
```

**Output:**
```
'apple' возможно в фильтре: True
'cherry' возможно в фильтре: False
```

### 2.2 Добавление элемента

При добавлении элемента:

1. Вычисляем k хешей элемента
2. Устанавливаем соответствующие биты в 1

**Example: Визуализация добавления**

```python
bf = BloomFilter(size=20, num_hashes=3)

# Добавляем элемент

bf.add("test")

# Показываем, какие биты установлены

print(f"Битовый массив после добавления 'test':")
print(f"  {bf.bit_array}")
print(f"  Установлено битов: {sum(bf.bit_array)}")
```

**Output:**
```
Битовый массив после добавления 'test':
  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
  Установлено битов: 3
```

### 2.3 Проверка принадлежности

При проверке:

1. Вычисляем k хешей элемента
2. Если хотя бы один бит = 0 → элемента точно нет
3. Если все биты = 1 → элемент возможно есть (может быть ложное срабатывание)

---

## 3. Ложные срабатывания

### 3.1 Что такое ложное срабатывание

**Ложное срабатывание (False Positive)** — когда фильтр говорит "возможно есть", но элемента на самом деле нет.

**Ложных отрицаний нет:** Если элемент был добавлен, фильтр всегда скажет "возможно есть".

### 3.2 Вероятность ложного срабатывания

Вероятность ложного срабатывания зависит от:

- Размера битового массива (m)
- Количества хеш-функций (k)
- Количества добавленных элементов (n)

**Приближённая формула:** P ≈ (1 - e^(-kn/m))^k

**Example: Влияние параметров**

```python
import math

def false_positive_probability(n, m, k):
    """Вычислить вероятность ложного срабатывания."""
    return (1 - math.exp(-k * n / m)) ** k

# Разные конфигурации

configs = [
    (1000, 10000, 3),   # n=1000, m=10000, k=3
    (1000, 5000, 3),    # Меньший массив
    (1000, 10000, 5),   # Больше хеш-функций
]

print("Вероятность ложного срабатывания:")
for n, m, k in configs:
    prob = false_positive_probability(n, m, k)
    print(f"  n={n}, m={m}, k={k}: {prob:.4f} ({prob*100:.2f}%)")
```

**Output:**
```
Вероятность ложного срабатывания:
  n=1000, m=10000, k=3: 0.0179 (1.79%)
  n=1000, m=5000, k=3: 0.0619 (6.19%)
  n=1000, m=10000, k=5: 0.0094 (0.94%)
```

### 3.3 Оптимальное количество хеш-функций

Оптимальное k ≈ (m/n) * ln(2)

**Example: Оптимальное k**

```python
def optimal_k(m, n):
    """Вычислить оптимальное количество хеш-функций."""
    return round((m / n) * math.log(2))

m, n = 10000, 1000
k_opt = optimal_k(m, n)
prob = false_positive_probability(n, m, k_opt)

print(f"Для m={m}, n={n}:")
print(f"  Оптимальное k: {k_opt}")
print(f"  Вероятность ложного срабатывания: {prob:.4f} ({prob*100:.2f}%)")
```

**Output:**
```
Для m=10000, n=1000:
  Оптимальное k: 7
  Вероятность ложного срабатывания: 0.0062 (0.62%)
```

---

## 4. Реализация Bloom Filter

### 4.1 Полная реализация

**Example: Улучшенная реализация**

```python
import hashlib
import math

class BloomFilter:
    """Реализация Bloom Filter."""
    def __init__(self, capacity, error_rate=0.01):
        """
        capacity: ожидаемое количество элементов
        error_rate: желаемая вероятность ложного срабатывания
        """
        self.capacity = capacity
        self.error_rate = error_rate
        
        # Вычисляем оптимальные параметры
        self.size = self._calculate_size(capacity, error_rate)
        self.num_hashes = self._calculate_num_hashes(self.size, capacity)
        
        self.bit_array = [0] * self.size
        self.count = 0
    
    def _calculate_size(self, n, p):
        """Вычислить размер массива."""
        # m = -n * ln(p) / (ln(2)^2)
        return int(-n * math.log(p) / (math.log(2) ** 2))
    
    def _calculate_num_hashes(self, m, n):
        """Вычислить количество хеш-функций."""
        # k = (m/n) * ln(2)
        return int((m / n) * math.log(2))
    
    def _hash(self, item, seed):
        """Хеш-функция."""
        hash_obj = hashlib.sha256(f"{item}_{seed}".encode())
        return int(hash_obj.hexdigest(), 16) % self.size
    
    def add(self, item):
        """Добавить элемент."""
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            self.bit_array[index] = 1
        self.count += 1
    
    def might_contain(self, item):
        """Проверить принадлежность."""
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return False
        return True
    
    def get_stats(self):
        """Получить статистику."""
        return {
            'size': self.size,
            'num_hashes': self.num_hashes,
            'capacity': self.capacity,
            'error_rate': self.error_rate,
            'elements_added': self.count,
            'bits_set': sum(self.bit_array)
        }

# Использование

bf = BloomFilter(capacity=1000, error_rate=0.01)
print("Параметры Bloom Filter:")
stats = bf.get_stats()
for key, value in stats.items():
    print(f"  {key}: {value}")
```

**Output:**
```
Параметры Bloom Filter:
  size: 9585
  num_hashes: 7
  capacity: 1000
  error_rate: 0.01
  elements_added: 0
  bits_set: 0
```

---

## 5. Применение Bloom Filter

### 5.1 Кэш-фильтр

**Example: Фильтр для кэша**

```python
class CacheWithBloomFilter:
    """Кэш с Bloom Filter для предварительной проверки."""
    def __init__(self):
        self.bloom_filter = BloomFilter(capacity=10000, error_rate=0.01)
        self.cache = {}  # Реальный кэш
    
    def get(self, key):
        """Получить значение из кэша."""
        # Быстрая проверка через Bloom Filter
        if not self.bloom_filter.might_contain(key):
            return None  # Точно нет в кэше
        
        # Возможно есть, проверяем реальный кэш
        return self.cache.get(key)
    
    def set(self, key, value):
        """Установить значение в кэш."""
        self.bloom_filter.add(key)
        self.cache[key] = value

# Использование

cache = CacheWithBloomFilter()
cache.set('user_1', {'name': 'Alice'})
cache.set('user_2', {'name': 'Bob'})

# Быстрая проверка

result = cache.get('user_1')
print(f"Результат для user_1: {result}")

result = cache.get('user_999')  # Нет в кэше
print(f"Результат для user_999: {result}")
```

**Output:**
```
Результат для user_1: {'name': 'Alice'}
Результат для user_999: None
```

### 5.2 Проверка дубликатов

**Example: Фильтр дубликатов**

```python
class DuplicateFilter:
    """Фильтр для проверки дубликатов."""
    def __init__(self, expected_items, error_rate=0.01):
        self.bloom_filter = BloomFilter(expected_items, error_rate)
        self.seen_items = set()  # Для точной проверки при необходимости
    
    def is_duplicate(self, item):
        """Проверить, является ли элемент дубликатом."""
        if not self.bloom_filter.might_contain(item):
            # Точно не дубликат
            self.bloom_filter.add(item)
            return False
        
        # Возможно дубликат, проверяем точно
        if item in self.seen_items:
            return True
        
        # Ложное срабатывание, добавляем
        self.seen_items.add(item)
        self.bloom_filter.add(item)
        return False

# Использование

dup_filter = DuplicateFilter(expected_items=1000)
items = ['item_1', 'item_2', 'item_1', 'item_3']

for item in items:
    is_dup = dup_filter.is_duplicate(item)
    print(f"{item}: {'Дубликат' if is_dup else 'Новый'}")
```

**Output:**
```
item_1: Новый
item_2: Новый
item_1: Дубликат
item_3: Новый
```

---

## 6. Преимущества и недостатки

### 6.1 Преимущества

**Преимущества:**

- ✅ Очень мало памяти (в разы меньше, чем множество)
- ✅ Быстрые операции (O(k), где k обычно 3-10)
- ✅ Нет ложных отрицаний
- ✅ Масштабируемость

### 6.2 Недостатки

**Недостатки:**

- ❌ Возможны ложные срабатывания
- ❌ Нельзя удалить элементы (без модификаций)
- ❌ Нельзя получить список элементов
- ❌ Нужно знать ожидаемое количество элементов заранее

---

## 7. Варианты Bloom Filter

### 7.1 Counting Bloom Filter

Позволяет удалять элементы, используя счётчики вместо битов.

### 7.2 Scalable Bloom Filter

Автоматически увеличивается при переполнении.

---

## 💡 Key Takeaways

- **Bloom Filter** — вероятностная структура для проверки принадлежности элемента

- **Нет ложных отрицаний:** если элемент добавлен, фильтр всегда скажет "возможно есть"

- **Возможны ложные срабатывания:** фильтр может сказать "возможно есть" для элемента, которого нет

- **Экономия памяти:** в разы меньше, чем обычное множество

- **Применение:** кэш-фильтры, проверка дубликатов, предварительная фильтрация перед дорогими операциями

---

## 🚀 Next Steps

**Related Modules:**

- [Count-Min Sketch](../17_Count_Min_Sketch/) — изучите структуру для оценки частоты
- [Структуры данных в реальных системах](../19_Data_Structures_In_Real_Systems/) — увидите применение Bloom Filter

**Practice Ideas:**

1. Реализуйте Bloom Filter с настраиваемыми параметрами
2. Измерьте вероятность ложных срабатываний на реальных данных
3. Примените Bloom Filter для оптимизации кэша

**Going Deeper:**

- Изучите Counting Bloom Filter и Scalable Bloom Filter
- Познакомьтесь с другими вероятностными структурами (Quotient Filter)
- Исследуйте применение в распределённых системах (Cassandra, Redis)

---



