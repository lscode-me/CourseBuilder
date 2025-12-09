# Python Classes
## Классы, объекты и основы ООП

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь создавать и вызывать функции
- Понимать области видимости переменных
- Знать работу со словарями и списками
- Иметь базовое представление о структурах данных

**Recommended prior modules:**
- [Functions](../04_Functions/) — функции, параметры, декораторы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать классы с атрибутами и методами
- Использовать конструктор `__init__` для инициализации объектов
- Применять наследование для переиспользования кода
- Понимать инкапсуляцию и соглашения о приватности
- Использовать специальные методы (dunder methods)

---

## 1. Введение в ООП

Объектно-ориентированное программирование (ООП) — парадигма, в которой программа строится вокруг объектов, объединяющих данные и поведение.

### 1.1 Зачем нужны классы

```python
# Без классов — данные и функции разрозненны
user1_name = "Alice"
user1_age = 30
user1_email = "alice@example.com"

def greet_user(name):
    return f"Hello, {name}!"

print(greet_user(user1_name))

# С классами — данные и поведение вместе
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def greet(self):
        return f"Hello, {self.name}!"

user1 = User("Alice", 30, "alice@example.com")
print(user1.greet())
```

**Output:**
```
Hello, Alice!
Hello, Alice!
```

### 1.2 Класс и объект

- **Класс** — шаблон (чертёж) для создания объектов
- **Объект (экземпляр)** — конкретная реализация класса

```python
class Dog:
    """Класс, представляющий собаку."""
    species = "Canis familiaris"  # Атрибут класса
    
    def __init__(self, name, age):
        self.name = name  # Атрибут экземпляра
        self.age = age
    
    def bark(self):
        return f"{self.name} говорит: Гав!"

# Создание объектов
buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)

print(f"{buddy.name} — {buddy.species}")
print(f"{max_dog.name} — {max_dog.species}")
print(buddy.bark())
print(max_dog.bark())
```

**Output:**
```
Buddy — Canis familiaris
Max — Canis familiaris
Buddy говорит: Гав!
Max говорит: Гав!
```

---

## 2. Создание классов

### 2.1 Метод __init__

`__init__` — конструктор, вызывается при создании объекта:

```python
class Rectangle:
    def __init__(self, width, height):
        """Инициализирует прямоугольник."""
        self.width = width
        self.height = height
        print(f"Создан прямоугольник {width}x{height}")
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"Площадь: {rect.area()}")
print(f"Периметр: {rect.perimeter()}")
```

**Output:**
```
Создан прямоугольник 10x5
Площадь: 50
Периметр: 30
```

### 2.2 Атрибуты класса vs атрибуты экземпляра

```python
class Counter:
    count = 0  # Атрибут класса — общий для всех экземпляров
    
    def __init__(self, name):
        self.name = name  # Атрибут экземпляра — уникален
        Counter.count += 1
    
    def __del__(self):
        Counter.count -= 1

c1 = Counter("first")
c2 = Counter("second")
c3 = Counter("third")

print(f"Всего счётчиков: {Counter.count}")
print(f"c1.count: {c1.count}")  # Доступ через экземпляр тоже работает

del c3
print(f"После удаления: {Counter.count}")
```

**Output:**
```
Всего счётчиков: 3
c1.count: 3
После удаления: 2
```

### 2.3 Методы экземпляра

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Пополнение счёта."""
        if amount > 0:
            self.balance += amount
            return f"Внесено {amount}. Баланс: {self.balance}"
        return "Сумма должна быть положительной"
    
    def withdraw(self, amount):
        """Снятие со счёта."""
        if amount > self.balance:
            return "Недостаточно средств"
        self.balance -= amount
        return f"Снято {amount}. Баланс: {self.balance}"
    
    def get_balance(self):
        return f"Баланс {self.owner}: {self.balance}"

account = BankAccount("Alice", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
```

**Output:**
```
Баланс Alice: 1000
Внесено 500. Баланс: 1500
Снято 200. Баланс: 1300
Недостаточно средств
```

---

## 3. Инкапсуляция

### 3.1 Соглашения о приватности

Python использует соглашения об именовании для обозначения приватности:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name           # Публичный атрибут
        self._department = "Unknown"  # "Защищённый" (convention)
        self.__salary = salary     # "Приватный" (name mangling)
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Зарплата должна быть положительной")

emp = Employee("Alice", 50000)
print(f"Имя: {emp.name}")           # OK
print(f"Отдел: {emp._department}")   # OK, но не рекомендуется извне
print(f"Зарплата: {emp.get_salary()}")

# emp.__salary  # AttributeError!
# Но можно обойти через name mangling (не делайте так!)
print(f"Через mangling: {emp._Employee__salary}")
```

**Output:**
```
Имя: Alice
Отдел: Unknown
Зарплата: 50000
Через mangling: 50000
```

### 3.2 Property декоратор

`@property` позволяет создавать управляемые атрибуты:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter для radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter для radius."""
        if value < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self._radius = value
    
    @property
    def area(self):
        """Вычисляемое свойство (только чтение)."""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def diameter(self):
        return self._radius * 2

