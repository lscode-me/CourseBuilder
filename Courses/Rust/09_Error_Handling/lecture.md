# Обработка ошибок
## panic!, Result, ? оператор

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать Option и Result (см. модуль [08_Struct_Enum](../08_Struct_Enum/))
- Знать pattern matching (см. модуль [05_Control_Flow](../05_Control_Flow/))
- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать panic! и Result для обработки ошибок
- Использовать Result для обработки восстанавливаемых ошибок
- Применять ? оператор для упрощения работы с Result
- Понимать, когда использовать panic! vs Result
- Создавать собственные типы ошибок

---

## 1. Два типа ошибок

### 1.1 Восстанавливаемые ошибки

**Восстанавливаемые ошибки** — ошибки, которые можно обработать и продолжить выполнение.

**Примеры:**

- Файл не найден
- Неверный формат данных
- Сетевая ошибка

**В Rust:** Используется `Result<T, E>`.

### 1.2 Невосстанавливаемые ошибки

**Невосстанавливаемые ошибки** — ошибки, указывающие на баг в программе.

**Примеры:**

- Выход за границы массива
- Обращение к null указателю
- Нарушение инвариантов

**В Rust:** Используется `panic!`.

---

## 2. panic!

### 2.1 Что такое panic!

**panic!** — макрос, который останавливает выполнение программы при невосстанавливаемой ошибке.

**Example: Явный panic!**

```rust
fn main() {
    panic!("Что-то пошло не так!");
}
```

**Output:**
```
thread 'main' panicked at 'Что-то пошло не так!', src/main.rs:2:5
```

### 2.2 Когда происходит panic!

**Example: Выход за границы массива**

```rust
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", v[10]);  // panic!
}
```

**Output:**
```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 10'
```

### 2.3 Когда использовать panic!

**Используйте panic! когда:**

- Ошибка указывает на баг в программе
- Невозможно продолжить выполнение
- Это ошибка программиста, а не пользователя

**Не используйте panic! когда:**

- Ошибка ожидаема (файл не найден)
- Можно обработать и продолжить
- Это ошибка пользователя или окружения

> **💡 Pro Tip:**  
> В production коде предпочитайте Result для обработки ошибок. panic! используйте только для действительно невосстанавливаемых ситуаций.

---

## 3. Result для обработки ошибок

### 3.1 Напоминание: Result

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

**Example: Базовое использование Result**

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt");
    
    match f {
        Ok(file) => println!("Файл открыт успешно"),
        Err(error) => println!("Ошибка: {:?}", error),
    }
}
```

**Output (если файл не существует):**
```
Ошибка: Os { code: 2, kind: NotFound, message: "No such file or directory" }
```

### 3.2 Обработка разных типов ошибок

**Example: Детальная обработка ошибок**

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");
    
    match f {
        Ok(file) => println!("Файл открыт"),
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                println!("Файл не найден. Создаём новый...");
                File::create("hello.txt").unwrap();
            }
            ErrorKind::PermissionDenied => {
                println!("Нет доступа к файлу");
            }
            other_error => {
                println!("Другая ошибка: {:?}", other_error);
            }
        },
    }
}
```

**Output:**
```
Файл не найден. Создаём новый...
```

---

## 4. Методы Result

### 4.1 unwrap()

**unwrap()** — извлекает значение из Ok, или вызывает panic! при Err.

**Example: unwrap()**

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").unwrap();  // panic! если ошибка
    println!("Файл открыт");
}
```

**⚠️ Warning:**  
Используйте `unwrap()` только в прототипах или когда уверены, что ошибки не будет.

### 4.2 expect()

**expect()** — как unwrap(), но с кастомным сообщением.

**Example: expect()**

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt")
        .expect("Не удалось открыть hello.txt");
    println!("Файл открыт");
}
```

**Output (если ошибка):**
```
thread 'main' panicked at 'Не удалось открыть hello.txt'
```

### 4.3 unwrap_or()

**unwrap_or()** — возвращает значение по умолчанию при ошибке.

**Example: unwrap_or()**

```rust
fn main() {
    let result: Result<i32, &str> = Err("ошибка");
    let value = result.unwrap_or(0);
    println!("Значение: {}", value);
}
```

**Output:**
```
Значение: 0
```

### 4.4 unwrap_or_else()

**unwrap_or_else()** — принимает замыкание для вычисления значения по умолчанию.

**Example: unwrap_or_else()**

```rust
fn main() {
    let result: Result<i32, &str> = Err("ошибка");
    let value = result.unwrap_or_else(|err| {
        println!("Ошибка: {}", err);
        42
    });
    println!("Значение: {}", value);
}
```

**Output:**
```
Ошибка: ошибка
Значение: 42
```

---

