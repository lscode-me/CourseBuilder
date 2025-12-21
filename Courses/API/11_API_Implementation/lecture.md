# Реализация и интеграция API
## Реализация API по стандартам, интеграция нескольких систем, Data transformation, Mapping и адаптеры

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать проектирование API
- Знать стандарты API (REST, SOAP, GraphQL)
- Иметь представление о контрактах и форматах данных

**Recommended prior modules:**

- [07_API_Design](../07_API_Design/) — проектирование API
- [06_API_Standards](../06_API_Standards/) — API стандарты
- [10_Contracts_Documentation](../10_Contracts_Documentation/) — контракты и документация

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Реализовывать API согласно стандартам (REST, OpenAPI)
- Интегрировать несколько систем через API
- Выполнять преобразование данных между форматами
- Создавать адаптеры и mapping слои
- Управлять сложными интеграциями с множественными системами

---

## 1. Реализация API по стандартам

Реализация API должна следовать стандартам для обеспечения совместимости и поддерживаемости.

### 1.1 RESTful реализация

**Example: RESTful API реализация**

```python

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserList(Resource):
    """GET /api/users, POST /api/users"""
    
    def get(self):
        """Список пользователей"""
        users = get_all_users()
        return jsonify(users), 200
    
    def post(self):
        """Создать пользователя"""
        data = request.json
        user = create_user(data)
        return jsonify(user), 201

class User(Resource):
    """GET /api/users/{id}, PUT /api/users/{id}, DELETE /api/users/{id}"""
    
    def get(self, user_id):
        """Получить пользователя"""
        user = get_user(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "Not found"}), 404
    
    def put(self, user_id):
        """Обновить пользователя"""
        data = request.json
        user = update_user(user_id, data)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "Not found"}), 404
    
    def delete(self, user_id):
        """Удалить пользователя"""
        if delete_user(user_id):
            return "", 204
        return jsonify({"error": "Not found"}), 404

# Регистрация ресурсов
api.add_resource(UserList, '/api/users')
api.add_resource(User, '/api/users/<int:user_id>')
```

### 1.2 Следование стандартам

**Ключевые принципы:**

- Использовать правильные HTTP методы
- Возвращать правильные status codes
- Следовать REST принципам
- Валидировать по контракту

---

## 2. Интеграция нескольких систем

Интеграция нескольких систем требует координации и преобразования данных.

### 2.1 Интеграция через API

**Example: Интеграция CRM, Payment и Email систем**

```python

class SystemIntegration:
    """Интеграция нескольких систем"""
    
    def __init__(self, crm_api, payment_api, email_api):
        self.crm_api = crm_api
        self.payment_api = payment_api
        self.email_api = email_api
    
    def process_order(self, order_data):
        """Обработка заказа через несколько систем"""
        # 1. Создать заказ в CRM
        crm_order = self.crm_api.create_order(order_data)
        
        # 2. Создать платеж
        payment = self.payment_api.create_payment({
            "amount": crm_order["total"],
            "order_id": crm_order["id"]
        })
        
        # 3. Обновить заказ в CRM
        self.crm_api.update_order(crm_order["id"], {
            "payment_id": payment["id"],
            "status": "paid"
        })
        
        # 4. Отправить email
        self.email_api.send_email({
            "to": order_data["customer_email"],
            "subject": "Order Confirmation",
            "body": f"Your order {crm_order['id']} is confirmed"
        })
        
        return crm_order

# Использование
integration = SystemIntegration(crm_api, payment_api, email_api)
order = integration.process_order(order_data)
```

---

## 3. Data Transformation

Преобразование данных необходимо при интеграции систем с разными форматами.

### 3.1 Преобразование форматов

**Example: Преобразование данных**

