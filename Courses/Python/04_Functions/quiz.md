# Python Functions - Quiz

Проверьте свои знания по теме "Функции, параметры, возвращаемые значения и лямбды".

---

## Question 1: Определение функции


Какое ключевое слово используется для определения функции?

A) `function`

B) `func`

C) `define`

D) `def`

---

## Question 2: Возвращаемое значение


Что вернёт функция без оператора return?

A) 0

B) Error

C) False

D) None

---

## Question 3: Позиционные аргументы


Что выведет следующий код?

```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

print(greet("Hello", "World"))
```

A) greeting, name!

B) Hello, World!

C) World, Hello!

D) Error

---

## Question 4: Именованные аргументы


Что выведет следующий код?

```python
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"

print(greet(greeting="Hello", name="Alice"))
```

A) Error

B) Alice, Hello!

C) Hi, Alice!

D) Hello, Alice!

---

## Question 5: Значения по умолчанию


Почему этот код работает неправильно?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

A) Синтаксическая ошибка

B) Код работает правильно

C) append() не работает

D) Список по умолчанию создаётся один раз

---

## Question 6: *args


Что выведет следующий код?

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))
```

A) 10

B) [1, 2, 3, 4]

C) Error

D) (1, 2, 3, 4)

---

## Question 7: **kwargs


Какой тип данных получает функция через **kwargs?

A) list

B) dict

C) tuple

D) set

---

## Question 8: Порядок параметров


Какой порядок параметров правильный?

A) `def f(**kwargs, *args, pos):`

B) `def f(pos, **kwargs, *args):`

C) `def f(pos, *args, **kwargs):`

D) `def f(*args, pos, **kwargs):`

---

## Question 9: Распаковка аргументов


Что выведет следующий код?

```python
def add(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(add(*args))
```

A) (1, 2, 3)

B) Error

C) 6

D) [1, 2, 3]

---

## Question 10: Область видимости


Что такое правило LEGB?

A) Способ передачи аргументов

B) Метод оптимизации функций

C) Порядок поиска переменных: Local, Enclosing, Global, Built-in

D) Порядок выполнения кода

---

## Question 11: global


Что делает ключевое слово `global`?

A) Делает переменную доступной везде автоматически

B) Позволяет изменять глобальную переменную внутри функции

C) Импортирует переменную из другого модуля

D) Создаёт новую глобальную переменную

---

## Question 12: Lambda функции


Какой синтаксис правильный для lambda?

A) `lambda x: x * 2`

B) `x => x * 2`

C) `lambda(x): x * 2`

D) `def lambda(x): return x * 2`

---

## Question 13: Lambda с filter


Что выведет следующий код?

```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, nums))
print(result)
```

A) 3

B) [1, 2]

C) [3, 4, 5]

D) [True, True, True]

---

## Question 14: Lambda с map


Что выведет следующий код?

```python
nums = [1, 2, 3]
result = list(map(lambda x: x ** 2, nums))
print(result)
```

A) [2, 4, 6]

B) [1, 2, 3]

C) 6

D) [1, 4, 9]

---

## Question 15: Декораторы


Что такое декоратор?

A) Способ форматирования вывода

B) Функция, модифицирующая поведение другой функции

C) Встроенная функция Python

D) Комментарий для документации

---

## Question 16: Синтаксис декоратора


Что эквивалентно `@decorator` перед функцией?

A) `func = decorator + func`

B) `func.decorator = decorator`

C) `func = decorator(func)`

D) `decorator.func = func`

---

## Question 17: functools.wraps


Зачем использовать `@functools.wraps` в декораторе?

A) Для ускорения выполнения

B) Для сохранения метаданных оригинальной функции

C) Для добавления документации

D) Для создания копии функции

---

## Question 18: Генераторы


Какое ключевое слово создаёт генератор?

A) `iter`

B) `return`

C) `generate`

D) `yield`

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

B) Делает функцию асинхронной

C) Кэширует результаты вызовов функции

D) Логирует вызовы функции

---

## Question 21: Аннотации типов


Какая аннотация правильная для функции?

A) `def add(a int, b int) int:`

B) `def add<int>(a, b):`

C) `def add(a, b) -> returns int:`

D) `def add(a: int, b: int) -> int:`

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

B) Error

C) 3

D) 8

---

## Question 23: Множественные return


Что выведет следующий код?

```python
def minmax(numbers):
    return min(numbers), max(numbers)

result = minmax([3, 1, 4, 1, 5])
print(type(result).__name__)
```

A) dict

B) tuple

C) list

D) int

---

## Question 24: Docstring


Как получить docstring функции?

A) `func.__doc__`

B) `getdoc(func)`

C) `func.docstring`

D) `func.doc`

---

## Question 25: partial


Что делает `functools.partial`?

A) Частично выполняет функцию

B) Проверяет частичное соответствие

C) Создаёт новую функцию с заранее заданными аргументами

D) Разделяет функцию на части

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `def` (define) — ключевое слово для определения функции в Python. |
| 2 | D | Функция без return (или с пустым return) возвращает None. |
| 3 | C | Позиционные аргументы передаются по порядку: name="Hello", greeting="World". |
| 4 | D | Именованные аргументы можно передавать в любом порядке. |
| 5 | D | Mutable default argument (список) создаётся один раз и переиспользуется. |
| 6 | A | `*args` собирает аргументы в tuple. sum((1,2,3,4)) = 10. |
| 7 | B | `**kwargs` собирает именованные аргументы в словарь (dict). |
| 8 | C | Правильный порядок: позиционные, *args, keyword-only, **kwargs. |
| 9 | C | `*args` распаковывает список в отдельные аргументы. 1+2+3=6. |
| 10 | C | LEGB — порядок поиска имён: Local → Enclosing → Global → Built-in. |
| 11 | B | `global` позволяет изменять (не только читать) глобальную переменную. |
| 12 | A | `lambda arguments: expression` — синтаксис lambda-функции. |
| 13 | C | `filter` оставляет элементы, для которых lambda вернула True (> 2). |
| 14 | D | `map` применяет функцию к каждому элементу: 1²=1, 2²=4, 3²=9. |
| 15 | B | Декоратор — функция, принимающая и возвращающая функцию с модифицированным поведением. |
| 16 | C | `@decorator` эквивалентно `func = decorator(func)`. |
| 17 | B | `@wraps` копирует `__name__`, `__doc__` и другие атрибуты оригинальной функции. |
| 18 | D | `yield` приостанавливает функцию и возвращает значение, создавая генератор. |
| 19 | B | Генераторы вычисляют значения по требованию, не храня всё в памяти. |
| 20 | C | `lru_cache` кэширует результаты, избегая повторных вычислений. |
| 21 | D | Синтаксис аннотаций: `param: type` и `-> return_type`. |
| 22 | D | Замыкание: inner() "помнит" x=5 из outer(). 5+3=8. |
| 23 | B | Множественный return автоматически создаёт tuple. |
| 24 | A | `__doc__` — специальный атрибут, содержащий docstring. |
| 25 | C | `partial` фиксирует часть аргументов, создавая новую функцию. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное понимание функций в Python! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите декораторы и генераторы. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на *args, **kwargs и замыкания. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и попрактиковаться. |

---

