# WebSocket
## Протокол двунаправленной связи в реальном времени

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP протокол
- Знать основы ASGI
- Иметь базовые знания JavaScript

**Recommended prior modules:**

- [HTTP Protocol](../01_HTTP/) — основы HTTP
- [ASGI](../06_ASGI/) — асинхронный интерфейс

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать протокол WebSocket
- Реализовывать WebSocket серверы и клиенты
- Использовать WebSocket в ASGI приложениях
- Создавать real-time приложения (чат, уведомления)
- Понимать масштабирование WebSocket

---

## 1. Введение в WebSocket

### 1.1 Зачем нужен WebSocket

**Проблемы HTTP для real-time:**

- Request-Response модель — сервер не может инициировать отправку
- Polling — неэффективен (много запросов)
- Long polling — сложен, ограничен

```
┌────────────────────────────────────────────────────────────┐
│                 HTTP Polling vs WebSocket                  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  HTTP Polling                     WebSocket                │
│                                                            │
│  Client         Server            Client         Server    │
│    │               │                │               │      │
│    ├──► Request   │                │◄─────────────►│       │
│    │◄── Response ─┤                │ (persistent)  │       │
│    │               │                │               │      │
│    ├──► Request   │                │◄── message ───┤       │
│    │◄── Response ─┤                │               │       │
│    │               │                ├── message ───►│      │
│    ├──► Request   │                │               │       │
│    │◄── Response ─┤                │◄── message ───┤       │
│    │   (data!)    │                │               │       │
│    │               │                ├── message ───►│      │
│    ...             ...              │               │      │
│                                     │   (both ways!)│      │
│  Много накладных расходов          Эффективно     │        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 1.2 Что такое WebSocket

**WebSocket** — протокол полнодуплексной связи поверх TCP, определённый в RFC 6455.

Особенности:

- **Персистентное соединение** — один раз подключился

- **Двунаправленность** — оба могут отправлять когда угодно

- **Низкие накладные расходы** — минимальный заголовок (2-14 байт)

- **Начинается как HTTP** — совместим с прокси и файрволами

### 1.3 WebSocket Handshake

```
┌────────────────────────────────────────────────────────────┐
│                  WebSocket Handshake                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Client                                    Server          │
│    │                                          │            │
│    │  HTTP Upgrade Request                    │            │
│    ├────────────────────────────────────────►│             │
│    │  GET /chat HTTP/1.1                      │            │
│    │  Host: server.example.com                │            │
│    │  Upgrade: websocket                      │            │
│    │  Connection: Upgrade                     │            │
│    │  Sec-WebSocket-Key: dGhlIHNhbXBsZS...   │             │
│    │  Sec-WebSocket-Version: 13              │             │
│    │                                          │            │
│    │  HTTP 101 Switching Protocols           │             │
│    │◄────────────────────────────────────────┤             │
│    │  Upgrade: websocket                      │            │
│    │  Connection: Upgrade                     │            │
│    │  Sec-WebSocket-Accept: s3pPLMBiTx...    │             │
│    │                                          │            │
│    │═══════════════════════════════════════►│              │
│    │        WebSocket connection             │             │
│    │◄═══════════════════════════════════════│              │
│    │                                          │            │
└────────────────────────────────────────────────────────────┘
```

**Клиентский запрос:**
```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
Origin: http://example.com
```

**Серверный ответ:**
```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

### 1.4 Sec-WebSocket-Accept

Сервер вычисляет `Sec-WebSocket-Accept` по формуле:

```python
import base64
import hashlib

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

def compute_accept(key: str) -> str:
    """Вычислить Sec-WebSocket-Accept."""
    combined = key + GUID
    sha1 = hashlib.sha1(combined.encode()).digest()
    return base64.b64encode(sha1).decode()

# Пример
key = "dGhlIHNhbXBsZSBub25jZQ=="
accept = compute_accept(key)
print(accept)  # s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

---

## 2. WebSocket Frame Format

### 2.1 Структура фрейма

```
┌─────────────────────────────────────────────────────────────┐
│                    WebSocket Frame                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   0                   1                   2                 │
│   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 ...       │
│  +-+-+-+-+-------+-+-------------+-------------------------------+
│  |F|R|R|R| opcode|M| Payload len |    Extended payload length    │
│  |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           │
│  |N|V|V|V|       |S|             |   (if payload len==126/127)   │
│  | |1|2|3|       |K|             |                               │
│  +-+-+-+-+-------+-+-------------+-------------------------------+
│  |     Extended payload length continued, if payload len == 127  │
│  +-------------------------------+-------------------------------+
│  |                               |Masking-key, if MASK set to 1  │
│  +-------------------------------+-------------------------------+
│  | Masking-key (continued)       |          Payload Data         │
│  +-------------------------------+-------------------------------+
│  :                     Payload Data continued ...                :
│  +---------------------------------------------------------------+
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Opcode

