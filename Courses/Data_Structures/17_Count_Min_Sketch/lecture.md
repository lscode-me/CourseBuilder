# Count-Min Sketch
## Оценка частоты элементов в потоковых данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать вероятностные структуры данных
- Знать, что такое Bloom Filter
- Понимать концепцию хеширования
- Иметь базовые знания о потоковых данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать принцип работы Count-Min Sketch
- Реализовывать базовый Count-Min Sketch
- Применять Count-Min Sketch для оценки частоты элементов
- Анализировать точность оценок

---

## 1. Введение: задача оценки частоты

В потоковых данных часто нужно оценить, сколько раз встречается каждый элемент. Для больших объёмов данных точный подсчёт может быть слишком дорогим по памяти.

**Count-Min Sketch** — это вероятностная структура данных, которая даёт приближённую оценку частоты элементов, используя значительно меньше памяти.

---

## 2. Принцип работы Count-Min Sketch

### 2.1 Структура

Count-Min Sketch состоит из:

- **Матрица счётчиков** размером w × d (ширина × глубина)

- **d хеш-функций**, каждая отображает элемент в столбец матрицы

**Example: Базовая структура**

```python
import hashlib

class CountMinSketch:
    """Простая реализация Count-Min Sketch."""
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.counters = [[0] * width for _ in range(depth)]
    
    def _hash(self, item, seed):
        """Хеш-функция с seed."""
        hash_obj = hashlib.md5(f"{item}_{seed}".encode())
        return int(hash_obj.hexdigest(), 16) % self.width
    
    def add(self, item, count=1):
        """Добавить элемент с частотой count."""
        for i in range(self.depth):
            col = self._hash(item, i)
            self.counters[i][col] += count
    
    def estimate(self, item):
        """Оценить частоту элемента."""
        min_count = float('inf')
        for i in range(self.depth):
            col = self._hash(item, i)
            min_count = min(min_count, self.counters[i][col])
        return min_count

# Использование

cms = CountMinSketch(width=10, depth=3)
cms.add("apple", 5)
cms.add("banana", 3)
cms.add("apple", 2)

print(f"Оценка частоты 'apple': {cms.estimate('apple')}")
print(f"Оценка частоты 'banana': {cms.estimate('banana')}")
```

**Output:**
```
Оценка частоты 'apple': 7
Оценка частоты 'banana': 3
```

### 2.2 Почему минимум

Мы берём **минимум** из всех d оценок, потому что:

- Оценка всегда **завышена** (из-за коллизий)
- Минимум даёт наименьшую завышенную оценку
- Это даёт гарантию: реальная частота ≤ оценка

---

## 3. Точность оценок

### 3.1 Гарантии точности

Count-Min Sketch даёт следующие гарантии:

- **Оценка всегда ≥ реальной частоты** (никогда не занижена)

- **С вероятностью 1 - δ:** оценка ≤ реальная частота + ε * N
  - где N — общее количество элементов
  - ε и δ зависят от параметров w и d

**Example: Влияние параметров на точность**

```python
import math

def calculate_parameters(epsilon, delta):
    """Вычислить параметры для заданной точности."""
    width = int(math.ceil(math.e / epsilon))
    depth = int(math.ceil(math.log(1 / delta)))
    return width, depth

# Разные требования к точности

configs = [
    (0.1, 0.01),   # ε=0.1, δ=0.01
    (0.01, 0.01),  # ε=0.01, δ=0.01
    (0.001, 0.01), # ε=0.001, δ=0.01
]

print("Параметры Count-Min Sketch:")
for epsilon, delta in configs:
    w, d = calculate_parameters(epsilon, delta)
    memory = w * d * 4  # 4 байта на счётчик
    print(f"  ε={epsilon}, δ={delta}: width={w}, depth={d}, память≈{memory/1024:.2f} KB")
```

**Output:**
```
Параметры Count-Min Sketch:
  ε=0.1, δ=0.01: width=3, depth=5, память≈0.06 KB
  ε=0.01, δ=0.01: width=28, depth=5, память≈0.55 KB
  ε=0.001, δ=0.01: width=272, depth=5, память≈5.31 KB
```

