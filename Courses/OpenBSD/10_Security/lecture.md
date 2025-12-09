# Security
## Безопасность в OpenBSD: pledge, unveil, securelevel

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [User Management](../05_UserManagement/) и [Services](../09_Services/)
- Понимать права доступа Unix
- Знать основы сетевой безопасности

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать и использовать механизмы pledge и unveil
- Настраивать securelevel для защиты системы
- Применять best practices безопасности OpenBSD
- Настраивать аудит и мониторинг безопасности
- Защищать службы от компрометации

---

## 1. Философия безопасности OpenBSD

### 1.1 Secure by Default

OpenBSD следует принципу минимальных привилегий:

- Минимум служб по умолчанию
- Строгие права доступа
- Регулярные аудиты кода
- Проактивные митигации

```sh
# Только необходимые службы запущены после установки
$ rcctl ls started
cron
ntpd
pflogd
sshd
```

### 1.2 Многослойная защита

```
┌─────────────────────────────────────────────────────┐
│                   Securelevel                        │
├─────────────────────────────────────────────────────┤
│            PF (Packet Filter)                        │
├─────────────────────────────────────────────────────┤
│            pledge / unveil                           │
├─────────────────────────────────────────────────────┤
│         Permissions / chroot                         │
├─────────────────────────────────────────────────────┤
│    Memory protections (W^X, ASLR, KARL)             │
└─────────────────────────────────────────────────────┘
```

---

## 2. pledge() — ограничение системных вызовов

### 2.1 Что такое pledge

`pledge()` — системный вызов, ограничивающий набор операций, которые может выполнять процесс.

```c
#include <unistd.h>

int main() {
    // Программа обещает использовать только:
    // - stdio: стандартный ввод/вывод
    // - rpath: чтение файлов
    pledge("stdio rpath", NULL);
    
    // После этого fork(), exec(), сеть — запрещены
    // Попытка их использовать = SIGABRT
}
```

### 2.2 Категории pledge

| Категория | Разрешённые операции |
|-----------|---------------------|
| `stdio` | Базовый I/O, printf, malloc |
| `rpath` | Чтение файлов |
| `wpath` | Запись файлов |
| `cpath` | Создание/удаление файлов |
| `tmppath` | Операции в /tmp |
| `inet` | Сетевые операции (IPv4/IPv6) |
| `unix` | Unix domain sockets |
| `dns` | DNS-запросы |
| `getpw` | Доступ к /etc/passwd |
| `proc` | fork, exec |
| `exec` | execve |
| `id` | Изменение UID/GID |
| `fattr` | Изменение атрибутов файлов |
| `tty` | Операции с терминалом |

### 2.3 Пример использования

```c
// cat_safe.c - безопасная версия cat
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    // Ограничиваем возможности программы
    if (pledge("stdio rpath", NULL) == -1) {
        err(1, "pledge");
    }
    
    if (argc < 2) {
        fprintf(stderr, "Usage: %s file\n", argv[0]);
        return 1;
    }
    
    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("fopen");
        return 1;
    }
    
    char buf[4096];
    while (fgets(buf, sizeof(buf), f)) {
        printf("%s", buf);
    }
    
    fclose(f);
    return 0;
}
```

### 2.4 Проверка pledge в программах

```sh
# Многие базовые утилиты используют pledge
$ ktrace -tc pledge cat /etc/passwd | kdump
  1234 cat      CALL  pledge(0x7f7fffffddd0,0)
  1234 cat      RET   pledge 0

# Если программа нарушает pledge
$ ./bad_program
Abort trap (core dumped)

# В логах:
$ dmesg | tail
bad_program(1234): pledge "stdio", syscall 97
```

---

## 3. unveil() — ограничение видимости файловой системы

### 3.1 Что такое unveil

`unveil()` ограничивает, какие пути файловой системы видит процесс.

```c
#include <unistd.h>

int main() {
    // Разрешить только чтение /etc и запись в /var/log
    unveil("/etc", "r");
    unveil("/var/log", "rw");
    unveil(NULL, NULL);  // Заблокировать добавление путей
    
    // Теперь /home, /root и т.д. недоступны
    // fopen("/home/user/file", "r") вернёт ENOENT
}
```

### 3.2 Права unveil

| Право | Описание |
|-------|----------|
| `r` | Чтение |
| `w` | Запись |
| `x` | Выполнение |
| `c` | Создание/удаление |

### 3.3 Пример: безопасный веб-сервер

