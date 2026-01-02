# Пайплайны Variant Calling
## От сырых данных FASTQ до аннотированных вариантов VCF

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [02_File_Formats](../03_File_Formats/) — форматы файлов
- Понимать структуру FASTQ, BAM, VCF файлов
- Иметь опыт работы с командной строкой Linux/macOS

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Описывать полный пайплайн variant calling от FASTQ до VCF
- Выполнять выравнивание ридов с BWA
- Применять GATK Best Practices для поиска вариантов
- Аннотировать варианты с SnpEff/VEP
- Фильтровать варианты по качеству и функциональному эффекту

---

## 1. Введение

Variant calling — это процесс идентификации генетических вариантов (отличий от референса) из данных секвенирования. Это ключевой этап анализа геномных данных, особенно в клинической диагностике.

**Pipeline: FASTQ → BAM → VCF**

---

## 1. Обзор Полного Пайплайна

```
Сырые данные (FASTQ)
    ↓
Quality Control (FastQC)
    ↓
Alignment to Reference (BWA)
    ↓
SAM → BAM conversion (samtools)
    ↓
Sort & Index BAM (samtools)
    ↓
Mark Duplicates (Picard)
    ↓
Base Quality Recalibration (GATK)
    ↓
Variant Calling (GATK HaplotypeCaller)
    ↓
Variant Filtering (GATK VariantFiltration)
    ↓
Annotation (SnpEff, VEP)
    ↓
Final Variants (VCF)
```

---

## 2. Quality Control

### 2.1 Зачем нужен QC?

Проверить качество данных перед анализом. Плохие данные → плохие результаты.

### 2.2 FastQC

```bash
# Запуск FastQC

fastqc sample_R1.fastq.gz sample_R2.fastq.gz

# Вывод: HTML отчёт с метриками
```

**Что проверяем:**

- Per base quality scores (должны быть >30)
- Per sequence GC content
- Adapter contamination
- Duplication levels
- Overrepresented sequences

### 2.3 MultiQC

Агрегирует отчёты от многих инструментов:

```bash
multiqc .
```

---

## 3. Alignment (Выравнивание)

### 3.1 Референс-геном

Скачать и индексировать:

```bash
# Скачать hg38 референс

wget ftp://ftp.ensembl.org/pub/release-104/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
gunzip Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

# Индексировать для BWA

bwa index reference.fasta

# Создать .fai индекс

samtools faidx reference.fasta

# Создать .dict словарь

samtools dict reference.fasta > reference.dict
```

### 3.2 BWA Alignment

BWA (Burrows-Wheeler Aligner) — основной инструмент для выравнивания коротких ридов.

```bash
# BWA MEM для paired-end ридов

bwa mem -t 8 -R '@RG\tID:sample\tSM:sample\tPL:ILLUMINA' \
    reference.fasta \
    sample_R1.fastq.gz \
    sample_R2.fastq.gz \
    > sample.sam

# -t 8: использовать 8 потоков
# -R: read group (важно для GATK!)
```

**Read Group (@RG):**

- **ID**: уникальный идентификатор

- **SM**: имя сэмпла

- **PL**: платформа (ILLUMINA, PACBIO, etc)

---

## 4. Post-Alignment Processing

### 4.1 SAM → BAM Конвертация и Сортировка

```bash
# Конвертировать в BAM и сразу отсортировать

samtools view -b sample.sam | samtools sort -o sample.sorted.bam

# Индексировать

samtools index sample.sorted.bam

# Удалить SAM (он огромный)

rm sample.sam
```

### 4.2 Mark Duplicates

Дубликаты — это риды с одинаковым началом и концом (PCR artifacts).

```bash
# Picard MarkDuplicates

java -jar picard.jar MarkDuplicates \
    I=sample.sorted.bam \
    O=sample.dedup.bam \
    M=sample.metrics.txt

# Индексировать

samtools index sample.dedup.bam
```

**Зачем:** Дубликаты искажают частоты аллелей.

### 4.3 Base Quality Score Recalibration (BQSR)

GATK перекалибрует quality scores на основе известных вариантов.

```bash
# 1. BuildBQSRModel

gatk BaseRecalibrator \
    -I sample.dedup.bam \
    -R reference.fasta \
    --known-sites dbsnp.vcf \
    --known-sites 1000G_phase1.snps.high_confidence.vcf \
    -O recal_data.table

# 2. ApplyBQSR

gatk ApplyBQSR \
    -R reference.fasta \
    -I sample.dedup.bam \
    --bqsr-recal-file recal_data.table \
    -O sample.recal.bam
```

---

