# Классы алгоритмов
## Поиск, сортировка, жадные алгоритмы, Divide and Conquer, динамическое программирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать связь алгоритмов и структур данных
- Знать Big-O нотацию и уметь анализировать сложность
- Иметь опыт реализации простых алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Классифицировать алгоритмы по их подходу к решению задач
- Применять алгоритмы поиска и сортировки
- Использовать жадные алгоритмы для задач оптимизации
- Разрабатывать решения методом Divide and Conquer
- Понимать принципы динамического программирования

---

## 1. Зачем классифицировать алгоритмы

### 1.1 Паттерны решения задач

Большинство алгоритмов можно отнести к нескольким большим классам. Понимание этих классов помогает:

- Быстро находить подход к новой задаче
- Оценивать сложность до реализации
- Выбирать между альтернативными решениями

### 1.2 Основные классы алгоритмов

| Класс | Идея | Примеры |
|-------|------|---------|
| Поиск | Найти элемент в данных | Линейный, бинарный поиск |
| Сортировка | Упорядочить данные | QuickSort, MergeSort |
| Жадные | Локально оптимальный выбор | Кодирование Хаффмана |
| Divide & Conquer | Разделяй и властвуй | MergeSort, бинарный поиск |
| Динамическое программирование | Решение через подзадачи | Фибоначчи, рюкзак |

---

## 2. Алгоритмы поиска

### 2.1 Линейный поиск

Простейший алгоритм — проверяем каждый элемент по очереди.

```python
def linear_search(arr, target):
    """
    Линейный поиск: O(n) время, O(1) память.
    Работает на любых данных, не требует сортировки.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Пример

data = [5, 2, 8, 1, 9, 3, 7]
print(f"Индекс 8: {linear_search(data, 8)}")
print(f"Индекс 10: {linear_search(data, 10)}")
```

**Output:**
```
Индекс 8: 2
Индекс 10: -1
```

### 2.2 Бинарный поиск

Работает только на отсортированных данных, но намного быстрее.

```python
def binary_search(arr, target):
    """
    Бинарный поиск: O(log n) время, O(1) память.
    Требует отсортированный массив!
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Пример на отсортированных данных

sorted_data = [1, 2, 3, 5, 7, 8, 9]
print(f"Индекс 7: {binary_search(sorted_data, 7)}")
print(f"Индекс 4: {binary_search(sorted_data, 4)}")
```

**Output:**
```
Индекс 7: 4
Индекс 4: -1
```

### 2.3 Вариации бинарного поиска

```python
import bisect

def find_first_occurrence(arr, target):
    """Находит первое вхождение элемента."""
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

def find_last_occurrence(arr, target):
    """Находит последнее вхождение элемента."""
    index = bisect.bisect_right(arr, target) - 1
    if index >= 0 and arr[index] == target:
        return index
    return -1

def count_occurrences(arr, target):
    """Считает количество вхождений элемента."""
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left

# Пример

data = [1, 2, 2, 2, 3, 4, 5]
print(f"Первое вхождение 2: {find_first_occurrence(data, 2)}")
print(f"Последнее вхождение 2: {find_last_occurrence(data, 2)}")
print(f"Количество 2: {count_occurrences(data, 2)}")
```

**Output:**
```
Первое вхождение 2: 1
Последнее вхождение 2: 3
Количество 2: 3
```

---

## 3. Алгоритмы сортировки

### 3.1 Обзор алгоритмов сортировки

| Алгоритм | Время (среднее) | Время (худшее) | Память | Стабильность |
|----------|-----------------|----------------|--------|--------------|
| Bubble Sort | O(n²) | O(n²) | O(1) | Стабильный |
| Insertion Sort | O(n²) | O(n²) | O(1) | Стабильный |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Стабильный |
| Quick Sort | O(n log n) | O(n²) | O(log n) | Нестабильный |
| Heap Sort | O(n log n) | O(n log n) | O(1) | Нестабильный |

### 3.2 Сортировка вставками

Эффективна для почти отсортированных данных.

```python
def insertion_sort(arr):
    """
    Сортировка вставками: O(n²) в среднем, O(n) для почти отсортированных.
    In-place, стабильная.
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Сдвигаем элементы, большие key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

# Пример

data = [5, 2, 8, 1, 9]
print(f"До: {data}")
print(f"После: {insertion_sort(data)}")
```

**Output:**
```
До: [5, 2, 8, 1, 9]
После: [1, 2, 5, 8, 9]
```

### 3.3 Сортировка слиянием (Merge Sort)

