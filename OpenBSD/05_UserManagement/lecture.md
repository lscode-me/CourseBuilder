# User Management
## Управление пользователями и группами в OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [File System](../04_FileSystem/)
- Понимать права доступа в Unix
- Уметь использовать doas для административных задач

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать и удалять пользователей и группы
- Управлять паролями и политиками безопасности
- Настраивать doas для делегирования прав
- Использовать login.conf для ограничения ресурсов
- Понимать системные файлы пользователей

---

## 1. Основы управления пользователями

### 1.1 Файлы пользователей

```sh
# Основные файлы
/etc/passwd     # информация о пользователях
/etc/master.passwd  # пароли (только для root)
/etc/group      # информация о группах
/etc/shells     # разрешённые оболочки
```

**Формат /etc/passwd:**

```sh
$ cat /etc/passwd
root:*:0:0:Charlie &:/root:/bin/ksh
daemon:*:1:1:The devil himself:/root:/sbin/nologin
admin:*:1000:1000:System Administrator:/home/admin:/bin/ksh
#     │  │    │          │               │          │
#     │  │    │          │               │          └── shell
#     │  │    │          │               └── домашний каталог
#     │  │    │          └── полное имя (GECOS)
#     │  │    └── GID (группа)
#     │  └── UID (идентификатор)
#     └── пароль (всегда *)
```

**Формат /etc/master.passwd:**

```sh
# doas cat /etc/master.passwd
root:$2b$10$abc...xyz:0:0:daemon:0:0:Charlie &:/root:/bin/ksh
#     │
#     └── зашифрованный пароль (bcrypt)
```

### 1.2 Группы

```sh
$ cat /etc/group
wheel:*:0:root,admin
daemon:*:1:
staff:*:20:admin
users:*:100:
#     │ │   │
#     │ │   └── члены группы
#     │ └── GID
#     └── пароль (не используется)
```

### 1.3 Важные группы

| Группа | GID | Назначение |
|--------|-----|------------|
| `wheel` | 0 | Доступ к doas/su |
| `operator` | 5 | Операторы системы |
| `staff` | 20 | Обычные пользователи |
| `_shadow` | 65 | Доступ к master.passwd |
| `dialer` | 117 | Доступ к модемам |
| `network` | 86 | Сетевые операции |
| `wobj` | 87 | Сборка world |

---

## 2. Создание пользователей

### 2.1 useradd

```sh
# Базовое создание пользователя
# doas useradd -m -G wheel,staff -s /bin/ksh username

# Опции:
# -m          создать домашний каталог
# -G groups   дополнительные группы
# -s shell    оболочка
# -c comment  полное имя
# -d dir      путь к домашнему каталогу
# -u uid      конкретный UID
# -g group    основная группа
```

**Пример создания пользователя:**

```sh
# doas useradd -m -G wheel,staff -s /bin/ksh -c "John Doe" john
# doas passwd john
Changing password for john.
New password:
Retype new password:
passwd: updating the database...
passwd: done
```

### 2.2 adduser (интерактивный)

```sh
# doas adduser

Use option '-silent' if you don't want to see all warnings and questions.

Enter username [a-z0-9_-]: john
Enter full name: John Doe
Enter shell [ksh]: 
UID [1001]: 
Login group john [john]: 
Login group is 'john'. Invite john into other groups: staff wheel
Login class [default]: 
Enter password []: 
Enter password again []: 

Name:     john
Password: ****
Fullname: John Doe
Uid:      1001
Gid:      1001 (john)
Groups:   john staff wheel
HOME:     /home/john
Shell:    /bin/ksh
OK? (y/n) [y]: y
```

### 2.3 Шаблон пользователя

Файлы из `/etc/skel` копируются в домашний каталог:

