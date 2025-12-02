# Python Exceptions - Quiz

Проверьте свои знания по теме "Исключения и обработка ошибок".

---

## Question 1: Базовый класс исключений

Какой класс является базовым для всех встроенных исключений?

A) `Error`

B) `Exception`

C) `BaseException`

D) `Throwable`

---

## Question 2: try/except

Что произойдёт если исключение не перехвачено?

A) Программа продолжит выполнение

B) Программа завершится с traceback

C) Исключение будет проигнорировано

D) Вернётся None

---

## Question 3: Множественные except

Что выведет следующий код?

```python
try:
    result = 10 / 0
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
```

A) ValueError

B) ZeroDivisionError

C) Оба

D) Ничего

---

## Question 4: Порядок except

Почему важен порядок блоков except?

A) Для производительности

B) Более специфичные исключения должны быть раньше общих

C) Порядок не важен

D) Для читаемости кода

---

## Question 5: Перехват нескольких исключений

Какой синтаксис для перехвата нескольких типов исключений одним блоком?

A) `except ValueError, TypeError:`

B) `except ValueError or TypeError:`

C) `except (ValueError, TypeError):`

D) `except [ValueError, TypeError]:`

---

## Question 6: Доступ к исключению

Как получить доступ к объекту исключения?

A) `except Error e:`

B) `except Error as e:`

C) `except e = Error:`

D) `catch(Error e):`

---

## Question 7: else в try

Когда выполняется блок else в try/except?

A) Всегда

B) Если исключение было перехвачено

C) Если исключение НЕ возникло

D) После finally

---

## Question 8: finally

Когда выполняется блок finally?

A) Только если было исключение

B) Только если не было исключения

C) Всегда, независимо от исключений

D) Только при явном вызове

---

## Question 9: raise

Как повторно вызвать текущее исключение?

A) `throw`

B) `raise`

C) `reraise`

D) `raise Exception`

---

## Question 10: Создание исключения

Как вызвать исключение с сообщением?

A) `raise ValueError, "message"`

B) `raise ValueError("message")`

C) `throw ValueError("message")`

D) `error ValueError("message")`

---

## Question 11: Цепочка исключений

Как сохранить информацию об оригинальном исключении?

A) `raise NewError from original`

B) `raise NewError(original)`

C) `raise NewError.chain(original)`

D) `raise NewError + original`

---

## Question 12: Пользовательские исключения

От какого класса следует наследовать пользовательские исключения?

A) `BaseException`

B) `Exception`

C) `Error`

D) `object`

---

## Question 13: KeyError

Когда возникает KeyError?

A) При обращении к несуществующему индексу списка

B) При обращении к несуществующему ключу словаря

C) При нажатии клавиши

D) При ошибке шифрования

---

## Question 14: IndexError vs KeyError

Что выведет следующий код?

```python
lst = [1, 2, 3]
try:
    print(lst[10])
except KeyError:
    print("KeyError")
except IndexError:
    print("IndexError")
```

A) KeyError

B) IndexError

C) None

D) 3

---

## Question 15: TypeError

Когда возникает TypeError?

A) При ошибке синтаксиса

B) При операции с несовместимыми типами

C) При обращении к несуществующему атрибуту

D) При делении на ноль

---

## Question 16: AttributeError

Что вызовет следующий код?

```python
x = 5
x.append(10)
```

A) TypeError

B) AttributeError

C) ValueError

D) IndexError

---

## Question 17: assert

Что делает оператор `assert`?

A) Проверяет условие и вызывает AssertionError если оно ложно

B) Выводит сообщение в консоль

C) Создаёт новую переменную

D) Импортирует модуль

---

## Question 18: Отключение assert

Как отключить assert в production?

A) `python --no-assert script.py`

B) `python -O script.py`

C) `assert.disable()`

D) Нельзя отключить

---

## Question 19: EAFP

Что означает принцип EAFP?

A) Error Always Follows Protocol

B) Easier to Ask Forgiveness than Permission

C) Exception And Finally Processing

D) Error Analysis For Python

---

## Question 20: EAFP vs LBYL

Какой код соответствует принципу EAFP?

A) `if key in dict: value = dict[key]`

B) `try: value = dict[key] except KeyError: ...`

C) `value = dict.get(key, default)`

D) `if dict.has_key(key): ...`

---

## Question 21: Context Manager

Что гарантирует конструкция `with open(...) as f:`?

A) Быстрое чтение файла

B) Закрытие файла даже при исключении

C) Кэширование файла

D) Блокировку файла

---

## Question 22: __enter__ и __exit__

Какие методы нужны для создания контекстного менеджера?

A) `__start__` и `__stop__`

B) `__enter__` and `__exit__`

C) `__open__` и `__close__`

D) `__init__` и `__del__`

---

## Question 23: suppress

Что делает `contextlib.suppress`?

A) Подавляет вывод в консоль

B) Игнорирует указанные исключения

C) Записывает исключения в лог

D) Останавливает выполнение

---

## Question 24: Логирование исключений

Как правильно логировать исключение с traceback?

A) `logger.error(str(e))`

B) `logger.exception("Error")`

C) `logger.error(e.traceback)`

D) `print(traceback)`

---

## Question 25: Иерархия исключений

Какое исключение является подклассом ArithmeticError?

A) ValueError

B) ZeroDivisionError

C) TypeError

D) KeyError

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `BaseException` — корень иерархии. `Exception` — для "обычных" исключений. |
| 2 | B | Неперехваченное исключение завершает программу с выводом traceback. |
| 3 | B | Деление на ноль вызывает ZeroDivisionError, который и перехватывается. |
| 4 | B | Более специфичные (дочерние) исключения должны быть раньше родительских. |
| 5 | C | Кортеж исключений в скобках: `except (ValueError, TypeError):`. |
| 6 | B | Синтаксис Python 3: `except Error as e:`. |
| 7 | C | `else` выполняется, если в try-блоке НЕ возникло исключение. |
| 8 | C | `finally` выполняется всегда — для очистки ресурсов. |
| 9 | B | Пустой `raise` повторно вызывает текущее исключение. |
| 10 | B | `raise ValueError("message")` — стандартный синтаксис Python 3. |
| 11 | A | `raise NewError from original` сохраняет цепочку (exception chaining). |
| 12 | B | Пользовательские исключения должны наследовать от `Exception`. |
| 13 | B | KeyError — доступ к несуществующему ключу словаря. |
| 14 | B | Выход за границы списка — IndexError, не KeyError. |
| 15 | B | TypeError — операция с несовместимыми типами (напр., "2" + 2). |
| 16 | B | int не имеет метода append — AttributeError. |
| 17 | A | `assert condition, "message"` — проверка инвариантов. |
| 18 | B | Флаг `-O` (optimize) отключает assert и `__debug__`. |
| 19 | B | EAFP — "Проще попросить прощения, чем разрешения" — пробуй, ловий исключения. |
| 20 | B | EAFP: сначала пробуем, потом обрабатываем исключение. |
| 21 | B | `with` гарантирует вызов `__exit__` (закрытие) даже при исключении. |
| 22 | B | Контекстный менеджер требует `__enter__` и `__exit__`. |
| 23 | B | `suppress(ValueError)` тихо игнорирует ValueError в блоке with. |
| 24 | B | `logger.exception()` автоматически добавляет traceback. |
| 25 | B | ZeroDivisionError, OverflowError, FloatingPointError — подклассы ArithmeticError. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное понимание обработки исключений! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите контекстные менеджеры. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на иерархию исключений и EAFP. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию с практическими примерами. |

---

