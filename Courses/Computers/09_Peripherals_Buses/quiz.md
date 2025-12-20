# Шины, периферия и драйверы - Quiz

Проверьте свои знания по теме "От ISA до PCIe: как подключаются устройства".

---

## Question 1: ISA

Что характеризовало шину ISA (1981)?

A) Point-to-point lanes

B) 32-bit, 133 MB/s

C) 8-bit/16-bit, 8 MHz, ~8 MB/s bandwidth

D) До 40 Gbps

---

## Question 2: PCI

Какая проблема была у шины PCI?

A) Слишком быстрая

B) Не поддерживает Plug and Play

C) Все устройства делят bandwidth (shared bus)

D) Слишком дорогая

---

## Question 3: AGP

Для чего использовалась шина AGP?

A) Специально для видеокарт, dedicated connection

B) Для жестких дисков

C) Для USB устройств

D) Для сетевых карт

---

## Question 4: PCIe революция

В чём революционность PCI Express?

A) Упростил архитектуру ISA

B) Увеличил скорость shared bus

C) От shared bus к point-to-point lanes

D) Заменил USB

---

## Question 5: PCIe Lanes

Сколько lanes обычно использует GPU в PCIe?

A) x1

B) x16

C) x4

D) x8

---

## Question 6: PCIe Generations

Какая пропускная способность у PCIe 4.0 x16?

A) 32 GB/s

B) 16 GB/s

C) 4 GB/s

D) 64 GB/s

---

## Question 7: USB эволюция

Какая скорость у USB 3.0 (SuperSpeed)?

A) 480 Mbps

B) 5 Gbps (625 MB/s)

C) 12 Mbps

D) 40 Gbps

---

## Question 8: USB-C

Какое преимущество USB-C?

A) Reversible (нет "правильной" стороны), универсальный коннектор

B) Только для зарядки

C) Медленнее USB 3.0

D) Только для передачи данных

---

## Question 9: SATA ограничение

Почему SATA недостаточно для современных SSD?

A) Слишком дорогая

B) Слишком быстрая

C) Не поддерживает NVMe

D) Ограничение 6 Gbps (~600 MB/s) недостаточно для современных SSD

---

## Question 10: NVMe

Что такое NVMe?

A) Тип жесткого диска

B) Протокол для PCIe SSD с низкой latency и высокой параллельностью

C) Тип памяти

D) Версия SATA

---

## Question 11: NVMe Performance

Какая примерная скорость у NVMe PCIe 4.0 x4?

A) ~3,500 MB/s

B) ~14,000 MB/s

C) ~550 MB/s

D) ~7,000 MB/s

---

## Question 12: Эволюция шин

Какая тенденция в эволюции шин?

A) От быстрых к медленным

B) От point-to-point к shared bus

C) От shared buses (ISA, PCI) к point-to-point (PCIe)

D) Нет тенденции

---

## Question 13: PCIe Point-to-Point

Почему point-to-point лучше shared bus?

A) Проще реализовать

B) Дешевле

C) Медленнее

D) Каждое устройство имеет dedicated lane, нет конкуренции за bandwidth

---

## Question 14: PCIe Lanes для NVMe

Сколько lanes обычно использует NVMe SSD?

A) x4

B) x8

C) x16

D) x1

---

## Question 15: USB4 Скорость

Какая скорость у USB4?

A) 20 Gbps

B) До 40 Gbps (5 GB/s)

C) 10 Gbps

D) 5 Gbps

---

## Question 16: USB Power Delivery

Какая максимальная мощность у USB Power Delivery?

A) До 240W

B) 500W

C) 100W

D) 5W

---

## Question 17: Thunderbolt

Что такое Thunderbolt 3/4?

A) Медленнее USB 3.0

B) Только для видео

C) Только для зарядки

D) До 40 Gbps, использует USB-C, поддержка PCIe/DisplayPort/USB

---

## Question 18: NVMe Queues

