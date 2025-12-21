# Архитектурная безопасность - Quiz

Проверьте свои знания по теме "Защита на уровне hardware и архитектуры".

---

## Question 1: Protection Rings

Сколько уровней привилегий (rings) в архитектуре x86?

A) 8 уровней

B) 4 уровня (Ring 0-3)

C) 3 уровня

D) 2 уровня

---

## Question 2: Ring 0

Что можно делать в Ring 0 (Kernel Mode)?

A) Выполнение пользовательских программ с ограниченными правами

B) Всё: I/O, управление памятью, прерывания

C) Чтение памяти без возможности записи

D) Работа с файлами через файловую систему

---

## Question 3: ARM Exception Levels

Сколько Exception Levels в архитектуре ARM?

A) 3 уровня (EL0-EL2)

B) 4 уровня (EL0-EL3)

C) 2 уровня (EL0-EL1)

D) 6 уровней

---

## Question 4: MMU Page Protection

Какие флаги защиты может иметь страница памяти?

A) Write и Execute без возможности чтения

B) Read и Execute без возможности записи

C) Read и Write без возможности выполнения

D) Read, Write, Execute (R, W, X)

---

## Question 5: NX Bit

Для чего используется NX bit (No-eXecute)?

A) Для экономии памяти

B) Для ускорения работы

C) Для защиты от чтения

D) Защита от выполнения кода на стеке (защита от buffer overflow)

---

## Question 6: ASLR

Что такое ASLR (Address Space Layout Randomization)?

A) Шифрование памяти

B) Сжатие данных

C) Рандомизация паролей

D) Рандомизация адресов при каждом запуске процесса

---

## Question 7: Spectre

В чём проблема Spectre vulnerability?

A) Проблема в операционной системе

B) Проблема в сети

C) Speculative execution + branch prediction оставляют следы в кэше

D) Проблема в компиляторе

---

## Question 8: Meltdown

В чём проблема Meltdown vulnerability?

A) Проблема в файловой системе

B) Kernel memory читается из user space через спекуляцию

C) Проблема в драйверах

D) Проблема в сети

---

## Question 9: Rowhammer

Что такое Rowhammer атака?

A) Атака через файловую систему

B) Физический дефект DRAM, быстрое чтение строк вызывает flip битов

C) Атака через сеть

D) Атака через программное обеспечение

---

## Question 10: Intel SGX

Что такое Intel SGX (Software Guard Extensions)?

A) Сетевой протокол для защищённой передачи данных

B) Специализированный тип памяти с аппаратным шифрованием

C) Расширение архитектуры процессора для виртуализации

D) Изолированная область памяти (enclave), защищена даже от OS

---

## Question 11: ARM TrustZone

Что такое ARM TrustZone?

A) Специализированная архитектура процессора для мобильных устройств

B) Secure World vs Normal World разделение

C) Защищённая область памяти с аппаратным шифрованием

D) Файловая система с встроенной защитой данных

---

## Question 12: TPM

Что такое TPM (Trusted Platform Module)?

A) Отдельный чип, хранит криптографические ключи, измеряет boot process

B) Расширение процессора для аппаратной виртуализации

C) Сетевой протокол для аутентификации устройств

D) Специализированная память для хранения ключей шифрования

---

## Question 13: DEP

Что такое DEP (Data Execution Prevention)?

A) Сжатие данных

B) Защита данных от чтения

C) Шифрование данных

D) NX bit + OS support, защита от выполнения кода на стеке и heap

---

## Question 14: Stack Canaries

Для чего используются Stack Canaries?

A) Для ускорения работы

B) Для экономии памяти

C) Защита от stack overflow через обнаружение изменения canary

D) Для защиты от чтения

---

## Question 15: CFI

Что такое Control Flow Integrity (CFI)?

A) Сжатие кода

B) Проверка, что программа прыгает только в легальные места

C) Шифрование кода

D) Защита данных

---

## Question 16: Spectre Mitigation

Какое mitigation используется для Spectre?

A) Microcode updates, software barriers (retpoline), performance penalty

B) Обновление драйверов устройств для устранения уязвимости

