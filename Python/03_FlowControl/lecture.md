# Python Flow Control
## Условные операторы и циклы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать базовые типы данных Python (числа, строки, списки)
- Понимать логические операции и сравнения
- Уметь работать с коллекциями (списки, словари)
- Знать концепцию truthiness в Python

**Recommended prior modules:**
- [Data Structures](../02_DataStructures/) — типы данных и коллекции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Использовать условные операторы if/elif/else для ветвления логики
- Применять циклы for и while для итерации и повторения
- Управлять выполнением циклов с помощью break, continue и else
- Создавать вложенные структуры управления потоком
- Использовать match/case для сопоставления с образцом (Python 3.10+)

---

## 1. Условные операторы

Условные операторы позволяют программе принимать решения и выполнять разный код в зависимости от условий.

### 1.1 Оператор if

Базовый оператор условия:

```python
age = 18

if age >= 18:
    print("Вы совершеннолетний")
    print("Доступ разрешён")

print("Программа продолжается")
```

**Output:**
```
Вы совершеннолетний
Доступ разрешён
Программа продолжается
```

Отступы критически важны — они определяют блок кода:

```python
temperature = 25

if temperature > 20:
    print("Тепло")
    print("Можно идти на прогулку")
print("Это выполнится в любом случае")
```

**Output:**
```
Тепло
Можно идти на прогулку
Это выполнится в любом случае
```

### 1.2 Оператор if-else

Когда нужно выполнить альтернативный код:

```python
number = 7

if number % 2 == 0:
    print(f"{number} — чётное число")
else:
    print(f"{number} — нечётное число")
```

**Output:**
```
7 — нечётное число
```

**Пример: Проверка доступа**

```python
password = "secret123"
user_input = "secret123"

if user_input == password:
    print("Доступ разрешён")
    print("Добро пожаловать!")
else:
    print("Доступ запрещён")
    print("Неверный пароль")
```

**Output:**
```
Доступ разрешён
Добро пожаловать!
```

### 1.3 Оператор if-elif-else

Для множественного выбора:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Оценка {score} — это {grade}")
```

**Output:**
```
Оценка 85 — это B
```

> **💡 Pro Tip:**  
> Порядок условий важен! Python проверяет условия сверху вниз и выполняет первый подходящий блок.

**Пример: Определение времени года**

```python
month = 4

if month in [12, 1, 2]:
    season = "Зима"
elif month in [3, 4, 5]:
    season = "Весна"
elif month in [6, 7, 8]:
    season = "Лето"
elif month in [9, 10, 11]:
    season = "Осень"
else:
    season = "Неизвестно"

print(f"Месяц {month} — это {season}")
```

**Output:**
```
Месяц 4 — это Весна
```

### 1.4 Вложенные условия

Условия можно вкладывать друг в друга:

```python
age = 25
has_license = True

if age >= 18:
    print("Возраст подходит")
    if has_license:
        print("Можете водить автомобиль")
    else:
        print("Нужно получить права")
else:
    print("Слишком молоды для вождения")
```

**Output:**
```
Возраст подходит
Можете водить автомобиль
```

> **⚠️ Warning:**  
> Избегайте глубокой вложенности (более 3 уровней). Это ухудшает читаемость. Используйте ранний return или логические операторы.

**Рефакторинг глубокой вложенности:**

```python
# Плохо — глубокая вложенность
def check_access(user):
    if user:
        if user.is_active:
            if user.has_permission:
                return "Access granted"
            else:
                return "No permission"
        else:
            return "User inactive"
    else:
        return "No user"

# Хорошо — ранний выход
def check_access(user):
    if not user:
        return "No user"
    if not user.is_active:
        return "User inactive"
    if not user.has_permission:
        return "No permission"
    return "Access granted"
```

### 1.5 Тернарный оператор

Компактная форма if-else для простых случаев:

```python
age = 20

# Стандартная форма
if age >= 18:
    status = "взрослый"
else:
    status = "ребёнок"

# Тернарная форма
status = "взрослый" if age >= 18 else "ребёнок"
print(f"Статус: {status}")

# Можно использовать в выражениях
print(f"Вы {'можете' if age >= 18 else 'не можете'} голосовать")
```

**Output:**
```
Статус: взрослый
Вы можете голосовать
```

**Вложенные тернарные операторы (используйте осторожно):**

```python
score = 85

# Работает, но трудно читать
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")
```

**Output:**
```
Grade: B
```

### 1.6 Truthiness в условиях

Python позволяет использовать любые значения в условиях:

```python
# Проверка пустой строки
name = ""
if name:
    print(f"Привет, {name}!")
