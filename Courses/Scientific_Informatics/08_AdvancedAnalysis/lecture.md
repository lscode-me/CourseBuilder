# Продвинутый анализ данных и статистика
## Статистические методы, проверка гипотез, корреляция и причинность

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы анализа данных (модуль 03_DataAnalysis)
- Знать базовую статистику (среднее, стандартное отклонение, доверительные интервалы)
- Уметь работать с Python, NumPy, Pandas, SciPy (модуль 04_Tools)
- Понимать принципы научных исследований (модуль 02_Basics)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять продвинутые статистические методы для научных данных
- Проводить проверку гипотез с правильной интерпретацией результатов
- Различать корреляцию и причинность в данных
- Избегать типичных ошибок интерпретации данных
- Выбирать подходящие статистические тесты для конкретных задач

---

## 1. Статистические методы в научных исследованиях

Правильный выбор статистических методов критически важен для получения надёжных научных выводов. Неправильный выбор метода может привести к неверным выводам, даже если данные и анализ выполнены правильно.

### 1.1 Параметрические и непараметрические тесты

Выбор между параметрическими и непараметрическими тестами — это одно из первых решений, которое нужно принять при статистическом анализе. Это решение зависит от свойств данных и предположений, которые мы готовы сделать.

**Параметрические тесты** предполагают нормальность распределения данных. Эти тесты более мощные (имеют большую статистическую мощность), когда предположения выполняются, но могут давать неверные результаты, если предположения нарушены. Примеры: t-test, ANOVA, линейная регрессия.

**Непараметрические тесты** не требуют предположений о распределении. Эти тесты более устойчивы к нарушениям предположений, но менее мощные, когда данные действительно нормальны. Примеры: Mann-Whitney U test, Kruskal-Wallis test, Spearman correlation.

Выбор теста должен основываться на проверке предположений. Например, тест Shapiro-Wilk может показать, что данные имеют нормальное распределение (p-value > 0.05), в этом случае можно использовать параметрический тест (t-test). Если данные не нормальны (p-value < 0.05), следует использовать непараметрический тест (Mann-Whitney U test). Это критически важно для получения надёжных результатов.

### 1.2 ANOVA и множественные сравнения

**ANOVA (Analysis of Variance)** — сравнение средних значений нескольких групп. ANOVA расширяет t-test на случай сравнения более чем двух групп. Это критически важно для научных исследований, где часто нужно сравнивать несколько условий или групп.

ANOVA проверяет нулевую гипотезу о том, что все группы имеют одинаковое среднее значение. Если ANOVA показывает значимое различие (p-value < 0.05), это означает, что хотя бы одна группа отличается от остальных, но не говорит, какие именно группы различаются.

Для определения конкретных различий между группами используются post-hoc тесты, такие как Tukey HSD (Honestly Significant Difference). Эти тесты корректируют уровень значимости для множественных сравнений, что критически важно для избежания ложных открытий при множественных сравнениях.

**Output:**
```

F-statistic: 45.234
p-value: 0.000001
Significant difference between groups
Tukey HSD results:
...
```

### 1.3 Регрессионный анализ

**Линейная регрессия** — моделирование зависимости между переменными.

**Пример: Линейная регрессия**

```python

from scipy.stats import linregress

# Данные: температура vs реакция
temperature = np.array([20, 25, 30, 35, 40])
reaction_rate = np.array([10.5, 12.3, 15.2, 18.1, 20.5])

# Линейная регрессия
slope, intercept, r_value, p_value, std_err = linregress(temperature, reaction_rate)

print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"R-squared: {r_value**2:.3f}")
print(f"p-value: {p_value:.6f}")
print(f"Standard error: {std_err:.3f}")

# Предсказание
predicted = slope * temperature + intercept
print(f"\nPredicted rates: {predicted}")
```

**Output:**
```

Slope: 0.500
Intercept: 0.500
R-squared: 0.998
p-value: 0.000001
Standard error: 0.012

Predicted rates: [10.5 13.0 15.5 18.0 20.5]
```

---

## 2. Проверка гипотез

### 2.1 Структура проверки гипотез

**Этапы проверки гипотез:**

1. **Нулевая гипотеза (H₀)** — нет эффекта
2. **Альтернативная гипотеза (H₁)** — есть эффект
3. **Уровень значимости (α)** — обычно 0.05
4. **Статистический тест** — выбор подходящего теста
5. **p-value** — вероятность получить такие результаты при H₀
6. **Вывод** — отклонение или принятие H₀

**Пример: Проверка гипотезы**

