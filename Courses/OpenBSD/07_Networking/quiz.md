# Networking - Quiz

Проверьте свои знания по сетевой настройке OpenBSD.

---

## Question 1: Конфигурация интерфейса





В каком файле настраивается интерфейс em0?

A) /etc/conf.d/net

B) /etc/sysconfig/network-scripts/ifcfg-em0

C) /etc/hostname.em0

D) /etc/network/interfaces

---

## Question 2: DHCP





Что нужно написать в hostname.if для получения адреса по DHCP?

A) auto

B) bootp

C) dhcp

D) dynamic

---

## Question 3: Шлюз по умолчанию





В каком файле указывается шлюз по умолчанию?

A) /etc/gateway

B) /etc/sysconfig/network

C) /etc/default/route

D) /etc/mygate

---

## Question 4: Имя хоста





В каком файле хранится имя хоста системы?

A) /etc/myname

B) /etc/hostname

C) /etc/sysconfig/network

D) /etc/HOSTNAME

---

## Question 5: Просмотр интерфейсов





Какая команда показывает конфигурацию сетевых интерфейсов?

A) ip addr

B) netstat -i

C) ifconfig

D) ipconfig

---

## Question 6: Таблица маршрутизации





Какая команда показывает таблицу маршрутизации?

A) ip route

B) netstat -rn

C) route -n

D) B верно

---

## Question 7: IP forwarding





Какой параметр sysctl включает пересылку IP пакетов?

A) kernel.ip_forward

B) net.core.forwarding

C) net.ipv4.ip_forward

D) net.inet.ip.forwarding

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

A) vlan_id

B) tag

C) vid

D) vnetid

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

A) /etc/init.d/networking restart

B) service network restart

C) sh /etc/netstart

D) systemctl restart network

---

## Question 12: Захват трафика





Какая утилита используется для захвата сетевого трафика?

A) tshark

B) snoop

C) wireshark

D) tcpdump

---

## Question 13: Группа egress





Что означает группа интерфейсов "egress"?

A) Виртуальный интерфейс

B) Интерфейс для исходящего трафика по умолчанию

C) Отключённый интерфейс

D) Интерфейс в состоянии ошибки

---

## Question 14: Trunk (агрегация)





Какой протокол используется для агрегации каналов по стандарту 802.3ad?

A) balance

B) lacp

C) failover

D) bonding

---

## Question 15: Проверка порта





Какая команда проверяет доступность порта на удалённом хосте?

A) telnet host port

B) ping host:port

C) A и B верны

D) nc -vz host port

---

## Question 16: route




Как добавить статический маршрут?

A) routing add

B) netstat -add

C) ip route add

D) route add destination gateway

---

## Question 17: ping6




Для чего используется ping6?

A) Для ping на порт 6

B) Для 6 пакетов ping

C) Для тестирования IPv6 соединения

D) Для ping версии 6

---

## Question 18: hostname.carp0




Для чего используется CARP в OpenBSD?

A) Для балансировки нагрузки

B) Для шифрования трафика

C) Для VPN

D) Для отказоустойчивости сетевых сервисов

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

A) Для локального разрешения имён в IP-адреса

B) Для firewall правил

C) Для настройки DHCP

D) Для списка хостов в сети

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | /etc/hostname.em0 — файл конфигурации интерфейса em0 |
| 2 | C | Простое слово "dhcp" включает получение адреса по DHCP |
| 3 | D | /etc/mygate содержит IP адрес шлюза по умолчанию |
| 4 | A | /etc/myname содержит полное имя хоста (FQDN) |
| 5 | C | ifconfig — стандартная команда для просмотра интерфейсов в BSD |
| 6 | B | netstat -rn показывает таблицу маршрутизации в числовом формате |
| 7 | D | net.inet.ip.forwarding=1 включает IP forwarding в OpenBSD |
| 8 | C | join "SSID" wpakey "password" — синтаксис WiFi в hostname.if |
| 9 | D | vnetid задаёт номер VLAN для интерфейса |
| 10 | B | /etc/resolv.conf — стандартный файл для DNS настроек |
| 11 | C | sh /etc/netstart применяет сетевую конфигурацию |
| 12 | D | tcpdump — встроенная утилита для захвата трафика в OpenBSD |
| 13 | B | egress — группа интерфейсов для исходящего трафика по умолчанию |
| 14 | B | lacp (Link Aggregation Control Protocol) — стандарт 802.3ad |
| 15 | C | И telnet, и nc -vz могут проверить доступность порта |
| 16 | D | route add destination gateway — синтаксис добавления маршрута |
| 17 | C | ping6 используется для тестирования IPv6 соединений |
| 18 | D | CARP обеспечивает отказоустойчивость сетевых сервисов |
| 19 | C | ifconfig em0 down отключает (деактивирует) интерфейс |
| 20 | A | /etc/hosts — локальное разрешение имён хостов в IP |

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

