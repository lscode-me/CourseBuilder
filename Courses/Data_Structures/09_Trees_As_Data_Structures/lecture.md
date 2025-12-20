# Деревья как структуры данных
## Иерархические данные, узлы, корень и листья

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые структуры данных (массивы, списки)
- Знать концепцию рекурсии
- Понимать разницу между линейными и нелинейными структурами
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать концепцию деревьев как структуры данных
- Различать узлы, корень, листья и рёбра дерева
- Понимать иерархическую природу деревьев
- Знать основные термины и свойства деревьев

---

## 1. Введение: от линейных к иерархическим структурам

До сих пор мы изучали **линейные структуры данных**, где элементы расположены последовательно. Но многие данные в реальном мире имеют **иерархическую структуру**:

- Файловая система (папки и файлы)
- Организационная структура компании
- DOM дерево в HTML
- Генеалогическое дерево

**Дерево** — это структура данных, которая идеально подходит для представления таких иерархических отношений.

---

## 2. Что такое дерево

### 2.1 Определение дерева

**Дерево** — это связный ациклический граф. Это означает:
- **Связный**: от любого узла можно добраться до любого другого

- **Ациклический**: нет циклов (нельзя вернуться к узлу, пройдя по рёбрам)

**Альтернативное определение:** Дерево состоит из узлов, связанных рёбрами, где:
- Есть один специальный узел — **корень** (root)
- Каждый узел (кроме корня) имеет ровно одного родителя
- От корня можно добраться до любого узла

### 2.2 Основные компоненты дерева

**Example: Визуализация дерева**

```python

class TreeNode:
    """Узел дерева."""
    def __init__(self, data):
        self.data = data
        self.children = []  # Список дочерних узлов
    
    def add_child(self, child):
        """Добавить дочерний узел."""
        self.children.append(child)
    
    def __str__(self):
        return str(self.data)

# Создание простого дерева
root = TreeNode("Корень")
child1 = TreeNode("Ребёнок 1")
child2 = TreeNode("Ребёнок 2")
grandchild1 = TreeNode("Внук 1")
grandchild2 = TreeNode("Внук 2")

root.add_child(child1)
root.add_child(child2)
child1.add_child(grandchild1)
child1.add_child(grandchild2)

print(f"Корень: {root}")
print(f"Дети корня: {[str(c) for c in root.children]}")
print(f"Дети ребёнка 1: {[str(c) for c in child1.children]}")
```

**Output:**
```

Корень: Корень
Дети корня: ['Ребёнок 1', 'Ребёнок 2']
Дети ребёнка 1: ['Внук 1', 'Внук 2']
```

---

## 3. Терминология деревьев

### 3.1 Основные термины

**Узел (Node):** Элемент дерева, содержащий данные и ссылки на дочерние узлы.

**Корень (Root):** Верхний узел дерева, не имеющий родителя.

**Лист (Leaf):** Узел, не имеющий дочерних узлов.

**Родитель (Parent):** Узел, имеющий дочерние узлы.

**Ребёнок/Дочерний узел (Child):** Узел, имеющий родителя.

**Предок (Ancestor):** Любой узел на пути от корня до данного узла.

**Потомок (Descendant):** Любой узел в поддереве данного узла.

**Степень узла (Degree):** Количество дочерних узлов.

**Глубина узла (Depth):** Количество рёбер от корня до узла.

**Высота дерева (Height):** Максимальная глубина среди всех узлов.

**Example: Демонстрация терминов**

```python

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def is_root(self):
        """Проверить, является ли узел корнем."""
        return self.parent is None
    
    def is_leaf(self):
        """Проверить, является ли узел листом."""
        return len(self.children) == 0
    
    def get_degree(self):
        """Получить степень узла (количество детей)."""
        return len(self.children)
    
    def get_depth(self):
        """Получить глубину узла."""
        depth = 0
        current = self
        while current.parent:
            depth += 1
            current = current.parent
        return depth

# Создание дерева
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)

# Анализ узлов

print(f"Узел A - корень: {root.is_root()}, лист: {root.is_leaf()}, степень: {root.get_degree()}, глубина: {root.get_depth()}")
print(f"Узел B - корень: {b.is_root()}, лист: {b.is_leaf()}, степень: {b.get_degree()}, глубина: {b.get_depth()}")
print(f"Узел D - корень: {d.is_root()}, лист: {d.is_leaf()}, степень: {d.get_degree()}, глубина: {d.get_depth()}")
```

**Output:**
```

Узел A - корень: True, лист: False, степень: 2, глубина: 0
Узел B - корень: False, лист: False, степень: 2, глубина: 1
Узел D - корень: False, лист: True, степень: 0, глубина: 2
```

---

## 4. Типы деревьев

### 4.1 Бинарное дерево

**Бинарное дерево** — дерево, где каждый узел имеет не более двух дочерних узлов (левого и правого).

**Example: Бинарное дерево**

