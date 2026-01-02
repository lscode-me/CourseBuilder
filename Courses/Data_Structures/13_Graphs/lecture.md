# Графы
## Ориентированные и неориентированные графы, взвешенные графы и их представление

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать деревья как структуру данных
- Знать концепцию узлов и рёбер
- Понимать рекурсию и итерацию
- Иметь базовые знания о сложности алгоритмов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру графов и их типы
- Различать ориентированные и неориентированные графы
- Работать со взвешенными графами
- Выбирать подходящее представление графа для задачи

---

## 1. Введение: что такое граф

**Граф** — это структура данных, состоящая из:
- **Вершин (Vertices/Nodes):** точек данных

- **Рёбер (Edges):** связей между вершинами

Графы используются для моделирования связей и отношений: социальные сети, дорожные карты, компьютерные сети, зависимости в проектах.

---

## 2. Типы графов

### 2.1 Неориентированный граф

**Неориентированный граф** — граф, где рёбра не имеют направления. Если есть ребро между A и B, можно двигаться в обоих направлениях.

**Example: Неориентированный граф**

```python
class Graph:
    """Неориентированный граф через список смежности."""
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Добавить вершину."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        """Добавить ребро (неориентированное)."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)  # Обратное направление
    
    def get_neighbors(self, vertex):
        """Получить соседей вершины."""
        return self.graph.get(vertex, [])

# Создание графа

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

print(f"Соседи A: {g.get_neighbors('A')}")
print(f"Соседи B: {g.get_neighbors('B')}")
```

**Output:**
```
Соседи A: ['B', 'C']
Соседи B: ['A', 'C']
```

### 2.2 Ориентированный граф

**Ориентированный граф (Digraph)** — граф, где рёбра имеют направление. Ребро от A к B не означает, что можно двигаться от B к A.

**Example: Ориентированный граф**

```python
class DirectedGraph:
    """Ориентированный граф."""
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Добавить вершину."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex):
        """Добавить направленное ребро."""
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)
        # НЕ добавляем обратное направление
    
    def get_neighbors(self, vertex):
        """Получить соседей (только исходящие рёбра)."""
        return self.graph.get(vertex, [])

# Создание ориентированного графа

dg = DirectedGraph()
dg.add_edge('A', 'B')
dg.add_edge('A', 'C')
dg.add_edge('B', 'C')

print(f"Соседи A (исходящие): {dg.get_neighbors('A')}")
print(f"Соседи B (исходящие): {dg.get_neighbors('B')}")
print(f"Соседи C (исходящие): {dg.get_neighbors('C')}")
```

**Output:**
```
Соседи A (исходящие): ['B', 'C']
Соседи B (исходящие): ['C']
Соседи C (исходящие): []
```

### 2.3 Взвешенный граф

**Взвешенный граф** — граф, где каждое ребро имеет вес (стоимость, расстояние, время).

**Example: Взвешенный граф**

```python
class WeightedGraph:
    """Взвешенный граф."""
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Добавить вершину."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2, weight):
        """Добавить взвешенное ребро."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append((v2, weight))
        self.graph[v2].append((v1, weight))  # Неориентированный
    
    def get_neighbors(self, vertex):
        """Получить соседей с весами."""
        return self.graph.get(vertex, [])

# Создание взвешенного графа (дороги между городами)

wg = WeightedGraph()
wg.add_edge('Москва', 'СПб', 700)  # км
wg.add_edge('Москва', 'Казань', 800)
wg.add_edge('СПб', 'Казань', 1200)

print("Расстояния от Москвы:")
for city, distance in wg.get_neighbors('Москва'):
    print(f"  {city}: {distance} км")
```

**Output:**
```
Расстояния от Москвы:
  СПб: 700 км
  Казань: 800 км
```

---

## 3. Представление графов

### 3.1 Список смежности (Adjacency List)

**Список смежности** — для каждой вершины хранится список её соседей.

**Преимущества:**

- Эффективно по памяти O(V + E)
- Быстрый обход соседей
- Легко добавлять/удалять рёбра

**Недостатки:**

- Медленная проверка наличия ребра O(degree)

**Example: Список смежности**

```python
# Представление через словарь списков

adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B']
}

print("Список смежности:")
for vertex, neighbors in adjacency_list.items():
    print(f"  {vertex}: {neighbors}")
```

**Output:**
```
Список смежности:
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B']
  D: ['B']
```

### 3.2 Матрица смежности (Adjacency Matrix)

**Матрица смежности** — матрица размером V×V, где элемент [i][j] = 1, если есть ребро между i и j.

**Преимущества:**

- Быстрая проверка наличия ребра O(1)
- Простая реализация

**Недостатки:**

- Использует много памяти O(V²)
- Медленный обход всех соседей

**Example: Матрица смежности**

```python
# Матрица смежности

vertices = ['A', 'B', 'C', 'D']
n = len(vertices)
vertex_to_index = {v: i for i, v in enumerate(vertices)}

# Создание матрицы

adjacency_matrix = [[0] * n for _ in range(n)]

# Добавление рёбер

edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]
for v1, v2 in edges:
    i1, i2 = vertex_to_index[v1], vertex_to_index[v2]
    adjacency_matrix[i1][i2] = 1
    adjacency_matrix[i2][i1] = 1  # Неориентированный

print("Матрица смежности:")
print("   ", " ".join(vertices))
for i, vertex in enumerate(vertices):
    print(f"{vertex}: {' '.join(map(str, adjacency_matrix[i]))}")
```

