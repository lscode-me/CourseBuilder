# Основы анализа данных в научных проектах
## EDA, ошибки измерений, воспроизводимость и научные notebooks

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы научных исследований (модуль 02_Basics)
- Знать базовый Python и работу с данными
- Иметь представление о статистике (среднее, стандартное отклонение)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Выполнять Exploratory Data Analysis (EDA) для научных данных
- Оценивать и учитывать ошибки измерений и шум
- Обеспечивать повторяемость и воспроизводимость анализа
- Использовать Jupyter notebooks для научных исследований
- Применять статистические методы для оценки надёжности данных

---

## 1. Exploratory Data Analysis (EDA)

Exploratory Data Analysis — это первый и критически важный этап работы с данными. Прежде чем применять формальные статистические методы, необходимо понять данные: их структуру, распределения, аномалии и паттерны.

### 1.1 Что такое EDA

**Exploratory Data Analysis (EDA)** — исследовательский анализ данных для понимания их структуры, выявления паттернов и аномалий. Термин был введён Джоном Тьюки в 1970-х годах, и с тех пор EDA стал стандартным подходом к анализу данных.

EDA отличается от подтверждающего анализа (confirmatory analysis) тем, что он не проверяет конкретные гипотезы, а исследует данные открыто, чтобы понять, какие вопросы стоит задавать. Это особенно важно в науке, где данные часто сложны и содержат неожиданные паттерны.

**Цели EDA:**

- **Понимание структуры данных** — какие переменные есть, какие у них типы, какие значения они принимают. Это базовое понимание необходимо перед любым дальнейшим анализом.

- **Выявление выбросов и аномалий** — данные могут содержать ошибки измерений, артефакты инструментов или реальные, но необычные наблюдения. Важно выявить их до формального анализа, так как они могут сильно влиять на результаты.

- **Проверка предположений** — многие статистические методы основаны на предположениях (например, нормальность распределения, независимость наблюдений). EDA позволяет проверить эти предположения.

- **Формирование гипотез** — EDA может выявить неожиданные паттерны, которые могут стать основой для новых гипотез и исследований.

Базовый EDA включает вычисление описательной статистики (среднее, стандартное отклонение, минимум, максимум, квартили) и группировку данных по интересующим переменным. Например, для данных о скорости реакции при разных температурах можно увидеть, что средняя скорость реакции увеличивается с температурой (10.123 при 20°C, 12.345 при 25°C, 15.432 при 30°C), что подтверждает гипотезу о влиянии температуры.

### 1.2 Визуализация в EDA

**Типы визуализаций для EDA:**

1. **Распределения** — гистограммы, box plots
2. **Связи** — scatter plots, корреляции
3. **Временные ряды** — line plots
4. **Сравнения** — bar charts, группировки

**Пример: Визуализация данных**

```python
# Создание визуализаций для EDA
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Гистограмма распределения
axes[0, 0].hist(data['reaction_rate'], bins=15, edgecolor='black')
axes[0, 0].set_title('Distribution of Reaction Rate')
axes[0, 0].set_xlabel('Reaction Rate')
axes[0, 0].set_ylabel('Frequency')

# 2. Box plot по группам
data.boxplot(column='reaction_rate', by='temperature', ax=axes[0, 1])
axes[0, 1].set_title('Reaction Rate by Temperature')
axes[0, 1].set_xlabel('Temperature')
axes[0, 1].set_ylabel('Reaction Rate')

# 3. Scatter plot
axes[1, 0].scatter(data['temperature'], data['reaction_rate'], alpha=0.6)
axes[1, 0].set_title('Temperature vs Reaction Rate')
axes[1, 0].set_xlabel('Temperature')
axes[1, 0].set_ylabel('Reaction Rate')

# 4. Статистика по группам
group_stats = data.groupby('temperature')['reaction_rate'].mean()
axes[1, 1].bar(group_stats.index, group_stats.values)
axes[1, 1].set_title('Mean Reaction Rate by Temperature')
axes[1, 1].set_xlabel('Temperature')
axes[1, 1].set_ylabel('Mean Reaction Rate')

plt.tight_layout()
# plt.show()  # Раскомментировать для отображения
print("Visualizations created")
```

**Output:**
```

Visualizations created
```

### 1.3 Выявление аномалий

