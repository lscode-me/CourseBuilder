# WSGI - Quiz

Проверьте свои знания по теме "Python Web Server Gateway Interface".

---

## Question 1: WSGI определение


Что такое WSGI?

A) Web Server Gateway Interface — стандартный интерфейс между Python приложениями и веб-серверами

B) Web Server General Interface

C) Python веб-фреймворк

D) HTTP протокол для Python

---

## Question 2: Сигнатура приложения


Какая сигнатура у WSGI приложения?

A) `def app(request) -> response`

B) `async def app(scope, receive, send)`

C) `def app(method, path, headers) -> body`

D) `def app(environ, start_response) -> Iterable[bytes]`

---

## Question 3: environ


Что содержит аргумент `environ` в WSGI приложении?

A) CGI-подобные переменные + WSGI-специфичные переменные

B) Только HTTP заголовки

C) Только URL и метод

D) Только переменные окружения системы

---

## Question 4: start_response


Что делает функция `start_response`?

A) Устанавливает HTTP статус и заголовки ответа

B) Парсит входящий запрос

C) Логирует запрос

D) Запускает веб-сервер

---

## Question 5: Возвращаемое значение


Что должно возвращать WSGI приложение?

A) Словарь с данными

B) Итерируемый объект с байтами

C) Строку с HTML

D) HTTP статус код

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

A) HTTP клиент

B) Веб-сервер

C) База данных

D) Обёртка над приложением, добавляющая функциональность

---

## Question 8: PEP


В каком PEP определён WSGI?

A) PEP 20

B) PEP 3333

C) PEP 484

D) PEP 8

---

## Question 9: Gunicorn


Что такое Gunicorn?

A) WSGI HTTP сервер для production

B) ORM для баз данных

C) Библиотека для тестирования

D) Python веб-фреймворк

---

## Question 10: Количество воркеров


Какая рекомендуемая формула для количества Gunicorn воркеров?

A) 2 * CPU + 1 для I/O-bound задач

B) Количество RAM в ГБ

C) 100 воркеров

D) Всегда 1 воркер

---

## Question 11: Flask и WSGI


Как Flask приложение связано с WSGI?

A) Flask app — это WSGI application (callable)

B) Flask работает только с uWSGI

C) Flask заменяет WSGI

D) Flask не использует WSGI

---

## Question 12: HTTP заголовки в environ


Как HTTP заголовки представлены в environ?

A) С префиксом HTTP_ (например, HTTP_USER_AGENT)

B) В виде списка кортежей

C) В отдельном словаре headers

D) Через wsgi.headers

---

## Question 13: wsgiref


Для чего используется модуль wsgiref?

A) Встроенный reference WSGI сервер для разработки

B) ORM

C) Парсер HTTP

D) Production веб-сервер

---

## Question 14: uWSGI


Чем uWSGI отличается от Gunicorn?

A) uWSGI только для Python 2

B) uWSGI работает только на Windows

C) uWSGI более функциональный, но сложнее в настройке

D) uWSGI не поддерживает WSGI

---

## Question 15: Nginx + Gunicorn


Зачем использовать Nginx перед Gunicorn?

A) Gunicorn не работает без Nginx

B) Для статических файлов, SSL терминации, балансировки нагрузки

C) Только для красоты

D) Nginx не нужен

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | WSGI = Web Server Gateway Interface, стандартизирует связь между Python веб-приложениями и серверами |
| 2 | D | WSGI app принимает environ (dict) и start_response (callable), возвращает iterable с bytes |
| 3 | A | environ содержит CGI переменные (REQUEST_METHOD, PATH_INFO) + WSGI (wsgi.input, wsgi.errors) |
| 4 | A | start_response устанавливает статус ('200 OK') и заголовки (list of tuples) |
| 5 | B | WSGI приложение возвращает iterable с bytes (например, [b'Hello']) |
| 6 | C | wsgi.input — файлоподобный объект для чтения тела запроса (POST данные) |
| 7 | D | Middleware оборачивает приложение, добавляя логирование, аутентификацию, CORS и т.д. |
| 8 | B | PEP 3333 определяет WSGI для Python 3 (PEP 333 — оригинал для Python 2) |
| 9 | A | Gunicorn (Green Unicorn) — популярный production WSGI HTTP сервер |
| 10 | A | Стандартная рекомендация: (2 × CPU cores) + 1 для I/O-bound приложений |
| 11 | A | Flask app — это WSGI callable, его можно запустить любым WSGI сервером |
| 12 | A | HTTP заголовки преобразуются: Host → HTTP_HOST, User-Agent → HTTP_USER_AGENT |
| 13 | A | wsgiref.simple_server — встроенный простой WSGI сервер для разработки и тестирования |
| 14 | C | uWSGI имеет больше возможностей (emperor mode, spooler) но сложнее в настройке |
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

