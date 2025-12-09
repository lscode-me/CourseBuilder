# Services
## Системные службы и демоны в OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [Basic Commands](../03_BasicCommands/) и [User Management](../05_UserManagement/)
- Понимать процессы и демоны Unix
- Уметь работать с doas

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Управлять службами через rcctl
- Понимать систему rc.d
- Настраивать автозапуск служб
- Создавать собственные rc.d скрипты
- Конфигурировать популярные демоны
- Мониторить работу служб

---

## 1. Система инициализации rc

### 1.1 Обзор rc

OpenBSD использует простую систему инициализации на основе shell-скриптов:

```
Загрузка → /etc/rc → /etc/rc.d/* → /etc/rc.local
                         ↓
              /etc/rc.conf.local (настройки)
```

### 1.2 Основные файлы

| Файл | Назначение |
|------|------------|
| `/etc/rc` | Главный скрипт инициализации |
| `/etc/rc.conf` | Настройки по умолчанию (не редактировать!) |
| `/etc/rc.conf.local` | Локальные настройки служб |
| `/etc/rc.d/` | Скрипты управления службами |
| `/etc/rc.local` | Локальные команды запуска |
| `/etc/rc.shutdown` | Команды при выключении |

### 1.3 Просмотр служб

```sh
# Все доступные службы
$ ls /etc/rc.d/
apmd        ftpproxy    ntpd        smtpd       unbound
bgpd        httpd       ospfd       snmpd       vmd
cron        iked        pflogd      spamd       watchdogd
dhcpd       inetd       ppp         sshd        ...

# Службы базовой системы
$ ls /etc/rc.d/ | wc -l
42
```

---

## 2. rcctl — управление службами

### 2.1 Основные команды

```sh
# Включить службу (автозапуск)
# doas rcctl enable sshd

# Выключить службу (убрать из автозапуска)
# doas rcctl disable httpd

# Запустить службу
# doas rcctl start sshd

# Остановить службу
# doas rcctl stop httpd

# Перезапустить
# doas rcctl restart sshd

# Перечитать конфигурацию
# doas rcctl reload nginx

# Проверить статус
$ doas rcctl check sshd
sshd(ok)

# Получить все настройки службы
$ rcctl get sshd
sshd_class=daemon
sshd_flags=
sshd_logger=
sshd_rtable=0
sshd_timeout=30
sshd_user=root
```

### 2.2 Просмотр состояния

```sh
# Статус всех служб
$ rcctl ls all
apmd
bgpd(disabled)
cron
dhcpd(disabled)
httpd(disabled)
ntpd
pflogd
sshd
...

# Только запущенные
$ rcctl ls started
cron
ntpd
pflogd
sshd

# Только включённые (автозапуск)
$ rcctl ls on
cron
ntpd
pflogd
sshd

# Выключенные
$ rcctl ls off
httpd
nginx
smtpd
```

### 2.3 Настройка параметров службы

```sh
# Установить флаги запуска
# doas rcctl set httpd flags "-f /etc/httpd.custom.conf"

# Установить пользователя
# doas rcctl set myservice user _myapp

# Установить таймаут
# doas rcctl set slowservice timeout 60

# Просмотреть флаги
$ rcctl get httpd flags
httpd_flags=-f /etc/httpd.custom.conf
```

---

## 3. Файл rc.conf.local

### 3.1 Формат

```sh
# /etc/rc.conf.local

# Включить службу
sshd_flags=""
ntpd_flags="-s"
httpd_flags=""

# Выключенные службы (не запускать)
smtpd_flags=NO

# Пакетные службы
pkg_scripts="nginx php82_fpm redis"
```

### 3.2 Порядок запуска

Службы запускаются в порядке, определённом в `pkg_scripts` или по зависимостям в rc.d скриптах.

```sh
# Указать порядок
pkg_scripts="mysqld php82_fpm nginx"
```

---

## 4. Структура rc.d скриптов

### 4.1 Базовый шаблон

```sh
#!/bin/ksh

daemon="/usr/local/sbin/myapp"
daemon_user="_myapp"
daemon_flags=""

. /etc/rc.d/rc.subr

rc_cmd $1
```

### 4.2 Расширенный шаблон

```sh
#!/bin/ksh

daemon="/usr/local/bin/myapp"
daemon_user="_myapp"
daemon_flags="-c /etc/myapp.conf"

# Файл PID (если не стандартный)
pexp="/usr/local/bin/myapp.*"

# Зависимости
rc_pre() {
    # Проверки перед запуском
    if [ ! -f /etc/myapp.conf ]; then
        echo "Config not found"
        return 1
    fi
}

rc_post() {
    # Действия после остановки
    rm -f /var/run/myapp.sock
}

. /etc/rc.d/rc.subr

rc_cmd $1
```

