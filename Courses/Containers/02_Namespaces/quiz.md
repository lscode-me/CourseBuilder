# Linux Namespaces - Quiz

Проверьте свои знания по теме "Механизмы изоляции ресурсов ядра".

---

## Question 1: Типы Namespaces





Сколько типов namespaces поддерживает современное ядро Linux (5.6+)?

A) 8

B) 10

C) 6

D) 5

---

## Question 2: Mount Namespace





Какой флаг используется для создания mount namespace?

A) CLONE_NEWMNT

B) CLONE_NEWFS

C) CLONE_MOUNT

D) CLONE_NEWNS

---

## Question 3: PID Namespace





Что произойдёт, если процесс PID 1 внутри PID namespace завершится?

A) Ничего, namespace продолжит работать

B) Namespace автоматически перезапустит PID 1

C) Будет выбран новый PID 1 из существующих процессов

D) Все процессы в namespace получат SIGKILL

---

## Question 4: Network Namespace





Что верно для нового network namespace сразу после создания?

A) Он разделяет loopback с хост-системой

B) Он автоматически получает IP-адрес через DHCP

C) Он пустой, нет даже loopback-интерфейса в состоянии UP

D) Он содержит все интерфейсы хост-системы

---

## Question 5: User Namespace





Какое главное преимущество user namespace для контейнеров?

A) Изоляция временных файлов

B) Ускорение работы процессов

C) Возможность запуска контейнеров без root (rootless containers)

D) Автоматическое шифрование данных пользователя

---

## Question 6: UTS Namespace





Что изолирует UTS namespace?

A) Hostname и domain name

B) Unix Time System (системные часы)

C) Пользователей и группы

D) Unix Terminal Settings

---

## Question 7: Системные вызовы





Какой системный вызов используется для присоединения к существующему namespace?

A) enter()

B) setns()

C) attach()

D) join()

---

## Question 8: IPC Namespace





Какие объекты изолирует IPC namespace?

A) System V IPC объекты и POSIX message queues

B) Переменные окружения

C) Сетевые сокеты и порты

D) Файловые дескрипторы

---

## Question 9: veth пары





Для чего используются veth-пары в контексте network namespaces?

A) Для шифрования сетевого трафика

B) Для виртуализации сетевых карт

C) Для мониторинга сетевого трафика

D) Для связи между network namespaces

---

## Question 10: Утилита unshare





Какая команда создаст новый PID namespace с правильно работающим `ps`?

A) `unshare --pid --fork /bin/bash`

B) `unshare --pid --fork --mount-proc /bin/bash`

C) `unshare --pid --mount /bin/bash`

D) `unshare --pid /bin/bash`

---

## Question 11: Хронология namespaces





Какой namespace был добавлен первым в Linux?

A) PID namespace

B) Mount namespace

C) User namespace

D) Network namespace

---

## Question 12: nsenter





Для чего используется утилита `nsenter`?

A) Создание новых namespaces

B) Мониторинг namespaces

C) Удаление namespaces

D) Вход в существующие namespaces процесса

---

## Question 13: Просмотр namespaces





Где находятся файлы namespaces процесса?

A) /sys/namespaces/[PID]/

B) /var/run/ns/[PID]/

C) /proc/[PID]/ns/

D) /etc/ns/[PID]/

---

## Question 14: Cgroup Namespace





Какова основная функция cgroup namespace?

A) Виртуализация видимости иерархии cgroups

B) Создание новых cgroups

C) Ограничение использования CPU

D) Мониторинг ресурсов

---

## Question 15: Mount Propagation





Какой тип mount propagation делает изменения локальными только для текущего namespace?

A) MS_PRIVATE

B) MS_SLAVE

C) MS_SHARED

D) MS_UNBINDABLE

---

## Question 16: User Namespace Mapping





Что определяет файл `/proc/[PID]/uid_map`?

A) Соответствие между UID в namespace и на хосте

B) Историю изменений UID

C) Максимальный UID в namespace

D) Список разрешённых UID для процесса

---

## Question 17: Time Namespace





В какой версии ядра Linux появился time namespace?

A) 5.0

B) 4.6

C) 6.0

D) 5.6

---

## Question 18: clone()





Какой флаг НЕ относится к созданию namespaces?

A) CLONE_NEWNS

B) CLONE_NEWTHREAD

C) CLONE_NEWNET

D) CLONE_NEWPID

---

## Question 19: PID в разных namespaces





Если процесс имеет PID 1 в своём namespace, какой у него PID на хосте?

A) Отрицательное число

B) Любой другой PID, выделенный хост-системой

C) 0

D) Тоже 1

---

## Question 20: Rootless Containers





Какой namespace критически важен для работы rootless-контейнеров?

A) Mount namespace

B) Network namespace

C) User namespace

D) PID namespace

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | 8 типов: Mount, UTS, IPC, PID, Network, User, Cgroup, Time |
| 2 | D | CLONE_NEWNS — исторически первый namespace, поэтому просто "NS" без указания типа |
| 3 | D | PID 1 в namespace особенный: при его завершении все процессы получают SIGKILL |
| 4 | C | Новый network namespace содержит только loopback в состоянии DOWN |
| 5 | C | User namespace позволяет маппить UID, что даёт возможность rootless-контейнеров |
| 6 | A | UTS namespace изолирует hostname и NIS domain name |
| 7 | B | `setns()` присоединяет процесс к существующему namespace по файловому дескриптору |
| 8 | A | IPC namespace изолирует System V IPC (shmem, semaphores, message queues) и POSIX queues |
| 9 | D | veth-пары — виртуальные Ethernet-интерфейсы для связи между network namespaces |
| 10 | B | Нужны --fork (чтобы PID 1 стал shell) и --mount-proc (для корректной работы ps) |
| 11 | B | Mount namespace (CLONE_NEWNS) появился в 2002 году в ядре 2.4.19 |
| 12 | D | nsenter позволяет войти в namespaces существующего процесса |
| 13 | C | Namespaces доступны как символические ссылки в /proc/[PID]/ns/ |
| 14 | A | Cgroup namespace виртуализирует видимость cgroup-иерархии (процесс видит / вместо полного пути) |
| 15 | A | MS_PRIVATE делает изменения монтирования локальными для namespace |
| 16 | A | uid_map определяет маппинг: какой UID в namespace соответствует какому UID на хосте |
| 17 | D | Time namespace появился в Linux 5.6 (2020) |
| 18 | B | CLONE_NEWTHREAD относится к потокам, не к namespaces |
| 19 | B | Процесс имеет разные PID в разных namespaces; на хосте это обычный PID |
| 20 | C | User namespace позволяет маппить UID 0 в контейнере на обычного пользователя на хосте |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете Linux namespaces. Переходите к изучению cgroups. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про PID и Network namespaces. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про системные вызовы и практическую работу с namespaces. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию и выполнить практические примеры. |

---

