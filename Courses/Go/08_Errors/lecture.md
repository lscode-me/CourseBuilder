# Error Handling
## Обработка ошибок, error interface, sentinel errors и wrapping

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать интерфейсы в Go
- Знать множественные возвращаемые значения
- Уметь работать с функциями и методами

**Recommended prior modules:**
- [04_Functions](../04_Functions/) — функции
- [07_Methods](../07_Methods/) — интерфейсы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать философию обработки ошибок в Go
- Создавать и возвращать ошибки
- Использовать sentinel errors и custom error types
- Применять error wrapping (Go 1.13+)
- Обрабатывать ошибки идиоматично

---

## 1. Философия ошибок в Go

### 1.1 Ошибки — это значения

В Go нет исключений. Ошибки — обычные значения:

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Открытие файла возвращает (file, error)
    file, err := os.Open("nonexistent.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer file.Close()
    
    fmt.Println("File opened:", file.Name())
}
```

**Output:**
```
Error: open nonexistent.txt: no such file or directory
```

### 1.2 Интерфейс error

```go
// Встроенный интерфейс error
type error interface {
    Error() string
}
```

Любой тип с методом `Error() string` реализует error:

```go
package main

import "fmt"

type MyError struct {
    Code    int
    Message string
}

func (e MyError) Error() string {
    return fmt.Sprintf("error %d: %s", e.Code, e.Message)
}

func doSomething() error {
    return MyError{Code: 404, Message: "not found"}
}

func main() {
    err := doSomething()
    if err != nil {
        fmt.Println(err)
    }
}
```

**Output:**
```
error 404: not found
```

---

## 2. Создание ошибок

### 2.1 errors.New

```go
package main

import (
    "errors"
    "fmt"
)

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println("Result:", result)
}
```

**Output:**
```
Error: division by zero
```

### 2.2 fmt.Errorf

```go
package main

import (
    "fmt"
)

func validateAge(age int) error {
    if age < 0 {
        return fmt.Errorf("invalid age: %d (must be non-negative)", age)
    }
    if age > 150 {
        return fmt.Errorf("invalid age: %d (too large)", age)
    }
    return nil
}

func main() {
    ages := []int{25, -5, 200}
    
    for _, age := range ages {
        if err := validateAge(age); err != nil {
            fmt.Println("Error:", err)
        } else {
            fmt.Printf("Age %d is valid\n", age)
        }
    }
}
```

**Output:**
```
Age 25 is valid
Error: invalid age: -5 (must be non-negative)
Error: invalid age: 200 (too large)
```

### 2.3 Custom Error Types

```go
package main

import "fmt"

type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation error in %s: %s", e.Field, e.Message)
}

type NotFoundError struct {
    Resource string
    ID       int
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s with ID %d not found", e.Resource, e.ID)
}

func findUser(id int) error {
    if id <= 0 {
        return &ValidationError{Field: "id", Message: "must be positive"}
    }
    if id > 100 {
        return &NotFoundError{Resource: "User", ID: id}
    }
    return nil
}

func main() {
    ids := []int{-1, 50, 101}
    
    for _, id := range ids {
        err := findUser(id)
        if err != nil {
            fmt.Printf("Error for ID %d: %v\n", id, err)
        } else {
            fmt.Printf("User %d found\n", id)
        }
    }
}
```

**Output:**
```
Error for ID -1: validation error in id: must be positive
User 50 found
Error for ID 101: User with ID 101 not found
```

---

## 3. Sentinel Errors

### 3.1 Определение sentinel errors

Sentinel errors — предопределённые ошибки для сравнения:

```go
package main

import (
    "errors"
    "fmt"
)

// Sentinel errors
var (
    ErrNotFound     = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
    ErrInvalidInput = errors.New("invalid input")
)

func getUser(id int) (string, error) {
    if id <= 0 {
        return "", ErrInvalidInput
    }
    if id == 999 {
        return "", ErrUnauthorized
    }
    if id > 100 {
        return "", ErrNotFound
    }
    return fmt.Sprintf("User-%d", id), nil
}

func main() {
    ids := []int{-1, 50, 101, 999}
    
    for _, id := range ids {
        user, err := getUser(id)
        
        switch {
        case errors.Is(err, ErrNotFound):
            fmt.Printf("ID %d: User not found\n", id)
        case errors.Is(err, ErrUnauthorized):
            fmt.Printf("ID %d: Access denied\n", id)
        case errors.Is(err, ErrInvalidInput):
            fmt.Printf("ID %d: Invalid ID\n", id)
        case err != nil:
            fmt.Printf("ID %d: Unknown error: %v\n", id, err)
        default:
            fmt.Printf("ID %d: Found %s\n", id, user)
        }
    }
}
```

**Output:**
```
ID -1: Invalid ID
ID 50: Found User-50
ID 101: User not found
ID 999: Access denied
```

### 3.2 io.EOF — пример sentinel error

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    r := strings.NewReader("Hello")
    buf := make([]byte, 2)
    
    for {
        n, err := r.Read(buf)
        
        if err == io.EOF {
            fmt.Println("End of data")
            break
        }
        if err != nil {
            fmt.Println("Error:", err)
            break
        }
        
        fmt.Printf("Read: %q\n", buf[:n])
    }
}
```

