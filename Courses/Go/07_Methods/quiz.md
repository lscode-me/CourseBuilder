# Methods and Interfaces - Quiz

Проверьте свои знания по теме "Методы, интерфейсы, полиморфизм и embedding".

---

## Question 1: Синтаксис метода

Какой синтаксис определения метода правильный?

A) `func Circle.Area() float64 {}`

B) `func (c Circle) Area() float64 {}`

C) `method Area(c Circle) float64 {}`

D) `def Circle::Area() float64 {}`

---

## Question 2: Receiver

Что такое receiver в методе Go?

A) Параметр функции

B) Возвращаемое значение

C) Тип, к которому привязан метод

D) Имя метода

---

## Question 3: Value receiver

Что происходит при вызове метода с value receiver?

A) Метод работает с оригиналом

B) Метод работает с копией

C) Ошибка компиляции

D) Зависит от размера структуры

---

## Question 4: Интерфейс

Как определить интерфейс в Go?

A) `interface Shape { Area() float64 }`

B) `type Shape interface { Area() float64 }`

C) `class Shape { abstract Area() float64 }`

D) `protocol Shape { Area() float64 }`

---

## Question 5: Реализация интерфейса

Как тип реализует интерфейс в Go?

A) Через ключевое слово `implements`

B) Через наследование

C) Неявно — имея все методы интерфейса

D) Через регистрацию

---

## Question 6: Пустой интерфейс

Что принимает `interface{}`?

A) Только nil

B) Только структуры

C) Любой тип

D) Только примитивные типы

---

## Question 7: any

Что такое `any` в Go 1.18+?

A) Новый примитивный тип

B) Алиас для `interface{}`

C) Generics constraint

D) Ключевое слово для dynamic typing

---

## Question 8: Type assertion

Какой синтаксис type assertion?

A) `value.(Type)`

B) `value as Type`

C) `(Type)value`

D) `cast(value, Type)`

---

## Question 9: Безопасный type assertion

Как проверить успешность type assertion?

A) `try-catch`

B) `v, ok := i.(Type)`

C) `i.isType(Type)`

D) `typeof(i) == Type`

---

## Question 10: Type switch

Какой синтаксис type switch?

A) `switch i.(type)`

B) `switch v := i.(type)`

C) `switch typeof(i)`

D) `typeswitch i`

---

## Question 11: Embedding

Что такое embedding в Go?

A) Инлайн функций

B) Встраивание типа без имени поля

C) Импорт пакета

D) Вложенные функции

---

## Question 12: Наследование методов

Что происходит с методами embedded типа?

A) Они недоступны

B) Они становятся методами внешнего типа

C) Они копируются

D) Требуется явное делегирование

---

## Question 13: Переопределение метода

Можно ли переопределить метод embedded типа?

A) Нет

B) Да, определив метод с тем же именем

C) Только через override

D) Только для публичных методов

---

## Question 14: Композиция интерфейсов

Как объединить интерфейсы?

A) `type RW = Reader + Writer`

B) `type RW interface { Reader; Writer }`

C) `type RW extends Reader, Writer`

D) `type RW implements Reader, Writer`

---

## Question 15: nil interface

Когда интерфейсная переменная равна nil?

A) Когда значение nil

B) Когда тип и значение nil

C) Никогда

D) Всегда по умолчанию

---

## Question 16: Pointer receiver и интерфейс

Если метод имеет pointer receiver, какой тип реализует интерфейс?

A) Только значение

B) Только указатель

C) Оба

D) Зависит от интерфейса

---

## Question 17: fmt.Stringer

Какой метод нужен для fmt.Stringer?

A) `ToString() string`

B) `String() string`

C) `Format() string`

D) `Print() string`

---

## Question 18: Полиморфизм

Как реализуется полиморфизм в Go?

A) Через наследование классов

B) Через интерфейсы

C) Через generics только

D) Через макросы

---

## Question 19: Методы на built-in типах

Можно ли добавить методы к `int`?

A) Да, напрямую

B) Нет, но можно через type alias

C) Только в main пакете

D) Невозможно

---

## Question 20: Доступ к полям embedded

Как получить поле embedded структуры?

A) Через точечную нотацию напрямую

B) Только через имя embedded типа

