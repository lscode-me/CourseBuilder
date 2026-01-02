# Медицинская Терминология для IT-специалистов
## Базовые концепции и понятия Healthcare IT

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь базовые знания программирования (Python предпочтительно)
- Понимать основы работы с JSON и XML
- Иметь представление о REST API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать базовую медицинскую терминологию (Patient, Encounter, Diagnosis)
- Понимать структуру медицинских данных и их типы
- Ориентироваться в системе идентификаторов в Healthcare
- Понимать роль стандартов в медицинских IT-системах

---

## 1. Введение в Healthcare IT

### 1.1 Почему это важно

Работа в Healthcare IT требует понимания специфической терминологии и процессов. Даже если вы опытный разработчик, медицинский домен имеет свои особенности:

**Ключевые отличия от других доменов:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                Healthcare IT vs Другие домены                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ Критичность данных         — ошибка может стоить жизни                  │
│  ✓ Регуляторные требования    — HIPAA, GDPR, строгий compliance            │
│  ✓ Legacy системы             — HL7 v2 (1988) до сих пор используется      │
│  ✓ Интеграция                 — десятки систем должны работать вместе      │
│  ✓ Стандартизация             — ICD-10, SNOMED CT, LOINC, FHIR             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Экосистема Healthcare IT

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Healthcare IT Ecosystem                               │
│                                                                             │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│    │     EHR      │◄──►│    Lab       │◄──►│   Radiology  │                 │
│    │   (EMR)      │    │   (LIS)      │    │  (RIS/PACS)  │                 │
│    └──────┬───────┘    └──────┬───────┘    └──────┬───────┘                 │
│           │                   │                   │                         │
│           └───────────────────┼───────────────────┘                         │
│                               │                                             │
│                        ┌──────▼───────┐                                     │
│                        │  Integration │                                     │
│                        │    Engine    │                                     │
│                        │   (HL7/FHIR) │                                     │
│                        └──────┬───────┘                                     │
│                               │                                             │
│    ┌──────────────────────────┼──────────────────────────┐                  │
│    │                          │                          │                  │
│    ▼                          ▼                          ▼                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   Pharmacy   │    │   Billing    │    │   Patient    │                   │
│  │   System     │    │   System     │    │   Portal     │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Базовая Медицинская Терминология

### 2.1 Основные сущности

В медицинских информационных системах используются специфические термины. Понимание этих терминов критически важно для эффективной работы.

#### Patient (Пациент)

**Определение:** Человек, который получает медицинскую помощь.

```python
# Структура данных пациента (упрощённо)

patient = {
    "id": "patient-12345",
    "mrn": "MRN-2024-123456",  # Medical Record Number
    "name": {
        "family": "Иванов",
        "given": ["Иван", "Петрович"]
    },
    "birth_date": "1980-05-15",
    "gender": "male",
    "address": {
        "line": ["ул. Примерная, д. 10, кв. 5"],
        "city": "Москва",
        "postal_code": "123456",
        "country": "RU"
    },
    "telecom": [
        {"system": "phone", "value": "+7-999-123-4567", "use": "mobile"},
        {"system": "email", "value": "ivan@example.com"}
    ],
    "active": True
}
```

**Ключевые атрибуты:**

- **MRN (Medical Record Number)** — уникальный идентификатор пациента в учреждении

- **Demographics** — имя, дата рождения, пол, адрес, контакты

- **Identifiers** — может быть несколько (MRN, СНИЛС, полис ОМС)

#### Encounter (Визит/Встреча)

**Определение:** Любое взаимодействие пациента с медицинским учреждением.

```python
# Типы encounters

encounter_types = {
    "AMB": "Ambulatory (амбулаторный визит)",
    "EMER": "Emergency (экстренный)",
    "IMP": "Inpatient (госпитализация)",
    "VR": "Virtual (телемедицина)",
    "HH": "Home Health (визит на дому)"
}

# Пример encounter

encounter = {
    "id": "encounter-789",
    "status": "finished",  # planned, arrived, in-progress, finished, cancelled
    "class": "AMB",
    "patient": {"reference": "Patient/patient-12345"},
    "period": {
        "start": "2024-03-15T10:00:00Z",
        "end": "2024-03-15T10:30:00Z"
    },
    "location": "Кабинет 205, Терапевтическое отделение",
    "practitioner": {"reference": "Practitioner/doc-456"},
    "reason": "Плановый осмотр"
}
```

