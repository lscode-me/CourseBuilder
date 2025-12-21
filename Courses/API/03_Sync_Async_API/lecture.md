# Синхронные и асинхронные API
## Request-Response, асинхронные вызовы, Webhooks и очереди сообщений

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы API и интеграции
- Знать типы API (REST, RPC, Event-based)
- Иметь представление о HTTP протоколе

**Recommended prior modules:**

- [01_What_is_API](../01_What_is_API/) — основы API и интеграции
- [02_Types_of_API](../02_Types_of_API/) — типы API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать синхронные и асинхронные API
- Применять паттерн Request-Response для синхронных операций
- Реализовывать асинхронные вызовы через callbacks и promises
- Использовать webhooks для доставки событий
- Применять очереди сообщений для надёжной асинхронной коммуникации

---

## 1. Синхронные vs асинхронные API

Различие между синхронными и асинхронными API определяется тем, блокирует ли клиент выполнение, ожидая ответа.

### 1.1 Синхронные API

**Синхронный API** блокирует клиента до получения ответа. Клиент ждёт, пока сервер обработает запрос и вернёт результат.

**Example: Синхронный API вызов**

```python

import requests
import time

def sync_api_call():
    """Синхронный вызов API - клиент блокируется"""
    print("Отправка запроса...")
    start_time = time.time()
    
    # Блокирующий вызов - клиент ждёт ответа
    response = requests.get('https://api.example.com/users/123')
    
    elapsed = time.time() - start_time
    print(f"Получен ответ за {elapsed:.2f} секунд")
    return response.json()

# Клиент блокируется на время обработки
result = sync_api_call()
print(f"User: {result['name']}")
```

**Output:**
```

Отправка запроса...
Получен ответ за 0.45 секунд
User: Иван
```

**Характеристики синхронных API:**

- Простота использования
- Прямой контроль потока выполнения
- Блокирует выполнение до получения ответа
- Подходит для операций, требующих немедленного результата

### 1.2 Асинхронные API

**Асинхронный API** не блокирует клиента. Клиент отправляет запрос и продолжает работу, получая ответ позже через callback, promise или другой механизм.

**Example: Асинхронный API вызов**

```python

import asyncio
import aiohttp

async def async_api_call():
    """Асинхронный вызов API - клиент не блокируется"""
    print("Отправка запроса...")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # Неблокирующий вызов
        async with session.get('https://api.example.com/users/123') as response:
            result = await response.json()
    
    elapsed = time.time() - start_time
    print(f"Получен ответ за {elapsed:.2f} секунд")
    return result

# Клиент может делать другую работу параллельно
async def main():
    # Можно запустить несколько запросов параллельно
    tasks = [
        async_api_call(),
        async_api_call(),
        async_api_call()
    ]
    results = await asyncio.gather(*tasks)
    return results

# Асинхронное выполнение
results = asyncio.run(main())
print(f"Выполнено {len(results)} запросов параллельно")
```

**Output:**
```

Отправка запроса...
Отправка запроса...
Отправка запроса...
Получен ответ за 0.48 секунд
Получен ответ за 0.49 секунд
Получен ответ за 0.50 секунд
Выполнено 3 запросов параллельно
```

**Характеристики асинхронных API:**

- Не блокирует выполнение
- Позволяет параллельную обработку
- Более эффективное использование ресурсов
- Подходит для операций, не требующих немедленного результата

### 1.3 Когда использовать синхронные vs асинхронные

| Критерий | Синхронные | Асинхронные |
|----------|------------|-------------|
| **Простота** | Проще | Сложнее |
| **Производительность** | Меньше параллелизма | Больше параллелизма |
| **Использование** | Немедленный результат нужен | Результат может прийти позже |
| **Ресурсы** | Блокирует поток | Эффективное использование |

---

## 2. Request-Response паттерн

**Request-Response** — это синхронный паттерн, где клиент отправляет запрос и ждёт ответа.

### 2.1 Базовый Request-Response

**Example: Классический Request-Response**

```python

import requests

class RequestResponseAPI:
    """API с паттерном Request-Response"""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_user(self, user_id):
        """Request: GET /users/{id}, Response: User data"""
        response = requests.get(f'{self.base_url}/users/{user_id}')
        response.raise_for_status()
        return response.json()
    
    def create_user(self, name, email):
        """Request: POST /users, Response: Created user"""
        data = {'name': name, 'email': email}
        response = requests.post(
            f'{self.base_url}/users',
            json=data
        )
        response.raise_for_status()
        return response.json()

# Использование
api = RequestResponseAPI('https://api.example.com')

# Синхронный вызов - ждём ответа
user = api.get_user(123)
print(f"User: {user['name']}")

# Создание пользователя - ждём подтверждения

new_user = api.create_user('Мария', 'maria@example.com')
print(f"Created: {new_user['id']}")
```