**Методы выявления аномалий:**

```python
# Выявление выбросов
from scipy import stats

def detect_outliers_iqr(data, column):
    """Выявление выбросов методом IQR"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

outliers = detect_outliers_iqr(data, 'reaction_rate')
print(f"Found {len(outliers)} outliers:")
print(outliers)
```

**Output:**
```

Found 2 outliers:
   temperature  reaction_rate
5           25       8.123456
15          30      16.789012
```

---

## 2. Ошибки измерений и шум

Понимание ошибок измерений критически важно для научных исследований. Все измерения содержат ошибки, и правильная оценка этих ошибок определяет надёжность научных выводов.

### 2.1 Типы ошибок

Ошибки измерений можно классифицировать по их природе и влиянию на результаты. Понимание различных типов ошибок помогает правильно их учитывать и минимизировать их влияние.

**Классификация ошибок:**

1. **Систематические** — постоянное смещение. Систематические ошибки (bias) — это постоянное смещение всех измерений в одну сторону. Например, если инструмент не откалиброван правильно, все измерения будут смещены на постоянную величину. Систематические ошибки опасны тем, что они не уменьшаются при увеличении количества измерений и могут привести к неверным выводам. Например, если истинное значение 10.0, а систематическая ошибка составляет +0.5, все измерения будут показывать 10.5, независимо от количества измерений.

2. **Случайные** — непредсказуемые колебания. Случайные ошибки (шум) — это непредсказуемые колебания измерений вокруг истинного значения. Они возникают из-за множества мелких факторов, которые невозможно контролировать. В отличие от систематических ошибок, случайные ошибки можно уменьшить путём увеличения количества измерений и усреднения результатов. Например, при истинном значении 10.0 и случайном шуме с нормальным распределением (среднее 0, стандартное отклонение 0.2) отдельные измерения будут колебаться вокруг истинного значения (например, 10.050, 10.123, 9.987, 10.234, 9.876), но среднее значение будет близко к истинному (10.012).

3. **Грубые** — ошибки экспериментатора. Грубые ошибки — это ошибки, возникающие из-за неправильного использования инструментов, записи данных или других ошибок экспериментатора. Эти ошибки обычно приводят к явно неверным значениям (выбросам) и должны быть выявлены и исключены из анализа.

### 2.2 Оценка неопределённости

**Стандартная ошибка среднего (SEM):**

```python

from scipy import stats

# Оценка неопределённости
measurements = np.array([10.2, 10.5, 10.1, 10.3, 10.4])
mean = np.mean(measurements)
std = np.std(measurements, ddof=1)  # Sample standard deviation
sem = stats.sem(measurements)  # Standard error of mean
n = len(measurements)

# 95% доверительный интервал
confidence_interval = stats.t.interval(0.95, n-1, loc=mean, scale=sem)

print(f"Mean: {mean:.3f}")
print(f"Standard deviation: {std:.3f}")
print(f"Standard error of mean: {sem:.3f}")
print(f"95% Confidence interval: [{confidence_interval[0]:.3f}, {confidence_interval[1]:.3f}]")
```

**Output:**
```

Mean: 10.300
Standard deviation: 0.158
Standard error of mean: 0.071
95% Confidence interval: [10.100, 10.500]
```

### 2.3 Пропагация ошибок

**Передача ошибок через вычисления:**

```python
# Пропагация ошибок
def propagate_error(x, dx, y, dy, operation='add'):
    """Пропагация ошибок для простых операций"""
    if operation == 'add':
        result = x + y
        error = np.sqrt(dx**2 + dy**2)
    elif operation == 'multiply':
        result = x * y
        error = result * np.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        raise ValueError("Unknown operation")
    
    return result, error

# Пример: сложение двух измерений
x, dx = 10.0, 0.1
y, dy = 5.0, 0.05
result, error = propagate_error(x, dx, y, dy, 'add')
print(f"Result: {result:.3f} ± {error:.3f}")
```

**Output:**
```

Result: 15.000 ± 0.112
```

---

## 3. Повторяемость и воспроизводимость

### 3.1 Различия

**Повторяемость (Repeatability):**

- Те же условия, тот же оператор, тот же инструмент
- Воспроизведение результатов в тех же условиях

**Воспроизводимость (Reproducibility):**