**Важность:** Encounter связывает пациента с конкретным визитом и всеми событиями во время этого визита (диагнозы, назначения, измерения).

#### Diagnosis (Диагноз)

**Определение:** Определение заболевания или состояния пациента.

```python
# Пример диагноза

diagnosis = {
    "id": "condition-456",
    "patient": {"reference": "Patient/patient-12345"},
    "code": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": "E11.9",
                "display": "Type 2 diabetes mellitus without complications"
            }
        ],
        "text": "Сахарный диабет 2 типа без осложнений"
    },
    "clinical_status": "active",  # active, recurrence, relapse, inactive, remission, resolved
    "verification_status": "confirmed",  # provisional, differential, confirmed, refuted
    "onset_date": "2020-01-15",
    "recorded_date": "2024-03-15"
}
```

**Типы диагнозов:**

- **Provisional (предварительный)** — требует подтверждения

- **Confirmed (подтверждённый)** — окончательный диагноз

- **Differential (дифференциальный)** — один из возможных вариантов

#### Procedure (Процедура)

**Определение:** Любое медицинское вмешательство — операция, обследование, манипуляция.

```python
procedure = {
    "id": "procedure-789",
    "status": "completed",
    "code": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "80146002",
            "display": "Appendectomy"
        }]
    },
    "subject": {"reference": "Patient/patient-12345"},
    "performed_date_time": "2024-03-15T14:30:00Z",
    "performer": {"reference": "Practitioner/surgeon-123"},
    "location": "Операционная №3"
}
```

#### Medication (Лекарство)

**Определение:** Лекарственный препарат для лечения или профилактики.

```python
# Назначение лекарства

medication_request = {
    "id": "rx-123",
    "status": "active",
    "medication": {
        "coding": [{
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
            "code": "860975",
            "display": "Metformin 500 MG Oral Tablet"
        }]
    },
    "subject": {"reference": "Patient/patient-12345"},
    "dosage_instruction": {
        "text": "По 1 таблетке 2 раза в день после еды",
        "timing": {
            "repeat": {
                "frequency": 2,
                "period": 1,
                "period_unit": "d"  # day
            }
        },
        "dose": {"value": 500, "unit": "mg"}
    },
    "dispense_request": {
        "quantity": {"value": 60, "unit": "tablets"},
        "expected_supply_duration": {"value": 30, "unit": "d"}
    }
}
```

#### Vital Signs (Жизненные показатели)

**Определение:** Базовые физиологические параметры пациента.

```python
# Основные vital signs

vital_signs = {
    "blood_pressure": {
        "systolic": {"value": 120, "unit": "mmHg"},
        "diastolic": {"value": 80, "unit": "mmHg"},
        "interpretation": "Normal"
    },
    "heart_rate": {
        "value": 72,
        "unit": "bpm",  # beats per minute
        "interpretation": "Normal"
    },
    "temperature": {
        "value": 36.6,
        "unit": "°C",
        "interpretation": "Normal"
    },
    "respiratory_rate": {
        "value": 16,
        "unit": "/min",
        "interpretation": "Normal"
    },
    "oxygen_saturation": {
        "value": 98,
        "unit": "%",
        "interpretation": "Normal"
    }
}

# Референсные диапазоны

reference_ranges = {
    "systolic_bp": {"low": 90, "high": 140, "unit": "mmHg"},
    "diastolic_bp": {"low": 60, "high": 90, "unit": "mmHg"},
    "heart_rate": {"low": 60, "high": 100, "unit": "bpm"},
    "temperature": {"low": 36.1, "high": 37.2, "unit": "°C"},
    "respiratory_rate": {"low": 12, "high": 20, "unit": "/min"},
    "oxygen_saturation": {"low": 95, "high": 100, "unit": "%"}
}
```

