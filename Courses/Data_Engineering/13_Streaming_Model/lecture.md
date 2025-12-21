# Streaming как модель обработки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать batch processing (модуль 09)
- Знать жизненный цикл данных (модуль 02)
- Иметь представление о распределённых системах

**Recommended prior modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing
- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять концепцию streaming обработки
- Различать event-driven и batch системы
- Понимать семантику доставки: exactly-once, at-least-once
- Применять windowing для агрегации потоковых данных

---

## 1. Введение в Streaming

Streaming processing — это обработка данных в реальном времени по мере их поступления. В отличие от batch, streaming обрабатывает непрерывный поток событий.

**Характеристики streaming:**

- Непрерывная обработка
- Низкая задержка (latency)
- Event-driven архитектура
- Обработка неограниченных потоков

---

## 2. Event-driven Systems

Event-driven системы реагируют на события в реальном времени.

### 2.1 Концепция событий

**Event (Событие):**

- Действие или изменение состояния
- Неизменяемая запись
- Временная метка

**Event Stream:**

- Непрерывная последовательность событий
- Упорядоченная по времени
- Неограниченный поток

**Example: Event-driven система**

```python

class EventDrivenSystem:
    def __init__(self):
        self.event_handlers = {}
        self.event_stream = []
    
    def register_handler(self, event_type, handler):
        """Регистрирует обработчик события"""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)
        print(f"✅ Обработчик зарегистрирован для '{event_type}'")
    
    def emit_event(self, event):
        """Генерирует событие"""
        event_type = event.get("type")
        event["timestamp"] = "2024-01-01T10:00:00Z"
        
        self.event_stream.append(event)
        print(f"📡 Событие '{event_type}' отправлено")
        
        # Обработка события
        if event_type in self.event_handlers:
            for handler in self.event_handlers[event_type]:
                handler(event)
    
    def get_event_stream(self):
        """Возвращает поток событий"""
        return self.event_stream

# Использование
system = EventDrivenSystem()

# Регистрация обработчиков
def handle_user_click(event):
    print(f"  🖱️  Обработка клика: пользователь {event.get('user_id')}")

def handle_purchase(event):
    print(f"  💰 Обработка покупки: заказ {event.get('order_id')}, сумма ${event.get('amount')}")

system.register_handler("user_click", handle_user_click)
system.register_handler("purchase", handle_purchase)

# Генерация событий

system.emit_event({"type": "user_click", "user_id": 123, "page": "/products"})
system.emit_event({"type": "purchase", "order_id": 1001, "amount": 99.99})
```

**Output:**
```

✅ Обработчик зарегистрирован для 'user_click'
✅ Обработчик зарегистрирован для 'purchase'
📡 Событие 'user_click' отправлено
  🖱️  Обработка клика: пользователь 123
📡 Событие 'purchase' отправлено
  💰 Обработка покупки: заказ 1001, сумма $99.99
```

---

## 3. Streams vs Batches

Понимание различий критично для выбора подхода.

### 3.1 Batch Processing

**Характеристики:**

- Обработка накопленных данных
- Запуск по расписанию
- Высокая пропускная способность
- Задержка от минут до дней

**Use cases:**

- Исторические данные
- Большие объёмы
- Сложные агрегации
- Когда задержка не критична

### 3.2 Streaming Processing

**Характеристики:**

- Обработка по мере поступления
- Непрерывная обработка
- Низкая задержка (секунды/миллисекунды)
- Обработка неограниченных потоков

**Use cases:**

- Real-time аналитика
- Мониторинг
- Fraud detection
- Когда нужна низкая задержка

**Example: Сравнение**

```python
# Batch: обработка накопленных данных
def batch_process(data_batch):
    """Обрабатывает батч данных"""
    print(f"📦 Batch: обработка {len(data_batch)} записей")
    # Симуляция обработки
    result = sum(r.get("value", 0) for r in data_batch)
    print(f"✅ Batch результат: {result}")
    return result

# Streaming: обработка по мере поступления
def stream_process(event):
    """Обрабатывает одно событие"""
    print(f"📡 Streaming: обработка события {event.get('id')}")
    # Симуляция обработки
    result = event.get("value", 0)
    print(f"✅ Streaming результат: {result}")
    return result

# Сравнение
data = [{"id": i, "value": i*10} for i in range(1, 6)]

print("BATCH Processing:")
batch_result = batch_process(data)

print("\nSTREAMING Processing:")
stream_results = []
for event in data:
    result = stream_process(event)
    stream_results.append(result)

print(f"\nСравнение:")
print(f"  Batch: обработано {len(data)} записей за один раз, задержка: высокая")
print(f"  Streaming: обработано {len(stream_results)} событий по мере поступления, задержка: низкая")
```

**Output:**
```

BATCH Processing:
📦 Batch: обработка 5 записей
✅ Batch результат: 150

STREAMING Processing:
📡 Streaming: обработка события 1
✅ Streaming результат: 10
📡 Streaming: обработка события 2
✅ Streaming результат: 20
📡 Streaming: обработка события 3
✅ Streaming результат: 30
📡 Streaming: обработка события 4
✅ Streaming результат: 40
📡 Streaming: обработка события 5
✅ Streaming результат: 50

Сравнение:
  Batch: обработано 5 записей за один раз, задержка: высокая
  Streaming: обработано 5 событий по мере поступления, задержка: низкая
```

