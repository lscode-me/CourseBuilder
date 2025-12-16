# Управление данными и визуализация
## Форматы данных, хранение, версионирование и визуализация

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать основы работы с данными (модуль 02_Basics)
- Уметь работать с Python и Pandas (модуль 04_Tools)
- Понимать основы анализа данных (модуль 03_DataAnalysis)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с различными форматами научных данных (CSV, HDF5, NetCDF, FASTA, BAM)
- Организовывать хранение и версионирование данных
- Создавать эффективные визуализации научных данных
- Использовать Matplotlib, Seaborn и Plotly для визуализации
- Выбирать подходящий формат данных для конкретных задач

---

## 1. Форматы научных данных

### 1.1 Текстовые форматы

**CSV (Comma-Separated Values)** — простой текстовый формат для табличных данных.

**Пример: Работа с CSV**

```python

import pandas as pd
import numpy as np

# Создание данных
data = pd.DataFrame({
    'temperature': [20, 25, 30, 35, 40],
    'reaction_rate': [10.5, 12.3, 15.2, 18.1, 20.5],
    'pressure': [1.0, 1.0, 1.0, 1.0, 1.0]
})

# Сохранение в CSV
data.to_csv('experiment_data.csv', index=False)

# Загрузка из CSV
loaded_data = pd.read_csv('experiment_data.csv')
print("Loaded data:")
print(loaded_data)
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
```

**Преимущества CSV:**

- Человекочитаемый
- Универсальный (работает везде)
- Простой для обработки

**Недостатки CSV:**

- Неэффективен для больших данных
- Нет поддержки сложных типов данных
- Нет метаданных

### 1.2 Бинарные форматы для больших данных

**HDF5 (Hierarchical Data Format)** — эффективный формат для больших научных данных.

**Пример: Работа с HDF5**

```python

import h5py
import numpy as np

# Создание HDF5 файла
with h5py.File('experiment_data.h5', 'w') as f:
    # Создание группы
    group = f.create_group('experiment_001')
    
    # Сохранение данных
    group.create_dataset('temperature', data=np.array([20, 25, 30, 35, 40]))
    group.create_dataset('reaction_rate', data=np.array([10.5, 12.3, 15.2, 18.1, 20.5]))
    
    # Метаданные
    group.attrs['date'] = '2024-01-15'
    group.attrs['researcher'] = 'Dr. Smith'

# Чтение HDF5
with h5py.File('experiment_data.h5', 'r') as f:
    group = f['experiment_001']
    temp = group['temperature'][:]
    rate = group['reaction_rate'][:]
    date = group.attrs['date']
    
    print(f"Date: {date}")
    print(f"Temperature: {temp}")
    print(f"Reaction rate: {rate}")
```

**Output:**
```

Date: 2024-01-15
Temperature: [20 25 30 35 40]
Reaction rate: [10.5 12.3 15.2 18.1 20.5]
```

**Преимущества HDF5:**

- Эффективное хранение больших данных
- Поддержка метаданных
- Иерархическая структура
- Сжатие данных

### 1.3 Специализированные форматы

**NetCDF (Network Common Data Form)** — формат для геонаучных данных.

**Пример: Работа с NetCDF**

```python
# NetCDF для геопространственных данных
# from netCDF4 import Dataset
# 
# # Создание NetCDF файла
# nc = Dataset('climate_data.nc', 'w', format='NETCDF4')
# 
# # Создание измерений
# time = nc.createDimension('time', None)
# lat = nc.createDimension('lat', 10)
# lon = nc.createDimension('lon', 10)
# 
# # Создание переменных
# times = nc.createVariable('time', 'f8', ('time',))
# latitudes = nc.createVariable('lat', 'f4', ('lat',))
# longitudes = nc.createVariable('lon', 'f4', ('lon',))
# 
# # Данные о температуре
# temp = nc.createVariable('temperature', 'f4', ('time', 'lat', 'lon'))
# 
# # Заполнение данными
# latitudes[:] = np.linspace(-90, 90, 10)
# longitudes[:] = np.linspace(-180, 180, 10)
# 
# nc.close()

print("NetCDF используется для геопространственных данных (климат, океанография)")
```

**FASTA** — формат для биологических последовательностей.

**Пример: Работа с FASTA**

