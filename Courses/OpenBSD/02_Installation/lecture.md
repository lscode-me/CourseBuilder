# Installation
## Установка и первоначальная настройка OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Прочитать модуль [Introduction](../01_Intro/) о философии OpenBSD
- Иметь компьютер или виртуальную машину для установки
- Понимать базовые концепции: разделы диска, IP-адреса, загрузка

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Скачать и проверить образ OpenBSD
- Выполнить установку на физическую или виртуальную машину
- Настроить разбиение диска
- Выполнить первоначальную настройку системы
- Подготовить систему к работе

---

## 1. Подготовка к установке

### 1.1 Загрузка образа

Официальные образы доступны на [www.openbsd.org](https://www.openbsd.org/faq/faq4.html#Download).

```sh
# Скачивание install образа для amd64 (версия 7.4)
$ curl -O https://cdn.openbsd.org/pub/OpenBSD/7.4/amd64/install74.img

# Или через ftp (встроенный в OpenBSD)
$ ftp https://cdn.openbsd.org/pub/OpenBSD/7.4/amd64/install74.img

```

**Типы образов:**

| Файл | Описание | Размер |
|------|----------|--------|
| `install74.img` | USB-образ для установки | ~650 MB |
| `install74.iso` | ISO для CD/виртуализации | ~650 MB |
| `miniroot74.img` | Минимальный сетевой образ | ~7 MB |
| `cd74.iso` | Только загрузчик (сетевая установка) | ~500 KB |

### 1.2 Проверка целостности

OpenBSD подписывает все образы криптографически.

```sh
# Скачать файл с контрольными суммами
$ curl -O https://cdn.openbsd.org/pub/OpenBSD/7.4/amd64/SHA256

# Проверить контрольную сумму
$ sha256 install74.img
SHA256 (install74.img) = abc123...

# Сравнить с файлом SHA256
$ grep install74.img SHA256
SHA256 (install74.img) = abc123...

```

> **🔒 Security:**  
> Всегда проверяйте контрольные суммы! Это защищает от повреждённых или модифицированных образов.

### 1.3 Создание загрузочного USB

**На OpenBSD/Linux:**

```sh
# Определить устройство USB (ОСТОРОЖНО!)
$ dmesg | tail
sd1 at scsibus2 targ 1 lun 0: <USB, Flash Drive, 1.00>

# Записать образ (замените sd1 на ваше устройство!)
# doas dd if=install74.img of=/dev/rsd1c bs=1M
```

**На macOS:**

```sh
# Найти диск
$ diskutil list

# Отмонтировать
$ diskutil unmountDisk /dev/disk2

# Записать образ
$ sudo dd if=install74.img of=/dev/rdisk2 bs=1m

```

> **⚠️ Warning:**  
> Команда `dd` перезапишет все данные на диске! Убедитесь, что указали правильное устройство.

### 1.4 Подготовка виртуальной машины

**VirtualBox:**

```sh
# Создание VM
VBoxManage createvm --name "OpenBSD" --ostype OpenBSD_64 --register

# Настройка параметров
VBoxManage modifyvm "OpenBSD" --memory 2048 --cpus 2
VBoxManage modifyvm "OpenBSD" --nic1 bridged --bridgeadapter1 en0

# Создание диска
VBoxManage createhd --filename OpenBSD.vdi --size 20480

# Подключение диска и ISO
VBoxManage storagectl "OpenBSD" --name "SATA" --add sata
VBoxManage storageattach "OpenBSD" --storagectl "SATA" --port 0 --type hdd --medium OpenBSD.vdi
VBoxManage storageattach "OpenBSD" --storagectl "SATA" --port 1 --type dvddrive --medium install74.iso

```

**QEMU/KVM:**

```sh
# Создание диска
qemu-img create -f qcow2 openbsd.qcow2 20G

# Запуск установки
qemu-system-x86_64 \
    -enable-kvm \
    -m 2048 \
    -cpu host \
    -smp 2 \
    -cdrom install74.iso \
    -drive file=openbsd.qcow2,format=qcow2 \
    -boot d

```

---

## 2. Процесс установки

### 2.1 Загрузка установщика

При загрузке вы увидите:

```

>> OpenBSD/amd64 BOOT 3.52
boot>

```

Просто нажмите Enter для продолжения. Через несколько секунд появится:

```

Welcome to the OpenBSD/amd64 7.4 installation program.
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell?

```

Введите `I` для новой установки.

### 2.2 Базовая конфигурация

**Раскладка клавиатуры:**

```

Choose your keyboard layout ('?' or 'L' for list) [default]

```

Для русской раскладки введите `ru`, для стандартной US — просто Enter.

**Имя хоста:**

```

System hostname? (short form, e.g. 'foo') puffy

```

Введите короткое имя, например `puffy` или `server1`.

### 2.3 Настройка сети

```

Available network interfaces are: em0 vlan0
Which network interface do you wish to configure? (or 'done') [em0]

```

**Автоматическая настройка (DHCP):**

```

IPv4 address for em0? (or 'autoconf' or 'none') [autoconf]

```

**Статический IP:**

```

IPv4 address for em0? (or 'autoconf' or 'none') 192.168.1.100
Netmask for em0? [255.255.255.0]

```

**DNS и шлюз:**

```

Default IPv4 route? (IPv4 address or 'none') 192.168.1.1
DNS domain name? (e.g. 'example.com') [my.domain] home.local
DNS nameservers? (IP address list or 'none') [none] 8.8.8.8 1.1.1.1

```

### 2.4 Пароль root

```

Password for root account? (will not echo)
Password for root account? (again)

```

> **🔒 Security:**  
> Используйте сложный пароль! Минимум 12 символов, буквы, цифры, спецсимволы.

### 2.5 Запуск sshd

```

Start sshd(8) by default? [yes]

```

Ответьте `yes` для удалённого доступа.

### 2.6 X Window System

```

Do you expect to run the X Window System? [yes]

```

- `yes` — если планируете графический интерфейс
- `no` — для сервера без GUI

### 2.7 Создание пользователя

```

Setup a user? (enter a lower-case loginname, or 'no') [no] admin
Full name for user admin? [admin] System Administrator
Password for user admin? (will not echo)

```

> **💡 Pro Tip:**  
> Всегда создавайте обычного пользователя! Работа от root — плохая практика.

### 2.8 Разрешить root SSH

```

Allow root ssh login? (yes, no, prohibit-password) [no]

```

- `no` — рекомендуется (входить через обычного пользователя, затем `doas`)
- `prohibit-password` — только по ключам
- `yes` — не рекомендуется

---

## 3. Разбиение диска

### 3.1 Выбор диска

```

Available disks are: sd0 sd1
Which disk is the root disk? ('?' for details) [sd0]

```

Введите `?` для просмотра информации о дисках:

```

sd0: NVMe, SAMSUNG, 1TB (1953525168 512-byte sectors)
sd1: USB, Flash, 32GB (62533296 512-byte sectors)

```

### 3.2 Инициализация диска

```

Use (W)hole disk MBR, whole disk (G)PT, (O)penBSD area, or (E)dit? [GPT]

```

- **GPT** — рекомендуется для UEFI и дисков >2TB

- **MBR** — для старых систем с BIOS

- **OpenBSD area** — если уже есть разделы других ОС

### 3.3 Схема разделов

```

Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a]

```

**Auto layout** создаст стандартную схему:

```

/dev/sd0a    /           1G
/dev/sd0b    swap        RAM * 2
/dev/sd0d    /tmp        2G
/dev/sd0e    /var        4G
/dev/sd0f    /usr        4G
/dev/sd0g    /usr/X11R6  1G
/dev/sd0h    /usr/local  4G
/dev/sd0i    /usr/src    2G
/dev/sd0j    /usr/obj    4G
/dev/sd0k    /home       остаток

```

### 3.4 Кастомная разметка

Для ручной настройки выберите `C`:

```

Label editor (enter '?' for help at any prompt)
sd0>

```

Полезные команды в редакторе:

| Команда | Описание |
|---------|----------|
| `p` | Показать разделы |
| `p M` | Показать в мегабайтах |
| `a` | Добавить раздел |
| `d X` | Удалить раздел X |
| `R` | Восстановить авто-разметку |
| `w` | Записать изменения |
| `q` | Выйти |

**Пример создания раздела:**

```

sd0> a a
offset: [64]
size: [1953525104] 2G
FS type: [4.2BSD]
mount point: [none] /
sd0*> w
sd0> q

```

### 3.5 Рекомендуемая схема для сервера

```

Раздел    Точка монтирования    Размер    Назначение
───────────────────────────────────────────────────────
a         /                     2G        Корневая система
b         swap                  2G        Подкачка
d         /tmp                  2G        Временные файлы
e         /var                  10G       Логи, почта, базы
f         /usr                  6G        Системные программы
g         /usr/local            10G       Пакеты
h         /home                 остаток   Данные пользователей

```

> **💡 Pro Tip:**  
> Отдельные разделы с `nodev,nosuid` повышают безопасность. OpenBSD автоматически применяет эти флаги.

---

## 4. Выбор наборов файлов

### 4.1 Источник установки

```

Location of sets? (cd0 disk http nfs or 'done') [cd0]

```

- **cd0** — с CD/DVD или ISO

- **disk** — с USB или другого диска

- **http** — из интернета (медленнее, но свежее)

### 4.2 Наборы файлов (Sets)

```

Set name(s)? (or 'abort' or 'done') [done]

    [X] bsd           - ядро
    [X] bsd.mp        - многопроцессорное ядро
    [X] bsd.rd        - ramdisk ядро для восстановления
    [X] base74.tgz    - базовая система
    [X] comp74.tgz    - компилятор и инструменты разработки
    [X] man74.tgz     - man-страницы
    [X] game74.tgz    - игры (fortune, tetris...)
    [ ] xbase74.tgz   - базовая X Window System
    [ ] xfont74.tgz   - шрифты для X
    [ ] xserv74.tgz   - X сервер
    [ ] xshare74.tgz  - общие файлы X

Set name(s)? (or 'abort' or 'done') [done]

```

**Минимальный сервер:**

- bsd, bsd.mp, bsd.rd, base74.tgz, man74.tgz

**Рабочая станция:**

- Все наборы включая x*

```
# Убрать ненужные наборы
Set name(s)? -game74.tgz -x*

# Добавить нужные
Set name(s)? +xbase74.tgz

```

### 4.3 Процесс установки

```

Installing bsd          100% |**************************|  24.2 MB    00:02
Installing bsd.mp       100% |**************************|  24.3 MB    00:02
Installing bsd.rd       100% |**************************|  4.39 MB    00:00
Installing base74.tgz   100% |**************************|   297 MB    00:45
Installing comp74.tgz   100% |**************************|  74.2 MB    00:12
Installing man74.tgz    100% |**************************|  8.92 MB    00:01

```

---

## 5. Завершение установки

### 5.1 Часовой пояс

```

What timezone are you in? ('?' for list) [US/Eastern]

```

Для России:

- `Europe/Moscow` — Москва
- `Asia/Yekaterinburg` — Екатеринбург
- `Asia/Novosibirsk` — Новосибирск
- `Asia/Vladivostok` — Владивосток

```

What timezone are you in? Europe/Moscow

```

### 5.2 Завершающие шаги

```

Saving configuration files... done.
Making all device nodes... done.
Multiprocessor machine; using bsd.mp instead of bsd.

CONGRATULATIONS! Your OpenBSD install has been successfully completed!

When you login to your new system the first time, please read your mail
using the 'mail' command.

Exit to (S)hell, (H)alt or (R)eboot? [reboot]

```

Выберите `R` для перезагрузки.

---

## 6. Первый вход в систему

### 6.1 Загрузка системы

После перезагрузки вы увидите:

```

>> OpenBSD/amd64 BOOT 3.52
boot>
booting hd0a:/bsd: ...

```

Затем приглашение входа:

```

OpenBSD/amd64 (puffy.home.local) (ttyC0)

login:
```

### 6.2 Чтение системной почты

После первого входа прочитайте системное сообщение:

```sh

$ mail
Mail version 8.1.2 01/15/2001.  Type ? for help.
"/var/mail/root": 1 message 1 new
>N  1 root@puffy.home.local  Mon Dec  1 12:00   18/661   Welcome to OpenBSD

& 1

```

Это письмо содержит важную информацию о системе.

### 6.3 Команда afterboot

Самый важный man после установки:

```sh

$ man afterboot

```

Этот документ описывает все шаги для настройки системы.

---

## 7. Первоначальная настройка

### 7.1 Обновление системы

```sh
# Проверить наличие патчей безопасности
# doas syspatch

Checking for available patches... done.
Installing patch 001_wifi... done.
Installing patch 002_libcrypto... done.
Relinking to create unique kernel... done.

```

> **⚠️ Warning:**  
> Всегда устанавливайте патчи безопасности сразу после установки!

### 7.2 Настройка doas

`doas` — аналог `sudo` в OpenBSD:

```sh
# Создать конфигурацию doas
# echo "permit persist :wheel" > /etc/doas.conf
```

Теперь пользователи группы `wheel` могут выполнять команды от root:

```sh

$ doas whoami
Password:
root

```

**Полезные настройки doas.conf:**

```sh
# Пользователи wheel могут выполнять любые команды
permit persist :wheel

# Конкретному пользователю без пароля для определённых команд
permit nopass admin cmd /sbin/reboot
permit nopass admin cmd /sbin/halt

# Сохранять переменные окружения
permit persist keepenv :wheel

```

### 7.3 Настройка пакетного менеджера

```sh
# Установить зеркало для pkg_add
# echo "https://cdn.openbsd.org/pub/OpenBSD" > /etc/installurl

# Или ближайшее зеркало
# echo "https://ftp.eu.openbsd.org/pub/OpenBSD" > /etc/installurl
```

### 7.4 Установка базовых пакетов

```sh
# Обновить список пакетов и установить базовые утилиты
# doas pkg_add vim nano htop git curl wget

quirks-7.14 signed on 2023-10-05T12:00:00Z
vim-9.0.1897-no_x11: ok
nano-7.2: ok
htop-3.2.2: ok
git-2.42.0: ok
curl-8.4.0: ok
wget-1.21.4: ok

```

---

## 8. Настройка SSH

### 8.1 Генерация ключей

```sh
# На клиентской машине (не на сервере)
$ ssh-keygen -t ed25519 -C "admin@workstation"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/admin/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Your public key has been saved in /home/admin/.ssh/id_ed25519.pub

```

### 8.2 Копирование ключа на сервер

```sh
# Скопировать ключ на OpenBSD сервер
$ ssh-copy-id admin@192.168.1.100

# Или вручную
$ cat ~/.ssh/id_ed25519.pub | ssh admin@192.168.1.100 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

```

### 8.3 Усиление безопасности SSH

Отредактируйте `/etc/ssh/sshd_config`:

```sh
# doas vim /etc/ssh/sshd_config

# Запретить вход root
PermitRootLogin no

# Только аутентификация по ключам
PasswordAuthentication no
PubkeyAuthentication yes

# Ограничить попытки входа
MaxAuthTries 3

# Отключить X11 forwarding если не нужен
X11Forwarding no

```

Перезапустить sshd:

```sh
# doas rcctl restart sshd
sshd(ok)
sshd(ok)

```

---

## 9. Troubleshooting установки

### 9.1 Не загружается с USB

**Проблема:** BIOS не видит USB

**Решение:**

- Включите USB boot в BIOS
- Попробуйте другой USB-порт (USB 2.0)
- Используйте ISO и виртуальный CD

### 9.2 Не определяется сеть

```sh
# Проверить доступные интерфейсы
$ ifconfig

# Посмотреть сообщения ядра о сети
$ dmesg | grep -i net

```

Если сетевая карта не определилась:

- Проверьте совместимость на [supported hardware](https://www.openbsd.org/amd64.html)
- Попробуйте другую сетевую карту

### 9.3 Нет места на диске после установки

```sh
# Проверить использование
$ df -h
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/sd0a      1.0G    890M    60M    94%    /

# Решение: при установке выбрать кастомную разметку
# с большими разделами
```

### 9.4 Забыл пароль root

1. Загрузитесь с установочного носителя
2. Выберите `(S)hell`
3. Смонтируйте корневой раздел:

```sh
# mount /dev/sd0a /mnt
# chroot /mnt
# passwd root
# exit
# reboot
```

---

## 10. Установка на специфические платформы

### 10.1 Raspberry Pi (arm64)

```sh
# Скачать образ для arm64
$ curl -O https://cdn.openbsd.org/pub/OpenBSD/7.4/arm64/miniroot74.img

# Записать на SD карту
$ dd if=miniroot74.img of=/dev/sdX bs=1M

```

### 10.2 AWS/Cloud

OpenBSD доступен как AMI в AWS:

- Используйте официальные AMI от OpenBSD
- Или создайте свой образ с помощью `installimage`

### 10.3 Dual Boot с Linux/Windows

```
# При разметке диска выберите:
Use (W)hole disk MBR, whole disk (G)PT, (O)penBSD area, or (E)dit? O

# Это установит OpenBSD в существующий раздел
# без удаления других ОС
```

---

## 💡 Key Takeaways

- **Проверяйте образы**: Всегда проверяйте SHA256 перед установкой

- **syspatch сразу**: Первое действие после установки — `syspatch`

- **Отдельные разделы**: Обеспечивают безопасность и удобство обслуживания

- **doas вместо sudo**: Простой и безопасный способ получить права root

- **man afterboot**: Обязательно прочитайте после установки

---

## 🚀 Next Steps

**Related Modules:**

- [Basic Commands](../03_BasicCommands/) — изучите базовые команды
- [Package Management](../06_PackageManagement/) — установка программ

**Practice Ideas:**

1. Установите OpenBSD в виртуальной машине
2. Попробуйте разные схемы разбиения диска
3. Настройте SSH-доступ по ключам
4. Выполните `syspatch` и перезагрузите систему

**Going Deeper:**

- Автоматическая установка через autoinstall
- PXE boot и сетевая установка
- Создание собственного установочного образа

---

## 📚 Additional Resources

**Documentation:**

- [OpenBSD FAQ 4](https://www.openbsd.org/faq/faq4.html) — подробное руководство по установке
- [man afterboot](https://man.openbsd.org/afterboot) — что делать после установки
- [man install](https://man.openbsd.org/install) — процесс установки

**Hardware Compatibility:**

- [amd64 Platform](https://www.openbsd.org/amd64.html)
- [arm64 Platform](https://www.openbsd.org/arm64.html)

---




