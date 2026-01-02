# Choosing Data Systems For System Design
## SQL vs NoSQL vs NewSQL. OLTP vs OLAP.

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **All previous modules**: Вы должны знать, что такое B-Trees (07), ACID (08), CAP (09), Replication (11).

- **Architecture**: Понимать разницу между микросервисами и монолитом.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Classify**: Четко различать OLTP, OLAP, Document, Wide-Column, Graph, Key-Value, Search Engines.

- **Select**: Выбирать правильную базу под задачу (Billing -> SQL, Catalog -> Mongo, Logs -> Elastic).

- **Refute**: Аргументированно объяснять, почему "MongoDB is Web Scale" — это не аргумент.

- **Migrate**: Планировать миграцию с одной базы на другую без даунтайма (Dual Write Strategy).

- **Cost**: Оценивать стоимость владения (TCO).

---

## 1. Ландшафт баз данных (The Landscape)

В 90-е был только Oracle (и чуть-чуть MySQL).
Сегодня у нас зоопарк. Давайте наведем порядок.

### 1.1 Decision Matrix

| Category | Model | Examples | CAP | Best For | Worst For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RDBMS** | Relational (Tables) | PostgreSQL, MySQL, Oracle | CA/CP | Financials, Structured Data, Joins | Unstructured JSON, Massive Write Throughput |
| **Document** | JSON Documents | MongoDB, Couchbase | CP/AP | Content Management, User Profiles, Catalogs | Complex Analytics (Joins), Multi-record Transactions |
| **Wide-Column** | Sparse 2D Map | Cassandra, HBase, Scylla | AP | IoT, Reviews, Messages, Write-Heavy | Ad-hoc queries, Small datasets |
| **Key-Value** | Hash Map | Redis, DynamoDB, Riak | AP/CP | Caching, Sessions, Shopping Carts | Relations, Range Scans (Redis yes, but limited) |
| **Search** | Inverted Index | Elasticsearch, Solr | AP | Full-text search, Logging (ELK) | Primary Store (Data Loss risk), Updates |
| **Graph** | Nodes & Edges | Neo4j, Neptune | CP/AP | Social Networks, Fraud Detection, Recommendations | General purpose storage |
| **Time Series** | Arrays of Time-Value | Prometheus, InfluxDB | AP | Metrics, Monitoring | User Data |

**Пример выбора базы данных:**

```python
class DatabaseSelector:
    """Помощник для выбора базы данных."""
    
    def select(self, requirements):
        """Выбор базы на основе требований."""
        score = {}
        
        # Оцениваем каждую базу
        databases = {
            'PostgreSQL': self.score_postgres(requirements),
            'MongoDB': self.score_mongo(requirements),
            'Cassandra': self.score_cassandra(requirements),
            'Redis': self.score_redis(requirements),
            'Elasticsearch': self.score_elasticsearch(requirements),
        }
        
        # Возвращаем лучший вариант
        best = max(databases.items(), key=lambda x: x[1])
        return best[0], best[1]
    
    def score_postgres(self, req):
        """Оценка PostgreSQL."""
        score = 0
        if req.get('needs_transactions'):
            score += 10
        if req.get('needs_joins'):
            score += 10
        if req.get('structured_data'):
            score += 8
        if req.get('write_heavy'):
            score -= 5
        return score
    
    def score_mongo(self, req):
        """Оценка MongoDB."""
        score = 0
        if req.get('unstructured_data'):
            score += 10
        if req.get('horizontal_scaling'):
            score += 8
        if req.get('needs_joins'):
            score -= 5
        return score

# Пример использования

selector = DatabaseSelector()
requirements = {
    'needs_transactions': True,
    'needs_joins': True,
    'structured_data': True,
    'write_heavy': False
}

db, score = selector.select(requirements)
print(f"Recommended: {db} (score: {score})")
```

---

## 2. Workload Analysis: OLTP vs OLAP

Первый вопрос, который вы должны задать: "Как мы будем читать данные?".

### 2.1 OLTP (Online Transaction Processing)

*   **Сценарий**: Юзер логинится, кладет товар в корзину, платит.

*   **Паттерн**: Много маленьких чтений/записей по ID (Random IO).

*   **Требования**: ACID, Low Latency (<10ms).

*   **Storage**: Row-Oriented (строка лежит целиком).

*   **Выбор**: PostgreSQL, MySQL, DynamoDB.

### 2.2 OLAP (Online Analytical Processing)

*   **Сценарий**: Аналитик строит отчет "Средний чек по регионам за год".

