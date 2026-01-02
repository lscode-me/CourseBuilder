# Web Servers
## Apache, Nginx, и эволюция веб-серверов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP протокол
- Знать основы работы с сокетами
- Иметь опыт работы с Linux/Unix системами

**Recommended prior modules:**

- [HTTP Protocol](../01_HTTP/) — структура HTTP
- [Socket Activation](../02_SocketActivation/) — обработка соединений

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать историю развития веб-серверов
- Различать архитектуры Apache (prefork/worker/event) и Nginx
- Настраивать базовую конфигурацию основных веб-серверов
- Выбирать подходящий веб-сервер для задачи
- Понимать концепции reverse proxy и load balancing

---

## 1. История веб-серверов

### 1.1 Timeline развития

```
1990 ─── CERN httpd (первый веб-сервер, Tim Berners-Lee)
   │
1991 ─── NCSA HTTPd
   │
1995 ─── Apache HTTP Server (из патчей к NCSA)
   │
1996 ─── Microsoft IIS
   │
2002 ─── Lighttpd (lighty)
   │
2004 ─── Nginx (Igor Sysoev, Rambler)
   │
2005 ─── Cherokee
   │
2014 ─── OpenBSD httpd (rewrite на OpenBSD)
   │
2015 ─── Caddy (автоматический HTTPS)
   │
2016 ─── H2O (HTTP/2 оптимизированный)
   │
2019 ─── Caddy 2.0
```

### 1.2 Доля рынка (исторически)

```
┌────────────────────────────────────────────────────────────┐
│               Web Server Market Share                      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  2000s:  [Apache ████████████████████████████ 70%]         │
│          [IIS    ████████ 20%]                             │
│          [Other  ██ 10%]                                   │
│                                                            │
│  2010s:  [Apache ██████████████████ 50%]                   │
│          [Nginx  ████████████ 30%]                         │
│          [IIS    ████ 10%]                                 │
│          [Other  ██ 10%]                                   │
│                                                            │
│  2020s:  [Nginx  ██████████████████████ 35%]               │
│          [Apache ██████████████ 25%]                       │
│          [Cloudflare ████████ 15%]                         │
│          [Other  ██████████████ 25%]                       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 2. Apache HTTP Server

### 2.1 История и архитектура

**Apache** появился в 1995 году как "a patchy server" — набор патчей к NCSA HTTPd.

Ключевые особенности:

- Модульная архитектура
- Множество MPM (Multi-Processing Modules)
- .htaccess для per-directory конфигурации
- Огромная экосистема модулей

### 2.2 MPM (Multi-Processing Modules)

```
┌────────────────────────────────────────────────────────────┐
│                   Apache MPM Types                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  PREFORK MPM (традиционный)                                │
│  ┌─────────┐                                               │
│  │ Master  │                                               │
│  │ Process │                                               │
│  └────┬────┘                                               │
│       │ fork()                                             │
│       ├────────────┬────────────┬────────────┐             │
│       ▼            ▼            ▼            ▼             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Worker  │  │ Worker  │  │ Worker  │  │ Worker  │        │
│  │Process 1│  │Process 2│  │Process 3│  │Process N│        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
│  1 conn/proc  1 conn/proc  1 conn/proc  1 conn/proc        │
│                                                            │
│  WORKER MPM (гибридный)                                    │
│  ┌─────────┐                                               │
│  │ Master  │                                               │
│  └────┬────┘                                               │
│       │                                                    │
│       ├─────────────────┬─────────────────┐                │
│       ▼                 ▼                 ▼                │
│  ┌─────────┐       ┌─────────┐       ┌─────────┐           │
│  │ Process │       │ Process │       │ Process │           │
│  │ Thread1 │       │ Thread1 │       │ Thread1 │           │
│  │ Thread2 │       │ Thread2 │       │ Thread2 │           │
│  │ ...     │       │ ...     │       │ ...     │           │
│  │ ThreadN │       │ ThreadN │       │ ThreadN │           │
│  └─────────┘       └─────────┘       └─────────┘           │
│                                                            │
│  EVENT MPM (современный, асинхронный)                      │
│  ┌─────────┐                                               │
│  │ Master  │                                               │
│  └────┬────┘                                               │
│       │                                                    │
│       ├─────────────────┬─────────────────┐                │
│       ▼                 ▼                 ▼                │
│  ┌─────────┐       ┌─────────┐       ┌─────────┐           │
│  │ Process │       │ Process │       │ Process │           │
│  │ Listener│       │ Listener│       │ Listener│           │
│  │ +Threads│       │ +Threads│       │ +Threads│           │
│  │ +async  │       │ +async  │       │ +async  │           │
│  │ keep-al │       │ keep-al │       │ keep-al │           │
│  └─────────┘       └─────────┘       └─────────┘           │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

