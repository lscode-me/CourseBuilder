# Форматы данных и сообщения
## JSON, XML, структура сообщений и валидация схем

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы API и интеграции
- Знать типы API (REST, SOAP, RPC)
- Иметь представление о структуре данных

**Recommended prior modules:**

- [01_What_is_API](../01_What_is_API/) — основы API и интеграции
- [02_Types_of_API](../02_Types_of_API/) — типы API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с JSON и XML форматами данных
- Понимать структуру сообщений в API
- Применять схемы для валидации данных
- Выбирать подходящий формат для конкретной задачи
- Валидировать данные согласно схемам

---

## 1. Введение в форматы данных

Формат данных определяет, как информация представлена и передаётся между системами. Выбор формата влияет на размер сообщений, скорость обработки и совместимость.

**Критерии выбора формата:**

- Размер сообщения
- Скорость парсинга
- Читаемость человеком
- Поддержка схемы
- Совместимость с системами

---

## 2. JSON (JavaScript Object Notation)

**JSON** — это текстовый формат обмена данными, основанный на синтаксисе JavaScript. JSON стал стандартом де-факто для REST API.

### 2.1 Структура JSON

**Example: Базовые типы данных в JSON**

```python
import json

# JSON поддерживает различные типы данных

json_data = {
    "string": "Hello, World!",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "array": [1, 2, 3],
    "object": {
        "nested": "value",
        "another": 123
    }
}

# Сериализация в JSON

json_string = json.dumps(json_data, indent=2)
print(json_string)
```

**Output:**
```json
{
  "string": "Hello, World!",
  "number": 42,
  "float": 3.14,
  "boolean": true,
  "null": null,
  "array": [1, 2, 3],
  "object": {
    "nested": "value",
    "another": 123
  }
}
```

### 2.2 JSON в API запросах и ответах

**Example: JSON в REST API**

```python
import requests
import json

# JSON в запросе

def create_user(name, email):
    """Создание пользователя через API"""
    data = {
        "name": name,
        "email": email
    }
    response = requests.post(
        'https://api.example.com/users',
        json=data,  # Автоматическая сериализация в JSON
        headers={'Content-Type': 'application/json'}
    )
    return response.json()

# JSON в ответе

def get_user(user_id):
    """Получение пользователя"""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    user_data = response.json()  # Автоматическая десериализация
    return user_data

# Использование

user = create_user('Иван', 'ivan@example.com')
print(f"Created user: {user['id']}")

retrieved = get_user(user['id'])
print(f"Retrieved: {retrieved['name']}")
```

**Output:**
```
Created user: 123
Retrieved: Иван
```

### 2.3 Преимущества JSON

**JSON популярен потому что:**

- Легко читается человеком
- Компактный формат
- Быстрый парсинг
- Широкая поддержка в языках программирования
- Нативный формат для JavaScript

---

## 3. XML (eXtensible Markup Language)

**XML** — это язык разметки для хранения и передачи структурированных данных. XML используется в SOAP API и многих enterprise системах.

### 3.1 Структура XML

**Example: Базовый XML документ**

```python
from xml.etree import ElementTree as ET

# Создание XML структуры

root = ET.Element("user")
root.set("id", "123")

name = ET.SubElement(root, "name")
name.text = "Иван Иванов"

email = ET.SubElement(root, "email")
email.text = "ivan@example.com"

address = ET.SubElement(root, "address")
city = ET.SubElement(address, "city")
city.text = "Москва"
country = ET.SubElement(address, "country")
country.text = "Россия"

# Сериализация в XML

xml_string = ET.tostring(root, encoding='unicode')
print(xml_string)
```

**Output:**
```xml
<user id="123">
  <name>Иван Иванов</name>
  <email>ivan@example.com</email>
  <address>
    <city>Москва</city>
    <country>Россия</country>
  </address>
</user>
```

### 3.2 XML в SOAP API

**Example: SOAP сообщение**

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetUser xmlns="http://example.com/api">
      <UserId>123</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>