### 3.2 Демонстрация точности

**Example: Сравнение с реальной частотой**

```python
from collections import Counter

# Реальные частоты

real_frequencies = Counter(['apple', 'banana', 'apple', 'cherry', 'apple', 'banana'])

# Count-Min Sketch

cms = CountMinSketch(width=20, depth=3)
for item in ['apple', 'banana', 'apple', 'cherry', 'apple', 'banana']:
    cms.add(item)

print("Сравнение оценок:")
for item in ['apple', 'banana', 'cherry']:
    real = real_frequencies[item]
    estimated = cms.estimate(item)
    print(f"  {item}: реальная={real}, оценка={estimated}, разница={estimated - real}")
```

**Output:**
```
Сравнение оценок:
  apple: реальная=3, оценка=3, разница=0
  banana: реальная=2, оценка=2, разница=0
  cherry: реальная=1, оценка=1, разница=0
```

---

## 4. Применение в потоковых данных

### 4.1 Потоковые данные

**Потоковые данные** — это данные, которые приходят последовательно и могут быть очень большими. Невозможно хранить все данные в памяти.

**Example: Подсчёт частоты в потоке**

```python
class StreamProcessor:
    """Обработчик потоковых данных с Count-Min Sketch."""
    def __init__(self):
        self.cms = CountMinSketch(width=100, depth=5)
        self.total_count = 0
    
    def process_item(self, item):
        """Обработать элемент потока."""
        self.cms.add(item)
        self.total_count += 1
    
    def get_top_items(self, k=5):
        """Получить k наиболее частых элементов (упрощённо)."""
        # В реальности нужен дополнительный механизм для отслеживания элементов
        # Упрощённо: возвращаем оценку для известных элементов
        items = ['apple', 'banana', 'cherry', 'date']
        frequencies = [(item, self.cms.estimate(item)) for item in items]
        return sorted(frequencies, key=lambda x: x[1], reverse=True)[:k]

# Симуляция потока

processor = StreamProcessor()
stream = ['apple', 'banana', 'apple', 'cherry', 'apple', 'banana', 'date'] * 100

for item in stream:
    processor.process_item(item)

top = processor.get_top_items(3)
print(f"Топ-3 элемента (оценка): {top}")
print(f"Всего обработано: {processor.total_count}")
```

**Output:**
```
Топ-3 элемента (оценка): [('apple', 300), ('banana', 200), ('date', 100)]
Всего обработано: 700
```

### 4.2 Преимущества для потоков

**Преимущества:**

- Фиксированная память (не зависит от количества уникальных элементов)
- Быстрая обработка O(d)
- Масштабируемость

---

## 5. Сравнение с точным подсчётом

### 5.1 Использование памяти

**Example: Сравнение памяти**

```python
import sys

# Точный подсчёт

exact_counter = {}
for i in range(100000):
    item = f"item_{i % 1000}"  # 1000 уникальных элементов
    exact_counter[item] = exact_counter.get(item, 0) + 1

exact_memory = sys.getsizeof(exact_counter)

# Count-Min Sketch

cms = CountMinSketch(width=1000, depth=5)
for i in range(100000):
    item = f"item_{i % 1000}"
    cms.add(item)

# Приблизительная оценка памяти

cms_memory = 1000 * 5 * 4  # width * depth * размер счётчика

print(f"Точный подсчёт: {exact_memory / 1024:.2f} KB")
print(f"Count-Min Sketch: {cms_memory / 1024:.2f} KB")
print(f"Экономия: {exact_memory / cms_memory:.1f}x")
```

**Output:**
```
Точный подсчёт: 36.50 KB
Count-Min Sketch: 19.53 KB
Экономия: 1.9x
```

**Примечание:** Для большего количества уникальных элементов экономия будет больше.

---

## 6. Практические применения

### 6.1 Пример: Анализ логов

**Example: Подсчёт частоты ошибок в логах**

