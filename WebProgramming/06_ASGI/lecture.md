# ASGI
## Asynchronous Server Gateway Interface

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать WSGI (предыдущий модуль)
- Знать основы asyncio в Python
- Понимать концепции async/await

**Recommended prior modules:**
- [WSGI](../05_WSGI/) — синхронный интерфейс
- [Python](../../Python/) — основы Python

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Понимать отличия ASGI от WSGI
- Писать ASGI приложения с нуля
- Использовать ASGI серверы (Uvicorn, Daphne)
- Понимать обработку WebSocket через ASGI
- Работать со Starlette и FastAPI

---

## 1. От WSGI к ASGI

### 1.1 Ограничения WSGI

**WSGI не поддерживает:**
- Асинхронные операции (async/await)
- WebSocket соединения
- HTTP/2 server push
- Long polling
- Потоковую передачу данных

```python
# WSGI — синхронный
def wsgi_app(environ, start_response):
    # Блокирующий вызов — блокирует весь воркер
    data = fetch_from_database()  # 100ms ожидания
    # Другие запросы ждут!
    
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [data.encode()]
```

### 1.2 Что такое ASGI

**ASGI (Asynchronous Server Gateway Interface)** — духовный наследник WSGI для асинхронных Python приложений.

```
┌────────────────────────────────────────────────────────────┐
│                   ASGI vs WSGI                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  WSGI                          ASGI                        │
│  ────                          ────                        │
│  Синхронный                    Асинхронный                 │
│  Только HTTP                   HTTP, WebSocket, HTTP/2     │
│  Request-Response              Event-driven                │
│  def app(environ, start)       async def app(scope, recv, send) │
│  Один запрос = один поток      Тысячи соединений в одном   │
│                                event loop                  │
│                                                            │
│  ┌────────────┐               ┌────────────────────────┐   │
│  │  Request   │               │      Connection        │   │
│  │     │      │               │   ┌───────────────┐    │   │
│  │     ▼      │               │   │ HTTP Request  │    │   │
│  │  Handler   │               │   │ WS Message    │    │   │
│  │     │      │               │   │ WS Message    │    │   │
│  │     ▼      │               │   │ WS Close      │    │   │
│  │  Response  │               │   └───────────────┘    │   │
│  └────────────┘               └────────────────────────┘   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 1.3 ASGI протокол

```python
# ASGI Application Interface
async def app(scope: dict, receive: callable, send: callable) -> None:
    """
    ASGI application.
    
    Parameters:
    -----------
    scope : dict
        Информация о соединении:
        - type: 'http', 'websocket', 'lifespan'
        - method: HTTP метод (для HTTP)
        - path: путь URL
        - headers: список кортежей (name, value)
        - query_string: bytes
        
    receive : async callable
        Получение событий от клиента
        event = await receive()
        
    send : async callable
        Отправка событий клиенту
        await send(event)
    """
    pass
```

---

## 2. ASGI Application

### 2.1 Минимальное ASGI приложение

```python
async def app(scope, receive, send):
    """Минимальное ASGI приложение."""
    
    if scope['type'] == 'http':
        # Отправляем HTTP ответ
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        
        await send({
            'type': 'http.response.body',
            'body': b'Hello, ASGI!',
        })
```

### 2.2 Структура scope

```python
async def debug_app(scope, receive, send):
    """Показывает структуру scope."""
    
    if scope['type'] != 'http':
        return
    
    # HTTP scope содержит:
    info = {
        'type': scope['type'],            # 'http'
        'asgi': scope.get('asgi'),        # {'version': '3.0'}
        'http_version': scope.get('http_version'),  # '1.1'
        'method': scope.get('method'),    # 'GET'
        'scheme': scope.get('scheme'),    # 'http' или 'https'
        'path': scope.get('path'),        # '/api/users'
        'raw_path': scope.get('raw_path'),# b'/api/users'
        'query_string': scope.get('query_string'),  # b'page=1'
        'root_path': scope.get('root_path'),  # ''
        'headers': scope.get('headers'),  # [(b'host', b'localhost'), ...]
        'server': scope.get('server'),    # ('localhost', 8000)
        'client': scope.get('client'),    # ('127.0.0.1', 54321)
    }
    
    import json
    body = json.dumps({k: str(v) for k, v in info.items()}, indent=2)
    
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [[b'content-type', b'application/json']],
    })
    await send({
        'type': 'http.response.body',
        'body': body.encode(),
    })
