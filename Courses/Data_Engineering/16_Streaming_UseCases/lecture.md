# Streaming use cases

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать streaming модель (модуль 13)
- Знать инструменты streaming (модуль 14)
- Иметь представление о хранении потоковых данных (модуль 15)

**Recommended prior modules:**

- [13_Streaming_Model](../13_Streaming_Model/) — streaming как модель обработки
- [14_Streaming_Tools](../14_Streaming_Tools/) — инструменты streaming
- [15_Streaming_Storage](../15_Streaming_Storage/) — хранение потоковых данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять streaming для event analytics
- Использовать streaming для мониторинга систем
- Проектировать fraud detection системы
- Создавать real-time dashboards

---

## 1. Введение в use cases

Streaming processing подходит для use cases, где критична низкая задержка и обработка в реальном времени.

**Основные use cases:**

- **Event Analytics** — аналитика событий в реальном времени

- **Monitoring** — мониторинг систем и приложений

- **Fraud Detection** — обнаружение мошенничества

- **Real-time Dashboards** — дашборды с live данными

---

## 2. Event Analytics

Event analytics анализирует события пользователей в реальном времени.

### 2.1 Характеристики

**Real-time метрики:**

- События обрабатываются сразу
- Агрегации по окнам
- Live обновления

**Use cases:**

- User behavior tracking
- Product analytics
- A/B testing

**Example: Event Analytics**

```python
class EventAnalytics:
    def __init__(self):
        self.events = []
        self.metrics = {
            "total_events": 0,
            "unique_users": set(),
            "events_by_type": {},
            "revenue": 0.0
        }
    
    def process_event(self, event):
        """Обрабатывает событие в реальном времени"""
        event_type = event.get("type")
        user_id = event.get("user_id")
        
        # Обновление метрик
        self.metrics["total_events"] += 1
        if user_id:
            self.metrics["unique_users"].add(user_id)
        
        if event_type not in self.metrics["events_by_type"]:
            self.metrics["events_by_type"][event_type] = 0
        self.metrics["events_by_type"][event_type] += 1
        
        if "revenue" in event:
            self.metrics["revenue"] += event["revenue"]
        
        self.events.append(event)
        print(f"📊 Событие обработано: {event_type} от user {user_id}")
    
    def get_realtime_stats(self):
        """Возвращает статистику в реальном времени"""
        return {
            "total_events": self.metrics["total_events"],
            "unique_users": len(self.metrics["unique_users"]),
            "events_by_type": self.metrics["events_by_type"].copy(),
            "total_revenue": f"${self.metrics['revenue']:.2f}"
        }

# Использование

analytics = EventAnalytics()

# Обработка событий

analytics.process_event({"type": "page_view", "user_id": 1, "page": "/products"})
analytics.process_event({"type": "purchase", "user_id": 1, "revenue": 99.99})
analytics.process_event({"type": "page_view", "user_id": 2, "page": "/home"})

stats = analytics.get_realtime_stats()
print("\nReal-time Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")
```

**Output:**
```
📊 Событие обработано: page_view от user 1
📊 Событие обработано: purchase от user 1
📊 Событие обработано: page_view от user 2

Real-time Statistics:
  total_events: 3
  unique_users: 2
  events_by_type: {'page_view': 2, 'purchase': 1}
  total_revenue: $99.99
```

---

## 3. Monitoring (Мониторинг)

Streaming используется для мониторинга систем в реальном времени.

### 3.1 Характеристики

**Real-time метрики:**

- Системные метрики
- Application metrics
- Error tracking

**Alerting:**

- Немедленные алерты
- Threshold-based
- Anomaly detection

**Example: System Monitoring**

