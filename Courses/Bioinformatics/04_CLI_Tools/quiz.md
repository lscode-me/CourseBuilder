# CLI Tools - Quiz

Проверьте свои знания по биоинформатическим CLI инструментам: samtools, bcftools, bedtools, seqtk.

---

## Question 1: samtools view






Команда `samtools view -F 4` выводит:

A) Риды с качеством > 4

B) Первые 4 рида

C) Unmapped reads

D) Mapped reads

---

## Question 2: bcftools






Какой инструмент используется для работы с VCF файлами?

A) bcftools

B) seqtk

C) samtools

D) bedtools

---

## Question 3: bedtools intersect






`bedtools intersect -a A.bed -b B.bed -v` выводит:

A) Регионы из A, которые НЕ пересекаются с B

B) Пересечения A и B

C) Регионы из B

D) Объединение A и B

---

## Question 4: Индексация BAM






Какая команда создаёт индекс для BAM файла?

A) samtools faidx

B) samtools index

C) samtools view

D) samtools sort

---

## Question 5: Фильтрация VCF






Как оставить только PASS варианты с bcftools?

A) bcftools select PASS

B) bcftools view -p PASS

C) bcftools view -f PASS

D) bcftools filter PASS

---

## Question 6: Coverage






Какой инструмент подсчитывает покрытие BAM по BED регионам?

A) bcftools coverage

B) samtools coverage

C) Все вышеперечисленные

D) bedtools coverage

---

## Question 7: seqtk






seqtk используется для:

A) Обработки FASTA/FASTQ файлов

B) Аннотации

C) Вызова вариантов

D) Выравнивания ридов

---

## Question 8: Pipe






Что делает `|` (pipe) в bash?

A) Объединяет файлы

B) Комментирует строку

C) Передаёт вывод одной команды на вход другой

D) Сохраняет вывод в файл

---

## Question 9: Сортировка BAM






Почему важно сортировать BAM файл?

A) Для улучшения качества

B) Для индексации и быстрого доступа к регионам

C) Для удаления дубликатов

D) Для уменьшения размера

---

## Question 10: bgzip






В чём отличие bgzip от обычного gzip?

A) bgzip быстрее

B) Нет различий

C) bgzip позволяет индексацию (block-compressed)

D) bgzip лучше сжимает

---

## Question 11: samtools flagstat






Что показывает команда `samtools flagstat`?

A) Содержимое BAM файла

B) Качество ридов

C) Покрытие по позициям

D) Статистику по mapped/unmapped/paired reads

---

## Question 12: bcftools stats






Что делает команда `bcftools stats`?

A) Показывает статистику VCF файла (SNPs, indels, transitions/transversions)

B) Сортирует варианты

C) Фильтрует варианты

D) Индексирует VCF

---

## Question 13: bedtools getfasta






Что делает `bedtools getfasta`?

A) Сортирует FASTA

B) Конвертирует FASTQ в FASTA

C) Извлекает последовательности из FASTA по BED координатам

D) Создаёт FASTA из BAM

---

## Question 14: seqtk sample






Что делает `seqtk sample input.fastq 10000`?

A) Разбивает файл на части

B) Обрезает первые 10000 оснований

C) Фильтрует по качеству 10000

D) Извлекает случайные 10000 ридов (subsampling)

---

## Question 15: samtools view -c






Что означает флаг `-c` в `samtools view -c aligned.bam`?

A) Проверить целостность

B) Подсчитать количество ридов (count)

C) Сортировать по chromsome

D) Конвертировать в CRAM

---

## Question 16: bcftools norm






Для чего используется `bcftools norm`?

A) Подсчёт статистики

B) Фильтрация по качеству

C) Нормализация и left-align indels

D) Аннотация вариантов

---

## Question 17: bedtools merge






Что делает `bedtools merge`?

A) Находит пересечения

B) Объединяет перекрывающиеся интервалы в один

C) Сортирует интервалы

D) Объединяет несколько BED файлов

---

## Question 18: samtools view -f 2






Что делает флаг `-f 2` в samtools view?

A) Выводит риды с FLAG 2 (properly paired)

B) Выводит первые 2 рида

C) Выводит 2 колонки

D) Выводит риды с качеством > 2

---

## Question 19: bedtools coverage -mean






Что добавляет флаг `-mean` в `bedtools coverage`?

A) Среднее покрытие для каждого региона

B) Медианное покрытие

C) Количество баз

D) Максимальное покрытие

---

## Question 20: bcftools query






Для чего используется `bcftools query`?

A) Статистика VCF

B) Поиск вариантов по ID

C) Индексация VCF

D) Извлечение полей из VCF в произвольном формате

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `-F 4` исключает unmapped (FLAG 4), т.е. выводит mapped reads. |
| 2 | A | bcftools — специализированный инструмент для VCF/BCF файлов. |
| 3 | A | `-v` выводит регионы из A, которые НЕ пересекаются с B. |
| 4 | B | `samtools index` создаёт .bai индекс для BAM файла. |
| 5 | C | `bcftools view -f PASS` фильтрует варианты по PASS статусу. |
| 6 | D | bedtools coverage подсчитывает покрытие по регионам. |
| 7 | A | seqtk — быстрый инструмент для обработки FASTA/FASTQ. |
| 8 | C | Pipe (`\|`) передаёт stdout одной команды на stdin другой. |
| 9 | B | Сортировка нужна для индексации и random access к регионам. |
| 10 | C | bgzip — block-compressed gzip, позволяет индексацию с tabix. |
| 11 | D | flagstat показывает статистику: total, mapped, properly paired, duplicates. |
| 12 | A | bcftools stats выводит SNPs, indels, Ti/Tv ratio и другую статистику. |
| 13 | C | getfasta извлекает последовательности из FASTA по BED координатам. |
| 14 | D | seqtk sample делает случайную выборку (subsampling) ридов. |
| 15 | B | `-c` = count, подсчитывает количество ридов вместо вывода. |
| 16 | C | bcftools norm нормализует и выравнивает indels влево. |
| 17 | B | merge объединяет перекрывающиеся интервалы в один. |
| 18 | A | `-f 2` включает только риды с FLAG 2 (properly paired). |
| 19 | A | `-mean` добавляет колонку со средним покрытием региона. |
| 20 | D | bcftools query извлекает поля из VCF в произвольном формате. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили CLI инструменты. |
| **7-8 правильных (70-80%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **5-6 правильных (50-60%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики в командной строке. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Перечитайте лекцию и попрактикуйтесь. |

---
