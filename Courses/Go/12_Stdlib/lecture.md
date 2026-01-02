# Standard Library
## net/http, encoding/json, io, os

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать функции и интерфейсы
- Знать обработку ошибок
- Уметь работать со структурами

**Recommended prior modules:**

- [07_Methods](../07_Methods/) — интерфейсы
- [08_Errors](../08_Errors/) — обработка ошибок

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать HTTP серверы и клиенты
- Работать с JSON
- Использовать io.Reader и io.Writer
- Работать с файловой системой
- Применять стандартные пакеты

---

## 1. net/http

### 1.1 HTTP сервер

```go
package main

import (
    "fmt"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", helloHandler)
    
    fmt.Println("Server starting on :8080")
    http.ListenAndServe(":8080", nil)
}
```

### 1.2 ServeMux

```go
package main

import (
    "encoding/json"
    "net/http"
)

func main() {
    mux := http.NewServeMux()
    
    mux.HandleFunc("/api/users", func(w http.ResponseWriter, r *http.Request) {
        switch r.Method {
        case http.MethodGet:
            json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
        case http.MethodPost:
            w.WriteHeader(http.StatusCreated)
        default:
            w.WriteHeader(http.StatusMethodNotAllowed)
        }
    })
    
    mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("healthy"))
    })
    
    http.ListenAndServe(":8080", mux)
}
```

### 1.3 HTTP клиент

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "time"
)

func main() {
    // Простой GET запрос
    resp, err := http.Get("https://api.github.com")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer resp.Body.Close()
    
    body, _ := io.ReadAll(resp.Body)
    fmt.Println("Status:", resp.Status)
    fmt.Println("Body:", string(body[:100])+"...")
}
```

### 1.4 Кастомный клиент

```go
package main

import (
    "bytes"
    "encoding/json"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{
        Timeout: 10 * time.Second,
    }
    
    // POST запрос с JSON
    data := map[string]string{"name": "Go"}
    jsonData, _ := json.Marshal(data)
    
    req, _ := http.NewRequest(
        http.MethodPost,
        "https://httpbin.org/post",
        bytes.NewBuffer(jsonData),
    )
    
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("Authorization", "Bearer token")
    
    resp, err := client.Do(req)
    if err != nil {
        return
    }
    defer resp.Body.Close()
}
```

### 1.5 Middleware

```go
package main

import (
    "log"
    "net/http"
    "time"
)

func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        
        next.ServeHTTP(w, r)
        
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}

func main() {
    mux := http.NewServeMux()
    
    mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello!"))
    })
    
    handler := loggingMiddleware(mux)
    http.ListenAndServe(":8080", handler)
}
```

---

## 2. encoding/json

### 2.1 Маршалинг

```go
package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    ID        int    `json:"id"`
    Name      string `json:"name"`
    Email     string `json:"email,omitempty"`
    Password  string `json:"-"`  // Игнорируется
    CreatedAt string `json:"created_at"`
}

func main() {
    user := User{
        ID:       1,
        Name:     "Alice",
        Password: "secret",
    }
    
    // Компактный JSON
    data, _ := json.Marshal(user)
    fmt.Println(string(data))
    
    // Pretty JSON
    prettyData, _ := json.MarshalIndent(user, "", "  ")
    fmt.Println(string(prettyData))
}
```

**Output:**
```json
{"id":1,"name":"Alice","created_at":""}
{
  "id": 1,
  "name": "Alice",
  "created_at": ""
}
```

### 2.2 Анмаршалинг

```go
package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

func main() {
    jsonData := `{"id": 1, "name": "Alice", "email": "alice@example.com"}`
    
    var user User
    err := json.Unmarshal([]byte(jsonData), &user)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    fmt.Printf("%+v\n", user)
}
```

**Output:**
```
{ID:1 Name:Alice Email:alice@example.com}
```

### 2.3 Работа с динамическим JSON

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    jsonData := `{
        "name": "Go",
        "year": 2009,
        "features": ["fast", "simple", "concurrent"]
    }`
    
    // Используем map[string]interface{}
    var data map[string]interface{}
    json.Unmarshal([]byte(jsonData), &data)
    
    fmt.Println("Name:", data["name"])
    fmt.Println("Year:", data["year"])
    
    // Type assertion для вложенных типов
    features := data["features"].([]interface{})
    for _, f := range features {
        fmt.Println("Feature:", f.(string))
    }
}
```

**Output:**
```
Name: Go
Year: 2009
Feature: fast
Feature: simple
Feature: concurrent
```

### 2.4 Streaming JSON

