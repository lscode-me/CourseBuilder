# Python Data Structures
## Числа, строки, списки, кортежи, множества и словари

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Установить Python 3.x на свою систему
- Уметь запускать Python-скрипты и использовать интерактивный режим
- Понимать основы присваивания переменных
- Знать, как использовать функцию `print()`

**Recommended prior modules:**
- [Intro](../01_Intro/) — введение в Python, установка, первые шаги

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Работать с числовыми типами данных и выполнять математические операции
- Создавать и манипулировать строками с помощью встроенных методов
- Использовать списки для хранения и обработки коллекций данных
- Применять кортежи, множества и словари для решения различных задач
- Выбирать подходящую структуру данных для конкретной задачи

---

## 1. Числовые типы данных

Python поддерживает несколько числовых типов. Они являются основой для любых вычислений и математических операций.

### 1.1 Целые числа (int)

Целые числа в Python не имеют ограничения по размеру (ограничены только памятью):

```python
# Целые числа
x = 42
y = -17
big_number = 999999999999999999999999999999

print(f"x = {x}, тип: {type(x)}")
print(f"big_number = {big_number}")

# Различные системы счисления
decimal = 255        # Десятичная
binary = 0b11111111  # Двоичная (0b)
octal = 0o377        # Восьмеричная (0o)
hexadecimal = 0xFF   # Шестнадцатеричная (0x)

print(f"Все равны 255: {decimal}, {binary}, {octal}, {hexadecimal}")
```

**Output:**
```
x = 42, тип: <class 'int'>
big_number = 999999999999999999999999999999
Все равны 255: 255, 255, 255, 255
```

**Разделитель разрядов:**

```python
# Underscore для читаемости больших чисел
population = 7_900_000_000
bytes_in_gb = 1_073_741_824

print(f"Население Земли: {population:,}")
print(f"Байт в ГБ: {bytes_in_gb:,}")
```

**Output:**
```
Население Земли: 7,900,000,000
Байт в ГБ: 1,073,741,824
```

### 1.2 Числа с плавающей точкой (float)

```python
# Числа с плавающей точкой
pi = 3.14159
temperature = -40.0
scientific = 6.022e23  # Научная нотация: 6.022 × 10²³

print(f"pi = {pi}, тип: {type(pi)}")
print(f"Число Авогадро: {scientific}")

# Специальные значения
import math
print(f"Бесконечность: {math.inf}")
print(f"Не число: {math.nan}")
```

**Output:**
```
pi = 3.14159, тип: <class 'float'>
Число Авогадро: 6.022e+23
Бесконечность: inf
Не число: nan
```

> **⚠️ Warning:**  
> Числа с плавающей точкой имеют ограниченную точность. Не используйте их для финансовых расчётов!

```python
# Проблема точности float
print(0.1 + 0.2)  # Не точно 0.3!
print(0.1 + 0.2 == 0.3)  # False!

# Для точных вычислений используйте Decimal
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))
```

**Output:**
```
0.30000000000000004
False
0.3
True
```

### 1.3 Комплексные числа (complex)

```python
# Комплексные числа (j — мнимая единица)
z1 = 3 + 4j
z2 = complex(2, -1)

print(f"z1 = {z1}")
print(f"Действительная часть: {z1.real}")
print(f"Мнимая часть: {z1.imag}")
print(f"Сопряжённое: {z1.conjugate()}")
print(f"Модуль: {abs(z1)}")
```

**Output:**
```
z1 = (3+4j)
Действительная часть: 3.0
Мнимая часть: 4.0
Сопряжённое: (3-4j)
Модуль: 5.0
```

### 1.4 Арифметические операции

```python
a, b = 17, 5

print(f"a + b = {a + b}")   # Сложение
print(f"a - b = {a - b}")   # Вычитание
print(f"a * b = {a * b}")   # Умножение
print(f"a / b = {a / b}")   # Деление (всегда float)
print(f"a // b = {a // b}") # Целочисленное деление
print(f"a % b = {a % b}")   # Остаток от деления
print(f"a ** b = {a ** b}") # Возведение в степень
print(f"-a = {-a}")         # Унарный минус
```

**Output:**
```
a + b = 22
a - b = 12
a * b = 85
a / b = 3.4
a // b = 3
a % b = 2
a ** b = 1419857
-a = -17
```

