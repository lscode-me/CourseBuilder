# Distributed Logs And Queues
## Kafka, Sequential IO, Zero-Copy и Stream Processing

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **OS Internals**: Понимать разницу между User Space и Kernel Space.

- **Disk IO**: Знать, что Random IO медленный, а Sequential IO быстрый.

- **Replication**: Понимать Leader/Follower модель (Модуль 11), так как Kafka использует её.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **The Log**: Понимать философию "Log-centric architecture". База данных — это просто кэш лога.

- **Architecture**: Проектировать топики и партиции в Kafka для масштабирования.

- **Performance**: Объяснять магию Zero-Copy (`sendfile`) и Sequential Writes, которая позволяет Kafka обрабатывать миллионы событий в секунду.

- **Semantics**: Различать At-Most-Once, At-Least-Once и Exactly-Once.

- **Stream Processing**: Использовать оконные функции (Tumbling/Hopping Windows) для анализа потоков в реальном времени.

---

## 1. Философия Лога (The Log)

В базах данных мы привыкли видеть таблицу: текущее состояние.
`User: {id: 1, balance: 100}`.
Но откуда взялись эти 100?

**Лог (Write-Ahead Log)** — это история того, что произошло.
1. `CreateUser(id=1, balance=0)`
2. `Deposit(id=1, amount=50)`
3. `Deposit(id=1, amount=50)`

**Текущее состояние = Сумма всех событий в логе**.
Если у вас есть Лог, вы можете восстановить состояние базы на любой момент времени.
Бэкап базы — это просто копия лога.
Репликация базы — это пересылка лога.

**Apache Kafka** вынесла эту идею наружу. Она сказала: "Пусть Лог будет центральным элементом архитектуры".

### 1.1 Event Sourcing: Лог как источник правды

```python

class EventStore:
    """Хранилище событий (Event Sourcing)."""
    
    def __init__(self):
        self.events = []  # Лог событий
    
    def append_event(self, event_type, aggregate_id, data):
        """Добавление события в лог."""
        event = {
            'timestamp': time.time(),
            'type': event_type,
            'aggregate_id': aggregate_id,
            'data': data
        }
        self.events.append(event)
        return event
    
    def get_events(self, aggregate_id):
        """Получение всех событий для агрегата."""
        return [e for e in self.events if e['aggregate_id'] == aggregate_id]
    
    def rebuild_state(self, aggregate_id):
        """Восстановление состояния из событий."""
        events = self.get_events(aggregate_id)
        state = {}
        
        for event in events:
            if event['type'] == 'UserCreated':
                state = {'id': event['data']['id'], 'balance': 0}
            elif event['type'] == 'Deposit':
                state['balance'] += event['data']['amount']
            elif event['type'] == 'Withdraw':
                state['balance'] -= event['data']['amount']
        
        return state

# Пример использования
store = EventStore()
store.append_event('UserCreated', 'user:1', {'id': 1})
store.append_event('Deposit', 'user:1', {'amount': 50})
store.append_event('Deposit', 'user:1', {'amount': 50})

# Восстанавливаем состояние

state = store.rebuild_state('user:1')
print(f"User balance: {state['balance']}")  # 100
```

### 1.2 Лог как очередь сообщений

```python

class SimpleLogQueue:
    """Простая очередь на основе лога."""
    
    def __init__(self):
        self.log = []
        self.consumer_offsets = {}  # consumer_id -> offset
    
    def produce(self, message):
        """Добавление сообщения в лог."""
        entry = {
            'offset': len(self.log),
            'message': message,
            'timestamp': time.time()
        }
        self.log.append(entry)
        return entry['offset']
    
    def consume(self, consumer_id, batch_size=10):
        """Чтение сообщений для консьюмера."""
        offset = self.consumer_offsets.get(consumer_id, 0)
        
        # Читаем с текущего offset
        messages = self.log[offset:offset+batch_size]
        
        # Обновляем offset
        if messages:
            self.consumer_offsets[consumer_id] = offset + len(messages)
        
        return messages
    
    def commit_offset(self, consumer_id, offset):
        """Коммит offset консьюмера."""
        self.consumer_offsets[consumer_id] = offset

# Пример
queue = SimpleLogQueue()
queue.produce("Message 1")
queue.produce("Message 2")
queue.produce("Message 3")

messages = queue.consume("consumer-1", batch_size=2)
print([m['message'] for m in messages])  # ['Message 1', 'Message 2']
```