## 5. Variant Calling

### 5.1 GATK HaplotypeCaller

Best practice для germline variants.

```bash
gatk HaplotypeCaller \
    -R reference.fasta \
    -I sample.recal.bam \
    -O sample.raw.vcf
```

**Что делает:**

1. Определяет активные регионы (где есть вариации)
2. Пересобирает гаплотипы в этих регионах
3. Вызывает варианты

### 5.2 Joint Calling (для нескольких сэмплов)

```bash
# Шаг 1: создать GVCF для каждого сэмпла

gatk HaplotypeCaller \
    -R reference.fasta \
    -I sample1.recal.bam \
    -O sample1.g.vcf \
    -ERC GVCF

# Шаг 2: объединить все GVCF

gatk CombineGVCFs \
    -R reference.fasta \
    --variant sample1.g.vcf \
    --variant sample2.g.vcf \
    -O cohort.g.vcf

# Шаг 3: joint genotyping

gatk GenotypeGVCFs \
    -R reference.fasta \
    -V cohort.g.vcf \
    -O cohort.vcf
```

---

## 6. Variant Filtering

### 6.1 Hard Filtering

Простая фильтрация по параметрам качества:

```bash
# Фильтровать SNPs

gatk VariantFiltration \
    -R reference.fasta \
    -V sample.raw.vcf \
    -O sample.filtered.vcf \
    --filter-name "QD_filter" --filter-expression "QD < 2.0" \
    --filter-name "FS_filter" --filter-expression "FS > 60.0" \
    --filter-name "MQ_filter" --filter-expression "MQ < 40.0"
```

**Критерии (для SNPs):**

- **QD** (Quality by Depth) > 2.0

- **FS** (Fisher Strand Bias) < 60.0

- **MQ** (Mapping Quality) > 40.0

- **SOR** (Strand Odds Ratio) < 3.0

### 6.2 VQSR (Variant Quality Score Recalibration)

Machine learning подход (для больших когорт):

```bash
# Построить модель

gatk VariantRecalibrator \
    -R reference.fasta \
    -V cohort.vcf \
    --resource:hapmap,known=false,training=true,truth=true,prior=15.0 hapmap.vcf \
    --resource:1000G,known=false,training=true,truth=false,prior=10.0 1000G.vcf \
    -an QD -an FS -an SOR -an MQ \
    -mode SNP \
    -O cohort.recal \
    --tranches-file cohort.tranches

# Применить

gatk ApplyVQSR \
    -R reference.fasta \
    -V cohort.vcf \
    --recal-file cohort.recal \
    --tranches-file cohort.tranches \
    -mode SNP \
    -O cohort.vqsr.vcf
```

---

## 7. Variant Annotation

### 7.1 SnpEff

Аннотация вариантов (гены, эффекты):

```bash
# Скачать базу данных

java -jar snpEff.jar download GRCh38.99

# Аннотировать

java -jar snpEff.jar GRCh38.99 sample.filtered.vcf > sample.annotated.vcf
```

**Аннотации:**

- Gene name
- Transcript
- Effect (missense, nonsense, splice site, etc)
- Impact (HIGH, MODERATE, LOW, MODIFIER)

### 7.2 VEP (Variant Effect Predictor)

Более детальная аннотация:

```bash
vep -i sample.filtered.vcf \
    -o sample.vep.vcf \
    --cache \
    --everything \
    --vcf
```

**Добавляет:**

- Consequence predictions
- Pathogenicity scores (SIFT, PolyPhen)
- Population frequencies (gnomAD, 1000G)
- Clinical annotations (ClinVar)

---

## 8. Интерпретация Результатов

### 8.1 Ключевые метрики в VCF

```vcf
chr1  12345  .  A  G  999  PASS  DP=100;AF=0.5;QD=25  GT:DP:GQ  0/1:50:99
```

- **DP** (Depth): покрытие (чем выше, тем лучше, обычно 20-100x)

- **AF** (Allele Frequency): частота альтернативного аллеля

- **QD** (Quality by Depth): нормализованное качество

- **GQ** (Genotype Quality): уверенность в генотипе

- **GT** (Genotype): 0/0, 0/1, 1/1

### 8.2 Фильтрация для клинического анализа

