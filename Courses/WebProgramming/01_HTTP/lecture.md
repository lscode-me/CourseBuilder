# HTTP Protocol
## Протокол передачи гипертекста

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы TCP/IP (порты, соединения)
- Знать основы клиент-серверной архитектуры
- Уметь работать с командной строкой Linux

**Recommended prior modules:**

- [Sockets](../../UnixProgramming/07_Sockets/) — сетевые сокеты

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру HTTP запросов и ответов
- Различать версии HTTP/1.0, HTTP/1.1, HTTP/2, HTTP/3
- Анализировать HTTP трафик с помощью инструментов
- Создавать HTTP запросы вручную через telnet/netcat
- Понимать заголовки, методы и статус-коды

---

## 1. Введение в HTTP

### 1.1 Что такое HTTP

**HTTP (HyperText Transfer Protocol)** — протокол прикладного уровня для передачи гипертекстовых документов. Изначально создан для передачи HTML, но сейчас используется для любых данных.

```
┌──────────────────────────────────────────────────────────────┐
│                    Web Architecture                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│    Client                                    Server          │
│   ┌────────┐                              ┌────────┐         │
│   │Browser │ ──── HTTP Request ─────────► │  Web   │         │
│   │  CLI   │                              │ Server │         │
│   │  App   │ ◄─── HTTP Response ───────── │        │         │
│   └────────┘                              └────────┘         │
│                                                              │
│         TCP Connection (порт 80/443)                         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

HTTP работает по модели **запрос-ответ**:

1. Клиент открывает TCP-соединение
2. Клиент отправляет запрос
3. Сервер обрабатывает и отправляет ответ
4. Соединение закрывается (или остаётся открытым в HTTP/1.1+)

### 1.2 История развития

| Версия | Год | Ключевые особенности |
|--------|-----|---------------------|
| HTTP/0.9 | 1991 | Только GET, только HTML |
| HTTP/1.0 | 1996 | Headers, статусы, Content-Type |
| HTTP/1.1 | 1997 | Keep-Alive, Host, chunked |
| HTTP/2 | 2015 | Мультиплексирование, бинарный |
| HTTP/3 | 2022 | QUIC (UDP), ещё быстрее |

### 1.3 Порты по умолчанию

- **80** — HTTP (незашифрованный)

- **443** — HTTPS (TLS/SSL)

```bash
# Проверить, что слушает на 80 порту
sudo ss -tlnp | grep :80
sudo netstat -tlnp | grep :80

# Или через lsof
sudo lsof -i :80
```

---

## 2. Структура HTTP запроса

### 2.1 Анатомия запроса

```
┌────────────────────────────────────────────────────────────┐
│ METHOD /path/to/resource?query=value HTTP/1.1              │ ← Request Line
├────────────────────────────────────────────────────────────┤
│ Host: example.com                                          │
│ User-Agent: Mozilla/5.0                                    │ ← Headers
│ Accept: text/html                                          │
│ Content-Length: 42                                         │
├────────────────────────────────────────────────────────────┤
│                                                            │ ← Empty Line (CRLF)
├────────────────────────────────────────────────────────────┤
│ {"key": "value", "another": "data"}                        │ ← Body (optional)
└────────────────────────────────────────────────────────────┘
```

**Request Line** состоит из:

- **Method** — GET, POST, PUT, DELETE и др.

- **URI** — путь к ресурсу (с query string)

- **Version** — HTTP/1.0, HTTP/1.1, HTTP/2

### 2.2 HTTP методы

| Метод | Описание | Тело запроса | Идемпотентный | Безопасный |
|-------|----------|--------------|---------------|------------|
| GET | Получить ресурс | Нет | Да | Да |
| HEAD | GET без тела ответа | Нет | Да | Да |
| POST | Создать ресурс | Да | Нет | Нет |
| PUT | Заменить ресурс | Да | Да | Нет |
| PATCH | Частично изменить | Да | Нет | Нет |
| DELETE | Удалить ресурс | Необязательно | Да | Нет |
| OPTIONS | Узнать возможности | Нет | Да | Да |
| TRACE | Диагностика | Нет | Да | Да |
| CONNECT | Туннелирование | Нет | Нет | Нет |

**Идемпотентность** — повторный запрос даёт тот же результат.
**Безопасность** — запрос не изменяет состояние сервера.

### 2.3 Практика: отправка запроса через netcat

```bash
# Простой GET запрос
echo -e "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n" | nc example.com 80

