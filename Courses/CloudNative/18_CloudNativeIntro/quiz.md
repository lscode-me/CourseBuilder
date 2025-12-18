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

B) Kubernetes

C) Helm

D) MySQL

---

## Question 4: Основной принцип Cloud Native

A) Design for on-premise

B) Design for perfection

C) Design for simplicity

D) Design for failure

---

## Question 5: Когда Cloud Native НЕ нужен?

A) Высоконагруженные системы

B) Глобальное распределённое приложение

C) Микросервисная архитектура

D) Простое CRUD приложение маленькой команды

---

## Question 6: Containers

Почему контейнеры важны для Cloud Native?

A) Portability и consistency между environments

B) Быстрее запускаются

C) Дешевле VMs

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

A) Git backup

B) Git security

C) Git как source of truth для infrastructure и deployments

D) Git hosting

---

## Question 11: Declarative Configuration

Что означает Declarative подход?

A) Только JSON файлы

B) Только YAML файлы

C) Описывать шаги выполнения

D) Описывать желаемое состояние, система сама достигает

---

## Question 12: Observability

Что включает Observability?

A) Logs, metrics, traces для понимания системы

B) Только monitoring

C) Только logs

D) Только alerting

---

## Question 13: Loose Coupling

Почему Loose Coupling важен?

A) Дешевле

B) Быстрее

C) Проще

D) Независимое развитие и deployment компонентов

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

A) Для compliance

B) Для security только

C) Consistency, speed, reduced human error

D) Для экономии времени

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

A) GraphQL только

B) REST только

C) gRPC только

D) Дизайн API/контрактов до implementation

---

## Question 19: Security by Design

Что означает Security by Design?

A) Security audit после deployment

B) Encryption только

C) Интеграция security с начала разработки

D) Firewall только

---

## Question 20: Cost Optimization

Как Cloud Native помогает с Cost Optimization?

A) Бесплатно

B) Фиксированная стоимость

C) Pay per use, auto-scaling, right-sizing

D) Только для enterprise

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | CNCF (Cloud Native Computing Foundation) — организация, управляющая cloud native проектами. |
| 2 | D | "Cattle" — серверы заменяемы и эфемерны. Сломался — уничтожь и создай новый. |
| 3 | D | MySQL — не CNCF проект. Kubernetes, Prometheus, Helm — graduated CNCF проекты. |
| 4 | D | "Design for failure" — предполагайте, что всё может сломаться, и проектируйте устойчиво. |
| 5 | D | Для простого CRUD с маленькой командой монолит проще и эффективнее. |
| 6 | A | Containers: portability и consistency |
| 7 | A | Service Mesh: observability, security, traffic |
| 8 | B | Prometheus — CNCF monitoring toolkit |
| 9 | D | Immutable: не изменять, а заменять |
| 10 | C | GitOps: Git как source of truth |
| 11 | D | Declarative: описывать желаемое состояние |
| 12 | A | Observability: logs, metrics, traces |
| 13 | D | Loose Coupling: независимое развитие |
| 14 | C | Resilience: работа при failures |
| 15 | B | Horizontal: добавление instances |
| 16 | C | Automation: consistency, speed, fewer errors |
| 17 | C | Self-Healing: автоматическое восстановление |
| 18 | D | API-First: дизайн API до implementation |
| 19 | C | Security by Design: с начала разработки |
| 20 | C | Cost: pay per use, auto-scaling |

---

