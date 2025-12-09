# Cloud Native Development - Quiz
## CDN: CloudFront

---

## Question 1: CDN Purpose


Какая основная цель CDN?

A) Доставка контента с низкой latency через edge locations

B) Балансировка нагрузки

C) Шифрование данных

D) Хранение данных

---

## Question 2: Cache Key


Что входит в cache key по умолчанию?

A) Только URL path

B) URL path + query strings + headers

C) URL path + все headers

D) Весь HTTP request

---

## Question 3: OAC


Для чего используется Origin Access Control?

A) Для rate limiting

B) Для шифрования трафика

C) Для ограничения доступа к S3 только через CloudFront

D) Для кэширования

---

## Question 4: CloudFront Functions vs Lambda@Edge


Какое преимущество CloudFront Functions?

A) Больше памяти

B) Быстрее и дешевле (< 1ms, $0.10/million)

C) Network доступ

D) Поддержка Python

---

## Question 5: Invalidation


Какой лучший способ обновить кэшированный контент?

A) Перезапустить distribution

B) Использовать versioned URLs (app.v2.js)

C) Ждать TTL expiry

D) Invalidation API

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | CDN кэширует контент на edge locations ближе к пользователям, снижая latency. |
| 2 | A | По умолчанию cache key = только URL path. Query strings и headers нужно добавлять явно. |
| 3 | C | OAC позволяет S3 bucket быть private, но доступным через CloudFront. |
| 4 | B | CloudFront Functions: < 1ms execution, $0.10/million. Lambda@Edge: больше возможностей, но дороже. |
| 5 | B | Versioned URLs (app.v2.js) — лучшая практика. Invalidation платный и не мгновенный. |

---
