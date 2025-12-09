# Tabular Data - Quiz

Проверьте свои знания по теме "Табличные данные: CSV, TSV".

---

## Question 1: CSV расшифровка






Что означает CSV?

A) Character Separated Values

B) Comma-Separated Values

C) Common Separated Values

D) Column Sorted Values

---

## Question 2: Разделитель CSV






Какой разделитель используется по умолчанию в CSV?

A) Запятая

B) Пробел

C) Табуляция

D) Точка с запятой

---

## Question 3: TSV разделитель






Какой разделитель используется в TSV?

A) Запятая

B) Табуляция

C) Вертикальная черта

D) Точка с запятой

---

## Question 4: Кавычки в CSV






Как записать значение "Hello, World" в CSV?

A) `Hello\, World`

B) `Hello, World`

C) `'Hello, World'`

D) "Hello, World"

---

## Question 5: Кавычки внутри значения






Как записать значение со словом "test" (в кавычках) в CSV?

A) "He said ""test"""

B) `He said \"test\"`

C) `"He said 'test'"`

D) `"He said "test""`

---

## Question 6: Python csv модуль






Какой класс читает CSV как словари?

A) csv.DictReader

B) `csv.MapReader`

C) `csv.reader`

D) `csv.DictParser`

---

## Question 7: newline параметр






Почему важен `newline=''` при открытии CSV в Python?

A) Для сжатия файла

B) Для ускорения чтения

C) Для корректной обработки переносов строк

D) Для поддержки Unicode

---

## Question 8: csvkit инструмент






Какой инструмент csvkit красиво выводит CSV в терминал?

A) `csvdisplay`

B) csvlook

C) `csvprint`

D) `csvshow`

---

## Question 9: Европейский CSV






Какой разделитель часто используется в европейских CSV файлах?

A) Запятая

B) Слеш

C) Двоеточие

D) Точка с запятой

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

B) UTF-16

C) Latin-1

D) UTF-8

---

## Question 12: csvgrep






Что делает команда `csvgrep -c name -m Alice data.csv`?

A) Фильтрует строки где колонка name содержит Alice

B) Удаляет строки с Alice

C) Заменяет Alice на другое значение

D) Сортирует по колонке name

---

## Question 13: csv.writer






Какой метод записывает несколько строк в CSV?

A) writer.writerows(rows)

B) `writer.dump(rows)`

C) `writer.write(rows)`

D) `writer.writeall(rows)`

---

## Question 14: Заголовок CSV






Как получить заголовок CSV при чтении в Python?

A) `reader.columns`

B) `reader.header()`

C) next(reader)

D) `reader[0]`

---

## Question 15: csvsql






Что позволяет делать csvsql?

A) Выполнять SQL запросы к CSV файлу

B) Все вышеперечисленное

C) Конвертировать CSV в SQL файл

D) Импортировать CSV в базу данных

---

## Question 16: csvstat






Что делает команда csvstat?

A) Сортирует CSV

B) Выводит CSV как таблицу

C) Выводит статистику по колонкам (мин, макс, среднее)

D) Конвертирует в JSON

---

## Question 17: awk сумма






Что делает `awk -F, 'NR>1 {sum+=$2} END {print sum}' data.csv`?

A) Подсчитывает строки

B) Сортирует по второй колонке

C) Суммирует значения второй колонки (без заголовка)

D) Выводит вторую колонку

---

## Question 18: BOM






Что такое BOM в контексте CSV файлов?

A) Разделитель колонок

B) Byte Order Mark — маркер порядка байтов в начале файла

C) Формат даты

D) Тип сжатия

---

## Question 19: csv.DictWriter






Какой метод csv.DictWriter записывает заголовок?

A) writer.columns()

B) writer.writeheader()

C) writer.header()

D) writer.writerow()

---

## Question 20: csvjson






Что делает команда csvjson?

A) Валидирует CSV

B) Выполняет SQL запросы

C) Конвертирует JSON в CSV

D) Конвертирует CSV в JSON

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Comma-Separated Values — значения, разделённые запятыми. |
| 2 | A | По умолчанию CSV использует запятую как разделитель. |
| 3 | B | TSV (Tab-Separated Values) использует табуляцию. |
| 4 | D | Значения с запятой заключаются в двойные кавычки. |
| 5 | A | Кавычки внутри значения удваиваются: `""`. |
| 6 | A | `csv.DictReader` возвращает строки как словари с ключами из заголовка. |
| 7 | C | `newline=''` предотвращает проблемы с переносами строк на разных ОС. |
| 8 | B | `csvlook` форматирует CSV как таблицу в терминале. |
| 9 | D | В европейских странах запятая — десятичный разделитель, поэтому CSV использует `;`. |
| 10 | B | `pd.read_csv()` — основная функция pandas для чтения CSV. |
| 11 | D | UTF-8 — рекомендуемая кодировка для совместимости. |
| 12 | A | `csvgrep -c column -m match` фильтрует строки по значению в колонке. |
| 13 | A | `writerows()` записывает список списков (несколько строк). |
| 14 | C | `next(reader)` возвращает первую строку (обычно заголовок). |
| 15 | B | csvsql может выполнять SQL запросы, конвертировать и импортировать в БД. |
| 16 | C | csvstat выводит статистику: min, max, mean, std и т.д. |
| 17 | C | NR>1 пропускает заголовок, sum+=$2 суммирует вторую колонку. |
| 18 | B | BOM (Byte Order Mark) — специальные байты в начале UTF-8/UTF-16 файлов. |
| 19 | B | writeheader() записывает строку с именами колонок из fieldnames. |
| 20 | D | csvjson конвертирует CSV файл в JSON формат. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично знаете CSV! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите работу с кавычками и csvkit. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте разделы о синтаксисе CSV. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---

