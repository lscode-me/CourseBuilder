# Python Standard Library
## Обзор самых важных модулей стандартной библиотеки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь импортировать и использовать модули
- Знать работу с файлами и исключениями
- Понимать ООП и создание классов
- Иметь опыт работы с коллекциями данных

**Recommended prior modules:**

- [Modules](../06_Modules/) — организация кода в модули
- [Files](../08_Files/) — работа с файлами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать datetime для работы с датами и временем
- Применять collections для продвинутых структур данных
- Работать с регулярными выражениями (re)
- Использовать subprocess для запуска внешних команд
- Применять logging для отладки и мониторинга
- Работать с os и sys для системных операций

---

## 1. datetime — дата и время

### 1.1 Основные классы

```python

from datetime import datetime, date, time, timedelta

# Текущая дата и время
now = datetime.now()
print(f"Сейчас: {now}")

# Только дата
today = date.today()
print(f"Сегодня: {today}")

# Создание конкретной даты/времени
birthday = datetime(1990, 5, 15, 10, 30)
print(f"День рождения: {birthday}")

# Компоненты даты
print(f"Год: {now.year}")
print(f"Месяц: {now.month}")
print(f"День: {now.day}")
print(f"Час: {now.hour}")
print(f"День недели: {now.weekday()}")  # 0 = понедельник

```

**Output:**
```

Сейчас: 2024-12-02 15:30:45.123456
Сегодня: 2024-12-02
День рождения: 1990-05-15 10:30:00
Год: 2024
Месяц: 12
День: 2
Час: 15
День недели: 0

```

### 1.2 Форматирование и парсинг

```python

from datetime import datetime

now = datetime.now()

# Форматирование (datetime → строка)
print(now.strftime("%Y-%m-%d"))           # 2024-12-02
print(now.strftime("%d.%m.%Y %H:%M"))     # 02.12.2024 15:30
print(now.strftime("%A, %B %d, %Y"))      # Monday, December 02, 2024

# Парсинг (строка → datetime)
date_str = "2024-12-25 18:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"Распарсено: {parsed}")

# ISO формат
print(f"ISO: {now.isoformat()}")
parsed_iso = datetime.fromisoformat("2024-12-25T18:30:00")
print(f"Из ISO: {parsed_iso}")

```

**Output:**
```

2024-12-02
02.12.2024 15:30
Monday, December 02, 2024
Распарсено: 2024-12-25 18:30:00
ISO: 2024-12-02T15:30:45.123456
Из ISO: 2024-12-25 18:30:00

```

### 1.3 Арифметика с датами

```python

from datetime import datetime, timedelta

now = datetime.now()

# timedelta — разница во времени
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
one_hour = timedelta(hours=1)

# Прибавление/вычитание
tomorrow = now + one_day
last_week = now - one_week
print(f"Завтра: {tomorrow}")
print(f"Неделю назад: {last_week}")

# Разница между датами
christmas = datetime(2024, 12, 25)
until_christmas = christmas - now
print(f"До Рождества: {until_christmas.days} дней")

# Сравнение дат
if now < christmas:
    print("Рождество ещё впереди!")

```

**Output:**
```

Завтра: 2024-12-03 15:30:45.123456
Неделю назад: 2024-11-25 15:30:45.123456
До Рождества: 22 дней
Рождество ещё впереди!

```

### 1.4 Часовые пояса

```python

from datetime import datetime, timezone, timedelta

# UTC
utc_now = datetime.now(timezone.utc)
print(f"UTC: {utc_now}")

# Создание часового пояса
moscow_tz = timezone(timedelta(hours=3))
moscow_time = datetime.now(moscow_tz)
print(f"Москва: {moscow_time}")

# Конвертация между зонами
utc_time = datetime(2024, 12, 25, 12, 0, tzinfo=timezone.utc)
moscow_converted = utc_time.astimezone(moscow_tz)
print(f"12:00 UTC в Москве: {moscow_converted}")

```

**Output:**
```

UTC: 2024-12-02 12:30:45.123456+00:00
Москва: 2024-12-02 15:30:45.123456+03:00
12:00 UTC в Москве: 2024-12-25 15:00:00+03:00

```

---

## 2. collections — продвинутые коллекции

### 2.1 Counter

