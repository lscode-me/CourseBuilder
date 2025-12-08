# Cloud Native Development - Quiz
## CDN: CloudFront

---

## Question 1: CDN Purpose

Какая основная цель CDN?

A) Хранение данных
B) Доставка контента с низкой latency через edge locations
C) Балансировка нагрузки
D) Шифрование данных

---

## Question 2: Cache Key

Что входит в cache key по умолчанию?

A) URL path + query strings + headers
B) Только URL path
C) URL path + все headers
D) Весь HTTP request

---

## Question 3: OAC

Для чего используется Origin Access Control?

A) Для шифрования трафика
B) Для ограничения доступа к S3 только через CloudFront
C) Для rate limiting
D) Для кэширования

---

## Question 4: CloudFront Functions vs Lambda@Edge

Какое преимущество CloudFront Functions?

A) Больше памяти
B) Network доступ
C) Быстрее и дешевле (< 1ms, $0.10/million)
D) Поддержка Python

---

## Question 5: Invalidation

Какой лучший способ обновить кэшированный контент?

A) Ждать TTL expiry
B) Invalidation API
C) Использовать versioned URLs (app.v2.js)
D) Перезапустить distribution

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CDN кэширует контент на edge locations ближе к пользователям, снижая latency. |
| 2 | B | По умолчанию cache key = только URL path. Query strings и headers нужно добавлять явно. |
| 3 | B | OAC позволяет S3 bucket быть private, но доступным через CloudFront. |
| 4 | C | CloudFront Functions: < 1ms execution, $0.10/million. Lambda@Edge: больше возможностей, но дороже. |
| 5 | C | Versioned URLs (app.v2.js) — лучшая практика. Invalidation платный и не мгновенный. |

---
