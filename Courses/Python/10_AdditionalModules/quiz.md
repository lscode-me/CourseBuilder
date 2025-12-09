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

A) `import requests --install`

B) `pip install requests`

C) `pip get requests`

D) `python install requests`

---

## Question 3: requests





Какой метод отправляет GET-запрос в библиотеке requests?

A) `requests.read()`

B) `requests.get()`

C) `requests.download()`

D) `requests.fetch()`

---

## Question 4: requests response





Как получить JSON из ответа requests?

A) `response.content`

B) `response.text`

C) `response.json()`

D) `json.loads(response)`

---

## Question 5: HTTP Status Code





Какое свойство содержит код статуса HTTP?

A) `response.code`

B) `response.status`

C) `response.http_code`

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

B) Числовые вычисления и работа с массивами

C) Парсинг HTML

D) Машинное обучение

---

## Question 8: NumPy массив





Как создать NumPy массив?

A) `numpy.new([1, 2, 3])`

B) `numpy.create([1, 2, 3])`

C) `numpy.list([1, 2, 3])`

D) `numpy.array([1, 2, 3])`

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

A) Двумерная табличная структура данных

B) График

C) Словарь

D) Одномерный массив

---

## Question 11: Создание DataFrame





Как создать DataFrame из словаря?

A) `pd.DataFrame(dict)`

B) `pd.from_dict(dict)`

C) `DataFrame.new(dict)`

D) `pd.create(dict)`

---

## Question 12: Чтение CSV





Какая функция читает CSV файл в Pandas?

A) `pd.read_csv()`

B) `pd.import_csv()`

C) `pd.load_csv()`

D) `pd.csv_read()`

---

## Question 13: Выбор колонки





Как выбрать колонку 'name' из DataFrame df?

A) `df.get_column('name')`

B) `df.column('name')`

C) `df.name` или `df['name']`

D) `df->name`

---

## Question 14: Flask





Что такое Flask?

A) Тестовый фреймворк

B) Микро веб-фреймворк

C) База данных

D) ORM библиотека

---

## Question 15: Flask маршрут





Как определить маршрут в Flask?

A) `@app.url('/')`

B) `@app.route('/')`

C) `@route('/')`

D) `app.path('/')`

---

## Question 16: Flask запуск





Как запустить Flask-приложение в режиме отладки?

A) Оба варианта A и C

B) `app.run(debug=True)`

C) `flask run --debug`

D) `app.start(debug=True)`

---

## Question 17: pytest





Как обозначается тестовая функция в pytest?

A) Любое имя

B) Декоратор `@test`

C) Начинается с `test_`

D) Наследует от TestCase

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

A) Парсинг HTML/XML

B) Работа с базами данных

C) Веб-разработка

D) Машинное обучение

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

A) ORM и инструменты для работы с базами данных

B) Библиотека для тестирования

C) Веб-фреймворк

D) База данных

---

## Question 23: virtualenv vs venv





В чём разница между virtualenv и venv?

A) venv встроен в Python 3, virtualenv — сторонний пакет

B) venv не работает на Windows

C) virtualenv быстрее

D) Нет разницы

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

A) Python Performance Index

B) Python Programming Interface

C) Python Package Index — репозиторий пакетов

D) Python Project Installer

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | pip (Pip Installs Packages) — стандартный менеджер пакетов Python. |
| 2 | B | `pip install package` устанавливает пакет из PyPI. |
| 3 | B | `requests.get(url)` отправляет GET-запрос. |
| 4 | C | `response.json()` автоматически парсит JSON-ответ. |
| 5 | D | `status_code` содержит HTTP-код: 200, 404, 500 и т.д. |
| 6 | B | `json=data_dict` автоматически сериализует и устанавливает Content-Type. |
| 7 | B | NumPy — библиотека для эффективных числовых вычислений и массивов. |
| 8 | D | `np.array()` создаёт ndarray из списка или другого итерируемого. |
| 9 | C | NumPy поддерживает векторизованные операции: [1,2,3] * 2 = [2,4,6]. |
| 10 | A | DataFrame — двумерная таблица с именованными колонками и индексом. |
| 11 | A | `pd.DataFrame(dict)` — основной способ создания из словаря. |
| 12 | A | `pd.read_csv('file.csv')` читает CSV в DataFrame. |
| 13 | C | `df['name']` или `df.name` (для имён без спецсимволов). |
| 14 | B | Flask — легковесный веб-фреймворк для Python. |
| 15 | B | `@app.route('/path')` связывает URL с функцией. |
| 16 | A | Оба способа работают: `app.run(debug=True)` и `flask run --debug`. |
| 17 | C | pytest автоматически находит функции, начинающиеся с `test_`. |
| 18 | C | pytest использует стандартный `assert` с улучшенными сообщениями. |
| 19 | B | Фикстуры готовят данные/ресурсы для тестов, управляют setup/teardown. |
| 20 | A | Beautiful Soup (bs4) парсит HTML/XML и позволяет навигацию по DOM. |
| 21 | A | Pillow (PIL fork) — библиотека для обработки изображений. |
| 22 | A | SQLAlchemy — ORM и SQL toolkit для Python. |
| 23 | A | venv — встроенный модуль Python 3.3+. virtualenv — сторонний, с дополнительными фичами. |
| 24 | C | `pip freeze` выводит установленные пакеты в формате requirements. |
| 25 | C | PyPI (Python Package Index) — официальный репозиторий Python-пакетов. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное знание экосистемы Python! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Попрактикуйтесь с requests и pandas. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Установите и попробуйте использовать основные библиотеки. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Начните с практического использования pip и requests. |

---