C) Перезагрузка системы для сброса состояния процессора

D) Обновление операционной системы без изменения микрокода

---

## Question 17: Meltdown Mitigation

Какое mitigation используется для Meltdown?

A) KPTI (Kernel Page Table Isolation) — отдельные page tables для kernel и user

B) Обновление драйверов для изоляции памяти ядра

C) Обновление ОС с улучшенной защитой памяти

D) Перезагрузка системы для применения новых настроек безопасности

---

## Question 18: Rowhammer Mitigation

Какое mitigation используется для Rowhammer?

A) Перезагрузка системы для сброса состояния памяти

B) ECC memory, Targeted Row Refresh (TRR)

C) Обновление ОС с улучшенным управлением памятью

D) Обновление драйверов для контроля доступа к памяти

---

## Question 19: Security Trade-off

Какое trade-off характерно для security features?

A) Security всегда улучшает производительность

B) Security не влияет на производительность

C) Security vs Performance — многие mitigation techniques снижают производительность

D) Security всегда бесплатна

---

## Question 20: Secure Enclaves применение

Где применяются Secure Enclaves (SGX, TrustZone)?

A) Защита данных в веб-браузерах и веб-приложениях

B) Защита игровых данных и предотвращение читерства

C) DRM, cryptocurrency wallets, secure computation

D) Защита файловых систем от несанкционированного доступа

---

## Question 21: Buffer Overflow без NX

Что происходит при buffer overflow без NX bit?

A) Код может быть записан на стек и выполнен

B) Запись данных за пределы буфера без возможности выполнения

C) Система автоматически предотвращает переполнение буфера

D) Чтение данных за пределами выделенной памяти

---

## Question 22: ASLR Эффект

Какой эффект имеет ASLR на эксплуатацию уязвимостей?

A) Полностью предотвращает эксплуатацию

B) Упрощает эксплуатацию

C) Не влияет на эксплуатацию

D) Усложняет эксплуатацию, так как атакующий не знает адреса

---

## Question 23: Spectre Performance Penalty

Какой performance penalty у mitigation для Spectre?

A) ~5-30% в зависимости от workload

B) Нет penalty

C) ~50%

D) ~100%

---

## Question 24: KPTI Overhead

Почему KPTI имеет performance overhead?

A) Из-за сжатия данных

B) Из-за шифрования

C) Нет overhead

D) Из-за переключения page tables при syscall

---

## Question 25: Stack Canaries Типы

Какие типы stack canaries существуют?

A) Terminator canaries, Random canaries, XOR canaries

B) Только terminator canaries

C) Только random canaries

D) Только один тип

---

## Question 26: CFI Hardware Support

Какая CPU feature поддерживает CFI?

A) Только software support

B) Только для ARM

C) Нет hardware support

D) Intel CET (Control-flow Enforcement Technology)

---

## Question 27: Address Sanitizer

Что обнаруживает Address Sanitizer (ASan)?

A) Только memory leaks

B) Только use-after-free

C) Use-after-free, buffer overflow, memory leaks и другие memory errors

D) Только buffer overflow

---

## Question 28: Format String Vulnerability

В чём проблема format string vulnerability?

A) Нет проблемы

B) Использование user input в format string может привести к утечке данных или записи в память

C) Проблема с чтением файлов

D) Только проблема с сетью

---

## Question 29: Timing Attack

Что такое timing attack?

A) Измерение времени выполнения для извлечения секретов

B) Атака через файловую систему

C) Атака через сеть

D) Атака через память

---

## Question 30: Defense in Depth

Что означает defense in depth в контексте security?

A) Только одна защита

B) Только hardware защита

C) Только software защита

