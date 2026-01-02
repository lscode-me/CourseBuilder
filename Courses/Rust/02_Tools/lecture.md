# Инструменты Rust
## rustup, cargo, rustc и структура проекта

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции программирования
- Уметь работать с командной строкой
- Иметь доступ к интернету для установки инструментов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Установить и настроить Rust через rustup
- Использовать cargo для создания и управления проектами
- Понимать структуру проекта Rust
- Компилировать код с помощью rustc
- Использовать основные команды cargo для разработки

---

## 1. Установка Rust

### 1.1 rustup — менеджер версий Rust

**rustup** — официальный инструмент для установки и управления версиями Rust. Он позволяет:
- Устанавливать различные версии Rust
- Переключаться между версиями
- Обновлять Rust
- Устанавливать компоненты (toolchains)

**Установка rustup:**

На Linux и macOS:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

На Windows:
```powershell
# Скачать и запустить rustup-init.exe с https://rustup.rs
```

После установки нужно перезагрузить терминал или выполнить:
```bash
source $HOME/.cargo/env
```

**Проверка установки:**

```bash
rustc --version
cargo --version
rustup --version
```

**Output:**
```
rustc 1.75.0 (82e1608df 2023-12-21)
cargo 1.75.0 (1d8b05cdd 2023-11-20)
rustup 1.26.0 (5af9b9484 2023-04-05)
```

### 1.2 Компоненты Rust

Rust состоит из нескольких компонентов:

- **rustc** — компилятор Rust

- **cargo** — менеджер пакетов и система сборки

- **rustdoc** — генератор документации

- **rustfmt** — форматировщик кода

- **clippy** — линтер с полезными советами

- **rust-analyzer** — LSP сервер для IDE

**Установка дополнительных компонентов:**

```bash
# Установка rustfmt и clippy

rustup component add rustfmt
rustup component add clippy

# Установка rust-analyzer (для IDE)

rustup component add rust-analyzer
```

---

## 2. rustc — компилятор Rust

### 2.1 Базовое использование

**rustc** — компилятор Rust, который преобразует исходный код в исполняемый файл.

**Example: Простая программа**

Создайте файл `main.rs`:

```rust
fn main() {
    println!("Hello, Rust!");
}
```

**Компиляция:**

```bash
rustc main.rs
```

**Output:**
```
# Создаётся исполняемый файл main (или main.exe на Windows)
```

**Запуск:**

```bash
./main
```

**Output:**
```
Hello, Rust!
```

### 2.2 Опции компилятора

**Вывод информации о компиляции:**

```bash
rustc --version --verbose
```

**Output:**
```
rustc 1.75.0 (82e1608df 2023-12-21)
binary: rustc
commit-hash: 82e1608df2b92c5d5b3e8e3c3c3c3c3c3c3c3c3c3
commit-date: 2023-12-21
host: x86_64-unknown-linux-gnu
release: 1.75.0
LLVM version: 17.0.6
```

**Оптимизация:**

```bash
rustc -O main.rs  # Оптимизация для производительности
```

**Вывод предупреждений:**

```bash
rustc -W unused main.rs  # Предупреждения о неиспользуемом коде
```

> **💡 Pro Tip:**  
> В реальных проектах используется `cargo`, а не прямой вызов `rustc`. `rustc` полезен для понимания процесса компиляции и простых примеров.

---

## 3. cargo — менеджер пакетов и система сборки

### 3.1 Что такое cargo

**cargo** — стандартный инструмент для управления проектами Rust. Он выполняет:
- Создание новых проектов
- Компиляцию кода
- Запуск тестов
- Управление зависимостями
- Сборку документации
- Публикацию пакетов

**cargo автоматически устанавливается вместе с Rust.**

### 3.2 Создание нового проекта

**Создание бинарного проекта (исполняемый файл):**

```bash
cargo new hello_rust
```

**Output:**
```
Created binary (application) `hello_rust` package
```

**Структура созданного проекта:**

```
hello_rust/
├── Cargo.toml
└── src/
    └── main.rs
```

**Создание библиотечного проекта:**

```bash
cargo new my_lib --lib
```

**Output:**
```
Created library `my_lib` package
```

**Структура библиотечного проекта:**

```
my_lib/
├── Cargo.toml
└── src/
    └── lib.rs
```

### 3.3 Основные команды cargo

**Компиляция проекта:**

```bash
cargo build
```

**Output:**
```
Compiling hello_rust v0.1.0 (/path/to/hello_rust)
Finished dev [unoptimized + debuginfo] target(s) in 0.50s
```

**Компиляция с оптимизацией (release):**

```bash
cargo build --release
```

