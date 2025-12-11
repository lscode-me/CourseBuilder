# File System
## Файловая система, метаданные и права доступа

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [Files & I/O](../02_FilesAndIO/)
- Понимать структуру файловой системы Unix
- Знать базовые права доступа

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Получать и интерпретировать метаданные файлов (stat)
- Управлять правами доступа программно
- Работать с символическими и жёсткими ссылками
- Использовать os.walk для обхода директорий
- Мониторить изменения файловой системы (kqueue/inotify)
- Создавать и управлять директориями

---

## 1. Метаданные файлов (stat)

### 1.1 os.stat — получение метаданных

```python

import os
import stat
from datetime import datetime

path = "/etc/passwd"
st = os.stat(path)

print(f"File: {path}")
print(f"Size: {st.st_size} bytes")
print(f"Mode: {oct(st.st_mode)}")
print(f"UID: {st.st_uid}")
print(f"GID: {st.st_gid}")
print(f"Access time: {datetime.fromtimestamp(st.st_atime)}")
print(f"Modify time: {datetime.fromtimestamp(st.st_mtime)}")
print(f"Change time: {datetime.fromtimestamp(st.st_ctime)}")
print(f"Inode: {st.st_ino}")
print(f"Device: {st.st_dev}")
print(f"Hard links: {st.st_nlink}")

```

**Output:**
```

File: /etc/passwd
Size: 1843 bytes
Mode: 0o100644
UID: 0
GID: 0
Access time: 2024-12-01 10:30:00
Modify time: 2024-11-15 14:30:00
Change time: 2024-11-15 14:30:00
Inode: 98304
Device: 0
Hard links: 1

```

### 1.2 Структура st_mode

```python

import stat as stat_module

mode = os.stat("/etc/passwd").st_mode

# Тип файла
print(f"Is regular file: {stat_module.S_ISREG(mode)}")
print(f"Is directory: {stat_module.S_ISDIR(mode)}")
print(f"Is symlink: {stat_module.S_ISLNK(mode)}")
print(f"Is block device: {stat_module.S_ISBLK(mode)}")
print(f"Is char device: {stat_module.S_ISCHR(mode)}")
print(f"Is FIFO: {stat_module.S_ISFIFO(mode)}")
print(f"Is socket: {stat_module.S_ISSOCK(mode)}")

# Права доступа
print(f"User read: {bool(mode & stat_module.S_IRUSR)}")
print(f"User write: {bool(mode & stat_module.S_IWUSR)}")
print(f"User exec: {bool(mode & stat_module.S_IXUSR)}")

# Специальные биты
print(f"Setuid: {bool(mode & stat_module.S_ISUID)}")
print(f"Setgid: {bool(mode & stat_module.S_ISGID)}")
print(f"Sticky: {bool(mode & stat_module.S_ISVTX)}")

```

### 1.3 os.lstat vs os.stat

```python

import os

# Создадим символическую ссылку для примера
# os.symlink("/etc/passwd", "/tmp/passwd_link")

# os.stat следует за ссылками
st = os.stat("/tmp/passwd_link")
print(f"stat size: {st.st_size}")  # Размер /etc/passwd

# os.lstat НЕ следует за ссылками
st = os.lstat("/tmp/passwd_link")
print(f"lstat size: {st.st_size}")  # Размер самой ссылки

```

### 1.4 fstat — stat по дескриптору

```python

import os

fd = os.open("/etc/passwd", os.O_RDONLY)
st = os.fstat(fd)
print(f"Size via fstat: {st.st_size}")
os.close(fd)

```

---

## 2. Права доступа

### 2.1 os.chmod — изменение прав

```python

import os
import stat

path = "/tmp/test.txt"

# Создать файл
with open(path, "w") as f:
    f.write("test")

# Установить права 644 (rw-r--r--)
os.chmod(path, 0o644)

# Добавить execute для владельца
current = os.stat(path).st_mode
os.chmod(path, current | stat.S_IXUSR)

# Убрать запись для группы и остальных
os.chmod(path, 0o744)

# Символьный способ (через stat константы)
os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

```

### 2.2 os.chown — изменение владельца

```python

import os
import pwd
import grp

path = "/tmp/test.txt"

# Получить UID и GID по имени
uid = pwd.getpwnam("admin").pw_uid
gid = grp.getgrnam("staff").gr_gid

# Изменить владельца (требует root)
# os.chown(path, uid, gid)

# Изменить только группу (-1 = не менять)
# os.chown(path, -1, gid)

# lchown — для символических ссылок
# os.lchown(path, uid, gid)
```

### 2.3 os.access — проверка доступа

