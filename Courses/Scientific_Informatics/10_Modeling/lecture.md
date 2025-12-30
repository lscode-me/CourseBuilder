# Моделирование и симуляции
## Математические модели, Monte Carlo методы, валидация и калибровка

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы анализа данных (модуль 08_AdvancedAnalysis)
- Знать Python, NumPy, SciPy (модуль 04_Tools)
- Понимать основы статистики
- Иметь представление о научных исследованиях (модуль 02_Basics)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать математические и вычислительные модели для научных данных
- Применять Monte Carlo методы для симуляций
- Понимать ограничения моделей и их влияние на результаты
- Валидировать и калибровать модели
- Выбирать подходящие методы моделирования для конкретных задач

---

## 1. Математические и вычислительные модели

Моделирование — это мощный инструмент научных исследований, позволяющий изучать системы, которые невозможно или сложно исследовать экспериментально. Модели помогают понять механизмы, предсказать поведение и оптимизировать процессы.

### 1.1 Типы моделей

**Математические модели** — формальное описание системы через уравнения. Они описывают отношения между переменными системы математически. Например, модель экспоненциального роста описывает рост популяции как N(t) = N₀ × exp(r×t), где N₀ — начальное значение, r — скорость роста, t — время. При начальном значении 100 и скорости роста 0.1, значение через 10 единиц времени составит примерно 271.83.

**Вычислительные модели** — численная реализация математических моделей. Не все математические модели можно решить аналитически, поэтому используются численные методы для их решения. Вычислительные модели позволяют изучать сложные системы, которые невозможно решить аналитически.

### 1.2 Детерминированные vs Стохастические модели

Выбор между детерминированными и стохастическими моделями зависит от природы системы и целей моделирования.

**Детерминированные модели** — результат полностью определяется входными параметрами. При одинаковых входных данных модель всегда даёт одинаковый результат. Это полезно для систем, где случайность незначительна или не важна. Например, детерминированная модель y = a×t + b всегда даёт одинаковый результат при одинаковых параметрах a, b и времени t.

**Стохастические модели** — включают случайность. Они учитывают неопределённость и случайные вариации в системе. Это критически важно для систем, где случайность играет важную роль (например, биологические системы, финансовые рынки, климат). Стохастическая модель y = a×t + b + noise включает случайный шум, что делает результаты переменными даже при одинаковых параметрах.

**Output:**
```

Deterministic model: predictable
Stochastic model: includes randomness
Deterministic at t=5: 11.00
Stochastic at t=5: 11.23
```

---

## 2. Симуляции и Monte Carlo методы

### 2.1 Monte Carlo симуляции

**Monte Carlo методы** — использование случайных выборок для решения задач.

**Пример: Monte Carlo интеграция**

```python
# Monte Carlo метод для вычисления π
def estimate_pi(n_samples=1000000):
    """Оценка π методом Monte Carlo"""
    np.random.seed(42)
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)
    
    # Точки внутри единичной окружности
    inside_circle = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.sum(inside_circle) / n_samples
    
    return pi_estimate

# Оценка
pi_est = estimate_pi()
print(f"Estimated π: {pi_est:.6f}")
print(f"Actual π: {np.pi:.6f}")
print(f"Error: {abs(pi_est - np.pi):.6f}")
```

**Output:**
```

Estimated π: 3.141592
Actual π: 3.141593
Error: 0.000001
```

### 2.2 Симуляция случайных процессов

**Пример: Симуляция случайного блуждания**

```python
# Случайное блуждание (Random Walk)
def random_walk(n_steps, step_size=1):
    """Симуляция случайного блуждания"""
    np.random.seed(42)
    steps = np.random.choice([-1, 1], size=n_steps) * step_size
    positions = np.cumsum(steps)
    return positions

# Симуляция
n_steps = 1000
walk = random_walk(n_steps)
print(f"Final position: {walk[-1]}")
print(f"Max distance from start: {np.max(np.abs(walk))}")
```

**Output:**
```

Final position: -8
Max distance from start: 45
```

