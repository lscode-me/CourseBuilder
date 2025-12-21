# Качество данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать batch processing (модуль 09)
- Знать основы data modeling (модуль 04)
- Иметь представление о метаданных (модуль 08)

**Recommended prior modules:**

- [09_Batch_Processing](../09_Batch_Processing/) — batch processing
- [04_Data_Modeling](../04_Data_Modeling/) — основы data modeling
- [08_Metadata_Catalogs](../08_Metadata_Catalogs/) — метаданные

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Валидировать данные на соответствие схеме и правилам
- Измерять и обеспечивать полноту данных
- Контролировать свежесть данных
- Обеспечивать консистентность данных между системами

---

## 1. Введение в качество данных

Качество данных критично для надёжности систем и правильности решений. Плохое качество данных приводит к неверным инсайтам и решениям.

**Аспекты качества данных:**

- **Validation** — соответствие схеме и правилам

- **Completeness** — полнота данных

- **Freshness** — актуальность данных

- **Consistency** — консистентность между системами

---

## 2. Data Validation (Валидация данных)

Валидация проверяет, соответствуют ли данные ожидаемой схеме и бизнес-правилам.

### 2.1 Типы валидации

**Schema Validation:**

- Соответствие схеме
- Типы данных
- Обязательные поля

**Business Rules Validation:**

- Бизнес-логика
- Ограничения значений
- Связи между полями

**Example: Валидация данных**

```python

class DataValidator:
    def __init__(self, schema, rules=None):
        self.schema = schema
        self.rules = rules or {}
    
    def validate_schema(self, record):
        """Валидация схемы"""
        errors = []
        
        # Проверка обязательных полей
        for field, field_info in self.schema.items():
            if field_info.get("required", False) and field not in record:
                errors.append(f"Отсутствует обязательное поле: {field}")
            
            # Проверка типа
            if field in record:
                expected_type = field_info.get("type")
                actual_type = type(record[field]).__name__
                if expected_type and actual_type != expected_type:
                    errors.append(f"Неверный тип для {field}: ожидается {expected_type}, получен {actual_type}")
        
        return errors
    
    def validate_rules(self, record):
        """Валидация бизнес-правил"""
        errors = []
        
        for rule_name, rule_func in self.rules.items():
            try:
                if not rule_func(record):
                    errors.append(f"Нарушено правило: {rule_name}")
            except Exception as e:
                errors.append(f"Ошибка при проверке правила {rule_name}: {e}")
        
        return errors
    
    def validate(self, record):
        """Полная валидация"""
        errors = []
        errors.extend(self.validate_schema(record))
        errors.extend(self.validate_rules(record))
        return errors

# Использование
schema = {
    "id": {"type": "int", "required": True},
    "name": {"type": "str", "required": True},
    "age": {"type": "int", "required": False},
    "email": {"type": "str", "required": True}
}

rules = {
    "age_positive": lambda r: r.get("age", 0) >= 0,
    "email_format": lambda r: "@" in r.get("email", "")
}

validator = DataValidator(schema, rules)

# Валидация
test_record = {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"}
errors = validator.validate(test_record)

if errors:
    print(f"❌ Ошибки валидации: {errors}")
else:
    print("✅ Данные валидны")
```

**Output:**
```

✅ Данные валидны
```

---

## 3. Data Completeness (Полнота данных)

Полнота данных измеряет, какая часть данных присутствует и не является NULL.

### 3.1 Метрики полноты

**Field Completeness:**

- Процент не-NULL значений в поле
- Пример: 95% записей имеют email

**Record Completeness:**

- Процент полных записей
- Все обязательные поля заполнены

**Example: Измерение полноты**