```python

class DataTransformer:
    """Преобразование данных между форматами"""
    
    def transform_crm_to_payment(self, crm_order):
        """Преобразование формата CRM в формат Payment"""
        return {
            "amount": crm_order["total"],
            "currency": "USD",
            "customer_id": crm_order["customer"]["id"],
            "description": f"Order #{crm_order['id']}"
        }
    
    def transform_payment_to_crm(self, payment):
        """Преобразование формата Payment в формат CRM"""
        return {
            "payment_id": payment["id"],
            "payment_status": payment["status"],
            "payment_date": payment["created_at"]
        }
    
    def normalize_user_data(self, user_data):
        """Нормализация данных пользователя"""
        return {
            "id": user_data.get("id") or user_data.get("user_id"),
            "name": user_data.get("name") or user_data.get("full_name"),
            "email": user_data.get("email") or user_data.get("email_address")
        }

# Использование
transformer = DataTransformer()
payment_data = transformer.transform_crm_to_payment(crm_order)
```

### 3.2 Маппинг полей

**Example: Маппинг полей**

```python

class FieldMapper:
    """Маппинг полей между системами"""
    
    def __init__(self):
        self.mappings = {
            "crm_to_payment": {
                "total": "amount",
                "customer.id": "customer_id",
                "id": "order_id"
            },
            "payment_to_crm": {
                "id": "payment_id",
                "status": "payment_status"
            }
        }
    
    def map_fields(self, source_data, mapping_name):
        """Маппинг полей согласно правилам"""
        mapping = self.mappings[mapping_name]
        result = {}
        
        for source_field, target_field in mapping.items():
            value = self._get_nested_value(source_data, source_field)
            self._set_nested_value(result, target_field, value)
        
        return result
    
    def _get_nested_value(self, data, field_path):
        """Получить значение по пути (например, 'customer.id')"""
        keys = field_path.split(".")
        value = data
        for key in keys:
            value = value.get(key)
            if value is None:
                return None
        return value
    
    def _set_nested_value(self, data, field_path, value):
        """Установить значение по пути"""
        keys = field_path.split(".")
        current = data
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
```

---

## 4. Адаптеры

**Адаптеры** преобразуют интерфейс одной системы в интерфейс, ожидаемый другой системой.

### 4.1 Паттерн Adapter

**Example: Адаптер для интеграции**

```python

class LegacySystemAdapter:
    """Адаптер для legacy системы"""
    
    def __init__(self, legacy_api):
        self.legacy_api = legacy_api
    
    def get_user(self, user_id):
        """Адаптация legacy API к современному формату"""
        # Legacy API возвращает другой формат
        legacy_data = self.legacy_api.fetch_user(user_id)
        
        # Преобразование в современный формат
        return {
            "id": legacy_data["user_id"],
            "name": legacy_data["full_name"],
            "email": legacy_data["email_address"],
            "created_at": self._parse_legacy_date(legacy_data["date_created"])
        }
    
    def create_user(self, user_data):
        """Адаптация современного формата к legacy API"""
        # Преобразование в legacy формат
        legacy_data = {
            "user_id": user_data["id"],
            "full_name": user_data["name"],
            "email_address": user_data["email"]
        }
        
        return self.legacy_api.create_user(legacy_data)
    
    def _parse_legacy_date(self, date_str):
        """Парсинг legacy формата даты"""
        # Преобразование формата даты
        from datetime import datetime
        return datetime.strptime(date_str, "%Y%m%d").isoformat()
```

### 4.2 Использование адаптеров

**Example: Интеграция через адаптеры**

```python
# Современная система использует адаптер для legacy системы
legacy_adapter = LegacySystemAdapter(legacy_api)

# Современный код работает с адаптированным интерфейсом
user = legacy_adapter.get_user(123)
print(f"User: {user['name']}")  # Единый формат
```

---

## 5. Сложные интеграции

### 5.1 Оркестрация интеграций

**Example: Оркестрация нескольких систем**