```python
class SystemMonitor:
    def __init__(self):
        self.metrics = {
            "cpu_usage": [],
            "memory_usage": [],
            "error_rate": 0,
            "requests_per_second": 0
        }
        self.alerts = []
        self.thresholds = {
            "cpu_usage": 80,
            "memory_usage": 90,
            "error_rate": 5
        }
    
    def process_metric(self, metric_name, value, timestamp):
        """Обрабатывает метрику в реальном времени"""
        if metric_name in self.metrics:
            if isinstance(self.metrics[metric_name], list):
                self.metrics[metric_name].append({"value": value, "timestamp": timestamp})
                # Храним только последние 100 значений
                if len(self.metrics[metric_name]) > 100:
                    self.metrics[metric_name] = self.metrics[metric_name][-100:]
            else:
                self.metrics[metric_name] = value
        
        # Проверка thresholds
        self._check_thresholds(metric_name, value)
    
    def _check_thresholds(self, metric_name, value):
        """Проверяет пороги и генерирует алерты"""
        if metric_name in self.thresholds:
            threshold = self.thresholds[metric_name]
            if value > threshold:
                alert = {
                    "metric": metric_name,
                    "value": value,
                    "threshold": threshold,
                    "timestamp": "2024-01-01T10:00:00Z"
                }
                self.alerts.append(alert)
                print(f"⚠️  ALERT: {metric_name} = {value} превышает threshold {threshold}")
    
    def get_current_metrics(self):
        """Возвращает текущие метрики"""
        return {
            "cpu_usage": self.metrics["cpu_usage"][-1]["value"] if self.metrics["cpu_usage"] else 0,
            "memory_usage": self.metrics["memory_usage"][-1]["value"] if self.metrics["memory_usage"] else 0,
            "error_rate": self.metrics["error_rate"],
            "requests_per_second": self.metrics["requests_per_second"],
            "active_alerts": len(self.alerts)
        }

# Использование

monitor = SystemMonitor()

# Обработка метрик

monitor.process_metric("cpu_usage", 75, "2024-01-01T10:00:00Z")
monitor.process_metric("cpu_usage", 85, "2024-01-01T10:01:00Z")  # Превышение threshold
monitor.process_metric("memory_usage", 95, "2024-01-01T10:02:00Z")  # Превышение threshold

current = monitor.get_current_metrics()
print("\nТекущие метрики:")
for key, value in current.items():
    print(f"  {key}: {value}")
```

**Output:**
```
⚠️  ALERT: cpu_usage = 85 превышает threshold 80
⚠️  ALERT: memory_usage = 95 превышает threshold 90

Текущие метрики:
  cpu_usage: 85
  memory_usage: 95
  error_rate: 0
  requests_per_second: 0
  active_alerts: 2
```

---

## 4. Fraud Detection (Обнаружение мошенничества)

Fraud detection требует обработки в реальном времени для быстрого обнаружения подозрительной активности.

### 4.1 Характеристики

**Real-time анализ:**

- Анализ транзакций сразу
- Pattern detection
- Anomaly detection

**Low latency:**

- Быстрое обнаружение
- Блокировка подозрительных операций
- Минимизация потерь

**Example: Fraud Detection**

