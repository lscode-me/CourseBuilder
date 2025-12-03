# Control Groups (cgroups)
## Управление и ограничение ресурсов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать концепцию namespaces
- Знать базовые команды Linux для работы с процессами
- Иметь представление о системных ресурсах (CPU, память, I/O)

**Recommended prior modules:**
- [Linux Namespaces](../02_Namespaces/) — изоляция ресурсов

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить архитектуру cgroups v1 и v2
- Создавать и настраивать cgroups для ограничения ресурсов
- Использовать systemd для управления cgroups
- Диагностировать проблемы с ресурсами через cgroups

---

## 1. Что такое Control Groups

Control Groups (cgroups) — механизм ядра Linux для организации процессов в иерархические группы и управления их потреблением системных ресурсов.

### 1.1 История cgroups

| Год | Событие |
|-----|---------|
| 2006 | Google разрабатывает "Process Containers" |
| 2007 | Переименование в cgroups, слияние в mainline kernel |
| 2008 | Cgroups v1 в Linux 2.6.24 |
| 2016 | Cgroups v2 становится стабильным (Linux 4.5) |
| 2020+ | Активный переход на cgroups v2 |

### 1.2 Основные возможности cgroups

**Resource Limiting:**
- Ограничение CPU, памяти, I/O, сети
- Жёсткие и мягкие лимиты

**Prioritization:**
- Распределение ресурсов между группами
- Веса и приоритеты

**Accounting:**
- Мониторинг использования ресурсов
- Статистика потребления

**Control:**
- Заморозка процессов (freezer)
- Checkpoint/restore

### 1.3 Архитектура cgroups

```
                    ┌─────────────────────┐
                    │      Root Cgroup    │
                    │     (all processes) │
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
    ┌──────▼──────┐     ┌──────▼──────┐     ┌──────▼──────┐
    │  user.slice │     │system.slice │     │ machine.slice│
    │             │     │             │     │ (containers) │
    └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
           │                   │                   │
      ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
      │ user-   │         │ nginx   │         │ docker- │
      │ 1000    │         │ service │         │ abc123  │
      └─────────┘         └─────────┘         └─────────┘
```

---

## 2. Cgroups v1 vs v2

### 2.1 Cgroups v1 — иерархия контроллеров

В v1 каждый контроллер (cpu, memory, blkio) имеет собственную иерархию:

```
/sys/fs/cgroup/
├── cpu/
│   ├── docker/
│   │   └── container1/
│   └── system.slice/
├── memory/
│   ├── docker/
│   │   └── container1/
│   └── system.slice/
├── blkio/
│   └── ...
└── devices/
    └── ...
```

**Проблемы v1:**
- Разные иерархии для разных контроллеров
- Сложность управления
- Неконсистентные интерфейсы
- Проблемы с делегированием

### 2.2 Cgroups v2 — единая иерархия

В v2 все контроллеры используют одну иерархию:

```
/sys/fs/cgroup/
├── cgroup.controllers      # Доступные контроллеры
├── cgroup.subtree_control  # Активные контроллеры для потомков
├── user.slice/
│   └── user-1000.slice/
│       └── session-1.scope/
├── system.slice/
│   └── nginx.service/
└── docker/
    └── abc123.../
        ├── cgroup.controllers
        ├── cpu.max
        ├── memory.max
        └── io.max
```

### 2.3 Сравнение v1 и v2

| Аспект | Cgroups v1 | Cgroups v2 |
|--------|------------|------------|
| Иерархия | Множественная | Единая |
| Контроллеры | Независимые | Унифицированные |
| Интерфейс | Различный | Консистентный |
| Делегирование | Сложное | Простое |
| Systemd | Поддержка | Рекомендуется |
| Контейнеры | Docker, LXC | Docker, Podman, K8s |

### 2.4 Проверка версии cgroups

```bash
# Проверить версию cgroups
mount | grep cgroup
```

**Output (v2):**
```
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime)
```

**Output (v1):**
```
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/cpu type cgroup (rw,nosuid,nodev,noexec,relatime,cpu)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
```

```bash
# Проверить текущую cgroup процесса
cat /proc/self/cgroup
```

**Output (v2):**
```
0::/user.slice/user-1000.slice/session-1.scope
```

---

## 3. Контроллеры ресурсов

### 3.1 CPU Controller

Контроллер CPU управляет распределением процессорного времени.

**Основные параметры (v2):**

