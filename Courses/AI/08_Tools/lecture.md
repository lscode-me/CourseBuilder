# Tool Usage и Function Calling
## Расширение возможностей LLM через инструменты

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [05_Prompt_Basics](../05_Prompt_Basics/) — базовый промптинг
- Понимать API взаимодействие с LLM
- Иметь опыт работы с JSON

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить концепцию tool use и function calling
- Определять функции для LLM
- Реализовывать базовый tool-calling pipeline
- Понимать границы ответственности модели
- Проектировать безопасные инструменты

---

## 1. Зачем нужны инструменты

### 1.1 Ограничения LLM

```

┌─────────────────────────────────────────────────────────────┐
│          Что LLM НЕ может делать сам                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ❌ Актуальная информация                                   │
│     Не знает текущую дату, погоду, новости                  │
│                                                              │
│  ❌ Точные вычисления                                       │
│     Арифметика ненадёжна                                    │
│                                                              │
│  ❌ Взаимодействие с миром                                  │
│     Не может отправить email, сделать бронирование          │
│                                                              │
│  ❌ Доступ к данным                                         │
│     Не видит ваши файлы, БД, API                            │
│                                                              │
│  Tools решают эти проблемы!                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Концепция Tool Use

Tool use (function calling) — способность LLM вызывать внешние функции:

```

┌─────────────────────────────────────────────────────────────┐
│                   Tool Use Flow                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. User: "Какая погода в Москве?"                          │
│                    │                                         │
│                    ▼                                         │
│  2. LLM: "Нужно вызвать get_weather(city='Moscow')"         │
│                    │                                         │
│                    ▼                                         │
│  3. System: Вызывает реальную функцию get_weather()         │
│                    │                                         │
│                    ▼                                         │
│  4. Result: {"temp": 15, "condition": "cloudy"}             │
│                    │                                         │
│                    ▼                                         │
│  5. LLM: "В Москве 15°C, облачно"                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Function Calling в OpenAI

### 2.1 Определение функций

```python

from openai import OpenAI
client = OpenAI()

# Определяем доступные функции
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather in a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, e.g. 'Moscow'"
                    },
                    "units": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature units"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to a recipient",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string", "description": "Recipient email"},
                    "subject": {"type": "string", "description": "Email subject"},
                    "body": {"type": "string", "description": "Email body"}
                },
                "required": ["to", "subject", "body"]
            }
        }
    }
]
```

### 2.2 Базовый pipeline

```python

import json

def process_with_tools(user_message):
    messages = [{"role": "user", "content": user_message}]
    
    # Шаг 1: Отправляем запрос с tools
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools
    )
    
    message = response.choices[0].message
    
    # Шаг 2: Проверяем, хочет ли модель вызвать функцию
    if message.tool_calls:
        # Выполняем каждый вызов
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            # Шаг 3: Вызываем реальную функцию
            result = execute_function(function_name, arguments)
            
            # Шаг 4: Добавляем результат в контекст
            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
        
        # Шаг 5: Получаем финальный ответ
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return final_response.choices[0].message.content
    
    return message.content

def execute_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    elif name == "send_email":
        return send_email(**args)
    raise ValueError(f"Unknown function: {name}")
```

### 2.3 Реальные функции

```python

import requests

def get_weather(city: str, units: str = "celsius") -> dict:
    """Реальный вызов weather API"""
    api_key = "your_api_key"
    url = f"https://api.weatherapi.com/v1/current.json"
    response = requests.get(url, params={"key": api_key, "q": city})
    data = response.json()
    return {
        "city": city,
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }

def send_email(to: str, subject: str, body: str) -> dict:
    """Отправка email (пример)"""
    # В реальности используйте SMTP или сервис вроде SendGrid
    print(f"Sending email to {to}: {subject}")
    return {"status": "sent", "to": to}
```

---

## 3. Parallel Function Calling

### 3.1 Множественные вызовы

LLM может запросить несколько функций одновременно:

```python
# User: "Какая погода в Москве и Париже?"

# Модель вернёт два tool_calls:
# 1. get_weather(city="Moscow")
# 2. get_weather(city="Paris")

# Можно выполнить параллельно!
import asyncio

async def process_parallel_tools(tool_calls):
    tasks = []
    for call in tool_calls:
        name = call.function.name
        args = json.loads(call.function.arguments)
        tasks.append(execute_function_async(name, args))
    
    results = await asyncio.gather(*tasks)
    return results
```

