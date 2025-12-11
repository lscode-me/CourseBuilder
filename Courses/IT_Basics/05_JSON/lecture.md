# JSON
## Синтаксис, валидация и инструменты обработки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать текстовые форматы (модуль 04_FileFormats)
- Знать основы кодировок (UTF-8)
- Иметь базовое представление о структурах данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Читать и писать корректный JSON
- Валидировать JSON и находить ошибки синтаксиса
- Использовать jq для обработки JSON в командной строке
- Работать с JSON в Python и других языках
- Понимать ограничения JSON и способы их обхода

---

## 1. Что такое JSON

### 1.1 Определение

**JSON** (JavaScript Object Notation) — текстовый формат обмена данными.

- Придуман Дугласом Крокфордом в начале 2000-х
- Стандартизирован: ECMA-404, RFC 8259
- Независим от языка программирования
- Человекочитаемый

### 1.2 Где используется JSON

| Область | Применение |
|---------|------------|
| Web API | REST API запросы и ответы |
| Конфигурации | package.json, tsconfig.json |
| Базы данных | MongoDB, PostgreSQL JSONB |
| Логирование | Structured logging |
| Обмен данными | Между сервисами, клиентом и сервером |

### 1.3 Пример JSON

```json

{
  "name": "Alice",
  "age": 30,
  "isActive": true,
  "balance": null,
  "skills": ["Python", "SQL", "Docker"],
  "address": {
    "city": "Moscow",
    "zip": "101000"
  }
}

```

---

## 2. Синтаксис JSON

### 2.1 Типы данных

JSON поддерживает **6 типов данных**:

| Тип | Пример | Описание |
|-----|--------|----------|
| String | `"hello"` | Строка в двойных кавычках |
| Number | `42`, `3.14`, `-5`, `1e10` | Число (целое или дробное) |
| Boolean | `true`, `false` | Логическое значение |
| Null | `null` | Отсутствие значения |
| Array | `[1, 2, 3]` | Упорядоченный список |
| Object | `{"key": "value"}` | Набор пар ключ-значение |

### 2.2 Строки (Strings)

```json

{
  "simple": "Hello, World!",
  "unicode": "Привет, мир! 你好 🎉",
  "escaped": "Line 1\nLine 2\tTabbed",
  "quotes": "He said \"Hello\"",
  "path": "C:\\Users\\name",
  "special": "\u0041"
}

```

**Escape-последовательности:**

| Последовательность | Значение |
|-------------------|----------|
| `\"` | Двойная кавычка |
| `\\` | Обратный слеш |
| `\/` | Прямой слеш (опционально) |
| `\n` | Новая строка |
| `\r` | Возврат каретки |
| `\t` | Табуляция |
| `\b` | Backspace |
| `\f` | Form feed |
| `\uXXXX` | Unicode символ |

### 2.3 Числа (Numbers)

```json

{
  "integer": 42,
  "negative": -17,
  "float": 3.14159,
  "exponent": 1.5e10,
  "negativeExp": 2.5e-3
}

```

**Не поддерживаются:**

- Ведущие нули: `007` ❌
- Hex: `0xFF` ❌
- Infinity, NaN ❌
- Октальные: `0o755` ❌

### 2.4 Массивы (Arrays)

```json

{
  "numbers": [1, 2, 3, 4, 5],
  "strings": ["apple", "banana", "cherry"],
  "mixed": [1, "two", true, null],
  "nested": [[1, 2], [3, 4]],
  "empty": []
}

```

### 2.5 Объекты (Objects)

```json

{
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  },
  "settings": {
    "theme": "dark",
    "notifications": {
      "email": true,
      "push": false
    }
  }
}

```

**Правила:**

- Ключи ВСЕГДА в двойных кавычках
- Порядок ключей не гарантирован
- Дубликаты ключей — undefined behavior

### 2.6 Полный пример

```json

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30,
  "isVerified": true,
  "balance": 1250.50,
  "tags": ["developer", "blogger"],
  "profile": {
    "bio": "Software engineer",
    "avatar": null,
    "social": {
      "twitter": "@johndoe",
      "github": "johndoe"
    }
  },
  "history": [
    {"action": "login", "timestamp": "2024-01-15T10:30:00Z"},
    {"action": "purchase", "timestamp": "2024-01-15T11:45:00Z"}
  ]
}

```

---

## 3. Распространённые ошибки

### 3.1 Trailing comma (хвостовая запятая)

❌ **Ошибка:**

