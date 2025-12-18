# Cloud Native Development - Quiz
## Микросервисная архитектура

---

## Question 1: Bounded Context

Что определяет границы микросервиса в DDD подходе?

A) База данных

B) Команда разработки

C) Bounded Context

D) Количество строк кода

---

## Question 2: Database Strategy

Какая стратегия работы с данными рекомендуется для микросервисов?

A) Только in-memory storage

B) Shared database для всех сервисов

C) Одна большая NoSQL база

D) Database per service

---

## Question 3: Circuit Breaker

Что делает паттерн Circuit Breaker?

A) Останавливает запросы к failing сервису, предотвращая cascade failures

B) Шифрует трафик между сервисами

C) Кэширует ответы

D) Балансирует нагрузку

---

## Question 4: Sync vs Async

Какое преимущество асинхронной коммуникации?

A) Мгновенный ответ

B) Проще debugging

C) Loose coupling и resilience

D) Не требует message broker

---

## Question 5: Saga Pattern

Для чего используется Saga Pattern?

A) Для управления распределёнными транзакциями

B) Для авторизации

C) Для логирования

D) Для кэширования

---

## Question 6: API Gateway Pattern

Для чего используется API Gateway в микросервисах?

A) Только для security

B) Только для logging

C) Single entry point, auth, rate limiting, aggregation

D) Только для routing

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

A) Backup container

B) Дополнительный сервис

C) Test container

D) Helper container рядом с main для cross-cutting concerns

---

## Question 9: Event Sourcing

Что такое Event Sourcing?

A) Хранение изменений как events, восстановление state

B) Event scheduling

C) Logging events

D) Event notifications

---

## Question 10: CQRS

Что такое CQRS?

A) Caching Query Results System

B) Command Query Responsibility Segregation — разделение read/write

C) Central Query Routing Service

D) Command Query Response System

---

## Question 11: Strangler Pattern

Для чего используется Strangler Pattern?

A) Для logging

B) Для testing

C) Для security

D) Для постепенной migration от monolith к microservices

---

## Question 12: Bulkhead Pattern

Что делает Bulkhead Pattern?

A) Caching

B) Security isolation

C) Изолирует failures для предотвращения cascade

D) Load balancing

---

## Question 13: Retry Pattern

Как правильно реализовать retries?

A) Exponential backoff с jitter

B) Fixed delay

C) Immediate retry

D) No retries

---

## Question 14: Timeout Pattern

Почему важны timeouts?

A) Для security

B) Предотвращение hung requests и resource exhaustion

C) Для экономии

D) Для logging

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

A) Для security

B) Для billing

C) Для отслеживания requests через сервисы

D) Для logging

---

## Question 17: Choreography vs Orchestration

Чем Choreography отличается от Orchestration?

A) Choreography: events, децентрализовано. Orchestration: центральный coordinator

B) Orchestration проще

C) Ничем

D) Choreography быстрее

---

## Question 18: Contract Testing

Что тестирует Contract Testing?

A) Код

B) Performance

C) API contracts между сервисами

D) UI

---

## Question 19: Domain Events

Что такое Domain Events?

A) UI events

B) Значимые бизнес-события для коммуникации между bounded contexts

C) Log events

D) System events

---

## Question 20: Anti-Corruption Layer

Для чего используется Anti-Corruption Layer?

A) Для logging

B) Для security

C) Для caching

D) Для изоляции от legacy или external systems

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Bounded Context из DDD определяет natural boundary для микросервиса — область с единым ubiquitous language. |
| 2 | D | Database per service обеспечивает loose coupling. Shared database создаёт tight coupling между сервисами. |
| 3 | A | Circuit Breaker переходит в OPEN state при failures, отклоняя запросы и предотвращая cascade failures. |
| 4 | C | Async communication через events обеспечивает loose coupling — сервисы не зависят от доступности друг друга. |
| 5 | A | Saga управляет distributed transactions через последовательность локальных транзакций с compensation при failure. |
| 6 | C | API Gateway: single entry, auth, rate limiting |
| 7 | B | Service Discovery: registry (DNS, Consul) |
| 8 | D | Sidecar: helper container для cross-cutting concerns |
| 9 | A | Event Sourcing: хранение изменений как events |
| 10 | B | CQRS: разделение read/write responsibilities |
| 11 | D | Strangler: постепенная migration от monolith |
| 12 | C | Bulkhead: изоляция failures |
| 13 | A | Exponential backoff с jitter для retries |
| 14 | B | Timeouts предотвращают hung requests |
| 15 | D | Liveness и readiness health checks |
| 16 | C | Distributed tracing: отслеживание requests |
| 17 | A | Choreography: events. Orchestration: coordinator |
| 18 | C | Contract Testing: API contracts между сервисами |
| 19 | B | Domain Events: значимые бизнес-события |
| 20 | D | Anti-Corruption Layer: изоляция от legacy |

---

