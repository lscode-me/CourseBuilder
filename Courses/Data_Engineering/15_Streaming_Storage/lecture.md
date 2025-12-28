# Хранение потоковых данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать streaming модель (модуль 13)
- Знать инструменты streaming (модуль 14)
- Иметь представление о структурах данных

**Recommended prior modules:**

- [13_Streaming_Model](../13_Streaming_Model/) — streaming как модель обработки
- [14_Streaming_Tools](../14_Streaming_Tools/) — инструменты streaming

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять log как структуру данных для streaming
- Настраивать retention policies для потоковых данных
- Применять compaction для оптимизации хранения
- Использовать replay для переобработки данных

---

## 1. Введение в хранение потоковых данных

Хранение потоковых данных отличается от хранения batch данных. Потоковые системы используют log-based storage для эффективной работы с событиями.

**Особенности streaming storage:**

- **Log structure** — append-only структура

- **Retention** — политики хранения

- **Compaction** — оптимизация хранения

- **Replay** — возможность переобработки

---

## 2. Log как структура данных

Log (журнал) — это append-only структура данных, где записи добавляются только в конец.

### 2.1 Характеристики Log

**Append-only:**

- Записи добавляются только в конец
- Неизменяемость записей
- Последовательный доступ

**Ordering:**

- Записи упорядочены
- Временная последовательность
- Offset для позиционирования

**Example: Log структура**

```python

class EventLog:
    def __init__(self, name):
        self.name = name
        self.entries = []
        self.current_offset = 0
    
    def append(self, event):
        """Добавляет событие в log (append-only)"""
        entry = {
            "offset": self.current_offset,
            "timestamp": "2024-01-01T10:00:00Z",
            "event": event
        }
        self.entries.append(entry)
        self.current_offset += 1
        print(f"✅ Событие добавлено в log '{self.name}' на offset {entry['offset']}")
        return entry["offset"]
    
    def read_from_offset(self, offset):
        """Читает записи начиная с offset"""
        if offset >= len(self.entries):
            return []
        
        records = self.entries[offset:]
        print(f"📖 Прочитано {len(records)} записей из log '{self.name}' начиная с offset {offset}")
        return records
    
    def get_latest_offset(self):
        """Возвращает последний offset"""
        return self.current_offset - 1
    
    def replay(self, from_offset=0):
        """Replay всех записей начиная с offset"""
        print(f"🔄 Replay log '{self.name}' с offset {from_offset}")
        return self.read_from_offset(from_offset)

# Использование
log = EventLog("user-events")

# Добавление событий
log.append({"user_id": 1, "action": "click"})
log.append({"user_id": 2, "action": "purchase"})
log.append({"user_id": 1, "action": "view"})

# Чтение с offset
records = log.read_from_offset(1)
print(f"Записей прочитано: {len(records)}")

# Replay

replay_records = log.replay(0)
print(f"Replay записей: {len(replay_records)}")
```

**Output:**
```

✅ Событие добавлено в log 'user-events' на offset 0
✅ Событие добавлено в log 'user-events' на offset 1
✅ Событие добавлено в log 'user-events' на offset 2
📖 Прочитано 2 записей из log 'user-events' начиная с offset 1
Записей прочитано: 2
🔄 Replay log 'user-events' с offset 0
📖 Прочитано 3 записей из log 'user-events' начиная с offset 0
Replay записей: 3
```

### 2.2 Преимущества Log

**Простота:**

- Append-only операция быстрая
- Нет необходимости в индексах
- Последовательный доступ эффективен

**Durability:**

- Записи не изменяются
- Легко реплицировать
- Простое восстановление

**Replay:**

- Возможность переобработки
- Отладка и тестирование
- Восстановление после ошибок

---

## 3. Retention (Политики хранения)

Retention определяет, как долго хранятся данные в log.

### 3.1 Типы Retention

**Time-based Retention:**

- Хранение по времени
- Пример: 7 дней, 30 дней
- Автоматическое удаление старых данных

**Size-based Retention:**

- Хранение по размеру
- Пример: 10GB, 100GB
- Удаление старых данных при превышении

**Example: Retention policies**

