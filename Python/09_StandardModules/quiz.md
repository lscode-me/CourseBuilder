# Python Standard Library Modules - Quiz

Проверьте свои знания по теме "Стандартные модули Python".

---

## Question 1: os модуль

Что возвращает `os.getcwd()`?

A) Список файлов в директории

B) Текущую рабочую директорию

C) Домашнюю директорию

D) Путь к Python

---

## Question 2: os.environ

Как получить значение переменной окружения?

A) `os.getenv('VAR')` или `os.environ.get('VAR')`

B) `os.environ.VAR`

C) `env.get('VAR')`

D) `getenv('VAR')`

---

## Question 3: sys модуль

Что содержит `sys.argv`?

A) Версию Python

B) Список аргументов командной строки

C) Пути к модулям

D) Системную информацию

---

## Question 4: sys.exit()

Что делает `sys.exit(0)`?

A) Перезапускает программу

B) Завершает программу с кодом 0 (успех)

C) Выводит сообщение об ошибке

D) Ничего

---

## Question 5: datetime

Как получить текущую дату и время?

A) `datetime.today()`

B) `datetime.datetime.now()`

C) `datetime.current()`

D) `time.now()`

---

## Question 6: Форматирование даты

Какой метод форматирует datetime в строку?

A) `format()`

B) `strftime()`

C) `to_string()`

D) `str()`

---

## Question 7: Парсинг даты

Какой метод парсит строку в datetime?

A) `parse()`

B) `strptime()`

C) `from_string()`

D) `datetime()`

---

## Question 8: timedelta

Что выведет следующий код?

```python
from datetime import datetime, timedelta
now = datetime(2024, 1, 15)
future = now + timedelta(days=30)
print(future.month)
```

A) 1

B) 2

C) 30

D) 45

---

## Question 9: re модуль

Какая функция ищет паттерн в любом месте строки?

A) `re.match()`

B) `re.search()`

C) `re.find()`

D) `re.locate()`

---

## Question 10: re.match vs re.search

В чём разница между `re.match()` и `re.search()`?

A) Нет разницы

B) `match()` ищет только в начале строки

C) `search()` ищет только в конце

D) `match()` быстрее

---

## Question 11: re.findall()

Что возвращает `re.findall()`?

A) Первое совпадение

B) Список всех совпадений

C) True/False

D) Итератор

---

## Question 12: Группы в регулярках

Как получить группу из match-объекта?

A) `match[1]`

B) `match.group(1)`

C) `match.get(1)`

D) `match.groups[1]`

---

## Question 13: json модуль

Что делает `json.dumps()`?

A) Загружает JSON из файла

B) Сериализует Python-объект в JSON-строку

C) Десериализует JSON-строку

D) Валидирует JSON

---

## Question 14: json.load vs json.loads

В чём разница?

A) `load()` из файла, `loads()` из строки

B) `loads()` быстрее

C) Нет разницы

D) `loads()` для списков

---

## Question 15: random модуль

Какая функция возвращает случайное float от 0 до 1?

A) `random.rand()`

B) `random.random()`

C) `random.float()`

D) `random.uniform(0, 1)`

---

## Question 16: random.choice()

Что делает `random.choice()`?

A) Выбирает несколько случайных элементов

B) Выбирает один случайный элемент

C) Перемешивает список

D) Генерирует случайное число

---

## Question 17: random.seed()

Зачем нужен `random.seed()`?

A) Для генерации случайных чисел

B) Для воспроизводимости случайной последовательности

C) Для увеличения случайности

D) Для криптографии

---

## Question 18: collections.Counter

Что выведет следующий код?

```python
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))
```

A) [('a', 5)]

B) {'a': 5}

C) 'a'

D) 5

---

## Question 19: collections.defaultdict

В чём преимущество `defaultdict`?

A) Быстрее обычного dict

B) Автоматически создаёт значение для несуществующего ключа

C) Сортирует ключи

D) Ограничивает размер

---

## Question 20: itertools

Какой модуль содержит `chain`, `cycle`, `combinations`?

A) `functools`

B) `itertools`

C) `collections`

D) `tools`

---

## Question 21: itertools.chain()

Что делает `itertools.chain()`?

A) Создаёт цепочку вызовов

B) Объединяет несколько итерируемых объектов в один

C) Связывает функции

D) Сортирует элементы

---

## Question 22: logging

Какой уровень логирования используется для отладочных сообщений?

A) `INFO`

B) `DEBUG`

C) `WARNING`

D) `TRACE`

---

## Question 23: logging уровни

Какой порядок уровней логирования (от низшего к высшему)?

A) DEBUG < INFO < WARNING < ERROR < CRITICAL

B) INFO < DEBUG < WARNING < ERROR < CRITICAL

C) WARNING < INFO < DEBUG < ERROR < CRITICAL

D) CRITICAL < ERROR < WARNING < INFO < DEBUG

---

## Question 24: argparse

Для чего используется модуль argparse?

A) Для парсинга JSON

B) Для парсинга аргументов командной строки

C) Для парсинга HTML

D) Для парсинга регулярных выражений

---

## Question 25: hashlib

Какой модуль используется для вычисления хэшей (MD5, SHA)?

A) `hash`

B) `hashlib`

C) `crypto`

D) `checksum`

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `getcwd()` = get current working directory. |
| 2 | A | `os.getenv()` или `os.environ.get()` безопасно получают переменную окружения. |
| 3 | B | `sys.argv` — список: [скрипт, арг1, арг2, ...]. `sys.argv[0]` — имя скрипта. |
| 4 | B | `sys.exit(0)` — успешное завершение. Ненулевой код означает ошибку. |
| 5 | B | `datetime.datetime.now()` или `datetime.now()` после `from datetime import datetime`. |
| 6 | B | `strftime()` (string format time) форматирует в строку. |
| 7 | B | `strptime()` (string parse time) парсит строку в datetime. |
| 8 | B | 15 января + 30 дней = 14 февраля, месяц = 2. |
| 9 | B | `search()` ищет в любом месте, `match()` — только в начале. |
| 10 | B | `match()` проверяет только начало строки. |
| 11 | B | `findall()` возвращает список всех неперекрывающихся совпадений. |
| 12 | B | `match.group(1)` возвращает первую группу. `group(0)` — всё совпадение. |
| 13 | B | `dumps` = dump string — сериализует в строку. |
| 14 | A | `load()` из file object, `loads()` из string. |
| 15 | B | `random.random()` — float в [0.0, 1.0). |
| 16 | B | `choice()` выбирает один элемент. `choices()` / `sample()` — несколько. |
| 17 | B | `seed()` инициализирует генератор для воспроизводимых результатов. |
| 18 | A | `most_common(n)` возвращает список кортежей [(element, count)]. |
| 19 | B | `defaultdict(list)` создаёт пустой список при обращении к несуществующему ключу. |
| 20 | B | `itertools` содержит функции для эффективной работы с итераторами. |
| 21 | B | `chain()` объединяет итерируемые объекты: `chain([1,2], [3,4])` → 1,2,3,4. |
| 22 | B | DEBUG — самый низкий уровень, для отладочной информации. |
| 23 | A | DEBUG (10) < INFO (20) < WARNING (30) < ERROR (40) < CRITICAL (50). |
| 24 | B | `argparse` — стандартный модуль для парсинга CLI-аргументов. |
| 25 | B | `hashlib` предоставляет хэш-алгоритмы: md5, sha256 и др. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание стандартной библиотеки! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите datetime и logging. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на регулярные выражения и collections. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Практикуйтесь с документацией стандартной библиотеки. |

---

