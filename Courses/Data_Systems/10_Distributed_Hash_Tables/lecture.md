# Распределенные хеш-таблицы (DHT) и Consistent Hashing
## Шардинг данных, кольцо хеширования и виртуальные узлы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу обычной хеш-таблицы (Hash Map)
- Знать, что такое хеш-функция
- Понимать проблему горизонтального масштабирования (Scaling Out)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять проблему "сдвига" ключей при наивном шардинге
- Реализовывать алгоритм Consistent Hashing
- Понимать роль виртуальных узлов (VNodes)
- Описывать архитектуру Dynamo-style баз данных (Cassandra, Riak)

---

## 1. Проблема масштабирования Hash Map

Представьте, что вы хотите сделать распределенный Key-Value кэш (как Memcached или Redis Cluster). Данных слишком много для одного сервера. Вам нужно распределить ключи по $N$ серверам.

### 1.1 Наивный подход: Modulo Sharding

Самый простой способ выбрать сервер для ключа $K$:
$$ \text{ServerIndex} = \text{hash}(K) \pmod N $$

```python
# Наивный шардинг
servers = ['Node A', 'Node B', 'Node C']
N = len(servers)

def get_server_naive(key):
    h = hash(key)
    return servers[h % N]

print(f"Key 'user_1' -> {get_server_naive('user_1')}")
print(f"Key 'user_2' -> {get_server_naive('user_2')}")
```

### 1.2 Проблема: Rebalancing

Что произойдет, если мы добавим один сервер? $N$ изменится с 3 на 4.
Формула $\text{hash}(K) \pmod 4$ вернет совершенно другие результаты, чем $\text{hash}(K) \pmod 3$.

**Effect**: Почти все ключи (примерно $1 - 1/N$) меняют свое местоположение.
Если у вас 100 ТБ данных в кэше, добавление 1 сервера заставит переместить 75 ТБ данных между узлами. Это "Cache Stampede" — сеть ляжет, база данных под кэшем умрет от нагрузки.

---

## 2. Consistent Hashing

**Consistent Hashing (Согласованное хеширование)** — алгоритм, который минимизирует перемещение данных при изменении количества узлов. При добавлении/удалении узла перемещаются только ключи, принадлежащие этому узлу (в среднем $K/N$ ключей).

Идея: расположить и серверы, и ключи на одном "Кольце" (Hash Ring).

### 2.1 Кольцо

Представим пространство хешей как кольцо (от 0 до $2^{32}-1$).

1.  **Помещаем серверы на кольцо**: Хешируем имя сервера (или IP).
    $\text{Pos}(S_1) = \text{hash}("Node A")$
    $\text{Pos}(S_2) = \text{hash}("Node B")$

2.  **Помещаем ключи на кольцо**: Хешируем данные.
    $\text{Pos}(Key) = \text{hash}("user\_1")$

3.  **Поиск сервера**: Чтобы найти сервер для ключа, идем по часовой стрелке от позиции ключа до первого встреченного сервера.

```

Кольцо (0 - 100):
Node A: 20
Node B: 60
Node C: 90

Key 1 (Pos 10) -> (идем по часовой) -> Node A (20)
Key 2 (Pos 40) -> Node B (60)
Key 3 (Pos 95) -> (переход через 0) -> Node A (20)
```

### 2.2 Добавление узла

Допустим, добавляем **Node D** на позицию 40.

*   **Key 1 (Pos 10)** -> был Node A, остался Node A.

*   **Key 2 (Pos 40)** -> был Node B, стал **Node D**!

*   **Key 3 (Pos 95)** -> был Node A, остался Node A.

Изменился только сегмент кольца между Node A (20) и Node B (60). Данные с Node B частично переезжают на Node D, частично остаются. Остальные узлы не тронуты.

### 2.3 Реализация (Python)

```python

import hashlib
import bisect

class ConsistentHash:
    def __init__(self, nodes=None):
        self.ring = {} # hash -> node_name
        self.sorted_keys = [] # Отсортированный список хешей для бинарного поиска
        
        if nodes:
            for node in nodes:
                self.add_node(node)
                
    def _hash(self, key):
        # Используем MD5 для стабильности результатов, берем первые 4 байта как int
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)
        
    def add_node(self, node):
        key = self._hash(node)
        self.ring[key] = node
        bisect.insort(self.sorted_keys, key)
        
    def remove_node(self, node):
        key = self._hash(node)
        del self.ring[key]
        self.sorted_keys.remove(key)
        
    def get_node(self, item):
        if not self.ring:
            return None
        
        key = self._hash(item)
        
        # Бинарный поиск первого узла справа (по часовой стрелке)
        idx = bisect.bisect_right(self.sorted_keys, key)
        
        if idx == len(self.sorted_keys):
            # Замыкаем кольцо: берем первый узел
            idx = 0
            
        return self.ring[self.sorted_keys[idx]]

# Тест
ch = ConsistentHash(['Node-A', 'Node-B', 'Node-C'])

print(f"User1 -> {ch.get_node('User1')}")
print(f"User2 -> {ch.get_node('User2')}")
print(f"User3 -> {ch.get_node('User3')}")

print("\nAdding Node-D...")
ch.add_node('Node-D')

print(f"User1 -> {ch.get_node('User1')}")
print(f"User2 -> {ch.get_node('User2')}")
print(f"User3 -> {ch.get_node('User3')}")
```