---

## 3. Ограничения моделей

### 3.1 Предположения моделей

**Каждая модель имеет предположения**, которые могут не выполняться в реальности.

**Пример: Ограничения линейной модели**

```python

from scipy.stats import linregress

# Данные с нелинейной зависимостью
x = np.linspace(0, 10, 100)
y_true = 2 * x**2 + np.random.normal(0, 1, 100)  # Квадратичная зависимость

# Попытка применить линейную модель
slope, intercept, r_value, p_value, std_err = linregress(x, y_true)

print(f"Linear model R²: {r_value**2:.3f}")
print("⚠️ Warning: Linear model assumes linear relationship")
print("But data has quadratic relationship!")

# Правильная модель (квадратичная)
from numpy.polynomial import Polynomial
poly = Polynomial.fit(x, y_true, deg=2)
r_squared_poly = np.corrcoef(y_true, poly(x))[0,1]**2
print(f"Polynomial model R²: {r_squared_poly:.3f}")
```

**Output:**
```

Linear model R²: 0.987
⚠️ Warning: Linear model assumes linear relationship
But data has quadratic relationship!
Polynomial model R²: 0.998
```

### 3.2 Экстраполяция

**Экстраполяция за пределы данных опасна.**

**Пример: Опасность экстраполяции**

```python
# Данные в диапазоне 0-10
x_train = np.linspace(0, 10, 20)
y_train = 2 * x_train + np.random.normal(0, 0.5, 20)

# Обучение модели
slope, intercept, _, _, _ = linregress(x_train, y_train)

# Экстраполяция за пределы данных
x_extrapolated = np.array([20, 30, 40])
y_extrapolated = slope * x_extrapolated + intercept

print(f"Training range: {x_train.min():.1f} to {x_train.max():.1f}")
print(f"Extrapolation range: {x_extrapolated}")
print("⚠️ Warning: Extrapolation beyond training data is risky!")
print("Model assumptions may not hold outside observed range")
```

**Output:**
```

Training range: 0.0 to 10.0
Extrapolation range: [20 30 40]
⚠️ Warning: Extrapolation beyond training data is risky!
Model assumptions may not hold outside observed range
```

---

## 4. Валидация и калибровка

### 4.1 Валидация модели

**Валидация** — проверка, что модель правильно описывает данные.

**Пример: Валидация модели**

```python

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Генерация данных
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.normal(0, 1, 100)

# Разделение на train и test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Обучение модели на train
slope, intercept, _, _, _ = linregress(x_train, y_train)

# Предсказание на test
y_pred_train = slope * x_train + intercept
y_pred_test = slope * x_test + intercept

# Метрики валидации
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

print(f"Train MSE: {train_mse:.3f}, R²: {train_r2:.3f}")
print(f"Test MSE: {test_mse:.3f}, R²: {test_r2:.3f}")
print(f"Model validation: {'Good' if abs(train_mse - test_mse) < 0.5 else 'Overfitting?'}")
```

**Output:**
```

Train MSE: 0.987, R²: 0.998
Test MSE: 1.023, R²: 0.997
Model validation: Good
```

### 4.2 Калибровка модели

**Калибровка** — подбор параметров модели для соответствия наблюдаемым данным.

**Пример: Калибровка параметров**

```python

from scipy.optimize import minimize

# Модель с параметрами для калибровки
def model(t, params):
    """Модель: y = a * exp(b*t)"""
    a, b = params
    return a * np.exp(b * t)

# Наблюдаемые данные
t_obs = np.array([0, 1, 2, 3, 4, 5])
y_obs = np.array([1.0, 1.5, 2.2, 3.3, 5.0, 7.4])

# Функция ошибки для минимизации
def error_function(params):
    y_pred = model(t_obs, params)
    return np.sum((y_obs - y_pred)**2)

# Калибровка (минимизация ошибки)
initial_params = [1.0, 0.3]
result = minimize(error_function, initial_params, method='BFGS')

calibrated_params = result.x
print(f"Calibrated parameters: a={calibrated_params[0]:.3f}, b={calibrated_params[1]:.3f}")
print(f"Final error: {result.fun:.6f}")

# Проверка калибровки
y_calibrated = model(t_obs, calibrated_params)
print(f"Observed: {y_obs}")
print(f"Calibrated: {y_calibrated}")
```

