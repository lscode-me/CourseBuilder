# Cloud Native Development - Quiz
## AWS Lambda

---

## Question 1: Максимальный timeout Lambda?


A) 15 минут

B) 5 минут

C) 30 минут

D) 60 минут

---

## Question 2: Что такое Cold Start?


A) Задержка при первом вызове из-за инициализации runtime

B) Запуск Lambda в холодном регионе

C) Ошибка запуска функции

D) Тестовый режим

---

## Question 3: Где инициализировать boto3 client?


A) В environment variables

B) Вне handler функции (global scope)

C) Внутри handler функции

D) В отдельном Lambda layer

---

## Question 4: Какой триггер СИНХРОННЫЙ?


A) SNS

B) EventBridge schedule

C) API Gateway

D) S3 (object created)

---

## Question 5: Что делает Provisioned Concurrency?


A) Автоматически масштабирует

B) Увеличивает memory

C) Держит warm instances готовыми для устранения cold start

D) Ограничивает concurrent executions

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Максимальный timeout Lambda — 15 минут (900 секунд). |
| 2 | A | Cold Start — задержка при создании нового execution environment: download code, start runtime, init. |
| 3 | B | SDK clients инициализируются вне handler для переиспользования между вызовами (warm invocations). |
| 4 | C | API Gateway — синхронный, ждёт ответа. S3, SNS, EventBridge — асинхронные. |
| 5 | C | Provisioned Concurrency держит указанное количество warm instances, устраняя cold start. |

---