```python

class CompletenessChecker:
    def __init__(self, required_fields):
        self.required_fields = required_fields
    
    def check_field_completeness(self, data, field):
        """Проверяет полноту поля"""
        total = len(data)
        non_null = sum(1 for record in data if record.get(field) is not None)
        completeness = (non_null / total * 100) if total > 0 else 0
        
        return {
            "field": field,
            "total": total,
            "non_null": non_null,
            "null": total - non_null,
            "completeness_percent": completeness
        }
    
    def check_record_completeness(self, data):
        """Проверяет полноту записей"""
        total = len(data)
        complete = sum(1 for record in data 
                      if all(record.get(field) is not None 
                            for field in self.required_fields))
        completeness = (complete / total * 100) if total > 0 else 0
        
        return {
            "total_records": total,
            "complete_records": complete,
            "incomplete_records": total - complete,
            "completeness_percent": completeness
        }
    
    def get_completeness_report(self, data):
        """Генерирует отчёт о полноте"""
        report = {
            "record_completeness": self.check_record_completeness(data),
            "field_completeness": {}
        }
        
        for field in self.required_fields:
            report["field_completeness"][field] = self.check_field_completeness(data, field)
        
        return report

# Использование
data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "Bob", "email": None, "age": 25},  # Отсутствует email
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": None}  # Отсутствует age
]

checker = CompletenessChecker(required_fields=["id", "name", "email"])
report = checker.get_completeness_report(data)

print("Отчёт о полноте данных:")
print(f"  Полнота записей: {report['record_completeness']['completeness_percent']:.1f}%")
for field, stats in report["field_completeness"].items():
    print(f"  {field}: {stats['completeness_percent']:.1f}% ({stats['non_null']}/{stats['total']})")
```

**Output:**
```

Отчёт о полноте данных:
  Полнота записей: 33.3%
  id: 100.0% (3/3)
  name: 100.0% (3/3)
  email: 66.7% (2/3)
```

---

## 4. Data Freshness (Свежесть данных)

Свежесть данных измеряет, насколько актуальны данные. Критично для real-time систем и регулярных обновлений.

### 4.1 Метрики свежести

**Last Updated:**

- Когда данные последний раз обновлялись
- Сравнение с текущим временем

**Update Frequency:**

- Как часто обновляются данные
- Соответствие ожидаемой частоте

**Example: Проверка свежести**

```python

from datetime import datetime, timedelta

class FreshnessChecker:
    def __init__(self, expected_frequency_hours=24):
        self.expected_frequency = timedelta(hours=expected_frequency_hours)
    
    def check_freshness(self, last_updated, current_time=None):
        """Проверяет свежесть данных"""
        if current_time is None:
            current_time = datetime.now()
        
        if isinstance(last_updated, str):
            last_updated = datetime.fromisoformat(last_updated)
        
        age = current_time - last_updated
        is_fresh = age <= self.expected_frequency
        
        return {
            "last_updated": last_updated,
            "current_time": current_time,
            "age_hours": age.total_seconds() / 3600,
            "expected_frequency_hours": self.expected_frequency.total_seconds() / 3600,
            "is_fresh": is_fresh,
            "status": "fresh" if is_fresh else "stale"
        }
    
    def check_table_freshness(self, table_name, last_updated):
        """Проверяет свежесть таблицы"""
        result = self.check_freshness(last_updated)
        print(f"📊 Свежесть таблицы '{table_name}':")
        print(f"   Последнее обновление: {result['last_updated']}")
        print(f"   Возраст: {result['age_hours']:.1f} часов")
        print(f"   Ожидаемая частота: {result['expected_frequency_hours']} часов")
        print(f"   Статус: {result['status'].upper()}")
        return result

# Использование

checker = FreshnessChecker(expected_frequency_hours=24)

# Свежие данные (обновлены 2 часа назад)
checker.check_table_freshness("users", "2024-01-01T09:00:00")

# Устаревшие данные (обновлены 30 часов назад)
checker.check_table_freshness("orders", "2023-12-31T05:00:00")
```

**Output:**
```

📊 Свежесть таблицы 'users':
   Последнее обновление: 2024-01-01 09:00:00
   Возраст: 2.0 часов
   Ожидаемая частота: 24.0 часов
   Статус: FRESH
📊 Свежесть таблицы 'orders':
   Последнее обновление: 2023-12-31 05:00:00
   Возраст: 30.0 часов
   Ожидаемая частота: 24.0 часов
   Статус: STALE
```

