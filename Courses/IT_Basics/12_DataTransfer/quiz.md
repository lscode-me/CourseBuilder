# Data Transfer Encoding - Quiz

Проверьте свои знания по теме "Кодирование для передачи данных".

---

## Question 1: Base64 назначение

Для чего используется Base64?

A) Хэширование

B) Шифрование данных

C) Представление бинарных данных в виде текста

D) Сжатие данных

---

## Question 2: Base64 символы

Сколько символов использует стандартный Base64?

A) 256

B) 32

C) 128

D) 64

---

## Question 3: Base64 размер

На сколько увеличивается размер данных при Base64 кодировании?

A) ~50%

B) ~10%

C) ~33%

D) ~100%

---

## Question 4: Base64 padding

Что означает символ `=` в конце Base64 строки?

A) Ошибка кодирования

B) Конец данных

C) Разделитель

D) Padding для выравнивания

---

## Question 5: URL encoding

Как кодируется пробел в URL?

A) `\ `

B) `_`

C) %20 или +

D) `%10`

---

## Question 6: URL-safe Base64

Какие символы используются в URL-safe Base64 вместо `+/`?

A) -_

B) `$.`

C) `~!`

D) `*&`

---

## Question 7: Python base64

Как закодировать строку в Base64 в Python?

A) base64.b64encode("text".encode())

B) `base64.encode("text")`

C) `"text".to_base64()`

D) `encode64("text")`

---

## Question 8: urlencode

Какая функция Python кодирует параметры URL?

A) `params.to_url()`

B) urllib.parse.urlencode(params)

C) `encode_url(params)`

D) `url.encode(params)`

---

## Question 9: MIME type JSON

Какой MIME type у JSON?

A) `json/text`

B) `text/json`

C) `data/json`

D) application/json

---

## Question 10: Data URL

Как начинается Data URL для PNG изображения?

A) `base64:image/png;`

B) `png:data;base64,`

C) data:image/png;base64,

D) `image:data/png;`

---

## Question 11: Content-Type charset

Как указать UTF-8 в Content-Type?

A) `text/html; encoding=utf-8`

B) `text/html+utf-8`

C) `text/html; utf-8`

D) text/html; charset=utf-8

---

## Question 12: Процент-кодирование

Как закодировать символ `&` в URL?

A) `%27`

B) %26

C) `%28`

D) `%25`

---

## Question 13: JWT

В каком формате закодированы части JWT токена?

A) Hex

B) ASCII85

C) Base32

D) Base64 URL-safe

---

## Question 14: multipart/form-data

Для чего используется multipart/form-data?

A) Для загрузки файлов через формы

B) Только для текстовых форм

C) Для JSON данных

D) Для сжатия форм

---

## Question 15: Безопасность кодирования

Является ли Base64 шифрованием?

A) Нет, это только кодирование, данные легко декодировать

B) Да, это надёжное шифрование

C) Да, если использовать пароль

D) Зависит от данных

---

## Question 16: Base32

Какие символы использует Base32?

A) Все ASCII символы

B) A-Z и 2-7

C) Только буквы

D) 0-9 и A-F

---

## Question 17: quote/unquote

Какие функции Python кодируют/декодируют отдельную строку для URL?

A) url_encode/url_decode

B) encode/decode

C) quote/unquote

D) escape/unescape

---

## Question 18: Content-Disposition inline

Что означает `Content-Disposition: inline`?

A) Сжать файл

B) Скачать файл

C) Удалить файл

D) Показать файл в браузере

---

## Question 19: multipart boundary

Для чего нужен boundary в multipart/form-data?

A) Для разделения частей формы

B) Для шифрования

C) Для сжатия данных

D) Для подсчёта размера

---

## Question 20: parse_qs

Что делает функция `urllib.parse.parse_qs()`?

A) Кодирует URL

B) Создаёт query string из словаря

C) Декодирует Base64

D) Парсит query string в словарь

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Base64 преобразует бинарные данные в ASCII текст для передачи. |
| 2 | D | Base64 использует 64 символа: A-Z, a-z, 0-9, +, /. |
| 3 | C | 3 байта → 4 символа, увеличение примерно на 33%. |
| 4 | D | `=` — padding для кратности 4 символам. |
| 5 | C | Пробел → `%20` или `+` (в query string). |
| 6 | A | URL-safe Base64 использует `-` и `_` вместо `+` и `/`. |
| 7 | A | `b64encode` принимает bytes, нужен `.encode()`. |
| 8 | B | `urllib.parse.urlencode()` кодирует словарь в query string. |
| 9 | D | Правильный MIME type: `application/json`. |
| 10 | C | Data URL: `data:mime/type;base64,<данные>`. |
| 11 | D | Параметр `charset=utf-8` указывает кодировку. |
| 12 | B | `&` = `%26` (26 hex = 38 dec = ASCII `&`). |
| 13 | D | JWT использует Base64 URL-safe без padding. |
| 14 | A | multipart/form-data используется для загрузки файлов в HTML формах. |
| 15 | A | Base64 — кодирование, не шифрование. Декодировать может кто угодно. |
| 16 | B | Base32 использует A-Z (26) + 2-7 (6) = 32 символа. |
| 17 | C | `quote()` кодирует строку, `unquote()` декодирует. |
| 18 | D | `inline` — показать в браузере, `attachment` — скачать. |
| 19 | A | boundary разделяет разные части формы (поля, файлы). |
| 20 | D | `parse_qs()` парсит query string в словарь списков. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично понимаете кодирование данных! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите URL encoding и MIME types. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте раздел о Base64. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---


