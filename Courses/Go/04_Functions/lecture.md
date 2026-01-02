# Functions
## Функции, множественные возвращаемые значения и замыкания

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис Go (переменные, типы)
- Понимать управление потоком (if, for, switch)
- Уметь работать с defer

**Recommended prior modules:**

- [02_Basics](../02_Basics/) — переменные и типы
- [03_FlowControl](../03_FlowControl/) — условия и циклы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Определять и вызывать функции в Go
- Работать с множественными возвращаемыми значениями
- Использовать именованные возвращаемые значения
- Создавать variadic-функции
- Применять анонимные функции и замыкания
- Понимать функции как first-class citizens

---

## 1. Базовый синтаксис функций

### 1.1 Определение функции

```go
package main

import "fmt"

// Функция без параметров и возвращаемого значения
func sayHello() {
    fmt.Println("Hello!")
}

// Функция с параметрами
func greet(name string) {
    fmt.Printf("Hello, %s!\n", name)
}

// Функция с возвращаемым значением
func add(a int, b int) int {
    return a + b
}

// Сокращённое объявление параметров одного типа
func multiply(a, b int) int {
    return a * b
}

func main() {
    sayHello()
    greet("Gopher")
    
    sum := add(3, 5)
    fmt.Println("3 + 5 =", sum)
    
    product := multiply(4, 7)
    fmt.Println("4 * 7 =", product)
}
```

**Output:**
```
Hello!
Hello, Gopher!
3 + 5 = 8
4 * 7 = 28
```

### 1.2 Множественные возвращаемые значения

Go позволяет возвращать несколько значений — это ключевая особенность языка:

```go
package main

import "fmt"

// Два возвращаемых значения
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

// Три возвращаемых значения
func getPersonInfo() (string, int, bool) {
    return "Alice", 30, true
}

func main() {
    // Получаем оба значения
    result, err := divide(10, 3)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Printf("10 / 3 = %.2f\n", result)
    }
    
    // Ошибка деления на ноль
    _, err = divide(10, 0)
    if err != nil {
        fmt.Println("Error:", err)
    }
    
    // Распаковка всех значений
    name, age, active := getPersonInfo()
    fmt.Printf("Name: %s, Age: %d, Active: %t\n", name, age, active)
    
    // Игнорирование ненужных значений
    onlyName, _, _ := getPersonInfo()
    fmt.Println("Only name:", onlyName)
}
```

**Output:**
```
10 / 3 = 3.33
Error: division by zero
Name: Alice, Age: 30, Active: true
Only name: Alice
```

### 1.3 Именованные возвращаемые значения

```go
package main

import "fmt"

// Именованные возвращаемые значения
func rectangle(width, height float64) (area, perimeter float64) {
    area = width * height
    perimeter = 2 * (width + height)
    return  // "naked return" — возвращает именованные значения
}

// Полезно для документирования
func divmod(a, b int) (quotient, remainder int) {
    quotient = a / b
    remainder = a % b
    return
}

// Можно смешивать naked return и явный return
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return x, y  // Явный return тоже работает
}

func main() {
    area, perimeter := rectangle(5, 3)
    fmt.Printf("Area: %.1f, Perimeter: %.1f\n", area, perimeter)
    
    q, r := divmod(17, 5)
    fmt.Printf("17 / 5 = %d remainder %d\n", q, r)
    
    x, y := split(17)
    fmt.Printf("split(17) = %d, %d\n", x, y)
}
```

**Output:**
```
Area: 15.0, Perimeter: 16.0
17 / 5 = 3 remainder 2
split(17) = 7, 10
```

> **💡 Pro Tip:**  
> Именованные возвращаемые значения улучшают читаемость, но `naked return` может запутывать в длинных функциях. Используйте осторожно.

---

## 2. Variadic Functions

### 2.1 Функции с переменным числом аргументов