circle = Circle(5)
print(f"Радиус: {circle.radius}")
print(f"Диаметр: {circle.diameter}")
print(f"Площадь: {circle.area:.2f}")

circle.radius = 10
print(f"Новый радиус: {circle.radius}")
print(f"Новая площадь: {circle.area:.2f}")

# circle.area = 100  # AttributeError — нет setter
```

**Output:**
```
Радиус: 5
Диаметр: 10
Площадь: 78.54
Новый радиус: 10
Новая площадь: 314.16
```

---

## 4. Наследование

### 4.1 Базовое наследование

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Подкласс должен реализовать этот метод")
    
    def describe(self):
        return f"Это {self.name}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"

# Использование
dog = Dog("Шарик")
cat = Cat("Мурка")

print(dog.describe())  # Унаследовано от Animal
print(dog.speak())     # Переопределено в Dog

print(cat.describe())
print(cat.speak())
```

**Output:**
```
Это Шарик
Шарик говорит: Гав!
Это Мурка
Мурка говорит: Мяу!
```

### 4.2 Расширение родительского класса

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Вызов конструктора родителя
        self.doors = doors
    
    def info(self):
        # Расширяем метод родителя
        return f"{super().info()} ({self.doors} двери)"

class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity
    
    def info(self):
        return f"{super().info()}, батарея {self.battery_capacity} кВт·ч"

tesla = ElectricCar("Tesla", "Model 3", 4, 75)
print(tesla.info())
print(f"isinstance(tesla, Car): {isinstance(tesla, Car)}")
print(f"isinstance(tesla, Vehicle): {isinstance(tesla, Vehicle)}")
```

**Output:**
```
Tesla Model 3 (4 двери), батарея 75 кВт·ч
isinstance(tesla, Car): True
isinstance(tesla, Vehicle): True
```

### 4.3 Множественное наследование

```python
class Flyable:
    def fly(self):
        return "Летит!"

class Swimmable:
    def swim(self):
        return "Плывёт!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} говорит: Кря!"

duck = Duck("Дональд")
print(duck.describe())  # От Animal
print(duck.speak())     # Собственный
print(duck.fly())       # От Flyable
print(duck.swim())      # От Swimmable

# Method Resolution Order (MRO)
print(f"\nMRO: {Duck.__mro__}")
```

**Output:**
```
Это Дональд
Дональд говорит: Кря!
Летит!
Плывёт!