```go
package main

import (
    "encoding/json"
    "os"
)

type LogEntry struct {
    Time    string `json:"time"`
    Level   string `json:"level"`
    Message string `json:"message"`
}

func main() {
    // Encoder пишет напрямую в Writer
    encoder := json.NewEncoder(os.Stdout)
    encoder.SetIndent("", "  ")
    
    entry := LogEntry{
        Time:    "2024-01-01",
        Level:   "INFO",
        Message: "Application started",
    }
    
    encoder.Encode(entry)
}
```

---

## 3. io

### 3.1 io.Reader и io.Writer

```go
// Основные интерфейсы
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}
```

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    // strings.Reader реализует io.Reader
    reader := strings.NewReader("Hello, World!")
    
    buf := make([]byte, 5)
    for {
        n, err := reader.Read(buf)
        if err == io.EOF {
            break
        }
        fmt.Printf("Read %d bytes: %s\n", n, buf[:n])
    }
}
```

**Output:**
```
Read 5 bytes: Hello
Read 5 bytes: , Wor
Read 3 bytes: ld!
```

### 3.2 io.Copy

```go
package main

import (
    "io"
    "os"
    "strings"
)

func main() {
    reader := strings.NewReader("Hello, io.Copy!")
    
    // Копирование из Reader в Writer
    n, err := io.Copy(os.Stdout, reader)
    if err != nil {
        return
    }
    
    println() // Новая строка
    println("Copied", n, "bytes")
}
```

**Output:**
```
Hello, io.Copy!
Copied 15 bytes
```

### 3.3 io.ReadAll

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    reader := strings.NewReader("Read all at once")
    
    data, err := io.ReadAll(reader)
    if err != nil {
        return
    }
    
    fmt.Println(string(data))
}
```

### 3.4 io.MultiReader и io.MultiWriter

```go
package main

import (
    "io"
    "os"
    "strings"
)

func main() {
    // MultiReader объединяет несколько readers
    r1 := strings.NewReader("Hello, ")
    r2 := strings.NewReader("World!")
    
    multi := io.MultiReader(r1, r2)
    io.Copy(os.Stdout, multi)
    println()
    
    // MultiWriter пишет во все writers
    var buf strings.Builder
    multi2 := io.MultiWriter(os.Stdout, &buf)
    multi2.Write([]byte("Written to both"))
    println()
    println("Buffer:", buf.String())
}
```

**Output:**
```
Hello, World!
Written to both
Buffer: Written to both
```

---

## 4. os

### 4.1 Работа с файлами

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Создание и запись
    file, err := os.Create("test.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    file.WriteString("Hello, File!")
    file.Close()
    
    // Чтение
    data, _ := os.ReadFile("test.txt")
    fmt.Println("Content:", string(data))
    
    // Информация о файле
    info, _ := os.Stat("test.txt")
    fmt.Printf("Name: %s, Size: %d, Mode: %s\n",
        info.Name(), info.Size(), info.Mode())
    
    // Удаление
    os.Remove("test.txt")
}
```

**Output:**
```
Content: Hello, File!
Name: test.txt, Size: 12, Mode: -rw-r--r--
```

### 4.2 Директории

```go
package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    // Создание директории
    os.Mkdir("mydir", 0755)
    os.MkdirAll("mydir/subdir/deep", 0755)
    
    // Чтение директории
    entries, _ := os.ReadDir("mydir")
    for _, e := range entries {
        fmt.Println(e.Name(), e.IsDir())
    }
    
    // Обход директорий
    filepath.Walk("mydir", func(path string, info os.FileInfo, err error) error {
        fmt.Println("Found:", path)
        return nil
    })
    
    // Очистка
    os.RemoveAll("mydir")
}
```

### 4.3 Переменные окружения

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Получение
    path := os.Getenv("PATH")
    fmt.Println("PATH:", path[:50]+"...")
    
    // Установка
    os.Setenv("MY_VAR", "my_value")
    fmt.Println("MY_VAR:", os.Getenv("MY_VAR"))
    
    // С значением по умолчанию
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }
    fmt.Println("PORT:", port)
    
    // LookupEnv — проверка существования
    value, exists := os.LookupEnv("UNDEFINED")
    fmt.Printf("UNDEFINED: value=%q, exists=%t\n", value, exists)
}
```

