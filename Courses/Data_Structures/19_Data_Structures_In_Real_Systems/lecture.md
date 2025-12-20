# Структуры данных в реальных системах
## Кэши, индексы, очереди сообщений и потоковые платформы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основные структуры данных (хеш-таблицы, деревья, кучи)
- Знать вероятностные структуры данных (Bloom Filter, Count-Min Sketch)
- Понимать концепции кэширования и индексации
- Иметь базовые знания о распределённых системах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать, как структуры данных применяются в реальных системах
- Знать структуры данных для кэшей (LRU, LFU)
- Понимать применение индексов в базах данных
- Применять структуры данных в очередях сообщений и потоковых платформах

---

## 1. Введение: структуры данных в производстве

В реальных системах структуры данных — это не просто учебные примеры, а основа производительности и масштабируемости. Понимание того, как структуры данных применяются в реальных системах, критично для создания эффективных решений.

---

## 2. Кэши

### 2.1 LRU Cache (Least Recently Used)

**LRU Cache** удаляет наименее недавно использованные элементы при переполнении.

**Структуры данных:**

- **Хеш-таблица:** для быстрого доступа O(1)

- **Двусвязный список:** для отслеживания порядка использования

**Example: Упрощённая реализация LRU Cache**

```python

from collections import OrderedDict

class LRUCache:
    """LRU Cache на основе OrderedDict."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """Получить значение."""
        if key not in self.cache:
            return None
        
        # Перемещаем в конец (самый недавно использованный)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """Установить значение."""
        if key in self.cache:
            # Обновляем и перемещаем в конец
            self.cache.move_to_end(key)
        else:
            # Проверяем размер
            if len(self.cache) >= self.capacity:
                # Удаляем наименее недавно использованный (первый)
                self.cache.popitem(last=False)
        
        self.cache[key] = value

# Использование
cache = LRUCache(capacity=3)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)

print(f"Получено 'a': {cache.get('a')}")
cache.put('d', 4)  # 'b' будет удалён (наименее недавно использованный)

print(f"Получено 'b': {cache.get('b')}")  # None, удалён
print(f"Получено 'c': {cache.get('c')}")
```

**Output:**
```

Получено 'a': 1
Получено 'b': None
Получено 'c': 3
```

### 2.2 LFU Cache (Least Frequently Used)

**LFU Cache** удаляет наименее часто используемые элементы.

**Структуры данных:**

- **Хеш-таблица:** для доступа к элементам

- **Куча или отсортированная структура:** для отслеживания частоты использования

**Example: Концептуальная реализация LFU**

```python

from collections import defaultdict

class LFUCache:
    """Упрощённая реализация LFU Cache."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> (value, frequency)
        self.frequency = defaultdict(int)  # key -> frequency
    
    def get(self, key):
        """Получить значение."""
        if key not in self.cache:
            return None
        
        # Увеличиваем частоту
        self.frequency[key] += 1
        value, _ = self.cache[key]
        self.cache[key] = (value, self.frequency[key])
        return value
    
    def put(self, key, value):
        """Установить значение."""
        if key in self.cache:
            # Обновляем
            self.frequency[key] += 1
            self.cache[key] = (value, self.frequency[key])
        else:
            # Проверяем размер
            if len(self.cache) >= self.capacity:
                # Находим наименее часто используемый
                min_freq_key = min(self.cache.keys(), key=lambda k: self.cache[k][1])
                del self.cache[min_freq_key]
                del self.frequency[min_freq_key]
            
            self.frequency[key] = 1
            self.cache[key] = (value, 1)

# Использование
lfu = LFUCache(capacity=3)
lfu.put('a', 1)
lfu.put('b', 2)
lfu.put('c', 3)

lfu.get('a')  # Используем 'a'
lfu.get('a')  # Используем 'a' ещё раз
lfu.put('d', 4)  # 'b' или 'c' будет удалён (наименее часто используемый)

print(f"Кэш: {dict(lfu.cache)}")
```

