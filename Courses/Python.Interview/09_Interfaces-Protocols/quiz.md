# Интерфейсы и протоколы — Quiz

Проверьте понимание ABC, протоколов и duck typing.

---

## Question 1: Duck Typing

Что означает duck typing в Python?

A) Динамическое создание типов

B) Проверяем не тип объекта, а наличие нужных методов

C) Специальный тип для работы с птицами

D) Типизация через аннотации

---

## Question 2: Hashable

Какой тип НЕ является hashable?

A) tuple

B) int

C) str

D) list

---

## Question 3: Iterable протокол

Какой метод делает объект iterable?

A) `__len__()`

B) `__next__()`

C) `__iter__()`

D) `__contains__()`

---

## Question 4: ABC abstractmethod

Что произойдёт при попытке создать экземпляр абстрактного класса?

A) Вызовется метод по умолчанию

B) Ничего, это разрешено

C) TypeError — нельзя создать экземпляр абстрактного класса

D) Создастся пустой объект

---

## Question 5: Callable

Как проверить, можно ли вызвать объект как функцию?

A) `isinstance(obj, Function)`

B) `type(obj) == function`

C) `hasattr(obj, '__run__')`

D) `callable(obj)` или `isinstance(obj, Callable)`

---

## Question 6: collections.abc

Какой ABC проверяет, что объект можно использовать как словарь?

A) Sequence

B) Iterable

C) Container

D) Mapping

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Duck typing: проверяем методы, а не тип |
| 2 | D | list — mutable, поэтому не hashable |
| 3 | C | `__iter__()` делает объект iterable |
| 4 | C | TypeError при попытке создать экземпляр ABC |
| 5 | D | `callable()` — встроенная функция, или isinstance с Callable |
| 6 | D | Mapping — для словарь-подобных объектов |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по протоколам |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите ABC и protocols |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите collections.abc |

---

