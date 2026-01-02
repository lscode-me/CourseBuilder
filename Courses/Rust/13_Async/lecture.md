# Асинхронность
## Threads, async/await, Futures

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Знать функции и модули (см. модуль [06_Functions_Modules](../06_Functions_Modules/))
- Понимать базовые концепции многопоточности

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять потоками (threads)
- Использовать async/await для асинхронного кода
- Понимать концепцию Futures
- Различать синхронный и асинхронный код
- Применять асинхронность в практических задачах

---

## 1. Threads (Потоки)

### 1.1 Создание потоков

**Threads** — позволяют выполнять код параллельно.

**Example: Создание потока**

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("Поток: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("Главный поток: {}", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

**Output:**
```
Главный поток: 1
Поток: 1
Главный поток: 2
Поток: 2
...
```

### 1.2 Ожидание завершения потока

**Example: join()**

```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Поток выполняется");
    });

    handle.join().unwrap();
    println!("Поток завершён");
}
```

**Output:**
```
Поток выполняется
Поток завершён
```

### 1.3 Передача данных в поток

**Example: move замыкания**

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Вектор: {:?}", v);
    });

    handle.join().unwrap();
}
```

**Output:**
```
Вектор: [1, 2, 3]
```

**`move`** передаёт владение в замыкание.

### 1.4 Разделяемые данные с Arc и Mutex

**Для разделения данных между потоками используйте Arc и Mutex:**

**Example: Arc и Mutex**

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Результат: {}", *counter.lock().unwrap());
}
```

**Output:**
```
Результат: 10
```

**Arc** — атомарный счётчик ссылок для многопоточности.
**Mutex** — взаимное исключение для безопасного доступа.

### 1.5 Каналы для коммуникации

**Каналы позволяют передавать данные между потоками:**

**Example: Каналы**

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("привет");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Получено: {}", received);
}
```

**Output:**
```
Получено: привет
```

**mpsc** — multiple producer, single consumer канал.

### 1.6 Множественные отправители

**Example: Несколько отправителей**

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx1 = tx.clone();

    thread::spawn(move || {
        tx.send(String::from("привет")).unwrap();
    });

    thread::spawn(move || {
        tx1.send(String::from("мир")).unwrap();
    });

    for received in rx {
        println!("Получено: {}", received);
    }
}
```

**Output:**
```
Получено: привет
Получено: мир
```

---

## 2. async/await

### 2.1 Базовый синтаксис

**async/await** — способ написания асинхронного кода.

**Example: async функция**

```rust
async fn hello() -> String {
    String::from("Hello, async!")
}

fn main() {
    let future = hello();
    // future - это Future, нужно запустить через runtime
}
```

### 2.2 Использование await

**Example: await**

```rust
use std::time::Duration;
use tokio::time::sleep;

async fn async_function() {
    println!("Начало");
    sleep(Duration::from_secs(1)).await;
    println!("Конец");
}

#[tokio::main]
async fn main() {
    async_function().await;
}
```

**Output:**
```
Начало
Конец
```

### 2.3 Параллельное выполнение

**Example: tokio::join!**

```rust
use tokio::time::{sleep, Duration};

async fn task1() {
    sleep(Duration::from_secs(1)).await;
    println!("Задача 1 завершена");
}

async fn task2() {
    sleep(Duration::from_secs(1)).await;
    println!("Задача 2 завершена");
}

#[tokio::main]
async fn main() {
    tokio::join!(task1(), task2());
    println!("Обе задачи завершены");
}
```

**Output:**
```
Задача 1 завершена
Задача 2 завершена
Обе задачи завершены
```

**tokio::join!** выполняет несколько futures параллельно.

### 2.4 Обработка ошибок в async

**Example: Result в async функциях**

```rust
use std::io;

async fn read_file() -> Result<String, io::Error> {
    // Симуляция чтения файла
    Ok(String::from("содержимое файла"))
}

#[tokio::main]
async fn main() {
    match read_file().await {
        Ok(content) => println!("{}", content),
        Err(e) => println!("Ошибка: {}", e),
    }
}
```

**Output:**
```
содержимое файла
```

### 2.5 Асинхронные потоки

