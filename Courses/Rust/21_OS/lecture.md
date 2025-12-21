# Rust и операционные системы
## Файлы, дескрипторы, потоки, процессы, сигналы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать системное программирование (см. модуль [17_System_Programming](../17_System_Programming/))
- Знать базовые концепции ОС
- Понимать файловую систему

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с файлами и дескрипторами
- Создавать и управлять процессами
- Работать с потоками на системном уровне
- Обрабатывать сигналы
- Понимать системные вызовы

---

## 1. Работа с файлами

### 1.1 Открытие файлов

**Example: Открытие файла**

```rust

use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::create("hello.txt")?;
    file.write_all(b"Hello, world!")?;
    Ok(())
}
```

### 1.2 Чтение файлов

**Example: Чтение файла**

```rust

use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("hello.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    println!("{}", contents);
    Ok(())
}
```

---

## 2. Процессы

### 2.1 Создание процесса

**Example: Запуск процесса**

```rust

use std::process::Command;

fn main() {
    let output = Command::new("echo")
        .arg("Hello")
        .output()
        .expect("Не удалось выполнить команду");
    
    println!("{}", String::from_utf8_lossy(&output.stdout));
}
```

**Output:**
```

Hello
```

### 2.2 Управление процессами

**Example: Ожидание процесса**

```rust

use std::process::Command;

fn main() {
    let mut child = Command::new("sleep")
        .arg("5")
        .spawn()
        .expect("Не удалось запустить процесс");
    
    let _result = child.wait().expect("Ошибка ожидания");
    println!("Процесс завершён");
}
```

---

## 3. Потоки

### 3.1 Создание потоков

**Example: Системные потоки**

```rust

use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Поток выполняется");
    });
    
    handle.join().unwrap();
}
```

---

## 4. Сигналы

### 4.1 Обработка сигналов

**Example: Обработка SIGINT**

```rust

// Требует: ctrlc = "3.2"
// use ctrlc;

// fn main() {
//     ctrlc::set_handler(move || {
//         println!("Получен сигнал прерывания");
//         std::process::exit(0);
//     }).expect("Ошибка установки обработчика");
//
//     loop {
//         std::thread::sleep(std::time::Duration::from_secs(1));
//     }
// }
```

### 4.2 Другие сигналы

**Примеры сигналов:**

- **SIGINT** — прерывание (Ctrl+C)

- **SIGTERM** — завершение процесса

- **SIGHUP** — hangup

- **SIGUSR1/USR2** — пользовательские сигналы

---

## 5. Системные вызовы

### 5.1 Прямые системные вызовы

**Для прямых системных вызовов используйте библиотеки:**

- **nix** — Unix системные вызовы

- **winapi** — Windows API

- **libc** — C библиотека

**Example: Использование nix**

```rust

// Требует: nix = "0.27"
// use nix::unistd::{fork, ForkResult};
// use nix::sys::wait::wait;

// fn main() {
//     match unsafe { fork() } {
//         Ok(ForkResult::Parent { child, .. }) => {
//             println!("Родительский процесс, child PID: {}", child);
//             wait().unwrap();
//         }
//         Ok(ForkResult::Child) => {
//             println!("Дочерний процесс");
//         }
//         Err(err) => {
//             eprintln!("Ошибка fork: {}", err);
//         }
//     }
// }
```

### 5.2 Работа с файловыми дескрипторами

**Example: Низкоуровневая работа с файлами**

```rust

use std::fs::File;
use std::os::unix::io::{AsRawFd, RawFd};

fn main() -> std::io::Result<()> {
    let file = File::create("test.txt")?;
    let fd: RawFd = file.as_raw_fd();
    
    println!("Файловый дескриптор: {}", fd);
    Ok(())
}
```

---

## 6. Практические примеры

### 6.1 Пример: Простой процесс-менеджер

```rust

use std::process::Command;

fn main() {
    let mut processes = Vec::new();
    
    for i in 1..=3 {
        let mut cmd = Command::new("sleep");
        cmd.arg("2");
        
        match cmd.spawn() {
            Ok(child) => {
                processes.push(child);
                println!("Запущен процесс {}", i);
            }
            Err(e) => {
                eprintln!("Ошибка запуска процесса {}: {}", i, e);
            }
        }
    }
    
    for mut child in processes {
        match child.wait() {
            Ok(status) => println!("Процесс завершён: {:?}", status),
            Err(e) => eprintln!("Ошибка ожидания: {}", e),
        }
    }
}
```

