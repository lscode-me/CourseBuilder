# Testing
## Тестирование в Go, table-driven tests и бенчмарки

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать функции и пакеты
- Знать структуры и интерфейсы
- Уметь организовывать код в модули

**Recommended prior modules:**

- [04_Functions](../04_Functions/) — функции
- [10_Packages](../10_Packages/) — пакеты

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Писать unit-тесты в Go
- Использовать table-driven tests
- Создавать бенчмарки
- Применять subtests и test fixtures
- Работать с test coverage

---

## 1. Основы тестирования

### 1.1 Первый тест

```go
// math.go
package math

func Add(a, b int) int {
    return a + b
}

func Multiply(a, b int) int {
    return a * b
}
```

```go
// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    expected := 5
    
    if result != expected {
        t.Errorf("Add(2, 3) = %d; want %d", result, expected)
    }
}

func TestMultiply(t *testing.T) {
    result := Multiply(3, 4)
    expected := 12
    
    if result != expected {
        t.Errorf("Multiply(3, 4) = %d; want %d", result, expected)
    }
}
```

```bash
go test
```

**Output:**
```
PASS
ok      mypackage/math    0.001s
```

### 1.2 Запуск тестов

```bash
# Все тесты в текущем пакете

go test

# Все тесты рекурсивно

go test ./...

# С verbose output

go test -v

# Конкретный тест

go test -run TestAdd

# Регулярное выражение

go test -run "Test.*Multiply"

# С race detector

go test -race
```

### 1.3 Методы testing.T

```go
func TestExample(t *testing.T) {
    // Продолжить после ошибки
    t.Error("something wrong")
    t.Errorf("formatted: %d", 42)
    
    // Остановить тест
    t.Fatal("critical error")
    t.Fatalf("formatted: %s", "error")
    
    // Логирование (видно с -v)
    t.Log("info message")
    t.Logf("formatted: %v", data)
    
    // Пропустить тест
    if condition {
        t.Skip("skipping test")
        t.Skipf("skipping: %s", reason)
    }
    
    // Пометить как failed без остановки
    t.Fail()      // Пометить failed
    t.FailNow()   // Пометить и остановить
}
```

---

## 2. Table-Driven Tests

### 2.1 Базовый паттерн

```go
package math

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive numbers", 2, 3, 5},
        {"negative numbers", -1, -2, -3},
        {"mixed numbers", 5, -3, 2},
        {"zeros", 0, 0, 0},
        {"with zero", 5, 0, 5},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d",
                    tt.a, tt.b, result, tt.expected)
            }
        })
    }
}
```

**Output:**
```
=== RUN   TestAdd
=== RUN   TestAdd/positive_numbers
=== RUN   TestAdd/negative_numbers
=== RUN   TestAdd/mixed_numbers
=== RUN   TestAdd/zeros
=== RUN   TestAdd/with_zero
--- PASS: TestAdd (0.00s)
    --- PASS: TestAdd/positive_numbers (0.00s)
    --- PASS: TestAdd/negative_numbers (0.00s)
    --- PASS: TestAdd/mixed_numbers (0.00s)
    --- PASS: TestAdd/zeros (0.00s)
    --- PASS: TestAdd/with_zero (0.00s)
PASS
```

### 2.2 Table tests с ошибками

