# Approximate Data Structures
## HyperLogLog, Bloom Filter, Count-Min Sketch и T-Digest

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **Hashing**: Понимать хеш-функции.

- **Probability**: Знать основы теории вероятностей (что такое коллизия, равномерное распределение).

- **Big Data context**: Понимать, что хранить 1 миллиард ID пользователей в `HashSet` — это дорого (8-10 ГБ RAM).

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Trade-offs**: Понимать, когда можно жертвовать точностью (Analytic) ради памяти (12 KB вместо 8 GB), а когда нельзя (Billing).

- **Count Distinct**: Использовать HyperLogLog для подсчета уникальных посетителей с ошибкой 0.81%.

- **Membership**: Использовать Bloom Filter и Cuckoo Filter, чтобы узнать "видел ли я этот URL раньше?".

- **Frequency**: Использовать Count-Min Sketch для поиска Top-K элементов (Heavy Hitters) в потоке.

- **Quantiles**: Использовать t-Digest для расчета 99-го перцентиля (P99) latency без сохранения всех значений.

- **Similarity**: Использовать SimHash/MinHash для поиска похожих документов (Near-Duplicate Detection).

---

## 1. Зачем нам неточные данные?

Представьте, вы Google. Вы хотите посчитать "Сколько уникальных поисковых запросов было сегодня?".
Всего запросов: 10 миллиардов.
Уникальных: допустим, 1 миллиард.

**Exact Soluton (HashSet)**:
Каждый запрос ~20 байт (среднее).
1 млрд х 20 байт = 20 ГБ RAM.
Вам нужен сервер с 32+ ГБ RAM только для одного счетчика. А если нужно разбить по странам? 200 стран * 20 ГБ = 4 ТБ RAM. Нереально.

**Probabilistic Solution (HyperLogLog)**:
Память: 12 КБ (Килобайт!).
Ошибка: 0.81% (стандартная).
12 KB * 200 = 2.4 МБ. Это влезает в L1 кэш процессора.

Экономия ресурсов: в **миллион раз**.
Цена: Мы скажем "Примерно 1,005,320 юзеров" вместо "Ровно 1,000,000".
Для аналитики это приемлемо.

---

## 2. HyperLogLog (HLL): Магия подсчета

Алгоритм, придуманный Филиппом Флажоле.

### 2.1 Интуиция (Подбрасывание монетки)

Представьте, что вы хешируете ID пользователя в битовую строку.
Хеш-функция выдает `0` и `1` с вероятностью 50%. Это как бросать монетку.
`01...` — 50%
`001...` — 25% (два орла подряд)
`0001...` — 12.5%
...
`00...01` (k нулей) — $1 / 2^k$.

Если я скажу вам: "Я видел хеш, который начинается с 10 нулей", вы можете предположить, сколько элементов я видел?
Чтобы получить 10 нулей подряд, нужно (в среднем) сделать $2^{10} = 1024$ попыток.
Значит, Cardinality $\approx 2^{max\_zeros}$.

### 2.2 Bucketing & Harmonic Mean (Борьба с дисперсией)

Один хеш дает огромную дисперсию ("повезло" получить 50 нулей сразу, хотя элемент один).
HLL делит поток на `m` корзин (buckets).
Берет первые несколько бит хеша как индекс корзины.
Считает `max_zeros` в каждой корзине отдельно.
Усредняет результаты.

**Почему Harmonic Mean?**
Арифметическое среднее чувствительно к выбросам (один "Lucky Hash" с 60 нулями испортит все).
Гармоническое среднее подавляет выбросы.

Формула ошибки: $1.04 / \sqrt{m}$.
Для Redis (16384 регистра): $1.04 / \sqrt{16384} = 1.04 / 128 \approx 0.81\%$.

### 2.3 Implementation Logic (Python style)

