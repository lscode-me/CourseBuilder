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

A) Конец данных

B) Ошибка кодирования

C) Padding для выравнивания

D) Разделитель

---

## Question 5: URL encoding




Как кодируется пробел в URL?

A) `_`

B) `\ `

C) `%10`

D) %20 или +

---

## Question 6: URL-safe Base64




Какие символы используются в URL-safe Base64 вместо `+/`?

A) `~!`

B) -_

C) `$.`

D) `*&`

---

## Question 7: Python base64




Как закодировать строку в Base64 в Python?

A) base64.b64encode("text".encode())

B) `encode64("text")`

C) `base64.encode("text")`

D) `"text".to_base64()`

---

## Question 8: urlencode




Какая функция Python кодирует параметры URL?

A) `encode_url(params)`

B) urllib.parse.urlencode(params)

C) `url.encode(params)`

D) `params.to_url()`

---

## Question 9: MIME type JSON




Какой MIME type у JSON?

A) `text/json`

B) `json/text`

C) application/json

D) `data/json`

---

## Question 10: Data URL




Как начинается Data URL для PNG изображения?

A) `png:data;base64,`

B) data:image/png;base64,

C) `base64:image/png;`

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

A) %26

B) `%27`

C) `%25`

D) `%28`

---

## Question 13: JWT




В каком формате закодированы части JWT токена?

A) Base64 URL-safe

B) Base32

C) ASCII85

D) Hex

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

A) Зависит от данных

B) Нет, это только кодирование, данные легко декодировать

C) Да, если использовать пароль

D) Да, это надёжное шифрование

---

## Question 16: Base32




Какие символы использует Base32?

A) Только буквы

B) 0-9 и A-F

C) Все ASCII символы

D) A-Z и 2-7

---

## Question 17: quote/unquote




Какие функции Python кодируют/декодируют отдельную строку для URL?

A) escape/unescape

B) encode/decode

C) url_encode/url_decode

D) quote/unquote

---

## Question 18: Content-Disposition inline




Что означает `Content-Disposition: inline`?

A) Показать файл в браузере

B) Сжать файл

C) Удалить файл

D) Скачать файл

---

## Question 19: multipart boundary




Для чего нужен boundary в multipart/form-data?

A) Для сжатия данных

B) Для шифрования

C) Для подсчёта размера

D) Для разделения частей формы

---

## Question 20: parse_qs




Что делает функция `urllib.parse.parse_qs()`?

A) Создаёт query string из словаря

B) Кодирует URL

C) Парсит query string в словарь

D) Декодирует Base64

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Base64 преобразует бинарные данные в ASCII текст для передачи. |
| 2 | D | Base64 использует 64 символа: A-Z, a-z, 0-9, +, /. |
| 3 | C | 3 байта → 4 символа, увеличение примерно на 33%. |
| 4 | C | `=` — padding для кратности 4 символам. |
| 5 | D | Пробел → `%20` или `+` (в query string). |
| 6 | B | URL-safe Base64 использует `-` и `_` вместо `+` и `/`. |
| 7 | A | `b64encode` принимает bytes, нужен `.encode()`. |
| 8 | B | `urllib.parse.urlencode()` кодирует словарь в query string. |
| 9 | C | Правильный MIME type: `application/json`. |
| 10 | B | Data URL: `data:mime/type;base64,<данные>`. |
| 11 | D | Параметр `charset=utf-8` указывает кодировку. |
| 12 | A | `&` = `%26` (26 hex = 38 dec = ASCII `&`). |
| 13 | A | JWT использует Base64 URL-safe без padding. |
| 14 | A | multipart/form-data используется для загрузки файлов в HTML формах. |
| 15 | B | Base64 — кодирование, не шифрование. Декодировать может кто угодно. |
| 16 | D | Base32 использует A-Z (26) + 2-7 (6) = 32 символа. |
| 17 | D | `quote()` кодирует строку, `unquote()` декодирует. |
| 18 | A | `inline` — показать в браузере, `attachment` — скачать. |
| 19 | D | boundary разделяет разные части формы (поля, файлы). |
| 20 | C | `parse_qs()` парсит query string в словарь списков. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично понимаете кодирование данных! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите URL encoding и MIME types. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте раздел о Base64. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---

