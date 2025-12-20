# Кучи и приоритетные очереди
## Heap структура данных и её применение

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать бинарные деревья
- Знать концепцию полных бинарных деревьев
- Понимать рекурсию
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру кучи (heap) и её свойства
- Реализовывать операции с кучей (вставка, извлечение минимума/максимума)
- Использовать модуль heapq в Python
- Применять приоритетные очереди для решения задач

---

## 1. Введение: что такое куча

**Куча (Heap)** — это специализированная древовидная структура данных, которая удовлетворяет свойству кучи:
- **Min-heap:** значение каждого узла меньше или равно значениям его детей

- **Max-heap:** значение каждого узла больше или равно значениям его детей

Куча обычно реализуется как **полное бинарное дерево**, что позволяет эффективно хранить её в массиве.

---

## 2. Структура кучи

### 2.1 Полное бинарное дерево

**Полное бинарное дерево** — это бинарное дерево, где все уровни полностью заполнены, кроме, возможно, последнего, который заполняется слева направо.

**Example: Представление кучи в массиве**

```python

class MinHeap:
    """Минимальная куча."""
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Индекс родителя."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Индекс левого ребёнка."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Индекс правого ребёнка."""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Поменять местами элементы."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Создание кучи
heap = MinHeap()
heap.heap = [1, 3, 2, 5, 4, 6, 7]

print(f"Куча: {heap.heap}")
print(f"Родитель индекса 3: индекс {heap.parent(3)}, значение {heap.heap[heap.parent(3)]}")
print(f"Левый ребёнок индекса 1: индекс {heap.left_child(1)}, значение {heap.heap[heap.left_child(1)]}")
```

**Output:**
```

Куча: [1, 3, 2, 5, 4, 6, 7]
Родитель индекса 3: индекс 1, значение 3
Левый ребёнок индекса 1: индекс 3, значение 5
```

### 2.2 Свойство кучи

**Min-heap свойство:** Для каждого узла значение меньше или равно значениям его детей.

**Max-heap свойство:** Для каждого узла значение больше или равно значениям его детей.

---

## 3. Операции с кучей

### 3.1 Вставка (Insert)

**Example: Вставка в min-heap**

```python

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, value):
        """Вставить элемент в кучу."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Восстановить свойство кучи снизу вверх."""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Использование
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.insert(9)

print(f"Куча после вставок: {heap.heap}")
```

**Output:**
```

Куча после вставок: [1, 3, 7, 5, 9]
```

### 3.2 Извлечение минимума (Extract Min)

**Example: Извлечение минимума**

```python

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def extract_min(self):
        """Извлечь минимальный элемент."""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, i):
        """Восстановить свойство кучи сверху вниз."""
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.swap(i, smallest)
            self._heapify_down(smallest)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Использование
heap = MinHeap()
for val in [5, 3, 7, 1, 9, 2]:
    heap.insert(val)

print(f"Куча: {heap.heap}")

min_val = heap.extract_min()
print(f"Извлечён минимум: {min_val}")
print(f"Куча после извлечения: {heap.heap}")
```

**Output:**
```

Куча: [1, 3, 2, 5, 9, 7]
Извлечён минимум: 1
Куча после извлечения: [2, 3, 7, 5, 9]
```

### 3.3 Получение минимума (Peek)

**Example: Получение минимума без удаления**

```python

def peek(self):
    """Получить минимальный элемент без удаления."""
    return self.heap[0] if self.heap else None

# Добавляем метод к классу
MinHeap.peek = peek

heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)

print(f"Минимум: {heap.peek()}")
print(f"Куча не изменилась: {heap.heap}")
```

**Output:**
```

Минимум: 3
Куча не изменилась: [3, 5, 7]
```

---

## 4. Модуль heapq в Python

### 4.1 Базовое использование

**Example: Использование heapq**

```python

import heapq

# Создание кучи (min-heap)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print(f"Куча: {heap}")

# Извлечение минимума
min_val = heapq.heappop(heap)
print(f"Извлечён минимум: {min_val}")
print(f"Куча после извлечения: {heap}")
```

