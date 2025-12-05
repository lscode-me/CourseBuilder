# Observability - Quiz

Проверьте свои знания по трём столпам observability.

---

## Question 1: Monitoring vs Observability

Чем observability отличается от мониторинга?

A) Observability дешевле

B) Monitoring — предопределённые проверки, Observability — исследование неизвестных проблем

C) Это одно и то же

D) Observability только для микросервисов

---

## Question 2: Three Pillars

Какие три столпа observability?

A) CPU, Memory, Disk

B) Logs, Metrics, Traces

C) Prometheus, Grafana, Alertmanager

D) HTTP, TCP, UDP

---

## Question 3: Structured Logging

Почему structured logging (JSON) лучше plain text?

A) JSON красивее

B) Легче парсить, искать, агрегировать

C) Меньше размер файлов

D) Быстрее записывается

---

## Question 4: Traces

Что показывает distributed trace?

A) Только ошибки

B) Путь запроса через сервисы с timing информацией

C) Размер базы данных

D) Количество пользователей

---

## Question 5: Span

Что такое span в контексте tracing?

A) Период времени без активности

B) Единица работы в trace (операция в одном сервисе)

C) Ошибка в логах

D) Тип метрики

---

## Question 6: Trace ID

Для чего используется trace_id?

A) Для аутентификации

B) Для связывания всех spans одного запроса через сервисы

C) Для шифрования

D) Для версионирования

---

## Question 7: OpenTelemetry

Что такое OpenTelemetry?

A) Протокол мониторинга

B) Стандарт и SDK для инструментации (logs, metrics, traces)

C) Облачный сервис

D) База данных

---

## Question 8: Context Propagation

Что такое context propagation в distributed tracing?

A) Распространение ошибок

B) Передача trace context между сервисами через headers

C) Копирование логов

D) Синхронизация времени

---

## Question 9: Log Levels

Какой log level использовать для нормальных событий в production?

A) DEBUG

B) INFO

C) WARNING

D) ERROR

---

## Question 10: Correlation

Как связать логи с traces?

A) По timestamp

B) Добавлять trace_id в логи

C) Использовать одинаковые имена файлов

D) Невозможно связать

---

## Question 11: ELK Stack

Что входит в ELK Stack?

A) Express, Linux, Kubernetes

B) Elasticsearch, Logstash, Kibana

C) Envoy, Linkerd, Kong

D) Etcd, Loki, Kafka

---

## Question 12: Jaeger

Для чего используется Jaeger?

A) Для сбора метрик

B) Для distributed tracing visualization

C) Для логирования

D) Для CI/CD

---

## Question 13: Instrumentation

Что такое auto-instrumentation?

A) Ручная настройка каждой функции

B) Автоматическое добавление tracing без изменения кода

C) Автоматическое логирование в файлы

D) Генерация документации

---

## Question 14: High Cardinality

Почему high cardinality в логах может быть проблемой?

A) Логи становятся красивее

B) Растёт размер индекса и стоимость хранения

C) Логи быстрее записываются

D) High cardinality не проблема

---

## Question 15: Debugging Workflow

Какой типичный workflow debugging с observability?

A) Только смотреть логи

B) Metrics → Traces → Logs (от общего к деталям)

C) Только смотреть метрики

D) Перезагрузить сервер

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Observability позволяет исследовать неизвестные проблемы |
| 2 | B | Logs, Metrics, Traces — три столпа |
| 3 | B | JSON легко парсить и искать |
| 4 | B | Trace показывает путь запроса через сервисы |
| 5 | B | Span — единица работы, операция в сервисе |
| 6 | B | trace_id связывает все spans одного запроса |
| 7 | B | OpenTelemetry — стандарт для instrumentation |
| 8 | B | Context propagation — передача trace context через headers |
| 9 | B | INFO для нормальных событий |
| 10 | B | trace_id в логах для корреляции |
| 11 | B | Elasticsearch, Logstash, Kibana |
| 12 | B | Jaeger для distributed tracing visualization |
| 13 | B | Auto-instrumentation добавляет tracing автоматически |
| 14 | B | High cardinality увеличивает размер индекса и стоимость |
| 15 | B | Metrics → Traces → Logs (от общего к деталям) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Переходите к SRE. |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите трейсинг. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте корреляцию. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Изучите три столпа детальнее. |

---

