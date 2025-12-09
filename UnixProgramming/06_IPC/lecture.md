# Inter-Process Communication (IPC)
## Межпроцессное взаимодействие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [Processes](../04_Processes/) и [Signals](../05_Signals/)
- Понимать как работает fork()
- Знать про файловые дескрипторы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и использовать pipes (каналы)
- Работать с именованными каналами (FIFO)
- Применять разделяемую память
- Использовать очереди сообщений
- Синхронизировать процессы через семафоры
- Выбирать подходящий механизм IPC

---

## 1. Обзор механизмов IPC

### 1.1 Классификация

```
┌─────────────────────────────────────────────────────┐
│                     IPC Methods                      │
├──────────────────┬──────────────────────────────────┤
│  Communication   │  Synchronization                 │
├──────────────────┼──────────────────────────────────┤
│  - Pipes         │  - Semaphores                    │
│  - FIFOs         │  - Mutexes                       │
│  - Message queues│  - Condition variables           │
│  - Shared memory │  - File locks                    │
│  - Sockets       │                                  │
│  - Signals       │                                  │
└──────────────────┴──────────────────────────────────┘
```

### 1.2 Сравнение методов

| Метод | Скорость | Сложность | Связанные процессы |
|-------|----------|-----------|-------------------|
| Pipe | Средняя | Низкая | Да (родственные) |
| FIFO | Средняя | Низкая | Нет |
| Shared Memory | Высокая | Высокая | Нет |
| Message Queue | Средняя | Средняя | Нет |
| Socket | Средняя | Средняя | Нет |

---

## 2. Pipes (Каналы)

### 2.1 Анонимные pipes

```python
import os

# Создать pipe: (read_fd, write_fd)
read_fd, write_fd = os.pipe()

pid = os.fork()

if pid == 0:
    # Дочерний процесс — пишет
    os.close(read_fd)  # Закрыть ненужный конец
    
    message = b"Hello from child!"
    os.write(write_fd, message)
    
    os.close(write_fd)
    os._exit(0)
else:
    # Родительский процесс — читает
    os.close(write_fd)  # Закрыть ненужный конец
    
    data = os.read(read_fd, 1024)
    print(f"Parent received: {data.decode()}")
    
    os.close(read_fd)
    os.wait()
```

### 2.2 Двунаправленная связь

```python
import os

# Два pipe для двусторонней связи
parent_to_child_r, parent_to_child_w = os.pipe()
child_to_parent_r, child_to_parent_w = os.pipe()

pid = os.fork()

if pid == 0:
    # Дочерний процесс
    os.close(parent_to_child_w)
    os.close(child_to_parent_r)
    
    # Читать от родителя
    data = os.read(parent_to_child_r, 1024)
    print(f"Child received: {data.decode()}")
    
    # Отправить ответ
    os.write(child_to_parent_w, b"Response from child")
    
    os.close(parent_to_child_r)
    os.close(child_to_parent_w)
    os._exit(0)
else:
    # Родительский процесс
    os.close(parent_to_child_r)
    os.close(child_to_parent_w)
    
    # Отправить ребёнку
    os.write(parent_to_child_w, b"Message from parent")
    
    # Получить ответ
    data = os.read(child_to_parent_r, 1024)
    print(f"Parent received: {data.decode()}")
    
    os.close(parent_to_child_w)
    os.close(child_to_parent_r)
    os.wait()
```

### 2.3 subprocess.Popen с pipes

```python
import subprocess

# Pipe между процессами
# ls | grep ".py"
ls = subprocess.Popen(
    ["ls", "-la"],
    stdout=subprocess.PIPE
)

grep = subprocess.Popen(
    ["grep", ".py"],
    stdin=ls.stdout,
    stdout=subprocess.PIPE,
    text=True
)

ls.stdout.close()  # Позволить ls получить SIGPIPE
output, _ = grep.communicate()
print(output)
```

### 2.4 os.pipe2() — с флагами

