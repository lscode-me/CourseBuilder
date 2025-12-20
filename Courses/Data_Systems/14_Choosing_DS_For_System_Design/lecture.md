# Выбор Data Store для System Design
## OLTP, OLAP, Time Series и Specialized DBs

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать разницу между B-tree и LSM-tree (Модуль 2)
- Понимать CAP теорему (Модуль 3)
- Знать основные паттерны доступа (Read/Write Heavy)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать OLTP и OLAP нагрузки
- Выбирать базу данных под конкретную задачу (SQL vs NoSQL)
- Понимать, когда нужны специализированные БД (Time Series, Search Engines)
- Применять метод "Access Pattern Analysis" для выбора хранилища

---

## 1. Методология выбора БД

На System Design интервью (и в жизни) нельзя просто сказать "Я возьму MongoDB, потому что она веб-масштабируемая".
Выбор базы данных диктуется **Паттернами Доступа (Access Patterns)**.

**Вопросы, которые нужно задать:**

1.  **Read vs Write**: Какое соотношение? (100:1 или 1:1?)
2.  **Latency vs Throughput**: Нам важно отвечать за 5 мс или перелопатить терабайт за час?
3.  **Consistency**: Нужны ли транзакции? (Финансы vs Комментарии).
4.  **Schema**: Данные меняются часто? (JSON vs Table).

---

## 2. SQL vs NoSQL: Конец холивара

### 2.1 SQL (Relational / RDBMS)

*   **Примеры**: PostgreSQL, MySQL, Oracle.

*   **Основа**: B-Tree, ACID, Normalized Data.

*   **Когда брать**:
    *   Структурированные данные (Пользователи, Заказы).
    *   Нужны транзакции и JOINs.
    *   **Default Choice**: Если не знаете, что выбрать — берите Postgres. Он умеет почти всё (включая JSONB и Geo).

### 2.2 NoSQL (Non-Relational)

Это зонтичный термин для всего, что не SQL. Делится на категории.

#### A. Document Stores (MongoDB, Couchbase)

*   **Основа**: B-Tree (обычно), JSON documents.

*   **Когда брать**:
    *   Гибкая схема (CMS, профили пользователей с разными полями).
    *   Быстрая разработка (не нужно мигрировать схему).
    *   Не нужны сложные JOINs.

#### B. Key-Value Stores (Redis, DynamoDB)

*   **Основа**: Hash Map.

*   **Когда брать**:
    *   Простейший доступ по ID (Session Store, Carts, Preferences).
    *   High Throughput / Low Latency.
    *   Горизонтальное масштабирование (DynamoDB).

#### C. Wide-Column Stores (Cassandra, HBase)

*   **Основа**: LSM-Tree, SSTables.

*   **Когда брать**:
    *   **Extremely Write Heavy** (IoT, Logs, Metrics).
    *   Петабайты данных.
    *   Линейная масштабируемость.
    *   *Минус*: Ограниченные возможности запросов (только по Partition Key).

#### D. Graph Databases (Neo4j, Amazon Neptune)

*   **Основа**: Adjacency Matrix/Lists.

*   **Когда брать**:
    *   Глубокие связи (Social Networks, Fraud Detection, Recommendation).
    *   Если SQL запросы требуют 5+ JOINs.

---

## 3. OLTP vs OLAP

Это самое фундаментальное разделение нагрузок.

### 3.1 OLTP (Online Transaction Processing)

*   **Суть**: Интерактивная работа с пользователем.

*   **Запросы**: "Дай мне заказ ID=123", "Обнови статус на Delivered".

*   **Характеристики**: Много мелких запросов, Random Access, важна Latency.

*   **БД**: Postgres, MySQL, DynamoDB.

*   **Storage**: Row-Oriented (строка хранится целиком).

### 3.2 OLAP (Online Analytical Processing)

*   **Суть**: Аналитика, отчеты для бизнеса.

*   **Запросы**: "Посчитай средний чек по всем магазинам за год".

*   **Характеристики**: Сканирование миллионов строк, Aggregations, важен Throughput.

*   **БД**: ClickHouse, Snowflake, Google BigQuery, Redshift.

