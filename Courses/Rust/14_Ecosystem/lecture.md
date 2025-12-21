# Экосистема
## crates.io, популярные crates, версионирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать cargo и управление зависимостями (см. модуль [02_Tools](../02_Tools/))
- Знать базовые концепции Rust
- Иметь представление о пакетных менеджерах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать crates.io для поиска библиотек
- Понимать семантическое версионирование
- Знать популярные crates для различных задач
- Управлять зависимостями в проектах
- Выбирать подходящие библиотеки для задач

---

## 1. crates.io

### 1.1 Что такое crates.io

**crates.io** — центральный реестр пакетов Rust (аналог npm, PyPI).

**Характеристики:**

- Более 100,000 crates
- Открытый и бесплатный
- Интегрирован с cargo
- Автоматическая документация

### 1.2 Поиск crates

**Способы поиска:**

- Веб-сайт: https://crates.io
- Команда: `cargo search название`
- Документация: https://docs.rs

**Example: Поиск через cargo**

```bash

cargo search serde
```

### 1.3 Добавление зависимостей

**Example: Добавление в Cargo.toml**

```toml

[dependencies]
serde = "1.0"
tokio = { version = "1.0", features = ["full"] }
reqwest = "0.11"
```

---

## 2. Популярные crates

### 2.1 Сериализация: serde

**serde** — фреймворк для сериализации/десериализации.

**Использование:**

- JSON, YAML, TOML и другие форматы
- Автоматическая генерация кода

**Example: Базовое использование**

```rust

// Требует: serde = { version = "1.0", features = ["derive"] }
// serde_json = "1.0"
// use serde::{Serialize, Deserialize};
// use serde_json;

// #[derive(Serialize, Deserialize, Debug)]
// struct User {
//     name: String,
//     age: u32,
// }
//
// fn main() {
//     let user = User {
//         name: String::from("Alice"),
//         age: 30,
//     };
//     
//     let json = serde_json::to_string(&user).unwrap();
//     println!("{}", json);
//     
//     let deserialized: User = serde_json::from_str(&json).unwrap();
//     println!("{:?}", deserialized);
// }
```

**Преимущества:**

- Автоматическая генерация кода
- Поддержка множества форматов
- Высокая производительность

### 2.2 Асинхронность: tokio

**tokio** — асинхронный runtime для Rust.

**Использование:**

- Сетевые приложения
- Высокопроизводительные сервисы
- Параллельная обработка

**Example: Базовое использование**

```rust

// Требует: tokio = { version = "1", features = ["full"] }
// use tokio::time::{sleep, Duration};
//
// #[tokio::main]
// async fn main() {
//     println!("Начало");
//     sleep(Duration::from_secs(1)).await;
//     println!("Конец");
// }
```

**Особенности:**

- Work-stealing scheduler
- Высокая производительность
- Богатая экосистема

### 2.3 HTTP клиент: reqwest

**reqwest** — HTTP клиент для Rust.

**Использование:**

- API запросы
- Веб-скрапинг
- Интеграция с сервисами

**Example: Базовое использование**

```rust

// Требует: reqwest = { version = "0.11", features = ["json"] }
// tokio = { version = "1", features = ["full"] }
// use reqwest;
//
// #[tokio::main]
// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let response = reqwest::get("https://httpbin.org/get").await?;
//     let body = response.text().await?;
//     println!("{}", body);
//     Ok(())
// }
```

### 2.4 CLI: clap

**clap** — парсер аргументов командной строки.

**Использование:**

- CLI утилиты
- Парсинг аргументов
- Генерация help

**Example: Базовое использование**

```rust

// Требует: clap = { version = "4", features = ["derive"] }
// use clap::Parser;
//
// #[derive(Parser, Debug)]
// #[command(name = "myapp")]
// struct Args {
//     #[arg(short, long)]
//     name: String,
//     
//     #[arg(short, long, default_value_t = 1)]
//     count: u32,
// }
//
// fn main() {
//     let args = Args::parse();
//     println!("{:?}", args);
// }
```

### 2.5 Логирование: log, env_logger

**log** — унифицированный интерфейс логирования.

**env_logger** — реализация для log.

**Example: Базовое использование**

```rust

// Требует: log = "0.4"
// env_logger = "0.10"
// use log::{info, warn, error};
//
// fn main() {
//     env_logger::init();
//     
//     info!("Информационное сообщение");
//     warn!("Предупреждение");
//     error!("Ошибка");
// }
```

### 2.6 Другие популярные crates

**Примеры:**

- **rayon** — параллельные вычисления

- **chrono** — работа с датами и временем

- **regex** — регулярные выражения

- **uuid** — генерация UUID

- **rand** — генерация случайных чисел

- **anyhow** — упрощённая обработка ошибок

- **thiserror** — создание типов ошибок

---

## 3. Версионирование

### 3.1 Семантическое версионирование

**Формат: MAJOR.MINOR.PATCH**

- **MAJOR** — несовместимые изменения

- **MINOR** — новая функциональность (обратно совместимо)

- **PATCH** — исправления ошибок (обратно совместимо)

**Example: Версии в Cargo.toml**

```toml

[dependencies]
serde = "1.0"        # 1.0.x (любая 1.0)
serde = "1.0.0"      # Точная версия
serde = "^1.0"       # Совместимая версия
serde = "~1.0.0"     # Обновления патчей
serde = ">=1.0, <2.0" # Диапазон версий
```

