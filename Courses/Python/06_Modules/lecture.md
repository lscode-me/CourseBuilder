# Python Modules
## Модули, пакеты и организация кода

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь создавать функции и классы
- Понимать области видимости переменных
- Знать работу с файловой системой
- Уметь запускать Python-скрипты из командной строки

**Recommended prior modules:**

- [Classes](../05_Classes/) — классы и объектно-ориентированное программирование

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и импортировать собственные модули
- Организовывать код в пакеты с правильной структурой
- Использовать различные способы импорта
- Понимать механизм поиска модулей Python
- Создавать переиспользуемые библиотеки

---

## 1. Что такое модуль

Модуль — это файл с расширением `.py`, содержащий Python-код. Модули позволяют организовать код, сделать его переиспользуемым и избежать конфликтов имён.

### 1.1 Создание простого модуля

Создадим файл `math_utils.py`:

```python
# math_utils.py
"""Модуль с математическими утилитами."""

PI = 3.14159

def square(x):
    """Возвращает квадрат числа."""
    return x ** 2

def cube(x):
    """Возвращает куб числа."""
    return x ** 3

def factorial(n):
    """Вычисляет факториал числа."""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Calculator:
    """Простой калькулятор."""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

```

### 1.2 Импорт модуля

```python
# main.py
import math_utils

print(f"PI = {math_utils.PI}")
print(f"square(5) = {math_utils.square(5)}")
print(f"factorial(5) = {math_utils.factorial(5)}")

calc = math_utils.Calculator()
print(f"calc.add(3, 5) = {calc.add(3, 5)}")

```

**Output:**
```

PI = 3.14159
square(5) = 25
factorial(5) = 120
calc.add(3, 5) = 8

```

### 1.3 Различные способы импорта

```python
# Импорт всего модуля
import math_utils
result = math_utils.square(5)

# Импорт с псевдонимом
import math_utils as mu
result = mu.square(5)

# Импорт конкретных объектов
from math_utils import square, PI
result = square(5)
print(PI)

# Импорт с переименованием
from math_utils import factorial as fact
result = fact(5)

# Импорт всего (НЕ рекомендуется!)
from math_utils import *
result = square(5)  # Непонятно откуда взялось

```

> **⚠️ Warning:**  
> Избегайте `from module import *` — это загрязняет пространство имён и делает код непонятным.

---

## 2. Пространства имён и области видимости

### 2.1 Пространство имён модуля

Каждый модуль имеет своё пространство имён:

```python
# module_a.py
value = "A"
def get_value():
    return value

# module_b.py
value = "B"
def get_value():
    return value

# main.py
import module_a
import module_b

print(module_a.value)       # "A"
print(module_b.value)       # "B"
print(module_a.get_value()) # "A"
print(module_b.get_value()) # "B"

```

### 2.2 Атрибут __name__

Каждый модуль имеет атрибут `__name__`:

```python
# mymodule.py
print(f"__name__ = {__name__}")

def main():
    print("Функция main выполняется")

# Это выполнится только при прямом запуске
if __name__ == "__main__":
    main()

```

При импорте:
```python
# other.py
import mymodule  # Выведет: __name__ = mymodule

```

При прямом запуске:
```bash

python mymodule.py  # Выведет: __name__ = __main__, затем "Функция main выполняется"

```

**Output:**
```

__name__ = mymodule
__name__ = __main__
Функция main выполняется

```

Это стандартный паттерн для модулей, которые могут использоваться и как библиотека, и как скрипт.

### 2.3 Атрибут __all__

`__all__` определяет, что экспортируется при `from module import *`:

```python
# my_library.py
__all__ = ['public_function', 'PublicClass']

def public_function():
    return "public"

def _private_function():
    return "private"

class PublicClass:
    pass

class _PrivateClass:
    pass

# При from my_library import * импортируются только public_function и PublicClass
```

---

## 3. Пакеты

### 3.1 Структура пакета

Пакет — это директория с файлом `__init__.py`:

```

mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

```

```python
# mypackage/__init__.py
"""Главный пакет."""
from .module1 import func1
from .module2 import func2

__version__ = "1.0.0"

```

```python
# mypackage/module1.py
def func1():
    return "func1 from module1"

```

```python
# mypackage/module2.py
def func2():
    return "func2 from module2"

```

```python
# mypackage/subpackage/__init__.py
from .module3 import func3

```

```python
# mypackage/subpackage/module3.py
def func3():
    return "func3 from subpackage"

```

### 3.2 Импорт из пакета

