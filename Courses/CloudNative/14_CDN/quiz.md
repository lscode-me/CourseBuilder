# Cloud Native Development - Quiz
## CDN: CloudFront

---

## Question 1: CDN Purpose

Какая основная цель CDN?

A) Балансировка нагрузки

B) Шифрование данных

C) Хранение данных

D) Доставка контента с низкой latency через edge locations

---

## Question 2: Cache Key

Что входит в cache key по умолчанию?

A) URL path + все headers

B) URL path + query strings + headers

C) Весь HTTP request

D) Только URL path

---

## Question 3: OAC

Для чего используется Origin Access Control?

A) Для кэширования

B) Для шифрования трафика

C) Для rate limiting

D) Для ограничения доступа к S3 только через CloudFront

---

## Question 4: CloudFront Functions vs Lambda@Edge

Какое преимущество CloudFront Functions?

A) Поддержка Python

B) Быстрее и дешевле (< 1ms, $0.10/million)

C) Больше памяти

D) Network доступ

---

## Question 5: Invalidation

Какой лучший способ обновить кэшированный контент?

A) Invalidation API

B) Перезапустить distribution

C) Ждать TTL expiry

D) Использовать versioned URLs (app.v2.js)

---

## Question 6: Price Classes

Что такое Price Classes в CloudFront?

A) Billing tiers

B) Security levels

C) Ограничение на какие edge locations использовать (cost vs latency)

D) Cache tiers

---

## Question 7: Signed URLs

Для чего используются Signed URLs?

A) Для кэширования

B) Для compression

C) Для временного доступа к private content

D) Для SEO

---

## Question 8: Field-Level Encryption

Что делает Field-Level Encryption?

A) Шифрует logs

B) Шифрует отдельные поля на edge до origin

C) Шифрует S3 bucket

D) Шифрует весь трафик

---

## Question 9: Geo Restriction

Как ограничить доступ по географии?

A) Geo Restriction (whitelist/blacklist countries)

B) Невозможно

C) Через Route 53

D) Через WAF только

---

## Question 10: WAF Integration

Как защитить CloudFront от атак?

A) Shield только

B) NACL

C) AWS WAF integration

D) Security Groups

---

## Question 11: Multiple Origins

Как настроить multiple origins?

A) Origin Groups с failover или path-based routing

B) Несколько distributions

C) Невозможно

D) Через Lambda only

---

## Question 12: Compression

Как включить сжатие в CloudFront?

A) Всегда включено

B) Compress objects automatically setting

C) Только в origin

D) Невозможно

---

## Question 13: Real-Time Logs

Куда можно отправлять real-time logs?

A) Только файлы

B) Kinesis Data Streams для real-time analysis

C) Только S3

D) Только CloudWatch

---

## Question 14: Alternate Domain Names

Что такое CNAMEs в CloudFront?

A) Origin servers

B) Cache rules

C) DNS серверы

D) Custom domain names для distribution

---

## Question 15: S3 vs Custom Origin

Когда использовать Custom Origin вместо S3?

A) Никогда

B) Для dynamic content, ALB, EC2, on-premises servers

C) Для дешевизны

D) Для static content

---

## Question 16: Behaviors

Что настраивают Cache Behaviors?

A) Только caching

B) Path patterns → origin mapping, caching, protocols, headers

C) Только security

D) Только logging

---

## Question 17: HTTP/3

Поддерживает ли CloudFront HTTP/3?

A) Нет

B) Да, QUIC protocol для better performance

C) Только для S3

D) Только enterprise

---

## Question 18: Viewer Protocol Policy

Что настраивает Viewer Protocol Policy?

A) Compression

B) Origin protocol

C) Caching

D) HTTP/HTTPS/redirect между viewer и CloudFront

---

## Question 19: Origin Shield

Что делает Origin Shield?

A) Security feature

B) SSL termination

C) Дополнительный caching layer между edge и origin

D) DDoS protection

---

## Question 20: Continuous Deployment

Как тестировать изменения в CloudFront?

A) Только production

B) Невозможно

C) Staging distribution или continuous deployment policies

D) Только локально

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | CDN кэширует контент на edge locations ближе к пользователям, снижая latency. |
| 2 | D | По умолчанию cache key = только URL path. Query strings и headers нужно добавлять явно. |
| 3 | D | OAC позволяет S3 bucket быть private, но доступным через CloudFront. |
| 4 | B | CloudFront Functions: < 1ms execution, $0.10/million. Lambda@Edge: больше возможностей, но дороже. |
| 5 | D | Versioned URLs (app.v2.js) — лучшая практика. Invalidation платный и не мгновенный. |
| 6 | C | Price Classes ограничивают edge locations |
| 7 | C | Signed URLs для временного private доступа |
| 8 | B | Field-Level Encryption шифрует поля на edge |
| 9 | A | Geo Restriction whitelist/blacklist countries |
| 10 | C | AWS WAF integration для защиты |
| 11 | A | Origin Groups с failover или path routing |
| 12 | B | Compress objects automatically setting |
| 13 | B | Kinesis Data Streams для real-time logs |
| 14 | D | CNAMEs — custom domain names |
| 15 | B | Custom Origin для dynamic content, ALB, EC2 |
| 16 | B | Cache Behaviors: path → origin, caching, etc |
| 17 | B | HTTP/3 QUIC protocol поддерживается |
| 18 | D | Viewer Protocol Policy: HTTP/HTTPS/redirect |
| 19 | C | Origin Shield — дополнительный caching layer |
| 20 | C | Staging distribution или continuous deployment |

---

