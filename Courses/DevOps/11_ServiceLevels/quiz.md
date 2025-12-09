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

A) Инструмент мониторинга

B) Тип метрики

C) Целевое значение SLI

D) Юридический контракт

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

A) SLI / SLO

B) SLO - 100%

C) SLA - SLO

D) 100% - SLO (или 1 - SLO)

---

## Question 5: 99.9% SLO





Сколько минут downtime в месяц допускает 99.9% SLO?

A) ~4.3 минуты

B) ~43 минуты

C) 0 минут

D) 7.2 часа

---

## Question 6: Good SLI





Что НЕ является хорошим SLI?

A) % successful HTTP requests

B) % successful logins

C) P99 response time

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

## Question 11: Latency SLI




Какой хороший SLI для latency?

A) Количество серверов

B) Размер логов

C) Средний CPU

D) p99 latency < 200ms

---

## Question 12: Multi-Window Alert




Что такое multi-window alerting для SLO?

A) Проверка burn rate на разных временных окнах

B) Много браузеров

C) Несколько дата центров

D) Несколько мониторов

---

## Question 13: Composite SLO




Когда используется composite SLO?

A) Для простых сервисов

B) Никогда

C) Только для UI

D) Когда сервис зависит от нескольких компонентов

---

## Question 14: User Journey SLI




Что такое user journey SLI?

A) История логинов

B) Возраст пользователя

C) Географическое положение

D) SLI измеряющий весь путь пользователя, не отдельные сервисы

---

## Question 15: SLO Document




Что должен содержать SLO document?

A) Только код

B) Только алерты

C) Только метрики

D) SLI definition, target, consequences, review process

---

## Question 16: Rolling Window




Что такое rolling window для SLO?

A) Вид тестирования

B) Скользящий период для расчёта (напр. 30 дней)

C) Окно в офисе

D) Тип деплоя

---

## Question 17: SLO Review




Как часто следует пересматривать SLO?

A) Только при проблемах

B) Регулярно (квартально) и после значительных изменений

C) Никогда

D) Ежедневно

---

## Question 18: Achievable SLO




Какой SLO считается achievable?

A) Любой высокий

B) Всегда 99.999%

C) 100%

D) Реалистичный на основе исторических данных

---

## Question 19: Consequences




Какие consequences обычно определяются для нарушения SLO?

A) Приостановка фич релизов, фокус на reliability

B) Штрафы для сотрудников

C) Ничего

D) Увольнения

---

## Question 20: SLI Specification




Что важно при определении SLI specification?

A) Только порог

B) Точное определение что измеряется, откуда данные, как агрегируются

C) Только алерт

D) Только название

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | SLI — количественная метрика надёжности |
| 2 | C | SLO — target value для SLI |
| 3 | B | SLA — юридический контракт с компенсациями |
| 4 | D | Error Budget = 1 - SLO |
| 5 | B | 0.1% от 43200 минут = ~43 минуты |
| 6 | D | CPU usage не user-centric |
| 7 | A | При исчерпании — фокус на reliability |
| 8 | B | SLO строже, чтобы иметь запас до SLA |
| 9 | C | Availability = successful / total requests |
| 10 | A | Burn rate — скорость расходования budget |
| 11 | D | p99 latency < 200ms — хороший latency SLI |
| 12 | A | Multi-window проверяет burn rate на разных окнах |
| 13 | D | Composite SLO когда сервис зависит от нескольких компонентов |
| 14 | D | User journey SLI измеряет весь путь пользователя |
| 15 | D | SLO document: SLI, target, consequences, review process |
| 16 | B | Rolling window — скользящий период расчёта |
| 17 | B | SLO пересматриваются регулярно и после изменений |
| 18 | D | Achievable SLO реалистичен на основе исторических данных |
| 19 | A | Consequences: приостановка фич, фокус на reliability |
| 20 | B | SLI specification: что, откуда, как агрегируется |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Incidents. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте SLI vs SLO vs SLA. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы. |

---

