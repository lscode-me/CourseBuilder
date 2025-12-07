# Домашнее задание: Эпигенетика и Генетические Маркеры

## Задание 1: Анализ метилирования (25 баллов)

Напишите функцию для анализа данных метилирования и определения статуса гена.

```python
def analyze_gene_methylation(methylation_data: list[dict]) -> dict:
    """
    Анализ метилирования промоторной области гена.
    
    Args:
        methylation_data: список словарей с полями:
            - position: позиция CpG сайта
            - beta_value: уровень метилирования (0.0 - 1.0)
    
    Returns:
        dict с полями:
            - avg_methylation: средний уровень метилирования
            - status: "hypermethylated", "hypomethylated", или "intermediate"
            - cpg_count: количество CpG сайтов
            - likely_expression: "silenced", "active", или "variable"
    
    Критерии:
        - hypermethylated: avg > 0.7
        - hypomethylated: avg < 0.3
        - intermediate: 0.3 <= avg <= 0.7
    """
    pass

# Тест
test_data = [
    {"position": 1000, "beta_value": 0.85},
    {"position": 1020, "beta_value": 0.78},
    {"position": 1045, "beta_value": 0.92},
    {"position": 1060, "beta_value": 0.81},
]

result = analyze_gene_methylation(test_data)
# Ожидаемый результат:
# {
#     "avg_methylation": 0.84,
#     "status": "hypermethylated",
#     "cpg_count": 4,
#     "likely_expression": "silenced"
# }
```

## Задание 2: Интерпретация гистоновых меток (20 баллов)

Реализуйте функцию для интерпретации комбинации гистоновых модификаций.

```python
def interpret_chromatin_state(histone_marks: list[str]) -> dict:
    """
    Определение состояния хроматина по набору гистоновых меток.
    
    Args:
        histone_marks: список гистоновых модификаций
            Примеры: "H3K4me3", "H3K27ac", "H3K9me3", "H3K27me3"
    
    Returns:
        dict с полями:
            - state: "active_promoter", "active_enhancer", "repressed", 
                     "bivalent", или "unknown"
            - confidence: "high", "medium", или "low"
            - description: текстовое описание
    
    Правила:
        - H3K4me3 + H3K27ac = active_promoter
        - H3K27ac без H3K4me3 = active_enhancer  
        - H3K9me3 или H3K27me3 (без активных) = repressed
        - H3K4me3 + H3K27me3 = bivalent (готов к активации или репрессии)
    """
    pass

# Тесты
print(interpret_chromatin_state(["H3K4me3", "H3K27ac"]))
# {"state": "active_promoter", "confidence": "high", ...}

print(interpret_chromatin_state(["H3K4me3", "H3K27me3"]))
# {"state": "bivalent", "confidence": "high", ...}
```

## Задание 3: GWAS анализ (30 баллов)

Реализуйте упрощённый GWAS анализ с визуализацией.

```python
import numpy as np
from scipy import stats

def perform_gwas(genotypes: np.ndarray, 
                 phenotypes: np.ndarray, 
                 snp_info: list[dict]) -> list[dict]:
    """
    Выполнение GWAS анализа.
    
    Args:
        genotypes: матрица (n_samples × n_snps), значения 0, 1, 2
        phenotypes: вектор (n_samples,), 0 = контроль, 1 = случай
        snp_info: список словарей с полями:
            - rsid: ID маркера
            - chromosome: номер хромосомы
            - position: позиция
    
    Returns:
        список словарей с полями:
            - rsid: ID маркера
            - chromosome: хромосома
            - position: позиция
            - p_value: p-value теста
            - odds_ratio: отношение шансов
            - significant: True если p < 5e-8
    """
    pass

def create_manhattan_plot(gwas_results: list[dict], output_file: str):
    """
    Создание Manhattan plot.
    
    Args:
        gwas_results: результаты perform_gwas
        output_file: путь для сохранения графика
    """
    pass

# Генерация тестовых данных
np.random.seed(42)
n_samples = 1000
n_snps = 100

genotypes = np.random.randint(0, 3, size=(n_samples, n_snps))
phenotypes = np.random.randint(0, 2, size=n_samples)

# Добавляем "настоящий" сигнал в SNP 50
causal_effect = genotypes[:, 50]
phenotypes = (np.random.random(n_samples) < 0.3 + 0.3 * causal_effect).astype(int)

snp_info = [
    {"rsid": f"rs{i}", "chromosome": (i % 22) + 1, "position": i * 1000000}
    for i in range(n_snps)
]

results = perform_gwas(genotypes, phenotypes, snp_info)
```

