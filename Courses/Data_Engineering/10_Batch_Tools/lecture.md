# Data Engineering
## Инструменты batch processing

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать batch processing (модуль 09)
- Знать основы SQL
- Иметь представление о распределённых системах

**Recommended prior modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать SQL engines для обработки данных
- Работать с Apache Spark для распределённой обработки
- Оркестрировать pipelines с Apache Airflow
- Применять dbt для трансформаций в хранилище

---

## 1. Введение в инструменты batch processing

Выбор правильных инструментов критичен для эффективной обработки данных. Различные инструменты оптимизированы для разных задач и масштабов.

**Категории инструментов:**

- **SQL Engines** — для запросов к данным

- **Distributed Processing** — Spark для больших объёмов

- **Orchestration** — Airflow для планирования

- **Transformation** — dbt для SQL трансформаций

---

## 2. SQL Engines

SQL engines позволяют выполнять SQL запросы к различным источникам данных.

### 2.1 Типы SQL Engines

**OLTP Engines:**

- PostgreSQL, MySQL
- Для транзакционных запросов
- Оптимизированы для операций

**OLAP Engines:**

- Presto, Trino, Spark SQL
- Для аналитических запросов
- Оптимизированы для агрегаций

**Example: SQL Engine запрос**

```python
# Симуляция SQL engine
class SQLEngine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        self.data = {}
    
    def execute_query(self, query):
        """Выполняет SQL запрос"""
        print(f"🔍 [{self.engine_type}] Выполнение запроса:")
        print(f"   {query}")
        
        # Симуляция выполнения
        if "SELECT" in query.upper():
            if "COUNT" in query.upper():
                return {"count": 1000}
            elif "SUM" in query.upper():
                return {"sum": 50000}
            else:
                return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        return True
    
    def query(self, sql):
        """Удобный метод для запросов"""
        return self.execute_query(sql)

# Использование
presto = SQLEngine("Presto")
result = presto.query("""
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(revenue) as total_revenue
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY month
""")
print(f"Результат: {result}")
```

**Output:**
```

🔍 [Presto] Выполнение запроса:
   SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(revenue) as total_revenue
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY month
Результат: {'sum': 50000}
```

---

## 3. Apache Spark

Apache Spark — это распределённый движок для обработки больших объёмов данных.

### 3.1 Характеристики Spark

**Распределённая обработка:**

- Обработка на кластере
- Горизонтальное масштабирование
- Отказоустойчивость

**In-memory processing:**

- Кеширование данных в памяти
- Быстрая итеративная обработка
- Оптимизация запросов

**Example: Spark концепция**

```python
# Симуляция Spark
class SparkJob:
    def __init__(self):
        self.stages = []
    
    def read(self, source):
        """Читает данные из источника"""
        print(f"📥 Spark: чтение из {source}")
        return self
    
    def transform(self, transformation):
        """Применяет трансформацию"""
        print(f"⚙️  Spark: трансформация '{transformation}'")
        self.stages.append(transformation)
        return self
    
    def write(self, target):
        """Записывает данные"""
        print(f"💾 Spark: запись в {target}")
        return self
    
    def execute(self):
        """Выполняет job"""
        print(f"🚀 Spark: выполнение job с {len(self.stages)} стадиями")
        print(f"   Стадии: {', '.join(self.stages)}")
        print("✅ Spark job завершён")
        return True

# Использование

spark_job = SparkJob()
spark_job.read("s3://data/raw/users.parquet") \
    .transform("filter(age > 18)") \
    .transform("groupBy(city)") \
    .transform("agg(count(*))") \
    .write("s3://data/processed/user_stats.parquet") \
    .execute()
```

