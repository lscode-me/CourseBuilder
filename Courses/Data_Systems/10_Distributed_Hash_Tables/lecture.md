# Distributed Hash Tables (DHT)
## Consistent Hashing, Chord, Gossip и Merkle Trees

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **Hashing**: Понимать, что хеш-функция (MD5/SHA) детерминирована и равномерно распределяет ключи.

- **Network**: Знать, что IP адрес — это идентификатор узла.

- **Big O**: Понимать разницу между $O(N)$ и $O(\log N)$.

- **Trees**: Знать структуру бинарного дерева.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Sharding**: Реализовать Consistent Hashing Ring для добавления/удаления узлов без решардинга всего кластера (перемещение $K/N$ ключей).

- **Balancing**: Использовать Virtual Nodes (VNodes) для устранения перекосов (Data Skew).

- **Routing**: Объяснять, как Chord находит узел за $O(\log N)$ шагов, используя Finger Table.

- **Synchronization**: Реализовать Merkle Tree для быстрого сравнения данных между репликами.

- **Discovery**: Написать симуляцию Gossip Protocol и понимать, за сколько раундов информация дойдет до всех.

---

## 1. Проблема масштабирования: `hash(key) % N`

Представьте, вы строите распределенный кэш (как Memcached).
У вас 4 сервера (`N=4`). Как узнать, на каком сервере лежит ключ `user_123`?

**Наивный подход**:
`server_index = hash("user_123") % 4`

*   `hash("user_123") = 99`.
*   `99 % 4 = 3`. (Сервер №3).

Все работает идеально. Нагрузка распределена равномерно (25% на сервер). Поиск — $O(1)$.

### Авария (Cluster Resizing)

Сервер 3 сгорел. Осталось 3 сервера (`N=3`).
Теперь формула поиска: `hash("user_123") % 3`.

*   `99 % 3 = 0`. (Сервер №0).
*   Вчера ключ был на 3, сегодня мы ищем на 0. Мы получили **Cache Miss**.

Это полбеды. Беда в том, что формула сменилась для **ВСЕХ** ключей.
`hash("user_456") = 100`. Было `100 % 4 = 0`. Стало `100 % 3 = 1`.
Почти 100% ключей сменили "прописку".
Весь кэш инвалидирован. Вся нагрузка пришла в базу данных. База упала.
Это называется **Rehashing Storm**.

Нам нужен алгоритм, при котором добавление/удаление узла перемещает лишь минимальное количество ключей ($1/N$).

---

## 2. Consistent Hashing (Согласованное хеширование)

Дэвид Каргер (MIT) и Дэниел Левин (основатель Akamai) решили эту задачу в 1997.

**Идея**: Замкнуть пространство хешей в кольцо.
Представьте окружность от $0$ до $2^{32}-1$.

### 2.1 Алгоритм

1.  **Placement**: Хешируем IP адреса серверов и ставим точки на кольце.
    *   Node A: Hash("10.0.0.1") -> 100.
    *   Node B: Hash("10.0.0.2") -> 500.
    *   Node C: Hash("10.0.0.3") -> 900.
2.  **Assignment**: Хешируем Ключ данных. Идем по часовой стрелке до первого сервера. Этот сервер — "Владелец".
    *   Key K1 (Hash=150) -> Идем по кругу -> Node B (500).
    *   Key K2 (Hash=700) -> Идем по кругу -> Node C (900).
    *   Key K3 (Hash=950) -> Wrap around -> Node A (100).

### 2.2 Добавление узла

Добавляем Node D (Hash=300). Он встает между A и B.

*   Ключи в диапазоне (100, 300], которые раньше принадлежали B, теперь принадлежат D.
*   Ключи > 300 все еще принадлежат B.
Перемещаются только ключи, попавшие в новый сегмент. Ключи на C и A не тронуты.

**Win**: При изменении $N$ мы перемещаем $K/N$ данных.

### 2.3 Virtual Nodes (VNodes) — Решение проблемы перекосов

Наивное кольцо имеет проблему: хеши случайны. Node A может занять дугу в 10°, а Node B в 100°.
Node B будет перегружен в 10 раз.

**Решение**:
Один физический сервер представлен на кольце **множеством** (например, 256) виртуальных точек.
`Node A_0, Node A_1 ... Node A_255`.
Эти точки перемешаны с точками Node B и Node C.
По закону больших чисел, сумма маленьких дуг Node A будет примерно равна сумме дуг Node B.
Распределение нагрузки становится почти идеальным.

### 2.4 Code: Consistent Hash Ring