## 5. ? оператор

### 5.1 Что такое ? оператор

**? оператор** — упрощает обработку Result, автоматически возвращая ошибку.

**Example: Без ? оператора**

```rust
use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn main() {
    match read_username_from_file() {
        Ok(content) => println!("Содержимое: {}", content),
        Err(e) => println!("Ошибка: {}", e),
    }
}
```

**Что делает `?`:**

- Если `Result` — `Ok(value)`, извлекает значение
- Если `Result` — `Err(error)`, возвращает ошибку из функции

### 5.2 Упрощение с ?

**Example: С ? оператором**

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    let s = fs::read_to_string("hello.txt")?;
    Ok(s)
}

fn main() {
    match read_username_from_file() {
        Ok(content) => println!("Содержимое: {}", content),
        Err(e) => println!("Ошибка: {}", e),
    }
}
```

**Преимущества:**

- Код становится короче и читабельнее
- Ошибки автоматически пробрасываются
- Меньше вложенности

### 5.3 Цепочка вызовов с ?

**Example: Цепочка операций**

```rust
use std::fs::File;
use std::io;
use std::io::Read;

fn read_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn main() {
    match read_file() {
        Ok(content) => println!("{}", content),
        Err(e) => println!("Ошибка: {}", e),
    }
}
```

---

## 6. Создание собственных типов ошибок

### 6.1 Простой тип ошибки

**Example: Кастомный тип ошибки**

```rust
use std::fmt;

#[derive(Debug)]
struct MyError {
    message: String,
}

impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Ошибка: {}", self.message)
    }
}

fn might_fail(x: i32) -> Result<i32, MyError> {
    if x < 0 {
        Err(MyError {
            message: String::from("Отрицательное число"),
        })
    } else {
        Ok(x * 2)
    }
}

fn main() {
    match might_fail(5) {
        Ok(value) => println!("Результат: {}", value),
        Err(e) => println!("{}", e),
    }
    
    match might_fail(-5) {
        Ok(value) => println!("Результат: {}", value),
        Err(e) => println!("{}", e),
    }
}
```

**Output:**
```
Результат: 10
Ошибка: Отрицательное число
```

---

## 7. Практические примеры

### 7.1 Пример: Парсинг числа

```rust
fn parse_number(s: &str) -> Result<i32, std::num::ParseIntError> {
    s.parse::<i32>()
}

fn main() {
    match parse_number("42") {
        Ok(n) => println!("Число: {}", n),
        Err(e) => println!("Ошибка парсинга: {}", e),
    }
    
    match parse_number("abc") {
        Ok(n) => println!("Число: {}", n),
        Err(e) => println!("Ошибка парсинга: {}", e),
    }
}
```

**Output:**
```
Число: 42
Ошибка парсинга: invalid digit found in string
```

### 7.2 Пример: Деление с обработкой ошибок

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Деление на ноль"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(10.0, 2.0) {
        Ok(result) => println!("Результат: {}", result),
        Err(e) => println!("Ошибка: {}", e),
    }
    
    match divide(10.0, 0.0) {
        Ok(result) => println!("Результат: {}", result),
        Err(e) => println!("Ошибка: {}", e),
    }
}
```

**Output:**
```
Результат: 5
Ошибка: Деление на ноль
```

---

## 💡 Key Takeaways

- **panic! для невосстанавливаемых ошибок:** Используйте только для багов в программе

- **Result для восстанавливаемых ошибок:** Предпочтительный способ обработки ошибок

- **? оператор упрощает код:** Автоматически пробрасывает ошибки

- **unwrap() и expect() для прототипов:** Не используйте в production коде

- **Создавайте собственные типы ошибок:** Для лучшей обработки ошибок в вашем коде

---

## 🚀 Next Steps

**Related Modules:**

- [Коллекции](../10_Collections/) — Vec, HashMap, String
- [Traits и Generics](../11_Traits_Generics/) — создание переиспользуемого кода

**Practice Ideas:**

1. Напишите функции, возвращающие Result
2. Используйте ? оператор для упрощения обработки ошибок
3. Создайте собственный тип ошибки
4. Попробуйте обработать различные типы ошибок

**Going Deeper:**

- Изучите библиотеку `anyhow` для упрощения обработки ошибок
- Почитайте о `thiserror` для создания типов ошибок
- Изучите обработку ошибок в асинхронном коде

---

## 📚 Additional Resources

**Documentation:**

- [Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html) — глава из The Rust Book
- [The ? operator](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#a-shortcut-for-propagating-errors-the--operator) — документация по ? оператору

**Libraries:**

- [anyhow](https://docs.rs/anyhow/) — упрощённая обработка ошибок
- [thiserror](https://docs.rs/thiserror/) — создание типов ошибок

---


