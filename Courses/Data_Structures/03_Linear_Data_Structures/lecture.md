# Линейные структуры данных
## Массивы, списки, стеки, очереди и деки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основные характеристики структур данных (из предыдущей лекции)
- Знать базовый синтаксис Python
- Понимать концепцию индексации и итерации

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать массивы и связанные списки и понимать их компромиссы
- Реализовывать и использовать стек для решения задач
- Применять очередь и дек в практических сценариях
- Выбирать подходящую линейную структуру данных для конкретной задачи

---

## 1. Введение: что такое линейные структуры данных

**Линейные структуры данных** — это структуры, в которых элементы расположены последовательно, один за другим. Каждый элемент (кроме первого и последнего) имеет ровно одного предшественника и одного преемника.

Основные типы линейных структур:

- **Массивы** — элементы хранятся в непрерывной области памяти

- **Связанные списки** — элементы связаны через указатели

- **Стек** — LIFO (Last In, First Out)

- **Очередь** — FIFO (First In, First Out)

- **Дек** — двойная очередь, элементы можно добавлять/удалять с обоих концов

---

## 2. Массивы (Arrays)

### 2.1 Что такое массив

**Массив** — это структура данных, которая хранит элементы в непрерывной области памяти. Каждый элемент имеет индекс, по которому к нему можно обратиться напрямую.

### 2.2 Массивы в Python

В Python нет встроенного типа "массив" в классическом понимании, но список (`list`) ведёт себя похоже на динамический массив.

**Example: Базовые операции с массивом (списком)**

```python
# Создание массива (списка)
numbers = [10, 20, 30, 40, 50]
print(f"Исходный массив: {numbers}")

# Доступ по индексу
print(f"Элемент с индексом 2: {numbers[2]}")

# Изменение элемента

numbers[1] = 25
print(f"После изменения: {numbers}")

# Длина массива
print(f"Длина массива: {len(numbers)}")
```

**Output:**
```

Исходный массив: [10, 20, 30, 40, 50]
Элемент с индексом 2: 30
После изменения: [10, 25, 30, 40, 50]
Длина массива: 5
```

### 2.3 Преимущества массивов

**Преимущества:**

- Прямой доступ по индексу — O(1)
- Эффективное использование памяти (элементы расположены рядом)
- Кэш-локальность (быстрый доступ благодаря локальности данных)

**Example: Кэш-локальность**

```python

import time

# Создаём большой список
large_list = list(range(1000000))

# Доступ к последовательным элементам (хорошая локальность)
start = time.time()
sum_seq = sum(large_list[i] for i in range(0, 10000, 1))
time_seq = time.time() - start

# Доступ к случайным элементам (плохая локальность)
import random
indices = random.sample(range(1000000), 10000)
start = time.time()
sum_random = sum(large_list[i] for i in indices)
time_random = time.time() - start

print(f"Последовательный доступ: {time_seq:.6f} секунд")
print(f"Случайный доступ: {time_random:.6f} секунд")
print(f"Разница: {time_random / time_seq:.2f}x медленнее")
```

**Output:**
```

Последовательный доступ: 0.001234 секунд
Случайный доступ: 0.002456 секунд
Разница: 1.99x медленнее
```

### 2.4 Недостатки массивов

**Недостатки:**

- Вставка/удаление в середину — O(n)
- Фиксированный размер (в классических массивах)
- Неэффективное использование памяти при частых изменениях размера

---

## 3. Связанные списки (Linked Lists)

### 3.1 Что такое связанный список

**Связанный список** — это структура данных, в которой элементы (узлы) связаны через указатели. Каждый узел содержит данные и ссылку на следующий узел.

### 3.2 Реализация связанного списка

**Example: Базовый связанный список**

```python

class Node:
    """Узел связанного списка."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Простой связанный список."""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Добавить элемент в конец."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
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
ll.append(10)
ll.append(20)
ll.append(30)
print(f"Связанный список: {ll.display()}")
```

**Output:**
```

Связанный список: [10, 20, 30]
```

### 3.3 Преимущества связанных списков

**Преимущества:**

- Вставка/удаление в начало — O(1)
- Динамический размер (легко добавлять/удалять элементы)
- Не требует непрерывной области памяти

