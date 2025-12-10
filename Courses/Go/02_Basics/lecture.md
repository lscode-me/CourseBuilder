# Go Basics
## Переменные, типы данных, константы и операторы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Установить Go и настроить окружение
- Уметь создавать и запускать Go-программы
- Понимать базовую структуру Go-программы (package, import, func main)

**Recommended prior modules:**
- [01_Intro](../01_Intro/) — введение в Go

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объявлять переменные различными способами
- Использовать все базовые типы данных Go
- Работать с константами и iota
- Применять арифметические, логические и побитовые операторы
- Понимать нулевые значения (zero values) в Go

---

## 1. Переменные

### 1.1 Объявление переменных

В Go есть несколько способов объявить переменную:

```go
package main

import "fmt"

func main() {
    // Способ 1: var с явным типом
    var name string = "Gopher"
    
    // Способ 2: var с выводом типа
    var age = 10
    
    // Способ 3: var без инициализации (zero value)
    var score int
    
    // Способ 4: короткое объявление := (только внутри функций)
    city := "Moscow"
    
    fmt.Printf("name: %s (type: %T)\n", name, name)
    fmt.Printf("age: %d (type: %T)\n", age, age)
    fmt.Printf("score: %d (type: %T)\n", score, score)
    fmt.Printf("city: %s (type: %T)\n", city, city)
}
```

**Output:**
```
name: Gopher (type: string)
age: 10 (type: int)
score: 0 (type: int)
city: Moscow (type: string)
```

### 1.2 Множественное объявление

```go
package main

import "fmt"

func main() {
    // Несколько переменных одного типа
    var a, b, c int = 1, 2, 3
    
    // Несколько переменных разных типов
    var (
        firstName string = "John"
        lastName  string = "Doe"
        age       int    = 30
        isActive  bool   = true
    )
    
    // Короткое объявление нескольких переменных
    x, y := 10, 20
    name, valid := "test", true
    
    fmt.Println("a, b, c:", a, b, c)
    fmt.Println("Name:", firstName, lastName)
    fmt.Println("Age:", age, "Active:", isActive)
    fmt.Println("x, y:", x, y)
    fmt.Println("name, valid:", name, valid)
}
```

**Output:**
```
a, b, c: 1 2 3
Name: John Doe
Age: 30 Active: true
x, y: 10 20
name, valid: test true
```

### 1.3 Zero Values

В Go все переменные автоматически инициализируются "нулевыми значениями":

```go
package main

import "fmt"

func main() {
    var i int
    var f float64
    var b bool
    var s string
    var p *int
    
    fmt.Printf("int:     %d\n", i)
    fmt.Printf("float64: %f\n", f)
    fmt.Printf("bool:    %t\n", b)
    fmt.Printf("string:  %q\n", s)  // %q показывает кавычки
    fmt.Printf("pointer: %v\n", p)
}
```

**Output:**
```
int:     0
float64: 0.000000
bool:    false
string:  ""
pointer: <nil>
```

**Таблица Zero Values:**

| Тип | Zero Value |
|-----|------------|
| `int`, `int8`, `int16`, `int32`, `int64` | `0` |
| `uint`, `uint8`, `uint16`, `uint32`, `uint64` | `0` |
| `float32`, `float64` | `0.0` |
| `bool` | `false` |
| `string` | `""` (пустая строка) |
| `pointer`, `slice`, `map`, `channel`, `function`, `interface` | `nil` |

> **💡 Pro Tip:**  
> Go намеренно использует zero values вместо неинициализированной памяти. Это делает программы более предсказуемыми и безопасными.

---

## 2. Базовые типы данных

### 2.1 Числовые типы

**Целые числа:**

