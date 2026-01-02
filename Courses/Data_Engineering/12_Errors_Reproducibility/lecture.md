# Ошибки и воспроизводимость

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать batch processing (модуль 09)
- Знать качество данных (модуль 11)
- Иметь представление о версионировании

**Recommended prior modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing
- [11_Data_Quality](../11_Data_Quality/) — качество данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Обрабатывать ошибки в pipelines с retry механизмами
- Выполнять backfills для переобработки данных
- Версионировать данные и схемы
- Создавать воспроизводимые pipelines

---

## 1. Введение в обработку ошибок

Ошибки в data pipelines неизбежны. Правильная обработка ошибок критична для надёжности системы.

**Типы ошибок:**

- **Transient errors** — временные (сеть, таймауты)

- **Permanent errors** — постоянные (невалидные данные, схема)

- **System errors** — системные (недостаток ресурсов)

---

## 2. Retries (Повторные попытки)

Retry механизмы позволяют автоматически повторять операции при временных ошибках.

### 2.1 Стратегии Retry

**Exponential Backoff:**

- Увеличение задержки между попытками
- Пример: 1s, 2s, 4s, 8s

**Fixed Delay:**

- Постоянная задержка
- Пример: 5s между попытками

**Max Retries:**

- Ограничение количества попыток
- Предотвращение бесконечных циклов

**Example: Retry механизм**

```python
import time
import random

class RetryHandler:
    def __init__(self, max_retries=3, strategy="exponential"):
        self.max_retries = max_retries
        self.strategy = strategy
    
    def exponential_backoff(self, attempt):
        """Exponential backoff: 2^attempt секунд"""
        delay = 2 ** attempt
        return delay
    
    def fixed_delay(self, attempt):
        """Fixed delay: постоянная задержка"""
        return 5
    
    def execute_with_retry(self, operation, *args, **kwargs):
        """Выполняет операцию с retry"""
        last_error = None
        
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"🔄 Попытка {attempt}/{self.max_retries}")
                result = operation(*args, **kwargs)
                print("✅ Операция выполнена успешно")
                return result
            except Exception as e:
                last_error = e
                print(f"❌ Ошибка: {e}")
                
                if attempt < self.max_retries:
                    if self.strategy == "exponential":
                        delay = self.exponential_backoff(attempt)
                    else:
                        delay = self.fixed_delay(attempt)
                    
                    print(f"⏳ Повтор через {delay} секунд...")
                    time.sleep(delay)
                else:
                    print(f"❌ Все попытки исчерпаны")
        
        raise last_error

# Симуляция операции с временными ошибками

def unreliable_operation():
    """Операция, которая может временно падать"""
    if random.random() < 0.7:  # 70% вероятность ошибки
        raise ConnectionError("Временная ошибка сети")
    return "Успех"

# Использование

handler = RetryHandler(max_retries=3, strategy="exponential")
try:
    result = handler.execute_with_retry(unreliable_operation)
    print(f"Результат: {result}")
except Exception as e:
    print(f"Финальная ошибка: {e}")
```

**Output:**
```
🔄 Попытка 1/3
❌ Ошибка: Временная ошибка сети
⏳ Повтор через 2 секунды...
🔄 Попытка 2/3
❌ Ошибка: Временная ошибка сети
⏳ Повтор через 4 секунды...
🔄 Попытка 3/3
✅ Операция выполнена успешно
Результат: Успех
```

---

## 3. Backfills (Переобработка данных)

Backfill — это переобработка исторических данных, обычно после исправления ошибок или изменений в логике.

### 3.1 Стратегии Backfill

**Full Backfill:**

- Переобработка всех данных
- Для критических исправлений

**Incremental Backfill:**

- Переобработка только изменённых периодов
- Более эффективно

**Example: Backfill процесс**