**Example: Быстрая вставка в начало**

```python

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        """Добавить элемент в начало — O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

ll = LinkedList()
ll.prepend(30)
ll.prepend(20)
ll.prepend(10)
print(f"После prepend: {ll.display()}")
```

**Output:**
```

После prepend: [10, 20, 30]
```

### 3.4 Недостатки связанных списков

**Недостатки:**

- Доступ по индексу — O(n)
- Нет кэш-локальности (узлы разбросаны в памяти)
- Дополнительная память на указатели

---

## 4. Стек (Stack)

### 4.1 Что такое стек

**Стек** — это структура данных, работающая по принципу LIFO (Last In, First Out — последним пришёл, первым ушёл). Элементы добавляются и удаляются только с одного конца (вершины стека).

### 4.2 Операции стека

Основные операции:

- `push(item)` — добавить элемент на вершину
- `pop()` — удалить и вернуть элемент с вершины
- `peek()` или `top()` — посмотреть элемент на вершине
- `is_empty()` — проверить, пуст ли стек
- `size()` — получить размер стека

**Example: Реализация стека**

```python

class Stack:
    """Реализация стека через список."""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Добавить элемент на вершину стека."""
        self.items.append(item)
    
    def pop(self):
        """Удалить и вернуть элемент с вершины."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()
    
    def peek(self):
        """Посмотреть элемент на вершине."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]
    
    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self.items) == 0
    
    def size(self):
        """Получить размер стека."""
        return len(self.items)

# Использование
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Вершина стека: {stack.peek()}")
print(f"Размер: {stack.size()}")

# Извлечение элементов
print(f"Извлечено: {stack.pop()}")
print(f"Извлечено: {stack.pop()}")
print(f"Осталось: {stack.size()}")
```

**Output:**
```

Вершина стека: 3
Размер: 3
Извлечено: 3
Извлечено: 2
Осталось: 1
```

### 4.3 Применение стека

**Примеры использования:**

- Отслеживание вызовов функций (call stack)
- Обработка выражений (проверка скобок, вычисление выражений)
- Отмена операций (undo)
- Обход графов (DFS)

**Example: Проверка правильности скобок**

```python

def is_balanced(expression):
    """Проверить, правильно ли расставлены скобки."""
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()

# Тестирование

test_cases = [
    "()",
    "()[]{}",
    "([{}])",
    "([)]",
    "((("
]

for expr in test_cases:
    result = is_balanced(expr)
    print(f"'{expr}': {'✓' if result else '✗'}")
```

**Output:**
```

'()': ✓
'()[]{}': ✓
'([{}])': ✓
'([)]': ✗
'(((': ✗
```

---

## 5. Очередь (Queue)

### 5.1 Что такое очередь

**Очередь** — это структура данных, работающая по принципу FIFO (First In, First Out — первым пришёл, первым ушёл). Элементы добавляются в конец (rear) и удаляются из начала (front).

### 5.2 Операции очереди

Основные операции:

- `enqueue(item)` — добавить элемент в конец
- `dequeue()` — удалить и вернуть элемент из начала
- `front()` или `peek()` — посмотреть элемент в начале
- `is_empty()` — проверить, пуста ли очередь
- `size()` — получить размер очереди

**Example: Реализация очереди**

```python

from collections import deque

class Queue:
    """Реализация очереди через deque."""
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Добавить элемент в конец очереди."""
        self.items.append(item)
    
    def dequeue(self):
        """Удалить и вернуть элемент из начала."""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()
    
    def front(self):
        """Посмотреть элемент в начале."""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]
    
    def is_empty(self):
        """Проверить, пуста ли очередь."""
        return len(self.items) == 0
    
    def size(self):
        """Получить размер очереди."""
        return len(self.items)

# Использование

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Передний элемент: {queue.front()}")
print(f"Размер: {queue.size()}")

# Извлечение элементов

print(f"Извлечено: {queue.dequeue()}")
print(f"Извлечено: {queue.dequeue()}")
print(f"Осталось: {queue.size()}")
```

**Output:**
```

Передний элемент: 1
Размер: 3
Извлечено: 1
Извлечено: 2
Осталось: 1
```

### 5.3 Применение очереди

**Примеры использования:**

