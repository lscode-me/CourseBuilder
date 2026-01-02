# Защита на уровне hardware и архитектуры

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

Одна из фундаментальных проблем многозадачных систем — как предотвратить ситуацию, когда одна программа может повредить другую или саму операционную систему? В ранних системах программы имели полный доступ ко всему компьютеру, что приводило к катастрофическим последствиям при ошибках или злонамеренных действиях.

Решение этой проблемы пришло из academia в 1960-х годах с концепцией protection rings (защитных колец). Идея революционна в своей простоте: разделить код на уровни доверия. Код операционной системы работает в привилегированном режиме с полным доступом к оборудованию, а пользовательские программы — в ограниченном режиме. Это было критически важным прорывом, который сделал возможными современные многозадачные системы.

Архитектура Intel x86, доминировавшая на рынке с 1980-х, реализовала эту концепцию через четыре уровня привилегий. Хотя на практике используются в основном два (Ring 0 для ядра и Ring 3 для приложений), сама идея иерархии привилегий фундаментально изменила способ проектирования операционных систем.

**x86 архитектура: 4 уровня (Ring 0-3)**

```
Ring 0: Kernel Mode
  ↓
Ring 1-2: Device Drivers (rarely used)
  ↓
Ring 3: User Mode (приложения)
```

**Что можно делать:**

Разделение на уровни привилегий определяет, какие операции может выполнять код на каждом уровне:

- **Ring 0: всё (I/O, управление памятью, прерывания)** — код в Ring 0 имеет полный доступ ко всем ресурсам системы. Это включает прямой доступ к портам ввода-вывода, управление виртуальной памятью, обработку прерываний и другие критически важные операции. Только ядро операционной системы работает в Ring 0, что критически важно для безопасности: ошибка в коде Ring 0 может привести к краху всей системы

- **Ring 3: ограниченный набор инструкций** — пользовательские приложения работают в Ring 3 с ограниченным набором доступных операций. Они не могут напрямую обращаться к оборудованию, изменять таблицы страниц памяти или выполнять другие привилегированные операции. Это критически важно для изоляции: приложение не может повредить другие приложения или операционную систему

**Попытка выполнить привилегированную инструкцию в Ring 3:**
→ General Protection Fault (GPF) → OS kill process

Когда код в Ring 3 пытается выполнить привилегированную инструкцию, процессор генерирует исключение General Protection Fault. Это аппаратная защита, которая предотвращает выполнение опасных операций. Операционная система получает это исключение и может завершить процесс, который пытался выполнить недопустимую операцию. Это критически важно для безопасности: даже если приложение содержит ошибку или вредоносный код, оно не может повредить систему благодаря аппаратной защите

### 1.2 ARM: Exception Levels

**EL0 - EL3:**

- EL0: User space
- EL1: Operating System
- EL2: Hypervisor
- EL3: Secure Monitor (TrustZone)

---

## 2. Защита памяти

### 2.1 Memory Protection Unit (MMU)

Вместе с концепцией виртуальной памяти пришло осознание, что MMU может делать не только трансляцию адресов, но и контролировать доступ к памяти. Это было революционным расширением функциональности: один и тот же механизм, который обеспечивает изоляцию адресных пространств процессов, теперь может контролировать, что именно можно делать с каждой страницей памяти.

Особенно критически важным стал контроль исполнения кода. В 1990-х и 2000-х годах основной класс атак — buffer overflow — работал именно так: переполнение буфера позволяло записать вредоносный код в память, а затем передать управление на него. Добавление бита NX (No eXecute) было фундаментальным улучшением безопасности, которое значительно усложнило эксплуатацию уязвимостей.

**Page-level protection:**

Каждая страница памяти имеет флаги доступа, которые процессор проверяет при каждом обращении. Это критически важный механизм защиты, работающий на аппаратном уровне:

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

**Без ASLR:**
```
Process 1:
  Stack at 0x7fff1234
  Libraries at 0x4000abcd

Process 2:
  Stack at 0x7fff1234  // Тот же адрес!
  Libraries at 0x4000abcd  // Тот же адрес!
```

**С ASLR:**
```
Process 1:
  Stack at 0x7fff1234
  Libraries at 0x4000abcd

Process 2:
  Stack at 0x7ffe9876  // Другой адрес!
  Libraries at 0x40005678  // Другой адрес!
```

**Эффект:** Атакующий не знает, куда прыгать

**Пример: Эксплойт без ASLR**

```c
// Атакующий знает адрес функции system()
void exploit() {
    char buffer[100];
    // ... overflow buffer ...
    // Перезаписать return address на известный адрес
    *((void**)&buffer[100]) = (void*)0x4000abcd;  // system()
}
```

**С ASLR:**
```c
// Атакующий не знает адрес (он меняется каждый запуск)
void exploit() {
    char buffer[100];
    // ... overflow buffer ...
    // Куда прыгать? Адрес неизвестен!
    // Эксплойт не работает
}
```

**Реализация:** OS + CPU (random generators)

**Проверка ASLR:**
```bash
# Проверка статуса ASLR в Linux

cat /proc/sys/kernel/randomize_va_space
# 0 = отключено
# 1 = частично (только stack)
# 2 = полностью включено

# Включение ASLR

echo 2 > /proc/sys/kernel/randomize_va_space
```

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

**Проблема без CFI:**
```c
// Атакующий может перезаписать function pointer
void (*func_ptr)() = legitimate_function;
// ... overflow ...
func_ptr = attacker_code;  // Перезапись
func_ptr();  // Выполнение attacker code
```

**С CFI:**
```c
// CFI добавляет проверки
void (*func_ptr)() = legitimate_function;
// ... overflow ...
func_ptr = attacker_code;  // Перезапись
// CFI проверка перед вызовом
if (!is_valid_target(func_ptr)) {
    abort();  // Нелегальный target!
}
func_ptr();
```

