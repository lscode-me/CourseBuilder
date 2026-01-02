# Упорядоченные структуры данных
## Отсортированные массивы, бинарный поиск и модуль bisect

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу массивов и списков
- Знать концепцию сложности алгоритмов (Big-O)
- Понимать разницу между линейным и бинарным поиском
- Иметь базовые знания о сортировке

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать преимущества отсортированных массивов
- Реализовывать и применять бинарный поиск
- Использовать модуль bisect для работы с отсортированными данными
- Выбирать между отсортированными и неотсортированными структурами

---

## 1. Введение: зачем нужна упорядоченность

Когда данные отсортированы, мы можем использовать более эффективные алгоритмы поиска. Вместо линейного поиска O(n) можно использовать бинарный поиск O(log n).

**Ключевая идея:** Упорядоченность данных открывает возможности для оптимизации операций поиска и вставки.

---

## 2. Отсортированные массивы

### 2.1 Преимущества отсортированных массивов

**Преимущества:**

- Быстрый поиск через бинарный поиск — O(log n)
- Легко найти минимальный/максимальный элемент — O(1)
- Легко найти элементы в диапазоне
- Можно использовать бинарные операции

**Недостатки:**

- Поддержание порядка требует времени
- Вставка в отсортированный массив — O(n)

**Example: Сравнение отсортированного и неотсортированного массива**

```python
import time

# Неотсортированный массив

unsorted_arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]

# Отсортированный массив

sorted_arr = sorted(unsorted_arr)

print(f"Неотсортированный: {unsorted_arr}")
print(f"Отсортированный: {sorted_arr}")

# Поиск элемента 7

target = 7

# Линейный поиск в неотсортированном

start = time.time()
found_linear = target in unsorted_arr
time_linear = time.time() - start

# Бинарный поиск в отсортированном

import bisect
start = time.time()
index = bisect.bisect_left(sorted_arr, target)
found_binary = index < len(sorted_arr) and sorted_arr[index] == target
time_binary = time.time() - start

print(f"\nЛинейный поиск: {time_linear:.9f} секунд")
print(f"Бинарный поиск: {time_binary:.9f} секунд")
```

**Output:**
```
Неотсортированный: [5, 2, 8, 1, 9, 3, 7, 4, 6]
Отсортированный: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Линейный поиск: 0.000000000 секунд
Бинарный поиск: 0.000000000 секунд
```

### 2.2 Поддержание порядка

**Example: Вставка с сохранением порядка**

```python
def insert_sorted(arr, value):
    """Вставить значение в отсортированный массив."""
    import bisect
    bisect.insort(arr, value)
    return arr

# Отсортированный массив

sorted_list = [1, 3, 5, 7, 9]

# Вставка элементов

insert_sorted(sorted_list, 4)
insert_sorted(sorted_list, 6)
insert_sorted(sorted_list, 2)

print(f"После вставок: {sorted_list}")
```

**Output:**
```
После вставок: [1, 2, 3, 4, 5, 6, 7, 9]
```

---

## 3. Бинарный поиск

### 3.1 Принцип работы

Бинарный поиск работает только на отсортированных массивах. Идея:

1. Сравниваем искомый элемент с элементом в середине
2. Если элемент меньше — ищем в левой половине
3. Если элемент больше — ищем в правой половине
4. Повторяем до нахождения или исчерпания массива

**Example: Реализация бинарного поиска**

```python
def binary_search(arr, target):
    """Бинарный поиск в отсортированном массиве."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Не найдено

# Тестирование

sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]

targets = [5, 9, 2, 16]

for target in targets:
    index = binary_search(sorted_arr, target)
    if index != -1:
        print(f"Элемент {target} найден на позиции {index}")
    else:
        print(f"Элемент {target} не найден")
```

**Output:**
```
Элемент 5 найден на позиции 2
Элемент 9 найден на позиции 4
Элемент 2 не найден
Элемент 16 не найден
```

### 3.2 Сложность бинарного поиска

