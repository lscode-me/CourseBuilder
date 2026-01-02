# systemd-nspawn
## Системные контейнеры и машины

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать Linux namespaces и cgroups
- Знать основы работы с systemd
- Иметь опыт работы с командной строкой Linux

**Recommended prior modules:**

- [Namespaces](../02_Namespaces/) — изоляция процессов
- [Cgroups](../03_Cgroups/) — управление ресурсами
- [Runtimes](../06_Runtimes/) — обзор container runtimes

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять системными контейнерами через systemd-nspawn
- Понимать отличия systemd-контейнеров от Docker/OCI контейнеров
- Настраивать сеть, ресурсы и безопасность nspawn-контейнеров
- Использовать machinectl для оркестрации машин
- Интегрировать контейнеры с systemd unit файлами

---

## 1. Введение в systemd-nspawn

### 1.1 Что такое systemd-nspawn?

systemd-nspawn — это инструмент для запуска команд или целых операционных систем в лёгких контейнерах. Он входит в состав systemd и предназначен для создания "системных контейнеров" (machine containers).

```
┌──────────────────────────────────────────────────────────────┐
│                    Application Containers                    │
│                    (Docker, Podman, OCI)                     │
│    • Запуск одного приложения                                │
│    • Layered filesystem                                      │
│    • Image-based deployment                                  │
└──────────────────────────────────────────────────────────────┘
                              vs
┌─────────────────────────────────────────────────────────────┐
│                    System Containers                        │
│                    (systemd-nspawn, LXC)                    │
│    • Полная ОС с init-системой                              │
│    • Традиционная файловая система                          │
│    • Похоже на лёгкую виртуальную машину                    │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Сравнение подходов

| Аспект | Docker/OCI | systemd-nspawn | VM (KVM/QEMU) |
|--------|------------|----------------|---------------|
| Изоляция | Namespaces + cgroups | Namespaces + cgroups | Полная (гипервизор) |
| Init система | Нет (PID 1 = app) | Да (systemd/init) | Да (полная ОС) |
| Образы | OCI images, layers | Директория/tar/raw | Disk images |
| Overhead | Минимальный | Минимальный | Значительный |
| Boot time | Миллисекунды | Секунды | Десятки секунд |
| Use case | Микросервисы | Системное тестирование | Полная изоляция |

### 1.3 Когда использовать systemd-nspawn

**Идеальные сценарии:**

- Тестирование других дистрибутивов
- Сборочные среды (build environments)
- CI/CD для системного ПО
- Изолированные сервисы с полным systemd
- Безопасное тестирование системных утилит
- Разработка и отладка systemd unit-файлов

```bash
# Проверка доступности

systemd-nspawn --version
```

**Output:**
```
systemd 252 (252.22-1~deb12u1)
+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD +BPF_FRAMEWORK +XKBCOMMON +UTMP -SYSVINIT default-hierarchy=unified
```

---

## 2. Быстрый старт

### 2.1 Минимальный контейнер

```bash
# Создаём минимальное дерево с busybox

mkdir -p /var/lib/machines/minimal
cd /var/lib/machines/minimal

# Копируем busybox

cp /bin/busybox bin/busybox
mkdir -p bin usr/bin sbin usr/sbin

# Создаём ссылки для основных команд

for cmd in sh ls cat echo mkdir rm; do
    ln -s busybox bin/$cmd
done

# Запускаем контейнер

systemd-nspawn -D /var/lib/machines/minimal /bin/sh
```

**Output:**
```
Spawning container minimal on /var/lib/machines/minimal.
Press ^] three times within 1s to kill container.
/ # ls
bin  sbin  usr
/ # echo "Hello from container"
Hello from container
/ # exit
Container minimal exited successfully.
```

### 2.2 Установка полноценной системы

```bash
# Debian/Ubuntu — используем debootstrap

apt install debootstrap

# Создаём контейнер с Debian

debootstrap --include=systemd,dbus bookworm /var/lib/machines/debian http://deb.debian.org/debian

# Запуск с полным boot

systemd-nspawn -b -D /var/lib/machines/debian
```

```bash
# Fedora/RHEL — используем dnf

dnf -y --releasever=39 --installroot=/var/lib/machines/fedora \
    --repo=fedora --repo=fedora-updates install \
    systemd passwd dnf fedora-release vim-minimal

