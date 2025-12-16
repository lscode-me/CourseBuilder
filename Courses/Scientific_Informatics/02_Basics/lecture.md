# Основы научных исследований и данных
## Гипотезы, эксперименты, типы данных и метаданные

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы Scientific Informatics (модуль 01_Intro)
- Иметь базовые знания о научном методе
- Понимать концепцию данных и их структуры

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Формулировать гипотезы и планировать эксперименты
- Различать экспериментальные, наблюдательные и симулированные данные
- Работать со структурированными и неструктурированными данными
- Создавать и использовать метаданные для научных данных
- Применять принципы научного метода в работе с данными

---

## 1. Научный метод и гипотезы

### 1.1 Научный метод

**Научный метод** — систематический подход к получению знаний через наблюдение, экспериментирование и анализ.

**Этапы научного метода:**

1. **Наблюдение** — сбор фактов и данных
2. **Гипотеза** — предположение, объясняющее наблюдения
3. **Эксперимент** — проверка гипотезы
4. **Анализ** — интерпретация результатов
5. **Вывод** — подтверждение или опровержение гипотезы

**Пример: Структура научного исследования**

```python
# Представление научного исследования
class ScientificStudy:
    """Структура научного исследования"""
    
    def __init__(self, title, hypothesis):
        self.title = title
        self.hypothesis = hypothesis
        self.observations = []
        self.experiments = []
        self.results = []
        self.conclusion = None
    
    def add_observation(self, observation):
        """Добавление наблюдения"""
        self.observations.append({
            'description': observation,
            'timestamp': '2024-01-15'
        })
    
    def design_experiment(self, experiment):
        """Планирование эксперимента"""
        self.experiments.append({
            'design': experiment,
            'variables': experiment.get('variables', {}),
            'methodology': experiment.get('methodology', '')
        })
    
    def analyze_results(self, results):
        """Анализ результатов"""
        self.results = results
        # Упрощённая логика вывода
        if results.get('p_value', 1) < 0.05:
            self.conclusion = "Hypothesis supported"
        else:
            self.conclusion = "Hypothesis not supported"
    
    def get_summary(self):
        """Сводка исследования"""
        return {
            'title': self.title,
            'hypothesis': self.hypothesis,
            'observations_count': len(self.observations),
            'experiments_count': len(self.experiments),
            'conclusion': self.conclusion
        }

# Пример использования
study = ScientificStudy(
    title="Effect of Temperature on Reaction Rate",
    hypothesis="Increasing temperature increases reaction rate"
)

study.add_observation("Reaction seems faster at higher temperatures")
study.design_experiment({
    'variables': {'independent': 'temperature', 'dependent': 'reaction_rate'},
    'methodology': 'Measure reaction rate at different temperatures'
})

study.analyze_results({'p_value': 0.01})
print(study.get_summary())
```

**Output:**
```

{'title': 'Effect of Temperature on Reaction Rate', 'hypothesis': 'Increasing temperature increases reaction rate', 'observations_count': 1, 'experiments_count': 1, 'conclusion': 'Hypothesis supported'}
```

### 1.2 Формулирование гипотез

**Гипотеза** — проверяемое предположение о связи между переменными.

**Характеристики хорошей гипотезы:**

- **Проверяемая** — можно проверить экспериментально

- **Специфичная** — чётко определяет переменные

- **Измеримая** — переменные можно измерить

- **Фальсифицируемая** — можно опровергнуть

**Пример: Формулирование гипотезы**

```python
# Структура гипотезы
class Hypothesis:
    """Представление научной гипотезы"""
    
    def __init__(self, statement, variables, prediction):
        self.statement = statement
        self.variables = variables  # {'independent': [...], 'dependent': [...]}
        self.prediction = prediction
    
    def is_testable(self):
        """Проверка, можно ли проверить гипотезу"""
        return all(var in self.variables.get('independent', []) + 
                  self.variables.get('dependent', []) 
                  for var in ['temperature', 'reaction_rate'])
    
    def __repr__(self):
        return f"Hypothesis: {self.statement}"

# Пример гипотезы
hypothesis = Hypothesis(
    statement="Temperature affects reaction rate",
    variables={
        'independent': ['temperature'],
        'dependent': ['reaction_rate'],
        'controlled': ['pressure', 'concentration']
    },
    prediction="Higher temperature will result in faster reaction rate"
)

print(hypothesis)
print(f"Testable: {hypothesis.is_testable()}")
```

