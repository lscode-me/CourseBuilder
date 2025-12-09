# Service Levels - Quiz

Проверьте свои знания по SLI, SLO, SLA и Error Budgets.

---

## Question 1: SLI


Что такое SLI?

A) Внутренняя цель команды

B) Контракт с клиентом

C) Количественная метрика надёжности сервиса

D) Service Level Insurance

---

## Question 2: SLO


Что такое SLO?

A) Юридический контракт

B) Целевое значение SLI

C) Инструмент мониторинга

D) Тип метрики

---

## Question 3: SLA


Что отличает SLA от SLO?

A) SLA не измеряется

B) SLA — юридический контракт с последствиями

C) SLA = SLO

D) SLA всегда выше SLO

---

## Question 4: Error Budget


Как рассчитывается Error Budget?

A) 100% - SLO (или 1 - SLO)

B) SLA - SLO

C) SLI / SLO

D) SLO - 100%

---

## Question 5: 99.9% SLO


Сколько минут downtime в месяц допускает 99.9% SLO?

A) ~4.3 минуты

B) 0 минут

C) ~43 минуты

D) 7.2 часа

---

## Question 6: Good SLI


Что НЕ является хорошим SLI?

A) P99 response time

B) % successful logins

C) % successful HTTP requests

D) CPU usage

---

## Question 7: Budget Exhausted


Что делать при исчерпании error budget?

A) Остановить feature releases, фокус на reliability

B) Продолжать релизить фичи

C) Игнорировать

D) Увеличить SLO

---

## Question 8: SLO vs SLA


Какое соотношение правильное?

A) SLO = SLA

B) SLO > SLA (более строгий)

C) SLO < SLA (менее строгий)

D) Не связаны

---

## Question 9: Availability SLI


Как измеряется availability SLI?

A) Disk space

B) Memory usage

C) successful_requests / total_requests

D) CPU usage

---

## Question 10: Burn Rate


Что показывает burn rate в SLO alerting?

A) Скорость расходования error budget

B) Размер логов

C) Температуру сервера

D) Количество пользователей

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | SLI — количественная метрика надёжности |
| 2 | B | SLO — target value для SLI |
| 3 | B | SLA — юридический контракт с компенсациями |
| 4 | A | Error Budget = 1 - SLO |
| 5 | C | 0.1% от 43200 минут = ~43 минуты |
| 6 | D | CPU usage не user-centric |
| 7 | A | При исчерпании — фокус на reliability |
| 8 | B | SLO строже, чтобы иметь запас до SLA |
| 9 | C | Availability = successful / total requests |
| 10 | A | Burn rate — скорость расходования budget |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Incidents. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте SLI vs SLO vs SLA. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы. |

---