| MPM | Описание | Когда использовать |
|-----|----------|-------------------|
| **prefork** | Один процесс = одно соединение | С mod_php, не thread-safe код |
| **worker** | Процессы с потоками | Высокая нагрузка, thread-safe |
| **event** | async для keep-alive | Много keep-alive соединений |

### 2.3 Конфигурация Apache

```apache
# /etc/apache2/apache2.conf (Debian/Ubuntu)
# /etc/httpd/httpd.conf (RHEL/CentOS)

# Глобальные настройки
ServerRoot "/etc/apache2"
Listen 80
Listen 443

# Загрузка модулей
LoadModule ssl_module modules/mod_ssl.so
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule proxy_module modules/mod_proxy.so

# MPM настройки (event)
<IfModule mpm_event_module>
    StartServers             3
    MinSpareThreads         75
    MaxSpareThreads        250
    ThreadsPerChild         25
    MaxRequestWorkers      400
    MaxConnectionsPerChild   0
</IfModule>

# Основной хост
ServerAdmin webmaster@example.com
ServerName www.example.com

# Директория по умолчанию
DocumentRoot "/var/www/html"
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

# Логирование
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

# Включить конфигурации сайтов
IncludeOptional sites-enabled/*.conf
```

### 2.4 Виртуальные хосты

```apache
# /etc/apache2/sites-available/example.com.conf

<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    
    DocumentRoot /var/www/example.com/public
    
    <Directory /var/www/example.com/public>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    # Логи
    ErrorLog ${APACHE_LOG_DIR}/example.com-error.log
    CustomLog ${APACHE_LOG_DIR}/example.com-access.log combined
    
    # Редирект на HTTPS
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com
    
    DocumentRoot /var/www/example.com/public
    
    # SSL
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
    
    # Современные SSL настройки
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLCipherSuite ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256
    SSLHonorCipherOrder off
    
    # HSTS
    Header always set Strict-Transport-Security "max-age=63072000"
</VirtualHost>
```

### 2.5 .htaccess

```apache
# /var/www/example.com/public/.htaccess

# Включить rewrite
RewriteEngine On

# Перенаправление на www
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Pretty URLs (убрать .php)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]

# Защита чувствительных файлов
<FilesMatch "^\.">
    Require all denied
</FilesMatch>

<Files "config.php">
    Require all denied
</Files>

# Кэширование
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
</IfModule>

# Сжатие
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>
```

### 2.6 Управление Apache

```bash
# Debian/Ubuntu
sudo apt install apache2
sudo systemctl start apache2
sudo systemctl enable apache2
sudo a2ensite example.com.conf
sudo a2enmod rewrite ssl headers
sudo apache2ctl configtest
sudo systemctl reload apache2

# RHEL/CentOS
sudo yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo httpd -t
sudo systemctl reload httpd

# Проверка
apachectl -M  # список модулей
apachectl -S  # список виртуальных хостов
```

---

## 3. Nginx

