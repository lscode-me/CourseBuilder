# Форматы файлов
## Текстовые и бинарные файлы, магические числа и MIME types

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать системы счисления и hex (модуль 02_NumberSystems)
- Знать основы кодировок (модуль 03_Encodings)
- Уметь работать в командной строке

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать текстовые и бинарные файлы
- Определять тип файла по магическим числам
- Работать с командой `file` для идентификации форматов
- Понимать и использовать MIME types
- Анализировать структуру бинарных файлов

---

## 1. Классификация файлов

### 1.1 Текстовые vs Бинарные

**Текстовые файлы:**

- Содержат символы в определённой кодировке
- Читаемы человеком в текстовом редакторе
- Разделены на строки переносами (`\n` или `\r\n`)
- Примеры: `.txt`, `.py`, `.json`, `.html`, `.csv`

**Бинарные файлы:**

- Содержат произвольные байты (0-255)
- Требуют специальных программ для интерпретации
- Не имеют концепции "строк"
- Примеры: `.png`, `.pdf`, `.exe`, `.zip`

### 1.2 Как определить тип

```bash
# Текстовый файл
file README.md
# README.md: UTF-8 Unicode text

# Бинарный файл  
file photo.jpg
# photo.jpg: JPEG image data, JFIF standard 1.01

# Исполняемый файл
file /bin/ls
# /bin/ls: Mach-O 64-bit executable arm64
```

### 1.3 Просмотр содержимого

```bash
# Текстовый файл — читаем
cat script.py

# Бинарный файл — hex dump
xxd image.png | head -5

```

```

00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0100 0000 0100 0802 0000 00d3 1025  ...............%
00000020: 0000 0006 624b 4744 0000 ff00 00ff 00ff  ....bKGD........
00000030: 0000 0001 7348 4953 0000 0000 0000 0001  ....sHIS........
00000040: 0100 0101 0001 0000 0001 0000 0001 0100  ................

```

---

## 2. Магические числа (Magic Numbers)

### 2.1 Что это такое

**Магические числа** — фиксированные байты в начале файла, идентифицирующие его формат.

```

PNG:  89 50 4E 47 0D 0A 1A 0A  (.PNG....)
JPEG: FF D8 FF
PDF:  25 50 44 46              (%PDF)
ZIP:  50 4B 03 04              (PK..)
GIF:  47 49 46 38              (GIF8)

```

### 2.2 Популярные сигнатуры

| Формат | Magic Bytes (hex) | ASCII | Смещение |
|--------|-------------------|-------|----------|
| PNG | `89 50 4E 47 0D 0A 1A 0A` | .PNG.... | 0 |
| JPEG | `FF D8 FF` | - | 0 |
| GIF87a | `47 49 46 38 37 61` | GIF87a | 0 |
| GIF89a | `47 49 46 38 39 61` | GIF89a | 0 |
| PDF | `25 50 44 46 2D` | %PDF- | 0 |
| ZIP | `50 4B 03 04` | PK.. | 0 |
| RAR | `52 61 72 21 1A 07` | Rar!.. | 0 |
| 7z | `37 7A BC AF 27 1C` | 7z... | 0 |
| ELF | `7F 45 4C 46` | .ELF | 0 |
| Mach-O | `FE ED FA CE` или `CF FA ED FE` | - | 0 |
| gzip | `1F 8B` | - | 0 |
| bzip2 | `42 5A 68` | BZh | 0 |
| tar | `75 73 74 61 72` | ustar | 257 |
| SQLite | `53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33` | SQLite format 3 | 0 |
| MP3 | `FF FB` или `49 44 33` | - / ID3 | 0 |
| MP4 | `66 74 79 70` | ftyp | 4 |
| DOCX/XLSX | `50 4B 03 04` | PK.. | 0 (это ZIP!) |

### 2.3 Проверка магических чисел

```bash
# Первые 8 байт PNG
xxd -l 8 image.png
# 00000000: 8950 4e47 0d0a 1a0a                      .PNG....

# Первые 3 байта JPEG
xxd -l 3 photo.jpg  
# 00000000: ffd8 ff                                  ...

# Проверка PDF
xxd -l 5 document.pdf
# 00000000: 2550 4446 2d                             %PDF-
```

### 2.4 Почему расширение файла не надёжно

