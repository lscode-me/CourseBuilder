# Basic Commands
## Базовые команды и навигация в OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Установить OpenBSD (модуль [Installation](../02_Installation/))
- Уметь войти в систему через консоль или SSH
- Понимать концепцию командной строки

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Уверенно навигировать по файловой системе
- Работать с файлами и каталогами
- Использовать man-страницы для получения справки
- Применять базовые текстовые утилиты
- Понимать работу с процессами
- Использовать переменные окружения и shell

---

## 1. Оболочка (Shell)

### 1.1 Korn Shell (ksh)

OpenBSD использует **ksh** (Korn Shell) как оболочку по умолчанию. Это не bash!

```sh
$ echo $SHELL
/bin/ksh
```

**Output:**
```
/bin/ksh
```

Основные отличия от bash:

- Синтаксис совместим с POSIX sh
- Нет массивов bash-стиля
- Другая история команд
- Встроенный редактор строк (emacs/vi режим)

### 1.2 Базовые горячие клавиши

| Клавиша | Действие |
|---------|----------|
| `Ctrl+A` | В начало строки |
| `Ctrl+E` | В конец строки |
| `Ctrl+U` | Удалить до начала строки |
| `Ctrl+K` | Удалить до конца строки |
| `Ctrl+W` | Удалить слово назад |
| `Ctrl+R` | Поиск в истории |
| `Ctrl+L` | Очистить экран |
| `Ctrl+C` | Прервать команду |
| `Ctrl+D` | Выход (EOF) |

### 1.3 История команд

```sh
# Показать историю

$ history
    1  ls
    2  cd /etc
    3  cat passwd

# Выполнить команду из истории

$ !2
cd /etc

# Выполнить последнюю команду

$ !!

# Выполнить последнюю команду, начинающуюся с 'ls'

$ !ls
```

### 1.4 Автодополнение

В ksh нажмите `Tab` или `Esc Esc` для автодополнения:

```sh
$ cd /u<Tab>
$ cd /usr/

$ cd /usr/lo<Tab>
$ cd /usr/local/
```

---

## 2. Навигация по файловой системе

### 2.1 Команда pwd

Показывает текущий рабочий каталог:

```sh
$ pwd
/home/admin
```

**Output:**
```
/home/admin
```

### 2.2 Команда cd

Изменение каталога:

```sh
# Перейти в каталог

$ cd /etc

# Вернуться в домашний каталог

$ cd
$ cd ~

# Перейти в предыдущий каталог

$ cd -

# Подняться на уровень выше

$ cd ..

# Подняться на два уровня

$ cd ../..
```

### 2.3 Команда ls

Просмотр содержимого каталога:

```sh
# Простой список

$ ls
Desktop  Documents  Downloads

# Подробный формат

$ ls -l
total 12
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Desktop
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Documents
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Downloads

# Показать скрытые файлы

$ ls -a
.  ..  .profile  .kshrc  Desktop  Documents

# Человекочитаемые размеры

$ ls -lh
total 12K
drwxr-xr-x  2 admin  admin  512B Dec  1 10:00 Desktop

# Сортировка по времени

$ ls -lt

# Рекурсивный просмотр

$ ls -R
```

**Output для ls -l:**
```
total 12
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Desktop
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Documents
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Downloads
```

**Расшифровка вывода ls -l:**

```
drwxr-xr-x  2 admin  admin  512 Dec  1 10:00 Desktop
│├─┤├─┤├─┤  │  │      │     │     │          │
││  │  │    │  │      │     │     │          └── Имя файла
││  │  │    │  │      │     │     └── Дата модификации
││  │  │    │  │      │     └── Размер в байтах
││  │  │    │  │      └── Группа
││  │  │    │  └── Владелец
││  │  │    └── Количество ссылок
││  │  └── Права для остальных (r-x)
││  └── Права для группы (r-x)
│└── Права для владельца (rwx)
└── Тип (d=каталог, -=файл, l=ссылка)
```

---

## 3. Работа с файлами

### 3.1 Создание файлов

```sh
# Создать пустой файл

$ touch newfile.txt

# Создать файл с содержимым

$ echo "Hello, OpenBSD!" > hello.txt

# Добавить в файл

$ echo "New line" >> hello.txt
```

### 3.2 Команда cat

Просмотр и конкатенация файлов:

```sh
# Просмотр файла

$ cat /etc/motd
OpenBSD 7.4 (GENERIC.MP) #0: Mon Oct  9 13:57:11 MDT 2023

# Конкатенация файлов

$ cat file1.txt file2.txt > combined.txt

# Нумерация строк

$ cat -n /etc/passwd
     1  root:*:0:0:Charlie &:/root:/bin/ksh
     2  daemon:*:1:1:The devil himself:/root:/sbin/nologin
     3  ...
```