```python

from collections import Counter

# Подсчёт элементов
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Counter: {word_count}")

# Наиболее частые
print(f"Top 2: {word_count.most_common(2)}")

# Подсчёт символов в строке
char_count = Counter("mississippi")
print(f"Символы: {char_count}")

# Операции с Counter
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")

```

**Output:**
```

Counter: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
Top 2: [('apple', 3), ('banana', 2)]
Символы: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c1 + c2: Counter({'a': 4, 'b': 3})
c1 - c2: Counter({'a': 2})

```

### 2.2 defaultdict

```python

from collections import defaultdict

# Значение по умолчанию — list
groups = defaultdict(list)
for item in [("A", 1), ("B", 2), ("A", 3), ("B", 4)]:
    groups[item[0]].append(item[1])
print(f"groups: {dict(groups)}")

# Значение по умолчанию — int (0)
counts = defaultdict(int)
for word in "hello world".split():
    counts[word] += 1
print(f"counts: {dict(counts)}")

# Вложенные defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested["users"]["alice"] += 1
nested["users"]["bob"] += 2
nested["admins"]["charlie"] += 1
print(f"nested: {dict(nested)}")

```

**Output:**
```

groups: {'A': [1, 3], 'B': [2, 4]}
counts: {'hello': 1, 'world': 1}
nested: {'users': defaultdict(<class 'int'>, {'alice': 1, 'bob': 2}), 'admins': defaultdict(<class 'int'>, {'charlie': 1})}

```

### 2.3 deque — двусторонняя очередь

```python

from collections import deque

# Создание
d = deque([1, 2, 3])

# Добавление с обоих концов
d.append(4)        # справа
d.appendleft(0)    # слева
print(f"После append: {d}")

# Удаление с обоих концов
right = d.pop()    # справа
left = d.popleft() # слева
print(f"После pop: {d}, удалено: {left}, {right}")

# Ротация
d = deque([1, 2, 3, 4, 5])
d.rotate(2)        # сдвиг вправо
print(f"rotate(2): {d}")
d.rotate(-2)       # сдвиг влево
print(f"rotate(-2): {d}")

# Ограничение размера
d = deque(maxlen=3)
for i in range(5):
    d.append(i)
    print(f"После добавления {i}: {list(d)}")

```

**Output:**
```

После append: deque([0, 1, 2, 3, 4])
После pop: deque([1, 2, 3]), удалено: 0, 4
rotate(2): deque([4, 5, 1, 2, 3])
rotate(-2): deque([1, 2, 3, 4, 5])
После добавления 0: [0]
После добавления 1: [0, 1]
После добавления 2: [0, 1, 2]
После добавления 3: [1, 2, 3]
После добавления 4: [2, 3, 4]

```

### 2.4 namedtuple и OrderedDict

```python

from collections import namedtuple, OrderedDict

# namedtuple — именованный кортеж
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"Point: {p}")
print(f"x={p.x}, y={p.y}")
print(f"Как кортеж: {p[0]}, {p[1]}")

# С значениями по умолчанию
Person = namedtuple('Person', ['name', 'age', 'city'], defaults=['Unknown'])
alice = Person('Alice', 30)
print(f"Person: {alice}")

# OrderedDict (в Python 3.7+ обычные dict сохраняют порядок)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
od.move_to_end('first')  # Перемещение в конец
print(f"OrderedDict: {od}")

```

**Output:**
```

Point: Point(x=3, y=4)
x=3, y=4
Как кортеж: 3, 4
Person: Person(name='Alice', age=30, city='Unknown')
OrderedDict: OrderedDict([('second', 2), ('third', 3), ('first', 1)])

```

---

## 3. re — регулярные выражения

### 3.1 Базовые операции

```python

import re

text = "Contact us at support@example.com or sales@company.org"

# search — первое совпадение
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(f"Найдено: {match.group()}")

# findall — все совпадения
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"Все email: {emails}")

# finditer — итератор совпадений
for match in re.finditer(r'\w+@\w+\.\w+', text):
    print(f"  Позиция {match.start()}-{match.end()}: {match.group()}")

```

**Output:**
```

Найдено: support@example.com
Все email: ['support@example.com', 'sales@company.org']
  Позиция 14-33: support@example.com
  Позиция 37-54: sales@company.org

```

### 3.2 Группы захвата