**Output:**
```

User1 -> Node-B
User2 -> Node-A
User3 -> Node-C

Adding Node-D...
User1 -> Node-D  <-- Изменился (переехал с B на D)
User2 -> Node-A  <-- Не изменился
User3 -> Node-C  <-- Не изменился
```

---

## 3. Виртуальные узлы (Virtual Nodes)

### 3.1 Проблема неравномерности

В "голом" Consistent Hashing, если узлов мало (например, 3), распределение хешей может быть неравномерным.
Один узел может случайно получить "большой кусок" кольца (50% данных), а другой — маленький (10%).

Кроме того, если у нас есть мощный сервер и слабый сервер, мы хотим, чтобы мощный хранил больше данных.

### 3.2 VNodes

Вместо того чтобы ставить один сервер в одну точку кольца, мы разбиваем его на $K$ **виртуальных узлов** (VNodes) и раскидываем их по кольцу.

*   **Node A** -> VNode A1, VNode A2, ..., VNode A100.

*   **Node B** -> VNode B1, VNode B2, ..., VNode B100.

Это дает:

1.  **Равномерное распределение**: Статистически данные "размазываются" ровно.
2.  **Гетерогенность**: Мощному серверу можно дать 200 VNodes, слабому — 50.

```python

    def add_node(self, node, weight=1):
        # Создаем 'weight' виртуальных копий
        for i in range(weight):
            vnode_key = f"{node}#{i}"
            key = self._hash(vnode_key)
            self.ring[key] = node # Указывает на физический узел
            bisect.insort(self.sorted_keys, key)
```

---

## 4. Репликация в DHT

Как обеспечить надежность? В DHT обычно используется стратегия:

**"Store on Next N Nodes"**.

Ключ $K$ попадает на узел $S_1$ (Coordinator).
Система также копирует $K$ на $S_2$ и $S_3$ — следующие по часовой стрелке узлы в кольце.

*   Важно: нужно выбирать следующие *физические* узлы, пропуская VNodes того же сервера.

Это используется в:

- **Cassandra**: Partition Key определяет позицию в кольце.

- **DynamoDB**: Внутренне использует кольцо для партиционирования.

- **Riak**: Классическая реализация Dynamo paper.

- **Chord**: P2P протокол для поиска в DHT.

---

## 5. Peer-to-Peer vs Coordinator

Как клиент узнает, на каком узле данные?

1.  **Smart Client**: Клиент знает топологию кольца (скачивает карту при старте) и сам вычисляет узел. (Cassandra drivers).
2.  **Proxy / Load Balancer**: Клиент идет на балансировщик, тот перенаправляет.
3.  **Gossip / Coordinator**: Клиент идет на *любой* узел. Этот узел (Coordinator) смотрит на кольцо и пересылает запрос нужному узлу.

---

## 6. Rendezvous Hashing (HRW)

Альтернатива Consistent Hashing.

**Highest Random Weight (HRW)** hashing:
Для каждого ключа $K$ и каждого сервера $S_i$ вычисляем вес $W = \text{hash}(K, S_i)$.
Выбираем сервер с максимальным $W$.

Плюсы:

- Нет состояния (кольца).
- Идеальное распределение.
Минусы:

- При каждом запросе нужно считать $N$ хешей (линейная зависимость от числа серверов).
- Хорошо работает для малого числа серверов (Proxy servers, Caches), но плохо для тысяч узлов.

---

## 💡 Key Takeaways

- **Modulo Sharding** плох для систем с меняющимся числом узлов (массовые миграции данных).

- **Consistent Hashing** (Hash Ring) решает проблему ребалансировки, перемещая только $1/N$ ключей.

- **Virtual Nodes (VNodes)** нужны для балансировки нагрузки и учета мощности серверов.

- **Репликация** в кольце делается на $N$ следующих узлов по часовой стрелке.
- Эта технология лежит в основе многих NoSQL баз данных (Cassandra, Dynamo).

---

## 🚀 Next Steps

**Related Modules:**

- [Репликация и согласованность](../11_Replication_And_Consistency/) — как синхронизировать данные между узлами кольца.
- [CAP теорема](../09_Distributed_Challenges/) — как DHT ведет себя при сбоях (обычно это AP системы).

**Practice Ideas:**

1. Реализуйте Consistent Hashing с VNodes на Python.
2. Визуализируйте кольцо и распределение ключей при N=3 и N=4.
3. Напишите симулятор: 10000 ключей, добавление узла, подсчет % перемещенных ключей.

---