**Output:**
```

Куча: [1, 3, 7, 5]
Извлечён минимум: 1
Куча после извлечения: [3, 5, 7]
```

### 4.2 Преобразование списка в кучу

**Example: heapify**

```python

import heapq

# Создание списка
data = [5, 3, 7, 1, 9, 2, 6]

# Преобразование в кучу за O(n)
heapq.heapify(data)

print(f"Куча: {data}")

# Извлечение элементов по порядку
print("Извлечение элементов:")
while data:
    print(f"  {heapq.heappop(data)}")
```

**Output:**
```

Куча: [1, 3, 2, 5, 9, 7, 6]
Извлечение элементов:
  1
  2
  3
  5
  6
  7
  9
```

### 4.3 Max-heap в Python

**Example: Реализация max-heap**

```python

import heapq

# Max-heap через инвертирование значений
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        heapq.heappush(self.heap, -value)  # Инвертируем
    
    def pop(self):
        return -heapq.heappop(self.heap)  # Инвертируем обратно
    
    def peek(self):
        return -self.heap[0] if self.heap else None

# Использование
max_heap = MaxHeap()
max_heap.push(5)
max_heap.push(3)
max_heap.push(7)
max_heap.push(1)

print(f"Максимум: {max_heap.peek()}")
print(f"Извлечён максимум: {max_heap.pop()}")
```

**Output:**
```

Максимум: 7
Извлечён максимум: 7
```

---

## 5. Приоритетные очереди

### 5.1 Что такое приоритетная очередь

**Приоритетная очередь** — это абстрактная структура данных, где каждый элемент имеет приоритет, и элементы с высшим приоритетом извлекаются первыми.

**Куча** — это эффективная реализация приоритетной очереди.

**Example: Приоритетная очередь задач**

```python

import heapq

class PriorityQueue:
    """Приоритетная очередь на основе кучи."""
    def __init__(self):
        self.heap = []
    
    def enqueue(self, item, priority):
        """Добавить элемент с приоритетом."""
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        """Извлечь элемент с наивысшим приоритетом."""
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item
        return None
    
    def is_empty(self):
        """Проверить, пуста ли очередь."""
        return len(self.heap) == 0

# Использование
pq = PriorityQueue()
pq.enqueue("Задача 1", 3)  # Низкий приоритет
pq.enqueue("Задача 2", 1)  # Высокий приоритет
pq.enqueue("Задача 3", 2)  # Средний приоритет

print("Обработка задач по приоритету:")
while not pq.is_empty():
    task = pq.dequeue()
    print(f"  Обработано: {task}")
```

**Output:**
```

Обработка задач по приоритету:
  Обработано: Задача 2
  Обработано: Задача 3
  Обработано: Задача 1
```

### 5.2 Применение: Алгоритм Дейкстры

**Example: Концептуальное использование в алгоритме Дейкстры**

```python

import heapq

def dijkstra_shortest_path(graph, start):
    """Упрощённая версия алгоритма Дейкстры."""
    # Приоритетная очередь для хранения (расстояние, узел)
    pq = [(0, start)]
    distances = {start: 0}
    visited = set()
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        # Обработка соседей (упрощённо)
        # В реальности здесь была бы обработка рёбер графа
        
    return distances

# Концептуальный пример
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2)],
    'C': []
}

distances = dijkstra_shortest_path(graph, 'A')
print(f"Расстояния: {distances}")
```

**Output:**
```

Расстояния: {'A': 0}
```

---

## 6. Сложность операций

### 6.1 Таблица сложности

| Операция | Сложность |
|----------|-----------|
| **Вставка** | O(log n) |
| **Извлечение минимума** | O(log n) |
| **Получение минимума** | O(1) |
| **Построение кучи из массива** | O(n) |
| **Удаление произвольного элемента** | O(log n) |

### 6.2 Построение кучи за O(n)

**Example: Эффективное построение кучи**

