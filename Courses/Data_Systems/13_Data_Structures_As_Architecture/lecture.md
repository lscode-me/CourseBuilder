# Data Structures As Architecture (Redis)
## Event Loops, Skip Lists, Persistence (RDB/AOF) и Caching

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **RAM vs Disk**: Понимать пропасть в скорости (Nanoseconds vs Milliseconds).

- **Time Complexity**: Знать $O(1)$, $O(\log N)$.

- **Networking**: Понимать сокеты.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Architecture**: Объяснять, почему Redis однопоточный и почему это *хорошо*.

- **Internals**: Понимать, как ZipList и IntSet экономят до 90% памяти.

- **Persistence**: Выбирать между RDB (Snapshot) и AOF (Log). Понимать механизм `fork()` и Copy-on-Write.

- **Algorithms**: Реализовать SkipList (структуру за Sorted Sets) или Event Loop на Python.

- **Clustering**: Шардировать Redis Cluster через Hash Slots (CRC16).

---

## 1. Redis: "Структуры данных как сервис"

Большинство баз данных прячут структуры (B-Trees) за слоем SQL.
Redis (Remote Dictionary Server) выставляет их наружу.
Это не "Кэш" (хотя часто так используется). Это **In-Memory Data Structure Store**.

---

## 2. Архитектура: Single Threaded Event Loop

Почему Redis обрабатывает 100,000 запросов в секунду на одном ядре?

1.  **RAM Operations**: Доступ к памяти занимает 100 наносекунд. Меньше, чем переключение контекста потока.
2.  **No Locks**: Раз поток один, не нужны мьютексы, семафоры и spinlocks. Нет Race Conditions внутри движка.
3.  **IO Multiplexing (epoll/kqueue)**: Redis не блокируется на чтении сокета.

### 2.1 Python Event Loop Simulation

Вот как работает Redis (упрощенно).

```python
import select
import socket
import queue

# Create a non-blocking server socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 6379))
server.listen(5)

inputs = [server] # Sockets to read from
outputs = [] # Sockets to write to
message_queues = {} # Buffer for outgoing data

print("Mini-Redis running on 6379...")
while inputs:
    # Magic syscall: wait until ANY socket is ready
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    for s in readable:
        if s is server: # New connection
            conn, addr = s.accept()
            conn.setblocking(False)
            inputs.append(conn)
            message_queues[conn] = queue.Queue()
            print(f"Client connected: {addr}")
        else: # Existing connection sends data
            data = s.recv(1024)
            if data:
                # Command Processing (Fast!)
                cmd = data.decode().strip()
                response = f"Simulated Result for {cmd}\n"
                
                message_queues[s].put(response.encode())
                if s not in outputs: outputs.append(s)
            else: # Disconnect
                if s in outputs: outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
                
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)
```

В реальности вместо `select` используется `epoll` (Linux) или `kqueue` (BSD/Mac), которые масштабируются до тысяч соединений $O(1)$.

---

## 3. Внутренности памяти (Internals)

Redis — маньяк оптимизации памяти.

### 3.1 ZipList (Compressed List)

Если вы создаете маленький List или Hash, Redis не создает Linked List с указателями (по 8 байт на указатель).
Он создает **ZipList**: плотный массив байт.
`[len][item1][len][item2]...`
Поиск в нем $O(N)$, но так как $N$ мал (до 512 элементов), это быстрее, чем прыгать по указателям в RAM (Cache Locality).

### 3.2 SkipList (Sorted Sets implementation)

Для `ZSET` (Sorted Set) Redis использует не красно-черное дерево, а **SkipList**.
Это вероятностная структура данных.

*   Уровень 0: Обычный связный список (все элементы).
*   Уровень 1: Половина элементов (ссылки через один).
*   Уровень 2: Четверть элементов.
Поиск работает как в метро: едем экспрессом, потом пересаживаемся на локальную. Сложность $O(\log N)$.

**Реализация SkipList:**

```python
import random

class SkipListNode:
    """Узел SkipList."""
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)  # Ссылки на следующий узел на каждом уровне

class SkipList:
    """Реализация SkipList для Sorted Set."""
    
    def __init__(self, max_level=16, probability=0.5):
        self.max_level = max_level
        self.probability = probability
        self.level = 0  # Текущий максимальный уровень
        self.header = SkipListNode(None, None, max_level)
    
    def random_level(self):
        """Генерация случайного уровня для нового узла."""
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level
    
    def insert(self, key, value):
        """Вставка элемента."""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Ищем место для вставки
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # Если ключ уже существует, обновляем значение
        if current and current.key == key:
            current.value = value
        else:
            # Создаем новый узел
            new_level = self.random_level()
            
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            
            new_node = SkipListNode(key, value, new_level)
            
            # Вставляем узел
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
    
    def search(self, key):
        """Поиск элемента."""
        current = self.header
        
        # Спускаемся с верхнего уровня
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        
        current = current.forward[0]
        
        if current and current.key == key:
            return current.value
        return None
    
    def delete(self, key):
        """Удаление элемента."""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Ищем узел для удаления
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        if current and current.key == key:
            # Удаляем узел
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            
            # Уменьшаем уровень, если нужно
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            
            return True
        return False

# Пример использования (как в Redis ZADD/ZRANGE)

skiplist = SkipList()
skiplist.insert("user:100", 1500)  # score = 1500
skiplist.insert("user:200", 2000)
skiplist.insert("user:300", 1200)

print(skiplist.search("user:200"))  # 2000
```