```python
import os

# Создать pipe с флагами (Python 3.3+, Linux/BSD)
# O_CLOEXEC — закрыть при exec
# O_NONBLOCK — неблокирующий режим
read_fd, write_fd = os.pipe2(os.O_CLOEXEC | os.O_NONBLOCK)
```

---

## 3. Named Pipes (FIFO)

### 3.1 Создание FIFO

```python
import os
import stat

fifo_path = "/tmp/myfifo"

# Создать FIFO
try:
    os.mkfifo(fifo_path, 0o644)
except FileExistsError:
    pass  # Уже существует

print(f"FIFO created: {fifo_path}")
```

### 3.2 Писатель (writer)

```python
import os

fifo_path = "/tmp/myfifo"

print("Opening FIFO for writing...")
# Блокируется до появления читателя
fd = os.open(fifo_path, os.O_WRONLY)

print("Writing to FIFO...")
os.write(fd, b"Hello via FIFO!\n")
os.write(fd, b"Another message\n")

os.close(fd)
print("Done")
```

### 3.3 Читатель (reader)

```python
import os

fifo_path = "/tmp/myfifo"

print("Opening FIFO for reading...")
# Блокируется до появления писателя
fd = os.open(fifo_path, os.O_RDONLY)

print("Reading from FIFO...")
while True:
    data = os.read(fd, 1024)
    if not data:
        break
    print(f"Received: {data.decode()}", end="")

os.close(fd)
print("Done")
```

### 3.4 Неблокирующий режим

```python
import os
import select
import errno

fifo_path = "/tmp/myfifo"

# Открыть в неблокирующем режиме
fd = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)

while True:
    # Использовать select для ожидания данных
    readable, _, _ = select.select([fd], [], [], 1.0)
    
    if readable:
        try:
            data = os.read(fd, 1024)
            if not data:
                print("Writer closed")
                break
            print(f"Got: {data.decode()}")
        except BlockingIOError:
            pass
    else:
        print("Timeout, waiting...")

os.close(fd)
```

---

## 4. Shared Memory (Разделяемая память)

### 4.1 multiprocessing.shared_memory (Python 3.8+)

```python
from multiprocessing import shared_memory, Process
import numpy as np

def writer(shm_name):
    """Процесс-писатель."""
    # Присоединиться к существующей памяти
    shm = shared_memory.SharedMemory(name=shm_name)
    
    # Создать numpy array поверх shared memory
    data = np.ndarray((10,), dtype=np.int64, buffer=shm.buf)
    
    # Записать данные
    for i in range(10):
        data[i] = i * i
    
    print(f"Writer wrote: {list(data)}")
    shm.close()

def main():
    # Создать shared memory
    shm = shared_memory.SharedMemory(create=True, size=80)  # 10 * 8 bytes
    print(f"Created shared memory: {shm.name}")
    
    # Запустить писателя
    p = Process(target=writer, args=(shm.name,))
    p.start()
    p.join()
    
    # Прочитать данные
    data = np.ndarray((10,), dtype=np.int64, buffer=shm.buf)
    print(f"Main read: {list(data)}")
    
    # Очистить
    shm.close()
    shm.unlink()

if __name__ == "__main__":
    main()
```

### 4.2 mmap для shared memory

```python
import mmap
import os
import struct

def create_shared_file():
    """Создать файл для shared memory."""
    path = "/tmp/shared_data"
    
    # Создать файл нужного размера
    fd = os.open(path, os.O_RDWR | os.O_CREAT, 0o644)
    os.ftruncate(fd, 1024)
    
    # Создать mmap
    mm = mmap.mmap(fd, 1024)
    
    return mm, fd, path

def main():
    mm, fd, path = create_shared_file()
    
    pid = os.fork()
    
    if pid == 0:
        # Дочерний процесс — писатель
        import time
        time.sleep(0.5)
        
        # Записать данные
        mm.seek(0)
        mm.write(struct.pack("i", 42))
        mm.write(b"Hello from child!")
        
        mm.close()
        os.close(fd)
        os._exit(0)
    else:
        # Родительский процесс — читатель
        import time
        time.sleep(1)  # Подождать писателя
        
        mm.seek(0)
        value = struct.unpack("i", mm.read(4))[0]
        message = mm.read(17).decode()
        
        print(f"Value: {value}")
        print(f"Message: {message}")
        
        mm.close()
        os.close(fd)
        os.unlink(path)
        os.wait()

if __name__ == "__main__":
    main()
```

