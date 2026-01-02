# Циклы
## for, while, until, break и continue

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать условия (модуль [06_Conditions](../06_Conditions/))
- Знать переменные и аргументы (модуль [05_Bash_Language](../05_Bash_Language/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать циклы for для итерации по спискам
- Применять while и until для условных циклов
- Использовать break и continue для управления циклом
- Вложенные циклы и комбинации

---

## 1. Цикл for

Цикл `for` выполняет команды для каждого элемента списка.

### 1.1 Базовый for

**Example: Простой for**

```bash
#!/bin/bash
for item in apple banana cherry; do
    echo "Fruit: $item"
done
```

**Output:**
```
Fruit: apple
Fruit: banana
Fruit: cherry
```

### 1.2 For с переменными

**Example: For с переменными**

```bash
#!/bin/bash
fruits="apple banana cherry"
for fruit in $fruits; do
    echo "Processing: $fruit"
done
```

### 1.3 C-стиль for

**Example: C-стиль for**

```bash
#!/bin/bash
for ((i=1; i<=5; i++)); do
    echo "Number: $i"
done
```

**Output:**
```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

## 2. Цикл while

Цикл `while` выполняется, пока условие истинно.

### 2.1 Базовый while

**Example: Простой while**

```bash
#!/bin/bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

**Output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### 2.2 While с чтением

**Example: Чтение из файла**

```bash
#!/bin/bash
while read line; do
    echo "Line: $line"
done < file.txt
```

---

## 3. Цикл until

Цикл `until` выполняется, пока условие ложно (противоположность while).

### 3.1 Базовый until

**Example: Простой until**

```bash
#!/bin/bash
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

## 4. break и continue

### 4.1 break

**Example: Выход из цикла**

```bash
#!/bin/bash
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done
```

**Output:**
```
1
2
3
4
```

### 4.2 continue

**Example: Пропуск итерации**

```bash
#!/bin/bash
for i in {1..10}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    echo $i
done
```

**Output:**
```
1
3
5
7
9
```

---

## 💡 Key Takeaways

- **for** — итерация по списку элементов

- **while** — выполнение пока условие истинно

- **until** — выполнение пока условие ложно

- **break** — выход из цикла

- **continue** — пропуск текущей итерации

---

## 🚀 Next Steps

**Related Modules:**

- [08_Functions](../08_Functions/) — функции
- [09_Text_Processing](../09_Text_Processing/) — обработка текста

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Looping Constructs](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)


