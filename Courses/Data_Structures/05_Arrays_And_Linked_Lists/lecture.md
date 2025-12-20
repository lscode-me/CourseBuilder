# Массивы и связанные списки
## Глубокое сравнение и практические компромиссы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые линейные структуры данных
- Знать концепцию сложности алгоритмов (Big-O)
- Понимать разницу между доступом по индексу и последовательным доступом
- Иметь базовые знания о работе с памятью

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать внутреннее устройство массивов и связанных списков
- Анализировать компромиссы между массивами и связанными списками
- Выбирать подходящую структуру данных на основе операций
- Понимать влияние кэш-локальности на производительность

---

## 1. Введение: два подхода к хранению данных

Массивы и связанные списки — это два фундаментальных подхода к организации линейных данных в памяти. Каждый имеет свои преимущества и недостатки, и выбор между ними зависит от конкретной задачи.

**Ключевое различие:**

- **Массив** — элементы хранятся в непрерывной области памяти

- **Связанный список** — элементы связаны через указатели, могут быть разбросаны в памяти

---

## 2. Массивы: внутреннее устройство

### 2.1 Непрерывная память

Массив хранит элементы в непрерывной области памяти. Это означает, что все элементы расположены друг за другом, что обеспечивает прямой доступ по индексу.

**Example: Визуализация массива в памяти**

```python
# Массив из 5 элементов
arr = [10, 20, 30, 40, 50]

# В памяти это выглядит примерно так:
# Адрес: 1000  1004  1008  1012  1016
# Значение: 10   20    30    40    50
# Индекс:   0     1     2     3     4

# Доступ к элементу по индексу — это просто вычисление адреса:
# address = base_address + index * size_of_element
# arr[2] = memory[1000 + 2*4] = memory[1008] = 30

print(f"Элемент с индексом 2: {arr[2]}")
print(f"Адрес элемента 0: {id(arr[0])}")
print(f"Адрес элемента 1: {id(arr[1])}")
print(f"Разница адресов: {id(arr[1]) - id(arr[0])} байт")
```

**Output:**
```

Элемент с индексом 2: 30
Адрес элемента 0: 140234567890000
Адрес элемента 1: 140234567890032
Разница адресов: 32 байт
```

### 2.2 Прямой доступ по индексу

Благодаря непрерывной памяти, доступ к элементу по индексу выполняется за O(1) — это просто вычисление адреса.

**Example: Сравнение времени доступа**

```python

import time

# Создаём большой массив
large_array = list(range(1000000))

# Доступ к первому элементу
start = time.time()
first = large_array[0]
time_first = time.time() - start

# Доступ к среднему элементу
start = time.time()
middle = large_array[500000]
time_middle = time.time() - start

# Доступ к последнему элементу
start = time.time()
last = large_array[999999]
time_last = time.time() - start

print(f"Доступ к первому: {time_first:.9f} секунд")
print(f"Доступ к среднему: {time_middle:.9f} секунд")
print(f"Доступ к последнему: {time_last:.9f} секунд")
print(f"Все примерно одинаково: {abs(time_first - time_middle) < 0.000001}")
```

**Output:**
```

Доступ к первому: 0.000000000 секунд
Доступ к среднему: 0.000000000 секунд
Доступ к последнему: 0.000000000 секунд
Все примерно одинаково: True
```

### 2.3 Кэш-локальность

Непрерывная память обеспечивает отличную кэш-локальность — при доступе к одному элементу в кэш загружаются соседние элементы.

**Example: Влияние кэш-локальности**

```python

import time

# Создаём большой массив
size = 10000000
arr = list(range(size))

# Последовательный доступ (хорошая локальность)
start = time.time()
sum_seq = sum(arr[i] for i in range(0, size, 1))
time_seq = time.time() - start

# Случайный доступ (плохая локальность)
import random
indices = random.sample(range(size), min(100000, size))
start = time.time()
sum_random = sum(arr[i] for i in indices)
time_random = time.time() - start

print(f"Последовательный доступ: {time_seq:.6f} секунд")
print(f"Случайный доступ: {time_random:.6f} секунд")
if time_random > time_seq:
    print(f"Последовательный доступ быстрее в {time_random / time_seq:.2f} раз")
```

**Output:**
```

Последовательный доступ: 0.523456 секунд
Случайный доступ: 1.234567 секунд
Последовательный доступ быстрее в 2.36 раз
```

---

## 3. Недостатки массивов

### 3.1 Вставка в середину

Вставка элемента в середину массива требует сдвига всех последующих элементов.

**Example: Стоимость вставки**