else:
    print("Имя не указано")

# Проверка пустого списка
items = []
if items:
    print(f"Элементов: {len(items)}")
else:
    print("Список пуст")

# Проверка None
result = None
if result is None:
    print("Результат отсутствует")
```

**Output:**
```
Имя не указано
Список пуст
Результат отсутствует
```

> **💡 Pro Tip:**  
> Используйте `if x is None` для проверки на None, а `if x` для проверки на truthiness.

---

## 2. Цикл for

Цикл `for` используется для итерации по последовательностям (списки, строки, словари и т.д.).

### 2.1 Базовый синтаксис

```python
# Итерация по списку
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Я люблю {fruit}")
```

**Output:**
```
Я люблю apple
Я люблю banana
Я люблю cherry
```

```python
# Итерация по строке
for char in "Python":
    print(char, end=" ")
print()
```

**Output:**
```
P y t h o n 
```

### 2.2 Функция range()

`range()` генерирует последовательность чисел:

```python
# range(stop) — от 0 до stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) — от start до stop-1
print("range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step) — с шагом
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Обратный порядок
print("range(5, 0, -1):")
for i in range(5, 0, -1):
    print(i, end=" ")
print()
```

**Output:**
```
range(5):
0 1 2 3 4 
range(2, 7):
2 3 4 5 6 
range(0, 10, 2):
0 2 4 6 8 
range(5, 0, -1):
5 4 3 2 1 
```

### 2.3 Функция enumerate()

`enumerate()` предоставляет индекс вместе со значением:

```python
fruits = ["apple", "banana", "cherry"]

# Без enumerate (плохо)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print()

# С enumerate (хорошо)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print()

# Начиная с другого индекса
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**
```
0: apple
1: banana
2: cherry

0: apple
1: banana
2: cherry

1. apple
2. banana
3. cherry
```

### 2.4 Итерация по словарям

```python
person = {"name": "Alice", "age": 30, "city": "Moscow"}

# По ключам (по умолчанию)
print("Ключи:")
for key in person:
    print(f"  {key}")

# По значениям
print("\nЗначения:")
for value in person.values():
    print(f"  {value}")

# По парам ключ-значение
print("\nПары:")
for key, value in person.items():
    print(f"  {key}: {value}")
```

**Output:**
```
Ключи:
  name
  age
  city

Значения:
  Alice
  30
  Moscow

Пары:
  name: Alice
  age: 30
  city: Moscow
```

### 2.5 Функция zip()

`zip()` объединяет несколько итерируемых объектов:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Moscow", "London", "Paris"]

# Параллельная итерация
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print()

# Несколько последовательностей
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
```

**Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old

Alice, 25, Moscow
Bob, 30, London
Charlie, 35, Paris
```

> **⚠️ Warning:**  
> `zip()` останавливается на самой короткой последовательности. Используйте `itertools.zip_longest()` для заполнения пропусков.

```python
from itertools import zip_longest

short = [1, 2]
long = [10, 20, 30, 40]

print("zip (короткая):")
for a, b in zip(short, long):
    print(f"  {a}, {b}")

print("\nzip_longest:")
for a, b in zip_longest(short, long, fillvalue=0):
    print(f"  {a}, {b}")
```

**Output:**
```
zip (короткая):
  1, 10
  2, 20

zip_longest:
  1, 10
  2, 20
  0, 30
  0, 40
```

### 2.6 Comprehensions

List, dict, set comprehensions — элегантные способы создания коллекций:

```python
# List comprehension
squares = [x**2 for x in range(10)]
print(f"Квадраты: {squares}")

# С условием
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Чётные квадраты: {even_squares}")

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}
print(f"Словарь квадратов: {square_dict}")

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "hi", "bye"]}
print(f"Уникальные длины: {unique_lengths}")

# Generator expression (ленивое вычисление)
sum_of_squares = sum(x**2 for x in range(1000000))
print(f"Сумма квадратов: {sum_of_squares}")
```

**Output:**
```
Квадраты: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Чётные квадраты: [0, 4, 16, 36, 64]
Словарь квадратов: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Уникальные длины: {2, 3, 5}
Сумма квадратов: 333332833333500000
```

---

## 3. Цикл while

Цикл `while` выполняется пока условие истинно.

### 3.1 Базовый синтаксис

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print("Цикл завершён")
```

**Output:**
```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
Цикл завершён
```

### 3.2 Практические примеры

**Ввод с валидацией:**

```python
# Симуляция ввода
inputs = iter(["", "abc", "25"])

def get_input():
    return next(inputs)

while True:
    user_input = get_input()
    if user_input.isdigit():
        age = int(user_input)
        break
    print(f"'{user_input}' — не число, попробуйте снова")

print(f"Ваш возраст: {age}")
```

**Output:**
```
'' — не число, попробуйте снова
'abc' — не число, попробуйте снова
Ваш возраст: 25
```

**Счётчик с условием:**

```python
total = 0
n = 1

while total < 100:
    total += n
    n += 1

print(f"Сумма {n-1} чисел = {total}")
print(f"Первое число, дающее сумму >= 100: {n-1}")
```

**Output:**
```
Сумма 14 чисел = 105
Первое число, дающее сумму >= 100: 14
```

### 3.3 Бесконечный цикл

Иногда бесконечный цикл — то, что нужно:

```python
import time

# Пример серверного цикла (симуляция)
max_iterations = 3
iteration = 0

while True:
    print(f"Сервер работает... (итерация {iteration + 1})")
    iteration += 1
    
    if iteration >= max_iterations:
        print("Демонстрация завершена")
        break
    
    time.sleep(0.1)  # Пауза 0.1 секунды
```

**Output:**
```
Сервер работает... (итерация 1)
Сервер работает... (итерация 2)
Сервер работает... (итерация 3)
Демонстрация завершена
```

> **⚠️ Warning:**  
> Всегда убедитесь, что у бесконечного цикла есть условие выхода (break), иначе программа зависнет!

---

## 4. Управление циклами

### 4.1 Оператор break

`break` прерывает цикл полностью:

```python
# Поиск элемента
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7

for num in numbers:
    print(f"Проверяем {num}...")
    if num == target:
        print(f"Найдено: {target}")
        break

print("Поиск завершён")
```

**Output:**
```
Проверяем 1...
Проверяем 3...
Проверяем 5...
Проверяем 7...
Найдено: 7
Поиск завершён
```

### 4.2 Оператор continue

`continue` переходит к следующей итерации:

```python
# Пропуск чётных чисел
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
```

**Output:**
```
1 3 5 7 9 
```

**Пример: Обработка данных с пропуском ошибок**

```python
data = ["10", "abc", "20", "", "30", "xyz"]

valid_numbers = []
for item in data:
    if not item:  # Пропуск пустых строк
        continue
    if not item.isdigit():  # Пропуск не-чисел
        print(f"Пропущено: '{item}'")
        continue
    valid_numbers.append(int(item))

print(f"Валидные числа: {valid_numbers}")
```

**Output:**
```
Пропущено: 'abc'
Пропущено: 'xyz'
Валидные числа: [10, 20, 30]
```

### 4.3 else в циклах

Блок `else` выполняется, если цикл завершился нормально (без break):

```python
# Поиск с else
def find_prime(numbers):
    for num in numbers:
        if is_prime(num):
            print(f"Найдено простое число: {num}")
            break
    else:
        print("Простых чисел не найдено")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Тест 1: есть простое число
find_prime([4, 6, 8, 11, 12])

# Тест 2: нет простых чисел
find_prime([4, 6, 8, 10, 12])
```

**Output:**
```
Найдено простое число: 11
Простых чисел не найдено
```

**else в while:**

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Цикл завершён нормально")
```

**Output:**
```
Count: 0
Count: 1
Count: 2
Цикл завершён нормально
```

### 4.4 Вложенные циклы с break

`break` прерывает только внутренний цикл:

```python
# Поиск в матрице
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5

found = False
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == target:
            print(f"Найдено {target} в позиции [{i}][{j}]")
            found = True
            break
    if found:
        break

if not found:
    print(f"{target} не найден")
```

**Output:**
```
Найдено 5 в позиции [1][1]
```

**Альтернатива: использование функции**

```python
def find_in_matrix(matrix, target):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)
    return None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = find_in_matrix(matrix, 5)

if result:
    print(f"Найдено в позиции {result}")
else:
    print("Не найдено")
```

**Output:**
```
Найдено в позиции (1, 1)
```

---

## 5. Pattern Matching (Python 3.10+)

### 5.1 Базовый match/case

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))
print(http_status(404))
print(http_status(999))
```

**Output:**
```
OK
Not Found
Unknown Status
```

### 5.2 Сопоставление с образцами

```python
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Выход из программы"
        case ["hello", name]:
            return f"Привет, {name}!"
        case ["add", x, y]:
            return f"Сумма: {int(x) + int(y)}"
        case ["hello", *names]:
            return f"Привет всем: {', '.join(names)}"
        case _:
            return "Неизвестная команда"

