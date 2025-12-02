# Introduction to Unix System Programming - Quiz

Проверьте свои знания по введению в системное программирование.

---

## Question 1: Определение

Что такое системное программирование?

A) Программирование бизнес-логики

B) Создание программ, взаимодействующих с ОС для управления ресурсами

C) Веб-разработка

D) Разработка мобильных приложений

---

## Question 2: Системные вызовы

Что такое syscall (системный вызов)?

A) Вызов функции в Python

B) Запрос к ядру для выполнения привилегированной операции

C) HTTP запрос к серверу

D) Вызов метода класса

---

## Question 3: Модуль os

Какая функция возвращает PID текущего процесса?

A) os.pid()

B) os.getpid()

C) os.process_id()

D) os.current_pid()

---

## Question 4: Переменные окружения

Как получить значение переменной окружения HOME?

A) os.getenv["HOME"]

B) os.environ.get("HOME")

C) os.environment("HOME")

D) os.env.HOME

---

## Question 5: Обработка ошибок

Какой стиль обработки ошибок рекомендуется в Python?

A) LBYL (Look Before You Leap)

B) EAFP (Easier to Ask Forgiveness than Permission)

C) Оба одинаково хороши

D) Никакой, ошибки игнорируются

---

## Question 6: errno

Что означает код ошибки ENOENT?

A) Permission denied

B) No such file or directory

C) File exists

D) Invalid argument

---

## Question 7: ctypes

Для чего используется модуль ctypes?

A) Для работы с типами данных

B) Для прямого вызова C-функций

C) Для шифрования

D) Для работы с базами данных

---

## Question 8: Информация о системе

Какая функция возвращает информацию об операционной системе?

A) os.system()

B) os.uname()

C) os.info()

D) os.platform()

---

## Question 9: Текущий каталог

Как получить путь к текущему рабочему каталогу?

A) os.pwd()

B) os.getcwd()

C) os.cwd()

D) os.current_dir()

---

## Question 10: Отладка

Какая утилита используется для трассировки syscalls на OpenBSD?

A) strace

B) ktrace

C) dtrace

D) ltrace

---

## Question 11: pathlib

Какой модуль предоставляет объектно-ориентированный API для работы с путями?

A) os.path

B) pathlib

C) filepath

D) path

---

## Question 12: PPID

Что возвращает функция os.getppid()?

A) PID текущего процесса

B) PID родительского процесса

C) PID первого процесса

D) PID последнего процесса

---

## Question 13: os.name

Какое значение возвращает os.name на Unix системах?

A) "unix"

B) "posix"

C) "linux"

D) "bsd"

---

## Question 14: OSError

Какой атрибут OSError содержит числовой код ошибки?

A) error_code

B) errno

C) code

D) number

---

## Question 15: libc

Что такое libc?

A) Компилятор C

B) Стандартная библиотека C

C) Редактор кода

D) Отладчик

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Системное программирование — взаимодействие с ОС для управления ресурсами |
| 2 | B | Syscall — запрос к ядру для привилегированных операций |
| 3 | B | os.getpid() возвращает Process ID текущего процесса |
| 4 | B | os.environ.get("HOME") безопасно получает переменную окружения |
| 5 | B | EAFP рекомендуется в Python — сначала пробуем, потом обрабатываем ошибку |
| 6 | B | ENOENT (Error NO ENTry) означает "No such file or directory" |
| 7 | B | ctypes позволяет вызывать функции из C библиотек |
| 8 | B | os.uname() возвращает информацию о системе (sysname, nodename, etc.) |
| 9 | B | os.getcwd() возвращает current working directory |
| 10 | B | ktrace используется на BSD, strace — на Linux |
| 11 | B | pathlib — современный ООП модуль для работы с путями |
| 12 | B | os.getppid() возвращает Parent Process ID |
| 13 | B | os.name возвращает "posix" на Unix-like системах |
| 14 | B | OSError.errno содержит числовой код ошибки |
| 15 | B | libc — стандартная библиотека C с обёртками над syscalls |

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

