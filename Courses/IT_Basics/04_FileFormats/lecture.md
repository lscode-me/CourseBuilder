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

**Важное понимание:** Все файлы на диске — это бинарные данные (последовательности байтов). Разница между "текстовыми" и "бинарными" файлами заключается в том, как мы их интерпретируем.

**Что понимается под "файлами":**

В контексте этой лекции "файл" — это не только объекты файловой системы на диске, но и более широкое понятие:

1. **Файлы файловой системы** — обычные файлы на диске (регулярные файлы, `-`)

2. **Файлы в Unix-философии** ("всё есть файл"):
   - **Потоки** (`stdin`, `stdout`, `stderr`) — стандартные потоки ввода/вывода
   - **Символьные устройства** (`c`) — терминалы, последовательные порты (`/dev/tty`, `/dev/ttyUSB0`)
   - **Блочные устройства** (`b`) — диски, разделы (`/dev/sda`, `/dev/nvme0n1`)
   - **Именованные каналы (FIFO)** (`p`) — `mkfifo pipe`
   - **Сокеты** (`s`) — Unix domain sockets

3. **Псевдофайловые системы:**
   - `/proc/*` — информация о процессах и системе
   - `/sys/*` — информация о ядре и устройствах
   - `/dev/*` — устройства (хотя некоторые реальные, некоторые виртуальные)

4. **Объекты object storage:**
   - **S3 objects** (Amazon S3, MinIO)
   - **Azure Blob Storage**
   - **Google Cloud Storage**
   - **Другие объектные хранилища**

Технически объекты storage не являются файлами файловой системы, но к ним применимы те же принципы: они представляют собой последовательности байтов, которые могут быть текстовыми или бинарными, имеют MIME types, могут быть идентифицированы по магическим числам и т.д.

**Примеры:**

```bash
# Обычный файл
cat /etc/passwd

# Псевдофайл из /proc
cat /proc/cpuinfo  # Текстовые данные о процессоре

# Устройство (блочное)
dd if=/dev/sda of=backup.img  # Бинарные данные диска

# Поток
echo "Hello" | cat  # Текстовые данные через pipe

# S3 объект (через AWS CLI)
aws s3 cp s3://bucket/file.txt -  # Текстовые данные из S3
```

**Текстовые файлы:**

- Содержат байты, которые можно интерпретировать как символы в определённой кодировке (UTF-8, ASCII, Windows-1251 и т.д.)
- Большинство байтов соответствуют читаемым символам
- Читаемы человеком в текстовом редакторе
- Разделены на строки переносами (`\n` или `\r\n`)
- Примеры: `.txt`, `.py`, `.json`, `.html`, `.csv`

**Бинарные файлы** (в узком смысле — файлы, не предназначенные для текстовой интерпретации):

- Содержат произвольные байты (0-255), которые не обязательно представляют текст
- Требуют специальных программ для интерпретации по их структуре
- Не имеют концепции "строк" — данные организованы по-другому (chunks, segments, records)
- Примеры: `.png`, `.pdf`, `.exe`, `.zip`

**Важно:** Даже в бинарных файлах могут быть текстовые строки! Например, в PNG файлах могут быть метаданные (tEXt chunks), в PDF — текст документа, в исполняемых файлах — строковые константы. Их можно извлечь с помощью утилиты `strings`:

```bash
# Извлечение строк из бинарного файла
strings image.png | head
strings program.exe | grep -i "error"
strings document.pdf | head -20
```

Утилита `strings` ищет последовательности печатных ASCII символов (обычно минимум 4 символа подряд) и выводит их. Это полезно для анализа бинарных файлов, поиска метаданных или отладочной информации.

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

### 1.4 Python open() — автоматическое преобразование в текст

**Важное отличие Python 3 от командной строки:**

В Python 3 функция `open()` **по умолчанию** открывает файлы в текстовом режиме и автоматически декодирует байты в строки:

