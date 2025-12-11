# File System
## Файловая система OpenBSD: FFS, разделы и права доступа

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [Basic Commands](../03_BasicCommands/)
- Понимать иерархию каталогов Unix
- Знать базовые команды работы с файлами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру файловой системы FFS
- Работать с разделами и точками монтирования
- Настраивать fstab для автоматического монтирования
- Управлять правами доступа и специальными битами
- Использовать softraid для шифрования и RAID
- Проверять и восстанавливать файловые системы

---

## 1. Файловая система FFS

### 1.1 Что такое FFS

**FFS** (Fast File System) — файловая система BSD, используемая в OpenBSD. Текущая версия — **FFS2**.

```sh
# Проверить тип файловой системы
$ mount | grep ffs
/dev/sd0a on / type ffs (local)
/dev/sd0d on /home type ffs (local, nodev, nosuid)

```

**Output:**
```

/dev/sd0a on / type ffs (local)
/dev/sd0d on /home type ffs (local, nodev, nosuid)

```

Характеристики FFS:

- **Soft Updates** — целостность данных без журнала

- **Высокая надёжность** — проверенная временем

- **Простота** — легко восстановить при проблемах

- **Нет фрагментации** — благодаря cylinder groups

### 1.2 Структура FFS

```

┌─────────────────────────────────────────────────────┐
│ Boot Block │ Superblock │ Cylinder Groups...        │
└─────────────────────────────────────────────────────┘

Cylinder Group:
┌────────────┬────────────┬─────────────┬─────────────┐
│ Copy of    │ Cylinder   │ Inode       │ Data        │
│ Superblock │ Group      │ Bitmap &    │ Blocks      │
│            │ Summary    │ Inodes      │             │
└────────────┴────────────┴─────────────┴─────────────┘

```

### 1.3 Inodes

Каждый файл имеет **inode** — структуру с метаданными:

```sh
# Просмотр inode
$ ls -i /etc/passwd
98304 /etc/passwd

# Подробная информация об inode
$ stat /etc/passwd
  File: /etc/passwd
  Size: 1843       Blocks: 8          IO Block: 16384  regular file
Device: 0,0        Inode: 98304       Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/   wheel)
Access: 2023-12-01 10:00:00.000000000 +0300
Modify: 2023-11-15 14:30:00.000000000 +0300
Change: 2023-11-15 14:30:00.000000000 +0300

```

**Output:**
```

  File: /etc/passwd
  Size: 1843       Blocks: 8          IO Block: 16384  regular file
Device: 0,0        Inode: 98304       Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/   wheel)

```

---

## 2. Иерархия файловой системы

### 2.1 Структура каталогов OpenBSD

```sh

$ man hier

/           корневой каталог
├── bin/    основные пользовательские утилиты
├── sbin/   основные системные утилиты
├── etc/    конфигурационные файлы
│   ├── rc.d/       скрипты служб
│   ├── mail/       конфигурация почты
│   └── ssh/        конфигурация SSH
├── dev/    файлы устройств
├── home/   домашние каталоги пользователей
├── root/   домашний каталог root
├── tmp/    временные файлы
├── var/    изменяемые данные
│   ├── log/        логи
│   ├── mail/       почтовые ящики
│   ├── run/        PID файлы
│   └── db/         базы данных
├── usr/    вторичная иерархия
│   ├── bin/        пользовательские утилиты
│   ├── sbin/       системные утилиты
│   ├── lib/        библиотеки
│   ├── include/    заголовочные файлы
│   ├── share/      архитектурно-независимые данные
│   │   └── man/    man-страницы
│   ├── local/      локально установленное ПО (пакеты)
│   ├── src/        исходный код системы
│   ├── obj/        объектные файлы компиляции
│   └── X11R6/      X Window System
└── altroot/ альтернативный корень (для восстановления)

```

### 2.2 Особенности каталогов

| Каталог | Назначение | Особенности |
|---------|------------|-------------|
| `/etc` | Конфигурация | Только локальные настройки |
| `/usr/local` | Пакеты | pkg_add устанавливает сюда |
| `/var` | Изменяемые данные | Логи, базы, почта |
| `/tmp` | Временные файлы | Очищается при перезагрузке |
| `/home` | Пользователи | Обычно nodev, nosuid |

---

## 3. Разделы и точки монтирования

### 3.1 Схема именования дисков

```sh
# Формат: sdXY
# X - номер диска (0, 1, 2...)
# Y - раздел (a, b, c, d...)

sd0     # первый диск целиком (raw)
sd0a    # раздел a (обычно /)
sd0b    # раздел b (обычно swap)
sd0c    # весь диск (для разметки)
sd0d    # раздел d (обычно /home)

```