```python

class IntegrationOrchestrator:
    """Оркестрация интеграций нескольких систем"""
    
    def __init__(self):
        self.systems = {}
        self.transformers = {}
    
    def register_system(self, name, api, transformer=None):
        """Регистрация системы"""
        self.systems[name] = api
        if transformer:
            self.transformers[name] = transformer
    
    def integrate(self, workflow):
        """Выполнение workflow интеграции"""
        results = {}
        
        for step in workflow:
            system_name = step["system"]
            action = step["action"]
            data = step.get("data", {})
            
            # Преобразование данных, если нужно
            if system_name in self.transformers:
                data = self.transformers[system_name].transform(data)
            
            # Выполнение действия
            system = self.systems[system_name]
            result = getattr(system, action)(data)
            results[step["name"]] = result
        
        return results

# Использование
orchestrator = IntegrationOrchestrator()
orchestrator.register_system("crm", crm_api)
orchestrator.register_system("payment", payment_api, payment_transformer)

workflow = [
    {"name": "create_order", "system": "crm", "action": "create_order", "data": order_data},
    {"name": "create_payment", "system": "payment", "action": "create_payment", "data": {}},
]

results = orchestrator.integrate(workflow)
```

---

## 6. Common Pitfalls

### 6.1 Pitfall: Игнорирование стандартов

❌ **Incorrect:**
```python
# Плохо: не следует REST стандартам
@app.route("/api/getUser", methods=["POST"])
def get_user():
    # POST для получения данных
    pass
```

✅ **Correct:**
```python
# Хорошо: следует REST стандартам
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # GET для получения данных
    pass
```

**Why:** Следование стандартам обеспечивает совместимость и понятность API.

### 6.2 Pitfall: Отсутствие преобразования данных

❌ **Incorrect:**
```python
# Плохо: прямое использование данных без преобразования
crm_order = crm_api.get_order(123)
payment_api.create_payment(crm_order)  # Форматы не совпадают!
```

✅ **Correct:**
```python
# Хорошо: преобразование данных
crm_order = crm_api.get_order(123)
payment_data = transformer.transform_crm_to_payment(crm_order)
payment_api.create_payment(payment_data)
```

**Why:** Системы могут использовать разные форматы данных, требуется преобразование.

---

## 💡 Key Takeaways

- **Реализация по стандартам**: API должны следовать стандартам (REST, OpenAPI) для обеспечения совместимости, понятности и поддерживаемости

- **Интеграция систем**: Интеграция нескольких систем требует координации, обработки ошибок и управления зависимостями между системами

- **Data Transformation**: Преобразование данных необходимо при интеграции систем с разными форматами. Маппинг полей упрощает преобразование

- **Адаптеры**: Паттерн Adapter преобразует интерфейс одной системы в интерфейс, ожидаемый другой, упрощая интеграцию legacy систем

- **Оркестрация**: Сложные интеграции требуют оркестрации workflow с преобразованием данных и управлением зависимостями между шагами

---

## 🚀 Next Steps

**Related Modules:**

- [08_Integration_Patterns](../08_Integration_Patterns/) — интеграционные паттерны
- [12_Advanced_Patterns](../12_Advanced_Patterns/) — продвинутые интеграционные паттерны
- [17_Enterprise_Integrations](../17_Enterprise_Integrations/) — enterprise интеграции

**Practice Ideas:**

1. Реализуйте RESTful API согласно стандартам
2. Интегрируйте несколько систем через API
3. Создайте адаптеры для преобразования данных

**Going Deeper:**

- Adapter Pattern: углублённое изучение паттерна Adapter
- Integration Patterns: паттерны интеграции систем
- Data Transformation Best Practices: лучшие практики преобразования данных

---

## 📚 Additional Resources

**Documentation:**

- [Flask-RESTful](https://flask-restful.readthedocs.io/) — RESTful API для Flask
- [Adapter Pattern](https://refactoring.guru/design-patterns/adapter) — паттерн Adapter

**Articles:**

- "API Integration Best Practices" — лучшие практики интеграции API
- "Data Transformation Patterns" — паттерны преобразования данных

---


