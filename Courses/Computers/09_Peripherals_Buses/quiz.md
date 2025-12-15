# Шины, периферия и драйверы - Quiz

Проверьте свои знания по теме "От ISA до PCIe: как подключаются устройства".

---

## Question 1: ISA

Что характеризовало шину ISA (1981)?

A) До 40 Gbps

B) Point-to-point lanes

C) 8-bit/16-bit, 8 MHz, ~8 MB/s bandwidth

D) 32-bit, 133 MB/s

---

## Question 2: PCI

Какая проблема была у шины PCI?

A) Слишком быстрая

B) Все устройства делят bandwidth (shared bus)

C) Не поддерживает Plug and Play

D) Слишком дорогая

---

## Question 3: AGP

Для чего использовалась шина AGP?

A) Для сетевых карт

B) Специально для видеокарт, dedicated connection

C) Для жестких дисков

D) Для USB устройств

---

## Question 4: PCIe революция

В чём революционность PCI Express?

A) Заменил USB

B) От shared bus к point-to-point lanes

C) Упростил архитектуру ISA

D) Увеличил скорость shared bus

---

## Question 5: PCIe Lanes

Сколько lanes обычно использует GPU в PCIe?

A) x1

B) x4

C) x8

D) x16

---

## Question 6: PCIe Generations

Какая пропускная способность у PCIe 4.0 x16?

A) 64 GB/s

B) 4 GB/s

C) 32 GB/s

D) 16 GB/s

---

## Question 7: USB эволюция

Какая скорость у USB 3.0 (SuperSpeed)?

A) 12 Mbps

B) 480 Mbps

C) 5 Gbps (625 MB/s)

D) 40 Gbps

---

## Question 8: USB-C

Какое преимущество USB-C?

A) Только для передачи данных

B) Reversible (нет "правильной" стороны), универсальный коннектор

C) Медленнее USB 3.0

D) Только для зарядки

---

## Question 9: SATA ограничение

Почему SATA недостаточно для современных SSD?

A) Слишком быстрая

B) Ограничение 6 Gbps (~600 MB/s) недостаточно для современных SSD

C) Не поддерживает NVMe

D) Слишком дорогая

---

## Question 10: NVMe

Что такое NVMe?

A) Тип жесткого диска

B) Протокол для PCIe SSD с низкой latency и высокой параллельностью

C) Версия SATA

D) Тип памяти

---

## Question 11: NVMe Performance

Какая примерная скорость у NVMe PCIe 4.0 x4?

A) ~550 MB/s

B) ~3,500 MB/s

C) ~7,000 MB/s

D) ~14,000 MB/s

---

## Question 12: Эволюция шин

Какая тенденция в эволюции шин?

A) От point-to-point к shared bus

B) От shared buses (ISA, PCI) к point-to-point (PCIe)

C) От быстрых к медленным

D) Нет тенденции

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | ISA характеризовалась 8-bit/16-bit, 8 MHz, ~8 MB/s bandwidth, была простой и дешёвой. |
| 2 | B | Проблема PCI в том, что все устройства делят bandwidth через shared bus. |
| 3 | B | AGP использовалась специально для видеокарт, предоставляя dedicated connection до 2 GB/s. |
| 4 | B | PCIe революционен тем, что перешёл от shared bus к point-to-point lanes, что улучшило масштабируемость. |
| 5 | D | GPU обычно использует x16 lanes в PCIe для максимальной пропускной способности. |
| 6 | C | PCIe 4.0 x16 имеет пропускную способность 32 GB/s. |
| 7 | C | USB 3.0 (SuperSpeed) имеет скорость 5 Gbps (625 MB/s). |
| 8 | B | USB-C reversible (нет "правильной" стороны), универсальный коннектор с Power Delivery и video output. |
| 9 | B | SATA ограничение 6 Gbps (~600 MB/s) недостаточно для современных быстрых SSD. |
| 10 | B | NVMe — это протокол для PCIe SSD с низкой latency и высокой параллельностью (64K queues). |
| 11 | C | NVMe PCIe 4.0 x4 имеет примерную скорость ~7,000 MB/s. |
| 12 | B | Тенденция в эволюции шин — от shared buses (ISA, PCI) к point-to-point (PCIe). |

---

## Scoring Guide

- **11-12 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал.

- **9-10 правильных ответов (75-89%):** ✅ Хорошо! Повторите темы, в которых ошиблись.

- **6-8 правильных ответов (50-74%):** ⚠️ Удовлетворительно. Перечитайте соответствующие разделы.

- **Менее 6 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию.

---