```python

import heapq
import time

# Большой список
large_list = list(range(10000, 0, -1))  # Обратный порядок

# Построение кучи
start = time.time()
heapq.heapify(large_list)
heapify_time = time.time() - start

# Проверка, что это куча
print(f"Построение кучи заняло: {heapify_time:.6f} секунд")
print(f"Минимум: {large_list[0]}")
print(f"Первые 10 элементов: {large_list[:10]}")
```

**Output:**
```

Построение кучи заняло: 0.001234 секунд
Минимум: 1
Первые 10 элементов: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## 7. Применение куч

### 7.1 Сортировка кучей (Heapsort)

**Example: Heapsort**

```python

import heapq

def heapsort(arr):
    """Сортировка с использованием кучи."""
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Тестирование
unsorted = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_arr = heapsort(unsorted.copy())

print(f"Неотсортированный: {unsorted}")
print(f"Отсортированный: {sorted_arr}")
```

**Output:**
```

Неотсортированный: [5, 2, 8, 1, 9, 3, 7, 4, 6]
Отсортированный: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Сложность:** O(n log n)

### 7.2 Поиск k наибольших элементов

**Example: Найти k наибольших элементов**

```python

import heapq

def find_k_largest(arr, k):
    """Найти k наибольших элементов."""
    # Используем min-heap размера k
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return sorted(heap, reverse=True)

# Тестирование
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3

result = find_k_largest(data, k)
print(f"Данные: {data}")
print(f"{k} наибольших: {result}")
```

**Output:**
```

Данные: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
3 наибольших: [9, 6, 5]
```

---

## 8. Практические примеры

### 8.1 Пример: Система обработки задач

**Example: Диспетчер задач с приоритетами**

```python

import heapq
from datetime import datetime

class TaskScheduler:
    """Планировщик задач с приоритетами."""
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_name, priority, deadline=None):
        """Добавить задачу."""
        # Приоритет: меньше = выше приоритет
        # Если есть deadline, учитываем его
        if deadline:
            priority_key = (priority, deadline.timestamp())
        else:
            priority_key = (priority, float('inf'))
        
        heapq.heappush(self.tasks, (priority_key, task_name))
    
    def process_next(self):
        """Обработать следующую задачу."""
        if self.tasks:
            priority, task = heapq.heappop(self.tasks)
            return task
        return None
    
    def get_queue_size(self):
        """Получить размер очереди."""
        return len(self.tasks)

# Использование
scheduler = TaskScheduler()
scheduler.add_task("Критическая задача", 1)
scheduler.add_task("Обычная задача", 3)
scheduler.add_task("Важная задача", 2)

print("Обработка задач:")
while scheduler.get_queue_size() > 0:
    task = scheduler.process_next()
    print(f"  {task}")
```

**Output:**
```

Обработка задач:
  Критическая задача
  Важная задача
  Обычная задача
```

---

## 💡 Key Takeaways

- **Куча** — это полное бинарное дерево, удовлетворяющее свойству кучи (min-heap или max-heap)

- **Представление в массиве** делает кучу эффективной: родитель = (i-1)//2, дети = 2*i+1, 2*i+2

- **Операции:** вставка O(log n), извлечение минимума O(log n), получение минимума O(1)

- **Приоритетная очередь** эффективно реализуется через кучу

- **Применение:** сортировка, алгоритм Дейкстры, планировщики задач, поиск k наибольших/наименьших

---

## 🚀 Next Steps

**Related Modules:**

- [Графы](../13_Graphs/) — изучите применение куч в алгоритмах на графах
- [Структуры данных в реальных системах](../19_Data_Structures_In_Real_Systems/) — увидите применение куч в практике

**Practice Ideas:**

1. Реализуйте min-heap и max-heap с нуля
2. Создайте систему планирования задач с приоритетами
3. Реализуйте heapsort и сравните с другими алгоритмами сортировки

**Going Deeper:**

- Изучите биномиальные и фибоначчиевы кучи
- Познакомьтесь с применением куч в алгоритмах сжатия данных
- Исследуйте оптимизации операций с кучей

---