```

### 2.3 HTTP события

```python
async def http_app(scope, receive, send):
    """Обработка HTTP запроса с телом."""
    
    if scope['type'] != 'http':
        return
    
    # Получение тела запроса
    body = b''
    while True:
        event = await receive()
        
        if event['type'] == 'http.request':
            body += event.get('body', b'')
            
            if not event.get('more_body', False):
                break
        
        elif event['type'] == 'http.disconnect':
            return
    
    # Обработка
    method = scope['method']
    path = scope['path']
    
    response_body = f"Method: {method}\nPath: {path}\nBody: {body.decode()}"
    
    # Отправка ответа
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain; charset=utf-8'],
            [b'content-length', str(len(response_body)).encode()],
        ],
    })
    
    await send({
        'type': 'http.response.body',
        'body': response_body.encode(),
    })
```

### 2.4 Типы HTTP событий

```python
# События от клиента (receive)
http_request = {
    'type': 'http.request',
    'body': b'request body',
    'more_body': False,  # True если есть ещё данные
}

http_disconnect = {
    'type': 'http.disconnect',
}

# События для клиента (send)
http_response_start = {
    'type': 'http.response.start',
    'status': 200,
    'headers': [
        [b'content-type', b'text/html'],
    ],
}

http_response_body = {
    'type': 'http.response.body',
    'body': b'response body',
    'more_body': False,  # True для streaming
}
```

---

## 3. Полноценное ASGI приложение

### 3.1 Приложение с роутингом

```python
#!/usr/bin/env python3
"""
asgi_app.py — полноценное ASGI приложение.
"""

import json
from datetime import datetime
from urllib.parse import parse_qs


class ASGIApplication:
    """ASGI приложение с роутингом."""
    
    def __init__(self):
        self.routes = {}
        self.request_count = 0
    
    async def __call__(self, scope, receive, send):
        """ASGI entry point."""
        
        if scope['type'] == 'lifespan':
            await self.handle_lifespan(scope, receive, send)
            return
        
        if scope['type'] == 'http':
            await self.handle_http(scope, receive, send)
            return
        
        if scope['type'] == 'websocket':
            await self.handle_websocket(scope, receive, send)
            return
    
    async def handle_lifespan(self, scope, receive, send):
        """Обработка lifecycle событий."""
        while True:
            event = await receive()
            
            if event['type'] == 'lifespan.startup':
                print("Application starting up...")
                # Инициализация ресурсов (БД, кэш и т.д.)
                await send({'type': 'lifespan.startup.complete'})
            
            elif event['type'] == 'lifespan.shutdown':
                print("Application shutting down...")
                # Очистка ресурсов
                await send({'type': 'lifespan.shutdown.complete'})
                return
    
    async def handle_http(self, scope, receive, send):
        """Обработка HTTP запросов."""
        self.request_count += 1
        
        method = scope['method']
        path = scope['path']
        
        # Роутинг
        handler = self.routes.get((method, path))
        if handler:
            await handler(scope, receive, send)
            return
        
        # 404
        await self.send_json(send, {'error': 'Not Found', 'path': path}, status=404)
    
    async def handle_websocket(self, scope, receive, send):
        """Обработка WebSocket."""
        # Реализация в следующем модуле
        await send({'type': 'websocket.close', 'code': 1000})
    
    def route(self, path, methods=None):
        """Декоратор для маршрутов."""
        methods = methods or ['GET']
        
        def decorator(func):
            for method in methods:
                self.routes[(method, path)] = func
            return func
        
        return decorator
    
    # --- Утилиты ---
    
    @staticmethod
    async def get_body(receive):
        """Получить тело запроса."""
        body = b''
        while True:
            event = await receive()
            if event['type'] == 'http.request':
                body += event.get('body', b'')
                if not event.get('more_body', False):
                    break
            elif event['type'] == 'http.disconnect':
                break
        return body
    
    @staticmethod
    async def send_json(send, data, status=200):
        """Отправить JSON ответ."""
        body = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
        
        await send({
            'type': 'http.response.start',
            'status': status,
            'headers': [
                [b'content-type', b'application/json; charset=utf-8'],
                [b'content-length', str(len(body)).encode()],
            ],
        })
        
        await send({
            'type': 'http.response.body',
            'body': body,
        })
    
    @staticmethod
    async def send_html(send, html, status=200):
        """Отправить HTML ответ."""
        body = html.encode('utf-8') if isinstance(html, str) else html
        
        await send({
            'type': 'http.response.start',
            'status': status,
            'headers': [
                [b'content-type', b'text/html; charset=utf-8'],
                [b'content-length', str(len(body)).encode()],
            ],
        })
        
        await send({
            'type': 'http.response.body',
            'body': body,
        })


