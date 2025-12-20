# Библиотечные и runtime-протоколы
## File-like protocol, Iterator protocol, Context manager, Serialization

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Владеть Python на базовом уровне
- Понимать концепцию протокола (модуль 01)
- Иметь опыт работы с файлами и итераторами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять file-like protocol для работы с различными источниками данных
- Реализовывать iterator protocol для создания итерируемых объектов
- Использовать context manager protocol для управления ресурсами
- Понимать протоколы сериализации данных

---

## 1. Введение: протоколы в языках программирования

Языки программирования определяют **протоколы** — неформальные интерфейсы, которым должны следовать объекты для поддержки определённых операций. В Python эти протоколы часто основаны на "магических методах" (dunder methods).

**Примеры протоколов в Python:**

- File-like protocol: `read()`, `write()`, `close()`
- Iterator protocol: `__iter__()`, `__next__()`
- Context manager protocol: `__enter__()`, `__exit__()`
- Sequence protocol: `__len__()`, `__getitem__()`

Эти протоколы позволяют создавать объекты, которые ведут себя как встроенные типы, обеспечивая единообразное API.

---

## 2. File-like Protocol

### 2.1 Концепция

**File-like protocol** — объект, который ведёт себя как файл, поддерживая операции чтения и/или записи.

**Базовые методы:**
```python

read(size=-1)    # Читать size байт (-1 = всё)
write(data)      # Записать data
close()          # Закрыть файл
seek(pos)        # Переместиться на позицию
tell()           # Текущая позиция
```

### 2.2 Пример: StringIO

```python

from io import StringIO

# StringIO ведёт себя как файл, но работает с строкой в памяти
f = StringIO()
f.write("Hello, ")
f.write("World!")
f.seek(0)  # Вернуться в начало
print(f.read())  # "Hello, World!"
f.close()
```

**Output:**
```

Hello, World!
```

### 2.3 Применение

**Замена файлов в тестах:**
```python

def process_file(file_obj):
    data = file_obj.read()
    return data.upper()

# В продакшене: с реальным файлом
with open('data.txt') as f:
    result = process_file(f)

# В тестах: с StringIO
from io import StringIO
test_data = StringIO("test data")
result = process_file(test_data)
assert result == "TEST DATA"
```

**Работа с HTTP response как с файлом:**
```python

import requests
response = requests.get('https://example.com')
# response.raw ведёт себя как файл
data = response.raw.read(1024)
```

### 2.4 Реализация file-like объекта

```python

class UpperCaseFile:
    """File wrapper that converts text to uppercase"""
    
    def __init__(self, file_obj):
        self.file = file_obj
    
    def read(self, size=-1):
        data = self.file.read(size)
        return data.upper()
    
    def write(self, data):
        return self.file.write(data.upper())
    
    def close(self):
        return self.file.close()

# Использование
from io import StringIO
f = UpperCaseFile(StringIO())
f.write("hello")
f.file.seek(0)
print(f.read())  # "HELLO"
```

**Output:**
```

HELLO
```

---

## 3. Iterator Protocol

### 3.1 Концепция

**Iterator protocol** позволяет объектам быть итерируемыми (использоваться в `for` циклах).

**Два метода:**
```python

__iter__()    # Возвращает итератор (обычно self)
__next__()    # Возвращает следующий элемент или StopIteration
```

### 3.2 Простой итератор

```python

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Использование
for num in Counter(0, 5):
    print(num, end=' ')
```

**Output:**
```

0 1 2 3 4 
```

### 3.3 Iterable vs Iterator

**Iterable** — объект, который возвращает итератор из `__iter__()`
**Iterator** — объект с `__iter__()` и `__next__()`

```python

class NumberRange:
    """Iterable (не iterator)"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return NumberRangeIterator(self.start, self.end)

class NumberRangeIterator:
    """Iterator"""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Можно использовать несколько раз
numbers = NumberRange(0, 3)
print(list(numbers))  # [0, 1, 2]
print(list(numbers))  # [0, 1, 2] — работает снова
```

**Output:**
```

[0, 1, 2]
[0, 1, 2]
```

### 3.4 Генераторы

**Генераторы** — простой способ создания итераторов через `yield`:

```python

def counter(start, end):
    current = start
    while current < end:
        yield current
        current += 1

for num in counter(0, 5):
    print(num, end=' ')
```

**Output:**
```

0 1 2 3 4 
```

---

## 4. Context Manager Protocol

### 4.1 Концепция

**Context manager** обеспечивает автоматическое управление ресурсами через `with` statement.

**Два метода:**
```python

__enter__()         # Вход в контекст (возвращает ресурс)
__exit__(exc_type, exc_val, exc_tb)  # Выход из контекста (cleanup)
```

### 4.2 Базовый пример

```python

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Возвращаем False, чтобы не подавлять исключения
        return False

# Использование
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# Файл автоматически закрыт

```

### 4.3 Обработка ошибок

```python

class ErrorHandlingContext:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            # Возвращаем True, чтобы подавить исключение
            return True
        print("Exiting context normally")
        return False

with ErrorHandlingContext():
    print("Inside context")
    raise ValueError("Test error")
print("After context")  # Выполнится, т.к. исключение подавлено
```

