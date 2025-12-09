# Observability - Quiz

Проверьте свои знания по трём столпам observability.

---

## Question 1: Monitoring vs Observability







Чем observability отличается от мониторинга?

A) Observability только для микросервисов

B) Это одно и то же

C) Monitoring — предопределённые проверки, Observability — исследование неизвестных проблем

D) Observability дешевле

---

## Question 2: Three Pillars







Какие три столпа observability?

A) Logs, Metrics, Traces

B) Prometheus, Grafana, Alertmanager

C) CPU, Memory, Disk

D) HTTP, TCP, UDP

---

## Question 3: Structured Logging







Почему structured logging (JSON) лучше plain text?

A) Быстрее записывается

B) Легче парсить, искать, агрегировать

C) Меньше размер файлов

D) JSON красивее

---

## Question 4: Traces







Что показывает distributed trace?

A) Количество пользователей

B) Путь запроса через сервисы с timing информацией

C) Размер базы данных

D) Только ошибки

---

## Question 5: Span







Что такое span в контексте tracing?

A) Единица работы в trace (операция в одном сервисе)

B) Тип метрики

C) Ошибка в логах

D) Период времени без активности

---

## Question 6: Trace ID







Для чего используется trace_id?

A) Для аутентификации

B) Для шифрования

C) Для связывания всех spans одного запроса через сервисы

D) Для версионирования

---

## Question 7: OpenTelemetry







Что такое OpenTelemetry?

A) База данных

B) Стандарт и SDK для инструментации (logs, metrics, traces)

C) Протокол мониторинга

D) Облачный сервис

---

## Question 8: Context Propagation







Что такое context propagation в distributed tracing?

A) Распространение ошибок

B) Копирование логов

C) Синхронизация времени

D) Передача trace context между сервисами через headers

---

## Question 9: Log Levels







Какой log level использовать для нормальных событий в production?

A) ERROR

B) DEBUG

C) WARNING

D) INFO

---

## Question 10: Correlation







Как связать логи с traces?

A) Использовать одинаковые имена файлов

B) Добавлять trace_id в логи

C) Невозможно связать

D) По timestamp

---

## Question 11: ELK Stack







Что входит в ELK Stack?

A) Express, Linux, Kubernetes

B) Elasticsearch, Logstash, Kibana

C) Etcd, Loki, Kafka

D) Envoy, Linkerd, Kong

---

## Question 12: Jaeger







Для чего используется Jaeger?

A) Для логирования

B) Для CI/CD

C) Для distributed tracing visualization

D) Для сбора метрик

---

## Question 13: Instrumentation







Что такое auto-instrumentation?

A) Генерация документации

B) Ручная настройка каждой функции

C) Автоматическое логирование в файлы

D) Автоматическое добавление tracing без изменения кода

---

## Question 14: High Cardinality







Почему high cardinality в логах может быть проблемой?

A) Растёт размер индекса и стоимость хранения

B) High cardinality не проблема

C) Логи становятся красивее

D) Логи быстрее записываются

---

## Question 15: Debugging Workflow







Какой типичный workflow debugging с observability?

A) Metrics → Traces → Logs (от общего к деталям)

B) Только смотреть логи

C) Только смотреть метрики

D) Перезагрузить сервер

---

## Question 16: Sampling






Что такое sampling в трейсинге?

A) Сжатие метрик

B) Удаление логов

C) Шифрование данных

D) Запись только части трейсов для снижения overhead

---

## Question 17: Baggage






Что такое baggage в distributed tracing?

A) Нагрузка на сеть

B) Дополнительные данные, передаваемые с trace context

C) Backup трейсов

D) Архив логов

---

## Question 18: RED method






Что измеряет RED method для сервисов?

A) RAM, Events, Data

B) Request, Error, Disk

C) Rate, Errors, Duration

D) Read, Edit, Delete

---

## Question 19: USE method






Что измеряет USE method для ресурсов?

A) Upload, Send, Execute

B) User, Service, Event

C) Utilization, Saturation, Errors

D) Unit, System, Error

---

## Question 20: Golden Signals






Какие метрики входят в Golden Signals?

A) Latency, Traffic, Errors, Saturation

B) Read, Write, Execute, Delete

C) Input, Process, Output, Store

D) CPU, Memory, Disk, Network

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Observability позволяет исследовать неизвестные проблемы |
| 2 | A | Logs, Metrics, Traces — три столпа |
| 3 | B | JSON легко парсить и искать |
| 4 | B | Trace показывает путь запроса через сервисы |
| 5 | A | Span — единица работы, операция в сервисе |
| 6 | C | trace_id связывает все spans одного запроса |
| 7 | B | OpenTelemetry — стандарт для instrumentation |
| 8 | D | Context propagation — передача trace context через headers |
| 9 | D | INFO для нормальных событий |
| 10 | B | trace_id в логах для корреляции |
| 11 | B | Elasticsearch, Logstash, Kibana |
| 12 | C | Jaeger для distributed tracing visualization |
| 13 | D | Auto-instrumentation добавляет tracing автоматически |
| 14 | A | High cardinality увеличивает размер индекса и стоимость |
| 15 | A | Metrics → Traces → Logs (от общего к деталям) |
| 16 | D | Sampling записывает только часть трейсов для снижения overhead |
| 17 | B | Baggage — дополнительные данные передаваемые с trace context |
| 18 | C | RED: Rate, Errors, Duration — метрики для сервисов |
| 19 | C | USE: Utilization, Saturation, Errors — метрики для ресурсов |
| 20 | A | Golden Signals: Latency, Traffic, Errors, Saturation |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Переходите к SRE. |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите трейсинг. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте корреляцию. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Изучите три столпа детальнее. |

---

