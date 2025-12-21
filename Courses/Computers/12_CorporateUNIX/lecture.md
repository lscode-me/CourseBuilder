# Solaris, BSD и корпоративный UNIX

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы UNIX и его философии
- Знать различия между различными вариантами UNIX
- Иметь представление о серверных системах

**Recommended prior modules:**

- [10_UNIX](../10_UNIX/) — UNIX и его философия

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить роль Solaris в серверных системах и его связь с SPARC
- Описать развитие BSD-систем и их влияние
- Понимать требования к надёжности и масштабируемости в корпоративных системах
- Объяснить роль UNIX в серверном мире 90-х и 2000-х

---

## 1. Solaris и SPARC

### 1.1 Создание Solaris

**Solaris** — операционная система от Sun Microsystems (теперь Oracle), основанная на UNIX System V.

**История:**

- Разработана для процессоров SPARC
- Оптимизирована для серверных задач
- Высокая надёжность и масштабируемость

**Особенности:**

**ZFS** — продвинутая файловая система

**Пример: ZFS команды**

```bash
# Создание ZFS pool
zpool create tank mirror /dev/sda /dev/sdb

# Создание файловой системы
zfs create tank/documents

# Создание snapshot
zfs snapshot tank/documents@backup1

# Клонирование snapshot
zfs clone tank/documents@backup1 tank/documents-clone

# Проверка целостности
zfs scrub tank

# Информация о pool
zpool status tank
zfs list
```

**DTrace** — инструмент динамической трассировки

**Пример: DTrace скрипт**

```dtrace
#!/usr/sbin/dtrace -s

syscall:::entry
{
    @[execname] = count();
}

END
{
    printa("System calls by process: %s = %@d\n", @);
}
```

**Контейнеры** — ранняя реализация контейнеризации (zones)

**Пример: Solaris Zones**

```bash
# Создание zone
zonecfg -z myzone
zonecfg:myzone> create
zonecfg:myzone> set zonepath=/zones/myzone
zonecfg:myzone> set autoboot=true
zonecfg:myzone> commit
zonecfg:myzone> exit

# Установка zone
zoneadm -z myzone install

# Запуск zone
zoneadm -z myzone boot
```

**Масштабируемость** — поддержка больших систем

### 1.2 Связь с SPARC

**Интеграция:**

- Solaris оптимизирована для архитектуры SPARC
- Использование особенностей SPARC (регистровые окна)
- Высокая производительность на SPARC системах

**Результат:**
Создание интегрированных решений "железо + ОС" для серверов.

### 1.3 Современное состояние

**OpenSolaris → illumos:**

- Solaris стала открытой (OpenSolaris)
- Развитие продолжается в проекте illumos
- Используется в специализированных системах

---

## 2. BSD-системы

### 2.1 Происхождение BSD

**BSD (Berkeley Software Distribution)** — вариант UNIX, разработанный в Калифорнийском университете в Беркли.

**История:**

- Начало в 1970-х годах
- Добавления к оригинальному UNIX
- Развитие сетевых возможностей

**Вклад:**

**TCP/IP стек:**
```c

// BSD sockets API (стал стандартом)
#include <sys/socket.h>
#include <netinet/in.h>

// Создание TCP socket
int sockfd = socket(AF_INET, SOCK_STREAM, 0);

struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(80);
inet_aton("192.168.1.1", &addr.sin_addr);

connect(sockfd, (struct sockaddr*)&addr, sizeof(addr));
```

**Виртуальная память:**

- Demand paging
- Memory mapping
- Swap space

**Файловая система FFS (Fast File System):**

- Улучшения над оригинальной файловой системой UNIX
- Цилиндрические группы
- Лучшая производительность

**Множество утилит:**

- vi, csh, tcsh
- Сетевые утилиты (ping, traceroute)
- Системные утилиты

### 2.2 Варианты BSD

**FreeBSD:**

- Фокус на производительности
- Широкое использование в серверах
- Основа для многих систем

**Пример: FreeBSD особенности**

```bash
# Ports system для установки ПО
cd /usr/ports/www/nginx
make install clean

# Jail (контейнеры)
jail -c name=myjail path=/jails/myjail \
     command=/bin/sh

# ZFS поддержка

zpool create tank /dev/ada0
```

**OpenBSD:**

- Фокус на безопасности
- Аудит безопасности кода
- Используется в критичных системах

**Пример: OpenBSD security features**

```bash
# W^X (Write XOR Execute) - страницы либо writable, либо executable
# ASLR (Address Space Layout Randomization)
# Stack canaries
# Privilege separation

# Проверка безопасности

auditd  # Security audit daemon
```

**NetBSD:**

- Фокус на переносимости
- Работает на множестве платформ
- Встроенные системы

**Поддерживаемые платформы:**

- x86, ARM, MIPS, PowerPC, SPARC, Alpha
- Embedded systems
- Рекордное количество платформ

**macOS:**

- Основан на BSD (Darwin)
- Показывает успех BSD в настольных системах

**Пример: macOS BSD команды**

```bash
# macOS использует BSD версии утилит

ps aux    # BSD формат (не System V)
ls -l     # BSD ls
```

### 2.3 BSD vs Linux

**Различия:**
| Аспект | BSD | Linux |
|--------|-----|-------|
| Лицензия | BSD (свободная) | GPL (copyleft) |
| Kernel + Userland | Единая система | Kernel + разные дистрибутивы |
| Происхождение | Прямой потомок UNIX | Клон UNIX |
| Инициализация | BSD init | systemd/sysvinit |
| Производительность | Высокая | Высокая |

