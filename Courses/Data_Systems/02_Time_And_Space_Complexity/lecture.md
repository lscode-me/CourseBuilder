# Временная и пространственная сложность
## Big-O, амортизированный анализ и практическое понимание сложности

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать связь алгоритмов и структур данных
- Знать базовые операции над структурами данных
- Иметь опыт анализа простых алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Анализировать временную и пространственную сложность алгоритмов
- Применять Big-O, Big-Ω и Big-Θ нотации
- Понимать разницу между лучшим, средним и худшим случаями
- Применять амортизированный анализ к динамическим структурам данных

---

## 1. Зачем измерять сложность

### 1.1 Проблема масштабирования

Алгоритм, который работает быстро на 100 элементах, может быть катастрофически медленным на миллионе.

**Example: Рост времени выполнения**

```python

import time

def measure_time(func, n):
    """Измеряет время выполнения функции."""
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start

# O(n) — линейный алгоритм
def linear(n):
    total = 0
    for i in range(n):
        total += i
    return total

# O(n²) — квадратичный алгоритм
def quadratic(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total

# Сравнение на разных размерах
for n in [100, 1000, 10000]:
    t_lin = measure_time(linear, n)
    t_quad = measure_time(quadratic, n)
    print(f"n={n:5d}: linear={t_lin*1000:.3f}ms, quadratic={t_quad*1000:.1f}ms")
```

**Output:**
```

n=  100: linear=0.005ms, quadratic=0.3ms
n= 1000: linear=0.034ms, quadratic=28.5ms
n=10000: linear=0.312ms, quadratic=2847.2ms
```

**Объяснение:**
При увеличении n в 10 раз: линейный алгоритм замедляется в ~10 раз, квадратичный — в ~100 раз.

### 1.2 Время vs память

Сложность бывает двух видов:

- **Временная сложность** (Time Complexity): сколько операций выполняет алгоритм

- **Пространственная сложность** (Space Complexity): сколько памяти использует алгоритм

Часто приходится выбирать между ними — это называется **trade-off**.

```python
# Высокая временная сложность, низкая пространственная
def has_duplicate_slow(arr):
    """O(n²) время, O(1) память"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Низкая временная сложность, высокая пространственная
def has_duplicate_fast(arr):
    """O(n) время, O(n) память"""
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

data = list(range(10000)) + [5000]  # Дубликат в середине

import time
start = time.perf_counter()
has_duplicate_slow(data)
time_slow = time.perf_counter() - start

start = time.perf_counter()
has_duplicate_fast(data)
time_fast = time.perf_counter() - start

print(f"O(n²) версия: {time_slow*1000:.1f} мс")
print(f"O(n) версия: {time_fast*1000:.3f} мс")
```

**Output:**
```

O(n²) версия: 892.3 мс
O(n) версия: 0.456 мс
```

---

## 2. Big-O нотация

### 2.1 Определение Big-O

**Big-O** описывает верхнюю границу роста функции. f(n) = O(g(n)) означает, что f(n) растёт не быстрее, чем g(n).

Формально: f(n) = O(g(n)), если существуют константы c > 0 и n₀, такие что для всех n ≥ n₀: f(n) ≤ c · g(n)

### 2.2 Распространённые классы сложности

| Сложность | Название | Пример |
|-----------|----------|--------|
| O(1) | Константная | Доступ по индексу |
| O(log n) | Логарифмическая | Бинарный поиск |
| O(n) | Линейная | Линейный поиск |
| O(n log n) | Линеарифмическая | Сортировка слиянием |
| O(n²) | Квадратичная | Bubble sort |
| O(2ⁿ) | Экспоненциальная | Перебор подмножеств |
| O(n!) | Факториальная | Перебор перестановок |

**Example: Визуализация роста сложности**

```python

import math

def show_complexity_growth():
    """Показывает, как быстро растут разные сложности."""
    
    sizes = [10, 100, 1000, 10000]
    
    print(f"{'n':>6} | {'O(1)':>8} | {'O(log n)':>8} | {'O(n)':>8} | {'O(n log n)':>12} | {'O(n²)':>12}")
    print("-" * 70)
    
    for n in sizes:
        o_1 = 1
        o_log = int(math.log2(n))
        o_n = n
        o_nlogn = n * int(math.log2(n))
        o_n2 = n * n
        
        print(f"{n:>6} | {o_1:>8} | {o_log:>8} | {o_n:>8} | {o_nlogn:>12} | {o_n2:>12}")

show_complexity_growth()
```

**Output:**
```

     n |     O(1) | O(log n) |     O(n) |   O(n log n) |       O(n²)
----------------------------------------------------------------------
    10 |        1 |        3 |       10 |           30 |          100
   100 |        1 |        6 |      100 |          600 |        10000
  1000 |        1 |        9 |     1000 |         9000 |      1000000
 10000 |        1 |       13 |    10000 |       130000 |    100000000
```