```python

import re

text = "John Smith (30), Jane Doe (25)"

# Группы с именами
pattern = r'(?P<name>\w+ \w+) \((?P<age>\d+)\)'
for match in re.finditer(pattern, text):
    print(f"Имя: {match.group('name')}, Возраст: {match.group('age')}")

# Группы без имён
pattern = r'(\w+) (\w+) \((\d+)\)'
matches = re.findall(pattern, text)
print(f"Кортежи: {matches}")

```

**Output:**
```

Имя: John Smith, Возраст: 30
Имя: Jane Doe, Возраст: 25
Кортежи: [('John', 'Smith', '30'), ('Jane', 'Doe', '25')]

```

### 3.3 Замена и разделение

```python

import re

text = "Hello   World!   How    are   you?"

# sub — замена
cleaned = re.sub(r'\s+', ' ', text)
print(f"Убраны лишние пробелы: '{cleaned}'")

# Замена с функцией
def upper_match(match):
    return match.group().upper()

result = re.sub(r'\b\w{4}\b', upper_match, "This is a test case")
print(f"Слова из 4 букв в верхнем регистре: '{result}'")

# split — разделение
parts = re.split(r'[,;]\s*', "apple, banana; cherry, date")
print(f"Разделено: {parts}")

```

**Output:**
```

Убраны лишние пробелы: 'Hello World! How are you?'
Слова из 4 букв в верхнем регистре: 'THIS is a TEST CASE'
Разделено: ['apple', 'banana', 'cherry', 'date']

```

### 3.4 Компиляция паттернов

```python

import re

# Компиляция для повторного использования
email_pattern = re.compile(r'''
    (?P<user>[\w.+-]+)    # Имя пользователя
    @                      # Символ @
    (?P<domain>[\w.-]+)   # Домен
    \.                     # Точка
    (?P<tld>\w{2,})       # TLD (минимум 2 символа)
''', re.VERBOSE)

text = "Contact: john@example.com, jane.doe@company.co.uk"

for match in email_pattern.finditer(text):
    print(f"User: {match.group('user')}, Domain: {match.group('domain')}.{match.group('tld')}")

```

**Output:**
```

User: john, Domain: example.com
User: jane.doe, Domain: company.co.uk

```

---

## 4. subprocess — запуск внешних команд

### 4.1 Базовое использование

```python

import subprocess

# run() — простой запуск
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print(f"stdout: {result.stdout}")
print(f"return code: {result.returncode}")

# Проверка ошибок
result = subprocess.run(["ls", "-la", "/tmp"], capture_output=True, text=True)
if result.returncode == 0:
    print("Команда выполнена успешно")
    print(result.stdout[:200] + "...")
else:
    print(f"Ошибка: {result.stderr}")

```

**Output:**
```

stdout: Hello, World!

return code: 0
Команда выполнена успешно
total 48
drwxrwxrwt 12 root root 4096 Dec  2 15:30 .
drwxr-xr-x 23 root root 4096 Dec  1 10:00 ..
...

```

### 4.2 Передача данных

```python

import subprocess

# stdin
result = subprocess.run(
    ["grep", "error"],
    input="info: ok\nerror: failed\ninfo: done\nerror: timeout\n",
    capture_output=True,
    text=True
)
print(f"Строки с 'error':\n{result.stdout}")

# shell=True (осторожно с пользовательским вводом!)
result = subprocess.run(
    "echo $HOME && pwd",
    shell=True,
    capture_output=True,
    text=True
)
print(f"Shell команда:\n{result.stdout}")

```

**Output:**
```

Строки с 'error':
error: failed
error: timeout

Shell команда:
/home/user
/home/user/project

```

### 4.3 Пайплайны

```python

import subprocess

# Пайплайн: ps aux | grep python | head -5
ps = subprocess.Popen(
    ["ps", "aux"],
    stdout=subprocess.PIPE
)
grep = subprocess.Popen(
    ["grep", "python"],
    stdin=ps.stdout,
    stdout=subprocess.PIPE
)
head = subprocess.Popen(
    ["head", "-5"],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
    text=True
)

ps.stdout.close()
grep.stdout.close()

output, _ = head.communicate()
print(f"Python процессы:\n{output}")

```

---

## 5. logging — логирование

### 5.1 Базовая настройка

