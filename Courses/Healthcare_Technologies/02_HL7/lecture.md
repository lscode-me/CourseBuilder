# HL7 v2 — Health Level 7
## Стандарт обмена медицинскими данными

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовую медицинскую терминологию (Patient, Encounter, Diagnosis)
- Понимать основы работы с текстовыми протоколами
- Иметь опыт работы с Python

**Recommended prior modules:**

- [01_Terminology](../01_Terminology/) — базовая медицинская терминология

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру HL7 v2 сообщений (сегменты, поля, компоненты)
- Парсить HL7 v2 сообщения в Python
- Работать с основными типами сообщений (ADT, ORM, ORU)
- Создавать и валидировать HL7 v2 сообщения

---

## 1. Введение в HL7

### 1.1 Что такое HL7?

**HL7 (Health Level 7)** — международный стандарт для обмена, интеграции и извлечения электронной медицинской информации.

**Почему "Level 7"?**
- Ссылка на 7-й уровень модели OSI (Application Layer)
- HL7 определяет формат данных на уровне приложений

```

┌─────────────────────────────────────────────────────────────────────────────┐
│                         OSI Model & HL7                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  7. Application    ◄─── HL7 works here                                      │
│  6. Presentation                                                             │
│  5. Session                                                                  │
│  4. Transport      ◄─── TCP (MLLP - Minimal Lower Layer Protocol)           │
│  3. Network                                                                  │
│  2. Data Link                                                                │
│  1. Physical                                                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

```

### 1.2 Версии HL7

```python

hl7_versions = {
    "v2.x": {
        "years": "1988 - настоящее время",
        "format": "Pipe-delimited text (|)",
        "status": "~95% медицинских учреждений используют",
        "versions": ["2.3", "2.4", "2.5", "2.5.1", "2.6", "2.7", "2.8", "2.9"],
        "pros": "Простой, широко поддерживается",
        "cons": "Слишком гибкий → проблемы совместимости"
    },
    "v3": {
        "years": "2005 - почти не используется",
        "format": "XML-based",
        "status": "Провалился — слишком сложный",
        "pros": "Теоретически строгий",
        "cons": "Дорогая имплементация, громоздкий"
    },
    "FHIR": {
        "years": "2014 - настоящее время",
        "format": "REST API + JSON/XML",
        "status": "Быстро набирает популярность",
        "pros": "Современный, удобный для разработчиков",
        "cons": "Ещё не везде поддерживается"
    }
}

```

### 1.3 Где используется HL7 v2

```

┌─────────────────────────────────────────────────────────────────────────────┐
│                    Типичная интеграция с HL7 v2                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│    ┌─────────────┐      ADT      ┌─────────────┐                            │
│    │    EHR      │──────────────►│   Pharmacy  │  Patient registration      │
│    │             │               │   System    │                            │
│    └──────┬──────┘               └─────────────┘                            │
│           │                                                                  │
│           │ ORM (Order)                                                      │
│           ▼                                                                  │
│    ┌─────────────┐      ORU      ┌─────────────┐                            │
│    │    Lab      │──────────────►│    EHR      │  Lab results               │
│    │   (LIS)     │               │             │                            │
│    └─────────────┘               └─────────────┘                            │
│                                                                              │
│    Протокол передачи: MLLP (TCP) или HTTP                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

```

---

## 2. Структура HL7 v2 сообщения

### 2.1 Иерархия элементов

```

MESSAGE
├── SEGMENT (строка, 3-буквенный код)
│   ├── FIELD (разделитель |)
│   │   ├── COMPONENT (разделитель ^)
│   │   │   └── SUBCOMPONENT (разделитель &)
│   │   └── REPETITION (разделитель ~)
│   └── ...
└── ...

```

### 2.2 Пример сообщения

```

MSH|^~\&|SENDING_APP|SENDING_FAC|RECEIVING_APP|RECEIVING_FAC|20240315120000||ADT^A01|MSG001|P|2.5
EVN|A01|20240315120000|||USER001
PID|1||MRN-123456^^^HOSPITAL^MR||Иванов^Иван^Петрович^^||19800515|M|||ул. Примерная 10^^Москва^^123456^RU||+7-999-123-4567
PV1|1|I|ICU^201^A|||DOC001^Смирнова^Анна^^^Др.||||MED||||ADM|A0||||||||||||||||||||||||||20240315120000

```

