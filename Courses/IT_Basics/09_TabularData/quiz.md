# Tabular Data - Quiz

Проверьте свои знания по теме "Табличные данные: CSV, TSV".

---

## Question 1: CSV расшифровка

Что означает CSV?

A) Comma-Separated Values

B) Common Separated Values

C) Character Separated Values

D) Column Sorted Values

---

## Question 2: Разделитель CSV

Какой разделитель используется по умолчанию в CSV?

A) Точка с запятой

B) Табуляция

C) Запятая

D) Пробел

---

## Question 3: TSV разделитель

Какой разделитель используется в TSV?

A) Запятая

B) Табуляция

C) Точка с запятой

D) Вертикальная черта

---

## Question 4: Кавычки в CSV

Как записать значение "Hello, World" в CSV?

A) `Hello, World`

B) `'Hello, World'`

C) `Hello\, World`

D) "Hello, World"

---

## Question 5: Кавычки внутри значения

Как записать значение со словом "test" (в кавычках) в CSV?

A) "He said ""test"""

B) `"He said "test""`

C) `"He said 'test'"`

D) `He said \"test\"`

---

## Question 6: Python csv модуль

Какой класс читает CSV как словари?

A) `csv.reader`

B) csv.DictReader

C) `csv.DictParser`

D) `csv.MapReader`

---

## Question 7: newline параметр

Почему важен `newline=''` при открытии CSV в Python?

A) Для ускорения чтения

B) Для сжатия файла

C) Для корректной обработки переносов строк

D) Для поддержки Unicode

---

## Question 8: csvkit инструмент

Какой инструмент csvkit красиво выводит CSV в терминал?

A) csvlook

B) `csvprint`

C) `csvshow`

D) `csvdisplay`

---

## Question 9: Европейский CSV

Какой разделитель часто используется в европейских CSV файлах?

A) Запятая

B) Точка с запятой

C) Двоеточие

D) Слеш

---

## Question 10: pandas чтение

Какая функция pandas читает CSV?

A) `pd.load_csv()`

B) pd.read_csv()

C) `pd.open_csv()`

D) `pd.csv_read()`

---

## Question 11: Кодировка CSV

Какую кодировку рекомендуется использовать для CSV?

A) ASCII

B) Latin-1

C) UTF-8

D) UTF-16

---

## Question 12: csvgrep

Что делает команда `csvgrep -c name -m Alice data.csv`?

A) Удаляет строки с Alice

B) Заменяет Alice на другое значение

C) Сортирует по колонке name

D) Фильтрует строки где колонка name содержит Alice

---

## Question 13: csv.writer

Какой метод записывает несколько строк в CSV?

A) writer.writerows(rows)

B) `writer.write(rows)`

C) `writer.writeall(rows)`

D) `writer.dump(rows)`

---

## Question 14: Заголовок CSV

Как получить заголовок CSV при чтении в Python?

A) `reader.header()`

B) next(reader)

C) `reader.columns`

D) `reader[0]`

---

## Question 15: csvsql

Что позволяет делать csvsql?

A) Конвертировать CSV в SQL файл

B) Выполнять SQL запросы к CSV файлу

C) Импортировать CSV в базу данных

D) Все вышеперечисленное

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Comma-Separated Values — значения, разделённые запятыми. |
| 2 | C | По умолчанию CSV использует запятую как разделитель. |
| 3 | B | TSV (Tab-Separated Values) использует табуляцию. |
| 4 | D | Значения с запятой заключаются в двойные кавычки. |
| 5 | A | Кавычки внутри значения удваиваются: `""`. |
| 6 | B | `csv.DictReader` возвращает строки как словари с ключами из заголовка. |
| 7 | C | `newline=''` предотвращает проблемы с переносами строк на разных ОС. |
| 8 | A | `csvlook` форматирует CSV как таблицу в терминале. |
| 9 | B | В европейских странах запятая — десятичный разделитель, поэтому CSV использует `;`. |
| 10 | B | `pd.read_csv()` — основная функция pandas для чтения CSV. |
| 11 | C | UTF-8 — рекомендуемая кодировка для совместимости. |
| 12 | D | `csvgrep -c column -m match` фильтрует строки по значению в колонке. |
| 13 | A | `writerows()` записывает список списков (несколько строк). |
| 14 | B | `next(reader)` возвращает первую строку (обычно заголовок). |
| 15 | D | csvsql может выполнять SQL запросы, конвертировать и импортировать в БД. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично знаете CSV! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите работу с кавычками и csvkit. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте разделы о синтаксисе CSV. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---

