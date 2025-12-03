# WSGI
## Python Web Server Gateway Interface

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать основы Python (функции, классы, итераторы)
- Понимать HTTP протокол
- Знать концепции CGI/FastCGI

**Recommended prior modules:**
- [CGI](../04_CGI/) — Gateway интерфейсы
- [Python](../../Python/) — основы Python

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Понимать спецификацию WSGI
- Писать WSGI приложения с нуля
- Создавать WSGI middleware
- Использовать WSGI серверы (Gunicorn, uWSGI)
- Понимать, как работают Flask, Django и другие фреймворки

---

## 1. Введение в WSGI

### 1.1 Что такое WSGI

**WSGI (Web Server Gateway Interface)** — стандартный интерфейс между Python веб-приложениями и веб-серверами, определённый в PEP 3333.

```
┌────────────────────────────────────────────────────────────┐
│                    WSGI Ecosystem                          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Web Servers        WSGI Servers       Applications        │
│  ┌─────────┐        ┌─────────┐       ┌─────────────┐      │
│  │ Nginx   │───────►│Gunicorn │──────►│ Flask       │      │
│  │ Apache  │        │ uWSGI   │       │ Django      │      │
│  └─────────┘        │ Waitress│       │ Custom WSGI │      │
│                     │ mod_wsgi│       └─────────────┘      │
│                     └─────────┘                            │
│                          │                                 │
│                          │ WSGI interface                  │
│                          │ (PEP 3333)                      │
│                          ▼                                 │
│                    ┌───────────────────┐                   │
│                    │ def app(environ,  │                   │
│                    │    start_response)│                   │
│                    │    ...            │                   │
│                    │    return [body]  │                   │
│                    └───────────────────┘                   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 1.2 Зачем нужен WSGI

**До WSGI:**
- Каждый сервер имел свой API
- Приложение привязано к конкретному серверу
- Нет стандарта для middleware

**После WSGI:**
- Единый стандартный интерфейс
- Приложение работает с любым WSGI-сервером
- Экосистема middleware
- Портируемость

### 1.3 История

```
2003 — PEP 333: Web Server Gateway Interface v1.0
2010 — PEP 3333: WSGI для Python 3 (обновлённый)
2010s — WSGI становится стандартом для Python веб
2015+ — ASGI для асинхронных приложений
```

---

## 2. WSGI Application

### 2.1 Минимальное WSGI приложение

```python
def application(environ, start_response):
    """
    Минимальное WSGI приложение.
    
    Args:
        environ: dict с CGI-подобными переменными окружения
        start_response: callable для отправки статуса и заголовков
    
    Returns:
        Iterable с телом ответа (bytes)
    """
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
    ]
    
    start_response(status, headers)
    
    return [b'Hello, WSGI World!']
```

### 2.2 Сигнатура WSGI приложения

```python
def app(environ: dict, start_response: callable) -> Iterable[bytes]:
    """
    WSGI application interface.
    
    Parameters:
    -----------
    environ : dict
        Словарь с переменными окружения:
        - REQUEST_METHOD: HTTP метод
        - SCRIPT_NAME: начальная часть пути
        - PATH_INFO: остальная часть пути
        - QUERY_STRING: строка запроса
        - CONTENT_TYPE: тип тела запроса
        - CONTENT_LENGTH: длина тела
        - SERVER_NAME, SERVER_PORT: сервер
        - wsgi.input: файлоподобный объект с телом запроса
        - wsgi.errors: файлоподобный объект для ошибок
        
    start_response : callable
        Функция с сигнатурой:
        start_response(status: str, headers: list[tuple]) -> callable
        
    Returns:
    --------
    Iterable[bytes]
        Итерируемый объект с байтами тела ответа
    """
    pass
```

### 2.3 environ — переменные окружения

```python
def debug_app(environ, start_response):
    """Показывает все переменные окружения WSGI."""
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    
    lines = []
    
    # CGI-подобные переменные
    lines.append("=== CGI Variables ===\n")
    cgi_vars = [
        'REQUEST_METHOD', 'SCRIPT_NAME', 'PATH_INFO', 
        'QUERY_STRING', 'CONTENT_TYPE', 'CONTENT_LENGTH',
        'SERVER_NAME', 'SERVER_PORT', 'SERVER_PROTOCOL',
        'REMOTE_ADDR', 'REMOTE_HOST'
    ]
    for var in cgi_vars:
        lines.append(f"{var}: {environ.get(var, '')}\n")
    
    # HTTP заголовки (начинаются с HTTP_)
    lines.append("\n=== HTTP Headers ===\n")
    for key, value in sorted(environ.items()):
        if key.startswith('HTTP_'):
            header_name = key[5:].replace('_', '-').title()
            lines.append(f"{header_name}: {value}\n")
    
    # WSGI-специфичные переменные
    lines.append("\n=== WSGI Variables ===\n")
    wsgi_vars = [
        'wsgi.version', 'wsgi.url_scheme', 'wsgi.multithread',
        'wsgi.multiprocess', 'wsgi.run_once'
    ]
    for var in wsgi_vars:
        lines.append(f"{var}: {environ.get(var, '')}\n")
    
    return [line.encode('utf-8') for line in lines]