---

## 2. Kafka Architecture

Kafka — это распределенный, партиционированный, реплицированный лог коммитов (Distributed Commit Log).

### 2.1 Topic & Partitions

*   **Topic**: Логическая очередь (напр. `orders`, `clicks`).

*   **Partition**: Топик бьется на шарды (Partitions). `Partition 0`, `Partition 1`...
    *   Партиция — это единица параллелизма.
    *   Партиция — это упорядоченная последовательность сообщений.
    *   Порядок гарантируется **только внутри партиции**. Между партициями порядка нет!

### 2.2 Offset

Каждое сообщение в партиции имеет ID: **Offset** (0, 1, 2...).
Offset монотонно растет и никогда не уменьшается.
Consumer (читатель) запоминает свой Offset: "Я прочитал до 100500".

### 2.3 Segment Files

На диске партиция — это папка с файлами `.log` (данные) и `.index` (индекс для поиска offset->position).
Kafka пишет только в конец последнего файла (Active Segment). Старые сегменты (`0000.log`, `1000.log`) доступны только для чтения.

**Структура сегментов:**

```python

class KafkaSegment:
    """Упрощенная реализация сегмента Kafka."""
    
    def __init__(self, base_offset, segment_size=1024*1024*100):  # 100MB
        self.base_offset = base_offset
        self.segment_size = segment_size
        self.entries = []
        self.index = {}  # offset -> position in entries
    
    def append(self, offset, message):
        """Добавление сообщения в сегмент."""
        if self.is_full():
            raise Exception("Segment is full")
        
        position = len(self.entries)
        entry = {
            'offset': offset,
            'message': message,
            'position': position
        }
        self.entries.append(entry)
        self.index[offset] = position
        return entry
    
    def is_full(self):
        """Проверка, заполнен ли сегмент."""
        return len(self.entries) * 100 > self.segment_size  # ~100 bytes per entry
    
    def get(self, offset):
        """Получение сообщения по offset."""
        if offset in self.index:
            return self.entries[self.index[offset]]
        return None
    
    def scan(self, start_offset, max_messages=100):
        """Сканирование сообщений с указанного offset."""
        results = []
        for entry in self.entries:
            if entry['offset'] >= start_offset:
                results.append(entry)
                if len(results) >= max_messages:
                    break
        return results

# Пример использования

segment = KafkaSegment(base_offset=0)
segment.append(0, "Message 0")
segment.append(1, "Message 1")
segment.append(2, "Message 2")

print(segment.get(1))  # {'offset': 1, 'message': 'Message 1', ...}
```

### 2.4 Consumer Groups

```python

class ConsumerGroup:
    """Управление группой консьюмеров."""
    
    def __init__(self, group_id, partitions):
        self.group_id = group_id
        self.partitions = partitions
        self.consumers = {}
        self.assignment = {}  # consumer_id -> [partitions]
    
    def add_consumer(self, consumer_id):
        """Добавление консьюмера в группу."""
        self.consumers[consumer_id] = {
            'id': consumer_id,
            'partitions': []
        }
        self.rebalance()
    
    def remove_consumer(self, consumer_id):
        """Удаление консьюмера."""
        if consumer_id in self.consumers:
            del self.consumers[consumer_id]
            self.rebalance()
    
    def rebalance(self):
        """Перебалансировка партиций между консьюмерами."""
        num_consumers = len(self.consumers)
        if num_consumers == 0:
            return
        
        # Распределяем партиции равномерно
        partitions_per_consumer = len(self.partitions) // num_consumers
        remainder = len(self.partitions) % num_consumers
        
        consumer_list = list(self.consumers.keys())
        partition_idx = 0
        
        for i, consumer_id in enumerate(consumer_list):
            # Некоторые консьюмеры получат на одну партицию больше
            count = partitions_per_consumer + (1 if i < remainder else 0)
            assigned = self.partitions[partition_idx:partition_idx+count]
            
            self.consumers[consumer_id]['partitions'] = assigned
            self.assignment[consumer_id] = assigned
            
            partition_idx += count
        
        print(f"Rebalanced: {self.assignment}")

# Пример

group = ConsumerGroup("my-group", [0, 1, 2, 3, 4, 5])
group.add_consumer("consumer-1")
group.add_consumer("consumer-2")
group.add_consumer("consumer-3")

# Результат: каждый консьюмер получит по 2 партиции

```

---

## 3. Почему Kafka такая быстрая?