Классический пример Divide and Conquer.

```python
def merge_sort(arr):
    """
    Сортировка слиянием: O(n log n) всегда, O(n) память.
    Стабильная, хороша для связанных списков.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Сливает два отсортированных массива."""
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

# Пример

data = [38, 27, 43, 3, 9, 82, 10]
print(f"До: {data}")
print(f"После: {merge_sort(data)}")
```

**Output:**
```
До: [38, 27, 43, 3, 9, 82, 10]
После: [3, 9, 10, 27, 38, 43, 82]
```

### 3.4 Быстрая сортировка (QuickSort)

На практике часто самая быстрая.

```python
def quicksort(arr):
    """
    Быстрая сортировка: O(n log n) в среднем, O(n²) в худшем.
    In-place версия использует O(log n) памяти на стек.
    """
    if len(arr) <= 1:
        return arr
    
    # Выбор pivot — ключ к производительности
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Пример

data = [3, 6, 8, 10, 1, 2, 1]
print(f"QuickSort: {quicksort(data)}")
```

**Output:**
```
QuickSort: [1, 1, 2, 3, 6, 8, 10]
```

---

## 4. Жадные алгоритмы

### 4.1 Принцип жадного выбора

**Жадный алгоритм** на каждом шаге делает локально оптимальный выбор, надеясь получить глобально оптимальное решение.

Жадный алгоритм работает, когда задача обладает свойствами:

- **Жадный выбор**: локально оптимальный выбор ведёт к глобальному оптимуму

- **Оптимальная подструктура**: оптимальное решение содержит оптимальные решения подзадач

### 4.2 Пример: Задача о сдаче

```python
def coin_change_greedy(amount, coins):
    """
    Жадный алгоритм для размена монет.
    Работает ТОЛЬКО для некоторых наборов монет!
    """
    coins = sorted(coins, reverse=True)  # От большего к меньшему
    result = []
    
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    
    return result if amount == 0 else None

# Работает для стандартных монет

print(f"Размен 93: {coin_change_greedy(93, [1, 5, 10, 25, 50])}")

# НЕ работает для некоторых наборов
# Для [1, 3, 4] и суммы 6: жадный даст [4, 1, 1], но оптимум [3, 3]

greedy_result = coin_change_greedy(6, [1, 3, 4])
print(f"Жадный для 6 с [1,3,4]: {greedy_result} (монет: {len(greedy_result)})")
print(f"Оптимальное: [3, 3] (монет: 2)")
```

**Output:**
```
Размен 93: [50, 25, 10, 5, 1, 1, 1]
Жадный для 6 с [1,3,4]: [4, 1, 1] (монет: 3)
Оптимальное: [3, 3] (монет: 2)
```

### 4.3 Пример: Интервальное расписание

Жадный подход работает идеально для задачи о максимальном количестве непересекающихся интервалов.

```python
def max_non_overlapping_intervals(intervals):
    """
    Выбирает максимальное количество непересекающихся интервалов.
    Жадный подход: выбираем интервал с минимальным концом.
    """
    if not intervals:
        return []
    
    # Сортируем по времени окончания
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    result = [sorted_intervals[0]]
    
    for interval in sorted_intervals[1:]:
        # Если начало нового интервала >= конца последнего выбранного
        if interval[0] >= result[-1][1]:
            result.append(interval)
    
    return result

# Пример: встречи в календаре

meetings = [(1, 3), (2, 5), (3, 6), (5, 7), (8, 10)]
selected = max_non_overlapping_intervals(meetings)
print(f"Все встречи: {meetings}")
print(f"Максимум без пересечений: {selected}")
```

**Output:**
```
Все встречи: [(1, 3), (2, 5), (3, 6), (5, 7), (8, 10)]
Максимум без пересечений: [(1, 3), (3, 6), (8, 10)]
```

### 4.4 Пример: Кодирование Хаффмана

```python
import heapq
from collections import Counter

def huffman_encoding(text):
    """Строит коды Хаффмана для символов текста."""
    # Подсчёт частот
    freq = Counter(text)
    
    # Создаём кучу из (частота, символ)
    heap = [[f, [char, ""]] for char, f in freq.items()]
    heapq.heapify(heap)
    
    # Строим дерево Хаффмана
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        # Добавляем 0 к кодам левого поддерева
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        
        # Добавляем 1 к кодам правого поддерева
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # Объединяем
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return {char: code for char, code in heap[0][1:]}

# Пример

text = "abracadabra"
codes = huffman_encoding(text)
print(f"Текст: {text}")
print(f"Коды Хаффмана: {codes}")

# Подсчёт экономии

original_bits = len(text) * 8  # ASCII
huffman_bits = sum(len(codes[c]) for c in text)
print(f"ASCII: {original_bits} бит, Huffman: {huffman_bits} бит")
```

