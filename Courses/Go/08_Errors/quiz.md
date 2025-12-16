# Error Handling - Quiz

Проверьте свои знания по теме "Обработка ошибок в Go".

---

## Question 1: Интерфейс error

Какой метод должен реализовать тип для error interface?

A) `ToString() string`

B) `Message() string`

C) `Error() string`

D) `String() string`

---

## Question 2: Создание ошибки

Какая функция создаёт простую ошибку?

A) `Error("message")`

B) `new(error, "message")`

C) `errors.New("message")`

D) `error.New("message")`

---

## Question 3: Проверка ошибки

Как проверить наличие ошибки?

A) `if err != nil { }`

B) `if err { }`

C) `if error(err) { }`

D) `if err.exists() { }`

---

## Question 4: fmt.Errorf

Для чего используется `fmt.Errorf`?

A) Для логирования ошибок

B) Для создания ошибки с форматированием

C) Только для форматирования

D) Для панических ситуаций

---

## Question 5: Error wrapping

Какой формат оборачивает ошибку?

A) `fmt.Errorf("msg: %v", err)`

B) `fmt.Errorf("msg: %e", err)`

C) `fmt.Errorf("msg: %w", err)`

D) `fmt.Errorf("msg: %wrap", err)`

---

## Question 6: errors.Is

Что проверяет `errors.Is(err, target)`?

A) Только прямое равенство

B) Равенство строк ошибок

C) Равенство типов ошибок

D) Наличие target в цепочке ошибок

---

## Question 7: errors.As

Для чего используется `errors.As`?

A) Для логирования ошибок

B) Для сравнения ошибок

C) Для поиска ошибки определённого типа в цепочке

D) Для преобразования ошибки в строку

---

## Question 8: Sentinel errors

Что такое sentinel error?

A) Ошибка безопасности

B) Ошибка в guard clause

C) Критическая ошибка

D) Предопределённая ошибка для сравнения

---

## Question 9: io.EOF

Как обрабатывать io.EOF?

A) Игнорировать

B) Как сигнал конца данных (не ошибка)

C) Как обычную ошибку

D) Через panic/recover

---

## Question 10: Custom error type

Какой код правильно определяет custom error?

A) `error MyError { msg string }`

B) `type MyError struct { msg string } func (e MyError) Error() string { return e.msg }`

C) `type MyError string`

D) `type MyError extends Error`

---

## Question 11: panic

Когда использовать panic?

A) Для всех ошибок

B) Вместо return error

C) Для пользовательских ошибок

D) Для невосстановимых ситуаций

---

## Question 12: recover

Где можно вызвать recover?

A) В любом месте

B) В catch блоке

C) Только в defer

D) Только в main

---

## Question 13: errors.Unwrap

Что возвращает `errors.Unwrap`?

A) Обёрнутую ошибку (если есть)

B) Новую ошибку

C) Nil всегда

D) Строку ошибки

---

## Question 14: Игнорирование ошибки

Как правильно игнорировать ошибку?

A) `file, nil := os.Open("f.txt")`

B) `file := os.Open("f.txt")`

C) `file, ignore := os.Open("f.txt")`

D) `file, _ := os.Open("f.txt")`

---

## Question 15: Multiple return

Где должна быть ошибка в возвращаемых значениях?

A) Последней

B) Первой

C) В середине

D) Не важно

---

## Question 16: nil error

Что означает `return nil` для ошибки?

A) Неизвестная ошибка

B) Операция успешна

C) Пустая ошибка

D) Нужна проверка

---

## Question 17: Defer и ошибки

Когда использовать defer для cleanup?

A) После успешного открытия ресурса

B) Только для файлов

C) Никогда

D) Только с panic

---

## Question 18: Error chain

Какой код создаёт цепочку ошибок?

A) `return append(err, newErr)`

B) `return fmt.Errorf("context: %w", err)`

C) `return err + newErr`

D) `return errors.Chain(err, newErr)`

---

## Question 19: Проверка типа ошибки

Как проверить тип ошибки без errors.As?

A) `if err.type == MyError`

B) `if typeof(err) == MyError`

C) `if err instanceof MyError`

D) `if myErr, ok := err.(*MyError); ok`

---

## Question 20: Error message style

Какой стиль сообщений ошибок рекомендуется?

