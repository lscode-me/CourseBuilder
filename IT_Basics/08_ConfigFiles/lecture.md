# Конфигурационные файлы
## INI, TOML, .env и другие форматы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать JSON и YAML (модули 05, 06)
- Понимать переменные окружения
- Иметь опыт работы с приложениями и их настройками

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Работать с INI файлами и понимать их ограничения
- Использовать TOML для современных конфигураций
- Управлять переменными окружения через .env файлы
- Выбирать подходящий формат конфигурации

---

## 1. Обзор форматов конфигурации

### 1.1 Эволюция форматов

```
1980s     1990s      2000s      2010s      2020s
INI  →  XML  →  JSON  →  YAML  →  TOML
                              ↓
                           .env (параллельно)
```

### 1.2 Сравнение форматов

| Формат | Комментарии | Вложенность | Типы данных | Применение |
|--------|-------------|-------------|-------------|------------|
| INI | `;` или `#` | Секции | Строки | Windows, Git |
| TOML | `#` | Таблицы | Да | Rust, Python |
| .env | `#` | Нет | Строки | Docker, Node.js |
| JSON | Нет | Полная | Да | API, Web |
| YAML | `#` | Полная | Да | DevOps |

---

## 2. INI файлы

### 2.1 Формат INI

```ini
; Это комментарий
# Это тоже комментарий

[section]
key = value
another_key = another value

[database]
host = localhost
port = 5432
username = admin
; password хранится в переменных окружения

[server]
debug = true
max_connections = 100
```

### 2.2 Правила INI

- **Секции** в квадратных скобках `[section]`
- **Пары ключ-значение**: `key = value`
- **Комментарии**: `;` или `#`
- **Значения** — всегда строки
- **Нет вложенности** (только секции)

### 2.3 INI в Python

```python
import configparser

# Чтение
config = configparser.ConfigParser()
config.read('config.ini')

# Доступ к значениям
host = config['database']['host']
port = config.getint('database', 'port')
debug = config.getboolean('server', 'debug')

print(f"Database: {host}:{port}")

# Запись
config['new_section'] = {
    'key1': 'value1',
    'key2': 'value2'
}

with open('config.ini', 'w') as f:
    config.write(f)
```

### 2.4 Примеры INI

```ini
; .gitconfig
[user]
    name = John Doe
    email = john@example.com

[core]
    editor = vim
    autocrlf = input

[alias]
    st = status
    co = checkout
    br = branch
```

```ini
; php.ini
[PHP]
engine = On
memory_limit = 128M
max_execution_time = 30

[Date]
date.timezone = Europe/Moscow
```

---

## 3. TOML

### 3.1 Что такое TOML

