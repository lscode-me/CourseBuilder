# Threading
## Многопоточность в Python

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули [Processes](../04_Processes/) и [Async I/O](../09_AsyncIO/)
- Понимать разницу между процессами и потоками
- Знать основы конкурентного программирования

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять потоками
- Понимать GIL и его влияние
- Использовать примитивы синхронизации
- Работать с очередями для потоков
- Применять ThreadPoolExecutor
- Избегать типичных ошибок многопоточности

---

## 1. Потоки vs Процессы

### 1.1 Сравнение

| Характеристика | Потоки | Процессы |
|----------------|--------|----------|
| Память | Общая | Изолированная |
| Создание | Быстрое | Медленное |
| Обмен данными | Простой | Через IPC |
| GIL | Да | Нет |
| Падение | Все потоки | Только один процесс |

### 1.2 Global Interpreter Lock (GIL)

```

┌─────────────────────────────────────────────────────────┐
│                     Python Process                       │
├─────────────────────────────────────────────────────────┤
│                         GIL                              │
│                          │                               │
│         ┌────────────────┼────────────────┐             │
│         ▼                ▼                ▼             │
│    ┌─────────┐      ┌─────────┐      ┌─────────┐       │
│    │ Thread 1│      │ Thread 2│      │ Thread 3│       │
│    │ RUNNING │      │ WAITING │      │ WAITING │       │
│    └─────────┘      └─────────┘      └─────────┘       │
│                                                         │
│  Только один поток выполняет Python bytecode!           │
└─────────────────────────────────────────────────────────┘

```

**Когда GIL НЕ мешает:**

- I/O операции (сеть, файлы)
- Вызовы C-расширений (NumPy)
- Ожидание (sleep, locks)

**Когда GIL мешает:**

- CPU-intensive вычисления

---

## 2. Создание потоков

### 2.1 threading.Thread

```python

import threading
import time

def worker(name, delay):
    """Функция потока."""
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} done")

# Создать потоки
t1 = threading.Thread(target=worker, args=("A", 2))
t2 = threading.Thread(target=worker, args=("B", 1))

# Запустить
t1.start()
t2.start()

# Дождаться завершения
t1.join()
t2.join()

print("All workers finished")

```

### 2.2 Наследование от Thread

```python

import threading
import time

class MyWorker(threading.Thread):
    def __init__(self, name, iterations):
        super().__init__()
        self.name = name
        self.iterations = iterations
        self.result = None
    
    def run(self):
        """Код, выполняемый в потоке."""
        total = 0
        for i in range(self.iterations):
            total += i
            time.sleep(0.01)
        self.result = total

# Использование
worker = MyWorker("Counter", 100)
worker.start()
worker.join()
print(f"Result: {worker.result}")

```

### 2.3 Daemon потоки

```python

import threading
import time

def background_task():
    """Фоновая задача."""
    while True:
        print("Background running...")
        time.sleep(1)

# Daemon поток завершается вместе с главным
t = threading.Thread(target=background_task)
t.daemon = True  # Или t.setDaemon(True)
t.start()

print("Main thread working...")
time.sleep(3)
print("Main thread exiting (daemon will be killed)")

```

---

## 3. Синхронизация

### 3.1 Lock

```python

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Автоматически acquire/release
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Counter: {counter}")  # Должно быть 400000

```

### 3.2 RLock (Recursive Lock)

```python

import threading

rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            print(f"Level {n}")
            recursive_function(n - 1)

# RLock можно захватить несколько раз одним потоком
recursive_function(5)

```

### 3.3 Condition

```python

import threading
import time
import random

items = []
condition = threading.Condition()

def producer():
    global items
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.5))
        with condition:
            item = f"item-{i}"
            items.append(item)
            print(f"Produced: {item}")
            condition.notify()

def consumer():
    global items
    while True:
        with condition:
            while not items:
                print("Consumer waiting...")
                condition.wait()
            item = items.pop(0)
            print(f"Consumed: {item}")
            if item == "item-9":
                break

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

```

### 3.4 Semaphore

```python

import threading
import time

# Ограничить доступ к ресурсу
semaphore = threading.Semaphore(3)  # Максимум 3 одновременно

def worker(name):
    print(f"{name} waiting for semaphore")
    with semaphore:
        print(f"{name} acquired semaphore")
        time.sleep(2)
        print(f"{name} releasing semaphore")

threads = [threading.Thread(target=worker, args=(f"Worker-{i}",)) for i in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

```

