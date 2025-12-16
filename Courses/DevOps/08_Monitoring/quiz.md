# Мониторинг систем - Quiz

Проверьте свои знания по Prometheus, Grafana и практикам мониторинга.

---

## Question 1: Типы метрик

Какой тип метрики подходит для подсчёта HTTP запросов?

A) Summary

B) Gauge

C) Counter

D) Histogram

---

## Question 2: Counter vs Gauge

Чем Counter отличается от Gauge?

A) Gauge быстрее

B) Counter только возрастает, Gauge может расти и уменьшаться

C) Это одно и то же

D) Counter для текстовых значений

---

## Question 3: Prometheus Pull Model

Как Prometheus собирает метрики?

A) Prometheus сам забирает метрики с /metrics endpoint

B) Через базу данных

C) Приложения отправляют метрики в Prometheus

D) Через message queue

---

## Question 4: PromQL

Какой PromQL запрос вычисляет rate (скорость изменения counter)?

A) rate(http_requests_total[5m])

B) avg(http_requests_total)

C) sum(http_requests_total)

D) http_requests_total / 60

---

## Question 5: USE Method

Для чего предназначен USE метод?

A) Для мониторинга ресурсов (CPU, Memory, Disk, Network)

B) Для логирования

C) Для трейсинга

D) Для мониторинга сервисов

---

## Question 6: RED Method

Какие метрики включает RED метод?

A) Resources, Endpoints, Dependencies

B) Read, Edit, Delete

C) Rate, Errors, Duration

D) Requests, Events, Data

---

## Question 7: Histogram

Для чего используется histogram в Prometheus?

A) Для логирования

B) Для подсчёта событий

C) Для измерения распределения значений (latency, size)

D) Для хранения текста

---

## Question 8: Percentiles

Как вычислить P99 latency в PromQL?

A) avg(http_request_duration_seconds)

B) histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

C) sum(http_request_duration_seconds)

D) max(http_request_duration_seconds)

---

## Question 9: Labels

Какие labels плохо использовать (высокая кардинальность)?

A) service="api"

B) user_id="unique_per_user"

C) method="GET"

D) status="200"

---

## Question 10: Alertmanager

Что делает Alertmanager?

A) Собирает метрики

B) Визуализирует дашборды

C) Маршрутизирует и отправляет уведомления об алертах

D) Хранит данные

---

## Question 11: Four Golden Signals

Какой сигнал НЕ входит в Four Golden Signals от Google SRE?

A) Traffic

B) Latency

C) Errors

D) Memory

---

## Question 12: Alert Best Practices

На что лучше настраивать алерты?

A) Только на критические ошибки

B) На симптомы проблем

C) На все возможные метрики

D) На причины проблем

---

## Question 13: Grafana

Для чего используется Grafana?

A) Для визуализации метрик и создания дашбордов

B) Для деплоя

C) Для сбора метрик

D) Для логирования

---

## Question 14: Scrape Interval

Что такое scrape_interval в Prometheus?

A) Время между запусками Prometheus

B) Время хранения данных

C) Задержка алертов

D) Интервал между сборами метрик с targets

---

## Question 15: For Clause

Для чего нужен 'for' clause в правилах алертов Prometheus?

A) Для группировки

B) Чтобы алерт сработал только если условие истинно определённое время

C) Для ускорения алертов

D) Для форматирования

---

## Question 16: Node Exporter

Что мониторит Node Exporter?

A) Host-level метрики (CPU, memory, disk, network)

B) Kubernetes pods

C) Application метрики

D) Database queries

---

## Question 17: CPU Utilization

Как измерить CPU utilization в процентах через node_exporter?

A) node_cpu_percent

B) 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

C) cpu_usage

D) node_cpu_total

---

## Question 18: Inhibit Rules

Что делают inhibit_rules в Alertmanager?

A) Подавляют менее важные алерты при срабатывании более важных

B) Ускоряют алерты

C) Группируют алерты

D) Удаляют старые алерты

---

## Question 19: Service Discovery

Как Prometheus может автоматически находить targets в Kubernetes?

A) Prometheus не поддерживает Kubernetes

B) kubernetes_sd_configs

C) DNS lookup

D) Ручная настройка static_configs

---

## Question 20: Metric Naming

Какое имя метрики соответствует best practices?

A) http-requests-count

B) http_requests_total

C) HTTPRequests

D) requests

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Counter — для подсчёта событий (монотонно возрастает) |
| 2 | B | Counter только растёт, Gauge может расти и уменьшаться |
| 3 | A | Prometheus pull model — сам забирает метрики с targets |
| 4 | A | rate() вычисляет скорость изменения counter за период |
| 5 | A | USE (Utilization, Saturation, Errors) для ресурсов |
| 6 | C | RED: Rate, Errors, Duration — для сервисов |
| 7 | C | Histogram для распределений (latency, размеры) |
| 8 | B | histogram_quantile(0.99, ...) для P99 |
| 9 | B | user_id — высокая кардинальность, убьёт Prometheus |
| 10 | C | Alertmanager маршрутизирует и отправляет notifications |
| 11 | D | Four Golden Signals: Latency, Traffic, Errors, Saturation |
| 12 | B | Алерты на симптомы, причины ищем при debugging |
| 13 | A | Grafana для визуализации и дашбордов |
| 14 | D | scrape_interval — как часто собирать метрики |
| 15 | B | 'for' требует, чтобы условие было истинно N времени |
| 16 | A | Node Exporter — host-level метрики |
| 17 | B | 100 - idle процент = utilization |
| 18 | A | inhibit_rules подавляют менее важные алерты |
| 19 | B | kubernetes_sd_configs для service discovery в K8s |
| 20 | B | http_requests_total — snake_case с _total для counters |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете мониторинг. Переходите к Observability. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите PromQL и методы мониторинга. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте USE/RED методы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы Prometheus. |

---