*   **Паттерн**: Сканирование миллионов строк, но всего пары колонок (Sequential IO).

*   **Требования**: Throughput (GB/s).

*   **Storage**: **Column-Oriented**. Данные хранятся по колонкам (все цены рядом, все даты рядом). Это позволяет сжимать данные в 10 раз (RLE) и сканировать только нужное.

*   **Выбор**: ClickHouse, Snowflake, Google BigQuery, Redshift.

**Anti-Pattern**: Делать аналитику на OLTP базе (`SELECT SUM` на проде). Вы положите базу и заблокируете продажи. Используйте ETL, чтобы переливать данные в Data Warehouse.

**Сравнение Row vs Column Storage:**

```python
# Row-Oriented (OLTP)
# Таблица в памяти:
# Row 1: [id=1, name="Alice", age=25, city="NYC", salary=50000]
# Row 2: [id=2, name="Bob", age=30, city="LA", salary=60000]
# Row 3: [id=3, name="Charlie", age=35, city="NYC", salary=70000]

# Запрос: SELECT AVG(salary) WHERE city="NYC"
# Нужно прочитать ВСЕ колонки всех строк, даже если нужна только salary

# Column-Oriented (OLAP)
# Хранение по колонкам:
# id:    [1, 2, 3]
# name:  ["Alice", "Bob", "Charlie"]
# age:   [25, 30, 35]
# city:  ["NYC", "LA", "NYC"]
# salary: [50000, 60000, 70000]

# Запрос: SELECT AVG(salary) WHERE city="NYC"
# Читаем только колонки city и salary!
# city: ["NYC", "LA", "NYC"] -> индексы [0, 2]
# salary: [50000, 60000, 70000] -> берем [0, 2] -> AVG(50000, 70000) = 60000

class ColumnStore:
    """Упрощенная реализация Column-Oriented хранилища."""
    
    def __init__(self):
        self.columns = {}  # column_name -> [values]
        self.row_count = 0
    
    def insert(self, row):
        """Вставка строки (разбиваем на колонки)."""
        for col, val in row.items():
            if col not in self.columns:
                self.columns[col] = []
            self.columns[col].append(val)
        self.row_count += 1
    
    def query_avg(self, column, where_column=None, where_value=None):
        """Запрос AVG с фильтром."""
        if where_column:
            # Получаем индексы строк, удовлетворяющих условию
            indices = [
                i for i, val in enumerate(self.columns[where_column])
                if val == where_value
            ]
            # Берем значения из нужной колонки только для этих индексов
            values = [self.columns[column][i] for i in indices]
        else:
            values = self.columns[column]
        
        return sum(values) / len(values) if values else 0

# Пример

store = ColumnStore()
store.insert({'id': 1, 'name': 'Alice', 'city': 'NYC', 'salary': 50000})
store.insert({'id': 2, 'name': 'Bob', 'city': 'LA', 'salary': 60000})
store.insert({'id': 3, 'name': 'Charlie', 'city': 'NYC', 'salary': 70000})

avg_salary = store.query_avg('salary', where_column='city', where_value='NYC')
print(f"Average salary in NYC: {avg_salary}")  # 60000
```

**ETL Pipeline пример:**

```python
class ETLPipeline:
    """ETL из OLTP в OLAP."""
    
    def __init__(self, oltp_db, olap_db):
        self.oltp_db = oltp_db  # PostgreSQL
        self.olap_db = olap_db   # ClickHouse
    
    def extract(self, table, last_sync_time):
        """Извлечение данных из OLTP."""
        query = f"""
            SELECT * FROM {table}
            WHERE updated_at > %s
        """
        return self.oltp_db.execute(query, (last_sync_time,))
    
    def transform(self, rows):
        """Трансформация данных."""
        # Денормализация, агрегация, очистка
        transformed = []
        for row in rows:
            # Пример: объединение связанных таблиц
            transformed_row = {
                'order_id': row['id'],
                'customer_name': row['customer_name'],
                'product_name': row['product_name'],
                'total': row['quantity'] * row['price'],
                'date': row['created_at'].date()
            }
            transformed.append(transformed_row)
        return transformed
    
    def load(self, table, rows):
        """Загрузка в OLAP."""
        # Batch insert для производительности
        self.olap_db.batch_insert(table, rows)
    
    def run(self, table):
        """Запуск ETL."""
        last_sync = self.get_last_sync_time(table)
        rows = self.extract(table, last_sync)
        transformed = self.transform(rows)
        self.load(f"{table}_analytics", transformed)
        self.update_last_sync_time(table)
```

