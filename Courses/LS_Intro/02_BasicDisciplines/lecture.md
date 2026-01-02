# Базовые научные дисциплины
## Bioinformatics, Cheminformatics, Medical Informatics и другие направления

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции Life Sciences Informatics (из модуля 01_Overview)
- Иметь представление о структуре биологических данных (ДНК, белки, молекулы)
- Знать основы работы с данными

**Recommended prior modules:**

- [01_Overview](../01_Overview/) — Общая картина Life Sciences Informatics

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать основные научные дисциплины Life Sciences Informatics
- Описывать типовые задачи и инструменты каждой дисциплины
- Понимать фокус и область применения Bioinformatics, Cheminformatics и Medical Informatics
- Применять знания о различных дисциплинах к практическим задачам
- Ориентироваться в инструментах и форматах данных каждой области

---

## 1. Bioinformatics

### 1.1 Определение и фокус

**Bioinformatics** (биоинформатика) — дисциплина, использующая вычислительные методы для анализа биологических данных, особенно связанных с ДНК, РНК, белками, клетками и организмами.

**Ключевые объекты изучения:**

```python
# Иерархия биологических объектов в Bioinformatics

bioinformatics_objects = {
    "молекулярный_уровень": {
        "днк": "Последовательности нуклеотидов (A, T, G, C)",
        "рнк": "Последовательности нуклеотидов (A, U, G, C)",
        "белки": "Последовательности аминокислот (20 типов)"
    },
    "клеточный_уровень": {
        "клетки": "Функциональные единицы организмов",
        "клеточные_процессы": "Экспрессия генов, метаболизм"
    },
    "организменный_уровень": {
        "организмы": "Целые живые существа",
        "популяции": "Группы организмов"
    }
}

print("Объекты изучения в Bioinformatics:\n")
for level, objects in bioinformatics_objects.items():
    print(f"{level.replace('_', ' ').title()}:")
    for obj, desc in objects.items():
        print(f"  • {obj.replace('_', ' ').title()}: {desc}")
    print()
```

**Output:**
```
Объекты изучения в Bioinformatics:

Молекулярный Уровень:
  • Днк: Последовательности нуклеотидов (A, T, G, C)
  • Рнк: Последовательности нуклеотидов (A, U, G, C)
  • Белки: Последовательности аминокислот (20 типов)

Клеточный Уровень:
  • Клетки: Функциональные единицы организмов
  • Клеточные Процессы: Экспрессия генов, метаболизм

Организменный Уровень:
  • Организмы: Целые живые существа
  • Популяции: Группы организмов
```

### 1.2 Типовые задачи Bioinformatics

**Основные классы задач:**

```python
# Типовые задачи Bioinformatics

bioinformatics_tasks = {
    "анализ_последовательностей": {
        "задачи": [
            "Выравнивание последовательностей (alignment)",
            "Поиск похожих последовательностей",
            "Поиск мотивов и паттернов",
            "Предсказание структуры"
        ],
        "примеры": ["BLAST поиск", "Multiple sequence alignment", "Motif finding"]
    },
    "сборка_геномов": {
        "задачи": [
            "De novo assembly из reads",
            "Сборка референсного генома",
            "Исправление ошибок",
            "Аннотация генов"
        ],
        "примеры": ["Genome assembly", "Scaffolding", "Gene prediction"]
    },
    "аннотация": {
        "задачи": [
            "Предсказание генов",
            "Функциональная аннотация",
            "Аннотация вариантов",
            "Сравнительная геномика"
        ],
        "примеры": ["Gene annotation", "Variant annotation", "Pathway analysis"]
    },
    "анализ_экспрессии": {
        "задачи": [
            "RNA-seq анализ",
            "Дифференциальная экспрессия",
            "Анализ альтернативного сплайсинга",
            "Co-expression networks"
        ],
        "примеры": ["Differential expression", "Pathway enrichment"]
    },
    "анализ_вариаций": {
        "задачи": [
            "Вызов вариантов (variant calling)",
            "Анализ SNP и инделей",
            "Структурные варианты",
            "Филогенетический анализ"
        ],
        "примеры": ["Variant calling", "Population genetics"]
    }
}

print("Типовые задачи Bioinformatics:\n")
for category, details in bioinformatics_tasks.items():
    print(f"{category.replace('_', ' ').title()}:")
    print(f"  Задачи: {', '.join(details['задачи'])}")
    print(f"  Примеры: {', '.join(details['примеры'])}")
    print()
```