# Запуск

systemd-nspawn -b -D /var/lib/machines/fedora
```

```bash
# Arch Linux — используем pacstrap

pacstrap -c /var/lib/machines/arch base

# Запуск

systemd-nspawn -b -D /var/lib/machines/arch
```

### 2.3 Первоначальная настройка

```bash
# Установка пароля root (без -b для доступа к shell)

systemd-nspawn -D /var/lib/machines/debian passwd root

# Или интерактивно

systemd-nspawn -D /var/lib/machines/debian
```

**Output:**
```
Spawning container debian on /var/lib/machines/debian.
Press ^] three times within 1s to kill container.
root@debian:~# passwd
New password: 
Retype new password: 
passwd: password updated successfully
root@debian:~# exit
```

---

## 3. Основные опции systemd-nspawn

### 3.1 Режимы запуска

```bash
# Интерактивный shell (по умолчанию)

systemd-nspawn -D /var/lib/machines/debian

# Boot mode — запуск init системы

systemd-nspawn -b -D /var/lib/machines/debian

# Выполнение одной команды

systemd-nspawn -D /var/lib/machines/debian cat /etc/os-release

# Интерактивный boot с автоматическим логином

systemd-nspawn -b -D /var/lib/machines/debian --console=autopipe
```

### 3.2 Namespaces и изоляция

```bash
# Показать какие namespaces изолированы

systemd-nspawn -D /var/lib/machines/debian \
    ls -la /proc/self/ns/
```

**Output:**
```
lrwxrwxrwx 1 root root 0 Dec  1 10:00 cgroup -> 'cgroup:[4026532509]'
lrwxrwxrwx 1 root root 0 Dec  1 10:00 ipc -> 'ipc:[4026532507]'
lrwxrwxrwx 1 root root 0 Dec  1 10:00 mnt -> 'mnt:[4026532505]'
lrwxrwxrwx 1 root root 0 Dec  1 10:00 net -> 'net:[4026532510]'
lrwxrwxrwx 1 root root 0 Dec  1 10:00 pid -> 'pid:[4026532508]'
lrwxrwxrwx 1 root root 0 Dec  1 10:00 uts -> 'uts:[4026532506]'
```

```bash
# Использовать host network namespace

systemd-nspawn --network-namespace-path=/proc/1/ns/net -D /var/lib/machines/debian

# Приватная сеть (изолированная)

systemd-nspawn --private-network -D /var/lib/machines/debian
```

### 3.3 Управление capabilities

```bash
# Показать capabilities по умолчанию

systemd-nspawn -D /var/lib/machines/debian \
    capsh --print

# Дополнительные capabilities

systemd-nspawn --capability=CAP_NET_ADMIN,CAP_SYS_ADMIN \
    -D /var/lib/machines/debian

# Все capabilities (небезопасно!)

systemd-nspawn --capability=all -D /var/lib/machines/debian

# Убрать capability

systemd-nspawn --drop-capability=CAP_NET_RAW \
    -D /var/lib/machines/debian
```

### 3.4 Bind mounts

```bash
# Монтирование директории (read-write)

systemd-nspawn --bind=/home/user/shared:/mnt/shared \
    -D /var/lib/machines/debian

# Read-only монтирование

systemd-nspawn --bind-ro=/etc/resolv.conf:/etc/resolv.conf \
    -D /var/lib/machines/debian

# Несколько mount-ов

systemd-nspawn \
    --bind=/var/log/containers:/var/log \
    --bind-ro=/etc/ssl/certs:/etc/ssl/certs \
    -D /var/lib/machines/debian
```

### 3.5 Переменные окружения

```bash
# Установка переменных окружения

systemd-nspawn \
    --setenv=MY_VAR=value \
    --setenv=LANG=en_US.UTF-8 \
    -D /var/lib/machines/debian env
```

**Output:**
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
TERM=xterm-256color
container=systemd-nspawn
MY_VAR=value
LANG=en_US.UTF-8
```

---

## 4. Сеть в systemd-nspawn

### 4.1 Режимы сети

