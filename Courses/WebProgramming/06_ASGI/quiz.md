# ASGI - Quiz

Проверьте свои знания по теме "Asynchronous Server Gateway Interface".

---

## Question 1: ASGI определение

Что такое ASGI?

A) Новая версия WSGI 2.0

B) Альтернатива HTTP протоколу

C) Асинхронный интерфейс между Python веб-приложениями и серверами

D) Библиотека для работы с базами данных

---

## Question 2: Сигнатура приложения

Какая сигнатура у ASGI приложения?

A) `async def app(scope, receive, send)`

B) `def app(request) -> response`

C) `def app(environ, start_response)`

D) `async def app(request, response)`

---

## Question 3: scope

Что содержит аргумент `scope` в ASGI?

A) Функции для отправки ответа

B) Информацию о соединении (тип, путь, заголовки)

C) Логи сервера

D) Тело запроса

---

## Question 4: Типы соединений

Какие типы соединений поддерживает ASGI?

A) HTTP, FTP, SMTP

B) HTTP, WebSocket, lifespan

C) Только HTTP

D) Только WebSocket

---

## Question 5: receive

Для чего используется `receive` в ASGI?

A) Для настройки сервера

B) Для получения событий от клиента (тело запроса, сообщения)

C) Для логирования

D) Для отправки ответа клиенту

---

## Question 6: send

Что делает функция `send` в ASGI?

A) Валидирует данные

B) Закрывает соединение

C) Получает данные от клиента

D) Отправляет события клиенту (статус, заголовки, тело)

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

A) Быстрый ASGI сервер на базе uvloop

B) База данных

C) Python фреймворк

D) WSGI сервер

---

## Question 9: FastAPI

На чём основан FastAPI?

A) На Tornado

B) На Django и WSGI

C) На Starlette и Pydantic (ASGI)

D) На Flask

---

## Question 10: Streaming

Как реализовать streaming response в ASGI?

A) Отправлять несколько http.response.body с more_body=True

B) Использовать специальный streaming протокол

C) Использовать WebSocket

D) Streaming не поддерживается в ASGI

---

## Question 11: lifespan

Для чего используется lifespan scope?

A) Для кэширования

B) Для событий startup/shutdown приложения

C) Для WebSocket

D) Для HTTP запросов

---

## Question 12: WSGI vs ASGI

Когда лучше использовать ASGI вместо WSGI?

A) Для CPU-bound задач

B) Для простых синхронных приложений

C) Когда нужны WebSocket, streaming, высокая конкурентность

D) Для legacy приложений

---

## Question 13: http.response.start

Что должно содержать событие http.response.start?

A) Статус и заголовки

B) Только тело ответа

C) URL редиректа

D) Только HTTP статус

---

## Question 14: Starlette

Что такое Starlette?

A) Библиотека для работы с БД

B) ASGI сервер

C) Легковесный ASGI веб-фреймворк

D) Средство тестирования

---

## Question 15: Middleware в ASGI

Как работает middleware в ASGI?

A) Оборачивает app и модифицирует scope/receive/send

B) Через наследование классов

C) Как декоратор функции

D) Через конфигурационный файл

---

## Question 16: http.request

Какой тип события содержит тело HTTP запроса?

A) http.body

B) http.request

C) http.request.body

D) request.body

---

## Question 17: scope['type']

Какие значения может принимать scope['type']?

A) http, websocket, lifespan

B) request, response

C) GET, POST, PUT

D) sync, async

---

## Question 18: more_body

Что означает more_body=False в http.response.body?

A) Это последний chunk тела ответа

B) Тело пустое

C) Ошибка в теле

D) Сжатие тела

---

## Question 19: Hypercorn

Что такое Hypercorn?

A) ASGI сервер с поддержкой HTTP/2

B) База данных

C) Фреймворк для тестирования

D) Форк Gunicorn для Python 2

---

## Question 20: websocket.receive

Какое событие получает ASGI приложение при входящем WebSocket сообщении?

A) socket.message

B) ws.message

C) websocket.receive

D) http.websocket.data

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | ASGI = Asynchronous Server Gateway Interface, async наследник WSGI |
| 2 | A | ASGI app: async callable с аргументами scope, receive, send |
| 3 | B | scope содержит type, path, method, headers и др. информацию о соединении |
| 4 | B | ASGI поддерживает HTTP, WebSocket и lifespan (startup/shutdown события) |
| 5 | B | receive — async callable для получения событий (тело запроса, WS сообщения) |
| 6 | D | send — async callable для отправки событий клиенту |
| 7 | B | HTTP ответ: сначала http.response.start (статус, заголовки), затем http.response.body |
| 8 | A | Uvicorn — быстрый ASGI сервер, использует uvloop и httptools |
| 9 | C | FastAPI построен на Starlette (ASGI) для HTTP и Pydantic для валидации |
| 10 | A | Streaming: отправляем http.response.body с more_body=True, последний с False |
| 11 | B | lifespan scope для startup (инициализация) и shutdown (очистка) событий |
| 12 | C | ASGI нужен для WebSocket, async I/O, streaming, высокой конкурентности |
| 13 | A | http.response.start содержит status (int) и headers (list of tuples) |
| 14 | C | Starlette — легковесный ASGI фреймворк, основа для FastAPI |
| 15 | A | ASGI middleware оборачивает приложение и может модифицировать scope/events |
| 16 | B | http.request содержит body (тело запроса) и more_body флаг |
| 17 | A | scope['type'] может быть 'http', 'websocket' или 'lifespan' |
| 18 | A | more_body=False означает, что это последняя часть тела ответа |
| 19 | A | Hypercorn — ASGI сервер с поддержкой HTTP/2 и HTTP/3 |
| 20 | C | websocket.receive — событие с входящим WebSocket сообщением |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете ASGI. Переходите к WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с FastAPI. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о структуре ASGI приложений. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите ASGI приложение с нуля для практики. |

---

