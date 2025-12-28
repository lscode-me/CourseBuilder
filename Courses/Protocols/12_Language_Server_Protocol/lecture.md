# Language Server Protocol (LSP)
## Зачем появился LSP, клиент-серверная модель, масштабирование IDE-экосистем

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать концепцию клиент-серверной модели
- Иметь опыт работы с IDE или редакторами кода
- Понимать концепцию протокола (модуль 01)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять проблему, которую решает LSP
- Понимать структуру LSP и его компоненты
- Анализировать, как LSP масштабирует IDE-экосистемы
- Применять LSP для создания языковой поддержки в редакторах

---

## 1. Введение: проблема языковой поддержки

**Проблема:** Каждая IDE должна поддерживать множество языков, каждый язык должен поддерживаться множеством IDE.

**До LSP:**
```

N языков × M редакторов = N×M интеграций

10 языков × 10 редакторов = 100 интеграций!
```

Каждая интеграция требует:

- Парсинг кода
- Автодополнение
- Go to definition
- Поиск ссылок
- Рефакторинг
- Диагностика ошибок

**Это не масштабируется.**

---

## 2. Решение: Language Server Protocol

### 2.1 Концепция

**LSP** — стандартизированный протокол между редакторами (клиентами) и языковыми серверами.

**После LSP:**
```

N языков + M редакторов = N+M реализаций

10 языков + 10 редакторов = 20 реализаций!
```

**Преимущества:**

- Каждый язык реализует один сервер
- Каждый редактор реализует один клиент
- Все работают вместе через LSP

### 2.2 Архитектура

```

┌──────────────┐              ┌──────────────┐
│   IDE Client │◄────LSP─────►│Lang Server   │
│  (VS Code)   │              │  (Pyright)   │
└──────────────┘              └──────────────┘
       │                                            │
       │                                            │
    UI/UX                       Language
                                Analysis
```

**Клиент (IDE):**

- Управляет UI
- Отправляет запросы серверу
- Отображает результаты

**Сервер (Language Server):**

- Анализирует код
- Предоставляет автодополнение, диагностику, и т.д.
- Не зависит от IDE

### 2.3 Коммуникация

LSP использует **JSON-RPC** через stdio, pipes, или сокеты.

**Пример инициализации:**
```json

Client → Server
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "rootUri": "file:///path/to/project",
    "capabilities": {
      "textDocument": {
        "completion": {}
      }
    }
  }
}

Server → Client
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "capabilities": {
      "completionProvider": {},
      "definitionProvider": true
    }
  }
}
```

---

## 3. Основные возможности LSP

### 3.1 Диагностика (Diagnostics)

Сервер отправляет ошибки и предупреждения клиенту:

```json

Server → Client (notification)
{
  "jsonrpc": "2.0",
  "method": "textDocument/publishDiagnostics",
  "params": {
    "uri": "file:///path/to/file.py",
    "diagnostics": [
      {
        "range": {
          "start": {"line": 5, "character": 10},
          "end": {"line": 5, "character": 20}
        },
        "severity": 1,
        "message": "Undefined variable 'foo'"
      }
    ]
  }
}
```

### 3.2 Автодополнение (Completion)

```json

Client → Server
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/completion",
  "params": {
    "textDocument": {"uri": "file:///path/to/file.py"},
    "position": {"line": 10, "character": 5}
  }
}

Server → Client
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "items": [
      {"label": "print", "kind": 3},
      {"label": "len", "kind": 3}
    ]
  }
}
```

### 3.3 Go to Definition

```json

Client → Server
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "textDocument/definition",
  "params": {
    "textDocument": {"uri": "file:///path/to/file.py"},
    "position": {"line": 15, "character": 10}
  }
}

Server → Client
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "uri": "file:///path/to/other.py",
    "range": {
      "start": {"line": 5, "character": 0},
      "end": {"line": 5, "character": 10}
    }
  }
}
```

### 3.4 Другие возможности

- **Hover**: подсказки при наведении

- **References**: поиск всех использований

- **Rename**: переименование символа

- **Formatting**: форматирование кода

- **Code actions**: быстрые исправления

- **Symbols**: навигация по символам

---

## 4. Жизненный цикл LSP сессии

### 4.1 Установление соединения

```

1. Client запускает Server процесс
2. Client отправляет initialize запрос
3. Server отвечает с capabilities
4. Client отправляет initialized уведомление
5. Сессия установлена
```

### 4.2 Работа с документами

```

Client открывает файл:
  → textDocument/didOpen

Client редактирует файл:
  → textDocument/didChange

Server анализирует изменения:
  ← textDocument/publishDiagnostics

Client запрашивает автодополнение:
  → textDocument/completion
  ← результаты
```

### 4.3 Завершение

```

Client → shutdown запрос
Server → подтверждение
Client → exit уведомление
Server → завершает процесс
```

---

## 5. Примеры Language Servers

### 5.1 Pyright (Python)

**Возможности:**

- Type checking
- Auto-completion
- Go to definition
- Find references

**Используется в:** VS Code, Neovim, Emacs

### 5.2 rust-analyzer (Rust)

