# Flow Control
## Условия, циклы, switch и defer

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовый синтаксис Go (переменные, типы, операторы)
- Понимать логические операторы (`&&`, `||`, `!`)
- Уметь создавать и запускать Go-программы

**Recommended prior modules:**

- [01_Intro](../01_Intro/) — введение в Go
- [02_Basics](../02_Basics/) — переменные и типы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать условные конструкции `if`, `else if`, `else`
- Применять все формы цикла `for`
- Работать с `switch` для множественных условий
- Понимать и применять `defer` для отложенного выполнения
- Использовать `break`, `continue` и метки

---

## 1. Условный оператор if

### 1.1 Базовый синтаксис

В Go условие `if` **не требует круглых скобок**, но **фигурные скобки обязательны**:

```go
package main

import "fmt"

func main() {
    age := 25
    
    // Базовый if
    if age >= 18 {
        fmt.Println("Совершеннолетний")
    }
    
    // if-else
    if age >= 21 {
        fmt.Println("Можно всё")
    } else {
        fmt.Println("Есть ограничения")
    }
    
    // if-else if-else
    if age < 13 {
        fmt.Println("Ребёнок")
    } else if age < 20 {
        fmt.Println("Подросток")
    } else if age < 60 {
        fmt.Println("Взрослый")
    } else {
        fmt.Println("Пожилой")
    }
}
```

**Output:**
```
Совершеннолетний
Есть ограничения
Взрослый
```

### 1.2 if с инициализацией

Уникальная особенность Go — можно объявить переменную прямо в `if`:

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    // Переменная err видна только внутри if-else блока
    if err := doSomething(); err != nil {
        fmt.Println("Ошибка:", err)
    } else {
        fmt.Println("Успех!")
    }
    
    // Паттерн для проверки существования файла
    if _, err := os.Stat("config.yaml"); err == nil {
        fmt.Println("Файл существует")
    } else if os.IsNotExist(err) {
        fmt.Println("Файл не найден")
    } else {
        fmt.Println("Ошибка доступа:", err)
    }
}

func doSomething() error {
    return nil
}
```

**Output:**
```
Успех!
Файл не найден
```

> **💡 Pro Tip:**  
> Паттерн `if err := ...; err != nil` — идиоматический Go. Переменная `err` ограничена блоком `if`, что предотвращает случайное переиспользование.

### 1.3 Вложенные условия

```go
package main

import "fmt"

func main() {
    user := "admin"
    isActive := true
    hasPermission := true
    
    if user == "admin" {
        if isActive {
            if hasPermission {
                fmt.Println("Доступ разрешён")
            }
        }
    }
    
    // Лучше — объединить условия
    if user == "admin" && isActive && hasPermission {
        fmt.Println("Доступ разрешён (упрощённо)")
    }
}
```

**Output:**
```
Доступ разрешён
Доступ разрешён (упрощённо)
```

---

## 2. Цикл for

### 2.1 Единственный цикл в Go

В Go есть только один тип цикла — `for`. Но он покрывает все сценарии:

```go
package main

import "fmt"

func main() {
    // Классический for (как C/Java)
    fmt.Println("Классический for:")
    for i := 0; i < 5; i++ {
        fmt.Print(i, " ")
    }
    fmt.Println()
    
    // While-стиль (только условие)
    fmt.Println("While-стиль:")
    j := 0
    for j < 5 {
        fmt.Print(j, " ")
        j++
    }
    fmt.Println()
    
    // Бесконечный цикл
    fmt.Println("Бесконечный с break:")
    k := 0
    for {
        if k >= 3 {
            break
        }
        fmt.Print(k, " ")
        k++
    }
    fmt.Println()
}
```

**Output:**
```
Классический for:
0 1 2 3 4 
While-стиль:
0 1 2 3 4 
Бесконечный с break:
0 1 2 
```

### 2.2 for range

`for range` — идиоматический способ итерации по коллекциям:

```go
package main

import "fmt"