**Output:**
```
Типовые задачи Bioinformatics:

Анализ Последовательностей:
  Задачи: Выравнивание последовательностей (alignment), Поиск похожих последовательностей, Поиск мотивов и паттернов, Предсказание структуры
  Примеры: BLAST поиск, Multiple sequence alignment, Motif finding

Сборка Геномов:
  Задачи: De novo assembly из reads, Сборка референсного генома, Исправление ошибок, Аннотация генов
  Примеры: Genome assembly, Scaffolding, Gene prediction

Аннотация:
  Задачи: Предсказание генов, Функциональная аннотация, Аннотация вариантов, Сравнительная геномика
  Примеры: Gene annotation, Variant annotation, Pathway analysis

Анализ Экспрессии:
  Задачи: RNA-seq анализ, Дифференциальная экспрессия, Анализ альтернативного сплайсинга, Co-expression networks
  Примеры: Differential expression, Pathway enrichment

Анализ Вариаций:
  Задачи: Вызов вариантов (variant calling), Анализ SNP и инделей, Структурные варианты, Филогенетический анализ
  Примеры: Variant calling, Population genetics
```

### 1.3 Инструменты и форматы данных

**Исторические вехи:**

- **1990:** BLAST (Basic Local Alignment Search Tool) — революция в поиске последовательностей

- **2000-е:** Human Genome Project — стандартизация форматов

- **2010-е:** NGS технологии — новые форматы и инструменты

**Основные форматы данных:**

```python
# Форматы данных в Bioinformatics

bioinformatics_formats = {
    "последовательности": {
        "fasta": "Формат для хранения последовательностей ДНК/РНК/белков",
        "fastq": "Формат для хранения reads с качеством (NGS)",
        "genbank": "Формат GenBank с аннотациями"
    },
    "выравнивания": {
        "sam": "Text-based формат выравниваний",
        "bam": "Binary формат выравниваний (сжатый SAM)",
        "paf": "Pairwise Alignment Format (для long reads)"
    },
    "вариации": {
        "vcf": "Variant Call Format — стандарт для геномных вариантов",
        "gff": "General Feature Format — аннотации генов"
    },
    "структуры": {
        "pdb": "Protein Data Bank — структуры белков",
        "mmcif": "Современный формат структурных данных"
    }
}

print("Форматы данных в Bioinformatics:\n")
for category, formats in bioinformatics_formats.items():
    print(f"{category.replace('_', ' ').title()}:")
    for fmt, desc in formats.items():
        print(f"  • {fmt.upper()}: {desc}")
    print()
```

**Output:**
```
Форматы данных в Bioinformatics:

Последовательности:
  • FASTA: Формат для хранения последовательностей ДНК/РНК/белков
  • FASTQ: Формат для хранения reads с качеством (NGS)
  • GENBANK: Формат GenBank с аннотациями

Выравнивания:
  • SAM: Text-based формат выравниваний
  • BAM: Binary формат выравниваний (сжатый SAM)
  • PAF: Pairwise Alignment Format (для long reads)

Вариации:
  • VCF: Variant Call Format — стандарт для геномных вариантов
  • GFF: General Feature Format — аннотации генов

Структуры:
  • PDB: Protein Data Bank — структуры белков
  • MMCIF: Современный формат структурных данных
```

**Популярные инструменты:**

| Инструмент | Назначение | Год создания |
|------------|-----------|--------------|
| **BLAST** | Поиск похожих последовательностей | 1990 |
| **Biopython** | Python библиотека для биоинформатики | 2000 |
| **BioConductor** | R пакеты для анализа биологических данных | 2001 |
| **Galaxy** | Веб-платформа для анализа данных | 2005 |
| **GATK** | Genome Analysis Toolkit | 2009 |
| **Nextflow** | Workflow management для биоданных | 2013 |

