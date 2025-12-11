# Архитектура веб-приложений
## От монолита до микросервисов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать HTTP и веб-серверы
- Знать основы WSGI/ASGI
- Иметь опыт разработки веб-приложений

**Recommended prior modules:**

- [Web Servers](../03_WebServers/) — веб-серверы
- [WSGI](../05_WSGI/) и [ASGI](../06_ASGI/) — интерфейсы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать различные архитектурные паттерны
- Проектировать масштабируемые веб-приложения
- Выбирать подходящую архитектуру для задачи
- Понимать роль кэширования, очередей, CDN
- Настраивать production-ready инфраструктуру

---

## 1. Эволюция веб-архитектуры

### 1.1 Традиционная архитектура (1990-е)

```

┌────────────────────────────────────────────────────────────┐
│              Traditional Web Architecture                   │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Browser ────► Web Server ────► CGI/PHP ────► Database     │
│              (Apache)       (mod_php)      (MySQL)         │
│                                                            │
│  Всё на одном сервере:                                     │
│  - Статические файлы                                       │
│  - Динамический контент                                    │
│  - База данных                                             │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 1.2 Современная архитектура

```

┌────────────────────────────────────────────────────────────┐
│              Modern Web Architecture                        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                         ┌──────────┐                       │
│                         │   CDN    │ ◄── Static files      │
│                         └────┬─────┘                       │
│                              │                             │
│    Browser ──────────► Load Balancer                       │
│                              │                             │
│         ┌────────────────────┼────────────────────┐        │
│         │                    │                    │        │
│         ▼                    ▼                    ▼        │
│    ┌─────────┐          ┌─────────┐          ┌─────────┐   │
│    │ App 1   │          │ App 2   │          │ App N   │   │
│    └────┬────┘          └────┬────┘          └────┬────┘   │
│         │                    │                    │        │
│         └──────────┬─────────┴────────────────────┘        │
│                    │                                       │
│              ┌─────┴─────┐                                 │
│              │   Cache   │ (Redis)                         │
│              └─────┬─────┘                                 │
│                    │                                       │
│         ┌─────────────────────┐                            │
│         │     Database        │                            │
│         │  Primary / Replica  │                            │
│         └─────────────────────┘                            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

---

## 2. Архитектурные паттерны

### 2.1 Монолитная архитектура

```

┌────────────────────────────────────────────────────────────┐
│                    Monolithic Application                   │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │                    One Codebase                     │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐            │    │
│  │  │   Auth   │ │  Orders  │ │ Products │            │    │
│  │  └──────────┘ └──────────┘ └──────────┘            │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐            │    │
│  │  │ Payments │ │   Users  │ │Notifications│         │    │
│  │  └──────────┘ └──────────┘ └──────────┘            │    │
│  │                                                     │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │              Shared Database                  │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────┘    │
│                                                            │
│  Преимущества:              Недостатки:                    │
│  + Простота разработки      - Сложно масштабировать       │
│  + Простой деплой           - Один баг ломает всё          │
│  + Транзакции               - Тяжело для больших команд   │
│  + Отладка                  - Медленный деплой            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 2.2 Микросервисная архитектура

```

┌────────────────────────────────────────────────────────────┐
│                  Microservices Architecture                 │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  API Gateway                                               │
│       │                                                    │
│       ├──────────────┬──────────────┬──────────────┐       │
│       │              │              │              │       │
│       ▼              ▼              ▼              ▼       │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │  Auth   │    │ Orders  │    │Products │    │ Users   │  │
│  │ Service │    │ Service │    │ Service │    │ Service │  │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘  │
│       │              │              │              │       │
│       ▼              ▼              ▼              ▼       │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │   DB    │    │   DB    │    │   DB    │    │   DB    │  │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘  │
│                                                            │
│  Каждый сервис:                                            │
│  - Независимо развёртывается                              │
│  - Своя база данных                                        │
│  - Своя команда                                            │
│  - Может быть на другом языке                              │
│                                                            │
│  Преимущества:              Недостатки:                    │
│  + Масштабирование          - Сложность операций          │
│  + Независимый деплой       - Distributed transactions    │
│  + Отказоустойчивость       - Network latency             │
│  + Разные технологии        - Сложная отладка             │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 2.3 Serverless (FaaS)

