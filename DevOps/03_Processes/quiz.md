# Процессы DevOps - Quiz

Проверьте свои знания по жизненному циклу DevOps, планированию и регламентам.

---

## Question 1: DevOps Lifecycle

Какая фаза DevOps lifecycle следует сразу после "Build"?

A) Deploy

B) Test

C) Release

D) Code

---

## Question 2: Value Stream

Что измеряет Process Cycle Efficiency?

A) Количество багов на 1000 строк кода

B) Отношение времени работы к общему lead time

C) Скорость deployment

D) Количество deployments в день

---

## Question 3: OKRs

Чем Key Result отличается от Objective в OKR?

A) Key Result качественный, Objective количественный

B) Objective качественный, Key Result измеримый

C) Это одно и то же

D) Objective для команды, Key Result для индивидуумов

---

## Question 4: Waste Types

Что из перечисленного является примером waste типа "handoffs"?

A) Ожидание code review

B) Передача задачи от Dev к QA к Ops

C) Написание ненужных фич

D) Исправление багов в production

---

## Question 5: Runbook

Что должен содержать хороший runbook?

A) Только команды для выполнения

B) Пошаговые инструкции, prerequisites, rollback план

C) Исходный код сервиса

D) Историю всех инцидентов

---

## Question 6: ADR

Что такое Architecture Decision Record (ADR)?

A) Запись о каждом merge request

B) Документ, фиксирующий важное архитектурное решение и его контекст

C) Лог ошибок приложения

D) Результаты performance тестирования

---

## Question 7: Change Types

Что характеризует "Standard Change" в change management?

A) Требует CAB approval

B) Pre-approved, автоматизированное, низкорисковое

C) Экстренное изменение при инциденте

D) Изменение с высоким риском

---

## Question 8: Semantic Versioning

Какая версия должна следовать после 2.4.1, если добавлена новая функция без breaking changes?

A) 2.4.2

B) 2.5.0

C) 3.0.0

D) 2.4.1.1

---

## Question 9: On-Call

Какова основная обязанность primary on-call?

A) Написание нового кода

B) Первая линия реагирования на алерты

C) Проведение code review

D) Планирование спринтов

---

## Question 10: Capacity Planning

При расчёте capacity команды из 5 человек на 2-недельный спринт, что следует учесть?

A) Только количество рабочих дней

B) Рабочие дни, PTO, время на meetings и ops work

C) Только story points предыдущего спринта

D) Количество открытых багов

---

## Question 11: Retrospective

Какой формат ретроспективы фокусируется на "Что начать/прекратить/продолжить делать"?

A) 5 Whys

B) Start/Stop/Continue

C) Fishbone Diagram

D) SWOT Analysis

---

## Question 12: 5 Whys

Для чего используется техника "5 Whys"?

A) Для оценки задач в story points

B) Для поиска root cause проблемы

C) Для планирования спринта

D) Для приоритизации backlog

---

## Question 13: Daily Standup

Что из перечисленного является anti-pattern для daily standup?

A) 15 минут длительность

B) Каждый говорит о блокерах

C) Детальные технические дискуссии

D) Обсуждение production status

---

## Question 14: Value Stream Mapping

Что выявляет Value Stream Mapping?

A) Количество разработчиков в команде

B) Waste и bottlenecks в процессе доставки

C) Требования к продукту

D) Бюджет проекта

---

## Question 15: Release Management

Чем Incremental Release отличается от Big Bang Release?

A) Big Bang — много маленьких релизов, Incremental — один большой

B) Incremental — много маленьких релизов, Big Bang — один большой

C) Это одно и то же

D) Incremental только для hotfixes

---

## Question 16: Change Advisory Board

Когда DevOps команде нужен CAB approval?

A) Для каждого деплоя

B) Для high-risk изменений, затрагивающих много команд

C) Никогда — CAB несовместим с DevOps

D) Только для изменений в документации

---

## Question 17: On-Call Handoff

Что должен содержать документ on-call handoff?

A) Только имена on-call инженеров

B) Активные issues, недавние инциденты, запланированные работы

C) Код последнего релиза

D) Зарплаты членов команды

---

## Question 18: Process Time vs Wait Time

В Value Stream, если Process Time = 8 часов, Wait Time = 32 часа, чему равна Efficiency?

A) 80%

B) 40%

C) 20%

D) 25%

---

## Question 19: Release Notes

Что из перечисленного должно быть в Release Notes?

A) Только список багфиксов

B) Новые функции, багфиксы, breaking changes, migration guide

C) Полный исходный код

D) Имена всех разработчиков компании

---

## Question 20: Ceremonies

Какая церемония проводится реже всего?

A) Daily Standup

B) Sprint Retrospective

C) OKR Planning (Quarterly)

D) Weekly Planning

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DevOps lifecycle: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor |
| 2 | B | PCE = Value-add time / Total lead time × 100%. Показывает долю полезной работы |
| 3 | B | Objective — качественная цель (что), Key Result — измеримый результат (как) |
| 4 | B | Handoffs — передача работы между людьми/командами, создающая задержки |
| 5 | B | Runbook должен содержать всё необходимое для выполнения задачи любым членом команды |
| 6 | B | ADR документирует решение, контекст, альтернативы и последствия |
| 7 | B | Standard change — типовое, заранее одобренное изменение с низким риском |
| 8 | B | Minor version (x.Y.z) увеличивается при добавлении функций без breaking changes |
| 9 | B | Primary on-call — первая линия реагирования, triage, эскалация |
| 10 | B | Capacity учитывает реальное доступное время: минус PTO, meetings, ops work |
| 11 | B | Start/Stop/Continue — простой формат для выявления улучшений |
| 12 | B | 5 Whys — техника поиска root cause путём последовательных "почему?" |
| 13 | C | Детальные технические дискуссии выходят за рамки 15-минутного standup |
| 14 | B | VSM визуализирует весь поток для выявления waste и узких мест |
| 15 | B | Incremental — частые маленькие релизы, Big Bang — редкие большие |
| 16 | B | CAB нужен для изменений с высоким риском или широким влиянием |
| 17 | B | Handoff обеспечивает continuity знаний между сменами |
| 18 | C | Efficiency = PT / (PT + WT) = 8 / (8 + 32) = 8/40 = 20% |
| 19 | B | Release notes информируют о всех изменениях и как мигрировать |
| 20 | C | OKR Planning — ежеквартально, остальные — ежедневно/еженедельно |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете процессы DevOps. Переходите к CI/CD. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Value Stream Mapping и change management. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о планировании. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и примеры. |

---

