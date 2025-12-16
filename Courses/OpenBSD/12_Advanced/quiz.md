# Advanced Topics - Quiz

Проверьте свои знания по продвинутым темам OpenBSD.

---

## Question 1: vmm

Как называется гипервизор в OpenBSD?

A) vmm

B) xen

C) bhyve

D) KVM

---

## Question 2: vmd

Какая команда управляет виртуальными машинами?

A) virsh

B) vm

C) vbox

D) vmctl

---

## Question 3: Создание VM диска

Какая команда создаёт диск для виртуальной машины?

A) qemu-img create disk.qcow2

B) vmctl create -s 10G disk.qcow2

C) vmctl disk create

D) dd if=/dev/zero of=disk.qcow2

---

## Question 4: CARP

Для чего используется CARP?

A) Логирование

B) Шифрование трафика

C) Отказоустойчивость (failover)

D) Сжатие данных

---

## Question 5: CARP параметр

Что определяет параметр advskew в CARP?

A) Интервал проверки

B) Приоритет (меньше = выше приоритет)

C) Размер пакета

D) Скорость интерфейса

---

## Question 6: pfsync

Для чего используется pfsync?

A) Резервное копирование

B) Мониторинг

C) Синхронизация состояний PF между нодами

D) Синхронизация файлов

---

## Question 7: Сборка ядра

Где находятся исходники ядра?

A) /usr/src/sys

B) /opt/kernel

C) /var/src/kern

D) /usr/src/kernel

---

## Question 8: Конфигурация ядра

Где находятся файлы конфигурации ядра для amd64?

A) /boot/kernel.conf

B) /usr/src/conf/amd64

C) /etc/kernel.conf

D) /usr/src/sys/arch/amd64/conf

---

## Question 9: IP forwarding

Какой sysctl включает пересылку IP пакетов?

A) ip.forward.enable

B) net.ipv4.ip_forward

C) net.inet.ip.forwarding

D) net.core.forwarding

---

## Question 10: WireGuard

Какой интерфейс создаётся для WireGuard?

A) vpn0

B) wg0

C) tun0

D) wire0

---

## Question 11: WireGuard порт

Какой UDP порт использует WireGuard по умолчанию?

A) 443

B) 500

C) 51820

D) 1194

---

## Question 12: Подключение к консоли VM

Какая команда подключает к консоли виртуальной машины?

A) vmctl connect vmname

B) vmctl tty vmname

C) vmctl console vmname

D) vmctl attach vmname

---

## Question 13: Откат ядра

Как загрузить старое ядро?

A) boot /obsd

B) boot /kernel.old

C) boot /bsd.old

D) boot -o

---

## Question 14: ktrace

Для чего используется ktrace?

A) Трассировка маршрутов

B) Трассировка сетевого трафика

C) Трассировка системных вызовов

D) Трассировка файловой системы

---

## Question 15: DHCP для роутера

Какой флаг указывает интерфейс для dhcpd?

A) rcctl set dhcpd listen em1

B) rcctl set dhcpd flags em1

C) rcctl set dhcpd interface em1

D) rcctl set dhcpd -i em1

---

## Question 16: vmd

Какой демон управляет виртуальными машинами?

A) qemu

B) vmm

C) libvirt

D) vmd

---

## Question 17: vio

Что такое vio в контексте vmm?

A) Виртуальная консоль

B) Виртуальный порт

C) Виртуальный диск

D) Виртуальный сетевой интерфейс

---

## Question 18: rdsetroot

Для чего используется rdsetroot?

A) Для настройки root раздела

B) Для создания RAID

C) Для встраивания ramdisk в ядро

D) Для настройки DNS

---

## Question 19: make build

Что делает make build в /usr/src?

A) Компилирует систему из исходников

B) Создаёт билд-сервер

C) Обновляет порты

D) Собирает пакеты

---

## Question 20: releng

Что такое release engineering в контексте OpenBSD?

A) Процесс создания официальных релизов системы

B) Система мониторинга

C) Модуль ядра

D) Инженерное ПО

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | vmm (Virtual Machine Monitor) — гипервизор в ядре OpenBSD |
| 2 | D | vmctl — утилита для управления виртуальными машинами |
| 3 | B | vmctl create -s SIZE FILE создаёт диск для VM |
| 4 | C | CARP обеспечивает отказоустойчивость через виртуальный IP |
| 5 | B | advskew определяет приоритет: 0 = master, 100 = backup |
| 6 | C | pfsync синхронизирует таблицы состояний PF между нодами |
| 7 | A | /usr/src/sys содержит исходники ядра |
| 8 | D | Конфигурации ядра в /usr/src/sys/arch/ARCH/conf |
| 9 | C | net.inet.ip.forwarding=1 включает IP forwarding |
| 10 | B | wg0 — имя WireGuard интерфейса |
| 11 | C | WireGuard по умолчанию использует UDP порт 51820 |
| 12 | C | vmctl console vmname подключает к консоли VM |
| 13 | A | boot /obsd загружает предыдущее ядро (original bsd) |
| 14 | C | ktrace трассирует системные вызовы процесса |
| 15 | B | rcctl set dhcpd flags em1 указывает интерфейс |
| 16 | D | vmd — демон, управляющий виртуальными машинами |
| 17 | D | vio — виртуальный сетевой интерфейс для VM |
| 18 | C | rdsetroot встраивает ramdisk образ в ядро |
| 19 | A | make build компилирует систему из исходников |
| 20 | A | release engineering — процесс создания официальных релизов |

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

