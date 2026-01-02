# API как протокол
## REST, RPC, gRPC, GraphQL. Контракты, версии, ошибки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP протокол (модуль 07)
- Иметь опыт работы с API
- Понимать концепцию клиент-серверной модели

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать REST, RPC, gRPC и GraphQL и выбирать подходящий стиль API
- Проектировать API контракты с учётом версионирования и обратной совместимости
- Обрабатывать ошибки в API согласно best practices
- Понимать компромиссы между различными стилями API

---

## 1. Введение: API как протокол

**API (Application Programming Interface)** — это протокол взаимодействия между приложениями. API определяет:
- Какие операции доступны
- Как их вызывать (формат запросов)
- Что ожидать в ответ (формат ответов)
- Как обрабатывать ошибки

В этом модуле мы рассмотрим основные стили API:

1. **REST** — ресурсо-ориентированный стиль
2. **RPC** — вызов удалённых процедур
3. **gRPC** — современный RPC от Google
4. **GraphQL** — язык запросов для API

---

## 2. REST (Representational State Transfer)

### 2.1 Принципы REST

**REST** — архитектурный стиль, основанный на ресурсах и HTTP методах.

**Ключевые принципы:**

1. **Ресурсы**: все — это ресурсы с уникальными URI
2. **HTTP методы**: GET, POST, PUT, DELETE для CRUD операций
3. **Без состояния**: каждый запрос содержит всю необходимую информацию
4. **Представления**: ресурсы имеют различные представления (JSON, XML)

### 2.2 REST API структура

**Ресурсы как URI:**
```
GET    /api/users          — получить список пользователей
GET    /api/users/123      — получить пользователя 123
POST   /api/users          — создать пользователя
PUT    /api/users/123      — обновить пользователя 123
DELETE /api/users/123      — удалить пользователя 123
```

**Вложенные ресурсы:**
```
GET /api/users/123/posts        — посты пользователя 123
GET /api/users/123/posts/456    — пост 456 пользователя 123
```

### 2.3 Пример REST API

**Запрос:**
```
GET /api/users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer token123
```

**Ответ:**
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:00:00Z"
}
```

### 2.4 REST уровни зрелости (Richardson Maturity Model)

**Level 0:** Один URI, один метод (обычно POST)
**Level 1:** Множество URI для разных ресурсов
**Level 2:** HTTP методы используются правильно
**Level 3:** HATEOAS — гиперссылки в ответах

---

## 3. RPC (Remote Procedure Call)

### 3.1 Концепция RPC

**RPC** — вызов процедур/функций на удалённом сервере как будто они локальные.

**Характеристики:**

- Ориентирован на действия, а не на ресурсы
- Клиент вызывает метод с параметрами
- Сервер выполняет и возвращает результат

### 3.2 JSON-RPC

**Структура запроса:**
```json
{
  "jsonrpc": "2.0",
  "method": "getUserById",
  "params": {"id": 123},
  "id": 1
}
```

**Структура ответа:**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "id": 1
}
```

**Ошибка:**
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32600,
    "message": "Invalid Request"
  },
  "id": 1
}
```

### 3.3 XML-RPC

**Запрос:**
```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>getUserById</methodName>
  <params>
    <param><value><int>123</int></value></param>
  </params>
</methodCall>
```

---

## 4. gRPC

### 4.1 Что такое gRPC

**gRPC** — современный RPC фреймворк от Google, использующий Protocol Buffers.

**Характеристики:**

- Бинарный протокол (Protocol Buffers)
- HTTP/2 (мультиплексирование, streaming)
- Кодогенерация клиентов и серверов
- Высокая производительность

### 4.2 Protocol Buffers определение

```protobuf
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}

message GetUserRequest {
  int32 id = 1;
}

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(Empty) returns (stream User);
}
```

### 4.3 Типы gRPC вызовов

**Unary RPC:** один запрос → один ответ

```
Client: GetUser(id=123)
Server: User{id=123, name="John"}
```

**Server streaming:** один запрос → поток ответов

```
Client: ListUsers()
Server: User{id=1, name="Alice"}
Server: User{id=2, name="Bob"}
Server: User{id=3, name="Charlie"}
```

**Client streaming:** поток запросов → один ответ
**Bidirectional streaming:** поток запросов ↔ поток ответов

### 4.4 Преимущества gRPC

- **Производительность**: бинарный формат, HTTP/2

- **Типизация**: строгая типизация через protobuf

- **Кодогенерация**: автоматическая генерация клиентов

- **Streaming**: поддержка streaming из коробки

---

## 5. GraphQL

### 5.1 Что такое GraphQL

**GraphQL** — язык запросов для API, разработанный Facebook.

**Характеристики:**

- Клиент запрашивает только нужные данные
- Один endpoint для всех запросов
- Строгая типизация через схему
- Introspection

### 5.2 GraphQL схема

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

type Query {
  user(id: ID!): User
  users: [User!]!
  post(id: ID!): Post
}

type Mutation {
  createUser(name: String!, email: String!): User!
  updateUser(id: ID!, name: String, email: String): User!
  deleteUser(id: ID!): Boolean!
}
```

### 5.3 GraphQL запрос

**Запрос:**
```graphql
query {
  user(id: "123") {
    id
    name
    email
    posts {
      id
      title
    }
  }
}
```