**Output:**
```

Entering context
Inside context
Exception occurred: ValueError: Test error
After context
```

### 4.4 contextlib

Python предоставляет `contextlib` для упрощения создания context managers:

```python

from contextlib import contextmanager

@contextmanager
def managed_resource():
    # Setup
    resource = acquire_resource()
    try:
        yield resource  # Передаём ресурс в with block
    finally:
        # Cleanup
        release_resource(resource)

# Использование
with managed_resource() as res:
    use_resource(res)
```

---

## 5. Serialization Protocols

### 5.1 Концепция

**Сериализация** — преобразование объекта в формат для хранения или передачи.

**Популярные протоколы:**

- JSON — текстовый, читаемый, универсальный
- Pickle — бинарный, Python-специфичный
- Protocol Buffers — бинарный, эффективный
- MessagePack — бинарный, компактный

### 5.2 JSON serialization

```python

import json

# Базовая сериализация
data = {"name": "John", "age": 30, "is_active": True}
json_str = json.dumps(data)
print(json_str)

# Десериализация
data_back = json.loads(json_str)
print(data_back)
```

**Output:**
```

{"name": "John", "age": 30, "is_active": true}
{'name': 'John', 'age': 30, 'is_active': True}
```

### 5.3 Кастомная сериализация

```python

import json
from datetime import datetime

class User:
    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'name': obj.name,
                'created_at': obj.created_at.isoformat()
            }
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

user = User("Alice", datetime(2024, 1, 15))
json_str = json.dumps(user, cls=UserEncoder)
print(json_str)
```

**Output:**
```

{"name": "Alice", "created_at": "2024-01-15T00:00:00"}
```

### 5.4 Pickle protocol

```python

import pickle

data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}

# Сериализация
pickled = pickle.dumps(data)
print(f"Pickled size: {len(pickled)} bytes")

# Десериализация
data_back = pickle.loads(pickled)
print(data_back)
```

**Output:**
```

Pickled size: 67 bytes
{'users': [{'name': 'Alice'}, {'name': 'Bob'}]}
```

---

## 6. Sequence Protocol

### 6.1 Концепция

**Sequence protocol** позволяет объектам вести себя как последовательности (списки, кортежи).

**Методы:**
```python

__len__()           # Длина последовательности
__getitem__(index)  # Получение элемента по индексу
__setitem__(index, value)  # Установка элемента
__delitem__(index)  # Удаление элемента
__contains__(item)  # Проверка наличия (in)
```

### 6.2 Пример

```python

class CircularList:
    def __init__(self, items):
        self.items = list(items)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        # Циклический доступ
        return self.items[index % len(self.items)]
    
    def __setitem__(self, index, value):
        self.items[index % len(self.items)] = value

# Использование
cl = CircularList([1, 2, 3])
print(cl[0])   # 1
print(cl[3])   # 1 (циклический)
print(cl[5])   # 3
print(len(cl)) # 3
```

**Output:**
```

1
1
3
3
```

---

## 7. Descriptor Protocol

### 7.1 Концепция

**Descriptor protocol** управляет доступом к атрибутам объекта.

**Методы:**
```python

__get__(self, obj, type=None)
__set__(self, obj, value)
__delete__(self, obj)
```

### 7.2 Пример: валидация

```python

class PositiveNumber:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Product:
    price = PositiveNumber('price')
    quantity = PositiveNumber('quantity')
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Использование
p = Product("Apple", 10, 5)
print(p.price)  # 10
# p.price = -5  # ValueError: price must be positive

```

**Output:**
```

10
```

---

## 💡 Key Takeaways

- **File-like protocol унифицирует работу с данными**: Объекты, поддерживающие `read()`, `write()`, `close()`, могут использоваться взаимозаменяемо с файлами, упрощая тестирование и абстракцию.

- **Iterator protocol для кастомных итераций**: Реализация `__iter__()` и `__next__()` позволяет создавать объекты, работающие в `for` циклах. Генераторы упрощают создание итераторов.

- **Context manager для управления ресурсами**: Протокол `__enter__()`/`__exit__()` обеспечивает автоматическое освобождение ресурсов, предотвращая утечки.

- **Протоколы сериализации для хранения и передачи**: JSON для читаемости и совместимости, Pickle для Python-объектов, Protocol Buffers для производительности. Выбор зависит от требований.

- **Протоколы создают единообразные API**: Следование протоколам позволяет создавать объекты, которые ведут себя как встроенные типы, упрощая их использование.

---

## 🚀 Next Steps

**Related Modules:**

- [10_OOP_Contract_Protocols](../10_OOP_Contract_Protocols/) — ООП и контрактные протоколы: интерфейсы, duck typing, LSP
- [13_UTF8_As_Protocol](../13_UTF8_As_Protocol/) — UTF-8 как протокол интерпретации данных

**Practice Ideas:**

1. Реализуйте file-like объект, который логирует все операции чтения/записи
2. Создайте итератор для обхода дерева или графа
3. Реализуйте context manager для управления подключением к базе данных

**Going Deeper:**

- Изучите async iterator protocol (`__aiter__`, `__anext__`) для асинхронных итераций
- Изучите typing.Protocol в Python 3.8+ для структурной типизации
- Изучите dataclasses и pydantic для автоматической сериализации

---


