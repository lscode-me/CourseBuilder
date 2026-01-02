# Bash как язык
## Скрипты, переменные, аргументы и exit codes

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь работать с файлами и потоками (модули [03_Files](../03_Files/), [04_Streams_Pipes](../04_Streams_Pipes/))
- Понимать базовые команды shell
- Знать концепцию переменных окружения

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и запускать bash-скрипты с правильным shebang
- Работать с переменными: объявление, присваивание, экспорт
- Использовать позиционные параметры и специальные переменные
- Понимать и использовать exit codes для обработки ошибок
- Применять различные типы переменных (локальные, readonly, окружения)

---

## 1. Скрипты и shebang

Bash скрипт — это текстовый файл с командами, которые выполняются последовательно.

### 1.1 Создание скрипта

**Example: Простой скрипт**

```bash
# Создать скрипт
$ cat > hello.sh << 'SCRIPT'
#!/bin/bash
echo "Hello, World!"
SCRIPT

# Сделать исполняемым
$ chmod +x hello.sh

# Запустить
$ ./hello.sh
```

**Output:**
```
Hello, World!
```

### 1.2 Shebang

**Shebang** (`#!`) указывает интерпретатор для выполнения скрипта.

**Example: Различные shebang**

```bash
#!/bin/bash        # Использовать bash
#!/bin/sh          # Использовать sh (POSIX)
#!/usr/bin/env bash # Использовать bash из PATH
```

> **💡 Pro Tip:**  
> `#!/usr/bin/env bash` более переносим, так как ищет bash в PATH, а не по фиксированному пути.

---

## 2. Переменные

Переменные в bash хранят данные, которые можно использовать в скриптах.

### 2.1 Объявление и присваивание

**Example: Базовое использование переменных**

```bash
# Присвоить значение
$ name="John"
$ age=25

# Использовать переменную
$ echo "Name: $name, Age: $age"
```

**Output:**
```
Name: John, Age: 25
```

**Example: В скрипте**

```bash
#!/bin/bash
name="Alice"
greeting="Hello, $name!"
echo "$greeting"
```

**Output:**
```
Hello, Alice!
```

### 2.2 Правила именования

- Имена переменных могут содержать буквы, цифры и подчёркивания
- Не могут начинаться с цифры
- Чувствительны к регистру

**Example: Валидные имена**

```bash
$ var1="value"
$ my_var="value"
$ MY_VAR="value"
$ _var="value"
```

### 2.3 Кавычки в переменных

**Example: Различия кавычек**

```bash
$ name="John"
$ echo "Hello, $name"      # Подстановка переменной
Hello, John

$ echo 'Hello, $name'      # Без подстановки
Hello, $name

$ echo Hello, $name        # Без кавычек (проблемы с пробелами)
Hello, John
```

Двойные кавычки позволяют подстановку переменных, одинарные — нет.

---

## 3. Локальные переменные

По умолчанию переменные глобальны. В функциях можно использовать `local`.

**Example: Локальные переменные в функциях**

```bash
#!/bin/bash
global_var="Global"

my_function() {
    local local_var="Local"
    echo "Inside function: $local_var"
    echo "Global in function: $global_var"
}

my_function
echo "Outside: $local_var"  # Пусто
echo "Global: $global_var"
```

**Output:**
```
Inside function: Local
Global in function: Global
Outside: 
Global: Global
```

---

## 4. Экспорт переменных (export)

`export` делает переменную доступной дочерним процессам.

**Example: Export переменных**

```bash
#!/bin/bash
MY_VAR="Hello"
export MY_VAR

# Дочерний процесс видит переменную
bash -c 'echo $MY_VAR'
```

**Output:**
```
Hello
```

Без `export` дочерний процесс не увидит переменную.

---

## 5. Readonly переменные

`readonly` делает переменную неизменяемой.

**Example: Readonly переменная**

```bash
#!/bin/bash
readonly PI=3.14159
PI=3.14  # Ошибка!
```

**Output:**
```
./script.sh: line 3: PI: readonly variable
```

---

## 6. Переменные окружения

