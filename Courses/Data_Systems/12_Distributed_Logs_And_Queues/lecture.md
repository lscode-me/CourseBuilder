# Distributed Logs и Очереди
## Kafka концепции, Append-only logs, Offset и Stream Processing

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать концепцию WAL (Write-Ahead Log)
- Знать модель Publisher/Subscriber
- Понимать, как работает последовательная запись на диск

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять, почему Лог — это универсальная структура данных для распределенных систем
- Понимать архитектуру Apache Kafka (Topics, Partitions, Brokers)
- Различать Queues (RabbitMQ) и Logs (Kafka)
- Понимать семантику доставки (At-most-once, At-least-once, Exactly-once)

---

## 1. Лог как сердце архитектуры

Мы привыкли думать о базах данных как о таблицах. Но внутри БД (как мы узнали в Модуле 2) главное — это **Лог (WAL)**.
Если лог — это так круто, почему бы не сделать его центральным элементом всей архитектуры?

**Идея**: The Unified Log.
Все события в системе пишутся в единый, упорядоченный, персистентный лог.
Сервисы читают этот лог и обновляют свои локальные базы данных.

### 1.1 Log vs Database

*   **Database**: Хранит *текущее состояние* (State). "Баланс = 100".

*   **Log**: Хранит *историю изменений* (Events). "Депозит +50", "Покупка -20", "Депозит +70".

Состояние — это производная от лога.
`State = Apply(Log)`

---

## 2. Архитектура Message Queue vs Log

### 2.1 Message Queue (RabbitMQ, SQS)

*   **Ephemeral**: Сообщение удаляется сразу после обработки (ack).

*   **Work Queue**: Если много потребителей, сообщение достается *одному* из них (балансировка).

*   **Random Access**: Нет (обычно FIFO).

### 2.2 Log-based Broker (Apache Kafka, Amazon Kinesis)

*   **Persistent**: Сообщения хранятся на диске дни или недели (Retention Policy).

*   **Broadcast**: Все потребители (в разных Consumer Groups) читают *одни и те же* сообщения.

*   **Replay**: Можно перемотать назад и перечитать историю (например, чтобы перестроить базу данных).

```

[Producer] -> [ LOG (Append Only) ] -> [Consumer A (Offset: 10)]

                                   -> [Consumer B (Offset: 5)]
```

---

## 3. Устройство Apache Kafka

Kafka — это распределенный commit log.

### 3.1 Topic & Partitions

Данные организованы в **Topics** (темы), например "user_clicks".
Топик режется на **Partitions** (партиции) для масштабирования.

*   Partition 0: хранится на сервере A.
*   Partition 1: хранится на сервере B.

Внутри партиции сообщения строго упорядочены и имеют **Offset** (ID: 0, 1, 2...).

**Порядок гарантируется только внутри партиции!**

```python
# Логическая структура Partition
# Offset:  0      1      2      3
# Data:   [MsgA] [MsgB] [MsgC] [MsgD] ...

```

### 3.2 Producers & Consumers

*   **Producer**: Выбирает партицию (обычно hash(key) % N) и пишет в конец.

*   **Consumer Group**: Группа сервисов, читающих топик.
    *   Kafka гарантирует, что одну партицию читает только *один* консьюмер в группе.
    *   Это позволяет параллелить обработку.

### 3.3 Consumer Offset

Консьюмер сам хранит информацию, до куда он дочитал (Offset).
Если консьюмер упал, другой подхватит его работу с последнего закоммиченного оффсета.

---

## 4. Демонстрация: Simple Log Broker

Эмуляция работы Kafka-подобного брокера на файлах.