Kafka написана на Java (GC, оверхед), но обрабатывает миллионы RPS. Как?
Ответ: **Отказ от лишней работы**.

### 3.1 Sequential I/O

Жесткие диски (HDD) ненавидят Random Seek (перемещение головки занимает 10мс).
Но Sequential Write на HDD быстрее, чем Random Write на SSD!
Kafka всегда пишет **Apppend-Only**. Ей не нужно прыгать по диску. Она просто льет биты в конец файла.

### 3.2 Zero-Copy (The syscall magic)

Обычная отправка файла в сеть (`read` + `write`):

1.  **Disk -> Kernel Buffer** (DMA copy).
2.  **Kernel Buffer -> User Buffer** (CPU copy). *Context switch!*
3.  Application code reading data...
4.  **User Buffer -> Socket Buffer** (CPU copy). *Context switch!*
5.  **Socket Buffer -> NIC** (DMA copy).

Итого: 4 копирования, 2 переключения контекста.

**Zero-Copy (`sendfile` in Linux)**:
1.  **Disk -> Page Cache** (Kernel).
2.  APP говорит ядру: "Скинь дескриптор файла в сокет".
3.  **Page Cache -> NIC Buffer** (DMA Scatter-Gather).

Данные **никогда не копируются** в память приложения (User Space).
CPU почти не нагружается. Kafka просто "соединяет трубу" между диском и сетью.

**C Code Example (Traditional vs Sendfile)**

```c

/* Traditional Read/Write (Slow) */
char buf[8192];
ssize_t n;
while ((n = read(disk_fd, buf, sizeof(buf))) > 0) {
    write(socket_fd, buf, n); // Context switch overhead + data copy
}

/* Zero-Copy with sendfile (Fast) */
#include <sys/sendfile.h>

struct stat stat_buf;
fstat(disk_fd, &stat_buf);
// Одна команда ядра делает всю работу.
// Данные летят Disk -> RAM (PageCache) -> NetCard.
sendfile(socket_fd, disk_fd, &offset, stat_buf.st_size);
```

**Python пример с mmap (Memory-Mapped Files):**

```python

import mmap
import os

class MappedLogReader:
    """Чтение лога через memory-mapped файлы (аналог Zero-Copy)."""
    
    def __init__(self, log_file_path):
        self.file_path = log_file_path
        self.file = open(log_file_path, 'rb')
        self.mmap = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)
    
    def read_at(self, offset, length):
        """Чтение данных по offset без копирования в Python."""
        self.mmap.seek(offset)
        return self.mmap.read(length)
    
    def close(self):
        self.mmap.close()
        self.file.close()

# Использование
reader = MappedLogReader('/var/kafka-logs/topic-0/00000000000000000000.log')
data = reader.read_at(offset=0, length=1024)  # Нет копирования в user space!
```

**Бенчмарк производительности:**

```python

import time

def benchmark_traditional_read(file_path, size):
    """Традиционное чтение с копированием."""
    start = time.time()
    with open(file_path, 'rb') as f:
        data = f.read(size)  # Копирование в Python buffer
    return time.time() - start

def benchmark_mmap_read(file_path, size):
    """Чтение через mmap (Zero-Copy)."""
    start = time.time()
    with open(file_path, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        data = mm[:size]  # Нет копирования!
        mm.close()
    return time.time() - start

# Результаты (примерные):
# Traditional: ~2ms для 1MB
# Mmap: ~0.1ms для 1MB (в 20 раз быстрее!)

```

### 3.3 Batching

Kafka не шлет сообщения по одному. Producer собирает пачку (Batch) и шлет её, если она наполнилась (16KB) или прошел таймаут (linger.ms=5ms). Сжатие (Gzip/Snappy/LZ4) работает эффективнее на батчах.

**Реализация батчинга:**

