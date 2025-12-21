# Системы хранения данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы работы компьютеров
- Знать концепцию файлов и файловых систем
- Иметь представление о надёжности систем

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Описать эволюцию систем хранения от магнитных лент до SSD
- Объяснить различия между HDD и SSD
- Понимать роль файловых систем
- Объяснить концепции надёжности и репликации данных

---

## 1. Магнитные ленты

### 1.1 Ранние системы хранения

**Магнитные ленты:**

- Первые системы массового хранения (1950-е)
- Последовательный доступ
- Низкая стоимость хранения
- Медленный доступ

**Структура магнитной ленты:**
```

┌─────────────────────────────────┐
│  Tape Header  │  Data Blocks   │
│  (metadata)   │  (sequential)  │
└─────────────────────────────────┘
```

**Пример: Работа с магнитной лентой**

```c

// Упрощённый пример работы с лентой
void write_to_tape(FILE *tape, void *data, size_t size) {
    // Запись header
    tape_header_t header = {
        .magic = TAPE_MAGIC,
        .size = size,
        .timestamp = time(NULL)
    };
    fwrite(&header, sizeof(header), 1, tape);
    
    // Последовательная запись данных
    fwrite(data, size, 1, tape);
    
    // Синхронизация (физическое перемещение ленты)
    fflush(tape);
}

// Чтение требует перемотки к нужной позиции
void read_from_tape(FILE *tape, void *buffer, size_t size) {
    // Поиск нужного блока (медленно - последовательный доступ)
    tape_header_t header;
    while (fread(&header, sizeof(header), 1, tape) == 1) {
        if (header.magic == TAPE_MAGIC && header.size == size) {
            fread(buffer, size, 1, tape);
            return;
        }
        // Пропуск блока
        fseek(tape, header.size, SEEK_CUR);
    }
}
```

**Применение:**

- Резервное копирование (backup)
- Архивное хранение (long-term storage)
- Массовое хранение данных (data centers)

**Современные ленты (LTO):**
```

LTO-8: 12 TB native, 30 TB compressed
LTO-9: 18 TB native, 45 TB compressed
Скорость: до 400 MB/s
```

**Ограничения:**

- Последовательный доступ (медленно для произвольного доступа)
- Физический износ (ограниченное количество проходов)
- Требуют специального оборудования (tape drives)
- Медленное восстановление данных

### 1.2 Дискеты (Floppy Disks)

**История:**

- 8-inch (1970s): 80 KB
- 5.25-inch (1970s-1980s): 360 KB - 1.2 MB
- 3.5-inch (1980s-2000s): 720 KB - 1.44 MB

**Характеристики:**

- Магнитные диски
- Низкая ёмкость
- Медленный доступ
- Портативность

**Применение:**

- Распространение программ
- Резервное копирование
- Перенос данных

---

## 2. HDD и SSD

### 2.1 Жёсткие диски (HDD)

**HDD (Hard Disk Drive):**

- Магнитные диски (platters)
- Механические движущиеся части
- Большая ёмкость
- Низкая стоимость за гигабайт

**Структура HDD:**
```

┌─────────────────────────┐
│  Platter (магнитный диск)│
│  ├── Track (дорожка)    │
│  │   └── Sector (сектор)│
│  └── Head (головка)     │
│  Actuator (привод)      │
└─────────────────────────┘
```

**Характеристики:**

**Скорость вращения:**

- 5400 RPM: Энергоэффективные, медленные
- 7200 RPM: Стандарт для desktop
- 10000 RPM: Высокопроизводительные (редко)
- 15000 RPM: Enterprise (очень редко)

**Время доступа:**
```c

// Компоненты времени доступа
total_time = seek_time + rotational_latency + transfer_time;

// Seek time: движение головки к нужной дорожке
// ~3-15 ms (зависит от расстояния)

// Rotational latency: ожидание нужного сектора
// ~4-8 ms (половина оборота при 7200 RPM)

// Transfer time: чтение/запись данных
// ~0.1-1 ms (зависит от размера данных)
```

**Пример: Бенчмарк HDD**

```bash
# Тест последовательного чтения
dd if=/dev/sda of=/dev/null bs=1M count=1000
# Типично: 100-200 MB/s

# Тест случайного чтения

fio --name=random-read --ioengine=libaio --iodepth=1 \

    --rw=randread --bs=4k --size=1G --filename=/dev/sda
# Типично: 50-150 IOPS (очень медленно!)

```

