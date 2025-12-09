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

A) Версию Python

B) Пути к модулям

C) Системную информацию

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

A) `from_string()`

B) `parse()`

C) `datetime()`

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

A) `re.search()`

B) `re.find()`

C) `re.locate()`

D) `re.match()`

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

B) Сериализует Python-объект в JSON-строку

C) Десериализует JSON-строку

D) Загружает JSON из файла

---

## Question 14: json.load vs json.loads





В чём разница?

A) `loads()` для списков

B) `loads()` быстрее

C) `load()` из файла, `loads()` из строки

D) Нет разницы

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

A) Выбирает несколько случайных элементов

B) Выбирает один случайный элемент

C) Генерирует случайное число

D) Перемешивает список

---

## Question 17: random.seed()





Зачем нужен `random.seed()`?

A) Для генерации случайных чисел

B) Для криптографии

C) Для воспроизводимости случайной последовательности

D) Для увеличения случайности

---

## Question 18: collections.Counter





Что выведет следующий код?

```python
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(1))
```

A) 5

B) {'a': 5}

C) [('a', 5)]

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

A) Создаёт цепочку вызовов

B) Связывает функции

C) Сортирует элементы

D) Объединяет несколько итерируемых объектов в один

---

## Question 22: logging





Какой уровень логирования используется для отладочных сообщений?

A) `TRACE`

B) `INFO`

C) `WARNING`

D) `DEBUG`

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

A) Для парсинга HTML

B) Для парсинга JSON

C) Для парсинга регулярных выражений

D) Для парсинга аргументов командной строки

---

## Question 25: hashlib





Какой модуль используется для вычисления хэшей (MD5, SHA)?

A) `crypto`

B) `checksum`

C) `hash`

D) `hashlib`

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
| 9 | A | `search()` ищет в любом месте, `match()` — только в начале. |
| 10 | A | `match()` проверяет только начало строки. |
| 11 | C | `findall()` возвращает список всех неперекрывающихся совпадений. |
| 12 | A | `match.group(1)` возвращает первую группу. `group(0)` — всё совпадение. |
| 13 | B | `dumps` = dump string — сериализует в строку. |
| 14 | C | `load()` из file object, `loads()` из string. |
| 15 | D | `random.random()` — float в [0.0, 1.0). |
| 16 | B | `choice()` выбирает один элемент. `choices()` / `sample()` — несколько. |
| 17 | C | `seed()` инициализирует генератор для воспроизводимых результатов. |
| 18 | C | `most_common(n)` возвращает список кортежей [(element, count)]. |
| 19 | B | `defaultdict(list)` создаёт пустой список при обращении к несуществующему ключу. |
| 20 | C | `itertools` содержит функции для эффективной работы с итераторами. |
| 21 | D | `chain()` объединяет итерируемые объекты: `chain([1,2], [3,4])` → 1,2,3,4. |
| 22 | D | DEBUG — самый низкий уровень, для отладочной информации. |
| 23 | B | DEBUG (10) < INFO (20) < WARNING (30) < ERROR (40) < CRITICAL (50). |
| 24 | D | `argparse` — стандартный модуль для парсинга CLI-аргументов. |
| 25 | D | `hashlib` предоставляет хэш-алгоритмы: md5, sha256 и др. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание стандартной библиотеки! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите datetime и logging. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на регулярные выражения и collections. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Практикуйтесь с документацией стандартной библиотеки. |

---

