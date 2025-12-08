# Cloud Native Development - Quiz
## CI/CD

---

## Question 1: CI vs CD

Что означает CI (Continuous Integration)?

A) Автоматический deploy в production
B) Автоматический build и тестирование при каждом commit
C) Контейнеризация приложений
D) Infrastructure as Code

---

## Question 2: Blue/Green Deployment

Какое преимущество Blue/Green deployment?

A) Меньше ресурсов
B) Instant rollback к предыдущей версии
C) Самая быстрая стратегия
D) Не требует load balancer

---

## Question 3: Canary Deployment

Что такое Canary deployment?

A) Полная замена всех instances сразу
B) Постепенный shift трафика с мониторингом
C) Deployment в разные regions
D) A/B тестирование UI

---

## Question 4: CodeBuild

Где определяются build steps в CodeBuild?

A) В консоли AWS
B) В buildspec.yml файле в репозитории
C) В CodePipeline
D) В CloudFormation

---

## Question 5: Pipeline Stages

Какой правильный порядок stages в типичном pipeline?

A) Deploy → Build → Test → Source
B) Source → Build → Test → Deploy
C) Test → Build → Deploy → Source
D) Build → Source → Deploy → Test

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CI = автоматический build и test при каждом commit. CD = автоматический deploy. |
| 2 | B | Blue/Green позволяет мгновенно переключить трафик обратно на старую версию при проблемах. |
| 3 | B | Canary: постепенно увеличивающийся % трафика на новую версию с мониторингом между шагами. |
| 4 | B | buildspec.yml в корне репозитория определяет phases, commands, artifacts. |
| 5 | B | Стандартный порядок: Source (код) → Build (компиляция) → Test (проверка) → Deploy (развёртывание). |

---
