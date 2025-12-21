# Проектирование API
## Ресурсы и URI, HTTP методы и идемпотентность, Status codes, Error handling

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать REST как архитектурный стиль
- Знать основы HTTP протокола
- Иметь представление о проектировании интерфейсов

**Recommended prior modules:**

- [06_API_Standards](../06_API_Standards/) — API стандарты и стили
- [02_Types_of_API](../02_Types_of_API/) — типы API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проектировать RESTful API с правильной структурой ресурсов и URI
- Применять HTTP методы согласно их семантике и идемпотентности
- Использовать правильные HTTP status codes
- Реализовывать стандартизированную обработку ошибок
- Создавать интуитивно понятные и поддерживаемые API

---

## 1. Ресурсы и URI

В REST всё является ресурсом, идентифицируемым через URI. Правильное проектирование ресурсов критично для понятного API.

### 1.1 Именование ресурсов

**Правила именования ресурсов:**

- Используйте существительные, не глаголы
- Используйте множественное число для коллекций
- Используйте иерархию для вложенных ресурсов
- Избегайте глубокой вложенности (> 2 уровней)

**Example: Правильное именование ресурсов**

```python
# ✅ Хорошо: существительные, множественное число
GET    /api/users
GET    /api/users/123
GET    /api/users/123/orders
GET    /api/users/123/orders/456

# ❌ Плохо: глаголы, единственное число
GET    /api/getUser
GET    /api/user
GET    /api/getUserOrders
```

### 1.2 Структура URI

**Example: Иерархия ресурсов**

```python
# Коллекции
GET    /api/users              # Список пользователей
POST   /api/users              # Создать пользователя

# Конкретный ресурс
GET    /api/users/123          # Получить пользователя
PUT    /api/users/123          # Обновить пользователя
DELETE /api/users/123          # Удалить пользователя

# Вложенные ресурсы
GET    /api/users/123/orders           # Заказы пользователя
POST   /api/users/123/orders           # Создать заказ
GET    /api/users/123/orders/456       # Конкретный заказ

# Избегайте глубокой вложенности
# ❌ Плохо: /api/users/123/orders/456/items/789/prices/1
# ✅ Хорошо: /api/order-items/789/price

```

---

## 2. HTTP методы и идемпотентность

HTTP методы имеют семантическое значение. Понимание идемпотентности критично для правильного использования методов.

### 2.1 Семантика HTTP методов

| Метод | Операция | Идемпотентность | Безопасность | Тело запроса |
|-------|----------|-----------------|--------------|--------------|
| GET | Чтение | Да | Да | Нет |
| POST | Создание | Нет | Нет | Да |
| PUT | Обновление/Создание | Да | Нет | Да |
| PATCH | Частичное обновление | Нет | Нет | Да |
| DELETE | Удаление | Да | Нет | Нет |

**Example: Использование HTTP методов**

```python

import requests

base_url = "https://api.example.com"

# GET - безопасное чтение (идемпотентно)
user = requests.get(f"{base_url}/users/123").json()

# POST - создание (не идемпотентно)
new_user = requests.post(
    f"{base_url}/users",
    json={"name": "Иван", "email": "ivan@example.com"}
).json()

# PUT - полное обновление (идемпотентно)
updated = requests.put(
    f"{base_url}/users/123",
    json={"name": "Иван Иванов", "email": "ivan@example.com"}
).json()

# PATCH - частичное обновление (не идемпотентно)
patched = requests.patch(
    f"{base_url}/users/123",
    json={"name": "Иван Иванов"}
).json()

# DELETE - удаление (идемпотентно)
requests.delete(f"{base_url}/users/123")
```

### 2.2 Идемпотентность

**Идемпотентность** означает, что повторный вызов операции даёт тот же результат.

**Example: Идемпотентные операции**

```python
# GET - идемпотентен (повторный вызов даёт тот же результат)
user1 = requests.get(f"{base_url}/users/123").json()
user2 = requests.get(f"{base_url}/users/123").json()
# user1 == user2

# PUT - идемпотентен (повторное обновление даёт тот же результат)
requests.put(f"{base_url}/users/123", json={"name": "Иван"})
requests.put(f"{base_url}/users/123", json={"name": "Иван"})
# Результат одинаковый

# DELETE - идемпотентен (повторное удаление даёт тот же результат)
requests.delete(f"{base_url}/users/123")  # 204 No Content
requests.delete(f"{base_url}/users/123")  # 404 Not Found (уже удалён)
# Оба вызова безопасны

# POST - НЕ идемпотентен (каждый вызов создаёт новый ресурс)
requests.post(f"{base_url}/users", json={"name": "Иван"})  # Создаёт пользователя 1
requests.post(f"{base_url}/users", json={"name": "Иван"})  # Создаёт пользователя 2
# Разные результаты

```

---

## 3. HTTP Status Codes

HTTP status codes сообщают результат операции. Правильное использование status codes критично для понятного API.

### 3.1 Категории status codes

| Категория | Коды | Описание |
|-----------|------|----------|
| **2xx Success** | 200-299 | Успешная операция |
| **3xx Redirection** | 300-399 | Перенаправление |
| **4xx Client Error** | 400-499 | Ошибка клиента |
| **5xx Server Error** | 500-599 | Ошибка сервера |

### 3.2 Основные status codes

**Example: Использование status codes**

```python

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify(user), 200  # OK
    return jsonify({"error": "Not found"}), 404  # Not Found

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    if not validate_user_data(data):
        return jsonify({"error": "Validation failed"}), 400  # Bad Request
    
    user = create_user(data)
    return jsonify(user), 201  # Created

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    
    updated = update_user_data(user_id, request.json)
    return jsonify(updated), 200  # OK

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not find_user(user_id):
        return jsonify({"error": "Not found"}), 404
    
    delete_user_data(user_id)
    return "", 204  # No Content

# Ошибка сервера
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
```

