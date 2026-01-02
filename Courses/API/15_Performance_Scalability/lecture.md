# Производительность и масштабируемость API
## Latency и throughput, Rate limiting, Caching, горизонтальное масштабирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать проектирование API
- Знать основы производительности и масштабирования
- Иметь представление о кэшировании и балансировке нагрузки

**Recommended prior modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [14_Errors_Monitoring](../14_Errors_Monitoring/) — ошибки и мониторинг

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Измерять и оптимизировать latency и throughput API
- Применять rate limiting для защиты от перегрузок
- Использовать кэширование для повышения производительности
- Проектировать горизонтальное масштабирование API
- Балансировать нагрузку между несколькими инстансами

---

## 1. Latency и Throughput

**Latency** — время отклика API. **Throughput** — количество запросов, обрабатываемых за единицу времени.

### 1.1 Измерение Latency

**Example: Измерение latency**

```python
import time
from functools import wraps

def measure_latency(f):
    """Декоратор для измерения latency"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        duration_ms = (time.time() - start_time) * 1000
        
        # Логирование latency
        log_latency(f.__name__, duration_ms)
        
        return result
    return decorated_function

@app.route("/api/users/<int:user_id>", methods=["GET"])
@measure_latency
def get_user(user_id):
    user = find_user(user_id)
    return jsonify(user), 200

def log_latency(endpoint, duration_ms):
    """Логирование latency"""
    if duration_ms > 1000:
        logger.warning(f"Slow endpoint: {endpoint} took {duration_ms}ms")
```

### 1.2 Throughput

**Example: Измерение throughput**

```python
class ThroughputMonitor:
    """Мониторинг throughput"""
    
    def __init__(self, window_seconds=60):
        self.window_seconds = window_seconds
        self.requests = []
    
    def record_request(self):
        """Запись запроса"""
        self.requests.append(time.time())
        self._clean_old_requests()
    
    def get_throughput(self):
        """Получение текущего throughput (requests per second)"""
        self._clean_old_requests()
        return len(self.requests) / self.window_seconds
    
    def _clean_old_requests(self):
        """Очистка старых запросов"""
        now = time.time()
        cutoff = now - self.window_seconds
        self.requests = [req_time for req_time in self.requests if req_time > cutoff]

# Использование

throughput_monitor = ThroughputMonitor()
throughput_monitor.record_request()
print(f"Throughput: {throughput_monitor.get_throughput()} req/s")
```

---

## 2. Rate Limiting

**Rate Limiting** ограничивает количество запросов от клиента для защиты от перегрузок.

### 2.1 Реализация Rate Limiting

**Example: Rate Limiting**

```python
from collections import defaultdict
from datetime import datetime, timedelta

class RateLimiter:
    """Rate limiting для API"""
    
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, identifier):
        """Проверка, разрешён ли запрос"""
        now = datetime.utcnow()
        window_start = now - timedelta(seconds=self.window_seconds)
        
        # Очистка старых запросов
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if req_time > window_start
        ]
        
        # Проверка лимита
        if len(self.requests[identifier]) >= self.max_requests:
            return False, self.max_requests - len(self.requests[identifier])
        
        # Регистрация запроса
        self.requests[identifier].append(now)
        remaining = self.max_requests - len(self.requests[identifier])
        return True, remaining

rate_limiter = RateLimiter(max_requests=100, window_seconds=60)

@app.route("/api/users", methods=["GET"])
def get_users():
    identifier = request.remote_addr
    allowed, remaining = rate_limiter.is_allowed(identifier)
    
    if not allowed:
        return jsonify({
            "error": "Rate limit exceeded",
            "retry_after": 60
        }), 429
    
    response = jsonify(get_all_users())
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    return response, 200
```

### 2.2 Стратегии Rate Limiting

**Типы rate limiting:**

- **Fixed Window**: Фиксированное окно времени

- **Sliding Window**: Скользящее окно

- **Token Bucket**: Ведро с токенами

---

## 3. Caching

**Кэширование** сохраняет ответы для повторного использования, снижая нагрузку на сервер.

### 3.1 HTTP Caching

**Example: HTTP кэширование**

```python
from flask import make_response
from datetime import datetime, timedelta

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user(user_id)
    
    response = make_response(jsonify(user))
    
    # Кэширование на 5 минут
    response.headers["Cache-Control"] = "public, max-age=300"
    response.headers["ETag"] = generate_etag(user)
    response.headers["Last-Modified"] = user["updated_at"]
    
    return response, 200

def generate_etag(data):
    """Генерация ETag для валидации кэша"""
    import hashlib
    content = json.dumps(data, sort_keys=True)
    return hashlib.md5(content.encode()).hexdigest()
```

### 3.2 Application-Level Caching

**Example: Кэширование в приложении**

```python
from functools import lru_cache
import redis

# In-memory кэш

@lru_cache(maxsize=1000)
def get_user_cached(user_id):
    """Кэширование в памяти"""
    return find_user(user_id)

# Redis кэш

redis_client = redis.Redis(host='localhost', port=6379)

def get_user_with_redis_cache(user_id):
    """Кэширование в Redis"""
    cache_key = f"user:{user_id}"
    
    # Попытка получить из кэша
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Получение из БД
    user = find_user(user_id)
    
    # Сохранение в кэш (TTL 5 минут)
    redis_client.setex(cache_key, 300, json.dumps(user))
    
    return user
```

---

## 4. Горизонтальное масштабирование

**Горизонтальное масштабирование** — добавление большего количества серверов для обработки нагрузки.

### 4.1 Load Balancing

**Example: Балансировка нагрузки**