---

## 4. Persistence: RDB vs AOF

Как Redis не теряет данные при рестарте?

### 4.1 RDB (Redis Database Snapshot)

Снапшот всей памяти на диск раз в 5 минут.

**Механизм**: `fork()`.
Redis (Parent) делает системный вызов `fork()`. ОС создает Child Process.
Благодаря **Copy-on-Write (CoW)** в Linux, память физически не копируется!
Child видит "замороженную" память на момент форка и спокойно пишет её на диск.
Parent продолжает писать. Если Parent меняет страницу памяти, ОС копирует эту страницу (Copy-on-Write).

*   **Плюс**: Компактно, быстро стартует.

*   **Минус**: Потеря данных за последние 5 минут при крэше.

### 4.2 AOF (Append Only File)

Пишет каждую команду (`SET a 1`) в лог файла.

*   **fsync strategies**:
    *   `always`: Медленно (safest).
    *   `everysec`: Стандарт (теряем макс 1 сек).
    *   `no`: Отдаем на откуп ОС.
*   **Rewriting**: Файл растет бесконечно. Redis переписывает его в фоне (на основе текущей памяти), чтобы удалить лишние `SET a 1`, `SET a 2`.

**Симуляция AOF:**

```python
class AOFWriter:
    """Упрощенная реализация AOF."""
    
    def __init__(self, file_path, fsync_strategy='everysec'):
        self.file_path = file_path
        self.fsync_strategy = fsync_strategy
        self.buffer = []
        self.last_fsync = time.time()
        self.file = open(file_path, 'a')
    
    def append_command(self, command, *args):
        """Добавление команды в AOF."""
        # Формат: *<argc>\r\n$<len>\r\n<arg>\r\n...
        line = f"{command} {' '.join(str(a) for a in args)}\n"
        self.buffer.append(line)
        
        if self.fsync_strategy == 'always':
            self.flush()
        elif self.fsync_strategy == 'everysec':
            if time.time() - self.last_fsync >= 1.0:
                self.flush()
    
    def flush(self):
        """Запись буфера на диск."""
        if not self.buffer:
            return
        
        data = ''.join(self.buffer)
        self.file.write(data)
        self.file.flush()
        os.fsync(self.file.fileno())  # Принудительная запись на диск
        
        self.buffer = []
        self.last_fsync = time.time()
    
    def close(self):
        """Закрытие файла."""
        self.flush()
        self.file.close()

# Пример использования

aof = AOFWriter('appendonly.aof', fsync_strategy='everysec')
aof.append_command('SET', 'key1', 'value1')
aof.append_command('SET', 'key2', 'value2')
aof.append_command('DEL', 'key1')
time.sleep(1.1)  # Триггерит fsync
aof.close()
```

**AOF Rewriting (компактификация):**

```python
class AOFRewriter:
    """Переписывание AOF для удаления избыточных команд."""
    
    def __init__(self, aof_path, current_state):
        self.aof_path = aof_path
        self.current_state = current_state  # Текущее состояние в памяти
    
    def rewrite(self):
        """Переписывание AOF на основе текущего состояния."""
        temp_path = self.aof_path + '.tmp'
        
        with open(temp_path, 'w') as f:
            # Записываем только финальные значения
            for key, value in self.current_state.items():
                if isinstance(value, str):
                    f.write(f"SET {key} {value}\n")
                elif isinstance(value, (int, float)):
                    f.write(f"SET {key} {value}\n")
                # ... другие типы
        
        # Атомарная замена
        os.rename(temp_path, self.aof_path)

# Пример: старый AOF
# SET x 1
# SET x 2
# SET x 3
# SET y 10

# После rewriting (текущее состояние: x=3, y=10)
# SET x 3
# SET y 10
```

---

## 5. Scaling: Redis Cluster

Один Redis не резиновый (макс RAM сервера).

### 5.1 Hash Slots

Redis Cluster не использует Consistent Hashing (кольцо).
Он делит пространство ключей на **16384 Hash Slots**.
`Slot = CRC16(key) % 16384`.

