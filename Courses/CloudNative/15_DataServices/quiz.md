# Cloud Native Development - Quiz
## Data Services

---

## Question 1: OLTP vs OLAP

Какой тип workload характерен для Redshift?

A) Caching

B) OLAP (аналитика)

C) Streaming

D) OLTP (транзакции)

---

## Question 2: Athena Pricing

Как оплачивается Athena?

A) Per-query based on data scanned

B) Фиксированная месячная плата

C) Per-row returned

D) Per-hour

---

## Question 3: Data Format

Какой формат данных рекомендуется для Athena/Redshift?

A) JSON

B) XML

C) CSV

D) Parquet/ORC (columnar)

---

## Question 4: Kinesis Firehose

Что делает Kinesis Firehose?

A) Загружает streaming данные в destinations (S3, Redshift)

B) Запускает Lambda функции

C) Обрабатывает данные с помощью SQL

D) Хранит данные 365 дней

---

## Question 5: Partitioning

Зачем партиционировать данные в S3 для Athena?

A) Для уменьшения объёма сканируемых данных и стоимости

B) Для увеличения скорости записи

C) Для репликации

D) Для шифрования

---

## Question 6: Redshift Spectrum

Что делает Redshift Spectrum?

A) Бэкапы

B) Monitoring

C) Запросы к данным в S3 без загрузки в Redshift

D) Ускоряет Redshift

---

## Question 7: Glue

Для чего используется AWS Glue?

A) ETL, Data Catalog, crawlers для metadata

B) Только SQL

C) Только ETL

D) Только storage

---

## Question 8: QuickSight

Что такое Amazon QuickSight?

A) Serverless BI visualization service

B) Database

C) Data warehouse

D) ETL tool

---

## Question 9: Lake Formation

Для чего используется Lake Formation?

A) Создание озёр

B) Только security

C) Simplified data lake setup и governance

D) Только storage

---

## Question 10: OpenSearch

Когда использовать OpenSearch вместо Athena?

A) Для data warehousing

B) Для SQL запросов

C) Для full-text search и log analytics

D) Для batch analytics

---

## Question 11: EMR

Для чего используется Amazon EMR?

A) Big data processing с Spark, Hadoop, Presto

B) Messaging

C) Email service

D) Monitoring

---

## Question 12: Data Pipeline

Что такое AWS Data Pipeline?

A) Streaming service

B) Database

C) Storage service

D) Orchestration для data movement и transformation

---

## Question 13: Glue Jobs

Какие типы jobs поддерживает Glue?

A) Только Scala

B) Только SQL

C) Только Python

D) Spark (Python/Scala) и Python Shell

---

## Question 14: Athena Workgroups

Для чего используются Athena Workgroups?

A) Только для storage

B) Для cost control, query limits, IAM isolation

C) Только для monitoring

D) Только для users

---

## Question 15: Kinesis Analytics

Что делает Kinesis Data Analytics?

A) Storage

B) Batch processing

C) ETL

D) Real-time SQL/Flink на streaming data

---

## Question 16: Redshift Serverless

Какое преимущество Redshift Serverless?

A) Auto-scaling, pay per use, no cluster management

B) Больше storage

C) Дешевле

D) Быстрее

---

## Question 17: Data Exchange

Что такое AWS Data Exchange?

A) ETL service

B) Marketplace для third-party data subscriptions

C) Storage

D) Database

---

## Question 18: Clean Rooms

Для чего используется AWS Clean Rooms?

A) ETL

B) Data cleaning

C) Secure data collaboration без sharing raw data

D) Storage

---

## Question 19: MSK

Что такое Amazon MSK?

A) SQL service

B) Storage

C) Monitoring service

D) Managed Kafka for streaming

---

## Question 20: DataZone

Для чего используется Amazon DataZone?

A) Data governance и cataloging across organization

B) Storage

C) Compute

D) DNS service

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Redshift — OLAP система для сложной аналитики, агрегаций, BI. RDS/DynamoDB — для OLTP. |
| 2 | A | Athena: $5 per TB scanned. Использование Parquet и partitions критично для снижения стоимости. |
| 3 | D | Columnar форматы (Parquet, ORC) позволяют читать только нужные колонки, сжимаются лучше. |
| 4 | A | Firehose — managed service для загрузки streaming данных в S3, Redshift, OpenSearch без кода. |
| 5 | A | Partitioning позволяет Athena сканировать только нужные partitions, снижая cost и время запроса. |
| 6 | C | Spectrum запрашивает S3 без загрузки |
| 7 | A | Glue: ETL, Data Catalog, crawlers |
| 8 | A | QuickSight — serverless BI |
| 9 | C | Lake Formation — simplified data lake |
| 10 | C | OpenSearch для full-text search и logs |
| 11 | A | EMR для big data (Spark, Hadoop) |
| 12 | D | Data Pipeline — data orchestration |
| 13 | D | Glue: Spark и Python Shell jobs |
| 14 | B | Workgroups: cost control, limits, isolation |
| 15 | D | Kinesis Analytics: real-time SQL/Flink |
| 16 | A | Redshift Serverless: auto-scaling, pay per use |
| 17 | B | Data Exchange: third-party data marketplace |
| 18 | C | Clean Rooms: secure collaboration |
| 19 | D | MSK: managed Kafka |
| 20 | A | DataZone: data governance и cataloging |

---