---

## 4. Границы ответственности

### 4.1 Что делает LLM vs что делает код

```

┌─────────────────────────────────────────────────────────────┐
│              Разделение ответственности                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  LLM отвечает за:                                           │
│  ✅ Понимание intent пользователя                           │
│  ✅ Выбор нужной функции                                    │
│  ✅ Извлечение параметров из запроса                        │
│  ✅ Формулировка ответа пользователю                        │
│                                                              │
│  Код отвечает за:                                           │
│  ✅ Выполнение функции                                      │
│  ✅ Валидация параметров                                    │
│  ✅ Обработка ошибок                                        │
│  ✅ Безопасность и авторизация                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Валидация и безопасность

```python

def execute_function_safe(name: str, args: dict, user_context: dict):
    """Безопасное выполнение функции"""
    
    # 1. Проверяем, что функция разрешена
    allowed_functions = ["get_weather", "search_products"]
    if name not in allowed_functions:
        raise PermissionError(f"Function {name} not allowed")
    
    # 2. Валидируем параметры
    if name == "send_email":
        # Проверяем, что пользователь авторизован отправлять email
        if not user_context.get("can_send_email"):
            raise PermissionError("User not authorized to send emails")
        
        # Проверяем получателя
        if not is_valid_email(args.get("to")):
            raise ValueError("Invalid email address")
    
    # 3. Логируем вызов
    log_function_call(name, args, user_context)
    
    # 4. Выполняем
    return execute_function(name, args)
```

---

## 5. Примеры использования

### 5.1 Калькулятор

```python

tools_calculator = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate a mathematical expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression, e.g. '2 + 2 * 3'"
                }
            },
            "required": ["expression"]
        }
    }
}]

def calculate(expression: str) -> dict:
    """Безопасное вычисление выражения"""
    # Используем ast.literal_eval или numexpr для безопасности
    import numexpr
    result = numexpr.evaluate(expression).item()
    return {"expression": expression, "result": result}
```

### 5.2 Поиск в базе данных

```python

tools_database = [{
    "type": "function",
    "function": {
        "name": "search_products",
        "description": "Search products in database",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "category": {"type": "string", "description": "Product category"},
                "max_price": {"type": "number", "description": "Maximum price"}
            },
            "required": ["query"]
        }
    }
}]

def search_products(query: str, category: str = None, max_price: float = None):
    """Поиск в реальной БД"""
    sql = "SELECT * FROM products WHERE name ILIKE %s"
    params = [f"%{query}%"]
    
    if category:
        sql += " AND category = %s"
        params.append(category)
    if max_price:
        sql += " AND price <= %s"
        params.append(max_price)
    
    return db.execute(sql, params).fetchall()
```

---

## 6. Best Practices

### 6.1 Проектирование функций

```python

function_design_tips = {
    "Naming": "Используйте глаголы: get_weather, send_email, create_order",
    "Description": "Пишите чёткие описания — LLM их читает!",
    "Parameters": "Минимум необходимых, с описаниями",
    "Granularity": "Одна функция = одно действие",
    "Idempotency": "По возможности делайте функции идемпотентными"
}
```

### 6.2 Обработка ошибок

```python

def execute_with_error_handling(name, args):
    try:
        result = execute_function(name, args)
        return {"success": True, "result": result}
    except ValueError as e:
        return {"success": False, "error": f"Invalid input: {e}"}
    except PermissionError as e:
        return {"success": False, "error": f"Permission denied: {e}"}
    except Exception as e:
        return {"success": False, "error": "Internal error occurred"}
```

---

## 💡 Key Takeaways

- **Tools расширяют LLM** — дают доступ к актуальным данным, вычислениям и действиям в реальном мире

- **LLM решает ЧТО, код решает КАК** — модель выбирает функцию и параметры, код выполняет и валидирует

- **Безопасность на стороне кода** — никогда не доверяйте input от LLM без валидации

- **Хорошие описания критичны** — LLM выбирает функцию по описанию, пишите их тщательно

---

## 🚀 Next Steps

**Related Modules:**

- [09_MCP](../09_MCP/) — Model Context Protocol
- [10_Agents_Basics](../10_Agents_Basics/) — AI-агенты

---