**Output:**
```

User: Иван
Created: 456
```

### 2.2 Timeout и обработка ошибок

**Example: Request-Response с timeout и обработкой ошибок**

```python

import requests
from requests.exceptions import Timeout, RequestException

def robust_request_response(url, timeout=5, retries=3):
    """Request-Response с обработкой ошибок"""
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except Timeout:
            print(f"Timeout на попытке {attempt + 1}")
            if attempt == retries - 1:
                raise
        except RequestException as e:
            print(f"Ошибка запроса: {e}")
            raise
    
    return None

# Использование с обработкой ошибок
try:
    result = robust_request_response('https://api.example.com/users/123')
    print(f"Success: {result}")
except Exception as e:
    print(f"Failed: {e}")
```

---

## 3. Асинхронные вызовы

Асинхронные вызовы позволяют клиенту не блокироваться, ожидая ответа.

### 3.1 Callbacks

**Callback** — это функция, которая вызывается, когда асинхронная операция завершается.

**Example: Асинхронный вызов с callback**

```python

import threading
import time

def async_api_call_with_callback(url, callback):
    """Асинхронный вызов с callback"""
    def fetch():
        # Симуляция асинхронного запроса
        time.sleep(1)  # Имитация сетевой задержки
        result = {'id': 123, 'name': 'Иван'}
        callback(result)
    
    # Запуск в отдельном потоке
    thread = threading.Thread(target=fetch)
    thread.start()
    return thread

# Callback функция
def handle_response(data):
    print(f"Получен ответ: {data['name']}")

# Асинхронный вызов
print("Отправка запроса...")
thread = async_api_call_with_callback(
    'https://api.example.com/users/123',
    handle_response
)

# Клиент может продолжать работу
print("Продолжаем работу...")
time.sleep(0.5)
print("Делаем что-то ещё...")

# Ждём завершения

thread.join()
```

**Output:**
```

Отправка запроса...
Продолжаем работу...
Делаем что-то ещё...
Получен ответ: Иван
```

### 3.2 Promises/Futures

**Promise (Future)** — это объект, представляющий результат асинхронной операции, который будет доступен в будущем.

**Example: Асинхронный вызов с Promise**

```python

import asyncio
import aiohttp

async def fetch_user(user_id):
    """Асинхронный запрос пользователя"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.example.com/users/{user_id}') as response:
            return await response.json()

async def main():
    """Использование Promise (Future)"""
    # Создание Future (Promise)
    task1 = asyncio.create_task(fetch_user(123))
    task2 = asyncio.create_task(fetch_user(456))
    task3 = asyncio.create_task(fetch_user(789))
    
    # Продолжаем работу, не ожидая результатов
    print("Запросы отправлены, продолжаем работу...")
    
    # Получаем результаты, когда они готовы
    user1 = await task1
    user2 = await task2
    user3 = await task3
    
    print(f"Users: {user1['name']}, {user2['name']}, {user3['name']}")

# Выполнение

asyncio.run(main())
```

**Output:**
```

Запросы отправлены, продолжаем работу...
Users: Иван, Мария, Петр
```

### 3.3 Polling для асинхронных операций

Когда операция долгая, клиент может периодически проверять статус (polling).

**Example: Polling статуса операции**

```python

import time
import requests

def start_long_operation():
    """Запуск долгой операции"""
    response = requests.post('https://api.example.com/tasks', json={
        'type': 'process_data',
        'data': 'large dataset'
    })
    return response.json()['task_id']

def poll_task_status(task_id, interval=2, max_attempts=30):
    """Polling статуса задачи"""
    for attempt in range(max_attempts):
        response = requests.get(f'https://api.example.com/tasks/{task_id}')
        status = response.json()['status']
        
        if status == 'completed':
            return response.json()['result']
        elif status == 'failed':
            raise Exception("Task failed")
        
        print(f"Статус: {status}, попытка {attempt + 1}")
        time.sleep(interval)
    
    raise TimeoutError("Task timeout")

# Использование
task_id = start_long_operation()
print(f"Задача создана: {task_id}")

# Polling статуса

result = poll_task_status(task_id)
print(f"Результат: {result}")
```

---

## 4. Webhooks

**Webhooks** — это способ доставки событий от сервера к клиенту через HTTP POST запросы.

### 4.1 Концепция Webhooks

Вместо того, чтобы клиент постоянно опрашивал сервер (polling), сервер отправляет события клиенту на указанный URL.

**Example: Регистрация и обработка webhook**

