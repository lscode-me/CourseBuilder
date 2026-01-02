# Сравнение базовых структур данных
## Комплексный анализ и выбор структуры данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу массивов, связанных списков, хеш-таблиц и отсортированных массивов
- Знать концепцию сложности алгоритмов (Big-O)
- Понимать компромиссы между различными структурами данных
- Иметь опыт работы с основными структурами данных в Python

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Сравнивать базовые структуры данных по различным критериям
- Выбирать оптимальную структуру данных для конкретной задачи
- Анализировать компромиссы между производительностью и использованием памяти
- Применять инженерное мышление при выборе структур данных

---

## 1. Введение: важность правильного выбора

Выбор структуры данных — это одно из самых важных решений при проектировании программы. Правильный выбор может сделать программу в разы быстрее, а неправильный — привести к проблемам с производительностью.

**Цель этого модуля:** Научиться систематически сравнивать структуры данных и делать осознанный выбор.

---

## 2. Критерии сравнения

### 2.1 Основные критерии

При сравнении структур данных мы рассматриваем:

1. **Временная сложность операций** (Big-O)
2. **Пространственная сложность** (использование памяти)
3. **Кэш-локальность** (влияние на производительность)
4. **Упорядоченность** (сохранение порядка элементов)
5. **Гибкость** (поддержка различных операций)

---

## 3. Сравнительная таблица операций

### 3.1 Полная таблица сравнения

| Операция | Массив | Связанный список | Хеш-таблица | Отсортированный массив |
|----------|--------|------------------|-------------|------------------------|
| **Доступ по индексу** | O(1) | O(n) | O(1)* | O(1) |
| **Поиск элемента** | O(n) | O(n) | O(1) | O(log n) |
| **Вставка в начало** | O(n) | O(1) | O(1) | O(n) |
| **Вставка в конец** | O(1)** | O(n) | O(1) | O(n) |
| **Вставка в середину** | O(n) | O(n)*** | O(1) | O(n) |
| **Удаление из начала** | O(n) | O(1) | O(1) | O(n) |
| **Удаление из конца** | O(1) | O(n) | O(1) | O(n) |
| **Удаление из середины** | O(n) | O(n)*** | O(1) | O(n) |
| **Поиск диапазона** | O(n) | O(n) | O(n) | O(log n + k)**** |
| **Память** | O(n) | O(n)***** | O(n) | O(n) |
| **Кэш-локальность** | Отличная | Плохая | Хорошая | Отличная |
| **Упорядоченность** | Да | Да | Нет****** | Да |

\* По ключу  
\*\* Амортизированная сложность  
\*\*\* Если есть указатель на узел  
\*\*\*\* k — количество элементов в диапазоне  
\*\*\*\*\* Больше из-за указателей  
\*\*\*\*\*\* В Python 3.7+ порядок вставки сохраняется

### 3.2 Детальный анализ операций

**Example: Сравнение времени выполнения**

```python
import time

# Создаём структуры данных

size = 100000

# Массив

arr = list(range(size))

# Связанный список (упрощённо)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll_head = Node(0)
current = ll_head
for i in range(1, size):
    current.next = Node(i)
    current = current.next

# Хеш-таблица

hash_table = {i: i for i in range(size)}

# Отсортированный массив

sorted_arr = sorted(arr)

# Тест: поиск элемента

target = size // 2

# Поиск в массиве (линейный)

start = time.time()
result = target in arr
time_arr = time.time() - start

# Поиск в хеш-таблице

start = time.time()
result = target in hash_table
time_hash = time.time() - start

# Поиск в отсортированном массиве (бинарный)

import bisect
start = time.time()
index = bisect.bisect_left(sorted_arr, target)
result = index < len(sorted_arr) and sorted_arr[index] == target
time_sorted = time.time() - start

print(f"Поиск в массиве (линейный): {time_arr:.6f} секунд")
print(f"Поиск в хеш-таблице: {time_hash:.6f} секунд")
print(f"Поиск в отсортированном массиве (бинарный): {time_sorted:.6f} секунд")
```

**Output:**
```
Поиск в массиве (линейный): 0.002345 секунд
Поиск в хеш-таблице: 0.000001 секунд
Поиск в отсортированном массиве (бинарный): 0.000001 секунд
```