**Составные операторы присваивания:**

```python
x = 10
x += 5   # x = x + 5
print(f"После x += 5: {x}")

x *= 2   # x = x * 2
print(f"После x *= 2: {x}")

x //= 3  # x = x // 3
print(f"После x //= 3: {x}")
```

**Output:**
```
После x += 5: 15
После x *= 2: 30
После x //= 3: 10
```

### 1.5 Математические функции

```python
import math

# Базовые функции
print(f"abs(-5) = {abs(-5)}")
print(f"round(3.7) = {round(3.7)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# Функции модуля math
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pow(2, 10) = {math.pow(2, 10)}")
print(f"math.ceil(3.1) = {math.ceil(3.1)}")
print(f"math.floor(3.9) = {math.floor(3.9)}")
print(f"math.log10(1000) = {math.log10(1000)}")

# Константы
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
```

**Output:**
```
abs(-5) = 5
round(3.7) = 4
round(3.14159, 2) = 3.14
math.sqrt(16) = 4.0
math.pow(2, 10) = 1024.0
math.ceil(3.1) = 4
math.floor(3.9) = 3
math.log10(1000) = 3.0
math.pi = 3.141592653589793
math.e = 2.718281828459045
```

---

## 2. Логический тип (bool)

### 2.1 Булевы значения

```python
# Булевы значения
is_active = True
is_deleted = False

print(f"is_active = {is_active}, тип: {type(is_active)}")

# bool — подкласс int
print(f"True + True = {True + True}")
print(f"True * 10 = {True * 10}")
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")
```

**Output:**
```
is_active = True, тип: <class 'bool'>
True + True = 2
True * 10 = 10
int(True) = 1
int(False) = 0
```

### 2.2 Операции сравнения

```python
x, y = 10, 20

print(f"x == y: {x == y}")  # Равно
print(f"x != y: {x != y}")  # Не равно
print(f"x < y: {x < y}")    # Меньше
print(f"x > y: {x > y}")    # Больше
print(f"x <= y: {x <= y}")  # Меньше или равно
print(f"x >= y: {x >= y}")  # Больше или равно

# Цепочки сравнений
age = 25
print(f"18 <= age <= 65: {18 <= age <= 65}")
```

**Output:**
```
x == y: False
x != y: True
x < y: True
x > y: False
x <= y: True
x >= y: False
18 <= age <= 65: True
```

### 2.3 Логические операторы

```python
a = True
b = False

print(f"a and b: {a and b}")  # Логическое И
print(f"a or b: {a or b}")    # Логическое ИЛИ
print(f"not a: {not a}")      # Логическое НЕ

# Короткое замыкание
print(f"False and print('не выполнится'): {False and 'hi'}")
print(f"True or print('не выполнится'): {True or 'hi'}")
```

**Output:**
```
a and b: False
a or b: True
not a: False
False and print('не выполнится'): False
True or print('не выполнится'): True
```

### 2.4 Truthiness

В Python многие значения можно использовать как булевы:

```python
# Falsy значения (преобразуются в False)
falsy_values = [None, 0, 0.0, '', [], {}, set()]

for val in falsy_values:
    print(f"bool({val!r}) = {bool(val)}")

print()

# Truthy значения (преобразуются в True)
truthy_values = [1, -1, "hello", [1, 2], {"a": 1}]

for val in truthy_values:
    print(f"bool({val!r}) = {bool(val)}")
```

**Output:**
```
bool(None) = False
bool(0) = False
bool(0.0) = False
bool('') = False
bool([]) = False
bool({}) = False
bool(set()) = False

bool(1) = True
bool(-1) = True
bool('hello') = True
bool([1, 2]) = True
bool({'a': 1}) = True
```

---

## 3. Строки (str)

Строки — один из самых часто используемых типов данных. Python предоставляет богатый набор методов для работы со строками.

### 3.1 Создание строк

```python
# Различные способы создания строк
s1 = 'Одинарные кавычки'
s2 = "Двойные кавычки"
s3 = '''Многострочная
строка с тройными
кавычками'''
s4 = """Тоже многострочная
строка"""

print(s1)
print(s2)
print(s3)

# Специальные символы
escaped = "Табуляция:\tновая строка:\nобратный слэш:\\"
print(escaped)

# Raw-строки (игнорируют escape-последовательности)
raw = r"C:\Users\name\documents"
print(raw)
```

