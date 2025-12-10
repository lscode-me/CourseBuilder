# Flow Control - Quiz

Проверьте свои знания по теме "Условия, циклы, switch и defer".

---

## Question 1: Синтаксис if

Какой синтаксис if корректен в Go?

A) `if (x > 0) { fmt.Println("positive") }`

B) `if x > 0 { fmt.Println("positive") }`

C) `if x > 0 fmt.Println("positive")`

D) `if x > 0 then { fmt.Println("positive") }`

---

## Question 2: if с инициализацией

Какой код корректно использует if с инициализацией?

A) `if x := getValue(); x > 0 { }`

B) `if (x := getValue()) x > 0 { }`

C) `if x := getValue() then x > 0 { }`

D) `if x = getValue(); x > 0 { }`

---

## Question 3: Циклы в Go

Сколько типов циклов есть в Go?

A) 0 (нет циклов)

B) 1 (только for)

C) 2 (for и while)

D) 3 (for, while, do-while)

---

## Question 4: while-стиль

Какой код эквивалентен `while x < 10` в Go?

A) `while x < 10 { }`

B) `for x < 10 { }`

C) `do { } while x < 10`

D) `loop x < 10 { }`

---

## Question 5: Бесконечный цикл

Как написать бесконечный цикл в Go?

A) `for (;;) { }`

B) `while true { }`

C) `for { }`

D) `loop { }`

---

## Question 6: for range

Что выведет код?

```go
for i, v := range []int{10, 20, 30} {
    fmt.Print(i, " ")
}
```

A) 10 20 30

B) 0 1 2

C) 0 10 1 20 2 30

D) Ошибка компиляции

---

## Question 7: Игнорирование значения

Как итерировать по слайсу, используя только индексы?

A) `for i, _ := range slice { }`

B) `for i := range slice { }`

C) `for i in slice { }`

D) `for i only range slice { }`

---

## Question 8: switch и break

Нужен ли break в конце case в Go switch?

A) Да, обязательно

B) Нет, break автоматический

C) Да, но только для default

D) Зависит от типа данных

---

## Question 9: Множественные значения case

Какой синтаксис позволяет проверить несколько значений в одном case?

A) `case 1 || 2 || 3:`

B) `case 1, 2, 3:`

C) `case 1 or 2 or 3:`

D) `case [1, 2, 3]:`

---

## Question 10: switch без выражения

Что выведет код?

```go
x := 15
switch {
case x < 10:
    fmt.Println("small")
case x < 20:
    fmt.Println("medium")
default:
    fmt.Println("large")
}
```

A) small

B) medium

C) large

D) small medium

---

## Question 11: fallthrough

Что делает ключевое слово fallthrough?

A) Прерывает выполнение switch

B) Переходит к следующему case безусловно

C) Перезапускает switch

D) Проверяет условие следующего case

---

## Question 12: defer порядок

В каком порядке выполняются defer-вызовы?

A) FIFO (First In, First Out)

B) LIFO (Last In, First Out)

C) Случайный порядок

D) Порядок объявления

---

## Question 13: defer выполнение

Когда выполняются defer-вызовы?

A) Сразу после объявления

B) При выходе из функции

C) В конце программы

D) При вызове panic

---

## Question 14: defer и аргументы

Что выведет код?

```go
x := 10
defer fmt.Println(x)
x = 20
```

A) 10

B) 20

C) Ошибка компиляции

D) Ничего

---

## Question 15: defer в цикле

Что выведет код?

```go
for i := 0; i < 3; i++ {
    defer fmt.Print(i, " ")
}
fmt.Print("done ")
```

A) 0 1 2 done

B) done 0 1 2

C) done 2 1 0

D) 2 1 0 done

---

## Question 16: break с меткой

Для чего используются метки с break?

A) Для выхода из функции

B) Для выхода из вложенных циклов

C) Для перехода к метке

D) Для пропуска итерации

---

## Question 17: continue

Что делает continue в цикле?

A) Выходит из цикла

B) Пропускает оставшийся код итерации

C) Перезапускает цикл

D) Переходит к следующему switch case

---

## Question 18: for range и строка

Что возвращает range при итерации по строке?

A) Байты

B) Символы (runes) и их байтовые позиции

C) Только символы

D) Символы и их индексы в массиве символов

---

## Question 19: map iteration

Гарантирован ли порядок итерации по map?

A) Да, в порядке вставки

B) Да, в алфавитном порядке ключей

C) Нет, порядок не определён

D) Да, в обратном порядке вставки

---

## Question 20: type switch

Какой синтаксис правильный для type switch?

A) `switch v.type { }`

B) `switch v := x.(type) { }`

C) `switch typeof(x) { }`

D) `switch v := type(x) { }`