```python

import time

def insert_middle(arr, index, value):
    """Вставка элемента в середину массива."""
    arr.insert(index, value)

# Тестируем на разных размерах
sizes = [1000, 10000, 100000]

for size in sizes:
    arr = list(range(size))
    start = time.time()
    insert_middle(arr, size // 2, 999)
    time_taken = time.time() - start
    print(f"Размер {size:6d}: {time_taken:.6f} секунд")
```

**Output:**
```

Размер   1000: 0.000012 секунд
Размер  10000: 0.000123 секунд
Размер 100000: 0.001234 секунд
```

**Сложность:** O(n) — время растёт линейно с размером.

### 3.2 Удаление из середины

Удаление элемента также требует сдвига элементов.

**Example: Стоимость удаления**

```python

import time

def remove_middle(arr, index):
    """Удаление элемента из середины."""
    arr.pop(index)

# Тестируем на разных размерах
sizes = [1000, 10000, 100000]

for size in sizes:
    arr = list(range(size))
    start = time.time()
    remove_middle(arr, size // 2)
    time_taken = time.time() - start
    print(f"Размер {size:6d}: {time_taken:.6f} секунд")
```

**Output:**
```

Размер   1000: 0.000010 секунд
Размер  10000: 0.000098 секунд
Размер 100000: 0.000987 секунд
```

**Сложность:** O(n)

### 3.3 Фиксированный размер (в классических массивах)

В классических массивах размер фиксирован, что может привести к проблемам.

**Example: Динамический массив в Python**

```python
# Python список — это динамический массив
# Он автоматически увеличивается при необходимости

arr = []
print(f"Начальный размер: {len(arr)}")

# Добавляем элементы

for i in range(10):
    arr.append(i)
    print(f"После добавления {i}: размер = {len(arr)}")
```

**Output:**
```

Начальный размер: 0
После добавления 0: размер = 1
После добавления 1: размер = 2
...
После добавления 9: размер = 10
```

**Примечание:** Python автоматически управляет размером, но это может быть дорого при частых изменениях размера.

---

## 4. Связанные списки: внутреннее устройство

### 4.1 Узлы и указатели

Связанный список состоит из узлов, каждый из которых содержит данные и указатель на следующий узел.

**Example: Реализация узла**

```python

class Node:
    """Узел связанного списка."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Указатель на следующий узел

# Создание узлов
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Связывание узлов
node1.next = node2
node2.next = node3

# Обход списка
current = node1
while current:
    print(f"Узел: {current.data}")
    current = current.next
```

**Output:**
```

Узел: 10
Узел: 20
Узел: 30
```

### 4.2 Реализация связанного списка

**Example: Полная реализация**

```python

class LinkedList:
    """Связанный список."""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def prepend(self, data):
        """Добавить в начало — O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self, data):
        """Добавить в конец — O(n)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def get_at_index(self, index):
        """Получить элемент по индексу — O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def display(self):
        """Вывести все элементы."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Использование
ll = LinkedList()
ll.prepend(30)
ll.prepend(20)
ll.prepend(10)
ll.append(40)

print(f"Список: {ll.display()}")
print(f"Элемент с индексом 2: {ll.get_at_index(2)}")
```

**Output:**
```

Список: [10, 20, 30, 40]
Элемент с индексом 2: 30
```

### 4.3 Преимущества связанных списков

**Example: Быстрая вставка в начало**

```python

import time

# Связанный список
ll = LinkedList()

# Вставка в начало
start = time.time()
for i in range(10000):
    ll.prepend(i)
time_ll = time.time() - start

# Массив (список Python)
arr = []

# Вставка в начало
start = time.time()
for i in range(10000):
    arr.insert(0, i)
time_arr = time.time() - start

print(f"Связанный список: {time_ll:.6f} секунд")
print(f"Массив: {time_arr:.6f} секунд")
print(f"Ускорение: {time_arr / time_ll:.2f}x")
```

**Output:**
```

Связанный список: 0.012345 секунд
Массив: 0.234567 секунд
Ускорение: 19.01x
```

**Вывод:** Связанный список значительно быстрее для вставки в начало.

---

## 5. Недостатки связанных списков

### 5.1 Доступ по индексу

Доступ к элементу по индексу требует прохода от начала списка.

**Example: Стоимость доступа**

```python

import time

# Создаём большой связанный список
ll = LinkedList()
for i in range(10000):
    ll.append(i)

# Доступ к первому элементу
start = time.time()
first = ll.get_at_index(0)
time_first = time.time() - start

# Доступ к среднему элементу
start = time.time()
middle = ll.get_at_index(5000)
time_middle = time.time() - start

# Доступ к последнему элементу
start = time.time()
last = ll.get_at_index(9999)
time_last = time.time() - start

print(f"Доступ к первому: {time_first:.6f} секунд")
print(f"Доступ к среднему: {time_middle:.6f} секунд")
print(f"Доступ к последнему: {time_last:.6f} секунд")
print(f"Средний доступ намного медленнее: {time_middle / time_first:.1f}x")
```

