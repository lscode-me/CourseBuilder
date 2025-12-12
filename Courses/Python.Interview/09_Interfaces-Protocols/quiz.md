# Интерфейсы и протоколы — Quiz

Проверьте понимание ABC, протоколов и duck typing.

---

## Question 1: Duck Typing

Что означает duck typing в Python?

A) Специальный тип для работы с птицами

B) Проверяем не тип объекта, а наличие нужных методов

C) Динамическое создание типов

D) Типизация через аннотации

---

## Question 2: Hashable

Какой тип НЕ является hashable?

A) str

B) tuple

C) list

D) int

---

## Question 3: Iterable протокол

Какой метод делает объект iterable?

A) `__next__()`

B) `__iter__()`

C) `__len__()`

D) `__contains__()`

---

## Question 4: ABC abstractmethod

Что произойдёт при попытке создать экземпляр абстрактного класса?

A) Создастся пустой объект

B) TypeError — нельзя создать экземпляр абстрактного класса

C) Вызовется метод по умолчанию

D) Ничего, это разрешено

---

## Question 5: Callable

Как проверить, можно ли вызвать объект как функцию?

A) `isinstance(obj, Function)`

B) `callable(obj)` или `isinstance(obj, Callable)`

C) `hasattr(obj, '__run__')`

D) `type(obj) == function`

---

## Question 6: collections.abc

Какой ABC проверяет, что объект можно использовать как словарь?

A) Iterable

B) Sequence

C) Mapping

D) Container

---

---

## Answer Key

| # | Ответ | Пояснение |
|---|-------|-----------|
| 1 | B | Duck typing: проверяем методы, а не тип |
| 2 | C | list — mutable, поэтому не hashable |
| 3 | B | `__iter__()` делает объект iterable |
| 4 | B | TypeError при попытке создать экземпляр ABC |
| 5 | B | `callable()` — встроенная функция, или isinstance с Callable |
| 6 | C | Mapping — для словарь-подобных объектов |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по протоколам |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите ABC и protocols |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите collections.abc |

---

