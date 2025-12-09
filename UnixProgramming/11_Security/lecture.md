# Security
## Безопасность: pledge, unveil и другие механизмы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [Processes](../04_Processes/) и [Files](../02_FilesAndIO/)
- Понимать права доступа Unix
- Знать основы безопасности ОС

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать pledge для ограничения syscalls
- Применять unveil для ограничения доступа к ФС
- Понимать chroot и его ограничения
- Сбрасывать привилегии в программах
- Писать безопасный системный код
- Применять принцип минимальных привилегий

---

## 1. Принцип минимальных привилегий

### 1.1 Defense in Depth

```
┌─────────────────────────────────────────────────────────┐
│                    Application                           │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Input Validation                              │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Pledge (syscall restrictions)                 │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Unveil (filesystem restrictions)              │
├─────────────────────────────────────────────────────────┤
│  Layer 4: chroot/sandbox                                │
├─────────────────────────────────────────────────────────┤
│  Layer 5: User separation (drop privileges)             │
├─────────────────────────────────────────────────────────┤
│                    Kernel                               │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Порядок применения

1. **Инициализация** — полные права
2. **Загрузка конфигурации** — чтение файлов
3. **Открытие сокетов/файлов** — сетевые операции
4. **Сброс привилегий** — setuid/setgid
5. **Ограничение syscalls** — pledge
6. **Ограничение ФС** — unveil
7. **Основная работа** — минимальные права

---

## 2. pledge — ограничение системных вызовов

### 2.1 Что такое pledge (OpenBSD)

**pledge** ограничивает набор syscalls, доступных процессу.

```python
import ctypes

libc = ctypes.CDLL(None)

def pledge(promises, execpromises=None):
    """
    Ограничить syscalls процесса.
    
    promises: строка с разрешёнными операциями
    execpromises: права для exec'd процессов
    """
    promises_b = promises.encode() if promises else None
    exec_b = execpromises.encode() if execpromises else None
    
    result = libc.pledge(promises_b, exec_b)
    if result == -1:
        raise OSError("pledge failed")
    
    return result

# Пример использования
try:
    # Разрешить только stdio, rpath, inet
    pledge("stdio rpath inet")
    print("Pledge set successfully")
except OSError as e:
    print(f"Pledge error (not on OpenBSD?): {e}")
```

### 2.2 Основные promises

| Promise | Описание |
|---------|----------|
| `stdio` | Базовый I/O (read, write, close) |
| `rpath` | Чтение файлов |
| `wpath` | Запись файлов |
| `cpath` | Создание/удаление файлов |
| `dpath` | Создание устройств |
| `tmppath` | /tmp операции |
| `inet` | Сетевые операции (IPv4/IPv6) |
| `unix` | Unix domain sockets |
| `dns` | DNS запросы |
| `getpw` | getpwnam и подобные |
| `proc` | fork, exec |
| `exec` | execve |
| `id` | setuid, setgid |
| `tty` | Операции с терминалом |

### 2.3 Пример: безопасный HTTP клиент

```python
#!/usr/bin/env python3
"""HTTP клиент с pledge."""

import ctypes
import socket
import sys

libc = ctypes.CDLL(None)

def pledge(promises, execpromises=None):
    promises_b = promises.encode() if promises else None
    exec_b = execpromises.encode() if execpromises else None
    result = libc.pledge(promises_b, exec_b)
    if result == -1:
        raise OSError("pledge failed")

def http_get(host, path="/"):
    # До pledge — полные права
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 80))
    
    # После соединения — ограничить до stdio
    try:
        pledge("stdio")
    except OSError:
        pass  # Не на OpenBSD
    
    # Теперь можем только читать/писать
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())
    
    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
    
    sock.close()
    return response.decode()

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    print(http_get(host))
```

---

## 3. unveil — ограничение файловой системы

### 3.1 Что такое unveil (OpenBSD)

**unveil** ограничивает видимость файловой системы для процесса.

```python
import ctypes

libc = ctypes.CDLL(None)

