# Cloud Native Development - Quiz
## Микросервисная архитектура

---

## Question 1: Bounded Context





Что определяет границы микросервиса в DDD подходе?

A) Bounded Context

B) База данных

C) Команда разработки

D) Количество строк кода

---

## Question 2: Database Strategy





Какая стратегия работы с данными рекомендуется для микросервисов?

A) Shared database для всех сервисов

B) Только in-memory storage

C) Database per service

D) Одна большая NoSQL база

---

## Question 3: Circuit Breaker





Что делает паттерн Circuit Breaker?

A) Останавливает запросы к failing сервису, предотвращая cascade failures

B) Кэширует ответы

C) Балансирует нагрузку

D) Шифрует трафик между сервисами

---

## Question 4: Sync vs Async





Какое преимущество асинхронной коммуникации?

A) Не требует message broker

B) Loose coupling и resilience

C) Проще debugging

D) Мгновенный ответ

---

## Question 5: Saga Pattern





Для чего используется Saga Pattern?

A) Для управления распределёнными транзакциями

B) Для логирования

C) Для кэширования

D) Для авторизации

---

## Question 6: API Gateway Pattern




Для чего используется API Gateway в микросервисах?

A) Только для logging

B) Только для security

C) Только для routing

D) Single entry point, auth, rate limiting, aggregation

---

## Question 7: Service Discovery




Как сервисы находят друг друга?

A) Hardcoded IPs

B) Service registry (DNS, Consul, Cloud Map)

C) Только через load balancer

D) Manual configuration

---

## Question 8: Sidecar Pattern




Что такое Sidecar Pattern?

A) Helper container рядом с main для cross-cutting concerns

B) Test container

C) Дополнительный сервис

D) Backup container

---

## Question 9: Event Sourcing




Что такое Event Sourcing?

A) Event notifications

B) Logging events

C) Event scheduling

D) Хранение изменений как events, восстановление state

---

## Question 10: CQRS




Что такое CQRS?

A) Command Query Response System

B) Command Query Responsibility Segregation — разделение read/write

C) Caching Query Results System

D) Central Query Routing Service

---

## Question 11: Strangler Pattern




Для чего используется Strangler Pattern?

A) Для testing

B) Для logging

C) Для постепенной migration от monolith к microservices

D) Для security

---

## Question 12: Bulkhead Pattern




Что делает Bulkhead Pattern?

A) Изолирует failures для предотвращения cascade

B) Load balancing

C) Caching

D) Security isolation

---

## Question 13: Retry Pattern




Как правильно реализовать retries?

A) Immediate retry

B) Exponential backoff с jitter

C) Fixed delay

D) No retries

---

## Question 14: Timeout Pattern




Почему важны timeouts?

A) Для экономии

B) Предотвращение hung requests и resource exhaustion

C) Для logging

D) Для security

---

## Question 15: Health Checks




Какие типы health checks используются?

A) Только readiness

B) Manual checks

C) Только liveness

D) Liveness (alive?) и readiness (ready for traffic?)

---

## Question 16: Distributed Tracing




Для чего используется distributed tracing?

A) Для billing

B) Для security

C) Для logging

D) Для отслеживания requests через сервисы

---

## Question 17: Choreography vs Orchestration




Чем Choreography отличается от Orchestration?

A) Choreography быстрее

B) Ничем

C) Orchestration проще

D) Choreography: events, децентрализовано. Orchestration: центральный coordinator

---

## Question 18: Contract Testing




Что тестирует Contract Testing?

A) Код

B) API contracts между сервисами

C) UI

D) Performance

---

## Question 19: Domain Events




Что такое Domain Events?

A) Log events

B) Значимые бизнес-события для коммуникации между bounded contexts

C) System events

D) UI events

---

## Question 20: Anti-Corruption Layer




Для чего используется Anti-Corruption Layer?

A) Для security

B) Для изоляции от legacy или external systems

C) Для caching

D) Для logging

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Bounded Context из DDD определяет natural boundary для микросервиса — область с единым ubiquitous language. |
| 2 | C | Database per service обеспечивает loose coupling. Shared database создаёт tight coupling между сервисами. |
| 3 | A | Circuit Breaker переходит в OPEN state при failures, отклоняя запросы и предотвращая cascade failures. |
| 4 | B | Async communication через events обеспечивает loose coupling — сервисы не зависят от доступности друг друга. |
| 5 | A | Saga управляет distributed transactions через последовательность локальных транзакций с compensation при failure. |
| 6 | D | API Gateway: single entry, auth, rate limiting |
| 7 | B | Service Discovery: registry (DNS, Consul) |
| 8 | A | Sidecar: helper container для cross-cutting concerns |
| 9 | D | Event Sourcing: хранение изменений как events |
| 10 | B | CQRS: разделение read/write responsibilities |
| 11 | C | Strangler: постепенная migration от monolith |
| 12 | A | Bulkhead: изоляция failures |
| 13 | B | Exponential backoff с jitter для retries |
| 14 | B | Timeouts предотвращают hung requests |
| 15 | D | Liveness и readiness health checks |
| 16 | D | Distributed tracing: отслеживание requests |
| 17 | D | Choreography: events. Orchestration: coordinator |
| 18 | B | Contract Testing: API contracts между сервисами |
| 19 | B | Domain Events: значимые бизнес-события |
| 20 | B | Anti-Corruption Layer: изоляция от legacy |

---
