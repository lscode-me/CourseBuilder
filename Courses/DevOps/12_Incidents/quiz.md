# Incident Management - Quiz

Проверьте свои знания по управлению инцидентами.

---

## Question 1: Blameless Culture







Что означает blameless postmortem?

A) Фокус на системных проблемах, не на обвинении людей

B) Не проводить postmortem вообще

C) Никто не несёт ответственности

D) Не записывать имена участников

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

A) Cosmetic issues

B) Сервис недоступен, все пользователи затронуты

C) Non-critical feature broken

D) Минимальное влияние

---

## Question 4: MTTR







Что измеряет MTTR?

A) Время до acknowledge

B) Время до обнаружения

C) Время от обнаружения до resolution

D) Количество инцидентов

---

## Question 5: 5 Whys







Для чего используется техника 5 Whys?

A) Для планирования capacity

B) Для обвинения виновных

C) Для поиска root cause проблемы

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

A) Конкретные, с owner, priority и deadline

B) Без owner

C) Без deadline

D) "Улучшить систему"

---

## Question 8: Postmortem Timing







Когда проводить postmortem?

A) Никогда

B) В течение нескольких дней после resolution

C) Только для SEV4

D) Через месяц после инцидента

---

## Question 9: Mitigation vs Resolution







Чем mitigation отличается от resolution?

A) Resolution проще

B) Mitigation — временное уменьшение impact, resolution — устранение причины

C) Mitigation дольше

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

A) Бумажные записки

B) Dedicated war room (chat channel) с timeline

C) Email

D) Личные сообщения

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

A) Для postmortem analysis и будущих улучшений

B) Не нужен

C) Для отчётности HR

D) Для красоты

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

A) Root Cause Analysis — анализ первопричины

B) Rapid Code Adjustment

C) Remote Computer Access

D) Regular Cleanup Activity

---

## Question 19: Customer Communication






Когда сообщать клиентам об инциденте?

A) После полного resolution

B) Только по запросу

C) При значительном impact, согласно communication plan

D) Никогда

---

## Question 20: Learning from Incidents






Как команда учится на инцидентах?

A) Штрафы

B) Увольнения

C) Blameless postmortems, action items, sharing learnings

D) Не учится

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Blameless = фокус на системах, не людях |
| 2 | B | IC координирует response |
| 3 | B | SEV1 = critical, сервис недоступен |
| 4 | C | MTTR = Mean Time to Resolve |
| 5 | C | 5 Whys для поиска root cause |
| 6 | B | Handoff содержит context для incoming |
| 7 | A | Action items конкретные, с owner и deadline |
| 8 | B | Postmortem в течение нескольких дней |
| 9 | B | Mitigation временно, resolution устраняет причину |
| 10 | A | Хороший алерт actionable с документацией |
| 11 | C | Качественные алерты на SLO breach, anomaly detection |
| 12 | B | War room (chat channel) с timeline для coordination |
| 13 | B | Escalation когда не resolve в рамках компетенции/времени |
| 14 | A | Timeline нужен для postmortem и улучшений |
| 15 | C | Тестирование runbooks гарантирует их работоспособность |
| 16 | B | War room: только релевантная информация, координация через IC |
| 17 | B | Page storm — множество алертов от одной проблемы |
| 18 | A | RCA — Root Cause Analysis |
| 19 | C | Сообщать клиентам при значительном impact |
| 20 | C | Blameless postmortems, action items, sharing learnings |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DORA Metrics. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите postmortem process. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте incident roles. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите incident lifecycle. |

---

