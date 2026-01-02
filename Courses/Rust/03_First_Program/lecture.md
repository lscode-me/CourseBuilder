# Первая программа
## fn main(), println!, cargo run

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Установить Rust через rustup (см. модуль [02_Tools](../02_Tools/))
- Понимать базовые концепции программирования
- Уметь работать с командной строкой

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создать и запустить первую программу на Rust
- Понимать структуру функции main()
- Использовать макрос println! для вывода
- Запускать программы через cargo run
- Понимать разницу между компиляцией и выполнением

---

## 1. Создание первого проекта

### 1.1 Создание проекта через cargo

**Создание нового проекта:**

```bash
cargo new hello_world
cd hello_world
```

**Структура проекта:**

```
hello_world/
├── Cargo.toml
└── src/
    └── main.rs
```

### 1.2 Содержимое main.rs

**Автоматически созданный код:**

```rust
fn main() {
    println!("Hello, world!");
}
```

Это минимальная программа на Rust, которая выводит "Hello, world!".

---

## 2. Функция main()

### 2.1 Что такое main()

**main()** — точка входа в программу Rust. Каждая исполняемая программа должна иметь функцию `main()`.

**Структура функции:**

```rust
fn main() {
    // Код программы
}
```

**Компоненты:**

- `fn` — ключевое слово для определения функции
- `main` — имя функции (зарезервированное)
- `()` — параметры функции (пустые)
- `{ }` — тело функции

### 2.2 Примеры main()

**Example: Простая программа**

```rust
fn main() {
    println!("Добро пожаловать в Rust!");
}
```

**Output:**
```
Добро пожаловать в Rust!
```

**Example: Несколько операций**

```rust
fn main() {
    println!("Первая строка");
    println!("Вторая строка");
    println!("Третья строка");
}
```

**Output:**
```
Первая строка
Вторая строка
Третья строка
```

---

## 3. Макрос println!

### 3.1 Что такое println!

**println!** — макрос (не функция!) для вывода текста в консоль с переводом строки.

**Синтаксис:**

```rust
println!("Текст для вывода");
```

**Восклицательный знак (`!`)** указывает, что это макрос, а не обычная функция.

### 3.2 Базовое использование

**Example: Простой вывод**

```rust
fn main() {
    println!("Hello, Rust!");
}
```

**Output:**
```
Hello, Rust!
```

**Example: Вывод переменных**

```rust
fn main() {
    let name = "Rust";
    println!("Hello, {}!", name);
}
```

**Output:**
```
Hello, Rust!
```

**`{}`** — плейсхолдер для подстановки значений.

### 3.3 Форматирование вывода

**Example: Несколько переменных**

```rust
fn main() {
    let name = "Alice";
    let age = 30;
    println!("Имя: {}, Возраст: {}", name, age);
}
```

**Output:**
```
Имя: Alice, Возраст: 30
```

**Example: Позиционные аргументы**

```rust
fn main() {
    println!("{0} любит {1}, а {1} любит {0}", "Alice", "Bob");
}
```

**Output:**
```
Alice любит Bob, а Bob любит Alice
```

**Example: Именованные аргументы**

```rust
fn main() {
    println!("{name} работает в {company}", 
             name = "Alice", 
             company = "TechCorp");
}
```

**Output:**
```
Alice работает в TechCorp
```

### 3.4 Специальное форматирование

**Example: Выравнивание и ширина**

```rust
fn main() {
    println!("{:>10}", "right");   // Выравнивание вправо
    println!("{:<10}", "left");    // Выравнивание влево
    println!("{:^10}", "center");  // По центру
    println!("{:*^10}", "stars");  // Заполнение символами
}
```

**Output:**
```
     right
left      
  center  
**stars***
```

**Example: Числовое форматирование**

```rust
fn main() {
    let number = 42;
    println!("Десятичное: {}", number);
    println!("Двоичное: {:b}", number);
    println!("Восьмеричное: {:o}", number);
    println!("Шестнадцатеричное: {:x}", number);
    println!("Шестнадцатеричное (верхний регистр): {:X}", number);
}
```

**Output:**
```
Десятичное: 42
Двоичное: 101010
Восьмеричное: 52
Шестнадцатеричное: 2a
Шестнадцатеричное (верхний регистр): 2A
```

### 3.5 print! vs println!

**print!** — выводит без перевода строки.

**println!** — выводит с переводом строки.

**Example: Разница между print! и println!**

```rust
fn main() {
    print!("Первая строка");
    print!(" вторая часть");
    println!(" третья часть");
    println!("Вторая строка");
}
```

**Output:**
```
Первая строка вторая часть третья часть
Вторая строка
```

---

## 4. Запуск программы

### 4.1 cargo run

**Команда для компиляции и запуска:**

```bash
cargo run
```

**Output:**
```
Compiling hello_world v0.1.0 (/path/to/hello_world)
Finished dev [unoptimized + debuginfo] target(s) in 0.50s
Running `target/debug/hello_world`
Hello, world!
```

**Что происходит:**

1. Cargo компилирует проект
2. Создаётся исполняемый файл в `target/debug/`
3. Программа запускается
4. Выводится результат

### 4.2 Компиляция отдельно

**Компиляция без запуска:**

```bash
cargo build
```

**Output:**
```
Compiling hello_world v0.1.0 (/path/to/hello_world)
Finished dev [unoptimized + debuginfo] target(s) in 0.50s
```

**Запуск скомпилированного файла:**

```bash
./target/debug/hello_world
```

**Output:**
```
Hello, world!
```

### 4.3 Release сборка

**Оптимизированная сборка:**

