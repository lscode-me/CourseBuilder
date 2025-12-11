# Data Structures
## Массивы, слайсы, мапы и структуры

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовые типы данных Go
- Понимать функции и циклы
- Уметь работать с for range

**Recommended prior modules:**

- [02_Basics](../02_Basics/) — переменные и типы
- [04_Functions](../04_Functions/) — функции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с массивами фиксированной длины
- Использовать слайсы для динамических коллекций
- Применять мапы для ассоциативных данных
- Создавать и использовать структуры
- Понимать различия между типами данных

---

## 1. Массивы (Arrays)

### 1.1 Определение массива

Массив в Go — последовательность элементов **фиксированной длины**:

```go

package main

import "fmt"

func main() {
    // Объявление с явным размером
    var numbers [5]int
    fmt.Println("Zero values:", numbers)
    
    // Инициализация при объявлении
    primes := [5]int{2, 3, 5, 7, 11}
    fmt.Println("Primes:", primes)
    
    // Автоматический подсчёт размера
    vowels := [...]string{"a", "e", "i", "o", "u"}
    fmt.Println("Vowels:", vowels)
    fmt.Println("Length:", len(vowels))
    
    // Частичная инициализация
    sparse := [5]int{0: 10, 2: 30, 4: 50}
    fmt.Println("Sparse:", sparse)
}

```

**Output:**
```

Zero values: [0 0 0 0 0]
Primes: [2 3 5 7 11]
Vowels: [a e i o u]
Length: 5
Sparse: [10 0 30 0 50]

```

### 1.2 Доступ к элементам

```go

package main

import "fmt"

func main() {
    arr := [5]int{10, 20, 30, 40, 50}
    
    // Доступ по индексу
    fmt.Println("First:", arr[0])
    fmt.Println("Last:", arr[4])
    fmt.Println("Length:", len(arr))
    
    // Модификация
    arr[2] = 300
    fmt.Println("Modified:", arr)
    
    // Итерация
    for i, v := range arr {
        fmt.Printf("arr[%d] = %d\n", i, v)
    }
}

```

**Output:**
```

First: 10
Last: 50
Length: 5
Modified: [10 20 300 40 50]
arr[0] = 10
arr[1] = 20
arr[2] = 300
arr[3] = 40
arr[4] = 50

```

### 1.3 Массивы — это значения

Массивы в Go копируются при присваивании:

```go

package main

import "fmt"

func main() {
    a := [3]int{1, 2, 3}
    b := a  // Копирование!
    
    b[0] = 100
    
    fmt.Println("a:", a)  // [1 2 3] — не изменился!
    fmt.Println("b:", b)  // [100 2 3]
}

```

**Output:**
```

a: [1 2 3]
b: [100 2 3]

```

> **⚠️ Warning:**  
> Размер массива — часть его типа. `[3]int` и `[5]int` — разные типы!

---

## 2. Слайсы (Slices)

### 2.1 Создание слайсов

Слайс — динамическая "обёртка" над массивом:

```go

package main

import "fmt"

func main() {
    // Литерал слайса (без размера)
    nums := []int{1, 2, 3, 4, 5}
    fmt.Println("nums:", nums)
    
    // make(тип, длина, ёмкость)
    a := make([]int, 5)
    fmt.Println("make([]int, 5):", a, "len:", len(a), "cap:", cap(a))
    
    b := make([]int, 3, 10)
    fmt.Println("make([]int, 3, 10):", b, "len:", len(b), "cap:", cap(b))
    
    // nil слайс
    var c []int
    fmt.Println("nil slice:", c, "len:", len(c), "cap:", cap(c), "is nil:", c == nil)
    
    // Пустой слайс (не nil)
    d := []int{}
    fmt.Println("empty slice:", d, "is nil:", d == nil)
}

```

**Output:**
```

nums: [1 2 3 4 5]
make([]int, 5): [0 0 0 0 0] len: 5 cap: 5
make([]int, 3, 10): [0 0 0] len: 3 cap: 10
nil slice: [] len: 0 cap: 0 is nil: true
empty slice: [] is nil: false

```

### 2.2 Слайсинг

```go

package main

import "fmt"

func main() {
    arr := [6]int{0, 1, 2, 3, 4, 5}
    
    // Создание слайса из массива
    s := arr[1:4]  // [1, 2, 3]
    fmt.Println("arr[1:4]:", s)
    
    // Различные срезы
    fmt.Println("arr[:3]:", arr[:3])   // [0, 1, 2]
    fmt.Println("arr[3:]:", arr[3:])   // [3, 4, 5]
    fmt.Println("arr[:]:", arr[:])     // [0, 1, 2, 3, 4, 5]
    
    // Слайсы ссылаются на тот же массив!
    s[0] = 100
    fmt.Println("After s[0] = 100:")
    fmt.Println("  s:", s)
    fmt.Println("  arr:", arr)  // arr тоже изменился!
}

```

