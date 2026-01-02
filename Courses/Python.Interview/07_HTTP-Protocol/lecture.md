# HTTP протокол

## Что нужно знать для интервью

HTTP — основа веб-разработки. Вас могут спросить про версии HTTP, методы, структуру URL, разницу между HTTP и HTTPS.

---

## 🔑 Версии HTTP

| Версия | Особенности |
|--------|-------------|
| **HTTP/1.0** | Одно соединение на запрос, базовые headers |
| **HTTP/1.1** | Keep-alive, chunked transfer, Host header |
| **HTTP/2** | Multiplexing, binary framing, header compression |
| **HTTP/3** | На основе QUIC (UDP), меньше latency |

**Ответ на интервью:**
> "HTTP/1.1 добавил persistent connections и Host header. HTTP/2 принёс multiplexing — много запросов через одно соединение. HTTP/3 использует QUIC поверх UDP для ещё меньшей задержки."

---

## 📋 HTTP методы

| Метод | Описание | Idempotent |
|-------|----------|------------|
| **GET** | Получить ресурс | ✅ Да |
| **POST** | Создать ресурс | ❌ Нет |
| **PUT** | Заменить ресурс | ✅ Да |
| **PATCH** | Частично обновить | ❌ Нет |
| **DELETE** | Удалить ресурс | ✅ Да |
| **HEAD** | Получить только headers | ✅ Да |
| **OPTIONS** | Узнать разрешённые методы | ✅ Да |

**Idempotent** — повторный вызов даёт тот же результат.

---

## 🔐 HTTPS, SSL, TLS

| Термин | Описание |
|--------|----------|
| **SSL** | Secure Sockets Layer (устаревший) |
| **TLS** | Transport Layer Security (современный) |
| **HTTPS** | HTTP поверх TLS |

**Ответ на интервью:**
> "HTTPS — это HTTP с шифрованием через TLS. TLS заменил устаревший SSL. Шифрование защищает данные от перехвата и гарантирует подлинность сервера через сертификаты."

---

## 🔗 Структура URL

```
scheme://user:password@host:port/path?query#fragment
```

| Компонент | Пример |
|-----------|--------|
| scheme | `https` |
| host | `example.com` |
| port | `443` (опционально) |
| path | `/api/users` |
| query | `?id=123&active=true` |
| fragment | `#section1` |

### Парсинг URL в Python

```python
from urllib.parse import urlparse, parse_qs

url = "https://example.com:8080/path?name=john&age=30#top"
parsed = urlparse(url)

print(parsed.scheme)    # https
print(parsed.netloc)    # example.com:8080
print(parsed.path)      # /path
print(parsed.query)     # name=john&age=30
print(parsed.fragment)  # top

# Парсинг query string

params = parse_qs(parsed.query)
print(params)  # {'name': ['john'], 'age': ['30']}
```

---

## 🐍 HTTP в Python

### requests (рекомендуется)

```python
import requests

# GET

response = requests.get("https://api.example.com/users")
print(response.status_code)  # 200
print(response.json())       # Распарсенный JSON

# POST с данными

response = requests.post(
    "https://api.example.com/users",
    json={"name": "John", "age": 30},
    headers={"Authorization": "Bearer token123"}
)

# С cookies

session = requests.Session()
session.cookies.set("session_id", "abc123")
response = session.get("https://example.com")
```

### Другие библиотеки

| Библиотека | Описание |
|------------|----------|
| `requests` | Синхронный, самый популярный |
| `httpx` | Sync + async, похож на requests |
| `aiohttp` | Асинхронный client/server |
| `urllib.request` | Стандартная библиотека |
| `http.client` | Низкоуровневая стандартная |

---

## 📨 Headers и Cookies

### Важные headers

| Header | Описание |
|--------|----------|
| `Content-Type` | Тип данных (application/json) |
| `Authorization` | Аутентификация (Bearer token) |
| `User-Agent` | Идентификация клиента |
| `Accept` | Какие типы принимает клиент |
| `Cookie` | Cookies от клиента |
| `Set-Cookie` | Установка cookie сервером |

### Cookies

**Ответ на интервью:**
> "Cookies — это данные, которые сервер отправляет клиенту через Set-Cookie header. Клиент хранит их и отправляет обратно с каждым запросом в Cookie header. Используются для сессий и аутентификации."

---

## ❓ Типичные вопросы на интервью

### Q: Разница между GET и POST?

**A:**
| GET | POST |
|-----|------|
| Параметры в URL | Параметры в body |
| Кэшируется | Не кэшируется |
| Ограничение длины URL | Нет ограничения |
| Idempotent | Не idempotent |
| Для получения данных | Для отправки данных |

### Q: Что такое REST?

**A:**
> "REST — архитектурный стиль для API. Использует HTTP методы (GET, POST, PUT, DELETE), ресурсы идентифицируются URL, stateless — сервер не хранит состояние клиента между запросами."

### Q: Коды ответов HTTP?

**A:**
| Диапазон | Значение |
|----------|----------|
| 2xx | Успех (200 OK, 201 Created) |
| 3xx | Редирект (301, 302, 304) |
| 4xx | Ошибка клиента (400, 401, 403, 404) |
| 5xx | Ошибка сервера (500, 502, 503) |

---

## 📚 Дополнительные материалы

- [MDN Web Docs: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [requests documentation](https://docs.python-requests.org/)
- [HTTP/2 Explained](https://http2-explained.haxx.se/)

---