```

### 2.4 start_response

```python
def app(environ, start_response):
    """Демонстрация start_response."""
    
    # Обычный вызов
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('X-Custom-Header', 'value'),
    ]
    
    # start_response возвращает write() callable (устаревший способ)
    write = start_response(status, response_headers)
    
    # Можно использовать write() для немедленной отправки
    # (не рекомендуется, только для совместимости)
    # write(b'Immediate data')
    
    # Рекомендуемый способ — возврат iterable
    return [b'<html><body>Hello</body></html>']
```

### 2.5 Обработка ошибок

```python
def app_with_error_handling(environ, start_response):
    """WSGI приложение с обработкой исключений."""
    
    try:
        # exc_info для обработки ошибок после начала ответа
        exc_info = None
        
        # ... обработка запроса ...
        
        if some_error_condition:
            # Если заголовки ещё не отправлены
            start_response('500 Internal Server Error',
                          [('Content-Type', 'text/plain')],
                          exc_info)
            return [b'Internal Server Error']
        
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Success']
        
    except Exception:
        import sys
        exc_info = sys.exc_info()
        
        # Третий аргумент — exc_info для замены заголовков
        start_response('500 Internal Server Error',
                      [('Content-Type', 'text/plain')],
                      exc_info)
        
        return [b'Internal Server Error']
```

---

## 3. Практическое WSGI приложение

### 3.1 Полноценный пример

```python
#!/usr/bin/env python3
"""
wsgi_app.py — полноценное WSGI приложение.
"""

import json
from datetime import datetime
from urllib.parse import parse_qs

class WSGIApplication:
    """WSGI приложение как класс."""
    
    def __init__(self):
        self.routes = {}
        self.request_count = 0
    
    def __call__(self, environ, start_response):
        """WSGI entry point."""
        self.request_count += 1
        
        method = environ.get('REQUEST_METHOD', 'GET')
        path = environ.get('PATH_INFO', '/')
        
        # Простой роутинг
        handler = self.routes.get((method, path))
        if handler:
            return handler(environ, start_response)
        
        # Пробуем GET для любого метода
        handler = self.routes.get(('GET', path))
        if handler and method == 'HEAD':
            return handler(environ, start_response)
        
        return self.not_found(environ, start_response)
    
    def route(self, path, methods=None):
        """Декоратор для регистрации маршрутов."""
        methods = methods or ['GET']
        
        def decorator(func):
            for method in methods:
                self.routes[(method, path)] = func
            return func
        
        return decorator
    
    def not_found(self, environ, start_response):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'404 Not Found']


# Создаём приложение
app = WSGIApplication()


# --- Утилиты ---

def parse_request_body(environ):
    """Парсинг тела запроса."""
    try:
        content_length = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        content_length = 0
    
    if content_length == 0:
        return b''
    
    return environ['wsgi.input'].read(content_length)


def json_response(start_response, data, status='200 OK'):
    """Отправка JSON ответа."""
    body = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
    
    start_response(status, [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Content-Length', str(len(body))),
    ])
    
    return [body]


def html_response(start_response, body, status='200 OK'):
    """Отправка HTML ответа."""
    if isinstance(body, str):
        body = body.encode('utf-8')
    
    start_response(status, [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(body))),
    ])
    
    return [body]


# --- Маршруты ---

@app.route('/')
def index(environ, start_response):
    html = f"""<!DOCTYPE html>
<html>
<head><title>WSGI Application</title></head>
<body>
    <h1>WSGI Application</h1>
    <p>Requests handled: {app.request_count}</p>
    <ul>
        <li><a href="/info">Request Info</a></li>
        <li><a href="/api/time">API: Time</a></li>
        <li><a href="/api/echo?message=hello">API: Echo</a></li>
        <li><a href="/form">Form Example</a></li>
    </ul>
</body>
</html>"""
    return html_response(start_response, html)


