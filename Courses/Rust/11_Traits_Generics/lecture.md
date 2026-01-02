# Traits и Generics
## Traits, generics, ограничения типов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать struct и enum (см. модуль [08_Struct_Enum](../08_Struct_Enum/))
- Знать функции и модули (см. модуль [06_Functions_Modules](../06_Functions_Modules/))
- Понимать ownership (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять и использовать traits для общего поведения
- Создавать generic функции и структуры
- Применять ограничения типов (trait bounds)
- Понимать разницу между traits и интерфейсами
- Использовать стандартные traits (Debug, Clone, Copy)

---

## 1. Traits

### 1.1 Что такое trait

**Trait** — определяет общее поведение, которое могут реализовывать разные типы.

**Example: Определение trait**

```rust
trait Summary {
    fn summarize(&self) -> String;
}

struct NewsArticle {
    headline: String,
    location: String,
    author: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

fn main() {
    let article = NewsArticle {
        headline: String::from("Важные новости"),
        location: String::from("Москва"),
        author: String::from("Иван Иванов"),
        content: String::from("Текст статьи..."),
    };
    
    println!("{}", article.summarize());
}
```

**Output:**
```
Важные новости, by Иван Иванов (Москва)
```

### 1.2 Реализация для нескольких типов

**Example: Множественная реализация**

```rust
trait Summary {
    fn summarize(&self) -> String;
}

struct NewsArticle {
    headline: String,
}

struct Tweet {
    username: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("Новость: {}", self.headline)
    }
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

fn main() {
    let article = NewsArticle {
        headline: String::from("Новость"),
    };
    let tweet = Tweet {
        username: String::from("user"),
        content: String::from("Твит"),
    };
    
    println!("{}", article.summarize());
    println!("{}", tweet.summarize());
}
```

**Output:**
```
Новость: Новость
user: Твит
```

### 1.3 Реализация по умолчанию

**Example: Методы по умолчанию**

```rust
trait Summary {
    fn summarize(&self) -> String {
        String::from("(Читать далее...)")
    }
}

struct NewsArticle {
    headline: String,
}

impl Summary for NewsArticle {
    // Использует реализацию по умолчанию
}

fn main() {
    let article = NewsArticle {
        headline: String::from("Новость"),
    };
    println!("{}", article.summarize());
}
```

**Output:**
```
(Читать далее...)
```

---

## 2. Generics

### 2.1 Generic функции

**Generics** — позволяют писать код, работающий с разными типами.

**Example: Generic функция**

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    
    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];
    let result = largest(&number_list);
    println!("Наибольшее число: {}", result);
}
```

**Output:**
```
Наибольшее число: 100
```

**`<T: PartialOrd>`** — generic параметр с ограничением (trait bound).

### 2.2 Generic структуры

**Example: Generic структура**

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
    
    println!("Целочисленная точка: ({}, {})", integer.x, integer.y);
    println!("Точка с плавающей точкой: ({}, {})", float.x, float.y);
}
```

**Output:**
```
Целочисленная точка: (5, 10)
Точка с плавающей точкой: (1, 4)
```

### 2.3 Несколько generic параметров

**Example: Несколько параметров**

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
    
    println!("({}, {})", integer_and_float.x, integer_and_float.y);
}
```

**Output:**
```
(5, 4)
```

---

## 3. Trait bounds

### 3.1 Ограничения типов

**Trait bounds** — ограничения на generic типы.

**Example: Trait bounds**

```rust
use std::fmt::Display;

fn print_summary<T: Summary>(item: &T) {
    println!("{}", item.summarize());
}

trait Summary {
    fn summarize(&self) -> String;
}

struct NewsArticle {
    headline: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        self.headline.clone()
    }
}

fn main() {
    let article = NewsArticle {
        headline: String::from("Новость"),
    };
    print_summary(&article);
}
```

**Output:**
```
Новость
```

### 3.2 Множественные bounds

**Example: Несколько bounds**

```rust
use std::fmt::Display;

