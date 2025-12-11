# Socket Activation
## Обработка сетевых соединений через systemd и inetd

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP протокол (предыдущий модуль)
- Знать основы работы с сокетами
- Иметь базовые знания systemd или inetd

**Recommended prior modules:**

- [HTTP Protocol](../01_HTTP/) — структура HTTP
- [Sockets](../../UnixProgramming/07_Sockets/) — сетевое программирование
- [Daemons](../../UnixProgramming/12_Daemons/) — фоновые процессы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать концепцию socket activation
- Создавать systemd socket units
- Писать простые веб-серверы на shell и Python
- Понимать преимущества socket activation
- Использовать inetd/xinetd как альтернативу

---

## 1. Концепция Socket Activation

### 1.1 Зачем нужен socket activation

**Традиционный подход:**
```

┌──────────────────────────────────────────────────────────────┐
│            Traditional Daemon Startup                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  System Boot                                                 │
│       │                                                      │
│       ▼                                                      │
│  ┌─────────────┐                                             │
│  │ Start nginx │ ← демон стартует сам                        │
│  └──────┬──────┘                                             │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────┐                                             │
│  │ bind(:80)   │ ← демон сам открывает сокет                 │
│  │ listen()    │                                             │
│  └──────┬──────┘                                             │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────┐                                             │
│  │   accept()  │ ← демон ждёт соединений                     │
│  │   (wait)    │                                             │
│  └─────────────┘                                             │
│                                                              │
└──────────────────────────────────────────────────────────────┘

```

**Проблемы:**

- Все демоны стартуют при загрузке (медленно)
- Потребляют память даже без нагрузки
- Жёсткий порядок запуска (зависимости)

**Socket Activation:**
```

┌──────────────────────────────────────────────────────────────┐
│            Socket Activation (systemd)                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  System Boot                                                 │
│       │                                                      │
│       ▼                                                      │
│  ┌─────────────┐                                             │
│  │ systemd     │                                             │
│  │ bind(:80)   │ ← systemd открывает сокет                   │
│  │ listen()    │                                             │
│  └──────┬──────┘                                             │
│         │                                                    │
│         │  (демон НЕ запущен, память не потребляет)          │
│         │                                                    │
│         ▼                                                    │
│  First connection arrives on :80                             │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────┐                                             │
│  │ Start nginx │ ← systemd запускает демон                   │
│  │ Pass FD 3   │ ← передаёт готовый сокет                    │
│  └──────┬──────┘                                             │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────┐                                             │
│  │ nginx       │                                             │
│  │ accept(3)   │ ← демон принимает соединение                │
│  └─────────────┘                                             │
│                                                              │
└──────────────────────────────────────────────────────────────┘

```

### 1.2 Преимущества socket activation

| Преимущество | Описание |
|--------------|----------|
| **Быстрая загрузка** | Демоны запускаются только при необходимости |
| **Экономия памяти** | Неиспользуемые сервисы не загружены |
| **Без потери соединений** | Сокет доступен даже во время перезапуска демона |
| **Параллельный запуск** | Нет жёстких зависимостей — сокеты готовы сразу |
| **Простые демоны** | Не нужен код для bind/listen |

### 1.3 История: inetd — "супердемон"

До systemd существовал **inetd** (Internet super-server daemon):

```
# /etc/inetd.conf
# service  socket  protocol  wait  user  program  args
echo       stream  tcp       nowait root  internal
daytime    stream  tcp       nowait root  internal
ftp        stream  tcp       nowait root  /usr/sbin/ftpd  ftpd
telnet     stream  tcp       nowait root  /usr/sbin/telnetd  telnetd

```

inetd слушает все порты и запускает соответствующую программу при подключении.

---

## 2. Простейший HTTP сервер на Shell

### 2.1 Минимальный веб-сервер

