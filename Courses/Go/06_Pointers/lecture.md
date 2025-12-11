# Pointers
## Указатели, значения vs ссылки, new vs make

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые типы данных Go
- Знать структуры и функции
- Иметь опыт работы со слайсами и мапами

**Recommended prior modules:**

- [02_Basics](../02_Basics/) — типы данных
- [05_DataStructures](../05_DataStructures/) — слайсы и структуры

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать указатели и их применение
- Различать передачу по значению и по ссылке
- Использовать операторы & и *
- Выбирать между new и make
- Применять указатели для модификации данных

---

## 1. Основы указателей

### 1.1 Что такое указатель

Указатель хранит адрес памяти другой переменной:

```go

package main

import "fmt"

func main() {
    x := 42
    
    // & — получить адрес переменной
    p := &x
    
    fmt.Println("Значение x:", x)
    fmt.Println("Адрес x:", p)
    fmt.Printf("Тип p: %T\n", p)
    
    // * — получить значение по адресу (разыменование)
    fmt.Println("Значение по адресу p:", *p)
    
    // Изменение через указатель
    *p = 100
    fmt.Println("x после *p = 100:", x)
}

```

**Output:**
```

Значение x: 42
Адрес x: 0xc0000a6010
Тип p: *int
Значение по адресу p: 42
x после *p = 100: 100

```

### 1.2 Операторы & и *

```go

package main

import "fmt"

func main() {
    value := 10
    
    // & — адрес
    pointer := &value
    fmt.Printf("value: %d, адрес: %p\n", value, pointer)
    
    // * — разыменование
    fmt.Printf("*pointer: %d\n", *pointer)
    
    // Изменение
    *pointer = 20
    fmt.Printf("После *pointer = 20: value = %d\n", value)
    
    // Цепочка
    pp := &pointer  // Указатель на указатель
    fmt.Printf("**pp = %d\n", **pp)
}

```

**Output:**
```

value: 10, адрес: 0xc0000a6010
*pointer: 10
После *pointer = 20: value = 20
**pp = 20

```

### 1.3 Zero value для указателей

```go

package main

import "fmt"

func main() {
    var p *int  // nil pointer
    
    fmt.Println("p:", p)
    fmt.Println("p == nil:", p == nil)
    
    // Разыменование nil — panic!
    // fmt.Println(*p)  // panic: runtime error
    
    // Безопасная проверка
    if p != nil {
        fmt.Println(*p)
    } else {
        fmt.Println("p is nil, cannot dereference")
    }
}

```

**Output:**
```

p: <nil>
p == nil: true
p is nil, cannot dereference

```

---

## 2. Передача по значению vs по указателю

### 2.1 Передача по значению

```go

package main

import "fmt"

func double(x int) {
    x = x * 2  // Изменяем копию!
    fmt.Println("Inside double:", x)
}

func main() {
    n := 10
    double(n)
    fmt.Println("After double:", n)  // Не изменился!
}

```

**Output:**
```

Inside double: 20
After double: 10

```

### 2.2 Передача по указателю

```go

package main

import "fmt"

func double(p *int) {
    *p = *p * 2  // Изменяем оригинал!
}

func main() {
    n := 10
    double(&n)
    fmt.Println("After double:", n)  // Изменился!
}

```

**Output:**
```

After double: 20

```

### 2.3 Практический пример

```go

package main

import "fmt"

type User struct {
    Name  string
    Score int
}

// Получает копию — не может модифицировать
func updateScoreBad(u User, delta int) {
    u.Score += delta
}

// Получает указатель — может модифицировать
func updateScore(u *User, delta int) {
    u.Score += delta
}

func main() {
    user := User{Name: "Alice", Score: 100}
    
    updateScoreBad(user, 50)
    fmt.Println("After updateScoreBad:", user.Score)  // 100
    
    updateScore(&user, 50)
    fmt.Println("After updateScore:", user.Score)     // 150
}

```

**Output:**
```

After updateScoreBad: 100
After updateScore: 150

```

---

## 3. Указатели на структуры

### 3.1 Автоматическое разыменование

```go

package main

import "fmt"

type Point struct {
    X, Y int
}

func main() {
    p := Point{X: 10, Y: 20}
    ptr := &p
    
    // Оба варианта эквивалентны
    fmt.Println("(*ptr).X:", (*ptr).X)
    fmt.Println("ptr.X:", ptr.X)  // Go автоматически разыменовывает!
    
    // Модификация
    ptr.X = 100
    fmt.Println("After ptr.X = 100:", p)
}

```

**Output:**
```

(*ptr).X: 10
ptr.X: 10
After ptr.X = 100: {100 20}

```

### 3.2 Создание указателя на структуру

```go

package main

import "fmt"

type Config struct {
    Host string
    Port int
}

func main() {
    // Способ 1: & от значения
    c1 := Config{Host: "localhost", Port: 8080}
    p1 := &c1
    
    // Способ 2: & от литерала (идиоматично)
    p2 := &Config{Host: "localhost", Port: 8080}
    
    // Способ 3: new (возвращает *T)
    p3 := new(Config)
    p3.Host = "localhost"
    p3.Port = 8080
    
    fmt.Printf("p1: %+v\n", *p1)
    fmt.Printf("p2: %+v\n", *p2)
    fmt.Printf("p3: %+v\n", *p3)
}

```