---

## 3. Polyglot Persistence

Идея "Одна база для всего" (Golden Hammer) мертва.
Современная архитектура использует **Polyglot Persistence**: разные базы для разных микросервисов.

### Пример Архитектуры Uber-like

1.  **User Service**: PostgreSQL. (Нужны транзакции, строгая схема).
2.  **Driver Location**: Redis (Geospatial). (Нужна скорость, потеря координат за секунду не страшно).
3.  **Trip History**: Cassandra. (Миллиарды записей, пишем один раз, никогда не меняем).
4.  **Invoices**: PostgreSQL (или Blob Storage PDF).
5.  **Search**: Elasticsearch (найти "поездка в аэропорт").
6.  **Analytics**: ClickHouse (куда ездят чаще всего?).

**Реализация Polyglot Persistence:**

```python
class PolyglotService:
    """Сервис с несколькими базами данных."""
    
    def __init__(self):
        self.postgres = PostgresClient()  # User data
        self.redis = RedisClient()       # Driver locations
        self.cassandra = CassandraClient()  # Trip history
        self.elasticsearch = ElasticsearchClient()  # Search
        self.clickhouse = ClickHouseClient()  # Analytics
    
    def create_user(self, user_data):
        """Создание пользователя."""
        # Пишем в PostgreSQL (транзакции, ACID)
        user_id = self.postgres.insert('users', user_data)
        
        # Индексируем в Elasticsearch для поиска
        self.elasticsearch.index('users', {
            'id': user_id,
            'name': user_data['name'],
            'email': user_data['email']
        })
        
        return user_id
    
    def update_driver_location(self, driver_id, lat, lon):
        """Обновление местоположения водителя."""
        # Redis Geospatial для быстрого поиска ближайших водителей
        self.redis.geoadd('drivers:locations', lon, lat, driver_id)
        
        # TTL для автоматического удаления старых локаций
        self.redis.expire(f'driver:{driver_id}:location', 60)  # 60 секунд
    
    def find_nearby_drivers(self, lat, lon, radius_km=5):
        """Поиск ближайших водителей."""
        # Redis GEORADIUS - O(N+log(M)) сложность
        driver_ids = self.redis.georadius(
            'drivers:locations',
            lon, lat, radius_km,
            unit='km'
        )
        return driver_ids
    
    def save_trip(self, trip_data):
        """Сохранение поездки."""
        # Cassandra для истории (write-heavy, time-series)
        trip_id = self.cassandra.insert('trips', {
            'trip_id': trip_data['id'],
            'user_id': trip_data['user_id'],
            'driver_id': trip_data['driver_id'],
            'start_time': trip_data['start_time'],
            'end_time': trip_data['end_time'],
            'distance': trip_data['distance'],
            'price': trip_data['price']
        })
        
        # ClickHouse для аналитики (агрегации)
        self.clickhouse.insert('trips_analytics', {
            'trip_id': trip_data['id'],
            'date': trip_data['start_time'].date(),
            'city': trip_data['city'],
            'distance': trip_data['distance'],
            'price': trip_data['price']
        })
        
        return trip_id
    
    def search_trips(self, query):
        """Поиск поездок по тексту."""
        # Elasticsearch для полнотекстового поиска
        results = self.elasticsearch.search('trips', {
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['pickup_address', 'dropoff_address', 'notes']
                }
            }
        })
        return results
```

---

## 4. Migration Strategy: Zero Downtime

Бизнес вырос. PostgreSQL перестал держать нагрузку. Мы хотим переехать на Cassandra.
Как это сделать, не останавливая сервис?
Паттерн **Dual Write**.

### Phase 1: Dual Write (Dark Launch)

Приложение пишет и в PG, и в Cass.

*   Читаем только из PG.
*   Ошибки записи в Cass игнорируем (логируем).

**Реализация Dual Write:**

```python
class DualWriteService:
    """Сервис с двойной записью для миграции."""
    
    def __init__(self, primary_db, new_db):
        self.primary_db = primary_db  # PostgreSQL
        self.new_db = new_db          # Cassandra
        self.read_from_primary = True
    
    def write(self, key, value):
        """Запись в обе базы."""
        # Всегда пишем в Primary
        try:
            self.primary_db.set(key, value)
        except Exception as e:
            raise Exception(f"Primary write failed: {e}")
        
        # Пробуем писать в New (игнорируем ошибки)
        try:
            self.new_db.set(key, value)
        except Exception as e:
            # Логируем, но не падаем
            print(f"Warning: New DB write failed: {e}")
    
    def read(self, key):
        """Чтение из Primary или New в зависимости от фазы."""
        if self.read_from_primary:
            return self.primary_db.get(key)
        else:
            return self.new_db.get(key)
    
    def verify(self, key):
        """Проверка согласованности данных."""
        primary_val = self.primary_db.get(key)
        new_val = self.new_db.get(key)
        
        if primary_val != new_val:
            print(f"⚠️ Mismatch for {key}: Primary={primary_val}, New={new_val}")
            return False
        return True
```

