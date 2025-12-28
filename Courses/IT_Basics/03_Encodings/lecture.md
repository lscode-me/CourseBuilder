# Кодировки символов
## ASCII, Unicode, UTF-8 и вечная головная боль инженеров

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать, что такое биты и байты (модуль 02_NumberSystems)
- Знать основы hex-системы
- Понимать, что компьютер работает только с числами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить историю и эволюцию кодировок символов
- Различать ASCII, Unicode, UTF-8, UTF-16 и другие кодировки
- Использовать модуль `unicodedata` для работы с метаданными Unicode
- Диагностировать и исправлять проблемы с кодировками ("кракозябры")
- Правильно работать с кодировками в командной строке и коде
- Выбирать правильную кодировку для разных сценариев

---

## 1. Зачем нужны кодировки

### 1.1 Проблема

Компьютер понимает только числа. Как сохранить текст?

```

Человек видит:  Hello, мир!
Компьютер хранит:  48 65 6C 6C 6F 2C 20 D0 BC D0 B8 D1 80 21

```

**Кодировка** — это таблица соответствия между символами и числами.

### 1.2 Почему это источник проблем

До появления Unicode каждая страна создавала свои кодировки:

```

Символ "Я" закодирован как:

- КОИ-8:        0xD1 (209)
- Windows-1251: 0xDF (223)
- ISO-8859-5:   0xEF (239)
- MacCyrillic:  0x9F (159)

```

Один и тот же байт — разные символы в разных кодировках!

### 1.3 "Кракозябры" — классическая проблема

```

Ожидалось:   Привет, мир!
Получилось:  ÐŸÑ€Ð¸Ð²ÐµÑ‚, Ð¼Ð¸Ñ€!

```

Или:

```

Ожидалось:   Привет, мир!
Получилось:  Пpивeт, миp!  (выглядит почти нормально, но часть букв — латиница!)

```

Или:

```

Ожидалось:   Привет, мир!
Получилось:  ?????, ???!

```

---

## 2. ASCII — начало всего

### 2.1 История

**ASCII** (American Standard Code for Information Interchange) создан в 1963 году.

7 бит → 128 символов (0-127):

- 0-31: управляющие символы (невидимые)
- 32-126: печатаемые символы
- 127: DEL (удаление)

### 2.2 Таблица ASCII

```

Dec  Hex  Char     Dec  Hex  Char     Dec  Hex  Char
───────────────    ───────────────    ───────────────
32   20   SPACE    48   30   0        65   41   A
33   21   !        49   31   1        66   42   B
34   22   "        50   32   2        ...
35   23   #        ...               90   5A   Z
36   24   $        57   39   9        
37   25   %                           97   61   a
38   26   &        58   3A   :        98   62   b
39   27   '        59   3B   ;        ...
...                ...               122  7A   z
47   2F   /        64   40   @

```

**Ключевые значения:**

| Символ | Dec | Hex | Описание |
|--------|-----|-----|----------|
| NUL | 0 | 0x00 | Null, конец строки в C |
| TAB | 9 | 0x09 | Горизонтальная табуляция |
| LF | 10 | 0x0A | Line Feed, перенос строки (Unix) |
| CR | 13 | 0x0D | Carriage Return (часть Windows newline) |
| SPACE | 32 | 0x20 | Пробел |
| 0-9 | 48-57 | 0x30-0x39 | Цифры |
| A-Z | 65-90 | 0x41-0x5A | Заглавные буквы |
| a-z | 97-122 | 0x61-0x7A | Строчные буквы |
| DEL | 127 | 0x7F | Delete |

### 2.3 Практика ASCII

```bash
# Смотрим ASCII код символа
printf "%d\n" "'A"
# 65

# Символ по ASCII коду
printf "\x41\n"
# A

# Таблица ASCII
man ascii

```

```python
# Python: символ ↔ код
print(ord('A'))     # 65
print(chr(65))      # A

# Проверка ASCII
text = "Hello"
print(text.isascii())  # True
print("Привет".isascii())  # False

```

**Output:**
```

65
A
True
False

```

### 2.4 Ограничения ASCII

ASCII поддерживает только:

- Латинские буквы (A-Z, a-z)
- Цифры (0-9)
- Базовые знаки препинания

**Не поддерживает:**

- Кириллицу (русский)
- Диакритические знаки (é, ñ, ü)
- Иероглифы (китайский, японский)
- Эмодзи 😀
- Математические символы (√, ∑, ∞)

---

## 3. Расширенный ASCII и "code pages"

### 3.1 Идея

ASCII использует 7 бит (0-127). В байте 8 бит!

Разные страны использовали оставшиеся 128 значений (128-255) по-своему.

### 3.2 Кодовые страницы (Code Pages)

**Западноевропейские:**

- ISO-8859-1 (Latin-1) — западноевропейские языки
- Windows-1252 — расширение Latin-1 для Windows

**Кириллические:**

- КОИ-8 (KOI8-R) — советский стандарт
- Windows-1251 (CP1251) — Windows для русского
- ISO-8859-5 — ISO стандарт для кириллицы
- CP866 (DOS) — DOS для русского

### 3.3 КОИ-8 (KOI8-R)

Советская кодировка. Особенность: если обнулить старший бит, кириллица превращается в похожую латиницу:

```

КОИ-8: П = 0xD0
       0xD0 = 11010000
       AND  = 01111111
              01010000 = 0x50 = 'P'

Поэтому: ПРИВЕТ → PRIVET при потере 8-го бита

```

### 3.4 Windows-1251

Самая распространённая кодировка для русского в Windows:

```

Символ  Код (hex)  Код (dec)
──────────────────────────────
А       0xC0       192
Б       0xC1       193
В       0xC2       194
...
Я       0xDF       223

а       0xE0       224
б       0xE1       225
...
я       0xFF       255

```

### 3.5 Проблема совместимости

```

Файл в KOI8-R открыт как Windows-1251:

Байт 0xD0 (KOI8-R: "П") → Windows-1251: "Р"
Байт 0xD2 (KOI8-R: "Р") → Windows-1251: "Т"

"ПРИВЕТ" → "ПТЙЧЕ|"

```

