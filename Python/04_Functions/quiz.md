# Python Functions - Quiz

Проверьте свои знания по теме "Функции, параметры, возвращаемые значения и лямбды".

---

## Question 1: Определение функции

Какое ключевое слово используется для определения функции?

A) `function`

B) `func`

C) `def`

D) `define`

---

## Question 2: Возвращаемое значение

Что вернёт функция без оператора return?

A) 0

B) False

C) None

D) Error

---

## Question 3: Позиционные аргументы

Что выведет следующий код?

```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

print(greet("Hello", "World"))
```

A) Hello, World!

B) World, Hello!

C) greeting, name!

D) Error

---

## Question 4: Именованные аргументы

Что выведет следующий код?

```python
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"

print(greet(greeting="Hello", name="Alice"))
```

A) Hi, Alice!

B) Hello, Alice!

C) Alice, Hello!

D) Error

---

## Question 5: Значения по умолчанию

Почему этот код работает неправильно?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

A) Синтаксическая ошибка

B) Список по умолчанию создаётся один раз

C) append() не работает

D) Код работает правильно

---

## Question 6: *args

Что выведет следующий код?

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))
```

A) (1, 2, 3, 4)

B) 10

C) [1, 2, 3, 4]

D) Error

---

## Question 7: **kwargs

Какой тип данных получает функция через **kwargs?

A) tuple

B) list

C) dict

D) set

---

## Question 8: Порядок параметров

Какой порядок параметров правильный?

A) `def f(*args, pos, **kwargs):`

B) `def f(pos, *args, **kwargs):`

C) `def f(**kwargs, *args, pos):`

D) `def f(pos, **kwargs, *args):`

---

## Question 9: Распаковка аргументов

Что выведет следующий код?

```python
def add(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(add(*args))
```

A) [1, 2, 3]

B) 6

C) (1, 2, 3)

D) Error

---

## Question 10: Область видимости

Что такое правило LEGB?

A) Порядок выполнения кода

B) Порядок поиска переменных: Local, Enclosing, Global, Built-in

C) Способ передачи аргументов

D) Метод оптимизации функций

---

## Question 11: global

Что делает ключевое слово `global`?

A) Создаёт новую глобальную переменную

B) Позволяет изменять глобальную переменную внутри функции

C) Импортирует переменную из другого модуля

D) Делает переменную доступной везде автоматически

---

## Question 12: Lambda функции

Какой синтаксис правильный для lambda?

A) `lambda(x): x * 2`

B) `lambda x: x * 2`

C) `def lambda(x): return x * 2`

D) `x => x * 2`

---

## Question 13: Lambda с filter

Что выведет следующий код?

```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, nums))
print(result)
```

A) [1, 2]

B) [3, 4, 5]

C) [True, True, True]

D) 3

---

## Question 14: Lambda с map

Что выведет следующий код?

```python
nums = [1, 2, 3]
result = list(map(lambda x: x ** 2, nums))
print(result)
```

A) [1, 2, 3]

B) [1, 4, 9]

C) 6

D) [2, 4, 6]

---

## Question 15: Декораторы

Что такое декоратор?

A) Комментарий для документации

B) Функция, модифицирующая поведение другой функции

C) Способ форматирования вывода

D) Встроенная функция Python

---

## Question 16: Синтаксис декоратора

Что эквивалентно `@decorator` перед функцией?

A) `func = decorator + func`

B) `func = decorator(func)`

C) `decorator.func = func`

D) `func.decorator = decorator`

---

## Question 17: functools.wraps

Зачем использовать `@functools.wraps` в декораторе?

A) Для ускорения выполнения

B) Для сохранения метаданных оригинальной функции

C) Для создания копии функции

D) Для добавления документации

---

## Question 18: Генераторы

Какое ключевое слово создаёт генератор?

A) `return`

B) `yield`

C) `generate`

D) `iter`

---

## Question 19: Преимущество генераторов

В чём главное преимущество генераторов?

A) Работают быстрее обычных функций

B) Экономят память при работе с большими данными

C) Проще в написании

D) Поддерживают больше операций

---

## Question 20: lru_cache

Что делает декоратор `@functools.lru_cache`?

A) Ограничивает время выполнения функции

B) Кэширует результаты вызовов функции

C) Логирует вызовы функции

D) Делает функцию асинхронной

---

## Question 21: Аннотации типов

Какая аннотация правильная для функции?

A) `def add(a, b) -> returns int:`

B) `def add(a: int, b: int) -> int:`

C) `def add(a int, b int) int:`

D) `def add<int>(a, b):`

---

## Question 22: Замыкание

Что выведет следующий код?

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))
```

A) 5

B) 3

C) 8

D) Error

---

## Question 23: Множественные return

Что выведет следующий код?

```python
def minmax(numbers):
    return min(numbers), max(numbers)

result = minmax([3, 1, 4, 1, 5])
print(type(result).__name__)
```

A) list

B) tuple

C) int

D) dict

---

## Question 24: Docstring

Как получить docstring функции?

A) `func.doc`

B) `func.__doc__`

C) `getdoc(func)`

D) `func.docstring`

---

## Question 25: partial

Что делает `functools.partial`?

A) Частично выполняет функцию

B) Создаёт новую функцию с заранее заданными аргументами

C) Разделяет функцию на части

D) Проверяет частичное соответствие

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `def` (define) — ключевое слово для определения функции в Python. |
| 2 | C | Функция без return (или с пустым return) возвращает None. |
| 3 | B | Позиционные аргументы передаются по порядку: name="Hello", greeting="World". |
| 4 | B | Именованные аргументы можно передавать в любом порядке. |
| 5 | B | Mutable default argument (список) создаётся один раз и переиспользуется. |
| 6 | B | `*args` собирает аргументы в tuple. sum((1,2,3,4)) = 10. |
| 7 | C | `**kwargs` собирает именованные аргументы в словарь (dict). |
| 8 | B | Правильный порядок: позиционные, *args, keyword-only, **kwargs. |
| 9 | B | `*args` распаковывает список в отдельные аргументы. 1+2+3=6. |
| 10 | B | LEGB — порядок поиска имён: Local → Enclosing → Global → Built-in. |
| 11 | B | `global` позволяет изменять (не только читать) глобальную переменную. |
| 12 | B | `lambda arguments: expression` — синтаксис lambda-функции. |
| 13 | B | `filter` оставляет элементы, для которых lambda вернула True (> 2). |
| 14 | B | `map` применяет функцию к каждому элементу: 1²=1, 2²=4, 3²=9. |
| 15 | B | Декоратор — функция, принимающая и возвращающая функцию с модифицированным поведением. |
| 16 | B | `@decorator` эквивалентно `func = decorator(func)`. |
| 17 | B | `@wraps` копирует `__name__`, `__doc__` и другие атрибуты оригинальной функции. |
| 18 | B | `yield` приостанавливает функцию и возвращает значение, создавая генератор. |
| 19 | B | Генераторы вычисляют значения по требованию, не храня всё в памяти. |
| 20 | B | `lru_cache` кэширует результаты, избегая повторных вычислений. |
| 21 | B | Синтаксис аннотаций: `param: type` и `-> return_type`. |
| 22 | C | Замыкание: inner() "помнит" x=5 из outer(). 5+3=8. |
| 23 | B | Множественный return автоматически создаёт tuple. |
| 24 | B | `__doc__` — специальный атрибут, содержащий docstring. |
| 25 | B | `partial` фиксирует часть аргументов, создавая новую функцию. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное понимание функций в Python! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите декораторы и генераторы. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на *args, **kwargs и замыкания. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и попрактиковаться. |

---