### 3.1 История и философия

**Nginx** (произносится "engine-x") создан Igor Sysoev в 2004 году для решения проблемы C10K — обработки 10000+ одновременных соединений.

Ключевые отличия от Apache:

- **Event-driven** архитектура (не процесс/поток на соединение)
- Малое потребление памяти
- Высокая производительность на статике
- Отличный reverse proxy
- Нет .htaccess (вся конфигурация централизована)

### 3.2 Архитектура Nginx

```
┌────────────────────────────────────────────────────────────┐
│                    Nginx Architecture                      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   Master Process                     │  │
│  │  - Reads config                                     │   │
│  │  - Binds ports                                      │   │
│  │  - Manages workers                                  │   │
│  └────────────────────────┬────────────────────────────┘   │
│                           │                                │
│          ┌────────────────┼────────────────┐               │
│          │                │                │               │
│          ▼                ▼                ▼               │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐     │
│  │    Worker     │ │    Worker     │ │    Worker     │     │
│  │    Process    │ │    Process    │ │    Process    │     │
│  │               │ │               │ │               │     │
│  │  event loop   │ │  event loop   │ │  event loop   │     │
│  │  ┌─────────┐  │ │  ┌─────────┐  │ │  ┌─────────┐  │     │
│  │  │ conn 1  │  │ │  │ conn 4  │  │ │  │ conn 7  │  │     │
│  │  │ conn 2  │  │ │  │ conn 5  │  │ │  │ conn 8  │  │     │
│  │  │ conn 3  │  │ │  │ conn 6  │  │ │  │ conn 9  │  │     │
│  │  │ ...     │  │ │  │ ...     │  │ │  │ ...     │  │     │
│  │  │ conn N  │  │ │  │ conn M  │  │ │  │ conn K  │  │     │
│  │  └─────────┘  │ │  └─────────┘  │ │  └─────────┘  │     │
│  └───────────────┘ └───────────────┘ └───────────────┘     │
│                                                            │
│  Каждый worker: один поток, тысячи соединений (epoll/kqueue│
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 3.3 Конфигурация Nginx

```nginx
# /etc/nginx/nginx.conf

user www-data;
worker_processes auto;  # = количество CPU
pid /run/nginx.pid;

# Подключение модулей
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 1024;  # соединений на worker
    use epoll;  # Linux (kqueue на BSD)
    multi_accept on;
}

