# Linux Namespaces
## Механизмы изоляции ресурсов ядра

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать историю изоляции процессов (chroot, jails)
- Знать базовые системные вызовы (fork, exec, clone)
- Уметь работать с процессами в Linux

**Recommended prior modules:**

- [Process Isolation](../01_Intro/) — история и основы изоляции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить назначение каждого типа namespace
- Использовать `unshare` и `nsenter` для работы с namespaces
- Создавать изолированные окружения программно через системные вызовы
- Анализировать namespaces запущенных процессов

---

## 1. Что такое Namespaces

Namespaces — механизм ядра Linux для изоляции глобальных системных ресурсов. Каждый namespace создаёт отдельную "видимость" ресурса для группы процессов.

### 1.1 Концепция изоляции

Без namespaces все процессы видят одни и те же:

- Дерево процессов (PID 1 — init)
- Сетевые интерфейсы и таблицы маршрутизации
- Точки монтирования
- Hostname и domain name
- Пользователей и группы
- IPC объекты (семафоры, очереди сообщений)

С namespaces каждый контейнер видит:

- Своё дерево процессов (свой PID 1)
- Свои сетевые интерфейсы
- Свои точки монтирования
- Свой hostname
- Своих пользователей
- Свои IPC объекты

### 1.2 Типы Namespaces

| Namespace | Флаг | Изолирует | Kernel версия |
|-----------|------|-----------|---------------|
| Mount | CLONE_NEWNS | Точки монтирования | 2.4.19 (2002) |
| UTS | CLONE_NEWUTS | Hostname, domain name | 2.6.19 (2006) |
| IPC | CLONE_NEWIPC | System V IPC, POSIX queues | 2.6.19 (2006) |
| PID | CLONE_NEWPID | Process IDs | 2.6.24 (2008) |
| Network | CLONE_NEWNET | Сетевые устройства, стек | 2.6.29 (2009) |
| User | CLONE_NEWUSER | UID/GID mapping | 3.8 (2013) |
| Cgroup | CLONE_NEWCGROUP | Cgroup root | 4.6 (2016) |
| Time | CLONE_NEWTIME | Системные часы | 5.6 (2020) |

### 1.3 Системные вызовы для работы с namespaces

```c

// Создание нового namespace
int clone(int (*fn)(void *), void *stack, int flags, void *arg);

// Создание namespace для текущего процесса
int unshare(int flags);

// Присоединение к существующему namespace
int setns(int fd, int nstype);

```

---

## 2. Mount Namespace (CLONE_NEWNS)

Mount namespace изолирует точки монтирования. Каждый mount namespace имеет собственный список точек монтирования.

### 2.1 Создание mount namespace

```bash
# Создаём новый mount namespace
sudo unshare --mount /bin/bash

# Теперь изменения монтирования видны только в этом namespace
mount -t tmpfs tmpfs /mnt
ls /mnt  # Пустая директория

# В другом терминале /mnt не изменился
```

### 2.2 Программное создание mount namespace

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/mount.h>

#define STACK_SIZE (1024 * 1024)

static char child_stack[STACK_SIZE];

int child_fn(void *arg) {
    printf("Child PID: %d\n", getpid());
    
    // Создаём приватную точку монтирования
    if (mount("none", "/", NULL, MS_REC | MS_PRIVATE, NULL) == -1) {
        perror("mount private");
        return 1;
    }
    
    // Монтируем tmpfs в /tmp
    if (mount("tmpfs", "/tmp", "tmpfs", 0, "size=64M") == -1) {
        perror("mount tmpfs");
        return 1;
    }
    
    printf("Mounted tmpfs on /tmp (visible only in this namespace)\n");
    
    // Запускаем shell
    execl("/bin/bash", "bash", NULL);
    return 0;
}