**Ёмкость:**

- Desktop: 1-8 TB
- Enterprise: до 20 TB
- Плотность записи: до 2 TB per platter

**Ограничения:**

- Механические части (износ, шум, вибрация)
- Медленнее SSD (особенно random access)
- Чувствительность к вибрации и ударам
- Высокое энергопотребление при работе

**Производительность HDD:**
```

Sequential Read:  100-200 MB/s
Sequential Write: 100-200 MB/s
Random Read:      50-150 IOPS (очень медленно!)
Random Write:     50-150 IOPS
Latency:          5-15 ms
```

### 2.2 Твёрдотельные накопители (SSD)

**SSD (Solid State Drive):**

- Флеш-память (NAND flash)
- Нет движущихся частей
- Быстрый доступ
- Низкое энергопотребление

**Структура NAND Flash:**
```

Block (128-512 KB)
  └── Page (4-16 KB)
      └── Cell (SLC/MLC/TLC/QLC)
```

**Типы NAND Flash:**
```

SLC (Single-Level Cell):  1 bit per cell, быстрый, дорогой, долговечный
MLC (Multi-Level Cell):   2 bits per cell, баланс
TLC (Triple-Level Cell):  3 bits per cell, дешёвый, медленнее
QLC (Quad-Level Cell):    4 bits per cell, самый дешёвый, медленный
```

**Пример: Структура SSD**

```c

// Упрощённая структура SSD
struct ssd_block {
    struct ssd_page pages[64];  // 64 страницы по 4 KB = 256 KB блок
    int erase_count;             // Счётчик стираний (wear leveling)
    int state;                   // FREE, USED, BAD
};

// Wear leveling: равномерное распределение записей
void wear_leveling_write(struct ssd *ssd, uint32_t lba, void *data) {
    // Найти блок с минимальным erase_count
    struct ssd_block *block = find_block_with_min_erases(ssd);
    
    // Записать данные
    write_to_block(block, lba, data);
    
    // Обновить mapping (LBA → физический адрес)
    update_mapping(ssd, lba, block->physical_addr);
}
```

**Преимущества:**

- Быстрый доступ (нет механических задержек)
- Низкая latency (0.1-0.5 ms vs 5-15 ms у HDD)
- Надёжность (нет движущихся частей)
- Тихая работа
- Низкое энергопотребление
- Устойчивость к вибрации

**Производительность SSD:**
```

Sequential Read:  500-3500 MB/s
Sequential Write: 400-3000 MB/s
Random Read:      50,000-500,000 IOPS (в 1000x быстрее HDD!)
Random Write:     30,000-200,000 IOPS
Latency:          0.1-0.5 ms
```

**Ограничения:**

- Выше стоимость за гигабайт (но разрыв сокращается)
- Ограниченное количество циклов записи (P/E cycles)
  - SLC: 100,000 cycles
  - MLC: 10,000 cycles
  - TLC: 3,000 cycles
  - QLC: 1,000 cycles
- Меньшая ёмкость (хотя разрыв сокращается, уже есть 8-16 TB SSD)
- Write amplification (из-за блочной структуры)

**Пример: Бенчмарк SSD**

```bash
# Тест последовательного чтения
dd if=/dev/nvme0n1 of=/dev/null bs=1M count=1000
# Типично: 2000-3500 MB/s

# Тест случайного чтения

fio --name=random-read --ioengine=libaio --iodepth=32 \

    --rw=randread --bs=4k --size=1G --filename=/dev/nvme0n1
# Типично: 50,000-200,000 IOPS
```

**Контроллер SSD:**
```

Функции:
- Wear leveling (равномерный износ)
- Bad block management (управление плохими блоками)
- Garbage collection (очистка неиспользуемых блоков)
- Error correction (ECC)
- Compression (опционально)
```

### 2.3 Сравнение

**Когда использовать HDD:**

- Большие объёмы данных
- Архивное хранение
- Когда стоимость важнее скорости

**Когда использовать SSD:**

- Операционная система
- Часто используемые данные
- Когда скорость важнее стоимости

---

## 3. Файловые системы

### 3.1 Назначение файловых систем

**Файловая система:**

- Организация данных на диске
- Управление пространством
- Контроль доступа
- Метаданные файлов

**Функции:**

- Хранение файлов и директорий
- Отслеживание свободного пространства
- Управление правами доступа
- Обеспечение целостности данных

