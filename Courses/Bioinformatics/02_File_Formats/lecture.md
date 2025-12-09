# Форматы Файлов в Биоинформатике
## FASTA, FASTQ, SAM/BAM, VCF, BED и другие

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [01_Basics](../01_Basics/) — основы биоинформатики
- Понимать структуру ДНК и концепцию секвенирования
- Иметь опыт работы с текстовыми файлами и командной строкой

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Читать и интерпретировать файлы FASTA и FASTQ
- Работать с форматами выравнивания SAM/BAM
- Парсить VCF файлы с вариантами
- Использовать BED формат для геномных интервалов
- Выбирать подходящий формат для конкретной задачи

---

## 1. Введение

В биоинформатике существует несколько стандартных форматов файлов для хранения различных типов данных. Если вы знакомы с JSON, CSV, XML — концепция та же: структурированное хранение данных. В этом модуле мы разберём основные форматы, с которыми вы будете работать.

**После этого модуля вы поймете:**
- Структуру основных биоинформатических форматов
- Когда какой формат использовать
- Как читать и обрабатывать эти файлы
- Базовые операции с файлами через командную строку

---

## 1. FASTA — Формат Последовательностей

### 1.1 Структура

FASTA — это текстовый формат для хранения последовательностей ДНК, РНК или белков.

```
>sequence_id optional description here
ATCGATCGATCGATCG
ATCGATCGATCGATCG
>another_sequence some info here
GCTAGCTAGCTAGCTA
```

**Правила:**
- Строка с `>` — заголовок (header)
- Первое "слово" после `>` — это **ID** (до первого пробела)
- Всё после первого пробела — **описание** (опционально, может отсутствовать)
- Следующие строки — сама последовательность
- Последовательность может быть разбита на несколько строк (обычно по 60-80 символов)

### 1.2 Пример реального файла

```fasta
>chr1:100000-100100
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
ATCGATCGATCGATCG
>NM_001256799.3 Homo sapiens BRCA1 DNA repair gene
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
GCTAGCTAGCTAGCTA
```

В первом случае ID = `chr1:100000-100100`, описание отсутствует.  
Во втором — ID = `NM_001256799.3`, описание = `Homo sapiens BRCA1 DNA repair gene`.

### 1.3 Чтение FASTA в Python

#### Наивный подход: стандартные средства

Попробуем прочитать FASTA-файл обычным Python:

```python
# Наивное чтение FASTA
sequences = {}
current_id = None
current_seq = []

with open("sequences.fasta") as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if current_id:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:].split()[0]  # Берём ID (первое слово после >)
            current_seq = []
        else:
            current_seq.append(line)
    
    if current_id:  # Не забыть последнюю последовательность!
        sequences[current_id] = ''.join(current_seq)

print(sequences)
```

**Проблемы этого подхода:**
- Легко забыть сохранить последнюю последовательность
- Нужно вручную обрабатывать многострочные последовательности
- Нет валидации формата (некорректный файл не вызовет ошибку)
- Нет доступа к описанию, только к ID
- Не поддерживает сжатые файлы (.gz)
- При работе с большими файлами нужно самому реализовывать потоковую обработку

#### Правильный подход: BioPython

```python
from Bio import SeqIO

# SeqIO.parse(файл, формат) — возвращает итератор записей
for record in SeqIO.parse("sequences.fasta", "fasta"):
    print(f"ID: {record.id}")                # chr1:100000-100100
    print(f"Description: {record.description}")  # полная строка заголовка
    print(f"Sequence: {record.seq}")         # объект Seq с последовательностью
    print(f"Length: {len(record)}")          # длина последовательности
    print("---")
```

**Аргументы `SeqIO.parse()`:**
- **Первый аргумент** — путь к файлу (или file-like объект)
- **Второй аргумент** — формат файла: `"fasta"`, `"fastq"`, `"genbank"` и др.

**Преимущества BioPython:**
- Корректная обработка всех edge cases
- `record.seq` — специальный объект с методами для работы с последовательностью
- Поддержка множества форматов одним API
- Поддержка сжатых файлов, потоковой обработки и т.д.

**Аналогия:** FASTA — это как Markdown для последовательностей: простой текст с минимальной разметкой (заголовок начинается с `>`, всё остальное — контент).

---

## 2. FASTQ — Формат Сырых Данных Секвенирования

### 2.1 Структура

FASTQ содержит риды с информацией о качестве прочтения каждого нуклеотида.

```
@read_id
ATCGATCGATCG
+
IIIIIIIIIIII
```

