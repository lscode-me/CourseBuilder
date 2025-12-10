# Concurrency
## Горутины, каналы, select и sync примитивы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать функции и замыкания
- Знать обработку ошибок
- Иметь базовое понимание параллельного выполнения

**Recommended prior modules:**
- [04_Functions](../04_Functions/) — функции и замыкания
- [08_Errors](../08_Errors/) — обработка ошибок

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять горутинами
- Использовать каналы для коммуникации
- Применять select для работы с несколькими каналами
- Использовать sync примитивы (Mutex, WaitGroup)
- Понимать паттерны конкурентного программирования

---

## 1. Горутины (Goroutines)

### 1.1 Запуск горутины

Горутина — легковесный поток, управляемый Go runtime:

```go
package main

import (
    "fmt"
    "time"
)

func sayHello(name string) {
    for i := 0; i < 3; i++ {
        fmt.Printf("Hello, %s! (%d)\n", name, i)
        time.Sleep(100 * time.Millisecond)
    }
}

func main() {
    // Запуск горутины с ключевым словом go
    go sayHello("Goroutine")
    
    // Основная горутина продолжает выполнение
    sayHello("Main")
    
    // Даём время горутине завершиться
    time.Sleep(500 * time.Millisecond)
}
```

**Output:**
```
Hello, Main! (0)
Hello, Goroutine! (0)
Hello, Main! (1)
Hello, Goroutine! (1)
Hello, Main! (2)
Hello, Goroutine! (2)
```

### 1.2 Анонимные горутины

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    // Анонимная горутина
    go func() {
        fmt.Println("Anonymous goroutine")
    }()
    
    // С параметром
    message := "Hello from closure"
    go func(msg string) {
        fmt.Println(msg)
    }(message)
    
    time.Sleep(100 * time.Millisecond)
}
```

**Output:**
```
Anonymous goroutine
Hello from closure
```

### 1.3 Количество горутин

```go
package main

import (
    "fmt"
    "runtime"
    "time"
)

func main() {
    fmt.Println("CPUs:", runtime.NumCPU())
    fmt.Println("Goroutines at start:", runtime.NumGoroutine())
    
    for i := 0; i < 10; i++ {
        go func(n int) {
            time.Sleep(time.Second)
        }(i)
    }
    
    fmt.Println("Goroutines after launch:", runtime.NumGoroutine())
    time.Sleep(2 * time.Second)
    fmt.Println("Goroutines after sleep:", runtime.NumGoroutine())
}
```

**Output:**
```
CPUs: 8
Goroutines at start: 1
Goroutines after launch: 11
Goroutines after sleep: 1
```

---

## 2. Каналы (Channels)

### 2.1 Создание и использование

```go
package main

import "fmt"

func main() {
    // Создание канала
    ch := make(chan string)
    
    // Отправка в горутине
    go func() {
        ch <- "Hello, Channel!"
    }()
    
    // Получение из канала (блокирующее)
    message := <-ch
    fmt.Println(message)
}
```

**Output:**
```
Hello, Channel!
```

### 2.2 Буферизованные каналы

```go
package main

import "fmt"

func main() {
    // Небуферизованный канал — синхронный
    unbuffered := make(chan int)
    
    // Буферизованный канал — асинхронный до заполнения
    buffered := make(chan int, 3)
    
    // Можно отправить без получателя (до заполнения буфера)
    buffered <- 1
    buffered <- 2
    buffered <- 3
    // buffered <- 4  // Заблокируется — буфер полон
    
    fmt.Println("Buffered length:", len(buffered))
    fmt.Println("Buffered capacity:", cap(buffered))
    
    fmt.Println(<-buffered)
    fmt.Println(<-buffered)
    fmt.Println(<-buffered)
    
    _ = unbuffered  // Для компиляции
}
```

**Output:**
```
Buffered length: 3
Buffered capacity: 3
1
2
3
```

### 2.3 Закрытие канала

```go
package main

import "fmt"

func producer(ch chan<- int) {
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)  // Закрываем канал
}

func main() {
    ch := make(chan int)
    
    go producer(ch)
    
    // Чтение до закрытия
    for value := range ch {
        fmt.Println("Received:", value)
    }
    
    fmt.Println("Channel closed")
    
    // Проверка закрытия
    ch2 := make(chan int)
    close(ch2)
    
    value, ok := <-ch2
    fmt.Printf("value: %d, ok: %t\n", value, ok)
}
```

**Output:**
```
Received: 0
Received: 1
Received: 2
Received: 3
Received: 4
Channel closed
value: 0, ok: false
```

### 2.4 Направление канала

```go
package main

import "fmt"

// Только для отправки
func sender(ch chan<- int) {
    ch <- 42
}

// Только для получения
func receiver(ch <-chan int) {
    fmt.Println("Received:", <-ch)
}