*   **Storage**: **Column-Oriented** (колонки хранятся отдельно). Это позволяет читать только нужные колонки и отлично сжимать данные.

**Пример Column-Oriented**:
В таблице Users есть поля `Name, Age, City`. Нужно посчитать средний `Age`.
В Row-store придется прочитать все строки целиком (с именами и городами).
В Column-store читаем с диска только файл `Age`. Экономия I/O в 100 раз.

---

## 4. Специализированные БД

### 4.1 Search Engines (Elasticsearch, Solr)

*   **Задача**: Полнотекстовый поиск ("найти слово 'котик' в описании").

*   **Структура**: **Inverted Index** (Обратный индекс).
    *   `"котик" -> [Doc1, Doc5]`
    *   `"собака" -> [Doc2, Doc5]`
*   **Когда использовать**: Поиск на сайте, автодополнение, фильтрация логов (ELK Stack).
*   *Note*: Обычные БД с `LIKE %...%` убивают перформанс.

### 4.2 Time Series DB (Prometheus, InfluxDB, TimescaleDB)

*   **Задача**: Хранение метрик (CPU usage, Temperature) во времени.

*   **Особенности**:
    *   Write-Heavy (Append-only).
    *   Read: Aggregations over time window (avg за 5 минут).
    *   Automatic Data Retention (удалять старое).
    *   Compression (Delta-of-delta encoding).

---

## 5. Polyglot Persistence

В современной архитектуре редко используют одну БД.
Используют **Polyglot Persistence** — каждому сервису своя БД.

**Пример E-commerce Архитектуры:**

1.  **Product Catalog**: MongoDB (JSON, гибкая схема товаров).
2.  **Transactions/Orders**: Postgres (ACID, деньги).
3.  **Search**: Elasticsearch (быстрый поиск по каталогу).
4.  **Cart/Session**: Redis (скорость, исчезнет — не критично).
5.  **Analytics**: ClickHouse/BigQuery (сливаем данные из всех источников для отчетов).
6.  **Recommendation**: Neo4j (граф "люди, купившие это, купили то").

---

## 6. Демонстрация: Выбор БД для "Uber-like" сервиса

**Задача**: Спроектировать Backend для такси.
1.  **Driver Location Updates**: Водитель шлет координаты раз в 5 сек.
    *   Миллионы записей в минуту. Write Heavy.
    *   Нужен Geospatial Index.
    *   *Выбор*: **Redis Geo** (для текущих позиций, быстро меняется) или **Cassandra/Scylla** (для истории трека).
2.  **User Profile/Payments**:
    *   Критические данные. ACID.
    *   *Выбор*: **PostgreSQL**.
3.  **Matching (Find nearest driver)**:
    *   Geospatial Query.
    *   *Выбор*: **PostGIS** (расширение Postgres) или Redis Geo.
4.  **Trip History (Archive)**:
    *   Write once, read rarely. Cold storage.
    *   *Выбор*: **S3** (дешево) или Cassandra.

---

## 💡 Key Takeaways

- Не выбирайте БД по хайпу. Анализируйте паттерны доступа.
- **Postgres** — швейцарский нож. Начинайте с него, если нет явных причин для NoSQL.

- **Row-Store (OLTP)** хорош для транзакций, **Column-Store (OLAP)** — для аналитики.

- **LSM-tree** базы (Cassandra) нужны для интенсивной записи.
- Используйте **Elasticsearch** для поиска, не мучайте базу данных.

---

## 🚀 Next Steps

**Related Modules:**

- [Approximate Data Structures](../15_Approximate_Data_Structures/) — как сэкономить память, если точность 100% не нужна.
- [Case Studies](../16_Case_Studies/) — как все это объединить в реальных системах.

**Practice Ideas:**

1. Попробуйте в Postgres создать таблицу на 10 млн строк и посчитать `AVG()`. Потом сделайте то же в ClickHouse. Сравните время.
2. Поднимите Elasticsearch и загрузите туда книги. Попробуйте Fuzzy Search.
3. Спроектируйте базу для Messenger (WhatsApp). Где хранить сообщения? (Подсказка: HBase/Cassandra).

---

