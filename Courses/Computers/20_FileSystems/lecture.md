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

**Структура inode:**
```c

struct inode {
    mode_t mode;           // Permissions + file type
    uid_t uid;             // Owner user ID
    gid_t gid;             // Owner group ID
    off_t size;            // File size in bytes
    time_t atime;          // Access time
    time_t mtime;          // Modification time
    time_t ctime;          // Change time
    blkcnt_t blocks;       // Number of 512-byte blocks
    block_t direct[12];    // Direct block pointers
    block_t indirect;      // Single indirect block
    block_t double_indirect;// Double indirect block
    block_t triple_indirect;// Triple indirect block
};
```

**Directory:**

- Файл, содержащий список имён → inode numbers

**Структура directory entry:**
```c

struct dirent {
    ino_t d_ino;           // Inode number
    char d_name[256];      // Filename
};
```

**Пример: Чтение directory**

```c
#include <dirent.h>
#include <stdio.h>

DIR *dir = opendir("/tmp");
struct dirent *entry;

while ((entry = readdir(dir)) != NULL) {
    printf("Inode: %lu, Name: %s\n", 
           entry->d_ino, entry->d_name);
}
closedir(dir);
```

**Block:**

- Минимальная единица выделения (обычно 4 KB)

**Пример: Размер блока влияет на производительность**

```bash
# Создание файловой системы с разными размерами блоков
mkfs.ext4 -b 1024 /dev/sda1   # 1 KB blocks (много маленьких файлов)
mkfs.ext4 -b 4096 /dev/sda1   # 4 KB blocks (стандарт)
mkfs.ext4 -b 8192 /dev/sda1   # 8 KB blocks (большие файлы)
```

**Trade-off:**

- Маленькие блоки: меньше waste для маленьких файлов, но больше overhead
- Большие блоки: лучше для больших файлов, но больше waste для маленьких

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

**Структура MFT Entry:**
```c

// Упрощённая структура
typedef struct {
    uint32_t magic;        // "FILE"
    uint16_t update_seq;   // Sequence number
    uint64_t logfile_seq;  // Log file sequence
    uint16_t link_count;   // Hard link count
    uint16_t attr_offset;  // Offset to attributes
    uint32_t flags;        // File flags
    uint64_t real_size;     // Real file size
    uint64_t allocated_size;// Allocated size
    // Attributes follow (variable length)
} mft_entry;

// Attributes могут быть:
// - $STANDARD_INFORMATION (timestamps, permissions)
// - $FILE_NAME (имя файла)
// - $DATA (данные файла)
// - $ATTRIBUTE_LIST (для больших файлов)
```

**NTFS Features:**

**1. ACL (Access Control Lists):**
```c

// Каждый файл имеет список разрешений
struct acl_entry {
    sid_t sid;              // Security ID (пользователь/группа)
    uint32_t mask;          // Permissions (read, write, execute)
    uint8_t flags;           // Inheritance flags
};
```

**2. Compression:**
```bash
# Включение сжатия на файле/каталоге
compact /c /s:C:\folder

# Проверка сжатых файлов
compact /q C:\folder
```

**3. Encryption (EFS):**
```bash
# Шифрование файла
cipher /e /a file.txt

# Расшифровка
cipher /d /a file.txt
```

**4. Hard Links:**
```bash
# Создание hard link (Windows 10+)
mklink /H link.txt original.txt

# Оба файла указывают на одни данные
# Удаление одного не удаляет данные, пока есть другой

```

**Применение:** Windows default

**Пример: Проверка NTFS**

```bash
# Проверка диска
chkdsk C: /f

# Детальная информация
fsutil fsinfo ntfsinfo C:
```

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

**Процесс записи:**
```

1. Записать намерение в journal: "собираюсь сделать X, Y, Z"
2. Выполнить операции
3. Отметить в journal: "завершено"
```

После сбоя: прочитать journal, доделать незавершённые операции.

**Пример: Journal entry**

```c

// Упрощённая структура journal entry
struct journal_entry {
    uint32_t transaction_id;
    uint32_t block_number;
    uint32_t operation;    // WRITE, DELETE, etc.
    char data[4096];        // Данные блока
    uint32_t checksum;
};

// При записи файла:
// 1. Записать в journal: "буду писать блок 1234"
// 2. Записать блок 1234 в файловую систему
// 3. Записать в journal: "завершено блок 1234"
```

**Trade-off:**

- Надёжность vs производительность (двойная запись)

**Режимы:**

- **Journal = data + metadata:** максимальная надёжность, медленно (2x записи)