func main() {
    // Итерация по слайсу
    numbers := []int{10, 20, 30, 40, 50}
    
    fmt.Println("Index и Value:")
    for index, value := range numbers {
        fmt.Printf("  [%d] = %d\n", index, value)
    }
    
    // Только значения (index игнорируется)
    fmt.Println("Только values:")
    for _, v := range numbers {
        fmt.Print(v, " ")
    }
    fmt.Println()
    
    // Только индексы
    fmt.Println("Только indices:")
    for i := range numbers {
        fmt.Print(i, " ")
    }
    fmt.Println()
}
```

**Output:**
```
Index и Value:
  [0] = 10
  [1] = 20
  [2] = 30
  [3] = 40
  [4] = 50
Только values:
10 20 30 40 50 
Только indices:
0 1 2 3 4 
```

**Итерация по строке:**

```go
package main

import "fmt"

func main() {
    s := "Hello, 世界!"
    
    // range по строке итерирует по рунам (Unicode code points)
    fmt.Println("По рунам:")
    for i, r := range s {
        fmt.Printf("  byte %2d: %c (U+%04X)\n", i, r, r)
    }
}
```

**Output:**
```
По рунам:
  byte  0: H (U+0048)
  byte  1: e (U+0065)
  byte  2: l (U+006C)
  byte  3: l (U+006C)
  byte  4: o (U+006F)
  byte  5: , (U+002C)
  byte  6:   (U+0020)
  byte  7: 世 (U+4E16)
  byte 10: 界 (U+754C)
  byte 13: ! (U+0021)
```

**Итерация по map:**

```go
package main

import "fmt"

func main() {
    capitals := map[string]string{
        "Russia":  "Moscow",
        "Japan":   "Tokyo",
        "Germany": "Berlin",
    }
    
    for country, capital := range capitals {
        fmt.Printf("%s -> %s\n", country, capital)
    }
}
```

**Output:**
```
Russia -> Moscow
Japan -> Tokyo
Germany -> Berlin
```

> **⚠️ Warning:**  
> Порядок итерации по `map` не определён и может меняться между запусками!

### 2.3 break и continue

```go
package main

import "fmt"

func main() {
    // break — выход из цикла
    fmt.Println("break:")
    for i := 0; i < 10; i++ {
        if i == 5 {
            break
        }
        fmt.Print(i, " ")
    }
    fmt.Println()
    
    // continue — пропуск итерации
    fmt.Println("continue (пропуск чётных):")
    for i := 0; i < 10; i++ {
        if i%2 == 0 {
            continue
        }
        fmt.Print(i, " ")
    }
    fmt.Println()
}
```

**Output:**
```
break:
0 1 2 3 4 
continue (пропуск чётных):
1 3 5 7 9 
```

### 2.4 Метки (labels)

Метки позволяют выйти из вложенных циклов:

```go
package main

import "fmt"

func main() {
    // Без метки — break выходит только из внутреннего цикла
    fmt.Println("Без метки:")
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if j == 1 {
                break
            }
            fmt.Printf("(%d,%d) ", i, j)
        }
    }
    fmt.Println()
    
    // С меткой — break выходит из внешнего цикла
    fmt.Println("С меткой:")
outer:
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if i == 1 && j == 1 {
                break outer
            }
            fmt.Printf("(%d,%d) ", i, j)
        }
    }
    fmt.Println()
}
```

**Output:**
```
Без метки:
(0,0) (1,0) (2,0) 
С меткой:
(0,0) (0,1) (0,2) (1,0) 
```

---

## 3. Switch

### 3.1 Базовый switch

В Go `switch` **не требует `break`** — каждый case автоматически завершается:

```go
package main

import "fmt"

func main() {
    day := 3
    
    switch day {
    case 1:
        fmt.Println("Понедельник")
    case 2:
        fmt.Println("Вторник")
    case 3:
        fmt.Println("Среда")
    case 4:
        fmt.Println("Четверг")
    case 5:
        fmt.Println("Пятница")
    case 6, 7:
        fmt.Println("Выходной!")
    default:
        fmt.Println("Неверный день")
    }
}
```

**Output:**
```
Среда
```

### 3.2 Switch с несколькими значениями

```go
package main