**Output:**
```
Матрица смежности:
    A B C D
A: 0 1 1 0
B: 1 0 1 1
C: 1 1 0 0
D: 0 1 0 0
```

### 3.3 Сравнение представлений

| Операция | Список смежности | Матрица смежности |
|----------|------------------|-------------------|
| **Память** | O(V + E) | O(V²) |
| **Проверка ребра** | O(degree) | O(1) |
| **Обход соседей** | O(degree) | O(V) |
| **Добавление ребра** | O(1) | O(1) |
| **Удаление ребра** | O(degree) | O(1) |

---

## 4. Обход графа

### 4.1 Обход в глубину (DFS)

**Example: DFS для графа**

```python
def dfs(graph, start, visited=None):
    """Обход графа в глубину."""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Граф

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

result = dfs(graph, 'A')
print(f"DFS обход: {result}")
```

**Output:**
```
DFS обход: ['A', 'B', 'D', 'C', 'E']
```

### 4.2 Обход в ширину (BFS)

**Example: BFS для графа**

```python
from collections import deque

def bfs(graph, start):
    """Обход графа в ширину."""
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

result = bfs(graph, 'A')
print(f"BFS обход: {result}")
```

**Output:**
```
BFS обход: ['A', 'B', 'C', 'D', 'E']
```

---

## 5. Практические применения

### 5.1 Социальная сеть

**Example: Моделирование социальной сети**

```python
class SocialNetwork:
    """Социальная сеть как неориентированный граф."""
    def __init__(self):
        self.graph = {}
    
    def add_friendship(self, user1, user2):
        """Добавить дружбу (неориентированное ребро)."""
        if user1 not in self.graph:
            self.graph[user1] = []
        if user2 not in self.graph:
            self.graph[user2] = []
        
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)
    
    def get_friends(self, user):
        """Получить друзей пользователя."""
        return self.graph.get(user, [])
    
    def are_friends(self, user1, user2):
        """Проверить, друзья ли пользователи."""
        return user2 in self.graph.get(user1, [])

# Использование

network = SocialNetwork()
network.add_friendship('Alice', 'Bob')
network.add_friendship('Alice', 'Charlie')
network.add_friendship('Bob', 'David')

print(f"Друзья Alice: {network.get_friends('Alice')}")
print(f"Alice и Bob друзья: {network.are_friends('Alice', 'Bob')}")
```

**Output:**
```
Друзья Alice: ['Bob', 'Charlie']
Alice и Bob друзья: True
```

### 5.2 Дорожная сеть

**Example: Моделирование дорожной сети**

```python
class RoadNetwork:
    """Дорожная сеть как взвешенный граф."""
    def __init__(self):
        self.graph = {}
    
    def add_road(self, city1, city2, distance):
        """Добавить дорогу между городами."""
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))
    
    def get_connections(self, city):
        """Получить соединения города."""
        return self.graph.get(city, [])

# Использование

roads = RoadNetwork()
roads.add_road('Москва', 'СПб', 700)
roads.add_road('Москва', 'Казань', 800)
roads.add_road('СПб', 'Казань', 1200)

print("Дороги из Москвы:")
for city, distance in roads.get_connections('Москва'):
    print(f"  {city}: {distance} км")
```

**Output:**
```
Дороги из Москвы:
  СПб: 700 км
  Казань: 800 км
```

---

## 6. Специальные типы графов

### 6.1 Полный граф

**Полный граф** — граф, где каждая пара вершин соединена ребром.

### 6.2 Дерево как граф

**Дерево** — это связный ациклический граф с n вершинами и n-1 рёбрами.

### 6.3 Двудольный граф

**Двудольный граф** — граф, вершины которого можно разделить на два множества так, что рёбра соединяют только вершины из разных множеств.

---

## 💡 Key Takeaways

- **Граф** состоит из вершин и рёбер, моделирует связи и отношения

- **Неориентированный граф** — рёбра без направления; **ориентированный** — с направлением

- **Взвешенный граф** — рёбра имеют веса (стоимость, расстояние)

- **Представление:** список смежности эффективнее по памяти, матрица смежности быстрее для проверки рёбер

- **Обход:** DFS (в глубину) и BFS (в ширину) для навигации по графу

- **Применение:** социальные сети, дорожные карты, компьютерные сети, зависимости

---

## 🚀 Next Steps

**Related Modules:**

- [Индексные структуры данных](../14_Index_Data_Structures/) — изучите B-деревья
- [Структуры данных в реальных системах](../19_Data_Structures_In_Real_Systems/) — увидите применение графов

**Practice Ideas:**

1. Реализуйте граф с различными представлениями
2. Создайте модель социальной сети с поиском друзей
3. Реализуйте обходы графа (DFS и BFS)

**Going Deeper:**

- Изучите алгоритмы на графах (Дейкстра, Флойд-Уоршелл, минимальное остовное дерево)
- Познакомьтесь с топологической сортировкой
- Исследуйте применение графов в компиляторах и анализах зависимостей

---