```c
// Ограничить веб-сервер только его директориями
unveil("/var/www", "r");           // Документы
unveil("/var/www/logs", "rwc");    // Логи
unveil("/etc/ssl", "r");           // SSL сертификаты
unveil("/usr/lib", "r");           // Библиотеки
unveil(NULL, NULL);                // Заблокировать

pledge("stdio rpath wpath inet", NULL);
```

### 3.4 Комбинация pledge и unveil

```c
// Типичный паттерн безопасности
int main() {
    // Сначала unveil — пока есть полный доступ
    unveil("/etc/myapp.conf", "r");
    unveil("/var/log/myapp", "rwc");
    unveil("/var/run/myapp.pid", "rwc");
    unveil(NULL, NULL);
    
    // Затем pledge — ограничить syscalls
    pledge("stdio rpath wpath cpath", NULL);
    
    // Теперь программа максимально ограничена
}
```

---

## 4. Securelevel

### 4.1 Уровни безопасности

OpenBSD поддерживает уровни защиты ядра:

| Уровень | Описание |
|---------|----------|
| -1 | Permanently insecure (для разработки) |
| 0 | Insecure (single-user mode) |
| 1 | Secure (по умолчанию в multi-user) |
| 2 | Highly secure |

### 4.2 Ограничения securelevel

**Securelevel 1:**
- Нельзя снять флаги schg, sappnd с файлов
- Нельзя модифицировать /dev/mem, /dev/kmem
- Нельзя загружать модули ядра

**Securelevel 2:**
- Всё из уровня 1
- Нельзя изменять время значительно
- Нельзя модифицировать правила PF

### 4.3 Настройка securelevel

```sh
# Проверить текущий уровень
$ sysctl kern.securelevel
kern.securelevel=1

# Повысить уровень (необратимо до перезагрузки!)
# doas sysctl kern.securelevel=2

# Для постоянной установки в /etc/sysctl.conf
kern.securelevel=2
```

> **⚠️ Warning:**  
> Securelevel можно только повышать. Понизить можно только перезагрузкой в single-user mode.

### 4.4 Защита конфигурации с schg

```sh
# Защитить важные файлы
# doas chflags schg /bsd
# doas chflags schg /etc/pf.conf

# Проверить флаги
$ ls -lo /bsd
-r-xr-xr-x  1 root  wheel  schg 24789504 Oct  9 13:57 /bsd

# Снять флаг (только в securelevel 0)
# boot -s
# mount -uw /
# chflags noschg /bsd
```

---

## 5. Митигации памяти

### 5.1 W^X (Write XOR Execute)

Страницы памяти либо записываемы, либо исполняемы, но не оба.

```sh
# Проверить защиту
$ dmesg | grep "protection"
```

### 5.2 ASLR (Address Space Layout Randomization)

Рандомизация расположения в памяти:

```sh
# Каждый запуск — разные адреса
$ cat /proc/self/maps
# Адреса стека, heap, библиотек — случайные
```

### 5.3 KARL (Kernel Address Randomized Link)

Ядро перелинковывается при каждой загрузке:

```sh
# После установки патчей
Relinking to create unique kernel... done.

# Каждая загрузка — уникальное ядро
```

### 5.4 RETGUARD

Защита от ROP-атак (Return-Oriented Programming):

- Все функции имеют cookie возврата
- Попытка подмены — crash

---

## 6. Практики безопасности

### 6.1 Chroot окружения

```sh
# Создать chroot для службы
# doas mkdir -p /var/www/{bin,etc,dev,tmp}
# doas cp /bin/sh /var/www/bin/
# doas mknod /var/www/dev/null c 2 2
# doas chmod 666 /var/www/dev/null

# Запустить в chroot
# doas chroot /var/www /bin/sh
```

### 6.2 Privilege separation

```sh
# Многие демоны OpenBSD используют разделение привилегий
# Пример: sshd

# 1. Главный процесс (root) слушает порт 22
# 2. При подключении — fork непривилегированного процесса
# 3. Аутентификация в песочнице
# 4. После успеха — смена пользователя

$ ps aux | grep sshd
root     78123  0.0  0.1  1234  5678 ??  Is   10:00  0:00 /usr/sbin/sshd
_sshd    78456  0.0  0.1  2345  6789 ??  S    10:01  0:00 sshd: user [priv]
user     78457  0.0  0.1  2345  6790 ??  S    10:01  0:00 sshd: user@pts/0
```

### 6.3 Минимизация служб

