# Python External Packages
## Обзор популярных модулей из PyPI

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь использовать pip для установки пакетов
- Знать работу с виртуальными окружениями
- Понимать импорт модулей и пакетов
- Иметь опыт работы со стандартной библиотекой

**Recommended prior modules:**

- [Modules](../06_Modules/) — организация кода, pip, виртуальные окружения
- [Standard Modules](../09_StandardModules/) — стандартная библиотека Python

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Делать HTTP-запросы с помощью requests
- Работать с данными используя pandas
- Создавать CLI-приложения с click/argparse
- Управлять конфигурацией с python-dotenv
- Выбирать подходящие библиотеки для своих задач

---

## 1. requests — HTTP-запросы

### 1.1 Установка и базовое использование

```bash

pip install requests

```

```python

import requests

# GET-запрос
response = requests.get("https://api.github.com/users/python")
print(f"Status: {response.status_code}")
print(f"Headers: {dict(list(response.headers.items())[:3])}")

# JSON ответ
data = response.json()
print(f"Login: {data['login']}")
print(f"Name: {data.get('name')}")
print(f"Public repos: {data['public_repos']}")

```

**Output:**
```

Status: 200
Headers: {'Server': 'GitHub.com', 'Content-Type': 'application/json; charset=utf-8', 'X-GitHub-Media-Type': 'github.v3'}
Login: python
Name: Python
Public repos: 55

```

### 1.2 Параметры и заголовки

```python

import requests

# GET с параметрами
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc"
}
response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)
print(f"URL: {response.url}")

# Заголовки
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json",
    "User-Agent": "MyApp/1.0"
}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

```

### 1.3 POST и другие методы

```python

import requests

# POST с JSON
data = {
    "title": "New Post",
    "body": "Content here",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print(f"Status: {response.status_code}")
print(f"Created: {response.json()}")

# POST с form data
response = requests.post(
    "https://httpbin.org/post",
    data={"name": "value"}
)

# PUT, DELETE, PATCH
# requests.put(url, json=data)
# requests.delete(url)
# requests.patch(url, json=data)
```

**Output:**
```

Status: 201
Created: {'title': 'New Post', 'body': 'Content here', 'userId': 1, 'id': 101}

```

### 1.4 Обработка ошибок и таймауты

```python

import requests
from requests.exceptions import RequestException, Timeout, HTTPError

def safe_request(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Вызывает HTTPError для 4xx/5xx
        return response.json()
    except Timeout:
        print(f"Таймаут при запросе к {url}")
    except HTTPError as e:
        print(f"HTTP ошибка: {e.response.status_code}")
    except RequestException as e:
        print(f"Ошибка запроса: {e}")
    return None

# Использование
data = safe_request("https://api.github.com/users/python")
if data:
    print(f"Получено: {data['login']}")

```

### 1.5 Сессии для повторных запросов

```python

import requests

# Сессия сохраняет настройки между запросами
with requests.Session() as session:
    session.headers.update({"User-Agent": "MyApp/1.0"})
    
    # Все запросы используют общие настройки
    r1 = session.get("https://api.github.com/users/python")
    r2 = session.get("https://api.github.com/users/django")
    
    print(f"Python repos: {r1.json()['public_repos']}")
    print(f"Django repos: {r2.json()['public_repos']}")

```

---

## 2. python-dotenv — управление конфигурацией

### 2.1 Установка и базовое использование

```bash

pip install python-dotenv

```

Создайте файл `.env`:
```
# .env
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=your-secret-api-key
DEBUG=true
MAX_CONNECTIONS=10

```

```python

import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Теперь они доступны через os.environ
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG", "false").lower() == "true"
max_conn = int(os.getenv("MAX_CONNECTIONS", "5"))

print(f"Database: {database_url}")
print(f"Debug mode: {debug}")
print(f"Max connections: {max_conn}")

```

**Output:**
```

Database: postgresql://user:pass@localhost/db
Debug mode: True
Max connections: 10

```

