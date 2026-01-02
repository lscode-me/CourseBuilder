# Типы API
## REST, SOAP, RPC и Event-based API

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции API и интеграции
- Знать основы HTTP протокола (методы, статус-коды, заголовки)
- Иметь представление о клиент-серверной архитектуре

**Recommended prior modules:**

- [01_What_is_API](../01_What_is_API/) — основы API и интеграции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать основные типы API: REST, SOAP, RPC и Event-based
- Выбирать подходящий тип API для конкретной задачи
- Понимать преимущества и ограничения каждого типа
- Применять REST принципы при проектировании API

---

## 1. Введение в типы API

API можно классифицировать по архитектурному стилю и способу взаимодействия. Разные типы API решают разные задачи и имеют свои преимущества.

**Основные типы API:**

- **REST API** — архитектурный стиль на основе HTTP

- **SOAP API** — протокол на основе XML

- **RPC API** — удалённый вызов процедур

- **Event-based API** — событийно-ориентированная архитектура

Каждый тип подходит для определённых сценариев использования.

---

## 2. REST API

**REST (Representational State Transfer)** — это архитектурный стиль для проектирования распределённых систем. REST API использует HTTP методы для работы с ресурсами.

### 2.1 Принципы REST

REST основан на нескольких ключевых принципах:

- **Ресурсы**: Всё является ресурсом, идентифицируемым URI

- **HTTP методы**: GET, POST, PUT, DELETE для операций

- **Stateless**: Каждый запрос содержит всю необходимую информацию

- **Кэшируемость**: Ответы могут кэшироваться

- **Единообразный интерфейс**: Стандартные способы взаимодействия

**Example: Базовый REST API**

```python
# REST API для работы с пользователями

# GET /api/users - получить список пользователей

def get_users():
    """Получить список всех пользователей"""
    return [
        {'id': 1, 'name': 'Иван', 'email': 'ivan@example.com'},
        {'id': 2, 'name': 'Мария', 'email': 'maria@example.com'}
    ]

# GET /api/users/1 - получить конкретного пользователя

def get_user(user_id):
    """Получить пользователя по ID"""
    return {'id': 1, 'name': 'Иван', 'email': 'ivan@example.com'}

# POST /api/users - создать нового пользователя

def create_user(data):
    """Создать нового пользователя"""
    return {'id': 3, 'name': data['name'], 'email': data['email']}

# PUT /api/users/1 - обновить пользователя

def update_user(user_id, data):
    """Обновить данные пользователя"""
    return {'id': user_id, **data}

# DELETE /api/users/1 - удалить пользователя

def delete_user(user_id):
    """Удалить пользователя"""
    return {'status': 'deleted', 'id': user_id}

# Использование

users = get_users()
print(f"Users: {len(users)}")
```

**Output:**
```
Users: 2
```

### 2.2 REST ресурсы и URI

В REST всё является ресурсом. URI идентифицирует ресурс, HTTP метод определяет операцию.

**Example: Структура REST ресурсов**

```python
# Ресурсы в REST API

# Коллекция пользователей

GET    /api/users           # Список всех пользователей
POST   /api/users           # Создать пользователя

# Конкретный пользователь

GET    /api/users/123       # Получить пользователя 123
PUT    /api/users/123       # Обновить пользователя 123
DELETE /api/users/123       # Удалить пользователя 123

# Вложенные ресурсы

GET    /api/users/123/orders        # Заказы пользователя 123
POST   /api/users/123/orders        # Создать заказ для пользователя 123
GET    /api/users/123/orders/456    # Конкретный заказ

# Использование

import requests

# Получить пользователя

response = requests.get('https://api.example.com/users/123')
user = response.json()
print(f"User: {user['name']}")

# Создать заказ

order_data = {'items': [{'id': 1, 'quantity': 2}]}
response = requests.post(
    f'https://api.example.com/users/{user["id"]}/orders',
    json=order_data
)
order = response.json()
print(f"Order created: {order['id']}")
```

**Output:**
```
User: Иван
Order created: 456
```

### 2.3 HTTP методы в REST

Каждый HTTP метод имеет семантическое значение в REST:

| Метод | Операция | Идемпотентность | Безопасность |
|-------|----------|-----------------|--------------|
| GET | Чтение | Да | Да |
| POST | Создание | Нет | Нет |
| PUT | Обновление/Создание | Да | Нет |
| PATCH | Частичное обновление | Нет | Нет |
| DELETE | Удаление | Да | Нет |

**Example: Использование HTTP методов**