```sh
$ ls -la /etc/skel
-rw-r--r--  1 root  wheel  87 Oct  9 13:57 .Xdefaults
-rw-r--r--  1 root  wheel  773 Oct  9 13:57 .cshrc
-rw-r--r--  1 root  wheel  398 Oct  9 13:57 .login
-rw-r--r--  1 root  wheel  113 Oct  9 13:57 .mailrc
-rw-r--r--  1 root  wheel  218 Oct  9 13:57 .profile

# Добавить свой файл в шаблон
# doas cp .kshrc /etc/skel/
```

---

## 3. Изменение и удаление пользователей

### 3.1 usermod

```sh
# Изменить оболочку
# doas usermod -s /bin/ksh john

# Добавить в группу
# doas usermod -G staff,wheel john

# Заблокировать аккаунт
# doas usermod -Z john

# Изменить домашний каталог
# doas usermod -d /home/newdir john

# Изменить полное имя
# doas usermod -c "John Smith" john
```

### 3.2 userdel

```sh
# Удалить пользователя (сохранить домашний каталог)
# doas userdel john

# Удалить пользователя и его файлы
# doas userdel -r john
```

### 3.3 rmuser (интерактивный)

```sh
# doas rmuser john
Matching password entry:
john:*:1001:1001:John Doe:/home/john:/bin/ksh

Is this the entry you wish to remove? [y/n] y
Remove user's home directory (/home/john)? [y/n] y
Removing user (john): mailspool home passwd.
```

---

## 4. Управление паролями

### 4.1 passwd

```sh
# Изменить свой пароль
$ passwd
Changing password for john.
Old password:
New password:
Retype new password:

# Изменить пароль другого пользователя (root)
# doas passwd john

# Заблокировать пароль
# doas passwd -l john

# Разблокировать пароль
# doas passwd -u john
```

### 4.2 Политика паролей

В `/etc/login.conf` настраивается сложность:

```sh
# Минимальная длина пароля
default:\
    :passwordtime=90d:\
    :minpasswordlen=8:\
    :localcipher=blowfish,a:\
    :tc=auth-defaults:
```

### 4.3 Шифрование паролей

OpenBSD использует **bcrypt** по умолчанию:

```sh
# Алгоритм настраивается в /etc/login.conf
:localcipher=blowfish,a:

# Проверить текущий алгоритм
$ grep cipher /etc/login.conf
```

> **🔒 Security:**  
> OpenBSD была первой ОС, использующей bcrypt по умолчанию. Это один из самых безопасных алгоритмов хеширования.

---

## 5. Управление группами

### 5.1 groupadd

```sh
# Создать группу
# doas groupadd developers

# С конкретным GID
# doas groupadd -g 500 developers
```

### 5.2 groupmod

```sh
# Изменить имя группы
# doas groupmod -n newname oldname

# Изменить GID
# doas groupmod -g 501 developers
```

### 5.3 groupdel

```sh
# Удалить группу
# doas groupdel developers
```

### 5.4 Добавление пользователя в группу

```sh
# Через usermod
# doas usermod -G developers john

# Напрямую редактируя /etc/group
# doas vi /etc/group
developers:*:500:john,jane,bob
```

---

## 6. doas — делегирование прав

### 6.1 Базовая настройка

```sh
# /etc/doas.conf
# Синтаксис: permit|deny [options] identity [as target] [cmd command [args]]

# Разрешить wheel выполнять любые команды
permit persist :wheel

# Разрешить конкретному пользователю
permit john

# Разрешить без пароля
permit nopass john cmd /sbin/reboot
```

### 6.2 Опции doas

| Опция | Описание |
|-------|----------|
| `persist` | Запомнить аутентификацию на 5 минут |
| `nopass` | Не спрашивать пароль |
| `keepenv` | Сохранить переменные окружения |
| `setenv { ... }` | Установить переменные |

### 6.3 Примеры конфигурации

