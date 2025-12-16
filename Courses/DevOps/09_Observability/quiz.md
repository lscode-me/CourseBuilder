# Observability - Quiz

Проверьте свои знания по трём столпам observability.

---

## Question 1: Monitoring vs Observability

Чем observability отличается от мониторинга?

A) Это одно и то же

B) Observability дешевле

C) Observability только для микросервисов

D) Monitoring — предопределённые проверки, Observability — исследование неизвестных проблем

---

## Question 2: Three Pillars

Какие три столпа observability?

A) Logs, Metrics, Traces

B) HTTP, TCP, UDP

C) CPU, Memory, Disk

D) Prometheus, Grafana, Alertmanager

---

## Question 3: Structured Logging

Почему structured logging (JSON) лучше plain text?

A) Меньше размер файлов

B) JSON красивее

C) Быстрее записывается

D) Легче парсить, искать, агрегировать

---

## Question 4: Traces

Что показывает distributed trace?

A) Только ошибки

B) Путь запроса через сервисы с timing информацией

C) Количество пользователей

D) Размер базы данных

---

## Question 5: Span

Что такое span в контексте tracing?

A) Ошибка в логах

B) Единица работы в trace (операция в одном сервисе)

C) Период времени без активности

D) Тип метрики

---

## Question 6: Trace ID

Для чего используется trace_id?

A) Для шифрования

B) Для версионирования

C) Для аутентификации

D) Для связывания всех spans одного запроса через сервисы

---

## Question 7: OpenTelemetry

Что такое OpenTelemetry?

A) База данных

B) Стандарт и SDK для инструментации (logs, metrics, traces)

C) Облачный сервис

D) Протокол мониторинга

---

## Question 8: Context Propagation

Что такое context propagation в distributed tracing?

A) Передача trace context между сервисами через headers

B) Распространение ошибок

C) Копирование логов

D) Синхронизация времени

---

## Question 9: Log Levels

Какой log level использовать для нормальных событий в production?

A) WARNING

B) INFO

C) ERROR

D) DEBUG

---

## Question 10: Correlation

Как связать логи с traces?

A) Добавлять trace_id в логи

B) Невозможно связать

C) По timestamp

D) Использовать одинаковые имена файлов

---

## Question 11: ELK Stack

Что входит в ELK Stack?

A) Elasticsearch, Logstash, Kibana

B) Envoy, Linkerd, Kong

C) Etcd, Loki, Kafka

D) Express, Linux, Kubernetes

---

## Question 12: Jaeger

Для чего используется Jaeger?

A) Для логирования

B) Для distributed tracing visualization

C) Для CI/CD

D) Для сбора метрик

---

## Question 13: Instrumentation

Что такое auto-instrumentation?

A) Автоматическое добавление tracing без изменения кода

B) Ручная настройка каждой функции

C) Генерация документации

D) Автоматическое логирование в файлы

---

## Question 14: High Cardinality

Почему high cardinality в логах может быть проблемой?

A) Растёт размер индекса и стоимость хранения

B) High cardinality не проблема

C) Логи быстрее записываются

D) Логи становятся красивее

---

## Question 15: Debugging Workflow

Какой типичный workflow debugging с observability?

A) Только смотреть логи

B) Только смотреть метрики

C) Перезагрузить сервер

D) Metrics → Traces → Logs (от общего к деталям)

---

## Question 16: Sampling

Что такое sampling в трейсинге?

A) Запись только части трейсов для снижения overhead

B) Сжатие метрик

C) Шифрование данных

D) Удаление логов

---

## Question 17: Baggage

Что такое baggage в distributed tracing?

A) Архив логов

B) Backup трейсов

C) Дополнительные данные, передаваемые с trace context

D) Нагрузка на сеть

---

## Question 18: RED method

Что измеряет RED method для сервисов?

A) RAM, Events, Data

B) Rate, Errors, Duration

C) Request, Error, Disk

D) Read, Edit, Delete

---

## Question 19: USE method

Что измеряет USE method для ресурсов?

A) Utilization, Saturation, Errors

B) Upload, Send, Execute

C) User, Service, Event

D) Unit, System, Error

---

## Question 20: Golden Signals

Какие метрики входят в Golden Signals?

A) CPU, Memory, Disk, Network

B) Input, Process, Output, Store

C) Read, Write, Execute, Delete

D) Latency, Traffic, Errors, Saturation

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Observability позволяет исследовать неизвестные проблемы |
| 2 | A | Logs, Metrics, Traces — три столпа |
| 3 | D | JSON легко парсить и искать |
| 4 | B | Trace показывает путь запроса через сервисы |
| 5 | B | Span — единица работы, операция в сервисе |
| 6 | D | trace_id связывает все spans одного запроса |
| 7 | B | OpenTelemetry — стандарт для instrumentation |
| 8 | A | Context propagation — передача trace context через headers |
| 9 | B | INFO для нормальных событий |
| 10 | A | trace_id в логах для корреляции |
| 11 | A | Elasticsearch, Logstash, Kibana |
| 12 | B | Jaeger для distributed tracing visualization |
| 13 | A | Auto-instrumentation добавляет tracing автоматически |
| 14 | A | High cardinality увеличивает размер индекса и стоимость |
| 15 | D | Metrics → Traces → Logs (от общего к деталям) |
| 16 | A | Sampling записывает только часть трейсов для снижения overhead |
| 17 | C | Baggage — дополнительные данные передаваемые с trace context |
| 18 | B | RED: Rate, Errors, Duration — метрики для сервисов |
| 19 | A | USE: Utilization, Saturation, Errors — метрики для ресурсов |
| 20 | D | Golden Signals: Latency, Traffic, Errors, Saturation |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Переходите к SRE. |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите трейсинг. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте корреляцию. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Изучите три столпа детальнее. |

---