**Example: Асинхронные потоки с tokio::spawn**

```rust
use tokio::time::{sleep, Duration};

async fn async_task(id: u32) {
    sleep(Duration::from_millis(100)).await;
    println!("Задача {} завершена", id);
}

#[tokio::main]
async fn main() {
    let mut handles = vec![];

    for i in 1..=5 {
        let handle = tokio::spawn(async_task(i));
        handles.push(handle);
    }

    for handle in handles {
        handle.await.unwrap();
    }
}
```

**Output:**
```
Задача 1 завершена
Задача 2 завершена
Задача 3 завершена
Задача 4 завершена
Задача 5 завершена
```

### 2.6 Select для конкурентного выполнения

**Example: tokio::select!**

```rust
use tokio::time::{sleep, Duration, timeout};

async fn task1() -> &'static str {
    sleep(Duration::from_millis(100)).await;
    "Задача 1"
}

async fn task2() -> &'static str {
    sleep(Duration::from_millis(50)).await;
    "Задача 2"
}

#[tokio::main]
async fn main() {
    tokio::select! {
        result = task1() => println!("{}", result),
        result = task2() => println!("{}", result),
    }
}
```

**Output:**
```
Задача 2
```

**select!** выполняет первую завершившуюся задачу.

---

## 3. Futures

### 3.1 Что такое Future

**Future** — значение, которое будет вычислено в будущем.

**Example: Понимание Future**

```rust
use std::future::Future;

async fn example() -> i32 {
    42
}

fn main() {
    // example() возвращает impl Future<Output = i32>
    let future = example();
    // Future нужно запустить через runtime (tokio, async-std и т.д.)
}
```

### 3.2 Создание Future

**Example: Создание Future**

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

struct MyFuture {
    value: i32,
}

impl Future for MyFuture {
    type Output = i32;

    fn poll(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<Self::Output> {
        Poll::Ready(self.value)
    }
}

fn main() {
    let future = MyFuture { value: 42 };
    // Использование через runtime
}
```

### 3.3 Ленивые вычисления

**Futures ленивы — они ничего не делают, пока не запущены:**

**Example: Ленивость Futures**

```rust
async fn expensive_computation() -> i32 {
    println!("Выполняется вычисление");
    42
}

fn main() {
    let future = expensive_computation();
    // Пока ничего не выполняется
    println!("Future создан, но не запущен");
    // Нужен runtime для выполнения
}
```

**Output:**
```
Future создан, но не запущен
```

### 3.4 Композиция Futures

**Futures можно комбинировать:**

**Example: Композиция**

```rust
async fn add_one(x: i32) -> i32 {
    x + 1
}

async fn multiply_two(x: i32) -> i32 {
    x * 2
}

async fn combined(x: i32) -> i32 {
    let result = add_one(x).await;
    multiply_two(result).await
}

#[tokio::main]
async fn main() {
    let result = combined(5).await;
    println!("Результат: {}", result);
}
```

**Output:**
```
Результат: 12
```

---

## 4. Сравнение потоков и async

### 4.1 Когда использовать потоки

**Используйте потоки для:**

- CPU-интенсивных задач
- Параллельных вычислений
- Когда нужен полный контроль

**Примеры:**

- Обработка изображений
- Математические вычисления
- Параллельная сортировка

### 4.2 Когда использовать async

**Используйте async для:**

- I/O операций
- Сетевых запросов
- Когда много задач ожидают I/O

**Примеры:**

- HTTP серверы
- Базы данных
- Файловые операции

### 4.3 Производительность

**Сравнение:**

| Подход | Потоки | Async |
|--------|--------|-------|
| Память на задачу | ~1-2 MB | ~1-2 KB |
| Переключение контекста | Дорогое | Дешёвое |
| Лучше для | CPU задачи | I/O задачи |

---

## 5. Практические примеры

### 5.1 Пример: Асинхронный HTTP запрос

```rust
// Требует зависимости: tokio, reqwest

// use reqwest;
// 
// #[tokio::main]
// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let response = reqwest::get("https://www.rust-lang.org").await?;
//     println!("Status: {}", response.status());
//     Ok(())
// }
```

### 5.2 Пример: Параллельная обработка

```rust
use tokio::time::{sleep, Duration};

async fn process_item(item: i32) {
    sleep(Duration::from_millis(100)).await;
    println!("Обработан элемент: {}", item);
}

#[tokio::main]
async fn main() {
    let items = vec![1, 2, 3, 4, 5];
    
    for item in items {
        tokio::spawn(process_item(item));
    }
    
    sleep(Duration::from_secs(1)).await;
}
```

**Output:**
```
Обработан элемент: 1
Обработан элемент: 2
Обработан элемент: 3
Обработан элемент: 4
Обработан элемент: 5
```

### 5.3 Пример: Асинхронный сервер

```rust
// Требует: tokio = { version = "1", features = ["full"] }
// use tokio::io::{AsyncReadExt, AsyncWriteExt};
// use tokio::net::TcpListener;

// #[tokio::main]
// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let listener = TcpListener::bind("127.0.0.1:8080").await?;
//     
//     loop {
//         let (mut socket, _) = listener.accept().await?;
//         
//         tokio::spawn(async move {
//             let mut buf = [0; 1024];
//             
//             match socket.read(&mut buf).await {
//                 Ok(n) => {
//                     if n == 0 {
//                         return;
//                     }
//                     socket.write_all(b"HTTP/1.1 200 OK\r\n\r\nHello").await.unwrap();
//                 }
//                 Err(e) => {
//                     eprintln!("Ошибка чтения: {}", e);
//                 }
//             }
//         });
//     }
// }
```

### 5.4 Пример: Таймауты

```rust
use tokio::time::{sleep, Duration, timeout};

async fn slow_task() -> &'static str {
    sleep(Duration::from_secs(2)).await;
    "Готово"
}