http {
    # Базовые настройки
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    server_tokens off;  # скрыть версию nginx
    
    # MIME типы
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    # Логирование
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    # Сжатие
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css application/json application/javascript 
               text/xml application/xml application/xml+rss text/javascript;
    
    # Виртуальные хосты
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

### 3.4 Виртуальный хост (server block)

```nginx
# /etc/nginx/sites-available/example.com

# HTTP → HTTPS редирект
server {
    listen 80;
    listen [::]:80;
    server_name example.com www.example.com;
    
    return 301 https://$server_name$request_uri;
}

# Основной HTTPS сервер
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name example.com www.example.com;
    
    root /var/www/example.com/public;
    index index.html index.php;
    
    # SSL
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;
    
    # Современные протоколы
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;
    
    # HSTS
    add_header Strict-Transport-Security "max-age=63072000" always;
    
    # Безопасность
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    
    # Логи
    access_log /var/log/nginx/example.com.access.log;
    error_log /var/log/nginx/example.com.error.log;
    
    # Статические файлы с кэшированием
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|pdf|txt)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Обработка PHP через FastCGI
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
    
    # Главный location
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
    
    # Запретить доступ к скрытым файлам
    location ~ /\. {
        deny all;
    }
}
```

### 3.5 Nginx как Reverse Proxy

```nginx
# Проксирование на backend приложение

upstream backend {
    # Round-robin по умолчанию
    server 127.0.0.1:8080 weight=3;
    server 127.0.0.1:8081;
    server 127.0.0.1:8082 backup;
    
    # Альтернативные алгоритмы:
    # least_conn;        # наименьшее число соединений
    # ip_hash;           # sticky sessions по IP
    # hash $request_uri; # по URI
    
    keepalive 32;  # keep-alive соединения к backend
}

server {
    listen 80;
    server_name api.example.com;
    
    location / {
        proxy_pass http://backend;
        
        # Заголовки для backend
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Таймауты
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
        
        # Буферизация
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 8 4k;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

### 3.6 Управление Nginx

```bash
# Установка
sudo apt install nginx  # Debian/Ubuntu
sudo yum install nginx  # RHEL/CentOS
pkg_add nginx           # OpenBSD

# Управление
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl reload nginx  # перечитать конфиг без даунтайма
sudo systemctl restart nginx

# Проверка конфигурации
sudo nginx -t

# Сигналы напрямую
sudo nginx -s reload
sudo nginx -s reopen  # переоткрыть логи
sudo nginx -s quit    # graceful shutdown
sudo nginx -s stop    # немедленная остановка
```

---

## 4. Apache vs Nginx

### 4.1 Сравнительная таблица

| Аспект | Apache | Nginx |
|--------|--------|-------|
| **Архитектура** | Процесс/поток на соединение | Event-driven, асинхронный |
| **Память** | Больше (особенно prefork) | Меньше, предсказуемо |
| **Статика** | Хорошо | Отлично |
| **Динамика** | Встроенный mod_php | Требует FastCGI |
| **.htaccess** | Да | Нет |
| **Конфигурация** | Распределённая | Централизованная |
| **Модули** | Runtime загрузка | Компиляция (до 1.9.11) |
| **Reverse Proxy** | Хорошо | Отлично |
| **Документация** | Обширная | Хорошая |

### 4.2 Когда что использовать

**Apache лучше когда:**

- Нужен .htaccess (shared hosting)
- Используется mod_php
- Сложные rewrite правила
- Требуется совместимость со старыми конфигурациями

**Nginx лучше когда:**

- Высокая нагрузка, много соединений
- В основном статический контент
- Reverse proxy / load balancer
- Ограниченные ресурсы (VPS)
- WebSocket проксирование

### 4.3 Гибридная архитектура

```
┌────────────────────────────────────────────────────────────┐
│               Nginx + Apache Architecture                  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Internet                                                  │
│     │                                                      │
│     ▼                                                      │
│  ┌─────────────────────────────────┐                       │
│  │            Nginx                 │                      │
│  │   - SSL termination             │                       │
│  │   - Static files                │                       │
│  │   - Caching                     │                       │
│  │   - Load balancing              │                       │
│  └───────────────┬─────────────────┘                       │
│                  │                                         │
│                  │ proxy_pass                              │
│                  ▼                                         │
│  ┌─────────────────────────────────┐                       │
│  │           Apache                │                       │
│  │   - mod_php                     │                       │
│  │   - .htaccess                   │                       │
│  │   - Dynamic content             │                       │
│  └─────────────────────────────────┘                       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 5. OpenBSD httpd

### 5.1 Философия

**OpenBSD httpd** — минималистичный веб-сервер, входящий в базовую систему OpenBSD. Переписан с нуля (не форк) с фокусом на безопасность.

Особенности:

- Privilege separation
- chroot по умолчанию
- Минимум функций (делает одно, но хорошо)
- Простая конфигурация

### 5.2 Конфигурация

```
# /etc/httpd.conf

# Основные настройки
prefork 3

# Типы контента
types {
    include "/usr/share/misc/mime.types"
}

# HTTP сервер
server "example.com" {
    listen on * port 80
    
    # Редирект на HTTPS
    location "/*" {
        block return 301 "https://$HTTP_HOST$REQUEST_URI"
    }
}

# HTTPS сервер
server "example.com" {
    listen on * tls port 443
    
    root "/htdocs/example.com"
    
    # TLS
    tls {
        certificate "/etc/ssl/example.com.fullchain.pem"
        key "/etc/ssl/private/example.com.key"
    }
    
    # Логи
    log {
        access "example.com-access.log"
        error "example.com-error.log"
    }
    
    # Статические файлы
    location "/static/*" {
        root "/htdocs/example.com"
        pass
    }
    
    # FastCGI для PHP
    location "*.php" {
        fastcgi socket "/run/php-fpm.sock"
    }
    
    # Все остальное
    location "/*" {
        pass
    }
}
```

### 5.3 Управление

```bash
# Проверка конфигурации
httpd -n

# Запуск
rcctl start httpd
rcctl enable httpd

# Перезагрузка
rcctl reload httpd
```

---

## 6. Другие веб-серверы

### 6.1 Caddy

**Caddy** — современный веб-сервер с автоматическим HTTPS (Let's Encrypt).

```
# Caddyfile

example.com {
    root * /var/www/example.com
    file_server
    
    # Автоматический HTTPS включён по умолчанию!
    
    # Reverse proxy
    reverse_proxy /api/* localhost:8080
    
    # PHP
    php_fastcgi unix//run/php-fpm.sock
    
    # Логи
    log {
        output file /var/log/caddy/example.com.log
    }
}
```

**Преимущества Caddy:**

- Автоматический HTTPS (Let's Encrypt)
- Простой синтаксис конфигурации
- Автоматические редиректы HTTP→HTTPS
- HTTP/2 и HTTP/3 по умолчанию
- Один бинарник, нет зависимостей

### 6.2 Lighttpd (lighty)

**Lighttpd** — лёгкий веб-сервер, оптимизированный для высоконагруженных сред.

```
# /etc/lighttpd/lighttpd.conf

server.modules = (
    "mod_access",
    "mod_fastcgi",
    "mod_rewrite"
)

server.document-root = "/var/www/html"
server.port = 80

# FastCGI
fastcgi.server = (
    ".php" => ((
        "socket" => "/var/run/php-fpm.sock"
    ))
)
```

**Когда использовать:**

- Встраиваемые системы
- Высокая нагрузка на статику
- Ограниченные ресурсы

### 6.3 H2O

**H2O** — ультра-быстрый HTTP/2 сервер от DeNA (Япония).

```yaml
# h2o.conf

hosts:
  "example.com":
    listen:
      port: 443
      ssl:
        certificate-file: /etc/ssl/cert.pem
        key-file: /etc/ssl/key.pem
    paths:
      "/":
        file.dir: /var/www/html
```

**Особенности:**

- Оптимизирован для HTTP/2
- Server push
- Очень низкие задержки

### 6.4 LiteSpeed

**LiteSpeed** — коммерческий веб-сервер, совместимый с Apache .htaccess.

**Особенности:**

- Drop-in замена Apache
- Поддержка .htaccess
- Встроенный PHP (LSAPI)
- Отличная производительность
- Используется многими хостинг-провайдерами

### 6.5 Traefik

**Traefik** — современный reverse proxy для микросервисов.

```yaml
# traefik.yml

entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

providers:
  docker:
    exposedByDefault: false

certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: /letsencrypt/acme.json
      httpChallenge:
        entryPoint: web
```

**Особенности:**

- Автоматическое обнаружение сервисов (Docker, Kubernetes)
- Автоматический HTTPS
- Dashboard
- Метрики (Prometheus)

### 6.6 Сводная таблица

| Сервер | Сильные стороны | Слабые стороны | Когда использовать |
|--------|----------------|----------------|-------------------|
| **Apache** | Модули, .htaccess, документация | Память, сложность | Legacy, shared hosting |
| **Nginx** | Производительность, reverse proxy | Нет .htaccess, динамика | High traffic, CDN, proxy |
| **OpenBSD httpd** | Безопасность, простота | Минимум функций | OpenBSD, безопасность |
| **Caddy** | Auto HTTPS, простота | Новый, меньше экосистема | Простые сайты, dev |
| **Lighttpd** | Лёгкий, быстрый | Меньше функций | Embedded, статика |
| **H2O** | HTTP/2, скорость | Меньше сообщество | Максимальная скорость |
| **LiteSpeed** | Apache-совместимость | Коммерческий | cPanel hosting |
| **Traefik** | Микросервисы, auto-discovery | Сложность | Docker, Kubernetes |

---

## 7. Практические примеры

### 7.1 Статический сайт с Nginx

```nginx
server {
    listen 80;
    server_name static.example.com;
    
    root /var/www/static;
    index index.html;
    
    # Кэширование
    location ~* \.(css|js|png|jpg|gif|ico|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # HTML без кэширования
    location ~* \.html$ {
        expires -1;
        add_header Cache-Control "no-store";
    }
    
    # Сжатие
    gzip on;
    gzip_types text/css application/javascript;
    
    # SPA fallback
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### 7.2 Load Balancer

```nginx
upstream app_servers {
    least_conn;
    
    server 10.0.0.1:8080 weight=3;
    server 10.0.0.2:8080 weight=2;
    server 10.0.0.3:8080;
    server 10.0.0.4:8080 backup;
    
    keepalive 32;
}

server {
    listen 80;
    server_name app.example.com;
    
    location / {
        proxy_pass http://app_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        
        # Health check endpoint
        proxy_next_upstream error timeout http_500 http_502 http_503;
        proxy_next_upstream_tries 3;
    }
    
    location /health {
        access_log off;
        return 200 "OK\n";
    }
}
```

### 7.3 SSL/TLS конфигурация (современная)

```nginx
# /etc/nginx/snippets/ssl-params.conf

ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

ssl_session_timeout 1d;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;

# OCSP Stapling
ssl_stapling on;
ssl_stapling_verify on;
resolver 1.1.1.1 8.8.8.8 valid=300s;
resolver_timeout 5s;

# Security headers
add_header Strict-Transport-Security "max-age=63072000" always;
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

---

## 💡 Key Takeaways

- **Apache** — модульный, гибкий, с .htaccess, но потребляет больше ресурсов

- **Nginx** — event-driven, эффективный для статики и reverse proxy

- **OpenBSD httpd** — минималистичный, безопасный, идеален для OpenBSD

- **Caddy** — автоматический HTTPS, простая конфигурация
- Комбинируйте: Nginx для статики + Apache/backend для динамики
- Выбор сервера зависит от задачи, нагрузки и экосистемы

---

## 🚀 Next Steps

**Related Modules:**

- [CGI](../04_CGI/) — Gateway интерфейсы
- [WSGI](../05_WSGI/) — Python Web Server Gateway Interface

**Practice Ideas:**

1. Настройте Nginx как reverse proxy для Python приложения
2. Сконфигурируйте SSL с Let's Encrypt
3. Настройте load balancing между несколькими backend серверами
4. Сравните производительность Apache и Nginx с помощью `ab` или `wrk`

**Going Deeper:**

- nginx.org documentation
- Apache mod_rewrite guide
- SSL Labs best practices

---

## 📚 Additional Resources

**Documentation:**

- [nginx.org](https://nginx.org/en/docs/)
- [Apache HTTP Server](https://httpd.apache.org/docs/)
- [OpenBSD httpd.conf(5)](https://man.openbsd.org/httpd.conf.5)
- [Caddy Documentation](https://caddyserver.com/docs/)

**Tools:**

- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- [SSL Labs Server Test](https://www.ssllabs.com/ssltest/)
- [ab](https://httpd.apache.org/docs/current/programs/ab.html) — Apache Benchmark
- [wrk](https://github.com/wg/wrk) — HTTP benchmarking tool

---




