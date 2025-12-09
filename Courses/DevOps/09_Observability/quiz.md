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

A) Для шифрования

B) Для аутентификации

C) Для версионирования

D) Для связывания всех spans одного запроса через сервисы

---

## Question 7: OpenTelemetry





Что такое OpenTelemetry?

A) Облачный сервис

B) Стандарт и SDK для инструментации (logs, metrics, traces)

C) База данных

D) Протокол мониторинга

---

## Question 8: Context Propagation





Что такое context propagation в distributed tracing?

A) Копирование логов

B) Передача trace context между сервисами через headers

C) Синхронизация времени

D) Распространение ошибок

---

## Question 9: Log Levels





Какой log level использовать для нормальных событий в production?

A) INFO

B) ERROR

C) WARNING

D) DEBUG

---

## Question 10: Correlation





Как связать логи с traces?

A) Невозможно связать

B) По timestamp

C) Использовать одинаковые имена файлов

D) Добавлять trace_id в логи

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

A) Для CI/CD

B) Для distributed tracing visualization

C) Для логирования

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

A) Логи быстрее записываются

B) Логи становятся красивее

C) High cardinality не проблема

D) Растёт размер индекса и стоимость хранения

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

A) Запись только части трейсов для снижения overhead

B) Удаление логов

C) Сжатие метрик

D) Шифрование данных

---

## Question 17: Baggage




Что такое baggage в distributed tracing?

A) Дополнительные данные, передаваемые с trace context

B) Архив логов

C) Backup трейсов

D) Нагрузка на сеть

---

## Question 18: RED method




Что измеряет RED method для сервисов?

A) Request, Error, Disk

B) RAM, Events, Data

C) Read, Edit, Delete

D) Rate, Errors, Duration

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

B) CPU, Memory, Disk, Network

C) Read, Write, Execute, Delete

D) Input, Process, Output, Store

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
| 6 | D | trace_id связывает все spans одного запроса |
| 7 | B | OpenTelemetry — стандарт для instrumentation |
| 8 | B | Context propagation — передача trace context через headers |
| 9 | A | INFO для нормальных событий |
| 10 | D | trace_id в логах для корреляции |
| 11 | B | Elasticsearch, Logstash, Kibana |
| 12 | B | Jaeger для distributed tracing visualization |
| 13 | D | Auto-instrumentation добавляет tracing автоматически |
| 14 | D | High cardinality увеличивает размер индекса и стоимость |
| 15 | A | Metrics → Traces → Logs (от общего к деталям) |
| 16 | A | Sampling записывает только часть трейсов для снижения overhead |
| 17 | A | Baggage — дополнительные данные передаваемые с trace context |
| 18 | D | RED: Rate, Errors, Duration — метрики для сервисов |
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