```python

import logging

# Простая настройка
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Разные уровни логирования
logger.debug("Отладочное сообщение")
logger.info("Информационное сообщение")
logger.warning("Предупреждение")
logger.error("Ошибка")
logger.critical("Критическая ошибка")

```

**Output:**
```

2024-12-02 15:30:00,123 - __main__ - DEBUG - Отладочное сообщение
2024-12-02 15:30:00,123 - __main__ - INFO - Информационное сообщение
2024-12-02 15:30:00,123 - __main__ - WARNING - Предупреждение
2024-12-02 15:30:00,123 - __main__ - ERROR - Ошибка
2024-12-02 15:30:00,123 - __main__ - CRITICAL - Критическая ошибка

```

### 5.2 Логирование в файл

```python

import logging

# Создаём logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Handler для файла
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Handler для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Форматирование
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Использование
logger.debug("Debug — только в файл с уровнем DEBUG")
logger.info("Info — в файл")
logger.warning("Warning — в файл и консоль")
logger.error("Error — в файл и консоль")

```

### 5.3 Логирование исключений

```python

import logging

logger = logging.getLogger(__name__)

def risky_operation():
    return 1 / 0

try:
    risky_operation()
except ZeroDivisionError:
    logger.exception("Ошибка при выполнении операции")
    # exception() автоматически добавляет traceback
```

**Output:**
```

2024-12-02 15:30:00,123 - __main__ - ERROR - Ошибка при выполнении операции
Traceback (most recent call last):
  File "example.py", line 8, in <module>
    risky_operation()
  File "example.py", line 5, in risky_operation
    return 1 / 0
ZeroDivisionError: division by zero

```

---

## 6. os и sys — системные операции

### 6.1 Модуль os

```python

import os

# Информация о системе
print(f"OS: {os.name}")  # posix, nt
print(f"CWD: {os.getcwd()}")
print(f"CPU count: {os.cpu_count()}")

# Переменные окружения
print(f"HOME: {os.environ.get('HOME')}")
print(f"PATH: {os.environ.get('PATH', '')[:50]}...")

# Установка переменной окружения
os.environ['MY_VAR'] = 'value'
print(f"MY_VAR: {os.getenv('MY_VAR')}")

# Работа с директориями
os.makedirs("a/b/c", exist_ok=True)
print(f"Создано: {os.path.exists('a/b/c')}")
os.removedirs("a/b/c")

# Выполнение команды
exit_code = os.system("echo 'Hello from shell'")
print(f"Exit code: {exit_code}")

```

**Output:**
```

OS: posix
CWD: /home/user/project
CPU count: 8
HOME: /home/user
PATH: /usr/local/bin:/usr/bin:/bin:/usr/local/g...
MY_VAR: value
Создано: True
Hello from shell
Exit code: 0

```

### 6.2 os.path — работа с путями

```python

import os.path

path = "/home/user/documents/report.txt"

print(f"basename: {os.path.basename(path)}")    # report.txt
print(f"dirname: {os.path.dirname(path)}")      # /home/user/documents
print(f"split: {os.path.split(path)}")          # ('/home/user/documents', 'report.txt')
print(f"splitext: {os.path.splitext(path)}")    # ('/home/user/documents/report', '.txt')
print(f"isabs: {os.path.isabs(path)}")          # True
print(f"join: {os.path.join('/home', 'user', 'file.txt')}")

# Проверки
print(f"exists: {os.path.exists('/tmp')}")
print(f"isfile: {os.path.isfile('/tmp')}")
print(f"isdir: {os.path.isdir('/tmp')}")

```

**Output:**
```

basename: report.txt
dirname: /home/user/documents
split: ('/home/user/documents', 'report.txt')
splitext: ('/home/user/documents/report', '.txt')
isabs: True
join: /home/user/file.txt
exists: True
isfile: False
isdir: True

```

### 6.3 Модуль sys

```python

import sys

# Информация о Python
print(f"Version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")

# Пути импорта
print(f"Path (первые 3): {sys.path[:3]}")

# Аргументы командной строки
print(f"argv: {sys.argv}")

# Размер объектов
lst = [1, 2, 3, 4, 5]
print(f"Размер списка: {sys.getsizeof(lst)} bytes")

# Выход с кодом
# sys.exit(0)  # Успех
# sys.exit(1)  # Ошибка
```

