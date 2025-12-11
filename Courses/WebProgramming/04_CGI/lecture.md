# CGI и Gateway Interfaces
## От CGI до FastCGI: эволюция интерфейсов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP протокол
- Знать основы веб-серверов (Apache, Nginx)
- Иметь базовые знания shell и Python

**Recommended prior modules:**

- [HTTP Protocol](../01_HTTP/) — структура HTTP
- [Web Servers](../03_WebServers/) — Apache, Nginx

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать принцип работы CGI
- Писать CGI-скрипты на разных языках
- Понимать проблемы CGI и их решения
- Различать CGI, FastCGI, SCGI
- Настраивать FastCGI в веб-серверах

---

## 1. Common Gateway Interface (CGI)

### 1.1 Что такое CGI

**CGI (Common Gateway Interface)** — стандарт интерфейса между веб-сервером и внешней программой для генерации динамического контента.

```

┌────────────────────────────────────────────────────────────┐
│                    CGI Architecture                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Client          Web Server              CGI Script        │
│    │                 │                       │             │
│    ├── GET /cgi-bin/hello.py ───────────────►│             │
│    │                 │                       │             │
│    │                 │                  ┌────┴────┐        │
│    │                 │      fork() ────►│ Process │        │
│    │                 │                  │ hello.py│        │
│    │                 │                  └────┬────┘        │
│    │                 │                       │             │
│    │                 │◄── stdout (HTML) ─────┤             │
│    │                 │                       │             │
│    │                 │                  Process exits      │
│    │◄── HTTP Response │                       │             │
│    │                 │                       │             │
└────────────────────────────────────────────────────────────┘

```

**Принцип работы:**

1. Клиент запрашивает URL, который указывает на CGI-скрипт
2. Веб-сервер создаёт новый процесс (fork/exec)
3. Сервер передаёт информацию о запросе через:
   - Переменные окружения (метод, заголовки, путь)
   - stdin (тело запроса для POST)
4. Скрипт выводит ответ в stdout
5. Сервер отправляет вывод клиенту
6. Процесс скрипта завершается

### 1.2 История CGI

```

1993 — NCSA HTTPd вводит CGI/1.0
1995 — CGI/1.1 становится стандартом
1997 — RFC 3875 формализует CGI/1.1
2004+ — FastCGI, SCGI, WSGI постепенно заменяют CGI

```

CGI был **революцией**: первый способ создавать динамические веб-страницы.

### 1.3 CGI переменные окружения

| Переменная | Описание | Пример |
|------------|----------|--------|
| `REQUEST_METHOD` | HTTP метод | GET, POST |
| `QUERY_STRING` | Часть URL после ? | `name=John&age=30` |
| `CONTENT_TYPE` | MIME тип тела | `application/x-www-form-urlencoded` |
| `CONTENT_LENGTH` | Длина тела запроса | `42` |
| `PATH_INFO` | Дополнительный путь | `/extra/path` |
| `SCRIPT_NAME` | Путь к скрипту | `/cgi-bin/hello.py` |
| `SERVER_NAME` | Имя сервера | `example.com` |
| `SERVER_PORT` | Порт сервера | `80` |
| `SERVER_PROTOCOL` | Протокол | `HTTP/1.1` |
| `HTTP_*` | HTTP заголовки | `HTTP_USER_AGENT`, `HTTP_COOKIE` |
| `REMOTE_ADDR` | IP клиента | `192.168.1.100` |
| `REMOTE_HOST` | Hostname клиента | `client.example.com` |

---

## 2. CGI скрипты

### 2.1 Простейший CGI на Shell

```bash
#!/bin/bash
# /var/www/cgi-bin/hello.sh

# Обязательно: Content-Type и пустая строка
echo "Content-Type: text/html"
echo ""

# Тело ответа
cat << EOF
<!DOCTYPE html>
<html>
<head><title>Hello CGI</title></head>
<body>
    <h1>Hello from Shell CGI!</h1>
    <p>Server: $SERVER_NAME</p>
    <p>Method: $REQUEST_METHOD</p>
    <p>Query: $QUERY_STRING</p>
    <p>Time: $(date)</p>
</body>
</html>
EOF

```

### 2.2 CGI на Python