**Output:**
```

📥 Spark: чтение из s3://data/raw/users.parquet
⚙️  Spark: трансформация 'filter(age > 18)'
⚙️  Spark: трансформация 'groupBy(city)'
⚙️  Spark: трансформация 'agg(count(*))'
💾 Spark: запись в s3://data/processed/user_stats.parquet
🚀 Spark: выполнение job с 3 стадиями
   Стадии: filter(age > 18), groupBy(city), agg(count(*))
✅ Spark job завершён
```

### 3.2 Spark компоненты

**Spark Core:**

- Базовый движок
- RDD (Resilient Distributed Datasets)
- Распределённая обработка

**Spark SQL:**

- SQL интерфейс
- DataFrame API
- Оптимизация запросов

**Spark Streaming:**

- Обработка потоков
- Микробатчи
- Real-time обработка

---

## 4. Apache Airflow

Apache Airflow — это платформа для оркестрации и планирования workflows.

### 4.1 Концепция Airflow

**DAG (Directed Acyclic Graph):**

- Граф задач
- Зависимости между задачами
- Планирование выполнения

**Tasks:**

- Отдельные операции
- Операторы (Python, SQL, Bash)
- Зависимости

**Example: Airflow DAG**

```python
# Симуляция Airflow DAG
class AirflowDAG:
    def __init__(self, dag_id, schedule):
        self.dag_id = dag_id
        self.schedule = schedule
        self.tasks = []
        self.dependencies = {}
    
    def add_task(self, task_id, operator, **kwargs):
        """Добавляет задачу в DAG"""
        task = {
            "task_id": task_id,
            "operator": operator,
            "kwargs": kwargs
        }
        self.tasks.append(task)
        print(f"✅ Задача '{task_id}' добавлена в DAG '{self.dag_id}'")
        return task_id
    
    def set_dependency(self, upstream, downstream):
        """Устанавливает зависимость"""
        if downstream not in self.dependencies:
            self.dependencies[downstream] = []
        self.dependencies[downstream].append(upstream)
        print(f"🔗 Зависимость: {upstream} -> {downstream}")
    
    def visualize(self):
        """Визуализирует DAG"""
        print(f"\n📊 DAG: {self.dag_id}")
        print(f"   Schedule: {self.schedule}")
        print(f"   Tasks: {len(self.tasks)}")
        print("   Зависимости:")
        for task, deps in self.dependencies.items():
            print(f"     {task} зависит от: {', '.join(deps)}")

# Использование

dag = AirflowDAG("daily_etl", "0 2 * * *")

# Задачи

extract_task = dag.add_task("extract_data", "PythonOperator")
transform_task = dag.add_task("transform_data", "PythonOperator")
load_task = dag.add_task("load_data", "PythonOperator")

# Зависимости
dag.set_dependency(extract_task, transform_task)
dag.set_dependency(transform_task, load_task)

dag.visualize()
```

**Output:**
```

✅ Задача 'extract_data' добавлена в DAG 'daily_etl'
✅ Задача 'transform_data' добавлена в DAG 'daily_etl'
✅ Задача 'load_data' добавлена в DAG 'daily_etl'
🔗 Зависимость: extract_data -> transform_data
🔗 Зависимость: transform_data -> load_data

📊 DAG: daily_etl
   Schedule: 0 2 * * *
   Tasks: 3
   Зависимости:
     transform_data зависит от: extract_data
     load_data зависит от: transform_data
```

### 4.2 Преимущества Airflow

**Оркестрация:**

- Управление сложными workflows
- Зависимости между задачами
- Параллельное выполнение

**Мониторинг:**

- UI для визуализации
- Логи выполнения
- Retry механизмы

**Масштабирование:**

- Распределённое выполнение
- Интеграция с различными системами

---

## 5. dbt (Data Build Tool)

dbt — это инструмент для трансформаций данных в хранилище с помощью SQL.

### 5.1 Концепция dbt

**SQL-based трансформации:**

- Трансформации в SQL
- Выполнение в хранилище
- Модели как код

**Модели:**

- SQL файлы для трансформаций
- Зависимости между моделями
- Тестирование данных

