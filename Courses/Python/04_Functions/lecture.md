# Python Functions
## Функции, параметры, возвращаемые значения и лямбды

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые типы данных Python
- Знать управляющие конструкции (if, for, while)
- Уметь работать с коллекциями (списки, словари)
- Понимать концепцию области видимости (scope)

**Recommended prior modules:**

- [Flow Control](../03_FlowControl/) — условия и циклы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать функции с различными типами параметров
- Использовать *args и **kwargs для гибкой передачи аргументов
- Применять декораторы для модификации поведения функций
- Создавать лямбда-функции для коротких операций
- Понимать области видимости и замыкания

---

## 1. Введение в функции

Функции — это именованные блоки кода, которые выполняют определённую задачу. Они позволяют организовать код, избежать повторений и сделать программу модульной.

### 1.1 Зачем нужны функции

```python
# Без функций — код повторяется

print("=" * 40)
print("Отчёт за январь")
print("=" * 40)

print("=" * 40)
print("Отчёт за февраль")
print("=" * 40)

# С функцией — код переиспользуется

def print_header(title):
    print("=" * 40)
    print(title)
    print("=" * 40)

print_header("Отчёт за январь")
print_header("Отчёт за февраль")
```

**Output:**
```
========================================
Отчёт за январь
========================================
========================================
Отчёт за февраль
========================================
========================================
Отчёт за январь
========================================
========================================
Отчёт за февраль
========================================
```

### 1.2 Определение функции

```python
def greet(name):
    """
    Приветствует пользователя по имени.
    
    Args:
        name: Имя пользователя
    
    Returns:
        Строка приветствия
    """
    return f"Привет, {name}!"

# Вызов функции

message = greet("Alice")
print(message)

# Доступ к документации

print(greet.__doc__)
```

**Output:**
```
Привет, Alice!

    Приветствует пользователя по имени.
    
    Args:
        name: Имя пользователя
    
    Returns:
        Строка приветствия
```

Структура функции:

- `def` — ключевое слово
- `greet` — имя функции
- `(name)` — параметры
- `"""..."""` — docstring (документация)
- `return` — возвращаемое значение

### 1.3 Функция без return

Если функция не содержит return, она возвращает `None`:

```python
def print_info(message):
    print(f"[INFO] {message}")
    # Нет return — вернёт None

result = print_info("Программа запущена")
print(f"result = {result}")
```

**Output:**
```
[INFO] Программа запущена
result = None
```

### 1.4 Множественные return

Функция может иметь несколько точек выхода:

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(85))  # B
print(get_grade(72))  # C
```

**Output:**
```
B
C
```

---

## 2. Параметры функций

### 2.1 Позиционные параметры

```python
def describe_pet(animal_type, pet_name):
    """Описывает питомца."""
    print(f"У меня есть {animal_type} по имени {pet_name}")

# Позиционные аргументы — порядок важен

describe_pet("кот", "Барсик")
describe_pet("собака", "Шарик")
```

**Output:**
```
У меня есть кот по имени Барсик
У меня есть собака по имени Шарик
```

### 2.2 Именованные аргументы

```python
def describe_pet(animal_type, pet_name):
    print(f"У меня есть {animal_type} по имени {pet_name}")

# Именованные аргументы — порядок не важен

describe_pet(pet_name="Мурка", animal_type="кошка")

# Смешивание (позиционные должны идти первыми)

describe_pet("хомяк", pet_name="Пушок")
```

**Output:**
```
У меня есть кошка по имени Мурка
У меня есть хомяк по имени Пушок
```

### 2.3 Параметры по умолчанию

```python
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                    # Использует значение по умолчанию
print(greet("Bob", "Здравствуй"))        # Переопределяет значение
print(greet("Charlie", greeting="Hi"))   # Именованный аргумент
```

**Output:**
```
Привет, Alice!
Здравствуй, Bob!
Hi, Charlie!
```

> **⚠️ Warning:**  
> Никогда не используйте изменяемые объекты как значения по умолчанию!

```python
# ПЛОХО — изменяемый default