### 2.3 Разбор структуры

#### MSH (Message Header)

```python
# MSH — первый сегмент в любом HL7 сообщении
msh_segment = "MSH|^~\\&|SENDING_APP|SENDING_FAC|RECEIVING_APP|RECEIVING_FAC|20240315120000||ADT^A01|MSG001|P|2.5"

msh_fields = {
    "MSH-1": "|",                      # Field separator
    "MSH-2": "^~\\&",                  # Encoding characters
    "MSH-3": "SENDING_APP",            # Sending Application
    "MSH-4": "SENDING_FAC",            # Sending Facility
    "MSH-5": "RECEIVING_APP",          # Receiving Application
    "MSH-6": "RECEIVING_FAC",          # Receiving Facility
    "MSH-7": "20240315120000",         # Date/Time of Message
    "MSH-8": "",                       # Security (пусто)
    "MSH-9": "ADT^A01",                # Message Type^Trigger Event
    "MSH-10": "MSG001",                # Message Control ID
    "MSH-11": "P",                     # Processing ID (P=Production, T=Test, D=Debug)
    "MSH-12": "2.5"                    # Version ID
}

# Encoding Characters (MSH-2): ^~\&
encoding_chars = {
    "^": "Component separator",        # Разделитель компонентов
    "~": "Repetition separator",       # Разделитель повторений
    "\\": "Escape character",          # Escape символ
    "&": "Subcomponent separator"      # Разделитель подкомпонентов
}

```

#### PID (Patient Identification)

```python
# PID — информация о пациенте
pid_segment = "PID|1||MRN-123456^^^HOSPITAL^MR||Иванов^Иван^Петрович^^||19800515|M|||ул. Примерная 10^^Москва^^123456^RU||+7-999-123-4567"

pid_fields = {
    "PID-1": "1",                      # Set ID
    "PID-2": "",                       # Patient ID (External) - устаревшее
    "PID-3": "MRN-123456^^^HOSPITAL^MR",  # Patient Identifier List
    "PID-4": "",                       # Alternate Patient ID
    "PID-5": "Иванов^Иван^Петрович^^", # Patient Name
    "PID-6": "",                       # Mother's Maiden Name
    "PID-7": "19800515",               # Date of Birth (YYYYMMDD)
    "PID-8": "M",                      # Administrative Sex
    "PID-9": "",                       # Patient Alias
    "PID-10": "",                      # Race
    "PID-11": "ул. Примерная 10^^Москва^^123456^RU",  # Patient Address
}

# Разбор PID-5 (Patient Name): Иванов^Иван^Петрович^^
name_components = {
    "family_name": "Иванов",           # Фамилия
    "given_name": "Иван",              # Имя
    "middle_name": "Петрович",         # Отчество
    "suffix": "",                      # Суффикс (Jr, Sr, III)
    "prefix": ""                       # Префикс (Dr, Mr)
}

# Разбор PID-3 (Patient Identifier): MRN-123456^^^HOSPITAL^MR
identifier_components = {
    "id_number": "MRN-123456",         # Номер
    "check_digit": "",                 # Контрольная цифра
    "check_digit_scheme": "",          # Схема
    "assigning_authority": "HOSPITAL", # Источник
    "identifier_type": "MR"            # Тип (MR = Medical Record)
}

```

#### PV1 (Patient Visit)

```python
# PV1 — информация о визите
pv1_fields = {
    "PV1-1": "1",                      # Set ID
    "PV1-2": "I",                      # Patient Class (I=Inpatient, O=Outpatient, E=Emergency)
    "PV1-3": "ICU^201^A",              # Assigned Patient Location (отделение^палата^койка)
    "PV1-7": "DOC001^Смирнова^Анна^^^Др.",  # Attending Doctor
    "PV1-44": "20240315120000"         # Admit Date/Time
}

patient_classes = {
    "I": "Inpatient (стационар)",
    "O": "Outpatient (амбулаторный)",
    "E": "Emergency (экстренный)",
    "P": "Preadmit",
    "R": "Recurring patient",
    "B": "Obstetrics"
}

```

---

## 3. Типы сообщений

### 3.1 ADT — Admission, Discharge, Transfer

