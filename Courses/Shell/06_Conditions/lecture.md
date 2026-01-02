# Условия
## if/then/else, test и [[ ]]

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать переменные и аргументы (модуль [05_Bash_Language](../05_Bash_Language/))
- Знать базовый синтаксис bash
- Понимать exit codes

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать конструкции if/then/else/elif/fi
- Применять команду test и её альтернативу [
- Использовать [[ ]] для расширенных проверок
- Сравнивать строки, числа и проверять файлы
- Комбинировать условия с логическими операторами

---

## 1. Базовый if/then/else

Конструкция `if` позволяет выполнять код в зависимости от условия.

### 1.1 Простой if

**Example: Базовый if**

```bash
#!/bin/bash
if [ "$1" = "hello" ]; then
    echo "Hello, World!"
fi
```

Если первый аргумент равен "hello", выводится сообщение.

### 1.2 if/else

**Example: if с else**

```bash
#!/bin/bash
if [ -f "$1" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
```

### 1.3 if/elif/else

**Example: Множественные условия**

```bash
#!/bin/bash
if [ "$1" -eq 0 ]; then
    echo "Zero"
elif [ "$1" -lt 0 ]; then
    echo "Negative"
else
    echo "Positive"
fi
```

---

## 2. Команда test и [

`test` и `[` — это команды для проверки условий.

### 2.1 Сравнение строк

**Example: Сравнение строк**

```bash

if [ "$var" = "value" ]; then
    echo "Equal"
fi

if [ "$var" != "value" ]; then
    echo "Not equal"
fi
```

### 2.2 Сравнение чисел

**Example: Числовые сравнения**

```bash

if [ "$num" -eq 10 ]; then    # равно
    echo "Equal to 10"
fi

if [ "$num" -lt 10 ]; then    # меньше
    echo "Less than 10"
fi

if [ "$num" -gt 10 ]; then    # больше
    echo "Greater than 10"
fi
```

Операторы: `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`.

### 2.3 Проверка файлов

**Example: Проверка файлов**

```bash

if [ -f "$file" ]; then       # обычный файл
    echo "File exists"
fi

if [ -d "$dir" ]; then         # директория
    echo "Directory exists"
fi

if [ -r "$file" ]; then        # читаемый
    echo "Readable"
fi
```

---

## 3. [[ ]] конструкция

`[[ ]]` — это встроенная конструкция bash с расширенными возможностями.

### 3.1 Преимущества [[ ]]

**Example: Безопасность с пробелами**

```bash
# С [ нужно кавычки
if [ "$var" = "value" ]; then

# С [[ кавычки не обязательны
if [[ $var == value ]]; then
```

### 3.2 Расширенные операторы

**Example: Pattern matching**

```bash

if [[ $file == *.txt ]]; then
    echo "Text file"
fi

if [[ $str =~ ^[0-9]+$ ]]; then
    echo "Only digits"
fi
```

---

## 4. Логические операторы

### 4.1 && и ||

**Example: Логические операторы**

```bash

if [ "$var" -gt 0 ] && [ "$var" -lt 100 ]; then
    echo "Between 0 and 100"
fi

if [ "$file" = "test.txt" ] || [ "$file" = "backup.txt" ]; then
    echo "Special file"
fi
```

### 4.2 В [[ ]]

**Example: Логические операторы в [[ ]]**

```bash

if [[ $num -gt 0 && $num -lt 100 ]]; then
    echo "Valid range"
fi
```

---

## 💡 Key Takeaways

- **if/then/else/elif/fi** — основная конструкция для условного выполнения

- **test и [** — команды для проверки условий, требуют кавычек

- **[[ ]]** — встроенная конструкция bash с расширенными возможностями

- **Логические операторы** (`&&`, `||`) позволяют комбинировать условия

- **Проверка файлов** (`-f`, `-d`, `-r` и др.) важна для безопасных скриптов

---

## 🚀 Next Steps

**Related Modules:**

- [07_Loops](../07_Loops/) — циклы (for, while)
- [08_Functions](../08_Functions/) — функции

**Practice Ideas:**

1. Создайте скрипт с различными условиями
2. Попрактикуйтесь в проверке файлов и директорий
3. Используйте логические операторы для сложных условий

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Conditional Constructs](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)


