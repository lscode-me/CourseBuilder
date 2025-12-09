# Cloud Native Development - Quiz
## Data Services

---

## Question 1: OLTP vs OLAP


Какой тип workload характерен для Redshift?

A) Caching

B) Streaming

C) OLAP (аналитика)

D) OLTP (транзакции)

---

## Question 2: Athena Pricing


Как оплачивается Athena?

A) Per-hour

B) Per-row returned

C) Фиксированная месячная плата

D) Per-query based on data scanned

---

## Question 3: Data Format


Какой формат данных рекомендуется для Athena/Redshift?

A) JSON

B) XML

C) Parquet/ORC (columnar)

D) CSV

---

## Question 4: Kinesis Firehose


Что делает Kinesis Firehose?

A) Хранит данные 365 дней

B) Запускает Lambda функции

C) Загружает streaming данные в destinations (S3, Redshift)

D) Обрабатывает данные с помощью SQL

---

## Question 5: Partitioning


Зачем партиционировать данные в S3 для Athena?

A) Для шифрования

B) Для уменьшения объёма сканируемых данных и стоимости

C) Для увеличения скорости записи

D) Для репликации

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Redshift — OLAP система для сложной аналитики, агрегаций, BI. RDS/DynamoDB — для OLTP. |
| 2 | D | Athena: $5 per TB scanned. Использование Parquet и partitions критично для снижения стоимости. |
| 3 | C | Columnar форматы (Parquet, ORC) позволяют читать только нужные колонки, сжимаются лучше. |
| 4 | C | Firehose — managed service для загрузки streaming данных в S3, Redshift, OpenSearch без кода. |
| 5 | B | Partitioning позволяет Athena сканировать только нужные partitions, снижая cost и время запроса. |

---