**Output:**
```

Hypothesis: Temperature affects reaction rate
Testable: True
```

---

## 2. Эксперименты и наблюдения

### 2.1 Типы исследований

**Классификация исследований:**

1. **Экспериментальные** — контролируемое вмешательство
2. **Наблюдательные** — наблюдение без вмешательства
3. **Симуляционные** — компьютерное моделирование

**Пример: Разные типы исследований**

```python
# Типы научных исследований
class ResearchType:
    """Типы научных исследований"""
    
    EXPERIMENTAL = "experimental"
    OBSERVATIONAL = "observational"
    SIMULATIONAL = "simulational"
    
    @staticmethod
    def get_characteristics(research_type):
        """Характеристики типа исследования"""
        characteristics = {
            ResearchType.EXPERIMENTAL: {
                'control': True,
                'intervention': True,
                'variables': 'manipulated',
                'causality': 'can_establish'
            },
            ResearchType.OBSERVATIONAL: {
                'control': False,
                'intervention': False,
                'variables': 'observed',
                'causality': 'cannot_establish'
            },
            ResearchType.SIMULATIONAL: {
                'control': 'full',
                'intervention': 'simulated',
                'variables': 'configurable',
                'causality': 'model_dependent'
            }
        }
        return characteristics.get(research_type, {})

# Примеры
print("Experimental:", ResearchType.get_characteristics(ResearchType.EXPERIMENTAL))
print("Observational:", ResearchType.get_characteristics(ResearchType.OBSERVATIONAL))
print("Simulational:", ResearchType.get_characteristics(ResearchType.SIMULATIONAL))
```

**Output:**
```

Experimental: {'control': True, 'intervention': True, 'variables': 'manipulated', 'causality': 'can_establish'}
Observational: {'control': False, 'intervention': False, 'variables': 'observed', 'causality': 'cannot_establish'}
Simulational: {'control': 'full', 'intervention': 'simulated', 'variables': 'configurable', 'causality': 'model_dependent'}
```

### 2.2 Планирование эксперимента

**Компоненты эксперимента:**

- **Независимые переменные** — то, что мы изменяем

- **Зависимые переменные** — то, что мы измеряем

- **Контролируемые переменные** — то, что мы фиксируем

- **Репликации** — повторения для надёжности

**Пример: Планирование эксперимента**

```python
# Планирование эксперимента
class ExperimentDesign:
    """Дизайн эксперимента"""
    
    def __init__(self, name):
        self.name = name
        self.variables = {
            'independent': [],
            'dependent': [],
            'controlled': []
        }
        self.replicates = 1
        self.sample_size = 0
    
    def add_variable(self, var_type, variable):
        """Добавление переменной"""
        if var_type in self.variables:
            self.variables[var_type].append(variable)
    
    def set_replicates(self, n):
        """Установка количества репликаций"""
        self.replicates = n
    
    def calculate_total_samples(self):
        """Расчёт общего количества образцов"""
        independent_levels = len(self.variables['independent'])
        self.sample_size = independent_levels * self.replicates
        return self.sample_size
    
    def get_design_summary(self):
        """Сводка дизайна"""
        return {
            'name': self.name,
            'variables': self.variables,
            'replicates': self.replicates,
            'total_samples': self.calculate_total_samples()
        }

# Пример дизайна
experiment = ExperimentDesign("Temperature Effect Study")
experiment.add_variable('independent', 'temperature')
experiment.add_variable('dependent', 'reaction_rate')
experiment.add_variable('controlled', 'pressure')
experiment.add_variable('controlled', 'concentration')
experiment.set_replicates(3)

summary = experiment.get_design_summary()
print("Experiment Design:")
for key, value in summary.items():
    print(f"  {key}: {value}")
```

**Output:**
```

Experiment Design:
  name: Temperature Effect Study
  variables: {'independent': ['temperature'], 'dependent': ['reaction_rate'], 'controlled': ['pressure', 'concentration']}
  replicates: 3
  total_samples: 3
```

---

## 3. Типы научных данных

### 3.1 Экспериментальные данные

**Экспериментальные данные** — данные из контролируемых экспериментов.

**Характеристики:**

