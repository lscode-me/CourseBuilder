# Batch processing

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать жизненный цикл данных (модуль 02)
- Знать хранилища данных (модуль 05)
- Иметь представление о форматах данных (модуль 06)

**Recommended prior modules:**

- [02_Data_Lifecycle](../02_Data_Lifecycle/) — жизненный цикл данных
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [06_Data_Formats](../06_Data_Formats/) — форматы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проектировать batch pipelines для обработки данных
- Различать ETL и ELT подходы
- Настраивать scheduling для batch jobs
- Обеспечивать идемпотентность pipeline'ов

---

## 1. Введение в Batch Processing

Batch processing — это обработка данных порциями (батчами) по расписанию. Это основной подход для обработки больших объёмов данных, когда не требуется real-time обработка.

**Характеристики batch processing:**

- Обработка накопленных данных
- Запуск по расписанию
- Высокая пропускная способность
- Эффективное использование ресурсов

---

## 2. Batch Pipelines

Batch pipeline — это последовательность шагов для обработки данных порциями.

### 2.1 Компоненты Batch Pipeline

**Extract (Извлечение):**

- Сбор данных из источников
- Чтение файлов, запросы к БД
- Загрузка в staging area

**Transform (Трансформация):**

- Очистка данных
- Валидация
- Обогащение
- Агрегация

**Load (Загрузка):**

- Запись в целевое хранилище
- Обновление существующих данных
- Создание индексов

**Example: Простой Batch Pipeline**

```python

class BatchPipeline:
    def __init__(self, name):
        self.name = name
        self.steps = []
    
    def extract(self, source):
        """Шаг 1: Extract"""
        print(f"📥 Extract: чтение данных из {source}")
        # Симуляция чтения
        data = [
            {"id": 1, "name": "Alice", "age": "30", "city": "Moscow"},
            {"id": 2, "name": "Bob", "age": "25", "city": "SPB"},
            {"id": 3, "name": "Charlie", "age": "35", "city": "Moscow"}
        ]
        return data
    
    def transform(self, data):
        """Шаг 2: Transform"""
        print(f"⚙️  Transform: обработка {len(data)} записей")
        transformed = []
        for record in data:
            # Очистка и валидация
            if record.get("id") and record.get("name"):
                transformed.append({
                    "id": int(record["id"]),
                    "name": record["name"].strip(),
                    "age": int(record["age"]),
                    "city": record["city"]
                })
        print(f"✅ Transform: {len(transformed)} записей обработано")
        return transformed
    
    def load(self, data, target):
        """Шаг 3: Load"""
        print(f"💾 Load: загрузка {len(data)} записей в {target}")
        # Симуляция загрузки
        print(f"✅ Load: данные загружены в {target}")
        return True
    
    def run(self, source, target):
        """Запуск полного pipeline"""
        print(f"\n🚀 Запуск batch pipeline: {self.name}")
        print("=" * 50)
        
        # Extract
        raw_data = self.extract(source)
        
        # Transform
        transformed_data = self.transform(raw_data)
        
        # Load
        self.load(transformed_data, target)
        
        print("=" * 50)
        print(f"✅ Pipeline '{self.name}' завершён успешно\n")
        return True

# Использование

pipeline = BatchPipeline("user_data_pipeline")
pipeline.run("users.csv", "data_warehouse.users")
```

**Output:**
```

🚀 Запуск batch pipeline: user_data_pipeline
==================================================
📥 Extract: чтение данных из users.csv
⚙️  Transform: обработка 3 записей
✅ Transform: 3 записей обработано
💾 Load: загрузка 3 записей в data_warehouse.users
✅ Load: данные загружены в data_warehouse.users
==================================================
✅ Pipeline 'user_data_pipeline' завершён успешно
```

---

## 3. ETL vs ELT

Разница между ETL и ELT в порядке операций.

### 3.1 ETL (Extract, Transform, Load)