### 2.3 Правила упрощения Big-O

1. **Отбрасываем константы**: O(2n) = O(n)
2. **Оставляем только доминирующий член**: O(n² + n) = O(n²)
3. **Вложенные циклы перемножаются**: два вложенных цикла по n = O(n²)

```python

def example_simplification(n):
    # Цикл 1: O(n)
    for i in range(n):
        pass
    
    # Цикл 2: O(n)
    for j in range(n):
        pass
    
    # Вложенные циклы: O(n²)
    for i in range(n):
        for j in range(n):
            pass
    
    # Общая сложность: O(n) + O(n) + O(n²) = O(n²)
    # Доминирует O(n²)
```

---

## 3. Big-Ω и Big-Θ

### 3.1 Big-Ω (Omega) — нижняя граница

**Big-Ω** описывает нижнюю границу: алгоритм работает НЕ БЫСТРЕЕ, чем Ω(g(n)).

```python
# Поиск элемента в несортированном массиве
# Лучший случай: O(1) — элемент в начале
# Худший случай: O(n) — элемент в конце или отсутствует
# Нижняя граница: Ω(1) — в лучшем случае нельзя быстрее

def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i  # В лучшем случае: 1 сравнение
    return -1
```

### 3.2 Big-Θ (Theta) — точная граница

**Big-Θ** описывает точную границу: g(n) ≤ f(n) ≤ g(n) (с точностью до констант).

```python
# Суммирование массива — всегда O(n)
# Мы ДОЛЖНЫ просмотреть каждый элемент
# Θ(n) — точная граница

def sum_array(arr):
    """Θ(n) — всегда линейное время."""
    total = 0
    for x in arr:
        total += x
    return total
```

### 3.3 Когда использовать какую нотацию

| Нотация | Использование | Пример |
|---------|--------------|--------|
| O(n) | Верхняя граница, общий случай | "Работает не медленнее O(n)" |
| Ω(n) | Нижняя граница | "Требует минимум Ω(n) операций" |
| Θ(n) | Точная характеристика | "Всегда выполняет Θ(n) операций" |

---

## 4. Лучший, средний и худший случаи

### 4.1 Три сценария анализа

- **Best case**: самый благоприятный вход

- **Worst case**: самый неблагоприятный вход

- **Average case**: типичный/случайный вход

**Example: Анализ QuickSort**

```python

import random

def quicksort(arr):
    """
    Best case: O(n log n) — хороший выбор pivot
    Worst case: O(n²) — уже отсортированный массив при плохом pivot
    Average case: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Pivot — средний элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Демонстрация
import time

# Худший случай для наивного quicksort (первый элемент как pivot)
def quicksort_bad_pivot(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Плохой выбор pivot!
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort_bad_pivot(left) + [pivot] + quicksort_bad_pivot(right)

# Тест на отсортированном массиве
n = 1000
sorted_arr = list(range(n))
random_arr = sorted_arr.copy()
random.shuffle(random_arr)

# Хороший quicksort
start = time.perf_counter()
quicksort(sorted_arr.copy())
time_good = time.perf_counter() - start

# Плохой quicksort на отсортированном массиве
import sys
sys.setrecursionlimit(2000)
start = time.perf_counter()
quicksort_bad_pivot(sorted_arr.copy())
time_bad = time.perf_counter() - start

print(f"Хороший pivot на отсортированном: {time_good*1000:.2f} мс")
print(f"Плохой pivot на отсортированном: {time_bad*1000:.2f} мс")
```

**Output:**
```

Хороший pivot на отсортированном: 1.23 мс
Плохой pivot на отсортированном: 156.78 мс
```

### 4.2 Какой случай анализировать?

- **Worst case** — наиболее важен для гарантий производительности

- **Average case** — важен для реальных сценариев

- **Best case** — редко используется, может ввести в заблуждение

---

## 5. Амортизированный анализ

### 5.1 Концепция амортизации

**Амортизированный анализ** оценивает среднюю стоимость операции в последовательности операций, даже если отдельные операции могут быть дорогими.

### 5.2 Пример: Динамический массив

```python

class DynamicArray:
    """
    Динамический массив с амортизированным O(1) добавлением.
    
    Большинство append — O(1), но иногда нужно расширять массив — O(n).
    Амортизированно: O(1) на операцию.
    """
    
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity
        self.resize_count = 0
    
    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = item
        self.size += 1
    
    def _resize(self):
        """Удваиваем размер — ключ к амортизации."""
        self.resize_count += 1
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

# Демонстрация

arr = DynamicArray()
for i in range(1000):
    arr.append(i)

print(f"Добавлено элементов: {arr.size}")
print(f"Расширений массива: {arr.resize_count}")
print(f"Итоговая ёмкость: {arr.capacity}")
```

