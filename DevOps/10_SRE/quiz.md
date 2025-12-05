# Site Reliability Engineering - Quiz

Проверьте свои знания по SRE.

---

## Question 1: Определение SRE

Как Ben Treynor определяет SRE?

A) Новая методология разработки

B) "SRE is what happens when you ask a software engineer to design an operations team"

C) Замена DevOps

D) Только мониторинг

---

## Question 2: Error Budget

Что такое Error Budget?

A) Бюджет на исправление ошибок

B) Допустимое количество downtime/ошибок (1 - SLO)

C) Стоимость разработки

D) Количество разработчиков

---

## Question 3: Toil

Что НЕ является характеристикой toil?

A) Manual (ручная работа)

B) Repetitive (повторяющаяся)

C) Strategic (стратегическая)

D) Automatable (автоматизируемая)

---

## Question 4: 50% Rule

Какой процент времени SRE должен тратить на toil (максимум)?

A) 100%

B) 75%

C) 50%

D) 25%

---

## Question 5: Error Budget Exhausted

Что делать, если error budget исчерпан?

A) Продолжать релизить фичи

B) Остановить feature releases, фокус на reliability

C) Увеличить SLO

D) Уволить команду

---

## Question 6: SRE vs DevOps

Как соотносятся SRE и DevOps?

A) Это конкуренты

B) SRE — конкретная реализация DevOps принципов

C) DevOps заменил SRE

D) Они не связаны

---

## Question 7: Nine 9s

Сколько минут downtime в год допускает 99.99% SLO?

A) 8.76 часов

B) 52.6 минут

C) 5.26 минут

D) 3.65 дней

---

## Question 8: Toil Examples

Что из перечисленного является toil?

A) Написание автоматизации

B) Ручной перезапуск сервиса при сбое

C) Design review

D) Postmortem analysis

---

## Question 9: On-Call

Какая лучшая практика для on-call?

A) Один человек всегда on-call

B) Только actionable алерты с runbooks

C) Алерты на всё подряд

D) Без эскалации

---

## Question 10: PRR

Что такое Production Readiness Review?

A) Code review

B) Чеклист готовности сервиса к production

C) Performance тест

D) Security audit

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Классическое определение SRE от создателя |
| 2 | B | Error Budget = 1 - SLO |
| 3 | C | Toil tactical, не strategic |
| 4 | C | Максимум 50% на toil, остальное на engineering |
| 5 | B | При исчерпании budget — фокус на reliability |
| 6 | B | "class SRE implements DevOps" |
| 7 | B | 99.99% = 52.6 минут/год |
| 8 | B | Ручной перезапуск — классический toil |
| 9 | B | Только actionable алерты с документацией |
| 10 | B | PRR — чеклист готовности к production |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к SLI/SLO/SLA. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите error budget. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте toil и PRR. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы SRE. |

---

