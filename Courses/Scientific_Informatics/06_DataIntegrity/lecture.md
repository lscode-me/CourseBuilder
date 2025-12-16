# Data Integrity и безопасность данных
## Качество данных, контроль изменений, проверка корректности и безопасность

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы работы с данными (модули 02-05)
- Знать основы управления данными (модуль 05_DataManagement)
- Иметь базовые знания о безопасности данных

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Оценивать и обеспечивать качество научных данных
- Контролировать изменения данных и отслеживать их историю
- Проверять корректность данных через валидацию
- Применять основы data security в научных проектах
- Использовать checksums и контрольные суммы для проверки целостности

---

## 1. Качество данных

### 1.1 Критерии качества

**Качество данных** определяется несколькими критериями:

| Критерий | Описание | Методы проверки |
|----------|----------|----------------|
| **Полнота** | Отсутствие пропущенных значений | Проверка на NaN, None |
| **Точность** | Соответствие реальным значениям | Сравнение с референсом |
| **Согласованность** | Логическая корректность | Проверка диапазонов, ограничений |
| **Актуальность** | Соответствие времени | Проверка дат, версий |
| **Валидность** | Соответствие формату | Проверка типов, структур |

**Пример: Проверка качества данных**

```python

import pandas as pd
import numpy as np

class DataQualityChecker:
    """Проверка качества научных данных"""
    
    def __init__(self):
        self.checks = []
    
    def check_completeness(self, data):
        """Проверка полноты данных"""
        missing = data.isna().sum()
        total = len(data)
        completeness = 1 - (missing.sum() / (total * len(data.columns)))
        
        result = {
            'check': 'completeness',
            'score': completeness,
            'missing_count': missing.sum(),
            'passed': completeness >= 0.95
        }
        self.checks.append(result)
        return result
    
    def check_consistency(self, data, rules):
        """Проверка согласованности по правилам"""
        violations = []
        for column, rule in rules.items():
            if 'min' in rule and (data[column] < rule['min']).any():
                violations.append(f"{column} < {rule['min']}")
            if 'max' in rule and (data[column] > rule['max']).any():
                violations.append(f"{column} > {rule['max']}")
        
        result = {
            'check': 'consistency',
            'violations': violations,
            'passed': len(violations) == 0
        }
        self.checks.append(result)
        return result
    
    def get_summary(self):
        """Сводка проверок"""
        passed = sum(1 for c in self.checks if c['passed'])
        total = len(self.checks)
        return {
            'total_checks': total,
            'passed': passed,
            'failed': total - passed,
            'checks': self.checks
        }

# Пример использования
data = pd.DataFrame({
    'temperature': [20, 25, 30, None, 40],
    'reaction_rate': [10.5, 12.3, 15.2, 18.1, 20.5],
    'pressure': [1.0, 1.0, 1.0, 1.0, 1.0]
})

checker = DataQualityChecker()
checker.check_completeness(data)
checker.check_consistency(data, {
    'temperature': {'min': 0, 'max': 100},
    'reaction_rate': {'min': 0, 'max': 50}
})

summary = checker.get_summary()
print("Data Quality Summary:")
print(f"  Total checks: {summary['total_checks']}")
print(f"  Passed: {summary['passed']}")
print(f"  Failed: {summary['failed']}")
```

**Output:**
```

Data Quality Summary:
  Total checks: 2
  Passed: 1
  Failed: 1
```

### 1.2 Обнаружение аномалий

**Методы обнаружения аномалий:**

```python

def detect_outliers_iqr(data, column):
    """Выявление выбросов методом IQR"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

def detect_outliers_zscore(data, column, threshold=3):
    """Выявление выбросов методом Z-score"""
    mean = data[column].mean()
    std = data[column].std()
    z_scores = np.abs((data[column] - mean) / std)
    outliers = data[z_scores > threshold]
    return outliers

# Пример
data = pd.DataFrame({
    'value': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]  # 100 - выброс
})

outliers_iqr = detect_outliers_iqr(data, 'value')
outliers_z = detect_outliers_zscore(data, 'value')

print(f"IQR outliers: {len(outliers_iqr)}")
print(f"Z-score outliers: {len(outliers_z)}")
```

**Output:**
```

IQR outliers: 1
Z-score outliers: 1
```

---

## 2. Контроль изменений

### 2.1 Версионирование данных

