# Troubleshooting scientific pipelines
## Типовые ошибки, отладка вычислений, проверка корректности результатов

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы scientific workflows (модуль 11_SpecializedTools)
- Знать Python и работу с данными (модуль 04_Tools)
- Понимать принципы анализа данных (модули 03, 08)
- Иметь опыт отладки кода

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Выявлять типовые ошибки в scientific pipelines
- Отлаживать вычисления и находить источники проблем
- Проверять корректность результатов анализа
- Идентифицировать performance bottlenecks
- Применять систематический подход к troubleshooting

---

## 1. Типовые ошибки scientific pipelines

Отладка научных pipeline — это критически важный навык. Ошибки в научных вычислениях могут привести к неверным выводам, которые могут повлиять на целые области исследований. Систематический подход к troubleshooting помогает быстро находить и исправлять проблемы.

### 1.1 Ошибки данных

Данные — это основа всех научных вычислений, и ошибки в данных могут привести к неверным результатам на всех последующих этапах анализа. Проверка качества данных должна быть первым шагом в любом научном pipeline.

**Типовые проблемы с данными:**

- **Пропущенные значения** — могут возникать из-за ошибок измерений, сбоев оборудования или проблем при записи данных. Они могут искажать статистические выводы и делать данные непригодными для анализа.

- **Неправильные форматы** — данные могут быть в неправильном формате (например, даты как строки, числа с запятыми вместо точек). Это может привести к ошибкам при обработке.

- **Некорректные типы данных** — колонки могут иметь неправильный тип (например, числовые данные как строки). Это может привести к ошибкам при вычислениях.

- **Выбросы и аномалии** — значения, которые значительно отличаются от остальных, могут быть ошибками измерений или реальными, но необычными наблюдениями. Важно различать эти случаи.

Систематическая проверка данных может выявить эти проблемы на ранних этапах. Например, проверка может обнаружить пропущенные значения в колонке 'value' и выбросы (значение 1000, когда остальные значения находятся в диапазоне 1-4). Это позволяет исправить проблемы до начала анализа.

### 1.2 Ошибки в вычислениях

Ошибки в вычислениях могут возникать на любом этапе анализа и часто остаются незамеченными, если результаты не проверяются тщательно.

**Типовые ошибки:**

- **Деление на ноль** — может возникать, когда делитель равен нулю или очень близок к нулю. Это может привести к бесконечным или неопределённым значениям, которые могут распространяться через весь анализ.
- Переполнение числовых типов
- Неправильный порядок операций
- Ошибки округления

**Пример: Обработка ошибок вычислений**

```python

def safe_divide(a, b):
    """Безопасное деление с обработкой ошибок"""
    try:
        if np.isclose(b, 0):
            return np.nan
        return a / b
    except (TypeError, ValueError) as e:
        print(f"Error in division: {e}")
        return np.nan

# Примеры
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")
```

**Output:**
```

10 / 2 = 5.0
10 / 0 = nan
Error in division: unsupported operand type(s) for /: 'int' and 'str'
10 / 'a' = nan
```

---

## 2. Отладка вычислений

### 2.1 Логирование

**Логирование** — ключевой инструмент отладки.

**Пример: Структурированное логирование**

```python

import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('pipeline')

def process_data(data, step_name):
    """Обработка данных с логированием"""
    logger.info(f"Starting {step_name}")
    logger.debug(f"Input data shape: {data.shape}")
    
    try:
        result = data.mean()
        logger.info(f"{step_name} completed successfully: {result:.3f}")
        return result
    except Exception as e:
        logger.error(f"Error in {step_name}: {e}", exc_info=True)
        raise

# Пример использования
data = np.array([1, 2, 3, 4, 5])
result = process_data(data, "mean_calculation")
```

**Output:**
```

2024-01-15 10:30:00 - pipeline - INFO - Starting mean_calculation
2024-01-15 10:30:00 - pipeline - INFO - mean_calculation completed successfully: 3.000
```

### 2.2 Проверка промежуточных результатов

**Пример: Валидация промежуточных результатов**

