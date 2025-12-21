# Работа с памятью и указателями
## Raw pointers, Box, Rc, Arc, unsafe код

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Знать управление памятью (см. модуль [12_Memory_Management](../12_Memory_Management/))
- Понимать системное программирование (см. модуль [17_System_Programming](../17_System_Programming/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать raw pointers для низкоуровневого доступа
- Применять Box для heap-выделения
- Использовать Rc и Arc для множественного владения
- Понимать границы безопасности unsafe кода
- Выбирать подходящий тип указателя для задачи

---

## 1. Raw Pointers

### 1.1 Что такое raw pointers

**Raw pointers** — небезопасные указатели, аналогичные указателям в C.

**Типы:**

- `*const T` — неизменяемый указатель
- `*mut T` — изменяемый указатель

**Example: Raw pointers**

```rust

fn main() {
    let mut num = 5;
    
    let r1 = &num as *const i32;
    let r2 = &mut num as *mut i32;
    
    unsafe {
        println!("r1: {}", *r1);
        println!("r2: {}", *r2);
    }
}
```

**Output:**
```

r1: 5
r2: 5
```

**⚠️ Важно:** Разыменование raw pointers требует `unsafe` блока!

### 1.2 Когда использовать raw pointers

**Используйте raw pointers для:**

- FFI с C кодом
- Низкоуровневых оптимизаций
- Реализации unsafe абстракций

---

## 2. Box<T>

### 2.1 Что такое Box

**Box<T>** — умный указатель для heap-выделения.

**Example: Box**

```rust

fn main() {
    let b = Box::new(5);
    println!("b = {}", b);
}  // b автоматически освобождается
```

**Output:**
```

b = 5
```

### 2.2 Использование Box

**Box полезен для:**

- Рекурсивных структур данных
- Больших данных на heap
- Трейт-объектов

**Example: Рекурсивная структура**

```rust

enum List {
    Cons(i32, Box<List>),
    Nil,
}

fn main() {
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
}
```

---

## 3. Rc<T> (Reference Counting)

### 3.1 Что такое Rc

**Rc<T>** — счётчик ссылок для множественного владения (только для одного потока).

**Example: Rc**

```rust

use std::rc::Rc;

fn main() {
    let a = Rc::new(5);
    let b = Rc::clone(&a);
    let c = Rc::clone(&a);
    
    println!("Счётчик ссылок: {}", Rc::strong_count(&a));
}
```

**Output:**
```

Счётчик ссылок: 3
```

### 3.2 Ограничения Rc

**Rc не thread-safe!** Для многопоточности используйте `Arc`.

---

## 4. Arc<T> (Atomically Reference Counting)

### 4.1 Что такое Arc

**Arc<T>** — атомарный счётчик ссылок для многопоточности.

**Example: Arc**

```rust

use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(5);
    let data1 = Arc::clone(&data);
    let data2 = Arc::clone(&data);
    
    let handle1 = thread::spawn(move || {
        println!("Поток 1: {}", data1);
    });
    
    let handle2 = thread::spawn(move || {
        println!("Поток 2: {}", data2);
    });
    
    handle1.join().unwrap();
    handle2.join().unwrap();
}
```

**Output:**
```

Поток 1: 5
Поток 2: 5
```

---

## 5. Сравнение типов указателей

| Тип | Владение | Thread-safe | Overhead | Использование |
|-----|----------|-------------|----------|---------------|
| `&T` | Заимствование | Да | Нет | Обычные ссылки |
| `Box<T>` | Единственное | Да | Heap allocation | Heap-выделение |
| `Rc<T>` | Множественное | Нет | Счётчик ссылок | Один поток |
| `Arc<T>` | Множественное | Да | Атомарный счётчик | Многопоточность |
| `*const T` | Нет | Нет | Нет | Unsafe, FFI |

### 5.1 Выбор типа указателя

**Когда использовать каждый тип:**

**`&T` (ссылка):**

- Обычное заимствование
- Параметры функций
- Временный доступ

**`Box<T>`:**

- Рекурсивные структуры
- Большие данные на heap
- Трейт-объекты

**`Rc<T>`:**

- Множественное владение в одном потоке
- Графы данных
- Циклические структуры (с Weak)

**`Arc<T>`:**

- Множественное владение в нескольких потоках
- Разделяемые данные
- Параллельная обработка

**`*const T` / `*mut T`:**
- FFI с C
- Низкоуровневые оптимизации
- Unsafe код

---

## 6. Практические примеры

### 6.1 Пример: Box для рекурсивной структуры

```rust

enum List {
    Cons(i32, Box<List>),
    Nil,
}

fn main() {
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
}
```

### 6.2 Пример: Rc для множественного владения

```rust

use std::rc::Rc;

struct Node {
    value: i32,
    next: Option<Rc<Node>>,
}

fn main() {
    let node1 = Rc::new(Node {
        value: 1,
        next: None,
    });
    
    let node2 = Rc::new(Node {
        value: 2,
        next: Some(Rc::clone(&node1)),
    });
    
    println!("Счётчик node1: {}", Rc::strong_count(&node1));
}
```

**Output:**
```

Счётчик node1: 2
```

### 6.3 Пример: Arc для многопоточности

```rust

use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(5);
    let data1 = Arc::clone(&data);
    let data2 = Arc::clone(&data);
    
    let handle1 = thread::spawn(move || {
        println!("Поток 1: {}", data1);
    });
    
    let handle2 = thread::spawn(move || {
        println!("Поток 2: {}", data2);
    });
    
    handle1.join().unwrap();
    handle2.join().unwrap();
    
    println!("Основной поток: {}", data);
}
```

**Output:**
```

Поток 1: 5
Поток 2: 5
Основной поток: 5
```

### 6.4 Пример: Weak для циклических ссылок

**Weak** позволяет избежать циклических ссылок:

```rust

use std::rc::{Rc, Weak};

struct Node {
    value: i32,
    parent: Option<Weak<Node>>,
    children: Vec<Rc<Node>>,
}

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: None,
        children: vec![],
    });
    
    let branch = Rc::new(Node {
        value: 5,
        parent: None,
        children: vec![Rc::clone(&leaf)],
    });
    
    // Устанавливаем слабую ссылку на родителя
    // leaf.parent = Some(Rc::downgrade(&branch));
    
    println!("Счётчик leaf: {}", Rc::strong_count(&leaf));
    println!("Счётчик branch: {}", Rc::strong_count(&branch));
}
```

**Weak** не увеличивает strong_count, что позволяет избежать циклов.

---

## 7. Производительность указателей

### 7.1 Сравнение производительности

**Измерения:**

| Тип | Время доступа | Память | Overhead |
|-----|---------------|--------|----------|
| `&T` | Самый быстрый | Нет | Нет |
| `Box<T>` | Быстрый | Heap | Минимальный |
| `Rc<T>` | Средний | Heap + счётчик | Счётчик ссылок |
| `Arc<T>` | Средний | Heap + атомарный счётчик | Атомарный счётчик |
| `*const T` | Быстрый | Нет | Нет (unsafe) |

### 7.2 Когда использовать каждый тип

**Рекомендации:**

**`&T`** — всегда предпочтительнее, когда возможно.

**`Box<T>`** — когда нужен heap, но нет множественного владения.

**`Rc<T>`** — когда нужно множественное владение в одном потоке.

**`Arc<T>`** — когда нужно множественное владение в нескольких потоках.

**`*const T`** — только для FFI или низкоуровневых оптимизаций.

---

## 8. Практические примеры

### 8.1 Пример: Дерево с Rc

```rust

use std::rc::Rc;

struct TreeNode {
    value: i32,
    left: Option<Rc<TreeNode>>,
    right: Option<Rc<TreeNode>>,
}

fn main() {
    let leaf = Rc::new(TreeNode {
        value: 3,
        left: None,
        right: None,
    });
    
    let root = Rc::new(TreeNode {
        value: 5,
        left: Some(Rc::clone(&leaf)),
        right: Some(Rc::clone(&leaf)),
    });
    
    println!("Счётчик leaf: {}", Rc::strong_count(&leaf));
}
```

**Output:**
```

Счётчик leaf: 3
```

### 8.2 Пример: Разделяемые данные с Arc

```rust

use std::sync::Arc;
use std::thread;

struct SharedData {
    counter: i32,
}

fn main() {
    let data = Arc::new(SharedData { counter: 0 });
    let mut handles = vec![];
    
    for i in 0..5 {
        let data = Arc::clone(&data);
        let handle = thread::spawn(move || {
            println!("Поток {}: counter = {}", i, data.counter);
        });
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

### 8.3 Пример: Raw pointers для оптимизации

```rust

fn unsafe_fast_sum(slice: &[i32]) -> i32 {
    let mut sum = 0;
    let ptr = slice.as_ptr();
    let len = slice.len();
    
    unsafe {
        for i in 0..len {
            sum += *ptr.add(i);
        }
    }
    
    sum
}

fn main() {
    let data = vec![1, 2, 3, 4, 5];
    println!("Сумма: {}", unsafe_fast_sum(&data));
}
```

**Output:**
```

Сумма: 15
```

**⚠️ Важно:** Обычно безопасный код достаточно быстр, unsafe нужен только в особых случаях.

---

## 💡 Key Takeaways

- **Raw pointers для низкоуровневого доступа:** Требуют unsafe, как в C

- **Box для heap-выделения:** Единственное владение, автоматическое освобождение

- **Rc для множественного владения:** Только для одного потока

- **Arc для многопоточности:** Thread-safe множественное владение

- **Выбор зависит от задачи:** Каждый тип имеет своё применение

---

## 🚀 Next Steps

**Related Modules:**

- [Unsafe Rust](../19_Unsafe_Rust/) — детальная работа с unsafe
- [FFI](../20_FFI/) — взаимодействие с C/C++

**Practice Ideas:**

1. Попробуйте создать рекурсивную структуру с Box
2. Используйте Rc для множественного владения
3. Примените Arc в многопоточном коде
4. Изучите разницу в производительности

**Going Deeper:**

- Изучите Weak<T> для циклических ссылок
- Почитайте о внутренней реализации умных указателей
- Изучите Cell и RefCell для внутренней изменяемости

---

## 📚 Additional Resources

**Documentation:**

- [Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html) — документация
- [Rc](https://doc.rust-lang.org/std/rc/struct.Rc.html) — документация по Rc
- [Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html) — документация по Arc

---