---

## 4. Unicode — единая таблица символов

### 4.1 Идея Unicode

**Unicode** — единый стандарт, присваивающий уникальный номер каждому символу всех языков мира.

На 2024 год: **149,813** символов в Unicode 15.1

```

U+0041 = A (латинская заглавная A)
U+0410 = А (кириллическая заглавная А)
U+4E2D = 中 (китайский иероглиф "середина")
U+1F600 = 😀 (эмодзи)

```

### 4.2 Кодовые точки (Code Points)

**Code point** — уникальный номер символа в Unicode.

Записывается как: `U+XXXX` или `U+XXXXX`

```

U+0000 — U+FFFF:   Basic Multilingual Plane (BMP)
U+10000 — U+10FFFF: Дополнительные плоскости (эмодзи, редкие символы)

```

### 4.3 Плоскости Unicode

| Плоскость | Диапазон | Содержание |
|-----------|----------|------------|
| BMP (0) | U+0000-U+FFFF | Основные языки, пунктуация |
| SMP (1) | U+10000-U+1FFFF | Исторические, музыкальные, эмодзи |
| SIP (2) | U+20000-U+2FFFF | Редкие CJK иероглифы |
| ... | ... | ... |

### 4.4 Категории символов в Unicode

Каждый символ Unicode имеет свою категорию:

| Категория | Код | Примеры |
|-----------|-----|---------|
| Letter, Uppercase | Lu | A, Б, Ω |
| Letter, Lowercase | Ll | a, б, ω |
| Letter, Other | Lo | 中, あ, ก |
| Number, Decimal Digit | Nd | 0-9, ٠-٩ |
| Punctuation | P* | . , ! ? |
| Symbol, Math | Sm | + − × ÷ ∑ |
| Symbol, Currency | Sc | $ € ¥ ₽ |
| Symbol, Other | So | ☀ ★ ♠ |
| Mark, Combining | M* | ́ ̈ ̃ (диакритика) |

### 4.5 Блоки Unicode

Символы в Unicode сгруппированы в блоки по языкам и назначению:

```

U+0000-U+007F    Basic Latin (ASCII)
U+0080-U+00FF    Latin-1 Supplement
U+0100-U+017F    Latin Extended-A
U+0400-U+04FF    Cyrillic (Кириллица)
U+0500-U+052F    Cyrillic Supplement
U+4E00-U+9FFF    CJK Unified Ideographs (Китайский/Японский/Корейский)
U+1F600-U+1F64F  Emoticons
U+1F300-U+1F5FF  Miscellaneous Symbols and Pictographs

```

### 4.6 Unicode — это не кодировка!

**Важно:** Unicode определяет КАКИЕ символы существуют и их номера.

**Кодировка** определяет КАК хранить эти номера в байтах:

- UTF-8
- UTF-16
- UTF-32

```

Символ "A" (U+0041):

- UTF-8:  0x41 (1 байт)
- UTF-16: 0x00 0x41 (2 байта)
- UTF-32: 0x00 0x00 0x00 0x41 (4 байта)

Символ "😀" (U+1F600):

- UTF-8:  0xF0 0x9F 0x98 0x80 (4 байта)
- UTF-16: 0xD8 0x3D 0xDE 0x00 (4 байта, surrogate pair)
- UTF-32: 0x00 0x01 0xF6 0x00 (4 байта)

```

### 4.7 Unicode — это набор спецификаций

**Unicode — это не просто таблица символов.** Это целый набор стандартов и спецификаций, который включает:

| Спецификация | Описание |
|--------------|----------|
| **UCD** (Unicode Character Database) | База данных всех символов с их свойствами |
| **UAX** (Unicode Standard Annexes) | Дополнения к стандарту (нормализация, сегментация, BiDi) |
| **UTS** (Unicode Technical Standards) | Технические стандарты (Emoji, регулярные выражения) |
| **UTR** (Unicode Technical Reports) | Технические отчёты |
| **CLDR** (Common Locale Data Repository) | Локализация: форматы дат, чисел, валют |
| **ICU** (International Components for Unicode) | Библиотека для работы с Unicode |

Каждый символ в Unicode имеет множество **свойств** (properties), не только код и название:

| Свойство | Описание | Пример |
|----------|----------|--------|
| **Code Point** | Уникальный номер символа | U+0041 |
| **Name** | Официальное название | LATIN CAPITAL LETTER A |
| **General Category** | Основная категория | Lu (Letter, uppercase) |
| **Script** | Письменность | Latin |
| **Block** | Блок Unicode | Basic Latin |
| **Bidirectional Class** | Направление текста | L (Left-to-Right) |
| **Numeric Value** | Числовое значение (для цифр) | 5.0 |
| **Decomposition** | Разложение на компоненты | é → e + ́ |
| **Case Mapping** | Преобразование регистра | A ↔ a |
| **Age** | Версия Unicode, когда добавлен | 1.1 |

#### Примеры символов с их Unicode-свойствами

**Цифры:**

| Символ | Code Point | Категория | Имя | Числовое значение |
|--------|------------|-----------|-----|-------------------|
| 0 | U+0030 | Nd | DIGIT ZERO | 0 |
| 5 | U+0035 | Nd | DIGIT FIVE | 5 |
| ٥ | U+0665 | Nd | ARABIC-INDIC DIGIT FIVE | 5 |
| ५ | U+096B | Nd | DEVANAGARI DIGIT FIVE | 5 |
| Ⅳ | U+2163 | Nl | ROMAN NUMERAL FOUR | 4 |
| ½ | U+00BD | No | VULGAR FRACTION ONE HALF | 0.5 |

**Латинские буквы:**

| Символ | Code Point | Категория | Имя | Регистр |
|--------|------------|-----------|-----|---------|
| A | U+0041 | Lu | LATIN CAPITAL LETTER A | a (U+0061) |
| z | U+007A | Ll | LATIN SMALL LETTER Z | Z (U+005A) |
| é | U+00E9 | Ll | LATIN SMALL LETTER E WITH ACUTE | É (U+00C9) |
| ß | U+00DF | Ll | LATIN SMALL LETTER SHARP S | SS (особый случай) |

