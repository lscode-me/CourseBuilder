# System Administration
## Системное администрирование OpenBSD

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти все предыдущие модули курса
- Иметь работающую систему OpenBSD
- Понимать службы, сеть и безопасность

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Мониторить состояние системы
- Анализировать логи и устранять проблемы
- Выполнять резервное копирование
- Планировать задачи с cron
- Обновлять систему и патчи безопасности
- Настраивать мониторинг и оповещения

---

## 1. Мониторинг системы

### 1.1 Общая информация

```sh
# Информация о системе
$ uname -a
OpenBSD server.home.local 7.4 GENERIC.MP#0 amd64

# Uptime и нагрузка
$ uptime
10:30AM  up 15 days,  3:45, 2 users, load averages: 0.08, 0.03, 0.01

# Версия системы
$ sysctl kern.version
kern.version=OpenBSD 7.4 (GENERIC.MP) #0: Mon Oct  9 13:57:11 MDT 2023
```

### 1.2 Память и процессы

```sh
# Память
$ vmstat
 procs    memory       page                    disks    traps          cpu
 r   s   avm     fre  flt  re  pi  po  fr  sr sd0 sd1  int   sys   cs us sy id
 0  28  234M   7098M   12   0   0   0   0   0   0   0   47   127   89  0  0 100

# Подробнее о памяти
$ top -S
Memory: Real: 234M/993M act/tot Free: 7098M Cache: 404M Swap: 0/2048M

# Процессы (top)
$ top
load averages:  0.08,  0.03,  0.01    server.home.local 10:30:15
26 processes: 25 idle, 1 on processor
CPU:  0.2% user,  0.0% nice,  0.4% sys,  0.0% spin,  0.0% intr, 99.4% idle

# Процессы (ps)
$ ps auxww
USER     PID %CPU %MEM   VSZ   RSS TT  STAT   STARTED       TIME COMMAND
root       1  0.0  0.0   524   488 ??  Is   Sun10AM     0:00.02 /sbin/init
```

### 1.3 Диски

```sh
# Использование дисков
$ df -h
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/sd0a      2.0G    890M    1.0G    47%    /
/dev/sd0d      4.0G    2.1G    1.7G    55%    /home

# Подробная статистика дисков
$ iostat
      tty              sd0              sd1             cpu
 tin  tout  KB/t  t/s  MB/s   KB/t  t/s  MB/s  us ni sy sp in id
   0    33  16.0    1  0.02    0.0    0  0.00   0  0  0  0  0 100

# S.M.A.R.T. статус
# doas smartctl -a /dev/sd0
```

### 1.4 Сеть

```sh
# Сетевые соединения
$ netstat -an
Active Internet connections (including servers)
Proto   Recv-Q Send-Q  Local Address          Foreign Address        State
tcp          0      0  192.168.1.100.22       192.168.1.50.54321     ESTABLISHED

# Статистика интерфейсов
$ netstat -i
Name    Mtu   Network     Address              Ipkts Ierrs    Opkts Oerrs  Coll
em0     1500  <Link>      00:11:22:33:44:55  1234567     0   987654     0     0

# Трафик в реальном времени
$ systat netstat
```

### 1.5 systat — интерактивный мониторинг

```sh
# Различные представления
$ systat vmstat    # память и CPU
$ systat iostat    # диски
$ systat netstat   # сеть
$ systat pigs      # процессы по CPU
$ systat mbufs     # сетевые буферы
$ systat sensors   # датчики температуры
```

---

## 2. Работа с логами

### 2.1 Основные логи

| Файл | Содержимое |
|------|------------|
| `/var/log/messages` | Общие системные сообщения |
| `/var/log/daemon` | Сообщения демонов |
| `/var/log/authlog` | Аутентификация |
| `/var/log/secure` | Безопасность |
| `/var/log/maillog` | Почта |
| `/var/log/pflog` | Файрвол PF |

### 2.2 Просмотр логов

```sh
# Последние сообщения
$ tail -f /var/log/messages

# Ошибки за сегодня
$ grep -i error /var/log/messages | tail -50

# Неудачные входы
$ grep -i "failed\|invalid" /var/log/authlog

# Логи по времени
$ grep "Dec  1 10:" /var/log/messages
```

### 2.3 newsyslog — ротация логов

```sh
# Конфигурация: /etc/newsyslog.conf
$ cat /etc/newsyslog.conf
# logfile              mode count size  when  flags
/var/log/messages      644  5     300   *     Z
/var/log/authlog       640  7     *     168   Z
/var/log/daemon        640  5     300   *     Z

# Принудительная ротация
# doas newsyslog -F
```