### 3.2 Типы файловых систем

**FAT/FAT32:**

- Простая файловая система
- Совместимость
- Ограничения по размеру файлов

**NTFS:**

- Файловая система Windows
- Права доступа
- Журналирование

**ext4:**

- Файловая система Linux
- Журналирование
- Большие файлы и разделы

**ZFS:**

- Продвинутая файловая система
- Проверка целостности
- Снимки и клонирование

---

## 4. Надёжность и репликация

### 4.1 Проблема надёжности

**Отказы дисков:**

- Механические отказы (HDD)
- Износ (SSD)
- Ошибки чтения/записи
- Потеря данных

**Последствия:**

- Потеря данных критична
- Необходимость защиты

### 4.2 RAID

**RAID (Redundant Array of Independent Disks):**

- Избыточное хранение данных
- Защита от отказов дисков
- Различные уровни (RAID 0, 1, 5, 6, 10)

**RAID 0 (Striping):**
```

Диск 1: [A1] [A3] [A5]
Диск 2: [A2] [A4] [A6]

Преимущества: Высокая производительность (параллельный доступ)
Недостатки: Нет избыточности (отказ одного диска = потеря всех данных)
Использование: 100% (нет overhead)
```

**RAID 1 (Mirroring):**
```

Диск 1: [A] [B] [C]
Диск 2: [A] [B] [C]  (копия)

Преимущества: Защита от одного отказа, быстрое чтение (параллельное)
Недостатки: 50% overhead (только половина ёмкости используется)
Использование: 50%
```

**Пример: RAID 1 реализация**

```c

// Упрощённая реализация RAID 1
void raid1_write(void *data, size_t size, uint64_t offset) {
    // Запись на оба диска
    write_to_disk(disk1, data, size, offset);
    write_to_disk(disk2, data, size, offset);
    
    // Ожидание завершения обеих записей
    wait_for_completion(disk1);
    wait_for_completion(disk2);
}

void raid1_read(void *buffer, size_t size, uint64_t offset) {
    // Чтение с любого диска (можно с обоих для проверки)
    read_from_disk(disk1, buffer, size, offset);
}
```

**RAID 5:**
```

Диск 1: [A1] [A2] [P1] [A5]
Диск 2: [A3] [P2] [A4] [A6]
Диск 3: [P3] [A7] [A8] [P4]

P = Parity (XOR всех данных)

Преимущества: 
- Защита от одного отказа
- Эффективное использование (n-1)/n
- Хорошая производительность чтения

Недостатки:

- Медленная запись (нужно вычислять parity)
- Проблема при восстановлении (очень медленно)

Использование: (n-1)/n (например, 3 диска = 66.7%)
```

**Пример: RAID 5 parity**

```c

// Вычисление parity для RAID 5
void calculate_parity(char *data1, char *data2, char *parity, size_t size) {
    for (size_t i = 0; i < size; i++) {
        parity[i] = data1[i] ^ data2[i];  // XOR
    }
}

// Восстановление данных при отказе диска
void recover_data(char *data1, char *parity, char *recovered, size_t size) {
    // Если data2 потерян, восстанавливаем через XOR
    for (size_t i = 0; i < size; i++) {
        recovered[i] = data1[i] ^ parity[i];
    }
}
```

**RAID 6:**
```

Два диска для parity (двойная защита)
Защита от двух отказов одновременно
Использование: (n-2)/n
```

**RAID 10 (1+0):**
```

Комбинация RAID 1 и RAID 0
Сначала mirroring, потом striping

Диск 1: [A] [C]     Диск 2: [A] [C]  (mirror)
Диск 3: [B] [D]     Диск 4: [B] [D]  (mirror)

Преимущества: Высокая производительность + надёжность
Недостатки: 50% overhead
```

**Пример: Создание RAID (Linux)**

```bash
# Создание RAID 1
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sda /dev/sdb

# Создание RAID 5
mdadm --create /dev/md0 --level=5 --raid-devices=3 \
    /dev/sda /dev/sdb /dev/sdc

# Проверка статуса

cat /proc/mdstat

# Добавление диска в RAID

mdadm --add /dev/md0 /dev/sdd
```

### 4.3 Репликация

**Репликация данных:**

- Копирование данных на несколько дисков/серверов
- Географическое распределение
- Высокая доступность

