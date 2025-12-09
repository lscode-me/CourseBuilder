# Asynchronous I/O
## Асинхронный ввод-вывод и событийный цикл

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [Sockets](../07_Sockets/) и [Unix Sockets](../08_UnixSockets/)
- Понимать блокирующий I/O
- Знать основы многопоточности

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать проблему blocking I/O
- Использовать select, poll, kqueue для мультиплексирования
- Применять asyncio для асинхронного программирования
- Создавать высокопроизводительные серверы
- Писать неблокирующий сетевой код

---

## 1. Проблема блокирующего I/O

### 1.1 Blocking vs Non-blocking

```
Blocking I/O:
┌─────────┐         ┌─────────┐
│ Thread  │─────────│  recv() │  Ждёт данные...
│ blocked │         │         │
└─────────┘         └─────────┘
                         │
                         ▼
                    Data arrives
                         │
                         ▼
                    Thread continues

Non-blocking I/O:
┌─────────┐         ┌─────────┐
│ Thread  │─────────│  recv() │  Возвращает сразу
│ active  │         │ EAGAIN  │  (нет данных)
└─────────┘         └─────────┘
     │
     ▼
   Делает другую работу
```

### 1.2 Способы обработки множества соединений

| Метод | Масштабируемость | Сложность |
|-------|------------------|-----------|
| Один процесс/поток | 1 соединение | Простая |
| Fork на соединение | Сотни | Средняя |
| Поток на соединение | Тысячи | Средняя |
| Event loop (select/poll) | Тысячи | Сложная |
| Event loop (epoll/kqueue) | Сотни тысяч | Сложная |
| asyncio | Сотни тысяч | Средняя |

---

## 2. select — базовый мультиплексор

### 2.1 Основы select

```python
import select
import socket

def select_server(host='0.0.0.0', port=8080):
    """Сервер на select."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind((host, port))
    server.listen(5)
    
    # Списки для мониторинга
    inputs = [server]
    outputs = []
    
    print(f"Select server on {host}:{port}")
    
    while inputs:
        # select блокируется до события
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs, 1.0  # timeout 1 sec
        )
        
        for sock in readable:
            if sock is server:
                # Новое соединение
                client, addr = sock.accept()
                client.setblocking(False)
                inputs.append(client)
                print(f"New connection: {addr}")
            else:
                # Данные от клиента
                try:
                    data = sock.recv(1024)
                    if data:
                        print(f"Received: {data.decode()}")
                        sock.sendall(data.upper())
                    else:
                        # Соединение закрыто
                        inputs.remove(sock)
                        sock.close()
                except BlockingIOError:
                    pass
        
        for sock in exceptional:
            inputs.remove(sock)
            sock.close()
    
    server.close()
```

### 2.2 Ограничения select

- Максимум ~1024 дескрипторов (FD_SETSIZE)
- O(n) сложность при каждом вызове
- Копирует все дескрипторы в ядро

---

## 3. poll — улучшенный мультиплексор

### 3.1 Основы poll

```python
import select
import socket

def poll_server(host='0.0.0.0', port=8080):
    """Сервер на poll."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind((host, port))
    server.listen(5)
    
    # Создать poll объект
    poll_obj = select.poll()
    poll_obj.register(server, select.POLLIN)
    
    # Словарь fd -> socket
    fd_to_socket = {server.fileno(): server}
    
    print(f"Poll server on {host}:{port}")
    
    while True:
        events = poll_obj.poll(1000)  # timeout 1000ms
        
        for fd, event in events:
            sock = fd_to_socket[fd]
            
            if event & select.POLLIN:
                if sock is server:
                    # Новое соединение
                    client, addr = sock.accept()
                    client.setblocking(False)
                    poll_obj.register(client, select.POLLIN)
                    fd_to_socket[client.fileno()] = client
                    print(f"New connection: {addr}")
                else:
                    # Данные от клиента
                    try:
                        data = sock.recv(1024)
                        if data:
                            sock.sendall(data.upper())
                        else:
                            poll_obj.unregister(fd)
                            del fd_to_socket[fd]
                            sock.close()
                    except BlockingIOError:
                        pass
            
            elif event & (select.POLLHUP | select.POLLERR):
                poll_obj.unregister(fd)
                del fd_to_socket[fd]
                sock.close()

if __name__ == "__main__":
    poll_server()
```

### 3.2 Флаги poll