*   Node A: Slots 0-5500.
*   Node B: Slots 5501-11000.
*   Node C: Slots 11001-16383.

Если Smart Client знает карту слотов, он идет сразу к нужному узлу. Если нет — узел отвечает `MOVED 127.0.0.1:6380`.

**Реализация Hash Slot:**

```python
import binascii

def crc16(key):
    """Вычисление CRC16 для ключа (упрощенная версия)."""
    return binascii.crc_hqx(key.encode('utf-8'), 0) & 0xffff

def get_slot(key):
    """Вычисление слота для ключа."""
    # Redis использует только часть ключа для hash tag
    # {user:1000}:profile -> использует только "user:1000"
    if '{' in key and '}' in key:
        start = key.index('{') + 1
        end = key.index('}')
        key = key[start:end]
    
    return crc16(key) % 16384

# Примеры

print(get_slot("user:1000"))  # 1234
print(get_slot("{user:1000}:profile"))  # 1234 (тот же слот!)
print(get_slot("{user:1000}:settings"))  # 1234 (тот же слот!)

# Это позволяет группировать связанные ключи на одном узле
```

**Redis Cluster Client:**

```python
class RedisClusterClient:
    """Упрощенный клиент для Redis Cluster."""
    
    def __init__(self, nodes):
        self.nodes = nodes  # [(host, port, slots), ...]
        self.slot_map = {}  # slot -> node
        self.build_slot_map()
    
    def build_slot_map(self):
        """Построение карты слотов."""
        for node in self.nodes:
            host, port, slots = node
            for slot in slots:
                self.slot_map[slot] = (host, port)
    
    def get_node_for_key(self, key):
        """Получение узла для ключа."""
        slot = get_slot(key)
        return self.slot_map.get(slot)
    
    def set(self, key, value):
        """Установка значения."""
        node = self.get_node_for_key(key)
        if not node:
            raise Exception(f"No node for key {key}")
        
        # Отправка команды на нужный узел
        print(f"Sending SET {key} to {node}")
        return True
    
    def get(self, key):
        """Получение значения."""
        node = self.get_node_for_key(key)
        if not node:
            raise Exception(f"No node for key {key}")
        
        print(f"Sending GET {key} to {node}")
        return "value"  # Симуляция

# Пример использования

nodes = [
    ("node1", 6379, range(0, 5461)),
    ("node2", 6379, range(5461, 10922)),
    ("node3", 6379, range(10922, 16384)),
]

client = RedisClusterClient(nodes)
client.set("user:1000", "Alice")
client.set("{user:1000}:profile", "data")  # Попадет на тот же узел!
```

### 5.2 Resharding (Перераспределение слотов)

```python
class ClusterResharding:
    """Перераспределение слотов между узлами."""
    
    def __init__(self, nodes):
        self.nodes = nodes
    
    def migrate_slot(self, slot, from_node, to_node):
        """Миграция слота с одного узла на другой."""
        print(f"Migrating slot {slot} from {from_node} to {to_node}")
        
        # 1. Устанавливаем слот в MIGRATING состояние на from_node
        # 2. Устанавливаем слот в IMPORTING состояние на to_node
        # 3. Копируем ключи слота
        # 4. Обновляем карту слотов
        # 5. Перенаправляем запросы на новый узел
        
        return True
    
    def rebalance(self, target_distribution):
        """Перебалансировка кластера."""
        current = self.get_current_distribution()
        
        for node, target_slots in target_distribution.items():
            current_slots = current[node]
            if len(current_slots) < len(target_slots):
                # Нужно добавить слоты
                needed = len(target_slots) - len(current_slots)
                # Находим узлы с избытком слотов
                # Мигрируем слоты
                pass
```

---

## 6. Glossary

*   **Eviction Policy (LRU/LFU)**: Правило удаления ключей, когда память полна.
    *   `allkeys-lru`: Удаляет давно неиспользуемые (даже полезные).
    *   `volatile-lru`: Удаляет только те, у которых есть TTL (Expire).
*   **TTL (Time To Live)**: Время жизни ключа. Удаляется "лениво" (при доступе) или "активно" (фоновым сканированием).

*   **Pub/Sub**: Механизм сообщений. Не сохраняет историю (Fire and Forget).

*   **Lua Scripting**: Возможность атомарно выполнить скрипт на сервере (`EVAL`). Заменяет транзакции.

*   **Pipeline**: Отправка пачки команд без ожидания ответа. Ускоряет работу в разы (меньше RTT).

*   **Sentinel**: Сервис мониторинга для Master-Slave failover (не для Cluster).