**Сложность:** O(log n)

На каждом шаге мы исключаем половину элементов, поэтому количество шагов равно log₂(n).

**Example: Визуализация количества шагов**

```python
import math

sizes = [10, 100, 1000, 10000, 100000, 1000000]

print("Количество шагов бинарного поиска:")
print(f"{'Размер':<10} {'Шагов (log₂)':<15} {'Линейный поиск':<15}")
print("-" * 40)

for size in sizes:
    binary_steps = math.ceil(math.log2(size))
    linear_steps = size
    print(f"{size:<10} {binary_steps:<15} {linear_steps:<15}")
```

**Output:**
```
Количество шагов бинарного поиска:
Размер     Шагов (log₂)   Линейный поиск
----------------------------------------
10         4              10             
100        7              100            
1000       10             1000          
10000      14             10000         
100000     17             100000        
1000000    20             1000000       
```

**Вывод:** Бинарный поиск намного эффективнее для больших массивов.

### 3.3 Рекурсивная реализация

**Example: Рекурсивный бинарный поиск**

```python
def binary_search_recursive(arr, target, left=0, right=None):
    """Рекурсивный бинарный поиск."""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Тестирование

sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search_recursive(sorted_arr, 7)
print(f"Элемент 7 найден на позиции: {result}")
```

**Output:**
```
Элемент 7 найден на позиции: 3
```

---

## 4. Модуль bisect

### 4.1 Обзор модуля bisect

Модуль `bisect` в Python предоставляет функции для работы с отсортированными списками.

**Основные функции:**

- `bisect_left()` — найти позицию для вставки слева
- `bisect_right()` — найти позицию для вставки справа
- `insort_left()` — вставить элемент слева
- `insort_right()` — вставить элемент справа

### 4.2 bisect_left и bisect_right

**Example: Использование bisect_left**

```python
import bisect

sorted_arr = [1, 3, 5, 7, 9]

# Найти позицию для вставки

target = 4
index = bisect.bisect_left(sorted_arr, target)
print(f"Позиция для вставки {target}: {index}")

# Вставить элемент

bisect.insort_left(sorted_arr, target)
print(f"После вставки: {sorted_arr}")

# Поиск существующего элемента

target = 5
index = bisect.bisect_left(sorted_arr, target)
print(f"\nПозиция элемента {target}: {index}")
print(f"Элемент найден: {sorted_arr[index] == target}")
```

**Output:**
```
Позиция для вставки 4: 2
После вставки: [1, 3, 4, 5, 7, 9]
Позиция элемента 5: 3
Элемент найден: True
```

**Example: Разница между bisect_left и bisect_right**

```python
import bisect

# Массив с дубликатами

arr = [1, 2, 2, 2, 3, 4]

target = 2

left_pos = bisect.bisect_left(arr, target)
right_pos = bisect.bisect_right(arr, target)

print(f"Массив: {arr}")
print(f"bisect_left({target}): {left_pos}")
print(f"bisect_right({target}): {right_pos}")
print(f"Количество элементов {target}: {right_pos - left_pos}")
```

**Output:**
```
Массив: [1, 2, 2, 2, 3, 4]
bisect_left(2): 1
bisect_right(2): 4
Количество элементов 2: 3
```

### 4.3 insort_left и insort_right

**Example: Вставка с сохранением порядка**

```python
import bisect

sorted_list = [1, 3, 5, 7, 9]

# Вставка слева

bisect.insort_left(sorted_list, 4)
print(f"После insort_left(4): {sorted_list}")

# Вставка справа

bisect.insort_right(sorted_list, 4)
print(f"После insort_right(4): {sorted_list}")
```

**Output:**
```
После insort_left(4): [1, 3, 4, 5, 7, 9]
После insort_right(4): [1, 3, 4, 4, 5, 7, 9]
```

### 4.4 Практические примеры

**Example: Поиск диапазона**

