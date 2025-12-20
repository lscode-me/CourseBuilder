# Репликация и согласованность
## Single Leader, Multi-Leader, Leaderless и кворумы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать CAP теорему (Consistency vs Availability)
- Знать, что такое сетевая задержка
- Понимать принцип работы логов (WAL)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать стратегии репликации (Single Leader, Multi-Leader, Leaderless)
- Понимать разницу между синхронной и асинхронной репликацией
- Объяснять механику кворумов (R + W > N)
- Реализовывать простую логику разрешения конфликтов (LWW)

---

## 1. Зачем нужна репликация?

**Репликация** — это хранение копий одних и тех же данных на нескольких узлах.

Цели репликации:

1.  **High Availability (Высокая доступность)**: Если один сервер упал, система продолжает работать.
2.  **Latency (Задержка)**: Данные ближе к пользователю (CDN, гео-распределение).
3.  **Scalability (Масштабируемость)**: Распределение нагрузки на чтение между репликами.

---

## 2. Leader-Based Replication (Active/Passive)

Самая популярная схема (MySQL, Postgres, Kafka, Mongo).

### 2.1 Архитектура

1.  Один узел назначается **Leader** (Master / Primary).
2.  Остальные узлы — **Followers** (Slaves / Secondaries / Replicas).
3.  Клиент пишет ТОЛЬКО в Leader.
4.  Leader пишет в свой лог и отправляет поток изменений (Replication Stream) всем Followers.
5.  Клиенты могут читать с Leader или Followers.

```

Client -> [Write] -> Leader
                       | \
                       |  \ (Replication Stream)
                       v   v
                   Follower1  Follower2
```

### 2.2 Sync vs Async

**Synchronous Replication**:
Leader ждет подтверждения от Follower, прежде чем сказать клиенту "ОК".

*   ➕ Strong Consistency (данные точно не пропадут).
*   ➖ Задержка (пишем со скоростью самого медленного диска + RTT).
*   ➖ Если Follower упал, запись встала.

**Asynchronous Replication** (Default in most DBs):
Leader говорит "ОК" сразу, данные летят на Follower в фоне.

*   ➕ Быстро.
*   ➕ Leader не зависит от Followers.
*   ➖ **Replication Lag**: Follower может отставать на секунды или минуты.
*   ➖ **Data Loss**: Если Leader умер до репликации, данные потеряны.

**Semi-Synchronous**:
Ждем подтверждения только от ОДНОГО Follower (золотая середина).

---

## 3. Проблемы репликации (Replication Lag)

В асинхронной системе клиент может столкнуться с аномалиями.

### 3.1 Reading Your Own Writes

Пользователь обновил профиль, перезагрузил страницу (запрос попал на отстающий Follower) — видит старый профиль.

*   *Решение*: Читать "свои" данные всегда с лидера.

### 3.2 Monotonic Reads

Пользователь сделал запрос 1 (попал на быстрый Follower) — увидел пост.
Сделал запрос 2 (попал на медленный Follower) — пост исчез. "Путешествие во времени".

*   *Решение*: Sticky Sessions (пользователь всегда читает с одной реплики).

---

## 4. Multi-Leader Replication (Active/Active)

Если у нас дата-центры в США и Европе, писать только в один Leader (в США) — это огромная задержка для европейцев.
Решение: По лидеру в каждом дата-центре.

```

DC 1 (USA): [Leader 1] <-> [Client US]
               ^  |
               |  | (Async sync)
               v  v
DC 2 (EU):  [Leader 2] <-> [Client EU]
```

*   ➕ Локальная запись (быстро).
*   ➕ Переживает падение целого дата-центра.
*   ➖ **Конфликты записи**: Клиент А изменил `Title="X"` в США, Клиент Б изменил `Title="Y"` в Европе одновременно.

### 4.1 Разрешение конфликтов

1.  **Last Write Wins (LWW)**: Выигрывает запись с большим timestamp. (Потеря данных!).
2.  **On read resolution**: Сохраняем обе версии, отдаем клиенту, пусть сам мержит. (Как Git merge conflict).
3.  **CRDTs (Conflict-free Replicated Data Types)**: Специальные структуры данных, которые всегда можно слить (merge) автоматически.

---

## 5. Leaderless Replication (Dynamo-style)

Используется в Cassandra, DynamoDB, Riak.
Здесь **нет лидера**. Клиент пишет на любые узлы.

Помните "Кольцо" из прошлой лекции?
Клиент посылает запись всем $N$ репликам.

### 5.1 Quorums (Кворумы)

Чтобы гарантировать согласованность, мы используем голосование.
Пусть $N$ — фактор репликации (например, 3 копии).
$W$ — сколько узлов должны подтвердить запись.
$R$ — со скольких узлов мы читаем.

**Формула кворума**:
$$ R + W > N $$

Если это условие выполняется, то при чтении $R$ узлов мы **гарантированно** увидим хотя бы один узел с последней записью ($W$).

