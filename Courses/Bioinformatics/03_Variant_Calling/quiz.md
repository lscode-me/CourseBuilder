# Variant Calling - Quiz

Проверьте свои знания по пайплайнам variant calling: QC, alignment, variant calling, фильтрация и аннотация.

---

## Question 1: Порядок шагов






Правильный порядок основных шагов variant calling:

A) QC → Alignment → Variant Calling → Filtering

B) QC → Variant Calling → Alignment → Filtering

C) Variant Calling → Alignment → QC → Filtering

D) Alignment → QC → Variant Calling → Filtering

---

## Question 2: BWA






Для чего используется BWA?

A) Variant calling

B) Alignment ридов на референс

C) Quality control

D) Аннотация вариантов

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

A) Аннотировать варианты

B) Удалить дубликаты

C) Скорректировать quality scores на основе известных вариантов

D) Улучшить выравнивание

---

## Question 5: HaplotypeCaller






GATK HaplotypeCaller используется для:

A) Выравнивания ридов

B) Фильтрации вариантов

C) Аннотации вариантов

D) Вызова вариантов

---

## Question 6: Coverage






Рекомендуемое минимальное покрытие для клинического анализа:

A) 10x

B) 5x

C) 30x

D) 100x

---

## Question 7: QD метрика






QD (Quality by Depth) в VCF это:

A) Генотип качество

B) Качество, нормализованное на покрытие

C) Общее качество варианта

D) Частота аллеля

---

## Question 8: SnpEff






SnpEff используется для:

A) Аннотации вариантов (гены, эффекты)

B) Выравнивания ридов

C) Вызова вариантов

D) Фильтрации вариантов

---

## Question 9: PASS фильтр






Что означает PASS в колонке FILTER VCF?

A) Вариант требует дополнительной проверки

B) Вариант — дубликат

C) Вариант не прошёл фильтры

D) Вариант прошёл все фильтры качества

---

## Question 10: Read Group






Зачем нужен Read Group (@RG) в SAM/BAM?

A) Для удаления дубликатов

B) Для сортировки ридов

C) Для индексации файла

D) Для группировки ридов из одного сэмпла/библиотеки

---

## Question 11: FastQC метрики






Какой показатель качества в FastQC должен быть > 30?

A) Adapter content

B) GC content

C) Per base quality scores

D) Sequence length

---

## Question 12: samtools sort






Что делает команда `samtools sort`?

A) Конвертирует SAM в BAM

B) Индексирует файл

C) Сортирует риды по геномным координатам

D) Удаляет дубликаты

---

## Question 13: GVCF






Для чего используется GVCF формат?

A) Аннотация вариантов

B) Хранение только вариантов

C) Сжатие VCF файла

D) Хранение информации о всех позициях для joint calling

---

## Question 14: FS метрика






FS (Fisher Strand Bias) показывает:

A) Смещение по цепям (strand bias)

B) Покрытие позиции

C) Частоту аллеля

D) Качество выравнивания

---

## Question 15: VQSR






VQSR (Variant Quality Score Recalibration) это:

A) Простая фильтрация по порогам

B) Аннотация вариантов

C) Machine learning подход к фильтрации вариантов

D) Выравнивание ридов

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

A) Variant calling

B) Выравнивания ридов

C) Индексации файлов

D) Получения популяционных частот вариантов

---

## Question 18: GQ






GQ (Genotype Quality) в VCF показывает:

A) Качество варианта в целом

B) Покрытие позиции

C) Уверенность в определённом генотипе

D) Частоту аллеля

---

## Question 19: Duplication rate






Какой максимальный допустимый duplication rate для качественных данных?

A) 5%

B) 50%

C) 80%

D) 20%

---

## Question 20: samtools index






Какое расширение файла создаёт `samtools index` для BAM?

A) .tbi

B) .idx

C) .fai

D) .bai

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | QC → Alignment → Variant Calling → Filtering — правильный порядок. |
| 2 | B | BWA выравнивает риды на референс-геном. |
| 3 | C | Дубликаты — это PCR artifacts с одинаковыми координатами. |
| 4 | C | BQSR корректирует качество на основе known sites. |
| 5 | D | HaplotypeCaller вызывает варианты из BAM файла. |
| 6 | C | 30x — стандартное покрытие для клинического анализа. |
| 7 | B | QD = QUAL / DP (качество нормализованное на глубину). |
| 8 | A | SnpEff аннотирует эффекты вариантов на гены и белки. |
| 9 | D | PASS означает успешное прохождение всех фильтров качества. |
| 10 | D | @RG группирует риды из одного источника (сэмпл/библиотека). |
| 11 | C | Per base quality > 30 означает точность 99.9%. |
| 12 | C | samtools sort сортирует риды по координатам для последующего анализа. |
| 13 | D | GVCF хранит информацию о всех позициях для joint genotyping. |
| 14 | A | Fisher Strand Bias показывает перекос по цепям (возможный артефакт). |
| 15 | C | VQSR использует machine learning для фильтрации вариантов. |
| 16 | D | VEP добавляет consequence, SIFT/PolyPhen, gnomAD, ClinVar. |
| 17 | D | gnomAD — база данных популяционных частот вариантов. |
| 18 | C | GQ показывает уверенность в определённом генотипе (0/1, 1/1 и т.д.). |
| 19 | D | Duplication rate < 20% считается приемлемым. |
| 20 | D | samtools index создаёт .bai индекс для BAM файла. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы освоили variant calling пайплайны. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики с пайплайнами. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попробуйте ещё раз. |

---