#### Allergy (Аллергия)

**Определение:** Непереносимость или аллергическая реакция на вещество.

```python
allergy = {
    "id": "allergy-001",
    "patient": {"reference": "Patient/patient-12345"},
    "clinical_status": "active",
    "verification_status": "confirmed",
    "type": "allergy",  # allergy, intolerance
    "category": ["medication"],  # food, medication, environment, biologic
    "criticality": "high",  # low, high, unable-to-assess
    "code": {
        "coding": [{
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
            "code": "70618",
            "display": "Penicillin"
        }]
    },
    "reaction": [{
        "manifestation": [{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "39579001",
                "display": "Anaphylaxis"
            }]
        }],
        "severity": "severe"  # mild, moderate, severe
    }]
}
```

> **⚠️ Критически важно:** Информация об аллергиях используется системой Clinical Decision Support для предотвращения назначения опасных препаратов. Врач увидит предупреждение, если попытается назначить лекарство, на которое у пациента аллергия.

### 2.2 Типы медицинских данных

```python
# Категоризация медицинских данных

medical_data_types = {
    "Demographics": {
        "description": "Идентификационная информация о пациенте",
        "examples": ["Имя", "Дата рождения", "Пол", "Адрес", "Контакты", "СНИЛС"],
        "sensitivity": "PII (Personally Identifiable Information)"
    },
    
    "Clinical Data": {
        "description": "Медицинская информация",
        "examples": [
            "Диагнозы",
            "Процедуры", 
            "Лекарства",
            "Аллергии",
            "Vital Signs",
            "Анамнез",
            "Семейная история"
        ],
        "sensitivity": "PHI (Protected Health Information)"
    },
    
    "Administrative Data": {
        "description": "Организационная информация",
        "examples": [
            "Страховка",
            "Записи на приём",
            "Направления",
            "Счета"
        ],
        "sensitivity": "Confidential"
    },
    
    "Imaging Data": {
        "description": "Медицинские изображения",
        "examples": ["X-ray", "CT", "MRI", "Ultrasound", "PET"],
        "format": "DICOM",
        "sensitivity": "PHI"
    },
    
    "Laboratory Results": {
        "description": "Результаты анализов",
        "examples": [
            "Общий анализ крови",
            "Биохимия",
            "Микробиология",
            "Генетические тесты"
        ],
        "sensitivity": "PHI"
    }
}
```

---

## 3. Идентификаторы в Healthcare

### 3.1 Почему идентификация критична

В healthcare часто работают с данными из разных источников. Неправильная идентификация пациента может привести к катастрофическим последствиям.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            Сценарий: Ошибка идентификации пациента                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Пациент А: Иванов Иван, 1980 г.р., аллергия на пенициллин                  │
│  Пациент Б: Иванов Иван, 1980 г.р., нет аллергий                            │
│                                                                             │
│  Если системы перепутают пациентов:                                         │
│  • Пациенту А могут назначить пенициллин → анафилактический шок             │
│  • Пациенту Б могут не назначить нужное лекарство                           │
│                                                                             │
│  Решение: Уникальные идентификаторы + правила matching                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Типы идентификаторов

