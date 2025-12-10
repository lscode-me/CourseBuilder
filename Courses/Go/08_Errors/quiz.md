# Error Handling - Quiz

Проверьте свои знания по теме "Обработка ошибок в Go".

---

## Question 1: Интерфейс error

Какой метод должен реализовать тип для error interface?

A) `String() string`

B) `Error() string`

C) `Message() string`

D) `ToString() string`

---

## Question 2: Создание ошибки

Какая функция создаёт простую ошибку?

A) `error.New("message")`

B) `errors.New("message")`

C) `new(error, "message")`

D) `Error("message")`

---

## Question 3: Проверка ошибки

Как проверить наличие ошибки?

A) `if err { }`

B) `if err != nil { }`

C) `if error(err) { }`

D) `if err.exists() { }`

---

## Question 4: fmt.Errorf

Для чего используется `fmt.Errorf`?

A) Только для форматирования

B) Для создания ошибки с форматированием

C) Для логирования ошибок

D) Для панических ситуаций

---

## Question 5: Error wrapping

Какой формат оборачивает ошибку?

A) `fmt.Errorf("msg: %v", err)`

B) `fmt.Errorf("msg: %w", err)`

C) `fmt.Errorf("msg: %e", err)`

D) `fmt.Errorf("msg: %wrap", err)`

---

## Question 6: errors.Is

Что проверяет `errors.Is(err, target)`?

A) Равенство строк ошибок

B) Равенство типов ошибок

C) Наличие target в цепочке ошибок

D) Только прямое равенство

---

## Question 7: errors.As

Для чего используется `errors.As`?

A) Для преобразования ошибки в строку

B) Для поиска ошибки определённого типа в цепочке

C) Для сравнения ошибок

D) Для логирования ошибок

---

## Question 8: Sentinel errors

Что такое sentinel error?

A) Ошибка безопасности

B) Предопределённая ошибка для сравнения

C) Ошибка в guard clause

D) Критическая ошибка

---

## Question 9: io.EOF

Как обрабатывать io.EOF?

A) Как обычную ошибку

B) Как сигнал конца данных (не ошибка)

C) Через panic/recover

D) Игнорировать

---

## Question 10: Custom error type

Какой код правильно определяет custom error?

A) `type MyError string`

B) `type MyError struct { msg string } func (e MyError) Error() string { return e.msg }`

C) `type MyError extends Error`

D) `error MyError { msg string }`

---

## Question 11: panic

Когда использовать panic?

A) Для всех ошибок

B) Для невосстановимых ситуаций

C) Вместо return error

D) Для пользовательских ошибок

---

## Question 12: recover

Где можно вызвать recover?

A) В любом месте

B) Только в defer

C) Только в main

D) В catch блоке

---

## Question 13: errors.Unwrap

Что возвращает `errors.Unwrap`?

A) Строку ошибки

B) Обёрнутую ошибку (если есть)

C) Nil всегда

D) Новую ошибку

---

## Question 14: Игнорирование ошибки

Как правильно игнорировать ошибку?

A) `file, _ := os.Open("f.txt")`

B) `file := os.Open("f.txt")`

C) `file, nil := os.Open("f.txt")`

D) `file, ignore := os.Open("f.txt")`

---

## Question 15: Multiple return

Где должна быть ошибка в возвращаемых значениях?

A) Первой

B) Последней

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

A) Никогда

B) После успешного открытия ресурса

C) Только для файлов

D) Только с panic

---

## Question 18: Error chain

Какой код создаёт цепочку ошибок?

A) `return err + newErr`

B) `return fmt.Errorf("context: %w", err)`

C) `return errors.Chain(err, newErr)`

D) `return append(err, newErr)`

---

## Question 19: Проверка типа ошибки

Как проверить тип ошибки без errors.As?

A) `if err.type == MyError`

B) `if myErr, ok := err.(*MyError); ok`

C) `if typeof(err) == MyError`

D) `if err instanceof MyError`

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

C) Для логирования

D) Для сравнения ошибок

---

## Question 23: Обработка множественных ошибок

Как обработать несколько ошибок в функции?

A) Вернуть первую ошибку

B) Объединить через errors.Join или slice

C) Игнорировать все кроме последней

D) Panic при первой ошибке

---

## Question 24: Error context

Какую информацию добавлять при wrapping?

A) Stack trace

B) Контекст операции

C) Время ошибки

D) Всё вышеперечисленное

---

## Question 25: Must functions

Для чего используется паттерн Must?

A) Для обязательных полей

B) Для panic при ошибке (в init или main)

C) Для валидации

D) Для retry логики

---

## Question 26: Error в defer

Как вернуть ошибку из defer?

A) Через именованное возвращаемое значение

B) Через return в defer

C) Через глобальную переменную

D) Невозможно

---

## Question 27: Nil interface vs nil value

Когда `err != nil` но `err.Error()` паникует?

A) Никогда

B) Когда err содержит nil pointer конкретного типа

C) При неправильной имплементации

D) При panic в Error()

---

## Question 28: Log или return?

Что делать с ошибкой: логировать или возвращать?

A) Всегда логировать

B) Всегда возвращать

C) Логировать ИЛИ возвращать, не оба

D) Делать оба всегда

---

## Question 29: errors.Is vs ==

Почему предпочтительнее errors.Is?

A) Быстрее

B) Проверяет цепочку обёрнутых ошибок

C) Красивее

D) Единственный способ

---

## Question 30: Retry logic

Как реализовать retry при временных ошибках?

A) Всегда retry 3 раза

B) Проверить тип ошибки, retry если recoverable

C) Никогда не retry

D) Через panic/recover

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `Error() string` — метод интерфейса error. |
| 2 | B | `errors.New("message")` создаёт простую ошибку. |
| 3 | B | `if err != nil` — стандартная проверка ошибки. |
| 4 | B | `fmt.Errorf` создаёт форматированную ошибку. |
| 5 | B | `%w` — спецификатор для wrapping. |
| 6 | C | errors.Is проверяет всю цепочку обёрнутых ошибок. |
| 7 | B | errors.As ищет ошибку определённого типа в цепочке. |
| 8 | B | Sentinel error — предопределённая ошибка (var ErrNotFound). |
| 9 | B | io.EOF — сигнал конца данных, не ошибка. |
| 10 | B | Структура с методом Error() string. |
| 11 | B | panic — для невосстановимых ситуаций. |
| 12 | B | recover работает только внутри defer. |
| 13 | B | Unwrap возвращает wrapped error. |
| 14 | A | `_, _ := ...` или `_, err := ...; _ = err`. |
| 15 | B | По соглашению error последний. |
| 16 | B | `return nil` означает успех. |
| 17 | B | defer для cleanup после успешного открытия ресурса. |
| 18 | B | `fmt.Errorf("...: %w", err)` создаёт цепочку. |
| 19 | B | Type assertion: `myErr, ok := err.(*MyError)`. |
| 20 | B | Маленькие буквы, без точки — для композиции. |
| 21 | B | Все defer выполнятся перед завершением. |
| 22 | B | errors.Join объединяет несколько ошибок. |
| 23 | B | Вернуть первую или объединить через Join. |
| 24 | B | Добавляем контекст операции. |
| 25 | B | Must паникует при ошибке. |
| 26 | A | Через именованное возвращаемое значение. |
| 27 | B | Interface с nil pointer конкретного типа. |
| 28 | C | Логировать ИЛИ возвращать, не оба. |
| 29 | B | errors.Is проверяет wrapped errors. |
| 30 | B | Retry только для recoverable ошибок. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете обработку ошибок. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите error wrapping и errors.Is/As. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о sentinel errors. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