---

## 2. Cheminformatics

### 2.1 Определение и фокус

**Cheminformatics** (химическая информатика) — дисциплина, использующая вычислительные методы для анализа химических соединений и реакций.

**Ключевые объекты:**

```python
# Объекты изучения в Cheminformatics

cheminformatics_objects = {
    "молекулы": {
        "описание": "Химические соединения",
        "примеры": ["Лекарства", "Пестициды", "Материалы"]
    },
    "реакции": {
        "описание": "Химические превращения",
        "примеры": ["Синтез", "Разложение", "Катализ"]
    },
    "свойства": {
        "описание": "Физико-химические характеристики",
        "примеры": ["Растворимость", "Токсичность", "Активность"]
    }
}

print("Объекты изучения в Cheminformatics:\n")
for obj, details in cheminformatics_objects.items():
    print(f"{obj.replace('_', ' ').title()}:")
    print(f"  Описание: {details['описание']}")
    print(f"  Примеры: {', '.join(details['примеры'])}")
    print()
```

**Output:**
```
Объекты изучения в Cheminformatics:

Молекулы:
  Описание: Химические соединения
  Примеры: Лекарства, Пестициды, Материалы

Реакции:
  Описание: Химические превращения
  Примеры: Синтез, Разложение, Катализ

Свойства:
  Описание: Физико-химические характеристики
  Примеры: Растворимость, Токсичность, Активность
```

### 2.2 Типовые задачи Cheminformatics

**Основные классы задач:**

```python
# Типовые задачи Cheminformatics

cheminformatics_tasks = {
    "представление_молекул": {
        "задачи": [
            "Кодирование структуры молекул",
            "Конвертация между форматами",
            "Валидация структур"
        ],
        "форматы": ["SMILES", "InChI", "MOL", "SDF"]
    },
    "similarity_search": {
        "задачи": [
            "Поиск похожих молекул",
            "Структурный поиск",
            "Поиск по подструктурам"
        ],
        "применение": "Drug discovery, lead optimization"
    },
    "qsar_qspr": {
        "задачи": [
            "Quantitative Structure-Activity Relationship",
            "Quantitative Structure-Property Relationship",
            "Предсказание свойств по структуре"
        ],
        "примеры": ["Предсказание активности", "Предсказание токсичности"]
    },
    "drug_design": {
        "задачи": [
            "Виртуальный скрининг",
            "De novo design",
            "Оптимизация lead соединений"
        ],
        "примеры": ["Library design", "ADMET prediction"]
    }
}

print("Типовые задачи Cheminformatics:\n")
for category, details in cheminformatics_tasks.items():
    print(f"{category.replace('_', ' ').title()}:")
    if 'задачи' in details:
        print(f"  Задачи: {', '.join(details['задачи'])}")
    if 'форматы' in details:
        print(f"  Форматы: {', '.join(details['форматы'])}")
    if 'применение' in details:
        print(f"  Применение: {details['применение']}")
    if 'примеры' in details:
        print(f"  Примеры: {', '.join(details['примеры'])}")
    print()
```

**Output:**
```
Типовые задачи Cheminformatics:

Представление Молекул:
  Задачи: Кодирование структуры молекул, Конвертация между форматами, Валидация структур
  Форматы: SMILES, InChI, MOL, SDF

Similarity Search:
  Задачи: Поиск похожих молекул, Структурный поиск, Поиск по подструктурам
  Применение: Drug discovery, lead optimization

Qsar Qspr:
  Задачи: Quantitative Structure-Activity Relationship, Quantitative Structure-Property Relationship, Предсказание свойств по структуре
  Примеры: Предсказание активности, Предсказание токсичности

Drug Design:
  Задачи: Виртуальный скрининг, De novo design, Оптимизация lead соединений
  Примеры: Library design, ADMET prediction
```

### 2.3 Инструменты и форматы

