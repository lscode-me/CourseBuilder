# Cloud Native Development - Quiz
## API Gateway

---

## Question 1: REST vs HTTP API


Какое преимущество HTTP API над REST API?

A) Больше features

B) Поддержка WAF

C) Поддержка caching

D) Ниже latency и цена

---

## Question 2: Lambda Proxy


Что такое Lambda Proxy Integration?

A) Шифрование между API Gateway и Lambda

B) Lambda запускается через proxy server

C) Lambda вызывает другую Lambda

D) API Gateway передаёт весь request в Lambda без transformation

---

## Question 3: Authorization


Какой тип авторизации лучше для валидации JWT от Auth0 в HTTP API?

A) IAM Authorization

B) Lambda Authorizer

C) API Keys

D) JWT Authorizer

---

## Question 4: API Keys


Для чего используются API Keys в API Gateway?

A) Для шифрования данных

B) Для rate limiting и usage tracking

C) Для cross-account доступа

D) Для безопасной аутентификации пользователей

---

## Question 5: Caching


Какой тип API Gateway поддерживает встроенный caching?

A) Все типы

B) WebSocket API

C) HTTP API

D) REST API

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | HTTP API: ~10ms latency vs ~100ms, $1/million vs $3.50/million. Но меньше features. |
| 2 | D | Lambda Proxy передаёт весь request (headers, body, params) в Lambda, Lambda формирует response. |
| 3 | D | JWT Authorizer в HTTP API — встроенная валидация JWT. Для REST API нужен Lambda Authorizer. |
| 4 | B | API Keys — для rate limiting и tracking usage, НЕ для security. Легко украсть из client-side кода. |
| 5 | D | Caching доступен только в REST API. HTTP API не поддерживает кэширование. |

---