### 4.3 Переменные rc.subr

| Переменная | Описание |
|------------|----------|
| `daemon` | Путь к исполняемому файлу |
| `daemon_user` | Пользователь для запуска |
| `daemon_flags` | Аргументы командной строки |
| `daemon_class` | Класс login.conf |
| `daemon_rtable` | Таблица маршрутизации |
| `daemon_timeout` | Таймаут для start/stop |
| `pexp` | Pattern для поиска процесса |

---

## 5. Популярные службы

### 5.1 sshd

```sh
# Конфигурация: /etc/ssh/sshd_config

# Включить и запустить
# doas rcctl enable sshd
# doas rcctl start sshd

# Проверить конфигурацию
# doas sshd -t

# Перезапустить после изменения конфигурации
# doas rcctl restart sshd
```

### 5.2 httpd (встроенный веб-сервер)

```sh
# /etc/httpd.conf
server "example.com" {
    listen on * port 80
    root "/htdocs/example.com"
    
    location "/.well-known/acme-challenge/*" {
        root "/acme"
        request strip 2
    }
}

# Включить
# doas rcctl enable httpd
# doas rcctl start httpd

# Проверить конфигурацию
# doas httpd -n
```

### 5.3 smtpd (почтовый сервер)

```sh
# /etc/mail/smtpd.conf
listen on lo0
listen on egress tls pki mail.example.com

action "local" mbox
action "relay" relay

match from local for local action "local"
match from local for any action "relay"

# Включить
# doas rcctl enable smtpd
# doas rcctl start smtpd
```

### 5.4 ntpd (синхронизация времени)

```sh
# /etc/ntpd.conf
servers pool.ntp.org
sensor *

# Флаги для немедленной синхронизации при старте
# doas rcctl set ntpd flags "-s"
# doas rcctl enable ntpd
# doas rcctl start ntpd
```

### 5.5 unbound (DNS resolver)

```sh
# /var/unbound/etc/unbound.conf
server:
    interface: 127.0.0.1
    interface: ::1
    access-control: 0.0.0.0/0 refuse
    access-control: 127.0.0.0/8 allow
    access-control: ::1 allow
    
    hide-identity: yes
    hide-version: yes

# Включить
# doas rcctl enable unbound
# doas rcctl start unbound
```

---

## 6. Пакетные службы

### 6.1 Установка и настройка nginx

```sh
# Установить
# doas pkg_add nginx

# Конфигурация: /etc/nginx/nginx.conf

# Включить
# doas rcctl enable nginx
# doas rcctl start nginx

# Проверить
$ doas rcctl check nginx
nginx(ok)
```

### 6.2 PHP-FPM

```sh
# Установить
# doas pkg_add php-8.2

# Конфигурация: /etc/php-fpm.conf
# Пул: /etc/php-8.2.d/

# Включить
# doas rcctl enable php82_fpm
# doas rcctl start php82_fpm
```

### 6.3 MariaDB/MySQL

```sh
# Установить
# doas pkg_add mariadb-server

# Инициализация
# doas mysql_install_db

# Включить
# doas rcctl enable mysqld
# doas rcctl start mysqld

# Безопасная настройка
# doas mysql_secure_installation
```

### 6.4 PostgreSQL

```sh
# Установить
# doas pkg_add postgresql-server

# Инициализация
# doas su - _postgresql
$ initdb -D /var/postgresql/data -U postgres -A scram-sha-256 -E UTF8 -W
$ exit

# Включить
# doas rcctl enable postgresql
# doas rcctl start postgresql
```

---

## 7. Мониторинг служб

### 7.1 Проверка статуса

```sh
# Проверить все службы
for s in $(rcctl ls on); do
    rcctl check $s
done

# Проверить конкретную
$ doas rcctl check nginx
nginx(ok)

$ doas rcctl check httpd
httpd(failed)
```

### 7.2 Логирование

```sh
# Системные логи
$ tail -f /var/log/messages
$ tail -f /var/log/daemon

# Логи служб
$ tail -f /var/log/nginx/error.log
$ tail -f /var/www/logs/error.log
```

### 7.3 Автоматический перезапуск

Используйте cron для проверки и перезапуска:

```sh
# /etc/cron.d/check_services
*/5 * * * * root rcctl check nginx || rcctl restart nginx
```

---

## 8. Создание собственной службы

### 8.1 Пример: простое приложение

