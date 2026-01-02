# Интеграционные паттерны
## Point-to-Point, Request-Response, Publish-Subscribe, Message Queues

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы API и интеграции
- Знать синхронные и асинхронные API
- Иметь представление о архитектурных паттернах

**Recommended prior modules:**

- [01_What_is_API](../01_What_is_API/) — основы API и интеграции
- [03_Sync_Async_API](../03_Sync_Async_API/) — синхронные и асинхронные API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать интеграционные паттерны: Point-to-Point, Request-Response, Publish-Subscribe
- Применять Message Queues для надёжной асинхронной коммуникации
- Выбирать подходящий паттерн для конкретной задачи
- Понимать преимущества и ограничения каждого паттерна
- Проектировать интеграции с учётом масштабируемости и надёжности

---

## 1. Point-to-Point интеграция

**Point-to-Point** — это паттерн, где системы соединены напрямую друг с другом.

### 1.1 Концепция

В Point-to-Point каждая пара систем имеет прямое соединение. Система A напрямую знает о системе B и наоборот.

**Example: Point-to-Point интеграция**

```python
class PointToPointIntegration:
    """Прямое соединение между двумя системами"""
    
    def __init__(self):
        self.connections = {}
    
    def connect(self, system_a, system_b):
        """Создание прямого соединения"""
        self.connections[system_a] = system_b
        self.connections[system_b] = system_a
        print(f"Connected {system_a} <-> {system_b}")
    
    def send(self, from_system, to_system, data):
        """Отправка данных напрямую"""
        if self.connections.get(from_system) == to_system:
            print(f"{from_system} -> {to_system}: {data}")
            return True
        return False

# Использование

integration = PointToPointIntegration()
integration.connect("CRM", "Payment")
integration.send("CRM", "Payment", {"action": "create_payment"})
```

**Output:**
```
Connected CRM <-> Payment
CRM -> Payment: {'action': 'create_payment'}
```

### 1.2 Преимущества и ограничения

**Преимущества:**

- Простота реализации
- Низкая задержка
- Прямой контроль

**Ограничения:**

- Экспоненциальный рост соединений (N*(N-1)/2)
- Тесная связанность
- Сложность масштабирования

---

## 2. Request-Response паттерн

**Request-Response** — это синхронный паттерн, где клиент отправляет запрос и ждёт ответа.

### 2.1 Концепция

**Example: Request-Response**

```python
import requests

def request_response_call(url, data):
    """Синхронный Request-Response вызов"""
    response = requests.post(url, json=data)
    return response.json()

# Клиент отправляет запрос и ждёт ответа

result = request_response_call(
    "https://api.example.com/process",
    {"data": "value"}
)
print(f"Result: {result}")
```

**Характеристики:**

- Синхронный
- Клиент блокируется до ответа
- Простой в использовании
- Подходит для операций, требующих немедленного результата

---

## 3. Publish-Subscribe паттерн

**Publish-Subscribe (Pub/Sub)** — это паттерн, где издатель публикует события, а подписчики получают их.

### 3.1 Концепция

**Example: Publish-Subscribe**

```python
class PubSubIntegration:
    """Publish-Subscribe интеграция"""
    
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_type, subscriber, callback):
        """Подписка на событие"""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append({
            "subscriber": subscriber,
            "callback": callback
        })
        print(f"{subscriber} subscribed to {event_type}")
    
    def publish(self, event_type, data):
        """Публикация события"""
        if event_type in self.subscribers:
            for sub in self.subscribers[event_type]:
                sub["callback"](data)
                print(f"Event {event_type} delivered to {sub['subscriber']}")

# Использование

pubsub = PubSubIntegration()

# Подписка

def handle_user_created(data):
    print(f"Processing user created: {data}")

pubsub.subscribe("user.created", "Analytics", handle_user_created)
pubsub.subscribe("user.created", "EmailService", handle_user_created)

# Публикация

pubsub.publish("user.created", {"id": 123, "name": "Иван"})
```

**Output:**
```
Analytics subscribed to user.created
EmailService subscribed to user.created
Event user.created delivered to Analytics
Processing user created: {'id': 123, 'name': 'Иван'}
Event user.created delivered to EmailService
Processing user created: {'id': 123, 'name': 'Иван'}
```

### 3.2 Преимущества Pub/Sub

**Преимущества:**

- Decoupling: издатель не знает о подписчиках
- Масштабируемость: легко добавить подписчиков
- Гибкость: множественные подписчики на одно событие

---

## 4. Message Queues

**Message Queues** обеспечивают надёжную асинхронную доставку сообщений между системами.

### 4.1 Концепция

**Example: Message Queue**

