# Cloud Native Development - Quiz
## Микросервисная архитектура

---

## Question 1: Bounded Context

Что определяет границы микросервиса в DDD подходе?

A) Количество строк кода
B) Bounded Context
C) Команда разработки
D) База данных

---

## Question 2: Database Strategy

Какая стратегия работы с данными рекомендуется для микросервисов?

A) Shared database для всех сервисов
B) Database per service
C) Одна большая NoSQL база
D) Только in-memory storage

---

## Question 3: Circuit Breaker

Что делает паттерн Circuit Breaker?

A) Шифрует трафик между сервисами
B) Останавливает запросы к failing сервису, предотвращая cascade failures
C) Балансирует нагрузку
D) Кэширует ответы

---

## Question 4: Sync vs Async

Какое преимущество асинхронной коммуникации?

A) Мгновенный ответ
B) Loose coupling и resilience
C) Проще debugging
D) Не требует message broker

---

## Question 5: Saga Pattern

Для чего используется Saga Pattern?

A) Для авторизации
B) Для управления распределёнными транзакциями
C) Для кэширования
D) Для логирования

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Bounded Context из DDD определяет natural boundary для микросервиса — область с единым ubiquitous language. |
| 2 | B | Database per service обеспечивает loose coupling. Shared database создаёт tight coupling между сервисами. |
| 3 | B | Circuit Breaker переходит в OPEN state при failures, отклоняя запросы и предотвращая cascade failures. |
| 4 | B | Async communication через events обеспечивает loose coupling — сервисы не зависят от доступности друг друга. |
| 5 | B | Saga управляет distributed transactions через последовательность локальных транзакций с compensation при failure. |

---