**Кириллица:**

| Символ | Code Point | Категория | Имя | Регистр |
|--------|------------|-----------|-----|---------|
| А | U+0410 | Lu | CYRILLIC CAPITAL LETTER A | а (U+0430) |
| я | U+044F | Ll | CYRILLIC SMALL LETTER YA | Я (U+042F) |
| Ж | U+0416 | Lu | CYRILLIC CAPITAL LETTER ZHE | ж (U+0436) |
| ё | U+0451 | Ll | CYRILLIC SMALL LETTER IO | Ё (U+0401) |

**Арабские символы:**

| Символ | Code Point | Категория | Имя | BiDi |
|--------|------------|-----------|-----|------|
| ا | U+0627 | Lo | ARABIC LETTER ALEF | AL (Arabic Letter) |
| ب | U+0628 | Lo | ARABIC LETTER BEH | AL |
| م | U+0645 | Lo | ARABIC LETTER MEEM | AL |
| ٠ | U+0660 | Nd | ARABIC-INDIC DIGIT ZERO | AN (Arabic Number) |

**Китайские/Японские:**

| Символ | Code Point | Категория | Имя | Script |
|--------|------------|-----------|-----|--------|
| 中 | U+4E2D | Lo | CJK UNIFIED IDEOGRAPH-4E2D | Han |
| 日 | U+65E5 | Lo | CJK UNIFIED IDEOGRAPH-65E5 | Han |
| あ | U+3042 | Lo | HIRAGANA LETTER A | Hiragana |
| ア | U+30A2 | Lo | KATAKANA LETTER A | Katakana |

**Математические символы:**

| Символ | Code Point | Категория | Имя |
|--------|------------|-----------|-----|
| + | U+002B | Sm | PLUS SIGN |
| ∞ | U+221E | Sm | INFINITY |
| √ | U+221A | Sm | SQUARE ROOT |
| ∑ | U+2211 | Sm | N-ARY SUMMATION |
| π | U+03C0 | Ll | GREEK SMALL LETTER PI |
| ≠ | U+2260 | Sm | NOT EQUAL TO |

**Валюты:**

| Символ | Code Point | Категория | Имя |
|--------|------------|-----------|-----|
| $ | U+0024 | Sc | DOLLAR SIGN |
| € | U+20AC | Sc | EURO SIGN |
| ₽ | U+20BD | Sc | RUBLE SIGN |
| ¥ | U+00A5 | Sc | YEN SIGN |
| ₿ | U+20BF | Sc | BITCOIN SIGN |

**Эмодзи:**

| Символ | Code Point | Категория | Имя |
|--------|------------|-----------|-----|
| 😀 | U+1F600 | So | GRINNING FACE |
| ❤️ | U+2764 | So | HEAVY BLACK HEART |
| 🚀 | U+1F680 | So | ROCKET |
| 🎉 | U+1F389 | So | PARTY POPPER |
| 👨‍💻 | U+1F468 U+200D U+1F4BB | — | MAN TECHNOLOGIST (ZWJ sequence) |

**Специальные и управляющие:**

| Символ | Code Point | Категория | Имя | Назначение |
|--------|------------|-----------|-----|------------|
| (space) | U+0020 | Zs | SPACE | Обычный пробел |
| (nbsp) | U+00A0 | Zs | NO-BREAK SPACE | Неразрывный пробел |
| ​ | U+200B | Cf | ZERO WIDTH SPACE | Невидимый разделитель |
| ‍ | U+200D | Cf | ZERO WIDTH JOINER | Соединитель (эмодзи) |
| ← | U+2190 | Sm | LEFTWARDS ARROW | Стрелка |
| • | U+2022 | Po | BULLET | Маркер списка |

```python
# Получение всех свойств символа в Python
import unicodedata

def show_char_properties(char):
    """Показывает основные Unicode-свойства символа."""
    print(f"Символ: {char}")
    print(f"  Code Point: U+{ord(char):04X}")
    print(f"  Name: {unicodedata.name(char, 'N/A')}")
    print(f"  Category: {unicodedata.category(char)}")
    print(f"  Bidirectional: {unicodedata.bidirectional(char)}")
    print(f"  East Asian Width: {unicodedata.east_asian_width(char)}")
    print(f"  Combining: {unicodedata.combining(char)}")
    print(f"  Mirrored: {unicodedata.mirrored(char)}")
    try:
        print(f"  Numeric Value: {unicodedata.numeric(char)}")
    except ValueError:
        print(f"  Numeric Value: N/A")

show_char_properties('5')
print()
show_char_properties('Ж')
print()
show_char_properties('😀')

```

**Output:**
```

Символ: 5
  Code Point: U+0035
  Name: DIGIT FIVE
  Category: Nd
  Bidirectional: EN
  East Asian Width: Na
  Combining: 0
  Mirrored: 0
  Numeric Value: 5.0

Символ: Ж
  Code Point: U+0416
  Name: CYRILLIC CAPITAL LETTER ZHE
  Category: Lu
  Bidirectional: L
  East Asian Width: A
  Combining: 0
  Mirrored: 0
  Numeric Value: N/A

Символ: 😀
  Code Point: U+1F600
  Name: GRINNING FACE
  Category: So
  Bidirectional: ON
  East Asian Width: W
  Combining: 0
  Mirrored: 0
  Numeric Value: N/A

```

