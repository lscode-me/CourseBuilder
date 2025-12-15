# Изменяемость (Mutability) — Quiz

Проверьте понимание mutable/immutable типов и связанных ловушек.

---

## Question 1: Mutable Default Argument

Что выведет этот код?

```python

def f(n, lst=[]):
    lst.append(n)
    return lst

print(f(1))
print(f(2))
```

A) `[1]` затем `[2]`

B) `[1]` затем `[1, 2]`

C) `[]` затем `[]`

D) Ошибка

---

## Question 2: Immutable типы

Какой из этих типов является immutable?

A) list

B) dict

C) tuple

D) set

---

## Question 3: Копирование списка

Что выведет код?

```python

a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

A) `[1, 2, 3]`

B) `[1, 2, 3, 4]`

C) `[4]`

D) Ошибка

---

## Question 4: Ключи словаря

Какой тип НЕЛЬЗЯ использовать как ключ словаря?

A) str

B) tuple

C) list

D) int

---

## Question 5: Tuple с mutable элементами

Что произойдёт при выполнении?

```python

t = ([1, 2], [3, 4])
t[0].append(5)
```

A) TypeError — tuple immutable

B) Успешно: t станет ([1, 2, 5], [3, 4])

C) Успешно: t станет ([5], [3, 4])

D) IndexError

---

## Question 6: Правильный default argument

Как правильно написать функцию с опциональным списком?

A) `def f(lst=[]):`

B) `def f(lst=None): lst = lst or []`

C) `def f(lst=list()):`

D) `def f(lst=()):`

---

---

## Answer Key

| # | Ответ | Пояснение |
|---|-------|-----------|
| 1 | B | Default list создаётся один раз и переиспользуется между вызовами |
| 2 | C | tuple — immutable. list, dict, set — mutable |
| 3 | B | `b = a` создаёт ссылку на тот же объект, изменение b меняет a |
| 4 | C | list — mutable, поэтому не hashable и не может быть ключом |
| 5 | B | tuple хранит ссылки, сам список можно изменять |
| 6 | B | None как default, создание нового списка внутри функции |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по mutability |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите ловушки с default arguments |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите разницу mutable/immutable |

---