**Output:**
```

Кэш: {'a': (1, 3), 'c': (3, 1), 'd': (4, 1)}
```

---

## 3. Индексы в базах данных

### 3.1 B+ деревья для индексов

Как мы изучали, базы данных используют **B+ деревья** для индексации.

**Применение:**

- Индекс первичного ключа
- Индекс внешнего ключа
- Составные индексы

**Example: Концептуальный индекс БД**

```python

class DatabaseIndex:
    """Концептуальный индекс базы данных."""
    def __init__(self):
        # В реальности: B+ дерево
        # Упрощённо: словарь для демонстрации
        self.index = {}  # key -> (page_id, offset)
    
    def insert(self, key, page_id, offset):
        """Добавить индекс."""
        self.index[key] = (page_id, offset)
    
    def search(self, key):
        """Поиск по ключу."""
        return self.index.get(key)
    
    def range_search(self, start_key, end_key):
        """Диапазонный поиск (B+ дерево оптимизировано)."""
        result = []
        for k, location in self.index.items():
            if start_key <= k <= end_key:
                result.append((k, location))
        return sorted(result)

# Использование
db_index = DatabaseIndex()
db_index.insert(100, page_id=5, offset=1024)
db_index.insert(200, page_id=5, offset=2048)
db_index.insert(150, page_id=6, offset=512)

result = db_index.search(150)
print(f"Запись 150: страница {result[0]}, смещение {result[1]}")

range_result = db_index.range_search(120, 180)
print(f"Диапазон [120, 180]: {range_result}")
```

**Output:**
```

Запись 150: страница 6, смещение 512
Диапазон [120, 180]: [(150, (6, 512))]
```

### 3.2 Хеш-индексы

Для точечного поиска используются **хеш-индексы**.

**Применение:**

- Точное совпадение (equality)
- Не подходит для диапазонных запросов

---

## 4. Очереди сообщений

### 4.1 Очередь сообщений

**Очереди сообщений** используют различные структуры данных:
- **Очередь (Queue):** для FIFO обработки

- **Приоритетная очередь (Priority Queue):** для обработки по приоритету

- **Кольцевой буфер (Ring Buffer):** для фиксированного размера

**Example: Очередь сообщений с приоритетами**

```python

import heapq
from datetime import datetime

class MessageQueue:
    """Очередь сообщений с приоритетами."""
    def __init__(self):
        self.queue = []  # (priority, timestamp, message)
        self.counter = 0  # Для стабильной сортировки
    
    def enqueue(self, message, priority=0):
        """Добавить сообщение."""
        timestamp = datetime.now()
        # Отрицательный приоритет для min-heap (меньше = выше приоритет)
        heapq.heappush(self.queue, (-priority, self.counter, timestamp, message))
        self.counter += 1
    
    def dequeue(self):
        """Обработать следующее сообщение."""
        if self.queue:
            _, _, timestamp, message = heapq.heappop(self.queue)
            return message, timestamp
        return None, None

# Использование

mq = MessageQueue()
mq.enqueue("Обычное сообщение", priority=0)
mq.enqueue("Важное сообщение", priority=2)
mq.enqueue("Критическое сообщение", priority=5)

print("Обработка сообщений:")
while mq.queue:
    msg, ts = mq.dequeue()
    print(f"  {msg}")
```

**Output:**
```

Обработка сообщений:
  Критическое сообщение
  Важное сообщение
  Обычное сообщение
```

### 4.2 Kafka и потоковые платформы

**Apache Kafka** использует:
- **Логи (Logs):** для хранения сообщений

- **Индексы:** для быстрого доступа к позициям в логе

- **Сегменты:** для управления размером

---

## 5. Потоковые платформы

### 5.1 Обработка потоковых данных

**Структуры данных для потоков:**

- **Count-Min Sketch:** для оценки частоты

- **Bloom Filter:** для фильтрации дубликатов

- **Sliding Window:** для обработки временных окон

**Example: Обработка потока с Count-Min Sketch**

