# Арифметика и расширения
## Арифметические операции, parameter expansion, command substitution

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать переменные (модуль [05_Bash_Language](../05_Bash_Language/))
- Знать функции (модуль [08_Functions](../08_Functions/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Выполнять арифметические операции
- Использовать parameter expansion
- Применять command substitution
- Работать с process substitution и here documents

---

## 1. Арифметические операции

### 1.1 $(( ))

**Example: Арифметическое расширение**

```bash
$ echo $((2 + 3))
5

$ x=10
$ y=5
$ echo $((x + y))
15
```

### 1.2 let

**Example: Команда let**

```bash
$ let "result=2+3"
$ echo $result
5
```

---

## 2. Parameter Expansion

### 2.1 Базовые формы

**Example: ${var}**

```bash
$ name="John"
$ echo ${name}
John
```

### 2.2 Значения по умолчанию

**Example: ${var:-default}**

```bash
$ echo ${unset_var:-"default"}
default

$ var="value"
$ echo ${var:-"default"}
value
```

### 2.3 Присваивание

**Example: ${var:=default}**

```bash
$ unset var
$ echo ${var:=default}
default
$ echo $var
default
```

---

## 3. Command Substitution

### 3.1 $( )

**Example: Command substitution**

```bash
$ files=$(ls)
$ echo "Files: $files"
```

### 3.2 ``

**Example: Старый синтаксис**

```bash
$ files=`ls`
$ echo "Files: $files"
```

Рекомендуется использовать `$()`.

---

## 4. Process Substitution

**Example: <()**

```bash
$ diff <(ls dir1) <(ls dir2)
```

---

## 5. Here Documents

**Example: <<**

```bash
$ cat << EOF
Line 1
Line 2
EOF
```

---

## 💡 Key Takeaways

- **$(( ))** — арифметическое расширение

- **Parameter expansion** — мощные возможности работы с переменными

- **Command substitution** — выполнение команд и использование вывода

- **Process substitution** — использование вывода команд как файлов

- **Here documents** — передача многострочного текста

---

## 🚀 Next Steps

**Related Modules:**

- [11_Builtins_Keywords](../11_Builtins_Keywords/) — встроенные команды

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)


