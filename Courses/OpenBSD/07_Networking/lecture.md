# Networking
## Сетевая настройка OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [Basic Commands](../03_BasicCommands/)
- Понимать базовые сетевые концепции: IP, маска, шлюз, DNS
- Иметь доступ к системе с правами root (doas)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Настраивать сетевые интерфейсы через hostname.if
- Конфигурировать статический IP и DHCP
- Настраивать маршрутизацию
- Управлять DNS и resolv.conf
- Настраивать VLAN и агрегацию каналов
- Использовать сетевые утилиты диагностики

---

## 1. Основы сетевой конфигурации

### 1.1 Сетевые интерфейсы

```sh
# Показать все интерфейсы
$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 32768
        index 1 priority 0 llprio 3
        groups: lo
        inet 127.0.0.1 netmask 0xff000000

em0: flags=8b43<UP,BROADCAST,RUNNING,PROMISC,ALLMULTI,SIMPLEX,MULTICAST> mtu 1500
        lladdr 00:11:22:33:44:55
        index 2 priority 0 llprio 3
        groups: egress
        media: Ethernet autoselect (1000baseT full-duplex)
        status: active
        inet 192.168.1.100 netmask 0xffffff00 broadcast 192.168.1.255
```

**Типы интерфейсов:**

| Префикс | Тип устройства |
|---------|----------------|
| `em0` | Intel Gigabit |
| `re0` | Realtek Gigabit |
| `bge0` | Broadcom |
| `iwn0` | Intel WiFi |
| `vio0` | Virtio (VM) |
| `lo0` | Loopback |
| `vlan0` | VLAN |
| `trunk0` | Агрегация |

### 1.2 Группы интерфейсов

```sh
# egress — интерфейс по умолчанию для исходящего трафика
$ ifconfig egress
em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        ...
```

---

## 2. Конфигурация hostname.if

### 2.1 Статический IP

Конфигурация хранится в `/etc/hostname.<interface>`:

```sh
# /etc/hostname.em0
inet 192.168.1.100 255.255.255.0
```

Или с CIDR нотацией:

```sh
# /etc/hostname.em0
inet 192.168.1.100/24
```

### 2.2 DHCP

```sh
# /etc/hostname.em0
dhcp
```

### 2.3 Полный пример

```sh
# /etc/hostname.em0
inet 192.168.1.100 255.255.255.0
inet6 autoconf
up
```

### 2.4 Применение настроек

```sh
# Перезапустить интерфейс
# doas sh /etc/netstart em0

# Или вручную
# doas ifconfig em0 down
# doas ifconfig em0 inet 192.168.1.100/24 up
```

---

## 3. Маршрутизация

### 3.1 Шлюз по умолчанию

```sh
# /etc/mygate
192.168.1.1
```

### 3.2 Просмотр таблицы маршрутизации

```sh
$ netstat -rn
Routing tables

Internet:
Destination        Gateway            Flags   Refs      Use   Mtu  Prio Iface
default            192.168.1.1        UGS        0        0     -     8 em0
192.168.1.0/24     192.168.1.100      UCn        1        0     -     4 em0
192.168.1.100      192.168.1.100      UHl        0        0     -     1 lo0
```

### 3.3 Управление маршрутами

```sh
# Добавить маршрут
# doas route add 10.0.0.0/8 192.168.1.254

# Удалить маршрут
# doas route delete 10.0.0.0/8

# Изменить шлюз по умолчанию
# doas route change default 192.168.1.2
```

### 3.4 Включение IP forwarding

Для роутера нужно включить пересылку пакетов:

```sh
# Временно
# doas sysctl net.inet.ip.forwarding=1

# Постоянно в /etc/sysctl.conf
net.inet.ip.forwarding=1

# Для IPv6
net.inet6.ip6.forwarding=1
```

---

## 4. DNS настройка

### 4.1 /etc/resolv.conf

```sh
# /etc/resolv.conf
nameserver 8.8.8.8
nameserver 1.1.1.1
search home.local
lookup file bind
```

