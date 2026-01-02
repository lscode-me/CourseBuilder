# Безопасность API
## OAuth 2.0, JWT, Scopes и permissions, защита от злоупотреблений

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы аутентификации и авторизации
- Знать типы API и HTTP протокол
- Иметь представление о безопасности веб-приложений

**Recommended prior modules:**

- [05_Authentication_Basics](../05_Authentication_Basics/) — основы аутентификации
- [07_API_Design](../07_API_Design/) — проектирование API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Реализовывать OAuth 2.0 для безопасной авторизации
- Работать с JWT токенами для аутентификации
- Управлять scopes и permissions для контроля доступа
- Защищать API от злоупотреблений (rate limiting, throttling)
- Применять best practices безопасности API

---

## 1. OAuth 2.0

**OAuth 2.0** — это протокол авторизации, позволяющий приложению получать ограниченный доступ к ресурсам пользователя.

### 1.1 OAuth 2.0 Flow

**Example: Authorization Code Flow**

```python
# Шаг 1: Клиент запрашивает авторизацию

def get_authorization_url(client_id, redirect_uri, scope):
    """Генерация URL для авторизации"""
    auth_url = "https://auth.example.com/authorize"
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_type": "code",
        "state": generate_state()
    }
    return f"{auth_url}?{urlencode(params)}"

# Шаг 2: Пользователь авторизуется, получает код

authorization_code = "abc123xyz"

# Шаг 3: Обмен кода на токен

def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    """Обмен authorization code на access token"""
    token_url = "https://auth.example.com/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri
    }
    response = requests.post(token_url, data=data)
    return response.json()

# Шаг 4: Использование access token

def access_api_with_token(access_token):
    """Доступ к API с токеном"""
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.example.com/users/me", headers=headers)
    return response.json()
```

### 1.2 OAuth 2.0 Grant Types

**Основные grant types:**

- **Authorization Code**: Для веб-приложений

- **Client Credentials**: Для сервер-сервер коммуникации

- **Implicit**: Устарел, не рекомендуется

- **Resource Owner Password**: Не рекомендуется

---

## 2. JWT (JSON Web Tokens)

**JWT** — это компактный способ передачи информации между сторонами в виде JSON объекта.

### 2.1 Структура JWT

**JWT состоит из трёх частей:**

- **Header**: Алгоритм и тип токена

- **Payload**: Данные (claims)

- **Signature**: Подпись для верификации

**Example: Работа с JWT**

```python
import jwt
from datetime import datetime, timedelta

def create_jwt_token(user_id, secret, expires_in_hours=24):
    """Создание JWT токена"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=expires_in_hours),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

def verify_jwt_token(token, secret):
    """Верификация JWT токена"""
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload, None
    except jwt.ExpiredSignatureError:
        return None, "Token expired"
    except jwt.InvalidTokenError:
        return None, "Invalid token"

# Использование

secret = "your-secret-key"
token = create_jwt_token(user_id=123, secret=secret)
payload, error = verify_jwt_token(token, secret)
```

### 2.2 JWT Claims

**Example: JWT с scopes**

```python
def create_jwt_with_scopes(user_id, scopes, secret):
    """Создание JWT с scopes"""
    payload = {
        "user_id": user_id,
        "scopes": scopes,  # ["read:users", "write:users"]
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def check_scope(token, secret, required_scope):
    """Проверка scope в JWT"""
    payload, error = verify_jwt_token(token, secret)
    if error:
        return False
    
    token_scopes = payload.get("scopes", [])
    return required_scope in token_scopes
```

---

## 3. Scopes и Permissions

**Scopes** определяют, какие действия разрешены токену. **Permissions** — это более детальные права доступа.

### 3.1 Scopes

**Example: Управление scopes**

```python
class ScopeManager:
    """Управление scopes и permissions"""
    
    def __init__(self):
        self.scopes = {
            "read:users": "Чтение данных пользователей",
            "write:users": "Создание/изменение пользователей",
            "delete:users": "Удаление пользователей",
            "admin": "Полный доступ"
        }
    
    def validate_scope(self, token_scopes, required_scope):
        """Валидация scope"""
        if "admin" in token_scopes:
            return True  # Admin имеет все права
        return required_scope in token_scopes
    
    def get_permissions(self, scopes):
        """Получение permissions из scopes"""
        permissions = []
        for scope in scopes:
            if scope == "read:users":
                permissions.extend(["users:read", "users:list"])
            elif scope == "write:users":
                permissions.extend(["users:create", "users:update"])
            elif scope == "delete:users":
                permissions.append("users:delete")
        return permissions

# Использование

scope_manager = ScopeManager()
token_scopes = ["read:users", "write:users"]

if scope_manager.validate_scope(token_scopes, "read:users"):
    print("Access granted")
```