func main() {
    ch := make(chan int)
    
    go sender(ch)
    receiver(ch)
}
```

**Output:**
```
Received: 42
```

---

## 3. Select

### 3.1 Множественные каналы

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    ch1 := make(chan string)
    ch2 := make(chan string)
    
    go func() {
        time.Sleep(100 * time.Millisecond)
        ch1 <- "from ch1"
    }()
    
    go func() {
        time.Sleep(50 * time.Millisecond)
        ch2 <- "from ch2"
    }()
    
    // select выбирает первый готовый канал
    for i := 0; i < 2; i++ {
        select {
        case msg1 := <-ch1:
            fmt.Println("Received", msg1)
        case msg2 := <-ch2:
            fmt.Println("Received", msg2)
        }
    }
}
```

**Output:**
```
Received from ch2
Received from ch1
```

### 3.2 Timeout

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    ch := make(chan string)
    
    go func() {
        time.Sleep(2 * time.Second)
        ch <- "result"
    }()
    
    select {
    case result := <-ch:
        fmt.Println("Got:", result)
    case <-time.After(1 * time.Second):
        fmt.Println("Timeout!")
    }
}
```

**Output:**
```
Timeout!
```

### 3.3 Non-blocking select с default

```go
package main

import "fmt"

func main() {
    ch := make(chan int)
    
    // Non-blocking receive
    select {
    case value := <-ch:
        fmt.Println("Received:", value)
    default:
        fmt.Println("No value ready")
    }
    
    // Non-blocking send
    select {
    case ch <- 42:
        fmt.Println("Sent")
    default:
        fmt.Println("Cannot send")
    }
}
```

**Output:**
```
No value ready
Cannot send
```

---

## 4. sync Package

### 4.1 WaitGroup

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func worker(id int, wg *sync.WaitGroup) {
    defer wg.Done()  // Уменьшает счётчик при завершении
    
    fmt.Printf("Worker %d starting\n", id)
    time.Sleep(100 * time.Millisecond)
    fmt.Printf("Worker %d done\n", id)
}

func main() {
    var wg sync.WaitGroup
    
    for i := 1; i <= 3; i++ {
        wg.Add(1)  // Увеличиваем счётчик
        go worker(i, &wg)
    }
    
    wg.Wait()  // Блокируется до счётчика = 0
    fmt.Println("All workers done")
}
```

**Output:**
```
Worker 1 starting
Worker 2 starting
Worker 3 starting
Worker 2 done
Worker 1 done
Worker 3 done
All workers done
```

### 4.2 Mutex

```go
package main

import (
    "fmt"
    "sync"
)

type SafeCounter struct {
    mu    sync.Mutex
    value int
}

func (c *SafeCounter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.value++
}

func (c *SafeCounter) Value() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.value
}

func main() {
    counter := SafeCounter{}
    var wg sync.WaitGroup
    
    for i := 0; i < 1000; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            counter.Increment()
        }()
    }
    
    wg.Wait()
    fmt.Println("Counter:", counter.Value())
}
```

**Output:**
```
Counter: 1000
```

### 4.3 RWMutex

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

type Cache struct {
    mu   sync.RWMutex
    data map[string]string
}

func (c *Cache) Get(key string) (string, bool) {
    c.mu.RLock()  // Множественные читатели
    defer c.mu.RUnlock()
    value, ok := c.data[key]
    return value, ok
}

func (c *Cache) Set(key, value string) {
    c.mu.Lock()  // Эксклюзивный писатель
    defer c.mu.Unlock()
    c.data[key] = value
}

func main() {
    cache := Cache{data: make(map[string]string)}
    
    cache.Set("hello", "world")
    
    var wg sync.WaitGroup
    
    // Много параллельных читателей
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            value, _ := cache.Get("hello")
            fmt.Printf("Reader %d: %s\n", id, value)
        }(i)
    }
    
    wg.Wait()
}
```

**Output:**
```
Reader 0: world
Reader 1: world
Reader 2: world
Reader 3: world
Reader 4: world
```

### 4.4 Once

```go
package main

import (
    "fmt"
    "sync"
)

var once sync.Once
var config string

func loadConfig() {
    fmt.Println("Loading config...")
    config = "loaded"
}

func getConfig() string {
    once.Do(loadConfig)  // Выполнится только один раз
    return config
}