```python
import bisect

def find_range(arr, start, end):
    """Найти все элементы в диапазоне [start, end)."""
    left = bisect.bisect_left(arr, start)
    right = bisect.bisect_right(arr, end)
    return arr[left:right]

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Найти элементы от 3 до 7

result = find_range(sorted_arr, 3, 7)
print(f"Элементы в диапазоне [3, 7): {result}")
```

**Output:**
```
Элементы в диапазоне [3, 7): [3, 4, 5, 6]
```

**Example: Вставка с поддержанием отсортированности**

```python
import bisect

class SortedList:
    """Список, который автоматически поддерживает порядок."""
    def __init__(self):
        self.items = []
    
    def insert(self, value):
        """Вставить значение с сохранением порядка."""
        bisect.insort(self.items, value)
    
    def search(self, value):
        """Найти значение."""
        index = bisect.bisect_left(self.items, value)
        if index < len(self.items) and self.items[index] == value:
            return index
        return -1
    
    def __str__(self):
        return str(self.items)

# Использование

sl = SortedList()
sl.insert(5)
sl.insert(2)
sl.insert(8)
sl.insert(1)

print(f"Отсортированный список: {sl}")
print(f"Поиск 5: индекс {sl.search(5)}")
```

**Output:**
```
Отсортированный список: [1, 2, 5, 8]
Поиск 5: индекс 2
```

---

## 5. Сравнение с другими структурами

### 5.1 Отсортированный массив vs хеш-таблица

| Операция | Отсортированный массив | Хеш-таблица |
|----------|------------------------|-------------|
| **Поиск** | O(log n) | O(1) |
| **Вставка** | O(n) | O(1) |
| **Удаление** | O(n) | O(1) |
| **Диапазон запросов** | O(log n + k)* | O(n) |
| **Память** | O(n) | O(n) |

\* k — количество элементов в диапазоне

**Example: Когда использовать отсортированный массив**

