# Introduction to Unix System Programming - Quiz

Проверьте свои знания по введению в системное программирование.

---

## Question 1: Определение

Что такое системное программирование?

A) Программирование бизнес-логики

B) Разработка мобильных приложений

C) Создание программ, взаимодействующих с ОС для управления ресурсами

D) Веб-разработка

---

## Question 2: Системные вызовы

Что такое syscall (системный вызов)?

A) Запрос к ядру для выполнения привилегированной операции

B) HTTP запрос к серверу

C) Вызов функции в Python

D) Вызов метода класса

---

## Question 3: Модуль os

Какая функция возвращает PID текущего процесса?

A) os.getpid()

B) os.pid()

C) os.current_pid()

D) os.process_id()

---

## Question 4: Переменные окружения

Как получить значение переменной окружения HOME?

A) os.env.HOME

B) os.environment("HOME")

C) os.environ.get("HOME")

D) os.getenv["HOME"]

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

A) No such file or directory

B) File exists

C) Permission denied

D) Invalid argument

---

## Question 7: ctypes

Для чего используется модуль ctypes?

A) Для прямого вызова C-функций

B) Для работы с типами данных

C) Для работы с базами данных

D) Для шифрования

---

## Question 8: Информация о системе

Какая функция возвращает информацию об операционной системе?

A) os.info()

B) os.system()

C) os.platform()

D) os.uname()

---

## Question 9: Текущий каталог

Как получить путь к текущему рабочему каталогу?

A) os.current_dir()

B) os.getcwd()

C) os.cwd()

D) os.pwd()

---

## Question 10: Отладка

Какая утилита используется для трассировки syscalls на OpenBSD?

A) dtrace

B) ltrace

C) ktrace

D) strace

---

## Question 11: pathlib

Какой модуль предоставляет объектно-ориентированный API для работы с путями?

A) filepath

B) pathlib

C) os.path

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

A) "linux"

B) "posix"

C) "unix"

D) "bsd"

---

## Question 14: OSError

Какой атрибут OSError содержит числовой код ошибки?

A) number

B) code

C) errno

D) error_code

---

## Question 15: libc

Что такое libc?

A) Редактор кода

B) Компилятор C

C) Отладчик

D) Стандартная библиотека C

---

## Question 16: User vs Kernel space

Что происходит при системном вызове?

A) Переключение из user space в kernel space

B) Перезагрузка системы

C) Ничего особенного

D) Запуск нового процесса

---

## Question 17: os.getcwd()

Что возвращает os.getcwd()?

A) Домашнюю директорию

B) Временную директорию

C) Текущую рабочую директорию

D) Корневую директорию

---

## Question 18: EPERM

Что означает код ошибки EPERM?

A) Operation not permitted

B) Invalid argument

C) File not found

D) File exists

---

## Question 19: os.chdir()

Что делает os.chdir(path)?

A) Создаёт директорию

B) Удаляет директорию

C) Меняет текущую рабочую директорию

D) Проверяет существование директории

---

## Question 20: POSIX

Что такое POSIX?

A) Язык программирования

B) Редактор кода

C) Операционная система

D) Стандарт совместимости Unix-подобных систем

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Системное программирование — взаимодействие с ОС для управления ресурсами |
| 2 | A | Syscall — запрос к ядру для привилегированных операций |
| 3 | A | os.getpid() возвращает Process ID текущего процесса |
| 4 | C | os.environ.get("HOME") безопасно получает переменную окружения |
| 5 | B | EAFP рекомендуется в Python — сначала пробуем, потом обрабатываем ошибку |
| 6 | A | ENOENT (Error NO ENTry) означает "No such file or directory" |
| 7 | A | ctypes позволяет вызывать функции из C библиотек |
| 8 | D | os.uname() возвращает информацию о системе (sysname, nodename, etc.) |
| 9 | B | os.getcwd() возвращает current working directory |
| 10 | C | ktrace используется на BSD, strace — на Linux |
| 11 | B | pathlib — современный ООП модуль для работы с путями |
| 12 | B | os.getppid() возвращает Parent Process ID |
| 13 | B | os.name возвращает "posix" на Unix-like системах |
| 14 | C | OSError.errno содержит числовой код ошибки |
| 15 | D | libc — стандартная библиотека C с обёртками над syscalls |
| 16 | A | Syscall требует переключения контекста из user в kernel mode |
| 17 | C | getcwd() возвращает current working directory |
| 18 | A | EPERM = Operation not permitted (нет прав) |
| 19 | C | chdir() изменяет текущую рабочую директорию процесса |
| 20 | D | POSIX — стандарт для Unix-совместимости |

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


