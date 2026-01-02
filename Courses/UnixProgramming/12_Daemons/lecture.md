# Daemons
## Создание демонов и системных служб

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти все предыдущие модули курса
- Понимать процессы, сигналы, файлы
- Знать основы безопасности (pledge/unveil)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать жизненный цикл демона
- Создавать правильные Unix демоны
- Работать с PID файлами
- Логировать через syslog
- Интегрировать с rc.d (OpenBSD) и systemd (Linux)
- Обрабатывать сигналы для graceful shutdown

---

## 1. Что такое демон

### 1.1 Определение

**Демон (daemon)** — фоновый процесс без управляющего терминала, работающий непрерывно.

```
┌─────────────────────────────────────────────────────────┐
│                    User Space                           │
├─────────────────────────────────────────────────────────┤
│  ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│  │ sshd    │    │ httpd   │    │ cron    │   Daemons    │
│  │ (daemon)│    │ (daemon)│    │ (daemon)│              │
│  └─────────┘    └─────────┘    └─────────┘              │
│       │              │              │                   │
│       └──────────────┴──────────────┘                   │
│                      │                                  │
│               No controlling terminal                   │
│               Parent: init/systemd (PID 1)              │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Характеристики демона

| Характеристика | Описание |
|----------------|----------|
| Нет терминала | PPID = 1 (init/systemd) |
| Рабочая директория | / или специфичная |
| umask | 0 или ограниченная |
| stdin/stdout/stderr | /dev/null |
| PID файл | /var/run/daemon.pid |
| Логирование | syslog |

---

## 2. Создание демона (традиционный способ)

### 2.1 Классический двойной fork

```python
#!/usr/bin/env python3
"""Традиционный Unix демон."""

import os
import sys
import atexit
import signal

