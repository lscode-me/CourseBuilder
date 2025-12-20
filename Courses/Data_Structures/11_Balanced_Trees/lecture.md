# Сбалансированные деревья
## AVL-деревья, красно-чёрные деревья и их применение

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать бинарные деревья поиска (BST)
- Знать проблему вырождения BST
- Понимать концепцию балансировки
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать концепцию сбалансированных деревьев
- Знать принципы работы AVL-деревьев
- Понимать красно-чёрные деревья и их свойства
- Выбирать подходящий тип сбалансированного дерева для задачи

---

## 1. Введение: зачем нужна балансировка

Как мы видели, несбалансированное BST может выродиться в связанный список, что ухудшает производительность с O(log n) до O(n). **Сбалансированные деревья** решают эту проблему, автоматически поддерживая баланс при вставке и удалении.

---

## 2. AVL-деревья

### 2.1 Определение AVL-дерева

**AVL-дерево** (названо в честь изобретателей Adelson-Velsky и Landis) — это самобалансирующееся бинарное дерево поиска, где для каждого узла разница высот левого и правого поддеревьев не превышает 1.

**Balance Factor (BF):** BF(node) = height(left) - height(right)
- Для AVL-дерева: |BF| ≤ 1 для всех узлов

**Example: Проверка баланса**

```python

class AVLNode:
    """Узел AVL-дерева."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

def get_height(node):
    """Получить высоту узла."""
    if node is None:
        return -1
    return node.height

def get_balance_factor(node):
    """Вычислить баланс-фактор."""
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    """Обновить высоту узла."""
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

# Создание сбалансированного дерева
root = AVLNode(5)
root.left = AVLNode(3)
root.right = AVLNode(7)
update_height(root)

bf = get_balance_factor(root)
print(f"Баланс-фактор корня: {bf}")
print(f"Дерево сбалансировано: {abs(bf) <= 1}")
```

**Output:**
```

Баланс-фактор корня: 0
Дерево сбалансировано: True
```

### 2.2 Повороты в AVL-деревьях

Для поддержания баланса используются **повороты**:

- **Правый поворот (Right Rotation):** для левого перекоса

- **Левый поворот (Left Rotation):** для правого перекоса

- **Двойной поворот:** комбинация левого и правого

**Example: Правый поворот**

```python

def right_rotate(y):
    """Правый поворот."""
    x = y.left
    T2 = x.right
    
    # Выполняем поворот
    x.right = y
    y.left = T2
    
    # Обновляем высоты
    update_height(y)
    update_height(x)
    
    return x  # Новый корень

# Демонстрация
node = AVLNode(5)
node.left = AVLNode(3)
node.left.left = AVLNode(2)
update_height(node)

print(f"До поворота - баланс: {get_balance_factor(node)}")
new_root = right_rotate(node)
print(f"После поворота - баланс: {get_balance_factor(new_root)}")
```

**Output:**
```

До поворота - баланс: 2
После поворота - баланс: 0
```

### 2.3 Вставка в AVL-дерево

**Example: Вставка с балансировкой**

```python

def insert_avl(node, data):
    """Вставить элемент в AVL-дерево."""
    # Обычная вставка BST
    if node is None:
        return AVLNode(data)
    
    if data < node.data:
        node.left = insert_avl(node.left, data)
    elif data > node.data:
        node.right = insert_avl(node.right, data)
    else:
        return node  # Дубликаты не допускаются
    
    # Обновляем высоту
    update_height(node)
    
    # Получаем баланс-фактор
    balance = get_balance_factor(node)
    
    # Левый перекос
    if balance > 1:
        if data < node.left.data:
            return right_rotate(node)  # Left-Left
        else:
            node.left = left_rotate(node.left)  # Left-Right
            return right_rotate(node)
    
    # Правый перекос
    if balance < -1:
        if data > node.right.data:
            return left_rotate(node)  # Right-Right
        else:
            node.right = right_rotate(node.right)  # Right-Left
            return left_rotate(node)
    
    return node

def left_rotate(x):
    """Левый поворот."""
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    update_height(x)
    update_height(y)
    
    return y
```

---

## 3. Красно-чёрные деревья

### 3.1 Определение красно-чёрного дерева

**Красно-чёрное дерево** — это самобалансирующееся бинарное дерево поиска с дополнительными свойствами:
1. Каждый узел либо красный, либо чёрный
2. Корень всегда чёрный
3. Все листья (NIL) чёрные
4. Если узел красный, оба его ребёнка чёрные
5. Для каждого узла все пути от узла до листьев содержат одинаковое количество чёрных узлов

**Example: Структура красно-чёрного узла**

