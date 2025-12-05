# Observability - Quiz

Проверьте свои знания по трём столпам observability.

---

## Question 1: Monitoring vs Observability


Чем observability отличается от мониторинга?

A) Это одно и то же

B) Observability только для микросервисов

C) Observability дешевле

D) Monitoring — предопределённые проверки, Observability — исследование неизвестных проблем

---

## Question 2: Three Pillars


Какие три столпа observability?

A) HTTP, TCP, UDP

B) CPU, Memory, Disk

C) Prometheus, Grafana, Alertmanager

D) Logs, Metrics, Traces

---

## Question 3: Structured Logging


Почему structured logging (JSON) лучше plain text?

A) Легче парсить, искать, агрегировать

B) Быстрее записывается

C) JSON красивее

D) Меньше размер файлов

---

## Question 4: Traces


Что показывает distributed trace?

A) Путь запроса через сервисы с timing информацией

B) Количество пользователей

C) Только ошибки

D) Размер базы данных

---

## Question 5: Span


Что такое span в контексте tracing?

A) Единица работы в trace (операция в одном сервисе)

B) Ошибка в логах

C) Тип метрики

D) Период времени без активности

---

## Question 6: Trace ID


Для чего используется trace_id?

A) Для версионирования

B) Для связывания всех spans одного запроса через сервисы

C) Для аутентификации

D) Для шифрования

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

A) По timestamp

B) Использовать одинаковые имена файлов

C) Добавлять trace_id в логи

D) Невозможно связать

---

## Question 11: ELK Stack


Что входит в ELK Stack?

A) Envoy, Linkerd, Kong

B) Etcd, Loki, Kafka

C) Elasticsearch, Logstash, Kibana

D) Express, Linux, Kubernetes

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

A) Автоматическое добавление tracing без изменения кода

B) Ручная настройка каждой функции

C) Автоматическое логирование в файлы

D) Генерация документации

---

## Question 14: High Cardinality


Почему high cardinality в логах может быть проблемой?

A) High cardinality не проблема

B) Логи быстрее записываются

C) Растёт размер индекса и стоимость хранения

D) Логи становятся красивее

---

## Question 15: Debugging Workflow


Какой типичный workflow debugging с observability?

A) Metrics → Traces → Logs (от общего к деталям)

B) Только смотреть логи

C) Только смотреть метрики

D) Перезагрузить сервер

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Observability позволяет исследовать неизвестные проблемы |
| 2 | D | Logs, Metrics, Traces — три столпа |
| 3 | A | JSON легко парсить и искать |
| 4 | A | Trace показывает путь запроса через сервисы |
| 5 | A | Span — единица работы, операция в сервисе |
| 6 | B | trace_id связывает все spans одного запроса |
| 7 | B | OpenTelemetry — стандарт для instrumentation |
| 8 | B | Context propagation — передача trace context через headers |
| 9 | A | INFO для нормальных событий |
| 10 | C | trace_id в логах для корреляции |
| 11 | C | Elasticsearch, Logstash, Kibana |
| 12 | B | Jaeger для distributed tracing visualization |
| 13 | A | Auto-instrumentation добавляет tracing автоматически |
| 14 | C | High cardinality увеличивает размер индекса и стоимость |
| 15 | A | Metrics → Traces → Logs (от общего к деталям) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Переходите к SRE. |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите трейсинг. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте корреляцию. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Изучите три столпа детальнее. |

---