**Output:**
```
Одинарные кавычки
Двойные кавычки
Многострочная
строка с тройными
кавычками
Табуляция:	новая строка:
обратный слэш:\
C:\Users\name\documents
```

### 3.2 Индексация и срезы

```python
s = "Python"

# Индексация (начинается с 0)
print(f"s[0] = '{s[0]}'")   # Первый символ
print(f"s[-1] = '{s[-1]}'") # Последний символ
print(f"s[2] = '{s[2]}'")   # Третий символ

# Срезы [start:stop:step]
print(f"s[0:3] = '{s[0:3]}'")   # С 0 по 2 включительно
print(f"s[2:] = '{s[2:]}'")     # С 2 до конца
print(f"s[:4] = '{s[:4]}'")     # С начала до 3
print(f"s[::2] = '{s[::2]}'")   # Каждый второй символ
print(f"s[::-1] = '{s[::-1]}'") # Разворот строки
```

**Output:**
```
s[0] = 'P'
s[-1] = 'n'
s[2] = 't'
s[0:3] = 'Pyt'
s[2:] = 'thon'
s[:4] = 'Pyth'
s[::2] = 'Pto'
s[::-1] = 'nohtyP'
```

### 3.3 Основные операции

```python
# Конкатенация
greeting = "Hello" + " " + "World"
print(greeting)

# Повторение
line = "-" * 20
print(line)

# Длина строки
text = "Python"
print(f"Длина '{text}': {len(text)}")

# Проверка вхождения
print(f"'th' in 'Python': {'th' in 'Python'}")
print(f"'x' in 'Python': {'x' in 'Python'}")

# Строки неизменяемы!
# s[0] = 'J'  # TypeError!
```

**Output:**
```
Hello World
--------------------
Длина 'Python': 6
'th' in 'Python': True
'x' in 'Python': False
```

### 3.4 Методы строк

```python
text = "  Hello, Python World!  "

# Регистр
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"swapcase(): '{text.swapcase()}'")

# Удаление пробелов
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")
```

**Output:**
```
upper(): '  HELLO, PYTHON WORLD!  '
lower(): '  hello, python world!  '
title(): '  Hello, Python World!  '
capitalize(): '  hello, python world!  '
swapcase(): '  hELLO, pYTHON wORLD!  '
strip(): 'Hello, Python World!'
lstrip(): 'Hello, Python World!  '
rstrip(): '  Hello, Python World!'
```

**Поиск и замена:**

```python
text = "Python is awesome and Python is fun"

# Поиск
print(f"find('Python'): {text.find('Python')}")
print(f"find('Python', 10): {text.find('Python', 10)}")
print(f"find('Java'): {text.find('Java')}")  # -1 если не найдено
print(f"count('Python'): {text.count('Python')}")

# Замена
print(f"replace(): '{text.replace('Python', 'Java')}'")

# Проверки
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('fun'): {text.endswith('fun')}")
```

**Output:**
```
find('Python'): 0
find('Python', 10): 23
find('Java'): -1
count('Python'): 2
replace(): 'Java is awesome and Java is fun'
startswith('Python'): True
endswith('fun'): True
```

**Разделение и объединение:**

```python
# split() — разделение строки
sentence = "Python is easy to learn"
words = sentence.split()
print(f"split(): {words}")

csv_line = "apple,banana,cherry"
fruits = csv_line.split(',')
print(f"split(','): {fruits}")

# join() — объединение списка в строку
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"join(): '{sentence}'")

path = "/".join(["home", "user", "documents"])
print(f"join path: '{path}'")
```

**Output:**
```
split(): ['Python', 'is', 'easy', 'to', 'learn']
split(','): ['apple', 'banana', 'cherry']
join(): 'Python is awesome'
join path: 'home/user/documents'
```

### 3.5 Форматирование строк

```python
name = "Alice"
age = 30
balance = 1234.5678

# f-strings (рекомендуется, Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Balance: ${balance:.2f}")
print(f"Name: {name:>10}")  # Выравнивание вправо
print(f"Name: {name:<10}")  # Выравнивание влево
print(f"Name: {name:^10}")  # По центру

# Форматирование чисел
number = 1234567
print(f"Number: {number:,}")      # С разделителями
print(f"Number: {number:_}")      # С подчёркиваниями
print(f"Percent: {0.75:.1%}")     # Проценты
print(f"Binary: {255:b}")         # Двоичное
print(f"Hex: {255:x}")            # Шестнадцатеричное
```

