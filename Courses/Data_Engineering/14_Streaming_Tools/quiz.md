# Data Engineering - Quiz
## Инструменты streaming обработки

Проверьте свои знания по теме "Инструменты streaming обработки".

---

## Question 1: Apache Kafka

Что такое Apache Kafka?

A) Только оркестратор

B) Распределённая event streaming platform

C) Только SQL engine

D) Только база данных

---

## Question 2: Kafka Topics

Что такое Kafka topic?

A) Только таблица

B) Только файл

C) Только база данных

D) Категория событий, разделённая на партиции

---

## Question 3: Kafka Producers

Что делают Kafka producers?

A) Только читают события

B) Только обрабатывают события

C) Только удаляют события

D) Отправляют события в topics

---

## Question 4: Kafka Consumers

Что делают Kafka consumers?

A) Только удаляют события

B) Только создают topics

C) Читают события из topics

D) Только отправляют события

---

## Question 5: Apache Pulsar

Что такое Apache Pulsar?

A) Cloud-native distributed messaging system

B) Только SQL engine

C) Только база данных

D) Только оркестратор

---

## Question 6: Pulsar отличия

Какие отличия имеет Pulsar от Kafka? (Выберите все подходящие)

A) Все вышеперечисленные

B) Multi-tenancy

C) Разделение storage и compute

D) Географическая репликация

---

## Question 7: Apache Flink

Что такое Apache Flink?

A) Distributed stream processing engine

B) Только база данных

C) Только оркестратор

D) Только message broker

---

## Question 8: Flink характеристики

Какие характеристики имеет Flink? (Выберите все подходящие)

A) Low latency

B) Все вышеперечисленные

C) State management

D) Exactly-once semantics

---

## Question 9: Spark Streaming

Что такое Spark Streaming?

A) Расширение Spark для обработки потоков через микробатчи

B) Только message broker

C) Только база данных

D) Только batch processing

---

## Question 10: Spark Streaming DStreams

Что такое DStreams в Spark Streaming?

A) Discretized Streams — последовательность RDD

B) Только файлы

C) Только базы данных

D) Только таблицы

---

## Question 11: Выбор Kafka

Когда следует использовать Kafka?

A) Только для batch processing

B) Только для маленьких объёмов

C) Только для SQL запросов

D) Для event streaming с высокой пропускной способностью

---

## Question 12: Выбор Pulsar

Когда следует использовать Pulsar?

A) Только для маленьких систем

B) Для cloud-native messaging с multi-tenancy

C) Только для batch processing

D) Только для SQL запросов

---

## Question 13: Выбор Flink

Когда следует использовать Flink?

A) Только для SQL запросов

B) Только для маленьких объёмов

C) Для stream processing с low latency и exactly-once

D) Только для batch processing

---

## Question 14: Выбор Spark Streaming

Когда следует использовать Spark Streaming?

A) Только для real-time processing

B) Только для SQL запросов

C) Для микробатчей и интеграции с Spark ecosystem

D) Только для маленьких объёмов

---

## Question 15: Kafka партиции

Зачем используются партиции в Kafka topics?

A) Для масштабирования и параллельной обработки

B) Только для увеличения размера

C) Только для удаления данных

D) Только для замедления обработки

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Apache Kafka — это распределённая event streaming platform для публикации и подписки на потоки событий. |
| 2 | D | Kafka topic — это категория событий, которая разделена на партиции для масштабирования и параллелизма. |
| 3 | D | Kafka producers отправляют события в topics, могут выбирать партицию для распределения нагрузки. |
| 4 | C | Kafka consumers читают события из topics, могут работать в consumer groups для масштабирования. |
| 5 | A | Apache Pulsar — это cloud-native distributed messaging system с разделением storage и compute. |
| 6 | A | Все отличия (разделение storage/compute, multi-tenancy, географическая репликация) относятся к Pulsar. |
| 7 | A | Apache Flink — это distributed stream processing engine для обработки неограниченных потоков данных. |
| 8 | B | Все характеристики (low latency, exactly-once, state management) относятся к Flink. |
| 9 | A | Spark Streaming — это расширение Spark для обработки потоков через микробатчи (DStreams). |
| 10 | A | DStreams (Discretized Streams) — это последовательность RDD, представляющая поток данных в Spark Streaming. |
| 11 | D | Kafka следует использовать для event streaming с высокой пропускной способностью и долгосрочным хранением. |
| 12 | B | Pulsar следует использовать для cloud-native messaging с multi-tenancy и географической репликацией. |
| 13 | C | Flink следует использовать для stream processing с требованиями к low latency и exactly-once semantics. |
| 14 | C | Spark Streaming следует использовать для микробатчей и когда нужна интеграция с Spark ecosystem. |
| 15 | A | Партиции в Kafka topics используются для масштабирования и параллельной обработки событий. |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Переходите к следующему модулю. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Хороший результат! Повторите темы, в которых ошиблись. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать соответствующие разделы лекции. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---