def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("a"))  # ['a']
print(add_item_bad("b"))  # ['a', 'b'] — неожиданно!

# ХОРОШО — None как default

def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_good("a"))  # ['a']
print(add_item_good("b"))  # ['b'] — правильно!
```

**Output:**
```
['a']
['a', 'b']
['a']
['b']
```

### 2.4 Только позиционные и только именованные параметры

Python 3.8+ позволяет указать, как должны передаваться аргументы:

```python
# / — всё до него только позиционно
# * — всё после него только именованно

def function(pos_only, /, standard, *, kw_only):
    print(f"pos_only={pos_only}, standard={standard}, kw_only={kw_only}")

# Правильные вызовы

function(1, 2, kw_only=3)
function(1, standard=2, kw_only=3)

# Ошибки:
# function(pos_only=1, standard=2, kw_only=3)  # TypeError
# function(1, 2, 3)  # TypeError
```

**Output:**
```
pos_only=1, standard=2, kw_only=3
pos_only=1, standard=2, kw_only=3
```

---

## 3. *args и **kwargs

### 3.1 *args — произвольное число позиционных аргументов

```python
def sum_all(*numbers):
    """Суммирует все переданные числа."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all())
```

**Output:**
```
6
15
0
```

```python
def print_args(first, *rest):
    """Первый аргумент отдельно, остальные в кортеже."""
    print(f"First: {first}")
    print(f"Rest: {rest}")

print_args("a", "b", "c", "d")
```

**Output:**
```
First: a
Rest: ('b', 'c', 'd')
```

### 3.2 **kwargs — произвольное число именованных аргументов

```python
def print_info(**kwargs):
    """Печатает все переданные именованные аргументы."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Moscow")
```

**Output:**
```
name: Alice
age: 30
city: Moscow
```

### 3.3 Комбинирование *args и **kwargs

```python
def universal_function(*args, **kwargs):
    """Принимает любые аргументы."""
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

universal_function(1, 2, 3, name="Alice", age=30)
```

**Output:**
```
args: (1, 2, 3)
kwargs: {'name': 'Alice', 'age': 30}
```

**Порядок параметров:**

```python
def example(pos1, pos2, *args, kw1=None, kw2=None, **kwargs):
    print(f"pos1={pos1}, pos2={pos2}")
    print(f"args={args}")
    print(f"kw1={kw1}, kw2={kw2}")
    print(f"kwargs={kwargs}")

example(1, 2, 3, 4, kw1="a", kw2="b", extra1="x", extra2="y")
```

**Output:**
```
pos1=1, pos2=2
args=(3, 4)
kw1=a, kw2=b
kwargs={'extra1': 'x', 'extra2': 'y'}
```

### 3.4 Распаковка при вызове

```python
def greet(name, greeting, punctuation):
    return f"{greeting}, {name}{punctuation}"

# Распаковка списка/кортежа с *

args = ["Alice", "Hello", "!"]
print(greet(*args))

# Распаковка словаря с **

kwargs = {"name": "Bob", "greeting": "Hi", "punctuation": "?"}
print(greet(**kwargs))

# Комбинирование

print(greet("Charlie", **{"greeting": "Hey", "punctuation": "..."}))
```

**Output:**
```
Hello, Alice!
Hi, Bob?
Hey, Charlie...
```

---

## 4. Возвращаемые значения

### 4.1 Возврат нескольких значений

```python
def get_min_max(numbers):
    """Возвращает минимум и максимум списка."""
    return min(numbers), max(numbers)

# Возвращается кортеж

result = get_min_max([5, 2, 8, 1, 9])
print(f"result: {result}")
print(f"type: {type(result)}")