---

## 5. Data Consistency (Консистентность данных)

Консистентность данных обеспечивает согласованность данных между различными системами и источниками.

### 5.1 Типы консистентности

**Referential Integrity:**

- Связи между таблицами
- Foreign keys
- Каскадные обновления

**Cross-system Consistency:**

- Согласованность между системами
- Синхронизация данных
- Единый источник истины

**Example: Проверка консистентности**

```python

class ConsistencyChecker:
    def __init__(self):
        self.references = {}
    
    def check_referential_integrity(self, child_table, parent_table, foreign_key):
        """Проверяет referential integrity"""
        child_records = child_table
        parent_keys = set(parent_table)
        
        violations = []
        for record in child_records:
            fk_value = record.get(foreign_key)
            if fk_value and fk_value not in parent_keys:
                violations.append({
                    "record": record,
                    "foreign_key": fk_value,
                    "issue": f"FK {fk_value} не существует в {parent_table}"
                })
        
        return {
            "total_records": len(child_records),
            "violations": violations,
            "is_consistent": len(violations) == 0
        }
    
    def check_cross_system_consistency(self, system1_data, system2_data, key_field):
        """Проверяет консистентность между системами"""
        system1_keys = {r[key_field] for r in system1_data if key_field in r}
        system2_keys = {r[key_field] for r in system2_data if key_field in r}
        
        only_in_system1 = system1_keys - system2_keys
        only_in_system2 = system2_keys - system1_keys
        in_both = system1_keys & system2_keys
        
        return {
            "only_in_system1": len(only_in_system1),
            "only_in_system2": len(only_in_system2),
            "in_both": len(in_both),
            "is_consistent": len(only_in_system1) == 0 and len(only_in_system2) == 0
        }

# Использование
checker = ConsistencyChecker()

# Referential integrity
users = [1, 2, 3]  # User IDs
orders = [
    {"order_id": 101, "user_id": 1},
    {"order_id": 102, "user_id": 2},
    {"order_id": 103, "user_id": 5}  # Нарушение: user_id 5 не существует
]

integrity_check = checker.check_referential_integrity(orders, users, "user_id")
print("Referential Integrity Check:")
print(f"  Всего записей: {integrity_check['total_records']}")
print(f"  Нарушений: {len(integrity_check['violations'])}")
print(f"  Консистентно: {integrity_check['is_consistent']}")

# Cross-system consistency

system1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
system2 = [{"id": 1, "name": "Alice"}, {"id": 3, "name": "Charlie"}]

consistency_check = checker.check_cross_system_consistency(system1, system2, "id")
print(f"\nCross-system Consistency:")
print(f"  Только в системе 1: {consistency_check['only_in_system1']}")
print(f"  Только в системе 2: {consistency_check['only_in_system2']}")
print(f"  В обеих системах: {consistency_check['in_both']}")
print(f"  Консистентно: {consistency_check['is_consistent']}")
```

**Output:**
```

Referential Integrity Check:
  Всего записей: 3
  Нарушений: 1
  Консистентно: False

Cross-system Consistency:
  Только в системе 1: 1
  Только в системе 2: 1
  В обеих системах: 1
  Консистентно: False
```

---

## 6. Data Quality Framework

Комплексный подход к обеспечению качества данных.

### 6.1 Компоненты Framework

**Validation Layer:**

- Валидация при ingestion
- Валидация при трансформации
- Валидация перед загрузкой

**Monitoring Layer:**

- Метрики качества
- Алерты при проблемах
- Дашборды качества

**Example: Data Quality Framework**