---

## 4. Exactly-once vs At-least-once

Семантика доставки определяет, сколько раз событие будет обработано.

### 4.1 At-least-once

**Характеристики:**

- Событие обработано минимум один раз
- Возможны дубликаты
- Проще в реализации
- Требует идемпотентности

**Example: At-least-once**

```python

class AtLeastOnceDelivery:
    def __init__(self):
        self.processed_events = set()
    
    def process_event(self, event_id, event_data):
        """Обрабатывает событие (может быть дубликат)"""
        print(f"📡 Получено событие {event_id}")
        
        # Обработка (может быть вызвана несколько раз)
        result = f"processed_{event_id}"
        
        # Идемпотентная обработка
        if event_id not in self.processed_events:
            self.processed_events.add(event_id)
            print(f"✅ Событие {event_id} обработано")
        else:
            print(f"⏭️  Событие {event_id} уже обработано (дубликат игнорирован)")
        
        return result

# Использование
delivery = AtLeastOnceDelivery()

# Первая обработка

delivery.process_event("evt_001", {"data": "value1"})

# Дубликат (at-least-once может доставить дважды)
print("\nПовторная доставка (дубликат):")
delivery.process_event("evt_001", {"data": "value1"})
```

**Output:**
```

📡 Получено событие evt_001
✅ Событие evt_001 обработано

Повторная доставка (дубликат):
📡 Получено событие evt_001
⏭️  Событие evt_001 уже обработано (дубликат игнорирован)
```

### 4.2 Exactly-once

**Характеристики:**

- Событие обработано ровно один раз
- Нет дубликатов
- Сложнее в реализации
- Требует координации

**Example: Exactly-once концепция**

```python

class ExactlyOnceDelivery:
    def __init__(self):
        self.processed_events = set()
        self.transactions = {}
    
    def process_event_transactional(self, event_id, event_data):
        """Обрабатывает событие транзакционно (exactly-once)"""
        # Начало транзакции
        transaction_id = f"tx_{event_id}"
        self.transactions[transaction_id] = {
            "event_id": event_id,
            "status": "processing"
        }
        
        print(f"🔄 Транзакция {transaction_id} начата для события {event_id}")
        
        # Обработка
        if event_id not in self.processed_events:
            result = f"processed_{event_id}"
            self.processed_events.add(event_id)
            self.transactions[transaction_id]["status"] = "committed"
            print(f"✅ Событие {event_id} обработано (exactly-once)")
            return result
        else:
            self.transactions[transaction_id]["status"] = "rolled_back"
            print(f"⏭️  Событие {event_id} уже обработано, транзакция откачена")
            return None

# Использование

exactly_once = ExactlyOnceDelivery()

# Обработка

exactly_once.process_event_transactional("evt_001", {"data": "value1"})

# Попытка повторной обработки
print("\nПопытка повторной обработки:")
exactly_once.process_event_transactional("evt_001", {"data": "value1"})
```

**Output:**
```

🔄 Транзакция tx_evt_001 начата для события evt_001
✅ Событие evt_001 обработано (exactly-once)

Попытка повторной обработки:
🔄 Транзакция tx_evt_001 начата для события evt_001
⏭️  Событие evt_001 уже обработано, транзакция откачена
```

### 4.3 Сравнение

| Аспект | At-least-once | Exactly-once |
|--------|---------------|--------------|
| **Гарантии** | Минимум один раз | Ровно один раз |
| **Дубликаты** | Возможны | Нет |
| **Сложность** | Проще | Сложнее |
| **Производительность** | Выше | Ниже |
| **Требования** | Идемпотентность | Транзакции |

---

## 5. Windowing (Оконные функции)

Windowing позволяет агрегировать потоковые данные по временным окнам.

### 5.1 Типы окон

**Tumbling Windows:**

- Непересекающиеся окна
- Фиксированный размер
- Пример: каждые 5 минут

**Sliding Windows:**

- Пересекающиеся окна
- Скользящее окно
- Пример: последние 5 минут каждую минуту

**Session Windows:**

- Окна по активности
- Динамический размер
- Пример: сессия пользователя

**Example: Windowing**