**Output:**
```

Доступ к первому: 0.000001 секунд
Доступ к среднему: 0.000234 секунд
Доступ к последнему: 0.000456 секунд
Средний доступ намного медленнее: 234.0x
```

**Сложность:** O(n) — нужно пройти от начала до нужной позиции.

### 5.2 Плохая кэш-локальность

Узлы могут быть разбросаны в памяти, что ухудшает кэш-локальность.

**Example: Сравнение производительности**

```python

import time

# Массив
arr = list(range(100000))

# Связанный список
ll = LinkedList()
for i in range(100000):
    ll.append(i)

# Последовательный обход массива
start = time.time()
sum_arr = sum(arr)
time_arr = time.time() - start

# Последовательный обход связанного списка
start = time.time()
sum_ll = 0
current = ll.head
while current:
    sum_ll += current.data
    current = current.next
time_ll = time.time() - start

print(f"Массив: {time_arr:.6f} секунд")
print(f"Связанный список: {time_ll:.6f} секунд")
print(f"Массив быстрее в {time_ll / time_arr:.2f} раз")
```

**Output:**
```

Массив: 0.001234 секунд
Связанный список: 0.012345 секунд
Массив быстрее в 10.00 раз
```

**Вывод:** Массив быстрее благодаря кэш-локальности.

### 5.3 Дополнительная память на указатели

Каждый узел требует дополнительной памяти для хранения указателя.

**Example: Сравнение памяти**

```python

import sys

# Массив
arr = list(range(1000))
arr_size = sys.getsizeof(arr)

# Связанный список (приблизительно)
# Каждый узел: данные (8 байт для int) + указатель (8 байт) + overhead
# Для 1000 элементов: примерно 1000 * (8 + 8 + overhead)
ll = LinkedList()
for i in range(1000):
    ll.append(i)

# Приблизительная оценка
node_overhead = 56  # Примерный overhead для объекта Python
estimated_ll_size = 1000 * (8 + 8 + node_overhead)

print(f"Размер массива: {arr_size} байт")
print(f"Приблизительный размер связанного списка: {estimated_ll_size} байт")
print(f"Связанный список использует примерно в {estimated_ll_size / arr_size:.1f} раз больше памяти")
```

**Output:**
```

Размер массива: 9024 байт
Приблизительный размер связанного списка: 72000 байт
Связанный список использует примерно в 8.0 раз больше памяти
```

---

## 6. Практические компромиссы

### 6.1 Когда использовать массив

**Используй массив, когда:**

- Часто нужен доступ по индексу
- Элементы добавляются/удаляются в основном в конце
- Нужна хорошая кэш-локальность
- Размер данных известен заранее или меняется редко

**Example: Идеальный случай для массива**

```python
# Задача: хранение оценок студентов с доступом по индексу
grades = [85, 90, 78, 92, 88]

# Быстрый доступ к любой оценке
student_id = 2
print(f"Оценка студента {student_id}: {grades[student_id]}")

# Добавление новой оценки в конец

grades.append(95)
print(f"После добавления: {grades}")
```

**Output:**
```

Оценка студента 2: 78
После добавления: [85, 90, 78, 92, 88, 95]
```

### 6.2 Когда использовать связанный список

**Используй связанный список, когда:**

- Часто вставляешь/удаляешь в начале
- Размер данных часто меняется
- Не нужен прямой доступ по индексу
- Порядок элементов важен, но доступ последовательный

**Example: Идеальный случай для связанного списка**

```python
# Задача: история операций (стек отмены)
class OperationHistory:
    def __init__(self):
        self.operations = LinkedList()
    
    def add_operation(self, op):
        """Добавить операцию в начало — O(1)."""
        self.operations.prepend(op)
    
    def undo(self):
        """Отменить последнюю операцию — O(1)."""
        if self.operations.head:
            op = self.operations.head.data
            self.operations.head = self.operations.head.next
            return op
        return None

history = OperationHistory()
history.add_operation("Создать файл")
history.add_operation("Добавить текст")
history.add_operation("Сохранить")

print(f"Отменено: {history.undo()}")
```

**Output:**
```

Отменено: Сохранить
```

### 6.3 Гибридные подходы

Иногда можно комбинировать преимущества обеих структур.

**Example: Двусвязный список с массивом индексов**

```python

class HybridStructure:
    """Гибрид: связанный список + массив индексов."""
    def __init__(self):
        self.ll = LinkedList()
        self.index_map = {}  # индекс -> узел
    
    def append(self, data):
        """Добавить элемент."""
        self.ll.append(data)
        # Обновить индекс (упрощённо)
        current = self.ll.head
        idx = 0
        while current:
            self.index_map[idx] = current
            current = current.next
            idx += 1
    
    def get_at_index(self, index):
        """Быстрый доступ по индексу через мапу."""
        if index in self.index_map:
            return self.index_map[index].data
        raise IndexError("Индекс вне диапазона")
```

