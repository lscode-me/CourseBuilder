# ООП и контрактные протоколы
## Интерфейсы как протоколы, Duck typing, LSP, Design by contract

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы ООП (классы, наследование, полиморфизм)
- Понимать концепцию протокола (модуль 01)
- Владеть Python или другим ООП языком

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать интерфейсы как протоколы взаимодействия
- Применять принцип duck typing для гибкого проектирования
- Понимать и применять Liskov Substitution Principle
- Использовать design by contract для формализации ожиданий

---

## 1. Введение: контракты в ООП

В ООП **контракты** — это формализованные ожидания о поведении объектов. Они определяют:

- Какие методы должен иметь объект
- Какие аргументы принимают методы
- Что методы возвращают
- Какие гарантии даёт объект

Контракты позволяют писать код, который работает с абстракциями, а не с конкретными реализациями, обеспечивая гибкость и расширяемость.

---

## 2. Интерфейсы как протоколы

### 2.1 Концепция интерфейса

**Интерфейс** — формальное определение методов, которые должен реализовать класс.

**Интерфейс определяет:**

- Сигнатуры методов (имя, параметры, возвращаемый тип)
- Поведенческие ожидания (что делает метод)
- Не определяет реализацию

### 2.2 Интерфейсы в Python (ABC)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Interface for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process payment and return success status"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, amount: float) -> bool:
        """Refund payment and return success status"""
        pass

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Stripe")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"Refunding ${amount} for transaction {transaction_id}")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"Refunding ${amount} for transaction {transaction_id}")
        return True

# Использование

def checkout(processor: PaymentProcessor, amount: float):
    if processor.process_payment(amount):
        print("Payment successful!")

checkout(StripeProcessor(), 100.0)
checkout(PayPalProcessor(), 50.0)
```

**Output:**
```
Processing $100.0 via Stripe
Payment successful!
Processing $50.0 via PayPal
Payment successful!
```

### 2.3 Преимущества интерфейсов

- **Полиморфизм**: разные реализации одного интерфейса

- **Тестируемость**: легко создавать mock объекты

- **Расширяемость**: добавление новых реализаций без изменения кода

- **Документация**: интерфейс — это контракт

---

## 3. Duck Typing

### 3.1 Концепция

**Duck typing** — "если это ходит как утка и крякает как утка, то это утка".

Объект считается совместимым, если он имеет нужные методы, независимо от типа или наследования.

### 3.2 Пример duck typing

```python
class File:
    def read(self):
        return "File content"
    
    def close(self):
        print("File closed")

class Network:
    def read(self):
        return "Network data"
    
    def close(self):
        print("Connection closed")

class StringBuffer:
    def __init__(self, data):
        self.data = data
    
    def read(self):
        return self.data
    
    def close(self):
        print("Buffer cleared")

def process_readable(obj):
    """Works with any object that has read() and close()"""
    data = obj.read()
    print(f"Data: {data}")
    obj.close()

# Все три типа работают без общего интерфейса

process_readable(File())
process_readable(Network())
process_readable(StringBuffer("Buffer content"))
```

**Output:**
```
Data: File content
File closed
Data: Network data
Connection closed
Data: Buffer content
Buffer cleared
```

### 3.3 Protocol (typing.Protocol)

Python 3.8+ добавил `Protocol` для явного определения duck typing:

```python
from typing import Protocol

class Readable(Protocol):
    def read(self) -> str: ...
    def close(self) -> None: ...

def process_readable(obj: Readable):
    """Type checker verifies obj has read() and close()"""
    data = obj.read()
    print(f"Data: {data}")
    obj.close()

# Любой класс с нужными методами проходит проверку типов
```

### 3.4 Duck typing vs интерфейсы

**Duck typing:**

- Гибче: не требует явного наследования
- Проще: не нужно объявлять интерфейсы
- Опаснее: ошибки обнаруживаются в runtime

**Интерфейсы:**

- Явнее: понятно, какой контракт
- Безопаснее: ошибки обнаруживаются раньше
- Жёстче: требует явного наследования

---

## 4. Liskov Substitution Principle (LSP)

### 4.1 Определение

**LSP**: объекты подтипа должны быть заменяемы объектами базового типа без изменения корректности программы.

**Формально:** если S — подтип T, то объекты типа T могут быть заменены объектами типа S без нарушения свойств программы.

### 4.2 Нарушение LSP

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    """Нарушает LSP!"""
    def set_width(self, width):
        self.width = width
        self.height = width  # Нарушает ожидания
    
    def set_height(self, height):
        self.width = height  # Нарушает ожидания
        self.height = height

def test_rectangle(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(10)
    assert rect.area() == 50, "Expected area 50"

# Работает с Rectangle

test_rectangle(Rectangle(0, 0))

# Ломается с Square!
# test_rectangle(Square(0))  # AssertionError
```

### 4.3 Правильный дизайн

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self) -> float:
        return self.side * self.side