# Создаём приложение
app = ASGIApplication()


# --- Маршруты ---

@app.route('/')
async def index(scope, receive, send):
    html = f"""<!DOCTYPE html>
<html>
<head><title>ASGI Application</title></head>
<body>
    <h1>ASGI Application</h1>
    <p>Requests: {app.request_count}</p>
    <ul>
        <li><a href="/api/info">API Info</a></li>
        <li><a href="/api/time">API Time</a></li>
        <li><a href="/api/echo?msg=hello">API Echo</a></li>
        <li><a href="/stream">Streaming Response</a></li>
    </ul>
</body>
</html>"""
    await app.send_html(send, html)


@app.route('/api/info')
async def api_info(scope, receive, send):
    """Информация о запросе."""
    headers = {
        name.decode(): value.decode() 
        for name, value in scope.get('headers', [])
    }
    
    data = {
        'method': scope['method'],
        'path': scope['path'],
        'query_string': scope.get('query_string', b'').decode(),
        'headers': headers,
        'client': scope.get('client'),
        'server': scope.get('server'),
        'asgi': scope.get('asgi'),
    }
    
    await app.send_json(send, data)


@app.route('/api/time')
async def api_time(scope, receive, send):
    """Текущее время."""
    import asyncio
    
    # Демонстрация асинхронности
    await asyncio.sleep(0.1)  # Не блокирует другие запросы!
    
    now = datetime.now()
    await app.send_json(send, {
        'time': now.isoformat(),
        'timestamp': now.timestamp(),
    })


@app.route('/api/echo', methods=['GET', 'POST'])
async def api_echo(scope, receive, send):
    """Echo API."""
    method = scope['method']
    query = parse_qs(scope.get('query_string', b'').decode())
    
    data = {
        'method': method,
        'query_params': query,
    }
    
    if method == 'POST':
        body = await app.get_body(receive)
        content_type = ''
        for name, value in scope.get('headers', []):
            if name == b'content-type':
                content_type = value.decode()
                break
        
        if 'application/json' in content_type:
            try:
                data['json_body'] = json.loads(body.decode())
            except json.JSONDecodeError:
                data['raw_body'] = body.decode()
        else:
            data['raw_body'] = body.decode()
    
    await app.send_json(send, data)


@app.route('/stream')
async def streaming(scope, receive, send):
    """Streaming response — отправка данных частями."""
    import asyncio
    
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain; charset=utf-8'],
        ],
    })
    
    # Отправляем данные порциями
    for i in range(10):
        await send({
            'type': 'http.response.body',
            'body': f"Chunk {i}\n".encode(),
            'more_body': True,
        })
        await asyncio.sleep(0.5)  # Имитация работы
    
    # Последний чанк
    await send({
        'type': 'http.response.body',
        'body': b"Done!\n",
        'more_body': False,
    })


# Для тестирования
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

---

## 4. ASGI серверы

### 4.1 Uvicorn

**Uvicorn** — быстрый ASGI сервер на базе uvloop и httptools.

```bash
# Установка
pip install uvicorn[standard]

# Базовый запуск
uvicorn asgi_app:app

# С настройками
uvicorn asgi_app:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --loop uvloop \
    --http httptools \
    --reload  # для разработки
```

```python
# Программный запуск
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "asgi_app:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="info",
        reload=True,  # только для разработки
    )
```

### 4.2 Daphne

**Daphne** — ASGI сервер от Django Channels.

```bash
# Установка
pip install daphne

# Запуск
daphne -b 0.0.0.0 -p 8000 asgi_app:app

# С несколькими воркерами (через supervisor/systemd)
daphne -u /tmp/daphne.sock asgi_app:app
```

### 4.3 Hypercorn

**Hypercorn** — ASGI сервер с поддержкой HTTP/2 и HTTP/3.

```bash
# Установка
pip install hypercorn

# Запуск
hypercorn asgi_app:app --bind 0.0.0.0:8000

# С HTTP/2
hypercorn asgi_app:app --bind 0.0.0.0:443 \
    --certfile cert.pem --keyfile key.pem
```

### 4.4 Сравнение серверов

| Сервер | HTTP/2 | HTTP/3 | WebSocket | Производительность |
|--------|--------|--------|-----------|-------------------|
| **Uvicorn** | ✅ | ❌ | ✅ | Очень высокая |
| **Daphne** | ❌ | ❌ | ✅ | Хорошая |
| **Hypercorn** | ✅ | ✅ | ✅ | Высокая |

