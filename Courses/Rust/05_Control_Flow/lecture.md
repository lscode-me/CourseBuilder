# Управление потоком
## if/else, loop, while, for, match

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать переменные и типы в Rust (см. модуль [04_Variables_Types](../04_Variables_Types/))
- Уметь создавать и запускать программы на Rust
- Знать базовые концепции программирования: условия, циклы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать условные операторы if/else и выражения
- Применять различные типы циклов: loop, while, for
- Использовать match для pattern matching
- Понимать разницу между выражениями и операторами в Rust
- Применять управление потоком в практических задачах

---

## 1. Условные операторы if/else

### 1.1 Базовый синтаксис

В Rust `if` — это **выражение**, а не оператор, что означает, что оно возвращает значение.

**Example: Простое условие**

```rust
fn main() {
    let number = 7;
    
    if number < 5 {
        println!("Число меньше 5");
    } else {
        println!("Число больше или равно 5");
    }
}
```

**Output:**
```
Число больше или равно 5
```

### 1.2 if как выражение

**Example: Возврат значения**

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };
    
    println!("Число: {}", number);
}
```

**Output:**
```
Число: 5
```

**Важно:** Оба ветки должны возвращать значения одного типа!

**Example: Ошибка — разные типы**

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { "six" };  // Ошибка!
}
```

**Ошибка компиляции:**
```
error[E0308]: if and else have incompatible types
```

### 1.3 Множественные условия

**Example: else if**

```rust
fn main() {
    let number = 6;
    
    if number % 4 == 0 {
        println!("Число делится на 4");
    } else if number % 3 == 0 {
        println!("Число делится на 3");
    } else if number % 2 == 0 {
        println!("Число делится на 2");
    } else {
        println!("Число не делится на 4, 3 или 2");
    }
}
```

**Output:**
```
Число делится на 3
```

---

## 2. Цикл loop

### 2.1 Бесконечный цикл

**loop** создаёт бесконечный цикл, который можно прервать с помощью `break`.

**Example: Простой loop**

```rust
fn main() {
    let mut counter = 0;
    
    loop {
        counter += 1;
        println!("Счётчик: {}", counter);
        
        if counter >= 5 {
            break;
        }
    }
}
```

**Output:**
```
Счётчик: 1
Счётчик: 2
Счётчик: 3
Счётчик: 4
Счётчик: 5
```

### 2.2 Возврат значения из loop

**Example: Возврат значения**

```rust
fn main() {
    let mut counter = 0;
    
    let result = loop {
        counter += 1;
        
        if counter == 10 {
            break counter * 2;
        }
    };
    
    println!("Результат: {}", result);
}
```

**Output:**
```
Результат: 20
```

### 2.3 Метки циклов

**Example: Вложенные циклы с метками**

```rust
fn main() {
    let mut count = 0;
    
    'outer: loop {
        println!("Внешний цикл: {}", count);
        let mut inner_count = 0;
        
        loop {
            println!("  Внутренний цикл: {}", inner_count);
            inner_count += 1;
            
            if inner_count == 3 {
                break;
            }
            
            if count == 2 {
                break 'outer;
            }
        }
        
        count += 1;
    }
}
```

**Output:**
```
Внешний цикл: 0
  Внутренний цикл: 0
  Внутренний цикл: 1
  Внутренний цикл: 2
Внешний цикл: 1
  Внутренний цикл: 0
  Внутренний цикл: 1
  Внутренний цикл: 2
Внешний цикл: 2
  Внутренний цикл: 0
```

---

## 3. Цикл while

### 3.1 Базовое использование

**while** выполняет блок кода, пока условие истинно.

**Example: Простой while**

```rust
fn main() {
    let mut number = 3;
    
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }
    
    println!("Старт!");
}
```

**Output:**
```
3!
2!
1!
Старт!
```

### 3.2 Обход массива

**Example: Обход массива**

```rust
fn main() {
    let arr = [10, 20, 30, 40, 50];
    let mut index = 0;
    
    while index < 5 {
        println!("Элемент {}: {}", index, arr[index]);
        index += 1;
    }
}
```

**Output:**
```
Элемент 0: 10
Элемент 1: 20
Элемент 2: 30
Элемент 3: 40
Элемент 4: 50
```

---

## 4. Цикл for

### 4.1 Обход диапазона

**for** — наиболее идиоматичный способ циклов в Rust.

**Example: Диапазон чисел**

```rust
fn main() {
    for number in 1..=5 {
        println!("{}", number);
    }
}
```

**Output:**
```
1
2
3
4
5
```

**Диапазоны:**

- `1..5` — от 1 до 4 (не включая 5)
- `1..=5` — от 1 до 5 (включая 5)

### 4.2 Обход массива

**Example: Обход массива**

```rust
fn main() {
    let arr = [10, 20, 30, 40, 50];
    
    for element in arr.iter() {
        println!("Значение: {}", element);
    }
}
```

**Output:**
```
Значение: 10
Значение: 20
Значение: 30
Значение: 40
Значение: 50
```

**Example: Обход с индексом**

```rust
fn main() {
    let arr = [10, 20, 30, 40, 50];
    
    for (index, value) in arr.iter().enumerate() {
        println!("Индекс {}: {}", index, value);
    }
}
```

**Output:**
```
Индекс 0: 10
Индекс 1: 20
Индекс 2: 30
Индекс 3: 40
Индекс 4: 50
```

### 4.3 Обратный порядок

**Example: Обратный порядок**