```python

class BatchedProducer:
    """Producer с батчингом сообщений."""
    
    def __init__(self, batch_size=16*1024, linger_ms=5):
        self.batch_size = batch_size
        self.linger_ms = linger_ms / 1000.0  # в секундах
        self.batch = []
        self.batch_bytes = 0
        self.last_send = time.time()
    
    def send(self, message):
        """Добавление сообщения в батч."""
        message_bytes = len(message.encode('utf-8'))
        
        # Проверяем, нужно ли отправить батч
        should_send = (
            self.batch_bytes + message_bytes >= self.batch_size or
            (time.time() - self.last_send) >= self.linger_ms
        )
        
        if should_send and self.batch:
            self.flush()
        
        # Добавляем в батч
        self.batch.append(message)
        self.batch_bytes += message_bytes
    
    def flush(self):
        """Отправка батча."""
        if not self.batch:
            return
        
        # Сжатие батча
        compressed = self.compress(self.batch)
        
        # Отправка (симуляция)
        print(f"Sending batch: {len(self.batch)} messages, {len(compressed)} bytes")
        
        self.batch = []
        self.batch_bytes = 0
        self.last_send = time.time()
    
    def compress(self, messages):
        """Сжатие батча (упрощенная версия)."""
        import gzip
        data = '\n'.join(messages).encode('utf-8')
        return gzip.compress(data)

# Пример использования

producer = BatchedProducer(batch_size=1000, linger_ms=10)

for i in range(100):
    producer.send(f"Message {i}")
    time.sleep(0.001)  # 1ms между сообщениями

producer.flush()  # Отправляем остатки
```

### 3.4 Compression Comparison

```python

import gzip
import lz4.frame
import zlib

def compare_compression(data):
    """Сравнение алгоритмов сжатия."""
    data_bytes = data.encode('utf-8')
    
    results = {
        'original': len(data_bytes),
        'gzip': len(gzip.compress(data_bytes)),
        'lz4': len(lz4.frame.compress(data_bytes)),
        'snappy': len(zlib.compress(data_bytes, level=1))  # Приближение к Snappy
    }
    
    for algo, size in results.items():
        if algo != 'original':
            ratio = (1 - size / results['original']) * 100
            print(f"{algo:10s}: {size:6d} bytes ({ratio:5.1f}% compression)")
    
    return results

# Тест на типичных данных Kafka (JSON события)
test_data = '\n'.join([
    '{"user_id": 123, "action": "click", "timestamp": 1234567890}'
    for _ in range(1000)
])

compare_compression(test_data)
# Результаты (примерные):
# gzip     : 15000 bytes (85% compression)
# lz4      : 18000 bytes (82% compression) - быстрее
# snappy   : 20000 bytes (80% compression) - самый быстрый

```

---

## 4. Delivery Semantics (Семантика доставки)

Гарантии — самая сложная часть.

### 4.1 At-Most-Once (Максимум один раз)

*   **Логика**: Producer шлет "Fire and Forget". Consumer читает, сначала коммитит оффсет, потом обрабатывает.

*   **Сбой**: Если Consumer упал во время обработки (но уже закоммитил), сообщение потеряно.

*   **Где**: IOT сенсоры, логи метрик (потеря одной точки не страшно).

### 4.2 At-Least-Once (Минимум один раз) — Стандарт

*   **Логика**: Producer ждет ACK. Consumer обрабатывает, потом коммитит.

*   **Сбой**: Если Consumer обработал, но упал *перед* коммитом оффсета, новый Consumer прочитает сообщение снова.

*   **Результат**: Дубликаты. Ваше приложение должно быть **Идемпотентным**.

### 4.3 Exactly-Once (Ровно один раз)

Святой Грааль.

*   **Kafka Transactions**: `beginTransaction` / `commitTransaction`. Позволяет атомарно писать в Kafka (в несколько топиков) и коммитить оффсеты.

*   **Idempotent Producer**: Каждое сообщение имеет Sequence Number. Брокер дедуплицирует повторы при сетевых ретраях.

*   **Ограничение**: Это работает только "Kafka -> Kafka" (Kafka Streams). Если вы пишете в БД, вам нужно делать дедупликацию там.

---

## 5. Stream Processing (Обработка потоков)

Данные никогда не заканчиваются.
"База данных — это подмножество потока данных на текущий момент".

### 5.1 Windows (Окна)

Как посчитать "среднее за час" в бесконечном потоке?

*   **Tumbling Window**: Каждые 5 минут. [00:00-00:05], [00:05-00:10]. Окна не перекрываются.

*   **Hopping Window**: Окно 5 минут, сдвиг 1 минута. [00:00-00:05], [00:01-00:06]. Перекрытие.

*   **Session Window**: Пока юзер активен + таймаут 30 мин. Размер окна динамический.

### 5.2 KSQL / Kafka Streams

Вам не нужно писать Java Consumer. Пишите SQL:

