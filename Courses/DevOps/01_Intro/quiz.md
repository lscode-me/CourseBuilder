# Введение в DevOps - Quiz

Проверьте свои знания по основам DevOps, его истории и ключевым концепциям.

---

## Question 1: Определение DevOps





Что из перечисленного лучше всего описывает DevOps?

A) Культура, практики и философия, направленные на сотрудничество Dev и Ops

B) Методология разработки программного обеспечения, заменяющая Agile

C) Набор инструментов для автоматизации инфраструктуры

D) Должность инженера, который управляет CI/CD pipeline

---

## Question 2: История DevOps





В каком году состоялась первая конференция DevOpsDays, на которой появился термин "DevOps"?

A) 2013

B) 2007

C) 2009

D) 2011

---

## Question 3: The Three Ways





Какой принцип НЕ относится к "The Three Ways" из философии DevOps?

A) Feedback (Amplify Feedback Loops)

B) Zero Downtime Deployment

C) Continuous Learning

D) Flow (Systems Thinking)

---

## Question 4: First Way - Flow





Что из перечисленного является практикой First Way (Flow)?

A) A/B тестирование

B) Уменьшение размера batch и ограничение WIP

C) Выделение 20% времени на эксперименты

D) Проведение blameless postmortems

---

## Question 5: CALMS Framework





Что означает буква "L" в акрониме CALMS?

A) Lean

B) Learning

C) Logging

D) Leadership

---

## Question 6: CALMS - Measurement





Какая метрика НЕ является частью DORA Four Keys?

A) Deployment frequency

B) Lines of code per sprint

C) Lead time for changes

D) Mean time to recovery

---

## Question 7: DevOps vs SRE





Как Google описывает взаимосвязь между DevOps и SRE?

A) "class SRE implements DevOps"

B) SRE — это устаревшая версия DevOps

C) DevOps и SRE — это конкурирующие подходы

D) DevOps — это часть SRE

---

## Question 8: Anti-patterns





Почему создание отдельной роли "DevOps Engineer" между Dev и Ops считается анти-паттерном?

A) Это создаёт новый silo вместо устранения существующих

B) DevOps Engineers слишком дорогие

C) DevOps Engineer не может знать и Dev, и Ops

D) Это замедляет deployment frequency

---

## Question 9: DORA Metrics





Согласно исследованию DORA, каким deployment frequency отличаются Elite performers?

A) Раз в неделю

B) On-demand (по требованию)

C) Раз в день

D) Раз в месяц

---

## Question 10: Традиционная проблема





Какой основной конфликт существовал между Dev и Ops командами до DevOps?

A) Dev хотели больше зарплату, Ops — меньше работать

B) Dev использовали Windows, Ops — Linux

C) Dev хотели быстрых релизов, Ops хотели стабильности

D) Dev писали код на Java, Ops предпочитали Python

---

## Question 11: Second Way - Feedback





Какая практика относится к Second Way (Feedback)?

A) Мониторинг и алертинг

B) Визуализация работы на Kanban board

C) Infrastructure as Code

D) Feature flags

---

## Question 12: Типы waste в Lean





Что из перечисленного является примером "waste" (потерь) в контексте Lean DevOps?

A) Автоматические тесты

B) Code review

C) Документация

D) Ожидание approval

---

## Question 13: Культура DevOps





Что означает принцип "You build it, you run it"?

A) Разработчик должен сам собирать свой компьютер

B) Нельзя использовать CI/CD — всё вручную

C) Команда несёт полную ответственность за свой сервис в production

D) Build и run должны выполняться в одной команде терминала

---

## Question 14: Модели внедрения





Что характеризует модель "Platform Team"?

A) Ops полностью заменяется на cloud services

B) Внешняя компания управляет инфраструктурой

C) Каждая команда сама создаёт свою инфраструктуру

D) Централизованная команда создаёт инструменты для product команд

---

## Question 15: Third Way





Какая практика относится к Third Way (Continuous Learning)?

A) Blameless postmortems

B) Централизованное логирование

C) Автоматизация deployment

D) Ограничение Work in Progress

---

## Question 16: CALMS - Automation





Что из перечисленного НЕ является типичной областью автоматизации в DevOps?

A) Testing

B) Infrastructure provisioning

C) Build и packaging

D) Принятие бизнес-решений о приоритетах

---

## Question 17: История DevOps





Какая компания представила доклад "10+ Deploys Per Day" на Velocity Conference 2009?

A) Flickr

B) Netflix

C) Amazon

D) Google

---

## Question 18: Зрелость DevOps





Какой уровень зрелости DevOps характеризуется Chaos engineering и AIOps?

A) Level 3: Advanced

B) Level 1: Beginning

C) Level 4: Elite

D) Level 2: Intermediate

---

## Question 19: SRE





Какой основной фокус Site Reliability Engineering по сравнению с DevOps?

A) Скорость разработки

B) Надёжность и reliability engineering

C) Снижение затрат на инфраструктуру

D) Улучшение UX

---

## Question 20: Бизнес-ценность





Согласно исследованию DORA, во сколько раз Elite performers деплоят чаще, чем Low performers?

A) В 50 раз

B) В 1000 раз

C) В 10 раз

D) В 208 раз

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | DevOps — это прежде всего культура и практики сотрудничества, а не инструменты или должность |
| 2 | C | Первая DevOpsDays состоялась в Генте (Бельгия) в 2009 году, организованная Patrick Debois |
| 3 | B | Three Ways: Flow, Feedback, Continuous Learning. Zero Downtime — это практика, но не один из "путей" |
| 4 | B | Уменьшение batch size и ограничение WIP — практики First Way для оптимизации потока |
| 5 | A | CALMS: Culture, Automation, Lean, Measurement, Sharing |
| 6 | B | DORA Four Keys: Deployment frequency, Lead time, Change failure rate, MTTR. Lines of code — vanity metric |
| 7 | A | Google описывает SRE как конкретную реализацию DevOps с фокусом на reliability |
| 8 | A | Создание отдельной роли создаёт новую "стену" между командами вместо устранения существующей |
| 9 | B | Elite performers деплоят по требованию — несколько раз в день или чаще |
| 10 | C | Основной конфликт: Dev хотели частых изменений (скорость), Ops хотели минимума изменений (стабильность) |
| 11 | A | Мониторинг и алертинг — это практики обратной связи (Second Way) |
| 12 | D | Ожидание (delays) — один из 7 типов waste. Тесты, review и документация добавляют ценность |
| 13 | C | Принцип означает полную ответственность команды за сервис от разработки до эксплуатации |
| 14 | D | Platform Team создаёт общие инструменты и платформу, которые используют product команды |
| 15 | A | Blameless postmortems — практика Third Way, создающая культуру обучения на ошибках |
| 16 | D | Автоматизируются технические задачи, но бизнес-решения остаются за людьми |
| 17 | A | John Allspaw и Paul Hammond из Flickr представили этот знаменитый доклад |
| 18 | C | Elite level характеризуется продвинутыми практиками вроде Chaos Engineering и AIOps |
| 19 | B | SRE фокусируется на reliability и применяет software engineering к операциям |
| 20 | D | По данным DORA, Elite performers деплоят в 208 раз чаще, чем Low performers |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили основы DevOps. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы CALMS и Three Ways. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о культуре и истории DevOps. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, обратите внимание на примеры. |

---

