# Cloud Native Development - Quiz
## Введение в Cloud Native

---

## Question 1: Что такое CNCF?





A) Тип базы данных

B) Язык программирования

C) Организация, развивающая cloud native экосистему

D) Облачный провайдер

---

## Question 2: "Pets vs Cattle"





Что означает подход "Cattle"?

A) Использование животноводческого ПО

B) Серверы уникальны и незаменимы

C) Только физические серверы

D) Серверы заменяемы и эфемерны

---

## Question 3: Какой проект НЕ является CNCF Graduated?





A) Prometheus

B) MySQL

C) Kubernetes

D) Helm

---

## Question 4: Основной принцип Cloud Native





A) Design for simplicity

B) Design for perfection

C) Design for failure

D) Design for on-premise

---

## Question 5: Когда Cloud Native НЕ нужен?





A) Простое CRUD приложение маленькой команды

B) Микросервисная архитектура

C) Глобальное распределённое приложение

D) Высоконагруженные системы

---

## Question 6: Containers




Почему контейнеры важны для Cloud Native?

A) Дешевле VMs

B) Portability и consistency между environments

C) Быстрее запускаются

D) Не требуют ОС

---

## Question 7: Service Mesh




Для чего используется Service Mesh?

A) Observability, security, traffic management между сервисами

B) Только для networking

C) Только для storage

D) Только для compute

---

## Question 8: Prometheus




Что такое Prometheus?

A) Database

B) CNCF monitoring и alerting toolkit

C) CI/CD tool

D) Container runtime

---

## Question 9: Immutable Infrastructure




Что означает Immutable Infrastructure?

A) Только read-only storage

B) Неизменяемые secrets

C) Неизменяемые данные

D) Не изменять running infrastructure, а заменять

---

## Question 10: GitOps




Что такое GitOps?

A) Git security

B) Git backup

C) Git hosting

D) Git как source of truth для infrastructure и deployments

---

## Question 11: Declarative Configuration




Что означает Declarative подход?

A) Только YAML файлы

B) Только JSON файлы

C) Описывать желаемое состояние, система сама достигает

D) Описывать шаги выполнения

---

## Question 12: Observability




Что включает Observability?

A) Только logs

B) Logs, metrics, traces для понимания системы

C) Только monitoring

D) Только alerting

---

## Question 13: Loose Coupling




Почему Loose Coupling важен?

A) Дешевле

B) Независимое развитие и deployment компонентов

C) Быстрее

D) Проще

---

## Question 14: Resilience




Что означает Resilience?

A) Быстрое выполнение

B) Большой масштаб

C) Способность продолжать работать при failures

D) Низкая стоимость

---

## Question 15: Horizontal Scaling




Что такое Horizontal Scaling?

A) Увеличение bandwidth

B) Добавление больше instances одного сервиса

C) Увеличение storage

D) Увеличение размера сервера

---

## Question 16: Automation




Почему Automation критичен?

A) Для security только

B) Для compliance

C) Для экономии времени

D) Consistency, speed, reduced human error

---

## Question 17: Self-Healing




Что означает Self-Healing?

A) Ручное восстановление

B) Health checks

C) Автоматическое обнаружение и восстановление от failures

D) Backups

---

## Question 18: API-First




Что означает API-First подход?

A) Дизайн API/контрактов до implementation

B) gRPC только

C) REST только

D) GraphQL только

---

## Question 19: Security by Design




Что означает Security by Design?

A) Security audit после deployment

B) Интеграция security с начала разработки

C) Firewall только

D) Encryption только

---

## Question 20: Cost Optimization




Как Cloud Native помогает с Cost Optimization?

A) Фиксированная стоимость

B) Pay per use, auto-scaling, right-sizing

C) Бесплатно

D) Только для enterprise

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | CNCF (Cloud Native Computing Foundation) — организация, управляющая cloud native проектами. |
| 2 | D | "Cattle" — серверы заменяемы и эфемерны. Сломался — уничтожь и создай новый. |
| 3 | B | MySQL — не CNCF проект. Kubernetes, Prometheus, Helm — graduated CNCF проекты. |
| 4 | C | "Design for failure" — предполагайте, что всё может сломаться, и проектируйте устойчиво. |
| 5 | A | Для простого CRUD с маленькой командой монолит проще и эффективнее. |
| 6 | B | Containers: portability и consistency |
| 7 | A | Service Mesh: observability, security, traffic |
| 8 | B | Prometheus — CNCF monitoring toolkit |
| 9 | D | Immutable: не изменять, а заменять |
| 10 | D | GitOps: Git как source of truth |
| 11 | C | Declarative: описывать желаемое состояние |
| 12 | B | Observability: logs, metrics, traces |
| 13 | B | Loose Coupling: независимое развитие |
| 14 | C | Resilience: работа при failures |
| 15 | B | Horizontal: добавление instances |
| 16 | D | Automation: consistency, speed, fewer errors |
| 17 | C | Self-Healing: автоматическое восстановление |
| 18 | A | API-First: дизайн API до implementation |
| 19 | B | Security by Design: с начала разработки |
| 20 | B | Cost: pay per use, auto-scaling |

---
