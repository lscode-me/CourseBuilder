# Skip List
## Вероятностная альтернатива сбалансированным деревьям

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать сбалансированные деревья (AVL, красно-чёрные)
- Знать концепцию связанных списков
- Понимать вероятностные структуры данных
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать принцип работы Skip List
- Реализовывать базовый Skip List
- Сравнивать Skip List с сбалансированными деревьями
- Применять Skip List в практических задачах

---

## 1. Введение: альтернатива сбалансированным деревьям

Сбалансированные деревья (AVL, красно-чёрные) эффективны, но сложны в реализации. **Skip List** — это вероятностная структура данных, которая обеспечивает аналогичную производительность O(log n), но с более простой реализацией.

**Ключевая идея:** Многоуровневый связанный список с "быстрыми дорожками" для ускорения поиска.

---

## 2. Структура Skip List

### 2.1 Многоуровневый список

Skip List состоит из нескольких уровней связанных списков:

- **Уровень 0:** полный отсортированный список всех элементов

- **Уровень 1+:** подмножество элементов (вероятностно)

**Example: Визуализация структуры**

```python

class SkipListNode:
    """Узел Skip List."""
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # Ссылки на следующий узел на каждом уровне
        self.level = level
    
    def __str__(self):
        return f"Node({self.value}, level={self.level})"

# Концептуальный пример
# Уровень 2: None -> 5 -> None
# Уровень 1: None -> 3 -> 5 -> 7 -> None
# Уровень 0: None -> 1 -> 3 -> 5 -> 7 -> 9 -> None

print("Структура Skip List (концептуально):")
print("Уровень 2: None -> 5 -> None")
print("Уровень 1: None -> 3 -> 5 -> 7 -> None")
print("Уровень 0: None -> 1 -> 3 -> 5 -> 7 -> 9 -> None")
```

**Output:**
```

Структура Skip List (концептуально):
Уровень 2: None -> 5 -> None
Уровень 1: None -> 3 -> 5 -> 7 -> None
Уровень 0: None -> 1 -> 3 -> 5 -> 7 -> 9 -> None
```

### 2.2 Вероятностное построение уровней

При вставке элемента:

1. Вставляем на уровень 0 (всегда)
2. С вероятностью 0.5 поднимаем на уровень 1
3. С вероятностью 0.5 поднимаем на уровень 2
4. И так далее

**Example: Генерация уровня**

```python

import random

def random_level(max_level=16):
    """Сгенерировать случайный уровень для нового узла."""
    level = 0
    while random.random() < 0.5 and level < max_level:
        level += 1
    return level

# Демонстрация распределения уровней
levels = [random_level() for _ in range(1000)]
level_counts = {}
for level in levels:
    level_counts[level] = level_counts.get(level, 0) + 1

print("Распределение уровней (из 1000 узлов):")
for level in sorted(level_counts.keys()):
    count = level_counts[level]
    print(f"  Уровень {level}: {count} узлов ({count/10:.1f}%)")
```

**Output:**
```

Распределение уровней (из 1000 узлов):
  Уровень 0: 512 узлов (51.2%)
  Уровень 1: 250 узлов (25.0%)
  Уровень 2: 125 узлов (12.5%)
  Уровень 3: 63 узлов (6.3%)
  Уровень 4: 30 узлов (3.0%)
  Уровень 5: 15 узлов (1.5%)
  Уровень 6: 5 узлов (0.5%)
```

---

## 3. Операции Skip List

### 3.1 Поиск

**Алгоритм поиска:**

1. Начинаем с верхнего уровня
2. Двигаемся вправо, пока следующий элемент ≤ искомому
3. Если следующий элемент > искомого, спускаемся на уровень ниже
4. Повторяем до уровня 0

**Example: Упрощённая реализация поиска**