```sql

SELECT 
    userid, 
    count(*) 
FROM clicks 
WINDOW TUMBLING (SIZE 1 HOUR) 
GROUP BY userid 
HAVING count(*) > 100;
```
Это превращается в Topology, которая крутится 24/7.

**Реализация оконных функций:**

```python

from collections import defaultdict
from datetime import datetime, timedelta

class WindowedAggregator:
    """Агрегация данных по окнам."""
    
    def __init__(self, window_size_seconds=3600):
        self.window_size = window_size_seconds
        self.windows = defaultdict(lambda: defaultdict(int))  # window_start -> {key: count}
    
    def add_event(self, key, timestamp):
        """Добавление события в окно."""
        window_start = self.get_window_start(timestamp)
        self.windows[window_start][key] += 1
    
    def get_window_start(self, timestamp):
        """Вычисление начала окна."""
        dt = datetime.fromtimestamp(timestamp)
        # Округляем до начала часа
        window_start = dt.replace(minute=0, second=0, microsecond=0)
        return window_start.timestamp()
    
    def get_results(self, window_start):
        """Получение результатов для окна."""
        return dict(self.windows.get(window_start, {}))
    
    def get_top_k(self, window_start, k=10):
        """Топ-K элементов в окне."""
        results = self.get_results(window_start)
        return sorted(results.items(), key=lambda x: x[1], reverse=True)[:k]

# Пример использования
aggregator = WindowedAggregator(window_size_seconds=3600)  # 1 час

# Симулируем события

events = [
    ("user1", 1000),
    ("user2", 1001),
    ("user1", 1002),
    ("user3", 2000),
    ("user1", 3000),
]

for key, ts in events:
    aggregator.add_event(key, ts)

# Получаем топ пользователей за первый час
top = aggregator.get_top_k(1000, k=2)
print(top)  # [('user1', 3), ('user2', 1)]
```

**Sliding Window реализация:**

```python

class SlidingWindow:
    """Скользящее окно для подсчета событий."""
    
    def __init__(self, window_size_seconds=60):
        self.window_size = window_size_seconds
        self.events = []  # (timestamp, value)
    
    def add(self, value, timestamp=None):
        """Добавление события."""
        if timestamp is None:
            timestamp = time.time()
        self.events.append((timestamp, value))
        self.cleanup_old(timestamp)
    
    def cleanup_old(self, current_time):
        """Удаление событий старше окна."""
        cutoff = current_time - self.window_size
        self.events = [(ts, v) for ts, v in self.events if ts > cutoff]
    
    def count(self):
        """Количество событий в окне."""
        return len(self.events)
    
    def sum(self):
        """Сумма значений в окне."""
        return sum(v for _, v in self.events)
    
    def average(self):
        """Среднее значение в окне."""
        if not self.events:
            return 0
        return self.sum() / len(self.events)

# Пример: Rate Limiter на основе Sliding Window

rate_limiter = SlidingWindow(window_size_seconds=60)

def check_rate_limit(user_id, max_requests=100):
    """Проверка лимита запросов."""
    rate_limiter.add(1)  # Добавляем событие
    if rate_limiter.count() > max_requests:
        return False  # Превышен лимит
    return True
```

---

## 6. Glossary

*   **Topic**: Категория сообщений. Аналог таблицы в БД.

*   **Partition**: Шард топика. Единица масштабирования.

*   **Offset**: Уникальный ID сообщения в партиции.

*   **Broker**: Сервер Kafka.

*   **Producer**: Приложение, пишущее данные.

*   **Consumer Group**: Группа читателей. Kafka балансирует партиции между ними. Если у вас 10 партиций и 5 консьюмеров, каждый получит по 2.

*   **Lag**: Разница между последним оффсетом писателя (High Watermark) и оффсетом читателя. Мера отставания.

*   **Compaction (Log Compaction)**: Режим очистки лога, где Kafka хранит только *последнее* значение для каждого ключа. (Как KV Store).

*   **ISR (In-Sync Replicas)**: Список реплик, которые живы и успевают за лидером. Запись считается надежной, только если её подтвердили `min.insync.replicas`.

*   **Zookeeper / KRaft**: Сервис координации (метаданные кластера Kafka). Современная Kafka избавляется от ZK в пользу KRaft (встроенный Raft).

---

## 📚 Appendix A: Troubleshooting Guide

### A.1 Symptom: Consumer Lag is Growing

