# Контекстные менеджеры в Python

## Что нужно знать для интервью

Context managers — важная тема для Python-разработчика. Вас могут попросить объяснить как работает `with`, написать свой контекстный менеджер или упростить вложенные `with` блоки.

---

## 🔑 Ключевые понятия

### Что такое контекстный менеджер?

**Ответ на интервью:**
> "Контекстный менеджер — это объект, который определяет методы `__enter__` и `__exit__` для управления ресурсами. Используется с оператором `with` для гарантированной очистки ресурсов, даже при исключениях."

### Методы `__enter__` и `__exit__`

```python
class MyContext:
    def __enter__(self):
        # Вызывается при входе в with блок
        # Возвращаемое значение присваивается переменной после as
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Вызывается при выходе из with блока
        # Получает информацию об исключении (если было)
        # Return True подавляет исключение
        return False

with MyContext() as ctx:
    # код здесь
    pass
```

---

## 💻 Код, который нужно уметь писать

### 1. Контекстный менеджер через класс

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False

# Использование
with Timer():
    sum(range(1000000))
```

### 2. Контекстный менеджер через @contextmanager

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield  # Здесь выполняется код внутри with
    finally:
        elapsed = time.time() - start
        print(f"Elapsed: {elapsed:.4f}s")

# Использование
with timer():
    sum(range(1000000))
```

### 3. Временная смена директории

```python
import os
from contextlib import contextmanager

@contextmanager
def change_dir(path):
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)

# Использование
with change_dir("/tmp"):
    print(os.getcwd())  # /tmp
print(os.getcwd())  # Вернулись в исходную директорию
```

---

## 💻 Упрощение вложенных with

### Проблема

```python
with A():
    with B():
        with C():
            with D():
                # код
```

### Решения

**Способ 1: Несколько менеджеров в одном with**

```python
with A(), B(), C(), D():
    # код
```

**Способ 2: ExitStack для динамического количества**

```python
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in file_list]
    # Все файлы будут закрыты при выходе
```

---

## ❓ Типичные вопросы на интервью

### Q: Что происходит если исключение внутри with?

**A:**
> "Метод `__exit__` всё равно вызывается. Он получает информацию об исключении через параметры `exc_type`, `exc_val`, `exc_tb`. Если `__exit__` возвращает `True`, исключение подавляется."

```python
class Suppress:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            return True  # Подавить ValueError
        return False  # Остальные исключения пробрасываются
```

### Q: Разница между классом и @contextmanager?

**A:**
| Класс | @contextmanager |
|-------|-----------------|
| Больше кода | Короче и проще |
| Можно хранить состояние | Локальные переменные |
| Можно наследовать | Нельзя наследовать |
| Лучше для сложных случаев | Лучше для простых случаев |

### Q: Какие стандартные контекстные менеджеры знаете?

**A:**
- `open()` — файлы
- `threading.Lock()` — блокировки
- `contextlib.suppress()` — подавление исключений
- `contextlib.redirect_stdout()` — перенаправление вывода
- `decimal.localcontext()` — настройки Decimal
- `unittest.mock.patch()` — мокирование

---

## 📚 Дополнительные материалы

- [Python docs: contextlib](https://docs.python.org/3/library/contextlib.html)
- [PEP 343 — The "with" Statement](https://peps.python.org/pep-0343/)
- "Fluent Python" Chapter 15: Context Managers and else Blocks

---

