# SQL в аналитике
## OLTP и OLAP, Fact и Dimension таблицы, Star и Snowflake схемы, SQL в BI

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу с JOIN и агрегациями
- Знать основы проектирования схем
- Иметь представление о различиях между операционными и аналитическими системами

**Recommended prior modules:**

- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY
- [06_Joins](../06_Joins/) — JOIN и связи между таблицами
- [08_Schema_Design](../08_Schema_Design/) — Проектирование схемы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать OLTP и OLAP системы
- Понимать концепцию Fact и Dimension таблиц
- Проектировать Star и Snowflake схемы
- Применять SQL для аналитических задач
- Понимать роль SQL в Business Intelligence

---

## 1. OLTP vs OLAP

### 1.1 OLTP (Online Transaction Processing)

**Операционные системы:**

- ✅ Много коротких транзакций
- ✅ Частые INSERT/UPDATE/DELETE
- ✅ Нормализованная схема
- ✅ Оптимизированы для записи

**Примеры:**

- Интернет-магазин (заказы, платежи)
- Банковские транзакции
- Системы бронирования

### 1.2 OLAP (Online Analytical Processing)

**Аналитические системы:**

- ✅ Много чтения, мало записи
- ✅ Сложные аналитические запросы
- ✅ Денормализованная схема
- ✅ Оптимизированы для чтения

**Примеры:**

- Data Warehouses
- Business Intelligence системы
- Аналитические отчёты

### 1.3 Сравнение

| Характеристика | OLTP | OLAP |
|----------------|------|------|
| Назначение | Операции | Аналитика |
| Схема | Нормализованная | Денормализованная |
| Операции | Много записи | Много чтения |
| Запросы | Простые, быстрые | Сложные, долгие |
| Данные | Текущие | Исторические |

---

## 2. Fact и Dimension таблицы

### 2.1 Fact таблицы

**Fact (Факт)** — таблица с измерениями и метриками.

**Характеристики:**

- Большое количество строк
- Содержит метрики (amount, quantity)
- Содержит ключи к Dimension таблицам
- Редко изменяется

**Пример:**

```sql
CREATE TABLE sales_fact (
    sale_id INTEGER PRIMARY KEY,
    date_id INTEGER,        -- FK to date_dimension
    product_id INTEGER,      -- FK to product_dimension
    customer_id INTEGER,     -- FK to customer_dimension
    amount DECIMAL(10, 2),   -- Метрика
    quantity INTEGER         -- Метрика
);
```

### 2.2 Dimension таблицы

**Dimension (Измерение)** — таблица с описательными данными.

**Характеристики:**

- Относительно небольшое количество строк
- Содержит атрибуты (названия, описания)
- Часто изменяется
- Используется для фильтрации и группировки

**Пример:**

```sql
CREATE TABLE product_dimension (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50)
);

CREATE TABLE customer_dimension (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    segment VARCHAR(50)
);
```

---

## 3. Star Schema (Звёздная схема)

### 3.1 Структура

**Star Schema** — одна Fact таблица в центре, окружённая Dimension таблицами.

```
        [Date Dimension]
              |
[Product Dimension] -- [Sales Fact] -- [Customer Dimension]
              |
        [Store Dimension]
```

**Пример:**

```sql
-- Fact таблица
CREATE TABLE sales_fact (
    sale_id INTEGER,
    date_id INTEGER,
    product_id INTEGER,
    customer_id INTEGER,
    store_id INTEGER,
    amount DECIMAL(10, 2),
    quantity INTEGER
);

-- Dimension таблицы
CREATE TABLE date_dimension (
    date_id INTEGER PRIMARY KEY,
    date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day_of_week VARCHAR(10)
);

CREATE TABLE product_dimension (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- Запрос
SELECT 
    d.year,
    p.category,
    SUM(s.amount) AS total_sales
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
JOIN product_dimension p ON s.product_id = p.product_id
GROUP BY d.year, p.category;
```

### 3.2 Преимущества

- ✅ Простая структура
- ✅ Быстрые запросы (меньше JOIN)
- ✅ Легко понимать
- ✅ Оптимизирована для аналитики