Переменные окружения доступны всем процессам.

**Example: Основные переменные окружения**

```bash
$ echo $HOME      # Домашний каталог
/home/user

$ echo $PATH      # Пути поиска команд
/usr/local/bin:/usr/bin:/bin

$ echo $USER      # Имя пользователя
user

$ echo $SHELL     # Оболочка
/bin/bash
```

---

## 7. Shell-специфичные переменные

Bash предоставляет множество специальных переменных.

**Example: Специальные переменные**

```bash
$ echo $PWD           # Текущая директория
/home/user

$ echo $OLDPWD        # Предыдущая директория
/home

$ echo $PS1           # Приглашение командной строки
\u@\h:\w\$ 

$ echo $RANDOM        # Случайное число
12345

$ echo $SECONDS       # Секунд с начала сессии
3600

$ echo $LINENO        # Номер текущей строки (в скрипте)
42

$ echo $BASH_VERSION  # Версия bash
5.1.16(1)-release
```

---

## 8. Аргументы скрипта

Скрипты могут принимать аргументы через командную строку.

### 8.1 Позиционные параметры

**Example: Позиционные параметры**

```bash
#!/bin/bash
# script.sh arg1 arg2 arg3

echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"
```

```bash
$ ./script.sh one two three
```

**Output:**
```
First argument: one
Second argument: two
Third argument: three
```

`$1`, `$2`, `$3` и т.д. — это позиционные параметры.

### 8.2 Специальные параметры

**Example: Специальные параметры**

```bash
#!/bin/bash
echo "Script name: $0"
echo "All arguments: $*"
echo "All arguments (quoted): $@"
echo "Number of arguments: $#"
echo "Last command exit code: $?"
echo "Current PID: $$"
```

```bash
$ ./script.sh arg1 arg2 arg3
```

**Output:**
```
Script name: ./script.sh
All arguments: arg1 arg2 arg3
All arguments (quoted): arg1 arg2 arg3
Number of arguments: 3
Last command exit code: 0
Current PID: 12345
```

- `$0` — имя скрипта
- `$*` — все аргументы как одна строка
- `$@` — все аргументы как отдельные строки
- `$#` — количество аргументов
- `$?` — код возврата последней команды
- `$$` — PID текущего процесса

---

## 9. Exit Codes

Каждая команда возвращает код выхода (0-255).

**Example: Проверка exit code**

```bash
$ ls /existing
$ echo $?
0

$ ls /nonexistent
ls: cannot access '/nonexistent': No such file or directory
$ echo $?
2
```

Код 0 означает успех, ненулевой — ошибку.

**Example: Использование в скрипте**

```bash
#!/bin/bash
if ls /nonexistent 2>/dev/null; then
    echo "Success"
else
    echo "Failed with code: $?"
fi
```

**Output:**
```
Failed with code: 2
```

---

## 💡 Key Takeaways

- **Shebang** (`#!/bin/bash`) указывает интерпретатор для скрипта

- **Переменные** создаются присваиванием, используются с `$`

- **Export** делает переменные доступными дочерним процессам

- **Позиционные параметры** (`$1`, `$2`, ...) передают аргументы в скрипт

- **Специальные параметры** (`$*`, `$@`, `$#`, `$?`, `$$`) предоставляют метаинформацию

- **Exit codes** (`$?`) показывают результат выполнения команды (0 = успех)

---

## 🚀 Next Steps

**Related Modules:**

- [06_Conditions](../06_Conditions/) — условия (if/then/else)
- [08_Functions](../08_Functions/) — функции в bash

**Practice Ideas:**

1. Создайте скрипт, который принимает аргументы и выводит их
2. Попрактикуйтесь в работе с переменными и их экспорте
3. Изучите exit codes различных команд
4. Создайте скрипт, использующий специальные переменные bash

**Going Deeper:**

- Изучите parameter expansion (${var:-default}, ${var#pattern} и др.)
- Узнайте о массивах в bash
- Изучите scope переменных в функциях и subshells

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Variables](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html)
- [Bash Manual: Special Parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html)


