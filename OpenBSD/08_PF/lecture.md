# Packet Filter (PF)
## Межсетевой экран OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [Networking](../07_Networking/)
- Понимать основы TCP/IP: порты, протоколы, маршрутизация
- Знать концепции файрволов: входящий/исходящий трафик, NAT

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Понимать синтаксис правил PF
- Создавать базовые и продвинутые правила фильтрации
- Настраивать NAT и перенаправление портов
- Управлять состояниями соединений
- Использовать таблицы и якоря
- Мониторить и отлаживать PF

---

## 1. Введение в PF

### 1.1 Что такое PF

**PF (Packet Filter)** — файрвол OpenBSD, созданный в 2001 году. Отличается:
- Простым и читаемым синтаксисом
- Высокой производительностью
- Продвинутыми возможностями (stateful filtering, NAT, QoS)

```sh
# Проверить статус PF
# doas pfctl -s info
Status: Enabled for 5 days 03:21:45

State Table                          Total             Rate
  current entries                       42
  searches                         1234567           2.8/s
  inserts                           12345           0.0/s
```

### 1.2 Включение PF

```sh
# Временно включить
# doas pfctl -e

# Временно выключить
# doas pfctl -d

# Включить при загрузке
# doas rcctl enable pf
```

### 1.3 Файл конфигурации

```sh
# Основной файл
/etc/pf.conf

# Загрузить конфигурацию
# doas pfctl -f /etc/pf.conf

# Проверить синтаксис без применения
# doas pfctl -nf /etc/pf.conf
```

---

## 2. Синтаксис правил

### 2.1 Базовая структура

```
action [direction] [log] [quick] [on interface] [af] [proto protocol]
    [from src_addr [port src_port]] [to dst_addr [port dst_port]]
    [flags tcp_flags] [state]
```

### 2.2 Основные действия

| Действие | Описание |
|----------|----------|
| `pass` | Разрешить пакет |
| `block` | Заблокировать пакет |
| `match` | Применить действия без фильтрации |

### 2.3 Направление

| Направление | Описание |
|-------------|----------|
| `in` | Входящий трафик |
| `out` | Исходящий трафик |
| (пусто) | Оба направления |

### 2.4 Простые примеры

```sh
# Блокировать всё по умолчанию
block all

# Разрешить весь исходящий
pass out all

# Разрешить SSH на всех интерфейсах
pass in proto tcp to port 22

# Разрешить HTTP/HTTPS на конкретном интерфейсе
pass in on em0 proto tcp to port { 80, 443 }
```

---

## 3. Базовая конфигурация

### 3.1 Минимальный файрвол

```sh
# /etc/pf.conf

# Макросы
ext_if = "em0"

# Опции
set skip on lo0
set block-policy drop

# Нормализация
match in all scrub (no-df)

# Правила по умолчанию
block in all
pass out all keep state

# Разрешить SSH
pass in on $ext_if proto tcp to port 22
```

### 3.2 Применение и проверка

```sh
# Проверить синтаксис
# doas pfctl -nf /etc/pf.conf

# Применить
# doas pfctl -f /etc/pf.conf

# Показать правила
# doas pfctl -sr
block drop in all
pass out all flags S/SA keep state
pass in on em0 proto tcp from any to any port = 22 flags S/SA keep state
```

---

## 4. Макросы и таблицы

### 4.1 Макросы

```sh
# Определение макросов
ext_if = "em0"
int_if = "em1"
ssh_port = "22"
web_ports = "{ 80, 443 }"
allowed_hosts = "{ 192.168.1.0/24, 10.0.0.0/8 }"

# Использование
pass in on $ext_if proto tcp to port $ssh_port
pass in on $int_if from $allowed_hosts
```

### 4.2 Таблицы

Таблицы эффективны для больших списков адресов:

```sh
# Определение таблицы
table <bruteforce> persist
table <trusted> { 192.168.1.0/24, 10.0.0.0/8 }
table <blocked> file "/etc/pf.blocked"

# Использование
block in quick from <bruteforce>
pass in from <trusted>
```

### 4.3 Управление таблицами

```sh
# Показать содержимое
# doas pfctl -t bruteforce -T show

# Добавить адрес
# doas pfctl -t bruteforce -T add 192.168.1.50

# Удалить адрес
# doas pfctl -t bruteforce -T delete 192.168.1.50

# Очистить таблицу
# doas pfctl -t bruteforce -T flush

# Загрузить из файла
# doas pfctl -t blocked -T replace -f /etc/pf.blocked
```