print(process_command("quit"))
print(process_command("hello World"))
print(process_command("add 5 3"))
print(process_command("hello Alice Bob Charlie"))
```

**Output:**
```
Выход из программы
Привет, World!
Сумма: 8
Привет всем: Alice, Bob, Charlie
```

### 5.3 Сопоставление с условиями (guards)

```python
def classify_point(point):
    match point:
        case (0, 0):
            return "Начало координат"
        case (x, 0):
            return f"На оси X, x={x}"
        case (0, y):
            return f"На оси Y, y={y}"
        case (x, y) if x == y:
            return f"На диагонали, x=y={x}"
        case (x, y):
            return f"Точка ({x}, {y})"

print(classify_point((0, 0)))
print(classify_point((5, 0)))
print(classify_point((0, 3)))
print(classify_point((4, 4)))
print(classify_point((2, 7)))
```

**Output:**
```
Начало координат
На оси X, x=5
На оси Y, y=3
На диагонали, x=y=4
Точка (2, 7)
```

### 5.4 Сопоставление словарей

```python
def process_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"Клик в ({x}, {y})"
        case {"type": "keypress", "key": key}:
            return f"Нажата клавиша: {key}"
        case {"type": "scroll", "direction": d}:
            return f"Скролл: {d}"
        case _:
            return "Неизвестное событие"