| Параметр | Описание |
|----------|----------|
| cpu.max | Максимум CPU (quota period) |
| cpu.weight | Относительный вес (1-10000) |
| cpu.pressure | Информация о CPU pressure |

```bash
# Ограничение до 50% одного CPU
echo "50000 100000" > /sys/fs/cgroup/mygroup/cpu.max

# Формат: $QUOTA $PERIOD (в микросекундах)
# 50000/100000 = 50% CPU

# Ограничение до 2 CPU
echo "200000 100000" > /sys/fs/cgroup/mygroup/cpu.max
```

**Пример: ограничение CPU для процесса:**

```bash
# Создаём cgroup
sudo mkdir /sys/fs/cgroup/cpu-limited

# Включаем cpu контроллер
echo "+cpu" | sudo tee /sys/fs/cgroup/cgroup.subtree_control

# Устанавливаем лимит 25% CPU
echo "25000 100000" | sudo tee /sys/fs/cgroup/cpu-limited/cpu.max

# Запускаем процесс в cgroup
echo $$ | sudo tee /sys/fs/cgroup/cpu-limited/cgroup.procs

# Проверяем ограничение
stress --cpu 1 --timeout 10
top  # CPU usage должен быть ~25%
```

### 3.2 Memory Controller

Контроллер памяти ограничивает использование RAM и swap.

**Основные параметры (v2):**

| Параметр | Описание |
|----------|----------|
| memory.max | Жёсткий лимит памяти |
| memory.high | Мягкий лимит (throttling) |
| memory.min | Минимальная защищённая память |
| memory.current | Текущее использование |
| memory.swap.max | Лимит swap |

```bash
# Ограничение памяти до 512MB
echo "536870912" > /sys/fs/cgroup/mygroup/memory.max

# Или с суффиксами (если поддерживается)
echo "512M" > /sys/fs/cgroup/mygroup/memory.max

# Мягкий лимит (начинается throttling)
echo "256M" > /sys/fs/cgroup/mygroup/memory.high

# Отключение swap
echo "0" > /sys/fs/cgroup/mygroup/memory.swap.max
```

**Пример: тестирование memory limits:**

```bash
# Создаём cgroup с ограничением памяти
sudo mkdir /sys/fs/cgroup/mem-limited
echo "+memory" | sudo tee /sys/fs/cgroup/cgroup.subtree_control

# Устанавливаем лимит 100MB
echo "104857600" | sudo tee /sys/fs/cgroup/mem-limited/memory.max

# Отключаем swap для чистоты эксперимента
echo "0" | sudo tee /sys/fs/cgroup/mem-limited/memory.swap.max

# Запускаем процесс
echo $$ | sudo tee /sys/fs/cgroup/mem-limited/cgroup.procs

# Пытаемся выделить больше памяти
python3 -c "x = 'a' * (200 * 1024 * 1024)"  # OOM killed!
```

### 3.3 I/O Controller

Контроллер I/O управляет дисковыми операциями.

**Основные параметры (v2):**

| Параметр | Описание |
|----------|----------|
| io.max | Лимиты IOPS и bandwidth |
| io.weight | Относительный вес (1-10000) |
| io.stat | Статистика I/O |

```bash
# Формат io.max: MAJ:MIN rbps=X wbps=Y riops=Z wiops=W

# Ограничение чтения до 10MB/s для диска 8:0
echo "8:0 rbps=10485760" > /sys/fs/cgroup/mygroup/io.max

# Ограничение записи до 1000 IOPS
echo "8:0 wiops=1000" > /sys/fs/cgroup/mygroup/io.max

# Комбинированное ограничение
echo "8:0 rbps=10485760 wbps=5242880 riops=1000 wiops=500" > /sys/fs/cgroup/mygroup/io.max
```

**Определение major:minor устройства:**

```bash
# Найти major:minor для диска
lsblk -o NAME,MAJ:MIN
```

**Output:**
```
NAME   MAJ:MIN
sda      8:0
├─sda1   8:1
└─sda2   8:2
nvme0n1 259:0
```

### 3.4 PIDs Controller

Контроллер PIDs ограничивает количество процессов.

```bash
# Максимум 100 процессов в cgroup
echo "100" > /sys/fs/cgroup/mygroup/pids.max

# Текущее количество процессов
cat /sys/fs/cgroup/mygroup/pids.current
```

**Защита от fork-бомб:**