**Output:**
```
Read: "He"
Read: "ll"
Read: "o"
End of data
```

---

## 4. Error Wrapping (Go 1.13+)

### 4.1 fmt.Errorf с %w

```go
package main

import (
    "errors"
    "fmt"
    "os"
)

func readConfig(path string) ([]byte, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        // Оборачиваем ошибку с контекстом
        return nil, fmt.Errorf("reading config %s: %w", path, err)
    }
    return data, nil
}

func loadSettings() error {
    _, err := readConfig("config.yaml")
    if err != nil {
        return fmt.Errorf("loading settings: %w", err)
    }
    return nil
}

func main() {
    err := loadSettings()
    if err != nil {
        fmt.Println("Error:", err)
        
        // Проверяем, является ли причиной os.ErrNotExist
        if errors.Is(err, os.ErrNotExist) {
            fmt.Println("Config file does not exist")
        }
    }
}
```

**Output:**
```
Error: loading settings: reading config config.yaml: open config.yaml: no such file or directory
Config file does not exist
```

### 4.2 errors.Is

`errors.Is` проверяет цепочку ошибок:

```go
package main

import (
    "errors"
    "fmt"
)

var ErrPermission = errors.New("permission denied")

func layer3() error {
    return ErrPermission
}

func layer2() error {
    err := layer3()
    return fmt.Errorf("layer2: %w", err)
}

func layer1() error {
    err := layer2()
    return fmt.Errorf("layer1: %w", err)
}

func main() {
    err := layer1()
    
    fmt.Println("Error:", err)
    fmt.Println("Is ErrPermission:", errors.Is(err, ErrPermission))
}
```

**Output:**
```
Error: layer1: layer2: permission denied
Is ErrPermission: true
```

### 4.3 errors.As

`errors.As` находит ошибку определённого типа в цепочке:

```go
package main

import (
    "errors"
    "fmt"
)

type HTTPError struct {
    StatusCode int
    Message    string
}

func (e *HTTPError) Error() string {
    return fmt.Sprintf("HTTP %d: %s", e.StatusCode, e.Message)
}

func apiCall() error {
    return &HTTPError{StatusCode: 404, Message: "Not Found"}
}

func fetchData() error {
    err := apiCall()
    return fmt.Errorf("fetching data: %w", err)
}

func main() {
    err := fetchData()
    
    var httpErr *HTTPError
    if errors.As(err, &httpErr) {
        fmt.Printf("HTTP Error: status=%d, message=%s\n", 
            httpErr.StatusCode, httpErr.Message)
    }
    
    fmt.Println("Full error:", err)
}
```

**Output:**
```
HTTP Error: status=404, message=Not Found
Full error: fetching data: HTTP 404: Not Found
```

### 4.4 errors.Unwrap

```go
package main

import (
    "errors"
    "fmt"
)

func main() {
    original := errors.New("original error")
    wrapped := fmt.Errorf("wrapped: %w", original)
    doubleWrapped := fmt.Errorf("double wrapped: %w", wrapped)
    
    fmt.Println("Double wrapped:", doubleWrapped)
    fmt.Println("Unwrap once:", errors.Unwrap(doubleWrapped))
    fmt.Println("Unwrap twice:", errors.Unwrap(errors.Unwrap(doubleWrapped)))
}
```

**Output:**
```
Double wrapped: double wrapped: wrapped: original error
Unwrap once: wrapped: original error
Unwrap twice: original error
```

---

## 5. Паттерны обработки ошибок

### 5.1 Early return

```go
package main

import (
    "errors"
    "fmt"
)

func process(data string) error {
    if data == "" {
        return errors.New("empty data")
    }
    
    if len(data) > 100 {
        return errors.New("data too long")
    }
    
    // Основная логика
    fmt.Println("Processing:", data)
    return nil
}

func main() {
    inputs := []string{"", "hello", string(make([]byte, 101))}
    
    for _, input := range inputs {
        if err := process(input); err != nil {
            fmt.Println("Error:", err)
        }
    }
}
```

**Output:**
```
Error: empty data
Processing: hello
Error: data too long
```

### 5.2 Defer для cleanup

