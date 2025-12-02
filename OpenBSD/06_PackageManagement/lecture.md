# Package Management
## Управление пакетами в OpenBSD: pkg_add и система портов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модули [Installation](../02_Installation/) и [Basic Commands](../03_BasicCommands/)
- Иметь настроенное сетевое подключение
- Понимать использование doas

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Устанавливать и удалять пакеты через pkg_add
- Обновлять установленные пакеты
- Искать пакеты и получать информацию о них
- Понимать систему портов и когда её использовать
- Собирать программы из портов
- Управлять зависимостями и flavors

---

## 1. Система пакетов OpenBSD

### 1.1 Обзор

OpenBSD имеет две системы установки ПО:

| Система | Описание | Когда использовать |
|---------|----------|-------------------|
| **pkg_add** | Бинарные пакеты | Повседневное использование |
| **Ports** | Сборка из исходников | Кастомизация, свежие версии |

### 1.2 Настройка зеркала

```sh
# Установить URL зеркала
# doas echo "https://cdn.openbsd.org/pub/OpenBSD" > /etc/installurl

# Или использовать ближайшее зеркало
# doas echo "https://ftp.eu.openbsd.org/pub/OpenBSD" > /etc/installurl
```

**Список зеркал:** https://www.openbsd.org/ftp.html

### 1.3 PKG_PATH

Альтернативно можно использовать переменную окружения:

```sh
# Для текущей сессии
$ export PKG_PATH=https://cdn.openbsd.org/pub/OpenBSD/$(uname -r)/packages/$(uname -m)/

# Проверить
$ echo $PKG_PATH
https://cdn.openbsd.org/pub/OpenBSD/7.4/packages/amd64/
```

---

## 2. Установка пакетов

### 2.1 pkg_add

```sh
# Установить пакет
# doas pkg_add vim

quirks-7.14 signed on 2023-10-05T12:00:00Z
vim-9.0.1897-no_x11: ok

# Установить несколько пакетов
# doas pkg_add git curl wget htop

# Установить конкретную версию
# doas pkg_add vim-9.0.1897-no_x11

# Интерактивный выбор (если несколько вариантов)
# doas pkg_add vim
Ambiguous: choose package for vim
a       0: <None>
        1: vim-9.0.1897-gtk3
        2: vim-9.0.1897-no_x11
Your choice: 2
```

### 2.2 Flavors (варианты пакетов)

Многие пакеты имеют варианты (flavors):

```sh
# Пример: vim с GUI и без
vim-9.0.1897-no_x11   # без X11
vim-9.0.1897-gtk3     # с GTK3

# Python с разными версиями
python-3.10.13
python-3.11.6

# Firefox ESR и обычный
firefox-119.0
firefox-esr-115.4.0
```

```sh
# Установить конкретный flavor
# doas pkg_add vim--no_x11

# Или указать полное имя
# doas pkg_add vim-9.0.1897-no_x11
```

### 2.3 Зависимости

pkg_add автоматически устанавливает зависимости:

```sh
# doas pkg_add git
git-2.42.0:libcurl-8.4.0: ok
git-2.42.0:p5-Error-0.17029: ok
git-2.42.0:p5-Authen-SASL-2.16p0: ok
git-2.42.0: ok
```

---

## 3. Обновление пакетов

### 3.1 pkg_add -u

```sh
# Обновить все пакеты
# doas pkg_add -u

quirks-7.15 signed on 2023-11-01T12:00:00Z
vim-9.0.1897-no_x11->vim-9.0.2000-no_x11: ok
curl-8.4.0->curl-8.5.0: ok

# Обновить конкретный пакет
# doas pkg_add -u vim
```

### 3.2 Автоматические обновления

```sh
# Создать скрипт для cron
# doas vi /etc/daily.local

pkg_add -u 2>&1 | mail -s "Package updates" root

# Или через crontab
# doas crontab -e
0 3 * * * /usr/sbin/pkg_add -u >/dev/null 2>&1
```

> **⚠️ Warning:**  
> Автоматические обновления могут сломать систему. Лучше обновлять вручную и проверять changelog.

---

## 4. Удаление пакетов

### 4.1 pkg_delete

```sh
# Удалить пакет
# doas pkg_delete vim

# Удалить пакет и его зависимости
# doas pkg_delete -a vim

# Удалить неиспользуемые зависимости
# doas pkg_delete -a
```

### 4.2 Очистка

```sh
# Удалить все пакеты-сироты (без зависящих)
# doas pkg_delete -a

# Удалить кэш загруженных пакетов
# doas rm -rf /var/cache/pkg/*
```

---

## 5. Поиск и информация

### 5.1 pkg_info