```bash
# Переименуем PNG в .txt
cp image.png fake.txt

# file определит правильно!
file fake.txt
# fake.txt: PNG image data, 256 x 256, 8-bit/color RGB

# Злоумышленник может скрыть вредоносный файл
file dangerous.jpg  # На самом деле это EXE
# dangerous.jpg: PE32 executable (GUI) Intel 80386
```

---

## 3. Команда file

### 3.1 Основы использования

```bash
# Определить тип файла
file document.pdf
# document.pdf: PDF document, version 1.4

# Несколько файлов
file *.txt
# README.txt: UTF-8 Unicode text
# notes.txt: ASCII text

# Рекурсивно для директории
find . -type f -exec file {} \;

```

### 3.2 Полезные опции

```bash
# MIME тип и кодировка
file -i document.txt
# document.txt: text/plain; charset=utf-8

# Только MIME тип
file --mime-type document.pdf
# document.pdf: application/pdf

# Только кодировка
file --mime-encoding script.py
# script.py: us-ascii

# Следовать симлинкам
file -L link_to_file

# Не показывать имя файла
file -b document.pdf
# PDF document, version 1.4

# Читать список файлов из stdin
find . -name "*.jpg" | file -f -

```

### 3.3 Как работает file

Команда `file` использует:

1. **Magic database** (`/usr/share/misc/magic` или `/usr/share/file/magic`)
2. **Эвристики** для текстовых файлов
3. **Анализ структуры** для бинарных

```bash
# Посмотреть magic database
file -C -m /usr/share/misc/magic

# Версия magic file
file -v

```

### 3.4 Написание собственных magic правил

```bash
# Файл: my_magic
# Формат: offset type test message

# Определение гипотетического формата
0 string MYFORMAT My Custom Format
>8 lelong x version %d

```

```bash
# Использование с кастомной базой
file -m my_magic testfile

```

---

## 4. MIME Types

### 4.1 Что такое MIME

**MIME** (Multipurpose Internet Mail Extensions) — стандарт для описания типа контента.

Формат: `type/subtype`

```

text/plain
text/html
application/json
image/png
audio/mpeg
video/mp4

```

### 4.2 Основные типы

| Тип | Описание | Примеры |
|-----|----------|---------|
| text | Текстовые данные | text/plain, text/html, text/css |
| image | Изображения | image/png, image/jpeg, image/gif |
| audio | Аудио | audio/mpeg, audio/ogg |
| video | Видео | video/mp4, video/webm |
| application | Приложения, данные | application/json, application/pdf |
| multipart | Составные данные | multipart/form-data |

### 4.3 Распространённые MIME types

| Расширение | MIME Type |
|------------|-----------|
| .txt | text/plain |
| .html | text/html |
| .css | text/css |
| .js | application/javascript |
| .json | application/json |
| .xml | application/xml |
| .pdf | application/pdf |
| .zip | application/zip |
| .png | image/png |
| .jpg | image/jpeg |
| .gif | image/gif |
| .svg | image/svg+xml |
| .mp3 | audio/mpeg |
| .mp4 | video/mp4 |
| .wasm | application/wasm |

### 4.4 MIME в HTTP

```http

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"message": "Hello"}

```

```http

POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="photo.jpg"
Content-Type: image/jpeg

[binary data]
------WebKitFormBoundary--

```

### 4.5 MIME в Python

```python

import mimetypes

# По расширению
print(mimetypes.guess_type('document.pdf'))
# ('application/pdf', None)

print(mimetypes.guess_type('archive.tar.gz'))
# ('application/x-tar', 'gzip')

# По MIME типу
print(mimetypes.guess_extension('image/png'))
# '.png'

# С python-magic для определения по содержимому
import magic

mime = magic.Magic(mime=True)
print(mime.from_file('photo.jpg'))
# 'image/jpeg'
```

---

## 5. Структура бинарных файлов

### 5.1 Общие паттерны

Большинство бинарных форматов имеют:

1. **Header (заголовок)** — метаданные в начале файла
2. **Magic number** — идентификатор формата
3. **Chunks/Sections** — блоки данных
4. **Footer (футер)** — необязательные данные в конце

```

┌─────────────────┐
│  Magic Number   │
├─────────────────┤
│     Header      │
├─────────────────┤
│    Chunk 1      │
├─────────────────┤
│    Chunk 2      │
├─────────────────┤
│      ...        │
├─────────────────┤
│     Footer      │
└─────────────────┘

```