fn some_function<T: Display + Clone, U: Clone + Copy>(t: &T, u: &U) {
    // ...
}
```

**Альтернативный синтаксис с where:**

```rust
fn some_function<T, U>(t: &T, u: &U)
where
    T: Display + Clone,
    U: Clone + Copy,
{
    // ...
}
```

---

## 4. Стандартные traits

### 4.1 Debug

**Debug** — trait для отладочного вывода.

**Example: Debug trait**

```rust
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 3, y: 4 };
    println!("{:?}", p);
    println!("{:#?}", p);  // Красивый вывод
}
```

**Output:**
```
Point { x: 3, y: 4 }
Point {
    x: 3,
    y: 4,
}
```

### 4.2 Clone и Copy

**Clone** — trait для создания копии значения.

**Example: Clone**

```rust
#[derive(Clone, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 3, y: 4 };
    let p2 = p1.clone();
    
    println!("p1: {:?}, p2: {:?}", p1, p2);
}
```

**Output:**
```
p1: Point { x: 3, y: 4 }, p2: Point { x: 3, y: 4 }
```

**Copy** — автоматическое копирование (только для типов, которые можно скопировать побитово).

**Example: Copy**

```rust
#[derive(Copy, Clone, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 3, y: 4 };
    let p2 = p1;  // Копирование автоматически
    
    println!("p1: {:?}, p2: {:?}", p1, p2);
}
```

**Output:**
```
p1: Point { x: 3, y: 4 }, p2: Point { x: 3, y: 4 }
```

### 4.3 PartialEq и Eq

**PartialEq** — сравнение на равенство.

**Example: PartialEq**

```rust
#[derive(PartialEq, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 3, y: 4 };
    let p2 = Point { x: 3, y: 4 };
    let p3 = Point { x: 5, y: 6 };
    
    println!("p1 == p2: {}", p1 == p2);
    println!("p1 == p3: {}", p1 == p3);
}
```

**Output:**
```
p1 == p2: true
p1 == p3: false
```

### 4.4 PartialOrd и Ord

**PartialOrd** — частичное упорядочивание.

**Example: PartialOrd**

```rust
#[derive(PartialOrd, PartialEq, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 3, y: 4 };
    let p2 = Point { x: 5, y: 6 };
    
    // Сравнение по x
    println!("p1 < p2: {}", p1 < p2);
}
```

**Output:**
```
p1 < p2: true
```

---

## 5. Практические примеры

### 5.1 Пример: Generic функция с trait bounds

```rust
use std::fmt::Display;

fn print_and_return<T: Display>(item: T) -> T {
    println!("Значение: {}", item);
    item
}

fn main() {
    let number = print_and_return(42);
    let text = print_and_return(String::from("hello"));
    
    println!("number: {}, text: {}", number, text);
}
```

**Output:**
```
Значение: 42
Значение: hello
number: 42, text: hello
```

### 5.2 Пример: Generic структура с методами

```rust
struct Container<T> {
    value: T,
}

impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
    
    fn get(&self) -> &T {
        &self.value
    }
}

impl<T: Display> Container<T> {
    fn display(&self) {
        println!("{}", self.value);
    }
}

use std::fmt::Display;

fn main() {
    let container = Container::new(42);
    println!("Значение: {}", container.get());
    container.display();
}
```

**Output:**
```
Значение: 42
42
```

### 5.3 Пример: Trait с ассоциированными типами

```rust
trait Iterator {
    type Item;
    
    fn next(&mut self) -> Option<Self::Item>;
}

struct Counter {
    count: u32,
}

impl Iterator for Counter {
    type Item = u32;
    
    fn next(&mut self) -> Option<Self::Item> {
        if self.count < 5 {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

fn main() {
    let mut counter = Counter { count: 0 };
    while let Some(value) = counter.next() {
        println!("{}", value);
    }
}
```

**Output:**
```
1
2
3
4
5
```

---

## 💡 Key Takeaways

- **Traits определяют поведение:** Похожи на интерфейсы в других языках

- **Generics для переиспользования:** Код работает с разными типами

- **Trait bounds ограничивают типы:** Гарантируют наличие нужного поведения

- **Стандартные traits полезны:** Debug, Clone, Copy и другие

- **derive макросы упрощают:** Автоматическая реализация traits

---

## 🚀 Next Steps

**Related Modules:**

- [Управление памятью](../12_Memory_Management/) — как Rust управляет памятью
- [Асинхронность](../13_Async/) — async/await и futures

**Practice Ideas:**

1. Создайте свой trait и реализуйте его для разных типов
2. Напишите generic функции для работы с разными типами
3. Используйте trait bounds для ограничения типов
4. Попробуйте derive макросы для стандартных traits

**Going Deeper:**

- Изучите продвинутые traits (Iterator, From, Into)
- Почитайте о trait objects и динамической диспетчеризации
- Изучите associated types в traits

---

## 📚 Additional Resources

**Documentation:**

- [Traits](https://doc.rust-lang.org/book/ch10-02-traits.html) — документация по traits
- [Generics](https://doc.rust-lang.org/book/ch10-01-syntax.html) — документация по generics

**Practice:**

- [Rustlings: Traits](https://github.com/rust-lang/rustlings) — упражнения

---


