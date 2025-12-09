# WebSocket - Quiz

Проверьте свои знания по теме "WebSocket протокол".

---

## Question 1: WebSocket определение





Что такое WebSocket?

A) Протокол полнодуплексной связи поверх TCP

B) Новая версия HTTP протокола

C) Тип базы данных

D) Замена REST API

---

## Question 2: Handshake





Как начинается WebSocket соединение?

A) С HTTP GET запроса с заголовком Upgrade: websocket

B) С TLS handshake

C) С TCP SYN пакета напрямую

D) С UDP пакета

---

## Question 3: Порт





На каком порту по умолчанию работает WebSocket (ws://)?

A) 8080

B) 443

C) 9000

D) 80 (как HTTP)

---

## Question 4: HTTP статус





Какой HTTP статус-код возвращается при успешном WebSocket handshake?

A) 101 Switching Protocols

B) 426 Upgrade Required

C) 301 Redirect

D) 200 OK

---

## Question 5: Преимущество





Какое главное преимущество WebSocket перед HTTP polling?

A) Двунаправленная связь с низкими накладными расходами

B) Поддержка больших файлов

C) Лучшее шифрование

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

A) Только сервер

B) Только клиент

C) Никто

D) И клиент, и сервер

---

## Question 8: Ping/Pong





Для чего используются Ping/Pong фреймы?

A) Для отправки данных

B) Для шифрования

C) Для сжатия

D) Для поддержания соединения (keep-alive)

---

## Question 9: ASGI событие





Какое событие ASGI отправляется при получении WebSocket сообщения?

A) websocket.data

B) websocket.incoming

C) websocket.receive

D) websocket.message

---

## Question 10: Close code





Что означает close code 1000?

A) Нормальное закрытие соединения

B) Серверная ошибка

C) Ошибка протокола

D) Потеря соединения

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

A) Просто добавить больше серверов

B) Использовать Redis Pub/Sub или sticky sessions

C) Невозможно масштабировать

D) Использовать UDP

---

## Question 13: Sec-WebSocket-Key





Для чего используется Sec-WebSocket-Key?

A) Для сжатия данных

B) Для подтверждения, что сервер понимает WebSocket

C) Для аутентификации пользователя

D) Для шифрования данных

---

## Question 14: Размер overhead





Какой минимальный overhead у WebSocket фрейма?

A) 0 байт

B) 1 килобайт

C) 2-14 байт

D) Как у HTTP (сотни байт)

---

## Question 15: Закрытие соединения





Какой opcode используется для закрытия соединения?

A) 0x1

B) 0x0

C) 0x8

D) 0xF

---

## Question 16: wss://




Что означает схема wss://?

A) WebSocket без шифрования

B) WebSocket secure without TLS

C) WebSocket streaming

D) WebSocket поверх TLS (шифрование)

---

## Question 17: Binary opcode




Какой opcode используется для бинарных данных?

A) 0x1

B) 0x9

C) 0x8

D) 0x2

---

## Question 18: Connection header




Какое значение должен иметь заголовок Connection при WebSocket handshake?

A) close

B) keep-alive

C) Upgrade

D) websocket

---

## Question 19: Fragments




Для чего используются фрагменты (fragmentation) в WebSocket?

A) Для шифрования

B) Для передачи больших сообщений по частям

C) Для сжатия

D) Для маскирования

---

## Question 20: Close code 1001




Что означает close code 1001?

A) Нормальное закрытие

B) Размер сообщения превышен

C) Endpoint уходит (going away) — сервер перезапускается или клиент уходит

D) Ошибка протокола

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
| 8 | D | Ping (0x9) и Pong (0xA) используются для проверки активности соединения |
| 9 | C | ASGI событие websocket.receive содержит text или bytes |
| 10 | A | Close code 1000 — нормальное закрытие без ошибок |
| 11 | D | onmessage вызывается при получении данных от сервера |
| 12 | B | Redis Pub/Sub или sticky sessions решают проблему broadcast между серверами |
| 13 | B | Sec-WebSocket-Accept вычисляется из Key для подтверждения протокола |
| 14 | C | Минимальный заголовок фрейма — 2 байта, максимум 14 для больших сообщений |
| 15 | C | Opcode 0x8 (Close) для закрытия соединения с опциональным кодом и причиной |
| 16 | D | wss:// = WebSocket Secure, использует TLS (порт 443) |
| 17 | D | Opcode 0x2 используется для бинарных данных |
| 18 | C | Connection: Upgrade сообщает о желании переключить протокол |
| 19 | B | Фрагментация позволяет разбить большое сообщение на части |
| 20 | C | 1001 = Going Away — endpoint закрывается (сервер shutdown, переход страницы) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете WebSocket. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Попрактикуйтесь с реализацией чата. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о handshake и фреймах. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Создайте простой WebSocket сервер и клиент для практики. |

---