### 5.2 Пример: структура PNG

```

PNG Signature: 89 50 4E 47 0D 0A 1A 0A (8 bytes)

Chunks:
┌──────────────────────────────────┐
│ Length (4 bytes, big-endian)     │
├──────────────────────────────────┤
│ Type (4 bytes, ASCII)            │
├──────────────────────────────────┤
│ Data (Length bytes)              │
├──────────────────────────────────┤
│ CRC (4 bytes)                    │
└──────────────────────────────────┘

Required chunks: IHDR, IDAT, IEND
Optional: tEXt, gAMA, sRGB, etc.

```

```bash
# Анализ PNG
xxd image.png | head -10

```

```

00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
          |_____signature___||len ||__type__|
00000010: 0000 0100 0000 0100 0802 0000 00d3 1025  ...............%
          |width ||height|| | | ||____CRC____|
                            ↓ ↓
                            bit depth, color type

```

### 5.3 Пример: структура JPEG

```

JPEG Structure:

- SOI (Start Of Image): FF D8
- Segments: FF XX (marker) + length + data
  - APP0 (JFIF): FF E0
  - DQT (Quantization Table): FF DB
  - SOF (Start Of Frame): FF C0
  - DHT (Huffman Table): FF C4
  - SOS (Start Of Scan): FF DA
- Image data
- EOI (End Of Image): FF D9

```

```bash
# Найти маркеры JPEG
xxd photo.jpg | grep "ff d8\|ff e0\|ff db\|ff c0\|ff d9" | head

```

### 5.4 Анализ бинарных файлов

**Инструменты:**

```bash
# binwalk — анализ embedded файлов
binwalk firmware.bin
# DECIMAL       HEXADECIMAL     DESCRIPTION
# 0             0x0             PNG image, 256 x 256
# 65536         0x10000         gzip compressed data

# strings — извлечение строк
strings binary_file | head

# exiftool — метаданные медиафайлов
exiftool photo.jpg

```

**Python:**

```python

import struct

with open('image.png', 'rb') as f:
    # Читаем PNG signature
    signature = f.read(8)
    print(f"Signature: {signature.hex()}")
    
    # Читаем первый chunk (IHDR)
    length = struct.unpack('>I', f.read(4))[0]
    chunk_type = f.read(4).decode('ascii')
    print(f"Chunk: {chunk_type}, Length: {length}")
    
    # Для IHDR: width, height
    if chunk_type == 'IHDR':
        width = struct.unpack('>I', f.read(4))[0]
        height = struct.unpack('>I', f.read(4))[0]
        print(f"Dimensions: {width}x{height}")

```

**Output:**
```

Signature: 89504e470d0a1a0a
Chunk: IHDR, Length: 13
Dimensions: 256x256

```

---

## 6. Форматы архивов

### 6.1 ZIP

**Структура ZIP:**

```

[Local file header 1]
[File data 1]
[Local file header 2]
[File data 2]
...
[Central directory]
[End of central directory record]

```

```bash
# Просмотр содержимого без распаковки
unzip -l archive.zip

# Информация о файле
zipinfo archive.zip

# DOCX, XLSX, PPTX — это ZIP!
unzip -l document.docx

```

### 6.2 tar

**tar** — не сжимает, только объединяет файлы.

```bash
# Просмотр содержимого
tar -tvf archive.tar

# tar.gz (gzip сжатие)
tar -tzvf archive.tar.gz

# tar.bz2 (bzip2 сжатие)
tar -tjvf archive.tar.bz2

```

### 6.3 gzip vs bzip2 vs xz

| Формат | Команда | Сжатие | Скорость |
|--------|---------|--------|----------|
| gzip | gzip/gunzip | Хорошее | Быстрый |
| bzip2 | bzip2/bunzip2 | Лучше | Медленнее |
| xz | xz/unxz | Лучшее | Самый медленный |

```bash
# Сравнение размеров
ls -la file.txt          # 1000000 bytes
gzip -k file.txt
ls -la file.txt.gz       # ~350000 bytes

bzip2 -k file.txt
ls -la file.txt.bz2      # ~300000 bytes

xz -k file.txt
ls -la file.txt.xz       # ~250000 bytes

```

---

## 7. Исполняемые файлы

### 7.1 ELF (Linux)

**ELF** (Executable and Linkable Format) — формат исполняемых файлов в Linux.

