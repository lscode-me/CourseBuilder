# Unix Domain Sockets
## Локальное межпроцессное взаимодействие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [Network Sockets](../07_Sockets/)
- Понимать API сокетов
- Знать файловую систему Unix

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать Unix domain sockets
- Понимать преимущества над TCP для локального IPC
- Передавать файловые дескрипторы между процессами
- Использовать abstract sockets на Linux
- Реализовывать клиент-серверные приложения

---

## 1. Что такое Unix Domain Sockets

### 1.1 Определение

**Unix Domain Socket** (UDS) — механизм IPC через интерфейс сокетов, но без сетевого стека.

```
┌─────────────────┐          ┌─────────────────┐
│    Process A    │          │    Process B    │
│                 │          │                 │
│  socket(AF_UNIX)│          │socket(AF_UNIX)  │
│        │        │          │        │        │
│        ▼        │          │        ▼        │
│   /tmp/socket   │◄────────►│   /tmp/socket   │
│                 │          │                 │
└─────────────────┘          └─────────────────┘
```

### 1.2 Преимущества перед TCP

| Характеристика | Unix Socket | TCP localhost |
|----------------|-------------|---------------|
| Производительность | Выше (без TCP stack) | Ниже |
| Права доступа | Файловые права | Нет |
| Передача fd | Да | Нет |
| Учётные данные | Да (SO_PEERCRED) | Нет |

### 1.3 Примеры использования

- Docker daemon (`/var/run/docker.sock`)
- MySQL (`/var/run/mysqld/mysqld.sock`)
- PostgreSQL (`/var/run/postgresql/.s.PGSQL.5432`)
- X11 (`/tmp/.X11-unix/X0`)

---

## 2. Создание Unix Sockets

### 2.1 Stream socket (аналог TCP)

```python
import socket
import os

SOCKET_PATH = "/tmp/my_socket"

def create_server():
    """Создать Unix domain socket сервер."""
    
    # Удалить существующий сокет
    try:
        os.unlink(SOCKET_PATH)
    except FileNotFoundError:
        pass
    
    # Создать сокет
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    # Привязать к пути
    server.bind(SOCKET_PATH)
    
    # Установить права доступа
    os.chmod(SOCKET_PATH, 0o660)
    
    # Начать слушать
    server.listen(5)
    
    return server

def create_client():
    """Создать Unix domain socket клиент."""
    
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(SOCKET_PATH)
    
    return client
```

### 2.2 Datagram socket (аналог UDP)

```python
import socket
import os

SERVER_PATH = "/tmp/server_socket"
CLIENT_PATH = "/tmp/client_socket"

def dgram_server():
    """Datagram сервер."""
    
    try:
        os.unlink(SERVER_PATH)
    except FileNotFoundError:
        pass
    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock.bind(SERVER_PATH)
    
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"From {addr}: {data.decode()}")
        sock.sendto(b"ACK", addr)

def dgram_client():
    """Datagram клиент."""
    
    try:
        os.unlink(CLIENT_PATH)
    except FileNotFoundError:
        pass
    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    # Клиент тоже должен bind() для получения ответов
    sock.bind(CLIENT_PATH)
    
    sock.sendto(b"Hello", SERVER_PATH)
    data, addr = sock.recvfrom(1024)
    print(f"Response: {data.decode()}")
    
    sock.close()
    os.unlink(CLIENT_PATH)
```

---

## 3. Полный пример: сервер и клиент

### 3.1 Сервер

```python
#!/usr/bin/env python3
"""Unix domain socket сервер."""

import socket
import os
import sys

SOCKET_PATH = "/tmp/echo_socket"

def main():
    # Очистить старый сокет
    try:
        os.unlink(SOCKET_PATH)
    except FileNotFoundError:
        pass
    
    # Создать сервер
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(SOCKET_PATH)
    os.chmod(SOCKET_PATH, 0o666)
    server.listen(5)
    
    print(f"Server listening on {SOCKET_PATH}")
    
    try:
        while True:
            client, _ = server.accept()
            print("Client connected")
            
            try:
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    client.sendall(data.upper())
            finally:
                print("Client disconnected")
                client.close()
    finally:
        server.close()
        os.unlink(SOCKET_PATH)

if __name__ == "__main__":
    main()
```

### 3.2 Клиент

```python
#!/usr/bin/env python3
"""Unix domain socket клиент."""

import socket

SOCKET_PATH = "/tmp/echo_socket"

def main():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(SOCKET_PATH)
    
    try:
        while True:
            message = input("Enter message (or 'quit'): ")
            if message == 'quit':
                break
            
            client.sendall(message.encode())
            response = client.recv(1024)
            print(f"Response: {response.decode()}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

---

## 4. Передача файловых дескрипторов

### 4.1 Ancillary data (SCM_RIGHTS)

Unix sockets позволяют передавать файловые дескрипторы между процессами!

```python
import socket
import os
import array

