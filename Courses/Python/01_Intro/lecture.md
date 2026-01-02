# Python
## Введение в язык: история, философия, установка и первые шаги

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь работать с компьютером на уровне пользователя
- Понимать основы алгоритмов (последовательность действий, циклы, условия)
- Иметь представление об устройстве вычислительных систем
- Иметь доступ к Linux или macOS (для практики)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить, что такое Python и для чего он используется
- Установить и настроить Python на своей системе
- Запускать Python-код в интерактивном режиме и из файлов
- Использовать основные инструменты разработчика Python
- Написать и запустить свою первую Python-программу

---

## 1. Что такое Python

Python — это высокоуровневый интерпретируемый язык программирования общего назначения. Он был создан Гвидо ван Россумом и впервые выпущен в 1991 году. Название языка происходит не от змеи, а от британского комедийного шоу "Monty Python's Flying Circus".

Python отличается простым и читаемым синтаксисом, что делает его идеальным языком для начинающих программистов. При этом он достаточно мощный для решения сложных задач в профессиональной разработке.

### 1.1 Ключевые особенности

**Python — интерпретируемый язык:**

```python
# Код выполняется построчно интерпретатором

print("Hello, Python!")
```

**Output:**
```
Hello, Python!
```

В отличие от компилируемых языков (C, C++, Go), код Python не требует предварительной компиляции в машинный код. Интерпретатор читает и выполняет код построчно.

**Python — динамически типизированный:**

```python
# Переменная может менять тип

x = 42        # x — целое число
print(type(x))

x = "hello"   # теперь x — строка
print(type(x))

x = [1, 2, 3] # теперь x — список
print(type(x))
```

**Output:**
```
<class 'int'>
<class 'str'>
<class 'list'>
```

Тип переменной определяется автоматически во время выполнения программы, а не при компиляции.

### 1.2 Философия Python

Python следует особой философии, записанной в документе "The Zen of Python" (PEP 20). Посмотреть её можно, выполнив:

```python
import this
```

**Output:**
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Главные принципы:

- **Читаемость важна** — код читают чаще, чем пишут

- **Явное лучше неявного** — код должен быть понятным

- **Простое лучше сложного** — не усложняйте без необходимости

---

## 2. Почему Python

### 2.1 Преимущества языка

**Простота изучения:**

```python
# Python — очень читаемый язык
# Сравните с аналогичным кодом на других языках

# Python

numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)
```

**Output:**
```
[2, 4, 6, 8, 10]
```

**Богатая стандартная библиотека:**

```python
# Работа с датами "из коробки"

from datetime import datetime

now = datetime.now()
print(f"Сейчас: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Работа с JSON

import json
data = {"name": "Python", "year": 1991}
print(json.dumps(data, indent=2))
```

**Output:**
```
Сейчас: 2024-12-02 15:30:00
{
  "name": "Python",
  "year": 1991
}
```

**Огромная экосистема:**

- Веб-разработка: Django, Flask, FastAPI
- Data Science: NumPy, Pandas, Matplotlib
- Machine Learning: TensorFlow, PyTorch, scikit-learn
- Автоматизация: Ansible, Salt
- DevOps: скрипты, утилиты, инструменты

### 2.2 Области применения

| Область | Примеры использования | Популярные библиотеки |
|---------|----------------------|----------------------|
| Веб-разработка | Сайты, API, микросервисы | Django, Flask, FastAPI |
| Data Science | Анализ данных, визуализация | Pandas, NumPy, Matplotlib |
| Machine Learning | Модели, нейросети | TensorFlow, PyTorch |
| Автоматизация | Скрипты, боты, парсинг | Selenium, BeautifulSoup |
| DevOps | Инфраструктура как код | Ansible, Fabric |
| Наука | Вычисления, моделирование | SciPy, SymPy |

### 2.3 Кто использует Python

Python используют крупнейшие компании мира:

- **Google** — один из основных языков разработки

- **Netflix** — анализ данных и машинное обучение

- **Instagram** — бэкенд на Django

- **Spotify** — анализ данных и рекомендации

- **NASA** — научные вычисления

- **Dropbox** — большая часть кода написана на Python

---

## 3. Версии Python

### 3.1 Python 2 vs Python 3

Python имеет две основные ветки: Python 2 и Python 3. **Python 2 официально прекратил поддержку 1 января 2020 года.** Всегда используйте Python 3!

```python
# Python 3 синтаксис

print("Hello, World!")  # print — функция

# Деление в Python 3

print(5 / 2)   # Истинное деление
print(5 // 2)  # Целочисленное деление
```