```go
package main

import "fmt"

// ... перед типом означает variadic параметр
func sum(numbers ...int) int {
    total := 0
    for _, n := range numbers {
        total += n
    }
    return total
}

// Variadic параметр должен быть последним
func greetAll(greeting string, names ...string) {
    for _, name := range names {
        fmt.Println(greeting, name)
    }
}

func main() {
    // Вызов с разным количеством аргументов
    fmt.Println("sum():", sum())
    fmt.Println("sum(1):", sum(1))
    fmt.Println("sum(1, 2, 3):", sum(1, 2, 3))
    fmt.Println("sum(1, 2, 3, 4, 5):", sum(1, 2, 3, 4, 5))
    
    fmt.Println()
    greetAll("Hello,", "Alice", "Bob", "Charlie")
}
```

**Output:**
```
sum(): 0
sum(1): 1
sum(1, 2, 3): 6
sum(1, 2, 3, 4, 5): 15

Hello, Alice
Hello, Bob
Hello, Charlie
```

### 2.2 Передача слайса в variadic функцию

```go
package main

import "fmt"

func sum(numbers ...int) int {
    total := 0
    for _, n := range numbers {
        total += n
    }
    return total
}

func main() {
    // Обычный вызов
    result1 := sum(1, 2, 3)
    fmt.Println("Direct:", result1)
    
    // Передача слайса с распаковкой
    nums := []int{10, 20, 30, 40}
    result2 := sum(nums...)  // Распаковка слайса
    fmt.Println("From slice:", result2)
    
    // Комбинирование не работает!
    // sum(1, 2, nums...)  // Ошибка компиляции
}
```

**Output:**
```
Direct: 6
From slice: 100
```

### 2.3 fmt.Printf — пример variadic функции

```go
package main

import "fmt"

func main() {
    // fmt.Printf — встроенная variadic функция
    fmt.Printf("Name: %s\n", "Go")
    fmt.Printf("Name: %s, Age: %d\n", "Go", 15)
    fmt.Printf("Name: %s, Age: %d, Active: %t\n", "Go", 15, true)
    
    // Можно передать слайс interface{}
    args := []interface{}{"Go", 15, true}
    fmt.Printf("Name: %s, Age: %d, Active: %t\n", args...)
}
```

**Output:**
```
Name: Go
Name: Go, Age: 15
Name: Go, Age: 15, Active: true
Name: Go, Age: 15, Active: true
```

---

## 3. Анонимные функции

### 3.1 Определение и немедленный вызов

```go
package main

import "fmt"

func main() {
    // Анонимная функция с немедленным вызовом (IIFE)
    result := func(a, b int) int {
        return a + b
    }(3, 5)
    fmt.Println("IIFE result:", result)
    
    // Присваивание функции переменной
    double := func(x int) int {
        return x * 2
    }
    
    fmt.Println("double(5):", double(5))
    fmt.Println("double(10):", double(10))
    
    // Тип переменной — функция
    fmt.Printf("Type of double: %T\n", double)
}
```

**Output:**
```
IIFE result: 8
double(5): 10
double(10): 20
Type of double: func(int) int
```

### 3.2 Функции как параметры

```go
package main

import "fmt"

// Функция принимает другую функцию как параметр
func apply(numbers []int, fn func(int) int) []int {
    result := make([]int, len(numbers))
    for i, n := range numbers {
        result[i] = fn(n)
    }
    return result
}

func main() {
    nums := []int{1, 2, 3, 4, 5}
    
    // Передаём анонимную функцию
    doubled := apply(nums, func(x int) int {
        return x * 2
    })
    fmt.Println("Doubled:", doubled)
    
    squared := apply(nums, func(x int) int {
        return x * x
    })
    fmt.Println("Squared:", squared)
}
```

**Output:**
```
Doubled: [2 4 6 8 10]
Squared: [1 4 9 16 25]
```

### 3.3 Функции как возвращаемые значения

