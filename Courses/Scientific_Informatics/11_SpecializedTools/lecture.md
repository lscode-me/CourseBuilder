# Специализированные инструменты scientific informatics
## Bioinformatics/Cheminformatics tools, scientific workflows, workflow managers

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Scientific Informatics (модули 01-04)
- Знать Python и работу с данными (модуль 04_Tools)
- Понимать принципы автоматизации (модуль 07_Collaboration)
- Иметь представление о научных workflows

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать специализированные инструменты для bioinformatics и cheminformatics
- Создавать и управлять scientific workflows
- Применять workflow managers (Snakemake, Nextflow)
- Интегрировать различные инструменты в единый pipeline
- Выбирать подходящие инструменты для конкретных научных задач

---

## 1. Bioinformatics Tools

### 1.1 Biopython

**Biopython** — библиотека Python для работы с биологическими данными.

**Пример: Работа с последовательностями**

```python
# Биоинформатика с Biopython
# from Bio import SeqIO
# from Bio.Seq import Seq
# from Bio.SeqUtils import GC

# # Чтение FASTA файла
# sequences = SeqIO.parse("sequences.fasta", "fasta")
# for record in sequences:
#     seq = record.seq
#     gc_content = GC(seq)
#     print(f"{record.id}: GC content = {gc_content:.2f}%")

print("Biopython provides:")
print("- Sequence manipulation")
print("- File format parsing (FASTA, GenBank, etc.)")
print("- Sequence analysis tools")
print("- Database access")
```

**Output:**
```

Biopython provides:
- Sequence manipulation
- File format parsing (FASTA, GenBank, etc.)
- Sequence analysis tools
- Database access
```

### 1.2 BLAST

**BLAST** — поиск гомологичных последовательностей.

**Пример: Концепция BLAST**

```python
# BLAST (Basic Local Alignment Search Tool)
print("BLAST workflow:")
print("1. Input: query sequence")
print("2. Search: against database")
print("3. Output: similar sequences with scores")
print("\nBLAST types:")
print("- BLASTN: nucleotide vs nucleotide")
print("- BLASTP: protein vs protein")
print("- BLASTX: translated nucleotide vs protein")
```

**Output:**
```

BLAST workflow:
1. Input: query sequence
2. Search: against database
3. Output: similar sequences with scores

BLAST types:
- BLASTN: nucleotide vs nucleotide
- BLASTP: protein vs protein
- BLASTX: translated nucleotide vs protein
```

---

## 2. Cheminformatics Tools

### 2.1 RDKit

**RDKit** — библиотека для работы с химическими структурами.

**Пример: Работа с молекулами**

```python
# Химическая информатика с RDKit
# from rdkit import Chem
# from rdkit.Chem import Descriptors

# # Создание молекулы из SMILES
# mol = Chem.MolFromSmiles('CCO')  # Этанол
# 
# # Вычисление свойств
# mw = Descriptors.MolWt(mol)
# logp = Descriptors.MolLogP(mol)
# 
# print(f"Molecular weight: {mw:.2f}")
# print(f"LogP: {logp:.2f}")

print("RDKit provides:")
print("- Molecular representation (SMILES, InChI)")
print("- Molecular descriptors")
print("- Substructure searching")
print("- Reaction handling")
```

**Output:**
```

RDKit provides:
- Molecular representation (SMILES, InChI)
- Molecular descriptors
- Molecular descriptors
- Substructure searching
- Reaction handling
```

---

## 3. Scientific Workflows

### 3.1 Что такое Scientific Workflow

**Scientific Workflow** — автоматизированный процесс анализа данных.

**Компоненты workflow:**

- **Inputs** — входные данные

- **Steps** — шаги обработки

- **Outputs** — выходные данные

- **Dependencies** — зависимости между шагами

**Пример: Простой workflow**

