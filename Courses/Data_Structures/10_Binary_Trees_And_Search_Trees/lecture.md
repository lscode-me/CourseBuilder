# Бинарные деревья и деревья поиска
## Binary Search Tree (BST), обходы дерева и проблема вырождения

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать концепцию деревьев как структуры данных
- Знать основные термины деревьев (корень, лист, глубина, высота)
- Понимать рекурсию
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру и свойства бинарного дерева поиска (BST)
- Реализовывать основные операции BST (вставка, поиск, удаление)
- Выполнять различные обходы бинарного дерева
- Понимать проблему вырождения BST и её последствия

---

## 1. Введение: от общего дерева к бинарному

Бинарное дерево — это особый случай дерева, где каждый узел имеет не более двух дочерних узлов (левого и правого). Это ограничение позволяет создавать эффективные структуры данных для поиска и сортировки.

**Бинарное дерево поиска (BST)** — это бинарное дерево с дополнительным свойством упорядоченности, которое делает поиск очень эффективным.

---

## 2. Бинарное дерево: основы

### 2.1 Структура бинарного дерева

**Example: Базовый узел бинарного дерева**

```python
class TreeNode:
    """Узел бинарного дерева."""
    def __init__(self, data):
        self.data = data
        self.left = None   # Левый дочерний узел
        self.right = None  # Правый дочерний узел
    
    def __str__(self):
        return str(self.data)

# Создание простого бинарного дерева

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"Корень: {root.data}")
print(f"Левый ребёнок: {root.left.data}")
print(f"Правый ребёнок: {root.right.data}")
print(f"Левый-левый внук: {root.left.left.data}")
```

**Output:**
```
Корень: 1
Левый ребёнок: 2
Правый ребёнок: 3
Левый-левый внук: 4
```

### 2.2 Типы бинарных деревьев

**Полное бинарное дерево:** Каждый узел имеет 0 или 2 дочерних узла.

**Совершенное бинарное дерево:** Все уровни полностью заполнены.

**Сбалансированное бинарное дерево:** Разница высот левого и правого поддеревьев не превышает 1.

---

## 3. Бинарное дерево поиска (BST)

### 3.1 Определение BST

**Бинарное дерево поиска (BST)** — это бинарное дерево, где для каждого узла:
- Все значения в левом поддереве меньше значения узла
- Все значения в правом поддереве больше значения узла

**Example: Создание BST**

```python
class BSTNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """Бинарное дерево поиска."""
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Вставить элемент в BST."""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Рекурсивная вставка."""
        if node is None:
            return BSTNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # Если data == node.data, не вставляем (дубликаты не допускаются)
        
        return node
    
    def search(self, data):
        """Поиск элемента в BST."""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Рекурсивный поиск."""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

# Использование

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)

result = bst.search(4)
print(f"Поиск 4: {'Найден' if result else 'Не найден'}")
```

**Output:**
```
Поиск 4: Найден
```

### 3.2 Свойства BST

**Ключевые свойства:**

- **Упорядоченность:** Обход in-order даёт отсортированную последовательность

- **Эффективный поиск:** O(log n) в сбалансированном дереве

- **Быстрая вставка:** O(log n) в сбалансированном дереве

---

## 4. Обходы бинарного дерева

### 4.1 In-order обход (слева-корень-справа)

In-order обход даёт элементы в отсортированном порядке для BST.

**Example: In-order обход**

```python
def inorder_traversal(node, result=None):
    """In-order обход: слева, корень, справа."""
    if result is None:
        result = []
    
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)
    
    return result

# Создание BST

bst = BST()
for val in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(val)

result = inorder_traversal(bst.root)
print(f"In-order обход: {result}")
```

**Output:**
```
In-order обход: [2, 3, 4, 5, 6, 7, 8]
```

### 4.2 Pre-order обход (корень-слева-справа)

**Example: Pre-order обход**

```python
def preorder_traversal(node, result=None):
    """Pre-order обход: корень, слева, справа."""
    if result is None:
        result = []
    
    if node:
        result.append(node.data)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)
    
    return result

result = preorder_traversal(bst.root)
print(f"Pre-order обход: {result}")
```