```python
import requests

class UserRESTAPI:
    """Клиент для REST API пользователей"""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_user(self, user_id):
        """GET - безопасная операция чтения"""
        response = requests.get(f'{self.base_url}/users/{user_id}')
        return response.json()
    
    def create_user(self, name, email):
        """POST - создание ресурса"""
        data = {'name': name, 'email': email}
        response = requests.post(
            f'{self.base_url}/users',
            json=data
        )
        return response.json()
    
    def update_user(self, user_id, data):
        """PUT - полное обновление (идемпотентно)"""
        response = requests.put(
            f'{self.base_url}/users/{user_id}',
            json=data
        )
        return response.json()
    
    def delete_user(self, user_id):
        """DELETE - удаление (идемпотентно)"""
        response = requests.delete(f'{self.base_url}/users/{user_id}')
        return response.status_code == 204

# Использование

api = UserRESTAPI('https://api.example.com')
user = api.get_user(123)
print(f"Retrieved: {user['name']}")
```

**Output:**
```
Retrieved: Иван
```

> **💡 Pro Tip:**  
> Идемпотентность означает, что повторный вызов операции даёт тот же результат. GET, PUT, DELETE идемпотентны, POST — нет.

### 2.4 Преимущества REST

**REST популярен потому что:**

- **Простота**: Использует стандартные HTTP методы

- **Кэширование**: HTTP кэширование работает из коробки

- **Масштабируемость**: Stateless архитектура легко масштабируется

- **Совместимость**: Работает через стандартные HTTP прокси и балансировщики

- **Гибкость**: Поддерживает различные форматы данных (JSON, XML)

---

## 3. SOAP API

**SOAP (Simple Object Access Protocol)** — это протокол для обмена структурированными сообщениями в распределённых системах. SOAP использует XML и обычно работает поверх HTTP.

### 3.1 Особенности SOAP

SOAP имеет строгую структуру и формализованный контракт:

- **XML формат**: Все сообщения в формате XML

- **WSDL контракт**: Формальное описание API через WSDL

- **Встроенная безопасность**: WS-Security стандарты

- **Транзакции**: Поддержка распределённых транзакций

**Example: SOAP запрос и ответ**

```xml
<!-- SOAP запрос -->
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetUser xmlns="http://example.com/api">
      <UserId>123</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>

<!-- SOAP ответ -->
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetUserResponse xmlns="http://example.com/api">
      <User>
        <Id>123</Id>
        <Name>Иван Иванов</Name>
        <Email>ivan@example.com</Email>
      </User>
    </GetUserResponse>
  </soap:Body>
</soap:Envelope>
```

**Example: Использование SOAP API в Python**

```python
from zeep import Client

# SOAP клиент использует WSDL для понимания API

wsdl_url = 'http://example.com/api?wsdl'
client = Client(wsdl_url)

# Вызов SOAP метода

result = client.service.GetUser(UserId=123)

print(f"User: {result.Name}")
print(f"Email: {result.Email}")
```

**Output:**
```
User: Иван Иванов
Email: ivan@example.com
```

### 3.2 WSDL контракт

**WSDL (Web Services Description Language)** — это XML формат для описания SOAP API. WSDL определяет:

- Доступные операции
- Формат запросов и ответов
- Типы данных
- Endpoint адреса

**Example: Фрагмент WSDL**

```xml
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

### 3.3 Когда использовать SOAP

**SOAP подходит для:**

- Enterprise интеграций с формальными контрактами
- Систем, требующих встроенной безопасности (WS-Security)
- Сценариев с распределёнными транзакциями
- Интеграций с legacy системами

**SOAP НЕ подходит для:**

- Простых CRUD операций
- Мобильных приложений (большой размер сообщений)
- Быстрой разработки прототипов

---

## 4. RPC API

**RPC (Remote Procedure Call)** — это способ вызова функций на удалённом сервере, как если бы они были локальными. RPC API фокусируется на вызове методов, а не на работе с ресурсами.

### 4.1 Концепция RPC

В RPC клиент вызывает удалённую процедуру (функцию) по имени, передавая параметры.

**Example: RPC API**

```python
# RPC API фокусируется на методах, а не ресурсах

# REST подход: работа с ресурсами

GET /api/users/123

# RPC подход: вызов метода

POST /api/rpc
{
  "method": "getUser",
  "params": {"userId": 123}
}

# Пример RPC клиента

import requests

