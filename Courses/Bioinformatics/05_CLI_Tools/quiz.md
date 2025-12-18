# CLI Tools - Quiz

Проверьте свои знания по биоинформатическим CLI инструментам: samtools, bcftools, bedtools, seqtk.

---

## Question 1: samtools view

Команда `samtools view -F 4` выводит:

A) Unmapped reads

B) Первые 4 рида

C) Риды с качеством > 4

D) Mapped reads

---

## Question 2: bcftools

Какой инструмент используется для работы с VCF файлами?

A) bedtools

B) seqtk

C) samtools

D) bcftools

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

A) samtools view

B) samtools faidx

C) samtools sort

D) samtools index

---

## Question 5: Фильтрация VCF

Как оставить только PASS варианты с bcftools?

A) bcftools view -f PASS

B) bcftools filter PASS

C) bcftools select PASS

D) bcftools view -p PASS

---

## Question 6: Coverage

Какой инструмент подсчитывает покрытие BAM по BED регионам?

A) bedtools coverage

B) bcftools coverage

C) samtools coverage

D) Все вышеперечисленные

---

## Question 7: seqtk

seqtk используется для:

A) Аннотации

B) Выравнивания ридов

C) Обработки FASTA/FASTQ файлов

D) Вызова вариантов

---

## Question 8: Pipe

Что делает `|` (pipe) в bash?

A) Сохраняет вывод в файл

B) Передаёт вывод одной команды на вход другой

C) Объединяет файлы

D) Комментирует строку

---

## Question 9: Сортировка BAM

Почему важно сортировать BAM файл?

A) Для удаления дубликатов

B) Для индексации и быстрого доступа к регионам

C) Для уменьшения размера

D) Для улучшения качества

---

## Question 10: bgzip

В чём отличие bgzip от обычного gzip?

A) bgzip позволяет индексацию (block-compressed)

B) bgzip быстрее

C) Нет различий

D) bgzip лучше сжимает

---

## Question 11: samtools flagstat

Что показывает команда `samtools flagstat`?

A) Статистику по mapped/unmapped/paired reads

B) Качество ридов

C) Покрытие по позициям

D) Содержимое BAM файла

---

## Question 12: bcftools stats

Что делает команда `bcftools stats`?

A) Фильтрует варианты

B) Индексирует VCF

C) Показывает статистику VCF файла (SNPs, indels, transitions/transversions)

D) Сортирует варианты

---

## Question 13: bedtools getfasta

Что делает `bedtools getfasta`?

A) Сортирует FASTA

B) Извлекает последовательности из FASTA по BED координатам

C) Конвертирует FASTQ в FASTA

D) Создаёт FASTA из BAM

---

## Question 14: seqtk sample

Что делает `seqtk sample input.fastq 10000`?

A) Фильтрует по качеству 10000

B) Извлекает случайные 10000 ридов (subsampling)

C) Разбивает файл на части

D) Обрезает первые 10000 оснований

---

## Question 15: samtools view -c

Что означает флаг `-c` в `samtools view -c aligned.bam`?

A) Подсчитать количество ридов (count)

B) Проверить целостность

C) Конвертировать в CRAM

D) Сортировать по chromsome

---

## Question 16: bcftools norm

Для чего используется `bcftools norm`?

A) Аннотация вариантов

B) Нормализация и left-align indels

C) Фильтрация по качеству

D) Подсчёт статистики

---

## Question 17: bedtools merge

Что делает `bedtools merge`?

A) Объединяет перекрывающиеся интервалы в один

B) Объединяет несколько BED файлов

C) Находит пересечения

D) Сортирует интервалы

---

## Question 18: samtools view -f 2

Что делает флаг `-f 2` в samtools view?

A) Выводит первые 2 рида

B) Выводит 2 колонки

C) Выводит риды с FLAG 2 (properly paired)

D) Выводит риды с качеством > 2

---

## Question 19: bedtools coverage -mean

Что добавляет флаг `-mean` в `bedtools coverage`?

A) Количество баз

B) Максимальное покрытие

C) Медианное покрытие

D) Среднее покрытие для каждого региона

---

## Question 20: bcftools query

Для чего используется `bcftools query`?

A) Извлечение полей из VCF в произвольном формате

B) Индексация VCF

C) Статистика VCF

D) Поиск вариантов по ID

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `-F 4` исключает unmapped (FLAG 4), т.е. выводит mapped reads. |
| 2 | D | bcftools — специализированный инструмент для VCF/BCF файлов. |
| 3 | B | `-v` выводит регионы из A, которые НЕ пересекаются с B. |
| 4 | D | `samtools index` создаёт .bai индекс для BAM файла. |
| 5 | A | `bcftools view -f PASS` фильтрует варианты по PASS статусу. |
| 6 | A | bedtools coverage подсчитывает покрытие по регионам. |
| 7 | C | seqtk — быстрый инструмент для обработки FASTA/FASTQ. |
| 8 | B | Pipe (`\|`) передаёт stdout одной команды на stdin другой. |
| 9 | B | Сортировка нужна для индексации и random access к регионам. |
| 10 | A | bgzip — block-compressed gzip, позволяет индексацию с tabix. |
| 11 | A | flagstat показывает статистику: total, mapped, properly paired, duplicates. |
| 12 | C | bcftools stats выводит SNPs, indels, Ti/Tv ratio и другую статистику. |
| 13 | B | getfasta извлекает последовательности из FASTA по BED координатам. |
| 14 | B | seqtk sample делает случайную выборку (subsampling) ридов. |
| 15 | A | `-c` = count, подсчитывает количество ридов вместо вывода. |
| 16 | B | bcftools norm нормализует и выравнивает indels влево. |
| 17 | A | merge объединяет перекрывающиеся интервалы в один. |
| 18 | C | `-f 2` включает только риды с FLAG 2 (properly paired). |
| 19 | D | `-mean` добавляет колонку со средним покрытием региона. |
| 20 | A | bcftools query извлекает поля из VCF в произвольном формате. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили CLI инструменты. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики в командной строке. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попрактикуйтесь. |

---