```python
#!/usr/bin/env python3
# /var/www/cgi-bin/hello.py

import os
import sys
from datetime import datetime
from urllib.parse import parse_qs

def main():
    # Получаем данные запроса
    method = os.environ.get('REQUEST_METHOD', 'GET')
    query_string = os.environ.get('QUERY_STRING', '')
    content_type = os.environ.get('CONTENT_TYPE', '')
    content_length = os.environ.get('CONTENT_LENGTH', '0')
    
    # Парсим query string
    params = parse_qs(query_string)
    name = params.get('name', ['World'])[0]
    
    # Читаем тело POST запроса
    body = ''
    if method == 'POST' and content_length:
        body = sys.stdin.read(int(content_length))
    
    # Выводим HTTP ответ
    print("Content-Type: text/html; charset=utf-8")
    print("X-Powered-By: Python CGI")
    print()  # Пустая строка — конец заголовков
    
    # HTML тело
    print(f"""<!DOCTYPE html>
<html>
<head><title>Python CGI</title></head>
<body>
    <h1>Hello, {name}!</h1>
    <h2>Request Info</h2>
    <ul>
        <li>Method: {method}</li>
        <li>Query String: {query_string}</li>
        <li>Content-Type: {content_type}</li>
        <li>Content-Length: {content_length}</li>
    </ul>
    
    <h2>Environment Variables</h2>
    <table border="1">
""")
    
    for key, value in sorted(os.environ.items()):
        if key.startswith(('HTTP_', 'REQUEST_', 'CONTENT_', 'SERVER_', 'SCRIPT_', 'PATH_', 'QUERY_', 'REMOTE_')):
            print(f"        <tr><td><code>{key}</code></td><td>{value}</td></tr>")
    
    print("""    </table>
    
    <h2>Form</h2>
    <form method="POST">
        <input type="text" name="message" placeholder="Enter message">
        <button type="submit">Send POST</button>
    </form>
""")
    
    if body:
        print(f"    <h2>POST Body</h2><pre>{body}</pre>")
    
    print(f"""
    <p><small>Generated at {datetime.now()}</small></p>
</body>
</html>""")


if __name__ == '__main__':
    main()

```

### 2.3 CGI на Perl (классика)

```perl
#!/usr/bin/perl
# /var/www/cgi-bin/hello.pl

use strict;
use warnings;
use CGI;

my $cgi = CGI->new();

print $cgi->header('text/html');
print $cgi->start_html('Perl CGI');
print $cgi->h1('Hello from Perl CGI!');

print $cgi->p("Method: " . $ENV{'REQUEST_METHOD'});
print $cgi->p("Query: " . $ENV{'QUERY_STRING'});

# Получить параметр
my $name = $cgi->param('name') || 'World';
print $cgi->p("Hello, $name!");

print $cgi->end_html();

```

### 2.4 CGI для обработки форм

```python
#!/usr/bin/env python3
# /var/www/cgi-bin/form_handler.py

import os
import sys
import cgi
import cgitb

# Включить отладку (показывает ошибки в браузере)
cgitb.enable()

def main():
    # Парсинг данных формы
    form = cgi.FieldStorage()
    
    # Получение значений
    username = form.getvalue('username', '')
    email = form.getvalue('email', '')
    message = form.getvalue('message', '')
    
    # Обработка загруженного файла
    uploaded_file = None
    if 'file' in form:
        file_item = form['file']
        if file_item.filename:
            uploaded_file = {
                'filename': file_item.filename,
                'type': file_item.type,
                'size': len(file_item.value)
            }
    
    print("Content-Type: text/html; charset=utf-8")
    print()
    
    print(f"""<!DOCTYPE html>
<html>
<head><title>Form Result</title></head>
<body>
    <h1>Form Submitted</h1>
    <p><strong>Username:</strong> {cgi.escape(username)}</p>
    <p><strong>Email:</strong> {cgi.escape(email)}</p>
    <p><strong>Message:</strong> {cgi.escape(message)}</p>
""")
    
    if uploaded_file:
        print(f"""
    <h2>Uploaded File</h2>
    <p>Filename: {cgi.escape(uploaded_file['filename'])}</p>
    <p>Type: {uploaded_file['type']}</p>
    <p>Size: {uploaded_file['size']} bytes</p>
""")
    
    print("""
    <p><a href="javascript:history.back()">Back</a></p>
</body>
</html>""")


if __name__ == '__main__':
    main()

```

