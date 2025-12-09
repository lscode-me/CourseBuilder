# Процессы DevOps - Quiz

Проверьте свои знания по жизненному циклу DevOps, планированию и регламентам.

---

## Question 1: DevOps Lifecycle







Какая фаза DevOps lifecycle следует сразу после "Build"?

A) Test

B) Release

C) Code

D) Deploy

---

## Question 2: Value Stream







Что измеряет Process Cycle Efficiency?

A) Скорость deployment

B) Количество deployments в день

C) Количество багов на 1000 строк кода

D) Отношение времени работы к общему lead time

---

## Question 3: OKRs







Чем Key Result отличается от Objective в OKR?

A) Objective качественный, Key Result измеримый

B) Key Result качественный, Objective количественный

C) Это одно и то же

D) Objective для команды, Key Result для индивидуумов

---

## Question 4: Waste Types







Что из перечисленного является примером waste типа "handoffs"?

A) Ожидание code review

B) Написание ненужных фич

C) Передача задачи от Dev к QA к Ops

D) Исправление багов в production

---

## Question 5: Runbook







Что должен содержать хороший runbook?

A) Историю всех инцидентов

B) Пошаговые инструкции, prerequisites, rollback план

C) Исходный код сервиса

D) Только команды для выполнения

---

## Question 6: ADR







Что такое Architecture Decision Record (ADR)?

A) Результаты performance тестирования

B) Документ, фиксирующий важное архитектурное решение и его контекст

C) Лог ошибок приложения

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

A) 2.4.2

B) 3.0.0

C) 2.5.0

D) 2.4.1.1

---

## Question 9: On-Call







Какова основная обязанность primary on-call?

A) Планирование спринтов

B) Написание нового кода

C) Проведение code review

D) Первая линия реагирования на алерты

---

## Question 10: Capacity Planning







При расчёте capacity команды из 5 человек на 2-недельный спринт, что следует учесть?

A) Только story points предыдущего спринта

B) Только количество рабочих дней

C) Количество открытых багов

D) Рабочие дни, PTO, время на meetings и ops work

---

## Question 11: Retrospective







Какой формат ретроспективы фокусируется на "Что начать/прекратить/продолжить делать"?

A) SWOT Analysis

B) Start/Stop/Continue

C) Fishbone Diagram

D) 5 Whys

---

## Question 12: 5 Whys







Для чего используется техника "5 Whys"?

A) Для планирования спринта

B) Для поиска root cause проблемы

C) Для оценки задач в story points

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

A) Это одно и то же

B) Incremental только для hotfixes

C) Big Bang — много маленьких релизов, Incremental — один большой

D) Incremental — много маленьких релизов, Big Bang — один большой

---

## Question 16: Change Advisory Board







Когда DevOps команде нужен CAB approval?

A) Никогда — CAB несовместим с DevOps

B) Для каждого деплоя

C) Только для изменений в документации

D) Для high-risk изменений, затрагивающих много команд

---

## Question 17: On-Call Handoff







Что должен содержать документ on-call handoff?

A) Активные issues, недавние инциденты, запланированные работы

B) Зарплаты членов команды

C) Код последнего релиза

D) Только имена on-call инженеров

---

## Question 18: Process Time vs Wait Time







В Value Stream, если Process Time = 8 часов, Wait Time = 32 часа, чему равна Efficiency?

A) 80%

B) 20%

C) 25%

D) 40%

---

## Question 19: Release Notes







Что из перечисленного должно быть в Release Notes?

A) Новые функции, багфиксы, breaking changes, migration guide

B) Только список багфиксов

C) Полный исходный код

D) Имена всех разработчиков компании

---

## Question 20: Ceremonies







Какая церемония проводится реже всего?

A) Weekly Planning

B) Sprint Retrospective

C) OKR Planning (Quarterly)

D) Daily Standup

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | DevOps lifecycle: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor |
| 2 | D | PCE = Value-add time / Total lead time × 100%. Показывает долю полезной работы |
| 3 | A | Objective — качественная цель (что), Key Result — измеримый результат (как) |
| 4 | C | Handoffs — передача работы между людьми/командами, создающая задержки |
| 5 | B | Runbook должен содержать всё необходимое для выполнения задачи любым членом команды |
| 6 | B | ADR документирует решение, контекст, альтернативы и последствия |
| 7 | B | Standard change — типовое, заранее одобренное изменение с низким риском |
| 8 | C | Minor version (x.Y.z) увеличивается при добавлении функций без breaking changes |
| 9 | D | Primary on-call — первая линия реагирования, triage, эскалация |
| 10 | D | Capacity учитывает реальное доступное время: минус PTO, meetings, ops work |
| 11 | B | Start/Stop/Continue — простой формат для выявления улучшений |
| 12 | B | 5 Whys — техника поиска root cause путём последовательных "почему?" |
| 13 | D | Детальные технические дискуссии выходят за рамки 15-минутного standup |
| 14 | D | VSM визуализирует весь поток для выявления waste и узких мест |
| 15 | D | Incremental — частые маленькие релизы, Big Bang — редкие большие |
| 16 | D | CAB нужен для изменений с высоким риском или широким влиянием |
| 17 | A | Handoff обеспечивает continuity знаний между сменами |
| 18 | B | Efficiency = PT / (PT + WT) = 8 / (8 + 32) = 8/40 = 20% |
| 19 | A | Release notes информируют о всех изменениях и как мигрировать |
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