**TOML** (Tom's Obvious Minimal Language) — современный формат конфигураций.

- Создан Томом Престон-Вернером (GitHub)
- Очевидный синтаксис
- Поддержка типов данных
- Стандарт для Rust (Cargo.toml), Python (pyproject.toml)

### 3.2 Синтаксис TOML

```toml
# Это комментарий

# Базовые типы
title = "TOML Example"
enabled = true
count = 42
price = 19.99
date = 2024-01-15
datetime = 2024-01-15T10:30:00Z

# Строки
simple = "Hello"
multiline = """
First line
Second line"""
literal = 'C:\path\to\file'

# Массивы
numbers = [1, 2, 3]
mixed = ["string", 42, true]
nested = [[1, 2], [3, 4]]

# Таблицы (объекты)
[server]
host = "localhost"
port = 8080

[database]
host = "db.example.com"
port = 5432
username = "admin"

# Вложенные таблицы
[database.pool]
min = 5
max = 20

# Массив таблиц
[[users]]
name = "Alice"
role = "admin"

[[users]]
name = "Bob"
role = "user"
```

### 3.3 TOML в Python

```python
# Встроенный модуль (Python 3.11+)
import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

print(config['server']['host'])
print(config['users'][0]['name'])

# Для записи используйте toml или tomli-w
import tomli_w

with open('output.toml', 'wb') as f:
    tomli_w.dump(config, f)
```

### 3.4 pyproject.toml

```toml
[project]
name = "myproject"
version = "1.0.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Author", email = "author@example.com"}
]
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
]

[project.scripts]
myapp = "myproject:main"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### 3.5 Cargo.toml (Rust)

```toml
[package]
name = "myapp"
version = "0.1.0"
edition = "2021"
authors = ["Author <author@example.com>"]

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[[bin]]
name = "myapp"
path = "src/main.rs"
```

---

## 4. .env файлы

### 4.1 Формат .env

```bash
# .env файл
# Комментарии начинаются с #

DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=your-secret-key-here
DEBUG=true

# Кавычки опциональны
API_KEY="key-with-spaces and special=chars"

# Многострочные значения
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
-----END RSA PRIVATE KEY-----"
```

### 4.2 Правила .env

- **Формат**: `KEY=value`
- **Комментарии**: `#`
- **Кавычки**: опциональны (нужны для пробелов)
- **Нет секций** — плоская структура
- **НЕ коммитить в Git** — добавить в .gitignore

### 4.3 .env в Python

```python
# С библиотекой python-dotenv
from dotenv import load_dotenv
import os

# Загрузка .env файла
load_dotenv()  # Ищет .env в текущей директории
# или
load_dotenv('/path/to/.env')

# Использование
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG', 'false').lower() == 'true'
port = int(os.getenv('PORT', '8080'))

print(f"Connecting to {database_url}")
```

### 4.4 .env и Docker

```yaml
# docker-compose.yml
services:
  app:
    image: myapp
    env_file:
      - .env
    environment:
      - EXTRA_VAR=value  # Дополнительные переменные
```

```dockerfile
# Dockerfile
# НЕ копируйте .env в образ!
ENV NODE_ENV=production
```

### 4.5 Пример структуры

```
project/
├── .env              # Локальные секреты (в .gitignore)
├── .env.example      # Шаблон (в Git)
├── .env.production   # Production настройки
└── .env.test         # Тестовые настройки
```

```bash
# .env.example
DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=change-me-in-production
DEBUG=true
```

---

## 5. Properties файлы (Java)

### 5.1 Формат

```properties
# application.properties
app.name=MyApp
app.version=1.0.0

# База данных
database.host=localhost
database.port=5432
database.username=admin

# Экранирование
path.windows=C:\\Program Files\\App
unicode=\u0041\u0042\u0043

# Многострочные
long.text=This is a very long \
    line that continues here
```

### 5.2 Properties в Python

```python
import jproperties

p = jproperties.Properties()

with open('app.properties', 'rb') as f:
    p.load(f)

# Доступ к значениям
name = p['app.name'].data
port = int(p['database.port'].data)
```

---

## 6. Сравнение и выбор формата

### 6.1 Таблица выбора

| Сценарий | Рекомендуемый формат |
|----------|---------------------|
| Секреты, credentials | .env |
| Python проект | pyproject.toml |
| Rust проект | Cargo.toml |
| DevOps, K8s | YAML |
| Git конфигурация | INI |
| API, веб | JSON |
| Простые настройки | INI или TOML |

### 6.2 Конвертация

```python
# INI → JSON
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

data = {s: dict(config[s]) for s in config.sections()}
print(json.dumps(data, indent=2))
```

---

## 7. Best Practices

### 7.1 Безопасность

```bash
# .gitignore
.env
*.pem
*_secret*
config/local.toml
```

### 7.2 Структура конфигурации

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # С дефолтами
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    PORT = int(os.getenv('PORT', '8080'))
    
    # Обязательные
    DATABASE_URL = os.environ['DATABASE_URL']  # Падает если нет
    SECRET_KEY = os.environ['SECRET_KEY']
```

### 7.3 Валидация конфигурации

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8080
    
    class Config:
        env_file = '.env'

settings = Settings()  # Автоматическая валидация
```

---

## 💡 Key Takeaways

- **INI — простой legacy формат**: Секции, строковые значения, ограниченные возможности.

- **TOML — современный стандарт**: Типы данных, читаемость, pyproject.toml.

- **.env — для секретов**: Переменные окружения, НЕ коммитить в Git.

- **Выбор формата**: Python → TOML, DevOps → YAML, секреты → .env.

---

## 🚀 Next Steps

**Practice Ideas:**
1. Создайте pyproject.toml для своего Python проекта
2. Настройте .env для Docker Compose приложения
3. Напишите скрипт конвертации INI → TOML

---

## 📚 Additional Resources

- [TOML Specification](https://toml.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---


