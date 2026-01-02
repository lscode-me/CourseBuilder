# Контракты и документация
## Contract-first подход, OpenAPI/Swagger, JSON Schema, документация как часть API

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать проектирование API
- Знать форматы данных (JSON, XML)
- Иметь представление о валидации данных

**Recommended prior modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [04_Data_Formats](../04_Data_Formats/) — форматы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять contract-first подход к разработке API
- Создавать и использовать OpenAPI/Swagger спецификации
- Работать с JSON Schema для валидации
- Понимать документацию как часть API
- Генерировать клиенты и серверы из контрактов

---

## 1. Contract-First подход

**Contract-First** означает, что контракт API определяется до реализации. Контракт — это источник истины.

### 1.1 Концепция

**Example: Contract-First процесс**

```python
# Шаг 1: Определить контракт (OpenAPI)
# openapi.yaml

"""
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
"""

# Шаг 2: Сгенерировать код из контракта
# Шаг 3: Реализовать логику
# Шаг 4: Валидировать по контракту
```

### 1.2 Преимущества

**Contract-First обеспечивает:**

- Единый источник истины
- Автогенерацию клиентов и серверов
- Валидацию запросов/ответов
- Документацию из контракта

---

## 2. OpenAPI / Swagger

**OpenAPI** (ранее Swagger) — это стандарт для описания REST API.

### 2.1 OpenAPI спецификация

**Example: Базовая OpenAPI спецификация**

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
  description: API для работы с пользователями

paths:
  /users:
    get:
      summary: Список пользователей
      responses:
        '200':
          description: Успешно
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    
    post:
      summary: Создать пользователя
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: Пользователь создан
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
          format: email
      required:
        - id
        - name
        - email
    
    CreateUserRequest:
      type: object
      properties:
        name:
          type: string
        email:
          type: string
          format: email
      required:
        - name
        - email
```

### 2.2 Использование OpenAPI

**Example: Генерация из OpenAPI**

```python
# Установка: pip install openapi-generator-cli

# Генерация клиента Python из OpenAPI
# openapi-generator generate -i openapi.yaml -g python -o ./client

# Генерация сервера
# openapi-generator generate -i openapi.yaml -g python-flask -o ./server

# Валидация запросов по OpenAPI

from openapi_core import validate_request
from openapi_core.contrib.flask import FlaskOpenAPIRequest

def validate_api_request(request):
    """Валидация запроса по OpenAPI"""
    openapi_request = FlaskOpenAPIRequest(request)
    validate_request(openapi_request, spec)
```

---

## 3. JSON Schema

**JSON Schema** определяет структуру и правила валидации JSON данных.

### 3.1 JSON Schema определение

**Example: JSON Schema для пользователя**

```python
import jsonschema

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

# Валидация

def validate_user(data):
    try:
        jsonschema.validate(instance=data, schema=user_schema)
        return True, None
    except jsonschema.ValidationError as e:
        return False, str(e)
```

### 3.2 JSON Schema в OpenAPI

**Example: JSON Schema в OpenAPI**

```yaml
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          minimum: 1
        name:
          type: string
          minLength: 1
          maxLength: 100
        email:
          type: string
          format: email
      required:
        - id
        - name
        - email
      additionalProperties: false
```

---

## 4. Документация как часть API

Документация должна быть частью API, а не отдельным документом.

### 4.1 Автогенерация документации

**Example: Swagger UI из OpenAPI**

```python
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI

SWAGGER_URL = '/api/docs'
API_URL = '/api/openapi.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "User API"}
)

app.register_blueprint(swaggerui_blueprint)

# OpenAPI JSON endpoint

@app.route('/api/openapi.json')
def openapi_spec():
    return jsonify(load_openapi_spec())
```

### 4.2 Интерактивная документация

**Swagger UI предоставляет:**

- Интерактивное тестирование API
- Примеры запросов/ответов
- Валидацию в реальном времени

---

## 5. Best Practices

### 5.1 Contract-First workflow

1. Определить контракт (OpenAPI)
2. Сгенерировать код
3. Реализовать логику
4. Валидировать по контракту
5. Обновить документацию автоматически

### 5.2 Версионирование контрактов

**Example: Версионирование OpenAPI**

```yaml
# openapi.v1.yaml

openapi: 3.0.0
info:
  title: User API
  version: 1.0.0

# openapi.v2.yaml

openapi: 3.0.0
info:
  title: User API
  version: 2.0.0
```

### 5.3 Валидация запросов по контракту

**Example: Валидация запросов**

```python
from openapi_core import validate_request
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.exceptions import OpenAPIError

@app.before_request
def validate_api_request():
    """Валидация запроса по OpenAPI контракту"""
    try:
        openapi_request = FlaskOpenAPIRequest(request)
        validate_request(openapi_request, openapi_spec)
    except OpenAPIError as e:
        return jsonify({
            "error": "Validation failed",
            "details": str(e)
        }), 400
```

### 5.4 Генерация клиентов из контракта

**Example: Генерация Python клиента**

```python
# Использование openapi-generator
# openapi-generator generate -i openapi.yaml -g python -o ./client

# Использование сгенерированного клиента

from client import ApiClient, UsersApi

client = ApiClient(host="https://api.example.com")
users_api = UsersApi(client)