```python
class BackfillManager:
    def __init__(self):
        self.processed_dates = set()
    
    def backfill_date_range(self, start_date, end_date, pipeline):
        """Выполняет backfill для диапазона дат"""
        from datetime import datetime, timedelta
        
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date)
        if isinstance(end_date, str):
            end_date = datetime.fromisoformat(end_date)
        
        current_date = start_date
        total_days = (end_date - start_date).days + 1
        
        print(f"🔄 Backfill: {start_date.date()} до {end_date.date()} ({total_days} дней)")
        
        processed = 0
        failed = 0
        
        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            try:
                print(f"  Обработка {date_str}...")
                pipeline.run(date_str)
                self.processed_dates.add(date_str)
                processed += 1
            except Exception as e:
                print(f"  ❌ Ошибка для {date_str}: {e}")
                failed += 1
            
            current_date += timedelta(days=1)
        
        print(f"\n✅ Backfill завершён: {processed} успешно, {failed} ошибок")
        return {"processed": processed, "failed": failed}
    
    def incremental_backfill(self, dates, pipeline):
        """Инкрементальный backfill для списка дат"""
        print(f"🔄 Инкрементальный backfill: {len(dates)} дат")
        
        for date in dates:
            if date not in self.processed_dates:
                try:
                    pipeline.run(date)
                    self.processed_dates.add(date)
                    print(f"  ✅ {date} обработана")
                except Exception as e:
                    print(f"  ❌ Ошибка для {date}: {e}")
            else:
                print(f"  ⏭️  {date} уже обработана, пропускаем")

# Симуляция pipeline

class SimplePipeline:
    def run(self, date):
        print(f"    Pipeline выполнен для {date}")
        return True

# Использование

manager = BackfillManager()
pipeline = SimplePipeline()

# Backfill за последние 3 дня

manager.backfill_date_range("2024-01-01", "2024-01-03", pipeline)
```

**Output:**
```
🔄 Backfill: 2024-01-01 до 2024-01-03 (3 дней)
  Обработка 2024-01-01...
    Pipeline выполнен для 2024-01-01
  Обработка 2024-01-02...
    Pipeline выполнен для 2024-01-02
  Обработка 2024-01-03...
    Pipeline выполнен для 2024-01-03

✅ Backfill завершён: 3 успешно, 0 ошибок
```

---

## 4. Versioning данных

Версионирование данных позволяет отслеживать изменения и восстанавливать предыдущие версии.

### 4.1 Стратегии версионирования

**Snapshot Versioning:**

- Полные снимки данных на момент времени
- Простота, но большой объём

**Delta Versioning:**

- Хранение только изменений
- Эффективнее по объёму

**Example: Версионирование данных**

```python
class DataVersioning:
    def __init__(self):
        self.versions = {}
        self.current_version = 0
    
    def create_version(self, data, description):
        """Создаёт новую версию данных"""
        self.current_version += 1
        version_id = f"v{self.current_version}"
        
        self.versions[version_id] = {
            "data": data.copy(),
            "description": description,
            "created_at": "2024-01-01",
            "parent_version": list(self.versions.keys())[-1] if self.versions else None
        }
        
        print(f"✅ Версия {version_id} создана: {description}")
        return version_id
    
    def get_version(self, version_id):
        """Получает данные версии"""
        if version_id not in self.versions:
            raise ValueError(f"Версия {version_id} не найдена")
        
        return self.versions[version_id]["data"]
    
    def list_versions(self):
        """Список всех версий"""
        print("\n📋 Версии данных:")
        for version_id, info in self.versions.items():
            print(f"  {version_id}: {info['description']} ({info['created_at']})")
        return list(self.versions.keys())

# Использование

versioning = DataVersioning()

# Создание версий

data_v1 = [{"id": 1, "name": "Alice"}]
versioning.create_version(data_v1, "Initial data")

data_v2 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
versioning.create_version(data_v2, "Added Bob")

# Список версий

versioning.list_versions()

# Получение версии

v1_data = versioning.get_version("v1")
print(f"\nДанные v1: {v1_data}")
```