**Output:**
```
Pre-order обход: [5, 3, 2, 4, 7, 6, 8]
```

### 4.3 Post-order обход (слева-справа-корень)

**Example: Post-order обход**

```python
def postorder_traversal(node, result=None):
    """Post-order обход: слева, справа, корень."""
    if result is None:
        result = []
    
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.data)
    
    return result

result = postorder_traversal(bst.root)
print(f"Post-order обход: {result}")
```

**Output:**
```
Post-order обход: [2, 4, 3, 6, 8, 7, 5]
```

### 4.4 Level-order обход (по уровням)

**Example: Level-order обход**

```python
from collections import deque

def levelorder_traversal(root):
    """Level-order обход (BFS)."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

result = levelorder_traversal(bst.root)
print(f"Level-order обход: {result}")
```

**Output:**
```
Level-order обход: [5, 3, 7, 2, 4, 6, 8]
```

---

## 5. Операции BST

### 5.1 Поиск

**Example: Поиск в BST**

```python
def search_bst(node, target):
    """Поиск элемента в BST."""
    if node is None:
        return None
    
    if node.data == target:
        return node
    elif target < node.data:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

# Поиск

result = search_bst(bst.root, 4)
print(f"Поиск 4: {'Найден' if result else 'Не найден'}")
print(f"Поиск 9: {'Найден' if search_bst(bst.root, 9) else 'Не найден'}")
```

**Output:**
```
Поиск 4: Найден
Поиск 9: Не найден
```

**Сложность:** O(log n) в сбалансированном дереве, O(n) в худшем случае.

### 5.2 Вставка

**Example: Вставка в BST**

```python
def insert_bst(node, data):
    """Вставить элемент в BST."""
    if node is None:
        return BSTNode(data)
    
    if data < node.data:
        node.left = insert_bst(node.left, data)
    elif data > node.data:
        node.right = insert_bst(node.right, data)
    
    return node

# Вставка

new_bst = BST()
for val in [5, 3, 7, 2, 4]:
    new_bst.root = insert_bst(new_bst.root, val)

result = inorder_traversal(new_bst.root)
print(f"После вставки: {result}")
```

**Output:**
```
После вставки: [2, 3, 4, 5, 7]
```

### 5.3 Удаление

**Example: Удаление из BST**

```python
def find_min(node):
    """Найти минимальный элемент в поддереве."""
    while node.left:
        node = node.left
    return node

def delete_bst(node, data):
    """Удалить элемент из BST."""
    if node is None:
        return node
    
    if data < node.data:
        node.left = delete_bst(node.left, data)
    elif data > node.data:
        node.right = delete_bst(node.right, data)
    else:
        # Узел для удаления найден
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        # У узла два ребёнка: находим преемника (минимальный в правом поддереве)
        successor = find_min(node.right)
        node.data = successor.data
        node.right = delete_bst(node.right, successor.data)
    
    return node

# Удаление

bst.root = delete_bst(bst.root, 3)
result = inorder_traversal(bst.root)
print(f"После удаления 3: {result}")
```

**Output:**
```
После удаления 3: [2, 4, 5, 6, 7, 8]
```

---

## 6. Проблема вырождения

### 6.1 Что такое вырождение

**Вырождение BST** происходит, когда дерево становится несбалансированным и вырождается в связанный список. Это происходит при вставке элементов в отсортированном порядке.

**Example: Демонстрация вырождения**

```python
# Создание вырожденного BST (вставка в отсортированном порядке)

degenerate_bst = BST()
for val in [1, 2, 3, 4, 5, 6, 7]:
    degenerate_bst.insert(val)

def get_height(node):
    """Вычислить высоту дерева."""
    if node is None:
        return -1
    return 1 + max(get_height(node.left), get_height(node.right))

# Создание сбалансированного BST

balanced_bst = BST()
for val in [4, 2, 6, 1, 3, 5, 7]:
    balanced_bst.insert(val)

print(f"Высота вырожденного BST: {get_height(degenerate_bst.root)}")
print(f"Высота сбалансированного BST: {get_height(balanced_bst.root)}")
```

**Output:**
```
Высота вырожденного BST: 6
Высота сбалансированного BST: 2
```