---

## 4. Анализ по типам операций

### 4.1 Частый доступ по индексу

**Лучший выбор: Массив**

```python
# Задача: хранение оценок студентов с доступом по ID

grades = [85, 90, 78, 92, 88]  # ID = индекс

# Быстрый доступ

student_id = 2
grade = grades[student_id]  # O(1)
print(f"Оценка студента {student_id}: {grade}")
```

**Output:**
```
Оценка студента 2: 78
```

### 4.2 Частый поиск по значению

**Лучший выбор: Хеш-таблица**

```python
# Задача: проверка, есть ли пользователь в системе

users = {'alice': True, 'bob': True, 'charlie': True}

# Быстрый поиск

username = 'alice'
if username in users:  # O(1)
    print(f"{username} найден в системе")
```

**Output:**
```
alice найден в системе
```

### 4.3 Частая вставка в начало

**Лучший выбор: Связанный список**

```python
# Задача: история операций (стек отмены)

class OperationHistory:
    def __init__(self):
        self.operations = []
        self.head = None
    
    def add_operation(self, op):
        """Добавить операцию в начало — O(1) для связанного списка."""
        # В Python list это O(n), но для демонстрации концепции
        self.operations.insert(0, op)  # В реальности использовали бы связанный список
```

### 4.4 Запросы по диапазону

**Лучший выбор: Отсортированный массив**

```python
# Задача: найти все оценки в диапазоне [80, 90]

import bisect

grades = [65, 72, 78, 85, 88, 92, 95]
sorted_grades = sorted(grades)

start = 80
end = 90

left = bisect.bisect_left(sorted_grades, start)
right = bisect.bisect_right(sorted_grades, end)

result = sorted_grades[left:right]
print(f"Оценки в диапазоне [{start}, {end}]: {result}")
```

**Output:**
```
Оценки в диапазоне [80, 90]: [85, 88]
```

---

## 5. Компромиссы

### 5.1 Производительность vs Память

**Example: Сравнение использования памяти**

```python
import sys

size = 1000

# Массив

arr = list(range(size))
arr_size = sys.getsizeof(arr)

# Хеш-таблица

hash_table = {i: i for i in range(size)}
hash_size = sys.getsizeof(hash_table)

# Связанный список (приблизительно)
# Каждый узел: данные + указатель + overhead

node_overhead = 56
estimated_ll_size = size * (8 + 8 + node_overhead)

print(f"Массив: {arr_size} байт")
print(f"Хеш-таблица: {hash_size} байт")
print(f"Связанный список (приблизительно): {estimated_ll_size} байт")
print(f"\nХеш-таблица использует примерно в {hash_size / arr_size:.1f} раз больше памяти")
```

**Output:**
```
Массив: 8056 байт
Хеш-таблица: 36968 байт
Связанный список (приблизительно): 72000 байт

Хеш-таблица использует примерно в 4.6 раз больше памяти
```

### 5.2 Скорость vs Гибкость

**Example: Сравнение гибкости**

```python
# Массив: ограниченный набор операций, но быстрый доступ

arr = [1, 2, 3, 4, 5]
print(f"Доступ по индексу: {arr[2]}")  # O(1)
print(f"Поиск элемента: {3 in arr}")  # O(n)

# Хеш-таблица: гибкий, быстрый поиск, но нет порядка (в старых версиях)

hash_table = {'a': 1, 'b': 2, 'c': 3}
print(f"Поиск по ключу: {hash_table.get('b')}")  # O(1)
print(f"Порядок элементов: {list(hash_table.keys())}")  # В Python 3.7+ сохраняется
```

**Output:**
```
Доступ по индексу: 3
Поиск элемента: True
Поиск по ключу: 2
Порядок элементов: ['a', 'b', 'c']
```

---

## 6. Практические сценарии выбора

### 6.1 Сценарий 1: Кэш данных

**Задача:** Кэшировать результаты вычислений с быстрым поиском.

**Выбор:** Хеш-таблица (dict)

