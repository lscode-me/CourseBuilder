# Функции и модули
## Функции, возврат значений, модули

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать управление потоком в Rust (см. модуль [05_Control_Flow](../05_Control_Flow/))
- Знать переменные и типы (см. модуль [04_Variables_Types](../04_Variables_Types/))
- Понимать базовые концепции программирования: функции, параметры

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать функции с параметрами и возвращаемыми значениями
- Понимать разницу между выражениями и операторами
- Организовывать код в модули
- Использовать pub для контроля видимости
- Применять функции в практических задачах

---

## 1. Определение функций

### 1.1 Базовый синтаксис

В Rust функции определяются с помощью ключевого слова `fn`.

**Example: Простая функция**

```rust

fn greet() {
    println!("Hello, Rust!");
}

fn main() {
    greet();
}
```

**Output:**
```

Hello, Rust!
```

### 1.2 Функции с параметрами

**Example: Функция с параметрами**

```rust

fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {
    greet("Alice");
    greet("Bob");
}
```

**Output:**
```

Hello, Alice!
Hello, Bob!
```

**Важно:** Типы параметров должны быть указаны явно!

### 1.3 Функции с несколькими параметрами

**Example: Несколько параметров**

```rust

fn add(x: i32, y: i32) {
    println!("{} + {} = {}", x, y, x + y);
}

fn main() {
    add(5, 3);
    add(10, 20);
}
```

**Output:**
```

5 + 3 = 8
10 + 20 = 30
```

---

## 2. Возврат значений

### 2.1 Явный return

**Example: Использование return**

```rust

fn add(x: i32, y: i32) -> i32 {
    return x + y;
}

fn main() {
    let result = add(5, 3);
    println!("Результат: {}", result);
}
```

**Output:**
```

Результат: 8
```

### 2.2 Выражения без return

В Rust последнее выражение без точки с запятой автоматически возвращается.

**Example: Выражение как возвращаемое значение**

```rust

fn add(x: i32, y: i32) -> i32 {
    x + y  // Нет точки с запятой - это выражение
}

fn main() {
    let result = add(5, 3);
    println!("Результат: {}", result);
}
```

**Output:**
```

Результат: 8
```

**Важно:** Точка с запятой превращает выражение в оператор!

**Example: Ошибка — точка с запятой**

```rust

fn add(x: i32, y: i32) -> i32 {
    x + y;  // Ошибка: это оператор, не выражение
}

fn main() {
    let result = add(5, 3);
    println!("Результат: {}", result);
}
```

**Ошибка компиляции:**
```

error[E0308]: mismatched types
 --> src/main.rs:2:5
  |
2 |     x + y;
  |     ^^^^^ expected `i32`, found `()`
```

### 2.3 Разница между выражениями и операторами

**Выражение** — вычисляет значение:
```rust

5 + 3  // Выражение, возвращает 8
```

**Оператор** — выполняет действие, не возвращает значение:
```rust

let x = 5;  // Оператор, возвращает ()
```

**Example: Выражения vs операторы**

```rust

fn main() {
    let x = 5;           // Оператор
    let y = {
        let a = 3;       // Оператор
        a + 2            // Выражение (без ;)
    };                   // y = 5
    
    println!("x = {}, y = {}", x, y);
}
```

**Output:**
```

x = 5, y = 5
```

---

## 3. Различные типы возвращаемых значений

### 3.1 Возврат примитивных типов

**Example: Различные типы**

```rust

fn get_number() -> i32 {
    42
}

fn get_float() -> f64 {
    3.14
}

fn get_bool() -> bool {
    true
}

fn main() {
    println!("Число: {}", get_number());
    println!("Дробное: {}", get_float());
    println!("Булево: {}", get_bool());
}
```

**Output:**
```

Число: 42
Дробное: 3.14
Булево: true
```

### 3.2 Возврат кортежей

**Example: Возврат нескольких значений**

```rust

fn calculate(x: i32, y: i32) -> (i32, i32, i32, i32) {
    (x + y, x - y, x * y, x / y)
}

fn main() {
    let (sum, diff, prod, quot) = calculate(10, 5);
    println!("Сумма: {}, Разность: {}, Произведение: {}, Частное: {}", 
             sum, diff, prod, quot);
}
```