```python
import pysam

vcf = pysam.VariantFile("sample.annotated.vcf")

for variant in vcf:
    # Только PASS
    if variant.filter.keys() != ['PASS']:
        continue
    
    # Достаточное покрытие
    if variant.info.get('DP', 0) < 20:
        continue
    
    # Высокое качество
    if variant.qual < 30:
        continue
    
    # Редкий вариант (не в популяции)
    gnomad_af = variant.info.get('gnomAD_AF', 0)
    if gnomad_af > 0.01:  # Частота > 1%
        continue
    
    # Патогенный эффект
    impact = variant.info.get('ANN', [''])[0].split('|')[2]
    if impact in ['HIGH', 'MODERATE']:
        print(f"Pathogenic variant: {variant.chrom}:{variant.pos} {variant.ref}>{variant.alts[0]}")
```

---

## 9. Best Practices

### 9.1 GATK Best Practices

```
1. QC → 2. Align → 3. MarkDuplicates → 4. BQSR → 5. Call Variants → 6. Filter → 7. Annotate
```

### 9.2 Минимальные требования к данным

- **Coverage**: минимум 20x, рекомендуется 30x

- **Quality**: средний Phred > 30

- **Duplication rate**: < 20%

---

## Резюме

- ✅ Полный пайплайн от FASTQ до аннотированного VCF
- ✅ QC → Alignment → Processing → Calling → Filtering → Annotation
- ✅ GATK Best Practices workflow
- ✅ Ключевые инструменты: BWA, SAMtools, GATK, SnpEff
- ✅ Критерии качества для клинического анализа

---

## 🚀 Следующие Шаги

**Связанные модули:**

- [CLI Tools](../05_CLI_Tools/) — детальная работа с samtools, bcftools, bedtools
- [Эпигенетика](../06_Epigenetics/) — GWAS, фармакогенетика, клиническая интерпретация

**Практические задачи для закрепления:**

1. Запустите FastQC на FASTQ файле и проанализируйте метрики
2. Выполните полный alignment с BWA и получите отсортированный BAM
3. Пометьте дубликаты с Picard и посчитайте процент дубликатов
4. Вызовите варианты с GATK HaplotypeCaller
5. Отфильтруйте VCF: QUAL ≥ 30, DP ≥ 20, только PASS
6. Аннотируйте варианты с SnpEff и найдите HIGH impact

> **💡 Совет:** Напишите bash-скрипт, автоматизирующий весь пайплайн с логированием каждого шага.

**Для углублённого изучения:**

- Somatic variant calling (для онкологии)
- Joint calling для когорт пациентов
- Structural variant calling (большие перестройки)

---

## 📚 Дополнительные Ресурсы

### GATK Best Practices

- [GATK Best Practices Workflows](https://gatk.broadinstitute.org/hc/en-us/sections/360007226651) — Официальные best practices от Broad Institute
- [GATK Tutorials](https://gatk.broadinstitute.org/hc/en-us/sections/360007226531) — Пошаговые туториалы
- [GATK Workshop Materials](https://gatk.broadinstitute.org/hc/en-us/sections/360007226831) — Материалы воркшопов

### Инструменты

- [BWA](http://bio-bwa.sourceforge.net/) — Burrows-Wheeler Aligner
- [GATK](https://gatk.broadinstitute.org/) — Genome Analysis Toolkit
- [Picard Tools](https://broadinstitute.github.io/picard/) — Манипуляции с SAM/BAM
- [SnpEff](https://pcingola.github.io/SnpEff/) — Аннотация и предсказание эффектов
- [VEP](https://www.ensembl.org/vep) — Variant Effect Predictor от Ensembl

### Справочные Данные

- [GATK Resource Bundle](https://gatk.broadinstitute.org/hc/en-us/articles/360035890811) — Референсы и known sites
- [gnomAD](https://gnomad.broadinstitute.org/) — Популяционные частоты вариантов
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) — Клиническая значимость вариантов

---

## 💡 Key Takeaways

- **Пайплайн стандартизирован**: FASTQ → BWA → BAM → GATK → VCF → Annotation

- **Quality Control на каждом этапе**: FastQC, flagstat, VariantEval

- **GATK Best Practices** — индустриальный стандарт для germline variant calling

- **Фильтрация критична**: QUAL, DP, AF — основные метрики качества вариантов

- **Аннотация добавляет смысл**: SnpEff/VEP показывают функциональный эффект вариантов

---

## 🚀 Next Steps

**Следующие модули:**

- [05_CLI_Tools](../05_CLI_Tools/) — Инструменты командной строки (samtools, bcftools)
- [Эпигенетика и Маркеры](../06_Epigenetics/) — Эпигенетика и генетические маркеры

**Практика:**

1. Установите GATK и запустите HaplotypeCaller на тестовых данных
2. Отфильтруйте VCF по QUAL ≥ 30 и DP ≥ 10
3. Аннотируйте варианты с SnpEff и найдите HIGH impact мутации






