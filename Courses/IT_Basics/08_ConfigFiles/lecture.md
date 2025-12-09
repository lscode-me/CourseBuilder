# Конфигурационные файлы
## INI, TOML, .env и Linux-специфичные форматы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать JSON и YAML (модули 05, 06)
- Понимать переменные окружения
- Иметь опыт работы с приложениями и их настройками

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с INI файлами и понимать их применение в systemd
- Использовать TOML для современных конфигураций
- Управлять переменными окружения через .env файлы
- Понимать Linux-специфичные форматы: passwd, sshd_config, fstab, nginx
- Выбирать подходящий формат конфигурации для разных задач

---

## 1. Обзор форматов конфигурации

### 1.1 Эволюция форматов

```
Универсальные форматы:
1980s     1990s      2000s      2010s      2020s
INI  →  XML  →  JSON  →  YAML  →  TOML
                              ↓
                           .env (параллельно)

Linux/UNIX форматы (с 1970-х, актуальны до сих пор):
passwd, group → sshd_config, sudoers → systemd units → nginx/apache
    (DSV)         (keyword-value)        (INI)         (блочный)
```

### 1.2 Сравнение форматов

**Универсальные форматы (кроссплатформенные):**

| Формат | Комментарии | Вложенность | Типы данных | Применение |
|--------|-------------|-------------|-------------|------------|
| INI | `;` или `#` | Секции | Строки | Windows, Git, systemd |
| TOML | `#` | Таблицы | Да | Rust, Python |
| .env | `#` | Нет | Строки | Docker, Node.js |
| JSON | Нет | Полная | Да | API, Web |
| YAML | `#` | Полная | Да | DevOps |

**Linux-специфичные форматы:**

| Формат | Комментарии | Разделитель | Применение |
|--------|-------------|-------------|------------|
| Colon-separated | Нет | `:` | passwd, group, shadow |
| Keyword-value | `#` | Пробелы | sshd_config, sudoers |
| Space-separated | `#` | Пробелы/табы | fstab, hosts |
| Apache-style | `#` | Блоки `<>` | httpd.conf, nginx |
| Shell-style | `#` | `=` | /etc/environment, profile |

---

## 2. INI файлы

### 2.1 Формат INI

**INI** (Initialization) — один из старейших форматов конфигурации, появившийся в MS-DOS и ранних версиях Windows. Несмотря на возраст, формат остаётся популярным благодаря своей простоте и читаемости. INI файлы используются в Git (`.gitconfig`), PHP (`php.ini`), MySQL (`my.cnf`), и многих других приложениях.

```ini
; Это комментарий
# Это тоже комментарий

[section]
key = value
another_key = another value

[database]
host = localhost
port = 5432
username = admin
; password хранится в переменных окружения

[server]
debug = true
max_connections = 100
```

### 2.2 Правила INI

Формат INI не имеет строгой спецификации, поэтому разные парсеры могут интерпретировать его по-разному. Однако основные правила одинаковы везде:

- **Секции** в квадратных скобках `[section]`
- **Пары ключ-значение**: `key = value`
- **Комментарии**: `;` или `#`
- **Значения** — всегда строки (парсер может конвертировать в типы)
- **Нет вложенности** (только секции, но некоторые реализации поддерживают `[parent.child]`)

### 2.3 INI в Python

```python
import configparser

# Чтение
config = configparser.ConfigParser()
config.read('config.ini')

# Доступ к значениям
host = config['database']['host']
port = config.getint('database', 'port')
debug = config.getboolean('server', 'debug')

print(f"Database: {host}:{port}")

# Запись
config['new_section'] = {
    'key1': 'value1',
    'key2': 'value2'
}

with open('config.ini', 'w') as f:
    config.write(f)
```

### 2.4 Примеры INI

```ini
; .gitconfig
[user]
    name = John Doe
    email = john@example.com

[core]
    editor = vim
    autocrlf = input

[alias]
    st = status
    co = checkout
    br = branch
```

```ini
; php.ini
[PHP]
engine = On
memory_limit = 128M
max_execution_time = 30

[Date]
date.timezone = Europe/Moscow
```

### 2.5 INI в systemd

**systemd** — система инициализации в современных Linux-дистрибутивах — использует расширенный INI-формат для своих unit-файлов. Это одно из самых важных применений INI в современном Linux. Все сервисы, таймеры, точки монтирования и другие единицы systemd описываются в этом формате.

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Service
Documentation=https://example.com/docs
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/server --config /etc/myapp/config.toml
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
EnvironmentFile=-/etc/myapp/env