### 3.3 Просмотр файлов: less, more, head, tail

```sh
# Постраничный просмотр

$ less /var/log/messages
# Клавиши: q-выход, /pattern-поиск, n-следующее совпадение

# Первые 10 строк

$ head /etc/passwd

# Последние 10 строк

$ tail /var/log/messages

# Последние 20 строк

$ tail -20 /var/log/messages

# Следить за файлом в реальном времени

$ tail -f /var/log/messages
```

### 3.4 Копирование: cp

```sh
# Копировать файл

$ cp source.txt destination.txt

# Копировать в каталог

$ cp file.txt /tmp/

# Рекурсивное копирование каталога

$ cp -r mydir /backup/

# Сохранить атрибуты

$ cp -p original.txt copy.txt

# Интерактивный режим (спрашивать перед перезаписью)

$ cp -i file.txt /tmp/
```

### 3.5 Перемещение и переименование: mv

```sh
# Переименовать файл

$ mv oldname.txt newname.txt

# Переместить в каталог

$ mv file.txt /tmp/

# Переместить несколько файлов

$ mv file1.txt file2.txt /backup/

# Интерактивный режим

$ mv -i file.txt /tmp/
```

### 3.6 Удаление: rm, rmdir

```sh
# Удалить файл

$ rm file.txt

# Удалить с подтверждением

$ rm -i file.txt

# Удалить каталог рекурсивно

$ rm -r mydir/

# Принудительное удаление (опасно!)

$ rm -rf mydir/

# Удалить пустой каталог

$ rmdir emptydir/
```

> **⚠️ Warning:**  
> `rm -rf` не спрашивает подтверждения! В OpenBSD нет корзины — файлы удаляются навсегда.

### 3.7 Создание каталогов: mkdir

```sh
# Создать каталог

$ mkdir newdir

# Создать с родительскими каталогами

$ mkdir -p path/to/newdir

# Установить права при создании

$ mkdir -m 700 private
```

---

## 4. Получение справки

### 4.1 man — основной источник информации

OpenBSD славится качеством man-страниц:

```sh
# Справка по команде

$ man ls

# Справка по конфигурационному файлу

$ man pf.conf

# Справка по системному вызову

$ man 2 open

# Поиск по ключевому слову

$ man -k network
hostname.if(5) - interface-specific configuration file
ifconfig(8) - configure network interface parameters
...
```

**Секции man:**

| Секция | Содержимое |
|--------|------------|
| 1 | Команды пользователя |
| 2 | Системные вызовы |
| 3 | Библиотечные функции |
| 4 | Устройства |
| 5 | Форматы файлов |
| 6 | Игры |
| 7 | Разное |
| 8 | Команды администратора |
| 9 | Ядро |

```sh
# Указать секцию явно

$ man 5 passwd    # Формат файла /etc/passwd
$ man 1 passwd    # Команда passwd
```

### 4.2 apropos — поиск по описаниям

```sh
$ apropos firewall
pf(4) - packet filter
pfctl(8) - control the packet filter (PF) device
pf.conf(5) - packet filter configuration file
```

### 4.3 whatis — краткое описание

```sh
$ whatis ls
ls(1) - list directory contents
```

### 4.4 info и --help

```sh
# Некоторые GNU утилиты имеют --help

$ grep --help

# info в OpenBSD доступен для некоторых пакетов

$ info coreutils
```

> **💡 Pro Tip:**  
> В OpenBSD man-страницы — главный и самый актуальный источник информации. Всегда начинайте с `man`.

---

## 5. Текстовые утилиты

### 5.1 grep — поиск по тексту

```sh
# Поиск строки в файле

$ grep "root" /etc/passwd
root:*:0:0:Charlie &:/root:/bin/ksh

# Игнорировать регистр

$ grep -i "ROOT" /etc/passwd

# Показать номера строк

$ grep -n "error" /var/log/messages

# Инвертировать (строки без совпадения)

$ grep -v "^#" /etc/pf.conf

# Рекурсивный поиск

$ grep -r "password" /etc/

# Расширенные регулярные выражения

$ grep -E "error|warning" /var/log/messages

# Только имена файлов

$ grep -l "pattern" *.txt
```

### 5.2 sed — потоковый редактор

```sh
# Замена текста

$ echo "hello world" | sed 's/world/OpenBSD/'
hello OpenBSD

# Замена в файле (вывод на stdout)

$ sed 's/old/new/g' file.txt

# Редактирование файла на месте

$ sed -i 's/old/new/g' file.txt

# Удалить строки с комментариями

$ sed '/^#/d' config.txt

# Показать только определённые строки

$ sed -n '5,10p' file.txt
```

### 5.3 awk — обработка текста