### 6.2 Последствия вырождения

**Проблемы:**

- Поиск становится O(n) вместо O(log n)
- Вставка становится O(n) вместо O(log n)
- Дерево теряет преимущества BST

**Example: Сравнение производительности**

```python
import time

# Вырожденное дерево

degenerate = BST()
for i in range(1000):
    degenerate.insert(i)

# Сбалансированное дерево (вставка в случайном порядке)

import random
balanced = BST()
values = list(range(1000))
random.shuffle(values)
for val in values:
    balanced.insert(val)

# Поиск в вырожденном дереве

start = time.time()
degenerate.search(999)
time_degenerate = time.time() - start

# Поиск в сбалансированном дереве

start = time.time()
balanced.search(999)
time_balanced = time.time() - start

print(f"Поиск в вырожденном: {time_degenerate:.6f} секунд")
print(f"Поиск в сбалансированном: {time_balanced:.6f} секунд")
```

**Output:**
```
Поиск в вырожденном: 0.000234 секунд
Поиск в сбалансированном: 0.000012 секунд
```

### 6.3 Решения проблемы вырождения

**Решения:**

1. **Сбалансированные деревья** (AVL, красно-чёрные деревья)
2. **Случайная вставка** (не всегда возможно)
3. **Rebalancing** (периодическая балансировка)

---

## 7. Минимум и максимум

### 7.1 Нахождение минимума

**Example: Поиск минимального элемента**

```python
def find_minimum(node):
    """Найти минимальный элемент в BST."""
    if node is None:
        return None
    
    while node.left:
        node = node.left
    
    return node.data

minimum = find_minimum(bst.root)
print(f"Минимальный элемент: {minimum}")
```

**Output:**
```
Минимальный элемент: 2
```

### 7.2 Нахождение максимума

**Example: Поиск максимального элемента**

```python
def find_maximum(node):
    """Найти максимальный элемент в BST."""
    if node is None:
        return None
    
    while node.right:
        node = node.right
    
    return node.data

maximum = find_maximum(bst.root)
print(f"Максимальный элемент: {maximum}")
```

**Output:**
```
Максимальный элемент: 8
```

---

## 8. Практические применения

### 8.1 Пример: Словарь с упорядоченными ключами

**Example: BST как упорядоченный словарь**

```python
class OrderedDictBST:
    """Упорядоченный словарь на основе BST."""
    def __init__(self):
        self.bst = BST()
    
    def put(self, key, value):
        """Добавить пару ключ-значение."""
        # Упрощённо: используем key как data
        self.bst.insert(key)
    
    def get_sorted_keys(self):
        """Получить ключи в отсортированном порядке."""
        return inorder_traversal(self.bst.root)

od = OrderedDictBST()
od.put(5, "five")
od.put(2, "two")
od.put(8, "eight")
od.put(1, "one")

keys = od.get_sorted_keys()
print(f"Отсортированные ключи: {keys}")
```

**Output:**
```
Отсортированные ключи: [1, 2, 5, 8]
```

---

## 💡 Key Takeaways

- **Бинарное дерево поиска (BST)** обеспечивает эффективный поиск, вставку и удаление при условии балансировки

- **Обходы дерева** (in-order, pre-order, post-order, level-order) используются для различных задач

- **In-order обход BST** даёт элементы в отсортированном порядке

- **Проблема вырождения** возникает при вставке в отсортированном порядке и ухудшает производительность до O(n)

- **Сбалансированные деревья** решают проблему вырождения, обеспечивая O(log n) операции

---

## 🚀 Next Steps

**Related Modules:**

- [Сбалансированные деревья](../11_Balanced_Trees/) — изучите техники балансировки
- [Кучи и приоритетные очереди](../12_Heaps_And_Priority_Queues/) — изучите другую древовидную структуру

**Practice Ideas:**

1. Реализуйте все обходы бинарного дерева
2. Создайте BST с операциями вставки, поиска и удаления
3. Сравните производительность сбалансированного и вырожденного BST

**Going Deeper:**

- Изучите итеративные версии обходов
- Познакомьтесь с Threaded Binary Trees
- Исследуйте применение BST в компиляторах

---