```bash
#!/bin/bash
# simple_http.sh — минимальный HTTP сервер для inetd/systemd

# Читаем первую строку запроса
read -r request_line

# Логируем (в stderr, потому что stdout — это соединение)
echo "Request: $request_line" >&2

# Парсим путь
path=$(echo "$request_line" | cut -d' ' -f2)

# Читаем заголовки (до пустой строки)
while read -r header; do
    # Убираем \r в конце
    header=$(echo "$header" | tr -d '\r')
    [ -z "$header" ] && break
    echo "Header: $header" >&2
done

# Определяем ответ
case "$path" in
    "/")
        body="<html><body><h1>Hello from Shell!</h1><p>Path: $path</p></body></html>"
        content_type="text/html"
        status="200 OK"
        ;;
    "/time")
        body="<html><body><h1>Current Time</h1><p>$(date)</p></body></html>"
        content_type="text/html"
        status="200 OK"
        ;;
    "/json")
        body='{"status":"ok","server":"shell","time":"'"$(date -Iseconds)"'"}'
        content_type="application/json"
        status="200 OK"
        ;;
    *)
        body="<html><body><h1>404 Not Found</h1><p>Path $path not found</p></body></html>"
        content_type="text/html"
        status="404 Not Found"
        ;;
esac

# Отправляем HTTP ответ
echo -en "HTTP/1.1 $status\r\n"
echo -en "Content-Type: $content_type\r\n"
echo -en "Content-Length: ${#body}\r\n"
echo -en "Connection: close\r\n"
echo -en "Server: ShellHTTP/1.0\r\n"
echo -en "\r\n"
echo -n "$body"

```

### 2.2 Тестирование с netcat

```bash
# Сделать скрипт исполняемым
chmod +x simple_http.sh

# Запустить "сервер" через netcat
# -l - listen, -p - port, -e - execute
while true; do nc -l -p 8080 -e ./simple_http.sh; done

# В другом терминале проверить
curl http://localhost:8080/
curl http://localhost:8080/time
curl http://localhost:8080/json

```

### 2.3 Расширенный shell сервер

```bash
#!/bin/bash
# http_server.sh — более полный HTTP сервер

set -e

# Конфигурация
DOC_ROOT="${DOC_ROOT:-/var/www/html}"
SERVER_NAME="ShellHTTP/1.0"

# Читаем запрос
read_request() {
    read -r method path version
    path=$(echo "$path" | tr -d '\r')
    
    # Читаем заголовки в ассоциативный массив
    declare -gA headers
    while IFS=': ' read -r key value; do
        value=$(echo "$value" | tr -d '\r')
        [ -z "$key" ] && break
        headers["$key"]="$value"
    done
    
    echo "[$( date '+%Y-%m-%d %H:%M:%S' )] $method $path" >&2
}

# Отправляем ответ
send_response() {
    local status="$1"
    local content_type="$2"
    local body="$3"
    
    local length=${#body}
    
    printf "HTTP/1.1 %s\r\n" "$status"
    printf "Content-Type: %s\r\n" "$content_type"
    printf "Content-Length: %d\r\n" "$length"
    printf "Server: %s\r\n" "$SERVER_NAME"
    printf "Date: %s\r\n" "$(date -u '+%a, %d %b %Y %H:%M:%S GMT')"
    printf "Connection: close\r\n"
    printf "\r\n"
    printf "%s" "$body"
}

# Отправить файл
send_file() {
    local filepath="$1"
    local content_type="$2"
    
    if [ ! -f "$filepath" ]; then
        send_response "404 Not Found" "text/html" "<h1>404 Not Found</h1>"
        return
    fi
    
    local length=$(stat -c%s "$filepath" 2>/dev/null || stat -f%z "$filepath")
    
    printf "HTTP/1.1 200 OK\r\n"
    printf "Content-Type: %s\r\n" "$content_type"
    printf "Content-Length: %d\r\n" "$length"
    printf "Server: %s\r\n" "$SERVER_NAME"
    printf "Connection: close\r\n"
    printf "\r\n"
    cat "$filepath"
}

# Определить MIME тип
get_mime_type() {
    case "$1" in
        *.html|*.htm) echo "text/html" ;;
        *.css)        echo "text/css" ;;
        *.js)         echo "application/javascript" ;;
        *.json)       echo "application/json" ;;
        *.txt)        echo "text/plain" ;;
        *.png)        echo "image/png" ;;
        *.jpg|*.jpeg) echo "image/jpeg" ;;
        *.gif)        echo "image/gif" ;;
        *.svg)        echo "image/svg+xml" ;;
        *.pdf)        echo "application/pdf" ;;
        *)            echo "application/octet-stream" ;;
    esac
}

# Главная функция
main() {
    read_request
    
    # Безопасность: удаляем .. из пути
    local safe_path=$(echo "$path" | sed 's/\.\.//g')
    
    # Добавляем index.html для директорий
    if [ "$safe_path" = "/" ]; then
        safe_path="/index.html"
    fi
    
    local filepath="${DOC_ROOT}${safe_path}"
    local mime_type=$(get_mime_type "$filepath")
    
    send_file "$filepath" "$mime_type"
}

main

```