### 3.5 Event

```python

import threading
import time

event = threading.Event()

def waiter(name):
    print(f"{name} waiting for event")
    event.wait()
    print(f"{name} received event")

def setter():
    print("Setter sleeping...")
    time.sleep(2)
    print("Setter setting event")
    event.set()

threads = [threading.Thread(target=waiter, args=(f"Waiter-{i}",)) for i in range(3)]
setter_thread = threading.Thread(target=setter)

for t in threads:
    t.start()
setter_thread.start()

for t in threads:
    t.join()
setter_thread.join()

```

### 3.6 Barrier

```python

import threading
import time
import random

barrier = threading.Barrier(3)

def worker(name):
    print(f"{name} starting")
    time.sleep(random.uniform(0.5, 2))
    print(f"{name} waiting at barrier")
    barrier.wait()  # Ждать пока все 3 достигнут барьера
    print(f"{name} passed barrier")

threads = [threading.Thread(target=worker, args=(f"Worker-{i}",)) for i in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()

```

---

## 4. Thread-safe очереди

### 4.1 queue.Queue

```python

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        item = f"item-{i}"
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(0.5)
    q.put(None)  # Сигнал завершения

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

```

### 4.2 Типы очередей

```python

import queue

# FIFO очередь (по умолчанию)
fifo = queue.Queue()

# LIFO очередь (стек)
lifo = queue.LifoQueue()

# Приоритетная очередь
priority = queue.PriorityQueue()
priority.put((3, "low"))
priority.put((1, "high"))
priority.put((2, "medium"))

while not priority.empty():
    print(priority.get())  # (1, "high"), (2, "medium"), (3, "low")

```

### 4.3 Bounded Queue

```python

import queue
import threading
import time

# Очередь с ограничением размера
bounded_q = queue.Queue(maxsize=5)

def producer():
    for i in range(20):
        item = f"item-{i}"
        print(f"Producing {item}...")
        bounded_q.put(item)  # Блокируется если очередь полная
        print(f"Produced {item}")

def consumer():
    for i in range(20):
        time.sleep(0.3)  # Медленный потребитель
        item = bounded_q.get()
        print(f"Consumed: {item}")
        bounded_q.task_done()

prod = threading.Thread(target=producer)
cons = threading.Thread(target=consumer)

prod.start()
cons.start()

prod.join()
cons.join()

```

---

## 5. ThreadPoolExecutor

### 5.1 Базовое использование

```python

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} starting")
    time.sleep(1)
    return n * n

# Создать пул потоков
with ThreadPoolExecutor(max_workers=4) as executor:
    # Запустить задачи
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Получить результаты
    for future in futures:
        result = future.result()
        print(f"Result: {result}")

```

### 5.2 executor.map()

```python

from concurrent.futures import ThreadPoolExecutor
import time

def download(url):
    print(f"Downloading {url}...")
    time.sleep(1)  # Имитация загрузки
    return f"Content of {url}"

urls = [
    "http://example1.com",
    "http://example2.com",
    "http://example3.com",
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, urls))
    
for result in results:
    print(result)

```

### 5.3 as_completed()

```python

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def task(n):
    delay = random.uniform(0.5, 2)
    time.sleep(delay)
    return n, delay

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(task, i): i for i in range(5)}
    
    # Получить результаты по мере готовности
    for future in as_completed(futures):
        task_id = futures[future]
        result, delay = future.result()
        print(f"Task {task_id} completed in {delay:.2f}s")

```

---

## 6. Thread-local данные

### 6.1 threading.local()

```python

import threading

# Данные, уникальные для каждого потока
local_data = threading.local()

def worker(name):
    local_data.name = name
    local_data.counter = 0
    
    for i in range(3):
        local_data.counter += 1
        print(f"Thread {local_data.name}: counter = {local_data.counter}")

threads = [
    threading.Thread(target=worker, args=(f"Worker-{i}",))
    for i in range(3)
]

for t in threads:
    t.start()

for t in threads:
    t.join()

```

---

## 7. Типичные проблемы

### 7.1 Race Condition