**Порядок:**

1. Extract — извлечение из источников
2. Transform — трансформация в промежуточной системе
3. Load — загрузка трансформированных данных

**Характеристики:**

- Трансформация до загрузки
- Требует промежуточного хранилища
- Данные уже готовы при загрузке

**Example: ETL Pipeline**

```python

class ETLPipeline:
    def extract(self, source):
        """Extract: извлечение сырых данных"""
        print("📥 ETL Extract: чтение из источника")
        raw_data = [{"id": 1, "name": "Alice", "age": "30"}]
        return raw_data
    
    def transform(self, data):
        """Transform: трансформация ПЕРЕД загрузкой"""
        print("⚙️  ETL Transform: обработка в промежуточной системе")
        transformed = []
        for record in data:
            transformed.append({
                "id": int(record["id"]),
                "name": record["name"].title(),
                "age": int(record["age"])
            })
        print(f"✅ ETL Transform: {len(transformed)} записей готовы")
        return transformed
    
    def load(self, data, target):
        """Load: загрузка УЖЕ трансформированных данных"""
        print(f"💾 ETL Load: загрузка готовых данных в {target}")
        print("✅ ETL: данные уже трансформированы при загрузке")
        return True
    
    def run(self, source, target):
        """Запуск ETL"""
        raw = self.extract(source)
        transformed = self.transform(raw)
        self.load(transformed, target)

# Использование

etl = ETLPipeline()
etl.run("source.csv", "warehouse.table")
```

**Output:**
```

📥 ETL Extract: чтение из источника
⚙️  ETL Transform: обработка в промежуточной системе
✅ ETL Transform: 1 записей готовы
💾 ETL Load: загрузка готовых данных в warehouse.table
✅ ETL: данные уже трансформированы при загрузке
```

### 3.2 ELT (Extract, Load, Transform)

**Порядок:**

1. Extract — извлечение из источников
2. Load — загрузка сырых данных в хранилище
3. Transform — трансформация в хранилище

**Характеристики:**

- Загрузка сырых данных сначала
- Трансформация в хранилище (SQL)
- Использует вычислительную мощность хранилища

**Example: ELT Pipeline**

```python

class ELTPipeline:
    def extract(self, source):
        """Extract: извлечение сырых данных"""
        print("📥 ELT Extract: чтение из источника")
        raw_data = [{"id": 1, "name": "Alice", "age": "30"}]
        return raw_data
    
    def load(self, data, target):
        """Load: загрузка СЫРЫХ данных в хранилище"""
        print(f"💾 ELT Load: загрузка сырых данных в {target}")
        print("✅ ELT: данные загружены как есть (Bronze layer)")
        return True
    
    def transform(self, target):
        """Transform: трансформация В хранилище (SQL)"""
        print(f"⚙️  ELT Transform: трансформация в {target} с помощью SQL")
        sql = """
        INSERT INTO silver.users
        SELECT 
            CAST(id AS INT) as id,
            TRIM(name) as name,
            CAST(age AS INT) as age
        FROM bronze.raw_users
        """
        print(f"✅ ELT Transform: SQL выполнен в хранилище")
        return True
    
    def run(self, source, target):
        """Запуск ELT"""
        raw = self.extract(source)
        self.load(raw, f"{target}_bronze")
        self.transform(target)

# Использование
elt = ELTPipeline()
elt.run("source.csv", "warehouse")
```

**Output:**
```

📥 ELT Extract: чтение из источника
💾 ELT Load: загрузка сырых данных в warehouse_bronze
✅ ELT: данные загружены как есть (Bronze layer)
⚙️  ELT Transform: трансформация в warehouse с помощью SQL
✅ ELT Transform: SQL выполнен в хранилище
```

### 3.3 Сравнение ETL vs ELT

