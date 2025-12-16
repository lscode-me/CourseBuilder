# Site Reliability Engineering - Quiz

Проверьте свои знания по SRE.

---

## Question 1: Определение SRE

Как Ben Treynor определяет SRE?

A) Новая методология разработки

B) Замена DevOps

C) "SRE is what happens when you ask a software engineer to design an operations team"

D) Только мониторинг

---

## Question 2: Error Budget

Что такое Error Budget?

A) Бюджет на исправление ошибок

B) Стоимость разработки

C) Количество разработчиков

D) Допустимое количество downtime/ошибок (1 - SLO)

---

## Question 3: Toil

Что НЕ является характеристикой toil?

A) Strategic (стратегическая)

B) Automatable (автоматизируемая)

C) Repetitive (повторяющаяся)

D) Manual (ручная работа)

---

## Question 4: 50% Rule

Какой процент времени SRE должен тратить на toil (максимум)?

A) 75%

B) 50%

C) 25%

D) 100%

---

## Question 5: Error Budget Exhausted

Что делать, если error budget исчерпан?

A) Остановить feature releases, фокус на reliability

B) Уволить команду

C) Увеличить SLO

D) Продолжать релизить фичи

---

## Question 6: SRE vs DevOps

Как соотносятся SRE и DevOps?

A) SRE — конкретная реализация DevOps принципов

B) DevOps заменил SRE

C) Они не связаны

D) Это конкуренты

---

## Question 7: Nine 9s

Сколько минут downtime в год допускает 99.99% SLO?

A) 5.26 минут

B) 52.6 минут

C) 3.65 дней

D) 8.76 часов

---

## Question 8: Toil Examples

Что из перечисленного является toil?

A) Design review

B) Написание автоматизации

C) Postmortem analysis

D) Ручной перезапуск сервиса при сбое

---

## Question 9: On-Call

Какая лучшая практика для on-call?

A) Один человек всегда on-call

B) Только actionable алерты с runbooks

C) Без эскалации

D) Алерты на всё подряд

---

## Question 10: PRR

Что такое Production Readiness Review?

A) Security audit

B) Code review

C) Чеклист готовности сервиса к production

D) Performance тест

---

## Question 11: Reliability

Что является главной задачей SRE?

A) Разработка новых функций

B) Написание документации

C) Обеспечение надёжности систем

D) Проведение интервью

---

## Question 12: Automation

Какой принцип SRE по автоматизации?

A) Ручная работа предпочтительнее

B) Автоматизация не нужна

C) Только для тестирования

D) Автоматизировать всё возможное для устранения toil

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

A) Только для джуниоров

B) Высокий — это основа работы SRE

C) Низкий

D) Никогда

---

## Question 15: Blameless Culture

Почему blameless culture важна для SRE?

A) Для увольнения сотрудников

B) Не важна

C) Чтобы скрывать ошибки

D) Для открытого обсуждения проблем и улучшений

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

A) Постепенные изменения с возможностью отката

B) Ручной деплой

C) Без контроля

D) Большие редкие релизы

---

## Question 18: Observability in SRE

Какую роль играет observability в SRE?

A) Критическую — основа для принятия решений

B) Минимальную

C) Только для логов

D) Декоративную

---

## Question 19: Runbooks

Что такое runbook в контексте SRE?

A) Список задач на день

B) Документированная процедура реагирования на инцидент

C) Код приложения

D) Книга для бега

---

## Question 20: Service Ownership

Что означает service ownership в SRE?

A) Ответственность команды за надёжность сервиса

B) Покупка серверов

C) Владение акциями компании

D) Найм сотрудников

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Классическое определение SRE от создателя |
| 2 | D | Error Budget = 1 - SLO |
| 3 | A | Toil tactical, не strategic |
| 4 | B | Максимум 50% на toil, остальное на engineering |
| 5 | A | При исчерпании budget — фокус на reliability |
| 6 | A | "class SRE implements DevOps" |
| 7 | B | 99.99% = 52.6 минут/год |
| 8 | D | Ручной перезапуск — классический toil |
| 9 | B | Только actionable алерты с документацией |
| 10 | C | PRR — чеклист готовности к production |
| 11 | C | Главная задача SRE — обеспечение надёжности систем |
| 12 | D | SRE автоматизирует всё возможное для устранения toil |
| 13 | A | Risk budget связан с error budget — допустимый уровень риска |
| 14 | B | Уменьшение toil — приоритетная задача SRE |
| 15 | D | Blameless culture позволяет открыто обсуждать проблемы |
| 16 | B | Capacity planning — прогнозирование и планирование ресурсов |
| 17 | A | Постепенные изменения с возможностью отката |
| 18 | A | Observability критична — основа для принятия решений |
| 19 | B | Runbook — документированная процедура реагирования |
| 20 | A | Service ownership — ответственность команды за надёжность |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к SLI/SLO/SLA. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте toil и PRR. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы SRE. |

---