- Обработка задач (task queue)
- BFS (обход графа в ширину)
- Буферизация данных
- Планировщик процессов

**Example: Симуляция очереди задач**

```python

class TaskQueue:
    """Очередь задач."""
    def __init__(self):
        self.queue = Queue()
    
    def add_task(self, task_name):
        """Добавить задачу."""
        self.queue.enqueue(task_name)
        print(f"Добавлена задача: {task_name}")
    
    def process_next(self):
        """Обработать следующую задачу."""
        if not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Обрабатывается: {task}")
            return task
        else:
            print("Очередь пуста")
            return None

# Симуляция
task_queue = TaskQueue()
task_queue.add_task("Задача 1")
task_queue.add_task("Задача 2")
task_queue.add_task("Задача 3")

task_queue.process_next()
task_queue.process_next()
task_queue.process_next()
task_queue.process_next()
```

**Output:**
```

Добавлена задача: Задача 1
Добавлена задача: Задача 2
Добавлена задача: Задача 3
Обрабатывается: Задача 1
Обрабатывается: Задача 2
Обрабатывается: Задача 3
Очередь пуста
```

---

## 6. Дек (Deque - Double-Ended Queue)

### 6.1 Что такое дек

**Дек** (double-ended queue) — это структура данных, которая позволяет добавлять и удалять элементы с обоих концов. Это комбинация стека и очереди.

### 6.2 Операции дека

Основные операции:

- `append(item)` — добавить в конец
- `appendleft(item)` — добавить в начало
- `pop()` — удалить и вернуть с конца
- `popleft()` — удалить и вернуть с начала
- `peek()` — посмотреть элемент

**Example: Использование deque в Python**

```python

from collections import deque

# Создание дека

d = deque([1, 2, 3])
print(f"Исходный дек: {d}")

# Добавление элементов
d.append(4)  # В конец
d.appendleft(0)  # В начало
print(f"После добавления: {d}")

# Удаление элементов

print(f"Удалён с конца: {d.pop()}")
print(f"Удалён с начала: {d.popleft()}")
print(f"Итоговый дек: {d}")
```

**Output:**
```

Исходный дек: deque([1, 2, 3])
После добавления: deque([0, 1, 2, 3, 4])
Удалён с конца: 4
Удалён с начала: 0
Итоговый дек: deque([1, 2, 3])
```

### 6.3 Преимущества дека

**Преимущества:**

- Гибкость: можно работать с обоих концов
- Эффективные операции: O(1) для добавления/удаления с обоих концов
- Можно использовать как стек или очередь

**Example: Дек как стек**

```python

from collections import deque

# Использование дека как стека
stack = deque()
stack.append(1)  # push
stack.append(2)
stack.append(3)

print(f"Вершина стека: {stack[-1]}")
print(f"Извлечено: {stack.pop()}")  # pop
print(f"Осталось: {list(stack)}")
```

**Output:**
```

Вершина стека: 3
Извлечено: 3
Осталось: [1, 2]
```

**Example: Дек как очередь**

```python

from collections import deque

# Использование дека как очереди
queue = deque()
queue.append(1)  # enqueue
queue.append(2)
queue.append(3)

print(f"Передний элемент: {queue[0]}")
print(f"Извлечено: {queue.popleft()}")  # dequeue
print(f"Осталось: {list(queue)}")
```

**Output:**
```

Передний элемент: 1
Извлечено: 1
Осталось: [2, 3]
```

---

## 7. Сравнение линейных структур

### 7.1 Сводная таблица

| Структура | Доступ | Вставка (начало) | Вставка (конец) | Удаление (начало) | Удаление (конец) |
|-----------|--------|------------------|-----------------|-------------------|------------------|
| **Массив/Список** | O(1) | O(n) | O(1)* | O(n) | O(1) |
| **Связанный список** | O(n) | O(1) | O(n) | O(1) | O(n) |
| **Стек** | N/A | N/A | O(1) | N/A | O(1) |
| **Очередь** | N/A | N/A | O(1) | O(1) | N/A |
| **Дек** | N/A | O(1) | O(1) | O(1) | O(1) |

\* Амортизированная сложность

### 7.2 Когда что использовать

**Используй массив/список, когда:**

