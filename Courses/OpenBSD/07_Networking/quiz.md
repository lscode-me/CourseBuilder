# Networking - Quiz

Проверьте свои знания по сетевой настройке OpenBSD.

---

## Question 1: Конфигурация интерфейса

В каком файле настраивается интерфейс em0?

A) /etc/hostname.em0

B) /etc/sysconfig/network-scripts/ifcfg-em0

C) /etc/network/interfaces

D) /etc/conf.d/net

---

## Question 2: DHCP

Что нужно написать в hostname.if для получения адреса по DHCP?

A) dynamic

B) bootp

C) dhcp

D) auto

---

## Question 3: Шлюз по умолчанию

В каком файле указывается шлюз по умолчанию?

A) /etc/mygate

B) /etc/sysconfig/network

C) /etc/default/route

D) /etc/gateway

---

## Question 4: Имя хоста

В каком файле хранится имя хоста системы?

A) /etc/myname

B) /etc/HOSTNAME

C) /etc/hostname

D) /etc/sysconfig/network

---

## Question 5: Просмотр интерфейсов

Какая команда показывает конфигурацию сетевых интерфейсов?

A) ifconfig

B) netstat -i

C) ipconfig

D) ip addr

---

## Question 6: Таблица маршрутизации

Какая команда показывает таблицу маршрутизации?

A) route -n

B) netstat -rn

C) B верно

D) ip route

---

## Question 7: IP forwarding

Какой параметр sysctl включает пересылку IP пакетов?

A) net.inet.ip.forwarding

B) kernel.ip_forward

C) net.ipv4.ip_forward

D) net.core.forwarding

---

## Question 8: WiFi подключение

Какая директива используется для подключения к WiFi с WPA2?

A) wpa_supplicant

B) join "SSID" wpakey "password"

C) wifi connect

D) connect wpa2

---

## Question 9: VLAN

Какой параметр задаёт номер VLAN?

A) vid

B) tag

C) vlan_id

D) vnetid

---

## Question 10: DNS серверы

В каком файле настраиваются DNS серверы?

A) /etc/nameservers

B) /etc/resolv.conf

C) /etc/dns.conf

D) /etc/named.conf

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

A) snoop

B) wireshark

C) tcpdump

D) tshark

---

## Question 13: Группа egress

Что означает группа интерфейсов "egress"?

A) Интерфейс для исходящего трафика по умолчанию

B) Интерфейс в состоянии ошибки

C) Виртуальный интерфейс

D) Отключённый интерфейс

---

## Question 14: Trunk (агрегация)

Какой протокол используется для агрегации каналов по стандарту 802.3ad?

A) failover

B) balance

C) bonding

D) lacp

---

## Question 15: Проверка порта

Какая команда проверяет доступность порта на удалённом хосте?

A) ping host:port

B) A и B верны

C) nc -vz host port

D) telnet host port

---

## Question 16: route

Как добавить статический маршрут?

A) netstat -add

B) route add destination gateway

C) ip route add

D) routing add

---

## Question 17: ping6

Для чего используется ping6?

A) Для 6 пакетов ping

B) Для ping версии 6

C) Для ping на порт 6

D) Для тестирования IPv6 соединения

---

## Question 18: hostname.carp0

Для чего используется CARP в OpenBSD?

A) Для VPN

B) Для шифрования трафика

C) Для отказоустойчивости сетевых сервисов

D) Для балансировки нагрузки

---

## Question 19: ifconfig down

Что делает ifconfig em0 down?

A) Перезагружает интерфейс

B) Очищает статистику

C) Отключает интерфейс

D) Удаляет интерфейс

---

## Question 20: /etc/hosts

Для чего используется /etc/hosts?

A) Для firewall правил

B) Для списка хостов в сети

C) Для локального разрешения имён в IP-адреса

D) Для настройки DHCP

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | /etc/hostname.em0 — файл конфигурации интерфейса em0 |
| 2 | C | Простое слово "dhcp" включает получение адреса по DHCP |
| 3 | A | /etc/mygate содержит IP адрес шлюза по умолчанию |
| 4 | A | /etc/myname содержит полное имя хоста (FQDN) |
| 5 | A | ifconfig — стандартная команда для просмотра интерфейсов в BSD |
| 6 | B | netstat -rn показывает таблицу маршрутизации в числовом формате |
| 7 | A | net.inet.ip.forwarding=1 включает IP forwarding в OpenBSD |
| 8 | B | join "SSID" wpakey "password" — синтаксис WiFi в hostname.if |
| 9 | D | vnetid задаёт номер VLAN для интерфейса |
| 10 | B | /etc/resolv.conf — стандартный файл для DNS настроек |
| 11 | D | sh /etc/netstart применяет сетевую конфигурацию |
| 12 | C | tcpdump — встроенная утилита для захвата трафика в OpenBSD |
| 13 | A | egress — группа интерфейсов для исходящего трафика по умолчанию |
| 14 | D | lacp (Link Aggregation Control Protocol) — стандарт 802.3ad |
| 15 | B | И telnet, и nc -vz могут проверить доступность порта |
| 16 | B | route add destination gateway — синтаксис добавления маршрута |
| 17 | D | ping6 используется для тестирования IPv6 соединений |
| 18 | C | CARP обеспечивает отказоустойчивость сетевых сервисов |
| 19 | C | ifconfig em0 down отключает (деактивирует) интерфейс |
| 20 | C | /etc/hosts — локальное разрешение имён хостов в IP |

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