# Или через telnet (интерактивно)
telnet example.com 80
# Затем ввести:
# GET / HTTP/1.1
# Host: example.com
# Connection: close
# (пустая строка)
```

**Example: Минимальный HTTP/1.0 запрос**

```bash
# HTTP/1.0 не требует Host заголовка
printf "GET / HTTP/1.0\r\n\r\n" | nc example.com 80
```

**Output:**
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Connection: close
...

<!doctype html>
<html>
...
</html>
```

---

## 3. Структура HTTP ответа

### 3.1 Анатомия ответа

```
┌────────────────────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                                            │ ← Status Line
├────────────────────────────────────────────────────────────┤
│ Date: Mon, 23 May 2023 22:38:34 GMT                        │
│ Content-Type: text/html; charset=UTF-8                     │ ← Headers
│ Content-Length: 1256                                       │
│ Server: nginx/1.18.0                                       │
├────────────────────────────────────────────────────────────┤
│                                                            │ ← Empty Line (CRLF)
├────────────────────────────────────────────────────────────┤
│ <!DOCTYPE html>                                            │
│ <html>                                                     │ ← Body
│ ...                                                        │
│ </html>                                                    │
└────────────────────────────────────────────────────────────┘
```

### 3.2 Статус-коды

Статус-коды сгруппированы по первой цифре:

| Диапазон | Категория | Примеры |
|----------|-----------|---------|
| **1xx** | Informational | 100 Continue, 101 Switching Protocols |
| **2xx** | Success | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| **5xx** | Server Error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

**Популярные статус-коды:**

```
200 OK                    — успех
201 Created               — ресурс создан (POST)
204 No Content            — успех без тела ответа
301 Moved Permanently     — постоянный редирект
302 Found                 — временный редирект
304 Not Modified          — использовать кэш
400 Bad Request           — ошибка в запросе
401 Unauthorized          — требуется аутентификация
403 Forbidden             — доступ запрещён
404 Not Found             — ресурс не найден
405 Method Not Allowed    — метод не поддерживается
500 Internal Server Error — ошибка сервера
502 Bad Gateway           — ошибка upstream сервера
503 Service Unavailable   — сервис недоступен
504 Gateway Timeout       — таймаут от upstream
```

---

## 4. HTTP заголовки

### 4.1 Общие заголовки

```http
# Управление соединением
Connection: keep-alive
Connection: close

# Дата
Date: Tue, 15 Nov 2023 08:12:31 GMT

# Кодирование
Transfer-Encoding: chunked
Content-Encoding: gzip
```

### 4.2 Заголовки запроса

```http
# Обязателен в HTTP/1.1
Host: www.example.com

# Информация о клиенте
User-Agent: Mozilla/5.0 (X11; Linux x86_64) ...
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br

# Кэширование
If-Modified-Since: Sat, 29 Oct 2023 19:43:31 GMT
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Cache-Control: no-cache

# Аутентификация
Authorization: Basic dXNlcjpwYXNz
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Cookie: session_id=abc123

# Тело запроса
Content-Type: application/json
Content-Length: 42
```

### 4.3 Заголовки ответа

```http
# Информация о сервере
Server: nginx/1.18.0
X-Powered-By: PHP/8.1

# Контент
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Content-Disposition: attachment; filename="file.pdf"

# Кэширование
Cache-Control: max-age=3600, public
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Sat, 29 Oct 2023 19:43:31 GMT
Expires: Thu, 01 Dec 2023 16:00:00 GMT

# Cookies
Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure

# Редиректы
Location: https://www.example.com/new-page

# Безопасность
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'

# CORS
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
```

### 4.4 Content-Type и MIME типы

```http
# Текстовые
Content-Type: text/html; charset=utf-8
Content-Type: text/plain
Content-Type: text/css
Content-Type: text/javascript

# Приложения
Content-Type: application/json
Content-Type: application/xml
Content-Type: application/pdf
Content-Type: application/octet-stream

# Формы
Content-Type: application/x-www-form-urlencoded
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

# Изображения
Content-Type: image/png
Content-Type: image/jpeg
Content-Type: image/gif
Content-Type: image/svg+xml
```