**Исторические вехи:**

- **1988:** SMILES (Simplified Molecular Input Line Entry System) — текстовое представление молекул

- **2005:** InChI (International Chemical Identifier) — уникальный идентификатор молекул

**Основные форматы:**

| Формат | Описание | Применение |
|--------|----------|------------|
| **SMILES** | Текстовое представление структуры | Поиск, хранение, обмен |
| **InChI** | Уникальный идентификатор | Стандартизация, поиск |
| **MOL/SDF** | Структурные файлы | Визуализация, анализ |
| **SMARTS** | Паттерны для поиска | Структурный поиск |

**Популярные инструменты:**

```python
# Инструменты Cheminformatics

cheminformatics_tools = {
    "rdkit": {
        "тип": "Python библиотека",
        "назначение": "Обработка молекул, QSAR, визуализация",
        "год": "2006"
    },
    "open_babel": {
        "тип": "Конвертер форматов",
        "назначение": "Конвертация между химическими форматами",
        "год": "2001"
    },
    "chemdraw": {
        "тип": "Визуализация",
        "назначение": "Рисование и редактирование структур",
        "год": "1985"
    },
    "schrodinger": {
        "тип": "Коммерческая платформа",
        "назначение": "Drug discovery, molecular modeling",
        "год": "1990"
    }
}

print("Инструменты Cheminformatics:\n")
for tool, info in cheminformatics_tools.items():
    print(f"{tool.replace('_', ' ').title()}:")
    print(f"  Тип: {info['тип']}")
    print(f"  Назначение: {info['назначение']}")
    print(f"  Год: {info['год']}")
    print()
```

**Output:**
```
Инструменты Cheminformatics:

Rdkit:
  Тип: Python библиотека
  Назначение: Обработка молекул, QSAR, визуализация
  Год: 2006

Open Babel:
  Тип: Конвертер форматов
  Назначение: Конвертация между химическими форматами
  Год: 2001

Chemdraw:
  Тип: Визуализация
  Назначение: Рисование и редактирование структур
  Год: 1985

Schrodinger:
  Тип: Коммерческая платформа
  Назначение: Drug discovery, molecular modeling
  Год: 1990
```

---

## 3. Medical & Clinical Informatics

### 3.1 Определение и фокус

**Medical & Clinical Informatics** (медицинская и клиническая информатика) — дисциплина, использующая информационные технологии для работы с клиническими данными и медицинскими процессами.

**Ключевые объекты:**

```python
# Объекты изучения в Medical Informatics

medical_informatics_objects = {
    "клинические_данные": {
        "типы": [
            "Электронные медицинские карты (EHR)",
            "Результаты лабораторных анализов",
            "Медицинские изображения",
            "Данные с устройств"
        ]
    },
    "медицинские_процессы": {
        "типы": [
            "Диагностика",
            "Лечение",
            "Мониторинг",
            "Профилактика"
        ]
    },
    "пациенты": {
        "фокус": "Индивидуальные данные пациентов",
        "применение": "Персонализированная медицина"
    }
}

print("Объекты изучения в Medical Informatics:\n")
for obj, details in medical_informatics_objects.items():
    print(f"{obj.replace('_', ' ').title()}:")
    if 'типы' in details:
        print(f"  Типы: {', '.join(details['типы'])}")
    if 'фокус' in details:
        print(f"  Фокус: {details['фокус']}")
    if 'применение' in details:
        print(f"  Применение: {details['применение']}")
    print()
```

**Output:**
```
Объекты изучения в Medical Informatics:

Клинические Данные:
  Типы: Электронные медицинские карты (EHR), Результаты лабораторных анализов, Медицинские изображения, Данные с устройств

Медицинские Процессы:
  Типы: Диагностика, Лечение, Мониторинг, Профилактика

Пациенты:
  Фокус: Индивидуальные данные пациентов
  Применение: Персонализированная медицина
```

### 3.2 Типовые задачи

**Основные классы задач:**

