# Продвинутые интеграционные паттерны
## Anti-corruption layer, API Gateway, Backend for Frontend (BFF), Service Mesh

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые интеграционные паттерны
- Знать архитектуру микросервисов
- Иметь представление о сетевых протоколах

**Recommended prior modules:**

- [08_Integration_Patterns](../08_Integration_Patterns/) — интеграционные паттерны
- [11_API_Implementation](../11_API_Implementation/) — реализация и интеграция API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять Anti-corruption layer для изоляции legacy систем
- Использовать API Gateway для централизованного управления API
- Реализовывать Backend for Frontend (BFF) паттерн
- Понимать концепцию Service Mesh и её применение
- Выбирать подходящий паттерн для конкретной архитектуры

---

## 1. Anti-Corruption Layer

**Anti-Corruption Layer (ACL)** — это слой, который изолирует вашу систему от legacy систем, преобразуя их интерфейсы в понятные для вашей системы.

### 1.1 Концепция

**Example: Anti-Corruption Layer**

```python
class LegacySystemACL:
    """Anti-Corruption Layer для legacy системы"""
    
    def __init__(self, legacy_api):
        self.legacy_api = legacy_api
    
    def get_user(self, user_id):
        """Преобразование legacy формата в современный"""
        # Legacy API возвращает устаревший формат
        legacy_data = self.legacy_api.fetch_user_data(user_id)
        
        # Преобразование в современный формат
        return {
            "id": legacy_data["usr_id"],
            "name": legacy_data["usr_nm"],
            "email": legacy_data["usr_email_addr"],
            "created_at": self._parse_legacy_date(legacy_data["crt_dt"])
        }
    
    def create_user(self, user_data):
        """Преобразование современного формата в legacy"""
        # Преобразование в legacy формат
        legacy_data = {
            "usr_id": user_data["id"],
            "usr_nm": user_data["name"],
            "usr_email_addr": user_data["email"]
        }
        
        return self.legacy_api.create_user_data(legacy_data)
    
    def _parse_legacy_date(self, date_str):
        """Парсинг legacy формата даты"""
        from datetime import datetime
        return datetime.strptime(date_str, "%Y%m%d").isoformat()

# Использование

acl = LegacySystemACL(legacy_api)
# Современная система работает с нормализованным интерфейсом

user = acl.get_user(123)
```

**Преимущества ACL:**

- Изоляция от legacy систем
- Защита от изменений в legacy системах
- Нормализация интерфейсов

---

## 2. API Gateway

**API Gateway** — это единая точка входа для всех клиентских запросов к микросервисам.

### 2.1 Концепция

**Example: API Gateway**

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

class APIGateway:
    """API Gateway для маршрутизации запросов"""
    
    def __init__(self):
        self.services = {
            "users": "http://user-service:8001",
            "orders": "http://order-service:8002",
            "payments": "http://payment-service:8003"
        }
    
    def route_request(self, service_name, path, method, data=None):
        """Маршрутизация запроса к соответствующему сервису"""
        if service_name not in self.services:
            return None, 404
        
        service_url = self.services[service_name]
        url = f"{service_url}{path}"
        
        response = requests.request(method, url, json=data)
        return response.json(), response.status_code

gateway = APIGateway()