---

## 3. Настройка CGI в веб-серверах

### 3.1 Apache CGI

```apache
# /etc/apache2/sites-available/example.conf

<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/html
    
    # Традиционный cgi-bin
    ScriptAlias /cgi-bin/ /var/www/cgi-bin/
    <Directory "/var/www/cgi-bin">
        Options +ExecCGI
        AddHandler cgi-script .cgi .py .pl .sh
        Require all granted
    </Directory>
    
    # Или: CGI в любой директории
    <Directory "/var/www/html">
        Options +ExecCGI
        AddHandler cgi-script .cgi
    </Directory>
</VirtualHost>

```

```bash
# Включить mod_cgi или mod_cgid
sudo a2enmod cgi     # для prefork MPM
sudo a2enmod cgid    # для worker/event MPM
sudo systemctl restart apache2

# Сделать скрипты исполняемыми
chmod +x /var/www/cgi-bin/*.py

```

### 3.2 Nginx CGI (через fcgiwrap)

Nginx не поддерживает CGI напрямую, только через FastCGI wrapper:

```bash
# Установить fcgiwrap
sudo apt install fcgiwrap

# Запустить
sudo systemctl start fcgiwrap
sudo systemctl enable fcgiwrap

```

```nginx
# /etc/nginx/sites-available/example.conf

server {
    listen 80;
    server_name example.com;
    root /var/www/html;
    
    location /cgi-bin/ {
        gzip off;
        root /var/www;
        
        fastcgi_pass unix:/var/run/fcgiwrap.socket;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}

```

---

## 4. Проблемы CGI

### 4.1 Накладные расходы

**Главная проблема CGI: fork() на каждый запрос.**

```

┌────────────────────────────────────────────────────────────┐
│                    CGI Overhead                             │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Request 1:                                                │
│    fork() → exec() → initialize → process → exit           │
│    ────────────────────────────────────────────────        │
│                     ~50-100ms для Python/Perl              │
│                                                            │
│  Request 2:                                                │
│    fork() → exec() → initialize → process → exit           │
│    ────────────────────────────────────────────────        │
│                                                            │
│  Request 3:                                                │
│    fork() → exec() → initialize → process → exit           │
│    ────────────────────────────────────────────────        │
│                                                            │
│  При 100 запросах/сек: 100 процессов, огромные накладные   │
│  расходы на fork(), загрузку интерпретатора, библиотек...  │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 4.2 Сравнение накладных расходов

| Компонент | CGI | FastCGI | mod_php |
|-----------|-----|---------|---------|
| fork() на запрос | Да | Нет | Нет |
| Загрузка интерпретатора | Да | Нет | Нет |
| Инициализация библиотек | Да | Нет | Нет |
| Персистентные соединения к БД | Нет | Да | Да |
| Типичная latency | 50-100ms | 1-10ms | 1-5ms |

### 4.3 Когда CGI всё ещё используется

- Редко вызываемые скрипты (cron задачи через веб)
- Legacy системы
- Простые задачи без высокой нагрузки
- Обучение (понимание основ)
- Системы с ограниченными ресурсами (embedded)

---

## 5. FastCGI

### 5.1 Концепция FastCGI

**FastCGI** решает проблему накладных расходов CGI:

```

┌────────────────────────────────────────────────────────────┐
│                   FastCGI Architecture                      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Web Server          FastCGI Process Manager               │
│       │                      │                             │
│       │    ┌─────────────────┴─────────────────┐           │
│       │    │                                   │           │
│       │    ▼                                   ▼           │
│       │  ┌───────────┐                    ┌───────────┐    │
│       │  │ Worker 1  │                    │ Worker N  │    │
│       │  │ (persistent)                   │ (persistent)   │
│       │  │           │                    │           │    │
│       │  │ - initialized                  │ - initialized  │
│       │  │ - DB connected                 │ - DB connected │
│       │  │ - modules loaded               │ - modules loaded│
│       │  └───────────┘                    └───────────┘    │
│       │        │                                │          │
│       │        │ socket/TCP                     │          │
│       │        │                                │          │
│       └────────┼────────────────────────────────┤          │
│                │                                │          │
│  Request 1 ────┴──► Worker 1 обрабатывает      │          │
│  Request 2 ─────────────────────────────────────┴──►       │
│                      Worker N обрабатывает                 │
│  Request 3 ────────► Worker 1 (уже освободился)           │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

