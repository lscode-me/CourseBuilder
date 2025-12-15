# Архитектурная безопасность - Quiz

Проверьте свои знания по теме "Защита на уровне hardware и архитектуры".

---

## Question 1: Protection Rings

Сколько уровней привилегий (rings) в архитектуре x86?

A) 4 уровня (Ring 0-3)

B) 2 уровня

C) 8 уровней

D) 3 уровня

---

## Question 2: Ring 0

Что можно делать в Ring 0 (Kernel Mode)?

A) Только выполнение программ

B) Только работа с файлами

C) Только чтение памяти

D) Всё: I/O, управление памятью, прерывания

---

## Question 3: ARM Exception Levels

Сколько Exception Levels в архитектуре ARM?

A) 2 уровня (EL0-EL1)

B) 4 уровня (EL0-EL3)

C) 3 уровня (EL0-EL2)

D) 6 уровней

---

## Question 4: MMU Page Protection

Какие флаги защиты может иметь страница памяти?

A) Только Write

B) Только Execute

C) Read, Write, Execute (R, W, X)

D) Только Read

---

## Question 5: NX Bit

Для чего используется NX bit (No-eXecute)?

A) Для ускорения работы

B) Защита от выполнения кода на стеке (защита от buffer overflow)

C) Для защиты от чтения

D) Для экономии памяти

---

## Question 6: ASLR

Что такое ASLR (Address Space Layout Randomization)?

A) Рандомизация паролей

B) Шифрование памяти

C) Рандомизация адресов при каждом запуске процесса

D) Сжатие данных

---

## Question 7: Spectre

В чём проблема Spectre vulnerability?

A) Проблема в операционной системе

B) Проблема в компиляторе

C) Speculative execution + branch prediction оставляют следы в кэше

D) Проблема в сети

---

## Question 8: Meltdown

В чём проблема Meltdown vulnerability?

A) Проблема в драйверах

B) Kernel memory читается из user space через спекуляцию

C) Проблема в файловой системе

D) Проблема в сети

---

## Question 9: Rowhammer

Что такое Rowhammer атака?

A) Атака через программное обеспечение

B) Физический дефект DRAM, быстрое чтение строк вызывает flip битов

C) Атака через сеть

D) Атака через файловую систему

---

## Question 10: Intel SGX

Что такое Intel SGX (Software Guard Extensions)?

A) Протокол сети

B) Тип процессора

C) Изолированная область памяти (enclave), защищена даже от OS

D) Тип памяти

---

## Question 11: ARM TrustZone

Что такое ARM TrustZone?

A) Тип процессора

B) Тип памяти

C) Secure World vs Normal World разделение

D) Файловая система

---

## Question 12: TPM

Что такое TPM (Trusted Platform Module)?

A) Отдельный чип, хранит криптографические ключи, измеряет boot process

B) Тип памяти

C) Тип процессора

D) Протокол сети

---

## Question 13: DEP

Что такое DEP (Data Execution Prevention)?

A) Сжатие данных

B) NX bit + OS support, защита от выполнения кода на стеке и heap

C) Защита данных от чтения

D) Шифрование данных

---

## Question 14: Stack Canaries

Для чего используются Stack Canaries?

A) Для экономии памяти

B) Защита от stack overflow через обнаружение изменения canary

C) Для ускорения работы

D) Для защиты от чтения

---

## Question 15: CFI

Что такое Control Flow Integrity (CFI)?

A) Проверка, что программа прыгает только в легальные места

B) Сжатие кода

C) Шифрование кода

D) Защита данных

---

## Question 16: Spectre Mitigation

Какое mitigation используется для Spectre?

A) Microcode updates, software barriers (retpoline), performance penalty

B) Только обновление ОС

C) Только перезагрузка

D) Только обновление драйверов

---

## Question 17: Meltdown Mitigation

Какое mitigation используется для Meltdown?

A) Только обновление драйверов

B) Только перезагрузка

C) Только обновление ОС

D) KPTI (Kernel Page Table Isolation) — отдельные page tables для kernel и user

---

## Question 18: Rowhammer Mitigation

Какое mitigation используется для Rowhammer?

A) Только обновление ОС

B) ECC memory, Targeted Row Refresh (TRR)

C) Только обновление драйверов

D) Только перезагрузка

---

## Question 19: Security Trade-off

Какое trade-off характерно для security features?

A) Security всегда бесплатна

B) Security не влияет на производительность

C) Security vs Performance — многие mitigation techniques снижают производительность

D) Security всегда улучшает производительность

---

## Question 20: Secure Enclaves применение

Где применяются Secure Enclaves (SGX, TrustZone)?

A) Только для игр

B) DRM, cryptocurrency wallets, secure computation

C) Только для файловых систем

D) Только для веб-браузеров

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Архитектура x86 имеет 4 уровня привилегий (Ring 0-3). |
| 2 | D | Ring 0 (Kernel Mode) позволяет делать всё: I/O, управление памятью, прерывания. |
| 3 | B | ARM имеет 4 Exception Levels (EL0-EL3): EL0 (User), EL1 (OS), EL2 (Hypervisor), EL3 (Secure Monitor). |
| 4 | C | Страница памяти может иметь флаги Read, Write, Execute (R, W, X). |
| 5 | B | NX bit используется для защиты от выполнения кода на стеке, что защищает от buffer overflow эксплойтов. |
| 6 | C | ASLR рандомизирует адреса при каждом запуске процесса, усложняя эксплуатацию уязвимостей. |
| 7 | C | Spectre использует speculative execution + branch prediction, которые оставляют следы в кэше, позволяя извлечь данные через timing attack. |
| 8 | B | Meltdown позволяет читать kernel memory из user space через спекулятивное выполнение до проверки прав. |
| 9 | B | Rowhammer — это физический дефект DRAM, где быстрое чтение строк A и C вызывает flip битов в строке B между ними. |
| 10 | C | Intel SGX создаёт изолированную область памяти (enclave), защищённую даже от операционной системы. |
| 11 | C | ARM TrustZone разделяет Secure World и Normal World для изоляции критичных данных. |
| 12 | A | TPM — это отдельный чип на материнской плате, который хранит криптографические ключи и измеряет boot process. |
| 13 | B | DEP (Data Execution Prevention) = NX bit + OS support, защищает от выполнения кода на стеке и heap. |
| 14 | B | Stack Canaries защищают от stack overflow через обнаружение изменения случайного значения (canary) перед возвратом из функции. |
| 15 | A | Control Flow Integrity проверяет, что программа прыгает только в легальные места, защищая от ROP атак. |
| 16 | A | Mitigation для Spectre включает microcode updates, software barriers (retpoline), с performance penalty ~5-30%. |
| 17 | D | Mitigation для Meltdown — KPTI (Kernel Page Table Isolation), отдельные page tables для kernel и user, с performance penalty ~5%. |
| 18 | B | Mitigation для Rowhammer включает ECC memory и Targeted Row Refresh (TRR). |
| 19 | C | Security vs Performance — многие mitigation techniques снижают производительность, это важный trade-off. |
| 20 | B | Secure Enclaves применяются для DRM, cryptocurrency wallets, secure computation. |

---

## Scoring Guide

- **18-20 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал. Переходите к следующему модулю.

- **14-17 правильных ответов (70-89%):** ✅ Хорошо! Хороший результат! Повторите темы, в которых ошиблись.

- **10-13 правильных ответов (50-69%):** ⚠️ Удовлетворительно. Рекомендуется перечитать соответствующие разделы лекции.

- **Менее 10 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию и попробуйте ещё раз.

---

