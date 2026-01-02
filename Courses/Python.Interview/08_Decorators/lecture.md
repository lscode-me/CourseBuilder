# Декораторы в Python

## Что нужно знать для интервью

Декораторы — обязательная тема Python-интервью. Вас попросят объяснить как работают декораторы и написать свой (обычно timing или memoization).

---

## 🔑 Ключевые понятия

### Что такое декоратор?

**Ответ на интервью:**
> "Декоратор — это функция, которая принимает функцию и возвращает новую функцию с изменённым поведением. Синтаксис `@decorator` — это просто сахар для `func = decorator(func)`."

### Декоратор без @

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

def say_hello():
    print("Hello!")

# Это:

say_hello = decorator(say_hello)

# Эквивалентно:

@decorator
def say_hello():
    print("Hello!")
```

---

## 💻 Код, который нужно уметь писать

### 1. Timing декоратор

```python
import time
from functools import wraps

def timing(func):
    @wraps(func)  # Сохраняет __name__, __doc__
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)

slow_function()  # slow_function took 1.0012s
```

### 2. Memoization декоратор

```python
from functools import wraps

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Мгновенно!
```

### 3. Встроенный lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 4. Декоратор с параметрами

```python
from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")  # Напечатает 3 раза
```

---

## ❓ Типичные вопросы на интервью

### Q: Зачем нужен @functools.wraps?

**A:**
> "Без `@wraps` wrapper-функция теряет метаданные оригинальной функции: `__name__`, `__doc__`, `__annotations__`. `@wraps(func)` копирует эти атрибуты."

```python
# Без @wraps

def deco(func):
    def wrapper():
        return func()
    return wrapper

@deco
def hello():
    """Says hello"""
    pass

print(hello.__name__)  # 'wrapper' — неправильно!
print(hello.__doc__)   # None — потеряна документация!
```

### Q: Как передать аргументы в декоратор?

**A:**
> "Нужен дополнительный уровень вложенности: внешняя функция принимает параметры и возвращает декоратор."

```python
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Arg: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args("hello")
def func():
    pass
```

### Q: Можно ли применить несколько декораторов?

**A:**
> "Да, декораторы применяются снизу вверх."

```python
@decorator1
@decorator2
@decorator3
def func():
    pass

# Эквивалентно:

func = decorator1(decorator2(decorator3(func)))
```

### Q: Как объяснить декораторы джуниору?

**A:**
> "Декоратор — это обёртка для функции. Представь, что у тебя есть подарок (функция), и ты заворачиваешь его в упаковку (декоратор). Упаковка может добавить бантик (логирование), измерить вес (timing) или запомнить, что уже дарили такой подарок (memoization)."

---

## 🎯 Применение декораторов

| Декоратор | Использование |
|-----------|---------------|
| `@timing` | Измерение времени выполнения |
| `@lru_cache` | Кэширование результатов |
| `@retry` | Повторные попытки при ошибках |
| `@login_required` | Проверка аутентификации |
| `@validate` | Валидация аргументов |
| `@log` | Логирование вызовов |

---

## 📚 Дополнительные материалы

- [Python docs: functools](https://docs.python.org/3/library/functools.html)
- [Real Python: Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- "Fluent Python" Chapter 7: Function Decorators and Closures

---



