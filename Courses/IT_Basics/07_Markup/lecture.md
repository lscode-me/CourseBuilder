# Языки разметки
## HTML, XML и Markdown

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать текстовые форматы (модуль 04_FileFormats)
- Знать JSON и YAML (модули 05, 06)
- Иметь базовое представление о веб-страницах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру HTML и его назначение
- Работать с XML и понимать его отличия от HTML
- Писать документацию в Markdown
- Выбирать правильный формат разметки для задачи

---

## 1. Что такое язык разметки

### 1.1 Определение

**Язык разметки (Markup Language)** — система аннотирования текста, где разметка синтаксически отличается от контента.

```html
<p>Это <strong>важный</strong> текст.</p>
```

Здесь:

- `<p>`, `<strong>` — разметка (теги)
- "Это важный текст." — контент

### 1.2 Типы разметки

| Тип | Пример | Назначение |
|-----|--------|------------|
| Презентационная | HTML | Определяет отображение |
| Описательная | DocBook | Описывает структуру |
| Процедурная | TeX | Инструкции обработки |
| Лёгкая | Markdown | Простота написания |

---

## 2. HTML

### 2.1 Основы HTML

**HTML** (HyperText Markup Language) — стандартный язык веб-страниц.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

### 2.2 Структура документа

```
<!DOCTYPE html>          ← Декларация типа документа
<html>                   ← Корневой элемент
├── <head>              ← Метаданные
│   ├── <meta>          ← Кодировка, viewport
│   ├── <title>         ← Заголовок вкладки
│   └── <link>          ← Стили, иконки
└── <body>              ← Видимый контент
    ├── <header>        ← Шапка
    ├── <main>          ← Основной контент
    └── <footer>        ← Подвал
```

### 2.3 Основные теги

```html
<!-- Заголовки -->
<h1>Главный заголовок</h1>
<h2>Подзаголовок</h2>
<h3>Заголовок третьего уровня</h3>

<!-- Текст -->
<p>Параграф текста.</p>
<strong>Жирный текст</strong>
<em>Курсив</em>
<code>Код</code>

<!-- Списки -->
<ul>
    <li>Маркированный элемент</li>
</ul>
<ol>
    <li>Нумерованный элемент</li>
</ol>

<!-- Ссылки и изображения -->
<a href="https://example.com">Ссылка</a>
<img src="image.png" alt="Описание">

<!-- Таблицы -->
<table>
    <tr>
        <th>Header</th>
        <td>Cell</td>
    </tr>
</table>

<!-- Формы -->
<form action="/submit" method="POST">
    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
```

### 2.4 Семантический HTML5

```html
<!-- Семантические элементы -->
<header>Шапка страницы</header>
<nav>Навигация</nav>
<main>Основной контент</main>
<article>Самостоятельная статья</article>
<section>Секция контента</section>
<aside>Боковая панель</aside>
<footer>Подвал страницы</footer>

<!-- Вместо <div class="header"> используйте <header> -->
```

### 2.5 Атрибуты

```html
<!-- Глобальные атрибуты -->
<div id="unique-id">Уникальный ID</div>
<div class="my-class">CSS класс</div>
<div style="color: red;">Inline стиль</div>
<div data-user-id="123">Data атрибут</div>

<!-- Специфичные атрибуты -->
<a href="url" target="_blank" rel="noopener">Ссылка</a>
<img src="img.png" alt="Описание" width="100" height="100">
<input type="email" required placeholder="Email">
```

---

## 3. XML

### 3.1 Что такое XML

**XML** (eXtensible Markup Language) — универсальный формат для структурированных данных.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="1">
        <title>The Pragmatic Programmer</title>
        <author>David Thomas</author>
        <year>2019</year>
    </book>
    <book id="2">
        <title>Clean Code</title>
        <author>Robert C. Martin</author>
        <year>2008</year>
    </book>
</library>
```

### 3.2 XML vs HTML

| Аспект | XML | HTML |
|--------|-----|------|
| Теги | Произвольные | Предопределённые |
| Закрытие тегов | Обязательное | Иногда опционально |
| Регистр | Чувствителен | Не чувствителен |
| Назначение | Данные | Отображение |
| Валидация | DTD, XSD | Loose |

### 3.3 Правила XML

```xml
<!-- 1. Один корневой элемент -->
<root>
    <child>Content</child>
