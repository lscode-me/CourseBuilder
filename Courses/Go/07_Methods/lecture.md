# Methods and Interfaces
## Методы, интерфейсы, полиморфизм и embedding

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать структуры и указатели
- Знать разницу между value и pointer receivers
- Уметь работать с функциями

**Recommended prior modules:**
- [05_DataStructures](../05_DataStructures/) — структуры
- [06_Pointers](../06_Pointers/) — указатели

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять методы для типов
- Создавать и реализовывать интерфейсы
- Применять полиморфизм через интерфейсы
- Использовать embedding для композиции
- Понимать пустой интерфейс и type assertions

---

## 1. Методы

### 1.1 Определение методов

Метод — это функция с receiver (получателем):

```go
package main

import (
    "fmt"
    "math"
)

type Circle struct {
    Radius float64
}

// Метод с value receiver
func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.Radius
}

func main() {
    c := Circle{Radius: 5}
    
    fmt.Printf("Radius: %.1f\n", c.Radius)
    fmt.Printf("Area: %.2f\n", c.Area())
    fmt.Printf("Perimeter: %.2f\n", c.Perimeter())
}
```

**Output:**
```
Radius: 5.0
Area: 78.54
Perimeter: 31.42
```

### 1.2 Value vs Pointer Receiver

```go
package main

import "fmt"

type Counter struct {
    value int
}

// Value receiver — не модифицирует
func (c Counter) ValueIncrement() {
    c.value++  // Изменяет копию!
}

// Pointer receiver — модифицирует оригинал
func (c *Counter) Increment() {
    c.value++
}

func (c *Counter) Add(n int) {
    c.value += n
}

func (c Counter) Value() int {
    return c.value
}

func main() {
    c := Counter{value: 0}
    
    c.ValueIncrement()
    fmt.Println("After ValueIncrement:", c.Value())  // 0
    
    c.Increment()
    fmt.Println("After Increment:", c.Value())       // 1
    
    c.Add(10)
    fmt.Println("After Add(10):", c.Value())         // 11
}
```

**Output:**
```
After ValueIncrement: 0
After Increment: 1
After Add(10): 11
```

### 1.3 Методы на любых типах

```go
package main

import "fmt"

// Метод на встроенном типе через type alias
type MyInt int

func (n MyInt) Double() MyInt {
    return n * 2
}

func (n MyInt) IsPositive() bool {
    return n > 0
}

// Метод на slice type
type IntSlice []int

func (s IntSlice) Sum() int {
    total := 0
    for _, v := range s {
        total += v
    }
    return total
}

func (s IntSlice) Average() float64 {
    if len(s) == 0 {
        return 0
    }
    return float64(s.Sum()) / float64(len(s))
}

func main() {
    n := MyInt(5)
    fmt.Println("n:", n)
    fmt.Println("n.Double():", n.Double())
    fmt.Println("n.IsPositive():", n.IsPositive())
    
    nums := IntSlice{1, 2, 3, 4, 5}
    fmt.Println("Sum:", nums.Sum())
    fmt.Println("Average:", nums.Average())
}
```

**Output:**
```
n: 5
n.Double(): 10
n.IsPositive(): true
Sum: 15
Average: 3
```

---

## 2. Интерфейсы

### 2.1 Определение интерфейса

Интерфейс определяет набор методов:

```go
package main

import (
    "fmt"
    "math"
)

// Интерфейс
type Shape interface {
    Area() float64
    Perimeter() float64
}

// Реализация: Circle
type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.Radius
}

// Реализация: Rectangle
type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}

// Функция принимает интерфейс
func PrintShapeInfo(s Shape) {
    fmt.Printf("Area: %.2f, Perimeter: %.2f\n", s.Area(), s.Perimeter())
}

func main() {
    c := Circle{Radius: 5}
    r := Rectangle{Width: 10, Height: 5}
    
    PrintShapeInfo(c)
    PrintShapeInfo(r)
    
    // Слайс интерфейсов
    shapes := []Shape{c, r}
    for _, s := range shapes {
        PrintShapeInfo(s)
    }
}
```

**Output:**
```
Area: 78.54, Perimeter: 31.42
Area: 50.00, Perimeter: 30.00
Area: 78.54, Perimeter: 31.42
Area: 50.00, Perimeter: 30.00
```

### 2.2 Неявная реализация

В Go интерфейсы реализуются **неявно** — не нужно объявлять `implements`:

```go
package main

import "fmt"

type Stringer interface {
    String() string
}

type Person struct {
    Name string
    Age  int
}

// Person автоматически реализует Stringer
func (p Person) String() string {
    return fmt.Sprintf("%s (%d years)", p.Name, p.Age)
}

func Print(s Stringer) {
    fmt.Println(s.String())
}

func main() {
    p := Person{Name: "Alice", Age: 30}
    Print(p)  // Person реализует Stringer
    
    // fmt.Println также использует Stringer
    fmt.Println(p)
}
```

**Output:**
```
Alice (30 years)
Alice (30 years)
```

### 2.3 Пустой интерфейс

`interface{}` (или `any` в Go 1.18+) принимает любое значение:

