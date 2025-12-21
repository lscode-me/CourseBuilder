# Основы аутентификации и авторизации
## Authentication vs Authorization, API Keys, Basic Auth и OAuth

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы API и интеграции
- Знать типы API и форматы данных
- Иметь представление о HTTP протоколе и заголовках

**Recommended prior modules:**

- [01_What_is_API](../01_What_is_API/) — основы API и интеграции
- [04_Data_Formats](../04_Data_Formats/) — форматы данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать аутентификацию и авторизацию
- Применять API Keys для простой аутентификации
- Использовать Basic Authentication
- Понимать концепцию OAuth и его основные компоненты
- Выбирать подходящий метод аутентификации для конкретной задачи

---

## 1. Authentication vs Authorization

**Аутентификация (Authentication)** и **Авторизация (Authorization)** — это разные, но связанные концепции безопасности.

### 1.1 Authentication (Аутентификация)

**Authentication** отвечает на вопрос: "Кто ты?" — это процесс проверки личности пользователя или системы.

**Example: Процесс аутентификации**

```python

def authenticate(username, password):
    """Аутентификация — проверка личности"""
    # Проверка: существует ли пользователь и правильный ли пароль
    user = get_user_by_username(username)
    if user and verify_password(password, user.hashed_password):
        return user  # Пользователь аутентифицирован
    return None  # Аутентификация не удалась

# Аутентификация
user = authenticate("ivan", "password123")
if user:
    print(f"Пользователь {user.username} аутентифицирован")
else:
    print("Неверные учётные данные")
```

**Output:**
```

Пользователь ivan аутентифицирован
```

### 1.2 Authorization (Авторизация)

**Authorization** отвечает на вопрос: "Что тебе разрешено?" — это процесс проверки прав доступа к ресурсам.

**Example: Процесс авторизации**

```python

def authorize(user, resource, action):
    """Авторизация — проверка прав доступа"""
    # Проверка: имеет ли пользователь право на действие
    permissions = get_user_permissions(user.id)
    
    required_permission = f"{resource}:{action}"
    if required_permission in permissions:
        return True  # Доступ разрешён
    return False  # Доступ запрещён

# Авторизация
user = authenticate("ivan", "password123")
if user:
    # Пользователь аутентифицирован, проверяем права
    if authorize(user, "users", "read"):
        print("Доступ к чтению пользователей разрешён")
    else:
        print("Доступ запрещён")
```

**Output:**
```

Доступ к чтению пользователей разрешён
```

### 1.3 Различие

**Ключевое различие:**

| Концепция | Вопрос | Проверяет |
|-----------|--------|-----------|
| **Authentication** | Кто ты? | Личность |
| **Authorization** | Что тебе разрешено? | Права доступа |

**Последовательность:**

1. Сначала **Authentication** — проверяем, кто пользователь
2. Затем **Authorization** — проверяем, что ему разрешено

---

## 2. API Keys

**API Keys** — это простой метод аутентификации через уникальный ключ, передаваемый в запросе.

### 2.1 Концепция API Keys

API Key — это секретный ключ, который идентифицирует клиента API. Ключ передаётся в каждом запросе.

**Example: Использование API Key**

```python

import requests

# API Key передаётся в заголовке или параметре запроса
api_key = "sk_live_1234567890abcdef"

# Вариант 1: В заголовке (рекомендуется)
headers = {
    "X-API-Key": api_key,
    "Content-Type": "application/json"
}
response = requests.get(
    "https://api.example.com/users",
    headers=headers
)

# Вариант 2: В параметре запроса
response = requests.get(
    "https://api.example.com/users",
    params={"api_key": api_key}
)

print(f"Status: {response.status_code}")
```

**Output:**
```

Status: 200
```

### 2.2 Генерация и хранение API Keys

**Example: Генерация API Key**