```go
package main

import "fmt"

func main() {
    // Знаковые целые
    var i8 int8 = 127              // -128 to 127
    var i16 int16 = 32767          // -32768 to 32767
    var i32 int32 = 2147483647     // -2^31 to 2^31-1
    var i64 int64 = 9223372036854775807 // -2^63 to 2^63-1
    var i int = 42                 // Платформозависимый (32 или 64 бит)
    
    // Беззнаковые целые
    var u8 uint8 = 255             // 0 to 255 (byte — алиас для uint8)
    var u16 uint16 = 65535
    var u32 uint32 = 4294967295
    var u64 uint64 = 18446744073709551615
    var u uint = 42                // Платформозависимый
    
    fmt.Println("int8:", i8)
    fmt.Println("int:", i)
    fmt.Println("uint8 (byte):", u8)
    fmt.Println("uint64:", u64)
}
```

**Output:**
```
int8: 127
int: 42
uint8 (byte): 255
uint64: 18446744073709551615
```

**Числа с плавающей точкой:**

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    var f32 float32 = 3.14159
    var f64 float64 = 3.141592653589793
    
    // float64 — тип по умолчанию для дробных литералов
    pi := 3.14159
    
    // Научная нотация
    avogadro := 6.022e23
    planck := 6.626e-34
    
    fmt.Printf("float32: %.5f\n", f32)
    fmt.Printf("float64: %.15f\n", f64)
    fmt.Printf("pi type: %T\n", pi)
    fmt.Printf("Avogadro: %e\n", avogadro)
    fmt.Printf("Planck: %e\n", planck)
    fmt.Printf("Max float64: %e\n", math.MaxFloat64)
}
```

**Output:**
```
float32: 3.14159
float64: 3.141592653589793
pi type: float64
Avogadro: 6.022000e+23
Planck: 6.626000e-34
Max float64: 1.797693e+308
```

**Комплексные числа:**

```go
package main

import "fmt"

func main() {
    var c64 complex64 = 3 + 4i
    var c128 complex128 = 3.0 + 4.0i
    
    // Встроенные функции
    c := complex(3, 4)  // Создание комплексного числа
    r := real(c)        // Реальная часть
    i := imag(c)        // Мнимая часть
    
    fmt.Printf("c64: %v\n", c64)
    fmt.Printf("c128: %v\n", c128)
    fmt.Printf("c: %v, real: %.1f, imag: %.1f\n", c, r, i)
}
```

**Output:**
```
c64: (3+4i)
c128: (3+4i)
c: (3+4i), real: 3.0, imag: 4.0
```

### 2.2 Boolean

```go
package main

import "fmt"

func main() {
    var active bool = true
    var deleted bool = false
    var enabled bool  // zero value = false
    
    // Результат сравнения — bool
    x := 10
    isPositive := x > 0
    isZero := x == 0
    
    fmt.Println("active:", active)
    fmt.Println("deleted:", deleted)
    fmt.Println("enabled:", enabled)
    fmt.Println("isPositive:", isPositive)
    fmt.Println("isZero:", isZero)
}
```

**Output:**
```
active: true
deleted: false
enabled: false
isPositive: true
isZero: false
```

### 2.3 Строки

```go
package main

import "fmt"

func main() {
    // Строки в двойных кавычках (интерпретируемые)
    s1 := "Hello, World!"
    s2 := "Line1\nLine2\tTabbed"
    
    // Сырые строки в обратных кавычках (raw strings)
    s3 := `This is a
multiline
raw string`
    
    s4 := `Path: C:\Users\name`  // Без экранирования
    
    // Длина строки в байтах
    fmt.Println("s1:", s1)
    fmt.Println("s1 length:", len(s1))
    fmt.Println()
    fmt.Println("s2:", s2)
    fmt.Println()
    fmt.Println("s3:", s3)
    fmt.Println()
    fmt.Println("s4:", s4)
}
```

**Output:**
```
s1: Hello, World!
s1 length: 13

s2: Line1
Line2	Tabbed

s3: This is a
multiline
raw string

s4: Path: C:\Users\name
```

**Работа с Unicode:**

```go
package main

