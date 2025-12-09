# JSON - Quiz

Проверьте свои знания по теме "JSON: синтаксис, валидация и инструменты".

---

## Question 1: Типы данных JSON

Сколько типов данных поддерживает JSON?

A) 6

B) 4

C) 8

D) 10

---

## Question 2: Строки в JSON

Какие кавычки используются для строк в JSON?

A) Одинарные `'`

B) Двойные `"`

C) Обратные `` ` ``

D) Любые

---

## Question 3: Комментарии

Поддерживает ли стандартный JSON комментарии?

A) Да, с //

B) Да, с /* */

C) Нет, комментарии не поддерживаются

D) Да, с #

---

## Question 4: Trailing comma

Какой JSON валидный?

A) `{"name": "Alice", "age": 30,}`

B) `{name: "Alice", age: 30}`

C) `{'name': 'Alice', 'age': 30}`

D) `{"name": "Alice", "age": 30}`

---

## Question 5: Числа в JSON

Какое число НЕ валидно в JSON?

A) 0xFF

B) 42

C) 3.14

D) 1e10

---

## Question 6: Null в JSON

Как записывается null в JSON?

A) NULL

B) null

C) Null

D) None

---

## Question 7: Ключи объекта

Какой ключ объекта валиден в JSON?

A) name

B) 'name'

C) "name"

D) @name

---

## Question 8: jq форматирование

Какая команда jq форматирует JSON?

A) `jq -f file.json`

B) `jq --pretty file.json`

C) `jq -p file.json`

D) `jq . file.json`

---

## Question 9: jq извлечение

Как извлечь поле `name` из JSON с помощью jq?

A) jq .name file.json

B) jq name file.json

C) jq [name] file.json

D) jq get name file.json

---

## Question 10: jq без кавычек

Какой флаг jq выводит строки без кавычек?

A) `-s`

B) -r

C) `-c`

D) `-n`

---

## Question 11: Python JSON

Какой метод преобразует Python dict в JSON строку?

A) `json.load()`

B) `json.loads()`

C) json.dumps()

D) `json.dump()`

---

## Question 12: Python чтение файла

Какой метод читает JSON из файла?

A) json.load(file)

B) `json.loads(file)`

C) `json.read(file)`

D) `json.parse(file)`

---

## Question 13: Escape символы

Как записать перенос строки в JSON строке?

A) "line1\nline2"

B) "line1/nline2"

C) "line1\\nline2"

D) "line1
line2"

---

## Question 14: Boolean

Как записываются логические значения в JSON?

A) `True` / `False`

B) true / false

C) `TRUE` / `FALSE`

D) `1` / `0`

---

## Question 15: Массивы

Какой массив валиден в JSON?

A) `[1, 2, 3,]`

B) `(1, 2, 3)`

C) [1, 2, 3]

D) `{1, 2, 3}`

---

## Question 16: JSON Schema

Для чего используется JSON Schema?

A) Для сжатия JSON

B) Для шифрования JSON

C) Для конвертации JSON в XML

D) Для валидации структуры JSON документа

---

## Question 17: ISO 8601

В каком формате рекомендуется хранить даты в JSON?

A) "2024-01-15T10:30:00Z"

B) "01/15/2024"

C) "January 15, 2024"

D) 1705312200

---

## Question 18: Кодировка JSON

Какая кодировка стандартна для JSON?

A) ASCII

B) UTF-8

C) UTF-16

D) Latin-1

---

## Question 19: jq select

Как отфильтровать элементы массива с условием в jq?

A) `jq '.[] | filter(.active)'`

B) `jq '.[] | where(.active)'`

C) jq '.[] | select(.active == true)'

D) `jq '.[] | if .active'`

---

## Question 20: JSON Lines

Что такое JSON Lines (JSONL)?

A) JSON с комментариями

B) JSON разбитый на части

C) Сжатый JSON

D) Формат, где каждая строка — отдельный JSON объект

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | JSON поддерживает 6 типов: string, number, boolean, null, array, object. |
| 2 | B | JSON использует только двойные кавычки для строк. |
| 3 | C | Стандартный JSON не поддерживает комментарии. JSONC и JSON5 поддерживают. |
| 4 | D | Trailing comma и unquoted keys невалидны в JSON. |
| 5 | A | Hex числа (`0xFF`) не поддерживаются в JSON. |
| 6 | B | Null пишется строчными буквами: `null` (не NULL, не None). |
| 7 | C | Ключи объекта ВСЕГДА в двойных кавычках: `"name"`. |
| 8 | D | `jq .` форматирует и валидирует JSON. |
| 9 | A | `.name` — синтаксис jq для доступа к полю. |
| 10 | B | `-r` (raw output) выводит строки без кавычек. |
| 11 | C | `json.dumps()` — dump string, преобразует в строку. |
| 12 | A | `json.load(file)` читает из файлового объекта. `loads()` — из строки. |
| 13 | A | `\n` — escape-последовательность для новой строки. |
| 14 | B | JSON использует строчные `true` и `false` (не Python True/False). |
| 15 | C | Trailing comma в массивах невалидна в JSON. |
| 16 | D | JSON Schema описывает структуру для валидации JSON документов. |
| 17 | A | ISO 8601 (`2024-01-15T10:30:00Z`) — стандартный формат дат. |
| 18 | B | По RFC 8259, JSON должен быть в UTF-8 (без BOM). |
| 19 | C | `select(.condition)` фильтрует элементы в jq. |
| 20 | D | JSON Lines — формат где каждая строка файла — отдельный JSON объект. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете JSON! Переходите к YAML. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с jq. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте раздел синтаксиса и ошибок. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и практиковаться. |

---

