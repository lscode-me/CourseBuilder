# Cloud Native Development - Quiz
## CI/CD

---

## Question 1: CI vs CD


Что означает CI (Continuous Integration)?

A) Infrastructure as Code

B) Автоматический build и тестирование при каждом commit

C) Контейнеризация приложений

D) Автоматический deploy в production

---

## Question 2: Blue/Green Deployment


Какое преимущество Blue/Green deployment?

A) Меньше ресурсов

B) Самая быстрая стратегия

C) Не требует load balancer

D) Instant rollback к предыдущей версии

---

## Question 3: Canary Deployment


Что такое Canary deployment?

A) Постепенный shift трафика с мониторингом

B) Полная замена всех instances сразу

C) A/B тестирование UI

D) Deployment в разные regions

---

## Question 4: CodeBuild


Где определяются build steps в CodeBuild?

A) В CloudFormation

B) В CodePipeline

C) В консоли AWS

D) В buildspec.yml файле в репозитории

---

## Question 5: Pipeline Stages


Какой правильный порядок stages в типичном pipeline?

A) Source → Build → Test → Deploy

B) Deploy → Build → Test → Source

C) Test → Build → Deploy → Source

D) Build → Source → Deploy → Test

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CI = автоматический build и test при каждом commit. CD = автоматический deploy. |
| 2 | D | Blue/Green позволяет мгновенно переключить трафик обратно на старую версию при проблемах. |
| 3 | A | Canary: постепенно увеличивающийся % трафика на новую версию с мониторингом между шагами. |
| 4 | D | buildspec.yml в корне репозитория определяет phases, commands, artifacts. |
| 5 | A | Стандартный порядок: Source (код) → Build (компиляция) → Test (проверка) → Deploy (развёртывание). |

---