**Output:**
```
Hello, World!
2.5
2
```

**Основные различия:**

| Аспект | Python 2 (устарел) | Python 3 (актуальный) |
|--------|-------------------|----------------------|
| print | `print "hello"` | `print("hello")` |
| Деление | `5/2 = 2` | `5/2 = 2.5` |
| Строки | ASCII по умолчанию | Unicode по умолчанию |
| range() | Возвращает список | Возвращает итератор |

### 3.2 Актуальные версии Python 3

На момент написания курса актуальны версии:

- **Python 3.11** — стабильная, рекомендуемая

- **Python 3.12** — новейшая, с улучшениями производительности

Проверить версию Python:

```bash
python3 --version
```

**Output:**
```
Python 3.11.5
```

> **💡 Pro Tip:**  
> Для учебных целей используйте последнюю стабильную версию Python 3.x. Для production-проектов выбирайте версию, которую поддерживают все ваши зависимости.

---

## 4. Установка Python

### 4.1 Проверка установленной версии

На большинстве Linux-систем и macOS Python уже установлен:

```bash
# Проверка версии Python 3

python3 --version

# Проверка пути к интерпретатору

which python3
```

**Output:**
```
Python 3.11.5
/usr/bin/python3
```

### 4.2 Установка на macOS

**Рекомендуемый способ — через Homebrew:**

```bash
# Установка Homebrew (если не установлен)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установка Python

brew install python3

# Проверка

python3 --version
```

### 4.3 Установка на Linux

**Ubuntu/Debian:**

```bash
# Обновление списка пакетов

sudo apt update

# Установка Python 3 и pip

sudo apt install python3 python3-pip python3-venv

# Проверка

python3 --version
pip3 --version
```

**Fedora/RHEL:**

```bash
# Установка Python 3

sudo dnf install python3 python3-pip

# Проверка

python3 --version
```

### 4.4 Использование pyenv (рекомендуется)

**pyenv** позволяет легко управлять несколькими версиями Python:

```bash
# Установка pyenv (macOS/Linux)

curl https://pyenv.run | bash

# Добавьте в ~/.bashrc или ~/.zshrc:

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Перезагрузите shell

source ~/.bashrc

# Установка конкретной версии Python

pyenv install 3.11.5

# Установка версии по умолчанию

pyenv global 3.11.5

# Проверка

python --version
```

**Output:**
```
Python 3.11.5
```

> **⚠️ Warning:**  
> Избегайте установки пакетов в системный Python (тот, что идёт с ОС) напрямую через `pip`. Это может вызвать конфликты с системными утилитами. Всегда используйте виртуальные окружения.

---

## 5. Способы запуска Python-кода

### 5.1 Интерактивный режим (REPL)

REPL (Read-Eval-Print Loop) — отличный способ экспериментировать с Python:

```bash
python3
```

```python
>>> 2 + 2
4
>>> name = "Python"
>>> print(f"Hello, {name}!")
Hello, Python!
>>> exit()
```

Для выхода из интерактивного режима используйте `exit()` или `Ctrl+D`.

### 5.2 Выполнение скриптов

Создайте файл `hello.py`:

```python
# hello.py

name = input("Как тебя зовут? ")
print(f"Привет, {name}! Добро пожаловать в Python!")
```

Запуск:

```bash
python3 hello.py
```

**Output:**
```
Как тебя зовут? Мир
Привет, Мир! Добро пожаловать в Python!
```

### 5.3 Исполняемые скрипты

На Linux/macOS можно делать Python-скрипты исполняемыми:

```python
#!/usr/bin/env python3
# executable_script.py

"""
Этот скрипт можно запускать напрямую
"""

print("Я исполняемый Python-скрипт!")
```

```bash
# Делаем файл исполняемым

chmod +x executable_script.py

# Запускаем напрямую

./executable_script.py
```

**Output:**
```
Я исполняемый Python-скрипт!
```

Строка `#!/usr/bin/env python3` называется **shebang** и указывает системе, какой интерпретатор использовать.

### 5.4 IPython и Jupyter

**IPython** — улучшенный интерактивный интерпретатор:

```bash
# Установка

pip3 install ipython

# Запуск

ipython
```

```python
In [1]: import math

In [2]: math.sqrt(16)
Out[2]: 4.0

In [3]: %timeit sum(range(1000))
12.8 µs ± 156 ns per loop
```

**Jupyter Notebook** — интерактивная среда для экспериментов:

```bash
# Установка

pip3 install jupyter

# Запуск

jupyter notebook
```

