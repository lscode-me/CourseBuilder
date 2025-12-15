# Протокол итерации — Quiz

Проверьте своё понимание итераторов, генераторов и протокола итерации в Python.

---

## Question 1: Iterable vs Iterator

Какие методы должен реализовать объект, чтобы быть **итератором** (Iterator)?

A) Только `__iter__()`

B) Только `__next__()`

C) `__iter__()` и `__next__()`

D) `__iter__()`, `__next__()` и `__len__()`

---

## Question 2: range() — итератор?

Что произойдёт при выполнении этого кода?

```python

r = range(5)
print(next(r))
```

A) Выведет `0`

B) Выведет `range(0, 5)`

C) TypeError: 'range' object is not an iterator

D) StopIteration

---

## Question 3: Generator expression

Чем отличается generator expression от list comprehension?

A) Ничем, это синтаксический сахар

B) Generator expression вычисляется лениво и не хранит все значения в памяти

C) List comprehension быстрее generator expression

D) Generator expression нельзя использовать в for-цикле

---

## Question 4: Второй аргумент next()

Что вернёт этот код?

```python

it = iter([1, 2, 3])
next(it)
next(it)
next(it)
result = next(it, "empty")
print(result)
```

A) StopIteration exception

B) None

C) "empty"

D) 3

---

## Question 5: Closure в comprehension

Что выведет этот код?

```python

funcs = [lambda x: x * i for i in range(3)]
print(funcs[0](10))
```

A) 0

B) 10

C) 20

D) 30

---

## Question 6: yield vs return

Что делает ключевое слово `yield` в функции?

A) Возвращает значение и завершает функцию

B) Возвращает значение и приостанавливает выполнение функции до следующего вызова next()

C) Создаёт список из всех значений

D) Вызывает исключение StopIteration

---

## Question 7: iter() с двумя аргументами

Что делает `iter(callable, sentinel)`?

A) Вызывает callable дважды

B) Вызывает callable пока не получит значение sentinel, затем останавливается

C) Возвращает sentinel если callable вызывает исключение

D) Это недопустимый синтаксис

---

---

## Answer Key

| # | Ответ | Пояснение |
|---|-------|-----------|
| 1 | C | Iterator должен реализовать `__iter__()` (возвращает self) и `__next__()` |
| 2 | C | `range()` — это iterable, но не iterator. Нужно вызвать `iter(r)` |
| 3 | B | Generator expression вычисляет значения лениво (lazy evaluation), экономя память |
| 4 | C | Второй аргумент next() возвращается вместо StopIteration когда итератор исчерпан |
| 5 | C | Closure захватывает переменную i по ссылке. К моменту вызова i=2, поэтому 10*2=20 |
| 6 | B | `yield` приостанавливает функцию и превращает её в генератор |
| 7 | B | `iter(callable, sentinel)` вызывает callable до получения sentinel |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **6-7 правильных (85-100%)** | 🏆 Отлично! | Вы готовы к вопросам по итерации |
| **4-5 правильных (57-71%)** | ✅ Хорошо | Повторите closure и lazy evaluation |
| **Менее 4 правильных (<57%)** | 📚 Нужно повторить | Перечитайте лекцию и напишите код |

---