import (
    "fmt"
    "unicode/utf8"
)

func main() {
    s := "Привет, 世界! 🌍"
    
    fmt.Println("Строка:", s)
    fmt.Println("len() (байты):", len(s))
    fmt.Println("Количество рун:", utf8.RuneCountInString(s))
    
    // Итерация по рунам
    fmt.Println("\nПосимвольно:")
    for i, r := range s {
        fmt.Printf("  index: %2d, rune: %c, code: %U\n", i, r, r)
    }
}
```

**Output:**
```
Строка: Привет, 世界! 🌍
len() (байты): 29
Количество рун: 14

Посимвольно:
  index:  0, rune: П, code: U+041F
  index:  2, rune: р, code: U+0440
  index:  4, rune: и, code: U+0438
  index:  6, rune: в, code: U+0432
  index:  8, rune: е, code: U+0435
  index: 10, rune: т, code: U+0442
  index: 12, rune: ,, code: U+002C
  index: 13, rune:  , code: U+0020
  index: 14, rune: 世, code: U+4E16
  index: 17, rune: 界, code: U+754C
  index: 20, rune: !, code: U+0021
  index: 21, rune:  , code: U+0020
  index: 22, rune: 🌍, code: U+1F30D
```

> **⚠️ Warning:**  
> `len(s)` возвращает длину в байтах, не в символах! Для Unicode используйте `utf8.RuneCountInString()`.

### 2.4 Rune и Byte

```go
package main

import "fmt"

func main() {
    // byte — алиас для uint8
    var b byte = 'A'  // ASCII значение
    
    // rune — алиас для int32 (Unicode code point)
    var r rune = 'Я'
    
    fmt.Printf("byte 'A': %d (%c)\n", b, b)
    fmt.Printf("rune 'Я': %d (%c) %U\n", r, r, r)
    
    // Строка как слайс байтов
    s := "Go"
    fmt.Printf("s[0]: %d (%c)\n", s[0], s[0])
    fmt.Printf("s[1]: %d (%c)\n", s[1], s[1])
}
```

**Output:**
```
byte 'A': 65 (A)
rune 'Я': 1071 (Я) U+042F
s[0]: 71 (G)
s[1]: 111 (o)
```

---

## 3. Константы

### 3.1 Базовые константы

```go
package main

import "fmt"

const Pi = 3.14159
const MaxSize = 1000

const (
    StatusOK       = 200
    StatusNotFound = 404
    StatusError    = 500
)

// Константа с явным типом
const TypedConst int64 = 9223372036854775807

func main() {
    fmt.Println("Pi:", Pi)
    fmt.Println("MaxSize:", MaxSize)
    fmt.Println("StatusOK:", StatusOK)
    fmt.Println("TypedConst:", TypedConst)
}
```

**Output:**
```
Pi: 3.14159
MaxSize: 1000
StatusOK: 200
TypedConst: 9223372036854775807
```

### 3.2 Untyped Constants

Константы в Go могут быть "нетипизированными" — их тип определяется контекстом:

```go
package main

import "fmt"

const big = 1e100  // Нетипизированная константа

func main() {
    // Нетипизированная константа адаптируется к типу
    var f32 float32 = big / 1e90  // Работает!
    var f64 float64 = big / 1e90  // Работает!
    
    fmt.Println("f32:", f32)
    fmt.Println("f64:", f64)
    
    // Константы могут иметь бо́льшую точность
    const exactPi = 3.14159265358979323846264338327950288
    var pi32 float32 = exactPi
    var pi64 float64 = exactPi
    
    fmt.Printf("pi32: %.20f\n", pi32)
    fmt.Printf("pi64: %.20f\n", pi64)
}
```

**Output:**
```
f32: 10000000000
f64: 10000000000
pi32: 3.14159274101257324219
pi64: 3.14159265358979311600
```

### 3.3 iota — Генератор констант

```go
package main

import "fmt"

