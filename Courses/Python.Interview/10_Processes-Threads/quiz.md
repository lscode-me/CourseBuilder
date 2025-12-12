# Процессы и потоки — Quiz

Проверьте понимание concurrency в Python.

---

## Question 1: GIL

Что такое GIL в Python?

A) Библиотека для работы с графикой

B) Global Interpreter Lock — mutex, позволяющий только одному потоку выполнять Python код

C) Garbage Interrupt Lock

D) Способ синхронизации процессов

---

## Question 2: Threads vs Processes

Что лучше использовать для CPU-bound задач?

A) threading

B) multiprocessing

C) asyncio

D) Всё одинаково эффективно

---

## Question 3: Race Condition

Почему `self.val += 1` может привести к race condition?

A) Python не поддерживает сложение

B) Операция не атомарна: read-modify-write

C) GIL защищает от race conditions

D) Это синтаксическая ошибка

---

## Question 4: Память

Как threads и processes отличаются по работе с памятью?

A) Threads имеют раздельную память, processes — общую

B) Threads имеют общую память, processes — раздельную

C) Оба имеют раздельную память

D) Оба имеют общую память

---

## Question 5: I/O-bound

Какой инструмент лучше для I/O-bound задач (сетевые запросы)?

A) multiprocessing

B) threading или asyncio

C) Только single-threaded код

D) subprocess

---

## Question 6: Threading Lock

Как правильно использовать Lock для защиты от race condition?

A) `lock.acquire(); code; lock.release()`

B) `with lock: code`

C) Оба варианта правильные

D) Lock не защищает от race conditions

---

---

## Answer Key

| # | Ответ | Пояснение |
|---|-------|-----------|
| 1 | B | GIL позволяет только одному потоку выполнять Python байткод |
| 2 | B | multiprocessing обходит GIL, каждый процесс имеет свой |
| 3 | B | += состоит из read, modify, write — между ними может вклиниться другой поток |
| 4 | B | Threads делят память процесса, processes имеют раздельную |
| 5 | B | threading или asyncio эффективны для I/O из-за GIL |
| 6 | C | Оба способа работают, with — предпочтительнее (безопаснее) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по concurrency |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите GIL и race conditions |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите threading vs multiprocessing |

---