**4 строки на один рид:**
1. `@read_id` — идентификатор рида
2. `ATCGATCGATCG` — сама последовательность
3. `+` — разделитель (иногда повторяет ID)
4. `IIIIIIIIIIII` — quality scores (по одному на каждый нуклеотид)

### 2.2 Quality Scores (Phred Scores)

Quality scores кодируются ASCII символами и показывают вероятность ошибки.

```
Symbol  ASCII  Phred  Error Probability
  !      33      0     1 in 1       (100%)
  I      73      40    1 in 10,000  (0.01%)
```

**Формула:**
```
Q = -10 * log10(P)
где P — вероятность ошибки
```

**Пример:**
```
Q30 → ошибка 1 на 1000 (точность 99.9%)
Q40 → ошибка 1 на 10000 (точность 99.99%)
```

### 2.3 Пример реального FASTQ

```fastq
@SRR123456.1 HWI-ST1234:123:C1234ACXX:1:1101:1234:2345 length=101
NATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
+
#AAFFJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
```

### 2.4 Чтение FASTQ в Python

```python
from Bio import SeqIO

for record in SeqIO.parse("reads.fastq", "fastq"):
    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
    print(f"Quality: {record.letter_annotations['phred_quality']}")
    print(f"Average Quality: {sum(record.letter_annotations['phred_quality'])/len(record):.2f}")

# Фильтрация по качеству
def filter_by_quality(fastq_in, fastq_out, min_quality=30):
    with open(fastq_out, 'w') as out:
        for record in SeqIO.parse(fastq_in, "fastq"):
            avg_qual = sum(record.letter_annotations['phred_quality']) / len(record)
            if avg_qual >= min_quality:
                SeqIO.write(record, out, "fastq")
```

**Аналогия:** FASTQ — это логи с метрикой качества каждой записи.

---

## 3. SAM/BAM — Alignment Formats

### 3.1 Что это?

После выравнивания ридов на референс-геном, результаты сохраняются в SAM (текстовый) или BAM (бинарный, сжатый).

**SAM** = Sequence Alignment/Map (текстовый, читаемый)  
**BAM** = Binary Alignment/Map (бинарный, компактный)

### 3.2 Структура SAM

```
@HD VN:1.6  SO:coordinate
@SQ SN:chr1 LN:248956422
@PG ID:bwa  PN:bwa  VN:0.7.17
read1   99   chr1   10000   60   100M   =   10200   300   ATCGATCG...   IIIIIIII...   NM:i:0
read2   147  chr1   10200   60   100M   =   10000   -300  GCTAGCTA...   JJJJJJJJ...   NM:i:1
```

**Секции:**
1. **Header lines** (начинаются с `@`) — метаданные
2. **Alignment lines** — каждый выровненный рид

### 3.3 Alignment Line (11 обязательных полей)

| № | Поле | Пример | Описание |
|---|------|--------|----------|
| 1 | QNAME | read1 | Имя рида |
| 2 | FLAG | 99 | Битовый флаг (парность, направление и т.д.) |
| 3 | RNAME | chr1 | Хромосома |
| 4 | POS | 10000 | Позиция начала выравнивания |
| 5 | MAPQ | 60 | Качество маппинга (0-255) |
| 6 | CIGAR | 100M | Как рид выровнен (M=match, I=insertion, D=deletion) |
| 7 | RNEXT | = | Хромосома пары (= значит та же) |
| 8 | PNEXT | 10200 | Позиция пары |
| 9 | TLEN | 300 | Длина фрагмента (insert size) |
| 10 | SEQ | ATCG... | Последовательность рида |
| 11 | QUAL | IIII... | Quality scores |

### 3.4 CIGAR String

Описывает, как рид выравнивается на референс:

```
100M      → 100 match (полное совпадение)
90M10S    → 90 match, 10 soft clip (не выровнено на конце)
80M2D18M  → 80 match, 2 deletion, 18 match
50M1I49M  → 50 match, 1 insertion, 49 match
```

**Операции:**
- **M** = Match (может быть mismatch, но выровнено)
- **I** = Insertion (есть в риде, нет в референсе)
- **D** = Deletion (есть в референсе, нет в риде)
- **S** = Soft clip (не выровнено, но сохранено)
- **H** = Hard clip (обрезано и удалено)

### 3.5 FLAG биты

FLAG — это битовое поле:

