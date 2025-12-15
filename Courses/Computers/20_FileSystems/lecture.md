# Файловые системы
## От FAT к ZFS: организация данных на дисках

---

## 📋 Prerequisites

- Понимание систем хранения данных
- Базовые знания об операционных системах

**Recommended prior modules:**
- [19_Storage](../19_Storage/)
- [10_UNIX](../10_UNIX/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять основные концепции файловых систем
- Понимать различия между FAT, ext4, NTFS, ZFS и другими FS
- Анализировать journaling и copy-on-write подходы
- Различать применение различных файловых систем

---

## 1. Основы файловых систем

### 1.1 Что такое файловая система

**Задачи FS:**
1. Организация файлов и каталогов
2. Управление свободным пространством
3. Metadata (размер, права, даты)
4. Эффективное использование диска
5. Надёжность и восстановление после сбоев

### 1.2 Базовые концепции

**Inode (Unix):**
- Структура с metadata файла
- Permissions, owner, размер, timestamps
- Указатели на data blocks

**Directory:**
- Файл, содержащий список имён → inode numbers

**Block:**
- Минимальная единица выделения (обычно 4 KB)

---

## 2. Классические файловые системы

### 2.1 FAT (File Allocation Table)

**История:**
- FAT12 (1977): дискеты
- FAT16 (1984): DOS
- FAT32 (1996): Windows 95

**Структура:**
- File Allocation Table — связный список блоков
- Simple, совместима со всем

**Ограничения:**
- Нет journaling → легко повреждается
- FAT32: файлы до 4 GB
- Нет permissions

**Применение:** USB флешки, камеры

### 2.2 ext2/ext3/ext4 (Linux)

**ext2 (1993):**
- Классическая Unix FS
- Inodes, directories, block groups

**ext3 (2001):**
- ext2 + journaling
- Защита от corruption при сбое

**ext4 (2008):**
- Extents (вместо block lists)
- Larger files (до 16 TB)
- Better performance
- Delayed allocation

**Применение:** Linux default

### 2.3 NTFS (Windows)

**Windows NT File System (1993):**
- Journaling (reliability)
- Access Control Lists (ACL)
- File compression
- Encryption (EFS)
- Hard links, symbolic links
- Large files (16 EB теоретически)

**Master File Table (MFT):**
- Аналог inodes, но более гибкий
- Everything is a file (включая metadata)

**Применение:** Windows default

---

## 3. Journaling

### 3.1 Проблема consistency

**Сценарий сбоя:**
```
1. Выделить block для файла
2. Обновить inode
3. Обновить bitmap свободных блоков
```

Если сбой питания между шагами → inconsistency!

### 3.2 Journal

**Решение:** Write-ahead logging

```
1. Записать намерение в journal: "собираюсь сделать X, Y, Z"
2. Выполнить операции
3. Отметить в journal: "завершено"
```

После сбоя: прочитать journal, доделать незавершённые операции.

**Trade-off:**
- Надёжность vs производительность (двойная запись)

**Режимы:**
- **Journal = data + metadata:** максимальная надёжность, медленно
- **Journal = metadata only:** быстрее, data может потеряться
- **Writeback:** только порядок операций

---

## 4. Copy-on-Write FS

### 4.1 Концепция CoW

**Традиционная FS:**
```
Modify block → overwrite in place
```

**CoW FS:**
```
Modify block → write new version, update pointer
```

**Преимущества:**
- Всегда consistent (atomic updates)
- Snapshots "бесплатны"
- No fsck needed

### 4.2 Btrfs (Linux)

**B-tree File System (2009):**
- CoW
- Built-in RAID
- Snapshots, subvolumes
- Compression
- Data checksums

**Применение:** Альтернатива ext4

### 4.3 ZFS (Sun/Oracle)

**Zettabyte File System (2005):**
- CoW
- Software RAID (pools)
- Snapshots
- Data integrity (checksums везде)
- Compression, deduplication
- Self-healing (auto-repair)

**Особенности:**
- Combines FS + Volume Manager
- Очень надёжная

**Применение:** Servers, NAS, FreeBSD

---

## 5. Modern Features

### 5.1 Snapshots

**Идея:** Мгновенный "снимок" FS

**CoW FS:** Snapshot = просто запомнить указатель на root
- Создание: мгновенно
- Занимает место только для изменённых блоков

**Применение:**
- Backup перед обновлением
- Recovery
- Testing

### 5.2 Deduplication

**Идея:** Хранить одинаковые данные один раз

Если два файла имеют одинаковые блоки → один блок, два указателя.

**Trade-off:** CPU/RAM для сравнения vs экономия места

### 5.3 Compression

**On-the-fly сжатие:**
- Transparent для приложений
- Экономит место, может ускорить I/O (меньше чтения с диска)

**Алгоритмы:**
- LZ4: быстрый, умеренное сжатие
- ZSTD: баланс
- GZIP/BZIP2: медленный, высокое сжатие

---

## 6. Специализированные FS

### 6.1 APFS (Apple File System, 2017)

**Замена HFS+:**
- CoW
- Snapshots
- Space sharing между volumes
- Encryption (native)
- Оптимизировано для SSD

### 6.2 F2FS (Flash-Friendly FS)

**Для SSD/flash:**
- Log-structured
- Учитывает износ flash
- Выравнивание на блоки flash

### 6.3 exFAT

**Extended FAT:**
- Нет ограничения 4 GB (FAT32)
- Проще NTFS
- Patent-free (с 2019)

**Применение:** SD карты, флешки >32 GB

---

## 7. Распределённые FS

### 7.1 NFS (Network File System)

**Remote file access:**
- Сервер экспортирует каталоги
- Клиенты монтируют как локальные

### 7.2 Ceph, GlusterFS

**Distributed storage:**
- Данные распределены по множеству серверов
- Replication
- Scalability

### 7.3 Объектные хранилища

**S3, Azure Blob, Google Cloud Storage:**
- Не файловая система (нет иерархии)
- Объекты + metadata
- HTTP API
- Massive scale

---

## 💡 Key Takeaways

- **Файловые системы** решают организацию данных, надёжность, производительность
- **Journaling** обеспечивает consistency при сбоях
- **Copy-on-Write** FS (Btrfs, ZFS) предоставляют snapshots и лучшую надёжность
- **Современные FS** включают compression, deduplication, checksums
- **Разные FS для разных задач:** ext4 для общего использования, ZFS для надёжности, F2FS для flash

---

## 🚀 Next Steps

- [21_Databases](../21_Databases/) — Как СУБД используют FS
- [25_CloudComputing](../25_CloudComputing/) — Объектные хранилища в облаке

---

## 📚 Additional Resources

- **"Operating Systems: Three Easy Pieces"** — File Systems chapters
- ZFS documentation
- Kernel.org documentation (ext4, Btrfs)

---