```sh
# Вывести второй столбец

$ ls -l | awk '{print $2}'

# Сумма чисел в столбце

$ awk '{sum += $1} END {print sum}' numbers.txt

# Фильтрация по условию

$ awk '$3 > 100' data.txt

# Разделитель полей

$ awk -F: '{print $1}' /etc/passwd
root
daemon
nobody
...
```

### 5.4 cut — извлечение полей

```sh
# Извлечь поля по разделителю

$ cut -d: -f1 /etc/passwd
root
daemon
...

# Извлечь символы

$ echo "Hello" | cut -c1-3
Hel

# Извлечь несколько полей

$ cut -d: -f1,3 /etc/passwd
root:0
daemon:1
```

### 5.5 sort и uniq

```sh
# Сортировка

$ sort file.txt

# Обратная сортировка

$ sort -r file.txt

# Числовая сортировка

$ sort -n numbers.txt

# Уникальные строки

$ sort file.txt | uniq

# Подсчёт повторений

$ sort file.txt | uniq -c

# Только дубликаты

$ sort file.txt | uniq -d
```

### 5.6 wc — подсчёт

```sh
# Строки, слова, байты

$ wc /etc/passwd
      37      65    1843 /etc/passwd

# Только строки

$ wc -l /etc/passwd
37

# Только слова

$ wc -w /etc/passwd
65
```

---

## 6. Перенаправление и конвейеры

### 6.1 Перенаправление вывода

```sh
# Записать в файл (перезаписать)

$ ls > files.txt

# Добавить в файл

$ date >> log.txt

# Перенаправить stderr

$ command 2> errors.txt

# Перенаправить stdout и stderr

$ command > output.txt 2>&1

# Или короче (ksh/bash)

$ command &> output.txt

# Подавить вывод

$ command > /dev/null 2>&1
```

### 6.2 Перенаправление ввода

```sh
# Ввод из файла

$ sort < unsorted.txt

# Here document

$ cat << EOF
Line 1
Line 2
EOF
```

### 6.3 Конвейеры (pipes)

```sh
# Передать вывод одной команды на вход другой

$ ls -l | grep ".txt"

# Цепочка команд

$ cat /var/log/messages | grep error | wc -l

# Найти 10 самых больших файлов

$ du -a /var | sort -rn | head -10

# Найти процессы по имени

$ ps aux | grep sshd
```

### 6.4 Команда tee

Разделяет вывод на экран и в файл:

```sh
# Вывести на экран и записать в файл

$ ls -l | tee listing.txt

# Добавить в файл

$ ls -l | tee -a listing.txt
```

---

## 7. Работа с процессами

### 7.1 ps — список процессов

```sh
# Ваши процессы

$ ps
  PID TT  STAT       TIME COMMAND
14532 p0  Ss      0:00.03 -ksh
14578 p0  R+      0:00.00 ps

# Все процессы

$ ps aux
USER     PID %CPU %MEM   VSZ   RSS TT  STAT   STARTED       TIME COMMAND
root       1  0.0  0.0   524   488 ??  Is   Mon10AM     0:00.02 /sbin/init

# Древовидный вывод

$ ps auxww

# Процессы конкретного пользователя

$ ps -U admin
```

### 7.2 top — мониторинг в реальном времени

```sh
$ top

load averages:  0.08,  0.03,  0.01    puffy.my.domain 14:32:15
26 processes: 25 idle, 1 on processor
CPU:  0.2% user,  0.0% nice,  0.4% sys,  0.0% spin,  0.0% intr, 99.4% idle
Memory: Real: 72M/993M act/tot  Free: 7098M  Cache: 404M  Swap: 0/2048M

  PID USERNAME PRI NICE  SIZE   RES STATE     WAIT      TIME    CPU COMMAND
    1 root      10    0  524K  488K idle      wait      0:00  0.00% init
14532 admin     18    0  1.2M  1.6M idle      kqread    0:00  0.00% ksh
```

**Горячие клавиши в top:**

- `q` — выход
- `k` — убить процесс
- `u` — фильтр по пользователю
- `?` — справка

### 7.3 kill — завершение процессов

```sh
# Завершить процесс (SIGTERM)

$ kill 1234

# Принудительное завершение (SIGKILL)

$ kill -9 1234

# Завершить по имени

$ pkill firefox

# Список сигналов

$ kill -l
HUP INT QUIT ILL TRAP ABRT EMT FPE KILL BUS SEGV SYS PIPE ALRM TERM ...
```

### 7.4 Фоновые процессы

```sh
# Запуск в фоне

$ long_command &

# Список фоновых задач

$ jobs
[1]+  Running    long_command &

# Вернуть на передний план

$ fg %1

# Приостановить текущую задачу
# Ctrl+Z

# Продолжить в фоне

$ bg %1
```

### 7.5 nohup — независимый от терминала процесс

