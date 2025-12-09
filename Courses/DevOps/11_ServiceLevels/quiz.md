# Service Levels - Quiz

Проверьте свои знания по SLI, SLO, SLA и Error Budgets.

---

## Question 1: SLI







Что такое SLI?

A) Внутренняя цель команды

B) Количественная метрика надёжности сервиса

C) Service Level Insurance

D) Контракт с клиентом

---

## Question 2: SLO







Что такое SLO?

A) Тип метрики

B) Инструмент мониторинга

C) Юридический контракт

D) Целевое значение SLI

---

## Question 3: SLA







Что отличает SLA от SLO?

A) SLA — юридический контракт с последствиями

B) SLA всегда выше SLO

C) SLA = SLO

D) SLA не измеряется

---

## Question 4: Error Budget







Как рассчитывается Error Budget?

A) SLO - 100%

B) SLI / SLO

C) 100% - SLO (или 1 - SLO)

D) SLA - SLO

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

B) Увеличить SLO

C) Продолжать релизить фичи

D) Игнорировать

---

## Question 8: SLO vs SLA







Какое соотношение правильное?

A) SLO > SLA (более строгий)

B) SLO < SLA (менее строгий)

C) SLO = SLA

D) Не связаны

---

## Question 9: Availability SLI







Как измеряется availability SLI?

A) CPU usage

B) Memory usage

C) Disk space

D) successful_requests / total_requests

---

## Question 10: Burn Rate







Что показывает burn rate в SLO alerting?

A) Количество пользователей

B) Размер логов

C) Скорость расходования error budget

D) Температуру сервера

---

## Question 11: Latency SLI






Какой хороший SLI для latency?

A) Размер логов

B) Количество серверов

C) p99 latency < 200ms

D) Средний CPU

---

## Question 12: Multi-Window Alert






Что такое multi-window alerting для SLO?

A) Несколько дата центров

B) Несколько мониторов

C) Проверка burn rate на разных временных окнах

D) Много браузеров

---

## Question 13: Composite SLO






Когда используется composite SLO?

A) Только для UI

B) Когда сервис зависит от нескольких компонентов

C) Для простых сервисов

D) Никогда

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

A) Окно в офисе

B) Тип деплоя

C) Вид тестирования

D) Скользящий период для расчёта (напр. 30 дней)

---

## Question 17: SLO Review






Как часто следует пересматривать SLO?

A) Никогда

B) Ежедневно

C) Только при проблемах

D) Регулярно (квартально) и после значительных изменений

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

A) Только название

B) Только алерт

C) Точное определение что измеряется, откуда данные, как агрегируются

D) Только порог

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | SLI — количественная метрика надёжности |
| 2 | D | SLO — target value для SLI |
| 3 | A | SLA — юридический контракт с компенсациями |
| 4 | C | Error Budget = 1 - SLO |
| 5 | B | 0.1% от 43200 минут = ~43 минуты |
| 6 | D | CPU usage не user-centric |
| 7 | A | При исчерпании — фокус на reliability |
| 8 | A | SLO строже, чтобы иметь запас до SLA |
| 9 | D | Availability = successful / total requests |
| 10 | C | Burn rate — скорость расходования budget |
| 11 | C | p99 latency < 200ms — хороший latency SLI |
| 12 | C | Multi-window проверяет burn rate на разных окнах |
| 13 | B | Composite SLO когда сервис зависит от нескольких компонентов |
| 14 | D | User journey SLI измеряет весь путь пользователя |
| 15 | D | SLO document: SLI, target, consequences, review process |
| 16 | D | Rolling window — скользящий период расчёта |
| 17 | D | SLO пересматриваются регулярно и после изменений |
| 18 | D | Achievable SLO реалистичен на основе исторических данных |
| 19 | A | Consequences: приостановка фич, фокус на reliability |
| 20 | C | SLI specification: что, откуда, как агрегируется |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Incidents. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте SLI vs SLO vs SLA. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы. |

---