**Output:**
```

arr[1:4]: [1 2 3]
arr[:3]: [0 1 2]
arr[3:]: [3 4 5]
arr[:]: [0 1 2 3 4 5]
After s[0] = 100:
  s: [100 2 3]
  arr: [0 100 2 3 4 5]

```

### 2.3 append

```go

package main

import "fmt"

func main() {
    s := []int{1, 2, 3}
    fmt.Printf("Before: %v, len=%d, cap=%d\n", s, len(s), cap(s))
    
    // Добавление элементов
    s = append(s, 4)
    s = append(s, 5, 6, 7)
    fmt.Printf("After: %v, len=%d, cap=%d\n", s, len(s), cap(s))
    
    // Добавление другого слайса
    more := []int{8, 9, 10}
    s = append(s, more...)
    fmt.Printf("Final: %v, len=%d, cap=%d\n", s, len(s), cap(s))
}

```

**Output:**
```

Before: [1 2 3], len=3, cap=3
After: [1 2 3 4 5 6 7], len=7, cap=12
Final: [1 2 3 4 5 6 7 8 9 10], len=10, cap=12

```

> **💡 Pro Tip:**  
> `append` может создать новый underlying array, если capacity недостаточен. Всегда используйте `s = append(s, ...)`.

### 2.4 copy

```go

package main

import "fmt"

func main() {
    src := []int{1, 2, 3, 4, 5}
    dst := make([]int, 3)
    
    // copy возвращает количество скопированных элементов
    n := copy(dst, src)
    fmt.Printf("Copied %d elements: %v\n", n, dst)
    
    // Полная копия
    fullCopy := make([]int, len(src))
    copy(fullCopy, src)
    
    // Теперь fullCopy независим от src
    fullCopy[0] = 100
    fmt.Println("src:", src)
    fmt.Println("fullCopy:", fullCopy)
}

```

**Output:**
```

Copied 3 elements: [1 2 3]
src: [1 2 3 4 5]
fullCopy: [100 2 3 4 5]

```

### 2.5 Удаление элементов

```go

package main

import "fmt"

func main() {
    s := []int{0, 1, 2, 3, 4, 5}
    
    // Удаление элемента по индексу i (сохраняя порядок)
    i := 2
    s = append(s[:i], s[i+1:]...)
    fmt.Println("After removing index 2:", s)
    
    // Удаление без сохранения порядка (быстрее)
    s = []int{0, 1, 2, 3, 4, 5}
    i = 2
    s[i] = s[len(s)-1]  // Заменяем на последний
    s = s[:len(s)-1]    // Укорачиваем
    fmt.Println("Fast delete index 2:", s)
}

```

**Output:**
```

After removing index 2: [0 1 3 4 5]
Fast delete index 2: [0 1 5 3 4]

```

---

## 3. Мапы (Maps)

### 3.1 Создание мап

```go

package main

import "fmt"

func main() {
    // Литерал
    ages := map[string]int{
        "Alice": 30,
        "Bob":   25,
        "Carol": 35,
    }
    fmt.Println("ages:", ages)
    
    // make
    scores := make(map[string]int)
    scores["math"] = 95
    scores["physics"] = 87
    fmt.Println("scores:", scores)
    
    // nil map (только для чтения!)
    var nilMap map[string]int
    fmt.Println("nil map:", nilMap, "is nil:", nilMap == nil)
    // nilMap["key"] = 1  // panic!
}

```

**Output:**
```

ages: map[Alice:30 Bob:25 Carol:35]
scores: map[math:95 physics:87]
nil map: map[] is nil: true

```

### 3.2 Операции с мапами

```go

package main

import "fmt"

func main() {
    m := map[string]int{
        "one":   1,
        "two":   2,
        "three": 3,
    }
    
    // Чтение
    fmt.Println("m[\"one\"]:", m["one"])
    
    // Проверка существования
    value, exists := m["four"]
    fmt.Printf("m[\"four\"]: value=%d, exists=%t\n", value, exists)
    
    // Идиоматическая проверка
    if v, ok := m["two"]; ok {
        fmt.Println("Found two:", v)
    }
    
    // Добавление/обновление
    m["four"] = 4
    m["one"] = 100
    fmt.Println("After update:", m)
    
    // Удаление
    delete(m, "two")
    fmt.Println("After delete:", m)
    
    // Длина
    fmt.Println("Length:", len(m))
}

```