### 4.4 Аргументы командной строки

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // os.Args[0] — имя программы
    fmt.Println("Program:", os.Args[0])
    
    // Остальные аргументы
    if len(os.Args) > 1 {
        fmt.Println("Arguments:", os.Args[1:])
    }
}
```

---

## 5. Другие полезные пакеты

### 5.1 strings

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    s := "Hello, World!"
    
    fmt.Println(strings.Contains(s, "World"))    // true
    fmt.Println(strings.HasPrefix(s, "Hello"))   // true
    fmt.Println(strings.HasSuffix(s, "!"))       // true
    fmt.Println(strings.ToUpper(s))              // HELLO, WORLD!
    fmt.Println(strings.ToLower(s))              // hello, world!
    fmt.Println(strings.Replace(s, "World", "Go", 1))
    fmt.Println(strings.Split(s, ", "))          // [Hello World!]
    fmt.Println(strings.TrimSpace("  hello  "))  // hello
    
    // Builder для эффективной конкатенации
    var sb strings.Builder
    sb.WriteString("Hello")
    sb.WriteString(", ")
    sb.WriteString("World!")
    fmt.Println(sb.String())
}
```

### 5.2 time

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    // Текущее время
    now := time.Now()
    fmt.Println("Now:", now)
    
    // Форматирование (используется референсное время!)
    fmt.Println("Formatted:", now.Format("2006-01-02 15:04:05"))
    
    // Парсинг
    t, _ := time.Parse("2006-01-02", "2024-01-15")
    fmt.Println("Parsed:", t)
    
    // Вычисления
    tomorrow := now.Add(24 * time.Hour)
    fmt.Println("Tomorrow:", tomorrow)
    
    // Duration
    start := time.Now()
    time.Sleep(100 * time.Millisecond)
    elapsed := time.Since(start)
    fmt.Println("Elapsed:", elapsed)
}
```

### 5.3 fmt

```go
package main

import (
    "fmt"
)

func main() {
    // Форматирование
    name := "Go"
    version := 1.22
    
    // Printf
    fmt.Printf("Language: %s, Version: %.2f\n", name, version)
    
    // Sprintf — возвращает строку
    s := fmt.Sprintf("Language: %s", name)
    fmt.Println(s)
    
    // Errorf — создаёт ошибку
    err := fmt.Errorf("error: %s not found", name)
    fmt.Println(err)
    
    // Scanf — ввод
    var input string
    fmt.Print("Enter name: ")
    // fmt.Scanf("%s", &input)
    _ = input
}
```

### 5.4 log

```go
package main

import (
    "log"
    "os"
)

func main() {
    // Простое логирование
    log.Println("Info message")
    
    // С форматированием
    log.Printf("Value: %d", 42)
    
    // Настройка логгера
    logger := log.New(os.Stdout, "[APP] ", log.Ldate|log.Ltime|log.Lshortfile)
    logger.Println("Custom logger")
    
    // Fatal — логирует и вызывает os.Exit(1)
    // log.Fatal("Critical error")
    
    // Panic — логирует и вызывает panic
    // log.Panic("Panic!")
}
```

**Output:**
```
2024/01/15 10:30:45 Info message
2024/01/15 10:30:45 Value: 42
[APP] 2024/01/15 10:30:45 main.go:16: Custom logger
```

---

## 6. Практические примеры

### 6.1 REST API сервер

```go
package main

import (
    "encoding/json"
    "net/http"
)

type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

var users = []User{
    {ID: 1, Name: "Alice"},
    {ID: 2, Name: "Bob"},
}

func main() {
    http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(users)
    })
    
    http.ListenAndServe(":8080", nil)
}
```

### 6.2 Чтение конфигурации

```go
package main

import (
    "encoding/json"
    "fmt"
    "os"
)

type Config struct {
    Host     string `json:"host"`
    Port     int    `json:"port"`
    Database string `json:"database"`
}

func LoadConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, err
    }
    
    var config Config
    if err := json.Unmarshal(data, &config); err != nil {
        return nil, err
    }
    
    return &config, nil
}

func main() {
    config, err := LoadConfig("config.json")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    fmt.Printf("%+v\n", config)
}
```

---

## 💡 Key Takeaways

- **net/http**: Встроенный HTTP сервер и клиент, достаточные для продакшена.

- **encoding/json**: Маршалинг/анмаршалинг с тегами структур.

- **io.Reader/Writer**: Универсальные интерфейсы для потоков данных.

- **os**: Работа с файлами, переменными окружения, аргументами.

- **Стандартная библиотека**: Мощная и достаточная для большинства задач.

---

## 🚀 Next Steps

**Practice Ideas:**

1. Создайте REST API с CRUD операциями
2. Напишите CLI утилиту с обработкой аргументов
3. Реализуйте загрузчик файлов с progress bar

**Going Deeper:**

- Изучите context для timeout и cancellation
- Посмотрите net/http/httptest для тестирования
- Изучите database/sql для работы с БД

---