MRO: (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Flyable'>, <class '__main__.Swimmable'>, <class 'object'>)
```

---

## 5. Специальные методы (Dunder Methods)

### 5.1 Строковое представление

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """Для пользователя (print, str())."""
        return f"Точка({self.x}, {self.y})"
    
    def __repr__(self):
        """Для разработчика (отладка, repr())."""
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(str(p))   # Вызывает __str__
print(repr(p))  # Вызывает __repr__
print(p)        # print использует __str__
print([p])      # В коллекциях используется __repr__
```

**Output:**
```
Точка(3, 4)
Point(x=3, y=4)
Точка(3, 4)
[Point(x=3, y=4)]
```

### 5.2 Операторы сравнения

```python
class Money:
    def __init__(self, amount, currency="RUB"):
        self.amount = amount
        self.currency = currency
    
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Нельзя сравнивать разные валюты")
        return self.amount < other.amount
    
    def __le__(self, other):
        return self == other or self < other
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

m1 = Money(100)
m2 = Money(100)
m3 = Money(200)

print(f"m1 == m2: {m1 == m2}")
print(f"m1 < m3: {m1 < m3}")
print(f"m3 <= m1: {m3 <= m1}")
```

**Output:**
```
m1 == m2: True
m1 < m3: True
m3 <= m1: False
```

### 5.3 Арифметические операторы

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v2 = {3 * v2}")
print(f"|v1| = {abs(v1)}")
```

**Output:**
```
v1 + v2 = Vector(4, 6)
v1 - v2 = Vector(2, 2)
v1 * 2 = Vector(6, 8)
3 * v2 = Vector(3, 6)
|v1| = 5.0
```

### 5.4 Контейнерные методы

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []
    
    def add(self, song):
        self._songs.append(song)
    
    def __len__(self):
        return len(self._songs)
    
    def __getitem__(self, index):
        return self._songs[index]
    
    def __setitem__(self, index, value):
        self._songs[index] = value
    
    def __contains__(self, song):
        return song in self._songs
    
    def __iter__(self):
        return iter(self._songs)
    
    def __repr__(self):
        return f"Playlist('{self.name}', {len(self)} songs)"

playlist = Playlist("My Favorites")
playlist.add("Song A")
playlist.add("Song B")
playlist.add("Song C")

print(f"Длина: {len(playlist)}")
print(f"Первая песня: {playlist[0]}")
print(f"'Song B' in playlist: {'Song B' in playlist}")

print("\nВсе песни:")
for song in playlist:
    print(f"  - {song}")
```

**Output:**
```
Длина: 3
Первая песня: Song A
'Song B' in playlist: True

Все песни:
  - Song A
  - Song B
  - Song C
```

### 5.5 Context Manager

```python
class Timer:
    def __init__(self, name="Timer"):
        self.name = name
    
    def __enter__(self):
        import time
        self.start = time.time()
        print(f"{self.name} запущен")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"{self.name} завершён за {elapsed:.4f}с")
        return False  # Не подавлять исключения

# Использование
with Timer("Вычисление"):
    total = sum(range(1000000))
    print(f"Сумма: {total}")
```

**Output:**
```
Вычисление запущен
Сумма: 499999500000
Вычисление завершён за 0.0312с
```

---

## 6. Методы класса и статические методы

### 6.1 @classmethod

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Альтернативный конструктор из строки."""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Создаёт дату с текущим днём."""
        from datetime import date
        d = date.today()
        return cls(d.year, d.month, d.day)
    
    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

# Использование
d1 = Date(2024, 12, 25)
d2 = Date.from_string("2024-12-31")
d3 = Date.today()

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}")
```

**Output:**
```
d1: Date(2024, 12, 25)
d2: Date(2024, 12, 31)
d3: Date(2024, 12, 2)
```

### 6.2 @staticmethod

```python
class MathUtils:
    @staticmethod
    def is_prime(n):
        """Проверяет, является ли число простым."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """Вычисляет факториал."""
        if n < 0:
            raise ValueError("Факториал не определён для отрицательных чисел")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Не нужно создавать экземпляр
print(f"is_prime(17): {MathUtils.is_prime(17)}")
print(f"is_prime(20): {MathUtils.is_prime(20)}")
print(f"factorial(5): {MathUtils.factorial(5)}")
```

**Output:**
```
is_prime(17): True
is_prime(20): False
factorial(5): 120
```

### 6.3 Сравнение методов

```python
class Demo:
    class_attr = "class attribute"
    
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
    
    def instance_method(self):
        """Имеет доступ к self и cls."""
        return f"instance: {self.instance_attr}, class: {self.class_attr}"
    
    @classmethod
    def class_method(cls):
        """Имеет доступ только к cls."""
        return f"class: {cls.class_attr}"
    
    @staticmethod
    def static_method():
        """Не имеет доступа к self и cls."""
        return "static method"

obj = Demo("instance")
print(obj.instance_method())
print(Demo.class_method())
print(Demo.static_method())
```

**Output:**
```
instance: instance, class: class attribute
class: class attribute
static method
```

---

## 7. Dataclasses (Python 3.7+)

### 7.1 Базовое использование

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # Значение по умолчанию

# Автоматически создаётся __init__, __repr__, __eq__
p1 = Point(3, 4)
p2 = Point(3, 4)

print(p1)
print(f"p1 == p2: {p1 == p2}")

person = Person("Alice", 30)
print(person)
```

**Output:**
```
Point(x=3, y=4)
p1 == p2: True
Person(name='Alice', age=30, email='')
```

### 7.2 Расширенные возможности

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    grades: List[int] = field(default_factory=list)
    _id: int = field(default=0, repr=False)  # Не показывается в repr
    
    @property
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

student = Student("Alice")
student.grades.extend([85, 90, 78])
print(student)
print(f"Средний балл: {student.average:.2f}")
```

**Output:**
```
Student(name='Alice', grades=[85, 90, 78])
Средний балл: 84.33
```

### 7.3 Frozen dataclasses

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

point = ImmutablePoint(3, 4)
print(point)

# point.x = 5  # FrozenInstanceError!

# Можно использовать как ключ словаря
points = {point: "origin"}
print(f"В словаре: {points}")
```

**Output:**
```
ImmutablePoint(x=3, y=4)
В словаре: {ImmutablePoint(x=3, y=4): 'origin'}
```

---

## 8. Абстрактные классы

### 8.1 ABC — Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Вычисляет периметр фигуры."""
        pass
    
    def describe(self):
        """Конкретный метод — можно не переопределять."""
        return f"Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# shape = Shape()  # TypeError — нельзя создать экземпляр ABC
rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Прямоугольник: {rect.describe()}")
print(f"Круг: {circle.describe()}")
```

**Output:**
```
Прямоугольник: Площадь: 50.00, Периметр: 30.00
Круг: Площадь: 153.94, Периметр: 43.98
```

---

## 9. Практические паттерны

### 9.1 Singleton

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"s1 is s2: {s1 is s2}")  # True — один и тот же объект
```

**Output:**
```
s1 is s2: True
```

### 9.2 Factory

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {
            "dog": Dog,
            "cat": Cat
        }
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        raise ValueError(f"Неизвестный тип: {animal_type}")

# Использование
dog = AnimalFactory.create("dog")
cat = AnimalFactory.create("cat")
print(dog.speak())
print(cat.speak())
```

**Output:**
```
Гав!
Мяу!
```

### 9.3 Composition over Inheritance

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Двигатель {self.horsepower} л.с. запущен"

class Wheels:
    def __init__(self, count):
        self.count = count
    
    def roll(self):
        return f"{self.count} колеса крутятся"

class Car:
    def __init__(self, brand, engine_hp, wheel_count):
        self.brand = brand
        self.engine = Engine(engine_hp)  # Композиция
        self.wheels = Wheels(wheel_count)  # Композиция
    
    def drive(self):
        return f"{self.brand}: {self.engine.start()}, {self.wheels.roll()}"

car = Car("Toyota", 150, 4)
print(car.drive())
```

**Output:**
```
Toyota: Двигатель 150 л.с. запущен, 4 колеса крутятся
```

---

## 10. Common Pitfalls

### 10.1 Забытый self

❌ **Ошибка:**
```python
class Counter:
    def __init__(self):
        count = 0  # Это локальная переменная!
    
    def increment(self):
        count += 1  # NameError
```

✅ **Правильно:**
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

c = Counter()
print(c.increment())  # 1
print(c.increment())  # 2
```

**Output:**
```
1
2
```

### 10.2 Изменяемый атрибут класса

❌ **Ошибка:**
```python
class Student:
    grades = []  # Общий для всех экземпляров!
    
    def add_grade(self, grade):
        self.grades.append(grade)

s1 = Student()
s2 = Student()
s1.add_grade(90)
print(f"s2.grades: {s2.grades}")  # [90] — неожиданно!
```

✅ **Правильно:**
```python
class Student:
    def __init__(self):
        self.grades = []  # Свой для каждого экземпляра
    
    def add_grade(self, grade):
        self.grades.append(grade)

s1 = Student()
s2 = Student()
s1.add_grade(90)
print(f"s1.grades: {s1.grades}")  # [90]
print(f"s2.grades: {s2.grades}")  # []
```

**Output:**
```
s2.grades: [90]
s1.grades: [90]
s2.grades: []
```

### 10.3 Неправильный вызов super()

❌ **Ошибка:**
```python
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(name)  # Забыли self!
```

✅ **Правильно:**
```python
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Python 3 способ
        self.age = age
```

---

## 💡 Key Takeaways

- **Классы объединяют данные и поведение**: Используйте их для моделирования сущностей из предметной области.

- **`__init__` — не конструктор, а инициализатор**: Объект уже создан к моменту вызова `__init__`.

- **Соглашения о приватности**: `_protected` и `__private` — это конвенции, не абсолютная защита.

- **Используйте @property**: Для контролируемого доступа к атрибутам и вычисляемых свойств.

- **Предпочитайте композицию наследованию**: "Has-a" часто лучше, чем "is-a".

---

## 🚀 Next Steps

**Related Modules:**
- [Modules](../06_Modules/) — организация классов в модули
- [Exceptions](../07_Exceptions/) — создание собственных исключений

**Practice Ideas:**
1. Создайте класс `BankAccount` с депозитами, снятиями и историей транзакций
2. Реализуйте иерархию геометрических фигур с абстрактным классом
3. Создайте класс `Deck` (колода карт) с методами shuffle и draw
4. Напишите dataclass для представления товара в интернет-магазине

**Going Deeper:**
- Изучите метаклассы
- Познакомьтесь с дескрипторами
- Изучите `__slots__` для оптимизации памяти

---

## 📚 Additional Resources

**Documentation:**
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [abc](https://docs.python.org/3/library/abc.html)

**Articles:**
- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)
- [Dunder Methods Guide](https://rszalski.github.io/magicmethods/)

---