[Install]
WantedBy=multi-user.target
```

**Особенности systemd INI:**

- Секции `[Unit]`, `[Service]`, `[Install]` — стандартные для сервисов
- Поддержка переменных: `$MAINPID`, `%u` (user), `%h` (home)
- Списки через пробелы или повторение ключей
- Префикс `-` означает "игнорировать ошибку" (например, `-/etc/myapp/env`)

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup timer

[Timer]
OnCalendar=daily
Persistent=true
RandomizedDelaySec=1h

[Install]
WantedBy=timers.target
```

---

## 3. TOML

### 3.1 Что такое TOML

**TOML** (Tom's Obvious Minimal Language) — современный формат конфигураций.

- Создан Томом Престон-Вернером (GitHub)
- Очевидный синтаксис
- Поддержка типов данных
- Стандарт для Rust (Cargo.toml), Python (pyproject.toml)

### 3.2 Синтаксис TOML

```toml
# Это комментарий

# Базовые типы
title = "TOML Example"
enabled = true
count = 42
price = 19.99
date = 2024-01-15
datetime = 2024-01-15T10:30:00Z

# Строки
simple = "Hello"
multiline = """
First line
Second line"""
literal = 'C:\path\to\file'

# Массивы
numbers = [1, 2, 3]
mixed = ["string", 42, true]
nested = [[1, 2], [3, 4]]

# Таблицы (объекты)
[server]
host = "localhost"
port = 8080

[database]
host = "db.example.com"
port = 5432
username = "admin"

# Вложенные таблицы
[database.pool]
min = 5
max = 20

# Массив таблиц
[[users]]
name = "Alice"
role = "admin"

[[users]]
name = "Bob"
role = "user"
```

### 3.3 TOML в Python

```python
# Встроенный модуль (Python 3.11+)
import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

print(config['server']['host'])
print(config['users'][0]['name'])

# Для записи используйте toml или tomli-w
import tomli_w

with open('output.toml', 'wb') as f:
    tomli_w.dump(config, f)
```

### 3.4 pyproject.toml

```toml
[project]
name = "myproject"
version = "1.0.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Author", email = "author@example.com"}
]
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
]

[project.scripts]
myapp = "myproject:main"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### 3.5 Cargo.toml (Rust)

```toml
[package]
name = "myapp"
version = "0.1.0"
edition = "2021"
authors = ["Author <author@example.com>"]

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[[bin]]
name = "myapp"
path = "src/main.rs"
```

---

## 4. .env файлы

### 4.1 Формат .env

```bash
# .env файл
# Комментарии начинаются с #

DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=your-secret-key-here
DEBUG=true

# Кавычки опциональны
API_KEY="key-with-spaces and special=chars"

# Многострочные значения
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
-----END RSA PRIVATE KEY-----"
```

### 4.2 Правила .env

- **Формат**: `KEY=value`
- **Комментарии**: `#`
- **Кавычки**: опциональны (нужны для пробелов)
- **Нет секций** — плоская структура
- **НЕ коммитить в Git** — добавить в .gitignore

### 4.3 .env в Python

```python
# С библиотекой python-dotenv
from dotenv import load_dotenv
import os

# Загрузка .env файла
load_dotenv()  # Ищет .env в текущей директории
# или
load_dotenv('/path/to/.env')

# Использование
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG', 'false').lower() == 'true'
port = int(os.getenv('PORT', '8080'))

print(f"Connecting to {database_url}")
```

### 4.4 .env и Docker

```yaml
# docker-compose.yml
services:
  app:
    image: myapp
    env_file:
      - .env
    environment:
      - EXTRA_VAR=value  # Дополнительные переменные
```

```dockerfile
# Dockerfile
# НЕ копируйте .env в образ!
ENV NODE_ENV=production
```

### 4.5 Пример структуры

```
project/
├── .env              # Локальные секреты (в .gitignore)
├── .env.example      # Шаблон (в Git)
├── .env.production   # Production настройки
└── .env.test         # Тестовые настройки
```

```bash
# .env.example
DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=change-me-in-production
DEBUG=true
```

---

## 5. Properties файлы (Java)

### 5.1 Формат

```properties
# application.properties
app.name=MyApp
app.version=1.0.0

# База данных
database.host=localhost
database.port=5432
database.username=admin

# Экранирование
path.windows=C:\\Program Files\\App
unicode=\u0041\u0042\u0043

# Многострочные
long.text=This is a very long \
    line that continues here
```

### 5.2 Properties в Python

```python
import jproperties

p = jproperties.Properties()

with open('app.properties', 'rb') as f:
    p.load(f)

# Доступ к значениям
name = p['app.name'].data
port = int(p['database.port'].data)
```

---

## 6. Linux-специфичные форматы

Linux исторически использует множество собственных форматов конфигурации, которые отличаются от универсальных форматов (JSON, YAML, INI). Эти форматы оптимизированы для конкретных задач и часто существуют с ранних версий UNIX.

### 6.1 Colon-separated values (DSV)

**Delimiter-separated values** — формат, где поля разделены двоеточием (`:`). Это один из древнейших форматов UNIX, используемый для системных баз данных. Формат очень компактный и эффективный для машинной обработки, хотя менее читаемый для человека.

```bash
# /etc/passwd — база пользователей
# username:password:UID:GID:GECOS:home:shell
root:x:0:0:root:/root:/bin/bash
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
john:x:1000:1000:John Doe:/home/john:/bin/bash
```

**Поля `/etc/passwd`:**
1. Имя пользователя
2. Пароль (`x` = в /etc/shadow)
3. UID — числовой идентификатор
4. GID — группа по умолчанию
5. GECOS — полное имя и комментарий
6. Домашняя директория
7. Shell при входе

```bash
# /etc/group — база групп
# groupname:password:GID:members
root:x:0:
wheel:x:10:john,admin
docker:x:998:john,deploy
```

```bash
# /etc/shadow — хеши паролей (только root)
# username:hash:lastchange:min:max:warn:inactive:expire:reserved
john:$6$rounds=5000$salt$hash...:19500:0:99999:7:::
```

**Парсинг в Python:**

```python
# Чтение /etc/passwd
def parse_passwd():
    users = []
    with open('/etc/passwd') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                fields = line.strip().split(':')
                users.append({
                    'username': fields[0],
                    'uid': int(fields[2]),
                    'gid': int(fields[3]),
                    'gecos': fields[4],
                    'home': fields[5],
                    'shell': fields[6]
                })
    return users

# Или через стандартный модуль
import pwd
import grp

user = pwd.getpwnam('john')
print(f"{user.pw_name}: UID={user.pw_uid}, home={user.pw_dir}")

group = grp.getgrnam('docker')
print(f"{group.gr_name}: members={group.gr_mem}")
```

### 6.2 Keyword-argument формат

**Keyword-argument** (или keyword-value) — формат, где каждая строка содержит директиву и её значение, разделённые пробелами. Этот формат широко используется в конфигурациях безопасности и сетевых сервисов. Он поддерживает сложные многострочные блоки и условную логику.

```bash
# /etc/ssh/sshd_config — конфигурация SSH сервера
# Основные настройки безопасности
Port 22
AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::

# Аутентификация
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no

# Ограничения
MaxAuthTries 3
MaxSessions 10
ClientAliveInterval 300
ClientAliveCountMax 2

# Подсистемы
Subsystem sftp /usr/lib/openssh/sftp-server

# Условные блоки — применяются к определённым пользователям/группам
Match User deploy
    PasswordAuthentication no
    AllowTcpForwarding no
    X11Forwarding no
    ForceCommand /usr/local/bin/deploy-only.sh

Match Group developers
    AllowTcpForwarding yes
    PermitTunnel yes
```

**Особенности формата:**

- Директива и значение разделены пробелами
- Регистронезависимые ключевые слова
- `Match` — условные блоки (применяются до следующего Match или конца файла)
- Нет кавычек для строк с пробелами (используется контекст)

```bash
# /etc/sudoers — права sudo
# Формат: user/group host=(runas) commands

# Пользователь admin может всё
admin ALL=(ALL:ALL) ALL

# Группа wheel может всё с паролем
%wheel ALL=(ALL:ALL) ALL

# Deploy без пароля только для systemctl
deploy ALL=(root) NOPASSWD: /bin/systemctl restart myapp, /bin/systemctl status myapp

# Defaults — глобальные настройки
Defaults    env_reset
Defaults    mail_badpass
Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"
Defaults    timestamp_timeout=15
```

> ⚠️ **Важно**: Редактируйте `/etc/sudoers` только через `visudo` — он проверяет синтаксис перед сохранением!

### 6.3 Space-separated табличный формат

Ряд системных файлов Linux использует табличный формат с разделением пробелами или табуляцией. Каждая строка — запись, колонки имеют фиксированное значение. Комментарии начинаются с `#`.

```bash
# /etc/fstab — таблица монтирования файловых систем
# <device>                                <mount>   <type>  <options>        <dump> <pass>
UUID=a1b2c3d4-...                         /         ext4    defaults         1      1
UUID=e5f6g7h8-...                         /home     ext4    defaults         1      2
UUID=i9j0k1l2-...                         none      swap    sw               0      0
/dev/sdb1                                 /data     xfs     defaults,noatime 0      2

# NFS монтирование
192.168.1.100:/exports/shared             /mnt/nfs  nfs     defaults,_netdev 0      0

# tmpfs в памяти
tmpfs                                     /tmp      tmpfs   defaults,noatime,mode=1777 0 0
```

**Колонки fstab:**
1. Устройство (UUID, LABEL, путь или сетевой адрес)
2. Точка монтирования
3. Тип файловой системы
4. Опции монтирования (через запятую)
5. dump — для утилиты backup (обычно 0)
6. pass — порядок проверки fsck (0 = не проверять)

```bash
# /etc/hosts — статические DNS записи
127.0.0.1       localhost
127.0.1.1       myserver.local myserver
::1             localhost ip6-localhost

# Локальные сервисы
192.168.1.10    db.local postgres
192.168.1.20    redis.local cache
192.168.1.30    api.local backend

# Блокировка рекламы/трекеров
0.0.0.0         ads.example.com
0.0.0.0         tracker.example.com
```

```bash
# /etc/crypttab — зашифрованные устройства
# <name>    <device>                        <keyfile>       <options>
crypthome   UUID=xxxx-yyyy                  /etc/keys/home  luks
cryptdata   /dev/disk/by-id/ata-Samsung...  none            luks,discard
```

### 6.4 Apache/Nginx-style (блочный формат)

Конфигурации веб-серверов используют блочный формат с директивами и вложенными блоками в фигурных скобках или XML-подобных тегах. Этот формат позволяет описывать сложные иерархии: виртуальные хосты, locations, условия.

```apache
# /etc/apache2/sites-available/mysite.conf
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/example

    <Directory /var/www/example>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    # Логи
    ErrorLog ${APACHE_LOG_DIR}/example-error.log
    CustomLog ${APACHE_LOG_DIR}/example-access.log combined

    # Редирект на HTTPS
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    DocumentRoot /var/www/example

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/example.pem
    SSLCertificateKeyFile /etc/ssl/private/example.key
</VirtualHost>
```

```nginx
# /etc/nginx/sites-available/mysite.conf
server {
    listen 80;
    server_name example.com www.example.com;
    
    # Редирект на HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/example.pem;
    ssl_certificate_key /etc/ssl/private/example.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    root /var/www/example;
    index index.html index.php;

    # Статика с кешированием
    location /static/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # API прокси
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # PHP
    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php8.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

### 6.5 Shell-style переменные

Многие Linux-конфигурации используют синтаксис shell-переменных — это позволяет их напрямую source'ить в shell-скриптах. Формат простой: `KEY=value` или `export KEY=value`.

```bash
# /etc/environment — системные переменные окружения
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
LANG="en_US.UTF-8"
EDITOR="vim"
```

```bash
# /etc/default/grub — конфигурация загрузчика
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="Ubuntu"
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
GRUB_DISABLE_OS_PROBER=false
```

```bash
# /etc/default/docker или /etc/sysconfig/docker
DOCKER_OPTS="--storage-driver=overlay2"
DOCKER_NETWORK_OPTIONS="--ip-forward=true"
```

```bash
# ~/.bashrc, ~/.profile — пользовательские настройки
export PATH="$HOME/.local/bin:$PATH"
export EDITOR="vim"
export VISUAL="code"

# Алиасы
alias ll='ls -alF'
alias la='ls -A'
alias grep='grep --color=auto'

# Функции
mkcd() {
    mkdir -p "$1" && cd "$1"
}
```

**Загрузка в скриптах:**

```bash
#!/bin/bash
# Загрузка конфигурации
if [ -f /etc/default/myapp ]; then
    source /etc/default/myapp
fi

# Использование переменных
echo "Starting with port: ${MYAPP_PORT:-8080}"
```

### 6.6 Crontab формат

**crontab** — специальный формат для планирования задач. Каждая строка содержит расписание (5 полей времени) и команду. Формат компактный, но требует привыкания.

```bash
# crontab -e
# Формат: минута час день месяц день_недели команда
#         0-59   0-23 1-31 1-12  0-7 (0,7=воскресенье)

# Каждый день в 3:00
0 3 * * * /usr/local/bin/backup.sh

# Каждые 15 минут
*/15 * * * * /usr/local/bin/check-health.sh

# Каждый понедельник в 9:00
0 9 * * 1 /usr/local/bin/weekly-report.sh

# Первого числа каждого месяца в полночь
0 0 1 * * /usr/local/bin/monthly-cleanup.sh

# Каждый будний день в 8:30
30 8 * * 1-5 /usr/local/bin/workday-start.sh

# Специальные строки
@reboot /usr/local/bin/on-startup.sh
@daily /usr/local/bin/daily-task.sh
@weekly /usr/local/bin/weekly-task.sh
@monthly /usr/local/bin/monthly-task.sh
@hourly /usr/local/bin/hourly-task.sh

# Переменные окружения
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@example.com
```

**Специальные символы:**
- `*` — любое значение
- `*/n` — каждые n единиц
- `n,m` — конкретные значения
- `n-m` — диапазон

---

## 7. Сравнение и выбор формата

### 7.1 Таблица выбора

| Сценарий | Рекомендуемый формат |
|----------|---------------------|
| Секреты, credentials | .env |
| Python проект | pyproject.toml |
| Rust проект | Cargo.toml |
| DevOps, K8s | YAML |
| Git конфигурация | INI |
| systemd сервисы | INI (unit files) |
| API, веб | JSON |
| Простые настройки | INI или TOML |
| Linux системные файлы | Специфичные форматы |

### 7.2 Конвертация

```python
# INI → JSON
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

data = {s: dict(config[s]) for s in config.sections()}
print(json.dumps(data, indent=2))
```

---

## 8. Best Practices

### 8.1 Безопасность

```bash
# .gitignore
.env
*.pem
*_secret*
config/local.toml
```

### 8.2 Структура конфигурации

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # С дефолтами
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    PORT = int(os.getenv('PORT', '8080'))
    
    # Обязательные
    DATABASE_URL = os.environ['DATABASE_URL']  # Падает если нет
    SECRET_KEY = os.environ['SECRET_KEY']
```

### 8.3 Валидация конфигурации

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8080
    
    class Config:
        env_file = '.env'

settings = Settings()  # Автоматическая валидация
```

---

## 💡 Key Takeaways

- **INI — простой, но живой формат**: Используется в Git, PHP, systemd. Секции, строковые значения, расширения в разных реализациях.

- **TOML — современный стандарт**: Типы данных, читаемость, pyproject.toml, Cargo.toml.

- **.env — для секретов**: Переменные окружения, НЕ коммитить в Git.

- **Linux-форматы разнообразны**: Colon-separated (/etc/passwd), keyword-value (sshd_config), табличные (fstab), блочные (nginx). Каждый оптимизирован для своей задачи.

- **Знание man-страниц критично**: `man 5 passwd`, `man sshd_config`, `man fstab` — всегда актуальная документация.

- **Выбор формата**: Python → TOML, DevOps → YAML, секреты → .env, Linux системное → специфичные форматы.

---

## 🚀 Next Steps

**Practice Ideas:**
1. Создайте pyproject.toml для своего Python проекта
2. Настройте .env для Docker Compose приложения
3. Напишите скрипт конвертации INI → TOML
4. Создайте systemd unit файл для своего сервиса
5. Изучите `/etc/passwd` и `/etc/group` на своей системе с помощью Python
6. Настройте sshd_config для повышения безопасности SSH

---

## 📚 Additional Resources

**Форматы:**
- [TOML Specification](https://toml.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

**Linux man-страницы (секция 5 — форматы файлов):**
- `man 5 passwd` — формат /etc/passwd
- `man 5 shadow` — формат /etc/shadow
- `man 5 fstab` — таблица файловых систем
- `man 5 hosts` — формат /etc/hosts
- `man sshd_config` — конфигурация SSH сервера
- `man 5 sudoers` — формат файла sudoers
- `man 5 crontab` — формат crontab
- `man systemd.unit` — формат unit-файлов systemd

---


