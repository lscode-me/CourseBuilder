# Другие скрытые протоколы
## Конец строки, Endianness, протоколы ошибок, Null/None/NaN, время и timezone

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать UTF-8 как протокол (модуль 13)
- Понимать концепцию протокола (модуль 01)
- Иметь опыт работы с разными платформами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать протоколы конца строки и их платформенные различия
- Объяснять endianness и его влияние на совместимость
- Различать протоколы представления отсутствия (Null, None, NaN)
- Понимать протоколы времени и timezone

---

## 1. Введение: скрытые протоколы

Многие протоколы настолько привычны, что мы их не замечаем. Они определяют базовые аспекты представления данных:

- Как обозначается конец строки?
- В каком порядке хранятся байты числа?
- Как представить отсутствие значения?
- Как представить время?

Эти **скрытые протоколы** критичны для совместимости между системами.

---

## 2. Конец строки (Line Endings)

### 2.1 Три стандарта

**LF (Line Feed, `\n`, 0x0A):**

- Unix, Linux, macOS
- Один байт

**CRLF (Carriage Return + Line Feed, `\r\n`, 0x0D 0x0A):**

- Windows, DOS
- Два байта

**CR (Carriage Return, `\r`, 0x0D):**

- Старые Mac OS (до OS X)
- Один байт

### 2.2 Исторические причины

**Телетайп (1960-е):**

- CR: вернуть каретку в начало
- LF: подать бумагу на одну строку
- Нужны оба для перехода на новую строку

**Unix (1970-е):**

- Упростили: только LF
- CR не нужен (нет физической каретки)

**Windows:**

- Сохранили оба для совместимости с DOS

### 2.3 Проблемы несовместимости

```python
# Unix файл

text = "Line 1\nLine 2\n"

# Windows файл

text = "Line 1\r\nLine 2\r\n"

# При открытии на другой платформе могут быть проблемы
```

**Git handling:**
```bash
# Автоматическое преобразование

git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # Unix
```

### 2.4 Универсальное чтение

```python
# Python обрабатывает все варианты

with open('file.txt', 'r', newline=None) as f:
    # Автоматически распознает LF, CRLF, CR
    lines = f.readlines()
```

---

## 3. Endianness

### 3.1 Концепция

**Endianness** — порядок байтов в многобайтовых числах.

**Число:** `0x12345678` (4 байта)

**Big-endian (старший байт первым):**
```
Адрес: 0x00  0x01  0x02  0x03
Байт:  0x12  0x34  0x56  0x78
```

**Little-endian (младший байт первым):**
```
Адрес: 0x00  0x01  0x02  0x03
Байт:  0x78  0x56  0x34  0x12
```

### 3.2 Платформы

**Big-endian:**

- Сетевые протоколы (network byte order)
- Некоторые RISC процессоры (SPARC, старые PowerPC)
- Более интуитивен для людей

**Little-endian:**

- x86, x86-64 (Intel, AMD)
- ARM (обычно little-endian)
- Более эффективен для некоторых операций

### 3.3 Пример

```python
import struct

number = 0x12345678

# Big-endian

big_endian_bytes = struct.pack('>I', number)
print(big_endian_bytes.hex())  # 12345678

# Little-endian

little_endian_bytes = struct.pack('<I', number)
print(little_endian_bytes.hex())  # 78563412
```

**Output:**
```
12345678
78563412
```

### 3.4 Network Byte Order

**Сетевые протоколы:** всегда big-endian

```python
import socket

# Host to network (может изменить порядок байтов)

network_order = socket.htonl(0x12345678)

# Network to host (обратно)

host_order = socket.ntohl(network_order)
```

Это обеспечивает совместимость между системами с разным endianness.

---

## 4. Протоколы отсутствия

### 4.1 Null / None / nil

**Различные представления отсутствия:**

**C:** `NULL` (обычно 0)

```c
int *ptr = NULL;
```

**Python:** `None`

```python
value = None
```

**JavaScript:** `null` и `undefined`

```javascript
let value1 = null;      // явное отсутствие
let value2 = undefined; // неинициализировано
```

**SQL:** `NULL`

```sql
SELECT * FROM users WHERE email IS NULL;
```

### 4.2 Проблемы Null

**Nullable types:**
```python
def get_user(id: int) -> User | None:
    # Может вернуть User или None
    pass

user = get_user(123)
if user is not None:
    print(user.name)  # Безопасно
```

**Billion dollar mistake (Tony Hoare):**
Null references приводят к NullPointerException/NullReferenceError.

### 4.3 NaN (Not a Number)

**IEEE 754 floating point:**
```python
import math

nan = float('nan')
print(nan)           # nan
print(math.isnan(nan))  # True

# NaN не равен ничему, даже себе!

print(nan == nan)    # False
print(nan != nan)    # True
```

**Output:**
```
nan
True
False
True
```

**Причины NaN:**

- `0.0 / 0.0`
- `math.sqrt(-1)`
- `float('inf') - float('inf')`

### 4.4 Optional types

