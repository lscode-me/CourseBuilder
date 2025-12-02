# Network Sockets
## Сетевое программирование с TCP/UDP

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модули [Files & I/O](../02_FilesAndIO/) и [IPC](../06_IPC/)
- Понимать модель TCP/IP
- Знать основы сетей (IP адреса, порты)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать TCP и UDP сокеты
- Реализовывать клиент-серверные приложения
- Понимать жизненный цикл соединения
- Обрабатывать несколько клиентов
- Использовать getaddrinfo для DNS
- Писать надёжный сетевой код

---

## 1. Основы сокетов

### 1.1 Что такое сокет

**Сокет** — конечная точка двунаправленного канала связи.

```
┌─────────────────┐                    ┌─────────────────┐
│     Client      │                    │     Server      │
│                 │                    │                 │
│  socket() ──────┼────────────────────┼─── socket()     │
│  connect() ─────┼────────────────────┼─── bind()       │
│                 │                    │     listen()    │
│                 │◄───────────────────┼─── accept()     │
│  send() ────────┼───────────────────►│                 │
│                 │◄───────────────────┼─── recv()       │
│  recv() ◄───────┼───────────────────┤                 │
│                 │                    │     send()      │
│  close() ───────┼────────────────────┼─── close()      │
└─────────────────┘                    └─────────────────┘
```

### 1.2 Типы сокетов

| Тип | Протокол | Характеристики |
|-----|----------|----------------|
| `SOCK_STREAM` | TCP | Надёжный, упорядоченный |
| `SOCK_DGRAM` | UDP | Ненадёжный, без соединения |
| `SOCK_RAW` | IP | Прямой доступ к IP |

### 1.3 Создание сокета

```python
import socket

# Создать TCP сокет
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Создать UDP сокет
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Создать IPv6 сокет
ipv6_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Не забыть закрыть!
tcp_sock.close()
```

---

## 2. TCP Server

### 2.1 Базовый сервер

```python
import socket

def simple_server(host='0.0.0.0', port=8080):
    """Простой TCP сервер."""
    
    # Создать сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Разрешить переиспользование адреса
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Привязать к адресу
    server.bind((host, port))
    
    # Начать слушать (backlog = 5)
    server.listen(5)
    
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            # Принять соединение
            client, address = server.accept()
            print(f"Connection from {address}")
            
            try:
                # Получить данные
                data = client.recv(1024)
                print(f"Received: {data.decode()}")
                
                # Отправить ответ
                client.send(b"Hello from server!\n")
            finally:
                client.close()
    finally:
        server.close()

if __name__ == "__main__":
    simple_server()
```

### 2.2 Использование context manager

```python
import socket

def server_with_context():
    """Сервер с автоматическим закрытием."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', 8080))
        server.listen(5)
        
        print("Server ready")
        
        while True:
            with client, address in server.accept():
                print(f"Connection from {address}")
                data = client.recv(1024)
                client.sendall(b"OK\n")
```

### 2.3 Обработка нескольких клиентов (потоки)

```python
import socket
import threading

def handle_client(client, address):
    """Обработчик клиента."""
    print(f"Handling {address}")
    
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            print(f"From {address}: {data.decode()}")
            client.sendall(data.upper())  # Echo uppercase
    finally:
        print(f"Closing {address}")
        client.close()

def threaded_server(host='0.0.0.0', port=8080):
    """Многопоточный сервер."""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    
    print(f"Threaded server on {host}:{port}")
    
    try:
        while True:
            client, address = server.accept()
            
            thread = threading.Thread(
                target=handle_client,
                args=(client, address)
            )
            thread.daemon = True
            thread.start()
    finally:
        server.close()
```

---

## 3. TCP Client

### 3.1 Базовый клиент

```python
import socket

def simple_client(host='localhost', port=8080):
    """Простой TCP клиент."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Подключиться
        sock.connect((host, port))
        
        # Отправить данные
        sock.sendall(b"Hello, server!")
        
        # Получить ответ
        response = sock.recv(1024)
        print(f"Response: {response.decode()}")

if __name__ == "__main__":
    simple_client()
```

### 3.2 Клиент с таймаутом

```python
import socket

def client_with_timeout(host, port, timeout=5.0):
    """Клиент с таймаутом."""
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        sock.connect((host, port))
        sock.sendall(b"Hello")
        response = sock.recv(1024)
        return response
    except socket.timeout:
        print("Connection timed out")
        return None
    finally:
        sock.close()
```

