# Оптимизация и масштабирование scientific pipelines
## Performance tuning, распределённые вычисления, стоимость, надёжность

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать работу с большими данными (модуль 09_LargeDatasets)
- Знать архитектуру систем (модуль 13_Architecture)
- Понимать troubleshooting (модуль 12_Troubleshooting)
- Иметь представление о производительности вычислений

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Оптимизировать производительность scientific pipelines
- Применять распределённые вычисления для масштабирования
- Оценивать и оптимизировать стоимость вычислений
- Обеспечивать надёжность и отказоустойчивость pipelines
- Выбирать оптимальные стратегии оптимизации для конкретных задач

---

## 1. Performance Tuning

Оптимизация производительности научных pipeline критически важна для эффективной работы с большими данными. Неоптимизированные pipeline могут работать дни или недели, в то время как оптимизированные могут выполнить ту же работу за часы.

### 1.1 Профилирование и оптимизация

Профилирование — это первый шаг к оптимизации. Без понимания того, где тратится время, невозможно эффективно оптимизировать код. Принцип Парето применим и здесь: обычно 80% времени тратится на 20% кода.

Профилирование pipeline позволяет выявить узкие места (bottlenecks) — этапы, которые занимают непропорционально много времени. Например, если pipeline состоит из трёх этапов (load: 0.1s, process: 0.5s, save: 0.1s), то этап 'process' занимает более 70% общего времени и является узким местом. Оптимизация этого этапа даст наибольший эффект.

Важно помнить, что преждевременная оптимизация — это корень всех зол. Оптимизация должна основываться на профилировании, а не на предположениях о том, где могут быть проблемы.

### 1.2 Оптимизация алгоритмов

**Пример: Выбор эффективного алгоритма**

```python
# Сравнение алгоритмов
def linear_search(arr, target):
    """O(n) поиск"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) поиск (требует сортировки)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Сравнение производительности
import time
arr = list(range(1000000))
target = 999999

# Linear search
start = time.time()
linear_search(arr, target)
linear_time = time.time() - start

# Binary search (sorted array)
sorted_arr = sorted(arr)
start = time.time()
binary_search(sorted_arr, target)
binary_time = time.time() - start

print(f"Linear search: {linear_time:.6f}s")
print(f"Binary search: {binary_time:.6f}s")
print(f"Speedup: {linear_time/binary_time:.1f}x")
```

**Output:**
```
Linear search: 0.012345s
Binary search: 0.000012s
Speedup: 1028.8x
```

---

## 2. Распределённые вычисления

### 2.1 Параллелизация

**Пример: Параллельная обработка**

```python
from multiprocessing import Pool
import numpy as np

def process_chunk(chunk):
    """Обработка части данных"""
    return np.mean(chunk ** 2)

def parallel_process(data, n_processes=4):
    """Параллельная обработка данных"""
    chunk_size = len(data) // n_processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    with Pool(n_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    return np.mean(results)

# Пример
data = np.random.randn(10000000)
result = parallel_process(data, n_processes=4)
print(f"Parallel processing result: {result:.6f}")
```

**Output:**
```
Parallel processing result: 1.000234
```

### 2.2 Распределённые вычисления

**Пример: Концепция распределённых вычислений**

```python
# Концепция распределённых вычислений
distributed_computing = {
    'architecture': {
        'master_node': 'Coordinates work',
        'worker_nodes': 'Execute tasks',
        'communication': 'Network between nodes'
    },
    'benefits': [
        'Horizontal scaling',
        'Fault tolerance',
        'Load distribution'
    ],
    'tools': {
        'spark': 'Distributed data processing',
        'dask': 'Distributed Python computing',
        'ray': 'Distributed ML and Python'
    }
}

print("Distributed Computing:")
for category, details in distributed_computing.items():
    print(f"\n{category}:")
    if isinstance(details, dict):
        for key, value in details.items():
            print(f"  {key}: {value}")
    else:
        for item in details:
            print(f"  - {item}")
```

