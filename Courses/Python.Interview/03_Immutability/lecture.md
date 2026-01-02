# Изменяемость (Mutability) в Python

## Что нужно знать для интервью

Это классическая тема Python-интервью. Вас почти наверняка спросят про "ловушку" с mutable default arguments или попросят объяснить разницу между mutable и immutable типами.

---

## 🔑 Ключевые понятия

### Mutable vs Immutable типы

| Immutable (неизменяемые) | Mutable (изменяемые) |
|--------------------------|----------------------|
| `int`, `float`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | объекты пользовательских классов |
| `bytes` | `bytearray` |

**Ответ на интервью:**
> "Immutable объекты нельзя изменить после создания — любая 'модификация' создаёт новый объект. Mutable объекты можно изменять in-place."

```python
# Immutable: создаётся новый объект

s = "hello"
s = s + " world"  # Новый объект str

# Mutable: изменяется тот же объект

lst = [1, 2, 3]
lst.append(4)  # Тот же объект list
```

---

## 💻 Классическая ловушка: Mutable Default Arguments

### Код-ловушка (вас попросят объяснить)

```python
def append_to(element, lst=[]):
    lst.append(element)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] — НЕ [2]!
print(append_to(3))  # [1, 2, 3] — НЕ [3]!
```

**Почему так происходит?**
> "Default arguments вычисляются **один раз** при определении функции, а не при каждом вызове. Поэтому все вызовы используют **один и тот же** объект списка."

### Правильное решение

```python
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

# Или короче:

def append_to(element, lst=None):
    lst = lst or []
    lst.append(element)
    return lst
```

**Ответ на интервью:**
> "Никогда не используйте mutable объекты как default arguments. Используйте None и создавайте новый объект внутри функции."

---

## 💻 Другие примеры

### Копирование списков

```python
# ❌ Это НЕ копия, это ссылка на тот же объект

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] — изменился и a!

# ✅ Shallow copy

b = a.copy()  # или b = a[:] или b = list(a)

# ✅ Deep copy (для вложенных структур)

import copy
b = copy.deepcopy(a)
```

### Почему tuple может содержать mutable объекты?

```python
t = ([1, 2], [3, 4])
t[0].append(5)  # Работает!
print(t)  # ([1, 2, 5], [3, 4])

# Но нельзя заменить элемент

t[0] = [6, 7]  # TypeError: tuple doesn't support item assignment
```

**Ответ:**
> "Tuple хранит **ссылки** на объекты, и эти ссылки immutable. Но если ссылка указывает на mutable объект, сам объект можно изменить."

---

## ❓ Типичные вопросы на интервью

### Q: Почему immutability важна?

**A:**

- **Thread safety** — immutable объекты безопасны для многопоточного доступа

- **Хэширование** — immutable объекты можно использовать как ключи dict и элементы set

- **Предсказуемость** — функция не может случайно изменить ваши данные

- **Кэширование** — можно безопасно кэшировать immutable объекты

### Q: Можно ли использовать список как ключ словаря?

**A:**
> "Нет, потому что list — mutable. Ключи словаря должны быть hashable, а hashable могут быть только immutable объекты. Используйте tuple вместо list."

```python
d = {}
d[[1, 2, 3]] = "value"  # TypeError: unhashable type: 'list'
d[(1, 2, 3)] = "value"  # Работает
```

### Q: Как сделать class immutable?

**A:**
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 3  # FrozenInstanceError
```

---

## 📚 Дополнительные материалы

- [Python docs: Data Model](https://docs.python.org/3/reference/datamodel.html)
- "Fluent Python" Chapter 8: Object References, Mutability, and Recycling
- [Real Python: Pass by Reference in Python](https://realpython.com/python-pass-by-reference/)

---