### 2.4 syslogd — конфигурация

```sh
# /etc/syslog.conf
*.notice;auth,authpriv,cron,ftp,kern,lpr,mail,user.none  /var/log/messages
kern.debug;syslog,user.info                               /var/log/messages
auth.info                                                 /var/log/authlog
authpriv.debug                                            /var/log/secure
daemon.info                                               /var/log/daemon
```

---

## 3. Резервное копирование

### 3.1 dump/restore

```sh
# Полный бэкап файловой системы
# doas dump -0auf /backup/root.dump /

# Инкрементальный бэкап (уровень 1)
# doas dump -1auf /backup/root.1.dump /

# Восстановление
# doas restore -rf /backup/root.dump

# Интерактивное восстановление
# doas restore -if /backup/root.dump
```

### 3.2 tar

```sh
# Архивация каталога
$ tar -cvzf /backup/home.tar.gz /home

# С исключениями
$ tar -cvzf /backup/etc.tar.gz /etc --exclude="*.log"

# Восстановление
$ tar -xvzf /backup/home.tar.gz -C /

# Просмотр содержимого
$ tar -tvzf /backup/home.tar.gz
```

### 3.3 rsync

```sh
# Установить rsync
# doas pkg_add rsync

# Локальная синхронизация
$ rsync -avz /home/ /backup/home/

# На удалённый сервер
$ rsync -avz -e ssh /home/ user@backup:/backup/home/

# С удалением
$ rsync -avz --delete /home/ /backup/home/

# Сухой запуск
$ rsync -avzn /home/ /backup/home/
```

### 3.4 Скрипт бэкапа

```sh
#!/bin/sh
# /root/backup.sh

BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d)
HOST=$(hostname -s)

# Создать директорию
mkdir -p $BACKUP_DIR/$DATE

# Бэкап конфигурации
tar -cvzf $BACKUP_DIR/$DATE/etc.tar.gz /etc

# Бэкап домашних каталогов
tar -cvzf $BACKUP_DIR/$DATE/home.tar.gz /home

# Бэкап баз данных (если есть)
# pg_dumpall > $BACKUP_DIR/$DATE/postgres.sql

# Удалить старые бэкапы (старше 7 дней)
find $BACKUP_DIR -type d -mtime +7 -exec rm -rf {} \;

# Отчёт
echo "Backup completed: $DATE" | mail -s "Backup $HOST" admin@example.com
```

---

## 4. Планировщик cron

### 4.1 Формат crontab

```
# минуты часы день_месяца месяц день_недели команда
# (0-59) (0-23)   (1-31)   (1-12)  (0-7)

# Примеры:
0 3 * * * /root/backup.sh              # Каждый день в 3:00
*/15 * * * * /usr/local/bin/check.sh   # Каждые 15 минут
0 0 * * 0 /root/weekly.sh              # Каждое воскресенье
0 9-18 * * 1-5 /root/workhours.sh      # 9-18 по будням
```

### 4.2 Управление crontab

```sh
# Редактировать свой crontab
$ crontab -e

# Просмотреть
$ crontab -l

# Удалить
$ crontab -r

# Редактировать для другого пользователя (root)
# doas crontab -u admin -e
```

### 4.3 Системные cron файлы

```sh
# /etc/crontab — системный
$ cat /etc/crontab
SHELL=/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin
#
#minute hour    mday    month   wday    user    command
#
0       *       *       *       *       root    /usr/sbin/newsyslog
30      1       *       *       *       root    /bin/sh /etc/daily
30      3       *       *       6       root    /bin/sh /etc/weekly
30      5       1       *       *       root    /bin/sh /etc/monthly
```

### 4.4 Периодические скрипты

```sh
/etc/daily       # Ежедневные задачи
/etc/weekly      # Еженедельные
/etc/monthly     # Ежемесячные

/etc/daily.local    # Локальные дополнения
/etc/weekly.local
/etc/monthly.local
```

```sh
# Пример /etc/daily.local
#!/bin/sh

# Проверка дисков
df -h | mail -s "Disk usage" admin@example.com

# Проверка обновлений
syspatch -c
```

---

## 5. Обновление системы

### 5.1 Патчи безопасности (syspatch)

```sh
# Проверить доступные патчи
# doas syspatch -c

# Установить патчи
# doas syspatch
Get/Verify syspatch74-001_wifi... 100% |*****| 12345       00:00
Installing patch 001_wifi
Relinking to create unique kernel... done.

# Откатить последний патч
# doas syspatch -r

# Список установленных патчей
# doas syspatch -l
001_wifi
002_libcrypto
```

