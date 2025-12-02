# Python Exceptions
## Обработка исключений и управление ошибками

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Уметь создавать функции и классы
- Понимать поток выполнения программы
- Знать основы ООП (наследование)
- Иметь опыт отладки Python-программ

**Recommended prior modules:**
- [Classes](../05_Classes/) — классы и наследование
- [Modules](../06_Modules/) — организация кода в модули

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Обрабатывать исключения с помощью try/except/else/finally
- Создавать собственные классы исключений
- Понимать иерархию встроенных исключений
- Применять best practices обработки ошибок
- Использовать контекстные менеджеры для управления ресурсами

---

## 1. Введение в исключения

Исключения — это события, которые нарушают нормальный поток выполнения программы. Python использует исключения для сообщения об ошибках и особых ситуациях.

### 1.1 Что происходит при ошибке

```python
# Без обработки исключений — программа завершается
numbers = [1, 2, 3]
print(numbers[10])  # IndexError: list index out of range
```

**Output:**
```
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    print(numbers[10])
IndexError: list index out of range
```

### 1.2 Базовая обработка исключений

```python
numbers = [1, 2, 3]

try:
    print(numbers[10])
except IndexError:
    print("Индекс выходит за пределы списка")

print("Программа продолжает работу")
```

**Output:**
```
Индекс выходит за пределы списка
Программа продолжает работу
```

### 1.3 Получение информации об исключении

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Тип ошибки: {type(e).__name__}")
    print(f"Сообщение: {e}")
    print(f"Аргументы: {e.args}")
```

**Output:**
```
Тип ошибки: ZeroDivisionError
Сообщение: division by zero
Аргументы: ('division by zero',)
```

---

## 2. Синтаксис try/except/else/finally

### 2.1 Полный синтаксис

```python
def divide(a, b):
    try:
        # Код, который может вызвать исключение
        result = a / b
    except ZeroDivisionError:
        # Обработка конкретного исключения
        print("Деление на ноль!")
        return None
    except TypeError as e:
        # Обработка с доступом к объекту исключения
        print(f"Ошибка типа: {e}")
        return None
    else:
        # Выполняется, если исключений НЕ было
        print("Деление выполнено успешно")
        return result
    finally:
        # Выполняется ВСЕГДА (даже при return)
        print("Блок finally выполнен")

print(f"divide(10, 2) = {divide(10, 2)}")
print()
print(f"divide(10, 0) = {divide(10, 0)}")
print()
print(f"divide('10', 2) = {divide('10', 2)}")
```

**Output:**
```
Деление выполнено успешно
Блок finally выполнен
divide(10, 2) = 5.0

Деление на ноль!
Блок finally выполнен
divide(10, 0) = None

Ошибка типа: unsupported operand type(s) for /: 'str' and 'int'
Блок finally выполнен
divide('10', 2) = None
```

### 2.2 Обработка нескольких типов исключений

```python
def process_data(data, index):
    try:
        value = data[index]
        result = 100 / value
        return result
    except (IndexError, KeyError) as e:
        # Группировка похожих исключений
        print(f"Ошибка доступа: {e}")
    except ZeroDivisionError:
        print("Значение равно нулю")
    except Exception as e:
        # Ловит все остальные исключения
        print(f"Неожиданная ошибка: {type(e).__name__}: {e}")

process_data([1, 2, 0], 0)   # 100.0
process_data([1, 2, 0], 10)  # Ошибка доступа
process_data([1, 2, 0], 2)   # Значение равно нулю
```

**Output:**
```
Ошибка доступа: list index out of range
Значение равно нулю
```

### 2.3 Блок finally для очистки ресурсов

```python
def read_file(filename):
    f = None
    try:
        f = open(filename, 'r')
        return f.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    finally:
        # Гарантированно закрываем файл
        if f:
            f.close()
            print("Файл закрыт")