int main() {
    printf("Parent PID: %d\n", getpid());
    
    int flags = CLONE_NEWNS | SIGCHLD;
    
    pid_t pid = clone(child_fn, child_stack + STACK_SIZE, flags, NULL);
    if (pid == -1) {
        perror("clone");
        exit(1);
    }
    
    printf("Created child with PID: %d\n", pid);
    waitpid(pid, NULL, 0);
    
    return 0;
}

```

**Компиляция и запуск:**
```bash

gcc -o mount_ns mount_ns.c
sudo ./mount_ns

```

### 2.3 Типы распространения монтирования

Mount namespace поддерживает разные типы propagation:

| Тип | Описание |
|-----|----------|
| MS_SHARED | Изменения распространяются между namespaces |
| MS_PRIVATE | Изменения локальны для namespace |
| MS_SLAVE | Получает изменения от master, но не отправляет |
| MS_UNBINDABLE | Нельзя создать bind mount |

```bash
# Сделать точку монтирования приватной
mount --make-private /mnt

# Сделать всё дерево приватным рекурсивно
mount --make-rprivate /

# Проверить propagation type
cat /proc/self/mountinfo | grep " / "

```

---

## 3. UTS Namespace (CLONE_NEWUTS)

UTS namespace изолирует hostname и NIS domain name. UTS расшифровывается как "Unix Time-sharing System".

### 3.1 Изменение hostname в изолированном namespace

```bash
# Текущий hostname
hostname

```

**Output:**
```

myserver

```

```bash
# Создаём новый UTS namespace
sudo unshare --uts /bin/bash

# Изменяем hostname
hostname container-host
hostname

```

**Output:**
```

container-host

```

```bash
# В другом терминале hostname не изменился
hostname

```

**Output:**
```

myserver

```

### 3.2 Программная работа с UTS namespace

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/utsname.h>

int main() {
    struct utsname uts;
    
    // Создаём новый UTS namespace
    if (unshare(CLONE_NEWUTS) == -1) {
        perror("unshare");
        exit(1);
    }
    
    // Изменяем hostname
    if (sethostname("isolated-host", 13) == -1) {
        perror("sethostname");
        exit(1);
    }
    
    // Получаем информацию о системе
    if (uname(&uts) == -1) {
        perror("uname");
        exit(1);
    }
    
    printf("Hostname in new namespace: %s\n", uts.nodename);
    printf("System: %s %s\n", uts.sysname, uts.release);
    
    // Запускаем shell для демонстрации
    execl("/bin/bash", "bash", NULL);
    
    return 0;
}

```

---

## 4. IPC Namespace (CLONE_NEWIPC)

IPC namespace изолирует System V IPC объекты и POSIX message queues.

### 4.1 Изолируемые объекты

- **System V shared memory** (shmget, shmat)

- **System V semaphores** (semget, semop)

- **System V message queues** (msgget, msgsnd, msgrcv)

- **POSIX message queues** (mq_open)

### 4.2 Демонстрация изоляции IPC

```bash
# Создаём shared memory segment
ipcmk -M 1024

# Просматриваем IPC объекты
ipcs -m

```

**Output:**
```

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch
0x52012296 0          root       644        1024       0

```

```bash
# Создаём новый IPC namespace
sudo unshare --ipc /bin/bash

# В новом namespace нет IPC объектов
ipcs -m

```

**Output:**
```

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch

```

### 4.3 Практический пример: изоляция очередей сообщений

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>

struct message {
    long mtype;
    char mtext[100];
};

void list_queues() {
    system("ipcs -q");
}

