# ASGI - Quiz

Проверьте свои знания по теме "Asynchronous Server Gateway Interface".

---

## Question 1: ASGI определение

Что такое ASGI?

A) Альтернатива HTTP протоколу

B) Асинхронный интерфейс между Python веб-приложениями и серверами

C) Библиотека для работы с базами данных

D) Новая версия WSGI 2.0

---

## Question 2: Сигнатура приложения

Какая сигнатура у ASGI приложения?

A) `def app(environ, start_response)`

B) `async def app(scope, receive, send)`

C) `def app(request) -> response`

D) `async def app(request, response)`

---

## Question 3: scope

Что содержит аргумент `scope` в ASGI?

A) Тело запроса

B) Информацию о соединении (тип, путь, заголовки)

C) Функции для отправки ответа

D) Логи сервера

---

## Question 4: Типы соединений

Какие типы соединений поддерживает ASGI?

A) Только HTTP

B) HTTP, WebSocket, lifespan

C) Только WebSocket

D) HTTP, FTP, SMTP

---

## Question 5: receive

Для чего используется `receive` в ASGI?

A) Для отправки ответа клиенту

B) Для получения событий от клиента (тело запроса, сообщения)

C) Для логирования

D) Для настройки сервера

---

## Question 6: send

Что делает функция `send` в ASGI?

A) Получает данные от клиента

B) Отправляет события клиенту (статус, заголовки, тело)

C) Закрывает соединение

D) Валидирует данные

---

## Question 7: HTTP ответ

Сколько событий нужно отправить для HTTP ответа?

A) Одно событие с полным ответом

B) Минимум два: http.response.start и http.response.body

C) Три: headers, status, body

D) Зависит от размера ответа

---

## Question 8: Uvicorn

Что такое Uvicorn?

A) WSGI сервер

B) Быстрый ASGI сервер на базе uvloop

C) Python фреймворк

D) База данных

---

## Question 9: FastAPI

На чём основан FastAPI?

A) На Django и WSGI

B) На Starlette и Pydantic (ASGI)

C) На Flask

D) На Tornado

---

## Question 10: Streaming

Как реализовать streaming response в ASGI?

A) Использовать специальный streaming протокол

B) Отправлять несколько http.response.body с more_body=True

C) Использовать WebSocket

D) Streaming не поддерживается в ASGI

---

## Question 11: lifespan

Для чего используется lifespan scope?

A) Для HTTP запросов

B) Для событий startup/shutdown приложения

C) Для WebSocket

D) Для кэширования

---

## Question 12: WSGI vs ASGI

Когда лучше использовать ASGI вместо WSGI?

A) Для простых синхронных приложений

B) Когда нужны WebSocket, streaming, высокая конкурентность

C) Для legacy приложений

D) Для CPU-bound задач

---

## Question 13: http.response.start

Что должно содержать событие http.response.start?

A) Только тело ответа

B) Только HTTP статус

C) Статус и заголовки

D) URL редиректа

---

## Question 14: Starlette

Что такое Starlette?

A) ASGI сервер

B) Легковесный ASGI веб-фреймворк

C) Библиотека для работы с БД

D) Средство тестирования

---

## Question 15: Middleware в ASGI

Как работает middleware в ASGI?

A) Как декоратор функции

B) Оборачивает app и модифицирует scope/receive/send

C) Через конфигурационный файл

D) Через наследование классов

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | ASGI = Asynchronous Server Gateway Interface, async наследник WSGI |
| 2 | B | ASGI app: async callable с аргументами scope, receive, send |
| 3 | B | scope содержит type, path, method, headers и др. информацию о соединении |
| 4 | B | ASGI поддерживает HTTP, WebSocket и lifespan (startup/shutdown события) |
| 5 | B | receive — async callable для получения событий (тело запроса, WS сообщения) |
| 6 | B | send — async callable для отправки событий клиенту |
| 7 | B | HTTP ответ: сначала http.response.start (статус, заголовки), затем http.response.body |
| 8 | B | Uvicorn — быстрый ASGI сервер, использует uvloop и httptools |
| 9 | B | FastAPI построен на Starlette (ASGI) для HTTP и Pydantic для валидации |
| 10 | B | Streaming: отправляем http.response.body с more_body=True, последний с False |
| 11 | B | lifespan scope для startup (инициализация) и shutdown (очистка) событий |
| 12 | B | ASGI нужен для WebSocket, async I/O, streaming, высокой конкурентности |
| 13 | C | http.response.start содержит status (int) и headers (list of tuples) |
| 14 | B | Starlette — легковесный ASGI фреймворк, основа для FastAPI |
| 15 | B | ASGI middleware оборачивает приложение и может модифицировать scope/events |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете ASGI. Переходите к WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с FastAPI. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о структуре ASGI приложений. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите ASGI приложение с нуля для практики. |

---