```python
import hashlib
import math

class SimpleHLL:
    def __init__(self, b=10):
        self.b = b # bits for bucket indexing (2^10 = 1024 registers)
        self.m = 1 << b 
        self.buckets = [0] * self.m

    def _trailing_zeros(self, x):
        s = bin(x)[2:] 
        return len(s) - len(s.rstrip('0'))

    def add(self, item):
        h = int(hashlib.md5(item.encode('utf-8')).hexdigest(), 16)
        
        # Первые b бит - номер корзины
        bucket_idx = h & (self.m - 1)
        
        # Остальные биты - для подсчета нулей
        w = h >> self.b
        # Паттерн: Нам нужно положение самого правого бита 1
        # Для простоты используем trailing zeros logic
        zeros = self._trailing_zeros(w) + 1
        
        self.buckets[bucket_idx] = max(self.buckets[bucket_idx], zeros)

    def count(self):
        # Harmonic Mean formula (Simplified by Flajolet)
        alpha = 0.7213 / (1 + 1.079 / self.m)
        z = sum(2**-reg for reg in self.buckets)
        raw_estimate = alpha * (self.m ** 2) / z
        
        # Small range correction (Linear Counting)
        if raw_estimate <= 2.5 * self.m:
            zeros = self.buckets.count(0)
            if zeros > 0:
                return int(self.m * math.log(self.m / zeros))
                
        return int(raw_estimate)

# Test

hll = SimpleHLL(b=12) # 4096 buckets
truth = 100000
for i in range(truth):
    hll.add(f"user_{i}")

est = hll.count()
error = abs(est - truth) / truth * 100
print(f"True: {truth}, Est: {est}, Error: {error:.2f}%")
```

---

## 3. Bloom Filter: "Я это уже видел?"

Вероятностное множество (Set).

*   Space efficient.
*   Operations: `add()`, `contains()`.
*   **False Positive**: Возможен (скажет "Да", хотя элемента нет).

*   **False Negative**: Невозможен (если сказал "Нет", значит точно нет).

### 3.1 Механика

Массив битов размера `M`. И `k` хеш-функций.
`add("hello")`:
1.  H1("hello") % M -> 5. bit[5] = 1.
2.  H2("hello") % M -> 12. bit[12] = 1.
3.  H3("hello") % M -> 23. bit[23] = 1.

`contains("hello")`:
Проверяем биты 5, 12, 23. Все единицы? Значит, "Наверное, есть".
`contains("world")`:
H1("world") -> 5 (Коллизия с hello!).
H2("world") -> 99 (Там 0).
Один из битов 0? Ответ: "Точно нет".

### 3.2 False Positive Probability

Чем больше мы добавляем элементов, тем больше массив заполняется единицами.
В какой-то момент для нового слова "world" все его хеши случайно попадут в биты, установленные другими словами. Это False Positive.
Формула для выбора размера: $M = - (n \ln P) / (\ln 2)^2$.
Где $P$ — желаемая вероятность ошибки (напр. 0.01).

### 3.3 Deletions (Проблема удаления)

Из обычного Bloom Filter нельзя удалять. Если вы обнулите бит №5 для удаления "hello", вы можете случайно "покалечить" другое слово, которое тоже использовало бит №5.
Решение: **Counting Bloom Filter** (хранить не биты, а счетчики). Но это занимает в 8-16 раз больше места.
Или **Cuckoo Filter** (более современный аналог).

**Counting Bloom Filter:**

```python
class CountingBloomFilter:
    """Bloom Filter с поддержкой удаления."""
    
    def __init__(self, m, k):
        self.m = m  # Размер массива
        self.k = k  # Количество хеш-функций
        self.counters = [0] * m  # Счетчики вместо битов
    
    def _hash(self, item, seed):
        """Хеш-функция с seed."""
        import hashlib
        h = hashlib.md5(f"{item}{seed}".encode()).hexdigest()
        return int(h, 16) % self.m
    
    def add(self, item):
        """Добавление элемента."""
        for i in range(self.k):
            idx = self._hash(item, i)
            self.counters[idx] += 1
    
    def remove(self, item):
        """Удаление элемента."""
        for i in range(self.k):
            idx = self._hash(item, i)
            if self.counters[idx] > 0:
                self.counters[idx] -= 1
    
    def contains(self, item):
        """Проверка наличия элемента."""
        for i in range(self.k):
            idx = self._hash(item, i)
            if self.counters[idx] == 0:
                return False
        return True

# Пример использования

cbf = CountingBloomFilter(m=1000, k=3)
cbf.add("hello")
cbf.add("world")

print(cbf.contains("hello"))  # True
print(cbf.contains("world"))  # True
print(cbf.contains("test"))   # False (или True с вероятностью false positive)

cbf.remove("hello")
print(cbf.contains("hello"))  # False (корректно удалено)
```

**Cuckoo Filter (более эффективный):**

