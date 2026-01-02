# Struct и Enum
## struct, enum, pattern matching, Option и Result

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Знать функции и модули (см. модуль [06_Functions_Modules](../06_Functions_Modules/))
- Понимать pattern matching (см. модуль [05_Control_Flow](../05_Control_Flow/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и использовать структуры (struct)
- Определять и применять перечисления (enum)
- Использовать pattern matching с struct и enum
- Работать с Option и Result для обработки отсутствующих значений и ошибок
- Применять методы и ассоциированные функции

---

## 1. Структуры (Struct)

### 1.1 Определение структуры

**Struct** — пользовательский тип данных, группирующий связанные значения.

**Example: Простая структура**

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn main() {
    let user = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        active: true,
    };
    
    println!("Пользователь: {}", user.username);
    println!("Email: {}", user.email);
    println!("Активен: {}", user.active);
}
```

**Output:**
```
Пользователь: alice
Email: alice@example.com
Активен: true
```

### 1.2 Изменяемые структуры

**Example: Изменяемая структура**

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn main() {
    let mut user = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        active: true,
    };
    
    user.email = String::from("newemail@example.com");
    println!("Новый email: {}", user.email);
}
```

**Output:**
```
Новый email: newemail@example.com
```

### 1.3 Функции-конструкторы

**Example: Функция создания структуры**

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn build_user(username: String, email: String) -> User {
    User {
        username,
        email,
        active: true,
    }
}

fn main() {
    let user = build_user(
        String::from("bob"),
        String::from("bob@example.com")
    );
    println!("Пользователь: {}", user.username);
}
```

**Output:**
```
Пользователь: bob
```

**Сокращённый синтаксис:** Если имя поля совпадает с параметром, можно не повторять.

### 1.4 Обновление структур

**Example: Struct update syntax**

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn main() {
    let user1 = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        active: true,
    };
    
    let user2 = User {
        email: String::from("another@example.com"),
        ..user1  // Копирует остальные поля из user1
    };
    
    println!("user2: {} ({})", user2.username, user2.email);
}
```

**Output:**
```
user2: alice (another@example.com)
```

---

## 2. Tuple Structs

### 2.1 Что такое tuple struct

**Tuple struct** — структура без именованных полей.

**Example: Tuple struct**

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0);
    
    println!("Цвет: ({}, {}, {})", black.0, black.1, black.2);
    println!("Точка: ({}, {})", origin.0, origin.1);
}
```

**Output:**
```
Цвет: (0, 0, 0)
Точка: (0, 0)
```

---

## 3. Методы

### 3.1 Определение методов

**Методы** — функции, ассоциированные со структурой.

**Example: Методы**

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50,
    };
    
    println!("Площадь: {}", rect.area());
    
    let small = Rectangle {
        width: 10,
        height: 20,
    };
    
    println!("rect может содержать small? {}", rect.can_hold(&small));
}
```

**Output:**
```
Площадь: 1500
rect может содержать small? true
```

**`&self`** — ссылка на экземпляр структуры.

### 3.2 Ассоциированные функции

**Ассоциированные функции** — функции без `self`, часто используются как конструкторы.

**Example: Ассоциированная функция**

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let sq = Rectangle::square(10);
    println!("Квадрат: {}x{}", sq.width, sq.height);
}
```

**Output:**
```
Квадрат: 10x10
```

**`::`** используется для вызова ассоциированных функций.

---

## 4. Перечисления (Enum)

### 4.1 Определение enum

**Enum** — тип, который может иметь одно из нескольких возможных значений.

**Example: Простое перечисление**

```rust
enum IpAddrKind {
    V4,
    V6,
}

fn main() {
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;
    
    route(four);
    route(six);
}

fn route(ip_kind: IpAddrKind) {
    match ip_kind {
        IpAddrKind::V4 => println!("IPv4"),
        IpAddrKind::V6 => println!("IPv6"),
    }
}
```

**Output:**
```
IPv4
IPv6
```

### 4.2 Enum с данными

**Example: Enum с ассоциированными данными**

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

fn main() {
    let home = IpAddr::V4(String::from("127.0.0.1"));
    let loopback = IpAddr::V6(String::from("::1"));
    
    match home {
        IpAddr::V4(addr) => println!("IPv4: {}", addr),
        IpAddr::V6(addr) => println!("IPv6: {}", addr),
    }
}
```

**Output:**
```
IPv4: 127.0.0.1
```

### 4.3 Разные типы данных в вариантах