**Ключевые отличия от CGI:**

- Процессы живут постоянно
- Множество запросов обрабатываются одним процессом
- Коммуникация через Unix socket или TCP
- Бинарный протокол (эффективнее)

### 5.2 FastCGI протокол

FastCGI использует бинарные записи (records):

```

┌─────────────────────────────────────────────────────────┐
│                FastCGI Record Format                     │
├─────────────────────────────────────────────────────────┤
│ Version (1)   │ Type (1)     │ Request ID (2)           │
├─────────────────────────────────────────────────────────┤
│ Content Length (2)           │ Padding Length (1)       │
├─────────────────────────────────────────────────────────┤
│ Reserved (1)                                            │
├─────────────────────────────────────────────────────────┤
│ Content Data (variable)                                 │
├─────────────────────────────────────────────────────────┤
│ Padding Data (variable)                                 │
└─────────────────────────────────────────────────────────┘

Типы записей:
  FCGI_BEGIN_REQUEST    (1)  — начало запроса
  FCGI_ABORT_REQUEST    (2)  — отмена запроса
  FCGI_END_REQUEST      (3)  — конец запроса
  FCGI_PARAMS           (4)  — переменные окружения
  FCGI_STDIN            (5)  — тело запроса
  FCGI_STDOUT           (6)  — ответ (тело)
  FCGI_STDERR           (7)  — ошибки
  FCGI_DATA             (8)  — дополнительные данные

```

### 5.3 PHP-FPM (FastCGI Process Manager)

Самое популярное использование FastCGI — PHP-FPM:

```ini

; /etc/php/8.1/fpm/pool.d/www.conf

[www]
user = www-data
group = www-data

; Слушать на Unix socket (рекомендуется)
listen = /run/php/php8.1-fpm.sock
listen.owner = www-data
listen.group = www-data
listen.mode = 0660

; Или на TCP порту
; listen = 127.0.0.1:9000

; Управление процессами
pm = dynamic                ; static, dynamic, ondemand
pm.max_children = 50        ; максимум воркеров
pm.start_servers = 5        ; начальное количество
pm.min_spare_servers = 5    ; минимум свободных
pm.max_spare_servers = 35   ; максимум свободных

; Ограничения
pm.max_requests = 500       ; перезапуск воркера после N запросов

; Логирование
access.log = /var/log/php-fpm/access.log
slowlog = /var/log/php-fpm/slow.log
request_slowlog_timeout = 5s

```

```nginx
# Nginx → PHP-FPM

server {
    listen 80;
    server_name example.com;
    root /var/www/html;
    index index.php index.html;
    
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
    
    location ~ \.php$ {
        # Проверка существования файла
        try_files $uri =404;
        
        # FastCGI параметры
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
        
        # Буферизация
        fastcgi_buffer_size 16k;
        fastcgi_buffers 4 16k;
        
        # Таймауты
        fastcgi_connect_timeout 60;
        fastcgi_send_timeout 180;
        fastcgi_read_timeout 180;
    }
}

```

### 5.4 Python FastCGI

```python
#!/usr/bin/env python3
"""
Python FastCGI сервер с использованием flup.
"""

from flup.server.fcgi import WSGIServer

def application(environ, start_response):
    """WSGI application."""
    
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')
    
    html = f"""<!DOCTYPE html>
<html>
<head><title>Python FastCGI</title></head>
<body>
    <h1>Hello from Python FastCGI!</h1>
    <p>Method: {method}</p>
    <p>Path: {path}</p>
</body>
</html>"""
    
    return [html.encode('utf-8')]

if __name__ == '__main__':
    # Запуск FastCGI сервера
    WSGIServer(application, bindAddress='/tmp/python-fcgi.sock').run()

```

---

## 6. SCGI (Simple CGI)

### 6.1 Что такое SCGI

**SCGI** — упрощённая версия FastCGI с более простым протоколом.

