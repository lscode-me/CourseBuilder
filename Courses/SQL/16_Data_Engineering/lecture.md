# SQL в Data Engineering
## ETL и ELT, SQL как слой трансформации, dbt, проверки качества данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу с агрегациями и JOIN
- Знать основы проектирования схем
- Иметь представление о ETL процессах

**Recommended prior modules:**

- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY
- [15_Analytics](../15_Analytics/) — SQL в аналитике

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать ETL и ELT подходы
- Использовать SQL как слой трансформации данных
- Понимать концепцию dbt (data build tool)
- Создавать проверки качества данных на SQL
- Применять SQL в data engineering пайплайнах

---

## 1. ETL vs ELT

### 1.1 ETL (Extract, Transform, Load)

**Традиционный подход:**

1. **Extract** — извлечение из источников
2. **Transform** — трансформация (часто на отдельном сервере)
3. **Load** — загрузка в хранилище

**Характеристики:**

- Трансформация до загрузки
- Требует промежуточное хранилище
- Сложнее масштабировать

### 1.2 ELT (Extract, Load, Transform)

**Современный подход:**

1. **Extract** — извлечение
2. **Load** — загрузка в хранилище (raw данные)
3. **Transform** — трансформация в хранилище (SQL)

**Характеристики:**

- Трансформация после загрузки
- Использует мощь хранилища данных
- Проще масштабировать
- SQL как язык трансформации

**Пример ELT:**

```sql

-- 1. Load: загрузка raw данных
CREATE TABLE raw_orders AS SELECT * FROM source_system.orders;

-- 2. Transform: SQL трансформация
CREATE TABLE cleaned_orders AS
SELECT 
    id,
    user_id,
    amount,
    order_date,
    CASE 
        WHEN status = 'completed' THEN 'success'
        ELSE 'pending'
    END AS normalized_status
FROM raw_orders
WHERE amount > 0;  -- Фильтрация
```

---

## 2. SQL как слой трансформации

### 2.1 Трансформации данных

**Типичные трансформации:**

- Очистка данных (удаление NULL, дубликатов)
- Нормализация (приведение к стандарту)
- Агрегация (суммы, средние)
- Обогащение (JOIN с другими таблицами)

**Пример:**

```sql

-- Трансформация: очистка и обогащение
CREATE TABLE transformed_sales AS
SELECT 
    o.id,
    u.name AS customer_name,
    p.name AS product_name,
    o.amount,
    o.quantity,
    o.amount * o.quantity AS total,
    DATE(o.order_date) AS sale_date
FROM raw_orders o
LEFT JOIN users u ON o.user_id = u.id
LEFT JOIN products p ON o.product_id = p.id
WHERE o.amount IS NOT NULL
  AND o.quantity > 0
  AND o.order_date >= '2024-01-01';
```

### 2.2 Инкрементальные трансформации

**Обновление только новых данных:**

```sql

-- Добавление только новых записей
INSERT INTO transformed_sales
SELECT ...
FROM raw_orders
WHERE order_date > (SELECT MAX(sale_date) FROM transformed_sales);
```

---

## 3. dbt (data build tool)

### 3.1 Что такое dbt

**dbt** — инструмент для трансформации данных с помощью SQL.

**Особенности:**

- ✅ SQL как код (version control)
- ✅ Модульность (модели, макросы)
- ✅ Тестирование данных
- ✅ Документация

### 3.2 Структура dbt проекта

```

models/
  staging/
    stg_orders.sql
    stg_users.sql
  marts/
    dim_customers.sql
    fact_sales.sql
```

**Пример модели:**

```sql

-- models/staging/stg_orders.sql
SELECT 
    id,
    user_id,
    amount,
    order_date
FROM {{ source('raw', 'orders') }}
WHERE amount > 0;
```

### 3.3 Тестирование в dbt

**Проверки качества данных:**

```sql

-- models/schema.yml
models:
  - name: stg_orders
    columns:
      - name: id
        tests:
          - unique
          - not_null
      - name: amount
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
```

---

## 4. Проверки качества данных

### 4.1 SQL проверки

**Проверка на дубликаты:**

```sql

-- Найти дубликаты
SELECT 
    user_id,
    order_date,
    COUNT(*) AS duplicate_count
FROM orders
GROUP BY user_id, order_date
HAVING COUNT(*) > 1;
```

**Проверка на NULL:**

```sql

-- Найти записи с NULL в критичных полях
SELECT * FROM orders
WHERE user_id IS NULL 
   OR amount IS NULL;
```

**Проверка диапазонов:**

```sql

-- Найти некорректные значения
SELECT * FROM orders
WHERE amount < 0 
   OR amount > 1000000;
```

### 4.2 Автоматизация проверок

**Создание таблицы с результатами проверок:**