---

## 4. Snowflake Schema (Снежинка)

### 4.1 Структура

**Snowflake Schema** — нормализованная версия Star Schema.

```
        [Date Dimension]
              |
[Product Dimension] -- [Sales Fact] -- [Customer Dimension]
      |                    |                |
[Category]          [Store Dimension]  [Country]
                           |
                      [Region]
```

**Пример:**

```sql
-- Нормализованные Dimension
CREATE TABLE category_dimension (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE product_dimension (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INTEGER,  -- FK вместо прямого category
    FOREIGN KEY (category_id) REFERENCES category_dimension(category_id)
);
```

### 4.2 Преимущества и недостатки

**Преимущества:**

- ✅ Меньше избыточности данных
- ✅ Легче обновлять

**Недостатки:**

- ❌ Больше JOIN (медленнее запросы)
- ❌ Сложнее структура

---

## 5. SQL в Business Intelligence

### 5.1 Типичные аналитические запросы

**Временные тренды:**

```sql
SELECT 
    d.year,
    d.month,
    SUM(s.amount) AS monthly_sales
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
```

**Сравнение периодов:**

```sql
SELECT 
    p.category,
    SUM(CASE WHEN d.year = 2023 THEN s.amount ELSE 0 END) AS sales_2023,
    SUM(CASE WHEN d.year = 2024 THEN s.amount ELSE 0 END) AS sales_2024,
    SUM(CASE WHEN d.year = 2024 THEN s.amount ELSE 0 END) - 
    SUM(CASE WHEN d.year = 2023 THEN s.amount ELSE 0 END) AS change
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
JOIN product_dimension p ON s.product_id = p.product_id
GROUP BY p.category;
```

**Топ-N анализ:**

```sql
SELECT 
    c.customer_name,
    SUM(s.amount) AS total_spent
FROM sales_fact s
JOIN customer_dimension c ON s.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;
```

---

## 6. ETL и Data Warehouses

### 6.1 ETL процесс

**ETL (Extract, Transform, Load):**

1. **Extract** — извлечение данных из источников
2. **Transform** — трансформация и очистка
3. **Load** — загрузка в Data Warehouse

**SQL в Transform:**

```sql
-- Очистка и трансформация данных
INSERT INTO sales_fact
SELECT 
    o.id,
    d.date_id,
    p.product_id,
    c.customer_id,
    o.amount,
    o.quantity
FROM raw_orders o
JOIN date_dimension d ON DATE(o.order_date) = d.date
JOIN product_dimension p ON o.product_name = p.product_name
JOIN customer_dimension c ON o.customer_email = c.email;
```

### 6.2 Инкрементальная загрузка

**Загрузка только новых данных:**

```sql
-- Загрузка только новых заказов
INSERT INTO sales_fact
SELECT 
    o.id,
    d.date_id,
    p.product_id,
    c.customer_id,
    o.amount,
    o.quantity
FROM raw_orders o
JOIN date_dimension d ON DATE(o.order_date) = d.date
JOIN product_dimension p ON o.product_name = p.product_name
JOIN customer_dimension c ON o.customer_email = c.email
WHERE o.id > (SELECT COALESCE(MAX(sale_id), 0) FROM sales_fact);
```

---

## 7. Колоночные хранилища

### 7.1 Что такое колоночные хранилища

**Колоночные хранилища** хранят данные по столбцам, а не по строкам.

**Преимущества для аналитики:**

- ✅ Отличное сжатие (одинаковые значения в столбце)
- ✅ Быстрые агрегации (читается только нужный столбец)
- ✅ Эффективны для OLAP запросов

**Примеры:**

- ClickHouse
- BigQuery
- Snowflake
- Amazon Redshift

### 7.2 SQL в колоночных хранилищах

**SQL синтаксис остаётся тем же:**

```sql
-- Запрос работает так же
SELECT 
    d.year,
    p.category,
    SUM(s.amount) AS total_sales
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
JOIN product_dimension p ON s.product_id = p.product_id
GROUP BY d.year, p.category;
```