import "fmt"

func main() {
    char := 'a'
    
    switch char {
    case 'a', 'e', 'i', 'o', 'u':
        fmt.Println("Гласная")
    case ' ', '\t', '\n':
        fmt.Println("Пробельный символ")
    default:
        fmt.Println("Согласная или другой символ")
    }
}
```

**Output:**
```
Гласная
```

### 3.3 Switch без выражения

Switch без выражения — это более читаемая альтернатива цепочке `if-else`:

```go
package main

import "fmt"

func main() {
    score := 85
    
    // Switch без выражения (эквивалент if-else if-else)
    switch {
    case score >= 90:
        fmt.Println("Отлично (A)")
    case score >= 80:
        fmt.Println("Хорошо (B)")
    case score >= 70:
        fmt.Println("Удовлетворительно (C)")
    case score >= 60:
        fmt.Println("Посредственно (D)")
    default:
        fmt.Println("Неудовлетворительно (F)")
    }
}
```

**Output:**
```
Хорошо (B)
```

### 3.4 Switch с инициализацией

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    switch hour := time.Now().Hour(); {
    case hour < 12:
        fmt.Println("Доброе утро!")
    case hour < 17:
        fmt.Println("Добрый день!")
    default:
        fmt.Println("Добрый вечер!")
    }
}
```

**Output:**
```
Добрый день!
```

### 3.5 fallthrough

Если нужно "провалиться" в следующий case, используйте `fallthrough`:

```go
package main

import "fmt"

func main() {
    n := 2
    
    switch n {
    case 1:
        fmt.Println("Один")
        fallthrough
    case 2:
        fmt.Println("Два")
        fallthrough
    case 3:
        fmt.Println("Три")
    case 4:
        fmt.Println("Четыре")
    }
}
```

**Output:**
```
Два
Три
```

> **⚠️ Warning:**  
> `fallthrough` переходит в следующий case **безусловно**, не проверяя его условие. Используйте осторожно!

### 3.6 Type Switch

Type switch позволяет проверять тип значения интерфейса:

```go
package main

import "fmt"

func describe(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("Целое число: %d\n", v)
    case string:
        fmt.Printf("Строка: %q (длина %d)\n", v, len(v))
    case bool:
        fmt.Printf("Булево: %t\n", v)
    case []int:
        fmt.Printf("Слайс int: %v\n", v)
    default:
        fmt.Printf("Неизвестный тип: %T\n", v)
    }
}

func main() {
    describe(42)
    describe("hello")
    describe(true)
    describe([]int{1, 2, 3})
    describe(3.14)
}
```

**Output:**
```
Целое число: 42
Строка: "hello" (длина 5)
Булево: true
Слайс int: [1 2 3]
Неизвестный тип: float64
```

---

## 4. Defer

### 4.1 Отложенное выполнение

`defer` откладывает выполнение функции до выхода из текущей функции:

```go
package main

import "fmt"

func main() {
    fmt.Println("Начало")
    defer fmt.Println("Отложено 1")
    defer fmt.Println("Отложено 2")
    defer fmt.Println("Отложено 3")
    fmt.Println("Конец")
}
```

**Output:**
```
Начало
Конец
Отложено 3
Отложено 2
Отложено 1
```

> **💡 Pro Tip:**  
> Отложенные вызовы выполняются в порядке LIFO (Last In, First Out) — как стек.

### 4.2 Типичные сценарии использования

**Закрытие файлов:**

```go
package main

import (
    "fmt"
    "os"
)

func readFile(filename string) error {
    f, err := os.Open(filename)
    if err != nil {
        return err
    }
    defer f.Close()  // Гарантированно закроется при выходе
    
    // Работа с файлом...
    buf := make([]byte, 100)
    n, _ := f.Read(buf)
    fmt.Printf("Прочитано %d байт\n", n)
    
    return nil
}

func main() {
    readFile("example.txt")
}
```