**Симптом**: `kafka-consumer-groups --describe` показывает Lag 1 000 000. Обработка отстает от риалтайма.
**Причина**:
1.  **Slow Processing**: Ваш бизнес-код (DB write, API call) слишком медленный. Kafka отдает быстро, вы не успеваете жевать.
2.  **Imbalance**: Весь трафик идет в одну партицию (плохой ключ партиционирования). Один консьюмер задыхается, остальные спят.
**Лечение**:
*   Добавить больше Партиций и больше Консьюмеров (Parallelism).
*   Оптимизировать код обработки (batch writes to DB).

### A.2 Symptom: Message Loss

**Симптом**: Клиент получил "OK", но сообщение потеряно при падении брокера.
**Причина**: `acks=1` (Leader only). Лидер принял, ответил OK, и тут же умер *до* репликации.
**Лечение**: Ставить `acks=all` (WAIT for ISR). Это медленнее, но надежнее.

---

## 📚 Appendix B: Historical Context

### 2010: LinkedIn

В LinkedIn (Джей Крепс, Неха Наркхеде, Джун Рао) был бардак. Сотни пайплайнов (XML, CSV, Logs) между Hadoop, DWH, Search. Спагетти-архитектура.
Они решили создать "Центральную нервную систему".
Вдохновлялись **Commit Log** баз данных. Назвали Kafka (в честь Франца Кафки, потому что система "оптимизирована для записи", а Кафка был писателем).

### The "Dumb Broker" Philosophy

В отличие от RabbitMQ (который умный: маршрутизация, retry, state tracking), Kafka сделала Брокера максимально тупым.
Брокер не знает, кто и что прочитал.
Вся логика (Offset tracking) вынесена на Клиента (или в спец. топик `__consumer_offsets`).
Это позволило скейлиться до миллионов сообщений. RabbitMQ на такое не способен.

### 2014: Confluent

Создатели ушли из LinkedIn и основали Confluent. Они добавили Schema Registry (Avro/Protobuf), KSQL, Kafka Connect.

---

## 📚 Appendix C: FAQ

**Q1: Kafka vs RabbitMQ?**
**A**:
*   **RabbitMQ**: Push-модель. Умный роутинг. Низкая задержка. Но не хранит историю (очередь очищается при чтении). Хорош для сложных Task Queues.

*   **Kafka**: Pull-модель. Хранит историю днями/неделями. Огромный Throughput. Основа для Data Pipeline.

**Q2: Можно ли использовать Kafka как Базу Данных?**
**A**: Мартин Клеппман говорит "Да" ("Turning the database inside out"). С Log Compaction и KTable вы можете хранить состояние вечно. NY Times хранит все стаьи (с 1851 года) в Kafka topic.

**Q3: Сколько партиций мне нужно?**
**A**: Партиции — это параллелизм. Если вам нужно читать в 10 потоков, нужно минимум 10 партиций. Но слишком много партиций (100k) перегружают Zookeeper/Controller долгой процедурой выборов лидера.

**Q4: Почему Kafka не удаляет сообщения после чтения?**
**A**: Потому что один топик могут читать 10 разных сервисов (Hadoop, Search, Billing). У каждого своя скорость. Лог персистентен (до истечения retention time, обычно 7 дней).

**Q5: Что если `sendfile` не поддерживается?**
**A**: Kafka упадет в производительности (будет User Space copy). Но на современных Linux/Java это работает из коробки (`FileChannel.transferTo`).

---

## 💡 Key Takeaways

1.  **Disk is fast**: Если вы пишете последовательно. Sequential IO > Random Memory Access (иногда).
2.  **Dumb Broker, Smart Client**: Секрет масштабируемости Kafka.
3.  **Events > State**: Храните события, а не состояние. Состояние всегда можно пересчитать.
4.  **Zero-Copy matters**: Использование `sendfile` и mmap может ускорить передачу данных в 10-20 раз.
5.  **Batching is essential**: Отправка сообщений батчами снижает overhead сети и улучшает сжатие.

---

## 🚀 Next Steps

**Практика:**

1.  Установите Kafka (или Docker: `confluentinc/cp-kafka`).
2.  Создайте топик с 3 партициями.
3.  Запустите `kafka-console-producer` и `consumer`.
4.  Посмотрите папку `/tmp/kafka-logs`. Найдите файлы `.log`. Откройте их `hexdump`.

В следующем модуле мы изучим **In-Memory** хранилища, которые живут в RAM, а не на диске. [Data Structures As Architecture (Redis)](../13_Data_Structures_As_Architecture/).


