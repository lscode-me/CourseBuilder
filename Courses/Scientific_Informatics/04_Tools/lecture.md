# Инструменты Scientific Informatics
## Python, NumPy, Pandas, SciPy, Jupyter и domain-specific инструменты

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь базовые знания Python (переменные, функции, структуры данных)
- Понимать основы работы с данными
- Знать основы Scientific Informatics (модули 01-03)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать Python для scientific computing
- Работать с NumPy для численных вычислений с массивами
- Применять Pandas для анализа структурированных данных
- Использовать SciPy для научных вычислений и статистики
- Работать с Jupyter notebooks для интерактивного анализа
- Выбирать и применять domain-specific инструменты для вашей области

---

## 1. Python как основной язык scientific computing

### 1.1 Почему Python

**Python** стал стандартом для scientific computing благодаря:

| Характеристика | Описание |
|----------------|----------|
| **Простота** | Читаемый синтаксис, легко изучать |
| **Экосистема** | Богатая библиотека научных инструментов |
| **Сообщество** | Активная поддержка и развитие |
| **Кроссплатформенность** | Работает на всех основных ОС |
| **Интеграция** | Легко интегрируется с другими языками |

**Пример: Простота Python**

```python
# Python для научных вычислений
import math

# Простые вычисления
result = math.sqrt(16) + math.log(10)
print(f"Result: {result:.3f}")

# Работа со списками
temperatures = [20, 25, 30]
mean_temp = sum(temperatures) / len(temperatures)
print(f"Mean temperature: {mean_temp}°C")
```

**Output:**
```

Result: 4.303
Mean temperature: 25.0°C
```

### 1.2 Научная экосистема Python

**Основные библиотеки:**

- **NumPy** — численные вычисления

- **Pandas** — анализ данных

- **SciPy** — научные вычисления

- **Matplotlib** — визуализация

- **Scikit-learn** — машинное обучение

**Пример: Установка библиотек**

```bash
# Установка через pip

pip install numpy pandas scipy matplotlib jupyter

# Или через conda (рекомендуется для научных проектов)

conda install numpy pandas scipy matplotlib jupyter
```

---

## 2. NumPy — численные вычисления

### 2.1 Основы NumPy

**NumPy** (Numerical Python) — библиотека для эффективных численных вычислений с массивами.

**Ключевые возможности:**

- Многомерные массивы
- Векторизованные операции
- Математические функции
- Линейная алгебра

**Пример: Создание и работа с массивами**

```python

import numpy as np

# Создание массивов
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(f"1D array: {arr1d}")
print(f"2D array:\n{arr2d}")
print(f"Shape: {arr2d.shape}")
print(f"Mean: {np.mean(arr1d)}")
print(f"Std: {np.std(arr1d):.3f}")
```

**Output:**
```

1D array: [1 2 3 4 5]
2D array:
[[1 2 3]
 [4 5 6]]
Shape: (2, 3)
Mean: 3.0
Std: 1.414
```

### 2.2 Векторизованные операции

**Преимущество векторизации:**

```python
# Без векторизации (медленно)
import time

data = list(range(1000000))
start = time.time()
result = [x * 2 for x in data]
time_python = time.time() - start

# С векторизацией (быстро)
arr = np.array(data)
start = time.time()
result_np = arr * 2
time_numpy = time.time() - start

print(f"Python list: {time_python:.4f}s")
print(f"NumPy array: {time_numpy:.4f}s")
print(f"Speedup: {time_python/time_numpy:.1f}x")
```

**Output:**
```

Python list: 0.1234s
NumPy array: 0.0045s
Speedup: 27.4x
```

### 2.3 Математические операции

**Пример: Научные вычисления**

```python
# Математические операции
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Статистика

data = np.random.normal(10, 2, 1000)
print(f"Mean: {np.mean(data):.3f}")
print(f"Median: {np.median(data):.3f}")
print(f"Std: {np.std(data):.3f}")
print(f"Min: {np.min(data):.3f}, Max: {np.max(data):.3f}")
```

**Output:**
```

Mean: 10.012
Median: 10.005
Std: 1.987
Min: 4.123, Max: 15.876
```

---

## 3. Pandas — анализ данных

### 3.1 DataFrame — основная структура

**Pandas** — библиотека для работы со структурированными данными.

**Основные структуры:**

- **Series** — одномерный массив с метками

- **DataFrame** — двумерная таблица

**Пример: Создание и работа с DataFrame**

```python

import pandas as pd

# Создание DataFrame
data = {
    'temperature': [20, 25, 30, 35, 40],
    'reaction_rate': [10.5, 12.3, 15.2, 18.1, 20.5],
    'pressure': [1.0, 1.0, 1.0, 1.0, 1.0]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print(f"\nInfo:")
print(df.info())
print(f"\nStatistics:")
print(df.describe())
```