```python

import secrets
import hashlib

def generate_api_key():
    """Генерация безопасного API ключа"""
    # Генерация случайного ключа
    api_key = secrets.token_urlsafe(32)
    return api_key

def hash_api_key(api_key):
    """Хеширование API ключа для хранения"""
    return hashlib.sha256(api_key.encode()).hexdigest()

def verify_api_key(provided_key, stored_hash):
    """Проверка API ключа"""
    provided_hash = hash_api_key(provided_key)
    return provided_hash == stored_hash

# Генерация ключа
api_key = generate_api_key()
print(f"Generated API Key: {api_key}")

# Хеширование для хранения
hashed_key = hash_api_key(api_key)
print(f"Hashed (for storage): {hashed_key}")

# Проверка ключа
is_valid = verify_api_key(api_key, hashed_key)
print(f"Key valid: {is_valid}")
```

**Output:**
```

Generated API Key: abc123xyz...
Hashed (for storage): 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d
Key valid: True
```

### 2.3 Валидация API Key на сервере

**Example: Валидация API Key в API**

```python

from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище API ключей (в реальности — база данных)
valid_api_keys = {
    "sk_live_1234567890abcdef": {"user_id": 123, "permissions": ["read", "write"]},
    "sk_test_abcdef1234567890": {"user_id": 456, "permissions": ["read"]}
}

def validate_api_key():
    """Валидация API ключа из запроса"""
    api_key = request.headers.get("X-API-Key") or request.args.get("api_key")
    
    if not api_key:
        return None, "API key missing"
    
    if api_key not in valid_api_keys:
        return None, "Invalid API key"
    
    return valid_api_keys[api_key], None

@app.route("/api/users", methods=["GET"])
def get_users():
    """Endpoint с проверкой API ключа"""
    user_info, error = validate_api_key()
    
    if error:
        return jsonify({"error": error}), 401
    
    # API ключ валиден, возвращаем данные
    return jsonify({
        "users": [
            {"id": 1, "name": "Иван"},
            {"id": 2, "name": "Мария"}
        ]
    }), 200
```

### 2.4 Преимущества и ограничения API Keys

**Преимущества:**

- Простота использования
- Легко реализовать
- Подходит для простых сценариев

**Ограничения:**

- Ключ передаётся в каждом запросе (риск перехвата)
- Нет встроенного механизма отзыва
- Ограниченная гибкость для сложных сценариев

---

## 3. Basic Authentication

**Basic Authentication** — это простой метод аутентификации через HTTP заголовок, использующий кодирование username:password в Base64.

### 3.1 Концепция Basic Auth

Basic Auth кодирует username и password в Base64 и передаёт в заголовке `Authorization`.

**Example: Basic Auth на клиенте**

```python

import requests
import base64

def basic_auth_header(username, password):
    """Создание Basic Auth заголовка"""
    credentials = f"{username}:{password}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"

# Использование Basic Auth
username = "ivan"
password = "password123"

headers = {
    "Authorization": basic_auth_header(username, password)
}

response = requests.get(
    "https://api.example.com/users",
    headers=headers
)

print(f"Status: {response.status_code}")
```

**Output:**
```

Status: 200
```

### 3.2 Basic Auth на сервере

**Example: Обработка Basic Auth на сервере**

```python

from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Хранилище пользователей (в реальности — база данных)
users = {
    "ivan": "password123",
    "maria": "securepass456"
}

def decode_basic_auth():
    """Декодирование Basic Auth заголовка"""
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Basic "):
        return None, None
    
    # Извлечение закодированных учётных данных
    encoded = auth_header.split(" ")[1]
    decoded = base64.b64decode(encoded).decode()
    username, password = decoded.split(":", 1)
    
    return username, password

@app.route("/api/users", methods=["GET"])
def get_users():
    """Endpoint с Basic Auth"""
    username, password = decode_basic_auth()
    
    if not username or not password:
        return jsonify({"error": "Authentication required"}), 401
    
    # Проверка учётных данных
    if username not in users or users[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Аутентификация успешна
    return jsonify({
        "users": [
            {"id": 1, "name": "Иван"},
            {"id": 2, "name": "Мария"}
        ]
    }), 200
```

### 3.3 Безопасность Basic Auth

**⚠️ Важно:** Basic Auth передаёт пароль в Base64 (не шифрование!). Обязательно использовать HTTPS.

**Example: Безопасное использование Basic Auth**