```python
class FraudDetection:
    def __init__(self):
        self.user_profiles = {}
        self.suspicious_patterns = []
    
    def analyze_transaction(self, transaction):
        """Анализирует транзакцию в реальном времени"""
        user_id = transaction.get("user_id")
        amount = transaction.get("amount", 0)
        location = transaction.get("location")
        timestamp = transaction.get("timestamp")
        
        risk_score = 0
        flags = []
        
        # Проверка 1: Необычно большая сумма
        if amount > 10000:
            risk_score += 30
            flags.append("high_amount")
        
        # Проверка 2: Необычное местоположение
        if user_id in self.user_profiles:
            usual_location = self.user_profiles[user_id].get("usual_location")
            if usual_location and location != usual_location:
                risk_score += 40
                flags.append("unusual_location")
        
        # Проверка 3: Частота транзакций
        if user_id in self.user_profiles:
            recent_transactions = self.user_profiles[user_id].get("recent_count", 0)
            if recent_transactions > 10:
                risk_score += 30
                flags.append("high_frequency")
        
        # Обновление профиля
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {}
        self.user_profiles[user_id]["usual_location"] = location
        self.user_profiles[user_id]["recent_count"] = self.user_profiles[user_id].get("recent_count", 0) + 1
        
        # Решение
        is_fraud = risk_score >= 70
        
        if is_fraud:
            self.suspicious_patterns.append({
                "transaction": transaction,
                "risk_score": risk_score,
                "flags": flags
            })
            print(f"🚨 FRAUD DETECTED: Transaction {transaction.get('id')}, Risk Score: {risk_score}, Flags: {flags}")
        else:
            print(f"✅ Transaction {transaction.get('id')} approved, Risk Score: {risk_score}")
        
        return {"is_fraud": is_fraud, "risk_score": risk_score, "flags": flags}

# Использование

fraud_detector = FraudDetection()

# Нормальная транзакция

fraud_detector.analyze_transaction({
    "id": "tx_001",
    "user_id": 1,
    "amount": 100,
    "location": "Moscow",
    "timestamp": "2024-01-01T10:00:00Z"
})

# Подозрительная транзакция

fraud_detector.analyze_transaction({
    "id": "tx_002",
    "user_id": 1,
    "amount": 15000,  # Большая сумма
    "location": "New York",  # Необычное местоположение
    "timestamp": "2024-01-01T10:01:00Z"
})
```

**Output:**
```
✅ Transaction tx_001 approved, Risk Score: 0
🚨 FRAUD DETECTED: Transaction tx_002, Risk Score: 70, Flags: ['high_amount', 'unusual_location']
```

---

## 5. Real-time Dashboards

Real-time dashboards отображают данные, обновляющиеся в реальном времени.

### 5.1 Характеристики

**Live обновления:**

- Данные обновляются автоматически
- Нет необходимости обновлять страницу
- WebSocket или Server-Sent Events

**Streaming источники:**

- События из Kafka
- Метрики из систем
- Агрегации в реальном времени

**Example: Real-time Dashboard**

```python
class RealTimeDashboard:
    def __init__(self):
        self.widgets = {}
        self.update_callbacks = []
    
    def add_widget(self, widget_id, widget_type, data_source):
        """Добавляет виджет на дашборд"""
        self.widgets[widget_id] = {
            "type": widget_type,
            "data_source": data_source,
            "data": None,
            "last_updated": None
        }
        print(f"✅ Виджет '{widget_id}' добавлен: {widget_type}")
    
    def update_widget(self, widget_id, new_data):
        """Обновляет виджет новыми данными"""
        if widget_id in self.widgets:
            self.widgets[widget_id]["data"] = new_data
            self.widgets[widget_id]["last_updated"] = "2024-01-01T10:00:00Z"
            print(f"🔄 Виджет '{widget_id}' обновлён")
            
            # Вызов callbacks для real-time обновления
            for callback in self.update_callbacks:
                callback(widget_id, new_data)
    
    def get_dashboard_data(self):
        """Возвращает данные для дашборда"""
        dashboard = {}
        for widget_id, widget in self.widgets.items():
            dashboard[widget_id] = {
                "type": widget["type"],
                "data": widget["data"],
                "last_updated": widget["last_updated"]
            }
        return dashboard
    
    def register_update_callback(self, callback):
        """Регистрирует callback для обновлений"""
        self.update_callbacks.append(callback)

# Использование

dashboard = RealTimeDashboard()

# Добавление виджетов

dashboard.add_widget("revenue", "metric", "kafka://revenue-events")
dashboard.add_widget("users_online", "counter", "kafka://user-events")
dashboard.add_widget("top_products", "table", "kafka://product-events")

# Обновление виджетов (симуляция streaming)

dashboard.update_widget("revenue", {"value": 50000, "trend": "+5%"})
dashboard.update_widget("users_online", {"count": 1250})
dashboard.update_widget("top_products", [
    {"product": "Laptop", "sales": 150},
    {"product": "Mouse", "sales": 200}
])

# Данные дашборда

dashboard_data = dashboard.get_dashboard_data()
print("\nReal-time Dashboard Data:")
for widget_id, widget in dashboard_data.items():
    print(f"  {widget_id}: {widget['data']}")
```