**Output:**
```
Compiling hello_rust v0.1.0 (/path/to/hello_rust)
Finished release [optimized] target(s) in 0.60s
```

**Запуск проекта:**

```bash
cargo run
```

**Output:**
```
Compiling hello_rust v0.1.0 (/path/to/hello_rust)
Finished dev [unoptimized + debuginfo] target(s) in 0.50s
Running `target/debug/hello_rust`
Hello, world!
```

**Проверка кода (без компиляции):**

```bash
cargo check
```

**Output:**
```
Checking hello_rust v0.1.0 (/path/to/hello_rust)
Finished dev [unoptimized + debuginfo] target(s) in 0.20s
```

**Форматирование кода:**

```bash
cargo fmt
```

**Output:**
```
# Код отформатирован согласно стандартам Rust
```

**Проверка с clippy:**

```bash
cargo clippy
```

**Output:**
```
Checking hello_rust v0.1.0 (/path/to/hello_rust)
Finished dev [unoptimized + debuginfo] target(s) in 0.50s
```

---

## 4. Структура проекта Rust

### 4.1 Файл Cargo.toml

**Cargo.toml** — манифест проекта, содержащий метаданные и зависимости.

**Example: Базовый Cargo.toml**

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2021"

[dependencies]
```

**Поля манифеста:**

- **name** — имя пакета

- **version** — версия (семантическое версионирование)

- **edition** — издание Rust (2015, 2018, 2021)

- **authors** — авторы (опционально)

- **description** — описание (опционально)

- **license** — лицензия (опционально)

- **dependencies** — зависимости проекта

### 4.2 Структура директорий

**Стандартная структура проекта:**

```
my_project/
├── Cargo.toml          # Манифест проекта
├── Cargo.lock          # Закреплённые версии зависимостей
├── src/                # Исходный код
│   ├── main.rs         # Точка входа для бинарного проекта
│   ├── lib.rs          # Точка входа для библиотеки
│   └── bin/            # Дополнительные исполняемые файлы
├── tests/              # Интеграционные тесты
├── examples/           # Примеры использования
├── benches/            # Бенчмарки
└── target/             # Скомпилированные файлы (генерируется)
    ├── debug/          # Debug сборка
    └── release/        # Release сборка
```

**target/** — директория со скомпилированными файлами (обычно добавляется в .gitignore).

### 4.3 Модули и файлы

**Организация кода в модули:**

```
src/
├── main.rs
├── lib.rs
├── config.rs
├── utils/
│   ├── mod.rs
│   └── helpers.rs
└── models/
    ├── mod.rs
    └── user.rs
```

**Example: Модульная структура**

**src/main.rs:**
```rust
mod config;
mod utils;
mod models;

use config::Config;
use utils::helpers::helper_function;

fn main() {
    let config = Config::new();
    helper_function();
}
```

**src/config.rs:**
```rust
pub struct Config {
    pub name: String,
}

impl Config {
    pub fn new() -> Self {
        Config {
            name: String::from("My App"),
        }
    }
}
```

**src/utils/mod.rs:**
```rust
pub mod helpers;
```

**src/utils/helpers.rs:**
```rust
pub fn helper_function() {
    println!("Helper function called");
}
```

---

## 5. Управление зависимостями

### 5.1 Добавление зависимостей

**Добавление зависимости в Cargo.toml:**

```toml
[dependencies]
serde = "1.0"
tokio = { version = "1.0", features = ["full"] }
reqwest = { version = "0.11", default-features = false }
```

**Установка зависимостей:**

```bash
cargo build
```

cargo автоматически загрузит и скомпилирует зависимости.

### 5.2 Версионирование зависимостей

**Семантическое версионирование:**

```toml
[dependencies]
# Точная версия

serde = "1.0.0"

# Совместимая версия (1.x.x)

serde = "1.0"

# Любая версия из диапазона

serde = ">=1.0, <2.0"

# Из git репозитория

my_lib = { git = "https://github.com/user/repo" }

# Из локального пути

my_lib = { path = "../my_lib" }
```

### 5.3 Cargo.lock

**Cargo.lock** — файл, фиксирующий точные версии зависимостей.

**Когда используется:**

- Для бинарных проектов (приложения)
- Обеспечивает воспроизводимые сборки

**Когда не коммитится:**

- Для библиотечных проектов (crates)
- Зависимости решаются на уровне приложения

---

## 6. Рабочие пространства (Workspaces)

### 6.1 Что такое workspace

**Workspace** — группа связанных проектов, которые совместно используют Cargo.lock и директорию target.

**Example: Структура workspace**

```
my_workspace/
├── Cargo.toml          # Workspace манифест
├── binary_crate/
│   ├── Cargo.toml
│   └── src/
│       └── main.rs
└── library_crate/
    ├── Cargo.toml
    └── src/
        └── lib.rs