```go
package main

import (
    "fmt"
    "os"
)

func processFile(path string) error {
    file, err := os.Open(path)
    if err != nil {
        return fmt.Errorf("opening file: %w", err)
    }
    defer file.Close()  // Гарантированно закроется
    
    // Обработка файла...
    info, err := file.Stat()
    if err != nil {
        return fmt.Errorf("getting file info: %w", err)
    }
    
    fmt.Printf("File: %s, Size: %d bytes\n", info.Name(), info.Size())
    return nil
}

func main() {
    // Создадим тестовый файл
    os.WriteFile("test.txt", []byte("Hello, World!"), 0644)
    defer os.Remove("test.txt")
    
    if err := processFile("test.txt"); err != nil {
        fmt.Println("Error:", err)
    }
}
```

**Output:**
```
File: test.txt, Size: 13 bytes
```

### 5.3 Error handling middleware

```go
package main

import "fmt"

type Result struct {
    Value int
    Err   error
}

func step1(input int) Result {
    if input < 0 {
        return Result{Err: fmt.Errorf("step1: negative input")}
    }
    return Result{Value: input * 2}
}

func step2(r Result) Result {
    if r.Err != nil {
        return r  // Передаём ошибку дальше
    }
    if r.Value > 100 {
        return Result{Err: fmt.Errorf("step2: value too large")}
    }
    return Result{Value: r.Value + 10}
}

func step3(r Result) Result {
    if r.Err != nil {
        return r
    }
    return Result{Value: r.Value * r.Value}
}

func main() {
    // Pipeline
    result := step3(step2(step1(5)))
    if result.Err != nil {
        fmt.Println("Error:", result.Err)
    } else {
        fmt.Println("Result:", result.Value)
    }
    
    // Pipeline с ошибкой
    result = step3(step2(step1(-5)))
    if result.Err != nil {
        fmt.Println("Error:", result.Err)
    }
}
```

**Output:**
```
Result: 400
Error: step1: negative input
```

---

## 6. panic и recover

### 6.1 Когда использовать panic

```go
package main

import "fmt"

// panic для невосстановимых ошибок
func mustParse(s string) int {
    var n int
    _, err := fmt.Sscanf(s, "%d", &n)
    if err != nil {
        panic(fmt.Sprintf("mustParse: invalid input %q", s))
    }
    return n
}

func main() {
    fmt.Println(mustParse("42"))
    // fmt.Println(mustParse("abc"))  // panic!
}
```

**Output:**
```
42
```

### 6.2 recover для перехвата panic

```go
package main

import "fmt"

func safeCall(fn func()) (err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic recovered: %v", r)
        }
    }()
    
    fn()
    return nil
}

func riskyOperation() {
    panic("something went wrong!")
}

func main() {
    err := safeCall(riskyOperation)
    if err != nil {
        fmt.Println("Error:", err)
    }
    
    fmt.Println("Program continues...")
}
```

**Output:**
```
Error: panic recovered: something went wrong!
Program continues...
```

---

## 7. Common Pitfalls

### 7.1 Игнорирование ошибок

```go
// ПЛОХО
file, _ := os.Open("file.txt")  // Игнорируем ошибку!

// ХОРОШО
file, err := os.Open("file.txt")
if err != nil {
    return err
}
```

### 7.2 Возврат обёрнутых sentinel errors

```go
package main

import (
    "errors"
    "fmt"
)

var ErrNotFound = errors.New("not found")

func findItem(id int) error {
    // ПРАВИЛЬНО: оборачиваем с контекстом
    return fmt.Errorf("item %d: %w", id, ErrNotFound)
}

func main() {
    err := findItem(123)
    
    // errors.Is работает с обёрнутыми ошибками
    if errors.Is(err, ErrNotFound) {
        fmt.Println("Item not found")
    }
    
    fmt.Println("Full error:", err)
}
```

**Output:**
```
Item not found
Full error: item 123: not found
```

---

## 💡 Key Takeaways

- **Ошибки — это значения**: Обрабатывайте их явно, не игнорируйте.

- **Интерфейс error**: Любой тип с `Error() string` — ошибка.

- **errors.Is / errors.As**: Для проверки цепочек обёрнутых ошибок.

- **fmt.Errorf с %w**: Оборачивает ошибку с сохранением контекста.

- **panic/recover**: Только для невосстановимых ситуаций.

---

## 🚀 Next Steps

**Related Modules:**
- [09_Concurrency](../09_Concurrency/) — ошибки в горутинах
- [12_Stdlib](../12_Stdlib/) — io.EOF и другие стандартные ошибки

**Practice Ideas:**
1. Создайте иерархию custom error types
2. Реализуйте retry логику с обработкой ошибок
3. Напишите middleware для логирования ошибок

---