**Стандартное назначение разделов:**

| Раздел | Точка монтирования | Назначение |
|--------|-------------------|------------|
| a | / | Корень |
| b | swap | Подкачка |
| c | — | Весь диск (не используется) |
| d | /tmp или /home | Временные или домашние |
| e | /var | Логи, почта |
| f | /usr | Системные программы |
| g | /usr/X11R6 | X Window |
| h | /usr/local | Пакеты |
| i | /usr/src | Исходники |
| j | /usr/obj | Объектные файлы |
| k+ | /home | Данные пользователей |

### 3.2 Просмотр разделов

```sh
# Список разделов диска
$ disklabel sd0
# /dev/rsd0c:
type: SCSI
disk: SCSI disk
label: SAMSUNG
duid: abcd1234567890ef
flags:
bytes/sector: 512
sectors/track: 63
tracks/cylinder: 255
sectors/cylinder: 16065
cylinders: 60801
total sectors: 976773168
boundstart: 64
boundend: 976773104

16 partitions:
#                size           offset  fstype [fsize bsize   cpg]
  a:          4194304               64  4.2BSD   2048 16384 12960
  b:          4194304          4194368    swap
  c:        976773168                0  unused
  d:          8388608          8388672  4.2BSD   2048 16384 12960
  e:         16777216         16777280  4.2BSD   2048 16384 12960
  f:         12582912         33554496  4.2BSD   2048 16384 12960
  g:          4194304         46137408  4.2BSD   2048 16384 12960
  h:         16777216         50331712  4.2BSD   2048 16384 12960
  k:        909663376         67108928  4.2BSD   4096 32768 26062

```

### 3.3 Редактирование разделов

```sh
# Редактировать разметку диска (ОСТОРОЖНО!)
# doas disklabel -E sd0

# Интерактивные команды:
# p    - показать разделы
# a    - добавить раздел
# d X  - удалить раздел X
# w    - записать изменения
# q    - выйти
```

> **⚠️ Warning:**  
> Изменение разделов на активном диске может привести к потере данных!

---

## 4. Монтирование файловых систем

### 4.1 Команда mount

```sh
# Показать смонтированные файловые системы
$ mount
/dev/sd0a on / type ffs (local)
/dev/sd0d on /home type ffs (local, nodev, nosuid)
/dev/sd0e on /var type ffs (local, nodev, nosuid)

# Смонтировать раздел
# doas mount /dev/sd1a /mnt

# Смонтировать с опциями
# doas mount -o nodev,nosuid /dev/sd1a /mnt

# Смонтировать только для чтения
# doas mount -r /dev/sd1a /mnt
```

### 4.2 Файл /etc/fstab

Конфигурация автоматического монтирования:

```sh

$ cat /etc/fstab
# Device         Mountpoint   FStype  Options          Dump  Pass
abcd1234.a       /            ffs     rw               1     1
abcd1234.b       none         swap    sw               0     0
abcd1234.d       /home        ffs     rw,nodev,nosuid  1     2
abcd1234.e       /var         ffs     rw,nodev,nosuid  1     2
abcd1234.f       /usr         ffs     rw,nodev         1     2
abcd1234.g       /usr/X11R6   ffs     rw,nodev         1     2
abcd1234.h       /usr/local   ffs     rw,wxallowed,nodev  1  2

```

**Поля fstab:**

| Поле | Описание |
|------|----------|
| Device | DUID.partition или /dev/sdXY |
| Mountpoint | Точка монтирования |
| FStype | Тип файловой системы (ffs, swap, nfs) |
| Options | Опции монтирования |
| Dump | Для dump (0 или 1) |
| Pass | Порядок fsck (0, 1, 2) |

### 4.3 Опции монтирования

| Опция | Описание |
|-------|----------|
| `rw` | Чтение и запись |
| `ro` | Только чтение |
| `nodev` | Игнорировать файлы устройств |
| `nosuid` | Игнорировать setuid/setgid |
| `noexec` | Запретить выполнение |
| `wxallowed` | Разрешить W+X память (для /usr/local) |
| `softdep` | Soft Updates (по умолчанию) |

### 4.4 DUID

OpenBSD использует **DUID** (Disk UID) вместо /dev/sdX:

```sh
# Узнать DUID диска
$ sysctl hw.disknames
hw.disknames=sd0:abcd1234567890ef,sd1:1234567890abcdef

# В fstab используется формат:
# DUID.partition
abcd1234567890ef.a    /    ffs    rw    1    1

```

> **💡 Pro Tip:**  
> DUID не изменяется при переключении портов или добавлении дисков, в отличие от /dev/sdX.

