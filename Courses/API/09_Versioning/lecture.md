# Версионирование и совместимость
## Зачем нужно версионирование, Backward compatibility, Deprecation стратегии, Breaking changes

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать проектирование API
- Знать основы REST и HTTP
- Иметь представление о контрактах API

**Recommended prior modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [01_What_is_API](../01_What_is_API/) — основы API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать зачем нужно версионирование API
- Обеспечивать backward compatibility при изменениях
- Применять deprecation стратегии для плавного перехода
- Управлять breaking changes безопасно
- Выбирать стратегию версионирования для конкретного API

---

## 1. Зачем нужно версионирование

API развиваются со временем. Версионирование позволяет вносить изменения, не ломая существующих клиентов.

### 1.1 Проблема без версионирования

**Example: Проблема изменения API**

```python
# Версия 1: API возвращает

{
  "id": 123,
  "name": "Иван",
  "email": "ivan@example.com"
}

# Версия 2: API изменён (добавлено поле)

{
  "id": 123,
  "name": "Иван",
  "email": "ivan@example.com",
  "phone": "+1234567890"  # Новое поле
}

# Клиент версии 1 ожидает только id, name, email
# Но получает phone — это может сломать клиента!
```

### 1.2 Решение через версионирование

**Example: Версионирование в URI**

```python
# Версия 1

GET /api/v1/users/123
# Возвращает: {"id": 123, "name": "Иван", "email": "ivan@example.com"}

# Версия 2

GET /api/v2/users/123
# Возвращает: {"id": 123, "name": "Иван", "email": "ivan@example.com", "phone": "+1234567890"}

# Клиенты версии 1 продолжают работать с /api/v1
# Новые клиенты используют /api/v2
```

---

## 2. Backward Compatibility

**Backward Compatibility** означает, что новая версия API совместима со старой — старые клиенты продолжают работать.

### 2.1 Обратно совместимые изменения

**Example: Обратно совместимые изменения**

```python
# Добавление новых полей (обратно совместимо)
# Старый клиент игнорирует новые поля

{
  "id": 123,
  "name": "Иван",
  "email": "ivan@example.com",
  "phone": "+1234567890"  # Новое поле — старый клиент игнорирует
}

# Добавление новых endpoints (обратно совместимо)

GET /api/v1/users/123/orders  # Новый endpoint

# Добавление новых query параметров (обратно совместимо)

GET /api/v1/users?status=active  # Новый параметр опционален
```

### 2.2 Несовместимые изменения

**Example: Breaking changes**

```python
# ❌ Удаление поля (breaking change)
# Было: {"id": 123, "name": "Иван", "email": "ivan@example.com"}
# Стало: {"id": 123, "name": "Иван"}  # email удалён — сломает клиента!

# ❌ Изменение типа поля (breaking change)
# Было: {"age": "30"}  # строка
# Стало: {"age": 30}   # число — сломает клиента!

# ❌ Изменение обязательности поля (breaking change)
# Было: {"name": "Иван"}  # email опционален
# Стало: {"name": "Иван", "email": "required"}  # email обязателен — сломает клиента!
```

---

## 3. Deprecation стратегии

**Deprecation** — это процесс уведомления о том, что функция/версия будет удалена в будущем.

### 3.1 Процесс deprecation