---

## 6. Инструменты разработчика

### 6.1 pip — менеджер пакетов

**pip** используется для установки сторонних библиотек:

```bash
# Установка пакета

pip3 install requests

# Установка конкретной версии

pip3 install requests==2.28.0

# Обновление пакета

pip3 install --upgrade requests

# Удаление пакета

pip3 uninstall requests

# Просмотр установленных пакетов

pip3 list

# Сохранение зависимостей проекта

pip3 freeze > requirements.txt

# Установка из файла зависимостей

pip3 install -r requirements.txt
```

### 6.2 Виртуальные окружения

**Виртуальные окружения** изолируют зависимости проектов:

```bash
# Создание виртуального окружения

python3 -m venv myproject_env

# Активация (Linux/macOS)

source myproject_env/bin/activate

# Проверка — теперь python указывает на окружение

which python
# /path/to/myproject_env/bin/python

# Установка пакетов в окружение

pip install requests pandas

# Деактивация окружения

deactivate
```

**Пример workflow:**

```bash
# 1. Создаем директорию проекта

mkdir my_project && cd my_project

# 2. Создаем виртуальное окружение

python3 -m venv venv

# 3. Активируем его

source venv/bin/activate

# 4. Устанавливаем зависимости

pip install requests

# 5. Работаем над проектом

python main.py

# 6. Сохраняем зависимости

pip freeze > requirements.txt

# 7. По завершении работы деактивируем

deactivate
```

> **💡 Pro Tip:**  
> Всегда используйте виртуальные окружения для каждого проекта. Это позволяет избежать конфликтов зависимостей между проектами.

### 6.3 Редакторы и IDE

**Популярные редакторы для Python:**

| Редактор | Преимущества | Для кого |
|----------|-------------|----------|
| VS Code | Бесплатный, легкий, расширяемый | Начинающие и средний уровень |
| PyCharm | Мощная IDE, отличная поддержка Python | Профессионалы |
| Vim/Neovim | Быстрый, работает везде | Опытные пользователи |
| Sublime Text | Быстрый, минималистичный | Любители лёгкости |

**Настройка VS Code для Python:**

1. Установите расширение "Python" от Microsoft
2. Установите расширение "Pylance" для лучшего автодополнения
3. Выберите интерпретатор: `Cmd/Ctrl + Shift + P` → "Python: Select Interpreter"

---

## 7. Первая программа

### 7.1 Hello, World!

Традиционно изучение языка начинается с программы "Hello, World!":

```python
# hello_world.py

print("Hello, World!")
```

**Output:**
```
Hello, World!
```

### 7.2 Чуть сложнее

Программа с переменными и выводом:

```python
# greeting.py

# Объявление переменных

language = "Python"
version = 3.11
creator = "Guido van Rossum"

# Вывод информации

print(f"Добро пожаловать в {language}!")
print(f"Версия: {version}")
print(f"Создатель: {creator}")
print(f"Python существует с 1991 года")

# Простые вычисления

current_year = 2024
age = current_year - 1991
print(f"Возраст языка: {age} лет")
```

**Output:**
```
Добро пожаловать в Python!
Версия: 3.11
Создатель: Guido van Rossum
Python существует с 1991 года
Возраст языка: 33 лет
```

### 7.3 Интерактивная программа

Программа с вводом от пользователя:

```python
# calculator.py

# Получаем ввод от пользователя

print("Простой калькулятор")
print("-" * 20)

# input() всегда возвращает строку

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

# Преобразуем строки в числа

num1 = float(num1)
num2 = float(num2)

# Выполняем вычисления

print(f"\nРезультаты:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
```

**Output:**
```
Простой калькулятор
--------------------
Введите первое число: 10
Введите второе число: 3

Результаты:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.3333333333333335
```

---

## 8. Базовый синтаксис

### 8.1 Отступы

Python использует отступы для обозначения блоков кода. Это одна из главных особенностей языка:

```python
# Правильно — отступы определяют блоки

if True:
    print("Этот код внутри блока if")
    print("И этот тоже")
print("А этот уже снаружи")
```

**Output:**
```
Этот код внутри блока if
И этот тоже
А этот уже снаружи
```

❌ **Неправильно:**
```python
# Это вызовет ошибку IndentationError

if True:
print("Нет отступа!")
```

> **⚠️ Warning:**  
> Используйте 4 пробела для отступов. Не смешивайте пробелы и табуляцию. Настройте редактор на автоматическую замену Tab на 4 пробела.

### 8.2 Комментарии