### 4.2 Автоматическое обновление при DHCP

При использовании DHCP файл `/etc/resolv.conf` обновляется автоматически.

Чтобы предотвратить перезапись:

```sh
# Сделать файл неизменяемым
# doas chflags schg /etc/resolv.conf
```

### 4.3 Локальный DNS кеш (unbound)

```sh
# Установить unbound
# doas pkg_add unbound

# Включить
# doas rcctl enable unbound
# doas rcctl start unbound

# В /etc/resolv.conf указать локальный
nameserver 127.0.0.1
```

---

## 5. Имя хоста

### 5.1 Настройка hostname

```sh
# /etc/myname
server.home.local

# Применить
# doas hostname server.home.local

# Проверить
$ hostname
server.home.local

$ hostname -s
server
```

### 5.2 /etc/hosts

```sh
# /etc/hosts
127.0.0.1       localhost
::1             localhost
192.168.1.100   server.home.local server
192.168.1.1     gateway.home.local gateway
```

---

## 6. WiFi настройка

### 6.1 Поиск сетей

```sh
# Сканирование
# doas ifconfig iwn0 scan
iwn0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        nwid MyNetwork chan 6 bssid 00:11:22:33:44:55 -65dBm
        nwid OtherNetwork chan 11 bssid aa:bb:cc:dd:ee:ff -78dBm
```

### 6.2 Подключение к WPA2

```sh
# /etc/hostname.iwn0
join "MyNetwork" wpakey "MyPassword"
dhcp
```

### 6.3 Несколько сетей

```sh
# /etc/hostname.iwn0
join "HomeNetwork" wpakey "home123"
join "WorkNetwork" wpakey "work456"
join "OpenCafe"
dhcp
```

---

## 7. VLAN

### 7.1 Создание VLAN

```sh
# /etc/hostname.vlan100
vnetid 100
parent em0
inet 10.100.0.1/24
```

### 7.2 Применение

```sh
# doas sh /etc/netstart vlan100

# Проверка
$ ifconfig vlan100
vlan100: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        lladdr 00:11:22:33:44:55
        vnetid 100 parent em0
        inet 10.100.0.1 netmask 0xffffff00 broadcast 10.100.0.255
```

---

## 8. Агрегация каналов (trunk)

### 8.1 LACP (802.3ad)

```sh
# /etc/hostname.em0
up

# /etc/hostname.em1
up

# /etc/hostname.trunk0
trunkproto lacp
trunkport em0
trunkport em1
inet 192.168.1.100/24
```

### 8.2 Failover

```sh
# /etc/hostname.trunk0
trunkproto failover
trunkport em0 master
trunkport em1
inet 192.168.1.100/24
```

---

## 9. Сетевые утилиты

### 9.1 ping / ping6

```sh
# IPv4
$ ping -c 3 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=117 time=15.234 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=14.987 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=15.102 ms

# IPv6
$ ping6 -c 3 2001:4860:4860::8888
```

### 9.2 traceroute

```sh
$ traceroute google.com
traceroute to google.com (142.250.74.110), 64 hops max, 40 byte packets
 1  192.168.1.1  1.234 ms  0.987 ms  0.876 ms
 2  10.0.0.1  5.432 ms  5.123 ms  4.987 ms
 3  ...
```

### 9.3 netstat

```sh
# Открытые порты
$ netstat -an | grep LISTEN
tcp        0      0  *.22                   *.*                    LISTEN
tcp        0      0  127.0.0.1.25           *.*                    LISTEN

# Статистика интерфейсов
$ netstat -i
Name    Mtu   Network     Address              Ipkts Ierrs    Opkts Oerrs  Coll
em0     1500  <Link>      00:11:22:33:44:55  1234567     0   987654     0     0
```

### 9.4 nc (netcat)