---

## 5. Права доступа (подробно)

### 5.1 Стандартные права

```

-rwxr-xr-x  1 root  wheel  12345  Dec  1 10:00  file
 │││ │││ │││
 │││ │││ └── права для others (остальные)
 │││ └── права для group (группа)
 └── права для user (владелец)

r = read  (4)
w = write (2)
x = execute (1)

```

### 5.2 Специальные биты

**setuid (4000)** — выполняется от имени владельца:

```sh

$ ls -l /usr/bin/passwd
-r-sr-xr-x  1 root  bin  40960 Oct  9 13:57 /usr/bin/passwd
#    ^
#    s = setuid

# Установить setuid
# doas chmod u+s program
# doas chmod 4755 program
```

**setgid (2000)** — выполняется от имени группы:

```sh

$ ls -l /usr/bin/mail
-r-xr-sr-x  1 root  mail  123456 Oct  9 13:57 /usr/bin/mail
#       ^
#       s = setgid

# Установить setgid
# doas chmod g+s program
# doas chmod 2755 program
```

**sticky bit (1000)** — только владелец может удалять:

```sh

$ ls -ld /tmp
drwxrwxrwt  8 root  wheel  512 Dec  1 10:00 /tmp
#        ^
#        t = sticky bit

# Установить sticky
# doas chmod +t directory
# doas chmod 1777 directory
```

### 5.3 umask

Маска для прав новых файлов:

```sh
# Показать текущую umask
$ umask
022

# Права по умолчанию:
# Файлы:    666 - 022 = 644 (rw-r--r--)
# Каталоги: 777 - 022 = 755 (rwxr-xr-x)

# Установить более строгую маску
$ umask 077
# Файлы:    666 - 077 = 600 (rw-------)
# Каталоги: 777 - 077 = 700 (rwx------)
```

Для постоянной umask добавьте в `~/.profile`:

```sh

umask 077

```

### 5.4 Флаги файлов (chflags)

OpenBSD поддерживает дополнительные флаги:

```sh
# Просмотр флагов
$ ls -lo /bsd
-r-xr-xr-x  1 root  wheel  - 24789504 Oct  9 13:57 /bsd

# Установить immutable (только root может снять)
# doas chflags schg /etc/passwd

# Просмотр флагов
$ ls -lo /etc/passwd
-r--r--r--  1 root  wheel  schg 1843 Nov 15 14:30 /etc/passwd

# Снять флаг
# doas chflags noschg /etc/passwd
```

**Полезные флаги:**

| Флаг | Описание |
|------|----------|
| `schg` | Системный immutable (root only) |
| `uchg` | Пользовательский immutable |
| `sappnd` | Только добавление (для логов) |
| `nodump` | Не включать в dump |

---

## 6. Softraid

### 6.1 Что такое Softraid

**Softraid** — программный RAID и шифрование в OpenBSD.

```sh
# Модули softraid
$ dmesg | grep softraid
softraid0 at root

```

### 6.2 Шифрование диска

```sh
# Создать зашифрованный том
# doas bioctl -c C -l sd1a softraid0
New passphrase:
Re-type passphrase:
softraid0: CRYPTO volume attached as sd2

# Теперь sd2 — расшифрованный диск
# Разметить и использовать как обычно
# doas fdisk -iy sd2
# doas disklabel -E sd2
# doas newfs sd2a
# doas mount /dev/sd2a /mnt
```

### 6.3 RAID уровни

```sh
# RAID 1 (зеркало)
# doas bioctl -c 1 -l sd1a,sd2a softraid0

# RAID 0 (страйп) - НЕ рекомендуется
# doas bioctl -c 0 -l sd1a,sd2a softraid0

# RAID 5
# doas bioctl -c 5 -l sd1a,sd2a,sd3a softraid0
```

### 6.4 Управление Softraid

```sh
# Просмотр состояния
# doas bioctl softraid0
Volume      Status               Size Device
softraid0 0  Online (auto_assemble)  500G sd2 CRYPTO

# Отключить том
# doas bioctl -d sd2
```

---

## 7. Проверка файловой системы

### 7.1 fsck

```sh
# Проверка файловой системы (размонтированной!)
# doas fsck /dev/sd0a

# Автоматическое исправление
# doas fsck -y /dev/sd0a

# Проверка всех файловых систем при загрузке
# В fstab поле Pass: 1 для /, 2 для остальных
```

### 7.2 При проблемах загрузки

Если система не загружается из-за ошибок FS:

```sh
# Boot в single-user mode
boot> boot -s

# Смонтировать корень для записи
# mount -uw /

# Проверить файловые системы
# fsck -y

# Перезагрузить
# reboot
```