### Phase 2: Backfill (Historical Data)

Запускаем скрипт, который копирует старые данные из PG в Cass.
Это сложно, так как данные меняются.

**Backfill скрипт:**

```python
class BackfillScript:
    """Скрипт для копирования исторических данных."""
    
    def __init__(self, source_db, target_db):
        self.source_db = source_db
        self.target_db = target_db
    
    def backfill_table(self, table_name, batch_size=1000):
        """Копирование таблицы батчами."""
        offset = 0
        total_copied = 0
        
        while True:
            # Читаем батч из source
            rows = self.source_db.query(
                f"SELECT * FROM {table_name} LIMIT %s OFFSET %s",
                (batch_size, offset)
            )
            
            if not rows:
                break
            
            # Пишем батч в target
            self.target_db.batch_insert(table_name, rows)
            
            total_copied += len(rows)
            offset += batch_size
            
            print(f"Copied {total_copied} rows...")
            
            # Небольшая задержка, чтобы не перегрузить систему
            time.sleep(0.1)
        
        print(f"Backfill complete: {total_copied} rows copied")
```

### Phase 3: Compare (Verification)

Приложение читает из PG и из Cass.
Сравнивает результаты.
Если есть разница — **Alarm**. Чиним баги миграции.

**Verification Service:**

```python
class VerificationService:
    """Сервис для проверки согласованности."""
    
    def __init__(self, primary_db, new_db):
        self.primary_db = primary_db
        self.new_db = new_db
        self.mismatches = []
    
    def verify_all(self, table_name):
        """Проверка всех записей."""
        primary_rows = self.primary_db.get_all(table_name)
        
        for row in primary_rows:
            key = row['id']
            primary_val = row
            new_val = self.new_db.get(table_name, key)
            
            if primary_val != new_val:
                self.mismatches.append({
                    'key': key,
                    'primary': primary_val,
                    'new': new_val
                })
        
        if self.mismatches:
            print(f"❌ Found {len(self.mismatches)} mismatches!")
            return False
        else:
            print("✅ All records match!")
            return True
```

### Phase 4: Switch Read

Начинаем читать из Cassandra. PG остается как бэкап (пишем в него, но не читаем).

### Phase 5: Stop Write

Перестаем писать в PG. Удаляем код PG.

---

## 5. Cost Analysis (Деньги счет любят)

Архитекторам часто приходится оправдывать бюджет.

### 5.1 Provisioned (EC2 / RDS)

Вы платите за инстанс 24/7. Даже если он простаивает ночью.

*   Хорошо для предсказуемой, постоянной нагрузки.
*   Дешевле на масштабе.

### 5.2 Serverless (DynamoDB / Aurora Serverless)

Вы платите за Request (Read/Write Unit).

*   Если трафика нет — цена 0.
*   Если хабраэффект — цена космос.
*   Хорошо для стартапов и рваной нагрузки.

**Кейс**: Стартап начал на DynamoDB ($10/mo). Вырос. Счет стал $10,000/mo. Переехали на ScyllaDB (EC2) -> $1,000/mo.
Serverless удобен, но дорог на большом объеме.

---

## 6. Glossary

*   **Polyglot Persistence**: Использование нескольких типов БД.

*   **ETL (Extract, Transform, Load)**: Процесс выгрузки данных из OLTP в OLAP.

*   **CDC (Change Data Capture)**: Механизм подписки на логи базы (WAL) для репликации данных в другую систему (напр. Debezium: Postgres -> Kafka -> Elastic).

*   **Columnar Store**: Хранение данных по колонкам (Parquet, ORC).

*   **HTAP (Hybrid Transactional/Analytical Processing)**: Новые базы (TiDB, Singlestore), пытающиеся уметь и OLTP и OLAP.

*   **NewSQL**: Реляционные базы, которые масштабируются горизонтально (CockroachDB, Spanner, VoltDB).

*   **Vendor Lock-in**: Зависимость от облачного провайдера (DynamoDB привязывает вас к AWS).

---

## 📚 Appendix A: Troubleshooting "Cloud Bills"

