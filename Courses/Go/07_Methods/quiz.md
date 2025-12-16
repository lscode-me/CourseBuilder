# Methods and Interfaces - Quiz

Проверьте свои знания по теме "Методы, интерфейсы, полиморфизм и embedding".

---

## Question 1: Синтаксис метода

Какой синтаксис определения метода правильный?

A) `func Circle.Area() float64 {}`

B) `def Circle::Area() float64 {}`

C) `func (c Circle) Area() float64 {}`

D) `method Area(c Circle) float64 {}`

---

## Question 2: Receiver

Что такое receiver в методе Go?

A) Возвращаемое значение

B) Параметр функции

C) Тип, к которому привязан метод

D) Имя метода

---

## Question 3: Value receiver

Что происходит при вызове метода с value receiver?

A) Ошибка компиляции

B) Метод работает с копией

C) Метод работает с оригиналом

D) Зависит от размера структуры

---

## Question 4: Интерфейс

Как определить интерфейс в Go?

A) `class Shape { abstract Area() float64 }`

B) `interface Shape { Area() float64 }`

C) `type Shape interface { Area() float64 }`

D) `protocol Shape { Area() float64 }`

---

## Question 5: Реализация интерфейса

Как тип реализует интерфейс в Go?

A) Через ключевое слово `implements`

B) Неявно — имея все методы интерфейса

C) Через наследование

D) Через регистрацию

---

## Question 6: Пустой интерфейс

Что принимает `interface{}`?

A) Любой тип

B) Только nil

C) Только примитивные типы

D) Только структуры

---

## Question 7: any

Что такое `any` в Go 1.18+?

A) Generics constraint

B) Ключевое слово для dynamic typing

C) Алиас для `interface{}`

D) Новый примитивный тип

---

## Question 8: Type assertion

Какой синтаксис type assertion?

A) `cast(value, Type)`

B) `value as Type`

C) `(Type)value`

D) `value.(Type)`

---

## Question 9: Безопасный type assertion

Как проверить успешность type assertion?

A) `i.isType(Type)`

B) `try-catch`

C) `typeof(i) == Type`

D) `v, ok := i.(Type)`

---

## Question 10: Type switch

Какой синтаксис type switch?

A) `typeswitch i`

B) `switch typeof(i)`

C) `switch v := i.(type)`

D) `switch i.(type)`

---

## Question 11: Embedding

Что такое embedding в Go?

A) Вложенные функции

B) Встраивание типа без имени поля

C) Инлайн функций

D) Импорт пакета

---

## Question 12: Наследование методов

Что происходит с методами embedded типа?

A) Они недоступны

B) Требуется явное делегирование

C) Они становятся методами внешнего типа

D) Они копируются

---

## Question 13: Переопределение метода

Можно ли переопределить метод embedded типа?

A) Нет

B) Только для публичных методов

C) Да, определив метод с тем же именем

D) Только через override

---

## Question 14: Композиция интерфейсов

Как объединить интерфейсы?

A) `type RW extends Reader, Writer`

B) `type RW implements Reader, Writer`

C) `type RW interface { Reader; Writer }`

D) `type RW = Reader + Writer`

---

## Question 15: nil interface

Когда интерфейсная переменная равна nil?

A) Никогда

B) Всегда по умолчанию

C) Когда тип и значение nil

D) Когда значение nil

---

## Question 16: Pointer receiver и интерфейс

Если метод имеет pointer receiver, какой тип реализует интерфейс?

A) Только указатель

B) Зависит от интерфейса

C) Оба

D) Только значение

---

## Question 17: fmt.Stringer

Какой метод нужен для fmt.Stringer?

A) `String() string`

B) `Format() string`

C) `Print() string`

D) `ToString() string`

---

## Question 18: Полиморфизм

Как реализуется полиморфизм в Go?

A) Через интерфейсы

B) Через макросы

C) Через generics только

D) Через наследование классов

---

## Question 19: Методы на built-in типах

Можно ли добавить методы к `int`?