**Output:**
```

m["one"]: 1
m["four"]: value=0, exists=false
Found two: 2
After update: map[four:4 one:100 three:3 two:2]
After delete: map[four:4 one:100 three:3]
Length: 3

```

### 3.3 Итерация по мапе

```go

package main

import "fmt"

func main() {
    capitals := map[string]string{
        "Russia":  "Moscow",
        "Japan":   "Tokyo",
        "Germany": "Berlin",
        "France":  "Paris",
    }
    
    // Порядок итерации не определён!
    for country, capital := range capitals {
        fmt.Printf("%s -> %s\n", country, capital)
    }
    
    // Только ключи
    fmt.Println("\nCountries:")
    for country := range capitals {
        fmt.Println(" ", country)
    }
}

```

**Output:**
```

Russia -> Moscow
Japan -> Tokyo
Germany -> Berlin
France -> Paris

Countries:
  Russia
  Japan
  Germany
  France

```

### 3.4 Мапа как множество (Set)

```go

package main

import "fmt"

func main() {
    // Go не имеет встроенного Set, используем map[T]bool или map[T]struct{}
    set := make(map[string]struct{})
    
    // Добавление
    set["apple"] = struct{}{}
    set["banana"] = struct{}{}
    set["cherry"] = struct{}{}
    
    // Проверка наличия
    if _, exists := set["apple"]; exists {
        fmt.Println("apple is in set")
    }
    
    if _, exists := set["grape"]; !exists {
        fmt.Println("grape is NOT in set")
    }
    
    // Удаление
    delete(set, "banana")
    
    fmt.Println("Set:", set)
}

```

**Output:**
```

apple is in set
grape is NOT in set
Set: map[apple:{} cherry:{}]

```

---

## 4. Структуры (Structs)

### 4.1 Определение структуры

```go

package main

import "fmt"

// Определение типа структуры
type Person struct {
    Name    string
    Age     int
    Email   string
    Active  bool
}

func main() {
    // Создание с именованными полями
    p1 := Person{
        Name:   "Alice",
        Age:    30,
        Email:  "alice@example.com",
        Active: true,
    }
    fmt.Printf("p1: %+v\n", p1)
    
    // Порядковая инициализация (не рекомендуется)
    p2 := Person{"Bob", 25, "bob@example.com", false}
    fmt.Printf("p2: %+v\n", p2)
    
    // Частичная инициализация (остальное — zero values)
    p3 := Person{Name: "Carol"}
    fmt.Printf("p3: %+v\n", p3)
    
    // Пустая структура
    var p4 Person
    fmt.Printf("p4: %+v\n", p4)
}

```

**Output:**
```

p1: {Name:Alice Age:30 Email:alice@example.com Active:true}
p2: {Name:Bob Age:25 Email:bob@example.com Active:false}
p3: {Name:Carol Age:0 Email: Active:false}
p4: {Name: Age:0 Email: Active:false}

```

### 4.2 Доступ к полям

```go

package main

import "fmt"

type Point struct {
    X, Y int
}

func main() {
    p := Point{X: 10, Y: 20}
    
    // Чтение
    fmt.Println("X:", p.X)
    fmt.Println("Y:", p.Y)
    
    // Запись
    p.X = 100
    p.Y = 200
    fmt.Println("Modified:", p)
    
    // Указатель на структуру
    ptr := &p
    ptr.X = 1000  // Автоматическое разыменование
    fmt.Println("Via pointer:", p)
}

```

**Output:**
```

X: 10
Y: 20
Modified: {100 200}
Via pointer: {1000 200}

```

### 4.3 Вложенные структуры

```go

package main

import "fmt"

type Address struct {
    City    string
    Street  string
    ZipCode string
}

type Employee struct {
    Name    string
    Age     int
    Address Address  // Вложенная структура
}

func main() {
    emp := Employee{
        Name: "John",
        Age:  35,
        Address: Address{
            City:    "Moscow",
            Street:  "Tverskaya",
            ZipCode: "123456",
        },
    }
    
    fmt.Printf("%+v\n", emp)
    fmt.Println("City:", emp.Address.City)
}

```

**Output:**
```

{Name:John Age:35 Address:{City:Moscow Street:Tverskaya ZipCode:123456}}
City: Moscow

```

### 4.4 Embedding (Встраивание)

```go

package main

import "fmt"

type Address struct {
    City   string
    Street string
}

type Person struct {
    Name string
    Age  int
    Address  // Встроенная структура (без имени поля)
}

func main() {
    p := Person{
        Name: "Alice",
        Age:  30,
        Address: Address{
            City:   "Tokyo",
            Street: "Shibuya",
        },
    }
    
    // Прямой доступ к полям встроенной структуры
    fmt.Println("Name:", p.Name)
    fmt.Println("City:", p.City)        // Напрямую!
    fmt.Println("Street:", p.Street)    // Напрямую!
    
    // Также доступен через имя типа
    fmt.Println("Address.City:", p.Address.City)
}

```