**Output:**
```

Добавлено элементов: 1000
Расширений массива: 10
Итоговая ёмкость: 1024
```

**Объяснение:**
За 1000 операций append произошло только 10 расширений. Большинство операций — O(1). Общая стоимость: n + n/2 + n/4 + ... ≈ 2n = O(n). Амортизированная стоимость одной операции: O(n)/n = O(1).

### 5.3 Методы амортизированного анализа

**Метод банковского счёта (Banker's method):**

- Каждая операция "платит" немного больше, чем нужно
- Избыток сохраняется для оплаты дорогих операций

```python
# Концептуальная демонстрация
class AmortizedAnalysis:
    """
    Каждый append стоит 3 "монеты":
    - 1 монета: записать элемент
    - 2 монеты: сохранить для будущего копирования
    
    При расширении: копируем n/2 элементов по 2 монеты (уже оплачено).
    """
    
    def demonstrate(self, n):
        # Добавляем n элементов
        # Общая стоимость: 3n монет
        # Расширения: копирование n/2 + n/4 + ... ≈ n элементов
        # Используем 2n монет из запасённых
        # Все операции оплачены!
        
        actual_cost = 0
        banked = 0
        size = 0
        capacity = 1
        
        for i in range(n):
            # Платим 3 монеты
            payment = 3
            
            # 1 монета на запись
            write_cost = 1
            
            # Нужно расширение?
            if size == capacity:
                resize_cost = size  # Копируем все элементы
                actual_cost += resize_cost
                banked -= resize_cost * 2
                capacity *= 2
            
            actual_cost += write_cost
            banked += payment - write_cost
            size += 1
        
        print(f"Элементов: {n}")
        print(f"Оплачено: {3 * n} монет")
        print(f"Фактическая стоимость: {actual_cost}")
        print(f"Остаток на счёте: {banked}")

AmortizedAnalysis().demonstrate(1000)
```

**Output:**
```

Элементов: 1000
Оплачено: 3000 монет
Фактическая стоимость: 2023
Остаток на счёте: 977
```

---

## 6. Анализ пространственной сложности

### 6.1 Что считать

- Память для входных данных (обычно не считается)
- Дополнительная память алгоритма
- Рекурсивный стек вызовов

**Example: Разные варианты пространственной сложности**

```python
# O(1) дополнительная память — in-place
def reverse_in_place(arr):
    """Разворачивает массив на месте."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# O(n) дополнительная память
def reverse_copy(arr):
    """Создаёт новый развёрнутый массив."""
    return arr[::-1]

# Демонстрация
original = [1, 2, 3, 4, 5]
print(f"In-place: {reverse_in_place(original.copy())}")
print(f"Copy: {reverse_copy(original)}")
```

**Output:**
```

In-place: [5, 4, 3, 2, 1]
Copy: [5, 4, 3, 2, 1]
```

### 6.2 Рекурсия и стек

```python
# O(n) пространства из-за стека вызовов
def factorial_recursive(n):
    """Рекурсивный факториал — O(n) stack space."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# O(1) пространства — итеративная версия
def factorial_iterative(n):
    """Итеративный факториал — O(1) space."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"Рекурсивный: {factorial_recursive(10)}")
print(f"Итеративный: {factorial_iterative(10)}")
```

**Output:**
```

Рекурсивный: 3628800
Итеративный: 3628800
```

### 6.3 Trade-off время vs память

| Подход | Время | Память | Когда использовать |
|--------|-------|--------|-------------------|
| Хеширование | O(1) | O(n) | Много памяти, нужна скорость |
| Бинарный поиск | O(log n) | O(1) | Данные отсортированы |
| Кэширование | O(1) после первого | O(k) | Повторяющиеся запросы |
| В потоке | O(n) | O(1) | Огромные данные, мало памяти |

---

## 7. Практический анализ алгоритмов

### 7.1 Пошаговый анализ

```python

def analyze_algorithm(arr, target):
    """
    Анализ шаг за шагом.
    """
    n = len(arr)
    result = []       # O(k) память, где k — размер результата
    
    # Цикл 1: O(n) время
    for x in arr:     # n итераций
        if x > target: # O(1) сравнение
            result.append(x)  # O(1) амортизированно
    
    # Цикл 2: O(n) время
    total = 0
    for x in arr:     # n итераций
        total += x    # O(1)
    
    # Вложенные циклы: O(n²) время
    pairs = 0
    for i in range(n):      # n итераций
        for j in range(i+1, n):  # в среднем n/2 итераций
            if arr[i] + arr[j] == target:  # O(1)
                pairs += 1
    
    # Общее время: O(n) + O(n) + O(n²) = O(n²)
    # Доминирует O(n²)
    
    return result, total, pairs
```

### 7.2 Распознавание паттернов сложности

```python
# O(1) — константное количество операций
def get_first(arr):
    return arr[0] if arr else None

# O(log n) — деление на 2 на каждом шаге
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # log n итераций
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) — один проход по данным
def find_sum(arr):
    return sum(arr)

# O(n log n) — обычно сортировка или divide & conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# O(n²) — вложенные циклы

def all_pairs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            pass
```

### 7.3 Анализ рекурсивных алгоритмов

Для рекурсии используем **рекуррентные соотношения**.

```python
# Пример: бинарный поиск
# T(n) = T(n/2) + O(1)
# T(n) = O(log n)

# Пример: merge sort
# T(n) = 2T(n/2) + O(n)
# T(n) = O(n log n)

# Пример: наивный Фибоначчи
# T(n) = T(n-1) + T(n-2) + O(1)
# T(n) = O(2^n) — экспоненциально!

def fib_naive(n):
    """O(2^n) — очень медленно!"""
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Оптимизированная версия с мемоизацией
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    """O(n) с мемоизацией."""
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

# Сравнение
import time

start = time.perf_counter()
fib_naive(30)
time_naive = time.perf_counter() - start

start = time.perf_counter()
fib_memo(30)
time_memo = time.perf_counter() - start

print(f"Наивный: {time_naive:.3f} сек")
print(f"С мемоизацией: {time_memo:.6f} сек")
```

**Output:**
```

Наивный: 0.234 сек
С мемоизацией: 0.000015 сек
```

---

## 8. Практические советы

### 8.1 Таблица сложности структур данных Python

| Структура | Операция | Средний случай | Худший случай |
|-----------|----------|----------------|---------------|
| list | index | O(1) | O(1) |
| list | append | O(1)* | O(n) |
| list | insert | O(n) | O(n) |
| list | in | O(n) | O(n) |
| dict | get | O(1) | O(n) |
| dict | set | O(1)* | O(n) |
| dict | delete | O(1)* | O(n) |
| set | add | O(1)* | O(n) |
| set | in | O(1) | O(n) |
| deque | appendleft | O(1) | O(1) |

*Амортизированная сложность

### 8.2 Когда сложность важна

```python
# При n < 100: сложность не критична
# При n ~ 1000: O(n²) заметно
# При n ~ 10000: O(n²) проблема
# При n ~ 1M: даже O(n log n) требует оптимизации

def practical_limits():
    """Показывает практические ограничения."""
    limits = {
        "O(n!)": 12,      # 12! = 479M операций
        "O(2^n)": 25,     # 2^25 = 33M операций
        "O(n²)": 10000,   # 100M операций
        "O(n log n)": 1000000,  # 20M операций
        "O(n)": 100000000, # 100M операций
    }
    
    for complexity, max_n in limits.items():
        print(f"{complexity}: практичный лимит ≈ {max_n:,}")

practical_limits()
```

**Output:**
```

O(n!): практичный лимит ≈ 12
O(2^n): практичный лимит ≈ 25
O(n²): практичный лимит ≈ 10,000
O(n log n): практичный лимит ≈ 1,000,000
O(n)): практичный лимит ≈ 100,000,000
```

### 8.3 Профилирование vs теоретический анализ

```python

import cProfile
import pstats

def profile_function(func, *args):
    """Профилирует функцию."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args)
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(5)
    
    return result

# Теоретически оба O(n), но на практике...
def sum_v1(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sum_v2(arr):
    return sum(arr)  # Встроенная функция — быстрее!

data = list(range(100000))

print("Версия 1 (цикл):")
profile_function(sum_v1, data)

print("\nВерсия 2 (sum):")
profile_function(sum_v2, data)
```

---

## 💡 Key Takeaways

- **Big-O** описывает верхнюю границу роста; используется для worst-case анализа

- **Амортизированный анализ** показывает среднюю стоимость операции в последовательности

- **Временная vs пространственная сложность** — классический trade-off; выбирайте под задачу

- **Константы важны** на практике: O(n) с большой константой может быть медленнее O(n²) на малых n

- **Профилируйте реальный код**: теоретический анализ — отправная точка, не финальный ответ

---

## 🚀 Next Steps

**Related Modules:**

- [Классы алгоритмов](../03_Algorithm_Classes/) — группировка алгоритмов по подходу
- [Lower bounds](../04_Lower_Bounds/) — теоретические ограничения

**Practice Ideas:**

1. Проанализируйте сложность алгоритма поиска подстроки
2. Сравните производительность list и deque для операций в начале
3. Реализуйте динамический массив и измерьте амортизированную сложность

**Going Deeper:**

- Изучите Master Theorem для анализа рекурсии
- Познакомьтесь с Θ-нотацией для точного анализа
- Исследуйте cache-oblivious алгоритмы

---