```
┌─────────────────────────────────────────────────────────────┐
│                    Network Modes                            │
├─────────────────────────────────────────────────────────────┤
│  --private-network     Полностью изолированная сеть (lo)    │
│  --network-veth        Virtual Ethernet pair к хосту        │
│  --network-bridge=br0  Подключение к bridge                 │
│  --network-macvlan=eth0  MACVLAN интерфейс                  │
│  --network-ipvlan=eth0   IPVLAN интерфейс                   │
│  (default)             Host network (без изоляции)          │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Virtual Ethernet (veth)

```bash
# Запуск с veth интерфейсом

systemd-nspawn -b --network-veth -D /var/lib/machines/debian
```

На хосте появится интерфейс `ve-<machine>`:

```bash
# На хосте

ip link show | grep ve-
```

**Output:**
```
5: ve-debian@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
```

```bash
# Настройка сети на хосте

ip addr add 10.0.0.1/24 dev ve-debian
ip link set ve-debian up

# Включение IP forwarding и NAT

sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -j MASQUERADE
```

Внутри контейнера:
```bash
# В контейнере

ip addr add 10.0.0.2/24 dev host0
ip link set host0 up
ip route add default via 10.0.0.1
echo "nameserver 8.8.8.8" > /etc/resolv.conf
```

### 4.3 Bridge networking

```bash
# Создание bridge на хосте

ip link add br0 type bridge
ip addr add 192.168.100.1/24 dev br0
ip link set br0 up

# Запуск контейнера с подключением к bridge

systemd-nspawn -b --network-bridge=br0 -D /var/lib/machines/debian
```

### 4.4 Автоматическая настройка сети через systemd-networkd

```bash
# В контейнере создаём /etc/systemd/network/80-container-host0.network

cat > /var/lib/machines/debian/etc/systemd/network/80-container-host0.network << 'EOF'
[Match]
Virtualization=container
Name=host0

[Network]
DHCP=yes
EOF

# Или статическая конфигурация

cat > /var/lib/machines/debian/etc/systemd/network/80-container-host0.network << 'EOF'
[Match]
Virtualization=container
Name=host0

[Network]
Address=10.0.0.2/24
Gateway=10.0.0.1
DNS=8.8.8.8
EOF
```

### 4.5 Port forwarding

systemd-nspawn не имеет встроенного port forwarding. Используем iptables:

```bash
# Forward порта 8080 хоста на порт 80 контейнера

iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.0.0.2:80
iptables -A FORWARD -p tcp -d 10.0.0.2 --dport 80 -j ACCEPT
```

---

## 5. machinectl — управление машинами

### 5.1 Регистрация машин

machinectl — CLI для systemd-machined, управляет "машинами" (контейнерами и VM).

```bash
# Список машин

machinectl list
```

**Output:**
```
MACHINE   CLASS     SERVICE        OS     VERSION ADDRESSES
debian    container systemd-nspawn debian 12      10.0.0.2...

1 machines listed.
```

```bash
# Детальная информация

machinectl status debian
```

**Output:**
```
debian(1234567890abcdef)
           Since: Wed 2024-12-01 10:00:00 UTC; 1h 30min ago
          Leader: 12345 (systemd)
         Service: systemd-nspawn; class container
            Root: /var/lib/machines/debian
              OS: Debian GNU/Linux 12 (bookworm)
            Unit: systemd-nspawn@debian.service
           Tasks: 15
          Memory: 128.5M
             CPU: 2.345s
```

### 5.2 Управление жизненным циклом

```bash
# Запуск машины

machinectl start debian

# Остановка

machinectl stop debian

# Перезагрузка

machinectl reboot debian

# Принудительное завершение

machinectl terminate debian

# Выключение (graceful)

machinectl poweroff debian
```

### 5.3 Интерактивный доступ

```bash
# Login shell

machinectl login debian

# Shell без login

machinectl shell debian

# Выполнение команды

machinectl shell debian /bin/cat /etc/os-release

# Shell от конкретного пользователя

machinectl shell --uid=www-data debian
```

### 5.4 Копирование файлов

```bash
# Копирование файла в машину

machinectl copy-to debian /local/path/file.txt /container/path/file.txt

# Копирование из машины

machinectl copy-from debian /container/path/file.txt /local/path/file.txt
```

### 5.5 Управление образами

```bash
# Список образов (директорий в /var/lib/machines)