Сколько queues поддерживает NVMe?

A) 1,000

B) До 64K queues, 64K commands per queue

C) 64

D) 1

---

## Question 19: I2C Применение

Для чего используется шина I2C?

A) Для сетевых устройств

B) Для высокоскоростных дисков

C) Для GPU

D) Для низкоскоростной периферии (датчики, EEPROM, RTC)

---

## Question 20: SPI Характеристики

Что характеризует SPI?

A) Только для аудио

B) Только для видео

C) Высокоскоростная последовательная шина, full-duplex, Master-Slave

D) Только half-duplex

---

## Question 21: PCIe 6.0

Какая пропускная способность у PCIe 6.0 x16?

A) 16 GB/s

B) 128 GB/s

C) 64 GB/s

D) 32 GB/s

---

## Question 22: USB Hub Ограничения

Какое ограничение у USB topology?

A) Нет ограничений

B) Максимум 5 уровней вложенности hubs

C) Максимум 10 уровней

D) Максимум 2 уровня

---

## Question 23: NVMe vs SATA SSD

Во сколько раз NVMe PCIe 3.0 x4 быстрее SATA SSD?

A) В 2 раза

B) Примерно в 6 раз (~3,500 MB/s vs ~550 MB/s)

C) В 4 раза

D) NVMe медленнее

---

## Question 24: DisplayPort vs HDMI

В чём отличие DisplayPort от HDMI?

A) DisplayPort только для аудио

B) Нет отличий

C) HDMI быстрее

D) DisplayPort превосходит HDMI для компьютеров, поддерживает daisy-chaining

---

## Question 25: PCIe Backward Compatibility

Совместимы ли PCIe поколения?

A) Только forward совместимость

B) Только для x16

C) Нет, каждое поколение несовместимо

D) Да, обратная совместимость (PCIe 4.0 device работает в PCIe 3.0 slot, но медленнее)

---

## Question 26: USB Enumeration

Что такое USB enumeration?

A) Только подключение устройства

B) Процесс обнаружения и настройки USB устройства (reset, descriptors, address, configuration)

C) Только удаление устройства

D) Только передача данных

---

## Question 27: PCIe Configuration Space

Для чего нужен PCIe configuration space?

A) Только для скорости

B) Для идентификации устройства, настройки ресурсов (IRQ, memory), управления устройством

C) Только для хранения данных

D) Только для питания

---

## Question 28: NVMe Latency

Почему NVMe имеет низкую latency?

A) Только из-за размера

B) Использует PCIe напрямую, bypass SATA overhead, меньше слоёв протокола

C) Только из-за цены

D) Только из-за скорости

---

## Question 29: USB-C Alt Modes

Что такое USB-C Alt Modes?

A) Только для зарядки

B) Только для данных

C) Только для аудио

D) Альтернативные режимы: DisplayPort, HDMI, Thunderbolt через USB-C коннектор

---

## Question 30: PCIe Lane Scaling

Как работает scaling в PCIe через lanes?

A) Только фиксированное количество

B) Только x1

C) Только x16