```go
package main

import "fmt"

// Функция возвращает функцию
func multiplier(factor int) func(int) int {
    return func(x int) int {
        return x * factor
    }
}

// Фабрика функций
func makeGreeter(greeting string) func(string) string {
    return func(name string) string {
        return greeting + ", " + name + "!"
    }
}

func main() {
    double := multiplier(2)
    triple := multiplier(3)
    
    fmt.Println("double(5):", double(5))
    fmt.Println("triple(5):", triple(5))
    
    helloGreeter := makeGreeter("Hello")
    hiGreeter := makeGreeter("Hi")
    
    fmt.Println(helloGreeter("Alice"))
    fmt.Println(hiGreeter("Bob"))
}
```

**Output:**
```
double(5): 10
triple(5): 15
Hello, Alice!
Hi, Bob!
```

---

## 4. Замыкания (Closures)

### 4.1 Захват переменных

Замыкание — функция, которая "захватывает" переменные из окружающей области видимости:

```go
package main

import "fmt"

func counter() func() int {
    count := 0  // Эта переменная "захвачена" замыканием
    return func() int {
        count++
        return count
    }
}

func main() {
    // Каждый вызов counter() создаёт новое замыкание
    c1 := counter()
    c2 := counter()
    
    fmt.Println("c1:", c1())  // 1
    fmt.Println("c1:", c1())  // 2
    fmt.Println("c1:", c1())  // 3
    
    fmt.Println("c2:", c2())  // 1 — независимый счётчик
    fmt.Println("c2:", c2())  // 2
    
    fmt.Println("c1:", c1())  // 4 — продолжает считать
}
```

**Output:**
```
c1: 1
c1: 2
c1: 3
c2: 1
c2: 2
c1: 4
```

### 4.2 Практический пример: генератор ID

```go
package main

import "fmt"

func idGenerator(prefix string) func() string {
    id := 0
    return func() string {
        id++
        return fmt.Sprintf("%s-%04d", prefix, id)
    }
}

func main() {
    userID := idGenerator("USER")
    orderID := idGenerator("ORDER")
    
    fmt.Println(userID())   // USER-0001
    fmt.Println(userID())   // USER-0002
    fmt.Println(orderID())  // ORDER-0001
    fmt.Println(userID())   // USER-0003
    fmt.Println(orderID())  // ORDER-0002
}
```

**Output:**
```
USER-0001
USER-0002
ORDER-0001
USER-0003
ORDER-0002
```

### 4.3 Замыкание в цикле

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    // ПРОБЛЕМА: все замыкания захватывают одну переменную
    funcs := make([]func(), 3)
    
    for i := 0; i < 3; i++ {
        funcs[i] = func() {
            fmt.Println("Value:", i)  // i захвачена по ссылке!
        }
    }
    
    fmt.Println("Проблемный вариант:")
    for _, f := range funcs {
        f()  // Все выведут 3
    }
    
    // РЕШЕНИЕ 1: передать как параметр
    funcs2 := make([]func(), 3)
    for i := 0; i < 3; i++ {
        funcs2[i] = func(n int) func() {
            return func() {
                fmt.Println("Value:", n)
            }
        }(i)
    }
    
    fmt.Println("\nРешение 1 (параметр):")
    for _, f := range funcs2 {
        f()
    }
    
    // РЕШЕНИЕ 2: локальная переменная (Go 1.22+ решает это автоматически)
    funcs3 := make([]func(), 3)
    for i := 0; i < 3; i++ {
        i := i  // Создаём новую переменную в каждой итерации
        funcs3[i] = func() {
            fmt.Println("Value:", i)
        }
    }
    
    fmt.Println("\nРешение 2 (локальная переменная):")
    for _, f := range funcs3 {
        f()
    }
    
    _ = time.Now()  // Используем time для компиляции
}
```

**Output:**
```
Проблемный вариант:
Value: 3
Value: 3
Value: 3

Решение 1 (параметр):
Value: 0
Value: 1
Value: 2

Решение 2 (локальная переменная):
Value: 0
Value: 1
Value: 2
```

---

## 5. Функциональные типы

### 5.1 Определение типа функции

```go
package main

import "fmt"

// Определяем тип функции
type Operation func(int, int) int
type Predicate func(int) bool
type Transformer func(string) string

