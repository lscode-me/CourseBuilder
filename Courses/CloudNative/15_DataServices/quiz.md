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

A) Хранит данные 365 дней

B) Запускает Lambda функции

C) Загружает streaming данные в destinations (S3, Redshift)

D) Обрабатывает данные с помощью SQL

---

## Question 5: Partitioning





Зачем партиционировать данные в S3 для Athena?

A) Для репликации

B) Для шифрования

C) Для уменьшения объёма сканируемых данных и стоимости

D) Для увеличения скорости записи

---

## Question 6: Redshift Spectrum




Что делает Redshift Spectrum?

A) Monitoring

B) Бэкапы

C) Ускоряет Redshift

D) Запросы к данным в S3 без загрузки в Redshift

---

## Question 7: Glue




Для чего используется AWS Glue?

A) Только storage

B) Только ETL

C) Только SQL

D) ETL, Data Catalog, crawlers для metadata

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

A) Monitoring

B) Email service

C) Messaging

D) Big data processing с Spark, Hadoop, Presto

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

A) Только для users

B) Для cost control, query limits, IAM isolation

C) Только для storage

D) Только для monitoring

---

## Question 15: Kinesis Analytics




Что делает Kinesis Data Analytics?

A) Real-time SQL/Flink на streaming data

B) ETL

C) Batch processing

D) Storage

---

## Question 16: Redshift Serverless




Какое преимущество Redshift Serverless?

A) Быстрее

B) Дешевле

C) Больше storage

D) Auto-scaling, pay per use, no cluster management

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

A) Secure data collaboration без sharing raw data

B) Storage

C) ETL

D) Data cleaning

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

A) Compute

B) DNS service

C) Data governance и cataloging across organization

D) Storage

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Redshift — OLAP система для сложной аналитики, агрегаций, BI. RDS/DynamoDB — для OLTP. |
| 2 | A | Athena: $5 per TB scanned. Использование Parquet и partitions критично для снижения стоимости. |
| 3 | D | Columnar форматы (Parquet, ORC) позволяют читать только нужные колонки, сжимаются лучше. |
| 4 | C | Firehose — managed service для загрузки streaming данных в S3, Redshift, OpenSearch без кода. |
| 5 | C | Partitioning позволяет Athena сканировать только нужные partitions, снижая cost и время запроса. |
| 6 | D | Spectrum запрашивает S3 без загрузки |
| 7 | D | Glue: ETL, Data Catalog, crawlers |
| 8 | A | QuickSight — serverless BI |
| 9 | C | Lake Formation — simplified data lake |
| 10 | C | OpenSearch для full-text search и logs |
| 11 | D | EMR для big data (Spark, Hadoop) |
| 12 | D | Data Pipeline — data orchestration |
| 13 | D | Glue: Spark и Python Shell jobs |
| 14 | B | Workgroups: cost control, limits, isolation |
| 15 | A | Kinesis Analytics: real-time SQL/Flink |
| 16 | D | Redshift Serverless: auto-scaling, pay per use |
| 17 | B | Data Exchange: third-party data marketplace |
| 18 | A | Clean Rooms: secure collaboration |
| 19 | D | MSK: managed Kafka |
| 20 | C | DataZone: data governance и cataloging |

---