```go
package main

import "fmt"

func PrintAnything(v interface{}) {
    fmt.Printf("Type: %T, Value: %v\n", v, v)
}

// any — алиас для interface{} (Go 1.18+)
func PrintAny(v any) {
    fmt.Printf("Type: %T, Value: %v\n", v, v)
}

func main() {
    PrintAnything(42)
    PrintAnything("hello")
    PrintAnything([]int{1, 2, 3})
    PrintAnything(map[string]int{"a": 1})
    
    // Слайс любых значений
    items := []any{42, "hello", true, 3.14}
    for _, item := range items {
        PrintAny(item)
    }
}
```

**Output:**
```
Type: int, Value: 42
Type: string, Value: hello
Type: []int, Value: [1 2 3]
Type: map[string]int, Value: map[a:1]
Type: int, Value: 42
Type: string, Value: hello
Type: bool, Value: true
Type: float64, Value: 3.14
```

---

## 3. Type Assertions

### 3.1 Базовый синтаксис

```go
package main

import "fmt"

func main() {
    var i interface{} = "hello"
    
    // Type assertion
    s := i.(string)
    fmt.Println("String:", s)
    
    // Безопасная форма с ok
    s, ok := i.(string)
    fmt.Printf("String: %q, ok: %t\n", s, ok)
    
    // Неуспешное assertion
    n, ok := i.(int)
    fmt.Printf("Int: %d, ok: %t\n", n, ok)
    
    // Panic при неуспешном assertion без ok
    // n = i.(int)  // panic: interface conversion
}
```

**Output:**
```
String: hello
String: "hello", ok: true
Int: 0, ok: false
```

### 3.2 Type Switch

```go
package main

import "fmt"

func describe(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("Integer: %d\n", v)
    case string:
        fmt.Printf("String: %q (len %d)\n", v, len(v))
    case bool:
        fmt.Printf("Boolean: %t\n", v)
    case []int:
        fmt.Printf("Int slice: %v\n", v)
    case nil:
        fmt.Println("Nil value")
    default:
        fmt.Printf("Unknown type: %T\n", v)
    }
}

func main() {
    describe(42)
    describe("hello")
    describe(true)
    describe([]int{1, 2, 3})
    describe(nil)
    describe(3.14)
}
```

**Output:**
```
Integer: 42
String: "hello" (len 5)
Boolean: true
Int slice: [1 2 3]
Nil value
Unknown type: float64
```

---

## 4. Композиция интерфейсов

### 4.1 Встраивание интерфейсов

```go
package main

import "fmt"

type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Композиция интерфейсов
type ReadWriter interface {
    Reader
    Writer
}

// Реализация
type Buffer struct {
    data []byte
}

func (b *Buffer) Read(p []byte) (int, error) {
    n := copy(p, b.data)
    b.data = b.data[n:]
    return n, nil
}

func (b *Buffer) Write(p []byte) (int, error) {
    b.data = append(b.data, p...)
    return len(p), nil
}

func main() {
    var rw ReadWriter = &Buffer{}
    
    rw.Write([]byte("Hello, Go!"))
    
    buf := make([]byte, 5)
    n, _ := rw.Read(buf)
    fmt.Printf("Read %d bytes: %s\n", n, buf)
}
```

**Output:**
```
Read 5 bytes: Hello
```

### 4.2 Стандартные интерфейсы

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    // strings.Reader реализует io.Reader
    r := strings.NewReader("Hello, World!")
    
    buf := make([]byte, 5)
    for {
        n, err := r.Read(buf)
        if err == io.EOF {
            break
        }
        fmt.Printf("Read: %q\n", buf[:n])
    }
}
```

**Output:**
```
Read: "Hello"
Read: ", Wor"
Read: "ld!"
```

---

## 5. Embedding (Встраивание)

### 5.1 Embedding структур

```go
package main

import "fmt"

type Address struct {
    City    string
    Country string
}

func (a Address) FullAddress() string {
    return a.City + ", " + a.Country
}

type Person struct {
    Name string
    Age  int
    Address  // Embedded struct
}

func main() {
    p := Person{
        Name: "Alice",
        Age:  30,
        Address: Address{
            City:    "Moscow",
            Country: "Russia",
        },
    }
    
    // Прямой доступ к полям embedded struct
    fmt.Println("Name:", p.Name)
    fmt.Println("City:", p.City)  // Напрямую!
    fmt.Println("Address.City:", p.Address.City)
    
    // Методы тоже "наследуются"
    fmt.Println("Full address:", p.FullAddress())
}
```

**Output:**
```
Name: Alice
City: Moscow
Address.City: Moscow
Full address: Moscow, Russia
```

### 5.2 Embedding для реализации интерфейсов

```go
package main

import "fmt"

type Logger interface {
    Log(message string)
}

type ConsoleLogger struct{}

func (l ConsoleLogger) Log(message string) {
    fmt.Println("[LOG]", message)
}

// Service встраивает Logger
type Service struct {
    Name string
    ConsoleLogger  // Embedding
}