```python

class BinaryTreeNode:
    """Узел бинарного дерева."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Создание бинарного дерева
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print(f"Корень: {root.data}")
print(f"Левый ребёнок: {root.left.data}")
print(f"Правый ребёнок: {root.right.data}")
```

**Output:**
```

Корень: 1
Левый ребёнок: 2
Правый ребёнок: 3
```

### 4.2 N-арное дерево

**N-арное дерево** — дерево, где узел может иметь любое количество дочерних узлов.

**Example: N-арное дерево (общее дерево)**

```python

class GeneralTreeNode:
    """Узел общего дерева (N-арного)."""
    def __init__(self, data):
        self.data = data
        self.children = []

# Создание N-арного дерева
root = GeneralTreeNode("Корень")
root.children = [
    GeneralTreeNode("Ребёнок 1"),
    GeneralTreeNode("Ребёнок 2"),
    GeneralTreeNode("Ребёнок 3")
]

print(f"Корень имеет {len(root.children)} детей")
```

**Output:**
```

Корень имеет 3 детей
```

---

## 5. Обход дерева

### 5.1 Обход в глубину (DFS)

**Обход в глубину** — посещение узлов, уходя как можно глубже перед возвратом.

**Example: Рекурсивный обход в глубину**

```python

def dfs_traversal(node, result=None):
    """Обход дерева в глубину."""
    if result is None:
        result = []
    
    if node:
        result.append(node.data)  # Посещаем узел
        for child in node.children:
            dfs_traversal(child, result)  # Рекурсивно обходим детей
    
    return result

# Создание дерева
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)

# Обход

result = dfs_traversal(root)
print(f"Обход в глубину: {result}")
```

**Output:**
```

Обход в глубину: ['A', 'B', 'D', 'E', 'C']
```

### 5.2 Обход в ширину (BFS)

**Обход в ширину** — посещение узлов уровень за уровнем.

**Example: Обход в ширину**

```python

from collections import deque

def bfs_traversal(root):
    """Обход дерева в ширину."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        # Добавляем всех детей в очередь
        for child in node.children:
            queue.append(child)
    
    return result

# Использование того же дерева

result = bfs_traversal(root)
print(f"Обход в ширину: {result}")
```

**Output:**
```

Обход в ширину: ['A', 'B', 'C', 'D', 'E']
```

---

## 6. Высота и глубина дерева

### 6.1 Вычисление высоты

**Example: Вычисление высоты дерева**

```python

def get_height(node):
    """Вычислить высоту дерева."""
    if not node or node.is_leaf():
        return 0
    
    max_child_height = 0
    for child in node.children:
        child_height = get_height(child)
        max_child_height = max(max_child_height, child_height)
    
    return 1 + max_child_height

# Создание дерева
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
d.add_child(f)

height = get_height(root)
print(f"Высота дерева: {height}")
```

**Output:**
```

Высота дерева: 3
```

### 6.2 Вычисление глубины узла

**Example: Вычисление глубины**

```python

def get_depth(node):
    """Вычислить глубину узла."""
    depth = 0
    current = node
    while current.parent:
        depth += 1
        current = current.parent
    return depth

# Использование того же дерева

print(f"Глубина узла A: {get_depth(root)}")
print(f"Глубина узла B: {get_depth(b)}")
print(f"Глубина узла F: {get_depth(f)}")
```

**Output:**
```

Глубина узла A: 0
Глубина узла B: 1
Глубина узла F: 3
```

---

## 7. Балансировка деревьев

### 7.1 Что такое балансировка

**Балансированное дерево** — дерево, где разница высот левого и правого поддеревьев для каждого узла не превышает определённого значения (обычно 1).

**Несбалансированное дерево** может выродиться в связанный список, что ухудшает производительность.

**Example: Сравнение сбалансированного и несбалансированного дерева**

```python
# Несбалансированное дерево (вырожденное)
unbalanced_root = BinaryTreeNode(1)
unbalanced_root.right = BinaryTreeNode(2)
unbalanced_root.right.right = BinaryTreeNode(3)
unbalanced_root.right.right.right = BinaryTreeNode(4)

# Сбалансированное дерево
balanced_root = BinaryTreeNode(2)
balanced_root.left = BinaryTreeNode(1)
balanced_root.right = BinaryTreeNode(3)
balanced_root.right.right = BinaryTreeNode(4)

def count_nodes(node):
    """Подсчитать количество узлов."""
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def get_height_binary(node):
    """Высота бинарного дерева."""
    if not node:
        return -1
    return 1 + max(get_height_binary(node.left), get_height_binary(node.right))

print(f"Несбалансированное: узлов={count_nodes(unbalanced_root)}, высота={get_height_binary(unbalanced_root)}")
print(f"Сбалансированное: узлов={count_nodes(balanced_root)}, высота={get_height_binary(balanced_root)}")
```

**Output:**
```

Несбалансированное: узлов=4, высота=3
Сбалансированное: узлов=4, высота=2
```

**Вывод:** При одинаковом количестве узлов сбалансированное дерево имеет меньшую высоту.