```python
# FASTA формат для ДНК/белковых последовательностей
fasta_content = """>seq1
ATGCGATCGATCGATCG
>seq2
GCTAGCTAGCTAGCTA
"""

# Парсинг FASTA
def parse_fasta(fasta_string):
    """Парсинг FASTA формата"""
    sequences = {}
    current_id = None
    current_seq = []
    
    for line in fasta_string.strip().split('\n'):
        if line.startswith('>'):
            if current_id:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:].strip()
            current_seq = []
        else:
            current_seq.append(line.strip())
    
    if current_id:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences

sequences = parse_fasta(fasta_content)
print("FASTA sequences:")
for seq_id, seq in sequences.items():
    print(f"{seq_id}: {seq[:20]}...")
```

**Output:**
```

FASTA sequences:
seq1: ATGCGATCGATCGATCG...
seq2: GCTAGCTAGCTAGCTA...
```

**BAM** — бинарный формат для выравниваний последовательностей.

```python
# BAM формат (требует pysam)
# import pysam
# 
# # Чтение BAM файла
# bamfile = pysam.AlignmentFile("alignment.bam", "rb")
# 
# for read in bamfile:
#     print(f"Read: {read.query_name}, Position: {read.reference_start}")
# 
# bamfile.close()

print("BAM используется для хранения выравниваний последовательностей")
```

---

## 2. Хранение и версионирование данных

### 2.1 Организация хранения

**Структура директорий для научных данных:**

```

data/
├── raw/              # Исходные данные
│   ├── experiment_001/
│   └── experiment_002/
├── processed/        # Обработанные данные
│   ├── v1.0/
│   └── v1.1/
├── derived/          # Производные данные
└── metadata/         # Метаданные
```

**Пример: Управление версиями данных**

```python

from pathlib import Path
import json
from datetime import datetime

class DataVersionManager:
    """Управление версиями научных данных"""
    
    def __init__(self, base_dir='data'):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
    
    def create_version(self, data_id, version, data, metadata=None):
        """Создание новой версии данных"""
        version_dir = self.base_dir / data_id / f"v{version}"
        version_dir.mkdir(parents=True, exist_ok=True)
        
        # Сохранение данных
        data_path = version_dir / 'data.csv'
        data.to_csv(data_path, index=False)
        
        # Сохранение метаданных
        if metadata:
            metadata['version'] = version
            metadata['created'] = datetime.now().isoformat()
            metadata_path = version_dir / 'metadata.json'
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
        
        return version_dir
    
    def get_version(self, data_id, version):
        """Получение конкретной версии данных"""
        version_dir = self.base_dir / data_id / f"v{version}"
        data_path = version_dir / 'data.csv'
        
        if data_path.exists():
            data = pd.read_csv(data_path)
            metadata_path = version_dir / 'metadata.json'
            metadata = {}
            if metadata_path.exists():
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
            return data, metadata
        return None, None

# Пример использования
manager = DataVersionManager('data')
data_v1 = pd.DataFrame({'value': [1, 2, 3]})
manager.create_version('exp001', '1.0', data_v1, {'researcher': 'Dr. Smith'})

data, meta = manager.get_version('exp001', '1.0')
print(f"Data: {data}")
print(f"Metadata: {meta}")
```

**Output:**
```

Data:    value
0      1
1      2
2      3
Metadata: {'researcher': 'Dr. Smith', 'version': '1.0', 'created': '2024-01-15T10:30:00.123456'}
```

### 2.2 Метаданные для версионирования

**Структура метаданных версии:**

```python

version_metadata = {
    'version': '1.0.0',
    'created': '2024-01-15T10:00:00',
    'creator': 'Dr. Smith',
    'changes': 'Initial data collection',
    'data_format': 'CSV',
    'size_bytes': 1024,
    'checksum': 'abc123def456',
    'dependencies': {
        'code_version': '1.0.0',
        'software': ['Python 3.9', 'Pandas 1.3.0']
    }
}

print("Version metadata structure:")
print(json.dumps(version_metadata, indent=2))
```

**Output:**
```

Version metadata structure:
{
  "version": "1.0.0",
  "created": "2024-01-15T10:00:00",
  "creator": "Dr. Smith",
  "changes": "Initial data collection",
  "data_format": "CSV",
  "size_bytes": 1024,
  "checksum": "abc123def456",
  "dependencies": {
    "code_version": "1.0.0",
    "software": ["Python 3.9", "Pandas 1.3.0"]
  }
}
```

---

## 3. Базовые методы визуализации

### 3.1 Matplotlib — основа визуализации

**Matplotlib** — библиотека для создания статических визуализаций.