int main() {
    key_t key = ftok("/tmp", 'A');
    int msqid;
    
    printf("=== Before unshare ===\n");
    
    // Создаём очередь сообщений
    msqid = msgget(key, IPC_CREAT | 0666);
    if (msqid == -1) {
        perror("msgget");
        exit(1);
    }
    printf("Created message queue with ID: %d\n", msqid);
    list_queues();
    
    printf("\n=== After unshare (new IPC namespace) ===\n");
    
    // Создаём новый IPC namespace
    if (unshare(CLONE_NEWIPC) == -1) {
        perror("unshare");
        exit(1);
    }
    
    // Старая очередь не видна
    list_queues();
    
    // Создаём новую очередь в новом namespace
    int new_msqid = msgget(key, IPC_CREAT | 0666);
    printf("Created new message queue with ID: %d\n", new_msqid);
    list_queues();
    
    return 0;
}

```

---

## 5. PID Namespace (CLONE_NEWPID)

PID namespace изолирует пространство идентификаторов процессов. Процессы в разных PID namespaces могут иметь одинаковые PID.

### 5.1 Как работает PID namespace

```

┌─────────────────────────────────────────────────┐
│                Host PID Namespace               │
│                                                 │
│  PID 1 (init/systemd)                           │
│  PID 1234 (container runtime)                   │
│      │                                          │
│      └─── Creates new PID namespace ────────────┤
│                                                 │
│  ┌────────────────────────────────────────────┐ │
│  │         Container PID Namespace            │ │
│  │                                            │ │
│  │  PID 1 (container init) ←── PID 1235 host  │ │
│  │  PID 2 (app process)    ←── PID 1236 host  │ │
│  │  PID 3 (worker)         ←── PID 1237 host  │ │
│  └────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘

```

### 5.2 Создание PID namespace

```bash
# Создаём новый PID namespace
# --fork нужен потому что unshare сам не становится PID 1
sudo unshare --pid --fork --mount-proc /bin/bash

# Проверяем PID
echo $$

```

**Output:**
```

1

```

```bash
# Смотрим процессы
ps aux

```

**Output:**
```

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   8304  5200 pts/0    S    12:00   0:00 /bin/bash
root         8  0.0  0.0  10072  3280 pts/0    R+   12:00   0:00 ps aux

```

### 5.3 Вложенные PID namespaces

PID namespaces образуют иерархию:

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/mount.h>

#define STACK_SIZE (1024 * 1024)
static char child_stack[STACK_SIZE];

int child_fn(void *arg) {
    int level = *(int *)arg;
    
    printf("Level %d: PID in this namespace = %d\n", level, getpid());
    
    // Монтируем /proc для этого namespace
    mount("proc", "/proc", "proc", 0, NULL);
    
    if (level < 3) {
        // Создаём ещё один уровень вложенности
        int next_level = level + 1;
        int flags = CLONE_NEWPID | SIGCHLD;
        
        pid_t pid = clone(child_fn, child_stack + STACK_SIZE, flags, &next_level);
        if (pid > 0) {
            printf("Level %d: Created child with PID %d (in this namespace)\n", 
                   level, pid);
            waitpid(pid, NULL, 0);
        }
    }
    
    return 0;
}

int main() {
    printf("Parent: PID = %d\n", getpid());
    
    int level = 1;
    int flags = CLONE_NEWPID | CLONE_NEWNS | SIGCHLD;
    
    pid_t pid = clone(child_fn, child_stack + STACK_SIZE, flags, &level);
    if (pid == -1) {
        perror("clone");
        exit(1);
    }
    
    printf("Parent: Created child with PID %d (in parent namespace)\n", pid);
    waitpid(pid, NULL, 0);
    
    return 0;
}

```

### 5.4 PID 1 в namespace

Первый процесс в PID namespace (PID 1) имеет особые свойства:

1. **Reaping orphans** — становится родителем осиротевших процессов
2. **Signal handling** — получает только сигналы, для которых установлен handler
3. **Namespace termination** — если PID 1 завершается, все процессы в namespace получают SIGKILL

```bash
# Демонстрация: что происходит при завершении PID 1
sudo unshare --pid --fork /bin/bash -c '
    sleep 1000 &
    echo "Started background process"
    ps aux
    echo "Exiting PID 1..."
'
# Все процессы в namespace завершатся
```