class RPCClient:
    """Клиент для RPC API"""
    
    def __init__(self, endpoint):
        self.endpoint = endpoint
    
    def call(self, method, params=None):
        """Вызов удалённой процедуры"""
        payload = {
            'method': method,
            'params': params or {}
        }
        response = requests.post(self.endpoint, json=payload)
        return response.json()['result']
    
    def get_user(self, user_id):
        """Вызов метода getUser"""
        return self.call('getUser', {'userId': user_id})
    
    def create_user(self, name, email):
        """Вызов метода createUser"""
        return self.call('createUser', {'name': name, 'email': email})

# Использование

client = RPCClient('https://api.example.com/rpc')
user = client.get_user(123)
print(f"User: {user['name']}")
```

**Output:**
```
User: Иван
```

### 4.2 JSON-RPC

**JSON-RPC** — это спецификация RPC, использующая JSON для кодирования вызовов.

**Example: JSON-RPC запрос и ответ**

```python
# JSON-RPC запрос

request = {
    "jsonrpc": "2.0",
    "method": "subtract",
    "params": {"minuend": 42, "subtrahend": 23},
    "id": 1
}

# JSON-RPC ответ

response = {
    "jsonrpc": "2.0",
    "result": 19,
    "id": 1
}

# Обработка ошибки

error_response = {
    "jsonrpc": "2.0",
    "error": {
        "code": -32601,
        "message": "Method not found"
    },
    "id": 1
}

# Реализация JSON-RPC клиента

import requests

def jsonrpc_call(url, method, params=None, request_id=1):
    """Вызов JSON-RPC метода"""
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "id": request_id
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    
    if 'error' in result:
        raise Exception(f"RPC Error: {result['error']['message']}")
    
    return result['result']

# Использование

result = jsonrpc_call(
    'https://api.example.com/jsonrpc',
    'getUser',
    {'userId': 123}
)
print(f"Result: {result}")
```

**Output:**
```
Result: {'id': 123, 'name': 'Иван'}
```

### 4.3 gRPC

**gRPC** — это современная реализация RPC от Google, использующая Protocol Buffers и HTTP/2.

**Example: gRPC определение и использование**

```protobuf
// user.proto - определение gRPC сервиса
syntax = "proto3";

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc CreateUser(CreateUserRequest) returns (User);
}