**Rust Option:**
```rust
fn find_user(id: u32) -> Option<User> {
    // Some(user) или None
}

match find_user(123) {
    Some(user) => println!("Found: {}", user.name),
    None => println!("Not found"),
}
```

Это делает отсутствие явным и безопасным.

---

## 5. Протоколы времени

### 5.1 Представление времени

**Unix timestamp:**
```python
import time

# Секунды с 1970-01-01 00:00:00 UTC

timestamp = time.time()
print(timestamp)  # 1705324800.123456
```

**ISO 8601:**
```
2024-01-15T10:00:00Z        # UTC
2024-01-15T10:00:00+03:00   # с timezone
2024-01-15T10:00:00.123Z    # с миллисекундами
```

### 5.2 Timezone проблемы

**Naïve datetime (без timezone):**
```python
from datetime import datetime

dt = datetime(2024, 1, 15, 10, 0, 0)
# 10:00:00 где? Москва? UTC? Непонятно!
```

**Aware datetime (с timezone):**
```python
from datetime import datetime, timezone

dt = datetime(2024, 1, 15, 10, 0, 0, tzinfo=timezone.utc)
# 10:00:00 UTC — понятно!
```

### 5.3 DST (Daylight Saving Time)

**Проблема:** переход на летнее время нарушает линейность времени.

**Пример:**
```
2024-03-10 02:00:00 → 2024-03-10 03:00:00 (skip 1 hour)
2024-11-03 02:00:00 occurs twice (fall back)
```

**Решение:** всегда использовать UTC для хранения, timezone только для отображения.

### 5.4 Leap seconds

**Проблема:** високосные секунды добавляются нерегулярно для синхронизации с вращением Земли.

**Пример:**
```
2016-12-31 23:59:59
2016-12-31 23:59:60  ← leap second
2017-01-01 00:00:00
```

Многие системы игнорируют leap seconds, что приводит к проблемам синхронизации.

---

## 6. Протоколы ошибок

### 6.1 Error codes vs Exceptions

**C:** Error codes

```c
int result = open_file("file.txt");
if (result < 0) {
    // Ошибка
    fprintf(stderr, "Error: %s\n", strerror(errno));
}
```

**Python:** Exceptions

```python
try:
    with open("file.txt") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
```

### 6.2 HTTP статус-коды

**Протокол представления ошибок в HTTP:**

- 2xx: Success
- 4xx: Client error
- 5xx: Server error

```
200 OK
404 Not Found
500 Internal Server Error
```

### 6.3 Exit codes

**Unix processes:**
```bash
# 0 = success
# Non-zero = error

exit 0  # success
exit 1  # error
```

```python
import sys

if error:
    sys.exit(1)  # Error exit code
else:
    sys.exit(0)  # Success
```

---

## 7. Совместимость через протоколы

### 7.1 Выбор правильного протокола

**Для файлов:**

- UTF-8 для текста
- LF для Unix, CRLF для Windows (или конвертировать)
- Binary для non-text

**Для сети:**

- UTF-8 для текста
- Big-endian (network byte order) для чисел
- ISO 8601 для времени

**Для API:**

- JSON/XML для структурированных данных
- ISO 8601 для времени
- Nullable types для отсутствия

### 7.2 Явные спецификации

**Content-Type в HTTP:**
```
Content-Type: text/plain; charset=UTF-8
```

**XML declaration:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
```

Это делает протокол явным.

---

## 💡 Key Takeaways

- **Конец строки — платформенный протокол**: LF (Unix), CRLF (Windows), CR (старые Mac). Git и современные инструменты автоматически конвертируют, но знание различий критично.

- **Endianness влияет на совместимость**: Big-endian (сети), little-endian (x86). Сетевые протоколы используют big-endian (network byte order) для совместимости.

- **Протоколы отсутствия разнообразны**: Null/None/nil, NaN, Optional types. Явные типы (Option в Rust) безопаснее неявных (null в C/Java).

- **Время и timezone — сложные протоколы**: Unix timestamp, ISO 8601, DST, leap seconds. Всегда храните время в UTC, timezone только для отображения.

- **Явные спецификации лучше неявных**: Указывайте кодировку, endianness, формат времени явно (Content-Type, XML declaration) для избежания неопределённости.

---

## 🚀 Next Steps

**Related Modules:**

- [15_Component_Service_Protocols](../15_Component_Service_Protocols/) — протоколы между компонентами: message queues, pub/sub
- [18_Good_Vs_Bad_Protocols](../18_Good_Vs_Bad_Protocols/) — хороший vs плохой протокол

**Practice Ideas:**

1. Создайте файлы с разными line endings и проверьте их на разных платформах
2. Напишите программу для конвертации endianness чисел
3. Реализуйте работу с timezone-aware datetime

**Going Deeper:**

- Изучите Unicode normalization для обработки комбинирующих символов
- Изучите TAI (International Atomic Time) как альтернативу UTC без leap seconds
- Изучите Protocol Buffers для бинарной сериализации с явным endianness

---