## Задание 4: Фармакогенетика (15 баллов)

Создайте систему рекомендаций по дозированию лекарств.

```python
def get_drug_recommendations(patient_genotypes: dict) -> list[dict]:
    """
    Генерация фармакогенетических рекомендаций.
    
    Args:
        patient_genotypes: словарь {rsid: genotype}
            Примеры:
            - rs9923231 (VKORC1): "GG", "GA", "AA"
            - rs1057910 (CYP2C9*3): "AA", "AC", "CC"
            - rs4244285 (CYP2C19*2): "GG", "GA", "AA"
    
    Returns:
        список рекомендаций с полями:
            - drug: название препарата
            - gene: ген
            - genotype: генотип пациента
            - metabolizer_status: статус метаболизма
            - recommendation: рекомендация по дозе
            - evidence_level: уровень доказательности ("1A", "1B", "2A", etc.)
    """
    pass

# Тест
patient = {
    "rs9923231": "AA",      # VKORC1 - чувствительность к варфарину
    "rs4244285": "GA",      # CYP2C19*2 - промежуточный метаболизм
}

recommendations = get_drug_recommendations(patient)
for rec in recommendations:
    print(f"{rec['drug']}: {rec['recommendation']}")
```

## Задание 5: STR-профилирование (10 баллов)

Реализуйте сравнение STR-профилей для установления родства.

```python
def compare_str_profiles(profile1: dict, 
                         profile2: dict,
                         relationship: str = "parent-child") -> dict:
    """
    Сравнение STR-профилей для установления родства.
    
    Args:
        profile1, profile2: словари {locus: (allele1, allele2)}
        relationship: тип родства для проверки
            - "parent-child": один аллель должен быть общим
            - "siblings": минимум один аллель общий (вероятностно)
            - "identical": все аллели совпадают
    
    Returns:
        dict с полями:
            - compatible: True/False - совместимо ли с родством
            - shared_alleles: количество общих аллелей по локусам
            - likelihood_ratio: отношение правдоподобия
            - conclusion: текстовый вывод
    """
    pass

# Тест: проверка отцовства
child = {
    "D3S1358": (15, 17),
    "D13S317": (8, 12),
    "D7S820": (10, 11),
}

alleged_father = {
    "D3S1358": (15, 16),   # Может передать 15
    "D13S317": (8, 9),     # Может передать 8
    "D7S820": (11, 12),    # Может передать 11
}

result = compare_str_profiles(child, alleged_father, "parent-child")
print(f"Совместимо с отцовством: {result['compatible']}")
```

---

## Критерии оценки

| Задание | Баллы | Критерии |
|---------|-------|----------|
| Задание 1 | 25 | Корректный расчёт, правильная классификация |
| Задание 2 | 20 | Правильная логика, обработка комбинаций |
| Задание 3 | 30 | Корректный статистический тест, визуализация |
| Задание 4 | 15 | Полнота базы данных, корректные рекомендации |
| Задание 5 | 10 | Правильная логика сравнения |

**Итого: 100 баллов**

---

## Бонусные задания

### Бонус 1: Эпигенетические часы (10 баллов)

Реализуйте упрощённую модель эпигенетических часов Horvath.

### Бонус 2: CNV детекция (10 баллов)

Напишите алгоритм обнаружения CNV по данным глубины покрытия.

### Бонус 3: Полигенный риск (15 баллов)

Реализуйте расчёт полигенного риска (PRS) на основе GWAS данных.



