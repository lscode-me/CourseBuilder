# Ownership и Borrowing
## Владение, заимствование, ссылки, lifetimes

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать функции и модули в Rust (см. модуль [06_Functions_Modules](../06_Functions_Modules/))
- Знать переменные и типы (см. модуль [04_Variables_Types](../04_Variables_Types/))
- Понимать базовые концепции программирования: указатели, ссылки

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать концепцию ownership (владения) в Rust
- Использовать borrowing (заимствование) через ссылки
- Различать изменяемые и неизменяемые ссылки
- Понимать правила borrowing на интуитивном уровне
- Применять ownership и borrowing в практических задачах

---

## 1. Что такое Ownership

### 1.1 Концепция владения

**Ownership** — уникальная для Rust система управления памятью без сборщика мусора.

**Три основных правила:**

1. Каждое значение имеет **одного владельца**
2. Когда владелец выходит из области видимости, значение удаляется
3. Значение может иметь **только одного владельца** в каждый момент времени

**Example: Перемещение владения**

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;  // s1 перемещается в s2
    
    // println!("{}", s1);  // Ошибка: s1 больше не владеет значением
    println!("{}", s2);
}
```

**Output:**
```
hello
```

**Ошибка при использовании s1:**
```
error[E0382]: borrow of moved value: `s1`
```

### 1.2 Почему это важно

**Без ownership (как в C/C++):**
```c
// C код - возможна утечка памяти или double-free
char* s1 = malloc(10);
char* s2 = s1;
free(s1);
// s2 теперь указывает на освобождённую память!
```

**С ownership (Rust):**
```rust
// Rust предотвращает это на этапе компиляции
let s1 = String::from("hello");
let s2 = s1;  // s1 перемещается, больше не валидна
// Невозможно использовать s1 после перемещения
```

---

## 2. Перемещение (Move)

### 2.1 Что происходит при присваивании

**Example: Перемещение для String**

```rust
fn main() {
    let s1 = String::from("hello");
    println!("s1 = {}", s1);
    
    let s2 = s1;  // s1 перемещается в s2
    
    println!("s2 = {}", s2);
    // println!("s1 = {}", s1);  // Ошибка!
}
```

**Output:**
```
s1 = hello
s2 = hello
```

### 2.2 Copy vs Move

**Типы, которые копируются (Copy trait):**

- Целые числа (i32, u32, etc.)
- Числа с плавающей точкой (f32, f64)
- bool
- char
- Кортежи из Copy типов

**Example: Copy типы**

```rust
fn main() {
    let x = 5;
    let y = x;  // x копируется, не перемещается
    
    println!("x = {}, y = {}", x, y);  // Оба работают!
}
```

**Output:**
```
x = 5, y = 5
```

**Типы, которые перемещаются:**

- String
- Vec
- Другие типы, владеющие данными в heap

**Example: Move типы**

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;  // s1 перемещается
    
    // println!("{}", s1);  // Ошибка!
    println!("{}", s2);
}
```

**Output:**
```
hello
```

---

## 3. Функции и ownership

### 3.1 Передача владения в функцию

**Example: Владение передаётся в функцию**

```rust
fn take_ownership(s: String) {
    println!("{}", s);
}  // s выходит из области видимости и удаляется

fn main() {
    let s = String::from("hello");
    take_ownership(s);  // s перемещается в функцию
    
    // println!("{}", s);  // Ошибка: s больше не валидна
}
```

**Output:**
```
hello
```

### 3.2 Возврат владения

**Example: Возврат владения**

```rust
fn give_ownership() -> String {
    let s = String::from("hello");
    s  // Владение возвращается
}

fn take_and_give_back(s: String) -> String {
    s  // Владение возвращается обратно
}

fn main() {
    let s1 = give_ownership();
    let s2 = String::from("world");
    let s3 = take_and_give_back(s2);
    
    println!("s1 = {}, s3 = {}", s1, s3);
}
```

**Output:**
```
s1 = hello, s3 = world
```

---

## 4. Borrowing (Заимствование)

### 4.1 Что такое borrowing

**Borrowing** — создание ссылки на значение без передачи владения.

**Example: Неизменяемая ссылка**

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}  // s не выходит из области видимости, так как не владеет

fn main() {
    let s = String::from("hello");
    let len = calculate_length(&s);
    
    println!("Длина '{}' равна {}", s, len);  // s всё ещё валидна!
}
```

**Output:**
```
Длина 'hello' равна 5
```

**`&`** создаёт ссылку (reference), которая **заимствует** значение, но не владеет им.

### 4.2 Изменяемые ссылки

**Example: Изменяемая ссылка**

```rust
fn change(s: &mut String) {
    s.push_str(", world");
}