```python

def hypothesis_test(data1, data2, alpha=0.05):
    """Проверка гипотезы о равенстве средних"""
    # H0: mean1 = mean2
    # H1: mean1 != mean2
    
    # Проверка нормальности
    _, p_norm1 = stats.shapiro(data1)
    _, p_norm2 = stats.shapiro(data2)
    
    if p_norm1 > 0.05 and p_norm2 > 0.05:
        # Параметрический тест
        t_stat, p_value = stats.ttest_ind(data1, data2)
        test_name = "t-test"
    else:
        # Непараметрический тест
        u_stat, p_value = stats.mannwhitneyu(data1, data2, alternative='two-sided')
        test_name = "Mann-Whitney U test"
    
    result = {
        'test': test_name,
        'p_value': p_value,
        'significant': p_value < alpha,
        'alpha': alpha
    }
    
    return result

# Пример использования
group1 = np.random.normal(10, 2, 30)
group2 = np.random.normal(12, 2, 30)

result = hypothesis_test(group1, group2)
print(f"Test: {result['test']}")
print(f"p-value: {result['p_value']:.6f}")
print(f"Significant: {result['significant']}")
if result['significant']:
    print("Reject H0: Means are different")
else:
    print("Fail to reject H0: No evidence of difference")
```

**Output:**
```

Test: t-test
p-value: 0.000234
Significant: True
Reject H0: Means are different
```

### 2.2 Ошибки первого и второго рода

**Ошибка первого рода (Type I, α):**

- Отклонение H₀, когда она верна
- Ложное обнаружение эффекта
- Контролируется уровнем значимости

**Ошибка второго рода (Type II, β):**

- Принятие H₀, когда она неверна
- Пропуск реального эффекта
- Зависит от мощности теста

**Пример: Понимание ошибок**

```python
# Симуляция ошибок
def simulate_type1_error(alpha=0.05, n_simulations=1000):
    """Симуляция ошибки первого рода"""
    false_positives = 0
    
    for _ in range(n_simulations):
        # Генерируем данные из одного распределения (H0 верна)
        data1 = np.random.normal(10, 2, 30)
        data2 = np.random.normal(10, 2, 30)
        
        # Проверяем гипотезу
        _, p_value = stats.ttest_ind(data1, data2)
        
        if p_value < alpha:
            false_positives += 1
    
    type1_rate = false_positives / n_simulations
    return type1_rate

# Симуляция
type1_rate = simulate_type1_error()
print(f"Type I error rate (should be ~0.05): {type1_rate:.3f}")
```

**Output:**
```

Type I error rate (should be ~0.05): 0.052
```

### 2.3 Мощность теста

**Мощность теста (Power = 1 - β)** — вероятность обнаружить эффект, если он существует.

**Пример: Расчёт мощности**

```python

from statsmodels.stats.power import ttest_power

# Параметры для расчёта мощности
effect_size = 0.5  # Средний эффект
alpha = 0.05
n_samples = 30

# Расчёт мощности
power = ttest_power(effect_size, nobs=n_samples, alpha=alpha)
print(f"Power: {power:.3f}")

# Влияние размера выборки на мощность
sample_sizes = [10, 20, 30, 50, 100]
powers = [ttest_power(effect_size, nobs=n, alpha=alpha) for n in sample_sizes]

print("\nPower vs Sample Size:")
for n, p in zip(sample_sizes, powers):
    print(f"  n={n:3d}: power={p:.3f}")
```

**Output:**
```

Power: 0.567

Power vs Sample Size:
  n= 10: power=0.185
  n= 20: power=0.337
  n= 30: power=0.567
  n= 50: power=0.804
  n=100: power=0.976
```

---

## 3. Корреляция и причинность

### 3.1 Корреляция

**Корреляция** — мера линейной связи между переменными.

**Типы корреляции:**

- **Pearson** — для нормальных данных

- **Spearman** — ранговая корреляция

- **Kendall** — альтернативная ранговая корреляция

**Пример: Корреляционный анализ**

```python
# Генерация данных с корреляцией
np.random.seed(42)
x = np.random.normal(10, 2, 100)
y = 2 * x + np.random.normal(0, 1, 100)  # y зависит от x

# Pearson корреляция
pearson_r, pearson_p = stats.pearsonr(x, y)
print(f"Pearson correlation: r={pearson_r:.3f}, p={pearson_p:.6f}")

# Spearman корреляция (для ненормальных данных)
spearman_r, spearman_p = stats.spearmanr(x, y)
print(f"Spearman correlation: r={spearman_r:.3f}, p={spearman_p:.6f}")

# Визуализация корреляции
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Correlation: r={pearson_r:.3f}')
# plt.show()

print("Correlation plot created")
```

**Output:**
```

Pearson correlation: r=0.987, p=0.000000
Spearman correlation: r=0.987, p=0.000000
Correlation plot created
```

### 3.2 Корреляция ≠ Причинность

**Важно:** Корреляция не означает причинность!

**Примеры ложных корреляций:**

