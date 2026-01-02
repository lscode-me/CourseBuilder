# Model Context Protocol (MCP)
## Стандарт интеграции AI с внешними системами

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [08_Tools](../08_Tools/) — понимать function calling
- Понимать концепцию API и интеграций
- Иметь представление об enterprise-системах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить проблему разрозненных интеграций
- Описать идею и архитектуру MCP
- Понимать роли MCP серверов и клиентов
- Оценивать значение MCP для enterprise-систем

---

## 1. Проблема разрозненных интеграций

### 1.1 Текущее состояние

Каждый AI-продукт создаёт свои интеграции:

```
┌─────────────────────────────────────────────────────────────┐
│          Проблема: N×M интеграций                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AI Clients          Integrations          Data Sources     │
│  ──────────          ────────────          ────────────     │
│                                                             │
│  ChatGPT ─────────┬─────────────────────── Slack            │
│     │             │                        │                │
│  Claude ──────────┼──────────┬──────────── GitHub           │
│     │             │          │             │                │
│  Cursor ──────────┼──────────┼──────────── Jira             │
│     │             │          │             │                │
│  Custom ──────────┴──────────┴──────────── Database         │
│                                                             │
│  Каждая пара = отдельная интеграция                         │
│  4 клиента × 4 источника = 16 интеграций!                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Проблемы текущего подхода

```python
integration_problems = {
    "Дублирование": "Каждый клиент реализует похожую логику",
    "Несовместимость": "Разные форматы, API, протоколы",
    "Сложность поддержки": "Обновление каждой интеграции отдельно",
    "Vendor lock-in": "Интеграции привязаны к конкретному AI",
    "Безопасность": "Разные модели доступа и авторизации"
}
```

---

## 2. Что такое MCP

### 2.1 Идея MCP

MCP (Model Context Protocol) — открытый стандарт от Anthropic для стандартизации взаимодействия AI с внешними системами:

```
┌─────────────────────────────────────────────────────────────┐
│              MCP: Стандартный протокол                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AI Clients           MCP              MCP Servers          │
│  ──────────           ───              ───────────          │
│                                                             │
│  Claude ─────┐                    ┌───── Slack Server       │
│              │                    │                         │
│  Cursor ─────┼──── MCP Protocol ──┼───── GitHub Server      │
│              │                    │                         │
│  Any AI ─────┘                    └───── Jira Server        │
│                                                             │
│  Один протокол для всех!                                    │
│  N + M вместо N × M                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Аналогия: USB

```python
# MCP — как USB для AI интеграций

usb_analogy = {
    "До USB": "Каждое устройство = свой разъём и драйвер",
    "После USB": "Единый стандарт, подключай и работай",
    
    "До MCP": "Каждый AI = свои интеграции",
    "После MCP": "Единый протокол, любой AI + любой источник"
}
```

---

## 3. Архитектура MCP

### 3.1 Компоненты

```
┌─────────────────────────────────────────────────────────────┐
│                   Архитектура MCP                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MCP Host (AI Application)                                  │
│  ─────────────────────────                                  │
│  • Cursor, Claude Desktop, custom app                       │
│  • Инициирует соединение                                    │
│  • Управляет MCP клиентами                                  │
│                                                             │
│  MCP Client                                                 │
│  ──────────                                                 │
│  • Встроен в Host                                           │
│  • Общается с серверами по протоколу                        │
│  • 1:1 связь с сервером                                     │
│                                                             │
│  MCP Server                                                 │
│  ──────────                                                 │
│  • Предоставляет Resources, Tools, Prompts                  │
│  • Может быть локальным или удалённым                       │
│  • Реализует конкретную интеграцию                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Возможности MCP Server

```python
# MCP Server предоставляет три типа capabilities

mcp_capabilities = {
    "Resources": {
        "what": "Данные, доступные для чтения",
        "examples": ["Файлы", "Записи БД", "API ответы"],
        "uri": "file:///path/to/file или custom://resource"
    },
    
    "Tools": {
        "what": "Функции, которые AI может вызывать",
        "examples": ["search(query)", "create_issue()", "send_message()"],
        "similar_to": "Function calling в OpenAI"
    },
    
    "Prompts": {
        "what": "Шаблоны промптов для типовых задач",
        "examples": ["summarize_pr", "review_code", "translate"],
        "purpose": "Переиспользуемые промпты"
    }
}
```

### 3.3 Пример MCP сервера

```python
# Простой MCP сервер на Python (псевдокод)

from mcp import Server, Resource, Tool

server = Server("my-company-data")

# Ресурсы

@server.resource("docs://{path}")
async def get_document(path: str) -> str:
    """Получить документ из базы знаний"""
    return knowledge_base.get(path)

# Инструменты

@server.tool("search_docs")
async def search_docs(query: str, limit: int = 10):
    """Поиск по документации"""
    return knowledge_base.search(query, limit=limit)

@server.tool("create_ticket")
async def create_ticket(title: str, description: str):
    """Создать тикет в Jira"""
    return jira.create_issue(title, description)

# Запуск

server.run()
```

---

## 4. MCP в Cursor и Claude

### 4.1 Настройка MCP в Cursor

```json
// ~/.cursor/mcp.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

### 4.2 Доступные MCP серверы

```python
available_mcp_servers = {
    "Official (Anthropic)": [
        "filesystem — доступ к файлам",
        "github — работа с репозиториями",
        "postgres — запросы к PostgreSQL",
        "sqlite — работа с SQLite",
        "puppeteer — браузерная автоматизация"
    ],
    "Community": [
        "slack — интеграция со Slack",
        "notion — работа с Notion",
        "linear — интеграция с Linear",
        "и многие другие..."
    ]
}
```

---

## 5. Значение MCP для Enterprise

### 5.1 Преимущества

```python
enterprise_benefits = {
    "Стандартизация": "Единый способ интеграции AI с системами",
    "Переиспользование": "Один MCP сервер для всех AI-инструментов",
    "Безопасность": "Централизованный контроль доступа",
    "Аудит": "Логирование всех взаимодействий",
    "Масштабирование": "Добавление новых AI без переделки интеграций"
}
```

### 5.2 Enterprise сценарии

```python
enterprise_scenarios = [
    "Внутренняя документация через MCP сервер",
    "Интеграция с CRM/ERP системами",
    "Доступ к внутренним API и микросервисам",
    "Работа с compliance-данными с контролем доступа",
    "Подключение legacy систем к AI"
]
```

---

## 💡 Key Takeaways

- **MCP решает проблему N×M интеграций** — стандартный протокол вместо кастомных интеграций для каждой пары AI + источник

- **Resources, Tools, Prompts** — три типа capabilities, которые предоставляет MCP сервер

- **Экосистема растёт** — уже есть серверы для GitHub, Slack, PostgreSQL и других систем

- **Enterprise ready** — MCP обеспечивает безопасность, аудит и стандартизацию для корпоративного использования

---

## 🚀 Next Steps

**Related Modules:**

- [10_Agents_Basics](../10_Agents_Basics/) — AI-агенты, использующие MCP

**Resources:**

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP GitHub](https://github.com/modelcontextprotocol)

---