**Example: dbt модель**

```python
# Симуляция dbt
class DBTModel:
    def __init__(self, name, sql, dependencies=None):
        self.name = name
        self.sql = sql
        self.dependencies = dependencies or []
        self.tests = []
    
    def add_test(self, test_name, test_sql):
        """Добавляет тест к модели"""
        self.tests.append({
            "name": test_name,
            "sql": test_sql
        })
        print(f"✅ Тест '{test_name}' добавлен к модели '{self.name}'")
    
    def compile(self):
        """Компилирует модель"""
        print(f"🔨 Компиляция модели '{self.name}'")
        print(f"   SQL: {self.sql[:50]}...")
        print(f"   Зависимости: {self.dependencies}")
        return self.sql
    
    def run(self, connection):
        """Выполняет модель"""
        print(f"🚀 Выполнение модели '{self.name}' в {connection}")
        print("✅ Модель выполнена успешно")
        return True

# Использование

user_stats_model = DBTModel(
    name="user_stats",
    sql="""
        SELECT 
            city,
            COUNT(*) as user_count,
            AVG(age) as avg_age
        FROM {{ ref('users') }}
        GROUP BY city
    """,
    dependencies=["users"]
)

user_stats_model.add_test("not_null", "SELECT * FROM {{ ref('user_stats') }} WHERE city IS NULL")
user_stats_model.compile()
user_stats_model.run("warehouse")
```

**Output:**
```

✅ Тест 'not_null' добавлен к модели 'user_stats'
🔨 Компиляция модели 'user_stats'
   SQL: 
        SELECT 
            city,
            COUNT(*) as user_count,
...
   Зависимости: ['users']
🚀 Выполнение модели 'user_stats' в warehouse
✅ Модель выполнена успешно
```

### 5.2 Преимущества dbt

**SQL-first:**

- Использование SQL для трансформаций
- Легко для аналитиков
- Выполнение в хранилище

**Версионирование:**

- Модели как код
- Git для управления
- Code review

**Тестирование:**

- Встроенные тесты
- Валидация данных
- Документация

---

## 6. Выбор инструментов

Выбор инструмента зависит от задачи и масштаба.

### 6.1 Decision Matrix

**SQL Engines (Presto, Trino):**

- Аналитические запросы
- Интерактивные запросы
- Ad-hoc анализ

**Spark:**

- Большие объёмы данных (>100GB)
- Сложные трансформации
- Распределённая обработка

**Airflow:**

- Оркестрация workflows
- Планирование задач
- Управление зависимостями

**dbt:**

- Трансформации в хранилище
- SQL-based подход
- Модели как код

**Example: Выбор инструмента**

```python

def recommend_tool(requirements):
    """Рекомендует инструмент"""
    if requirements.get("orchestration") and requirements.get("scheduling"):
        return "Airflow (оркестрация и планирование)"
    elif requirements.get("large_volume") and requirements.get("distributed"):
        return "Spark (распределённая обработка больших объёмов)"
    elif requirements.get("sql_transformations") and requirements.get("warehouse"):
        return "dbt (SQL трансформации в хранилище)"
    elif requirements.get("analytical_queries") and requirements.get("interactive"):
        return "SQL Engine (Presto/Trino для аналитических запросов)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"orchestration": True, "scheduling": True, "workflows": True},
    {"large_volume": True, "distributed": True, "complex_transforms": True},
    {"sql_transformations": True, "warehouse": True, "models": True},
    {"analytical_queries": True, "interactive": True, "ad_hoc": True}
]

print("Рекомендации инструментов:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_tool(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации инструментов:
  Пример 1: Airflow (оркестрация и планирование)
  Пример 2: Spark (распределённая обработка больших объёмов)
  Пример 3: dbt (SQL трансформации в хранилище)
  Пример 4: SQL Engine (Presto/Trino для аналитических запросов)
```

---

## 7. Комбинация инструментов