**Output:**
```
Текст: abracadabra
Коды Хаффмана: {'a': '0', 'r': '10', 'b': '110', 'c': '1110', 'd': '1111'}
ASCII: 88 бит, Huffman: 23 бит
```

---

## 5. Divide and Conquer

### 5.1 Принцип разделяй и властвуй

1. **Divide**: разбить задачу на подзадачи того же типа
2. **Conquer**: решить подзадачи рекурсивно
3. **Combine**: объединить решения подзадач

### 5.2 Анализ сложности D&C

Рекуррентное соотношение: T(n) = a·T(n/b) + f(n)

Где:

- a — количество подзадач
- n/b — размер каждой подзадачи
- f(n) — стоимость разделения и объединения

**Master Theorem (упрощённо):**

- Если f(n) = O(n^k), то:
  - a > b^k: T(n) = O(n^(log_b(a)))
  - a = b^k: T(n) = O(n^k · log n)
  - a < b^k: T(n) = O(n^k)

### 5.3 Пример: Возведение в степень

```python
def power_naive(x, n):
    """Наивное возведение в степень: O(n)."""
    result = 1
    for _ in range(n):
        result *= x
    return result

def power_divide_conquer(x, n):
    """
    Divide and Conquer: O(log n).
    T(n) = T(n/2) + O(1) → O(log n)
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_divide_conquer(x, -n)
    
    half = power_divide_conquer(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

# Сравнение

import time

n = 100000
x = 1.0001

start = time.perf_counter()
power_naive(x, n)
time_naive = time.perf_counter() - start

start = time.perf_counter()
power_divide_conquer(x, n)
time_dc = time.perf_counter() - start

print(f"Наивный O(n): {time_naive*1000:.3f} мс")
print(f"D&C O(log n): {time_dc*1000:.3f} мс")
```

**Output:**
```
Наивный O(n): 8.234 мс
D&C O(log n): 0.021 мс
```

### 5.4 Пример: Поиск максимума в массиве (D&C)

```python
def find_max_dc(arr, left, right):
    """
    Divide and Conquer для поиска максимума.
    T(n) = 2T(n/2) + O(1) → O(n)
    Не быстрее линейного, но демонстрирует подход.
    """
    # База: один элемент
    if left == right:
        return arr[left]
    
    # Divide
    mid = (left + right) // 2
    
    # Conquer
    max_left = find_max_dc(arr, left, mid)
    max_right = find_max_dc(arr, mid + 1, right)
    
    # Combine
    return max(max_left, max_right)

# Пример

data = [3, 7, 2, 9, 1, 5, 8]
result = find_max_dc(data, 0, len(data) - 1)
print(f"Максимум: {result}")
```

**Output:**
```
Максимум: 9
```

---

## 6. Динамическое программирование

### 6.1 Принципы DP

**Динамическое программирование** применяется, когда задача имеет:
- **Оптимальная подструктура**: оптимальное решение строится из оптимальных решений подзадач

- **Перекрывающиеся подзадачи**: одни и те же подзадачи решаются многократно

Два подхода:

- **Top-down (мемоизация)**: рекурсия с кэшированием

- **Bottom-up (табуляция)**: итеративное заполнение таблицы

### 6.2 Пример: Числа Фибоначчи

```python
from functools import lru_cache
import time

# Наивная рекурсия: O(2^n)

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Top-down с мемоизацией: O(n)

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

# Bottom-up: O(n) время, O(1) память

def fib_tabulation(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Сравнение

n = 35

start = time.perf_counter()
fib_naive(n)
time_naive = time.perf_counter() - start

start = time.perf_counter()
fib_memo(n)
time_memo = time.perf_counter() - start

start = time.perf_counter()
fib_tabulation(n)
time_tab = time.perf_counter() - start

print(f"fib({n}) = {fib_tabulation(n)}")
print(f"Наивный: {time_naive:.3f} сек")
print(f"Мемоизация: {time_memo:.6f} сек")
print(f"Табуляция: {time_tab:.6f} сек")
```

**Output:**
```
fib(35) = 9227465
Наивный: 1.892 сек
Мемоизация: 0.000018 сек
Табуляция: 0.000005 сек
```

### 6.3 Пример: Задача о рюкзаке (Knapsack)

