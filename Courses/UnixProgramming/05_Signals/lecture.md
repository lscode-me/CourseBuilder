# Signals
## Сигналы Unix и их обработка

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [Processes](../04_Processes/)
- Понимать концепцию процессов
- Знать как работает fork() и wait()

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать механизм сигналов Unix
- Устанавливать обработчики сигналов в Python
- Отправлять сигналы процессам
- Правильно обрабатывать SIGCHLD
- Использовать сигналы для IPC
- Писать программы устойчивые к сигналам

---

## 1. Основы сигналов

### 1.1 Что такое сигнал

**Сигнал** — асинхронное уведомление процессу о событии. Это механизм "программных прерываний".

```

┌──────────────┐     ┌──────────────┐
│   Kernel     │────►│   Process    │
│              │     │              │
│  События:    │     │  Действия:   │
│  - Ctrl+C    │     │  - Default   │
│  - kill cmd  │     │  - Ignore    │
│  - Exception │     │  - Handler   │
│  - Child exit│     │  - Block     │
└──────────────┘     └──────────────┘

```

### 1.2 Основные сигналы

```python

import signal

# Посмотреть все сигналы
for name, value in sorted(signal.Signals.__members__.items()):
    print(f"{value:2d} {name}")

```

| Сигнал | Номер | Описание | Действие |
|--------|-------|----------|----------|
| SIGHUP | 1 | Hangup (закрытие терминала) | Terminate |
| SIGINT | 2 | Interrupt (Ctrl+C) | Terminate |
| SIGQUIT | 3 | Quit (Ctrl+\) | Core dump |
| SIGKILL | 9 | Kill (нельзя перехватить) | Terminate |
| SIGTERM | 15 | Terminate (мягкое завершение) | Terminate |
| SIGCHLD | 20 | Child status changed | Ignore |
| SIGSTOP | 17 | Stop (нельзя перехватить) | Stop |
| SIGCONT | 19 | Continue | Continue |
| SIGUSR1 | 30 | User-defined 1 | Terminate |
| SIGUSR2 | 31 | User-defined 2 | Terminate |

> **⚠️ Warning:**  
> Номера сигналов могут различаться между ОС. Всегда используйте константы из модуля `signal`.

### 1.3 Действия по умолчанию

| Действие | Описание |
|----------|----------|
| Terminate | Завершить процесс |
| Core dump | Завершить + создать core файл |
| Stop | Остановить (заморозить) процесс |
| Continue | Продолжить остановленный процесс |
| Ignore | Игнорировать сигнал |

---

## 2. Установка обработчиков

### 2.1 signal.signal()

```python

import signal
import sys

def handler(signum, frame):
    """Обработчик сигнала."""
    sig_name = signal.Signals(signum).name
    print(f"\nReceived signal {signum} ({sig_name})")
    sys.exit(0)

# Установить обработчик
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print("Press Ctrl+C to send SIGINT...")

# Ожидание сигналов
while True:
    signal.pause()  # Ждать любой сигнал

```

### 2.2 Специальные обработчики

```python

import signal

# SIG_IGN — игнорировать сигнал
signal.signal(signal.SIGHUP, signal.SIG_IGN)

# SIG_DFL — вернуть обработчик по умолчанию
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Получить текущий обработчик
current = signal.getsignal(signal.SIGTERM)
print(f"Current SIGTERM handler: {current}")

```

### 2.3 Безопасное завершение

```python

import signal
import sys
import time

class GracefulKiller:
    """Класс для graceful shutdown."""
    
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    
    def exit_gracefully(self, signum, frame):
        print(f"\nReceived signal {signum}, shutting down...")
        self.kill_now = True

def main():
    killer = GracefulKiller()
    
    print("Working... Press Ctrl+C to stop")
    
    while not killer.kill_now:
        # Основная работа
        print(".", end="", flush=True)
        time.sleep(0.5)
    
    # Cleanup
    print("\nCleaning up...")
    time.sleep(1)
    print("Done!")

if __name__ == "__main__":
    main()

```

---

## 3. Отправка сигналов

### 3.1 os.kill()

```python

import os
import signal
import time

pid = os.fork()

if pid == 0:
    # Дочерний процесс
    print(f"Child {os.getpid()} waiting for signal...")
    signal.pause()
    print("Child received signal!")
    os._exit(0)
else:
    # Родитель
    time.sleep(1)
    print(f"Parent sending SIGUSR1 to {pid}")
    os.kill(pid, signal.SIGUSR1)
    os.wait()

```

### 3.2 Отправка группе процессов