### 4.3 POSIX shared memory (через ctypes)

```python
import ctypes
import ctypes.util
import mmap
import os

# Загрузить libc
libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Константы
O_CREAT = 0x0200
O_RDWR = 0x0002

def shm_open(name, oflag, mode):
    """Открыть POSIX shared memory."""
    return libc.shm_open(name.encode(), oflag, mode)

def shm_unlink(name):
    """Удалить POSIX shared memory."""
    return libc.shm_unlink(name.encode())

# Использование
shm_name = "/my_shared_memory"
fd = shm_open(shm_name, O_CREAT | O_RDWR, 0o644)

if fd >= 0:
    os.ftruncate(fd, 4096)
    mm = mmap.mmap(fd, 4096)
    
    mm.write(b"Hello, shared memory!")
    mm.seek(0)
    print(mm.read(21).decode())
    
    mm.close()
    os.close(fd)
    shm_unlink(shm_name)
```

---

## 5. Message Queues

### 5.1 multiprocessing.Queue

```python
from multiprocessing import Process, Queue
import time

def producer(queue):
    """Производитель сообщений."""
    for i in range(5):
        message = f"Message {i}"
        queue.put(message)
        print(f"Produced: {message}")
        time.sleep(0.5)
    
    queue.put(None)  # Сигнал завершения

def consumer(queue):
    """Потребитель сообщений."""
    while True:
        message = queue.get()
        if message is None:
            break
        print(f"Consumed: {message}")

if __name__ == "__main__":
    queue = Queue()
    
    prod = Process(target=producer, args=(queue,))
    cons = Process(target=consumer, args=(queue,))
    
    prod.start()
    cons.start()
    
    prod.join()
    cons.join()
```

### 5.2 Queue с таймаутом

```python
from multiprocessing import Process, Queue
from queue import Empty

def consumer_with_timeout(queue):
    """Потребитель с таймаутом."""
    while True:
        try:
            message = queue.get(timeout=2)
            if message is None:
                break
            print(f"Got: {message}")
        except Empty:
            print("Timeout, no message")

if __name__ == "__main__":
    queue = Queue()
    
    p = Process(target=consumer_with_timeout, args=(queue,))
    p.start()
    
    import time
    queue.put("First")
    time.sleep(3)  # Вызовет timeout в consumer
    queue.put("Second")
    queue.put(None)
    
    p.join()
```

### 5.3 JoinableQueue — с подтверждением

```python
from multiprocessing import Process, JoinableQueue
import time

def worker(queue):
    """Рабочий с подтверждением обработки."""
    while True:
        task = queue.get()
        if task is None:
            queue.task_done()
            break
        
        print(f"Processing: {task}")
        time.sleep(0.5)  # Имитация работы
        
        queue.task_done()  # Подтвердить обработку

if __name__ == "__main__":
    queue = JoinableQueue()
    
    # Запустить рабочих
    workers = []
    for i in range(3):
        p = Process(target=worker, args=(queue,))
        p.start()
        workers.append(p)
    
    # Добавить задачи
    for task in range(10):
        queue.put(f"Task {task}")
    
    # Отправить сигналы завершения
    for _ in workers:
        queue.put(None)
    
    # Ждать обработки всех задач
    queue.join()
    print("All tasks completed")
    
    for p in workers:
        p.join()
```

---

## 6. Семафоры

### 6.1 multiprocessing.Semaphore