def unveil(path, permissions):
    """
    Ограничить доступ к файловой системе.
    
    path: путь к файлу/директории
    permissions: комбинация r/w/x/c
        r - чтение
        w - запись
        x - выполнение
        c - создание
    """
    path_b = path.encode() if path else None
    perm_b = permissions.encode() if permissions else None
    
    result = libc.unveil(path_b, perm_b)
    if result == -1:
        raise OSError("unveil failed")
    
    return result

# Пример
try:
    unveil("/etc", "r")          # Только чтение /etc
    unveil("/tmp", "rwc")        # Полный доступ к /tmp
    unveil("/var/log", "w")      # Только запись логов
    unveil(None, None)           # Закрыть добавление путей
    
    print("Unveil set successfully")
except OSError as e:
    print(f"Unveil error: {e}")
```

### 3.2 Пример: безопасный файловый сервер

```python
#!/usr/bin/env python3
"""Файловый сервер с unveil."""

import ctypes
import os
import socket

libc = ctypes.CDLL(None)

def pledge(promises, execpromises=None):
    promises_b = promises.encode() if promises else None
    exec_b = execpromises.encode() if execpromises else None
    if libc.pledge(promises_b, exec_b) == -1:
        raise OSError("pledge failed")

def unveil(path, permissions):
    path_b = path.encode() if path else None
    perm_b = permissions.encode() if permissions else None
    if libc.unveil(path_b, perm_b) == -1:
        raise OSError("unveil failed")

def file_server(root_dir, port=8080):
    """Простой файловый сервер."""
    
    # Ограничить видимость ФС
    try:
        unveil(root_dir, "r")  # Только чтение из root_dir
        unveil(None, None)     # Закрыть unveil
    except OSError:
        print("Warning: unveil not available")
    
    # Создать сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    
    # Ограничить syscalls
    try:
        pledge("stdio rpath inet")
    except OSError:
        print("Warning: pledge not available")
    
    print(f"File server on port {port}, serving {root_dir}")
    
    while True:
        client, addr = server.accept()
        handle_client(client, root_dir)

def handle_client(client, root_dir):
    try:
        request = client.recv(1024).decode()
        # Простой парсинг GET запроса
        path = request.split()[1] if request else "/"
        
        # Защита от path traversal
        full_path = os.path.normpath(os.path.join(root_dir, path.lstrip("/")))
        if not full_path.startswith(root_dir):
            client.sendall(b"HTTP/1.1 403 Forbidden\r\n\r\nForbidden")
            return
        
        try:
            with open(full_path, "rb") as f:
                content = f.read()
            response = b"HTTP/1.1 200 OK\r\n\r\n" + content
        except FileNotFoundError:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nNot Found"
        except PermissionError:
            response = b"HTTP/1.1 403 Forbidden\r\n\r\nForbidden"
        
        client.sendall(response)
    finally:
        client.close()

if __name__ == "__main__":
    file_server("/var/www", 8080)
```

---

## 4. Сброс привилегий

### 4.1 setuid/setgid

```python
import os
import pwd
import grp

def drop_privileges(user="nobody", group="nogroup"):
    """Сбросить привилегии до непривилегированного пользователя."""
    
    if os.getuid() != 0:
        print("Not running as root, no privileges to drop")
        return
    
    # Получить UID и GID
    pw = pwd.getpwnam(user)
    uid = pw.pw_uid
    gid = grp.getgrnam(group).gr_gid
    
    # Сначала сменить группу (пока ещё root)
    os.setgroups([])  # Очистить дополнительные группы
    os.setgid(gid)
    os.setegid(gid)
    
    # Затем сменить пользователя
    os.setuid(uid)
    os.seteuid(uid)
    
    # Проверить
    assert os.getuid() == uid
    assert os.getgid() == gid
    
    print(f"Dropped privileges to {user}:{group}")

# Использование в демоне
def secure_daemon():
    # 1. Открыть привилегированный порт как root
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 80))  # Требует root
    server.listen(5)
    
    # 2. Сбросить привилегии
    drop_privileges("www-data", "www-data")
    
    # 3. Работать как непривилегированный пользователь
    # Сокет остаётся открытым!
```

### 4.2 Проверка привилегий

```python
import os

def require_root():
    """Проверить, что программа запущена от root."""
    if os.geteuid() != 0:
        raise PermissionError("This program requires root privileges")