```python
import queue
import threading

class MessageQueue:
    """Очередь сообщений"""
    
    def __init__(self):
        self.queue = queue.Queue()
        self.consumers = []
    
    def publish(self, message):
        """Публикация сообщения в очередь"""
        self.queue.put(message)
        print(f"Message published: {message}")
    
    def subscribe(self, consumer_name, handler):
        """Подписка на сообщения"""
        def consume():
            while True:
                message = self.queue.get()
                handler(message)
                self.queue.task_done()
        
        thread = threading.Thread(target=consume, daemon=True)
        thread.start()
        self.consumers.append(consumer_name)
        print(f"{consumer_name} subscribed to queue")

# Использование

mq = MessageQueue()

def process_order(message):
    print(f"Processing order: {message}")

mq.subscribe("OrderProcessor", process_order)

# Публикация

mq.publish({"order_id": 123, "total": 100.0})
```

**Преимущества:**

- Надёжность: сообщения сохраняются
- Асинхронность: отправитель не блокируется
- Масштабируемость: можно добавить обработчиков
- Decoupling: системы не знают друг о друге

### 4.2 Надёжная доставка

**Example: Надёжная доставка с подтверждением**

```python
class ReliableMessageQueue:
    """Message Queue с надёжной доставкой"""
    
    def __init__(self):
        self.queue = queue.Queue()
        self.pending = {}  # Сообщения в обработке
        self.delivered = set()  # Подтверждённые сообщения
    
    def publish(self, message):
        """Публикация с ID для отслеживания"""
        message_id = str(uuid.uuid4())
        message_with_id = {
            "id": message_id,
            "data": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.queue.put(message_with_id)
        return message_id
    
    def consume(self, handler):
        """Потребление с подтверждением"""
        message = self.queue.get()
        try:
            handler(message["data"])
            # Подтверждение доставки
            self.delivered.add(message["id"])
        except Exception as e:
            # В случае ошибки возвращаем в очередь
            self.queue.put(message)
            raise e
        finally:
            self.queue.task_done()
```

### 4.3 Приоритетные очереди

**Example: Message Queue с приоритетами**

```python
import heapq

class PriorityMessageQueue:
    """Message Queue с приоритетами"""
    
    def __init__(self):
        self.queue = []
        self.counter = 0  # Для стабильной сортировки
    
    def publish(self, message, priority=0):
        """Публикация с приоритетом (меньше = выше приоритет)"""
        heapq.heappush(self.queue, (priority, self.counter, message))
        self.counter += 1
    
    def consume(self):
        """Потребление с учётом приоритета"""
        if self.queue:
            priority, counter, message = heapq.heappop(self.queue)
            return message
        return None

# Использование

pq = PriorityMessageQueue()
pq.publish({"type": "critical", "data": "urgent"}, priority=1)
pq.publish({"type": "normal", "data": "regular"}, priority=5)
pq.publish({"type": "low", "data": "background"}, priority=10)

# Обработка в порядке приоритета

while True:
    message = pq.consume()
    if message:
        process(message)
    else:
        break
```

### 4.4 Dead Letter Queue

**Example: Dead Letter Queue для неудачных сообщений**

```python
class MessageQueueWithDLQ:
    """Message Queue с Dead Letter Queue"""
    
    def __init__(self, max_retries=3):
        self.queue = queue.Queue()
        self.dlq = queue.Queue()  # Dead Letter Queue
        self.max_retries = max_retries
        self.retry_count = {}
    
    def publish(self, message):
        """Публикация сообщения"""
        self.queue.put(message)
    
    def consume(self, handler):
        """Потребление с обработкой ошибок"""
        message = self.queue.get()
        message_id = message.get("id", str(uuid.uuid4()))
        
        try:
            handler(message)
            # Успешная обработка
            if message_id in self.retry_count:
                del self.retry_count[message_id]
        except Exception as e:
            # Ошибка обработки
            retries = self.retry_count.get(message_id, 0) + 1
            self.retry_count[message_id] = retries
            
            if retries >= self.max_retries:
                # Превышен лимит попыток - в DLQ
                self.dlq.put({
                    "original_message": message,
                    "error": str(e),
                    "retries": retries,
                    "timestamp": datetime.utcnow().isoformat()
                })
            else:
                # Повторная попытка
                self.queue.put(message)
```

---

## 5. Сравнение паттернов

### 5.1 Сравнительная таблица

| Паттерн | Связность | Масштабируемость | Надёжность | Сложность |
|---------|-----------|------------------|------------|-----------|
| **Point-to-Point** | Высокая | Плохая | Средняя | Низкая |
| **Request-Response** | Средняя | Средняя | Средняя | Низкая |
| **Pub/Sub** | Низкая | Хорошая | Средняя | Средняя |
| **Message Queue** | Низкая | Отличная | Высокая | Высокая |

### 5.2 Выбор паттерна

**Используйте Point-to-Point если:**

- Мало систем (2-3)
- Нужна простота
- Низкая задержка критична

**Используйте Request-Response если:**

- Нужен немедленный результат
- Простые операции
- Синхронность приемлема

**Используйте Pub/Sub если:**

- Множественные подписчики
- Decoupling важен
- События происходят нечасто

**Используйте Message Queue если:**

- Критична надёжность
- Нужна обработка пиков
- Асинхронность обязательна

---