### 3.3 Полное чтение данных

```python
import socket

def recv_all(sock, length):
    """Получить точно length байт."""
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("Connection closed")
        data += chunk
    return data

def recv_until(sock, delimiter=b"\n"):
    """Получить данные до разделителя."""
    data = b""
    while not data.endswith(delimiter):
        chunk = sock.recv(1)
        if not chunk:
            raise ConnectionError("Connection closed")
        data += chunk
    return data
```

---

## 4. UDP Sockets

### 4.1 UDP Server

```python
import socket

def udp_server(host='0.0.0.0', port=8080):
    """UDP сервер."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((host, port))
        
        print(f"UDP server on {host}:{port}")
        
        while True:
            data, address = server.recvfrom(1024)
            print(f"From {address}: {data.decode()}")
            
            # Отправить ответ
            server.sendto(b"ACK", address)
```

### 4.2 UDP Client

```python
import socket

def udp_client(host='localhost', port=8080):
    """UDP клиент."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # UDP не требует connect(), но можно использовать
        # для "псевдо-соединения"
        
        # Отправить без connect()
        sock.sendto(b"Hello UDP!", (host, port))
        
        # Получить ответ
        data, address = sock.recvfrom(1024)
        print(f"Response from {address}: {data.decode()}")
```

### 4.3 UDP с connect()

```python
import socket

def udp_connected_client(host, port):
    """UDP клиент с connect()."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # "Подключиться" — запомнить адрес
        sock.connect((host, port))
        
        # Теперь можно использовать send/recv вместо sendto/recvfrom
        sock.send(b"Hello")
        data = sock.recv(1024)
        print(f"Response: {data.decode()}")
```

---

## 5. Адреса и DNS

### 5.1 getaddrinfo — универсальное разрешение

```python
import socket

def resolve_address(host, port, family=socket.AF_UNSPEC):
    """Разрешить адрес в list of (family, type, proto, canonname, sockaddr)."""
    
    results = socket.getaddrinfo(
        host, port,
        family,
        socket.SOCK_STREAM,
        0,
        socket.AI_PASSIVE  # Для серверов
    )
    
    for family, socktype, proto, canonname, sockaddr in results:
        print(f"Family: {family}")
        print(f"Sockaddr: {sockaddr}")
        print()
    
    return results

# Пример
resolve_address("google.com", 80)
```

### 5.2 Универсальный клиент (IPv4/IPv6)

```python
import socket

def universal_connect(host, port):
    """Подключиться к любому адресу (IPv4 или IPv6)."""
    
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        family, socktype, proto, canonname, sockaddr = res
        
        try:
            sock = socket.socket(family, socktype, proto)
            sock.settimeout(5)
            sock.connect(sockaddr)
            return sock
        except socket.error:
            if sock:
                sock.close()
            continue
    
    raise ConnectionError(f"Could not connect to {host}:{port}")

# Использование
sock = universal_connect("google.com", 80)
sock.sendall(b"GET / HTTP/1.0\r\n\r\n")
print(sock.recv(1024).decode())
sock.close()
```

### 5.3 gethostname и gethostbyname

```python
import socket

# Имя текущего хоста
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Разрешить имя в IP (устаревший способ, используйте getaddrinfo)
ip = socket.gethostbyname("google.com")
print(f"google.com IP: {ip}")

# Обратное разрешение
hostname, aliases, ips = socket.gethostbyaddr("8.8.8.8")
print(f"8.8.8.8 hostname: {hostname}")
```

---

## 6. Опции сокетов

### 6.1 SO_REUSEADDR

```python
import socket

# Разрешить переиспользование адреса (важно для серверов!)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
```

### 6.2 SO_KEEPALIVE

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Включить TCP keepalive
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

# На Linux можно настроить параметры
# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)
# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)
```

### 6.3 TCP_NODELAY (отключение алгоритма Nagle)

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Отключить буферизацию Nagle для низкой задержки
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
```

### 6.4 Размеры буферов

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получить текущие размеры
recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f"Receive buffer: {recv_buf}")
print(f"Send buffer: {send_buf}")

# Установить размеры
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
```

---

## 7. Обработка ошибок

### 7.1 Основные исключения

```python
import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect(('nonexistent.host', 80))
    sock.sendall(b"Hello")
    data = sock.recv(1024)
except socket.timeout:
    print("Operation timed out")
except socket.gaierror as e:
    print(f"Address error: {e}")