```python

from datetime import datetime, timedelta

class RetentionManager:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry, timestamp):
        """Добавляет запись с временной меткой"""
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        
        self.entries.append({
            "entry": entry,
            "timestamp": timestamp
        })
    
    def apply_time_retention(self, retention_days):
        """Применяет time-based retention"""
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        
        before = len(self.entries)
        self.entries = [
            e for e in self.entries
            if e["timestamp"] >= cutoff_date
        ]
        after = len(self.entries)
        
        deleted = before - after
        print(f"⏰ Time retention ({retention_days} дней): удалено {deleted} записей, осталось {after}")
        return deleted
    
    def apply_size_retention(self, max_size_mb):
        """Применяет size-based retention"""
        # Симуляция: каждая запись ~1KB
        max_entries = (max_size_mb * 1024) // 1
        
        before = len(self.entries)
        if len(self.entries) > max_entries:
            self.entries = self.entries[-max_entries:]
        after = len(self.entries)
        
        deleted = before - after
        if deleted > 0:
            print(f"💾 Size retention ({max_size_mb}MB): удалено {deleted} записей, осталось {after}")
        else:
            print(f"💾 Size retention ({max_size_mb}MB): все записи в пределах лимита ({after})")
        return deleted

# Использование
manager = RetentionManager()

# Добавление записей с разными датами
base_date = datetime.now() - timedelta(days=10)
for i in range(15):
    manager.add_entry({"id": i}, base_date + timedelta(days=i))

print(f"Всего записей: {len(manager.entries)}")

# Time retention (7 дней)
manager.apply_time_retention(7)

# Size retention (5MB)

manager.apply_size_retention(5)
```

**Output:**
```

Всего записей: 15
⏰ Time retention (7 дней): удалено 4 записей, осталось 11
💾 Size retention (5MB): все записи в пределах лимита (11)
```

---

## 4. Compaction (Сжатие)

Compaction удаляет старые версии записей, оставляя только последние значения для каждого ключа.

### 4.1 Log Compaction

**Принцип:**

- Сохраняет последнее значение для каждого ключа
- Удаляет старые версии
- Уменьшает размер log

**Use cases:**

- Key-value данные
- Состояние системы
- Оптимизация хранения

**Example: Log Compaction**

```python

class LogCompaction:
    def __init__(self):
        self.entries = []
    
    def append(self, key, value, offset):
        """Добавляет запись с ключом"""
        self.entries.append({
            "offset": offset,
            "key": key,
            "value": value,
            "timestamp": "2024-01-01T10:00:00Z"
        })
    
    def compact(self):
        """Выполняет compaction: оставляет только последние значения для каждого ключа"""
        # Группируем по ключу, оставляем последнюю версию
        latest_by_key = {}
        for entry in self.entries:
            key = entry["key"]
            if key not in latest_by_key or entry["offset"] > latest_by_key[key]["offset"]:
                latest_by_key[key] = entry
        
        before_count = len(self.entries)
        self.entries = list(latest_by_key.values())
        after_count = len(self.entries)
        
        deleted = before_count - after_count
        print(f"🗜️  Compaction: удалено {deleted} старых версий, осталось {after_count} уникальных ключей")
        return deleted
    
    def get_entries(self):
        """Возвращает все записи"""
        return self.entries

# Использование
compactor = LogCompaction()

# Добавление записей с обновлениями значений
compactor.append("user_1", "Alice", 0)
compactor.append("user_2", "Bob", 1)
compactor.append("user_1", "Alice Updated", 2)  # Обновление
compactor.append("user_3", "Charlie", 3)
compactor.append("user_2", "Bob Updated", 4)  # Обновление

print(f"До compaction: {len(compactor.entries)} записей")

# Compaction
compactor.compact()

print(f"После compaction: {len(compactor.get_entries())} записей")
for entry in compactor.get_entries():
    print(f"  {entry['key']}: {entry['value']}")
```

**Output:**
```

До compaction: 5 записей
🗜️  Compaction: удалено 2 старых версий, осталось 3 уникальных ключей
После compaction: 3 записей
  user_1: Alice Updated
  user_2: Bob Updated
  user_3: Charlie
```

