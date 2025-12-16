# YAML - Quiz

Проверьте свои знания по теме "YAML: формат данных для конфигураций".

---

## Question 1: Расшифровка YAML

Что означает аббревиатура YAML?

A) Yet Another Markup Language

B) YAML Advanced Modeling Language

C) Your Application Markup Language

D) YAML Ain't Markup Language

---

## Question 2: Комментарии

Как написать комментарий в YAML?

A) # comment

B) `/* comment */`

C) `-- comment`

D) `// comment`

---

## Question 3: Отступы

Какие символы можно использовать для отступов в YAML?

A) Только табы

B) Табы и пробелы

C) Любые пробельные символы

D) Только пробелы

---

## Question 4: Boolean значения

Какое значение НЕ интерпретируется как boolean в YAML 1.1?

A) `maybe`

B) `no`

C) `on`

D) `yes`

---

## Question 5: Norway Problem

Что произойдёт с `country: NO` в YAML 1.1?

A) Null

B) Ошибка синтаксиса

C) Строка "NO"

D) Boolean false

---

## Question 6: Многострочные строки

Какой синтаксис сохраняет переносы строк в многострочном тексте?

A) `'''`

B) `>`

C) | 

D) `"""`

---

## Question 7: Flow style

Как записать список `[1, 2, 3]` в YAML flow style?

A) `items: (1, 2, 3)`

B) `items: {1, 2, 3}`

C) items: [1, 2, 3]

D) `items: <1, 2, 3>`

---

## Question 8: Якоря и алиасы

Для чего используется синтаксис `&name` и `*name` в YAML?

A) Для регулярных выражений

B) Для комментариев

C) Для переменных окружения

D) Для якорей (определение) и алиасов (использование)

---

## Question 9: Множественные документы

Какой разделитель используется между документами в YAML?

A) `---`

B) `===`

C) `***`

D) `~~~`

---

## Question 10: YAML vs JSON

Какое утверждение верно?

A) YAML — надмножество JSON (с версии 1.2)

B) Они несовместимы

C) YAML — бинарный формат

D) JSON — надмножество YAML

---

## Question 11: Python safe_load

Почему нужно использовать `yaml.safe_load()` вместо `yaml.load()`?

A) yaml.load может выполнить произвольный код

B) `safe_load` быстрее

C) `safe_load` лучше форматирует вывод

D) `safe_load` поддерживает больше типов

---

## Question 12: Типы данных

Как YAML интерпретирует значение `1.0` без кавычек?

A) Целое число 1

B) Число с плавающей точкой 1.0

C) Boolean true

D) Строка "1.0"

---

## Question 13: Null значения

Какой из вариантов НЕ является null в YAML?

A) `value: ~`

B) `value:`

C) `value: null`

D) value: ""

---

## Question 14: Строки с двоеточием

Как правильно записать строку "Error: file not found"?

A) message: "Error: file not found"

B) `message: Error file not found`

C) `message: Error: file not found`

D) `message: Error\: file not found`

---

## Question 15: yq команда

Какая команда извлекает значение поля `port` из `server.port` в yq?

A) `yq get server.port file.yaml`

B) `yq select .server.port file.yaml`

C) yq eval '.server.port' file.yaml

D) `yq eval 'server.port' file.yaml`

---

## Question 16: Kubernetes

В каком инструменте чаще всего используется YAML?

A) Kubernetes

B) PostgreSQL

C) MySQL

D) Apache HTTP Server

---

## Question 17: Версия YAML

Какая версия YAML решает "Norway Problem"?

A) YAML 1.2

B) YAML 2.0

C) YAML 1.1

D) YAML 1.0

---

## Question 18: Валидация

Какой инструмент используется для проверки стиля YAML файлов?

A) jsonlint

B) yamlcheck

C) yamlvalidate

D) yamllint

---

## Question 19: Block vs Flow

Какой стиль рекомендуется для конфигурационных файлов?

A) JSON-совместимый

B) Смешанный

C) Block style (отступы)

D) Flow style (`{}`, `[]`)

---

## Question 20: Docker Compose

Как называется файл Docker Compose по умолчанию?

A) `compose.yaml` или `docker-compose.yml`

B) `docker.yaml`

C) `Dockerfile`

D) `container.yml`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | YAML Ain't Markup Language — рекурсивный акроним. |
| 2 | A | Комментарии в YAML начинаются с `#`. |
| 3 | D | В YAML можно использовать ТОЛЬКО пробелы для отступов, табы запрещены. |
| 4 | A | `maybe` — строка. `yes`, `no`, `on`, `off` — boolean в YAML 1.1. |
| 5 | D | `NO` интерпретируется как false в YAML 1.1 (Norway Problem). |
| 6 | C | `|` (literal block) сохраняет переносы, `>` (folded) преобразует их в пробелы. |
| 7 | C | Flow style использует `[]` для списков и `{}` для объектов, как в JSON. |
| 8 | D | `&name` создаёт якорь, `*name` ссылается на него (алиас). |
| 9 | A | `---` (три дефиса) — разделитель документов в YAML. |
| 10 | A | Валидный JSON — валидный YAML (начиная с YAML 1.2). |
| 11 | A | `yaml.load()` может выполнить произвольный Python код через теги. |
| 12 | B | `1.0` без кавычек — число с плавающей точкой. Для строки: `"1.0"`. |
| 13 | D | Пустая строка `""` — это строка, не null. Остальные — null. |
| 14 | A | Кавычки нужны для строк с `: ` (двоеточие + пробел). |
| 15 | C | `.server.port` — синтаксис yq (точка в начале обязательна). |
| 16 | A | Kubernetes широко использует YAML для манифестов. |
| 17 | A | YAML 1.2 не интерпретирует `yes/no/on/off` как boolean. |
| 18 | D | yamllint — линтер для проверки YAML файлов. |
| 19 | C | Block style (с отступами) читабельнее для конфигураций. |
| 20 | A | `docker-compose.yml` или `compose.yaml` (новое имя). |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете YAML! Переходите к Markup. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите gotchas и типы данных. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте раздел о подводных камнях. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и практиковаться. |

---


