# Introduction to Unix System Programming
## Введение в системное программирование с Python

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Владеть базовым Python (функции, классы, исключения)
- Понимать основы Unix/Linux (файлы, процессы, права)
- Уметь работать в командной строке

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить что такое системное программирование
- Понимать уровни абстракции: ядро, syscalls, libc, Python
- Использовать модуль `os` для базовых системных вызовов
- Применять `ctypes` для прямого вызова C-функций
- Отлаживать программы с помощью `ktrace`/`strace`

---

## 1. Что такое системное программирование

### 1.1 Определение

**Системное программирование** — это создание программ, которые напрямую взаимодействуют с операционной системой для управления ресурсами: файлами, процессами, памятью, сетью.

В отличие от прикладного программирования:

| Прикладное | Системное |
|------------|-----------|
| Высокоуровневые абстракции | Низкоуровневый доступ к ОС |
| Библиотеки скрывают детали | Работа с syscalls |
| Кроссплатформенность | Платформо-специфичный код |
| Бизнес-логика | Управление ресурсами |

### 1.2 Примеры системного ПО

- Операционные системы и ядра
- Драйверы устройств
- Системные утилиты (`ls`, `ps`, `top`)
- Серверные демоны (`sshd`, `httpd`)
- Базы данных
- Виртуальные машины

### 1.3 Зачем Python для системного программирования?

**Преимущества:**
- Быстрое прототипирование
- Читаемый код для сложной логики
- Богатая стандартная библиотека
- Доступ к C через ctypes/cffi

**Ограничения:**
- Медленнее C (не критично для I/O-bound)
- GIL ограничивает многопоточность
- Не подходит для ядра/драйверов

```python
# Python отлично подходит для:
# - Системных утилит
# - Серверов и демонов
# - Автоматизации
# - Сетевого программирования
# - Обработки файлов
```

---

## 2. Архитектура Unix

### 2.1 Уровни абстракции

```
┌─────────────────────────────────────────────┐
│           User Applications                  │
│        (Python, shell scripts)               │
├─────────────────────────────────────────────┤
│         Python Standard Library              │
│           (os, socket, signal)               │
├─────────────────────────────────────────────┤
│              C Library (libc)                │
│         (open, read, write, fork)            │
├─────────────────────────────────────────────┤
│            System Call Interface             │
│         (syscall numbers, traps)             │
├─────────────────────────────────────────────┤
│                  Kernel                      │
│    (process management, VFS, networking)     │
├─────────────────────────────────────────────┤
│                 Hardware                     │
└─────────────────────────────────────────────┘
```

### 2.2 Системные вызовы (syscalls)

**Системный вызов** — запрос к ядру для выполнения привилегированной операции.

```python
import os

# os.open() → вызывает syscall open(2)
fd = os.open("/etc/passwd", os.O_RDONLY)

# os.read() → вызывает syscall read(2)
data = os.read(fd, 1024)

# os.close() → вызывает syscall close(2)
os.close(fd)

print(data.decode())
```

**Output:**
```
root:*:0:0:Charlie &:/root:/bin/ksh
daemon:*:1:1:The devil himself:/root:/sbin/nologin
...
```

### 2.3 Просмотр системных вызовов

**На OpenBSD (ktrace):**

```bash
$ ktrace -tc python3 -c "import os; os.getpid()"
$ kdump
  1234 python3  CALL  getpid
  1234 python3  RET   getpid 1234
```

**На Linux (strace):**

```bash
$ strace -e trace=getpid python3 -c "import os; os.getpid()"
getpid()                                = 1234
```

### 2.4 Основные категории syscalls

| Категория | Примеры | Python |
|-----------|---------|--------|
| Файлы | open, read, write, close | os.open, os.read |
| Процессы | fork, exec, wait, exit | os.fork, os.exec* |
| Сигналы | kill, sigaction | signal.signal |
| Память | mmap, brk | mmap.mmap |
| Сеть | socket, bind, listen | socket.socket |
| Время | gettimeofday, nanosleep | time.time |

---

## 3. Модуль os — ваш главный инструмент

### 3.1 Информация о процессе

```python
import os

# Идентификаторы процесса
print(f"PID: {os.getpid()}")
print(f"Parent PID: {os.getppid()}")
print(f"User ID: {os.getuid()}")
print(f"Group ID: {os.getgid()}")
print(f"Effective UID: {os.geteuid()}")

# Группы процесса
print(f"Groups: {os.getgroups()}")

# Имя пользователя
print(f"Login: {os.getlogin()}")
```

**Output:**
```
PID: 12345
Parent PID: 12344
User ID: 1000
Group ID: 1000
Effective UID: 1000
Groups: [1000, 0, 20]
Login: admin
```