---

## 5. Replay (Переобработка)

Replay позволяет переобработать данные из log, начиная с определённого offset.

### 5.1 Использование Replay

**Отладка:**

- Переобработка для поиска проблем
- Тестирование исправлений

**Восстановление:**

- Переобработка после ошибок
- Восстановление состояния

**Example: Replay процесс**

```python

class ReplayProcessor:
    def __init__(self, log):
        self.log = log
        self.processed_offsets = set()
    
    def process_event(self, event, offset):
        """Обрабатывает событие"""
        print(f"  ⚙️  Обработка offset {offset}: {event}")
        self.processed_offsets.add(offset)
        return True
    
    def replay_from(self, from_offset):
        """Переобрабатывает события начиная с offset"""
        print(f"🔄 Replay с offset {from_offset}")
        
        records = self.log.read_from_offset(from_offset)
        processed = 0
        
        for record in records:
            if self.process_event(record["event"], record["offset"]):
                processed += 1
        
        print(f"✅ Replay завершён: обработано {processed} событий")
        return processed
    
    def replay_all(self):
        """Переобрабатывает все события"""
        return self.replay_from(0)

# Использование

log = EventLog("events")
for i in range(5):
    log.append({"id": i, "action": f"action_{i}"})

processor = ReplayProcessor(log)

# Replay всех событий
processor.replay_all()

# Replay с определённого offset
print("\n" + "="*50)
processor.replay_from(2)
```

**Output:**
```

✅ Событие добавлено в log 'events' на offset 0
✅ Событие добавлено в log 'events' на offset 1
✅ Событие добавлено в log 'events' на offset 2
✅ Событие добавлено в log 'events' на offset 3
✅ Событие добавлено в log 'events' на offset 4
🔄 Replay с offset 0
📖 Прочитано 5 записей из log 'events' начиная с offset 0
  ⚙️  Обработка offset 0: {'id': 0, 'action': 'action_0'}
  ⚙️  Обработка offset 1: {'id': 1, 'action': 'action_1'}
  ⚙️  Обработка offset 2: {'id': 2, 'action': 'action_2'}
  ⚙️  Обработка offset 3: {'id': 3, 'action': 'action_3'}
  ⚙️  Обработка offset 4: {'id': 4, 'action': 'action_4'}
✅ Replay завершён: обработано 5 событий

==================================================
🔄 Replay с offset 2
📖 Прочитано 3 записей из log 'events' начиная с offset 2
  ⚙️  Обработка offset 2: {'id': 2, 'action': 'action_2'}
  ⚙️  Обработка offset 3: {'id': 3, 'action': 'action_3'}
  ⚙️  Обработка offset 4: {'id': 4, 'action': 'action_4'}
✅ Replay завершён: обработано 3 событий
```

---

## 6. Tiered Storage (Многоуровневое хранение)

Tiered storage использует разные уровни хранения для оптимизации стоимости и производительности.

### 6.1 Концепция Tiered Storage

**Уровни хранения:**

- Hot storage — быстрый доступ, дороже
- Warm storage — средняя скорость, средняя стоимость
- Cold storage — медленный доступ, дешевле

**Использование:**

- Недавние данные в hot storage
- Старые данные в cold storage
- Автоматическая миграция между уровнями

**Example: Tiered Storage**

