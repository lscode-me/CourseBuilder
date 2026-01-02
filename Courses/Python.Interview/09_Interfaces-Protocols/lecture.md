# Интерфейсы и протоколы в Python

## Что нужно знать для интервью

Эта тема проверяет понимание duck typing, Abstract Base Classes (ABC) и стандартных протоколов Python. Важно уметь объяснить как проверить "что умеет объект".

---

## 🔑 Ключевые понятия

### Duck Typing

**Ответ на интервью:**
> "В Python используется duck typing: 'Если оно ходит как утка и крякает как утка, это утка'. Мы не проверяем тип объекта, а только наличие нужных методов."

```python
def process(obj):
    # Не проверяем тип, просто вызываем метод
    return obj.read()

# Работает с файлом, StringIO, любым объектом с методом read()
```

### Протоколы (Protocols)

Протокол — это набор методов, которые объект должен реализовать.

| Протокол | Методы | Описание |
|----------|--------|----------|
| **Iterable** | `__iter__()` | Можно итерироваться |
| **Iterator** | `__iter__()`, `__next__()` | Итератор |
| **Callable** | `__call__()` | Можно вызвать как функцию |
| **Hashable** | `__hash__()`, `__eq__()` | Можно использовать как ключ dict |
| **Sized** | `__len__()` | Можно узнать длину |
| **Container** | `__contains__()` | Поддерживает `in` |
| **Mapping** | `__getitem__()`, `__iter__()`, `__len__()` | Словарь-подобный |
| **Sequence** | `__getitem__()`, `__len__()` | Последовательность |

---

## 💻 Abstract Base Classes (ABC)

### Зачем нужны ABC

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# dog = Animal()  # TypeError: Can't instantiate abstract class

dog = Dog()
print(dog.speak())  # Woof!
```

**Ответ на интервью:**
> "ABC позволяет определить интерфейс, который должны реализовать подклассы. Нельзя создать экземпляр абстрактного класса — нужно наследоваться и реализовать все abstractmethod."

### Абстрактный Iterable

```python
from abc import ABC, abstractmethod

class MyIterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass
```

### Абстрактный Mapping

```python
from abc import ABC, abstractmethod

class MyMapping(ABC):
    @abstractmethod
    def __getitem__(self, key):
        pass
    
    @abstractmethod
    def __setitem__(self, key, value):
        pass
    
    @abstractmethod
    def __delitem__(self, key):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __len__(self):
        pass
```

---

## 🔍 Проверка возможностей объекта

### Через collections.abc

```python
from collections.abc import Iterable, Hashable, Callable, Mapping

# Проверка iterable

isinstance([1, 2, 3], Iterable)  # True
isinstance(42, Iterable)          # False

# Проверка hashable

isinstance("hello", Hashable)     # True
isinstance([1, 2], Hashable)      # False (list mutable)

# Проверка callable

isinstance(print, Callable)       # True
isinstance(42, Callable)          # False

# Проверка mapping

isinstance({}, Mapping)           # True
isinstance([], Mapping)           # False
```

### Через hasattr (duck typing)

```python
def is_iterable(obj):
    return hasattr(obj, '__iter__')

def is_callable(obj):
    return callable(obj)  # Встроенная функция
```

---

## ❓ Типичные вопросы на интервью

### Q: Как проверить, можно ли итерироваться по объекту?

**A:**
```python
from collections.abc import Iterable

# Способ 1: isinstance

isinstance(obj, Iterable)

# Способ 2: hasattr

hasattr(obj, '__iter__')

# Способ 3: try/except

try:
    iter(obj)
    print("Iterable")
except TypeError:
    print("Not iterable")
```

### Q: Что нужно для использования объекта как ключа dict?

**A:**
> "Объект должен быть hashable — реализовать `__hash__()` и `__eq__()`, и быть immutable (или хотя бы hash не должен меняться)."

```python
# Можно: str, int, tuple (если элементы hashable)

d = {"key": 1, (1, 2): 2}

# Нельзя: list, dict, set

d = {[1, 2]: 1}  # TypeError: unhashable type: 'list'
```

### Q: Разница между duck typing и ABC?

**A:**
| Duck Typing | ABC |
|-------------|-----|
| Проверяем методы неявно | Явный интерфейс |
| Ошибка при вызове | Ошибка при создании |
| Гибко | Строже |
| Runtime проверка | Можно проверить заранее |

### Q: Назовите стандартные ABC из collections.abc

**A:**

- `Iterable`, `Iterator`, `Generator`
- `Sequence`, `MutableSequence`
- `Mapping`, `MutableMapping`
- `Set`, `MutableSet`
- `Callable`
- `Hashable`
- `Sized`, `Container`

---

## 📚 Дополнительные материалы

- [Python docs: abc](https://docs.python.org/3/library/abc.html)
- [Python docs: collections.abc](https://docs.python.org/3/library/collections.abc.html)
- "Fluent Python" Chapter 11: Interfaces, Protocols, and ABCs

---