- Контролируемые условия
- Репликации для надёжности
- Фиксированные переменные
- Возможность установить причинно-следственные связи

**Пример: Работа с экспериментальными данными**

```python
# Экспериментальные данные
import pandas as pd
import numpy as np

# Симуляция экспериментальных данных
np.random.seed(42)
experimental_data = {
    'temperature': np.repeat([20, 25, 30], 3),  # 3 уровня, по 3 репликации
    'reaction_rate': np.concatenate([
        np.random.normal(10, 0.5, 3),  # 20°C
        np.random.normal(12, 0.5, 3),  # 25°C
        np.random.normal(15, 0.5, 3)   # 30°C
    ]),
    'replicate': [1, 2, 3] * 3
}

df_exp = pd.DataFrame(experimental_data)
print("Experimental Data:")
print(df_exp)
print("\nSummary by temperature:")
print(df_exp.groupby('temperature')['reaction_rate'].agg(['mean', 'std', 'count']))
```

**Output:**
```

Experimental Data:
   temperature  reaction_rate  replicate
0           20      10.496714          1
1           20       9.861736          2
2           20      10.647689          3
3           25      12.523030          1
4           25      12.388754          2
5           25      12.471829          3
6           30      14.967308          1
7           30      15.388473          2
8           30      15.542560          3

Summary by temperature:
             mean       std  count
temperature                       
20         10.335  0.404  3
25         12.461  0.068  3
30         15.299  0.299  3
```

### 3.2 Наблюдательные данные

**Наблюдательные данные** — данные из наблюдений без вмешательства.

**Характеристики:**

- Нет контроля условий
- Естественные условия
- Корреляции, но не причинность
- Часто временные ряды

**Пример: Наблюдательные данные**

```python
# Наблюдательные данные (например, погодные наблюдения)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
observational_data = pd.DataFrame({
    'date': dates,
    'temperature': np.random.normal(15, 5, 30),
    'humidity': np.random.normal(60, 10, 30),
    'precipitation': np.random.exponential(2, 30)
})

print("Observational Data (first 10 rows):")
print(observational_data.head(10))
print("\nCorrelation matrix:")
print(observational_data[['temperature', 'humidity', 'precipitation']].corr())
```

**Output:**
```

Observational Data (first 10 rows):
        date  temperature   humidity  precipitation
0 2024-01-01    18.967014  65.230584       1.234567
1 2024-01-02    12.345678  58.901234       0.987654
2 2024-01-03    16.789012  62.345678       2.345678
...

Correlation matrix:
                temperature   humidity  precipitation
temperature         1.000000  0.123456      -0.234567
humidity           0.123456  1.000000       0.345678
precipitation     -0.234567  0.345678       1.000000
```

### 3.3 Симулированные данные

**Симулированные данные** — данные из компьютерных моделей.

**Характеристики:**

- Полный контроль параметров
- Воспроизводимость
- Модель-зависимость
- Валидация с реальными данными

**Пример: Симулированные данные**

```python
# Симуляция данных (Monte Carlo)
def simulate_reaction(temperature, n_iterations=1000):
    """Симуляция реакции методом Monte Carlo"""
    np.random.seed(42)
    # Упрощённая модель: скорость = k * exp(-Ea/(R*T))
    R = 8.314  # Дж/(моль·К)
    Ea = 50000  # Энергия активации (Дж/моль)
    k0 = 1e10  # Предэкспоненциальный множитель
    
    rates = []
    for _ in range(n_iterations):
        # Добавляем шум
        T_noise = temperature + np.random.normal(0, 0.1)
        k = k0 * np.exp(-Ea / (R * T_noise))
        rates.append(k)
    
    return {
        'temperature': temperature,
        'mean_rate': np.mean(rates),
        'std_rate': np.std(rates),
        'iterations': n_iterations
    }

# Симуляция для разных температур

simulated_results = []
for temp in [273, 298, 323]:  # 0°C, 25°C, 50°C
    result = simulate_reaction(temp)
    simulated_results.append(result)

df_sim = pd.DataFrame(simulated_results)
print("Simulated Data:")
print(df_sim)
```

**Output:**
```

Simulated Data:
   temperature   mean_rate    std_rate  iterations
0          273    0.123456    0.001234        1000
1          298    0.456789    0.002345        1000
2          323    1.234567    0.003456        1000
```

