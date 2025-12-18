# Python Third-Party Modules (pip) - Quiz

Проверьте свои знания по теме "Популярные сторонние модули из PyPI".

---

## Question 1: pip

Что такое pip?

A) Интерпретатор Python

B) Библиотека для работы с изображениями

C) Менеджер пакетов Python

D) Фреймворк для веб-разработки

---

## Question 2: Установка пакета

Как установить последнюю версию пакета requests?

A) `python install requests`

B) `pip get requests`

C) `pip install requests`

D) `import requests --install`

---

## Question 3: requests

Какой метод отправляет GET-запрос в библиотеке requests?

A) `requests.fetch()`

B) `requests.read()`

C) `requests.download()`

D) `requests.get()`

---

## Question 4: requests response

Как получить JSON из ответа requests?

A) `json.loads(response)`

B) `response.json()`

C) `response.text`

D) `response.content`

---

## Question 5: HTTP Status Code

Какое свойство содержит код статуса HTTP?

A) `response.http_code`

B) `response.code`

C) `response.status`

D) `response.status_code`

---

## Question 6: requests POST

Как отправить POST-запрос с JSON-данными?

A) `requests.post(url).json(data_dict)`

B) `requests.post(url, json=data_dict)`

C) `requests.send(url, method='POST', data=data)`

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

A) `numpy.create([1, 2, 3])`

B) `numpy.new([1, 2, 3])`

C) `numpy.array([1, 2, 3])`

D) `numpy.list([1, 2, 3])`

---

## Question 9: NumPy операции

Что выведет следующий код?

```python

import numpy as np
a = np.array([1, 2, 3])
print(a * 2)

```

A) [1, 2, 3, 1, 2, 3]

B) [2, 4, 6]

C) Error

D) 6

---

## Question 10: Pandas

Что такое DataFrame в Pandas?

A) Двумерная табличная структура данных

B) График

C) Словарь

D) Одномерный массив

---

## Question 11: Создание DataFrame

Как создать DataFrame из словаря?

A) `DataFrame.new(dict)`

B) `pd.DataFrame(dict)`

C) `pd.from_dict(dict)`

D) `pd.create(dict)`

---

## Question 12: Чтение CSV

Какая функция читает CSV файл в Pandas?

A) `pd.import_csv()`

B) `pd.read_csv()`

C) `pd.csv_read()`

D) `pd.load_csv()`

---

## Question 13: Выбор колонки

Как выбрать колонку 'name' из DataFrame df?

A) `df->name`

B) `df.name` или `df['name']`

C) `df.column('name')`

D) `df.get_column('name')`

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

A) `@route('/')`

B) `@app.url('/')`

C) `@app.route('/')`

D) `app.path('/')`

---

## Question 16: Flask запуск

Как запустить Flask-приложение в режиме отладки?

A) `app.start(debug=True)`

B) `flask run --debug`

C) `app.run(debug=True)`

D) Оба варианта A и C

---

## Question 17: pytest

Как обозначается тестовая функция в pytest?

A) Декоратор `@test`

B) Любое имя

C) Наследует от TestCase

D) Начинается с `test_`

---

## Question 18: pytest assert

Какой синтаксис проверки в pytest?

A) `self.assertEqual(a, b)`

B) `verify(a == b)`

C) `assert a == b`

D) `expect(a).toBe(b)`

---

## Question 19: pytest фикстуры

Для чего используются фикстуры в pytest?

A) Для форматирования кода

B) Для подготовки тестового окружения

C) Для параллельного выполнения

D) Для отчётов

---

## Question 20: Beautiful Soup

Для чего используется Beautiful Soup?

A) Работа с базами данных

B) Машинное обучение

C) Веб-разработка

D) Парсинг HTML/XML

---

## Question 21: Pillow

Что такое Pillow?

A) Веб-фреймворк

B) ORM

C) Библиотека для обработки изображений

D) Тестовый фреймворк

---

## Question 22: SQLAlchemy

Что такое SQLAlchemy?

A) Библиотека для тестирования

B) ORM и инструменты для работы с базами данных

C) База данных

D) Веб-фреймворк

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

B) `pip list > requirements.txt`

C) `pip freeze > requirements.txt`

D) `pip save > requirements.txt`

---

## Question 25: PyPI

Что такое PyPI?

A) Python Programming Interface

B) Python Performance Index

C) Python Project Installer

D) Python Package Index — репозиторий пакетов

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | pip (Pip Installs Packages) — стандартный менеджер пакетов Python. |
| 2 | C | `pip install package` устанавливает пакет из PyPI. |
| 3 | D | `requests.get(url)` отправляет GET-запрос. |
| 4 | B | `response.json()` автоматически парсит JSON-ответ. |
| 5 | D | `status_code` содержит HTTP-код: 200, 404, 500 и т.д. |
| 6 | B | `json=data_dict` автоматически сериализует и устанавливает Content-Type. |
| 7 | C | NumPy — библиотека для эффективных числовых вычислений и массивов. |
| 8 | C | `np.array()` создаёт ndarray из списка или другого итерируемого. |
| 9 | B | NumPy поддерживает векторизованные операции: [1,2,3] * 2 = [2,4,6]. |
| 10 | A | DataFrame — двумерная таблица с именованными колонками и индексом. |
| 11 | B | `pd.DataFrame(dict)` — основной способ создания из словаря. |
| 12 | B | `pd.read_csv('file.csv')` читает CSV в DataFrame. |
| 13 | B | `df['name']` или `df.name` (для имён без спецсимволов). |
| 14 | A | Flask — легковесный веб-фреймворк для Python. |
| 15 | C | `@app.route('/path')` связывает URL с функцией. |
| 16 | D | Оба способа работают: `app.run(debug=True)` и `flask run --debug`. |
| 17 | D | pytest автоматически находит функции, начинающиеся с `test_`. |
| 18 | C | pytest использует стандартный `assert` с улучшенными сообщениями. |
| 19 | B | Фикстуры готовят данные/ресурсы для тестов, управляют setup/teardown. |
| 20 | D | Beautiful Soup (bs4) парсит HTML/XML и позволяет навигацию по DOM. |
| 21 | C | Pillow (PIL fork) — библиотека для обработки изображений. |
| 22 | B | SQLAlchemy — ORM и SQL toolkit для Python. |
| 23 | C | venv — встроенный модуль Python 3.3+. virtualenv — сторонний, с дополнительными фичами. |
| 24 | C | `pip freeze` выводит установленные пакеты в формате requirements. |
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




