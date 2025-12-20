# Протоколы между компонентами и сервисами
## Message queues, Event-driven systems, Pub/Sub, Backpressure

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые протоколы передачи сообщений (модуль 05)
- Понимать API как протокол (модуль 08)
- Иметь представление о распределённых системах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять message queues для асинхронной коммуникации
- Проектировать event-driven системы
- Использовать Pub/Sub паттерн для масштабируемости
- Обрабатывать backpressure для предотвращения перегрузки

---

## 1. Введение: коммуникация между сервисами

В распределённых системах компоненты и сервисы должны взаимодействовать. **Протоколы коммуникации** определяют, как это происходит:

- **Синхронно** (HTTP, gRPC) — клиент ждёт ответа

- **Асинхронно** (message queues, events) — отправил и продолжил

В этом модуле мы рассмотрим асинхронные протоколы коммуникации.

---

## 2. Message Queues

### 2.1 Концепция

**Message Queue** — асинхронный протокол обмена сообщениями через очередь.

**Компоненты:**

- **Producer**: отправляет сообщения в очередь

- **Queue**: хранит сообщения

- **Consumer**: получает и обрабатывает сообщения

### 2.2 Базовая модель

```

Producer → [Queue] → Consumer

Producer отправляет: {"order_id": 123, "action": "process"}
Consumer получает и обрабатывает
```

**Преимущества:**

- Decoupling: producer и consumer не знают друг о друге
- Асинхронность: producer не ждёт обработки
- Буферизация: очередь поглощает пики нагрузки
- Надёжность: сообщения не теряются при падении consumer

### 2.3 Пример: RabbitMQ

```python

import pika

# Producer
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks')

channel.basic_publish(
    exchange='',
    routing_key='tasks',
    body='Process order 123'
)
print("Sent message")
connection.close()

# Consumer
def callback(ch, method, properties, body):
    print(f"Received: {body}")
    # Process message
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks')
channel.basic_consume(queue='tasks', on_message_callback=callback)
channel.start_consuming()
```

### 2.4 At-least-once delivery

**Проблема:** Consumer может упасть после получения, но до обработки.

**Решение:** Acknowledgments (ACK)

```

1. Consumer получает сообщение
2. Consumer обрабатывает сообщение
3. Consumer отправляет ACK
4. Queue удаляет сообщение
```

Если Consumer упадёт до ACK, сообщение будет повторно доставлено.

---

## 3. Event-Driven Systems

### 3.1 Концепция

**Event-Driven** — система реагирует на события, а не на прямые запросы.

**Компоненты:**

- **Event Producer**: генерирует события

- **Event Bus**: распространяет события

- **Event Consumer**: подписывается на события и реагирует

### 3.2 Пример: Order Processing

```

Order Service → Event: OrderCreated
    ↓
Event Bus
    ↓
    ├→ Inventory Service (reserves items)
    ├→ Payment Service (processes payment)
    └→ Notification Service (sends email)
```

**Преимущества:**

- Loose coupling: сервисы не знают друг о друге
- Extensibility: легко добавить новый consumer
- Scalability: consumers масштабируются независимо

### 3.3 Event structure

```json

{
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "event_type": "OrderCreated",
  "timestamp": "2024-01-15T10:00:00Z",
  "data": {
    "order_id": 123,
    "user_id": 456,
    "items": [{"product_id": 789, "quantity": 2}]
  }
}
```

### 3.4 Event sourcing

**Event Sourcing** — хранение всех изменений как последовательность событий.

```

Events:

1. OrderCreated {order_id: 123, items: [...]}
2. OrderPaid {order_id: 123, amount: 100}
3. OrderShipped {order_id: 123, tracking: "..."}

Current state = применение всех событий
```

**Преимущества:**

- Полная история изменений
- Audit trail
- Возможность replay событий

---

## 4. Pub/Sub (Publish/Subscribe)

### 4.1 Концепция

**Pub/Sub** — паттерн, где publishers отправляют сообщения в topics, subscribers получают из topics.

**Отличие от queue:**

- **Queue**: одно сообщение → один consumer

- **Pub/Sub**: одно сообщение → множество subscribers

### 4.2 Модель

```

Publisher → Topic: "orders" → Subscriber 1 (Inventory)
                           → Subscriber 2 (Notifications)
                           → Subscriber 3 (Analytics)
```

Все subscribers получают каждое сообщение из topic.

### 4.3 Пример: Redis Pub/Sub

```python

import redis

# Publisher

r = redis.Redis()
r.publish('orders', 'New order: 123')

# Subscriber
p = r.pubsub()
p.subscribe('orders')

for message in p.listen():
    if message['type'] == 'message':
        print(f"Received: {message['data']}")
```

### 4.4 Topics и filters