**Пример: Базовые графики**

```python

import matplotlib.pyplot as plt
import numpy as np

# Данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', linewidth=2)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sine Wave')
plt.legend()
plt.grid(True, alpha=0.3)
# plt.show()

print("Matplotlib plot created")
```

**Output:**
```

Matplotlib plot created
```

**Пример: Scatter plot**

```python
# Scatter plot для научных данных
np.random.seed(42)
temperature = np.array([20, 25, 30, 35, 40])
reaction_rate = np.array([10.5, 12.3, 15.2, 18.1, 20.5])
error = np.random.normal(0, 0.5, len(temperature))

plt.figure(figsize=(10, 6))
plt.errorbar(temperature, reaction_rate, yerr=error, 
             fmt='o', capsize=5, capthick=2, label='Measurements')
plt.xlabel('Temperature (°C)')
plt.ylabel('Reaction Rate')
plt.title('Temperature vs Reaction Rate')
plt.legend()
plt.grid(True, alpha=0.3)
# plt.show()

print("Error bar plot created")
```

**Output:**
```

Error bar plot created
```

### 3.2 Seaborn — статистическая визуализация

**Seaborn** — библиотека для статистической визуализации на основе Matplotlib.

**Пример: Статистические графики**

```python

import seaborn as sns

# Настройка стиля
sns.set_style("whitegrid")

# Данные
data = pd.DataFrame({
    'temperature': np.repeat([20, 25, 30], 10),
    'reaction_rate': np.concatenate([
        np.random.normal(10, 1, 10),
        np.random.normal(12, 1, 10),
        np.random.normal(15, 1, 10)
    ])
})

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='temperature', y='reaction_rate')
plt.title('Reaction Rate Distribution by Temperature')
# plt.show()

print("Seaborn boxplot created")
```

**Output:**
```

Seaborn boxplot created
```

**Пример: Heatmap корреляций**

```python
# Корреляционная матрица
data_corr = pd.DataFrame({
    'temperature': np.random.normal(25, 5, 100),
    'pressure': np.random.normal(1.0, 0.1, 100),
    'reaction_rate': np.random.normal(12, 2, 100)
})

correlation_matrix = data_corr.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
# plt.show()

print("Correlation heatmap created")
```

**Output:**
```

Correlation heatmap created
```

### 3.3 Plotly — интерактивная визуализация

**Plotly** — библиотека для создания интерактивных визуализаций.

**Пример: Интерактивный график**

```python

import plotly.graph_objects as go
import plotly.express as px

# Интерактивный scatter plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=temperature,
    y=reaction_rate,
    mode='markers+lines',
    name='Reaction Rate',
    error_y=dict(type='data', array=error, visible=True)
))

fig.update_layout(
    title='Temperature vs Reaction Rate (Interactive)',
    xaxis_title='Temperature (°C)',
    yaxis_title='Reaction Rate',
    hovermode='closest'
)

# fig.show()

print("Plotly interactive plot created")
```

**Output:**
```

Plotly interactive plot created
```

**Пример: 3D визуализация**

```python
# 3D scatter plot
np.random.seed(42)
x = np.random.normal(25, 5, 50)
y = np.random.normal(1.0, 0.1, 50)
z = np.random.normal(12, 2, 50)

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=z,
        colorscale='Viridis',
        showscale=True
    )
)])

fig.update_layout(
    title='3D Scientific Data Visualization',
    scene=dict(
        xaxis_title='Temperature',
        yaxis_title='Pressure',
        zaxis_title='Reaction Rate'
    )
)

# fig.show()

print("3D plot created")
```

**Output:**
```

3D plot created
```

---

## 4. Выбор формата данных

### 4.1 Критерии выбора

**Матрица выбора формата:**

| Формат | Размер данных | Скорость | Метаданные | Использование |
|--------|---------------|----------|------------|---------------|
| **CSV** | Малый (<100MB) | Средняя | Нет | Простые таблицы |
| **HDF5** | Большой (GB+) | Высокая | Да | Большие массивы |
| **NetCDF** | Большой | Высокая | Да | Геоданные |
| **FASTA** | Средний | Средняя | Ограниченные | Последовательности |
| **BAM** | Большой | Высокая | Да | Выравнивания |

**Пример: Выбор формата**