content = read_file("nonexistent.txt")
```

**Output:**
```
Файл nonexistent.txt не найден
```

> **💡 Pro Tip:**  
> Для работы с файлами лучше использовать `with` — он автоматически закрывает ресурсы.

---

## 3. Иерархия исключений

### 3.1 Встроенная иерархия

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── ...
    ├── RuntimeError
    │   └── RecursionError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    └── Warning
```

### 3.2 Наиболее частые исключения

```python
# ValueError — неправильное значение
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError — неправильный тип
try:
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError — ключ не найден в словаре
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

# AttributeError — атрибут не существует
try:
    "hello".nonexistent()
except AttributeError as e:
    print(f"AttributeError: {e}")

# FileNotFoundError — файл не найден
try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
```

**Output:**
```
ValueError: invalid literal for int() with base 10: 'abc'
TypeError: can only concatenate str (not "int") to str
KeyError: 'b'
AttributeError: 'str' object has no attribute 'nonexistent'
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
```

### 3.3 Порядок обработки важен

```python
# ПЛОХО — Exception перехватит всё
try:
    d = {}
    print(d["key"])
except Exception:
    print("Общая ошибка")
except KeyError:  # Никогда не выполнится!
    print("Ключ не найден")

# ХОРОШО — сначала конкретные, потом общие
try:
    d = {}
    print(d["key"])
except KeyError:
    print("Ключ не найден")
except Exception:
    print("Другая ошибка")
```

**Output:**
```
Общая ошибка
Ключ не найден
```

---

## 4. Генерация исключений