```sh
# Список установленных пакетов
$ pkg_info
bash-5.2.15         GNU Bourne Again Shell
curl-8.4.0          get files from FTP, Gopher, HTTP or HTTPS servers
git-2.42.0          distributed version control system
...

# Информация о пакете
$ pkg_info vim
Information for vim-9.0.1897-no_x11

Comment: vi clone, many additional features

Description:
Vim is an almost compatible version of the UNIX editor vi.
...

# Файлы пакета
$ pkg_info -L vim | head
Information for vim-9.0.1897-no_x11

Files:
/usr/local/bin/ex
/usr/local/bin/rview
/usr/local/bin/rvim
/usr/local/bin/vi
/usr/local/bin/view
/usr/local/bin/vim
...

# Какому пакету принадлежит файл
$ pkg_info -E /usr/local/bin/vim
vim-9.0.1897-no_x11
```

### 5.2 Поиск пакетов

```sh
# Поиск в установленных
$ pkg_info | grep python
python-3.10.13      interpreted object-oriented programming language

# Поиск в репозитории
$ pkg_info -Q vim
vim-9.0.1897-gtk3
vim-9.0.1897-no_x11

# Поиск по описанию
$ pkg_info -Q editor
ed-1.19             text editor
joe-4.6p0           Joe's Own Editor
nano-7.2            pico clone with enhancements
vim-9.0.1897-gtk3   vi clone, many additional features
vim-9.0.1897-no_x11 vi clone, many additional features
...
```

### 5.3 Зависимости

```sh
# Зависимости пакета
$ pkg_info -f vim | grep @depend
@depend :gettext-runtime-*:gettext-runtime-0.22.3
@depend :libiconv-*:libiconv-1.17

# Что зависит от пакета
$ pkg_info -R curl
Information for curl-8.4.0

Required by:
git-2.42.0
wget-1.21.4
```

---

## 6. Система портов

### 6.1 Что такое порты

**Ports** — система сборки ПО из исходников с автоматическим управлением зависимостями.

```
/usr/ports/
├── archivers/      # архиваторы
├── databases/      # базы данных
├── devel/          # разработка
├── editors/        # редакторы
├── games/          # игры
├── lang/           # языки программирования
├── mail/           # почта
├── net/            # сетевые утилиты
├── security/       # безопасность
├── sysutils/       # системные утилиты
├── www/            # веб
└── ...
```

### 6.2 Установка портов

```sh
# Скачать дерево портов
$ cd /tmp
$ ftp https://cdn.openbsd.org/pub/OpenBSD/$(uname -r)/ports.tar.gz

# Распаковать
# doas tar -xzf ports.tar.gz -C /usr

# Или через cvs (для -current)
# cd /usr
# doas cvs -qd anoncvs@anoncvs.openbsd.org:/cvs checkout -P ports
```

### 6.3 Сборка из портов

```sh
# Перейти в каталог порта
$ cd /usr/ports/editors/vim

# Посмотреть информацию
$ make show=COMMENT
vi clone, many additional features

# Скачать исходники
# doas make fetch

# Собрать
# doas make build

# Создать пакет
# doas make package

# Установить
# doas make install

# Всё вместе
# doas make install clean
```

### 6.4 Flavors и subpackages в портах

```sh
# Просмотр доступных flavors
$ cd /usr/ports/editors/vim
$ make show=FLAVORS
no_x11 gtk3 huge

# Сборка с определённым flavor
# doas env FLAVOR=no_x11 make install clean

# Subpackages
$ cd /usr/ports/databases/postgresql
$ make show=SUBPACKAGES
postgresql-client postgresql-server postgresql-contrib
```

### 6.5 Обновление портов

```sh
# Обновить дерево портов
$ cd /usr/ports
# doas cvs -q up -Pd

# Или пересказать архив
# Скачать новый ports.tar.gz и распаковать
```

---

## 7. pkg vs ports

### 7.1 Когда использовать pkg_add

✅ **Используйте pkg_add когда:**
- Нужна стандартная конфигурация
- Важна скорость установки
- Хотите стабильность
- Не нужны специфические опции сборки

### 7.2 Когда использовать ports

✅ **Используйте ports когда:**
- Нужны специфические опции компиляции
- Пакет отсутствует в бинарном репозитории
- Нужна самая свежая версия
- Изучаете как собирается ПО

### 7.3 Смешивание pkg и ports

> **⚠️ Warning:**  
> Не смешивайте pkg и ports для одних и тех же пакетов! Это может привести к конфликтам. Если собрали из ports — обновляйте из ports.

---

## 8. Практические примеры

### 8.1 Установка веб-стека