### 3.3 Часто используемые status codes

| Код | Название | Использование |
|-----|----------|---------------|
| 200 | OK | Успешный GET, PUT, PATCH |
| 201 | Created | Успешное создание (POST) |
| 204 | No Content | Успешное удаление (DELETE) |
| 400 | Bad Request | Невалидный запрос |
| 401 | Unauthorized | Требуется аутентификация |
| 403 | Forbidden | Доступ запрещён |
| 404 | Not Found | Ресурс не найден |
| 409 | Conflict | Конфликт (например, дубликат) |
| 422 | Unprocessable Entity | Валидация не прошла |
| 500 | Internal Server Error | Ошибка сервера |

---

## 4. Error Handling

Стандартизированная обработка ошибок упрощает интеграцию и отладку.

### 4.1 Структура ошибок

**Example: Стандартизированная структура ошибок**

```python

def error_response(code, message, details=None):
    """Стандартизированная структура ошибки"""
    error = {
        "error": {
            "code": code,
            "message": message,
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

conflict_error = error_response(
    "CONFLICT",
    "Email already exists",
    {"field": "email", "value": "existing@example.com"}
)
```

### 4.2 Обработка различных типов ошибок

**Example: Обработка ошибок в API**

```python

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        if not data:
            return jsonify({
                "error": {
                    "code": "BAD_REQUEST",
                    "message": "Request body is required"
                }
            }), 400
        
        # Валидация
        if "email" not in data:
            return jsonify({
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Email is required",
                    "details": {"field": "email"}
                }
            }), 422
        
        # Проверка дубликатов
        if user_exists(data["email"]):
            return jsonify({
                "error": {
                    "code": "CONFLICT",
                    "message": "Email already exists",
                    "details": {"field": "email", "value": data["email"]}
                }
            }), 409
        
        # Создание
        user = create_user_data(data)
        return jsonify(user), 201
    
    except Exception as e:
        # Логирование ошибки
        log_error(e)
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An error occurred"
            }
        }), 500
```

---

## 5. Best Practices

### 5.1 Версионирование в URI

**Example: Версионирование API**

```python
# Версионирование в URI
GET /api/v1/users
GET /api/v2/users

# Или в заголовке
GET /api/users
Headers: Accept: application/vnd.api.v1+json
```

### 5.2 Пагинация

**Example: Пагинация в API**

```python

@app.route("/api/users", methods=["GET"])
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    
    users, total = get_users_paginated(page, per_page)
    
    return jsonify({
        "data": users,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": (total + per_page - 1) // per_page
        }
    }), 200
```

### 5.3 Фильтрация и сортировка

**Example: Фильтрация и сортировка**

```python

@app.route("/api/users", methods=["GET"])
def get_users():
    # Фильтрация
    status = request.args.get("status")
    role = request.args.get("role")
    
    # Сортировка
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")
    
    users = get_users_filtered(status=status, role=role, sort_by=sort_by, order=order)
    return jsonify(users), 200
```

---

## 6. Common Pitfalls

### 6.1 Pitfall: Неправильное использование HTTP методов

❌ **Incorrect:**
```python
# Плохо: POST для получения данных
POST /api/getUser
POST /api/getUsers
```

✅ **Correct:**
```python
# Хорошо: GET для чтения
GET /api/users/123
GET /api/users
```

**Why:** HTTP методы имеют семантическое значение. GET для чтения, POST для создания.

### 6.2 Pitfall: Неправильные status codes

❌ **Incorrect:**
```python
# Плохо: 200 для ошибки
return jsonify({"error": "Not found"}), 200
```

✅ **Correct:**
```python
# Хорошо: 404 для не найденного ресурса
return jsonify({"error": "Not found"}), 404
```

**Why:** Status codes сообщают результат операции. Неправильные коды вводят в заблуждение.

---

## 💡 Key Takeaways

- **Ресурсы и URI**: Используйте существительные во множественном числе, иерархию для вложенных ресурсов, избегайте глубокой вложенности. URI должны быть интуитивно понятными

- **HTTP методы**: GET для чтения, POST для создания, PUT для полного обновления, PATCH для частичного, DELETE для удаления. Понимайте идемпотентность методов

- **Status codes**: Используйте правильные коды (200 для успеха, 201 для создания, 404 для не найденного, 400/422 для ошибок валидации, 500 для серверных ошибок)

- **Error handling**: Стандартизированная структура ошибок с кодом, сообщением и опциональными деталями упрощает интеграцию и отладку

- **Best practices**: Версионирование, пагинация, фильтрация и сортировка делают API более функциональным и удобным для использования

---

## 🚀 Next Steps

**Related Modules:**

- [09_Versioning](../09_Versioning/) — версионирование и совместимость
- [10_Contracts_Documentation](../10_Contracts_Documentation/) — контракты и документация
- [16_API_Design_Review](../16_API_Design_Review/) — API design review

**Practice Ideas:**

1. Спроектируйте RESTful API для ресурса (например, задачи или заметки)
2. Реализуйте правильные HTTP методы и status codes
3. Создайте стандартизированную обработку ошибок

**Going Deeper:**

- REST API Design Best Practices: лучшие практики проектирования REST API
- HTTP Status Codes Guide: полное руководство по status codes
- API Design Patterns: паттерны проектирования API

---

## 📚 Additional Resources

**Documentation:**

- [HTTP Status Codes](https://httpstatuses.com/) — справочник status codes
- [REST API Tutorial](https://restfulapi.net/) — руководство по REST

**Articles:**

- "REST API Design Best Practices" — лучшие практики проектирования
- "Understanding HTTP Methods and Idempotency" — понимание HTTP методов

---