D) Комбинация множества mitigation techniques (NX + ASLR + Canaries + CFI)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Архитектура x86 имеет 4 уровня привилегий (Ring 0-3). |
| 2 | B | Ring 0 (Kernel Mode) позволяет делать всё: I/O, управление памятью, прерывания. |
| 3 | B | ARM имеет 4 Exception Levels (EL0-EL3): EL0 (User), EL1 (OS), EL2 (Hypervisor), EL3 (Secure Monitor). |
| 4 | D | Страница памяти может иметь флаги Read, Write, Execute (R, W, X). |
| 5 | D | NX bit используется для защиты от выполнения кода на стеке, что защищает от buffer overflow эксплойтов. |
| 6 | D | ASLR рандомизирует адреса при каждом запуске процесса, усложняя эксплуатацию уязвимостей. |
| 7 | C | Spectre использует speculative execution + branch prediction, которые оставляют следы в кэше, позволяя извлечь данные через timing attack. |
| 8 | B | Meltdown позволяет читать kernel memory из user space через спекулятивное выполнение до проверки прав. |
| 9 | B | Rowhammer — это физический дефект DRAM, где быстрое чтение строк A и C вызывает flip битов в строке B между ними. |
| 10 | D | Intel SGX создаёт изолированную область памяти (enclave), защищённую даже от операционной системы. |
| 11 | B | ARM TrustZone разделяет Secure World и Normal World для изоляции критичных данных. |
| 12 | A | TPM — это отдельный чип на материнской плате, который хранит криптографические ключи и измеряет boot process. |
| 13 | D | DEP (Data Execution Prevention) = NX bit + OS support, защищает от выполнения кода на стеке и heap. |
| 14 | C | Stack Canaries защищают от stack overflow через обнаружение изменения случайного значения (canary) перед возвратом из функции. |
| 15 | B | Control Flow Integrity проверяет, что программа прыгает только в легальные места, защищая от ROP атак. |
| 16 | A | Mitigation для Spectre включает microcode updates, software barriers (retpoline), с performance penalty ~5-30%. |
| 17 | A | Mitigation для Meltdown — KPTI (Kernel Page Table Isolation), отдельные page tables для kernel и user, с performance penalty ~5%. |
| 18 | B | Mitigation для Rowhammer включает ECC memory и Targeted Row Refresh (TRR). |
| 19 | C | Security vs Performance — многие mitigation techniques снижают производительность, это важный trade-off. |
| 20 | C | Secure Enclaves применяются для DRM, cryptocurrency wallets, secure computation. |
| 21 | A | Без NX bit код может быть записан на стек через buffer overflow и выполнен, что позволяет атакующему выполнить произвольный код. |
| 22 | D | ASLR усложняет эксплуатацию, так как атакующий не знает адреса функций и данных (они меняются при каждом запуске), но не предотвращает полностью. |
| 23 | A | Mitigation для Spectre имеет performance penalty ~5-30% в зависимости от workload из-за барьеров и ограничений спекулятивного выполнения. |
| 24 | D | KPTI имеет performance overhead из-за переключения page tables при каждом syscall, что добавляет latency (~5% overhead). |
| 25 | A | Существуют разные типы stack canaries: Terminator canaries (содержат NULL, CR, LF), Random canaries (случайные значения), XOR canaries (XOR с return address). |
| 26 | D | Intel CET (Control-flow Enforcement Technology) предоставляет hardware support для CFI через Indirect Branch Tracking (IBT) и Shadow Stack. |
| 27 | C | Address Sanitizer (ASan) обнаруживает use-after-free, buffer overflow, memory leaks и другие memory errors во время выполнения с overhead ~2x slowdown. |
| 28 | B | Format string vulnerability возникает при использовании user input в format string (printf, sprintf), что может привести к утечке данных со стека или записи в память через %n. |
| 29 | A | Timing attack — это извлечение секретов через измерение времени выполнения операций (например, сравнение паролей, доступ к кэшу). |
| 30 | D | Defense in depth означает использование комбинации множества mitigation techniques (NX + ASLR + Canaries + CFI), что значительно усложняет эксплуатацию уязвимостей. |

---

## Scoring Guide

- **27-30 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал. Переходите к следующему модулю.

- **21-26 правильных ответов (70-89%):** ✅ Хорошо! Хороший результат! Повторите темы, в которых ошиблись.

- **15-20 правильных ответов (50-69%):** ⚠️ Удовлетворительно. Рекомендуется перечитать соответствующие разделы лекции.

- **Менее 15 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию и попробуйте ещё раз.

---