// iota начинается с 0 и увеличивается на 1
const (
    Sunday = iota  // 0
    Monday         // 1
    Tuesday        // 2
    Wednesday      // 3
    Thursday       // 4
    Friday         // 5
    Saturday       // 6
)

// Пропуск значения с blank identifier
const (
    _ = iota       // 0 (пропущено)
    KB = 1 << (10 * iota)  // 1 << 10 = 1024
    MB                      // 1 << 20 = 1048576
    GB                      // 1 << 30 = 1073741824
    TB                      // 1 << 40
)

// Битовые флаги
const (
    FlagRead  = 1 << iota  // 1
    FlagWrite              // 2
    FlagExec               // 4
)

func main() {
    fmt.Println("Days:")
    fmt.Println("  Sunday:", Sunday, "Saturday:", Saturday)
    
    fmt.Println("\nSizes:")
    fmt.Println("  KB:", KB)
    fmt.Println("  MB:", MB)
    fmt.Println("  GB:", GB)
    
    fmt.Println("\nFlags:")
    fmt.Println("  Read:", FlagRead)
    fmt.Println("  Write:", FlagWrite)
    fmt.Println("  Exec:", FlagExec)
    fmt.Println("  Read+Write:", FlagRead|FlagWrite)
}
```

**Output:**
```
Days:
  Sunday: 0 Saturday: 6

Sizes:
  KB: 1024
  MB: 1048576
  GB: 1073741824

Flags:
  Read: 1
  Write: 2
  Exec: 4
  Read+Write: 3
```

> **💡 Pro Tip:**  
> iota сбрасывается в 0 в каждом новом блоке `const`. Это позволяет создавать независимые наборы констант.

---

## 4. Операторы

### 4.1 Арифметические операторы

```go
package main

import "fmt"

func main() {
    a, b := 17, 5
    
    fmt.Printf("%d + %d = %d\n", a, b, a+b)   // Сложение
    fmt.Printf("%d - %d = %d\n", a, b, a-b)   // Вычитание
    fmt.Printf("%d * %d = %d\n", a, b, a*b)   // Умножение
    fmt.Printf("%d / %d = %d\n", a, b, a/b)   // Целочисленное деление
    fmt.Printf("%d %% %d = %d\n", a, b, a%b)  // Остаток от деления
    
    // Деление с плавающей точкой
    x, y := 17.0, 5.0
    fmt.Printf("%.1f / %.1f = %.2f\n", x, y, x/y)
    
    // Инкремент и декремент (только как statement, не expression!)
    c := 10
    c++
    fmt.Println("c++ =", c)
    c--
    fmt.Println("c-- =", c)
}
```

**Output:**
```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3
17 % 5 = 2
17.0 / 5.0 = 3.40
c++ = 11
c-- = 10
```

> **⚠️ Warning:**  
> В Go `i++` и `i--` — это statements, не expressions. Нельзя писать `x = i++` или `if i++ > 0`.

### 4.2 Операторы сравнения

```go
package main

import "fmt"

func main() {
    a, b := 10, 20
    
    fmt.Printf("%d == %d: %t\n", a, b, a == b)  // Равно
    fmt.Printf("%d != %d: %t\n", a, b, a != b)  // Не равно
    fmt.Printf("%d < %d: %t\n", a, b, a < b)    // Меньше
    fmt.Printf("%d > %d: %t\n", a, b, a > b)    // Больше
    fmt.Printf("%d <= %d: %t\n", a, b, a <= b)  // Меньше или равно
    fmt.Printf("%d >= %d: %t\n", a, b, a >= b)  // Больше или равно
    
    // Сравнение строк (лексикографическое)
    s1, s2 := "apple", "banana"
    fmt.Printf("%q < %q: %t\n", s1, s2, s1 < s2)
}
```

**Output:**
```
10 == 20: false
10 != 20: true
10 < 20: true
10 > 20: false
10 <= 20: true
10 >= 20: false
"apple" < "banana": true
```

### 4.3 Логические операторы

```go
package main