```python
# ❌ НЕБЕЗОПАСНО: HTTP
response = requests.get("http://api.example.com/users", headers=headers)

# ✅ БЕЗОПАСНО: HTTPS

response = requests.get("https://api.example.com/users", headers=headers)
```

**Ограничения Basic Auth:**

- Пароль передаётся в каждом запросе
- Base64 — это кодирование, не шифрование
- Нет механизма отзыва токенов
- Ограниченная гибкость

---

## 4. OAuth — общая идея

**OAuth** — это протокол авторизации, позволяющий приложению получать ограниченный доступ к ресурсам пользователя без передачи пароля.

### 4.1 Концепция OAuth

OAuth решает проблему: как дать приложению доступ к ресурсам без передачи пароля?

**Основные компоненты OAuth:**

- **Resource Owner** (Владелец ресурса) — пользователь

- **Client** (Клиент) — приложение, запрашивающее доступ

- **Authorization Server** (Сервер авторизации) — выдает токены

- **Resource Server** (Сервер ресурсов) — API, защищённое OAuth

### 4.2 OAuth Flow (упрощённый)

**Example: Упрощённый OAuth flow**

```python
# Шаг 1: Клиент запрашивает авторизацию
def request_authorization(client_id, redirect_uri, scope):
    """Запрос авторизации"""
    auth_url = f"https://auth.example.com/authorize"
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_type": "code"
    }
    return f"{auth_url}?{urlencode(params)}"

# Шаг 2: Пользователь авторизуется и получает код
authorization_code = "abc123xyz"

# Шаг 3: Клиент обменивает код на токен
def exchange_code_for_token(authorization_code, client_id, client_secret):
    """Обмен кода на токен доступа"""
    token_url = "https://auth.example.com/token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(token_url, data=data)
    return response.json()["access_token"]

# Шаг 4: Использование токена для доступа к API
def access_api_with_token(access_token):
    """Доступ к API с токеном"""
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get("https://api.example.com/users", headers=headers)
    return response.json()

# Использование

access_token = exchange_code_for_token(
    authorization_code,
    client_id="my_app",
    client_secret="secret"
)

users = access_api_with_token(access_token)
print(f"Users: {users}")
```

### 4.3 Преимущества OAuth

**OAuth обеспечивает:**

- Безопасность: пароль не передаётся приложению
- Гибкость: можно ограничить доступ (scopes)
- Отзыв токенов: можно отозвать доступ
- Делегирование: пользователь даёт доступ приложению

### 4.4 OAuth Scopes

**Scopes** определяют, какие действия разрешены токену.

**Example: OAuth Scopes**

```python
# Scopes определяют права доступа
scopes = {
    "read:users": "Чтение данных пользователей",
    "write:users": "Создание/изменение пользователей",
    "delete:users": "Удаление пользователей"
}

# Токен с ограниченными правами
token_with_read_only = {
    "access_token": "token123",
    "scope": "read:users"  # Только чтение
}

# Проверка scope при доступе
def check_scope(token, required_scope):
    """Проверка scope токена"""
    token_scopes = token["scope"].split()
    return required_scope in token_scopes

# Использование
if check_scope(token_with_read_only, "read:users"):
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
```

**Output:**
```

Доступ разрешён
```

---

## 5. Сравнение методов аутентификации

### 5.1 Сравнительная таблица

| Метод | Сложность | Безопасность | Использование |
|-------|-----------|--------------|---------------|
| **API Keys** | Низкая | Средняя | Простые API, сервер-сервер |
| **Basic Auth** | Низкая | Низкая (только с HTTPS) | Простые сценарии |
| **OAuth** | Высокая | Высокая | Публичные API, делегирование доступа |

### 5.2 Выбор метода

**Используйте API Keys если:**

- Простой API для сервер-сервер коммуникации
- Не нужна гибкость в управлении доступом
- Простота важнее безопасности

**Используйте Basic Auth если:**

- Простые сценарии с одним пользователем
- Обязательно с HTTPS
- Временное решение

**Используйте OAuth если:**

- Публичный API с множественными клиентами
- Нужно делегирование доступа
- Требуется гибкое управление правами
- Высокие требования к безопасности

---

## 6. Практические примеры

