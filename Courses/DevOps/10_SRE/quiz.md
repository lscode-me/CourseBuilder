# Site Reliability Engineering - Quiz

Проверьте свои знания по SRE.

---

## Question 1: Определение SRE







Как Ben Treynor определяет SRE?

A) Только мониторинг

B) "SRE is what happens when you ask a software engineer to design an operations team"

C) Замена DevOps

D) Новая методология разработки

---

## Question 2: Error Budget







Что такое Error Budget?

A) Количество разработчиков

B) Бюджет на исправление ошибок

C) Допустимое количество downtime/ошибок (1 - SLO)

D) Стоимость разработки

---

## Question 3: Toil







Что НЕ является характеристикой toil?

A) Automatable (автоматизируемая)

B) Strategic (стратегическая)

C) Repetitive (повторяющаяся)

D) Manual (ручная работа)

---

## Question 4: 50% Rule







Какой процент времени SRE должен тратить на toil (максимум)?

A) 100%

B) 50%

C) 75%

D) 25%

---

## Question 5: Error Budget Exhausted







Что делать, если error budget исчерпан?

A) Увеличить SLO

B) Продолжать релизить фичи

C) Остановить feature releases, фокус на reliability

D) Уволить команду

---

## Question 6: SRE vs DevOps







Как соотносятся SRE и DevOps?

A) DevOps заменил SRE

B) Они не связаны

C) Это конкуренты

D) SRE — конкретная реализация DevOps принципов

---

## Question 7: Nine 9s







Сколько минут downtime в год допускает 99.99% SLO?

A) 8.76 часов

B) 3.65 дней

C) 52.6 минут

D) 5.26 минут

---

## Question 8: Toil Examples







Что из перечисленного является toil?

A) Postmortem analysis

B) Ручной перезапуск сервиса при сбое

C) Design review

D) Написание автоматизации

---

## Question 9: On-Call







Какая лучшая практика для on-call?

A) Один человек всегда on-call

B) Алерты на всё подряд

C) Без эскалации

D) Только actionable алерты с runbooks

---

## Question 10: PRR







Что такое Production Readiness Review?

A) Performance тест

B) Чеклист готовности сервиса к production

C) Security audit

D) Code review

---

## Question 11: Reliability






Что является главной задачей SRE?

A) Обеспечение надёжности систем

B) Написание документации

C) Разработка новых функций

D) Проведение интервью

---

## Question 12: Automation






Какой принцип SRE по автоматизации?

A) Автоматизировать всё возможное для устранения toil

B) Только для тестирования

C) Автоматизация не нужна

D) Ручная работа предпочтительнее

---

## Question 13: Risk Budget






Что такое risk budget в SRE?

A) Допустимый уровень риска (связан с error budget)

B) Зарплата команды

C) Стоимость серверов

D) Бюджет на рекламу

---

## Question 14: Reducing Toil






Какой приоритет у задач по уменьшению toil?

A) Низкий

B) Высокий — это основа работы SRE

C) Никогда

D) Только для джуниоров

---

## Question 15: Blameless Culture






Почему blameless culture важна для SRE?

A) Для открытого обсуждения проблем и улучшений

B) Чтобы скрывать ошибки

C) Для увольнения сотрудников

D) Не важна

---

## Question 16: Capacity Planning






Что включает capacity planning в SRE?

A) Только тестирование

B) Прогнозирование роста и планирование ресурсов

C) Только deployment

D) Только мониторинг

---

## Question 17: Change Management






Какой подход к change management в SRE?

A) Большие редкие релизы

B) Без контроля

C) Постепенные изменения с возможностью отката

D) Ручной деплой

---

## Question 18: Observability in SRE






Какую роль играет observability в SRE?

A) Критическую — основа для принятия решений

B) Декоративную

C) Минимальную

D) Только для логов

---

## Question 19: Runbooks






Что такое runbook в контексте SRE?

A) Книга для бега

B) Код приложения

C) Документированная процедура реагирования на инцидент

D) Список задач на день

---

## Question 20: Service Ownership






Что означает service ownership в SRE?

A) Владение акциями компании

B) Покупка серверов

C) Найм сотрудников

D) Ответственность команды за надёжность сервиса

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Классическое определение SRE от создателя |
| 2 | C | Error Budget = 1 - SLO |
| 3 | B | Toil tactical, не strategic |
| 4 | B | Максимум 50% на toil, остальное на engineering |
| 5 | C | При исчерпании budget — фокус на reliability |
| 6 | D | "class SRE implements DevOps" |
| 7 | C | 99.99% = 52.6 минут/год |
| 8 | B | Ручной перезапуск — классический toil |
| 9 | D | Только actionable алерты с документацией |
| 10 | B | PRR — чеклист готовности к production |
| 11 | A | Главная задача SRE — обеспечение надёжности систем |
| 12 | A | SRE автоматизирует всё возможное для устранения toil |
| 13 | A | Risk budget связан с error budget — допустимый уровень риска |
| 14 | B | Уменьшение toil — приоритетная задача SRE |
| 15 | A | Blameless culture позволяет открыто обсуждать проблемы |
| 16 | B | Capacity planning — прогнозирование и планирование ресурсов |
| 17 | C | Постепенные изменения с возможностью отката |
| 18 | A | Observability критична — основа для принятия решений |
| 19 | C | Runbook — документированная процедура реагирования |
| 20 | D | Service ownership — ответственность команды за надёжность |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к SLI/SLO/SLA. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте toil и PRR. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы SRE. |

---