---

## 5. NAT и перенаправление

### 5.1 NAT (Network Address Translation)

```sh
# Простой NAT для внутренней сети
ext_if = "em0"
int_if = "em1"
int_net = "192.168.1.0/24"

# NAT исходящего трафика
match out on $ext_if from $int_net nat-to ($ext_if)

# Или с явным указанием
match out on $ext_if from $int_net to any nat-to ($ext_if:0)
```

### 5.2 Port Forwarding

```sh
# Перенаправление порта на внутренний сервер
ext_if = "em0"
webserver = "192.168.1.10"

# Перенаправить порт 80 на веб-сервер
pass in on $ext_if proto tcp to ($ext_if) port 80 rdr-to $webserver port 80

# Перенаправление нескольких портов
pass in on $ext_if proto tcp to port { 80, 443 } rdr-to $webserver
```

### 5.3 1:1 NAT (Binat)

```sh
# Двунаправленный NAT
pass on $ext_if from 192.168.1.10 binat-to 203.0.113.10
```

---

## 6. Stateful Filtering

### 6.1 Состояния соединений

PF по умолчанию использует stateful filtering:

```sh
# keep state — создать запись состояния
pass out all keep state

# modulate state — для TCP, рандомизирует ISN
pass out proto tcp all modulate state

# synproxy state — защита от SYN flood
pass in on $ext_if proto tcp to port 80 synproxy state
```

### 6.2 Просмотр состояний

```sh
# Все состояния
# doas pfctl -ss
all tcp 192.168.1.100:54321 -> 142.250.74.110:443       ESTABLISHED:ESTABLISHED
all tcp 192.168.1.100:54322 -> 93.184.216.34:80         TIME_WAIT:TIME_WAIT

# Статистика состояний
# doas pfctl -si
State Table
  current entries                       42
  searches                         1234567
  inserts                           12345
  removals                          12303
```

### 6.3 Опции состояний

```sh
# Лимиты состояний для правила
pass in proto tcp to port 22 keep state (max 100, source-track rule, max-src-conn 10)

# Глобальные лимиты
set limit states 100000
set limit src-nodes 50000
```

---

## 7. Защита от атак

### 7.1 Защита от брутфорса SSH

```sh
table <bruteforce> persist

# Блокировать адреса из таблицы
block in quick from <bruteforce>

# Добавлять в таблицу при превышении лимита
pass in on $ext_if proto tcp to port 22 \
    keep state (max-src-conn 5, max-src-conn-rate 3/30, \
    overload <bruteforce> flush global)
```

### 7.2 SYN Flood защита

```sh
# synproxy — прокси TCP handshake
pass in on $ext_if proto tcp to port 80 synproxy state
```

### 7.3 Scrubbing (нормализация)

```sh
# Нормализация всех пакетов
match in all scrub (no-df max-mss 1440)

# no-df — очистить бит "don't fragment"
# max-mss — ограничить Maximum Segment Size
# reassemble tcp — пересборка TCP
```

---

## 8. Логирование

### 8.1 Включение логирования

```sh
# Логировать заблокированные пакеты
block in log all

# Логировать определённый трафик
pass in log on $ext_if proto tcp to port 22

# Логировать всё (для отладки)
pass in log (all) on $ext_if
```

### 8.2 Просмотр логов

```sh
# Реальное время
# doas tcpdump -n -e -ttt -i pflog0

# Из файла
# doas tcpdump -n -e -ttt -r /var/log/pflog

# Фильтрация по правилу
# doas tcpdump -n -e -ttt -i pflog0 'rulenum 5'
```

### 8.3 pflogd

```sh
# Включить демон логирования
# doas rcctl enable pflogd
# doas rcctl start pflogd

# Логи сохраняются в /var/log/pflog
```

---

## 9. Anchors (якоря)

### 9.1 Что такое якоря

Якоря позволяют загружать правила динамически:

```sh
# /etc/pf.conf
anchor "ssh_rules"
load anchor "ssh_rules" from "/etc/pf.d/ssh.conf"

anchor "dynamic_rules"  # пустой якорь для динамических правил
```

### 9.2 Управление якорями

```sh
# Показать правила якоря
# doas pfctl -a ssh_rules -sr

# Загрузить правила в якорь
# doas pfctl -a dynamic_rules -f /etc/pf.d/rules.conf

# Очистить якорь
# doas pfctl -a dynamic_rules -F rules
```

