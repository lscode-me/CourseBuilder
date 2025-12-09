# Cloud Native Development - Quiz
## API Gateway

---

## Question 1: REST vs HTTP API







Какое преимущество HTTP API над REST API?

A) Поддержка caching

B) Больше features

C) Поддержка WAF

D) Ниже latency и цена

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

A) Только body

B) Request body, query parameters, headers по JSON Schema

C) Ничего

D) Только headers

---

## Question 8: Throttling






Какой default throttling limit для API Gateway?

A) 100 RPS

B) 1,000 RPS

C) 10,000 RPS (soft limit)

D) Unlimited

---

## Question 9: Lambda Integration Types






Чем PROXY отличается от non-proxy integration?

A) Proxy быстрее

B) Ничем

C) Non-proxy дешевле

D) Proxy передаёт всё в Lambda, non-proxy позволяет mapping templates

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

A) Только Kinesis

B) Только S3

C) Только CloudWatch

D) CloudWatch Logs, Kinesis Firehose

---

## Question 14: Mock Integration






Для чего используется Mock Integration?

A) Для billing

B) Для security

C) Для тестирования без backend

D) Для caching

---

## Question 15: Usage Plans






Что позволяют настроить Usage Plans?

A) Только security

B) Только logging

C) Только billing

D) Throttling и quota для API keys

---

## Question 16: WebSocket API






Для чего используется WebSocket API?

A) Для file upload

B) Для REST endpoints

C) Для batch processing

D) Для real-time bidirectional communication

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

A) Mapping templates (VTL) в REST API

B) Только с CloudFront

C) Только в Lambda

D) Невозможно

---

## Question 19: Private API






Как создать API доступный только из VPC?

A) Private API с VPC Endpoint

B) Custom domain

C) Security Groups

D) IP whitelist

---

## Question 20: Canary Deployments






Как реализовать canary deployment?

A) Canary settings на stage для traffic splitting

B) Только вручную

C) Невозможно

D) Только через Lambda

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | HTTP API: ~10ms latency vs ~100ms, $1/million vs $3.50/million. Но меньше features. |
| 2 | B | Lambda Proxy передаёт весь request (headers, body, params) в Lambda, Lambda формирует response. |
| 3 | D | JWT Authorizer в HTTP API — встроенная валидация JWT. Для REST API нужен Lambda Authorizer. |
| 4 | A | API Keys — для rate limiting и tracking usage, НЕ для security. Легко украсть из client-side кода. |
| 5 | D | Caching доступен только в REST API. HTTP API не поддерживает кэширование. |
| 6 | B | Stages для dev/staging/prod environments |
| 7 | B | Request validation: body, params, headers по JSON Schema |
| 8 | C | Default 10,000 RPS soft limit |
| 9 | D | Proxy передаёт всё, non-proxy позволяет mapping |
| 10 | B | ACM сертификат + Route 53 alias |
| 11 | C | Настроить в console или OPTIONS method |
| 12 | D | VPC Link для private integration |
| 13 | D | CloudWatch Logs, Kinesis Firehose |
| 14 | C | Mock Integration для тестирования без backend |
| 15 | D | Usage Plans: throttling и quota для API keys |
| 16 | D | WebSocket для real-time bidirectional communication |
| 17 | D | Resource Policies: cross-account и IP-based access |
| 18 | A | Mapping templates (VTL) в REST API |
| 19 | A | Private API с VPC Endpoint |
| 20 | A | Canary settings для traffic splitting |

---
