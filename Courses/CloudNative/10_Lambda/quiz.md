# Cloud Native Development - Quiz
## AWS Lambda

---

## Question 1: Максимальный timeout Lambda?

A) 15 минут

B) 30 минут

C) 5 минут

D) 60 минут

---

## Question 2: Что такое Cold Start?

A) Запуск Lambda в холодном регионе

B) Тестовый режим

C) Ошибка запуска функции

D) Задержка при первом вызове из-за инициализации runtime

---

## Question 3: Где инициализировать boto3 client?

A) Внутри handler функции

B) Вне handler функции (global scope)

C) В environment variables

D) В отдельном Lambda layer

---

## Question 4: Какой триггер СИНХРОННЫЙ?

A) S3 (object created)

B) API Gateway

C) EventBridge schedule

D) SNS

---

## Question 5: Что делает Provisioned Concurrency?

A) Увеличивает memory

B) Держит warm instances готовыми для устранения cold start

C) Автоматически масштабирует

D) Ограничивает concurrent executions

---

## Question 6: Layers

Для чего используются Lambda Layers?

A) Для logging

B) Для security

C) Для sharing libraries/dependencies между functions

D) Для networking

---

## Question 7: Memory

Как memory влияет на CPU в Lambda?

A) Меньше memory = больше CPU

B) Больше memory = пропорционально больше CPU

C) CPU настраивается отдельно

D) Не влияет

---

## Question 8: Concurrency Limit

Какой default лимит concurrent executions?

A) Безлимитно

B) 1000

C) 10000

D) 100

---

## Question 9: Reserved Concurrency

Что делает Reserved Concurrency?

A) Включает VPC

B) Ускоряет выполнение

C) Увеличивает memory

D) Резервирует capacity для function, ограничивает max

---

## Question 10: Destinations

Для чего используются Destinations?

A) Для routing результатов async invocations (success/failure)

B) Для логирования

C) Для networking

D) Для шифрования

---

## Question 11: VPC Lambda

Какие компоненты нужны для Lambda в VPC?

A) Internet Gateway

B) Только Security Group

C) Subnet + Security Group + NAT для интернета

D) Только subnet

---

## Question 12: Environment Variables

Как безопасно хранить секреты для Lambda?

A) В коде

B) В Environment Variables + KMS encryption, или Secrets Manager

C) В логах

D) В S3

---

## Question 13: Dead Letter Queue

Для чего используется DLQ в Lambda?

A) Для шифрования

B) Для логирования

C) Для failed async invocations

D) Для хранения результатов

---

## Question 14: SnapStart

Что делает Lambda SnapStart (Java)?

A) Ускоряет deployment

B) Создаёт snapshot initialized VM для быстрого cold start

C) Шифрует код

D) Увеличивает memory

---

## Question 15: Function URL

Что такое Function URL?

A) VPC endpoint

B) IAM endpoint

C) S3 URL

D) Dedicated HTTP endpoint для Lambda без API Gateway

---

## Question 16: Ephemeral Storage

Какой размер /tmp в Lambda?

A) 512 MB only

B) 1 GB only

C) Unlimited

D) 512 MB до 10 GB (configurable)

---

## Question 17: X-Ray

Для чего Lambda использует X-Ray?

A) Для distributed tracing

B) Для networking

C) Для backup

D) Для шифрования

---

## Question 18: Alias

Для чего используются Lambda Aliases?

A) Для логирования

B) Для security

C) Для traffic shifting и environment management (dev/prod)

D) Для шифрования

---

## Question 19: Extensions

Что такое Lambda Extensions?

A) Увеличение memory

B) Дополнительные процессы для monitoring/security

C) Увеличение timeout

D) Новые языки

---

## Question 20: ARM vs x86

Какое преимущество AWS Graviton2 (ARM) для Lambda?

A) Длиннее timeout

B) Дешевле (~34%) с хорошей производительностью

C) Быстрее

D) Больше memory

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Максимальный timeout Lambda — 15 минут (900 секунд). |
| 2 | D | Cold Start — задержка при создании нового execution environment: download code, start runtime, init. |
| 3 | B | SDK clients инициализируются вне handler для переиспользования между вызовами (warm invocations). |
| 4 | B | API Gateway — синхронный, ждёт ответа. S3, SNS, EventBridge — асинхронные. |
| 5 | B | Provisioned Concurrency держит указанное количество warm instances, устраняя cold start. |
| 6 | C | Layers для sharing libraries между functions |
| 7 | B | Больше memory = пропорционально больше CPU |
| 8 | B | Default limit 1000 concurrent executions |
| 9 | D | Reserved Concurrency резервирует и ограничивает capacity |
| 10 | A | Destinations для routing async results |
| 11 | C | VPC Lambda: subnet + SG + NAT для интернета |
| 12 | B | Secrets в env vars + KMS или Secrets Manager |
| 13 | C | DLQ для failed async invocations |
| 14 | B | SnapStart — snapshot VM для быстрого cold start |
| 15 | D | Function URL — HTTP endpoint без API Gateway |
| 16 | D | /tmp: 512 MB до 10 GB configurable |
| 17 | A | X-Ray для distributed tracing |
| 18 | C | Aliases для traffic shifting и environments |
| 19 | B | Extensions — дополнительные процессы |
| 20 | B | Graviton2 ARM дешевле ~34% |

---

