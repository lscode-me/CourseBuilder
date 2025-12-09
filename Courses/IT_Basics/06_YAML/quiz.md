# YAML - Quiz

Проверьте свои знания по теме "YAML: формат данных для конфигураций".

---

## Question 1: Расшифровка YAML

Что означает аббревиатура YAML?

A) YAML Ain't Markup Language

B) Yet Another Markup Language

C) Your Application Markup Language

D) YAML Advanced Modeling Language

---

## Question 2: Комментарии

Как написать комментарий в YAML?

A) `// comment`

B) # comment

C) `/* comment */`

D) `-- comment`

---

## Question 3: Отступы

Какие символы можно использовать для отступов в YAML?

A) Только табы

B) Табы и пробелы

C) Только пробелы

D) Любые пробельные символы

---

## Question 4: Boolean значения

Какое значение НЕ интерпретируется как boolean в YAML 1.1?

A) `yes`

B) `no`

C) `on`

D) `maybe`

---

## Question 5: Norway Problem

Что произойдёт с `country: NO` в YAML 1.1?

A) Строка "NO"

B) Boolean false

C) Null

D) Ошибка синтаксиса

---

## Question 6: Многострочные строки

Какой синтаксис сохраняет переносы строк в многострочном тексте?

A) `>`

B) | 

C) `"""`

D) `'''`

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

A) Для комментариев

B) Для переменных окружения

C) Для регулярных выражений

D) Для якорей (определение) и алиасов (использование)

---

## Question 9: Множественные документы

Какой разделитель используется между документами в YAML?

A) ---

B) `===`

C) `***`

D) `~~~`

---

## Question 10: YAML vs JSON

Какое утверждение верно?

A) JSON — надмножество YAML

B) YAML — надмножество JSON (с версии 1.2)

C) Они несовместимы

D) YAML — бинарный формат

---

## Question 11: Python safe_load

Почему нужно использовать `yaml.safe_load()` вместо `yaml.load()`?

A) `safe_load` быстрее

B) `safe_load` поддерживает больше типов

C) yaml.load может выполнить произвольный код

D) `safe_load` лучше форматирует вывод

---

## Question 12: Типы данных

Как YAML интерпретирует значение `1.0` без кавычек?

A) Строка "1.0"

B) Целое число 1

C) Boolean true

D) Число с плавающей точкой 1.0

---

## Question 13: Null значения

Какой из вариантов НЕ является null в YAML?

A) value: ""

B) `value:`

C) `value: ~`

D) `value: null`

---

## Question 14: Строки с двоеточием

Как правильно записать строку "Error: file not found"?

A) `message: Error: file not found`

B) message: "Error: file not found"

C) `message: Error file not found`

D) `message: Error\: file not found`

---

## Question 15: yq команда

Какая команда извлекает значение поля `port` из `server.port` в yq?

A) `yq eval 'server.port' file.yaml`

B) `yq get server.port file.yaml`

C) yq eval '.server.port' file.yaml

D) `yq select .server.port file.yaml`

---

## Question 16: Kubernetes

В каком инструменте чаще всего используется YAML?

A) MySQL

B) Apache HTTP Server

C) PostgreSQL

D) Kubernetes

---

## Question 17: Версия YAML

Какая версия YAML решает "Norway Problem"?

A) YAML 1.2

B) YAML 1.0

C) YAML 1.1

D) YAML 2.0

---

## Question 18: Валидация

Какой инструмент используется для проверки стиля YAML файлов?

A) jsonlint

B) yamllint

C) yamlcheck

D) yamlvalidate

---

## Question 19: Block vs Flow

Какой стиль рекомендуется для конфигурационных файлов?

A) Flow style (`{}`, `[]`)

B) Смешанный

C) Block style (отступы)

D) JSON-совместимый

---

## Question 20: Docker Compose

Как называется файл Docker Compose по умолчанию?

A) `Dockerfile`

B) `docker.yaml`

C) `container.yml`

D) `compose.yaml` или `docker-compose.yml`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | YAML Ain't Markup Language — рекурсивный акроним. |
| 2 | B | Комментарии в YAML начинаются с `#`. |
| 3 | C | В YAML можно использовать ТОЛЬКО пробелы для отступов, табы запрещены. |
| 4 | D | `maybe` — строка. `yes`, `no`, `on`, `off` — boolean в YAML 1.1. |
| 5 | B | `NO` интерпретируется как false в YAML 1.1 (Norway Problem). |
| 6 | B | `|` (literal block) сохраняет переносы, `>` (folded) преобразует их в пробелы. |
| 7 | C | Flow style использует `[]` для списков и `{}` для объектов, как в JSON. |
| 8 | D | `&name` создаёт якорь, `*name` ссылается на него (алиас). |
| 9 | A | `---` разделяет документы, `...` (опционально) завершает документ. |
| 10 | B | Валидный JSON — валидный YAML (начиная с YAML 1.2). |
| 11 | C | `yaml.load()` может выполнить произвольный Python код через теги. |
| 12 | D | `1.0` без кавычек — число с плавающей точкой. Для строки: `"1.0"`. |
| 13 | A | Пустая строка `""` — это строка, не null. Остальные — null. |
| 14 | B | Кавычки нужны для строк с `: ` (двоеточие + пробел). |
| 15 | C | `.server.port` — синтаксис yq (точка в начале обязательна). |
| 16 | D | Kubernetes широко использует YAML для манифестов. |
| 17 | A | YAML 1.2 не интерпретирует `yes/no/on/off` как boolean. |
| 18 | B | yamllint — линтер для проверки YAML файлов. |
| 19 | C | Block style (с отступами) читабельнее для конфигураций. |
| 20 | D | `docker-compose.yml` или `compose.yaml` (новое имя). |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете YAML! Переходите к Markup. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите gotchas и типы данных. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте раздел о подводных камнях. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию и практиковаться. |

---