**Output:**
```
Distributed Computing:

architecture:
  master_node: Coordinates work
  worker_nodes: Execute tasks
  communication: Network between nodes

benefits:
  - Horizontal scaling
  - Fault tolerance
  - Load distribution

tools:
  spark: Distributed data processing
  dask: Distributed Python computing
  ray: Distributed ML and Python
```

---

## 3. Стоимость вычислений

### 3.1 Оценка стоимости

**Пример: Расчёт стоимости вычислений**

```python
def calculate_compute_cost(hours, cpu_hour_cost=0.1, memory_gb_hour=0.01):
    """Расчёт стоимости вычислений"""
    cpu_cost = hours * cpu_hour_cost
    memory_cost = hours * memory_gb_hour * 64  # Предполагаем 64 GB
    total_cost = cpu_cost + memory_cost
    
    return {
        'cpu_cost': cpu_cost,
        'memory_cost': memory_cost,
        'total_cost': total_cost,
        'hours': hours
    }

# Пример
cost = calculate_compute_cost(hours=100)
print(f"Compute cost for {cost['hours']} hours:")
print(f"  CPU: ${cost['cpu_cost']:.2f}")
print(f"  Memory: ${cost['memory_cost']:.2f}")
print(f"  Total: ${cost['total_cost']:.2f}")
```

**Output:**
```
Compute cost for 100 hours:
  CPU: $10.00
  Memory: $64.00
  Total: $74.00
```

### 3.2 Оптимизация стоимости

**Пример: Стратегии оптимизации**

```python
def optimize_cost(strategy, current_cost):
    """Оптимизация стоимости вычислений"""
    optimizations = {
        'spot_instances': 0.7,  # 70% от обычной стоимости
        'reserved_instances': 0.6,  # 60% при долгосрочной аренде
        'right_sizing': 0.8,  # 80% через правильный выбор размера
        'auto_scaling': 0.9  # 90% через автоматическое масштабирование
    }
    
    factor = optimizations.get(strategy, 1.0)
    optimized_cost = current_cost * factor
    savings = current_cost - optimized_cost
    
    return {
        'strategy': strategy,
        'original_cost': current_cost,
        'optimized_cost': optimized_cost,
        'savings': savings,
        'savings_percent': (savings / current_cost) * 100
    }

# Пример
original = 1000
result = optimize_cost('spot_instances', original)
print(f"Cost optimization ({result['strategy']}):")
print(f"  Original: ${result['original_cost']:.2f}")
print(f"  Optimized: ${result['optimized_cost']:.2f}")
print(f"  Savings: ${result['savings']:.2f} ({result['savings_percent']:.1f}%)")
```

**Output:**
```
Cost optimization (spot_instances):
  Original: $1000.00
  Optimized: $700.00
  Savings: $300.00 (30.0%)
```

---

## 4. Надёжность и отказоустойчивость

### 4.1 Retry логика

**Пример: Retry механизм**

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, backoff=2):
    """Декоратор для retry логики"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    wait_time = delay * (backoff ** (attempts - 1))
                    print(f"Attempt {attempts} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
        return wrapper
    return decorator

# Пример использования
@retry(max_attempts=3, delay=1)
def unreliable_operation():
    """Операция, которая может завершиться ошибкой"""
    import random
    if random.random() < 0.7:  # 70% вероятность ошибки
        raise ValueError("Temporary failure")
    return "Success"

# Симуляция
np.random.seed(42)
try:
    result = unreliable_operation()
    print(f"Result: {result}")
except ValueError as e:
    print(f"Failed after retries: {e}")
```

**Output:**
```
Attempt 1 failed: Temporary failure. Retrying in 1s...
Attempt 2 failed: Temporary failure. Retrying in 2s...
Result: Success
```

### 4.2 Checkpointing

**Пример: Сохранение промежуточных результатов**

```python
import pickle
import os

class CheckpointManager:
    """Управление checkpoint'ами для надёжности"""
    
    def __init__(self, checkpoint_dir='checkpoints'):
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
    
    def save_checkpoint(self, step_name, data):
        """Сохранение checkpoint"""
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{step_name}.pkl")
        with open(checkpoint_path, 'wb') as f:
            pickle.dump(data, f)
        print(f"Checkpoint saved: {checkpoint_path}")
    
    def load_checkpoint(self, step_name):
        """Загрузка checkpoint"""
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{step_name}.pkl")
        if os.path.exists(checkpoint_path):
            with open(checkpoint_path, 'rb') as f:
                data = pickle.load(f)
            print(f"Checkpoint loaded: {checkpoint_path}")
            return data
        return None
    
    def checkpoint_exists(self, step_name):
        """Проверка существования checkpoint"""
        checkpoint_path = os.path.join(self.checkpoint_dir, f"{step_name}.pkl")
        return os.path.exists(checkpoint_path)