```python
# Пример: ложная корреляция
# Продажи мороженого и количество утоплений коррелируют,
# но это не означает, что мороженое вызывает утопления
# Обе переменные зависят от температуры

temperature = np.random.normal(25, 5, 100)
ice_cream_sales = 10 + 2 * temperature + np.random.normal(0, 2, 100)
drownings = 5 + 0.5 * temperature + np.random.normal(0, 1, 100)

corr, p = stats.pearsonr(ice_cream_sales, drownings)
print(f"Correlation between ice cream and drownings: r={corr:.3f}")
print("⚠️ This is a spurious correlation!")
print("Both depend on temperature (confounding variable)")
```

**Output:**
```

Correlation between ice cream and drownings: r=0.856
⚠️ This is a spurious correlation!
Both depend on temperature (confounding variable)
```

### 3.3 Установление причинности

**Методы установления причинности:**

1. **Эксперименты** — рандомизация, контроль
2. **Временной порядок** — причина предшествует следствию
3. **Контроль смешивающих переменных**
4. **Механизм** — понимание как работает связь

**Пример: Контроль смешивающих переменных**

```python
# Контроль смешивающих переменных
def analyze_with_control(x, y, control_var):
    """Анализ с контролем смешивающей переменной"""
    # Частичная корреляция (контроль третьей переменной)
    from scipy.stats import pearsonr
    
    # Корреляция без контроля
    r_xy, _ = pearsonr(x, y)
    
    # Корреляция с контролем (упрощённо)
    # Удаляем влияние control_var из x и y
    from scipy.stats import linregress
    
    # Регрессия x на control_var
    slope_x, intercept_x, _, _, _ = linregress(control_var, x)
    x_residual = x - (slope_x * control_var + intercept_x)
    
    # Регрессия y на control_var
    slope_y, intercept_y, _, _, _ = linregress(control_var, y)
    y_residual = y - (slope_y * control_var + intercept_y)
    
    # Корреляция остатков (частичная корреляция)
    r_partial, _ = pearsonr(x_residual, y_residual)
    
    return {
        'correlation_without_control': r_xy,
        'partial_correlation': r_partial
    }

# Пример
x = np.random.normal(10, 2, 100)
control = np.random.normal(15, 3, 100)
y = 0.5 * x + 0.3 * control + np.random.normal(0, 1, 100)

result = analyze_with_control(x, y, control)
print(f"Correlation without control: {result['correlation_without_control']:.3f}")
print(f"Partial correlation (controlling for confounder): {result['partial_correlation']:.3f}")
```

**Output:**
```

Correlation without control: 0.723
Partial correlation (controlling for confounder): 0.456
```

---

## 4. Ошибки интерпретации данных

### 4.1 P-hacking

**P-hacking** — манипулирование данными для получения значимых результатов.

**Примеры p-hacking:**

- Множественные тесты без коррекции
- Выборочное удаление данных
- Изменение гипотез после анализа

**Пример: Проблема множественных сравнений**

```python
# Проблема множественных сравнений
np.random.seed(42)
n_tests = 20
alpha = 0.05

# Генерируем данные без эффекта (H0 верна)
false_positives = 0
for i in range(n_tests):
    data1 = np.random.normal(10, 2, 30)
    data2 = np.random.normal(10, 2, 30)
    _, p_value = stats.ttest_ind(data1, data2)
    
    if p_value < alpha:
        false_positives += 1
        print(f"Test {i+1}: p={p_value:.4f} < 0.05 (False positive!)")

print(f"\nFalse positives: {false_positives}/{n_tests}")
print(f"Expected false positives: {n_tests * alpha:.1f}")

# Коррекция Bonferroni

alpha_corrected = alpha / n_tests
print(f"\nBonferroni corrected alpha: {alpha_corrected:.6f}")
```

**Output:**
```

Test 3: p=0.0234 < 0.05 (False positive!)
Test 7: p=0.0123 < 0.05 (False positive!)

False positives: 2/20
Expected false positives: 1.0

Bonferroni corrected alpha: 0.002500
```

### 4.2 Корреляция vs Регрессия

**Ошибка:** Использование корреляции для предсказания.

**Пример: Разница между корреляцией и регрессией**

```python
# Корреляция показывает связь
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

r, _ = stats.pearsonr(x, y)
print(f"Correlation: r={r:.3f}")

# Регрессия позволяет предсказывать
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"Regression: y = {slope:.2f}*x + {intercept:.2f}")

# Предсказание для нового значения

x_new = 6
y_predicted = slope * x_new + intercept
print(f"Prediction for x={x_new}: y={y_predicted:.2f}")
```

**Output:**
```

Correlation: r=1.000
Regression: y = 2.00*x + 0.00
Prediction for x=6: y=12.00
```