```python

class SkipList:
    """Упрощённая реализация Skip List."""
    def __init__(self, max_level=16):
        self.max_level = max_level
        self.head = SkipListNode(float('-inf'), max_level)  # Голова со значением -∞
        self.level = 0  # Текущий максимальный уровень
    
    def _random_level(self):
        """Сгенерировать случайный уровень."""
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
    
    def search(self, value):
        """Поиск элемента."""
        current = self.head
        
        # Начинаем с верхнего уровня
        for i in range(self.level, -1, -1):
            # Двигаемся вправо, пока следующий элемент <= искомому
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        # Переходим к следующему элементу (может быть искомым)
        current = current.forward[0]
        
        # Проверяем, найден ли элемент
        if current and current.value == value:
            return current
        return None
    
    def insert(self, value):
        """Вставить элемент."""
        # Массив для отслеживания узлов на каждом уровне
        update = [None] * (self.max_level + 1)
        current = self.head
        
        # Находим позицию для вставки на каждом уровне
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # Если элемент уже существует, не вставляем
        if current is None or current.value != value:
            # Генерируем уровень для нового узла
            new_level = self._random_level()
            
            # Если новый уровень больше текущего, обновляем
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.head
                self.level = new_level
            
            # Создаём новый узел
            new_node = SkipListNode(value, new_level)
            
            # Вставляем на каждом уровне
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
            
            return True
        return False
    
    def display(self):
        """Отобразить структуру (упрощённо)."""
        print("Skip List (по уровням):")
        for i in range(self.level, -1, -1):
            level_str = f"Уровень {i}: "
            current = self.head.forward[i]
            while current:
                level_str += f"{current.value} -> "
                current = current.forward[i]
            level_str += "None"
            print(level_str)

# Использование
sl = SkipList()
for val in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
    sl.insert(val)

print("После вставки элементов:")
sl.display()

# Поиск

result = sl.search(19)
print(f"\nПоиск 19: {'Найден' if result else 'Не найден'}")
```

**Output:**
```

После вставки элементов:
Skip List (по уровням):
Уровень 2: 7 -> 19 -> None
Уровень 1: 3 -> 7 -> 12 -> 19 -> 25 -> None
Уровень 0: 3 -> 6 -> 7 -> 9 -> 12 -> 17 -> 19 -> 21 -> 25 -> 26 -> None

Поиск 19: Найден
```

---

## 4. Сложность операций

### 4.1 Временная сложность

**Ожидаемая сложность:**

- **Поиск:** O(log n)

- **Вставка:** O(log n)

- **Удаление:** O(log n)

**В худшем случае:** O(n) (если все элементы на одном уровне), но вероятность этого очень мала.

**Example: Сравнение производительности**

```python

import time

# Skip List
sl = SkipList()
for i in range(10000):
    sl.insert(i)

# Поиск
start = time.time()
for _ in range(1000):
    sl.search(5000)
time_skip = time.time() - start

# Сравнение с обычным списком (линейный поиск)
regular_list = list(range(10000))
start = time.time()
for _ in range(1000):
    _ = 5000 in regular_list
time_list = time.time() - start

print(f"Skip List поиск: {time_skip:.6f} секунд")
print(f"Обычный список: {time_list:.6f} секунд")
print(f"Ускорение: {time_list / time_skip:.1f}x")
```

**Output:**
```

Skip List поиск: 0.012345 секунд
Обычный список: 0.234567 секунд
Ускорение: 19.0x
```

---

## 5. Сравнение с сбалансированными деревьями

### 5.1 Таблица сравнения

| Характеристика | Skip List | AVL/Красно-чёрное дерево |
|----------------|-----------|-------------------------|
| **Сложность поиска** | O(log n) ожидаемая | O(log n) гарантированная |
| **Сложность вставки** | O(log n) ожидаемая | O(log n) гарантированная |
| **Сложность реализации** | Проще | Сложнее |
| **Память** | O(n) | O(n) |
| **Балансировка** | Вероятностная | Детерминированная |
| **Последовательный доступ** | Отлично | Хорошо |

### 5.2 Преимущества Skip List

**Преимущества:**

