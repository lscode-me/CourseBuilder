# Процессы DevOps - Quiz

Проверьте свои знания по жизненному циклу DevOps, планированию и регламентам.

---

## Question 1: DevOps Lifecycle

Какая фаза DevOps lifecycle следует сразу после "Build"?

A) Code

B) Deploy

C) Release

D) Test

---

## Question 2: Value Stream

Что измеряет Process Cycle Efficiency?

A) Скорость deployment

B) Количество багов на 1000 строк кода

C) Отношение времени работы к общему lead time

D) Количество deployments в день

---

## Question 3: OKRs

Чем Key Result отличается от Objective в OKR?

A) Objective качественный, Key Result измеримый

B) Objective для команды, Key Result для индивидуумов

C) Key Result качественный, Objective количественный

D) Это одно и то же

---

## Question 4: Waste Types

Что из перечисленного является примером waste типа "handoffs"?

A) Передача задачи от Dev к QA к Ops

B) Написание ненужных фич

C) Ожидание code review

D) Исправление багов в production

---

## Question 5: Runbook

Что должен содержать хороший runbook?

A) Исходный код сервиса

B) Историю всех инцидентов

C) Только команды для выполнения

D) Пошаговые инструкции, prerequisites, rollback план

---

## Question 6: ADR

Что такое Architecture Decision Record (ADR)?

A) Лог ошибок приложения

B) Запись о каждом merge request

C) Результаты performance тестирования

D) Документ, фиксирующий важное архитектурное решение и его контекст

---

## Question 7: Change Types

Что характеризует "Standard Change" в change management?

A) Требует CAB approval

B) Изменение с высоким риском

C) Pre-approved, автоматизированное, низкорисковое

D) Экстренное изменение при инциденте

---

## Question 8: Semantic Versioning

Какая версия должна следовать после 2.4.1, если добавлена новая функция без breaking changes?

A) 2.4.1.1

B) 2.5.0

C) 3.0.0

D) 2.4.2

---

## Question 9: On-Call

Какова основная обязанность primary on-call?

A) Проведение code review

B) Написание нового кода

C) Планирование спринтов

D) Первая линия реагирования на алерты

---

## Question 10: Capacity Planning

При расчёте capacity команды из 5 человек на 2-недельный спринт, что следует учесть?

A) Только story points предыдущего спринта

B) Количество открытых багов

C) Только количество рабочих дней

D) Рабочие дни, PTO, время на meetings и ops work

---

## Question 11: Retrospective

Какой формат ретроспективы фокусируется на "Что начать/прекратить/продолжить делать"?

A) SWOT Analysis

B) Fishbone Diagram

C) Start/Stop/Continue

D) 5 Whys

---

## Question 12: 5 Whys

Для чего используется техника "5 Whys"?

A) Для приоритизации backlog

B) Для планирования спринта

C) Для оценки задач в story points

D) Для поиска root cause проблемы

---

## Question 13: Daily Standup

Что из перечисленного является anti-pattern для daily standup?

A) 15 минут длительность

B) Обсуждение production status

C) Каждый говорит о блокерах

D) Детальные технические дискуссии

---

## Question 14: Value Stream Mapping

Что выявляет Value Stream Mapping?

A) Waste и bottlenecks в процессе доставки

B) Требования к продукту

C) Количество разработчиков в команде

D) Бюджет проекта

---

## Question 15: Release Management

Чем Incremental Release отличается от Big Bang Release?

A) Big Bang — много маленьких релизов, Incremental — один большой

B) Это одно и то же

C) Incremental только для hotfixes

D) Incremental — много маленьких релизов, Big Bang — один большой

---

## Question 16: Change Advisory Board

Когда DevOps команде нужен CAB approval?

A) Для каждого деплоя

B) Только для изменений в документации

C) Никогда — CAB несовместим с DevOps

D) Для high-risk изменений, затрагивающих много команд

---

## Question 17: On-Call Handoff

Что должен содержать документ on-call handoff?

A) Только имена on-call инженеров

B) Зарплаты членов команды

C) Активные issues, недавние инциденты, запланированные работы

D) Код последнего релиза

---

## Question 18: Process Time vs Wait Time

В Value Stream, если Process Time = 8 часов, Wait Time = 32 часа, чему равна Efficiency?

A) 40%

B) 20%

C) 25%

D) 80%

---

## Question 19: Release Notes

Что из перечисленного должно быть в Release Notes?

A) Только список багфиксов

B) Имена всех разработчиков компании

C) Полный исходный код

D) Новые функции, багфиксы, breaking changes, migration guide

---

## Question 20: Ceremonies

Какая церемония проводится реже всего?

A) Sprint Retrospective

B) Weekly Planning

C) OKR Planning (Quarterly)

D) Daily Standup

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | DevOps lifecycle: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor |
| 2 | C | PCE = Value-add time / Total lead time × 100%. Показывает долю полезной работы |
| 3 | A | Objective — качественная цель (что), Key Result — измеримый результат (как) |
| 4 | A | Handoffs — передача работы между людьми/командами, создающая задержки |
| 5 | D | Runbook должен содержать всё необходимое для выполнения задачи любым членом команды |
| 6 | D | ADR документирует решение, контекст, альтернативы и последствия |
| 7 | C | Standard change — типовое, заранее одобренное изменение с низким риском |
| 8 | B | Minor version (x.Y.z) увеличивается при добавлении функций без breaking changes |
| 9 | D | Primary on-call — первая линия реагирования, triage, эскалация |
| 10 | D | Capacity учитывает реальное доступное время: минус PTO, meetings, ops work |
| 11 | C | Start/Stop/Continue — простой формат для выявления улучшений |
| 12 | D | 5 Whys — техника поиска root cause путём последовательных "почему?" |
| 13 | D | Детальные технические дискуссии выходят за рамки 15-минутного standup |
| 14 | A | VSM визуализирует весь поток для выявления waste и узких мест |
| 15 | D | Incremental — частые маленькие релизы, Big Bang — редкие большие |
| 16 | D | CAB нужен для изменений с высоким риском или широким влиянием |
| 17 | C | Handoff обеспечивает continuity знаний между сменами |
| 18 | B | Efficiency = PT / (PT + WT) = 8 / (8 + 32) = 8/40 = 20% |
| 19 | D | Release notes информируют о всех изменениях и как мигрировать |
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

