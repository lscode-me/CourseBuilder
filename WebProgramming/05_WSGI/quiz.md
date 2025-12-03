# WSGI - Quiz

Проверьте свои знания по теме "Python Web Server Gateway Interface".

---

## Question 1: WSGI определение

Что такое WSGI?

A) Web Server General Interface

B) Web Server Gateway Interface — стандартный интерфейс между Python приложениями и веб-серверами

C) Python веб-фреймворк

D) HTTP протокол для Python

---

## Question 2: Сигнатура приложения

Какая сигнатура у WSGI приложения?

A) `def app(request) -> response`

B) `def app(environ, start_response) -> Iterable[bytes]`

C) `def app(method, path, headers) -> body`

D) `async def app(scope, receive, send)`

---

## Question 3: environ

Что содержит аргумент `environ` в WSGI приложении?

A) Только HTTP заголовки

B) Только переменные окружения системы

C) CGI-подобные переменные + WSGI-специфичные переменные

D) Только URL и метод

---

## Question 4: start_response

Что делает функция `start_response`?

A) Запускает веб-сервер

B) Устанавливает HTTP статус и заголовки ответа

C) Парсит входящий запрос

D) Логирует запрос

---

## Question 5: Возвращаемое значение

Что должно возвращать WSGI приложение?

A) Строку с HTML

B) Словарь с данными

C) Итерируемый объект с байтами

D) HTTP статус код

---

## Question 6: wsgi.input

Для чего используется `environ['wsgi.input']`?

A) Для записи ответа

B) Для чтения тела запроса (stdin)

C) Для чтения заголовков

D) Для записи логов

---

## Question 7: Middleware

Что такое WSGI middleware?

A) Веб-сервер

B) База данных

C) Обёртка над приложением, добавляющая функциональность

D) HTTP клиент

---

## Question 8: PEP

В каком PEP определён WSGI?

A) PEP 8

B) PEP 20

C) PEP 3333

D) PEP 484

---

## Question 9: Gunicorn

Что такое Gunicorn?

A) Python веб-фреймворк

B) WSGI HTTP сервер для production

C) Библиотека для тестирования

D) ORM для баз данных

---

## Question 10: Количество воркеров

Какая рекомендуемая формула для количества Gunicorn воркеров?

A) Всегда 1 воркер

B) 2 * CPU + 1 для I/O-bound задач

C) 100 воркеров

D) Количество RAM в ГБ

---

## Question 11: Flask и WSGI

Как Flask приложение связано с WSGI?

A) Flask не использует WSGI

B) Flask app — это WSGI application (callable)

C) Flask заменяет WSGI

D) Flask работает только с uWSGI

---

## Question 12: HTTP заголовки в environ

Как HTTP заголовки представлены в environ?

A) В виде списка кортежей

B) С префиксом HTTP_ (например, HTTP_USER_AGENT)

C) В отдельном словаре headers

D) Через wsgi.headers

---

## Question 13: wsgiref

Для чего используется модуль wsgiref?

A) Production веб-сервер

B) Встроенный reference WSGI сервер для разработки

C) Парсер HTTP

D) ORM

---

## Question 14: uWSGI

Чем uWSGI отличается от Gunicorn?

A) uWSGI только для Python 2

B) uWSGI более функциональный, но сложнее в настройке

C) uWSGI не поддерживает WSGI

D) uWSGI работает только на Windows

---

## Question 15: Nginx + Gunicorn

Зачем использовать Nginx перед Gunicorn?

A) Nginx не нужен

B) Для статических файлов, SSL терминации, балансировки нагрузки

C) Только для красоты

D) Gunicorn не работает без Nginx

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | WSGI = Web Server Gateway Interface, стандартизирует связь между Python веб-приложениями и серверами |
| 2 | B | WSGI app принимает environ (dict) и start_response (callable), возвращает iterable с bytes |
| 3 | C | environ содержит CGI переменные (REQUEST_METHOD, PATH_INFO) + WSGI (wsgi.input, wsgi.errors) |
| 4 | B | start_response устанавливает статус ('200 OK') и заголовки (list of tuples) |
| 5 | C | WSGI приложение возвращает iterable с bytes (например, [b'Hello']) |
| 6 | B | wsgi.input — файлоподобный объект для чтения тела запроса (POST данные) |
| 7 | C | Middleware оборачивает приложение, добавляя логирование, аутентификацию, CORS и т.д. |
| 8 | C | PEP 3333 определяет WSGI для Python 3 (PEP 333 — оригинал для Python 2) |
| 9 | B | Gunicorn (Green Unicorn) — популярный production WSGI HTTP сервер |
| 10 | B | Стандартная рекомендация: (2 × CPU cores) + 1 для I/O-bound приложений |
| 11 | B | Flask app — это WSGI callable, его можно запустить любым WSGI сервером |
| 12 | B | HTTP заголовки преобразуются: Host → HTTP_HOST, User-Agent → HTTP_USER_AGENT |
| 13 | B | wsgiref.simple_server — встроенный простой WSGI сервер для разработки и тестирования |
| 14 | B | uWSGI имеет больше возможностей (emperor mode, spooler) но сложнее в настройке |
| 15 | B | Nginx эффективно отдаёт статику, терминирует SSL, балансирует нагрузку между воркерами |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете WSGI. Переходите к ASGI. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с middleware. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о сигнатуре приложения и environ. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Напишите WSGI приложение с нуля для практики. |

---

