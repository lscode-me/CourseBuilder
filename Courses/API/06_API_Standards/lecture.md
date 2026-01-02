# API стандарты и стили
## REST как архитектурный стиль, SOAP и WSDL, GraphQL

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать типы API (REST, SOAP, RPC, Event-based)
- Знать основы HTTP протокола
- Иметь представление о форматах данных (JSON, XML)

**Recommended prior modules:**

- [02_Types_of_API](../02_Types_of_API/) — типы API
- [04_Data_Formats](../04_Data_Formats/) — форматы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать REST как архитектурный стиль и его принципы
- Работать с SOAP и WSDL для формальных контрактов
- Применять GraphQL для гибких запросов данных
- Выбирать подходящий стандарт для конкретной задачи
- Сравнивать преимущества и ограничения различных стандартов

---

## 1. REST как архитектурный стиль

**REST (Representational State Transfer)** — это архитектурный стиль, а не протокол или стандарт. REST определяет принципы проектирования распределённых систем.

### 1.1 Принципы REST

**Основные принципы REST:**

- **Ресурсы**: Всё является ресурсом, идентифицируемым URI

- **HTTP методы**: Стандартные методы (GET, POST, PUT, DELETE) для операций

- **Stateless**: Каждый запрос содержит всю необходимую информацию

- **Кэшируемость**: Ответы могут кэшироваться

- **Единообразный интерфейс**: Стандартные способы взаимодействия

- **Layered system**: Многоуровневая архитектура

**Example: RESTful API структура**

```python
# REST API использует ресурсы и HTTP методы

# Ресурс: пользователи

GET    /api/users           # Список пользователей
GET    /api/users/123       # Конкретный пользователь
POST   /api/users           # Создать пользователя
PUT    /api/users/123       # Обновить пользователя
DELETE /api/users/123       # Удалить пользователя

# Вложенные ресурсы

GET    /api/users/123/orders        # Заказы пользователя
POST   /api/users/123/orders        # Создать заказ

import requests

# RESTful вызовы

base_url = "https://api.example.com"

# Получить пользователя (GET)

user = requests.get(f"{base_url}/users/123").json()
print(f"User: {user['name']}")

# Создать пользователя (POST)

new_user = requests.post(
    f"{base_url}/users",
    json={"name": "Иван", "email": "ivan@example.com"}
).json()
print(f"Created: {new_user['id']}")
```

**Output:**
```
User: Иван
Created: 456
```

### 1.2 REST Constraints

**Ограничения REST (constraints):**

1. **Client-Server**: Разделение клиента и сервера
2. **Stateless**: Сервер не хранит состояние клиента
3. **Cacheable**: Ответы должны быть помечены как кэшируемые или нет
4. **Uniform Interface**: Единообразный интерфейс
5. **Layered System**: Многоуровневая архитектура
6. **Code on Demand** (опционально): Сервер может отправлять исполняемый код

---

## 2. SOAP и WSDL

**SOAP (Simple Object Access Protocol)** — это протокол для обмена структурированными сообщениями. **WSDL (Web Services Description Language)** — это язык описания SOAP веб-сервисов.

### 2.1 SOAP структура

**Example: SOAP сообщение**

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <Authentication>
      <Token>abc123</Token>
    </Authentication>
  </soap:Header>
  <soap:Body>
    <GetUser xmlns="http://example.com/api">
      <UserId>123</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>
```

### 2.2 WSDL контракт

**WSDL** формально описывает SOAP API через XML.

**Example: WSDL определение**

```xml
<?xml version="1.0"?>
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/">
  <types>
    <schema>
      <element name="GetUserRequest">
        <complexType>
          <sequence>
            <element name="UserId" type="int"/>
          </sequence>
        </complexType>
      </element>
      <element name="GetUserResponse">
        <complexType>
          <sequence>
            <element name="User" type="tns:User"/>
          </sequence>
        </complexType>
      </element>
    </schema>
  </types>
  
  <message name="GetUserRequest">
    <part name="body" element="tns:GetUserRequest"/>
  </message>
  
  <portType name="UserService">
    <operation name="GetUser">
      <input message="tns:GetUserRequest"/>
      <output message="tns:GetUserResponse"/>
    </operation>
  </portType>
</definitions>
```

### 2.3 SOAP преимущества

**SOAP обеспечивает:**

- Формальные контракты через WSDL
- Встроенную безопасность (WS-Security)
- Поддержку транзакций
- Стандартизацию для enterprise

---

## 3. GraphQL

**GraphQL** — это язык запросов и runtime для выполнения запросов к API. GraphQL позволяет клиентам запрашивать только нужные данные.

### 3.1 Концепция GraphQL

**GraphQL решает проблему over-fetching и under-fetching:**

- **Over-fetching**: Получение лишних данных

- **Under-fetching**: Недостаточно данных, нужны дополнительные запросы

**Example: GraphQL запрос**

```python
# GraphQL запрос — клиент определяет, какие поля нужны

query = """
{
  user(id: 123) {
    id
    name
    email
    orders {
      id
      total
      items {
        name
        price
      }
    }
  }
}
"""

# Один запрос получает все нужные данные

import requests

