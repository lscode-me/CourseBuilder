# WSGI - Quiz

Проверьте свои знания по теме "Python Web Server Gateway Interface".

---

## Question 1: WSGI определение





Что такое WSGI?

A) HTTP протокол для Python

B) Python веб-фреймворк

C) Web Server General Interface

D) Web Server Gateway Interface — стандартный интерфейс между Python приложениями и веб-серверами

---

## Question 2: Сигнатура приложения





Какая сигнатура у WSGI приложения?

A) `async def app(scope, receive, send)`

B) `def app(environ, start_response) -> Iterable[bytes]`

C) `def app(method, path, headers) -> body`

D) `def app(request) -> response`

---

## Question 3: environ





Что содержит аргумент `environ` в WSGI приложении?

A) Только URL и метод

B) Только HTTP заголовки

C) Только переменные окружения системы

D) CGI-подобные переменные + WSGI-специфичные переменные

---

## Question 4: start_response





Что делает функция `start_response`?

A) Запускает веб-сервер

B) Устанавливает HTTP статус и заголовки ответа

C) Логирует запрос

D) Парсит входящий запрос

---

## Question 5: Возвращаемое значение





Что должно возвращать WSGI приложение?

A) HTTP статус код

B) Итерируемый объект с байтами

C) Строку с HTML

D) Словарь с данными

---

## Question 6: wsgi.input





Для чего используется `environ['wsgi.input']`?

A) Для записи ответа

B) Для записи логов

C) Для чтения заголовков

D) Для чтения тела запроса (stdin)

---

## Question 7: Middleware





Что такое WSGI middleware?

A) Обёртка над приложением, добавляющая функциональность

B) База данных

C) Веб-сервер

D) HTTP клиент

---

## Question 8: PEP





В каком PEP определён WSGI?

A) PEP 8

B) PEP 484

C) PEP 3333

D) PEP 20

---

## Question 9: Gunicorn





Что такое Gunicorn?

A) Python веб-фреймворк

B) WSGI HTTP сервер для production

C) ORM для баз данных

D) Библиотека для тестирования

---

## Question 10: Количество воркеров





Какая рекомендуемая формула для количества Gunicorn воркеров?

A) Всегда 1 воркер

B) 2 * CPU + 1 для I/O-bound задач

C) Количество RAM в ГБ

D) 100 воркеров

---

## Question 11: Flask и WSGI





Как Flask приложение связано с WSGI?

A) Flask работает только с uWSGI

B) Flask app — это WSGI application (callable)

C) Flask заменяет WSGI

D) Flask не использует WSGI

---

## Question 12: HTTP заголовки в environ





Как HTTP заголовки представлены в environ?

A) В отдельном словаре headers

B) С префиксом HTTP_ (например, HTTP_USER_AGENT)

C) Через wsgi.headers

D) В виде списка кортежей

---

## Question 13: wsgiref





Для чего используется модуль wsgiref?

A) Встроенный reference WSGI сервер для разработки

B) ORM

C) Production веб-сервер

D) Парсер HTTP

---

## Question 14: uWSGI





Чем uWSGI отличается от Gunicorn?

A) uWSGI более функциональный, но сложнее в настройке

B) uWSGI работает только на Windows

C) uWSGI только для Python 2

D) uWSGI не поддерживает WSGI

---

## Question 15: Nginx + Gunicorn





Зачем использовать Nginx перед Gunicorn?

A) Nginx не нужен

B) Gunicorn не работает без Nginx

C) Для статических файлов, SSL терминации, балансировки нагрузки

D) Только для красоты

---

## Question 16: REQUEST_METHOD




Как получить HTTP метод в WSGI приложении?

A) start_response.method

B) environ['METHOD']

C) environ['HTTP_METHOD']

D) environ['REQUEST_METHOD']

---

## Question 17: PATH_INFO




Что содержит environ['PATH_INFO']?

A) Путь запроса (часть URL до query string)

B) Путь к скрипту

C) Полный URL запроса

D) Query string

---

## Question 18: wsgi.errors




Для чего используется environ['wsgi.errors']?

A) Для валидации данных

B) Для отправки ошибок клиенту

C) Для чтения ошибок запроса

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

A) Схему URL (http или https)

B) Версию HTTP

C) Кодировку URL

D) Порт сервера

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | WSGI = Web Server Gateway Interface, стандартизирует связь между Python веб-приложениями и серверами |
| 2 | B | WSGI app принимает environ (dict) и start_response (callable), возвращает iterable с bytes |
| 3 | D | environ содержит CGI переменные (REQUEST_METHOD, PATH_INFO) + WSGI (wsgi.input, wsgi.errors) |
| 4 | B | start_response устанавливает статус ('200 OK') и заголовки (list of tuples) |
| 5 | B | WSGI приложение возвращает iterable с bytes (например, [b'Hello']) |
| 6 | D | wsgi.input — файлоподобный объект для чтения тела запроса (POST данные) |
| 7 | A | Middleware оборачивает приложение, добавляя логирование, аутентификацию, CORS и т.д. |
| 8 | C | PEP 3333 определяет WSGI для Python 3 (PEP 333 — оригинал для Python 2) |
| 9 | B | Gunicorn (Green Unicorn) — популярный production WSGI HTTP сервер |
| 10 | B | Стандартная рекомендация: (2 × CPU cores) + 1 для I/O-bound приложений |
| 11 | B | Flask app — это WSGI callable, его можно запустить любым WSGI сервером |
| 12 | B | HTTP заголовки преобразуются: Host → HTTP_HOST, User-Agent → HTTP_USER_AGENT |
| 13 | A | wsgiref.simple_server — встроенный простой WSGI сервер для разработки и тестирования |
| 14 | A | uWSGI имеет больше возможностей (emperor mode, spooler) но сложнее в настройке |
| 15 | C | Nginx эффективно отдаёт статику, терминирует SSL, балансирует нагрузку между воркерами |
| 16 | D | REQUEST_METHOD содержит HTTP метод (GET, POST и т.д.) |
| 17 | A | PATH_INFO содержит путь запроса без query string |
| 18 | D | wsgi.errors — файлоподобный объект для записи ошибок (обычно stderr) |
| 19 | C | exc_info передаёт информацию об исключении для обработки ошибок |
| 20 | A | wsgi.url_scheme содержит 'http' или 'https' |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете WSGI. Переходите к ASGI. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с middleware. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о сигнатуре приложения и environ. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите WSGI приложение с нуля для практики. |

---