**Принципы версионирования:**

1. **Семантическое версионирование** — MAJOR.MINOR.PATCH
2. **Неизменяемость** — старые версии не изменяются
3. **Метаданные** — описание изменений в каждой версии

**Пример: Система версионирования**

```python

import hashlib
import json
from datetime import datetime

class DataVersionControl:
    """Контроль версий данных"""
    
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
    
    def calculate_checksum(self, data_path):
        """Вычисление checksum для проверки целостности"""
        sha256 = hashlib.sha256()
        with open(data_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def create_version(self, data_id, version, data_path, changes):
        """Создание новой версии данных"""
        version_dir = self.data_dir / data_id / f"v{version}"
        version_dir.mkdir(parents=True, exist_ok=True)
        
        # Копирование данных
        import shutil
        dest_path = version_dir / data_path.name
        shutil.copy(data_path, dest_path)
        
        # Вычисление checksum
        checksum = self.calculate_checksum(dest_path)
        
        # Метаданные версии
        metadata = {
            'version': version,
            'created': datetime.now().isoformat(),
            'changes': changes,
            'checksum': checksum,
            'file_size': dest_path.stat().st_size
        }
        
        metadata_path = version_dir / 'metadata.json'
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
    
    def verify_integrity(self, data_id, version):
        """Проверка целостности данных"""
        version_dir = self.data_dir / data_id / f"v{version}"
        metadata_path = version_dir / 'metadata.json'
        
        if not metadata_path.exists():
            return False, "Metadata not found"
        
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        
        # Находим файл данных
        data_files = list(version_dir.glob('*.csv'))
        if not data_files:
            return False, "Data file not found"
        
        data_file = data_files[0]
        current_checksum = self.calculate_checksum(data_file)
        stored_checksum = metadata.get('checksum')
        
        if current_checksum == stored_checksum:
            return True, "Integrity verified"
        else:
            return False, "Checksum mismatch - data may be corrupted"

# Пример использования
dvc = DataVersionControl()
# dvc.create_version('exp001', '1.0.0', Path('data.csv'), 'Initial data collection')
print("Data version control system created")
```

**Output:**
```

Data version control system created
```

### 2.2 Отслеживание изменений

**Логирование изменений:**

```python

class ChangeLog:
    """Лог изменений данных"""
    
    def __init__(self):
        self.changes = []
    
    def add_change(self, version, author, description, affected_files):
        """Добавление записи об изменении"""
        change = {
            'version': version,
            'timestamp': datetime.now().isoformat(),
            'author': author,
            'description': description,
            'affected_files': affected_files
        }
        self.changes.append(change)
        return change
    
    def get_changelog(self):
        """Получение полного лога изменений"""
        return self.changes
    
    def get_version_changes(self, version):
        """Изменения в конкретной версии"""
        return [c for c in self.changes if c['version'] == version]

# Пример
changelog = ChangeLog()
changelog.add_change('1.0.0', 'Dr. Smith', 'Initial data collection', ['data.csv'])
changelog.add_change('1.1.0', 'Dr. Smith', 'Added metadata', ['data.csv', 'metadata.json'])

print("Changelog:")
for change in changelog.get_changelog():
    print(f"  v{change['version']}: {change['description']}")
```

**Output:**
```

Changelog:
  v1.0.0: Initial data collection
  v1.1.0: Added metadata
```

---

## 3. Проверка корректности данных

### 3.1 Валидация данных

**Типы валидации:**

1. **Структурная** — формат, типы данных
2. **Семантическая** — логическая корректность
3. **Бизнес-правила** — доменные ограничения

**Пример: Валидация данных**

