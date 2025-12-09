# Control Groups (cgroups) - Quiz

Проверьте свои знания по теме "Управление и ограничение ресурсов".

---

## Question 1: История cgroups


Какая компания изначально разработала механизм cgroups?

A) Microsoft

B) Google

C) Red Hat

D) Docker Inc.

---

## Question 2: Назначение cgroups


Какова основная функция cgroups?

A) Сетевая виртуализация

B) Управление и ограничение ресурсов

C) Изоляция файловой системы

D) Шифрование данных

---

## Question 3: Cgroups v1 vs v2


В чём главное отличие cgroups v2 от v1?

A) v2 не требует root-прав

B) v2 использует единую иерархию вместо множественной

C) v2 работает только с контейнерами

D) v2 поддерживает больше контроллеров

---

## Question 4: CPU Controller


Какой формат имеет параметр `cpu.max` в cgroups v2?

A) Количество ядер (например, "2")

B) Процент CPU (например, "50%")

C) QUOTA PERIOD в микросекундах (например, "50000 100000")

D) Частота в MHz

---

## Question 5: Memory Controller


Какой параметр устанавливает мягкий лимит памяти в cgroups v2?

A) memory.high

B) memory.max

C) memory.limit

D) memory.soft

---

## Question 6: OOM Killer


Что произойдёт, когда процесс превысит значение `memory.max`?

A) Процесс будет убит OOM killer

B) Процесс будет замедлен (throttled)

C) Операции выделения памяти будут блокироваться

D) Процесс получит сигнал SIGTERM

---

## Question 7: I/O Controller


Какой формат имеет ограничение I/O в параметре `io.max`?

A) IOPS без указания устройства

B) MAJ:MIN параметр=значение (например, "8:0 rbps=10485760")

C) Проценты пропускной способности

D) Байты в секунду (например, "10485760")

---

## Question 8: PIDs Controller


Для чего используется PIDs controller?

A) Изоляция PID namespace

B) Ограничение количества процессов в cgroup

C) Ограничение CPU для каждого процесса

D) Мониторинг процессов

---

## Question 9: systemd интеграция


Какой параметр в unit-файле systemd ограничивает CPU до 50%?

A) CPUShares=50%

B) CPULimit=50%

C) CPUQuota=50%

D) CPUMax=50%

---

## Question 10: Иерархия systemd


Что такое "slice" в терминологии systemd cgroups?

A) Группа unit'ов, разделяющих ресурсы

B) Временный сервис

C) Ограничение CPU

D) Отдельный процесс

---

## Question 11: Файловая система cgroups v2


Где находится файловая система cgroups v2?

A) /run/cgroups

B) /var/lib/cgroups

C) /sys/fs/cgroup

D) /proc/cgroups

---

## Question 12: Добавление процесса


В какой файл нужно записать PID, чтобы добавить процесс в cgroup v2?

A) cgroup.procs

B) tasks

C) cgroup.pids

D) cgroup.tasks

---

## Question 13: CPU weight


Что означает `cpu.weight = 100` в cgroups v2?

A) 100% CPU

B) 100 процессов могут использовать CPU

C) 100 микросекунд CPU

D) Относительный вес по умолчанию

---

## Question 14: Memory pressure


Что показывает файл `memory.pressure`?

A) Текущее использование памяти

B) Информацию о нехватке ресурсов (PSI)

C) Количество страниц памяти

D) Лимит памяти

---

## Question 15: Включение контроллеров


Как включить контроллер memory для дочерних cgroups?

A) `systemctl enable cgroup-memory`

B) `echo "memory" > /sys/fs/cgroup/cgroup.controllers`

C) `mount -t cgroup memory /sys/fs/cgroup/memory`

D) `echo "+memory" > /sys/fs/cgroup/cgroup.subtree_control`

---

## Question 16: Throttling


Когда начинается memory throttling?

A) При достижении memory.max

B) Throttling не существует для memory

C) При достижении memory.high

D) При достижении 50% от memory.max

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

A) Использование ресурсов по cgroups

B) Топ системных вызовов

C) Сетевой трафик

D) Топ процессов по PID

---

## Question 19: Наследование


Как процессы наследуют cgroup?

A) Только процессы с тем же UID

B) Наследования не существует

C) Дочерние процессы автоматически наследуют cgroup родителя

D) Вручную, нужно добавлять каждый процесс

---

## Question 20: Graceful degradation


Какой паттерн обеспечивает graceful degradation для памяти?

A) Использование только memory.max

B) memory.max = memory.high

C) memory.min > memory.high

D) memory.high < memory.max

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Google разработал cgroups (тогда "Process Containers") в 2006 году |
| 2 | B | Cgroups управляют и ограничивают ресурсы: CPU, память, I/O, PIDs |
| 3 | B | Cgroups v2 использует единую иерархию для всех контроллеров вместо отдельных |
| 4 | C | cpu.max имеет формат "QUOTA PERIOD" в микросекундах, например "50000 100000" = 50% |
| 5 | A | memory.high — мягкий лимит, при достижении которого начинается throttling |
| 6 | A | При превышении memory.max процесс будет убит OOM killer |
| 7 | B | io.max требует указания устройства в формате MAJ:MIN и параметра |
| 8 | B | PIDs controller ограничивает количество процессов/потоков в cgroup |
| 9 | C | CPUQuota=50% в unit-файле systemd ограничивает CPU до 50% |
| 10 | A | Slice — группа systemd unit'ов, разделяющих ресурсы |
| 11 | C | Cgroups v2 монтируется в /sys/fs/cgroup |
| 12 | A | В cgroups v2 процессы добавляются через файл cgroup.procs |
| 13 | D | cpu.weight=100 — значение по умолчанию, относительный вес для распределения CPU |
| 14 | B | memory.pressure содержит PSI (Pressure Stall Information) — метрики нехватки ресурсов |
| 15 | D | Контроллеры включаются через cgroup.subtree_control с префиксом + |
| 16 | C | Memory throttling начинается при достижении memory.high |
| 17 | A | echo "0" > memory.swap.max полностью отключает swap для cgroup |
| 18 | A | systemd-cgtop показывает использование ресурсов в разрезе cgroups |
| 19 | C | Дочерние процессы автоматически наследуют cgroup родительского процесса |
| 20 | D | memory.high < memory.max: throttling начинается раньше OOM kill |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете cgroups. Переходите к изучению файловых систем контейнеров. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про контроллеры и systemd интеграцию. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про различия v1/v2 и практическую настройку. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию и выполнить практические примеры. |

---