```python
# Python 3: по умолчанию текстовый режим
with open('file.txt') as f:  # Режим 'r' (текст)
    content = f.read()  # Получаем строку (str), не байты!
    print(type(content))  # <class 'str'>

# Для бинарных данных нужно явно указать 'rb'
with open('image.png', 'rb') as f:  # Бинарный режим
    data = f.read()  # Получаем байты (bytes)
    print(type(data))  # <class 'bytes'>
```

**Сравнение с командной строкой:**

Командные утилиты `cat`, `head`, `tail` **не преобразуют** файлы в текст — они просто выводят байты на экран, и терминал интерпретирует их как символы согласно своей кодировке:

```bash
# cat выводит байты как есть
cat file.txt  # Терминал интерпретирует байты как символы в своей кодировке

# Если файл бинарный, увидим "мусор"
cat image.png  # Увидим странные символы и возможно звуковой сигнал
```

**Про кодировку терминала:**

Терминал имеет свою кодировку (обычно UTF-8 в современных системах). Когда `cat` выводит байты, терминал пытается интерпретировать их как символы в этой кодировке. Если байты соответствуют валидным символам UTF-8 — они отображаются корректно. Если нет — терминал показывает заменяющие символы (например, `�`) или управляющие последовательности (звуковые сигналы, изменение цвета и т.д.). Это не преобразование файла — это просто способ отображения байтов на экране.

**Как узнать кодировку терминала:**

```bash
# В Linux/macOS через переменную окружения
echo $LANG
# en_US.UTF-8 (кодировка указана после точки)

# Или более точно
locale charmap
# UTF-8

# Посмотреть все настройки локали
locale

# В Python можно проверить кодировку stdout
python3 -c "import sys; print(sys.stdout.encoding)"
# UTF-8

# Или через locale в Python
python3 -c "import locale; print(locale.getpreferredencoding())"
# UTF-8
```

**Важно:** Если кодировка терминала не совпадает с кодировкой файла, символы могут отображаться некорректно. Например, если файл в Windows-1251, а терминал в UTF-8, кириллица будет показана как "кракозябры".

**Историческая справка:**

В Python 2 `open()` работал точно так же, как команды Unix (`cat`, `head`, `tail`) — возвращал байты без преобразования. Python 3 изменил это поведение, сделав текстовый режим по умолчанию для удобства работы со строками.

```python
# Python 2 (устарело) — работает как cat/head/tail
f = open('file.txt')  # Возвращает байты
content = f.read()  # <type 'str'>, но это были байты!
# То же самое, что делает cat file.txt — просто читает байты

# Python 3 — автоматическое преобразование
f = open('file.txt')  # Возвращает строки (Unicode)
content = f.read()  # <class 'str'> — настоящие строки
```

**Практическое правило:**

- Используйте `open('file', 'r')` или просто `open('file')` для текстовых файлов
- Всегда используйте `open('file', 'rb')` для бинарных файлов (изображения, архивы, исполняемые файлы)
- Если не уверены — используйте `'rb'`, потом можно декодировать вручную с помощью `.decode()`:

```python
# Читаем как байты, потом декодируем
with open('file.txt', 'rb') as f:
    data = f.read()  # bytes
    text = data.decode('utf-8')  # str

# Или с обработкой ошибок
text = data.decode('utf-8', errors='ignore')  # Пропустить невалидные байты
```

---

## 2. Магические числа (Magic Numbers)

### 2.1 Что это такое

**Магические числа** (также называемые "file signatures" или "magic bytes") — фиксированные последовательности байтов в начале файла, которые однозначно идентифицируют его формат.

**Важно:** Магические числа используются в основном для **бинарных файлов**. Текстовые файлы обычно определяются по содержимому (эвристики команды `file`) или расширению, так как у них нет фиксированной сигнатуры — любой текст может быть валидным текстовым файлом.

**Зачем они нужны:**

1. **Надёжная идентификация формата** — расширение файла можно легко изменить, но содержимое останется прежним. Магические числа позволяют определить формат по содержимому
2. **Безопасность** — проверка магических чисел помогает обнаружить подмену файлов (например, вредоносный `.exe`, переименованный в `.jpg`)
3. **Автоматическая обработка** — программы могут автоматически определить, какой парсер использовать для файла
4. **Исторические причины** — в Unix-системах расширения файлов не всегда использовались, поэтому формат определялся по содержимому