### 2.2 Различные файлы окружения

```python

from dotenv import load_dotenv
import os

# Загрузка конкретного файла
load_dotenv(".env.development")

# Или выбор по переменной окружения
env = os.getenv("APP_ENV", "development")
load_dotenv(f".env.{env}")

# Не перезаписывать существующие переменные
load_dotenv(override=False)

```

### 2.3 Паттерн конфигурации

```python
# config.py
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Config:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///default.db")
    api_key: str = os.getenv("API_KEY", "")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

config = Config()

# Использование в других модулях
# from config import config
# print(config.database_url)
```

---

## 3. click — создание CLI

### 3.1 Установка и простой пример

```bash

pip install click

```

```python
# cli.py
import click

@click.command()
@click.option("--name", "-n", default="World", help="Имя для приветствия")
@click.option("--count", "-c", default=1, type=int, help="Количество повторений")
def hello(name, count):
    """Простая программа, которая приветствует NAME."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()

```

```bash

$ python cli.py --name Alice --count 3
Hello, Alice!
Hello, Alice!
Hello, Alice!

$ python cli.py --help
Usage: cli.py [OPTIONS]

  Простая программа, которая приветствует NAME.

Options:
  -n, --name TEXT    Имя для приветствия
  -c, --count INTEGER  Количество повторений
  --help             Show this message and exit.

```

### 3.2 Аргументы и опции

```python

import click

@click.command()
@click.argument("filename")  # Обязательный аргумент
@click.option("--output", "-o", type=click.Path(), help="Выходной файл")
@click.option("--verbose", "-v", is_flag=True, help="Подробный вывод")
@click.option("--format", type=click.Choice(["json", "csv", "xml"]), default="json")
def process(filename, output, verbose, format):
    """Обрабатывает FILENAME и сохраняет результат."""
    if verbose:
        click.echo(f"Обработка {filename} в формате {format}")
    
    # Логика обработки...
    
    if output:
        click.echo(f"Сохранено в {output}")
    else:
        click.echo("Результат выведен в stdout")

if __name__ == "__main__":
    process()

```

### 3.3 Группы команд

```python

import click

@click.group()
def cli():
    """Утилита управления пользователями."""
    pass

@cli.command()
@click.argument("username")
@click.option("--email", required=True)
def create(username, email):
    """Создаёт нового пользователя."""
    click.echo(f"Создан пользователь {username} ({email})")

@cli.command()
@click.argument("username")
def delete(username):
    """Удаляет пользователя."""
    if click.confirm(f"Удалить пользователя {username}?"):
        click.echo(f"Пользователь {username} удалён")
    else:
        click.echo("Отменено")

@cli.command()
def list():
    """Показывает список пользователей."""
    users = ["alice", "bob", "charlie"]
    for user in users:
        click.echo(f"  - {user}")

if __name__ == "__main__":
    cli()

```

```bash

$ python cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  Утилита управления пользователями.

Options:
  --help  Show this message and exit.

Commands:
  create  Создаёт нового пользователя.
  delete  Удаляет пользователя.
  list    Показывает список пользователей.

$ python cli.py create alice --email alice@example.com
Создан пользователь alice (alice@example.com)

$ python cli.py list
  - alice
  - bob
  - charlie

```

---

## 4. pandas — работа с данными

### 4.1 Установка и базовые операции

```bash

pip install pandas

```

```python

import pandas as pd

# Создание DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "city": ["Moscow", "London", "Paris", "Berlin"],
    "salary": [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Информация о данных
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Types:\n{df.dtypes}")

```

**Output:**
```

DataFrame:
      name  age    city  salary
0    Alice   25  Moscow   50000
1      Bob   30  London   60000
2  Charlie   35   Paris   70000
3    Diana   28  Berlin   55000

Shape: (4, 4)
Columns: ['name', 'age', 'city', 'salary']
Types:
name      object
age        int64
city      object
salary     int64
dtype: object

```

