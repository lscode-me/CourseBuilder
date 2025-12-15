# Архитектурная безопасность
## Защита на уровне hardware и архитектуры

---

## 📋 Prerequisites

- Понимание архитектуры процессоров
- Знание концепций виртуальной памяти
- Базовые представления об ОС

**Recommended prior modules:**

- [04_ProcessorArchitectures](../04_ProcessorArchitectures/)
- [05_MemoryHierarchy](../05_MemoryHierarchy/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять уровни привилегий и защитные кольца
- Понимать механизмы защиты памяти
- Анализировать hardware vulnerabilities (Spectre, Meltdown)
- Различать security features современных CPU

---

## 1. Уровни привилегий

### 1.1 Protection Rings

**x86 архитектура: 4 уровня (Ring 0-3)**

```

Ring 0: Kernel Mode
  ↓
Ring 1-2: Device Drivers (rarely used)
  ↓
Ring 3: User Mode (приложения)
```

**Что можно делать:**

- Ring 0: всё (I/O, управление памятью, прерывания)
- Ring 3: ограниченный набор инструкций

**Попытка выполнить привилегированную инструкцию в Ring 3:**
→ General Protection Fault (GPF) → OS kill process

### 1.2 ARM: Exception Levels

**EL0 - EL3:**

- EL0: User space
- EL1: Operating System
- EL2: Hypervisor
- EL3: Secure Monitor (TrustZone)

---

## 2. Защита памяти

### 2.1 Memory Protection Unit (MMU)

**Page-level protection:**

Каждая страница имеет флаги:

- **R (Read):** можно читать

- **W (Write):** можно писать

- **X (Execute):** можно выполнять код

**Примеры:**
```

Code section: R-X (можно читать и выполнять, нельзя писать)
Data section: RW- (можно читать/писать, нельзя выполнять)
Stack: RW- (защита от выполнения кода на стеке)
```

### 2.2 NX Bit (No-eXecute)

**AMD: NX bit, Intel: XD bit (eXecute Disable)**

**Проблема:** Buffer overflow может записать код на стек и выполнить его

**Решение:** Страницы стека помечены NX → попытка выполнения → exception

**Эффект:** Защита от многих эксплойтов

### 2.3 ASLR (Address Space Layout Randomization)

**Идея:** Рандомизировать адреса при каждом запуске

```

Process 1:
  Stack at 0x7fff1234
  Libraries at 0x4000abcd

Process 2:
  Stack at 0x7ffe9876
  Libraries at 0x40005678
```

**Эффект:** Атакующий не знает, куда прыгать

**Реализация:** OS + CPU (random generators)

---

## 3. Hardware Vulnerabilities

### 3.1 Spectre (2018)

**Проблема:** Speculative execution + branch prediction

**Как это работает:**
```c

if (x < array_size) {   // Предсказание: true
    y = array[x];       // Спекулятивно выполняется
                        // даже если x >= array_size!
}
```

Спекулятивное выполнение оставляет следы в кэше → timing attack может извлечь данные.

**Эффект:** Утечка данных между процессами

**Mitigation:**

- Microcode updates
- Software barriers (retpoline)
- Performance penalty ~5-30%

### 3.2 Meltdown (2018)

**Проблема:** Kernel memory читается из user space через спекуляцию

```c

// В user space:
char value = *kernel_address;  // должен быть exception
// Но спекулятивно читается ДО проверки прав!
// След остаётся в кэше
```

**Эффект:** Пользовательский процесс читает kernel memory

**Mitigation:**

- KPTI (Kernel Page Table Isolation) — отдельные page tables для kernel и user
- Performance penalty ~5%

### 3.3 Rowhammer (2014)

**Проблема:** Физический дефект DRAM

**Атака:**
```

Быстро читать строки A и C в DRAM
→ Биты в строке B между ними могут flip!
```

**Эффект:** Изменение памяти без записи в неё

**Mitigation:**

- ECC memory
- Targeted Row Refresh (TRR)

---

## 4. Secure Enclaves

### 4.1 Intel SGX (Software Guard Extensions)

**Идея:** Изолированная область памяти (enclave), защищена даже от OS

```

┌──────────────────────┐
│   Enclave Memory     │ ← Encrypted
│  (protected by CPU)  │
├──────────────────────┤
│   Normal Memory      │
└──────────────────────┘
```

**Применение:**

- DRM
- Cryptocurrency wallets
- Secure computation

**Ограничения:**

- Малый размер enclave
- Performance overhead
- Side-channel attacks

### 4.2 ARM TrustZone

**Secure World vs Normal World:**

```

┌─────────────┬─────────────┐
│ Normal World│ Secure World│
│   (Rich OS) │  (Trusted OS│
│   Android   │   OP-TEE)   │
└─────────────┴─────────────┘
```

**Применение:**

- Mobile payments
- Biometric authentication
- DRM

---

## 5. Trusted Platform Module (TPM)

### 5.1 Что такое TPM

**Отдельный чип на материнской плате:**

- Хранит криптографические ключи
- Измеряет boot process (Measured Boot)
- Attestation — доказывает, что система не скомпрометирована

### 5.2 Применение

**BitLocker (Windows):**

- Ключ шифрования диска хранится в TPM
- Невозможно извлечь

**Secure Boot:**

- TPM проверяет подпись bootloader
- Защита от rootkit'ов

---

## 6. Mitigation Techniques

### 6.1 DEP (Data Execution Prevention)

**= NX bit + OS support**

Стек и heap помечены non-executable.

### 6.2 Stack Canaries

**Compiler-generated protection:**

```c

void function() {
    int canary = RANDOM_VALUE;
    char buffer[100];
    // ... код ...
    if (canary != RANDOM_VALUE)
        abort();  // Buffer overflow обнаружен!
}
```

**Trade-off:** Небольшой overhead, но защита от stack overflow

### 6.3 Control Flow Integrity (CFI)

**Идея:** Проверять, что программа прыгает только в легальные места

**Реализация:**

- Compiler adds checks
- CPU features (Intel CET — Control-flow Enforcement Technology)

---

## 💡 Key Takeaways

- **Protection rings** изолируют kernel от user space

- **Memory protection** (NX bit, ASLR) усложняет эксплуатацию уязвимостей

- **Spectre/Meltdown** показали, что speculative execution имеет security implications

- **Secure enclaves** (SGX, TrustZone) защищают данные даже от OS

- **Trade-off:** Security vs Performance — многие mitigation techniques снижают производительность

---

## 🚀 Next Steps

- [25_CloudComputing](../25_CloudComputing/) — Безопасность в облаке
- [26_ModernComputing](../26_ModernComputing/) — Интеграция security в современные системы

---

## 📚 Additional Resources

- **"The Hardware Hacker"** — Andrew "bunnie" Huang
- Intel/AMD security whitepapers
- Spectre & Meltdown papers

---

