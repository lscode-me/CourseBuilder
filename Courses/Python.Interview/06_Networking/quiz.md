# TCP/IP и основы сетей — Quiz

Проверьте знание сетевых протоколов и диагностики.

---

## Question 1: TCP vs UDP

Какой протокол гарантирует доставку пакетов?

A) UDP

B) IP

C) TCP

D) ICMP

---

## Question 2: Порты

Какой порт по умолчанию использует HTTPS?

A) 8080

B) 80

C) 443

D) 22

---

## Question 3: DNS записи

Какой тип DNS записи связывает доменное имя с IPv4 адресом?

A) A

B) CNAME

C) TXT

D) MX

---

## Question 4: Three-way handshake

В каком порядке происходит TCP handshake?

A) ACK → SYN → SYN-ACK

B) UDP не использует handshake

C) SYN → SYN-ACK → ACK

D) SYN → ACK → SYN-ACK

---

## Question 5: Python sockets

Какой socket type используется для TCP?

A) SOCK_STREAM

B) SOCK_DGRAM

C) SOCK_RAW

D) SOCK_TCP

---

## Question 6: Диагностика

Какая команда проверит открыт ли порт 80 на сервере?

A) `ping host 80`

B) `telnet host 80`

C) `dig host 80`

D) `traceroute host 80`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | TCP гарантирует доставку; UDP — нет |
| 2 | C | HTTPS использует порт 443, HTTP — порт 80 |
| 3 | A | A-запись связывает имя с IPv4, AAAA — с IPv6 |
| 4 | C | SYN → SYN-ACK → ACK — классический three-way handshake |
| 5 | A | SOCK_STREAM для TCP, SOCK_DGRAM для UDP |
| 6 | B | `telnet host port` проверяет TCP соединение на порт |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по сетям |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Повторите DNS и диагностику |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите TCP/IP основы |

---

