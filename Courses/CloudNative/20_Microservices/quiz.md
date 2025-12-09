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

A) Database per service

B) Одна большая NoSQL база

C) Только in-memory storage

D) Shared database для всех сервисов

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

A) Проще debugging

B) Не требует message broker

C) Мгновенный ответ

D) Loose coupling и resilience

---

## Question 5: Saga Pattern


Для чего используется Saga Pattern?

A) Для управления распределёнными транзакциями

B) Для логирования

C) Для кэширования

D) Для авторизации

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Bounded Context из DDD определяет natural boundary для микросервиса — область с единым ubiquitous language. |
| 2 | A | Database per service обеспечивает loose coupling. Shared database создаёт tight coupling между сервисами. |
| 3 | A | Circuit Breaker переходит в OPEN state при failures, отклоняя запросы и предотвращая cascade failures. |
| 4 | D | Async communication через events обеспечивает loose coupling — сервисы не зависят от доступности друг друга. |
| 5 | A | Saga управляет distributed transactions через последовательность локальных транзакций с compensation при failure. |

---