```

┌────────────────────────────────────────────────────────────┐
│                  Serverless / FaaS                          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Event ──────► Function ──────► Response                   │
│                                                            │
│  HTTP Request ─────► Lambda/Cloud Function                 │
│  Queue Message ────► Lambda/Cloud Function                 │
│  Schedule (cron) ──► Lambda/Cloud Function                 │
│  DB Change ────────► Lambda/Cloud Function                 │
│                                                            │
│  Преимущества:              Недостатки:                    │
│  + Pay per use              - Cold start latency          │
│  + Auto-scaling             - Vendor lock-in               │
│  + Нет управления серверами - Ограничения runtime          │
│  + Быстрая разработка       - Сложная отладка             │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

---

## 3. Компоненты веб-архитектуры

### 3.1 Load Balancer

```

┌────────────────────────────────────────────────────────────┐
│                     Load Balancer                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                    Load Balancer                           │
│                         │                                  │
│         ┌───────────────┼───────────────┐                  │
│         │               │               │                  │
│         ▼               ▼               ▼                  │
│    ┌─────────┐     ┌─────────┐     ┌─────────┐             │
│    │ Server 1│     │ Server 2│     │ Server 3│             │
│    │ (25%)   │     │ (50%)   │     │ (25%)   │             │
│    └─────────┘     └─────────┘     └─────────┘             │
│                                                            │
│  Алгоритмы:                                                │
│  - Round Robin        — по очереди                         │
│  - Least Connections  — наименьшее число соединений        │
│  - IP Hash            — sticky sessions                    │
│  - Weighted           — с весами                           │
│                                                            │
│  L4 (Transport):      L7 (Application):                    │
│  - TCP/UDP            - HTTP/HTTPS                         │
│  - Быстрее            - Routing по URL/headers             │
│  - HAProxy, LVS       - Nginx, HAProxy, Traefik            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

**Nginx как Load Balancer:**
```nginx

upstream backend {
    least_conn;
    server 10.0.0.1:8000 weight=3;
    server 10.0.0.2:8000 weight=2;
    server 10.0.0.3:8000;
    server 10.0.0.4:8000 backup;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_next_upstream error timeout http_502 http_503;
    }
}

```

### 3.2 Reverse Proxy

```

┌────────────────────────────────────────────────────────────┐
│                     Reverse Proxy                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Client ────► Reverse Proxy ────► Backend Server           │
│              (Nginx)             (Gunicorn)                │
│                                                            │
│  Функции:                                                  │
│  - SSL termination                                         │
│  - Caching                                                 │
│  - Compression                                             │
│  - Load balancing                                          │
│  - Security (WAF)                                          │
│  - Rate limiting                                           │
│  - Static files                                            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 3.3 CDN (Content Delivery Network)

```

┌────────────────────────────────────────────────────────────┐
│                          CDN                                │
├────────────────────────────────────────────────────────────┤
│                                                            │
│           Origin Server (US)                               │
│                  │                                         │
│    ┌─────────────┼─────────────┐                           │
│    │             │             │                           │
│    ▼             ▼             ▼                           │
│  Edge         Edge          Edge                           │
│  (Europe)     (Asia)        (US West)                      │
│    │             │             │                           │
│    ▼             ▼             ▼                           │
│  Users        Users         Users                          │
│  (low         (low          (low                           │
│   latency)     latency)      latency)                      │
│                                                            │
│  Кэшируется:                                               │
│  - Статические файлы (JS, CSS, images)                     │
│  - API ответы (с правильными Cache-Control)                │
│                                                            │
│  Провайдеры: Cloudflare, AWS CloudFront, Fastly            │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 3.4 Кэширование

