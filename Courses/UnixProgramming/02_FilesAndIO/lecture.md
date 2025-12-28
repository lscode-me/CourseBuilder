# Files and Low-Level I/O
## Файлы и низкоуровневый ввод-вывод

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [Intro](../01_Intro/)
- Понимать работу с файлами в Python (open, read, write)
- Знать основы файловой системы Unix

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с файловыми дескрипторами напрямую
- Понимать разницу между buffered и unbuffered I/O
- Использовать os.open, os.read, os.write
- Управлять позицией чтения/записи с помощью seek
- Применять файловые блокировки (fcntl)
- Создавать временные файлы безопасно

---

## 1. Файловые дескрипторы

### 1.1 Что такое файловый дескриптор

**Файловый дескриптор (fd)** — целое число, идентифицирующее открытый файл в процессе.

```

┌─────────────────────────────────────────────────────┐
│                    Process                          │
├─────────────────────────────────────────────────────┤
│  fd 0 → stdin  (стандартный ввод)                   │
│  fd 1 → stdout (стандартный вывод)                  │
│  fd 2 → stderr (стандартный вывод ошибок)           │
│  fd 3 → /etc/passwd                                 │
│  fd 4 → socket                                      │
│  ...                                                │
└─────────────────────────────────────────────────────┘

```

```python

import sys

# Стандартные дескрипторы
print(f"stdin fd: {sys.stdin.fileno()}")   # 0
print(f"stdout fd: {sys.stdout.fileno()}")  # 1
print(f"stderr fd: {sys.stderr.fileno()}")  # 2

```

**Output:**
```

stdin fd: 0
stdout fd: 1
stderr fd: 2

```

### 1.2 Связь между fd и файловыми объектами Python

```python
# Высокоуровневый Python файл — обёртка над fd
f = open("/etc/passwd", "r")
print(f"File object: {f}")
print(f"File descriptor: {f.fileno()}")
f.close()

```

**Output:**
```

File object: <_io.TextIOWrapper name='/etc/passwd' mode='r' encoding='UTF-8'>
File descriptor: 3

```

---

## 2. Низкоуровневые операции с файлами

### 2.1 os.open — открытие файла

```python

import os

# Открыть файл для чтения
fd = os.open("/etc/passwd", os.O_RDONLY)
print(f"Opened fd: {fd}")

# Обязательно закрыть!
os.close(fd)

```

**Флаги открытия:**

| Флаг | Описание |
|------|----------|
| `O_RDONLY` | Только чтение |
| `O_WRONLY` | Только запись |
| `O_RDWR` | Чтение и запись |
| `O_CREAT` | Создать если не существует |
| `O_EXCL` | Ошибка если существует (с O_CREAT) |
| `O_TRUNC` | Обрезать до нуля |
| `O_APPEND` | Дописывать в конец |
| `O_NONBLOCK` | Неблокирующий режим |
| `O_SYNC` | Синхронная запись |
| `O_CLOEXEC` | Закрыть при exec |

```python

import os

# Создать новый файл (или ошибка если существует)
fd = os.open(
    "/tmp/test.txt",
    os.O_WRONLY | os.O_CREAT | os.O_EXCL,
    0o644  # права доступа
)

# Создать или обрезать существующий
fd = os.open(
    "/tmp/test.txt",
    os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
    0o644
)

```

### 2.2 os.read и os.write

```python

import os

# Открыть для чтения
fd = os.open("/etc/passwd", os.O_RDONLY)

# Прочитать до 100 байт
data = os.read(fd, 100)
print(f"Read {len(data)} bytes")
print(data.decode())

os.close(fd)

```

**Output:**
```

Read 100 bytes
root:*:0:0:Charlie &:/root:/bin/ksh
daemon:*:1:1:The devil himself:/root:/sbin/n

```

