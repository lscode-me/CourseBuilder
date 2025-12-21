# Форматы данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать типы данных (модуль 03)
- Знать основы хранилищ данных (модуль 05)
- Иметь представление о структуре данных

**Recommended prior modules:**

- [03_Data_Types](../03_Data_Types/) — типы данных
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать форматы данных: CSV, JSON, Avro, Parquet, ORC
- Понимать разницу между row-based и column-based форматами
- Выбирать подходящий формат для конкретных задач
- Объяснять trade-offs между различными форматами

---

## 1. Введение в форматы данных

Формат данных определяет, как данные представлены и хранятся. Выбор формата критичен для производительности, размера файлов и совместимости.

**Критерии выбора формата:**

- Размер файла (сжатие)
- Скорость чтения/записи
- Совместимость
- Поддержка схемы
- Тип данных (structured, semi-structured)

---

## 2. Row-based форматы

Row-based форматы хранят данные построчно: каждая строка содержит все поля записи.

### 2.1 CSV (Comma-Separated Values)

**Характеристики:**

- Текстовый формат
- Простой и читаемый
- Нет схемы
- Большой размер файлов

**Use cases:**

- Обмен данными
- Импорт/экспорт
- Маленькие объёмы данных

**Example: CSV формат**

```python

import csv
import io

# Создание CSV данных
data = [
    {"id": 1, "name": "Alice", "age": 30, "city": "Moscow"},
    {"id": 2, "name": "Bob", "age": 25, "city": "Saint Petersburg"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Moscow"}
]

# Запись в CSV
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["id", "name", "age", "city"])
writer.writeheader()
writer.writerows(data)

csv_content = output.getvalue()
print("CSV формат:")
print(csv_content)

# Размер (примерно)

print(f"\nРазмер CSV: ~{len(csv_content)} байт")
```

**Output:**
```

CSV формат:
id,name,age,city
1,Alice,30,Moscow
2,Bob,25,Saint Petersburg
3,Charlie,35,Moscow

Размер CSV: ~95 байт
```

### 2.2 JSON (JavaScript Object Notation)

**Характеристики:**

- Текстовый формат
- Semi-structured данные
- Встроенная схема (гибкая)
- Поддержка вложенных структур

**Use cases:**

- API responses
- Configuration files
- Semi-structured данные

**Example: JSON формат**

```python

import json

# JSON данные
json_data = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "Moscow",
            "zip": "101000"
        },
        "skills": ["Python", "SQL"]
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 25,
        "address": {
            "city": "Saint Petersburg",
            "zip": "190000"
        },
        "skills": ["Java", "JavaScript"]
    }
]

# Сериализация
json_string = json.dumps(json_data, indent=2)
print("JSON формат:")
print(json_string)

# Размер

print(f"\nРазмер JSON: ~{len(json_string)} байт")
```

**Output:**
```

JSON формат:
[
  {
    "id": 1,
    "name": "Alice",
    "age": 30,
    "address": {
      "city": "Moscow",
      "zip": "101000"
    },
    "skills": ["Python", "SQL"]
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 25,
    "address": {
      "city": "Saint Petersburg",
      "zip": "190000"
    },
    "skills": ["Java", "JavaScript"]
  }
]

Размер JSON: ~350 байт
```

### 2.3 Avro

**Характеристики:**

- Бинарный формат
- Schema-on-write (схема в файле)
- Row-based storage
- Хорошее сжатие

**Use cases:**

- Streaming данные (Kafka)
- Schema evolution
- Большие объёмы данных

**Example: Avro концепция**

```python
# Симуляция Avro (схема + данные)
avro_schema = {
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}

avro_data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
]

print("Avro формат:")
print(f"Schema: {avro_schema}")
print(f"Data: {avro_data}")
print("\nПреимущества Avro:")
print("  - Schema встроен в файл")
print("  - Хорошее сжатие")
print("  - Schema evolution")
print("  - Быстрая сериализация/десериализация")
```

**Output:**
```

Avro формат:
Schema: {'type': 'record', 'name': 'User', 'fields': [{'name': 'id', 'type': 'int'}, {'name': 'name', 'type': 'string'}, {'name': 'age', 'type': 'int'}]}
Data: [{'id': 1, 'name': 'Alice', 'age': 30}, {'id': 2, 'name': 'Bob', 'age': 25}]

Преимущества Avro:

  - Schema встроен в файл
  - Хорошее сжатие
  - Schema evolution
  - Быстрая сериализация/десериализация
```

---

## 3. Column-based форматы

Column-based форматы хранят данные по колонкам: все значения одной колонки хранятся вместе.