```python
class Cache:
    """Простой кэш на основе хеш-таблицы."""
    def __init__(self):
        self.cache = {}
    
    def get(self, key):
        """Получить значение — O(1)."""
        return self.cache.get(key)
    
    def put(self, key, value):
        """Добавить значение — O(1)."""
        self.cache[key] = value

cache = Cache()
cache.put('result_1', 42)
print(f"Получено: {cache.get('result_1')}")
```

**Output:**
```
Получено: 42
```

**Обоснование:** Нужен быстрый поиск O(1), порядок не важен.

### 6.2 Сценарий 2: Очередь задач

**Задача:** Обрабатывать задачи в порядке поступления.

**Выбор:** Очередь (deque или связанный список)

```python
from collections import deque

class TaskQueue:
    """Очередь задач."""
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, task):
        """Добавить задачу — O(1)."""
        self.queue.append(task)
    
    def dequeue(self):
        """Обработать задачу — O(1)."""
        return self.queue.popleft()

queue = TaskQueue()
queue.enqueue("Задача 1")
queue.enqueue("Задача 2")
print(f"Обработано: {queue.dequeue()}")
```

**Output:**
```
Обработано: Задача 1
```

**Обоснование:** Нужен FIFO порядок, быстрая вставка/удаление с концов.

### 6.3 Сценарий 3: Поиск по диапазону

**Задача:** Найти все события в определённом временном диапазоне.

**Выбор:** Отсортированный массив

```python
import bisect
from datetime import datetime, timedelta

events = [
    (datetime(2024, 1, 1, 10, 0), "Встреча"),
    (datetime(2024, 1, 1, 11, 0), "Обед"),
    (datetime(2024, 1, 1, 14, 0), "Презентация"),
    (datetime(2024, 1, 1, 16, 0), "Встреча")
]

# Сортируем по времени

events.sort(key=lambda x: x[0])

# Найти события в диапазоне

start = datetime(2024, 1, 1, 11, 0)
end = datetime(2024, 1, 1, 15, 0)

times = [e[0] for e in events]
left = bisect.bisect_left(times, start)
right = bisect.bisect_right(times, end)

result = events[left:right]
print("События в диапазоне:")
for time, event in result:
    print(f"  {time.strftime('%H:%M')}: {event}")
```

**Output:**
```
События в диапазоне:
  11:00: Обед
  14:00: Презентация
```

**Обоснование:** Нужны запросы по диапазону, данные редко изменяются.

---

## 7. Чеклист для выбора структуры данных

### 7.1 Вопросы для анализа задачи

1. **Какие операции выполняются чаще всего?**
   - Доступ по индексу → Массив
   - Поиск по значению → Хеш-таблица
   - Вставка в начало → Связанный список
   - Запросы по диапазону → Отсортированный массив

2. **Как часто данные изменяются?**
   - Часто → Хеш-таблица или связанный список
   - Редко → Отсортированный массив

3. **Нужен ли порядок элементов?**
   - Да → Массив, связанный список, отсортированный массив
   - Нет → Хеш-таблица

4. **Есть ли ограничения по памяти?**
   - Да → Массив или отсортированный массив
   - Нет → Хеш-таблица

5. **Нужны ли запросы по диапазону?**
   - Да → Отсортированный массив
   - Нет → Хеш-таблица или массив

### 7.2 Матрица решений

**Example: Интерактивный выбор**

```python
def choose_data_structure(requirements):
    """Выбрать структуру данных на основе требований."""
    score = {
        'array': 0,
        'linked_list': 0,
        'hash_table': 0,
        'sorted_array': 0
    }
    
    # Частый доступ по индексу
    if requirements.get('frequent_index_access'):
        score['array'] += 3
        score['sorted_array'] += 2
    
    # Частый поиск
    if requirements.get('frequent_search'):
        score['hash_table'] += 3
        score['sorted_array'] += 2
    
    # Частая вставка в начало
    if requirements.get('frequent_prepend'):
        score['linked_list'] += 3
    
    # Запросы по диапазону
    if requirements.get('range_queries'):
        score['sorted_array'] += 3
    
    # Ограничения по памяти
    if requirements.get('memory_constrained'):
        score['array'] += 2
        score['sorted_array'] += 2
        score['hash_table'] -= 1
    
    # Нужен порядок
    if requirements.get('need_order'):
        score['array'] += 1
        score['linked_list'] += 1
        score['sorted_array'] += 1
    
    # Найти максимальный счёт
    best = max(score, key=score.get)
    return best, score

# Пример использования

requirements = {
    'frequent_search': True,
    'frequent_index_access': False,
    'range_queries': False,
    'memory_constrained': False,
    'need_order': False
}

best, scores = choose_data_structure(requirements)
print(f"Рекомендуемая структура: {best}")
print(f"Оценки: {scores}")
```