def daemonize(pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    """Преобразовать процесс в демон."""
    
    # 1. Первый fork — отделиться от родителя
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # Родитель завершается
    except OSError as e:
        sys.stderr.write(f"First fork failed: {e}\n")
        sys.exit(1)
    
    # 2. Создать новую сессию
    os.setsid()  # Стать лидером сессии
    
    # 3. Игнорировать SIGHUP (потеря терминала)
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    
    # 4. Второй fork — избавиться от лидерства сессии
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  # Первый ребёнок завершается
    except OSError as e:
        sys.stderr.write(f"Second fork failed: {e}\n")
        sys.exit(1)
    
    # 5. Теперь мы демон!
    
    # 6. Сменить рабочую директорию
    os.chdir("/")
    
    # 7. Сбросить umask
    os.umask(0)
    
    # 8. Перенаправить стандартные потоки
    sys.stdout.flush()
    sys.stderr.flush()
    
    with open(stdin, 'rb', 0) as si:
        os.dup2(si.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as so:
        os.dup2(so.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as se:
        os.dup2(se.fileno(), sys.stderr.fileno())
    
    # 9. Записать PID файл
    pid = str(os.getpid())
    with open(pidfile, 'w') as f:
        f.write(pid + '\n')
    
    # 10. Удалить PID файл при завершении
    atexit.register(lambda: os.remove(pidfile))

# Использование
if __name__ == "__main__":
    daemonize('/var/run/mydaemon.pid')
    
    # Код демона
    import time
    while True:
        time.sleep(60)
```

### 2.2 Современный подход с python-daemon

```python
#!/usr/bin/env python3
"""Демон с использованием python-daemon."""
# pip install python-daemon

import daemon
import daemon.pidfile
import signal
import time
import logging
import logging.handlers

def run_daemon():
    """Основной код демона."""
    logger = logging.getLogger('mydaemon')
    logger.setLevel(logging.INFO)
    
    # Логирование в syslog
    handler = logging.handlers.SysLogHandler(address='/dev/log')
    logger.addHandler(handler)
    
    logger.info("Daemon started")
    
    while True:
        logger.info("Daemon working...")
        time.sleep(60)

def main():
    pidfile = daemon.pidfile.TimeoutPIDLockFile('/var/run/mydaemon.pid')
    
    context = daemon.DaemonContext(
        working_directory='/var/lib/mydaemon',
        umask=0o002,
        pidfile=pidfile,
    )
    
    # Обработчики сигналов
    context.signal_map = {
        signal.SIGTERM: lambda signum, frame: sys.exit(0),
        signal.SIGHUP: 'terminate',  # Или функция для reload
    }
    
    with context:
        run_daemon()

if __name__ == "__main__":
    main()
```

---

## 3. PID файлы

### 3.1 Работа с PID файлами

```python
import os
import fcntl
import sys

class PIDFile:
    """Управление PID файлом с блокировкой."""
    
    def __init__(self, path):
        self.path = path
        self.fd = None
    
    def acquire(self):
        """Создать и заблокировать PID файл."""
        self.fd = os.open(self.path, os.O_CREAT | os.O_RDWR, 0o644)
        
        try:
            # Эксклюзивная блокировка (неблокирующая)
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            # Уже запущен другой экземпляр
            os.close(self.fd)
            raise RuntimeError("Another instance is running")
        
        # Записать PID
        os.ftruncate(self.fd, 0)
        os.write(self.fd, f"{os.getpid()}\n".encode())
        os.fsync(self.fd)
    
    def release(self):
        """Освободить PID файл."""
        if self.fd:
            fcntl.flock(self.fd, fcntl.LOCK_UN)
            os.close(self.fd)
            try:
                os.unlink(self.path)
            except OSError:
                pass
    
    @staticmethod
    def read_pid(path):
        """Прочитать PID из файла."""
        try:
            with open(path) as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return None
    
    @staticmethod
    def is_running(path):
        """Проверить, запущен ли демон."""
        pid = PIDFile.read_pid(path)
        if pid is None:
            return False
        
        try:
            os.kill(pid, 0)  # Проверка существования
            return True
        except OSError:
            return False
    
    def __enter__(self):
        self.acquire()
        return self
    
    def __exit__(self, *args):
        self.release()

# Использование
with PIDFile("/var/run/mydaemon.pid"):
    # Код демона
    pass
```

---

## 4. Логирование через syslog

### 4.1 syslog модуль

```python
import syslog

# Открыть соединение с syslog
syslog.openlog(
    ident="mydaemon",
    logoption=syslog.LOG_PID | syslog.LOG_NDELAY,
    facility=syslog.LOG_DAEMON
)

# Отправить сообщения
syslog.syslog(syslog.LOG_INFO, "Daemon started")
syslog.syslog(syslog.LOG_WARNING, "Something wrong")
syslog.syslog(syslog.LOG_ERR, "Error occurred")

# Закрыть соединение
syslog.closelog()
```

### 4.2 logging с SysLogHandler

```python
import logging
import logging.handlers

def setup_logging(name, level=logging.INFO):
    """Настроить логирование в syslog."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Handler для syslog
    handler = logging.handlers.SysLogHandler(
        address='/dev/log',
        facility=logging.handlers.SysLogHandler.LOG_DAEMON
    )
    
    # Формат сообщений
    formatter = logging.Formatter(
        '%(name)s[%(process)d]: %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Использование
logger = setup_logging('mydaemon')
logger.info("Daemon started")
logger.error("Something went wrong", exc_info=True)
```

### 4.3 Уровни syslog

| Уровень | Описание |
|---------|----------|
| LOG_EMERG | Система неработоспособна |
| LOG_ALERT | Требуется немедленное действие |
| LOG_CRIT | Критическая ошибка |
| LOG_ERR | Ошибка |
| LOG_WARNING | Предупреждение |
| LOG_NOTICE | Нормальное, но важное |
| LOG_INFO | Информационное |
| LOG_DEBUG | Отладочное |

---

## 5. Обработка сигналов

### 5.1 Graceful shutdown

```python
import signal
import sys
import threading

class GracefulShutdown:
    """Класс для graceful shutdown."""
    
    def __init__(self):
        self.shutdown_event = threading.Event()
        
        # Регистрируем обработчики
        signal.signal(signal.SIGTERM, self._handler)
        signal.signal(signal.SIGINT, self._handler)
        signal.signal(signal.SIGHUP, self._reload_handler)
    
    def _handler(self, signum, frame):
        """Обработчик завершения."""
        self.shutdown_event.set()
    
    def _reload_handler(self, signum, frame):
        """Обработчик перезагрузки конфигурации."""
        # Переопределите этот метод для reload
        pass
    
    def should_shutdown(self):
        return self.shutdown_event.is_set()
    
    def wait(self, timeout=None):
        return self.shutdown_event.wait(timeout)

# Использование
shutdown = GracefulShutdown()

while not shutdown.should_shutdown():
    # Работа демона
    shutdown.wait(timeout=1)

# Cleanup
print("Cleaning up...")
```

### 5.2 Reload конфигурации по SIGHUP

```python
import signal
import json
import threading

class ConfigurableDaemon:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}
        self.config_lock = threading.Lock()
        self.running = True
        
        signal.signal(signal.SIGHUP, self._reload_config)
        signal.signal(signal.SIGTERM, self._shutdown)
        
        self.load_config()
    
    def load_config(self):
        """Загрузить конфигурацию."""
        with self.config_lock:
            with open(self.config_path) as f:
                self.config = json.load(f)
        print(f"Config loaded: {self.config}")
    
    def _reload_config(self, signum, frame):
        """SIGHUP handler — перезагрузить конфигурацию."""
        print("Received SIGHUP, reloading config...")
        self.load_config()
    
    def _shutdown(self, signum, frame):
        """SIGTERM handler — завершить работу."""
        print("Received SIGTERM, shutting down...")
        self.running = False
    
    def run(self):
        """Основной цикл."""
        while self.running:
            with self.config_lock:
                # Использовать config
                interval = self.config.get('interval', 60)
            
            # Работа
            time.sleep(interval)
```

---

## 6. Интеграция с init системами

### 6.1 rc.d скрипт для OpenBSD

```sh
#!/bin/ksh
# /etc/rc.d/mydaemon

daemon="/usr/local/bin/mydaemon"
daemon_flags=""
daemon_user="_mydaemon"

. /etc/rc.d/rc.subr

rc_reload=YES

rc_pre() {
    install -d -o ${daemon_user} /var/run/mydaemon
}

rc_cmd $1
```

```python
#!/usr/bin/env python3
# /usr/local/bin/mydaemon
"""Демон для OpenBSD rc.d."""

import os
import sys
import signal
import syslog
import time

PIDFILE = "/var/run/mydaemon/mydaemon.pid"

def main():
    syslog.openlog("mydaemon", syslog.LOG_PID, syslog.LOG_DAEMON)
    syslog.syslog(syslog.LOG_INFO, "Starting daemon")
    
    # Записать PID файл
    with open(PIDFILE, 'w') as f:
        f.write(f"{os.getpid()}\n")
    
    # Обработчик завершения
    running = True
    def shutdown(signum, frame):
        nonlocal running
        syslog.syslog(syslog.LOG_INFO, "Shutting down")
        running = False
    
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    
    try:
        while running:
            # Работа демона
            time.sleep(1)
    finally:
        os.unlink(PIDFILE)
        syslog.syslog(syslog.LOG_INFO, "Daemon stopped")
        syslog.closelog()

if __name__ == "__main__":
    main()
```

### 6.2 systemd unit для Linux

```ini
# /etc/systemd/system/mydaemon.service
[Unit]
Description=My Python Daemon
After=network.target

[Service]
Type=simple
User=mydaemon
Group=mydaemon
ExecStart=/usr/local/bin/mydaemon
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5

# Безопасность
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

```python
#!/usr/bin/env python3
# /usr/local/bin/mydaemon
"""Демон для systemd (Type=simple)."""

import signal
import sys
import time
import logging

# systemd не требует daemonize() - просто запускаем foreground!

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger('mydaemon')

running = True

def shutdown(signum, frame):
    global running
    logger.info("Shutting down...")
    running = False

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

def main():
    logger.info("Daemon started")
    
    while running:
        logger.info("Working...")
        time.sleep(10)
    
    logger.info("Daemon stopped")

if __name__ == "__main__":
    main()
```

---

## 7. Практический пример: полный демон

```python
#!/usr/bin/env python3
"""Полнофункциональный демон."""

import os
import sys
import signal
import time
import json
import socket
import logging
import logging.handlers
import threading
import argparse
import fcntl

class Daemon:
    """Базовый класс демона."""
    
    def __init__(self, config_path, pidfile):
        self.config_path = config_path
        self.pidfile = pidfile
        self.config = {}
        self.running = True
        self.logger = None
        
    def setup_logging(self):
        """Настроить логирование."""
        self.logger = logging.getLogger('mydaemon')
        self.logger.setLevel(logging.INFO)
        
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        formatter = logging.Formatter('mydaemon[%(process)d]: %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def load_config(self):
        """Загрузить конфигурацию."""
        try:
            with open(self.config_path) as f:
                self.config = json.load(f)
            self.logger.info(f"Config loaded from {self.config_path}")
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
    
    def acquire_pidfile(self):
        """Захватить PID файл."""
        self.pid_fd = os.open(self.pidfile, os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(self.pid_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            self.logger.error("Another instance is running")
            sys.exit(1)
        
        os.ftruncate(self.pid_fd, 0)
        os.write(self.pid_fd, f"{os.getpid()}\n".encode())
        os.fsync(self.pid_fd)
    
    def release_pidfile(self):
        """Освободить PID файл."""
        if hasattr(self, 'pid_fd'):
            fcntl.flock(self.pid_fd, fcntl.LOCK_UN)
            os.close(self.pid_fd)
            try:
                os.unlink(self.pidfile)
            except OSError:
                pass
    
    def setup_signals(self):
        """Настроить обработчики сигналов."""
        signal.signal(signal.SIGTERM, self.handle_shutdown)
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGHUP, self.handle_reload)
    
    def handle_shutdown(self, signum, frame):
        """Обработчик завершения."""
        self.logger.info(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def handle_reload(self, signum, frame):
        """Обработчик перезагрузки."""
        self.logger.info("Received SIGHUP, reloading config...")
        self.load_config()
    
    def run(self):
        """Основной цикл демона."""
        self.setup_logging()
        self.logger.info("Daemon starting...")
        
        self.load_config()
        self.acquire_pidfile()
        self.setup_signals()
        
        self.logger.info(f"Daemon started, PID {os.getpid()}")
        
        try:
            while self.running:
                self.do_work()
                time.sleep(self.config.get('interval', 60))
        finally:
            self.cleanup()
    
    def do_work(self):
        """Основная работа демона. Переопределите в подклассе."""
        self.logger.debug("Heartbeat")
    
    def cleanup(self):
        """Очистка при завершении."""
        self.logger.info("Cleaning up...")
        self.release_pidfile()
        self.logger.info("Daemon stopped")

class MyDaemon(Daemon):
    """Пример конкретного демона."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server = None
    
    def do_work(self):
        """Реальная работа."""
        self.logger.info("Processing tasks...")
        # Ваш код здесь

def main():
    parser = argparse.ArgumentParser(description='My Daemon')
    parser.add_argument('-c', '--config', default='/etc/mydaemon.json',
                        help='Config file path')
    parser.add_argument('-p', '--pidfile', default='/var/run/mydaemon.pid',
                        help='PID file path')
    parser.add_argument('-f', '--foreground', action='store_true',
                        help='Run in foreground')
    args = parser.parse_args()
    
    daemon = MyDaemon(args.config, args.pidfile)
    daemon.run()

if __name__ == "__main__":
    main()
```

---

## 💡 Key Takeaways

- **Двойной fork** — классический способ создания демона

- **PID файл** — предотвращает множественный запуск

- **syslog** — стандартное логирование для демонов

- **SIGHUP** — для перезагрузки конфигурации

- **SIGTERM** — для graceful shutdown

- **systemd** — не требует daemonize(), запускайте foreground

---

## 🚀 Завершение курса

Поздравляем! Вы прошли курс по системному программированию в Unix/OpenBSD с Python.

**Что вы изучили:**

- Низкоуровневая работа с файлами и I/O
- Управление процессами (fork, exec, wait)
- Сигналы и IPC
- Сетевое программирование (TCP/UDP, Unix sockets)
- Асинхронный I/O и многопоточность
- Безопасность (pledge, unveil)
- Создание демонов

**Следующие шаги:**

1. Практика — создайте свой демон
2. Изучите исходники OpenBSD утилит
3. Прочитайте "Advanced Programming in the UNIX Environment"
4. Попробуйте написать что-то полезное!

---

## 📚 Additional Resources

**Documentation:**

- [man daemon(3)](https://man.openbsd.org/daemon.3)
- [man rc.d(8)](https://man.openbsd.org/rc.d.8)
- [systemd.service](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

**Books:**

- "Advanced Programming in the UNIX Environment" — Stevens, Rago
- "The Linux Programming Interface" — Michael Kerrisk

---

## 🚀 Next Steps

**Это последний модуль курса Unix Programming.**

**Практика:**

1. Напишите демон, который логирует системные события в файл
2. Создайте systemd unit файл для вашего демона
3. Реализуйте graceful shutdown с обработкой SIGTERM

**Рекомендуемые курсы для продолжения:**

- [Containers](../../Containers/) — Контейнеризация и Docker
- [DevOps](../../DevOps/) — DevOps практики и инструменты
- [Networking](../../Networking/) — Сетевое программирование