### 3.2 Cargo.lock

**Cargo.lock** фиксирует точные версии зависимостей для воспроизводимых сборок.

**Когда используется:**

- Для бинарных проектов (приложения)
- Обеспечивает воспроизводимые сборки

**Когда не коммитится:**

- Для библиотечных проектов (crates)
- Зависимости решаются на уровне приложения

### 3.3 Features (функции)

**Features** позволяют включать/выключать функциональность.

**Example: Features в Cargo.toml**

```toml

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1.0", features = ["full"] }
reqwest = { version = "0.11", default-features = false, features = ["json"] }
```

**Преимущества:**

- Уменьшение размера бинарника
- Включение только нужной функциональности
- Гибкая конфигурация

---

## 4. Поиск и выбор crates

### 4.1 Критерии выбора

**При выборе crate учитывайте:**

- Количество загрузок
- Последнее обновление
- Качество документации
- Активность разработки
- Лицензия

### 4.2 Оценка качества

**Признаки хорошего crate:**

- Хорошая документация
- Активная разработка
- Тесты
- Примеры использования
- Обработка ошибок

### 4.3 Альтернативные источники

**Помимо crates.io:**

- Git репозитории
- Локальные пути
- Workspace зависимости

**Example: Git зависимость**

```toml

[dependencies]
my_lib = { git = "https://github.com/user/repo", branch = "main" }
```

**Example: Локальный путь**

```toml

[dependencies]
my_lib = { path = "../my_lib" }
```

### 4.4 Workspace

**Workspace** — группа связанных проектов.

**Example: Структура workspace**

```toml
# Cargo.toml (корень)
[workspace]
members = ["crate1", "crate2", "crate3"]

# Все члены workspace разделяют один Cargo.lock

```

**Преимущества:**

- Единый Cargo.lock
- Общие зависимости
- Упрощённая сборка

---

## 5. Управление зависимостями

### 5.1 Типы зависимостей

**dependencies** — для production кода:
```toml

[dependencies]
serde = "1.0"
```

**dev-dependencies** — только для разработки:
```toml

[dev-dependencies]
mockito = "1.0"
```

**build-dependencies** — для build.rs:
```toml

[build-dependencies]
bindgen = "0.65"
```

### 5.2 Обновление зависимостей

**Команды:**

- `cargo update` — обновляет зависимости в Cargo.lock
- `cargo outdated` — показывает устаревшие зависимости
- `cargo audit` — проверяет уязвимости

### 5.3 Удаление зависимостей

**Просто удалите строку из Cargo.toml:**
```toml

[dependencies]
# serde = "1.0"  # Удалено

```

Затем запустите `cargo build` для обновления Cargo.lock.

---

## 6. Публикация crates

### 6.1 Подготовка к публикации

**Требования:**

- Уникальное имя
- Версия в формате semver
- Описание в Cargo.toml
- Лицензия

**Example: Cargo.toml для публикации**

```toml

[package]
name = "my-awesome-crate"
version = "0.1.0"
edition = "2021"
description = "Описание crate"
license = "MIT OR Apache-2.0"
authors = ["Your Name <you@example.com>"]
```

### 6.2 Публикация

**Шаги:**

1. Создайте аккаунт на crates.io
2. Получите API токен
3. `cargo login <token>`
4. `cargo publish`

### 6.3 Версионирование после публикации

**Правила:**

- Нельзя изменить опубликованную версию
- Нужно увеличить версию для изменений
- Следуйте semver

---

## 7. Практические примеры

### 7.1 Пример: Создание проекта с зависимостями

**Cargo.toml:**
```toml

[package]
name = "my-project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
reqwest = "0.11"

[dev-dependencies]
tokio-test = "0.4"
```

### 7.2 Пример: Использование features

```toml

[dependencies]
my-crate = { version = "1.0", default-features = false, features = ["feature1", "feature2"] }
```

### 7.3 Пример: Условные зависимости

```toml

[target.'cfg(unix)'.dependencies]
libc = "0.2"

[target.'cfg(windows)'.dependencies]
winapi = "0.3"
```

---

## 💡 Key Takeaways

- **crates.io — центральный реестр:** Более 100,000 библиотек

- **Популярные crates покрывают основные задачи:** serde, tokio, reqwest, clap

- **Семантическое версионирование:** MAJOR.MINOR.PATCH

- **Cargo.lock для воспроизводимости:** Фиксирует точные версии

- **Документация на docs.rs:** Автоматически генерируется

---

## 🚀 Next Steps

**Related Modules:**

- [Практические применения](../15_Practical_Applications/) — использование crates в реальных проектах
- [Ограничения Rust](../16_Limitations/) — когда Rust не подходит

**Practice Ideas:**

1. Найдите и добавьте crate для вашей задачи
2. Изучите документацию популярных crates
3. Попробуйте создать свой crate
4. Изучите зависимости существующих проектов

**Going Deeper:**

- Изучите создание и публикацию собственных crates
- Почитайте о workspace для больших проектов
- Изучите альтернативные реестры (Git, локальные пути)

---

## 📚 Additional Resources

**Websites:**

- [crates.io](https://crates.io/) — центральный реестр
- [docs.rs](https://docs.rs/) — документация crates
- [lib.rs](https://lib.rs/) — альтернативный поиск crates

**Documentation:**

- [Cargo Book](https://doc.rust-lang.org/cargo/) — документация по cargo

---