```python

import os

# Открыть для записи
fd = os.open("/tmp/output.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

# Записать данные (должны быть bytes!)
message = "Hello, Unix!\n"
written = os.write(fd, message.encode())
print(f"Written {written} bytes")

os.close(fd)

```

### 2.3 Полное чтение файла

```python

import os

def read_file_low_level(path):
    """Прочитать весь файл через низкоуровневый API."""
    fd = os.open(path, os.O_RDONLY)
    try:
        chunks = []
        while True:
            chunk = os.read(fd, 8192)  # Читать блоками по 8KB
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(fd)

content = read_file_low_level("/etc/passwd")
print(content.decode())

```

### 2.4 Копирование файла

```python

import os

def copy_file(src, dst, buffer_size=8192):
    """Копировать файл низкоуровневыми операциями."""
    # Получить права исходного файла
    src_stat = os.stat(src)
    mode = src_stat.st_mode & 0o777
    
    src_fd = os.open(src, os.O_RDONLY)
    try:
        dst_fd = os.open(dst, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, mode)
        try:
            while True:
                data = os.read(src_fd, buffer_size)
                if not data:
                    break
                os.write(dst_fd, data)
        finally:
            os.close(dst_fd)
    finally:
        os.close(src_fd)

copy_file("/etc/passwd", "/tmp/passwd_copy")

```

---

## 3. Позиционирование в файле

### 3.1 os.lseek

```python

import os

fd = os.open("/etc/passwd", os.O_RDONLY)

# Прочитать первые 10 байт
data = os.read(fd, 10)
print(f"First 10 bytes: {data}")

# Вернуться в начало
os.lseek(fd, 0, os.SEEK_SET)

# Прочитать снова
data = os.read(fd, 10)
print(f"After seek: {data}")

# Перейти к позиции 100
os.lseek(fd, 100, os.SEEK_SET)

# Перейти на 50 байт вперёд от текущей позиции
os.lseek(fd, 50, os.SEEK_CUR)

# Перейти к концу файла
os.lseek(fd, 0, os.SEEK_END)

# Узнать текущую позицию
position = os.lseek(fd, 0, os.SEEK_CUR)
print(f"File size: {position}")

os.close(fd)

```

**Константы SEEK:**

| Константа | Описание |
|-----------|----------|
| `SEEK_SET` | От начала файла |
| `SEEK_CUR` | От текущей позиции |
| `SEEK_END` | От конца файла |

### 3.2 Создание sparse файла

```python

import os

# Sparse файл — файл с "дырками" (нулевые участки не занимают место)
fd = os.open("/tmp/sparse.dat", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

# Записать в начало
os.write(fd, b"START")

# Перепрыгнуть на 1GB
os.lseek(fd, 1024 * 1024 * 1024, os.SEEK_SET)

# Записать в конец
os.write(fd, b"END")

os.close(fd)

# Проверить размеры
stat = os.stat("/tmp/sparse.dat")
print(f"Apparent size: {stat.st_size} bytes")
print(f"Actual blocks: {stat.st_blocks * 512} bytes")

```

**Output:**
```

Apparent size: 1073741828 bytes
Actual blocks: 8192 bytes

```

---

## 4. Buffered vs Unbuffered I/O

### 4.1 Разница между уровнями

```

┌────────────────────────────────────────────────────┐
│            Python high-level I/O                   │
│   open(), file.read(), file.write()                │
│              ↓ (Python buffer)                     │
├────────────────────────────────────────────────────┤
│               C stdio library                      │
│        fopen(), fread(), fwrite()                  │
│              ↓ (stdio buffer)                      │
├────────────────────────────────────────────────────┤
│            Kernel system calls                     │
│          open(), read(), write()                   │
│              ↓ (kernel buffer)                     │
├────────────────────────────────────────────────────┤
│                  Disk                              │
└────────────────────────────────────────────────────┘

```

### 4.2 Буферизация Python

