# Оконные функции
## OVER, PARTITION BY, ORDER BY, ROW_NUMBER, RANK, LAG, LEAD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать агрегатные функции (COUNT, SUM, AVG)
- Понимать работу с GROUP BY
- Иметь представление о подзапросах

**Recommended prior modules:**

- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY
- [07_Subqueries](../07_Subqueries/) — Подзапросы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать оконные функции для вычислений над группами строк
- Применять PARTITION BY для разделения на окна
- Использовать ORDER BY в окнах для упорядочивания
- Применять ROW_NUMBER, RANK, DENSE_RANK для нумерации
- Использовать LAG и LEAD для доступа к предыдущим/следующим строкам

---

## 1. Введение в оконные функции

### 1.1 Что такое оконные функции

**Оконные функции (Window Functions)** выполняют вычисления над набором строк, связанных с текущей строкой, без группировки результата.

**Отличие от агрегатов:**

- **Агрегаты** (GROUP BY) — уменьшают количество строк

- **Оконные функции** — сохраняют все строки, добавляя вычисленные значения

**Пример:**

```sql

CREATE TABLE sales (
    id INTEGER,
    product VARCHAR(100),
    sale_date DATE,
    amount DECIMAL(10, 2)
);

INSERT INTO sales VALUES
    (1, 'Product A', '2024-01-01', 100),
    (2, 'Product A', '2024-01-02', 150),
    (3, 'Product B', '2024-01-01', 200),
    (4, 'Product B', '2024-01-02', 250);

-- Агрегат: уменьшает строки
SELECT product, SUM(amount) FROM sales GROUP BY product;

-- Оконная функция: сохраняет все строки
SELECT 
    product,
    amount,
    SUM(amount) OVER (PARTITION BY product) AS total_by_product
FROM sales;
```

**Output:**
```

product   | amount | total_by_product
----------+--------+-----------------
Product A | 100    | 250
Product A | 150    | 250
Product B | 200    | 450
Product B | 250    | 450
```

---

## 2. Синтаксис OVER

### 2.1 Базовый синтаксис

```sql

function() OVER (
    [PARTITION BY column]
    [ORDER BY column]
    [ROWS/RANGE frame]
)
```

**Компоненты:**

- **function()** — оконная функция

- **PARTITION BY** — разделение на окна

- **ORDER BY** — упорядочивание в окне

- **ROWS/RANGE** — определение рамки окна

### 2.2 OVER без PARTITION BY

**Применение ко всей таблице:**

```sql

SELECT 
    product,
    amount,
    SUM(amount) OVER () AS total_all
FROM sales;
```

**Output:**
```

product   | amount | total_all
----------+--------+----------
Product A | 100    | 700
Product A | 150    | 700
Product B | 200    | 700
Product B | 250    | 700
```

---

## 3. PARTITION BY

### 3.1 Разделение на окна

**PARTITION BY** разделяет строки на группы (окна):

```sql

SELECT 
    product,
    amount,
    SUM(amount) OVER (PARTITION BY product) AS total_by_product,
    AVG(amount) OVER (PARTITION BY product) AS avg_by_product
FROM sales;
```

**Output:**
```

product   | amount | total_by_product | avg_by_product
----------+--------+------------------+---------------
Product A | 100    | 250              | 125.00
Product A | 150    | 250              | 125.00
Product B | 200    | 450              | 225.00
Product B | 250    | 450              | 225.00
```

### 3.2 Несколько столбцов в PARTITION BY

```sql

SELECT 
    product,
    sale_date,
    amount,
    SUM(amount) OVER (PARTITION BY product, sale_date) AS total
FROM sales;
```

---

## 4. ORDER BY в окнах

### 4.1 Упорядочивание в окне

**ORDER BY** упорядочивает строки внутри окна:

```sql

SELECT 
    product,
    sale_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY product 
        ORDER BY sale_date
    ) AS running_total
FROM sales;
```

**Output:**
```

product   | sale_date  | amount | running_total
----------+------------+--------+---------------
Product A | 2024-01-01 | 100    | 100
Product A | 2024-01-02 | 150    | 250
Product B | 2024-01-01 | 200    | 200
Product B | 2024-01-02 | 250    | 450
```

**Накопительная сумма (running total)** — сумма накапливается по мере упорядочивания.

---

## 5. ROW_NUMBER, RANK, DENSE_RANK

### 5.1 ROW_NUMBER

**ROW_NUMBER** — уникальный номер строки в окне:

```sql

SELECT 
    product,
    amount,
    ROW_NUMBER() OVER (PARTITION BY product ORDER BY amount DESC) AS rn
FROM sales;
```

**Output:**
```

product   | amount | rn
----------+--------+----
Product A | 150    | 1
Product A | 100    | 2
Product B | 250    | 1
Product B | 200    | 2
```

### 5.2 RANK

**RANK** — ранг с пропусками при равенстве:

```sql

INSERT INTO sales VALUES (5, 'Product A', '2024-01-03', 150);

SELECT 
    product,
    amount,
    RANK() OVER (PARTITION BY product ORDER BY amount DESC) AS rank
FROM sales;
```

