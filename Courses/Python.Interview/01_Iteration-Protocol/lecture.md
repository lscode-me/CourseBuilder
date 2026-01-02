# Протокол итерации в Python

## Что нужно знать для интервью

Протокол итерации — одна из базовых тем Python-интервью. Вас могут попросить объяснить разницу между iterable, iterator и generator, а также написать генератор (например, Fibonacci).

---

## 🔑 Ключевые понятия

### Iterable vs Iterator vs Generator

| Тип | Методы | Описание |
|-----|--------|----------|
| **Iterable** | `__iter__()` | Объект, по которому можно итерироваться (list, str, dict) |
| **Iterator** | `__iter__()` + `__next__()` | Объект, который помнит позицию в итерации |
| **Generator** | Iterator + `yield` | Специальный итератор, созданный через функцию с `yield` |

**Ответ на интервью:**
> "Iterable — это любой объект с методом `__iter__()`, который возвращает iterator. Iterator — это объект с методами `__iter__()` и `__next__()`. Generator — это iterator, созданный через функцию с `yield` или generator expression."

### Важно: `range()` — это НЕ итератор!

```python
>>> r = range(5)
>>> next(r)  # TypeError: 'range' object is not an iterator
>>> it = iter(r)
>>> next(it)  # 0 — работает
```

`range()` — это iterable, но не iterator. Нужно вызвать `iter()` для получения итератора.

---

## 💻 Код, который нужно уметь писать

### 1. Генератор чисел Фибоначчи

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Использование

fib = fibonacci()
print([next(fib) for _ in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 2. Функция index через next() и enumerate()

```python
def index(iterable, element):
    return next((i for i, e in enumerate(iterable) if e == element), -1)

# Однострочник (lambda)

index = lambda it, el: next(i for i, e in enumerate(it) if e == el)
```

### 3. Класс iter_int — итерируемое целое число

```python
class iter_int(int):
    def __iter__(self):
        return iter(range(self))

# Использование

print(list(iter_int(4)))  # [0, 1, 2, 3]
print(iter_int(4) + 2)    # 6
```

### 4. Переписать for через while

```python
# for c in "hello": print(c)

it = iter("hello")
while True:
    try:
        c = next(it)
        print(c)
    except StopIteration:
        break
```

---

## ❓ Типичные вопросы на интервью

### Q: Сколько аргументов принимают iter() и next()?

**A:** 

- `iter(obj)` — один аргумент (iterable)
- `iter(callable, sentinel)` — два аргумента (вызывает callable пока не получит sentinel)
- `next(iterator)` — один аргумент
- `next(iterator, default)` — два аргумента (возвращает default вместо StopIteration)

### Q: В чём разница между list comprehension и generator expression?

```python
# List comprehension — создаёт список сразу

squares_list = [x**2 for x in range(1000000)]  # Занимает память

# Generator expression — вычисляет лениво

squares_gen = (x**2 for x in range(1000000))  # Почти не занимает память
```

### Q: Что выведет этот код?

```python
for i in [lambda x: x**y for y in range(5)]: print(i(2))
for i in (lambda x: x**y for y in range(5)): print(i(2))
```

**A:**

- Первый цикл: `16 16 16 16 16` — все lambda захватывают **последнее** значение y=4
- Второй цикл: `1 2 4 8 16` — generator вычисляет лениво, y разный каждый раз

**Это ловушка closure!** В list comprehension все lambda создаются сразу с одной ссылкой на y.

---

## 🧩 Live Coding: merge_iterator

Напишите функцию, которая сливает два отсортированных итератора:

```python
def merge_sorted(iter1, iter2):
    val1 = next(iter1, None)
    val2 = next(iter2, None)
    
    while val1 is not None or val2 is not None:
        if val2 is None or (val1 is not None and val1 <= val2):
            yield val1
            val1 = next(iter1, None)
        else:
            yield val2
            val2 = next(iter2, None)

# Тест

list(merge_sorted(iter([1, 3, 5]), iter([2, 4, 6])))
# [1, 2, 3, 4, 5, 6]
```

---

## 📚 Дополнительные материалы

- [Python docs: Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Real Python: Python Generators](https://realpython.com/introduction-to-python-generators/)
- "Fluent Python" Chapter 14: Iterables, Iterators, and Generators

---



