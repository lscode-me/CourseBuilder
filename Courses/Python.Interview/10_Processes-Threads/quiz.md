# Процессы и потоки — Quiz

Проверьте понимание concurrency в Python.

---

## Question 1: GIL

Что такое GIL в Python?

A) Global Interpreter Lock — mutex, позволяющий только одному потоку выполнять Python код

B) Garbage Interrupt Lock

C) Способ синхронизации процессов

D) Библиотека для работы с графикой

---

## Question 2: Threads vs Processes

Что лучше использовать для CPU-bound задач?

A) multiprocessing

B) asyncio

C) threading

D) Всё одинаково эффективно

---

## Question 3: Race Condition

Почему `self.val += 1` может привести к race condition?

A) Python не поддерживает сложение

B) GIL защищает от race conditions

C) Операция не атомарна: read-modify-write

D) Это синтаксическая ошибка

---

## Question 4: Память

Как threads и processes отличаются по работе с памятью?

A) Оба имеют общую память

B) Threads имеют раздельную память, processes — общую

C) Threads имеют общую память, processes — раздельную

D) Оба имеют раздельную память

---

## Question 5: I/O-bound

Какой инструмент лучше для I/O-bound задач (сетевые запросы)?

A) multiprocessing

B) threading или asyncio

C) subprocess

D) Только single-threaded код

---

## Question 6: Threading Lock

Как правильно использовать Lock для защиты от race condition?

A) Оба варианта правильные

B) `with lock: code`

C) Lock не защищает от race conditions

D) `lock.acquire(); code; lock.release()`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | GIL позволяет только одному потоку выполнять Python байткод |
| 2 | A | multiprocessing обходит GIL, каждый процесс имеет свой |
| 3 | C | += состоит из read, modify, write — между ними может вклиниться другой поток |
| 4 | C | Threads делят память процесса, processes имеют раздельную |
| 5 | B | threading или asyncio эффективны для I/O из-за GIL |
| 6 | A | Оба способа работают, with — предпочтительнее (безопаснее) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по concurrency |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите GIL и race conditions |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите threading vs multiprocessing |

---

