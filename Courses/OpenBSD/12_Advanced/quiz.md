# Advanced Topics - Quiz

Проверьте свои знания по продвинутым темам OpenBSD.

---

## Question 1: vmm





Как называется гипервизор в OpenBSD?

A) xen

B) KVM

C) bhyve

D) vmm

---

## Question 2: vmd





Какая команда управляет виртуальными машинами?

A) vbox

B) vm

C) vmctl

D) virsh

---

## Question 3: Создание VM диска





Какая команда создаёт диск для виртуальной машины?

A) dd if=/dev/zero of=disk.qcow2

B) vmctl create -s 10G disk.qcow2

C) vmctl disk create

D) qemu-img create disk.qcow2

---

## Question 4: CARP





Для чего используется CARP?

A) Сжатие данных

B) Логирование

C) Отказоустойчивость (failover)

D) Шифрование трафика

---

## Question 5: CARP параметр





Что определяет параметр advskew в CARP?

A) Скорость интерфейса

B) Приоритет (меньше = выше приоритет)

C) Размер пакета

D) Интервал проверки

---

## Question 6: pfsync





Для чего используется pfsync?

A) Синхронизация файлов

B) Синхронизация состояний PF между нодами

C) Мониторинг

D) Резервное копирование

---

## Question 7: Сборка ядра





Где находятся исходники ядра?

A) /opt/kernel

B) /usr/src/kernel

C) /usr/src/sys

D) /var/src/kern

---

## Question 8: Конфигурация ядра





Где находятся файлы конфигурации ядра для amd64?

A) /usr/src/conf/amd64

B) /etc/kernel.conf

C) /usr/src/sys/arch/amd64/conf

D) /boot/kernel.conf

---

## Question 9: IP forwarding





Какой sysctl включает пересылку IP пакетов?

A) net.core.forwarding

B) net.ipv4.ip_forward

C) net.inet.ip.forwarding

D) ip.forward.enable

---

## Question 10: WireGuard





Какой интерфейс создаётся для WireGuard?

A) vpn0

B) tun0

C) wg0

D) wire0

---

## Question 11: WireGuard порт





Какой UDP порт использует WireGuard по умолчанию?

A) 51820

B) 1194

C) 500

D) 443

---

## Question 12: Подключение к консоли VM





Какая команда подключает к консоли виртуальной машины?

A) vmctl tty vmname

B) vmctl console vmname

C) vmctl connect vmname

D) vmctl attach vmname

---

## Question 13: Откат ядра





Как загрузить старое ядро?

A) boot /bsd.old

B) boot /obsd

C) boot /kernel.old

D) boot -o

---

## Question 14: ktrace





Для чего используется ktrace?

A) Трассировка файловой системы

B) Трассировка сетевого трафика

C) Трассировка системных вызовов

D) Трассировка маршрутов

---

## Question 15: DHCP для роутера





Какой флаг указывает интерфейс для dhcpd?

A) rcctl set dhcpd interface em1

B) rcctl set dhcpd -i em1

C) rcctl set dhcpd flags em1

D) rcctl set dhcpd listen em1

---

## Question 16: vmd




Какой демон управляет виртуальными машинами?

A) qemu

B) vmd

C) vmm

D) libvirt

---

## Question 17: vio




Что такое vio в контексте vmm?

A) Виртуальный порт

B) Виртуальный сетевой интерфейс

C) Виртуальная консоль

D) Виртуальный диск

---

## Question 18: rdsetroot




Для чего используется rdsetroot?

A) Для настройки DNS

B) Для создания RAID

C) Для настройки root раздела

D) Для встраивания ramdisk в ядро

---

## Question 19: make build




Что делает make build в /usr/src?

A) Обновляет порты

B) Собирает пакеты

C) Создаёт билд-сервер

D) Компилирует систему из исходников

---

## Question 20: releng




Что такое release engineering в контексте OpenBSD?

A) Модуль ядра

B) Инженерное ПО

C) Система мониторинга

D) Процесс создания официальных релизов системы

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | vmm (Virtual Machine Monitor) — гипервизор в ядре OpenBSD |
| 2 | C | vmctl — утилита для управления виртуальными машинами |
| 3 | B | vmctl create -s SIZE FILE создаёт диск для VM |
| 4 | C | CARP обеспечивает отказоустойчивость через виртуальный IP |
| 5 | B | advskew определяет приоритет: 0 = master, 100 = backup |
| 6 | B | pfsync синхронизирует таблицы состояний PF между нодами |
| 7 | C | /usr/src/sys содержит исходники ядра |
| 8 | C | Конфигурации ядра в /usr/src/sys/arch/ARCH/conf |
| 9 | C | net.inet.ip.forwarding=1 включает IP forwarding |
| 10 | C | wg0 — имя WireGuard интерфейса |
| 11 | A | WireGuard по умолчанию использует UDP порт 51820 |
| 12 | B | vmctl console vmname подключает к консоли VM |
| 13 | B | boot /obsd загружает предыдущее ядро (original bsd) |
| 14 | C | ktrace трассирует системные вызовы процесса |
| 15 | C | rcctl set dhcpd flags em1 указывает интерфейс |
| 16 | B | vmd — демон, управляющий виртуальными машинами |
| 17 | B | vio — виртуальный сетевой интерфейс для VM |
| 18 | D | rdsetroot встраивает ramdisk образ в ядро |
| 19 | D | make build компилирует систему из исходников |
| 20 | D | release engineering — процесс создания официальных релизов |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы готовы к продвинутым задачам. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите vmm/vmd и CARP. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется практика с виртуализацией. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите man vmctl и man carp. |

---

## 🎓 Поздравляем с завершением курса!

Вы прошли все 12 модулей курса OpenBSD. Продолжайте практиковаться и экспериментировать!

---