```json

{
  "name": "Alice",
  "age": 30,
}

```

✅ **Правильно:**

```json

{
  "name": "Alice",
  "age": 30
}

```

### 3.2 Одинарные кавычки

❌ **Ошибка:**

```json

{
  'name': 'Alice'
}

```

✅ **Правильно:**

```json

{
  "name": "Alice"
}

```

### 3.3 Комментарии

❌ **Ошибка:**

```json

{
  "name": "Alice",  // user name
  /* multi-line comment */
  "age": 30
}

```

✅ **JSON не поддерживает комментарии!**

> **💡 Pro Tip:**  
> Для конфигураций с комментариями используйте YAML, JSONC (VS Code), или JSON5.

### 3.4 Unquoted keys

❌ **Ошибка:**

```json

{
  name: "Alice"
}

```

✅ **Правильно:**

```json

{
  "name": "Alice"
}

```

### 3.5 Специальные числа

❌ **Ошибка:**

```json

{
  "value": NaN,
  "max": Infinity
}

```

✅ **Альтернативы:**

```json

{
  "value": null,
  "max": 1e308
}

```

---

## 4. Валидация JSON

### 4.1 Командная строка

```bash
# jq — валидация и форматирование
echo '{"name":"Alice"}' | jq .
# {
#   "name": "Alice"
# }

# Проверка файла
jq . config.json

# Если JSON невалидный — ошибка
echo '{"name":}' | jq .
# parse error: Invalid numeric literal at line 1, column 9

# python -m json.tool
echo '{"name":"Alice"}' | python3 -m json.tool

# Проверка синтаксиса
python3 -m json.tool config.json > /dev/null && echo "Valid JSON"

```

### 4.2 Онлайн инструменты

