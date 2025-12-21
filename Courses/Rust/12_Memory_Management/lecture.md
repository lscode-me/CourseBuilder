# Управление памятью
## Stack и Heap, RAII, Drop, отсутствие GC

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Знать базовые типы данных (см. модуль [04_Variables_Types](../04_Variables_Types/))
- Понимать struct (см. модуль [08_Struct_Enum](../08_Struct_Enum/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать разницу между Stack и Heap
- Объяснять концепцию RAII (Resource Acquisition Is Initialization)
- Понимать, как работает Drop trait
- Объяснять, почему Rust не нужен сборщик мусора
- Понимать, когда данные размещаются на Stack vs Heap

---

## 1. Stack vs Heap

### 1.1 Stack

**Stack** — область памяти для данных с известным размером.

**Характеристики:**

- Быстрый доступ (LIFO)
- Фиксированный размер
- Автоматическое управление
- Локальные переменные

**Example: Stack данные**

```rust

fn main() {
    let x = 5;        // i32 на stack
    let y = x;        // Копирование на stack
    println!("x = {}, y = {}", x, y);
}
```

**Output:**
```

x = 5, y = 5
```

### 1.2 Heap

**Heap** — область памяти для данных с неизвестным размером.

**Характеристики:**

- Медленнее, чем stack
- Динамический размер
- Ручное управление (в Rust — автоматическое через ownership)
- String, Vec и другие владеющие типы

**Example: Heap данные**

```rust

fn main() {
    let s1 = String::from("hello");  // Данные на heap
    let s2 = s1;  // Владение перемещается, данные не копируются
    // println!("{}", s1);  // Ошибка: s1 больше не владеет
    println!("{}", s2);
}
```

**Output:**
```

hello
```

---

## 2. RAII (Resource Acquisition Is Initialization)

### 2.1 Что такое RAII

**RAII** — ресурс получается при инициализации и освобождается при выходе из области видимости.

**Example: RAII в действии**

```rust

fn main() {
    {
        let s = String::from("hello");  // Ресурс получен
        println!("{}", s);
    }  // s выходит из области видимости, память освобождена
    
    // s больше не доступна
}
```

**Output:**
```

hello
```

### 2.2 Автоматическое освобождение

**В Rust память освобождается автоматически** когда значение выходит из области видимости.

**Example: Автоматическое освобождение**

```rust

fn main() {
    let s = String::from("hello");
    // В конце функции s автоматически освобождается
}
```

**Не нужно вызывать free() или delete()!**

---

## 3. Drop trait

### 3.1 Что такое Drop

**Drop** — trait, который вызывается автоматически при выходе значения из области видимости.

**Example: Кастомный Drop**

```rust

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Освобождаем {}", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("мои данные"),
    };
    println!("CustomSmartPointer создан");
}  // drop() вызывается здесь автоматически
```

**Output:**
```

CustomSmartPointer создан
Освобождаем мои данные
```

### 3.2 Раннее освобождение

**Example: std::mem::drop**

```rust

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Освобождаем {}", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("данные"),
    };
    drop(c);  // Явное освобождение
    println!("После drop");
}
```

**Output:**
```

Освобождаем данные
После drop
```

---

## 4. Отсутствие сборщика мусора

### 4.1 Почему Rust не нужен GC

**Rust не нужен сборщик мусора, потому что:**

1. **Ownership система** — компилятор знает, когда освобождать память
2. **RAII** — ресурсы освобождаются автоматически
3. **Статическая проверка** — ошибки обнаруживаются на этапе компиляции

**Сравнение:**

| Язык | Управление памятью | Runtime |
|------|-------------------|---------|
| C/C++ | Ручное | Нет |
| Rust | Автоматическое (ownership) | Нет |
| Java/Go | GC | Да |
| Python | GC | Да |

### 4.2 Преимущества без GC

**Преимущества:**

- **Нет пауз** — GC не останавливает выполнение

- **Предсказуемость** — память освобождается сразу

- **Производительность** — нет overhead от GC

- **Контроль** — полный контроль над памятью

---

## 5. Размещение данных: Stack vs Heap

### 5.1 Когда данные на Stack

**Данные размещаются на Stack когда:**

- Размер известен на этапе компиляции
- Тип реализует Copy trait
- Это примитивные типы или простые структуры

**Example: Stack данные**

```rust

fn main() {
    let x = 5;           // i32 на stack
    let y = 3.14;        // f64 на stack
    let b = true;        // bool на stack
    let c = 'A';         // char на stack
    
    // Кортежи из Copy типов тоже на stack
    let tuple = (1, 2.0, true);
    
    println!("x: {}, y: {}, b: {}, c: {}", x, y, b, c);
    println!("tuple: {:?}", tuple);
}
```

**Output:**
```

x: 5, y: 3.14, b: true, c: A
tuple: (1, 2.0, true)
```

### 5.2 Когда данные на Heap

**Данные размещаются на Heap когда:**

- Размер неизвестен на этапе компиляции
- Размер может изменяться
- Это владеющие типы (String, Vec, Box)

**Example: Heap данные**

```rust

fn main() {
    let s = String::from("hello");  // Данные на heap
    let v = vec![1, 2, 3];          // Данные на heap
    let boxed = Box::new(5);        // Данные на heap
    
    println!("s: {}, v: {:?}, boxed: {}", s, v, boxed);
}  // Все автоматически освобождаются
```

**Output:**
```

s: hello, v: [1, 2, 3], boxed: 5
```

### 5.3 Сравнение производительности

**Stack:**

- Очень быстрый доступ
- Нет overhead на выделение/освобождение
- Ограничен размером

**Heap:**

- Медленнее доступ
- Overhead на управление
- Гибкий размер

---

## 6. Практические примеры

### 6.1 Пример: Владение и освобождение

```rust

fn takes_ownership(s: String) {
    println!("{}", s);
}  // s освобождается здесь

fn main() {
    let s = String::from("hello");
    takes_ownership(s);
    // s больше не доступна
}
```

**Output:**
```

hello
```

### 6.2 Пример: Множественное владение

```rust

fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone();  // Глубокое копирование
    
    println!("s1 = {}, s2 = {}", s1, s2);
}  // Оба освобождаются
```

**Output:**
```

s1 = hello, s2 = hello
```

### 6.3 Пример: Вложенные структуры

```rust

struct Person {
    name: String,
    age: u32,
}

fn main() {
    let person = Person {
        name: String::from("Alice"),
        age: 30,
    };
    
    println!("{}: {}", person.name, person.age);
}  // person и name освобождаются
```

**Output:**
```

Alice: 30
```

### 6.4 Пример: Векторы и память

```rust

fn main() {
    let mut v = Vec::new();
    
    for i in 1..=5 {
        v.push(i);
    }
    
    println!("{:?}", v);
}  // v и все элементы освобождаются
```

**Output:**
```

[1, 2, 3, 4, 5]
```

---

## 7. Оптимизации компилятора

### 7.1 Zero-cost abstractions

**Rust компилятор оптимизирует:**

- Inlining функций
- Удаление неиспользуемого кода
- Оптимизацию циклов
- Размещение данных на stack когда возможно

**Example: Оптимизация**

```rust

fn add_one(x: i32) -> i32 {
    x + 1
}

fn main() {
    let result = add_one(5);
    println!("{}", result);
}
```

Компилятор может заинлайнить функцию, сделав код эквивалентным `let result = 5 + 1;`.

### 7.2 Размещение на stack

**Компилятор старается размещать данные на stack когда возможно:**

```rust

fn main() {
    let small_array = [1, 2, 3, 4, 5];  // На stack
    let large_vec = vec![1; 1000];      // На heap
}
```

---

## 💡 Key Takeaways

- **Stack для фиксированных данных:** Быстро, автоматически управляется

- **Heap для динамических данных:** Медленнее, управляется через ownership

- **RAII автоматизирует управление:** Ресурсы освобождаются при выходе из области видимости

- **Drop вызывается автоматически:** Можно переопределить для кастомной логики

- **Нет GC, нет проблем:** Ownership система делает GC ненужным

---

## 🚀 Next Steps

**Related Modules:**

- [Асинхронность](../13_Async/) — threads, async/await
- [Практические применения](../15_Practical_Applications/) — реальные примеры

**Practice Ideas:**

1. Создайте структуру с кастомным Drop
2. Поэкспериментируйте с владением и освобождением памяти
3. Попробуйте различные способы передачи владения
4. Изучите, когда данные размещаются на stack vs heap

**Going Deeper:**

- Изучите Box, Rc, Arc для различных паттернов владения
- Почитайте о производительности stack vs heap
- Изучите оптимизации компилятора Rust

---

## 📚 Additional Resources

**Documentation:**

- [The Stack and the Heap](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#the-stack-and-the-heap) — документация
- [Drop](https://doc.rust-lang.org/std/ops/trait.Drop.html) — документация по Drop

**Practice:**

- [Rustlings: Ownership](https://github.com/rust-lang/rustlings) — упражнения

---