### 6.1 Пример: API с API Key

```python

class APIKeyAuth:
    """Аутентификация через API Key"""
    
    def __init__(self):
        self.api_keys = {}
    
    def register_key(self, key, user_id, permissions):
        """Регистрация API ключа"""
        self.api_keys[key] = {
            "user_id": user_id,
            "permissions": permissions
        }
    
    def validate_key(self, api_key):
        """Валидация API ключа"""
        return self.api_keys.get(api_key)

# Использование

auth = APIKeyAuth()
auth.register_key("sk_123", user_id=1, permissions=["read", "write"])

user_info = auth.validate_key("sk_123")
if user_info:
    print(f"User {user_info['user_id']} authenticated")
```

**Output:**
```

User 1 authenticated
```

---

## 7. Common Pitfalls

### 7.1 Pitfall: API Key в URL

❌ **Incorrect:**
```python
# API Key в URL — виден в логах и истории браузера

response = requests.get(f"https://api.example.com/users?api_key={api_key}")
```

✅ **Correct:**
```python
# API Key в заголовке

headers = {"X-API-Key": api_key}
response = requests.get("https://api.example.com/users", headers=headers)
```

**Why:** API Key в URL попадает в логи сервера и историю браузера.

### 7.2 Pitfall: Basic Auth без HTTPS

❌ **Incorrect:**
```python
# HTTP — пароль может быть перехвачен

response = requests.get("http://api.example.com/users", auth=("user", "pass"))
```

✅ **Correct:**
```python
# HTTPS — зашифрованное соединение
response = requests.get("https://api.example.com/users", auth=("user", "pass"))
```

**Why:** Без HTTPS пароль передаётся в открытом виде и может быть перехвачен.

### 7.3 Pitfall: Смешивание Authentication и Authorization

❌ **Incorrect:**
```python

def check_access(api_key):
    # Смешивание: проверка и личности, и прав одновременно
    if api_key == "admin_key":
        return "admin"
    return None
```

✅ **Correct:**
```python

def authenticate(api_key):
    # Сначала аутентификация
    user = get_user_by_api_key(api_key)
    return user

def authorize(user, resource, action):
    # Затем авторизация
    return check_permission(user, resource, action)
```

**Why:** Authentication и Authorization — разные этапы. Сначала проверяем личность, затем права.

---

## 💡 Key Takeaways

- **Authentication vs Authorization**: Authentication проверяет "кто ты", Authorization проверяет "что тебе разрешено". Это разные, но связанные этапы безопасности

- **API Keys**: Простой метод аутентификации через уникальный ключ. Подходит для сервер-сервер коммуникации, но требует защиты ключа

- **Basic Auth**: Простой метод через username:password в Base64. Используется только с HTTPS, подходит для простых сценариев

- **OAuth**: Протокол авторизации для делегирования доступа без передачи пароля. Обеспечивает гибкость и безопасность через токены и scopes

- **Выбор метода**: API Keys для простых API, Basic Auth для простых сценариев (только с HTTPS), OAuth для публичных API с требованиями безопасности и гибкости

---

## 🚀 Next Steps

**Related Modules:**

- [13_API_Security](../13_API_Security/) — продвинутая безопасность API: OAuth 2.0, JWT, scopes
- [06_API_Standards](../06_API_Standards/) — стандарты API
- [07_API_Design](../07_API_Design/) — проектирование API

**Practice Ideas:**

1. Реализуйте API с аутентификацией через API Key
2. Создайте систему с Basic Auth (обязательно с HTTPS)
3. Изучите OAuth 2.0 flow на практике

**Going Deeper:**

- OAuth 2.0 Specification: полная спецификация OAuth 2.0
- JWT (JSON Web Tokens): токены для аутентификации
- API Security Best Practices: лучшие практики безопасности API

---

## 📚 Additional Resources

**Documentation:**

- [OAuth 2.0 RFC](https://oauth.net/2/) — спецификация OAuth 2.0
- [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) — документация Basic Auth

**Articles:**

- "Understanding OAuth 2.0" — понимание OAuth 2.0
- "API Key vs OAuth: When to Use What" — сравнение методов аутентификации

---