```python

import os
import signal

# Отправить сигнал группе процессов
pgid = os.getpgid(0)  # Получить PGID текущего процесса
# os.killpg(pgid, signal.SIGTERM)

# Отправить сигнал всем процессам (требует root)
# os.kill(-1, signal.SIGTERM)

# Отправить сигнал себе
os.kill(os.getpid(), signal.SIGUSR1)

```

### 3.3 signal.raise_signal()

```python

import signal

# Отправить сигнал текущему процессу (Python 3.8+)
signal.raise_signal(signal.SIGUSR1)

```

---

## 4. SIGCHLD — мониторинг дочерних процессов

### 4.1 Автоматический сбор зомби

```python

import signal
import os
import time

def sigchld_handler(signum, frame):
    """Обработчик SIGCHLD для сбора зомби."""
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
            print(f"Child {pid} exited with status {status}")
        except ChildProcessError:
            break

# Установить обработчик
signal.signal(signal.SIGCHLD, sigchld_handler)

# Создать детей
for i in range(3):
    pid = os.fork()
    if pid == 0:
        time.sleep(i + 1)
        os._exit(i)

# Родитель продолжает работу
print("Parent doing other work...")
time.sleep(5)
print("Parent done")

```

### 4.2 Игнорирование SIGCHLD

```python

import signal
import os

# На некоторых системах игнорирование SIGCHLD
# автоматически удаляет зомби
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid == 0:
    os._exit(0)

# Зомби не создаётся
```

---

## 5. Сигналы и многопоточность

### 5.1 Ограничения

```python

import signal
import threading
import time

# Сигналы доставляются ТОЛЬКО главному потоку!

def handler(signum, frame):
    print(f"Signal received in thread: {threading.current_thread().name}")

signal.signal(signal.SIGUSR1, handler)

def worker():
    print(f"Worker running in: {threading.current_thread().name}")
    time.sleep(10)

t = threading.Thread(target=worker)
t.start()

# Этот сигнал будет получен главным потоком
# даже если worker thread активен
```

### 5.2 Прерывание потоков через сигналы

```python

import signal
import threading
import time

class SignalHandler:
    def __init__(self):
        self.stop_event = threading.Event()
        signal.signal(signal.SIGINT, self._handler)
        signal.signal(signal.SIGTERM, self._handler)
    
    def _handler(self, signum, frame):
        self.stop_event.set()

def worker(stop_event):
    while not stop_event.is_set():
        print("Working...")
        time.sleep(1)
    print("Worker stopped")

handler = SignalHandler()
t = threading.Thread(target=worker, args=(handler.stop_event,))
t.start()
t.join()

```

---

## 6. Таймеры и алармы

### 6.1 signal.alarm()

```python

import signal
import time

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

signal.signal(signal.SIGALRM, timeout_handler)

def long_operation():
    time.sleep(10)  # Долгая операция
    return "Done"

try:
    signal.alarm(3)  # Таймаут 3 секунды
    result = long_operation()
    signal.alarm(0)  # Отменить таймер
    print(f"Result: {result}")
except TimeoutError as e:
    print(f"Error: {e}")

```

### 6.2 Context manager для таймаута

```python

import signal
from contextlib import contextmanager

class TimeoutError(Exception):
    pass

@contextmanager
def timeout(seconds):
    """Context manager для таймаута операции."""
    def handler(signum, frame):
        raise TimeoutError(f"Timed out after {seconds} seconds")
    
    # Сохранить старый обработчик
    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

# Использование
try:
    with timeout(5):
        # Долгая операция
        import time
        time.sleep(10)
except TimeoutError as e:
    print(e)

```

### 6.3 setitimer — более точные таймеры

```python

import signal
import time

def handler(signum, frame):
    print(f"Timer fired at {time.time()}")

signal.signal(signal.SIGALRM, handler)

# Установить периодический таймер (каждые 0.5 секунды)
# (delay, interval)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

start = time.time()
while time.time() - start < 3:
    signal.pause()

# Отменить таймер
signal.setitimer(signal.ITIMER_REAL, 0)

```

---

## 7. Блокировка сигналов

### 7.1 signal.pthread_sigmask()

```python

import signal
import time
import os

# Заблокировать SIGINT на время критической секции
def critical_section():
    # Заблокировать
    old_mask = signal.pthread_sigmask(
        signal.SIG_BLOCK,
        [signal.SIGINT]
    )
    
    try:
        print("Critical section (SIGINT blocked)")
        print("Try pressing Ctrl+C...")
        time.sleep(3)
        print("Critical section done")
    finally:
        # Разблокировать
        signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)
        print("SIGINT unblocked")

# После разблокировки отложенный сигнал будет доставлен
critical_section()

```

### 7.2 Проверка отложенных сигналов

```python

import signal

# Получить маску отложенных сигналов
pending = signal.sigpending()
print(f"Pending signals: {pending}")

```

---