```python
# Идентификаторы пациента

patient_identifiers = {
    "MRN": {
        "full_name": "Medical Record Number",
        "description": "Уникальный ID внутри одного учреждения",
        "format": "Определяется учреждением",
        "example": "MRN-2024-123456",
        "scope": "Hospital/Clinic"
    },
    
    "SSN_SNILS": {
        "full_name": "СНИЛС (РФ) / SSN (США)",
        "description": "Государственный идентификатор",
        "format": "11 цифр (СНИЛС) / 9 цифр (SSN)",
        "example": "123-456-789 00",
        "scope": "National"
    },
    
    "Insurance_ID": {
        "full_name": "Номер полиса ОМС/ДМС",
        "description": "Идентификатор страховки",
        "format": "16 цифр (ОМС)",
        "example": "1234567890123456",
        "scope": "Insurance company"
    },
    
    "Enterprise_ID": {
        "full_name": "Enterprise Patient ID",
        "description": "ID в системе нескольких учреждений",
        "format": "UUID или custom",
        "example": "550e8400-e29b-41d4-a716-446655440000",
        "scope": "Healthcare network"
    }
}

# Пример пациента с несколькими идентификаторами

patient_with_ids = {
    "id": "patient-abc123",
    "identifier": [
        {
            "use": "official",
            "type": {"coding": [{"code": "MR", "display": "Medical Record Number"}]},
            "system": "http://hospital.org/patients",
            "value": "MRN-2024-123456"
        },
        {
            "use": "secondary",
            "type": {"coding": [{"code": "SS", "display": "SNILS"}]},
            "system": "http://gov.ru/snils",
            "value": "123-456-789 00"
        },
        {
            "use": "secondary",
            "type": {"coding": [{"code": "INS", "display": "Insurance"}]},
            "system": "http://foms.ru/oms",
            "value": "1234567890123456"
        }
    ]
}
```

### 3.3 Patient Matching

```python
def match_patients(patient1: dict, patient2: dict) -> float:
    """
    Вычисляет вероятность того, что два пациента — один и тот же человек.
    Returns: score от 0.0 до 1.0
    """
    score = 0.0
    weights = {
        "exact_mrn": 1.0,        # Точное совпадение MRN
        "exact_ssn": 0.95,       # Точное совпадение СНИЛС
        "name_match": 0.3,       # Совпадение имени
        "dob_match": 0.25,       # Совпадение даты рождения
        "gender_match": 0.1,     # Совпадение пола
        "address_match": 0.1,    # Совпадение адреса
    }
    
    # Точное совпадение MRN — 100% match
    if get_mrn(patient1) and get_mrn(patient1) == get_mrn(patient2):
        return 1.0
    
    # Точное совпадение СНИЛС — почти 100%
    if get_ssn(patient1) and get_ssn(patient1) == get_ssn(patient2):
        return 0.95
    
    # Probabilistic matching
    if names_match(patient1, patient2):
        score += weights["name_match"]
    if dob_match(patient1, patient2):
        score += weights["dob_match"]
    if gender_match(patient1, patient2):
        score += weights["gender_match"]
    if address_match(patient1, patient2):
        score += weights["address_match"]
    
    return min(score, 1.0)

# Thresholds для принятия решений

MATCH_THRESHOLDS = {
    "automatic_match": 0.9,    # Автоматическое связывание
    "review_required": 0.7,    # Требуется ручная проверка
    "no_match": 0.5            # Разные пациенты
}
```

---

## 4. Обзор стандартов Healthcare IT

### 4.1 Зачем нужны стандарты

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  Проблема без стандартов                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Больница с 10 системами без стандартов:                                    │
│  • EHR ↔ Lab: custom интеграция #1                                          │
│  • EHR ↔ Radiology: custom интеграция #2                                    │
│  • EHR ↔ Pharmacy: custom интеграция #3                                     │
│  • ... итого 45 уникальных интеграций (n*(n-1)/2)                           │
│                                                                             │
│  Больница с 10 системами со стандартами:                                    │
│  • Все системы говорят на HL7/FHIR                                          │
│  • Integration Engine переводит сообщения                                   │
│  • 10 стандартных интерфейсов вместо 45 custom                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Карта стандартов