> **📝 Note:**  
> Полная база данных Unicode доступна на [unicode.org](https://www.unicode.org/ucd/) и обновляется с каждой новой версией стандарта.

---

## 5. UTF-8 — современный стандарт

### 5.1 Почему UTF-8

**UTF-8** (8-bit Unicode Transformation Format) — самая популярная кодировка в мире.

**Преимущества:**

- Совместима с ASCII (первые 128 символов идентичны)
- Переменная длина (экономия места)
- Самосинхронизация (легко найти начало символа)
- Не зависит от endianness

### 5.2 Как работает UTF-8

| Диапазон code point | Байт 1 | Байт 2 | Байт 3 | Байт 4 |
|---------------------|--------|--------|--------|--------|
| U+0000-U+007F | 0xxxxxxx | - | - | - |
| U+0080-U+07FF | 110xxxxx | 10xxxxxx | - | - |
| U+0800-U+FFFF | 1110xxxx | 10xxxxxx | 10xxxxxx | - |
| U+10000-U+10FFFF | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |

**Правила:**

- ASCII (0-127): 1 байт, начинается с `0`
- 2 байта: первый начинается с `110`, второй с `10`
- 3 байта: первый с `1110`, остальные с `10`
- 4 байта: первый с `11110`, остальные с `10`

### 5.3 Примеры кодирования UTF-8

**Пример 1: "A" (U+0041)**

```

U+0041 = 65 = 1000001
Диапазон: U+0000-U+007F (1 байт)

Результат: 0 1000001 = 0x41
           ^
           ASCII совместимо!

```

**Пример 2: "й" (U+0439)**

```

U+0439 = 1081 = 10000111001
Диапазон: U+0080-U+07FF (2 байта)

Формат: 110xxxxx 10xxxxxx
Биты:      10000   111001

Результат: 11010000 10111001 = 0xD0 0xB9

```

**Пример 3: "€" (U+20AC)**

```

U+20AC = 8364 = 10000010101100
Диапазон: U+0800-U+FFFF (3 байта)

Формат: 1110xxxx 10xxxxxx 10xxxxxx
Биты:       0010   000010   101100

Результат: 11100010 10000010 10101100 = 0xE2 0x82 0xAC

```

**Пример 4: "😀" (U+1F600)**

```

U+1F600 = 128512 = 11111011000000000
Диапазон: U+10000-U+10FFFF (4 байта)

Формат: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Биты:       000   011111   011000   000000

Результат: 11110000 10011111 10011000 10000000 = 0xF0 0x9F 0x98 0x80

```

### 5.4 UTF-8 на практике

```python
# Кодирование строки в UTF-8
text = "Привет 😀"
utf8_bytes = text.encode('utf-8')
print(f"Bytes: {utf8_bytes}")
print(f"Hex: {utf8_bytes.hex()}")
print(f"Length: {len(utf8_bytes)} bytes, {len(text)} chars")

```

**Output:**
```

Bytes: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xf0\x9f\x98\x80'
Hex: d09fd180d0b8d0b2d0b5d18220f09f9880
Length: 18 bytes, 9 chars

```

```bash
# В bash
echo -n "Привет" | xxd

```

```

00000000: d09f d180 d0b8 d0b2 d0b5 d182            ............

```

---

## 6. UTF-16 и UTF-32

### 6.1 UTF-16

**UTF-16** — кодировка с минимумом 2 байта на символ.

```

BMP (U+0000-U+FFFF): 2 байта
За пределами BMP: 4 байта (surrogate pairs)

```

**Surrogate pairs для символов за пределами BMP:**

```

Символ U+1F600 (😀):

1. Вычитаем 0x10000: 0x1F600 - 0x10000 = 0xF600
2. Старшие 10 бит + 0xD800 = High surrogate: 0xD83D
3. Младшие 10 бит + 0xDC00 = Low surrogate: 0xDE00

UTF-16: 0xD83D 0xDE00

```

**Проблема UTF-16:**

- Не совместима с ASCII
- Зависит от endianness (UTF-16 BE vs UTF-16 LE)
- Всё равно переменная длина (2 или 4 байта)

### 6.2 BOM (Byte Order Mark)

**BOM** — специальный символ в начале файла, указывающий порядок байтов:

| Кодировка | BOM (hex) |
|-----------|-----------|
| UTF-8 | EF BB BF (опционально) |
| UTF-16 BE | FE FF |
| UTF-16 LE | FF FE |
| UTF-32 BE | 00 00 FE FF |
| UTF-32 LE | FF FE 00 00 |

```bash
# Файл с BOM
xxd -l 4 file_with_bom.txt
# 00000000: efbb bf48                                ...H
#           ^^^^^^ UTF-8 BOM

# В Python BOM вызывает проблемы
# Используйте 'utf-8-sig' для чтения файлов с BOM
```

### 6.3 UTF-32

**UTF-32** — фиксированные 4 байта на символ.

**Преимущества:**

- Простая индексация (символ N = байты N*4 до N*4+3)
- Нет surrogate pairs

**Недостатки:**

- Расточительный (4x размер для ASCII)
- Редко используется

### 6.4 Сравнение кодировок

| Кодировка | ASCII текст | Кириллица | Эмодзи |
|-----------|-------------|-----------|--------|
| UTF-8 | 1 байт | 2 байта | 4 байта |
| UTF-16 | 2 байта | 2 байта | 4 байта |
| UTF-32 | 4 байта | 4 байта | 4 байта |

**Вывод:** UTF-8 эффективнее для ASCII и смешанного текста.

---

## 7. Работа с кодировками в командной строке

### 7.1 Определение кодировки

```bash
# Команда file
file document.txt
# document.txt: UTF-8 Unicode text

file -i document.txt
# document.txt: text/plain; charset=utf-8

file russian_cp1251.txt
# russian_cp1251.txt: ISO-8859 text
# (file не всегда точно определяет кодировку!)
```

### 7.2 Конвертация кодировок

```bash
# iconv: из Windows-1251 в UTF-8
iconv -f WINDOWS-1251 -t UTF-8 input.txt > output.txt

# Список доступных кодировок
iconv -l | head -20

# С заменой недекодируемых символов
iconv -f CP1251 -t UTF-8//TRANSLIT input.txt > output.txt

# Игнорировать ошибки
iconv -f CP1251 -t UTF-8//IGNORE input.txt > output.txt

```

### 7.3 Просмотр в hex

```bash
# Смотрим байты UTF-8 текста
echo -n "Привет" | xxd
# 00000000: d09f d180 d0b8 d0b2 d0b5 d182            ............

# То же самое в Python
echo -n "Привет" | python3 -c "import sys; print(sys.stdin.buffer.read().hex())"
# d09fd180d0b8d0b2d0b5d182
```

### 7.4 Системная локаль

```bash
# Текущая локаль
locale

# Переменные окружения для кодировки
echo $LANG
# en_US.UTF-8

echo $LC_ALL

# Установка локали
export LANG=ru_RU.UTF-8

```

---

## 8. Работа с кодировками в Python

### 8.1 Строки и байты

```python
# В Python 3: str = Unicode, bytes = сырые байты
text = "Привет"  # str (Unicode)
data = b"Hello"  # bytes (ASCII только)

# Кодирование: str → bytes
encoded = text.encode('utf-8')
print(type(encoded), encoded)
# <class 'bytes'> b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Декодирование: bytes → str
decoded = encoded.decode('utf-8')
print(type(decoded), decoded)
# <class 'str'> Привет
```

### 8.2 Чтение файлов с кодировкой

```python
# Явно указывайте кодировку!
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Файл в Windows-1251
with open('russian.txt', 'r', encoding='cp1251') as f:
    content = f.read()

# Файл с BOM
with open('bom_file.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Обработка ошибок декодирования
with open('mixed.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()  # Неизвестные байты → �

with open('mixed.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()  # Неизвестные байты пропускаются

```

### 8.3 Определение кодировки

```python
# Библиотека chardet
import chardet

with open('unknown.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)
    # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# Декодируем с определённой кодировкой
text = raw_data.decode(result['encoding'])

```

### 8.4 Unicode нормализация

```python

import unicodedata

# Один и тот же символ может быть представлен по-разному
# "é" = U+00E9 (1 символ) или "e" + "́" = U+0065 U+0301 (2 символа)

s1 = "café"  # с U+00E9
s2 = "café"  # с e + combining accent

print(len(s1), len(s2))  # Может быть разная длина!
print(s1 == s2)          # Может быть False!

# Нормализация
s1_nfc = unicodedata.normalize('NFC', s1)
s2_nfc = unicodedata.normalize('NFC', s2)
print(s1_nfc == s2_nfc)  # True

```

### 8.5 Модуль unicodedata — работа с метаданными Unicode

Модуль `unicodedata` предоставляет доступ к базе данных Unicode:

```python

import unicodedata

# Получить название символа
print(unicodedata.name('А'))       # CYRILLIC CAPITAL LETTER A
print(unicodedata.name('€'))       # EURO SIGN
print(unicodedata.name('😀'))      # GRINNING FACE
print(unicodedata.name('∞'))       # INFINITY

```

**Output:**
```

CYRILLIC CAPITAL LETTER A
EURO SIGN
GRINNING FACE
INFINITY

```

```python
# Получить символ по имени
print(unicodedata.lookup('CYRILLIC SMALL LETTER ZHE'))  # ж
print(unicodedata.lookup('SNOWMAN'))                    # ☃
print(unicodedata.lookup('ROCKET'))                     # 🚀
print(unicodedata.lookup('PILE OF POO'))                # 💩

```

**Output:**
```

ж
☃
🚀
💩

```

```python
# Категория символа
print(unicodedata.category('A'))   # Lu (Letter, uppercase)
print(unicodedata.category('a'))   # Ll (Letter, lowercase)
print(unicodedata.category('5'))   # Nd (Number, decimal digit)
print(unicodedata.category('€'))   # Sc (Symbol, currency)
print(unicodedata.category(' '))   # Zs (Separator, space)
print(unicodedata.category('\n'))  # Cc (Other, control)

```

**Output:**
```

Lu
Ll
Nd
Sc
Zs
Cc

```

```python
# Числовое значение символа (для цифр и дробей)
print(unicodedata.numeric('5'))    # 5.0
print(unicodedata.numeric('½'))    # 0.5
print(unicodedata.numeric('¾'))    # 0.75
print(unicodedata.numeric('Ⅳ'))    # 4.0 (римская цифра)
print(unicodedata.numeric('๕'))    # 5.0 (тайская цифра)

```

**Output:**
```

5.0
0.5
0.75
4.0
5.0

```

```python
# Проверка типа символа
char = 'Ж'
print(f"Символ: {char}")
print(f"  Имя: {unicodedata.name(char)}")
print(f"  Категория: {unicodedata.category(char)}")
print(f"  Двунаправленность: {unicodedata.bidirectional(char)}")
print(f"  Ширина (East Asian): {unicodedata.east_asian_width(char)}")

```

**Output:**
```

Символ: Ж
  Имя: CYRILLIC CAPITAL LETTER ZHE
  Категория: Lu
  Двунаправленность: L
  Ширина (East Asian): A

```

### 8.6 Практические примеры с unicodedata

**Пример 1: Удаление диакритических знаков**

```python

import unicodedata

def remove_accents(text):
    """Удаляет диакритические знаки (accents) из текста."""
    # NFD разбивает символы на базовый + комбинирующий знак
    normalized = unicodedata.normalize('NFD', text)
    # Фильтруем только не-комбинирующие символы
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')

print(remove_accents("café résumé naïve"))
# cafe resume naive

print(remove_accents("Cześć świat"))
# Czesc swiat
```

**Output:**
```

cafe resume naive
Czesc swiat

```

**Пример 2: Определение языка текста**

```python

import unicodedata
from collections import Counter

def detect_script(text):
    """Определяет основной скрипт (алфавит) текста."""
    scripts = Counter()
    for char in text:
        if char.isalpha():
            name = unicodedata.name(char, '')
            if 'CYRILLIC' in name:
                scripts['Cyrillic'] += 1
            elif 'LATIN' in name:
                scripts['Latin'] += 1
            elif 'CJK' in name or 'HIRAGANA' in name or 'KATAKANA' in name:
                scripts['CJK'] += 1
            elif 'ARABIC' in name:
                scripts['Arabic'] += 1
            elif 'GREEK' in name:
                scripts['Greek'] += 1
            elif 'HEBREW' in name:
                scripts['Hebrew'] += 1
    return scripts.most_common()

print(detect_script("Привет мир"))
# [('Cyrillic', 9)]

print(detect_script("Hello world"))
# [('Latin', 10)]

print(detect_script("混合 text テスト"))
# [('CJK', 5), ('Latin', 4)]
```

**Output:**
```

[('Cyrillic', 9)]
[('Latin', 10)]
[('CJK', 5), ('Latin', 4)]

```

**Пример 3: Поиск похожих символов (homoglyphs)**

```python

import unicodedata

def find_homoglyphs(char):
    """Находит символы с похожими названиями."""
    target_name = unicodedata.name(char, '')
    if not target_name:
        return []
    
    # Получаем ключевое слово (например, "A" из "LATIN CAPITAL LETTER A")
    words = target_name.split()
    if 'LETTER' in words:
        letter = words[-1]  # Последнее слово — обычно буква
        
        results = []
        # Ищем в разных диапазонах
        for code in range(0x10000):  # Только BMP для скорости
            try:
                c = chr(code)
                name = unicodedata.name(c, '')
                if name.endswith(f'LETTER {letter}') and c != char:
                    results.append((c, name))
            except ValueError:
                pass
        return results[:10]  # Первые 10
    return []

# Поиск "A" в разных алфавитах
for char, name in find_homoglyphs('A')[:5]:
    print(f"  {char} - {name}")

```

**Output:**
```

  Α - GREEK CAPITAL LETTER ALPHA
  А - CYRILLIC CAPITAL LETTER A

```

**Пример 4: Информация о версии Unicode**

```python

import unicodedata

# Версия базы данных Unicode в Python
print(f"Unicode version: {unicodedata.unidata_version}")

```

**Output:**
```

Unicode version: 15.0.0

```

---

## 9. Диагностика и исправление проблем

### 9.1 Типичные симптомы

| Симптом | Вероятная причина |
|---------|-------------------|
| ÐŸÑ€Ð¸Ð²ÐµÑ‚ | UTF-8 открыт как Latin-1/CP1251 |
| Пpивeт | Mojibake (двойное перекодирование) |
| ????? | Кодировка не поддерживает символы |
| □□□□□ | Шрифт не содержит глифы |
| ﻿ | BOM в начале файла |

### 9.2 Mojibake

**Mojibake** — "испорченные символы" при неправильной интерпретации.

```python
# Как получается mojibake
original = "Привет"
# 1. Кодируем в UTF-8
utf8_bytes = original.encode('utf-8')
print(utf8_bytes)  # b'\xd0\x9f\xd1\x80...'

# 2. Неправильно декодируем как Latin-1
wrong = utf8_bytes.decode('latin-1')
print(wrong)  # ÐŸÑ€Ð¸Ð²ÐµÑ‚

```

### 9.3 Исправление mojibake

```python
# Если текст выглядит как: ÐŸÑ€Ð¸Ð²ÐµÑ‚
broken = "ÐŸÑ€Ð¸Ð²ÐµÑ‚"

# Шаг 1: Кодируем обратно как Latin-1 (чтобы получить оригинальные байты)
raw_bytes = broken.encode('latin-1')
print(raw_bytes)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Шаг 2: Декодируем правильно как UTF-8
fixed = raw_bytes.decode('utf-8')
print(fixed)  # Привет

```

### 9.4 Утилита для исправления

```python

def fix_mojibake(text, wrong_encoding='latin-1', correct_encoding='utf-8'):
    """
    Исправляет mojibake.
    
    Args:
        text: Испорченный текст
        wrong_encoding: Кодировка, которой текст был неправильно декодирован
        correct_encoding: Правильная кодировка
    """
    try:
        return text.encode(wrong_encoding).decode(correct_encoding)
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text

# Использование
broken = "ÐŸÑ€Ð¸Ð²ÐµÑ‚"
print(fix_mojibake(broken))  # Привет

```

### 9.5 Скрипт для массового исправления

```bash
#!/bin/bash
# fix_encoding.sh - конвертация файлов из CP1251 в UTF-8

find . -name "*.txt" | while read file; do
    encoding=$(file -bi "$file" | grep -oP 'charset=\K[^ ]+')
    
    if [[ "$encoding" != "utf-8" ]]; then
        echo "Converting: $file ($encoding → UTF-8)"
        iconv -f "$encoding" -t UTF-8 "$file" > "$file.tmp"
        mv "$file.tmp" "$file"
    fi
done

```

---

## 10. Best Practices

### 10.1 Правила работы с кодировками

1. **Всегда используйте UTF-8** — современный стандарт

2. **Явно указывайте кодировку** — не полагайтесь на дефолты

```python
# Плохо
open('file.txt')

# Хорошо
open('file.txt', encoding='utf-8')

```

3. **Храните текст как Unicode** — конвертируйте на границах (ввод/вывод)

4. **Знайте кодировку источника** — спрашивайте, проверяйте

### 10.2 HTTP и кодировки

```http

Content-Type: text/html; charset=utf-8

```

```html

<meta charset="UTF-8">

```

### 10.3 Базы данных

```sql

-- MySQL: создание базы с UTF-8
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- PostgreSQL: по умолчанию UTF-8

```

> **⚠️ Warning:**  
> В MySQL `utf8` — это НЕ полный UTF-8! Используйте `utf8mb4` для полной поддержки Unicode (включая эмодзи).

### 10.4 Git и кодировки

```bash
# Настройка Git для UTF-8
git config --global core.quotepath false
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8

```

---

## 11. Специальные символы и их проблемы

### 11.1 Невидимые символы

| Символ | Code Point | Описание |
|--------|------------|----------|
| NBSP | U+00A0 | Non-breaking space |
| ZWSP | U+200B | Zero-width space |
| ZWNJ | U+200C | Zero-width non-joiner |
| ZWJ | U+200D | Zero-width joiner |
| LRM | U+200E | Left-to-right mark |
| RLM | U+200F | Right-to-left mark |

```python
# Невидимые символы могут сломать сравнение
s1 = "hello"
s2 = "hello\u200b"  # с zero-width space

print(s1 == s2)  # False
print(len(s1), len(s2))  # 5, 6

```

### 11.2 Homoglyphs — похожие символы

```python
# Кириллическая 'а' vs латинская 'a'
cyrillic_a = 'а'  # U+0430
latin_a = 'a'     # U+0061

print(cyrillic_a == latin_a)  # False
print(ord(cyrillic_a), ord(latin_a))  # 1072, 97

```

Это используется в фишинговых атаках:

- `google.com` vs `gооgle.com` (с кириллическими 'о')

### 11.3 Эмодзи сложности

```python
# Эмодзи могут занимать больше одного code point
emoji = "👨‍👩‍👧‍👦"  # Family emoji

print(len(emoji))  # 11 (!) — 7 code points + 4 ZWJ

# Это: 👨 + ZWJ + 👩 + ZWJ + 👧 + ZWJ + 👦
for char in emoji:
    print(f"U+{ord(char):04X}", end=" ")
# U+1F468 U+200D U+1F469 U+200D U+1F467 U+200D U+1F466
```

---

## 12. Common Pitfalls

### 12.1 Не указывать кодировку

❌ **Ошибка:**

```python

with open('file.txt') as f:
    content = f.read()  # Какая кодировка? Зависит от системы!

```

✅ **Решение:**

```python

with open('file.txt', encoding='utf-8') as f:
    content = f.read()

```

### 12.2 MySQL utf8 vs utf8mb4

❌ **Ошибка:**

```sql

CREATE TABLE posts (content TEXT) CHARACTER SET utf8;
-- Не поддерживает эмодзи!

```

✅ **Решение:**

```sql

CREATE TABLE posts (content TEXT) CHARACTER SET utf8mb4;

```

### 12.3 Сравнение строк с разной нормализацией

❌ **Ошибка:**

```python
# Может дать False даже для "одинаковых" строк
s1 == s2

```

✅ **Решение:**

```python

import unicodedata
unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)

```

### 12.4 Доверять file -i

❌ **Ошибка:** Слепо верить `file -i`

```bash

file -i russian.txt
# Может показать iso-8859-1 для CP1251!
```

✅ **Решение:** Используйте `chardet` или знайте источник данных

---

## 13. Сводная таблица кодировок

### 13.1 Основные кодировки: краткий обзор

| Кодировка | Год | Размер символа | Символов | Статус |
|-----------|-----|----------------|----------|--------|
| ASCII | 1963 | 1 байт (7 бит) | 128 | Основа всего, ASCII-часть в UTF-8 |
| ISO-8859-1 (Latin-1) | 1987 | 1 байт | 256 | Устарела, заменена UTF-8 |
| Windows-1252 | 1985 | 1 байт | 256 | Устарела, legacy в Windows |
| KOI8-R | 1993 | 1 байт | 256 | Устарела, legacy в Unix/Linux |
| Windows-1251 (CP1251) | 1990 | 1 байт | 256 | Устарела, legacy в Windows |
| CP866 (DOS) | 1986 | 1 байт | 256 | Устарела, legacy в DOS |
| ISO-8859-5 | 1988 | 1 байт | 256 | Устарела, редко использовалась |
| UTF-8 | 1993 | 1-4 байта | 1,112,064 | **Современный стандарт** |
| UTF-16 | 1996 | 2-4 байта | 1,112,064 | Java, Windows API, JavaScript |
| UTF-32 | 1996 | 4 байта | 1,112,064 | Редко используется |
| GB2312 / GBK / GB18030 | 1980+ | 1-4 байта | варьируется | Китай (GB18030 обязателен) |
| Shift_JIS | 1982 | 1-2 байта | ~7000 | Япония (legacy) |
| EUC-JP | 1991 | 1-3 байта | ~7000+ | Япония (legacy в Unix) |
| EUC-KR | 1991 | 1-2 байта | ~2350 | Корея (legacy) |

### 13.2 Детальное сравнение кодировок

#### ASCII и его потомки

| Свойство | ASCII | ISO-8859-1 | Windows-1252 |
|----------|-------|------------|--------------|
| **Диапазон** | 0x00-0x7F | 0x00-0xFF | 0x00-0xFF |
| **Байт на символ** | 1 | 1 | 1 |
| **Языки** | Английский | Западноевропейские | Западноевропейские + € |
| **Кириллица** | ❌ | ❌ | ❌ |
| **Совместимость с UTF-8** | ✅ (0-127) | ⚠️ (0-127 only) | ⚠️ (0-127 only) |
| **Современный статус** | Подмножество UTF-8 | Устарела | Legacy |

#### Кириллические кодировки

| Свойство | KOI8-R | Windows-1251 | ISO-8859-5 | CP866 |
|----------|--------|--------------|------------|-------|
| **Происхождение** | СССР/Unix | Microsoft | ISO | IBM/DOS |
| **Байт на символ** | 1 | 1 | 1 | 1 |
| **Диапазон** | 0x00-0xFF | 0x00-0xFF | 0x00-0xFF | 0x00-0xFF |
| **Русские буквы** | 0x80-0xFF | 0xC0-0xFF | 0xA1-0xFF | 0x80-0xAF, 0xE0-0xF1 |
| **Украинский** | KOI8-U | ✅ | ❌ | ❌ |
| **Особенность** | "Транслитерируется" | Алфавитный порядок | Редко использовалась | Псевдографика |
| **Где использовалась** | Email, Unix | Windows | Редко | DOS, консоль |
| **Современный статус** | Legacy | Legacy | Практически мертва | Legacy (cmd.exe) |

#### Unicode кодировки

| Свойство | UTF-8 | UTF-16 | UTF-32 |
|----------|-------|--------|--------|
| **Байт на символ** | 1-4 | 2-4 | 4 |
| **ASCII (U+0000-007F)** | 1 байт | 2 байта | 4 байта |
| **Кириллица (U+0400-04FF)** | 2 байта | 2 байта | 4 байта |
| **Китайский (BMP)** | 3 байта | 2 байта | 4 байта |
| **Эмодзи (U+1F600+)** | 4 байта | 4 байта (surrogate) | 4 байта |
| **BOM нужен** | Нет (опционально) | Да (BE/LE) | Да (BE/LE) |
| **Совместим с ASCII** | ✅ | ❌ | ❌ |
| **Endianness** | Не зависит | Зависит | Зависит |
| **Индексация O(1)** | ❌ | ❌ | ✅ |
| **Эффективность (ASCII)** | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Эффективность (CJK)** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

### 13.3 Где какая кодировка используется

| Область применения | Рекомендуемая кодировка | Примечания |
|-------------------|------------------------|------------|
| **Веб (HTML, CSS, JS)** | UTF-8 | ~98% веб-сайтов |
| **JSON** | UTF-8 | Стандарт RFC 8259 |
| **XML** | UTF-8 | Дефолт в XML 1.0 |
| **Python 3 исходники** | UTF-8 | PEP 3120 |
| **Java исходники** | UTF-8 | Unicode escapes для не-UTF-8 |
| **JavaScript/Node.js** | UTF-8 | UTF-16 внутри движка |
| **Windows API** | UTF-16 | Исторически сложилось |
| **Unix/Linux файлы** | UTF-8 | Современный стандарт |
| **macOS** | UTF-8 (NFD) | Нормализация NFD в файловой системе |
| **MySQL** | utf8mb4 | НЕ utf8 (3 байта)! |
| **PostgreSQL** | UTF-8 | Дефолт |
| **SQLite** | UTF-8 | Дефолт |
| **Redis** | UTF-8 | Binary-safe, но UTF-8 рекомендуется |
| **Git** | UTF-8 | Для имён файлов и коммитов |
| **Email (современный)** | UTF-8 | RFC 6532 |
| **Старые Windows файлы** | Windows-1251 | Legacy |
| **Старый DOS** | CP866 | Legacy |
| **Китай (обязательно)** | GB18030 | Гос. стандарт |

### 13.4 Признаки кодировок в hex-дампе

Как определить кодировку по байтам:

```

UTF-8 BOM:           EF BB BF
UTF-16 LE BOM:       FF FE
UTF-16 BE BOM:       FE FF
UTF-32 LE BOM:       FF FE 00 00
UTF-32 BE BOM:       00 00 FE FF

Русский текст "Привет":
  UTF-8:             D0 9F D1 80 D0 B8 D0 B2 D0 B5 D1 82
  Windows-1251:      CF F0 E8 E2 E5 F2
  KOI8-R:            F0 D2 C9 D7 C5 D4
  CP866:             8F E0 A8 A2 A5 E2

Признаки UTF-8 кириллицы:
  - Каждая буква = 2 байта
  - Первый байт: D0 или D1
  - Второй байт: 80-BF

Признаки Windows-1251:
  - Каждая буква = 1 байт
  - Заглавные: C0-DF
  - Строчные: E0-FF

```

### 13.5 Как выбрать кодировку

```

                    ┌─────────────────────────────────┐
                    │    Какую кодировку выбрать?     │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  Это новый проект?            │
                    └───────────────┬───────────────┘
                           │                               │
                          Да              Нет
                           │                │
                           ▼                ▼
                    ┌──────────┐    ┌─────────────────── ┐
                    │  UTF-8   │    │ Нужна совместимость│
                    └──────────┘    │ со старыми данными?│
                                    └─────────┬──────────────────────────┘
                                         │                                    │
                                        Да       Нет
                                         │         │
                                         ▼         ▼
                              ┌───────────────┐┐
                              │ Используйте    │
                              │ исходную       ┘
                              │ кодировку или  │
                              │ конвертируйте  │
                              │ в UTF-8        │
                              └────────────────┘

```

**Правило:** Если сомневаетесь — выбирайте **UTF-8**.

---

## 💡 Key Takeaways

- **ASCII — только латиница**: 7 бит, 128 символов. Остальные языки не поддерживает.

- **Unicode — единая таблица**: Номер для каждого символа всех языков. Каждый символ имеет имя, категорию, числовое значение. UTF-8/16/32 — способы хранения.

- **UTF-8 — современный стандарт**: Совместим с ASCII, переменная длина (1-4 байта), используйте везде.

- **unicodedata — ваш друг**: Модуль Python для работы с метаданными Unicode. `name()`, `category()`, `normalize()` — must-know функции.

- **"Кракозябры" — несовпадение кодировок**: Файл сохранён в одной кодировке, открыт в другой. Диагностируйте с `xxd` и `chardet`.

- **Legacy кодировки всё ещё живы**: Windows-1251, KOI8-R, CP866 — встречаются в старых системах. Знайте, как их определить и конвертировать.

- **Всегда явно указывайте кодировку**: Не полагайтесь на дефолты — они отличаются между системами.

---

## 🚀 Next Steps

**Related Modules:**

- [File Formats](../04_FileFormats/) — как кодировки применяются в форматах файлов
- [JSON](../05_JSON/) — JSON и Unicode

**Practice Ideas:**

1. Создайте файл в UTF-8, откройте его с разными кодировками, посмотрите результат
2. Напишите скрипт для автоматического определения и конвертации кодировки файлов
3. Найдите файл с mojibake и исправьте его
4. Проверьте, какая кодировка используется в вашей системе по умолчанию

**Going Deeper:**

- Изучите Unicode Collation Algorithm (сортировка строк)
- Разберитесь с Punycode (Unicode в доменных именах)
- Посмотрите как работает ICU (International Components for Unicode)

---

## 📚 Additional Resources

**Must Read:**

- [The Absolute Minimum Every Developer Must Know About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) — Joel Spolsky
- [Пара слов про строковые типы в Python](https://github.com/newtover/python_strings/wiki) — отличная шпаргалка по str/bytes, UnicodeDecodeError и отличиям Python 2/3

**Documentation:**

- [Unicode Standard](https://www.unicode.org/standard/standard.html)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)

**Tools:**

- [Unicode Table](https://unicode-table.com/) — поиск символов
- [UTF-8 Encoder/Decoder](https://mothereff.in/utf-8)
- [chardet](https://github.com/chardet/chardet) — определение кодировки

---