C) Через getter

D) Через reflection

---

## Question 21: interface{} vs any

В чём разница между `interface{}` и `any`?

A) any быстрее

B) Разницы нет, any — алиас

C) any более строгий

D) interface{} устарел

---

## Question 22: Проверка реализации

Как проверить, реализует ли тип интерфейс?

A) Компилятор проверяет автоматически

B) Через runtime check

C) Через reflection

D) Через unit тесты

---

## Question 23: Метод на nil receiver

Можно ли вызвать метод на nil указателе?

A) Нет, всегда panic

B) Да, если метод это обрабатывает

C) Ошибка компиляции

D) Только value receiver

---

## Question 24: Множественное embedding

Что произойдёт при конфликте имён?

A) Ошибка компиляции

B) Нужно обращаться через имя типа

C) Последний embedded выигрывает

D) Первый embedded выигрывает

---

## Question 25: Интерфейс с одним методом

Как называется интерфейс с одним методом?

A) Single-method interface

B) Functional interface

C) По соглашению: имя метода + "er"

D) Simple interface

---

## Question 26: Пустой интерфейс в слайсе

Какой тип у `[]interface{}{1, "a", true}`?

A) []int

B) []any

C) []interface{}

D) mixed slice

---

## Question 27: Type assertion panic

Когда type assertion вызывает panic?

A) Всегда при неуспехе

B) Только при форме без ok

C) Никогда

D) При nil interface

---

## Question 28: Интерфейс и nil value

Что выведет код?

```go

var p *MyType = nil
var i interface{} = p
fmt.Println(i == nil)

```

A) true

B) false

C) Ошибка компиляции

D) Panic

---

## Question 29: Receiver conventions

Когда использовать pointer receiver?

A) Всегда

B) Когда нужно изменять состояние или структура большая

C) Только для публичных методов

D) Никогда

---

## Question 30: Embedding указателя

Можно ли embed указатель на структуру?

A) Нет

B) Да

C) Только в интерфейсах

D) Только для приватных структур

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `func (c Circle) Area() float64 {}` — правильный синтаксис метода. |
| 2 | C | Receiver — тип, к которому привязан метод. |
| 3 | B | Value receiver работает с копией структуры. |
| 4 | B | `type Shape interface { ... }` — определение интерфейса. |
| 5 | C | В Go интерфейсы реализуются неявно — наличием всех методов. |
| 6 | C | `interface{}` (пустой интерфейс) принимает любой тип. |
| 7 | B | `any` — алиас для `interface{}`, введённый в Go 1.18. |
| 8 | A | `value.(Type)` — синтаксис type assertion. |
| 9 | B | `v, ok := i.(Type)` — безопасная форма с проверкой. |
| 10 | B | `switch v := i.(type)` — type switch. |
| 11 | B | Embedding — встраивание типа без имени поля. |
| 12 | B | Методы embedded типа становятся методами внешнего типа. |
| 13 | B | Да, определив метод с тем же именем во внешнем типе. |
| 14 | B | `type RW interface { Reader; Writer }` — композиция. |
| 15 | B | Интерфейс nil когда и тип, и значение nil. |
| 16 | B | Только *T реализует интерфейс, не T. |
| 17 | B | `String() string` — метод для fmt.Stringer. |
| 18 | B | Полиморфизм через интерфейсы. |
| 19 | B | Через type alias: `type MyInt int`. |
| 20 | A | Можно напрямую: `s.EmbeddedField`. |
| 21 | B | `any` — алиас для `interface{}`. |
| 22 | A | Компилятор проверяет при присваивании. |
| 23 | B | Можно, если метод обрабатывает nil. |
| 24 | B | При конфликте нужно обращаться через имя типа. |
| 25 | C | По соглашению: Reader, Writer, Stringer и т.д. |
| 26 | C | Тип слайса: `[]interface{}`. |
| 27 | B | Panic только при `i.(Type)` без ok. |
| 28 | B | false — интерфейс содержит тип *MyType с nil значением. |
| 29 | B | Pointer receiver для изменения состояния или больших структур. |
| 30 | B | Да, можно embed `*Type`. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете ООП в Go. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите интерфейсы и embedding. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о type assertions. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---