---

## 3. HTTP сервер на Python

### 3.1 Минимальный STDIN/STDOUT сервер

```python
#!/usr/bin/env python3
"""
simple_http.py — HTTP сервер для socket activation.
Читает из stdin, пишет в stdout.
"""

import sys
from datetime import datetime


def parse_request():
    """Парсит HTTP запрос из stdin."""
    # Первая строка: METHOD /path HTTP/1.1
    request_line = sys.stdin.readline().strip()
    if not request_line:
        return None, None, {}
    
    parts = request_line.split()
    if len(parts) < 2:
        return None, None, {}
    
    method = parts[0]
    path = parts[1]
    
    # Читаем заголовки
    headers = {}
    while True:
        line = sys.stdin.readline()
        if not line or line.strip() == '':
            break
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip().lower()] = value.strip()
    
    return method, path, headers


def send_response(status: str, body: str, content_type: str = "text/html"):
    """Отправляет HTTP ответ в stdout."""
    body_bytes = body.encode('utf-8')
    
    sys.stdout.write(f"HTTP/1.1 {status}\r\n")
    sys.stdout.write(f"Content-Type: {content_type}; charset=utf-8\r\n")
    sys.stdout.write(f"Content-Length: {len(body_bytes)}\r\n")
    sys.stdout.write(f"Server: PythonHTTP/1.0\r\n")
    sys.stdout.write(f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n")
    sys.stdout.write(f"Connection: close\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write(body)
    sys.stdout.flush()


def handle_request(method: str, path: str, headers: dict):
    """Обработка HTTP запроса."""
    
    if path == "/":
        body = f"""<!DOCTYPE html>
<html>
<head><title>Python HTTP Server</title></head>
<body>
    <h1>Hello from Python!</h1>
    <p>Method: {method}</p>
    <p>Path: {path}</p>
    <p>Time: {datetime.now()}</p>
</body>
</html>"""
        send_response("200 OK", body)
    
    elif path == "/json":
        import json
        data = {
            "status": "ok",
            "server": "python",
            "method": method,
            "time": datetime.now().isoformat(),
            "headers": headers
        }
        send_response("200 OK", json.dumps(data, indent=2), "application/json")
    
    elif path == "/env":
        import os
        body = "<html><body><h1>Environment</h1><pre>"
        for key, value in sorted(os.environ.items()):
            body += f"{key}={value}\n"
        body += "</pre></body></html>"
        send_response("200 OK", body)
    
    else:
        body = f"<html><body><h1>404 Not Found</h1><p>Path {path} not found</p></body></html>"
        send_response("404 Not Found", body)


def main():
    method, path, headers = parse_request()
    
    if method is None:
        send_response("400 Bad Request", "<h1>Bad Request</h1>")
        return
    
    # Логируем в stderr
    print(f"[{datetime.now()}] {method} {path}", file=sys.stderr)
    
    handle_request(method, path, headers)


if __name__ == "__main__":
    main()

```

### 3.2 Python сервер с сокетом

