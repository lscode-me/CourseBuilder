# Advanced Topics
## Продвинутые темы: виртуализация, обновления, кастомное ядро

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти все предыдущие модули курса
- Иметь опыт администрирования OpenBSD
- Понимать работу ядра и системы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Настраивать виртуализацию с vmm/vmd
- Создавать и управлять виртуальными машинами
- Собирать кастомное ядро
- Настраивать CARP для отказоустойчивости
- Использовать OpenBSD как роутер

---

## 1. Виртуализация vmm/vmd

### 1.1 Что такое vmm/vmd

**vmm** (Virtual Machine Monitor) — гипервизор в ядре OpenBSD.
**vmd** — демон управления виртуальными машинами.

```sh
# Проверить поддержку виртуализации
$ dmesg | grep vmm
vmm0 at mainbus0: VMX/EPT

# Если нет — возможно нужно включить в BIOS
```

### 1.2 Настройка vmd

```sh
# Включить vmd
# doas rcctl enable vmd
# doas rcctl start vmd

# Конфигурация: /etc/vm.conf
```

### 1.3 Создание виртуальной машины

```sh
# Создать диск для VM
# doas vmctl create -s 10G /var/vm/linux.qcow2

# Скачать образ для установки
$ ftp https://cdn.openbsd.org/pub/OpenBSD/7.4/amd64/install74.iso
# doas mv install74.iso /var/vm/

# Конфигурация VM
# doas vi /etc/vm.conf
```

```sh
# /etc/vm.conf
switch "local" {
    interface bridge0
}

vm "openbsd-vm" {
    memory 1G
    disk /var/vm/openbsd.qcow2
    cdrom /var/vm/install74.iso
    interface { switch "local" }
    owner admin
    disable
}

```

### 1.4 Управление VM

```sh
# Перезагрузить конфигурацию
# doas vmctl reload

# Запустить VM
# doas vmctl start openbsd-vm

# Подключиться к консоли
# doas vmctl console openbsd-vm

# Остановить VM
# doas vmctl stop openbsd-vm

# Принудительная остановка
# doas vmctl stop -f openbsd-vm

# Статус всех VM
$ vmctl status
   ID   PID VCPUS  MAXMEM  CURMEM     TTY        OWNER    NAME
    1  1234     1    1.0G    256M   ttyp0        admin    openbsd-vm

```

### 1.5 Сеть для VM

```sh
# Создать bridge
# doas ifconfig bridge0 create
# echo "up" | doas tee /etc/hostname.bridge0

# Добавить физический интерфейс в bridge
# echo "add em0" >> /etc/hostname.bridge0

# Или использовать NAT с vether
# doas ifconfig vether0 create
# echo "inet 10.0.0.1/24 up" | doas tee /etc/hostname.vether0

# NAT в pf.conf
match out on egress from 10.0.0.0/24 nat-to (egress)
pass out on egress from 10.0.0.0/24

```

### 1.6 Linux гости

```sh
# Для Linux нужен cloud-init образ или установка через ISO
# doas vmctl create -s 20G /var/vm/debian.qcow2

# /etc/vm.conf
vm "debian" {
    memory 2G
    disk /var/vm/debian.qcow2
    cdrom /var/vm/debian-netinst.iso
    interface { switch "local" }
    boot cdrom
}

```

---

## 2. CARP — отказоустойчивость

### 2.1 Что такое CARP

**CARP** (Common Address Redundancy Protocol) — протокол для создания отказоустойчивых конфигураций.

```

┌──────────────┐     ┌──────────────┐
│   Master     │     │   Backup     │
│  (Active)    │     │  (Standby)   │
│ 192.168.1.2  │     │ 192.168.1.3  │
└──────┬───────┘     └──────┬───────┘
       │                    │
       └────────┬───────────┘
                │
         ┌──────┴──────┐
         │ Virtual IP  │
         │192.168.1.1  │
         └─────────────┘

```

### 2.2 Настройка CARP

**Master (первичный сервер):**

```sh
# /etc/hostname.carp0
inet 192.168.1.1 255.255.255.0 192.168.1.255 vhid 1 pass secretkey advskew 0

```

**Backup (резервный сервер):**

```sh
# /etc/hostname.carp0
inet 192.168.1.1 255.255.255.0 192.168.1.255 vhid 1 pass secretkey advskew 100

```

### 2.3 Проверка CARP