@app.route('/info')
def info(environ, start_response):
    """Показать информацию о запросе."""
    info_data = {
        'method': environ.get('REQUEST_METHOD'),
        'path': environ.get('PATH_INFO'),
        'query': environ.get('QUERY_STRING'),
        'server': f"{environ.get('SERVER_NAME')}:{environ.get('SERVER_PORT')}",
        'protocol': environ.get('SERVER_PROTOCOL'),
        'remote': environ.get('REMOTE_ADDR'),
        'headers': {
            k[5:].replace('_', '-').title(): v
            for k, v in environ.items()
            if k.startswith('HTTP_')
        },
        'wsgi': {
            'version': environ.get('wsgi.version'),
            'url_scheme': environ.get('wsgi.url_scheme'),
            'multithread': environ.get('wsgi.multithread'),
            'multiprocess': environ.get('wsgi.multiprocess'),
        }
    }
    
    return json_response(start_response, info_data)


@app.route('/api/time')
def api_time(environ, start_response):
    """API: текущее время."""
    now = datetime.now()
    
    return json_response(start_response, {
        'time': now.isoformat(),
        'timestamp': now.timestamp(),
        'formatted': now.strftime('%Y-%m-%d %H:%M:%S'),
    })


@app.route('/api/echo', methods=['GET', 'POST'])
def api_echo(environ, start_response):
    """API: эхо параметров."""
    method = environ.get('REQUEST_METHOD')
    
    data = {
        'method': method,
        'query_params': parse_qs(environ.get('QUERY_STRING', '')),
    }
    
    if method == 'POST':
        body = parse_request_body(environ)
        content_type = environ.get('CONTENT_TYPE', '')
        
        if 'application/json' in content_type:
            try:
                data['json_body'] = json.loads(body.decode('utf-8'))
            except json.JSONDecodeError:
                data['raw_body'] = body.decode('utf-8', errors='replace')
        elif 'application/x-www-form-urlencoded' in content_type:
            data['form_data'] = parse_qs(body.decode('utf-8'))
        else:
            data['raw_body'] = body.decode('utf-8', errors='replace')
    
    return json_response(start_response, data)


@app.route('/form')
def form_page(environ, start_response):
    """Страница с формой."""
    html = """<!DOCTYPE html>
<html>
<head><title>Form Example</title></head>
<body>
    <h1>Form Example</h1>
    
    <h2>POST Form (URL-encoded)</h2>
    <form method="POST" action="/api/echo">
        <input type="text" name="name" placeholder="Name">
        <input type="email" name="email" placeholder="Email">
        <button type="submit">Submit</button>
    </form>
    
    <h2>POST Form (JSON)</h2>
    <form id="json-form">
        <input type="text" id="json-name" placeholder="Name">
        <input type="text" id="json-value" placeholder="Value">
        <button type="submit">Submit JSON</button>
    </form>
    
    <pre id="result"></pre>
    
    <script>
    document.getElementById('json-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('json-name').value;
        const value = document.getElementById('json-value').value;
        
        const response = await fetch('/api/echo', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name, value})
        });
        
        const data = await response.json();
        document.getElementById('result').textContent = JSON.stringify(data, null, 2);
    });
    </script>
</body>
</html>"""
    return html_response(start_response, html)


# Для запуска напрямую (без WSGI сервера)
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    
    print("Starting WSGI server on http://localhost:8080")
    server = make_server('0.0.0.0', 8080, app)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
```

---

## 4. WSGI Middleware

### 4.1 Концепция middleware

```
┌────────────────────────────────────────────────────────────┐
│                   Middleware Chain                          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Request                                                   │
│     │                                                      │
│     ▼                                                      │
│  ┌──────────────────┐                                      │
│  │ Logging MW       │ ◄─── записывает запрос               │
│  └────────┬─────────┘                                      │
│           │                                                │
│           ▼                                                │
│  ┌──────────────────┐                                      │
│  │ Auth MW          │ ◄─── проверяет авторизацию           │
│  └────────┬─────────┘                                      │
│           │                                                │
│           ▼                                                │
│  ┌──────────────────┐                                      │
│  │ CORS MW          │ ◄─── добавляет CORS заголовки        │
│  └────────┬─────────┘                                      │
│           │                                                │
│           ▼                                                │
│  ┌──────────────────┐                                      │
│  │ Application      │ ◄─── основное приложение             │
│  └────────┬─────────┘                                      │
│           │                                                │
│           ▼                                                │
│  Response                                                  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 4.2 Простой middleware