**Реализация:**

**1. Compiler-based CFI (LLVM):**
```bash
# Включение CFI в LLVM

clang -fsanitize=cfi program.c
```

**2. Hardware CFI (Intel CET):**
```
- Indirect Branch Tracking (IBT): Защита indirect calls/jumps
- Shadow Stack: Отдельный стек для return addresses
```

**Пример: Shadow Stack**

```
Normal Stack:          Shadow Stack:
[return addr 1]  ←→   [return addr 1]
[local vars]          [protected copy]
[return addr 2]  ←→   [return addr 2]

При return: проверка совпадения адресов
Если не совпадают → abort()
```

**Включение Intel CET:**
```bash
# Требует поддержку в CPU и OS
# Проверка поддержки

grep cet /proc/cpuinfo

# Компиляция с CET

gcc -fcf-protection=full program.c
```

### 6.4 Address Sanitizer (ASan)

**Runtime detection of memory errors:**

```c
// ASan обнаруживает use-after-free, buffer overflow и др.
#include <stdlib.h>

int main() {
    int *p = malloc(10 * sizeof(int));
    free(p);
    p[5] = 42;  // Use-after-free → ASan обнаруживает!
    return 0;
}
```

**Компиляция с ASan:**
```bash
gcc -fsanitize=address -g program.c
./a.out
# Output: AddressSanitizer: heap-use-after-free
```

**Overhead:** ~2x slowdown, ~3x memory

### 6.5 Format String Protection

**Проблема: Format string vulnerabilities**

```c
// Уязвимый код
char user_input[100];
fgets(user_input, 100, stdin);
printf(user_input);  // Опасно! Если user_input содержит %x, %s и т.д.

// Эксплойт
// Ввод: "%x %x %x" → утечка данных со стека
// Ввод: "%n" → запись в память
```

**Защита:**
```c
// Правильно: всегда использовать format string
printf("%s", user_input);  // Безопасно
```

**Compiler warning:**
```bash
gcc -Wformat-security program.c
# Предупреждение при использовании user input в format string
```

---

## 7. Secure Boot и Chain of Trust

### 7.1 Chain of Trust

**Идея:** Каждый компонент проверяет следующий перед загрузкой

```
Hardware (ROM) → Bootloader → Kernel → OS
     ↓              ↓           ↓       ↓
  Verified      Verified   Verified  Verified
```

**Пример: UEFI Secure Boot**

```bash
# Проверка статуса Secure Boot

mokutil --sb-state

# Просмотр загруженных ключей

mokutil --list-enrolled
```

### 7.2 Measured Boot

**TPM измеряет каждый компонент при загрузке:**

```
1. Bootloader → Hash → TPM PCR[0]
2. Kernel → Hash → TPM PCR[1]
3. Initrd → Hash → TPM PCR[2]
...
```

**Attestation:** Удалённая сторона может проверить, что система не скомпрометирована

**Пример: Remote attestation**

```python
# Упрощённый пример

import tpm2_pytss

# Чтение PCR values из TPM

pcr_values = tpm2_pytss.read_pcr()

# Отправка на сервер для проверки

server.verify_boot_integrity(pcr_values)
# Сервер сравнивает с известными good values
```

---

## 8. Side-Channel Attacks

### 8.1 Timing Attacks

**Идея:** Измерение времени выполнения для извлечения секретов

**Пример: Уязвимое сравнение паролей**

```c
// Уязвимый код
int compare_passwords(char *input, char *correct) {
    for (int i = 0; i < strlen(correct); i++) {
        if (input[i] != correct[i]) {
            return 0;  // Возврат при первом несовпадении
        }
    }
    return 1;
}

// Timing attack
uint64_t start = rdtsc();
compare_passwords("A...", "B...");
uint64_t end = rdtsc();
// Время выполнения зависит от количества совпадающих символов
```

**Защита: Constant-time comparison**

```c
// Безопасное сравнение
int secure_compare(char *a, char *b, size_t len) {
    int result = 0;
    for (size_t i = 0; i < len; i++) {
        result |= a[i] ^ b[i];  // Всегда проверяет все байты
    }
    return result == 0;
}
```

### 8.2 Cache Attacks

**Идея:** Использование shared cache для извлечения данных

**Пример: Flush+Reload**

```c
// Атакующий процесс
void attack() {
    // 1. Flush shared memory из cache
    _mm_clflush(shared_memory);
    
    // 2. Ждать выполнения victim
    sleep(1);
    
    // 3. Проверить, что загружено в cache
    uint64_t start = rdtsc();
    access(shared_memory);
    uint64_t end = rdtsc();
    
    if (end - start < threshold) {
        // Данные в cache → victim их использовал
    }
}
```

**Mitigation:**

- Cache partitioning
- Constant-time algorithms
- Cache randomization

---

## 💡 Key Takeaways

- **Protection rings** изолируют kernel от user space, предотвращая доступ пользовательских процессов к привилегированным операциям

- **Memory protection** (NX bit предотвращает выполнение кода на стеке, ASLR рандомизирует адреса) усложняет эксплуатацию уязвимостей, но не делает её невозможной

- **Spectre/Meltdown** показали, что speculative execution имеет серьёзные security implications — даже оптимизации производительности могут быть уязвимыми

- **Secure enclaves** (SGX, TrustZone) защищают данные даже от OS, но имеют ограничения (размер, overhead, side-channel attacks)

- **Defense in depth** — комбинация mitigation techniques (NX + ASLR + Canaries + CFI) значительно усложняет эксплуатацию

- **Trade-off:** Security vs Performance — многие mitigation techniques снижают производительность (5-30%), но необходимы для защиты

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



