# Python Files
## Работа с файлами и файловой системой

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать обработку исключений (try/except/finally)
- Знать работу с контекстными менеджерами (with)
- Уметь работать со строками и бинарными данными
- Понимать кодировки текста (UTF-8, ASCII)

**Recommended prior modules:**

- [Exceptions](../07_Exceptions/) — обработка ошибок и контекстные менеджеры

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Открывать, читать и записывать текстовые и бинарные файлы
- Использовать pathlib для работы с путями
- Работать с CSV, JSON и конфигурационными файлами
- Навигировать по файловой системе и управлять файлами
- Применять best practices для безопасной работы с файлами

---

## 1. Основы работы с файлами

### 1.1 Открытие и закрытие файлов

```python
# Базовый способ (НЕ рекомендуется)

f = open("example.txt", "w")
f.write("Hello, World!")
f.close()  # Легко забыть!

# Правильный способ — контекстный менеджер

with open("example.txt", "w") as f:
    f.write("Hello, World!")
# Файл автоматически закрыт

# Чтение файла

with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

**Output:**
```
Hello, World!
```

### 1.2 Режимы открытия файлов

| Режим | Описание |
|-------|----------|
| `r` | Чтение (по умолчанию). Файл должен существовать |
| `w` | Запись. Создаёт файл или перезаписывает существующий |
| `a` | Добавление в конец файла |
| `x` | Эксклюзивное создание. Ошибка если файл существует |
| `b` | Бинарный режим (добавляется к другим: `rb`, `wb`) |
| `t` | Текстовый режим (по умолчанию) |
| `+` | Чтение и запись (`r+`, `w+`, `a+`) |

```python
# Запись (перезаписывает)

with open("data.txt", "w") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")

# Добавление в конец

with open("data.txt", "a") as f:
    f.write("Третья строка\n")

# Чтение

with open("data.txt", "r") as f:
    print(f.read())

# Эксклюзивное создание

try:
    with open("data.txt", "x") as f:
        f.write("Новый файл")
except FileExistsError:
    print("Файл уже существует!")
```

**Output:**
```
Первая строка
Вторая строка
Третья строка

Файл уже существует!
```

### 1.3 Кодировки

```python
# Указание кодировки (рекомендуется всегда указывать)

with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир! 🌍")