```python
# Полная буферизация (по умолчанию для файлов)
f = open("/tmp/test.txt", "w")
f.write("Hello")  # Данные в буфере Python
f.flush()         # Отправить в ядро
f.close()         # Автоматически flush

# Строковая буферизация (для текстовых файлов с tty)
f = open("/tmp/test.txt", "w", buffering=1)

# Без буферизации (только для бинарных)
f = open("/tmp/test.txt", "wb", buffering=0)

```

### 4.3 Когда использовать unbuffered I/O

✅ **Используйте unbuffered когда:**

- Важна немедленная запись (логи)
- Работаете с устройствами
- Несколько процессов пишут в файл
- Критична производительность больших блоков

❌ **Не используйте unbuffered когда:**

- Много мелких операций чтения/записи
- Обрабатываете текст построчно

```python

import os

# Unbuffered write — данные сразу идут в ядро
fd = os.open("/var/log/myapp.log", os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
os.write(fd, b"Log message\n")  # Сразу на диске (после sync ядра)
os.close(fd)

```

### 4.4 os.fsync и os.fdatasync

```python

import os

fd = os.open("/tmp/important.dat", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

os.write(fd, b"Critical data")

# fsync — гарантирует запись данных И метаданных на диск
os.fsync(fd)

# fdatasync — только данные (быстрее, но не обновляет mtime)
# os.fdatasync(fd)  # Не на всех системах

os.close(fd)

```

---

## 5. Дублирование дескрипторов

### 5.1 os.dup и os.dup2

```python

import os

# dup — создать копию дескриптора
fd = os.open("/tmp/test.txt", os.O_WRONLY | os.O_CREAT, 0o644)
fd_copy = os.dup(fd)

print(f"Original fd: {fd}")
print(f"Duplicated fd: {fd_copy}")

# Оба указывают на один файл
os.write(fd, b"Hello ")
os.write(fd_copy, b"World\n")

os.close(fd)
os.close(fd_copy)

```

### 5.2 Перенаправление stdout

```python

import os
import sys

def redirect_stdout_to_file(filename):
    """Перенаправить stdout в файл."""
    # Сохранить оригинальный stdout
    saved_stdout = os.dup(1)
    
    # Открыть файл
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    
    # Заменить fd 1 (stdout) на наш файл
    os.dup2(fd, 1)
    os.close(fd)
    
    return saved_stdout

def restore_stdout(saved_fd):
    """Восстановить оригинальный stdout."""
    os.dup2(saved_fd, 1)
    os.close(saved_fd)

# Использование
saved = redirect_stdout_to_file("/tmp/output.log")

print("This goes to file")  # Пишется в файл!

restore_stdout(saved)

print("This goes to terminal")  # Снова на экран

```

### 5.3 Пример: логирование stderr

```python

import os
import sys
from datetime import datetime

class StderrLogger:
    """Перенаправление stderr с добавлением timestamp."""
    
    def __init__(self, log_path):
        self.log_fd = os.open(
            log_path,
            os.O_WRONLY | os.O_CREAT | os.O_APPEND,
            0o644
        )
        self.saved_stderr = os.dup(2)
        os.dup2(self.log_fd, 2)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        os.dup2(self.saved_stderr, 2)
        os.close(self.saved_stderr)
        os.close(self.log_fd)

# Использование
with StderrLogger("/tmp/error.log"):
    print("Error message", file=sys.stderr)

```

---

## 6. Файловые блокировки

### 6.1 fcntl — управление дескрипторами

```python

import fcntl
import os
import struct

def lock_file(fd, exclusive=True, blocking=True):
    """Заблокировать файл."""
    if exclusive:
        lock_type = fcntl.LOCK_EX  # Эксклюзивная (для записи)
    else:
        lock_type = fcntl.LOCK_SH  # Разделяемая (для чтения)
    
    if not blocking:
        lock_type |= fcntl.LOCK_NB  # Не блокировать
    
    try:
        fcntl.flock(fd, lock_type)
        return True
    except BlockingIOError:
        return False  # Файл уже заблокирован

def unlock_file(fd):
    """Разблокировать файл."""
    fcntl.flock(fd, fcntl.LOCK_UN)

```