### 4.1 Оператор raise

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Возраст должен быть целым числом, получено: {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Возраст не может быть отрицательным: {age}")
    if age > 150:
        raise ValueError(f"Возраст слишком большой: {age}")
    return True

# Тесты
try:
    validate_age("25")
except TypeError as e:
    print(f"TypeError: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

print(f"validate_age(25) = {validate_age(25)}")
```

**Output:**
```
TypeError: Возраст должен быть целым числом, получено: str
ValueError: Возраст не может быть отрицательным: -5
validate_age(25) = True
```

### 4.2 Повторное возбуждение исключения

```python
def process_data(data):
    try:
        # Какая-то обработка
        return int(data)
    except ValueError:
        print(f"Логирование: не удалось преобразовать '{data}'")
        raise  # Повторно возбуждаем то же исключение

try:
    process_data("abc")
except ValueError as e:
    print(f"Поймано в main: {e}")
```

**Output:**
```
Логирование: не удалось преобразовать 'abc'
Поймано в main: invalid literal for int() with base 10: 'abc'
```

### 4.3 Цепочки исключений (Exception Chaining)

```python
def load_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as e:
        # raise ... from e — сохраняет связь с оригинальным исключением
        raise RuntimeError(f"Не удалось загрузить конфигурацию") from e

try:
    load_config("config.txt")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Причина: {e.__cause__}")
```

**Output:**
```
RuntimeError: Не удалось загрузить конфигурацию
Причина: [Errno 2] No such file or directory: 'config.txt'
```

---

## 5. Создание собственных исключений

### 5.1 Базовое пользовательское исключение

```python
class ApplicationError(Exception):
    """Базовое исключение приложения."""
    pass

class ValidationError(ApplicationError):
    """Ошибка валидации данных."""
    pass

class DatabaseError(ApplicationError):
    """Ошибка работы с базой данных."""
    pass

def validate_email(email):
    if "@" not in email:
        raise ValidationError(f"Неверный формат email: {email}")
    return True

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"Ошибка валидации: {e}")
except ApplicationError as e:
    print(f"Ошибка приложения: {e}")
```

**Output:**
```
Ошибка валидации: Неверный формат email: invalid-email
```

### 5.2 Исключения с дополнительными данными

```python
class HTTPError(Exception):
    """Исключение HTTP-запроса."""
    
    def __init__(self, status_code, message, url=None):
        self.status_code = status_code
        self.message = message
        self.url = url
        super().__init__(f"HTTP {status_code}: {message}")
    
    def __repr__(self):
        return f"HTTPError({self.status_code}, '{self.message}', url='{self.url}')"

def fetch_url(url):
    # Симуляция HTTP-запроса
    if "error" in url:
        raise HTTPError(404, "Not Found", url)
    return "Success"

try:
    fetch_url("http://example.com/error")
except HTTPError as e:
    print(f"Код статуса: {e.status_code}")
    print(f"Сообщение: {e.message}")
    print(f"URL: {e.url}")
    print(f"repr: {repr(e)}")
```

**Output:**
```
Код статуса: 404
Сообщение: Not Found
URL: http://example.com/error
repr: HTTPError(404, 'Not Found', url='http://example.com/error')
```

### 5.3 Иерархия пользовательских исключений

```python
# Хорошая практика — создать иерархию исключений для библиотеки

class LibraryError(Exception):
    """Базовое исключение библиотеки."""
    pass

class ConfigurationError(LibraryError):
    """Ошибка конфигурации."""
    pass

class ConnectionError(LibraryError):
    """Ошибка подключения."""
    pass

class AuthenticationError(ConnectionError):
    """Ошибка аутентификации."""
    pass

class TimeoutError(ConnectionError):
    """Таймаут подключения."""
    pass

# Пользователь может ловить:
# - Конкретное исключение (AuthenticationError)
# - Группу исключений (ConnectionError — все ошибки подключения)
# - Все исключения библиотеки (LibraryError)
```

---

## 6. Контекстные менеджеры

### 6.1 Оператор with

```python
# Без контекстного менеджера
f = open("file.txt", "w")
try:
    f.write("Hello")
finally:
    f.close()

# С контекстным менеджером — чище и безопаснее
with open("file.txt", "w") as f:
    f.write("Hello")
# Файл автоматически закрыт

# Несколько контекстных менеджеров
with open("input.txt") as fin, open("output.txt", "w") as fout:
    data = fin.read()
    fout.write(data.upper())
```

### 6.2 Создание контекстного менеджера (класс)

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None
    
    def __enter__(self):
        print(f"Подключение к {self.host}")
        self.connection = f"Connection to {self.host}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Закрытие соединения с {self.host}")
        self.connection = None
        
        # Возвращаем False — исключение не подавляется
        # Возвращаем True — исключение подавляется
        return False
    
    def query(self, sql):
        if not self.connection:
            raise RuntimeError("Нет соединения")
        return f"Результат запроса: {sql}"

# Использование
with DatabaseConnection("localhost") as db:
    print(db.query("SELECT * FROM users"))
    print(db.query("SELECT * FROM orders"))

print("Вне контекста")
```

**Output:**
```
Подключение к localhost
Результат запроса: SELECT * FROM users
Результат запроса: SELECT * FROM orders
Закрытие соединения с localhost
Вне контекста
```

### 6.3 Создание контекстного менеджера (декоратор)

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Контекстный менеджер для измерения времени."""
    start = time.time()
    print(f"{name} начат")
    try:
        yield  # Здесь выполняется тело with
    finally:
        elapsed = time.time() - start
        print(f"{name} завершён за {elapsed:.4f}с")

# Использование
with timer("Вычисление"):
    total = sum(range(1000000))
    print(f"Сумма: {total}")
```

**Output:**
```
Вычисление начат
Сумма: 499999500000
Вычисление завершён за 0.0312с
```

### 6.4 suppress — подавление исключений

```python
from contextlib import suppress

# Вместо:
try:
    import os
    os.remove("nonexistent.txt")
except FileNotFoundError:
    pass

# Можно написать:
with suppress(FileNotFoundError):
    import os
    os.remove("nonexistent.txt")

print("Программа продолжается")
```

**Output:**
```
Программа продолжается
```

---

## 7. Best Practices

### 7.1 Конкретные исключения

❌ **Плохо:**
```python
try:
    do_something()
except:  # Ловит ВСЁ, включая KeyboardInterrupt и SystemExit
    pass
```

❌ **Тоже плохо:**
```python
try:
    do_something()
except Exception:  # Слишком общее
    pass
```

✅ **Хорошо:**
```python
try:
    do_something()
except (ValueError, TypeError) as e:
    handle_error(e)
```

### 7.2 Не используйте исключения для управления потоком

❌ **Плохо:**
```python
def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
```

✅ **Лучше:**
```python
def get_item(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return None
```

### 7.3 EAFP vs LBYL

Python предпочитает EAFP (Easier to Ask for Forgiveness than Permission):

```python
# LBYL (Look Before You Leap) — проверка перед действием
# Менее Pythonic
if key in dictionary:
    value = dictionary[key]
else:
    value = default

# EAFP (Easier to Ask for Forgiveness) — попытка с обработкой ошибки
# Более Pythonic
try:
    value = dictionary[key]
except KeyError:
    value = default

# Ещё лучше — встроенный метод
value = dictionary.get(key, default)
```

### 7.4 Документируйте исключения

```python
def divide(a: float, b: float) -> float:
    """
    Делит a на b.
    
    Args:
        a: Делимое
        b: Делитель
    
    Returns:
        Результат деления
    
    Raises:
        TypeError: Если аргументы не числа
        ZeroDivisionError: Если b равно нулю
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Делитель не может быть нулём")
    return a / b
```

### 7.5 Логирование исключений

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError:
        logger.exception(f"Не удалось обработать данные: {data}")
        # .exception() автоматически добавляет traceback
        raise
```

---

## 8. Практические паттерны

### 8.1 Retry с экспоненциальной задержкой

```python
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """Повторяет функцию с экспоненциальной задержкой."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Попытка {attempt + 1} не удалась: {e}")
            print(f"Повтор через {delay:.2f}с")
            time.sleep(delay)

# Использование
def unreliable_operation():
    if random.random() < 0.7:
        raise ConnectionError("Сервер недоступен")
    return "Успех!"

try:
    result = retry_with_backoff(unreliable_operation)
    print(f"Результат: {result}")
except ConnectionError:
    print("Все попытки исчерпаны")
```

### 8.2 Null Object Pattern

```python
class NullUser:
    """Null Object — безопасная заглушка вместо None."""
    name = "Guest"
    email = ""
    
    def has_permission(self, permission):
        return False
    
    def __bool__(self):
        return False

def get_user(user_id):
    users = {1: {"name": "Alice", "email": "alice@example.com"}}
    data = users.get(user_id)
    
    if data:
        class User:
            def __init__(self, data):
                self.name = data["name"]
                self.email = data["email"]
            def has_permission(self, p):
                return True
            def __bool__(self):
                return True
        return User(data)
    
    return NullUser()

# Не нужно проверять на None
user = get_user(999)
print(f"Имя: {user.name}")
print(f"Есть доступ: {user.has_permission('admin')}")
```

**Output:**
```
Имя: Guest
Есть доступ: False
```

### 8.3 Graceful Degradation

```python
def get_data_with_fallback(primary_source, fallback_source, default=None):
    """Получает данные с fallback на альтернативный источник."""
    try:
        return primary_source()
    except Exception as e:
        print(f"Основной источник недоступен: {e}")
        try:
            return fallback_source()
        except Exception as e:
            print(f"Резервный источник недоступен: {e}")
            return default

# Пример
def fetch_from_api():
    raise ConnectionError("API недоступен")

def fetch_from_cache():
    return {"data": "cached"}

result = get_data_with_fallback(fetch_from_api, fetch_from_cache, {"data": "default"})
print(f"Результат: {result}")
```

**Output:**
```
Основной источник недоступен: API недоступен
Результат: {'data': 'cached'}
```

---

## 9. Common Pitfalls

### 9.1 Пустой except

❌ **Плохо:**
```python
try:
    do_something()
except:
    pass  # Молча проглатываем ВСЕ ошибки, включая Ctrl+C!
```

✅ **Правильно:**
```python
try:
    do_something()
except Exception as e:
    logger.error(f"Ошибка: {e}")
    # Или хотя бы:
    raise
```

### 9.2 Слишком широкий try

❌ **Плохо:**
```python
try:
    user = get_user(user_id)
    posts = get_posts(user)
    comments = get_comments(posts)
    send_email(user, posts, comments)
except Exception as e:
    print(f"Что-то пошло не так: {e}")  # Где именно?
```

✅ **Правильно:**
```python
try:
    user = get_user(user_id)
except UserNotFoundError:
    print("Пользователь не найден")
    return

try:
    posts = get_posts(user)
except DatabaseError:
    print("Ошибка базы данных при получении постов")
    return

# ... и так далее
```

### 9.3 Потеря информации об исключении

❌ **Плохо:**
```python
try:
    do_something()
except SomeError:
    raise AnotherError("Ошибка")  # Потеряли оригинальную ошибку
```

✅ **Правильно:**
```python
try:
    do_something()
except SomeError as e:
    raise AnotherError("Ошибка") from e  # Сохраняем цепочку
```

### 9.4 Использование assert в production

❌ **Плохо:**
```python
def transfer_money(amount):
    assert amount > 0, "Сумма должна быть положительной"  # Отключается с -O !
    # ...
```

✅ **Правильно:**
```python
def transfer_money(amount):
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    # ...
```

---

## 10. Отладка исключений

### 10.1 Получение traceback

```python
import traceback
import sys

def problematic_function():
    return 1 / 0

try:
    problematic_function()
except ZeroDivisionError:
    # Полный traceback в строку
    tb_str = traceback.format_exc()
    print("Traceback:")
    print(tb_str)
    
    # Или в поток
    print("\nОтправляем в stderr:")
    traceback.print_exc(file=sys.stderr)
```

**Output:**
```
Traceback:
Traceback (most recent call last):
  File "example.py", line 7, in <module>
    problematic_function()
  File "example.py", line 5, in problematic_function
    return 1 / 0
ZeroDivisionError: division by zero
```

### 10.2 Анализ исключения

```python
import sys

try:
    raise ValueError("Тестовая ошибка")
except ValueError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(f"Тип: {exc_type}")
    print(f"Значение: {exc_value}")
    print(f"Файл: {exc_tb.tb_frame.f_code.co_filename}")
    print(f"Строка: {exc_tb.tb_lineno}")
```

**Output:**
```
Тип: <class 'ValueError'>
Значение: Тестовая ошибка
Файл: example.py
Строка: 4
```

---

## 💡 Key Takeaways

- **Ловите конкретные исключения**: Никогда не используйте голый `except:`. Ловите только те ошибки, которые умеете обрабатывать.

- **finally гарантирует выполнение**: Используйте для очистки ресурсов. Ещё лучше — контекстные менеджеры (`with`).

- **Создавайте свои исключения**: Организуйте их в иерархию для вашей библиотеки/приложения.

- **raise from сохраняет контекст**: Всегда используйте `raise NewError() from original_error` для сохранения цепочки.

- **EAFP — Python-стиль**: "Проще попросить прощения, чем разрешения" — используйте try/except вместо проверок.

---

## 🚀 Next Steps

**Related Modules:**
- [Files](../08_Files/) — обработка ошибок при работе с файлами
- [Standard Modules](../09_StandardModules/) — модуль logging для исключений

**Practice Ideas:**
1. Создайте иерархию исключений для библиотеки интернет-магазина
2. Напишите декоратор @retry для автоматического повтора при ошибках
3. Реализуйте контекстный менеджер для подключения к базе данных
4. Создайте функцию валидации с детальными сообщениями об ошибках

**Going Deeper:**
- Изучите модуль `warnings` для предупреждений
- Познакомьтесь с `traceback` для анализа стека вызовов
- Изучите обработку исключений в асинхронном коде

---

## 📚 Additional Resources

**Documentation:**
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [contextlib](https://docs.python.org/3/library/contextlib.html)

**Articles:**
- [Python Exception Handling Best Practices](https://realpython.com/python-exceptions/)

---