```python

import os

path = "/etc/passwd"

# Проверить права текущего пользователя
print(f"Exists: {os.access(path, os.F_OK)}")
print(f"Readable: {os.access(path, os.R_OK)}")
print(f"Writable: {os.access(path, os.W_OK)}")
print(f"Executable: {os.access(path, os.X_OK)}")

# Комбинированная проверка
print(f"Read+Write: {os.access(path, os.R_OK | os.W_OK)}")

```

### 2.4 umask — маска прав по умолчанию

```python

import os

# Получить текущую umask (и установить новую)
old_umask = os.umask(0o022)
print(f"Old umask: {oct(old_umask)}")

# Восстановить
os.umask(old_umask)

# Создание файла с учётом umask
# umask 022: файл с mode 0666 → 0644
# umask 077: файл с mode 0666 → 0600
```

### 2.5 Утилита для отображения прав

```python

import os
import stat

def format_mode(mode):
    """Форматировать права как ls -l."""
    chars = [
        'd' if stat.S_ISDIR(mode) else
        'l' if stat.S_ISLNK(mode) else
        'c' if stat.S_ISCHR(mode) else
        'b' if stat.S_ISBLK(mode) else
        'p' if stat.S_ISFIFO(mode) else
        's' if stat.S_ISSOCK(mode) else '-',
        
        'r' if mode & stat.S_IRUSR else '-',
        'w' if mode & stat.S_IWUSR else '-',
        'x' if mode & stat.S_IXUSR else '-',
        'r' if mode & stat.S_IRGRP else '-',
        'w' if mode & stat.S_IWGRP else '-',
        'x' if mode & stat.S_IXGRP else '-',
        'r' if mode & stat.S_IROTH else '-',
        'w' if mode & stat.S_IWOTH else '-',
        'x' if mode & stat.S_IXOTH else '-',
    ]
    
    # Специальные биты
    if mode & stat.S_ISUID:
        chars[3] = 's' if mode & stat.S_IXUSR else 'S'
    if mode & stat.S_ISGID:
        chars[6] = 's' if mode & stat.S_IXGRP else 'S'
    if mode & stat.S_ISVTX:
        chars[9] = 't' if mode & stat.S_IXOTH else 'T'
    
    return ''.join(chars)

# Пример
mode = os.stat("/etc/passwd").st_mode
print(format_mode(mode))  # -rw-r--r--

```

---

## 3. Ссылки

### 3.1 Жёсткие ссылки

```python

import os

# Создать жёсткую ссылку
os.link("/etc/passwd", "/tmp/passwd_hard")

# Оба имени указывают на один inode
st1 = os.stat("/etc/passwd")
st2 = os.stat("/tmp/passwd_hard")

print(f"Same inode: {st1.st_ino == st2.st_ino}")
print(f"Link count: {st1.st_nlink}")

# Удаление
os.unlink("/tmp/passwd_hard")

```

### 3.2 Символические ссылки

```python

import os

# Создать символическую ссылку
os.symlink("/etc/passwd", "/tmp/passwd_sym")

# Прочитать цель ссылки
target = os.readlink("/tmp/passwd_sym")
print(f"Link target: {target}")

# Проверить, является ли путь ссылкой
print(f"Is symlink: {os.path.islink('/tmp/passwd_sym')}")

# Удаление (unlink удаляет ссылку, не цель)
os.unlink("/tmp/passwd_sym")

```

### 3.3 Разрешение пути

```python

import os

# Получить абсолютный путь
abs_path = os.path.abspath("./file.txt")
print(f"Absolute: {abs_path}")

# Разрешить символические ссылки
real_path = os.path.realpath("/tmp/passwd_sym")
print(f"Real path: {real_path}")

# Нормализовать путь
norm = os.path.normpath("/home/user/../user/./file.txt")
print(f"Normalized: {norm}")

```

---

## 4. Директории

### 4.1 Создание и удаление

```python

import os

# Создать директорию
os.mkdir("/tmp/mydir")

# Создать с определёнными правами
os.mkdir("/tmp/mydir2", 0o755)

# Создать вложенные директории
os.makedirs("/tmp/a/b/c", exist_ok=True)

# Удалить пустую директорию
os.rmdir("/tmp/mydir")

# Удалить вложенные пустые директории
os.removedirs("/tmp/a/b/c")

```

### 4.2 os.listdir и os.scandir

```python

import os

# Простой список
entries = os.listdir("/etc")
for entry in entries[:5]:
    print(entry)

# scandir — эффективнее, возвращает DirEntry объекты
with os.scandir("/etc") as it:
    for entry in it:
        if entry.is_file():
            print(f"File: {entry.name}, size: {entry.stat().st_size}")
        elif entry.is_dir():
            print(f"Dir: {entry.name}")

```