**Ответ:**
```json
{
  "data": {
    "user": {
      "id": "123",
      "name": "John Doe",
      "email": "john@example.com",
      "posts": [
        {"id": "1", "title": "First Post"},
        {"id": "2", "title": "Second Post"}
      ]
    }
  }
}
```

### 5.4 Мутации

```graphql
mutation {
  createUser(name: "Alice", email: "alice@example.com") {
    id
    name
    email
  }
}
```

### 5.5 Преимущества GraphQL

- **Гибкость**: клиент получает только нужные данные

- **Один endpoint**: не нужно много REST endpoints

- **Типизация**: строгая схема

- **Introspection**: API самодокументируемо

**Недостатки:**

- Сложность: требует больше настроек
- Кэширование: сложнее, чем в REST
- N+1 проблема: нужно решать через DataLoader

---

## 6. Сравнение стилей API

| Характеристика | REST | RPC | gRPC | GraphQL |
|----------------|------|-----|------|---------|
| Ориентация | Ресурсы | Действия | Действия | Запросы |
| Транспорт | HTTP | HTTP | HTTP/2 | HTTP |
| Формат | JSON, XML | JSON, XML | Protobuf | JSON |
| Типизация | Слабая | Слабая | Строгая | Строгая |
| Производительность | Средняя | Средняя | Высокая | Средняя |
| Streaming | Нет | Нет | Да | Subscriptions |
| Кэширование | HTTP cache | Сложно | Сложно | Сложно |
| Use case | CRUD | Операции | Микросервисы | Сложные запросы |

---

## 7. API контракты

### 7.1 Что такое контракт

**API контракт** — формальное определение того, что API принимает и возвращает.

**Инструменты:**

- **OpenAPI (Swagger)** для REST

- **Protocol Buffers** для gRPC

- **GraphQL Schema** для GraphQL

### 7.2 OpenAPI пример

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0

paths:
  /users/{id}:
    get:
      summary: Get user by ID
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
        '404':
          description: User not found

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
```

---

## 8. Версионирование API

### 8.1 Зачем версионировать

**Причины:**

- Изменения могут сломать клиентов
- Нужна обратная совместимость
- Постепенная миграция клиентов

### 8.2 Стратегии версионирования

**URL версионирование:**
```
/api/v1/users
/api/v2/users
```

**Header версионирование:**
```
GET /api/users
Accept: application/vnd.myapi.v2+json
```

**Query параметр:**
```
/api/users?version=2
```

**Content negotiation:**
```
GET /api/users
Accept: application/json; version=2
```

### 8.3 Обратная совместимость

**Правила:**

- Не удаляйте поля (deprecated, но сохраняйте)
- Добавление полей безопасно (клиенты игнорируют)
- Не меняйте типы полей
- Не меняйте семантику операций

---

## 9. Обработка ошибок

### 9.1 HTTP статус-коды

**REST best practices:**

- 200 OK — успех
- 201 Created — ресурс создан
- 400 Bad Request — некорректный запрос
- 401 Unauthorized — требуется авторизация
- 403 Forbidden — доступ запрещён
- 404 Not Found — ресурс не найден
- 409 Conflict — конфликт (например, дубликат)
- 422 Unprocessable Entity — валидация не прошла
- 500 Internal Server Error — ошибка сервера

### 9.2 Структура ошибки

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with id 123 not found",
    "details": {
      "user_id": 123
    }
  }
}
```

### 9.3 gRPC статус-коды

- OK — успех
- CANCELLED — операция отменена
- INVALID_ARGUMENT — некорректные аргументы
- NOT_FOUND — не найдено
- PERMISSION_DENIED — доступ запрещён
- UNAUTHENTICATED — требуется авторизация
- INTERNAL — внутренняя ошибка

### 9.4 GraphQL ошибки

```json
{
  "data": null,
  "errors": [
    {
      "message": "User not found",
      "locations": [{"line": 2, "column": 3}],
      "path": ["user"],
      "extensions": {
        "code": "USER_NOT_FOUND",
        "userId": "123"
      }
    }
  ]
}
```

---

## 💡 Key Takeaways

- **REST для CRUD, RPC для операций**: REST ориентирован на ресурсы, RPC на действия. Выбор зависит от доменной модели.

- **gRPC для производительности, GraphQL для гибкости**: gRPC оптимизирован для скорости через бинарный формат, GraphQL даёт клиентам контроль над данными.

- **API контракт критичен**: Формализация API через OpenAPI, Protobuf или GraphQL схему обеспечивает понятность и проверяемость.

- **Версионирование и обратная совместимость**: Изменения API неизбежны. Версионирование и правила совместимости позволяют эволюционировать без поломки клиентов.

- **Стандартная обработка ошибок**: Используйте HTTP статус-коды, структурированные ошибки и понятные сообщения для упрощения отладки.

---

## 🚀 Next Steps

**Related Modules:**

- [09_Library_Runtime_Protocols](../09_Library_Runtime_Protocols/) — библиотечные протоколы: file-like, iterator, context manager
- [18_Good_Vs_Bad_Protocols](../18_Good_Vs_Bad_Protocols/) — хороший vs плохой протокол: принципы дизайна

**Practice Ideas:**

1. Создайте REST API с OpenAPI спецификацией
2. Реализуйте простой gRPC сервис с Protocol Buffers
3. Спроектируйте GraphQL схему для вашего домена

**Going Deeper:**

- Изучите HATEOAS для понимания REST Level 3
- Изучите gRPC interceptors для cross-cutting concerns
- Изучите GraphQL federation для микросервисной архитектуры

---