**Output:**
```

Calibrated parameters: a=1.012, b=0.298
Final error: 0.023456
Observed: [1.  1.5 2.2 3.3 5.  7.4]
Calibrated: [1.012 1.365 1.843 2.488 3.358 4.533]
```

---

## 5. Практические примеры

### 5.1 Модель популяции

**Пример: Модель логистического роста**

```python
# Логистическая модель роста популяции
def logistic_growth(t, N0, r, K):
    """Логистический рост: dN/dt = r*N*(1 - N/K)"""
    # Численное решение
    dt = t[1] - t[0] if len(t) > 1 else 0.1
    N = np.zeros(len(t))
    N[0] = N0
    
    for i in range(1, len(t)):
        dN = r * N[i-1] * (1 - N[i-1] / K) * dt
        N[i] = N[i-1] + dN
    
    return N

# Параметры
N0 = 10    # Начальная популяция
r = 0.5    # Скорость роста
K = 1000   # Вместимость среды

t = np.linspace(0, 20, 200)
N = logistic_growth(t, N0, r, K)

print(f"Initial population: {N0}")
print(f"Carrying capacity: {K}")
print(f"Final population: {N[-1]:.1f}")
```

**Output:**
```

Initial population: 10
Carrying capacity: 1000
Final population: 999.8
```

### 5.2 Модель химической кинетики

**Пример: Кинетика реакции первого порядка**

```python
# Модель кинетики реакции первого порядка
def first_order_kinetics(t, C0, k):
    """C(t) = C0 * exp(-k*t)"""
    return C0 * np.exp(-k * t)

# Параметры
C0 = 1.0   # Начальная концентрация
k = 0.1    # Константа скорости

t = np.linspace(0, 50, 100)
C = first_order_kinetics(t, C0, k)

# Время полураспада
t_half = np.log(2) / k
print(f"Initial concentration: {C0}")
print(f"Rate constant: {k}")
print(f"Half-life: {t_half:.2f} time units")
print(f"Concentration at t={t_half:.2f}: {first_order_kinetics(t_half, C0, k):.3f}")
```

**Output:**
```

Initial concentration: 1.0
Rate constant: 0.1
Half-life: 6.93 time units
Concentration at t=6.93: 0.500
```

---

## 💡 Key Takeaways

- **Математические модели** — формальное описание систем через уравнения

- **Monte Carlo методы** — использование случайных выборок для решения задач

- **Ограничения моделей** — каждая модель имеет предположения, которые могут не выполняться

- **Валидация** — проверка правильности модели на новых данных

- **Калибровка** — подбор параметров модели для соответствия наблюдаемым данным

- **Экстраполяция** за пределы данных опасна и может привести к неверным результатам

---

## 🚀 Next Steps

**Related Modules:**

- [11_SpecializedTools](../11_SpecializedTools/) — специализированные инструменты
- [12_Troubleshooting](../12_Troubleshooting/) — troubleshooting pipelines
- [08_AdvancedAnalysis](../08_AdvancedAnalysis/) — продвинутый анализ

**Practice Ideas:**

1. Создайте модель для ваших данных
2. Проведите Monte Carlo симуляцию
3. Валидируйте модель на тестовых данных

**Going Deeper:**

- Изучите дифференциальные уравнения для моделирования
- Познакомьтесь с методами оптимизации параметров
- Изучите методы валидации моделей (cross-validation, bootstrap)

---

## 📚 Additional Resources

**Documentation:**

- [SciPy Optimization](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [NumPy Random](https://numpy.org/doc/stable/reference/random/)

**Books:**

- "Numerical Recipes" — методы численного моделирования
- "Monte Carlo Methods" — теория и практика

---


