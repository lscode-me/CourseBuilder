# Протоколы распределённых систем
## Consensus, Leader election, Heartbeats, Failure detection

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые протоколы передачи сообщений (модуль 05)
- Понимать протоколы между компонентами (модуль 15)
- Иметь представление о распределённых системах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать протоколы consensus для согласованности данных
- Применять протоколы leader election для координации
- Использовать heartbeats для мониторинга состояния
- Обнаруживать отказы через failure detection протоколы

---

## 1. Введение: координация в распределённых системах

В распределённых системах узлы должны координировать действия, но могут:

- Падать в любой момент
- Терять сообщения
- Работать с разной скоростью

**Протоколы распределённых систем** решают проблемы координации в условиях отказов и асинхронности.

---

## 2. Consensus (Консенсус)

### 2.1 Проблема

**Проблема:** N узлов должны согласовать значение, несмотря на отказы.

**Требования:**

- **Agreement**: все узлы согласовывают одно значение

- **Validity**: согласованное значение предложено одним из узлов

- **Termination**: процесс завершается

### 2.2 Raft Consensus

**Роли узлов:**

- **Leader**: принимает запросы, реплицирует log

- **Follower**: пассивно реплицирует log

- **Candidate**: претендует на роль leader

**Процесс:**
```
1. Client отправляет запрос Leader
2. Leader добавляет в log и реплицирует Followers
3. Когда большинство (majority) подтвердили:
   - Leader применяет (commits) изменение
   - Leader сообщает Followers
4. Все узлы применили изменение → consensus
```

### 2.3 Log replication

```
Leader log:    [1] [2] [3] [4]
               commit ↑

Follower 1:    [1] [2] [3] [4]
Follower 2:    [1] [2] [3]
Follower 3:    [1] [2]

Leader: отправляет [4] Followers 2 и 3
После получения подтверждений от majority: commit
```

### 2.4 Quorum

**Quorum** — минимальное количество узлов для принятия решения.

**Для N узлов:**

- Quorum = N/2 + 1
- 3 узла: quorum = 2
- 5 узлов: quorum = 3

**Зачем:** Обеспечивает, что два quorums всегда пересекаются (гарантируя видимость изменений).

---

## 3. Leader Election

### 3.1 Проблема

**Проблема:** Множество узлов должны выбрать одного leader для координации.

**Требования:**

- Только один leader в момент времени
- При отказе leader — новые выборы
- Процесс должен завершиться

### 3.2 Raft Leader Election

**Процесс:**
```
1. Узел не получает heartbeat от leader → становится Candidate
2. Candidate инкрементирует term, голосует за себя
3. Candidate запрашивает голоса у других узлов
4. Если получает majority голосов → становится Leader
5. Leader отправляет heartbeats для поддержания статуса
```

**Term (срок):**

- Монотонно растущее число
- Новый term начинается при выборах
- Узлы отклоняют сообщения со старым term

### 3.3 Split vote

**Проблема:** Несколько candidates получают одинаковое количество голосов.

**Решение:**
```
1. Нет победителя → timeout
2. Новый term, новые выборы
3. Random timeout для избежания повторных split votes
```

### 3.4 Zookeeper Leader Election

```python
from kazoo.client import KazooClient

zk = KazooClient('localhost:2181')
zk.start()

# Создаём ephemeral sequential node

election_path = "/election"
zk.ensure_path(election_path)

node = zk.create(
    f"{election_path}/candidate-",
    ephemeral=True,
    sequence=True
)

# Узел с наименьшим sequence number — leader

children = sorted(zk.get_children(election_path))
if node.endswith(children[0]):
    print("I am the leader!")
else:
    print("I am a follower")
```

---

## 4. Heartbeats

### 4.1 Концепция

**Heartbeat** — периодическое сообщение "я жив".

**Назначение:**

- Обнаружение отказов
- Поддержание статуса leader
- Проверка доступности узлов

### 4.2 Протокол heartbeat

```
Leader → Followers: Heartbeat (каждые 100ms)
Followers: получают heartbeat, сбрасывают election timeout

Если Follower не получил heartbeat за timeout (300ms):
    → начать выборы
```

### 4.3 Пример реализации

```python
import time
import threading

class HeartbeatMonitor:
    def __init__(self, timeout=1.0):
        self.timeout = timeout
        self.last_heartbeat = time.time()
        self.is_alive = True
    
    def send_heartbeat(self):
        """Call periodically from leader"""
        self.last_heartbeat = time.time()
    
    def check_heartbeat(self):
        """Check if heartbeat timed out"""
        if time.time() - self.last_heartbeat > self.timeout:
            self.is_alive = False
            return False
        return True

# Leader thread

def leader_heartbeat():
    monitor = HeartbeatMonitor()
    while True:
        monitor.send_heartbeat()
        time.sleep(0.5)  # Send every 500ms

# Follower thread

def follower_check():
    monitor = HeartbeatMonitor(timeout=2.0)
    while True:
        if not monitor.check_heartbeat():
            print("Leader failed, starting election")
            break
        time.sleep(0.5)
```

### 4.4 Adaptive heartbeats

**Проблема:** Фиксированный timeout может быть слишком коротким (false positives) или длинным (медленное обнаружение).

**Решение:** Адаптивный timeout на основе network latency.