### 7.2 Важность балансировки

Балансировка критична для производительности:

- **Сбалансированное дерево:** O(log n) для поиска, вставки, удаления

- **Несбалансированное дерево:** O(n) в худшем случае (вырождается в список)

---

## 8. Применение деревьев

### 8.1 Файловая система

**Example: Моделирование файловой системы**

```python

class FileSystemNode:
    """Узел файловой системы."""
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_path(self):
        """Получить полный путь."""
        path = [self.name]
        current = self.parent
        while current:
            path.insert(0, current.name)
            current = current.parent
        return "/" + "/".join(path)

# Создание файловой системы
root = FileSystemNode("", is_file=False)
home = FileSystemNode("home", is_file=False)
user = FileSystemNode("user", is_file=False)
documents = FileSystemNode("documents", is_file=False)
file1 = FileSystemNode("file1.txt", is_file=True)

root.add_child(home)
home.add_child(user)
user.add_child(documents)
documents.add_child(file1)

print(f"Путь к файлу: {file1.get_path()}")
```

**Output:**
```

Путь к файлу: /home/user/documents/file1.txt
```

### 8.2 Организационная структура

**Example: Иерархия компании**

```python

class Employee:
    """Сотрудник в организационной структуре."""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []
        self.manager = None
    
    def add_subordinate(self, employee):
        employee.manager = self
        self.subordinates.append(employee)
    
    def get_all_subordinates(self):
        """Получить всех подчинённых (рекурсивно)."""
        all_subs = []
        for sub in self.subordinates:
            all_subs.append(sub)
            all_subs.extend(sub.get_all_subordinates())
        return all_subs

# Создание структуры
ceo = Employee("Alice", "CEO")
cto = Employee("Bob", "CTO")
manager1 = Employee("Charlie", "Manager")
engineer1 = Employee("David", "Engineer")
engineer2 = Employee("Eve", "Engineer")

ceo.add_subordinate(cto)
cto.add_subordinate(manager1)
manager1.add_subordinate(engineer1)
manager1.add_subordinate(engineer2)

print(f"{ceo.name} ({ceo.position}) имеет {len(ceo.get_all_subordinates())} подчинённых")
print(f"{manager1.name} ({manager1.position}) имеет {len(manager1.subordinates)} прямых подчинённых")
```

**Output:**
```

Alice (CEO) имеет 4 подчинённых
Charlie (Manager) имеет 2 прямых подчинённых
```

---

## 9. Свойства деревьев

### 9.1 Основные свойства

1. **Количество рёбер:** В дереве с n узлами всегда n-1 рёбер
2. **Единственный путь:** Между любыми двумя узлами существует ровно один путь
3. **Связность:** Дерево всегда связно
4. **Ацикличность:** В дереве нет циклов

**Example: Проверка свойств**

```python

def count_edges(node, visited=None):
    """Подсчитать количество рёбер."""
    if visited is None:
        visited = set()
    
    if not node or node in visited:
        return 0
    
    visited.add(node)
    edges = len(node.children)
    
    for child in node.children:
        edges += count_edges(child, visited)
    
    return edges

def count_nodes(node, visited=None):
    """Подсчитать количество узлов."""
    if visited is None:
        visited = set()
    
    if not node or node in visited:
        return 0
    
    visited.add(node)
    count = 1
    
    for child in node.children:
        count += count_nodes(child, visited)
    
    return count

# Создание дерева
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

root.add_child(b)
root.add_child(c)
b.add_child(d)

nodes = count_nodes(root)
edges = count_edges(root)

print(f"Узлов: {nodes}, Рёбер: {edges}")
print(f"Свойство: рёбер = узлов - 1? {edges == nodes - 1}")
```

**Output:**
```

Узлов: 4, Рёбер: 3
Свойство: рёбер = узлов - 1? True
```

---

## 💡 Key Takeaways

- **Дерево** — это иерархическая структура данных, идеальная для представления отношений родитель-потомок

- **Основные компоненты:** узел, корень, лист, родитель, ребёнок, глубина, высота

- **Обход дерева** может быть в глубину (DFS) или в ширину (BFS)

- **Балансировка** критична для производительности: сбалансированное дерево обеспечивает O(log n) операции

- **Применение:** файловые системы, организационные структуры, DOM деревья, иерархические данные

---

## 🚀 Next Steps

**Related Modules:**

- [Бинарные деревья и деревья поиска](../10_Binary_Trees_And_Search_Trees/) — углубитесь в бинарные деревья
- [Сбалансированные деревья](../11_Balanced_Trees/) — изучите техники балансировки

**Practice Ideas:**

1. Реализуйте обход дерева в глубину и в ширину
2. Создайте модель файловой системы с использованием деревьев
3. Вычислите высоту и глубину узлов в дереве

**Going Deeper:**

- Изучите различные типы деревьев (бинарные, N-арные, полные, совершенные)
- Познакомьтесь с представлением деревьев в памяти
- Исследуйте применение деревьев в компиляторах и парсерах

---


