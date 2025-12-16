# Variant Calling - Quiz

Проверьте свои знания по пайплайнам variant calling: QC, alignment, variant calling, фильтрация и аннотация.

---

## Question 1: Порядок шагов

Правильный порядок основных шагов variant calling:

A) Variant Calling → Alignment → QC → Filtering

B) Alignment → QC → Variant Calling → Filtering

C) QC → Variant Calling → Alignment → Filtering

D) QC → Alignment → Variant Calling → Filtering

---

## Question 2: BWA

Для чего используется BWA?

A) Alignment ридов на референс

B) Quality control

C) Аннотация вариантов

D) Variant calling

---

## Question 3: Mark Duplicates

Что такое дубликаты в контексте секвенирования?

A) Парные риды

B) Ошибки секвенирования

C) Повторяющиеся регионы генома

D) Риды с одинаковым началом и концом (PCR artifacts)

---

## Question 4: BQSR

Зачем нужна Base Quality Score Recalibration?

A) Удалить дубликаты

B) Аннотировать варианты

C) Скорректировать quality scores на основе известных вариантов

D) Улучшить выравнивание

---

## Question 5: HaplotypeCaller

GATK HaplotypeCaller используется для:

A) Фильтрации вариантов

B) Аннотации вариантов

C) Вызова вариантов

D) Выравнивания ридов

---

## Question 6: Coverage

Рекомендуемое минимальное покрытие для клинического анализа:

A) 100x

B) 30x

C) 5x

D) 10x

---

## Question 7: QD метрика

QD (Quality by Depth) в VCF это:

A) Качество, нормализованное на покрытие

B) Частота аллеля

C) Генотип качество

D) Общее качество варианта

---

## Question 8: SnpEff

SnpEff используется для:

A) Фильтрации вариантов

B) Вызова вариантов

C) Выравнивания ридов

D) Аннотации вариантов (гены, эффекты)

---

## Question 9: PASS фильтр

Что означает PASS в колонке FILTER VCF?

A) Вариант — дубликат

B) Вариант не прошёл фильтры

C) Вариант требует дополнительной проверки

D) Вариант прошёл все фильтры качества

---

## Question 10: Read Group

Зачем нужен Read Group (@RG) в SAM/BAM?

A) Для сортировки ридов

B) Для группировки ридов из одного сэмпла/библиотеки

C) Для удаления дубликатов

D) Для индексации файла

---

## Question 11: FastQC метрики

Какой показатель качества в FastQC должен быть > 30?

A) Sequence length

B) Adapter content

C) Per base quality scores

D) GC content

---

## Question 12: samtools sort

Что делает команда `samtools sort`?

A) Удаляет дубликаты

B) Сортирует риды по геномным координатам

C) Индексирует файл

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

A) Качество выравнивания

B) Покрытие позиции

C) Частоту аллеля

D) Смещение по цепям (strand bias)

---

## Question 15: VQSR

VQSR (Variant Quality Score Recalibration) это:

A) Аннотация вариантов

B) Machine learning подход к фильтрации вариантов

C) Простая фильтрация по порогам

D) Выравнивание ридов

---

## Question 16: VEP

Что добавляет VEP (Variant Effect Predictor) к вариантам?

A) Consequence predictions, SIFT/PolyPhen scores, population frequencies

B) Только название гена

C) Только качество

D) Только координаты

---

## Question 17: gnomAD

gnomAD используется для:

A) Выравнивания ридов

B) Variant calling

C) Индексации файлов

D) Получения популяционных частот вариантов

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

A) 20%

B) 50%

C) 80%

D) 5%

---

## Question 20: samtools index

Какое расширение файла создаёт `samtools index` для BAM?

A) .idx

B) .fai

C) .bai

D) .tbi

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | QC → Alignment → Variant Calling → Filtering — правильный порядок. |
| 2 | A | BWA выравнивает риды на референс-геном. |
| 3 | D | Дубликаты — это PCR artifacts с одинаковыми координатами. |
| 4 | C | BQSR корректирует качество на основе known sites. |
| 5 | C | HaplotypeCaller вызывает варианты из BAM файла. |
| 6 | B | 30x — стандартное покрытие для клинического анализа. |
| 7 | A | QD = QUAL / DP (качество нормализованное на глубину). |
| 8 | D | SnpEff аннотирует эффекты вариантов на гены и белки. |
| 9 | D | PASS означает успешное прохождение всех фильтров качества. |
| 10 | B | @RG группирует риды из одного источника (сэмпл/библиотека). |
| 11 | C | Per base quality > 30 означает точность 99.9%. |
| 12 | B | samtools sort сортирует риды по координатам для последующего анализа. |
| 13 | B | GVCF хранит информацию о всех позициях для joint genotyping. |
| 14 | D | Fisher Strand Bias показывает перекос по цепям (возможный артефакт). |
| 15 | B | VQSR использует machine learning для фильтрации вариантов. |
| 16 | A | VEP добавляет consequence, SIFT/PolyPhen, gnomAD, ClinVar. |
| 17 | D | gnomAD — база данных популяционных частот вариантов. |
| 18 | C | GQ показывает уверенность в определённом генотипе (0/1, 1/1 и т.д.). |
| 19 | A | Duplication rate < 20% считается приемлемым. |
| 20 | C | samtools index создаёт .bai индекс для BAM файла. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы освоили variant calling пайплайны. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики с пайплайнами. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попробуйте ещё раз. |

---