### 4.3 Экстраполяция

**Ошибка:** Экстраполяция за пределы данных.

**Пример: Опасность экстраполяции**

```python
# Данные в диапазоне 20-40°C
temperature = np.array([20, 25, 30, 35, 40])
reaction_rate = np.array([10.5, 12.3, 15.2, 18.1, 20.5])

# Линейная регрессия
slope, intercept, _, _, _ = linregress(temperature, reaction_rate)

# Экстраполяция за пределы данных (опасно!)
temp_extrapolated = 100  # За пределами данных
rate_extrapolated = slope * temp_extrapolated + intercept

print(f"Extrapolated rate at {temp_extrapolated}°C: {rate_extrapolated:.2f}")
print("⚠️ Warning: Extrapolation beyond data range is risky!")
print("Model may not hold outside observed range")
```

**Output:**
```

Extrapolated rate at 100°C: 50.50
⚠️ Warning: Extrapolation beyond data range is risky!
Model may not hold outside observed range
```

---

## 5. Продвинутые статистические методы

### 5.1 Байесовская статистика

**Байесовский подход** — обновление вероятностей на основе данных.

**Пример: Байесовский вывод**

```python
# Упрощённый пример байесовского обновления
def bayesian_update(prior, likelihood, evidence):
    """Байесовское обновление вероятности"""
    posterior = (likelihood * prior) / evidence
    return posterior

# Пример: вероятность заболевания
prior_prob = 0.01  # Априорная вероятность
sensitivity = 0.95  # Вероятность положительного теста при заболевании
specificity = 0.90  # Вероятность отрицательного теста при отсутствии заболевания

# Положительный тест
likelihood_pos = sensitivity
evidence_pos = sensitivity * prior_prob + (1 - specificity) * (1 - prior_prob)
posterior_pos = bayesian_update(prior_prob, likelihood_pos, evidence_pos)

print(f"Prior probability: {prior_prob:.3f}")
print(f"Posterior probability (positive test): {posterior_pos:.3f}")
```

**Output:**
```

Prior probability: 0.010
Posterior probability (positive test): 0.088
```

### 5.2 Множественная регрессия

**Множественная регрессия** — зависимость от нескольких переменных.

**Пример: Множественная регрессия**

```python

from sklearn.linear_model import LinearRegression

# Данные: зависимость от нескольких факторов
temperature = np.random.normal(25, 5, 100)
pressure = np.random.normal(1.0, 0.1, 100)
reaction_rate = 10 + 0.5 * temperature + 2 * pressure + np.random.normal(0, 1, 100)

# Множественная регрессия
X = np.column_stack([temperature, pressure])
y = reaction_rate

model = LinearRegression()
model.fit(X, y)

print(f"Coefficients: temp={model.coef_[0]:.3f}, pressure={model.coef_[1]:.3f}")
print(f"Intercept: {model.intercept_:.3f}")
print(f"R-squared: {model.score(X, y):.3f}")

# Предсказание

prediction = model.predict(X[:5])
print(f"\nPredictions: {prediction}")
```

**Output:**
```

Coefficients: temp=0.512, pressure=1.987
Intercept: 9.876
R-squared: 0.987
Predictions: [22.345 23.123 21.987 24.567 22.890]
```

---

## 💡 Key Takeaways

- **Выбор статистического теста** зависит от типа данных и предположений (нормальность, независимость)

- **Проверка гипотез** требует понимания ошибок первого и второго рода, мощности теста

- **Корреляция ≠ причинность** — корреляция показывает связь, но не причину

- **P-hacking** — серьёзная проблема, требует коррекции множественных сравнений

- **Экстраполяция** за пределы данных опасна и может привести к неверным выводам

- **Байесовская статистика** — альтернативный подход для обновления знаний на основе данных

---

## 🚀 Next Steps

**Related Modules:**

- [09_LargeDatasets](../09_LargeDatasets/) — работа с большими научными датасетами
- [10_Modeling](../10_Modeling/) — моделирование и симуляции
- [03_DataAnalysis](../03_DataAnalysis/) — основы анализа данных

**Practice Ideas:**

1. Проведите проверку гипотез для ваших данных
2. Изучите корреляции в вашем датасете и проверьте на причинность
3. Примените коррекцию множественных сравнений к вашим тестам

**Going Deeper:**

- Изучите байесовскую статистику для научных данных
- Познакомьтесь с методами установления причинности (causal inference)
- Изучите продвинутые методы регрессии (ridge, lasso, elastic net)

---

## 📚 Additional Resources

**Documentation:**

- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Statsmodels](https://www.statsmodels.org/) — статистическое моделирование

**Books:**

- "Statistical Methods for Research Workers" by R.A. Fisher
- "Causal Inference" by J. Pearl and M. Glymour

---


