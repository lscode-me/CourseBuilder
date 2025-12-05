# Мониторинг систем - Quiz

Проверьте свои знания по Prometheus, Grafana и практикам мониторинга.

---

## Question 1: Типы метрик

Какой тип метрики подходит для подсчёта HTTP запросов?

A) Gauge

B) Counter

C) Histogram

D) Summary

---

## Question 2: Counter vs Gauge

Чем Counter отличается от Gauge?

A) Counter только возрастает, Gauge может расти и уменьшаться

B) Это одно и то же

C) Gauge быстрее

D) Counter для текстовых значений

---

## Question 3: Prometheus Pull Model

Как Prometheus собирает метрики?

A) Приложения отправляют метрики в Prometheus

B) Prometheus сам забирает метрики с /metrics endpoint

C) Через базу данных

D) Через message queue

---

## Question 4: PromQL

Какой PromQL запрос вычисляет rate (скорость изменения counter)?

A) sum(http_requests_total)

B) rate(http_requests_total[5m])

C) avg(http_requests_total)

D) http_requests_total / 60

---

## Question 5: USE Method

Для чего предназначен USE метод?

A) Для мониторинга сервисов

B) Для мониторинга ресурсов (CPU, Memory, Disk, Network)

C) Для логирования

D) Для трейсинга

---

## Question 6: RED Method

Какие метрики включает RED метод?

A) Rate, Errors, Duration

B) Requests, Events, Data

C) Read, Edit, Delete

D) Resources, Endpoints, Dependencies

---

## Question 7: Histogram

Для чего используется histogram в Prometheus?

A) Для подсчёта событий

B) Для измерения распределения значений (latency, size)

C) Для хранения текста

D) Для логирования

---

## Question 8: Percentiles

Как вычислить P99 latency в PromQL?

A) avg(http_request_duration_seconds)

B) histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

C) max(http_request_duration_seconds)

D) sum(http_request_duration_seconds)

---

## Question 9: Labels

Какие labels плохо использовать (высокая кардинальность)?

A) method="GET"

B) status="200"

C) user_id="unique_per_user"

D) service="api"

---

## Question 10: Alertmanager

Что делает Alertmanager?

A) Собирает метрики

B) Маршрутизирует и отправляет уведомления об алертах

C) Визуализирует дашборды

D) Хранит данные

---

## Question 11: Four Golden Signals

Какой сигнал НЕ входит в Four Golden Signals от Google SRE?

A) Latency

B) Traffic

C) Memory

D) Errors

---

## Question 12: Alert Best Practices

На что лучше настраивать алерты?

A) На причины проблем

B) На симптомы проблем

C) На все возможные метрики

D) Только на критические ошибки

---

## Question 13: Grafana

Для чего используется Grafana?

A) Для сбора метрик

B) Для визуализации метрик и создания дашбордов

C) Для логирования

D) Для деплоя

---

## Question 14: Scrape Interval

Что такое scrape_interval в Prometheus?

A) Время между запусками Prometheus

B) Интервал между сборами метрик с targets

C) Время хранения данных

D) Задержка алертов

---

## Question 15: For Clause

Для чего нужен 'for' clause в правилах алертов Prometheus?

A) Для ускорения алертов

B) Чтобы алерт сработал только если условие истинно определённое время

C) Для форматирования

D) Для группировки

---

## Question 16: Node Exporter

Что мониторит Node Exporter?

A) Kubernetes pods

B) Host-level метрики (CPU, memory, disk, network)

C) Application метрики

D) Database queries

---

## Question 17: CPU Utilization

Как измерить CPU utilization в процентах через node_exporter?

A) node_cpu_total

B) 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

C) node_cpu_percent

D) cpu_usage

---

## Question 18: Inhibit Rules

Что делают inhibit_rules в Alertmanager?

A) Ускоряют алерты

B) Подавляют менее важные алерты при срабатывании более важных

C) Удаляют старые алерты

D) Группируют алерты

---

## Question 19: Service Discovery

Как Prometheus может автоматически находить targets в Kubernetes?

A) Ручная настройка static_configs

B) kubernetes_sd_configs

C) DNS lookup

D) Prometheus не поддерживает Kubernetes

---

## Question 20: Metric Naming

Какое имя метрики соответствует best practices?

A) http_requests_total

B) HTTPRequests

C) requests

D) http-requests-count

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Counter — для подсчёта событий (монотонно возрастает) |
| 2 | A | Counter только растёт, Gauge может расти и уменьшаться |
| 3 | B | Prometheus pull model — сам забирает метрики с targets |
| 4 | B | rate() вычисляет скорость изменения counter за период |
| 5 | B | USE (Utilization, Saturation, Errors) для ресурсов |
| 6 | A | RED: Rate, Errors, Duration — для сервисов |
| 7 | B | Histogram для распределений (latency, размеры) |
| 8 | B | histogram_quantile(0.99, ...) для P99 |
| 9 | C | user_id — высокая кардинальность, убьёт Prometheus |
| 10 | B | Alertmanager маршрутизирует и отправляет notifications |
| 11 | C | Four Golden Signals: Latency, Traffic, Errors, Saturation |
| 12 | B | Алерты на симптомы, причины ищем при debugging |
| 13 | B | Grafana для визуализации и дашбордов |
| 14 | B | scrape_interval — как часто собирать метрики |
| 15 | B | 'for' требует, чтобы условие было истинно N времени |
| 16 | B | Node Exporter — host-level метрики |
| 17 | B | 100 - idle процент = utilization |
| 18 | B | inhibit_rules подавляют менее важные алерты |
| 19 | B | kubernetes_sd_configs для service discovery в K8s |
| 20 | A | http_requests_total — snake_case с _total для counters |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете мониторинг. Переходите к Observability. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите PromQL и методы мониторинга. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте USE/RED методы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы Prometheus. |

---

