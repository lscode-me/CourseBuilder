# Приближенные структуры данных
## Bloom Filters, HyperLogLog и Count-Min Sketch

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать, что такое хеш-функция и коллизии
- Понимать понятие Bitset (битовая карта)
- Знать ограничения RAM (почему нельзя хранить 1 миллиард ID в set)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять принцип работы Bloom Filter и HyperLogLog
- Понимать компромисс "Точность vs Память"
- Использовать вероятностные структуры для оптимизации больших систем (Big Data)

---

## 1. Зачем нужна неточность?

В Computer Science мы привыкли к точности. `Set` либо содержит элемент, либо нет.
Но что, если у нас **10 миллиардов url** (Google Crawler), и мы хотим знать, посещали ли мы уже этот url?

*   Хранить в `HashSet` (строки по 100 байт): 10 млрд * 100 байт = **1 ТБ RAM**. Это дорого.
*   Хранить на диске: Медленно (Random I/O).

Решение: **Probabilistic Data Structures**.
Мы используем **мало памяти** (МБ вместо ГБ) и получаем ответ с **маленькой погрешностью**.

---

## 2. Bloom Filter (Фильтр Блума)

**Задача**: Проверка принадлежности множеству (Membership Query). "Есть ли X в наборе Y?".
**Ответы**:
1.  "Точно НЕТ".
2.  "Возможно ДА" (False Positive с вероятностью $P$).

### 2.1 Алгоритм

1.  Берем битовый массив `B` длины $M$ (все 0).
2.  Берем $K$ независимых хеш-функций.
3.  **Add(item)**: Хешируем item $K$ раз. Получаем позиции. Ставим там 1.
4.  **Check(item)**: Хешируем item. Если **все** биты на позициях равны 1 — возвращаем "Возможно ДА". Если хоть один 0 — "Точно НЕТ".

### 2.2 Пример

Array: `[0, 0, 0, 0, 0, 0, 0, 0]`
Hash1("cat") -> 1, Hash2("cat") -> 4.
Set: `[0, 1, 0, 0, 1, 0, 0, 0]`

Check("dog") -> Hash1: 2 (бит 0), Hash2: 4 (бит 1).
Видим 0 на позиции 2 -> **Точно НЕТ**.

Check("mouse") -> Hash1: 1 (бит 1), Hash2: 4 (бит 1).
Видим все 1 -> **Возможно ДА**. (Хотя "mouse" мы не добавляли — это коллизия / False Positive).

### 2.3 Применение

*   **Databases (Cassandra, Postgres)**: Перед чтением с диска проверь Bloom Filter. Если "Нет" — не читай диск. Экономит 90% I/O.

*   **Web Browsers**: Список вредоносных URL. Если "Возможно ДА" — сделай запрос к серверу Google для точной проверки.

---

## 3. HyperLogLog (HLL)

**Задача**: Подсчет уникальных элементов (Cardinality Estimation). "Сколько уникальных IP заходило на сайт?".
Точное решение (`Set.size`) требует памяти $O(N)$.
HLL требует $O(1)$ памяти (~12 КБ для подсчета миллиардов).
Погрешность: ~0.81%.

### 3.1 Алгоритм (Идея)

Если у нас есть хорошие случайные хеши (равномерное распределение), то максимальное количество нулей в начале бинарного хеша говорит о размере множества.

*   `hash(x) = ...001` (вероятность 1/8)
*   `hash(x) = ...000001` (вероятность 1/64)
Если мы видим хеш с 10 нулями, значит, мы видели примерно $2^{10}$ элементов.

HyperLogLog делит поток на регистры и усредняет показатели (Harmonic Mean), чтобы убрать выбросы.

### 3.2 Применение

*   **Redis**: Команда `PFCOUNT`.

*   **Analytics**: Data warehousing (Presto, BigQuery) используют HLL для `COUNT(DISTINCT)`.

---

## 4. Count-Min Sketch

**Задача**: Частота элементов (Frequency Lookups). "Сколько раз видео X посмотрели на Youtube?". "Топ-10 запросов".
Точное решение (`HashMap<ID, Counter>`) требует памяти для всех ключей.
CM Sketch требует фиксированную матрицу.

### 4.1 Алгоритм

Матрица $D \times W$. $D$ хеш-функций.

**Add(x)**: Инкрементируем счетчик в каждой строке на позиции `hash_i(x)`.
**Get(x)**: Берем `min` из всех ячеек, куда мапится `x` (потому что из-за коллизий значение может быть только *завышено*, но не занижено).

### 4.2 Свойства

*   Может завышать частоту (Overestimation).
*   Никогда не занижает.
*   Хорош для поиска "Heavy Hitters" (топ популярных).

---

## 5. Демонстрация: Bloom Filter на Python

```python

import mmh3 # MurmurHash3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for i in range(self.hash_count):
            digest = mmh3.hash(string, i) % self.size
            self.bit_array[digest] = 1

    def check(self, string):
        for i in range(self.hash_count):
            digest = mmh3.hash(string, i) % self.size
            if self.bit_array[digest] == 0:
                return False # Definitely NO
        return True # Maybe YES

# Тест
bf = BloomFilter(5000, 7) # Size 5000 bits, 7 hashes

# Добавляем данные
animals = ["cat", "dog", "elephant", "bird"]
for a in animals:
    bf.add(a)

# Проверяем
print(f"Cat in set? {bf.check('cat')}")       # True
print(f"Lion in set? {bf.check('lion')}")    # False (likely)
print(f"Dog in set? {bf.check('dog')}")      # True

# Проверка False Positive
import random
import string

fp_count = 0
tests = 10000
for _ in range(tests):
    # Генерим случайную строку
    s = ''.join(random.choices(string.ascii_lowercase, k=5))
    if s not in animals and bf.check(s):
        fp_count += 1

print(f"False Positives: {fp_count}/{tests} ({fp_count/tests:.2%})")
```

---

## 6. GeoHash и Quadtree (Пространственные индексы)

Для поиска "кто рядом" latitude/longitude превращают в строки или деревья.

### 6.1 Geohash

Превращает 2D координаты в 1D строку.
Чем длиннее общий префикс у двух геохешей, тем они ближе.
`u4pruydqqvj` (Google HQ).
Соседи будут иметь префикс `u4pru...`.

**Поиск**: `SELECT * FROM Drivers WHERE geohash LIKE 'u4pru%'`.
БД может использовать обычный B-tree индекс для этого!

---

## 💡 Key Takeaways

- **Probabilistic DS** — это обмен точности на память (Space-Accuracy Trade-off).

- **Bloom Filter**: "Точно нет" или "Возможно да". Экономит Disk I/O.

- **HyperLogLog**: Считает уникальные элементы (mrd distinct) с крошечной памятью.

- **False Positives** допустимы там, где цена ошибки мала (показать рекламу лишний раз) или где есть второй этап проверки (обращение к диску).

---

## 🚀 Next Steps

**Module 4 Final:**

- [Case Studies](../16_Case_Studies/) — мы готовы разобрать архитектуру реальных гигантов (Twitter Timeline, Uber Geospatial, URL Shortener).

**Practice Ideas:**

1. Используйте Redis PFADD / PFCOUNT для подсчета уникальных слов в "Войне и Мире". Сравните память с `SCARD` (Set).
2. Реализуйте простой спелл-чекер с использованием Bloom Filter.
3. Попробуйте библиотеку `pygeohash` для поиска соседей.

---