**Освобождение мьютексов:**

```go
package main

import (
    "fmt"
    "sync"
)

var (
    counter int
    mu      sync.Mutex
)

func increment() {
    mu.Lock()
    defer mu.Unlock()  // Гарантированно разблокируется
    
    counter++
}

func main() {
    for i := 0; i < 5; i++ {
        increment()
    }
    fmt.Println("Counter:", counter)
}
```

**Output:**
```
Counter: 5
```

### 4.3 Defer и значения аргументов

Аргументы defer вычисляются немедленно, но вызов откладывается:

```go
package main

import "fmt"

func main() {
    x := 10
    defer fmt.Println("Deferred x =", x)  // x вычисляется сейчас (10)
    x = 20
    fmt.Println("Current x =", x)
}
```

**Output:**
```
Current x = 20
Deferred x = 10
```

**Для "захвата" текущего значения используйте замыкание:**

```go
package main

import "fmt"

func main() {
    x := 10
    defer func() {
        fmt.Println("Closure x =", x)  // x захвачен по ссылке
    }()
    x = 20
    fmt.Println("Current x =", x)
}
```

**Output:**
```
Current x = 20
Closure x = 20
```

### 4.4 Defer и возвращаемые значения

Defer может модифицировать именованные возвращаемые значения:

```go
package main

import "fmt"

func double(x int) (result int) {
    defer func() {
        result *= 2  // Модифицируем result после return
    }()
    return x
}

func main() {
    fmt.Println(double(5))  // 10, не 5!
}
```

**Output:**
```
10
```

### 4.5 Defer в цикле

```go
package main

import "fmt"

func main() {
    // Осторожно! Все defer выполнятся только после выхода из функции
    for i := 0; i < 3; i++ {
        defer fmt.Println("Deferred:", i)
    }
    fmt.Println("После цикла")
}
```

**Output:**
```
После цикла
Deferred: 2
Deferred: 1
Deferred: 0
```

> **⚠️ Warning:**  
> Defer в цикле может привести к утечке ресурсов (например, открытых файлов). Для каждой итерации используйте отдельную функцию.

---

## 5. Goto

### 5.1 Использование goto

Go поддерживает `goto`, но его использование ограничено и обычно не рекомендуется:

```go
package main

import "fmt"

func main() {
    i := 0

loop:
    if i < 5 {
        fmt.Print(i, " ")
        i++
        goto loop
    }
    fmt.Println()
    fmt.Println("Конец")
}
```

**Output:**
```
0 1 2 3 4 
Конец
```

> **⚠️ Warning:**  
> `goto` не может перепрыгивать через объявления переменных. В большинстве случаев лучше использовать циклы и функции.

---

## 6. Практические паттерны

### 6.1 Early Return

```go
package main

import "fmt"

// Плохо — много вложенности
func processUserBad(user string, age int, active bool) {
    if user != "" {
        if age >= 18 {
            if active {
                fmt.Println("Обработка пользователя:", user)
            }
        }
    }
}

// Хорошо — ранние возвраты
func processUserGood(user string, age int, active bool) {
    if user == "" {
        return
    }
    if age < 18 {
        return
    }
    if !active {
        return
    }
    fmt.Println("Обработка пользователя:", user)
}

func main() {
    processUserBad("John", 25, true)
    processUserGood("Jane", 30, true)
}
```

**Output:**
```
Обработка пользователя: John
Обработка пользователя: Jane
```

