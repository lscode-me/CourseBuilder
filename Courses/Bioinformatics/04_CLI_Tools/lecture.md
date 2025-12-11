# Биоинформатические CLI Инструменты
## SAMtools, BCFtools, BEDtools и другие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [02_File_Formats](../02_File_Formats/) — форматы файлов
- Понимать структуру SAM/BAM, VCF, BED файлов
- Иметь опыт работы с командной строкой Linux/macOS

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать SAMtools для работы с BAM файлами
- Применять BCFtools для фильтрации и анализа VCF
- Выполнять операции с геномными интервалами через BEDtools
- Строить эффективные пайплайны из CLI инструментов

---

## 1. Введение

Командная строка — основной интерфейс работы в биоинформатике. В этом модуле вы освоите ключевые инструменты для обработки геномных данных.

---

## 2. SAMtools — Swiss Army Knife для SAM/BAM

### 1.1 Основные команды

```bash
# Просмотр BAM файла
samtools view aligned.bam | head

# С заголовком
samtools view -h aligned.bam | head

# Только mapped reads
samtools view -F 4 aligned.bam

# Конвертация SAM → BAM
samtools view -b input.sam > output.bam

# Сортировка
samtools sort input.bam -o sorted.bam

# Индексирование
samtools index sorted.bam

# Статистика
samtools flagstat aligned.bam
samtools stats aligned.bam
samtools idxstats aligned.bam

# Извлечение региона
samtools view aligned.bam chr1:1000-2000

# Покрытие
samtools depth aligned.bam
samtools coverage aligned.bam

```

### 1.2 Фильтрация

```bash
# Только properly paired reads
samtools view -f 2 -b aligned.bam > proper_pairs.bam

# Минимальное качество маппинга
samtools view -q 30 -b aligned.bam > high_quality.bam

# Конкретная хромосома
samtools view -b aligned.bam chr1 > chr1.bam

# Комбинирование
samtools view -f 2 -q 30 -b aligned.bam chr1 > filtered.bam

```

### 1.3 Merge и Split

```bash
# Объединить BAM файлы
samtools merge merged.bam sample1.bam sample2.bam sample3.bam

# Разделить по read group
samtools split -f 'rg_%!.bam' merged.bam

```

---

## 2. BCFtools — Работа с VCF

### 2.1 Просмотр и Статистика

```bash
# Просмотр VCF
bcftools view variants.vcf.gz | less

# Только SNPs
bcftools view -v snps variants.vcf.gz

# Только Indels
bcftools view -v indels variants.vcf.gz

# Статистика
bcftools stats variants.vcf.gz

# Подсчёт вариантов
bcftools view -H variants.vcf.gz | wc -l

```

### 2.2 Фильтрация

```bash
# Фильтровать по качеству
bcftools filter -i 'QUAL>30' variants.vcf.gz

# Фильтровать по глубине
bcftools filter -i 'INFO/DP>20' variants.vcf.gz

# Только PASS варианты
bcftools view -f PASS variants.vcf.gz

# Конкретный регион
bcftools view -r chr1:1000-2000 variants.vcf.gz

# Множественные условия
bcftools filter -i 'QUAL>30 && INFO/DP>20' variants.vcf.gz

```

### 2.3 Аннотация и Модификация

```bash
# Добавить ID из dbSNP
bcftools annotate -c ID -a dbsnp.vcf.gz variants.vcf.gz

# Нормализация
bcftools norm -m -any variants.vcf.gz

# Удалить дубликаты
bcftools norm -d all variants.vcf.gz

# Left-align indels
bcftools norm -f reference.fasta variants.vcf.gz

```

### 2.4 Сравнение VCF файлов

```bash
# Найти пересечения
bcftools isec -p output_dir sample1.vcf.gz sample2.vcf.gz

# Объединить VCF
bcftools merge sample1.vcf.gz sample2.vcf.gz -o merged.vcf

```

---

## 3. BEDtools — Геномные Интервалы