```python
class LoggingMiddleware:
    """Middleware для логирования запросов."""
    
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        import time
        
        # До обработки запроса
        start_time = time.time()
        method = environ.get('REQUEST_METHOD')
        path = environ.get('PATH_INFO')
        
        # Обёртка над start_response для захвата статуса
        captured_status = [None]
        
        def custom_start_response(status, headers, exc_info=None):
            captured_status[0] = status
            return start_response(status, headers, exc_info)
        
        # Вызов следующего приложения
        try:
            response = self.app(environ, custom_start_response)
            
            # После обработки
            duration = (time.time() - start_time) * 1000
            print(f"[{method}] {path} - {captured_status[0]} ({duration:.2f}ms)")
            
            return response
            
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            print(f"[{method}] {path} - ERROR: {e} ({duration:.2f}ms)")
            raise


# Использование
app = LoggingMiddleware(app)
```

### 4.3 Полезные middleware

```python
class CORSMiddleware:
    """Middleware для CORS заголовков."""
    
    def __init__(self, app, allowed_origins=None):
        self.app = app
        self.allowed_origins = allowed_origins or ['*']
    
    def __call__(self, environ, start_response):
        origin = environ.get('HTTP_ORIGIN', '')
        
        # Проверка preflight запроса
        if environ.get('REQUEST_METHOD') == 'OPTIONS':
            start_response('204 No Content', [
                ('Access-Control-Allow-Origin', self._get_allowed_origin(origin)),
                ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'),
                ('Access-Control-Allow-Headers', 'Content-Type, Authorization'),
                ('Access-Control-Max-Age', '86400'),
            ])
            return [b'']
        
        # Обёртка для добавления CORS заголовков к ответу
        def cors_start_response(status, headers, exc_info=None):
            cors_headers = [
                ('Access-Control-Allow-Origin', self._get_allowed_origin(origin)),
            ]
            return start_response(status, headers + cors_headers, exc_info)
        
        return self.app(environ, cors_start_response)
    
    def _get_allowed_origin(self, origin):
        if '*' in self.allowed_origins:
            return '*'
        if origin in self.allowed_origins:
            return origin
        return self.allowed_origins[0] if self.allowed_origins else ''


class GzipMiddleware:
    """Middleware для gzip сжатия."""
    
    def __init__(self, app, min_length=500):
        self.app = app
        self.min_length = min_length
    
    def __call__(self, environ, start_response):
        # Проверяем, поддерживает ли клиент gzip
        accept_encoding = environ.get('HTTP_ACCEPT_ENCODING', '')
        if 'gzip' not in accept_encoding.lower():
            return self.app(environ, start_response)
        
        # Собираем ответ
        response_body = []
        response_headers = []
        response_status = [None]
        
        def capture_start_response(status, headers, exc_info=None):
            response_status[0] = status
            response_headers.extend(headers)
            return lambda s: response_body.append(s)
        
        # Вызов приложения
        app_response = self.app(environ, capture_start_response)
        
        # Собираем тело
        body = b''.join(response_body)
        for chunk in app_response:
            body += chunk
        
        # Сжимаем, если достаточно большой
        if len(body) >= self.min_length:
            import gzip
            compressed = gzip.compress(body)
            
            # Обновляем заголовки
            headers = [(k, v) for k, v in response_headers if k.lower() != 'content-length']
            headers.append(('Content-Encoding', 'gzip'))
            headers.append(('Content-Length', str(len(compressed))))
            
            start_response(response_status[0], headers)
            return [compressed]
        
        # Возвращаем без сжатия
        start_response(response_status[0], response_headers)
        return [body]


class ErrorHandlerMiddleware:
    """Middleware для обработки ошибок."""
    
    def __init__(self, app, debug=False):
        self.app = app
        self.debug = debug
    
    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        
        except Exception as e:
            import traceback
            
            if self.debug:
                # Показываем подробности в debug режиме
                tb = traceback.format_exc()
                body = f"""<!DOCTYPE html>
<html>
<head><title>500 Internal Server Error</title></head>
<body>
    <h1>500 Internal Server Error</h1>
    <h2>{type(e).__name__}: {e}</h2>
    <pre>{tb}</pre>
</body>
</html>""".encode('utf-8')
            else:
                # Production — минимум информации
                body = b'Internal Server Error'
            
            start_response('500 Internal Server Error', [
                ('Content-Type', 'text/html' if self.debug else 'text/plain'),
                ('Content-Length', str(len(body))),
            ])
            return [body]


# Применение middleware (порядок важен!)
app = ErrorHandlerMiddleware(app, debug=True)
app = GzipMiddleware(app)
app = CORSMiddleware(app, allowed_origins=['http://localhost:3000'])
app = LoggingMiddleware(app)
```

