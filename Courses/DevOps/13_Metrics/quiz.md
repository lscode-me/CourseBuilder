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

A) Code Coverage, Bugs, Technical Debt, Velocity

B) Deployment Frequency, Lead Time, Change Failure Rate, MTTR

C) CPU, Memory, Disk, Network

D) Availability, Latency, Throughput, Errors

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

A) Время от commit до production

B) Время code review

C) Время тестирования

D) Время написания кода

---

## Question 5: Change Failure Rate


Что показывает Change Failure Rate?

A) Количество багов

B) Количество строк кода

C) Скорость разработки

D) Процент деплоев, вызывающих сбои

---

## Question 6: MTTR Elite


Какой MTTR у Elite performers?

A) < 1 hour

B) < 1 day

C) < 1 week

D) < 1 month

---

## Question 7: Throughput vs Stability


Как связаны скорость (throughput) и стабильность?

A) Выше скорость = ниже стабильность

B) Не связаны

C) Elite performers имеют высокую скорость И высокую стабильность

D) Стабильность важнее скорости всегда

---

## Question 8: Data Sources


Откуда брать данные для Deployment Frequency?

A) Финансовые отчёты

B) Опросы разработчиков

C) CI/CD pipeline, Git tags, Kubernetes events

D) Ручной подсчёт

---

## Question 9: Improvement


Как улучшить высокий Lead Time?

A) Реже деплоить

B) Увеличить количество тестов

C) Оптимизировать CI, уменьшить batch size, trunk-based development

D) Нанять больше разработчиков

---

## Question 10: Measurement


Как часто нужно измерять DORA метрики?

A) Только при проблемах

B) Раз в квартал вручную

C) Непрерывно (автоматически)

D) Раз в год

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | DORA — DevOps Research and Assessment |
| 2 | B | DF, Lead Time, CFR, MTTR — четыре ключевые метрики |
| 3 | D | Elite performers деплоят on-demand |
| 4 | A | Lead Time = время от commit до production |
| 5 | D | CFR = % деплоев, вызывающих сбои |
| 6 | A | Elite MTTR < 1 hour |
| 7 | C | Elite: высокая скорость И высокая стабильность |
| 8 | C | CI/CD, Git, K8s — автоматические источники |
| 9 | C | Оптимизация CI, меньше batch, trunk-based |
| 10 | C | Непрерывное автоматическое измерение |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к DevSecOps. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите improvement actions. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте классификацию уровней. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите четыре метрики. |

---

