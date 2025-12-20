# Language Server Protocol - Quiz

Проверьте свои знания по теме "Language Server Protocol".

---

## Question 1: LSP определение

Что такое Language Server Protocol?

A) Протокол взаимодействия между IDE и language server для функций редактора

B) Только для Python

C) База данных

D) Язык программирования

---

## Question 2: N×M проблема в IDE

Какую проблему решает LSP?

A) N×M проблема: каждый язык требовал поддержки в каждом редакторе

B) Производительность

C) Нет проблемы

D) Безопасность

---

## Question 3: LSP архитектура

Какая архитектура у LSP?

A) Монолитная

B) Peer-to-peer

C) Нет архитектуры

D) Клиент-сервер (IDE — клиент, language server — сервер)

---

## Question 4: LSP communication

Как общаются клиент и сервер в LSP?

A) WebSocket

B) JSON-RPC 2.0 (через stdin/stdout или сокеты)

C) HTTP

D) FTP

---

## Question 5: LSP capabilities

Какие функции предоставляет LSP?

A) Нет функций

B) Только компиляция

C) Автодополнение, go to definition, find references, diagnostics, formatting

D) Только подсветка синтаксиса

---

## Question 6: textDocument/didOpen

Что делает textDocument/didOpen notification?

A) Закрывает документ

B) Не используется

C) Уведомляет сервер, что документ открыт в редакторе

D) Форматирует код

---

## Question 7: textDocument/didChange

Что делает textDocument/didChange notification?

A) Уведомляет сервер об изменениях в документе

B) Открывает документ

C) Закрывает документ

D) Не используется

---

## Question 8: textDocument/completion

Что делает textDocument/completion request?

A) Форматирует код

B) Не используется

C) Закрывает документ

D) Запрашивает варианты автодополнения в указанной позиции

---

## Question 9: textDocument/definition

Что делает textDocument/definition request?

A) Закрывает документ

B) Форматирует код

C) Не используется

D) Запрашивает определение символа (go to definition)

---

## Question 10: textDocument/references

Что делает textDocument/references request?

A) Форматирует код

B) Закрывает документ

C) Не используется

D) Запрашивает все использования символа (find references)

---

## Question 11: textDocument/hover

Что делает textDocument/hover request?

A) Не используется

B) Закрывает документ

C) Форматирует код

D) Запрашивает информацию при наведении на символ (tooltip)

---

## Question 12: textDocument/formatting

Что делает textDocument/formatting request?

A) Закрывает документ

B) Не используется

C) Удаляет код

D) Запрашивает форматирование всего документа

---

## Question 13: textDocument/publishDiagnostics

Что делает textDocument/publishDiagnostics notification?

A) Закрывает документ

B) Не используется

C) Форматирует код

D) Сервер отправляет клиенту ошибки и предупреждения (diagnostics)

---

## Question 14: LSP инициализация

Какой первый запрос в LSP?

A) Нет инициализации

B) textDocument/didOpen

C) initialize (клиент и сервер обмениваются capabilities)

D) textDocument/completion

---

## Question 15: LSP capabilities negotiation

Зачем нужен capabilities negotiation?

A) Не нужен

B) Клиент и сервер сообщают, какие функции поддерживают

C) Только для безопасности

D) Только для производительности

---

## Question 16: LSP и языки

Для каких языков работает LSP?

A) Для любых языков (Python, JavaScript, Rust, Go, etc.)

B) Только для динамических языков

C) Только для Python

D) Только для статических языков

---

## Question 17: LSP в редакторах

Какие редакторы поддерживают LSP?

A) Только Vim

B) Нет поддержки

C) Только VS Code

D) VS Code, Vim, Emacs, Sublime Text, IntelliJ, etc.

---

## Question 18: pyright vs pylsp

В чём отличие pyright от pylsp?

A) Разные реализации Python language server (pyright — TypeScript, быстрый; pylsp — Python)

B) Нет отличий

C) pylsp не для Python

D) pyright только для JavaScript

---

## Question 19: LSP выгоды

Какие главные выгоды LSP?

A) Только скорость

B) Решает N×M проблему, стандартизация, переиспользование серверов

C) Только для одного языка

D) Нет выгод

---

## Question 20: Debug Adapter Protocol

Что такое DAP?

A) База данных

B) Аналог LSP для отладчиков (стандартизация взаимодействия IDE с debuggers)

C) Язык программирования

D) Не используется

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | LSP — протокол взаимодействия между IDE и language server для функций редактора. |
| 2 | A | LSP решает N×M проблему: каждый язык требовал поддержки в каждом редакторе. |
| 3 | D | LSP — клиент-сервер архитектура (IDE — клиент, language server — сервер). |
| 4 | B | Общение через JSON-RPC 2.0 (stdin/stdout или сокеты). |
| 5 | C | LSP: автодополнение, go to definition, find references, diagnostics, formatting. |
| 6 | C | textDocument/didOpen уведомляет сервер, что документ открыт. |
| 7 | A | textDocument/didChange уведомляет сервер об изменениях в документе. |
| 8 | D | textDocument/completion запрашивает варианты автодополнения. |
| 9 | D | textDocument/definition запрашивает определение символа (go to definition). |
| 10 | D | textDocument/references запрашивает все использования символа (find references). |
| 11 | D | textDocument/hover запрашивает информацию при наведении на символ (tooltip). |
| 12 | D | textDocument/formatting запрашивает форматирование всего документа. |
| 13 | D | textDocument/publishDiagnostics — сервер отправляет ошибки и предупреждения. |
| 14 | C | Первый запрос — initialize (обмен capabilities). |
| 15 | B | Capabilities negotiation: клиент и сервер сообщают, какие функции поддерживают. |
| 16 | A | LSP работает для любых языков (Python, JavaScript, Rust, Go, etc.). |
| 17 | D | LSP поддерживают VS Code, Vim, Emacs, Sublime Text, IntelliJ, etc. |
| 18 | A | pyright и pylsp — разные реализации Python language server. |
| 19 | B | LSP решает N×M проблему, стандартизация, переиспользование серверов. |
| 20 | B | DAP — аналог LSP для отладчиков (стандартизация взаимодействия IDE с debuggers). |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы, в которых ошиблись. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать соответствующие разделы лекции. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию и попробуйте ещё раз. |

---