### 3.1 Parquet

**Характеристики:**

- Бинарный формат
- Columnar storage
- Отличное сжатие
- Schema-on-write
- Оптимизация для аналитики

**Use cases:**

- Data Warehouses
- Аналитические запросы
- Большие объёмы данных
- Data Lakes

**Example: Parquet концепция**

```python
# Симуляция Parquet (columnar storage)
parquet_data = {
    "columns": {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [30, 25, 35]
    },
    "schema": {
        "id": "INT64",
        "name": "STRING",
        "age": "INT64"
    },
    "metadata": {
        "row_count": 3,
        "compression": "SNAPPY"
    }
}

print("Parquet формат (Columnar):")
print("Структура:")
print("  Column 'id': [1, 2, 3]")
print("  Column 'name': ['Alice', 'Bob', 'Charlie']")
print("  Column 'age': [30, 25, 35]")
print("\nПреимущества:")
print("  - Отличное сжатие (одинаковые значения в колонке)")
print("  - Быстрые агрегации (читаем только нужные колонки)")
print("  - Оптимизация для аналитики")
print("  - Schema встроен")
```

**Output:**
```

Parquet формат (Columnar):
Структура:
  Column 'id': [1, 2, 3]
  Column 'name': ['Alice', 'Bob', 'Charlie']
  Column 'age': [30, 25, 35]

Преимущества:

  - Отличное сжатие (одинаковые значения в колонке)
  - Быстрые агрегации (читаем только нужные колонки)
  - Оптимизация для аналитики
  - Schema встроен
```

### 3.2 ORC (Optimized Row Columnar)

**Характеристики:**

- Бинарный формат
- Columnar storage
- Отличное сжатие
- Индексы встроены
- Оптимизация для Hive

**Use cases:**

- Hadoop экосистема
- Hive таблицы
- Большие объёмы данных
- Аналитические запросы

**Example: ORC концепция**

```python
# Симуляция ORC
orc_data = {
    "stripes": [
        {
            "columns": {
                "id": [1, 2],
                "name": ["Alice", "Bob"],
                "age": [30, 25]
            }
        },
        {
            "columns": {
                "id": [3],
                "name": ["Charlie"],
                "age": [35]
            }
        }
    ],
    "indexes": {
        "min": {"id": 1, "age": 25},
        "max": {"id": 3, "age": 35}
    },
    "compression": "ZLIB"
}

print("ORC формат:")
print("  - Columnar storage в stripes")
print("  - Встроенные индексы (min/max)")
print("  - Отличное сжатие")
print("  - Оптимизация для Hive")
```

**Output:**
```

ORC формат:

  - Columnar storage в stripes
  - Встроенные индексы (min/max)
  - Отличное сжатие
  - Оптимизация для Hive
```

---

## 4. Row-based vs Column-based

Понимание различий критично для выбора формата.

### 4.1 Row-based (CSV, JSON, Avro)

**Преимущества:**

- Быстрое чтение полных записей
- Подходит для транзакций
- Простота понимания

**Недостатки:**

- Медленные агрегации
- Больший размер файлов
- Читаем все колонки, даже если нужна одна

**Example: Row-based чтение**

```python
# Row-based: читаем всю строку

row_based_data = [
    {"id": 1, "name": "Alice", "age": 30, "city": "Moscow", "salary": 5000},
    {"id": 2, "name": "Bob", "age": 25, "city": "SPB", "salary": 4000},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Moscow", "salary": 6000}
]

# Запрос: средний возраст
# Нужно прочитать ВСЕ поля всех записей

ages = [r["age"] for r in row_based_data]
avg_age = sum(ages) / len(ages)

print("Row-based запрос (средний возраст):")
print(f"  Прочитано полей: {len(row_based_data) * 5} (все поля всех записей)")
print(f"  Средний возраст: {avg_age}")
```

**Output:**
```

Row-based запрос (средний возраст):
  Прочитано полей: 15 (все поля всех записей)
  Средний возраст: 30.0
```

### 4.2 Column-based (Parquet, ORC)

**Преимущества:**

- Быстрые агрегации (читаем только нужные колонки)
- Отличное сжатие
- Оптимизация для аналитики

**Недостатки:**

- Медленное чтение полных записей
- Сложнее для транзакций
- Требует больше памяти для записи

**Example: Column-based чтение**