```python
from multiprocessing import Process, Semaphore
import time

def worker(sem, worker_id):
    """Рабочий, использующий семафор."""
    print(f"Worker {worker_id} waiting for semaphore")
    
    with sem:
        print(f"Worker {worker_id} acquired semaphore")
        time.sleep(2)  # Критическая секция
        print(f"Worker {worker_id} releasing semaphore")

if __name__ == "__main__":
    # Семафор на 2 одновременных доступа
    sem = Semaphore(2)
    
    workers = []
    for i in range(5):
        p = Process(target=worker, args=(sem, i))
        p.start()
        workers.append(p)
    
    for p in workers:
        p.join()
```

### 6.2 BoundedSemaphore

```python
from multiprocessing import Process, BoundedSemaphore

# BoundedSemaphore — с проверкой на overflow
sem = BoundedSemaphore(3)

# Попытка release() без acquire() вызовет ошибку
# (в отличие от обычного Semaphore)
```

### 6.3 Named Semaphore через ctypes

```python
import ctypes
import ctypes.util

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# На BSD/macOS
SEM_FAILED = ctypes.c_void_p(-1).value

def sem_open(name, oflag, mode=0, value=1):
    """Открыть именованный семафор."""
    libc.sem_open.restype = ctypes.c_void_p
    return libc.sem_open(name.encode(), oflag, mode, value)

def sem_wait(sem):
    """Ждать семафор."""
    return libc.sem_wait(ctypes.c_void_p(sem))

def sem_post(sem):
    """Освободить семафор."""
    return libc.sem_post(ctypes.c_void_p(sem))

def sem_close(sem):
    """Закрыть семафор."""
    return libc.sem_close(ctypes.c_void_p(sem))

def sem_unlink(name):
    """Удалить семафор."""
    return libc.sem_unlink(name.encode())
```

---

## 7. Locks (Блокировки)

### 7.1 multiprocessing.Lock

```python
from multiprocessing import Process, Lock, Value
import time

def increment(lock, counter, worker_id):
    """Увеличить счётчик с блокировкой."""
    for _ in range(1000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    lock = Lock()
    counter = Value('i', 0)  # 'i' = integer
    
    workers = []
    for i in range(4):
        p = Process(target=increment, args=(lock, counter, i))
        p.start()
        workers.append(p)
    
    for p in workers:
        p.join()
    
    print(f"Final counter: {counter.value}")  # Должно быть 4000
```

### 7.2 RLock (Recursive Lock)

```python
from multiprocessing import Process, RLock

def recursive_function(lock, depth=3):
    """Функция, которая может вызываться рекурсивно."""
    with lock:
        print(f"Depth {depth}")
        if depth > 0:
            recursive_function(lock, depth - 1)

if __name__ == "__main__":
    # RLock можно захватывать несколько раз одним процессом
    lock = RLock()
    
    p = Process(target=recursive_function, args=(lock,))
    p.start()
    p.join()
```

---

## 8. Практические примеры

### 8.1 Producer-Consumer с shared memory