```go
func Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

func TestDivide(t *testing.T) {
    tests := []struct {
        name    string
        a, b    float64
        want    float64
        wantErr bool
    }{
        {"normal division", 10, 2, 5, false},
        {"division by zero", 10, 0, 0, true},
        {"negative result", -10, 2, -5, false},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := Divide(tt.a, tt.b)
            
            if (err != nil) != tt.wantErr {
                t.Errorf("Divide() error = %v, wantErr %v", err, tt.wantErr)
                return
            }
            
            if got != tt.want {
                t.Errorf("Divide() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

---

## 3. Subtests

### 3.1 t.Run

```go
func TestUserService(t *testing.T) {
    t.Run("Create", func(t *testing.T) {
        // Test create
    })
    
    t.Run("Read", func(t *testing.T) {
        // Test read
    })
    
    t.Run("Update", func(t *testing.T) {
        // Test update
    })
    
    t.Run("Delete", func(t *testing.T) {
        // Test delete
    })
}
```

### 3.2 Параллельные тесты

```go
func TestParallel(t *testing.T) {
    tests := []struct {
        name  string
        input int
    }{
        {"case1", 1},
        {"case2", 2},
        {"case3", 3},
    }
    
    for _, tt := range tests {
        tt := tt // Важно для параллельных тестов!
        t.Run(tt.name, func(t *testing.T) {
            t.Parallel() // Запуск параллельно
            
            result := process(tt.input)
            if result != tt.input*2 {
                t.Errorf("got %d, want %d", result, tt.input*2)
            }
        })
    }
}
```

---

## 4. Test Fixtures и Helpers

### 4.1 Setup и Teardown

```go
func TestWithSetup(t *testing.T) {
    // Setup
    db, err := setupDatabase()
    if err != nil {
        t.Fatalf("setup failed: %v", err)
    }
    
    // Teardown
    t.Cleanup(func() {
        db.Close()
    })
    
    // Tests
    t.Run("test1", func(t *testing.T) {
        // использует db
    })
    
    t.Run("test2", func(t *testing.T) {
        // использует db
    })
}
```

### 4.2 TestMain

```go
var testDB *sql.DB

func TestMain(m *testing.M) {
    // Setup перед всеми тестами
    var err error
    testDB, err = sql.Open("postgres", "...")
    if err != nil {
        log.Fatal(err)
    }
    
    // Запуск тестов
    code := m.Run()
    
    // Teardown после всех тестов
    testDB.Close()
    
    os.Exit(code)
}

func TestSomething(t *testing.T) {
    // testDB доступен
}
```

### 4.3 Helper функции

```go
func assertEqual(t *testing.T, got, want interface{}) {
    t.Helper() // Показывает caller в ошибках
    
    if got != want {
        t.Errorf("got %v, want %v", got, want)
    }
}

func assertNoError(t *testing.T, err error) {
    t.Helper()
    
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
}

func TestWithHelpers(t *testing.T) {
    result, err := SomeFunction()
    assertNoError(t, err)
    assertEqual(t, result, 42)
}
```

---

## 5. Бенчмарки

### 5.1 Базовый бенчмарк

```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(1, 2)
    }
}
```

```bash
go test -bench=.
```

**Output:**
```
BenchmarkAdd-8    1000000000    0.290 ns/op
```

### 5.2 Бенчмарк с подготовкой

```go
func BenchmarkComplexOperation(b *testing.B) {
    // Подготовка (не измеряется)
    data := prepareData()
    
    b.ResetTimer() // Сбросить таймер
    
    for i := 0; i < b.N; i++ {
        processData(data)
    }
}
```

### 5.3 Бенчмарк памяти

```go
func BenchmarkWithAllocs(b *testing.B) {
    b.ReportAllocs() // Показать аллокации
    
    for i := 0; i < b.N; i++ {
        _ = make([]byte, 1024)
    }
}
```

**Output:**
```
BenchmarkWithAllocs-8    1234567    890 ns/op    1024 B/op    1 allocs/op
```

### 5.4 Сравнительные бенчмарки

```go
func BenchmarkConcat(b *testing.B) {
    b.Run("plus", func(b *testing.B) {
        for i := 0; i < b.N; i++ {
            _ = "hello" + " " + "world"
        }
    })
    
    b.Run("Sprintf", func(b *testing.B) {
        for i := 0; i < b.N; i++ {
            _ = fmt.Sprintf("%s %s", "hello", "world")
        }
    })
    
    b.Run("Builder", func(b *testing.B) {
        for i := 0; i < b.N; i++ {
            var sb strings.Builder
            sb.WriteString("hello")
            sb.WriteString(" ")
            sb.WriteString("world")
            _ = sb.String()
        }
    })
}
```

---

## 6. Coverage

### 6.1 Запуск с coverage

```bash
# Показать процент coverage

