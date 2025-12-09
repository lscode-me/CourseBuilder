# ASGI - Quiz

Проверьте свои знания по теме "Asynchronous Server Gateway Interface".

---

## Question 1: ASGI определение







Что такое ASGI?

A) Асинхронный интерфейс между Python веб-приложениями и серверами

B) Альтернатива HTTP протоколу

C) Библиотека для работы с базами данных

D) Новая версия WSGI 2.0

---

## Question 2: Сигнатура приложения







Какая сигнатура у ASGI приложения?

A) `def app(request) -> response`

B) `async def app(scope, receive, send)`

C) `async def app(request, response)`

D) `def app(environ, start_response)`

---

## Question 3: scope







Что содержит аргумент `scope` в ASGI?

A) Информацию о соединении (тип, путь, заголовки)

B) Функции для отправки ответа

C) Тело запроса

D) Логи сервера

---

## Question 4: Типы соединений







Какие типы соединений поддерживает ASGI?

A) HTTP, WebSocket, lifespan

B) Только WebSocket

C) HTTP, FTP, SMTP

D) Только HTTP

---

## Question 5: receive







Для чего используется `receive` в ASGI?

A) Для отправки ответа клиенту

B) Для настройки сервера

C) Для логирования

D) Для получения событий от клиента (тело запроса, сообщения)

---

## Question 6: send







Что делает функция `send` в ASGI?

A) Закрывает соединение

B) Получает данные от клиента

C) Отправляет события клиенту (статус, заголовки, тело)

D) Валидирует данные

---

## Question 7: HTTP ответ







Сколько событий нужно отправить для HTTP ответа?

A) Три: headers, status, body

B) Минимум два: http.response.start и http.response.body

C) Зависит от размера ответа

D) Одно событие с полным ответом

---

## Question 8: Uvicorn







Что такое Uvicorn?

A) База данных

B) Python фреймворк

C) Быстрый ASGI сервер на базе uvloop

D) WSGI сервер

---

## Question 9: FastAPI







На чём основан FastAPI?

A) На Flask

B) На Django и WSGI

C) На Starlette и Pydantic (ASGI)

D) На Tornado

---

## Question 10: Streaming







Как реализовать streaming response в ASGI?

A) Использовать WebSocket

B) Отправлять несколько http.response.body с more_body=True

C) Streaming не поддерживается в ASGI

D) Использовать специальный streaming протокол

---

## Question 11: lifespan







Для чего используется lifespan scope?

A) Для WebSocket

B) Для событий startup/shutdown приложения

C) Для HTTP запросов

D) Для кэширования

---

## Question 12: WSGI vs ASGI







Когда лучше использовать ASGI вместо WSGI?

A) Для CPU-bound задач

B) Для legacy приложений

C) Когда нужны WebSocket, streaming, высокая конкурентность

D) Для простых синхронных приложений

---

## Question 13: http.response.start







Что должно содержать событие http.response.start?

A) Только тело ответа

B) Статус и заголовки

C) URL редиректа

D) Только HTTP статус

---

## Question 14: Starlette







Что такое Starlette?

A) Средство тестирования

B) Библиотека для работы с БД

C) ASGI сервер

D) Легковесный ASGI веб-фреймворк

---

## Question 15: Middleware в ASGI







Как работает middleware в ASGI?

A) Через конфигурационный файл

B) Как декоратор функции

C) Оборачивает app и модифицирует scope/receive/send

D) Через наследование классов

---

## Question 16: http.request






Какой тип события содержит тело HTTP запроса?

A) http.request.body

B) http.body

C) http.request

D) request.body

---

## Question 17: scope['type']






Какие значения может принимать scope['type']?

A) request, response

B) GET, POST, PUT

C) sync, async

D) http, websocket, lifespan

---

## Question 18: more_body






Что означает more_body=False в http.response.body?

A) Ошибка в теле

B) Это последний chunk тела ответа

C) Сжатие тела

D) Тело пустое

---

## Question 19: Hypercorn






Что такое Hypercorn?

A) Форк Gunicorn для Python 2

B) Фреймворк для тестирования

C) База данных

D) ASGI сервер с поддержкой HTTP/2

---

## Question 20: websocket.receive






Какое событие получает ASGI приложение при входящем WebSocket сообщении?

A) websocket.receive

B) http.websocket.data

C) ws.message

D) socket.message

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | ASGI = Asynchronous Server Gateway Interface, async наследник WSGI |
| 2 | B | ASGI app: async callable с аргументами scope, receive, send |
| 3 | A | scope содержит type, path, method, headers и др. информацию о соединении |
| 4 | A | ASGI поддерживает HTTP, WebSocket и lifespan (startup/shutdown события) |
| 5 | D | receive — async callable для получения событий (тело запроса, WS сообщения) |
| 6 | C | send — async callable для отправки событий клиенту |
| 7 | B | HTTP ответ: сначала http.response.start (статус, заголовки), затем http.response.body |
| 8 | C | Uvicorn — быстрый ASGI сервер, использует uvloop и httptools |
| 9 | C | FastAPI построен на Starlette (ASGI) для HTTP и Pydantic для валидации |
| 10 | B | Streaming: отправляем http.response.body с more_body=True, последний с False |
| 11 | B | lifespan scope для startup (инициализация) и shutdown (очистка) событий |
| 12 | C | ASGI нужен для WebSocket, async I/O, streaming, высокой конкурентности |
| 13 | B | http.response.start содержит status (int) и headers (list of tuples) |
| 14 | D | Starlette — легковесный ASGI фреймворк, основа для FastAPI |
| 15 | C | ASGI middleware оборачивает приложение и может модифицировать scope/events |
| 16 | C | http.request содержит body (тело запроса) и more_body флаг |
| 17 | D | scope['type'] может быть 'http', 'websocket' или 'lifespan' |
| 18 | B | more_body=False означает, что это последняя часть тела ответа |
| 19 | D | Hypercorn — ASGI сервер с поддержкой HTTP/2 и HTTP/3 |
| 20 | A | websocket.receive — событие с входящим WebSocket сообщением |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете ASGI. Переходите к WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с FastAPI. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о структуре ASGI приложений. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите ASGI приложение с нуля для практики. |

---