| Opcode | Тип | Описание |
|--------|-----|----------|
| 0x0 | Continuation | Продолжение фрагментированного сообщения |
| 0x1 | Text | Текстовые данные (UTF-8) |
| 0x2 | Binary | Бинарные данные |
| 0x8 | Close | Закрытие соединения |
| 0x9 | Ping | Ping (keep-alive) |
| 0xA | Pong | Pong (ответ на ping) |

### 2.3 Маскирование

**Клиент → Сервер**: данные ДОЛЖНЫ быть замаскированы
**Сервер → Клиент**: данные НЕ ДОЛЖНЫ быть замаскированы

```python
def mask_data(data: bytes, mask_key: bytes) -> bytes:
    """Маскирование данных WebSocket."""
    masked = bytearray(len(data))
    for i, byte in enumerate(data):
        masked[i] = byte ^ mask_key[i % 4]
    return bytes(masked)

# Пример
mask_key = b'\x37\xfa\x21\x3d'
data = b'Hello'
masked = mask_data(data, mask_key)
# Демаскирование — та же операция
original = mask_data(masked, mask_key)
```

---

## 3. WebSocket в Python

### 3.1 Клиент с библиотекой websockets

```python
#!/usr/bin/env python3
"""WebSocket клиент."""

import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        # Отправить сообщение
        await websocket.send("Hello, Server!")
        print(f"Sent: Hello, Server!")
        
        # Получить ответ
        response = await websocket.recv()
        print(f"Received: {response}")
        
        # Интерактивный режим
        while True:
            message = input("Enter message (or 'quit'): ")
            if message == 'quit':
                break
            
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(client())
```

### 3.2 Сервер с библиотекой websockets

```python
#!/usr/bin/env python3
"""WebSocket сервер."""

import asyncio
import websockets
from datetime import datetime

async def handler(websocket, path):
    """Обработчик WebSocket соединения."""
    
    client_addr = websocket.remote_address
    print(f"Client connected: {client_addr}")
    
    try:
        async for message in websocket:
            print(f"Received from {client_addr}: {message}")
            
            # Echo с timestamp
            response = f"[{datetime.now().strftime('%H:%M:%S')}] Echo: {message}"
            await websocket.send(response)
    
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {client_addr}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
```

### 3.3 Broadcast сервер (чат)

```python
#!/usr/bin/env python3
"""WebSocket чат сервер с broadcast."""

import asyncio
import websockets
import json
from datetime import datetime

# Множество подключённых клиентов
connected_clients = set()

async def broadcast(message: str, sender=None):
    """Отправить сообщение всем клиентам."""
    if connected_clients:
        await asyncio.gather(
            *[client.send(message) 
              for client in connected_clients 
              if client != sender]
        )

async def handler(websocket, path):
    """Обработчик соединения."""
    
    # Добавляем клиента
    connected_clients.add(websocket)
    client_id = id(websocket)
    
    # Уведомляем о подключении
    join_msg = json.dumps({
        'type': 'system',
        'message': f'User {client_id} joined',
        'time': datetime.now().isoformat(),
    })
    await broadcast(join_msg)
    print(f"Client {client_id} connected. Total: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            # Обрабатываем сообщение
            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                data = {'message': message}
            
            # Broadcast
            chat_msg = json.dumps({
                'type': 'message',
                'user': client_id,
                'message': data.get('message', ''),
                'time': datetime.now().isoformat(),
            })
            await broadcast(chat_msg)
    
    except websockets.exceptions.ConnectionClosed:
        pass
    
    finally:
        # Удаляем клиента
        connected_clients.discard(websocket)
        
        # Уведомляем об отключении
        leave_msg = json.dumps({
            'type': 'system',
            'message': f'User {client_id} left',
            'time': datetime.now().isoformat(),
        })
        await broadcast(leave_msg)
        print(f"Client {client_id} disconnected. Total: {len(connected_clients)}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Chat server started on ws://0.0.0.0:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 4. WebSocket в ASGI

### 4.1 ASGI WebSocket события

```python
# WebSocket scope
websocket_scope = {
    'type': 'websocket',
    'asgi': {'version': '3.0'},
    'http_version': '1.1',
    'scheme': 'ws',  # или 'wss'
    'path': '/ws/chat',
    'query_string': b'room=general',
    'headers': [...],
    'server': ('localhost', 8000),
    'client': ('127.0.0.1', 54321),
}