### 6.2 Практический пример: блокировка PID файла

```python

import os
import fcntl
import sys

class PidFile:
    """PID файл с блокировкой для singleton процессов."""
    
    def __init__(self, path):
        self.path = path
        self.fd = None
    
    def acquire(self):
        """Получить блокировку."""
        self.fd = os.open(
            self.path,
            os.O_WRONLY | os.O_CREAT,
            0o644
        )
        
        try:
            # Неблокирующая эксклюзивная блокировка
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(self.fd)
            self.fd = None
            return False
        
        # Обрезать и записать PID
        os.ftruncate(self.fd, 0)
        os.write(self.fd, f"{os.getpid()}\n".encode())
        os.fsync(self.fd)
        
        return True
    
    def release(self):
        """Освободить блокировку."""
        if self.fd is not None:
            fcntl.flock(self.fd, fcntl.LOCK_UN)
            os.close(self.fd)
            os.unlink(self.path)
            self.fd = None
    
    def __enter__(self):
        if not self.acquire():
            raise RuntimeError("Another instance is running")
        return self
    
    def __exit__(self, *args):
        self.release()

# Использование
try:
    with PidFile("/var/run/myapp.pid"):
        print("Application running...")
        # ... работа приложения ...
except RuntimeError as e:
    print(f"Error: {e}")
    sys.exit(1)

```

### 6.3 Типы блокировок

| Тип | Описание | Использование |
|-----|----------|---------------|
| `LOCK_SH` | Shared (читатели) | Несколько процессов могут читать |
| `LOCK_EX` | Exclusive (писатели) | Только один процесс |
| `LOCK_NB` | Non-blocking | Не ждать, вернуть ошибку |
| `LOCK_UN` | Unlock | Снять блокировку |

---

## 7. Временные файлы

### 7.1 Безопасное создание временных файлов

```python

import os
import tempfile

# Небезопасно! Race condition
# bad_path = "/tmp/myapp_temp"  # Кто-то может создать раньше!

# Безопасно: tempfile модуль
with tempfile.NamedTemporaryFile(delete=False) as f:
    print(f"Temp file: {f.name}")
    f.write(b"Temporary data")
    temp_path = f.name

# Файл существует после выхода из with (delete=False)
print(f"File exists: {os.path.exists(temp_path)}")

# Удалить вручную
os.unlink(temp_path)

```

### 7.2 os.mkstemp — низкоуровневый аналог

```python

import os

# Создать временный файл и вернуть (fd, path)
fd, path = tempfile.mkstemp(prefix="myapp_", suffix=".tmp")

print(f"Created: {path}")

os.write(fd, b"Data")
os.close(fd)

# Не забыть удалить!
os.unlink(path)

```

### 7.3 Временные директории

```python

import tempfile
import shutil
import os

# Создать временную директорию
temp_dir = tempfile.mkdtemp(prefix="myapp_")
print(f"Temp dir: {temp_dir}")

# Использовать...
with open(os.path.join(temp_dir, "file.txt"), "w") as f:
    f.write("Data")

# Удалить со всем содержимым
shutil.rmtree(temp_dir)

```

### 7.4 Context manager для временных файлов

```python

import os
import tempfile
from contextlib import contextmanager

@contextmanager
def atomic_write(path, mode=0o644):
    """Атомарная запись файла через временный файл."""
    dir_path = os.path.dirname(path) or "."
    fd, temp_path = tempfile.mkstemp(dir=dir_path)
    
    try:
        # Записать во временный файл
        yield fd
        os.fsync(fd)
        os.close(fd)
        
        # Установить права
        os.chmod(temp_path, mode)
        
        # Атомарно переименовать
        os.rename(temp_path, path)
    except:
        os.close(fd)
        os.unlink(temp_path)
        raise

# Использование
with atomic_write("/etc/myapp.conf") as fd:
    os.write(fd, b"key=value\n")

```