---

## 5. HTTP/1.0 vs HTTP/1.1

### 5.1 Ключевые отличия

| Особенность | HTTP/1.0 | HTTP/1.1 |
|-------------|----------|----------|
| Соединение | Закрывается после запроса | Keep-Alive по умолчанию |
| Host заголовок | Опционален | **Обязателен** |
| Chunked transfer | Нет | Да |
| Pipelining | Нет | Да (но плохо работает) |
| Кэширование | Expires, Last-Modified | + ETag, Cache-Control |
| Range requests | Нет | Да |

### 5.2 Keep-Alive соединения

**HTTP/1.0:** Новое TCP соединение для каждого запроса.

```
Client          Server
  │                │
  ├── TCP SYN ────►│
  │◄── TCP ACK ────┤
  ├── GET /1 ─────►│
  │◄── Response ───┤
  ├── TCP FIN ────►│  ← соединение закрыто
  │                │
  ├── TCP SYN ────►│  ← новое соединение для /2
  │◄── TCP ACK ────┤
  ├── GET /2 ─────►│
  ...
```

**HTTP/1.1:** Повторное использование соединения.

```
Client          Server
  │                │
  ├── TCP SYN ────►│
  │◄── TCP ACK ────┤
  ├── GET /1 ─────►│
  │◄── Response ───┤
  ├── GET /2 ─────►│  ← то же соединение
  │◄── Response ───┤
  ├── GET /3 ─────►│
  │◄── Response ───┤
  ...
```

### 5.3 Chunked Transfer Encoding

Когда сервер не знает размер ответа заранее:

```http
HTTP/1.1 200 OK
Transfer-Encoding: chunked

7\r\n
Mozilla\r\n
9\r\n
Developer\r\n
7\r\n
Network\r\n
0\r\n
\r\n
```

Формат: `размер_в_hex\r\nданные\r\n`, заканчивается `0\r\n\r\n`.

### 5.4 Virtual Hosts

HTTP/1.1 требует заголовок `Host`, что позволяет размещать несколько сайтов на одном IP:

```http
GET /index.html HTTP/1.1
Host: site1.example.com
```

```http
GET /index.html HTTP/1.1
Host: site2.example.com
```

Оба запроса идут на один IP, но сервер отдаёт разный контент.

---

## 6. HTTP/2

### 6.1 Проблема HTTP/1.1: Head-of-Line Blocking

В HTTP/1.1 запросы обрабатываются последовательно в рамках одного соединения:

```
Connection 1: GET /style.css ... (waiting) ... 200 OK
              GET /script.js ... (waiting) ... (blocked!)
              GET /image.png ... (blocked!)
```

Браузеры открывают 6-8 параллельных соединений как workaround.

### 6.2 Ключевые улучшения HTTP/2

```
┌────────────────────────────────────────────────────────────┐
│                      HTTP/2 Connection                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Stream 1: GET /style.css ──────► ◄────── 200 OK           │
│  Stream 3: GET /script.js ──────► ◄────── 200 OK           │
│  Stream 5: GET /image.png ──────► ◄────── 200 OK           │
│                                                            │
│  (все потоки в одном TCP соединении, мультиплексированы)   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Особенности:**

| Особенность | Описание |
|-------------|----------|
| **Binary framing** | Бинарный формат вместо текстового |
| **Multiplexing** | Множество потоков в одном соединении |
| **Header compression** | HPACK сжатие заголовков |
| **Server Push** | Сервер отправляет ресурсы до запроса |
| **Stream priority** | Приоритизация запросов |

### 6.3 Бинарный протокол

HTTP/2 использует фреймы:

```
┌─────────────────────────────────────┐
│ Length (24 bits)                    │
├─────────────────────────────────────┤
│ Type (8 bits) │ Flags (8 bits)      │
├─────────────────────────────────────┤
│ Stream Identifier (31 bits)         │
├─────────────────────────────────────┤
│ Frame Payload (variable)            │
└─────────────────────────────────────┘
```

Типы фреймов: DATA, HEADERS, PRIORITY, RST_STREAM, SETTINGS, PUSH_PROMISE, PING, GOAWAY, WINDOW_UPDATE, CONTINUATION.

### 6.4 Проверка HTTP/2

```bash
# С помощью curl
curl -I --http2 https://www.google.com
# HTTP/2 200