**Output:**
```
Name: Alice, Age: 30
Balance: $1234.57
Name:      Alice
Name: Alice     
Name:   Alice   
Number: 1,234,567
Number: 1_234_567
Percent: 75.0%
Binary: 11111111
Hex: ff
```

**Метод format() (альтернатива):**

```python
# Позиционные аргументы
print("{} {} {}".format("a", "b", "c"))

# Именованные аргументы
print("{name} is {age} years old".format(name="Bob", age=25))

# Индексы
print("{0} {1} {0}".format("Python", "is"))
```

**Output:**
```
a b c
Bob is 25 years old
Python is Python
```

---

## 4. Списки (list)

Списки — упорядоченные изменяемые коллекции. Они могут содержать элементы любых типов.

### 4.1 Создание списков

```python
# Пустой список
empty = []
empty2 = list()

# Список с элементами
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"nested: {nested}")

# Создание из других итерируемых объектов
from_string = list("Python")
from_range = list(range(5))

print(f"from_string: {from_string}")
print(f"from_range: {from_range}")
```

**Output:**
```
numbers: [1, 2, 3, 4, 5]
mixed: [1, 'hello', 3.14, True, None]
nested: [[1, 2], [3, 4], [5, 6]]
from_string: ['P', 'y', 't', 'h', 'o', 'n']
from_range: [0, 1, 2, 3, 4]
```

### 4.2 Индексация и срезы

Работают так же, как со строками:

```python
numbers = [10, 20, 30, 40, 50]

print(f"numbers[0]: {numbers[0]}")
print(f"numbers[-1]: {numbers[-1]}")
print(f"numbers[1:4]: {numbers[1:4]}")
print(f"numbers[::2]: {numbers[::2]}")
print(f"numbers[::-1]: {numbers[::-1]}")

# Но списки изменяемы!
numbers[0] = 100
print(f"После numbers[0] = 100: {numbers}")

numbers[1:3] = [200, 300]
print(f"После numbers[1:3] = [200, 300]: {numbers}")
```

**Output:**
```
numbers[0]: 10
numbers[-1]: 50
numbers[1:4]: [20, 30, 40]
numbers[::2]: [10, 30, 50]
numbers[::-1]: [50, 40, 30, 20, 10]
После numbers[0] = 100: [100, 20, 30, 40, 50]
После numbers[1:3] = [200, 300]: [100, 200, 300, 40, 50]
```

### 4.3 Основные методы списков

```python
fruits = ["apple", "banana"]

# Добавление элементов
fruits.append("cherry")           # В конец
print(f"После append: {fruits}")

fruits.insert(1, "blueberry")     # По индексу
print(f"После insert: {fruits}")

fruits.extend(["date", "elderberry"])  # Несколько элементов
print(f"После extend: {fruits}")

# Удаление элементов
removed = fruits.pop()            # Последний элемент
print(f"pop() вернул: {removed}")
print(f"После pop(): {fruits}")

fruits.remove("blueberry")        # По значению
print(f"После remove: {fruits}")

# Поиск
print(f"index('banana'): {fruits.index('banana')}")
print(f"count('apple'): {fruits.count('apple')}")
print(f"'apple' in fruits: {'apple' in fruits}")
```

**Output:**
```
После append: ['apple', 'banana', 'cherry']
После insert: ['apple', 'blueberry', 'banana', 'cherry']
После extend: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
pop() вернул: elderberry
После pop(): ['apple', 'blueberry', 'banana', 'cherry', 'date']
После remove: ['apple', 'banana', 'cherry', 'date']
index('banana'): 1
count('apple'): 1
'apple' in fruits: True
```

### 4.4 Сортировка

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() — изменяет список на месте
numbers.sort()
print(f"После sort(): {numbers}")

numbers.sort(reverse=True)
print(f"После sort(reverse=True): {numbers}")

# sorted() — возвращает новый список
original = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(original)
print(f"original: {original}")
print(f"sorted(): {sorted_list}")