machinectl list-images
```

**Output:**
```
NAME   TYPE      RO  USAGE  CREATED                     MODIFIED
debian directory no  1.2G   Wed 2024-12-01 10:00:00 UTC Wed 2024-12-01 11:30:00 UTC
fedora directory no  800.0M Wed 2024-12-01 09:00:00 UTC Wed 2024-12-01 09:30:00 UTC
```

```bash
# Клонирование образа

machinectl clone debian debian-clone

# Переименование

machinectl rename debian-clone debian-test

# Удаление образа

machinectl remove debian-test

# Экспорт образа в tar

machinectl export-tar debian debian-backup.tar.gz

# Импорт

machinectl import-tar debian-backup.tar.gz debian-restored
```

### 5.6 Raw образы

machinectl поддерживает raw disk images:

```bash
# Создание raw образа

truncate -s 4G /var/lib/machines/myimage.raw
mkfs.ext4 /var/lib/machines/myimage.raw

# Монтирование и установка системы

mount /var/lib/machines/myimage.raw /mnt
debootstrap bookworm /mnt
umount /mnt

# Запуск (автоматическое определение)

machinectl start myimage

# Или с указанием образа

systemd-nspawn -b -i /var/lib/machines/myimage.raw
```

---

## 6. Конфигурационные файлы .nspawn

### 6.1 Создание .nspawn файла

Файлы `/etc/systemd/nspawn/<machine>.nspawn` позволяют настроить машину декларативно:

```ini
# /etc/systemd/nspawn/debian.nspawn

[Exec]
Boot=yes
Capability=CAP_NET_ADMIN CAP_SYS_ADMIN
Environment=LANG=en_US.UTF-8

[Files]
Bind=/home/user/shared:/shared
BindReadOnly=/etc/resolv.conf
TemporaryFileSystem=/tmp

[Network]
VirtualEthernet=yes
Bridge=br0
```

### 6.2 Секция [Exec]

```ini
[Exec]
# Запускать init систему

Boot=yes

# Команда для запуска (если не boot)

ProcessTwo=no
Parameters=/bin/bash

# Capabilities

Capability=CAP_NET_ADMIN CAP_SYS_TIME
DropCapability=CAP_SYS_RAWIO

# Ограничения

NoNewPrivileges=yes
PrivateUsers=yes

# Окружение

Environment=MY_VAR=value
Environment=ANOTHER_VAR=another

# Hostname

Hostname=mycontainer

# Рабочая директория

WorkingDirectory=/app
```

### 6.3 Секция [Files]

```ini
[Files]
# Bind mounts

Bind=/host/path:/container/path
BindReadOnly=/host/readonly:/container/readonly

# Временные файловые системы

TemporaryFileSystem=/tmp
TemporaryFileSystem=/run

# Volatile mode

Volatile=yes  # Overlay над root
# или

Volatile=state  # Только /var изменяем

# Приватные директории

PrivateUsersChown=yes
```

### 6.4 Секция [Network]

```ini
[Network]
# Приватная сеть (только loopback)

Private=yes

# Virtual Ethernet

VirtualEthernet=yes
VirtualEthernetExtra=veth-extra:host-extra

# Bridge

Bridge=br0

# MACVLAN/IPVLAN

MACVLAN=eth0
IPVLAN=eth0

# Зона (для firewalld)

Zone=trusted

# Port forwarding через nspawn (systemd 254+)

Port=tcp:8080:80
Port=udp:5353:53
```

### 6.5 Полный пример

```ini
# /etc/systemd/nspawn/webserver.nspawn

[Exec]
Boot=yes
Capability=CAP_NET_BIND_SERVICE
Environment=NODE_ENV=production
WorkingDirectory=/app

[Files]
Bind=/srv/webserver/data:/var/lib/app
BindReadOnly=/etc/ssl/certs:/etc/ssl/certs
TemporaryFileSystem=/tmp:mode=1777

[Network]
VirtualEthernet=yes
Port=tcp:80:80
Port=tcp:443:443
```

---

## 7. Интеграция с systemd

### 7.1 systemd-nspawn@.service

systemd предоставляет template unit для запуска машин:

```bash
# Включение автозапуска машины

systemctl enable systemd-nspawn@debian.service

# Запуск

systemctl start systemd-nspawn@debian.service

# Статус

