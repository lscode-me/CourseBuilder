# HTTP протокол — Quiz

Проверьте знание HTTP протокола и работы с ним в Python.

---

## Question 1: HTTP методы

Какой HTTP метод является idempotent?

A) POST

B) GET

C) PATCH

D) Все вышеперечисленные

---

## Question 2: Версии HTTP

Какое главное преимущество HTTP/2 над HTTP/1.1?

A) Шифрование

B) Multiplexing — много запросов через одно соединение

C) Поддержка JSON

D) Cookies

---

## Question 3: HTTPS

Что такое HTTPS?

A) HTTP с сжатием

B) HTTP поверх TLS/SSL с шифрованием

C) Быстрая версия HTTP

D) HTTP для мобильных устройств

---

## Question 4: URL структура

Какая часть URL идёт после знака вопроса?

A) fragment

B) path

C) query

D) scheme

---

## Question 5: Коды ответов

К какой категории относится код ответа 404?

A) Успех (2xx)

B) Редирект (3xx)

C) Ошибка клиента (4xx)

D) Ошибка сервера (5xx)

---

## Question 6: Python requests

Как отправить JSON в POST запросе через requests?

A) `requests.post(url, data={"key": "value"})`

B) `requests.post(url, json={"key": "value"})`

C) `requests.post(url, body={"key": "value"})`

D) `requests.post(url, content={"key": "value"})`

---

---

## Answer Key

| # | Ответ | Пояснение |
|---|-------|-----------|
| 1 | B | GET, PUT, DELETE — idempotent; POST, PATCH — нет |
| 2 | B | HTTP/2 поддерживает multiplexing — много запросов в одном соединении |
| 3 | B | HTTPS = HTTP + TLS шифрование |
| 4 | C | URL: scheme://host/path?query#fragment |
| 5 | C | 4xx — ошибки клиента (404 Not Found) |
| 6 | B | `json=` автоматически сериализует и ставит Content-Type |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по HTTP |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите коды ответов |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите HTTP методы и структуру |

---