```python
#!/usr/bin/env python3
"""
http_server.py — HTTP сервер с поддержкой socket activation.
Может работать как standalone или принимать сокет от systemd.
"""

import os
import sys
import socket
from datetime import datetime
import json


def get_listen_socket(port: int = 8080) -> socket.socket:
    """
    Получить сокет для прослушивания.
    Если запущен через socket activation — использовать переданный сокет.
    Иначе — создать свой.
    """
    # Проверяем, есть ли переданные от systemd сокеты
    # LISTEN_FDS — количество переданных файловых дескрипторов
    # LISTEN_PID — PID процесса, которому предназначены сокеты
    listen_fds = os.environ.get('LISTEN_FDS')
    listen_pid = os.environ.get('LISTEN_PID')
    
    if listen_fds and listen_pid:
        # Socket activation!
        if int(listen_pid) == os.getpid():
            # Сокеты начинаются с FD 3 (после stdin, stdout, stderr)
            # SD_LISTEN_FDS_START = 3
            fd = 3
            print(f"Using socket activation, FD={fd}", file=sys.stderr)
            return socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
    
    # Standalone режим — создаём сокет сами
    print(f"Creating socket on port {port}", file=sys.stderr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)
    return sock


def parse_request(data: bytes) -> tuple:
    """Парсит HTTP запрос."""
    try:
        text = data.decode('utf-8', errors='replace')
        lines = text.split('\r\n')
        
        # Request line
        request_line = lines[0]
        parts = request_line.split()
        method = parts[0] if len(parts) > 0 else ''
        path = parts[1] if len(parts) > 1 else '/'
        
        # Headers
        headers = {}
        for line in lines[1:]:
            if not line:
                break
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip().lower()] = value.strip()
        
        return method, path, headers
    except Exception as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return 'GET', '/', {}


def build_response(status: str, body: str, content_type: str = "text/html") -> bytes:
    """Строит HTTP ответ."""
    body_bytes = body.encode('utf-8')
    
    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: {content_type}; charset=utf-8\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        f"Server: PythonHTTP/1.0\r\n"
        f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    
    return response.encode('utf-8') + body_bytes


def handle_request(method: str, path: str, headers: dict) -> bytes:
    """Обработка запроса, возвращает HTTP ответ."""
    
    if path == "/":
        body = f"""<!DOCTYPE html>
<html>
<head><title>Python HTTP Server</title></head>
<body>
    <h1>Hello from Python!</h1>
    <p>Method: {method}</p>
    <p>Time: {datetime.now()}</p>
    <ul>
        <li><a href="/json">JSON endpoint</a></li>
        <li><a href="/env">Environment</a></li>
        <li><a href="/status">Status</a></li>
    </ul>
</body>
</html>"""
        return build_response("200 OK", body)
    
    elif path == "/json":
        data = {
            "status": "ok",
            "method": method,
            "time": datetime.now().isoformat(),
            "pid": os.getpid(),
            "socket_activation": 'LISTEN_FDS' in os.environ
        }
        return build_response("200 OK", json.dumps(data, indent=2), "application/json")
    
    elif path == "/env":
        body = "<html><body><h1>Environment</h1><table border='1'>"
        for key in sorted(os.environ.keys()):
            value = os.environ[key]
            # Скрываем чувствительные данные
            if 'SECRET' in key or 'PASSWORD' in key or 'KEY' in key:
                value = '***'
            body += f"<tr><td><code>{key}</code></td><td><code>{value}</code></td></tr>"
        body += "</table></body></html>"
        return build_response("200 OK", body)
    
    elif path == "/status":
        import resource
        rusage = resource.getrusage(resource.RUSAGE_SELF)
        data = {
            "pid": os.getpid(),
            "ppid": os.getppid(),
            "user_time": rusage.ru_utime,
            "system_time": rusage.ru_stime,
            "max_rss_kb": rusage.ru_maxrss,
            "socket_activation": 'LISTEN_FDS' in os.environ,
            "listen_fds": os.environ.get('LISTEN_FDS', 'N/A'),
        }
        return build_response("200 OK", json.dumps(data, indent=2), "application/json")
    
    else:
        body = f"<html><body><h1>404 Not Found</h1><p>Path: {path}</p></body></html>"
        return build_response("404 Not Found", body)


def handle_client(client: socket.socket, address: tuple):
    """Обработка одного клиента."""
    try:
        data = client.recv(4096)
        if not data:
            return
        
        method, path, headers = parse_request(data)
        print(f"[{datetime.now()}] {address[0]}:{address[1]} {method} {path}", file=sys.stderr)
        
        response = handle_request(method, path, headers)
        client.sendall(response)
    
    except Exception as e:
        print(f"Error handling {address}: {e}", file=sys.stderr)
    
    finally:
        client.close()


def main():
    port = int(os.environ.get('PORT', 8080))
    server = get_listen_socket(port)
    
    print(f"Server listening on port {port}", file=sys.stderr)
    
    try:
        while True:
            client, address = server.accept()
            handle_client(client, address)
    
    except KeyboardInterrupt:
        print("\nShutting down...", file=sys.stderr)
    
    finally:
        server.close()


if __name__ == "__main__":
    main()

```

---

## 4. Настройка systemd Socket Activation

### 4.1 Создание socket unit

```ini
# /etc/systemd/system/myhttp.socket
[Unit]
Description=My HTTP Server Socket

[Socket]
ListenStream=8080
Accept=no

[Install]
WantedBy=sockets.target

```

**Параметры [Socket]:**