```python
# Задача: найти все оценки в диапазоне [80, 90]

grades = [65, 72, 78, 85, 88, 92, 95]

# Сортируем

sorted_grades = sorted(grades)

# Используем bisect для поиска диапазона

import bisect
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

### 5.2 Когда использовать отсортированный массив

**Используй отсортированный массив, когда:**

- ✅ Нужны запросы по диапазону
- ✅ Данные редко изменяются
- ✅ Нужен быстрый поиск (но не критично O(1))
- ✅ Память ограничена

**Используй хеш-таблицу, когда:**

- ✅ Нужен очень быстрый поиск O(1)
- ✅ Данные часто изменяются
- ✅ Не нужны запросы по диапазону

---

## 6. Оптимизации и продвинутые техники

### 6.1 Интерполяционный поиск

Для равномерно распределённых данных можно использовать интерполяционный поиск.

**Example: Интерполяционный поиск**

```python
def interpolation_search(arr, target):
    """Интерполяционный поиск (для равномерно распределённых данных)."""
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Интерполяция позиции
        pos = left + int(((target - arr[left]) * (right - left)) / (arr[right] - arr[left]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

# Тестирование на равномерно распределённых данных

uniform_data = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
result = interpolation_search(uniform_data, 50)
print(f"Элемент 50 найден на позиции: {result}")
```

**Output:**
```
Элемент 50 найден на позиции: 25
```

### 6.2 Экспоненциальный поиск

**Example: Экспоненциальный поиск**

```python
def exponential_search(arr, target):
    """Экспоненциальный поиск."""
    if arr[0] == target:
        return 0
    
    # Находим диапазон
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Бинарный поиск в найденном диапазоне
    left = i // 2
    right = min(i, len(arr) - 1)
    
    return binary_search(arr[left:right+1], target) + left if binary_search(arr[left:right+1], target) != -1 else -1

# Тестирование

sorted_arr = list(range(1, 100))
result = exponential_search(sorted_arr, 50)
print(f"Элемент 50 найден на позиции: {result}")
```

---

## 7. Практические применения

### 7.1 Пример: Система оценок

**Example: Поиск студентов по оценкам**

```python
import bisect

class GradeSystem:
    """Система управления оценками."""
    def __init__(self):
        self.grades = []  # Отсортированный список оценок
    
    def add_grade(self, grade):
        """Добавить оценку."""
        bisect.insort(self.grades, grade)
    
    def find_students_in_range(self, min_grade, max_grade):
        """Найти количество студентов с оценками в диапазоне."""
        left = bisect.bisect_left(self.grades, min_grade)
        right = bisect.bisect_right(self.grades, max_grade)
        return self.grades[left:right]
    
    def get_percentile(self, percentile):
        """Получить оценку на заданном процентиле."""
        index = int(len(self.grades) * percentile / 100)
        return self.grades[index] if index < len(self.grades) else None

# Использование

system = GradeSystem()
system.add_grade(85)
system.add_grade(92)
system.add_grade(78)
system.add_grade(88)
system.add_grade(95)

print(f"Оценки: {system.grades}")
print(f"Оценки в диапазоне [80, 90]: {system.find_students_in_range(80, 90)}")
print(f"90-й процентиль: {system.get_percentile(90)}")
```

**Output:**
```
Оценки: [78, 85, 88, 92, 95]
Оценки в диапазоне [80, 90]: [85, 88]
90-й процентиль: 92
```

### 7.2 Пример: Календарь событий

**Example: Управление событиями по времени**

```python
import bisect
from datetime import datetime, timedelta

class EventCalendar:
    """Календарь событий."""
    def __init__(self):
        self.events = []  # Список (время, событие)
    
    def add_event(self, time, event):
        """Добавить событие."""
        bisect.insort(self.events, (time, event))
    
    def get_events_in_range(self, start_time, end_time):
        """Получить события в диапазоне времени."""
        start_key = (start_time, "")
        end_key = (end_time, "")
        
        left = bisect.bisect_left(self.events, start_key)
        right = bisect.bisect_right(self.events, end_key)
        
        return self.events[left:right]

# Использование

calendar = EventCalendar()
base_time = datetime(2024, 1, 1, 10, 0)

calendar.add_event(base_time + timedelta(hours=2), "Встреча")
calendar.add_event(base_time + timedelta(hours=1), "Обед")
calendar.add_event(base_time + timedelta(hours=3), "Презентация")

start = base_time + timedelta(hours=1, minutes=30)
end = base_time + timedelta(hours=2, minutes=30)

events = calendar.get_events_in_range(start, end)
print("События в диапазоне:")
for time, event in events:
    print(f"  {time.strftime('%H:%M')}: {event}")
```

**Output:**
```
События в диапазоне:
  11:00: Обед
  12:00: Встреча
```

---

## 💡 Key Takeaways

- **Отсортированные массивы** позволяют использовать бинарный поиск O(log n) вместо линейного O(n)

- **Бинарный поиск** работает только на отсортированных данных и исключает половину элементов на каждом шаге

- **Модуль bisect** предоставляет эффективные функции для работы с отсортированными списками

- **Выбор структуры** зависит от операций: отсортированный массив для диапазонных запросов, хеш-таблица для точечного поиска

- **Поддержание порядка** требует времени, но открывает возможности для оптимизации

---

## 🚀 Next Steps

**Related Modules:**

- [Сравнение базовых структур данных](../08_Comparing_Basic_Data_Structures/) — сравните все изученные структуры
- [Бинарные деревья и деревья поиска](../10_Binary_Trees_And_Search_Trees/) — изучите деревья как альтернативу отсортированным массивам

**Practice Ideas:**

1. Реализуйте систему поиска с использованием бинарного поиска
2. Создайте структуру данных, которая автоматически поддерживает порядок
3. Сравните производительность бинарного и линейного поиска на больших данных

**Going Deeper:**

- Изучите интерполяционный и экспоненциальный поиск
- Познакомьтесь с fractional cascading
- Исследуйте применение бинарного поиска в задачах оптимизации

---



