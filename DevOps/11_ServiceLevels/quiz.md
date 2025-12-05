# Service Levels - Quiz

Проверьте свои знания по SLI, SLO, SLA и Error Budgets.

---

## Question 1: SLI

Что такое SLI?

A) Service Level Insurance

B) Количественная метрика надёжности сервиса

C) Контракт с клиентом

D) Внутренняя цель команды

---

## Question 2: SLO

Что такое SLO?

A) Юридический контракт

B) Целевое значение SLI

C) Тип метрики

D) Инструмент мониторинга

---

## Question 3: SLA

Что отличает SLA от SLO?

A) SLA = SLO

B) SLA — юридический контракт с последствиями

C) SLA всегда выше SLO

D) SLA не измеряется

---

## Question 4: Error Budget

Как рассчитывается Error Budget?

A) SLO - 100%

B) 100% - SLO (или 1 - SLO)

C) SLA - SLO

D) SLI / SLO

---

## Question 5: 99.9% SLO

Сколько минут downtime в месяц допускает 99.9% SLO?

A) 7.2 часа

B) ~43 минуты

C) ~4.3 минуты

D) 0 минут

---

## Question 6: Good SLI

Что НЕ является хорошим SLI?

A) % successful HTTP requests

B) P99 response time

C) CPU usage

D) % successful logins

---

## Question 7: Budget Exhausted

Что делать при исчерпании error budget?

A) Продолжать релизить фичи

B) Остановить feature releases, фокус на reliability

C) Увеличить SLO

D) Игнорировать

---

## Question 8: SLO vs SLA

Какое соотношение правильное?

A) SLO = SLA

B) SLO < SLA (менее строгий)

C) SLO > SLA (более строгий)

D) Не связаны

---

## Question 9: Availability SLI

Как измеряется availability SLI?

A) CPU usage

B) successful_requests / total_requests

C) Memory usage

D) Disk space

---

## Question 10: Burn Rate

Что показывает burn rate в SLO alerting?

A) Температуру сервера

B) Скорость расходования error budget

C) Количество пользователей

D) Размер логов

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | SLI — количественная метрика надёжности |
| 2 | B | SLO — target value для SLI |
| 3 | B | SLA — юридический контракт с компенсациями |
| 4 | B | Error Budget = 1 - SLO |
| 5 | B | 0.1% от 43200 минут = ~43 минуты |
| 6 | C | CPU usage не user-centric |
| 7 | B | При исчерпании — фокус на reliability |
| 8 | C | SLO строже, чтобы иметь запас до SLA |
| 9 | B | Availability = successful / total requests |
| 10 | B | Burn rate — скорость расходования budget |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Incidents. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте SLI vs SLO vs SLA. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы. |

---

