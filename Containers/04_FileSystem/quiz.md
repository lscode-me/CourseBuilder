# Union Filesystems - Quiz

Проверьте свои знания по теме "Слои образов и Copy-on-Write".

---

## Question 1: Назначение Union FS

Какую основную проблему решают union filesystems?

A) Шифрование данных контейнеров

B) Экономия дискового пространства через переиспользование слоёв

C) Ускорение сетевого обмена

D) Изоляция процессов

---

## Question 2: OverlayFS статус

Начиная с какой версии ядра OverlayFS включена в mainline Linux?

A) 2.6.32

B) 3.0

C) 3.18

D) 4.0

---

## Question 3: Компоненты OverlayFS

Какой компонент OverlayFS является записываемым?

A) lowerdir

B) upperdir

C) workdir

D) merged

---

## Question 4: Copy-on-Write

Что происходит при изменении файла из lower layer в OverlayFS?

A) Файл изменяется на месте в lower layer

B) Файл целиком копируется в upper layer перед изменением

C) Создаётся diff-файл с изменениями

D) Изменения записываются в workdir

---

## Question 5: Whiteout файлы

Что такое whiteout в контексте OverlayFS?

A) Пустой файл для оптимизации

B) Специальный файл, маскирующий удалённый файл из lower layer

C) Файл с правами только на чтение

D) Временный файл для кеширования

---

## Question 6: Приоритет слоёв

Если файл с одинаковым именем существует в нескольких lower layers, какой будет виден?

A) Из самого нижнего layer

B) Из самого верхнего lower layer

C) Случайный

D) Будет ошибка конфликта

---

## Question 7: AUFS vs OverlayFS

Почему Docker перешёл с AUFS на OverlayFS?

A) AUFS быстрее

B) OverlayFS включён в mainline kernel

C) AUFS не поддерживает multiple layers

D) OverlayFS появилась раньше AUFS

---

## Question 8: Docker storage driver

Какой storage driver рекомендуется для Docker?

A) aufs

B) devicemapper

C) overlay2

D) vfs

---

## Question 9: Структура overlay2

Что содержит директория `diff/` в слое overlay2 Docker?

A) Разницу между слоями в бинарном формате

B) Содержимое файлов этого слоя

C) Метаданные слоя

D) Ссылки на другие слои

---

## Question 10: Оптимизация Dockerfile

Какой порядок инструкций в Dockerfile оптимален для кеширования?

A) COPY код → RUN pip install → COPY requirements.txt

B) RUN pip install → COPY requirements.txt → COPY код

C) COPY requirements.txt → RUN pip install → COPY код

D) Порядок не влияет на кеширование

---

## Question 11: Multi-stage builds

Какова главная цель multi-stage builds в Docker?

A) Ускорение сборки

B) Уменьшение размера финального образа

C) Улучшение безопасности

D) Поддержка нескольких архитектур

---

## Question 12: Copy-up overhead

Когда copy-up создаёт наибольший overhead?

A) При создании новых файлов

B) При чтении файлов

C) При изменении больших файлов из lower layer

D) При удалении файлов

---

## Question 13: Metacopy

Что такое metacopy в OverlayFS (kernel 4.19+)?

A) Копирование только метаданных при изменении permissions

B) Копирование файлов между контейнерами

C) Метаданные о слоях образа

D) Шифрование метаданных

---

## Question 14: Docker diff

Что показывает команда `docker diff`?

A) Различия между версиями образа

B) Изменения в файловой системе контейнера (upper layer)

C) Разницу в конфигурации

D) Различия в использовании ресурсов

---

## Question 15: fuse-overlayfs

Для чего используется fuse-overlayfs?

A) Для шифрования overlay

B) Для rootless контейнеров без CAP_SYS_ADMIN

C) Для ускорения overlay

D) Для сжатия данных

---

## Question 16: Btrfs driver

Какое преимущество имеет Btrfs storage driver?

A) Не требует OverlayFS

B) Работает только с root

C) Нативные snapshots и CoW

D) Максимальная совместимость

---

## Question 17: Workdir назначение

Для чего используется workdir в OverlayFS?

A) Хранение временных файлов пользователя

B) Внутренние атомарные операции OverlayFS

C) Логирование операций

D) Хранение метаданных

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

B) Слои образа и команды их создавшие

C) Изменения в конфигурации Docker

D) Историю pull/push операций

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Union FS позволяют переиспользовать общие слои между образами/контейнерами |
| 2 | C | OverlayFS включена в mainline kernel начиная с версии 3.18 |
| 3 | B | upperdir — единственный записываемый слой в OverlayFS |
| 4 | B | Copy-on-Write копирует весь файл в upper layer перед изменением |
| 5 | B | Whiteout — character device 0,0, маскирующий удалённый файл из lower layer |
| 6 | B | Файл из самого верхнего lower layer имеет приоритет |
| 7 | B | OverlayFS в mainline kernel — не нужны патчи, лучше поддержка |
| 8 | C | overlay2 — рекомендуемый storage driver для современного Docker |
| 9 | B | diff/ содержит файлы этого конкретного слоя |
| 10 | C | Сначала requirements.txt, затем pip install, затем код — для оптимального кеширования |
| 11 | B | Multi-stage builds позволяют исключить build tools из финального образа |
| 12 | C | Изменение больших файлов требует копирования всего файла (copy-up) |
| 13 | A | Metacopy копирует только метаданные при изменении permissions/timestamps |
| 14 | B | docker diff показывает изменённые/добавленные/удалённые файлы в контейнере |
| 15 | B | fuse-overlayfs позволяет использовать overlay без root (через FUSE) |
| 16 | C | Btrfs имеет встроенные механизмы CoW и snapshots |
| 17 | B | workdir используется для атомарных операций внутри OverlayFS |
| 18 | B | XFS без ftype=1 не поддерживает d_type, нужный для overlay2 |
| 19 | C | Современный OverlayFS не имеет жёстких ограничений на количество lower layers |
| 20 | B | docker history показывает историю слоёв образа с командами создания |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете union filesystems. Переходите к OCI стандартам. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Copy-on-Write и оптимизацию Dockerfile. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про структуру OverlayFS и Docker storage drivers. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется выполнить практические примеры с OverlayFS вручную. |

---