</root>

<!-- 2. Теги должны быть закрыты -->
<element>text</element>
<empty-element />

<!-- 3. Регистр важен -->
<Tag>Not same as</tag>  <!-- ОШИБКА! -->

<!-- 4. Правильная вложенность -->
<a><b></b></a>  <!-- OK -->
<a><b></a></b>  <!-- ОШИБКА! -->

<!-- 5. Атрибуты в кавычках -->
<element attr="value">

<!-- 6. Специальные символы -->
&lt;   <!-- < -->
&gt;   <!-- > -->
&amp;  <!-- & -->
&apos; <!-- ' -->
&quot; <!-- " -->
```

### 3.4 XML в реальном мире

```xml
<!-- RSS Feed -->
<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>My Blog</title>
        <item>
            <title>Post Title</title>
            <link>https://example.com/post</link>
        </item>
    </channel>
</rss>

<!-- SVG (векторная графика) -->
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40" fill="red" />
</svg>

<!-- Android Layout -->
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content">
    <TextView android:text="Hello" />
</LinearLayout>
```

### 3.5 XML в Python

```python
import xml.etree.ElementTree as ET

# Парсинг XML

xml_string = """
<users>
    <user id="1">
        <name>Alice</name>
        <email>alice@example.com</email>
    </user>
</users>
"""

root = ET.fromstring(xml_string)

# Навигация

for user in root.findall('user'):
    name = user.find('name').text
    email = user.find('email').text
    user_id = user.get('id')
    print(f"{name} ({user_id}): {email}")

# Создание XML

root = ET.Element('books')
book = ET.SubElement(root, 'book')
ET.SubElement(book, 'title').text = 'Python Guide'

xml_str = ET.tostring(root, encoding='unicode')
print(xml_str)
```

---

## 4. Markdown

### 4.1 Что такое Markdown

**Markdown** — лёгкий язык разметки для форматирования текста.

- Создан Джоном Грубером в 2004
- Читаем как plain text
- Легко конвертируется в HTML
- Стандарт для документации (GitHub, GitLab, Stack Overflow)

### 4.2 Базовый синтаксис

```markdown
# Заголовок 1
## Заголовок 2
### Заголовок 3

Обычный текст параграфа.

**Жирный текст** и *курсив*.
Также __жирный__ и _курсив_.
***Жирный курсив***

~~Зачёркнутый текст~~

---

> Цитата
> Многострочная цитата

- Маркированный список
- Ещё элемент
  - Вложенный элемент

1. Нумерованный список
2. Второй элемент
   1. Вложенный

`Inline code`

    Блок кода с отступом
    (4 пробела)

