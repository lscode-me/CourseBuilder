# CLI Tools - Quiz

Проверьте свои знания по биоинформатическим CLI инструментам: samtools, bcftools, bedtools, seqtk.

---

## Question 1: samtools view

Команда `samtools view -F 4` выводит:

A) Unmapped reads

B) Mapped reads

C) Первые 4 рида

D) Риды с качеством > 4

---

## Question 2: bcftools

Какой инструмент используется для работы с VCF файлами?

A) samtools

B) bcftools

C) bedtools

D) seqtk

---

## Question 3: bedtools intersect

`bedtools intersect -a A.bed -b B.bed -v` выводит:

A) Пересечения A и B

B) Регионы из A, которые НЕ пересекаются с B

C) Регионы из B

D) Объединение A и B

---

## Question 4: Индексация BAM

Какая команда создаёт индекс для BAM файла?

A) samtools index

B) samtools sort

C) samtools view

D) samtools faidx

---

## Question 5: Фильтрация VCF

Как оставить только PASS варианты с bcftools?

A) bcftools view -f PASS

B) bcftools filter PASS

C) bcftools view -p PASS

D) bcftools select PASS

---

## Question 6: Coverage

Какой инструмент подсчитывает покрытие BAM по BED регионам?

A) samtools coverage

B) bedtools coverage

C) bcftools coverage

D) Все вышеперечисленные

---

## Question 7: seqtk

seqtk используется для:

A) Выравнивания ридов

B) Обработки FASTA/FASTQ файлов

C) Вызова вариантов

D) Аннотации

---

## Question 8: Pipe

Что делает `|` (pipe) в bash?

A) Сохраняет вывод в файл

B) Передаёт вывод одной команды на вход другой

C) Комментирует строку

D) Объединяет файлы

---

## Question 9: Сортировка BAM

Почему важно сортировать BAM файл?

A) Для уменьшения размера

B) Для индексации и быстрого доступа к регионам

C) Для улучшения качества

D) Для удаления дубликатов

---

## Question 10: bgzip

В чём отличие bgzip от обычного gzip?

A) bgzip быстрее

B) bgzip позволяет индексацию (block-compressed)

C) bgzip лучше сжимает

D) Нет различий

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `-F 4` исключает unmapped (FLAG 4), т.е. выводит mapped reads. |
| 2 | B | bcftools — специализированный инструмент для VCF/BCF файлов. |
| 3 | B | `-v` выводит регионы из A, которые НЕ пересекаются с B. |
| 4 | A | `samtools index` создаёт .bai индекс для BAM файла. |
| 5 | A | `bcftools view -f PASS` фильтрует варианты по PASS статусу. |
| 6 | B | bedtools coverage подсчитывает покрытие по регионам. |
| 7 | B | seqtk — быстрый инструмент для обработки FASTA/FASTQ. |
| 8 | B | Pipe (`|`) передаёт stdout одной команды на stdin другой. |
| 9 | B | Сортировка нужна для индексации и random access к регионам. |
| 10 | B | bgzip — block-compressed gzip, позволяет индексацию с tabix. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили CLI инструменты. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики в командной строке. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попрактикуйтесь. |

---