---

## Question 21: Early return

Какой код лучше с точки зрения читаемости?

A) Вложенные if-else

B) Early return с проверкой условий

C) Всегда использовать switch

D) goto statements

---

## Question 22: Присваивание в if

Какое утверждение верно об объявлении переменной в if?

A) Переменная видна во всей функции

B) Переменная видна только в блоке if-else

C) Переменная видна в пакете

D) Такое объявление невозможно

---

## Question 23: default в switch

Где должен располагаться default в switch?

A) Только в начале

B) Только в конце

C) В любом месте

D) После break

---

## Question 24: for range и модификация

Что произойдёт при изменении v в цикле?

```go
nums := []int{1, 2, 3}
for _, v := range nums {
    v = v * 2
}
```

A) nums станет [2, 4, 6]

B) nums останется [1, 2, 3]

C) Ошибка компиляции

D) Runtime panic

---

## Question 25: goto ограничения

Какое ограничение есть у goto в Go?

A) goto запрещён в Go

B) goto не может перепрыгивать через объявления переменных

C) goto можно использовать только в циклах

D) goto требует специального import

---

## Question 26: defer и panic

Выполняются ли defer-вызовы при panic?

A) Да

B) Нет

C) Только если есть recover

D) Зависит от типа panic

---

## Question 27: Пустой for

Что представляет собой `for {}`?

A) Синтаксическую ошибку

B) Бесконечный цикл

C) Пустой цикл, который ничего не делает

D) Цикл с нулём итераций

---

## Question 28: switch с инициализацией

Какой код корректен?

A) `switch x := getValue(); x { case 1: ... }`

B) `switch x := getValue() { case 1: ... }`

C) `switch (x := getValue()) x { case 1: ... }`

D) `switch getValue() as x { case 1: ... }`

---

## Question 29: defer с методами

Что выведет код?

```go
type Counter struct{ value int }
func (c *Counter) Print() { fmt.Println(c.value) }

func main() {
    c := Counter{10}
    defer c.Print()
    c.value = 20
}
```

A) 10

B) 20

C) 0

D) Ошибка компиляции

---

## Question 30: Множественный defer

Что выведет код?

```go
defer fmt.Print("1 ")
defer fmt.Print("2 ")
defer fmt.Print("3 ")
fmt.Print("start ")
```

A) start 1 2 3

B) 1 2 3 start

C) start 3 2 1

D) 3 2 1 start

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | В Go условия if не требуют круглых скобок, но фигурные обязательны. |
| 2 | A | `if x := getValue(); x > 0 { }` — корректный синтаксис с инициализацией. |
| 3 | B | В Go только один тип цикла — for. |
| 4 | B | `for x < 10 { }` — while-стиль в Go. |
| 5 | C | `for { }` — бесконечный цикл в Go. |
| 6 | B | range возвращает индекс и значение. Выводятся индексы: 0 1 2. |
| 7 | B | `for i := range slice` — опускаем второе значение для получения только индексов. |
| 8 | B | В Go break не нужен — каждый case завершается автоматически. |
| 9 | B | `case 1, 2, 3:` — множественные значения через запятую. |
| 10 | B | 15 < 20, поэтому выполнится второй case: "medium". |
| 11 | B | fallthrough безусловно переходит к следующему case. |
| 12 | B | defer выполняются в порядке LIFO (стек). |
| 13 | B | defer выполняются при выходе из функции. |
| 14 | A | Аргументы defer вычисляются при объявлении. x был 10. |
| 15 | C | defer-ы выполняются после done в порядке LIFO: done 2 1 0. |
| 16 | B | Метки с break позволяют выйти из внешних вложенных циклов. |
| 17 | B | continue пропускает оставшуюся часть текущей итерации. |
| 18 | B | range по строке возвращает руны и их байтовые позиции. |
| 19 | C | Порядок итерации по map не определён и может меняться. |
| 20 | B | `switch v := x.(type)` — синтаксис type switch. |
| 21 | B | Early return уменьшает вложенность и улучшает читаемость. |
| 22 | B | Переменная в if видна только в блоке if-else. |
| 23 | C | default может быть в любом месте switch. |
| 24 | B | v — копия. Изменение v не влияет на nums. |
| 25 | B | goto не может перепрыгивать через объявления переменных. |
| 26 | A | defer-вызовы выполняются даже при panic. |
| 27 | B | `for {}` — бесконечный цикл. |
| 28 | A | `switch x := getValue(); x { case 1: }` — корректный синтаксис. |
| 29 | B | Метод вызывается при defer, но c.value уже изменён на 20. |
| 30 | C | defer LIFO: сначала start, затем 3 2 1. |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили управление потоком в Go. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы defer и switch. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о циклах и defer. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---