**Но выполняется быстрее** благодаря колоночному хранению.

---

## 8. BI инструменты и SQL

### 8.1 SQL в BI инструментах

**BI инструменты используют SQL для запросов:**

- **Tableau** — визуализация с SQL запросами

- **Power BI** — DAX и SQL

- **Metabase** — SQL-first BI инструмент

- **Looker** — LookML на основе SQL

### 8.2 Пример запроса для BI

**Запрос для дашборда:**

```sql
-- Продажи по месяцам и категориям
SELECT 
    d.year,
    d.month,
    p.category,
    SUM(s.amount) AS total_sales,
    COUNT(DISTINCT s.customer_id) AS unique_customers,
    AVG(s.amount) AS avg_order_value
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
JOIN product_dimension p ON s.product_id = p.product_id
WHERE d.year >= 2023
GROUP BY d.year, d.month, p.category
ORDER BY d.year, d.month, total_sales DESC;
```

---

## 9. Аналитические функции в SQL

### 9.1 Оконные функции для аналитики

**Оконные функции идеальны для аналитики:**

```sql
-- Накопительные продажи по месяцам
SELECT 
    d.year,
    d.month,
    SUM(s.amount) AS monthly_sales,
    SUM(SUM(s.amount)) OVER (
        PARTITION BY d.year 
        ORDER BY d.month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_sales
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
```

### 9.2 Сравнение периодов

**YoY (Year over Year) сравнение:**

```sql
SELECT 
    d.year,
    d.month,
    SUM(s.amount) AS current_sales,
    LAG(SUM(s.amount), 12) OVER (
        ORDER BY d.year, d.month
    ) AS previous_year_sales,
    SUM(s.amount) - LAG(SUM(s.amount), 12) OVER (
        ORDER BY d.year, d.month
    ) AS yoy_change
FROM sales_fact s
JOIN date_dimension d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
```

---

## 10. Практические аналитические запросы

### 10.1 Когортный анализ

**Анализ по когортам пользователей:**

```sql
-- Первая покупка каждого пользователя
WITH first_purchase AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
),
cohorts AS (
    SELECT 
        c.customer_id,
        DATE_TRUNC('month', fp.first_order_date) AS cohort_month,
        DATE_TRUNC('month', c.order_date) AS order_month,
        EXTRACT(MONTH FROM AGE(c.order_date, fp.first_order_date)) AS period_number
    FROM orders c
    JOIN first_purchase fp ON c.customer_id = fp.customer_id
)
SELECT 
    cohort_month,
    period_number,
    COUNT(DISTINCT customer_id) AS customers,
    SUM(amount) AS revenue
FROM cohorts
GROUP BY cohort_month, period_number
ORDER BY cohort_month, period_number;
```

### 10.2 RFM анализ

**Recency, Frequency, Monetary анализ:**

```sql
WITH customer_metrics AS (
    SELECT 
        customer_id,
        MAX(order_date) AS last_order_date,
        COUNT(*) AS frequency,
        SUM(amount) AS monetary
    FROM orders
    GROUP BY customer_id
),
rfm_scores AS (
    SELECT 
        customer_id,
        CASE 
            WHEN last_order_date >= CURRENT_DATE - INTERVAL '30 days' THEN 5
            WHEN last_order_date >= CURRENT_DATE - INTERVAL '60 days' THEN 4
            WHEN last_order_date >= CURRENT_DATE - INTERVAL '90 days' THEN 3
            WHEN last_order_date >= CURRENT_DATE - INTERVAL '180 days' THEN 2
            ELSE 1
        END AS recency_score,
        CASE 
            WHEN frequency >= 20 THEN 5
            WHEN frequency >= 10 THEN 4
            WHEN frequency >= 5 THEN 3
            WHEN frequency >= 2 THEN 2
            ELSE 1
        END AS frequency_score,
        CASE 
            WHEN monetary >= 10000 THEN 5
            WHEN monetary >= 5000 THEN 4
            WHEN monetary >= 2000 THEN 3
            WHEN monetary >= 1000 THEN 2
            ELSE 1
        END AS monetary_score
    FROM customer_metrics
)
SELECT 
    recency_score,
    frequency_score,
    monetary_score,
    COUNT(*) AS customer_count
FROM rfm_scores
GROUP BY recency_score, frequency_score, monetary_score
ORDER BY recency_score DESC, frequency_score DESC, monetary_score DESC;
```

