# Unsafe Rust
## Что такое unsafe, когда оправдан, best practices

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать raw pointers (см. модуль [18_Memory_Pointers](../18_Memory_Pointers/))
- Знать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Понимать системное программирование (см. модуль [17_System_Programming](../17_System_Programming/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать, что такое unsafe Rust
- Знать, когда unsafe оправдан
- Использовать unsafe для низкоуровневых операций
- Следовать best practices работы с unsafe
- Изолировать unsafe код в безопасные абстракции

---

## 1. Что такое unsafe

### 1.1 Пять unsafe операций

**unsafe** позволяет выполнять пять операций, которые компилятор не может проверить:

1. Разыменование raw pointers
2. Вызов unsafe функций
3. Реализация unsafe traits
4. Изменение статических переменных
5. Реализация unsafe функций

**Example: unsafe блок**

```rust

unsafe fn dangerous() {}

fn main() {
    unsafe {
        dangerous();
    }
}
```

### 1.2 Почему unsafe существует

**unsafe необходим для:**

- FFI с другими языками
- Низкоуровневых системных операций
- Оптимизаций производительности
- Реализации безопасных абстракций

---

## 2. Когда unsafe оправдан

### 2.1 FFI

**Example: Вызов C функции**

```rust

extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!("Абсолютное значение -3: {}", abs(-3));
    }
}
```

**Output:**
```

Абсолютное значение -3: 3
```

### 2.2 Низкоуровневые операции

**Example: Прямой доступ к памяти**

```rust

fn main() {
    let address = 0x01234usize;
    let r = address as *const i32;
    
    unsafe {
        // Опасно! Может быть невалидный указатель
        // println!("Значение: {}", *r);
    }
}
```

### 2.3 Оптимизации

**unsafe может использоваться для:**

- Обхода проверок компилятора
- Низкоуровневых оптимизаций
- Реализации высокопроизводительных абстракций

---

## 3. Best Practices

### 3.1 Изоляция unsafe

**Изолируйте unsafe код в безопасные абстракции:**

```rust

fn split_at_mut(slice: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = slice.len();
    let ptr = slice.as_mut_ptr();
    
    assert!(mid <= len);
    
    unsafe {
        (
            std::slice::from_raw_parts_mut(ptr, mid),
            std::slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}

fn main() {
    let mut v = vec![1, 2, 3, 4, 5, 6];
    let (left, right) = split_at_mut(&mut v, 3);
    println!("left: {:?}, right: {:?}", left, right);
}
```

**Output:**
```

left: [1, 2, 3], right: [4, 5, 6]
```

**Принцип:** Минимизируйте количество unsafe кода, изолируя его в безопасные функции.

### 3.2 Документация инвариантов

**Всегда документируйте инварианты unsafe кода:**

```rust

/// Безопасно создаёт slice из указателя.
///
/// # Safety
///
/// Указатель должен быть валидным и указывать на валидные данные.
/// Длина должна соответствовать размеру данных.
unsafe fn create_slice(ptr: *const i32, len: usize) -> &[i32] {
    std::slice::from_raw_parts(ptr, len)
}
```

### 3.3 Проверка инвариантов

**Проверяйте инварианты перед unsafe операциями:**

```rust

fn safe_index(slice: &[i32], index: usize) -> Option<&i32> {
    if index < slice.len() {
        unsafe {
            Some(slice.get_unchecked(index))
        }
    } else {
        None
    }
}

fn main() {
    let v = vec![1, 2, 3];
    println!("{:?}", safe_index(&v, 1));
    println!("{:?}", safe_index(&v, 10));
}
```

**Output:**
```

Some(2)
None
```

### 3.4 Минимизация unsafe

**Правила:**

- Используйте unsafe только когда необходимо
- Изолируйте в безопасные абстракции
- Документируйте все инварианты
- Тестируйте тщательно

---

## 4. Типичные use cases

### 4.1 FFI

**Example: Вызов C функции**

```rust

extern "C" {
    fn sqrt(x: f64) -> f64;
}

fn safe_sqrt(x: f64) -> f64 {
    unsafe { sqrt(x) }
}

fn main() {
    println!("Квадратный корень из 16: {}", safe_sqrt(16.0));
}
```

**Output:**
```

Квадратный корень из 16: 4
```

### 4.2 Оптимизации

**Example: Обход проверок для производительности**

```rust

fn fast_sum(slice: &[i32]) -> i32 {
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
    println!("Сумма: {}", fast_sum(&data));
}
```

**Output:**
```

Сумма: 15
```

### 4.3 Реализация безопасных абстракций

**Example: Безопасная обёртка**

```rust

pub struct SafeVec<T> {
    ptr: *mut T,
    len: usize,
    capacity: usize,
}

impl<T> SafeVec<T> {
    pub fn new() -> Self {
        SafeVec {
            ptr: std::ptr::null_mut(),
            len: 0,
            capacity: 0,
        }
    }
    
    pub fn push(&mut self, item: T) {
        // Реализация с unsafe для выделения памяти
        // Но публичный API безопасен
    }
}

impl<T> Drop for SafeVec<T> {
    fn drop(&mut self) {
        unsafe {
            // Освобождение памяти
        }
    }
}
```

### 4.4 Пример: Безопасный интерфейс для unsafe кода

```rust

pub struct SafePointer<T> {
    ptr: *mut T,
}

impl<T> SafePointer<T> {
    pub fn new(value: T) -> Self {
        let boxed = Box::new(value);
        SafePointer {
            ptr: Box::into_raw(boxed),
        }
    }
    
    pub fn get(&self) -> &T {
        unsafe {
            &*self.ptr
        }
    }
    
    pub fn get_mut(&mut self) -> &mut T {
        unsafe {
            &mut *self.ptr
        }
    }
}

impl<T> Drop for SafePointer<T> {
    fn drop(&mut self) {
        unsafe {
            let _ = Box::from_raw(self.ptr);
        }
    }
}

fn main() {
    let mut ptr = SafePointer::new(42);
    println!("Значение: {}", ptr.get());
    *ptr.get_mut() = 100;
    println!("Новое значение: {}", ptr.get());
}
```

**Output:**
```

Значение: 42
Новое значение: 100
```

---

## 5. Проверка unsafe кода

### 5.1 Тестирование

**Важно тестировать unsafe код тщательно:**

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_safe_wrapper() {
        let data = vec![1, 2, 3];
        let result = safe_wrapper(&data);
        assert_eq!(result, 6);
    }
    
    #[test]
    fn test_null_pointer() {
        let ptr: *const i32 = std::ptr::null();
        assert!(ptr.is_null());
    }
}
```

### 5.2 Статический анализ

**Инструменты:**

- **Miri** — интерпретатор для проверки unsafe кода

- **Clippy** — линтер с проверками unsafe

- **Sanitizers** — обнаружение проблем во время выполнения

### 5.3 Документация

**Всегда документируйте инварианты:**

```rust

/// Безопасно создаёт slice из указателя.
///
/// # Safety
///
/// - `ptr` должен быть валидным указателем
/// - `ptr` должен указывать на валидные данные длиной `len`
/// - Данные должны быть инициализированы
/// - Память не должна быть освобождена пока используется slice
unsafe fn create_slice(ptr: *const i32, len: usize) -> &[i32] {
    std::slice::from_raw_parts(ptr, len)
}
```

---

## 6. Типичные ошибки

### 6.1 Разыменование невалидного указателя

**Ошибка:**
```rust

// unsafe {
//     let ptr: *const i32 = std::ptr::null();
//     println!("{}", *ptr);  // Неопределённое поведение!
// }
```

**Правильно:**
```rust

unsafe {
    let ptr: *const i32 = std::ptr::null();
    if !ptr.is_null() {
        println!("{}", *ptr);
    }
}
```

### 6.2 Использование после освобождения

**Ошибка:**
```rust

// let ptr = Box::into_raw(Box::new(5));
// let _ = Box::from_raw(ptr);
// unsafe {
//     println!("{}", *ptr);  // Использование после освобождения!
// }
```

**Правильно:**
```rust

let ptr = Box::into_raw(Box::new(5));
unsafe {
    println!("{}", *ptr);
    let _ = Box::from_raw(ptr);
}
```

### 6.3 Нарушение инвариантов

**Важно:** Всегда соблюдайте инварианты, документированные в unsafe функциях.

---

## 💡 Key Takeaways

- **unsafe позволяет пять операций:** Которые компилятор не может проверить

- **unsafe не отключает проверки:** Только позволяет дополнительные операции

- **Изолируйте unsafe код:** Создавайте безопасные абстракции

- **Документируйте инварианты:** Важно для поддержки кода

- **Используйте минимально:** Только когда действительно необходимо

---

## 🚀 Next Steps

**Related Modules:**

- [FFI](../20_FFI/) — взаимодействие с C/C++
- [Rust и ОС](../21_OS/) — системные операции

**Practice Ideas:**

1. Создайте безопасную абстракцию над unsafe кодом
2. Попробуйте реализовать низкоуровневую операцию
3. Изучите unsafe код в стандартной библиотеке
4. Документируйте инварианты вашего unsafe кода

**Going Deeper:**

- Изучите unsafe код в стандартной библиотеке Rust
- Почитайте о проверке unsafe кода
- Изучите инструменты для анализа unsafe кода

---

## 📚 Additional Resources

**Documentation:**

- [Unsafe Rust](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html) — документация
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) — книга о unsafe Rust

---