```bash
# Создаём cgroup с ограничением PIDs
sudo mkdir /sys/fs/cgroup/fork-limited
echo "+pids" | sudo tee /sys/fs/cgroup/cgroup.subtree_control
echo "50" | sudo tee /sys/fs/cgroup/fork-limited/pids.max

# Добавляем shell
echo $$ | sudo tee /sys/fs/cgroup/fork-limited/cgroup.procs

# Fork-бомба теперь безопасна (будет ограничена)
:(){ :|:& };:  # Остановится на 50 процессах
```

---

## 4. Работа с cgroups v2

### 4.1 Структура файловой системы

```bash
# Список файлов в cgroup
ls -la /sys/fs/cgroup/
```

**Output:**
```
-r--r--r-- 1 root root 0 Dec  1 12:00 cgroup.controllers
-rw-r--r-- 1 root root 0 Dec  1 12:00 cgroup.max.depth
-rw-r--r-- 1 root root 0 Dec  1 12:00 cgroup.max.descendants
-rw-r--r-- 1 root root 0 Dec  1 12:00 cgroup.procs
-r--r--r-- 1 root root 0 Dec  1 12:00 cgroup.stat
-rw-r--r-- 1 root root 0 Dec  1 12:00 cgroup.subtree_control
drwxr-xr-x 2 root root 0 Dec  1 12:00 system.slice
drwxr-xr-x 2 root root 0 Dec  1 12:00 user.slice
```

### 4.2 Создание и настройка cgroup

```bash
#!/bin/bash
# create_cgroup.sh - создание cgroup с ограничениями

CGROUP_NAME="${1:-myapp}"
CGROUP_PATH="/sys/fs/cgroup/$CGROUP_NAME"

# Создаём cgroup
sudo mkdir -p "$CGROUP_PATH"

# Включаем контроллеры для root cgroup
echo "+cpu +memory +io +pids" | sudo tee /sys/fs/cgroup/cgroup.subtree_control

# Устанавливаем ограничения
# CPU: 50% одного ядра
echo "50000 100000" | sudo tee "$CGROUP_PATH/cpu.max"

# Memory: 512MB
echo "536870912" | sudo tee "$CGROUP_PATH/memory.max"

# PIDs: максимум 100 процессов
echo "100" | sudo tee "$CGROUP_PATH/pids.max"

echo "Cgroup $CGROUP_NAME created at $CGROUP_PATH"
echo "To add a process: echo \$PID | sudo tee $CGROUP_PATH/cgroup.procs"
```

### 4.3 Добавление процессов в cgroup

```bash
# Добавить текущий shell
echo $$ | sudo tee /sys/fs/cgroup/myapp/cgroup.procs

# Добавить по PID
echo 12345 | sudo tee /sys/fs/cgroup/myapp/cgroup.procs

# Все дочерние процессы автоматически наследуют cgroup
```

### 4.4 Мониторинг cgroup

```bash
# Текущее использование CPU
cat /sys/fs/cgroup/myapp/cpu.stat
```

**Output:**
```
usage_usec 1234567
user_usec 1000000
system_usec 234567
nr_periods 100
nr_throttled 5
throttled_usec 50000
```

```bash
# Использование памяти
cat /sys/fs/cgroup/myapp/memory.current
cat /sys/fs/cgroup/myapp/memory.stat
```

**Output:**
```
anon 52428800
file 10485760
kernel_stack 163840
...
```

### 4.5 Удаление cgroup

```bash
# Перед удалением нужно переместить все процессы
cat /sys/fs/cgroup/myapp/cgroup.procs | while read pid; do
    echo $pid | sudo tee /sys/fs/cgroup/cgroup.procs
done

# Удаляем cgroup
sudo rmdir /sys/fs/cgroup/myapp
```

---

## 5. Cgroups и systemd

Systemd полностью интегрирован с cgroups и является рекомендуемым способом управления ими.

### 5.1 Slice, Scope и Service

**Slice** — группа unit'ов, делящих ресурсы:
```
-.slice (root)
├── user.slice
│   └── user-1000.slice
├── system.slice
│   └── nginx.service
└── machine.slice
    └── docker containers
```

**Service** — управляемый systemd сервис
**Scope** — внешний процесс, зарегистрированный в systemd

### 5.2 Управление ресурсами через systemd

```bash
# Просмотр cgroup unit'а
systemctl status nginx
```

**Output:**
```
● nginx.service - A high performance web server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
     Active: active (running)
    Process: 1234 ExecStart=/usr/sbin/nginx
   Main PID: 1235 (nginx)
      Tasks: 5 (limit: 4915)
     Memory: 12.5M
        CPU: 1.234s
     CGroup: /system.slice/nginx.service
             ├─1235 nginx: master process /usr/sbin/nginx
             └─1236 nginx: worker process
```