# Детально
curl -v --http2 https://www.google.com 2>&1 | grep -i "http/"

# Nghttp2 — специальный клиент
nghttp -nv https://www.google.com
```

---

## 7. HTTP/3 и QUIC

### 7.1 Проблема HTTP/2: TCP Head-of-Line Blocking

Хотя HTTP/2 решил HoL blocking на уровне HTTP, TCP всё ещё блокирует:

```
TCP пакеты: [1] [2] [X] [4] [5]
                   ↑
              потерян пакет 3
              
Все данные после пакета 3 ждут ретрансмита!
(даже если они для других HTTP потоков)
```

### 7.2 QUIC — замена TCP

**QUIC (Quick UDP Internet Connections):**

- Работает поверх UDP
- Встроенное шифрование (TLS 1.3)
- Мультиплексирование без HoL blocking
- Быстрое установление соединения (0-RTT)

```
┌──────────────────────────────────────────────────────────┐
│                    Protocol Stack                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  HTTP/1.1      HTTP/2          HTTP/3                    │
│     │             │               │                      │
│     ▼             ▼               ▼                      │
│   [TCP]         [TCP]          [QUIC]                    │
│     │             │               │                      │
│     ▼             ▼               ▼                      │
│   [TLS]         [TLS]           (встроен в QUIC)         │
│     │             │               │                      │
│     ▼             ▼               ▼                      │
│   [IP]          [IP]           [UDP]                     │
│                                   │                      │
│                                   ▼                      │
│                                 [IP]                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 7.3 Преимущества HTTP/3

| Особенность | Преимущество |
|-------------|--------------|
| **0-RTT** | Мгновенное соединение при повторных визитах |
| **No TCP HoL** | Потеря пакета не блокирует другие потоки |
| **Connection migration** | Смена IP/сети без разрыва соединения |
| **Built-in TLS** | Невозможно использовать без шифрования |

---

## 8. Практические примеры

### 8.1 HTTP клиент на Python

```python
#!/usr/bin/env python3
"""Простой HTTP/1.1 клиент."""

import socket

def http_get(host: str, path: str = "/", port: int = 80) -> tuple[int, dict, str]:
    """
    Выполнить HTTP GET запрос.
    
    Returns:
        tuple: (status_code, headers_dict, body)
    """
    # Формируем запрос
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Connection: close\r\n"
        f"User-Agent: SimplePythonClient/1.0\r\n"
        f"\r\n"
    )
    
    # Отправляем
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(request.encode())
        
        # Получаем ответ
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
    
    # Парсим ответ
    response_text = response.decode('utf-8', errors='replace')
    
    # Разделяем headers и body
    header_end = response_text.find('\r\n\r\n')
    if header_end == -1:
        return 0, {}, response_text
    
    header_section = response_text[:header_end]
    body = response_text[header_end + 4:]
    
    # Парсим status line и headers
    lines = header_section.split('\r\n')
    status_line = lines[0]
    # "HTTP/1.1 200 OK" -> 200
    status_code = int(status_line.split()[1])
    
    headers = {}
    for line in lines[1:]:
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip().lower()] = value.strip()
    
    return status_code, headers, body

if __name__ == "__main__":
    status, headers, body = http_get("example.com", "/")
    
    print(f"Status: {status}")
    print(f"Headers: {headers}")
    print(f"Body length: {len(body)}")
    print(f"Body preview: {body[:200]}...")
```

**Output:**
```
Status: 200
Headers: {'content-type': 'text/html; charset=UTF-8', 'content-length': '1256', ...}
Body length: 1256
Body preview: <!doctype html>
<html>
<head>
    <title>Example Domain</title>...
```

### 8.2 HTTP сервер на Python (без фреймворков)