def send_fd(sock, fd):
    """Отправить файловый дескриптор через сокет."""
    sock.sendmsg(
        [b"FD"],  # Обычные данные
        [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", [fd]))]  # Ancillary
    )

def recv_fd(sock):
    """Получить файловый дескриптор из сокета."""
    msg, ancdata, flags, addr = sock.recvmsg(1024, socket.CMSG_SPACE(4))
    
    for cmsg_level, cmsg_type, cmsg_data in ancdata:
        if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
            return array.array("i", cmsg_data)[0]
    
    return None
```

### 4.2 Пример: передача открытого файла

```python
#!/usr/bin/env python3
"""Пример передачи файлового дескриптора."""

import socket
import os
import array

SOCKET_PATH = "/tmp/fd_passing"

def sender():
    """Процесс-отправитель."""
    # Открыть файл
    fd = os.open("/etc/passwd", os.O_RDONLY)
    print(f"Sender: opened file, fd={fd}")
    
    # Создать сокет и подключиться
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(SOCKET_PATH)
    
    # Отправить fd
    sock.sendmsg(
        [b"Here's a file descriptor"],
        [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", [fd]))]
    )
    
    print("Sender: fd sent")
    
    # Закрыть локальную копию
    os.close(fd)
    sock.close()

def receiver():
    """Процесс-получатель."""
    try:
        os.unlink(SOCKET_PATH)
    except FileNotFoundError:
        pass
    
    # Создать сервер
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(SOCKET_PATH)
    server.listen(1)
    
    print("Receiver: waiting for connection")
    
    client, _ = server.accept()
    
    # Получить fd
    msg, ancdata, flags, addr = client.recvmsg(1024, socket.CMSG_SPACE(4))
    
    print(f"Receiver: got message: {msg.decode()}")
    
    for cmsg_level, cmsg_type, cmsg_data in ancdata:
        if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
            received_fd = array.array("i", cmsg_data)[0]
            print(f"Receiver: got fd={received_fd}")
            
            # Использовать полученный fd
            data = os.read(received_fd, 100)
            print(f"Receiver: read from fd: {data.decode()[:50]}...")
            
            os.close(received_fd)
    
    client.close()
    server.close()
    os.unlink(SOCKET_PATH)

# Запустить receiver, затем sender в разных процессах
```

---

## 5. Учётные данные (Credentials)

### 5.1 SO_PEERCRED

```python
import socket
import struct

SOCKET_PATH = "/tmp/cred_socket"

def get_peer_credentials(sock):
    """Получить credentials подключенного процесса."""
    
    # На Linux структура ucred: pid, uid, gid
    # На BSD/macOS структура xucred отличается
    
    try:
        # Linux
        creds = sock.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12)
        pid, uid, gid = struct.unpack("III", creds)
        return {"pid": pid, "uid": uid, "gid": gid}
    except (OSError, AttributeError):
        pass
    
    try:
        # macOS/BSD: LOCAL_PEERCRED
        LOCAL_PEERCRED = 0x001
        creds = sock.getsockopt(socket.SOL_LOCAL, LOCAL_PEERCRED, struct.calcsize("IHHI16I"))
        # Формат xucred на macOS
        return {"uid": struct.unpack_from("I", creds, 4)[0]}
    except (OSError, AttributeError):
        pass
    
    return None

def authenticated_server():
    """Сервер с проверкой credentials."""
    
    try:
        os.unlink(SOCKET_PATH)
    except:
        pass
    
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(SOCKET_PATH)
    server.listen(1)
    
    print("Waiting for connection...")
    client, _ = server.accept()
    
    creds = get_peer_credentials(client)
    print(f"Peer credentials: {creds}")
    
    # Проверить права
    if creds and creds.get("uid") == 0:
        client.sendall(b"Access granted (root)")
    else:
        client.sendall(b"Access granted (non-root)")
    
    client.close()
    server.close()
```

---

## 6. Abstract Sockets (Linux)

### 6.1 Что такое abstract sockets

На Linux можно создать сокет без файла в ФС, используя null байт в начале пути.

```python
import socket

# Abstract socket (Linux only)
# Путь начинается с \0
ABSTRACT_PATH = "\0my_abstract_socket"

def abstract_server():
    """Сервер с abstract socket."""
    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(ABSTRACT_PATH)  # Без файла в ФС!
    sock.listen(1)
    
    print(f"Abstract server ready")
    
    client, _ = sock.accept()
    data = client.recv(1024)
    print(f"Received: {data.decode()}")
    
    client.close()
    sock.close()

def abstract_client():
    """Клиент для abstract socket."""
    
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(ABSTRACT_PATH)
    sock.sendall(b"Hello abstract!")
    sock.close()
```

### 6.2 Преимущества abstract sockets

- Не нужно удалять файл
- Автоматически удаляются при закрытии
- Нет конфликтов с файловой системой
- ⚠️ Работают только на Linux!

---

## 7. Socketpair

### 7.1 Создание связанной пары

```python
import socket
import os

def socketpair_example():
    """Пример использования socketpair для IPC."""
    
    # Создать пару связанных сокетов
    parent_sock, child_sock = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
    
    pid = os.fork()
    
    if pid == 0:
        # Дочерний процесс
        parent_sock.close()  # Закрыть ненужный конец
        
        data = child_sock.recv(1024)
        print(f"Child received: {data.decode()}")
        
        child_sock.sendall(b"Hello from child!")
        child_sock.close()
        os._exit(0)
    else:
        # Родительский процесс
        child_sock.close()  # Закрыть ненужный конец
        
        parent_sock.sendall(b"Hello from parent!")
        
        data = parent_sock.recv(1024)
        print(f"Parent received: {data.decode()}")
        
        parent_sock.close()
        os.wait()

if __name__ == "__main__":
    socketpair_example()
```

---

## 8. Практические примеры

### 8.1 Простой демон с управляющим сокетом

```python
#!/usr/bin/env python3
"""Демон с управляющим Unix socket."""

import socket
import os
import signal
import json
import threading

CONTROL_SOCKET = "/var/run/mydaemon.sock"

class Daemon:
    def __init__(self):
        self.running = True
        self.stats = {"requests": 0, "errors": 0}
    
    def handle_command(self, client):
        """Обработать команду от клиента."""
        try:
            data = client.recv(1024).decode().strip()
            
            if data == "status":
                response = json.dumps(self.stats)
            elif data == "stop":
                self.running = False
                response = "Stopping..."
            elif data == "reset":
                self.stats = {"requests": 0, "errors": 0}
                response = "Stats reset"
            else:
                response = f"Unknown command: {data}"
                self.stats["errors"] += 1
            
            self.stats["requests"] += 1
            client.sendall(response.encode() + b"\n")
        finally:
            client.close()
    
    def run_control_socket(self):
        """Запустить управляющий сокет."""
        try:
            os.unlink(CONTROL_SOCKET)
        except FileNotFoundError:
            pass
        
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(CONTROL_SOCKET)
        os.chmod(CONTROL_SOCKET, 0o600)  # Только root
        server.listen(5)
        server.settimeout(1.0)
        
        while self.running:
            try:
                client, _ = server.accept()
                self.handle_command(client)
            except socket.timeout:
                continue
        
        server.close()
        os.unlink(CONTROL_SOCKET)
    
    def run(self):
        """Основной цикл демона."""
        print(f"Daemon started, PID: {os.getpid()}")
        print(f"Control socket: {CONTROL_SOCKET}")
        
        # Обработчик сигналов
        signal.signal(signal.SIGTERM, lambda s, f: setattr(self, 'running', False))
        signal.signal(signal.SIGINT, lambda s, f: setattr(self, 'running', False))
        
        # Запустить control socket в отдельном потоке
        control_thread = threading.Thread(target=self.run_control_socket)
        control_thread.start()
        
        # Основная работа
        import time
        while self.running:
            time.sleep(1)
        
        control_thread.join()
        print("Daemon stopped")

if __name__ == "__main__":
    daemon = Daemon()
    daemon.run()
```

### 8.2 Клиент для управления демоном

```python
#!/usr/bin/env python3
"""Клиент для управления демоном."""

import socket
import sys

CONTROL_SOCKET = "/var/run/mydaemon.sock"

def send_command(command):
    """Отправить команду демону."""
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(CONTROL_SOCKET)
        
        sock.sendall(command.encode())
        response = sock.recv(4096).decode()
        
        print(response)
        sock.close()
    except FileNotFoundError:
        print("Daemon not running")
        sys.exit(1)
    except PermissionError:
        print("Permission denied")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <command>")
        print("Commands: status, stop, reset")
        sys.exit(1)
    
    send_command(sys.argv[1])
```

---

## 💡 Key Takeaways

- **Unix sockets** — быстрее TCP для локального IPC
- **SCM_RIGHTS** — передача файловых дескрипторов
- **SO_PEERCRED** — аутентификация по UID/GID
- **Abstract sockets** — без файла в ФС (только Linux)
- **socketpair()** — простой способ создать IPC канал

---

## 🚀 Next Steps

**Related Modules:**
- [Async I/O](../09_AsyncIO/) — асинхронная работа с сокетами
- [Daemons](../12_Daemons/) — создание демонов

**Practice Ideas:**
1. Создайте систему плагинов с передачей fd
2. Реализуйте простой сервис-менеджер
3. Напишите proxy между Unix и TCP socket
4. Создайте мультиплексор файловых дескрипторов

**Going Deeper:**
- SOCK_SEQPACKET — сохраняет границы сообщений
- SO_PASSCRED — автоматическая передача credentials
- ancillary data для других целей

---

## 📚 Additional Resources

**Documentation:**
- [man unix(7)](https://man.openbsd.org/unix.4)
- [man sendmsg(2)](https://man.openbsd.org/sendmsg.2)
- [Python socket](https://docs.python.org/3/library/socket.html)

---

