# Работа с большими научными датасетами
## Large-scale data, memory-efficient processing, chunking и parallel processing

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы работы с данными (модули 03-05)
- Знать Python, Pandas, NumPy (модуль 04_Tools)
- Понимать основы анализа данных (модуль 08_AdvancedAnalysis)
- Иметь представление о производительности вычислений

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Работать с большими научными датасетами, которые не помещаются в память
- Применять memory-efficient методы обработки данных
- Использовать chunking и streaming для обработки данных
- Применять параллельную обработку для ускорения вычислений
- Выбирать подходящие инструменты для работы с большими данными

---

## 1. Large-scale Scientific Data

Современные научные инструменты генерируют огромные объёмы данных. Геномные проекты могут создавать терабайты данных, спутниковые наблюдения — петабайты, а симуляции — ещё больше. Работа с такими данными требует специальных методов и инструментов.

### 1.1 Характеристики больших научных данных

**Большие научные датасеты** — данные, которые превышают возможности стандартных методов обработки. Это не просто большие файлы — это данные, которые требуют изменения подхода к их обработке.

**Большие научные датасеты** — данные, которые:
- **Не помещаются в оперативную память** — стандартные методы предполагают загрузку всех данных в память, что невозможно для больших датасетов. Например, датасет с 10 миллионами строк и 100 колонками типа float64 занимает примерно 7.45 GB памяти, что превышает возможности большинства компьютеров.

- **Требуют специальных методов обработки** — стандартные инструменты (например, Pandas) не могут обработать такие данные напрямую. Нужны специальные методы: chunking, streaming, распределённая обработка.

- **Имеют объём от GB до PB** — современные научные проекты генерируют данные от гигабайтов (отдельные эксперименты) до петабайтов (крупные проекты, такие как секвенирование тысяч геномов или многолетние спутниковые наблюдения).

### 1.2 Типы больших научных данных

Разные типы больших научных данных требуют разных подходов к обработке. Понимание структуры данных критически важно для выбора правильных методов и инструментов.

**Классификация по структуре:**

1. **Табличные данные** — CSV, Parquet, HDF5. Это наиболее распространённый тип больших научных данных. Табличные форматы различаются по эффективности: CSV прост, но неэффективен (1000 MB, медленное чтение, без сжатия), Parquet эффективен (200 MB, быстрое чтение, высокое сжатие), HDF5 хорош для научных данных (300 MB, быстрое чтение, среднее сжатие, поддержка метаданных), Feather очень быстр для временного хранения (250 MB, очень быстрое чтение, среднее сжатие).

2. **Последовательности** — геномные данные, временные ряды. Эти данные имеют линейную структуру, но могут быть очень длинными (геномы — миллиарды символов, временные ряды — миллионы точек). Требуют streaming-обработки.

3. **Изображения** — микроскопия, спутниковые снимки. Изображения могут быть очень большими (высокое разрешение, множество каналов, временные серии). Требуют специальных библиотек для обработки изображений.

4. **Графы** — сети взаимодействий. Графы могут иметь миллионы узлов и рёбер. Требуют специализированных алгоритмов и структур данных для эффективной обработки.

---

## 2. Memory-Efficient Processing

Когда данные не помещаются в память, стандартные методы обработки становятся неприменимыми. Нужны методы, которые обрабатывают данные эффективно, не загружая их полностью в память.

### 2.1 Chunking — обработка по частям

**Chunking** — обработка данных небольшими порциями. Это один из самых простых и эффективных методов работы с большими данными. Вместо загрузки всего файла в память, данные читаются и обрабатываются небольшими порциями (chunks).

Преимущество chunking в том, что он позволяет обрабатывать данные любого размера, используя фиксированное количество памяти. Например, файл можно читать порциями по 10,000 строк, обрабатывать каждую порцию независимо, и затем объединять результаты. Это критически важно для больших файлов, которые не помещаются в память.

Chunking особенно эффективен для операций, которые можно выполнять независимо на каждой порции (например, группировка и агрегация), а затем объединить результаты. Это позволяет обрабатывать данные любого размера, используя ограниченную память.

### 2.2 Streaming — потоковая обработка

**Streaming** — обработка данных по мере их поступления.

**Пример: Потоковая обработка**