**Output:**
```

Version: 3.11.5 (main, Aug 25 2023, 13:19:05)
Platform: linux
Executable: /usr/bin/python3
Path (первые 3): ['', '/usr/lib/python311.zip', '/usr/lib/python3.11']
argv: ['example.py']
Размер списка: 120 bytes

```

---

## 7. itertools — итераторы

### 7.1 Комбинаторные функции

```python

from itertools import permutations, combinations, product

# Перестановки
print(f"permutations('AB'): {list(permutations('AB'))}")
print(f"permutations('ABC', 2): {list(permutations('ABC', 2))}")

# Комбинации
print(f"combinations('ABCD', 2): {list(combinations('ABCD', 2))}")

# Декартово произведение
print(f"product('AB', '12'): {list(product('AB', '12'))}")
print(f"product([0,1], repeat=3): {list(product([0, 1], repeat=3))}")

```

**Output:**
```

permutations('AB'): [('A', 'B'), ('B', 'A')]
permutations('ABC', 2): [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
combinations('ABCD', 2): [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
product('AB', '12'): [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
product([0,1], repeat=3): [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

```

### 7.2 Бесконечные итераторы

```python

from itertools import count, cycle, repeat, islice

# count — бесконечный счётчик
counter = count(start=10, step=2)
print(f"count(10, 2): {list(islice(counter, 5))}")

# cycle — бесконечный цикл
colors = cycle(['red', 'green', 'blue'])
print(f"cycle: {[next(colors) for _ in range(7)]}")

# repeat — повторение
print(f"repeat('A', 3): {list(repeat('A', 3))}")

```

**Output:**
```

count(10, 2): [10, 12, 14, 16, 18]
cycle: ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']
repeat('A', 3): ['A', 'A', 'A']

```

### 7.3 Полезные функции

```python

from itertools import chain, groupby, accumulate, takewhile, dropwhile

# chain — объединение итераторов
print(f"chain: {list(chain([1, 2], [3, 4], [5]))}")

# groupby — группировка
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
data.sort(key=lambda x: x[0])  # Важно: данные должны быть отсортированы!
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# accumulate — накопление
print(f"accumulate: {list(accumulate([1, 2, 3, 4, 5]))}")

# takewhile / dropwhile
nums = [1, 3, 5, 7, 2, 4, 6]
print(f"takewhile(x<6): {list(takewhile(lambda x: x < 6, nums))}")
print(f"dropwhile(x<6): {list(dropwhile(lambda x: x < 6, nums))}")

```

**Output:**
```

chain: [1, 2, 3, 4, 5]
  A: [('A', 1), ('A', 2), ('A', 5)]
  B: [('B', 3), ('B', 4)]
accumulate: [1, 3, 6, 10, 15]
takewhile(x<6): [1, 3, 5]
dropwhile(x<6): [7, 2, 4, 6]

```

---

## 8. functools — инструменты для функций

### 8.1 lru_cache

```python

from functools import lru_cache
import time

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Без кэша было бы очень медленно
start = time.time()
result = fibonacci(100)
print(f"fib(100) = {result}")
print(f"Время: {time.time() - start:.6f}с")

# Статистика кэша
print(f"Статистика: {fibonacci.cache_info()}")

```

**Output:**
```

fib(100) = 354224848179261915075
Время: 0.000123с
Статистика: CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

```

### 8.2 partial

```python

from functools import partial

def power(base, exponent):
    return base ** exponent

# Создаём специализированные функции
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5) = {square(5)}")
print(f"cube(5) = {cube(5)}")

# Полезно с функциями высшего порядка
numbers = [1, 2, 3, 4, 5]
squared = list(map(partial(power, exponent=2), numbers))
print(f"Квадраты: {squared}")

```

**Output:**
```

square(5) = 25
cube(5) = 125
Квадраты: [1, 4, 9, 16, 25]

```

### 8.3 reduce

```python

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Сумма
total = reduce(lambda a, b: a + b, numbers)
print(f"Сумма: {total}")

# Произведение
product = reduce(lambda a, b: a * b, numbers)
print(f"Произведение: {product}")

# Максимум (с начальным значением)
maximum = reduce(lambda a, b: a if a > b else b, numbers, 0)
print(f"Максимум: {maximum}")

# Построение словаря
pairs = [('a', 1), ('b', 2), ('c', 3)]
d = reduce(lambda acc, pair: {**acc, pair[0]: pair[1]}, pairs, {})
print(f"Словарь: {d}")

```