with open("unicode.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Обработка ошибок кодировки

with open("file.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()  # Игнорирует некорректные символы

# errors="replace" — заменяет на ?
# errors="strict" — вызывает исключение (по умолчанию)
```

**Output:**
```
Привет, мир! 🌍
```

---

## 2. Чтение файлов

### 2.1 Различные способы чтения

```python
# Подготовим тестовый файл

with open("test.txt", "w") as f:
    f.write("Строка 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5\n")

# read() — весь файл в одну строку

with open("test.txt", "r") as f:
    content = f.read()
    print(f"read(): '{content}'")

# read(n) — n символов

with open("test.txt", "r") as f:
    chunk = f.read(10)
    print(f"read(10): '{chunk}'")

# readline() — одна строка

with open("test.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"readline(): '{line1}' '{line2}'")

# readlines() — список всех строк

with open("test.txt", "r") as f:
    lines = f.readlines()
    print(f"readlines(): {lines}")
```

**Output:**
```
read(): 'Строка 1
Строка 2
Строка 3
Строка 4
Строка 5
'
read(10): 'Строка 1
С'
readline(): 'Строка 1
' 'Строка 2
'
readlines(): ['Строка 1\n', 'Строка 2\n', 'Строка 3\n', 'Строка 4\n', 'Строка 5\n']
```

### 2.2 Итерация по строкам

```python
# Лучший способ для больших файлов — итерация

with open("test.txt", "r") as f:
    for line in f:  # Читает по одной строке, экономит память
        print(f"Строка: {line.strip()}")

# С enumerate для номеров строк

with open("test.txt", "r") as f:
    for num, line in enumerate(f, start=1):
        print(f"{num}: {line.strip()}")
```

**Output:**
```
Строка: Строка 1
Строка: Строка 2
Строка: Строка 3
Строка: Строка 4
Строка: Строка 5
1: Строка 1
2: Строка 2
3: Строка 3
4: Строка 4
5: Строка 5
```

### 2.3 Позиция в файле

```python
with open("test.txt", "r") as f:
    print(f"Позиция: {f.tell()}")  # 0
    
    f.read(10)
    print(f"После read(10): {f.tell()}")
    
    f.seek(0)  # Вернуться в начало
    print(f"После seek(0): {f.tell()}")
    
    f.seek(5)  # Перейти к позиции 5
    print(f"После seek(5): {f.read(5)}")
```

**Output:**
```
Позиция: 0
После read(10): 17
После seek(0): 0
После seek(5): ка 1
```

---

## 3. Запись в файлы

### 3.1 Методы записи

```python
# write() — записывает строку

with open("output.txt", "w") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")

# writelines() — записывает список строк

lines = ["Строка A\n", "Строка B\n", "Строка C\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# print() в файл

with open("output.txt", "w") as f:
    print("Hello", "World", sep=", ", end="!\n", file=f)
    print("Another line", file=f)

with open("output.txt", "r") as f:
    print(f.read())
```

**Output:**
```
Hello, World!
Another line
```

### 3.2 Буферизация

```python
# Немедленная запись (без буферизации)

with open("log.txt", "w", buffering=1) as f:  # Построчная буферизация
    f.write("Log entry 1\n")
    f.flush()  # Принудительно сбросить буфер
    f.write("Log entry 2\n")

# buffering=0 — без буферизации (только для бинарного режима)
# buffering=1 — построчная (для текстового режима)
# buffering=-1 — системная (по умолчанию)
```

---

## 4. Бинарные файлы

### 4.1 Чтение и запись бинарных данных

```python
# Запись бинарных данных

data = bytes([0x48, 0x65, 0x6c, 0x6c, 0x6f])  # "Hello" в байтах
with open("binary.bin", "wb") as f:
    f.write(data)

# Чтение бинарных данных

with open("binary.bin", "rb") as f:
    content = f.read()
    print(f"Байты: {content}")
    print(f"Как строка: {content.decode('utf-8')}")
    print(f"Hex: {content.hex()}")
```

**Output:**
```
Байты: b'Hello'
Как строка: Hello
Hex: 48656c6c6f
```

### 4.2 Работа с изображениями (пример)

```python
# Копирование бинарного файла

def copy_file(src, dst, chunk_size=8192):
    """Копирует файл по частям (экономит память)."""
    with open(src, "rb") as f_in, open(dst, "wb") as f_out:
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            f_out.write(chunk)

# copy_file("image.jpg", "image_copy.jpg")
```

### 4.3 struct — упаковка бинарных данных

```python
import struct

# Упаковка данных

packed = struct.pack("ihf", 42, 1000, 3.14)
print(f"Упакованные данные: {packed}")
print(f"Размер: {len(packed)} байт")

# Распаковка данных

i, h, f = struct.unpack("ihf", packed)
print(f"Распаковано: i={i}, h={h}, f={f}")

# Запись структурированных данных

with open("data.bin", "wb") as f:
    for i in range(5):
        f.write(struct.pack("if", i, i * 1.5))

# Чтение структурированных данных

with open("data.bin", "rb") as f:
    while True:
        data = f.read(struct.calcsize("if"))
        if not data:
            break
        i, f_val = struct.unpack("if", data)
        print(f"i={i}, f={f_val}")
```

**Output:**
```
Упакованные данные: b'*\x00\x00\x00\xe8\x03\xc3\xf5H@'
Размер: 10 байт
Распаковано: i=42, h=1000, f=3.140000104904175
i=0, f=0.0
i=1, f=1.5
i=2, f=3.0
i=3, f=4.5
i=4, f=6.0
```

---

## 5. pathlib — современная работа с путями

### 5.1 Создание путей

```python
from pathlib import Path

# Создание пути

p = Path("/home/user/documents")
print(f"Path: {p}")

# Текущая директория

cwd = Path.cwd()
print(f"CWD: {cwd}")

# Домашняя директория

home = Path.home()
print(f"Home: {home}")

# Сборка пути с помощью /

path = Path.home() / "documents" / "file.txt"
print(f"Собранный путь: {path}")

# Или joinpath()

path = Path.home().joinpath("documents", "file.txt")
print(f"joinpath(): {path}")
```

**Output:**
```
Path: /home/user/documents
CWD: /home/user/project
Home: /home/user
Собранный путь: /home/user/documents/file.txt
joinpath(): /home/user/documents/file.txt
```

### 5.2 Свойства пути

```python
from pathlib import Path

p = Path("/home/user/documents/report.txt")

print(f"name: {p.name}")           # report.txt
print(f"stem: {p.stem}")           # report
print(f"suffix: {p.suffix}")       # .txt
print(f"parent: {p.parent}")       # /home/user/documents
print(f"parents: {list(p.parents)}")  # Все родительские директории
print(f"parts: {p.parts}")         # ('/', 'home', 'user', 'documents', 'report.txt')
print(f"anchor: {p.anchor}")       # /
print(f"is_absolute: {p.is_absolute()}")  # True
```

**Output:**
```
name: report.txt
stem: report
suffix: .txt
parent: /home/user/documents
parents: [PosixPath('/home/user/documents'), PosixPath('/home/user'), PosixPath('/home'), PosixPath('/')]
parts: ('/', 'home', 'user', 'documents', 'report.txt')
anchor: /
is_absolute: True
```

### 5.3 Проверки и операции

```python
from pathlib import Path

p = Path("test.txt")

# Создадим файл для демонстрации

p.write_text("Hello, World!")

print(f"exists(): {p.exists()}")
print(f"is_file(): {p.is_file()}")
print(f"is_dir(): {p.is_dir()}")
print(f"stat(): {p.stat().st_size} bytes")

# Изменение расширения

new_path = p.with_suffix(".md")
print(f"with_suffix('.md'): {new_path}")

# Изменение имени

new_path = p.with_name("other.txt")
print(f"with_name('other.txt'): {new_path}")

# Удаление файла

p.unlink()
print(f"Файл удалён: {not p.exists()}")
```

**Output:**
```
exists(): True
is_file(): True
is_dir(): False
stat(): 13 bytes
with_suffix('.md'): test.md
with_name('other.txt'): other.txt
Файл удалён: True
```

### 5.4 Чтение и запись с pathlib

```python
from pathlib import Path

p = Path("example.txt")

# Запись текста

p.write_text("Привет, мир!", encoding="utf-8")

# Чтение текста

content = p.read_text(encoding="utf-8")
print(f"Содержимое: {content}")

# Запись байтов

p.write_bytes(b"Hello bytes")

# Чтение байтов

data = p.read_bytes()
print(f"Байты: {data}")

# Очистка

p.unlink()
```

**Output:**
```
Содержимое: Привет, мир!
Байты: b'Hello bytes'
```

### 5.5 Обход директорий

```python
from pathlib import Path

# Создадим тестовую структуру

base = Path("test_dir")
base.mkdir(exist_ok=True)
(base / "file1.txt").write_text("content1")
(base / "file2.py").write_text("content2")
(base / "subdir").mkdir(exist_ok=True)
(base / "subdir" / "file3.txt").write_text("content3")

# iterdir() — содержимое директории

print("iterdir():")
for item in base.iterdir():
    print(f"  {item.name} ({'dir' if item.is_dir() else 'file'})")

# glob() — поиск по паттерну

print("\nglob('*.txt'):")
for txt_file in base.glob("*.txt"):
    print(f"  {txt_file}")

# rglob() — рекурсивный glob

print("\nrglob('*.txt'):")
for txt_file in base.rglob("*.txt"):
    print(f"  {txt_file}")

# Очистка

import shutil
shutil.rmtree(base)
```

**Output:**
```
iterdir():
  file1.txt (file)
  file2.py (file)
  subdir (dir)

glob('*.txt'):
  test_dir/file1.txt

rglob('*.txt'):
  test_dir/file1.txt
  test_dir/subdir/file3.txt
```

---

## 6. Работа с форматами данных

### 6.1 JSON

```python
import json

# Данные

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL", "Docker"],
    "active": True
}

# Запись в файл

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Чтение из файла

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"Загружено: {loaded}")

# В строку и обратно

json_str = json.dumps(data, indent=2)
print(f"JSON строка:\n{json_str}")

parsed = json.loads(json_str)
print(f"\nРаспарсено: {parsed['name']}")
```

**Output:**
```
Загружено: {'name': 'Alice', 'age': 30, 'skills': ['Python', 'SQL', 'Docker'], 'active': True}
JSON строка:
{
  "name": "Alice",
  "age": 30,
  "skills": [
    "Python",
    "SQL",
    "Docker"
  ],
  "active": true
}

Распарсено: Alice
```

### 6.2 CSV

```python
import csv

# Запись CSV

data = [
    ["name", "age", "city"],
    ["Alice", 30, "Moscow"],
    ["Bob", 25, "London"],
    ["Charlie", 35, "Paris"]
]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Чтение CSV

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print()

# DictReader/DictWriter — удобнее для работы со словарями

data_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

with open("data_dict.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data_dicts)

with open("data_dict.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old")
```

**Output:**
```
['name', 'age', 'city']
['Alice', '30', 'Moscow']
['Bob', '25', 'London']
['Charlie', '35', 'Paris']

Alice is 30 years old
Bob is 25 years old
```

### 6.3 INI/Config файлы

```python
import configparser

# Создание конфигурации

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "debug": "false",
    "log_level": "INFO"
}

config["database"] = {
    "host": "localhost",
    "port": "5432",
    "name": "myapp"
}

config["server"] = {
    "host": "0.0.0.0",
    "port": "8080"
}

# Запись

with open("config.ini", "w") as f:
    config.write(f)

# Чтение

config = configparser.ConfigParser()
config.read("config.ini")

print(f"Секции: {config.sections()}")
print(f"Database host: {config['database']['host']}")
print(f"Debug (default): {config['server'].getboolean('debug')}")
print(f"Port (int): {config['server'].getint('port')}")
```

**Output:**
```
Секции: ['database', 'server']
Database host: localhost
Debug (default): False
Port (int): 8080
```

### 6.4 YAML (с библиотекой PyYAML)

```python
# pip install pyyaml

import yaml

data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "features": ["auth", "logging", "caching"]
}

# Запись

with open("config.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

# Чтение

with open("config.yaml", "r") as f:
    loaded = yaml.safe_load(f)
    print(f"Host: {loaded['database']['host']}")
    print(f"Features: {loaded['features']}")
```

**Output:**
```
Host: localhost
Features: ['auth', 'logging', 'caching']
```

---

## 7. Операции с файловой системой

### 7.1 Модуль os

```python
import os

# Информация о системе

print(f"Текущая директория: {os.getcwd()}")
print(f"Разделитель пути: {os.sep}")
print(f"Перенос строки: {repr(os.linesep)}")

# Переменные окружения

print(f"HOME: {os.environ.get('HOME')}")
print(f"PATH: {os.environ.get('PATH', '')[:50]}...")

# Создание директорий

os.makedirs("a/b/c", exist_ok=True)  # Создаёт все промежуточные

# Список файлов

print(f"Содержимое: {os.listdir('.')[:5]}")

# Удаление директорий

os.removedirs("a/b/c")  # Удаляет пустые директории
```

### 7.2 shutil — высокоуровневые операции

```python
import shutil
from pathlib import Path

# Подготовка

Path("source_dir").mkdir(exist_ok=True)
Path("source_dir/file.txt").write_text("content")

# Копирование файла

shutil.copy("source_dir/file.txt", "copy.txt")
shutil.copy2("source_dir/file.txt", "copy2.txt")  # Сохраняет метаданные

# Копирование директории

shutil.copytree("source_dir", "dest_dir")

# Перемещение

shutil.move("copy.txt", "moved.txt")

# Удаление директории с содержимым

shutil.rmtree("source_dir")
shutil.rmtree("dest_dir")

# Информация о диске

total, used, free = shutil.disk_usage("/")
print(f"Диск: {total // (1024**3)} GB всего, {free // (1024**3)} GB свободно")

# Очистка

Path("copy2.txt").unlink()
Path("moved.txt").unlink()
```

**Output:**
```
Диск: 500 GB всего, 123 GB свободно
```

### 7.3 Временные файлы

```python
import tempfile
from pathlib import Path

# Временный файл

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("Временные данные")
    temp_path = f.name
    print(f"Временный файл: {temp_path}")

# Файл существует после закрытия (delete=False)

print(f"Существует: {Path(temp_path).exists()}")
Path(temp_path).unlink()  # Удаляем вручную

# Временная директория

with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Временная директория: {tmpdir}")
    temp_file = Path(tmpdir) / "data.txt"
    temp_file.write_text("test")
    print(f"Файл создан: {temp_file.exists()}")
# Директория автоматически удалена

# Получение директории для временных файлов

print(f"Temp директория системы: {tempfile.gettempdir()}")
```

**Output:**
```
Временный файл: /tmp/tmp12345678.txt
Существует: True
Временная директория: /tmp/tmpabc12345
Файл создан: True
Temp директория системы: /tmp
```

---

## 8. Практические примеры

### 8.1 Логирование в файл

```python
from pathlib import Path
from datetime import datetime

class FileLogger:
    def __init__(self, filename):
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
    
    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{level}] {message}\n"
        
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(log_line)
    
    def info(self, message):
        self.log("INFO", message)
    
    def error(self, message):
        self.log("ERROR", message)

# Использование

logger = FileLogger("logs/app.log")
logger.info("Приложение запущено")
logger.error("Произошла ошибка")

# Проверка

print(Path("logs/app.log").read_text())
```

**Output:**
```
[2024-12-02 15:30:00] [INFO] Приложение запущено
[2024-12-02 15:30:00] [ERROR] Произошла ошибка
```

### 8.2 Поиск файлов

```python
from pathlib import Path

def find_files(directory, pattern, recursive=True):
    """Находит файлы по паттерну."""
    path = Path(directory)
    
    if recursive:
        return list(path.rglob(pattern))
    else:
        return list(path.glob(pattern))

def find_large_files(directory, min_size_mb=100):
    """Находит файлы больше указанного размера."""
    path = Path(directory)
    min_size = min_size_mb * 1024 * 1024
    
    large_files = []
    for file in path.rglob("*"):
        if file.is_file() and file.stat().st_size > min_size:
            large_files.append((file, file.stat().st_size))
    
    return sorted(large_files, key=lambda x: x[1], reverse=True)

# Примеры
# python_files = find_files(".", "*.py")
# large = find_large_files("/home/user", min_size_mb=100)
```

### 8.3 Обработка логов

```python
from pathlib import Path
from collections import Counter
import re

def analyze_log(log_path):
    """Анализирует лог-файл."""
    path = Path(log_path)
    
    if not path.exists():
        return None
    
    stats = {
        "total_lines": 0,
        "errors": 0,
        "warnings": 0,
        "error_messages": []
    }
    
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            stats["total_lines"] += 1
            
            if "ERROR" in line:
                stats["errors"] += 1
                # Извлекаем сообщение об ошибке
                match = re.search(r"\[ERROR\] (.+)", line)
                if match:
                    stats["error_messages"].append(match.group(1))
            elif "WARNING" in line:
                stats["warnings"] += 1
    
    # Подсчёт частых ошибок
    stats["error_counts"] = Counter(stats["error_messages"]).most_common(5)
    
    return stats

# stats = analyze_log("app.log")
```

---

## 9. Common Pitfalls

### 9.1 Забытый encoding

❌ **Плохо:**
```python
with open("file.txt", "w") as f:
    f.write("Привет")  # Может сломаться на Windows
```

✅ **Хорошо:**
```python
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Привет")
```

### 9.2 Использование строк вместо pathlib

❌ **Плохо:**
```python
path = "/home/user" + "/" + "documents" + "/" + "file.txt"
```

✅ **Хорошо:**
```python
from pathlib import Path
path = Path.home() / "documents" / "file.txt"
```

### 9.3 Чтение большого файла целиком

❌ **Плохо:**
```python
with open("huge.log", "r") as f:
    content = f.read()  # Может не хватить памяти!
    for line in content.split("\n"):
        process(line)
```

✅ **Хорошо:**
```python
with open("huge.log", "r") as f:
    for line in f:  # Читает по одной строке
        process(line)
```

### 9.4 Забытый newline в CSV

❌ **Плохо:**
```python
with open("data.csv", "w") as f:  # Пустые строки на Windows
    writer = csv.writer(f)
    writer.writerow(["a", "b"])
```

✅ **Хорошо:**
```python
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b"])
```

---

## 10. Best Practices

### 10.1 Всегда используйте with

```python
# with гарантирует закрытие файла даже при исключениях

with open("file.txt", "w") as f:
    f.write("data")
# Файл закрыт автоматически
```

### 10.2 Проверяйте существование файла

```python
from pathlib import Path

def safe_read(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    if not p.is_file():
        raise IsADirectoryError(f"Это директория: {path}")
    return p.read_text(encoding="utf-8")
```

### 10.3 Атомарная запись

```python
from pathlib import Path
import tempfile
import os

def atomic_write(path, content):
    """Атомарная запись — либо полностью записано, либо ничего."""
    path = Path(path)
    
    # Записываем во временный файл
    fd, temp_path = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        # Атомарное переименование
        os.replace(temp_path, path)
    except:
        os.unlink(temp_path)
        raise
```

---

## 💡 Key Takeaways

- **Всегда используйте `with`**: Контекстный менеджер гарантирует закрытие файла даже при ошибках.

- **pathlib > os.path**: Используйте `pathlib.Path` для современной и удобной работы с путями.

- **Указывайте encoding**: Всегда указывайте `encoding="utf-8"` для текстовых файлов.

- **Итерируйте по большим файлам**: Не читайте весь файл в память — используйте итерацию по строкам.

- **Используйте специализированные модули**: `json`, `csv`, `configparser` для соответствующих форматов.

---

## 🚀 Next Steps

**Related Modules:**

- [Standard Modules](../09_StandardModules/) — os, shutil, tempfile подробнее
- [Additional Modules](../10_AdditionalModules/) — pandas для работы с данными

**Practice Ideas:**

1. Напишите утилиту для поиска дубликатов файлов по хэшу
2. Создайте скрипт резервного копирования с ротацией
3. Реализуйте парсер логов с группировкой ошибок
4. Создайте конвертер CSV в JSON

**Going Deeper:**

- Изучите модуль `io` для работы с потоками
- Познакомьтесь с `mmap` для memory-mapped файлов
- Изучите асинхронную работу с файлами (`aiofiles`)

---

## 📚 Additional Resources

**Documentation:**

- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [shutil](https://docs.python.org/3/library/shutil.html)

**Formats:**

- [json](https://docs.python.org/3/library/json.html)
- [csv](https://docs.python.org/3/library/csv.html)
- [configparser](https://docs.python.org/3/library/configparser.html)

---





