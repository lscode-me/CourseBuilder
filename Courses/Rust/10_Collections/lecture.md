# Коллекции
## Vec, HashMap, String, итераторы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать ownership и borrowing (см. модуль [07_Ownership_Borrowing](../07_Ownership_Borrowing/))
- Знать базовые типы данных (см. модуль [04_Variables_Types](../04_Variables_Types/))
- Понимать управление потоком (см. модуль [05_Control_Flow](../05_Control_Flow/))

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать Vec для динамических массивов
- Работать с HashMap для ключ-значение структур
- Понимать разницу между String и &str
- Применять итераторы для обработки коллекций
- Выбирать подходящую коллекцию для задачи

---

## 1. Vec (Вектор)

### 1.1 Создание вектора

**Vec** — динамический массив, который может расти и уменьшаться.

**Example: Создание вектора**

```rust

fn main() {
    let v: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3];  // Макрос для создания с начальными значениями
    
    println!("v: {:?}", v);
    println!("v2: {:?}", v2);
}
```

**Output:**
```

v: []
v2: [1, 2, 3]
```

### 1.2 Добавление элементов

**Example: Добавление элементов**

```rust

fn main() {
    let mut v = Vec::new();
    
    v.push(1);
    v.push(2);
    v.push(3);
    
    println!("{:?}", v);
}
```

**Output:**
```

[1, 2, 3]
```

### 1.3 Доступ к элементам

**Example: Доступ по индексу**

```rust

fn main() {
    let v = vec![1, 2, 3, 4, 5];
    
    let third = &v[2];  // Получаем ссылку
    println!("Третий элемент: {}", third);
    
    match v.get(2) {  // Безопасный доступ
        Some(third) => println!("Третий элемент: {}", third),
        None => println!("Нет третьего элемента"),
    }
}
```

**Output:**
```

Третий элемент: 3
Третий элемент: 3
```

**Разница:**

- `&v[index]` — паника при выходе за границы
- `v.get(index)` — возвращает `Option<&T>`

### 1.4 Итерация по вектору

**Example: Итерация**

```rust

fn main() {
    let v = vec![100, 32, 57];
    
    for i in &v {
        println!("{}", i);
    }
    
    // Изменение элементов
    let mut v2 = vec![100, 32, 57];
    for i in &mut v2 {
        *i += 50;
    }
    println!("{:?}", v2);
}
```

**Output:**
```

100
32
57
[150, 82, 107]
```

---

## 2. HashMap

### 2.1 Создание HashMap

**HashMap** — коллекция ключ-значение.

**Example: Создание HashMap**

```rust

use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    
    println!("{:?}", scores);
}
```

**Output:**
```

{"Blue": 10, "Yellow": 50}
```

### 2.2 Доступ к значениям

**Example: Получение значения**

```rust

use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    
    let team_name = String::from("Blue");
    let score = scores.get(&team_name);
    
    match score {
        Some(s) => println!("Счёт Blue: {}", s),
        None => println!("Команда не найдена"),
    }
}
```

**Output:**
```

Счёт Blue: 10
```

### 2.3 Итерация по HashMap

**Example: Итерация**

```rust

use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    
    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
}
```

**Output:**
```

Blue: 10
Yellow: 50
```

### 2.4 Обновление значений

**Example: Обновление**

```rust

use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    
    // Перезапись
    scores.insert(String::from("Blue"), 25);
    println!("{:?}", scores);
    
    // Вставка только если нет ключа
    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);
    println!("{:?}", scores);
}
```

**Output:**
```

{"Blue": 25}
{"Blue": 25, "Yellow": 50}
```

---

## 3. String

### 3.1 Создание строк

**String** — владеющая строка, которая может расти.

**Example: Создание String**

```rust

fn main() {
    let mut s = String::new();
    
    let data = "initial contents";
    let s = data.to_string();
    
    let s = String::from("initial contents");
    
    println!("{}", s);
}
```

**Output:**
```

initial contents
```

### 3.2 Обновление строк

**Example: Добавление к строке**

```rust

fn main() {
    let mut s = String::from("foo");
    s.push_str("bar");
    s.push('!');
    
    println!("{}", s);
    
    // Конкатенация
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2;  // s1 перемещается
    
    println!("{}", s3);
}
```

**Output:**
```

foobar!
Hello, world!
```

### 3.3 Форматирование строк

**Example: format! макрос**