### 5.3 Настройка ограничений в unit-файле

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/myapp
Restart=always

# Resource limits
CPUQuota=50%
MemoryMax=512M
MemoryHigh=384M
TasksMax=100

# I/O limits
IOReadBandwidthMax=/dev/sda 10M
IOWriteBandwidthMax=/dev/sda 5M

[Install]
WantedBy=multi-user.target
```

### 5.4 Runtime изменение ограничений

```bash
# Изменить CPU limit для запущенного сервиса
sudo systemctl set-property nginx.service CPUQuota=25%

# Изменить memory limit
sudo systemctl set-property nginx.service MemoryMax=256M

# Посмотреть текущие ограничения
systemctl show nginx.service | grep -E "(CPU|Memory|Tasks)"
```

### 5.5 Transient units (одноразовые)

```bash
# Запустить команду с ограничениями без создания unit-файла
systemd-run --scope --property=MemoryMax=100M ./memory-hungry-app

# С именем для отслеживания
systemd-run --unit=mytest --scope \
    --property=CPUQuota=25% \
    --property=MemoryMax=256M \
    stress --cpu 2 --vm 1 --vm-bytes 128M --timeout 60
```

---

## 6. Практические сценарии

### 6.1 Изоляция веб-приложения

```bash
#!/bin/bash
# webapp_cgroup.sh - настройка cgroup для веб-приложения

APP_NAME="webapp"
CGROUP="/sys/fs/cgroup/$APP_NAME"

# Создаём cgroup
sudo mkdir -p "$CGROUP"

# Включаем контроллеры
echo "+cpu +memory +io +pids" | sudo tee /sys/fs/cgroup/cgroup.subtree_control

# CPU: максимум 2 ядра
echo "200000 100000" | sudo tee "$CGROUP/cpu.max"

# Memory: 2GB max, 1.5GB high (throttling начнётся раньше)
echo "2147483648" | sudo tee "$CGROUP/memory.max"
echo "1610612736" | sudo tee "$CGROUP/memory.high"

# Swap отключен для предсказуемости
echo "0" | sudo tee "$CGROUP/memory.swap.max"

# Максимум 500 процессов/потоков
echo "500" | sudo tee "$CGROUP/pids.max"

# I/O: ограничение для SSD (259:0)
echo "259:0 rbps=104857600 wbps=52428800" | sudo tee "$CGROUP/io.max"

echo "Cgroup for $APP_NAME configured"
```

### 6.2 Мониторинг контейнера

```bash
#!/bin/bash
# monitor_cgroup.sh - мониторинг ресурсов cgroup

CGROUP_PATH="${1:-/sys/fs/cgroup/docker}"

while true; do
    clear
    echo "=== Cgroup Monitor: $CGROUP_PATH ==="
    echo "Time: $(date)"
    echo ""
    
    # CPU
    if [ -f "$CGROUP_PATH/cpu.stat" ]; then
        echo "=== CPU ==="
        cat "$CGROUP_PATH/cpu.stat" | head -5
        echo ""
    fi
    
    # Memory
    if [ -f "$CGROUP_PATH/memory.current" ]; then
        echo "=== Memory ==="
        current=$(cat "$CGROUP_PATH/memory.current")
        max=$(cat "$CGROUP_PATH/memory.max" 2>/dev/null || echo "max")
        echo "Current: $(numfmt --to=iec $current)"
        echo "Max: $max"
        
        if [ -f "$CGROUP_PATH/memory.stat" ]; then
            echo "Stats:"
            grep -E "^(anon|file|kernel)" "$CGROUP_PATH/memory.stat"
        fi
        echo ""
    fi
    
    # PIDs
    if [ -f "$CGROUP_PATH/pids.current" ]; then
        echo "=== PIDs ==="
        echo "Current: $(cat $CGROUP_PATH/pids.current)"
        echo "Max: $(cat $CGROUP_PATH/pids.max)"
        echo ""
    fi
    
    # Processes
    echo "=== Processes ==="
    cat "$CGROUP_PATH/cgroup.procs" | head -10
    
    sleep 2
done
```

### 6.3 Защита от OOM

```bash
# Настройка OOM killer для cgroup

# memory.oom.group - при OOM убить всю группу, а не один процесс
echo "1" | sudo tee /sys/fs/cgroup/myapp/memory.oom.group

