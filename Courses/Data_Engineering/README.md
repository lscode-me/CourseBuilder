# 📘 Курс: Data Engineering — от данных к масштабируемым системам

Комплексный курс по Data Engineering на русском языке.

---

## 📖 Описание курса

Data Engineering — это инженерная дисциплина, занимающаяся проектированием, построением и эксплуатацией систем, которые собирают, хранят, обрабатывают и предоставляют данные в надёжной, масштабируемой и воспроизводимой форме.

В отличие от Data Science, Data Engineering фокусируется не на моделях, а на инфраструктуре данных: пайплайнах, хранилищах, форматах, потоках, надёжности, стоимости и масштабировании.

Этот курс формирует **системное понимание Data Engineering** и показывает, как данные превращаются в продукт.

---

## 🎯 Цели курса

После прохождения курса слушатель:

- Понимает роль Data Engineering в компании
- Умеет проектировать data pipelines
- Ориентируется в хранилищах и форматах данных
- Понимает batch и streaming подходы
- Умеет рассуждать о надёжности, масштабировании и стоимости
- Видит связь Data Engineering с system design

---

## 🧩 Структура курса

### Модуль 1: Основы Data Engineering (4 лекции)

| № | Модуль | Тема | Основные темы |
|---|--------|------|---------------|
| 1 | [01_What_Is_Data_Engineering](01_What_Is_Data_Engineering/) | Что такое Data Engineering | Data Engineering vs Data Science vs Analytics, роль data engineer, типы data-систем, данные как продукт |
| 2 | [02_Data_Lifecycle](02_Data_Lifecycle/) | Жизненный цикл данных | Источники данных, Ingestion, Storage, Processing, Serving, Consumption |
| 3 | [03_Data_Types](03_Data_Types/) | Типы данных | Structured, Semi-structured, Unstructured, Operational vs analytical data, OLTP vs OLAP |
| 4 | [04_Data_Modeling](04_Data_Modeling/) | Основы data modeling | Entity–relationship модели, Normalization, Denormalization, Trade-offs |

### Модуль 2: Хранение и форматы данных (4 лекции)

| № | Модуль | Тема | Основные темы |
|---|--------|------|---------------|
| 5 | [05_Data_Storage](05_Data_Storage/) | Хранилища данных | Databases, Data warehouses, Data lakes, Lakehouse |
| 6 | [06_Data_Formats](06_Data_Formats/) | Форматы данных | CSV, JSON, Avro, Parquet, ORC, row-based vs column-based, schema-on-read vs schema-on-write |
| 7 | [07_Indexes_Partitioning](07_Indexes_Partitioning/) | Индексы и партиционирование | Индексы как структуры данных, Партиционирование, Sharding, Performance trade-offs |
| 8 | [08_Metadata_Catalogs](08_Metadata_Catalogs/) | Метаданные и каталоги данных | Schema, Data catalog, Lineage, Data discovery |

### Модуль 3: Data Pipelines и обработка данных (4 лекции)

| № | Модуль | Тема | Основные темы |
|---|--------|------|---------------|
| 9 | [09_Batch_Processing](09_Batch_Processing/) | Batch processing | Batch pipelines, ETL vs ELT, Scheduling, Idempotency |
| 10 | [10_Batch_Tools](10_Batch_Tools/) | Инструменты batch processing | SQL engines, Spark, Airflow, dbt |
| 11 | [11_Data_Quality](11_Data_Quality/) | Качество данных | Data validation, Data completeness, Data freshness, Data consistency |
| 12 | [12_Errors_Reproducibility](12_Errors_Reproducibility/) | Ошибки и воспроизводимость | Retries, Backfills, Versioning данных, Reproducible pipelines |

### Модуль 4: Streaming и real-time данные (4 лекции)

| № | Модуль | Тема | Основные темы |
|---|--------|------|---------------|
| 13 | [13_Streaming_Model](13_Streaming_Model/) | Streaming как модель обработки | Event-driven systems, Streams vs batches, Exactly-once / at-least-once, Windowing |
| 14 | [14_Streaming_Tools](14_Streaming_Tools/) | Инструменты streaming обработки | Kafka, Pulsar, Flink, Spark Streaming |
| 15 | [15_Streaming_Storage](15_Streaming_Storage/) | Хранение потоковых данных | Log как структура данных, Retention, Compaction, Replay |
| 16 | [16_Streaming_UseCases](16_Streaming_UseCases/) | Streaming use cases | Event analytics, Monitoring, Fraud detection, Real-time dashboards |