```python
# Column-based: читаем только нужную колонку

column_based_data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "city": ["Moscow", "SPB", "Moscow"],
    "salary": [5000, 4000, 6000]
}

# Запрос: средний возраст
# Читаем ТОЛЬКО колонку age

ages = column_based_data["age"]
avg_age = sum(ages) / len(ages)

print("Column-based запрос (средний возраст):")
print(f"  Прочитано полей: {len(ages)} (только колонка age)")
print(f"  Средний возраст: {avg_age}")
print("  Преимущество: читаем только нужные данные!")
```

**Output:**
```

Column-based запрос (средний возраст):
  Прочитано полей: 3 (только колонка age)
  Средний возраст: 30.0
  Преимущество: читаем только нужные данные!
```

### 4.3 Сравнение

| Аспект | Row-based | Column-based |
|--------|-----------|--------------|
| **Чтение полной записи** | Быстро | Медленно |
| **Агрегации** | Медленно | Быстро |
| **Сжатие** | Среднее | Отличное |
| **Use case** | Транзакции | Аналитика |
| **Примеры** | CSV, JSON, Avro | Parquet, ORC |

---

## 5. Schema-on-read vs Schema-on-write

Разница в том, когда применяется схема данных.

### 5.1 Schema-on-write

**Характеристики:**

- Схема применяется при записи
- Валидация при записи
- Данные уже структурированы

**Примеры:**

- Parquet, Avro, ORC
- Databases, Data Warehouses

**Example: Schema-on-write**

```python
# Schema-on-write: схема применяется при записи
schema = {
    "id": "INT",
    "name": "VARCHAR(100)",
    "age": "INT"
}

def write_with_schema(data, schema):
    """Записывает данные с применением схемы"""
    validated = []
    for record in data:
        # Валидация по схеме
        if not all(k in record and isinstance(record[k], type(schema[k])) 
                   for k in schema.keys()):
            raise ValueError("Данные не соответствуют схеме")
        validated.append(record)
    
    print("✅ Данные записаны с применением схемы")
    return validated

data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
]

validated_data = write_with_schema(data, schema)
print(f"Записано записей: {len(validated_data)}")
```

**Output:**
```

✅ Данные записаны с применением схемы
Записано записей: 2
```

### 5.2 Schema-on-read

**Характеристики:**

- Схема применяется при чтении
- Гибкость: разные схемы для одних данных
- Данные хранятся "как есть"

**Примеры:**

- CSV, JSON (без схемы)
- Data Lakes

**Example: Schema-on-read**

```python
# Schema-on-read: схема применяется при чтении
raw_data = [
    {"id": "1", "name": "Alice", "age": "30"},
    {"id": "2", "name": "Bob", "age": "25"}
]

def read_with_schema(data, schema):
    """Читает данные с применением схемы"""
    transformed = []
    for record in data:
        transformed_record = {}
        for field, field_type in schema.items():
            value = record.get(field)
            if field_type == "INT":
                transformed_record[field] = int(value)
            elif field_type == "VARCHAR":
                transformed_record[field] = str(value)
        transformed.append(transformed_record)
    
    print("✅ Данные прочитаны с применением схемы")
    return transformed

schema = {
    "id": "INT",
    "name": "VARCHAR",
    "age": "INT"
}

transformed_data = read_with_schema(raw_data, schema)
print(f"Прочитано записей: {transformed_data}")
```

**Output:**
```

✅ Данные прочитаны с применением схемы
Прочитано записей: [{'id': 1, 'name': 'Alice', 'age': 30}, {'id': 2, 'name': 'Bob', 'age': 25}]
```

### 5.3 Сравнение

| Аспект | Schema-on-write | Schema-on-read |
|--------|-----------------|----------------|
| **Валидация** | При записи | При чтении |
| **Гибкость** | Низкая | Высокая |
| **Производительность** | Быстрое чтение | Медленнее чтение |
| **Use case** | Структурированные данные | Сырые данные |
| **Примеры** | Parquet, Avro | CSV, Data Lakes |

---

## 6. Выбор формата

Выбор формата зависит от требований к данным и использования.

### 6.1 Decision Matrix

**Используйте CSV, если:**

- Маленькие объёмы данных
- Обмен данными
- Простота важнее производительности

**Используйте JSON, если:**

- API responses
- Semi-structured данные
- Гибкая схема

**Используйте Avro, если:**

- Streaming данные (Kafka)
- Нужна schema evolution
- Row-based с хорошим сжатием

**Используйте Parquet, если:**

- Аналитические запросы
- Большие объёмы данных
- Data Warehouses
- Нужно отличное сжатие

**Используйте ORC, если:**

- Hadoop экосистема
- Hive таблицы
- Аналитические запросы

**Example: Выбор формата**