| Аспект | ETL | ELT |
|--------|-----|-----|
| **Порядок** | Extract → Transform → Load | Extract → Load → Transform |
| **Где трансформация** | Промежуточная система | В хранилище (SQL) |
| **Сырые данные** | Не сохраняются | Сохраняются (Bronze) |
| **Использование** | Традиционный подход | Современный подход (Data Lakehouse) |
| **Гибкость** | Меньше (данные уже трансформированы) | Больше (можно трансформировать по-разному) |

---

## 4. Scheduling (Планирование)

Scheduling — это автоматический запуск batch jobs по расписанию.

### 4.1 Типы расписаний

**Time-based:**

- По времени (каждый час, день, неделю)
- Cron expressions
- Пример: "0 2 * * *" (каждый день в 2:00)

**Event-based:**

- По событию (файл появился, данные готовы)
- Triggers
- Пример: запуск после завершения другого job

**Example: Scheduling**

```python

from datetime import datetime, timedelta

class Scheduler:
    def __init__(self):
        self.jobs = []
    
    def schedule_daily(self, job_name, time="02:00"):
        """Планирует ежедневный запуск"""
        schedule = {
            "job": job_name,
            "frequency": "daily",
            "time": time,
            "next_run": self._calculate_next_run("daily", time)
        }
        self.jobs.append(schedule)
        print(f"✅ Запланирован daily job '{job_name}' на {time}")
        return schedule
    
    def schedule_hourly(self, job_name):
        """Планирует ежечасный запуск"""
        schedule = {
            "job": job_name,
            "frequency": "hourly",
            "next_run": datetime.now() + timedelta(hours=1)
        }
        self.jobs.append(schedule)
        print(f"✅ Запланирован hourly job '{job_name}'")
        return schedule
    
    def schedule_on_event(self, job_name, trigger_job):
        """Планирует запуск по событию"""
        schedule = {
            "job": job_name,
            "frequency": "event-based",
            "trigger": trigger_job
        }
        self.jobs.append(schedule)
        print(f"✅ Запланирован event-based job '{job_name}' после '{trigger_job}'")
        return schedule
    
    def _calculate_next_run(self, frequency, time_str):
        """Вычисляет следующее время запуска"""
        now = datetime.now()
        if frequency == "daily":
            hour, minute = map(int, time_str.split(":"))
            next_run = now.replace(hour=hour, minute=minute, second=0)
            if next_run <= now:
                next_run += timedelta(days=1)
            return next_run
        return now
    
    def get_upcoming_jobs(self):
        """Возвращает предстоящие jobs"""
        upcoming = sorted([j for j in self.jobs if "next_run" in j], 
                         key=lambda x: x["next_run"])
        return upcoming

# Использование
scheduler = Scheduler()

# Daily job
scheduler.schedule_daily("daily_sales_etl", "02:00")

# Hourly job
scheduler.schedule_hourly("hourly_metrics_update")

# Event-based job

scheduler.schedule_on_event("analytics_refresh", "daily_sales_etl")

# Предстоящие jobs
upcoming = scheduler.get_upcoming_jobs()
print(f"\nПредстоящие jobs: {len(upcoming)}")
for job in upcoming[:3]:
    print(f"  {job['job']}: {job.get('next_run', 'N/A')}")
```

**Output:**
```

✅ Запланирован daily job 'daily_sales_etl' на 02:00
✅ Запланирован hourly job 'hourly_metrics_update'
✅ Запланирован event-based job 'analytics_refresh' после 'daily_sales_etl'

Предстоящие jobs: 2
  hourly_metrics_update: 2024-01-01 11:00:00
  daily_sales_etl: 2024-01-02 02:00:00
```

---

## 5. Idempotency (Идемпотентность)

Idempotency — это свойство операции: повторное выполнение даёт тот же результат, что и первое.

### 5.1 Зачем нужна идемпотентность

**Проблемы без идемпотентности:**

- Дублирование данных при повторном запуске
- Неконсистентность данных
- Сложность отладки

**Преимущества идемпотентности:**

