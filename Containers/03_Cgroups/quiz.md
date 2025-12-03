# Control Groups (cgroups) - Quiz

Проверьте свои знания по теме "Управление и ограничение ресурсов".

---

## Question 1: История cgroups

Какая компания изначально разработала механизм cgroups?

A) Red Hat

B) Google

C) Docker Inc.

D) Microsoft

---

## Question 2: Назначение cgroups

Какова основная функция cgroups?

A) Изоляция файловой системы

B) Управление и ограничение ресурсов

C) Сетевая виртуализация

D) Шифрование данных

---

## Question 3: Cgroups v1 vs v2

В чём главное отличие cgroups v2 от v1?

A) v2 поддерживает больше контроллеров

B) v2 использует единую иерархию вместо множественной

C) v2 работает только с контейнерами

D) v2 не требует root-прав

---

## Question 4: CPU Controller

Какой формат имеет параметр `cpu.max` в cgroups v2?

A) Процент CPU (например, "50%")

B) Частота в MHz

C) QUOTA PERIOD в микросекундах (например, "50000 100000")

D) Количество ядер (например, "2")

---

## Question 5: Memory Controller

Какой параметр устанавливает мягкий лимит памяти в cgroups v2?

A) memory.max

B) memory.high

C) memory.soft

D) memory.limit

---

## Question 6: OOM Killer

Что произойдёт, когда процесс превысит значение `memory.max`?

A) Процесс будет замедлен (throttled)

B) Процесс получит сигнал SIGTERM

C) Процесс будет убит OOM killer

D) Операции выделения памяти будут блокироваться

---

## Question 7: I/O Controller

Какой формат имеет ограничение I/O в параметре `io.max`?

A) Байты в секунду (например, "10485760")

B) MAJ:MIN параметр=значение (например, "8:0 rbps=10485760")

C) Проценты пропускной способности

D) IOPS без указания устройства

---

## Question 8: PIDs Controller

Для чего используется PIDs controller?

A) Ограничение CPU для каждого процесса

B) Изоляция PID namespace

C) Ограничение количества процессов в cgroup

D) Мониторинг процессов

---

## Question 9: systemd интеграция

Какой параметр в unit-файле systemd ограничивает CPU до 50%?

A) CPULimit=50%

B) CPUQuota=50%

C) CPUMax=50%

D) CPUShares=50%

---

## Question 10: Иерархия systemd

Что такое "slice" в терминологии systemd cgroups?

A) Отдельный процесс

B) Группа unit'ов, разделяющих ресурсы

C) Временный сервис

D) Ограничение CPU

---

## Question 11: Файловая система cgroups v2

Где находится файловая система cgroups v2?

A) /proc/cgroups

B) /var/lib/cgroups

C) /sys/fs/cgroup

D) /run/cgroups

---

## Question 12: Добавление процесса

В какой файл нужно записать PID, чтобы добавить процесс в cgroup v2?

A) cgroup.tasks

B) cgroup.procs

C) cgroup.pids

D) tasks

---

## Question 13: CPU weight

Что означает `cpu.weight = 100` в cgroups v2?

A) 100% CPU

B) Относительный вес по умолчанию

C) 100 микросекунд CPU

D) 100 процессов могут использовать CPU

---

## Question 14: Memory pressure

Что показывает файл `memory.pressure`?

A) Текущее использование памяти

B) Лимит памяти

C) Информацию о нехватке ресурсов (PSI)

D) Количество страниц памяти

---

## Question 15: Включение контроллеров

Как включить контроллер memory для дочерних cgroups?

A) `echo "memory" > /sys/fs/cgroup/cgroup.controllers`

B) `echo "+memory" > /sys/fs/cgroup/cgroup.subtree_control`

C) `mount -t cgroup memory /sys/fs/cgroup/memory`

D) `systemctl enable cgroup-memory`

---

## Question 16: Throttling

Когда начинается memory throttling?

A) При достижении memory.max

B) При достижении memory.high

C) При достижении 50% от memory.max

D) Throttling не существует для memory

---

## Question 17: Swap limit

Как полностью отключить swap для cgroup в v2?

A) `echo "0" > memory.swap.max`

B) `echo "disabled" > memory.swap`

C) `echo "noswap" > memory.flags`

D) Swap нельзя отключить для отдельной cgroup

---

## Question 18: systemd-cgtop

Что показывает утилита systemd-cgtop?

A) Топ процессов по PID

B) Использование ресурсов по cgroups

C) Топ системных вызовов

D) Сетевой трафик

---

## Question 19: Наследование

Как процессы наследуют cgroup?

A) Вручную, нужно добавлять каждый процесс

B) Дочерние процессы автоматически наследуют cgroup родителя

C) Только процессы с тем же UID

D) Наследования не существует

---

## Question 20: Graceful degradation

Какой паттерн обеспечивает graceful degradation для памяти?

A) memory.max = memory.high

B) memory.high < memory.max

C) memory.min > memory.high

D) Использование только memory.max

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Google разработал cgroups (тогда "Process Containers") в 2006 году |
| 2 | B | Cgroups управляют и ограничивают ресурсы: CPU, память, I/O, PIDs |
| 3 | B | Cgroups v2 использует единую иерархию для всех контроллеров вместо отдельных |
| 4 | C | cpu.max имеет формат "QUOTA PERIOD" в микросекундах, например "50000 100000" = 50% |
| 5 | B | memory.high — мягкий лимит, при достижении которого начинается throttling |
| 6 | C | При превышении memory.max процесс будет убит OOM killer |
| 7 | B | io.max требует указания устройства в формате MAJ:MIN и параметра |
| 8 | C | PIDs controller ограничивает количество процессов/потоков в cgroup |
| 9 | B | CPUQuota=50% в unit-файле systemd ограничивает CPU до 50% |
| 10 | B | Slice — группа systemd unit'ов, разделяющих ресурсы |
| 11 | C | Cgroups v2 монтируется в /sys/fs/cgroup |
| 12 | B | В cgroups v2 процессы добавляются через файл cgroup.procs |
| 13 | B | cpu.weight=100 — значение по умолчанию, относительный вес для распределения CPU |
| 14 | C | memory.pressure содержит PSI (Pressure Stall Information) — метрики нехватки ресурсов |
| 15 | B | Контроллеры включаются через cgroup.subtree_control с префиксом + |
| 16 | B | Memory throttling начинается при достижении memory.high |
| 17 | A | echo "0" > memory.swap.max полностью отключает swap для cgroup |
| 18 | B | systemd-cgtop показывает использование ресурсов в разрезе cgroups |
| 19 | B | Дочерние процессы автоматически наследуют cgroup родительского процесса |
| 20 | B | memory.high < memory.max: throttling начинается раньше OOM kill |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете cgroups. Переходите к изучению файловых систем контейнеров. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про контроллеры и systemd интеграцию. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про различия v1/v2 и практическую настройку. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию и выполнить практические примеры. |

---

