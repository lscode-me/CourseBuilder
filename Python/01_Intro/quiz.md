# Python Introduction - Quiz

Проверьте свои знания по теме "Введение в Python: история, философия, установка и первые шаги".

---

## Question 1: История Python

Кто является создателем языка Python?

A) Джеймс Гослинг (James Gosling)

B) Бьёрн Страуструп (Bjarne Stroustrup)

C) Гвидо ван Россум (Guido van Rossum)

D) Деннис Ритчи (Dennis Ritchie)

---

## Question 2: Тип языка

Python является:

A) Компилируемым языком со статической типизацией

B) Интерпретируемым языком с динамической типизацией

C) Компилируемым языком с динамической типизацией

D) Интерпретируемым языком со статической типизацией

---

## Question 3: Версии Python

Какая версия Python официально прекратила поддержку 1 января 2020 года?

A) Python 1.x

B) Python 2.x

C) Python 3.0

D) Python 3.5

---

## Question 4: Деление в Python 3

Каков результат выражения `5 / 2` в Python 3?

A) 2

B) 2.0

C) 2.5

D) 2.50

---

## Question 5: Целочисленное деление

Какой оператор используется для целочисленного деления в Python?

A) `/`

B) `%`

C) `//`

D) `**`

---

## Question 6: Функция print()

Какой синтаксис правильный для Python 3?

A) `print "Hello, World!"`

B) `print("Hello, World!")`

C) `echo("Hello, World!")`

D) `console.log("Hello, World!")`

---

## Question 7: Виртуальные окружения

Какая команда создаёт виртуальное окружение в Python 3?

A) `pip create venv myenv`

B) `python -m virtualenv myenv`

C) `python3 -m venv myenv`

D) `virtualenv --create myenv`

---

## Question 8: Активация окружения

Как активировать виртуальное окружение на Linux/macOS?

A) `venv/bin/activate`

B) `source venv/bin/activate`

C) `activate venv`

D) `venv\Scripts\activate`

---

## Question 9: pip

Что делает команда `pip freeze > requirements.txt`?

A) Замораживает установку пакетов

B) Сохраняет список установленных пакетов в файл

C) Удаляет все пакеты

D) Устанавливает пакеты из файла

---

## Question 10: Отступы

Почему следующий код вызовет ошибку?

```python
if True:
print("Hello")
```

A) Неправильный синтаксис условия

B) Отсутствует отступ перед print

C) Не хватает скобок у True

D) print должен быть на той же строке

---

## Question 11: Zen of Python

Как посмотреть "The Zen of Python"?

A) `print(zen)`

B) `import zen`

C) `import this`

D) `python --zen`

---

## Question 12: Shebang

Для чего нужна строка `#!/usr/bin/env python3` в начале скрипта?

A) Это комментарий с информацией об авторе

B) Указывает системе, какой интерпретатор использовать

C) Импортирует модуль env

D) Устанавливает переменные окружения

---

## Question 13: Проверка версии

Какая команда покажет версию установленного Python?

A) `python --v`

B) `python -version`

C) `python --version`

D) `python /version`

---

## Question 14: PEP 8

Сколько пробелов рекомендуется использовать для отступа согласно PEP 8?

A) 2

B) 3

C) 4

D) 8

---

## Question 15: Именование переменных

Какое имя переменной соответствует конвенции PEP 8 для обычных переменных?

A) `UserName`

B) `user_name`

C) `USERNAME`

D) `userName`

---

## Question 16: Тип переменной

Что выведет следующий код?

```python
x = 42
x = "hello"
print(type(x).__name__)
```

A) int

B) str

C) TypeError

D) NoneType

---

## Question 17: pyenv

Для чего используется инструмент pyenv?

A) Для создания виртуальных окружений

B) Для управления несколькими версиями Python

C) Для установки pip пакетов

D) Для форматирования кода

---

## Question 18: REPL

Что означает аббревиатура REPL?

A) Run-Execute-Print-Loop

B) Read-Eval-Print-Loop

C) Read-Execute-Parse-Loop

D) Run-Evaluate-Print-Log

---

## Question 19: f-strings

Какой синтаксис правильный для f-string в Python 3.6+?

A) `"Hello, {name}!"`

B) `f"Hello, {name}!"`

C) `"Hello, " + name + "!"`

D) `format("Hello, {}!", name)`

---

## Question 20: Выход из интерактивного режима

Как выйти из интерактивного режима Python?

A) `quit`

B) `exit()` или `Ctrl+D`

C) `close()`

D) `Ctrl+C`

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Гвидо ван Россум создал Python в 1991 году. Название от "Monty Python". |
| 2 | B | Python — интерпретируемый язык с динамической типизацией, типы определяются во время выполнения. |
| 3 | B | Python 2.x прекратил поддержку 1 января 2020 года. Всегда используйте Python 3. |
| 4 | C | В Python 3 оператор `/` всегда возвращает float: `5 / 2 = 2.5`. |
| 5 | C | Оператор `//` выполняет целочисленное деление: `5 // 2 = 2`. |
| 6 | B | В Python 3 `print` — это функция, требующая скобки: `print("Hello")`. |
| 7 | C | Команда `python3 -m venv myenv` создаёт виртуальное окружение. |
| 8 | B | На Linux/macOS активация: `source venv/bin/activate`. На Windows: `venv\Scripts\activate`. |
| 9 | B | `pip freeze` выводит список пакетов, `> requirements.txt` перенаправляет в файл. |
| 10 | B | Python использует отступы для обозначения блоков кода. Без отступа — IndentationError. |
| 11 | C | `import this` выводит "The Zen of Python" — философию языка (PEP 20). |
| 12 | B | Shebang указывает ОС, какой интерпретатор использовать при запуске скрипта. |
| 13 | C | `python --version` или `python -V` показывает версию Python. |
| 14 | C | PEP 8 рекомендует 4 пробела для отступа. Не смешивайте пробелы и табы. |
| 15 | B | `snake_case` для переменных и функций, `PascalCase` для классов, `UPPER_CASE` для констант. |
| 16 | B | Переменная `x` динамически меняет тип. После присвоения строки тип становится `str`. |
| 17 | B | pyenv позволяет устанавливать и переключаться между разными версиями Python. |
| 18 | B | REPL = Read-Eval-Print-Loop — интерактивный режим Python. |
| 19 | B | f-strings (Python 3.6+): `f"Hello, {name}!"` — современный способ форматирования. |
| 20 | B | `exit()`, `quit()` или `Ctrl+D` (Linux/macOS) / `Ctrl+Z` (Windows) для выхода. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили основы Python. Переходите к структурам данных! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы установки и настройки окружения. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о виртуальных окружениях и синтаксисе Python 3. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию целиком. |

---

