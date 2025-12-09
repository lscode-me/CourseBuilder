# Variant Calling - Quiz

Проверьте свои знания по пайплайнам variant calling: QC, alignment, variant calling, фильтрация и аннотация.

---

## Question 1: Порядок шагов




Правильный порядок основных шагов variant calling:

A) Alignment → QC → Variant Calling → Filtering

B) QC → Alignment → Variant Calling → Filtering

C) Variant Calling → Alignment → QC → Filtering

D) QC → Variant Calling → Alignment → Filtering

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

A) Повторяющиеся регионы генома

B) Риды с одинаковым началом и концом (PCR artifacts)

C) Ошибки секвенирования

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

B) Вызова вариантов

C) Фильтрации вариантов

D) Аннотации вариантов

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

A) Общее качество варианта

B) Качество, нормализованное на покрытие

C) Частота аллеля

D) Генотип качество

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

A) Вариант требует дополнительной проверки

B) Вариант — дубликат

C) Вариант не прошёл фильтры

D) Вариант прошёл все фильтры качества

---

## Question 10: Read Group




Зачем нужен Read Group (@RG) в SAM/BAM?

A) Для группировки ридов из одного сэмпла/библиотеки

B) Для индексации файла

C) Для сортировки ридов

D) Для удаления дубликатов

---

## Question 11: FastQC метрики




Какой показатель качества в FastQC должен быть > 30?

A) Per base quality scores

B) Sequence length

C) Adapter content

D) GC content

---

## Question 12: samtools sort




Что делает команда `samtools sort`?

A) Индексирует файл

B) Конвертирует SAM в BAM

C) Удаляет дубликаты

D) Сортирует риды по геномным координатам

---

## Question 13: GVCF




Для чего используется GVCF формат?

A) Хранение только вариантов

B) Хранение информации о всех позициях для joint calling

C) Сжатие VCF файла

D) Аннотация вариантов

---

## Question 14: FS метрика




FS (Fisher Strand Bias) показывает:

A) Частоту аллеля

B) Качество выравнивания

C) Смещение по цепям (strand bias)

D) Покрытие позиции

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

A) Consequence predictions, SIFT/PolyPhen scores, population frequencies

B) Только качество

C) Только название гена

D) Только координаты

---

## Question 17: gnomAD




gnomAD используется для:

A) Получения популяционных частот вариантов

B) Индексации файлов

C) Выравнивания ридов

D) Variant calling

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

B) 20%

C) 50%

D) 80%

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
| 1 | B | QC → Alignment → Variant Calling → Filtering — правильный порядок. |
| 2 | B | BWA выравнивает риды на референс-геном. |
| 3 | B | Дубликаты — это PCR artifacts с одинаковыми координатами. |
| 4 | C | BQSR корректирует качество на основе known sites. |
| 5 | B | HaplotypeCaller вызывает варианты из BAM файла. |
| 6 | C | 30x — стандартное покрытие для клинического анализа. |
| 7 | B | QD = QUAL / DP (качество нормализованное на глубину). |
| 8 | D | SnpEff аннотирует эффекты вариантов на гены и белки. |
| 9 | D | PASS означает успешное прохождение всех фильтров качества. |
| 10 | A | @RG группирует риды из одного источника (сэмпл/библиотека). |
| 11 | A | Per base quality > 30 означает точность 99.9%. |
| 12 | D | samtools sort сортирует риды по координатам для последующего анализа. |
| 13 | B | GVCF хранит информацию о всех позициях для joint genotyping. |
| 14 | C | Fisher Strand Bias показывает перекос по цепям (возможный артефакт). |
| 15 | C | VQSR использует machine learning для фильтрации вариантов. |
| 16 | A | VEP добавляет consequence, SIFT/PolyPhen, gnomAD, ClinVar. |
| 17 | A | gnomAD — база данных популяционных частот вариантов. |
| 18 | C | GQ показывает уверенность в определённом генотипе (0/1, 1/1 и т.д.). |
| 19 | B | Duplication rate < 20% считается приемлемым. |
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