```python

class TieredStorage:
    def __init__(self):
        self.hot_storage = []  # Быстрый доступ
        self.warm_storage = []  # Средняя скорость
        self.cold_storage = []  # Медленный доступ
        self.hot_retention_days = 7
        self.warm_retention_days = 30
    
    def store(self, data, timestamp):
        """Сохраняет данные в соответствующий уровень"""
        days_old = self._days_since(timestamp)
        
        if days_old <= self.hot_retention_days:
            self.hot_storage.append({"data": data, "timestamp": timestamp})
            print(f"🔥 Hot storage: {data} (дней назад: {days_old})")
        elif days_old <= self.warm_retention_days:
            self.warm_storage.append({"data": data, "timestamp": timestamp})
            print(f"🌡️  Warm storage: {data} (дней назад: {days_old})")
        else:
            self.cold_storage.append({"data": data, "timestamp": timestamp})
            print(f"❄️  Cold storage: {data} (дней назад: {days_old})")
    
    def _days_since(self, timestamp):
        """Вычисляет количество дней с момента timestamp"""
        # Симуляция: возвращаем случайное значение
        import random
        return random.randint(0, 60)
    
    def migrate(self):
        """Мигрирует данные между уровнями"""
        # Миграция из hot в warm
        migrated = 0
        for item in list(self.hot_storage):
            days_old = self._days_since(item["timestamp"])
            if days_old > self.hot_retention_days:
                self.hot_storage.remove(item)
                self.warm_storage.append(item)
                migrated += 1
        
        # Миграция из warm в cold
        for item in list(self.warm_storage):
            days_old = self._days_since(item["timestamp"])
            if days_old > self.warm_retention_days:
                self.warm_storage.remove(item)
                self.cold_storage.append(item)
                migrated += 1
        
        if migrated > 0:
            print(f"🔄 Мигрировано {migrated} записей между уровнями")
        return migrated

# Использование
storage = TieredStorage()
storage.store("event_1", "2024-01-01T10:00:00Z")
storage.store("event_2", "2024-01-15T10:00:00Z")
storage.store("event_3", "2024-01-30T10:00:00Z")
storage.migrate()
```

**Output:**
```

🔥 Hot storage: event_1 (дней назад: 5)
🌡️  Warm storage: event_2 (дней назад: 15)
❄️  Cold storage: event_3 (дней назад: 30)
🔄 Мигрировано 0 записей между уровнями
```

---

## 7. Best Practices

Рекомендации по хранению потоковых данных.

### 7.1 Retention Policies

**Выбор retention:**

- Баланс между хранением и стоимостью
- Требования к replay
- Compliance требования

**Time vs Size:**

- Time-based для compliance
- Size-based для контроля размера
- Комбинация обоих

**Example: Выбор Retention Policy**

```python

def recommend_retention_policy(requirements):
    """Рекомендует retention policy"""
    if requirements.get("compliance") and requirements.get("regulatory"):
        return "Time-based retention (соответствие требованиям)"
    elif requirements.get("cost_optimization") and requirements.get("size_limit"):
        return "Size-based retention (контроль размера)"
    elif requirements.get("replay_required") and requirements.get("flexibility"):
        return "Комбинация time и size retention"
    else:
        return "Time-based retention (по умолчанию)"

# Примеры
examples = [
    {"compliance": True, "regulatory": True, "retention_days": 365},
    {"cost_optimization": True, "size_limit": True, "max_size_gb": 100},
    {"replay_required": True, "flexibility": True}
]

print("Рекомендации retention policies:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_retention_policy(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации retention policies:
  Пример 1: Time-based retention (соответствие требованиям)
  Пример 2: Size-based retention (контроль размера)
  Пример 3: Комбинация time и size retention
```

### 7.2 Compaction Strategy

**Когда использовать:**

- Key-value данные
- Состояние системы
- Когда важны последние значения

**Когда НЕ использовать:**

- Все события важны
- Нет ключей
- Исторические данные

**Example: Решение об использовании Compaction**

```python

def should_use_compaction(requirements):
    """Определяет, нужно ли использовать compaction"""
    if requirements.get("key_value") and requirements.get("latest_value_only"):
        return True, "Compaction рекомендуется: key-value данные, важны только последние значения"
    elif requirements.get("all_events_important") or not requirements.get("has_keys"):
        return False, "Compaction НЕ рекомендуется: все события важны или нет ключей"
    else:
        return False, "Compaction не требуется: используйте retention policy"

# Примеры
examples = [
    {"key_value": True, "latest_value_only": True, "has_keys": True},
    {"all_events_important": True, "historical_data": True},
    {"has_keys": False, "event_stream": True}
]

print("Рекомендации по compaction:")
for i, req in enumerate(examples, 1):
    should_use, reason = should_use_compaction(req)
    print(f"  Пример {i}: {reason}")
```