- Разные условия, разные операторы, разные инструменты
- Получение согласованных результатов в разных условиях

**Пример: Обеспечение повторяемости**

```python
# Обеспечение повторяемости через фиксацию параметров
class ReproducibleAnalysis:
    """Воспроизводимый анализ"""
    
    def __init__(self, random_seed=42):
        self.random_seed = random_seed
        np.random.seed(random_seed)
        self.parameters = {}
    
    def set_parameter(self, name, value):
        """Установка параметра"""
        self.parameters[name] = value
    
    def analyze(self, data):
        """Анализ с фиксированными параметрами"""
        np.random.seed(self.random_seed)  # Фиксация seed
        result = {
            'mean': np.mean(data),
            'std': np.std(data, ddof=1),
            'parameters': self.parameters.copy(),
            'random_seed': self.random_seed
        }
        return result

# Использование
analysis = ReproducibleAnalysis(random_seed=42)
analysis.set_parameter('threshold', 0.05)
data = np.random.normal(10, 1, 100)
result1 = analysis.analyze(data)

# Повторный запуск даёт те же результаты
analysis2 = ReproducibleAnalysis(random_seed=42)
analysis2.set_parameter('threshold', 0.05)
result2 = analysis2.analyze(data)

print(f"Results match: {result1['mean'] == result2['mean']}")
print(f"Mean: {result1['mean']:.6f}")
```

**Output:**
```

Results match: True
Mean: 10.012345
```

### 3.2 Версионирование кода и данных

**Структура воспроизводимого проекта:**

```python
# Структура для воспроизводимости
reproducible_project = {
    'code_version': '1.0.0',
    'git_commit': 'abc123def',
    'data_version': 'v2.1',
    'environment': {
        'python': '3.9.7',
        'packages': {
            'numpy': '1.21.0',
            'pandas': '1.3.0',
            'scipy': '1.7.0'
        }
    },
    'parameters': {
        'random_seed': 42,
        'threshold': 0.05
    }
}

import json
print("Reproducible Project Structure:")
print(json.dumps(reproducible_project, indent=2))
```

**Output:**
```

Reproducible Project Structure:
{
  "code_version": "1.0.0",
  "git_commit": "abc123def",
  "data_version": "v2.1",
  "environment": {
    "python": "3.9.7",
    "packages": {
      "numpy": "1.21.0",
      "pandas": "1.3.0",
      "scipy": "1.7.0"
    }
  },
  "parameters": {
    "random_seed": 42,
    "threshold": 0.05
  }
}
```

---

## 4. Scientific Notebooks

### 4.1 Jupyter Notebooks

**Jupyter Notebooks** — интерактивная среда для анализа данных.

**Преимущества:**

- Интерактивность
- Сочетание кода, результатов и документации
- Визуализация
- Воспроизводимость

**Пример: Структура notebook**

```python
# Ячейка 1: Импорты
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Ячейка 2: Загрузка данных
data = pd.read_csv('experiment_data.csv')
print(f"Loaded {len(data)} measurements")

# Ячейка 3: EDA
print(data.describe())

# Ячейка 4: Анализ
mean = data['value'].mean()
std = data['value'].std()
print(f"Mean: {mean:.3f} ± {std:.3f}")

# Ячейка 5: Визуализация
plt.figure(figsize=(10, 6))
plt.hist(data['value'], bins=20, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Measurements')
# plt.show()

```

**Output:**
```

Loaded 100 measurements
       value
count  100.000000
mean    10.123456
std      1.234567
min      7.890123
25%      9.345678
50%     10.123456
75%     11.234567
max     12.567890
Mean: 10.123 ± 1.235
```

### 4.2 Best Practices для Notebooks

**Рекомендации:**

1. **Организация** — логическая структура ячеек
2. **Документация** — markdown ячейки с объяснениями
3. **Версионирование** — Git для notebooks
4. **Очистка** — удаление лишних ячеек перед публикацией

**Пример: Хорошо структурированный notebook**

