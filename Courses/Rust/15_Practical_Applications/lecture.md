# Практические применения
## CLI‑утилиты, Backend‑сервисы, FFI

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Rust (все предыдущие модули)
- Знать экосистему Rust (см. модуль [14_Ecosystem](../14_Ecosystem/))
- Иметь представление о различных областях применения

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать CLI утилиты на Rust
- Понимать применение Rust в backend разработке
- Использовать FFI для взаимодействия с C/C++
- Выбирать подходящие области применения Rust
- Понимать реальные кейсы использования

---

## 1. CLI утилиты

### 1.1 Почему Rust для CLI

**Преимущества:**

- Быстрая компиляция в нативный код
- Отличная производительность
- Простое распространение (один бинарный файл)
- Богатая экосистема (clap, structopt)
- Низкое потребление памяти

**Сравнение производительности:**

| Инструмент | Язык | Скорость |
|------------|------|----------|
| ripgrep | Rust | ⭐⭐⭐⭐⭐ |
| grep | C | ⭐⭐⭐⭐ |
| ag | C | ⭐⭐⭐ |
| ack | Perl | ⭐⭐ |

### 1.2 Популярные CLI инструменты на Rust

**Примеры:**

- **ripgrep** — быстрый поиск в файлах (замена grep)

- **fd** — альтернатива find

- **bat** — улучшенный cat с подсветкой синтаксиса

- **exa** — улучшенный ls

- **dust** — анализ использования диска

- **hyperfine** — бенчмаркинг команд

- **zoxide** — умный cd

**Почему они популярны:**

- Быстрее аналогов
- Лучший UX
- Современный дизайн
- Активная разработка

### 1.3 Создание CLI утилиты

**Example: Базовая структура**

```rust
// Используя clap для парсинга аргументов
// Требует: clap = { version = "4", features = ["derive"] }
// use clap::Parser;

// #[derive(Parser, Debug)]
// #[command(name = "myapp", about = "Описание приложения")]
// struct Args {
//     #[arg(short, long)]
//     name: String,
//     
//     #[arg(short, long, default_value_t = 1)]
//     count: u32,
// }

// fn main() {
//     let args = Args::parse();
//     for _ in 0..args.count {
//         println!("Hello, {}!", args.name);
//     }
// }
```

**Example: Более сложная утилита**

```rust
// use clap::{Parser, Subcommand};
//
// #[derive(Parser)]
// #[command(name = "filetool")]
// struct Cli {
//     #[command(subcommand)]
//     command: Commands,
// }
//
// #[derive(Subcommand)]
// enum Commands {
//     Read { file: String },
//     Write { file: String, content: String },
// }
//
// fn main() {
//     let cli = Cli::parse();
//     match cli.command {
//         Commands::Read { file } => {
//             println!("Чтение файла: {}", file);
//         }
//         Commands::Write { file, content } => {
//             println!("Запись в файл {}: {}", file, content);
//         }
//     }
// }
```

---

## 2. Backend сервисы

### 2.1 Почему Rust для backend

**Преимущества:**

- Высокая производительность
- Низкое потребление памяти
- Безопасность памяти
- Отличная конкурентность
- Предсказуемая производительность

**Сравнение производительности:**

| Фреймворк | Язык | Запросов/сек |
|-----------|------|--------------|
| actix-web | Rust | ~200,000+ |
| warp | Rust | ~150,000+ |
| Express | Node.js | ~20,000 |
| Django | Python | ~5,000 |

### 2.2 Популярные фреймворки

**Примеры:**

- **actix-web** — высокопроизводительный веб-фреймворк

- **warp** — минималистичный фреймворк

- **axum** — современный фреймворк от tokio

- **rocket** — простой в использовании фреймворк

**Сравнение фреймворков:**

| Фреймворк | Производительность | Простота | Экосистема |
|-----------|-------------------|----------|------------|
| actix-web | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| warp | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| axum | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| rocket | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

### 2.3 Пример: Простой сервер

**Example: actix-web**

```rust
// Требует: actix-web = "4"
// use actix_web::{web, App, HttpServer, Responder};

// async fn hello() -> impl Responder {
//     "Hello, World!"
// }

// #[actix_web::main]
// async fn main() -> std::io::Result<()> {
//     HttpServer::new(|| {
//         App::new().route("/", web::get().to(hello))
//     })
//     .bind("127.0.0.1:8080")?
//     .run()
//     .await
// }
```

**Example: warp**

```rust
// Требует: warp = "0.3"
// tokio = { version = "1", features = ["full"] }
// use warp::Filter;

// #[tokio::main]
// async fn main() {
//     let hello = warp::path("hello")
//         .map(|| format!("Hello, World!"));
//     
//     warp::serve(hello)
//         .run(([127, 0, 0, 1], 8080))
//         .await;
// }
```

### 2.4 Пример: REST API

```rust
// Требует: actix-web = "4"
// serde = { version = "1.0", features = ["derive"] }
// use actix_web::{web, App, HttpServer, Responder};
// use serde::{Serialize, Deserialize};

// #[derive(Serialize, Deserialize)]
// struct User {
//     id: u32,
//     name: String,
// }

// async fn get_user() -> impl Responder {
//     web::Json(User {
//         id: 1,
//         name: String::from("Alice"),
//     })
// }

// #[actix_web::main]
// async fn main() -> std::io::Result<()> {
//     HttpServer::new(|| {
//         App::new()
//             .route("/user", web::get().to(get_user))
//     })
//     .bind("127.0.0.1:8080")?
//     .run()
//     .await
// }
```

---

## 3. FFI (Foreign Function Interface)

### 3.1 Что такое FFI

**FFI** — интерфейс для вызова функций из других языков.

**Основные случаи:**