```sh
# Отключить ненужные службы
# doas rcctl disable snmpd
# doas rcctl disable lpd

# Проверить, что слушает сеть
$ netstat -an | grep LISTEN
tcp        0      0  *.22                   *.*                    LISTEN
tcp        0      0  127.0.0.1.25           *.*                    LISTEN
```

### 6.4 Безопасность SSH

```sh
# /etc/ssh/sshd_config

# Запретить root
PermitRootLogin no

# Только ключи
PasswordAuthentication no
PubkeyAuthentication yes

# Ограничить алгоритмы
KexAlgorithms curve25519-sha256
Ciphers chacha20-poly1305@openssh.com

# Лимиты
MaxAuthTries 3
MaxSessions 5
ClientAliveInterval 300
ClientAliveCountMax 2

# Ограничить пользователей
AllowUsers admin operator
```

---

## 7. Аудит безопасности

### 7.1 Системные логи

```sh
# Важные файлы логов
/var/log/authlog    # Аутентификация
/var/log/secure     # Безопасность
/var/log/messages   # Общие сообщения
/var/log/daemon     # Демоны
/var/log/pflog      # Файрвол
```

### 7.2 Мониторинг входов

```sh
# Последние входы
$ last
admin    pts/0    192.168.1.100    Dec  1 10:00   still logged in

# Неудачные попытки
$ lastb

# Текущие пользователи
$ who
```

### 7.3 Проверка целостности

```sh
# mtree — проверка целостности файлов
# Создать спецификацию
$ mtree -c -K sha256digest -p /etc > /root/etc.mtree

# Проверить изменения
$ mtree -p /etc < /root/etc.mtree
./ssh/sshd_config changed
        modification time expected Fri Nov 15 14:30:00 2023 found Mon Dec  1 10:00:00 2023
        SHA-256 expected abc123... found def456...
```

### 7.4 Проверка портов

```sh
# Что слушает
$ netstat -an | grep LISTEN

# Какие процессы
# doas fstat | grep internet
root     sshd       1234   3* internet stream tcp *:22
```

---

## 8. Hardening чеклист

### 8.1 После установки

```sh
# 1. Установить патчи
# doas syspatch

# 2. Настроить doas (не sudo)
echo "permit persist :wheel" | doas tee /etc/doas.conf

# 3. Отключить root по SSH
# В /etc/ssh/sshd_config:
PermitRootLogin no

# 4. Настроить PF
# doas vi /etc/pf.conf
# doas pfctl -ef /etc/pf.conf

# 5. Включить securelevel 2 (опционально)
echo "kern.securelevel=2" | doas tee -a /etc/sysctl.conf
```

### 8.2 Регулярные проверки

```sh
# Еженедельно
# 1. Проверить обновления
# doas syspatch -c

# 2. Проверить логи
$ doas grep -i "fail\|error\|denied" /var/log/authlog

# 3. Проверить процессы
$ ps auxww

# 4. Проверить соединения
$ netstat -an
```

---

## 💡 Key Takeaways

- **pledge**: Ограничивает syscalls — даже при компрометации атакующий ограничен
- **unveil**: Скрывает файловую систему — программа видит только нужное
- **securelevel**: Защита ядра и критических файлов
- **Комбинируйте**: pledge + unveil + chroot + PF = многослойная защита
- **Минимизируйте**: Меньше служб = меньше поверхность атаки

---

## 🚀 Next Steps

**Related Modules:**
- [System Admin](../11_SystemAdmin/) — мониторинг и логи
- [PF](../08_PF/) — файрвол

**Practice Ideas:**
1. Напишите программу с pledge и unveil
2. Настройте securelevel 2 на тестовой системе
3. Создайте скрипт проверки безопасности
4. Настройте полный hardening для сервера

**Going Deeper:**
- Изучите исходный код OpenSSH для примеров privsep
- Создайте chroot для веб-приложения
- Настройте автоматический аудит с mtree

---

## 📚 Additional Resources

**Documentation:**
- [man pledge](https://man.openbsd.org/pledge) — ограничение syscalls
- [man unveil](https://man.openbsd.org/unveil) — ограничение filesystem
- [man securelevel](https://man.openbsd.org/securelevel) — уровни безопасности
- [man mtree](https://man.openbsd.org/mtree) — проверка целостности

**Articles:**
- [OpenBSD Innovations](https://www.openbsd.org/innovations.html)
- [Pledge presentation](https://www.openbsd.org/papers/)

---