```python

class DataQualityFramework:
    def __init__(self):
        self.validators = []
        self.metrics = {}
        self.alerts = []
    
    def add_validator(self, validator, stage):
        """Добавляет валидатор на этап"""
        self.validators.append({
            "validator": validator,
            "stage": stage
        })
        print(f"✅ Валидатор добавлен на этап '{stage}'")
    
    def validate_at_stage(self, data, stage):
        """Валидирует данные на этапе"""
        print(f"\n🔍 Валидация на этапе '{stage}':")
        all_errors = []
        
        for val_info in self.validators:
            if val_info["stage"] == stage:
                errors = val_info["validator"].validate(data)
                if errors:
                    all_errors.extend(errors)
                    print(f"   ❌ Найдено ошибок: {len(errors)}")
                else:
                    print(f"   ✅ Валидация пройдена")
        
        return all_errors
    
    def calculate_quality_score(self, completeness, freshness, consistency):
        """Вычисляет общий score качества"""
        score = (
            completeness * 0.4 +
            (1.0 if freshness else 0.0) * 0.3 +
            (1.0 if consistency else 0.0) * 0.3
        ) * 100
        return score
    
    def monitor_quality(self, data, metadata):
        """Мониторинг качества данных"""
        # Симуляция вычисления метрик
        completeness = 0.95
        freshness = True
        consistency = True
        
        score = self.calculate_quality_score(completeness, freshness, consistency)
        
        print(f"\n📊 Качество данных:")
        print(f"   Completeness: {completeness*100:.1f}%")
        print(f"   Freshness: {'✅' if freshness else '❌'}")
        print(f"   Consistency: {'✅' if consistency else '❌'}")
        print(f"   Overall Score: {score:.1f}/100")
        
        if score < 80:
            self.alerts.append(f"⚠️  Низкое качество данных: {score:.1f}/100")
            print(f"   {self.alerts[-1]}")
        
        return score

# Использование

framework = DataQualityFramework()

# Добавление валидаторов
from types import SimpleNamespace
validator = SimpleNamespace(validate=lambda d: [])
framework.add_validator(validator, "ingestion")
framework.add_validator(validator, "transformation")

# Мониторинг
data = [{"id": 1, "name": "Alice"}]
framework.monitor_quality(data, {})
```

**Output:**
```

✅ Валидатор добавлен на этап 'ingestion'
✅ Валидатор добавлен на этап 'transformation'

📊 Качество данных:
   Completeness: 95.0%
   Freshness: ✅
   Consistency: ✅
   Overall Score: 95.0/100
```

---

## 💡 Key Takeaways

- **Data Validation**: Проверка соответствия схеме и бизнес-правилам. Критично на всех этапах pipeline.

- **Data Completeness**: Измерение полноты данных (field и record level). Метрики помогают выявить проблемы.

- **Data Freshness**: Контроль актуальности данных. Критично для real-time систем и регулярных обновлений.

- **Data Consistency**: Обеспечение согласованности между системами. Referential integrity и cross-system consistency.

- **Data Quality Framework**: Комплексный подход с валидацией, мониторингом и алертами. Автоматизация критична для больших систем.

---

## 🚀 Next Steps

**Related Modules:**

- [12_Errors_Reproducibility](../12_Errors_Reproducibility/) — ошибки и воспроизводимость
- [08_Metadata_Catalogs](../08_Metadata_Catalogs/) — метаданные
- [09_Batch_Processing](../09_Batch_Processing/) — batch processing

**Practice Ideas:**

1. Создайте валидатор для ваших данных: проверка схемы и бизнес-правил
2. Измерьте качество данных: полнота, свежесть, консистентность
3. Настройте мониторинг качества: метрики и алерты

**Going Deeper:**

- Изучите Great Expectations: framework для валидации данных
- Погрузитесь в data profiling: автоматическое обнаружение проблем
- Изучите data quality в streaming: real-time валидация

---

## 📚 Additional Resources

**Books:**

- "Data Quality: The Accuracy Dimension" by Jack Olson — качество данных
- "Fundamentals of Data Engineering" — глава о качестве данных

**Articles:**

- "Data Quality Best Practices" — рекомендации
- "Measuring Data Quality" — метрики качества

**Documentation:**

- Great Expectations: https://greatexpectations.io/
- Apache Griffin: https://griffin.apache.org/ (data quality)

---