---

## 6. Network Namespace (CLONE_NEWNET)

Network namespace изолирует сетевой стек: интерфейсы, таблицы маршрутизации, файрвол, сокеты.

### 6.1 Компоненты сетевой изоляции

- Network interfaces (включая loopback)
- IP addresses
- Routing tables
- Firewall rules (iptables/nftables)
- /proc/net, /sys/class/net
- Socket namespaces
- UNIX domain sockets (abstract namespace)

### 6.2 Создание network namespace через ip

```bash
# Создаём network namespace
sudo ip netns add isolated

# Список namespaces
ip netns list

```

**Output:**
```

isolated

```

```bash
# Выполняем команду в namespace
sudo ip netns exec isolated ip link

```

**Output:**
```

1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

```

```bash
# Поднимаем loopback
sudo ip netns exec isolated ip link set lo up

# Создаём veth-пару для связи с host
sudo ip link add veth0 type veth peer name veth1

# Перемещаем один конец в namespace
sudo ip link set veth1 netns isolated

# Настраиваем адреса
sudo ip addr add 10.0.0.1/24 dev veth0
sudo ip link set veth0 up

sudo ip netns exec isolated ip addr add 10.0.0.2/24 dev veth1
sudo ip netns exec isolated ip link set veth1 up

# Проверяем связность
ping -c 1 10.0.0.2

```

**Output:**
```

PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.045 ms

```

### 6.3 Программное создание network namespace

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <string.h>

void list_interfaces() {
    struct if_nameindex *if_ni, *i;
    
    if_ni = if_nameindex();
    if (if_ni == NULL) {
        perror("if_nameindex");
        return;
    }
    
    printf("Network interfaces:\n");
    for (i = if_ni; i->if_index != 0 || i->if_name != NULL; i++) {
        printf("  %d: %s\n", i->if_index, i->if_name);
    }
    
    if_freenameindex(if_ni);
}

int main() {
    printf("=== Before unshare ===\n");
    list_interfaces();
    
    // Создаём новый network namespace
    if (unshare(CLONE_NEWNET) == -1) {
        perror("unshare");
        exit(1);
    }
    
    printf("\n=== After unshare (new network namespace) ===\n");
    list_interfaces();
    
    printf("\nOnly loopback exists, and it's DOWN\n");
    
    return 0;
}

```

### 6.4 Практический пример: изолированная сеть

```bash
#!/bin/bash
# create_network_ns.sh - создание изолированной сети

NS_NAME="mycontainer"

# Создаём namespace
ip netns add $NS_NAME

# Создаём veth-пару
ip link add veth-host type veth peer name veth-ns

# Перемещаем один конец в namespace
ip link set veth-ns netns $NS_NAME

# Настраиваем host-сторону
ip addr add 172.20.0.1/24 dev veth-host
ip link set veth-host up

# Настраиваем namespace-сторону
ip netns exec $NS_NAME ip addr add 172.20.0.2/24 dev veth-ns
ip netns exec $NS_NAME ip link set veth-ns up
ip netns exec $NS_NAME ip link set lo up

# Добавляем маршрут по умолчанию в namespace
ip netns exec $NS_NAME ip route add default via 172.20.0.1

# Включаем NAT для доступа в интернет
iptables -t nat -A POSTROUTING -s 172.20.0.0/24 -j MASQUERADE
echo 1 > /proc/sys/net/ipv4/ip_forward

echo "Network namespace $NS_NAME created"
echo "Enter with: ip netns exec $NS_NAME bash"

```

---

## 7. User Namespace (CLONE_NEWUSER)

User namespace изолирует UID и GID. Позволяет процессу иметь разные привилегии внутри и вне namespace.

### 7.1 UID/GID Mapping

User namespace использует маппинг идентификаторов:

```

Host                    User Namespace
─────────────────       ─────────────────
UID 1000 (user)   ───►  UID 0 (root)
UID 1001              ►  UID 1
UID 1002              ►  UID 2