// Используем тип в параметрах
func calculate(a, b int, op Operation) int {
    return op(a, b)
}

func filter(numbers []int, pred Predicate) []int {
    var result []int
    for _, n := range numbers {
        if pred(n) {
            result = append(result, n)
        }
    }
    return result
}

func main() {
    add := func(a, b int) int { return a + b }
    sub := func(a, b int) int { return a - b }
    
    fmt.Println("10 + 5 =", calculate(10, 5, add))
    fmt.Println("10 - 5 =", calculate(10, 5, sub))
    
    nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    isEven := func(n int) bool { return n%2 == 0 }
    isGreaterThan5 := func(n int) bool { return n > 5 }
    
    fmt.Println("Even:", filter(nums, isEven))
    fmt.Println(">5:", filter(nums, isGreaterThan5))
}
```

**Output:**
```
10 + 5 = 15
10 - 5 = 5
Even: [2 4 6 8 10]
>5: [6 7 8 9 10]
```

### 5.2 Методы на функциональных типах

```go
package main

import "fmt"

type IntSliceFunc func([]int) []int

// Можно определять методы на функциональных типах!
func (f IntSliceFunc) Then(next IntSliceFunc) IntSliceFunc {
    return func(input []int) []int {
        return next(f(input))
    }
}

func main() {
    double := IntSliceFunc(func(nums []int) []int {
        result := make([]int, len(nums))
        for i, n := range nums {
            result[i] = n * 2
        }
        return result
    })
    
    addOne := IntSliceFunc(func(nums []int) []int {
        result := make([]int, len(nums))
        for i, n := range nums {
            result[i] = n + 1
        }
        return result
    })
    
    // Композиция функций
    pipeline := double.Then(addOne)
    
    nums := []int{1, 2, 3}
    fmt.Println("Original:", nums)
    fmt.Println("double:", double(nums))
    fmt.Println("double.Then(addOne):", pipeline(nums))
}
```

**Output:**
```
Original: [1 2 3]
double: [2 4 6]
double.Then(addOne): [3 5 7]
```

---

## 6. Рекурсия

### 6.1 Базовая рекурсия

```go
package main

import "fmt"

// Факториал
func factorial(n int) int {
    if n <= 1 {
        return 1
    }
    return n * factorial(n-1)
}

// Числа Фибоначчи
func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
    for i := 0; i <= 10; i++ {
        fmt.Printf("factorial(%d) = %d\n", i, factorial(i))
    }
    
    fmt.Println()
    
    for i := 0; i <= 10; i++ {
        fmt.Printf("fibonacci(%d) = %d\n", i, fibonacci(i))
    }
}
```

**Output:**
```
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
factorial(5) = 120
factorial(6) = 720
factorial(7) = 5040
factorial(8) = 40320
factorial(9) = 362880
factorial(10) = 3628800

fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(2) = 1
fibonacci(3) = 2
fibonacci(4) = 3
fibonacci(5) = 5
fibonacci(6) = 8
fibonacci(7) = 13
fibonacci(8) = 21
fibonacci(9) = 34
fibonacci(10) = 55
```

### 6.2 Оптимизация рекурсии (мемоизация)

```go
package main

import "fmt"

// Рекурсия с мемоизацией через замыкание
func fibMemo() func(int) int {
    cache := make(map[int]int)
    
    var fib func(int) int
    fib = func(n int) int {
        if n <= 1 {
            return n
        }
        if val, ok := cache[n]; ok {
            return val
        }
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    }
    
    return fib
}

func main() {
    fib := fibMemo()
    
    // Теперь работает быстро даже для больших чисел
    fmt.Println("fib(10):", fib(10))
    fmt.Println("fib(40):", fib(40))
    fmt.Println("fib(50):", fib(50))
}
```

**Output:**
```
fib(10): 55
fib(40): 102334155
fib(50): 12586269025
```

---

## 7. init() функция

### 7.1 Специальная функция инициализации

```go
package main

import "fmt"

var message string

