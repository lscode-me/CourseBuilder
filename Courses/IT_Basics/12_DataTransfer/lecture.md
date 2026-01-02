# Кодирование для передачи данных
## Base64, URL encoding и MIME types

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать кодировки символов (модуль 03_Encodings)
- Знать основы HTTP
- Иметь опыт работы с JSON

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Кодировать и декодировать данные в Base64
- Использовать URL encoding для параметров
- Понимать MIME types и их применение
- Встраивать бинарные данные в текстовые форматы

---

## 1. Зачем нужно кодирование

### 1.1 Проблема

Как передать бинарные данные (изображение, файл) там, где ожидается текст?

- JSON поддерживает только строки, не байты
- URL не поддерживает все символы
- Email был создан для ASCII текста

### 1.2 Решение

Кодирование преобразует бинарные данные в безопасный текст:

```
Binary:  [0x48, 0x65, 0x6C, 0x6C, 0x6F]
Base64:  "SGVsbG8="
```

---

## 2. Base64

### 2.1 Как работает Base64

Base64 использует 64 символа:

- `A-Z` (26)
- `a-z` (26)
- `0-9` (10)
- `+`, `/` (2)
- `=` (padding)

**Алгоритм:**

1. Берём 3 байта (24 бита)
2. Делим на 4 группы по 6 бит
3. Каждая группа → один из 64 символов

```
Input:  "Hi" = 0x48 0x69
Binary: 01001000 01101001
Groups: 010010 000110 1001XX
Base64: S      G      k=

Padding: 2 байта дают 3 символа + 1 "="
```

### 2.2 Командная строка

```bash
# Кодирование

echo -n "Hello, World!" | base64
# SGVsbG8sIFdvcmxkIQ==

# Декодирование

echo "SGVsbG8sIFdvcmxkIQ==" | base64 -d
# Hello, World!

# Файл

base64 image.png > image.txt
base64 -d image.txt > restored.png
```

### 2.3 Python

```python
import base64

# Кодирование

text = "Hello, World!"
encoded = base64.b64encode(text.encode()).decode()
print(encoded)  # SGVsbG8sIFdvcmxkIQ==

# Декодирование

decoded = base64.b64decode(encoded).decode()
print(decoded)  # Hello, World!

# Бинарные данные (изображение)

with open('image.png', 'rb') as f:
    image_data = f.read()
    
encoded_image = base64.b64encode(image_data).decode()

# Декодирование и сохранение

decoded_image = base64.b64decode(encoded_image)
with open('restored.png', 'wb') as f:
    f.write(decoded_image)
```

### 2.4 Варианты Base64

| Вариант | Символы | Применение |
|---------|---------|------------|
| Standard | `+/=` | MIME, PEM |
| URL-safe | `-_` | URL, filenames |
| Base32 | `A-Z2-7` | Case-insensitive |
| Base16 | `0-9A-F` | Hex |

```python
import base64

# URL-safe Base64

encoded = base64.urlsafe_b64encode(b"data?with/special+chars")
print(encoded)  # ZGF0YT93aXRoL3NwZWNpYWwrY2hhcnM=
```

### 2.5 Data URLs

```html
<!-- Изображение встроенное в HTML -->
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" />
```

```python
# Генерация data URL

def image_to_data_url(filepath, mime_type):
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:{mime_type};base64,{data}"

data_url = image_to_data_url('logo.png', 'image/png')
```

---

## 3. URL Encoding

### 3.1 Зачем нужен

URL может содержать только ASCII символы из "безопасного" набора. Специальные символы нужно кодировать.

```
Небезопасные: пробел, ?, &, =, #, %, русские буквы
```

### 3.2 Процент-кодирование

```
Пробел  →  %20 или +
?       →  %3F
&       →  %26
=       →  %3D
#       →  %23

%       →  %25
```

### 3.3 Примеры

```
До:   "Hello World"
После: "Hello%20World" или "Hello+World"

До:   "price=100&discount=10%"
После: "price%3D100%26discount%3D10%25"

До:   "Привет"
После: "%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82"
```

### 3.4 Python urllib

```python
from urllib.parse import quote, unquote, urlencode, parse_qs

# Кодирование строки

encoded = quote("Привет мир!")
print(encoded)  # %D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%20%D0%BC%D0%B8%D1%80%21

# Декодирование

decoded = unquote(encoded)
print(decoded)  # Привет мир!

# Параметры URL

params = {'name': 'Иван', 'city': 'Москва', 'age': 30}
query_string = urlencode(params)
print(query_string)  # name=%D0%98%D0%B2%D0%B0%D0%BD&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&age=30

# Парсинг параметров

parsed = parse_qs(query_string)
print(parsed)  # {'name': ['Иван'], 'city': ['Москва'], 'age': ['30']}
```

