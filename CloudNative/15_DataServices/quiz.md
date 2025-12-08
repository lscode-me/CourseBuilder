# Cloud Native Development - Quiz
## Data Services

---

## Question 1: OLTP vs OLAP

Какой тип workload характерен для Redshift?

A) OLTP (транзакции)
B) OLAP (аналитика)
C) Caching
D) Streaming

---

## Question 2: Athena Pricing

Как оплачивается Athena?

A) Per-hour
B) Per-query based on data scanned
C) Фиксированная месячная плата
D) Per-row returned

---

## Question 3: Data Format

Какой формат данных рекомендуется для Athena/Redshift?

A) CSV
B) JSON
C) Parquet/ORC (columnar)
D) XML

---

## Question 4: Kinesis Firehose

Что делает Kinesis Firehose?

A) Обрабатывает данные с помощью SQL
B) Загружает streaming данные в destinations (S3, Redshift)
C) Хранит данные 365 дней
D) Запускает Lambda функции

---

## Question 5: Partitioning

Зачем партиционировать данные в S3 для Athena?

A) Для шифрования
B) Для уменьшения объёма сканируемых данных и стоимости
C) Для увеличения скорости записи
D) Для репликации

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Redshift — OLAP система для сложной аналитики, агрегаций, BI. RDS/DynamoDB — для OLTP. |
| 2 | B | Athena: $5 per TB scanned. Использование Parquet и partitions критично для снижения стоимости. |
| 3 | C | Columnar форматы (Parquet, ORC) позволяют читать только нужные колонки, сжимаются лучше. |
| 4 | B | Firehose — managed service для загрузки streaming данных в S3, Redshift, OpenSearch без кода. |
| 5 | B | Partitioning позволяет Athena сканировать только нужные partitions, снижая cost и время запроса. |

---