```python
#!/usr/bin/env python3
"""Producer-Consumer с разделяемой памятью."""

from multiprocessing import Process, Value, Array, Condition
import time
import random

BUFFER_SIZE = 5

def producer(buffer, count, empty, full, mutex):
    """Производитель."""
    for i in range(20):
        item = random.randint(1, 100)
        
        with empty:  # Ждём пустой слот
            while count.value >= BUFFER_SIZE:
                empty.wait()
        
        with mutex:
            # Добавляем элемент
            buffer[count.value] = item
            count.value += 1
            print(f"Produced: {item}, count: {count.value}")
        
        with full:  # Сигнализируем о новом элементе
            full.notify()
        
        time.sleep(random.uniform(0.1, 0.3))

def consumer(buffer, count, empty, full, mutex, consumer_id):
    """Потребитель."""
    while True:
        with full:  # Ждём элемент
            while count.value <= 0:
                full.wait(timeout=2)
                if count.value <= 0:
                    print(f"Consumer {consumer_id} timeout, exiting")
                    return
        
        with mutex:
            # Забираем элемент
            count.value -= 1
            item = buffer[count.value]
            print(f"Consumer {consumer_id} consumed: {item}, count: {count.value}")
        
        with empty:  # Сигнализируем о свободном слоте
            empty.notify()
        
        time.sleep(random.uniform(0.2, 0.5))

if __name__ == "__main__":
    from multiprocessing import Manager
    
    manager = Manager()
    buffer = Array('i', BUFFER_SIZE)
    count = Value('i', 0)
    empty = manager.Condition()
    full = manager.Condition()
    mutex = manager.Lock()
    
    prod = Process(target=producer, args=(buffer, count, empty, full, mutex))
    cons1 = Process(target=consumer, args=(buffer, count, empty, full, mutex, 1))
    cons2 = Process(target=consumer, args=(buffer, count, empty, full, mutex, 2))
    
    prod.start()
    cons1.start()
    cons2.start()
    
    prod.join()
    cons1.join()
    cons2.join()
```

### 8.2 Простой RPC через FIFO

```python
#!/usr/bin/env python3
"""Простой RPC через именованные каналы."""

import os
import json
import threading

REQUEST_FIFO = "/tmp/rpc_request"
RESPONSE_FIFO = "/tmp/rpc_response"

class RPCServer:
    def __init__(self):
        self.methods = {}
    
    def register(self, name, func):
        self.methods[name] = func
    
    def serve(self):
        # Создать FIFO
        for fifo in (REQUEST_FIFO, RESPONSE_FIFO):
            try:
                os.mkfifo(fifo)
            except FileExistsError:
                pass
        
        print("RPC Server started")
        
        while True:
            # Читать запрос
            with open(REQUEST_FIFO, 'r') as f:
                request = json.load(f)
            
            # Обработать
            method = request.get('method')
            args = request.get('args', [])
            
            try:
                result = self.methods[method](*args)
                response = {'result': result}
            except Exception as e:
                response = {'error': str(e)}
            
            # Отправить ответ
            with open(RESPONSE_FIFO, 'w') as f:
                json.dump(response, f)

class RPCClient:
    def call(self, method, *args):
        request = {'method': method, 'args': args}
        
        # Отправить запрос
        with open(REQUEST_FIFO, 'w') as f:
            json.dump(request, f)
        
        # Получить ответ
        with open(RESPONSE_FIFO, 'r') as f:
            response = json.load(f)
        
        if 'error' in response:
            raise Exception(response['error'])
        
        return response['result']

# Пример использования:
# Server:
#   server = RPCServer()
#   server.register('add', lambda a, b: a + b)
#   server.serve()
#
# Client:
#   client = RPCClient()
#   result = client.call('add', 2, 3)
```

---

## 💡 Key Takeaways

- **Pipes** — простой способ связи между родственными процессами
- **FIFO** — именованные каналы для несвязанных процессов
- **Shared Memory** — самый быстрый способ, но требует синхронизации
- **Message Queues** — структурированный обмен сообщениями
- **Semaphores/Locks** — синхронизация доступа к ресурсам

---

## 🚀 Next Steps

**Related Modules:**
- [Sockets](../07_Sockets/) — сетевое взаимодействие
- [Unix Sockets](../08_UnixSockets/) — локальные сокеты

**Practice Ideas:**
1. Реализуйте простой shell с поддержкой pipe
2. Создайте систему логирования через FIFO
3. Напишите пул рабочих процессов с очередью задач
4. Реализуйте read-write lock

**Going Deeper:**
- POSIX message queues (mq_*)
- System V IPC (shmget, semget, msgget)
- D-Bus для IPC на десктопе

---

## 📚 Additional Resources

**Documentation:**
- [man pipe(2)](https://man.openbsd.org/pipe.2)
- [man mkfifo(2)](https://man.openbsd.org/mkfifo.2)
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

---