### 3.5 Командная строка

```bash
# Python

python3 -c "from urllib.parse import quote; print(quote('Привет'))"

# jq

echo '"Привет"' | jq -r '@uri'
```

---

## 4. MIME Types в деталях

### 4.1 Структура

```
type/subtype; parameter=value

Примеры:
text/plain; charset=utf-8
application/json
image/png
multipart/form-data; boundary=----WebKitFormBoundary
```

### 4.2 Основные типы

| Тип | Описание | Примеры |
|-----|----------|---------|
| text | Текстовые данные | text/html, text/css |
| image | Изображения | image/png, image/jpeg |
| audio | Аудио | audio/mpeg, audio/ogg |
| video | Видео | video/mp4, video/webm |
| application | Приложения, данные | application/json, application/pdf |
| multipart | Составные данные | multipart/form-data |

### 4.3 В HTTP

```http
# Запрос

POST /api/data HTTP/1.1
Content-Type: application/json

{"key": "value"}

# Ответ

HTTP/1.1 200 OK
Content-Type: image/png

[binary data]
```

### 4.4 Content-Disposition

```http
Content-Disposition: attachment; filename="report.pdf"
Content-Disposition: inline; filename="image.png"
```

---

## 5. Multipart формы

### 5.1 Структура

```http
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----Boundary

------Boundary
Content-Disposition: form-data; name="title"

My Document
------Boundary
Content-Disposition: form-data; name="file"; filename="doc.pdf"
Content-Type: application/pdf

[binary content]
------Boundary--
```

### 5.2 Python requests

```python
import requests

# Загрузка файла

files = {
    'file': ('document.pdf', open('document.pdf', 'rb'), 'application/pdf')
}
data = {
    'title': 'My Document',
    'description': 'Test upload'
}

response = requests.post(
    'https://api.example.com/upload',
    files=files,
    data=data
)
```

---

## 6. Практические примеры

### 6.1 JWT токены

```python
import base64
import json

# JWT = header.payload.signature (Base64 URL)

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Декодируем payload

parts = jwt.split('.')
# Добавляем padding если нужно

payload = parts[1] + '=' * (4 - len(parts[1]) % 4)
decoded = base64.urlsafe_b64decode(payload)
data = json.loads(decoded)
print(data)
# {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}
```

### 6.2 Email вложения

```python
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = 'Document'

# Вложение

with open('document.pdf', 'rb') as f:
    attachment = MIMEBase('application', 'pdf')
    attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        'Content-Disposition',
        'attachment; filename="document.pdf"'
    )
    msg.attach(attachment)
```

### 6.3 Изображение в JSON

```python
import base64
import json

def image_to_json(filepath):
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return {
        'filename': filepath,
        'data': data,
        'mime_type': 'image/png'
    }

# В API

image_json = image_to_json('photo.png')
response = requests.post(
    'https://api.example.com/images',
    json=image_json
)
```

---

## 7. Best Practices

### 7.1 Base64

- Увеличивает размер на ~33%
- Не используйте для больших файлов
- Предпочитайте URL-safe вариант для URL

### 7.2 URL Encoding

- Всегда кодируйте пользовательский ввод
- Используйте `urlencode` для параметров
- Помните о разнице `+` и `%20`

### 7.3 MIME Types

- Указывайте правильный Content-Type
- Добавляйте charset для текста
- Используйте Content-Disposition для скачивания

---

## 💡 Key Takeaways

- **Base64 — бинарные данные в текст**: 64 безопасных символа, +33% к размеру.

- **URL encoding — безопасные URL**: Спецсимволы → %XX.

- **MIME types — тип контента**: type/subtype, критично для HTTP.

- **Не путайте с шифрованием**: Кодирование не защищает данные!

---

## 📚 Additional Resources

- [RFC 4648 - Base Encodings](https://tools.ietf.org/html/rfc4648)
- [RFC 3986 - URI](https://tools.ietf.org/html/rfc3986)
- [IANA Media Types](https://www.iana.org/assignments/media-types/)

---

## 🚀 Next Steps

**Это последний модуль курса IT Basics.**

**Практика:**

1. Закодируйте и раскодируйте файл в Base64
2. Правильно URL-кодируйте строку с кириллицей
3. Определите MIME type для разных файлов

**Рекомендуемые курсы для продолжения:**

- [Linux](../../Linux/) — Командная строка Linux
- [Python](../../Python/) — Программирование на Python
- [Networking](../../Networking/) — Компьютерные сети