#[tokio::main]
async fn main() {
    match timeout(Duration::from_secs(1), slow_task()).await {
        Ok(result) => println!("{}", result),
        Err(_) => println!("Таймаут!"),
    }
}
```

**Output:**
```
Таймаут!
```

### 5.5 Пример: Семафор для ограничения конкурентности

```rust
// Требует: tokio = { version = "1", features = ["full"] }
// use tokio::sync::Semaphore;
// use tokio::time::{sleep, Duration};

// async fn task(id: u32, semaphore: Arc<Semaphore>) {
//     let permit = semaphore.acquire().await.unwrap();
//     println!("Задача {} начала выполнение", id);
//     sleep(Duration::from_millis(100)).await;
//     println!("Задача {} завершена", id);
//     drop(permit);
// }

// #[tokio::main]
// async fn main() {
//     let semaphore = Arc::new(Semaphore::new(3));
//     let mut handles = vec![];
//     
//     for i in 1..=10 {
//         let sem = Arc::clone(&semaphore);
//         handles.push(tokio::spawn(task(i, sem)));
//     }
//     
//     for handle in handles {
//         handle.await.unwrap();
//     }
// }
```

---

## 💡 Key Takeaways

- **Threads для параллелизма:** Создание потоков для параллельного выполнения

- **async/await для асинхронности:** Современный способ написания асинхронного кода

- **Futures представляют будущие значения:** Вычисляются через runtime

- **tokio — популярный runtime:** Для выполнения асинхронного кода

- **Параллельность vs асинхронность:** Разные подходы к конкурентности

---

## 🚀 Next Steps

**Related Modules:**

- [Экосистема](../14_Ecosystem/) — популярные библиотеки и crates
- [Практические применения](../15_Practical_Applications/) — реальные примеры

**Practice Ideas:**

1. Создайте программу с несколькими потоками
2. Попробуйте async/await с tokio
3. Реализуйте параллельную обработку данных
4. Изучите каналы для обмена данными между потоками

**Going Deeper:**

- Изучите каналы (channels) для коммуникации между потоками
- Почитайте о Mutex и Arc для разделяемого состояния
- Изучите различные async runtimes (tokio, async-std)

---

## 📚 Additional Resources

**Documentation:**

- [Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) — документация по конкурентности
- [Async Book](https://rust-lang.github.io/async-book/) — книга по асинхронности

**Libraries:**

- [tokio](https://tokio.rs/) — асинхронный runtime
- [async-std](https://async.rs/) — альтернативный runtime

---