```bash
# Информация о ELF
file /bin/ls
# /bin/ls: ELF 64-bit LSB pie executable, x86-64

# Детальная информация
readelf -h /bin/ls

# Секции
readelf -S /bin/ls

# Символы
nm /bin/ls

```

### 7.2 Mach-O (macOS)

```bash
# Информация о Mach-O
file /bin/ls
# /bin/ls: Mach-O 64-bit executable arm64

# Детальная информация
otool -h /bin/ls

```

### 7.3 PE (Windows)

```bash
# В Linux можно анализировать PE файлы
file program.exe
# program.exe: PE32+ executable (GUI) x86-64

# С помощью objdump
objdump -x program.exe | head

```

---

## 8. Работа с файлами в коде

### 8.1 Определение типа в Python

```python

import magic

# Определение по содержимому
def get_file_type(filepath):
    """Определяет тип файла по содержимому."""
    mime = magic.Magic(mime=True)
    file_type = magic.Magic()
    
    return {
        'mime': mime.from_file(filepath),
        'description': file_type.from_file(filepath)
    }

# Проверка на изображение
def is_image(filepath):
    """Проверяет, является ли файл изображением."""
    mime = magic.Magic(mime=True)
    return mime.from_file(filepath).startswith('image/')

# Пример использования
info = get_file_type('photo.jpg')
print(info)
# {'mime': 'image/jpeg', 'description': 'JPEG image data, JFIF standard 1.01'}
```

### 8.2 Безопасная проверка загружаемых файлов

```python

import magic
from pathlib import Path

ALLOWED_MIMES = {
    'image/jpeg',
    'image/png',
    'image/gif',
    'application/pdf',
}

def validate_upload(file_path: str) -> bool:
    """
    Валидирует загруженный файл.
    Проверяет MIME тип по содержимому, а не по расширению.
    """
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    
    if file_mime not in ALLOWED_MIMES:
        return False
    
    # Дополнительно проверяем magic bytes
    with open(file_path, 'rb') as f:
        header = f.read(8)
        
    # PNG signature
    if file_mime == 'image/png':
        if header[:8] != b'\x89PNG\r\n\x1a\n':
            return False
    
    # JPEG signature
    if file_mime == 'image/jpeg':
        if header[:2] != b'\xff\xd8':
            return False
    
    return True

```

### 8.3 Чтение бинарных данных

```python

import struct

def read_png_header(filepath):
    """Читает заголовок PNG файла."""
    with open(filepath, 'rb') as f:
        # Signature (8 bytes)
        sig = f.read(8)
        if sig != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a PNG file")
        
        # IHDR chunk
        length = struct.unpack('>I', f.read(4))[0]
        chunk_type = f.read(4)
        
        if chunk_type != b'IHDR':
            raise ValueError("IHDR chunk not found")
        
        # Parse IHDR data
        data = f.read(length)
        width, height, bit_depth, color_type = struct.unpack('>IIBB', data[:10])
        
        return {
            'width': width,
            'height': height,
            'bit_depth': bit_depth,
            'color_type': color_type
        }

# Использование
info = read_png_header('image.png')
print(f"Image: {info['width']}x{info['height']}")

```

---

## 9. Создание собственных форматов

### 9.1 Принципы дизайна

1. **Уникальная сигнатура** — легко идентифицировать
2. **Версия формата** — для обратной совместимости
3. **Самоописание** — размеры, типы данных в заголовке
4. **Расширяемость** — chunk-based структура
5. **Контрольные суммы** — целостность данных

### 9.2 Пример простого формата