```python
class CuckooFilter:
    """Cuckoo Filter - более эффективная альтернатива Counting Bloom Filter."""
    
    def __init__(self, capacity, bucket_size=4, fingerprint_size=8):
        self.capacity = capacity
        self.bucket_size = bucket_size
        self.fingerprint_size = fingerprint_size
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
    
    def _fingerprint(self, item):
        """Вычисление отпечатка элемента."""
        import hashlib
        h = hashlib.md5(item.encode()).hexdigest()
        return int(h[:self.fingerprint_size], 16)
    
    def _hash1(self, item):
        """Первая хеш-функция."""
        import hashlib
        h = hashlib.md5(item.encode()).hexdigest()
        return int(h, 16) % self.capacity
    
    def _hash2(self, fingerprint, hash1):
        """Вторая хеш-функция (альтернативная позиция)."""
        return (hash1 ^ self._hash(str(fingerprint))) % self.capacity
    
    def add(self, item):
        """Добавление элемента."""
        fp = self._fingerprint(item)
        h1 = self._hash1(item)
        h2 = self._hash2(fp, h1)
        
        # Пробуем вставить в первую позицию
        if len(self.buckets[h1]) < self.bucket_size:
            self.buckets[h1].append(fp)
            self.size += 1
            return True
        
        # Пробуем вторую позицию
        if len(self.buckets[h2]) < self.bucket_size:
            self.buckets[h2].append(fp)
            self.size += 1
            return True
        
        # Обе позиции заняты - вытесняем (cuckoo)
        # Упрощенная версия - в реальности нужна рекурсия
        return False
    
    def contains(self, item):
        """Проверка наличия."""
        fp = self._fingerprint(item)
        h1 = self._hash1(item)
        h2 = self._hash2(fp, h1)
        
        return fp in self.buckets[h1] or fp in self.buckets[h2]
    
    def remove(self, item):
        """Удаление элемента."""
        fp = self._fingerprint(item)
        h1 = self._hash1(item)
        h2 = self._hash2(fp, h1)
        
        if fp in self.buckets[h1]:
            self.buckets[h1].remove(fp)
            self.size -= 1
            return True
        elif fp in self.buckets[h2]:
            self.buckets[h2].remove(fp)
            self.size -= 1
            return True
        return False
```

---

## 4. Count-Min Sketch: Топ Посещаемых (Frequency)

Задача: Кто самые активные пользователи? (Heavy Hitters).
HashTable (HashMap) съест память. CMS работает с константной памятью.
Это "Bloom Filter со счетчиками".

### 4.1 Алгоритм

Матрица $d \times w$ (строки x ширину).
`add(x)`: Инкрементируем `Matrix[i][Hi(x)]` для всех $i=0..d$.
`estimate(x)`: Возвращаем `min(Matrix[i][Hi(x)])`.
Почему минимум? Потому что коллизии могут только *увеличить* счетчик. Минимум — это верхняя граница истинного значения.

### 4.2 Conservative Update

Оптимизация: когда делаем `add(x)`, мы сначала читаем значения. Инкрементируем только те ячейки, которые *меньше* остальных. Это уменьшает завышение.

**Реализация Count-Min Sketch:**

```python
import hashlib
import random

class CountMinSketch:
    """Count-Min Sketch для подсчета частоты элементов."""
    
    def __init__(self, width=1000, depth=5):
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]
        self.hash_seeds = [random.randint(0, 2**32) for _ in range(depth)]
    
    def _hash(self, item, seed):
        """Хеш-функция для элемента."""
        h = hashlib.md5(f"{item}{seed}".encode()).hexdigest()
        return int(h, 16) % self.width
    
    def add(self, item, count=1):
        """Добавление элемента."""
        for i in range(self.depth):
            idx = self._hash(item, self.hash_seeds[i])
            self.table[i][idx] += count
    
    def estimate(self, item):
        """Оценка частоты элемента."""
        estimates = []
        for i in range(self.depth):
            idx = self._hash(item, self.hash_seeds[i])
            estimates.append(self.table[i][idx])
        
        # Возвращаем минимум (наименьшее завышение)
        return min(estimates)
    
    def conservative_update(self, item, count=1):
        """Conservative Update: инкрементируем только минимальные ячейки."""
        estimates = []
        for i in range(self.depth):
            idx = self._hash(item, self.hash_seeds[i])
            estimates.append((self.table[i][idx], i, idx))
        
        # Находим минимальное значение
        min_val = min(estimates, key=lambda x: x[0])[0]
        
        # Инкрементируем только ячейки с минимальным значением
        for val, i, idx in estimates:
            if val == min_val:
                self.table[i][idx] += count

# Пример использования

cms = CountMinSketch(width=1000, depth=5)

# Добавляем элементы

for _ in range(100):
    cms.add("apple")
for _ in range(50):
    cms.add("banana")
for _ in range(25):
    cms.add("cherry")

# Оценка частоты

print(f"Apple: {cms.estimate('apple')}")    # ~100
print(f"Banana: {cms.estimate('banana')}")  # ~50
print(f"Cherry: {cms.estimate('cherry')}")  # ~25
```