```python

import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas=100):
        self.replicas = replicas # VNodes per server
        self.ring = {} # hash -> server_ip
        self.sorted_keys = []

    def _hash(self, key):
        # Используем MD5 для хорошего распределения
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node_ip):
        for i in range(self.replicas):
            vnode_key = f"{node_ip}:{i}"
            h = self._hash(vnode_key)
            self.ring[h] = node_ip
            bisect.insort(self.sorted_keys, h)

    def remove_node(self, node_ip):
        # Найти и удалить все 100 виртуальных узлов
        hashes_to_remove = [h for h, ip in self.ring.items() if ip == node_ip]
        for h in hashes_to_remove:
            del self.ring[h]
            self.sorted_keys.remove(h)

    def get_node(self, key):
        if not self.ring: return None
        h = self._hash(key)
        
        # Бинарный поиск: найти первый узел справа
        idx = bisect.bisect(self.sorted_keys, h)
        
        if idx == len(self.sorted_keys):
            idx = 0 # Wrap around (Кольцо!)
            
        return self.ring[self.sorted_keys[idx]]

# Simulation
ring = ConsistentHashRing(replicas=50)
ring.add_node("10.0.0.1")
ring.add_node("10.0.0.2")
ring.add_node("10.0.0.3")

# Check distribution

counts = {"10.0.0.1":0, "10.0.0.2":0, "10.0.0.3":0}
for i in range(10000):
    node = ring.get_node(f"user_{i}")
    counts[node] += 1
    
print(f"Distribution: {counts}") 
# Ожидаем примерно 3333 на каждом

```

---

## 3. Chord Protocol: Поиск в глобальном интернете

Consistent Hashing говорит, *где* лежат данные. Но как *найти* этот сервер, если серверов 1 миллион (P2P сеть), и ты знаешь только IP своего соседа?
Держать таблицу всех IP в памяти невозможно.

**Chord** (MIT, 2001) предлагает решение: каждый узел знает лишь о небольшом числе соседей ("Пальцев").

### Finger Table

В кольце размером $M$ бит ($2^M$ адресов), у каждого узла есть таблица из $M$ записей.
$i$-я запись таблицы узла $N$ указывает на узел, ответственный за ключ $N + 2^{i-1}$.

*   Finger 1: $N+1$ (прямой сосед).
*   Finger 2: $N+2$.
*   Finger 3: $N+4$.
*   Finger 10: $N+512$.
*   ...

Это позволяет "прыгать" через пол-кольца, потом через четверть, потом через 1/8.

**Сложность поиска**: $O(\log N)$. Точно как бинарный поиск, но в кольце.

### Routing Example

Пусть Node 1 ищет Key 54.

*   Node 1 смотрит в Finger Table: "У меня есть прыжок на 32 (Node 32) и на 64 (не подходит)".
*   Node 1 шлет запрос в Node 32: "Найди 54".
*   Node 32 смотрит Fingers: "У меня есть прыжок на 48...".
*   Процесс сходится экспоненциально быстро.

---

## 4. Gossip Протокол: Эпидемия знаний

Как кластер DynamoDB или Cassandra узнает, что узел X умер, а узел Y поднялся?
Центральный мастер (ZooKeeper) может стать узким местом.
Gossip (Сплетни) — децентрализованный протокол.

**Алгоритм**:
1.  Каждую секунду каждый узел выбирает случайного соседа.
2.  Шлет ему свою версию состояния ("Я жив v10, Узел А мертв v5").
3.  Сосед сравнивает версии и обновляет свои знания (Merge).

**Математика**:
Информация распространяется как вирус (логистическая кривая).
Время полного заражения кластера $N$: $O(\log N)$.
Для 1000 узлов "сплетня" дойдет до всех за ~10-15 раундов (секунд).
Это делает систему **Eventual Consistent**.

**Python Simulation: Gossip**

```python

import random

NUM_NODES = 100
INFECTED = {0} # Patient Zero (знает новость)
ROUNDS = 0

while len(INFECTED) < NUM_NODES:
    newly_infected = set()
    for node in INFECTED:
        # Каждый зараженный звонит случайному партнеру
        partner = random.randint(0, NUM_NODES - 1)
        newly_infected.add(partner)
    
    INFECTED.update(newly_infected)
    ROUNDS += 1
    print(f"Round {ROUNDS}: {len(INFECTED)} nodes know.")

print(f"Cluster synced in {ROUNDS} rounds.")
```

---

## 5. Anti-Entropy: Merkle Trees

