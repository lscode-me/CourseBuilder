# Introduction to Unix System Programming - Quiz

Проверьте свои знания по введению в системное программирование.

---

## Question 1: Определение


Что такое системное программирование?

A) Разработка мобильных приложений

B) Веб-разработка

C) Создание программ, взаимодействующих с ОС для управления ресурсами

D) Программирование бизнес-логики

---

## Question 2: Системные вызовы


Что такое syscall (системный вызов)?

A) Запрос к ядру для выполнения привилегированной операции

B) Вызов метода класса

C) Вызов функции в Python

D) HTTP запрос к серверу

---

## Question 3: Модуль os


Какая функция возвращает PID текущего процесса?

A) os.pid()

B) os.getpid()

C) os.current_pid()

D) os.process_id()

---

## Question 4: Переменные окружения


Как получить значение переменной окружения HOME?

A) os.environment("HOME")

B) os.getenv["HOME"]

C) os.env.HOME

D) os.environ.get("HOME")

---

## Question 5: Обработка ошибок


Какой стиль обработки ошибок рекомендуется в Python?

A) Никакой, ошибки игнорируются

B) LBYL (Look Before You Leap)

C) EAFP (Easier to Ask Forgiveness than Permission)

D) Оба одинаково хороши

---

## Question 6: errno


Что означает код ошибки ENOENT?

A) File exists

B) Invalid argument

C) Permission denied

D) No such file or directory

---

## Question 7: ctypes


Для чего используется модуль ctypes?

A) Для прямого вызова C-функций

B) Для шифрования

C) Для работы с базами данных

D) Для работы с типами данных

---

## Question 8: Информация о системе


Какая функция возвращает информацию об операционной системе?

A) os.system()

B) os.platform()

C) os.uname()

D) os.info()

---

## Question 9: Текущий каталог


Как получить путь к текущему рабочему каталогу?

A) os.getcwd()

B) os.pwd()

C) os.cwd()

D) os.current_dir()

---

## Question 10: Отладка


Какая утилита используется для трассировки syscalls на OpenBSD?

A) ltrace

B) dtrace

C) ktrace

D) strace

---

## Question 11: pathlib


Какой модуль предоставляет объектно-ориентированный API для работы с путями?

A) os.path

B) pathlib

C) path

D) filepath

---

## Question 12: PPID


Что возвращает функция os.getppid()?

A) PID текущего процесса

B) PID последнего процесса

C) PID первого процесса

D) PID родительского процесса

---

## Question 13: os.name


Какое значение возвращает os.name на Unix системах?

A) "bsd"

B) "posix"

C) "linux"

D) "unix"

---

## Question 14: OSError


Какой атрибут OSError содержит числовой код ошибки?

A) code

B) errno

C) error_code

D) number

---

## Question 15: libc


Что такое libc?

A) Редактор кода

B) Отладчик

C) Компилятор C

D) Стандартная библиотека C

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Системное программирование — взаимодействие с ОС для управления ресурсами |
| 2 | A | Syscall — запрос к ядру для привилегированных операций |
| 3 | B | os.getpid() возвращает Process ID текущего процесса |
| 4 | D | os.environ.get("HOME") безопасно получает переменную окружения |
| 5 | C | EAFP рекомендуется в Python — сначала пробуем, потом обрабатываем ошибку |
| 6 | D | ENOENT (Error NO ENTry) означает "No such file or directory" |
| 7 | A | ctypes позволяет вызывать функции из C библиотек |
| 8 | C | os.uname() возвращает информацию о системе (sysname, nodename, etc.) |
| 9 | A | os.getcwd() возвращает current working directory |
| 10 | C | ktrace используется на BSD, strace — на Linux |
| 11 | B | pathlib — современный ООП модуль для работы с путями |
| 12 | D | os.getppid() возвращает Parent Process ID |
| 13 | B | os.name возвращает "posix" на Unix-like системах |
| 14 | B | OSError.errno содержит числовой код ошибки |
| 15 | D | libc — стандартная библиотека C с обёртками над syscalls |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Отличное понимание основ системного программирования. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите errno и ctypes. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать лекцию. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Внимательно изучите модуль os. |

---

