# Cloud Native Development - Quiz
## AWS Lambda

---

## Question 1: Максимальный timeout Lambda?

A) 5 минут
B) 15 минут
C) 30 минут
D) 60 минут

---

## Question 2: Что такое Cold Start?

A) Запуск Lambda в холодном регионе
B) Задержка при первом вызове из-за инициализации runtime
C) Ошибка запуска функции
D) Тестовый режим

---

## Question 3: Где инициализировать boto3 client?

A) Внутри handler функции
B) Вне handler функции (global scope)
C) В отдельном Lambda layer
D) В environment variables

---

## Question 4: Какой триггер СИНХРОННЫЙ?

A) S3 (object created)
B) SNS
C) API Gateway
D) EventBridge schedule

---

## Question 5: Что делает Provisioned Concurrency?

A) Увеличивает memory
B) Держит warm instances готовыми для устранения cold start
C) Ограничивает concurrent executions
D) Автоматически масштабирует

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Максимальный timeout Lambda — 15 минут (900 секунд). |
| 2 | B | Cold Start — задержка при создании нового execution environment: download code, start runtime, init. |
| 3 | B | SDK clients инициализируются вне handler для переиспользования между вызовами (warm invocations). |
| 4 | C | API Gateway — синхронный, ждёт ответа. S3, SNS, EventBridge — асинхронные. |
| 5 | B | Provisioned Concurrency держит указанное количество warm instances, устраняя cold start. |

---