```

┌────────────────────────────────────────────────────────────┐
│                    Caching Layers                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Browser Cache ◄── CDN Cache ◄── App Cache ◄── DB Cache    │
│     (local)        (edge)       (Redis)      (query cache) │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Application                        │  │
│  │                                                       │  │
│  │   Request ──► Cache hit? ──► Yes ──► Return cached    │  │
│  │                   │                                   │  │
│  │                   No                                  │  │
│  │                   │                                   │  │
│  │                   ▼                                   │  │
│  │              Compute/Query                            │  │
│  │                   │                                   │  │
│  │                   ▼                                   │  │
│  │              Store in cache                           │  │
│  │                   │                                   │  │
│  │                   ▼                                   │  │
│  │              Return result                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                            │
│  Стратегии инвалидации:                                    │
│  - TTL (Time To Live)                                      │
│  - Write-through (обновлять при записи)                   │
│  - Write-behind (отложенная запись)                       │
│  - Cache-aside (ленивая загрузка)                         │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

**Redis как кэш:**
```python

import redis
import json

cache = redis.Redis(host='localhost', port=6379)

def get_user(user_id: int):
    # Пробуем кэш
    cached = cache.get(f'user:{user_id}')
    if cached:
        return json.loads(cached)
    
    # Запрос к БД
    user = db.query(User).filter(User.id == user_id).first()
    
    # Сохраняем в кэш на 5 минут
    cache.setex(f'user:{user_id}', 300, json.dumps(user.to_dict()))
    
    return user.to_dict()

def update_user(user_id: int, data: dict):
    # Обновляем БД
    db.query(User).filter(User.id == user_id).update(data)
    db.commit()
    
    # Инвалидируем кэш
    cache.delete(f'user:{user_id}')

```

### 3.5 Message Queue

```

┌────────────────────────────────────────────────────────────┐
│                    Message Queue                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Producer ──────► Queue ──────► Consumer                   │
│  (Web App)      (RabbitMQ/     (Worker)                    │
│                  Redis/SQS)                                │
│                                                            │
│  Use Cases:                                                │
│  - Async tasks (email, notifications)                      │
│  - Background processing                                   │
│  - Decoupling services                                     │
│  - Load leveling                                           │
│                                                            │
│  ┌──────────┐    ┌─────────┐    ┌──────────────────────┐   │
│  │  Web     │    │  Queue  │    │      Workers         │   │
│  │  Request │───►│         │───►│  ┌────┐ ┌────┐      │   │
│  │  (fast)  │    │ ░░░░░░░ │    │  │ W1 │ │ W2 │ ...  │   │
│  └──────────┘    └─────────┘    │  └────┘ └────┘      │   │
│                                  └──────────────────────┘   │
│                                                            │
│  Системы: RabbitMQ, Redis (Queue), AWS SQS, Kafka          │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

**Celery с Redis:**
```python
# tasks.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def send_email(to: str, subject: str, body: str):
    """Асинхронная отправка email."""
    # ... отправка email ...
    return {'status': 'sent', 'to': to}

# views.py
from tasks import send_email

def register_user(request):
    user = create_user(request.data)
    
    # Асинхронно отправляем email
    send_email.delay(
        to=user.email,
        subject='Welcome!',
        body='Thanks for registering...'
    )
    
    return {'status': 'ok'}  # Ответ сразу, email в фоне

```

---

## 4. Database Architecture

### 4.1 Репликация

```

┌────────────────────────────────────────────────────────────┐
│                  Database Replication                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Primary/Replica (Master/Slave):                           │
│                                                            │
│           Writes                                           │
│              │                                             │
│              ▼                                             │
│         ┌─────────┐                                        │
│         │ Primary │ ──── Replication ────┐                 │
│         │ (R/W)   │                      │                 │
│         └─────────┘                      │                 │
│                               ┌──────────┴──────────┐      │
│                               │                     │      │
│                               ▼                     ▼      │
│                          ┌─────────┐           ┌─────────┐ │
│                          │ Replica │           │ Replica │ │
│                          │ (Read)  │           │ (Read)  │ │
│                          └─────────┘           └─────────┘ │
│                               ▲                     ▲      │
│                               │                     │      │
│                               └─────────┬───────────┘      │
│                                         │                  │
│                                      Reads                 │
│                                                            │
│  Преимущества:                                             │
│  - Масштабирование чтения                                 │
│  - Отказоустойчивость                                      │
│  - Backup на replica                                       │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 4.2 Шардирование

```