# Распаковка

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"min: {minimum}, max: {maximum}")
```

**Output:**
```
result: (1, 9)
type: <class 'tuple'>
min: 1, max: 9
```

### 4.2 Возврат словаря

```python
def analyze_text(text):
    """Анализирует текст и возвращает статистику."""
    words = text.split()
    return {
        "char_count": len(text),
        "word_count": len(words),
        "avg_word_length": sum(len(w) for w in words) / len(words) if words else 0
    }

stats = analyze_text("Python is a great programming language")
print(stats)
print(f"Слов: {stats['word_count']}")
```

**Output:**
```
{'char_count': 38, 'word_count': 6, 'avg_word_length': 5.333333333333333}
Слов: 6
```

### 4.3 Возврат функции

Функции могут возвращать другие функции:

```python
def create_multiplier(factor):
    """Создаёт функцию-множитель."""
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
```

**Output:**
```
double(5) = 10
triple(5) = 15
```

---

## 5. Области видимости (Scope)

### 5.1 Правило LEGB

Python ищет переменные в порядке LEGB:

- **L**ocal — локальные переменные функции

- **E**nclosing — переменные внешних функций (замыкания)

- **G**lobal — глобальные переменные модуля

- **B**uilt-in — встроенные имена Python

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"inner: {x}")
    
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")
```

**Output:**
```
inner: local
outer: enclosing
global: global
```

### 5.2 global и nonlocal

```python
counter = 0

def increment():
    global counter  # Используем глобальную переменную
    counter += 1
    return counter

print(increment())  # 1
print(increment())  # 2
print(f"counter = {counter}")
```

**Output:**
```
1
2
counter = 2
```

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Используем переменную из enclosing scope
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

**Output:**
```
1
2
3
```

> **💡 Pro Tip:**  
> Избегайте global когда возможно. Лучше передавать данные через параметры и возвращаемые значения.

---

## 6. Лямбда-функции

### 6.1 Синтаксис

Лямбда-функции — анонимные функции для коротких операций:

```python
# Обычная функция

def square(x):
    return x ** 2

# Эквивалентная лямбда

square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))
```

**Output:**
```
25
25
```

### 6.2 Использование с функциями высшего порядка

```python
numbers = [1, 2, 3, 4, 5]

# map — применить функцию к каждому элементу

squared = list(map(lambda x: x ** 2, numbers))
print(f"squared: {squared}")

# filter — отфильтровать элементы

even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"even: {even}")

# sorted — сортировка с ключом

words = ["banana", "Apple", "cherry"]
sorted_words = sorted(words, key=lambda s: s.lower())
print(f"sorted: {sorted_words}")
```

**Output:**
```
squared: [1, 4, 9, 16, 25]
even: [2, 4]
sorted: ['Apple', 'banana', 'cherry']
```

### 6.3 Практические примеры

```python
# Сортировка списка словарей

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# По возрасту

by_age = sorted(users, key=lambda u: u["age"])
print("По возрасту:", [u["name"] for u in by_age])

# По имени (обратный порядок)

by_name_desc = sorted(users, key=lambda u: u["name"], reverse=True)
print("По имени (desc):", [u["name"] for u in by_name_desc])
```

**Output:**
```
По возрасту: ['Bob', 'Alice', 'Charlie']
По имени (desc): ['Charlie', 'Bob', 'Alice']
```

> **⚠️ Warning:**  
> Лямбды должны быть простыми. Если логика сложная — используйте обычную функцию.

```python
# ПЛОХО — сложная лямбда
# sorted(items, key=lambda x: (x.split()[0], -int(x.split()[1]) if x.split()[1].isdigit() else 0))

# ХОРОШО — обычная функция

def sort_key(x):
    parts = x.split()
    name = parts[0]
    number = -int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    return (name, number)

items = ["Alice 30", "Bob 25", "Alice 20"]
print(sorted(items, key=sort_key))
```

**Output:**
```
['Alice 30', 'Alice 20', 'Bob 25']
```

---

## 7. Декораторы

### 7.1 Что такое декоратор

Декоратор — функция, которая модифицирует поведение другой функции:

```python
def my_decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
До вызова функции
Hello!
После вызова функции
```