| Флаг | Описание |
|------|----------|
| `POLLIN` | Данные для чтения |
| `POLLOUT` | Можно писать |
| `POLLERR` | Ошибка |
| `POLLHUP` | Соединение закрыто |
| `POLLNVAL` | Невалидный дескриптор |

---

## 4. kqueue — BSD/macOS

### 4.1 Основы kqueue

```python
import select
import socket

def kqueue_server(host='0.0.0.0', port=8080):
    """Сервер на kqueue (BSD/macOS)."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind((host, port))
    server.listen(5)
    
    # Создать kqueue
    kq = select.kqueue()
    
    # Зарегистрировать сервер
    event = select.kevent(
        server.fileno(),
        filter=select.KQ_FILTER_READ,
        flags=select.KQ_EV_ADD
    )
    kq.control([event], 0)
    
    fd_to_socket = {server.fileno(): server}
    
    print(f"Kqueue server on {host}:{port}")
    
    while True:
        events = kq.control(None, 10, 1)  # max 10 events, 1 sec timeout
        
        for event in events:
            fd = event.ident
            sock = fd_to_socket.get(fd)
            
            if sock is None:
                continue
            
            if event.filter == select.KQ_FILTER_READ:
                if sock is server:
                    # Новое соединение
                    client, addr = sock.accept()
                    client.setblocking(False)
                    
                    # Зарегистрировать клиента
                    kevent = select.kevent(
                        client.fileno(),
                        filter=select.KQ_FILTER_READ,
                        flags=select.KQ_EV_ADD
                    )
                    kq.control([kevent], 0)
                    
                    fd_to_socket[client.fileno()] = client
                    print(f"New connection: {addr}")
                else:
                    # Данные от клиента
                    try:
                        data = sock.recv(1024)
                        if data:
                            sock.sendall(data.upper())
                        else:
                            # Удалить из kqueue
                            kevent = select.kevent(
                                fd,
                                filter=select.KQ_FILTER_READ,
                                flags=select.KQ_EV_DELETE
                            )
                            kq.control([kevent], 0)
                            del fd_to_socket[fd]
                            sock.close()
                    except BlockingIOError:
                        pass

if __name__ == "__main__":
    kqueue_server()
```

---

## 5. selectors — высокоуровневый API

### 5.1 DefaultSelector

```python
import selectors
import socket

def selectors_server(host='0.0.0.0', port=8080):
    """Сервер на selectors (автовыбор лучшего метода)."""
    
    sel = selectors.DefaultSelector()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind((host, port))
    server.listen(5)
    
    def accept(sock):
        client, addr = sock.accept()
        client.setblocking(False)
        sel.register(client, selectors.EVENT_READ, handle_client)
        print(f"New connection: {addr}")
    
    def handle_client(sock):
        try:
            data = sock.recv(1024)
            if data:
                sock.sendall(data.upper())
            else:
                sel.unregister(sock)
                sock.close()
        except BlockingIOError:
            pass
    
    sel.register(server, selectors.EVENT_READ, accept)
    
    print(f"Selectors server on {host}:{port}")
    print(f"Using: {type(sel).__name__}")
    
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == "__main__":
    selectors_server()
```

---

## 6. asyncio — современный подход

### 6.1 Базовый asyncio сервер

```python
import asyncio

async def handle_client(reader, writer):
    """Обработчик клиента."""
    addr = writer.get_extra_info('peername')
    print(f"New connection: {addr}")
    
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            
            message = data.decode()
            print(f"Received from {addr}: {message}")
            
            writer.write(data.upper())
            await writer.drain()
    finally:
        print(f"Closing: {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '0.0.0.0', 8080
    )
    
    addr = server.sockets[0].getsockname()
    print(f"Asyncio server on {addr}")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.2 Asyncio клиент

```python
import asyncio

async def tcp_client(message):
    """Asyncio TCP клиент."""
    
    reader, writer = await asyncio.open_connection('localhost', 8080)
    
    print(f"Sending: {message}")
    writer.write(message.encode())
    await writer.drain()
    
    data = await reader.read(1024)
    print(f"Received: {data.decode()}")
    
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_client("Hello, asyncio!"))
```

### 6.3 Параллельные задачи

```python
import asyncio

async def fetch_url(url, delay):
    """Имитация HTTP запроса."""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    print(f"Done: {url}")
    return f"Result from {url}"

