# Python Exceptions - Quiz

Проверьте свои знания по теме "Исключения и обработка ошибок".

---

## Question 1: Базовый класс исключений





Какой класс является базовым для всех встроенных исключений?

A) `Throwable`

B) `BaseException`

C) `Error`

D) `Exception`

---

## Question 2: try/except





Что произойдёт если исключение не перехвачено?

A) Программа продолжит выполнение

B) Вернётся None

C) Исключение будет проигнорировано

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

A) ZeroDivisionError

B) ValueError

C) Оба

D) Ничего

---

## Question 4: Порядок except





Почему важен порядок блоков except?

A) Для производительности

B) Для читаемости кода

C) Более специфичные исключения должны быть раньше общих

D) Порядок не важен

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

A) `catch(Error e):`

B) `except e = Error:`

C) `except Error as e:`

D) `except Error e:`

---

## Question 7: else в try





Когда выполняется блок else в try/except?

A) Если исключение было перехвачено

B) Если исключение НЕ возникло

C) После finally

D) Всегда

---

## Question 8: finally





Когда выполняется блок finally?

A) Всегда, независимо от исключений

B) Только при явном вызове

C) Только если не было исключения

D) Только если было исключение

---

## Question 9: raise





Как повторно вызвать текущее исключение?

A) `raise Exception`

B) `raise`

C) `reraise`

D) `throw`

---

## Question 10: Создание исключения





Как вызвать исключение с сообщением?

A) `error ValueError("message")`

B) `raise ValueError, "message"`

C) `raise ValueError("message")`

D) `throw ValueError("message")`

---

## Question 11: Цепочка исключений





Как сохранить информацию об оригинальном исключении?

A) `raise NewError + original`

B) `raise NewError.chain(original)`

C) `raise NewError from original`

D) `raise NewError(original)`

---

## Question 12: Пользовательские исключения





От какого класса следует наследовать пользовательские исключения?

A) `Exception`

B) `object`

C) `BaseException`

D) `Error`

---

## Question 13: KeyError





Когда возникает KeyError?

A) При нажатии клавиши

B) При ошибке шифрования

C) При обращении к несуществующему ключу словаря

D) При обращении к несуществующему индексу списка

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

A) IndexError

B) KeyError

C) 3

D) None

---

## Question 15: TypeError





Когда возникает TypeError?

A) При делении на ноль

B) При обращении к несуществующему атрибуту

C) При ошибке синтаксиса

D) При операции с несовместимыми типами

---

## Question 16: AttributeError





Что вызовет следующий код?

```python
x = 5
x.append(10)
```

A) AttributeError

B) TypeError

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

A) `assert.disable()`

B) Нельзя отключить

C) `python --no-assert script.py`

D) `python -O script.py`

---

## Question 19: EAFP





Что означает принцип EAFP?

A) Easier to Ask Forgiveness than Permission

B) Error Always Follows Protocol

C) Exception And Finally Processing

D) Error Analysis For Python

---

## Question 20: EAFP vs LBYL





Какой код соответствует принципу EAFP?

A) `if dict.has_key(key): ...`

B) `if key in dict: value = dict[key]`

C) `try: value = dict[key] except KeyError: ...`

D) `value = dict.get(key, default)`

---

## Question 21: Context Manager





Что гарантирует конструкция `with open(...) as f:`?

A) Блокировку файла

B) Быстрое чтение файла

C) Закрытие файла даже при исключении

D) Кэширование файла

---

## Question 22: __enter__ и __exit__





Какие методы нужны для создания контекстного менеджера?

A) `__open__` и `__close__`

B) `__enter__` and `__exit__`

C) `__init__` и `__del__`

D) `__start__` и `__stop__`

---

## Question 23: suppress





Что делает `contextlib.suppress`?

A) Игнорирует указанные исключения

B) Подавляет вывод в консоль

C) Записывает исключения в лог

D) Останавливает выполнение

---

## Question 24: Логирование исключений





Как правильно логировать исключение с traceback?

A) `logger.error(e.traceback)`

B) `logger.error(str(e))`

C) `logger.exception("Error")`

D) `print(traceback)`

---

## Question 25: Иерархия исключений





Какое исключение является подклассом ArithmeticError?

A) ZeroDivisionError

B) KeyError

C) ValueError

D) TypeError

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `BaseException` — корень иерархии. `Exception` — для "обычных" исключений. |
| 2 | D | Неперехваченное исключение завершает программу с выводом traceback. |
| 3 | A | Деление на ноль вызывает ZeroDivisionError, который и перехватывается. |
| 4 | C | Более специфичные (дочерние) исключения должны быть раньше родительских. |
| 5 | C | Кортеж исключений в скобках: `except (ValueError, TypeError):`. |
| 6 | C | Синтаксис Python 3: `except Error as e:`. |
| 7 | B | `else` выполняется, если в try-блоке НЕ возникло исключение. |
| 8 | A | `finally` выполняется всегда — для очистки ресурсов. |
| 9 | B | Пустой `raise` повторно вызывает текущее исключение. |
| 10 | C | `raise ValueError("message")` — стандартный синтаксис Python 3. |
| 11 | C | `raise NewError from original` сохраняет цепочку (exception chaining). |
| 12 | A | Пользовательские исключения должны наследовать от `Exception`. |
| 13 | C | KeyError — доступ к несуществующему ключу словаря. |
| 14 | A | Выход за границы списка — IndexError, не KeyError. |
| 15 | D | TypeError — операция с несовместимыми типами (напр., "2" + 2). |
| 16 | A | int не имеет метода append — AttributeError. |
| 17 | A | `assert condition, "message"` — проверка инвариантов. |
| 18 | D | Флаг `-O` (optimize) отключает assert и `__debug__`. |
| 19 | A | EAFP — "Проще попросить прощения, чем разрешения" — пробуй, ловий исключения. |
| 20 | C | EAFP: сначала пробуем, потом обрабатываем исключение. |
| 21 | C | `with` гарантирует вызов `__exit__` (закрытие) даже при исключении. |
| 22 | B | Контекстный менеджер требует `__enter__` и `__exit__`. |
| 23 | A | `suppress(ValueError)` тихо игнорирует ValueError в блоке with. |
| 24 | C | `logger.exception()` автоматически добавляет traceback. |
| 25 | A | ZeroDivisionError, OverflowError, FloatingPointError — подклассы ArithmeticError. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Превосходное понимание обработки исключений! |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат. Повторите контекстные менеджеры. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Обратите внимание на иерархию исключений и EAFP. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию с практическими примерами. |

---

