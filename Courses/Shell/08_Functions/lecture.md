# Функции
## Объявление, аргументы, возврат значений и локальные переменные

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать циклы (модуль [07_Loops](../07_Loops/))
- Знать переменные (модуль [05_Bash_Language](../05_Bash_Language/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объявлять и вызывать функции
- Передавать аргументы в функции
- Возвращать значения из функций
- Использовать локальные переменные
- Загружать скрипты через source

---

## 1. Объявление функций

### 1.1 Два способа объявления

**Example: Синтаксис function**

```bash

function my_function() {
    echo "Hello from function"
}
```

**Example: Синтаксис без function**

```bash

my_function() {
    echo "Hello from function"
}
```

Оба способа эквивалентны.

---

## 2. Аргументы функций

Функции принимают аргументы через позиционные параметры.

**Example: Аргументы функции**

```bash

greet() {
    echo "Hello, $1!"
}

greet "Alice"
```

**Output:**
```

Hello, Alice!
```

---

## 3. Возврат значений

Функции возвращают значения через exit code или вывод.

**Example: Exit code**

```bash

is_even() {
    if [ $(($1 % 2)) -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

if is_even 4; then
    echo "Even"
fi
```

**Example: Вывод**

```bash

get_name() {
    echo "Alice"
}

name=$(get_name)
echo "Name: $name"
```

---

## 4. Локальные переменные

**Example: local переменные**

```bash

my_function() {
    local local_var="Local value"
    global_var="Global value"
    echo "Local: $local_var"
}

my_function
echo "Global: $global_var"
echo "Local: $local_var"  # Пусто
```

---

## 5. source и .

Команды `source` и `.` загружают скрипт в текущую shell сессию.

**Example: Загрузка скрипта**

```bash
# В файле functions.sh
greet() {
    echo "Hello, $1!"
}

# Загрузить
source functions.sh
# или
. functions.sh

# Использовать
greet "Bob"
```

---

## 💡 Key Takeaways

- Функции объявляются через `function name()` или `name()`
- Аргументы доступны через `$1`, `$2`, и т.д.
- `return` устанавливает exit code, вывод через `echo`
- `local` создаёт локальные переменные
- `source` и `.` загружают скрипты в текущую сессию

---

## 🚀 Next Steps

**Related Modules:**

- [09_Text_Processing](../09_Text_Processing/) — работа с текстом
- [10_Arithmetic_Expansions](../10_Arithmetic_Expansions/) — расширения

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Shell Functions](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html)