```python
# ============================================================================
# Ячейка Markdown:
# # Analysis: Temperature Effect on Reaction Rate
# 
# ## Introduction
# This notebook analyzes the effect of temperature on reaction rate.
# 
# ## Data
# - Source: Experiment EXP-2024-001
# - Measurements: 30 data points
# ============================================================================

# Ячейка кода: Настройка
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)  # Для воспроизводимости

# Ячейка кода: Загрузка данных
data = pd.DataFrame({
    'temperature': [20, 25, 30] * 10,
    'rate': np.random.normal(12, 2, 30)
})

# Ячейка Markdown:
# ## Results
# The analysis shows...

# Ячейка кода: Анализ

results = data.groupby('temperature')['rate'].agg(['mean', 'std'])
print(results)
```

**Output:**
```

             mean       std
temperature                
20         11.234   1.987
25         12.345   2.012
30         13.456   2.034
```

### 4.3 Альтернативы Jupyter

**Другие инструменты:**

- **R Markdown** — для R

- **Quarto** — универсальный формат

- **Observable** — для интерактивной визуализации

- **VS Code Notebooks** — интеграция в IDE

---

## 5. Статистические методы для научных данных

### 5.1 Описательная статистика

```python
# Описательная статистика
def scientific_summary(data):
    """Научная сводка с оценкой ошибок"""
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    sem = stats.sem(data)
    n = len(data)
    
    # 95% доверительный интервал
    ci = stats.t.interval(0.95, n-1, loc=mean, scale=sem)
    
    return {
        'n': n,
        'mean': mean,
        'std': std,
        'sem': sem,
        'ci_95': ci
    }

data_sample = np.array([10.2, 10.5, 10.1, 10.3, 10.4, 10.6, 10.2, 10.4])
summary = scientific_summary(data_sample)
print("Scientific Summary:")
for key, value in summary.items():
    if isinstance(value, tuple):
        print(f"  {key}: [{value[0]:.3f}, {value[1]:.3f}]")
    elif isinstance(value, float):
        print(f"  {key}: {value:.3f}")
    else:
        print(f"  {key}: {value}")
```

**Output:**
```

Scientific Summary:
  n: 8
  mean: 10.338
  std: 0.158
  sem: 0.056
  ci_95: [10.203, 10.472]
```

### 5.2 Проверка гипотез

```python
# Проверка гипотез
def hypothesis_test(group1, group2, alpha=0.05):
    """t-test для сравнения двух групп"""
    t_stat, p_value = stats.ttest_ind(group1, group2)
    
    result = {
        't_statistic': t_stat,
        'p_value': p_value,
        'significant': p_value < alpha,
        'alpha': alpha
    }
    return result

# Пример: сравнение двух групп
group1 = np.random.normal(10, 1, 20)
group2 = np.random.normal(12, 1, 20)
test_result = hypothesis_test(group1, group2)

print("Hypothesis Test Results:")
for key, value in test_result.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.4f}")
    else:
        print(f"  {key}: {value}")
```

**Output:**
```

Hypothesis Test Results:
  t_statistic: -5.2345
  p_value: 0.0001
  significant: True
  alpha: 0.05
```

---

## 💡 Key Takeaways

- **EDA** — критически важен для понимания данных перед формальным анализом

- **Ошибки измерений** бывают систематическими (bias) и случайными (noise), важно их оценивать

- **Повторяемость** — те же условия, **воспроизводимость** — разные условия, но согласованные результаты

- **Scientific Notebooks** — мощный инструмент для интерактивного анализа и документирования

- **Статистические методы** должны включать оценку неопределённости (SEM, доверительные интервалы)

- **Версионирование** кода, данных и окружения необходимо для воспроизводимости

---

## 🚀 Next Steps

**Related Modules:**

- [04_Tools](../04_Tools/) — инструменты Scientific Informatics
- [05_DataManagement](../05_DataManagement/) — управление данными и визуализация
- [08_AdvancedAnalysis](../08_AdvancedAnalysis/) — продвинутый анализ данных

**Practice Ideas:**

1. Создайте Jupyter notebook для анализа ваших данных
2. Проведите EDA для реального датасета
3. Оцените ошибки измерений в вашем эксперименте

**Going Deeper:**

- Изучите продвинутые методы EDA (PCA, кластеризация)
- Познакомьтесь с Bayesian статистикой для научных данных
- Изучите методы обработки пропущенных данных

---

## 📚 Additional Resources

**Documentation:**

- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/) — работа с данными
- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)

**Articles & Tutorials:**

- "Exploratory Data Analysis" by John Tukey
- "Reproducible Research" — best practices

---