```python

import threading

# ПРОБЛЕМА: Race condition
counter = 0

def bad_increment():
    global counter
    for _ in range(100000):
        # Не атомарная операция!
        counter += 1

# РЕШЕНИЕ: Использовать Lock
counter_safe = 0
lock = threading.Lock()

def good_increment():
    global counter_safe
    for _ in range(100000):
        with lock:
            counter_safe += 1

```

### 7.2 Deadlock

```python

import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    with lock_a:
        print("Thread 1 acquired A")
        # Потенциальный deadlock!
        with lock_b:
            print("Thread 1 acquired B")

def thread2():
    with lock_b:
        print("Thread 2 acquired B")
        # Потенциальный deadlock!
        with lock_a:
            print("Thread 2 acquired A")

# РЕШЕНИЕ: Всегда захватывать locks в одном порядке
def safe_thread():
    # Всегда сначала A, потом B
    with lock_a:
        with lock_b:
            pass

```

---

## 8. Практические примеры

### 8.1 Параллельная загрузка

```python
#!/usr/bin/env python3
"""Параллельная загрузка файлов."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
import time

def download_url(url):
    """Загрузить URL."""
    start = time.time()
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            elapsed = time.time() - start
            return url, len(data), elapsed, None
    except Exception as e:
        elapsed = time.time() - start
        return url, 0, elapsed, str(e)

def main():
    urls = [
        "http://example.com",
        "http://httpbin.org/get",
        "http://httpbin.org/delay/1",
    ]
    
    print("Starting parallel downloads...")
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(download_url, url): url for url in urls}
        
        for future in as_completed(futures):
            url, size, elapsed, error = future.result()
            if error:
                print(f"✗ {url}: {error}")
            else:
                print(f"✓ {url}: {size} bytes in {elapsed:.2f}s")
    
    total_time = time.time() - start
    print(f"\nTotal time: {total_time:.2f}s")

if __name__ == "__main__":
    main()

```

### 8.2 Worker Pool Pattern

```python
#!/usr/bin/env python3
"""Worker pool для обработки задач."""

import threading
import queue
import time

class WorkerPool:
    def __init__(self, num_workers):
        self.tasks = queue.Queue()
        self.results = queue.Queue()
        self.workers = []
        self.running = True
        
        for i in range(num_workers):
            t = threading.Thread(target=self._worker, args=(i,))
            t.daemon = True
            t.start()
            self.workers.append(t)
    
    def _worker(self, worker_id):
        while self.running:
            try:
                task_id, func, args = self.tasks.get(timeout=1)
            except queue.Empty:
                continue
            
            try:
                result = func(*args)
                self.results.put((task_id, result, None))
            except Exception as e:
                self.results.put((task_id, None, e))
            finally:
                self.tasks.task_done()
    
    def submit(self, task_id, func, *args):
        self.tasks.put((task_id, func, args))
    
    def get_result(self, timeout=None):
        return self.results.get(timeout=timeout)
    
    def wait(self):
        self.tasks.join()
    
    def shutdown(self):
        self.running = False
        for t in self.workers:
            t.join()

# Использование
def process(x):
    time.sleep(0.5)
    return x * x

pool = WorkerPool(4)

for i in range(10):
    pool.submit(i, process, i)

pool.wait()

while not pool.results.empty():
    task_id, result, error = pool.get_result()
    print(f"Task {task_id}: {result}")

pool.shutdown()

```

---

## 💡 Key Takeaways

- **GIL** не мешает I/O-bound задачам

- **Lock** — базовый примитив синхронизации

- **Queue** — безопасный обмен данными между потоками

- **ThreadPoolExecutor** — удобный API для пула потоков
- Для CPU-bound используйте multiprocessing, не threading

---

## 🚀 Next Steps

**Related Modules:**

- [Security](../11_Security/) — безопасность
- [Daemons](../12_Daemons/) — создание демонов

**Practice Ideas:**

1. Создайте параллельный web scraper
2. Напишите producer-consumer систему
3. Реализуйте connection pool для базы данных
4. Создайте rate limiter с семафорами

**Going Deeper:**

- threading vs multiprocessing vs asyncio
- Lock-free структуры данных
- Memory ordering и volatile

---

## 📚 Additional Resources

**Documentation:**

- [Python threading](https://docs.python.org/3/library/threading.html)
- [Python queue](https://docs.python.org/3/library/queue.html)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)

---