systemctl status systemd-nspawn@debian.service
```

**Output:**
```
● systemd-nspawn@debian.service - Container debian
     Loaded: loaded (/lib/systemd/system/systemd-nspawn@.service; enabled; preset: enabled)
     Active: active (running) since Wed 2024-12-01 10:00:00 UTC; 2h ago
       Docs: man:systemd-nspawn(1)
   Main PID: 12345 (systemd-nspawn)
     Status: "Container running: Startup finished in 1.234s."
      Tasks: 25 (limit: 16384)
     Memory: 256.0M
        CPU: 5.678s
     CGroup: /machine.slice/systemd-nspawn@debian.service
             ├─12345 /usr/bin/systemd-nspawn --quiet --keep-unit --boot --link-journal=try-guest...
             └─supervisor
               ├─init.scope
               │ └─12346 /lib/systemd/systemd
               └─system.slice
                 ├─systemd-journald.service
                 │ └─12347 /lib/systemd/systemd-journald
                 └─...
```

### 7.2 Собственный unit файл

```ini
# /etc/systemd/system/mycontainer.service

[Unit]
Description=My Container
After=network.target
Wants=network.target

[Service]
Type=notify
ExecStart=/usr/bin/systemd-nspawn \
    --quiet \
    --keep-unit \
    --boot \
    --network-veth \
    --settings=override \
    --machine=mycontainer \
    --directory=/var/lib/machines/mycontainer
KillMode=mixed
Restart=on-failure
RestartSec=10s

# Resource limits

MemoryMax=2G
CPUQuota=200%
TasksMax=500

[Install]
WantedBy=multi-user.target
```

### 7.3 Resource limits через cgroups

```bash
# Через systemd-run

systemd-run --scope -p MemoryMax=1G -p CPUQuota=50% \
    systemd-nspawn -b -D /var/lib/machines/debian

# Через .nspawn файл — не поддерживается напрямую
# Используем drop-in для unit файла

mkdir -p /etc/systemd/system/systemd-nspawn@debian.service.d/

cat > /etc/systemd/system/systemd-nspawn@debian.service.d/limits.conf << 'EOF'
[Service]
MemoryMax=2G
CPUQuota=150%
TasksMax=200
IOWeight=100
EOF

systemctl daemon-reload
systemctl restart systemd-nspawn@debian.service
```

### 7.4 Journald интеграция

```bash
# Логи контейнера

journalctl -M debian

# Follow логов

journalctl -M debian -f

# Логи конкретного сервиса в контейнере

journalctl -M debian -u nginx.service

# Логи с хоста для unit-а контейнера

journalctl -u systemd-nspawn@debian.service
```

### 7.5 Проброс журналов

```bash
# Опция --link-journal контролирует проброс

systemd-nspawn --link-journal=host -b -D /var/lib/machines/debian
# host: журналы пишутся в host journal
# guest: журналы в контейнере
# try-host/try-guest: попытка, fallback на guest
# no: отключить
```

---

## 8. Безопасность

### 8.1 Модель безопасности

```
┌─────────────────────────────────────────────────────────────┐
│               systemd-nspawn Security Layers                │
├─────────────────────────────────────────────────────────────┤
│  1. Linux Namespaces      → Изоляция ресурсов               │
│  2. Cgroups v2            → Ограничение ресурсов            │
│  3. Seccomp               → Фильтрация syscalls             │
│  4. Capabilities          → Ограничение привилегий          │
│  5. Read-only paths       → Защита системных путей          │
│  6. Private /dev          → Изоляция устройств              │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Capabilities по умолчанию

systemd-nspawn по умолчанию даёт ограниченный набор capabilities:

```bash
# Capabilities в контейнере

systemd-nspawn -D /var/lib/machines/debian capsh --print
```

**Output:**
```
Current: cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_ipc_lock,cap_ipc_owner,cap_kill,cap_lease,cap_linux_immutable,cap_mknod,cap_net_bind_service,cap_net_broadcast,cap_net_raw,cap_setfcap,cap_setgid,cap_setpcap,cap_setuid,cap_sys_admin,cap_sys_chroot,cap_sys_nice,cap_sys_ptrace,cap_sys_resource=ep
Bounding set =cap_chown,cap_dac_override,...
```

### 8.3 Усиление безопасности