**Output:**
```
✅ Версия v1 создана: Initial data
✅ Версия v2 создана: Added Bob

📋 Версии данных:
  v1: Initial data (2024-01-01)
  v2: Added Bob (2024-01-01)

Данные v1: [{'id': 1, 'name': 'Alice'}]
```

---

## 5. Reproducible Pipelines (Воспроизводимые pipelines)

Воспроизводимость означает, что pipeline даёт одинаковый результат при повторном выполнении с теми же входными данными.

### 5.1 Компоненты воспроизводимости

**Deterministic Operations:**

- Детерминированные функции
- Отсутствие случайности
- Фиксированные алгоритмы

**Version Control:**

- Версионирование кода
- Версионирование данных
- Версионирование схем

**Example: Воспроизводимый Pipeline**

```python
class ReproduciblePipeline:
    def __init__(self, code_version, data_version, schema_version):
        self.code_version = code_version
        self.data_version = data_version
        self.schema_version = schema_version
        self.config = {}
    
    def set_config(self, **kwargs):
        """Устанавливает конфигурацию"""
        self.config.update(kwargs)
        print(f"✅ Конфигурация установлена: {self.config}")
    
    def get_reproducibility_info(self):
        """Возвращает информацию для воспроизводимости"""
        return {
            "code_version": self.code_version,
            "data_version": self.data_version,
            "schema_version": self.schema_version,
            "config": self.config
        }
    
    def run(self, input_data):
        """Запускает pipeline (детерминированный)"""
        print(f"\n🚀 Запуск воспроизводимого pipeline:")
        print(f"   Code version: {self.code_version}")
        print(f"   Data version: {self.data_version}")
        print(f"   Schema version: {self.schema_version}")
        
        # Детерминированная обработка
        result = []
        for record in input_data:
            # Фиксированная логика (без случайности)
            processed = {
                "id": record.get("id"),
                "name": record.get("name", "").upper(),  # Детерминированное преобразование
                "processed_at": "2024-01-01T10:00:00"  # Фиксированное время для воспроизводимости
            }
            result.append(processed)
        
        print(f"✅ Pipeline выполнен, обработано {len(result)} записей")
        return result

# Использование

pipeline = ReproduciblePipeline(
    code_version="v1.2.3",
    data_version="v2",
    schema_version="v1"
)

pipeline.set_config(threshold=100, enable_feature_x=True)

input_data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
result1 = pipeline.run(input_data)

# Повторный запуск с теми же параметрами

print("\n" + "="*50)
print("Повторный запуск с теми же параметрами:")
result2 = pipeline.run(input_data)

# Результаты должны быть идентичны

print(f"\nРезультаты идентичны: {result1 == result2}")
```

**Output:**
```
✅ Конфигурация установлена: {'threshold': 100, 'enable_feature_x': True}

🚀 Запуск воспроизводимого pipeline:
   Code version: v1.2.3
   Data version: v2
   Schema version: v1
✅ Pipeline выполнен, обработано 2 записей

==================================================
Повторный запуск с теми же параметрами:

🚀 Запуск воспроизводимого pipeline:
   Code version: v1.2.3
   Data version: v2
   Schema version: v1
✅ Pipeline выполнен, обработано 2 записей

Результаты идентичны: True
```

### 5.2 Best Practices для воспроизводимости

**Фиксированные версии:**

- Версионирование всех зависимостей
- Фиксация версий библиотек
- Использование requirements.txt

**Детерминированные операции:**

- Избегать случайности
- Фиксировать seeds для random
- Использовать детерминированные алгоритмы

**Документация:**

- Документировать все параметры
- Сохранять конфигурации
- Версионировать схемы

---

## 6. Обработка ошибок в Production

Практические подходы к обработке ошибок в production системах.

### 6.1 Стратегии обработки