- Вызов C библиотек из Rust
- Использование Rust из C/C++
- Интеграция с существующим кодом

### 3.2 Вызов C из Rust

**Example: Базовый FFI**

```rust
// extern "C" {
//     fn abs(input: i32) -> i32;
// }
//
// fn main() {
//     unsafe {
//         println!("Абсолютное значение -3: {}", abs(-3));
//     }
// }
```

### 3.3 Использование Rust из C

**Example: Экспорт функции**

```rust
// #[no_mangle]
// pub extern "C" fn add(a: i32, b: i32) -> i32 {
//     a + b
// }
```

**Example: Экспорт структуры**

```rust
// #[repr(C)]
// pub struct Point {
//     x: i32,
//     y: i32,
// }
//
// #[no_mangle]
// pub extern "C" fn create_point(x: i32, y: i32) -> Point {
//     Point { x, y }
// }
```

### 3.4 Создание C библиотеки

**Cargo.toml:**
```toml
[lib]
crate-type = ["cdylib"]
```

**Example: Полный пример**

```rust
// #[no_mangle]
// pub extern "C" fn rust_function(input: i32) -> i32 {
//     input * 2
// }
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

### 3.5 Безопасные обёртки

**Важно:** Создавайте безопасные обёртки над unsafe FFI кодом.

**Example: Безопасная обёртка**

```rust
// extern "C" {
//     fn unsafe_c_function(ptr: *const i32) -> i32;
// }
//
// pub fn safe_wrapper(data: &[i32]) -> i32 {
//     unsafe {
//         unsafe_c_function(data.as_ptr())
//     }
// }
```

---

## 4. Реальные кейсы

### 4.1 Компании, использующие Rust

**Примеры:**

- **Mozilla** — компоненты Firefox

- **Dropbox** — файловое хранилище

- **Discord** — backend сервисы

- **Cloudflare** — сетевые компоненты

- **npm** — реестр пакетов

### 4.2 Проекты на Rust

**Примеры:**

- **Servo** — движок браузера

- **Redox OS** — операционная система

- **Firecracker** — микро-VM

- **Rust compiler** — сам компилятор Rust

### 4.3 Детальные кейсы

**Discord:**

- Миграция с Go на Rust для критических компонентов
- Снижение задержек на 70%
- Улучшение стабильности
- Меньше инцидентов в production

**Cloudflare:**

- Сетевые компоненты на Rust
- Edge computing
- Высокая пропускная способность
- Низкая задержка

**npm:**

- Реестр пакетов
- Обработка миллионов запросов
- Высокая надёжность
- Эффективное использование ресурсов

---

## 5. Сравнение производительности

### 5.1 HTTP серверы

**Бенчмарки (запросов/сек):**

| Фреймворк | Язык | Производительность |
|-----------|------|-------------------|
| actix-web | Rust | ~200,000+ |
| warp | Rust | ~150,000+ |
| Express | Node.js | ~20,000 |
| Django | Python | ~5,000 |
| Flask | Python | ~3,000 |

### 5.2 Потребление памяти

**Сравнение:**

| Язык | Память на задачу | Overhead |
|------|------------------|----------|
| Rust (async) | ~1-2 KB | Минимальный |
| Go (goroutine) | ~2-4 KB | Минимальный |
| Java (thread) | ~1-2 MB | GC |
| Python (thread) | ~8 MB | GC + интерпретатор |

### 5.3 Задержка

**P99 задержка:**

| Язык | P50 | P99 |
|------|-----|-----|
| Rust | <1ms | <5ms |
| Go | <2ms | <10ms |
| Java | <5ms | <20ms |
| Python | <10ms | <50ms |

---

## 6. Практические рекомендации

### 6.1 Когда использовать Rust

**Используйте Rust для:**

- Высоконагруженных сервисов
- Критически важных компонентов
- Системного программирования
- Долгосрочных проектов
- Когда важна безопасность памяти

### 6.2 Стратегии внедрения

**Постепенная миграция:**

1. Начните с новых компонентов
2. Замените критические части
3. Используйте FFI для интеграции
4. Постепенно расширяйте использование

### 6.3 Пример: Миграция компонента

```rust
// Старый код на C
// int process_data(int* data, int len);

// Новый код на Rust
#[no_mangle]
pub extern "C" fn process_data(data: *const i32, len: usize) -> i32 {
    unsafe {
        let slice = std::slice::from_raw_parts(data, len);
        slice.iter().sum()
    }
}
```

---

## 💡 Key Takeaways

- **CLI утилиты:** Rust отлично подходит для быстрых инструментов командной строки

- **Backend сервисы:** Высокая производительность и безопасность

- **FFI для интеграции:** Взаимодействие с существующим C/C++ кодом

- **Реальные применения:** Множество компаний используют Rust в production

- **Выбор области:** Rust подходит для системного программирования и высокопроизводительных сервисов

---

## 🚀 Next Steps

**Related Modules:**

- [Ограничения Rust](../16_Limitations/) — когда Rust не подходит
- [System Programming](../17_System_Programming/) — системное программирование

**Practice Ideas:**

1. Создайте простую CLI утилиту
2. Попробуйте создать простой веб-сервер
3. Изучите существующие проекты на Rust
4. Попробуйте интегрировать Rust с C кодом

**Going Deeper:**

- Изучите конкретные фреймворки (actix-web, warp)
- Почитайте о производительности Rust vs других языков
- Изучите кейсы компаний, использующих Rust

---

## 📚 Additional Resources

**Projects:**

- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust) — список проектов
- [Rust in Production](https://www.rust-lang.org/production) — кейсы компаний

**Frameworks:**

- [actix-web](https://actix.rs/) — веб-фреймворк
- [warp](https://github.com/seanmonstar/warp) — минималистичный фреймворк

---



