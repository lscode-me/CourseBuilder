# Python Third-Party Modules (pip) - Quiz

Проверьте свои знания по теме "Популярные сторонние модули из PyPI".

---

## Question 1: pip

Что такое pip?

A) Интерпретатор Python

B) Менеджер пакетов Python

C) Библиотека для работы с изображениями

D) Фреймворк для веб-разработки

---

## Question 2: Установка пакета

Как установить последнюю версию пакета requests?

A) `python install requests`

B) `pip install requests`

C) `pip get requests`

D) `import requests --install`

---

## Question 3: requests

Какой метод отправляет GET-запрос в библиотеке requests?

A) `requests.fetch()`

B) `requests.get()`

C) `requests.download()`

D) `requests.read()`

---

## Question 4: requests response

Как получить JSON из ответа requests?

A) `response.text`

B) `response.json()`

C) `response.content`

D) `json.loads(response)`

---

## Question 5: HTTP Status Code

Какое свойство содержит код статуса HTTP?

A) `response.code`

B) `response.status_code`

C) `response.http_code`

D) `response.status`

---

## Question 6: requests POST

Как отправить POST-запрос с JSON-данными?

A) `requests.post(url, data=json_data)`

B) `requests.post(url, json=data_dict)`

C) `requests.send(url, method='POST', data=data)`

D) `requests.post(url).json(data_dict)`

---

## Question 7: NumPy

Для чего используется NumPy?

A) Веб-разработка

B) Числовые вычисления и работа с массивами

C) Машинное обучение

D) Парсинг HTML

---

## Question 8: NumPy массив

Как создать NumPy массив?

A) `numpy.array([1, 2, 3])`

B) `numpy.list([1, 2, 3])`

C) `numpy.create([1, 2, 3])`

D) `numpy.new([1, 2, 3])`

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

C) 6

D) Error

---

## Question 10: Pandas

Что такое DataFrame в Pandas?

A) Одномерный массив

B) Двумерная табличная структура данных

C) Словарь

D) График

---

## Question 11: Создание DataFrame

Как создать DataFrame из словаря?

A) `pd.DataFrame(dict)`

B) `pd.from_dict(dict)`

C) `pd.create(dict)`

D) `DataFrame.new(dict)`

---

## Question 12: Чтение CSV

Какая функция читает CSV файл в Pandas?

A) `pd.load_csv()`

B) `pd.read_csv()`

C) `pd.import_csv()`

D) `pd.csv_read()`

---

## Question 13: Выбор колонки

Как выбрать колонку 'name' из DataFrame df?

A) `df.name` или `df['name']`

B) `df.column('name')`

C) `df.get_column('name')`

D) `df->name`

---

## Question 14: Flask

Что такое Flask?

A) База данных

B) Микро веб-фреймворк

C) ORM библиотека

D) Тестовый фреймворк

---

## Question 15: Flask маршрут

Как определить маршрут в Flask?

A) `@app.route('/')`

B) `@route('/')`

C) `app.path('/')`

D) `@app.url('/')`

---

## Question 16: Flask запуск

Как запустить Flask-приложение в режиме отладки?

A) `app.run(debug=True)`

B) `app.start(debug=True)`

C) `flask run --debug`

D) Оба варианта A и C

---

## Question 17: pytest

Как обозначается тестовая функция в pytest?

A) Начинается с `test_`

B) Декоратор `@test`

C) Наследует от TestCase

D) Любое имя

---

## Question 18: pytest assert

Какой синтаксис проверки в pytest?

A) `self.assertEqual(a, b)`

B) `assert a == b`

C) `expect(a).toBe(b)`

D) `verify(a == b)`

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

A) Веб-разработка

B) Парсинг HTML/XML

C) Работа с базами данных

D) Машинное обучение

---

## Question 21: Pillow

Что такое Pillow?

A) Веб-фреймворк

B) Библиотека для обработки изображений

C) ORM

D) Тестовый фреймворк

---

## Question 22: SQLAlchemy

Что такое SQLAlchemy?

A) База данных

B) ORM и инструменты для работы с базами данных

C) Веб-фреймворк

D) Библиотека для тестирования

---

## Question 23: virtualenv vs venv

В чём разница между virtualenv и venv?

A) venv встроен в Python 3, virtualenv — сторонний пакет

B) virtualenv быстрее

C) venv не работает на Windows

D) Нет разницы

---

## Question 24: requirements.txt

Как создать requirements.txt с текущими пакетами?

A) `pip save > requirements.txt`

B) `pip freeze > requirements.txt`

C) `pip list > requirements.txt`

D) `pip export requirements.txt`

---

## Question 25: PyPI

Что такое PyPI?

A) Python Package Index — репозиторий пакетов

B) Python Programming Interface

C) Python Performance Index

D) Python Project Installer

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | pip (Pip Installs Packages) — стандартный менеджер пакетов Python. |
| 2 | B | `pip install package` устанавливает пакет из PyPI. |
| 3 | B | `requests.get(url)` отправляет GET-запрос. |
| 4 | B | `response.json()` автоматически парсит JSON-ответ. |
| 5 | B | `status_code` содержит HTTP-код: 200, 404, 500 и т.д. |
| 6 | B | `json=data_dict` автоматически сериализует и устанавливает Content-Type. |
| 7 | B | NumPy — библиотека для эффективных числовых вычислений и массивов. |
| 8 | A | `np.array()` создаёт ndarray из списка или другого итерируемого. |
| 9 | B | NumPy поддерживает векторизованные операции: [1,2,3] * 2 = [2,4,6]. |
| 10 | B | DataFrame — двумерная таблица с именованными колонками и индексом. |
| 11 | A | `pd.DataFrame(dict)` — основной способ создания из словаря. |
| 12 | B | `pd.read_csv('file.csv')` читает CSV в DataFrame. |
| 13 | A | `df['name']` или `df.name` (для имён без спецсимволов). |
| 14 | B | Flask — легковесный веб-фреймворк для Python. |
| 15 | A | `@app.route('/path')` связывает URL с функцией. |
| 16 | D | Оба способа работают: `app.run(debug=True)` и `flask run --debug`. |
| 17 | A | pytest автоматически находит функции, начинающиеся с `test_`. |
| 18 | B | pytest использует стандартный `assert` с улучшенными сообщениями. |
| 19 | B | Фикстуры готовят данные/ресурсы для тестов, управляют setup/teardown. |
| 20 | B | Beautiful Soup (bs4) парсит HTML/XML и позволяет навигацию по DOM. |
| 21 | B | Pillow (PIL fork) — библиотека для обработки изображений. |
| 22 | B | SQLAlchemy — ORM и SQL toolkit для Python. |
| 23 | A | venv — встроенный модуль Python 3.3+. virtualenv — сторонний, с дополнительными фичами. |
| 24 | B | `pip freeze` выводит установленные пакеты в формате requirements. |
| 25 | A | PyPI (Python Package Index) — официальный репозиторий Python-пакетов. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание экосистемы Python! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Попрактикуйтесь с requests и pandas. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Установите и попробуйте использовать основные библиотеки. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Начните с практического использования pip и requests. |

---