func main() {
    var wg sync.WaitGroup
    
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            fmt.Println("Config:", getConfig())
        }()
    }
    
    wg.Wait()
}
```

**Output:**
```
Loading config...
Config: loaded
Config: loaded
Config: loaded
Config: loaded
Config: loaded
```

---

## 5. Паттерны конкурентности

### 5.1 Worker Pool

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    
    for job := range jobs {
        fmt.Printf("Worker %d processing job %d\n", id, job)
        time.Sleep(50 * time.Millisecond)
        results <- job * 2
    }
}

func main() {
    jobs := make(chan int, 10)
    results := make(chan int, 10)
    var wg sync.WaitGroup
    
    // Запускаем 3 воркера
    for w := 1; w <= 3; w++ {
        wg.Add(1)
        go worker(w, jobs, results, &wg)
    }
    
    // Отправляем задачи
    for j := 1; j <= 5; j++ {
        jobs <- j
    }
    close(jobs)
    
    // Ждём завершения воркеров
    go func() {
        wg.Wait()
        close(results)
    }()
    
    // Собираем результаты
    for result := range results {
        fmt.Println("Result:", result)
    }
}
```

**Output:**
```
Worker 1 processing job 1
Worker 2 processing job 2
Worker 3 processing job 3
Worker 1 processing job 4
Worker 2 processing job 5
Result: 2
Result: 4
Result: 6
Result: 8
Result: 10
```

### 5.2 Fan-out / Fan-in

```go
package main

import (
    "fmt"
    "sync"
)

func generator(nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        for _, n := range nums {
            out <- n
        }
        close(out)
    }()
    return out
}

func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        for n := range in {
            out <- n * n
        }
        close(out)
    }()
    return out
}

func merge(cs ...<-chan int) <-chan int {
    var wg sync.WaitGroup
    out := make(chan int)
    
    output := func(c <-chan int) {
        defer wg.Done()
        for n := range c {
            out <- n
        }
    }
    
    wg.Add(len(cs))
    for _, c := range cs {
        go output(c)
    }
    
    go func() {
        wg.Wait()
        close(out)
    }()
    
    return out
}

func main() {
    in := generator(1, 2, 3, 4, 5)
    
    // Fan-out: несколько воркеров читают из одного канала
    c1 := square(in)
    c2 := square(in)
    
    // Fan-in: объединяем результаты
    for result := range merge(c1, c2) {
        fmt.Println(result)
    }
}
```

---

## 6. Context

### 6.1 Отмена операций

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func worker(ctx context.Context, id int) {
    for {
        select {
        case <-ctx.Done():
            fmt.Printf("Worker %d: cancelled\n", id)
            return
        default:
            fmt.Printf("Worker %d: working...\n", id)
            time.Sleep(100 * time.Millisecond)
        }
    }
}

func main() {
    ctx, cancel := context.WithCancel(context.Background())
    
    go worker(ctx, 1)
    go worker(ctx, 2)
    
    time.Sleep(300 * time.Millisecond)
    
    cancel()  // Отменяем все операции
    time.Sleep(100 * time.Millisecond)
    fmt.Println("Done")
}
```

**Output:**
```
Worker 1: working...
Worker 2: working...
Worker 1: working...
Worker 2: working...
Worker 2: working...
Worker 1: working...
Worker 1: cancelled
Worker 2: cancelled
Done
```

### 6.2 Timeout с context

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func slowOperation(ctx context.Context) error {
    select {
    case <-time.After(2 * time.Second):
        return nil
    case <-ctx.Done():
        return ctx.Err()
    }
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
    defer cancel()
    
    err := slowOperation(ctx)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Success")
    }
}
```

**Output:**
```
Error: context deadline exceeded
```

---

## 7. Common Pitfalls

### 7.1 Race condition

```go
// ПЛОХО — race condition
var counter int
for i := 0; i < 1000; i++ {
    go func() { counter++ }()
}

// ХОРОШО — с Mutex
var mu sync.Mutex
var counter int
for i := 0; i < 1000; i++ {
    go func() {
        mu.Lock()
        counter++
        mu.Unlock()
    }()
}
```

### 7.2 Забытый close

```go
// ПЛОХО — утечка горутины
ch := make(chan int)
go func() {
    for v := range ch {  // Никогда не завершится
        fmt.Println(v)
    }
}()
// ch никогда не закрывается

// ХОРОШО — закрываем канал
ch := make(chan int)
go func() {
    for v := range ch {
        fmt.Println(v)
    }
}()
close(ch)  // Горутина завершится
```

---

## 💡 Key Takeaways

- **go keyword**: Запускает горутину — легковесный поток.

- **Каналы для коммуникации**: "Don't communicate by sharing memory; share memory by communicating".

- **select**: Для работы с несколькими каналами и timeout.

- **sync.WaitGroup**: Для ожидания завершения горутин.

- **sync.Mutex**: Для защиты shared state.

---

## 🚀 Next Steps

**Related Modules:**
- [10_Packages](../10_Packages/) — организация кода
- [11_Testing](../11_Testing/) — тестирование concurrent кода

**Practice Ideas:**
1. Реализуйте worker pool
2. Создайте rate limiter с каналами
3. Напишите concurrent web scraper

---

