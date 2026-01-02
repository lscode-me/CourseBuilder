# Табличные данные
## CSV, TSV: чтение, запись и обработка

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать текстовые форматы файлов
- Знать основы работы с файлами в Python
- Иметь базовое представление о таблицах (строки, колонки)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Читать и писать CSV файлы
- Обрабатывать типичные проблемы CSV
- Использовать командные утилиты для CSV
- Работать с CSV в Python

---

## 1. Что такое CSV

### 1.1 Определение

**CSV** (Comma-Separated Values) — текстовый формат для табличных данных.

```csv
name,age,city
Alice,30,Moscow
Bob,25,London
Charlie,35,Paris
```

### 1.2 Преимущества и недостатки

**Преимущества:**

- Простой текстовый формат
- Универсальная поддержка (Excel, базы данных, языки)
- Компактный
- Человекочитаемый

**Недостатки:**

- Нет стандарта (RFC 4180 — рекомендация, не требование)
- Нет типов данных (всё — строки)
- Проблемы с разделителями в данных
- Нет метаданных

---

## 2. Синтаксис CSV

### 2.1 Базовый формат

```csv
header1,header2,header3
value1,value2,value3
value4,value5,value6
```

### 2.2 Кавычки для специальных значений

```csv
name,description,price
"Widget","Simple widget",9.99
"Gadget","Has a comma, inside",19.99
"Thing","Has ""quotes"" inside",29.99
"Item","Has
newline",39.99
```

Правила кавычек:

- Значение с запятой → в кавычки
- Значение с кавычками → удваиваем кавычки `""`
- Значение с переносом строки → в кавычки

### 2.3 TSV (Tab-Separated Values)

```tsv
name	age	city
Alice	30	Moscow
Bob	25	London
```

Преимущество: табы редко встречаются в данных.

---

## 3. Проблемы CSV

### 3.1 Кодировка

```python
# Файл в Windows-1251

with open('data.csv', 'r', encoding='cp1251') as f:
    # ...

# Файл с BOM

with open('data.csv', 'r', encoding='utf-8-sig') as f:
    # ...
```

### 3.2 Разделители

```python
# Точка с запятой (европейский стандарт)
# name;age;city

import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
```

### 3.3 Пустые значения

```csv
name,age,city
Alice,30,
Bob,,London
,25,Paris
```

---

## 4. CSV в командной строке

### 4.1 Просмотр

```bash
# Просмотр

cat data.csv
head -5 data.csv
tail -5 data.csv

# Красивый вывод

column -t -s, data.csv

# Подсчёт строк (минус заголовок)

wc -l data.csv
```

### 4.2 Обработка с awk

```bash
# Выбор колонок (1 и 3)

awk -F, '{print $1,$3}' data.csv

# Фильтрация по условию

awk -F, '$2 > 30 {print $1}' data.csv

# Сумма колонки

awk -F, 'NR>1 {sum+=$2} END {print sum}' data.csv
```

### 4.3 csvkit (рекомендуется)

```bash
# Установка

pip install csvkit

# Просмотр

csvlook data.csv

# Статистика

csvstat data.csv

# Выбор колонок

csvcut -c name,age data.csv

# Фильтрация

csvgrep -c age -m 30 data.csv

# Сортировка

csvsort -c age data.csv

# Конвертация в JSON

csvjson data.csv

# SQL запросы к CSV!

csvsql --query "SELECT name, age FROM data WHERE age > 25" data.csv
```

---

## 5. CSV в Python

### 5.1 Модуль csv

```python
import csv

# Чтение как списки

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # Первая строка — заголовок
    for row in reader:
        print(row)  # ['Alice', '30', 'Moscow']

# Чтение как словари

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

### 5.2 Запись CSV

```python
import csv

# Запись списков

data = [
    ['name', 'age', 'city'],
    ['Alice', 30, 'Moscow'],
    ['Bob', 25, 'London'],
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Запись словарей

users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
]

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(users)
```

### 5.3 Параметры csv

```python
import csv

# Европейский формат (точка с запятой, запятая в числах)

with open('european.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')

# Excel формат

with open('excel.csv', newline='') as f:
    reader = csv.reader(f, dialect='excel')

# Кастомный формат

csv.register_dialect('custom',
    delimiter='|',
    quoting=csv.QUOTE_ALL)
```

### 5.4 pandas для CSV

```python
import pandas as pd

# Чтение

df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', encoding='cp1251', sep=';')

# Базовые операции

print(df.head())
print(df.describe())
print(df[df['age'] > 25])

# Запись

df.to_csv('output.csv', index=False)
```

---

## 6. Best Practices

### 6.1 Рекомендации

```python
# Всегда указывайте
# - encoding='utf-8'
# - newline='' (важно для Windows)

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Используйте DictReader/DictWriter для читаемости
```

### 6.2 Валидация

```python
def validate_csv(filepath):
    """Проверка CSV файла."""
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        expected_columns = len(header)
        
        for i, row in enumerate(reader, start=2):
            if len(row) != expected_columns:
                print(f"Row {i}: expected {expected_columns}, got {len(row)}")
```

---

## 💡 Key Takeaways

- **CSV — простой, но хитрый**: Кавычки, разделители, кодировки требуют внимания.

- **newline=''**: Всегда используйте при открытии CSV в Python.

- **csvkit**: Мощные инструменты для работы с CSV в командной строке.

- **pandas**: Для сложной обработки используйте pandas.

---

## 📚 Additional Resources

- [RFC 4180](https://tools.ietf.org/html/rfc4180)
- [csvkit Documentation](https://csvkit.readthedocs.io/)
- [pandas CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

---

## 🚀 Next Steps

**Следующие модули:**

- [10_Compression](../10_Compression/) — Сжатие данных (gzip, zip, tar)
- [11_Checksums](../11_Checksums/) — Контрольные суммы и хеширование

**Практика:**

1. Обработайте CSV файл с помощью csvkit в командной строке
2. Загрузите и проанализируйте табличные данные с pandas
3. Напишите скрипт конвертации между CSV, TSV и JSON