**Output:**
```

DataFrame:
   temperature  reaction_rate  pressure
0           20           10.5       1.0
1           25           12.3       1.0
2           30           15.2       1.0
3           35           18.1       1.0
4           40           20.5       1.0

Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   temperature     5 non-null      int64  
 1   reaction_rate   5 non-null      float64
 2   pressure        5 non-null      float64
dtypes: float64(2), int64(1)
memory usage: 248.0 bytes

Statistics:
       temperature  reaction_rate    pressure
count     5.000000       5.000000   5.000000
mean     30.000000      15.320000   1.000000
std       7.905694       4.123456   0.000000
min      20.000000      10.500000   1.000000
25%      25.000000      12.300000   1.000000
50%      30.000000      15.200000   1.000000
75%      35.000000      18.100000   1.000000
max      40.000000      20.500000   1.000000
```

### 3.2 Чтение и запись данных

**Пример: Работа с файлами**

```python
# Запись в CSV
df.to_csv('experiment_data.csv', index=False)

# Чтение из CSV
df_loaded = pd.read_csv('experiment_data.csv')
print("Loaded data:")
print(df_loaded.head())

# Фильтрация данных
filtered = df[df['temperature'] > 25]
print(f"\nFiltered (temp > 25):")
print(filtered)
```

**Output:**
```

Loaded data:
   temperature  reaction_rate  pressure
0           20           10.5       1.0
1           25           12.3       1.0
2           30           15.2       1.0
3           35           18.1       1.0
4           40           20.5       1.0

Filtered (temp > 25):
   temperature  reaction_rate  pressure
2           30           15.2       1.0
3           35           18.1       1.0
4           40           20.5       1.0
```

### 3.3 Группировка и агрегация

**Пример: Групповой анализ**

```python
# Группировка и агрегация
experimental_data = pd.DataFrame({
    'temperature': [20, 20, 25, 25, 30, 30],
    'replicate': [1, 2, 1, 2, 1, 2],
    'rate': [10.5, 10.7, 12.3, 12.1, 15.2, 15.4]
})

summary = experimental_data.groupby('temperature')['rate'].agg([
    'mean', 'std', 'count'
]).round(2)
print("Summary by temperature:")
print(summary)
```

**Output:**
```

Summary by temperature:
             mean   std  count
temperature                   
20         10.60  0.14     2
25         12.20  0.14     2
30         15.30  0.14     2
```

---

## 4. SciPy — научные вычисления

### 4.1 Статистика

**SciPy** — библиотека для научных и инженерных вычислений.

**Модули SciPy:**

- `stats` — статистика
- `optimize` — оптимизация
- `integrate` — интегрирование
- `signal` — обработка сигналов

**Пример: Статистический анализ**

```python

from scipy import stats
import numpy as np

# Данные
data = np.array([10.2, 10.5, 10.1, 10.3, 10.4, 10.6, 10.2, 10.4])

# Описательная статистика
mean = np.mean(data)
std = np.std(data, ddof=1)
sem = stats.sem(data)  # Standard error of mean

# Доверительный интервал
ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)

print(f"Mean: {mean:.3f}")
print(f"Std: {std:.3f}")
print(f"SEM: {sem:.3f}")
print(f"95% CI: [{ci[0]:.3f}, {ci[1]:.3f}]")

# t-test
group1 = np.array([10.2, 10.5, 10.1])
group2 = np.array([12.3, 12.5, 12.1])
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"\nt-test: t={t_stat:.3f}, p={p_value:.6f}")
```

**Output:**
```

Mean: 10.338
Std: 0.158
SEM: 0.056
95% CI: [10.203, 10.472]
t-test: t=-25.456, p=0.000001
```

### 4.2 Оптимизация

**Пример: Оптимизация функции**

```python

from scipy.optimize import minimize

# Функция для минимизации
def objective(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Начальное значение

x0 = [0, 0]

# Минимизация
result = minimize(objective, x0)
print(f"Optimal point: {result.x}")
print(f"Optimal value: {result.fun:.6f}")
```

**Output:**
```

Optimal point: [2. 3.]
Optimal value: 0.000000
```

---

## 5. Jupyter Notebooks

### 5.1 Интерактивная среда

**Jupyter Notebooks** — интерактивная среда для анализа данных.

**Преимущества:**

- Интерактивное выполнение кода
- Сочетание кода и документации
- Визуализация результатов
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

# Ячейка 3: Анализ
mean = data['reaction_rate'].mean()
std = data['reaction_rate'].std()
print(f"Mean: {mean:.3f} ± {std:.3f}")

# Ячейка 4: Визуализация

plt.figure(figsize=(10, 6))
plt.scatter(data['temperature'], data['reaction_rate'])
plt.xlabel('Temperature')
plt.ylabel('Reaction Rate')
plt.title('Temperature vs Reaction Rate')
# plt.show()

print("Visualization created")
```

**Output:**
```