---

## 5. WSGI Серверы

### 5.1 Обзор серверов

| Сервер | Особенности | Production |
|--------|-------------|------------|
| **wsgiref** | Встроенный, для разработки | ❌ |
| **Gunicorn** | Популярный, простой, prefork | ✅ |
| **uWSGI** | Мощный, много функций | ✅ |
| **Waitress** | Pure Python, Windows | ✅ |
| **mod_wsgi** | Apache модуль | ✅ |
| **Bjoern** | Ультра-быстрый, C | ✅ |

### 5.2 Gunicorn

**Gunicorn** (Green Unicorn) — самый популярный WSGI сервер.

```bash
# Установка
pip install gunicorn

# Базовый запуск
gunicorn wsgi_app:app

# С настройками
gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --timeout 30 \
    --access-logfile - \
    --error-logfile - \
    wsgi_app:app
```

```python
# gunicorn.conf.py — конфигурационный файл

import multiprocessing

# Сокет
bind = "0.0.0.0:8000"
# bind = "unix:/tmp/gunicorn.sock"

# Воркеры
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"  # sync, gevent, eventlet, tornado
threads = 2  # для worker_class = "gthread"

# Таймауты
timeout = 30
graceful_timeout = 30
keepalive = 2

# Перезагрузка (для разработки)
reload = False
reload_engine = "auto"

# Логирование
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Процесс
daemon = False
pidfile = None
user = None
group = None

# Хуки
def on_starting(server):
    print("Starting Gunicorn server...")

def pre_fork(server, worker):
    pass

def post_fork(server, worker):
    print(f"Worker {worker.pid} spawned")

def worker_exit(server, worker):
    print(f"Worker {worker.pid} exiting")
```

```bash
# Запуск с конфигурационным файлом
gunicorn -c gunicorn.conf.py wsgi_app:app

# Graceful restart
kill -HUP $(cat /tmp/gunicorn.pid)

# Graceful shutdown
kill -TERM $(cat /tmp/gunicorn.pid)
```

### 5.3 uWSGI

```bash
# Установка
pip install uwsgi

# Базовый запуск
uwsgi --http :8000 --wsgi-file wsgi_app.py --callable app

# Production конфигурация
uwsgi \
    --socket /tmp/uwsgi.sock \
    --chmod-socket=666 \
    --wsgi-file wsgi_app.py \
    --callable app \
    --processes 4 \
    --threads 2 \
    --master \
    --vacuum \
    --die-on-term \
    --harakiri 30
```

```ini
; uwsgi.ini — конфигурационный файл

[uwsgi]
; Сокет
socket = /tmp/uwsgi.sock
chmod-socket = 666

; Или HTTP напрямую
; http = 0.0.0.0:8000

; Приложение
wsgi-file = wsgi_app.py
callable = app
; Или module:
; module = wsgi_app:app

; Процессы и потоки
processes = 4
threads = 2
master = true

; Управление
vacuum = true
die-on-term = true
harakiri = 30

; Логирование
logto = /var/log/uwsgi/app.log
log-format = %(addr) - %(user) [%(ltime)] "%(method) %(uri) %(proto)" %(status) %(size) "%(referer)" "%(uagent)" %(msecs)ms

; Статистика
stats = /tmp/uwsgi-stats.sock
```

### 5.4 Nginx + Gunicorn

```nginx
# /etc/nginx/sites-available/app

upstream app_server {
    server unix:/tmp/gunicorn.sock fail_timeout=0;
    # Или TCP:
    # server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen 80;
    server_name example.com;
    
    # Редирект на HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    # Статические файлы
    location /static/ {
        alias /var/www/app/static/;
        expires 30d;
    }
    
    # Проксирование на Gunicorn
    location / {
        proxy_pass http://app_server;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        proxy_connect_timeout 60;
        proxy_read_timeout 60;
        proxy_send_timeout 60;
        
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 8 4k;
    }
}
```

### 5.5 systemd service

