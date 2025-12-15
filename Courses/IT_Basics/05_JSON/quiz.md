# JSON - Quiz

Проверьте свои знания по теме "JSON: синтаксис, валидация и инструменты".

---

## Question 1: Типы данных JSON

Сколько типов данных поддерживает JSON?

A) 8

B) 4

C) 6

D) 10

---

## Question 2: Строки в JSON

Какие кавычки используются для строк в JSON?

A) Одинарные `'`

B) Любые кавычки

C) Двойные `"`

D) Обратные кавычки `` ` ``

---

## Question 3: Комментарии

Поддерживает ли стандартный JSON комментарии?

A) Нет, комментарии не поддерживаются

B) Да, с //

C) Да, с #

D) Да, с /* */

---

## Question 4: Trailing comma

Какой JSON валидный?

A) `{'name': 'Alice', 'age': 30}`

B) `{name: "Alice", age: 30}`

C) `{"name": "Alice", "age": 30,}`

D) `{"name": "Alice", "age": 30}`

---

## Question 5: Числа в JSON

Какое число НЕ валидно в JSON?

A) 0xFF

B) 42

C) 1e10

D) 3.14

---

## Question 6: Null в JSON

Как записывается null в JSON?

A) NULL

B) null

C) None

D) Null

---

## Question 7: Ключи объекта

Какой ключ объекта валиден в JSON?

A) "name"

B) name_without_quotes

C) 'name'

D) name

---

## Question 8: jq форматирование

Какая команда jq форматирует JSON?

A) `jq --pretty file.json`

B) `jq -f file.json`

C) `jq . file.json`

D) `jq -p file.json`

---

## Question 9: jq извлечение

Как извлечь поле `name` из JSON с помощью jq?

A) jq [name] file.json

B) jq name file.json

C) jq get name file.json

D) jq .name file.json

---

## Question 10: jq без кавычек

Какой флаг jq выводит строки без кавычек?

A) `-c`

B) `-n`

C) -r

D) `-s`

---

## Question 11: Python JSON

Какой метод преобразует Python dict в JSON строку?

A) `json.dump()`

B) json.dumps()

C) `json.load()`

D) `json.loads()`

---

## Question 12: Python чтение файла

Какой метод читает JSON из файла?

A) `json.loads(file)`

B) json.load(file)

C) `json.parse(file)`

D) `json.read(file)`

---

## Question 13: Escape символы

Как записать перенос строки в JSON строке?

A) "line1 newline line2"

B) "line1\nline2"

C) "line1\\nline2"

D) "line1/nline2"

---

## Question 14: Boolean

Как записываются логические значения в JSON?

A) true / false

B) `TRUE` / `FALSE`

C) `1` / `0`

D) `True` / `False`

---

## Question 15: Массивы

Какой массив валиден в JSON?

A) `{1, 2, 3}`

B) [1, 2, 3]

C) `(1, 2, 3)`

D) `[1, 2, 3,]`

---

## Question 16: JSON Schema

Для чего используется JSON Schema?

A) Для шифрования JSON

B) Для конвертации JSON в XML

C) Для сжатия JSON

D) Для валидации структуры JSON документа

---

## Question 17: ISO 8601

В каком формате рекомендуется хранить даты в JSON?

A) "2024-01-15T10:30:00Z"

B) 1705312200

C) "January 15, 2024"

D) "01/15/2024"

---

## Question 18: Кодировка JSON

Какая кодировка стандартна для JSON?

A) Latin-1

B) UTF-8

C) ASCII

D) UTF-16

---

## Question 19: jq select

Как отфильтровать элементы массива с условием в jq?

A) `jq '.[] | filter(.active)'`

B) jq '.[] | select(.active == true)'

C) `jq '.[] | where(.active)'`

D) `jq '.[] | if .active'`

---

## Question 20: JSON Lines

Что такое JSON Lines (JSONL)?

A) Формат, где каждая строка — отдельный JSON объект

B) JSON с комментариями

C) JSON разбитый на части

D) Сжатый JSON

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | JSON поддерживает 6 типов: string, number, boolean, null, array, object. |
| 2 | C | JSON использует только двойные кавычки для строк. |
| 3 | A | Стандартный JSON не поддерживает комментарии. JSONC и JSON5 поддерживают. |
| 4 | D | Trailing comma и unquoted keys невалидны в JSON. |
| 5 | A | Hex числа (`0xFF`) не поддерживаются в JSON. |
| 6 | B | Null пишется строчными буквами: `null` (не NULL, не None). |
| 7 | A | Ключи объекта ВСЕГДА в двойных кавычках: `"name"`. |
| 8 | C | `jq .` форматирует и валидирует JSON. |
| 9 | D | `.name` — синтаксис jq для доступа к полю. |
| 10 | C | `-r` (raw output) выводит строки без кавычек. |
| 11 | B | `json.dumps()` — dump string, преобразует в строку. |
| 12 | B | `json.load(file)` читает из файлового объекта. `loads()` — из строки. |
| 13 | A | `\n` — escape-последовательность для новой строки. |
| 14 | A | JSON использует строчные `true` и `false` (не Python True/False). |
| 15 | B | Trailing comma в массивах невалидна в JSON. |
| 16 | D | JSON Schema описывает структуру для валидации JSON документов. |
| 17 | A | ISO 8601 (`2024-01-15T10:30:00Z`) — стандартный формат дат. |
| 18 | B | По RFC 8259, JSON должен быть в UTF-8 (без BOM). |
| 19 | B | `select(.condition)` фильтрует элементы в jq. |
| 20 | A | JSON Lines — формат где каждая строка файла — отдельный JSON объект. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете JSON! Переходите к YAML. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с jq. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте раздел синтаксиса и ошибок. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и практиковаться. |

---