### 3.2 Переменные окружения

```python
import os

# Получить переменную
home = os.environ.get("HOME")
path = os.environ.get("PATH")
print(f"HOME: {home}")
print(f"PATH: {path}")

# Установить переменную (для текущего процесса)
os.environ["MY_VAR"] = "my_value"

# Удалить переменную
del os.environ["MY_VAR"]

# Все переменные
for key, value in os.environ.items():
    print(f"{key}={value}")
```

### 3.3 Текущий каталог

```python
import os

# Получить текущий каталог
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Сменить каталог
os.chdir("/tmp")
print(f"New directory: {os.getcwd()}")

# Вернуться
os.chdir(cwd)
```

### 3.4 Информация о системе

```python
import os

# Имя ОС
print(f"OS name: {os.name}")  # 'posix' на Unix

# Детальная информация
uname = os.uname()
print(f"System: {uname.sysname}")
print(f"Node: {uname.nodename}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
```

**Output:**
```
OS name: posix
System: OpenBSD
Node: server.home.local
Release: 7.4
Version: GENERIC.MP#0
Machine: amd64
```

### 3.5 Работа с путями

```python
import os.path
from pathlib import Path

# os.path (старый способ)
path = "/home/admin/documents/file.txt"
print(f"Basename: {os.path.basename(path)}")
print(f"Dirname: {os.path.dirname(path)}")
print(f"Exists: {os.path.exists(path)}")
print(f"Is file: {os.path.isfile(path)}")
print(f"Is dir: {os.path.isdir(path)}")

# pathlib (современный способ)
p = Path("/home/admin/documents/file.txt")
print(f"Name: {p.name}")
print(f"Stem: {p.stem}")
print(f"Suffix: {p.suffix}")
print(f"Parent: {p.parent}")
print(f"Exists: {p.exists()}")
```

---

## 4. Обработка ошибок

### 4.1 errno — коды ошибок Unix

```python
import os
import errno

try:
    fd = os.open("/nonexistent", os.O_RDONLY)
except OSError as e:
    print(f"Error number: {e.errno}")
    print(f"Error name: {errno.errorcode.get(e.errno)}")
    print(f"Error message: {e.strerror}")
    print(f"Filename: {e.filename}")
```

**Output:**
```
Error number: 2
Error name: ENOENT
Error message: No such file or directory
Filename: /nonexistent
```

### 4.2 Распространённые коды ошибок

| Код | Имя | Описание |
|-----|-----|----------|
| 1 | EPERM | Operation not permitted |
| 2 | ENOENT | No such file or directory |
| 9 | EBADF | Bad file descriptor |
| 13 | EACCES | Permission denied |
| 17 | EEXIST | File exists |
| 21 | EISDIR | Is a directory |
| 22 | EINVAL | Invalid argument |
| 28 | ENOSPC | No space left on device |

### 4.3 Безопасная обработка ошибок

```python
import os
import errno

def safe_mkdir(path):
    """Создать каталог, игнорируя если существует."""
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        # Каталог уже существует — это OK

def safe_remove(path):
    """Удалить файл, игнорируя если не существует."""
    try:
        os.remove(path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
        # Файл не существует — это OK
```

### 4.4 Проверка возможностей перед действием (LBYL vs EAFP)

```python
import os

# LBYL (Look Before You Leap) — не рекомендуется
# Проблема: race condition между проверкой и действием
if os.path.exists(path):
    os.remove(path)  # Файл мог исчезнуть!

# EAFP (Easier to Ask Forgiveness than Permission) — рекомендуется
try:
    os.remove(path)
except FileNotFoundError:
    pass  # Файл уже не существует
```

> **💡 Pro Tip:**  
> В Python и Unix предпочитайте EAFP — пробуйте выполнить операцию и обрабатывайте ошибку, а не проверяйте заранее.

---

## 5. ctypes — прямой вызов C-функций

### 5.1 Зачем нужен ctypes

Иногда Python не предоставляет обёртку для нужного syscall или C-функции. `ctypes` позволяет вызывать их напрямую.

```python
import ctypes
import ctypes.util

# Загрузить libc
libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Вызвать getpid()
pid = libc.getpid()
print(f"PID from ctypes: {pid}")
```

**Output:**
```
PID from ctypes: 12345
```

### 5.2 Пример: gethostname

```python
import ctypes

libc = ctypes.CDLL(None)  # Загрузить libc по умолчанию

# Создать буфер для результата
buffer = ctypes.create_string_buffer(256)

# Вызвать gethostname(buf, len)
result = libc.gethostname(buffer, 256)

if result == 0:
    hostname = buffer.value.decode()
    print(f"Hostname: {hostname}")
else:
    print("Error getting hostname")
```