```rust

fn main() {
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");
    
    let s = format!("{}-{}-{}", s1, s2, s3);
    println!("{}", s);
}
```

**Output:**
```

tic-tac-toe
```

### 3.4 Индексация строк

**⚠️ Важно:** String не поддерживает прямую индексацию!

**Example: Работа со строками**

```rust

fn main() {
    let s = String::from("hello");
    
    // Не работает: let h = s[0];
    
    // Работает: срезы
    let hello = &s[0..5];
    println!("{}", hello);
    
    // Итерация по символам
    for c in s.chars() {
        println!("{}", c);
    }
}
```

**Output:**
```

hello
h
e
l
l
o
```

---

## 4. Итераторы

### 4.1 Что такое итераторы

**Итераторы** — способ обработки последовательности элементов.

**Example: Базовое использование**

```rust

fn main() {
    let v1 = vec![1, 2, 3];
    let v1_iter = v1.iter();
    
    for val in v1_iter {
        println!("{}", val);
    }
}
```

**Output:**
```

1
2
3
```

### 4.2 Методы итераторов

**Example: map и collect**

```rust

fn main() {
    let v1 = vec![1, 2, 3];
    let v2: Vec<_> = v1.iter().map(|x| x * 2).collect();
    
    println!("{:?}", v2);
}
```

**Output:**
```

[2, 4, 6]
```

### 4.3 Фильтрация

**Example: filter**

```rust

fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6];
    let evens: Vec<_> = numbers.iter()
        .filter(|&x| x % 2 == 0)
        .collect();
    
    println!("{:?}", evens);
}
```

**Output:**
```

[2, 4, 6]
```

### 4.4 Цепочка операций

**Example: Цепочка**

```rust

fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    let result: Vec<i32> = numbers.iter()
        .map(|x| x * 2)
        .filter(|&x| x > 5)
        .collect();
    
    println!("{:?}", result);
}
```

**Output:**
```

[6, 8, 10]
```

### 4.5 Ленивые вычисления

**Итераторы ленивы** — они ничего не делают, пока не вызван метод потребления.

**Example: Ленивые вычисления**

```rust

fn main() {
    let v1 = vec![1, 2, 3];
    let v1_iter = v1.iter().map(|x| x + 1);  // Пока ничего не вычислено
    
    let v2: Vec<_> = v1_iter.collect();  // Теперь вычисляется
    println!("{:?}", v2);
}
```

**Output:**
```

[2, 3, 4]
```

---

## 5. Практические примеры

### 5.1 Пример: Подсчёт слов

```rust

use std::collections::HashMap;

fn main() {
    let text = "hello world wonderful world";
    let mut map = HashMap::new();
    
    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
    
    println!("{:?}", map);
}
```

**Output:**
```

{"world": 2, "hello": 1, "wonderful": 1}
```

### 5.2 Пример: Фильтрация и преобразование

```rust

fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    
    let result: Vec<i32> = numbers.iter()
        .filter(|&n| n % 2 == 0)
        .map(|n| n * n)
        .collect();
    
    println!("Чётные числа в квадрате: {:?}", result);
}
```

**Output:**
```

Чётные числа в квадрате: [4, 16, 36, 64, 100]
```

---

## 💡 Key Takeaways

- **Vec для динамических массивов:** Может расти и уменьшаться

- **HashMap для ключ-значение:** Эффективный поиск по ключу

- **String vs &str:** String владеет данными, &str — ссылка

- **Итераторы ленивы:** Вычисляются только при потреблении

- **Цепочка операций:** map, filter, collect для функционального стиля

---

## 🚀 Next Steps

**Related Modules:**

- [Traits и Generics](../11_Traits_Generics/) — создание переиспользуемого кода
- [Асинхронность](../13_Async/) — работа с async/await

**Practice Ideas:**

1. Создайте программу для подсчёта частоты слов
2. Реализуйте фильтрацию и преобразование данных
3. Попробуйте различные методы итераторов
4. Поработайте с вложенными структурами данных

**Going Deeper:**

- Изучите другие коллекции: BTreeMap, HashSet
- Почитайте о производительности различных коллекций
- Изучите продвинутые методы итераторов

---

## 📚 Additional Resources

**Documentation:**

- [Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html) — документация по Vec
- [HashMap](https://doc.rust-lang.org/book/ch08-03-hash-maps.html) — документация по HashMap
- [Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html) — документация по итераторам

**Practice:**

- [Rustlings: Collections](https://github.com/rust-lang/rustlings) — упражнения

---