| Параметр | Описание |
|----------|----------|
| `ListenStream` | TCP порт или путь к Unix socket |
| `ListenDatagram` | UDP порт |
| `Accept=no` | Один процесс на все соединения |
| `Accept=yes` | Новый процесс на каждое соединение |
| `BindIPv6Only` | Слушать только IPv6 |
| `Backlog` | Размер очереди listen() |
| `MaxConnections` | Лимит соединений (для Accept=yes) |

### 4.2 Создание service unit

```ini
# /etc/systemd/system/myhttp.service
[Unit]
Description=My HTTP Server
Requires=myhttp.socket
After=myhttp.socket

[Service]
Type=simple
ExecStart=/opt/myhttp/http_server.py
StandardInput=socket
StandardOutput=journal
StandardError=journal

# Безопасность
User=www-data
Group=www-data
NoNewPrivileges=yes
ProtectSystem=strict
ProtectHome=yes

[Install]
WantedBy=multi-user.target

```

### 4.3 Активация и запуск

```bash
# Перезагрузить конфигурацию systemd
sudo systemctl daemon-reload

# Включить и запустить socket (не service!)
sudo systemctl enable myhttp.socket
sudo systemctl start myhttp.socket

# Проверить статус
sudo systemctl status myhttp.socket
sudo systemctl status myhttp.service  # ещё не запущен!

# Сделать запрос — сервис запустится автоматически
curl http://localhost:8080/

# Теперь сервис запущен
sudo systemctl status myhttp.service

```

### 4.4 Accept=yes vs Accept=no

**Accept=no (по умолчанию):**

- Один долгоживущий процесс
- Сам делает accept() в цикле
- Эффективнее для высокой нагрузки

```

┌─────────────────────────────────────────────────────────┐
│  Accept=no                                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   systemd                         Service               │
│      │                               │                  │
│      ├── socket FD ─────────────────►│                  │
│      │                               │                  │
│      │                          ┌────┴────┐             │
│      │                          │ accept()│             │
│      │                          │ handle  │             │
│      │                          │ accept()│             │
│      │                          │ handle  │             │
│      │                          │   ...   │             │
│      │                          └─────────┘             │
│                                                         │
└─────────────────────────────────────────────────────────┘

```

**Accept=yes:**

- Новый процесс на каждое соединение
- Как inetd — stdin/stdout это соединение
- Простой код, но дорого при высокой нагрузке

```

┌─────────────────────────────────────────────────────────┐
│  Accept=yes                                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   systemd                                               │
│      │                                                  │
│      ├── accept() ──► fork() ──► Service Instance 1    │
│      │                              stdin/stdout = conn │
│      │                                                  │
│      ├── accept() ──► fork() ──► Service Instance 2    │
│      │                              stdin/stdout = conn │
│      │                                                  │
│      ├── accept() ──► fork() ──► Service Instance 3    │
│      │                              stdin/stdout = conn │
│      ...                                                │
│                                                         │
└─────────────────────────────────────────────────────────┘

```

### 4.5 Socket unit с Accept=yes

```ini
# /etc/systemd/system/myhttp-inetd.socket
[Unit]
Description=My HTTP Server (inetd-style)

[Socket]
ListenStream=8080
Accept=yes
MaxConnections=100

[Install]
WantedBy=sockets.target

```

```ini
# /etc/systemd/system/myhttp-inetd@.service
# Обратите внимание на @ в имени — это шаблон!
[Unit]
Description=My HTTP Server Instance

[Service]
Type=simple
ExecStart=/opt/myhttp/simple_http.py
StandardInput=socket
StandardOutput=socket
StandardError=journal
User=www-data

```

---

## 5. Практика: Полноценный веб-сервер

### 5.1 Структура проекта

```

/opt/myhttp/
├── http_server.py      # Основной сервер
├── handlers.py         # Обработчики маршрутов
├── static/             # Статические файлы
│   ├── index.html
│   ├── style.css
│   └── script.js
└── templates/          # HTML шаблоны
    └── base.html

```

### 5.2 Продвинутый HTTP сервер