# События от клиента (receive)
websocket_connect = {'type': 'websocket.connect'}
websocket_receive = {
    'type': 'websocket.receive',
    'text': 'Hello!',  # или 'bytes' для бинарных
}
websocket_disconnect = {'type': 'websocket.disconnect', 'code': 1000}

# События для клиента (send)
websocket_accept = {'type': 'websocket.accept'}
websocket_send = {
    'type': 'websocket.send',
    'text': 'Response',  # или 'bytes'
}
websocket_close = {'type': 'websocket.close', 'code': 1000}
```

### 4.2 ASGI WebSocket приложение

```python
#!/usr/bin/env python3
"""ASGI приложение с WebSocket."""

import json
from datetime import datetime

# Подключённые WebSocket клиенты
websocket_clients = set()

class WebSocketClient:
    """Обёртка для WebSocket соединения."""
    
    def __init__(self, scope, receive, send):
        self.scope = scope
        self.receive = receive
        self.send = send
        self.client_id = id(self)
    
    async def accept(self):
        await self.send({'type': 'websocket.accept'})
    
    async def send_text(self, text: str):
        await self.send({'type': 'websocket.send', 'text': text})
    
    async def send_json(self, data: dict):
        await self.send_text(json.dumps(data))
    
    async def close(self, code: int = 1000):
        await self.send({'type': 'websocket.close', 'code': code})
    
    async def receive_message(self):
        """Получить следующее сообщение."""
        event = await self.receive()
        
        if event['type'] == 'websocket.receive':
            return event.get('text') or event.get('bytes', b'').decode()
        elif event['type'] == 'websocket.disconnect':
            return None
        
        return None

async def broadcast(message: str, exclude=None):
    """Отправить сообщение всем клиентам."""
    for client in websocket_clients:
        if client != exclude:
            try:
                await client.send_text(message)
            except:
                pass

async def websocket_handler(scope, receive, send):
    """Обработчик WebSocket соединений."""
    
    client = WebSocketClient(scope, receive, send)
    
    # Принимаем соединение
    event = await receive()
    if event['type'] != 'websocket.connect':
        return
    
    await client.accept()
    websocket_clients.add(client)
    
    # Уведомляем о подключении
    await broadcast(json.dumps({
        'type': 'system',
        'message': f'User {client.client_id} joined',
    }))
    
    print(f"WebSocket connected: {client.client_id}")
    
    try:
        while True:
            event = await receive()
            
            if event['type'] == 'websocket.receive':
                text = event.get('text', '')
                
                # Broadcast
                await broadcast(json.dumps({
                    'type': 'message',
                    'user': client.client_id,
                    'text': text,
                    'time': datetime.now().isoformat(),
                }))
            
            elif event['type'] == 'websocket.disconnect':
                break
    
    finally:
        websocket_clients.discard(client)
        await broadcast(json.dumps({
            'type': 'system',
            'message': f'User {client.client_id} left',
        }))
        print(f"WebSocket disconnected: {client.client_id}")