A) Только в main пакете

B) Невозможно

C) Да, напрямую

D) Нет, но можно через type alias

---

## Question 20: Доступ к полям embedded

Как получить поле embedded структуры?

A) Только через имя embedded типа

B) Через reflection

C) Через getter

D) Через точечную нотацию напрямую

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

A) Через runtime check

B) Через unit тесты

C) Компилятор проверяет автоматически

D) Через reflection

---

## Question 23: Метод на nil receiver

Можно ли вызвать метод на nil указателе?

A) Ошибка компиляции

B) Нет, всегда panic

C) Только value receiver

D) Да, если метод это обрабатывает

---

## Question 24: Множественное embedding

Что произойдёт при конфликте имён?

A) Первый embedded выигрывает

B) Последний embedded выигрывает

C) Нужно обращаться через имя типа

D) Ошибка компиляции

---

## Question 25: Интерфейс с одним методом

Как называется интерфейс с одним методом?

A) Functional interface

B) Single-method interface

C) По соглашению: имя метода + "er"

D) Simple interface

---

## Question 26: Пустой интерфейс в слайсе

Какой тип у `[]interface{}{1, "a", true}`?

A) []any

B) mixed slice

C) []interface{}

D) []int

---

## Question 27: Type assertion panic

Когда type assertion вызывает panic?

A) При nil interface

B) Только при форме без ok

C) Никогда

D) Всегда при неуспехе

---

## Question 28: Интерфейс и nil value

Что выведет код?

```go

var p *MyType = nil
var i interface{} = p
fmt.Println(i == nil)

```

A) false

B) Panic

C) Ошибка компиляции

D) true

---

## Question 29: Receiver conventions

Когда использовать pointer receiver?

A) Всегда

B) Когда нужно изменять состояние или структура большая

C) Никогда

D) Только для публичных методов

---

## Question 30: Embedding указателя

Можно ли embed указатель на структуру?

A) Только для приватных структур

B) Да

C) Нет

D) Только в интерфейсах

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `func (c Circle) Area() float64 {}` — правильный синтаксис метода. |
| 2 | C | Receiver — тип, к которому привязан метод. |
| 3 | B | Value receiver работает с копией структуры. |
| 4 | C | `type Shape interface { ... }` — определение интерфейса. |
| 5 | B | В Go интерфейсы реализуются неявно — наличием всех методов. |
| 6 | A | `interface{}` (пустой интерфейс) принимает любой тип. |
| 7 | C | `any` — алиас для `interface{}`, введённый в Go 1.18. |
| 8 | D | `value.(Type)` — синтаксис type assertion. |
| 9 | D | `v, ok := i.(Type)` — безопасная форма с проверкой. |
| 10 | C | `switch v := i.(type)` — type switch. |
| 11 | B | Embedding — встраивание типа без имени поля. |
| 12 | C | Методы embedded типа становятся методами внешнего типа. |
| 13 | C | Да, определив метод с тем же именем во внешнем типе. |
| 14 | C | `type RW interface { Reader; Writer }` — композиция. |
| 15 | C | Интерфейс nil когда и тип, и значение nil. |
| 16 | A | Только *T реализует интерфейс, не T. |
| 17 | A | `String() string` — метод для fmt.Stringer. |
| 18 | A | Полиморфизм через интерфейсы. |
| 19 | D | Через type alias: `type MyInt int`. |
| 20 | D | Можно напрямую: `s.EmbeddedField`. |
| 21 | B | `any` — алиас для `interface{}`. |
| 22 | C | Компилятор проверяет при присваивании. |
| 23 | D | Можно, если метод обрабатывает nil. |
| 24 | C | При конфликте нужно обращаться через имя типа. |
| 25 | C | По соглашению: Reader, Writer, Stringer и т.д. |
| 26 | C | Тип слайса: `[]interface{}`. |
| 27 | B | Panic только при `i.(Type)` без ok. |
| 28 | A | false — интерфейс содержит тип *MyType с nil значением. |
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