**Output:**
```

Сумма: 15
Произведение: 120
Максимум: 5
Словарь: {'a': 1, 'b': 2, 'c': 3}

```

---

## 9. Другие полезные модули

### 9.1 hashlib — хэширование

```python

import hashlib

text = "Hello, World!"

# MD5 (не для безопасности!)
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"MD5: {md5_hash}")

# SHA-256 (безопасный)
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print(f"SHA256: {sha256_hash}")

# Хэширование файла
def hash_file(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

# file_hash = hash_file('document.pdf')
```

**Output:**
```

MD5: 65a8e27d8879283831b664bd8b7f0ad4
SHA256: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

```

### 9.2 uuid — уникальные идентификаторы

```python

import uuid

# UUID4 — случайный
print(f"UUID4: {uuid.uuid4()}")
print(f"UUID4: {uuid.uuid4()}")

# UUID1 — на основе времени и MAC-адреса
print(f"UUID1: {uuid.uuid1()}")

# UUID из строки
u = uuid.UUID('12345678-1234-5678-1234-567812345678')
print(f"Из строки: {u}")
print(f"Hex: {u.hex}")
print(f"Bytes: {len(u.bytes)} bytes")

```

**Output:**
```

UUID4: 550e8400-e29b-41d4-a716-446655440000
UUID4: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
UUID1: 6ba7b810-9dad-11d1-80b4-00c04fd430c8
Из строки: 12345678-1234-5678-1234-567812345678
Hex: 12345678123456781234567812345678
Bytes: 16 bytes

```

### 9.3 random — случайные числа

```python

import random

# Целые числа
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randrange(0, 100, 5): {random.randrange(0, 100, 5)}")

# Вещественные числа
print(f"random(): {random.random():.4f}")
print(f"uniform(1, 10): {random.uniform(1, 10):.4f}")

# Выбор из последовательности
items = ['apple', 'banana', 'cherry', 'date']
print(f"choice: {random.choice(items)}")
print(f"choices (k=3): {random.choices(items, k=3)}")
print(f"sample (k=2): {random.sample(items, k=2)}")

# Перемешивание
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"shuffle: {numbers}")

# Воспроизводимость
random.seed(42)
print(f"seed(42): {[random.randint(1, 100) for _ in range(5)]}")

```

**Output:**
```

randint(1, 10): 7
randrange(0, 100, 5): 45
random(): 0.8234
uniform(1, 10): 5.6789
choice: banana
choices (k=3): ['apple', 'cherry', 'apple']
sample (k=2): ['date', 'banana']
shuffle: [3, 1, 4, 5, 2]
seed(42): [82, 15, 4, 95, 36]

```

---

## 💡 Key Takeaways

- **datetime**: Всегда используйте timezone-aware даты в production. `strptime`/`strftime` для парсинга и форматирования.

- **collections**: `Counter` для подсчёта, `defaultdict` для автоматических значений, `deque` для очередей.

- **re**: Компилируйте паттерны для повторного использования. Используйте `re.VERBOSE` для читаемости.

- **logging**: Используйте вместо `print()`. Настройте разные handlers для разных уровней и целей.

- **itertools**: Экономит память и код. `chain`, `groupby`, `product` решают многие задачи элегантно.

---

## 🚀 Next Steps

**Related Modules:**

- [Additional Modules](../10_AdditionalModules/) — популярные pip-пакеты

**Practice Ideas:**

1. Создайте парсер логов с regex и группировкой по дате
2. Напишите скрипт мониторинга процессов с subprocess и logging
3. Реализуйте кэширование результатов функций с TTL
4. Создайте утилиту для поиска дубликатов файлов (hashlib)

**Going Deeper:**

- Изучите `asyncio` для асинхронного программирования
- Познакомьтесь с `multiprocessing` для параллельных вычислений
- Изучите `typing` для статической типизации

---

## 📚 Additional Resources

**Documentation:**

- [Python Standard Library](https://docs.python.org/3/library/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [re](https://docs.python.org/3/library/re.html)
- [logging](https://docs.python.org/3/library/logging.html)

**Tutorials:**

- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)

---




