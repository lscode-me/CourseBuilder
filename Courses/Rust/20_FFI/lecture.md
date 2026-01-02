# FFI и взаимодействие с C/C++
## Foreign Function Interface, bindgen, вызов C из Rust

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать unsafe Rust (см. модуль [19_Unsafe_Rust](../19_Unsafe_Rust/))
- Знать базовые концепции C/C++
- Понимать системное программирование (см. модуль [17_System_Programming](../17_System_Programming/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать FFI для вызова C функций из Rust
- Применять bindgen для генерации биндингов
- Вызывать C библиотеки из Rust
- Использовать Rust код из C/C++
- Понимать безопасность FFI

---

## 1. Foreign Function Interface

### 1.1 Что такое FFI

**FFI** — интерфейс для вызова функций из других языков.

**Основные случаи:**

- Вызов C библиотек из Rust
- Использование Rust из C/C++
- Интеграция с существующим кодом

### 1.2 Базовый FFI

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

**`extern "C"`** — указывает соглашение о вызовах C.

---

## 2. bindgen

### 2.1 Что такое bindgen

**bindgen** — инструмент для автоматической генерации Rust биндингов из C заголовков.

**Использование:**
```bash
cargo install bindgen
```

**Example: Генерация биндингов**

```rust
// build.rs
// use bindgen;

// fn main() {
//     bindgen::Builder::default()
//         .header("wrapper.h")
//         .generate()
//         .expect("Не удалось сгенерировать биндинги")
//         .write_to_file("src/bindings.rs")
//         .expect("Не удалось записать биндинги");
// }
```

---

## 3. Вызов C библиотек

### 3.1 Статическая линковка

**Example: Линковка C библиотеки**

```toml
# Cargo.toml

[build-dependencies]
bindgen = "0.65"

[dependencies]
libc = "0.2"
```

### 3.2 Динамическая линковка

**Example: Динамическая библиотека**

```rust
#[link(name = "mylib")]
extern "C" {
    fn my_function();
}
```

---

## 4. Использование Rust из C

### 4.1 Экспорт функций

**Example: Экспорт функции**

```rust
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

**`#[no_mangle]`** — предотвращает изменение имени функции компилятором.

### 4.2 Экспорт структур

**Example: Экспорт структуры**

```rust
#[repr(C)]
pub struct Point {
    x: i32,
    y: i32,
}

#[no_mangle]
pub extern "C" fn create_point(x: i32, y: i32) -> Point {
    Point { x, y }
}

#[no_mangle]
pub extern "C" fn get_x(p: *const Point) -> i32 {
    unsafe {
        (*p).x
    }
}
```

**`#[repr(C)]`** гарантирует C-совместимое расположение в памяти.

### 4.3 Создание C библиотеки

**Cargo.toml:**
```toml
[lib]
crate-type = ["cdylib"]
name = "my_lib"
```

**Example: Полный пример**

```rust
#[no_mangle]
pub extern "C" fn rust_function(input: i32) -> i32 {
    input * 2
}
```

**Использование из C:**
```c
// extern int rust_function(int input);
//
// int main() {
//     int result = rust_function(5);
//     printf("%d\n", result);
//     return 0;
// }
```

### 4.4 Генерация C заголовков

**Используйте cbindgen для генерации заголовков:**

```bash
cargo install cbindgen
cbindgen --lang C --output header.h
```

---

## 5. Практические примеры

### 5.1 Пример: Интеграция с существующей C библиотекой

```rust
// extern "C" {
//     fn existing_c_function(data: *const u8, len: usize) -> i32;
// }
//
// pub fn safe_wrapper(data: &[u8]) -> i32 {
//     unsafe {
//         existing_c_function(data.as_ptr(), data.len())
//     }
// }
```

### 5.2 Пример: Экспорт Rust API для C

```rust
// #[repr(C)]
// pub struct Config {
//     timeout: u32,
//     retries: u32,
// }
//
// #[no_mangle]
// pub extern "C" fn create_config(timeout: u32, retries: u32) -> *mut Config {
//     Box::into_raw(Box::new(Config { timeout, retries }))
// }
//
// #[no_mangle]
// pub extern "C" fn destroy_config(config: *mut Config) {
//     unsafe {
//         if !config.is_null() {
//             Box::from_raw(config);
//         }
//     }
// }
```

### 5.3 Пример: Работа со строками

**Важно:** C строки и Rust строки имеют разный формат!

**Example: Конвертация строк**

```rust
use std::ffi::{CString, CStr};
use std::os::raw::c_char;

// Rust → C
fn rust_to_c(rust_str: &str) -> *const c_char {
    CString::new(rust_str).unwrap().into_raw()
}

// C → Rust
unsafe fn c_to_rust(c_str: *const c_char) -> String {
    CStr::from_ptr(c_str).to_string_lossy().into_owned()
}
```

### 5.4 Пример: Callback функции

**Example: Передача callback из C в Rust**

```rust
// extern "C" {
//     type Callback = extern "C" fn(data: *const u8, len: usize);
//     fn c_function_with_callback(cb: Callback);
// }
//
// extern "C" fn rust_callback(data: *const u8, len: usize) {
//     unsafe {
//         let slice = std::slice::from_raw_parts(data, len);
//         println!("Получено {} байт", slice.len());
//     }
// }
//
// fn main() {
//     unsafe {
//         c_function_with_callback(rust_callback);
//     }
// }
```

### 5.5 Пример: Управление памятью

**Важно:** При работе с FFI нужно правильно управлять памятью!

**Example: Безопасное управление памятью**

```rust
use std::ffi::CString;

#[no_mangle]
pub extern "C" fn allocate_string() -> *mut std::os::raw::c_char {
    let s = CString::new("Hello").unwrap();
    s.into_raw()
}

#[no_mangle]
pub extern "C" fn free_string(ptr: *mut std::os::raw::c_char) {
    unsafe {
        if !ptr.is_null() {
            let _ = CString::from_raw(ptr);
        }
    }
}
```

---

## 6. Безопасность FFI

### 6.1 Риски FFI

**Основные риски:**

- Невалидные указатели
- Утечки памяти
- Неправильное управление ресурсами
- Нарушение инвариантов

### 6.2 Best Practices

**Рекомендации:**

1. Изолируйте unsafe код в безопасные обёртки
2. Документируйте все инварианты
3. Тестируйте тщательно
4. Используйте типы из std::ffi для строк
5. Проверяйте указатели на null

### 6.3 Пример: Безопасная обёртка

```rust
use std::ffi::CString;

pub struct SafeCString {
    ptr: *mut std::os::raw::c_char,
}

impl SafeCString {
    pub fn new(s: &str) -> Result<Self, std::ffi::NulError> {
        let cstr = CString::new(s)?;
        Ok(SafeCString {
            ptr: cstr.into_raw(),
        })
    }
    
    pub fn as_ptr(&self) -> *const std::os::raw::c_char {
        self.ptr
    }
}

impl Drop for SafeCString {
    fn drop(&mut self) {
        unsafe {
            if !self.ptr.is_null() {
                let _ = CString::from_raw(self.ptr);
            }
        }
    }
}
```

---

## 7. Интеграция с существующим кодом

### 7.1 Постепенная миграция

**Стратегии:**

- Начать с новых компонентов на Rust
- Использовать FFI для интеграции
- Постепенно мигрировать критические части

### 7.2 Пример: Гибридный подход

```rust
// Rust компонент, вызываемый из C
#[no_mangle]
pub extern "C" fn process_data(data: *const u8, len: usize) -> i32 {
    unsafe {
        let slice = std::slice::from_raw_parts(data, len);
        // Обработка данных на Rust
        slice.len() as i32
    }
}
```

**Использование из C:**
```c
// extern int process_data(const unsigned char* data, size_t len);
//
// int main() {
//     unsigned char data[] = {1, 2, 3, 4, 5};
//     int result = process_data(data, sizeof(data));
//     printf("Результат: %d\n", result);
//     return 0;
// }
```

---

## 💡 Key Takeaways

- **FFI для межъязыкового взаимодействия:** Вызов функций между языками

- **bindgen автоматизирует биндинги:** Генерация из C заголовков

- **extern "C" для соглашения вызовов:** Совместимость с C

- **unsafe необходим для FFI:** Низкоуровневое взаимодействие

- **Rust можно использовать из C:** Экспорт функций через FFI

---

## 🚀 Next Steps

**Related Modules:**

- [Rust и ОС](../21_OS/) — системные операции
- [Кейсы системного Rust](../23_System_Cases/) — реальные примеры

**Practice Ideas:**

1. Создайте простую C библиотеку и вызовите её из Rust
2. Используйте bindgen для генерации биндингов
3. Экспортируйте Rust функцию для использования в C
4. Изучите существующие FFI проекты

**Going Deeper:**

- Изучите cbindgen для генерации C заголовков
- Почитайте о безопасности FFI
- Изучите примеры интеграции Rust с существующим кодом

---

## 📚 Additional Resources

**Tools:**

- [bindgen](https://github.com/rust-lang/rust-bindgen) — генерация биндингов
- [cbindgen](https://github.com/eqrion/cbindgen) — генерация C заголовков

**Documentation:**

- [FFI](https://doc.rust-lang.org/nomicon/ffi.html) — документация по FFI

---