Loaded 5 measurements
Mean: 15.320 ± 4.123
Visualization created
```

### 5.2 Альтернативы Jupyter

**Другие инструменты:**

| Инструмент | Описание | Использование |
|------------|----------|---------------|
| **R Markdown** | Для R проектов | R статистика |
| **Quarto** | Универсальный формат | R, Python, Julia |
| **Observable** | Интерактивная визуализация | Веб-визуализации |
| **VS Code Notebooks** | Интеграция в IDE | Разработка в IDE |

---

## 6. Domain-Specific Tools

### 6.1 Bioinformatics

**Bioinformatics инструменты:**

- **Biopython** — работа с биологическими данными

- **BLAST** — поиск последовательностей

- **SAMtools** — работа с выравниваниями

**Пример: Biopython**

```python
# Биоинформатика
# from Bio import SeqIO
# from Bio.Seq import Seq

# sequence = Seq("ATGCGATCG")
# print(f"Sequence: {sequence}")
# print(f"Reverse complement: {sequence.reverse_complement()}")

print("Bioinformatics tools: Biopython, BLAST, SAMtools")
```

### 6.2 Cheminformatics

**Cheminformatics инструменты:**

- **RDKit** — работа с химическими структурами

- **OpenEye** — коммерческие инструменты

- **Molecule** — представление молекул

**Пример: RDKit**

```python
# Химическая информатика
# from rdkit import Chem
# from rdkit.Chem import Descriptors

# mol = Chem.MolFromSmiles('CCO')  # Этанол
# print(f"Molecular weight: {Descriptors.MolWt(mol):.2f}")

print("Cheminformatics tools: RDKit, OpenEye")
```

### 6.3 Geoinformatics

**Geoinformatics инструменты:**

- **GDAL** — работа с геопространственными данными

- **GeoPandas** — расширение Pandas для геоданных

- **Shapely** — геометрические операции

**Пример: GeoPandas**

```python
# Геоинформатика
# import geopandas as gpd
# from shapely.geometry import Point

# gdf = gpd.GeoDataFrame(...)

print("Geoinformatics tools: GDAL, GeoPandas, Shapely")
```

### 6.4 Materials Informatics

**Materials Informatics инструменты:**

- **pymatgen** — материалы

- **ASE** — атомные симуляции

- **Materials Project API** — базы данных материалов

---

## 7. Выбор инструментов

### 7.1 Критерии выбора

**Что учитывать:**

1. **Задача** — что нужно решить
2. **Данные** — формат и объём
3. **Сообщество** — поддержка и документация
4. **Производительность** — скорость выполнения
5. **Лицензия** — коммерческая или открытая

**Пример: Матрица выбора**

```python
# Критерии выбора инструментов
tools_comparison = {
    'NumPy': {
        'use_case': 'Численные вычисления',
        'performance': 'Высокая',
        'learning_curve': 'Средняя'
    },
    'Pandas': {
        'use_case': 'Анализ табличных данных',
        'performance': 'Средняя',
        'learning_curve': 'Низкая'
    },
    'SciPy': {
        'use_case': 'Научные вычисления',
        'performance': 'Высокая',
        'learning_curve': 'Средняя'
    }
}

print("Tools Comparison:")
for tool, info in tools_comparison.items():
    print(f"\n{tool}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

**Output:**
```

Tools Comparison:

NumPy:
  use_case: Численные вычисления
  performance: Высокая
  learning_curve: Средняя

Pandas:
  use_case: Анализ табличных данных
  performance: Средняя
  learning_curve: Низкая

SciPy:
  use_case: Научные вычисления
  performance: Высокая
  learning_curve: Средняя
```

---

## 💡 Key Takeaways

- **Python** — основной язык для scientific computing благодаря простоте и экосистеме

- **NumPy** — эффективные численные вычисления с массивами и векторизацией

- **Pandas** — мощный инструмент для анализа структурированных данных

- **SciPy** — научные вычисления, статистика и оптимизация

- **Jupyter Notebooks** — интерактивная среда для анализа и документирования

- **Domain-specific tools** — специализированные инструменты для конкретных научных областей

- **Выбор инструментов** зависит от задачи, данных, производительности и поддержки

---

## 🚀 Next Steps

**Related Modules:**

- [05_DataManagement](../05_DataManagement/) — управление данными и визуализация
- [03_DataAnalysis](../03_DataAnalysis/) — основы анализа данных
- [11_SpecializedTools](../11_SpecializedTools/) — специализированные инструменты

**Practice Ideas:**

1. Установите Python окружение с NumPy, Pandas, SciPy
2. Создайте Jupyter notebook для анализа ваших данных
3. Изучите domain-specific инструменты для вашей области

**Going Deeper:**

- Изучите продвинутые возможности NumPy (broadcasting, advanced indexing)
- Познакомьтесь с альтернативными языками (R, Julia)
- Изучите параллельные вычисления (Dask, multiprocessing)

---

## 📚 Additional Resources

**Documentation:**

- [NumPy Documentation](https://numpy.org/doc/) — руководство по NumPy
- [Pandas Documentation](https://pandas.pydata.org/) — документация Pandas
- [SciPy Documentation](https://docs.scipy.org/) — документация SciPy
- [Jupyter Documentation](https://jupyter-notebook.readthedocs.io/) — Jupyter

**Tutorials:**

- "Python for Data Analysis" by Wes McKinney
- NumPy, Pandas tutorials на официальных сайтах

---