┌────────────────────────────────────────────────────────────┐
│                    Database Sharding                        │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  User ID ────► Hash/Range ────► Shard                      │
│                                                            │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Shard 1  │    │ Shard 2  │    │ Shard 3  │              │
│  │ (A-H)    │    │ (I-P)    │    │ (Q-Z)    │              │
│  │ Users    │    │ Users    │    │ Users    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                            │
│  Стратегии:                                                │
│  - Range-based (по диапазону ключа)                       │
│  - Hash-based (хэш от ключа)                              │
│  - Directory-based (lookup table)                          │
│                                                            │
│  Проблемы:                                                 │
│  - Cross-shard queries                                     │
│  - Resharding                                              │
│  - Hot spots                                               │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 4.3 Выбор базы данных

| Тип | Примеры | Когда использовать |
|-----|---------|-------------------|
| **RDBMS** | PostgreSQL, MySQL | Сложные запросы, транзакции, связи |
| **Document** | MongoDB | Гибкая схема, JSON документы |
| **Key-Value** | Redis, Memcached | Кэш, сессии, простые данные |
| **Wide-Column** | Cassandra, HBase | Time-series, большие объёмы |
| **Graph** | Neo4j | Графовые связи, рекомендации |
| **Search** | Elasticsearch | Full-text search, логи |

---

## 5. Паттерны API

### 5.1 REST

```

┌────────────────────────────────────────────────────────────┐
│                    RESTful API                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Ресурсы и методы:                                         │
│                                                            │
│  GET    /users          — список пользователей             │
│  GET    /users/123      — конкретный пользователь          │
│  POST   /users          — создать пользователя             │
│  PUT    /users/123      — заменить пользователя            │
│  PATCH  /users/123      — частичное обновление             │
│  DELETE /users/123      — удалить пользователя             │
│                                                            │
│  Вложенные ресурсы:                                        │
│  GET    /users/123/orders      — заказы пользователя       │
│  POST   /users/123/orders      — создать заказ             │
│                                                            │
│  Query parameters:                                          │
│  GET    /users?page=1&limit=20&sort=name                   │
│  GET    /users?filter[status]=active                       │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 5.2 GraphQL

```graphql
# Query — получение данных
query {
  user(id: 123) {
    name
    email
    orders(last: 5) {
      id
      total
      items {
        product {
          name
          price
        }
      }
    }
  }
}

# Mutation — изменение данных
mutation {
  createUser(input: {name: "John", email: "john@example.com"}) {
    id
    name
  }
}

# Subscription — real-time
subscription {
  orderCreated {
    id
    total
    user {
      name
    }
  }
}

```

### 5.3 gRPC

```protobuf

// user.proto
syntax = "proto3";

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc CreateUser(CreateUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (stream User);
}

message User {
  int64 id = 1;
  string name = 2;
  string email = 3;
}

message GetUserRequest {
  int64 id = 1;
}

```

| Аспект | REST | GraphQL | gRPC |
|--------|------|---------|------|
| **Формат** | JSON | JSON | Protobuf (binary) |
| **Транспорт** | HTTP | HTTP | HTTP/2 |
| **Гибкость** | Средняя | Высокая | Низкая |
| **Производительность** | Хорошая | Хорошая | Отличная |
| **Типизация** | Слабая | Средняя | Строгая |
| **Когда** | Public API | Flexible UI | Internal services |

---

## 6. Production Setup

### 6.1 Типичный production stack

```