```

### 7.2 Создание user namespace без root

```bash
# Создаём user namespace (можно без sudo!)
unshare --user --map-root-user /bin/bash

# Проверяем
id

```

**Output:**
```

uid=0(root) gid=0(root) groups=0(root),65534(nogroup)

```

```bash
# Но мы не настоящий root!
cat /etc/shadow  # Permission denied

```

### 7.3 Настройка UID mapping

```bash
# Создаём user namespace
unshare --user /bin/bash &
PID=$!

# Настраиваем mapping (из другого терминала)
echo "0 1000 1" > /proc/$PID/uid_map
echo "0 1000 1" > /proc/$PID/gid_map

# Теперь процесс видит себя как root
```

### 7.4 Программная настройка user namespace

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>

#define STACK_SIZE (1024 * 1024)
static char child_stack[STACK_SIZE];

int child_fn(void *arg) {
    // Ждём пока родитель настроит mapping
    sleep(1);
    
    printf("Child: UID = %d, GID = %d\n", getuid(), getgid());
    printf("Child: Effective UID = %d, Effective GID = %d\n", 
           geteuid(), getegid());
    
    // Проверяем capabilities
    system("cat /proc/self/status | grep Cap");
    
    return 0;
}

void write_mapping(pid_t pid, const char *file, const char *mapping) {
    char path[256];
    snprintf(path, sizeof(path), "/proc/%d/%s", pid, file);
    
    int fd = open(path, O_WRONLY);
    if (fd == -1) {
        perror("open");
        return;
    }
    
    write(fd, mapping, strlen(mapping));
    close(fd);
}

int main() {
    printf("Parent: UID = %d, GID = %d\n", getuid(), getgid());
    
    int flags = CLONE_NEWUSER | SIGCHLD;
    
    pid_t pid = clone(child_fn, child_stack + STACK_SIZE, flags, NULL);
    if (pid == -1) {
        perror("clone");
        exit(1);
    }
    
    // Настраиваем mapping: UID 0 в namespace = наш UID на host
    char mapping[100];
    snprintf(mapping, sizeof(mapping), "0 %d 1\n", getuid());
    write_mapping(pid, "uid_map", mapping);
    
    // Для gid_map нужно сначала отключить setgroups
    write_mapping(pid, "setgroups", "deny\n");
    snprintf(mapping, sizeof(mapping), "0 %d 1\n", getgid());
    write_mapping(pid, "gid_map", mapping);
    
    waitpid(pid, NULL, 0);
    
    return 0;
}

```

### 7.5 Rootless containers

User namespace позволяет запускать контейнеры без root:

```bash
# Podman может работать в rootless режиме
podman run --rm alpine id

```

**Output:**
```

uid=0(root) gid=0(root)

```

Процесс видит себя как root внутри контейнера, но на хосте работает от обычного пользователя.

---

## 8. Cgroup Namespace (CLONE_NEWCGROUP)

Cgroup namespace виртуализирует view иерархии cgroups.

### 8.1 Зачем нужен cgroup namespace

Без cgroup namespace процесс видит полный путь cgroup:
```

/sys/fs/cgroup/cpu/docker/abc123.../

```

С cgroup namespace процесс видит:
```

/sys/fs/cgroup/cpu/

```

### 8.2 Демонстрация cgroup namespace

```bash
# Без cgroup namespace
cat /proc/self/cgroup

```

**Output:**
```

0::/user.slice/user-1000.slice/session-1.scope

```

```bash
# С cgroup namespace
sudo unshare --cgroup /bin/bash
cat /proc/self/cgroup

```

**Output:**
```

0::/

```

---

## 9. Time Namespace (CLONE_NEWTIME)

Time namespace (Linux 5.6+) позволяет иметь разные системные часы в разных namespaces.

### 9.1 Изменение времени в namespace