import "fmt"

func main() {
    a, b := true, false
    
    fmt.Printf("%t && %t = %t\n", a, b, a && b)  // AND
    fmt.Printf("%t || %t = %t\n", a, b, a || b)  // OR
    fmt.Printf("!%t = %t\n", a, !a)              // NOT
    
    // Короткое замыкание (short-circuit evaluation)
    x := 0
    // Вторая часть не выполнится, если первая false
    if x != 0 && 10/x > 1 {
        fmt.Println("Won't print")
    }
    
    // Вторая часть не выполнится, если первая true
    if x == 0 || someFunc() {
        fmt.Println("Short-circuit works!")
    }
}

func someFunc() bool {
    fmt.Println("someFunc called")
    return true
}
```

**Output:**
```
true && false = false
true || false = true
!true = false
Short-circuit works!
```

### 4.4 Побитовые операторы

```go
package main

import "fmt"

func main() {
    a, b := 0b1100, 0b1010  // 12 и 10 в двоичной системе
    
    fmt.Printf("a = %04b (%d)\n", a, a)
    fmt.Printf("b = %04b (%d)\n", b, b)
    fmt.Println()
    
    fmt.Printf("a & b  (AND) = %04b (%d)\n", a&b, a&b)
    fmt.Printf("a | b  (OR)  = %04b (%d)\n", a|b, a|b)
    fmt.Printf("a ^ b  (XOR) = %04b (%d)\n", a^b, a^b)
    fmt.Printf("a &^ b (AND NOT) = %04b (%d)\n", a&^b, a&^b)
    fmt.Println()
    
    // Битовые сдвиги
    c := 1
    fmt.Printf("1 << 4 = %d\n", c<<4)   // Сдвиг влево (умножение на 2^4)
    fmt.Printf("16 >> 2 = %d\n", 16>>2) // Сдвиг вправо (деление на 2^2)
}
```

**Output:**
```
a = 1100 (12)
b = 1010 (10)

a & b  (AND) = 1000 (8)
a | b  (OR)  = 1110 (14)
a ^ b  (XOR) = 0110 (6)
a &^ b (AND NOT) = 0100 (4)

1 << 4 = 16
16 >> 2 = 4
```

### 4.5 Операторы присваивания

```go
package main

import "fmt"

func main() {
    x := 10
    
    x += 5   // x = x + 5
    fmt.Println("x += 5:", x)
    
    x -= 3   // x = x - 3
    fmt.Println("x -= 3:", x)
    
    x *= 2   // x = x * 2
    fmt.Println("x *= 2:", x)
    
    x /= 4   // x = x / 4
    fmt.Println("x /= 4:", x)
    
    x %= 2   // x = x % 2
    fmt.Println("x %= 2:", x)
    
    // Побитовые операторы присваивания
    y := 0b1111
    y &= 0b1010
    fmt.Printf("y &= 0b1010: %04b\n", y)
    
    y |= 0b0001
    fmt.Printf("y |= 0b0001: %04b\n", y)
}
```

**Output:**
```
x += 5: 15
x -= 3: 12
x *= 2: 24
x /= 4: 6
x %= 2: 0
y &= 0b1010: 1010
y |= 0b0001: 1011
```

---

## 5. Преобразование типов

### 5.1 Явное преобразование

Go требует явного преобразования между типами:

```go
package main

import "fmt"

