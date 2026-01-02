# Struct и Enum - Quiz

Проверьте свои знания по теме "struct, enum, pattern matching, Option и Result".

---

## Question 1: Определение struct

Как правильно определить структуру?

A) `struct User { username: String, email: String }`

B) `User { username, email }`

C) `struct User { username, email }`

D) `struct User(username, email)`

---

## Question 2: Методы

Что такое &self в методах?

A) Значение структуры

B) Копия структуры

C) Указатель

D) Ссылка на экземпляр структуры

---

## Question 3: Enum варианты

Что выведет код?

```rust
enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    let c = Color::Red;
    match c {
        Color::Red => println!("Красный"),
        Color::Blue => println!("Синий"),
        Color::Green => println!("Зелёный"),
    }
}
```

A) Красный

B) Ошибка компиляции

C) Зелёный

D) Синий

---

## Question 4: Option

Что такое Option<T>?

A) Всегда None

B) Всегда содержит значение типа T

C) Может содержать Some(T) или None

D) Всегда Some(T)

---

## Question 5: Result

Что такое Result<T, E>?

A) Всегда успех

B) Всегда ошибка

C) Ok(T) для успеха или Err(E) для ошибки

D) Option с ошибкой

---

## Question 6: Pattern matching

Что произойдёт при компиляции?

```rust
enum State {
    Idle,
    Running,
}

fn main() {
    let s = State::Idle;
    match s {
        State::Idle => println!("Ожидание"),
    }
}
```

A) Ошибка: не все случаи покрыты

B) Код скомпилируется

C) Паника во время выполнения

D) Предупреждение

---

## Question 7: if let

Что делает if let?

A) Создаёт переменную

B) Упрощённый синтаксис для match с одним паттерном

C) Цикл

D) Проверяет условие

---

## Question 8: Ассоциированные функции

Как вызвать ассоциированную функцию?

A) `new Rectangle()`

B) `Rectangle.new()`

C) `Rectangle::new()`

D) `rect.new()`

---

## Question 9: Tuple structs

Что такое tuple struct?

A) Функция

B) Структура без имён полей

C) Обычная struct

D) Enum

---

## Question 10: Unit-like struct

Что такое unit-like struct?

A) Функция

B) Enum

C) Struct без полей

D) Struct с полями

---

## Question 11: Enum с данными

Что выведет код?

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}

fn main() {
    let msg = Message::Write(String::from("hello"));
    match msg {
        Message::Write(text) => println!("{}", text),
        _ => {}
    }
}
```

A) Ошибка компиляции

B) Паника

C) hello

D) Ничего

---

## Question 12: match и Option

Что выведет код?

```rust
fn main() {
    let some_number = Some(5);
    match some_number {
        Some(x) => println!("{}", x),
        None => println!("Нет значения"),
    }
}
```

A) Паника

B) Нет значения

C) 5

D) Ошибка компиляции

---

## Question 13: if let с Option

Что выведет код?

```rust
fn main() {
    let some_value = Some(3);
    if let Some(x) = some_value {
        println!("{}", x);
    }
}
```

A) Ничего

B) 3

C) Ошибка компиляции

D) Паника

---

## Question 14: while let

Что делает while let?

A) Цикл, пока паттерн совпадает

B) Условный оператор

C) Цикл с условием

D) Создаёт переменную

---

## Question 15: Enum методы

Можно ли иметь методы для enum?

A) Нет

B) Да, через impl

C) В unsafe коде

D) Для struct

---

## Question 16: match guards

Что такое match guards?

A) Защита от ошибок

B) Дополнительные условия в match

C) Создание новых паттернов

D) Удаление паттернов

---

## Question 17: Деструктуризация

Что делает деструктуризация в match?

A) Удаляет структуру

B) Копирует структуру

C) Извлекает значения из структуры или enum

D) Создаёт структуру

---

## Question 18: @ binding

Что делает @ в match?

A) Создаёт переменную

B) Связывает значение с переменной при сопоставлении

C) Копирует значение

D) Удаляет значение

---

## Question 19: match и ссылки

Что произойдёт при компиляции?

```rust
fn main() {
    let opt = Some(&5);
    match opt {
        Some(x) => println!("{}", x),
        None => {}
    }
}
```

A) Предупреждение

B) Код скомпилируется и выведет 5

C) Паника

D) Ошибка компиляции

---

## Question 20: Enum и match exhaustiveness

Почему match должен быть exhaustive?

A) Для безопасности — компилятор проверяет все случаи

B) Для Option и Result

C) Для производительности

D) Не должен

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Структура определяется с указанием типов полей: `struct Name { field: Type }` |
| 2 | D | &self — это ссылка на экземпляр структуры, на котором вызывается метод |
| 3 | A | match сопоставляет Color::Red с первым паттерном и выводит "Красный" |
| 4 | C | Option<T> может быть Some(T) (есть значение) или None (нет значения) |
| 5 | C | Result<T, E> представляет Ok(T) для успеха или Err(E) для ошибки |
| 6 | A | match должен покрывать все варианты enum, нужен паттерн для State::Running |
| 7 | B | if let — упрощённый синтаксис для match с одним паттерном |
| 8 | C | Ассоциированные функции вызываются через `::`: `Type::function()` |
| 9 | C | Tuple struct — структура без имён полей, только типы: `struct Point(i32, i32)` |
| 10 | C | Unit-like struct — структура без полей: `struct Marker;` |
| 11 | C | match извлекает String из Message::Write и выводит "hello" |
| 12 | C | match извлекает значение из Some(5) и выводит 5 |
| 13 | B | if let извлекает значение из Some(3) и выводит 3 |
| 14 | A | while let — цикл, который выполняется пока паттерн совпадает |
| 15 | B | Enum может иметь методы через impl блок, как и struct |
| 16 | B | Match guards — дополнительные условия в match: `Some(x) if x > 5 => ...` |
| 17 | C | Деструктуризация извлекает значения из структуры или enum в match |
| 18 | B | @ связывает значение с переменной при сопоставлении: `x @ 1..=5 => ...` |
| 19 | B | Код скомпилируется, match извлечёт ссылку и выведет 5 |
| 20 | A | Match должен быть exhaustive для безопасности — компилятор проверяет все случаи |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Переходите к следующему модулю. |
| **14-17 правильных (70-85%)** | ✅ Хорошо | Хороший результат! Повторите темы, в которых ошиблись. |
| **10-13 правильных (50-65%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать соответствующие разделы лекции. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---


