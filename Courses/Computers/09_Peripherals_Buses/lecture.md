# От ISA до PCIe: как подключаются устройства

---

## 📋 Prerequisites

- Понимание подсистем ввода-вывода
- Базовые знания об архитектуре компьютера

**Recommended prior modules:**

- [08_IO_Subsystems](../08_IO_Subsystems/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять эволюцию шин от ISA до PCIe
- Понимать концепции bandwidth и latency для шин
- Анализировать архитектуру современных шинных систем

---

## 1. Эволюция шин

### 1.1 ISA (Industry Standard Architecture, 1981)

ISA была первой стандартизированной шиной для персональных компьютеров и стала основой для развития шинных архитектур. Она была разработана для IBM PC и стала де-факто стандартом для расширения компьютеров.

**IBM PC:**

ISA была разработана для оригинального IBM PC и стала основой для расширения компьютеров:

- **8-bit, затем 16-bit** — первоначально ISA была 8-битной шиной, что соответствовало возможностям процессора Intel 8088. С появлением процессора Intel 80286 ISA была расширена до 16 бит, что удвоило пропускную способность. 16-битная версия сохраняла обратную совместимость с 8-битными картами, что было важно для защиты инвестиций пользователей

- **8 MHz** — ISA работала на частоте 8 MHz, что соответствовало частоте процессора IBM PC. Это упрощало синхронизацию и снижало стоимость. Однако фиксированная частота ограничивала возможности расширения, так как более быстрые процессоры не могли использовать более высокую скорость шины

- **~8 MB/s bandwidth** — пропускная способность ISA составляла примерно 8 МБ/с, что было достаточно для ранних периферийных устройств, таких как звуковые карты, модемы и сетевые адаптеры. Однако для современных устройств, таких как видеокарты и быстрые диски, этого было недостаточно

- **Простая, дешёвая** — ISA была простой шиной с минимальными требованиями к аппаратуре, что делало её дешёвой в производстве. Это было важно для массового рынка персональных компьютеров. Простота также означала, что разработка карт расширения была относительно простой, что способствовало росту экосистемы устройств

### 1.2 PCI (Peripheral Component Interconnect, 1992)

PCI была разработана Intel как замена ISA и стала стандартом для расширения компьютеров на многие годы. Она решала проблемы ISA и добавляла новые возможности, которые стали критически важными для современных компьютеров.

**Характеристики:**

PCI имела характеристики, которые делали её значительно лучше ISA:

- **32-bit, 33 MHz** — PCI использовала 32-битную шину на частоте 33 MHz, что давало значительно большую пропускную способность по сравнению с ISA. Это было достаточно для большинства устройств того времени, включая сетевые адаптеры, звуковые карты и даже ранние видеокарты. 32-битная шина также упрощала работу с современными процессорами

- **133 MB/s** — пропускная способность PCI составляла 133 МБ/с, что было в 16 раз больше, чем у ISA. Это позволяло подключать более быстрые устройства и улучшало общую производительность системы. Однако для современных устройств, таких как высокопроизводительные видеокарты и быстрые диски, этого стало недостаточно

- **Plug and Play** — PCI поддерживала технологию Plug and Play, которая автоматически определяла подключённые устройства и настраивала их без вмешательства пользователя. Это было революционным изменением по сравнению с ISA, где пользователь должен был вручную настраивать адреса и прерывания. Plug and Play значительно упростила использование компьютеров

- **Shared bus** — PCI использовала общую шину (shared bus), где все устройства подключались к одной шине и делили пропускную способность. Это упрощало архитектуру и снижало стоимость, но создавало проблему конкуренции за пропускную способность между устройствами

**Проблема:** Все устройства делят bandwidth

Основная проблема PCI заключалась в том, что все устройства делили одну шину и конкурировали за пропускную способность. Это означало, что когда одно устройство активно использовало шину, другие устройства должны были ждать. Для устройств с высокими требованиями к пропускной способности, таких как видеокарты, это создавало узкое место. Это ограничение привело к разработке специализированных шин, таких как AGP для видеокарт, и в конечном итоге к переходу на архитектуру point-to-point в PCIe.

### 1.3 AGP (Accelerated Graphics Port, 1997)

**Специально для видеокарт:**

- Dedicated connection
- До 2 GB/s (AGP 8x)

**Устарел:** Заменён PCIe

### 1.4 PCI Express (2003 - настоящее время)

PCI Express (PCIe) стала революционным изменением в архитектуре шин, перейдя от общей шины к архитектуре point-to-point с выделенными линиями для каждого устройства. Это решило проблему конкуренции за пропускную способность и позволило масштабировать производительность в зависимости от потребностей устройства.

**Революция:** От shared bus к point-to-point lanes

Переход от общей шины к архитектуре point-to-point был революционным изменением, которое решило фундаментальные проблемы предыдущих шин:

**Архитектура PCIe:**

Архитектура PCIe кардинально отличается от предыдущих шин:

```

Shared Bus (PCI):
  CPU ──┬── Device 1
        ├── Device 2  (делят bandwidth)
        └── Device 3

Point-to-Point (PCIe):
  CPU ── Device 1 (dedicated lane)
  CPU ── Device 2 (dedicated lane)
  CPU ── Device 3 (dedicated lane)
```

В архитектуре shared bus (PCI) все устройства подключаются к одной шине и конкурируют за пропускную способность. Когда одно устройство активно использует шину, другие устройства должны ждать. Это создаёт узкое место и ограничивает производительность системы.

В архитектуре point-to-point (PCIe) каждое устройство имеет выделенные линии связи с процессором или коммутатором. Это означает, что устройства не конкурируют за пропускную способность и могут работать одновременно на полной скорости. Каждое устройство получает гарантированную пропускную способность, что критически важно для устройств с высокими требованиями к производительности, таких как видеокарты и быстрые диски.

**PCIe Generations:**

| Gen | Year | Per Lane | x16 Bandwidth |
|-----|------|----------|---------------|
| 1.0 | 2003 | 250 MB/s | 4 GB/s |
| 2.0 | 2007 | 500 MB/s | 8 GB/s |
| 3.0 | 2010 | ~1 GB/s | 16 GB/s |
| 4.0 | 2017 | ~2 GB/s | 32 GB/s |
| 5.0 | 2019 | ~4 GB/s | 64 GB/s |
| 6.0 | 2022 | ~8 GB/s | 128 GB/s |

**Lanes:** x1, x4, x8, x16
- GPU: обычно x16 (максимальная производительность)
- NVMe SSD: x4 (достаточно для SSD)
- WiFi card: x1 (низкие требования)
- Sound card: x1

**Пример: Проверка PCIe устройств (Linux)**

```bash
# Просмотр PCIe устройств
lspci

# Детальная информация
lspci -v

# Информация о PCIe слотах
lspci -vv | grep -i "pcie"

# Проверка скорости и ширины
lspci -vv | grep -i "lnksta"
```

**Пример: PCIe configuration space**

```c

// Чтение PCIe configuration (упрощённо)
uint32_t read_pcie_config(uint8_t bus, uint8_t device, 
                          uint8_t function, uint8_t offset) {
    uint32_t address = (1 << 31) |           // Enable bit
                       (bus << 16) | 
                       (device << 11) | 
                       (function << 8) | 
                       (offset & 0xFC);
    
    outl(0xCF8, address);
    return inl(0xCFC);
}

// Чтение vendor ID и device ID
uint16_t vendor_id = read_pcie_config(bus, dev, 0, 0) & 0xFFFF;
uint16_t device_id = (read_pcie_config(bus, dev, 0, 0) >> 16) & 0xFFFF;
```

---

## 2. USB (Universal Serial Bus)

### 2.1 Эволюция USB

**USB 1.0 (1996):**

- 12 Mbps (1.5 MB/s)
- Клавиатуры, мыши

**USB 2.0 (2000):**

- 480 Mbps (60 MB/s)
- "Hi-Speed"

**USB 3.0 (2008):**

- 5 Gbps (625 MB/s)
- "SuperSpeed"

**USB 3.2 (2017):**

- До 20 Gbps (2.5 GB/s)

**USB4 (2019):**

- До 40 Gbps (5 GB/s)
- Based on Thunderbolt 3

### 2.2 USB-C

**Единый коннектор:**

- Reversible (нет "правильной" стороны)
- Power Delivery (до 240W)
- Video output (DisplayPort Alt Mode)
- Универсальный для всех устройств

**USB-C возможности:**
```

Один коннектор для:
- Данные (USB)
- Питание (Power Delivery)
- Видео (DisplayPort/HDMI Alt Mode)
- Аудио
- Thunderbolt 3/4
```

**Пример: USB device enumeration**

```c

// Упрощённый процесс enumeration
void usb_enumerate() {
    // 1. Reset device
    usb_reset();
    
    // 2. Get device descriptor
    usb_get_descriptor(DEVICE_DESCRIPTOR);
    
    // 3. Set address
    usb_set_address(new_address);
    
    // 4. Get configuration descriptor
    usb_get_descriptor(CONFIGURATION_DESCRIPTOR);
    
    // 5. Set configuration
    usb_set_configuration(config_num);
}
```

### 2.3 USB Topology

**USB Hub:**
```

Host Controller
    └── Hub
        ├── Device 1
        ├── Device 2
        └── Hub (nested)
            └── Device 3
```

**Ограничения:**

- Максимум 5 уровней вложенности
- Bandwidth делится между устройствами на одном hub

---

## 3. Storage Interfaces

### 3.1 SATA (Serial ATA)

**SATA 1.0 (2003):** 1.5 Gbps  
**SATA 2.0 (2004):** 3 Gbps  
**SATA 3.0 (2009):** 6 Gbps (~600 MB/s)

**Ограничение:** Недостаточно для современных SSD

### 3.2 NVMe (Non-Volatile Memory Express)

**Протокол для PCIe SSD:**

- Использует PCIe напрямую (без SATA overhead)
- Low latency (меньше слоёв протокола)
- High parallelism (64K queues, 64K commands per queue)

**Архитектура NVMe:**
```

Application
    ↓
NVMe Driver
    ↓
PCIe (bypass SATA)
    ↓
NVMe Controller
    ↓
NAND Flash
```

**Пример: NVMe команда (упрощённо)**

```c

// NVMe command structure
struct nvme_command {
    uint32_t opcode;        // Операция (read/write)
    uint32_t nsid;          // Namespace ID
    uint64_t metadata;      // Metadata pointer
    uint64_t prp1, prp2;    // Data pointers
    uint32_t cdw10, cdw11;  // Command-specific
    // ...
};

// Отправка команды чтения
void nvme_read(uint64_t lba, uint32_t count, void *buffer) {
    struct nvme_command cmd = {
        .opcode = NVME_CMD_READ,
        .nsid = 1,
        .prp1 = (uint64_t)buffer,
        .cdw10 = count - 1,
        .cdw11 = (lba >> 32) & 0xFFFFFFFF,
        .cdw12 = lba & 0xFFFFFFFF,
    };
    
    // Запись команды в submission queue
    nvme_submit_command(&cmd);
    
    // Ожидание completion
    nvme_wait_completion();
}
```

**Performance:**

- SATA SSD: ~550 MB/s (ограничение SATA 3.0)
- NVMe PCIe 3.0 x4: ~3,500 MB/s (6x быстрее SATA)
- NVMe PCIe 4.0 x4: ~7,000 MB/s (12x быстрее SATA)
- NVMe PCIe 5.0 x4: ~14,000 MB/s (25x быстрее SATA)

**Пример: Проверка NVMe (Linux)**

```bash
# Просмотр NVMe устройств
lsblk | grep nvme

# Информация о NVMe
nvme list

# Тест производительности
nvme read /dev/nvme0n1 -s 0 -c 1000 -z 4096
```

### 3.3 Thunderbolt

**Thunderbolt 3/4:**

- До 40 Gbps (5 GB/s)
- Использует USB-C коннектор
- Поддержка PCIe, DisplayPort, USB
- Daisy-chaining (последовательное подключение устройств)

**Применение:**

- External GPUs
- High-speed storage
- 4K/5K displays

---

## 4. Другие интерфейсы

### 4.1 I2C (Inter-Integrated Circuit)

**Низкоскоростная шина для периферии:**

- 100 Kbps - 3.4 Mbps
- Master-Slave архитектура
- Используется для: датчики, EEPROM, RTC

**Пример: Чтение с I2C устройства**

```c

// I2C чтение (упрощённо)
void i2c_read(uint8_t device_addr, uint8_t reg_addr, uint8_t *data) {
    // Start condition
    i2c_start();
    
    // Write device address + write bit
    i2c_write((device_addr << 1) | 0);
    
    // Write register address
    i2c_write(reg_addr);
    
    // Repeated start
    i2c_start();
    
    // Write device address + read bit
    i2c_write((device_addr << 1) | 1);
    
    // Read data
    *data = i2c_read();
    
    // Stop condition
    i2c_stop();
}
```

### 4.2 SPI (Serial Peripheral Interface)

**Высокоскоростная последовательная шина:**

- До 50+ Mbps
- Master-Slave
- Full-duplex (одновременная передача в обе стороны)
- Используется для: flash память, дисплеи, ADC

**Пример: SPI transfer**

```c

// SPI передача (упрощённо)
uint8_t spi_transfer(uint8_t data) {
    // Запись данных в shift register
    SPI_DATA_REG = data;
    
    // Ожидание завершения передачи
    while (!(SPI_STATUS & SPI_TX_COMPLETE));
    
    // Чтение полученных данных
    return SPI_DATA_REG;
}
```

### 4.3 Display Interfaces

**HDMI (High-Definition Multimedia Interface):**

- До 48 Gbps (HDMI 2.1)
- Аудио + видео
- Consumer electronics

**DisplayPort:**

- До 80 Gbps (DP 2.0)
- Превосходит HDMI для компьютеров
- Daisy-chaining

---

## 💡 Key Takeaways

- **Эволюция шин:** От shared buses (ISA, PCI) к point-to-point (PCIe) — каждый device имеет dedicated lane, нет конкуренции за bandwidth

- **PCIe** — доминирующая шина, scalable через lanes (x1, x4, x8, x16), каждая генерация удваивает скорость per lane

- **USB-C** — универсальный коннектор будущего (данные, питание, видео, аудио в одном коннекторе), reversible design

- **NVMe** раскрывает потенциал SSD через PCIe (bypass SATA), обеспечивает низкую latency и высокий parallelism (64K queues)

- **Специализированные шины** (I2C, SPI) для embedded и периферии с разными требованиями по скорости и сложности

---

## 🚀 Next Steps

- [07_Graphics_GPU](../07_Graphics_GPU/) — Как GPU подключается через PCIe
- [08_IO_Subsystems](../08_IO_Subsystems/) — Детали работы с устройствами

---

## 📚 Additional Resources

- PCI-SIG specifications
- USB.org standards
- NVMe specification

---