```python
# Структура scientific workflow
workflow_steps = {
    'step1': {
        'name': 'Data loading',
        'input': 'raw_data.csv',
        'output': 'cleaned_data.csv',
        'tool': 'pandas'
    },
    'step2': {
        'name': 'Quality control',
        'input': 'cleaned_data.csv',
        'output': 'qc_report.html',
        'tool': 'custom_script',
        'depends_on': ['step1']
    },
    'step3': {
        'name': 'Analysis',
        'input': 'cleaned_data.csv',
        'output': 'results.csv',
        'tool': 'scipy',
        'depends_on': ['step1', 'step2']
    }
}

print("Workflow structure:")
for step_id, step in workflow_steps.items():
    print(f"\n{step_id}: {step['name']}")
    print(f"  Input: {step['input']}")
    print(f"  Output: {step['output']}")
    print(f"  Depends on: {step.get('depends_on', [])}")
```

**Output:**
```

Workflow structure:

step1: Data loading
  Input: raw_data.csv
  Output: cleaned_data.csv
  Depends on: []

step2: Quality control
  Input: cleaned_data.csv
  Output: qc_report.html
  Depends on: ['step1']

step3: Analysis
  Input: cleaned_data.csv
  Output: results.csv
  Depends on: ['step1', 'step2']
```

---

## 4. Workflow Managers

### 4.1 Snakemake

**Snakemake** — workflow management system на Python.

**Пример: Snakemake workflow**

```python
# Snakemake workflow (концепция)
snakemake_example = """
# Snakefile
rule all:
    input: "results/final_report.html"

rule clean_data:
    input: "data/raw.csv"
    output: "data/cleaned.csv"
    shell: "python scripts/clean.py {input} {output}"

rule analyze:
    input: "data/cleaned.csv"
    output: "results/analysis.csv"
    shell: "python scripts/analyze.py {input} {output}"

rule report:
    input: "results/analysis.csv"
    output: "results/final_report.html"
    shell: "python scripts/report.py {input} {output}"
"""

print("Snakemake features:")
print("- Python-based syntax")
print("- Automatic dependency resolution")
print("- Parallel execution")
print("- Reproducibility")
```

**Output:**
```

Snakemake features:
- Python-based syntax
- Automatic dependency resolution
- Parallel execution
- Reproducibility
```

### 4.2 Nextflow

**Nextflow** — workflow manager на основе DSL.

**Пример: Nextflow workflow**

```python
# Nextflow workflow (концепция)
nextflow_example = """
process cleanData {
    input:
    file raw from 'data/raw.csv'
    
    output:
    file cleaned into 'data/cleaned.csv'
    
    script:
    '''
    python scripts/clean.py $raw $cleaned
    '''
}

process analyze {
    input:
    file cleaned from 'data/cleaned.csv'
    
    output:
    file results into 'results/analysis.csv'
    
    script:
    '''
    python scripts/analyze.py $cleaned $results
    '''
}
"""

print("Nextflow features:")
print("- Domain-specific language (DSL)")
print("- Container support (Docker, Singularity)")
print("- Cloud execution")
print("- Dataflow programming")
```

**Output:**
```

Nextflow features:
- Domain-specific language (DSL)
- Container support (Docker, Singularity)
- Cloud execution
- Dataflow programming
```

### 4.3 Сравнение workflow managers

**Сравнение инструментов:**

| Инструмент | Язык | Особенности |
|------------|------|-------------|
| **Snakemake** | Python | Простой синтаксис, хорошая интеграция с Python |
| **Nextflow** | DSL | Контейнеры, облачные вычисления |
| **CWL** | YAML/JSON | Стандартизированный формат |
| **WDL** | DSL | Используется в облачных платформах |

**Пример: Выбор workflow manager**

```python

def choose_workflow_manager(requirements):
    """Выбор workflow manager на основе требований"""
    if requirements.get('python_heavy'):
        return "Snakemake (Python integration)"
    elif requirements.get('containers'):
        return "Nextflow (container support)"
    elif requirements.get('standardization'):
        return "CWL (standardized format)"
    else:
        return "Snakemake (general purpose)"

print("Workflow manager selection:")
print(f"Python-heavy: {choose_workflow_manager({'python_heavy': True})}")
print(f"Containers: {choose_workflow_manager({'containers': True})}")
```