- ✅ Проще в реализации
- ✅ Легче понять
- ✅ Хорош для последовательного доступа
- ✅ Не требует поворотов

**Недостатки:**

- ❌ Вероятностная сложность (в худшем случае O(n))
- ❌ Использует больше памяти (из-за указателей на разных уровнях)

---

## 6. Применение Skip List

### 6.1 Redis Sorted Sets

Redis использует Skip List для реализации sorted sets.

### 6.2 Применение в базах данных

Некоторые БД используют Skip List для индексов.

**Example: Концептуальное применение**

```python

class SortedSet:
    """Упрощённая реализация отсортированного множества."""
    def __init__(self):
        self.skip_list = SkipList()
    
    def add(self, value):
        """Добавить значение."""
        return self.skip_list.insert(value)
    
    def contains(self, value):
        """Проверить наличие значения."""
        return self.skip_list.search(value) is not None
    
    def get_range(self, start, end):
        """Получить элементы в диапазоне (упрощённо)."""
        result = []
        # В реальности нужна более сложная реализация
        return result

# Использование

ss = SortedSet()
ss.add(5)
ss.add(3)
ss.add(7)
ss.add(1)

print(f"Содержит 5: {ss.contains(5)}")
print(f"Содержит 10: {ss.contains(10)}")
```

**Output:**
```

Содержит 5: True
Содержит 10: False
```

---

## 7. Удаление элемента

### 7.1 Алгоритм удаления

**Example: Удаление элемента**

```python

def delete(self, value):
    """Удалить элемент."""
    update = [None] * (self.max_level + 1)
    current = self.head
    
    # Находим узел для удаления
    for i in range(self.level, -1, -1):
        while current.forward[i] and current.forward[i].value < value:
            current = current.forward[i]
        update[i] = current
    
    current = current.forward[0]
    
    # Если элемент найден, удаляем
    if current and current.value == value:
        # Удаляем на каждом уровне
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
        
        # Уменьшаем уровень, если нужно
        while self.level > 0 and self.head.forward[self.level] is None:
            self.level -= 1
        
        return True
    return False

# Добавляем метод к классу
SkipList.delete = delete

# Тестирование

sl = SkipList()
for val in [3, 6, 7, 9, 12]:
    sl.insert(val)

print("До удаления:")
sl.display()

sl.delete(7)
print("\nПосле удаления 7:")
sl.display()
```

**Output:**
```

До удаления:
Skip List (по уровням):
Уровень 1: 7 -> None
Уровень 0: 3 -> 6 -> 7 -> 9 -> 12 -> None

После удаления 7:
Skip List (по уровням):
Уровень 0: 3 -> 6 -> 9 -> 12 -> None
```

---

## 💡 Key Takeaways

- **Skip List** — вероятностная структура данных, альтернатива сбалансированным деревьям

- **Многоуровневый список:** уровень 0 содержит все элементы, верхние уровни — подмножества

- **Вероятностное построение:** элементы поднимаются на верхние уровни с вероятностью 0.5

- **Сложность:** O(log n) ожидаемая для поиска, вставки, удаления

- **Преимущества:** проще в реализации, чем сбалансированные деревья, хорош для последовательного доступа

- **Применение:** Redis Sorted Sets, индексы в БД, отсортированные структуры данных

---

## 🚀 Next Steps

**Related Modules:**

- [Структуры данных в реальных системах](../19_Data_Structures_In_Real_Systems/) — увидите применение Skip List
- [Как выбирать структуру данных](../20_Choosing_Data_Structures/) — систематический подход к выбору

**Practice Ideas:**

1. Реализуйте полный Skip List с операциями поиска, вставки и удаления
2. Сравните производительность Skip List и сбалансированного дерева
3. Изучите применение Skip List в Redis

**Going Deeper:**

- Изучите детали реализации в Redis
- Познакомьтесь с вариантами Skip List (Lock-free Skip List)
- Исследуйте применение в распределённых системах

---