### 4.3 os.walk — рекурсивный обход

```python

import os

def find_files(directory, extension):
    """Найти все файлы с определённым расширением."""
    matches = []
    
    for root, dirs, files in os.walk(directory):
        # Пропустить скрытые директории
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            if filename.endswith(extension):
                matches.append(os.path.join(root, filename))
    
    return matches

# Найти все .conf файлы в /etc
conf_files = find_files("/etc", ".conf")
for f in conf_files[:10]:
    print(f)

```

### 4.4 Подсчёт размера директории

```python

import os

def get_dir_size(path):
    """Подсчитать размер директории."""
    total = 0
    
    with os.scandir(path) as it:
        for entry in it:
            try:
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += get_dir_size(entry.path)
            except PermissionError:
                pass
    
    return total

def format_size(size):
    """Форматировать размер в человекочитаемый вид."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"

size = get_dir_size("/var/log")
print(f"/var/log size: {format_size(size)}")

```

---

## 5. Модификация файловой системы

### 5.1 Переименование и перемещение

```python

import os

# Переименовать файл
os.rename("/tmp/old.txt", "/tmp/new.txt")

# Атомарная замена (если new.txt существует — заменить)
os.replace("/tmp/temp.txt", "/tmp/config.txt")

# Примечание: rename может не работать между файловыми системами
# Используйте shutil.move для cross-filesystem перемещения
```

### 5.2 os.truncate — изменение размера

```python

import os

# Создать файл
with open("/tmp/test.txt", "w") as f:
    f.write("Hello, World!")

# Обрезать до 5 байт
os.truncate("/tmp/test.txt", 5)

# Проверить
with open("/tmp/test.txt", "r") as f:
    print(f.read())  # "Hello"

# Расширить (заполнится нулями)
os.truncate("/tmp/test.txt", 100)

```

### 5.3 Изменение времени

```python

import os
import time

path = "/tmp/test.txt"

# Установить atime и mtime
now = time.time()
os.utime(path, (now, now))

# Установить конкретное время
atime = 1609459200  # 2021-01-01 00:00:00
mtime = 1609459200
os.utime(path, (atime, mtime))

# None — использовать текущее время
os.utime(path, None)

```

---

## 6. pathlib — современный API

### 6.1 Основы pathlib

```python

from pathlib import Path

# Создание пути
p = Path("/etc/passwd")
print(f"Name: {p.name}")
print(f"Suffix: {p.suffix}")
print(f"Stem: {p.stem}")
print(f"Parent: {p.parent}")
print(f"Parts: {p.parts}")

# Проверки
print(f"Exists: {p.exists()}")
print(f"Is file: {p.is_file()}")
print(f"Is dir: {p.is_dir()}")
print(f"Is symlink: {p.is_symlink()}")

```

### 6.2 Операции с путями

```python

from pathlib import Path

# Конкатенация путей
base = Path("/home/user")
full = base / "documents" / "file.txt"
print(full)

# Чтение и запись
p = Path("/tmp/test.txt")
p.write_text("Hello, pathlib!")
content = p.read_text()
print(content)

# Бинарные данные
p.write_bytes(b"Binary data")
data = p.read_bytes()

```

### 6.3 Поиск файлов

```python

from pathlib import Path

# Найти все .py файлы в текущей директории
for py_file in Path(".").glob("*.py"):
    print(py_file)

# Рекурсивный поиск
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Итерация по директории
for item in Path("/etc").iterdir():
    if item.is_file():
        print(f"File: {item}")

```

### 6.4 Создание и удаление

```python

from pathlib import Path

# Создать директории
Path("/tmp/a/b/c").mkdir(parents=True, exist_ok=True)

# Создать файл
Path("/tmp/new_file.txt").touch()

# Удалить файл
Path("/tmp/new_file.txt").unlink()

# Удалить пустую директорию
Path("/tmp/a/b/c").rmdir()

```

---

## 7. Мониторинг файловой системы

### 7.1 kqueue на BSD (select.kqueue)

