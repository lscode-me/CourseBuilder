# Введение в DevOps - Quiz

Проверьте свои знания по основам DevOps, его истории и ключевым концепциям.

---

## Question 1: Определение DevOps

Что из перечисленного лучше всего описывает DevOps?

A) Должность инженера, который управляет CI/CD pipeline

B) Культура, практики и философия, направленные на сотрудничество Dev и Ops

C) Методология разработки программного обеспечения, заменяющая Agile

D) Набор инструментов для автоматизации инфраструктуры

---

## Question 2: История DevOps

В каком году состоялась первая конференция DevOpsDays, на которой появился термин "DevOps"?

A) 2007

B) 2013

C) 2011

D) 2009

---

## Question 3: The Three Ways

Какой принцип НЕ относится к "The Three Ways" из философии DevOps?

A) Flow (Systems Thinking)

B) Zero Downtime Deployment

C) Continuous Learning

D) Feedback (Amplify Feedback Loops)

---

## Question 4: First Way - Flow

Что из перечисленного является практикой First Way (Flow)?

A) Уменьшение размера batch и ограничение WIP

B) Проведение blameless postmortems

C) A/B тестирование

D) Выделение 20% времени на эксперименты

---

## Question 5: CALMS Framework

Что означает буква "L" в акрониме CALMS?

A) Lean

B) Logging

C) Learning

D) Leadership

---

## Question 6: CALMS - Measurement

Какая метрика НЕ является частью DORA Four Keys?

A) Lead time for changes

B) Lines of code per sprint

C) Deployment frequency

D) Mean time to recovery

---

## Question 7: DevOps vs SRE

Как Google описывает взаимосвязь между DevOps и SRE?

A) "class SRE implements DevOps"

B) SRE — это устаревшая версия DevOps

C) DevOps — это часть SRE

D) DevOps и SRE — это конкурирующие подходы

---

## Question 8: Anti-patterns

Почему создание отдельной роли "DevOps Engineer" между Dev и Ops считается анти-паттерном?

A) Это замедляет deployment frequency

B) Это создаёт новый silo вместо устранения существующих

C) DevOps Engineer не может знать и Dev, и Ops

D) DevOps Engineers слишком дорогие

---

## Question 9: DORA Metrics

Согласно исследованию DORA, каким deployment frequency отличаются Elite performers?

A) Раз в день

B) On-demand (по требованию)

C) Раз в месяц

D) Раз в неделю

---

## Question 10: Традиционная проблема

Какой основной конфликт существовал между Dev и Ops командами до DevOps?

A) Dev использовали Windows, Ops — Linux

B) Dev хотели быстрых релизов, Ops хотели стабильности

C) Dev хотели больше зарплату, Ops — меньше работать

D) Dev писали код на Java, Ops предпочитали Python

---

## Question 11: Second Way - Feedback

Какая практика относится к Second Way (Feedback)?

A) Infrastructure as Code

B) Мониторинг и алертинг

C) Feature flags

D) Визуализация работы на Kanban board

---

## Question 12: Типы waste в Lean

Что из перечисленного является примером "waste" (потерь) в контексте Lean DevOps?

A) Документация

B) Ожидание approval

C) Code review

D) Автоматические тесты

---

## Question 13: Культура DevOps

Что означает принцип "You build it, you run it"?

A) Нельзя использовать CI/CD — всё вручную

B) Команда несёт полную ответственность за свой сервис в production

C) Build и run должны выполняться в одной команде терминала

D) Разработчик должен сам собирать свой компьютер

---

## Question 14: Модели внедрения

Что характеризует модель "Platform Team"?

A) Каждая команда сама создаёт свою инфраструктуру

B) Централизованная команда создаёт инструменты для product команд

C) Внешняя компания управляет инфраструктурой

D) Ops полностью заменяется на cloud services

---

## Question 15: Third Way

Какая практика относится к Third Way (Continuous Learning)?

A) Blameless postmortems

B) Централизованное логирование

C) Ограничение Work in Progress

D) Автоматизация deployment

---

## Question 16: CALMS - Automation

Что из перечисленного НЕ является типичной областью автоматизации в DevOps?

A) Testing

B) Принятие бизнес-решений о приоритетах

C) Build и packaging

D) Infrastructure provisioning

---

## Question 17: История DevOps

Какая компания представила доклад "10+ Deploys Per Day" на Velocity Conference 2009?

A) Netflix

B) Amazon

C) Flickr

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

A) Снижение затрат на инфраструктуру

B) Скорость разработки

C) Улучшение UX

D) Надёжность и reliability engineering

---

## Question 20: Бизнес-ценность

Согласно исследованию DORA, во сколько раз Elite performers деплоят чаще, чем Low performers?

A) В 208 раз

B) В 1000 раз

C) В 50 раз

D) В 10 раз

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DevOps — это прежде всего культура и практики сотрудничества, а не инструменты или должность |
| 2 | D | Первая DevOpsDays состоялась в Генте (Бельгия) в 2009 году, организованная Patrick Debois |
| 3 | B | Three Ways: Flow, Feedback, Continuous Learning. Zero Downtime — это практика, но не один из "путей" |
| 4 | A | Уменьшение batch size и ограничение WIP — практики First Way для оптимизации потока |
| 5 | A | CALMS: Culture, Automation, Lean, Measurement, Sharing |
| 6 | B | DORA Four Keys: Deployment frequency, Lead time, Change failure rate, MTTR. Lines of code — vanity metric |
| 7 | A | Google описывает SRE как конкретную реализацию DevOps с фокусом на reliability |
| 8 | B | Создание отдельной роли создаёт новую "стену" между командами вместо устранения существующей |
| 9 | B | Elite performers деплоят по требованию — несколько раз в день или чаще |
| 10 | B | Основной конфликт: Dev хотели частых изменений (скорость), Ops хотели минимума изменений (стабильность) |
| 11 | B | Мониторинг и алертинг — это практики обратной связи (Second Way) |
| 12 | B | Ожидание (delays) — один из 7 типов waste. Тесты, review и документация добавляют ценность |
| 13 | B | Принцип означает полную ответственность команды за сервис от разработки до эксплуатации |
| 14 | B | Platform Team создаёт общие инструменты и платформу, которые используют product команды |
| 15 | A | Blameless postmortems — практика Third Way, создающая культуру обучения на ошибках |
| 16 | B | Автоматизируются технические задачи, но бизнес-решения остаются за людьми |
| 17 | C | John Allspaw и Paul Hammond из Flickr представили этот знаменитый доклад |
| 18 | C | Elite level характеризуется продвинутыми практиками вроде Chaos Engineering и AIOps |
| 19 | D | SRE фокусируется на reliability и применяет software engineering к операциям |
| 20 | A | По данным DORA, Elite performers деплоят в 208 раз чаще, чем Low performers |

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