```bash
# Минимальные capabilities

systemd-nspawn --drop-capability=all \
    --capability=CAP_NET_BIND_SERVICE \
    -D /var/lib/machines/debian

# Private users (user namespace mapping)

systemd-nspawn --private-users=pick \
    -D /var/lib/machines/debian

# Запрет новых привилегий

systemd-nspawn --no-new-privileges=yes \
    -D /var/lib/machines/debian

# Read-only root

systemd-nspawn --read-only \
    -D /var/lib/machines/debian
```

### 8.4 User namespaces

```bash
# Автоматический выбор UID/GID mapping

systemd-nspawn --private-users=pick -b -D /var/lib/machines/debian

# Конкретный диапазон

systemd-nspawn --private-users=100000:65536 -b -D /var/lib/machines/debian

# Настройка /etc/subuid и /etc/subgid

echo "root:100000:65536" >> /etc/subuid
echo "root:100000:65536" >> /etc/subgid
```

### 8.5 Seccomp и system call filtering

systemd-nspawn применяет seccomp фильтр по умолчанию:

```bash
# Проверка seccomp статуса в контейнере

cat /proc/self/status | grep Seccomp
```

**Output:**
```
Seccomp:    2
Seccomp_filters:    1
```

```bash
# Отключение seccomp (небезопасно!)

systemd-nspawn --system-call-filter='' -D /var/lib/machines/debian
```

### 8.6 SELinux и AppArmor

```bash
# Проверка контекста SELinux

systemd-nspawn -D /var/lib/machines/debian id -Z

# Установка контекста

systemd-nspawn --selinux-context=system_u:system_r:container_t:s0 \
    -D /var/lib/machines/debian

# AppArmor профиль

systemd-nspawn --settings=trusted -D /var/lib/machines/debian
```

---

## 9. Практические примеры

### 9.1 Build environment

```bash
#!/bin/bash
# Изолированная среда сборки

BUILD_ROOT="/var/lib/machines/build-env"

# Создание среды

debootstrap --variant=minbase \
    --include=build-essential,git,curl,wget \
    bookworm "$BUILD_ROOT" http://deb.debian.org/debian

# Запуск с монтированием исходников

systemd-nspawn \
    --bind="$PWD:/src" \
    --private-network \
    --read-only \
    --volatile=yes \
    -D "$BUILD_ROOT" \
    /bin/bash -c "cd /src && make clean && make"
```

### 9.2 Тестирование на разных дистрибутивах

```bash
#!/bin/bash
# Тестирование на нескольких дистрибутивах

DISTROS=("debian" "fedora" "arch")

for distro in "${DISTROS[@]}"; do
    echo "Testing on $distro..."
    machinectl start "$distro"
    
    machinectl shell "$distro" /bin/bash -c "
        cd /test
        ./run_tests.sh
    " > "test-results-${distro}.log" 2>&1
    
    machinectl stop "$distro"
done
```

### 9.3 Ephemeral контейнер

```bash
# Volatile контейнер — изменения теряются после остановки

systemd-nspawn \
    --volatile=yes \
    --ephemeral \
    -D /var/lib/machines/debian \
    /bin/bash

# С overlay над базовым образом

systemd-nspawn \
    --volatile=overlay \
    --template=/var/lib/machines/debian \
    --ephemeral \
    -b -M test-instance
```

### 9.4 Веб-сервер в контейнере

```bash
# Создание контейнера

debootstrap --include=nginx,systemd bookworm \
    /var/lib/machines/webserver http://deb.debian.org/debian

# Конфигурация

cat > /etc/systemd/nspawn/webserver.nspawn << 'EOF'
[Exec]
Boot=yes
Capability=CAP_NET_BIND_SERVICE

[Files]
Bind=/srv/www:/var/www/html

[Network]
VirtualEthernet=yes
EOF

# Настройка сети на хосте

cat > /etc/systemd/network/80-ve-webserver.network << 'EOF'
[Match]
Name=ve-webserver

[Network]
Address=192.168.99.1/24
IPMasquerade=yes
EOF

# Запуск

machinectl start webserver

# Настройка сети в контейнере

machinectl shell webserver /bin/bash -c '
cat > /etc/systemd/network/80-host0.network << EOF
[Match]
Name=host0

[Network]
Address=192.168.99.2/24
Gateway=192.168.99.1
DNS=8.8.8.8
EOF
systemctl restart systemd-networkd
systemctl enable --now nginx
'
```

