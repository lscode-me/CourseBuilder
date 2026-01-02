# Web Programming in Linux

Курс по веб-программированию в среде Linux — от низкоуровневых сокетов до современных асинхронных фреймворков.

---

## 🎯 О курсе

Этот курс раскрывает полный стек веб-технологий:

- Как работает HTTP на уровне байтов
- Как Linux обрабатывает сетевые соединения
- Эволюция веб-серверов от Apache до современных решений
- Gateway интерфейсы: CGI → FastCGI → WSGI → ASGI
- Реальная архитектура production-систем

---

## 📋 Prerequisites

- Базовые знания Linux и командной строки
- Основы TCP/IP и сетей
- Знание Python (для примеров)
- Желательно: курс [Unix Programming](../UnixProgramming/)

---

## 📚 Modules

### Фундамент

| # | Модуль | Описание |
|---|--------|----------|
| 01 | [HTTP Protocol](./01_HTTP/) | HTTP/1.0, HTTP/1.1, HTTP/2, структура запросов/ответов, статусы |
| 02 | [Socket Activation](./02_SocketActivation/) | systemd socket activation, эмуляция веб-сервера на shell/python |

### Веб-серверы

| # | Модуль | Описание |
|---|--------|----------|
| 03 | [Web Servers](./03_WebServers/) | Apache, Nginx, OpenBSD httpd, Caddy, Lighttpd и др. |

### Gateway Interfaces

| # | Модуль | Описание |
|---|--------|----------|
| 04 | [CGI](./04_CGI/) | CGI, FastCGI, SCGI — эволюция gateway интерфейсов |
| 05 | [WSGI](./05_WSGI/) | Python Web Server Gateway Interface, middleware, frameworks |
| 06 | [ASGI](./06_ASGI/) | Асинхронный ASGI, uvicorn, Starlette, современные подходы |

### Современные технологии

| # | Модуль | Описание |
|---|--------|----------|
| 07 | [WebSockets](./07_WebSockets/) | WebSocket протокол, real-time приложения |
| 08 | [Architecture](./08_Architecture/) | Архитектура современных веб-приложений |
| 09 | [Database](./09_Database/) | Взаимодействие веб-приложений с БД |
| 10 | [OpenResty](./10_OpenResty/) | Lua и программируемый веб-сервер на базе Nginx |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────┐
│                    Web Programming                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐     ┌──────────────────┐                       │
│  │  HTTP   │────►│ Socket Activation│                       │
│  └─────────┘     └────────┬─────────┘                       │
│                           │                                 │
│                           ▼                                 │
│                  ┌─────────────────┐                        │
│                  │   Web Servers   │                        │
│                  └────────┬────────┘                        │
│                           │                                 │
│         ┌─────────────────┼─────────────────┐               │
│         ▼                 ▼                 ▼               │
│    ┌─────────┐      ┌──────────┐      ┌──────────┐          │
│    │   CGI   │─────►│   WSGI   │─────►│   ASGI   │          │
│    └─────────┘      └──────────┘      └──────────┘          │
│                           │                 │               │
│                           └────────┬────────┘               │
│                                    ▼                        │
│              ┌─────────────────────────────────────┐        │
│              │  WebSockets │ Architecture │ DB     │        │
│              └──────────────────┬──────────────────┘        │
│                                 │                           │
│                                 ▼                           │
│                        ┌──────────────┐                     │
│                        │  OpenResty   │                     │
│                        │  (Lua edge)  │                     │
│                        └──────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Practice Environment

Для практики понадобится:

```bash
# Linux-система (или VM/container)
# Например, Debian/Ubuntu:
sudo apt update
sudo apt install python3 python3-pip nginx apache2

# Python пакеты
pip3 install flask django gunicorn uvicorn starlette websockets
```

---

## 📖 Recommended Reading

**Specifications:**

- [RFC 7230-7235](https://tools.ietf.org/html/rfc7230) — HTTP/1.1
- [RFC 7540](https://tools.ietf.org/html/rfc7540) — HTTP/2
- [RFC 6455](https://tools.ietf.org/html/rfc6455) — WebSocket
- [PEP 3333](https://peps.python.org/pep-3333/) — WSGI
- [ASGI Spec](https://asgi.readthedocs.io/) — ASGI

**Books:**

- "HTTP: The Definitive Guide" — полное руководство по HTTP
- "High Performance Browser Networking" by Ilya Grigorik
- "nginx: A Practical Guide to High Performance"

---