A) С заглавной буквы и точкой

B) С маленькой буквы без точки

C) Всё CAPS

D) Не важно

---

## Question 21: Panic recovery

Что произойдёт с отложенными defer при panic?

A) Они не выполнятся

B) Они выполнятся перед завершением

C) Только первый defer

D) Зависит от типа panic

---

## Question 22: errors.Join (Go 1.20+)

Для чего используется `errors.Join`?

A) Для объединения строк ошибок

B) Для создания ошибки из нескольких ошибок

C) Для сравнения ошибок

D) Для логирования

---

## Question 23: Обработка множественных ошибок

Как обработать несколько ошибок в функции?

A) Вернуть первую ошибку

B) Panic при первой ошибке

C) Объединить через errors.Join или slice

D) Игнорировать все кроме последней

---

## Question 24: Error context

Какую информацию добавлять при wrapping?

A) Всё вышеперечисленное

B) Время ошибки

C) Stack trace

D) Контекст операции

---

## Question 25: Must functions

Для чего используется паттерн Must?

A) Для panic при ошибке (в init или main)

B) Для retry логики

C) Для обязательных полей

D) Для валидации

---

## Question 26: Error в defer

Как вернуть ошибку из defer?

A) Через глобальную переменную

B) Невозможно

C) Через именованное возвращаемое значение

D) Через return в defer

---

## Question 27: Nil interface vs nil value

Когда `err != nil` но `err.Error()` паникует?

A) Никогда

B) Когда err содержит nil pointer конкретного типа

C) При panic в Error()

D) При неправильной имплементации

---

## Question 28: Log или return?

Что делать с ошибкой: логировать или возвращать?

A) Логировать ИЛИ возвращать, не оба

B) Всегда возвращать

C) Делать оба всегда

D) Всегда логировать

---

## Question 29: errors.Is vs ==

Почему предпочтительнее errors.Is?

A) Красивее

B) Быстрее

C) Единственный способ

D) Проверяет цепочку обёрнутых ошибок

---

## Question 30: Retry logic

Как реализовать retry при временных ошибках?

A) Проверить тип ошибки, retry если recoverable

B) Через panic/recover

C) Всегда retry 3 раза

D) Никогда не retry

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `Error() string` — метод интерфейса error. |
| 2 | C | `errors.New("message")` создаёт простую ошибку. |
| 3 | A | `if err != nil` — стандартная проверка ошибки. |
| 4 | B | `fmt.Errorf` создаёт форматированную ошибку. |
| 5 | C | `%w` — спецификатор для wrapping. |
| 6 | D | errors.Is проверяет всю цепочку обёрнутых ошибок. |
| 7 | C | errors.As ищет ошибку определённого типа в цепочке. |
| 8 | D | Sentinel error — предопределённая ошибка (var ErrNotFound). |
| 9 | B | io.EOF — сигнал конца данных, не ошибка. |
| 10 | B | Структура с методом Error() string. |
| 11 | D | panic — для невосстановимых ситуаций. |
| 12 | C | recover работает только внутри defer. |
| 13 | A | Unwrap возвращает wrapped error. |
| 14 | D | `_, _ := ...` или `_, err := ...; _ = err`. |
| 15 | A | По соглашению error последний. |
| 16 | B | `return nil` означает успех. |
| 17 | A | defer для cleanup после успешного открытия ресурса. |
| 18 | B | `fmt.Errorf("...: %w", err)` создаёт цепочку. |
| 19 | D | Type assertion: `myErr, ok := err.(*MyError)`. |
| 20 | B | Маленькие буквы, без точки — для композиции. |
| 21 | B | Все defer выполнятся перед завершением. |
| 22 | B | errors.Join объединяет несколько ошибок. |
| 23 | C | Вернуть первую или объединить через Join. |
| 24 | D | Добавляем контекст операции. |
| 25 | A | Must паникует при ошибке. |
| 26 | C | Через именованное возвращаемое значение. |
| 27 | B | Interface с nil pointer конкретного типа. |
| 28 | A | Логировать ИЛИ возвращать, не оба. |
| 29 | D | errors.Is проверяет wrapped errors. |
| 30 | A | Retry только для recoverable ошибок. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете обработку ошибок. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите error wrapping и errors.Is/As. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о sentinel errors. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