- **Journal = metadata only:** быстрее, data может потеряться (только metadata в journal)

- **Writeback:** только порядок операций (быстрее всего, но меньше защиты)

**Пример: Настройка journal режима (ext4)**

```bash
# Проверка текущего режима
dumpe2fs /dev/sda1 | grep "Default mount options"

# Изменение режима (требует remount)
mount -o remount,journal=ordered /dev/sda1 /mnt

# Для постоянного изменения
tune2fs -o journal_data_writeback /dev/sda1
```

**Производительность:**

- Full journal: ~50% overhead (каждая запись дублируется)
- Metadata journal: ~10-20% overhead
- Writeback: ~5% overhead

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

**ZFS Pool (объединение дисков):**
```bash
# Создание ZFS pool (RAID-Z1, аналог RAID5)
zpool create tank raidz1 /dev/sda /dev/sdb /dev/sdc

# Создание файловой системы
zfs create tank/documents

# Создание snapshot
zfs snapshot tank/documents@backup1
# Мгновенно!

```

**Self-healing:**
```c

// ZFS проверяет checksums при чтении
read_block(block_number) {
    data = read_from_disk(block_number);
    checksum = calculate_checksum(data);
    
    if (checksum != stored_checksum) {
        // Corruption обнаружена!
        // Попытка восстановления из mirror/parity
        data = recover_from_redundancy(block_number);
        // Автоматическое исправление
        write_corrected_block(block_number, data);
    }
    return data;
}
```

**Deduplication:**
```bash
# Включение deduplication (требует много RAM!)
zfs set dedup=on tank/documents

# Проверка эффективности

zfs get dedup tank/documents
```

**Compression:**
```bash
# Включение сжатия
zfs set compression=lz4 tank/documents

# Проверка сжатия

zfs get compressratio tank/documents
```

**Применение:** Servers, NAS, FreeBSD, некоторые Linux дистрибутивы

**Пример: ZFS команды**

```bash
# Информация о pool
zpool status tank

# Информация о файловой системе
zfs list
zfs get all tank/documents

# Восстановление из snapshot
zfs rollback tank/documents@backup1

# Клонирование snapshot

zfs clone tank/documents@backup1 tank/documents-clone
```

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

**Как работает:**
```c

// Запись файла
write(fd, data, size);  // 10 MB данных
// FS сжимает на лету
compress(data, size) → compressed_data (3 MB)
write_to_disk(compressed_data);  // Записано 3 MB

// Чтение файла
read_from_disk(compressed_data);  // Читаем 3 MB
decompress(compressed_data) → data;  // Распаковываем в 10 MB
read(fd, buffer, size);  // Приложение получает 10 MB
```

**Алгоритмы:**

- **LZ4:** быстрый, умеренное сжатие (2-3x), низкий CPU overhead

- **ZSTD:** баланс скорости и сжатия (3-5x), средний CPU overhead

- **GZIP/BZIP2:** медленный, высокое сжатие (5-10x), высокий CPU overhead

**Пример: Настройка сжатия**

**Btrfs:**
```bash
# Включение LZ4 сжатия
mount -o compress=lz4 /dev/sda1 /mnt

# Проверка эффективности

btrfs filesystem defragment -r -v /mnt
compsize /mnt  # Показывает сжатие
```

**ZFS:**
```bash
# Включение сжатия
zfs set compression=lz4 tank/documents

# Проверка

zfs get compressratio tank/documents
# compressratio 2.5x означает, что данные сжаты в 2.5 раза

```

**ext4 (только для отдельных файлов):**
```bash
# Использование e4compress (не встроено)

e4compress -c /mnt/file.txt  # Сжатие
e4compress -d /mnt/file.txt  # Распаковка
```

**Когда сжатие ускоряет I/O:**

- Медленный диск (меньше данных читать/писать)
- Сетевые файловые системы (меньше трафика)
- SSD с ограниченной скоростью записи

**Когда сжатие замедляет:**

- Быстрый SSD (CPU overhead больше выгоды)
- Уже сжатые данные (изображения, видео)
- Высокая нагрузка на CPU

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

**Структура exFAT:**
```

- 64-bit file sizes (до 16 EB)
- Улучшенная структура каталогов
- Файловая таблица (как FAT, но расширенная)
```

**Пример: Создание exFAT**

```bash
# Форматирование в exFAT
sudo mkfs.exfat -n "MyUSB" /dev/sdb1

# Монтирование

sudo mount -t exfat /dev/sdb1 /mnt

# Проверка

exfatfsck /dev/sdb1
```

