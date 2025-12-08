# Configuration Files - Quiz

Проверьте свои знания по теме "Конфигурационные файлы: INI, TOML, .env".

---

## Question 1: Секции в INI

Как обозначаются секции в INI файлах?

A) `{section}`

B) `[section]`

C) `<section>`

D) `section:`

---

## Question 2: Комментарии INI

Какой символ используется для комментариев в INI?

A) `//`

B) `/*`

C) `;` или `#`

D) `--`

---

## Question 3: TOML расшифровка

Что означает TOML?

A) Text Object Markup Language

B) Tom's Obvious Minimal Language

C) Typed Object Model Language

D) Terminal Output Markup Language

---

## Question 4: TOML типы данных

Какой тип данных поддерживает TOML, но не INI?

A) Строки

B) Boolean и числа с явными типами

C) Ключи

D) Комментарии

---

## Question 5: pyproject.toml

Для чего используется pyproject.toml?

A) Конфигурация веб-сервера

B) Метаданные и настройки Python проекта

C) Настройки Git

D) Docker конфигурация

---

## Question 6: .env безопасность

Почему .env файл не коммитят в Git?

A) Он слишком большой

B) Он содержит секреты и пароли

C) Git не поддерживает формат .env

D) Он автоматически генерируется

---

## Question 7: .env формат

Какой синтаксис правильный для .env?

A) `key: value`

B) `KEY=value`

C) `key = value`

D) `[KEY] value`

---

## Question 8: python-dotenv

Какая функция загружает .env файл в Python?

A) `import_env()`

B) `load_dotenv()`

C) `read_env()`

D) `parse_env()`

---

## Question 9: TOML массивы

Как записать массив в TOML?

A) `items: [1, 2, 3]`

B) `items = [1, 2, 3]`

C) `items = (1, 2, 3)`

D) `items = {1, 2, 3}`

---

## Question 10: TOML таблицы

Что создаёт `[server]` в TOML?

A) Комментарий

B) Таблицу (объект) server

C) Массив

D) Строку

---

## Question 11: INI Python модуль

Какой модуль Python работает с INI файлами?

A) `iniparser`

B) `configparser`

C) `ini`

D) `settings`

---

## Question 12: TOML Python 3.11

Какой модуль для чтения TOML встроен в Python 3.11+?

A) `toml`

B) `tomllib`

C) `tomlparser`

D) `pytoml`

---

## Question 13: .env.example

Для чего нужен файл .env.example?

A) Резервная копия .env

B) Шаблон со списком необходимых переменных (без значений)

C) Автоматически сгенерированный .env

D) Тестовый .env

---

## Question 14: Docker env_file

Как подключить .env в docker-compose?

A) `environment: .env`

B) `env_file: .env`

C) `load: .env`

D) `source: .env`

---

## Question 15: TOML даты

Как записать дату в TOML?

A) `date = "2024-01-15"`

B) `date = 2024-01-15`

C) `date = @2024-01-15`

D) `date = #2024-01-15`

---

## Question 16: Cargo.toml

Для какого языка используется Cargo.toml?

A) Python

B) Go

C) Rust

D) JavaScript

---

## Question 17: INI ограничения

Какое ограничение есть у INI формата?

A) Нет комментариев

B) Все значения — строки (нет типов)

C) Нельзя использовать секции

D) Максимум 100 ключей

---

## Question 18: os.getenv

Что делает `os.getenv('KEY', 'default')`?

A) Устанавливает переменную

B) Возвращает значение KEY или 'default' если не найдено

C) Удаляет переменную

D) Проверяет существование

---

## Question 19: pydantic-settings

Для чего используется pydantic-settings?

A) Форматирование конфигов

B) Типизированная загрузка и валидация конфигурации

C) Шифрование настроек

D) Конвертация форматов

---

## Question 20: Выбор формата

Какой формат лучше для хранения API ключей?

A) JSON (коммитить)

B) YAML (коммитить)

C) .env (не коммитить)

D) INI (коммитить)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Секции в INI обозначаются `[section_name]`. |
| 2 | C | В INI комментарии начинаются с `;` или `#`. |
| 3 | B | Tom's Obvious Minimal Language — по имени создателя Tom Preston-Werner. |
| 4 | B | TOML поддерживает integer, float, boolean, datetime как отдельные типы. |
| 5 | B | pyproject.toml — стандартный файл конфигурации Python проектов (PEP 518, 621). |
| 6 | B | .env содержит секреты (пароли, ключи), которые не должны быть в репозитории. |
| 7 | B | Стандартный формат .env: `KEY=value` (без пробелов вокруг `=`). |
| 8 | B | `load_dotenv()` из библиотеки python-dotenv загружает .env в os.environ. |
| 9 | B | В TOML массивы: `key = [1, 2, 3]`. |
| 10 | B | `[server]` создаёт таблицу (эквивалент объекта/словаря). |
| 11 | B | `configparser` — стандартный модуль Python для работы с INI. |
| 12 | B | `tomllib` встроен в Python 3.11+ (только чтение). |
| 13 | B | .env.example — шаблон со списком переменных без реальных значений, коммитится в Git. |
| 14 | B | `env_file: .env` или `env_file: [.env]` в docker-compose.yml. |
| 15 | B | TOML поддерживает даты без кавычек: `date = 2024-01-15`. |
| 16 | C | Cargo.toml — файл конфигурации пакетов Rust. |
| 17 | B | В INI все значения — строки, нужно вручную преобразовывать типы. |
| 18 | B | `os.getenv(key, default)` возвращает значение переменной или default. |
| 19 | B | pydantic-settings загружает и валидирует конфигурацию с типизацией. |
| 20 | C | Секреты хранятся в .env и исключаются из Git через .gitignore. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете конфигурационные форматы! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите TOML и .env практики. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о безопасности конфигов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию целиком. |

---


