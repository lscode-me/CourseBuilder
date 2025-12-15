# Шины, периферия и драйверы
## От ISA до PCIe: как подключаются устройства

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

**IBM PC:**

- 8-bit, затем 16-bit
- 8 MHz
- ~8 MB/s bandwidth
- Простая, дешёвая

### 1.2 PCI (Peripheral Component Interconnect, 1992)

**Характеристики:**

- 32-bit, 33 MHz
- 133 MB/s
- Plug and Play
- Shared bus

**Проблема:** Все устройства делят bandwidth

### 1.3 AGP (Accelerated Graphics Port, 1997)

**Специально для видеокарт:**

- Dedicated connection
- До 2 GB/s (AGP 8x)

**Устарел:** Заменён PCIe

### 1.4 PCI Express (2003 - настоящее время)

**Революция:** От shared bus к point-to-point lanes

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
- GPU: обычно x16
- NVMe SSD: x4
- WiFi card: x1

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

---

## 3. Storage Interfaces

### 3.1 SATA (Serial ATA)

**SATA 1.0 (2003):** 1.5 Gbps  
**SATA 2.0 (2004):** 3 Gbps  
**SATA 3.0 (2009):** 6 Gbps (~600 MB/s)

**Ограничение:** Недостаточно для современных SSD

### 3.2 NVMe (Non-Volatile Memory Express)

**Протокол для PCIe SSD:**

- Использует PCIe напрямую
- Low latency
- High parallelism (64K queues)

**Performance:**

- SATA SSD: ~550 MB/s
- NVMe PCIe 3.0 x4: ~3,500 MB/s
- NVMe PCIe 4.0 x4: ~7,000 MB/s
- NVMe PCIe 5.0 x4: ~14,000 MB/s

---

## 💡 Key Takeaways

- **Эволюция шин:** От shared buses (ISA, PCI) к point-to-point (PCIe)

- **PCIe** — доминирующая шина, scalable через lanes

- **USB-C** — универсальный коннектор будущего

- **NVMe** раскрывает потенциал SSD через PCIe

---

## 📚 Additional Resources

- PCI-SIG specifications
- USB.org standards

---