message GetUserRequest {
  int32 user_id = 1;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

```python
# gRPC клиент в Python

import grpc
from user_pb2 import GetUserRequest, User
from user_pb2_grpc import UserServiceStub

# Создание канала и клиента

channel = grpc.insecure_channel('localhost:50051')
stub = UserServiceStub(channel)

# Вызов метода

request = GetUserRequest(user_id=123)
user = stub.GetUser(request)

print(f"User: {user.name}")
```

**Output:**
```
User: Иван
```

### 4.4 Когда использовать RPC

**RPC подходит для:**

- Вызова конкретных методов/функций
- Микросервисной архитектуры (gRPC)
- Высокопроизводительных систем (gRPC с HTTP/2)
- Систем с чётко определёнными операциями

**RPC НЕ подходит для:**

- Простых CRUD операций (REST проще)
- Публичных API (REST более понятен)
- Систем, где важна кэшируемость HTTP

---

## 5. Event-based API

**Event-based API** — это архитектура, где системы взаимодействуют через события. Вместо запросов-ответов система публикует события, а другие системы подписываются на них.

### 5.1 Концепция событий

В event-based архитектуре система публикует события, когда происходит что-то важное. Другие системы подписываются на интересующие их события.

**Example: Event-based взаимодействие**

```python
# Event-based API использует события вместо запросов

class EventPublisher:
    """Публикатор событий"""
    
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_type, callback):
        """Подписка на событие"""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
    
    def publish(self, event_type, data):
        """Публикация события"""
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)
    
    def user_created(self, user_data):
        """Публикация события создания пользователя"""
        self.publish('user.created', user_data)
    
    def order_placed(self, order_data):
        """Публикация события размещения заказа"""
        self.publish('order.placed', order_data)

# Использование

publisher = EventPublisher()

# Подписка на события

def handle_user_created(data):
    print(f"New user created: {data['name']}")

def handle_order_placed(data):
    print(f"New order placed: {data['id']}")

publisher.subscribe('user.created', handle_user_created)
publisher.subscribe('order.placed', handle_order_placed)

# Публикация событий

publisher.user_created({'id': 123, 'name': 'Иван'})
publisher.order_placed({'id': 456, 'total': 100.0})
```

**Output:**
```
New user created: Иван
New order placed: 456
```

### 5.2 Webhooks

**Webhooks** — это способ доставки событий через HTTP POST запросы. Сервер отправляет событие на URL, указанный клиентом.

**Example: Webhook реализация**

```python
import requests
from flask import Flask, request

app = Flask(__name__)

class WebhookPublisher:
    """Публикатор webhooks"""
    
    def __init__(self):
        self.webhooks = {}  # event_type -> [urls]
    
    def register_webhook(self, event_type, url):
        """Регистрация webhook URL для события"""
        if event_type not in self.webhooks:
            self.webhooks[event_type] = []
        self.webhooks[event_type].append(url)
    
    def trigger_webhook(self, event_type, data):
        """Отправка webhook"""
        if event_type in self.webhooks:
            for url in self.webhooks[event_type]:
                try:
                    requests.post(url, json={
                        'event': event_type,
                        'data': data,
                        'timestamp': '2024-01-15T10:30:00Z'
                    })
                except Exception as e:
                    print(f"Failed to send webhook to {url}: {e}")

# Webhook endpoint для получения событий

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    """Обработчик входящих webhooks"""
    event = request.json
    print(f"Received event: {event['event']}")
    print(f"Data: {event['data']}")
    return {'status': 'ok'}, 200

# Использование

publisher = WebhookPublisher()
publisher.register_webhook('user.created', 'http://client.example.com/webhook')

# При создании пользователя отправляется webhook

publisher.trigger_webhook('user.created', {
    'id': 123,
    'name': 'Иван',
    'email': 'ivan@example.com'
})
```

**Output:**
```
Received event: user.created
Data: {'id': 123, 'name': 'Иван', 'email': 'ivan@example.com'}
```

### 5.3 Message Queues

**Message Queues** используются для надёжной доставки событий между системами.

**Example: Использование message queue**

```python
# Event-based API через message queue (например, RabbitMQ)

import pika

class EventQueue:
    """Очередь событий"""
    
    def __init__(self, connection_string):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(connection_string)
        )
        self.channel = self.connection.channel()
    
    def publish_event(self, event_type, data):
        """Публикация события в очередь"""
        self.channel.exchange_declare(
            exchange='events',
            exchange_type='topic'
        )
        
        self.channel.basic_publish(
            exchange='events',
            routing_key=event_type,
            body=json.dumps(data)
        )
        print(f"Published event: {event_type}")
    
    def subscribe(self, event_type, callback):
        """Подписка на события"""
        queue_name = f'queue_{event_type}'
        self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(
            exchange='events',
            queue=queue_name,
            routing_key=event_type
        )
        
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )
    
    def start_consuming(self):
        """Начать обработку событий"""
        self.channel.start_consuming()

# Использование

queue = EventQueue('amqp://localhost')

# Публикация события

queue.publish_event('user.created', {
    'id': 123,
    'name': 'Иван'
})

# Подписка на события

def handle_user_created(ch, method, properties, body):
    data = json.loads(body)
    print(f"User created: {data['name']}")

queue.subscribe('user.created', handle_user_created)
```

### 5.4 Когда использовать Event-based API

**Event-based API подходит для:**

- Асинхронной обработки событий
- Систем, где источник события не знает о получателях
- Сценариев с множественными подписчиками
- Decoupled архитектуры

**Event-based API НЕ подходит для:**

- Синхронных операций, требующих немедленного ответа
- Простых CRUD операций
- Систем, где важна гарантия доставки в реальном времени

---

## 6. Сравнение типов API

### 6.1 Сравнительная таблица

| Критерий | REST | SOAP | RPC | Event-based |
|----------|------|------|-----|-------------|
| **Формат данных** | JSON, XML | XML | JSON, Binary | JSON, Binary |
| **Протокол** | HTTP | HTTP, SMTP | HTTP, TCP | HTTP, Message Queue |
| **Сложность** | Низкая | Высокая | Средняя | Средняя |
| **Кэширование** | Да | Ограничено | Нет | Нет |
| **Типизация** | Слабая | Строгая (WSDL) | Зависит | Зависит |
| **Производительность** | Хорошая | Средняя | Высокая (gRPC) | Высокая |
| **Использование** | Публичные API | Enterprise | Микросервисы | Асинхронные системы |

### 6.2 Выбор типа API

**Выбирайте REST если:**

- Нужен простой, понятный API
- Важна кэшируемость
- Публичный API для веб/мобильных приложений
- CRUD операции с ресурсами

**Выбирайте SOAP если:**

- Enterprise интеграция с формальными контрактами
- Требуется встроенная безопасность (WS-Security)
- Работа с legacy системами
- Распределённые транзакции

**Выбирайте RPC если:**

- Вызов конкретных методов/функций
- Микросервисная архитектура (gRPC)
- Высокая производительность важна
- Чётко определённые операции

**Выбирайте Event-based если:**

- Асинхронная обработка событий
- Decoupled архитектура
- Множественные подписчики на события
- Реактивные системы

---

## 7. Практические примеры

### 7.1 Пример: REST API для блога

```python
# REST API для блога

from flask import Flask, request, jsonify

app = Flask(__name__)

posts = [
    {'id': 1, 'title': 'First Post', 'content': 'Content...'},
    {'id': 2, 'title': 'Second Post', 'content': 'Content...'}
]

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """GET /api/posts - список постов"""
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """GET /api/posts/1 - конкретный пост"""
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
    """POST /api/posts - создать пост"""
    data = request.json
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content']
    }
    posts.append(new_post)
    return jsonify(new_post), 201

# REST использует ресурсы и HTTP методы
```

### 7.2 Пример: RPC API для вычислений

```python
# RPC API для математических операций

class MathRPCService:
    """RPC сервис для математических операций"""
    
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def calculate(self, operation, *args):
        """Вызов метода по имени"""
        method = getattr(self, operation, None)
        if method:
            return method(*args)
        raise ValueError(f"Unknown operation: {operation}")

# Использование

service = MathRPCService()
result = service.calculate('add', 5, 3)
print(f"5 + 3 = {result}")
```

**Output:**
```
5 + 3 = 8
```

---

## 8. Common Pitfalls

### 8.1 Pitfall: Смешивание REST и RPC

❌ **Incorrect:**
```python
# Плохо: REST endpoint, но RPC семантика

POST /api/getUser
{
  "userId": 123
}
```

✅ **Correct:**
```python
# Хорошо: REST подход

GET /api/users/123

# Или RPC подход

POST /api/rpc
{
  "method": "getUser",
  "params": {"userId": 123}
}
```

**Why:** REST фокусируется на ресурсах, RPC на методах. Смешивание создаёт путаницу.

### 8.2 Pitfall: Игнорирование REST принципов

❌ **Incorrect:**
```python
# Плохо: POST для получения данных

POST /api/getUsers
```

✅ **Correct:**
```python
# Хорошо: GET для получения данных

GET /api/users
```

**Why:** HTTP методы имеют семантическое значение. GET для чтения, POST для создания.

### 8.3 Pitfall: Неправильный выбор типа API

❌ **Incorrect:**
```python
# Использование SOAP для простого CRUD API
# Избыточная сложность для простой задачи
```

✅ **Correct:**
```python
# REST для простого CRUD API

GET /api/users
POST /api/users
PUT /api/users/123
DELETE /api/users/123
```

**Why:** Выбор типа API должен соответствовать задаче. REST проще для CRUD, SOAP для сложных enterprise интеграций.

---

## 💡 Key Takeaways

- **REST API**: Архитектурный стиль на основе HTTP, фокусируется на ресурсах. Простой, кэшируемый, подходит для большинства публичных API

- **SOAP API**: Формальный протокол на XML с WSDL контрактами. Подходит для enterprise интеграций с требованиями безопасности

- **RPC API**: Удалённый вызов процедур, фокусируется на методах. gRPC обеспечивает высокую производительность для микросервисов

- **Event-based API**: Событийно-ориентированная архитектура через события, webhooks или message queues. Подходит для асинхронных, decoupled систем

- **Выбор типа API**: Зависит от требований. REST для простых CRUD, SOAP для enterprise, RPC для микросервисов, Event-based для асинхронных систем

---

## 🚀 Next Steps

**Related Modules:**

- [03_Sync_Async_API](../03_Sync_Async_API/) — синхронные и асинхронные API, webhooks, очереди
- [06_API_Standards](../06_API_Standards/) — детальное изучение REST, SOAP, GraphQL стандартов
- [07_API_Design](../07_API_Design/) — проектирование REST API

**Practice Ideas:**

1. Создайте простой REST API для работы с ресурсами (например, задачи или заметки)
2. Реализуйте RPC API для набора математических операций
3. Создайте event-based систему с публикацией и подпиской на события

**Going Deeper:**

- RESTful API Design: углублённое изучение REST принципов
- gRPC и Protocol Buffers: современный подход к RPC
- Event Sourcing: паттерн хранения событий вместо состояния

---

## 📚 Additional Resources

**Documentation:**

- [REST API Tutorial](https://restfulapi.net/) — полное руководство по REST
- [JSON-RPC Specification](https://www.jsonrpc.org/) — спецификация JSON-RPC
- [gRPC Documentation](https://grpc.io/docs/) — документация gRPC

**Articles:**

- "REST vs SOAP: Choosing the Right Web Service" — сравнение REST и SOAP
- "Understanding Event-Driven Architecture" — понимание событийно-ориентированной архитектуры

---