```python
# Типовые задачи Medical Informatics

medical_informatics_tasks = {
    "анализ_ehr": {
        "задачи": [
            "Извлечение информации из EHR",
            "Анализ истории болезни",
            "Выявление паттернов"
        ],
        "применение": "Clinical decision support, population health"
    },
    "clinical_decision_support": {
        "задачи": [
            "Поддержка принятия решений",
            "Алерты и напоминания",
            "Рекомендации по лечению"
        ],
        "примеры": ["Drug-drug interactions", "Clinical guidelines"]
    },
    "персонализированная_медицина": {
        "задачи": [
            "Интеграция геномных данных",
            "Предсказание ответа на лечение",
            "Оптимизация терапии"
        ],
        "примеры": ["Pharmacogenomics", "Precision oncology"]
    },
    "медицинская_аналитика": {
        "задачи": [
            "Анализ эффективности лечения",
            "Прогнозирование исходов",
            "Population health analytics"
        ],
        "примеры": ["Readmission prediction", "Disease surveillance"]
    }
}

print("Типовые задачи Medical Informatics:\n")
for category, details in medical_informatics_tasks.items():
    print(f"{category.replace('_', ' ').title()}:")
    print(f"  Задачи: {', '.join(details['задачи'])}")
    if 'применение' in details:
        print(f"  Применение: {details['применение']}")
    if 'примеры' in details:
        print(f"  Примеры: {', '.join(details['примеры'])}")
    print()
```

**Output:**
```
Типовые задачи Medical Informatics:

Анализ Ehr:
  Задачи: Извлечение информации из EHR, Анализ истории болезни, Выявление паттернов
  Применение: Clinical decision support, population health

Clinical Decision Support:
  Задачи: Поддержка принятия решений, Алерты и напоминания, Рекомендации по лечению
  Примеры: Drug-drug interactions, Clinical guidelines

Персонализированная Медицина:
  Задачи: Интеграция геномных данных, Предсказание ответа на лечение, Оптимизация терапия
  Примеры: Pharmacogenomics, Precision oncology

Медицинская Аналитика:
  Задачи: Анализ эффективности лечения, Прогнозирование исходов, Population health analytics
  Примеры: Readmission prediction, Disease surveillance
```

### 3.3 Стандарты и инструменты

**Ключевые стандарты:**

| Стандарт | Описание | Применение |
|----------|----------|------------|
| **HL7** | Health Level 7 — стандарт обмена медицинскими данными | Интеграция систем |
| **FHIR** | Fast Healthcare Interoperability Resources | Современный стандарт обмена |
| **DICOM** | Digital Imaging and Communications in Medicine | Медицинские изображения |
| **ICD-10** | Международная классификация болезней | Кодирование диагнозов |
| **SNOMED CT** | Систематизированная номенклатура медицины | Клиническая терминология |

**Инструменты и платформы:**

```python
# Инструменты Medical Informatics

medical_informatics_tools = {
    "ehr_systems": {
        "примеры": ["Epic", "Cerner", "Allscripts"],
        "назначение": "Управление электронными медицинскими картами"
    },
    "clinical_data_platforms": {
        "примеры": ["REDCap", "i2b2", "OMOP"],
        "назначение": "Хранение и анализ клинических данных"
    },
    "imaging_systems": {
        "примеры": ["PACS", "DICOM viewers"],
        "назначение": "Хранение и просмотр медицинских изображений"
    }
}

print("Инструменты Medical Informatics:\n")
for category, info in medical_informatics_tools.items():
    print(f"{category.replace('_', ' ').title()}:")
    print(f"  Примеры: {', '.join(info['примеры'])}")
    print(f"  Назначение: {info['назначение']}")
    print()
```

**Output:**
```
Инструменты Medical Informatics:

Ehr Systems:
  Примеры: Epic, Cerner, Allscripts
  Назначение: Управление электронными медицинскими картами

Clinical Data Platforms:
  Примеры: REDCap, i2b2, OMOP
  Назначение: Хранение и анализ клинических данных

Imaging Systems:
  Примеры: PACS, DICOM viewers
  Назначение: Хранение и просмотр медицинских изображений
```

