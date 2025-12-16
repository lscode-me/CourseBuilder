# Incident Management - Quiz

Проверьте свои знания по управлению инцидентами.

---

## Question 1: Blameless Culture

Что означает blameless postmortem?

A) Не записывать имена участников

B) Никто не несёт ответственности

C) Фокус на системных проблемах, не на обвинении людей

D) Не проводить postmortem вообще

---

## Question 2: Incident Commander

Какова главная роль Incident Commander?

A) Коммуникация с клиентами

B) Писать код fix

C) Координация response и принятие решений

D) Документирование timeline

---

## Question 3: SEV1

Что характеризует SEV1 инцидент?

A) Cosmetic issues

B) Минимальное влияние

C) Сервис недоступен, все пользователи затронуты

D) Non-critical feature broken

---

## Question 4: MTTR

Что измеряет MTTR?

A) Время до acknowledge

B) Время от обнаружения до resolution

C) Время до обнаружения

D) Количество инцидентов

---

## Question 5: 5 Whys

Для чего используется техника 5 Whys?

A) Для подсчёта инцидентов

B) Для обвинения виновных

C) Для поиска root cause проблемы

D) Для планирования capacity

---

## Question 6: On-Call Handoff

Что должен содержать on-call handoff?

A) Зарплаты команды

B) Код последнего релиза

C) Active issues, recent incidents, scheduled maintenance

D) Только имена on-call

---

## Question 7: Action Items

Какие action items хорошие?

A) Конкретные, с owner, priority и deadline

B) Без deadline

C) Без owner

D) "Улучшить систему"

---

## Question 8: Postmortem Timing

Когда проводить postmortem?

A) Только для SEV4

B) Никогда

C) Через месяц после инцидента

D) В течение нескольких дней после resolution

---

## Question 9: Mitigation vs Resolution

Чем mitigation отличается от resolution?

A) Resolution проще

B) Mitigation дольше

C) Это одно и то же

D) Mitigation — временное уменьшение impact, resolution — устранение причины

---

## Question 10: Good On-Call Alert

Что характеризует хороший on-call алерт?

A) Срабатывает на всё

B) Без документации

C) Actionable, с runbook, low noise

D) Максимальная чувствительность

---

## Question 11: Detection

Как улучшить incident detection?

A) Меньше мониторинга

B) Только ручные проверки

C) Ожидать жалоб пользователей

D) Качественные алерты на SLO breach, anomaly detection

---

## Question 12: Communication

Какой канал лучше для incident communication?

A) Dedicated war room (chat channel) с timeline

B) Личные сообщения

C) Бумажные записки

D) Email

---

## Question 13: Escalation

Когда происходит escalation?

A) Всегда

B) Когда incident не resolve в рамках компетенции или времени

C) Никогда

D) Только для SEV1

---

## Question 14: Timeline

Зачем вести timeline инцидента?

A) Для красоты

B) Для отчётности HR

C) Не нужен

D) Для postmortem analysis и будущих улучшений

---

## Question 15: Testing Runbooks

Почему важно тестировать runbooks?

A) Чтобы убедиться что они работают во время реального инцидента

B) Не важно

C) Только для документации

D) Для развлечения

---

## Question 16: War Room Etiquette

Какие правила в incident war room?

A) Только релевантная информация, координация через IC

B) Без правил

C) Говорить обо всём

D) Обсуждать другие проекты

---

## Question 17: Page Storm

Что такое page storm?

A) Тип сервера

B) Вид деплоя

C) Погодное явление

D) Множество связанных алертов от одной проблемы

---

## Question 18: RCA

Что такое RCA?

A) Rapid Code Adjustment

B) Regular Cleanup Activity

C) Root Cause Analysis — анализ первопричины

D) Remote Computer Access

---

## Question 19: Customer Communication

Когда сообщать клиентам об инциденте?

A) Только по запросу

B) После полного resolution

C) Никогда

D) При значительном impact, согласно communication plan

---

## Question 20: Learning from Incidents

Как команда учится на инцидентах?

A) Увольнения

B) Blameless postmortems, action items, sharing learnings

C) Штрафы

D) Не учится

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Blameless = фокус на системах, не людях |
| 2 | C | IC координирует response |
| 3 | C | SEV1 = critical, сервис недоступен |
| 4 | B | MTTR = Mean Time to Resolve |
| 5 | C | 5 Whys для поиска root cause |
| 6 | C | Handoff содержит context для incoming |
| 7 | A | Action items конкретные, с owner и deadline |
| 8 | D | Postmortem в течение нескольких дней |
| 9 | D | Mitigation временно, resolution устраняет причину |
| 10 | C | Хороший алерт actionable с документацией |
| 11 | D | Качественные алерты на SLO breach, anomaly detection |
| 12 | A | War room (chat channel) с timeline для coordination |
| 13 | B | Escalation когда не resolve в рамках компетенции/времени |
| 14 | D | Timeline нужен для postmortem и улучшений |
| 15 | A | Тестирование runbooks гарантирует их работоспособность |
| 16 | A | War room: только релевантная информация, координация через IC |
| 17 | D | Page storm — множество алертов от одной проблемы |
| 18 | C | RCA — Root Cause Analysis |
| 19 | D | Сообщать клиентам при значительном impact |
| 20 | B | Blameless postmortems, action items, sharing learnings |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DORA Metrics. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите postmortem process. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте incident roles. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите incident lifecycle. |

---