```python

def recommend_format(requirements):
    """Рекомендует формат на основе требований"""
    if requirements.get("small_volume") and requirements.get("exchange"):
        return "CSV (простота, совместимость)"
    elif requirements.get("api") or requirements.get("semi_structured"):
        return "JSON (гибкость, вложенные структуры)"
    elif requirements.get("streaming") and requirements.get("schema_evolution"):
        return "Avro (schema-on-write, хорошее сжатие)"
    elif requirements.get("analytical") and requirements.get("large_volume"):
        return "Parquet (columnar, отличное сжатие)"
    elif requirements.get("hadoop") or requirements.get("hive"):
        return "ORC (Hadoop экосистема, индексы)"
    else:
        return "Определить на основе детальных требований"

# Примеры

examples = [
    {"small_volume": True, "exchange": True},
    {"api": True, "semi_structured": True},
    {"streaming": True, "schema_evolution": True},
    {"analytical": True, "large_volume": True},
    {"hadoop": True, "hive": True}
]

print("Рекомендации форматов:")
for i, req in enumerate(examples, 1):
    recommendation = recommend_format(req)
    print(f"  Пример {i}: {recommendation}")
```

**Output:**
```

Рекомендации форматов:
  Пример 1: CSV (простота, совместимость)
  Пример 2: JSON (гибкость, вложенные структуры)
  Пример 3: Avro (schema-on-write, хорошее сжатие)
  Пример 4: Parquet (columnar, отличное сжатие)
  Пример 5: ORC (Hadoop экосистема, индексы)
```

---

## 7. Сравнение форматов

Сводная таблица для быстрого выбора.

### 7.1 Таблица сравнения

| Формат | Тип | Схема | Сжатие | Use case |
|--------|-----|-------|--------|----------|
| **CSV** | Row | Нет | Нет | Обмен, маленькие объёмы |
| **JSON** | Row | Гибкая | Нет | API, конфигурация |
| **Avro** | Row | Schema-on-write | Хорошее | Streaming, schema evolution |
| **Parquet** | Column | Schema-on-write | Отличное | Аналитика, Data Warehouses |
| **ORC** | Column | Schema-on-write | Отличное | Hadoop, Hive |

### 7.2 Размер файлов (примерно)

Для 1M записей (id, name, age, city):

- CSV: ~50 MB
- JSON: ~80 MB
- Avro: ~20 MB (сжатие)
- Parquet: ~5 MB (columnar + сжатие)
- ORC: ~6 MB (columnar + сжатие)

---

## 💡 Key Takeaways

- **Row-based vs Column-based**: Row-based (CSV, JSON, Avro) для транзакций, column-based (Parquet, ORC) для аналитики. Выбор зависит от паттернов доступа.

- **Schema-on-write vs Schema-on-read**: Schema-on-write (Parquet, Avro) валидирует при записи, schema-on-read (CSV, Data Lakes) применяет схему при чтении. Разные требования к гибкости.

- **Выбор формата**: CSV для простоты, JSON для гибкости, Avro для streaming, Parquet для аналитики, ORC для Hadoop. Нет универсального решения.

- **Сжатие и производительность**: Column-based форматы (Parquet, ORC) обеспечивают отличное сжатие и быстрые агрегации за счёт columnar storage.

- **Современные тренды**: Parquet становится стандартом для Data Lakes и Data Warehouses благодаря балансу между производительностью и совместимостью.

---

## 🚀 Next Steps

**Related Modules:**

- [07_Indexes_Partitioning](../07_Indexes_Partitioning/) — индексы и партиционирование
- [05_Data_Storage](../05_Data_Storage/) — хранилища данных
- [09_Batch_Processing](../09_Batch_Processing/) — batch processing

**Practice Ideas:**

1. Сравните размеры файлов: создайте одинаковые данные в CSV, JSON и Parquet
2. Измерьте производительность: сравните скорость чтения row-based и column-based форматов
3. Изучите schema evolution: как Avro и Parquet обрабатывают изменения схемы

**Going Deeper:**

- Изучите внутреннюю структуру Parquet: row groups, column chunks
- Погрузитесь в Avro schema evolution: forward/backward compatibility
- Изучите оптимизацию Parquet: partitioning, sorting, compression codecs

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — форматы данных
- "High Performance Spark" — оптимизация форматов для Spark

**Articles:**

- "Apache Parquet: Columnar Storage for the People" — детальное объяснение Parquet
- "Avro vs Parquet vs ORC" — сравнение форматов

**Documentation:**

- Apache Parquet: https://parquet.apache.org/docs/
- Apache Avro: https://avro.apache.org/docs/current/
- Apache ORC: https://orc.apache.org/docs/

---