print(process_event({"type": "click", "x": 100, "y": 200}))
print(process_event({"type": "keypress", "key": "Enter"}))
print(process_event({"type": "scroll", "direction": "up"}))
```

**Output:**
```
Клик в (100, 200)
Нажата клавиша: Enter
Скролл: up
```

---

## 6. Практические паттерны

### 6.1 Фильтрация данных

```python
# Фильтрация с циклом
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Способ 1: цикл с append
positive = []
for n in numbers:
    if n > 0:
        positive.append(n)
print(f"Положительные (цикл): {positive}")

# Способ 2: list comprehension (предпочтительно)
positive = [n for n in numbers if n > 0]
print(f"Положительные (comprehension): {positive}")

# Способ 3: filter()
positive = list(filter(lambda n: n > 0, numbers))
print(f"Положительные (filter): {positive}")
```

**Output:**
```
Положительные (цикл): [1, 3, 5, 7, 9]
Положительные (comprehension): [1, 3, 5, 7, 9]
Положительные (filter): [1, 3, 5, 7, 9]
```

### 6.2 Преобразование данных

```python
# Преобразование списка словарей
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Извлечение имён
names = [user["name"] for user in users]
print(f"Имена: {names}")

# Фильтрация + преобразование
adult_names = [user["name"] for user in users if user["age"] >= 30]
print(f"Взрослые: {adult_names}")

# Создание нового списка словарей
summaries = [
    {"name": user["name"], "adult": user["age"] >= 18}
    for user in users
]
print(f"Summaries: {summaries}")
```

**Output:**
```
Имена: ['Alice', 'Bob', 'Charlie']
Взрослые: ['Alice', 'Charlie']
Summaries: [{'name': 'Alice', 'adult': True}, {'name': 'Bob', 'adult': True}, {'name': 'Charlie', 'adult': True}]
```

### 6.3 Агрегация данных

```python
# Подсчёт элементов
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Способ 1: цикл
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(f"Подсчёт (цикл): {counts}")

# Способ 2: dict.get()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"Подсчёт (get): {counts}")

# Способ 3: Counter (предпочтительно)
from collections import Counter
counts = Counter(words)
print(f"Подсчёт (Counter): {dict(counts)}")
```

**Output:**
```
Подсчёт (цикл): {'apple': 3, 'banana': 2, 'cherry': 1}
Подсчёт (get): {'apple': 3, 'banana': 2, 'cherry': 1}
Подсчёт (Counter): {'apple': 3, 'banana': 2, 'cherry': 1}
```

### 6.4 Группировка данных

```python
from collections import defaultdict

# Группировка по первой букве
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

groups = defaultdict(list)
for word in words:
    first_letter = word[0]
    groups[first_letter].append(word)

print("Группировка по первой букве:")
for letter, word_list in sorted(groups.items()):
    print(f"  {letter}: {word_list}")
```

**Output:**
```
Группировка по первой букве:
  a: ['apple', 'apricot', 'avocado']
  b: ['banana', 'blueberry']
  c: ['cherry']