Это эквивалентно:

```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```

### 7.2 Декораторы с аргументами функции

```python
import functools

def log_call(func):
    @functools.wraps(func)  # Сохраняет метаданные функции
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    """Складывает два числа."""
    return a + b

result = add(3, 5)
print(f"add.__name__: {add.__name__}")
print(f"add.__doc__: {add.__doc__}")
```

**Output:**
```
Вызов add((3, 5), {})
Результат: 8
add.__name__: add
add.__doc__: Складывает два числа.
```

### 7.3 Практические декораторы

**Измерение времени:**

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнилась за {end - start:.4f}с")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"

result = slow_function()
```

**Output:**
```
slow_function выполнилась за 0.1003с
```

**Кэширование:**

```python
import functools

def cache(func):
    """Простой кэширующий декоратор."""
    cached = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Без кэша было бы очень медленно

print(f"fib(30) = {fibonacci(30)}")
print(f"fib(35) = {fibonacci(35)}")
```

**Output:**
```
fib(30) = 832040
fib(35) = 9227465
```

> **💡 Pro Tip:**  
> Python предоставляет встроенный `@functools.lru_cache` для кэширования.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fib(100) = {fibonacci(100)}")
```

**Output:**
```
fib(100) = 354224848179261915075
```

### 7.4 Декораторы с параметрами

```python
import functools

def repeat(times):
    """Декоратор, повторяющий вызов функции."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```

**Output:**
```
Hello, World!
Hello, World!
Hello, World!
```

---

## 8. Генераторы

### 8.1 Функции-генераторы

Генераторы создают значения "лениво" — по мере необходимости:

```python
def count_up_to(max_value):
    """Генератор чисел от 1 до max_value."""
    count = 1
    while count <= max_value:
        yield count  # Приостанавливает и возвращает значение
        count += 1

# Итерация по генератору

for num in count_up_to(5):
    print(num, end=" ")
print()

# Создание списка из генератора

numbers = list(count_up_to(5))
print(numbers)
```

**Output:**
```
1 2 3 4 5 
[1, 2, 3, 4, 5]
```

### 8.2 Преимущества генераторов

```python
import sys

# Список — занимает много памяти

big_list = [x ** 2 for x in range(1000000)]
print(f"Размер списка: {sys.getsizeof(big_list):,} bytes")

# Генератор — почти не занимает памяти

big_gen = (x ** 2 for x in range(1000000))
print(f"Размер генератора: {sys.getsizeof(big_gen):,} bytes")
```

**Output:**
```
Размер списка: 8,448,728 bytes
Размер генератора: 200 bytes
```

### 8.3 Практический пример

```python
def read_large_file(file_path):
    """Читает большой файл построчно."""
    with open(file_path) as f:
        for line in f:
            yield line.strip()

def process_log_lines(lines):
    """Фильтрует строки с ошибками."""
    for line in lines:
        if "ERROR" in line:
            yield line

# Пример использования (если бы был файл)
# for error in process_log_lines(read_large_file("app.log")):
#     print(error)

# Демонстрация на списке

sample_logs = [
    "INFO: Started",
    "ERROR: Connection failed",
    "INFO: Retrying",
    "ERROR: Timeout",
    "INFO: Success"
]

for error in process_log_lines(sample_logs):
    print(f"Found: {error}")
```

**Output:**
```
Found: ERROR: Connection failed
Found: ERROR: Timeout
```

### 8.4 yield from

```python
def flatten(nested):
    """Разворачивает вложенные списки."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Делегирует генерацию
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested)))
```

**Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 9. Аннотации типов

### 9.1 Базовые аннотации

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Аннотации не проверяются во время выполнения!

print(greet(123))  # Работает, но IDE предупредит
print(add("a", "b"))  # Работает, но это плохо
```

**Output:**
```
Hello, 123!
ab
```

### 9.2 Optional и Union

```python
from typing import Optional, Union