### 3.1 Пересечения

```bash
# Найти пересекающиеся регионы
bedtools intersect -a regions_a.bed -b regions_b.bed

# С процентом перекрытия
bedtools intersect -a regions_a.bed -b regions_b.bed -f 0.5

# Вывести только уникальные для A
bedtools intersect -a regions_a.bed -b regions_b.bed -v

```

### 3.2 Merge и Sort

```bash
# Объединить перекрывающиеся интервалы
bedtools merge -i regions.bed

# Сортировка
bedtools sort -i unsorted.bed > sorted.bed

```

### 3.3 Coverage

```bash
# Покрытие BAM по BED регионам
bedtools coverage -a exons.bed -b aligned.bam

# Histogram покрытия
bedtools coverage -a exons.bed -b aligned.bam -hist

# Среднее покрытие
bedtools coverage -a exons.bed -b aligned.bam -mean

```

### 3.4 Genomecov

```bash
# Геномное покрытие
bedtools genomecov -ibam aligned.bam -bg > coverage.bedgraph

# По базам
bedtools genomecov -ibam aligned.bam -d > coverage.txt

```

### 3.5 GetFasta

```bash
# Извлечь последовательности из FASTA по BED координатам
bedtools getfasta -fi reference.fasta -bed regions.bed -fo output.fasta

```

---

## 4. seqtk — Обработка FASTA/FASTQ

### 4.1 Базовые операции

```bash
# Конвертация FASTQ → FASTA
seqtk seq -a input.fastq > output.fasta

# Обратная комплементарная
seqtk seq -r input.fasta > reverse_complement.fasta

# Subsample (взять случайные 10000 ридов)
seqtk sample input.fastq 10000 > sample.fastq

# Обрезать качество
seqtk trimfq input.fastq > trimmed.fastq

```

### 4.2 Фильтрация

```bash
# Фильтровать по длине (>= 100bp)
seqtk seq -L 100 input.fastq > filtered.fastq

# Первые N последовательностей
seqtk seq -n 1000 input.fastq > first_1000.fastq

```

---

## 5. FastQC — Quality Control

```bash
# Запуск FastQC
fastqc sample_R1.fastq.gz sample_R2.fastq.gz

# Указать output директорию
fastqc -o output_dir sample.fastq.gz

# Множество файлов
fastqc *.fastq.gz

# Quiet mode
fastqc -q sample.fastq.gz

```

---

## 6. Комбинирование инструментов (Pipes)

### 6.1 Примеры пайплайнов

```bash
# Конвертировать SAM в sorted BAM
samtools view -b input.sam | samtools sort -o output.bam

# Фильтровать и индексировать
samtools view -q 30 -b input.bam | samtools sort -o filtered.bam
samtools index filtered.bam

# Извлечь регион и посчитать
samtools view input.bam chr1:1000-2000 | wc -l

# VCF: фильтровать и подсчитать
bcftools view -f PASS variants.vcf.gz | bcftools view -v snps | wc -l

# Покрытие конкретных регионов
bedtools intersect -a exons.bed -b aligned.bam | \
    bedtools coverage -a - -b aligned.bam

```

### 6.2 Практический пример: QC + Alignment + Stats

```bash
#!/bin/bash

SAMPLE=$1
REF="reference.fasta"

# QC
fastqc ${SAMPLE}_R1.fastq.gz ${SAMPLE}_R2.fastq.gz

# Alignment
bwa mem -t 8 $REF ${SAMPLE}_R1.fastq.gz ${SAMPLE}_R2.fastq.gz | \
    samtools view -b | \
    samtools sort -o ${SAMPLE}.bam

# Index
samtools index ${SAMPLE}.bam

# Stats
samtools flagstat ${SAMPLE}.bam > ${SAMPLE}.flagstat.txt
samtools stats ${SAMPLE}.bam > ${SAMPLE}.stats.txt

```

---

## 7. Полезные One-Liners