```
Flag  Bit  Значение
1     0x1  Paired read
2     0x2  Правильно выровнен в паре
4     0x4  Не выровнен
8     0x8  Пара не выровнена
16    0x10 Обратная цепь
64    0x40 Первый рид в паре
128   0x80 Второй рид в паре
```

**Пример:** FLAG=99 = 64+32+2+1 = первый рид, в паре, правильно выровнен

### 3.6 Работа с SAM/BAM

```python
import pysam

# Чтение BAM файла
bamfile = pysam.AlignmentFile("aligned.bam", "rb")

for read in bamfile:
    print(f"Read: {read.query_name}")
    print(f"Chromosome: {read.reference_name}")
    print(f"Position: {read.reference_start}")
    print(f"CIGAR: {read.cigarstring}")
    print(f"Is reverse: {read.is_reverse}")
    print(f"Mapping quality: {read.mapping_quality}")
    print("---")

bamfile.close()

# Подсчёт покрытия
def calculate_coverage(bamfile, chrom, start, end):
    bam = pysam.AlignmentFile(bamfile, "rb")
    coverage = bam.count_coverage(chrom, start, end)
    # coverage это 4 массива (A, C, G, T)
    total_coverage = [sum(x) for x in zip(*coverage)]
    return total_coverage
```

**Аналогия:** SAM — это таблица в БД, где каждая строка — выровненный рид.

---

## 4. VCF — Variant Call Format

### 4.1 Что это?

VCF хранит информацию о генетических вариантах (отличиях от референса).

### 4.2 Структура VCF

```vcf
##fileformat=VCFv4.2
##reference=hg38
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM  POS     ID      REF ALT QUAL    FILTER  INFO    FORMAT  Sample1
chr1    12345   rs123   A   G   999     PASS    DP=100  GT:DP   0/1:50
chr1    67890   .       T   C   500     PASS    DP=80   GT:DP   1/1:80
```

**Секции:**
1. **Meta-information lines** (`##`) — описание формата и полей
2. **Header line** (`#CHROM...`) — названия колонок
3. **Data lines** — варианты

### 4.3 Основные колонки

| Колонка | Описание | Пример |
|---------|----------|--------|
| CHROM | Хромосома | chr1 |
| POS | Позиция | 12345 |
| ID | ID варианта (dbSNP) | rs123 или `.` |
| REF | Референсный аллель | A |
| ALT | Альтернативный аллель | G |
| QUAL | Качество variant call | 999 |
| FILTER | Фильтр (PASS если OK) | PASS |
| INFO | Дополнительная инфа | DP=100;AF=0.5 |
| FORMAT | Формат для сэмплов | GT:DP:GQ |
| Sample1 | Данные сэмпла | 0/1:50:99 |

### 4.4 Генотипы (GT)

```
0/0  → Гомозигота по референсу (REF/REF)
0/1  → Гетерозигота (REF/ALT)
1/1  → Гомозигота по альтернативе (ALT/ALT)
1/2  → Два разных альтернативных аллеля
./.  → Генотип не определён
```

**Фазирование:**
```
0/1  → не фазировано (неизвестно, какая хромосома какой аллель)
0|1  → фазировано (известно, что REF от одного родителя, ALT от другого)
```

### 4.5 Типы вариантов

```vcf
# SNP (замена одного нуклеотида)
chr1  1000  .  A  G  ...

# Insertion (вставка)
chr1  2000  .  T  TGGG  ...

# Deletion (делеция)
chr1  3000  .  ATCG  A  ...

# MNP (замена нескольких нуклеотидов)
chr1  4000  .  AT  GC  ...
```

### 4.6 Работа с VCF

```python
import pysam

vcf = pysam.VariantFile("variants.vcf")

for variant in vcf:
    print(f"Variant: {variant.chrom}:{variant.pos}")
    print(f"REF: {variant.ref}, ALT: {variant.alts}")
    print(f"Quality: {variant.qual}")
    print(f"Filter: {variant.filter}")
    
    # Информация
    if 'DP' in variant.info:
        print(f"Depth: {variant.info['DP']}")
    
    # Генотипы
    for sample in variant.samples:
        gt = variant.samples[sample]['GT']
        print(f"Sample {sample}: {gt}")

vcf.close()
```

**Аналогия:** VCF — это diff файл, показывающий отличия от master branch (референса).

---

## 5. BED — Browser Extensible Data

### 5.1 Что это?

BED — простой формат для описания геномных интервалов/регионов.

### 5.2 Структура

Минимум 3 колонки (tab-separated):

```
chr1    1000    2000
chr1    5000    6000    gene1    100    +
chr2    3000    4000    gene2    200    -    3000    4000    255,0,0
```