### 5.2 Обновление между релизами

```sh
# 1. Скачать sysupgrade
$ cd /tmp
$ ftp https://cdn.openbsd.org/pub/OpenBSD/7.5/amd64/bsd.rd

# 2. Запустить обновление
# doas sysupgrade

# Система перезагрузится в bsd.rd и выполнит обновление
```

### 5.3 Обновление пакетов

```sh
# Обновить все пакеты
# doas pkg_add -u

# Проверить устаревшие
# doas pkg_add -u -n
```

---

## 6. Диагностика проблем

### 6.1 Загрузка системы

```sh
# Сообщения загрузки
$ dmesg | less

# Сохранённые сообщения
$ cat /var/run/dmesg.boot

# Последние сообщения ядра
$ dmesg | tail -50
```

### 6.2 Проблемы с железом

```sh
# Датчики температуры
$ sysctl hw.sensors
hw.sensors.cpu0.temp0=45.00 degC

# PCI устройства
$ pcidump

# USB устройства
$ usbdevs -v
```

### 6.3 Сетевые проблемы

```sh
# Проверить интерфейс
$ ifconfig em0

# Проверить маршрутизацию
$ netstat -rn

# Проверить DNS
$ dig google.com

# Трассировка
$ traceroute google.com

# Захват трафика
# doas tcpdump -i em0
```

### 6.4 Проблемы с дисками

```sh
# Проверить файловую систему
# doas fsck /dev/sd0a

# SMART статус
# doas pkg_add smartmontools
# doas smartctl -H /dev/sd0

# Проверить логи на ошибки
$ dmesg | grep -i error
$ grep -i "error\|fail" /var/log/messages
```

---

## 7. Автоматизация

### 7.1 Скрипт мониторинга

```sh
#!/bin/sh
# /root/monitor.sh

# Пороги
DISK_THRESHOLD=90
LOAD_THRESHOLD=5
MAIL="admin@example.com"

# Проверка дисков
df -P | awk 'NR>1 {gsub(/%/,"",$5); if($5>'"$DISK_THRESHOLD"') print $6": "$5"%"}' | \
while read line; do
    echo "Disk warning: $line" | mail -s "Disk Alert" $MAIL
done

# Проверка нагрузки
LOAD=$(uptime | awk -F'load averages:' '{print $2}' | awk '{print $1}')
if [ $(echo "$LOAD > $LOAD_THRESHOLD" | bc) -eq 1 ]; then
    echo "Load average: $LOAD" | mail -s "Load Alert" $MAIL
fi
```

### 7.2 Автоматические обновления

```sh
# /etc/daily.local

# Установить патчи и отправить отчёт
syspatch 2>&1 | mail -s "Syspatch report $(hostname)" admin@example.com
```

---

## 8. Документирование

### 8.1 Что документировать

- Конфигурацию сети
- Установленные пакеты
- Изменения в конфигурации
- Процедуры восстановления
- Контакты и пароли

### 8.2 Сбор информации о системе

```sh
#!/bin/sh
# /root/sysinfo.sh

echo "=== System Info ==="
uname -a
echo

echo "=== Network ==="
ifconfig
echo

echo "=== Disks ==="
df -h
echo

echo "=== Packages ==="
pkg_info
echo

echo "=== Services ==="
rcctl ls on
echo

echo "=== PF Rules ==="
pfctl -sr
```

---

## 💡 Key Takeaways

- **systat**: Интерактивный мониторинг в реальном времени
- **syspatch**: Регулярно устанавливайте патчи безопасности
- **dump/tar/rsync**: Несколько способов бэкапа — выберите подходящий
- **cron**: Автоматизируйте рутинные задачи
- **Логи**: Первое место для диагностики проблем

---

## 🚀 Next Steps

**Related Modules:**
- [Advanced](../12_Advanced/) — виртуализация и продвинутые темы

**Practice Ideas:**
1. Настройте автоматический бэкап на удалённый сервер
2. Создайте скрипт мониторинга с оповещениями
3. Настройте ротацию логов для своих приложений
4. Обновите систему через sysupgrade

**Going Deeper:**
- Мониторинг с Prometheus/Grafana
- Централизованные логи с syslog
- Автоматизация с Ansible

---

## 📚 Additional Resources

**Documentation:**
- [man systat](https://man.openbsd.org/systat) — мониторинг
- [man syspatch](https://man.openbsd.org/syspatch) — патчи
- [man dump](https://man.openbsd.org/dump) — резервное копирование
- [man cron](https://man.openbsd.org/cron) — планировщик

---