# Приоритет OOM (чем выше, тем раньше убьют)
# Для критических сервисов понизить приоритет
echo "-1000" | sudo tee /proc/$(cat /sys/fs/cgroup/critical/cgroup.procs | head -1)/oom_score_adj
```

---

## 7. Cgroups v1 (legacy)

Хотя v2 рекомендуется, v1 всё ещё используется. Рассмотрим основные отличия.

### 7.1 Структура cgroups v1

```bash
# В v1 каждый контроллер монтируется отдельно
mount | grep cgroup
```

**Output:**
```
cgroup on /sys/fs/cgroup/cpu type cgroup (rw,cpu,cpuacct)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,memory)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,blkio)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,freezer)
```

### 7.2 Настройка CPU в v1

```bash
# Создаём cgroup в иерархии cpu
sudo mkdir /sys/fs/cgroup/cpu/myapp

# CPU shares (относительный вес, default = 1024)
echo "512" | sudo tee /sys/fs/cgroup/cpu/myapp/cpu.shares

# CPU quota (CFS bandwidth control)
# Period в микросекундах
echo "100000" | sudo tee /sys/fs/cgroup/cpu/myapp/cpu.cfs_period_us
# Quota - сколько микросекунд CPU можно использовать за период
echo "50000" | sudo tee /sys/fs/cgroup/cpu/myapp/cpu.cfs_quota_us

# Добавляем процесс
echo $$ | sudo tee /sys/fs/cgroup/cpu/myapp/tasks
```

### 7.3 Настройка Memory в v1

```bash
# Создаём cgroup в иерархии memory
sudo mkdir /sys/fs/cgroup/memory/myapp

# Hard limit (OOM при превышении)
echo "536870912" | sudo tee /sys/fs/cgroup/memory/myapp/memory.limit_in_bytes

# Soft limit (начало reclaim)
echo "268435456" | sudo tee /sys/fs/cgroup/memory/myapp/memory.soft_limit_in_bytes

# Лимит swap + memory
echo "1073741824" | sudo tee /sys/fs/cgroup/memory/myapp/memory.memsw.limit_in_bytes

# Добавляем процесс
echo $$ | sudo tee /sys/fs/cgroup/memory/myapp/tasks
```

### 7.4 Таблица соответствия v1 и v2

| Функция | Cgroups v1 | Cgroups v2 |
|---------|------------|------------|
| Процессы | tasks | cgroup.procs |
| CPU quota | cpu.cfs_quota_us | cpu.max |
| CPU shares | cpu.shares | cpu.weight |
| Memory limit | memory.limit_in_bytes | memory.max |
| Memory soft | memory.soft_limit_in_bytes | memory.high |
| Swap limit | memory.memsw.limit_in_bytes | memory.swap.max |
| I/O weight | blkio.weight | io.weight |
| I/O limit | blkio.throttle.* | io.max |

---

## 8. Cgroups в контейнерных runtime

### 8.1 Docker и cgroups

```bash
# Docker использует cgroups для ограничения ресурсов контейнера
docker run -d \
    --name limited-container \
    --cpus="0.5" \
    --memory="256m" \
    --memory-swap="256m" \
    --pids-limit=50 \
    nginx

# Проверяем cgroup контейнера
CONTAINER_ID=$(docker inspect --format '{{.Id}}' limited-container)
ls /sys/fs/cgroup/system.slice/docker-${CONTAINER_ID}.scope/
```

### 8.2 Просмотр ограничений Docker

```bash
# Docker stats показывает использование ресурсов
docker stats --no-stream limited-container
```

**Output:**
```
CONTAINER ID   NAME                CPU %     MEM USAGE / LIMIT   MEM %     NET I/O     BLOCK I/O
abc123         limited-container   0.50%     10MiB / 256MiB      3.91%     1kB / 0B    0B / 0B
```

### 8.3 Podman (rootless) и cgroups

```bash
# Podman использует cgroups v2 delegation для rootless
podman run -d \
    --cpus=1 \
    --memory=512m \
    alpine sleep 1000