```sh
# Процесс продолжит работу после выхода из сессии

$ nohup long_command &

# Вывод будет в nohup.out
```

---

## 8. Права доступа

### 8.1 chmod — изменение прав

```sh
# Символьный режим

$ chmod u+x script.sh    # Добавить execute для владельца
$ chmod g-w file.txt     # Убрать write для группы
$ chmod o=r file.txt     # Только read для остальных
$ chmod a+r file.txt     # Read для всех

# Числовой режим

$ chmod 755 script.sh    # rwxr-xr-x
$ chmod 644 file.txt     # rw-r--r--
$ chmod 600 secret.txt   # rw-------

# Рекурсивно

$ chmod -R 755 mydir/
```

**Числовые значения:**

| Число | Права |
|-------|-------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 3 | -wx |
| 2 | -w- |
| 1 | --x |
| 0 | --- |

### 8.2 chown — изменение владельца

```sh
# Изменить владельца
# doas chown admin file.txt

# Изменить владельца и группу
# doas chown admin:staff file.txt

# Рекурсивно
# doas chown -R admin:admin mydir/
```

### 8.3 chgrp — изменение группы

```sh
# Изменить группу

$ chgrp staff file.txt

# Рекурсивно

$ chgrp -R staff mydir/
```

---

## 9. Поиск файлов

### 9.1 find — мощный поиск

```sh
# Найти по имени

$ find /etc -name "*.conf"

# Найти по типу (f=файл, d=каталог)

$ find /home -type f -name "*.txt"

# Найти по размеру

$ find /var -size +100M

# Найти по времени модификации (дни)

$ find /tmp -mtime +7

# Выполнить команду для найденных файлов

$ find . -name "*.bak" -exec rm {} \;

# Найти и удалить интерактивно

$ find . -name "*.tmp" -ok rm {} \;
```

### 9.2 locate — быстрый поиск по базе

```sh
# Обновить базу (требует root)
# doas /usr/libexec/locate.updatedb

# Найти файл

$ locate pf.conf
/etc/pf.conf
/usr/share/man/man5/pf.conf.5
```

### 9.3 which и whereis

```sh
# Путь к исполняемому файлу

$ which ls
/bin/ls

# Расположение программы и man-страниц

$ whereis ls
ls: /bin/ls /usr/share/man/man1/ls.1
```

---

## 10. Переменные окружения

### 10.1 Просмотр переменных

```sh
# Все переменные

$ env
HOME=/home/admin
SHELL=/bin/ksh
PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
...

# Конкретная переменная

$ echo $HOME
/home/admin

$ echo $PATH
/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
```

### 10.2 Установка переменных

```sh
# Для текущей сессии

$ export EDITOR=vim
$ export PATH="$PATH:/usr/local/bin"

# Только для одной команды

$ LANG=C sort file.txt
```

### 10.3 Постоянные настройки

Добавьте в `~/.profile` или `~/.kshrc`:

```sh
# ~/.profile

export EDITOR=vim
export VISUAL=vim
export PAGER=less
export PATH="$HOME/bin:$PATH"

# Алиасы

alias ll='ls -la'
alias la='ls -a'
alias ..='cd ..'
```

Применить изменения:

```sh
$ . ~/.profile
# или

$ source ~/.profile
```

---

## 💡 Key Takeaways

- **ksh — не bash**: OpenBSD использует Korn Shell, помните о различиях

- **man — главный друг**: Документация OpenBSD — эталон качества

- **Перенаправление и pipes**: Основа работы в Unix — комбинируйте простые команды

- **Права доступа**: 755 для скриптов, 644 для файлов, 600 для секретных

- **find — мощный инструмент**: Но требует практики

---

## 🚀 Next Steps

**Related Modules:**

- [File System](../04_FileSystem/) — глубже о файловой системе
- [User Management](../05_UserManagement/) — управление пользователями

**Practice Ideas:**

1. Создайте структуру каталогов для проекта с помощью mkdir -p
2. Напишите конвейер для поиска 10 самых больших файлов в /var
3. Настройте ~/.kshrc с полезными алиасами
4. Найдите все файлы .conf в /etc и посчитайте их

**Going Deeper:**

- Изучите регулярные выражения для grep и sed
- Освойте vim или ed для редактирования
- Познакомьтесь со скриптами на ksh

---

## 📚 Additional Resources

**Documentation:**

- [man intro](https://man.openbsd.org/intro) — введение в команды
- [man ksh](https://man.openbsd.org/ksh) — документация оболочки
- [man hier](https://man.openbsd.org/hier) — иерархия файловой системы

**Practice:**

- [Exercism Shell Track](https://exercism.org/tracks/bash) — упражнения (совместимы с ksh)
- [Command Line Challenge](https://cmdchallenge.com/) — интерактивные задания

---