**Синхронная репликация:**
```c

// Упрощённый пример синхронной репликации
int sync_replicate(void *data, size_t size) {
    // Запись на primary
    int result1 = write_to_server(primary_server, data, size);
    if (result1 != 0) return -1;
    
    // Запись на replica (ждём подтверждения)
    int result2 = write_to_server(replica_server, data, size);
    if (result2 != 0) {
        // Откат на primary
        rollback(primary_server);
        return -1;
    }
    
    return 0;  // Успех только когда оба сервера подтвердили
}

// Преимущества: Гарантия консистентности
// Недостатки: Высокая latency (ждём оба сервера)
```

**Асинхронная репликация:**
```c

// Упрощённый пример асинхронной репликации
int async_replicate(void *data, size_t size) {
    // Запись на primary (не ждём replica)
    int result = write_to_server(primary_server, data, size);
    if (result != 0) return -1;
    
    // Асинхронная отправка на replica (не ждём)
    async_write_to_server(replica_server, data, size);
    
    return 0;  // Возвращаемся сразу
}

// Преимущества: Низкая latency
// Недостатки: Возможна потеря данных при отказе primary
```

**Типы:**

- **Синхронная репликация:** Гарантия консистентности, высокая latency

- **Асинхронная репликация:** Низкая latency, возможна потеря данных

- **Semi-synchronous:** Компромисс (ждём хотя бы одну replica)

**Географическое распределение:**
```

Primary (US East)
  ├── Replica 1 (US West)      - синхронная
  ├── Replica 2 (Europe)        - асинхронная
  └── Replica 3 (Asia)          - асинхронная
```

**Пример: Репликация в базе данных**

```sql

-- MySQL Master-Slave репликация
-- Master
CHANGE MASTER TO
  MASTER_HOST='replica.example.com',
  MASTER_USER='repl',
  MASTER_PASSWORD='password',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=12345;

START SLAVE;
```

---

## 5. Производительность и оптимизация

### 5.1 Измерение производительности

**Метрики:**

- **Throughput:** MB/s (последовательный доступ)

- **IOPS:** Операций в секунду (случайный доступ)

- **Latency:** Время отклика (ms)

**Пример: Бенчмарк инструменты**

```bash
# fio - гибкий I/O тестер

fio --name=test --ioengine=libaio --iodepth=32 \

    --rw=randread --bs=4k --size=1G --filename=/dev/sda

# dd - простой тест последовательного доступа

dd if=/dev/zero of=testfile bs=1M count=1000 oflag=direct

# hdparm - тест кэша

hdparm -T /dev/sda  # Тест кэша
hdparm -t /dev/sda  # Тест диска
```

### 5.2 Оптимизация производительности

**Для HDD:**

- Дефрагментация (уменьшение seek time)
- Размещение часто используемых данных на внешних дорожках (быстрее)
- RAID 0 для производительности

**Для SSD:**

- TRIM команда (освобождение неиспользуемых блоков)
- Выравнивание разделов (alignment)
- Over-provisioning (резервное пространство для wear leveling)

**Пример: TRIM для SSD**

```bash
# Включение TRIM в Linux

sudo fstrim -v /

# Автоматический TRIM

sudo systemctl enable fstrim.timer
```

---

## 💡 Key Takeaways

- **Эволюция хранения** от магнитных лент к SSD показывает прогресс в скорости (1000x) и надёжности, но с компромиссами по стоимости

- **HDD vs SSD** — компромисс между стоимостью и производительностью: HDD дешевле и больше ёмкость, SSD быстрее (особенно random access) и надёжнее

- **Файловые системы** организуют данные и обеспечивают целостность, выбор зависит от требований (FAT для совместимости, ext4 для Linux, ZFS для надёжности)

- **Надёжность** критически важна — RAID (1, 5, 6, 10) и репликация (синхронная/асинхронная) защищают от потери данных, но с overhead по ёмкости и производительности

- **Выбор системы хранения** зависит от требований: скорость (SSD), стоимость (HDD), надёжность (RAID), доступность (репликация)

---

## 🚀 Next Steps

**Related Modules:**

- [21_Databases](../21_Databases/) — базы данных и ПО для СУБД
- [26_ModernComputing](../26_ModernComputing/) — современные вычисления

**Practice Ideas:**

1. Сравните производительность HDD и SSD
2. Изучите различные файловые системы
3. Исследуйте технологии RAID и репликации

---

## 📚 Additional Resources

**Books:**

- "Database System Concepts" by Silberschatz, Korth, Sudarshan
- Технологии хранения данных

---