```

---

## 7. Common Pitfalls

### 7.1 Модификация списка во время итерации

❌ **Ошибка:**
```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)  # Опасно!
print(numbers)  # [1, 3, 5]? Нет, может быть неожиданный результат!
```

✅ **Правильно:**
```python
# Создаём новый список
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)

# Или итерируем по копии
numbers = [1, 2, 3, 4, 5]
for n in numbers.copy():
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)
```

**Output:**
```
[1, 3, 5]
[1, 3, 5]
```

### 7.2 Забытый break в while True

❌ **Ошибка:**
```python
# Это зависнет!
# while True:
#     print("Бесконечный цикл!")
```

✅ **Правильно:**
```python
count = 0
while True:
    print(f"Итерация {count}")
    count += 1
    if count >= 3:
        break  # Не забываем условие выхода!
```

**Output:**
```
Итерация 0
Итерация 1
Итерация 2
```

### 7.3 Использование range(len()) вместо enumerate

❌ **Не идиоматично:**
```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

✅ **Pythonic:**
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### 7.4 Слишком сложные comprehensions

❌ **Трудно читать:**
```python
result = [[x*y for y in range(1,4) if y != x] for x in range(1,4) if x > 1]
```

✅ **Читаемо:**
```python
result = []
for x in range(1, 4):
    if x > 1:
        row = []
        for y in range(1, 4):
            if y != x:
                row.append(x * y)
        result.append(row)
print(result)
```

**Output:**
```
[[2, 6], [3, 6]]
```

---

## 8. Производительность

### 8.1 Выбор структуры цикла

```python
import time

# Тест производительности
def test_loop_performance():
    data = list(range(1000000))
    
    # for цикл с append
    start = time.time()
    result = []
    for x in data:
        result.append(x * 2)
    loop_time = time.time() - start
    
    # List comprehension
    start = time.time()
    result = [x * 2 for x in data]
    comp_time = time.time() - start
    
    # map()
    start = time.time()
    result = list(map(lambda x: x * 2, data))
    map_time = time.time() - start
    
    print(f"for + append: {loop_time:.4f}s")
    print(f"comprehension: {comp_time:.4f}s")
    print(f"map(): {map_time:.4f}s")

test_loop_performance()
```

**Output:**
```
for + append: 0.0892s
comprehension: 0.0524s
map(): 0.0687s
```

> **💡 Pro Tip:**  
> List comprehensions обычно быстрее обычных циклов с append. Используйте их для простых преобразований.

### 8.2 Раннее прерывание

```python
# Поиск первого совпадения
def find_first(items, predicate):
    for item in items:
        if predicate(item):
            return item  # Ранний выход
    return None

# Вместо обработки всего списка
numbers = list(range(1000000))
result = find_first(numbers, lambda x: x > 100)
print(f"First > 100: {result}")  # Быстро!
```

**Output:**
```
First > 100: 101
```

---

## 💡 Key Takeaways

- **if/elif/else**: Используйте для ветвления логики. Избегайте глубокой вложенности — применяйте ранний return.

- **for vs while**: `for` для итерации по известным последовательностям, `while` когда условие выхода неизвестно заранее.

- **break и continue**: `break` прерывает цикл, `continue` пропускает итерацию. Используйте умеренно.

- **Comprehensions**: Предпочитайте list/dict/set comprehensions обычным циклам для создания коллекций. Но не жертвуйте читаемостью.

- **Pattern matching**: Python 3.10+ предоставляет мощный match/case для сопоставления с образцами.

---

## 🚀 Next Steps

**Related Modules:**
- [Functions](../04_Functions/) — создание функций для инкапсуляции логики
- [Exceptions](../07_Exceptions/) — обработка ошибок в циклах

**Practice Ideas:**
1. Напишите программу "Угадай число" с использованием while
2. Создайте FizzBuzz (числа от 1 до 100: Fizz для кратных 3, Buzz для кратных 5)
3. Реализуйте поиск простых чисел в диапазоне с помощью решета Эратосфена
4. Напишите валидатор пароля с несколькими проверками

**Going Deeper:**
- Изучите itertools для продвинутой работы с итераторами
- Познакомьтесь с генераторами и yield
- Изучите асинхронные циклы (async for)

---

## 📚 Additional Resources

**Documentation:**
- [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [Pattern Matching (PEP 634)](https://peps.python.org/pep-0634/)

**Articles:**
- [Python Loop Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

---