```python

adt_message_types = {
    "ADT^A01": {
        "name": "Admit/Visit Notification",
        "description": "Поступление пациента (госпитализация)",
        "use_case": "Пациент поступил в стационар"
    },
    "ADT^A02": {
        "name": "Transfer a Patient",
        "description": "Перевод пациента в другое отделение",
        "use_case": "Из терапии в хирургию"
    },
    "ADT^A03": {
        "name": "Discharge a Patient",
        "description": "Выписка пациента",
        "use_case": "Пациент выписан домой"
    },
    "ADT^A04": {
        "name": "Register a Patient",
        "description": "Регистрация амбулаторного пациента",
        "use_case": "Пациент пришёл на приём"
    },
    "ADT^A08": {
        "name": "Update Patient Information",
        "description": "Обновление данных пациента",
        "use_case": "Изменился адрес или телефон"
    },
    "ADT^A28": {
        "name": "Add Person Information",
        "description": "Добавление нового пациента",
        "use_case": "Новый пациент в системе"
    },
    "ADT^A31": {
        "name": "Update Person Information",
        "description": "Обновление демографических данных",
        "use_case": "Изменение имени, адреса"
    }
}

```

### 3.2 ORM — Orders

```python

orm_message_types = {
    "ORM^O01": {
        "name": "Order Message",
        "description": "Назначение обследования/процедуры",
        "use_case": "Врач назначил анализ крови",
        "segments": ["MSH", "PID", "PV1", "ORC", "OBR"]
    }
}

# Пример ORM^O01 сообщения
orm_example = """
MSH|^~\\&|EHR|HOSPITAL|LAB|HOSPITAL|20240315100000||ORM^O01|ORD001|P|2.5
PID|1||MRN-123456||Иванов^Иван||19800515|M
PV1|1|O|CLINIC^^^HOSPITAL
ORC|NW|ORD-2024-001||||||20240315100000|||DOC001^Смирнова^Анна
OBR|1|ORD-2024-001||CBC^Complete Blood Count|||20240315100000
"""

```

### 3.3 ORU — Observation Results

```python

oru_message_types = {
    "ORU^R01": {
        "name": "Observation Result",
        "description": "Результаты лабораторных анализов",
        "use_case": "Готов общий анализ крови",
        "segments": ["MSH", "PID", "PV1", "ORC", "OBR", "OBX"]
    }
}

# Пример ORU^R01 сообщения с результатами
oru_example = """
MSH|^~\\&|LAB|HOSPITAL|EHR|HOSPITAL|20240315143000||ORU^R01|LAB001|P|2.5
PID|1||MRN-123456||Иванов^Иван||19800515|M
OBR|1||LAB-2024-001|CBC^Complete Blood Count|||20240315140000
OBX|1|NM|718-7^Hemoglobin^LN||145|g/L|130-175|N|||F
OBX|2|NM|787-2^WBC^LN||8.5|10*9/L|4.0-11.0|N|||F
OBX|3|NM|777-3^Platelets^LN||250|10*9/L|150-400|N|||F
"""

```

### 3.4 OBX — Observation Segment

```python
# OBX содержит результаты наблюдений
obx_fields = {
    "OBX-1": "1",                      # Set ID
    "OBX-2": "NM",                     # Value Type (NM=Numeric, ST=String, TX=Text)
    "OBX-3": "718-7^Hemoglobin^LN",    # Observation Identifier (LOINC)
    "OBX-4": "",                       # Observation Sub-ID
    "OBX-5": "145",                    # Observation Value
    "OBX-6": "g/L",                    # Units
    "OBX-7": "130-175",                # Reference Range
    "OBX-8": "N",                      # Abnormal Flags (N=Normal, L=Low, H=High)
    "OBX-11": "F"                      # Observation Result Status (F=Final)
}

value_types = {
    "NM": "Numeric",
    "ST": "String",
    "TX": "Text",
    "DT": "Date",
    "TM": "Time",
    "TS": "Timestamp",
    "CE": "Coded Element"
}

abnormal_flags = {
    "N": "Normal",
    "L": "Below low normal",
    "H": "Above high normal",
    "LL": "Below lower panic limits",
    "HH": "Above upper panic limits",
    "A": "Abnormal"
}

```

---

## 4. Парсинг HL7 в Python

### 4.1 Библиотека python-hl7

```bash

pip install hl7

```

### 4.2 Базовый парсинг