```python

import struct
import hashlib

# Формат: MYDATA v1
# Signature: "MYDATA" (6 bytes)
# Version: uint16 (2 bytes)  
# Data length: uint32 (4 bytes)
# Data: variable
# Checksum: MD5 (16 bytes)

class SimpleFormat:
    SIGNATURE = b'MYDATA'
    VERSION = 1
    
    @classmethod
    def write(cls, filepath, data: bytes):
        with open(filepath, 'wb') as f:
            # Signature
            f.write(cls.SIGNATURE)
            # Version
            f.write(struct.pack('>H', cls.VERSION))
            # Data length
            f.write(struct.pack('>I', len(data)))
            # Data
            f.write(data)
            # Checksum
            checksum = hashlib.md5(data).digest()
            f.write(checksum)
    
    @classmethod
    def read(cls, filepath) -> bytes:
        with open(filepath, 'rb') as f:
            # Verify signature
            sig = f.read(6)
            if sig != cls.SIGNATURE:
                raise ValueError("Invalid file signature")
            
            # Read version
            version = struct.unpack('>H', f.read(2))[0]
            if version > cls.VERSION:
                raise ValueError(f"Unsupported version: {version}")
            
            # Read data
            length = struct.unpack('>I', f.read(4))[0]
            data = f.read(length)
            
            # Verify checksum
            expected_checksum = f.read(16)
            actual_checksum = hashlib.md5(data).digest()
            if expected_checksum != actual_checksum:
                raise ValueError("Checksum mismatch")
            
            return data

# Использование
SimpleFormat.write('test.mydata', b'Hello, World!')
content = SimpleFormat.read('test.mydata')
print(content)  # b'Hello, World!'

```

---

## 10. Common Pitfalls

### 10.1 Доверие расширению файла

❌ **Ошибка:** Проверять тип только по расширению

```python
# Небезопасно!
if filename.endswith('.jpg'):
    process_image(filename)

```

✅ **Решение:** Проверять содержимое

```python

import magic
mime = magic.Magic(mime=True)
if mime.from_file(filename) == 'image/jpeg':
    process_image(filename)

```

### 10.2 Неправильное чтение бинарных файлов

❌ **Ошибка:** Открывать бинарные файлы без 'rb'

```python
# Плохо — может испортить данные!
with open('image.png', 'r') as f:
    data = f.read()

```

✅ **Решение:** Всегда использовать binary mode

```python

with open('image.png', 'rb') as f:
    data = f.read()

```

### 10.3 Игнорирование endianness

❌ **Ошибка:** Читать многобайтовые числа без учёта порядка байтов

```python
# Какой порядок байтов в файле?
length = int.from_bytes(f.read(4), 'big')  # или 'little'?

```

✅ **Решение:** Знать спецификацию формата

```python
# PNG использует big-endian
length = struct.unpack('>I', f.read(4))[0]

```

### 10.4 Не проверять magic numbers

❌ **Ошибка:** Парсить файл без проверки сигнатуры

```python
# Опасно — может быть не PNG!
width = struct.unpack('>I', f.read(4))[0]

```

✅ **Решение:** Всегда проверять сигнатуру

```python

sig = f.read(8)
if sig != b'\x89PNG\r\n\x1a\n':
    raise ValueError("Not a PNG file")

```

---

## 💡 Key Takeaways

- **Текстовые vs Бинарные**: Текстовые содержат символы в кодировке, бинарные — произвольные байты. Используйте `'rb'` для бинарных.

- **Магические числа надёжнее расширений**: Используйте `file` или проверяйте первые байты для определения типа.

- **MIME types для веба**: Правильный Content-Type критичен для HTTP. `application/json`, `image/png`, etc.

- **Понимание структуры**: Большинство форматов имеют header, chunks, footer. Изучайте спецификации.

- **Безопасность**: Всегда проверяйте тип загружаемых файлов по содержимому, не доверяйте расширению.

---

## 🚀 Next Steps

**Related Modules:**

- [JSON](../05_JSON/) — структура и работа с JSON
- [Compression](../10_Compression/) — подробнее о сжатии

**Practice Ideas:**

1. Напишите скрипт, который находит все файлы с неправильным расширением
2. Проанализируйте структуру JPEG файла с помощью xxd
3. Создайте свой простой бинарный формат для хранения списка задач
4. Напишите валидатор загружаемых файлов для веб-приложения

**Going Deeper:**

- Изучите спецификацию PNG (libpng.org)
- Посмотрите как устроен PDF
- Разберитесь с форматом ELF для исполняемых файлов Linux

---

## 📚 Additional Resources

**Tools:**

- [file manual](https://man7.org/linux/man-pages/man1/file.1.html)
- [binwalk](https://github.com/ReFirmLabs/binwalk)
- [python-magic](https://github.com/ahupp/python-magic)

**Specifications:**

- [PNG Specification](http://www.libpng.org/pub/png/spec/)
- [JPEG Format](https://www.w3.org/Graphics/JPEG/)
- [PDF Reference](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf)

**Learning:**

- [File Signatures Table](https://www.garykessler.net/library/file_sigs.html)
- [MIME Types Registry](https://www.iana.org/assignments/media-types/)

---