В реальных системах часто используются несколько инструментов вместе.

### 7.1 Типичная архитектура

**Airflow + Spark:**

- Airflow оркестрирует Spark jobs
- Планирование и мониторинг
- Обработка больших объёмов

**Airflow + dbt:**

- Airflow запускает dbt модели
- Управление зависимостями
- SQL трансформации

**Spark + SQL Engines:**

- Spark для ETL
- SQL Engines для аналитики
- Разделение нагрузки

**Example: Комбинированная архитектура**

```python

class IntegratedPipeline:
    def __init__(self):
        self.components = {}
    
    def setup(self):
        """Настраивает компоненты"""
        self.components = {
            "airflow": "Оркестрация workflows",
            "spark": "Обработка больших объёмов",
            "dbt": "SQL трансформации",
            "presto": "Аналитические запросы"
        }
        print("✅ Компоненты настроены:")
        for component, purpose in self.components.items():
            print(f"   {component}: {purpose}")
    
    def run_pipeline(self):
        """Запускает интегрированный pipeline"""
        print("\n🚀 Запуск интегрированного pipeline:")
        print("   1. Airflow планирует выполнение")
        print("   2. Spark обрабатывает большие объёмы данных")
        print("   3. dbt выполняет SQL трансформации")
        print("   4. Presto предоставляет аналитические запросы")
        print("✅ Pipeline завершён")

# Использование

pipeline = IntegratedPipeline()
pipeline.setup()
pipeline.run_pipeline()
```

**Output:**
```

✅ Компоненты настроены:
   airflow: Оркестрация workflows
   spark: Обработка больших объёмов
   dbt: SQL трансформации
   presto: Аналитические запросы

🚀 Запуск интегрированного pipeline:

   1. Airflow планирует выполнение
   2. Spark обрабатывает большие объёмы данных
   3. dbt выполняет SQL трансформации
   4. Presto предоставляет аналитические запросы
✅ Pipeline завершён
```

---

## 💡 Key Takeaways

- **SQL Engines**: Presto, Trino для аналитических запросов. Оптимизированы для интерактивных запросов к большим данным.

- **Apache Spark**: Распределённый движок для обработки больших объёмов. In-memory processing, горизонтальное масштабирование.

- **Apache Airflow**: Оркестрация и планирование workflows. DAG для управления зависимостями, мониторинг и retry.

- **dbt**: SQL-based трансформации в хранилище. Модели как код, тестирование, версионирование.

- **Комбинация инструментов**: Реальные системы используют несколько инструментов вместе. Airflow оркестрирует, Spark обрабатывает, dbt трансформирует.

---

## 🚀 Next Steps

**Related Modules:**

- [11_Data_Quality](../11_Data_Quality/) — качество данных
- [12_Errors_Reproducibility](../12_Errors_Reproducibility/) — ошибки и воспроизводимость
- [13_Streaming_Model](../13_Streaming_Model/) — streaming обработка

**Practice Ideas:**

1. Создайте простой Airflow DAG: несколько задач с зависимостями
2. Изучите Spark на практике: создайте простой Spark job
3. Попробуйте dbt: создайте модель и тесты

**Going Deeper:**

- Изучите Spark internals: RDD, DataFrame, Catalyst optimizer
- Погрузитесь в Airflow: операторы, sensors, XComs
- Изучите dbt best practices: макросы, инкрементальные модели

---

## 📚 Additional Resources

**Books:**

- "Learning Spark" by Jules Damji — практическое руководство по Spark
- "High Performance Spark" — оптимизация Spark jobs

**Articles:**

- "Apache Airflow Tutorial" — введение в Airflow
- "dbt Best Practices" — рекомендации по использованию dbt

**Documentation:**

- Apache Spark: https://spark.apache.org/docs/latest/
- Apache Airflow: https://airflow.apache.org/docs/
- dbt: https://docs.getdbt.com/

---