```sh
# Проверить порт
$ nc -vz google.com 443
Connection to google.com 443 port [tcp/https] succeeded!

# Простой сервер
$ nc -l 8080

# Передача файла
# На сервере:
$ nc -l 8080 > file.txt
# На клиенте:
$ nc server 8080 < file.txt
```

### 9.5 tcpdump

```sh
# Захват трафика на интерфейсе
# doas tcpdump -i em0

# Фильтр по порту
# doas tcpdump -i em0 port 80

# Фильтр по хосту
# doas tcpdump -i em0 host 192.168.1.1

# Сохранить в файл
# doas tcpdump -i em0 -w capture.pcap
```

### 9.6 dig / host

```sh
# DNS запрос
$ dig google.com
;; ANSWER SECTION:
google.com.             300     IN      A       142.250.74.110

# Краткий вывод
$ dig +short google.com
142.250.74.110

# Reverse lookup
$ dig -x 8.8.8.8
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.   21600   IN      PTR     dns.google.

# Простой запрос
$ host google.com
google.com has address 142.250.74.110
```

---

## 10. DHCP сервер

### 10.1 dhcpd

```sh
# /etc/dhcpd.conf
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8, 1.1.1.1;
    option domain-name "home.local";
    default-lease-time 86400;
}

# Статические адреса
host server {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 192.168.1.10;
}
```

```sh
# Включить и запустить
# doas rcctl enable dhcpd
# doas rcctl set dhcpd flags em0
# doas rcctl start dhcpd
```

---

## 11. Практические примеры

### 11.1 Настройка роутера

```sh
# 1. Внешний интерфейс (DHCP от провайдера)
# /etc/hostname.em0
dhcp

# 2. Внутренний интерфейс
# /etc/hostname.em1
inet 192.168.1.1/24

# 3. Включить forwarding
# /etc/sysctl.conf
net.inet.ip.forwarding=1

# 4. Настроить NAT в /etc/pf.conf
# (см. модуль PF)

# 5. DHCP сервер
# /etc/dhcpd.conf
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8;
}

# 6. Применить
# doas sh /etc/netstart
# doas rcctl enable dhcpd
# doas rcctl start dhcpd
```

### 11.2 Bonding для отказоустойчивости

```sh
# /etc/hostname.em0
up

# /etc/hostname.em1
up

# /etc/hostname.trunk0
trunkproto failover
trunkport em0 master
trunkport em1
inet 192.168.1.100/24

# Применить
# doas sh /etc/netstart trunk0
```

### 11.3 Множественные IP на интерфейсе

```sh
# /etc/hostname.em0
inet 192.168.1.100/24
inet alias 192.168.1.101/32
inet alias 192.168.1.102/32
```

---

## 💡 Key Takeaways

- **hostname.if**: Простая конфигурация одной строкой
- **/etc/mygate**: Шлюз по умолчанию
- **/etc/myname**: Имя хоста
- **netstat -rn**: Таблица маршрутизации
- **ifconfig**: Основной инструмент диагностики
- **tcpdump**: Анализ сетевого трафика

---

## 🚀 Next Steps

**Related Modules:**
- [PF](../08_PF/) — настройка файрвола
- [Services](../09_Services/) — сетевые службы

**Practice Ideas:**
1. Настройте статический IP и проверьте связь
2. Создайте VLAN для отдельной сети
3. Настройте WiFi с WPA2
4. Запустите DHCP сервер для локальной сети

**Going Deeper:**
- Настройка VPN (WireGuard, OpenIKED)
- IPv6 туннели
- BGP/OSPF маршрутизация с OpenBGPD/OpenOSPFD

---

## 📚 Additional Resources

**Documentation:**
- [man hostname.if](https://man.openbsd.org/hostname.if) — конфигурация интерфейсов
- [man ifconfig](https://man.openbsd.org/ifconfig) — управление интерфейсами
- [man route](https://man.openbsd.org/route) — маршрутизация
- [OpenBSD FAQ 6](https://www.openbsd.org/faq/faq6.html) — сетевая настройка

---

