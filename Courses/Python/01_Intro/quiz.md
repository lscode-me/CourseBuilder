# Python Introduction - Quiz

Проверьте свои знания по теме "Введение в Python: история, философия, установка и первые шаги".

---

## Question 1: История Python


Кто является создателем языка Python?

A) Деннис Ритчи (Dennis Ritchie)

B) Джеймс Гослинг (James Gosling)

C) Бьёрн Страуструп (Bjarne Stroustrup)

D) Гвидо ван Россум (Guido van Rossum)

---

## Question 2: Тип языка


Python является:

A) Компилируемым языком со статической типизацией

B) Интерпретируемым языком с динамической типизацией

C) Интерпретируемым языком со статической типизацией

D) Компилируемым языком с динамической типизацией

---

## Question 3: Версии Python


Какая версия Python официально прекратила поддержку 1 января 2020 года?

A) Python 1.x

B) Python 3.0

C) Python 2.x

D) Python 3.5

---

## Question 4: Деление в Python 3


Каков результат выражения `5 / 2` в Python 3?

A) 2

B) 2.5

C) 2.50

D) 2.0

---

## Question 5: Целочисленное деление


Какой оператор используется для целочисленного деления в Python?

A) `%`

B) `/`

C) `//`

D) `**`

---

## Question 6: Функция print()


Какой синтаксис правильный для Python 3?

A) `echo("Hello, World!")`

B) `print("Hello, World!")`

C) `print "Hello, World!"`

D) `console.log("Hello, World!")`

---

## Question 7: Виртуальные окружения


Какая команда создаёт виртуальное окружение в Python 3?

A) `python3 -m venv myenv`

B) `virtualenv --create myenv`

C) `python -m virtualenv myenv`

D) `pip create venv myenv`

---

## Question 8: Активация окружения


Как активировать виртуальное окружение на Linux/macOS?

A) `venv/bin/activate`

B) `activate venv`

C) `venv\Scripts\activate`

D) `source venv/bin/activate`

---

## Question 9: pip


Что делает команда `pip freeze > requirements.txt`?

A) Сохраняет список установленных пакетов в файл

B) Замораживает установку пакетов

C) Устанавливает пакеты из файла

D) Удаляет все пакеты

---

## Question 10: Отступы


Почему следующий код вызовет ошибку?

```python
if True:
print("Hello")
```

A) print должен быть на той же строке

B) Отсутствует отступ перед print

C) Неправильный синтаксис условия

D) Не хватает скобок у True

---

## Question 11: Zen of Python


Как посмотреть "The Zen of Python"?

A) `python --zen`

B) `import this`

C) `import zen`

D) `print(zen)`

---

## Question 12: Shebang


Для чего нужна строка `#!/usr/bin/env python3` в начале скрипта?

A) Указывает системе, какой интерпретатор использовать

B) Устанавливает переменные окружения

C) Импортирует модуль env

D) Это комментарий с информацией об авторе

---

## Question 13: Проверка версии


Какая команда покажет версию установленного Python?

A) `python --v`

B) `python --version`

C) `python -version`

D) `python /version`

---

## Question 14: PEP 8


Сколько пробелов рекомендуется использовать для отступа согласно PEP 8?

A) 2

B) 8

C) 4

D) 3

---

## Question 15: Именование переменных


Какое имя переменной соответствует конвенции PEP 8 для обычных переменных?

A) `userName`

B) `UserName`

C) `USERNAME`

D) `user_name`

---

## Question 16: Тип переменной


Что выведет следующий код?

```python
x = 42
x = "hello"
print(type(x).__name__)
```

A) str

B) int

C) TypeError

D) NoneType

---

## Question 17: pyenv


Для чего используется инструмент pyenv?

A) Для форматирования кода

B) Для создания виртуальных окружений

C) Для установки pip пакетов

D) Для управления несколькими версиями Python

---

## Question 18: REPL


Что означает аббревиатура REPL?

A) Read-Eval-Print-Loop

B) Run-Evaluate-Print-Log

C) Run-Execute-Print-Loop

D) Read-Execute-Parse-Loop

---

## Question 19: f-strings


Какой синтаксис правильный для f-string в Python 3.6+?

A) `"Hello, " + name + "!"`

B) `format("Hello, {}!", name)`

C) `"Hello, {name}!"`

D) `f"Hello, {name}!"`

---

## Question 20: Выход из интерактивного режима


Как выйти из интерактивного режима Python?

A) `Ctrl+C`

B) `close()`

C) `quit`

D) `exit()` или `Ctrl+D`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Гвидо ван Россум создал Python в 1991 году. Название от "Monty Python". |
| 2 | B | Python — интерпретируемый язык с динамической типизацией, типы определяются во время выполнения. |
| 3 | C | Python 2.x прекратил поддержку 1 января 2020 года. Всегда используйте Python 3. |
| 4 | B | В Python 3 оператор `/` всегда возвращает float: `5 / 2 = 2.5`. |
| 5 | C | Оператор `//` выполняет целочисленное деление: `5 // 2 = 2`. |
| 6 | B | В Python 3 `print` — это функция, требующая скобки: `print("Hello")`. |
| 7 | A | Команда `python3 -m venv myenv` создаёт виртуальное окружение. |
| 8 | D | На Linux/macOS активация: `source venv/bin/activate`. На Windows: `venv\Scripts\activate`. |
| 9 | A | `pip freeze` выводит список пакетов, `> requirements.txt` перенаправляет в файл. |
| 10 | B | Python использует отступы для обозначения блоков кода. Без отступа — IndentationError. |
| 11 | B | `import this` выводит "The Zen of Python" — философию языка (PEP 20). |
| 12 | A | Shebang указывает ОС, какой интерпретатор использовать при запуске скрипта. |
| 13 | B | `python --version` или `python -V` показывает версию Python. |
| 14 | C | PEP 8 рекомендует 4 пробела для отступа. Не смешивайте пробелы и табы. |
| 15 | D | `snake_case` для переменных и функций, `PascalCase` для классов, `UPPER_CASE` для констант. |
| 16 | A | Переменная `x` динамически меняет тип. После присвоения строки тип становится `str`. |
| 17 | D | pyenv позволяет устанавливать и переключаться между разными версиями Python. |
| 18 | A | REPL = Read-Eval-Print-Loop — интерактивный режим Python. |
| 19 | D | f-strings (Python 3.6+): `f"Hello, {name}!"` — современный способ форматирования. |
| 20 | D | `exit()`, `quit()` или `Ctrl+D` (Linux/macOS) / `Ctrl+Z` (Windows) для выхода. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили основы Python. Переходите к структурам данных! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы установки и настройки окружения. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о виртуальных окружениях и синтаксисе Python 3. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию целиком. |

---