**Output:**
```

product   | amount | rank
----------+--------+-----
Product A | 150    | 1
Product A | 150    | 1
Product A | 100    | 3  (пропуск 2)
Product B | 250    | 1
Product B | 200    | 2
```

### 5.3 DENSE_RANK

**DENSE_RANK** — ранг без пропусков:

```sql

SELECT 
    product,
    amount,
    DENSE_RANK() OVER (PARTITION BY product ORDER BY amount DESC) AS dense_rank
FROM sales;
```

**Output:**
```

product   | amount | dense_rank
----------+--------+-----------
Product A | 150    | 1
Product A | 150    | 1
Product A | 100    | 2  (без пропуска)
Product B | 250    | 1
Product B | 200    | 2
```

---

## 6. LAG и LEAD

### 6.1 LAG — предыдущая строка

**LAG** получает значение из предыдущей строки:

```sql

SELECT 
    product,
    sale_date,
    amount,
    LAG(amount) OVER (PARTITION BY product ORDER BY sale_date) AS prev_amount
FROM sales;
```

**Output:**
```

product   | sale_date  | amount | prev_amount
----------+------------+--------+------------
Product A | 2024-01-01 | 100    | NULL
Product A | 2024-01-02 | 150    | 100
Product B | 2024-01-01 | 200    | NULL
Product B | 2024-01-02 | 250    | 200
```

### 6.2 LEAD — следующая строка

**LEAD** получает значение из следующей строки:

```sql

SELECT 
    product,
    sale_date,
    amount,
    LEAD(amount) OVER (PARTITION BY product ORDER BY sale_date) AS next_amount
FROM sales;
```

### 6.3 LAG/LEAD с offset

**Указание смещения:**

```sql

-- Значение 2 строки назад
LAG(amount, 2) OVER (PARTITION BY product ORDER BY sale_date)

-- Значение 2 строки вперёд
LEAD(amount, 2) OVER (PARTITION BY product ORDER BY sale_date)
```

---

## 7. Агрегаты как оконные функции

### 7.1 SUM, AVG, COUNT в окнах

```sql

SELECT 
    product,
    amount,
    SUM(amount) OVER (PARTITION BY product) AS total,
    AVG(amount) OVER (PARTITION BY product) AS avg_amount,
    COUNT(*) OVER (PARTITION BY product) AS count
FROM sales;
```

### 7.2 FIRST_VALUE и LAST_VALUE

**Первое и последнее значение в окне:**

```sql

SELECT 
    product,
    sale_date,
    amount,
    FIRST_VALUE(amount) OVER (
        PARTITION BY product 
        ORDER BY sale_date
    ) AS first_amount,
    LAST_VALUE(amount) OVER (
        PARTITION BY product 
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_amount
FROM sales;
```

---

## 8. Рамки окон (Frame)

### 8.1 ROWS vs RANGE

**ROWS** — физические строки:

```sql

-- Текущая строка и предыдущая
SUM(amount) OVER (
    PARTITION BY product 
    ORDER BY sale_date
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
)
```

**RANGE** — логические значения:

```sql

-- Все строки с тем же значением
SUM(amount) OVER (
    PARTITION BY product 
    ORDER BY sale_date
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

---

## 9. Практические примеры

### 9.1 Топ-N запросы

**Топ-3 продажи по каждому продукту:**

```sql

SELECT * FROM (
    SELECT 
        product,
        sale_date,
        amount,
        ROW_NUMBER() OVER (PARTITION BY product ORDER BY amount DESC) AS rn
    FROM sales
) ranked
WHERE rn <= 3;
```

### 9.2 Изменение по сравнению с предыдущим периодом

```sql

SELECT 
    product,
    sale_date,
    amount,
    LAG(amount) OVER (PARTITION BY product ORDER BY sale_date) AS prev_amount,
    amount - LAG(amount) OVER (PARTITION BY product ORDER BY sale_date) AS change
FROM sales;
```

### 9.3 Процент от общего

```sql

SELECT 
    product,
    amount,
    amount * 100.0 / SUM(amount) OVER () AS percent_of_total
FROM sales;
```

---

## 💡 Key Takeaways

- **Оконные функции** сохраняют все строки, добавляя вычисленные значения

- **PARTITION BY** разделяет строки на окна для независимых вычислений

- **ORDER BY** в окне упорядочивает строки и создаёт накопительные вычисления

- **ROW_NUMBER, RANK, DENSE_RANK** — для нумерации строк

- **LAG/LEAD** — для доступа к предыдущим/следующим строкам

---

## 🚀 Next Steps

**Related Modules:**

- [12_CTE](../12_CTE/) — CTE и рекурсивные запросы
- [05_Aggregations](../05_Aggregations/) — Агрегации и GROUP BY

**Practice Ideas:**

1. Перепишите запросы с подзапросов на оконные функции
2. Решите задачи: топ-N, изменение по периодам, проценты
3. Сравните производительность оконных функций и подзапросов
4. Попрактикуйтесь с LAG/LEAD для временных рядов

**Going Deeper:**

- Изучите другие оконные функции (NTILE, PERCENT_RANK)
- Изучите оптимизацию оконных функций
- Изучите использование рамок окон (ROWS/RANGE)

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html) — учебник
- [Window Functions](https://www.postgresql.org/docs/current/functions-window.html) — все функции

---