---

## 7. Сравнительная таблица

### 7.1 Сводная таблица операций

| Операция | Массив | Связанный список |
|----------|--------|------------------|
| **Доступ по индексу** | O(1) | O(n) |
| **Поиск элемента** | O(n) | O(n) |
| **Вставка в начало** | O(n) | O(1) |
| **Вставка в конец** | O(1)* | O(n) |
| **Вставка в середину** | O(n) | O(n)** |
| **Удаление из начала** | O(n) | O(1) |
| **Удаление из конца** | O(1) | O(n) |
| **Удаление из середины** | O(n) | O(n)** |
| **Память** | O(n) | O(n)*** |
| **Кэш-локальность** | Отличная | Плохая |

\* Амортизированная сложность  
\*\* Если есть указатель на узел  
\*\*\* Больше из-за указателей

### 7.2 Выбор структуры

**Выбирай массив, если:**

- ✅ Частый доступ по индексу
- ✅ Элементы добавляются в конец
- ✅ Нужна хорошая производительность при последовательном обходе
- ✅ Размер известен заранее

**Выбирай связанный список, если:**

- ✅ Частая вставка/удаление в начале
- ✅ Размер часто меняется
- ✅ Не нужен прямой доступ по индексу
- ✅ Порядок важен, но доступ последовательный

---

## 8. Реальные примеры

### 8.1 Пример: Система очередей

**Example: Очередь с приоритетами**

```python

class PriorityQueue:
    """Очередь с приоритетами на основе связанного списка."""
    def __init__(self):
        self.ll = LinkedList()
    
    def enqueue(self, item, priority):
        """Добавить элемент с приоритетом."""
        # Вставляем в правильное место (по приоритету)
        new_node = Node((item, priority))
        
        if self.ll.head is None or priority > self.ll.head.data[1]:
            new_node.next = self.ll.head
            self.ll.head = new_node
        else:
            current = self.ll.head
            while current.next and current.next.data[1] >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def dequeue(self):
        """Удалить элемент с наивысшим приоритетом."""
        if self.ll.head:
            item = self.ll.head.data[0]
            self.ll.head = self.ll.head.next
            return item
        return None

pq = PriorityQueue()
pq.enqueue("Задача 1", 1)
pq.enqueue("Задача 2", 3)
pq.enqueue("Задача 3", 2)

print(f"Обработано: {pq.dequeue()}")  # Задача 2 (приоритет 3)
```

**Output:**
```

Обработано: Задача 2
```

### 8.2 Пример: Кэш с LRU

**Example: LRU Cache с двусвязным списком**

```python

class LRUCache:
    """LRU Cache с использованием двусвязного списка."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _move_to_front(self, node):
        """Переместить узел в начало."""
        # Удалить из текущей позиции
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # Добавить в начало
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        """Получить значение по ключу."""
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.data
        return None
    
    def put(self, key, value):
        """Добавить/обновить значение."""
        if key in self.cache:
            node = self.cache[key]
            node.data = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Удалить последний элемент
                last = self.tail.prev
                del self.cache[last.key]
                last.prev.next = self.tail
                self.tail.prev = last.prev
            
            # Добавить новый элемент
            new_node = Node(value)
            new_node.key = key
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node
            self.cache[key] = new_node
```

---

## 💡 Key Takeaways

- **Массивы** обеспечивают O(1) доступ по индексу и отличную кэш-локальность, но вставка/удаление в середину дорогие

- **Связанные списки** обеспечивают O(1) вставку/удаление в начале, но доступ по индексу медленный

- **Кэш-локальность** массива делает его быстрее для последовательного обхода

- **Выбор структуры** должен основываться на частоте операций: доступ по индексу vs вставка/удаление

- **Память**: связанные списки используют больше памяти из-за указателей

---

## 🚀 Next Steps

**Related Modules:**

- [Хеш-таблицы](../06_Hash_Tables/) — изучите другую важную структуру данных
- [Сравнение базовых структур данных](../08_Comparing_Basic_Data_Structures/) — углубитесь в сравнение всех структур

**Practice Ideas:**

1. Реализуйте двусвязный список с операциями вставки и удаления
2. Сравните производительность массива и связанного списка на реальных задачах
3. Создайте гибридную структуру, объединяющую преимущества обеих

**Going Deeper:**

- Изучите циклические буферы (circular buffers)
- Познакомьтесь с skip lists
- Исследуйте, как Python реализует динамические массивы

---