```python
# Разные способы импорта
import mypackage
print(mypackage.func1())
print(mypackage.__version__)

from mypackage import func1, func2
print(func1())

from mypackage.module1 import func1
print(func1())

from mypackage.subpackage import func3
print(func3())

from mypackage.subpackage.module3 import func3
print(func3())

```

**Output:**
```

func1 from module1
1.0.0
func1 from module1
func1 from module1
func3 from subpackage
func3 from subpackage

```

### 3.3 Относительные импорты

Внутри пакета можно использовать относительные импорты:

```python
# mypackage/module2.py
from .module1 import func1  # Из того же пакета
from ..otherpackage import something  # Из родительского пакета
from . import module1  # Импорт модуля из того же пакета

```

> **💡 Pro Tip:**  
> Относительные импорты работают только внутри пакетов. В скриптах верхнего уровня используйте абсолютные импорты.

---

## 4. Поиск модулей

### 4.1 sys.path

Python ищет модули в директориях из `sys.path`:

```python

import sys

print("Пути поиска модулей:")
for path in sys.path:
    print(f"  {path}")

```

**Output:**
```

Пути поиска модулей:
  /current/directory
  /usr/lib/python3.11
  /usr/lib/python3.11/lib-dynload
  /home/user/.local/lib/python3.11/site-packages
  /usr/local/lib/python3.11/dist-packages
  /usr/lib/python3/dist-packages

```

### 4.2 Порядок поиска

1. Директория запущенного скрипта
2. Директории из переменной окружения `PYTHONPATH`
3. Стандартная библиотека
4. site-packages (установленные пакеты)

### 4.3 Добавление путей

```python

import sys

# Добавление пути программно
sys.path.insert(0, '/path/to/my/modules')

# Теперь можно импортировать модули из этой директории
import my_custom_module

```

```bash
# Через переменную окружения
export PYTHONPATH="/path/to/modules:$PYTHONPATH"
python script.py

```

### 4.4 Файл .pth

Создайте файл с расширением `.pth` в site-packages:

```
# myproject.pth
/path/to/my/project
/another/path

```

---

## 5. Практическая организация проекта

### 5.1 Типичная структура проекта

```

myproject/
├── README.md
├── requirements.txt
├── setup.py
├── pyproject.toml
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── core.py
│       ├── utils.py
│       └── models/
│           ├── __init__.py
│           └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
└── scripts/
    └── run_app.py

```

### 5.2 Файл setup.py

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="A short description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/mypackage",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "click>=7.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "mycommand=mypackage.cli:main",
        ],
    },
)

```

### 5.3 Файл pyproject.toml (современный подход)

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "1.0.0"
description = "A short description"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.25.0",
    "click>=7.0",
]

[project.optional-dependencies]
dev = ["pytest", "black", "flake8"]

[project.scripts]
mycommand = "mypackage.cli:main"

```

### 5.4 Установка в режиме разработки

```bash
# Установка пакета в editable mode
pip install -e .

# С dev зависимостями
pip install -e ".[dev]"

```

---

## 6. Встроенные модули

### 6.1 Полезные встроенные модули

```python
# os — работа с операционной системой
import os
print(f"Текущая директория: {os.getcwd()}")
print(f"Переменные окружения: {os.environ.get('HOME')}")

# sys — системные параметры
import sys
print(f"Версия Python: {sys.version}")
print(f"Платформа: {sys.platform}")

# datetime — дата и время
from datetime import datetime, timedelta
now = datetime.now()
print(f"Сейчас: {now}")
print(f"Через неделю: {now + timedelta(days=7)}")

# json — работа с JSON
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)
print(f"JSON:\n{json_str}")

# pathlib — современная работа с путями
from pathlib import Path
home = Path.home()
print(f"Домашняя директория: {home}")

```

**Output:**
```

Текущая директория: /home/user/project
Переменные окружения: /home/user
Версия Python: 3.11.5 (main, Aug 25 2023, 13:19:05)
Платформа: linux
Сейчас: 2024-12-02 15:30:00.123456
Через неделю: 2024-12-09 15:30:00.123456
JSON:
{
  "name": "Alice",
  "age": 30
}
Домашняя директория: /home/user

```

### 6.2 Инспекция модулей

```python

import math

# Просмотр содержимого модуля
print("Атрибуты модуля math:")
print([attr for attr in dir(math) if not attr.startswith('_')][:10])

# Документация
print(f"\nmath.sqrt.__doc__: {math.sqrt.__doc__}")

# Путь к файлу модуля
print(f"\nmath.__file__: {getattr(math, '__file__', 'built-in')}")

```