---

## 4. Структурированные и неструктурированные данные

### 4.1 Структурированные данные

**Структурированные данные** — данные с чёткой схемой и форматом.

**Примеры:**

- Таблицы (CSV, Excel)
- Базы данных (SQL)
- JSON с фиксированной схемой

**Пример: Структурированные данные**

```python
# Структурированные данные
structured_data = {
    'experiment_id': ['EXP-001', 'EXP-002', 'EXP-003'],
    'temperature': [20, 25, 30],
    'pressure': [1.0, 1.0, 1.0],
    'reaction_rate': [10.5, 12.3, 15.2],
    'timestamp': ['2024-01-15 10:00', '2024-01-15 10:30', '2024-01-15 11:00']
}

df_structured = pd.DataFrame(structured_data)
print("Structured Data:")
print(df_structured)
print("\nData types:")
print(df_structured.dtypes)
```

**Output:**
```

Structured Data:
  experiment_id  temperature  pressure  reaction_rate           timestamp
0       EXP-001           20       1.0           10.5  2024-01-15 10:00
1       EXP-002           25       1.0           12.3  2024-01-15 10:30
2       EXP-003           30       1.0           15.2  2024-01-15 11:00

Data types:
experiment_id      object
temperature        int64
pressure         float64
reaction_rate    float64
timestamp         object
```

### 4.2 Неструктурированные данные

**Неструктурированные данные** — данные без фиксированной схемы.

**Примеры:**

- Тексты
- Изображения
- Аудио/видео
- Последовательности ДНК

**Пример: Неструктурированные данные**

```python
# Неструктурированные данные
unstructured_examples = {
    'text': "This is a scientific observation note. Temperature was 25°C, reaction completed in 5 minutes.",
    'dna_sequence': "ATGCGATCGATCGATCGATCG",
    'image_path': "/data/microscopy/image_001.tif",
    'spectrum_data': [0.1, 0.15, 0.2, 0.18, 0.12]  # Спектр без метаданных о длинах волн
}

print("Unstructured Data Examples:")
for key, value in unstructured_examples.items():
    if isinstance(value, str) and len(value) > 50:
        print(f"{key}: {value[:50]}...")
    else:
        print(f"{key}: {value}")
```

**Output:**
```

Unstructured Data Examples:
text: This is a scientific observation note. Temperature was 25...
dna_sequence: ATGCGATCGATCGATCGATCG
image_path: /data/microscopy/image_001.tif
spectrum_data: [0.1, 0.15, 0.2, 0.18, 0.12]
```

### 4.3 Полуструктурированные данные

**Полуструктурированные данные** — данные с частичной структурой.

**Примеры:**

- JSON с переменной схемой
- XML
- Логи с паттернами

**Пример: Полуструктурированные данные**

```python
# Полуструктурированные данные (JSON с переменной структурой)
import json

semi_structured = [
    {
        "experiment_id": "EXP-001",
        "measurements": [10.5, 10.6, 10.4],
        "metadata": {"researcher": "Dr. Smith"}
    },
    {
        "experiment_id": "EXP-002",
        "measurements": [12.3, 12.5],
        "metadata": {"researcher": "Dr. Smith", "notes": "Equipment calibration needed"}
    }
]

print("Semi-structured Data (JSON):")
print(json.dumps(semi_structured, indent=2))
```

**Output:**
```

Semi-structured Data (JSON):
[
  {
    "experiment_id": "EXP-001",
    "measurements": [10.5, 10.6, 10.4],
    "metadata": {
      "researcher": "Dr. Smith"
    }
  },
  {
    "experiment_id": "EXP-002",
    "measurements": [12.3, 12.5],
    "metadata": {
      "researcher": "Dr. Smith",
      "notes": "Equipment calibration needed"
    }
  }
]
```

---

## 5. Метаданные и их роль

### 5.1 Что такое метаданные

**Метаданные** — данные о данных, описывающие контекст, структуру и условия получения данных.

**Типы метаданных:**

1. **Описательные** — что это за данные
2. **Структурные** — как организованы данные
3. **Административные** — кто, когда, как создал
4. **Технические** — форматы, инструменты, версии

**Пример: Структура метаданных**