def is_privileged():
    """Проверить, есть ли дополнительные привилегии."""
    return os.geteuid() == 0 or os.getuid() != os.geteuid()
```

---

## 5. chroot — изоляция файловой системы

### 5.1 Что такое chroot

```python
import os

def setup_chroot(new_root):
    """Изолировать процесс в директорию."""
    
    # Требует root
    if os.geteuid() != 0:
        raise PermissionError("chroot requires root")
    
    # Сменить корень
    os.chroot(new_root)
    
    # Сменить рабочую директорию
    os.chdir("/")
    
    print(f"Chrooted to {new_root}")

# После chroot "/" указывает на new_root
```

### 5.2 Ограничения chroot

⚠️ **chroot НЕ является полноценной песочницей:**

- Root может выбраться из chroot
- Не изолирует сеть
- Не изолирует процессы
- Не ограничивает syscalls

```python
# Как root может выбраться из chroot:
# 1. Создать device node (mknod)
# 2. Использовать ptrace на процесс вне chroot
# 3. Открыть fd до chroot и использовать fchdir
```

### 5.3 Безопасный chroot

```python
import os
import pwd

def secure_chroot(new_root, user="nobody"):
    """Безопасный chroot с потерей привилегий."""
    
    # 1. Открыть нужные файлы/сокеты ДО chroot
    # ...
    
    # 2. chroot
    os.chroot(new_root)
    os.chdir("/")
    
    # 3. Сбросить привилегии
    pw = pwd.getpwnam(user)
    os.setgroups([])
    os.setgid(pw.pw_gid)
    os.setuid(pw.pw_uid)
    
    # Теперь выбраться из chroot невозможно
```

---

## 6. Безопасная работа с данными

### 6.1 Очистка памяти

```python
import ctypes
import sys

def secure_zero(data):
    """Очистить байты в памяти."""
    if isinstance(data, bytearray):
        for i in range(len(data)):
            data[i] = 0
    elif isinstance(data, memoryview):
        for i in range(len(data)):
            data[i] = 0

def secure_string_del(s):
    """Попытка очистить строку (не гарантирует успех в Python)."""
    # В Python строки неизменяемы, это лучшее что можем сделать
    # Реально безопасная работа с секретами требует специальных библиотек
    pass

# Использование
password = bytearray(b"secret")
# ... использование пароля ...
secure_zero(password)  # Очистить после использования
```

### 6.2 Безопасное сравнение

```python
import hmac

def secure_compare(a, b):
    """Сравнение за константное время."""
    # Защита от timing attacks
    return hmac.compare_digest(a, b)

# НЕПРАВИЛЬНО (timing attack):
# if token == expected_token:

# ПРАВИЛЬНО:
if secure_compare(token.encode(), expected_token.encode()):
    print("Valid token")
```

### 6.3 Безопасная генерация случайных данных

```python
import os
import secrets

# os.urandom — криптографически стойкий
random_bytes = os.urandom(32)

# secrets — высокоуровневый API (Python 3.6+)
token = secrets.token_hex(32)
url_safe = secrets.token_urlsafe(32)
random_int = secrets.randbelow(100)

# НЕ использовать random для безопасности!
# import random  # НЕ криптографически стойкий
```

---

## 7. Практические примеры

### 7.1 Безопасный демон

```python
#!/usr/bin/env python3
"""Безопасный демон с pledge/unveil."""

import os
import sys
import pwd
import socket
import ctypes

libc = ctypes.CDLL(None)

def pledge(promises, execpromises=None):
    promises_b = promises.encode() if promises else None
    exec_b = execpromises.encode() if execpromises else None
    if libc.pledge(promises_b, exec_b) == -1:
        raise OSError("pledge failed")

def unveil(path, permissions):
    path_b = path.encode() if path else None
    perm_b = permissions.encode() if permissions else None
    if libc.unveil(path_b, perm_b) == -1:
        raise OSError("unveil failed")

def drop_privileges(user="nobody"):
    if os.getuid() != 0:
        return
    
    pw = pwd.getpwnam(user)
    os.setgroups([])
    os.setgid(pw.pw_gid)
    os.setuid(pw.pw_uid)

