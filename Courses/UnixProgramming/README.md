# Unix System Programming with Python

Курс по системному программированию в среде Unix/OpenBSD с использованием Python. Изучите низкоуровневое взаимодействие с операционной системой: процессы, сигналы, файловые дескрипторы, сокеты, IPC и безопасность.

---

## 📋 Требования

- **ОС**: OpenBSD 7.4+ (рекомендуется), также подходит Linux/macOS
- **Python**: 3.10+
- **Знания**: Базовый Python, основы Unix (курс OpenBSD)
- **Инструменты**: терминал, текстовый редактор

---

## 📚 Структура курса

| # | Модуль | Описание | Время |
|---|--------|----------|-------|
| 01 | [Intro](01_Intro/) | Введение в системное программирование, модуль os | 40 мин |
| 02 | [Files & I/O](02_FilesAndIO/) | Файловые дескрипторы, низкоуровневый I/O | 45 мин |
| 03 | [File System](03_FileSystem/) | Метаданные, права, ссылки, inotify/kqueue | 45 мин |
| 04 | [Processes](04_Processes/) | fork, exec, wait, subprocess | 50 мин |
| 05 | [Signals](05_Signals/) | Сигналы Unix, обработчики, SIGCHLD | 40 мин |
| 06 | [IPC](06_IPC/) | Pipes, FIFO, очереди сообщений, shared memory | 50 мин |
| 07 | [Sockets](07_Sockets/) | TCP/UDP сокеты, клиент-сервер | 50 мин |
| 08 | [Unix Sockets](08_UnixSockets/) | Unix domain sockets, передача дескрипторов | 40 мин |
| 09 | [Async I/O](09_AsyncIO/) | select, poll, kqueue, asyncio | 50 мин |
| 10 | [Threads](10_Threads/) | threading, синхронизация, GIL | 45 мин |
| 11 | [Security](11_Security/) | pledge, unveil, chroot, capabilities | 45 мин |
| 12 | [Daemons](12_Daemons/) | Создание демонов, systemd/rc.d, логирование | 50 мин |

**Общее время курса**: ~9 часов

---

## 🎯 Что вы изучите

После прохождения курса вы сможете:

- ✅ Работать с файлами на уровне дескрипторов
- ✅ Создавать и управлять процессами (fork/exec)
- ✅ Обрабатывать сигналы Unix
- ✅ Реализовывать межпроцессное взаимодействие
- ✅ Программировать TCP/UDP и Unix сокеты
- ✅ Использовать асинхронный I/O и event loop
- ✅ Писать многопоточные приложения
- ✅ Применять механизмы безопасности OpenBSD
- ✅ Создавать системные демоны

---

## 🗺️ Карта зависимостей модулей

```
01_Intro
    │
    ▼
02_FilesAndIO ───────────────┐
    │                        │
    ▼                        │
03_FileSystem                │
    │                        │
    ▼                        │
04_Processes                 │
    │                        │
    ├──────────┐             │
    ▼          ▼             │
05_Signals  06_IPC           │
    │          │             │
    └────┬─────┘             │
         │                   │
         ▼                   │
    07_Sockets ◄─────────────┘
         │
         ▼
    08_UnixSockets
         │
         ▼
    09_AsyncIO
         │
         ▼
    10_Threads
         │
         ▼
    11_Security
         │
         ▼
    12_Daemons
```

---

## 🚀 Как использовать курс

### 1. Подготовка окружения

```bash
# На OpenBSD
$ doas pkg_add python-3.11

# Создать виртуальное окружение
$ python3 -m venv venv
$ source venv/bin/activate

# Установить зависимости (если нужны)
$ pip install psutil
```

### 2. Изучение материала

1. Читайте лекции последовательно
2. Выполняйте все примеры кода
3. Экспериментируйте в интерактивном режиме
4. Используйте `strace`/`ktrace` для понимания syscalls

### 3. Практика

Каждый модуль содержит:
- **Practice Ideas** — задачи для закрепления
- **Going Deeper** — продвинутые темы

---

## 📖 Навигация по модулям

### Начинающим в системном программировании
Изучите модули 01-06 последовательно, уделяя внимание примерам.

### Опытным Python разработчикам
Можете быстро пройти 01-03 и сосредоточиться на процессах и IPC (04-08).

### Для разработки серверов
Фокус на модули 07-09 (сокеты и асинхронный I/O) и 12 (демоны).

---

## 🛠️ Ключевые модули Python

| Модуль | Назначение |
|--------|------------|
| `os` | Базовые системные вызовы |
| `os.path` / `pathlib` | Работа с путями |
| `stat` | Метаданные файлов |
| `fcntl` | Управление файловыми дескрипторами |
| `signal` | Обработка сигналов |
| `subprocess` | Запуск процессов |
| `multiprocessing` | Многопроцессность |
| `socket` | Сетевое программирование |
| `select` / `selectors` | Мультиплексирование I/O |
| `asyncio` | Асинхронное программирование |
| `threading` | Многопоточность |

---

## 📝 Соглашения в курсе

### Форматирование кода

```python
#!/usr/bin/env python3
"""Описание модуля."""

import os
import sys

def main():
    """Главная функция."""
    # Код примера
    result = os.getpid()
    print(f"PID: {result}")

if __name__ == "__main__":
    main()
```

**Output:**
```
PID: 12345
```

### Маркеры

- 💡 **Pro Tip** — полезные советы
- ⚠️ **Warning** — важные предупреждения  
- 🔒 **Security** — важно для безопасности
- 🐧 **Linux-specific** — специфично для Linux
- 🐡 **OpenBSD-specific** — специфично для OpenBSD

---

## 🔗 Дополнительные ресурсы

**Книги:**
- "Advanced Programming in the UNIX Environment" by W. Richard Stevens
- "The Linux Programming Interface" by Michael Kerrisk
- "Unix Network Programming" by W. Richard Stevens

**Документация:**
- [Python os module](https://docs.python.org/3/library/os.html)
- [Python socket module](https://docs.python.org/3/library/socket.html)
- [OpenBSD man pages](https://man.openbsd.org/)

**Отладка:**
- `ktrace` / `kdump` — трассировка syscalls на OpenBSD
- `strace` — трассировка syscalls на Linux
- `lsof` — открытые файлы и сокеты

---

## 📄 Лицензия

Материалы курса предоставляются для образовательных целей.

---

**Версия курса**: 1.0  
**Дата создания**: Декабрь 2024  
**Python version**: 3.10+  
**Target OS**: OpenBSD 7.4+

---

