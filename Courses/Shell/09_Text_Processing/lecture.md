# Работа с текстом
## grep, sed, awk, cut, sort, uniq

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать pipes и перенаправление (модуль [04_Streams_Pipes](../04_Streams_Pipes/))
- Знать базовые команды shell

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать grep для поиска в тексте
- Применять sed для редактирования текста
- Использовать awk для обработки данных
- Работать с cut, sort, uniq

---

## 1. grep — поиск в тексте

**Example: Базовое использование**

```bash

$ echo -e "apple\nbanana\ncherry" | grep "an"
banana
```

**Example: С опциями**

```bash

$ grep -i "ERROR" log.txt      # Игнорировать регистр
$ grep -r "pattern" dir/       # Рекурсивно
$ grep -v "exclude" file.txt   # Исключить строки
```

---

## 2. sed — потоковый редактор

**Example: Замена текста**

```bash

$ echo "Hello World" | sed 's/World/Universe/'
Hello Universe
```

**Example: Удаление строк**

```bash

$ sed '2d' file.txt            # Удалить строку 2
$ sed '/pattern/d' file.txt    # Удалить строки с pattern
```

---

## 3. awk — обработка данных

**Example: Базовое использование**

```bash

$ echo -e "1 apple\n2 banana" | awk '{print $2}'
apple
banana
```

**Example: С условиями**

```bash

$ awk '$1 > 10 {print $2}' data.txt
```

---

## 4. cut — извлечение полей

**Example: Извлечение колонок**

```bash

$ echo "name:age:city" | cut -d: -f1,3
name:city
```

---

## 5. sort и uniq

**Example: Сортировка**

```bash

$ sort file.txt
$ sort -r file.txt             # Обратный порядок
$ sort -n numbers.txt          # Числовая сортировка
```

**Example: Уникальные строки**

```bash

$ sort file.txt | uniq
$ uniq -c file.txt             # С подсчётом
```

---

## 💡 Key Takeaways

- **grep** — поиск паттернов в тексте

- **sed** — потоковое редактирование

- **awk** — обработка структурированных данных

- **cut** — извлечение полей

- **sort/uniq** — сортировка и уникальные значения

---

## 🚀 Next Steps

**Related Modules:**

- [10_Arithmetic_Expansions](../10_Arithmetic_Expansions/) — расширения

---

## 📚 Additional Resources

**Documentation:**

- [GNU grep Manual](https://www.gnu.org/software/grep/manual/)
- [GNU sed Manual](https://www.gnu.org/software/sed/manual/)
- [GNU awk Manual](https://www.gnu.org/software/gawk/manual/)