```sh
# Nginx
# doas pkg_add nginx

# PHP
# doas pkg_add php-8.2

# MariaDB
# doas pkg_add mariadb-server mariadb-client

# Включить службы
# doas rcctl enable nginx php82_fpm mysqld
# doas rcctl start nginx php82_fpm mysqld
```

### 8.2 Установка окружения разработчика

```sh
# Git и инструменты
# doas pkg_add git git-lfs

# Python
# doas pkg_add python-3.11 py3-pip

# Node.js
# doas pkg_add node

# Компиляторы
# doas pkg_add gcc llvm

# Редакторы
# doas pkg_add vim--no_x11 nano
```

### 8.3 Установка графического окружения

```sh
# X.org уже в системе если выбрали x* sets

# Оконный менеджер
# doas pkg_add cwm       # простой WM из OpenBSD
# doas pkg_add i3        # тайловый WM
# doas pkg_add xfce      # полноценный DE

# Терминал и утилиты
# doas pkg_add xterm st
# doas pkg_add dmenu rofi

# Браузер
# doas pkg_add firefox
```

### 8.4 Сборка с кастомными опциями

```sh
# Пример: сборка nginx с дополнительными модулями
$ cd /usr/ports/www/nginx

# Посмотреть доступные flavors
$ make show=FLAVORS
lua naxsi passenger slice stream

# Собрать с нужными опциями
# doas env FLAVOR="lua stream" make install clean
```

---

## 9. Устранение проблем

### 9.1 Ошибки при установке

```sh
# Принудительная переустановка
# doas pkg_add -r vim

# Игнорировать зависимости (опасно!)
# doas pkg_add -D installed vim
```

### 9.2 Проверка целостности

```sh
# Проверить установленные пакеты
# doas pkg_check

# Исправить повреждённые
# doas pkg_check -f
```

### 9.3 Откат к предыдущей версии

```sh
# Скачать старую версию
$ ftp https://cdn.openbsd.org/pub/OpenBSD/7.3/packages/amd64/vim-9.0.1500-no_x11.tgz

# Установить
# doas pkg_add -D installed vim-9.0.1500-no_x11.tgz
```

---

## 10. Полезные команды

### 10.1 Шпаргалка pkg_*

```sh
# Установка
pkg_add name            # установить пакет
pkg_add -u              # обновить все
pkg_add -u name         # обновить конкретный

# Удаление
pkg_delete name         # удалить пакет
pkg_delete -a           # удалить orphans

# Информация
pkg_info                # список установленных
pkg_info name           # информация о пакете
pkg_info -L name        # файлы пакета
pkg_info -E /path/file  # найти пакет по файлу
pkg_info -Q search      # поиск в репозитории
pkg_info -f name        # зависимости
pkg_info -R name        # обратные зависимости

# Прочее
pkg_check               # проверить целостность
```

### 10.2 Полезные скрипты

```sh
# Найти пакет, предоставляющий файл
$ cat ~/bin/pkg_search
#!/bin/sh
pkg_info -E "$1" 2>/dev/null || echo "Not found"

# Обновить с логированием
$ cat ~/bin/pkg_update
#!/bin/sh
doas pkg_add -u 2>&1 | tee /var/log/pkg_update.log
```

---

## 💡 Key Takeaways

- **/etc/installurl**: Основной способ указать зеркало пакетов
- **pkg_add -u**: Обновление всех пакетов одной командой
- **Flavors**: Разные варианты одного пакета (с GUI / без GUI)
- **Ports**: Используйте только когда нужна кастомизация
- **Не смешивайте**: Пакеты из pkg и ports для одного ПО

---

## 🚀 Next Steps

**Related Modules:**
- [Networking](../07_Networking/) — настройка сети
- [Services](../09_Services/) — управление службами

**Practice Ideas:**
1. Установите стек LEMP (Linux→OpenBSD, Nginx, MariaDB, PHP)
2. Соберите nginx из портов с модулем stream
3. Создайте скрипт для еженедельной проверки обновлений
4. Установите и настройте графическое окружение

**Going Deeper:**
- Создание собственных пакетов
- Локальное зеркало пакетов
- Написание собственных портов

---

## 📚 Additional Resources

**Documentation:**
- [man pkg_add](https://man.openbsd.org/pkg_add) — установка пакетов
- [man pkg_info](https://man.openbsd.org/pkg_info) — информация
- [man ports](https://man.openbsd.org/ports) — система портов
- [OpenBSD FAQ 15](https://www.openbsd.org/faq/faq15.html) — пакеты и порты

**Ports:**
- [Ports README](https://cvsweb.openbsd.org/ports/infrastructure/templates/README)
- [Ports Guide](https://www.openbsd.org/faq/ports/)

---