### 6.2 Пример: Многопоточная обработка файлов

```rust

use std::fs;
use std::thread;

fn process_file(filename: &str) {
    match fs::read_to_string(filename) {
        Ok(content) => {
            println!("Файл {}: {} байт", filename, content.len());
        }
        Err(e) => {
            eprintln!("Ошибка чтения {}: {}", filename, e);
        }
    }
}

fn main() {
    let files = vec!["file1.txt", "file2.txt", "file3.txt"];
    let mut handles = Vec::new();
    
    for file in files {
        let handle = thread::spawn(move || {
            process_file(file);
        });
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

### 6.3 Пример: Мониторинг процессов

```rust

use std::process::Command;

fn get_process_info(pid: u32) -> std::io::Result<String> {
    let output = Command::new("ps")
        .arg("-p")
        .arg(pid.to_string())
        .output()?;
    
    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

fn main() {
    match get_process_info(1) {
        Ok(info) => println!("{}", info),
        Err(e) => eprintln!("Ошибка: {}", e),
    }
}
```

### 6.4 Пример: Работа с переменными окружения

```rust

use std::env;

fn main() {
    // Получение переменной окружения
    match env::var("PATH") {
        Ok(path) => println!("PATH: {}", path),
        Err(e) => eprintln!("Ошибка: {}", e),
    }
    
    // Установка переменной окружения для дочернего процесса
    let mut cmd = std::process::Command::new("echo");
    cmd.env("MY_VAR", "my_value");
    cmd.arg("$MY_VAR");
    cmd.status().unwrap();
}
```

---

## 7. Продвинутые темы

### 7.1 Работа с сокетами

**Example: TCP сервер**

```rust

// use std::net::{TcpListener, TcpStream};
// use std::io::{Read, Write};
//
// fn handle_client(mut stream: TcpStream) {
//     let mut buffer = [0; 1024];
//     stream.read(&mut buffer).unwrap();
//     stream.write(b"HTTP/1.1 200 OK\r\n\r\nHello").unwrap();
// }
//
// fn main() -> std::io::Result<()> {
//     let listener = TcpListener::bind("127.0.0.1:8080")?;
//     
//     for stream in listener.incoming() {
//         handle_client(stream?);
//     }
//     Ok(())
// }
```

### 7.2 Работа с разделяемой памятью

**Example: Концептуальный пример**

```rust

// use std::sync::mpsc;
//
// fn main() {
//     let (tx, rx) = mpsc::channel();
//     
//     std::thread::spawn(move || {
//         tx.send("Данные").unwrap();
//     });
//     
//     let received = rx.recv().unwrap();
//     println!("Получено: {}", received);
// }
```

### 7.3 Работа с временем

```rust

use std::time::{SystemTime, UNIX_EPOCH};

fn get_timestamp() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs()
}

fn main() {
    println!("Текущий timestamp: {}", get_timestamp());
}
```

---

## 💡 Key Takeaways

- **Файлы через стандартную библиотеку:** File, read, write операции

- **Процессы через Command:** Создание и управление процессами

- **Потоки через thread:** Многопоточность на системном уровне

- **Сигналы требуют библиотек:** ctrlc для обработки сигналов

- **Системные вызовы абстрагированы:** Стандартная библиотека скрывает детали

---

## 🚀 Next Steps

**Related Modules:**

- [Встраиваемые системы](../22_Embedded/) — embedded Rust
- [Кейсы системного Rust](../23_System_Cases/) — реальные примеры

**Practice Ideas:**

1. Создайте программу для работы с файлами
2. Реализуйте простой процесс-менеджер
3. Попробуйте обработку сигналов
4. Изучите системные вызовы в вашей ОС

**Going Deeper:**

- Изучите nix crate для Unix системных вызовов
- Почитайте о различиях между платформами
- Изучите примеры системного кода на Rust

---

## 📚 Additional Resources

**Libraries:**

- [nix](https://github.com/nix-rust/nix) — Unix системные вызовы
- [ctrlc](https://github.com/Detegr/rust-ctrlc) — обработка сигналов

---