# Cgroup находится в пользовательской иерархии
cat /sys/fs/cgroup/user.slice/user-$(id -u).slice/user@$(id -u).service/*/cgroup.procs
```

---

## 9. Отладка и диагностика

### 9.1 Утилита systemd-cgtop

```bash
# Топ процессов по cgroups
systemd-cgtop
```

**Output:**
```
Control Group                     Tasks   %CPU   Memory  Input/s Output/s
/                                   234   15.2     2.1G        -        -
/system.slice                        45    8.3   512.0M        -        -
/system.slice/docker.service         12    5.1   256.0M        -        -
/user.slice                         189    6.9     1.6G        -        -
```

### 9.2 Анализ CPU throttling

```bash
# Проверка throttling
cat /sys/fs/cgroup/myapp/cpu.stat
```

**Если `nr_throttled` растёт — процесс достиг лимита:**
```
nr_periods 1000
nr_throttled 150      # 15% периодов throttled
throttled_usec 750000 # 0.75 секунды суммарно
```

### 9.3 Pressure Stall Information (PSI)

PSI показывает, насколько процессы "страдают" от нехватки ресурсов:

```bash
# CPU pressure
cat /sys/fs/cgroup/myapp/cpu.pressure
```

**Output:**
```
some avg10=5.00 avg60=3.50 avg300=2.10 total=123456
full avg10=2.00 avg60=1.50 avg300=1.00 total=56789
```

- **some**: какой-то процесс ждал CPU
- **full**: все процессы ждали CPU

```bash
# Memory pressure
cat /sys/fs/cgroup/myapp/memory.pressure
```

### 9.4 Логирование событий cgroup

```bash
# Логирование OOM событий
dmesg | grep -i "killed process"

# Или через journalctl
journalctl -k | grep -i oom
```

---

## 10. Best Practices

### 10.1 Рекомендации по настройке

1. **Используйте cgroups v2** — унифицированная иерархия и лучшая поддержка
2. **Настраивайте memory.high** — мягкий лимит для graceful degradation
3. **Ограничивайте PIDs** — защита от fork-бомб
4. **Используйте systemd** — интеграция из коробки

### 10.2 Типичные ошибки

❌ **Не устанавливать memory.swap.max:**
```bash
# Процесс может использовать много swap и замедлить систему
echo "0" | sudo tee /sys/fs/cgroup/myapp/memory.swap.max
```

❌ **Слишком жёсткие CPU limits:**
```bash
# Лучше использовать веса для справедливого распределения
echo "100" | sudo tee /sys/fs/cgroup/myapp/cpu.weight  # Относительно 100 default
```

❌ **Забыть о наследовании:**
```bash
# Дочерние cgroups наследуют ограничения
# Нужно явно включать контроллеры
echo "+cpu +memory" | sudo tee /sys/fs/cgroup/parent/cgroup.subtree_control
```

### 10.3 Паттерн: Graceful degradation

```bash
# Настройка для graceful degradation
# memory.high < memory.max
echo "384M" | sudo tee /sys/fs/cgroup/myapp/memory.high  # Throttling
echo "512M" | sudo tee /sys/fs/cgroup/myapp/memory.max   # OOM kill

# Приложение начнёт замедляться при 384MB
# OOM kill только при 512MB
```

---

## 💡 Key Takeaways

- **Cgroups** управляют ресурсами (CPU, memory, I/O), namespaces изолируют видимость
- **Cgroups v2** имеет единую иерархию и консистентный интерфейс
- **systemd** — рекомендуемый способ управления cgroups
- **memory.high** + **memory.max** обеспечивают graceful degradation
- **PIDs limit** защищает от fork-бомб

---

## 🚀 Next Steps

**Related Modules:**
- [Union Filesystems](../04_FileSystem/) — слои образов контейнеров
- [Container Runtimes](../06_Runtimes/) — как runtime используют cgroups

**Practice Ideas:**
1. Создайте cgroup с ограничением CPU и проверьте throttling через stress
2. Настройте memory limits и вызовите OOM intentionally
3. Используйте systemd-run для запуска команд с ограничениями
4. Настройте PSI мониторинг для cgroup

**Going Deeper:**
- eBPF и расширенный мониторинг cgroups
- io.latency контроллер для SSD
- Kubernetes resource quotas и limits

---

## 📚 Additional Resources

**Documentation:**
- [cgroups(7) man page](https://man7.org/linux/man-pages/man7/cgroups.7.html)
- [Linux kernel cgroups v2 documentation](https://www.kernel.org/doc/Documentation/cgroup-v2.txt)
- [systemd resource control](https://www.freedesktop.org/software/systemd/man/systemd.resource-control.html)

**Articles:**
- [Control Group v2 (kernel.org)](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- [Facebook's cgroup2 journey](https://engineering.fb.com/2018/07/19/core-data/cgroup2/)

**Books:**
- "Container Security" by Liz Rice — глава 5 о cgroups
- "Linux Kernel Development" by Robert Love

---