# Автоматически типизированные методы из контракта

user = users_api.get_user(user_id=123)
users = users_api.list_users()
new_user = users_api.create_user({
    "name": "Иван",
    "email": "ivan@example.com"
})
```

### 5.5 Генерация серверов из контракта

**Example: Генерация Flask сервера**

```python
# Генерация: openapi-generator generate -i openapi.yaml -g python-flask -o ./server

# Сгенерированный сервер имеет заглушки методов

from server import UsersApi

class UsersApiImpl(UsersApi):
    """Реализация методов из контракта"""
    
    def get_user(self, user_id):
        """Реализация GET /users/{id}"""
        user = db.get_user(user_id)
        if not user:
            raise NotFound(f"User {user_id} not found")
        return user
    
    def create_user(self, user_data):
        """Реализация POST /users"""
        user = db.create_user(user_data)
        return user, 201
```

## 6. JSON Schema валидация

### 6.1 Расширенная валидация

**Example: Сложная JSON Schema**

```python
complex_schema = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "minimum": 1},
                "name": {"type": "string", "minLength": 1, "maxLength": 100},
                "email": {"type": "string", "format": "email"},
                "age": {"type": "integer", "minimum": 0, "maximum": 150},
                "tags": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 0,
                    "maxItems": 10
                }
            },
            "required": ["id", "name", "email"]
        }
    },
    "required": ["user"],
    "additionalProperties": False
}

def validate_complex_data(data):
    """Валидация сложной структуры"""
    try:
        jsonschema.validate(instance=data, schema=complex_schema)
        return True, None
    except jsonschema.ValidationError as e:
        return False, {
            "path": list(e.path),
            "message": e.message,
            "validator": e.validator
        }
```

### 6.2 Кастомные валидаторы

**Example: Кастомная валидация**

```python
from jsonschema import validate, ValidationError

def validate_phone(validator, phone, instance, schema):
    """Кастомный валидатор для телефона"""
    import re
    phone_pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(phone_pattern, instance):
        yield ValidationError(f"{instance} is not a valid phone number")

# Расширение валидатора

from jsonschema.validators import extend
CustomValidator = extend(jsonschema.Draft7Validator, {
    "phone": validate_phone
})

schema = {
    "type": "object",
    "properties": {
        "phone": {"type": "string", "phone": True}
    }
}

CustomValidator(schema).validate({"phone": "+1234567890"})
```

## 7. Common Pitfalls

### 7.1 Pitfall: Контракт после реализации

❌ **Incorrect:**
```python
# Плохо: Реализация перед контрактом

def get_user(user_id):
    return {"id": user_id, "name": "Иван"}

# Контракт создаётся потом и может не совпадать
```

✅ **Correct:**
```python
# Хорошо: Контракт перед реализацией
# 1. Создать OpenAPI контракт
# 2. Сгенерировать код
# 3. Реализовать логику

def get_user(user_id):
    return {"id": user_id, "name": "Иван"}  # Соответствует контракту
```

**Why:** Контракт должен быть источником истины.

### 7.2 Pitfall: Устаревшая документация

❌ **Incorrect:**
```python
# Плохо: Документация обновляется вручную
# Может расходиться с кодом
```

✅ **Correct:**
```python
# Хорошо: Документация генерируется из контракта
# Всегда актуальна

swagger_ui = get_swaggerui_blueprint(
    '/api/docs',
    '/api/openapi.json'  # Генерируется из контракта
)
```

**Why:** Автогенерация исключает расхождения.

---

## 💡 Key Takeaways

- **Contract-First**: Контракт определяется до реализации, является источником истины и позволяет автогенерацию кода

- **OpenAPI/Swagger**: Стандарт для описания REST API, обеспечивает автогенерацию клиентов/серверов и интерактивную документацию

- **JSON Schema**: Определяет структуру и правила валидации JSON данных, используется в OpenAPI для описания схем

- **Документация как часть API**: Документация генерируется из контракта, всегда актуальна и доступна через Swagger UI

- **Автогенерация**: Контракты позволяют генерировать клиенты, серверы, тесты и документацию, снижая ошибки и ускоряя разработку

---

## 🚀 Next Steps

**Related Modules:**

- [09_Versioning](../09_Versioning/) — версионирование и совместимость
- [07_API_Design](../07_API_Design/) — проектирование API
- [11_API_Implementation](../11_API_Implementation/) — реализация API

**Practice Ideas:**

1. Создайте OpenAPI спецификацию для вашего API
2. Сгенерируйте клиент и сервер из OpenAPI
3. Настройте Swagger UI для интерактивной документации

**Going Deeper:**

- OpenAPI Specification: полная спецификация OpenAPI
- JSON Schema Specification: спецификация JSON Schema
- API Documentation Best Practices: лучшие практики документации

---

## 📚 Additional Resources

**Documentation:**

- [OpenAPI Specification](https://swagger.io/specification/) — спецификация OpenAPI
- [JSON Schema](https://json-schema.org/) — спецификация JSON Schema
- [Swagger UI](https://swagger.io/tools/swagger-ui/) — интерактивная документация

**Articles:**

- "Contract-First API Development" — разработка API с contract-first подходом
- "OpenAPI Best Practices" — лучшие практики OpenAPI

---




