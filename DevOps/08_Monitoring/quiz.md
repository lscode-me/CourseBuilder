# Мониторинг систем - Quiz

Проверьте свои знания по Prometheus, Grafana и практикам мониторинга.

---

## Question 1: Типы метрик


Какой тип метрики подходит для подсчёта HTTP запросов?

A) Summary

B) Gauge

C) Histogram

D) Counter

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

A) Prometheus сам забирает метрики с /metrics endpoint

B) Через базу данных

C) Приложения отправляют метрики в Prometheus

D) Через message queue

---

## Question 4: PromQL


Какой PromQL запрос вычисляет rate (скорость изменения counter)?

A) avg(http_requests_total)

B) rate(http_requests_total[5m])

C) http_requests_total / 60

D) sum(http_requests_total)

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

B) Rate, Errors, Duration

C) Read, Edit, Delete

D) Requests, Events, Data

---

## Question 7: Histogram


Для чего используется histogram в Prometheus?

A) Для подсчёта событий

B) Для хранения текста

C) Для измерения распределения значений (latency, size)

D) Для логирования

---

## Question 8: Percentiles


Как вычислить P99 latency в PromQL?

A) histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

B) avg(http_request_duration_seconds)

C) max(http_request_duration_seconds)

D) sum(http_request_duration_seconds)

---

## Question 9: Labels


Какие labels плохо использовать (высокая кардинальность)?

A) status="200"

B) method="GET"

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

A) Errors

B) Traffic

C) Latency

D) Memory

---

## Question 12: Alert Best Practices


На что лучше настраивать алерты?

A) На причины проблем

B) На все возможные метрики

C) Только на критические ошибки

D) На симптомы проблем

---

## Question 13: Grafana


Для чего используется Grafana?

A) Для логирования

B) Для сбора метрик

C) Для деплоя

D) Для визуализации метрик и создания дашбордов

---

## Question 14: Scrape Interval


Что такое scrape_interval в Prometheus?

A) Время между запусками Prometheus

B) Интервал между сборами метрик с targets

C) Задержка алертов

D) Время хранения данных

---

## Question 15: For Clause


Для чего нужен 'for' clause в правилах алертов Prometheus?

A) Для группировки

B) Для форматирования

C) Чтобы алерт сработал только если условие истинно определённое время

D) Для ускорения алертов

---

## Question 16: Node Exporter


Что мониторит Node Exporter?

A) Application метрики

B) Database queries

C) Kubernetes pods

D) Host-level метрики (CPU, memory, disk, network)

---

## Question 17: CPU Utilization


Как измерить CPU utilization в процентах через node_exporter?

A) 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

B) cpu_usage

C) node_cpu_percent

D) node_cpu_total

---

## Question 18: Inhibit Rules


Что делают inhibit_rules в Alertmanager?

A) Удаляют старые алерты

B) Подавляют менее важные алерты при срабатывании более важных

C) Группируют алерты

D) Ускоряют алерты

---

## Question 19: Service Discovery


Как Prometheus может автоматически находить targets в Kubernetes?

A) Prometheus не поддерживает Kubernetes

B) DNS lookup

C) Ручная настройка static_configs

D) kubernetes_sd_configs

---

## Question 20: Metric Naming


Какое имя метрики соответствует best practices?

A) HTTPRequests

B) http-requests-count

C) requests

D) http_requests_total

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Counter — для подсчёта событий (монотонно возрастает) |
| 2 | A | Counter только растёт, Gauge может расти и уменьшаться |
| 3 | A | Prometheus pull model — сам забирает метрики с targets |
| 4 | B | rate() вычисляет скорость изменения counter за период |
| 5 | A | USE (Utilization, Saturation, Errors) для ресурсов |
| 6 | B | RED: Rate, Errors, Duration — для сервисов |
| 7 | C | Histogram для распределений (latency, размеры) |
| 8 | A | histogram_quantile(0.99, ...) для P99 |
| 9 | C | user_id — высокая кардинальность, убьёт Prometheus |
| 10 | B | Alertmanager маршрутизирует и отправляет notifications |
| 11 | D | Four Golden Signals: Latency, Traffic, Errors, Saturation |
| 12 | D | Алерты на симптомы, причины ищем при debugging |
| 13 | D | Grafana для визуализации и дашбордов |
| 14 | B | scrape_interval — как часто собирать метрики |
| 15 | C | 'for' требует, чтобы условие было истинно N времени |
| 16 | D | Node Exporter — host-level метрики |
| 17 | A | 100 - idle процент = utilization |
| 18 | B | inhibit_rules подавляют менее важные алерты |
| 19 | D | kubernetes_sd_configs для service discovery в K8s |
| 20 | D | http_requests_total — snake_case с _total для counters |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете мониторинг. Переходите к Observability. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите PromQL и методы мониторинга. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте USE/RED методы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы Prometheus. |

---