# Сортировка с ключом
words = ["banana", "Apple", "cherry"]
print(f"sorted(key=str.lower): {sorted(words, key=str.lower)}")
print(f"sorted(key=len): {sorted(words, key=len)}")
```

**Output:**
```
После sort(): [1, 1, 2, 3, 4, 5, 6, 9]
После sort(reverse=True): [9, 6, 5, 4, 3, 2, 1, 1]
original: [3, 1, 4, 1, 5, 9]
sorted(): [1, 1, 3, 4, 5, 9]
sorted(key=str.lower): ['Apple', 'banana', 'cherry']
sorted(key=len): ['Apple', 'banana', 'cherry']
```

### 4.5 List Comprehensions

List comprehensions — элегантный способ создания списков:

```python
# Базовый синтаксис
squares = [x**2 for x in range(10)]
print(f"Квадраты: {squares}")

# С условием
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Чётные квадраты: {even_squares}")

# С преобразованием
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"Upper: {upper_words}")

# Вложенные comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")

# Conditional expression (тернарный оператор)
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"Absolute: {abs_values}")
```

**Output:**
```
Квадраты: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Чётные квадраты: [0, 4, 16, 36, 64]
Upper: ['HELLO', 'WORLD', 'PYTHON']
Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Absolute: [1, 2, 3, 4, 5]
```

---

## 5. Кортежи (tuple)

Кортежи — упорядоченные **неизменяемые** коллекции. Используются когда данные не должны меняться.

### 5.1 Создание кортежей

```python
# Создание кортежей
empty_tuple = ()
single = (42,)       # Запятая обязательна для одного элемента!
point = (3, 4)
mixed = (1, "hello", 3.14)

print(f"point: {point}, тип: {type(point)}")
print(f"single: {single}, тип: {type(single)}")

# Без скобок (packing)
coords = 10, 20, 30
print(f"coords: {coords}, тип: {type(coords)}")

# Unpacking
x, y, z = coords
print(f"x={x}, y={y}, z={z}")

# Обмен значениями (использует кортежи)
a, b = 1, 2
a, b = b, a
print(f"После обмена: a={a}, b={b}")
```

**Output:**
```
point: (3, 4), тип: <class 'tuple'>
single: (42,), тип: <class 'tuple'>
coords: (10, 20, 30), тип: <class 'tuple'>
x=10, y=20, z=30
После обмена: a=2, b=1
```

### 5.2 Операции с кортежами

```python
t = (1, 2, 3, 2, 4, 2)

# Индексация и срезы (как в списках)
print(f"t[0]: {t[0]}")
print(f"t[-1]: {t[-1]}")
print(f"t[1:4]: {t[1:4]}")

# Методы
print(f"count(2): {t.count(2)}")
print(f"index(3): {t.index(3)}")

# Кортежи неизменяемы!
# t[0] = 100  # TypeError!

# Но можно создать новый кортеж
new_t = t + (5, 6)
print(f"После конкатенации: {new_t}")
```

**Output:**
```
t[0]: 1
t[-1]: 2
t[1:4]: (2, 3, 2)
count(2): 3
index(3): 2
После конкатенации: (1, 2, 3, 2, 4, 2, 5, 6)
```

### 5.3 Named Tuples

Именованные кортежи — удобный способ создания простых классов данных:

```python
from collections import namedtuple

# Создание типа
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Использование
p = Point(3, 4)
print(f"Point: {p}")
print(f"x: {p.x}, y: {p.y}")
print(f"Как кортеж: {p[0]}, {p[1]}")

alice = Person("Alice", 30, "Moscow")
print(f"Person: {alice}")
print(f"Name: {alice.name}")

# Распаковка работает
name, age, city = alice
print(f"Распаковка: {name}, {age}, {city}")
```

**Output:**
```
Point: Point(x=3, y=4)
x: 3, y: 4
Как кортеж: 3, 4
Person: Person(name='Alice', age=30, city='Moscow')
Name: Alice
Распаковка: Alice, 30, Moscow
```

---

## 6. Множества (set)

Множества — неупорядоченные коллекции **уникальных** элементов. Эффективны для проверки членства и удаления дубликатов.

### 6.1 Создание множеств

```python
# Создание множеств
empty_set = set()  # Не {} — это пустой словарь!
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])

print(f"numbers: {numbers}")
print(f"from_list (дубликаты удалены): {from_list}")