```python
# Однострочный комментарий

# Многострочный комментарий
# можно писать
# в несколько строк

"""
Docstring — строка документации.
Используется для документирования
модулей, классов и функций.
"""

def greet(name):
    """
    Приветствует пользователя по имени.
    
    Args:
        name: Имя пользователя
    
    Returns:
        Строка приветствия
    """
    return f"Привет, {name}!"

# Посмотреть документацию функции

print(greet.__doc__)
```

**Output:**
```
    Приветствует пользователя по имени.
    
    Args:
        name: Имя пользователя
    
    Returns:
        Строка приветствия
```

### 8.3 Переменные и присваивание

```python
# Простое присваивание

x = 10
name = "Python"

# Множественное присваивание

a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Обмен значениями

a, b = b, a
print(f"После обмена: a={a}, b={b}")

# Присваивание одного значения нескольким переменным

x = y = z = 0
print(f"x={x}, y={y}, z={z}")
```

**Output:**
```
a=1, b=2, c=3
После обмена: a=2, b=1
x=0, y=0, z=0
```

### 8.4 Именование переменных

**Правила:**

- Имя начинается с буквы или `_`
- Содержит буквы, цифры, `_`
- Регистр важен: `name` и `Name` — разные переменные

**Конвенции (PEP 8):**

```python
# snake_case для переменных и функций

user_name = "John"
max_value = 100

def calculate_total():
    pass

# UPPER_CASE для констант

MAX_SIZE = 1000
PI = 3.14159

# PascalCase для классов

class UserAccount:
    pass

# _prefix для "приватных" имён

_internal_value = 42
```

---

## 9. Common Pitfalls

### 9.1 Python 2 vs Python 3

❌ **Ошибка:** Использование синтаксиса Python 2

```python
# Python 2 (НЕ РАБОТАЕТ в Python 3)
# print "Hello"

# Python 3 (правильно)

print("Hello")
```

### 9.2 Неправильные отступы

❌ **Ошибка:** Смешивание пробелов и табов

```python
# Настройте редактор на 4 пробела!

if True:
    print("4 пробела")
    print("Тоже 4 пробела")  # Правильно
```

### 9.3 Путаница с версией интерпретатора

```bash
# Убедитесь, что используете правильную версию

python3 --version      # Рекомендуется
python --version       # Может быть Python 2!

# Используйте python3 явно

python3 my_script.py
```

### 9.4 Установка пакетов без виртуального окружения

❌ **Плохо:**
```bash
pip install some_package  # В системный Python!
```

✅ **Хорошо:**
```bash
# Сначала создаём и активируем виртуальное окружение

python3 -m venv venv
source venv/bin/activate
pip install some_package  # Теперь в изолированное окружение
```

---

## 💡 Key Takeaways

- **Python — простой и мощный**: Легко изучить, но способен решать сложные задачи. Идеальный первый язык программирования.

- **Всегда используйте Python 3**: Python 2 устарел. Используйте последнюю стабильную версию Python 3.x.

- **Виртуальные окружения обязательны**: Изолируйте зависимости каждого проекта с помощью `venv` для избежания конфликтов.

- **Отступы — часть синтаксиса**: Python использует отступы вместо скобок. Используйте 4 пробела.

- **Читаемость важна**: Следуйте PEP 8 и философии "The Zen of Python" для написания чистого кода.

---

## 🚀 Next Steps

**Related Modules:**

- [Data Structures](../02_DataStructures/) — изучите числа, строки, списки и словари
- [Flow Control](../03_FlowControl/) — условия и циклы

**Practice Ideas:**

1. Установите Python с помощью pyenv и создайте первое виртуальное окружение
2. Напишите программу, которая спрашивает имя и выводит приветствие
3. Создайте калькулятор с операциями сложения, вычитания, умножения и деления
4. Поэкспериментируйте в REPL с различными типами данных

**Going Deeper:**

- Изучите PEP 8 — руководство по стилю Python
- Прочитайте "The Zen of Python" и подумайте над каждым принципом
- Настройте любимый редактор для работы с Python

---

## 📚 Additional Resources

**Documentation:**

- [Python Official Documentation](https://docs.python.org/3/) — официальная документация
- [Python Tutorial](https://docs.python.org/3/tutorial/) — официальный учебник

**Style Guides:**

- [PEP 8](https://peps.python.org/pep-0008/) — руководство по стилю кода
- [PEP 20](https://peps.python.org/pep-0020/) — The Zen of Python

**Tools:**

- [pyenv](https://github.com/pyenv/pyenv) — управление версиями Python
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) — расширение для VS Code

---