async def http_handler(scope, receive, send):
    """Обработчик HTTP запросов."""
    
    path = scope['path']
    
    if path == '/':
        # Отдаём HTML страницу с чатом
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        #messages { height: 300px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; }
        .message { margin: 5px 0; }
        .system { color: #666; font-style: italic; }
        #messageInput { width: 80%; padding: 10px; }
        button { padding: 10px 20px; }
    </style>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <div id="messages"></div>
    <input type="text" id="messageInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
    
    <script>
        const ws = new WebSocket('ws://' + window.location.host + '/ws');
        const messages = document.getElementById('messages');
        const input = document.getElementById('messageInput');
        
        ws.onopen = () => {
            addMessage('Connected to server', 'system');
        };
        
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === 'system') {
                addMessage(data.message, 'system');
            } else {
                addMessage(`User ${data.user}: ${data.text}`, 'message');
            }
        };
        
        ws.onclose = () => {
            addMessage('Disconnected from server', 'system');
        };
        
        function addMessage(text, className) {
            const div = document.createElement('div');
            div.className = className;
            div.textContent = text;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }
        
        function sendMessage() {
            if (input.value) {
                ws.send(input.value);
                input.value = '';
            }
        }
        
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>'''
        
        body = html.encode()
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [[b'content-type', b'text/html']],
        })
        await send({'type': 'http.response.body', 'body': body})
    
    else:
        await send({
            'type': 'http.response.start',
            'status': 404,
            'headers': [[b'content-type', b'text/plain']],
        })
        await send({'type': 'http.response.body', 'body': b'Not Found'})

async def app(scope, receive, send):
    """Главное ASGI приложение."""
    
    if scope['type'] == 'http':
        await http_handler(scope, receive, send)
    
    elif scope['type'] == 'websocket':
        await websocket_handler(scope, receive, send)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

---

## 5. WebSocket в фреймворках

### 5.1 FastAPI

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

class ConnectionManager:
    """Менеджер WebSocket соединений."""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head><title>FastAPI WebSocket</title></head>
    <body>
        <h1>WebSocket Chat</h1>
        <div id="messages"></div>
        <input id="messageInput" type="text">
        <button onclick="sendMessage()">Send</button>
        
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = (event) => {
                const div = document.createElement('div');
                div.textContent = event.data;
                document.getElementById('messages').appendChild(div);
            };
            function sendMessage() {
                const input = document.getElementById('messageInput');
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
    </html>
    """)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user left the chat")
```

### 5.2 Django Channels

```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Покидаем группу
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        # Отправляем в группу
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    async def chat_message(self, event):
        # Отправляем клиенту
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
```

```python
# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```

---

## 6. JavaScript клиент

### 6.1 Базовый клиент

```javascript
// Создание соединения
const ws = new WebSocket('ws://localhost:8000/ws');

// События
ws.onopen = (event) => {
    console.log('Connected to server');
    ws.send('Hello, Server!');
};

ws.onmessage = (event) => {
    console.log('Received:', event.data);
    
    // Если JSON
    try {
        const data = JSON.parse(event.data);
        console.log('Parsed:', data);
    } catch (e) {
        // Не JSON
    }
};

ws.onclose = (event) => {
    console.log('Disconnected:', event.code, event.reason);
};

ws.onerror = (error) => {
    console.error('Error:', error);
};

// Отправка
ws.send('Hello!');
ws.send(JSON.stringify({type: 'message', text: 'Hello'}));

// Закрытие
ws.close(1000, 'Normal closure');
```

### 6.2 Reconnecting WebSocket

```javascript
class ReconnectingWebSocket {
    constructor(url, options = {}) {
        this.url = url;
        this.reconnectInterval = options.reconnectInterval || 1000;
        this.maxReconnectInterval = options.maxReconnectInterval || 30000;
        this.reconnectDecay = options.reconnectDecay || 1.5;
        this.maxReconnectAttempts = options.maxReconnectAttempts || null;
        
        this.reconnectAttempts = 0;
        this.currentReconnectInterval = this.reconnectInterval;
        
        this.onopen = () => {};
        this.onmessage = () => {};
        this.onclose = () => {};
        this.onerror = () => {};
        
        this.connect();
    }
    
    connect() {
        this.ws = new WebSocket(this.url);
        
        this.ws.onopen = (event) => {
            this.reconnectAttempts = 0;
            this.currentReconnectInterval = this.reconnectInterval;
            this.onopen(event);
        };
        
        this.ws.onmessage = (event) => {
            this.onmessage(event);
        };
        
        this.ws.onclose = (event) => {
            this.onclose(event);
            
            if (!event.wasClean) {
                this.reconnect();
            }
        };
        
        this.ws.onerror = (error) => {
            this.onerror(error);
        };
    }
    
    reconnect() {
        if (this.maxReconnectAttempts && 
            this.reconnectAttempts >= this.maxReconnectAttempts) {
            console.log('Max reconnect attempts reached');
            return;
        }
        
        this.reconnectAttempts++;
        
        console.log(`Reconnecting in ${this.currentReconnectInterval}ms...`);
        
        setTimeout(() => {
            this.connect();
        }, this.currentReconnectInterval);
        
        // Exponential backoff
        this.currentReconnectInterval = Math.min(
            this.currentReconnectInterval * this.reconnectDecay,
            this.maxReconnectInterval
        );
    }
    
    send(data) {
        if (this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(data);
        }
    }
    
    close() {
        this.ws.close(1000, 'Normal closure');
    }
}

// Использование
const ws = new ReconnectingWebSocket('ws://localhost:8000/ws');
ws.onmessage = (event) => console.log(event.data);
```

---

## 7. Масштабирование WebSocket

### 7.1 Проблема масштабирования

```
┌────────────────────────────────────────────────────────────┐
│              WebSocket Scaling Problem                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Load Balancer                                             │
│       │                                                    │
│       ├────────────► Server 1 ◄──── Client A               │
│       │              (clients: A, B)                       │
│       │                                                    │
│       └────────────► Server 2 ◄──── Client C               │
│                      (clients: C, D)                       │
│                                                            │
│  Проблема: Client A не может отправить сообщение Client C  │
│  (они на разных серверах!)                                 │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 7.2 Решение: Pub/Sub с Redis

```
┌────────────────────────────────────────────────────────────┐
│              WebSocket with Redis Pub/Sub                  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                        Redis                               │
│                    ┌──────────┐                            │
│                    │ Pub/Sub  │                            │
│                    └────┬─────┘                            │
│              ┌──────────┼──────────┐                       │
│              │          │          │                       │
│              ▼          ▼          ▼                       │
│         Server 1   Server 2   Server 3                     │
│         ┌──────┐   ┌──────┐   ┌──────┐                     │
│         │ A, B │   │ C, D │   │ E, F │                     │
│         └──────┘   └──────┘   └──────┘                     │
│                                                            │
│  Client A → Server 1 → Redis → All Servers → All Clients   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

```python
#!/usr/bin/env python3
"""WebSocket сервер с Redis Pub/Sub."""

import asyncio
import aioredis
import json
from fastapi import FastAPI, WebSocket
from typing import Set

app = FastAPI()
redis = None
pubsub = None
connected_websockets: Set[WebSocket] = set()

@app.on_event("startup")
async def startup():
    global redis, pubsub
    redis = await aioredis.from_url("redis://localhost")
    pubsub = redis.pubsub()
    await pubsub.subscribe("chat")
    asyncio.create_task(redis_listener())

async def redis_listener():
    """Слушает Redis и рассылает сообщения."""
    async for message in pubsub.listen():
        if message['type'] == 'message':
            data = message['data'].decode()
            # Рассылаем всем локальным клиентам
            for ws in connected_websockets.copy():
                try:
                    await ws.send_text(data)
                except:
                    connected_websockets.discard(ws)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.add(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            # Публикуем в Redis
            await redis.publish("chat", data)
    except:
        pass
    finally:
        connected_websockets.discard(websocket)
```

### 7.3 Sticky Sessions

Альтернативный подход — sticky sessions на load balancer:

```nginx
upstream websocket_servers {
    ip_hash;  # Sticky sessions по IP
    server server1:8000;
    server server2:8000;
    server server3:8000;
}

server {
    location /ws {
        proxy_pass http://websocket_servers;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## 💡 Key Takeaways

- **WebSocket** — протокол полнодуплексной связи поверх TCP

- **Handshake** — начинается как HTTP Upgrade запрос

- **Фреймы** — минимальный overhead (2-14 байт заголовка)

- **ASGI** — нативно поддерживает WebSocket

- **Масштабирование** — требует Pub/Sub (Redis) или sticky sessions

- **Ping/Pong** — для поддержания соединения

---

## 🚀 Next Steps

**Related Modules:**

- [Architecture](../08_Architecture/) — Архитектура веб-приложений
- [ASGI](../06_ASGI/) — Асинхронный интерфейс

**Practice Ideas:**

1. Создайте чат-приложение с комнатами
2. Реализуйте real-time уведомления
3. Создайте collaborative editor
4. Настройте WebSocket с Redis для масштабирования

**Going Deeper:**

- RFC 6455 — WebSocket Protocol
- Socket.IO — библиотека с fallback
- Server-Sent Events как альтернатива

---

## 📚 Additional Resources

**Specifications:**

- [RFC 6455](https://tools.ietf.org/html/rfc6455) — WebSocket Protocol

**Libraries:**

- [websockets](https://websockets.readthedocs.io/) — Python WebSocket
- [Django Channels](https://channels.readthedocs.io/) — WebSocket для Django
- [Socket.IO](https://socket.io/) — Real-time библиотека

**Articles:**

- [WebSocket MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---