**Example: Deprecation процесс**

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_v1(user_id):
    """Версия 1 — deprecated"""
    # Уведомление о deprecation в заголовках
    response = jsonify({
        "id": user_id,
        "name": "Иван",
        "email": "ivan@example.com"
    })
    
    # Deprecation заголовки
    response.headers["Deprecation"] = "true"
    response.headers["Sunset"] = (datetime.now() + timedelta(days=365)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    response.headers["Link"] = '</api/v2/users/{user_id}>; rel="successor-version"'
    
    return response, 200

@app.route("/api/v2/users/<int:user_id>", methods=["GET"])
def get_user_v2(user_id):
    """Версия 2 — текущая"""
    return jsonify({
        "id": user_id,
        "name": "Иван",
        "email": "ivan@example.com",
        "phone": "+1234567890"
    }), 200
```

### 3.2 Timeline deprecation

**Рекомендуемый timeline:**

1. **Объявление**: Уведомление о deprecation (6-12 месяцев до удаления)
2. **Предупреждения**: Логирование использования deprecated функций
3. **Удаление**: Удаление после достаточного времени миграции

---

## 4. Breaking Changes

**Breaking Changes** — это изменения, которые ломают существующих клиентов.

### 4.1 Типы breaking changes

**Example: Категории breaking changes**

```python
# 1. Удаление endpoint
# ❌ Было: GET /api/v1/users/123/orders
# ❌ Стало: Endpoint удалён

# 2. Изменение структуры ответа
# ❌ Было: {"user": {"id": 123, "name": "Иван"}}
# ❌ Стало: {"id": 123, "name": "Иван"}  # Структура изменена

# 3. Изменение типа данных
# ❌ Было: {"age": "30"}  # строка
# ❌ Стало: {"age": 30}   # число

# 4. Изменение обязательности полей
# ❌ Было: {"name": "Иван"}  # email опционален
# ❌ Стало: {"name": "Иван", "email": "required"}  # email обязателен
```

### 4.2 Управление breaking changes

**Стратегия:**

1. Создать новую версию API
2. Поддерживать старую версию параллельно
3. Deprecate старую версию
4. Удалить после миграции клиентов

---

## 5. Стратегии версионирования

### 5.1 Версионирование в URI

**Example: URI версионирование**

```python
# Версии в URI

GET /api/v1/users/123
GET /api/v2/users/123
GET /api/v3/users/123

# Преимущества: Явное, понятное
# Недостатки: Загрязняет URI
```

### 5.2 Версионирование в заголовках

**Example: Заголовок версионирования**

```python
# Версия в заголовке Accept

GET /api/users/123
Headers: Accept: application/vnd.api.v1+json

# Преимущества: Чистые URI
# Недостатки: Менее явное
```

### 5.3 Выбор стратегии

**Используйте URI версионирование если:**

- Нужна явность
- Простота важнее чистоты URI
- Много breaking changes

**Используйте заголовок версионирования если:**

- Важны чистые URI
- Минимум breaking changes
- RESTful принципы критичны

---

## 6. Best Practices

### 6.1 Семантическое версионирование

**Example: Semantic Versioning**

```python
# MAJOR.MINOR.PATCH
# v1.0.0 -> v1.1.0 (minor: обратно совместимые изменения)
# v1.1.0 -> v2.0.0 (major: breaking changes)

# API версионирование обычно использует только MAJOR

GET /api/v1/users
GET /api/v2/users
```

### 6.2 Поддержка нескольких версий

**Example: Параллельная поддержка версий**

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

class VersionManager:
    """Управление версиями API"""
    
    def __init__(self):
        self.versions = {
            "v1": {
                "status": "deprecated",
                "sunset_date": datetime.now() + timedelta(days=180),
                "handler": self.handle_v1
            },
            "v2": {
                "status": "current",
                "handler": self.handle_v2
            },
            "v3": {
                "status": "beta",
                "handler": self.handle_v3
            }
        }
    
    def get_version(self, version):
        """Получение информации о версии"""
        return self.versions.get(version)
    
    def handle_v1(self, user_id):
        """Обработчик версии 1"""
        return {"id": user_id, "name": "Иван", "email": "ivan@example.com"}
    
    def handle_v2(self, user_id):
        """Обработчик версии 2"""
        return {
            "id": user_id,
            "name": "Иван",
            "email": "ivan@example.com",
            "phone": "+1234567890"
        }
    
    def handle_v3(self, user_id):
        """Обработчик версии 3 (beta)"""
        return {
            "id": user_id,
            "name": "Иван",
            "email": "ivan@example.com",
            "phone": "+1234567890",
            "preferences": {}
        }

version_manager = VersionManager()

@app.route("/api/<version>/users/<int:user_id>", methods=["GET"])
def get_user(version, user_id):
    """Endpoint с версионированием"""
    version_info = version_manager.get_version(version)
    
    if not version_info:
        return jsonify({"error": "Unknown version"}), 404
    
    # Проверка deprecation
    if version_info["status"] == "deprecated":
        sunset_date = version_info["sunset_date"]
        response = jsonify(version_info["handler"](user_id))
        response.headers["Deprecation"] = "true"
        response.headers["Sunset"] = sunset_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
        response.headers["Link"] = f'</api/v2/users/{user_id}>; rel="successor-version"'
        return response, 200
    
    return jsonify(version_info["handler"](user_id)), 200
```

### 6.3 Автоматическое определение версии

**Example: Определение версии из заголовка**

```python
from flask import request

def get_api_version():
    """Определение версии API из заголовка"""
    accept_header = request.headers.get("Accept", "")
    
    # Парсинг Accept: application/vnd.api.v1+json
    if "vnd.api.v1" in accept_header:
        return "v1"
    elif "vnd.api.v2" in accept_header:
        return "v2"
    elif "vnd.api.v3" in accept_header:
        return "v3"
    
    # По умолчанию последняя стабильная версия
    return "v2"

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user_versioned(user_id):
    """Endpoint с автоматическим определением версии"""
    version = get_api_version()
    version_info = version_manager.get_version(version)
    return jsonify(version_info["handler"](user_id)), 200
```

### 6.4 Миграция данных между версиями

**Example: Миграция данных для совместимости**

```python
class DataMigrator:
    """Миграция данных между версиями"""
    
    def migrate_to_v2(self, v1_data):
        """Миграция из v1 в v2"""
        return {
            "id": v1_data["id"],
            "name": v1_data["name"],
            "email": v1_data["email"],
            "phone": None  # Новое поле с дефолтным значением
        }
    
    def migrate_to_v1(self, v2_data):
        """Миграция из v2 в v1 (для обратной совместимости)"""
        return {
            "id": v2_data["id"],
            "name": v2_data["name"],
            "email": v2_data["email"]
            # phone удаляется
        }

migrator = DataMigrator()

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_v1(user_id):
    """Версия 1 с миграцией из v2"""
    # Получаем данные из БД (хранятся в формате v2)
    v2_data = db.get_user(user_id)
    
    # Мигрируем в формат v1
    v1_data = migrator.migrate_to_v1(v2_data)
    
    return jsonify(v1_data), 200
```

## 7. Common Pitfalls

### 7.1 Pitfall: Отсутствие версионирования при breaking changes

❌ **Incorrect:**
```python
# Плохо: Изменение API без версионирования
# Было: GET /api/users/123 -> {"id": 123, "name": "Иван"}
# Стало: GET /api/users/123 -> {"id": 123, "name": "Иван", "email": "ivan@example.com"}
# Клиенты, ожидающие только id и name, могут сломаться
```

✅ **Correct:**
```python
# Хорошо: Версионирование при breaking changes
# v1: GET /api/v1/users/123 -> {"id": 123, "name": "Иван"}
# v2: GET /api/v2/users/123 -> {"id": 123, "name": "Иван", "email": "ivan@example.com"}
# Старые клиенты продолжают работать с v1
```

**Why:** Версионирование защищает существующих клиентов.

### 7.2 Pitfall: Слишком короткий период deprecation

❌ **Incorrect:**
```python
# Плохо: Deprecation на 1 месяц

sunset_date = datetime.now() + timedelta(days=30)  # Слишком мало времени
```

✅ **Correct:**
```python
# Хорошо: Deprecation на 6-12 месяцев

sunset_date = datetime.now() + timedelta(days=180)  # Достаточно времени для миграции
```

**Why:** Клиентам нужно время для миграции.

### 7.3 Pitfall: Удаление версии без deprecation

❌ **Incorrect:**
```python
# Плохо: Удаление версии без предупреждения

if version == "v1":
    return 404  # Неожиданно для клиентов
```

✅ **Correct:**
```python
# Хорошо: Deprecation перед удалением

if version == "v1":
    if datetime.now() < sunset_date:
        # Deprecated, но ещё работает
        response = handle_v1()
        response.headers["Deprecation"] = "true"
        return response
    else:
        # Удалено после sunset date
        return 410  # Gone
```

**Why:** Deprecation даёт клиентам время подготовиться.

---

## 💡 Key Takeaways

- **Версионирование необходимо**: API развиваются, версионирование позволяет вносить изменения без поломки клиентов

- **Backward Compatibility**: Обратно совместимые изменения (добавление полей, endpoints) не ломают старых клиентов

- **Deprecation стратегии**: Процесс уведомления о будущем удалении с достаточным временем для миграции (6-12 месяцев)

- **Breaking Changes**: Изменения, ломающие клиентов, требуют новой версии API и параллельной поддержки старой версии

- **Стратегии версионирования**: URI версионирование (явное) или заголовки (чистые URI). Выбор зависит от требований

---

## 🚀 Next Steps

**Related Modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [10_Contracts_Documentation](../10_Contracts_Documentation/) — контракты и документация
- [17_Enterprise_Integrations](../17_Enterprise_Integrations/) — enterprise интеграции

**Practice Ideas:**

1. Создайте API с версионированием в URI
2. Реализуйте deprecation процесс для старой версии
3. Управляйте breaking changes через новую версию

**Going Deeper:**

- Semantic Versioning: полное руководство по версионированию
- API Versioning Strategies: стратегии версионирования API
- Managing Breaking Changes: управление breaking changes

---

## 📚 Additional Resources

**Documentation:**

- [Semantic Versioning](https://semver.org/) — спецификация версионирования
- [HTTP Deprecation Header](https://tools.ietf.org/html/draft-ietf-httpapi-deprecation-header) — стандарт deprecation

**Articles:**

- "API Versioning Best Practices" — лучшие практики версионирования
- "Managing Breaking Changes in APIs" — управление breaking changes

---