```python

import hl7

# HL7 сообщение
hl7_message = """MSH|^~\\&|SENDING_APP|HOSPITAL|RECEIVING_APP|HOSPITAL|20240315120000||ADT^A01|MSG001|P|2.5
EVN|A01|20240315120000
PID|1||MRN-123456^^^HOSPITAL^MR||Иванов^Иван^Петрович||19800515|M|||ул. Примерная 10^^Москва^^123456
PV1|1|I|ICU^201^A|||DOC001^Смирнова^Анна|||MED||||ADM"""

# Парсинг
message = hl7.parse(hl7_message)

# Доступ к сегментам
msh = message.segment('MSH')
pid = message.segment('PID')
pv1 = message.segment('PV1')

# Доступ к полям
print(f"Message Type: {msh[9]}")       # ADT^A01
print(f"Message ID: {msh[10]}")        # MSG001
print(f"HL7 Version: {msh[12]}")       # 2.5

```

**Output:**
```

Message Type: ADT^A01
Message ID: MSG001
HL7 Version: 2.5

```

### 4.3 Извлечение данных пациента

```python

import hl7
from datetime import datetime

def parse_patient_from_hl7(hl7_message: str) -> dict:
    """Извлекает данные пациента из HL7 сообщения."""
    
    message = hl7.parse(hl7_message)
    pid = message.segment('PID')
    
    # PID-3: Patient Identifier
    patient_id_field = pid[3]
    patient_id = str(patient_id_field[0][0]) if patient_id_field else None
    
    # PID-5: Patient Name
    name_field = pid[5]
    family_name = str(name_field[0][0]) if len(name_field[0]) > 0 else ""
    given_name = str(name_field[0][1]) if len(name_field[0]) > 1 else ""
    middle_name = str(name_field[0][2]) if len(name_field[0]) > 2 else ""
    
    # PID-7: Date of Birth
    dob_str = str(pid[7])
    dob = None
    if dob_str and len(dob_str) >= 8:
        dob = datetime.strptime(dob_str[:8], '%Y%m%d').date()
    
    # PID-8: Gender
    gender = str(pid[8])
    
    # PID-11: Address
    address_field = pid[11]
    address = {
        "street": str(address_field[0][0]) if address_field else "",
        "city": str(address_field[0][2]) if len(address_field[0]) > 2 else "",
        "postal_code": str(address_field[0][4]) if len(address_field[0]) > 4 else ""
    }
    
    return {
        "patient_id": patient_id,
        "name": {
            "family": family_name,
            "given": given_name,
            "middle": middle_name
        },
        "birth_date": dob,
        "gender": gender,
        "address": address
    }

# Использование
patient = parse_patient_from_hl7(hl7_message)
print(f"Patient: {patient['name']['given']} {patient['name']['family']}")
print(f"DOB: {patient['birth_date']}")
print(f"Gender: {patient['gender']}")

```

### 4.4 Парсинг результатов анализов

```python

def parse_lab_results(hl7_message: str) -> list:
    """Извлекает результаты лабораторных анализов из ORU сообщения."""
    
    message = hl7.parse(hl7_message)
    results = []
    
    # Находим все OBX сегменты
    for segment in message:
        if str(segment[0]) == 'OBX':
            # OBX-3: Observation Identifier
            obs_id = segment[3]
            code = str(obs_id[0][0]) if obs_id else ""
            display = str(obs_id[0][1]) if len(obs_id[0]) > 1 else ""
            
            # OBX-5: Value
            value = str(segment[5])
            
            # OBX-6: Units
            units = str(segment[6])
            
            # OBX-7: Reference Range
            ref_range = str(segment[7])
            
            # OBX-8: Abnormal Flag
            flag = str(segment[8])
            
            results.append({
                "code": code,
                "display": display,
                "value": float(value) if value.replace('.', '').isdigit() else value,
                "units": units,
                "reference_range": ref_range,
                "flag": flag,
                "interpretation": interpret_flag(flag)
            })
    
    return results

def interpret_flag(flag: str) -> str:
    """Интерпретирует abnormal flag."""
    interpretations = {
        "N": "Normal",
        "L": "Low",
        "H": "High",
        "LL": "Critical Low",
        "HH": "Critical High",
        "A": "Abnormal"
    }
    return interpretations.get(flag, "Unknown")

# Пример использования
oru_message = """MSH|^~\\&|LAB|HOSPITAL|EHR|HOSPITAL|20240315143000||ORU^R01|LAB001|P|2.5
PID|1||MRN-123456||Иванов^Иван||19800515|M
OBR|1||LAB-2024-001|CBC^Complete Blood Count|||20240315140000
OBX|1|NM|718-7^Hemoglobin^LN||145|g/L|130-175|N|||F
OBX|2|NM|787-2^WBC^LN||12.5|10*9/L|4.0-11.0|H|||F
OBX|3|NM|777-3^Platelets^LN||250|10*9/L|150-400|N|||F"""

results = parse_lab_results(oru_message)
print("\nЛабораторные результаты:")
print("-" * 60)
for r in results:
    status = "⚠️" if r["flag"] != "N" else "✓"
    print(f"{status} {r['display']}: {r['value']} {r['units']} "
          f"(ref: {r['reference_range']}) - {r['interpretation']}")

```

