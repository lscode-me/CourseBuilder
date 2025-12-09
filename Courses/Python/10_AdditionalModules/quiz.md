# Python Third-Party Modules (pip) - Quiz

Проверьте свои знания по теме "Популярные сторонние модули из PyPI".

---

## Question 1: pip


Что такое pip?

A) Менеджер пакетов Python

B) Интерпретатор Python

C) Библиотека для работы с изображениями

D) Фреймворк для веб-разработки

---

## Question 2: Установка пакета


Как установить последнюю версию пакета requests?

A) `pip get requests`

B) `python install requests`

C) `import requests --install`

D) `pip install requests`

---

## Question 3: requests


Какой метод отправляет GET-запрос в библиотеке requests?

A) `requests.download()`

B) `requests.fetch()`

C) `requests.get()`

D) `requests.read()`

---

## Question 4: requests response


Как получить JSON из ответа requests?

A) `json.loads(response)`

B) `response.content`

C) `response.text`

D) `response.json()`

---

## Question 5: HTTP Status Code


Какое свойство содержит код статуса HTTP?

A) `response.code`

B) `response.status`

C) `response.status_code`

D) `response.http_code`

---

## Question 6: requests POST


Как отправить POST-запрос с JSON-данными?

A) `requests.send(url, method='POST', data=data)`

B) `requests.post(url, json=data_dict)`

C) `requests.post(url).json(data_dict)`

D) `requests.post(url, data=json_data)`

---

## Question 7: NumPy


Для чего используется NumPy?

A) Веб-разработка

B) Машинное обучение

C) Числовые вычисления и работа с массивами

D) Парсинг HTML

---

## Question 8: NumPy массив


Как создать NumPy массив?

A) `numpy.array([1, 2, 3])`

B) `numpy.create([1, 2, 3])`

C) `numpy.new([1, 2, 3])`

D) `numpy.list([1, 2, 3])`

---

## Question 9: NumPy операции


Что выведет следующий код?

```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 2)
```

A) 6

B) Error

C) [2, 4, 6]

D) [1, 2, 3, 1, 2, 3]

---

## Question 10: Pandas


Что такое DataFrame в Pandas?

A) Одномерный массив

B) Двумерная табличная структура данных

C) График

D) Словарь

---

## Question 11: Создание DataFrame


Как создать DataFrame из словаря?

A) `pd.create(dict)`

B) `pd.DataFrame(dict)`

C) `DataFrame.new(dict)`

D) `pd.from_dict(dict)`

---

## Question 12: Чтение CSV


Какая функция читает CSV файл в Pandas?

A) `pd.import_csv()`

B) `pd.csv_read()`

C) `pd.load_csv()`

D) `pd.read_csv()`

---

## Question 13: Выбор колонки


Как выбрать колонку 'name' из DataFrame df?

A) `df->name`

B) `df.name` или `df['name']`

C) `df.get_column('name')`

D) `df.column('name')`

---

## Question 14: Flask


Что такое Flask?

A) Микро веб-фреймворк

B) Тестовый фреймворк

C) ORM библиотека

D) База данных

---

## Question 15: Flask маршрут


Как определить маршрут в Flask?

A) `@app.url('/')`

B) `@app.route('/')`

C) `app.path('/')`

D) `@route('/')`

---

## Question 16: Flask запуск


Как запустить Flask-приложение в режиме отладки?

A) Оба варианта A и C

B) `app.start(debug=True)`

C) `app.run(debug=True)`

D) `flask run --debug`

---

## Question 17: pytest


Как обозначается тестовая функция в pytest?

A) Любое имя

B) Наследует от TestCase

C) Декоратор `@test`

D) Начинается с `test_`

---

## Question 18: pytest assert


Какой синтаксис проверки в pytest?

A) `expect(a).toBe(b)`

B) `assert a == b`

C) `self.assertEqual(a, b)`

D) `verify(a == b)`

---

## Question 19: pytest фикстуры


Для чего используются фикстуры в pytest?

A) Для отчётов

B) Для форматирования кода

C) Для параллельного выполнения

D) Для подготовки тестового окружения

---

## Question 20: Beautiful Soup


Для чего используется Beautiful Soup?

A) Веб-разработка

B) Машинное обучение

C) Работа с базами данных

D) Парсинг HTML/XML

---

## Question 21: Pillow


Что такое Pillow?

A) Библиотека для обработки изображений

B) Веб-фреймворк

C) ORM

D) Тестовый фреймворк

---

## Question 22: SQLAlchemy


Что такое SQLAlchemy?

A) Веб-фреймворк

B) Библиотека для тестирования

C) ORM и инструменты для работы с базами данных

D) База данных

---

## Question 23: virtualenv vs venv


В чём разница между virtualenv и venv?

A) virtualenv быстрее

B) Нет разницы

C) venv встроен в Python 3, virtualenv — сторонний пакет

D) venv не работает на Windows

---

## Question 24: requirements.txt


Как создать requirements.txt с текущими пакетами?

A) `pip export requirements.txt`

B) `pip freeze > requirements.txt`

C) `pip save > requirements.txt`

D) `pip list > requirements.txt`

---

## Question 25: PyPI


Что такое PyPI?

A) Python Performance Index

B) Python Project Installer

C) Python Programming Interface

D) Python Package Index — репозиторий пакетов

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | pip (Pip Installs Packages) — стандартный менеджер пакетов Python. |
| 2 | D | `pip install package` устанавливает пакет из PyPI. |
| 3 | C | `requests.get(url)` отправляет GET-запрос. |
| 4 | D | `response.json()` автоматически парсит JSON-ответ. |
| 5 | C | `status_code` содержит HTTP-код: 200, 404, 500 и т.д. |
| 6 | B | `json=data_dict` автоматически сериализует и устанавливает Content-Type. |
| 7 | C | NumPy — библиотека для эффективных числовых вычислений и массивов. |
| 8 | A | `np.array()` создаёт ndarray из списка или другого итерируемого. |
| 9 | C | NumPy поддерживает векторизованные операции: [1,2,3] * 2 = [2,4,6]. |
| 10 | B | DataFrame — двумерная таблица с именованными колонками и индексом. |
| 11 | B | `pd.DataFrame(dict)` — основной способ создания из словаря. |
| 12 | D | `pd.read_csv('file.csv')` читает CSV в DataFrame. |
| 13 | B | `df['name']` или `df.name` (для имён без спецсимволов). |
| 14 | A | Flask — легковесный веб-фреймворк для Python. |
| 15 | B | `@app.route('/path')` связывает URL с функцией. |
| 16 | A | Оба способа работают: `app.run(debug=True)` и `flask run --debug`. |
| 17 | D | pytest автоматически находит функции, начинающиеся с `test_`. |
| 18 | B | pytest использует стандартный `assert` с улучшенными сообщениями. |
| 19 | D | Фикстуры готовят данные/ресурсы для тестов, управляют setup/teardown. |
| 20 | D | Beautiful Soup (bs4) парсит HTML/XML и позволяет навигацию по DOM. |
| 21 | A | Pillow (PIL fork) — библиотека для обработки изображений. |
| 22 | C | SQLAlchemy — ORM и SQL toolkit для Python. |
| 23 | C | venv — встроенный модуль Python 3.3+. virtualenv — сторонний, с дополнительными фичами. |
| 24 | B | `pip freeze` выводит установленные пакеты в формате requirements. |
| 25 | D | PyPI (Python Package Index) — официальный репозиторий Python-пакетов. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание экосистемы Python! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Попрактикуйтесь с requests и pandas. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Установите и попробуйте использовать основные библиотеки. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Начните с практического использования pip и requests. |

---