### 10.3 Воронка конверсии

**Анализ воронки:**

```sql
WITH funnel AS (
    SELECT 
        'Visitors' AS stage,
        COUNT(DISTINCT session_id) AS count
    FROM page_views
    UNION ALL
    SELECT 
        'Signups' AS stage,
        COUNT(DISTINCT user_id) AS count
    FROM users
    WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
    UNION ALL
    SELECT 
        'First Purchase' AS stage,
        COUNT(DISTINCT customer_id) AS count
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT 
    stage,
    count,
    LAG(count) OVER (ORDER BY 
        CASE stage
            WHEN 'Visitors' THEN 1
            WHEN 'Signups' THEN 2
            WHEN 'First Purchase' THEN 3
        END
    ) AS previous_stage,
    ROUND(100.0 * count / LAG(count) OVER (ORDER BY 
        CASE stage
            WHEN 'Visitors' THEN 1
            WHEN 'Signups' THEN 2
            WHEN 'First Purchase' THEN 3
        END
    ), 2) AS conversion_rate
FROM funnel;
```

---

## 11. Оптимизация аналитических запросов

### 11.1 Индексы для аналитики

**Создавайте индексы на столбцах для фильтрации и группировки:**

```sql
-- Индексы для аналитических запросов
CREATE INDEX idx_sales_date ON sales_fact(date_id);
CREATE INDEX idx_sales_product ON sales_fact(product_id);
CREATE INDEX idx_sales_customer ON sales_fact(customer_id);

-- Составной индекс для группировки
CREATE INDEX idx_sales_date_product ON sales_fact(date_id, product_id);
```

### 11.2 Партиционирование для аналитики

**Партиционирование по дате для больших таблиц:**

```sql
-- Партиционирование по месяцам
CREATE TABLE sales_fact (
    sale_id INTEGER,
    date_id INTEGER,
    product_id INTEGER,
    customer_id INTEGER,
    amount DECIMAL(10, 2)
) PARTITION BY RANGE (date_id);

-- Партиции по месяцам
CREATE TABLE sales_2024_01 PARTITION OF sales_fact
    FOR VALUES FROM (20240101) TO (20240201);
```

**Преимущества:**

- ✅ Быстрые запросы (сканируется только нужная партиция)
- ✅ Легко удалять старые данные (DROP PARTITION)

---

## 💡 Key Takeaways

- **OLTP** — операционные системы (много записи), **OLAP** — аналитические (много чтения)

- **Fact таблицы** — метрики и измерения, **Dimension таблицы** — описательные атрибуты

- **Star Schema** — простая денормализованная схема, **Snowflake** — нормализованная

- **SQL в аналитике** — временные тренды, сравнения, топ-N анализ

- **Data Warehouses** — хранилища данных для аналитики с денормализованными схемами

---

## 🚀 Next Steps

**Related Modules:**

- [16_Data_Engineering](../16_Data_Engineering/) — SQL в Data Engineering
- [18_System_Design](../18_System_Design/) — SQL как часть system design

**Practice Ideas:**

1. Спроектируйте Star Schema для вашего домена
2. Создайте аналитические запросы с временными трендами
3. Попрактикуйтесь с Fact и Dimension таблицами
4. Сравните Star и Snowflake схемы

**Going Deeper:**

- Изучите Data Warehousing концепции
- Изучите инструменты BI (Tableau, Power BI, Metabase)
- Изучите колоночные хранилища (ClickHouse, BigQuery)

---

## 📚 Additional Resources

**Documentation:**

- [Data Warehousing Concepts](https://www.postgresql.org/docs/current/ddl-partitioning.html) — концепции хранилищ данных
- [OLAP vs OLTP](https://www.postgresql.org/docs/current/indexes.html) — различия систем

---


