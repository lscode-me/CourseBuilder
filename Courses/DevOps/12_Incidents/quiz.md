# Incident Management - Quiz

Проверьте свои знания по управлению инцидентами.

---

## Question 1: Blameless Culture





Что означает blameless postmortem?

A) Никто не несёт ответственности

B) Не проводить postmortem вообще

C) Не записывать имена участников

D) Фокус на системных проблемах, не на обвинении людей

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

A) Non-critical feature broken

B) Сервис недоступен, все пользователи затронуты

C) Минимальное влияние

D) Cosmetic issues

---

## Question 4: MTTR





Что измеряет MTTR?

A) Время от обнаружения до resolution

B) Время до обнаружения

C) Количество инцидентов

D) Время до acknowledge

---

## Question 5: 5 Whys





Для чего используется техника 5 Whys?

A) Для поиска root cause проблемы

B) Для планирования capacity

C) Для обвинения виновных

D) Для подсчёта инцидентов

---

## Question 6: On-Call Handoff





Что должен содержать on-call handoff?

A) Только имена on-call

B) Active issues, recent incidents, scheduled maintenance

C) Зарплаты команды

D) Код последнего релиза

---

## Question 7: Action Items





Какие action items хорошие?

A) "Улучшить систему"

B) Без deadline

C) Без owner

D) Конкретные, с owner, priority и deadline

---

## Question 8: Postmortem Timing





Когда проводить postmortem?

A) Никогда

B) Только для SEV4

C) Через месяц после инцидента

D) В течение нескольких дней после resolution

---

## Question 9: Mitigation vs Resolution





Чем mitigation отличается от resolution?

A) Mitigation — временное уменьшение impact, resolution — устранение причины

B) Mitigation дольше

C) Resolution проще

D) Это одно и то же

---

## Question 10: Good On-Call Alert





Что характеризует хороший on-call алерт?

A) Actionable, с runbook, low noise

B) Срабатывает на всё

C) Без документации

D) Максимальная чувствительность

---

## Question 11: Detection




Как улучшить incident detection?

A) Меньше мониторинга

B) Только ручные проверки

C) Качественные алерты на SLO breach, anomaly detection

D) Ожидать жалоб пользователей

---

## Question 12: Communication




Какой канал лучше для incident communication?

A) Email

B) Dedicated war room (chat channel) с timeline

C) Личные сообщения

D) Бумажные записки

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

B) Для postmortem analysis и будущих улучшений

C) Для отчётности HR

D) Не нужен

---

## Question 15: Testing Runbooks




Почему важно тестировать runbooks?

A) Только для документации

B) Для развлечения

C) Чтобы убедиться что они работают во время реального инцидента

D) Не важно

---

## Question 16: War Room Etiquette




Какие правила в incident war room?

A) Говорить обо всём

B) Только релевантная информация, координация через IC

C) Без правил

D) Обсуждать другие проекты

---

## Question 17: Page Storm




Что такое page storm?

A) Погодное явление

B) Множество связанных алертов от одной проблемы

C) Вид деплоя

D) Тип сервера

---

## Question 18: RCA




Что такое RCA?

A) Remote Computer Access

B) Root Cause Analysis — анализ первопричины

C) Rapid Code Adjustment

D) Regular Cleanup Activity

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

B) Штрафы

C) Не учится

D) Blameless postmortems, action items, sharing learnings

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Blameless = фокус на системах, не людях |
| 2 | B | IC координирует response |
| 3 | B | SEV1 = critical, сервис недоступен |
| 4 | A | MTTR = Mean Time to Resolve |
| 5 | A | 5 Whys для поиска root cause |
| 6 | B | Handoff содержит context для incoming |
| 7 | D | Action items конкретные, с owner и deadline |
| 8 | D | Postmortem в течение нескольких дней |
| 9 | A | Mitigation временно, resolution устраняет причину |
| 10 | A | Хороший алерт actionable с документацией |
| 11 | C | Качественные алерты на SLO breach, anomaly detection |
| 12 | B | War room (chat channel) с timeline для coordination |
| 13 | B | Escalation когда не resolve в рамках компетенции/времени |
| 14 | B | Timeline нужен для postmortem и улучшений |
| 15 | C | Тестирование runbooks гарантирует их работоспособность |
| 16 | B | War room: только релевантная информация, координация через IC |
| 17 | B | Page storm — множество алертов от одной проблемы |
| 18 | B | RCA — Root Cause Analysis |
| 19 | D | Сообщать клиентам при значительном impact |
| 20 | D | Blameless postmortems, action items, sharing learnings |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DORA Metrics. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите postmortem process. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте incident roles. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите incident lifecycle. |

---