```python
#!/usr/bin/env python3
"""
http_server.py — полноценный HTTP сервер с поддержкой:

- Socket activation (systemd)
- Статические файлы
- Простой роутинг
"""

import os
import sys
import socket
import mimetypes
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import json

# Конфигурация
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / 'static'
SERVER_NAME = "PythonHTTP/2.0"


class HTTPRequest:
    """Представление HTTP запроса."""
    
    def __init__(self, data: bytes):
        self.raw = data
        self.method = 'GET'
        self.path = '/'
        self.query_string = ''
        self.query_params = {}
        self.headers = {}
        self.body = b''
        
        self._parse(data)
    
    def _parse(self, data: bytes):
        try:
            text = data.decode('utf-8', errors='replace')
            
            # Разделяем headers и body
            if '\r\n\r\n' in text:
                header_section, body = text.split('\r\n\r\n', 1)
                self.body = body.encode()
            else:
                header_section = text
            
            lines = header_section.split('\r\n')
            
            # Request line
            request_line = lines[0]
            parts = request_line.split()
            self.method = parts[0] if len(parts) > 0 else 'GET'
            
            # Парсим URL
            if len(parts) > 1:
                parsed = urlparse(parts[1])
                self.path = parsed.path or '/'
                self.query_string = parsed.query
                self.query_params = parse_qs(parsed.query)
            
            # Headers
            for line in lines[1:]:
                if ':' in line:
                    key, value = line.split(':', 1)
                    self.headers[key.strip().lower()] = value.strip()
        
        except Exception as e:
            print(f"Parse error: {e}", file=sys.stderr)


class HTTPResponse:
    """Построитель HTTP ответа."""
    
    def __init__(self, status: int = 200, reason: str = "OK"):
        self.status = status
        self.reason = reason
        self.headers = {
            'Server': SERVER_NAME,
            'Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            'Connection': 'close',
        }
        self.body = b''
    
    def set_header(self, key: str, value: str):
        self.headers[key] = value
        return self
    
    def set_body(self, body, content_type: str = 'text/html'):
        if isinstance(body, str):
            self.body = body.encode('utf-8')
        else:
            self.body = body
        
        self.headers['Content-Type'] = content_type
        self.headers['Content-Length'] = str(len(self.body))
        return self
    
    def json(self, data):
        return self.set_body(json.dumps(data, indent=2), 'application/json')
    
    def html(self, content: str):
        return self.set_body(content, 'text/html; charset=utf-8')
    
    def build(self) -> bytes:
        lines = [f"HTTP/1.1 {self.status} {self.reason}"]
        for key, value in self.headers.items():
            lines.append(f"{key}: {value}")
        lines.append('')
        lines.append('')
        
        return '\r\n'.join(lines).encode('utf-8') + self.body


class Router:
    """Простой роутер."""
    
    def __init__(self):
        self.routes = []
    
    def add_route(self, path: str, handler, methods=None):
        methods = methods or ['GET']
        self.routes.append((path, methods, handler))
    
    def match(self, path: str, method: str):
        for route_path, methods, handler in self.routes:
            if path == route_path and method in methods:
                return handler
        return None


# Создаём роутер
router = Router()


def index_handler(request: HTTPRequest) -> HTTPResponse:
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Python HTTP Server</title>
    <style>
        body { font-family: -apple-system, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        h1 { color: #333; }
        a { color: #0066cc; }
        pre { background: #f5f5f5; padding: 15px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>🐍 Python HTTP Server</h1>
    <p>Socket activation: <strong>{socket_activation}</strong></p>
    <p>PID: <code>{pid}</code></p>
    <p>Time: <code>{time}</code></p>
    
    <h2>Endpoints</h2>
    <ul>
        <li><a href="/json">/json</a> — JSON информация</li>
        <li><a href="/env">/env</a> — Переменные окружения</li>
        <li><a href="/echo?message=hello">/echo?message=hello</a> — Echo</li>
        <li><a href="/static/index.html">/static/*</a> — Статические файлы</li>
    </ul>
</body>
</html>""".format(
        socket_activation='Yes' if 'LISTEN_FDS' in os.environ else 'No',
        pid=os.getpid(),
        time=datetime.now().isoformat()
    )
    return HTTPResponse().html(html)


def json_handler(request: HTTPRequest) -> HTTPResponse:
    data = {
        "status": "ok",
        "server": SERVER_NAME,
        "method": request.method,
        "path": request.path,
        "query": request.query_params,
        "headers": request.headers,
        "pid": os.getpid(),
        "socket_activation": 'LISTEN_FDS' in os.environ,
        "timestamp": datetime.now().isoformat()
    }
    return HTTPResponse().json(data)


def env_handler(request: HTTPRequest) -> HTTPResponse:
    # Фильтруем чувствительные данные
    safe_env = {}
    for key, value in os.environ.items():
        if any(s in key.upper() for s in ['SECRET', 'PASSWORD', 'KEY', 'TOKEN']):
            safe_env[key] = '***'
        else:
            safe_env[key] = value
    
    return HTTPResponse().json(safe_env)


def echo_handler(request: HTTPRequest) -> HTTPResponse:
    message = request.query_params.get('message', [''])[0]
    return HTTPResponse().json({
        "echo": message,
        "method": request.method,
        "timestamp": datetime.now().isoformat()
    })


def static_handler(request: HTTPRequest) -> HTTPResponse:
    # Безопасность: убираем .. и нормализуем путь
    relative_path = request.path.replace('/static/', '', 1)
    relative_path = relative_path.replace('..', '')
    
    file_path = STATIC_DIR / relative_path
    
    # Проверяем, что путь не выходит за пределы STATIC_DIR
    try:
        file_path = file_path.resolve()
        if not str(file_path).startswith(str(STATIC_DIR.resolve())):
            return HTTPResponse(403, "Forbidden").html("<h1>403 Forbidden</h1>")
    except Exception:
        return HTTPResponse(400, "Bad Request").html("<h1>400 Bad Request</h1>")
    
    if not file_path.exists():
        return HTTPResponse(404, "Not Found").html(f"<h1>404 Not Found</h1><p>File: {relative_path}</p>")
    
    if file_path.is_dir():
        # Ищем index.html
        index = file_path / 'index.html'
        if index.exists():
            file_path = index
        else:
            return HTTPResponse(403, "Forbidden").html("<h1>403 Forbidden</h1>")
    
    # Определяем MIME тип
    mime_type, _ = mimetypes.guess_type(str(file_path))
    mime_type = mime_type or 'application/octet-stream'
    
    # Читаем и отправляем файл
    with open(file_path, 'rb') as f:
        content = f.read()
    
    return HTTPResponse().set_body(content, mime_type)


# Регистрируем маршруты
router.add_route('/', index_handler)
router.add_route('/json', json_handler)
router.add_route('/env', env_handler)
router.add_route('/echo', echo_handler)


def handle_request(request: HTTPRequest) -> HTTPResponse:
    """Главный обработчик запросов."""
    
    # Статические файлы
    if request.path.startswith('/static/'):
        return static_handler(request)
    
    # Ищем обработчик в роутере
    handler = router.match(request.path, request.method)
    if handler:
        return handler(request)
    
    # 404
    return HTTPResponse(404, "Not Found").html(
        f"<h1>404 Not Found</h1><p>Path: {request.path}</p>"
    )


def get_listen_socket(port: int = 8080) -> socket.socket:
    """Получить сокет (от systemd или создать свой)."""
    listen_fds = os.environ.get('LISTEN_FDS')
    listen_pid = os.environ.get('LISTEN_PID')
    
    if listen_fds and listen_pid:
        if int(listen_pid) == os.getpid():
            fd = 3  # SD_LISTEN_FDS_START
            print(f"Using socket activation, FD={fd}", file=sys.stderr)
            sock = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
            # Важно: не закрывать оригинальный FD
            return sock
    
    print(f"Creating socket on port {port}", file=sys.stderr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(128)
    return sock


def main():
    port = int(os.environ.get('PORT', 8080))
    server = get_listen_socket(port)
    
    print(f"Server running on port {port}", file=sys.stderr)
    print(f"PID: {os.getpid()}", file=sys.stderr)
    
    try:
        while True:
            client, address = server.accept()
            
            try:
                data = client.recv(8192)
                if data:
                    request = HTTPRequest(data)
                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                          f"{address[0]} {request.method} {request.path}", 
                          file=sys.stderr)
                    
                    response = handle_request(request)
                    client.sendall(response.build())
            
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                error_response = HTTPResponse(500, "Internal Server Error")
                error_response.html("<h1>500 Internal Server Error</h1>")
                client.sendall(error_response.build())
            
            finally:
                client.close()
    
    except KeyboardInterrupt:
        print("\nShutting down...", file=sys.stderr)
    
    finally:
        server.close()


if __name__ == "__main__":
    main()

```

