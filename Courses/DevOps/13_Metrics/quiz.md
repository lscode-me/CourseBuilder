# Метрики DevOps - Quiz

Проверьте свои знания по DORA metrics.

---

## Question 1: DORA





Что такое DORA?

A) Инструмент мониторинга

B) CI/CD платформа

C) Исследовательская группа, изучающая DevOps практики

D) Методология разработки

---

## Question 2: Four Keys





Какие четыре ключевые метрики DORA?

A) CPU, Memory, Disk, Network

B) Availability, Latency, Throughput, Errors

C) Deployment Frequency, Lead Time, Change Failure Rate, MTTR

D) Code Coverage, Bugs, Technical Debt, Velocity

---

## Question 3: Elite Performers





Как часто Elite performers деплоят?

A) Раз в месяц

B) Раз в неделю

C) Раз в квартал

D) On-demand (несколько раз в день)

---

## Question 4: Lead Time





Что измеряет Lead Time for Changes?

A) Время code review

B) Время от commit до production

C) Время написания кода

D) Время тестирования

---

## Question 5: Change Failure Rate





Что показывает Change Failure Rate?

A) Количество багов

B) Процент деплоев, вызывающих сбои

C) Скорость разработки

D) Количество строк кода

---

## Question 6: MTTR Elite





Какой MTTR у Elite performers?

A) < 1 week

B) < 1 hour

C) < 1 month

D) < 1 day

---

## Question 7: Throughput vs Stability





Как связаны скорость (throughput) и стабильность?

A) Выше скорость = ниже стабильность

B) Стабильность важнее скорости всегда

C) Elite performers имеют высокую скорость И высокую стабильность

D) Не связаны

---

## Question 8: Data Sources





Откуда брать данные для Deployment Frequency?

A) Опросы разработчиков

B) Финансовые отчёты

C) Ручной подсчёт

D) CI/CD pipeline, Git tags, Kubernetes events

---

## Question 9: Improvement





Как улучшить высокий Lead Time?

A) Увеличить количество тестов

B) Реже деплоить

C) Нанять больше разработчиков

D) Оптимизировать CI, уменьшить batch size, trunk-based development

---

## Question 10: Measurement





Как часто нужно измерять DORA метрики?

A) Только при проблемах

B) Раз в квартал вручную

C) Непрерывно (автоматически)

D) Раз в год

---

## Question 11: Mean Time Between Failures




Что измеряет MTBF?

A) Среднее время восстановления

B) Размер изменений

C) Среднее время между сбоями

D) Частоту деплоя

---

## Question 12: Deployment Size




Как размер deployment влияет на DORA metrics?

A) Размер не измеряется

B) Не влияет

C) Меньшие deployments → лучшие metrics (быстрее, меньше failures)

D) Большие deployments лучше

---

## Question 13: Team Size




Как размер команды влияет на DORA metrics?

A) Большие команды всегда лучше

B) Только leadership важен

C) Не влияет

D) Меньшие команды часто показывают лучшие результаты

---

## Question 14: Culture




Как культура влияет на DORA metrics?

A) Только процессы важны

B) Только технологии важны

C) Не влияет

D) Generative culture (high trust) коррелирует с лучшими metrics

---

## Question 15: Capability




Какие capabilities улучшают DORA metrics?

A) CI/CD, trunk-based dev, monitoring, loose coupling

B) Только документация

C) Только автоматизация

D) Только код-ревью

---

## Question 16: Benchmarking




Как правильно использовать DORA benchmarks?

A) Копировать metrics других компаний

B) Сравнивать только с другими компаниями

C) Игнорировать benchmarks

D) Сравнивать свой прогресс во времени, использовать benchmarks как ориентир

---

## Question 17: Automation Impact




Как automation влияет на DORA metrics?

A) Снижает все metrics

B) Улучшает deployment frequency и lead time

C) Не влияет

D) Только ухудшает change failure rate

---

## Question 18: Testing Impact




Как тестирование влияет на change failure rate?

A) Тесты замедляют deployment

B) Quality тесты снижают change failure rate

C) Тесты не влияют

D) Больше тестов = выше failure rate

---

## Question 19: Psychological Safety




Как psychological safety влияет на DORA metrics?

A) Только HR метрика

B) Снижает productivity

C) High psychological safety → лучшее reporting → улучшение metrics

D) Не связано

---

## Question 20: Continuous Improvement




Как использовать DORA metrics для improvement?

A) Сравнивать людей

B) Наказывать за плохие metrics

C) Identify bottlenecks, experiment, measure, iterate

D) Просто измерять

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | DORA — DevOps Research and Assessment |
| 2 | C | DF, Lead Time, CFR, MTTR — четыре ключевые метрики |
| 3 | D | Elite performers деплоят on-demand |
| 4 | B | Lead Time = время от commit до production |
| 5 | B | CFR = % деплоев, вызывающих сбои |
| 6 | B | Elite MTTR < 1 hour |
| 7 | C | Elite: высокая скорость И высокая стабильность |
| 8 | D | CI/CD, Git, K8s — автоматические источники |
| 9 | D | Оптимизация CI, меньше batch, trunk-based |
| 10 | C | Непрерывное автоматическое измерение |
| 11 | C | MTBF — Mean Time Between Failures |
| 12 | C | Меньшие deployments дают лучшие DORA metrics |
| 13 | D | Меньшие команды часто показывают лучшие результаты |
| 14 | D | Generative culture коррелирует с лучшими metrics |
| 15 | A | CI/CD, trunk-based dev, monitoring, loose coupling |
| 16 | D | Сравнивать свой прогресс, использовать benchmarks как ориентир |
| 17 | B | Автоматизация улучшает deployment frequency и lead time |
| 18 | B | Quality тесты снижают change failure rate |
| 19 | C | High psychological safety улучшает reporting и metrics |
| 20 | C | Identify bottlenecks, experiment, measure, iterate |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DevSecOps. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите improvement actions. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте классификацию уровней. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите четыре метрики. |

---

