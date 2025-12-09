# JSON - Quiz

Проверьте свои знания по теме "JSON: синтаксис, валидация и инструменты".

---

## Question 1: Типы данных JSON




Сколько типов данных поддерживает JSON?

A) 4

B) 10

C) 6

D) 8

---

## Question 2: Строки в JSON




Какие кавычки используются для строк в JSON?

A) Двойные `"`

B) Обратные `` ` ``

C) Любые

D) Одинарные `'`

---

## Question 3: Комментарии




Поддерживает ли стандартный JSON комментарии?

A) Да, с #

B) Нет, комментарии не поддерживаются

C) Да, с //

D) Да, с /* */

---

## Question 4: Trailing comma




Какой JSON валидный?

A) `{"name": "Alice", "age": 30,}`

B) `{'name': 'Alice', 'age': 30}`

C) `{name: "Alice", age: 30}`

D) `{"name": "Alice", "age": 30}`

---

## Question 5: Числа в JSON




Какое число НЕ валидно в JSON?

A) 1e10

B) 42

C) 0xFF

D) 3.14

---

## Question 6: Null в JSON




Как записывается null в JSON?

A) Null

B) None

C) null

D) NULL

---

## Question 7: Ключи объекта




Какой ключ объекта валиден в JSON?

A) "name"

B) name

C) 'name'

D) @name

---

## Question 8: jq форматирование




Какая команда jq форматирует JSON?

A) `jq -f file.json`

B) `jq -p file.json`

C) `jq --pretty file.json`

D) `jq . file.json`

---

## Question 9: jq извлечение




Как извлечь поле `name` из JSON с помощью jq?

A) jq .name file.json

B) jq name file.json

C) jq get name file.json

D) jq [name] file.json

---

## Question 10: jq без кавычек




Какой флаг jq выводит строки без кавычек?

A) `-c`

B) `-s`

C) `-n`

D) -r

---

## Question 11: Python JSON




Какой метод преобразует Python dict в JSON строку?

A) `json.dump()`

B) `json.load()`

C) `json.loads()`

D) json.dumps()

---

## Question 12: Python чтение файла




Какой метод читает JSON из файла?

A) `json.read(file)`

B) `json.parse(file)`

C) json.load(file)

D) `json.loads(file)`

---

## Question 13: Escape символы




Как записать перенос строки в JSON строке?

A) "line1\\nline2"

B) "line1

C) "line1/nline2"

D) "line1\nline2"

---

## Question 14: Boolean




Как записываются логические значения в JSON?

A) `True` / `False`

B) `1` / `0`

C) true / false

D) `TRUE` / `FALSE`

---

## Question 15: Массивы




Какой массив валиден в JSON?

A) `[1, 2, 3,]`

B) `(1, 2, 3)`

C) `{1, 2, 3}`

D) [1, 2, 3]

---

## Question 16: JSON Schema




Для чего используется JSON Schema?

A) Для конвертации JSON в XML

B) Для валидации структуры JSON документа

C) Для сжатия JSON

D) Для шифрования JSON

---

## Question 17: ISO 8601




В каком формате рекомендуется хранить даты в JSON?

A) "2024-01-15T10:30:00Z"

B) "01/15/2024"

C) 1705312200

D) "January 15, 2024"

---

## Question 18: Кодировка JSON




Какая кодировка стандартна для JSON?

A) ASCII

B) Latin-1

C) UTF-16

D) UTF-8

---

## Question 19: jq select




Как отфильтровать элементы массива с условием в jq?

A) `jq '.[] | if .active'`

B) `jq '.[] | where(.active)'`

C) jq '.[] | select(.active == true)'

D) `jq '.[] | filter(.active)'`

---

## Question 20: JSON Lines




Что такое JSON Lines (JSONL)?

A) Формат, где каждая строка — отдельный JSON объект

B) Сжатый JSON

C) JSON с комментариями

D) JSON разбитый на части

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | JSON поддерживает 6 типов: string, number, boolean, null, array, object. |
| 2 | A | JSON использует только двойные кавычки для строк. |
| 3 | B | Стандартный JSON не поддерживает комментарии. JSONC и JSON5 поддерживают. |
| 4 | D | Trailing comma и unquoted keys невалидны в JSON. |
| 5 | C | Hex числа (`0xFF`) не поддерживаются в JSON. |
| 6 | C | Null пишется строчными буквами: `null` (не NULL, не None). |
| 7 | A | Ключи объекта ВСЕГДА в двойных кавычках: `"name"`. |
| 8 | D | `jq .` форматирует и валидирует JSON. |
| 9 | A | `.name` — синтаксис jq для доступа к полю. |
| 10 | D | `-r` (raw output) выводит строки без кавычек. |
| 11 | D | `json.dumps()` — dump string, преобразует в строку. |
| 12 | C | `json.load(file)` читает из файлового объекта. `loads()` — из строки. |
| 13 | D | `\n` — escape-последовательность для новой строки. |
| 14 | C | JSON использует строчные `true` и `false` (не Python True/False). |
| 15 | D | Trailing comma в массивах невалидна в JSON. |
| 16 | B | JSON Schema описывает структуру для валидации JSON документов. |
| 17 | A | ISO 8601 (`2024-01-15T10:30:00Z`) — стандартный формат дат. |
| 18 | D | По RFC 8259, JSON должен быть в UTF-8 (без BOM). |
| 19 | C | `select(.condition)` фильтрует элементы в jq. |
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