**Top-K Heavy Hitters:**

```python
class HeavyHitters:
    """Поиск Top-K наиболее частых элементов."""
    
    def __init__(self, k, width=1000, depth=5):
        self.k = k
        self.cms = CountMinSketch(width, depth)
        self.candidates = {}  # item -> estimated_count
    
    def add(self, item):
        """Добавление элемента."""
        self.cms.add(item)
        estimate = self.cms.estimate(item)
        
        # Обновляем кандидатов
        if item in self.candidates:
            self.candidates[item] = estimate
        elif len(self.candidates) < self.k:
            self.candidates[item] = estimate
        else:
            # Если оценка больше минимальной в кандидатах
            min_candidate = min(self.candidates.items(), key=lambda x: x[1])
            if estimate > min_candidate[1]:
                del self.candidates[min_candidate[0]]
                self.candidates[item] = estimate
    
    def get_top_k(self):
        """Получение Top-K элементов."""
        return sorted(self.candidates.items(), key=lambda x: x[1], reverse=True)

# Пример

hh = HeavyHitters(k=3)
items = ["apple"] * 100 + ["banana"] * 50 + ["cherry"] * 25 + ["date"] * 10

for item in items:
    hh.add(item)

top = hh.get_top_k()
print(top)  # [('apple', ~100), ('banana', ~50), ('cherry', ~25)]
```

---

## 5. T-Digest: Перцентили (Quantiles)

Задача: Посчитать P99 latency.
Среднее (Mean) врет. Вам нужно распределение.
T-Digest (Ted Dunning) строит адаптивную гистограмму.

*   Он кластеризует близкие точки в "Центроиды".
*   Точность адаптивна: высокая на краях (tails) — P99, P99.9, P0.1, и низкая в центре (P50).
*   Это идеально для SLA мониторинга, где нам важны именно экстремальные выбросы.
*   Они **Mergeable**: можно сложить T-Digest с 1000 серверов и получить точный глобальный P99.

---

## 6. SimHash: Поиск дубликатов (LSH)

Задача: Найти похожие статьи в Википедии.
Обычный хеш (MD5) лавинообразен: изменение 1 бита меняет весь хеш.
Нам нужен **Locality Sensitive Hashing (LSH)**: похожие входы дают похожие хеши.

### 6.1 SimHash (Google)

1.  Разбиваем текст на слова (фичи).
2.  Хешируем каждое слово (64 бита).
3.  Создаем вектор V [64] из нулей.
4.  Для каждого слова и каждого бита его хеша:
    *   Если бит=1, прибавляем вес слова к V[i].
    *   Если бит=0, вычитаем.
5.  Финал: если V[i] > 0 -> 1, иначе -> 0.

Теперь Hamming Distance между хешами пропорциональна косинусному расстоянию между текстами.
Если хеши отличаются на 3 бита — тексты почти копии.

---

## 7. Glossary

*   **Cardinality**: Мощность множества (количество уникальных элементов).

*   **Probabilistic Data Structures**: Структуры, дающие приближенный ответ с контролируемой ошибкой.

*   **False Positive**: Система говорит "Да", а на самом деле "Нет".

*   **False Negative**: Система говорит "Нет", а на самом деле "Да". (Bloom Filter не имеет FN).

*   **Heavy Hitters**: Элементы с высокой частотой (Top-K).

*   **Quantile / Percentile**: Значение, ниже которого падает X% наблюдений.

*   **Mergeable**: Свойство структуры, позволяющее объединять результаты с разных шардов без потери точности (HLL, T-Digest, CMS — mergeable).