```python

def validate_intermediate_result(value, expected_range, step_name):
    """Валидация промежуточного результата"""
    min_val, max_val = expected_range
    
    if not (min_val <= value <= max_val):
        raise ValueError(
            f"{step_name}: Value {value} outside expected range [{min_val}, {max_val}]"
        )
    
    print(f"✓ {step_name}: {value} is within expected range")
    return True

# Пример
try:
    result = 15.5
    validate_intermediate_result(result, (10, 20), "temperature_check")
except ValueError as e:
    print(f"Validation failed: {e}")
```

**Output:**
```

✓ temperature_check: 15.5 is within expected range
```

---

## 3. Проверка корректности результатов

### 3.1 Sanity checks

**Sanity checks** — проверки на разумность результатов.

**Пример: Sanity checks**

```python

def sanity_check_results(results):
    """Проверка разумности результатов"""
    checks = []
    
    # Проверка на NaN
    if pd.isna(results).any():
        checks.append("WARNING: NaN values in results")
    
    # Проверка на бесконечность
    if np.isinf(results).any():
        checks.append("WARNING: Infinite values in results")
    
    # Проверка на отрицательные значения (если не ожидаются)
    if (results < 0).any():
        checks.append("WARNING: Negative values found")
    
    # Проверка на неожиданно большие значения
    if (results > 1e6).any():
        checks.append("WARNING: Very large values detected")
    
    return checks

# Пример
results = np.array([1.5, 2.3, np.nan, 1e7, -0.5])
checks = sanity_check_results(results)
for check in checks:
    print(check)
```

**Output:**
```

WARNING: NaN values in results
WARNING: Infinite values in results
WARNING: Negative values found
WARNING: Very large values detected
```

### 3.2 Сравнение с ожидаемыми результатами

**Пример: Сравнение результатов**

```python

def compare_results(actual, expected, tolerance=0.01):
    """Сравнение фактических и ожидаемых результатов"""
    if isinstance(actual, (list, np.ndarray)) and isinstance(expected, (list, np.ndarray)):
        actual = np.array(actual)
        expected = np.array(expected)
        differences = np.abs(actual - expected)
        max_diff = np.max(differences)
        
        if max_diff > tolerance:
            return {
                'match': False,
                'max_difference': max_diff,
                'message': f"Results differ by up to {max_diff:.6f}"
            }
        else:
            return {
                'match': True,
                'max_difference': max_diff,
                'message': "Results match within tolerance"
            }
    else:
        diff = abs(actual - expected)
        return {
            'match': diff <= tolerance,
            'difference': diff,
            'message': f"Match: {diff <= tolerance}, difference: {diff:.6f}"
        }

# Пример
actual = [1.001, 2.002, 3.003]
expected = [1.0, 2.0, 3.0]
comparison = compare_results(actual, expected, tolerance=0.01)
print(comparison['message'])
```

**Output:**
```

Results match within tolerance
```

---

## 4. Performance Bottlenecks

### 4.1 Профилирование

**Профилирование** — выявление медленных частей кода.

**Пример: Простое профилирование**

```python

import time

def profile_function(func, *args, **kwargs):
    """Профилирование функции"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    return {
        'result': result,
        'execution_time': end_time - start_time
    }

# Пример
def slow_function(data):
    """Медленная функция"""
    result = []
    for item in data:
        result.append(item ** 2)
    return result

def fast_function(data):
    """Быстрая функция"""
    return np.array(data) ** 2

data = list(range(100000))

slow_profile = profile_function(slow_function, data)
fast_profile = profile_function(fast_function, data)

print(f"Slow function: {slow_profile['execution_time']:.4f}s")
print(f"Fast function: {fast_profile['execution_time']:.4f}s")
print(f"Speedup: {slow_profile['execution_time'] / fast_profile['execution_time']:.1f}x")
```

**Output:**
```

Slow function: 0.0234s
Fast function: 0.0012s
Speedup: 19.5x
```

### 4.2 Идентификация bottlenecks

**Пример: Поиск узких мест**

