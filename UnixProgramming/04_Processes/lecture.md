# Processes
## Управление процессами: fork, exec, wait

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модули [Intro](../01_Intro/) и [Files & I/O](../02_FilesAndIO/)
- Понимать концепцию процессов в Unix
- Знать что такое PID и PPID

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать дочерние процессы с помощью fork()
- Заменять образ процесса с помощью exec()
- Ожидать завершения процессов (wait/waitpid)
- Использовать subprocess для запуска программ
- Понимать и предотвращать зомби-процессы
- Применять multiprocessing для параллелизма

---

## 1. Основы процессов

### 1.1 Что такое процесс

**Процесс** — экземпляр выполняющейся программы со своим:
- Адресным пространством (код, данные, стек)
- Файловыми дескрипторами
- Идентификатором (PID)
- Состоянием (running, sleeping, zombie...)

```python
import os

# Информация о текущем процессе
print(f"PID: {os.getpid()}")
print(f"Parent PID: {os.getppid()}")
print(f"User ID: {os.getuid()}")
print(f"Group ID: {os.getgid()}")
print(f"Working dir: {os.getcwd()}")
```

### 1.2 Жизненный цикл процесса

```
      fork()
Parent ──────► Child
   │              │
   │              │ exec() (опционально)
   │              ▼
   │         Running
   │              │
   │              │ exit()
   │              ▼
   │         Zombie ◄── Процесс завершился,
   │              │      но parent не вызвал wait()
   │ wait()       │
   └──────────────┘
         │
         ▼
      Removed
```

---

## 2. fork() — создание процесса

### 2.1 Базовый fork

```python
import os

print(f"Before fork, PID: {os.getpid()}")

pid = os.fork()

if pid == 0:
    # Дочерний процесс
    print(f"Child process, PID: {os.getpid()}, Parent: {os.getppid()}")
else:
    # Родительский процесс
    print(f"Parent process, PID: {os.getpid()}, Child: {pid}")
```

**Output:**
```
Before fork, PID: 1234
Parent process, PID: 1234, Child: 1235
Child process, PID: 1235, Parent: 1234
```

### 2.2 Возвращаемое значение fork()

| Значение | Контекст |
|----------|----------|
| `0` | Дочерний процесс |
| `> 0` | Родительский процесс (значение = PID ребёнка) |
| `-1` | Ошибка (в Python — исключение) |

### 2.3 Что копируется при fork

```python
import os

data = ["original"]

pid = os.fork()

if pid == 0:
    # Ребёнок модифицирует свою КОПИЮ
    data.append("child")
    print(f"Child: {data}")
    os._exit(0)
else:
    import time
    time.sleep(0.1)
    # Родитель видит оригинальные данные
    print(f"Parent: {data}")
```

**Output:**
```
Child: ['original', 'child']
Parent: ['original']
```

### 2.4 Copy-on-Write

Современные системы используют **Copy-on-Write (COW)**:
- Память не копируется сразу
- Копирование происходит только при записи
- Экономит память и время

```python
import os

# Создать большой объект
big_data = b"X" * (100 * 1024 * 1024)  # 100 MB

pid = os.fork()  # Мгновенно! COW не копирует данные сразу

if pid == 0:
    # Только чтение — память разделяется
    print(f"Child reads: {len(big_data)} bytes")
    os._exit(0)
else:
    os.wait()
    print("Parent done")
```

---

## 3. exec() — замена образа процесса

### 3.1 Семейство exec

```python
import os

# exec заменяет текущий процесс новой программой
# После exec() код НИЖЕ НЕ ВЫПОЛНИТСЯ (если exec успешен)

pid = os.fork()

if pid == 0:
    # Дочерний процесс заменяет себя на ls
    os.execvp("ls", ["ls", "-la", "/tmp"])
    # Этот код НЕ выполнится
    print("This never prints")
else:
    os.wait()
    print("Child finished")
```

### 3.2 Варианты exec

| Функция | Описание |
|---------|----------|
| `execl(path, arg0, arg1, ...)` | Список аргументов |
| `execle(path, arg0, ..., env)` | С окружением |
| `execlp(file, arg0, arg1, ...)` | Поиск в PATH |
| `execv(path, args)` | Аргументы как список |
| `execve(path, args, env)` | Полный контроль |
| `execvp(file, args)` | Поиск в PATH + список |

```python
import os

pid = os.fork()

if pid == 0:
    # execve — полный контроль
    os.execve(
        "/usr/bin/env",
        ["env"],
        {"MY_VAR": "hello", "PATH": "/usr/bin"}
    )
```

### 3.3 Паттерн fork + exec

```python
import os
import sys

def run_command(cmd, args):
    """Запустить команду в дочернем процессе."""
    pid = os.fork()
    
    if pid == 0:
        # Дочерний процесс
        try:
            os.execvp(cmd, [cmd] + args)
        except OSError as e:
            print(f"exec failed: {e}", file=sys.stderr)
            os._exit(127)
    else:
        # Родитель ждёт
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status)

# Использование
exit_code = run_command("ls", ["-la", "/tmp"])
print(f"Command exited with: {exit_code}")
```