**Output:**
```

Лабораторные результаты:
------------------------------------------------------------
✓ Hemoglobin: 145.0 g/L (ref: 130-175) - Normal
⚠️ WBC: 12.5 10*9/L (ref: 4.0-11.0) - High
✓ Platelets: 250.0 10*9/L (ref: 150-400) - Normal

```

### 4.5 Создание HL7 сообщения

```python

from datetime import datetime

def create_adt_a04(patient_id: str, family_name: str, given_name: str, 
                   dob: str, gender: str, facility: str = "HOSPITAL") -> str:
    """Создаёт ADT^A04 сообщение (регистрация амбулаторного пациента)."""
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    msg_id = f"MSG{timestamp}"
    
    segments = [
        f"MSH|^~\\&|EHR|{facility}|ADT|{facility}|{timestamp}||ADT^A04|{msg_id}|P|2.5",
        f"EVN|A04|{timestamp}",
        f"PID|1||{patient_id}^^^{facility}^MR||{family_name}^{given_name}||{dob}|{gender}",
        f"PV1|1|O|OUTPATIENT^^^{facility}||||DOC001^Врач^Дежурный"
    ]
    
    # HL7 использует \r как разделитель сегментов
    return "\r".join(segments)

# Создание сообщения
adt_message = create_adt_a04(
    patient_id="MRN-999888",
    family_name="Петров",
    given_name="Пётр",
    dob="19901231",
    gender="M"
)

print("Созданное ADT^A04 сообщение:")
print("-" * 60)
print(adt_message.replace("\r", "\n"))

```

---

## 5. Валидация HL7 сообщений

```python

def validate_hl7_message(hl7_string: str) -> tuple[bool, list]:
    """Базовая валидация HL7 сообщения."""
    
    errors = []
    
    # Попытка парсинга
    try:
        message = hl7.parse(hl7_string)
    except Exception as e:
        return False, [f"Parse error: {e}"]
    
    # Проверка MSH
    msh = message.segment('MSH')
    if not msh:
        errors.append("Missing required MSH segment")
    else:
        # Проверка версии
        version = str(msh[12])
        valid_versions = ['2.3', '2.4', '2.5', '2.5.1', '2.6', '2.7', '2.8', '2.9']
        if version not in valid_versions:
            errors.append(f"Unsupported HL7 version: {version}")
        
        # Проверка типа сообщения
        msg_type = str(msh[9])
        if not msg_type:
            errors.append("Missing message type (MSH-9)")
        
        # Проверка Message Control ID
        msg_id = str(msh[10])
        if not msg_id:
            errors.append("Missing Message Control ID (MSH-10)")
    
    # Для ADT сообщений проверяем PID
    if msh and str(msh[9]).startswith('ADT'):
        pid = message.segment('PID')
        if not pid:
            errors.append("ADT message missing required PID segment")
        else:
            # Проверка Patient ID
            if not str(pid[3]):
                errors.append("Missing Patient ID (PID-3)")
    
    return len(errors) == 0, errors

# Пример валидации
is_valid, validation_errors = validate_hl7_message(hl7_message)
if is_valid:
    print("✓ HL7 message is valid")
else:
    print("✗ Validation errors:")
    for error in validation_errors:
        print(f"  - {error}")

```

---

## 6. Частые проблемы и решения

### 6.1 Escape-последовательности