### 5.3 Пример: sysctl на OpenBSD

```python
import ctypes
import struct

# На OpenBSD можно читать sysctl через ctypes
libc = ctypes.CDLL(None)

# Определяем CTL_KERN и KERN_HOSTNAME
CTL_KERN = 1
KERN_HOSTNAME = 10

# MIB (Management Information Base)
mib = (ctypes.c_int * 2)(CTL_KERN, KERN_HOSTNAME)

# Буфер для результата
buf = ctypes.create_string_buffer(256)
buf_len = ctypes.c_size_t(256)

# Вызов sysctl
result = libc.sysctl(
    mib, 2,
    buf, ctypes.byref(buf_len),
    None, 0
)

if result == 0:
    print(f"Hostname via sysctl: {buf.value.decode()}")
```

### 5.4 Типы данных ctypes

| Python | C | ctypes |
|--------|---|--------|
| int | int | c_int |
| int | long | c_long |
| int | size_t | c_size_t |
| bytes | char* | c_char_p |
| str | wchar_t* | c_wchar_p |
| None | void* | c_void_p |

---

## 6. Практика: системная утилита

### 6.1 Простая версия ls

```python
#!/usr/bin/env python3
"""Простая реализация ls."""

import os
import sys
import stat
import pwd
import grp
from datetime import datetime

def format_mode(mode):
    """Форматировать права доступа как ls -l."""
    result = ""
    
    # Тип файла
    if stat.S_ISDIR(mode):
        result += "d"
    elif stat.S_ISLNK(mode):
        result += "l"
    elif stat.S_ISREG(mode):
        result += "-"
    else:
        result += "?"
    
    # Права доступа
    for who in ("USR", "GRP", "OTH"):
        for perm in ("R", "W", "X"):
            if mode & getattr(stat, f"S_I{perm}{who}"):
                result += perm.lower()
            else:
                result += "-"
    
    return result

def format_size(size):
    """Форматировать размер файла."""
    for unit in ("", "K", "M", "G", "T"):
        if size < 1024:
            return f"{size:>5.1f}{unit}"
        size /= 1024
    return f"{size:.1f}P"

def list_directory(path="."):
    """Вывести содержимое каталога."""
    try:
        entries = os.listdir(path)
    except PermissionError:
        print(f"ls: {path}: Permission denied", file=sys.stderr)
        return
    
    entries.sort()
    
    for entry in entries:
        if entry.startswith("."):
            continue  # Пропустить скрытые
        
        full_path = os.path.join(path, entry)
        
        try:
            st = os.lstat(full_path)
        except OSError:
            continue
        
        # Форматирование
        mode = format_mode(st.st_mode)
        nlink = st.st_nlink
        
        try:
            owner = pwd.getpwuid(st.st_uid).pw_name
        except KeyError:
            owner = str(st.st_uid)
        
        try:
            group = grp.getgrgid(st.st_gid).gr_name
        except KeyError:
            group = str(st.st_gid)
        
        size = format_size(st.st_size)
        mtime = datetime.fromtimestamp(st.st_mtime).strftime("%b %d %H:%M")
        
        print(f"{mode} {nlink:>3} {owner:<8} {group:<8} {size} {mtime} {entry}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    list_directory(path)
```

**Output:**
```
$ python3 myls.py /etc
drwxr-xr-x   2 root     wheel     512B Dec  1 10:00 ssh
-rw-r--r--   1 root     wheel     1.8K Nov 15 14:30 passwd
-rw-r--r--   1 root     wheel     2.1K Nov 15 14:30 group
...
```

### 6.2 Версия ps (список процессов)

```python
#!/usr/bin/env python3
"""Простая реализация ps."""

import os

def list_processes():
    """Вывести список процессов из /proc (Linux) или sysctl (BSD)."""
    
    # На Linux используем /proc
    if os.path.exists("/proc"):
        for pid in os.listdir("/proc"):
            if not pid.isdigit():
                continue
            
            try:
                # Читаем командную строку
                with open(f"/proc/{pid}/comm") as f:
                    comm = f.read().strip()
                
                # Читаем статус
                with open(f"/proc/{pid}/status") as f:
                    status = {}
                    for line in f:
                        if ":" in line:
                            key, value = line.split(":", 1)
                            status[key.strip()] = value.strip()
                
                uid = status.get("Uid", "?").split()[0]
                print(f"{pid:>6} {uid:>6} {comm}")
                
            except (OSError, PermissionError):
                continue
    else:
        # На BSD используем sysctl (упрощённо)
        print("BSD process listing requires different approach")
        print("Use: os.popen('ps aux').read()")

if __name__ == "__main__":
    list_processes()
```

