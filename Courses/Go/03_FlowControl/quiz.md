# Flow Control - Quiz

Проверьте свои знания по теме "Условия, циклы, switch и defer".

---

## Question 1: Синтаксис if

Какой синтаксис if корректен в Go?

A) `if x > 0 { fmt.Println("positive") }`

B) `if x > 0 fmt.Println("positive")`

C) `if x > 0 then { fmt.Println("positive") }`

D) `if (x > 0) { fmt.Println("positive") }`

---

## Question 2: if с инициализацией

Какой код корректно использует if с инициализацией?

A) `if x = getValue(); x > 0 { }`

B) `if x := getValue() then x > 0 { }`

C) `if x := getValue(); x > 0 { }`

D) `if (x := getValue()) x > 0 { }`

---

## Question 3: Циклы в Go

Сколько типов циклов есть в Go?

A) 1 (только for)

B) 3 (for, while, do-while)

C) 0 (нет циклов)

D) 2 (for и while)

---

## Question 4: while-стиль

Какой код эквивалентен `while x < 10` в Go?

A) `while x < 10 { }`

B) `for x < 10 { }`

C) `loop x < 10 { }`

D) `do { } while x < 10`

---

## Question 5: Бесконечный цикл

Как написать бесконечный цикл в Go?

A) `loop { }`

B) `for (;;) { }`

C) `for { }`

D) `while true { }`

---

## Question 6: for range

Что выведет код?

```go

for i, v := range []int{10, 20, 30} {
    fmt.Print(i, " ")
}

```

A) 0 10 1 20 2 30

B) 0 1 2

C) 10 20 30

D) Ошибка компиляции

---

## Question 7: Игнорирование значения

Как итерировать по слайсу, используя только индексы?

A) `for i := range slice { }`

B) `for i in slice { }`

C) `for i, _ := range slice { }`

D) `for i only range slice { }`

---

## Question 8: switch и break

Нужен ли break в конце case в Go switch?

A) Зависит от типа данных

B) Нет, break автоматический

C) Да, но только для default

D) Да, обязательно

---

## Question 9: Множественные значения case

Какой синтаксис позволяет проверить несколько значений в одном case?

A) `case 1 || 2 || 3:`

B) `case [1, 2, 3]:`

C) `case 1, 2, 3:`

D) `case 1 or 2 or 3:`

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

A) medium

B) small

C) large

D) small medium

---

## Question 11: fallthrough

Что делает ключевое слово fallthrough?

A) Перезапускает switch

B) Переходит к следующему case безусловно

C) Проверяет условие следующего case

D) Прерывает выполнение switch

---

## Question 12: defer порядок

В каком порядке выполняются defer-вызовы?

A) LIFO (Last In, First Out)

B) Порядок объявления

C) FIFO (First In, First Out)

D) Случайный порядок

---

## Question 13: defer выполнение

Когда выполняются defer-вызовы?

A) В конце программы

B) При вызове panic

C) Сразу после объявления

D) При выходе из функции

---

## Question 14: defer и аргументы

Что выведет код?

```go

x := 10
defer fmt.Println(x)
x = 20

```

A) Ошибка компиляции

B) 10

C) Ничего

D) 20

---

## Question 15: defer в цикле

Что выведет код?

```go

for i := 0; i < 3; i++ {
    defer fmt.Print(i, " ")
}
fmt.Print("done ")

```

A) 2 1 0 done

B) 0 1 2 done

C) done 0 1 2

D) done 2 1 0

---

## Question 16: break с меткой

Для чего используются метки с break?

A) Для перехода к метке

B) Для пропуска итерации

C) Для выхода из вложенных циклов

D) Для выхода из функции

---

## Question 17: continue

Что делает continue в цикле?

A) Пропускает оставшийся код итерации

B) Переходит к следующему switch case

C) Перезапускает цикл

D) Выходит из цикла

---

## Question 18: for range и строка

Что возвращает range при итерации по строке?

A) Символы (runes) и их байтовые позиции

B) Только символы

C) Символы и их индексы в массиве символов

D) Байты

---

## Question 19: map iteration

Гарантирован ли порядок итерации по map?

A) Да, в порядке вставки

B) Нет, порядок не определён

C) Да, в алфавитном порядке ключей

D) Да, в обратном порядке вставки

---

## Question 20: type switch

Какой синтаксис правильный для type switch?

A) `switch typeof(x) { }`

B) `switch v.type { }`

C) `switch v := type(x) { }`

