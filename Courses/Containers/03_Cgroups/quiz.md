# Control Groups (cgroups) - Quiz

Проверьте свои знания по теме "Управление и ограничение ресурсов".

---

## Question 1: История cgroups







Какая компания изначально разработала механизм cgroups?

A) Google

B) Microsoft

C) Docker Inc.

D) Red Hat

---

## Question 2: Назначение cgroups







Какова основная функция cgroups?

A) Сетевая виртуализация

B) Изоляция файловой системы

C) Управление и ограничение ресурсов

D) Шифрование данных

---

## Question 3: Cgroups v1 vs v2







В чём главное отличие cgroups v2 от v1?

A) v2 не требует root-прав

B) v2 использует единую иерархию вместо множественной

C) v2 поддерживает больше контроллеров

D) v2 работает только с контейнерами

---

## Question 4: CPU Controller







Какой формат имеет параметр `cpu.max` в cgroups v2?

A) QUOTA PERIOD в микросекундах (например, "50000 100000")

B) Процент CPU (например, "50%")

C) Частота в MHz

D) Количество ядер (например, "2")

---

## Question 5: Memory Controller







Какой параметр устанавливает мягкий лимит памяти в cgroups v2?

A) memory.max

B) memory.limit

C) memory.high

D) memory.soft

---

## Question 6: OOM Killer







Что произойдёт, когда процесс превысит значение `memory.max`?

A) Операции выделения памяти будут блокироваться

B) Процесс будет замедлен (throttled)

C) Процесс получит сигнал SIGTERM

D) Процесс будет убит OOM killer

---

## Question 7: I/O Controller







Какой формат имеет ограничение I/O в параметре `io.max`?

A) Байты в секунду (например, "10485760")

B) Проценты пропускной способности

C) MAJ:MIN параметр=значение (например, "8:0 rbps=10485760")

D) IOPS без указания устройства

---

## Question 8: PIDs Controller







Для чего используется PIDs controller?

A) Изоляция PID namespace

B) Ограничение количества процессов в cgroup

C) Мониторинг процессов

D) Ограничение CPU для каждого процесса

---

## Question 9: systemd интеграция







Какой параметр в unit-файле systemd ограничивает CPU до 50%?

A) CPUQuota=50%

B) CPUMax=50%

C) CPUShares=50%

D) CPULimit=50%

---

## Question 10: Иерархия systemd







Что такое "slice" в терминологии systemd cgroups?

A) Временный сервис

B) Отдельный процесс

C) Группа unit'ов, разделяющих ресурсы

D) Ограничение CPU

---

## Question 11: Файловая система cgroups v2







Где находится файловая система cgroups v2?

A) /proc/cgroups

B) /sys/fs/cgroup

C) /run/cgroups

D) /var/lib/cgroups

---

## Question 12: Добавление процесса







В какой файл нужно записать PID, чтобы добавить процесс в cgroup v2?

A) tasks

B) cgroup.tasks

C) cgroup.pids

D) cgroup.procs

---

## Question 13: CPU weight







Что означает `cpu.weight = 100` в cgroups v2?

A) Относительный вес по умолчанию

B) 100 процессов могут использовать CPU

C) 100% CPU

D) 100 микросекунд CPU

---

## Question 14: Memory pressure







Что показывает файл `memory.pressure`?

A) Текущее использование памяти

B) Информацию о нехватке ресурсов (PSI)

C) Лимит памяти

D) Количество страниц памяти

---

## Question 15: Включение контроллеров







Как включить контроллер memory для дочерних cgroups?

A) `echo "+memory" > /sys/fs/cgroup/cgroup.subtree_control`

B) `systemctl enable cgroup-memory`

C) `mount -t cgroup memory /sys/fs/cgroup/memory`

D) `echo "memory" > /sys/fs/cgroup/cgroup.controllers`

---

## Question 16: Throttling







Когда начинается memory throttling?

A) При достижении 50% от memory.max

B) При достижении memory.max

C) При достижении memory.high

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

A) Топ системных вызовов

B) Использование ресурсов по cgroups

C) Сетевой трафик

D) Топ процессов по PID

---

## Question 19: Наследование







Как процессы наследуют cgroup?

A) Только процессы с тем же UID

B) Дочерние процессы автоматически наследуют cgroup родителя

C) Вручную, нужно добавлять каждый процесс

D) Наследования не существует

---

## Question 20: Graceful degradation







Какой паттерн обеспечивает graceful degradation для памяти?

A) memory.max = memory.high

B) memory.min > memory.high

C) memory.high < memory.max

D) Использование только memory.max

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Google разработал cgroups (тогда "Process Containers") в 2006 году |
| 2 | C | Cgroups управляют и ограничивают ресурсы: CPU, память, I/O, PIDs |
| 3 | B | Cgroups v2 использует единую иерархию для всех контроллеров вместо отдельных |
| 4 | A | cpu.max имеет формат "QUOTA PERIOD" в микросекундах, например "50000 100000" = 50% |
| 5 | C | memory.high — мягкий лимит, при достижении которого начинается throttling |
| 6 | D | При превышении memory.max процесс будет убит OOM killer |
| 7 | C | io.max требует указания устройства в формате MAJ:MIN и параметра |
| 8 | B | PIDs controller ограничивает количество процессов/потоков в cgroup |
| 9 | A | CPUQuota=50% в unit-файле systemd ограничивает CPU до 50% |
| 10 | C | Slice — группа systemd unit'ов, разделяющих ресурсы |
| 11 | B | Cgroups v2 монтируется в /sys/fs/cgroup |
| 12 | D | В cgroups v2 процессы добавляются через файл cgroup.procs |
| 13 | A | cpu.weight=100 — значение по умолчанию, относительный вес для распределения CPU |
| 14 | B | memory.pressure содержит PSI (Pressure Stall Information) — метрики нехватки ресурсов |
| 15 | A | Контроллеры включаются через cgroup.subtree_control с префиксом + |
| 16 | C | Memory throttling начинается при достижении memory.high |
| 17 | A | echo "0" > memory.swap.max полностью отключает swap для cgroup |
| 18 | B | systemd-cgtop показывает использование ресурсов в разрезе cgroups |
| 19 | B | Дочерние процессы автоматически наследуют cgroup родительского процесса |
| 20 | C | memory.high < memory.max: throttling начинается раньше OOM kill |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете cgroups. Переходите к изучению файловых систем контейнеров. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про контроллеры и systemd интеграцию. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про различия v1/v2 и практическую настройку. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется внимательно перечитать лекцию и выполнить практические примеры. |

---