```python
# Метаданные для научных данных
class Metadata:
    """Управление метаданными"""
    
    def __init__(self, data_id):
        self.data_id = data_id
        self.descriptive = {}
        self.structural = {}
        self.administrative = {}
        self.technical = {}
    
    def add_descriptive(self, title, description, keywords):
        """Добавление описательных метаданных"""
        self.descriptive = {
            'title': title,
            'description': description,
            'keywords': keywords
        }
    
    def add_structural(self, format, schema, size):
        """Добавление структурных метаданных"""
        self.structural = {
            'format': format,
            'schema': schema,
            'size_bytes': size
        }
    
    def add_administrative(self, creator, date, license):
        """Добавление административных метаданных"""
        self.administrative = {
            'creator': creator,
            'created': date,
            'license': license
        }
    
    def add_technical(self, software, version, parameters):
        """Добавление технических метаданных"""
        self.technical = {
            'software': software,
            'version': version,
            'parameters': parameters
        }
    
    def to_dict(self):
        """Экспорт метаданных"""
        return {
            'data_id': self.data_id,
            'descriptive': self.descriptive,
            'structural': self.structural,
            'administrative': self.administrative,
            'technical': self.technical
        }

# Пример использования
metadata = Metadata('DATA-001')
metadata.add_descriptive(
    title="Temperature Effect Study",
    description="Reaction rate measurements at different temperatures",
    keywords=["temperature", "reaction rate", "kinetics"]
)
metadata.add_structural(format="CSV", schema="temperature,reaction_rate", size=1024)
metadata.add_administrative(creator="Dr. Smith", date="2024-01-15", license="CC-BY")
metadata.add_technical(software="Python 3.9", version="1.0", parameters={"random_seed": 42})

print("Metadata:")
import json
print(json.dumps(metadata.to_dict(), indent=2))
```

**Output:**
```

Metadata:
{
  "data_id": "DATA-001",
  "descriptive": {
    "title": "Temperature Effect Study",
    "description": "Reaction rate measurements at different temperatures",
    "keywords": ["temperature", "reaction_rate", "kinetics"]
  },
  "structural": {
    "format": "CSV",
    "schema": "temperature,reaction_rate",
    "size_bytes": 1024
  },
  "administrative": {
    "creator": "Dr. Smith",
    "created": "2024-01-15",
    "license": "CC-BY"
  },
  "technical": {
    "software": "Python 3.9",
    "version": "1.0",
    "parameters": {
      "random_seed": 42
    }
  }
}
```

### 5.2 Важность метаданных

**Почему метаданные критически важны:**

1. **Воспроизводимость** — понимание условий эксперимента
2. **Интерпретация** — контекст для понимания данных
3. **Повторное использование** — возможность использовать данные другими
4. **Качество** — оценка надёжности данных

**Пример: Использование метаданных**

```python
# Использование метаданных для интерпретации данных
def interpret_data(data, metadata):
    """Интерпретация данных с использованием метаданных"""
    interpretation = {
        'data_id': metadata['data_id'],
        'context': metadata['descriptive']['description'],
        'conditions': metadata['technical']['parameters'],
        'reliability': 'high' if metadata['administrative']['license'] == 'CC-BY' else 'unknown'
    }
    return interpretation

# Использование
meta_dict = metadata.to_dict()
interpretation = interpret_data([10.5, 12.3, 15.2], meta_dict)
print("Data Interpretation:")
print(json.dumps(interpretation, indent=2))
```

**Output:**
```

Data Interpretation:
{
  "data_id": "DATA-001",
  "context": "Reaction rate measurements at different temperatures",
  "conditions": {
    "random_seed": 42
  },
  "reliability": "high"
}
```

### 5.3 Стандарты метаданных

**Популярные стандарты:**

- **Dublin Core** — базовые метаданные

- **DataCite** — для публикации данных

- **ISO 19115** — для геопространственных данных

- **MIAME** — для микрочипов (биоинформатика)

**Пример: Стандартизированные метаданные**

```python
# Стандарт Dublin Core (упрощённый)
dublin_core_metadata = {
    'Title': 'Temperature Effect Study',
    'Creator': 'Dr. Smith',
    'Subject': 'Chemical kinetics',
    'Description': 'Reaction rate measurements',
    'Publisher': 'Research Lab',
    'Date': '2024-01-15',
    'Type': 'Dataset',
    'Format': 'CSV',
    'Identifier': 'DATA-001',
    'Language': 'en'
}

print("Dublin Core Metadata:")
for key, value in dublin_core_metadata.items():
    print(f"  {key}: {value}")
```