**Output:**
```

p1: {Host:localhost Port:8080}
p2: {Host:localhost Port:8080}
p3: {Host:localhost Port:8080}

```

---

## 4. new vs make

### 4.1 new

`new(T)` выделяет память и возвращает `*T` с zero value:

```go

package main

import "fmt"

func main() {
    // new для простых типов
    pi := new(int)
    fmt.Printf("pi: %v, *pi: %d\n", pi, *pi)
    
    *pi = 42
    fmt.Printf("After *pi = 42: %d\n", *pi)
    
    // new для структур
    type Person struct {
        Name string
        Age  int
    }
    
    p := new(Person)
    fmt.Printf("new(Person): %+v\n", *p)
    
    p.Name = "Alice"
    p.Age = 30
    fmt.Printf("After init: %+v\n", *p)
}

```

**Output:**
```

pi: 0xc0000a6010, *pi: 0
After *pi = 42: 42
new(Person): {Name: Age:0}
After init: {Name:Alice Age:30}

```

### 4.2 make

`make(T, ...)` только для slice, map, channel:

```go

package main

import "fmt"

func main() {
    // make для slice
    s := make([]int, 5, 10)
    fmt.Printf("slice: %v, len: %d, cap: %d\n", s, len(s), cap(s))
    
    // make для map
    m := make(map[string]int)
    m["one"] = 1
    fmt.Printf("map: %v\n", m)
    
    // make для channel
    ch := make(chan int, 5)
    fmt.Printf("channel: %v, cap: %d\n", ch, cap(ch))
    
    // new для slice — создаёт указатель на nil slice!
    sp := new([]int)
    fmt.Printf("new([]int): %v, is nil: %t\n", *sp, *sp == nil)
}

```

**Output:**
```

slice: [0 0 0 0 0], len: 5, cap: 10
map: map[one:1]
channel: 0xc00006c060, cap: 5
new([]int): [], is nil: true

```

### 4.3 Сравнение new и make

| Характеристика | new(T) | make(T, ...) |
|----------------|--------|--------------|
| Возвращает | `*T` | `T` |
| Применимо к | Любой тип | slice, map, channel |
| Инициализация | Zero value | Инициализированная структура |
| Пример | `new(int)` → `*int` | `make([]int, 5)` → `[]int` |

```go

package main

import "fmt"

func main() {
    // new создаёт указатель на zero value
    s1 := new([]int)
    fmt.Printf("new([]int): type=%T, value=%v, nil=%t\n", s1, *s1, *s1 == nil)
    
    // make создаёт инициализированный слайс
    s2 := make([]int, 0)
    fmt.Printf("make([]int, 0): type=%T, value=%v, nil=%t\n", s2, s2, s2 == nil)
}

```

**Output:**
```

new([]int): type=*[]int, value=[], nil=true
make([]int, 0): type=[]int, value=[], nil=false

```

---

## 5. Указатели и методы

### 5.1 Value receiver vs Pointer receiver

```go

package main

import "fmt"

type Counter struct {
    value int
}

// Value receiver — работает с копией
func (c Counter) IncrementBad() {
    c.value++  // Изменяем копию!
}

// Pointer receiver — работает с оригиналом
func (c *Counter) Increment() {
    c.value++  // Изменяем оригинал
}

func (c Counter) Value() int {
    return c.value
}

func main() {
    c := Counter{value: 0}
    
    c.IncrementBad()
    fmt.Println("After IncrementBad:", c.Value())
    
    c.Increment()
    fmt.Println("After Increment:", c.Value())
    
    // Go автоматически преобразует c в &c при вызове
    c.Increment()  // Эквивалентно (&c).Increment()
    fmt.Println("After second Increment:", c.Value())
}

```

**Output:**
```

After IncrementBad: 0
After Increment: 1
After second Increment: 2

```

### 5.2 Правило консистентности

```go

package main

import "fmt"

type Rectangle struct {
    Width, Height float64
}

// Если один метод использует pointer receiver,
// все методы должны использовать pointer receiver
func (r *Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

func (r *Rectangle) String() string {
    return fmt.Sprintf("Rectangle(%.1f x %.1f)", r.Width, r.Height)
}

func main() {
    r := Rectangle{Width: 10, Height: 5}
    fmt.Println("Initial:", r.String())
    fmt.Println("Area:", r.Area())
    
    r.Scale(2)
    fmt.Println("After Scale(2):", r.String())
    fmt.Println("Area:", r.Area())
}

```

**Output:**
```

Initial: Rectangle(10.0 x 5.0)
Area: 50
After Scale(2): Rectangle(20.0 x 10.0)
Area: 200

```

---

## 6. Когда использовать указатели

### 6.1 Рекомендации

**Используйте указатели когда:**

- Нужно модифицировать значение
- Структура большая (избежать копирования)
- Все методы используют pointer receiver
- Работа с nil имеет смысл