```sh
# Статус CARP интерфейсов
$ ifconfig carp0
carp0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        carp: MASTER vhid 1 advbase 1 advskew 0
        inet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255

# На backup будет BACKUP вместо MASTER
```

### 2.4 pfsync — синхронизация состояний PF

```sh
# Синхронизация состояний файрвола между нодами
# /etc/hostname.pfsync0
syncdev em1

# В pf.conf
set syncookies adaptive (start 25%, end 12%)
set state-defaults pflow

```

---

## 3. Сборка ядра

### 3.1 Получение исходников

```sh
# Скачать исходники
$ cd /usr
$ ftp https://cdn.openbsd.org/pub/OpenBSD/7.4/sys.tar.gz
# doas tar -xzf sys.tar.gz
```

### 3.2 Конфигурация ядра

```sh
# Скопировать конфигурацию
$ cd /usr/src/sys/arch/amd64/conf
$ doas cp GENERIC.MP MYKERNEL

# Редактировать конфигурацию
# doas vi MYKERNEL

# Примеры изменений:
# - Отключить ненужные драйверы
# - Изменить параметры
# - Включить отладку
```

### 3.3 Сборка ядра

```sh
# Создать конфигурацию
$ cd /usr/src/sys/arch/amd64/conf
# doas config MYKERNEL

# Собрать ядро
$ cd /usr/src/sys/arch/amd64/compile/MYKERNEL
# doas make clean
# doas make

# Установить
# doas make install

# Старое ядро сохраняется как /obsd
# doas reboot
```

### 3.4 Откат к старому ядру

```sh
# При загрузке:
boot> boot /obsd

# Или если совсем не грузится — boot с bsd.rd
boot> boot /bsd.rd

```

---

## 4. OpenBSD как роутер

### 4.1 Базовая конфигурация роутера

```sh
# Включить IP forwarding
# echo "net.inet.ip.forwarding=1" >> /etc/sysctl.conf

# Внешний интерфейс (DHCP от провайдера)
# /etc/hostname.em0
dhcp

# Внутренний интерфейс
# /etc/hostname.em1
inet 192.168.1.1/24

```

### 4.2 NAT и файрвол для роутера

```sh
# /etc/pf.conf
ext_if = "em0"
int_if = "em1"
int_net = "192.168.1.0/24"

set skip on lo0
set block-policy drop

# NAT
match out on $ext_if from $int_net nat-to ($ext_if)

# Блокировать входящий, разрешить исходящий
block in all
pass out all keep state

# Разрешить от внутренней сети
pass in on $int_if from $int_net

# SSH к роутеру только из внутренней сети
pass in on $int_if proto tcp to port 22

```

### 4.3 DHCP сервер

```sh
# /etc/dhcpd.conf
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8, 1.1.1.1;
    option domain-name "home.local";
    default-lease-time 86400;
    max-lease-time 172800;
}

# Включить
# doas rcctl enable dhcpd
# doas rcctl set dhcpd flags em1
# doas rcctl start dhcpd
```

### 4.4 DNS сервер (unbound)

```sh
# /var/unbound/etc/unbound.conf
server:
    interface: 192.168.1.1
    interface: 127.0.0.1
    access-control: 192.168.1.0/24 allow
    access-control: 127.0.0.0/8 allow
    
    # Кэширование
    cache-max-ttl: 86400
    cache-min-ttl: 3600
    
    # Блокировка рекламы (опционально)
    local-zone: "ads.example.com" redirect
    local-data: "ads.example.com A 0.0.0.0"

# Включить
# doas rcctl enable unbound
# doas rcctl start unbound
```

---

## 5. WireGuard VPN

### 5.1 Настройка сервера

```sh
# Создать интерфейс
# doas ifconfig wg0 create

# Сгенерировать ключи
$ openssl rand -base64 32 > /etc/wireguard/private.key
$ chmod 600 /etc/wireguard/private.key
$ cat /etc/wireguard/private.key | wg pubkey > /etc/wireguard/public.key

# /etc/hostname.wg0
wgkey $(cat /etc/wireguard/private.key)
wgport 51820
wgpeer <client_public_key> wgaip 10.0.0.2/32
inet 10.0.0.1/24
up

```

### 5.2 Настройка клиента

```sh
# /etc/hostname.wg0
wgkey <client_private_key>
wgpeer <server_public_key> wgendpoint server.example.com 51820 wgaip 0.0.0.0/0 wgpka 25
inet 10.0.0.2/24
wgrtable 1
up

# Маршрут через VPN
!/sbin/route -T1 add default 10.0.0.1

```

