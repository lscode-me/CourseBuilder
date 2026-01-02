# Протоколы языков программирования
## ABI, Calling conventions, Bytecode formats, Runtime contracts

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы компиляции и интерпретации
- Иметь представление о низкоуровневом программировании
- Понимать концепцию протокола (модуль 01)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать роль ABI в совместимости бинарных модулей
- Объяснять calling conventions и их влияние на производительность
- Понимать bytecode formats как протоколы виртуальных машин
- Анализировать runtime contracts языков программирования

---

## 1. Введение: протоколы на уровне языка

Языки программирования определяют множество **протоколов** — договорённостей о том, как компоненты взаимодействуют на низком уровне:

- **ABI (Application Binary Interface)** — как бинарные модули взаимодействуют

- **Calling conventions** — как функции вызывают друг друга

- **Bytecode formats** — как код представляется в виртуальных машинах

- **Runtime contracts** — гарантии runtime системы

Эти протоколы невидимы для обычного программиста, но критичны для совместимости и производительности.

---

## 2. ABI (Application Binary Interface)

### 2.1 Что такое ABI

**ABI** — протокол взаимодействия между бинарными модулями на уровне машинного кода.

**ABI определяет:**

- Размеры и выравнивание типов данных
- Порядок байтов (endianness)
- Calling conventions (как передаются параметры)
- Name mangling (как именуются символы)
- Exception handling
- Системные вызовы

**Зачем:** ABI позволяет бинарным модулям, скомпилированным разными компиляторами или в разное время, работать вместе.

### 2.2 Примеры ABI

**Linux x86-64 System V ABI:**

- Первые 6 целочисленных аргументов в регистрах: RDI, RSI, RDX, RCX, R8, R9
- Остальные аргументы на стеке
- Возврат в регистре RAX
- Стек выровнен по 16 байтам

**Windows x64 calling convention:**

- Первые 4 аргумента в регистрах: RCX, RDX, R8, R9
- Остальные на стеке
- Caller выделяет shadow space (32 байта)

### 2.3 ABI и совместимость

**Проблема:** Изменение ABI ломает бинарную совместимость.

**Пример:**
```
Библиотека v1.0: функция foo(int a)
Приложение скомпилировано с v1.0

Библиотека v1.1: функция foo(int a, int b)  
// Приложение сломается при использовании v1.1!
```

**Решение:** 

- Версионирование библиотек (libfoo.so.1, libfoo.so.2)
- Добавление функций, не изменение существующих
- Symbol versioning

### 2.4 ABI stability

**Стабильный ABI:** изменения не ломают совместимость

**Python Limited API (Stable ABI):**
```c
// Вместо прямого доступа к структурам
// PyObject *obj; obj->ob_refcnt++;

// Используются функции API
Py_INCREF(obj);
```

Это позволяет расширениям работать с разными версиями Python без перекомпиляции.

---

## 3. Calling Conventions

### 3.1 Концепция

**Calling convention** — протокол вызова функций: как передаются параметры, кто очищает стек, где возвращается результат.

**Компоненты:**

- Передача параметров (регистры или стек)
- Порядок параметров
- Кто очищает стек (caller или callee)
- Возврат значения
- Сохранение регистров

### 3.2 Основные calling conventions

**cdecl (C declaration):**

- Параметры на стеке справа налево
- Caller очищает стек
- Поддерживает variadic functions
- Стандарт для C

**stdcall:**

- Параметры на стеке справа налево
- Callee очищает стек
- Не поддерживает variadic functions
- Windows API

**fastcall:**

- Первые 2 параметра в регистрах (ECX, EDX)
- Остальные на стеке
- Быстрее, но ограничена поддержка

### 3.3 Пример

```c
// cdecl
int add(int a, int b) {
    return a + b;
}

// Assembly (упрощённо)
add:
    push ebp
    mov ebp, esp
    mov eax, [ebp+8]   # параметр a
    add eax, [ebp+12]  # параметр b
    pop ebp
    ret                # caller очистит стек

// Вызов
push 5      # b
push 3      # a
call add
add esp, 8  # caller очищает стек (2 параметра * 4 байта)
```

### 3.4 Влияние на производительность

**Регистры vs стек:**

- Регистры быстрее (нет обращения к памяти)
- Стек медленнее, но неограничен

**Современные ABI:** используют регистры для первых параметров, стек для остальных.

---

## 4. Bytecode Formats

### 4.1 Концепция

**Bytecode** — промежуточное представление кода между исходным кодом и машинным кодом.

**Зачем:**

- Портабельность (один bytecode для всех платформ)
- Быстрее интерпретации исходного кода
- Оптимизация на уровне bytecode

### 4.2 Python bytecode

```python
def add(a, b):
    return a + b

# Disassembly

import dis
dis.dis(add)
```