**Возможности:**

- Быстрая диагностика
- Macro expansion
- Type inference
- Refactoring

### 5.3 clangd (C/C++)

**Возможности:**

- Code completion
- Cross-references
- Code navigation
- Formatting

### 5.4 typescript-language-server (TypeScript)

**Возможности:**

- Type checking
- Auto-imports
- Rename refactoring
- Quick fixes

---

## 6. Масштабирование IDE-экосистем

### 6.1 До LSP: N×M проблема

**Пример:** VS Code добавляет поддержку нового языка

1. Нужно изучить API VS Code
2. Реализовать парсинг языка
3. Реализовать все фичи (completion, diagnostics, и т.д.)
4. Поддерживать при изменениях VS Code API

**Для 10 языков:** 10 плагинов, 10 реализаций.

### 6.2 После LSP: N+M решение

**Пример:** VS Code добавляет поддержку нового языка

1. Используется существующий Language Server для языка
2. VS Code LSP клиент работает со всеми серверами
3. Один раз реализован, работает везде

**Для 10 языков:** 1 клиент + 10 серверов.

### 6.3 Преимущества для разработчиков языков

- **Одна реализация**: работает во всех IDE

- **Фокус на языке**: не нужно знать каждую IDE

- **Переиспользование**: language analysis используется везде

### 6.4 Преимущества для IDE разработчиков

- **Одна реализация**: LSP клиент для всех языков

- **Фокус на UI**: не нужно знать каждый язык

- **Экосистема**: сразу поддержка множества языков

---

## 7. Реализация простого Language Server

### 7.1 Базовая структура (Python)

```python

from pygls.server import LanguageServer
from lsprotocol import types

server = LanguageServer("example-server", "v0.1")

@server.feature(types.TEXT_DOCUMENT_COMPLETION)
def completion(params: types.CompletionParams):
    return types.CompletionList(
        is_incomplete=False,
        items=[
            types.CompletionItem(label="hello"),
            types.CompletionItem(label="world")
        ]
    )

@server.feature(types.TEXT_DOCUMENT_DID_OPEN)
def did_open(params: types.DidOpenTextDocumentParams):
    # Анализ открытого документа
    pass

if __name__ == "__main__":
    server.start_io()
```

### 7.2 Интеграция с VS Code

```json

// package.json
{
  "contributes": {
    "languages": [{
      "id": "example",
      "extensions": [".ex"]
    }],
    "configuration": {
      "type": "object",
      "properties": {
        "exampleServer.enabled": {
          "type": "boolean",
          "default": true
        }
      }
    }
  }
}
```

```typescript

// extension.ts
import { LanguageClient } from 'vscode-languageclient/node';

const client = new LanguageClient(
  'exampleServer',
  {
    command: 'python',
    args: ['/path/to/server.py']
  },
  {}
);

client.start();
```

---

## 8. LSP и будущее

### 8.1 Расширение LSP

**LSP продолжает развиваться:**

- Semantic tokens (подсветка синтаксиса)
- Inline values (значения переменных в отладке)
- Type hierarchy (иерархия типов)
- Call hierarchy (иерархия вызовов)

### 8.2 За пределами IDE

**LSP используется в:**

- Онлайн редакторах (GitHub Codespaces)
- Code review инструментах
- Static analysis инструментах
- Documentation генераторах

### 8.3 Похожие протоколы

**Debug Adapter Protocol (DAP):**

- Стандартизирует отладку
- Та же идея: N+M вместо N×M

**Test Adapter Protocol:**

- Стандартизирует запуск тестов

---

## 💡 Key Takeaways

- **LSP решает N×M проблему**: Вместо N×M интеграций между языками и IDE, LSP требует N+M реализаций (N серверов + M клиентов), масштабируя экосистему.

- **Клиент-серверная архитектура**: IDE (клиент) общается с language server через JSON-RPC, разделяя ответственность: UI в клиенте, анализ языка в сервере.

- **Стандартизированный протокол**: LSP определяет единый набор возможностей (completion, diagnostics, references), позволяя любому серверу работать с любым клиентом.

- **Одна реализация для всех IDE**: Разработчики языков реализуют один сервер, работающий во всех IDE. Разработчики IDE реализуют один клиент, поддерживающий все языки.

- **Экосистемный эффект**: LSP создал экосистему серверов и клиентов, упростив добавление языковой поддержки и мотивируя создание качественных language servers.

---

## 🚀 Next Steps

**Related Modules:**

- [13_UTF8_As_Protocol](../13_UTF8_As_Protocol/) — UTF-8 как протокол интерпретации данных
- [19_Protocol_Design](../19_Protocol_Design/) — как проектировать протоколы: принципы и best practices

**Practice Ideas:**

1. Настройте language server для вашего языка в VS Code или Neovim
2. Реализуйте простой language server с базовыми возможностями
3. Изучите спецификацию LSP и реализованные возможности

**Going Deeper:**

- Изучите Debug Adapter Protocol для понимания похожего подхода к отладке
- Изучите Tree-sitter для эффективного парсинга в language servers
- Изучите WASM для запуска language servers в браузере

---