- [JSONLint](https://jsonlint.com/) — валидация
- [JSON Formatter](https://jsonformatter.org/) — форматирование
- [jq play](https://jqplay.org/) — тестирование jq

### 4.3 Python валидация

```python

import json

def validate_json(json_string):
    """Проверяет валидность JSON строки."""
    try:
        json.loads(json_string)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)

# Примеры
valid, error = validate_json('{"name": "Alice"}')
print(f"Valid: {valid}")  # Valid: True

valid, error = validate_json('{"name": }')
print(f"Valid: {valid}, Error: {error}")
# Valid: False, Error: Expecting value: line 1 column 10 (char 9)
```

---

## 5. jq — мощный инструмент для JSON

### 5.1 Основы jq

```bash
# Форматирование (pretty print)
cat data.json | jq .

# Компактный вывод
jq -c . data.json

# Извлечение поля
echo '{"name":"Alice","age":30}' | jq '.name'
# "Alice"

# Без кавычек
echo '{"name":"Alice"}' | jq -r '.name'
# Alice
```

### 5.2 Навигация по структуре

```bash
# Вложенные поля
echo '{"user":{"name":"Alice"}}' | jq '.user.name'
# "Alice"

# Элемент массива
echo '{"items":["a","b","c"]}' | jq '.items[0]'
# "a"

# Все элементы массива
echo '{"items":["a","b","c"]}' | jq '.items[]'
# "a"
# "b"
# "c"

# Последний элемент
echo '[1,2,3,4,5]' | jq '.[-1]'
# 5

# Срез
echo '[1,2,3,4,5]' | jq '.[1:3]'
# [2, 3]
```

### 5.3 Фильтрация и трансформация

```bash
# Данные для примеров
cat > users.json << 'EOF'
[
  {"name": "Alice", "age": 30, "active": true},
  {"name": "Bob", "age": 25, "active": false},
  {"name": "Charlie", "age": 35, "active": true}
]
EOF

# Фильтрация по условию
jq '.[] | select(.active == true)' users.json
# {"name": "Alice", "age": 30, "active": true}
# {"name": "Charlie", "age": 35, "active": true}

# Извлечение полей
jq '.[].name' users.json
# "Alice"
# "Bob"
# "Charlie"

# Создание нового объекта
jq '.[] | {username: .name, years: .age}' users.json

# Преобразование в массив
jq '[.[] | .name]' users.json
# ["Alice", "Bob", "Charlie"]
```

### 5.4 Модификация данных

```bash
# Добавление поля
echo '{"name":"Alice"}' | jq '. + {age: 30}'
# {"name": "Alice", "age": 30}

# Обновление поля
echo '{"name":"Alice","age":30}' | jq '.age = 31'
# {"name": "Alice", "age": 31}

# Удаление поля
echo '{"name":"Alice","age":30}' | jq 'del(.age)'
# {"name": "Alice"}

# Обновление вложенного
echo '{"user":{"name":"Alice"}}' | jq '.user.name = "Bob"'
# {"user": {"name": "Bob"}}
```

### 5.5 Агрегация

```bash
# Количество элементов
jq 'length' users.json
# 3

# Сумма
echo '[1,2,3,4,5]' | jq 'add'
# 15

# Средний возраст
jq '[.[].age] | add / length' users.json
# 30

# Сортировка
jq 'sort_by(.age)' users.json

# Группировка
jq 'group_by(.active)' users.json

# Уникальные значения
echo '["a","b","a","c","b"]' | jq 'unique'
# ["a", "b", "c"]
```

### 5.6 Практические примеры

```bash
# Извлечь все email из API ответа
curl -s https://api.example.com/users | jq '.[].email'

# Конвертировать JSON в CSV
jq -r '.[] | [.name, .age] | @csv' users.json
# "Alice",30
# "Bob",25
# "Charlie",35

# Найти пользователей старше 28
jq '[.[] | select(.age > 28)]' users.json

# Подсчёт по условию
jq '[.[] | select(.active)] | length' users.json
# 2

# Форматирование для вставки в скрипт
jq -r '.[] | "User: \(.name), Age: \(.age)"' users.json
# User: Alice, Age: 30
# User: Bob, Age: 25
# User: Charlie, Age: 35
```

---

## 6. JSON в Python

### 6.1 Базовые операции

```python

import json

# Python dict → JSON string
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"]
}

json_string = json.dumps(data)
print(json_string)
# {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

# С форматированием
pretty_json = json.dumps(data, indent=2)
print(pretty_json)
# {
#   "name": "Alice",
#   "age": 30,
#   "skills": ["Python", "SQL"]
# }

# JSON string → Python dict
parsed = json.loads(json_string)
print(parsed["name"])  # Alice

```

### 6.2 Работа с файлами

```python

import json

# Запись в файл
data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Чтение из файла
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)

```

### 6.3 Обработка ошибок

```python

import json

def safe_parse_json(json_string):
    """Безопасно парсит JSON."""
    try:
        return json.loads(json_string), None
    except json.JSONDecodeError as e:
        return None, {
            "error": str(e),
            "line": e.lineno,
            "column": e.colno,
            "position": e.pos
        }

# Пример
data, error = safe_parse_json('{"name": invalid}')
if error:
    print(f"Error at line {error['line']}, column {error['column']}: {error['error']}")

```

### 6.4 Кастомная сериализация

```python

import json
from datetime import datetime, date
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    """Кастомный энкодер для типов, которые JSON не поддерживает."""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

# Использование
data = {
    "timestamp": datetime.now(),
    "price": Decimal("19.99"),
    "tags": {"python", "json"}
}

json_string = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_string)

```

### 6.5 Работа с большими файлами

```python

import json

# Для очень больших файлов — построчное чтение JSON Lines
def read_jsonl(filepath):
    """Читает JSON Lines файл (один JSON объект на строку)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# Записать JSON Lines
def write_jsonl(filepath, items):
    """Записывает iterable как JSON Lines."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item) + '\n')

# Использование
users = [{"name": "Alice"}, {"name": "Bob"}]
write_jsonl("users.jsonl", users)

for user in read_jsonl("users.jsonl"):
    print(user)

```

---

## 7. JSON Schema

### 7.1 Что такое JSON Schema

**JSON Schema** — способ описания структуры JSON документа для валидации.

```json

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "maximum": 150
    },
    "email": {
      "type": "string",
      "format": "email"
    }
  },
  "required": ["name", "email"]
}

```

### 7.2 Валидация по схеме в Python

```python

from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name"]
}

# Валидные данные
valid_data = {"name": "Alice", "age": 30}
validate(valid_data, schema)  # OK

# Невалидные данные
invalid_data = {"age": -5}
try:
    validate(invalid_data, schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
    # Validation error: 'name' is a required property
```

---

## 8. Альтернативы JSON

### 8.1 Когда JSON не подходит

| Ограничение | Альтернатива |
|-------------|--------------|
| Нет комментариев | YAML, TOML, JSON5 |
| Verbose для конфигов | YAML, TOML |
| Нет бинарных данных | Base64 encoding, BSON |
| Медленный парсинг | MessagePack, Protocol Buffers |
| Нет схемы | JSON Schema, TypeScript types |

### 8.2 JSON5

```javascript

// JSON5 поддерживает:
{
  // Комментарии
  name: 'Alice',  // Одинарные кавычки
  age: 30,        // Trailing comma OK
  'special-key': true,
}

```

### 8.3 JSONC (JSON with Comments)

```jsonc

{
  // VS Code использует JSONC для settings.json
  "editor.fontSize": 14,
  /* Multi-line
     comments too */
  "editor.tabSize": 2,
}

```

---

## 9. Best Practices

### 9.1 Именование ключей

```json

// ✅ camelCase (JavaScript style)
{"firstName": "Alice", "lastName": "Smith"}

// ✅ snake_case (Python style)
{"first_name": "Alice", "last_name": "Smith"}

// ❌ Смешивание стилей
{"firstName": "Alice", "last_name": "Smith"}

// ❌ Пробелы в ключах
{"first name": "Alice"}

```

### 9.2 Даты и время

```json

// ✅ ISO 8601 format
{
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00+03:00"
}

// ❌ Нестандартные форматы
{
  "date": "01/15/2024",
  "time": "10:30 AM"
}

```

### 9.3 Nullable поля

```json

// ✅ Явный null
{
  "middle_name": null,
  "nickname": null
}

// ✅ Или опустить поле
{
  "first_name": "Alice"
}

// ❌ Пустая строка вместо null
{
  "middle_name": ""
}

```

### 9.4 Числовые ID

```json

// ⚠️ Большие числа могут терять точность в JavaScript
{
  "id": 9007199254740993
}

// ✅ Строковые ID для больших чисел
{
  "id": "9007199254740993"
}

```

---

## 10. Common Pitfalls

### 10.1 Кодировка файла

❌ **Ошибка:** Сохранять JSON не в UTF-8

```python
# Всегда указывайте encoding
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

```

### 10.2 Неэкранированные строки

❌ **Ошибка:**

```json

{"message": "Line 1
Line 2"}

```

✅ **Правильно:**

```json

{"message": "Line 1\nLine 2"}

```

### 10.3 Decimal и float

❌ **Проблема:**

```python

import json
from decimal import Decimal

# Ошибка!
json.dumps({"price": Decimal("19.99")})
# TypeError: Object of type Decimal is not JSON serializable
```

✅ **Решение:**

```python

json.dumps({"price": Decimal("19.99")}, default=str)
# или используйте CustomEncoder из раздела 6.4
```

### 10.4 Круговые ссылки

❌ **Проблема:**

```python

a = {"b": None}
b = {"a": a}
a["b"] = b

json.dumps(a)
# ValueError: Circular reference detected
```

✅ **Решение:** Избегайте циклических структур или используйте специальные библиотеки.

---

## 💡 Key Takeaways

- **JSON — простой формат**: 6 типов данных, строгий синтаксис, нет комментариев.

- **Валидация важна**: Используйте `jq .` или `python -m json.tool` для проверки.

- **jq — мощный инструмент**: Фильтрация, трансформация, агрегация в командной строке.

- **Кодировка — UTF-8**: Всегда используйте UTF-8 и `ensure_ascii=False` для нелатинских символов.

- **Даты — ISO 8601**: Стандартный формат `2024-01-15T10:30:00Z`.

---

## 🚀 Next Steps

**Related Modules:**

- [YAML](../06_YAML/) — более читаемая альтернатива для конфигураций
- [Data Transfer](../12_DataTransfer/) — Base64 для бинарных данных в JSON

**Practice Ideas:**

1. Напишите валидатор JSON файлов с информативными сообщениями об ошибках
2. Создайте jq фильтры для обработки реального API (GitHub, JSONPlaceholder)
3. Реализуйте конвертер JSON → CSV для произвольной структуры
4. Напишите JSON Schema для своего проекта

**Going Deeper:**

- Изучите JSON Patch (RFC 6902) для частичных обновлений
- Посмотрите JSONPath как альтернативу jq
- Разберитесь с BSON (Binary JSON) для MongoDB

---

## 📚 Additional Resources

**Documentation:**

- [JSON.org](https://www.json.org/)
- [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259)
- [jq Manual](https://stedolan.github.io/jq/manual/)

**Tools:**

- [jq play](https://jqplay.org/)
- [JSON Schema](https://json-schema.org/)
- [JSONLint](https://jsonlint.com/)

**Learning:**

- [jq Cookbook](https://github.com/stedolan/jq/wiki/Cookbook)
- [JSON Schema Tutorial](https://json-schema.org/learn/getting-started-step-by-step)

---