# Оба следуют контракту Shape, но не наследуют друг друга
```

### 4.4 Правила LSP

1. **Preconditions** не могут быть усилены в подтипе
2. **Postconditions** не могут быть ослаблены в подтипе
3. **Invariants** базового типа должны сохраняться
4. **History constraint**: подтип не может менять состояние, недоступное базовому типу

---

## 5. Design by Contract

### 5.1 Концепция

**Design by Contract** — методология, где каждый компонент имеет формальный контракт:

**Компоненты контракта:**

- **Preconditions** (предусловия): что должно быть истинно перед вызовом

- **Postconditions** (постусловия): что гарантируется после вызова

- **Invariants** (инварианты): что всегда истинно для объекта

### 5.2 Пример с assert

```python
class BankAccount:
    def __init__(self, balance: float):
        # Invariant: balance >= 0
        assert balance >= 0, "Balance cannot be negative"
        self._balance = balance
    
    def withdraw(self, amount: float) -> bool:
        # Precondition: amount > 0
        assert amount > 0, "Amount must be positive"
        
        # Precondition: sufficient funds
        if self._balance < amount:
            return False
        
        self._balance -= amount
        
        # Postcondition: balance decreased by amount
        # Invariant: balance >= 0 (maintained)
        assert self._balance >= 0, "Invariant violated"
        
        return True
    
    def deposit(self, amount: float):
        # Precondition
        assert amount > 0, "Amount must be positive"
        
        old_balance = self._balance
        self._balance += amount
        
        # Postcondition
        assert self._balance == old_balance + amount
        # Invariant maintained
        assert self._balance >= 0

account = BankAccount(100)
account.withdraw(50)
account.deposit(25)
print(f"Balance: {account._balance}")
```

**Output:**
```
Balance: 75.0
```

### 5.3 Декораторы для контрактов

```python
def requires(precondition, message="Precondition failed"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not precondition(*args, **kwargs):
                raise ValueError(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def ensures(postcondition, message="Postcondition failed"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not postcondition(result, *args, **kwargs):
                raise ValueError(message)
            return result
        return wrapper
    return decorator

class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance
    
    @requires(lambda self, amount: amount > 0, "Amount must be positive")
    @requires(lambda self, amount: self._balance >= amount, "Insufficient funds")
    @ensures(lambda result, self, amount: result == True, "Withdrawal must succeed")
    def withdraw(self, amount: float) -> bool:
        self._balance -= amount
        return True
```

### 5.4 Преимущества DbC

- **Ясность**: явные ожидания

- **Отладка**: ошибки обнаруживаются раньше

- **Документация**: контракты — это документация

- **Верификация**: можно автоматически проверять

---

## 6. SOLID принципы и протоколы

### 6.1 Interface Segregation Principle

**ISP**: клиенты не должны зависеть от интерфейсов, которые не используют.

**Плохо:**
```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    
    @abstractmethod
    def eat(self): pass

class Robot(Worker):
    def work(self): pass
    def eat(self): pass  # Роботы не едят!
```

**Хорошо:**
```python
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): pass
    def eat(self): pass

class Robot(Workable):
    def work(self): pass
```

### 6.2 Dependency Inversion Principle

**DIP**: зависеть от абстракций, а не от конкретных реализаций.

**Плохо:**
```python
class EmailSender:
    def send(self, message): pass

class NotificationService:
    def __init__(self):
        self.sender = EmailSender()  # Зависимость от конкретного класса
```

**Хорошо:**
```python
class MessageSender(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailSender(MessageSender):
    def send(self, message): pass

class SMSSender(MessageSender):
    def send(self, message): pass

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Зависимость от абстракции
```

---

## 💡 Key Takeaways

- **Интерфейсы формализуют контракты**: ABC в Python позволяет определять интерфейсы, обеспечивая полиморфизм и расширяемость без изменения существующего кода.

- **Duck typing для гибкости**: Объекты совместимы, если имеют нужные методы, независимо от типа. typing.Protocol делает duck typing явным и проверяемым.

- **LSP обеспечивает корректную замену**: Подтипы должны быть заменяемы базовыми типами без нарушения корректности. Нарушение LSP приводит к неожиданным ошибкам.

- **Design by Contract для надёжности**: Явные preconditions, postconditions и invariants делают ожидания понятными и проверяемыми, упрощая отладку и верификацию.

- **SOLID принципы и протоколы**: ISP и DIP обеспечивают правильное использование интерфейсов — небольшие, специфичные интерфейсы и зависимость от абстракций.

---

## 🚀 Next Steps

**Related Modules:**

- [11_Language_Protocols](../11_Language_Protocols/) — протоколы языков программирования: ABI, calling conventions, bytecode
- [18_Good_Vs_Bad_Protocols](../18_Good_Vs_Bad_Protocols/) — хороший vs плохой протокол: принципы дизайна

**Practice Ideas:**

1. Спроектируйте систему с использованием интерфейсов для разных способов оплаты
2. Найдите нарушение LSP в существующем коде и исправьте его
3. Реализуйте декораторы для проверки контрактов (preconditions/postconditions)

**Going Deeper:**

- Изучите formальную верификацию для автоматической проверки контрактов
- Изучите Eiffel язык, где DbC встроен в язык
- Изучите refinement types для типизации с ограничениями

---