```bash
cargo build --release
```

**Output:**
```
Compiling hello_world v0.1.0 (/path/to/hello_world)
Finished release [optimized] target(s) in 0.60s
```

**Запуск release версии:**

```bash
./target/release/hello_world
```

**Разница:**

- `debug` — быстрая компиляция, отладочная информация
- `release` — оптимизация, медленная компиляция, быстрый код

---

## 5. Полный пример программы

### 5.1 Пример: Калькулятор

```rust
fn main() {
    let a = 10;
    let b = 5;
    
    println!("Калькулятор");
    println!("a = {}, b = {}", a, b);
    println!("Сложение: {} + {} = {}", a, b, a + b);
    println!("Вычитание: {} - {} = {}", a, b, a - b);
    println!("Умножение: {} * {} = {}", a, b, a * b);
    println!("Деление: {} / {} = {}", a, b, a / b);
}
```

**Output:**
```
Калькулятор
a = 10, b = 5
Сложение: 10 + 5 = 15
Вычитание: 10 - 5 = 5
Умножение: 10 * 5 = 50
Деление: 10 / 5 = 2
```

### 5.2 Пример: Приветствие

```rust
fn main() {
    let name = "Rust";
    let version = "1.75.0";
    
    println!("Добро пожаловать в {}!", name);
    println!("Версия: {}", version);
    println!("Начнём изучение языка программирования Rust!");
}
```

**Output:**
```
Добро пожаловать в Rust!
Версия: 1.75.0
Начнём изучение языка программирования Rust!
```

---

## 6. Ошибки компиляции

### 6.1 Типичные ошибки

**Example: Отсутствие точки с запятой**

```rust
fn main() {
    println!("Hello")
    // Ошибка: ожидается `;`
}
```

**Ошибка компиляции:**
```
error: expected `;`, found `}`
 --> src/main.rs:2:24
  |
2 |     println!("Hello")
  |                        ^ help: add `;` here
```

**Исправление:**

```rust
fn main() {
    println!("Hello");
}
```

### 6.2 Ошибки в форматировании

**Example: Неправильное количество аргументов**

```rust
fn main() {
    let name = "Alice";
    println!("Hello, {} and {}", name);
    // Ошибка: недостаточно аргументов
}
```

**Ошибка компиляции:**
```
error: 2 positional arguments in format string, but there is 1 argument
 --> src/main.rs:2:32
  |
2 |     println!("Hello, {} and {}", name);
  |                                ^^   ^^
```

**Исправление:**

```rust
fn main() {
    let name = "Alice";
    let name2 = "Bob";
    println!("Hello, {} and {}", name, name2);
}
```

---

## 7. Комментарии

### 7.1 Однострочные комментарии

```rust
fn main() {
    // Это однострочный комментарий
    println!("Hello, Rust!");
    // Комментарии игнорируются компилятором
}
```

### 7.2 Многострочные комментарии

```rust
fn main() {
    /* Это многострочный
       комментарий
       на несколько строк */
    println!("Hello, Rust!");
}
```

### 7.3 Документационные комментарии

```rust
/// Это документационный комментарий
/// Используется для генерации документации
fn main() {
    println!("Hello, Rust!");
}
```

---

## 8. Практические советы

### 8.1 Использование cargo check

**Быстрая проверка без компиляции:**

```bash
cargo check
```

**Output:**
```
Checking hello_world v0.1.0 (/path/to/hello_world)
Finished dev [unoptimized + debuginfo] target(s) in 0.20s
```

**Преимущества:**

- Быстрее, чем `cargo build`
- Проверяет только синтаксис и типы
- Не создаёт исполняемый файл

### 8.2 Форматирование кода

**Автоматическое форматирование:**

```bash
cargo fmt
```

**Пример:**

**До форматирования:**
```rust
fn main(){
println!("Hello");
}
```

**После форматирования:**
```rust
fn main() {
    println!("Hello");
}
```

> **💡 Pro Tip:**  
> Используйте `cargo fmt` перед коммитом кода. Это обеспечивает единообразный стиль.

---

## 💡 Key Takeaways

- **main() — точка входа:** Каждая исполняемая программа должна иметь функцию main()

- **println! — макрос для вывода:** Используется для вывода текста в консоль с форматированием

- **cargo run компилирует и запускает:** Удобная команда для разработки

- **Компилятор помогает:** Ошибки компиляции дают полезные подсказки

- **Форматирование важно:** Используйте cargo fmt для единообразного стиля

---

## 🚀 Next Steps

**Related Modules:**

- [Переменные и типы](../04_Variables_Types/) — изучим переменные и типы данных
- [Управление потоком](../05_Control_Flow/) — условные операторы и циклы

**Practice Ideas:**

1. Создайте программу, которая выводит ваше имя и возраст
2. Напишите программу-калькулятор с несколькими операциями
3. Попробуйте различные способы форматирования вывода
4. Используйте cargo check для проверки кода

**Going Deeper:**

- Изучите другие макросы: `format!`, `eprintln!`, `dbg!`
- Почитайте о системе макросов Rust
- Попробуйте создать программу с пользовательским вводом

---

## 📚 Additional Resources

**Documentation:**

- [std::fmt](https://doc.rust-lang.org/std/fmt/) — документация по форматированию
- [Macros](https://doc.rust-lang.org/book/ch19-06-macros.html) — глава о макросах из The Rust Book

**Tools:**

- [rustfmt](https://github.com/rust-lang/rustfmt) — форматировщик кода
- [cargo watch](https://github.com/watchexec/cargo-watch) — автоматический запуск при изменениях

---