### 6.2 Бесконечный цикл с условием выхода

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    start := time.Now()
    attempts := 0
    maxAttempts := 5
    
    for {
        attempts++
        fmt.Printf("Попытка %d...\n", attempts)
        
        // Симуляция проверки
        if time.Since(start) > 100*time.Millisecond {
            fmt.Println("Успех!")
            break
        }
        
        if attempts >= maxAttempts {
            fmt.Println("Превышено число попыток")
            break
        }
        
        time.Sleep(30 * time.Millisecond)
    }
}
```

**Output:**
```
Попытка 1...
Попытка 2...
Попытка 3...
Попытка 4...
Успех!
```

### 6.3 Паттерн обработки ошибок с defer

```go
package main

import (
    "fmt"
    "errors"
)

func processData() (err error) {
    // Ресурс 1
    fmt.Println("Открываем ресурс 1")
    defer func() {
        fmt.Println("Закрываем ресурс 1")
    }()
    
    // Ресурс 2
    fmt.Println("Открываем ресурс 2")
    defer func() {
        fmt.Println("Закрываем ресурс 2")
    }()
    
    // Симуляция ошибки
    if true {
        return errors.New("что-то пошло не так")
    }
    
    return nil
}

func main() {
    err := processData()
    if err != nil {
        fmt.Println("Ошибка:", err)
    }
}
```

**Output:**
```
Открываем ресурс 1
Открываем ресурс 2
Закрываем ресурс 2
Закрываем ресурс 1
Ошибка: что-то пошло не так
```

---

## 7. Common Pitfalls

### 7.1 Забытые фигурные скобки

```go
// Ошибка компиляции!
if x > 0
    fmt.Println("positive")

// Правильно
if x > 0 {
    fmt.Println("positive")
}
```

### 7.2 Модификация слайса при итерации

```go
package main

import "fmt"

func main() {
    nums := []int{1, 2, 3, 4, 5}
    
    // Осторожно! v — это копия
    for i, v := range nums {
        v = v * 2        // НЕ изменяет nums!
        nums[i] = v * 2  // Это изменяет
        _ = i
    }
    
    fmt.Println(nums)  // [4 8 12 16 20]
}
```

**Output:**
```
[4 8 12 16 20]
```

### 7.3 Захват переменной цикла в горутине

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    // НЕПРАВИЛЬНО (до Go 1.22)
    for i := 0; i < 3; i++ {
        go func() {
            fmt.Print(i, " ")  // Все выведут одно значение!
        }()
    }
    
    time.Sleep(100 * time.Millisecond)
    fmt.Println()
    
    // ПРАВИЛЬНО — передаём как аргумент
    for i := 0; i < 3; i++ {
        go func(n int) {
            fmt.Print(n, " ")
        }(i)
    }
    
    time.Sleep(100 * time.Millisecond)
    fmt.Println()
}
```

**Output (может варьироваться):**
```
3 3 3 
0 1 2 
```

> **💡 Pro Tip:**  
> В Go 1.22+ переменные цикла создаются заново на каждой итерации, поэтому эта проблема решена.

---

## 💡 Key Takeaways

- **Только for**: В Go один тип цикла — `for`, который покрывает все сценарии (классический, while, бесконечный).

- **Скобки**: Условия `if` и `switch` не требуют круглых скобок, но фигурные обязательны.

- **Switch без break**: В Go каждый case завершается автоматически. Используйте `fallthrough` для проваливания.

- **defer — для очистки**: Гарантирует выполнение кода при выходе из функции. Идеально для закрытия ресурсов.

- **LIFO для defer**: Отложенные вызовы выполняются в обратном порядке (стек).

---

## 🚀 Next Steps

**Related Modules:**

- [04_Functions](../04_Functions/) — функции и замыкания
- [08_Errors](../08_Errors/) — обработка ошибок
- [09_Concurrency](../09_Concurrency/) — горутины и каналы

**Practice Ideas:**

1. Напишите программу FizzBuzz
2. Создайте простой калькулятор с switch
3. Реализуйте функцию чтения файла с defer для закрытия
4. Напишите программу с вложенными циклами и метками

**Going Deeper:**

- Изучите паттерны graceful shutdown с defer
- Прочитайте о "comma ok" паттерне
- Изучите context для отмены операций

---




