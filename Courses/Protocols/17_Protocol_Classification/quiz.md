# Классификация протоколов - Quiz

Проверьте свои знания по теме "Классификация протоколов".

---

## Question 1: Уровни протоколов

На каких уровнях существуют протоколы?

A) Только технические

B) Бытовые, социальные, организационные, технические (сетевые, программные)

C) Только программные

D) Только социальные

---

## Question 2: Текстовые vs Бинарные

В чём отличие текстовых от бинарных протоколов?

A) Нет отличий

B) Текстовые читабельны человеком (HTTP, JSON), бинарные компактны (gRPC, Protocol Buffers)

C) Текстовые только для веба

D) Бинарные только для сетей

---

## Question 3: Stateful vs Stateless

В чём отличие stateful от stateless протоколов?

A) Stateful сохраняет состояние (TCP, FTP), stateless — каждый запрос независим (HTTP, REST)

B) Stateful только для баз данных

C) Stateless только для веба

D) Нет отличий

---

## Question 4: Синхронные vs Асинхронные

В чём отличие синхронных от асинхронных протоколов?

A) Нет отличий

B) Асинхронные только для событий

C) Синхронные — запрос ждёт ответ (HTTP), асинхронные — не ждут (message queues)

D) Синхронные только для функций

---

## Question 5: Request-Response

Что такое request-response паттерн?

A) Не используется

B) Только для HTTP

C) Только для баз данных

D) Клиент отправляет запрос, сервер отправляет ответ (HTTP, RPC)

---

## Question 6: Publish-Subscribe

Что такое publish-subscribe паттерн?

A) Publishers публикуют в канал, subscribers подписываются (Kafka, RabbitMQ)

B) Только для событий

C) Прямая коммуникация

D) Не используется

---

## Question 7: Event-driven

Что такое event-driven паттерн?

A) Компоненты реагируют на события (event producers → event bus → consumers)

B) Не используется

C) Только для веба

D) Только для GUI

---

## Question 8: Симметричные vs Асимметричные

В чём отличие симметричных от асимметричных протоколов?

A) Симметричные — все участники равны (P2P), асимметричные — разные роли (клиент-сервер)

B) Асимметричные только для HTTP

C) Симметричные только для сетей

D) Нет отличий

---

## Question 9: Unicast vs Multicast vs Broadcast

В чём отличие unicast, multicast, broadcast?

A) Не используются

B) Только для сетей

C) Нет отличий

D) Unicast — 1 получатель, multicast — группа, broadcast — все

---

## Question 10: Point-to-Point vs Broadcast

В чём отличие point-to-point от broadcast?

A) Нет отличий

B) Point-to-point — сообщение одному получателю, broadcast — всем

C) Только для радио

D) Не используются

---

## Question 11: Формальные vs Неформальные

В чём отличие формальных от неформальных протоколов?

A) Нет отличий

B) Формальные только для сетей

C) Неформальные не существуют

D) Формальные задокументированы (RFC), неформальные — неявные соглашения

---

## Question 12: Explicit vs Implicit

В чём отличие explicit от implicit протоколов?

A) Implicit не существуют

B) Explicit явно заданы, implicit — неявные (например, calling convention)

C) Explicit только для API

D) Нет отличий

---

## Question 13: Application layer vs Transport layer

В чём отличие протоколов application layer от transport layer?

A) Нет отличий

B) Application только для веба

C) Transport только для TCP

D) Application — логика приложения (HTTP, FTP), transport — надёжная доставка (TCP, UDP)

---

## Question 14: Reliable vs Unreliable

В чём отличие reliable от unreliable протоколов?

A) Reliable только для HTTP

B) Unreliable не используются

C) Нет отличий

D) Reliable гарантируют доставку (TCP), unreliable — нет (UDP)

---

## Question 15: Connection-oriented vs Connectionless

В чём отличие connection-oriented от connectionless?

A) Connectionless не используются

B) Нет отличий

C) Connection-oriented устанавливают соединение (TCP), connectionless — нет (UDP)

D) Connection-oriented только для HTTP

---

## Question 16: Push vs Pull

В чём отличие push от pull?

A) Pull только для веба

B) Нет отличий

C) Push только для уведомлений

D) Push — сервер отправляет данные (notifications), pull — клиент запрашивает (HTTP GET)

---

## Question 17: Idempotent vs Non-idempotent

В чём отличие idempotent от non-idempotent?

A) Non-idempotent не существуют

B) Idempotent — множественные запросы дают тот же результат (GET, PUT), non-idempotent — нет (POST)

C) Нет отличий

D) Idempotent только для GET

---

## Question 18: Encrypted vs Plain

В чём отличие encrypted от plain протоколов?

A) Plain не используются

B) Encrypted используют шифрование (HTTPS, SSH), plain — нет (HTTP, FTP)

C) Нет отличий

D) Encrypted только для банков

---

## Question 19: Standard vs Proprietary

В чём отличие standard от proprietary протоколов?

A) Standard только для сетей

B) Нет отличий

C) Proprietary не используются

D) Standard — открытые стандарты (HTTP, TCP), proprietary — собственные (Apple AirPlay)

---

## Question 20: Зачем классифицировать протоколы

Зачем нужна классификация протоколов?

A) Только для теории

B) Только для экзаменов

C) Не нужна

D) Для понимания характеристик, выбора подходящего протокола, анализа систем

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Протоколы существуют на всех уровнях: бытовые, социальные, организационные, технические. |
| 2 | B | Текстовые читабельны (HTTP, JSON), бинарные компактны (gRPC, Protocol Buffers). |
| 3 | A | Stateful сохраняет состояние (TCP), stateless — каждый запрос независим (HTTP, REST). |
| 4 | C | Синхронные ждут ответ (HTTP), асинхронные — нет (message queues). |
| 5 | D | Request-response: клиент запрос → сервер ответ (HTTP, RPC). |
| 6 | A | Publish-subscribe: publishers публикуют, subscribers подписываются (Kafka, RabbitMQ). |
| 7 | A | Event-driven: компоненты реагируют на события. |
| 8 | A | Симметричные — все равны (P2P), асимметричные — разные роли (клиент-сервер). |
| 9 | D | Unicast — 1 получатель, multicast — группа, broadcast — все. |
| 10 | B | Point-to-point — одному, broadcast — всем. |
| 11 | D | Формальные задокументированы (RFC), неформальные — неявные соглашения. |
| 12 | B | Explicit явно заданы, implicit — неявные (calling convention). |
| 13 | D | Application — логика приложения (HTTP), transport — надёжная доставка (TCP). |
| 14 | D | Reliable гарантируют доставку (TCP), unreliable — нет (UDP). |
| 15 | C | Connection-oriented устанавливают соединение (TCP), connectionless — нет (UDP). |
| 16 | D | Push — сервер отправляет, pull — клиент запрашивает. |
| 17 | B | Idempotent — множественные запросы дают тот же результат (GET, PUT), non-idempotent — нет (POST). |
| 18 | B | Encrypted используют шифрование (HTTPS), plain — нет (HTTP). |
| 19 | D | Standard — открытые (HTTP, TCP), proprietary — собственные (Apple AirPlay). |
| 20 | D | Классификация для понимания характеристик, выбора протокола, анализа систем. |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы, в которых ошиблись. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать соответствующие разделы лекции. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---