```

**my_workspace/Cargo.toml:**

```toml
[workspace]
members = [
    "binary_crate",
    "library_crate",
]
```

### 6.2 Преимущества workspace

- Общая директория target (экономия места)
- Единый Cargo.lock
- Упрощённое управление зависимостями
- Параллельная компиляция

---

## 7. Тестирование

### 7.1 Unit тесты

**Тесты в том же файле:**

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
```

**Запуск тестов:**

```bash
cargo test
```

**Output:**
```
running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

### 7.2 Интеграционные тесты

**Файл tests/integration_test.rs:**

```rust
use my_lib;

#[test]
fn test_integration() {
    assert_eq!(my_lib::add(2, 2), 4);
}
```

---

## 8. Документация

### 8.1 Генерация документации

**Создание документации:**

```bash
cargo doc
```

**Просмотр документации:**

```bash
cargo doc --open
```

**Example: Документирование кода**

```rust
/// Adds two numbers together.
///
/// # Examples
///
/// ```
/// let result = add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

---

## 9. Полезные команды cargo

### 9.1 Обновление зависимостей

```bash
# Обновить все зависимости

cargo update

# Обновить конкретную зависимость

cargo update -p serde
```

### 9.2 Очистка проекта

```bash
# Удалить директорию target

cargo clean
```

### 9.3 Публикация пакета

```bash
# Публикация на crates.io

cargo publish
```

### 9.4 Установка бинарных crates

```bash
# Установить crate глобально

cargo install cargo-watch

# Использование

cargo watch -x run
```

---

## 10. Интеграция с IDE

### 10.1 rust-analyzer

**rust-analyzer** — LSP сервер для IDE, обеспечивающий:
- Автодополнение
- Проверку типов
- Рефакторинг
- Навигацию по коду
- Форматирование

**Установка:**

```bash
rustup component add rust-analyzer
```

**Поддерживаемые IDE:**

- VS Code (расширение rust-analyzer)
- IntelliJ IDEA / CLion (плагин Rust)
- Vim / Neovim (через LSP)
- Emacs (через LSP)

### 10.2 Настройка VS Code

**Установка расширения:**

1. Откройте VS Code
2. Перейдите в Extensions (Ctrl+Shift+X)
3. Найдите "rust-analyzer"
4. Установите расширение

**Файл настроек .vscode/settings.json:**

```json
{
    "rust-analyzer.checkOnSave.command": "clippy",
    "rust-analyzer.inlayHints.enable": true,
    "editor.formatOnSave": true,
    "[rust]": {
        "editor.defaultFormatter": "rust-lang.rust-analyzer"
    }
}
```

---

## 💡 Key Takeaways

- **rustup управляет версиями Rust:** Установка, обновление, переключение между версиями

- **cargo — основной инструмент разработки:** Создание проектов, управление зависимостями, сборка, тестирование

- **Cargo.toml определяет проект:** Метаданные, зависимости, конфигурация

- **Структура проекта стандартизирована:** src/, tests/, examples/, target/

- **rust-analyzer обеспечивает отличный опыт разработки:** Автодополнение, проверка типов, рефакторинг

---

## 🚀 Next Steps

**Related Modules:**

- [Первая программа](../03_First_Program/) — напишем первую программу на Rust
- [Переменные и типы](../04_Variables_Types/) — изучим базовые типы данных

**Practice Ideas:**

1. Установите Rust и проверьте версию: `rustc --version`
2. Создайте новый проект: `cargo new my_first_project`
3. Изучите структуру созданного проекта
4. Запустите проект: `cargo run`

**Going Deeper:**

- [Cargo Book](https://doc.rust-lang.org/cargo/) — официальная документация по cargo
- [rustup Book](https://rust-lang.github.io/rustup/) — документация по rustup
- Изучите популярные crates на crates.io

---

## 📚 Additional Resources

**Documentation:**

- [Cargo Book](https://doc.rust-lang.org/cargo/) — полная документация по cargo
- [rustup Book](https://rust-lang.github.io/rustup/) — руководство по rustup
- [The Edition Guide](https://doc.rust-lang.org/edition-guide/) — руководство по изданиям Rust

**Tools:**

- [crates.io](https://crates.io/) — центральный реестр пакетов
- [rust-analyzer](https://rust-analyzer.github.io/) — LSP сервер для IDE
- [Clippy](https://github.com/rust-lang/rust-clippy) — линтер для Rust

---




