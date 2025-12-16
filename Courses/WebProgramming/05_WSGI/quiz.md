# WSGI - Quiz

Проверьте свои знания по теме "Python Web Server Gateway Interface".

---

## Question 1: WSGI определение

Что такое WSGI?

A) Web Server General Interface

B) HTTP протокол для Python

C) Web Server Gateway Interface — стандартный интерфейс между Python приложениями и веб-серверами

D) Python веб-фреймворк

---

## Question 2: Сигнатура приложения

Какая сигнатура у WSGI приложения?

A) `async def app(scope, receive, send)`

B) `def app(request) -> response`

C) `def app(method, path, headers) -> body`

D) `def app(environ, start_response) -> Iterable[bytes]`

---

## Question 3: environ

Что содержит аргумент `environ` в WSGI приложении?

A) Только HTTP заголовки

B) Только переменные окружения системы

C) Только URL и метод

D) CGI-подобные переменные + WSGI-специфичные переменные

---

## Question 4: start_response

Что делает функция `start_response`?

A) Запускает веб-сервер

B) Парсит входящий запрос

C) Устанавливает HTTP статус и заголовки ответа

D) Логирует запрос

---

## Question 5: Возвращаемое значение

Что должно возвращать WSGI приложение?

A) Словарь с данными

B) Строку с HTML

C) HTTP статус код

D) Итерируемый объект с байтами

---

## Question 6: wsgi.input

Для чего используется `environ['wsgi.input']`?

A) Для чтения заголовков

B) Для записи ответа

C) Для чтения тела запроса (stdin)

D) Для записи логов

---

## Question 7: Middleware

Что такое WSGI middleware?

A) Обёртка над приложением, добавляющая функциональность

B) HTTP клиент

C) Веб-сервер

D) База данных

---

## Question 8: PEP

В каком PEP определён WSGI?

A) PEP 3333

B) PEP 20

C) PEP 8

D) PEP 484

---

## Question 9: Gunicorn

Что такое Gunicorn?

A) ORM для баз данных

B) WSGI HTTP сервер для production

C) Python веб-фреймворк

D) Библиотека для тестирования

---

## Question 10: Количество воркеров

Какая рекомендуемая формула для количества Gunicorn воркеров?

A) Количество RAM в ГБ

B) Всегда 1 воркер

C) 100 воркеров

D) 2 * CPU + 1 для I/O-bound задач

---

## Question 11: Flask и WSGI

Как Flask приложение связано с WSGI?

A) Flask заменяет WSGI

B) Flask app — это WSGI application (callable)

C) Flask не использует WSGI

D) Flask работает только с uWSGI

---

## Question 12: HTTP заголовки в environ

Как HTTP заголовки представлены в environ?

A) В отдельном словаре headers

B) Через wsgi.headers

C) В виде списка кортежей

D) С префиксом HTTP_ (например, HTTP_USER_AGENT)

---

## Question 13: wsgiref

Для чего используется модуль wsgiref?

A) Парсер HTTP

B) ORM

C) Встроенный reference WSGI сервер для разработки

D) Production веб-сервер

---

## Question 14: uWSGI

Чем uWSGI отличается от Gunicorn?

A) uWSGI только для Python 2

B) uWSGI более функциональный, но сложнее в настройке

C) uWSGI работает только на Windows

D) uWSGI не поддерживает WSGI

---

## Question 15: Nginx + Gunicorn

Зачем использовать Nginx перед Gunicorn?

A) Nginx не нужен

B) Только для красоты

C) Для статических файлов, SSL терминации, балансировки нагрузки

D) Gunicorn не работает без Nginx

---

## Question 16: REQUEST_METHOD

Как получить HTTP метод в WSGI приложении?

A) start_response.method

B) environ['HTTP_METHOD']

C) environ['REQUEST_METHOD']

D) environ['METHOD']

---

## Question 17: PATH_INFO

Что содержит environ['PATH_INFO']?

A) Полный URL запроса

B) Путь к скрипту

C) Путь запроса (часть URL до query string)

D) Query string

---

## Question 18: wsgi.errors

Для чего используется environ['wsgi.errors']?

A) Для чтения ошибок запроса

B) Для валидации данных

C) Для отправки ошибок клиенту

D) Для записи ошибок сервера (stderr)

---

## Question 19: exc_info

Для чего нужен третий аргумент start_response(status, headers, exc_info)?

A) Для логирования

B) Для закрытия соединения

C) Для передачи информации об исключении

D) Для кэширования

---

## Question 20: wsgi.url_scheme

Что содержит environ['wsgi.url_scheme']?

A) Кодировку URL

B) Схему URL (http или https)

C) Версию HTTP

D) Порт сервера

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | WSGI = Web Server Gateway Interface, стандартизирует связь между Python веб-приложениями и серверами |
| 2 | D | WSGI app принимает environ (dict) и start_response (callable), возвращает iterable с bytes |
| 3 | D | environ содержит CGI переменные (REQUEST_METHOD, PATH_INFO) + WSGI (wsgi.input, wsgi.errors) |
| 4 | C | start_response устанавливает статус ('200 OK') и заголовки (list of tuples) |
| 5 | D | WSGI приложение возвращает iterable с bytes (например, [b'Hello']) |
| 6 | C | wsgi.input — файлоподобный объект для чтения тела запроса (POST данные) |
| 7 | A | Middleware оборачивает приложение, добавляя логирование, аутентификацию, CORS и т.д. |
| 8 | A | PEP 3333 определяет WSGI для Python 3 (PEP 333 — оригинал для Python 2) |
| 9 | B | Gunicorn (Green Unicorn) — популярный production WSGI HTTP сервер |
| 10 | D | Стандартная рекомендация: (2 × CPU cores) + 1 для I/O-bound приложений |
| 11 | B | Flask app — это WSGI callable, его можно запустить любым WSGI сервером |
| 12 | D | HTTP заголовки преобразуются: Host → HTTP_HOST, User-Agent → HTTP_USER_AGENT |
| 13 | C | wsgiref.simple_server — встроенный простой WSGI сервер для разработки и тестирования |
| 14 | B | uWSGI имеет больше возможностей (emperor mode, spooler) но сложнее в настройке |
| 15 | C | Nginx эффективно отдаёт статику, терминирует SSL, балансирует нагрузку между воркерами |
| 16 | C | REQUEST_METHOD содержит HTTP метод (GET, POST и т.д.) |
| 17 | C | PATH_INFO содержит путь запроса без query string |
| 18 | D | wsgi.errors — файлоподобный объект для записи ошибок (обычно stderr) |
| 19 | C | exc_info передаёт информацию об исключении для обработки ошибок |
| 20 | B | wsgi.url_scheme содержит 'http' или 'https' |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете WSGI. Переходите к ASGI. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с middleware. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о сигнатуре приложения и environ. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите WSGI приложение с нуля для практики. |

---