# Множество из строки
chars = set("hello")
print(f"chars: {chars}")  # Порядок не гарантирован
```

**Output:**
```
numbers: {1, 2, 3, 4, 5}
from_list (дубликаты удалены): {1, 2, 3}
chars: {'h', 'e', 'l', 'o'}
```

### 6.2 Операции с множествами

```python
s = {1, 2, 3}

# Добавление и удаление
s.add(4)
print(f"После add(4): {s}")

s.discard(2)  # Не вызывает ошибку если элемента нет
print(f"После discard(2): {s}")

s.remove(3)   # Вызывает KeyError если элемента нет
print(f"После remove(3): {s}")

# Проверка членства — очень быстрая O(1)
print(f"1 in s: {1 in s}")
print(f"5 in s: {5 in s}")
```

**Output:**
```
После add(4): {1, 2, 3, 4}
После discard(2): {1, 3, 4}
После remove(3): {1, 4}
1 in s: True
5 in s: False
```

### 6.3 Операции над множествами

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Объединение
print(f"a | b (объединение): {a | b}")
print(f"a.union(b): {a.union(b)}")

# Пересечение
print(f"a & b (пересечение): {a & b}")
print(f"a.intersection(b): {a.intersection(b)}")

# Разность
print(f"a - b (разность): {a - b}")
print(f"a.difference(b): {a.difference(b)}")

# Симметрическая разность
print(f"a ^ b (симм. разность): {a ^ b}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")

# Проверки
print(f"{{1, 2}} <= {{1, 2, 3}}: {{1, 2} <= {1, 2, 3}}")  # Подмножество
print(f"a.isdisjoint({{10, 20}}): {a.isdisjoint({10, 20})}")  # Нет общих
```

**Output:**
```
a | b (объединение): {1, 2, 3, 4, 5, 6}
a.union(b): {1, 2, 3, 4, 5, 6}
a & b (пересечение): {3, 4}
a.intersection(b): {3, 4}
a - b (разность): {1, 2}
a.difference(b): {1, 2}
a ^ b (симм. разность): {1, 2, 5, 6}
a.symmetric_difference(b): {1, 2, 5, 6}
{1, 2} <= {1, 2, 3}: True
a.isdisjoint({10, 20}): True
```

### 6.4 Frozenset

`frozenset` — неизменяемое множество:

```python
# Обычное множество нельзя использовать как ключ словаря
# или добавить в другое множество

fs = frozenset([1, 2, 3])
print(f"frozenset: {fs}")

# Можно использовать как ключ словаря
d = {fs: "value"}
print(f"Словарь с frozenset ключом: {d}")

# Можно добавить в множество
s = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Множество frozenset'ов: {s}")
```

**Output:**
```
frozenset: frozenset({1, 2, 3})
Словарь с frozenset ключом: {frozenset({1, 2, 3}): 'value'}
Множество frozenset'ов: {frozenset({1, 2}), frozenset({3, 4})}
```

---

## 7. Словари (dict)

Словари — коллекции пар ключ-значение. Один из самых важных типов данных в Python.

### 7.1 Создание словарей

```python
# Различные способы создания
empty = {}
person = {"name": "Alice", "age": 30, "city": "Moscow"}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(x=10, y=20)

print(f"person: {person}")
print(f"from_pairs: {from_pairs}")
print(f"from_kwargs: {from_kwargs}")

# Dict comprehension
squares = {x: x**2 for x in range(5)}
print(f"squares: {squares}")
```

**Output:**
```
person: {'name': 'Alice', 'age': 30, 'city': 'Moscow'}
from_pairs: {'a': 1, 'b': 2}
from_kwargs: {'x': 10, 'y': 20}
squares: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 7.2 Доступ к элементам

```python
person = {"name": "Alice", "age": 30, "city": "Moscow"}

# Доступ по ключу
print(f"name: {person['name']}")

# get() — безопасный доступ
print(f"age: {person.get('age')}")
print(f"salary: {person.get('salary')}")  # None если нет ключа
print(f"salary: {person.get('salary', 0)}")  # Значение по умолчанию

# Проверка наличия ключа
print(f"'name' in person: {'name' in person}")
print(f"'salary' in person: {'salary' in person}")
```

**Output:**
```
name: Alice
age: 30
salary: None
salary: 0
'name' in person: True
'salary' in person: False
```

### 7.3 Изменение словарей

```python
person = {"name": "Alice", "age": 30}