```python

import os
import select

def watch_file_kqueue(path):
    """Следить за изменениями файла на BSD."""
    kq = select.kqueue()
    
    fd = os.open(path, os.O_RDONLY)
    
    # Создать событие для отслеживания изменений
    event = select.kevent(
        fd,
        filter=select.KQ_FILTER_VNODE,
        flags=select.KQ_EV_ADD | select.KQ_EV_ENABLE | select.KQ_EV_CLEAR,
        fflags=select.KQ_NOTE_WRITE | select.KQ_NOTE_DELETE | select.KQ_NOTE_RENAME
    )
    
    try:
        print(f"Watching {path}...")
        while True:
            events = kq.control([event], 1, None)  # Блокирующее ожидание
            
            for e in events:
                if e.fflags & select.KQ_NOTE_WRITE:
                    print("File modified")
                if e.fflags & select.KQ_NOTE_DELETE:
                    print("File deleted")
                    return
                if e.fflags & select.KQ_NOTE_RENAME:
                    print("File renamed")
                    return
    finally:
        os.close(fd)
        kq.close()

# Использование (только BSD)
# watch_file_kqueue("/tmp/test.txt")
```

### 7.2 Кроссплатформенный мониторинг с watchdog

```python
# pip install watchdog

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")
    
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
    
    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")
    
    def on_moved(self, event):
        print(f"Moved: {event.src_path} → {event.dest_path}")

def watch_directory(path):
    """Следить за директорией."""
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

# watch_directory("/tmp")
```

---

## 8. Практические примеры

### 8.1 Синхронизация директорий

```python
#!/usr/bin/env python3
"""Простая синхронизация директорий."""

import os
import shutil
from pathlib import Path

def sync_directories(src, dst):
    """Синхронизировать src → dst."""
    src = Path(src)
    dst = Path(dst)
    
    if not dst.exists():
        dst.mkdir(parents=True)
    
    # Копировать новые и изменённые файлы
    for src_file in src.rglob("*"):
        if src_file.is_file():
            rel_path = src_file.relative_to(src)
            dst_file = dst / rel_path
            
            # Создать директории
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Копировать если изменился
            if not dst_file.exists() or \
               src_file.stat().st_mtime > dst_file.stat().st_mtime:
                print(f"Copying: {rel_path}")
                shutil.copy2(src_file, dst_file)
    
    # Удалить файлы, которых нет в src
    for dst_file in dst.rglob("*"):
        if dst_file.is_file():
            rel_path = dst_file.relative_to(dst)
            src_file = src / rel_path
            
            if not src_file.exists():
                print(f"Removing: {rel_path}")
                dst_file.unlink()

# sync_directories("/home/user/documents", "/backup/documents")
```

### 8.2 Поиск дубликатов файлов

```python
#!/usr/bin/env python3
"""Поиск дубликатов по размеру и хэшу."""

import os
import hashlib
from collections import defaultdict
from pathlib import Path

def file_hash(path, chunk_size=8192):
    """Вычислить SHA-256 хэш файла."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(directory):
    """Найти дубликаты файлов."""
    # Группировать по размеру
    by_size = defaultdict(list)
    
    for file_path in Path(directory).rglob("*"):
        if file_path.is_file():
            size = file_path.stat().st_size
            by_size[size].append(file_path)
    
    # Для файлов одинакового размера — проверить хэш
    duplicates = []
    
    for size, files in by_size.items():
        if len(files) < 2:
            continue
        
        by_hash = defaultdict(list)
        for f in files:
            h = file_hash(f)
            by_hash[h].append(f)
        
        for hash_val, hash_files in by_hash.items():
            if len(hash_files) > 1:
                duplicates.append(hash_files)
    
    return duplicates

# Найти дубликаты
dups = find_duplicates("/home/user/photos")
for group in dups:
    print("Duplicates:")
    for f in group:
        print(f"  {f}")

```

---

## 💡 Key Takeaways

- **os.stat** — основной способ получения метаданных

- **os.lstat** — не следует за символическими ссылками

- **pathlib** — современный ООП интерфейс для работы с путями

- **os.walk** — рекурсивный обход директорий

- **kqueue/inotify** — системный мониторинг изменений

- **Атомарность** — используйте rename для безопасных обновлений

---

## 🚀 Next Steps

**Related Modules:**

- [Processes](../04_Processes/) — fork и работа с процессами
- [Security](../11_Security/) — права и безопасность

**Practice Ideas:**

1. Напишите `du -sh` на Python
2. Создайте утилиту для поиска больших файлов
3. Реализуйте `find` с фильтрами
4. Напишите синхронизатор с rsync-подобным поведением

**Going Deeper:**

- Extended attributes (xattr)
- ACL (Access Control Lists)
- inotify на Linux для эффективного мониторинга

---

## 📚 Additional Resources

**Documentation:**

- [man stat(2)](https://man.openbsd.org/stat.2)
- [man chmod(2)](https://man.openbsd.org/chmod.2)
- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python os module](https://docs.python.org/3/library/os.html)

---




