# Python Exceptions - Quiz

Проверьте свои знания по теме "Исключения и обработка ошибок".

---

## Question 1: Базовый класс исключений


Какой класс является базовым для всех встроенных исключений?

A) `Throwable`

B) `Error`

C) `BaseException`

D) `Exception`

---

## Question 2: try/except


Что произойдёт если исключение не перехвачено?

A) Исключение будет проигнорировано

B) Программа продолжит выполнение

C) Вернётся None

D) Программа завершится с traceback

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

C) Ничего

D) Оба

---

## Question 4: Порядок except


Почему важен порядок блоков except?

A) Более специфичные исключения должны быть раньше общих

B) Для производительности

C) Порядок не важен

D) Для читаемости кода

---

## Question 5: Перехват нескольких исключений


Какой синтаксис для перехвата нескольких типов исключений одним блоком?

A) `except [ValueError, TypeError]:`

B) `except ValueError or TypeError:`

C) `except (ValueError, TypeError):`

D) `except ValueError, TypeError:`

---

## Question 6: Доступ к исключению


Как получить доступ к объекту исключения?

A) `except Error as e:`

B) `except Error e:`

C) `catch(Error e):`

D) `except e = Error:`

---

## Question 7: else в try


Когда выполняется блок else в try/except?

A) После finally

B) Если исключение было перехвачено

C) Всегда

D) Если исключение НЕ возникло

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

A) `raise`

B) `reraise`

C) `throw`

D) `raise Exception`

---

## Question 10: Создание исключения


Как вызвать исключение с сообщением?

A) `raise ValueError, "message"`

B) `error ValueError("message")`

C) `raise ValueError("message")`

D) `throw ValueError("message")`

---

## Question 11: Цепочка исключений


Как сохранить информацию об оригинальном исключении?

A) `raise NewError(original)`

B) `raise NewError from original`

C) `raise NewError + original`

D) `raise NewError.chain(original)`

---

## Question 12: Пользовательские исключения


От какого класса следует наследовать пользовательские исключения?

A) `Exception`

B) `object`

C) `Error`

D) `BaseException`

---

## Question 13: KeyError


Когда возникает KeyError?

A) При обращении к несуществующему индексу списка

B) При нажатии клавиши

C) При обращении к несуществующему ключу словаря

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

A) 3

B) KeyError

C) IndexError

D) None

---

## Question 15: TypeError


Когда возникает TypeError?

A) При операции с несовместимыми типами

B) При ошибке синтаксиса

C) При обращении к несуществующему атрибуту

D) При делении на ноль

---

## Question 16: AttributeError


Что вызовет следующий код?

```python
x = 5
x.append(10)
```

A) IndexError

B) AttributeError

C) ValueError

D) TypeError

---

## Question 17: assert


Что делает оператор `assert`?

A) Создаёт новую переменную

B) Проверяет условие и вызывает AssertionError если оно ложно

C) Импортирует модуль

D) Выводит сообщение в консоль

---

## Question 18: Отключение assert


Как отключить assert в production?

A) `assert.disable()`

B) `python -O script.py`

C) `python --no-assert script.py`

D) Нельзя отключить

---

## Question 19: EAFP


Что означает принцип EAFP?

A) Error Always Follows Protocol

B) Error Analysis For Python

C) Exception And Finally Processing

D) Easier to Ask Forgiveness than Permission

---

## Question 20: EAFP vs LBYL


Какой код соответствует принципу EAFP?

A) `if key in dict: value = dict[key]`

B) `if dict.has_key(key): ...`

C) `try: value = dict[key] except KeyError: ...`

D) `value = dict.get(key, default)`

---

## Question 21: Context Manager


Что гарантирует конструкция `with open(...) as f:`?

A) Закрытие файла даже при исключении

B) Кэширование файла

C) Блокировку файла

D) Быстрое чтение файла

---

## Question 22: __enter__ и __exit__


Какие методы нужны для создания контекстного менеджера?

A) `__enter__` and `__exit__`

B) `__open__` и `__close__`

C) `__init__` и `__del__`

D) `__start__` и `__stop__`

---

## Question 23: suppress


Что делает `contextlib.suppress`?

A) Игнорирует указанные исключения

B) Записывает исключения в лог

C) Останавливает выполнение

D) Подавляет вывод в консоль

---

## Question 24: Логирование исключений


Как правильно логировать исключение с traceback?

A) `logger.exception("Error")`

B) `logger.error(e.traceback)`

C) `logger.error(str(e))`

D) `print(traceback)`

---

## Question 25: Иерархия исключений


Какое исключение является подклассом ArithmeticError?

A) KeyError

B) ZeroDivisionError

C) TypeError

D) ValueError

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | `BaseException` — корень иерархии. `Exception` — для "обычных" исключений. |
| 2 | D | Неперехваченное исключение завершает программу с выводом traceback. |
| 3 | B | Деление на ноль вызывает ZeroDivisionError, который и перехватывается. |
| 4 | A | Более специфичные (дочерние) исключения должны быть раньше родительских. |
| 5 | C | Кортеж исключений в скобках: `except (ValueError, TypeError):`. |
| 6 | A | Синтаксис Python 3: `except Error as e:`. |
| 7 | D | `else` выполняется, если в try-блоке НЕ возникло исключение. |
| 8 | C | `finally` выполняется всегда — для очистки ресурсов. |
| 9 | A | Пустой `raise` повторно вызывает текущее исключение. |
| 10 | C | `raise ValueError("message")` — стандартный синтаксис Python 3. |
| 11 | B | `raise NewError from original` сохраняет цепочку (exception chaining). |
| 12 | A | Пользовательские исключения должны наследовать от `Exception`. |
| 13 | C | KeyError — доступ к несуществующему ключу словаря. |
| 14 | C | Выход за границы списка — IndexError, не KeyError. |
| 15 | A | TypeError — операция с несовместимыми типами (напр., "2" + 2). |
| 16 | B | int не имеет метода append — AttributeError. |
| 17 | B | `assert condition, "message"` — проверка инвариантов. |
| 18 | B | Флаг `-O` (optimize) отключает assert и `__debug__`. |
| 19 | D | EAFP — "Проще попросить прощения, чем разрешения" — пробуй, ловий исключения. |
| 20 | C | EAFP: сначала пробуем, потом обрабатываем исключение. |
| 21 | A | `with` гарантирует вызов `__exit__` (закрытие) даже при исключении. |
| 22 | A | Контекстный менеджер требует `__enter__` и `__exit__`. |
| 23 | A | `suppress(ValueError)` тихо игнорирует ValueError в блоке with. |
| 24 | A | `logger.exception()` автоматически добавляет traceback. |
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