```sh
# /etc/doas.conf

# Администраторы (группа wheel) — полный доступ с кешированием пароля
permit persist :wheel

# Оператор может перезагружать сервер без пароля
permit nopass operator cmd /sbin/reboot
permit nopass operator cmd /sbin/halt

# Разработчик может управлять своим приложением
permit persist developers cmd /etc/rc.d/myapp

# Запретить пользователю выполнять команды от root
deny baduser

# Сохранять переменные при работе с pkg
permit persist setenv { PKG_PATH } :wheel cmd pkg_add
```

### 6.4 Использование doas

```sh
# Выполнить команду от root
$ doas ls /root
Password:
.Xauthority  .cshrc  .kshrc  .profile

# Выполнить от другого пользователя
$ doas -u postgres psql

# Запустить shell от root
$ doas -s

# Проверить конфигурацию
$ doas -C /etc/doas.conf && echo "Config OK"
Config OK
```

---

## 7. login.conf — классы входа

### 7.1 Структура login.conf

```sh
$ cat /etc/login.conf
# Класс по умолчанию
default:\
    :path=/usr/bin /bin /usr/sbin /sbin /usr/local/bin:\
    :umask=022:\
    :datasize-max=512M:\
    :datasize-cur=512M:\
    :maxproc-max=256:\
    :maxproc-cur=128:\
    :openfiles-cur=512:\
    :openfiles-max=1024:\
    :stacksize-cur=4M:\
    :localcipher=blowfish,a:\
    :tc=auth-defaults:

# Класс для разработчиков
developer:\
    :datasize-max=2048M:\
    :openfiles-max=4096:\
    :maxproc-max=512:\
    :tc=default:

# Класс для демонов
daemon:\
    :ignorenologin:\
    :datasize=infinity:\
    :maxproc=infinity:\
    :openfiles-max=1024:\
    :tc=default:
```

### 7.2 Лимиты ресурсов

| Лимит | Описание |
|-------|----------|
| `datasize` | Размер сегмента данных |
| `stacksize` | Размер стека |
| `maxproc` | Максимум процессов |
| `openfiles` | Максимум открытых файлов |
| `memorylocked` | Заблокированная память |
| `vmemoryuse` | Виртуальная память |

### 7.3 Применение login.conf

```sh
# После изменения login.conf
# doas cap_mkdb /etc/login.conf

# Назначить класс пользователю
# doas usermod -L developer john

# Проверить лимиты
$ ulimit -a
-t: cpu time (seconds)         unlimited
-f: file size (blocks)         unlimited
-d: data seg size (kbytes)     524288
-s: stack size (kbytes)        4096
-c: core file size (blocks)    0
-m: resident set size (kbytes) unlimited
-l: locked-in-memory size (kb) 331085
-n: file descriptors           512
-p: processes                  128
```

---

## 8. Информация о пользователях

### 8.1 Команды для получения информации

```sh
# Текущий пользователь
$ whoami
admin

# UID и группы
$ id
uid=1000(admin) gid=1000(admin) groups=1000(admin), 0(wheel), 20(staff)

# Информация о пользователе
$ id john
uid=1001(john) gid=1001(john) groups=1001(john), 20(staff)

# Кто залогинен
$ who
admin    ttyC0    Dec  1 10:00
john     pts/0    Dec  1 10:30 (192.168.1.100)

# Подробнее о залогиненных
$ w
10:45AM  up 5 days,  3:21, 2 users, load averages: 0.08, 0.03, 0.01
USER     TTY FROM              LOGIN@  IDLE WHAT
admin    C0  -                10:00AM     - -ksh
john     p0  192.168.1.100    10:30AM     1 vim config.txt

# Последние входы
$ last
admin    ttyC0                     Dec  1 10:00   still logged in
john     pts/0    192.168.1.100    Dec  1 10:30   still logged in
reboot   ~                         Dec  1 09:55
```

### 8.2 finger

```sh
$ finger john
Login: john                             Name: John Doe
Directory: /home/john                   Shell: /bin/ksh
Last login Fri Dec  1 10:30 (UTC) on pts/0 from 192.168.1.100
No mail.
No Plan.
```