**Колонки (первые 3 обязательные):**
1. **chrom** — хромосома
2. **chromStart** — начало (0-based, включительно)
3. **chromEnd** — конец (0-based, не включительно)
4. name — имя региона
5. score — оценка (0-1000)
6. strand — цепь (+/-)
7-12. дополнительные поля для визуализации

### 5.3 Важно: 0-based координаты

```
Последовательность:  A T C G A T C G
Позиции (1-based):   1 2 3 4 5 6 7 8
Позиции (0-based):   0 1 2 3 4 5 6 7

BED использует 0-based:
chr1  1  4  → захватывает позиции 1,2,3 (символы T,C,G)
```

### 5.4 Работа с BED

```python
import pandas as pd

# Чтение BED файла
bed = pd.read_csv('regions.bed', sep='\t', header=None, 
                  names=['chrom', 'start', 'end', 'name', 'score', 'strand'])

print(bed.head())

# Фильтрация регионов
long_regions = bed[bed['end'] - bed['start'] > 1000]

# Пересечение регионов (нужен bedtools)
import pybedtools

a = pybedtools.BedTool('regions_a.bed')
b = pybedtools.BedTool('regions_b.bed')

# Найти пересечения
intersection = a.intersect(b)
intersection.saveas('intersection.bed')
```

**Аналогия:** BED — это список интервалов, как time ranges в логах.

---

## 6. Сравнение Форматов

| Формат | Что хранит | Размер | Компрессия | Индексация |
|--------|------------|--------|------------|------------|
| **FASTA** | Последовательности | Средний | .gz | .fai |
| **FASTQ** | Риды + качество | Большой | .gz | Нет |
| **SAM** | Выравнивания | Огромный | → BAM | Нет |
| **BAM** | Выравнивания | Большой | Да | .bai |
| **VCF** | Варианты | Малый-средний | .gz | .tbi |
| **BED** | Регионы | Малый | .gz | Нет |

### Типичные размеры для целого генома (30x coverage):

```
FASTQ (сырые данные):     ~100-200 GB
BAM (выравнивания):       ~30-60 GB
VCF (варианты):           ~1-5 GB
```

---

## 7. Индексация Файлов

### 7.1 Зачем нужна индексация?

Чтобы быстро получить данные для конкретного региона без чтения всего файла.

```python
# БЕЗ индекса: читать весь файл
# С индексом: прыгнуть к нужному месту
```

### 7.2 Типы индексов

```bash
# FASTA index
samtools faidx reference.fasta
# Создаёт reference.fasta.fai

# BAM index
samtools index aligned.bam
# Создаёт aligned.bam.bai

# VCF index (bgzip + tabix)
bgzip variants.vcf  # → variants.vcf.gz
tabix -p vcf variants.vcf.gz  # → variants.vcf.gz.tbi
```

### 7.3 Использование индексированных файлов

```python
import pysam

# Быстрое чтение региона из BAM
bam = pysam.AlignmentFile("aligned.bam", "rb")
for read in bam.fetch("chr1", 10000, 20000):
    print(read.query_name)

# Быстрое чтение региона из VCF
vcf = pysam.VariantFile("variants.vcf.gz")
for variant in vcf.fetch("chr1", 10000, 20000):
    print(variant.pos, variant.ref, variant.alts)
```

**Без индекса это работать не будет!**

---

## 8. Конвертация Форматов

### 8.1 SAM ↔ BAM

```bash
# SAM → BAM
samtools view -b input.sam > output.bam

# BAM → SAM
samtools view -h input.bam > output.sam
```

### 8.2 Сжатие FASTQ/VCF

```bash
# Обычный gzip
gzip file.fastq  # → file.fastq.gz

# bgzip (block gzip, позволяет индексацию)
bgzip file.vcf  # → file.vcf.gz
tabix -p vcf file.vcf.gz  # индексировать
```

### 8.3 FASTA → 2bit (компактный формат)

```bash
faToTwoBit genome.fasta genome.2bit
```

---

## Резюме

В этом модуле вы изучили:

- ✅ **FASTA** — последовательности (референсы, гены)
- ✅ **FASTQ** — сырые риды с качеством
- ✅ **SAM/BAM** — выравнивания на референс
- ✅ **VCF** — генетические варианты
- ✅ **BED** — геномные интервалы
- ✅ Как читать и обрабатывать эти форматы в Python
- ✅ Важность индексации для больших файлов
- ✅ Базовые операции конвертации

### Ключевые выводы

