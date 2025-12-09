# Python Standard Library Modules - Quiz

Проверьте свои знания по теме "Стандартные модули Python".

---

## Question 1: os модуль


Что возвращает `os.getcwd()`?

A) Домашнюю директорию

B) Список файлов в директории

C) Путь к Python

D) Текущую рабочую директорию

---

## Question 2: os.environ


Как получить значение переменной окружения?

A) `os.environ.VAR`

B) `getenv('VAR')`

C) `os.getenv('VAR')` или `os.environ.get('VAR')`

D) `env.get('VAR')`

---

## Question 3: sys модуль


Что содержит `sys.argv`?

A) Системную информацию

B) Список аргументов командной строки

C) Версию Python

D) Пути к модулям

---

## Question 4: sys.exit()


Что делает `sys.exit(0)`?

A) Ничего

B) Выводит сообщение об ошибке

C) Перезапускает программу

D) Завершает программу с кодом 0 (успех)

---

## Question 5: datetime


Как получить текущую дату и время?

A) `datetime.current()`

B) `datetime.today()`

C) `datetime.datetime.now()`

D) `time.now()`

---

## Question 6: Форматирование даты


Какой метод форматирует datetime в строку?

A) `format()`

B) `to_string()`

C) `str()`

D) `strftime()`

---

## Question 7: Парсинг даты


Какой метод парсит строку в datetime?

A) `from_string()`

B) `datetime()`

C) `parse()`

D) `strptime()`

---

## Question 8: timedelta


Что выведет следующий код?

```python
from datetime import datetime, timedelta
now = datetime(2024, 1, 15)
future = now + timedelta(days=30)
print(future.month)
```

A) 45

B) 2

C) 1

D) 30

---

## Question 9: re модуль


Какая функция ищет паттерн в любом месте строки?

A) `re.locate()`

B) `re.match()`

C) `re.find()`

D) `re.search()`

---

## Question 10: re.match vs re.search


В чём разница между `re.match()` и `re.search()`?

A) `match()` быстрее

B) Нет разницы

C) `match()` ищет только в начале строки

D) `search()` ищет только в конце

---

## Question 11: re.findall()


Что возвращает `re.findall()`?

A) Список всех совпадений

B) Первое совпадение

C) True/False

D) Итератор

---

## Question 12: Группы в регулярках


Как получить группу из match-объекта?

A) `match.groups[1]`

B) `match.group(1)`

C) `match[1]`

D) `match.get(1)`

---

## Question 13: json модуль


Что делает `json.dumps()`?

A) Десериализует JSON-строку

B) Сериализует Python-объект в JSON-строку

C) Валидирует JSON

D) Загружает JSON из файла

---

## Question 14: json.load vs json.loads


В чём разница?

A) `load()` из файла, `loads()` из строки

B) `loads()` для списков

C) `loads()` быстрее

D) Нет разницы

---

## Question 15: random модуль


Какая функция возвращает случайное float от 0 до 1?

A) `random.random()`

B) `random.float()`

C) `random.uniform(0, 1)`

D) `random.rand()`

---

## Question 16: random.choice()


Что делает `random.choice()`?

A) Перемешивает список

B) Выбирает один случайный элемент

C) Выбирает несколько случайных элементов

D) Генерирует случайное число

---

## Question 17: random.seed()


Зачем нужен `random.seed()`?

A) Для увеличения случайности

B) Для криптографии

C) Для воспроизводимости случайной последовательности

D) Для генерации случайных чисел

---

## Question 18: collections.Counter


Что выведет следующий код?

```python
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))
```

A) {'a': 5}

B) [('a', 5)]

C) 5

D) 'a'

---

## Question 19: collections.defaultdict


В чём преимущество `defaultdict`?

A) Сортирует ключи

B) Ограничивает размер

C) Быстрее обычного dict

D) Автоматически создаёт значение для несуществующего ключа

---

## Question 20: itertools


Какой модуль содержит `chain`, `cycle`, `combinations`?

A) `itertools`

B) `functools`

C) `collections`

D) `tools`

---

## Question 21: itertools.chain()


Что делает `itertools.chain()`?

A) Создаёт цепочку вызовов

B) Связывает функции

C) Сортирует элементы

D) Объединяет несколько итерируемых объектов в один

---

## Question 22: logging


Какой уровень логирования используется для отладочных сообщений?

A) `DEBUG`

B) `WARNING`

C) `INFO`

D) `TRACE`

---

## Question 23: logging уровни


Какой порядок уровней логирования (от низшего к высшему)?

A) CRITICAL < ERROR < WARNING < INFO < DEBUG

B) INFO < DEBUG < WARNING < ERROR < CRITICAL

C) DEBUG < INFO < WARNING < ERROR < CRITICAL

D) WARNING < INFO < DEBUG < ERROR < CRITICAL

---

## Question 24: argparse


Для чего используется модуль argparse?

A) Для парсинга регулярных выражений

B) Для парсинга аргументов командной строки

C) Для парсинга HTML

D) Для парсинга JSON

---

## Question 25: hashlib


Какой модуль используется для вычисления хэшей (MD5, SHA)?

A) `checksum`

B) `hashlib`

C) `hash`

D) `crypto`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `getcwd()` = get current working directory. |
| 2 | C | `os.getenv()` или `os.environ.get()` безопасно получают переменную окружения. |
| 3 | B | `sys.argv` — список: [скрипт, арг1, арг2, ...]. `sys.argv[0]` — имя скрипта. |
| 4 | D | `sys.exit(0)` — успешное завершение. Ненулевой код означает ошибку. |
| 5 | C | `datetime.datetime.now()` или `datetime.now()` после `from datetime import datetime`. |
| 6 | D | `strftime()` (string format time) форматирует в строку. |
| 7 | D | `strptime()` (string parse time) парсит строку в datetime. |
| 8 | B | 15 января + 30 дней = 14 февраля, месяц = 2. |
| 9 | D | `search()` ищет в любом месте, `match()` — только в начале. |
| 10 | C | `match()` проверяет только начало строки. |
| 11 | A | `findall()` возвращает список всех неперекрывающихся совпадений. |
| 12 | B | `match.group(1)` возвращает первую группу. `group(0)` — всё совпадение. |
| 13 | B | `dumps` = dump string — сериализует в строку. |
| 14 | A | `load()` из file object, `loads()` из string. |
| 15 | A | `random.random()` — float в [0.0, 1.0). |
| 16 | B | `choice()` выбирает один элемент. `choices()` / `sample()` — несколько. |
| 17 | C | `seed()` инициализирует генератор для воспроизводимых результатов. |
| 18 | B | `most_common(n)` возвращает список кортежей [(element, count)]. |
| 19 | D | `defaultdict(list)` создаёт пустой список при обращении к несуществующему ключу. |
| 20 | A | `itertools` содержит функции для эффективной работы с итераторами. |
| 21 | D | `chain()` объединяет итерируемые объекты: `chain([1,2], [3,4])` → 1,2,3,4. |
| 22 | A | DEBUG — самый низкий уровень, для отладочной информации. |
| 23 | C | DEBUG (10) < INFO (20) < WARNING (30) < ERROR (40) < CRITICAL (50). |
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