```bash
# Подсчитать количество mapped reads
samtools view -c -F 4 aligned.bam

# Найти read по имени
samtools view aligned.bam | grep "read_name"

# Извлечь последовательности ридов
samtools view aligned.bam | cut -f10

# Подсчитать SNPs и Indels отдельно
bcftools view -v snps variants.vcf.gz | bcftools view -H | wc -l
bcftools view -v indels variants.vcf.gz | bcftools view -H | wc -l

# Найти высококачественные варианты
bcftools view -i 'QUAL>50 && INFO/DP>30' variants.vcf.gz | wc -l

# Среднее покрытие по экзонам
bedtools coverage -a exons.bed -b aligned.bam -mean | \
    awk '{sum+=$4; count++} END {print sum/count}'

# Конвертировать BED в регионы для samtools
awk '{print $1":"$2"-"$3}' regions.bed

# Извлечь генотипы из VCF
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT]\n' variants.vcf.gz

```

---

## Резюме

- ✅ **samtools** — основной инструмент для SAM/BAM
- ✅ **bcftools** — работа с VCF файлами
- ✅ **bedtools** — операции с геномными интервалами
- ✅ **seqtk** — обработка FASTA/FASTQ
- ✅ **Pipes** — комбинирование инструментов для мощных пайплайнов

---

## 🚀 Следующие Шаги

**Связанные модули:**

- [Variant Calling](../03_Variant_Calling/) — полный пайплайн с использованием CLI инструментов
- [Эпигенетика](../05_Epigenetics_Markers/) — продвинутые анализы и клиническая интерпретация

**Практические задачи для закрепления:**

1. Получите статистику BAM файла: total/mapped/properly paired reads
2. Отфильтруйте BAM: MAPQ ≥ 30, properly paired, не дубликаты
3. Извлеките риды из конкретных регионов (BED файл)
4. Подсчитайте SNPs и Indels отдельно из VCF файла
5. Найдите варианты в экзонах (пересечение VCF и BED)
6. Подсчитайте среднее покрытие по генам
7. Создайте subset FASTQ файла (100,000 случайных ридов)

> **💡 Совет:** Напишите bash-скрипт, комбинирующий несколько инструментов в один pipeline.

**Для углублённого изучения:**

- AWK и sed для продвинутой обработки текста
- Snakemake/Nextflow для воспроизводимых пайплайнов
- Параллельная обработка с GNU parallel

---

## 📚 Дополнительные Ресурсы

### Документация

- [SAMtools](http://www.htslib.org/doc/samtools.html) — Полная документация samtools
- [BCFtools](http://www.htslib.org/doc/bcftools.html) — Документация bcftools
- [BEDTools](https://bedtools.readthedocs.io/) — Руководство по bedtools
- [seqtk](https://github.com/lh3/seqtk) — GitHub репозиторий seqtk

### Туториалы

- [SAMtools Tutorial](https://davetang.org/wiki/tiki-index.php?page=SAMtools) — Практические примеры
- [BEDTools Tutorial](https://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html) — Подробные примеры использования

---

## 💡 Key Takeaways

- **SAMtools** — универсальный инструмент для BAM: view, sort, index, flagstat, depth

- **BCFtools** — манипуляции с VCF: filter, query, stats, merge

- **BEDtools** — операции над интервалами: intersect, subtract, coverage

- **Пайпы критичны** — `|` позволяет строить эффективные цепочки команд

- **Индексация обязательна** — без .bai/.tbi файлов быстрый доступ к регионам невозможен

---

## 🚀 Next Steps

**Следующие модули:**

- [05_Epigenetics_Markers](../05_Epigenetics_Markers/) — Эпигенетика и генетические маркеры

**Практика:**

1. Отфильтруйте BAM: MAPQ ≥ 30, properly paired, не дубликаты
2. Извлеките варианты из VCF в определённых регионах (BED файл)
3. Подсчитайте среднее покрытие по генам из GTF/BED файла