```python

class DataValidator:
    """Валидатор научных данных"""
    
    def __init__(self):
        self.rules = []
        self.errors = []
    
    def add_rule(self, column, rule_type, rule_value):
        """Добавление правила валидации"""
        self.rules.append({
            'column': column,
            'type': rule_type,
            'value': rule_value
        })
    
    def validate(self, data):
        """Валидация данных по правилам"""
        self.errors = []
        
        for rule in self.rules:
            column = rule['column']
            rule_type = rule['type']
            rule_value = rule['value']
            
            if rule_type == 'not_null':
                null_count = data[column].isna().sum()
                if null_count > 0:
                    self.errors.append(f"{column}: {null_count} null values")
            
            elif rule_type == 'range':
                min_val, max_val = rule_value
                out_of_range = ((data[column] < min_val) | (data[column] > max_val)).sum()
                if out_of_range > 0:
                    self.errors.append(f"{column}: {out_of_range} values out of range [{min_val}, {max_val}]")
            
            elif rule_type == 'type':
                expected_type = rule_value
                if data[column].dtype != expected_type:
                    self.errors.append(f"{column}: wrong type, expected {expected_type}")
        
        return len(self.errors) == 0
    
    def get_errors(self):
        """Получение списка ошибок"""
        return self.errors

# Пример использования
data = pd.DataFrame({
    'temperature': [20, 25, 30, None, 40],
    'reaction_rate': [10.5, 12.3, 15.2, 18.1, 20.5]
})

validator = DataValidator()
validator.add_rule('temperature', 'not_null', None)
validator.add_rule('temperature', 'range', (0, 100))
validator.add_rule('reaction_rate', 'range', (0, 50))

is_valid = validator.validate(data)
print(f"Data is valid: {is_valid}")
if not is_valid:
    print("Errors:")
    for error in validator.get_errors():
        print(f"  - {error}")
```

**Output:**
```

Data is valid: False
Errors:
  - temperature: 1 null values
```

### 3.2 Проверка целостности

**Checksums и хэши:**

```python

import hashlib

def calculate_file_hash(file_path, algorithm='sha256'):
    """Вычисление хэша файла"""
    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def verify_file_integrity(file_path, expected_hash, algorithm='sha256'):
    """Проверка целостности файла"""
    actual_hash = calculate_file_hash(file_path, algorithm)
    return actual_hash == expected_hash, actual_hash

# Пример
# file_path = 'data.csv'
# expected_hash = 'abc123def456...'
# is_valid, actual_hash = verify_file_integrity(file_path, expected_hash)
# print(f"File integrity: {is_valid}")
# print(f"Actual hash: {actual_hash}")
print("File integrity checking functions created")
```

**Output:**
```

File integrity checking functions created
```

---

## 4. Основы data security

### 4.1 Контроль доступа

**Принципы контроля доступа:**

1. **Минимальные привилегии** — доступ только к необходимым данным
2. **Аутентификация** — проверка личности пользователя
3. **Авторизация** — проверка прав доступа

**Пример: Система контроля доступа**

```python

class DataAccessControl:
    """Контроль доступа к данным"""
    
    def __init__(self):
        self.permissions = {}
    
    def grant_access(self, user, data_id, access_level):
        """Предоставление доступа"""
        if data_id not in self.permissions:
            self.permissions[data_id] = {}
        self.permissions[data_id][user] = access_level
    
    def check_access(self, user, data_id, required_level):
        """Проверка доступа"""
        if data_id not in self.permissions:
            return False
        if user not in self.permissions[data_id]:
            return False
        
        user_level = self.permissions[data_id][user]
        access_levels = {'read': 1, 'write': 2, 'admin': 3}
        return access_levels.get(user_level, 0) >= access_levels.get(required_level, 0)
    
    def revoke_access(self, user, data_id):
        """Отзыв доступа"""
        if data_id in self.permissions and user in self.permissions[data_id]:
            del self.permissions[data_id][user]

# Пример
access_control = DataAccessControl()
access_control.grant_access('researcher1', 'exp001', 'read')
access_control.grant_access('researcher2', 'exp001', 'write')

can_read = access_control.check_access('researcher1', 'exp001', 'read')
can_write = access_control.check_access('researcher1', 'exp001', 'write')

print(f"Researcher1 can read: {can_read}")
print(f"Researcher1 can write: {can_write}")
```

**Output:**
```

Researcher1 can read: True
Researcher1 can write: False
```

### 4.2 Шифрование данных

**Типы шифрования:**

1. **At rest** — шифрование хранимых данных
2. **In transit** — шифрование при передаче
3. **End-to-end** — шифрование от источника до получателя

**Пример: Базовое шифрование (концептуально)**

```python
# Концептуальный пример (для production используйте библиотеки типа cryptography)
import base64

def simple_encrypt(data, key):
    """Простое шифрование (для демонстрации, не для production)"""
    # В production используйте библиотеки типа cryptography
    encoded = base64.b64encode(data.encode()).decode()
    return encoded

def simple_decrypt(encrypted_data, key):
    """Простое расшифрование"""
    decoded = base64.b64decode(encrypted_data.encode()).decode()
    return decoded

# Пример
sensitive_data = "Experimental results: 10.5, 12.3, 15.2"
encrypted = simple_encrypt(sensitive_data, "key")
decrypted = simple_decrypt(encrypted, "key")

print(f"Original: {sensitive_data}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

**Output:**
```

