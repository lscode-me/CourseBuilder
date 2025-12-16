# Метрики DevOps - Quiz

Проверьте свои знания по DORA metrics.

---

## Question 1: DORA

Что такое DORA?

A) Методология разработки

B) Инструмент мониторинга

C) Исследовательская группа, изучающая DevOps практики

D) CI/CD платформа

---

## Question 2: Four Keys

Какие четыре ключевые метрики DORA?

A) Code Coverage, Bugs, Technical Debt, Velocity

B) CPU, Memory, Disk, Network

C) Availability, Latency, Throughput, Errors

D) Deployment Frequency, Lead Time, Change Failure Rate, MTTR

---

## Question 3: Elite Performers

Как часто Elite performers деплоят?

A) On-demand (несколько раз в день)

B) Раз в неделю

C) Раз в месяц

D) Раз в квартал

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

A) Процент деплоев, вызывающих сбои

B) Скорость разработки

C) Количество багов

D) Количество строк кода

---

## Question 6: MTTR Elite

Какой MTTR у Elite performers?

A) < 1 week

B) < 1 day

C) < 1 month

D) < 1 hour

---

## Question 7: Throughput vs Stability

Как связаны скорость (throughput) и стабильность?

A) Выше скорость = ниже стабильность

B) Стабильность важнее скорости всегда

C) Не связаны

D) Elite performers имеют высокую скорость И высокую стабильность

---

## Question 8: Data Sources

Откуда брать данные для Deployment Frequency?

A) Опросы разработчиков

B) Ручной подсчёт

C) Финансовые отчёты

D) CI/CD pipeline, Git tags, Kubernetes events

---

## Question 9: Improvement

Как улучшить высокий Lead Time?

A) Реже деплоить

B) Нанять больше разработчиков

C) Увеличить количество тестов

D) Оптимизировать CI, уменьшить batch size, trunk-based development

---

## Question 10: Measurement

Как часто нужно измерять DORA метрики?

A) Раз в квартал вручную

B) Только при проблемах

C) Непрерывно (автоматически)

D) Раз в год

---

## Question 11: Mean Time Between Failures

Что измеряет MTBF?

A) Размер изменений

B) Частоту деплоя

C) Среднее время между сбоями

D) Среднее время восстановления

---

## Question 12: Deployment Size

Как размер deployment влияет на DORA metrics?

A) Размер не измеряется

B) Не влияет

C) Большие deployments лучше

D) Меньшие deployments → лучшие metrics (быстрее, меньше failures)

---

## Question 13: Team Size

Как размер команды влияет на DORA metrics?

A) Большие команды всегда лучше

B) Не влияет

C) Меньшие команды часто показывают лучшие результаты

D) Только leadership важен

---

## Question 14: Culture

Как культура влияет на DORA metrics?

A) Generative culture (high trust) коррелирует с лучшими metrics

B) Только технологии важны

C) Не влияет

D) Только процессы важны

---

## Question 15: Capability

Какие capabilities улучшают DORA metrics?

A) Только код-ревью

B) Только документация

C) CI/CD, trunk-based dev, monitoring, loose coupling

D) Только автоматизация

---

## Question 16: Benchmarking

Как правильно использовать DORA benchmarks?

A) Сравнивать только с другими компаниями

B) Копировать metrics других компаний

C) Игнорировать benchmarks

D) Сравнивать свой прогресс во времени, использовать benchmarks как ориентир

---

## Question 17: Automation Impact

Как automation влияет на DORA metrics?

A) Улучшает deployment frequency и lead time

B) Только ухудшает change failure rate

C) Не влияет

D) Снижает все metrics

---

## Question 18: Testing Impact

Как тестирование влияет на change failure rate?

A) Тесты не влияют

B) Тесты замедляют deployment

C) Больше тестов = выше failure rate

D) Quality тесты снижают change failure rate

---

## Question 19: Psychological Safety

Как psychological safety влияет на DORA metrics?

A) Снижает productivity

B) Не связано

C) Только HR метрика

D) High psychological safety → лучшее reporting → улучшение metrics

---

## Question 20: Continuous Improvement

Как использовать DORA metrics для improvement?

A) Просто измерять

B) Наказывать за плохие metrics

C) Сравнивать людей

D) Identify bottlenecks, experiment, measure, iterate

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | DORA — DevOps Research and Assessment |
| 2 | D | DF, Lead Time, CFR, MTTR — четыре ключевые метрики |
| 3 | A | Elite performers деплоят on-demand |
| 4 | B | Lead Time = время от commit до production |
| 5 | A | CFR = % деплоев, вызывающих сбои |
| 6 | D | Elite MTTR < 1 hour |
| 7 | D | Elite: высокая скорость И высокая стабильность |
| 8 | D | CI/CD, Git, K8s — автоматические источники |
| 9 | D | Оптимизация CI, меньше batch, trunk-based |
| 10 | C | Непрерывное автоматическое измерение |
| 11 | C | MTBF — Mean Time Between Failures |
| 12 | D | Меньшие deployments дают лучшие DORA metrics |
| 13 | C | Меньшие команды часто показывают лучшие результаты |
| 14 | A | Generative culture коррелирует с лучшими metrics |
| 15 | C | CI/CD, trunk-based dev, monitoring, loose coupling |
| 16 | D | Сравнивать свой прогресс, использовать benchmarks как ориентир |
| 17 | A | Автоматизация улучшает deployment frequency и lead time |
| 18 | D | Quality тесты снижают change failure rate |
| 19 | D | High psychological safety улучшает reporting и metrics |
| 20 | D | Identify bottlenecks, experiment, measure, iterate |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DevSecOps. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите improvement actions. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте классификацию уровней. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите четыре метрики. |

---

