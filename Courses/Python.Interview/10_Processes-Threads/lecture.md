# Процессы и потоки в Python

## Что нужно знать для интервью

Это важная и часто задаваемая тема. Вас спросят про GIL, разницу между threads и processes, и попросят найти race condition в коде.

---

## 🔑 Ключевые понятия

### GIL (Global Interpreter Lock)

**Ответ на интервью:**
> "GIL — это mutex, который защищает доступ к объектам Python. Из-за GIL только один поток может выполнять Python байткод одновременно. Поэтому threads не дают ускорения для CPU-bound задач, но полезны для I/O-bound."

### Threads vs Processes

| Аспект | Threads | Processes |
|--------|---------|-----------|
| **Память** | Общая | Раздельная |
| **Вес** | Легковесные | Тяжёлые |
| **GIL** | Ограничены GIL | Не ограничены |
| **Лучше для** | I/O-bound | CPU-bound |
| **Коммуникация** | Прямой доступ | IPC (очереди, pipes) |

### Когда что использовать

| Задача | Решение |
|--------|---------|
| Сетевые запросы | `threading` или `asyncio` |
| Чтение файлов | `threading` |
| Вычисления (CPU) | `multiprocessing` |
| Параллельный API | `concurrent.futures` |

---

## 💻 Код с race condition

### Задача на интервью

```python

import threading

class Counter:
    def __init__(self):
        self.val = 0

    def increment(self):
        self.val += 1  # НЕ атомарная операция!

def work(counter, n):
    for _ in range(n):
        counter.increment()

counter = Counter()
threads = []

for _ in range(10):
    t = threading.Thread(target=work, args=(counter, 100000))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Expected: 1000000, Got: {counter.val}")
# Получим меньше 1000000!
```

**Почему так?**
> "`self.val += 1` — не атомарная операция. Она состоит из: прочитать val, добавить 1, записать val. Между этими шагами другой поток может изменить val."

### Исправление с Lock

```python

import threading

class SafeCounter:
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # Только один поток одновременно
            self.val += 1
```

---

## 💻 os.fork()

### Вопрос на интервью

> "Что произойдёт, если выполнить `os.fork()` в Python REPL?"

**Ответ:**
> "Процесс раздваивается. И parent, и child продолжат выполнение с того же места. В REPL это создаёт путаницу — оба процесса будут писать в терминал. Нужно нажать Ctrl+D дважды для выхода."

```python

import os

pid = os.fork()
if pid == 0:
    print(f"Child process: {os.getpid()}")
else:
    print(f"Parent process: {os.getpid()}, child: {pid}")
```

---

## 💻 Практические примеры

### ThreadPoolExecutor

```python

from concurrent.futures import ThreadPoolExecutor
import requests

urls = ["http://example.com"] * 10

def fetch(url):
    return requests.get(url).status_code

# I/O-bound — используем threads
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch, urls))
```

### ProcessPoolExecutor

```python

from concurrent.futures import ProcessPoolExecutor

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# CPU-bound — используем processes
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_heavy, [10**6] * 10))
```

---

## ❓ Типичные вопросы на интервью

### Q: Почему threads не ускоряют CPU-bound код?

**A:**
> "Из-за GIL. Только один поток выполняет Python код одновременно. Threads переключаются, но не работают параллельно. Для CPU-bound нужен multiprocessing — отдельные процессы со своими GIL."

### Q: Есть ли разница между `val += 1` и `val = val + 1`?

**A:**
> "С точки зрения thread safety — нет разницы. Обе операции не атомарны. Обе состоят из read-modify-write и требуют lock для безопасности."

### Q: Как обмениваться данными между процессами?

**A:**
| Метод | Описание |
|-------|----------|
| `Queue` | Потокобезопасная очередь |
| `Pipe` | Двустороннее соединение |
| `Value`, `Array` | Shared memory |
| `Manager` | Сложные структуры (dict, list) |

### Q: Что такое deadlock?

**A:**
> "Deadlock — ситуация когда два или более потоков ждут ресурсы друг друга и никто не может продолжить. Например: Thread A держит Lock 1 и ждёт Lock 2, Thread B держит Lock 2 и ждёт Lock 1."

---

## 🔧 Оптимизация кода

**Сценарий:** Функция с I/O и CPU операциями работает медленно.

**Ответ:**

1. **Профилировать** — определить что bottleneck
2. **I/O часть** — вынести в threads или asyncio
3. **CPU часть** — вынести в multiprocessing
4. **Общее** — рассмотреть batching, caching, background workers

---

## 📚 Дополнительные материалы

- [Python docs: threading](https://docs.python.org/3/library/threading.html)
- [Python docs: multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [Real Python: Speed Up Python With Concurrency](https://realpython.com/python-concurrency/)
- "Fluent Python" Chapter 19: Concurrency with Futures

---