## 6. Common Pitfalls

### 6.1 Pitfall: Point-to-Point для многих систем

❌ **Incorrect:**
```python
# Плохо: Point-to-Point для 10 систем = 45 соединений

connect_all_systems(systems)  # N*(N-1)/2
```

✅ **Correct:**
```python
# Хорошо: Message Queue для многих систем

mq = MessageQueue()
for system in systems:
    mq.subscribe(system, handler)
```

**Why:** Point-to-Point не масштабируется для большого количества систем.

### 6.2 Pitfall: Синхронный Request-Response для долгих операций

❌ **Incorrect:**
```python
# Плохо: Синхронный вызов для долгой операции

result = request_response_call("http://api/process-large-data", data)
# Клиент блокируется на долгое время
```

✅ **Correct:**
```python
# Хорошо: Асинхронная обработка через Message Queue

mq.publish({"task": "process-large-data", "data": data})
# Клиент не блокируется, получает результат позже
```

**Why:** Долгие операции должны быть асинхронными.

### 6.3 Pitfall: Pub/Sub без обработки ошибок

❌ **Incorrect:**
```python
# Плохо: Нет обработки ошибок подписчиков

def publish(event_type, data):
    for subscriber in subscribers[event_type]:
        subscriber.callback(data)  # Может упасть
```

✅ **Correct:**
```python
# Хорошо: Обработка ошибок для каждого подписчика

def publish(event_type, data):
    for subscriber in subscribers[event_type]:
        try:
            subscriber.callback(data)
        except Exception as e:
            log_error(subscriber, e)
            # Продолжаем обработку других подписчиков
```

**Why:** Ошибка одного подписчика не должна ломать остальных.

## 7. Гибридные подходы

### 7.1 Комбинирование паттернов

**Example: Request-Response с Message Queue**

```python
class HybridIntegration:
    """Комбинирование Request-Response и Message Queue"""
    
    def __init__(self):
        self.sync_api = SyncAPI()
        self.async_queue = MessageQueue()
    
    def process_request(self, request_type, data):
        """Обработка с выбором паттерна"""
        if request_type == "immediate":
            # Синхронный Request-Response
            return self.sync_api.process(data)
        else:
            # Асинхронный через Message Queue
            message_id = self.async_queue.publish(data)
            return {"status": "queued", "message_id": message_id}
```

### 7.2 Event Sourcing с Pub/Sub

**Example: Event Sourcing через Pub/Sub**

```python
class EventSourcedSystem:
    """Система с Event Sourcing через Pub/Sub"""
    
    def __init__(self):
        self.pubsub = PubSubIntegration()
        self.event_store = []
    
    def publish_event(self, event_type, event_data):
        """Публикация события"""
        event = {
            "type": event_type,
            "data": event_data,
            "timestamp": datetime.utcnow().isoformat(),
            "id": str(uuid.uuid4())
        }
        
        # Сохранение в event store
        self.event_store.append(event)
        
        # Публикация подписчикам
        self.pubsub.publish(event_type, event)
        
        return event["id"]
    
    def replay_events(self, event_type):
        """Воспроизведение событий"""
        events = [e for e in self.event_store if e["type"] == event_type]
        for event in events:
            self.pubsub.publish(event["type"], event["data"])
```

---

## 💡 Key Takeaways

- **Point-to-Point**: Прямое соединение между системами. Простой, но не масштабируется для многих систем

- **Request-Response**: Синхронный паттерн для операций, требующих немедленного результата. Простой, но блокирующий

- **Publish-Subscribe**: Паттерн для событий с множественными подписчиками. Обеспечивает decoupling и гибкость

- **Message Queues**: Надёжная асинхронная доставка сообщений. Подходит для критичных операций с требованиями надёжности

- **Выбор паттерна**: Зависит от требований к связности, масштабируемости, надёжности и сложности. Каждый паттерн решает свои задачи

---

## 🚀 Next Steps

**Related Modules:**

- [12_Advanced_Patterns](../12_Advanced_Patterns/) — продвинутые интеграционные паттерны
- [03_Sync_Async_API](../03_Sync_Async_API/) — синхронные и асинхронные API

**Practice Ideas:**

1. Реализуйте Point-to-Point интеграцию между двумя системами
2. Создайте Pub/Sub систему с несколькими подписчиками
3. Настройте Message Queue для асинхронной обработки

**Going Deeper:**

- Enterprise Integration Patterns: паттерны интеграции на уровне предприятия
- Message Queue Patterns: паттерны работы с очередями
- Event-Driven Architecture: событийно-ориентированная архитектура

---

## 📚 Additional Resources

**Documentation:**

- [RabbitMQ Tutorial](https://www.rabbitmq.com/getstarted.html) — работа с очередями
- [Apache Kafka](https://kafka.apache.org/documentation/) — распределённая очередь сообщений

**Articles:**

- "Integration Patterns: A Comprehensive Guide" — руководство по паттернам интеграции
- "Pub/Sub vs Message Queues" — сравнение паттернов

---