```python
#!/usr/bin/env python3
"""Минимальный HTTP сервер."""

import socket
from datetime import datetime

def handle_request(request: str) -> str:
    """Обработать HTTP запрос и вернуть ответ."""
    
    lines = request.split('\r\n')
    if not lines:
        return build_response(400, "Bad Request", "Invalid request")
    
    # Парсим request line: "GET /path HTTP/1.1"
    try:
        method, path, version = lines[0].split()
    except ValueError:
        return build_response(400, "Bad Request", "Invalid request line")
    
    # Простой роутинг
    if path == "/":
        body = "<html><body><h1>Welcome!</h1><p>Current time: {}</p></body></html>".format(
            datetime.now().isoformat()
        )
        return build_response(200, "OK", body)
    
    elif path == "/json":
        import json
        data = {"status": "ok", "time": datetime.now().isoformat()}
        body = json.dumps(data)
        return build_response(200, "OK", body, content_type="application/json")
    
    elif path == "/headers":
        # Вернуть полученные заголовки
        body = "<html><body><h1>Your Headers</h1><pre>{}</pre></body></html>".format(
            '\n'.join(lines[1:])
        )
        return build_response(200, "OK", body)
    
    else:
        return build_response(404, "Not Found", f"<h1>404</h1><p>Path {path} not found</p>")

def build_response(status: int, reason: str, body: str, 
                   content_type: str = "text/html") -> str:
    """Построить HTTP ответ."""
    
    headers = [
        f"HTTP/1.1 {status} {reason}",
        f"Content-Type: {content_type}; charset=utf-8",
        f"Content-Length: {len(body.encode())}",
        f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}",
        "Server: SimplePythonServer/1.0",
        "Connection: close",
        "",
        ""
    ]
    
    return '\r\n'.join(headers) + body

def run_server(host: str = "0.0.0.0", port: int = 8080):
    """Запустить HTTP сервер."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    
    print(f"Server running on http://{host}:{port}")
    
    try:
        while True:
            client, address = server.accept()
            print(f"Connection from {address}")
            
            try:
                request = client.recv(4096).decode()
                response = handle_request(request)
                client.sendall(response.encode())
            finally:
                client.close()
    
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    run_server()
```

### 8.3 Тестирование с curl

```bash
# Базовый GET
curl http://localhost:8080/

# Получить только заголовки
curl -I http://localhost:8080/

# Verbose вывод (показывает весь обмен)
curl -v http://localhost:8080/

# POST с данными
curl -X POST -d "name=John&age=30" http://localhost:8080/form

# POST с JSON
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"John"}' http://localhost:8080/api

# Следовать редиректам
curl -L http://example.com/redirect

# Записать ответ в файл
curl -o output.html http://example.com/

# Отправить cookies
curl -b "session=abc123" http://example.com/

# Показать время запроса
curl -w "Time: %{time_total}s\n" -o /dev/null -s http://example.com/
```

### 8.4 Анализ HTTP с помощью инструментов

```bash
# tcpdump — захват пакетов
sudo tcpdump -i any -A port 80

# Wireshark / tshark
sudo tshark -i any -f "port 80" -Y "http"

# ngrep — grep для сети
sudo ngrep -q -W byline port 80

# httpie — удобный HTTP клиент
http GET example.com/api
http POST example.com/api name=John
```

---

## 9. Кэширование

### 9.1 Механизмы кэширования

```
┌────────────────────────────────────────────────────────────┐
│                  HTTP Caching Flow                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Client                Cache                Server         │
│    │                     │                    │            │
│    ├── GET /resource ───►│                    │            │
│    │                     ├── GET /resource ──►│            │
│    │                     │◄── 200 OK ─────────┤            │
│    │                     │    (cached)        │            │
│    │◄── 200 OK ──────────┤                    │            │
│    │                     │                    │            │
│    ├── GET /resource ───►│                    │            │
│    │◄── 200 OK ──────────┤  (from cache)      │            │
│    │                     │                    │            │
│    │     ... время проходит ...               │            │
│    │                     │                    │            │
│    ├── GET /resource ───►│                    │            │
│    │                     ├── GET /resource ──►│            │
│    │                     │   If-None-Match    │            │
│    │                     │◄── 304 Not Mod ────┤            │
│    │◄── 200 OK ──────────┤  (from cache)      │            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 9.2 Cache-Control

```http
# Ответ сервера
Cache-Control: max-age=3600          # кэшировать 1 час
Cache-Control: no-cache              # всегда проверять свежесть
Cache-Control: no-store              # не кэшировать
Cache-Control: private               # только браузер, не прокси
Cache-Control: public                # можно кэшировать везде
Cache-Control: must-revalidate       # проверить после истечения
```

### 9.3 ETag и условные запросы

**Первый запрос:**
```http
GET /style.css HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
ETag: "abc123"
Content-Length: 1234

