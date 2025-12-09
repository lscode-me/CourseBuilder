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

A) Файл изменяется на месте в lower layer

B) Файл целиком копируется в upper layer перед изменением

C) Изменения записываются в workdir

D) Создаётся diff-файл с изменениями

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

A) overlay2

B) vfs

C) aufs

D) devicemapper

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

A) Для ускорения overlay

B) Для rootless контейнеров без CAP_SYS_ADMIN

C) Для сжатия данных

D) Для шифрования overlay

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

A) Логирование операций

B) Внутренние атомарные операции OverlayFS

C) Хранение временных файлов пользователя

D) Хранение метаданных

---

## Question 18: d_type ошибка





Что означает ошибка "upper fs needs to support d_type"?

A) Недостаточно прав доступа

B) Неправильная версия ядра

C) Файловая система не поддерживает overlay

D) Файловая система создана без поддержки directory entry types

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
| 1 | A | Union FS позволяют переиспользовать общие слои между образами/контейнерами |
| 2 | D | OverlayFS включена в mainline kernel начиная с версии 3.18 |
| 3 | C | upperdir — единственный записываемый слой в OverlayFS |
| 4 | B | Copy-on-Write копирует весь файл в upper layer перед изменением |
| 5 | A | Whiteout — character device 0,0, маскирующий удалённый файл из lower layer |
| 6 | B | Файл из самого верхнего lower layer имеет приоритет |
| 7 | A | OverlayFS в mainline kernel — не нужны патчи, лучше поддержка |
| 8 | A | overlay2 — рекомендуемый storage driver для современного Docker |
| 9 | C | diff/ содержит файлы этого конкретного слоя |
| 10 | D | Сначала requirements.txt, затем pip install, затем код — для оптимального кеширования |
| 11 | B | Multi-stage builds позволяют исключить build tools из финального образа |
| 12 | C | Изменение больших файлов требует копирования всего файла (copy-up) |
| 13 | C | Metacopy копирует только метаданные при изменении permissions/timestamps |
| 14 | D | docker diff показывает изменённые/добавленные/удалённые файлы в контейнере |
| 15 | B | fuse-overlayfs позволяет использовать overlay без root (через FUSE) |
| 16 | C | Btrfs имеет встроенные механизмы CoW и snapshots |
| 17 | B | workdir используется для атомарных операций внутри OverlayFS |
| 18 | D | XFS без ftype=1 не поддерживает d_type, нужный для overlay2 |
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