### 4.2 Выбор данных

```python

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 70000, 55000]
})

# Выбор столбца
print("Столбец 'name':")
print(df["name"])
print()

# Выбор нескольких столбцов
print("Несколько столбцов:")
print(df[["name", "salary"]])
print()

# Выбор строк по условию
print("Возраст > 28:")
print(df[df["age"] > 28])
print()

# loc и iloc
print("loc (по меткам):")
print(df.loc[0:2, ["name", "age"]])
print()

print("iloc (по индексам):")
print(df.iloc[0:2, 0:2])

```

**Output:**
```

Столбец 'name':
0      Alice
1        Bob
2    Charlie
3      Diana
Name: name, dtype: object

Несколько столбцов:
      name  salary
0    Alice   50000
1      Bob   60000
2  Charlie   70000
3    Diana   55000

Возраст > 28:
      name  age  salary
1      Bob   30   60000
2  Charlie   35   70000

loc (по меткам):
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35

iloc (по индексам):
    name  age
0  Alice   25
1    Bob   30

```

### 4.3 Операции с данными

```python

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "department": ["IT", "Sales", "IT", "Sales"],
    "salary": [50000, 60000, 70000, 55000]
})

# Добавление столбца
df["bonus"] = df["salary"] * 0.1
print("С бонусом:")
print(df)
print()

# Группировка
print("Группировка по отделу:")
grouped = df.groupby("department")["salary"].agg(["mean", "sum", "count"])
print(grouped)
print()

# Сортировка
print("Сортировка по зарплате:")
print(df.sort_values("salary", ascending=False))

```

**Output:**
```

С бонусом:
      name department  salary   bonus
0    Alice         IT   50000  5000.0
1      Bob      Sales   60000  6000.0
2  Charlie         IT   70000  7000.0
3    Diana      Sales   55000  5500.0

Группировка по отделу:
               mean     sum  count
department                        
IT           60000.0  120000      2
Sales        57500.0  115000      2

Сортировка по зарплате:
      name department  salary   bonus
2  Charlie         IT   70000  7000.0
1      Bob      Sales   60000  6000.0
3    Diana      Sales   55000  5500.0
0    Alice         IT   50000  5000.0

```

### 4.4 Чтение и запись файлов

```python

import pandas as pd

# Создание тестовых данных
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})

# CSV
df.to_csv("data.csv", index=False)
df_csv = pd.read_csv("data.csv")
print("Из CSV:")
print(df_csv)
print()

# JSON
df.to_json("data.json", orient="records", indent=2)
df_json = pd.read_json("data.json")
print("Из JSON:")
print(df_json)
print()

# Excel (требует openpyxl)
# df.to_excel("data.xlsx", index=False)
# df_excel = pd.read_excel("data.xlsx")
```

**Output:**
```

Из CSV:
      name  age  salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000

Из JSON:
      name  age  salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000

```

---

## 5. pytest — тестирование

### 5.1 Установка и базовые тесты

```bash

pip install pytest

```

```python
# test_math.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Тесты
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

```

```bash

$ pytest test_math.py -v
============================= test session starts ==============================
test_math.py::test_add PASSED
test_math.py::test_divide PASSED
test_math.py::test_divide_by_zero PASSED
============================== 3 passed in 0.01s ===============================

```

### 5.2 Фикстуры

```python
# test_with_fixtures.py
import pytest

@pytest.fixture
def sample_data():
    """Подготавливает тестовые данные."""
    return {"users": ["alice", "bob"], "count": 2}

@pytest.fixture
def temp_file(tmp_path):
    """Создаёт временный файл."""
    file = tmp_path / "test.txt"
    file.write_text("test content")
    return file

def test_with_data(sample_data):
    assert len(sample_data["users"]) == sample_data["count"]

def test_with_file(temp_file):
    content = temp_file.read_text()
    assert content == "test content"

```

### 5.3 Параметризация

