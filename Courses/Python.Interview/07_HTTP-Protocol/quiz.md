# HTTP протокол — Quiz

Проверьте знание HTTP протокола и работы с ним в Python.

---

## Question 1: HTTP методы

Какой HTTP метод является idempotent?

A) Все вышеперечисленные

B) GET

C) POST

D) PATCH

---

## Question 2: Версии HTTP

Какое главное преимущество HTTP/2 над HTTP/1.1?

A) Шифрование

B) Cookies

C) Multiplexing — много запросов через одно соединение

D) Поддержка JSON

---

## Question 3: HTTPS

Что такое HTTPS?

A) HTTP с сжатием

B) HTTP для мобильных устройств

C) Быстрая версия HTTP

D) HTTP поверх TLS/SSL с шифрованием

---

## Question 4: URL структура

Какая часть URL идёт после знака вопроса?

A) path

B) query

C) fragment

D) scheme

---

## Question 5: Коды ответов

К какой категории относится код ответа 404?

A) Успех (2xx)

B) Редирект (3xx)

C) Ошибка сервера (5xx)

D) Ошибка клиента (4xx)

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

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | GET, PUT, DELETE — idempotent; POST, PATCH — нет |
| 2 | C | HTTP/2 поддерживает multiplexing — много запросов в одном соединении |
| 3 | D | HTTPS = HTTP + TLS шифрование |
| 4 | B | URL: scheme://host/path?query#fragment |
| 5 | D | 4xx — ошибки клиента (404 Not Found) |
| 6 | B | `json=` автоматически сериализует и ставит Content-Type |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по HTTP |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите коды ответов |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите HTTP методы и структуру |

---