**Fail Fast:**

- Быстрое обнаружение ошибок
- Немедленная остановка при критических ошибках

**Graceful Degradation:**

- Продолжение работы при некритических ошибках
- Частичные результаты

**Dead Letter Queue:**

- Очередь для необработанных записей
- Ручная обработка проблемных данных

**Example: Production Error Handling**

```python
class ProductionPipeline:
    def __init__(self):
        self.dead_letter_queue = []
        self.stats = {"processed": 0, "failed": 0, "skipped": 0}
    
    def process_record(self, record, fail_fast=False):
        """Обрабатывает запись с обработкой ошибок"""
        try:
            # Симуляция обработки
            if record.get("id") is None:
                raise ValueError("Отсутствует обязательное поле 'id'")
            
            # Успешная обработка
            self.stats["processed"] += 1
            return {"status": "success", "record": record}
        
        except ValueError as e:
            # Критическая ошибка
            if fail_fast:
                raise
            self.dead_letter_queue.append({"record": record, "error": str(e)})
            self.stats["failed"] += 1
            return {"status": "failed", "error": str(e)}
        
        except Exception as e:
            # Некритическая ошибка
            self.stats["skipped"] += 1
            return {"status": "skipped", "error": str(e)}
    
    def process_batch(self, records, fail_fast=False):
        """Обрабатывает батч записей"""
        results = []
        for record in records:
            result = self.process_record(record, fail_fast)
            results.append(result)
        
        print(f"\n📊 Статистика обработки:")
        print(f"   Обработано: {self.stats['processed']}")
        print(f"   Ошибок: {self.stats['failed']}")
        print(f"   Пропущено: {self.stats['skipped']}")
        print(f"   В dead letter queue: {len(self.dead_letter_queue)}")
        
        return results

# Использование

pipeline = ProductionPipeline()

records = [
    {"id": 1, "name": "Alice"},
    {"id": None, "name": "Bob"},  # Ошибка
    {"id": 3, "name": "Charlie"}
]

results = pipeline.process_batch(records, fail_fast=False)
```

**Output:**
```
📊 Статистика обработки:
   Обработано: 2
   Ошибок: 1
   Пропущено: 0
   В dead letter queue: 1
```

---

## 💡 Key Takeaways

- **Retries**: Автоматические повторные попытки при временных ошибках. Exponential backoff для эффективности.

- **Backfills**: Переобработка исторических данных после исправлений. Full или incremental стратегии.

- **Versioning**: Версионирование данных, кода и схем для отслеживания изменений и восстановления.

- **Reproducibility**: Воспроизводимые pipelines дают одинаковый результат. Детерминированные операции, фиксированные версии.

- **Production Error Handling**: Fail fast для критических ошибок, graceful degradation для некритических, dead letter queue для проблемных данных.

---

## 🚀 Next Steps

**Related Modules:**

- [13_Streaming_Model](../13_Streaming_Model/) — streaming обработка
- [19_Reliability_Operations](../19_Reliability_Operations/) — надёжность и эксплуатация
- [09_Batch_Processing](../09_Batch_Processing/) — batch processing

**Practice Ideas:**

1. Реализуйте retry механизм: exponential backoff для ваших операций
2. Создайте backfill процесс: переобработка данных за период
3. Версионируйте ваши данные: отслеживание изменений

**Going Deeper:**

- Изучите паттерны обработки ошибок: circuit breaker, bulkhead
- Погрузитесь в data versioning: Delta Lake, time travel
- Изучите воспроизводимость в ML: MLflow, DVC

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — обработка ошибок
- "Release It!" by Michael Nygard — production reliability

**Articles:**

- "Error Handling in Data Pipelines" — best practices
- "Data Versioning Strategies" — подходы к версионированию

**Documentation:**

- Delta Lake: https://delta.io/ (time travel)
- MLflow: https://mlflow.org/ (ML reproducibility)

---