```python

import pytest

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

@pytest.mark.parametrize("input,expected", [
    ("radar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
])
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected

```

```bash

$ pytest test_palindrome.py -v
test_palindrome.py::test_is_palindrome[radar-True] PASSED
test_palindrome.py::test_is_palindrome[hello-False] PASSED
test_palindrome.py::test_is_palindrome[A man a plan a canal Panama-True] PASSED
test_palindrome.py::test_is_palindrome[-True] PASSED
test_palindrome.py::test_is_palindrome[a-True] PASSED

```

---

## 6. Pydantic — валидация данных

### 6.1 Установка и базовые модели

```bash

pip install pydantic

```

```python

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)
    
    @validator('name')
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError('Name must be capitalized')
        return v

# Валидный пользователь
user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    age=30,
    tags=["admin", "active"]
)
print(f"User: {user}")
print(f"Dict: {user.dict()}")
print(f"JSON: {user.json()}")

```

**Output:**
```

User: id=1 name='Alice' email='alice@example.com' age=30 tags=['admin', 'active'] created_at=datetime.datetime(2024, 12, 2, 15, 30, 0, 0)
Dict: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 30, 'tags': ['admin', 'active'], 'created_at': datetime.datetime(2024, 12, 2, 15, 30, 0, 0)}
JSON: {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30, "tags": ["admin", "active"], "created_at": "2024-12-02T15:30:00"}

```

### 6.2 Обработка ошибок валидации

```python

from pydantic import BaseModel, ValidationError

class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Невалидные данные
try:
    item = Item(name="Widget", price="not a number", quantity=-5)
except ValidationError as e:
    print("Ошибки валидации:")
    for error in e.errors():
        print(f"  {error['loc']}: {error['msg']}")

```

**Output:**
```

Ошибки валидации:
  ('price',): value is not a valid float
  ('quantity',): ensure this value is greater than or equal to 0

```

---

## 7. tqdm — прогресс-бары

### 7.1 Установка и базовое использование

```bash

pip install tqdm

```

```python

from tqdm import tqdm
import time

# Простой прогресс-бар
for i in tqdm(range(100), desc="Processing"):
    time.sleep(0.01)

# С ручным обновлением
with tqdm(total=100, desc="Downloading") as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)

# Вложенные прогресс-бары
for i in tqdm(range(3), desc="Outer"):
    for j in tqdm(range(100), desc="Inner", leave=False):
        time.sleep(0.001)

```

**Output:**
```

Processing: 100%|██████████████████████████████| 100/100 [00:01<00:00, 99.01it/s]
Downloading: 100%|████████████████████████████| 100/100 [00:01<00:00, 99.98it/s]
Outer:  33%|███████████                      | 1/3 [00:00<00:00,  9.99it/s]

```

### 7.2 С pandas

```python

from tqdm import tqdm
import pandas as pd

# Регистрируем tqdm для pandas
tqdm.pandas()

df = pd.DataFrame({"values": range(1000)})

# Прогресс для apply
df["squared"] = df["values"].progress_apply(lambda x: x ** 2)

```

---

## 8. Другие полезные библиотеки

### 8.1 httpx — асинхронные HTTP-запросы

```python
# pip install httpx
import httpx
import asyncio

async def fetch_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/python")
        return response.json()

# Запуск
# data = asyncio.run(fetch_users())
```

### 8.2 rich — красивый вывод

```python
# pip install rich
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# Красивая таблица
table = Table(title="Users")
table.add_column("Name", style="cyan")
table.add_column("Age", style="magenta")
table.add_row("Alice", "30")
table.add_row("Bob", "25")
console.print(table)

# Прогресс с стилем
for i in track(range(10), description="Processing..."):
    time.sleep(0.1)

```

### 8.3 loguru — улучшенное логирование

```python
# pip install loguru
from loguru import logger

# Автоматическое форматирование
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# Логирование в файл с ротацией
logger.add("app.log", rotation="500 MB", retention="10 days")

# Декоратор для исключений
@logger.catch
def risky_function():
    return 1 / 0

```