**Output:**
```

Сумма: 15, Разность: 5, Произведение: 50, Частное: 2
```

---

## 4. Практические примеры функций

### 4.1 Пример: Факториал

```rust

fn factorial(n: u32) -> u32 {
    if n <= 1 {
        1
    } else {
        n * factorial(n - 1)
    }
}

fn main() {
    for i in 1..=5 {
        println!("{}! = {}", i, factorial(i));
    }
}
```

**Output:**
```

1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

### 4.2 Пример: Проверка простого числа

```rust

fn is_prime(n: u32) -> bool {
    if n < 2 {
        return false;
    }
    
    for i in 2..n {
        if n % i == 0 {
            return false;
        }
    }
    
    true
}

fn main() {
    for num in 2..=20 {
        if is_prime(num) {
            println!("{} - простое число", num);
        }
    }
}
```

**Output:**
```

2 - простое число
3 - простое число
5 - простое число
7 - простое число
11 - простое число
13 - простое число
17 - простое число
19 - простое число
```

---

## 5. Модули

### 5.1 Что такое модули

**Модули** позволяют организовать код в логические группы и контролировать видимость.

**Example: Простой модуль**

```rust

mod math {
    pub fn add(x: i32, y: i32) -> i32 {
        x + y
    }
    
    fn subtract(x: i32, y: i32) -> i32 {
        x - y
    }
}

fn main() {
    println!("5 + 3 = {}", math::add(5, 3));
    // println!("5 - 3 = {}", math::subtract(5, 3));  // Ошибка: функция не публичная
}
```

**Output:**
```

5 + 3 = 8
```

### 5.2 Видимость: pub

**pub** делает элемент публичным (доступным извне модуля).

**Example: Публичные и приватные функции**

```rust

mod calculator {
    pub fn add(x: i32, y: i32) -> i32 {
        x + y
    }
    
    fn subtract(x: i32, y: i32) -> i32 {
        x - y
    }
    
    pub fn multiply(x: i32, y: i32) -> i32 {
        x * y
    }
}

fn main() {
    println!("5 + 3 = {}", calculator::add(5, 3));
    println!("5 * 3 = {}", calculator::multiply(5, 3));
    // calculator::subtract(5, 3);  // Ошибка: функция приватная
}
```

**Output:**
```

5 + 3 = 8
5 * 3 = 15
```

### 5.3 Вложенные модули

**Example: Вложенные модули**

```rust

mod math {
    pub mod basic {
        pub fn add(x: i32, y: i32) -> i32 {
            x + y
        }
    }
    
    pub mod advanced {
        pub fn power(base: i32, exp: u32) -> i32 {
            let mut result = 1;
            for _ in 0..exp {
                result *= base;
            }
            result
        }
    }
}

fn main() {
    println!("5 + 3 = {}", math::basic::add(5, 3));
    println!("2^8 = {}", math::advanced::power(2, 8));
}
```

**Output:**
```

5 + 3 = 8
2^8 = 256
```

---

## 6. use для импорта

### 6.1 Базовое использование use

**use** позволяет импортировать модули для более короткого синтаксиса.

**Example: Импорт модуля**

```rust

mod math {
    pub fn add(x: i32, y: i32) -> i32 {
        x + y
    }
    
    pub fn multiply(x: i32, y: i32) -> i32 {
        x * y
    }
}

use math::add;

fn main() {
    println!("5 + 3 = {}", add(5, 3));
    println!("5 * 3 = {}", math::multiply(5, 3));
}
```

**Output:**
```

5 + 3 = 8
5 * 3 = 15
```

### 6.2 Импорт нескольких элементов

**Example: Импорт нескольких функций**

```rust

mod math {
    pub fn add(x: i32, y: i32) -> i32 {
        x + y
    }
    
    pub fn multiply(x: i32, y: i32) -> i32 {
        x * y
    }
}

use math::{add, multiply};

fn main() {
    println!("5 + 3 = {}", add(5, 3));
    println!("5 * 3 = {}", multiply(5, 3));
}
```

**Output:**
```