```

┌────────────────────────────────────────────────────────────┐
│                    SCGI Protocol                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Format: <length>:<headers>,<body>                         │
│                                                            │
│  Example:                                                  │
│  70:CONTENT_LENGTH\x0027\x00SCGI\x001\x00REQUEST_METHOD\x00POST\x00,body │
│                                                            │
│  - Length of headers in decimal ASCII                      │
│  - Headers as null-terminated key-value pairs              │
│  - Comma separator                                         │
│  - Request body                                            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 6.2 Сравнение CGI, FastCGI, SCGI

| Аспект | CGI | FastCGI | SCGI |
|--------|-----|---------|------|
| Процесс на запрос | Да | Нет | Нет |
| Протокол | Текст (env vars) | Бинарный | Текст (простой) |
| Сложность | Низкая | Высокая | Средняя |
| Производительность | Низкая | Высокая | Высокая |
| Мультиплексирование | Нет | Да | Нет |
| Поддержка | Везде | Широкая | Ограниченная |

### 6.3 SCGI в Nginx

```nginx

server {
    listen 80;
    server_name example.com;
    
    location / {
        scgi_pass 127.0.0.1:9000;
        include scgi_params;
    }
}

```

---

## 7. Практические примеры

### 7.1 CGI: Гостевая книга

```python
#!/usr/bin/env python3
# /var/www/cgi-bin/guestbook.py

import os
import cgi
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path('/var/www/data/guestbook.json')

def load_entries():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_entries(entries):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(entries, indent=2))

def main():
    form = cgi.FieldStorage()
    
    # Обработка POST
    if os.environ.get('REQUEST_METHOD') == 'POST':
        name = form.getvalue('name', 'Anonymous')
        message = form.getvalue('message', '')
        
        if message:
            entries = load_entries()
            entries.append({
                'name': name,
                'message': message,
                'time': datetime.now().isoformat()
            })
            # Ограничиваем до 100 записей
            save_entries(entries[-100:])
    
    entries = load_entries()
    
    print("Content-Type: text/html; charset=utf-8")
    print()
    
    print("""<!DOCTYPE html>
<html>
<head>
    <title>Guestbook</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .entry { border: 1px solid #ccc; padding: 10px; margin: 10px 0; }
        .entry-header { font-weight: bold; color: #333; }
        .entry-time { font-size: 0.8em; color: #666; }
    </style>
</head>
<body>
    <h1>📖 Guestbook</h1>
    
    <form method="POST">
        <p><input type="text" name="name" placeholder="Your name" style="width: 100%;"></p>
        <p><textarea name="message" placeholder="Your message" rows="4" style="width: 100%;"></textarea></p>
        <p><button type="submit">Post</button></p>
    </form>
    
    <h2>Entries</h2>
""")
    
    for entry in reversed(entries):
        name = cgi.escape(entry['name'])
        message = cgi.escape(entry['message'])
        time = entry['time']
        print(f"""
    <div class="entry">
        <div class="entry-header">{name}</div>
        <div class="entry-time">{time}</div>
        <p>{message}</p>
    </div>""")
    
    print("""
</body>
</html>""")

if __name__ == '__main__':
    main()

```

### 7.2 CGI: Простой API

```python
#!/usr/bin/env python3
# /var/www/cgi-bin/api.py

import os
import sys
import json
import cgi
from datetime import datetime

def json_response(data, status='200 OK'):
    print(f"Status: {status}")
    print("Content-Type: application/json")
    print("Access-Control-Allow-Origin: *")
    print()
    print(json.dumps(data, indent=2))

def main():
    method = os.environ.get('REQUEST_METHOD', 'GET')
    path_info = os.environ.get('PATH_INFO', '')
    
    # Простой роутинг
    if path_info == '/time':
        json_response({
            'time': datetime.now().isoformat(),
            'timestamp': datetime.now().timestamp()
        })
    
    elif path_info == '/echo':
        if method == 'POST':
            content_length = int(os.environ.get('CONTENT_LENGTH', 0))
            body = sys.stdin.read(content_length) if content_length else ''
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                data = body
            json_response({'echo': data})
        else:
            form = cgi.FieldStorage()
            params = {key: form.getvalue(key) for key in form.keys()}
            json_response({'params': params})
    
    elif path_info == '/env':
        env = {k: v for k, v in os.environ.items() 
               if k.startswith(('HTTP_', 'REQUEST_', 'SERVER_', 'CONTENT_'))}
        json_response({'environment': env})
    
    else:
        json_response({
            'error': 'Not Found',
            'path': path_info,
            'available': ['/time', '/echo', '/env']
        }, '404 Not Found')

if __name__ == '__main__':
    main()

