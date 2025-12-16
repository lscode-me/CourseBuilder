# CLI Tools - Quiz

Проверьте свои знания по биоинформатическим CLI инструментам: samtools, bcftools, bedtools, seqtk.

---

## Question 1: samtools view

Команда `samtools view -F 4` выводит:

A) Риды с качеством > 4

B) Unmapped reads

C) Первые 4 рида

D) Mapped reads

---

## Question 2: bcftools

Какой инструмент используется для работы с VCF файлами?

A) bedtools

B) samtools

C) bcftools

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

A) samtools sort

B) samtools view

C) samtools index

D) samtools faidx

---

## Question 5: Фильтрация VCF

Как оставить только PASS варианты с bcftools?

A) bcftools view -p PASS

B) bcftools select PASS

C) bcftools view -f PASS

D) bcftools filter PASS

---

## Question 6: Coverage

Какой инструмент подсчитывает покрытие BAM по BED регионам?

A) samtools coverage

B) Все вышеперечисленные

C) bedtools coverage

D) bcftools coverage

---

## Question 7: seqtk

seqtk используется для:

A) Вызова вариантов

B) Выравнивания ридов

C) Аннотации

D) Обработки FASTA/FASTQ файлов

---

## Question 8: Pipe

Что делает `|` (pipe) в bash?

A) Объединяет файлы

B) Передаёт вывод одной команды на вход другой

C) Комментирует строку

D) Сохраняет вывод в файл

---

## Question 9: Сортировка BAM

Почему важно сортировать BAM файл?

A) Для уменьшения размера

B) Для улучшения качества

C) Для удаления дубликатов

D) Для индексации и быстрого доступа к регионам

---

## Question 10: bgzip

В чём отличие bgzip от обычного gzip?

A) bgzip лучше сжимает

B) bgzip позволяет индексацию (block-compressed)

C) bgzip быстрее

D) Нет различий

---

## Question 11: samtools flagstat

Что показывает команда `samtools flagstat`?

A) Качество ридов

B) Содержимое BAM файла

C) Статистику по mapped/unmapped/paired reads

D) Покрытие по позициям

---

## Question 12: bcftools stats

Что делает команда `bcftools stats`?

A) Сортирует варианты

B) Показывает статистику VCF файла (SNPs, indels, transitions/transversions)

C) Индексирует VCF

D) Фильтрует варианты

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

A) Разбивает файл на части

B) Извлекает случайные 10000 ридов (subsampling)

C) Фильтрует по качеству 10000

D) Обрезает первые 10000 оснований

---

## Question 15: samtools view -c

Что означает флаг `-c` в `samtools view -c aligned.bam`?

A) Сортировать по chromsome

B) Подсчитать количество ридов (count)

C) Конвертировать в CRAM

D) Проверить целостность

---

## Question 16: bcftools norm

Для чего используется `bcftools norm`?

A) Нормализация и left-align indels

B) Фильтрация по качеству

C) Аннотация вариантов

D) Подсчёт статистики

---

## Question 17: bedtools merge

Что делает `bedtools merge`?

A) Объединяет перекрывающиеся интервалы в один

B) Сортирует интервалы

C) Находит пересечения

D) Объединяет несколько BED файлов

---

## Question 18: samtools view -f 2

Что делает флаг `-f 2` в samtools view?

A) Выводит риды с качеством > 2

B) Выводит первые 2 рида

C) Выводит риды с FLAG 2 (properly paired)

D) Выводит 2 колонки

---

## Question 19: bedtools coverage -mean

Что добавляет флаг `-mean` в `bedtools coverage`?

A) Среднее покрытие для каждого региона

B) Максимальное покрытие

C) Медианное покрытие

D) Количество баз

---

## Question 20: bcftools query

Для чего используется `bcftools query`?

A) Поиск вариантов по ID

B) Статистика VCF

C) Извлечение полей из VCF в произвольном формате

D) Индексация VCF

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `-F 4` исключает unmapped (FLAG 4), т.е. выводит mapped reads. |
| 2 | C | bcftools — специализированный инструмент для VCF/BCF файлов. |
| 3 | B | `-v` выводит регионы из A, которые НЕ пересекаются с B. |
| 4 | C | `samtools index` создаёт .bai индекс для BAM файла. |
| 5 | C | `bcftools view -f PASS` фильтрует варианты по PASS статусу. |
| 6 | C | bedtools coverage подсчитывает покрытие по регионам. |
| 7 | D | seqtk — быстрый инструмент для обработки FASTA/FASTQ. |
| 8 | B | Pipe (`\|`) передаёт stdout одной команды на stdin другой. |
| 9 | D | Сортировка нужна для индексации и random access к регионам. |
| 10 | B | bgzip — block-compressed gzip, позволяет индексацию с tabix. |
| 11 | C | flagstat показывает статистику: total, mapped, properly paired, duplicates. |
| 12 | B | bcftools stats выводит SNPs, indels, Ti/Tv ratio и другую статистику. |
| 13 | B | getfasta извлекает последовательности из FASTA по BED координатам. |
| 14 | B | seqtk sample делает случайную выборку (subsampling) ридов. |
| 15 | B | `-c` = count, подсчитывает количество ридов вместо вывода. |
| 16 | A | bcftools norm нормализует и выравнивает indels влево. |
| 17 | A | merge объединяет перекрывающиеся интервалы в один. |
| 18 | C | `-f 2` включает только риды с FLAG 2 (properly paired). |
| 19 | A | `-mean` добавляет колонку со средним покрытием региона. |
| 20 | C | bcftools query извлекает поля из VCF в произвольном формате. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили CLI инструменты. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики в командной строке. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попрактикуйтесь. |

---
