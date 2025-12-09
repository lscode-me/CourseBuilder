# Union Filesystems - Quiz

Проверьте свои знания по теме "Слои образов и Copy-on-Write".

---

## Question 1: Назначение Union FS


Какую основную проблему решают union filesystems?

A) Экономия дискового пространства через переиспользование слоёв

B) Ускорение сетевого обмена

C) Изоляция процессов

D) Шифрование данных контейнеров

---

## Question 2: OverlayFS статус


Начиная с какой версии ядра OverlayFS включена в mainline Linux?

A) 4.0

B) 3.18

C) 2.6.32

D) 3.0

---

## Question 3: Компоненты OverlayFS


Какой компонент OverlayFS является записываемым?

A) upperdir

B) merged

C) lowerdir

D) workdir

---

## Question 4: Copy-on-Write


Что происходит при изменении файла из lower layer в OverlayFS?

A) Файл изменяется на месте в lower layer

B) Файл целиком копируется в upper layer перед изменением

C) Изменения записываются в workdir

D) Создаётся diff-файл с изменениями

---

## Question 5: Whiteout файлы


Что такое whiteout в контексте OverlayFS?

A) Временный файл для кеширования

B) Пустой файл для оптимизации

C) Файл с правами только на чтение

D) Специальный файл, маскирующий удалённый файл из lower layer

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

B) AUFS не поддерживает multiple layers

C) AUFS быстрее

D) OverlayFS появилась раньше AUFS

---

## Question 8: Docker storage driver


Какой storage driver рекомендуется для Docker?

A) vfs

B) devicemapper

C) overlay2

D) aufs

---

## Question 9: Структура overlay2


Что содержит директория `diff/` в слое overlay2 Docker?

A) Разницу между слоями в бинарном формате

B) Ссылки на другие слои

C) Содержимое файлов этого слоя

D) Метаданные слоя

---

## Question 10: Оптимизация Dockerfile


Какой порядок инструкций в Dockerfile оптимален для кеширования?

A) RUN pip install → COPY requirements.txt → COPY код

B) COPY код → RUN pip install → COPY requirements.txt

C) COPY requirements.txt → RUN pip install → COPY код

D) Порядок не влияет на кеширование

---

## Question 11: Multi-stage builds


Какова главная цель multi-stage builds в Docker?

A) Улучшение безопасности

B) Уменьшение размера финального образа

C) Поддержка нескольких архитектур

D) Ускорение сборки

---

## Question 12: Copy-up overhead


Когда copy-up создаёт наибольший overhead?

A) При чтении файлов

B) При удалении файлов

C) При создании новых файлов

D) При изменении больших файлов из lower layer

---

## Question 13: Metacopy


Что такое metacopy в OverlayFS (kernel 4.19+)?

A) Метаданные о слоях образа

B) Шифрование метаданных

C) Копирование только метаданных при изменении permissions

D) Копирование файлов между контейнерами

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

A) Для сжатия данных

B) Для шифрования overlay

C) Для rootless контейнеров без CAP_SYS_ADMIN

D) Для ускорения overlay

---

## Question 16: Btrfs driver


Какое преимущество имеет Btrfs storage driver?

A) Нативные snapshots и CoW

B) Максимальная совместимость

C) Работает только с root

D) Не требует OverlayFS

---

## Question 17: Workdir назначение


Для чего используется workdir в OverlayFS?

A) Внутренние атомарные операции OverlayFS

B) Хранение метаданных

C) Логирование операций

D) Хранение временных файлов пользователя

---

## Question 18: d_type ошибка


Что означает ошибка "upper fs needs to support d_type"?

A) Файловая система создана без поддержки directory entry types

B) Недостаточно прав доступа

C) Неправильная версия ядра

D) Файловая система не поддерживает overlay

---

## Question 19: Количество слоёв


Сколько lower layers поддерживает OverlayFS?

A) Максимум 2

B) Практически без ограничений (зависит от системы)

C) Максимум 127

D) Максимум 10

---

## Question 20: Docker history


Что показывает команда `docker history`?

A) Изменения в конфигурации Docker

B) Историю запусков контейнера

C) Историю pull/push операций

D) Слои образа и команды их создавшие

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Union FS позволяют переиспользовать общие слои между образами/контейнерами |
| 2 | B | OverlayFS включена в mainline kernel начиная с версии 3.18 |
| 3 | A | upperdir — единственный записываемый слой в OverlayFS |
| 4 | B | Copy-on-Write копирует весь файл в upper layer перед изменением |
| 5 | D | Whiteout — character device 0,0, маскирующий удалённый файл из lower layer |
| 6 | B | Файл из самого верхнего lower layer имеет приоритет |
| 7 | A | OverlayFS в mainline kernel — не нужны патчи, лучше поддержка |
| 8 | C | overlay2 — рекомендуемый storage driver для современного Docker |
| 9 | C | diff/ содержит файлы этого конкретного слоя |
| 10 | C | Сначала requirements.txt, затем pip install, затем код — для оптимального кеширования |
| 11 | B | Multi-stage builds позволяют исключить build tools из финального образа |
| 12 | D | Изменение больших файлов требует копирования всего файла (copy-up) |
| 13 | C | Metacopy копирует только метаданные при изменении permissions/timestamps |
| 14 | D | docker diff показывает изменённые/добавленные/удалённые файлы в контейнере |
| 15 | C | fuse-overlayfs позволяет использовать overlay без root (через FUSE) |
| 16 | A | Btrfs имеет встроенные механизмы CoW и snapshots |
| 17 | A | workdir используется для атомарных операций внутри OverlayFS |
| 18 | A | XFS без ftype=1 не поддерживает d_type, нужный для overlay2 |
| 19 | B | Современный OverlayFS не имеет жёстких ограничений на количество lower layers |
| 20 | D | docker history показывает историю слоёв образа с командами создания |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете union filesystems. Переходите к OCI стандартам. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Copy-on-Write и оптимизацию Dockerfile. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про структуру OverlayFS и Docker storage drivers. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется выполнить практические примеры с OverlayFS вручную. |

---