D) Устройства могут использовать x1, x4, x8, x16 lanes в зависимости от потребностей

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | ISA характеризовалась 8-bit/16-bit, 8 MHz, ~8 MB/s bandwidth, была простой и дешёвой. |
| 2 | C | Проблема PCI в том, что все устройства делят bandwidth через shared bus. |
| 3 | A | AGP использовалась специально для видеокарт, предоставляя dedicated connection до 2 GB/s. |
| 4 | C | PCIe революционен тем, что перешёл от shared bus к point-to-point lanes, что улучшило масштабируемость. |
| 5 | B | GPU обычно использует x16 lanes в PCIe для максимальной пропускной способности. |
| 6 | A | PCIe 4.0 x16 имеет пропускную способность 32 GB/s. |
| 7 | B | USB 3.0 (SuperSpeed) имеет скорость 5 Gbps (625 MB/s). |
| 8 | A | USB-C reversible (нет "правильной" стороны), универсальный коннектор с Power Delivery и video output. |
| 9 | D | SATA ограничение 6 Gbps (~600 MB/s) недостаточно для современных быстрых SSD. |
| 10 | B | NVMe — это протокол для PCIe SSD с низкой latency и высокой параллельностью (64K queues). |
| 11 | D | NVMe PCIe 4.0 x4 имеет примерную скорость ~7,000 MB/s. |
| 12 | C | Тенденция в эволюции шин — от shared buses (ISA, PCI) к point-to-point (PCIe). |
| 13 | D | Point-to-point лучше shared bus, так как каждое устройство имеет dedicated lane, нет конкуренции за bandwidth, лучше масштабируемость. |
| 14 | A | NVMe SSD обычно использует x4 lanes (достаточно для высокой производительности, экономит PCIe lanes для других устройств). |
| 15 | B | USB4 имеет скорость до 40 Gbps (5 GB/s), основан на Thunderbolt 3. |
| 16 | A | USB Power Delivery может доставлять до 240W мощности через USB-C коннектор. |
| 17 | D | Thunderbolt 3/4 обеспечивает до 40 Gbps, использует USB-C коннектор, поддерживает PCIe, DisplayPort, USB в одном интерфейсе. |
| 18 | B | NVMe поддерживает до 64K queues с 64K commands per queue, обеспечивая высокий parallelism. |
| 19 | D | I2C используется для низкоскоростной периферии: датчики, EEPROM, RTC (Real-Time Clock), скорость 100 Kbps - 3.4 Mbps. |
| 20 | C | SPI характеризуется как высокоскоростная последовательная шина (до 50+ Mbps), full-duplex (одновременная передача в обе стороны), Master-Slave архитектура. |
| 21 | B | PCIe 6.0 x16 имеет пропускную способность 128 GB/s (8 GB/s per lane × 16 lanes). |
| 22 | B | USB topology ограничена максимум 5 уровнями вложенности hubs для предотвращения проблем с timing и сигналами. |
| 23 | B | NVMe PCIe 3.0 x4 примерно в 6 раз быстрее SATA SSD (~3,500 MB/s vs ~550 MB/s), так как bypass SATA overhead. |
| 24 | D | DisplayPort превосходит HDMI для компьютеров, поддерживает daisy-chaining (последовательное подключение мониторов), до 80 Gbps в DP 2.0. |
| 25 | D | PCIe имеет обратную совместимость: PCIe 4.0 device работает в PCIe 3.0 slot, но на скорости PCIe 3.0 (медленнее). |
| 26 | B | USB enumeration — процесс обнаружения и настройки USB устройства: reset, получение descriptors, установка address, configuration. |
| 27 | B | PCIe configuration space используется для идентификации устройства (vendor/device ID), настройки ресурсов (IRQ, memory addresses), управления устройством. |
| 28 | B | NVMe имеет низкую latency, так как использует PCIe напрямую (bypass SATA overhead), меньше слоёв протокола, прямая связь с CPU. |
| 29 | D | USB-C Alt Modes позволяют использовать USB-C коннектор для альтернативных протоколов: DisplayPort, HDMI, Thunderbolt через тот же физический коннектор. |
| 30 | D | PCIe lane scaling позволяет устройствам использовать x1, x4, x8, x16 lanes в зависимости от потребностей в bandwidth (GPU: x16, SSD: x4, WiFi: x1). |

---

## Scoring Guide

- **27-30 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал. Переходите к следующему модулю.

- **21-26 правильных ответов (70-89%):** ✅ Хорошо! Хороший результат! Повторите темы, в которых ошиблись.

- **15-20 правильных ответов (50-69%):** ⚠️ Удовлетворительно. Рекомендуется перечитать соответствующие разделы лекции.

- **Менее 15 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию и попробуйте ещё раз.

---