---

## 10. Практические примеры

### 10.1 Файрвол для веб-сервера

```sh
# /etc/pf.conf

ext_if = "em0"

# Таблицы
table <bruteforce> persist
table <abusive_clients> persist

# Опции
set skip on lo0
set block-policy drop
set loginterface $ext_if

# Нормализация
match in all scrub (no-df)

# Блокировать известных нарушителей
block in quick from <bruteforce>
block in quick from <abusive_clients>

# По умолчанию
block in all
pass out all keep state

# SSH с защитой от брутфорса
pass in on $ext_if proto tcp to port 22 \
    keep state (max-src-conn 5, max-src-conn-rate 3/30, \
    overload <bruteforce> flush global)

# HTTP/HTTPS
pass in on $ext_if proto tcp to port { 80, 443 } \
    synproxy state

# ICMP ping
pass in on $ext_if proto icmp icmp-type echoreq
```

### 10.2 Роутер с NAT

```sh
# /etc/pf.conf

ext_if = "em0"
int_if = "em1"
int_net = "192.168.1.0/24"
webserver = "192.168.1.10"
mailserver = "192.168.1.20"

set skip on lo0
set block-policy drop

# Нормализация
match in all scrub (no-df)

# NAT для внутренней сети
match out on $ext_if from $int_net nat-to ($ext_if)

# Port forwarding
pass in on $ext_if proto tcp to port 80 rdr-to $webserver
pass in on $ext_if proto tcp to port 443 rdr-to $webserver
pass in on $ext_if proto tcp to port 25 rdr-to $mailserver

# Правила фильтрации
block in all
pass out all keep state

# Разрешить внутренней сети выходить наружу
pass in on $int_if from $int_net

# SSH только из внутренней сети
pass in on $int_if proto tcp to port 22

# ICMP
pass in proto icmp icmp-type echoreq
```

### 10.3 VPN сервер (WireGuard)

```sh
# /etc/pf.conf

ext_if = "em0"
wg_if = "wg0"
wg_net = "10.0.0.0/24"

set skip on lo0

# NAT для VPN клиентов
match out on $ext_if from $wg_net nat-to ($ext_if)

block in all
pass out all keep state

# WireGuard UDP
pass in on $ext_if proto udp to port 51820

# Разрешить трафик VPN клиентов
pass in on $wg_if from $wg_net
```

---

## 11. Отладка и мониторинг

### 11.1 Полезные команды pfctl

```sh
# Статус PF
pfctl -s info

# Показать правила
pfctl -sr

# Показать NAT правила
pfctl -sn

# Показать таблицы
pfctl -sT

# Показать состояния
pfctl -ss

# Показать всё
pfctl -sa

# Статистика интерфейсов
pfctl -si

# Статистика по правилам
pfctl -vsr
```

### 11.2 Тестирование правил

```sh
# Проверить синтаксис
pfctl -nf /etc/pf.conf

# Проверить, какое правило сработает
pfctl -s rules -vvv
```

---

## 💡 Key Takeaways

- **Порядок важен**: PF обрабатывает правила сверху вниз, последнее совпадение побеждает (без `quick`)
- **quick**: Немедленно применяет действие без дальнейшей обработки
- **stateful по умолчанию**: `keep state` включён автоматически для `pass`
- **Таблицы**: Эффективны для больших списков IP-адресов
- **scrub**: Всегда нормализуйте входящий трафик

---

## 🚀 Next Steps

**Related Modules:**
- [Services](../09_Services/) — настройка служб
- [Security](../10_Security/) — дополнительная безопасность

**Practice Ideas:**
1. Настройте базовый файрвол для сервера
2. Добавьте защиту SSH от брутфорса
3. Настройте NAT для домашней сети
4. Создайте правила для веб-сервера с rate-limiting

**Going Deeper:**
- Балансировка нагрузки с PF
- QoS и приоритизация трафика (ALTQ)
- relayd для application-level балансировки

---

## 📚 Additional Resources

**Documentation:**
- [man pf.conf](https://man.openbsd.org/pf.conf) — синтаксис конфигурации
- [man pfctl](https://man.openbsd.org/pfctl) — управление PF
- [PF User's Guide](https://www.openbsd.org/faq/pf/) — официальное руководство
- "The Book of PF" by Peter N. M. Hansteen — отличная книга

---