### 5.3 Создание статических файлов

```bash

mkdir -p /opt/myhttp/static

cat > /opt/myhttp/static/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Static Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Static HTML Page</h1>
    <p>This is served from the static directory.</p>
    <script src="script.js"></script>
</body>
</html>
EOF

cat > /opt/myhttp/static/style.css << 'EOF'
body {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    max-width: 800px;
    margin: 50px auto;
    padding: 20px;
    background: #f9f9f9;
}
h1 { color: #333; }
EOF

cat > /opt/myhttp/static/script.js << 'EOF'
console.log('Static JS loaded!');
document.addEventListener('DOMContentLoaded', () => {
    document.body.innerHTML += '<p><em>JavaScript is working!</em></p>';
});
EOF

```

---

## 6. inetd и xinetd (альтернатива)

### 6.1 Классический inetd

```
# /etc/inetd.conf
# service  socket  protocol  wait/nowait  user     program        args
8080       stream  tcp       nowait       www-data /opt/myhttp/simple_http.py simple_http.py

```

### 6.2 xinetd (расширенный inetd)

```
# /etc/xinetd.d/myhttp
service myhttp
{
    type            = UNLISTED
    port            = 8080
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = www-data
    server          = /opt/myhttp/simple_http.py
    instances       = 50
    per_source      = 10
    log_on_success  = HOST PID DURATION
    log_on_failure  = HOST
    disable         = no
}

```

