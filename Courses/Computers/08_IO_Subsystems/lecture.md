# Подсистемы ввода-вывода
## Как компьютер взаимодействует с внешним миром

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

```c

while (device_not_ready())
    ; // busy wait
read_data_from_device();
```

**Проблемы:**

- CPU тратит время на ожидание
- Неэффективно для медленных устройств

### 1.2 Interrupt-Driven I/O

**Концепция:** Устройство посылает interrupt, когда готово

```

CPU выполняет программу
    ↓
Устройство готово → IRQ (Interrupt Request)
    ↓
CPU сохраняет контекст
    ↓
Выполняет Interrupt Handler
    ↓
Восстанавливает контекст
```

**Преимущества:**

- CPU может делать полезную работу
- Быстрая реакция на события

**Interrupt Controller:**

- Intel 8259 PIC (Programmable Interrupt Controller)
- Современный: APIC (Advanced PIC)

### 1.3 Direct Memory Access (DMA)

**Проблема:** Даже с interrupts CPU должен копировать данные

**DMA решение:** Специальный контроллер копирует данные напрямую в память

```

CPU: "DMA, скопируй 1 MB с диска в память по адресу 0x1000000"
DMA: "OK" (CPU продолжает работу)
...
DMA: копирует данные
DMA: посылает interrupt "готово"
```

**Преимущества:**

- CPU свободен во время transfer
- High throughput

---

## 2. Memory-Mapped I/O vs Port I/O

### 2.1 Port-Mapped I/O (x86)

**Отдельное адресное пространство для устройств:**

```assembly

IN  AL, 0x60    ; читать с порта клавиатуры
OUT 0x20, AL    ; писать в порт
```

**Характеристики:**

- Специальные инструкции (IN/OUT)
- Ограниченное пространство (64K портов на x86)

### 2.2 Memory-Mapped I/O

**Устройства отображаются в адресное пространство памяти:**

```c

volatile uint32_t *uart = (uint32_t *)0x10000000;

*uart = 'A';  // обычная запись в "память" = запись в устройство
```

**Преимущества:**

- Используются обычные инструкции LOAD/STORE
- Удобнее программировать
- Используется в ARM, RISC-V

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

- Sequential access
- Пример: keyboard, serial port

**Block devices:**

- Random access, блоками
- Пример: HDD, SSD

**Network devices:**

- Packet-based
- Пример: Ethernet, WiFi

---

## 💡 Key Takeaways

- **Три метода I/O:** Polling (простой но неэффективный), Interrupts (эффективный), DMA (для bulk transfers)

- **Memory-mapped I/O** упрощает программирование устройств

- **Драйверы** изолируют специфику hardware от ОС

---

## 📚 Additional Resources

- **"Operating Systems: Three Easy Pieces"** — Remzi, Andrea Arpaci-Dusseau (I/O chapters)

---

