# Python Standard Library Modules - Quiz

Проверьте свои знания по теме "Стандартные модули Python".

---

## Question 1: os модуль

Что возвращает `os.getcwd()`?

A) Домашнюю директорию

B) Путь к Python

C) Текущую рабочую директорию

D) Список файлов в директории

---

## Question 2: os.environ

Как получить значение переменной окружения?

A) `getenv('VAR')`

B) `env.get('VAR')`

C) `os.environ.VAR`

D) `os.getenv('VAR')` или `os.environ.get('VAR')`

---

## Question 3: sys модуль

Что содержит `sys.argv`?

A) Пути к модулям

B) Системную информацию

C) Версию Python

D) Список аргументов командной строки

---

## Question 4: sys.exit()

Что делает `sys.exit(0)`?

A) Завершает программу с кодом 0 (успех)

B) Выводит сообщение об ошибке

C) Перезапускает программу

D) Ничего

---

## Question 5: datetime

Как получить текущую дату и время?

A) `datetime.datetime.now()`

B) `datetime.current()`

C) `time.now()`

D) `datetime.today()`

---

## Question 6: Форматирование даты

Какой метод форматирует datetime в строку?

A) `strftime()`

B) `to_string()`

C) `str()`

D) `format()`

---

## Question 7: Парсинг даты

Какой метод парсит строку в datetime?

A) `datetime()`

B) `from_string()`

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

A) 1

B) 2

C) 45

D) 30

---

## Question 9: re модуль

Какая функция ищет паттерн в любом месте строки?

A) `re.find()`

B) `re.match()`

C) `re.locate()`

D) `re.search()`

---

## Question 10: re.match vs re.search

В чём разница между `re.match()` и `re.search()`?

A) `match()` ищет только в начале строки

B) `match()` быстрее

C) `search()` ищет только в конце

D) Нет разницы

---

## Question 11: re.findall()

Что возвращает `re.findall()`?

A) Первое совпадение

B) True/False

C) Список всех совпадений

D) Итератор

---

## Question 12: Группы в регулярках

Как получить группу из match-объекта?

A) `match.group(1)`

B) `match.get(1)`

C) `match.groups[1]`

D) `match[1]`

---

## Question 13: json модуль

Что делает `json.dumps()`?

A) Валидирует JSON

B) Загружает JSON из файла

C) Сериализует Python-объект в JSON-строку

D) Десериализует JSON-строку

---

## Question 14: json.load vs json.loads

В чём разница?

A) `loads()` быстрее

B) `loads()` для списков

C) Нет разницы

D) `load()` из файла, `loads()` из строки

---

## Question 15: random модуль

Какая функция возвращает случайное float от 0 до 1?

A) `random.uniform(0, 1)`

B) `random.float()`

C) `random.rand()`

D) `random.random()`

---

## Question 16: random.choice()

Что делает `random.choice()`?

A) Выбирает один случайный элемент

B) Генерирует случайное число

C) Выбирает несколько случайных элементов

D) Перемешивает список

---

## Question 17: random.seed()

Зачем нужен `random.seed()`?

A) Для увеличения случайности

B) Для воспроизводимости случайной последовательности

C) Для криптографии

D) Для генерации случайных чисел

---

## Question 18: collections.Counter

Что выведет следующий код?

```python
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))
```

A) [('a', 5)]

B) 5

C) {'a': 5}

D) 'a'

---

## Question 19: collections.defaultdict

В чём преимущество `defaultdict`?

A) Сортирует ключи

B) Автоматически создаёт значение для несуществующего ключа

C) Быстрее обычного dict

D) Ограничивает размер

---

## Question 20: itertools

Какой модуль содержит `chain`, `cycle`, `combinations`?

A) `functools`

B) `tools`

C) `itertools`

D) `collections`

---

## Question 21: itertools.chain()

Что делает `itertools.chain()`?

A) Объединяет несколько итерируемых объектов в один

B) Связывает функции

C) Создаёт цепочку вызовов

D) Сортирует элементы

---

## Question 22: logging

Какой уровень логирования используется для отладочных сообщений?

A) `DEBUG`

B) `TRACE`

C) `WARNING`

D) `INFO`

---

## Question 23: logging уровни

Какой порядок уровней логирования (от низшего к высшему)?

A) WARNING < INFO < DEBUG < ERROR < CRITICAL

B) DEBUG < INFO < WARNING < ERROR < CRITICAL

C) CRITICAL < ERROR < WARNING < INFO < DEBUG

D) INFO < DEBUG < WARNING < ERROR < CRITICAL

---

## Question 24: argparse

Для чего используется модуль argparse?

A) Для парсинга JSON

B) Для парсинга регулярных выражений

C) Для парсинга HTML

D) Для парсинга аргументов командной строки

---

## Question 25: hashlib

Какой модуль используется для вычисления хэшей (MD5, SHA)?

A) `hashlib`

B) `crypto`

C) `hash`

D) `checksum`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `getcwd()` = get current working directory. |
| 2 | D | `os.getenv()` или `os.environ.get()` безопасно получают переменную окружения. |
| 3 | D | `sys.argv` — список: [скрипт, арг1, арг2, ...]. `sys.argv[0]` — имя скрипта. |
| 4 | A | `sys.exit(0)` — успешное завершение. Ненулевой код означает ошибку. |
| 5 | A | `datetime.datetime.now()` или `datetime.now()` после `from datetime import datetime`. |
| 6 | A | `strftime()` (string format time) форматирует в строку. |
| 7 | D | `strptime()` (string parse time) парсит строку в datetime. |
| 8 | B | 15 января + 30 дней = 14 февраля, месяц = 2. |
| 9 | D | `search()` ищет в любом месте, `match()` — только в начале. |
| 10 | A | `match()` проверяет только начало строки. |
| 11 | C | `findall()` возвращает список всех неперекрывающихся совпадений. |
| 12 | A | `match.group(1)` возвращает первую группу. `group(0)` — всё совпадение. |
| 13 | C | `dumps` = dump string — сериализует в строку. |
| 14 | D | `load()` из file object, `loads()` из string. |
| 15 | D | `random.random()` — float в [0.0, 1.0). |
| 16 | A | `choice()` выбирает один элемент. `choices()` / `sample()` — несколько. |
| 17 | B | `seed()` инициализирует генератор для воспроизводимых результатов. |
| 18 | A | `most_common(n)` возвращает список кортежей [(element, count)]. |
| 19 | B | `defaultdict(list)` создаёт пустой список при обращении к несуществующему ключу. |
| 20 | C | `itertools` содержит функции для эффективной работы с итераторами. |
| 21 | A | `chain()` объединяет итерируемые объекты: `chain([1,2], [3,4])` → 1,2,3,4. |
| 22 | A | DEBUG — самый низкий уровень, для отладочной информации. |
| 23 | B | DEBUG (10) < INFO (20) < WARNING (30) < ERROR (40) < CRITICAL (50). |
| 24 | D | `argparse` — стандартный модуль для парсинга CLI-аргументов. |
| 25 | A | `hashlib` предоставляет хэш-алгоритмы: md5, sha256 и др. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание стандартной библиотеки! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите datetime и logging. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на регулярные выражения и collections. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Практикуйтесь с документацией стандартной библиотеки. |

---