**Как это работает:**

Программа читает первые несколько байтов файла и сравнивает их с известными сигнатурами. Если совпадение найдено — формат определён.

```

PNG:  89 50 4E 47 0D 0A 1A 0A  (.PNG....)
JPEG: FF D8 FF
PDF:  25 50 44 46              (%PDF)
ZIP:  50 4B 03 04              (PK..)
GIF:  47 49 46 38              (GIF8)

```

**Интересные детали:**

- Некоторые сигнатуры читаемы как ASCII (PNG начинается с `.PNG`, PDF с `%PDF`)
- Другие — произвольные байты (JPEG начинается с `FF D8 FF`)
- Некоторые форматы имеют сигнатуру не в самом начале (например, MP4 имеет `ftyp` на смещении 4 байта)
- ZIP файлы начинаются с `PK` — это инициалы Фила Каца (Phil Katz), создателя формата ZIP

**Почему PNG сигнатура содержит `0D 0A` и `1A`:**

PNG сигнатура: `89 50 4E 47 0D 0A 1A 0A` (`.PNG\r\n\x1a\n`)

- `89 50 4E 47` — `.PNG` в ASCII
- `0D 0A` — `\r\n` (CRLF, перевод строки в Windows/DOS). Это сделано для того, чтобы PNG файлы корректно обрабатывались при передаче через системы, которые преобразуют переводы строк (например, старые FTP серверы в текстовом режиме)
- `1A` — символ Ctrl+Z (EOF в DOS). В старых DOS системах этот символ означал конец файла, что помогало предотвратить случайное отображение бинарных данных как текста
- `0A` — `\n` (LF, перевод строки в Unix)

Эта комбинация гарантирует, что PNG файл будет корректно обработан как бинарный даже в системах, которые пытаются преобразовывать текстовые файлы.

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

Команда `file` — это мощный инструмент, который определяет тип файла по его содержимому, а не по расширению. Она использует многоуровневый подход:

1. **Magic database** (`/usr/share/misc/magic` или `/usr/share/file/magic`) — база данных магических чисел и правил для определения форматов. Содержит тысячи паттернов для различных форматов файлов. Это текстовый файл с правилами вида "если первые 4 байта равны X, то это формат Y"

2. **Эвристики для текстовых файлов** — если файл не определён как бинарный, `file` анализирует его как текст:
   - Проверяет кодировку (UTF-8, ASCII, Windows-1251 и т.д.)
   - Определяет язык программирования по ключевым словам (например, `def`, `import` → Python)
   - Распознаёт структурированные форматы (XML, JSON, CSV)

3. **Анализ структуры для бинарных** — для бинарных файлов `file` читает заголовки и метаданные:
   - Исполняемые файлы: проверяет формат (ELF, Mach-O, PE)
   - Изображения: читает размеры, цветовую модель из заголовков
   - Архивы: анализирует структуру каталогов

**Почему это важно:**

- Расширение файла можно легко изменить, но содержимое останется прежним
- `file` всегда показывает реальный тип файла по содержимому
- Это критично для безопасности — злоумышленники часто маскируют вредоносные файлы под безопасные

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

**MIME** (Multipurpose Internet Mail Extensions) — стандарт для описания типа контента, изначально разработанный для электронной почты, но ставший универсальным способом указания типа данных в интернете.

**Зачем нужны MIME types:**

1. **Компьютеру нужно знать, как обработать данные** — браузер должен понять, что делать с файлом: показать как изображение, выполнить как JavaScript, скачать как архив
2. **Безопасность** — сервер может проверить тип загружаемого файла и отклонить потенциально опасные
3. **Правильная обработка** — разные программы по-разному обрабатывают данные в зависимости от типа
4. **Стандартизация** — единый способ описания типов данных в HTTP, email, файловых системах

**Формат:** `type/subtype`

Тип определяет общую категорию (text, image, application), подтип — конкретный формат.

```

text/plain          # Простой текст
text/html           # HTML документ
application/json    # JSON данные
image/png           # PNG изображение
audio/mpeg          # MP3 аудио
video/mp4           # MP4 видео

```