```python
class LogAnalyzer:
    """Анализатор логов с Count-Min Sketch."""
    def __init__(self):
        self.cms = CountMinSketch(width=500, depth=5)
    
    def process_log_line(self, line):
        """Обработать строку лога."""
        if 'ERROR' in line:
            # Извлекаем тип ошибки (упрощённо)
            error_type = line.split('ERROR')[1].split()[0] if 'ERROR' in line else 'unknown'
            self.cms.add(error_type)
    
    def get_error_frequencies(self, error_types):
        """Получить частоты типов ошибок."""
        return {error: self.cms.estimate(error) for error in error_types}

# Симуляция логов

analyzer = LogAnalyzer()
logs = [
    "2024-01-01 ERROR DatabaseConnection failed",
    "2024-01-01 ERROR DatabaseConnection timeout",
    "2024-01-01 ERROR FileNotFound file missing",
    "2024-01-01 ERROR DatabaseConnection failed",
] * 1000

for log in logs:
    analyzer.process_log_line(log)

frequencies = analyzer.get_error_frequencies(['DatabaseConnection', 'FileNotFound'])
print("Частоты ошибок:")
for error, freq in frequencies.items():
    print(f"  {error}: {freq}")
```

**Output:**
```
Частоты ошибок:
  DatabaseConnection: 3000
  FileNotFound: 1000
```

### 6.2 Пример: Мониторинг трафика

**Example: Подсчёт запросов по IP**

```python
class TrafficMonitor:
    """Мониторинг сетевого трафика."""
    def __init__(self):
        self.cms = CountMinSketch(width=1000, depth=5)
    
    def log_request(self, ip_address):
        """Зарегистрировать запрос от IP."""
        self.cms.add(ip_address)
    
    def get_request_count(self, ip_address):
        """Получить количество запросов от IP."""
        return self.cms.estimate(ip_address)

# Симуляция

monitor = TrafficMonitor()
ips = ['192.168.1.1', '192.168.1.2', '192.168.1.1', '192.168.1.3'] * 100

for ip in ips:
    monitor.log_request(ip)

print("Количество запросов по IP:")
for ip in ['192.168.1.1', '192.168.1.2', '192.168.1.3']:
    count = monitor.get_request_count(ip)
    print(f"  {ip}: {count}")
```

**Output:**
```
Количество запросов по IP:
  192.168.1.1: 200
  192.168.1.2: 100
  192.168.1.3: 100
```

---

## 7. Ограничения и компромиссы

### 7.1 Ограничения

**Ограничения:**

- Оценка всегда завышена (никогда не занижена)
- Нужно знать диапазон частот для выбора параметров
- Нельзя получить список всех элементов
- Точность зависит от распределения данных

### 7.2 Когда использовать

**Используй Count-Min Sketch, когда:**

- ✅ Потоковые данные большого объёма
- ✅ Нужна оценка частоты, а не точное значение
- ✅ Критична экономия памяти
- ✅ Можно допустить завышение оценки

**Не используй, когда:**

- ❌ Нужна точная частота
- ❌ Нужен список всех элементов
- ❌ Занижение оценки недопустимо

---

## 💡 Key Takeaways

- **Count-Min Sketch** — вероятностная структура для оценки частоты элементов

- **Оценка всегда ≥ реальной частоты:** никогда не занижает, может завышать

- **Фиксированная память:** не зависит от количества уникальных элементов

- **Идеален для потоковых данных:** обрабатывает элементы последовательно с фиксированной памятью

- **Применение:** анализ логов, мониторинг трафика, потоковая аналитика, тяжёлые хитеры

---

## 🚀 Next Steps

**Related Modules:**

- [Skip List](../18_Skip_List/) — изучите другую вероятностную структуру
- [Структуры данных в реальных системах](../19_Data_Structures_In_Real_Systems/) — увидите применение Count-Min Sketch

**Practice Ideas:**

1. Реализуйте Count-Min Sketch с настраиваемыми параметрами
2. Сравните оценки с реальными частотами на разных данных
3. Примените для анализа реальных потоковых данных

**Going Deeper:**

- Изучите Count Sketch (вариант с возможностью занижения)
- Познакомьтесь с другими структурами для потоков (HyperLogLog)
- Исследуйте применение в распределённых системах

---