```python
# Конфигурация load balancer (Nginx)

"""
upstream api_servers {
    server api1.example.com:8000;
    server api2.example.com:8000;
    server api3.example.com:8000;
}

server {
    location /api {
        proxy_pass http://api_servers;
    }
}
"""

# Приложение должно быть stateless для горизонтального масштабирования
# Не хранить состояние в памяти приложения
```

### 4.2 Stateless архитектура

**Критично для масштабирования:**

- Не хранить состояние в памяти приложения
- Использовать внешние хранилища (БД, кэш)
- Stateless позволяет добавлять инстансы

---

## 5. Оптимизация производительности

### 5.1 Database оптимизация

**Example: Оптимизация запросов**

```python
# ❌ Плохо: N+1 проблема

def get_users_with_orders():
    users = get_all_users()
    for user in users:
        user["orders"] = get_user_orders(user["id"])  # N запросов!
    return users

# ✅ Хорошо: Batch запрос

def get_users_with_orders_optimized():
    users = get_all_users()
    user_ids = [u["id"] for u in users]
    all_orders = get_orders_for_users(user_ids)  # 1 запрос
    
    # Группировка по пользователям
    orders_by_user = defaultdict(list)
    for order in all_orders:
        orders_by_user[order["user_id"]].append(order)
    
    for user in users:
        user["orders"] = orders_by_user.get(user["id"], [])
    return users
```

### 5.2 Пагинация

**Example: Пагинация для производительности**

```python
@app.route("/api/users", methods=["GET"])
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 10, type=int), 100)  # Максимум 100
    
    # Пагинация снижает нагрузку
    users = get_users_paginated(page, per_page)
    return jsonify(users), 200
```

### 5.3 Оптимизация запросов к БД

**Example: Использование индексов**

```python
# Создание индексов для частых запросов
# CREATE INDEX idx_user_email ON users(email);
# CREATE INDEX idx_order_user_id ON orders(user_id);

def get_user_by_email(email):
    """Быстрый поиск по индексу"""
    # Использует индекс idx_user_email
    return db.query("SELECT * FROM users WHERE email = ?", email).first()
```

### 5.4 Connection Pooling

**Example: Connection Pooling для производительности**

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Connection pool для переиспользования соединений

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    poolclass=QueuePool,
    pool_size=10,  # Размер пула
    max_overflow=20,  # Максимум дополнительных соединений
    pool_pre_ping=True  # Проверка соединений перед использованием
)
```

### 5.5 Асинхронная обработка

**Example: Асинхронная обработка долгих операций**

```python
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379')

@celery_app.task
def process_large_dataset(data):
    """Асинхронная обработка большого набора данных"""
    # Долгая операция
    result = process_data(data)
    return result

@app.route("/api/process", methods=["POST"])
def start_processing():
    """Запуск асинхронной обработки"""
    data = request.json
    task = process_large_dataset.delay(data)
    return jsonify({"task_id": task.id, "status": "processing"}), 202
```

## 6. Мониторинг производительности

### 6.1 Измерение метрик

**Example: Измерение latency и throughput**

```python
import time
from functools import wraps

def measure_performance(func):
    """Декоратор для измерения производительности"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration_ms = (time.time() - start_time) * 1000
        
        # Логирование метрик
        logger.info(f"{func.__name__} took {duration_ms:.2f}ms")
        
        # Запись в метрики
        metrics.record_latency(func.__name__, duration_ms)
        
        return result
    return wrapper

@measure_performance
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Endpoint с измерением производительности"""
    user = db.get_user(user_id)
    return jsonify(user), 200
```

### 6.2 Профилирование

**Example: Профилирование медленных запросов**

```python
import cProfile
import pstats

class PerformanceProfiler:
    """Профилирование производительности"""
    
    def profile_endpoint(self, endpoint_func):
        """Профилирование endpoint"""
        profiler = cProfile.Profile()
        profiler.enable()
        
        result = endpoint_func()
        
        profiler.disable()
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Топ 10 медленных операций
        
        return result
```

---

## 💡 Key Takeaways

- **Latency и Throughput**: Latency — время отклика, throughput — количество запросов в секунду. Оба критичны для производительности API

- **Rate Limiting**: Ограничение количества запросов защищает от перегрузок и злоупотреблений. Возвращает 429 при превышении лимита

- **Caching**: HTTP кэширование и application-level кэширование снижают нагрузку на сервер и улучшают latency. Критично для часто запрашиваемых данных

- **Горизонтальное масштабирование**: Добавление серверов для обработки нагрузки. Требует stateless архитектуры и load balancing

- **Оптимизация**: Database оптимизация (избегать N+1), пагинация, индексы критичны для производительности API

---

## 🚀 Next Steps

**Related Modules:**

- [14_Errors_Monitoring](../14_Errors_Monitoring/) — ошибки и мониторинг
- [13_API_Security](../13_API_Security/) — безопасность API

**Practice Ideas:**

1. Измерьте latency и throughput вашего API
2. Реализуйте rate limiting с различными стратегиями
3. Настройте кэширование для улучшения производительности

**Going Deeper:**

- Performance Optimization: углублённая оптимизация производительности
- Caching Strategies: стратегии кэширования
- Scalability Patterns: паттерны масштабирования

---

## 📚 Additional Resources

**Documentation:**

- [Redis Documentation](https://redis.io/docs/) — кэширование
- [Nginx Load Balancing](https://nginx.org/en/docs/http/load_balancing.html) — балансировка нагрузки

**Articles:**

- "API Performance Optimization" — оптимизация производительности API
- "Caching Strategies for APIs" — стратегии кэширования

---