```sh
# 1. Создать системного пользователя
# doas useradd -r -d /var/empty -s /sbin/nologin _myapp

# 2. Создать rc.d скрипт
# doas vi /etc/rc.d/myapp
```

```sh
#!/bin/ksh

daemon="/usr/local/bin/myapp"
daemon_user="_myapp"
daemon_flags="-c /etc/myapp.conf"

. /etc/rc.d/rc.subr

rc_cmd $1
```

```sh
# 3. Сделать исполняемым
# doas chmod 755 /etc/rc.d/myapp

# 4. Включить
# doas rcctl enable myapp
# doas rcctl start myapp
```

### 8.2 Пример: приложение с зависимостями

```sh
#!/bin/ksh

daemon="/usr/local/bin/webapp"
daemon_user="_webapp"

rc_pre() {
    # Проверить, что PostgreSQL запущен
    rcctl check postgresql || return 1
    
    # Проверить конфигурацию
    [ -f /etc/webapp.conf ] || return 1
}

rc_start() {
    ${rcexec} "${daemon} ${daemon_flags}"
}

. /etc/rc.d/rc.subr

rc_cmd $1
```

---

## 9. Практические примеры

### 9.1 LEMP Stack (Linux→OpenBSD, nginx, MariaDB, PHP)

```sh
# Установка
# doas pkg_add nginx php-8.2 php-mysqli-8.2 mariadb-server

# Настройка nginx с PHP
# /etc/nginx/nginx.conf
server {
    listen 80;
    root /var/www/htdocs;
    index index.php index.html;
    
    location ~ \.php$ {
        fastcgi_pass unix:/run/php-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}

# Включить службы
# doas rcctl enable nginx php82_fpm mysqld
# doas rcctl start nginx php82_fpm mysqld
```

### 9.2 Почтовый сервер (smtpd + dovecot)

```sh
# Установить Dovecot
# doas pkg_add dovecot

# Настроить smtpd
# /etc/mail/smtpd.conf
listen on lo0
listen on egress tls pki mail.example.com

action "local_mail" lmtp "/var/dovecot/lmtp" rcpt-to virtual <vusers>
action "outbound" relay

match from local for local action "local_mail"
match from any for domain "example.com" action "local_mail"
match from local for any action "outbound"

# Включить
# doas rcctl enable smtpd dovecot
# doas rcctl start smtpd dovecot
```

---

## 10. Устранение проблем

### 10.1 Служба не запускается

```sh
# Проверить синтаксис конфигурации
# doas nginx -t
# doas httpd -n
# doas smtpd -n

# Запустить вручную с отладкой
# doas -u _nginx nginx -g "daemon off;"

# Проверить логи
$ tail -50 /var/log/messages
$ tail -50 /var/log/daemon
```

### 10.2 Служба падает после запуска

```sh
# Проверить права на файлы
$ ls -la /var/run/nginx.pid
$ ls -la /var/www/

# Проверить лимиты
$ ulimit -a

# Проверить процесс
$ ps aux | grep nginx
```

### 10.3 Служба не отвечает

```sh
# Проверить, слушает ли порт
$ netstat -an | grep LISTEN | grep 80

# Проверить файрвол
# doas pfctl -sr | grep 80

# Проверить соединение локально
$ nc -vz localhost 80
```

---

## 💡 Key Takeaways

- **rcctl**: Единая команда для управления всеми службами
- **rc.conf.local**: Все локальные настройки в одном файле
- **pkg_scripts**: Порядок запуска пакетных служб
- **Простота**: rc.d скрипты — обычные shell-скрипты
- **Логи**: Всегда проверяйте /var/log/messages и daemon

---

## 🚀 Next Steps

**Related Modules:**
- [Security](../10_Security/) — безопасность служб
- [System Admin](../11_SystemAdmin/) — мониторинг и логи

**Practice Ideas:**
1. Настройте LEMP стек для веб-приложения
2. Создайте rc.d скрипт для своего приложения
3. Настройте мониторинг служб через cron
4. Настройте почтовый сервер smtpd

**Going Deeper:**
- Кластеризация служб с CARP
- Мониторинг с Prometheus/Grafana
- Автоматизация с Ansible

---

## 📚 Additional Resources

**Documentation:**
- [man rcctl](https://man.openbsd.org/rcctl) — управление службами
- [man rc.d](https://man.openbsd.org/rc.d) — формат скриптов
- [man rc.conf](https://man.openbsd.org/rc.conf) — конфигурация rc
- [man httpd.conf](https://man.openbsd.org/httpd.conf) — веб-сервер
- [man smtpd.conf](https://man.openbsd.org/smtpd.conf) — почтовый сервер

---

