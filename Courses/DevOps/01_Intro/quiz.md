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

C) Leadership

D) Logging

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

A) SRE — это устаревшая версия DevOps

B) "class SRE implements DevOps"

C) DevOps и SRE — это конкурирующие подходы

D) DevOps — это часть SRE

---

## Question 8: Anti-patterns


Почему создание отдельной роли "DevOps Engineer" между Dev и Ops считается анти-паттерном?

A) Это замедляет deployment frequency

B) Это создаёт новый silo вместо устранения существующих

C) DevOps Engineers слишком дорогие

D) DevOps Engineer не может знать и Dev, и Ops

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

B) Dev хотели быстрых релизов, Ops хотели стабильности

C) Dev использовали Windows, Ops — Linux

D) Dev писали код на Java, Ops предпочитали Python

---

## Question 11: Second Way - Feedback


Какая практика относится к Second Way (Feedback)?

A) Визуализация работы на Kanban board

B) Мониторинг и алертинг

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

A) Ограничение Work in Progress

B) Централизованное логирование

C) Автоматизация deployment

D) Blameless postmortems

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

A) Google

B) Amazon

C) Netflix

D) Flickr

---

## Question 18: Зрелость DevOps


Какой уровень зрелости DevOps характеризуется Chaos engineering и AIOps?

A) Level 3: Advanced

B) Level 2: Intermediate

C) Level 4: Elite

D) Level 1: Beginning

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

A) В 50 раз

B) В 1000 раз

C) В 10 раз

D) В 208 раз

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | DevOps — это прежде всего культура и практики сотрудничества, а не инструменты или должность |
| 2 | C | Первая DevOpsDays состоялась в Генте (Бельгия) в 2009 году, организованная Patrick Debois |
| 3 | B | Three Ways: Flow, Feedback, Continuous Learning. Zero Downtime — это практика, но не один из "путей" |
| 4 | B | Уменьшение batch size и ограничение WIP — практики First Way для оптимизации потока |
| 5 | A | CALMS: Culture, Automation, Lean, Measurement, Sharing |
| 6 | B | DORA Four Keys: Deployment frequency, Lead time, Change failure rate, MTTR. Lines of code — vanity metric |
| 7 | B | Google описывает SRE как конкретную реализацию DevOps с фокусом на reliability |
| 8 | B | Создание отдельной роли создаёт новую "стену" между командами вместо устранения существующей |
| 9 | B | Elite performers деплоят по требованию — несколько раз в день или чаще |
| 10 | B | Основной конфликт: Dev хотели частых изменений (скорость), Ops хотели минимума изменений (стабильность) |
| 11 | B | Мониторинг и алертинг — это практики обратной связи (Second Way) |
| 12 | D | Ожидание (delays) — один из 7 типов waste. Тесты, review и документация добавляют ценность |
| 13 | C | Принцип означает полную ответственность команды за сервис от разработки до эксплуатации |
| 14 | D | Platform Team создаёт общие инструменты и платформу, которые используют product команды |
| 15 | D | Blameless postmortems — практика Third Way, создающая культуру обучения на ошибках |
| 16 | D | Автоматизируются технические задачи, но бизнес-решения остаются за людьми |
| 17 | D | John Allspaw и Paul Hammond из Flickr представили этот знаменитый доклад |
| 18 | C | Elite level характеризуется продвинутыми практиками вроде Chaos Engineering и AIOps |
| 19 | D | SRE фокусируется на reliability и применяет software engineering к операциям |
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