```ini
# /etc/systemd/system/gunicorn.service

[Unit]
Description=Gunicorn WSGI Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/app
Environment="PATH=/var/www/app/venv/bin"
ExecStart=/var/www/app/venv/bin/gunicorn \
    --bind unix:/tmp/gunicorn.sock \
    --workers 4 \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log \
    wsgi_app:app

ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
# Управление
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn

# Graceful reload
sudo systemctl reload gunicorn
```

---

## 6. WSGI и фреймворки

### 6.1 Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

# Flask app — это WSGI application
# app.__call__(environ, start_response)
```

```bash
# Gunicorn + Flask
gunicorn 'myapp:app'

# Для фабрики приложений
gunicorn 'myapp:create_app()'
```

### 6.2 Django

```python
# myproject/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
```

```bash
# Gunicorn + Django
gunicorn myproject.wsgi:application

# uWSGI + Django
uwsgi --module myproject.wsgi:application
```

### 6.3 Bottle

```python
from bottle import Bottle, run

app = Bottle()

@app.route('/')
def index():
    return 'Hello, Bottle!'

# Bottle app — WSGI application
# Можно запустить встроенным сервером
run(app, host='localhost', port=8080)

# Или через Gunicorn
# gunicorn 'myapp:app'
```

---

## 7. Производительность и оптимизация

### 7.1 Количество воркеров

```python
# Формула для Gunicorn
import multiprocessing

# CPU-bound задачи
workers = multiprocessing.cpu_count()

# I/O-bound задачи
workers = multiprocessing.cpu_count() * 2 + 1

# С потоками
workers = multiprocessing.cpu_count()
threads = 4  # итого: workers * threads обработчиков
```

### 7.2 Профилирование

```python
class ProfilingMiddleware:
    """Middleware для профилирования."""
    
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        import cProfile
        import pstats
        import io
        
        profiler = cProfile.Profile()
        profiler.enable()
        
        try:
            return self.app(environ, start_response)
        finally:
            profiler.disable()
            
            stream = io.StringIO()
            stats = pstats.Stats(profiler, stream=stream)
            stats.sort_stats('cumulative')
            stats.print_stats(20)
            
            print(stream.getvalue())
```

### 7.3 Мониторинг

```python
# Prometheus metrics middleware
from prometheus_client import Counter, Histogram, generate_latest

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'path', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

class MetricsMiddleware:
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        import time
        
        method = environ.get('REQUEST_METHOD')
        path = environ.get('PATH_INFO')
        start_time = time.time()
        
        captured_status = ['']
        
        def custom_start_response(status, headers, exc_info=None):
            captured_status[0] = status.split()[0]
            return start_response(status, headers, exc_info)
        
        try:
            response = self.app(environ, custom_start_response)
            return response
        finally:
            duration = time.time() - start_time
            REQUEST_COUNT.labels(method, path, captured_status[0]).inc()
            REQUEST_LATENCY.observe(duration)
```

---

## 💡 Key Takeaways

- **WSGI** — стандартный интерфейс между Python веб-приложениями и серверами
- **Application** — callable с сигнатурой `(environ, start_response) -> Iterable[bytes]`
- **Middleware** — обёртки для добавления функциональности (logging, auth, CORS)
- **Gunicorn** — рекомендуемый WSGI сервер для production
- Flask, Django, Bottle — все используют WSGI под капотом
- Формула воркеров: `2 * CPU + 1` для I/O-bound задач

---

## 🚀 Next Steps

**Related Modules:**
- [ASGI](../06_ASGI/) — Асинхронный интерфейс
- [Web Architecture](../08_Architecture/) — Архитектура приложений

**Practice Ideas:**
1. Напишите WSGI приложение с нуля
2. Создайте middleware для аутентификации
3. Настройте Nginx + Gunicorn + Flask
4. Профилируйте и оптимизируйте WSGI приложение

**Going Deeper:**
- PEP 3333 — полная спецификация WSGI
- Werkzeug — WSGI toolkit (используется Flask)
- WebOb — объекты request/response для WSGI

---

## 📚 Additional Resources

**Specifications:**
- [PEP 3333](https://peps.python.org/pep-3333/) — WSGI specification
- [PEP 333](https://peps.python.org/pep-0333/) — оригинальный WSGI

**Documentation:**
- [Gunicorn](https://docs.gunicorn.org/)
- [uWSGI](https://uwsgi-docs.readthedocs.io/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)

**Libraries:**
- [WebOb](https://webob.org/) — request/response объекты
- [Paste](https://pythonpaste.readthedocs.io/) — WSGI utilities

---