# Добавление/изменение
person["city"] = "Moscow"
person["age"] = 31
print(f"После изменений: {person}")

# update() — объединение словарей
person.update({"country": "Russia", "age": 32})
print(f"После update: {person}")

# Python 3.9+ — оператор |
extra = {"job": "Developer"}
merged = person | extra
print(f"Merged: {merged}")

# Удаление
del person["country"]
print(f"После del: {person}")

removed = person.pop("city")
print(f"pop('city') вернул: {removed}")
print(f"После pop: {person}")
```

**Output:**
```
После изменений: {'name': 'Alice', 'age': 31, 'city': 'Moscow'}
После update: {'name': 'Alice', 'age': 32, 'city': 'Moscow', 'country': 'Russia'}
Merged: {'name': 'Alice', 'age': 32, 'city': 'Moscow', 'country': 'Russia', 'job': 'Developer'}
После del: {'name': 'Alice', 'age': 32, 'city': 'Moscow'}
pop('city') вернул: Moscow
После pop: {'name': 'Alice', 'age': 32}
```

### 7.4 Итерация по словарям

```python
person = {"name": "Alice", "age": 30, "city": "Moscow"}

# Итерация по ключам (по умолчанию)
print("Ключи:")
for key in person:
    print(f"  {key}")

# Явно по ключам
print("\nkeys():")
for key in person.keys():
    print(f"  {key}: {person[key]}")

# По значениям
print("\nvalues():")
for value in person.values():
    print(f"  {value}")

# По парам ключ-значение
print("\nitems():")
for key, value in person.items():
    print(f"  {key}: {value}")
```

**Output:**
```
Ключи:
  name
  age
  city

keys():
  name: Alice
  age: 30
  city: Moscow

values():
  Alice
  30
  Moscow

items():
  name: Alice
  age: 30
  city: Moscow
```

### 7.5 Полезные методы

```python
# setdefault — получить или установить значение
stats = {}
stats.setdefault("count", 0)
stats["count"] += 1
print(f"stats: {stats}")

# defaultdict — словарь со значением по умолчанию
from collections import defaultdict

word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count[word] += 1
print(f"word_count: {dict(word_count)}")

# Counter — подсчёт элементов
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(f"char_count: {char_count}")
print(f"most_common(3): {char_count.most_common(3)}")
```

**Output:**
```
stats: {'count': 1}
word_count: {'apple': 3, 'banana': 2, 'cherry': 1}
char_count: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
most_common(3): [('l', 3), ('o', 2), ('h', 1)]
```

---

## 8. Преобразование типов

### 8.1 Явное преобразование

```python
# Строка в число
s = "42"
n = int(s)
f = float(s)
print(f"int('42') = {n}, float('42') = {f}")

# Число в строку
n = 42
s = str(n)
print(f"str(42) = '{s}'")

# Список, кортеж, множество
lst = [1, 2, 3]
tpl = tuple(lst)
st = set(lst)
print(f"list -> tuple: {tpl}")
print(f"list -> set: {st}")

# Из range
r = range(5)
print(f"list(range(5)): {list(r)}")
print(f"tuple(range(5)): {tuple(r)}")
```

**Output:**
```
int('42') = 42, float('42') = 42.0
str(42) = '42'
list -> tuple: (1, 2, 3)
list -> set: {1, 2, 3}
list(range(5)): [0, 1, 2, 3, 4]
tuple(range(5)): (0, 1, 2, 3, 4)
```

### 8.2 Полезные функции

```python
# ord() и chr() — символ <-> код
print(f"ord('A') = {ord('A')}")
print(f"chr(65) = '{chr(65)}'")

# bin(), oct(), hex() — системы счисления
n = 255
print(f"bin(255) = {bin(n)}")
print(f"oct(255) = {oct(n)}")
print(f"hex(255) = {hex(n)}")