### 8.4 Schedule — планирование задач

```python
# pip install schedule
import schedule
import time

def job():
    print(f"Job executed at {time.strftime('%H:%M:%S')}")

# Расписание
schedule.every(10).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

# Запуск планировщика (в реальном коде)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
```

---

## 9. Выбор библиотек

### 9.1 По категориям

| Категория | Библиотека | Использование |
|-----------|------------|---------------|
| HTTP клиент | requests, httpx | API, веб-скрапинг |
| Веб-фреймворк | Flask, FastAPI, Django | Веб-приложения, API |
| Данные | pandas, polars | Анализ данных |
| Тестирование | pytest | Юнит-тесты |
| CLI | click, typer | Командная строка |
| Валидация | pydantic | Валидация данных |
| Конфигурация | python-dotenv | Переменные окружения |
| Логирование | loguru | Улучшенные логи |
| Прогресс | tqdm, rich | Прогресс-бары |
| Async | asyncio, httpx | Асинхронный код |

### 9.2 Критерии выбора

При выборе библиотеки обратите внимание на:

- **Популярность**: Звёзды на GitHub, скачивания на PyPI

- **Активность**: Дата последнего релиза, открытые issues

- **Документация**: Качество документации и примеров

- **Зависимости**: Количество и качество зависимостей

- **Совместимость**: Поддержка нужной версии Python

```bash
# Информация о пакете
pip show requests

# Скачивания
# https://pypistats.org/packages/requests
```

---

## 10. requirements.txt и управление зависимостями

### 10.1 Создание requirements.txt

```bash
# Все установленные пакеты
pip freeze > requirements.txt

# Установка из файла
pip install -r requirements.txt

```

### 10.2 Пример requirements.txt

```
# requirements.txt
requests>=2.28.0,<3.0.0
pandas>=1.5.0
click>=8.0.0
python-dotenv>=1.0.0
pydantic>=2.0.0
pytest>=7.0.0
tqdm>=4.65.0

# Dev зависимости (можно выделить в requirements-dev.txt)
black>=23.0.0
flake8>=6.0.0
mypy>=1.0.0

```

### 10.3 Современный подход с pyproject.toml

```toml
# pyproject.toml
[project]
name = "myproject"
version = "1.0.0"
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.5.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.black]
line-length = 88

```

---

## 💡 Key Takeaways

- **requests — для HTTP**: Простой и мощный. Используйте сессии для повторных запросов.

- **pandas — для данных**: Стандарт для работы с табличными данными. Изучите groupby, merge, pivot.

- **click — для CLI**: Декларативный подход к созданию командной строки. Легко создавать подкоманды.

- **pytest — для тестов**: Фикстуры и параметризация делают тесты чистыми и читаемыми.

- **pydantic — для валидации**: Валидация на основе типов. Отлично работает с FastAPI.

---

## 🚀 Next Steps

**Practice Ideas:**

1. Создайте CLI-утилиту для работы с API (requests + click)
2. Напишите скрипт анализа данных с pandas и визуализацией
3. Создайте веб-API с FastAPI и pydantic
4. Покройте свой код тестами с pytest

**Going Deeper:**

- Изучите FastAPI для создания современных API
- Познакомьтесь с SQLAlchemy для работы с БД
- Изучите Celery для фоновых задач
- Попробуйте Poetry для управления зависимостями

---

## 📚 Additional Resources

**Documentation:**

- [requests](https://requests.readthedocs.io/)
- [pandas](https://pandas.pydata.org/docs/)
- [click](https://click.palletsprojects.com/)
- [pytest](https://docs.pytest.org/)
- [pydantic](https://docs.pydantic.dev/)

**PyPI:**

- [PyPI — Python Package Index](https://pypi.org/)
- [Awesome Python](https://awesome-python.com/) — каталог библиотек

---