---

## 8. Практические примеры

### 8.1 Tail -f на Python

```python
#!/usr/bin/env python3
"""Реализация tail -f."""

import os
import sys
import time

def tail_follow(path, lines=10):
    """Следить за файлом как tail -f."""
    fd = os.open(path, os.O_RDONLY)
    
    try:
        # Сначала показать последние N строк
        file_size = os.lseek(fd, 0, os.SEEK_END)
        
        # Найти начало последних N строк
        block_size = 1024
        data = b""
        
        while data.count(b"\n") <= lines and file_size > 0:
            read_size = min(block_size, file_size)
            file_size -= read_size
            os.lseek(fd, file_size, os.SEEK_SET)
            data = os.read(fd, read_size) + data
        
        # Вывести последние строки
        output_lines = data.split(b"\n")[-lines-1:-1]
        for line in output_lines:
            print(line.decode())
        
        # Следить за новыми строками
        os.lseek(fd, 0, os.SEEK_END)
        
        while True:
            data = os.read(fd, 4096)
            if data:
                sys.stdout.write(data.decode())
                sys.stdout.flush()
            else:
                time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    finally:
        os.close(fd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tail_f.py <file>")
        sys.exit(1)
    
    tail_follow(sys.argv[1])

```

### 8.2 Безопасное обновление конфигурации

```python
#!/usr/bin/env python3
"""Атомарное обновление конфигурационного файла."""

import os
import tempfile
import json

def update_config(path, updates):
    """Обновить JSON конфигурацию атомарно."""
    
    # Читаем текущую конфигурацию
    try:
        with open(path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    
    # Обновляем
    config.update(updates)
    
    # Записываем атомарно
    dir_path = os.path.dirname(path) or "."
    fd, temp_path = tempfile.mkstemp(dir=dir_path, suffix=".tmp")
    
    try:
        # Записываем JSON
        data = json.dumps(config, indent=2).encode()
        os.write(fd, data)
        os.fsync(fd)
        os.close(fd)
        
        # Копируем права оригинала
        try:
            st = os.stat(path)
            os.chmod(temp_path, st.st_mode)
        except FileNotFoundError:
            os.chmod(temp_path, 0o644)
        
        # Атомарная замена
        os.rename(temp_path, path)
        
    except:
        os.unlink(temp_path)
        raise
    
    return config

# Использование
config = update_config("/etc/myapp/config.json", {
    "debug": True,
    "port": 8080
})
print(f"Updated config: {config}")

```

---

## 💡 Key Takeaways

- **Файловые дескрипторы** — целые числа, идентификаторы открытых файлов

- **0, 1, 2** — stdin, stdout, stderr соответственно

- **os.open/read/write** — низкоуровневые операции без буферизации

- **fcntl.flock** — блокировки для координации процессов

- **tempfile** — безопасное создание временных файлов

- **Атомарные операции** — rename для безопасного обновления

---

## 🚀 Next Steps

**Related Modules:**

- [File System](../03_FileSystem/) — метаданные и права
- [Processes](../04_Processes/) — fork и наследование дескрипторов

**Practice Ideas:**

1. Реализуйте `head -n` с низкоуровневым I/O
2. Напишите программу копирования с прогресс-баром
3. Создайте логгер с ротацией файлов
4. Реализуйте простой `tee`

**Going Deeper:**

- Изучите mmap для memory-mapped файлов
- Познакомьтесь с aio для асинхронного I/O
- Изучите splice/sendfile для zero-copy

---

## 📚 Additional Resources

**Documentation:**

- [man open(2)](https://man.openbsd.org/open.2)
- [man read(2)](https://man.openbsd.org/read.2)
- [man fcntl(2)](https://man.openbsd.org/fcntl.2)
- [Python os module](https://docs.python.org/3/library/os.html)

---