```bash
# Создаём time namespace со смещением +1 день
sudo unshare --time /bin/bash

# Устанавливаем смещение (в наносекундах)
echo "86400 0" > /proc/self/timens_offsets

# Форкаем процесс, чтобы применить смещение
exec bash

# Проверяем время
date

```

### 9.2 Применение time namespace

- Тестирование time-sensitive приложений
- Воспроизведение багов, связанных со временем
- Изоляция контейнеров с собственным временем

---

## 10. Практическая работа с Namespaces

### 10.1 Утилита unshare

```bash
# Справка
unshare --help

```

**Основные флаги:**
```

--mount, -m       Create mount namespace
--uts, -u         Create UTS namespace
--ipc, -i         Create IPC namespace
--net, -n         Create network namespace
--pid, -p         Create PID namespace
--user, -U        Create user namespace
--cgroup, -C      Create cgroup namespace
--time, -T        Create time namespace

--fork, -f        Fork before executing command
--mount-proc      Mount /proc in new mount namespace
--map-root-user   Map current user to root in user namespace

```

### 10.2 Утилита nsenter

`nsenter` позволяет войти в существующий namespace:

```bash
# Найти PID контейнера
docker inspect --format '{{.State.Pid}}' mycontainer

```

**Output:**
```

12345

```

```bash
# Войти в namespaces контейнера
sudo nsenter --target 12345 --mount --uts --ipc --net --pid /bin/bash

# Или все namespaces сразу
sudo nsenter --target 12345 --all /bin/bash

```

### 10.3 Просмотр namespaces процесса

```bash
# Список namespaces процесса
ls -la /proc/self/ns/

```

**Output:**
```

lrwxrwxrwx 1 user user 0 Dec  1 12:00 cgroup -> 'cgroup:[4026531835]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 ipc -> 'ipc:[4026531839]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 mnt -> 'mnt:[4026531840]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 net -> 'net:[4026531992]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 pid -> 'pid:[4026531836]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 pid_for_children -> 'pid:[4026531836]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 time -> 'time:[4026531834]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 time_for_children -> 'time:[4026531834]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 user -> 'user:[4026531837]'
lrwxrwxrwx 1 user user 0 Dec  1 12:00 uts -> 'uts:[4026531838]'

```

### 10.4 Сравнение namespaces двух процессов

```bash
# Скрипт для сравнения namespaces
#!/bin/bash

compare_ns() {
    local pid1=$1
    local pid2=$2
    
    echo "Comparing namespaces of PID $pid1 and PID $pid2:"
    echo "----------------------------------------"
    
    for ns in cgroup ipc mnt net pid user uts; do
        ns1=$(readlink /proc/$pid1/ns/$ns)
        ns2=$(readlink /proc/$pid2/ns/$ns)
        
        if [ "$ns1" = "$ns2" ]; then
            echo "$ns: SAME ($ns1)"
        else
            echo "$ns: DIFFERENT"
            echo "  PID $pid1: $ns1"
            echo "  PID $pid2: $ns2"
        fi
    done
}

compare_ns $1 $2

```

### 10.5 Создание мини-контейнера

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <string.h>

#define STACK_SIZE (1024 * 1024)
static char child_stack[STACK_SIZE];

struct container_config {
    char *hostname;
    char *rootfs;
    char **argv;
};