D) `switch v := x.(type) { }`

---

## Question 21: Early return

Какой код лучше с точки зрения читаемости?

A) Всегда использовать switch

B) Вложенные if-else

C) goto statements

D) Early return с проверкой условий

---

## Question 22: Присваивание в if

Какое утверждение верно об объявлении переменной в if?

A) Переменная видна во всей функции

B) Переменная видна в пакете

C) Переменная видна только в блоке if-else

D) Такое объявление невозможно

---

## Question 23: default в switch

Где должен располагаться default в switch?

A) Только в начале

B) После break

C) Только в конце

D) В любом месте

---

## Question 24: for range и модификация

Что произойдёт при изменении v в цикле?

```go

nums := []int{1, 2, 3}
for _, v := range nums {
    v = v * 2
}

```

A) Ошибка компиляции

B) Runtime panic

C) nums станет [2, 4, 6]

D) nums останется [1, 2, 3]

---

## Question 25: goto ограничения

Какое ограничение есть у goto в Go?

A) goto требует специального import

B) goto можно использовать только в циклах

C) goto запрещён в Go

D) goto не может перепрыгивать через объявления переменных

---

## Question 26: defer и panic

Выполняются ли defer-вызовы при panic?

A) Нет

B) Зависит от типа panic

C) Да

D) Только если есть recover

---

## Question 27: Пустой for

Что представляет собой `for {}`?

A) Бесконечный цикл

B) Синтаксическую ошибку

C) Пустой цикл, который ничего не делает

D) Цикл с нулём итераций

---

## Question 28: switch с инициализацией

Какой код корректен?

A) `switch x := getValue() { case 1: ... }`

B) `switch getValue() as x { case 1: ... }`

C) `switch (x := getValue()) x { case 1: ... }`

D) `switch x := getValue(); x { case 1: ... }`

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

A) Ошибка компиляции

B) 0

C) 10

D) 20

---

## Question 30: Множественный defer

Что выведет код?

```go

defer fmt.Print("1 ")
defer fmt.Print("2 ")
defer fmt.Print("3 ")
fmt.Print("start ")

```

A) start 3 2 1

B) start 1 2 3

C) 3 2 1 start

D) 1 2 3 start

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | В Go условия if не требуют круглых скобок, но фигурные обязательны. |
| 2 | C | `if x := getValue(); x > 0 { }` — корректный синтаксис с инициализацией. |
| 3 | A | В Go только один тип цикла — for. |
| 4 | B | `for x < 10 { }` — while-стиль в Go. |
| 5 | C | `for { }` — бесконечный цикл в Go. |
| 6 | B | range возвращает индекс и значение. Выводятся индексы: 0 1 2. |
| 7 | A | `for i := range slice` — опускаем второе значение для получения только индексов. |
| 8 | B | В Go break не нужен — каждый case завершается автоматически. |
| 9 | C | `case 1, 2, 3:` — множественные значения через запятую. |
| 10 | A | 15 < 20, поэтому выполнится второй case: "medium". |
| 11 | B | fallthrough безусловно переходит к следующему case. |
| 12 | A | defer выполняются в порядке LIFO (стек). |
| 13 | D | defer выполняются при выходе из функции. |
| 14 | B | Аргументы defer вычисляются при объявлении. x был 10. |
| 15 | D | defer-ы выполняются после done в порядке LIFO: done 2 1 0. |
| 16 | C | Метки с break позволяют выйти из внешних вложенных циклов. |
| 17 | A | continue пропускает оставшуюся часть текущей итерации. |
| 18 | A | range по строке возвращает руны и их байтовые позиции. |
| 19 | B | Порядок итерации по map не определён и может меняться. |
| 20 | D | `switch v := x.(type)` — синтаксис type switch. |
| 21 | D | Early return уменьшает вложенность и улучшает читаемость. |
| 22 | C | Переменная в if видна только в блоке if-else. |
| 23 | D | default может быть в любом месте switch. |
| 24 | D | v — копия. Изменение v не влияет на nums. |
| 25 | D | goto не может перепрыгивать через объявления переменных. |
| 26 | C | defer-вызовы выполняются даже при panic. |
| 27 | A | `for {}` — бесконечный цикл. |
| 28 | D | `switch x := getValue(); x { case 1: }` — корректный синтаксис. |
| 29 | D | Метод вызывается при defer, но c.value уже изменён на 20. |
| 30 | A | defer LIFO: сначала start, затем 3 2 1. |

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