**Применение:** SD карты, флешки >32 GB, внешние диски

**Сравнение FAT32 vs exFAT:**
| Характеристика | FAT32 | exFAT |
|----------------|-------|-------|
| Макс. размер файла | 4 GB | 16 EB |
| Макс. размер тома | 2 TB | 128 PB |
| Совместимость | Везде | Современные системы |
| Сложность | Простая | Простая |

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

**Пример: AWS S3**

```python

import boto3

# Создание клиента
s3 = boto3.client('s3')

# Загрузка объекта
s3.upload_file('local_file.txt', 'my-bucket', 'remote_file.txt')

# Скачивание объекта
s3.download_file('my-bucket', 'remote_file.txt', 'local_file.txt')

# Список объектов

response = s3.list_objects_v2(Bucket='my-bucket')
for obj in response['Contents']:
    print(obj['Key'])
```

**Характеристики:**

- **Плоская структура:** нет каталогов (только префиксы в именах)

- **Metadata:** произвольные ключ-значение пары

- **Версионирование:** можно хранить версии объектов

- **Lifecycle policies:** автоматическое удаление/архивирование

**Применение:**

- Backup и архивирование
- Static website hosting
- Big data storage
- Media storage

**Сравнение с файловыми системами:**
| Характеристика | Файловая система | Объектное хранилище |
|----------------|-----------------|---------------------|
| Структура | Иерархическая | Плоская |
| Доступ | POSIX API | HTTP REST API |
| Метаданные | Ограниченные | Произвольные |
| Масштаб | Терабайты | Петабайты+ |
| Производительность | Низкая latency | Высокая throughput |

---

## 8. Производительность файловых систем

### 8.1 Факторы производительности

**1. Тип нагрузки:**

- **Sequential read/write:** Большие файлы последовательно

- **Random read/write:** Много маленьких файлов случайно

- **Metadata operations:** Создание/удаление файлов

**2. Размер блока:**
```bash
# Большие блоки лучше для больших файлов

mkfs.ext4 -b 8192 /dev/sda1  # 8 KB blocks

# Маленькие блоки лучше для маленьких файлов

mkfs.ext4 -b 1024 /dev/sda1  # 1 KB blocks
```

**3. Фрагментация:**
```bash
# Проверка фрагментации (ext4)
filefrag -v /path/to/file

# Дефрагментация
e4defrag /path/to/file
```

### 8.2 Benchmarking

**Пример: Тест производительности**

```bash
# Sequential write

dd if=/dev/zero of=/mnt/test bs=1M count=1000 oflag=direct

# Random read

fio --name=random-read --ioengine=libaio --iodepth=16 \

    --rw=randread --bs=4k --size=1G --filename=/mnt/test

# Random write

fio --name=random-write --ioengine=libaio --iodepth=16 \

    --rw=randwrite --bs=4k --size=1G --filename=/mnt/test
```

**Типичные результаты (SSD):**

- Sequential read: 500-3000 MB/s
- Sequential write: 400-2000 MB/s
- Random read: 50-200 MB/s
- Random write: 50-150 MB/s

### 8.3 Оптимизация

**1. Выбор файловой системы:**

- **ext4:** Универсальная, хорошая производительность

- **XFS:** Лучше для больших файлов

- **Btrfs:** Лучше для snapshots, но может быть медленнее

- **ZFS:** Максимальная надёжность, но overhead

**2. Mount options:**
```bash
# Оптимизация для SSD

mount -o noatime,nodiratime /dev/sda1 /mnt

# noatime: не обновлять access time (меньше записей)
# nodiratime: не обновлять access time каталогов

```

**3. I/O Scheduler:**
```bash
# Для SSD: noop или none

echo noop > /sys/block/sda/queue/scheduler

# Для HDD: deadline или mq-deadline

echo deadline > /sys/block/sda/queue/scheduler
```

---

## 💡 Key Takeaways

- **Файловые системы** решают организацию данных, надёжность, производительность — выбор зависит от задачи

- **Journaling** обеспечивает consistency при сбоях, но имеет overhead (10-50% в зависимости от режима)

- **Copy-on-Write** FS (Btrfs, ZFS) предоставляют snapshots "бесплатно" и лучшую надёжность через atomic updates

- **Современные FS** включают compression (экономия места, иногда ускорение I/O), deduplication (для VM/backup), checksums (обнаружение corruption)

- **Разные FS для разных задач:** ext4 для общего использования, ZFS для максимальной надёжности, F2FS для flash/SSD, FAT/exFAT для совместимости

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