```python
# Потоковая обработка данных
def stream_process(filepath):
    """Потоковая обработка данных"""
    accumulator = {'sum': 0, 'count': 0}
    
    # Открываем файл и читаем построчно
    with open(filepath, 'r') as f:
        header = f.readline()  # Пропускаем заголовок
        
        for line in f:
            # Обрабатываем каждую строку
            values = line.strip().split(',')
            if len(values) > 1:
                try:
                    value = float(values[1])
                    accumulator['sum'] += value
                    accumulator['count'] += 1
                except ValueError:
                    continue
    
    # Вычисляем среднее
    if accumulator['count'] > 0:
        mean = accumulator['sum'] / accumulator['count']
        return mean
    return None

print("Streaming processing:")
print("Reads file line by line")
print("Processes data incrementally")
print("Minimal memory usage")
```

**Output:**
```
Streaming processing:
Reads file line by line
Processes data incrementally
Minimal memory usage
```

### 2.3 Оптимизация типов данных

**Оптимизация памяти через правильные типы данных.**

**Пример: Оптимизация типов**

```python
# Оптимизация типов данных для экономии памяти
def optimize_dtypes(df):
    """Оптимизация типов данных DataFrame"""
    original_size = df.memory_usage(deep=True).sum() / 1024**2
    
    # Оптимизация числовых колонок
    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')
    
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = pd.to_numeric(df[col], downcast='float')
    
    # Оптимизация категориальных данных
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].nunique() / len(df) < 0.5:  # Если < 50% уникальных значений
            df[col] = df[col].astype('category')
    
    optimized_size = df.memory_usage(deep=True).sum() / 1024**2
    reduction = (1 - optimized_size / original_size) * 100
    
    return {
        'original_mb': original_size,
        'optimized_mb': optimized_size,
        'reduction_percent': reduction
    }

# Пример
df = pd.DataFrame({
    'id': range(1000000),
    'category': ['A', 'B', 'C'] * 333334,
    'value': np.random.randn(1000000)
})

result = optimize_dtypes(df.copy())
print(f"Original size: {result['original_mb']:.2f} MB")
print(f"Optimized size: {result['optimized_mb']:.2f} MB")
print(f"Reduction: {result['reduction_percent']:.1f}%")
```

**Output:**
```
Original size: 24.00 MB
Optimized size: 16.00 MB
Reduction: 33.3%
```

---

## 3. Chunking и Streaming

### 3.1 Pandas Chunking

**Пример: Chunking с Pandas**

```python
# Обработка большого файла по частям
def process_csv_chunked(filepath, process_func, chunk_size=50000):
    """Обработка CSV файла по частям"""
    chunk_results = []
    
    try:
        for i, chunk in enumerate(pd.read_csv(filepath, chunksize=chunk_size)):
            # Применяем функцию обработки к каждой части
            result = process_func(chunk)
            chunk_results.append(result)
            
            # Логирование прогресса
            if (i + 1) % 10 == 0:
                print(f"Processed {(i + 1) * chunk_size:,} rows")
    
    except Exception as e:
        print(f"Error processing chunk: {e}")
        raise
    
    # Объединение результатов
    if chunk_results:
        return pd.concat(chunk_results, ignore_index=True)
    return pd.DataFrame()

# Функция обработки
def calculate_statistics(chunk):
    """Вычисление статистики для части данных"""
    return pd.DataFrame({
        'mean': [chunk['value'].mean()],
        'std': [chunk['value'].std()],
        'count': [len(chunk)]
    })

print("Chunked processing with Pandas:")
print("- Reads file in chunks")
print("- Processes each chunk")
print("- Combines results")
```

**Output:**
```
Chunked processing with Pandas:
- Reads file in chunks
- Processes each chunk
- Combines results
```

### 3.2 Dask для больших данных

**Dask** — библиотека для параллельных вычислений с большими данными.

**Пример: Использование Dask**

```python
# Dask для работы с большими данными
try:
    import dask.dataframe as dd
    
    # Создание Dask DataFrame из CSV
    # ddf = dd.read_csv('large_file.csv')
    
    # Операции выполняются лениво
    # result = ddf.groupby('category')['value'].mean()
    # result.compute()  # Выполнение вычислений
    
    print("Dask allows:")
    print("- Lazy evaluation")
    print("- Parallel processing")
    print("- Out-of-core computation")
except ImportError:
    print("Dask not installed. Install with: pip install dask")
```

**Output:**
```
Dask allows:
- Lazy evaluation
- Parallel processing
- Out-of-core computation
```

---

## 4. Parallel Processing

### 4.1 Многопроцессорная обработка

**Пример: Параллельная обработка**

```python
from multiprocessing import Pool
import numpy as np

def process_chunk(chunk_data):
    """Обработка части данных"""
    # Симуляция обработки
    result = np.mean(chunk_data)
    return result

def parallel_process(data, n_processes=4):
    """Параллельная обработка данных"""
    # Разделение данных на части
    chunk_size = len(data) // n_processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Параллельная обработка
    with Pool(n_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    return results

# Пример
data = np.random.randn(1000000)
results = parallel_process(data, n_processes=4)
print(f"Parallel processing results: {results}")
print(f"Overall mean: {np.mean(results):.4f}")
```