- Безопасный перезапуск
- Отсутствие дубликатов
- Предсказуемость

**Example: Идемпотентный Pipeline**

```python

class IdempotentPipeline:
    def __init__(self):
        self.processed_dates = set()
    
    def is_already_processed(self, date):
        """Проверяет, обработана ли дата"""
        return date in self.processed_dates
    
    def mark_as_processed(self, date):
        """Помечает дату как обработанную"""
        self.processed_dates.add(date)
        print(f"✅ Дата {date} помечена как обработанная")
    
    def process_date(self, date):
        """Обрабатывает данные за дату (идемпотентно)"""
        if self.is_already_processed(date):
            print(f"⏭️  Дата {date} уже обработана, пропускаем")
            return True
        
        print(f"🔄 Обработка данных за {date}")
        # Симуляция обработки
        result = f"processed_{date}"
        
        self.mark_as_processed(date)
        return result
    
    def run(self, date):
        """Запуск pipeline (идемпотентный)"""
        print(f"\n🚀 Запуск pipeline для {date}")
        
        # Проверка идемпотентности
        if self.is_already_processed(date):
            print("✅ Pipeline уже выполнен для этой даты")
            return True
        
        # Обработка
        self.process_date(date)
        
        print("✅ Pipeline завершён\n")
        return True

# Использование

pipeline = IdempotentPipeline()

# Первый запуск

pipeline.run("2024-01-01")

# Повторный запуск (идемпотентный)
print("Повторный запуск того же pipeline:")
pipeline.run("2024-01-01")

# Новый запуск
pipeline.run("2024-01-02")
```

**Output:**
```

🚀 Запуск pipeline для 2024-01-01
🔄 Обработка данных за 2024-01-01
✅ Дата 2024-01-01 помечена как обработанная
✅ Pipeline завершён

Повторный запуск того же pipeline:
🚀 Запуск pipeline для 2024-01-01
⏭️  Дата 2024-01-01 уже обработана, пропускаем
✅ Pipeline уже выполнен для этой даты

🚀 Запуск pipeline для 2024-01-02
🔄 Обработка данных за 2024-01-02
✅ Дата 2024-01-02 помечена как обработанная
✅ Pipeline завершён
```

### 5.2 Стратегии идемпотентности

**Upsert:**

- Обновление существующих, вставка новых
- Использование уникальных ключей

**Delete and Insert:**

- Удаление данных за период
- Вставка новых данных

**Versioning:**

- Версионирование данных
- Отслеживание версий

**Example: Upsert стратегия**

```python

def upsert_data(target_table, data, key_column):
    """Upsert: обновление существующих, вставка новых"""
    print(f"🔄 Upsert в {target_table} по ключу {key_column}")
    
    # Симуляция: проверяем существующие записи
    existing_keys = {1, 3}  # Симуляция существующих
    
    updated = 0
    inserted = 0
    
    for record in data:
        key = record.get(key_column)
        if key in existing_keys:
            # UPDATE
            print(f"  UPDATE: запись {key}")
            updated += 1
        else:
            # INSERT
            print(f"  INSERT: запись {key}")
            inserted += 1
    
    print(f"✅ Upsert завершён: {updated} обновлено, {inserted} вставлено")
    return updated, inserted

# Использование
data = [
    {"id": 1, "name": "Alice Updated"},
    {"id": 2, "name": "Bob New"},
    {"id": 3, "name": "Charlie Updated"}
]

upsert_data("users", data, "id")
```

**Output:**
```

🔄 Upsert в users по ключу id
  UPDATE: запись 1
  INSERT: запись 2
  UPDATE: запись 3
✅ Upsert завершён: 2 обновлено, 1 вставлено
```

---

## 6. Best Practices Batch Processing

Рекомендации для проектирования эффективных batch pipelines.

### 6.1 Проектирование Pipeline

**Модульность:**

- Разбивать на отдельные шаги
- Переиспользование компонентов
- Легкость тестирования