int container_main(void *arg) {
    struct container_config *config = arg;
    
    // Устанавливаем hostname
    if (sethostname(config->hostname, strlen(config->hostname)) == -1) {
        perror("sethostname");
        return 1;
    }
    
    // Делаем все монтирования приватными
    if (mount(NULL, "/", NULL, MS_REC | MS_PRIVATE, NULL) == -1) {
        perror("mount private");
        return 1;
    }
    
    // Монтируем новый root
    if (mount(config->rootfs, config->rootfs, NULL, MS_BIND, NULL) == -1) {
        perror("mount bind rootfs");
        return 1;
    }
    
    // Создаём oldroot для pivot_root
    char oldroot[256];
    snprintf(oldroot, sizeof(oldroot), "%s/oldroot", config->rootfs);
    mkdir(oldroot, 0755);
    
    // pivot_root
    if (syscall(SYS_pivot_root, config->rootfs, oldroot) == -1) {
        perror("pivot_root");
        return 1;
    }
    
    // Переходим в новый root
    if (chdir("/") == -1) {
        perror("chdir");
        return 1;
    }
    
    // Размонтируем старый root
    if (umount2("/oldroot", MNT_DETACH) == -1) {
        perror("umount oldroot");
        return 1;
    }
    rmdir("/oldroot");
    
    // Монтируем /proc
    if (mount("proc", "/proc", "proc", 0, NULL) == -1) {
        perror("mount proc");
        return 1;
    }
    
    // Монтируем /sys (readonly)
    if (mount("sysfs", "/sys", "sysfs", MS_RDONLY, NULL) == -1) {
        perror("mount sys");
        // Не критично, продолжаем
    }
    
    // Запускаем процесс
    printf("Container started!\n");
    execvp(config->argv[0], config->argv);
    perror("execvp");
    
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <rootfs> <command> [args...]\n", argv[0]);
        exit(1);
    }
    
    struct container_config config = {
        .hostname = "container",
        .rootfs = argv[1],
        .argv = &argv[2]
    };
    
    int flags = CLONE_NEWNS |      // Mount namespace
                CLONE_NEWUTS |     // UTS namespace
                CLONE_NEWIPC |     // IPC namespace
                CLONE_NEWPID |     // PID namespace
                CLONE_NEWNET |     // Network namespace
                SIGCHLD;
    
    pid_t pid = clone(container_main, 
                      child_stack + STACK_SIZE, 
                      flags, 
                      &config);
    
    if (pid == -1) {
        perror("clone");
        exit(1);
    }
    
    printf("Container PID: %d\n", pid);
    
    int status;
    waitpid(pid, &status, 0);
    
    printf("Container exited with status %d\n", WEXITSTATUS(status));
    
    return WEXITSTATUS(status);
}

```

---

## 💡 Key Takeaways

- **Namespaces** — основа изоляции в Linux-контейнерах, каждый тип изолирует свой ресурс

- **Mount namespace** изолирует файловую систему и точки монтирования

- **PID namespace** даёт контейнеру собственное дерево процессов с PID 1

- **Network namespace** изолирует сетевой стек, veth-пары связывают namespaces

- **User namespace** позволяет rootless-контейнеры и маппинг UID/GID

---

## 🚀 Next Steps

**Related Modules:**

- [Cgroups](../03_Cgroups/) — управление ресурсами
- [OCI](../05_OCI/) — как namespaces используются в стандартах OCI

**Practice Ideas:**

1. Создайте изолированный network namespace с доступом в интернет
2. Напишите программу, которая создаёт мини-контейнер со всеми namespaces
3. Используйте `nsenter` для входа в namespaces Docker-контейнера
4. Исследуйте namespaces реального контейнера через `/proc`

**Going Deeper:**

- Seccomp для ограничения системных вызовов
- Capabilities для гранулярных привилегий
- Rootless containers и их ограничения

---

## 📚 Additional Resources

**Documentation:**

- [namespaces(7) man page](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- [unshare(1) man page](https://man7.org/linux/man-pages/man1/unshare.1.html)
- [nsenter(1) man page](https://man7.org/linux/man-pages/man1/nsenter.1.html)

**Articles:**

- [Namespaces in operation (LWN series)](https://lwn.net/Articles/531114/)
- [Introduction to Linux namespaces](https://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/)

**Books:**

- "Container Security" by Liz Rice — глава 4 о namespaces
- "Linux Kernel Development" by Robert Love — глава о процессах

---