go test -cover

# Создать coverage profile

go test -coverprofile=coverage.out

# HTML отчёт

go tool cover -html=coverage.out

# Показать по функциям

go tool cover -func=coverage.out
```

**Output:**
```
ok      mypackage    0.005s    coverage: 80.0% of statements
```

### 6.2 Coverage mode

```bash
# set — was line executed (default)

go test -covermode=set -coverprofile=coverage.out

# count — how many times

go test -covermode=count -coverprofile=coverage.out

# atomic — like count, safe for concurrent

go test -covermode=atomic -coverprofile=coverage.out
```

---

## 7. Mocking

### 7.1 Интерфейсы для mocking

```go
// Интерфейс для зависимости
type UserRepository interface {
    GetByID(id int) (*User, error)
    Save(user *User) error
}

// Реальная реализация
type PostgresUserRepo struct {
    db *sql.DB
}

func (r *PostgresUserRepo) GetByID(id int) (*User, error) {
    // Реальная логика
}

// Mock для тестов
type MockUserRepo struct {
    users map[int]*User
    err   error
}

func (m *MockUserRepo) GetByID(id int) (*User, error) {
    if m.err != nil {
        return nil, m.err
    }
    return m.users[id], nil
}
```

### 7.2 Использование mock

```go
func TestUserService(t *testing.T) {
    mock := &MockUserRepo{
        users: map[int]*User{
            1: {ID: 1, Name: "Alice"},
        },
    }
    
    service := NewUserService(mock)
    
    user, err := service.GetUser(1)
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    
    if user.Name != "Alice" {
        t.Errorf("got name %s, want Alice", user.Name)
    }
}

func TestUserServiceError(t *testing.T) {
    mock := &MockUserRepo{
        err: errors.New("database error"),
    }
    
    service := NewUserService(mock)
    
    _, err := service.GetUser(1)
    if err == nil {
        t.Error("expected error, got nil")
    }
}
```

---

## 8. Examples

### 8.1 Testable Examples

```go
func ExampleAdd() {
    result := Add(2, 3)
    fmt.Println(result)
    // Output: 5
}

func ExampleAdd_negative() {
    result := Add(-1, -2)
    fmt.Println(result)
    // Output: -3
}
```

### 8.2 Unordered output

```go
func ExamplePrintMap() {
    m := map[string]int{"a": 1, "b": 2}
    for k, v := range m {
        fmt.Printf("%s: %d\n", k, v)
    }
    // Unordered output:
    // a: 1
    // b: 2
}
```

---

## 9. Best Practices

### 9.1 Naming

```go
// Тестовые файлы: *_test.go
// math.go -> math_test.go

// Тестовые функции: Test*
func TestFunctionName(t *testing.T)

// Бенчмарки: Benchmark*
func BenchmarkFunctionName(b *testing.B)

// Examples: Example*
func ExampleFunctionName()
```

### 9.2 Test isolation

```go
func TestIsolated(t *testing.T) {
    // Каждый тест должен быть независимым
    // Не полагаться на порядок выполнения
    // Не изменять глобальное состояние
    
    // Используйте t.Cleanup для очистки
    t.Cleanup(func() {
        // cleanup
    })
}
```

---

## 💡 Key Takeaways

- **_test.go файлы**: Тесты в отдельных файлах с суффиксом _test.

- **Table-driven tests**: Стандартный паттерн для Go тестов.

- **t.Run для subtests**: Организация и фильтрация тестов.

- **Бенчмарки**: Используйте для измерения производительности.

- **Интерфейсы для mocking**: Позволяют тестировать без реальных зависимостей.

---

## 🚀 Next Steps

**Related Modules:**

- [12_Stdlib](../12_Stdlib/) — тестирование HTTP

**Practice Ideas:**

1. Напишите тесты для своего проекта
2. Достигните 80% coverage
3. Создайте бенчмарки для критичного кода

---