**Output:**
```

Атрибуты модуля math:
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb']

math.sqrt.__doc__: Return the square root of x.

math.__file__: built-in

```

---

## 7. Импорт и перезагрузка

### 7.1 Кэширование импортов

```python

import sys

# Модули кэшируются в sys.modules
print("Загруженные модули (первые 10):")
for name in list(sys.modules.keys())[:10]:
    print(f"  {name}")

# Проверка, загружен ли модуль
print(f"\nos загружен: {'os' in sys.modules}")

```

**Output:**
```

Загруженные модули (первые 10):
  sys
  builtins
  _frozen_importlib
  _imp
  _thread
  _warnings
  _weakref
  _io
  marshal
  posix

os загружен: True

```

### 7.2 Перезагрузка модуля

```python

import importlib
import mymodule

# Если модуль изменился, перезагружаем
importlib.reload(mymodule)

```

> **⚠️ Warning:**  
> Перезагрузка не обновляет уже созданные объекты и не работает с `from module import *`.

---

## 8. Создание переиспользуемой библиотеки

### 8.1 Пример: библиотека валидации

```

validators/
├── __init__.py
├── core.py
├── string_validators.py
├── number_validators.py
└── exceptions.py

```

```python
# validators/exceptions.py
class ValidationError(Exception):
    """Исключение валидации."""
    pass

```

```python
# validators/core.py
from abc import ABC, abstractmethod

class Validator(ABC):
    """Базовый класс валидатора."""
    
    @abstractmethod
    def validate(self, value):
        """Валидирует значение. Возвращает True или выбрасывает ValidationError."""
        pass
    
    def __call__(self, value):
        return self.validate(value)

```

```python
# validators/string_validators.py
from .core import Validator
from .exceptions import ValidationError

class NotEmptyValidator(Validator):
    """Проверяет, что строка не пуста."""
    
    def validate(self, value):
        if not value or not value.strip():
            raise ValidationError("Строка не должна быть пустой")
        return True

class EmailValidator(Validator):
    """Проверяет формат email."""
    
    def validate(self, value):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValidationError(f"Неверный формат email: {value}")
        return True

class LengthValidator(Validator):
    """Проверяет длину строки."""
    
    def __init__(self, min_length=0, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, value):
        length = len(value)
        if length < self.min_length:
            raise ValidationError(f"Минимальная длина: {self.min_length}")
        if self.max_length and length > self.max_length:
            raise ValidationError(f"Максимальная длина: {self.max_length}")
        return True

```

```python
# validators/number_validators.py
from .core import Validator
from .exceptions import ValidationError

class RangeValidator(Validator):
    """Проверяет, что число в диапазоне."""
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"Значение должно быть >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"Значение должно быть <= {self.max_value}")
        return True

class PositiveValidator(RangeValidator):
    """Проверяет, что число положительное."""
    
    def __init__(self):
        super().__init__(min_value=0)

```

```python
# validators/__init__.py
"""Библиотека валидаторов."""

from .exceptions import ValidationError
from .core import Validator
from .string_validators import NotEmptyValidator, EmailValidator, LengthValidator
from .number_validators import RangeValidator, PositiveValidator

__version__ = "1.0.0"
__all__ = [
    'ValidationError',
    'Validator',
    'NotEmptyValidator',
    'EmailValidator',
    'LengthValidator',
    'RangeValidator',
    'PositiveValidator',
]

```

### 8.2 Использование библиотеки

```python

from validators import (
    EmailValidator, 
    LengthValidator, 
    RangeValidator,
    ValidationError
)

# Создание валидаторов
email_validator = EmailValidator()
length_validator = LengthValidator(min_length=3, max_length=50)
age_validator = RangeValidator(min_value=0, max_value=150)

# Использование
def validate_user(email, username, age):
    try:
        email_validator(email)
        length_validator(username)
        age_validator(age)
        return True, "Валидация прошла успешно"
    except ValidationError as e:
        return False, str(e)

# Тесты
print(validate_user("alice@example.com", "alice", 30))
print(validate_user("invalid-email", "alice", 30))
print(validate_user("alice@example.com", "al", 30))
print(validate_user("alice@example.com", "alice", 200))

```

**Output:**
```

(True, 'Валидация прошла успешно')
(False, 'Неверный формат email: invalid-email')
(False, 'Минимальная длина: 3')
(False, 'Значение должно быть <= 150')

```

---

## 9. Распространённые паттерны

### 9.1 Lazy Import