---

## 4. wait() — ожидание дочерних процессов

### 4.1 os.wait()

```python
import os
import time

pid = os.fork()

if pid == 0:
    print("Child: working...")
    time.sleep(2)
    print("Child: done")
    os._exit(42)  # Код завершения
else:
    print("Parent: waiting for child...")
    child_pid, status = os.wait()
    
    if os.WIFEXITED(status):
        exit_code = os.WEXITSTATUS(status)
        print(f"Child {child_pid} exited with code {exit_code}")
```

### 4.2 os.waitpid()

```python
import os

pid1 = os.fork()
if pid1 == 0:
    os._exit(1)

pid2 = os.fork()
if pid2 == 0:
    os._exit(2)

# Ждать конкретный процесс
_, status1 = os.waitpid(pid1, 0)
print(f"PID {pid1} exited with {os.WEXITSTATUS(status1)}")

# Ждать любой процесс
_, status2 = os.waitpid(-1, 0)
print(f"Another child exited with {os.WEXITSTATUS(status2)}")
```

### 4.3 Флаги waitpid

| Флаг | Описание |
|------|----------|
| `0` | Блокирующее ожидание |
| `WNOHANG` | Не блокировать, вернуть 0 если нет завершённых |
| `WUNTRACED` | Также возвращать остановленные процессы |

```python
import os
import time

pid = os.fork()

if pid == 0:
    time.sleep(10)
    os._exit(0)
else:
    # Неблокирующая проверка
    result, status = os.waitpid(pid, os.WNOHANG)
    
    if result == 0:
        print("Child still running")
    else:
        print(f"Child {result} finished")
```

### 4.4 Анализ статуса

```python
import os
import signal

def analyze_status(status):
    """Анализировать статус завершения процесса."""
    if os.WIFEXITED(status):
        code = os.WEXITSTATUS(status)
        print(f"Exited normally with code {code}")
    elif os.WIFSIGNALED(status):
        sig = os.WTERMSIG(status)
        print(f"Killed by signal {sig} ({signal.Signals(sig).name})")
    elif os.WIFSTOPPED(status):
        sig = os.WSTOPSIG(status)
        print(f"Stopped by signal {sig}")
```

---

## 5. Зомби-процессы

### 5.1 Что такое зомби

**Зомби** — процесс, который завершился, но родитель не вызвал wait().

```python
import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child {os.getpid()} exiting")
    os._exit(0)
else:
    print(f"Parent sleeping, child {pid} becomes zombie")
    time.sleep(60)  # Зомби существует 60 секунд
    os.wait()       # Только теперь зомби удаляется
```

### 5.2 Предотвращение зомби

**Способ 1: Всегда вызывать wait()**

```python
import os

for i in range(5):
    pid = os.fork()
    if pid == 0:
        os._exit(0)

# Дождаться всех детей
while True:
    try:
        os.wait()
    except ChildProcessError:
        break  # Нет больше детей
```

**Способ 2: Двойной fork**

```python
import os

pid = os.fork()

if pid == 0:
    # Первый ребёнок сразу форкается и завершается
    pid2 = os.fork()
    if pid2 == 0:
        # Внук — становится сиротой, adoptится init
        os.setsid()  # Новая сессия
        # Выполнить долгую работу...
        os._exit(0)
    else:
        os._exit(0)  # Первый ребёнок сразу завершается
else:
    os.wait()  # Быстро освобождаем первого ребёнка
```

**Способ 3: Обработчик SIGCHLD (см. модуль Signals)**

---

## 6. subprocess — высокоуровневый API

### 6.1 subprocess.run()

```python
import subprocess

# Простой запуск
result = subprocess.run(["ls", "-la", "/tmp"])
print(f"Return code: {result.returncode}")

# С захватом вывода
result = subprocess.run(
    ["ls", "-la", "/tmp"],
    capture_output=True,
    text=True
)
print(f"stdout: {result.stdout}")
print(f"stderr: {result.stderr}")

# Проверка кода возврата
result = subprocess.run(["ls", "/nonexistent"], check=True)
# Raises CalledProcessError if return code != 0
```

### 6.2 Передача ввода

```python
import subprocess

# Передать данные на stdin
result = subprocess.run(
    ["grep", "root"],
    input="root:x:0:0\nnobody:x:65534:65534\n",
    capture_output=True,
    text=True
)
print(result.stdout)

# Из файла
with open("/etc/passwd") as f:
    result = subprocess.run(["head", "-5"], stdin=f, capture_output=True, text=True)
    print(result.stdout)
```

### 6.3 Конвейеры (pipes)

```python
import subprocess

# Pipe: ls | grep .txt
ls = subprocess.Popen(["ls", "-la"], stdout=subprocess.PIPE)
grep = subprocess.Popen(
    ["grep", ".txt"],
    stdin=ls.stdout,
    stdout=subprocess.PIPE,
    text=True
)

ls.stdout.close()  # Позволить ls получить SIGPIPE
output, _ = grep.communicate()
print(output)
```