```

### 7.3 FastCGI: Python Application Server

```python
#!/usr/bin/env python3
"""
FastCGI application server с роутингом.
"""

import json
import os
from datetime import datetime

# Счётчик запросов (персистентный между запросами!)
request_count = 0

def application(environ, start_response):
    global request_count
    request_count += 1
    
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')
    
    # Роутинг
    if path == '/':
        return index(environ, start_response)
    elif path == '/api/info':
        return api_info(environ, start_response)
    elif path == '/api/stats':
        return api_stats(environ, start_response)
    else:
        return not_found(environ, start_response)

def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    html = f"""<!DOCTYPE html>
<html>
<head><title>FastCGI App</title></head>
<body>
    <h1>FastCGI Application</h1>
    <p>This process has handled {request_count} requests.</p>
    <p>Process PID: {os.getpid()}</p>
    <ul>
        <li><a href="/api/info">API Info</a></li>
        <li><a href="/api/stats">API Stats</a></li>
    </ul>
</body>
</html>"""
    return [html.encode()]

def api_info(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    data = {
        'server': 'Python FastCGI',
        'pid': os.getpid(),
        'time': datetime.now().isoformat(),
        'environ': {k: v for k, v in environ.items() if isinstance(v, str)}
    }
    return [json.dumps(data, indent=2).encode()]

def api_stats(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    data = {
        'request_count': request_count,
        'pid': os.getpid()
    }
    return [json.dumps(data, indent=2).encode()]

def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'application/json')])
    return [json.dumps({'error': 'Not Found'}).encode()]

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(application).run()

```

---

## 8. Отладка CGI

### 8.1 Распространённые проблемы

```bash
# 1. Права на выполнение
chmod +x script.py

# 2. Правильный shebang
#!/usr/bin/env python3  # не #!/usr/bin/python

# 3. Правильные окончания строк (Unix LF, не Windows CRLF)
dos2unix script.py

# 4. Проверка синтаксиса
python3 -m py_compile script.py

# 5. Логирование ошибок
# Apache: /var/log/apache2/error.log
# Nginx: /var/log/nginx/error.log
tail -f /var/log/apache2/error.log

```

### 8.2 Тестирование CGI из командной строки

```bash
# Симуляция GET запроса
REQUEST_METHOD=GET \
QUERY_STRING="name=John&age=30" \
SERVER_NAME=localhost \
./script.py

# Симуляция POST запроса
echo "name=John&message=Hello" | \
REQUEST_METHOD=POST \
CONTENT_TYPE="application/x-www-form-urlencoded" \
CONTENT_LENGTH=24 \
./script.py

```

### 8.3 cgitb для отладки Python

```python
#!/usr/bin/env python3

import cgitb
cgitb.enable()  # Показывает трейсбеки в браузере

# Теперь ошибки будут отображаться в HTML
```

---

## 💡 Key Takeaways

- **CGI** — первый стандарт для динамического контента, новый процесс на каждый запрос

- **FastCGI** — персистентные процессы, значительно эффективнее

- **SCGI** — упрощённый FastCGI, легче в реализации

- **PHP-FPM** — самая распространённая реализация FastCGI для PHP
- CGI всё ещё используется для низконагруженных задач
- Переменные окружения — основной способ передачи данных в CGI

---

## 🚀 Next Steps

**Related Modules:**

- [WSGI](../05_WSGI/) — Python Web Server Gateway Interface
- [ASGI](../06_ASGI/) — Асинхронный ASGI

**Practice Ideas:**

1. Напишите CGI скрипт для обработки форм
2. Настройте PHP-FPM с Nginx
3. Сравните производительность CGI и FastCGI с помощью ab
4. Создайте простой REST API на CGI

**Going Deeper:**

- RFC 3875 (CGI/1.1)
- FastCGI Specification
- PHP-FPM configuration tuning

---

## 📚 Additional Resources

**Specifications:**

- [RFC 3875](https://tools.ietf.org/html/rfc3875) — CGI/1.1
- [FastCGI Specification](https://fastcgi-archives.github.io/FastCGI_Specification.html)

**Documentation:**

- [PHP-FPM](https://www.php.net/manual/en/install.fpm.php)
- [Apache mod_cgi](https://httpd.apache.org/docs/current/mod/mod_cgi.html)
- [Nginx FastCGI](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html)

---