*   **Off-heap memory**: Память вне кучи процесс (в Java/C#). Redis написан на C, у него вся память "Off-heap" (malloc).

---

## 📚 Appendix A: Troubleshooting Guide

### A.1 Symptom: OOM (Out Of Memory) Crash

**Симптом**: Linux OOM Killer убивает Redis.
**Причина**:
1.  **NO EVICTION**: `maxmemory-policy noeviction`. Redis уперся в лимит и падает.
2.  **Fragmentation**: `used_memory_rss` >> `used_memory`. ОС выделила страницы, но аллокатор (jemalloc) не вернул их (фрагментация).
**Лечение**:
*   Включить LRU.
*   Перезапустить Redis (дефрагментация).
*   Включить `activedefrag yes` (в новых версиях).

### A.2 Symptom: High Latency Spikes

**Симптом**: 99% запросов быстрые, 1% висит 500мс.
**Причина**:
1.  **Slow Log**: Кто-то запустил `KEYS *` (O(N) операция) или удаляет огромный Set на миллион элементов.
2.  **Fork overhead**: При сохранении RDB на огромной памяти (64GB) вызов `fork()` может заблокировать CPU на 200мс (копирование Page Tables).
**Лечение**:
*   Никогда не использовать `KEYS *`, использовать `SCAN`.
*   Использовать `Unlink` (Async delete) вместо `Del` для больших объектов.

---

## 📚 Appendix B: Historical Context

### Salvatore Sanfilippo (antirez)

Итальянский разработчик. В 2009 году писал стартап (аналитика в реальном времени). MySQL "не тянул" обновления счетчиков.
Он написал прототип "in-memory БД" на Tcl (потом переписал на C).
Redis расшифровывается как **RE**mote **DI**ctionary **S**erver.
Антирез известен своей принципиальностью в качестве кода и отказом от фич, усложняющих ядро (например, долго не хотел добавлять многопоточность).

### Memcached comparison

До Redis королем был Memcached (LiveJournal).

*   **Memcached**: Multi-threaded (масштабируется вверх), но только String ключи-значения. "Тупой кэш".

*   **Redis**: Single-threaded, но богатые структуры данных. "Умное хранилище".
Сегодня Redis почти полностью вытеснил Memcached.

---

## 📚 Appendix C: FAQ

**Q1: Redis — это база или кэш?**
**A**: И то и другое. Если вы включили AOF/RDB — это надежная (почти) БД. Но часто используют как кэш поверх медленного Postgres.

**Q2: Почему Redis не использует Multi-threading для команд?**
**A**: Потому что узкое место обычно сеть, а не CPU. Сложность кода с локами (Race Conditions, Deadlocks) замедлит разработку. (В версии 6.0 добавили IO threads — парсинг сети в потоках, но исполнение команд всё еще в одном).

**Q3: Сколько ключей влезает в Redis?**
**A**: Миллиарды. Зависит от RAM. Один пустой ключ ~50 байт оверхеда.

**Q4: Можно ли потерять данные в Redis Cluster?**
**A**: Да. Репликация асинхронна. Если Мастер одобрил запись и умер до репликации на Слейв — данные потеряны. Redis не ACID база (в строгом смысле Durability).

**Q5: Что лучше: JSON in String или Hash?**
**A**:
*   JSON blob в String (`SET user:1 "{...}"`): Проще для приложения. Но чтобы сменить одно поле, нужно читать/писать весь JSON.
*   Hash (`HSET user:1 field val`): Экономит трафик, можно менять поля атомарно. И работает ZipList компрессия. Hash лучше.

---

## 💡 Key Takeaways

1.  **Single Threaded is Fast**: Простота архитектуры дает скорость.
2.  **Know your Data Structures**: Использование Sorted Set вместо выборки из SQL может ускорить лидерборд в 1000 раз.
3.  **Persistence isn't free**: `fork()` стоит дорого. Рассчитывайте память (нужно 50% запаса под CoW буферы).
4.  **Memory optimization matters**: ZipList и IntSet экономят до 90% памяти для маленьких коллекций.
5.  **Hash Slots > Consistent Hashing**: Redis Cluster использует фиксированные слоты для предсказуемости и упрощения миграции.

---

## 🚀 Next Steps

**Практика:**

1.  `redis-cli`.
2.  Создайте список: `LPUSH mylist A`, `LPUSH mylist B`.
3.  Посмотрите внутреннюю кодировку: `OBJECT ENCODING mylist`. (Должно быть `quicklist` или `ziplist`).
4.  Создайте Set: `SADD myset 1`.
5.  Посмотрите encoding. Если числа малые — `intset`. добавьте строку `SADD myset "hello"`. Encoding станет `hashtable`.

В следующем модуле мы обсудим, как выбирать между SQL, NoSQL и NewSQL. [Choosing Data Systems](../14_Choosing_DS_For_System_Design/).