### A.1 Symptom: DynamoDB Cost Blowup

**Симптом**: Счет за DynamoDB вырос в 10 раз.
**Причина**: Scan Operations. Разработчик сделал `scan()` всей таблицы вместо `query()` по индексу. В DynamoDB вы платите за каждый прочитанный байт, даже если вы его отфильтровали на стороне базы.
**Лечение**: Запретить Scan в коде. Использовать Global Secondary Indexes (GSI).

### A.2 Symptom: Data Gravity

**Симптом**: Вы хотите переехать из AWS в Google Cloud, но Egress Traffic (выкачка 1 Петабайта) стоит миллион долларов.
**Суть**: Данные имеют "гравитацию". Чем их больше, тем сложнее их сдвинуть. Думайте об этом *до* накопления петабайтов.

---

## 📚 Appendix B: Historical Context

### 2009: NoSQL Meetup

Термин "NoSQL" (Not Only SQL) популяризировал Йохан Оскарссон на митапе в Сан-Франциско.
Это была реакция на доминирование Oracle/MySQL, которые не могли скейлиться на кластеры (Web 2.0 scale).
Тогда появились: MongoDB, Cassandra, HBase, Redis.

### 2010s: The Hype Cycle

Все бросились переписывать всё на Mongo.
Потом поняли, что потеряли транзакции и JOIN-ы. (Mongo долго не имела транзакций).
Наступило "похмелье".

### 2020s: Convergence (NewSQL)

Старые базы добавили JSON (Postgres JSONB).
Новые базы добавили SQL (CockroachDB — это KV store, который говорит на SQL).
Границы стерлись. Сейчас тренд на надежность (SQL, ACID) + масштабируемость.

---

## 📚 Appendix C: FAQ (Часто задаваемые вопросы)

**Q1: Какой Stack выбрать для стартапа?**
**A**: **PostgreSQL**.
Серьезно. Postgres умеет ВСЁ:

*   Реляционные данные (SQL).
*   Документы (JSONB работает быстрее Mongo в некоторых кейсах).
*   Поиск (Full Text Search tsvector).
*   Гео (PostGIS).
*   Очереди (через `SKIP LOCKED`).
Используйте Postgres, пока не упретесь в потолок. Это называется "Boring Technology Stack".

**Q2: Что не так с ORM (Hibernate, Prisma)?**
**A**:
*   N+1 Problem: ORM делает цикл запросов вместо одного JOIN.
*   Они прячут сложность, и вы не понимаете, почему тормозит.
Используйте ORM для простых CRUD, но пишите Raw SQL для сложной аналитики.

**Q3: Зачем нужен GraphQL?**
**A**: Чтобы фронтендер мог забрать данные из User, Order и Product одним запросом, не прося бэкендера писать новый эндпоинт. Но это перекладывает сложность Join-ов на Runtime. Осторожно с N+1!

**Q4: Почему Uber перешел с Postgres на MySQL (Schemaless)?**
**A**: (Знаменитая статья Uber Eng). Они уперлись в проблему Write Amplification в Postgres (из-за того, как PG обновляет индексы при MVCC). Для их специфичного use-case (Write heavy updates) MySQL + InnoDB работал лучше. Но это уровень Uber. Не повторяйте это дома без причины.

**Q5: Что такое "Serverless Database"?**
**A**: Это когда база сама скейлится в 0, когда нет нагрузки, и поднимает ресурсы при нагрузке. Пример: Aurora Serverless, CockroachDB Serverless, Neon (Postgres separation of compute/storage).

---

## 💡 Key Takeaways

1.  **There is no Silver Bullet**: Идеальной базы нет.
2.  **Start with SQL**: Реляционная модель самая гибкая. Денормализация (NoSQL) — это оптимизация, которую надо заслужить.
3.  **Read vs Write**: Поймите свой профиль нагрузки.
4.  **Polyglot is Normal**: Современные системы используют 3-5 разных баз данных для разных задач.
5.  **Migration is Hard**: Планируйте миграцию заранее, используйте Dual Write и Verification.

---

## 🚀 Next Steps

**Практика:**

1.  Возьмите свой пет-проект.
2.  Нарисуйте схему данных в SQL.
3.  Попробуйте переложить её на Cassandra (Wide Column). Осознайте боль отсутствия JOIN-ов. Поймите, что вам придется дублировать данные (Data Denormalization).

В следующем модуле мы рассмотрим структуры данных, которые **врут**, но экономят память. [Approximate Data Structures](../15_Approximate_Data_Structures/).