except ConnectionRefusedError:
    print("Connection refused")
except ConnectionResetError:
    print("Connection reset by peer")
except BrokenPipeError:
    print("Broken pipe")
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    sock.close()
```

### 7.2 Graceful shutdown

```python
import socket

def graceful_close(sock):
    """Корректное закрытие соединения."""
    try:
        # Завершить отправку
        sock.shutdown(socket.SHUT_WR)
        
        # Прочитать оставшиеся данные
        while True:
            data = sock.recv(1024)
            if not data:
                break
    except socket.error:
        pass
    finally:
        sock.close()
```

---

## 8. Практические примеры

### 8.1 HTTP клиент

```python
#!/usr/bin/env python3
"""Простой HTTP клиент."""

import socket

def http_get(host, path="/", port=80):
    """Выполнить HTTP GET запрос."""
    
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(request.encode())
        
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
    
    return response.decode()

if __name__ == "__main__":
    response = http_get("example.com")
    print(response)
```

### 8.2 Echo сервер с протоколом

```python
#!/usr/bin/env python3
"""Echo сервер с простым протоколом."""

import socket
import struct

# Протокол: 4 байта длины + данные

def send_message(sock, data):
    """Отправить сообщение с префиксом длины."""
    length = len(data)
    sock.sendall(struct.pack("!I", length) + data)

def recv_message(sock):
    """Получить сообщение с префиксом длины."""
    # Прочитать длину
    length_data = b""
    while len(length_data) < 4:
        chunk = sock.recv(4 - len(length_data))
        if not chunk:
            return None
        length_data += chunk
    
    length = struct.unpack("!I", length_data)[0]
    
    # Прочитать данные
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("Connection closed")
        data += chunk
    
    return data

def echo_server(port=8080):
    """Echo сервер."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', port))
        server.listen(5)
        
        print(f"Echo server on port {port}")
        
        while True:
            client, addr = server.accept()
            print(f"Client: {addr}")
            
            try:
                while True:
                    message = recv_message(client)
                    if message is None:
                        break
                    print(f"Received: {message.decode()}")
                    send_message(client, message.upper())
            finally:
                client.close()
                print(f"Closed: {addr}")

if __name__ == "__main__":
    echo_server()
```

### 8.3 Простой чат сервер

```python
#!/usr/bin/env python3
"""Простой чат сервер."""

import socket
import threading
import sys

clients = []
clients_lock = threading.Lock()

def broadcast(message, sender=None):
    """Отправить сообщение всем клиентам."""
    with clients_lock:
        for client in clients:
            if client != sender:
                try:
                    client.sendall(message)
                except:
                    pass

def handle_client(client, address):
    """Обработчик клиента."""
    name = f"{address[0]}:{address[1]}"
    
    with clients_lock:
        clients.append(client)
    
    broadcast(f"[{name} joined]\n".encode())
    
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            message = f"[{name}] {data.decode()}"
            print(message, end="")
            broadcast(message.encode(), sender=client)
    finally:
        with clients_lock:
            clients.remove(client)
        
        broadcast(f"[{name} left]\n".encode())
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    
    print("Chat server started on port 8080")
    
    try:
        while True:
            client, address = server.accept()
            print(f"New connection: {address}")
            
            thread = threading.Thread(
                target=handle_client,
                args=(client, address)
            )
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    main()
```

---

## 💡 Key Takeaways

- **TCP** — надёжный, с установкой соединения
- **UDP** — ненадёжный, без соединения
- **SO_REUSEADDR** — обязателен для серверов
- **getaddrinfo** — универсальный способ разрешения адресов
- **sendall** — гарантирует отправку всех данных
- Всегда обрабатывайте ошибки сети!

---

## 🚀 Next Steps

**Related Modules:**
- [Unix Sockets](../08_UnixSockets/) — локальные сокеты
- [Async I/O](../09_AsyncIO/) — асинхронная работа с сокетами

**Practice Ideas:**
1. Реализуйте FTP-подобный сервер
2. Создайте простой proxy сервер
3. Напишите port scanner
4. Реализуйте протокол поверх UDP с подтверждениями

**Going Deeper:**
- SSL/TLS (модуль ssl)
- HTTP/2 и WebSockets
- Zero-copy с sendfile()

---

## 📚 Additional Resources

**Documentation:**
- [man socket(2)](https://man.openbsd.org/socket.2)
- [Python socket](https://docs.python.org/3/library/socket.html)
- [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

---