**Кодировка для текстовых типов:**

Для текстовых MIME types (`text/*`) часто нужно указывать кодировку символов. Это делается через параметр `charset`:

```

text/plain; charset=utf-8
text/html; charset=utf-8
text/css; charset=windows-1251
```

**Где указывается кодировка:**

1. **В HTTP заголовках** — через параметр `charset` в заголовке `Content-Type`:
   ```http

   Content-Type: text/html; charset=utf-8
   ```

2. **В HTML документах** — через мета-тег или атрибут:
   ```html

   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
   <!-- или -->
   <meta charset="utf-8">
   ```

3. **В email** — в заголовке `Content-Type`:
   ```

   Content-Type: text/plain; charset=utf-8
   ```

4. **В файловых системах** — некоторые системы хранят MIME type с кодировкой в метаданных файла

**Важно:** Для бинарных типов (`image/*`, `application/*` и т.д.) кодировка обычно не указывается, так как они не содержат текста в обычном смысле. Исключение — некоторые текстовые форматы, которые классифицируются как `application/*` (например, `application/xml` может иметь `charset`).

**Почему JSON — это `application/json`, а не `text/json`?**

Хотя JSON — это текстовый формат (можно открыть в текстовом редакторе), он классифицируется как `application` по следующим причинам:

1. **Структурированные данные, а не документ** — JSON предназначен для программной обработки, а не для чтения человеком (в отличие от HTML или Markdown)
2. **Строгий синтаксис** — JSON требует валидации и парсинга, это не просто текст
3. **Исторические причины** — когда JSON появился, `text/*` использовался для документов, а `application/*` — для данных, обрабатываемых программами
4. **Семантика использования** — JSON передаёт структурированные данные между системами, а не отображается напрямую пользователю

Аналогично: XML может быть `text/xml` (если это документ) или `application/xml` (если это данные), но чаще используется `application/xml` для структурированных данных.

### 4.2 Основные типы

| Тип | Описание | Примеры |
|-----|----------|---------|
| text | Текстовые данные. Символы в определённой кодировке (UTF-8, ASCII). | text/plain, text/html, text/css, text/javascript |
| image | Изображения в различных форматах. | image/png, image/jpeg, image/gif, image/svg+xml, image/webp |
| audio | Аудио файлы. | audio/mpeg, audio/ogg, audio/wav, audio/webm |
| video | Видео файлы. | video/mp4, video/webm, video/ogg, video/quicktime |
| application | Данные, которые требуют специальной обработки программой. Это самый широкий тип — сюда попадают архивы, документы, исполняемые файлы, структурированные данные (JSON, XML). | application/json, application/pdf, application/zip, application/xml, application/octet-stream |
| multipart | Составные данные, состоящие из нескольких частей с разными типами. Используется в email и формах загрузки файлов. | multipart/form-data, multipart/mixed, multipart/alternative |

**Дополнительные типы:**

- `font/*` — шрифты (font/woff, font/ttf)
- `model/*` — 3D модели (model/gltf+json, model/obj)
- `message/*` — сообщения (message/rfc822 для email)

**Специальный тип `application/octet-stream`:**

Это "универсальный бинарный файл" — используется когда тип неизвестен или файл должен быть скачан, а не обработан браузером. Многие серверы используют его для исполняемых файлов или неизвестных форматов.

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

Большинство бинарных форматов следуют похожей структуре, что упрощает их парсинг и обработку:

1. **Header (заголовок)** — метаданные в начале файла, описывающие общие свойства (размеры, версия формата, параметры). Парсер читает заголовок, чтобы понять, как обрабатывать остальной файл

2. **Magic number** — идентификатор формата, позволяющий быстро определить тип файла без полного парсинга

3. **Chunks/Sections** — блоки данных, организованные по смыслу. Каждый chunk имеет свой тип и размер. Преимущества такой структуры:
   - Можно пропускать неизвестные chunks (расширяемость)
   - Легко добавлять новые типы данных без нарушения совместимости
   - Можно читать файл частично, не загружая всё в память