func main() {
    // int -> float64
    var i int = 42
    var f float64 = float64(i)
    fmt.Printf("int %d -> float64 %f\n", i, f)
    
    // float64 -> int (отбрасывает дробную часть)
    var pi float64 = 3.99
    var intPi int = int(pi)
    fmt.Printf("float64 %f -> int %d\n", pi, intPi)
    
    // int -> string (это НЕ то, что вы думаете!)
    var n int = 65
    var s string = string(n)  // Получаем символ с кодом 65
    fmt.Printf("int %d -> string %q (code point!)\n", n, s)
    
    // Правильное преобразование числа в строку
    import_strconv := fmt.Sprintf("%d", n)
    fmt.Printf("int %d -> string %q (correct)\n", n, import_strconv)
}
```

**Output:**
```
int 42 -> float64 42.000000
float64 3.990000 -> int 3
int 65 -> string "A" (code point!)
int 65 -> string "65" (correct)
```

### 5.2 Преобразование строк

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    // string -> int
    s := "42"
    i, err := strconv.Atoi(s)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Printf("string %q -> int %d\n", s, i)
    }
    
    // int -> string
    n := 123
    str := strconv.Itoa(n)
    fmt.Printf("int %d -> string %q\n", n, str)
    
    // string -> float64
    sf := "3.14159"
    f, _ := strconv.ParseFloat(sf, 64)
    fmt.Printf("string %q -> float64 %f\n", sf, f)
    
    // float64 -> string
    fv := 2.71828
    fs := strconv.FormatFloat(fv, 'f', 4, 64)
    fmt.Printf("float64 %f -> string %q\n", fv, fs)
    
    // string -> bool
    sb := "true"
    b, _ := strconv.ParseBool(sb)
    fmt.Printf("string %q -> bool %t\n", sb, b)
}
```

**Output:**
```
string "42" -> int 42
int 123 -> string "123"
string "3.14159" -> float64 3.141590
float64 2.718280 -> string "2.7183"
string "true" -> bool true
```

> **⚠️ Warning:**  
> `string(65)` не даёт "65", а даёт "A" (символ с Unicode code point 65). Используйте `strconv.Itoa()` для преобразования чисел в строки.

---

## 6. Область видимости

### 6.1 Package-level vs Local

```go
package main

import "fmt"

// Package-level переменная (видна во всём пакете)
var globalVar = "I'm global"

// Package-level константа
const GlobalConst = 100

func main() {
    // Локальная переменная (видна только в main)
    localVar := "I'm local"
    
    fmt.Println(globalVar)
    fmt.Println(localVar)
    fmt.Println(GlobalConst)
    
    showGlobal()
}

func showGlobal() {
    fmt.Println("From showGlobal:", globalVar)
    // fmt.Println(localVar) // Ошибка! localVar не видна здесь
}
```

**Output:**
```
I'm global
I'm local
100
From showGlobal: I'm global
```

### 6.2 Shadowing (затенение)

```go
package main

import "fmt"

var x = "global"

func main() {
    fmt.Println("1:", x)  // global
    
    x := "main-local"     // Новая переменная x, затеняет глобальную
    fmt.Println("2:", x)  // main-local
    
    {
        x := "block-local"  // Ещё одна x, затеняет main-local
        fmt.Println("3:", x)  // block-local
    }
    
    fmt.Println("4:", x)  // main-local (block-local вышла из области видимости)
}
```

**Output:**
```
1: global
2: main-local
3: block-local
4: main-local
```

> **⚠️ Warning:**  
> Shadowing — частый источник багов! Будьте внимательны с `:=` внутри блоков.

---

## 7. Числовые литералы

### 7.1 Разные системы счисления

```go
package main

import "fmt"

func main() {
    // Десятичная (по умолчанию)
    dec := 42
    
    // Двоичная (0b или 0B)
    bin := 0b101010  // = 42
    
    // Восьмеричная (0o или 0O, или просто 0)
    oct := 0o52      // = 42
    
    // Шестнадцатеричная (0x или 0X)
    hex := 0x2A      // = 42
    
    fmt.Printf("dec: %d\n", dec)
    fmt.Printf("bin: 0b%b = %d\n", bin, bin)
    fmt.Printf("oct: 0o%o = %d\n", oct, oct)
    fmt.Printf("hex: 0x%X = %d\n", hex, hex)
}
```