@app.route("/api/<service>/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def gateway_route(service, path):
    """Gateway endpoint"""
    data = request.json if request.is_json else None
    result, status = gateway.route_request(
        service,
        f"/{path}",
        request.method,
        data
    )
    return jsonify(result), status
```

### 2.2 Функции API Gateway

**API Gateway обеспечивает:**

- Единую точку входа
- Аутентификацию и авторизацию
- Rate limiting
- Кэширование
- Логирование и мониторинг
- Преобразование протоколов

### 2.3 Аутентификация в API Gateway

**Example: Централизованная аутентификация**

```python
from functools import wraps
from flask import request, jsonify

def require_auth(f):
    """Декоратор для проверки аутентификации"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not validate_token(token):
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/<service>/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
@require_auth
def gateway_route(service, path):
    """Gateway endpoint с аутентификацией"""
    data = request.json if request.is_json else None
    result, status = gateway.route_request(
        service,
        f"/{path}",
        request.method,
        data
    )
    return jsonify(result), status
```

### 2.4 Rate Limiting в API Gateway

**Example: Rate limiting на уровне Gateway**

```python
from collections import defaultdict
from datetime import datetime, timedelta

class GatewayRateLimiter:
    """Rate limiting для API Gateway"""
    
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, client_id):
        """Проверка rate limit"""
        now = datetime.utcnow()
        window_start = now - timedelta(seconds=self.window_seconds)
        
        self.requests[client_id] = [
            req_time for req_time in self.requests[client_id]
            if req_time > window_start
        ]
        
        if len(self.requests[client_id]) >= self.max_requests:
            return False
        
        self.requests[client_id].append(now)
        return True

rate_limiter = GatewayRateLimiter()

@app.before_request
def check_rate_limit():
    """Проверка rate limit перед запросом"""
    client_id = request.remote_addr
    if not rate_limiter.is_allowed(client_id):
        return jsonify({"error": "Rate limit exceeded"}), 429
```

### 2.5 Кэширование в API Gateway

**Example: Кэширование ответов**

```python
from functools import lru_cache
import hashlib
import json

class GatewayCache:
    """Кэширование ответов в API Gateway"""
    
    def __init__(self, ttl_seconds=300):
        self.cache = {}
        self.ttl = ttl_seconds
    
    def get_cache_key(self, service, path, method):
        """Генерация ключа кэша"""
        key_string = f"{service}:{path}:{method}"
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def get(self, key):
        """Получение из кэша"""
        if key in self.cache:
            entry = self.cache[key]
            if datetime.utcnow() < entry["expires_at"]:
                return entry["data"]
            del self.cache[key]
        return None
    
    def set(self, key, data):
        """Сохранение в кэш"""
        self.cache[key] = {
            "data": data,
            "expires_at": datetime.utcnow() + timedelta(seconds=self.ttl)
        }

gateway_cache = GatewayCache()

@app.route("/api/<service>/<path:path>", methods=["GET"])
def gateway_route_cached(service, path):
    """Gateway с кэшированием для GET запросов"""
    cache_key = gateway_cache.get_cache_key(service, path, "GET")
    cached = gateway_cache.get(cache_key)
    
    if cached:
        return jsonify(cached), 200
    
    result, status = gateway.route_request(service, f"/{path}", "GET")
    if status == 200:
        gateway_cache.set(cache_key, result)
    
    return jsonify(result), status
```

---

## 3. Backend for Frontend (BFF)

**BFF** — это отдельный backend для каждого типа клиента (web, mobile), адаптирующий API под нужды клиента.

### 3.1 Концепция

**Example: BFF для мобильного приложения**

```python
class MobileBFF:
    """Backend for Frontend для мобильного приложения"""
    
    def __init__(self, user_service, order_service):
        self.user_service = user_service
        self.order_service = order_service
    
    def get_user_dashboard(self, user_id):
        """Агрегация данных для мобильного dashboard"""
        # Получение данных из нескольких сервисов
        user = self.user_service.get_user(user_id)
        orders = self.order_service.get_user_orders(user_id)
        
        # Адаптация под мобильное приложение
        return {
            "user": {
                "id": user["id"],
                "name": user["name"],
                "avatar": user.get("avatar_url")
            },
            "recent_orders": [
                {
                    "id": order["id"],
                    "total": order["total"],
                    "status": order["status"],
                    "date": order["created_at"]
                }
                for order in orders[:5]  # Только последние 5
            ],
            "summary": {
                "total_orders": len(orders),
                "total_spent": sum(o["total"] for o in orders)
            }
        }

# Использование

bff = MobileBFF(user_service, order_service)
dashboard = bff.get_user_dashboard(123)
```

**Преимущества BFF:**

- Оптимизация данных для клиента
- Уменьшение количества запросов
- Адаптация под специфику клиента

---

## 4. Service Mesh

**Service Mesh** — это инфраструктурный слой для управления коммуникацией между микросервисами.

### 4.1 Концепция

**Service Mesh обеспечивает:**

- Service discovery
- Load balancing
- Retry и circuit breaking
- Security (mTLS)
- Observability (метрики, трейсинг)

**Example: Service Mesh концепция**

```python
# Service Mesh управляет коммуникацией между сервисами
# Вместо прямых вызовов:
# service_a -> service_b

# Service Mesh обеспечивает:
# service_a -> sidecar -> mesh -> sidecar -> service_b

# Sidecar обрабатывает:
# - Service discovery
# - Load balancing
# - Retry logic
# - Security
# - Observability
```

### 4.2 Service Discovery

**Example: Service Discovery концепция**

```python
class ServiceRegistry:
    """Регистр сервисов для Service Discovery"""
    
    def __init__(self):
        self.services = {}
    
    def register(self, service_name, instances):
        """Регистрация инстансов сервиса"""
        self.services[service_name] = instances
    
    def discover(self, service_name):
        """Обнаружение инстансов сервиса"""
        return self.services.get(service_name, [])
    
    def get_instance(self, service_name, strategy="round_robin"):
        """Получение инстанса по стратегии"""
        instances = self.discover(service_name)
        if not instances:
            return None
        
        if strategy == "round_robin":
            # Round-robin балансировка
            return instances[0]  # Упрощённо
        elif strategy == "random":
            import random
            return random.choice(instances)
        return instances[0]

# Использование

registry = ServiceRegistry()
registry.register("user-service", [
    "http://user-service-1:8001",
    "http://user-service-2:8001",
    "http://user-service-3:8001"
])

instance = registry.get_instance("user-service")
```

### 4.3 Circuit Breaker паттерн

**Example: Circuit Breaker для надёжности**

```python
class CircuitBreaker:
    """Circuit Breaker для защиты от каскадных отказов"""
    
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open
    
    def call(self, func, *args, **kwargs):
        """Вызов функции через circuit breaker"""
        if self.state == "open":
            if self._should_attempt_reset():
                self.state = "half-open"
            else:
                raise Exception("Circuit breaker is open")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Обработка успешного вызова"""
        self.failures = 0
        self.state = "closed"
    
    def _on_failure(self):
        """Обработка неудачного вызова"""
        self.failures += 1
        self.last_failure_time = datetime.utcnow()
        
        if self.failures >= self.failure_threshold:
            self.state = "open"
    
    def _should_attempt_reset(self):
        """Проверка, можно ли попробовать сбросить"""
        if self.last_failure_time:
            elapsed = (datetime.utcnow() - self.last_failure_time).total_seconds()
            return elapsed >= self.timeout
        return False

# Использование

circuit_breaker = CircuitBreaker()

def call_external_service():
    """Вызов внешнего сервиса"""
    return requests.get("http://external-service/api/data").json()

try:
    result = circuit_breaker.call(call_external_service)
except Exception as e:
    # Fallback логика
    result = {"error": "Service unavailable"}
```

### 4.4 Популярные Service Mesh

**Примеры:**

- **Istio**: Популярный Service Mesh для Kubernetes

- **Linkerd**: Легковесный Service Mesh

- **Consul Connect**: Service Mesh от HashiCorp

### 4.5 Retry логика

**Example: Retry с экспоненциальной задержкой**

```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3, initial_delay=1, backoff_factor=2):
    """Декоратор для retry с экспоненциальной задержкой"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator

@retry_with_backoff(max_retries=3, initial_delay=1)
def call_service():
    """Вызов сервиса с retry"""
    response = requests.get("http://service/api/data")
    response.raise_for_status()
    return response.json()
```

---

## 5. Комбинирование паттернов

### 5.1 Комбинирование ACL и API Gateway

**Example: ACL через API Gateway**

```python
class GatewayWithACL:
    """API Gateway с поддержкой ACL для legacy систем"""
    
    def __init__(self):
        self.gateway = APIGateway()
        self.acl_layers = {}
    
    def register_legacy_service(self, service_name, legacy_api):
        """Регистрация legacy сервиса с ACL"""
        acl = LegacySystemACL(legacy_api)
        self.acl_layers[service_name] = acl
        self.gateway.services[service_name] = "legacy"
    
    def route_legacy_request(self, service_name, path, method, data=None):
        """Маршрутизация через ACL"""
        if service_name in self.acl_layers:
            acl = self.acl_layers[service_name]
            # Преобразование через ACL
            if method == "GET":
                return acl.get_user(data.get("id")), 200
            elif method == "POST":
                return acl.create_user(data), 201
        return None, 404
```

### 5.2 Комбинирование BFF и API Gateway

**Example: BFF через API Gateway**

```python
class GatewayBFF:
    """BFF, использующий API Gateway для доступа к сервисам"""
    
    def __init__(self, gateway):
        self.gateway = gateway
        self.bff = MobileBFF(
            lambda user_id: gateway.route_request("users", f"/users/{user_id}", "GET")[0],
            lambda user_id: gateway.route_request("orders", f"/orders?user_id={user_id}", "GET")[0]
        )
    
    def get_dashboard(self, user_id):
        """Dashboard через BFF и Gateway"""
        return self.bff.get_user_dashboard(user_id)
```

## 6. Сравнение паттернов

### 6.1 Сравнительная таблица

| Паттерн | Назначение | Сложность | Использование |
|---------|-----------|-----------|---------------|
| **ACL** | Изоляция от legacy | Средняя | Legacy интеграции |
| **API Gateway** | Единая точка входа | Высокая | Микросервисы |
| **BFF** | Адаптация под клиента | Средняя | Множественные клиенты |
| **Service Mesh** | Инфраструктура коммуникации | Очень высокая | Крупные микросервисы |

### 6.2 Выбор паттерна

**Используйте ACL если:**

- Интеграция с legacy системами
- Нужна изоляция от изменений
- Нормализация интерфейсов

**Используйте API Gateway если:**

- Микросервисная архитектура
- Нужна централизованная точка входа
- Требуется единая аутентификация

**Используйте BFF если:**

- Множественные типы клиентов
- Нужна оптимизация данных
- Разные требования клиентов

**Используйте Service Mesh если:**

- Крупная микросервисная архитектура
- Нужна инфраструктура коммуникации
- Требуется observability

## 7. Практические примеры

### 7.1 Пример: Полноценный API Gateway

```python
class FullFeaturedGateway:
    """Полнофункциональный API Gateway"""
    
    def __init__(self):
        self.services = {}
        self.rate_limiter = GatewayRateLimiter()
        self.cache = GatewayCache()
        self.auth_validator = None
    
    def route_with_features(self, service, path, method, data=None, client_id=None):
        """Маршрутизация со всеми функциями Gateway"""
        # 1. Rate limiting
        if not self.rate_limiter.is_allowed(client_id):
            return None, 429
        
        # 2. Кэширование для GET
        if method == "GET":
            cache_key = self.cache.get_cache_key(service, path, method)
            cached = self.cache.get(cache_key)
            if cached:
                return cached, 200
        
        # 3. Маршрутизация
        result, status = self._route_to_service(service, path, method, data)
        
        # 4. Сохранение в кэш
        if method == "GET" and status == 200:
            cache_key = self.cache.get_cache_key(service, path, method)
            self.cache.set(cache_key, result)
        
        return result, status
    
    def _route_to_service(self, service, path, method, data):
        """Внутренняя маршрутизация"""
        # Реализация маршрутизации
        pass
```

### 7.2 Пример: Множественные BFF

```python
class BFFManager:
    """Управление множественными BFF"""
    
    def __init__(self):
        self.bffs = {
            "mobile": MobileBFF(user_service, order_service),
            "web": WebBFF(user_service, order_service, analytics_service),
            "admin": AdminBFF(user_service, order_service, analytics_service)
        }
    
    def get_dashboard(self, client_type, user_id):
        """Получение dashboard для типа клиента"""
        bff = self.bffs.get(client_type)
        if not bff:
            raise ValueError(f"Unknown client type: {client_type}")
        return bff.get_user_dashboard(user_id)

# Использование

bff_manager = BFFManager()
mobile_dashboard = bff_manager.get_dashboard("mobile", 123)
web_dashboard = bff_manager.get_dashboard("web", 123)
```

## 8. Common Pitfalls

### 8.1 Pitfall: Переусложнение с Service Mesh

❌ **Incorrect:**
```python
# Плохо: Service Mesh для простой архитектуры из 2-3 сервисов

setup_service_mesh(services)  # Избыточная сложность
```

✅ **Correct:**
```python
# Хорошо: Service Mesh только для крупных систем

if len(services) > 10:
    setup_service_mesh(services)
else:
    use_simple_integration(services)
```

**Why:** Service Mesh добавляет сложность. Используйте только когда это оправдано.

### 8.2 Pitfall: Отсутствие ACL для legacy

❌ **Incorrect:**
```python
# Плохо: Прямое использование legacy API

legacy_data = legacy_api.get_data()  # Прямая зависимость
```

✅ **Correct:**
```python
# Хорошо: ACL изолирует legacy

acl = LegacySystemACL(legacy_api)
normalized_data = acl.get_data()  # Нормализованный интерфейс
```

**Why:** ACL защищает от изменений в legacy системах.

---

## 💡 Key Takeaways

- **Anti-Corruption Layer**: Изолирует систему от legacy, преобразуя интерфейсы. Защищает от изменений в legacy системах

- **API Gateway**: Единая точка входа для микросервисов. Обеспечивает аутентификацию, rate limiting, кэширование, логирование

- **Backend for Frontend (BFF)**: Отдельный backend для каждого типа клиента. Оптимизирует данные и уменьшает количество запросов

- **Service Mesh**: Инфраструктурный слой для управления коммуникацией между микросервисами. Обеспечивает service discovery, load balancing, security, observability

- **Выбор паттерна**: Зависит от архитектуры. ACL для legacy, API Gateway для микросервисов, BFF для множественных клиентов, Service Mesh для крупных систем

---

## 🚀 Next Steps

**Related Modules:**

- [08_Integration_Patterns](../08_Integration_Patterns/) — базовые интеграционные паттерны
- [17_Enterprise_Integrations](../17_Enterprise_Integrations/) — enterprise интеграции

**Practice Ideas:**

1. Реализуйте ACL для legacy системы
2. Настройте API Gateway для микросервисов
3. Создайте BFF для мобильного приложения

**Going Deeper:**

- API Gateway Patterns: паттерны API Gateway
- Service Mesh Architecture: архитектура Service Mesh
- Microservices Patterns: паттерны микросервисов

---

## 📚 Additional Resources

**Documentation:**

- [Istio Documentation](https://istio.io/docs/) — Service Mesh Istio
- [Kong API Gateway](https://docs.konghq.com/) — API Gateway

**Articles:**

- "API Gateway Pattern" — паттерн API Gateway
- "Service Mesh Explained" — объяснение Service Mesh

---