### 6.3 OpenBSD inetd

```
# /etc/inetd.conf на OpenBSD
8080 stream tcp nowait www /opt/myhttp/simple_http.py simple_http.py

```

```bash
# Перезапуск inetd
rcctl restart inetd

```

---

## 7. Отладка и мониторинг

### 7.1 Проверка systemd

```bash
# Статус socket
systemctl status myhttp.socket

# Логи socket
journalctl -u myhttp.socket

# Статус service
systemctl status myhttp.service

# Логи service
journalctl -u myhttp.service -f

# Проверить, какие сокеты слушает systemd
systemctl list-sockets

# Детали socket unit
systemctl show myhttp.socket

```

### 7.2 Отладка сети

```bash
# Проверить, что порт слушается
ss -tlnp | grep 8080
netstat -tlnp | grep 8080

# Проверить, кто держит порт
sudo lsof -i :8080

# Тестовые запросы
curl -v http://localhost:8080/
curl -v http://localhost:8080/json

# Смотреть пакеты
sudo tcpdump -i lo port 8080 -A

```

### 7.3 Тестирование socket activation

```bash
# Запускаем напрямую (без systemd)
./http_server.py

# Симулируем socket activation
LISTEN_PID=$$ LISTEN_FDS=1 ./http_server.py 3<>/dev/tcp/localhost/8080
# (не сработает напрямую, но показывает идею)

# Используем systemd-socket-activate для тестирования
systemd-socket-activate -l 8080 ./http_server.py

```

---

## 💡 Key Takeaways

- **Socket activation** — systemd открывает сокет, запускает демон при первом соединении

- **Accept=no** — один процесс обрабатывает все соединения (эффективно)

- **Accept=yes** — новый процесс на каждое соединение (просто как inetd)

- **LISTEN_FDS** и **LISTEN_PID** — переменные окружения от systemd

- **FD 3** — первый переданный файловый дескриптор (после 0, 1, 2)
- Shell и Python легко могут работать в режиме stdin/stdout для Accept=yes

---

## 🚀 Next Steps

**Related Modules:**

- [Web Servers](../03_WebServers/) — Apache, Nginx и другие
- [CGI](../04_CGI/) — Common Gateway Interface

**Practice Ideas:**

1. Создайте systemd socket unit для своего сервера
2. Реализуйте поддержку POST запросов с телом
3. Добавьте логирование в файл
4. Создайте простой reverse proxy на Python

**Going Deeper:**

- systemd.socket(5) man page
- sd_listen_fds(3) — библиотека для работы с socket activation
- xinetd documentation

---

## 📚 Additional Resources

**Documentation:**

- [systemd.socket](https://www.freedesktop.org/software/systemd/man/systemd.socket.html)
- [sd_listen_fds](https://www.freedesktop.org/software/systemd/man/sd_listen_fds.html)
- [inetd(8)](https://man.openbsd.org/inetd.8)

**Articles:**

- [Socket Activation](http://0pointer.de/blog/projects/socket-activation.html) — Lennart Poettering
- [systemd for Developers](https://www.freedesktop.org/wiki/Software/systemd/DaemonSocketActivation/)

---