```python
healthcare_standards = {
    "Messaging Standards": {
        "HL7 v2": {
            "year": 1988,
            "format": "Pipe-delimited text",
            "status": "Legacy, но широко используется",
            "use_case": "ADT, Lab results, Orders"
        },
        "HL7 FHIR": {
            "year": 2014,
            "format": "REST API + JSON/XML",
            "status": "Modern standard",
            "use_case": "Все типы данных, mobile apps, API"
        }
    },
    
    "Terminology Standards": {
        "ICD-10": {
            "description": "Классификация болезней",
            "codes": "~70,000",
            "example": "E11.9 - Diabetes Type 2"
        },
        "SNOMED CT": {
            "description": "Клиническая терминология",
            "concepts": "~350,000",
            "example": "44054006 - Type 2 diabetes mellitus"
        },
        "LOINC": {
            "description": "Лабораторные наблюдения",
            "codes": "~94,000",
            "example": "718-7 - Hemoglobin"
        }
    },
    
    "Imaging Standards": {
        "DICOM": {
            "description": "Медицинские изображения",
            "use_case": "X-ray, CT, MRI, Ultrasound"
        }
    }
}
```

### 4.3 Когда использовать какой стандарт

| Задача | Стандарт | Почему |
|--------|----------|--------|
| Интеграция с legacy системой | HL7 v2 | Большинство старых систем используют v2 |
| Новая разработка / API | FHIR | Современный, REST, удобный для разработчиков |
| Кодирование диагнозов | ICD-10 | Требуется для billing, статистики |
| Клиническая документация | SNOMED CT | Более детальная терминология |
| Лабораторные результаты | LOINC | Стандарт для lab observations |
| Медицинские изображения | DICOM | Единственный стандарт для imaging |

---

## 5. Workflow в Healthcare

### 5.1 Типичный клинический workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Амбулаторный визит: Workflow                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. РЕГИСТРАЦИЯ                                                             │
│     └─► Patient check-in → ADT^A04 (Registration)                           │
│         • Проверка демографических данных                                   │
│         • Подтверждение страховки                                           │
│         • Создание Encounter                                                │
│                                                                             │
│  2. TRIAGE (если нужно)                                                     │
│     └─► Измерение vital signs → Observation resources                       │
│         • BP, HR, Temperature, SpO2                                         │
│                                                                             │
│  3. ОСМОТР ВРАЧА                                                            │
│     └─► Clinical assessment                                                 │
│         • Сбор анамнеза                                                     │
│         • Физикальный осмотр                                                │
│         • Работа с предыдущими данными пациента                             │
│                                                                             │
│  4. НАЗНАЧЕНИЯ                                                              │
│     └─► Orders                                                              │
│         • Лабораторные анализы → ORM^O01                                    │
│         • Направления на исследования                                       │
│         • Рецепты → MedicationRequest                                       │
│                                                                             │
│  5. ДИАГНОЗ                                                                 │
│     └─► Condition resource                                                  │
│         • Код ICD-10                                                        │
│         • Клинический статус                                                │
│                                                                             │
│  6. ЗАВЕРШЕНИЕ                                                              │
│     └─► ADT^A03 (Discharge)                                                 │
│         • Закрытие Encounter                                                │
│         • Выписной эпикриз                                                  │
│         • Следующий визит                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Потоки данных

```python
# Пример: результаты лабораторных анализов

lab_workflow = """
1. Врач назначает анализ (EHR → LIS)
   └─► ORM^O01 (Order Message)
   
2. Пациент сдаёт кровь
   └─► Образец регистрируется в LIS
   
3. Лаборатория выполняет анализ
   └─► Результаты вводятся в LIS
   
4. Результаты отправляются в EHR (LIS → EHR)
   └─► ORU^R01 (Observation Result)
   
5. Врач получает уведомление
   └─► Результаты отображаются в карте пациента
   
6. Clinical Decision Support
   └─► Если результат критический → Alert врачу
"""
```

---

## 6. Практические примеры

### 6.1 Чтение данных пациента

