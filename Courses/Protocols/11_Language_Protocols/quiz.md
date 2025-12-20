# Языковые протоколы - Quiz

Проверьте свои знания по теме "Языковые протоколы".

---

## Question 1: Python PEP

Что такое PEP?

A) База данных

B) Только для экспертов

C) Python Enhancement Proposal — документ, описывающий изменения/стандарты Python

D) Язык программирования

---

## Question 2: PEP 8

Что описывает PEP 8?

A) Модули

B) Type hints

C) Асинхронность

D) Style Guide — правила форматирования кода Python

---

## Question 3: PEP 484

Что описывает PEP 484?

A) Walrus operator

B) F-strings

C) Type Hints — аннотации типов в Python

D) Async/await

---

## Question 4: PEP 3107

Что описывает PEP 3107?

A) Match statement

B) Function Annotations — синтаксис аннотаций функций

C) Async/await

D) Type hints

---

## Question 5: PEP 492

Что описывает PEP 492?

A) Match statement

B) F-strings

C) Async/await синтаксис для корутин

D) Type hints

---

## Question 6: Протокол import

Какие методы входят в протокол import в Python?

A) Только import

B) Не используется

C) Только from

D) __import__(), sys.path, finder, loader механизмы

---

## Question 7: __init__.py

Зачем нужен __init__.py в Python пакетах?

A) Не нужен

B) Обозначает директорию как пакет (до Python 3.3 обязательно)

C) Только для функций

D) Только для классов

---

## Question 8: __all__

Что определяет __all__ в модуле?

A) Все переменные

B) Только функции

C) Список имён, экспортируемых при import *

D) Не используется

---

## Question 9: Python descriptor протокол

Где используется descriptor протокол?

A) Только для классов

B) Нигде

C) Только для функций

D) property, classmethod, staticmethod используют descriptor протокол

---

## Question 10: Metaclass

Что такое metaclass в Python?

A) Только для модулей

B) Не используется

C) Обычный класс

D) Класс классов — определяет поведение создания классов

---

## Question 11: __new__ vs __init__

В чём отличие __new__ от __init__?

A) Нет отличий

B) __new__ создаёт объект, __init__ инициализирует

C) __new__ только для классов

D) Не используются

---

## Question 12: Protocol для pattern matching

Что описывает PEP 622/634/635?

A) Async/await

B) Structural Pattern Matching (match statement в Python 3.10+)

C) Type hints

D) F-strings

---

## Question 13: Context manager протокол в других языках

Есть ли аналог context manager в других языках?

A) Только в Python

B) Да, например using в C#, try-with-resources в Java

C) Не используется

D) Нет

---

## Question 14: Iterator протокол в других языках

Есть ли аналог iterator протокола в других языках?

A) Нет

B) Только в Python

C) Не используется

D) Да, Iterator/Iterable в Java, IEnumerable в C#

---

## Question 15: Callable протокол в других языках

Есть ли аналог callable в других языках?

A) Нет

B) Не используется

C) Только в Python

D) Да, функциональные объекты (functors в C++, callable objects в Java)

---

## Question 16: Type system в Python

Какой тип системы в Python?

A) Статическая, слабая

B) Динамическая, слабая

C) Динамическая, сильная (типы проверяются в runtime, но строго)

D) Статическая, сильная

---

## Question 17: Static typing в Python

Как добавить статическую проверку типов в Python?

A) Использовать type hints + mypy/pyright

B) Только для классов

C) Невозможно

D) Python всегда статический

---

## Question 18: TypedDict

Что такое TypedDict в Python?

A) Не используется

B) Способ аннотировать типы для словарей с определённой структурой

C) Обычный dict

D) Только для JSON

---

## Question 19: Generics в Python

Что такое Generics (например, List[int])?

A) Параметризованные типы для коллекций и функций

B) Только для списков

C) Не используется

D) Обычные типы

---

## Question 20: Protocol vs ABC

Когда использовать Protocol вместо ABC?

A) Всегда ABC

B) Не используется

C) Нет отличий

D) Protocol для structural typing (duck typing), ABC для nominal typing

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | PEP — Python Enhancement Proposal, документ, описывающий изменения/стандарты Python. |
| 2 | D | PEP 8 — Style Guide для форматирования кода Python. |
| 3 | C | PEP 484 — Type Hints (аннотации типов в Python). |
| 4 | B | PEP 3107 — Function Annotations (синтаксис аннотаций функций). |
| 5 | C | PEP 492 — Async/await синтаксис для корутин. |
| 6 | D | Протокол import включает __import__(), sys.path, finder, loader механизмы. |
| 7 | B | __init__.py обозначает директорию как пакет (обязательно до Python 3.3). |
| 8 | C | __all__ определяет список имён, экспортируемых при import *. |
| 9 | D | property, classmethod, staticmethod используют descriptor протокол. |
| 10 | D | Metaclass — класс классов, определяет поведение создания классов. |
| 11 | B | __new__ создаёт объект, __init__ инициализирует. |
| 12 | B | PEP 622/634/635 — Structural Pattern Matching (match statement в Python 3.10+). |
| 13 | B | Аналоги context manager: using в C#, try-with-resources в Java. |
| 14 | D | Аналоги iterator: Iterator/Iterable в Java, IEnumerable в C#. |
| 15 | D | Аналоги callable: functors в C++, callable objects в Java. |
| 16 | C | Python — динамическая, сильная типизация (типы проверяются в runtime, но строго). |
| 17 | A | Использовать type hints + mypy/pyright для статической проверки типов. |
| 18 | B | TypedDict — способ аннотировать типы для словарей с определённой структурой. |
| 19 | A | Generics — параметризованные типы для коллекций и функций (List[int]). |
| 20 | D | Protocol для structural typing (duck typing), ABC для nominal typing. |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы, в которых ошиблись. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать соответствующие разделы лекции. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---