async def main():
    # Создать задачи
    tasks = [
        asyncio.create_task(fetch_url("http://example1.com", 2)),
        asyncio.create_task(fetch_url("http://example2.com", 1)),
        asyncio.create_task(fetch_url("http://example3.com", 3)),
    ]
    
    # Ждать все
    results = await asyncio.gather(*tasks)
    print(f"All results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.4 Таймауты

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 7. Низкоуровневый asyncio

### 7.1 Протоколы и транспорты

```python
import asyncio

class EchoProtocol(asyncio.Protocol):
    """Echo протокол."""
    
    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info('peername')
        print(f"Connection from {peername}")
    
    def data_received(self, data):
        print(f"Received: {data.decode()}")
        self.transport.write(data.upper())
    
    def connection_lost(self, exc):
        print("Connection closed")

async def main():
    loop = asyncio.get_running_loop()
    
    server = await loop.create_server(
        EchoProtocol,
        '0.0.0.0', 8080
    )
    
    print("Protocol server started")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
```

### 7.2 Работа с файлами

```python
import asyncio
import aiofiles  # pip install aiofiles

async def read_file_async(path):
    """Асинхронное чтение файла."""
    async with aiofiles.open(path, 'r') as f:
        content = await f.read()
    return content

async def write_file_async(path, content):
    """Асинхронная запись в файл."""
    async with aiofiles.open(path, 'w') as f:
        await f.write(content)

async def main():
    # Параллельное чтение файлов
    tasks = [
        read_file_async("/etc/passwd"),
        read_file_async("/etc/group"),
    ]
    
    results = await asyncio.gather(*tasks)
    for i, content in enumerate(results):
        print(f"File {i}: {len(content)} bytes")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 8. Практические примеры

### 8.1 Асинхронный HTTP сервер

```python
#!/usr/bin/env python3
"""Простой асинхронный HTTP сервер."""

import asyncio
from datetime import datetime

async def handle_http(reader, writer):
    """Обработчик HTTP запроса."""
    # Прочитать запрос
    request = await reader.read(4096)
    request_line = request.decode().split('\r\n')[0]
    print(f"Request: {request_line}")
    
    # Сформировать ответ
    body = f"""<html>
    <head><title>AsyncIO Server</title></head>
    <body>
        <h1>Hello from asyncio!</h1>
        <p>Time: {datetime.now()}</p>
    </body>
    </html>"""
    
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )
    
    writer.write(response.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_http, '0.0.0.0', 8080
    )
    
    print("HTTP server on http://localhost:8080")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
```

### 8.2 Параллельный сканер портов

```python
#!/usr/bin/env python3
"""Асинхронный сканер портов."""

import asyncio
import sys

async def check_port(host, port, timeout=1.0):
    """Проверить открыт ли порт."""
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
        writer.close()
        await writer.wait_closed()
        return port, True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return port, False

async def scan_ports(host, ports, concurrency=100):
    """Сканировать порты."""
    semaphore = asyncio.Semaphore(concurrency)
    
    async def scan_with_semaphore(port):
        async with semaphore:
            return await check_port(host, port)
    
    tasks = [scan_with_semaphore(port) for port in ports]
    results = await asyncio.gather(*tasks)
    
    return [(port, status) for port, status in results if status]

async def main():
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    
    print(f"Scanning {host}...")
    
    open_ports = await scan_ports(host, range(1, 1025))
    
    print(f"\nOpen ports on {host}:")
    for port, _ in open_ports:
        print(f"  {port}")
    
    print(f"\nTotal: {len(open_ports)} open ports")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 💡 Key Takeaways

- **select/poll** — базовые мультиплексоры (O(n))
- **kqueue/epoll** — масштабируемые (O(1))
- **selectors** — кроссплатформенный высокоуровневый API
- **asyncio** — современный способ асинхронного программирования
- **await** — приостановить корутину до завершения операции

---

## 🚀 Next Steps

**Related Modules:**
- [Threads](../10_Threads/) — многопоточность
- [Daemons](../12_Daemons/) — создание демонов

**Practice Ideas:**
1. Создайте асинхронный прокси сервер
2. Напишите параллельный HTTP клиент
3. Реализуйте WebSocket сервер
4. Создайте асинхронный DNS resolver

**Going Deeper:**
- uvloop — быстрая альтернатива event loop
- aiohttp — асинхронный HTTP
- trio — альтернативная async библиотека

---

## 📚 Additional Resources

**Documentation:**
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [Python selectors](https://docs.python.org/3/library/selectors.html)
- [man select(2)](https://man.openbsd.org/select.2)
- [man kqueue(2)](https://man.openbsd.org/kqueue.2)

---

