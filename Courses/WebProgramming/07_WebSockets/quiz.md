# WebSocket - Quiz

Проверьте свои знания по теме "WebSocket протокол".

---

## Question 1: WebSocket определение

Что такое WebSocket?

A) Протокол полнодуплексной связи поверх TCP

B) Тип базы данных

C) Новая версия HTTP протокола

D) Замена REST API

---

## Question 2: Handshake

Как начинается WebSocket соединение?

A) С HTTP GET запроса с заголовком Upgrade: websocket

B) С UDP пакета

C) С TCP SYN пакета напрямую

D) С TLS handshake

---

## Question 3: Порт

На каком порту по умолчанию работает WebSocket (ws://)?

A) 8080

B) 9000

C) 443

D) 80 (как HTTP)

---

## Question 4: HTTP статус

Какой HTTP статус-код возвращается при успешном WebSocket handshake?

A) 101 Switching Protocols

B) 426 Upgrade Required

C) 200 OK

D) 301 Redirect

---

## Question 5: Преимущество

Какое главное преимущество WebSocket перед HTTP polling?

A) Двунаправленная связь с низкими накладными расходами

B) Лучшее шифрование

C) Поддержка больших файлов

D) Лучшая совместимость

---

## Question 6: Opcode

Какой opcode используется для текстовых сообщений?

A) 0x0

B) 0x1

C) 0x8

D) 0x9

---

## Question 7: Маскирование

Кто должен маскировать данные в WebSocket?

A) Никто

B) Только клиент

C) Только сервер

D) И клиент, и сервер

---

## Question 8: Ping/Pong

Для чего используются Ping/Pong фреймы?

A) Для отправки данных

B) Для шифрования

C) Для поддержания соединения (keep-alive)

D) Для сжатия

---

## Question 9: ASGI событие

Какое событие ASGI отправляется при получении WebSocket сообщения?

A) websocket.message

B) websocket.data

C) websocket.incoming

D) websocket.receive

---

## Question 10: Close code

Что означает close code 1000?

A) Серверная ошибка

B) Нормальное закрытие соединения

C) Потеря соединения

D) Ошибка протокола

---

## Question 11: JavaScript API

Какое событие JavaScript вызывается при получении сообщения?

A) ws.ondata

B) ws.onincoming

C) ws.onreceive

D) ws.onmessage

---

## Question 12: Масштабирование

Как масштабировать WebSocket на несколько серверов?

A) Использовать Redis Pub/Sub или sticky sessions

B) Использовать UDP

C) Невозможно масштабировать

D) Просто добавить больше серверов

---

## Question 13: Sec-WebSocket-Key

Для чего используется Sec-WebSocket-Key?

A) Для аутентификации пользователя

B) Для шифрования данных

C) Для подтверждения, что сервер понимает WebSocket

D) Для сжатия данных

---

## Question 14: Размер overhead

Какой минимальный overhead у WebSocket фрейма?

A) 2-14 байт

B) 1 килобайт

C) Как у HTTP (сотни байт)

D) 0 байт

---

## Question 15: Закрытие соединения

Какой opcode используется для закрытия соединения?

A) 0x8

B) 0xF

C) 0x0

D) 0x1

---

## Question 16: wss://

Что означает схема wss://?

A) WebSocket secure without TLS

B) WebSocket без шифрования

C) WebSocket streaming

D) WebSocket поверх TLS (шифрование)

---

## Question 17: Binary opcode

Какой opcode используется для бинарных данных?

A) 0x9

B) 0x1

C) 0x8

D) 0x2

---

## Question 18: Connection header

Какое значение должен иметь заголовок Connection при WebSocket handshake?

A) Upgrade

B) close

C) keep-alive

D) websocket

---

## Question 19: Fragments

Для чего используются фрагменты (fragmentation) в WebSocket?

A) Для передачи больших сообщений по частям

B) Для сжатия

C) Для шифрования

D) Для маскирования

---

## Question 20: Close code 1001

Что означает close code 1001?

A) Ошибка протокола

B) Нормальное закрытие

C) Размер сообщения превышен

D) Endpoint уходит (going away) — сервер перезапускается или клиент уходит

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | WebSocket — протокол полнодуплексной (двунаправленной) связи поверх TCP |
| 2 | A | WebSocket начинается с HTTP GET запроса с заголовками Upgrade: websocket |
| 3 | D | ws:// использует порт 80, wss:// — порт 443 (как HTTP/HTTPS) |
| 4 | A | 101 Switching Protocols означает успешный переход на WebSocket |
| 5 | A | Двунаправленная связь без накладных расходов HTTP на каждое сообщение |
| 6 | B | Opcode 0x1 — текст (UTF-8), 0x2 — бинарные данные |
| 7 | B | Клиент → Сервер: данные маскируются; Сервер → Клиент: без маски |
| 8 | C | Ping (0x9) и Pong (0xA) используются для проверки активности соединения |
| 9 | D | ASGI событие websocket.receive содержит text или bytes |
| 10 | B | Close code 1000 — нормальное закрытие без ошибок |
| 11 | D | onmessage вызывается при получении данных от сервера |
| 12 | A | Redis Pub/Sub или sticky sessions решают проблему broadcast между серверами |
| 13 | C | Sec-WebSocket-Accept вычисляется из Key для подтверждения протокола |
| 14 | A | Минимальный заголовок фрейма — 2 байта, максимум 14 для больших сообщений |
| 15 | A | Opcode 0x8 (Close) для закрытия соединения с опциональным кодом и причиной |
| 16 | D | wss:// = WebSocket Secure, использует TLS (порт 443) |
| 17 | D | Opcode 0x2 используется для бинарных данных |
| 18 | A | Connection: Upgrade сообщает о желании переключить протокол |
| 19 | A | Фрагментация позволяет разбить большое сообщение на части |
| 20 | D | 1001 = Going Away — endpoint закрывается (сервер shutdown, переход страницы) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с реализацией чата. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о handshake и фреймах. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Создайте простой WebSocket сервер и клиент для практики. |

---