```rust
fn main() {
    for number in (1..=5).rev() {
        println!("{}", number);
    }
}
```

**Output:**
```
5
4
3
2
1
```

---

## 5. Pattern matching с match

### 5.1 Базовый синтаксис

**match** — мощный инструмент для pattern matching, похожий на switch в других языках, но более выразительный.

**Example: Простой match**

```rust
fn main() {
    let number = 3;
    
    match number {
        1 => println!("Один"),
        2 => println!("Два"),
        3 => println!("Три"),
        _ => println!("Другое число"),
    }
}
```

**Output:**
```
Три
```

**`_`** — catch-all паттерн для всех остальных случаев.

### 5.2 Возврат значений

**Example: match как выражение**

```rust
fn main() {
    let number = 5;
    
    let description = match number {
        1 => "один",
        2 => "два",
        3 => "три",
        _ => "много",
    };
    
    println!("Число: {}", description);
}
```

**Output:**
```
Число: много
```

### 5.3 Множественные паттерны

**Example: Несколько значений**

```rust
fn main() {
    let number = 2;
    
    match number {
        1 | 2 | 3 => println!("Маленькое число"),
        4 | 5 | 6 => println!("Среднее число"),
        _ => println!("Большое число"),
    }
}
```

**Output:**
```
Маленькое число
```

### 5.4 Диапазоны в match

**Example: Диапазоны**

```rust
fn main() {
    let number = 42;
    
    match number {
        1..=10 => println!("От 1 до 10"),
        11..=20 => println!("От 11 до 20"),
        21..=50 => println!("От 21 до 50"),
        _ => println!("Другое"),
    }
}
```

**Output:**
```
От 21 до 50
```

### 5.5 Деструктуризация в match

**Example: Деструктуризация кортежей**

```rust
fn main() {
    let point = (0, 5);
    
    match point {
        (0, 0) => println!("В начале координат"),
        (0, y) => println!("На оси Y: {}", y),
        (x, 0) => println!("На оси X: {}", x),
        (x, y) => println!("В точке ({}, {})", x, y),
    }
}
```

**Output:**
```
На оси Y: 5
```

---

## 6. Практические примеры

### 6.1 Пример: Поиск в массиве

```rust
fn main() {
    let arr = [10, 20, 30, 40, 50];
    let target = 30;
    let mut found = false;
    
    for (index, &value) in arr.iter().enumerate() {
        if value == target {
            println!("Найдено {} на позиции {}", target, index);
            found = true;
            break;
        }
    }
    
    if !found {
        println!("{} не найдено", target);
    }
}
```

**Output:**
```
Найдено 30 на позиции 2
```

### 6.2 Пример: Подсчёт суммы

```rust
fn main() {
    let numbers = [1, 2, 3, 4, 5];
    let mut sum = 0;
    
    for &number in numbers.iter() {
        sum += number;
    }
    
    println!("Сумма: {}", sum);
}
```

**Output:**
```
Сумма: 15
```

### 6.3 Пример: FizzBuzz

```rust
fn main() {
    for number in 1..=20 {
        match (number % 3, number % 5) {
            (0, 0) => println!("FizzBuzz"),
            (0, _) => println!("Fizz"),
            (_, 0) => println!("Buzz"),
            _ => println!("{}", number),
        }
    }
}
```

**Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

---

## 7. Управление циклом: continue

### 7.1 Пропуск итерации

**continue** пропускает текущую итерацию и переходит к следующей.

**Example: Пропуск чётных чисел**

```rust
fn main() {
    for number in 1..=10 {
        if number % 2 == 0 {
            continue;
        }
        println!("{}", number);
    }
}
```

**Output:**
```
1
3
5
7
9
```

---

## 8. Сравнение циклов

| Цикл | Когда использовать | Примеры |
|------|-------------------|---------|
| **loop** | Бесконечный цикл, пока не break | Игровые циклы, серверы |
| **while** | Цикл с условием | Чтение до EOF, обработка очереди |
| **for** | Обход коллекций, диапазонов | Итерация по массивам, спискам |

> **💡 Pro Tip:**  
> В Rust предпочтительно использовать `for` для обхода коллекций, так как это безопаснее и идиоматичнее.

---

## 💡 Key Takeaways

- **if — это выражение:** Может возвращать значения, все ветки должны иметь один тип

- **loop — бесконечный цикл:** Можно прервать break и вернуть значение

- **while — цикл с условием:** Выполняется пока условие истинно

- **for — идиоматичный способ:** Предпочтителен для обхода коллекций

- **match — мощный pattern matching:** Более выразительный чем switch, обязателен для enum

---

## 🚀 Next Steps

**Related Modules:**

- [Функции и модули](../06_Functions_Modules/) — создание функций и организация кода
- [Ownership и Borrowing](../07_Ownership_Borrowing/) — ключевая концепция Rust

**Practice Ideas:**

1. Реализуйте алгоритм поиска в массиве
2. Создайте программу-калькулятор с использованием match
3. Напишите FizzBuzz с различными вариантами
4. Попробуйте обойти вектор разными способами

**Going Deeper:**

- Изучите итераторы (Iterator trait)
- Почитайте о pattern matching с guard clauses
- Изучите if let и while let для упрощения кода

---

## 📚 Additional Resources

**Documentation:**

- [Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html) — документация по управлению потоком
- [Pattern Matching](https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html) — синтаксис pattern matching

**Practice:**

- [Rustlings: Control Flow](https://github.com/rust-lang/rustlings) — упражнения

---