func (s Service) DoWork() {
    s.Log("Starting work...")  // Используем метод embedded type
    fmt.Println("Working on", s.Name)
    s.Log("Work completed")
}

func main() {
    s := Service{Name: "DataProcessor"}
    s.DoWork()
    
    // Service реализует Logger!
    var logger Logger = s
    logger.Log("Direct log call")
}
```

**Output:**
```
[LOG] Starting work...
Working on DataProcessor
[LOG] Work completed
[LOG] Direct log call
```

### 5.3 Переопределение методов

```go
package main

import "fmt"

type Animal struct {
    Name string
}

func (a Animal) Speak() string {
    return "..."
}

type Dog struct {
    Animal  // Embedding
    Breed string
}

// Переопределяем метод
func (d Dog) Speak() string {
    return "Woof!"
}

func main() {
    d := Dog{
        Animal: Animal{Name: "Buddy"},
        Breed:  "Labrador",
    }
    
    fmt.Println("Name:", d.Name)
    fmt.Println("Breed:", d.Breed)
    fmt.Println("Dog speaks:", d.Speak())
    fmt.Println("Animal speaks:", d.Animal.Speak())
}
```

**Output:**
```
Name: Buddy
Breed: Labrador
Dog speaks: Woof!
Animal speaks: ...
```

---

## 6. Полиморфизм

### 6.1 Полиморфизм через интерфейсы

```go
package main

import "fmt"

type PaymentMethod interface {
    Pay(amount float64) string
}

type CreditCard struct {
    Number string
}

func (c CreditCard) Pay(amount float64) string {
    return fmt.Sprintf("Paid $%.2f with Credit Card %s", amount, c.Number[len(c.Number)-4:])
}

type PayPal struct {
    Email string
}

func (p PayPal) Pay(amount float64) string {
    return fmt.Sprintf("Paid $%.2f via PayPal (%s)", amount, p.Email)
}

type Bitcoin struct {
    Wallet string
}

func (b Bitcoin) Pay(amount float64) string {
    return fmt.Sprintf("Paid $%.2f in Bitcoin to %s", amount, b.Wallet[:8]+"...")
}

func ProcessPayment(method PaymentMethod, amount float64) {
    result := method.Pay(amount)
    fmt.Println(result)
}

func main() {
    methods := []PaymentMethod{
        CreditCard{Number: "1234567890123456"},
        PayPal{Email: "user@example.com"},
        Bitcoin{Wallet: "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"},
    }
    
    for _, m := range methods {
        ProcessPayment(m, 99.99)
    }
}
```

**Output:**
```
Paid $99.99 with Credit Card 3456
Paid $99.99 via PayPal (user@example.com)
Paid $99.99 in Bitcoin to 1A1zP1eP...
```

---

## 7. Common Pitfalls

### 7.1 nil интерфейс vs nil значение

```go
package main

import "fmt"

type MyError struct {
    Message string
}

func (e *MyError) Error() string {
    return e.Message
}

func getError(fail bool) error {
    var err *MyError = nil
    if fail {
        err = &MyError{"something went wrong"}
    }
    return err  // Возвращает interface с nil value!
}

func main() {
    err := getError(false)
    
    // Внимание: err != nil, хотя значение nil!
    if err != nil {
        fmt.Println("Got error:", err)  // Это выполнится!
    } else {
        fmt.Println("No error")
    }
    
    fmt.Printf("err == nil: %t\n", err == nil)
    fmt.Printf("Type: %T, Value: %v\n", err, err)
}
```

**Output:**
```
Got error: <nil>
err == nil: false
Type: *main.MyError, Value: <nil>
```

**Решение:**

```go
func getErrorCorrect(fail bool) error {
    if fail {
        return &MyError{"something went wrong"}
    }
    return nil  // Возвращаем nil напрямую
}
```

### 7.2 Pointer receiver и интерфейсы

```go
package main

import "fmt"

type Incrementer interface {
    Increment()
}

type Counter struct {
    value int
}

func (c *Counter) Increment() {  // Pointer receiver!
    c.value++
}

func main() {
    c := Counter{value: 0}
    
    // Это работает
    var i Incrementer = &c
    i.Increment()
    fmt.Println("Value:", c.value)
    
    // Это НЕ работает!
    // var i2 Incrementer = c  // Ошибка компиляции!
    // Counter не реализует Incrementer, только *Counter
}
```

---

## 💡 Key Takeaways

- **Методы = функции с receiver**: Добавляют поведение к типам.

- **Интерфейсы — неявные**: Тип реализует интерфейс, если имеет все его методы.

- **interface{} / any**: Пустой интерфейс принимает любой тип.

- **Type assertions**: Извлекают конкретный тип из интерфейса.

- **Embedding**: Композиция вместо наследования. Методы "наследуются".

---

## 🚀 Next Steps

**Related Modules:**
- [08_Errors](../08_Errors/) — error interface
- [10_Packages](../10_Packages/) — экспорт и видимость

**Practice Ideas:**
1. Создайте интерфейс Shape с несколькими реализациями
2. Реализуйте паттерн Strategy через интерфейсы
3. Напишите обёртку для логирования с embedding

---

