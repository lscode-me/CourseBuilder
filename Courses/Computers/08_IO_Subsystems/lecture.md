# Как компьютер взаимодействует с внешним миром

---

## 📋 Prerequisites

- Понимание архитектуры процессора и памяти
- Базовые знания об устройствах компьютера

**Recommended prior modules:**

- [04_ProcessorArchitectures](../04_ProcessorArchitectures/)
- [05_MemoryHierarchy](../05_MemoryHierarchy/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять различные методы ввода-вывода
- Понимать концепции прерываний и DMA
- Анализировать архитектуру шин и их эволюцию
- Различать memory-mapped I/O и port-mapped I/O

---

## 1. Методы ввода-вывода

### 1.1 Programmed I/O (Polling)

**Простейший метод:** CPU постоянно проверяет готовность устройства

**Пример: Polling UART**

```c

// Простой polling для чтения из UART
#define UART_STATUS  0x10000000
#define UART_DATA    0x10000004
#define STATUS_READY (1 << 0)

char read_uart() {
    // Busy wait - CPU занят ожиданием
    while (!(*(volatile uint32_t*)UART_STATUS & STATUS_READY)) {
        // CPU тратит циклы на проверку
    }
    return *(volatile uint32_t*)UART_DATA;
}

// Проблема: CPU не может делать другую работу
```

**Пример: Polling с задержкой**

```c

// Немного лучше: добавляем небольшую задержку
char read_uart_with_delay() {
    while (!(*(volatile uint32_t*)UART_STATUS & STATUS_READY)) {
        // Небольшая задержка уменьшает нагрузку на шину
        for (volatile int i = 0; i < 1000; i++);
    }
    return *(volatile uint32_t*)UART_DATA;
}
// Но всё равно неэффективно
```

**Проблемы:**

- CPU тратит время на ожидание (busy waiting)
- Неэффективно для медленных устройств
- Высокое энергопотребление
- CPU не может выполнять другую работу

**Когда использовать:**

- Очень быстрые устройства (когда ожидание короткое)
- Real-time системы (предсказуемое время отклика)
- Простые embedded системы

### 1.2 Interrupt-Driven I/O

**Концепция:** Устройство посылает interrupt, когда готово

**Процесс обработки прерывания:**
```

CPU выполняет программу
    ↓
Устройство готово → IRQ (Interrupt Request)
    ↓
CPU сохраняет контекст (registers, flags)
    ↓
Переход к Interrupt Handler (по адресу из IDT)
    ↓
Выполняет Interrupt Handler
    ↓
Восстанавливает контекст
    ↓
Возврат к прерванной программе
```

**Пример: Interrupt handler для UART**

```c

// Interrupt handler (упрощённо)
void uart_interrupt_handler(void) {
    // Проверка источника прерывания
    uint32_t status = *(volatile uint32_t*)UART_STATUS;
    
    if (status & UART_RX_READY) {
        // Данные готовы для чтения
        char data = *(volatile uint32_t*)UART_DATA;
        uart_rx_buffer[uart_rx_index++] = data;
    }
    
    if (status & UART_TX_READY) {
        // Готов к передаче
        if (uart_tx_index < uart_tx_count) {
            *(volatile uint32_t*)UART_DATA = uart_tx_buffer[uart_tx_index++];
        }
    }
    
    // Очистка флага прерывания
    *(volatile uint32_t*)UART_IRQ_CLEAR = 1;
}

// Основная программа может делать другую работу
void main() {
    while (1) {
        // CPU свободен для других задач
        process_data();
        if (uart_rx_index > 0) {
            handle_received_data();
        }
    }
}
```

**Преимущества:**

- CPU может делать полезную работу (не занят ожиданием)
- Быстрая реакция на события (низкая latency)
- Энергоэффективность (CPU может перейти в sleep mode)

**Недостатки:**

- Overhead на переключение контекста
- Сложнее отлаживать
- Может быть нестабильно при высокой частоте прерываний

**Interrupt Controller:**

**Intel 8259 PIC (Programmable Interrupt Controller):**
```

- 8 уровней прерываний (IRQ 0-7)
- Каскадирование до 64 прерываний (master + 8 slaves)
- Программируемые приоритеты
```

**APIC (Advanced PIC):**
```

- Локальный APIC в каждом CPU
- I/O APIC для маршрутизации прерываний
- Поддержка SMP (Symmetric Multiprocessing)
- Message Signaled Interrupts (MSI)
```

**Пример: Настройка прерывания**

```c

// Регистрация interrupt handler
void setup_uart_interrupt() {
    // Установка handler в IDT (Interrupt Descriptor Table)
    idt_set_handler(UART_IRQ_NUM, uart_interrupt_handler);
    
    // Включение прерывания в устройстве
    *(volatile uint32_t*)UART_IRQ_ENABLE = 1;
    
    // Включение прерывания в interrupt controller
    enable_irq(UART_IRQ_NUM);
}
```

### 1.3 Direct Memory Access (DMA)

**Проблема:** Даже с interrupts CPU должен копировать данные

**Без DMA:**
```c

// CPU должен копировать каждый байт
void copy_without_dma(void *dest, void *src, size_t size) {
    for (size_t i = 0; i < size; i++) {
        // CPU занят копированием
        ((char*)dest)[i] = ((char*)src)[i];
    }
    // Для 1 MB это тысячи циклов CPU
}
```

**DMA решение:** Специальный контроллер копирует данные напрямую в память

**Процесс DMA transfer:**
```

1. CPU настраивает DMA:
   - Источник (device buffer)
   - Назначение (memory address)
   - Размер (bytes)
   
2. CPU запускает DMA transfer
   CPU: "DMA, скопируй 1 MB с диска в память по адресу 0x1000000"
   
3. CPU продолжает работу (не занят копированием)
   
4. DMA копирует данные напрямую:
   Device Buffer → DMA Controller → Memory
   
5. DMA посылает interrupt когда готово
   DMA: interrupt "transfer complete"
   
6. CPU обрабатывает interrupt и использует данные
```

**Пример: Использование DMA**

```c

// Настройка DMA для копирования с диска
void setup_dma_transfer(void *dest, size_t size) {
    // Настройка DMA контроллера
    dma_channel_t *channel = &dma_channels[0];
    
    channel->source_addr = DISK_BUFFER_ADDR;
    channel->dest_addr = (uint32_t)dest;
    channel->transfer_size = size;
    channel->control = DMA_ENABLE | DMA_INTERRUPT_ENABLE;
    
    // Запуск transfer
    channel->control |= DMA_START;
    
    // CPU свободен! Может делать другую работу
}

// Interrupt handler для DMA
void dma_interrupt_handler(void) {
    // Transfer завершён
    dma_channels[0].control &= ~DMA_ENABLE;
    
    // Уведомление о готовности данных
    notify_data_ready();
}
```

**Преимущества:**

- CPU свободен во время transfer (может выполнять другую работу)
- High throughput (параллельная работа DMA и CPU)
- Энергоэффективность

**Типы DMA:**

**1. Single Transfer:**
```

Один блок данных за раз
```

**2. Block Transfer:**
```

Весь блок данных за один раз
```

**3. Scatter-Gather DMA:**
```

Копирование из/в несколько несмежных областей памяти
```

**Пример: Scatter-Gather DMA**

```c

// Копирование из нескольких буферов в один
struct dma_sg_entry {
    void *addr;
    size_t len;
};

void scatter_gather_dma(struct dma_sg_entry *entries, int count) {
    dma_sg_table_t *table = allocate_sg_table(count);
    
    for (int i = 0; i < count; i++) {
        table->entries[i].addr = entries[i].addr;
        table->entries[i].len = entries[i].len;
    }
    
    dma_start_sg(table);
}
```

**Ограничения DMA:**

- Требует когерентность кэша (cache coherency)
- Может конфликтовать с CPU доступом к памяти
- Сложнее отлаживать

---

## 2. Memory-Mapped I/O vs Port I/O

### 2.1 Port-Mapped I/O (x86)

**Отдельное адресное пространство для устройств:**

**Assembly примеры:**
```assembly

; Чтение из порта
IN  AL, 0x60    ; читать байт с порта клавиатуры (0x60) в AL
IN  AX, 0x60    ; читать слово (2 байта)
IN  EAX, 0x60   ; читать двойное слово (4 байта)

; Запись в порт
OUT 0x20, AL    ; записать байт из AL в порт 0x20 (PIC)
OUT 0x20, AX    ; записать слово
OUT 0x20, EAX   ; записать двойное слово
```

**C примеры:**
```c

// Встроенные функции для портов
#include <sys/io.h>

// Получить доступ к портам (требует root)
ioperm(0x60, 1, 1);  // Разрешить доступ к порту 0x60

// Чтение
unsigned char data = inb(0x60);      // Байт
unsigned short word = inw(0x60);     // Слово
unsigned int dword = inl(0x60);      // Двойное слово

// Запись
outb(0x20, 0x20);    // Записать байт
outw(0x20, 0x1234);  // Записать слово
outl(0x20, 0x12345678); // Записать двойное слово
```

**Пример: Работа с клавиатурой (PS/2)**

```c

// Чтение scan code с клавиатуры
unsigned char read_keyboard() {
    // Ждать готовности данных
    while (!(inb(0x64) & 0x01)) {
        // Busy wait
    }
    // Читать scan code
    return inb(0x60);
}
```

**Характеристики:**

- Специальные инструкции (IN/OUT) — отдельные от обычных memory access
- Ограниченное пространство (64K портов на x86: 0x0000-0xFFFF)
- Изоляция от памяти (нельзя случайно перезаписать)
- Медленнее чем memory access (специальные инструкции)

**Порты x86:**
```

0x0000-0x03FF: System board (timer, keyboard, etc.)
0x0400-0x04FF: Reserved
0x0500-0x05FF: Reserved
0x0600-0x06FF: Keyboard controller
0x0700-0x07FF: Real-time clock
0x0800-0x08FF: DMA controller
...
```

### 2.2 Memory-Mapped I/O

**Устройства отображаются в адресное пространство памяти:**

**Пример: UART через MMIO**

```c

// Определение регистров UART
#define UART_BASE    0x10000000
#define UART_DATA    (*(volatile uint32_t*)(UART_BASE + 0x00))
#define UART_STATUS  (*(volatile uint32_t*)(UART_BASE + 0x04))
#define UART_CONTROL (*(volatile uint32_t*)(UART_BASE + 0x08))

// Запись символа
void uart_putchar(char c) {
    // Ждать готовности
    while (UART_STATUS & 0x01) {
        // TX busy
    }
    // Записать символ (обычная запись в память!)
    UART_DATA = c;
}

// Чтение символа
char uart_getchar() {
    // Проверить наличие данных
    if (UART_STATUS & 0x02) {
        return UART_DATA;  // Обычное чтение из памяти!
    }
    return -1;
}
```

**Пример: GPIO через MMIO (ARM)**

```c

// GPIO регистры на ARM
#define GPIO_BASE    0x20200000
#define GPIO_FSEL0   (*(volatile uint32_t*)(GPIO_BASE + 0x00))
#define GPIO_SET0    (*(volatile uint32_t*)(GPIO_BASE + 0x1C))
#define GPIO_CLR0    (*(volatile uint32_t*)(GPIO_BASE + 0x28))

// Настройка GPIO как output
void gpio_set_output(int pin) {
    int reg = pin / 10;
    int shift = (pin % 10) * 3;
    GPIO_FSEL0 |= (1 << shift);  // Function Select
}

// Установить pin в HIGH
void gpio_set(int pin) {
    GPIO_SET0 = (1 << pin);  // Просто запись в память!
}

// Установить pin в LOW
void gpio_clear(int pin) {
    GPIO_CLR0 = (1 << pin);  // Просто запись в память!
}
```

**Преимущества:**

- Используются обычные инструкции LOAD/STORE (не нужны специальные IN/OUT)
- Удобнее программировать (как работа с памятью)
- Используется в ARM, RISC-V, MIPS
- Компилятор может оптимизировать (но нужно `volatile`!)

**Важно: `volatile`**

```c

// БЕЗ volatile - компилятор может оптимизировать
uint32_t *uart = (uint32_t*)0x10000000;
*uart = 'A';
*uart = 'B';  // Компилятор может удалить первую запись!

// С volatile - компилятор не оптимизирует
volatile uint32_t *uart = (volatile uint32_t*)0x10000000;
*uart = 'A';  // Гарантированная запись
*uart = 'B';  // Гарантированная запись
```

**Memory map пример (Raspberry Pi):**
```

0x00000000 - 0x3FFFFFFF: RAM
0x20000000 - 0x20FFFFFF: Peripherals (MMIO)
  0x20200000: GPIO
  0x20201000: UART
  0x20215000: SPI
  0x3F000000 - 0x3FFFFFFF: Legacy peripherals
```

---

## 3. Драйверы устройств

### 3.1 Роль драйвера

**Драйвер** — программа, управляющая устройством

**Задачи:**

- Инициализация устройства
- Обработка запросов ОС
- Interrupt handling
- Error recovery

### 3.2 Типы драйверов

**Character devices:**

- Sequential access (последовательный доступ)
- Пример: keyboard, serial port, mouse

**Пример: Character device driver (Linux)**

```c
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>

static struct cdev my_cdev;
static dev_t dev_num;

// File operations
static ssize_t my_read(struct file *file, char __user *buf, 
                       size_t count, loff_t *pos) {
    // Чтение данных из устройства
    char data[] = "Hello from device\n";
    if (copy_to_user(buf, data, strlen(data))) {
        return -EFAULT;
    }
    return strlen(data);
}

static ssize_t my_write(struct file *file, const char __user *buf,
                        size_t count, loff_t *pos) {
    // Запись данных в устройство
    char data[256];
    if (copy_from_user(data, buf, count)) {
        return -EFAULT;
    }
    // Обработка данных
    return count;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .read = my_read,
    .write = my_write,
};

static int __init my_init(void) {
    // Регистрация character device
    alloc_chrdev_region(&dev_num, 0, 1, "mydevice");
    cdev_init(&my_cdev, &fops);
    cdev_add(&my_cdev, dev_num, 1);
    return 0;
}
```

**Block devices:**

- Random access (произвольный доступ), блоками
- Пример: HDD, SSD, USB flash

**Пример: Block device operations**

```c

// Block device operations (упрощённо)
static int my_block_open(struct block_device *bdev, fmode_t mode) {
    // Открытие устройства
    return 0;
}

static void my_block_release(struct gendisk *disk, fmode_t mode) {
    // Закрытие устройства
}

static int my_block_ioctl(struct block_device *bdev, fmode_t mode,
                          unsigned int cmd, unsigned long arg) {
    // IOCTL команды
    switch (cmd) {
        case BLKFLSBUF:
            // Сброс буферов
            break;
    }
    return 0;
}

static struct block_device_operations bops = {
    .owner = THIS_MODULE,
    .open = my_block_open,
    .release = my_block_release,
    .ioctl = my_block_ioctl,
};
```

**Network devices:**

- Packet-based (пакетная передача)
- Пример: Ethernet, WiFi, Bluetooth

**Пример: Network device driver (упрощённо)**

```c
#include <linux/netdevice.h>

// Передача пакета
static int my_net_xmit(struct sk_buff *skb, struct net_device *dev) {
    // Отправка пакета в сеть
    // skb содержит пакет данных
    return NETDEV_TX_OK;
}

// Приём пакета (вызывается из interrupt handler)
static void my_net_rx(struct net_device *dev) {
    struct sk_buff *skb = alloc_skb(MAX_PACKET_SIZE, GFP_ATOMIC);
    
    // Чтение пакета из hardware
    // ...
    
    // Передача пакета в сетевой стек
    netif_rx(skb);
}

static const struct net_device_ops my_net_ops = {
    .ndo_start_xmit = my_net_xmit,
};
```

### 3.3 Структура драйвера

**Типичная структура драйвера:**
```c

// 1. Инициализация
static int __init driver_init(void) {
    // Регистрация устройства
    // Выделение ресурсов
    // Настройка hardware
    return 0;
}

// 2. Обработка запросов
static ssize_t driver_read(...) {
    // Чтение из устройства
}

static ssize_t driver_write(...) {
    // Запись в устройство
}

// 3. Interrupt handling
static irqreturn_t driver_interrupt(int irq, void *dev_id) {
    // Обработка прерывания от устройства
    return IRQ_HANDLED;
}

// 4. Cleanup
static void __exit driver_exit(void) {
    // Освобождение ресурсов
    // Отмена регистрации
}
```

---

## 4. Шины и интерфейсы

### 4.1 PCI (Peripheral Component Interconnect)

**PCI — стандартная шина для подключения периферии:**

**Характеристики:**

- Parallel bus (32-bit или 64-bit)
- Plug and Play (автоматическое определение устройств)
- Configuration space (регистры конфигурации)

**Пример: Чтение PCI configuration**

```c

// Чтение vendor ID и device ID
uint16_t read_pci_config(uint8_t bus, uint8_t device, 
                         uint8_t function, uint8_t offset) {
    uint32_t address = (1 << 31) | 
                       (bus << 16) | 
                       (device << 11) | 
                       (function << 8) | 
                       (offset & 0xFC);
    
    outl(0xCF8, address);
    return (inl(0xCFC) >> ((offset & 2) * 8)) & 0xFFFF;
}

// Поиск устройства
void find_pci_device(uint16_t vendor_id, uint16_t device_id) {
    for (int bus = 0; bus < 256; bus++) {
        for (int device = 0; device < 32; device++) {
            uint16_t vid = read_pci_config(bus, device, 0, 0);
            uint16_t did = read_pci_config(bus, device, 0, 2);
            if (vid == vendor_id && did == device_id) {
                printf("Found at bus %d, device %d\n", bus, device);
            }
        }
    }
}
```

### 4.2 USB (Universal Serial Bus)

**USB — последовательная шина для периферии:**

**Характеристики:**

- Serial bus (последовательная передача)
- Hot-plug (подключение на ходу)
- Power delivery (питание устройств)

**USB скорости:**
```

USB 1.0: 1.5 Mbps (Low Speed)
USB 1.1: 12 Mbps (Full Speed)
USB 2.0: 480 Mbps (High Speed)
USB 3.0: 5 Gbps (SuperSpeed)
USB 3.1: 10 Gbps (SuperSpeed+)
USB 4.0: 40 Gbps
```

**Пример: USB device descriptor**

```c

// USB device descriptor (упрощённо)
struct usb_device_descriptor {
    uint8_t bLength;
    uint8_t bDescriptorType;
    uint16_t bcdUSB;
    uint8_t bDeviceClass;
    uint8_t bDeviceSubClass;
    uint8_t bDeviceProtocol;
    uint8_t bMaxPacketSize0;
    uint16_t idVendor;
    uint16_t idProduct;
    // ...
};
```

### 4.3 SATA (Serial ATA)

**SATA — интерфейс для подключения дисков:**

**Характеристики:**

- Serial interface (последовательный)
- Hot-plug support
- Native Command Queuing (NCQ)

**SATA скорости:**
```

SATA 1.0: 1.5 Gbps (150 MB/s)
SATA 2.0: 3 Gbps (300 MB/s)
SATA 3.0: 6 Gbps (600 MB/s)
SATA 3.2: 16 Gbps (SATA Express)
```

## 5. Буферизация и кэширование

### 5.1 Буферизация I/O

**Проблема:** Устройства работают с разной скоростью

**Решение:** Буферы для временного хранения данных

**Пример: Double buffering**

```c

// Двойная буферизация для плавной передачи
char buffer1[BUFFER_SIZE];
char buffer2[BUFFER_SIZE];
char *current_buffer = buffer1;
char *next_buffer = buffer2;

void write_data(char *data, size_t len) {
    // Запись в текущий буфер
    memcpy(current_buffer, data, len);
    
    // Запуск DMA transfer из текущего буфера
    start_dma_transfer(current_buffer, len);
    
    // Пока DMA работает, подготовка следующего буфера
    prepare_next_buffer(next_buffer);
    
    // Переключение буферов
    swap(&current_buffer, &next_buffer);
}
```

### 5.2 Кэширование устройств

**Кэш для устройств хранения:**

- Read cache: кэширование прочитанных данных
- Write cache: буферизация записей

**Пример: Write-back cache**

```c

// Write-back: запись сначала в кэш
void write_to_disk(char *data, size_t len) {
    // Запись в кэш (быстро)
    cache_write(data, len);
    
    // Асинхронная запись на диск (медленно)
    schedule_disk_write(data, len);
}

// Flush кэша на диск
void flush_cache() {
    // Принудительная запись всех данных из кэша
    for (each cached block) {
        write_block_to_disk(block);
    }
}
```

---

## 💡 Key Takeaways

- **Три метода I/O:** Polling (простой но неэффективный, CPU занят ожиданием), Interrupts (эффективный, CPU свободен), DMA (для bulk transfers, максимальная производительность)

- **Memory-mapped I/O** упрощает программирование устройств (обычные инструкции LOAD/STORE), используется в ARM/RISC-V, но требует `volatile`

- **Port-mapped I/O** использует отдельное адресное пространство (x86), специальные инструкции IN/OUT, ограничено 64K портов

- **Драйверы** изолируют специфику hardware от ОС, три типа: character (sequential), block (random access), network (packet-based)

- **Шины** (PCI, USB, SATA) обеспечивают стандартизированное подключение устройств с разными характеристиками скорости и возможностей

---

## 🚀 Next Steps

- [09_Peripherals_Buses](../09_Peripherals_Buses/) — Детали про шины и периферийные устройства
- [19_Storage](../19_Storage/) — Системы хранения данных

---

## 📚 Additional Resources

- **"Operating Systems: Three Easy Pieces"** — Remzi, Andrea Arpaci-Dusseau (I/O chapters)

- **Linux Device Drivers** — Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman

- **PCI Local Bus Specification**

---