**Output:**
```
Рекомендуемая структура: hash_table
Оценки: {'array': 0, 'linked_list': 0, 'hash_table': 3, 'sorted_array': 2}
```

---

## 8. Реальные примеры

### 8.1 Пример: Система управления пользователями

**Требования:**

- Быстрый поиск пользователя по ID
- Частые обновления профилей
- Нет необходимости в порядке

**Выбор:** Хеш-таблица (dict)

```python
class UserManager:
    """Управление пользователями через хеш-таблицу."""
    def __init__(self):
        self.users = {}  # ID -> User data
    
    def get_user(self, user_id):
        """Получить пользователя — O(1)."""
        return self.users.get(user_id)
    
    def update_user(self, user_id, data):
        """Обновить пользователя — O(1)."""
        self.users[user_id] = data

manager = UserManager()
manager.update_user(1, {'name': 'Alice', 'email': 'alice@example.com'})
user = manager.get_user(1)
print(f"Пользователь: {user}")
```

**Output:**
```
Пользователь: {'name': 'Alice', 'email': 'alice@example.com'}
```

### 8.2 Пример: Система логов

**Требования:**

- Хранение логов в хронологическом порядке
- Поиск логов в временном диапазоне
- Редкие изменения

**Выбор:** Отсортированный массив

```python
import bisect
from datetime import datetime

class LogSystem:
    """Система логов на основе отсортированного массива."""
    def __init__(self):
        self.logs = []  # (timestamp, message)
    
    def add_log(self, timestamp, message):
        """Добавить лог с сохранением порядка."""
        bisect.insort(self.logs, (timestamp, message))
    
    def get_logs_in_range(self, start, end):
        """Получить логи в диапазоне."""
        times = [log[0] for log in self.logs]
        left = bisect.bisect_left(times, start)
        right = bisect.bisect_right(times, end)
        return self.logs[left:right]

logs = LogSystem()
base = datetime(2024, 1, 1, 10, 0)
logs.add_log(base, "Система запущена")
logs.add_log(base.replace(hour=11), "Ошибка соединения")
logs.add_log(base.replace(hour=12), "Соединение восстановлено")

start = base.replace(hour=10, minute=30)
end = base.replace(hour=11, minute=30)
result = logs.get_logs_in_range(start, end)
print("Логи в диапазоне:")
for time, msg in result:
    print(f"  {time.strftime('%H:%M')}: {msg}")
```

**Output:**
```
Логи в диапазоне:
  11:00: Ошибка соединения
```

---

## 💡 Key Takeaways

- **Выбор структуры данных** должен основываться на анализе операций и требований задачи

- **Нет универсальной структуры** — каждая оптимизирована для своих задач

- **Компромиссы неизбежны** — нужно балансировать между производительностью, памятью и гибкостью

- **Анализ операций** — ключ к правильному выбору: какие операции частые, какие редкие

- **Практический опыт** помогает принимать правильные решения, но систематический анализ надёжнее

---

## 🚀 Next Steps

**Related Modules:**

- [Деревья как структуры данных](../09_Trees_As_Data_Structures/) — изучите более сложные структуры данных
- [Как выбирать структуру данных](../20_Choosing_Data_Structures/) — углубитесь в инженерный подход к выбору

**Practice Ideas:**

1. Проанализируйте реальную задачу и выберите оптимальную структуру данных
2. Сравните производительность разных структур на ваших данных
3. Создайте систему рекомендаций для выбора структуры данных

**Going Deeper:**

- Изучите амортизированный анализ сложности
- Познакомьтесь с пространственно-временными компромиссами
- Исследуйте гибридные структуры данных

---