**Используйте значения когда:**

- Данные маленькие и неизменяемые
- Нужна копия (изоляция)
- Работа с map ключами (должны быть сравнимы)

```go

package main

import "fmt"

// Маленькая неизменяемая структура — значение
type Point struct {
    X, Y int
}

// Большая или изменяемая структура — указатель
type User struct {
    ID        int
    Name      string
    Email     string
    Settings  map[string]string
    History   []string
}

func NewUser(id int, name, email string) *User {
    return &User{
        ID:       id,
        Name:     name,
        Email:    email,
        Settings: make(map[string]string),
        History:  make([]string, 0),
    }
}

func (u *User) AddHistory(entry string) {
    u.History = append(u.History, entry)
}

func main() {
    // Point — по значению
    p1 := Point{1, 2}
    p2 := p1
    p2.X = 100
    fmt.Println("p1:", p1)  // Не изменился
    fmt.Println("p2:", p2)
    
    // User — по указателю
    user := NewUser(1, "Alice", "alice@example.com")
    user.AddHistory("login")
    user.AddHistory("view_page")
    fmt.Printf("User: %+v\n", user)
}

```

**Output:**
```

p1: {1 2}
p2: {100 2}
User: &{ID:1 Name:Alice Email:alice@example.com Settings:map[] History:[login view_page]}

```

---

## 7. Указатели и слайсы/мапы

### 7.1 Слайсы уже содержат указатель

```go

package main

import "fmt"

func modifySlice(s []int) {
    s[0] = 999  // Модифицирует оригинал!
}

func appendToSlice(s []int) []int {
    return append(s, 100)  // Может создать новый underlying array
}

func main() {
    nums := []int{1, 2, 3}
    
    modifySlice(nums)
    fmt.Println("After modifySlice:", nums)
    
    // append требует возврата!
    nums = appendToSlice(nums)
    fmt.Println("After appendToSlice:", nums)
}

```

**Output:**
```

After modifySlice: [999 2 3]
After appendToSlice: [999 2 3 100]

```

### 7.2 Указатель на слайс (редко нужно)

```go

package main

import "fmt"

func appendViaPointer(sp *[]int, value int) {
    *sp = append(*sp, value)
}

func main() {
    nums := []int{1, 2, 3}
    
    appendViaPointer(&nums, 4)
    appendViaPointer(&nums, 5)
    
    fmt.Println("Result:", nums)
}

```

**Output:**
```

Result: [1 2 3 4 5]

```

---

## 8. Common Pitfalls

### 8.1 Разыменование nil

```go

package main

import "fmt"

type Config struct {
    Host string
}

func getConfig() *Config {
    return nil  // Нет конфигурации
}

func main() {
    cfg := getConfig()
    
    // Плохо — panic если nil
    // fmt.Println(cfg.Host)
    
    // Хорошо — проверка
    if cfg != nil {
        fmt.Println("Host:", cfg.Host)
    } else {
        fmt.Println("No config available")
    }
}

```

**Output:**
```

No config available

```

### 8.2 Возврат адреса локальной переменной

```go

package main

import "fmt"

// В Go это безопасно! (escape analysis)
func createInt() *int {
    x := 42
    return &x  // Go переместит x в heap
}

func main() {
    p := createInt()
    fmt.Println("Value:", *p)
}

```

**Output:**
```

Value: 42

```

### 8.3 Указатели в циклах

```go

package main

import "fmt"

type Item struct {
    Name string
}

func main() {
    items := []Item{{"a"}, {"b"}, {"c"}}
    
    // НЕПРАВИЛЬНО (до Go 1.22)
    var pointers []*Item
    for _, item := range items {
        pointers = append(pointers, &item)  // Все указывают на одну переменную!
    }
    
    fmt.Println("Wrong:")
    for _, p := range pointers {
        fmt.Println(p.Name)  // Все выведут "c"
    }
    
    // ПРАВИЛЬНО
    pointers = nil
    for i := range items {
        pointers = append(pointers, &items[i])
    }
    
    fmt.Println("Correct:")
    for _, p := range pointers {
        fmt.Println(p.Name)
    }
}

```

**Output:**
```

Wrong:
c
c
c
Correct:
a
b
c

```

---

## 💡 Key Takeaways

- **& получает адрес, * разыменовывает**: `p := &x` и `value := *p`.

- **Указатели для модификации**: Передавайте указатель, если функция должна изменить значение.

- **new vs make**: `new` для указателей на zero value, `make` для slice/map/channel.

- **Go автоматически разыменовывает**: `ptr.Field` эквивалентно `(*ptr).Field`.

- **Слайсы и мапы уже ссылочные**: Не нужен указатель для модификации элементов.

---

## 🚀 Next Steps

**Related Modules:**

- [07_Methods](../07_Methods/) — методы с pointer receiver
- [09_Concurrency](../09_Concurrency/) — безопасность указателей в горутинах

**Practice Ideas:**

1. Создайте функцию swap, меняющую значения через указатели
2. Реализуйте связанный список с указателями
3. Напишите builder pattern с методами на pointer receiver

---