Реплики могут рассинхронизироваться тихо (Bit rot, пропущенное сообщение).
Нам нужен протокол Anti-Entropy, чтобы сверять данные.
Передавать все данные дорого.
Передавать хеш всех данных (`md5(AllDB)`) ненадежно (если не совпал, непонятно где ошибка).

**Merkle Tree** (Хеш-дерево):
1.  Разбиваем данные на блоки. Считаем хеш каждого блока (листья).
2.  Группируем хеши пар и считаем хеш от них (Parent = Hash(Left + Right)).
3.  Повторяем до корня (Root Hash).

**Сверка**:
1.  Узлы A и B сравнивают Root Hash.
2.  Если совпадает -> Данные идентичны.
3.  Если нет -> Скачивают хеши детей (Left, Right).
4.  Если Left совпадает -> Проблема в Right.
5.  Спускаемся рекурсивно, пока не найдем конкретный лист (блок), который отличается.
6.  Синхронизируем **только этот блок**.

**Применение**:
*   Amazon DynamoDB (detecting entropy).
*   Cassandra (`nodetool repair`).
*   Bitcoin (проверка транзакций в блоке).
*   Git (структура коммитов — это Merkle DAG).

```python

import hashlib

def get_hash(val):
    return hashlib.sha256(val.encode()).hexdigest()

class MerkleNode:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        if data:
            self.hash = get_hash(data)
        else:
            # Hash of children hashes
            self.hash = get_hash((left.hash if left else "") + (right.hash if right else ""))

def build_merkle(data_list): # Упрощенно
    nodes = [MerkleNode(data=d) for d in data_list]
    while len(nodes) > 1:
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i+1] if i+1 < len(nodes) else None
            new_level.append(MerkleNode(left, right))
        nodes = new_level
    return nodes[0] # Root

# Test
db_version_a = ["Row1", "Row2", "Row3", "Row4"]
db_version_b = ["Row1", "Row2", "Row3_MODIFIED", "Row4"]

tree_a = build_merkle(db_version_a)
tree_b = build_merkle(db_version_b)

print(f"Root A: {tree_a.hash}")
print(f"Root B: {tree_b.hash}")
# Roots differ -> Drill down

if tree_a.left.hash == tree_b.left.hash:
    print("Left branch OK")
else:
    print("Diff in Left")

if tree_a.right.hash == tree_b.right.hash:
    print("Right branch OK")
else:
    print("Diff in Right branch (Row3 vs Row3_MODIFIED)")
```

---

## 6. Glossary

*   **DHT (Distributed Hash Table)**: Класс децентрализованных распределенных систем, обеспечивающих lookup сервис похожий на hash table: (key, value).

*   **Consistent Hashing**: Метод распределения ключей, где добавление слота не меняет маппинг всех ключей, а только соседей.

*   **Virtual Node (VNode)**: Виртуальная сущность узла на кольце хеширования для статистически равномерного распределения.

*   **Chord**: P2P протокол поиска узла с кольцевой топологией и логарифмической сложностью.

*   **Finger Table**: Таблица маршрутизации в Chord, содержащая ссылки на узлы с экспоненциальным шагом ($2^i$).

*   **Gossip Protocol (Epidemic Protocol)**: Протокол распространения информации "от соседа к соседу". Случайный, надежный, масштабируемый.

*   **Convergence**: Состояние, когда все узлы кластера имеют одинаковое представление о данных/топологии.

*   **Merkle Tree**: Дерево хешей для эффективной сверки больших объемов данных с минимизацией трафика.

*   **Stabilization**: Периодический процесс в Chord/DHT для проверки правильности соседей и обновления Finger Table.

*   **Sloppy Quorum**: Кворум, в который могут входить любые N доступных узлов (используется для High Availability).

*   **Hinted Handoff**: Механизм передачи данных "заместителю", если целевой узел недоступен, с последующим возвратом.

*   **Key Space**: Диапазон возможных значений хеша (обычно $0..2^{160}-1$ для SHA-1).

---

## 📚 Appendix A: Troubleshooting Guide

### A.1 Symptom: Hotspots (Перегрев одного узла)

**Симптом**: CPU 100% на одном узле, остальные прохлаждаются. Задержка запросов к этому узлу растет.
**Причина**:
1.  **Poor Hashing**: Хеш-функция не дает Uniform Distribution.
2.  **Insufficient VNodes**: Мало виртуальных узлов, серверу "повезло" захватить большой кусок кольца.
3.  **Key Popularity (Justin Bieber effect)**: Один ключ (напр. профиль звезды) запрашивают миллион раз. Consistent Hashing тут не поможет (он балансирует ключи, а не запросы).
**Лечение**:
1.  Увеличьте число VNodes (num_tokens в Cassandra default 256).
2.  Для "горячих ключей": Кэширование на клиенте или добавление случайного суффикса при чтении (Scatter-Gather).