def secure_daemon(config_path, port=8080):
    """Запустить безопасный демон."""
    
    # 1. Прочитать конфигурацию (ещё с полными правами)
    with open(config_path) as f:
        config = f.read()
    print(f"Config loaded from {config_path}")
    
    # 2. Открыть привилегированный порт
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"Listening on port {port}")
    
    # 3. Ограничить файловую систему
    try:
        unveil("/var/log", "w")
        unveil(None, None)
        print("Filesystem restricted with unveil")
    except OSError:
        print("Warning: unveil not available")
    
    # 4. Сбросить привилегии
    drop_privileges("daemon")
    print(f"Running as UID {os.getuid()}")
    
    # 5. Ограничить syscalls
    try:
        pledge("stdio inet")
        print("Syscalls restricted with pledge")
    except OSError:
        print("Warning: pledge not available")
    
    # 6. Основной цикл
    print("Daemon ready")
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client.sendall(b"Hello from secure daemon\n")
        client.close()

if __name__ == "__main__":
    if os.getuid() != 0:
        print("This daemon requires root to bind to privileged ports")
        sys.exit(1)
    
    secure_daemon("/etc/daemon.conf", 80)
```

### 7.2 Обёртка для pledge/unveil

```python
#!/usr/bin/env python3
"""Модуль для работы с pledge/unveil."""

import ctypes
import os
import sys

class SecurityError(Exception):
    pass

class OpenBSDSecurity:
    """Обёртка над pledge/unveil."""
    
    def __init__(self):
        self.libc = ctypes.CDLL(None)
        self._pledged = False
        self._unveiled = False
        self._unveil_locked = False
    
    def is_openbsd(self):
        """Проверить, работаем ли на OpenBSD."""
        return sys.platform.startswith("openbsd")
    
    def pledge(self, promises, execpromises=None):
        """Ограничить syscalls."""
        if not self.is_openbsd():
            return False
        
        promises_b = promises.encode() if promises else None
        exec_b = execpromises.encode() if execpromises else None
        
        result = self.libc.pledge(promises_b, exec_b)
        if result == -1:
            raise SecurityError("pledge failed")
        
        self._pledged = True
        return True
    
    def unveil(self, path, permissions):
        """Ограничить доступ к пути."""
        if not self.is_openbsd():
            return False
        
        if self._unveil_locked:
            raise SecurityError("unveil already locked")
        
        path_b = path.encode() if path else None
        perm_b = permissions.encode() if permissions else None
        
        result = self.libc.unveil(path_b, perm_b)
        if result == -1:
            raise SecurityError("unveil failed")
        
        if path is None and permissions is None:
            self._unveil_locked = True
        
        self._unveiled = True
        return True
    
    def lock_unveil(self):
        """Закрыть возможность добавления путей."""
        return self.unveil(None, None)

# Глобальный экземпляр
security = OpenBSDSecurity()

# Использование
if security.is_openbsd():
    security.unveil("/etc", "r")
    security.unveil("/tmp", "rwc")
    security.lock_unveil()
    security.pledge("stdio rpath wpath cpath")
```

---

## 💡 Key Takeaways

- **pledge** — ограничивает syscalls (только нужные операции)
- **unveil** — ограничивает видимость ФС (только нужные файлы)
- **Порядок важен**: открыть ресурсы → ограничить права
- **Drop privileges** — минимальные права для работы
- **chroot** — не замена настоящей песочнице

---

## 🚀 Next Steps

**Related Modules:**
- [Daemons](../12_Daemons/) — создание демонов с безопасностью

**Practice Ideas:**
1. Создайте безопасный файловый сервер с pledge/unveil
2. Напишите демон с полной изоляцией
3. Реализуйте sandbox для выполнения скриптов
4. Создайте аудит безопасности для своего приложения

**Going Deeper:**
- seccomp-bpf на Linux
- Capsicum на FreeBSD
- SELinux/AppArmor
- Containers и namespaces

---

## 📚 Additional Resources

**Documentation:**
- [man pledge(2)](https://man.openbsd.org/pledge.2)
- [man unveil(2)](https://man.openbsd.org/unveil.2)
- [man chroot(2)](https://man.openbsd.org/chroot.2)
- [OpenBSD Security](https://www.openbsd.org/security.html)

---

