# Data Transfer Encoding - Quiz

Проверьте свои знания по теме "Кодирование для передачи данных".

---

## Question 1: Base64 назначение

Для чего используется Base64?

A) Представление бинарных данных в виде текста

B) Шифрование данных

C) Сжатие данных

D) Хэширование

---

## Question 2: Base64 символы

Сколько символов использует стандартный Base64?

A) 32

B) 64

C) 128

D) 256

---

## Question 3: Base64 размер

На сколько увеличивается размер данных при Base64 кодировании?

A) ~10%

B) ~50%

C) ~33%

D) ~100%

---

## Question 4: Base64 padding

Что означает символ `=` в конце Base64 строки?

A) Конец данных

B) Ошибка кодирования

C) Разделитель

D) Padding для выравнивания

---

## Question 5: URL encoding

Как кодируется пробел в URL?

A) %20 или +

B) `%10`

C) `\ `

D) `_`

---

## Question 6: URL-safe Base64

Какие символы используются в URL-safe Base64 вместо `+/`?

A) `*&`

B) -_

C) `~!`

D) `$.`

---

## Question 7: Python base64

Как закодировать строку в Base64 в Python?

A) `base64.encode("text")`

B) `"text".to_base64()`

C) base64.b64encode("text".encode())

D) `encode64("text")`

---

## Question 8: urlencode

Какая функция Python кодирует параметры URL?

A) urllib.parse.urlencode(params)

B) `url.encode(params)`

C) `params.to_url()`

D) `encode_url(params)`

---

## Question 9: MIME type JSON

Какой MIME type у JSON?

A) `text/json`

B) application/json

C) `data/json`

D) `json/text`

---

## Question 10: Data URL

Как начинается Data URL для PNG изображения?

A) data:image/png;base64,

B) `image:data/png;`

C) `base64:image/png;`

D) `png:data;base64,`

---

## Question 11: Content-Type charset

Как указать UTF-8 в Content-Type?

A) `text/html; encoding=utf-8`

B) text/html; charset=utf-8

C) `text/html; utf-8`

D) `text/html+utf-8`

---

## Question 12: Процент-кодирование

Как закодировать символ `&` в URL?

A) `%25`

B) %26

C) `%27`

D) `%28`

---

## Question 13: JWT

В каком формате закодированы части JWT токена?

A) Base64 URL-safe

B) Base32

C) Hex

D) ASCII85

---

## Question 14: multipart/form-data

Для чего используется multipart/form-data?

A) Только для текстовых форм

B) Для загрузки файлов через формы

C) Для JSON данных

D) Для сжатия форм

---

## Question 15: Безопасность кодирования

Является ли Base64 шифрованием?

A) Да, это надёжное шифрование

B) Да, если использовать пароль

C) Нет, это только кодирование, данные легко декодировать

D) Зависит от данных

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Base64 преобразует бинарные данные в ASCII текст для передачи. |
| 2 | B | Base64 использует 64 символа: A-Z, a-z, 0-9, +, /. |
| 3 | C | 3 байта → 4 символа, увеличение примерно на 33%. |
| 4 | D | `=` — padding для кратности 4 символам. |
| 5 | A | Пробел → `%20` или `+` (в query string). |
| 6 | B | URL-safe Base64 использует `-` и `_` вместо `+` и `/`. |
| 7 | C | `b64encode` принимает bytes, нужен `.encode()`. |
| 8 | A | `urllib.parse.urlencode()` кодирует словарь в query string. |
| 9 | B | Правильный MIME type: `application/json`. |
| 10 | A | Data URL: `data:mime/type;base64,<данные>`. |
| 11 | B | Параметр `charset=utf-8` указывает кодировку. |
| 12 | B | `&` = `%26` (26 hex = 38 dec = ASCII `&`). |
| 13 | A | JWT использует Base64 URL-safe без padding. |
| 14 | B | multipart/form-data используется для загрузки файлов в HTML формах. |
| 15 | C | Base64 — кодирование, не шифрование. Декодировать может кто угодно. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично понимаете кодирование данных! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите URL encoding и MIME types. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте раздел о Base64. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---