```python

from collections import defaultdict

class StreamProcessor:
    """Обработчик потоковых данных."""
    def __init__(self):
        # В реальности: Count-Min Sketch
        # Упрощённо: счётчик для демонстрации
        self.frequencies = defaultdict(int)
    
    def process_stream(self, stream):
        """Обработать поток данных."""
        for item in stream:
            self.frequencies[item] += 1
    
    def get_top_items(self, k=5):
        """Получить k наиболее частых элементов."""
        sorted_items = sorted(self.frequencies.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:k]

# Симуляция потока
processor = StreamProcessor()
stream = ['user_1', 'user_2', 'user_1', 'user_3', 'user_1', 'user_2'] * 1000

processor.process_stream(stream)
top = processor.get_top_items(3)

print("Топ-3 элемента:")
for item, count in top:
    print(f"  {item}: {count}")
```

**Output:**
```

Топ-3 элемента:
  user_1: 3000
  user_2: 2000
  user_3: 1000
```

---

## 6. Реальные примеры систем

### 6.1 Redis

**Redis использует:**

- **Хеш-таблицы:** для обычных ключей

- **Skip List:** для Sorted Sets

- **Списки:** для Lists

- **Строки:** для Strings

### 6.2 PostgreSQL

**PostgreSQL использует:**

- **B+ деревья:** для большинства индексов

- **Хеш-индексы:** для точного совпадения

- **GiST индексы:** для специализированных типов данных

### 6.3 Cassandra

**Cassandra использует:**

- **LSM-деревья:** для хранения данных

- **Bloom Filter:** для предварительной фильтрации

- **Memtables:** для записи в память

---

## 7. Выбор структуры данных для системы

### 7.1 Критерии выбора

При выборе структуры данных для системы нужно учитывать:

- **Паттерны доступа:** какие операции частые?

- **Объём данных:** сколько данных ожидается?

- **Ограничения по памяти:** сколько памяти доступно?

- **Latency vs Throughput:** что важнее?

- **Требования к точности:** нужна ли гарантированная точность?

**Example: Анализ требований**

```python

def choose_cache_strategy(requirements):
    """Выбрать стратегию кэширования."""
    if requirements.get('need_frequency_tracking'):
        return "LFU Cache"
    elif requirements.get('need_recency_tracking'):
        return "LRU Cache"
    elif requirements.get('fixed_size'):
        return "Ring Buffer"
    else:
        return "Simple Cache"

# Примеры

req1 = {'need_recency_tracking': True}
req2 = {'need_frequency_tracking': True}
req3 = {'fixed_size': True}

print(f"Требования 1: {choose_cache_strategy(req1)}")
print(f"Требования 2: {choose_cache_strategy(req2)}")
print(f"Требования 3: {choose_cache_strategy(req3)}")
```

**Output:**
```

Требования 1: LRU Cache
Требования 2: LFU Cache
Требования 3: Ring Buffer
```

---

## 💡 Key Takeaways

- **Кэши (LRU, LFU)** используют комбинацию хеш-таблиц и структур для отслеживания порядка/частоты

- **Индексы БД** используют B+ деревья для эффективного поиска и диапазонных запросов

- **Очереди сообщений** используют приоритетные очереди и кольцевые буферы

- **Потоковые платформы** используют вероятностные структуры (Count-Min Sketch, Bloom Filter)

- **Реальные системы** комбинируют различные структуры данных для оптимальной производительности

- **Выбор структуры** зависит от паттернов доступа, объёма данных и требований системы

---

## 🚀 Next Steps

**Related Modules:**

- [Как выбирать структуру данных](../20_Choosing_Data_Structures/) — систематический подход к выбору

**Practice Ideas:**

1. Изучите реализацию кэша в вашем любимом фреймворке
2. Проанализируйте индексы в вашей БД
3. Исследуйте структуры данных в Redis или другой системе

**Going Deeper:**

- Изучите детали реализации в конкретных системах (Redis, PostgreSQL, Kafka)
- Познакомьтесь с новыми структурами данных (LSM-деревья, Raft)
- Исследуйте применение в распределённых системах

---