### 6.4 subprocess.Popen

```python
import subprocess
import time

# Запустить в фоне
proc = subprocess.Popen(
    ["sleep", "10"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print(f"Started process {proc.pid}")

# Проверить статус
if proc.poll() is None:
    print("Still running")

# Подождать с таймаутом
try:
    proc.wait(timeout=2)
except subprocess.TimeoutExpired:
    print("Timeout, killing...")
    proc.kill()
    proc.wait()
```

### 6.5 Shell команды

```python
import subprocess

# shell=True — выполнить через оболочку
# ОСТОРОЖНО: уязвимость shell injection!
result = subprocess.run(
    "ls -la /tmp | head -5",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)

# Безопаснее: shlex.quote для экранирования
import shlex
user_input = "file with spaces.txt"
cmd = f"ls -la {shlex.quote(user_input)}"
```

---

## 7. multiprocessing — параллелизм

### 7.1 Process class

```python
from multiprocessing import Process
import os

def worker(name):
    print(f"Worker {name}, PID: {os.getpid()}")

if __name__ == "__main__":
    processes = []
    
    for i in range(4):
        p = Process(target=worker, args=(f"process-{i}",))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    print("All workers finished")
```

### 7.2 Pool

```python
from multiprocessing import Pool
import time

def square(x):
    time.sleep(0.1)  # Симуляция работы
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        # map — применить функцию к каждому элементу
        results = pool.map(square, range(10))
        print(f"Results: {results}")
        
        # imap — ленивый итератор
        for result in pool.imap(square, range(10)):
            print(f"Got: {result}")
```

### 7.3 Обмен данными

```python
from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        q.put(i)
    q.put(None)  # Сигнал завершения

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Got: {item}")

if __name__ == "__main__":
    queue = Queue()
    
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

---

## 8. Практические примеры

### 8.1 Простая shell

```python
#!/usr/bin/env python3
"""Минималистичная shell."""

import os
import sys
import shlex

def execute(cmd):
    """Выполнить команду."""
    args = shlex.split(cmd)
    if not args:
        return
    
    # Встроенные команды
    if args[0] == "cd":
        try:
            os.chdir(args[1] if len(args) > 1 else os.environ["HOME"])
        except OSError as e:
            print(f"cd: {e}", file=sys.stderr)
        return
    
    if args[0] == "exit":
        sys.exit(0)
    
    # Внешние команды
    pid = os.fork()
    
    if pid == 0:
        try:
            os.execvp(args[0], args)
        except OSError as e:
            print(f"{args[0]}: {e}", file=sys.stderr)
            os._exit(127)
    else:
        _, status = os.waitpid(pid, 0)
        return os.WEXITSTATUS(status)

def main():
    while True:
        try:
            cmd = input(f"{os.getcwd()}$ ")
            execute(cmd)
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()

if __name__ == "__main__":
    main()
```

### 8.2 Параллельный загрузчик

```python
#!/usr/bin/env python3
"""Параллельная загрузка файлов."""

from multiprocessing import Pool, cpu_count
import subprocess
import sys

def download(url):
    """Загрузить URL через curl."""
    filename = url.split("/")[-1]
    result = subprocess.run(
        ["curl", "-sL", "-o", filename, url],
        capture_output=True
    )
    return (url, result.returncode == 0, filename)

def main(urls):
    workers = min(cpu_count(), len(urls))
    
    with Pool(workers) as pool:
        for url, success, filename in pool.imap_unordered(download, urls):
            status = "✓" if success else "✗"
            print(f"{status} {url} → {filename}")

if __name__ == "__main__":
    urls = [
        "https://example.com/file1.txt",
        "https://example.com/file2.txt",
        # ...
    ]
    main(urls)
```

---

## 💡 Key Takeaways

- **fork()** создаёт копию процесса, возвращает 0 в ребёнке
- **exec()** заменяет образ процесса новой программой
- **wait()** необходим для предотвращения зомби
- **subprocess** — предпочтительный API для запуска команд
- **multiprocessing** — для параллелизма без GIL

---

## 🚀 Next Steps

**Related Modules:**
- [Signals](../05_Signals/) — обработка сигналов
- [IPC](../06_IPC/) — межпроцессное взаимодействие

**Practice Ideas:**
1. Напишите простую shell с поддержкой pipe
2. Создайте менеджер процессов (запуск, мониторинг, остановка)
3. Реализуйте параллельный grep
4. Напишите утилиту timeout

**Going Deeper:**
- Process groups и sessions
- Control terminals
- Daemon processes

---

## 📚 Additional Resources

**Documentation:**
- [man fork(2)](https://man.openbsd.org/fork.2)
- [man execve(2)](https://man.openbsd.org/execve.2)
- [man waitpid(2)](https://man.openbsd.org/waitpid.2)
- [Python subprocess](https://docs.python.org/3/library/subprocess.html)
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

---