**Обработка ошибок:**

- Retry механизмы
- Логирование
- Alerting при ошибках

**Мониторинг:**

- Метрики выполнения
- Время выполнения
- Объём обработанных данных

**Example: Best Practices**

```python

class RobustPipeline:
    def __init__(self, name):
        self.name = name
        self.metrics = {
            "runs": 0,
            "success": 0,
            "failures": 0,
            "total_records": 0
        }
    
    def run_with_retry(self, max_retries=3):
        """Запуск с retry механизмом"""
        for attempt in range(1, max_retries + 1):
            try:
                print(f"🔄 Попытка {attempt}/{max_retries}")
                result = self._execute()
                self.metrics["success"] += 1
                print("✅ Pipeline выполнен успешно")
                return result
            except Exception as e:
                print(f"❌ Ошибка: {e}")
                if attempt == max_retries:
                    self.metrics["failures"] += 1
                    raise
                print("⏳ Повтор через 5 секунд...")
                import time
                time.sleep(5)
    
    def _execute(self):
        """Выполнение pipeline"""
        self.metrics["runs"] += 1
        # Симуляция выполнения
        self.metrics["total_records"] += 100
        return True
    
    def get_metrics(self):
        """Возвращает метрики"""
        return self.metrics

# Использование
pipeline = RobustPipeline("robust_pipeline")

# Успешный запуск
pipeline.run_with_retry()

# Метрики

metrics = pipeline.get_metrics()
print(f"\nМетрики pipeline:")
for key, value in metrics.items():
    print(f"  {key}: {value}")
```

**Output:**
```

🔄 Попытка 1/3
✅ Pipeline выполнен успешно

Метрики pipeline:
  runs: 1
  success: 1
  failures: 0
  total_records: 100
```

---

## 💡 Key Takeaways

- **Batch Processing**: Обработка данных порциями по расписанию. Эффективно для больших объёмов данных, когда не требуется real-time.

- **ETL vs ELT**: ETL трансформирует до загрузки, ELT загружает сырые данные и трансформирует в хранилище. ELT более гибкий и современный подход.

- **Scheduling**: Автоматический запуск jobs по расписанию (time-based, event-based). Критично для регулярной обработки данных.

- **Idempotency**: Повторное выполнение даёт тот же результат. Обеспечивает безопасность перезапуска и отсутствие дубликатов.

- **Best Practices**: Модульность, обработка ошибок, мониторинг, retry механизмы — всё это критично для надёжных batch pipelines.

---

## 🚀 Next Steps

**Related Modules:**

- [10_Batch_Tools](../10_Batch_Tools/) — инструменты batch processing (Spark, Airflow, dbt)
- [11_Data_Quality](../11_Data_Quality/) — качество данных
- [12_Errors_Reproducibility](../12_Errors_Reproducibility/) — ошибки и воспроизводимость

**Practice Ideas:**

1. Создайте простой batch pipeline на Python: Extract, Transform, Load
2. Реализуйте идемпотентность: добавьте проверку уже обработанных данных
3. Настройте scheduling: используйте cron или планировщик задач

**Going Deeper:**

- Изучите Apache Airflow: оркестрация batch pipelines
- Погрузитесь в dbt: трансформации в хранилище
- Изучите паттерны batch processing: incremental loads, full loads, upserts

---

## 📚 Additional Resources

**Books:**

- "Fundamentals of Data Engineering" by Joe Reis & Matt Housley — batch processing
- "Designing Data-Intensive Applications" by Martin Kleppmann — batch systems

**Articles:**

- "ETL vs ELT: What's the Difference?" — сравнение подходов
- "Building Idempotent Data Pipelines" — best practices

**Documentation:**

- Apache Airflow: https://airflow.apache.org/docs/
- dbt: https://docs.getdbt.com/
- Apache Spark: https://spark.apache.org/docs/latest/

---


