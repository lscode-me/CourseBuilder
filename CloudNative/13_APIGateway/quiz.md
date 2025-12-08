# Cloud Native Development - Quiz
## API Gateway

---

## Question 1: REST vs HTTP API

Какое преимущество HTTP API над REST API?

A) Больше features
B) Ниже latency и цена
C) Поддержка caching
D) Поддержка WAF

---

## Question 2: Lambda Proxy

Что такое Lambda Proxy Integration?

A) Lambda запускается через proxy server
B) API Gateway передаёт весь request в Lambda без transformation
C) Lambda вызывает другую Lambda
D) Шифрование между API Gateway и Lambda

---

## Question 3: Authorization

Какой тип авторизации лучше для валидации JWT от Auth0 в HTTP API?

A) IAM Authorization
B) Lambda Authorizer
C) JWT Authorizer
D) API Keys

---

## Question 4: API Keys

Для чего используются API Keys в API Gateway?

A) Для безопасной аутентификации пользователей
B) Для rate limiting и usage tracking
C) Для шифрования данных
D) Для cross-account доступа

---

## Question 5: Caching

Какой тип API Gateway поддерживает встроенный caching?

A) HTTP API
B) REST API
C) WebSocket API
D) Все типы

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | HTTP API: ~10ms latency vs ~100ms, $1/million vs $3.50/million. Но меньше features. |
| 2 | B | Lambda Proxy передаёт весь request (headers, body, params) в Lambda, Lambda формирует response. |
| 3 | C | JWT Authorizer в HTTP API — встроенная валидация JWT. Для REST API нужен Lambda Authorizer. |
| 4 | B | API Keys — для rate limiting и tracking usage, НЕ для security. Легко украсть из client-side кода. |
| 5 | B | Caching доступен только в REST API. HTTP API не поддерживает кэширование. |

---