```python

from flask import Flask, request, jsonify

app = Flask(__name__)

class WebhookAPI:
    """API с поддержкой webhooks"""
    
    def __init__(self):
        self.webhooks = {}  # event_type -> [urls]
    
    def register_webhook(self, event_type, url, secret=None):
        """Регистрация webhook URL"""
        if event_type not in self.webhooks:
            self.webhooks[event_type] = []
        
        self.webhooks[event_type].append({
            'url': url,
            'secret': secret
        })
        print(f"Webhook зарегистрирован: {event_type} -> {url}")
    
    def trigger_webhook(self, event_type, data):
        """Отправка webhook"""
        if event_type in self.webhooks:
            for webhook in self.webhooks[event_type]:
                self._send_webhook(webhook['url'], event_type, data, webhook.get('secret'))
    
    def _send_webhook(self, url, event_type, data, secret=None):
        """Отправка HTTP POST запроса"""
        import requests
        
        payload = {
            'event': event_type,
            'data': data,
            'timestamp': '2024-01-15T10:30:00Z'
        }
        
        headers = {'Content-Type': 'application/json'}
        if secret:
            # Подпись webhook для безопасности
            import hmac
            signature = hmac.new(
                secret.encode(),
                json.dumps(payload).encode(),
                'sha256'
            ).hexdigest()
            headers['X-Webhook-Signature'] = signature
        
        try:
            requests.post(url, json=payload, headers=headers, timeout=5)
            print(f"Webhook отправлен: {event_type} -> {url}")
        except Exception as e:
            print(f"Ошибка отправки webhook: {e}")

# Webhook endpoint на стороне клиента
@app.route('/webhook', methods=['POST'])
def webhook_handler():
    """Обработчик входящих webhooks"""
    event = request.json
    print(f"Получен webhook: {event['event']}")
    print(f"Данные: {event['data']}")
    return jsonify({'status': 'ok'}), 200

# Использование
api = WebhookAPI()
api.register_webhook('user.created', 'http://client.example.com/webhook')

# При создании пользователя отправляется webhook
api.trigger_webhook('user.created', {
    'id': 123,
    'name': 'Иван',
    'email': 'ivan@example.com'
})
```

**Output:**
```

Webhook зарегистрирован: user.created -> http://client.example.com/webhook
Webhook отправлен: user.created -> http://client.example.com/webhook
Получен webhook: user.created
Данные: {'id': 123, 'name': 'Иван', 'email': 'ivan@example.com'}
```

### 4.2 Webhook безопасность

**Example: Верификация webhook подписи**

```python

import hmac
import hashlib

def verify_webhook_signature(payload, signature, secret):
    """Верификация подписи webhook"""
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_signature, signature)

# На стороне клиента
@app.route('/webhook', methods=['POST'])
def secure_webhook_handler():
    """Безопасный обработчик webhook"""
    signature = request.headers.get('X-Webhook-Signature')
    secret = 'your-webhook-secret'
    
    if not verify_webhook_signature(
        request.data.decode(),
        signature,
        secret
    ):
        return jsonify({'error': 'Invalid signature'}), 401
    
    # Обработка webhook
    event = request.json
    process_event(event)
    return jsonify({'status': 'ok'}), 200
```

---

## 5. Очереди сообщений

**Message Queues** обеспечивают надёжную асинхронную доставку сообщений между системами.

### 5.1 Концепция очередей

Очередь сообщений позволяет отправителю и получателю работать независимо, не зная друг о друге.

**Example: Использование очереди сообщений**

```python

import json
import pika

class MessageQueueAPI:
    """API с использованием очереди сообщений"""
    
    def __init__(self, connection_string):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(connection_string)
        )
        self.channel = self.connection.channel()
    
    def publish_event(self, event_type, data, exchange='events'):
        """Публикация события в очередь"""
        self.channel.exchange_declare(exchange=exchange, exchange_type='topic')
        
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=event_type,
            body=json.dumps(data),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Сохранять сообщения на диск
            )
        )
        print(f"Событие опубликовано: {event_type}")
    
    def subscribe(self, event_type, callback, queue_name=None):
        """Подписка на события"""
        if queue_name is None:
            queue_name = f'queue_{event_type}'
        
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.queue_bind(
            exchange='events',
            queue=queue_name,
            routing_key=event_type
        )
        
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=False  # Подтверждение после обработки
        )
    
    def start_consuming(self):
        """Начать обработку сообщений"""
        print("Ожидание сообщений...")
        self.channel.start_consuming()

# Публикация события
queue = MessageQueueAPI('amqp://localhost')
queue.publish_event('user.created', {
    'id': 123,
    'name': 'Иван',
    'email': 'ivan@example.com'
})

# Подписка на события
def handle_user_created(ch, method, properties, body):
    data = json.loads(body)
    print(f"Обработка события: user.created")
    print(f"Данные: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

queue.subscribe('user.created', handle_user_created)
```