## 8. Практические примеры

### 8.1 Демон с reload конфигурации

```python
#!/usr/bin/env python3
"""Демон с поддержкой reload через SIGHUP."""

import signal
import time
import json
import os

class Daemon:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}
        self.running = True
        
        # Установить обработчики
        signal.signal(signal.SIGHUP, self.reload_config)
        signal.signal(signal.SIGTERM, self.shutdown)
        signal.signal(signal.SIGINT, self.shutdown)
        
        self.load_config()
    
    def load_config(self):
        """Загрузить конфигурацию."""
        try:
            with open(self.config_path) as f:
                self.config = json.load(f)
            print(f"Config loaded: {self.config}")
        except Exception as e:
            print(f"Config error: {e}")
    
    def reload_config(self, signum, frame):
        """Обработчик SIGHUP — перезагрузить конфигурацию."""
        print("Received SIGHUP, reloading config...")
        self.load_config()
    
    def shutdown(self, signum, frame):
        """Обработчик завершения."""
        print(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def run(self):
        """Основной цикл."""
        print(f"Daemon started, PID: {os.getpid()}")
        print("Send SIGHUP to reload config, SIGTERM to stop")
        
        while self.running:
            # Основная работа
            print(f"Working with config: {self.config.get('setting', 'default')}")
            time.sleep(2)
        
        print("Daemon stopped")

if __name__ == "__main__":
    daemon = Daemon("/tmp/daemon.json")
    daemon.run()

```

### 8.2 Watchdog процесс

```python
#!/usr/bin/env python3
"""Watchdog — перезапуск упавших процессов."""

import os
import signal
import sys
import time

class Watchdog:
    def __init__(self, command):
        self.command = command
        self.child_pid = None
        self.running = True
        
        signal.signal(signal.SIGCHLD, self.handle_child)
        signal.signal(signal.SIGTERM, self.handle_term)
        signal.signal(signal.SIGINT, self.handle_term)
    
    def handle_child(self, signum, frame):
        """Дочерний процесс завершился."""
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == self.child_pid:
                if os.WIFEXITED(status):
                    code = os.WEXITSTATUS(status)
                    print(f"Child {pid} exited with code {code}")
                elif os.WIFSIGNALED(status):
                    sig = os.WTERMSIG(status)
                    print(f"Child {pid} killed by signal {sig}")
                
                self.child_pid = None
        except ChildProcessError:
            pass
    
    def handle_term(self, signum, frame):
        """Завершение watchdog."""
        print("Watchdog stopping...")
        self.running = False
        if self.child_pid:
            os.kill(self.child_pid, signal.SIGTERM)
    
    def start_child(self):
        """Запустить дочерний процесс."""
        pid = os.fork()
        if pid == 0:
            os.execvp(self.command[0], self.command)
            os._exit(127)
        else:
            self.child_pid = pid
            print(f"Started child {pid}")
    
    def run(self):
        """Основной цикл."""
        print(f"Watchdog started, PID: {os.getpid()}")
        self.start_child()
        
        while self.running:
            if self.child_pid is None:
                print("Restarting child in 2 seconds...")
                time.sleep(2)
                if self.running:
                    self.start_child()
            else:
                signal.pause()
        
        # Дождаться завершения ребёнка
        if self.child_pid:
            os.waitpid(self.child_pid, 0)
        
        print("Watchdog stopped")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} command [args...]")
        sys.exit(1)
    
    watchdog = Watchdog(sys.argv[1:])
    watchdog.run()

```

---

## 💡 Key Takeaways

- **Сигналы** — механизм асинхронных уведомлений

- **SIGKILL и SIGSTOP** — нельзя перехватить или игнорировать

- **signal.signal()** — устанавливает обработчик

- **SIGCHLD** — уведомляет о завершении дочерних процессов

- **signal.alarm()** — для таймаутов
- В многопоточных программах сигналы получает только главный поток

---

## 🚀 Next Steps

**Related Modules:**

- [IPC](../06_IPC/) — межпроцессное взаимодействие
- [Daemons](../12_Daemons/) — создание демонов

**Practice Ideas:**

1. Создайте процесс с graceful shutdown
2. Напишите timeout wrapper для команд
3. Реализуйте supervisor для группы процессов
4. Создайте heartbeat между процессами через SIGUSR1

**Going Deeper:**

- Real-time signals (SIGRTMIN-SIGRTMAX)
- signalfd (Linux) для работы с сигналами через fd
- sigaction для детального контроля

---

## 📚 Additional Resources

**Documentation:**

- [man signal(7)](https://man.openbsd.org/signal.3)
- [man kill(2)](https://man.openbsd.org/kill.2)
- [Python signal module](https://docs.python.org/3/library/signal.html)

---