```python
class AdaptiveHeartbeat:
    def __init__(self):
        self.avg_latency = 0.1
        self.timeout_multiplier = 3
    
    def update_latency(self, latency):
        # Exponential moving average
        self.avg_latency = 0.9 * self.avg_latency + 0.1 * latency
    
    def get_timeout(self):
        return self.avg_latency * self.timeout_multiplier
```

---

## 5. Failure Detection

### 5.1 Типы отказов

**Crash failure:**

- Узел останавливается и не отвечает
- Детектируется через отсутствие heartbeat

**Byzantine failure:**

- Узел ведёт себя произвольно (злонамеренно или из-за багов)
- Сложнее детектировать

**Network partition:**

- Сеть разделяется на части
- Узлы в разных частях не могут общаться

### 5.2 Failure Detector свойства

**Completeness:**

- Все упавшие узлы будут обнаружены

**Accuracy:**

- Не будет false positives (живые узлы не считаются упавшими)

**Компромисс:** Perfect failure detector невозможен в асинхронных системах (FLP impossibility).

**Практика:** Eventually perfect failure detector (может ошибаться, но в итоге исправится).

### 5.3 Gossip-based failure detection

```
Узел A → Узел B: "Я живой, C живой, D не отвечает"
Узел B → Узел C: "Я живой, A живой, D не отвечает"
Узел C → Узел A: "Я живой, B живой, D не отвечает"

Если все узлы сообщают, что D не отвечает → D упал
```

**SWIM (Scalable Weakly-consistent Infection-style Membership):**
```
1. Узел A пингует случайный узел B
2. Если B не отвечает:
   - A просит K других узлов пропинговать B
3. Если все K не получили ответ → B упал
```

### 5.4 Split-brain problem

**Проблема:** Network partition → обе части считают другую упавшей → два leaders!

**Решение:** Quorum

```
Partition 1: 2 узла (minority) → не может стать leader
Partition 2: 3 узла (majority) → выбирает leader

Только majority может принимать решения
```

---

## 6. Distributed Transactions

### 6.1 Two-Phase Commit (2PC)

**Фаза 1 (Prepare):**
```
Coordinator → Participants: "Готовы к commit?"
Participants → Coordinator: "Да" или "Нет"
```

**Фаза 2 (Commit):**
```
Если все "Да":
    Coordinator → Participants: "Commit"
Иначе:
    Coordinator → Participants: "Abort"
```

**Проблема:** Coordinator — single point of failure.

### 6.2 Three-Phase Commit (3PC)

Добавляет фазу "Pre-commit" для снижения риска блокировки.

**Фазы:**

1. **Can-Commit**: готовы к commit?
2. **Pre-Commit**: все готовы, подготовка к commit
3. **Do-Commit**: окончательный commit

Более устойчив к отказам coordinator.

---

## 7. CAP Theorem

### 7.1 Теорема

**CAP:** Невозможно одновременно гарантировать все три:
- **Consistency**: все узлы видят одинаковые данные

- **Availability**: каждый запрос получает ответ

- **Partition tolerance**: система работает при network partition

**Можно выбрать только 2 из 3.**

### 7.2 Выбор компромисса

**CP (Consistency + Partition tolerance):**

- Жертвуем availability
- При partition: minority недоступны
- Примеры: HBase, MongoDB (strong consistency mode)

**AP (Availability + Partition tolerance):**

- Жертвуем consistency
- При partition: обе части доступны, но несогласованы
- Примеры: Cassandra, DynamoDB

**CA (Consistency + Availability):**

- Невозможно при partitions
- Только в single-datacenter без partitions

### 7.3 Eventual Consistency

**Компромисс для AP систем:**

- Temporary inconsistency допустима
- В итоге (eventually) все узлы согласуются
- Требует conflict resolution

---

## 💡 Key Takeaways

- **Consensus для согласованности**: Raft и Paxos позволяют узлам согласовать значение, несмотря на отказы. Quorum (N/2+1) гарантирует consistency.

- **Leader election для координации**: Один leader координирует систему. При отказе — новые выборы. Term и majority голосов предотвращают split-brain.

- **Heartbeats для мониторинга**: Периодические сообщения обнаруживают отказы. Adaptive timeouts снижают false positives при изменении latency.

- **Failure detection несовершенен**: Perfect failure detector невозможен в асинхронных системах. Eventually perfect (может ошибаться, но исправляется) — практический компромисс.

- **CAP theorem определяет компромиссы**: Невозможно одновременно иметь consistency, availability и partition tolerance. Выбор зависит от требований системы.

---

## 🚀 Next Steps

**Related Modules:**

- [17_Protocol_Classification](../17_Protocol_Classification/) — классификация протоколов: stateful/stateless, sync/async
- [19_Protocol_Design](../19_Protocol_Design/) — как проектировать протоколы: принципы и best practices

**Practice Ideas:**

1. Реализуйте простой Raft consensus (без snapshots и log compaction)
2. Создайте leader election с использованием Zookeeper или etcd
3. Реализуйте failure detector с adaptive heartbeats

**Going Deeper:**

- Изучите Paxos для понимания классического consensus
- Изучите Byzantine fault tolerance (PBFT) для защиты от злонамеренных узлов
- Изучите vector clocks и version vectors для eventual consistency

---