### 2.3 Лицензия BSD

**Особенности:**

- Более свободная, чем GPL
- Позволяет использование в проприетарном ПО
- Способствовала распространению

---

## 3. Надёжность и масштабируемость

### 3.1 Требования корпоративных систем

**Надёжность:**

- Минимальное время простоя
- Отказоустойчивость
- Восстановление после сбоев

**Масштабируемость:**

- Поддержка большого количества пользователей
- Обработка больших объёмов данных
- Горизонтальное и вертикальное масштабирование

**Производительность:**

- Высокая пропускная способность
- Низкая задержка
- Эффективное использование ресурсов

### 3.2 Технологии надёжности

**RAID:**

- Избыточное хранение данных
- Защита от отказов дисков

**Пример: RAID в Solaris**

```bash
# Solaris Volume Manager
metainit d10 1 1 c0t0d0s0
metainit d20 1 1 c0t1d0s0
metainit d0 -m d10
metattach d0 d20  # Mirror
```

**Кластеризация:**

- Несколько серверов работают вместе
- Высокая доступность

**Пример: Solaris Cluster**

```bash
# Высокая доступность через кластеризацию
# Автоматический failover при отказе узла
# Shared storage между узлами

```

**Резервное копирование:**

- Регулярные бэкапы
- Восстановление данных

**Пример: ZFS snapshots для backup**

```bash
# Автоматические snapshots
zfs set snapdir=visible tank/documents
zfs snapshot -r tank/documents@$(date +%Y%m%d)

# Отправка snapshots на удалённый сервер

zfs send tank/documents@snapshot1 | \
    ssh remote zfs receive tank/backup
```

### 3.3 Мониторинг и обслуживание

**Пример: Мониторинг системы**

```bash
# Solaris prstat (аналог top)
prstat -a

# iostat для I/O статистики
iostat -xn 1

# DTrace для детального анализа

dtrace -n 'syscall:::entry { @[execname] = count(); }'
```

---

### 3.3 Масштабирование

**Вертикальное масштабирование:**

- Увеличение мощности одного сервера
- Больше процессоров, памяти

**Горизонтальное масштабирование:**

- Добавление серверов
- Распределение нагрузки

---

## 4. Серверный мир 90-х и 2000-х

### 4.1 Доминирование UNIX

**1990-е:**

- UNIX доминировал в серверном мире
- Различные варианты: Solaris, AIX, HP-UX, BSD
- Высокая стоимость, но необходимая надёжность

**Применение:**

- Корпоративные серверы
- Базы данных
- Веб-серверы (ранний интернет)
- Файловые серверы

### 4.2 Конкуренция

**Linux:**

- Появление Linux в 1990-х
- Бесплатная альтернатива
- Рост популярности

**Windows NT Server:**

- Конкуренция от Microsoft
- Упрощённое администрирование
- Интеграция с Windows клиентами

**Результат:**
Трёхсторонняя конкуренция: проприетарный UNIX, Linux, Windows Server.

### 4.3 Изменения в 2000-х

**Консолидация:**

- Меньше вариантов проприетарного UNIX
- Доминирование Linux и Windows Server
- Облачные вычисления

**Наследие:**
Идеи и технологии из корпоративного UNIX перешли в Linux и современные системы.

---

## 5. Современное состояние

### 5.1 illumos и OpenSolaris наследие

**illumos:**

- Форк OpenSolaris после закрытия Oracle
- Развитие ZFS, DTrace
- Используется в специализированных системах

**Примеры использования:**

- OmniOS, SmartOS
- Joyent Triton (cloud platform)
- Nexenta (storage systems)

### 5.2 BSD в современности

**FreeBSD:**

- Используется в Netflix (CDN)
- PlayStation 4 (основана на FreeBSD)
- Множество серверов

**OpenBSD:**

- OpenSSH (используется везде)
- pf firewall (портирован в другие системы)
- Критичные системы безопасности

**NetBSD:**

- Embedded systems
- Портативные устройства
- Специализированные платформы

---

## 💡 Key Takeaways

- **Solaris** показала важность интеграции ОС и аппаратуры (SPARC) для серверных систем, создала технологии (ZFS, DTrace, zones), которые повлияли на современные системы

- **BSD** внесла огромный вклад в развитие UNIX (TCP/IP, виртуальная память, FFS) и сетевых технологий, более свободная лицензия способствовала распространению

- **Надёжность и масштабируемость** — ключевые требования корпоративных систем (RAID, кластеризация, резервное копирование, вертикальное и горизонтальное масштабирование)

- **Серверный мир 90-2000-х** был эпохой доминирования UNIX (Solaris, AIX, HP-UX, BSD), которая сформировала современные подходы, многие идеи перешли в Linux и современные системы

---

## 🚀 Next Steps

**Related Modules:**

- [13_Plan9](../13_Plan9/) — альтернативные взгляды на операционные системы
- [17_Networks](../17_Networks/) — сети и распределённые системы

**Practice Ideas:**

1. Изучите различия между различными вариантами BSD
2. Исследуйте технологии надёжности в современных системах
3. Сравните подходы к масштабированию в разных системах

---

## 📚 Additional Resources

**Books:**

- "Design and Implementation of the FreeBSD Operating System" by McKusick & Neville-Neil
- История развития BSD и Solaris

---