┌────────────────────────────────────────────────────────────┐
│                 Production Architecture                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                      CDN                             │   │
│  │              (Cloudflare / CloudFront)               │   │
│  └────────────────────────┬────────────────────────────┘   │
│                           │                                │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │              Load Balancer (HAProxy)                 │   │
│  │                    SSL Termination                   │   │
│  └────────────┬─────────────────────────┬──────────────┘   │
│               │                         │                  │
│       ┌───────▼───────┐         ┌───────▼───────┐          │
│       │    Nginx      │         │    Nginx      │          │
│       │  (Static +    │         │  (Static +    │          │
│       │   Proxy)      │         │   Proxy)      │          │
│       └───────┬───────┘         └───────┬───────┘          │
│               │                         │                  │
│       ┌───────▼───────┐         ┌───────▼───────┐          │
│       │   Gunicorn    │         │   Gunicorn    │          │
│       │   (Workers)   │         │   (Workers)   │          │
│       └───────┬───────┘         └───────┬───────┘          │
│               │                         │                  │
│               └───────────┬─────────────┘                  │
│                           │                                │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │                    Redis                             │   │
│  │         (Cache + Sessions + Celery Broker)           │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │              PostgreSQL (Primary)                    │   │
│  │                       │                              │   │
│  │            ┌──────────┴──────────┐                   │   │
│  │            │                     │                   │   │
│  │      ┌─────▼─────┐         ┌─────▼─────┐             │   │
│  │      │  Replica  │         │  Replica  │             │   │
│  │      └───────────┘         └───────────┘             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                            │
│  Отдельно:                                                 │
│  - Celery Workers (background tasks)                       │
│  - Celery Beat (scheduled tasks)                           │
│  - Monitoring (Prometheus + Grafana)                       │
│  - Logging (ELK / Loki)                                    │
│                                                            │
└────────────────────────────────────────────────────────────┘

```

### 6.2 Docker Compose пример

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./static:/var/www/static
    depends_on:
      - web

  web:
    build: .
    command: gunicorn -w 4 -b 0.0.0.0:8000 app:app
    environment:
      - DATABASE_URL=postgresql://user:pass@db/app
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  celery:
    build: .
    command: celery -A tasks worker -l info
    environment:
      - DATABASE_URL=postgresql://user:pass@db/app
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=app

  redis:
    image: redis:alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### 6.3 Kubernetes пример

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer

```

---

## 7. Мониторинг и логирование

### 7.1 Метрики (Prometheus)

```python
# metrics.py
from prometheus_client import Counter, Histogram, generate_latest

REQUEST_COUNT = Counter(
    'http_requests_total', 
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

# Middleware
def metrics_middleware(app):
    async def middleware(scope, receive, send):
        if scope['type'] != 'http':
            await app(scope, receive, send)
            return
        
        start_time = time.time()
        status = 500
        
        async def send_wrapper(message):
            nonlocal status
            if message['type'] == 'http.response.start':
                status = message['status']
            await send(message)
        
        try:
            await app(scope, receive, send_wrapper)
        finally:
            duration = time.time() - start_time
            method = scope['method']
            path = scope['path']
            
            REQUEST_COUNT.labels(method, path, status).inc()
            REQUEST_LATENCY.labels(method, path).observe(duration)
    
    return middleware

```

### 7.2 Structured Logging

```python

import structlog
import logging

# Конфигурация
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.BoundLogger,
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)

logger = structlog.get_logger()

# Использование
logger.info("user_created", user_id=123, email="user@example.com")
logger.error("payment_failed", order_id=456, error="insufficient_funds")

# Output (JSON):
# {"timestamp": "2023-11-15T10:30:00Z", "level": "info", "event": "user_created", "user_id": 123, "email": "user@example.com"}
```

---

## 💡 Key Takeaways

- **Монолит** — простота, но сложно масштабировать

- **Микросервисы** — масштабирование, но операционная сложность

- **Load Balancer** — распределение нагрузки и отказоустойчивость

- **Кэширование** — критично для производительности (Redis)

- **Message Queue** — для async задач и decoupling

- **Database Replication** — масштабирование чтения

- **CDN** — для статики и снижения latency

---

## 🚀 Next Steps

**Related Modules:**

- [Database](../09_Database/) — Взаимодействие с БД

**Practice Ideas:**

1. Настройте Nginx + Gunicorn + Redis
2. Реализуйте кэширование с инвалидацией
3. Добавьте Celery для фоновых задач
4. Настройте мониторинг с Prometheus + Grafana

**Going Deeper:**

- "Designing Data-Intensive Applications" — Martin Kleppmann
- "Building Microservices" — Sam Newman
- "Release It!" — Michael Nygard

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" — Martin Kleppmann
- "Building Microservices" — Sam Newman
- "Site Reliability Engineering" — Google

**Tools:**

- [Nginx](https://nginx.org/)
- [HAProxy](https://www.haproxy.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)

---