fn main() {
    let mut s = String::from("hello");
    change(&mut s);
    
    println!("{}", s);
}
```

**Output:**
```
hello, world
```

**Правила изменяемых ссылок:**

1. Может быть **только одна** изменяемая ссылка на значение
2. Нельзя иметь изменяемую и неизменяемую ссылки одновременно
3. Нельзя иметь несколько изменяемых ссылок одновременно

**Example: Ошибка — несколько изменяемых ссылок**

```rust
fn main() {
    let mut s = String::from("hello");
    let r1 = &mut s;
    let r2 = &mut s;  // Ошибка!
    
    println!("{}, {}", r1, r2);
}
```

**Ошибка компиляции:**
```
error[E0499]: cannot borrow `s` as mutable more than once at a time
```

### 4.3 Неизменяемые ссылки

**Example: Несколько неизменяемых ссылок**

```rust
fn main() {
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;  // OK: можно иметь несколько неизменяемых ссылок
    
    println!("{}, {}", r1, r2);
}
```

**Output:**
```
hello, hello
```

**Правило:** Можно иметь **неограниченное количество** неизменяемых ссылок одновременно.

---

## 5. Правила borrowing

### 5.1 Три основных правила

1. **В любой момент времени** может быть либо:
   - Одна изменяемая ссылка, либо
   - Любое количество неизменяемых ссылок

2. Ссылки должны быть **валидными** (нельзя ссылаться на удалённые данные)

3. Нельзя иметь изменяемую и неизменяемую ссылки одновременно

**Example: Конфликт ссылок**

```rust
fn main() {
    let mut s = String::from("hello");
    let r1 = &s;      // Неизменяемая ссылка
    let r2 = &s;      // Ещё одна неизменяемая ссылка - OK
    let r3 = &mut s;  // Ошибка: нельзя иметь изменяемую ссылку
    
    println!("{}, {}, {}", r1, r2, r3);
}
```

**Ошибка компиляции:**
```
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
```

### 5.2 Область видимости ссылок

**Example: Область видимости**

```rust
fn main() {
    let mut s = String::from("hello");
    
    {
        let r1 = &s;  // Неизменяемая ссылка
        println!("{}", r1);
    }  // r1 выходит из области видимости
    
    let r2 = &mut s;  // Теперь можно создать изменяемую ссылку
    println!("{}", r2);
}
```

**Output:**
```
hello
hello
```

---

## 6. Dangling References

### 6.1 Что такое dangling reference

**Dangling reference** — ссылка на данные, которые были удалены.

**Rust предотвращает это на этапе компиляции!**

**Example: Попытка создать dangling reference**

```rust
fn dangle() -> &String {
    let s = String::from("hello");
    &s  // Ошибка: s удаляется в конце функции
}

fn main() {
    let reference = dangle();
}
```

**Ошибка компиляции:**
```
error[E0106]: missing lifetime specifier
```

### 6.2 Правильное решение

**Example: Возврат владения вместо ссылки**

```rust
fn no_dangle() -> String {
    let s = String::from("hello");
    s  // Возвращаем владение
}

fn main() {
    let s = no_dangle();
    println!("{}", s);
}
```

**Output:**
```
hello
```

---

## 7. Срезы (Slices)

### 7.1 Строковые срезы

**Срез** — ссылка на часть строки.

**Example: Строковый срез**

```rust
fn main() {
    let s = String::from("hello world");
    
    let hello = &s[0..5];
    let world = &s[6..11];
    
    println!("{} {}", hello, world);
}
```

**Output:**
```
hello world
```

**Синтаксис:**

- `&s[0..5]` — от индекса 0 до 5 (не включая 5)
- `&s[..5]` — от начала до 5
- `&s[6..]` — от 6 до конца
- `&s[..]` — вся строка

### 7.2 Срезы массивов

**Example: Срезы массивов**

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
    let slice = &arr[1..4];
    
    for &item in slice.iter() {
        println!("{}", item);
    }
}
```

**Output:**
```
2
3
4
```

---

## 8. Практические примеры

### 8.1 Пример: Функция, не принимающая владение

```rust
fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();
    
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }
    
    s.len()
}

fn main() {
    let s = String::from("hello world");
    let index = first_word(&s);
    
    println!("Первый пробел на позиции {}", index);
    println!("Строка всё ещё валидна: {}", s);
}
```

**Output:**
```
Первый пробел на позиции 5
Строка всё ещё валидна: hello world
```

### 8.2 Пример: Изменение через ссылку

```rust
fn add_one(n: &mut i32) {
    *n += 1;  // * разыменовывает ссылку
}

fn main() {
    let mut x = 5;
    add_one(&mut x);
    println!("x = {}", x);
}
```

**Output:**
```
x = 6
```

**`*`** — оператор разыменования для доступа к значению по ссылке.

---

## 9. Lifetimes (введение)

### 9.1 Что такое lifetime

**Lifetime** — область видимости, в течение которой ссылка валидна.

**Rust автоматически определяет lifetimes в большинстве случаев.**

**Example: Автоматическое определение lifetime**

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let s1 = String::from("long string");
    let s2 = "xyz";
    
    let result = longest(s1.as_str(), s2);
    println!("Самая длинная строка: {}", result);
}
```

**Output:**
```
Самая длинная строка: long string
```

**`'a`** — параметр lifetime, указывающий, что возвращаемая ссылка живёт столько же, сколько и входные параметры.

> **💡 Pro Tip:**  
> На данном этапе достаточно понимать, что lifetimes существуют. Детальное изучение — в продвинутых темах.

---

## 💡 Key Takeaways

- **Ownership управляет памятью:** Каждое значение имеет одного владельца

- **Move vs Copy:** Некоторые типы копируются, другие перемещаются

- **Borrowing через ссылки:** Можно заимствовать без передачи владения

- **Правила borrowing:** Одна изменяемая или много неизменяемых ссылок

- **Rust предотвращает ошибки:** Dangling references и data races на этапе компиляции

---

## 🚀 Next Steps

**Related Modules:**

- [Struct и Enum](../08_Struct_Enum/) — пользовательские типы данных
- [Обработка ошибок](../09_Error_Handling/) — Result и Option

**Practice Ideas:**

1. Напишите функции, принимающие и возвращающие String
2. Попробуйте создать функции с изменяемыми ссылками
3. Реализуйте функции, работающие со срезами
4. Поэкспериментируйте с правилами borrowing

**Going Deeper:**

- Изучите детально lifetimes (продвинутая тема)
- Почитайте о Copy и Clone traits
- Изучите Rc и Arc для множественного владения

---

## 📚 Additional Resources

**Documentation:**

- [Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) — глава из The Rust Book
- [References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html) — ссылки и заимствование

**Practice:**

- [Rustlings: Ownership](https://github.com/rust-lang/rustlings) — упражнения

---