def find_user(user_id: int) -> Optional[dict]:
    """Возвращает пользователя или None."""
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)

def process_value(value: Union[int, str]) -> str:
    """Принимает int или str."""
    return str(value)

# Python 3.10+: Optional[X] = X | None

def find_user_new(user_id: int) -> dict | None:
    users = {1: {"name": "Alice"}}
    return users.get(user_id)

print(find_user(1))
print(find_user(99))
print(process_value(42))
print(process_value("hello"))
```

**Output:**
```
{'name': 'Alice'}
None
42
hello
```

### 9.3 Callable и другие типы

```python
from typing import Callable, Iterable

def apply_to_all(
    items: Iterable[int],
    func: Callable[[int], int]
) -> list[int]:
    """Применяет функцию к каждому элементу."""
    return [func(item) for item in items]

result = apply_to_all([1, 2, 3], lambda x: x ** 2)
print(result)
```

**Output:**
```
[1, 4, 9]
```

---

## 10. Common Pitfalls

### 10.1 Изменяемый default

❌ **Ошибка:**
```python
def append_to(item, lst=[]):
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] — неожиданно!
```

✅ **Правильно:**
```python
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [2]
```

**Output:**
```
[1]
[1, 2]
[1]
[2]
```

### 10.2 Поздняя привязка в замыканиях

❌ **Ошибка:**
```python
# Все функции возвращают 4!

funcs = []
for i in range(5):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [4, 4, 4, 4, 4]
```

✅ **Правильно:**
```python
# Захватываем значение i

funcs = []
for i in range(5):
    funcs.append(lambda i=i: i)  # i=i — захват текущего значения

print([f() for f in funcs])  # [0, 1, 2, 3, 4]
```

**Output:**
```
[4, 4, 4, 4, 4]
[0, 1, 2, 3, 4]
```

### 10.3 Забытый return

❌ **Ошибка:**
```python
def double(x):
    result = x * 2
    # Забыли return!

print(double(5))  # None
```

✅ **Правильно:**
```python
def double(x):
    return x * 2

print(double(5))  # 10
```

### 10.4 Слишком много параметров

❌ **Плохо:**
```python
def create_user(name, email, age, city, country, zip_code, phone, company):
    ...
```

✅ **Лучше:**
```python
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    country: str
    zip_code: str

@dataclass
class UserData:
    name: str
    email: str
    age: int
    address: Address
    phone: str
    company: str

def create_user(data: UserData):
    ...
```

---

## 💡 Key Takeaways

- **Функции — основа организации кода**: Используйте их для переиспользования и модульности. Одна функция — одна задача.

- **Параметры гибкие**: Используйте default values, *args, **kwargs для гибкости, но не злоупотребляйте.

- **Декораторы — мощный инструмент**: Позволяют модифицировать поведение функций без изменения их кода.

- **Генераторы экономят память**: Используйте yield для работы с большими данными.

- **Аннотации типов улучшают код**: Они не проверяются в runtime, но помогают IDE и читателям кода.

---

## 🚀 Next Steps

**Related Modules:**

- [Classes](../05_Classes/) — создание классов и ООП
- [Modules](../06_Modules/) — организация кода в модули

**Practice Ideas:**

1. Напишите декоратор для валидации аргументов функции
2. Создайте генератор для чисел Фибоначчи
3. Реализуйте функцию retry с параметрами (количество попыток, задержка)
4. Напишите функцию-мемоизатор с ограничением размера кэша

**Going Deeper:**

- Изучите модуль `functools` (partial, reduce, wraps)
- Познакомьтесь с `itertools` для работы с итераторами
- Изучите асинхронные функции (async/await)

---

## 📚 Additional Resources

**Documentation:**

- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [functools](https://docs.python.org/3/library/functools.html)
- [typing](https://docs.python.org/3/library/typing.html)

**PEPs:**

- [PEP 484](https://peps.python.org/pep-0484/) — Type Hints
- [PEP 318](https://peps.python.org/pep-0318/) — Decorators

---