```python

class RBNode:
    """Узел красно-чёрного дерева."""
    RED = True
    BLACK = False
    
    def __init__(self, data, color=RED):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

# Создание узлов
root = RBNode(10, RBNode.BLACK)  # Корень чёрный
left = RBNode(5, RBNode.RED)
right = RBNode(15, RBNode.RED)

root.left = left
root.right = right
left.parent = root
right.parent = root

print(f"Корень: {root.data}, цвет: {'Чёрный' if root.color == RBNode.BLACK else 'Красный'}")
print(f"Левый: {left.data}, цвет: {'Чёрный' if left.color == RBNode.BLACK else 'Красный'}")
```

**Output:**
```

Корень: 10, цвет: Чёрный
Левый: 5, цвет: Красный
```

### 3.2 Свойства красно-чёрных деревьев

**Ключевые свойства:**

- Высота дерева: O(log n)
- Поиск, вставка, удаление: O(log n)
- Меньше поворотов, чем в AVL (лучше для частых изменений)

---

## 4. Сравнение AVL и красно-чёрных деревьев

### 4.1 Таблица сравнения

| Характеристика | AVL-дерево | Красно-чёрное дерево |
|----------------|------------|---------------------|
| **Балансировка** | Строже (|BF| ≤ 1) | Менее строгая |
| **Высота** | log₂(n) | ≤ 2log₂(n+1) |
| **Поиск** | O(log n) | O(log n) |
| **Вставка** | O(log n) | O(log n) |
| **Повороты** | Больше | Меньше |
| **Лучше для** | Частый поиск | Частые вставки/удаления |

### 4.2 Когда что использовать

**Используй AVL, когда:**

- Частые операции поиска
- Данные редко изменяются
- Нужна строгая балансировка

**Используй красно-чёрное дерево, когда:**

- Частые вставки и удаления
- Нужна хорошая производительность при изменениях
- Меньше поворотов предпочтительнее

---

## 5. Применение в Python

### 5.1 collections.OrderedDict

В Python `collections.OrderedDict` (в старых версиях) использовал красно-чёрное дерево для поддержания порядка.

**Example: Использование OrderedDict**

```python

from collections import OrderedDict

# OrderedDict сохраняет порядок вставки
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print("Порядок элементов:")
for key, value in od.items():
    print(f"  {key}: {value}")
```

**Output:**
```

Порядок элементов:
  first: 1
  second: 2
  third: 3
```

### 5.2 sortedcontainers

Библиотека `sortedcontainers` предоставляет сбалансированные структуры данных.

---

## 6. Практические примеры

### 6.1 Пример: База данных индексов

**Example: Индекс в базе данных**

```python
# Концептуально: база данных использует B-деревья (вариант сбалансированных деревьев)
# для индексации данных

class DatabaseIndex:
    """Концептуальный индекс базы данных."""
    def __init__(self):
        # В реальности используется B-дерево или B+ дерево
        self.index = {}  # Упрощённо
    
    def insert(self, key, record_id):
        """Добавить индекс."""
        self.index[key] = record_id
    
    def search(self, key):
        """Поиск по индексу."""
        return self.index.get(key)

# Использование

db_index = DatabaseIndex()
db_index.insert(100, "record_1")
db_index.insert(200, "record_2")
db_index.insert(150, "record_3")

result = db_index.search(150)
print(f"Найденная запись: {result}")
```

**Output:**
```

Найденная запись: record_3
```

---

## 💡 Key Takeaways

- **Сбалансированные деревья** автоматически поддерживают баланс, обеспечивая O(log n) операции

- **AVL-деревья** обеспечивают строгую балансировку (|BF| ≤ 1), лучше для частого поиска

- **Красно-чёрные деревья** менее строгие, но требуют меньше поворотов, лучше для частых изменений

- **Выбор типа дерева** зависит от паттернов доступа: частый поиск → AVL, частые изменения → красно-чёрное

- **Применение:** индексы баз данных, упорядоченные структуры данных, компиляторы

---

## 🚀 Next Steps

**Related Modules:**

- [Индексные структуры данных](../14_Index_Data_Structures/) — изучите B-деревья для баз данных
- [Кучи и приоритетные очереди](../12_Heaps_And_Priority_Queues/) — изучите другую древовидную структуру

**Practice Ideas:**

1. Реализуйте базовые операции AVL-дерева
2. Сравните производительность AVL и красно-чёрных деревьев
3. Изучите применение сбалансированных деревьев в реальных системах

**Going Deeper:**

- Изучите детали реализации поворотов
- Познакомьтесь с другими типами сбалансированных деревьев (Splay trees, Treaps)
- Исследуйте применение в компиляторах и интерпретаторах

---