**Output:**
```
✅ Виджет 'revenue' добавлен: metric
✅ Виджет 'users_online' добавлен: counter
✅ Виджет 'top_products' добавлен: table
🔄 Виджет 'revenue' обновлён
🔄 Виджет 'users_online' обновлён
🔄 Виджет 'top_products' обновлён

Real-time Dashboard Data:
  revenue: {'value': 50000, 'trend': '+5%'}
  users_online: {'count': 1250}
  top_products: [{'product': 'Laptop', 'sales': 150}, {'product': 'Mouse', 'sales': 200}]
```

---

## 6. IoT и Sensor Data

IoT устройства генерируют огромные объёмы данных, требующих streaming обработки.

### 6.1 Характеристики IoT Streaming

**Высокий объём:**

- Миллионы устройств
- Непрерывный поток данных
- Высокая частота событий

**Real-time обработка:**

- Немедленная обработка
- Агрегация данных
- Алерты на аномалии

**Example: IoT Data Processing**

```python
class IoTStreamProcessor:
    def __init__(self):
        self.devices = {}
        self.aggregations = {}
        self.alerts = []
    
    def process_sensor_data(self, device_id, sensor_type, value, timestamp):
        """Обрабатывает данные сенсора в реальном времени"""
        if device_id not in self.devices:
            self.devices[device_id] = {}
        
        if sensor_type not in self.devices[device_id]:
            self.devices[device_id][sensor_type] = []
        
        data_point = {
            "value": value,
            "timestamp": timestamp
        }
        
        self.devices[device_id][sensor_type].append(data_point)
        
        # Агрегация
        self._aggregate(device_id, sensor_type, value)
        
        # Проверка аномалий
        self._check_anomalies(device_id, sensor_type, value)
        
        print(f"📡 Обработано: device={device_id}, sensor={sensor_type}, value={value}")
    
    def _aggregate(self, device_id, sensor_type, value):
        """Агрегирует данные"""
        key = f"{device_id}:{sensor_type}"
        if key not in self.aggregations:
            self.aggregations[key] = {
                "count": 0,
                "sum": 0,
                "min": float('inf'),
                "max": float('-inf')
            }
        
        agg = self.aggregations[key]
        agg["count"] += 1
        agg["sum"] += value
        agg["min"] = min(agg["min"], value)
        agg["max"] = max(agg["max"], value)
    
    def _check_anomalies(self, device_id, sensor_type, value):
        """Проверяет аномалии"""
        threshold = 100  # Пример порога
        if value > threshold:
            alert = {
                "device_id": device_id,
                "sensor_type": sensor_type,
                "value": value,
                "threshold": threshold
            }
            self.alerts.append(alert)
            print(f"⚠️  ALERT: {device_id}/{sensor_type} = {value} превышает {threshold}")

# Использование

processor = IoTStreamProcessor()

# Обработка данных с разных устройств

processor.process_sensor_data("device_1", "temperature", 25, "2024-01-01T10:00:00Z")
processor.process_sensor_data("device_1", "temperature", 105, "2024-01-01T10:01:00Z")  # Аномалия
processor.process_sensor_data("device_2", "humidity", 60, "2024-01-01T10:00:00Z")

print(f"\nАгрегации: {len(processor.aggregations)}")
print(f"Алертов: {len(processor.alerts)}")
```

**Output:**
```
📡 Обработано: device=device_1, sensor=temperature, value=25
📡 Обработано: device=device_1, sensor=temperature, value=105
⚠️  ALERT: device_1/temperature = 105 превышает 100
📡 Обработано: device=device_2, sensor=humidity, value=60

Агрегации: 2
Алертов: 1
```

---

## 7. Сравнение Use Cases

Различные use cases имеют разные требования к streaming.

### 7.1 Требования