```python
def display_patient_summary(patient: dict) -> str:
    """Форматирует сводку по пациенту."""
    
    # Получаем имя
    name = patient.get("name", [{}])[0]
    full_name = f"{' '.join(name.get('given', []))} {name.get('family', '')}"
    
    # Дата рождения и возраст
    dob = patient.get("birth_date", "Unknown")
    age = calculate_age(dob) if dob != "Unknown" else "Unknown"
    
    # Пол
    gender_map = {"male": "М", "female": "Ж", "other": "Другой"}
    gender = gender_map.get(patient.get("gender", ""), "Не указан")
    
    # MRN
    mrn = None
    for identifier in patient.get("identifier", []):
        if identifier.get("type", {}).get("coding", [{}])[0].get("code") == "MR":
            mrn = identifier.get("value")
            break
    
    summary = f"""
╔══════════════════════════════════════════════════════╗
║              КАРТОЧКА ПАЦИЕНТА                       ║
╠══════════════════════════════════════════════════════╣
║  ФИО:          {full_name:<35} ║
║  Дата рождения: {dob:<34} ║
║  Возраст:       {age} лет{' ' * (30 - len(str(age)))} ║
║  Пол:           {gender:<34} ║
║  MRN:           {mrn or 'Не присвоен':<34} ║
╚══════════════════════════════════════════════════════╝
    """
    return summary

# Пример использования

patient_data = {
    "name": [{"family": "Иванов", "given": ["Иван", "Петрович"]}],
    "birth_date": "1980-05-15",
    "gender": "male",
    "identifier": [
        {"type": {"coding": [{"code": "MR"}]}, "value": "MRN-2024-123456"}
    ]
}

print(display_patient_summary(patient_data))
```

### 6.2 Проверка аллергий перед назначением

```python
def check_medication_safety(patient_id: str, medication_code: str) -> dict:
    """
    Проверяет безопасность назначения лекарства.
    Возвращает информацию о потенциальных проблемах.
    """
    
    # Получаем аллергии пациента (из базы данных)
    patient_allergies = get_patient_allergies(patient_id)
    
    # Проверяем cross-reactivity
    warnings = []
    
    for allergy in patient_allergies:
        allergy_code = allergy.get("code", {}).get("coding", [{}])[0].get("code")
        
        # Проверка прямого совпадения
        if medication_code == allergy_code:
            warnings.append({
                "severity": "high",
                "type": "allergy",
                "message": f"ЗАПРЕЩЕНО: У пациента аллергия на {allergy_code}",
                "action": "block"
            })
            continue
        
        # Проверка cross-reactivity (например, пенициллин ↔ амоксициллин)
        if is_cross_reactive(medication_code, allergy_code):
            warnings.append({
                "severity": "moderate",
                "type": "cross-reactivity",
                "message": f"ВНИМАНИЕ: Возможна перекрёстная реакция с {allergy_code}",
                "action": "warn"
            })
    
    return {
        "safe": len([w for w in warnings if w["action"] == "block"]) == 0,
        "warnings": warnings
    }

# Пример использования

result = check_medication_safety("patient-12345", "amoxicillin")
if not result["safe"]:
    print("⛔ Назначение заблокировано!")
    for warning in result["warnings"]:
        print(f"  - {warning['message']}")
```

---

## 💡 Key Takeaways

- **Patient, Encounter, Diagnosis** — основные сущности в любой медицинской системе

- **Идентификация критична** — MRN, СНИЛС, страховые номера должны быть точными

- **Стандарты обязательны** — HL7, FHIR, ICD-10, SNOMED CT обеспечивают interoperability

- **Аллергии** — информация об аллергиях может спасти жизнь

- **Workflow** — понимание клинических процессов важно для правильной разработки

---

## 🚀 Next Steps

**Следующие модули:**

- [02_HL7](../02_HL7/) — Детальное изучение HL7 v2 стандарта
- [03_FHIR](../03_FHIR/) — Современный FHIR стандарт

**Практика:**

1. Создайте структуру данных Patient с несколькими идентификаторами
2. Напишите функцию проверки аллергий
3. Изучите примеры кодов ICD-10 для распространённых заболеваний

---

## 📚 Additional Resources

**Стандарты:**

- [HL7 International](https://www.hl7.org/)
- [FHIR Specification](https://www.hl7.org/fhir/)

**Терминологии:**

- [ICD-10 Browser](https://icd.who.int/browse10/)
- [SNOMED CT Browser](https://browser.ihtsdotools.org/)
- [LOINC](https://loinc.org/)

---