### 3.2 Permissions

**Example: Детальные permissions**

```python
def check_permission(user, resource, action):
    """Проверка детального permission"""
    user_permissions = get_user_permissions(user.id)
    required_permission = f"{resource}:{action}"
    
    return required_permission in user_permissions

# Использование

if check_permission(user, "users", "read"):
    # Разрешено чтение пользователей
    pass
```

---

## 4. Защита от злоупотреблений

### 4.1 Rate Limiting

**Example: Rate Limiting**

```python
from functools import wraps
from flask import request, jsonify
import time
from collections import defaultdict

class RateLimiter:
    """Rate limiting для API"""
    
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, identifier):
        """Проверка, разрешён ли запрос"""
        now = time.time()
        window_start = now - self.window_seconds
        
        # Очистка старых запросов
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if req_time > window_start
        ]
        
        # Проверка лимита
        if len(self.requests[identifier]) >= self.max_requests:
            return False
        
        # Регистрация запроса
        self.requests[identifier].append(now)
        return True

rate_limiter = RateLimiter(max_requests=100, window_seconds=60)

def rate_limit(f):
    """Декоратор для rate limiting"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        identifier = request.remote_addr  # IP адрес
        if not rate_limiter.is_allowed(identifier):
            return jsonify({
                "error": "Rate limit exceeded"
            }), 429
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/users", methods=["GET"])
@rate_limit
def get_users():
    return jsonify(get_all_users()), 200
```

### 4.2 Throttling

**Example: Throttling**

```python
class Throttler:
    """Throttling для ограничения скорости запросов"""
    
    def __init__(self, requests_per_second=10):
        self.requests_per_second = requests_per_second
        self.min_interval = 1.0 / requests_per_second
        self.last_request = {}
    
    def throttle(self, identifier):
        """Throttling запроса"""
        now = time.time()
        if identifier in self.last_request:
            elapsed = now - self.last_request[identifier]
            if elapsed < self.min_interval:
                return False, self.min_interval - elapsed
        
        self.last_request[identifier] = now
        return True, 0
```

---

## 5. Best Practices безопасности

### 5.1 HTTPS обязателен

**Всегда используйте HTTPS для API:**

- Шифрование данных в транзите
- Защита от man-in-the-middle атак
- Требование для OAuth и JWT

### 5.2 Валидация входных данных

**Example: Валидация и санитизация**

```python
def validate_and_sanitize_input(data):
    """Валидация и санитизация входных данных"""
    # Валидация
    if "email" in data:
        if not is_valid_email(data["email"]):
            raise ValueError("Invalid email")
    
    # Санитизация
    if "name" in data:
        data["name"] = sanitize_string(data["name"])
    
    return data
```

### 5.3 Защита от SQL Injection и XSS

- Использовать параметризованные запросы
- Экранировать пользовательский ввод
- Валидировать все входные данные

---

## 💡 Key Takeaways

- **OAuth 2.0**: Протокол авторизации для безопасного делегирования доступа. Authorization Code flow — рекомендуемый для веб-приложений

- **JWT**: Компактный способ передачи информации через токены. Состоит из header, payload и signature. Подходит для stateless аутентификации

- **Scopes и Permissions**: Scopes определяют общие права (read:users), permissions — детальные (users:read). Оба механизма контролируют доступ

- **Защита от злоупотреблений**: Rate limiting ограничивает количество запросов, throttling ограничивает скорость. Критично для публичных API

- **Best Practices**: HTTPS обязателен, валидация входных данных, защита от injection атак, правильное хранение секретов

---

## 🚀 Next Steps

**Related Modules:**

- [05_Authentication_Basics](../05_Authentication_Basics/) — основы аутентификации
- [14_Errors_Monitoring](../14_Errors_Monitoring/) — ошибки и мониторинг
- [15_Performance_Scalability](../15_Performance_Scalability/) — производительность

**Practice Ideas:**

1. Реализуйте OAuth 2.0 Authorization Code flow
2. Создайте систему с JWT токенами и scopes
3. Настройте rate limiting для вашего API

**Going Deeper:**

- OAuth 2.0 Specification: полная спецификация OAuth 2.0
- JWT Specification: спецификация JWT
- API Security Best Practices: лучшие практики безопасности

---

## 📚 Additional Resources

**Documentation:**

- [OAuth 2.0 RFC](https://oauth.net/2/) — спецификация OAuth 2.0
- [JWT.io](https://jwt.io/) — информация о JWT

**Articles:**

- "OAuth 2.0 Security Best Practices" — лучшие практики безопасности OAuth
- "JWT Security Best Practices" — лучшие практики безопасности JWT

---