- Нужен прямой доступ по индексу
- Часто обращаешься к элементам по позиции
- Элементы добавляются/удаляются в основном в конце

**Используй связанный список, когда:**

- Часто вставляешь/удаляешь в начале
- Размер данных часто меняется
- Не нужен прямой доступ по индексу

**Используй стек, когда:**

- Нужен LIFO порядок
- Отслеживание вызовов функций
- Обработка выражений

**Используй очередь, когда:**

- Нужен FIFO порядок
- Обработка задач по порядку
- BFS обход графа

**Используй дек, когда:**

- Нужна гибкость работы с обоих концов
- Комбинация операций стека и очереди

---

## 8. Практические примеры

### 8.1 Пример: Обработка истории браузера

**Example: Навигация назад/вперёд**

```python

class BrowserHistory:
    """История браузера с навигацией назад/вперёд."""
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = None
    
    def visit(self, url):
        """Посетить URL."""
        if self.current:
            self.back_stack.push(self.current)
        self.current = url
        # Очищаем стек вперёд при новом посещении
        self.forward_stack = Stack()
        print(f"Посещён: {url}")
    
    def back(self):
        """Назад."""
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()
            print(f"Назад к: {self.current}")
            return self.current
        print("Нельзя идти назад")
        return None
    
    def forward(self):
        """Вперёд."""
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current)
            self.current = self.forward_stack.pop()
            print(f"Вперёд к: {self.current}")
            return self.current
        print("Нельзя идти вперёд")
        return None

# Симуляция

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("github.com")
browser.visit("stackoverflow.com")

browser.back()
browser.back()
browser.forward()
```

**Output:**
```

Посещён: google.com
Посещён: github.com
Посещён: stackoverflow.com
Назад к: github.com
Назад к: google.com
Вперёд к: github.com
```

### 8.2 Пример: Обработка принтера

**Example: Очередь печати**

```python

class PrintQueue:
    """Очередь печати документов."""
    def __init__(self):
        self.queue = Queue()
    
    def add_document(self, doc_name):
        """Добавить документ в очередь."""
        self.queue.enqueue(doc_name)
        print(f"Добавлен в очередь: {doc_name} (позиция: {self.queue.size()})")
    
    def print_next(self):
        """Распечатать следующий документ."""
        if not self.queue.is_empty():
            doc = self.queue.dequeue()
            print(f"Печатается: {doc}")
            return doc
        print("Очередь печати пуста")
        return None

# Симуляция
printer = PrintQueue()
printer.add_document("Документ1.pdf")
printer.add_document("Документ2.pdf")
printer.add_document("Документ3.pdf")

printer.print_next()
printer.print_next()
printer.print_next()
printer.print_next()
```

**Output:**
```

Добавлен в очередь: Документ1.pdf (позиция: 1)
Добавлен в очередь: Документ2.pdf (позиция: 2)
Добавлен в очередь: Документ3.pdf (позиция: 3)
Печатается: Документ1.pdf
Печатается: Документ2.pdf
Печатается: Документ3.pdf
Очередь печати пуста
```

---

## 💡 Key Takeaways

- **Массивы** обеспечивают быстрый доступ по индексу, но вставка/удаление в середину дорогие

- **Связанные списки** позволяют быстро вставлять/удалять в начале, но доступ по индексу медленный

- **Стек** (LIFO) идеален для задач, требующих обратного порядка обработки

- **Очередь** (FIFO) подходит для задач, требующих обработки в порядке поступления

- **Дек** объединяет преимущества стека и очереди, обеспечивая гибкость работы с обоих концов

---

## 🚀 Next Steps

**Related Modules:**

- [Встроенные структуры данных Python](../04_Builtin_Python_Data_Structures/) — изучите встроенные структуры Python
- [Массивы и связанные списки](../05_Arrays_And_Linked_Lists/) — углубитесь в детали массивов и списков

**Practice Ideas:**

1. Реализуйте стек для вычисления выражений в обратной польской нотации
2. Создайте систему очередей для обработки задач с приоритетами
3. Реализуйте связанный список с операциями вставки и удаления

**Going Deeper:**

- Изучите циклические буферы (circular buffers)
- Познакомьтесь с двусвязными списками (doubly linked lists)
- Исследуйте реализацию deque в Python

---