| Use Case | Latency | Throughput | Complexity |
|----------|---------|------------|------------|
| **Event Analytics** | Средняя (секунды) | Высокая | Средняя |
| **Monitoring** | Низкая (миллисекунды) | Средняя | Низкая |
| **Fraud Detection** | Очень низкая (миллисекунды) | Высокая | Высокая |
| **Real-time Dashboards** | Низкая (секунды) | Средняя | Низкая |
| **IoT/Sensor Data** | Низкая (секунды) | Очень высокая | Средняя |

### 7.2 Выбор Use Case

**Example: Выбор подходящего use case**

```python
def recommend_use_case(requirements):
    """Рекомендует use case на основе требований"""
    if requirements.get("low_latency") and requirements.get("high_throughput") and requirements.get("fraud"):
        return "Fraud Detection (очень низкая задержка, высокая пропускная способность)"
    elif requirements.get("monitoring") and requirements.get("alerts"):
        return "Monitoring (низкая задержка, алерты)"
    elif requirements.get("analytics") and requirements.get("aggregations"):
        return "Event Analytics (агрегации, аналитика)"
    elif requirements.get("visualization") and requirements.get("dashboards"):
        return "Real-time Dashboards (визуализация, live обновления)"
    elif requirements.get("iot") and requirements.get("high_volume"):
        return "IoT/Sensor Data (высокий объём, агрегация)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"low_latency": True, "high_throughput": True, "fraud": True},
    {"monitoring": True, "alerts": True, "system_metrics": True},
    {"iot": True, "high_volume": True, "aggregations": True}
]

print("Рекомендации use cases:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_use_case(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```
Рекомендации use cases:
  Пример 1: Fraud Detection (очень низкая задержка, высокая пропускная способность)
  Пример 2: Monitoring (низкая задержка, алерты)
  Пример 3: IoT/Sensor Data (высокий объём, агрегация)
```

---

## 💡 Key Takeaways

- **Event Analytics**: Аналитика событий в реальном времени. Агрегации по окнам, live обновления метрик.

- **Monitoring**: Мониторинг систем в реальном времени. Real-time метрики, немедленные алерты при превышении порогов.

- **Fraud Detection**: Обнаружение мошенничества требует очень низкой задержки. Pattern detection, anomaly detection в реальном времени.

- **Real-time Dashboards**: Дашборды с live обновлениями. WebSocket или Server-Sent Events для передачи данных.

- **IoT и Sensor Data**: Обработка данных от IoT устройств требует высокой пропускной способности. Агрегация и обнаружение аномалий в реальном времени.

- **Выбор use case**: Требования к задержке, пропускной способности и сложности различаются для разных use cases. Правильный выбор критичен для успеха системы.

---

## 🚀 Next Steps

**Related Modules:**

- [17_Data_Platform_Architectures](../17_Data_Platform_Architectures/) — архитектуры data-платформ
- [19_Reliability_Operations](../19_Reliability_Operations/) — надёжность и эксплуатация
- [13_Streaming_Model](../13_Streaming_Model/) — streaming модель

**Practice Ideas:**

1. Создайте простую систему мониторинга: метрики и алерты в реальном времени
2. Реализуйте fraud detection: анализ транзакций с risk scoring
3. Постройте real-time dashboard: виджеты с live обновлениями

**Going Deeper:**

- Изучите anomaly detection: алгоритмы для обнаружения аномалий
- Погрузитесь в real-time ML: модели для streaming данных
- Изучите CEP (Complex Event Processing): обработка сложных событий

---

## 📚 Additional Resources

**Books:**

- "Streaming Systems" by Tyler Akidau — use cases streaming
- "Designing Data-Intensive Applications" — real-time systems

**Articles:**

- "Real-time Analytics Use Cases" — примеры использования
- "Fraud Detection with Streaming" — практические подходы

**Documentation:**

- Apache Flink: https://flink.apache.org/docs/ (streaming use cases)
- Kafka Streams: https://kafka.apache.org/documentation/streams/ (event processing)

---