[Ссылка](https://example.com)
[Ссылка с заголовком](https://example.com "Заголовок")

![Картинка](image.png)
![Alt текст](image.png "Заголовок")
```

### 4.3 Расширенный синтаксис (GitHub Flavored Markdown)

````markdown
```python
# Блок кода с подсветкой

def hello():
    print("Hello, World!")
```
| Column 1 | Column 2 | Column 3 |
|----------|:--------:|---------:|
| Left     | Center   | Right    |
| aligned  | aligned  | aligned  |

- [x] Выполненная задача
- [ ] Невыполненная задача

Footnote reference[^1]

[^1]: Footnote content.

Автоссылки: https://example.com

:emoji: (на GitHub: :smile:)
````

### 4.4 Markdown в документации

```markdown
# Project Name

Brief description of the project.

## Installation
```bash
pip install myproject

```
## Usage
```python
from myproject import main
main()

```
## API Reference

### `function_name(param1, param2)`

Description of the function.

**Parameters:**
- `param1` (str): Description
- `param2` (int): Description

**Returns:**
- `bool`: Description

## License

MIT License
```

### 4.5 Конвертация Markdown

```bash
# pandoc — универсальный конвертер

pandoc README.md -o README.html
pandoc README.md -o README.pdf

# marked (Node.js)

npx marked README.md > README.html

# Python markdown

python -m markdown README.md > README.html
```

```python
# Python

import markdown

md_text = "# Hello\n\nThis is **bold**."
html = markdown.markdown(md_text)
print(html)
# <h1>Hello</h1>
# <p>This is <strong>bold</strong>.</p>
```

---

## 5. Сравнение форматов

### 5.1 Когда использовать

| Формат | Когда использовать |
|--------|-------------------|
| HTML | Веб-страницы, email templates |
| XML | Конфигурации (legacy), обмен данными, SVG |
| Markdown | Документация, README, заметки |
| JSON | API, современные конфигурации |
| YAML | DevOps, Kubernetes, Ansible |

### 5.2 Читаемость vs Функциональность

```
Простота          Мощность
←─────────────────────────────→
Markdown  HTML  XML  LaTeX
```

### 5.3 Конвертация между форматами

```bash
# Markdown → HTML

pandoc input.md -o output.html

# HTML → Markdown

pandoc input.html -o output.md

# XML → JSON (с xq)

xq '.' input.xml

# Markdown → PDF

pandoc input.md -o output.pdf
```

---

## 6. Практические примеры

### 6.1 README.md шаблон

```markdown
# Project Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build](https://github.com/user/repo/workflows/CI/badge.svg)](actions)

Short description.

## Features

- Feature 1
- Feature 2

## Quick Start
```bash
git clone https://github.com/user/repo.git
cd repo
make install

```
## Documentation

See [docs/](docs/) for detailed documentation.

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push to branch (`git push origin feature/name`)
5. Open Pull Request

## License

MIT © [Author](https://github.com/author)
```

### 6.2 HTML Email Template

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 20px;">
    <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td align="center">
                <table width="600" cellpadding="20">
                    <tr>
                        <td style="background-color: #f8f9fa;">
                            <h1 style="color: #333;">Welcome!</h1>
                            <p>Thank you for signing up.</p>
                            <a href="#" style="background: #007bff; color: white; 
                               padding: 10px 20px; text-decoration: none;">
                                Get Started
                            </a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### 6.3 XML Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <appSettings>
        <add key="DatabaseConnection" value="Server=localhost;Database=mydb"/>
        <add key="LogLevel" value="Info"/>
        <add key="MaxRetries" value="3"/>
    </appSettings>
    
    <logging>
        <logger name="default" level="INFO">
            <appender type="file" path="/var/log/app.log"/>
            <appender type="console"/>
        </logger>
    </logging>
</configuration>
```

---

## 7. Common Pitfalls

### 7.1 HTML: незакрытые теги

❌ **Ошибка:**
```html
<p>Paragraph without closing tag
<div>Another element
```

✅ **Правильно:**
```html
<p>Paragraph with closing tag</p>
<div>Another element</div>
```

### 7.2 XML: регистр тегов

❌ **Ошибка:**
```xml
<User>
    <Name>Alice</name>
</user>
```

✅ **Правильно:**
```xml
<user>
    <name>Alice</name>
</user>
```

### 7.3 Markdown: пробелы для переноса

```markdown
Строка 1
Строка 2 (будет на той же строке!)

Строка 1  
Строка 2 (два пробела в конце = <br>)

Строка 1

Строка 2 (пустая строка = новый параграф)
```

---

## 💡 Key Takeaways

- **HTML — для веба**: Семантические теги, атрибуты, формы.

- **XML — строгий формат**: Обязательное закрытие тегов, чувствителен к регистру.

- **Markdown — для людей**: Простой синтаксис, отлично для документации.

- **Выбор формата**: HTML для отображения, XML для данных (legacy), Markdown для документов.

---

## 🚀 Next Steps

**Related Modules:**

- [Config Files](../08_ConfigFiles/) — INI, TOML
- [JSON](../05_JSON/) — альтернатива XML

**Practice Ideas:**

1. Напишите README.md для своего проекта
2. Создайте HTML страницу с семантической разметкой
3. Конвертируйте XML конфиг в JSON
4. Настройте автоматическую генерацию документации из Markdown

---

## 📚 Additional Resources

- [MDN HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark Spec](https://commonmark.org/)
- [W3C XML](https://www.w3.org/XML/)

---