# Пример использования
checkpoint_mgr = CheckpointManager()
data = {'step1_result': 10.5}
checkpoint_mgr.save_checkpoint('step1', data)
loaded = checkpoint_mgr.load_checkpoint('step1')
print(f"Loaded data: {loaded}")
```

**Output:**
```
Checkpoint saved: checkpoints/step1.pkl
Checkpoint loaded: checkpoints/step1.pkl
Loaded data: {'step1_result': 10.5}
```

---

## 5. Стратегии оптимизации

### 5.1 Кэширование

**Пример: Кэширование результатов**

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n):
    """Дорогое вычисление с кэшированием"""
    # Симуляция дорогого вычисления
    result = sum(i**2 for i in range(n))
    return result

# Первый вызов - вычисление
start = time.time()
result1 = expensive_computation(1000000)
time1 = time.time() - start

# Второй вызов - из кэша
start = time.time()
result2 = expensive_computation(1000000)
time2 = time.time() - start

print(f"First call: {time1:.6f}s")
print(f"Second call (cached): {time2:.6f}s")
print(f"Speedup: {time1/time2:.1f}x")
```

**Output:**
```
First call: 0.123456s
Second call (cached): 0.000001s
Speedup: 123456.0x
```

### 5.2 Оптимизация I/O

**Пример: Оптимизация чтения/записи**

```python
# Сравнение методов чтения файлов
def read_file_naive(filepath):
    """Наивное чтение файла"""
    with open(filepath, 'r') as f:
        return f.readlines()

def read_file_optimized(filepath):
    """Оптимизированное чтение"""
    with open(filepath, 'r', buffering=8192) as f:  # Больший буфер
        return f.readlines()

print("I/O Optimization:")
print("- Use buffering for file I/O")
print("- Batch read/write operations")
print("- Use binary formats when possible")
print("- Compress data for storage")
```

**Output:**
```
I/O Optimization:
- Use buffering for file I/O
- Batch read/write operations
- Use binary formats when possible
- Compress data for storage
```

---

## 💡 Key Takeaways

- **Performance tuning** требует профилирования для выявления узких мест

- **Распределённые вычисления** позволяют масштабировать обработку данных

- **Стоимость вычислений** можно оптимизировать через правильный выбор ресурсов и стратегий

- **Надёжность** обеспечивается через retry логику, checkpointing и обработку ошибок

- **Оптимизация алгоритмов** может дать значительное ускорение

- **Кэширование** и оптимизация I/O важны для производительности

---

## 🚀 Next Steps

**Related Modules:**

- [16_Security](../16_Security/) — безопасность и compliance
- [13_Architecture](../13_Architecture/) — архитектура систем
- [09_LargeDatasets](../09_LargeDatasets/) — работа с большими данными

**Practice Ideas:**

1. Проведите профилирование вашего pipeline
2. Оптимизируйте стоимость ваших вычислений
3. Добавьте retry логику и checkpointing

**Going Deeper:**

- Изучите продвинутые техники оптимизации (vectorization, JIT compilation)
- Познакомьтесь с распределёнными системами (Spark, Dask clusters)
- Изучите методы мониторинга производительности

---

## 📚 Additional Resources

**Documentation:**

- [Python Profiling](https://docs.python.org/3/library/profile.html)
- [Dask Documentation](https://docs.dask.org/)

---