// init вызывается автоматически перед main
func init() {
    fmt.Println("init() called")
    message = "Initialized!"
}

// Можно иметь несколько init в одном файле
func init() {
    fmt.Println("second init() called")
}

func main() {
    fmt.Println("main() called")
    fmt.Println("message:", message)
}
```

**Output:**
```
init() called
second init() called
main() called
message: Initialized!
```

### 7.2 Порядок инициализации

```go
// Порядок выполнения:
// 1. Инициализация переменных пакета
// 2. init() функции (в порядке появления)
// 3. main() (только для main пакета)

package main

import "fmt"

var a = initVar("a")

func initVar(name string) string {
    fmt.Printf("Initializing var %s\n", name)
    return name
}

var b = initVar("b")

func init() {
    fmt.Println("First init")
}

func init() {
    fmt.Println("Second init")
}

func main() {
    fmt.Println("main")
}
```

**Output:**
```
Initializing var a
Initializing var b
First init
Second init
main
```

---

## 8. Common Pitfalls

### 8.1 Неиспользуемые параметры

```go
package main

// Ошибка: unused parameter
// func process(data []byte, options string) {
//     // options не используется
// }

// Используйте _ для неиспользуемых параметров
func process(data []byte, _ string) {
    _ = data
}

func main() {
    process([]byte("test"), "unused")
}
```

### 8.2 Путаница с naked return

```go
package main

import "fmt"

// Запутанный код — избегайте в длинных функциях
func confusing(x int) (a, b int) {
    if x > 0 {
        a = x
        b = x * 2
        return  // Что возвращается?
    }
    a = -x
    return  // А здесь?
}

// Лучше — явный return
func clear(x int) (a, b int) {
    if x > 0 {
        a = x
        b = x * 2
        return a, b
    }
    a = -x
    b = 0
    return a, b
}

func main() {
    fmt.Println(confusing(5))
    fmt.Println(clear(5))
}
```

**Output:**
```
5 10
5 10
```

### 8.3 Изменение слайса в функции

```go
package main

import "fmt"

func addElement(s []int, elem int) []int {
    return append(s, elem)  // append может создать новый слайс!
}

func modifyInPlace(s []int) {
    for i := range s {
        s[i] *= 2  // Изменяет оригинальный слайс
    }
}

func main() {
    nums := []int{1, 2, 3}
    
    // addElement не изменяет оригинал
    newNums := addElement(nums, 4)
    fmt.Println("Original:", nums)
    fmt.Println("New:", newNums)
    
    // modifyInPlace изменяет оригинал
    modifyInPlace(nums)
    fmt.Println("After modify:", nums)
}
```

**Output:**
```
Original: [1 2 3]
New: [1 2 3 4]
After modify: [2 4 6]
```

---

## 💡 Key Takeaways

- **Множественные возвращаемые значения**: Идиоматический способ возвращать результат и ошибку. Всегда проверяйте ошибки.

- **Variadic функции**: Используйте `...` для переменного числа аргументов. Передавайте слайс с `slice...`.

- **Замыкания захватывают переменные**: Замыкания сохраняют доступ к переменным из внешней области видимости.

- **Функции — first-class citizens**: Функции можно передавать как параметры, возвращать и присваивать переменным.

- **init() для инициализации**: Используйте для настройки пакета, но не злоупотребляйте.

---

## 🚀 Next Steps

**Related Modules:**

- [05_DataStructures](../05_DataStructures/) — массивы, слайсы, мапы
- [06_Pointers](../06_Pointers/) — указатели и передача по ссылке
- [07_Methods](../07_Methods/) — методы и интерфейсы

**Practice Ideas:**

1. Напишите функцию `map` для трансформации слайса
2. Создайте генератор уникальных ID с замыканием
3. Реализуйте функцию `reduce` для агрегации значений
4. Напишите мемоизированную версию тяжёлой функции

**Going Deeper:**

- Изучите паттерн functional options
- Прочитайте о defer с анонимными функциями
- Изучите context для отмены функций

---




