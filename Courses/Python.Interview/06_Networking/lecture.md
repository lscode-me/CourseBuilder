# TCP/IP и основы сетей

## Что нужно знать для интервью

Базовые знания сетей важны для backend-разработчика. Вас могут спросить про TCP vs UDP, DNS записи, порты и диагностику сетевых проблем.

---

## 🔑 Ключевые понятия

### Порты

| Порт | Протокол |
|------|----------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 6379 | Redis |
| 27017 | MongoDB |

### TCP vs UDP

| TCP | UDP |
|-----|-----|
| Connection-oriented | Connectionless |
| Гарантия доставки | Нет гарантии |
| Порядок пакетов | Порядок не гарантирован |
| Медленнее | Быстрее |
| HTTP, SSH, FTP | DNS, видео, игры |

### TCP Three-way Handshake

```

Client          Server
   |               |
   |--- SYN ------>|   1. Клиент: "Хочу соединиться"
   |<-- SYN-ACK ---|   2. Сервер: "OK, готов"
   |--- ACK ------>|   3. Клиент: "Отлично, начинаем"
   |               |
   |== Соединение установлено ==
```

**Ответ на интервью:**
> "TCP использует three-way handshake: клиент отправляет SYN, сервер отвечает SYN-ACK, клиент подтверждает ACK. После этого соединение установлено. UDP не имеет handshake — просто отправляет данные."

---

## 🌐 DNS

### Типы записей

| Тип | Описание | Пример |
|-----|----------|--------|
| **A** | IPv4 адрес | example.com → 93.184.216.34 |
| **AAAA** | IPv6 адрес | example.com → 2606:2800:220:1:... |
| **CNAME** | Алиас (каноническое имя) | www.example.com → example.com |
| **MX** | Mail сервер | example.com → mail.example.com |
| **TXT** | Текстовые данные | SPF, DKIM, верификация |
| **NS** | Name server | example.com → ns1.example.com |

### Load Balancing через DNS

> "Можно настроить несколько A-записей с разными IP. DNS будет возвращать их по очереди (round-robin). Это простой способ балансировки, но без health checks."

---

## 🐍 Python socket module

### Address families

```python

import socket

# AF_INET  — IPv4
# AF_INET6 — IPv6
# AF_UNIX  — Unix domain sockets (локальные)
```

### Socket types

```python
# SOCK_STREAM — TCP (поток)
# SOCK_DGRAM  — UDP (датаграммы)
```

### Простой TCP клиент

```python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("example.com", 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    response = s.recv(4096)
    print(response.decode())
```

### Простой TCP сервер

```python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 8080))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        conn.sendall(data)  # Echo
```

---

## 🔧 Диагностика сети

### Команды

```bash

ping google.com           # Проверка доступности
traceroute google.com     # Маршрут до хоста
telnet host 80            # Проверка порта
nc -zv host 80            # Netcat проверка порта
dig example.com           # DNS запрос
nslookup example.com      # DNS запрос (альтернатива)
netstat -tlnp             # Открытые порты
ss -tlnp                  # Современная альтернатива netstat
curl -v http://host       # HTTP запрос с деталями
```

### Диагностика "Connection refused"

1. **Сервис запущен?** `systemctl status service`
2. **Слушает порт?** `netstat -tlnp | grep PORT`
3. **Firewall?** `iptables -L` или `ufw status`
4. **Правильный хост/порт?** Проверьте конфигурацию

---

## ❓ Типичные вопросы на интервью

### Q: Что такое NAT?

**A:**
> "Network Address Translation — преобразование IP адресов. Позволяет множеству устройств в локальной сети использовать один внешний IP. Поэтому у многих роутер имеет адрес 192.168.1.1."

### Q: Разница между switch и router?

**A:**
| Switch | Router |
|--------|--------|
| Layer 2 (MAC) | Layer 3 (IP) |
| Локальная сеть | Между сетями |
| Не знает про IP | Маршрутизирует по IP |

### Q: Что такое firewall?

**A:**
> "Firewall фильтрует сетевой трафик по правилам: разрешает или блокирует соединения на основе IP, портов, протоколов. Может быть программным (iptables, ufw) или аппаратным."

---

## 📚 Дополнительные материалы

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- "TCP/IP Illustrated" by W. Richard Stevens
- [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

---


