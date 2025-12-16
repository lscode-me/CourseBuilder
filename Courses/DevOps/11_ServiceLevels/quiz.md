# Service Levels - Quiz

Проверьте свои знания по SLI, SLO, SLA и Error Budgets.

---

## Question 1: SLI

Что такое SLI?

A) Контракт с клиентом

B) Service Level Insurance

C) Внутренняя цель команды

D) Количественная метрика надёжности сервиса

---

## Question 2: SLO

Что такое SLO?

A) Тип метрики

B) Юридический контракт

C) Целевое значение SLI

D) Инструмент мониторинга

---

## Question 3: SLA

Что отличает SLA от SLO?

A) SLA не измеряется

B) SLA = SLO

C) SLA — юридический контракт с последствиями

D) SLA всегда выше SLO

---

## Question 4: Error Budget

Как рассчитывается Error Budget?

A) 100% - SLO (или 1 - SLO)

B) SLO - 100%

C) SLA - SLO

D) SLI / SLO

---

## Question 5: 99.9% SLO

Сколько минут downtime в месяц допускает 99.9% SLO?

A) 7.2 часа

B) ~4.3 минуты

C) 0 минут

D) ~43 минуты

---

## Question 6: Good SLI

Что НЕ является хорошим SLI?

A) P99 response time

B) % successful logins

C) CPU usage

D) % successful HTTP requests

---

## Question 7: Budget Exhausted

Что делать при исчерпании error budget?

A) Остановить feature releases, фокус на reliability

B) Увеличить SLO

C) Продолжать релизить фичи

D) Игнорировать

---

## Question 8: SLO vs SLA

Какое соотношение правильное?

A) SLO > SLA (более строгий)

B) SLO < SLA (менее строгий)

C) Не связаны

D) SLO = SLA

---

## Question 9: Availability SLI

Как измеряется availability SLI?

A) Disk space

B) CPU usage

C) successful_requests / total_requests

D) Memory usage

---

## Question 10: Burn Rate

Что показывает burn rate в SLO alerting?

A) Количество пользователей

B) Скорость расходования error budget

C) Размер логов

D) Температуру сервера

---

## Question 11: Latency SLI

Какой хороший SLI для latency?

A) Количество серверов

B) Размер логов

C) Средний CPU

D) p99 latency < 200ms

---

## Question 12: Multi-Window Alert

Что такое multi-window alerting для SLO?

A) Несколько мониторов

B) Несколько дата центров

C) Много браузеров

D) Проверка burn rate на разных временных окнах

---

## Question 13: Composite SLO

Когда используется composite SLO?

A) Только для UI

B) Никогда

C) Когда сервис зависит от нескольких компонентов

D) Для простых сервисов

---

## Question 14: User Journey SLI

Что такое user journey SLI?

A) Географическое положение

B) Возраст пользователя

C) SLI измеряющий весь путь пользователя, не отдельные сервисы

D) История логинов

---

## Question 15: SLO Document

Что должен содержать SLO document?

A) Только алерты

B) SLI definition, target, consequences, review process

C) Только код

D) Только метрики

---

## Question 16: Rolling Window

Что такое rolling window для SLO?

A) Вид тестирования

B) Окно в офисе

C) Тип деплоя

D) Скользящий период для расчёта (напр. 30 дней)

---

## Question 17: SLO Review

Как часто следует пересматривать SLO?

A) Ежедневно

B) Никогда

C) Только при проблемах

D) Регулярно (квартально) и после значительных изменений

---

## Question 18: Achievable SLO

Какой SLO считается achievable?

A) Любой высокий

B) Всегда 99.999%

C) Реалистичный на основе исторических данных

D) 100%

---

## Question 19: Consequences

Какие consequences обычно определяются для нарушения SLO?

A) Ничего

B) Увольнения

C) Приостановка фич релизов, фокус на reliability

D) Штрафы для сотрудников

---

## Question 20: SLI Specification

Что важно при определении SLI specification?

A) Точное определение что измеряется, откуда данные, как агрегируются

B) Только порог

C) Только алерт

D) Только название

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | SLI — количественная метрика надёжности |
| 2 | C | SLO — target value для SLI |
| 3 | C | SLA — юридический контракт с компенсациями |
| 4 | A | Error Budget = 1 - SLO |
| 5 | D | 0.1% от 43200 минут = ~43 минуты |
| 6 | C | CPU usage не user-centric |
| 7 | A | При исчерпании — фокус на reliability |
| 8 | A | SLO строже, чтобы иметь запас до SLA |
| 9 | C | Availability = successful / total requests |
| 10 | B | Burn rate — скорость расходования budget |
| 11 | D | p99 latency < 200ms — хороший latency SLI |
| 12 | D | Multi-window проверяет burn rate на разных окнах |
| 13 | C | Composite SLO когда сервис зависит от нескольких компонентов |
| 14 | C | User journey SLI измеряет весь путь пользователя |
| 15 | B | SLO document: SLI, target, consequences, review process |
| 16 | D | Rolling window — скользящий период расчёта |
| 17 | D | SLO пересматриваются регулярно и после изменений |
| 18 | C | Achievable SLO реалистичен на основе исторических данных |
| 19 | C | Consequences: приостановка фич, фокус на reliability |
| 20 | A | SLI specification: что, откуда, как агрегируется |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Incidents. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте SLI vs SLO vs SLA. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы. |

---

