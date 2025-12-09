# Introduction to Unix System Programming - Quiz

Проверьте свои знания по введению в системное программирование.

---

## Question 1: Определение





Что такое системное программирование?

A) Разработка мобильных приложений

B) Создание программ, взаимодействующих с ОС для управления ресурсами

C) Программирование бизнес-логики

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

A) os.current_pid()

B) os.process_id()

C) os.getpid()

D) os.pid()

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

A) EAFP (Easier to Ask Forgiveness than Permission)

B) Никакой, ошибки игнорируются

C) Оба одинаково хороши

D) LBYL (Look Before You Leap)

---

## Question 6: errno





Что означает код ошибки ENOENT?

A) Invalid argument

B) File exists

C) No such file or directory

D) Permission denied

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

A) os.uname()

B) os.system()

C) os.info()

D) os.platform()

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

A) PID первого процесса

B) PID последнего процесса

C) PID текущего процесса

D) PID родительского процесса

---

## Question 13: os.name





Какое значение возвращает os.name на Unix системах?

A) "posix"

B) "linux"

C) "bsd"

D) "unix"

---

## Question 14: OSError





Какой атрибут OSError содержит числовой код ошибки?

A) code

B) errno

C) number

D) error_code

---

## Question 15: libc





Что такое libc?

A) Отладчик

B) Компилятор C

C) Стандартная библиотека C

D) Редактор кода

---

## Question 16: User vs Kernel space




Что происходит при системном вызове?

A) Ничего особенного

B) Переключение из user space в kernel space

C) Перезагрузка системы

D) Запуск нового процесса

---

## Question 17: os.getcwd()




Что возвращает os.getcwd()?

A) Корневую директорию

B) Текущую рабочую директорию

C) Временную директорию

D) Домашнюю директорию

---

## Question 18: EPERM




Что означает код ошибки EPERM?

A) File not found

B) Invalid argument

C) File exists

D) Operation not permitted

---

## Question 19: os.chdir()




Что делает os.chdir(path)?

A) Проверяет существование директории

B) Удаляет директорию

C) Создаёт директорию

D) Меняет текущую рабочую директорию

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
| 1 | B | Системное программирование — взаимодействие с ОС для управления ресурсами |
| 2 | A | Syscall — запрос к ядру для привилегированных операций |
| 3 | C | os.getpid() возвращает Process ID текущего процесса |
| 4 | C | os.environ.get("HOME") безопасно получает переменную окружения |
| 5 | A | EAFP рекомендуется в Python — сначала пробуем, потом обрабатываем ошибку |
| 6 | C | ENOENT (Error NO ENTry) означает "No such file or directory" |
| 7 | A | ctypes позволяет вызывать функции из C библиотек |
| 8 | A | os.uname() возвращает информацию о системе (sysname, nodename, etc.) |
| 9 | B | os.getcwd() возвращает current working directory |
| 10 | C | ktrace используется на BSD, strace — на Linux |
| 11 | B | pathlib — современный ООП модуль для работы с путями |
| 12 | D | os.getppid() возвращает Parent Process ID |
| 13 | A | os.name возвращает "posix" на Unix-like системах |
| 14 | B | OSError.errno содержит числовой код ошибки |
| 15 | C | libc — стандартная библиотека C с обёртками над syscalls |
| 16 | B | Syscall требует переключения контекста из user в kernel mode |
| 17 | B | getcwd() возвращает current working directory |
| 18 | D | EPERM = Operation not permitted (нет прав) |
| 19 | D | chdir() изменяет текущую рабочую директорию процесса |
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