```python

from datetime import datetime, timedelta

class WindowProcessor:
    def __init__(self, window_size_minutes=5):
        self.window_size = timedelta(minutes=window_size_minutes)
        self.events = []
    
    def add_event(self, event, timestamp):
        """Добавляет событие"""
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        
        self.events.append({
            "event": event,
            "timestamp": timestamp
        })
    
    def tumbling_window(self, window_start):
        """Tumbling window: непересекающиеся окна"""
        window_end = window_start + self.window_size
        
        window_events = [
            e for e in self.events
            if window_start <= e["timestamp"] < window_end
        ]
        
        return {
            "window_start": window_start,
            "window_end": window_end,
            "events": window_events,
            "count": len(window_events)
        }
    
    def sliding_window(self, current_time, window_size_minutes):
        """Sliding window: скользящее окно"""
        window_start = current_time - timedelta(minutes=window_size_minutes)
        
        window_events = [
            e for e in self.events
            if window_start <= e["timestamp"] <= current_time
        ]
        
        return {
            "window_start": window_start,
            "window_end": current_time,
            "events": window_events,
            "count": len(window_events)
        }

# Использование
processor = WindowProcessor(window_size_minutes=5)

# Добавление событий
base_time = datetime(2024, 1, 1, 10, 0, 0)
for i in range(10):
    processor.add_event({"id": i, "value": i*10}, base_time + timedelta(minutes=i))

# Tumbling window

tumbling = processor.tumbling_window(base_time)
print(f"Tumbling Window (10:00-10:05):")
print(f"  Событий: {tumbling['count']}")

# Sliding window
sliding = processor.sliding_window(base_time + timedelta(minutes=7), 5)
print(f"\nSliding Window (последние 5 минут до 10:07):")
print(f"  Событий: {sliding['count']}")
```

**Output:**
```

Tumbling Window (10:00-10:05):
  Событий: 5

Sliding Window (последние 5 минут до 10:07):
  Событий: 5
```

---

## 6. Use Cases для Streaming

Streaming подходит для различных use cases.

### 6.1 Real-time Analytics

**Характеристики:**

- Аналитика в реальном времени
- Дашборды с live данными
- Мониторинг метрик

**Example: Real-time Analytics**

```python

class RealTimeAnalytics:
    def __init__(self):
        self.metrics = {
            "total_events": 0,
            "total_revenue": 0.0,
            "events_per_minute": 0
        }
        self.recent_events = []
    
    def process_event(self, event):
        """Обрабатывает событие и обновляет метрики"""
        self.metrics["total_events"] += 1
        
        if "revenue" in event:
            self.metrics["total_revenue"] += event["revenue"]
        
        self.recent_events.append({
            "event": event,
            "timestamp": datetime.now()
        })
        
        # Обновление метрик
        self._update_metrics()
    
    def _update_metrics(self):
        """Обновляет метрики"""
        # Симуляция вычисления events per minute
        self.metrics["events_per_minute"] = len([
            e for e in self.recent_events
            if (datetime.now() - e["timestamp"]).total_seconds() < 60
        ])
    
    def get_dashboard(self):
        """Возвращает данные для дашборда"""
        return {
            "total_events": self.metrics["total_events"],
            "total_revenue": f"${self.metrics['total_revenue']:.2f}",
            "events_per_minute": self.metrics["events_per_minute"]
        }

# Использование

analytics = RealTimeAnalytics()

# Обработка событий
analytics.process_event({"type": "purchase", "revenue": 99.99})
analytics.process_event({"type": "purchase", "revenue": 149.99})
analytics.process_event({"type": "view"})

dashboard = analytics.get_dashboard()
print("Real-time Dashboard:")
for key, value in dashboard.items():
    print(f"  {key}: {value}")
```

**Output:**
```

Real-time Dashboard:
  total_events: 3
  total_revenue: $249.98
  events_per_minute: 3
```

---

## 💡 Key Takeaways

- **Streaming vs Batch**: Streaming обрабатывает данные в реальном времени с низкой задержкой, batch обрабатывает накопленные данные порциями. Выбор зависит от требований к задержке.

- **Event-driven Systems**: Системы, реагирующие на события в реальном времени. События неизменяемы и упорядочены по времени.

- **Exactly-once vs At-least-once**: At-least-once проще, но требует идемпотентности. Exactly-once сложнее, но гарантирует обработку ровно один раз.

- **Windowing**: Агрегация потоковых данных по временным окнам (tumbling, sliding, session). Критично для аналитики в реальном времени.

- **Use Cases**: Real-time аналитика, мониторинг, fraud detection — все требуют низкой задержки и streaming обработки.

---

## 🚀 Next Steps

**Related Modules:**

- [14_Streaming_Tools](../14_Streaming_Tools/) — инструменты streaming (Kafka, Flink)
- [15_Streaming_Storage](../15_Streaming_Storage/) — хранение потоковых данных
- [16_Streaming_UseCases](../16_Streaming_UseCases/) — use cases streaming

**Practice Ideas:**

1. Создайте простую event-driven систему: обработка событий в реальном времени
2. Реализуйте windowing: агрегация данных по временным окнам
3. Изучите разницу между at-least-once и exactly-once на практике

**Going Deeper:**

- Изучите Kafka: event streaming platform
- Погрузитесь в Flink: stream processing engine
- Изучите паттерны streaming: CQRS, event sourcing

---

## 📚 Additional Resources

**Books:**

- "Streaming Systems" by Tyler Akidau — фундаментальная книга о streaming
- "Designing Data-Intensive Applications" by Martin Kleppmann — streaming systems

**Articles:**

- "The World Beyond Batch: Streaming 101" — введение в streaming
- "Exactly-once Semantics" — детальное объяснение

**Documentation:**

- Apache Kafka: https://kafka.apache.org/documentation/
- Apache Flink: https://flink.apache.org/docs/

---