**Output:**
```

Name: Alice
City: Tokyo
Street: Shibuya
Address.City: Tokyo

```

### 4.5 Теги структур

```go

package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    ID        int    `json:"id"`
    Username  string `json:"username"`
    Email     string `json:"email,omitempty"`
    Password  string `json:"-"`  // Игнорируется при JSON
    CreatedAt string `json:"created_at"`
}

func main() {
    user := User{
        ID:       1,
        Username: "gopher",
        Password: "secret123",
    }
    
    data, _ := json.MarshalIndent(user, "", "  ")
    fmt.Println(string(data))
}

```

**Output:**
```json

{
  "id": 1,
  "username": "gopher",
  "created_at": ""
}

```

---

## 5. Сравнение структур данных

| Характеристика | Array | Slice | Map |
|----------------|-------|-------|-----|
| Размер | Фиксированный | Динамический | Динамический |
| Zero value | [0, 0, ...] | nil | nil |
| Сравнение (==) | Да | Нет | Нет |
| Копирование | По значению | По ссылке | По ссылке |
| Передача в функцию | Копируется | Ссылка | Ссылка |

```go

package main

import "fmt"

func main() {
    // Массивы можно сравнивать
    a1 := [3]int{1, 2, 3}
    a2 := [3]int{1, 2, 3}
    fmt.Println("Arrays equal:", a1 == a2)
    
    // Слайсы нельзя сравнивать (кроме nil)
    s1 := []int{1, 2, 3}
    // s1 == s2  // Ошибка компиляции!
    fmt.Println("Slice is nil:", s1 == nil)
    
    // Структуры можно сравнивать, если все поля сравнимы
    type Point struct{ X, Y int }
    p1 := Point{1, 2}
    p2 := Point{1, 2}
    fmt.Println("Structs equal:", p1 == p2)
}

```

**Output:**
```

Arrays equal: true
Slice is nil: false
Structs equal: true

```

---

## 6. Common Pitfalls

### 6.1 Модификация слайса в функции

```go

package main

import "fmt"

func addElement(s []int) {
    s = append(s, 100)  // Может создать новый массив!
    fmt.Println("Inside:", s)
}

func addElementCorrect(s []int) []int {
    return append(s, 100)
}

func main() {
    nums := []int{1, 2, 3}
    
    addElement(nums)
    fmt.Println("After addElement:", nums)  // Не изменился!
    
    nums = addElementCorrect(nums)
    fmt.Println("After addElementCorrect:", nums)
}

```

**Output:**
```

Inside: [1 2 3 100]
After addElement: [1 2 3]
After addElementCorrect: [1 2 3 100]

```

### 6.2 nil map

```go

package main

func main() {
    var m map[string]int
    // m["key"] = 1  // panic: assignment to entry in nil map
    
    // Правильно — инициализировать
    m = make(map[string]int)
    m["key"] = 1
}

```

### 6.3 Итерация и модификация мапы

```go

package main

import "fmt"

func main() {
    m := map[string]int{"a": 1, "b": 2, "c": 3}
    
    // Удаление во время итерации — безопасно
    for k := range m {
        if k == "b" {
            delete(m, k)
        }
    }
    fmt.Println("After delete:", m)
    
    // Добавление во время итерации — поведение не определено!
    // Не делайте так:
    // for k := range m {
    //     m["new_" + k] = 0
    // }
}

```

**Output:**
```

After delete: map[a:1 c:3]

```

---

## 💡 Key Takeaways

- **Массивы — значения**: Копируются при присваивании. Размер — часть типа.

- **Слайсы — ссылки на массивы**: Динамические, передаются по ссылке. Используйте `make()` для создания.

- **Мапы — ссылочный тип**: nil map паникует при записи. Порядок итерации не определён.

- **Структуры**: Группируют данные. Embedding позволяет "наследовать" поля.

- **append возвращает новый слайс**: Всегда используйте `s = append(s, ...)`.

---

## 🚀 Next Steps

**Related Modules:**

- [06_Pointers](../06_Pointers/) — указатели и ссылки
- [07_Methods](../07_Methods/) — методы на структурах

**Practice Ideas:**

1. Реализуйте стек на слайсах
2. Создайте телефонную книгу на мапах
3. Напишите функции для работы со слайсами (filter, map, reduce)
4. Создайте вложенные структуры для представления JSON

---




