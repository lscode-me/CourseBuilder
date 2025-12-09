# ASGI - Quiz

Проверьте свои знания по теме "Asynchronous Server Gateway Interface".

---

## Question 1: ASGI определение


Что такое ASGI?

A) Альтернатива HTTP протоколу

B) Новая версия WSGI 2.0

C) Асинхронный интерфейс между Python веб-приложениями и серверами

D) Библиотека для работы с базами данных

---

## Question 2: Сигнатура приложения


Какая сигнатура у ASGI приложения?

A) `async def app(scope, receive, send)`

B) `async def app(request, response)`

C) `def app(environ, start_response)`

D) `def app(request) -> response`

---

## Question 3: scope


Что содержит аргумент `scope` в ASGI?

A) Логи сервера

B) Информацию о соединении (тип, путь, заголовки)

C) Тело запроса

D) Функции для отправки ответа

---

## Question 4: Типы соединений


Какие типы соединений поддерживает ASGI?

A) Только WebSocket

B) Только HTTP

C) HTTP, WebSocket, lifespan

D) HTTP, FTP, SMTP

---

## Question 5: receive


Для чего используется `receive` в ASGI?

A) Для настройки сервера

B) Для отправки ответа клиенту

C) Для получения событий от клиента (тело запроса, сообщения)

D) Для логирования

---

## Question 6: send


Что делает функция `send` в ASGI?

A) Закрывает соединение

B) Отправляет события клиенту (статус, заголовки, тело)

C) Получает данные от клиента

D) Валидирует данные

---

## Question 7: HTTP ответ


Сколько событий нужно отправить для HTTP ответа?

A) Одно событие с полным ответом

B) Зависит от размера ответа

C) Три: headers, status, body

D) Минимум два: http.response.start и http.response.body

---

## Question 8: Uvicorn


Что такое Uvicorn?

A) WSGI сервер

B) База данных

C) Python фреймворк

D) Быстрый ASGI сервер на базе uvloop

---

## Question 9: FastAPI


На чём основан FastAPI?

A) На Flask

B) На Starlette и Pydantic (ASGI)

C) На Tornado

D) На Django и WSGI

---

## Question 10: Streaming


Как реализовать streaming response в ASGI?

A) Streaming не поддерживается в ASGI

B) Использовать специальный streaming протокол

C) Использовать WebSocket

D) Отправлять несколько http.response.body с more_body=True

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

A) Когда нужны WebSocket, streaming, высокая конкурентность

B) Для legacy приложений

C) Для CPU-bound задач

D) Для простых синхронных приложений

---

## Question 13: http.response.start


Что должно содержать событие http.response.start?

A) URL редиректа

B) Только HTTP статус

C) Статус и заголовки

D) Только тело ответа

---

## Question 14: Starlette


Что такое Starlette?

A) Библиотека для работы с БД

B) Легковесный ASGI веб-фреймворк

C) ASGI сервер

D) Средство тестирования

---

## Question 15: Middleware в ASGI


Как работает middleware в ASGI?

A) Через наследование классов

B) Как декоратор функции

C) Через конфигурационный файл

D) Оборачивает app и модифицирует scope/receive/send

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | ASGI = Asynchronous Server Gateway Interface, async наследник WSGI |
| 2 | A | ASGI app: async callable с аргументами scope, receive, send |
| 3 | B | scope содержит type, path, method, headers и др. информацию о соединении |
| 4 | C | ASGI поддерживает HTTP, WebSocket и lifespan (startup/shutdown события) |
| 5 | C | receive — async callable для получения событий (тело запроса, WS сообщения) |
| 6 | B | send — async callable для отправки событий клиенту |
| 7 | D | HTTP ответ: сначала http.response.start (статус, заголовки), затем http.response.body |
| 8 | D | Uvicorn — быстрый ASGI сервер, использует uvloop и httptools |
| 9 | B | FastAPI построен на Starlette (ASGI) для HTTP и Pydantic для валидации |
| 10 | D | Streaming: отправляем http.response.body с more_body=True, последний с False |
| 11 | B | lifespan scope для startup (инициализация) и shutdown (очистка) событий |
| 12 | A | ASGI нужен для WebSocket, async I/O, streaming, высокой конкурентности |
| 13 | C | http.response.start содержит status (int) и headers (list of tuples) |
| 14 | B | Starlette — легковесный ASGI фреймворк, основа для FastAPI |
| 15 | D | ASGI middleware оборачивает приложение и может модифицировать scope/events |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете ASGI. Переходите к WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с FastAPI. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о структуре ASGI приложений. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите ASGI приложение с нуля для практики. |

---