### 9.5 Development environment

```bash
# Создание dev-среды с сохранением home directory

systemd-nspawn \
    --bind=/home/developer:/home/developer \
    --bind=/var/run/docker.sock:/var/run/docker.sock \
    --setenv=HOME=/home/developer \
    --setenv=USER=developer \
    -u developer \
    -D /var/lib/machines/dev-env \
    /bin/zsh
```

---

## 10. Сравнение с другими решениями

### 10.1 systemd-nspawn vs Docker

| Аспект | systemd-nspawn | Docker |
|--------|----------------|--------|
| Философия | Системные контейнеры | Application контейнеры |
| Daemon | Нет | dockerd |
| Image format | Directory/tar/raw | OCI layers |
| Init system | Поддержка systemd | Не рекомендуется |
| Networking | Ручная настройка | Встроенный networking |
| Volumes | bind mounts | volumes + bind mounts |
| Orchestration | machinectl | Docker Swarm/Compose |
| Registry | Нет | Docker Hub, registries |
| Ecosystem | systemd | Огромная |

### 10.2 systemd-nspawn vs LXC/LXD

| Аспект | systemd-nspawn | LXC/LXD |
|--------|----------------|---------|
| Установка | Часть systemd | Отдельный пакет |
| Конфигурация | .nspawn файлы | YAML/config |
| Управление | machinectl | lxc/lxd CLI |
| Images | Manual/debootstrap | Image servers |
| Networking | Ручная настройка | Встроенная |
| Storage | Directory/raw | ZFS, btrfs, LVM |
| Snapshots | Нет (без btrfs) | Да |
| Clustering | Нет | Да (LXD) |

### 10.3 Когда выбрать systemd-nspawn

**Выбирайте systemd-nspawn если:**

- Нужен полноценный systemd в контейнере
- Тестирование системного ПО
- Уже используете systemd экосистему
- Нужен простой и понятный инструмент
- CI/CD для системных пакетов
- Минимум зависимостей

**Не выбирайте systemd-nspawn если:**

- Нужна оркестрация (используйте K8s, Docker Swarm)
- Нужен image registry (используйте Docker, Podman)
- Микросервисная архитектура (используйте Docker)
- Нужны snapshots и advanced storage

---

## 💡 Key Takeaways

- **systemd-nspawn** — это инструмент для системных контейнеров, часть systemd

- **machinectl** — CLI для управления машинами и образами

- **Конфигурация** через .nspawn файлы для декларативной настройки

- **Интеграция с systemd** — unit файлы, journald, cgroups

- **Безопасность** — namespaces, capabilities, seccomp, user namespaces

- **Use cases** — тестирование, сборка, системные сервисы с init

---

## 🚀 Next Steps

**Related Modules:**

- [Runtimes](../06_Runtimes/) — другие container runtimes
- [Namespaces](../02_Namespaces/) — глубже в изоляцию
- [Cgroups](../03_Cgroups/) — ограничение ресурсов

**Practice Ideas:**

1. Создайте контейнер с Debian и настройте в нём nginx с systemd
2. Настройте bridge networking для нескольких контейнеров
3. Напишите .nspawn файл для production-ready конфигурации
4. Сравните производительность systemd-nspawn и Docker
5. Настройте CI pipeline с ephemeral контейнерами

**Going Deeper:**

- Portable Services (systemd-portable)
- Integration с systemd-homed
- mkosi — tool для создания образов

---

## 📚 Additional Resources

**Documentation:**

- [systemd-nspawn man page](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html)
- [machinectl man page](https://www.freedesktop.org/software/systemd/man/machinectl.html)
- [systemd.nspawn man page](https://www.freedesktop.org/software/systemd/man/systemd.nspawn.html)

**Articles:**

- [Arch Wiki: systemd-nspawn](https://wiki.archlinux.org/title/systemd-nspawn)
- [Fedora: systemd-nspawn](https://fedoramagazine.org/systemd-nspawn-containers/)
- [Running systemd in containers](https://systemd.io/CONTAINER_INTERFACE/)

**Tools:**

- [mkosi](https://github.com/systemd/mkosi) — создание образов для systemd-nspawn
- [casync](https://github.com/systemd/casync) — content-addressable sync

---