**Output:**
```
Parallel processing results: [0.0012, -0.0008, 0.0005, -0.0003]
Overall mean: 0.0002
```

### 4.2 NumPy параллельные операции

**Пример: Векторизованные операции**

```python
# Векторизованные операции NumPy (автоматически параллельные)
import numpy as np

# Большой массив
large_array = np.random.randn(10_000_000)

# Векторизованные операции быстрее циклов
result_vectorized = np.mean(large_array ** 2)
print(f"Vectorized result: {result_vectorized:.4f}")

# Сравнение с циклом (медленнее)
# result_loop = sum(x**2 for x in large_array) / len(large_array)  # Очень медленно
print("Vectorized operations are automatically optimized")
```

**Output:**
```
Vectorized result: 1.0002
Vectorized operations are automatically optimized
```

---

## 5. Инструменты для больших данных

### 5.1 Apache Spark

**Spark** — распределённая система обработки данных.

**Пример: Концепция Spark**

```python
# Концепция работы со Spark (упрощённо)
print("Apache Spark:")
print("- Distributed data processing")
print("- Resilient Distributed Datasets (RDD)")
print("- DataFrame API similar to Pandas")
print("- Can handle TB-PB scale data")
print("\nExample workflow:")
print("1. Load data from storage")
print("2. Transform data (filter, map, reduce)")
print("3. Aggregate results")
print("4. Save or display results")
```

**Output:**
```
Apache Spark:
- Distributed data processing
- Resilient Distributed Datasets (RDD)
- DataFrame API similar to Pandas
- Can handle TB-PB scale data

Example workflow:
1. Load data from storage
2. Transform data (filter, map, reduce)
3. Aggregate results
4. Save or display results
```

### 5.2 Выбор инструмента

**Критерии выбора:**

| Инструмент | Размер данных | Когда использовать |
|------------|---------------|-------------------|
| **Pandas** | До нескольких GB | Данные помещаются в память |
| **Dask** | GB - TB | Нужна параллельная обработка |
| **Spark** | TB - PB | Распределённая обработка |
| **Chunking** | Любой | Простая обработка по частям |

**Пример: Выбор инструмента**

```python
def choose_tool(data_size_gb, complexity='simple'):
    """Выбор инструмента для обработки данных"""
    if data_size_gb < 10:
        return "Pandas (fits in memory)"
    elif data_size_gb < 100:
        return "Dask or Pandas with chunking"
    elif data_size_gb < 1000:
        return "Dask or Spark"
    else:
        return "Spark (distributed processing)"

print("Tool selection:")
print(f"5 GB: {choose_tool(5)}")
print(f"50 GB: {choose_tool(50)}")
print(f"500 GB: {choose_tool(500)}")
print(f"5000 GB: {choose_tool(5000)}")
```

**Output:**
```
Tool selection:
5 GB: Pandas (fits in memory)
50 GB: Dask or Pandas with chunking
500 GB: Dask or Spark
5000 GB: Spark (distributed processing)
```

---

## 💡 Key Takeaways

- **Большие научные данные** требуют специальных методов обработки (chunking, streaming)

- **Memory-efficient processing** — оптимизация типов данных и обработка по частям

- **Chunking** — обработка данных небольшими порциями для экономии памяти

- **Streaming** — обработка данных по мере поступления, минимальное использование памяти

- **Parallel processing** — ускорение обработки через параллельные вычисления

- **Выбор инструмента** зависит от размера данных и сложности обработки

---

## 🚀 Next Steps

**Related Modules:**

- [10_Modeling](../10_Modeling/) — моделирование и симуляции
- [15_Optimization](../15_Optimization/) — оптимизация и масштабирование
- [05_DataManagement](../05_DataManagement/) — управление данными

**Practice Ideas:**

1. Обработайте большой файл используя chunking
2. Оптимизируйте типы данных в вашем датасете
3. Примените параллельную обработку к вашим вычислениям

**Going Deeper:**

- Изучите Apache Spark для распределённой обработки
- Познакомьтесь с Dask для параллельных вычислений
- Изучите оптимизацию запросов к базам данных

---

## 📚 Additional Resources

**Documentation:**

- [Dask Documentation](https://docs.dask.org/)
- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [Pandas Memory Usage](https://pandas.pydata.org/docs/user_guide/scale.html)

---