```python

def choose_data_format(data_size_mb, has_metadata, data_type):
    """Выбор формата данных на основе характеристик"""
    if data_size_mb < 100 and not has_metadata:
        return "CSV"
    elif data_size_mb > 1000 and has_metadata:
        if data_type == "geospatial":
            return "NetCDF"
        else:
            return "HDF5"
    elif data_type == "sequence":
        return "FASTA"
    elif data_type == "alignment":
        return "BAM"
    else:
        return "HDF5"

# Примеры
print(f"Small table: {choose_data_format(50, False, 'table')}")
print(f"Large array: {choose_data_format(5000, True, 'array')}")
print(f"DNA sequence: {choose_data_format(200, False, 'sequence')}")
```

**Output:**
```

Small table: CSV
Large array: HDF5
DNA sequence: FASTA
```

---

## 5. Best Practices визуализации

### 5.1 Принципы научной визуализации

**Рекомендации:**

1. **Ясность** — график должен быть понятен без объяснений
2. **Точность** — масштабы и оси должны быть корректными
3. **Информативность** — показывать ошибки измерений
4. **Воспроизводимость** — код должен генерировать тот же график

**Пример: Правильная визуализация**

```python
# Правильная визуализация научных данных
fig, ax = plt.subplots(figsize=(10, 6))

# Данные с ошибками
x = np.array([20, 25, 30, 35, 40])
y = np.array([10.5, 12.3, 15.2, 18.1, 20.5])
yerr = np.array([0.5, 0.6, 0.7, 0.8, 0.9])

# График с error bars
ax.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, 
            capthick=2, linewidth=2, markersize=8,
            label='Experimental data')

# Подгонка кривой
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
ax.plot(x, p(x), '--', alpha=0.7, label=f'Linear fit: y={z[0]:.2f}x+{z[1]:.2f}')

# Оформление
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('Reaction Rate (units)', fontsize=12)
ax.set_title('Temperature Dependence of Reaction Rate', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# plt.show()

print("Scientific visualization created")
```

**Output:**
```

Scientific visualization created
```

### 5.2 Цветовые схемы

**Выбор цветов для научных графиков:**

```python
# Цветовые схемы для научных публикаций
scientific_colors = {
    'colorblind_friendly': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
    'grayscale': ['#000000', '#404040', '#808080', '#c0c0c0'],
    'viridis': 'viridis',  # Для heatmaps
    'plasma': 'plasma'     # Для heatmaps
}

# Пример использования
fig, ax = plt.subplots(figsize=(10, 6))
for i, color in enumerate(scientific_colors['colorblind_friendly']):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i)
    ax.plot(x, y, color=color, linewidth=2, label=f'Series {i+1}')

ax.legend()
ax.set_title('Colorblind-Friendly Color Scheme')
# plt.show()

print("Color scheme applied")
```

**Output:**
```

Color scheme applied
```

---

## 💡 Key Takeaways

- **Форматы данных** — выбор зависит от размера, типа данных и необходимости в метаданных

- **CSV** — для простых таблиц, **HDF5** — для больших массивов, **NetCDF** — для геоданных

- **Версионирование данных** — критически важно для воспроизводимости научных исследований

- **Визуализация** — Matplotlib (базовые), Seaborn (статистика), Plotly (интерактивные)

- **Научная визуализация** — должна показывать ошибки измерений, быть ясной и воспроизводимой

- **Метаданные** — необходимы для понимания и повторного использования данных

---

## 🚀 Next Steps

**Related Modules:**

- [06_DataIntegrity](../06_DataIntegrity/) — качество данных и безопасность
- [03_DataAnalysis](../03_DataAnalysis/) — основы анализа данных
- [09_LargeDatasets](../09_LargeDatasets/) — работа с большими датасетами

**Practice Ideas:**

1. Создайте структуру хранения для ваших данных с версионированием
2. Визуализируйте ваши экспериментальные данные с error bars
3. Сравните производительность CSV и HDF5 для ваших данных

**Going Deeper:**

- Изучите специализированные форматы для вашей области (FASTA, BAM, NetCDF)
- Познакомьтесь с DVC (Data Version Control) для управления версиями данных
- Изучите продвинутые техники визуализации (subplots, animations)

---

## 📚 Additional Resources

**Documentation:**

- [HDF5 Documentation](https://www.hdfgroup.org/solutions/hdf5/)
- [NetCDF Documentation](https://www.unidata.ucar.edu/software/netcdf/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Plotly Documentation](https://plotly.com/python/)

**Tutorials:**

- "Effective Data Visualization" — принципы научной визуализации
- "HDF5 for Python" — работа с HDF5

---