### 4.5 Nginx + Uvicorn

```nginx
# /etc/nginx/sites-available/app

upstream asgi_app {
    server unix:/tmp/uvicorn.sock;
}

server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /etc/ssl/cert.pem;
    ssl_certificate_key /etc/ssl/key.pem;
    
    location / {
        proxy_pass http://asgi_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        
        proxy_read_timeout 86400;
    }
    
    location /static/ {
        alias /var/www/app/static/;
    }
}
```

```bash
# Запуск Uvicorn с Unix socket
uvicorn asgi_app:app --uds /tmp/uvicorn.sock --workers 4
```

---

## 5. ASGI Middleware

### 5.1 Структура middleware

```python
class ASGIMiddleware:
    """Базовый ASGI middleware."""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        # Модификация scope перед обработкой
        # ...
        
        # Вызов следующего приложения
        await self.app(scope, receive, send)
        
        # Действия после (ограничены для HTTP)
```

### 5.2 Logging Middleware

```python
import time
import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """Middleware для логирования запросов."""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        
        start_time = time.time()
        method = scope['method']
        path = scope['path']
        
        # Захват статуса
        status_code = 0
        
        async def send_wrapper(message):
            nonlocal status_code
            if message['type'] == 'http.response.start':
                status_code = message['status']
            await send(message)
        
        try:
            await self.app(scope, receive, send_wrapper)
        finally:
            duration = (time.time() - start_time) * 1000
            logger.info(f"{method} {path} - {status_code} ({duration:.2f}ms)")


# Применение
app = LoggingMiddleware(app)
```

### 5.3 CORS Middleware

```python
class CORSMiddleware:
    """CORS middleware для ASGI."""
    
    def __init__(self, app, allow_origins=None, allow_methods=None):
        self.app = app
        self.allow_origins = allow_origins or ['*']
        self.allow_methods = allow_methods or ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    
    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        
        # Получаем Origin
        origin = ''
        for name, value in scope.get('headers', []):
            if name == b'origin':
                origin = value.decode()
                break
        
        # Preflight request
        if scope['method'] == 'OPTIONS':
            await self.send_preflight_response(send, origin)
            return
        
        # Обычный запрос — добавляем CORS заголовки
        async def send_with_cors(message):
            if message['type'] == 'http.response.start':
                headers = list(message.get('headers', []))
                headers.append([b'access-control-allow-origin', 
                               self.get_allowed_origin(origin).encode()])
                message = {**message, 'headers': headers}
            await send(message)
        
        await self.app(scope, receive, send_with_cors)
    
    async def send_preflight_response(self, send, origin):
        await send({
            'type': 'http.response.start',
            'status': 204,
            'headers': [
                [b'access-control-allow-origin', self.get_allowed_origin(origin).encode()],
                [b'access-control-allow-methods', ', '.join(self.allow_methods).encode()],
                [b'access-control-allow-headers', b'content-type, authorization'],
                [b'access-control-max-age', b'86400'],
            ],
        })
        await send({'type': 'http.response.body', 'body': b''})
    
    def get_allowed_origin(self, origin):
        if '*' in self.allow_origins:
            return '*'
        if origin in self.allow_origins:
            return origin
        return ''
```

### 5.4 Authentication Middleware

```python
class AuthMiddleware:
    """Simple JWT authentication middleware."""
    
    def __init__(self, app, exclude_paths=None):
        self.app = app
        self.exclude_paths = exclude_paths or ['/login', '/health']
    
    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        
        path = scope['path']
        
        # Пропускаем исключённые пути
        if path in self.exclude_paths:
            await self.app(scope, receive, send)
            return
        
        # Получаем Authorization header
        auth_header = None
        for name, value in scope.get('headers', []):
            if name == b'authorization':
                auth_header = value.decode()
                break
        
        if not auth_header or not auth_header.startswith('Bearer '):
            await self.send_unauthorized(send)
            return
        
        token = auth_header[7:]  # Убираем "Bearer "
        
        # Валидация токена (упрощённо)
        user = self.validate_token(token)
        if not user:
            await self.send_unauthorized(send)
            return
        
        # Добавляем user в scope
        scope['user'] = user
        await self.app(scope, receive, send)
    
    def validate_token(self, token):
        # Здесь должна быть реальная валидация JWT
        if token == 'valid-token':
            return {'id': 1, 'username': 'admin'}
        return None
    
    async def send_unauthorized(self, send):
        body = b'{"error": "Unauthorized"}'
        await send({
            'type': 'http.response.start',
            'status': 401,
            'headers': [
                [b'content-type', b'application/json'],
                [b'www-authenticate', b'Bearer'],
            ],
        })
        await send({'type': 'http.response.body', 'body': body})
```