### 5.2 Преимущества очередей

**Очереди сообщений обеспечивают:**

- **Надёжность**: Сообщения сохраняются и не теряются

- **Масштабируемость**: Можно добавить больше обработчиков

- **Decoupling**: Отправитель и получатель не знают друг о друге

- **Обработка пиков**: Очередь буферизует нагрузку

---

## 6. Сравнение подходов

### 6.1 Сравнительная таблица

| Подход | Синхронность | Надёжность | Сложность | Использование |
|--------|--------------|------------|-----------|---------------|
| **Request-Response** | Синхронный | Средняя | Низкая | Немедленный результат нужен |
| **Callbacks** | Асинхронный | Низкая | Средняя | Простые асинхронные операции |
| **Promises/Futures** | Асинхронный | Средняя | Средняя | Современные асинхронные приложения |
| **Webhooks** | Асинхронный | Средняя | Средняя | События от сервера к клиенту |
| **Message Queues** | Асинхронный | Высокая | Высокая | Критичные асинхронные операции |

### 6.2 Выбор подхода

**Используйте Request-Response если:**

- Нужен немедленный результат
- Операция быстрая (< 1 секунды)
- Простота важнее производительности

**Используйте асинхронные вызовы если:**

- Операция может занять время
- Нужна параллельная обработка
- Эффективность использования ресурсов важна

**Используйте Webhooks если:**

- Сервер должен уведомлять клиента о событиях
- Избегаете постоянного polling
- События происходят нечасто

**Используйте Message Queues если:**

- Критична надёжность доставки
- Нужна обработка пиков нагрузки
- Множественные получатели

---

## 7. Common Pitfalls

### 7.1 Pitfall: Блокирующие вызовы в асинхронном коде

❌ **Incorrect:**
```python

async def bad_async():
    # Блокирующий вызов в async функции
    result = requests.get('https://api.example.com/data')
    return result.json()
```

✅ **Correct:**
```python

async def good_async():
    # Неблокирующий async вызов
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com/data') as response:
            return await response.json()
```

**Why:** Блокирующие вызовы в async функции блокируют весь event loop.

### 7.2 Pitfall: Отсутствие обработки ошибок в webhooks

❌ **Incorrect:**
```python

def unsafe_webhook_handler():
    data = request.json
    process_data(data)  # Нет проверки подписи
```

✅ **Correct:**
```python

def safe_webhook_handler():
    signature = request.headers.get('X-Webhook-Signature')
    if not verify_signature(signature):
        return {'error': 'Invalid signature'}, 401
    data = request.json
    process_data(data)
```

**Why:** Webhooks должны проверять подпись для безопасности.

---

## 💡 Key Takeaways

- **Синхронные vs асинхронные**: Синхронные API блокируют клиента, асинхронные позволяют продолжать работу. Выбор зависит от требований к времени ответа и эффективности

- **Request-Response**: Классический синхронный паттерн для операций, требующих немедленного результата. Простой, но блокирующий

- **Асинхронные вызовы**: Callbacks, Promises/Futures позволяют неблокирующую обработку. Подходят для операций, не требующих немедленного результата

- **Webhooks**: Способ доставки событий от сервера к клиенту через HTTP POST. Избегает polling, требует проверки подписи для безопасности

- **Message Queues**: Обеспечивают надёжную асинхронную доставку сообщений. Подходят для критичных операций с требованиями надёжности и масштабируемости

---

## 🚀 Next Steps

**Related Modules:**

- [04_Data_Formats](../04_Data_Formats/) — форматы данных для API
- [08_Integration_Patterns](../08_Integration_Patterns/) — интеграционные паттерны
- [14_Errors_Monitoring](../14_Errors_Monitoring/) — обработка ошибок и мониторинг

**Practice Ideas:**

1. Реализуйте синхронный и асинхронный клиент для одного и того же API
2. Создайте систему с webhooks для уведомлений о событиях
3. Настройте очередь сообщений для асинхронной обработки задач

**Going Deeper:**

- Event-Driven Architecture: углублённое изучение событийно-ориентированной архитектуры
- Message Queue Patterns: паттерны работы с очередями сообщений
- Async/Await Best Practices: лучшие практики асинхронного программирования

---

## 📚 Additional Resources

**Documentation:**

- [aiohttp Documentation](https://docs.aiohttp.org/) — асинхронный HTTP клиент/сервер
- [RabbitMQ Tutorial](https://www.rabbitmq.com/getstarted.html) — работа с очередями сообщений

**Articles:**

- "Understanding Async/Await in Python" — понимание асинхронного программирования
- "Webhooks vs Polling: When to Use What" — сравнение webhooks и polling

---