```sql

CREATE TABLE data_quality_checks (
    check_date TIMESTAMP,
    check_name VARCHAR(100),
    status VARCHAR(20),
    error_count INTEGER
);

-- Запуск проверок
INSERT INTO data_quality_checks
SELECT 
    CURRENT_TIMESTAMP,
    'duplicate_orders',
    CASE WHEN COUNT(*) > 0 THEN 'FAIL' ELSE 'PASS' END,
    COUNT(*)
FROM (
    SELECT user_id, order_date
    FROM orders
    GROUP BY user_id, order_date
    HAVING COUNT(*) > 1
) duplicates;
```

---

## 5. Практические примеры

### 5.1 ETL пайплайн на SQL

```sql

-- 1. Extract & Load (raw данные)
CREATE TABLE raw_orders AS 
SELECT * FROM external_source.orders;

-- 2. Transform (очистка)
CREATE TABLE cleaned_orders AS
SELECT 
    id,
    user_id,
    COALESCE(amount, 0) AS amount,
    order_date
FROM raw_orders
WHERE order_date IS NOT NULL;

-- 3. Transform (обогащение)
CREATE TABLE enriched_orders AS
SELECT 
    o.*,
    u.country,
    u.segment
FROM cleaned_orders o
LEFT JOIN users u ON o.user_id = u.id;

-- 4. Transform (агрегация)
CREATE TABLE daily_sales AS
SELECT 
    DATE(order_date) AS sale_date,
    country,
    SUM(amount) AS total_sales,
    COUNT(*) AS order_count
FROM enriched_orders
GROUP BY DATE(order_date), country;
```

### 5.2 Инкрементальная загрузка

```sql

-- Загрузка только новых данных
INSERT INTO transformed_sales
SELECT ...
FROM raw_orders
WHERE order_date > (
    SELECT COALESCE(MAX(sale_date), '1900-01-01')
    FROM transformed_sales
);
```

### 5.3 Обработка обновлений (UPSERT)

**Обновление существующих и вставка новых:**

```sql

-- PostgreSQL: ON CONFLICT
INSERT INTO transformed_sales (id, sale_date, amount)
SELECT id, sale_date, amount
FROM raw_orders
ON CONFLICT (id) 
DO UPDATE SET
    sale_date = EXCLUDED.sale_date,
    amount = EXCLUDED.amount,
    updated_at = CURRENT_TIMESTAMP;
```

---

## 6. Оркестрация пайплайнов

### 6.1 SQL в Airflow

**Airflow DAG с SQL задачами:**

```python

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

dag = DAG('etl_pipeline', start_date=datetime(2024, 1, 1))

extract_task = PostgresOperator(
    task_id='extract_raw_data',
    postgres_conn_id='source_db',
    sql='SELECT * FROM orders WHERE order_date = CURRENT_DATE - 1',
    dag=dag
)

transform_task = PostgresOperator(
    task_id='transform_data',
    postgres_conn_id='warehouse_db',
    sql='''
        INSERT INTO transformed_sales
        SELECT 
            id,
            DATE(order_date) AS sale_date,
            amount,
            user_id
        FROM staging.orders
        WHERE amount > 0
    ''',
    dag=dag
)

extract_task >> transform_task
```

### 6.2 SQL в Prefect

**Prefect flow с SQL:**

```python

from prefect import flow, task
from prefect_sqlalchemy import SqlAlchemyConnector

@task
def transform_data():
    with SqlAlchemyConnector.load("warehouse") as database:
        database.execute(
            """
            INSERT INTO transformed_sales
            SELECT * FROM staging.orders
            WHERE amount > 0
            """
        )

@flow
def etl_flow():
    transform_data()

if __name__ == "__main__":
    etl_flow()
```

---

## 7. Продвинутые трансформации

### 7.1 Дедупликация данных

**Удаление дубликатов:**

```sql

-- Найти дубликаты
WITH duplicates AS (
    SELECT 
        id,
        ROW_NUMBER() OVER (
            PARTITION BY email, order_date, amount 
            ORDER BY created_at DESC
        ) AS rn
    FROM raw_orders
)
DELETE FROM raw_orders
WHERE id IN (
    SELECT id FROM duplicates WHERE rn > 1
);
```

### 7.2 Обогащение данных

**Добавление данных из других источников:**

```sql

-- Обогащение заказов данными о пользователях
CREATE TABLE enriched_orders AS
SELECT 
    o.id,
    o.order_date,
    o.amount,
    u.country,
    u.segment,
    u.registration_date,
    CASE 
        WHEN u.registration_date > o.order_date - INTERVAL '30 days' 
        THEN 'new_customer'
        ELSE 'returning_customer'
    END AS customer_type
FROM raw_orders o
LEFT JOIN users u ON o.user_id = u.id;
```

### 7.3 Нормализация данных

**Приведение к стандартному формату:**

```sql

-- Нормализация email
UPDATE users
SET email = LOWER(TRIM(email))
WHERE email IS NOT NULL;

-- Нормализация телефонов
UPDATE users
SET phone = REGEXP_REPLACE(phone, '[^0-9]', '', 'g')
WHERE phone IS NOT NULL;
```

