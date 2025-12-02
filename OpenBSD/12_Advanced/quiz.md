# Advanced Topics - Quiz

Проверьте свои знания по продвинутым темам OpenBSD.

---

## Question 1: vmm

Как называется гипервизор в OpenBSD?

A) KVM

B) bhyve

C) vmm

D) xen

---

## Question 2: vmd

Какая команда управляет виртуальными машинами?

A) vm

B) vmctl

C) virsh

D) vbox

---

## Question 3: Создание VM диска

Какая команда создаёт диск для виртуальной машины?

A) vmctl disk create

B) vmctl create -s 10G disk.qcow2

C) qemu-img create disk.qcow2

D) dd if=/dev/zero of=disk.qcow2

---

## Question 4: CARP

Для чего используется CARP?

A) Шифрование трафика

B) Отказоустойчивость (failover)

C) Сжатие данных

D) Логирование

---

## Question 5: CARP параметр

Что определяет параметр advskew в CARP?

A) Скорость интерфейса

B) Приоритет (меньше = выше приоритет)

C) Интервал проверки

D) Размер пакета

---

## Question 6: pfsync

Для чего используется pfsync?

A) Синхронизация файлов

B) Синхронизация состояний PF между нодами

C) Резервное копирование

D) Мониторинг

---

## Question 7: Сборка ядра

Где находятся исходники ядра?

A) /usr/src/kernel

B) /usr/src/sys

C) /var/src/kern

D) /opt/kernel

---

## Question 8: Конфигурация ядра

Где находятся файлы конфигурации ядра для amd64?

A) /etc/kernel.conf

B) /usr/src/sys/arch/amd64/conf

C) /boot/kernel.conf

D) /usr/src/conf/amd64

---

## Question 9: IP forwarding

Какой sysctl включает пересылку IP пакетов?

A) net.ipv4.ip_forward

B) net.inet.ip.forwarding

C) net.core.forwarding

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

A) 443

B) 1194

C) 51820

D) 500

---

## Question 12: Подключение к консоли VM

Какая команда подключает к консоли виртуальной машины?

A) vmctl attach vmname

B) vmctl console vmname

C) vmctl connect vmname

D) vmctl tty vmname

---

## Question 13: Откат ядра

Как загрузить старое ядро?

A) boot /kernel.old

B) boot /obsd

C) boot /bsd.old

D) boot -o

---

## Question 14: ktrace

Для чего используется ktrace?

A) Трассировка сетевого трафика

B) Трассировка системных вызовов

C) Трассировка маршрутов

D) Трассировка файловой системы

---

## Question 15: DHCP для роутера

Какой флаг указывает интерфейс для dhcpd?

A) rcctl set dhcpd interface em1

B) rcctl set dhcpd flags em1

C) rcctl set dhcpd listen em1

D) rcctl set dhcpd -i em1

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | vmm (Virtual Machine Monitor) — гипервизор в ядре OpenBSD |
| 2 | B | vmctl — утилита для управления виртуальными машинами |
| 3 | B | vmctl create -s SIZE FILE создаёт диск для VM |
| 4 | B | CARP обеспечивает отказоустойчивость через виртуальный IP |
| 5 | B | advskew определяет приоритет: 0 = master, 100 = backup |
| 6 | B | pfsync синхронизирует таблицы состояний PF между нодами |
| 7 | B | /usr/src/sys содержит исходники ядра |
| 8 | B | Конфигурации ядра в /usr/src/sys/arch/ARCH/conf |
| 9 | B | net.inet.ip.forwarding=1 включает IP forwarding |
| 10 | C | wg0 — имя WireGuard интерфейса |
| 11 | C | WireGuard по умолчанию использует UDP порт 51820 |
| 12 | B | vmctl console vmname подключает к консоли VM |
| 13 | B | boot /obsd загружает предыдущее ядро (original bsd) |
| 14 | B | ktrace трассирует системные вызовы процесса |
| 15 | B | rcctl set dhcpd flags em1 указывает интерфейс |

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