*Пример*: $N=3, W=2, R=2$. ($2+2 > 3$).
Мы пишем на 2 узла. Значит, только 1 узел может быть старым. Если читаем с 2-х, минимум один будет новым.

### 5.2 Read Repair & Anti-Entropy

В Leaderless системах данные часто разъезжаются. Механизмы починки:

1.  **Read Repair**: Когда клиент читает данные (с $R$ узлов), он видит версии. Если версии отличаются, он возвращает клиенту самую свежую, а в фоне обновляет старые узлы.
2.  **Anti-Entropy (Merkle Trees)**: Фоновый процесс сравнивает хеши данных на узлах и синхронизирует разницу.

---

## 6. Демонстрация: Quorum Consistency

Скрипт симулирует N=3, W=2, R=2.

```python

import time
import random

class Replica:
    def __init__(self, id):
        self.id = id
        self.data = {} # Key -> (Value, Timestamp)
        
    def write(self, key, value, timestamp):
        # Принимаем только если timestamp новее
        if key not in self.data or self.data[key][1] < timestamp:
            self.data[key] = (value, timestamp)
            return True
        return False
        
    def read(self, key):
        return self.data.get(key)

class Coordinator:
    def __init__(self):
        self.replicas = [Replica(1), Replica(2), Replica(3)]
        
    def write_quorum(self, key, value, w=2):
        ts = time.time()
        success_count = 0
        # Пытаемся записать на все, но ждем подтверждения от W
        for r in self.replicas:
            # Симуляция сбоя сети (иногда запись не доходит)
            if random.random() > 0.2: 
                if r.write(key, value, ts):
                    success_count += 1
            else:
                print(f"Write to Replica {r.id} failed (Network error)")
                
        if success_count >= w:
            print(f"Write '{value}' SUCCESS (W={success_count}/{w})")
            return True
        else:
            print(f"Write '{value}' FAILED (W={success_count}/{w})")
            return False

    def read_quorum(self, key, r=2):
        responses = []
        for rep in self.replicas:
            # Симуляция сбоя
            if random.random() > 0.2:
                val = rep.read(key)
                if val: responses.append(val)
            else:
                print(f"Read form Replica {rep.id} failed")
        
        if len(responses) < r:
            print("Read FAILED: Quorum not met")
            return None
            
        # Находим версию с максимальным timestamp
        # responses = [(val, ts), (val, ts)...]
        newest = max(responses, key=lambda x: x[1])
        print(f"Read result: {newest[0]} (Quorum {len(responses)}/{r})")
        
        # Read Repair (упрощенно): нужно бы обновить старые реплики
        return newest[0]

# Тест
coord = Coordinator()

# Пишем с W=2. Допустим, Replica 3 недоступна.
# Запись пройдет, так как 2 узла ответили.

coord.write_quorum("x", 100, w=2)

# Читаем с R=2. Допустим, Replica 1 недоступна.
# Мы прочитаем с 2 и 3. В 3 нет данных (она пропустила запись), но в 2 есть!
# Max timestamp выберет верное значение.
coord.read_quorum("x", r=2)
```

**Output Scenario**:
```

Write to Replica 3 failed (Network error)
Write '100' SUCCESS (W=2/2)
Read result: 100 (Quorum 3/2) 
```

---

## 7. Chain Replication (Цепочка)

Еще один подход, популярный в хранилищах (например, Ceph).
`Client -> Node A -> Node B -> Node C -> Client`

*   Запись идет по цепочке A -> B -> C.
*   Чтение только с хвоста (C).
*   **Strong Consistency**: Пока данные не дошли до хвоста, их никто не прочитает. Если дошли — они на всех узлах.

---

## 💡 Key Takeaways

- **Single Leader** — стандарт де-факто (Postgres/MySQL). Просто понять, но Leader = точка отказа и "бутылочное горлышко" записи.

- **Async Replication** — риск потери данных, но быстро. **Sync** — надежно, но медленно.

- **Multi-Leader** — нужен для Cross-Datacenter, но сложно разрешать конфликты.

- **Leaderless (Dynamo)** — максимальная доступность (High Availability), "Always Writable". Требует понимания Кворумов ($R+W>N$).

- **Replication Lag** — причина многих багов в веб-приложениях ("Я не вижу свой коммент").

---

## 🚀 Next Steps

**Related Modules:**

- [Distributed Logs & Queues](../12_Distributed_Logs_And_Queues/) — как Kafka использует репликацию логов.
- [Case Studies](../16_Case_Studies/) — разбор архитектуры DynamoDB и Spanner.

**Practice Ideas:**

1. Настройте PostgreSQL Streaming Replication (Docker). Убейте мастера, сделайте `promote` слейва.
2. Попробуйте Cassandra в Docker. Создайте таблицу с `replication_factor=3`. Уроните одну ноду, прочитайте данные.
3. Реализуйте LWW (Last Write Wins) мерж двух JSON-документов.

---