Отложенный импорт для ускорения загрузки:

```python
# mypackage/__init__.py

def get_heavy_module():
    """Ленивая загрузка тяжёлого модуля."""
    from . import heavy_module
    return heavy_module

# Вместо:
# from . import heavy_module  # Загружается сразу
```

### 9.2 Условный импорт

```python
# Использование разных библиотек в зависимости от доступности
try:
    import ujson as json  # Быстрая реализация
except ImportError:
    import json  # Стандартная библиотека

# Проверка версии Python
import sys
if sys.version_info >= (3, 11):
    from tomllib import load as toml_load
else:
    from tomli import load as toml_load

```

### 9.3 Плагинная система

```python
# plugins/__init__.py
import importlib
import pkgutil

def load_plugins():
    """Автоматически загружает все плагины из директории."""
    plugins = {}
    
    # Находим все модули в пакете
    for finder, name, ispkg in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f".{name}", __package__)
        
        # Регистрируем плагин, если у него есть нужный атрибут
        if hasattr(module, 'register'):
            plugins[name] = module.register()
    
    return plugins

# plugins/plugin_a.py
def register():
    return {"name": "Plugin A", "handler": lambda x: x * 2}

# plugins/plugin_b.py
def register():
    return {"name": "Plugin B", "handler": lambda x: x + 10}

# main.py
from plugins import load_plugins

plugins = load_plugins()
for name, plugin in plugins.items():
    print(f"{plugin['name']}: {plugin['handler'](5)}")

```

**Output:**
```

Plugin A: 10
Plugin B: 15

```

---

## 10. Common Pitfalls

### 10.1 Циклические импорты

❌ **Ошибка:**
```python
# module_a.py
from module_b import func_b
def func_a():
    return func_b()

# module_b.py
from module_a import func_a  # Циклический импорт!
def func_b():
    return func_a()

```

✅ **Решения:**

```python
# 1. Импорт внутри функции
# module_a.py
def func_a():
    from module_b import func_b
    return func_b()

# 2. Реструктуризация — вынести общий код в третий модуль
# common.py
def shared_func():
    pass

# module_a.py
from common import shared_func

```

### 10.2 Изменение sys.path в __init__.py

❌ **Плохо:**
```python
# mypackage/__init__.py
import sys
sys.path.insert(0, '/some/path')  # Побочный эффект при импорте!

```

✅ **Хорошо:**
```python
# Настраивайте пути в точке входа, не в __init__.py
```

### 10.3 from module import *

❌ **Плохо:**
```python

from os import *
from sys import *
# Теперь непонятно, откуда взялись path, getcwd и т.д.
```

✅ **Хорошо:**
```python

import os
import sys
# Явно видно происхождение: os.path, sys.path
```

### 10.4 Забытый __init__.py в Python 3.3+

```python
# В Python 3.3+ можно создавать namespace packages без __init__.py
# Но для обычных пакетов лучше его создавать для явности

# mypackage/__init__.py
"""Документация пакета."""
__version__ = "1.0.0"

```

---

## 💡 Key Takeaways

- **Модуль = файл .py**: Каждый Python-файл автоматически является модулем.

- **Пакет = директория с __init__.py**: Используйте пакеты для организации связанных модулей.

- **if __name__ == "__main__"**: Стандартный паттерн для кода, выполняемого только при прямом запуске.

- **Избегайте from module import ***: Явные импорты делают код понятнее и предотвращают конфликты имён.

- **pyproject.toml — современный стандарт**: Используйте его вместо setup.py для новых проектов.

---

## 🚀 Next Steps

**Related Modules:**

- [Exceptions](../07_Exceptions/) — создание исключений для библиотек
- [Standard Modules](../09_StandardModules/) — обзор стандартной библиотеки

**Practice Ideas:**

1. Создайте пакет утилит для работы со строками (форматирование, валидация)
2. Организуйте существующий проект в правильную структуру пакета
3. Создайте библиотеку с настраиваемыми логгерами
4. Реализуйте простую плагинную систему

**Going Deeper:**

- Изучите создание и публикацию пакетов на PyPI
- Познакомьтесь с importlib для динамических импортов
- Изучите namespace packages (PEP 420)

---

## 📚 Additional Resources

**Documentation:**

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [importlib](https://docs.python.org/3/library/importlib.html)

**PEPs:**

- [PEP 328](https://peps.python.org/pep-0328/) — Imports: Multi-Line and Absolute/Relative
- [PEP 420](https://peps.python.org/pep-0420/) — Implicit Namespace Packages

---