# int() с основанием
print(f"int('ff', 16) = {int('ff', 16)}")
print(f"int('11111111', 2) = {int('11111111', 2)}")
```

**Output:**
```
ord('A') = 65
chr(65) = 'A'
bin(255) = 0b11111111
oct(255) = 0o377
hex(255) = 0xff
int('ff', 16) = 255
int('11111111', 2) = 255
```

---

## 9. Выбор структуры данных

### 9.1 Сравнение коллекций

| Структура | Упорядочена | Изменяема | Дубликаты | Использовать когда |
|-----------|-------------|-----------|-----------|-------------------|
| `list` | Да | Да | Да | Нужна упорядоченная коллекция |
| `tuple` | Да | Нет | Да | Данные не должны меняться |
| `set` | Нет | Да | Нет | Нужна уникальность, быстрый поиск |
| `dict` | Да* | Да | Ключи — нет | Пары ключ-значение |

*Python 3.7+ гарантирует сохранение порядка вставки в словарях.

### 9.2 Производительность

| Операция | list | set | dict |
|----------|------|-----|------|
| Доступ по индексу | O(1) | - | - |
| Доступ по ключу | - | - | O(1) |
| Поиск (in) | O(n) | O(1) | O(1) |
| Добавление в конец | O(1) | O(1) | O(1) |
| Добавление в начало | O(n) | - | - |
| Удаление | O(n) | O(1) | O(1) |

### 9.3 Когда что использовать

```python
# list — когда важен порядок и нужны дубликаты
tasks = ["task1", "task2", "task1"]  # Повторяющиеся задачи ОК

# tuple — для неизменяемых данных, как ключи словаря
coordinates = (55.7558, 37.6173)  # Координаты не должны меняться
locations = {(55.7558, 37.6173): "Moscow"}

# set — для уникальных значений, быстрой проверки членства
unique_ids = {101, 102, 103}
if 101 in unique_ids:  # O(1)
    print("Found!")

# dict — для связи ключей со значениями
user = {"name": "Alice", "age": 30}
```

---

## 10. Common Pitfalls

### 10.1 Изменяемый аргумент по умолчанию

❌ **Ошибка:**
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — не [2]!
```

✅ **Правильно:**
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2]
```

### 10.2 Копирование вложенных структур

```python
import copy

# Поверхностная копия
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999

print(f"original: {original}")  # Изменился!
print(f"shallow: {shallow}")

# Глубокая копия
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999

print(f"original: {original}")  # Не изменился
print(f"deep: {deep}")
```

**Output:**
```
original: [[999, 2], [3, 4]]
shallow: [[999, 2], [3, 4]]
original: [[1, 2], [3, 4]]
deep: [[999, 2], [3, 4]]
```

### 10.3 Сравнение float

❌ **Ошибка:**
```python
if 0.1 + 0.2 == 0.3:
    print("Equal")  # Не выполнится!
```

✅ **Правильно:**
```python
import math

if math.isclose(0.1 + 0.2, 0.3):
    print("Equal")  # Выполнится

# Или для финансов
from decimal import Decimal
if Decimal('0.1') + Decimal('0.2') == Decimal('0.3'):
    print("Equal")  # Выполнится
```

---

## 💡 Key Takeaways

- **Числа**: `int` для целых (без ограничений), `float` для дробных (осторожно с точностью), `Decimal` для финансов.

- **Строки неизменяемы**: Методы строк возвращают новые строки. Используйте f-strings для форматирования.

- **Списки vs кортежи**: Списки изменяемы, кортежи — нет. Используйте кортежи для данных, которые не должны меняться.

- **Множества для уникальности**: Автоматически удаляют дубликаты, поиск за O(1).

- **Словари — ключевая структура**: Используйте для связи ключей со значениями. `get()` для безопасного доступа.

---

## 🚀 Next Steps

**Related Modules:**
- [Flow Control](../03_FlowControl/) — циклы и условия для работы с коллекциями
- [Functions](../04_Functions/) — создание функций для обработки данных

**Practice Ideas:**
1. Создайте телефонную книгу на словарях с поиском по имени
2. Напишите программу для подсчёта слов в тексте (используйте Counter)
3. Реализуйте удаление дубликатов из списка с сохранением порядка
4. Создайте программу для работы с матрицами (вложенные списки)

**Going Deeper:**
- Изучите модуль `collections` (deque, OrderedDict, ChainMap)
- Познакомьтесь с dataclasses (Python 3.7+)
- Изучите array для эффективной работы с числами

---

## 📚 Additional Resources

**Documentation:**
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Collections module](https://docs.python.org/3/library/collections.html)
- [Decimal module](https://docs.python.org/3/library/decimal.html)

**Articles:**
- [Python Data Structures Tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- [Time Complexity (Big O)](https://wiki.python.org/moin/TimeComplexity)

---