.body { ... }
```

**Повторный запрос (валидация):**
```http
GET /style.css HTTP/1.1
Host: example.com
If-None-Match: "abc123"

HTTP/1.1 304 Not Modified
ETag: "abc123"
```

---

## 10. Безопасность HTTP

### 10.1 HTTPS и TLS

```
┌────────────────────────────────────────────────────────────┐
│                    TLS Handshake                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Client                                    Server          │
│    │                                          │            │
│    ├── ClientHello ─────────────────────────►│             │
│    │   (supported ciphers, random)           │             │
│    │                                          │            │
│    │◄────────────────────────── ServerHello ──┤            │
│    │   (selected cipher, certificate)         │            │
│    │                                          │            │
│    ├── Key Exchange ────────────────────────►│             │
│    │   (verify cert, generate keys)          │             │
│    │                                          │            │
│    │◄─────────────────────── Finished ────────┤            │
│    │                                          │            │
│    ├═══════════ Encrypted HTTP ══════════════►│            │
│    │                                          │            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 10.2 Security Headers

```http
# Принудительно HTTPS
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Защита от XSS
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff

# Защита от clickjacking
X-Frame-Options: DENY

# Content Security Policy
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'

# Referrer Policy
Referrer-Policy: strict-origin-when-cross-origin
```

### 10.3 Проверка безопасности

```bash
# Проверить сертификат
openssl s_client -connect example.com:443 -servername example.com

# Проверить TLS версию
curl -v --tlsv1.3 https://example.com 2>&1 | grep "SSL connection"

# Nmap для проверки SSL
nmap --script ssl-enum-ciphers -p 443 example.com

# testssl.sh — комплексная проверка
./testssl.sh https://example.com
```

---

## 💡 Key Takeaways

- **HTTP** — текстовый протокол запрос-ответ поверх TCP

- **HTTP/1.1** — Keep-Alive, Host заголовок обязателен, chunked encoding

- **HTTP/2** — бинарный, мультиплексирование, сжатие заголовков

- **HTTP/3** — QUIC поверх UDP, 0-RTT, нет TCP HoL blocking

- **Статус-коды**: 2xx — успех, 3xx — редирект, 4xx — ошибка клиента, 5xx — ошибка сервера

- **Кэширование** — Cache-Control, ETag, условные запросы

---

## 🚀 Next Steps

**Related Modules:**

- [Socket Activation](../02_SocketActivation/) — обработка соединений через systemd
- [Web Servers](../03_WebServers/) — Apache, Nginx и другие

**Practice Ideas:**

1. Напишите HTTP клиент с поддержкой редиректов
2. Реализуйте сервер с базовым кэшированием
3. Добавьте поддержку chunked encoding
4. Проанализируйте HTTP/2 трафик в Wireshark

**Going Deeper:**

- HTTP/2 спецификация (RFC 7540)
- QUIC и HTTP/3 (RFC 9000, 9114)
- TLS 1.3 (RFC 8446)

---

## 📚 Additional Resources

**RFCs:**

- [RFC 7230-7235](https://tools.ietf.org/html/rfc7230) — HTTP/1.1
- [RFC 7540](https://tools.ietf.org/html/rfc7540) — HTTP/2
- [RFC 9000](https://tools.ietf.org/html/rfc9000) — QUIC
- [RFC 9114](https://tools.ietf.org/html/rfc9114) — HTTP/3

**Books:**

- "HTTP: The Definitive Guide" — O'Reilly
- "High Performance Browser Networking" — Ilya Grigorik (бесплатно онлайн)

**Tools:**

- [curl](https://curl.se/) — универсальный HTTP клиент
- [httpie](https://httpie.io/) — удобный HTTP клиент
- [Wireshark](https://www.wireshark.org/) — анализ трафика

---