**Output:**
```
dec: 42
bin: 0b101010 = 42
oct: 0o52 = 42
hex: 0x2A = 42
```

### 7.2 Разделители для читаемости

Go 1.13+ позволяет использовать `_` как разделитель в числовых литералах:

```go
package main

import "fmt"

func main() {
    billion := 1_000_000_000
    creditCard := 1234_5678_9012_3456
    hexColor := 0xFF_FF_FF
    binary := 0b1111_0000_1111_0000
    
    fmt.Println("Billion:", billion)
    fmt.Println("Card:", creditCard)
    fmt.Printf("Color: #%06X\n", hexColor)
    fmt.Printf("Binary: %016b\n", binary)
}
```

**Output:**
```
Billion: 1000000000
Card: 1234567890123456
Color: #FFFFFF
Binary: 1111000011110000
```

---

## 8. Common Pitfalls

### 8.1 Деление целых чисел

❌ **Проблема:**
```go
package main

import "fmt"

func main() {
    result := 5 / 2
    fmt.Println(result)  // 2, не 2.5!
}
```

✅ **Решение:**
```go
package main

import "fmt"

func main() {
    result := 5.0 / 2.0
    fmt.Println(result)  // 2.5
    
    // Или явное преобразование
    a, b := 5, 2
    result2 := float64(a) / float64(b)
    fmt.Println(result2)  // 2.5
}
```

### 8.2 Переполнение чисел

```go
package main

import "fmt"

func main() {
    var i8 int8 = 127
    i8++  // Переполнение! Без ошибки!
    fmt.Println("int8 overflow:", i8)  // -128
    
    var u8 uint8 = 255
    u8++  // Переполнение!
    fmt.Println("uint8 overflow:", u8)  // 0
}
```

**Output:**
```
int8 overflow: -128
uint8 overflow: 0
```

### 8.3 Сравнение float

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    a := 0.1 + 0.2
    b := 0.3
    
    // Неправильно!
    fmt.Println("0.1 + 0.2 == 0.3:", a == b)  // false!
    fmt.Printf("0.1 + 0.2 = %.17f\n", a)
    fmt.Printf("0.3      = %.17f\n", b)
    
    // Правильно — сравнение с погрешностью
    epsilon := 1e-9
    fmt.Println("With epsilon:", math.Abs(a-b) < epsilon)
}
```

**Output:**
```
0.1 + 0.2 == 0.3: false
0.1 + 0.2 = 0.30000000000000004
0.3      = 0.29999999999999999
With epsilon: true
```

---

## 💡 Key Takeaways

- **Zero Values**: Все переменные в Go автоматически инициализируются нулевыми значениями. Это делает код безопаснее.

- **Статическая типизация**: Go требует явного преобразования типов. `float64(x)` для преобразования int в float64.

- **Короткое объявление `:=`**: Используется только внутри функций. `var` нужен для package-level переменных.

- **iota**: Мощный инструмент для создания последовательных констант и битовых флагов.

- **Строки — UTF-8**: `len(s)` возвращает байты, не символы. Используйте `range` или `utf8.RuneCountInString()` для работы с рунами.

---

## 🚀 Next Steps

**Related Modules:**
- [03_FlowControl](../03_FlowControl/) — условия, циклы, defer
- [04_Functions](../04_Functions/) — функции и замыкания
- [05_DataStructures](../05_DataStructures/) — массивы, слайсы, мапы

**Practice Ideas:**
1. Создайте конвертер температур (Цельсий ↔ Фаренгейт)
2. Напишите программу расчёта возраста по году рождения
3. Поэкспериментируйте с iota для создания констант дней недели и месяцев
4. Напишите калькулятор, обрабатывающий разные типы чисел

**Going Deeper:**
- Изучите пакет `math` для математических операций
- Изучите пакет `strconv` для преобразований
- Прочитайте о IEEE 754 для понимания чисел с плавающей точкой

---