---

## 7. Отладка системных программ

### 7.1 ktrace на OpenBSD

```bash
# Трассировка всех syscalls
$ ktrace python3 myscript.py
$ kdump | less

# Только определённые syscalls
$ ktrace -tc python3 myscript.py  # Syscalls
$ ktrace -ti python3 myscript.py  # I/O
$ ktrace -tn python3 myscript.py  # Namei (lookups)
```

### 7.2 strace на Linux

```bash
# Все syscalls
$ strace python3 myscript.py

# Только определённые
$ strace -e trace=open,read,write python3 myscript.py

# Статистика
$ strace -c python3 myscript.py
```

### 7.3 Пример вывода ktrace

```
$ ktrace python3 -c "open('/etc/passwd').read()"
$ kdump
  1234 python3  CALL  openat(AT_FDCWD,"/etc/passwd",O_RDONLY|O_CLOEXEC)
  1234 python3  RET   openat 3
  1234 python3  CALL  fstat(3,0x7f7fffffd8b0)
  1234 python3  RET   fstat 0
  1234 python3  CALL  read(3,0x5678901234,8192)
  1234 python3  RET   read 1843
  1234 python3  CALL  close(3)
  1234 python3  RET   close 0
```

### 7.4 Логирование в системных программах

```python
import logging
import sys

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('/var/log/myapp.log'),
        logging.StreamHandler(sys.stderr)
    ]
)

logger = logging.getLogger('myapp')

def main():
    logger.info("Application started")
    logger.debug(f"PID: {os.getpid()}")
    
    try:
        # ... код ...
        pass
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
```

---

## 8. Особенности OpenBSD

### 8.1 pledge и unveil в Python

OpenBSD предоставляет уникальные механизмы безопасности:

```python
# На OpenBSD можно использовать pledge через ctypes
import ctypes

libc = ctypes.CDLL(None)

def pledge(promises, execpromises=None):
    """Вызвать pledge(2)."""
    promises_b = promises.encode() if promises else None
    exec_b = execpromises.encode() if execpromises else None
    result = libc.pledge(promises_b, exec_b)
    if result == -1:
        raise OSError("pledge failed")

def unveil(path, permissions):
    """Вызвать unveil(2)."""
    path_b = path.encode() if path else None
    perm_b = permissions.encode() if permissions else None
    result = libc.unveil(path_b, perm_b)
    if result == -1:
        raise OSError("unveil failed")

# Пример использования
unveil("/etc", "r")
unveil("/tmp", "rwc")
unveil(None, None)  # Закрыть добавление путей

pledge("stdio rpath wpath cpath")

# Теперь программа ограничена!
```

> **🐡 OpenBSD-specific:**  
> pledge и unveil работают только на OpenBSD. На других системах эти вызовы вернут ошибку.

### 8.2 Проверка платформы

```python
import sys
import platform

# Проверка ОС
if sys.platform == "openbsd7":
    print("Running on OpenBSD")
elif sys.platform == "linux":
    print("Running on Linux")
elif sys.platform == "darwin":
    print("Running on macOS")

# Детальная информация
print(f"Platform: {platform.platform()}")
print(f"System: {platform.system()}")
print(f"Release: {platform.release()}")
```

---

## 💡 Key Takeaways

- **Системное программирование** — прямое взаимодействие с ОС через syscalls
- **Модуль os** — основной инструмент для системного программирования в Python
- **EAFP > LBYL** — ловите исключения вместо предварительных проверок
- **ctypes** — позволяет вызывать любые C-функции
- **ktrace/strace** — незаменимые инструменты отладки

---

## 🚀 Next Steps

**Related Modules:**
- [Files & I/O](../02_FilesAndIO/) — низкоуровневая работа с файлами
- [Processes](../04_Processes/) — управление процессами

**Practice Ideas:**
1. Напишите свою версию `pwd` с использованием `os.getcwd()`
2. Создайте утилиту `env` для вывода переменных окружения
3. Реализуйте `id` для вывода UID/GID
4. Используйте `ktrace` для анализа любой программы

**Going Deeper:**
- Изучите исходники CPython (`Modules/posixmodule.c`)
- Прочитайте man-страницы основных syscalls
- Попробуйте cffi как альтернативу ctypes

---

## 📚 Additional Resources

**Documentation:**
- [Python os module](https://docs.python.org/3/library/os.html)
- [man intro(2)](https://man.openbsd.org/intro.2) — введение в syscalls
- [man ktrace](https://man.openbsd.org/ktrace)

**Books:**
- "Advanced Programming in the UNIX Environment" — классика
- "The Linux Programming Interface" — современный справочник

---