**Hierarchical topics:**
```

orders/created
orders/paid
orders/shipped
```

**Wildcards:**
```

orders/*           # все события orders
orders/created     # только created

*/created          # created от всех
```

---

## 5. Backpressure

### 5.1 Проблема

**Проблема:** Producer быстрее consumer, очередь растёт → OOM (Out of Memory).

```

Producer: 1000 msg/sec
Consumer: 100 msg/sec
Queue: растёт на 900 msg/sec → через 100 сек = 90k сообщений!
```

### 5.2 Стратегии backpressure

**1. Blocking (блокировка producer):**
```python

queue.put(message, block=True, timeout=5)
# Блокируется, если очередь заполнена
```

**2. Drop (отбрасывание сообщений):**
```python

try:
    queue.put_nowait(message)
except queue.Full:
    print("Queue full, dropping message")
```

**3. Buffering with limit:**
```python

queue = Queue(maxsize=1000)
# Ограничение размера очереди

```

**4. Rate limiting (ограничение скорости):**
```python

import time

for message in messages:
    queue.put(message)
    time.sleep(0.01)  # 100 msg/sec max
```

### 5.3 Reactive Streams

**Protocol for backpressure:**
```

Consumer: Request(10) → Producer
Producer: onNext(msg1), onNext(msg2), ... onNext(msg10)
Consumer: Request(10) → Producer
```

Consumer контролирует скорость через requests.

### 5.4 Flow control

**TCP flow control:**

- Window size: сколько данных можно отправить без ACK
- Backpressure встроен в протокол

**Application level:**
```python

class RateLimitedProducer:
    def __init__(self, max_rate):
        self.max_rate = max_rate
        self.tokens = max_rate
        self.last_update = time.time()
    
    def send(self, message):
        self._refill_tokens()
        if self.tokens >= 1:
            self.tokens -= 1
            self._actual_send(message)
        else:
            raise RateLimitExceeded()
```

---

## 6. Гарантии доставки

### 6.1 At-most-once

**Характеристики:**

- Сообщения могут быть потеряны
- Сообщения не дублируются
- Самое быстрое

**Применение:** Метрики, логи (потеря допустима)

### 6.2 At-least-once

**Характеристики:**

- Сообщения не теряются
- Могут быть дубликаты
- Средняя производительность

**Применение:** Большинство систем (orders, payments с идемпотентностью)

### 6.3 Exactly-once

**Характеристики:**

- Сообщения доставляются ровно один раз
- Нет потерь и дубликатов
- Самое медленное, сложное

**Применение:** Критичные транзакции (финансы)

### 6.4 Идемпотентность

**Для at-least-once нужна идемпотентность:**

```python

def process_order(order_id):
    # Проверка, не обработан ли уже
    if is_already_processed(order_id):
        return  # Идемпотентность
    
    # Обработка
    process(order_id)
    mark_as_processed(order_id)
```

---

## 7. Сравнение паттернов

| Паттерн | Coupling | Гарантии | Scalability | Use case |
|---------|----------|----------|-------------|----------|
| HTTP API | Tight | Sync | Limited | CRUD операции |
| Message Queue | Loose | At-least-once | High | Async tasks |
| Pub/Sub | Very loose | At-most-once | Very high | Events, notifications |
| Event Sourcing | Loose | Exactly-once | High | Audit, replay |

---

## 💡 Key Takeaways

- **Message queues для decoupling**: Очереди разделяют producer и consumer, обеспечивая асинхронность и буферизацию пиков нагрузки.

- **Event-driven для масштабируемости**: События позволяют добавлять новых consumers без изменения producers, создавая расширяемые системы.

- **Pub/Sub для broadcasting**: Одно сообщение доставляется множеству subscribers, идеально для уведомлений и реакций на события.

- **Backpressure критичен**: Без backpressure быстрый producer перегружает медленный consumer. Стратегии: blocking, dropping, rate limiting.

- **Гарантии доставки — компромисс**: At-most-once (быстро, потери), at-least-once (средне, дубликаты), exactly-once (медленно, сложно). Выбор зависит от требований.

---

## 🚀 Next Steps

**Related Modules:**

- [16_Distributed_Systems_Protocols](../16_Distributed_Systems_Protocols/) — протоколы распределённых систем: consensus, leader election
- [08_API_As_Protocol](../08_API_As_Protocol/) — синхронные протоколы: REST, gRPC, GraphQL

**Practice Ideas:**

1. Реализуйте producer-consumer систему с RabbitMQ или Redis
2. Спроектируйте event-driven систему для заказов (order processing)
3. Реализуйте backpressure через rate limiting

**Going Deeper:**

- Изучите Kafka для высокопроизводительного event streaming
- Изучите NATS для легковесного messaging
- Изучите Reactive Streams spec для стандартизированного backpressure

---



