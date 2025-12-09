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

B) API Keys

C) Lambda Authorizer

D) JWT Authorizer

---

## Question 4: API Keys





Для чего используются API Keys в API Gateway?

A) Для rate limiting и usage tracking

B) Для шифрования данных

C) Для cross-account доступа

D) Для безопасной аутентификации пользователей

---

## Question 5: Caching





Какой тип API Gateway поддерживает встроенный caching?

A) WebSocket API

B) Все типы

C) HTTP API

D) REST API

---

## Question 6: Stages




Для чего используются Stages в API Gateway?

A) Для security

B) Для deployment environments (dev/staging/prod)

C) Для caching

D) Для billing

---

## Question 7: Request Validation




Что может валидировать API Gateway?

A) Только headers

B) Request body, query parameters, headers по JSON Schema

C) Только body

D) Ничего

---

## Question 8: Throttling




Какой default throttling limit для API Gateway?

A) 100 RPS

B) 10,000 RPS (soft limit)

C) Unlimited

D) 1,000 RPS

---

## Question 9: Lambda Integration Types




Чем PROXY отличается от non-proxy integration?

A) Proxy передаёт всё в Lambda, non-proxy позволяет mapping templates

B) Non-proxy дешевле

C) Ничем

D) Proxy быстрее

---

## Question 10: Custom Domain




Как использовать custom domain с API Gateway?

A) Невозможно

B) ACM сертификат + Route 53 alias

C) Только платный план

D) Только с CloudFront

---

## Question 11: CORS




Как включить CORS в API Gateway?

A) Невозможно

B) Через CloudFront

C) Настроить в console или через OPTIONS method

D) Автоматически

---

## Question 12: VPC Link




Для чего используется VPC Link?

A) Для caching

B) Для logging

C) Для public APIs

D) Для private integration с resources в VPC

---

## Question 13: Access Logs




Куда можно отправлять access logs?

A) Только S3

B) CloudWatch Logs, Kinesis Firehose

C) Только CloudWatch

D) Только Kinesis

---

## Question 14: Mock Integration




Для чего используется Mock Integration?

A) Для тестирования без backend

B) Для security

C) Для caching

D) Для billing

---

## Question 15: Usage Plans




Что позволяют настроить Usage Plans?

A) Только logging

B) Только security

C) Throttling и quota для API keys

D) Только billing

---

## Question 16: WebSocket API




Для чего используется WebSocket API?

A) Для REST endpoints

B) Для real-time bidirectional communication

C) Для batch processing

D) Для file upload

---

## Question 17: Resource Policies




Что контролируют Resource Policies?

A) Только caching

B) Только logging

C) Только IAM users

D) Cross-account и IP-based access к API

---

## Question 18: Request/Response Transformation




Как трансформировать request/response?

A) Невозможно

B) Mapping templates (VTL) в REST API

C) Только в Lambda

D) Только с CloudFront

---

## Question 19: Private API




Как создать API доступный только из VPC?

A) IP whitelist

B) Security Groups

C) Custom domain

D) Private API с VPC Endpoint

---

## Question 20: Canary Deployments




Как реализовать canary deployment?

A) Только через Lambda

B) Невозможно

C) Только вручную

D) Canary settings на stage для traffic splitting

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | HTTP API: ~10ms latency vs ~100ms, $1/million vs $3.50/million. Но меньше features. |
| 2 | D | Lambda Proxy передаёт весь request (headers, body, params) в Lambda, Lambda формирует response. |
| 3 | D | JWT Authorizer в HTTP API — встроенная валидация JWT. Для REST API нужен Lambda Authorizer. |
| 4 | A | API Keys — для rate limiting и tracking usage, НЕ для security. Легко украсть из client-side кода. |
| 5 | D | Caching доступен только в REST API. HTTP API не поддерживает кэширование. |
| 6 | B | Stages для dev/staging/prod environments |
| 7 | B | Request validation: body, params, headers по JSON Schema |
| 8 | B | Default 10,000 RPS soft limit |
| 9 | A | Proxy передаёт всё, non-proxy позволяет mapping |
| 10 | B | ACM сертификат + Route 53 alias |
| 11 | C | Настроить в console или OPTIONS method |
| 12 | D | VPC Link для private integration |
| 13 | B | CloudWatch Logs, Kinesis Firehose |
| 14 | A | Mock Integration для тестирования без backend |
| 15 | C | Usage Plans: throttling и quota для API keys |
| 16 | B | WebSocket для real-time bidirectional communication |
| 17 | D | Resource Policies: cross-account и IP-based access |
| 18 | B | Mapping templates (VTL) в REST API |
| 19 | D | Private API с VPC Endpoint |
| 20 | D | Canary settings для traffic splitting |

---
