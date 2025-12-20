# Структуры данных как Архитектура
## От Queue и Map к Kafka и Redis

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовые структуры данных (Queue, Stack, Map, Tree, Graph)
- Понимать основы распределенных систем (Модуль 3)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Видеть дуальность "Code vs Architecture"
- Понимать, как локальная Queue превращается в Message Broker
- Понимать, как HashMap масштабируется до Key-Value Store
- Проектировать системы, используя паттерны структур данных

---

## 1. Изоморфизм "Код — Архитектура"

Главная идея этого модуля: **System Design — это просто структуры данных на стероидах**.
Все, что вы учили в курсе CS 101 (алгоритмы), имеет прямой аналог в архитектуре больших систем.

| Локальная Структура (In-Memory) | Распределенный Компонент (Architecture) |
| :--- | :--- |
| **Variable** | **Database Row** |
| **Hash Map** | **Key-Value Store (Redis, Memcached, Dynamo)** |
| **Queue (FIFO)** | **Message Broker (RabbitMQ, SQS, Kafka)** |
| **Log (Append-only)** | **Event Store / WAL / Kafka** |
| **Tree (B-tree)** | **Database Index / DOM / DNS** |
| **Graph** | **Knowledge Graph / Social Network Service** |

Если вы знаете, когда использовать `Queue` в коде, вы знаете, когда использовать RabbitMQ в архитектуре.

---

## 2. Queue -> Message Broker

### 2.1 Локальная очередь

В многопоточном коде мы используем `BlockingQueue`:

- Producer кладет задачу.
- Consumer (Worker Thread) забирает.
- **Цель**: Асинхронность, сглаживание пиков (buffering).

### 2.2 Распределенная очередь

В микросервисах мы используем брокер:

- Service A (Producer) кладет событие.
- Service B (Consumer) забирает.
- **Цель**: Decoupling (слабая связанность), надежность (retries).

**Пример (Python -> System)**:
```python
# Code
q = Queue()
def producer(): q.put(data)
def consumer(): process(q.get())

# Architecture
# [Service A] -> (Network/Redis) -> [Service B]

```

### 2.3 Dead Letter Queue (DLQ)

Что делать, если `process(task)` падает с исключением?

- В коде: `try-except`, логируем ошибку.
- В архитектуре: Перекладываем сообщение в **DLQ** (Dead Letter Queue) — отдельную очередь "для плохих сообщений", чтобы разобрать их вручную позже.

---

## 3. Map -> Key-Value Store

### 3.1 Локальный словарь

`cache = {}`
Самый быстрый способ доступа O(1).
Проблема: Данные пропадают при перезапуске (Volatile) и ограничены RAM одной машины.

### 3.2 Распределенный Map

**Redis / Memcached**.
Это буквально огромный Hash Map, доступный по сети.

- **Sharding**: Если данных много, бьем ключи на шарды (как бакеты в хеш-таблице).

- **TTL**: В коде мы чистим кеш вручную, в Redis есть `Expire`.

**Паттерн: Write-Through vs Write-Back**
- В процессоре есть L1/L2 Cache.
- В системе есть Redis перед Postgres.
Логика идентична.

---

## 4. Tree -> Hierarchy & Routing

### 4.1 Деревья в коде

DOM (Document Object Model) — это дерево.
AST (Abstract Syntax Tree) — это дерево.

### 4.2 Деревья в архитектуре

1.  **DNS (Domain Name System)**: Глобальное, распределенное дерево.
    `Root (.) -> com -> google -> www`
2.  **Filesystems (S3 Prefixes)**: Иерархия папок.
3.  **URL Routing**: `/api/v1/users/{id}` — это префиксное дерево (Trie).
4.  **Zookeeper**: Хранит конфигурацию в виде дерева ZNodes.

---

## 5. Graph -> Connections

### 5.1 Графы в коде

Матрица смежности, списки смежности. Поиск кратчайшего пути (Dijkstra).

### 5.2 Графы в архитектуре

Когда данных много (Facebook, LinkedIn), SQL `JOIN` умирает.
Нужны **Graph Databases** (Neo4j).
Они оптимизированы для "хождений" по связям (Pointer chasing), а не сканирования таблиц.

*Пример*: "Найти друзей друзей, которые лайкнули этот пост".
В графе это локальный обход. В SQL это 3 heavy joins.

---

## 6. Stack -> Undo/Navigation

### 6.1 Стек в коде

Вызов функций (Call Stack), парсинг выражений.

### 6.2 Стек в архитектуре

1.  **Browser History**: Кнопка "Back".
2.  **Undo/Redo Command Pattern**: Стек операций пользователя.
3.  **Saga Compensation**: Если транзакция упала, мы выполняем компенсирующие действия в обратном порядке (как размотка стека).

---

## 7. Практическое задание: Design Twitter

Давайте спроектируем Twitter, используя только термины структур данных (примитивная модель).

**Requirements**:
1.  Post tweet.
2.  Follow user.
3.  View Home Timeline.

**Architectural Mapping**:

1.  **Users Table**: Partitioned Hash Map.
    `Key: UserID -> Value: {ProfileData}`

2.  **Social Graph (Followers)**: Adjacency List (Graph).
    `Key: UserID -> Value: [List of FollowerIDs]`
    *Где хранить?* Graph DB или Redis Set.

3.  **Tweets**: Append-only Log (per user).
    `Key: UserID -> Value: [Tweet1, Tweet2, ...]`

4.  **Home Timeline (Fan-out on write)**:
    Когда Илон Маск пишет твит:

    - Получаем список фолловеров (Graph traversal).
    - Для каждого фолловера пишем ID твита в его личную **Queue** (Timeline).
    - Пользователь читает свою Queue (O(1)).

```python

class TwitterSystem:
    def __init__(self):
        self.users = {} # Map
        self.graphs = {} # Graph (User -> [Followers])
        self.timelines = {} # Queue (User -> [Tweets])
        
    def post(self, user_id, content):
        # 1. Save tweet (Log)
        tweet = {"id": 123, "content": content}
        
        # 2. Fan-out (Queue push)
        followers = self.graphs.get(user_id, [])
        for f in followers:
            self.timelines.setdefault(f, []).append(tweet)
            
    def get_timeline(self, user_id):
        # O(1) read
        return self.timelines.get(user_id, [])
```

Это упрощенная модель того, как работает реальный Twitter/Instagram.

---

## 💡 Key Takeaways

- Не бойтесь System Design. Это те же структуры данных, только распределенные по сети и жестким дискам.
- **Latency**: Обращение к RAM (Hash Map) — наносекунды. Обращение к Redis (Network Map) — миллисекунды. Это коэффициент масштаба.

- **Database** — это сложная структура данных, сохраняемая на диск.
- Любую сложную систему можно декомпозировать на Queues, Logs, Maps и Trees.

---

## 🚀 Next Steps

**Related Modules:**

- [Choosing DS for System Design](../14_Choosing_DS_For_System_Design/) — как выбирать конкретные базы данных под задачу.
- [Case Studies](../16_Case_Studies/) — разбор реальных систем.

**Practice Ideas:**

1. Возьмите любую программу, которую вы писали (чат, todo list), и распишите, какие "взрослые" компоненты заменили бы ваши переменные.
2. Спроектируйте URL Shortener (bit.ly), используя только Maps и Counters.

---