*   **Reservoir Sampling**: Алгоритм выбора K случайных элементов из потока неизвестной длины.

*   **Leading Zeros**: Количество нулей в начале бинарного представления (основа HLL).

*   **Linear Counting**: Алгоритм подсчета уников для малых множеств (использует битовую карту). HLL переключается на него при малом N.

---

## 📚 Appendix A: Troubleshooting Guide

### A.1 Symptom: HLL Error > 10%

**Причина**:
1.  **Low Cardinality**: Вы используете HLL для подсчета 5 уников. На малых числах ошибка выше (нужен Bias Correction / Linear Counting).
2.  **Bad Hash**: Если ваши ID это "1, 2, 3", а хеш-функция слабая (Identity), у вас будут проблемы. Всегда используйте MurmurHash или xxHash перед HLL.

### A.2 Symptom: Bloom Filter saturated

**Симптом**: Фильтр начал говорить "Да" на всё.
**Причина**: Он переполнился. Вы рассчитывали на 1M, вставили 10M. Все биты стали единицами.
**Лечение**: Scalable Bloom Filters. Это цепочка фильтров (BF1 -> BF2 -> BF3). Когда BF1 полн, создаем BF2 (x2 размера). При поиске проверяем все.

---

## 📚 Appendix B: Historical Context

### Philippe Flajolet (1948-2011)

Французский ученый, отец "Analytic Combinatorics".
В 1983 году придумал **Probabilistic Counting**.
В 2007 году (незадолго до смерти) улучшил его до **HyperLogLog**.
Он показал миру, что Big Data можно обрабатывать на калькуляторе.

### Google & Bloom Filters

Google BigTable использует Bloom Filters, чтобы не делать чтение с диска (SSTable), если ключа там нет. Без этого BigTable был бы в 10 раз медленнее на чтение несуществующих ключей.

---

## 📚 Appendix C: FAQ (Часто задаваемые вопросы)

**Q1: Можно ли использовать HLL для биллинга (платить авторам за просмотры)?**
**A**: Нет. Автор обидится, если вы насчитаете ему на 1% меньше денег. Используйте точный `COUNT(DISTINCT)` или `HyperLogLog++` с 64-битной точностью, но лучше всё же `uniq`. Approximate — для аналитики, трендов, мониторинга.

**Q2: Как работает удаление в Cuckoo Filter?**
**A**: Cuckoo Filter хранит "отпечатки" (fingerprints) в хеш-таблице. При удалении он находит отпечаток и удаляет его. В отличие от Bloom Filter, где биты "размазаны", здесь есть четкое место для элемента.

**Q3: Что лучше: Redis HyperLogLog или ElasticSearch cardinality agg?**
**A**: Оба используют HLL внутри. Redis хранит структуру в памяти (быстро обновлять). Elastic строит её на лету при запросе (или использует precomputed). Результат одинаков.

**Q4: Почему Count-Min Sketch не используется повсеместно вместо HashMap?**
**A**: Он не хранит *сами ключи*. Он отвечает на вопрос "Сколько раз встречался X?", если вы спросите про X. Но он не может сказать "Дай список всех ключей, которые встречались". Вам нужен отдельный список ключей.

---

## 💡 Key Takeaways

1.  **Accept Uncertainty**: Погрешность в 1% позволяет сэкономить 99% денег. Это отличная сделка для инженерии.
2.  **Additivity**: HLL и T-Digest можно складывать. Это делает их идеальными для распределенных систем (MapReduce).
3.  **Space-Time Tradeoff**: Мы меняем Память на Точность (и немного на CPU для хеширования).
4.  **False Positives are OK**: Bloom Filter может дать ложные срабатывания, но никогда не пропустит существующий элемент.
5.  **Mergeable Structures**: HLL, T-Digest, CMS можно объединять с разных серверов без потери точности.

---

## 🚀 Next Steps

**Практика:**

1.  В Redis: `PFADD hll_key user1`.
2.  Вставьте 1000 уников скриптом.
3.  `PFCOUNT hll_key`. Сравните с 1000.
4.  `DEBUG OBJECT hll_key` -> посмотрите `serializedlength`. Будет смешно мало.

В следующем (заключительном) модуле мы применим все эти знания для разбора реальных **Case Studies** проектирования систем. [Case Studies](../16_Case_Studies/).



