# Union Filesystems - Quiz

Проверьте свои знания по теме "Слои образов и Copy-on-Write".

---

## Question 1: Назначение Union FS

Какую основную проблему решают union filesystems?

A) Шифрование данных контейнеров

B) Ускорение сетевого обмена

C) Экономия дискового пространства через переиспользование слоёв

D) Изоляция процессов

---

## Question 2: OverlayFS статус

Начиная с какой версии ядра OverlayFS включена в mainline Linux?

A) 2.6.32

B) 3.0

C) 4.0

D) 3.18

---

## Question 3: Компоненты OverlayFS

Какой компонент OverlayFS является записываемым?

A) lowerdir

B) merged

C) upperdir

D) workdir

---

## Question 4: Copy-on-Write

Что происходит при изменении файла из lower layer в OverlayFS?

A) Создаётся diff-файл с изменениями

B) Файл целиком копируется в upper layer перед изменением

C) Файл изменяется на месте в lower layer

D) Изменения записываются в workdir

---

## Question 5: Whiteout файлы

Что такое whiteout в контексте OverlayFS?

A) Специальный файл, маскирующий удалённый файл из lower layer

B) Файл с правами только на чтение

C) Пустой файл для оптимизации

D) Временный файл для кеширования

---

## Question 6: Приоритет слоёв

Если файл с одинаковым именем существует в нескольких lower layers, какой будет виден?

A) Случайный

B) Из самого верхнего lower layer

C) Из самого нижнего layer

D) Будет ошибка конфликта

---

## Question 7: AUFS vs OverlayFS

Почему Docker перешёл с AUFS на OverlayFS?

A) OverlayFS включён в mainline kernel

B) OverlayFS появилась раньше AUFS

C) AUFS быстрее

D) AUFS не поддерживает multiple layers

---

## Question 8: Docker storage driver

Какой storage driver рекомендуется для Docker?

A) devicemapper

B) aufs

C) vfs

D) overlay2

---

## Question 9: Структура overlay2

Что содержит директория `diff/` в слое overlay2 Docker?

A) Содержимое файлов этого слоя

B) Ссылки на другие слои

C) Метаданные слоя

D) Разницу между слоями в бинарном формате

---

## Question 10: Оптимизация Dockerfile

Какой порядок инструкций в Dockerfile оптимален для кеширования?

A) COPY код → RUN pip install → COPY requirements.txt

B) RUN pip install → COPY requirements.txt → COPY код

C) Порядок не влияет на кеширование

D) COPY requirements.txt → RUN pip install → COPY код

---

## Question 11: Multi-stage builds

Какова главная цель multi-stage builds в Docker?

A) Ускорение сборки

B) Уменьшение размера финального образа

C) Поддержка нескольких архитектур

D) Улучшение безопасности

---

## Question 12: Copy-up overhead

Когда copy-up создаёт наибольший overhead?

A) При удалении файлов

B) При чтении файлов

C) При изменении больших файлов из lower layer

D) При создании новых файлов

---

## Question 13: Metacopy

Что такое metacopy в OverlayFS (kernel 4.19+)?

A) Метаданные о слоях образа

B) Копирование файлов между контейнерами

C) Копирование только метаданных при изменении permissions

D) Шифрование метаданных

---

## Question 14: Docker diff

Что показывает команда `docker diff`?

A) Разницу в конфигурации

B) Различия между версиями образа

C) Различия в использовании ресурсов

D) Изменения в файловой системе контейнера (upper layer)

---

## Question 15: fuse-overlayfs

Для чего используется fuse-overlayfs?

A) Для rootless контейнеров без CAP_SYS_ADMIN

B) Для ускорения overlay

C) Для шифрования overlay

D) Для сжатия данных

---

## Question 16: Btrfs driver

Какое преимущество имеет Btrfs storage driver?

A) Работает только с root

B) Не требует OverlayFS

C) Нативные snapshots и CoW

D) Максимальная совместимость

---

## Question 17: Workdir назначение

Для чего используется workdir в OverlayFS?

A) Хранение метаданных

B) Хранение временных файлов пользователя

C) Внутренние атомарные операции OverlayFS

D) Логирование операций

---

## Question 18: d_type ошибка

Что означает ошибка "upper fs needs to support d_type"?

A) Файловая система не поддерживает overlay

B) Файловая система создана без поддержки directory entry types

C) Недостаточно прав доступа

D) Неправильная версия ядра

---

## Question 19: Количество слоёв

Сколько lower layers поддерживает OverlayFS?

A) Максимум 2

B) Максимум 127

C) Практически без ограничений (зависит от системы)

D) Максимум 10

---

## Question 20: Docker history

Что показывает команда `docker history`?

A) Историю запусков контейнера

B) Изменения в конфигурации Docker

C) Слои образа и команды их создавшие

D) Историю pull/push операций

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Union FS позволяют переиспользовать общие слои между образами/контейнерами |
| 2 | D | OverlayFS включена в mainline kernel начиная с версии 3.18 |
| 3 | C | upperdir — единственный записываемый слой в OverlayFS |
| 4 | B | Copy-on-Write копирует весь файл в upper layer перед изменением |
| 5 | A | Whiteout — character device 0,0, маскирующий удалённый файл из lower layer |
| 6 | B | Файл из самого верхнего lower layer имеет приоритет |
| 7 | A | OverlayFS в mainline kernel — не нужны патчи, лучше поддержка |
| 8 | D | overlay2 — рекомендуемый storage driver для современного Docker |
| 9 | A | diff/ содержит файлы этого конкретного слоя |
| 10 | D | Сначала requirements.txt, затем pip install, затем код — для оптимального кеширования |
| 11 | B | Multi-stage builds позволяют исключить build tools из финального образа |
| 12 | C | Изменение больших файлов требует копирования всего файла (copy-up) |
| 13 | C | Metacopy копирует только метаданные при изменении permissions/timestamps |
| 14 | D | docker diff показывает изменённые/добавленные/удалённые файлы в контейнере |
| 15 | A | fuse-overlayfs позволяет использовать overlay без root (через FUSE) |
| 16 | C | Btrfs имеет встроенные механизмы CoW и snapshots |
| 17 | C | workdir используется для атомарных операций внутри OverlayFS |
| 18 | B | XFS без ftype=1 не поддерживает d_type, нужный для overlay2 |
| 19 | C | Современный OverlayFS не имеет жёстких ограничений на количество lower layers |
| 20 | C | docker history показывает историю слоёв образа с командами создания |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете union filesystems. Переходите к OCI стандартам. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Copy-on-Write и оптимизацию Dockerfile. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про структуру OverlayFS и Docker storage drivers. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется выполнить практические примеры с OverlayFS вручную. |

---


