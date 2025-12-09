# Процессы DevOps - Quiz

Проверьте свои знания по жизненному циклу DevOps, планированию и регламентам.

---

## Question 1: DevOps Lifecycle


Какая фаза DevOps lifecycle следует сразу после "Build"?

A) Deploy

B) Test

C) Code

D) Release

---

## Question 2: Value Stream


Что измеряет Process Cycle Efficiency?

A) Отношение времени работы к общему lead time

B) Скорость deployment

C) Количество багов на 1000 строк кода

D) Количество deployments в день

---

## Question 3: OKRs


Чем Key Result отличается от Objective в OKR?

A) Objective качественный, Key Result измеримый

B) Key Result качественный, Objective количественный

C) Objective для команды, Key Result для индивидуумов

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

B) Только команды для выполнения

C) Историю всех инцидентов

D) Пошаговые инструкции, prerequisites, rollback план

---

## Question 6: ADR


Что такое Architecture Decision Record (ADR)?

A) Документ, фиксирующий важное архитектурное решение и его контекст

B) Лог ошибок приложения

C) Результаты performance тестирования

D) Запись о каждом merge request

---

## Question 7: Change Types


Что характеризует "Standard Change" в change management?

A) Требует CAB approval

B) Pre-approved, автоматизированное, низкорисковое

C) Изменение с высоким риском

D) Экстренное изменение при инциденте

---

## Question 8: Semantic Versioning


Какая версия должна следовать после 2.4.1, если добавлена новая функция без breaking changes?

A) 3.0.0

B) 2.5.0

C) 2.4.2

D) 2.4.1.1

---

## Question 9: On-Call


Какова основная обязанность primary on-call?

A) Написание нового кода

B) Первая линия реагирования на алерты

C) Планирование спринтов

D) Проведение code review

---

## Question 10: Capacity Planning


При расчёте capacity команды из 5 человек на 2-недельный спринт, что следует учесть?

A) Только количество рабочих дней

B) Рабочие дни, PTO, время на meetings и ops work

C) Количество открытых багов

D) Только story points предыдущего спринта

---

## Question 11: Retrospective


Какой формат ретроспективы фокусируется на "Что начать/прекратить/продолжить делать"?

A) Start/Stop/Continue

B) Fishbone Diagram

C) 5 Whys

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

A) Каждый говорит о блокерах

B) Обсуждение production status

C) 15 минут длительность

D) Детальные технические дискуссии

---

## Question 14: Value Stream Mapping


Что выявляет Value Stream Mapping?

A) Бюджет проекта

B) Количество разработчиков в команде

C) Требования к продукту

D) Waste и bottlenecks в процессе доставки

---

## Question 15: Release Management


Чем Incremental Release отличается от Big Bang Release?

A) Incremental — много маленьких релизов, Big Bang — один большой

B) Big Bang — много маленьких релизов, Incremental — один большой

C) Incremental только для hotfixes

D) Это одно и то же

---

## Question 16: Change Advisory Board


Когда DevOps команде нужен CAB approval?

A) Для каждого деплоя

B) Никогда — CAB несовместим с DevOps

C) Только для изменений в документации

D) Для high-risk изменений, затрагивающих много команд

---

## Question 17: On-Call Handoff


Что должен содержать документ on-call handoff?

A) Зарплаты членов команды

B) Активные issues, недавние инциденты, запланированные работы

C) Только имена on-call инженеров

D) Код последнего релиза

---

## Question 18: Process Time vs Wait Time


В Value Stream, если Process Time = 8 часов, Wait Time = 32 часа, чему равна Efficiency?

A) 20%

B) 40%

C) 80%

D) 25%

---

## Question 19: Release Notes


Что из перечисленного должно быть в Release Notes?

A) Только список багфиксов

B) Имена всех разработчиков компании

C) Новые функции, багфиксы, breaking changes, migration guide

D) Полный исходный код

---

## Question 20: Ceremonies


Какая церемония проводится реже всего?

A) Sprint Retrospective

B) Daily Standup

C) Weekly Planning

D) OKR Planning (Quarterly)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DevOps lifecycle: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor |
| 2 | A | PCE = Value-add time / Total lead time × 100%. Показывает долю полезной работы |
| 3 | A | Objective — качественная цель (что), Key Result — измеримый результат (как) |
| 4 | A | Handoffs — передача работы между людьми/командами, создающая задержки |
| 5 | D | Runbook должен содержать всё необходимое для выполнения задачи любым членом команды |
| 6 | A | ADR документирует решение, контекст, альтернативы и последствия |
| 7 | B | Standard change — типовое, заранее одобренное изменение с низким риском |
| 8 | B | Minor version (x.Y.z) увеличивается при добавлении функций без breaking changes |
| 9 | B | Primary on-call — первая линия реагирования, triage, эскалация |
| 10 | B | Capacity учитывает реальное доступное время: минус PTO, meetings, ops work |
| 11 | A | Start/Stop/Continue — простой формат для выявления улучшений |
| 12 | B | 5 Whys — техника поиска root cause путём последовательных "почему?" |
| 13 | D | Детальные технические дискуссии выходят за рамки 15-минутного standup |
| 14 | D | VSM визуализирует весь поток для выявления waste и узких мест |
| 15 | A | Incremental — частые маленькие релизы, Big Bang — редкие большие |
| 16 | D | CAB нужен для изменений с высоким риском или широким влиянием |
| 17 | B | Handoff обеспечивает continuity знаний между сменами |
| 18 | A | Efficiency = PT / (PT + WT) = 8 / (8 + 32) = 8/40 = 20% |
| 19 | C | Release notes информируют о всех изменениях и как мигрировать |
| 20 | D | OKR Planning — ежеквартально, остальные — ежедневно/еженедельно |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете процессы DevOps. Переходите к CI/CD. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Value Stream Mapping и change management. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о планировании. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и примеры. |

---