```

### 3.3 Преимущества и недостатки XML

**Преимущества XML:**

- Строгая структура
- Поддержка схем (XSD)
- Самодокументируемость
- Широкая поддержка в enterprise системах

**Недостатки XML:**

- Больший размер по сравнению с JSON
- Медленнее парсинг
- Более сложный синтаксис

---

## 4. Сравнение JSON и XML

### 4.1 Сравнительная таблица

| Критерий | JSON | XML |
|----------|------|-----|
| **Размер** | Компактный | Больше |
| **Читаемость** | Высокая | Средняя |
| **Парсинг** | Быстрый | Медленнее |
| **Схемы** | JSON Schema | XSD |
| **Использование** | REST API, веб | SOAP, enterprise |
| **Типизация** | Слабая | Строгая |

### 4.2 Когда использовать JSON vs XML

**Используйте JSON если:**

- REST API
- Веб-приложения
- Мобильные приложения
- Нужна компактность и скорость

**Используйте XML если:**

- SOAP API
- Enterprise интеграции
- Нужна строгая валидация через XSD
- Legacy системы

---

## 5. Структура сообщений

Структура сообщения определяет, как данные организованы в запросе или ответе API.

### 5.1 Базовая структура сообщения

**Example: Структура REST API ответа**

```python
# Стандартная структура ответа

def standard_api_response(data, status="success", message=None):
    """Стандартизированная структура ответа API"""
    response = {
        "status": status,
        "data": data,
        "timestamp": "2024-01-15T10:30:00Z"
    }
    if message:
        response["message"] = message
    return response

# Успешный ответ

success_response = standard_api_response(
    {"id": 123, "name": "Иван"},
    status="success"
)
print(json.dumps(success_response, indent=2))
```

**Output:**
```json
{
  "status": "success",
  "data": {
    "id": 123,
    "name": "Иван"
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### 5.2 Структура ошибок

**Example: Стандартизированная структура ошибок**

```python
def error_response(error_code, error_message, details=None):
    """Стандартизированная структура ошибки"""
    error = {
        "error": {
            "code": error_code,
            "message": error_message,
            "timestamp": "2024-01-15T10:30:00Z"
        }
    }
    if details:
        error["error"]["details"] = details
    return error

# Примеры ошибок

validation_error = error_response(
    "VALIDATION_ERROR",
    "Invalid email format",
    {"field": "email", "value": "invalid-email"}
)

not_found_error = error_response(
    "NOT_FOUND",
    "User not found",
    {"resource": "user", "id": 123}
)

print("Validation Error:")
print(json.dumps(validation_error, indent=2))
```

**Output:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "timestamp": "2024-01-15T10:30:00Z",
    "details": {
      "field": "email",
      "value": "invalid-email"
    }
  }
}
```

### 5.3 Пагинация в ответах

**Example: Структура пагинированного ответа**

```python
def paginated_response(items, page, per_page, total):
    """Структура пагинированного ответа"""
    return {
        "data": items,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": (total + per_page - 1) // per_page
        }
    }

# Пример пагинированного ответа

response = paginated_response(
    items=[{"id": 1}, {"id": 2}, {"id": 3}],
    page=1,
    per_page=10,
    total=25
)
print(json.dumps(response, indent=2))
```

**Output:**
```json
{
  "data": [
    {"id": 1},
    {"id": 2},
    {"id": 3}
  ],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 25,
    "total_pages": 3
  }
}
```

---

## 6. Схемы и валидация данных

Схемы определяют структуру и правила валидации данных, обеспечивая контракт между системами.

### 6.1 JSON Schema

**JSON Schema** — это стандарт для описания структуры JSON данных.

**Example: JSON Schema для пользователя**

```python
import jsonschema
from jsonschema import validate

# JSON Schema определение

user_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1
        },
        "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "age": {
            "type": "integer",
            "minimum": 0,
            "maximum": 150
        }
    },
    "required": ["id", "name", "email"],
    "additionalProperties": False
}

# Валидация данных

def validate_user(data):
    """Валидация данных пользователя по схеме"""
    try:
        validate(instance=data, schema=user_schema)
        return True, None
    except jsonschema.ValidationError as e:
        return False, str(e)

# Валидные данные

valid_user = {
    "id": 123,
    "name": "Иван",
    "email": "ivan@example.com",
    "age": 30
}
is_valid, error = validate_user(valid_user)
print(f"Valid: {is_valid}")

# Невалидные данные

invalid_user = {
    "id": "not-a-number",
    "name": "",
    "email": "invalid-email"
}
is_valid, error = validate_user(invalid_user)
print(f"Valid: {is_valid}, Error: {error}")
```

**Output:**
```
Valid: True
Valid: False, Error: 'not-a-number' is not of type 'integer'
```

### 6.2 XSD для XML

**XSD (XML Schema Definition)** — это схема для валидации XML документов.

**Example: XSD схема**

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="user">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="id" type="xs:integer"/>
        <xs:element name="name" type="xs:string"/>
        <xs:element name="email" type="xs:string"/>
      </xs:sequence>
      <xs:attribute name="active" type="xs:boolean"/>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### 6.3 Валидация в API

**Example: Валидация запроса в API**

```python
from flask import Flask, request, jsonify
import jsonschema