### 8.3 getent

```sh
# Получить запись из passwd
$ getent passwd john
john:*:1001:1001:John Doe:/home/john:/bin/ksh

# Получить запись из group
$ getent group wheel
wheel:*:0:root,admin,john
```

---

## 9. Системные пользователи

### 9.1 Создание системного пользователя

```sh
# Для демонов и служб используйте UID < 1000
# doas useradd -r -d /var/empty -s /sbin/nologin _myapp

# Или через useradd с указанием UID
# doas useradd -u 500 -g =uid -d /nonexistent -s /sbin/nologin _myapp
```

### 9.2 Соглашения об именовании

В OpenBSD системные пользователи начинаются с `_`:

```sh
$ grep "^_" /etc/passwd | head
_pflogd:*:507:507:pflogd:/var/empty:/sbin/nologin
_dhcp:*:62:62:DHCP:/var/empty:/sbin/nologin
_sshd:*:27:27:sshd:/var/empty:/sbin/nologin
_ntp:*:123:123:NTP:/var/empty:/sbin/nologin
```

### 9.3 Запуск процессов от системного пользователя

```sh
# В rc.d скриптах
daemon_user="_myapp"

# Через doas
$ doas -u _myapp /usr/local/bin/myapp
```

---

## 10. Практические примеры

### 10.1 Создание разработчика с расширенными лимитами

```sh
# 1. Создать класс в login.conf
# doas vi /etc/login.conf
developer:\
    :datasize=2048M:\
    :openfiles=4096:\
    :maxproc=512:\
    :tc=default:

# 2. Перестроить базу
# doas cap_mkdb /etc/login.conf

# 3. Создать пользователя
# doas useradd -m -G wheel,staff -L developer -c "Developer" dev

# 4. Установить пароль
# doas passwd dev
```

### 10.2 Настройка оператора с ограниченным доступом

```sh
# /etc/doas.conf
permit nopass operator cmd /sbin/reboot
permit nopass operator cmd /sbin/halt
permit nopass operator cmd /etc/rc.d/httpd
permit nopass operator cmd /usr/bin/tail args -f /var/log/messages

# Создать пользователя
# doas useradd -m -s /bin/ksh -c "System Operator" operator
```

### 10.3 Блокировка и разблокировка

```sh
# Заблокировать аккаунт
# doas usermod -Z john

# Или через passwd
# doas passwd -l john

# Разблокировать
# doas passwd -u john

# Установить срок действия аккаунта
# doas usermod -e 2024-12-31 tempuser
```

---

## 💡 Key Takeaways

- **bcrypt по умолчанию**: OpenBSD использует самый безопасный алгоритм хеширования паролей
- **doas вместо sudo**: Простой и безопасный, конфигурация в одном файле
- **Группа wheel**: Только члены wheel могут использовать su/doas
- **login.conf**: Мощный инструмент для ограничения ресурсов пользователей
- **Системные пользователи**: Имена начинаются с `_`, используют /sbin/nologin

---

## 🚀 Next Steps

**Related Modules:**
- [Package Management](../06_PackageManagement/) — установка программ
- [Security](../10_Security/) — безопасность системы

**Practice Ideas:**
1. Создайте пользователя-разработчика с расширенными лимитами
2. Настройте doas для оператора с ограниченными правами
3. Создайте системного пользователя для своего приложения
4. Настройте класс входа с ограничением памяти

**Going Deeper:**
- Изучите LDAP интеграцию для централизованной аутентификации
- Настройте YP/NIS для сетевого управления пользователями
- Разберитесь с Kerberos аутентификацией

---

## 📚 Additional Resources

**Documentation:**
- [man useradd](https://man.openbsd.org/useradd) — создание пользователей
- [man doas.conf](https://man.openbsd.org/doas.conf) — настройка doas
- [man login.conf](https://man.openbsd.org/login.conf) — классы входа
- [man passwd](https://man.openbsd.org/passwd) — управление паролями

---