**Output:**
```

Workflow manager selection:
Python-heavy: Snakemake (Python integration)
Containers: Nextflow (container support)
```

---

## 5. Интеграция инструментов

### 5.1 Объединение инструментов

**Пример: Интеграция различных инструментов**

```python
# Интеграция инструментов в pipeline
class ScientificPipeline:
    """Pipeline для интеграции инструментов"""
    
    def __init__(self):
        self.steps = []
    
    def add_step(self, name, tool, input_files, output_files):
        """Добавление шага в pipeline"""
        self.steps.append({
            'name': name,
            'tool': tool,
            'input': input_files,
            'output': output_files
        })
    
    def execute(self):
        """Выполнение pipeline"""
        results = {}
        for step in self.steps:
            print(f"Executing: {step['name']} with {step['tool']}")
            # Симуляция выполнения
            results[step['name']] = f"Output from {step['tool']}"
        return results

# Пример pipeline
pipeline = ScientificPipeline()
pipeline.add_step('load', 'pandas', ['raw.csv'], ['data.df'])
pipeline.add_step('analyze', 'scipy', ['data.df'], ['results.csv'])
pipeline.add_step('visualize', 'matplotlib', ['results.csv'], ['plot.png'])

results = pipeline.execute()
print(f"\nPipeline results: {results}")
```

**Output:**
```

Executing: load with pandas
Executing: analyze with scipy
Executing: visualize with matplotlib

Pipeline results: {'load': 'Output from pandas', 'analyze': 'Output from scipy', 'visualize': 'Output from matplotlib'}
```

### 5.2 Контейнеризация инструментов

**Docker/Singularity** для изоляции инструментов.

**Пример: Контейнеризация**

```python
# Концепция контейнеризации инструментов
print("Containerization benefits:")
print("- Reproducibility: same environment everywhere")
print("- Isolation: no conflicts between tools")
print("- Portability: run anywhere")
print("\nExample Dockerfile:")
print("FROM python:3.9")
print("RUN pip install biopython rdkit")
print("COPY scripts/ /app/")
print("WORKDIR /app")
```

**Output:**
```

Containerization benefits:
- Reproducibility: same environment everywhere
- Isolation: no conflicts between tools
- Portability: run anywhere

Example Dockerfile:
FROM python:3.9
RUN pip install biopython rdkit
COPY scripts/ /app/
WORKDIR /app
```

---

## 💡 Key Takeaways

- **Bioinformatics tools** (Biopython, BLAST) — для работы с биологическими данными

- **Cheminformatics tools** (RDKit) — для работы с химическими структурами

- **Scientific workflows** — автоматизированные процессы анализа данных

- **Workflow managers** (Snakemake, Nextflow) — управление сложными workflows

- **Интеграция инструментов** — объединение различных инструментов в единый pipeline

- **Контейнеризация** — обеспечение воспроизводимости и изоляции инструментов

---

## 🚀 Next Steps

**Related Modules:**

- [12_Troubleshooting](../12_Troubleshooting/) — troubleshooting pipelines
- [14_CustomSolutions](../14_CustomSolutions/) — разработка кастомных решений
- [07_Collaboration](../07_Collaboration/) — коллаборация в проектах

**Practice Ideas:**

1. Создайте простой workflow с Snakemake или Nextflow
2. Интегрируйте несколько инструментов в pipeline
3. Контейнеризуйте ваш workflow

**Going Deeper:**

- Изучите конкретные инструменты для вашей области (bio/chemo/geo)
- Познакомьтесь с продвинутыми возможностями workflow managers
- Изучите best practices для создания воспроизводимых workflows

---

## 📚 Additional Resources

**Documentation:**

- [Snakemake Documentation](https://snakemake.readthedocs.io/)
- [Nextflow Documentation](https://www.nextflow.io/docs/)
- [Biopython Tutorial](https://biopython.org/wiki/Documentation)

---