```python
# HL7 использует escape-последовательности для специальных символов
escape_sequences = {
    "\\F\\": "|",    # Field separator
    "\\S\\": "^",    # Component separator
    "\\T\\": "&",    # Subcomponent separator
    "\\R\\": "~",    # Repetition separator
    "\\E\\": "\\"    # Escape character
}

def unescape_hl7(text: str) -> str:
    """Обрабатывает escape-последовательности в HL7 тексте."""
    result = text
    for escape, char in escape_sequences.items():
        result = result.replace(escape, char)
    return result

# Пример: текст с escape-последовательностями
escaped_text = "Blood Pressure \\T\\ Systolic\\S\\Diastolic"
unescaped = unescape_hl7(escaped_text)
print(f"Original: {escaped_text}")
print(f"Unescaped: {unescaped}")

```

### 6.2 Обработка пустых полей

```python

def safe_get_field(segment, index: int, default: str = "") -> str:
    """Безопасное получение поля с учётом пустых значений."""
    try:
        value = str(segment[index])
        return value if value and value != '""' else default
    except (IndexError, TypeError):
        return default

def safe_get_component(field, index: int, default: str = "") -> str:
    """Безопасное получение компонента."""
    try:
        if hasattr(field, '__getitem__') and len(field) > 0:
            components = field[0]
            if len(components) > index:
                return str(components[index]) or default
        return default
    except (IndexError, TypeError):
        return default

```

### 6.3 Работа с датами

```python

from datetime import datetime

def parse_hl7_datetime(dt_string: str) -> datetime | None:
    """Парсит HL7 дату/время в различных форматах."""
    
    formats = [
        '%Y%m%d%H%M%S',     # YYYYMMDDHHMMSS
        '%Y%m%d%H%M',       # YYYYMMDDHHMM
        '%Y%m%d',           # YYYYMMDD
        '%Y%m'              # YYYYMM
    ]
    
    # Убираем часовой пояс если есть
    dt_string = dt_string.split('+')[0].split('-')[0][:14]
    
    for fmt in formats:
        try:
            return datetime.strptime(dt_string[:len(fmt.replace('%', ''))], fmt)
        except ValueError:
            continue
    
    return None

# Примеры
dates = ["20240315143000", "202403151430", "20240315", "202403"]
for d in dates:
    parsed = parse_hl7_datetime(d)
    print(f"{d} → {parsed}")

```

---

## 7. MLLP — Minimal Lower Layer Protocol

```python
# MLLP — протокол для передачи HL7 по TCP
# Структура: <VT>MESSAGE<FS><CR>

MLLP_START = b'\x0b'  # VT (Vertical Tab) - начало сообщения
MLLP_END = b'\x1c'    # FS (File Separator) - конец сообщения
MLLP_CR = b'\x0d'     # CR (Carriage Return)

def wrap_mllp(message: str) -> bytes:
    """Оборачивает HL7 сообщение в MLLP."""
    return MLLP_START + message.encode('utf-8') + MLLP_END + MLLP_CR

def unwrap_mllp(data: bytes) -> str:
    """Извлекает HL7 сообщение из MLLP."""
    # Убираем MLLP wrapper
    if data.startswith(MLLP_START):
        data = data[1:]
    if data.endswith(MLLP_CR):
        data = data[:-1]
    if data.endswith(MLLP_END):
        data = data[:-1]
    return data.decode('utf-8')

```

---

## 💡 Key Takeaways

- **HL7 v2** — текстовый pipe-delimited формат, широко используется в legacy системах

- **MSH** — обязательный заголовок каждого сообщения

- **PID** — информация о пациенте, PV1 — о визите

- **ADT** — события регистрации/выписки, ORM — назначения, ORU — результаты

- **OBX** — содержит результаты наблюдений с кодами LOINC

- **MLLP** — протокол передачи HL7 по TCP

---

## 🚀 Next Steps

**Следующие модули:**

- [03_FHIR](../03_FHIR/) — Современный FHIR стандарт
- [04_Standards](../04_Standards/) — ICD-10, SNOMED CT, LOINC

**Практика:**

1. Напишите парсер HL7 для извлечения данных пациента
2. Создайте ADT^A01 сообщение
3. Реализуйте валидатор HL7 сообщений
4. Напишите конвертер HL7 → JSON

---

## 📚 Additional Resources

- [HL7 International](https://www.hl7.org/)
- [HL7 v2.5 Specification](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=144)
- [python-hl7 Documentation](https://python-hl7.readthedocs.io/)

---





