# Мониторинг систем - Quiz

Проверьте свои знания по Prometheus, Grafana и практикам мониторинга.

---

## Question 1: Типы метрик







Какой тип метрики подходит для подсчёта HTTP запросов?

A) Gauge

B) Summary

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

A) Через message queue

B) Через базу данных

C) Prometheus сам забирает метрики с /metrics endpoint

D) Приложения отправляют метрики в Prometheus

---

## Question 4: PromQL







Какой PromQL запрос вычисляет rate (скорость изменения counter)?

A) sum(http_requests_total)

B) http_requests_total / 60

C) avg(http_requests_total)

D) rate(http_requests_total[5m])

---

## Question 5: USE Method







Для чего предназначен USE метод?

A) Для мониторинга ресурсов (CPU, Memory, Disk, Network)

B) Для логирования

C) Для мониторинга сервисов

D) Для трейсинга

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

A) max(http_request_duration_seconds)

B) avg(http_request_duration_seconds)

C) sum(http_request_duration_seconds)

D) histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

---

## Question 9: Labels







Какие labels плохо использовать (высокая кардинальность)?

A) service="api"

B) status="200"

C) user_id="unique_per_user"

D) method="GET"

---

## Question 10: Alertmanager







Что делает Alertmanager?

A) Собирает метрики

B) Хранит данные

C) Визуализирует дашборды

D) Маршрутизирует и отправляет уведомления об алертах

---

## Question 11: Four Golden Signals







Какой сигнал НЕ входит в Four Golden Signals от Google SRE?

A) Traffic

B) Errors

C) Latency

D) Memory

---

## Question 12: Alert Best Practices







На что лучше настраивать алерты?

A) На причины проблем

B) На все возможные метрики

C) На симптомы проблем

D) Только на критические ошибки

---

## Question 13: Grafana







Для чего используется Grafana?

A) Для визуализации метрик и создания дашбордов

B) Для деплоя

C) Для логирования

D) Для сбора метрик

---

## Question 14: Scrape Interval







Что такое scrape_interval в Prometheus?

A) Задержка алертов

B) Время хранения данных

C) Интервал между сборами метрик с targets

D) Время между запусками Prometheus

---

## Question 15: For Clause







Для чего нужен 'for' clause в правилах алертов Prometheus?

A) Для форматирования

B) Для группировки

C) Чтобы алерт сработал только если условие истинно определённое время

D) Для ускорения алертов

---

## Question 16: Node Exporter







Что мониторит Node Exporter?

A) Database queries

B) Application метрики

C) Host-level метрики (CPU, memory, disk, network)

D) Kubernetes pods

---

## Question 17: CPU Utilization







Как измерить CPU utilization в процентах через node_exporter?

A) cpu_usage

B) node_cpu_percent

C) node_cpu_total

D) 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

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

A) Prometheus не поддерживает Kubernetes

B) DNS lookup

C) kubernetes_sd_configs

D) Ручная настройка static_configs

---

## Question 20: Metric Naming







Какое имя метрики соответствует best practices?

A) requests

B) HTTPRequests

C) http_requests_total

D) http-requests-count

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Counter — для подсчёта событий (монотонно возрастает) |
| 2 | B | Counter только растёт, Gauge может расти и уменьшаться |
| 3 | C | Prometheus pull model — сам забирает метрики с targets |
| 4 | D | rate() вычисляет скорость изменения counter за период |
| 5 | A | USE (Utilization, Saturation, Errors) для ресурсов |
| 6 | C | RED: Rate, Errors, Duration — для сервисов |
| 7 | C | Histogram для распределений (latency, размеры) |
| 8 | D | histogram_quantile(0.99, ...) для P99 |
| 9 | C | user_id — высокая кардинальность, убьёт Prometheus |
| 10 | D | Alertmanager маршрутизирует и отправляет notifications |
| 11 | D | Four Golden Signals: Latency, Traffic, Errors, Saturation |
| 12 | C | Алерты на симптомы, причины ищем при debugging |
| 13 | A | Grafana для визуализации и дашбордов |
| 14 | C | scrape_interval — как часто собирать метрики |
| 15 | C | 'for' требует, чтобы условие было истинно N времени |
| 16 | C | Node Exporter — host-level метрики |
| 17 | D | 100 - idle процент = utilization |
| 18 | B | inhibit_rules подавляют менее важные алерты |
| 19 | C | kubernetes_sd_configs для service discovery в K8s |
| 20 | C | http_requests_total — snake_case с _total для counters |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете мониторинг. Переходите к Observability. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите PromQL и методы мониторинга. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте USE/RED методы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы Prometheus. |

---