4. **Footer (футер)** — необязательные данные в конце файла (индексы, контрольные суммы, метаданные)

**Почему бинарные форматы структурированы именно так:**

- **Эффективность** — бинарные данные занимают меньше места, чем текстовые представления

- **Скорость** — не нужно парсить текст, можно читать данные напрямую как числа

- **Точность** — нет проблем с округлением или потерей точности при преобразовании в текст и обратно

- **Расширяемость** — можно добавлять новые типы chunks без нарушения старых парсеров

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

**ZIP** — один из самых популярных форматов архивов, который объединяет несколько файлов в один и может сжимать их.

**Структура ZIP:**

ZIP файл состоит из нескольких частей:

```

[Local file header 1]    # Метаданные файла 1 (имя, размер, метод сжатия)
[File data 1]            # Сжатые или несжатые данные файла 1
[Local file header 2]    # Метаданные файла 2
[File data 2]            # Данные файла 2
...
[Central directory]      # Индекс всех файлов (для быстрого доступа)
[End of central directory record]  # Маркер конца архива

```

**Как это работает:**

- Каждый файл в архиве имеет свой заголовок с метаданными (имя, размер до/после сжатия, метод сжатия, CRC)
- Файлы могут быть сжаты разными алгоритмами (Deflate, BZip2, LZMA) или вообще не сжаты
- Central directory в конце позволяет быстро получить список файлов без чтения всего архива
- Можно добавлять файлы в конец архива без пересоздания всего файла

**Интересный факт:** Форматы Microsoft Office (DOCX, XLSX, PPTX) — это ZIP архивы! Внутри находятся XML файлы с содержимым документа, изображения и другие ресурсы. Можно распаковать `.docx` как обычный ZIP и посмотреть структуру.

```bash
# Просмотр содержимого без распаковки
unzip -l archive.zip

# Информация о файле
zipinfo archive.zip

# DOCX, XLSX, PPTX — это ZIP!

unzip -l document.docx

```

### 6.2 tar

**tar** (Tape Archive) — формат архива, который **не сжимает** данные, а только объединяет несколько файлов и директорий в один файл, сохраняя метаданные (права доступа, владельцы, временные метки).

**Зачем нужен tar без сжатия:**

- Можно объединить много файлов в один для удобной передачи
- Сохраняются все метаданные файловой системы
- Можно работать с архивом без полной распаковки (читать отдельные файлы)
- Сжатие применяется отдельно с помощью gzip, bzip2 или xz

**Комбинации tar + сжатие:**

- `tar.gz` или `.tgz` — tar + gzip (самый популярный)
- `tar.bz2` — tar + bzip2 (лучшее сжатие)
- `tar.xz` — tar + xz (максимальное сжатие)
- `tar.Z` — tar + compress (устаревший формат)

Важно понимать: tar сначала создаёт архив, затем сжатие применяется к этому архиву. Поэтому `.tar.gz` — это сжатый tar-файл, а не tar со сжатыми файлами внутри.

```bash
# Просмотр содержимого
tar -tvf archive.tar

# tar.gz (gzip сжатие)
tar -tzvf archive.tar.gz

# tar.bz2 (bzip2 сжатие)

tar -tjvf archive.tar.bz2

```

### 6.3 gzip vs bzip2 vs xz

Это три популярных алгоритма сжатия данных. Они используют разные методы и имеют разные компромиссы между степенью сжатия и скоростью.

| Формат | Команда | Сжатие | Скорость | Когда использовать |
|--------|---------|--------|----------|-------------------|
| gzip | gzip/gunzip | Хорошее (~60-70% от оригинала) | Быстрый | По умолчанию для большинства задач, быстрая распаковка |
| bzip2 | bzip2/bunzip2 | Лучше (~50-60% от оригинала) | Медленнее | Когда важнее размер, чем скорость |
| xz | xz/unxz | Лучшее (~40-50% от оригинала) | Самый медленный | Максимальное сжатие, не критична скорость |

**Как работают алгоритмы сжатия:**

Все три алгоритма используют вариации одного принципа: находят повторяющиеся паттерны в данных и заменяют их более короткими кодами. Разница в методах:

- **gzip** использует алгоритм Deflate (LZ77 + Huffman coding) — хороший баланс скорости и сжатия

- **bzip2** использует Burrows-Wheeler transform + Huffman — лучше сжимает, но медленнее

- **xz** использует LZMA2 — самый эффективный алгоритм, но требует больше времени и памяти

**Практические рекомендации:**

- Для веб-серверов и логов: **gzip** (быстрая распаковка важна)
- Для долгосрочного хранения: **xz** или **bzip2** (размер важнее скорости)
- Для передачи по сети: **gzip** (быстрее распаковывается на клиенте)

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

Исполняемые файлы — это специальные бинарные файлы, которые содержат машинный код и метаданные, необходимые операционной системе для запуска программы. В отличие от обычных данных, эти файлы выполняются процессором напрямую.

**Что содержится в исполняемом файле:**

- **Машинный код** — инструкции процессора в бинарном виде

- **Метаданные** — информация о том, как загрузить программу в память

- **Секции** — код, данные, строки, символы организованы в секции

- **Таблицы** — таблицы символов, релокаций, динамических библиотек

Каждая операционная система использует свой формат исполняемых файлов, потому что они тесно связаны с архитектурой ОС и процессора.

### 7.1 ELF (Linux)

**ELF** (Executable and Linkable Format) — формат исполняемых файлов в Linux и большинстве Unix-подобных систем. Также используется для объектных файлов (.o) и библиотек (.so).

**Структура ELF:**

- **ELF Header** — общая информация о файле (архитектура, тип, точки входа)

- **Program Header Table** — описывает сегменты для загрузчика

- **Section Header Table** — описывает секции для линкера

- **Секции** — .text (код), .data (инициализированные данные), .bss (неинициализированные данные), .rodata (только чтение), .symtab (символы) и др.

**Типы ELF файлов:**

- **Executable** — исполняемая программа

- **Shared Object** (.so) — динамическая библиотека

- **Relocatable** (.o) — объектный файл для линковки

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

**Mach-O** (Mach Object) — формат исполняемых файлов в macOS и iOS. Разработан для микроядра Mach, которое лежит в основе macOS.

**Особенности Mach-O:**

- Поддерживает "fat binaries" (universal binaries) — один файл может содержать код для нескольких архитектур (например, x86_64 и arm64)
- Использует динамические библиотеки (.dylib) вместо .so
- Имеет систему "frameworks" для организации библиотек
- Поддерживает code signing для безопасности

**Инструменты для работы:**

- `otool` — анализ Mach-O файлов (аналог readelf для ELF)
- `nm` — просмотр символов
- `codesign` — работа с подписями кода

```bash
# Информация о Mach-O

file /bin/ls
# /bin/ls: Mach-O 64-bit executable arm64

# Детальная информация

otool -h /bin/ls

# Проверка подписи

codesign -dv /bin/ls

```

### 7.3 PE (Windows)

**PE** (Portable Executable) — формат исполняемых файлов в Windows (.exe, .dll, .sys).

**Структура PE:**

- Начинается с DOS заголовка (для совместимости со старыми программами)
- PE Signature — сигнатура формата
- COFF Header — общая информация
- Optional Header — важные метаданные (точка входа, размеры, адреса)
- Section Table — описание секций
- Секции — .text, .data, .rdata, .rsrc (ресурсы) и др.

**Особенности PE:**

- Поддерживает ресурсы (иконки, строки, диалоги) встроенные в файл
- Использует динамические библиотеки (.dll)
- Имеет систему манифестов для описания зависимостей
- Поддерживает code signing и Authenticode

**Интересный факт:** PE формат основан на COFF (Common Object File Format), который использовался в ранних версиях Unix. Windows адаптировала его для своих нужд.

```bash
# В Linux можно анализировать PE файлы

file program.exe
# program.exe: PE32+ executable (GUI) x86-64

# С помощью objdump

objdump -x program.exe | head

# В Windows можно использовать:
# dumpbin (из Visual Studio)
# PE Explorer (GUI инструмент)

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