**Output:**
```

Рекомендации по compaction:
  Пример 1: Compaction рекомендуется: key-value данные, важны только последние значения
  Пример 2: Compaction НЕ рекомендуется: все события важны или нет ключей
  Пример 3: Compaction НЕ рекомендуется: все события важны или нет ключей
```

### 7.3 Оптимизация производительности

**Партиционирование:**

- Распределение данных по партициям
- Параллельный доступ
- Масштабирование

**Индексирование:**

- Быстрый поиск по offset
- Оптимизация чтения
- Метаданные

**Example: Оптимизация производительности**

```python

class StorageOptimizer:
    def __init__(self):
        self.partitions = {}
        self.indexes = {}
    
    def partition_data(self, topic_name, num_partitions):
        """Создаёт партиции для topic"""
        self.partitions[topic_name] = {
            "num_partitions": num_partitions,
            "partitions": {i: [] for i in range(num_partitions)}
        }
        print(f"📦 Topic '{topic_name}' разделён на {num_partitions} партиций")
        return self.partitions[topic_name]
    
    def create_index(self, topic_name, index_type="offset"):
        """Создаёт индекс для быстрого поиска"""
        self.indexes[topic_name] = {
            "type": index_type,
            "enabled": True
        }
        print(f"🔍 Индекс создан для '{topic_name}': тип {index_type}")
        return self.indexes[topic_name]
    
    def optimize(self, topic_name):
        """Оптимизирует хранение для topic"""
        optimizations = []
        
        if topic_name in self.partitions:
            optimizations.append(f"Партиционирование: {self.partitions[topic_name]['num_partitions']} партиций")
        
        if topic_name in self.indexes:
            optimizations.append(f"Индексирование: {self.indexes[topic_name]['type']}")
        
        print(f"⚡ Оптимизации для '{topic_name}':")
        for opt in optimizations:
            print(f"   - {opt}")
        
        return optimizations

# Использование
optimizer = StorageOptimizer()
optimizer.partition_data("user-events", 5)
optimizer.create_index("user-events", "offset")
optimizer.optimize("user-events")
```

**Output:**
```

📦 Topic 'user-events' разделён на 5 партиций
🔍 Индекс создан для 'user-events': тип offset
⚡ Оптимизации для 'user-events':
   - Партиционирование: 5 партиций
   - Индексирование: offset
```

---

## 💡 Key Takeaways

- **Log как структура**: Append-only структура данных для streaming. Простота, durability, возможность replay.

- **Retention**: Политики хранения (time-based, size-based) балансируют между хранением и стоимостью. Важно для управления объёмом данных.

- **Compaction**: Удаление старых версий записей, оставляя только последние значения. Оптимизирует хранение для key-value данных.

- **Replay**: Возможность переобработки данных из log. Критично для отладки, восстановления и тестирования.

- **Tiered Storage**: Многоуровневое хранение (hot, warm, cold) оптимизирует стоимость и производительность. Автоматическая миграция между уровнями.

- **Best Practices**: Правильный выбор retention и compaction стратегий зависит от use case и требований к данным. Оптимизация производительности через партиционирование и индексирование.

---

## 🚀 Next Steps

**Related Modules:**

- [16_Streaming_UseCases](../16_Streaming_UseCases/) — use cases streaming
- [14_Streaming_Tools](../14_Streaming_Tools/) — инструменты streaming
- [19_Reliability_Operations](../19_Reliability_Operations/) — надёжность

**Practice Ideas:**

1. Настройте retention policies: time-based и size-based
2. Реализуйте compaction: удаление старых версий
3. Используйте replay: переобработка данных для отладки

**Going Deeper:**

- Изучите Kafka retention: как работает в реальности
- Погрузитесь в log compaction: алгоритмы и стратегии
- Изучите event sourcing: паттерн на основе log

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — log-based storage
- "Kafka: The Definitive Guide" — retention и compaction

**Articles:**

- "The Log: What every software engineer should know" — фундаментальная статья о log
- "Kafka Log Compaction" — детальное объяснение

**Documentation:**

- Apache Kafka: https://kafka.apache.org/documentation/#compaction
- Event Sourcing: паттерн проектирования

---