### 7.3 df и du

```sh
# Использование разделов
$ df -h
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/sd0a      2.0G    890M    1.0G    47%    /
/dev/sd0d      4.0G    2.1G    1.7G    55%    /home
/dev/sd0e      8.0G    234M    7.4G     3%    /var

# Использование каталогов
$ du -sh /var/*
1.2M    /var/cache
234M    /var/log
12K     /var/mail

# Найти большие файлы
$ du -a /var | sort -rn | head -10

```

---

## 8. Монтирование внешних носителей

### 8.1 USB-накопители

```sh
# Подключить USB и посмотреть сообщения
$ dmesg | tail
sd1 at scsibus2 targ 1 lun 0: <USB, Flash Drive, 1.00>
sd1: 32768MB, 512 bytes/sector

# Посмотреть разделы
$ disklabel sd1

# Смонтировать (обычно раздел i для FAT32)
# doas mount /dev/sd1i /mnt

# Для NTFS (только чтение без пакета ntfs-3g)
# doas mount -t ntfs /dev/sd1i /mnt
```

### 8.2 CD/DVD

```sh
# Смонтировать CD
# doas mount /dev/cd0a /mnt

# Размонтировать и извлечь
# doas umount /mnt
# doas eject cd0
```

### 8.3 NFS

```sh
# Клиент NFS
# doas mount -t nfs server:/export /mnt

# Для автомонтирования в fstab:
server:/export    /mnt    nfs    rw    0    0

```

### 8.4 tmpfs

Файловая система в памяти:

```sh
# Смонтировать tmpfs (128MB)
# doas mount -t tmpfs -o size=128M tmpfs /mnt/ramdisk

# В fstab:
swap    /mnt/ramdisk    tmpfs    rw,nodev,nosuid,size=128M    0    0

```

---

## 9. Практические примеры

### 9.1 Добавление нового диска

```sh
# 1. Инициализировать диск
# doas fdisk -iy sd1

# 2. Создать разделы
# doas disklabel -E sd1
> a a
offset: [64]
size: [976773104]
FS type: [4.2BSD]
mount point: [none] /data
> w
> q

# 3. Создать файловую систему
# doas newfs sd1a

# 4. Создать точку монтирования
# doas mkdir /data

# 5. Добавить в fstab
# echo "sd1a /data ffs rw,nodev,nosuid 1 2" | doas tee -a /etc/fstab

# 6. Смонтировать
# doas mount /data
```

### 9.2 Расширение файловой системы

```sh
# FFS можно расширить онлайн
# doas growfs sd0k

# Или после изменения размера раздела
# doas disklabel -E sd0  # увеличить раздел
# doas growfs sd0k
```

### 9.3 Создание зашифрованного /home

```sh
# При установке или после:
# 1. Создать шифрованный том
# doas bioctl -c C -l sd0k softraid0

# 2. Создать файловую систему
# doas newfs sd2a

# 3. Перенести данные
# doas mount /dev/sd2a /mnt
# doas cp -rp /home/* /mnt/
# doas umount /home
# doas mount /dev/sd2a /home

# 4. Обновить fstab
```

---

## 💡 Key Takeaways

- **FFS надёжен**: Проверенная временем файловая система с Soft Updates

- **DUID лучше /dev**: Используйте DUID в fstab для стабильности

- **nodev, nosuid**: Всегда используйте на /home, /tmp, /var

- **Softraid**: Встроенное шифрование и RAID без сторонних инструментов

- **fsck**: Регулярно проверяйте при проблемах, но на размонтированных FS

---

## 🚀 Next Steps

**Related Modules:**

- [User Management](../05_UserManagement/) — управление пользователями
- [Security](../10_Security/) — безопасность и шифрование

**Practice Ideas:**

1. Добавьте второй диск и настройте автомонтирование
2. Создайте зашифрованный раздел с softraid
3. Настройте tmpfs для /tmp
4. Изучите вывод `df -h` и найдите, что занимает место

**Going Deeper:**

- Изучите dump/restore для резервного копирования
- Настройте NFS-сервер
- Разберитесь с softraid RAID5 для отказоустойчивости

---

## 📚 Additional Resources

**Documentation:**

- [man ffs](https://man.openbsd.org/ffs) — файловая система FFS
- [man mount](https://man.openbsd.org/mount) — монтирование
- [man disklabel](https://man.openbsd.org/disklabel) — разметка дисков
- [man bioctl](https://man.openbsd.org/bioctl) — управление softraid
- [OpenBSD FAQ 14](https://www.openbsd.org/faq/faq14.html) — работа с дисками

---