```python

import os
import time

class SimpleLogPartition:
    def __init__(self, name):
        self.filename = f"{name}.log"
        self.offset = 0
        
    def append(self, message):
        """Producer: Append-only write"""
        with open(self.filename, "a") as f:
            # Format: Offset:Message
            entry = f"{self.offset}:{message}\n"
            f.write(entry)
            print(f"Written offset {self.offset}")
            self.offset += 1
            
    def read(self, read_offset, count=5):
        """Consumer: Sequential read from offset"""
        if not os.path.exists(self.filename):
            return []
            
        messages = []
        with open(self.filename, "r") as f:
            for line in f:
                # Простой парсинг (в реальности binary format + indexing)
                parts = line.strip().split(":", 1)
                msg_offset = int(parts[0])
                msg_body = parts[1]
                
                if msg_offset >= read_offset:
                    messages.append((msg_offset, msg_body))
                    if len(messages) >= count:
                        break
        return messages

# Сценарий
log = SimpleLogPartition("clicks")

print("--- Producer writes ---")
log.append("User 1 Click")
log.append("User 2 Click")
log.append("User 1 Buy")

print("--- Consumer A reads from 0 ---")
batch1 = log.read(0)
for off, msg in batch1:
    print(f"Got [{off}]: {msg}")
    # Обработали, коммитим оффсет
    committed_offset_a = off + 1

print("--- Producer writes more ---")
log.append("User 3 Login")

print(f"--- Consumer A reads from {committed_offset_a} ---")
batch2 = log.read(committed_offset_a)
for off, msg in batch2:
    print(f"Got [{off}]: {msg}")

# Cleanup
os.remove("clicks.log")
```

**Output:**
```

--- Producer writes ---
Written offset 0
Written offset 1
Written offset 2
--- Consumer A reads from 0 ---
Got [0]: User 1 Click
Got [1]: User 2 Click
Got [2]: User 1 Buy

--- Producer writes more ---
Written offset 3

--- Consumer A reads from 3 ---
Got [3]: User 3 Login
```

---

## 5. Семантика доставки (Delivery Semantics)

Самая сложная часть распределенных очередей.

### 5.1 At-most-once (Максимум один раз)

*   Отправили — забыли. Или: прочитали, сдвинули оффсет, *потом* начали обрабатывать.
*   Если обработка упала — сообщение потеряно.
*   *Где*: Мониторинг, метрики (потеря пары пакетов не страшно).

### 5.2 At-least-once (Минимум один раз)

*   Прочитали, обработали, *только потом* сдвинули оффсет.
*   Если упали после обработки, но до сдвига оффсета — сообщение будет прочитано снова.
*   *Результат*: Дубликаты. Нужна **Идемпотентность** (умение обрабатывать дубли корректно).
*   *Где*: Платежи, бизнес-логика (стандарт де-факто).

### 5.3 Exactly-once (Ровно один раз)

*   Святой Грааль. Очень сложно достичь.
*   Kafka Transactions позволяют делать exactly-once между топиками (чтение из Kafka -> обработка -> запись в Kafka).
*   Для связи с внешним миром (Kafka -> Database) обычно используют идемпотентность потребителя.

---

## 6. Stream Processing

Логи позволяют перейти от пакетной обработки (Batch ETL) к потоковой (Streaming).

*   **Batch**: Запускаем Job раз в сутки, считаем статистику за вчера.

*   **Stream**: Обрабатываем каждое событие из Kafka по мере поступления, обновляем витрины данных в реальном времени.

Инструменты: Kafka Streams, Apache Flink, Spark Structured Streaming.

---

## 7. Change Data Capture (CDC)

Как засунуть базу данных в Kafka?
Использовать **CDC (Change Data Capture)**.
Коннектор (например, Debezium) читает WAL базы данных (Postgres/MySQL) и транслирует каждое изменение (Insert/Update/Delete) как событие в Kafka.
Это позволяет строить реактивные системы на основе старых баз.

---

## 💡 Key Takeaways

- **Лог** — это фундаментальная структура упорядоченных событий.

- **Kafka** — это не очередь сообщений, а распределенный лог с долгосрочным хранением.

- **Partitioning** обеспечивает масштабируемость (Total Order только внутри партиции).

- **At-least-once** доставка требует от потребителей быть **идемпотентными**.

- **CDC** превращает базу данных в поток событий.

---

## 🚀 Next Steps

**Module 4 Preview:**

- Мы изучили кирпичики: Алгоритмы, Индексы (B-tree, LSM), Распределенные концепции (CAP, DHT, Replication, Logs).
- В финальном модуле мы будем собирать из них **Архитектуру**.
- Как выбрать правильную БД? Как спроектировать Twitter?

**Practice Ideas:**

1. Запустите Kafka в Docker (Confluent Platform). Создайте топик с 3 партициями.
2. Напишите Producer и Consumer на Python (`confluent-kafka` или `kafka-python`). Посмотрите, как меняются оффсеты.
3. Симулируйте At-least-once: обработайте сообщение, но "упадите" до коммита оффсета. Проверьте, что сообщение придет снова.

---