### 5.3 PF правила для WireGuard

```sh
# Разрешить WireGuard трафик
pass in on egress proto udp to port 51820

# NAT для VPN клиентов
match out on egress from 10.0.0.0/24 nat-to (egress)

# Трафик от VPN клиентов
pass in on wg0

```

---

## 6. Мониторинг и метрики

### 6.1 pflow — экспорт NetFlow

```sh
# /etc/hostname.pflow0
flowsrc 192.168.1.1 flowdst 192.168.1.10:9995 pflowproto 10

# В pf.conf
set state-defaults pflow

# Включить интерфейс
# doas sh /etc/netstart pflow0
```

### 6.2 SNMP

```sh
# Установить net-snmp
# doas pkg_add net-snmp

# Конфигурация: /etc/snmpd.conf
# Включить
# doas rcctl enable snmpd
# doas rcctl start snmpd
```

### 6.3 Prometheus node_exporter

```sh
# Установить
# doas pkg_add node_exporter

# Включить
# doas rcctl enable node_exporter
# doas rcctl start node_exporter

# Доступен на :9100/metrics
```

---

## 7. Отладка и профилирование

### 7.1 ktrace — трассировка syscalls

```sh
# Трассировать команду
$ ktrace ls

# Просмотреть результат
$ kdump

# Фильтр по типу
$ ktrace -tc syscall ls
$ kdump | grep open

```

### 7.2 DTrace (экспериментальный)

```sh
# DTrace доступен в OpenBSD (ограниченно)
# doas dtrace -l | head
```

### 7.3 Core dumps

```sh
# Включить core dumps
$ ulimit -c unlimited

# Местоположение
# Обычно в текущем каталоге или /var/crash

# Анализ с gdb
$ gdb /path/to/program /path/to/core

```

---

## 8. Практические проекты

### 8.1 Домашний роутер/файрвол

```

ISP ─── em0 [OpenBSD Router] em1 ─── LAN
                   │
                   └─ wg0 ─── VPN Clients

```

Компоненты:

- PF файрвол с NAT
- DHCP сервер
- DNS кэширование (unbound)
- WireGuard VPN
- Мониторинг трафика

### 8.2 VPN сервер

```

Internet ─── [OpenBSD VPN] ─── Secure Access
                   │
              wg0/tun0

```

### 8.3 Web-хостинг

```

Internet ─── PF ─── httpd/nginx ─── Applications
                         │
                    PostgreSQL

```

---

## 💡 Key Takeaways

- **vmm/vmd**: Нативная виртуализация для OpenBSD и Linux гостей

- **CARP**: Простая отказоустойчивость без сложной конфигурации

- **WireGuard**: Современный VPN прямо в базовой системе

- **Роутер**: OpenBSD — отличная платформа для файрволов и роутеров

- **Ядро**: Можно собрать кастомное, но GENERIC обычно достаточно

---

## 🚀 Next Steps

**После курса:**

- Постройте домашний роутер на OpenBSD
- Настройте VPN для удалённого доступа
- Изучите исходный код OpenBSD
- Присоединитесь к рассылке misc@openbsd.org

**Going Deeper:**

- Изучите relayd для балансировки
- Настройте OpenBGPD для BGP
- Создайте кластер с CARP и pfsync

---

## 📚 Additional Resources

**Documentation:**

- [man vmctl](https://man.openbsd.org/vmctl) — управление VM
- [man vm.conf](https://man.openbsd.org/vm.conf) — конфигурация VM
- [man carp](https://man.openbsd.org/carp) — отказоустойчивость
- [OpenBSD FAQ](https://www.openbsd.org/faq/) — полное руководство

**Books:**

- "Absolute OpenBSD" by Michael W. Lucas
- "The Book of PF" by Peter N. M. Hansteen

**Community:**

- misc@openbsd.org — общие вопросы
- tech@openbsd.org — технические обсуждения
- https://undeadly.org — новости OpenBSD

---

## 🎓 Поздравляем!

Вы завершили курс по OpenBSD. Теперь вы можете:

✅ Устанавливать и настраивать OpenBSD
✅ Управлять пользователями и пакетами
✅ Настраивать сеть и файрвол PF
✅ Обеспечивать безопасность системы
✅ Администрировать серверы
✅ Настраивать виртуализацию и VPN

**Продолжайте изучать и экспериментировать!**

---