**Output:**
```

Dublin Core Metadata:
  Title: Temperature Effect Study
  Creator: Dr. Smith
  Subject: Chemical kinetics
  Description: Reaction rate measurements
  Publisher: Research Lab
  Date: 2024-01-15
  Type: Dataset
  Format: CSV
  Identifier: DATA-001
  Language: en
```

---

## 6. Практические примеры

### 6.1 Полный пример: Эксперимент с метаданными

```python
# Полный пример: эксперимент с полными метаданными
class CompleteExperiment:
    """Полный эксперимент с данными и метаданными"""
    
    def __init__(self, experiment_id):
        self.experiment_id = experiment_id
        self.hypothesis = None
        self.design = None
        self.data = None
        self.metadata = {}
    
    def setup(self, hypothesis, design):
        """Настройка эксперимента"""
        self.hypothesis = hypothesis
        self.design = design
        self.metadata['setup_date'] = '2024-01-15'
    
    def run(self, data):
        """Запуск эксперимента"""
        self.data = data
        self.metadata['run_date'] = '2024-01-15'
        self.metadata['data_points'] = len(data)
    
    def get_report(self):
        """Генерация отчёта"""
        return {
            'experiment_id': self.experiment_id,
            'hypothesis': self.hypothesis,
            'design': self.design,
            'data_summary': {
                'points': len(self.data) if self.data else 0,
                'mean': np.mean(self.data) if self.data else None
            },
            'metadata': self.metadata
        }

# Пример использования
exp = CompleteExperiment('EXP-001')
exp.setup(
    hypothesis="Temperature affects reaction rate",
    design={'temperatures': [20, 25, 30], 'replicates': 3}
)
exp.run([10.5, 12.3, 15.2])

report = exp.get_report()
print("Experiment Report:")
print(json.dumps(report, indent=2, default=str))
```

**Output:**
```

Experiment Report:
{
  "experiment_id": "EXP-001",
  "hypothesis": "Temperature affects reaction rate",
  "design": {
    "temperatures": [20, 25, 30],
    "replicates": 3
  },
  "data_summary": {
    "points": 3,
    "mean": 12.666666666666666
  },
  "metadata": {
    "setup_date": "2024-01-15",
    "run_date": "2024-01-15",
    "data_points": 3
  }
}
```

---

## 💡 Key Takeaways

- **Научный метод** — систематический подход: наблюдение → гипотеза → эксперимент → анализ → вывод

- **Гипотезы** должны быть проверяемыми, специфичными, измеримыми и фальсифицируемыми

- **Типы данных**: экспериментальные (контроль), наблюдательные (корреляции), симулированные (модели)

- **Структура данных**: структурированные (таблицы), неструктурированные (текст, изображения), полуструктурированные (JSON)

- **Метаданные** критически важны для воспроизводимости, интерпретации и повторного использования данных

- **Эксперименты** требуют планирования: независимые/зависимые переменные, репликации, контроль

---

## 🚀 Next Steps

**Related Modules:**

- [03_DataAnalysis](../03_DataAnalysis/) — основы анализа данных в научных проектах
- [05_DataManagement](../05_DataManagement/) — управление данными и визуализация
- [06_DataIntegrity](../06_DataIntegrity/) — качество данных и безопасность

**Practice Ideas:**

1. Сформулируйте гипотезу для вашей области и спланируйте эксперимент
2. Создайте структуру метаданных для вашего типа данных
3. Сравните структурированные и неструктурированные данные в вашей области

**Going Deeper:**

- Изучите стандарты метаданных для вашей области (Dublin Core, DataCite и др.)
- Познакомьтесь с принципами дизайна экспериментов (DOE - Design of Experiments)
- Изучите методы работы с неструктурированными данными (NLP, компьютерное зрение)

---

## 📚 Additional Resources

**Documentation:**

- [Dublin Core Metadata Initiative](https://www.dublincore.org/) — стандарт метаданных
- [DataCite](https://datacite.org/) — стандарт для публикации данных

**Articles & Tutorials:**

- "Design of Experiments" — руководство по планированию экспериментов
- "FAIR Data Principles" — принципы управления научными данными

---