**Output:**
```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

**Инструкции:**

- `LOAD_FAST 0`: загрузить локальную переменную 0 (a) на стек
- `LOAD_FAST 1`: загрузить локальную переменную 1 (b) на стек
- `BINARY_ADD`: сложить два значения на стеке
- `RETURN_VALUE`: вернуть значение со стека

### 4.3 JVM bytecode

```java
public int add(int a, int b) {
    return a + b;
}

// Bytecode
0: iload_1        // load a
1: iload_2        // load b
2: iadd           // add
3: ireturn        // return
```

### 4.4 Bytecode как протокол

**Bytecode — это протокол между:**

- Компилятором (генерирует bytecode)
- Виртуальной машиной (выполняет bytecode)

**Стабильность bytecode:**

- Изменение формата ломает совместимость
- Нужно версионирование (.pyc файлы в Python содержат версию)

---

## 5. Runtime Contracts

### 5.1 Концепция

**Runtime contract** — гарантии, которые даёт runtime система.

**Примеры:**

- Автоматическое управление памятью (GC)
- Проверка границ массивов
- Type safety
- Thread safety
- Exception handling

### 5.2 Memory management contracts

**C:** Программист управляет памятью вручную

```c
int *p = malloc(sizeof(int) * 10);
// Использование p
free(p);  // Программист должен освободить
```

**Python:** Автоматическое управление памятью

```python
items = [1, 2, 3, 4, 5]
# GC автоматически освободит память
```

**Контракт:** Python гарантирует, что память будет освобождена, когда объект больше не используется.

### 5.3 Safety contracts

**Bounds checking:**
```python
items = [1, 2, 3]
# Python проверяет границы

print(items[10])  # IndexError
```

**Type safety:**
```python
def add(a: int, b: int) -> int:
    return a + b

# Runtime может проверить типы (в Python опционально)

add(1, "2")  # TypeError (если используется typing с проверкой)
```

### 5.4 Concurrency contracts

**JavaScript:** Single-threaded, event loop
- Гарантия: код не прерывается (run-to-completion)
- Нет data races

**Java:** Multi-threaded, synchronized
- Гарантии при правильном использовании synchronized
- Видимость изменений (happens-before)

---

## 6. Name Mangling

### 6.1 Концепция

**Name mangling** — преобразование имён функций/методов в символы для линкера.

**Зачем:** Поддержка перегрузки функций, namespaces, templates.

### 6.2 C++ name mangling

```cpp
namespace Math {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}

// Mangled names (пример):
// _ZN4Math3addEii    - Math::add(int, int)
// _ZN4Math3addEdd    - Math::add(double, double)
```

### 6.3 extern "C"

```cpp
extern "C" {
    int add(int a, int b) { return a + b; }
}
// Mangled name: add (без mangling)
```

Это позволяет C коду вызывать C++ функции.

---

## 7. FFI (Foreign Function Interface)

### 7.1 Концепция

**FFI** — протокол вызова функций из других языков.

**Проблемы:**

- Разные calling conventions
- Разные представления типов
- Разные runtime contracts

### 7.2 Python ctypes

```python
from ctypes import CDLL, c_int

# Загрузить C библиотеку

libc = CDLL("libc.so.6")

# Вызвать C функцию

result = libc.printf(b"Hello from Python: %d\n", c_int(42))
```

**Output:**
```
Hello from Python: 42
```

### 7.3 Type marshalling

**Проблема:** Типы разных языков несовместимы.

**Решение:** Маршалинг — преобразование типов.

```python
# Python string → C char*
# Python int → C int
# Python list → C array
```

---

## 💡 Key Takeaways

- **ABI определяет бинарную совместимость**: Изменение ABI ломает совместимость между бинарными модулями. Стабильный ABI критичен для библиотек.

- **Calling conventions — протокол вызова функций**: Определяют передачу параметров и возврат результата. Влияют на производительность и совместимость.

- **Bytecode — промежуточный протокол**: Связывает компиляторы и виртуальные машины, обеспечивая портабельность. Изменение формата требует версионирования.

- **Runtime contracts определяют гарантии**: Автоматическое управление памятью, проверка границ, type safety — гарантии runtime системы, упрощающие разработку.

- **Name mangling и FFI для взаимодействия**: Name mangling поддерживает перегрузку, FFI позволяет вызывать код из других языков.

---

## 🚀 Next Steps

**Related Modules:**

- [12_Language_Server_Protocol](../12_Language_Server_Protocol/) — LSP: протокол взаимодействия IDE и языковых серверов
- [13_UTF8_As_Protocol](../13_UTF8_As_Protocol/) — UTF-8 как протокол интерпретации данных

**Practice Ideas:**

1. Изучите bytecode вашей любимой программы (Python dis, Java javap)
2. Вызовите C функцию из Python через ctypes
3. Сравните ABI разных платформ (Linux vs Windows)

**Going Deeper:**

- Изучите LLVM IR как универсальный bytecode
- Изучите WebAssembly как бинарный формат для веба
- Изучите Rust FFI для безопасного взаимодействия с C

---