```python

def identify_bottlenecks(steps_with_times):
    """Идентификация узких мест в pipeline"""
    total_time = sum(steps_with_times.values())
    
    bottlenecks = []
    for step, time_taken in steps_with_times.items():
        percentage = (time_taken / total_time) * 100
        if percentage > 20:  # Больше 20% от общего времени
            bottlenecks.append({
                'step': step,
                'time': time_taken,
                'percentage': percentage
            })
    
    return sorted(bottlenecks, key=lambda x: x['percentage'], reverse=True)

# Пример
steps = {
    'load_data': 1.0,
    'preprocess': 0.5,
    'analyze': 5.0,  # Узкое место
    'visualize': 0.3
}

bottlenecks = identify_bottlenecks(steps)
print("Performance bottlenecks:")
for b in bottlenecks:
    print(f"  {b['step']}: {b['time']:.2f}s ({b['percentage']:.1f}%)")
```

**Output:**
```

Performance bottlenecks:
  analyze: 5.00s (73.5%)
```

---

## 5. Систематический подход к troubleshooting

### 5.1 Чеклист troubleshooting

**Систематический подход:**

1. **Воспроизвести проблему** — понять, когда она возникает
2. **Изолировать проблему** — найти минимальный пример
3. **Проверить данные** — валидность входных данных
4. **Проверить логи** — найти сообщения об ошибках
5. **Проверить промежуточные результаты** — валидация на каждом шаге
6. **Сравнить с ожидаемым** — sanity checks

**Пример: Troubleshooting framework**

```python

class TroubleshootingFramework:
    """Систематический подход к troubleshooting"""
    
    def __init__(self):
        self.checks = []
    
    def check_data(self, data, step_name):
        """Проверка данных"""
        if data is None:
            self.checks.append(f"❌ {step_name}: Data is None")
            return False
        if hasattr(data, 'shape') and data.shape[0] == 0:
            self.checks.append(f"❌ {step_name}: Empty data")
            return False
        self.checks.append(f"✓ {step_name}: Data OK")
        return True
    
    def check_computation(self, result, expected_range=None):
        """Проверка вычислений"""
        if pd.isna(result):
            self.checks.append("❌ Computation: Result is NaN")
            return False
        if expected_range and not (expected_range[0] <= result <= expected_range[1]):
            self.checks.append(f"❌ Computation: Result {result} outside range")
            return False
        self.checks.append("✓ Computation: OK")
        return True
    
    def get_report(self):
        """Получить отчёт"""
        return "\n".join(self.checks)

# Пример использования
troubleshooter = TroubleshootingFramework()
data = np.array([1, 2, 3, 4, 5])
troubleshooter.check_data(data, "input")
result = np.mean(data)
troubleshooter.check_computation(result, expected_range=(0, 10))
print(troubleshooter.get_report())
```

**Output:**
```

✓ input: Data OK
✓ Computation: OK
```

---

## 💡 Key Takeaways

- **Типовые ошибки** включают проблемы с данными (пропуски, выбросы) и ошибки вычислений (деление на ноль, переполнение)

- **Отладка** требует логирования, проверки промежуточных результатов и систематического подхода

- **Проверка корректности** включает sanity checks и сравнение с ожидаемыми результатами

- **Performance bottlenecks** можно выявить через профилирование и анализ времени выполнения

- **Систематический подход** к troubleshooting помогает быстрее находить и исправлять проблемы

---

## 🚀 Next Steps

**Related Modules:**

- [13_Architecture](../13_Architecture/) — архитектура data-систем
- [15_Optimization](../15_Optimization/) — оптимизация pipelines
- [11_SpecializedTools](../11_SpecializedTools/) — workflow managers

**Practice Ideas:**

1. Добавьте логирование в ваш pipeline
2. Создайте sanity checks для ваших результатов
3. Проведите профилирование вашего кода

**Going Deeper:**

- Изучите продвинутые техники отладки (debugger, tracing)
- Познакомьтесь с инструментами профилирования (cProfile, line_profiler)
- Изучите методы мониторинга production pipelines

---

## 📚 Additional Resources

**Documentation:**

- [Python Logging](https://docs.python.org/3/library/logging.html)
- [cProfile Documentation](https://docs.python.org/3/library/profile.html)

---


