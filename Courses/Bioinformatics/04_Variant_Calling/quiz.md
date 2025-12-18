# Variant Calling - Quiz

Проверьте свои знания по пайплайнам variant calling: QC, alignment, variant calling, фильтрация и аннотация.

---

## Question 1: Порядок шагов

Правильный порядок основных шагов variant calling:

A) Variant Calling → Alignment → QC → Filtering

B) QC → Variant Calling → Alignment → Filtering

C) Alignment → QC → Variant Calling → Filtering

D) QC → Alignment → Variant Calling → Filtering

---

## Question 2: BWA

Для чего используется BWA?

A) Quality control

B) Variant calling

C) Аннотация вариантов

D) Alignment ридов на референс

---

## Question 3: Mark Duplicates

Что такое дубликаты в контексте секвенирования?

A) Ошибки секвенирования

B) Повторяющиеся регионы генома

C) Риды с одинаковым началом и концом (PCR artifacts)

D) Парные риды

---

## Question 4: BQSR

Зачем нужна Base Quality Score Recalibration?

A) Удалить дубликаты

B) Аннотировать варианты

C) Улучшить выравнивание

D) Скорректировать quality scores на основе известных вариантов

---

## Question 5: HaplotypeCaller

GATK HaplotypeCaller используется для:

A) Выравнивания ридов

B) Фильтрации вариантов

C) Вызова вариантов

D) Аннотации вариантов

---

## Question 6: Coverage

Рекомендуемое минимальное покрытие для клинического анализа:

A) 30x

B) 10x

C) 100x

D) 5x

---

## Question 7: QD метрика

QD (Quality by Depth) в VCF это:

A) Качество, нормализованное на покрытие

B) Генотип качество

C) Частота аллеля

D) Общее качество варианта

---

## Question 8: SnpEff

SnpEff используется для:

A) Вызова вариантов

B) Фильтрации вариантов

C) Выравнивания ридов

D) Аннотации вариантов (гены, эффекты)

---

## Question 9: PASS фильтр

Что означает PASS в колонке FILTER VCF?

A) Вариант — дубликат

B) Вариант требует дополнительной проверки

C) Вариант прошёл все фильтры качества

D) Вариант не прошёл фильтры

---

## Question 10: Read Group

Зачем нужен Read Group (@RG) в SAM/BAM?

A) Для индексации файла

B) Для группировки ридов из одного сэмпла/библиотеки

C) Для сортировки ридов

D) Для удаления дубликатов

---

## Question 11: FastQC метрики

Какой показатель качества в FastQC должен быть > 30?

A) GC content

B) Per base quality scores

C) Sequence length

D) Adapter content

---

## Question 12: samtools sort

Что делает команда `samtools sort`?

A) Индексирует файл

B) Удаляет дубликаты

C) Сортирует риды по геномным координатам

D) Конвертирует SAM в BAM

---

## Question 13: GVCF

Для чего используется GVCF формат?

A) Сжатие VCF файла

B) Хранение информации о всех позициях для joint calling

C) Аннотация вариантов

D) Хранение только вариантов

---

## Question 14: FS метрика

FS (Fisher Strand Bias) показывает:

A) Частоту аллеля

B) Смещение по цепям (strand bias)

C) Покрытие позиции

D) Качество выравнивания

---

## Question 15: VQSR

VQSR (Variant Quality Score Recalibration) это:

A) Аннотация вариантов

B) Выравнивание ридов

C) Простая фильтрация по порогам

D) Machine learning подход к фильтрации вариантов

---

## Question 16: VEP

Что добавляет VEP (Variant Effect Predictor) к вариантам?

A) Только координаты

B) Только название гена

C) Только качество

D) Consequence predictions, SIFT/PolyPhen scores, population frequencies

---

## Question 17: gnomAD

gnomAD используется для:

A) Индексации файлов

B) Выравнивания ридов

C) Получения популяционных частот вариантов

D) Variant calling

---

## Question 18: GQ

GQ (Genotype Quality) в VCF показывает:

A) Покрытие позиции

B) Качество варианта в целом

C) Уверенность в определённом генотипе

D) Частоту аллеля

---

## Question 19: Duplication rate

Какой максимальный допустимый duplication rate для качественных данных?

A) 80%

B) 20%

C) 5%

D) 50%

---

## Question 20: samtools index

Какое расширение файла создаёт `samtools index` для BAM?

A) .fai

B) .bai

C) .tbi

D) .idx

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | QC → Alignment → Variant Calling → Filtering — правильный порядок. |
| 2 | D | BWA выравнивает риды на референс-геном. |
| 3 | C | Дубликаты — это PCR artifacts с одинаковыми координатами. |
| 4 | D | BQSR корректирует качество на основе known sites. |
| 5 | C | HaplotypeCaller вызывает варианты из BAM файла. |
| 6 | A | 30x — стандартное покрытие для клинического анализа. |
| 7 | A | QD = QUAL / DP (качество нормализованное на глубину). |
| 8 | D | SnpEff аннотирует эффекты вариантов на гены и белки. |
| 9 | C | PASS означает успешное прохождение всех фильтров качества. |
| 10 | B | @RG группирует риды из одного источника (сэмпл/библиотека). |
| 11 | B | Per base quality > 30 означает точность 99.9%. |
| 12 | C | samtools sort сортирует риды по координатам для последующего анализа. |
| 13 | B | GVCF хранит информацию о всех позициях для joint genotyping. |
| 14 | B | Fisher Strand Bias показывает перекос по цепям (возможный артефакт). |
| 15 | D | VQSR использует machine learning для фильтрации вариантов. |
| 16 | D | VEP добавляет consequence, SIFT/PolyPhen, gnomAD, ClinVar. |
| 17 | C | gnomAD — база данных популяционных частот вариантов. |
| 18 | C | GQ показывает уверенность в определённом генотипе (0/1, 1/1 и т.д.). |
| 19 | B | Duplication rate < 20% считается приемлемым. |
| 20 | B | samtools index создаёт .bai индекс для BAM файла. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы освоили variant calling пайплайны. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики с пайплайнами. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попробуйте ещё раз. |

---