### Модуль 5: Архитектура и system design (4 лекции)

| № | Модуль | Тема | Основные темы |
|---|--------|------|---------------|
| 17 | [17_Data_Platform_Architectures](17_Data_Platform_Architectures/) | Архитектуры data-платформ | Lambda architecture, Kappa architecture, Modern data stack |
| 18 | [18_Scaling_Performance](18_Scaling_Performance/) | Масштабирование и производительность | Horizontal vs vertical scaling, Throughput vs latency, Bottlenecks, Cost-aware design |
| 19 | [19_Reliability_Operations](19_Reliability_Operations/) | Надёжность и эксплуатация | Fault tolerance, Monitoring, Alerting, SLA и SLO |
| 20 | [20_Data_Engineering_System_Design](20_Data_Engineering_System_Design/) | Data Engineering как system design | Выбор хранилищ, Выбор форматов, Выбор DS и алгоритмов, Компромиссы архитектуры |

---

## 🎓 Целевая аудитория

- Backend-разработчики, переходящие в Data Engineering
- Data Scientists, желающие понять инфраструктуру данных
- DevOps-инженеры, работающие с data pipelines
- Архитекторы, проектирующие data-системы
- Все, кто хочет понимать современные data-платформы

---

## 📋 Предварительные требования

- Опыт программирования на любом языке
- Базовое понимание баз данных (SQL)
- Знакомство с Linux/Unix командной строкой
- Понимание основ сетей (HTTP, TCP/IP)
- Желательно: опыт работы с Python

**Рекомендуемые курсы:**

- Data Structures
- Algorithms & Complexity
- Distributed Systems
- Protocols & APIs

---

## ⏱️ Время прохождения

| Раздел | Модули | Время чтения | Время практики |
|--------|--------|--------------|----------------|
| Основы Data Engineering | 1-4 | 2-3 часа | 2-3 часа |
| Хранение и форматы данных | 5-8 | 2-3 часа | 3-4 часа |
| Data Pipelines и обработка | 9-12 | 3-4 часа | 4-5 часов |
| Streaming и real-time | 13-16 | 3-4 часа | 4-5 часов |
| Архитектура и system design | 17-20 | 3-4 часа | 4-5 часов |
| **Итого** | **20 модулей** | **13-18 часов** | **17-22 часа** |

---

## 📋 Формат модуля

Каждый модуль содержит:

```

XX_ModuleName/
├── lecture.md    # Основной материал лекции
└── quiz.md       # Вопросы для самопроверки
```

### Структура лекции

- **Prerequisites** — что нужно знать перед началом

- **Learning Objectives** — цели обучения

- **Основной материал** — теория с реальными примерами

- **Key Takeaways** — главные выводы

- **Next Steps** — что изучить дальше

- **Additional Resources** — дополнительные материалы

### Quiz

- 20-40 вопросов с множественным выбором
- Вопросы на понимание концепций и практическое применение
- Ответы с пояснениями

---

## 🧠 Итоги курса

Data Engineering — это:

- Инженерия данных, а не аналитика
- Основа для Data Science, ML и BI
- Дисциплина про надёжность, масштабирование и стоимость

Сильный Data Engineer:

- Думает системно
- Понимает структуры данных и алгоритмы
- Проектирует data-системы осознанно

---

## 📌 Возможные продолжения

- Advanced Data Engineering
- Streaming Systems Internals
- Data Platform Architecture
- MLOps & Feature Stores

---

## 🔗 Связь с другими курсами

**Рекомендуется знание:**

- [Data Structures](../Data_Structures/) — структуры данных
- [Data Systems](../Data_Systems/) — системы данных
- [CloudNative](../CloudNative/) — облачные технологии
- [DevOps](../DevOps/) — автоматизация и CI/CD

---

## 📚 Дополнительные ресурсы

**Книги:**

- "Designing Data-Intensive Applications" by Martin Kleppmann
- "Fundamentals of Data Engineering" by Joe Reis & Matt Housley
- "Streaming Systems" by Tyler Akidau, Slava Chernyak, Reuven Lax

**Документация:**

- Apache Spark: https://spark.apache.org/docs/latest/
- Apache Kafka: https://kafka.apache.org/documentation/
- Apache Airflow: https://airflow.apache.org/docs/

---

**Версия:** 1.0  
**Дата:** 2024-12-09


