# Advanced Topics - Quiz

Проверьте свои знания по продвинутым темам OpenBSD.

---

## Question 1: vmm


Как называется гипервизор в OpenBSD?

A) vmm

B) bhyve

C) xen

D) KVM

---

## Question 2: vmd


Какая команда управляет виртуальными машинами?

A) vmctl

B) virsh

C) vm

D) vbox

---

## Question 3: Создание VM диска


Какая команда создаёт диск для виртуальной машины?

A) vmctl create -s 10G disk.qcow2

B) dd if=/dev/zero of=disk.qcow2

C) vmctl disk create

D) qemu-img create disk.qcow2

---

## Question 4: CARP


Для чего используется CARP?

A) Логирование

B) Шифрование трафика

C) Сжатие данных

D) Отказоустойчивость (failover)

---

## Question 5: CARP параметр


Что определяет параметр advskew в CARP?

A) Интервал проверки

B) Размер пакета

C) Приоритет (меньше = выше приоритет)

D) Скорость интерфейса

---

## Question 6: pfsync


Для чего используется pfsync?

A) Синхронизация состояний PF между нодами

B) Резервное копирование

C) Мониторинг

D) Синхронизация файлов

---

## Question 7: Сборка ядра


Где находятся исходники ядра?

A) /usr/src/kernel

B) /opt/kernel

C) /usr/src/sys

D) /var/src/kern

---

## Question 8: Конфигурация ядра


Где находятся файлы конфигурации ядра для amd64?

A) /boot/kernel.conf

B) /etc/kernel.conf

C) /usr/src/sys/arch/amd64/conf

D) /usr/src/conf/amd64

---

## Question 9: IP forwarding


Какой sysctl включает пересылку IP пакетов?

A) net.inet.ip.forwarding

B) ip.forward.enable

C) net.core.forwarding

D) net.ipv4.ip_forward

---

## Question 10: WireGuard


Какой интерфейс создаётся для WireGuard?

A) wire0

B) tun0

C) wg0

D) vpn0

---

## Question 11: WireGuard порт


Какой UDP порт использует WireGuard по умолчанию?

A) 443

B) 500

C) 1194

D) 51820

---

## Question 12: Подключение к консоли VM


Какая команда подключает к консоли виртуальной машины?

A) vmctl tty vmname

B) vmctl attach vmname

C) vmctl connect vmname

D) vmctl console vmname

---

## Question 13: Откат ядра


Как загрузить старое ядро?

A) boot /bsd.old

B) boot /kernel.old

C) boot /obsd

D) boot -o

---

## Question 14: ktrace


Для чего используется ktrace?

A) Трассировка файловой системы

B) Трассировка системных вызовов

C) Трассировка сетевого трафика

D) Трассировка маршрутов

---

## Question 15: DHCP для роутера


Какой флаг указывает интерфейс для dhcpd?

A) rcctl set dhcpd flags em1

B) rcctl set dhcpd -i em1

C) rcctl set dhcpd listen em1

D) rcctl set dhcpd interface em1

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | vmm (Virtual Machine Monitor) — гипервизор в ядре OpenBSD |
| 2 | A | vmctl — утилита для управления виртуальными машинами |
| 3 | A | vmctl create -s SIZE FILE создаёт диск для VM |
| 4 | D | CARP обеспечивает отказоустойчивость через виртуальный IP |
| 5 | C | advskew определяет приоритет: 0 = master, 100 = backup |
| 6 | A | pfsync синхронизирует таблицы состояний PF между нодами |
| 7 | C | /usr/src/sys содержит исходники ядра |
| 8 | C | Конфигурации ядра в /usr/src/sys/arch/ARCH/conf |
| 9 | A | net.inet.ip.forwarding=1 включает IP forwarding |
| 10 | C | wg0 — имя WireGuard интерфейса |
| 11 | D | WireGuard по умолчанию использует UDP порт 51820 |
| 12 | D | vmctl console vmname подключает к консоли VM |
| 13 | C | boot /obsd загружает предыдущее ядро (original bsd) |
| 14 | B | ktrace трассирует системные вызовы процесса |
| 15 | A | rcctl set dhcpd flags em1 указывает интерфейс |

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