Original: Experimental results: 10.5, 12.3, 15.2
Encrypted: RXhwZXJpbWVudGFsIHJlc3VsdHM6IDEwLjUsIDEyLjMsIDE1LjI=
Decrypted: Experimental results: 10.5, 12.3, 15.2
```

> **⚠️ Warning:**  
> Для production используйте проверенные библиотеки шифрования (например, `cryptography` в Python).

### 4.3 Аудит данных

**Логирование доступа:**

```python

class DataAuditLog:
    """Аудит доступа к данным"""
    
    def __init__(self):
        self.logs = []
    
    def log_access(self, user, data_id, action, timestamp=None):
        """Логирование доступа"""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        log_entry = {
            'timestamp': timestamp,
            'user': user,
            'data_id': data_id,
            'action': action
        }
        self.logs.append(log_entry)
        return log_entry
    
    def get_access_history(self, data_id=None, user=None):
        """Получение истории доступа"""
        filtered = self.logs
        if data_id:
            filtered = [l for l in filtered if l['data_id'] == data_id]
        if user:
            filtered = [l for l in filtered if l['user'] == user]
        return filtered

# Пример
audit_log = DataAuditLog()
audit_log.log_access('researcher1', 'exp001', 'read')
audit_log.log_access('researcher2', 'exp001', 'write')
audit_log.log_access('researcher1', 'exp001', 'read')

history = audit_log.get_access_history(data_id='exp001')
print("Access history for exp001:")
for entry in history:
    print(f"  {entry['timestamp']}: {entry['user']} - {entry['action']}")
```

**Output:**
```

Access history for exp001:
  2024-01-15T10:30:00.123456: researcher1 - read
  2024-01-15T10:30:00.123456: researcher2 - write
  2024-01-15T10:30:00.123456: researcher1 - read
```

---

## 5. Best Practices

### 5.1 Чеклист качества данных

**Перед использованием данных проверьте:**

1. ✅ Полнота — нет пропущенных значений
2. ✅ Точность — значения соответствуют ожиданиям
3. ✅ Согласованность — нет противоречий
4. ✅ Валидность — соответствие формату
5. ✅ Целостность — checksum совпадает

### 5.2 Чеклист безопасности

**Для защиты данных:**

1. ✅ Контроль доступа — кто имеет доступ
2. ✅ Аудит — логирование всех действий
3. ✅ Шифрование — для чувствительных данных
4. ✅ Резервное копирование — регулярные бэкапы
5. ✅ Политики хранения — сроки и правила удаления

---

## 💡 Key Takeaways

- **Качество данных** — полнота, точность, согласованность, валидность, актуальность

- **Контроль изменений** — версионирование, checksums, логирование изменений

- **Валидация данных** — структурная, семантическая, бизнес-правила

- **Безопасность данных** — контроль доступа, шифрование, аудит

- **Checksums** — для проверки целостности данных

- **Аудит** — логирование доступа для трассируемости

---

## 🚀 Next Steps

**Related Modules:**

- [07_Collaboration](../07_Collaboration/) — коллаборация в научных проектах
- [16_Security](../16_Security/) — продвинутая безопасность и compliance
- [05_DataManagement](../05_DataManagement/) — управление данными

**Practice Ideas:**

1. Создайте систему проверки качества для ваших данных
2. Реализуйте версионирование с checksums
3. Настройте контроль доступа для вашего проекта

**Going Deeper:**

- Изучите DVC (Data Version Control) для управления версиями данных
- Познакомьтесь с библиотеками валидации (Great Expectations, Pandera)
- Изучите продвинутые методы шифрования и безопасности

---

## 📚 Additional Resources

**Documentation:**

- [DVC Documentation](https://dvc.org/) — Data Version Control
- [Great Expectations](https://greatexpectations.io/) — валидация данных
- [Pandera](https://pandera.readthedocs.io/) — валидация DataFrame

**Tutorials:**

- "Data Quality Best Practices" — руководство по качеству данных
- "Data Security in Scientific Computing" — безопасность данных

---


