# Incident Management - Quiz

Проверьте свои знания по управлению инцидентами.

---

## Question 1: Blameless Culture

Что означает blameless postmortem?

A) Никто не несёт ответственности

B) Фокус на системных проблемах, не на обвинении людей

C) Не записывать имена участников

D) Не проводить postmortem вообще

---

## Question 2: Incident Commander

Какова главная роль Incident Commander?

A) Писать код fix

B) Координация response и принятие решений

C) Коммуникация с клиентами

D) Документирование timeline

---

## Question 3: SEV1

Что характеризует SEV1 инцидент?

A) Минимальное влияние

B) Сервис недоступен, все пользователи затронуты

C) Cosmetic issues

D) Non-critical feature broken

---

## Question 4: MTTR

Что измеряет MTTR?

A) Время до обнаружения

B) Время до acknowledge

C) Время от обнаружения до resolution

D) Количество инцидентов

---

## Question 5: 5 Whys

Для чего используется техника 5 Whys?

A) Для обвинения виновных

B) Для поиска root cause проблемы

C) Для подсчёта инцидентов

D) Для планирования capacity

---

## Question 6: On-Call Handoff

Что должен содержать on-call handoff?

A) Только имена on-call

B) Active issues, recent incidents, scheduled maintenance

C) Код последнего релиза

D) Зарплаты команды

---

## Question 7: Action Items

Какие action items хорошие?

A) "Улучшить систему"

B) Конкретные, с owner, priority и deadline

C) Без deadline

D) Без owner

---

## Question 8: Postmortem Timing

Когда проводить postmortem?

A) Через месяц после инцидента

B) В течение нескольких дней после resolution

C) Никогда

D) Только для SEV4

---

## Question 9: Mitigation vs Resolution

Чем mitigation отличается от resolution?

A) Это одно и то же

B) Mitigation — временное уменьшение impact, resolution — устранение причины

C) Mitigation дольше

D) Resolution проще

---

## Question 10: Good On-Call Alert

Что характеризует хороший on-call алерт?

A) Срабатывает на всё

B) Actionable, с runbook, low noise

C) Без документации

D) Максимальная чувствительность

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Blameless = фокус на системах, не людях |
| 2 | B | IC координирует response |
| 3 | B | SEV1 = critical, сервис недоступен |
| 4 | C | MTTR = Mean Time to Resolve |
| 5 | B | 5 Whys для поиска root cause |
| 6 | B | Handoff содержит context для incoming |
| 7 | B | Action items конкретные, с owner и deadline |
| 8 | B | Postmortem в течение нескольких дней |
| 9 | B | Mitigation временно, resolution устраняет причину |
| 10 | B | Хороший алерт actionable с документацией |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DORA Metrics. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите postmortem process. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте incident roles. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите incident lifecycle. |

---

