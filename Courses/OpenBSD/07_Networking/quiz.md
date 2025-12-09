# Networking - Quiz

Проверьте свои знания по сетевой настройке OpenBSD.

---

## Question 1: Конфигурация интерфейса


В каком файле настраивается интерфейс em0?

A) /etc/hostname.em0

B) /etc/network/interfaces

C) /etc/sysconfig/network-scripts/ifcfg-em0

D) /etc/conf.d/net

---

## Question 2: DHCP


Что нужно написать в hostname.if для получения адреса по DHCP?

A) bootp

B) auto

C) dynamic

D) dhcp

---

## Question 3: Шлюз по умолчанию


В каком файле указывается шлюз по умолчанию?

A) /etc/sysconfig/network

B) /etc/mygate

C) /etc/gateway

D) /etc/default/route

---

## Question 4: Имя хоста


В каком файле хранится имя хоста системы?

A) /etc/sysconfig/network

B) /etc/HOSTNAME

C) /etc/myname

D) /etc/hostname

---

## Question 5: Просмотр интерфейсов


Какая команда показывает конфигурацию сетевых интерфейсов?

A) ipconfig

B) netstat -i

C) ifconfig

D) ip addr

---

## Question 6: Таблица маршрутизации


Какая команда показывает таблицу маршрутизации?

A) B верно

B) route -n

C) ip route

D) netstat -rn

---

## Question 7: IP forwarding


Какой параметр sysctl включает пересылку IP пакетов?

A) net.inet.ip.forwarding

B) net.core.forwarding

C) net.ipv4.ip_forward

D) kernel.ip_forward

---

## Question 8: WiFi подключение


Какая директива используется для подключения к WiFi с WPA2?

A) wpa_supplicant

B) connect wpa2

C) join "SSID" wpakey "password"

D) wifi connect

---

## Question 9: VLAN


Какой параметр задаёт номер VLAN?

A) vnetid

B) vid

C) vlan_id

D) tag

---

## Question 10: DNS серверы


В каком файле настраиваются DNS серверы?

A) /etc/resolv.conf

B) /etc/dns.conf

C) /etc/named.conf

D) /etc/nameservers

---

## Question 11: Применение настроек


Какая команда применяет сетевую конфигурацию?

A) /etc/init.d/networking restart

B) systemctl restart network

C) service network restart

D) sh /etc/netstart

---

## Question 12: Захват трафика


Какая утилита используется для захвата сетевого трафика?

A) tcpdump

B) snoop

C) tshark

D) wireshark

---

## Question 13: Группа egress


Что означает группа интерфейсов "egress"?

A) Интерфейс для исходящего трафика по умолчанию

B) Виртуальный интерфейс

C) Интерфейс в состоянии ошибки

D) Отключённый интерфейс

---

## Question 14: Trunk (агрегация)


Какой протокол используется для агрегации каналов по стандарту 802.3ad?

A) lacp

B) failover

C) bonding

D) balance

---

## Question 15: Проверка порта


Какая команда проверяет доступность порта на удалённом хосте?

A) A и B верны

B) nc -vz host port

C) telnet host port

D) ping host:port

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | /etc/hostname.em0 — файл конфигурации интерфейса em0 |
| 2 | D | Простое слово "dhcp" включает получение адреса по DHCP |
| 3 | B | /etc/mygate содержит IP адрес шлюза по умолчанию |
| 4 | C | /etc/myname содержит полное имя хоста (FQDN) |
| 5 | C | ifconfig — стандартная команда для просмотра интерфейсов в BSD |
| 6 | D | netstat -rn показывает таблицу маршрутизации в числовом формате |
| 7 | A | net.inet.ip.forwarding=1 включает IP forwarding в OpenBSD |
| 8 | C | join "SSID" wpakey "password" — синтаксис WiFi в hostname.if |
| 9 | A | vnetid задаёт номер VLAN для интерфейса |
| 10 | A | /etc/resolv.conf — стандартный файл для DNS настроек |
| 11 | D | sh /etc/netstart применяет сетевую конфигурацию |
| 12 | A | tcpdump — встроенная утилита для захвата трафика в OpenBSD |
| 13 | A | egress — группа интерфейсов для исходящего трафика по умолчанию |
| 14 | A | lacp (Link Aggregation Control Protocol) — стандарт 802.3ad |
| 15 | A | И telnet, и nc -vz могут проверить доступность порта |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы хорошо понимаете сетевую настройку OpenBSD. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите VLAN и агрегацию каналов. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Попрактикуйтесь с hostname.if и netstat. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите man hostname.if и FAQ 6. |

---