```python
def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack: каждый предмет можно взять только один раз.
    O(n * capacity) время и память.
    """
    n = len(weights)
    
    # dp[i][w] = максимальная ценность для первых i предметов и вместимости w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Не берём i-й предмет
            dp[i][w] = dp[i-1][w]
            
            # Берём i-й предмет (если помещается)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# Пример

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack_01(weights, values, capacity)
print(f"Веса: {weights}")
print(f"Ценности: {values}")
print(f"Вместимость: {capacity}")
print(f"Максимальная ценность: {max_value}")
```

**Output:**
```
Веса: [2, 3, 4, 5]
Ценности: [3, 4, 5, 6]
Вместимость: 8
Максимальная ценность: 10
```

### 6.4 Пример: Наибольшая общая подпоследовательность (LCS)

```python
def lcs(s1, s2):
    """
    Longest Common Subsequence.
    O(n * m) время и память.
    """
    m, n = len(s1), len(s2)
    
    # dp[i][j] = длина LCS для s1[:i] и s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Восстановление LCS
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs_str))

# Пример

s1 = "ABCDGH"
s2 = "AEDFHR"
result = lcs(s1, s2)
print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"LCS: {result} (длина: {len(result)})")
```

**Output:**
```
s1: ABCDGH
s2: AEDFHR
LCS: ADH (длина: 3)
```

---

## 7. Выбор подхода к задаче

### 7.1 Когда использовать какой класс

| Признак задачи | Рекомендуемый подход |
|----------------|---------------------|
| Найти элемент в данных | Поиск |
| Упорядочить данные | Сортировка |
| Локальный оптимум = глобальный | Жадный алгоритм |
| Задача разбивается на независимые части | Divide & Conquer |
| Перекрывающиеся подзадачи | Динамическое программирование |

### 7.2 Дерево решений

```python
def choose_algorithm_class(problem):
    """
    Псевдокод для выбора класса алгоритма.
    """
    # 1. Задача оптимизации?
    if problem.is_optimization:
        # 1.1. Жадный выбор гарантирует оптимум?
        if problem.has_greedy_property:
            return "Жадный алгоритм"
        
        # 1.2. Есть перекрывающиеся подзадачи?
        if problem.has_overlapping_subproblems:
            return "Динамическое программирование"
        
        # 1.3. Задача разбивается на независимые части?
        if problem.can_divide_independently:
            return "Divide and Conquer"
    
    # 2. Задача поиска?
    if problem.is_search:
        if problem.data_is_sorted:
            return "Бинарный поиск"
        return "Линейный поиск или хеширование"
    
    # 3. Нужна сортировка?
    if problem.needs_ordering:
        return "Сортировка (выбор по ограничениям)"
    
    return "Перебор с отсечениями"
```

### 7.3 Сравнение подходов на примере

**Задача**: Минимальное количество монет для получения суммы S.

```python
# Жадный подход (не всегда оптимален!)

def coins_greedy(coins, amount):
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else float('inf')

# Динамическое программирование (всегда оптимален)

def coins_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Сравнение

coins = [1, 3, 4]
amount = 6

greedy = coins_greedy(coins, amount)
dp = coins_dp(coins, amount)

print(f"Монеты: {coins}, сумма: {amount}")
print(f"Жадный: {greedy} монет")
print(f"DP: {dp} монет")
```

**Output:**
```
Монеты: [1, 3, 4], сумма: 6
Жадный: 3 монет
DP: 2 монет
```

---

## 💡 Key Takeaways

- **Поиск**: линейный O(n) для несортированных, бинарный O(log n) для отсортированных данных

- **Сортировка**: O(n log n) — теоретический нижний предел для сравнительных сортировок

- **Жадные алгоритмы** просты и быстры, но работают не для всех задач

- **Divide and Conquer**: эффективен когда подзадачи независимы

- **Динамическое программирование**: мощный инструмент для задач с перекрывающимися подзадачами

---

## 🚀 Next Steps

**Related Modules:**

- [Lower bounds и пределы оптимизации](../04_Lower_Bounds/) — когда нельзя улучшить
- [Индексы как структуры данных](../06_Indexes_As_Data_Structures/) — применение D&C в БД

**Practice Ideas:**

1. Реализуйте HeapSort и сравните с QuickSort
2. Решите задачу о размене монет методом DP
3. Найдите задачу, где жадный подход даёт неоптимальный результат

**Going Deeper:**

- Изучите алгоритмы на графах (BFS, DFS, Dijkstra)
- Познакомьтесь с рандомизированными алгоритмами
- Исследуйте NP-полные задачи

---