**Example: Разные типы в вариантах**

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
    let msg = Message::Write(String::from("hello"));
    
    match msg {
        Message::Quit => println!("Выход"),
        Message::Move { x, y } => println!("Перемещение в ({}, {})", x, y),
        Message::Write(text) => println!("Текст: {}", text),
        Message::ChangeColor(r, g, b) => println!("Цвет: RGB({}, {}, {})", r, g, b),
    }
}
```

**Output:**
```
Текст: hello
```

---

## 5. Option

### 5.1 Что такое Option

**Option** — перечисление для представления значения, которое может отсутствовать.

```rust
enum Option<T> {
    Some(T),
    None,
}
```

**Example: Использование Option**

```rust
fn main() {
    let some_number = Some(5);
    let some_string = Some("строка");
    let absent_number: Option<i32> = None;
    
    match some_number {
        Some(value) => println!("Значение: {}", value),
        None => println!("Нет значения"),
    }
}
```

**Output:**
```
Значение: 5
```

### 5.2 Option vs null

**В других языках (например, Java):**
```java
String s = null;  // Может быть null, может быть String
```

**В Rust:**
```rust
let s: Option<String> = None;  // Явно указано, что может отсутствовать
let s: String = ...;           // Всегда есть значение
```

**Преимущество:** Невозможно случайно использовать None как значение!

### 5.3 Работа с Option

**Example: Pattern matching с Option**

```rust
fn divide(a: f64, b: f64) -> Option<f64> {
    if b != 0.0 {
        Some(a / b)
    } else {
        None
    }
}

fn main() {
    match divide(10.0, 2.0) {
        Some(result) => println!("Результат: {}", result),
        None => println!("Деление на ноль!"),
    }
    
    match divide(10.0, 0.0) {
        Some(result) => println!("Результат: {}", result),
        None => println!("Деление на ноль!"),
    }
}
```

**Output:**
```
Результат: 5
Деление на ноль!
```

---

## 6. Result

### 6.1 Что такое Result

**Result** — перечисление для представления успеха или ошибки.

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

**Example: Использование Result**

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt");
    
    match f {
        Ok(file) => println!("Файл открыт успешно"),
        Err(error) => println!("Ошибка открытия файла: {:?}", error),
    }
}
```

**Output (если файл не существует):**
```
Ошибка открытия файла: Os { code: 2, kind: NotFound, message: "No such file or directory" }
```

### 6.2 Обработка ошибок

**Example: Обработка разных типов ошибок**

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");
    
    match f {
        Ok(file) => println!("Файл открыт"),
        Err(error) => match error.kind() {
            ErrorKind::NotFound => println!("Файл не найден"),
            ErrorKind::PermissionDenied => println!("Нет доступа"),
            other_error => println!("Другая ошибка: {:?}", other_error),
        },
    }
}
```

**Output:**
```
Файл не найден
```

---

## 7. if let и while let

### 7.1 if let

**if let** — упрощённый синтаксис для match с одним паттерном.

**Example: if let**

```rust
fn main() {
    let some_value = Some(3);
    
    // Вместо match:
    // match some_value {
    //     Some(3) => println!("три"),
    //     _ => (),
    // }
    
    // Можно использовать if let:
    if let Some(3) = some_value {
        println!("три");
    }
}
```

**Output:**
```
три
```

### 7.2 while let

**Example: while let**

```rust
fn main() {
    let mut stack = Vec::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    
    while let Some(top) = stack.pop() {
        println!("{}", top);
    }
}
```

**Output:**
```
3
2
1
```

---

## 8. Практические примеры

### 8.1 Пример: Структура с методами

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn new(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }
    
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    fn is_square(&self) -> bool {
        self.width == self.height
    }
}

fn main() {
    let rect = Rectangle::new(10, 20);
    println!("Площадь: {}", rect.area());
    println!("Квадрат? {}", rect.is_square());
    
    let square = Rectangle::new(15, 15);
    println!("Квадрат? {}", square.is_square());
}
```

**Output:**
```
Площадь: 200
Квадрат? false
Квадрат? true
```

### 8.2 Пример: Enum для состояний

```rust
enum State {
    Idle,
    Running,
    Paused,
    Stopped,
}

fn main() {
    let state = State::Running;
    
    match state {
        State::Idle => println!("Ожидание"),
        State::Running => println!("Работает"),
        State::Paused => println!("Приостановлено"),
        State::Stopped => println!("Остановлено"),
    }
}
```

**Output:**
```
Работает
```

---

## 💡 Key Takeaways

- **Struct группирует данные:** Позволяет создавать пользовательские типы

- **Enum представляет варианты:** Может иметь разные типы данных в вариантах

- **Option для отсутствующих значений:** Some(T) или None, безопаснее чем null

- **Result для обработки ошибок:** Ok(T) для успеха, Err(E) для ошибки

- **Pattern matching обязателен:** match должен покрывать все случаи enum

---

## 🚀 Next Steps

**Related Modules:**

- [Обработка ошибок](../09_Error_Handling/) — детальная работа с Result и ?
- [Коллекции](../10_Collections/) — Vec, HashMap, String

**Practice Ideas:**

1. Создайте структуру для представления пользователя
2. Реализуйте enum для состояний приложения
3. Напишите функции, возвращающие Option и Result
4. Используйте pattern matching для обработки всех случаев

**Going Deeper:**

- Изучите методы и ассоциированные функции подробнее
- Почитайте о derive макросах (Debug, Clone, Copy)
- Изучите ? оператор для упрощения работы с Result

---

## 📚 Additional Resources

**Documentation:**

- [Structs](https://doc.rust-lang.org/book/ch05-00-structs.html) — документация по структурам
- [Enums](https://doc.rust-lang.org/book/ch06-00-enums.html) — документация по перечислениям

**Practice:**

- [Rustlings: Structs](https://github.com/rust-lang/rustlings) — упражнения

---