---

## 6. Фреймворки на ASGI

### 6.1 Starlette

**Starlette** — легковесный ASGI фреймворк.

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


async def homepage(request):
    return HTMLResponse('<h1>Hello, Starlette!</h1>')


async def api_info(request):
    return JSONResponse({
        'method': request.method,
        'path': request.url.path,
        'query_params': dict(request.query_params),
    })


async def api_user(request):
    user_id = request.path_params['user_id']
    return JSONResponse({'user_id': user_id})


routes = [
    Route('/', homepage),
    Route('/api/info', api_info),
    Route('/api/users/{user_id:int}', api_user),
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*']),
]

app = Starlette(routes=routes, middleware=middleware)
```

### 6.2 FastAPI

**FastAPI** — современный фреймворк на базе Starlette и Pydantic.

```python
from fastapi import FastAPI, Query, Path, Body, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(title="My API", version="1.0.0")


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime


# Хранилище (в памяти)
items_db = {}
item_id_counter = 0


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items")
async def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    items = list(items_db.values())
    return items[skip:skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: int = Path(..., ge=1)):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    global item_id_counter
    item_id_counter += 1
    
    item_data = {
        'id': item_id_counter,
        **item.dict(),
        'created_at': datetime.now(),
    }
    items_db[item_id_counter] = item_data
    return item_data


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    items_db[item_id].update(item.dict())
    return items_db[item_id]


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items_db[item_id]


# Запуск
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

### 6.3 Django + ASGI

```python
# myproject/asgi.py

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
```

```python
# С Django Channels для WebSocket
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import myapp.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns
        )
    ),
})
```

---

## 7. WSGI vs ASGI: когда что использовать

### 7.1 Используйте WSGI когда:

- Простое синхронное приложение
- Нет WebSocket или streaming
- Legacy код на Flask/Django (без Channels)
- CPU-bound задачи

### 7.2 Используйте ASGI когда:

- Нужны WebSocket соединения
- Real-time функциональность
- Много I/O операций (БД, API)
- Streaming ответы
- HTTP/2 server push
- Высокая конкурентность

### 7.3 Сравнение производительности

```
┌────────────────────────────────────────────────────────────┐
│              I/O Bound Request Handling                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  WSGI (4 workers):                                         │
│  Request 1: ████████░░░░ (waiting for DB)                  │
│  Request 2: ████████░░░░ (waiting for DB)                  │
│  Request 3: ████████░░░░ (waiting for DB)                  │
│  Request 4: ████████░░░░ (waiting for DB)                  │
│  Request 5: ░░░░░░░░░░░░ (waiting for worker!)             │
│                                                            │
│  ASGI (1 worker, async):                                   │
│  Request 1: ██░░██                                         │
│  Request 2: ░██░░██                                        │
│  Request 3: ░░██░░██                                       │
│  Request 4: ░░░██░░██                                      │
│  Request 5: ░░░░██░░██                                     │
│  (все запросы обрабатываются параллельно!)                 │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 💡 Key Takeaways

- **ASGI** — асинхронный наследник WSGI для async/await приложений
- **Сигнатура**: `async def app(scope, receive, send)`
- **Поддерживает**: HTTP, WebSocket, HTTP/2, streaming
- **Uvicorn** — рекомендуемый ASGI сервер для production
- **FastAPI** — самый популярный фреймворк на ASGI
- ASGI позволяет обрабатывать тысячи соединений в одном event loop

---

## 🚀 Next Steps

**Related Modules:**
- [WebSockets](../07_WebSockets/) — WebSocket протокол
- [Architecture](../08_Architecture/) — Архитектура приложений

**Practice Ideas:**
1. Напишите ASGI приложение с нуля
2. Реализуйте streaming endpoint
3. Создайте middleware для rate limiting
4. Сравните производительность WSGI и ASGI с wrk

**Going Deeper:**
- ASGI Specification
- FastAPI documentation
- Starlette internals

---

## 📚 Additional Resources

**Specifications:**
- [ASGI Spec](https://asgi.readthedocs.io/)

**Documentation:**
- [Uvicorn](https://www.uvicorn.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Starlette](https://www.starlette.io/)
- [Django Channels](https://channels.readthedocs.io/)

**Articles:**
- [Intro to ASGI](https://florimond.dev/en/posts/2019/08/introduction-to-asgi-async-python-web/)

---