1. **Каждый формат — для своей задачи:** последовательности, риды, выравнивания, варианты, регионы
2. **Индексация критична** для работы с большими файлами
3. **Бинарные форматы (BAM) намного компактнее** текстовых (SAM)
4. **Стандартизация** — все используют одни и те же форматы
5. **BioPython и pysam** — основные библиотеки для работы

### Следующие Шаги

**Связанные модули:**
- [Variant Calling](../03_Variant_Calling/) — как из FASTQ файлов получить VCF с вариантами
- [CLI Tools](../04_CLI_Tools/) — работа с файлами через командную строку

**Практические задачи для закрепления:**
1. Напишите парсер FASTA файла с подсчётом статистик (длина, GC-содержание)
2. Реализуйте фильтрацию FASTQ по качеству (avg_quality >= 30)
3. Напишите функцию декодирования SAM FLAG в читаемый формат
4. Разберите CIGAR строку на операции и подсчитайте длину на референсе
5. Прочитайте VCF и отфильтруйте только PASS SNPs с качеством >= 30

> **💡 Совет:** Используйте BioPython и pysam для проверки — сравните вывод вашего кода с библиотечным.

**Для углублённого изучения:**
- CRAM формат — более компактная альтернатива BAM
- GFF/GTF форматы для аннотации генов
- BigWig/BigBed для визуализации в браузерах генома

---

## 📚 Дополнительные Ресурсы

### Официальные Спецификации
- [SAM/BAM/CRAM Format Specification](https://samtools.github.io/hts-specs/) — Все спецификации в одном месте
- [VCF Format v4.3](https://samtools.github.io/hts-specs/VCFv4.3.pdf) — Детальное описание VCF
- [BED Format](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) — Описание от UCSC
- [FASTQ Format](https://en.wikipedia.org/wiki/FASTQ_format) — Подробное описание

### Инструменты Командной Строки
- [SAMtools](http://www.htslib.org/) — Работа с SAM/BAM/CRAM файлами
- [BCFtools](http://www.htslib.org/) — Работа с VCF/BCF файлами
- [BEDTools](https://bedtools.readthedocs.io/) — Операции с геномными интервалами
- [seqtk](https://github.com/lh3/seqtk) — Быстрая обработка FASTA/FASTQ
- [Tabix](http://www.htslib.org/doc/tabix.html) — Индексация tab-delimited файлов

### Python Библиотеки
- [BioPython SeqIO](https://biopython.org/wiki/SeqIO) — Работа с FASTA/FASTQ
- [pysam](https://pysam.readthedocs.io/) — Python интерфейс для SAM/BAM/VCF
- [PyVCF](https://pyvcf.readthedocs.io/) — Парсер VCF файлов
- [pybedtools](https://daler.github.io/pybedtools/) — Python обёртка для BEDTools

### Визуализация
- [IGV](https://software.broadinstitute.org/software/igv/) — Integrative Genomics Viewer
- [UCSC Genome Browser](https://genome.ucsc.edu/) — Веб-браузер геномных данных
- [JBrowse](https://jbrowse.org/) — Современный геномный браузер

### Примеры Данных
- [SAMtools Examples](https://github.com/samtools/samtools/tree/develop/examples) — Примеры файлов
- [1000 Genomes Data](https://www.internationalgenome.org/data) — Реальные геномные данные
- [GIAB Reference Materials](https://www.nist.gov/programs-projects/genome-bottle) — Эталонные данные

---

## 💡 Key Takeaways

- **FASTA** — простой текстовый формат для последовательностей (референсы, гены)
- **FASTQ** — сырые риды с качеством, основной входной формат для анализа
- **SAM/BAM** — выравнивания ридов на референс, BAM = сжатый бинарный SAM
- **VCF** — варианты (мутации), стандарт для хранения SNP/Indel/SV
- **BED** — геномные интервалы (регионы, гены, экзоны), используется для фильтрации
- **Индексация критична** — .bai, .tbi файлы позволяют быстрый доступ к регионам

---

## 🚀 Next Steps

**Следующие модули:**
- [03_Variant_Calling](../03_Variant_Calling/) — Пайплайны от FASTQ до VCF
- [04_CLI_Tools](../04_CLI_Tools/) — Инструменты командной строки для работы с файлами

**Практика:**
1. Скачайте пример FASTQ файла и проанализируйте качество с FastQC
2. Изучите структуру BAM файла с помощью `samtools view`
3. Напишите скрипт для парсинга VCF файла на Python с использованием pysam