### 7.4 Агрегация и сводные таблицы

**Создание агрегированных таблиц:**

```sql

-- Ежедневная статистика
CREATE TABLE daily_stats AS
SELECT 
    DATE(order_date) AS stat_date,
    COUNT(*) AS order_count,
    COUNT(DISTINCT user_id) AS unique_customers,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_order_value,
    MIN(amount) AS min_order,
    MAX(amount) AS max_order
FROM orders
GROUP BY DATE(order_date);
```

---

## 8. Качество данных

### 8.1 Проверка целостности

**Проверка внешних ключей:**

```sql

-- Найти "осиротевшие" записи
SELECT o.*
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;
```

### 8.2 Проверка бизнес-правил

**Валидация данных:**

```sql

-- Проверка бизнес-правил
WITH validation_errors AS (
    SELECT 
        id,
        'negative_amount' AS error_type
    FROM orders
    WHERE amount < 0
    
    UNION ALL
    
    SELECT 
        id,
        'future_date' AS error_type
    FROM orders
    WHERE order_date > CURRENT_DATE
    
    UNION ALL
    
    SELECT 
        id,
        'missing_required_field' AS error_type
    FROM orders
    WHERE user_id IS NULL OR amount IS NULL
)
SELECT * FROM validation_errors;
```

### 8.3 Автоматизация проверок

**Таблица результатов проверок:**

```sql

CREATE TABLE data_quality_checks (
    check_id SERIAL PRIMARY KEY,
    check_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    check_name VARCHAR(100),
    status VARCHAR(20),
    error_count INTEGER,
    error_details JSONB
);

-- Запуск проверок
INSERT INTO data_quality_checks (check_name, status, error_count)
SELECT 
    'duplicate_orders',
    CASE WHEN COUNT(*) > 0 THEN 'FAIL' ELSE 'PASS' END,
    COUNT(*)
FROM (
    SELECT user_id, order_date, amount
    FROM orders
    GROUP BY user_id, order_date, amount
    HAVING COUNT(*) > 1
) duplicates;
```

---

## 9. Оптимизация трансформаций

### 9.1 Параллельная обработка

**Партиционирование для параллелизма:**

```sql

-- Обработка по партициям
INSERT INTO transformed_sales_2024_01
SELECT * FROM raw_orders_2024_01
WHERE amount > 0;

INSERT INTO transformed_sales_2024_02
SELECT * FROM raw_orders_2024_02
WHERE amount > 0;
-- Можно выполнять параллельно
```

### 9.2 Batch обработка

**Обработка больших объёмов порциями:**

```sql

-- Обработка по батчам
DO $$
DECLARE
    batch_size INTEGER := 10000;
    offset_val INTEGER := 0;
BEGIN
    LOOP
        INSERT INTO transformed_sales
        SELECT * FROM raw_orders
        ORDER BY id
        LIMIT batch_size OFFSET offset_val;
        
        EXIT WHEN NOT FOUND;
        offset_val := offset_val + batch_size;
    END LOOP;
END $$;
```

### 9.3 Оптимизация JOIN

**Оптимизация больших JOIN:**

```sql

-- Создание индексов для JOIN
CREATE INDEX idx_orders_user_id ON raw_orders(user_id);
CREATE INDEX idx_users_id ON users(id);

-- Использование индексов в JOIN
SELECT 
    o.*,
    u.country,
    u.segment
FROM raw_orders o
INNER JOIN users u ON o.user_id = u.id;
```

---

## 💡 Key Takeaways

- **ETL** — трансформация до загрузки, **ELT** — трансформация после загрузки (SQL в хранилище)

- **SQL как слой трансформации** — очистка, нормализация, агрегация, обогащение

- **dbt** — инструмент для трансформации данных с помощью SQL, модульность, тестирование

- **Проверки качества данных** — дубликаты, NULL, диапазоны, автоматизация

- **Data Engineering** — SQL критичен для трансформации данных в пайплайнах

---

## 🚀 Next Steps

**Related Modules:**

- [15_Analytics](../15_Analytics/) — SQL в аналитике
- [18_System_Design](../18_System_Design/) — SQL как часть system design

**Practice Ideas:**

1. Создайте ETL/ELT пайплайн на SQL
2. Попрактикуйтесь с проверками качества данных
3. Изучите dbt и создайте простой проект
4. Реализуйте инкрементальную загрузку данных

**Going Deeper:**

- Изучите инструменты: dbt, Airflow, Prefect
- Изучите колоночные хранилища для аналитики
- Изучите streaming обработку данных

---

## 📚 Additional Resources

**Documentation:**

- [dbt Documentation](https://docs.getdbt.com/) — документация dbt
- [ELT vs ETL](https://www.getdbt.com/what-is-analytics-engineering/) — различия подходов

---