app = Flask(__name__)

# Схема для создания пользователя

create_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "email"],
    "additionalProperties": False
}

@app.route('/api/users', methods=['POST'])
def create_user():
    """Создание пользователя с валидацией"""
    data = request.json
    
    # Валидация по схеме
    try:
        jsonschema.validate(instance=data, schema=create_user_schema)
    except jsonschema.ValidationError as e:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": str(e)
            }
        }), 400
    
    # Создание пользователя
    user = {
        "id": 123,
        "name": data["name"],
        "email": data["email"]
    }
    return jsonify(user), 201
```

---

## 7. Практические примеры

### 7.1 Пример: API с JSON Schema валидацией

```python
class ValidatedAPI:
    """API с валидацией через JSON Schema"""
    
    def __init__(self):
        self.schemas = {}
    
    def register_schema(self, endpoint, schema):
        """Регистрация схемы для endpoint"""
        self.schemas[endpoint] = schema
    
    def validate_request(self, endpoint, data):
        """Валидация запроса"""
        if endpoint in self.schemas:
            try:
                jsonschema.validate(instance=data, schema=self.schemas[endpoint])
                return True, None
            except jsonschema.ValidationError as e:
                return False, e.message
        return True, None  # Нет схемы - пропускаем

# Использование

api = ValidatedAPI()
api.register_schema('/users', create_user_schema)

is_valid, error = api.validate_request('/users', {
    "name": "Иван",
    "email": "ivan@example.com"
})
print(f"Valid: {is_valid}")
```

**Output:**
```
Valid: True
```

---

## 8. Common Pitfalls

### 8.1 Pitfall: Отсутствие валидации

❌ **Incorrect:**
```python
def unsafe_create_user(data):
    # Нет валидации
    user = {
        "id": data["id"],
        "name": data["name"],
        "email": data["email"]
    }
    return user
```

✅ **Correct:**
```python
def safe_create_user(data):
    # Валидация по схеме
    jsonschema.validate(instance=data, schema=user_schema)
    user = {
        "id": data["id"],
        "name": data["name"],
        "email": data["email"]
    }
    return user
```

**Why:** Валидация предотвращает ошибки и обеспечивает соответствие контракту.

### 8.2 Pitfall: Нестандартная структура ошибок

❌ **Incorrect:**
```python
# Разные форматы ошибок

return "Error: User not found"
return {"error": "User not found"}
return {"message": "User not found", "code": 404}
```

✅ **Correct:**
```python
# Стандартизированный формат

return {
    "error": {
        "code": "NOT_FOUND",
        "message": "User not found",
        "timestamp": "2024-01-15T10:30:00Z"
    }
}
```

**Why:** Стандартизированная структура упрощает обработку ошибок клиентами.

---

## 💡 Key Takeaways

- **JSON vs XML**: JSON компактнее и быстрее, подходит для REST API. XML строже и поддерживает схемы, используется в SOAP и enterprise системах

- **Структура сообщений**: Стандартизированная структура запросов и ответов упрощает интеграцию и обработку ошибок

- **Схемы и валидация**: JSON Schema и XSD обеспечивают контракт данных, предотвращают ошибки и гарантируют соответствие структуре

- **Выбор формата**: JSON для современных веб-API, XML для enterprise и SOAP интеграций. Выбор зависит от требований к валидации и совместимости

- **Валидация критична**: Валидация данных по схемам предотвращает ошибки, обеспечивает безопасность и соответствие контракту API

---

## 🚀 Next Steps

**Related Modules:**

- [05_Authentication_Basics](../05_Authentication_Basics/) — основы аутентификации и авторизации
- [10_Contracts_Documentation](../10_Contracts_Documentation/) — контракты и документация API
- [07_API_Design](../07_API_Design/) — проектирование API

**Practice Ideas:**

1. Создайте JSON Schema для вашего API
2. Реализуйте валидацию запросов и ответов
3. Сравните размер и скорость парсинга JSON vs XML

**Going Deeper:**

- JSON Schema Specification: полная спецификация JSON Schema
- XML Schema (XSD): углублённое изучение XSD
- Data Validation Patterns: паттерны валидации данных

---

## 📚 Additional Resources

**Documentation:**

- [JSON Schema](https://json-schema.org/) — спецификация JSON Schema
- [XML Schema (XSD)](https://www.w3.org/XML/Schema) — спецификация XSD

**Articles:**

- "JSON vs XML: Which is Better?" — сравнение форматов
- "API Response Structure Best Practices" — лучшие практики структуры ответов

---