### A.2 Symptom: Slow Convergence (Кластер "тупит" при сбоях)

**Симптом**: Узел упал, но клиенты продолжают долбиться в него. Балансировщик не видит падения.
**Причина**: Gossip слишком медленный. Интервал опроса велик или порог детектора сбоев (Failure Detector) слишком консервативен.
**Лечение**:
1.  Настройка **Phi Accrual Failure Detector**: Вместо бинарного "жив/мертв", он выдает вероятность ошибки. Это позволяет адаптироваться к лагам сети.
2.  Уменьшить Gossip Interval (но следите за трафиком управления!).

---

## 📚 Appendix B: Historical Context

### 1999: Napster

Первый P2P. Но не настоящий. У него был **Центральный сервер** индексации.
Когда власти США закрыли сервер — сеть умерла. Это SPOF (Single Point of Failure).

### 2000: Gnutella

Полная децентрализация. Поиск методом "заливки" (Flood).
"У кого есть песня Х?" -> перешли всем соседям.
Сеть задохнулась от трафика. Не масштабировалось.

### 2001: The DHT Breakthrough (Chord, Pastry, Kademlia)

В MIT придумали Chord. Структурированный P2P.
Теперь поиск был эффективным ($O(\log N)$) и без центрального сервера.

**Kademlia** (использует XOR метрику) стала основой BitTorrent и Ethereum.

### 2007: Amazon Dynamo

Вернер Фогельс опубликовал Dynamo Paper.
"Мы взяли P2P технологии (Consistent Hashing, Gossip, Merkle Tree) и применили их внутри доверенного датацентра для построения надежного Key-Value хранилища".
Так родилась современная NoSQL революция. Cassandra — прямой потомок Dynamo.

---

## 📚 Appendix C: FAQ (Часто задаваемые вопросы)

**Q1: Где на практике я встречу Consistent Hashing?**
**A**:
1.  **Load Balancers**: Распределение липких сессий (Sticky Sessions).
2.  **Client-side sharding**: Библиотеки Memcached/Redis на клиенте сами выбирают сервер.
3.  **Sharded Databases**: Cassandra, Riak, DynamoDB.

**Q2: Почему VNodes лучше, чем просто много физических узлов?**
**A**: VNodes позволяют балансировать гетерогенное железо. Мощному серверу можно дать 500 токенов, а слабому — 100. Они будут получать пропорциональную нагрузку.

**Q3: Зачем Gossip, если есть ZooKeeper?**
**A**: ZooKeeper — это CP система (строгая согласованность). Он плохо масштабируется на запись (все пишут через Лидера). Gossip — AP система. Он масштабируется линейно, но дает лишь Eventual Consistency. Cassandra выбрала Gossip для децентрализации. Kafka выбрала ZK (а теперь Raft) для управления.

**Q4: Как удалить данные из Merkle Tree?**
**A**: Вы удаляете лист, пересчитываете хеш родителя, и так до корня. Это $O(\log N)$ операция. Дерево всегда консистентно.

**Q5: Может ли хеш-функция "сломаться"?**
**A**: Для криптографии MD5 сломан (коллизии). Для Hash Map/Ring — коллизии допустимы, если их мало. Главное свойство здесь — Avalanche Effect (лавина): изменение 1 бита ключа меняет половину битов хеша, разбрасывая близкие ключи по разным серверам.

---

## 💡 Key Takeaways

1.  **Rings > Lists**: Кольцевая топология упрощает логику "соседа".
2.  **Log N**: Магия масштабирования. Вы можете найти иголку в стоге сена из миллиарда узлов за 30 шагов.
3.  **Epidemics work**: Gossip протоколы надежнее центральных реестров.
4.  **Verification**: Merkle Trees позволяют дешево проверить целостность дорогих данных.

---

## 🚀 Next Steps

**Практика:**

1.  Реализуйте Consistent Hash Ring с визуализацией (ASCII круг).
2.  Добавьте метод `add_node` и посчитайте, какой процент ключей реально переехал. Убедитесь, что это близко к теоретическому $1/N$.

В следующем модуле мы перейдем к тому, как узлы договариваются друг с другом в условиях хаоса. [Replication And Consistency](../11_Replication_And_Consistency/).

