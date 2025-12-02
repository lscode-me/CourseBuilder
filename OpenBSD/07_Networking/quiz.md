# Networking - Quiz

Проверьте свои знания по сетевой настройке OpenBSD.

---

## Question 1: Конфигурация интерфейса

В каком файле настраивается интерфейс em0?

A) /etc/network/interfaces

B) /etc/hostname.em0

C) /etc/sysconfig/network-scripts/ifcfg-em0

D) /etc/conf.d/net

---

## Question 2: DHCP

Что нужно написать в hostname.if для получения адреса по DHCP?

A) auto

B) dynamic

C) dhcp

D) bootp

---

## Question 3: Шлюз по умолчанию

В каком файле указывается шлюз по умолчанию?

A) /etc/gateway

B) /etc/mygate

C) /etc/default/route

D) /etc/sysconfig/network

---

## Question 4: Имя хоста

В каком файле хранится имя хоста системы?

A) /etc/hostname

B) /etc/myname

C) /etc/HOSTNAME

D) /etc/sysconfig/network

---

## Question 5: Просмотр интерфейсов

Какая команда показывает конфигурацию сетевых интерфейсов?

A) ip addr

B) ipconfig

C) ifconfig

D) netstat -i

---

## Question 6: Таблица маршрутизации

Какая команда показывает таблицу маршрутизации?

A) route -n

B) netstat -rn

C) ip route

D) B верно

---

## Question 7: IP forwarding

Какой параметр sysctl включает пересылку IP пакетов?

A) net.ipv4.ip_forward

B) net.inet.ip.forwarding

C) net.core.forwarding

D) kernel.ip_forward

---

## Question 8: WiFi подключение

Какая директива используется для подключения к WiFi с WPA2?

A) wpa_supplicant

B) wifi connect

C) join "SSID" wpakey "password"

D) connect wpa2

---

## Question 9: VLAN

Какой параметр задаёт номер VLAN?

A) vlan_id

B) vnetid

C) tag

D) vid

---

## Question 10: DNS серверы

В каком файле настраиваются DNS серверы?

A) /etc/named.conf

B) /etc/resolv.conf

C) /etc/dns.conf

D) /etc/nameservers

---

## Question 11: Применение настроек

Какая команда применяет сетевую конфигурацию?

A) systemctl restart network

B) service network restart

C) sh /etc/netstart

D) /etc/init.d/networking restart

---

## Question 12: Захват трафика

Какая утилита используется для захвата сетевого трафика?

A) wireshark

B) tcpdump

C) tshark

D) snoop

---

## Question 13: Группа egress

Что означает группа интерфейсов "egress"?

A) Интерфейс для исходящего трафика по умолчанию

B) Интерфейс в состоянии ошибки

C) Отключённый интерфейс

D) Виртуальный интерфейс

---

## Question 14: Trunk (агрегация)

Какой протокол используется для агрегации каналов по стандарту 802.3ad?

A) bonding

B) lacp

C) failover

D) balance

---

## Question 15: Проверка порта

Какая команда проверяет доступность порта на удалённом хосте?

A) telnet host port

B) nc -vz host port

C) ping host:port

D) A и B верны

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | /etc/hostname.em0 — файл конфигурации интерфейса em0 |
| 2 | C | Простое слово "dhcp" включает получение адреса по DHCP |
| 3 | B | /etc/mygate содержит IP адрес шлюза по умолчанию |
| 4 | B | /etc/myname содержит полное имя хоста (FQDN) |
| 5 | C | ifconfig — стандартная команда для просмотра интерфейсов в BSD |
| 6 | B | netstat -rn показывает таблицу маршрутизации в числовом формате |
| 7 | B | net.inet.ip.forwarding=1 включает IP forwarding в OpenBSD |
| 8 | C | join "SSID" wpakey "password" — синтаксис WiFi в hostname.if |
| 9 | B | vnetid задаёт номер VLAN для интерфейса |
| 10 | B | /etc/resolv.conf — стандартный файл для DNS настроек |
| 11 | C | sh /etc/netstart применяет сетевую конфигурацию |
| 12 | B | tcpdump — встроенная утилита для захвата трафика в OpenBSD |
| 13 | A | egress — группа интерфейсов для исходящего трафика по умолчанию |
| 14 | B | lacp (Link Aggregation Control Protocol) — стандарт 802.3ad |
| 15 | D | И telnet, и nc -vz могут проверить доступность порта |

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