5 + 3 = 8
5 * 3 = 15
```

### 6.3 Импорт всего модуля

**Example: Импорт всего модуля**

```rust

mod math {
    pub fn add(x: i32, y: i32) -> i32 {
        x + y
    }
    
    pub fn multiply(x: i32, y: i32) -> i32 {
        x * y
    }
}

use math::*;

fn main() {
    println!("5 + 3 = {}", add(5, 3));
    println!("5 * 3 = {}", multiply(5, 3));
}
```

**Output:**
```

5 + 3 = 8
5 * 3 = 15
```

> **⚠️ Warning:**  
> Использование `use module::*` может привести к конфликтам имён. Используйте осторожно!

---

## 7. Модули в отдельных файлах

### 7.1 Структура проекта

**Example: Модуль в отдельном файле**

**src/main.rs:**
```rust

mod math;

fn main() {
    println!("5 + 3 = {}", math::add(5, 3));
}
```

**src/math.rs:**
```rust

pub fn add(x: i32, y: i32) -> i32 {
    x + y
}

pub fn multiply(x: i32, y: i32) -> i32 {
    x * y
}
```

**Output:**
```

5 + 3 = 8
```

### 7.2 Вложенные модули в файлах

**Example: Вложенные модули**

**src/main.rs:**
```rust

mod math;

fn main() {
    println!("5 + 3 = {}", math::basic::add(5, 3));
}
```

**src/math/mod.rs:**
```rust

pub mod basic;

pub mod advanced {
    pub fn power(base: i32, exp: u32) -> i32 {
        let mut result = 1;
        for _ in 0..exp {
            result *= base;
        }
        result
    }
}
```

**src/math/basic.rs:**
```rust

pub fn add(x: i32, y: i32) -> i32 {
    x + y
}
```

**Output:**
```

5 + 3 = 8
```

---

## 8. Практический пример: Организация кода

### 8.1 Пример: Структура проекта

**Структура:**
```

my_project/
├── Cargo.toml
└── src/
    ├── main.rs
    ├── math.rs
    └── utils.rs
```

**src/main.rs:**
```rust

mod math;
mod utils;

use math::{add, multiply};
use utils::greet;

fn main() {
    greet("Rust");
    println!("5 + 3 = {}", add(5, 3));
    println!("5 * 3 = {}", multiply(5, 3));
}
```

**src/math.rs:**
```rust

pub fn add(x: i32, y: i32) -> i32 {
    x + y
}

pub fn multiply(x: i32, y: i32) -> i32 {
    x * y
}
```

**src/utils.rs:**
```rust

pub fn greet(name: &str) {
    println!("Hello, {}!", name);
}
```

**Output:**
```

Hello, Rust!
5 + 3 = 8
5 * 3 = 15
```

---

## 💡 Key Takeaways

- **fn определяет функции:** Типы параметров и возвращаемого значения обязательны

- **Выражения vs операторы:** Последнее выражение без ; возвращается автоматически

- **Модули организуют код:** Позволяют логически группировать функциональность

- **pub контролирует видимость:** По умолчанию всё приватно, pub делает публичным

- **use упрощает импорт:** Позволяет использовать короткие имена вместо полных путей

---

## 🚀 Next Steps

**Related Modules:**

- [Ownership и Borrowing](../07_Ownership_Borrowing/) — ключевая концепция Rust
- [Struct и Enum](../08_Struct_Enum/) — пользовательские типы данных

**Practice Ideas:**

1. Создайте модуль с математическими функциями
2. Организуйте код в несколько модулей
3. Реализуйте рекурсивные функции (факториал, Фибоначчи)
4. Попробуйте создать библиотечный проект с модулями

**Going Deeper:**

- Изучите crate и workspace
- Почитайте о visibility modifiers (pub(crate), pub(super))
- Изучите re-exports с помощью pub use

---

## 📚 Additional Resources

**Documentation:**

- [Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html) — документация по функциям
- [Modules](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html) — документация по модулям

**Practice:**

- [Rustlings: Functions](https://github.com/rust-lang/rustlings) — упражнения

---