response = requests.post(
    "https://api.example.com/graphql",
    json={"query": query}
)
data = response.json()
print(f"User: {data['data']['user']['name']}")
print(f"Orders: {len(data['data']['user']['orders'])}")
```

**Output:**
```
User: Иван
Orders: 3
```

### 3.2 GraphQL Schema

**GraphQL Schema** определяет типы данных и операции.

**Example: GraphQL Schema**

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Order {
  id: ID!
  total: Float!
  items: [OrderItem!]!
}

type Query {
  user(id: ID!): User
  users: [User!]!
}
```

### 3.3 GraphQL преимущества

**GraphQL обеспечивает:**

- Гибкость запросов
- Эффективность (только нужные данные)
- Единую точку входа
- Сильную типизацию

---

## 4. Сравнение стандартов

### 4.1 Сравнительная таблица

| Критерий | REST | SOAP | GraphQL |
|----------|------|------|---------|
| **Формат** | JSON, XML | XML | JSON |
| **Контракт** | Неформальный | Формальный (WSDL) | Schema |
| **Запросы** | Фиксированные endpoints | Фиксированные операции | Гибкие запросы |
| **Over-fetching** | Да | Да | Нет |
| **Кэширование** | HTTP кэш | Ограничено | Сложнее |
| **Сложность** | Низкая | Высокая | Средняя |
| **Использование** | Веб, мобильные | Enterprise | Современные приложения |

### 4.2 Когда использовать

**Используйте REST если:**

- Простые CRUD операции
- Нужна кэшируемость HTTP
- Публичный API
- Простота важнее гибкости

**Используйте SOAP если:**

- Enterprise интеграции
- Нужны формальные контракты
- Требования безопасности (WS-Security)
- Legacy системы

**Используйте GraphQL если:**

- Нужна гибкость запросов
- Важна эффективность данных
- Множественные клиенты с разными требованиями
- Сложные связанные данные

---

## 5. Практические примеры

### 5.1 Пример: RESTful API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Мария", "email": "maria@example.com"}
]

@app.route("/api/users", methods=["GET"])
def get_users():
    """GET /api/users - список пользователей"""
    return jsonify(users), 200

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """GET /api/users/{id} - конкретный пользователь"""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/api/users", methods=["POST"])
def create_user():
    """POST /api/users - создать пользователя"""
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201
```

### 5.2 Пример: GraphQL запрос

```python
# GraphQL позволяет запрашивать только нужные поля

query_simple = """
{
  user(id: 123) {
    name
    email
  }
}
"""

query_complex = """
{
  user(id: 123) {
    name
    orders {
      id
      total
      items {
        name
        quantity
      }
    }
  }
}
```

---

## 6. Common Pitfalls

### 6.1 Pitfall: Нарушение REST принципов

❌ **Incorrect:**
```python
# Плохо: RPC стиль в REST

POST /api/getUser
POST /api/calculateTotal
```

✅ **Correct:**
```python
# Хорошо: REST стиль

GET /api/users/123
POST /api/orders (с total в теле)
```

**Why:** REST фокусируется на ресурсах, а не методах.

### 6.2 Pitfall: Over-fetching в REST

❌ **Incorrect:**
```python
# REST: всегда возвращает все поля

GET /api/users/123
# Возвращает: id, name, email, address, phone, orders, preferences...
# Но клиенту нужен только name
```

✅ **Correct:**
```python
# GraphQL: клиент запрашивает только нужные поля

query {
  user(id: 123) {
    name
  }
}
```

**Why:** GraphQL решает проблему over-fetching, позволяя клиенту выбирать поля.

---

## 💡 Key Takeaways

- **REST как архитектурный стиль**: REST — это не протокол, а набор принципов (ресурсы, HTTP методы, stateless, кэшируемость). Простой и широко используемый стандарт

- **SOAP и WSDL**: SOAP обеспечивает формальные контракты через WSDL, встроенную безопасность и поддержку транзакций. Подходит для enterprise интеграций

- **GraphQL**: GraphQL решает проблему over-fetching и under-fetching, позволяя клиентам запрашивать только нужные данные. Обеспечивает гибкость и эффективность

- **Выбор стандарта**: REST для простых CRUD и публичных API, SOAP для enterprise с формальными контрактами, GraphQL для гибких запросов и эффективности данных

- **Сравнение**: Каждый стандарт имеет свои преимущества. Выбор зависит от требований к гибкости, формальности контрактов, кэшированию и сложности

---

## 🚀 Next Steps

**Related Modules:**

- [07_API_Design](../07_API_Design/) — проектирование REST API
- [10_Contracts_Documentation](../10_Contracts_Documentation/) — контракты и документация
- [13_API_Security](../13_API_Security/) — безопасность API

**Practice Ideas:**

1. Создайте RESTful API для ресурса
2. Изучите WSDL для SOAP сервиса
3. Реализуйте GraphQL API с гибкими запросами

**Going Deeper:**

- REST API Design Best Practices: лучшие практики REST
- GraphQL Specification: полная спецификация GraphQL
- SOAP vs REST: детальное сравнение

---

## 📚 Additional Resources

**Documentation:**

- [REST API Tutorial](https://restfulapi.net/) — руководство по REST
- [GraphQL Documentation](https://graphql.org/) — документация GraphQL
- [SOAP Specification](https://www.w3.org/TR/soap/) — спецификация SOAP

**Articles:**

- "REST vs GraphQL: Which is Better?" — сравнение REST и GraphQL
- "Understanding SOAP and WSDL" — понимание SOAP и WSDL

---