---

## 4. Другие научные направления

### 4.1 Neuroinformatics

**Neuroinformatics** (нейроинформатика) — дисциплина, работающая с данными о мозге и нервной системе.

**Фокус:**

- Нейронные сети и их структура
- Данные нейровизуализации (fMRI, EEG)
- Моделирование нейронной активности

**Применение:**

- Понимание работы мозга
- Лечение неврологических заболеваний
- Brain-computer interfaces

### 4.2 Geoinformatics

**Geoinformatics** (геоинформатика) — работа с пространственными и экологическими данными в контексте life sciences.

**Фокус:**

- Распределение видов
- Экологические данные
- Климатические данные
- ГИС (геоинформационные системы)

**Применение:**

- Экология
- Сельское хозяйство
- Охрана природы

### 4.3 Materials Informatics

**Materials Informatics** (информатика материалов) — применение информатики к разработке и анализу материалов.

**Фокус:**

- Свойства материалов
- Дизайн новых материалов
- Предсказание характеристик

**Применение:**

- Биоматериалы
- Нанотехнологии
- Биомедицинские устройства

---

## 5. Сравнение дисциплин

### 5.1 Сравнительная таблица

| Дисциплина | Тип данных | Основной фокус | Типовые задачи |
|------------|-----------|----------------|----------------|
| **Bioinformatics** | Последовательности (ДНК, РНК, белки) | Биология | Анализ последовательностей, сборка геномов |
| **Cheminformatics** | Молекулы, структуры | Химия | Представление молекул, QSAR, drug design |
| **Medical Informatics** | Клинические данные | Медицина | Анализ EHR, clinical decision support |
| **Neuroinformatics** | Данные о мозге | Нейронауки | Нейровизуализация, моделирование |
| **Geoinformatics** | Пространственные данные | Экология | ГИС, экологический анализ |

### 5.2 Пересечения дисциплин

**Важно понимать:** Дисциплины часто пересекаются:

- **Bioinformatics + Cheminformatics** → Drug discovery

- **Bioinformatics + Medical Informatics** → Precision medicine

- **Все дисциплины** → Используют Scientific Informatics как базовый слой

---

## 💡 Key Takeaways

- **Bioinformatics** фокусируется на ДНК, РНК, белках и использует инструменты типа BLAST, Biopython

- **Cheminformatics** работает с химическими соединениями и использует SMILES, RDKit для drug design

- **Medical Informatics** обрабатывает клинические данные через HL7/FHIR стандарты и EHR системы

- **Другие направления** (Neuroinformatics, Geoinformatics, Materials Informatics) расширяют область применения
- Все дисциплины используют **Scientific Informatics** как фундаментальный слой

---

## 🚀 Next Steps

**Related Modules:**

- [03_Intersections](../03_Intersections/) — Пересечения и отличия дисциплин
- [04_AppliedDomains](../04_AppliedDomains/) — Прикладные домены Life Sciences Informatics
- [07_Tools](../07_Tools/) — Инструменты и технологии

**Practice Ideas:**

1. Изучите примеры данных в различных форматах (FASTA, SMILES, HL7)
2. Попробуйте базовые инструменты (Biopython, RDKit) на простых примерах
3. Изучите публичные базы данных каждой дисциплины

**Going Deeper:**

- Bioinformatics: "Bioinformatics and Functional Genomics" by Jonathan Pevsner
- Cheminformatics: "Introduction to Cheminformatics" курсы
- Medical Informatics: HL7/FHIR документация

---

## 📚 Additional Resources

**Documentation:**

- [NCBI Bioinformatics Resources](https://www.ncbi.nlm.nih.gov/) — база данных биологических данных
- [RDKit Documentation](https://www.rdkit.org/) — документация по Cheminformatics
- [HL7 FHIR](https://www.hl7.org/fhir/) — стандарт обмена медицинскими данными

**Articles & Tutorials:**

- "A Beginner's Guide to Bioinformatics" — вводные материалы
- "Cheminformatics: An Introduction" — обзор химической информатики

---



