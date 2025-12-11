# Медицинские Классификаторы и Терминологии
## ICD-10, SNOMED CT, LOINC

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовую медицинскую терминологию
- Понимать структуру FHIR ресурсов
- Иметь представление о кодировании данных

**Recommended prior modules:**

- [01_Terminology](../01_Terminology/) — базовая терминология
- [03_FHIR](../03_FHIR/) — использование кодов в FHIR

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать структуру и применение ICD-10 кодов
- Работать с SNOMED CT терминологией
- Использовать LOINC коды для лабораторных данных
- Выбирать правильную систему кодирования для разных задач

---

## 1. Зачем нужны стандартные коды

### 1.1 Проблема без стандартизации

```

┌─────────────────────────────────────────────────────────────────────────────┐
│                  Без стандартных кодов                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Больница A: "Сахарный диабет II типа"                                      │
│  Больница B: "Diabetes mellitus type 2"                                     │
│  Больница C: "СДII без осложнений"                                          │
│  Лаборатория: "DM2"                                                         │
│                                                                              │
│  → Невозможно агрегировать данные                                           │
│  → Невозможно автоматизировать billing                                      │
│  → Невозможно проводить исследования                                        │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                  Со стандартными кодами                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Все системы: ICD-10 код E11.9                                              │
│                                                                              │
│  → Единое понимание                                                         │
│  → Автоматический billing                                                   │
│  → Статистика и исследования                                                │
│  → Interoperability                                                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

```

### 1.2 Основные системы кодирования

```python

coding_systems = {
    "ICD-10": {
        "full_name": "International Classification of Diseases, 10th Revision",
        "purpose": "Классификация заболеваний и причин смерти",
        "codes": "~70,000 (ICD-10-CM)",
        "use_cases": ["Billing", "Статистика", "Страхование"],
        "uri": "http://hl7.org/fhir/sid/icd-10"
    },
    "SNOMED CT": {
        "full_name": "Systematized Nomenclature of Medicine - Clinical Terms",
        "purpose": "Детальная клиническая терминология",
        "concepts": "~350,000",
        "use_cases": ["Клиническая документация", "Decision support", "Исследования"],
        "uri": "http://snomed.info/sct"
    },
    "LOINC": {
        "full_name": "Logical Observation Identifiers Names and Codes",
        "purpose": "Идентификация лабораторных и клинических наблюдений",
        "codes": "~94,000",
        "use_cases": ["Лабораторные анализы", "Vital signs", "Документы"],
        "uri": "http://loinc.org"
    }
}

```

---

## 2. ICD-10 — Международная Классификация Болезней

### 2.1 Структура кода

```

E 11 . 65
│ ││   ││
│ ││   │└─ Подкатегория (гипергликемия)
│ ││   └── Этиология/локализация
│ │└────── Категория (диабет 2 типа)
│ └─────── Глава (Эндокринные заболевания)
└───────── Буква главы (E = Endocrine)

```

### 2.2 Главы ICD-10

```python

icd10_chapters = {
    "A00-B99": "Инфекционные и паразитарные болезни",
    "C00-D49": "Новообразования",
    "D50-D89": "Болезни крови и кроветворных органов",
    "E00-E89": "Болезни эндокринной системы",
    "F01-F99": "Психические расстройства",
    "G00-G99": "Болезни нервной системы",
    "H00-H59": "Болезни глаза",
    "H60-H95": "Болезни уха",
    "I00-I99": "Болезни системы кровообращения",
    "J00-J99": "Болезни органов дыхания",
    "K00-K95": "Болезни органов пищеварения",
    "L00-L99": "Болезни кожи",
    "M00-M99": "Болезни костно-мышечной системы",
    "N00-N99": "Болезни мочеполовой системы",
    "O00-O9A": "Беременность, роды",
    "P00-P96": "Перинатальный период",
    "Q00-Q99": "Врождённые аномалии",
    "R00-R99": "Симптомы и признаки",
    "S00-T88": "Травмы и отравления",
    "V00-Y99": "Внешние причины",
    "Z00-Z99": "Факторы, влияющие на здоровье"
}

```

### 2.3 Примеры кодов

```python
# Примеры ICD-10 кодов с разбором
icd10_examples = {
    # Эндокринные заболевания (E00-E89)
    "E11.9": {
        "description": "Type 2 diabetes mellitus without complications",
        "ru": "Сахарный диабет 2 типа без осложнений",
        "chapter": "E - Endocrine",
        "category": "11 - Type 2 DM"
    },
    "E11.65": {
        "description": "Type 2 diabetes mellitus with hyperglycemia",
        "ru": "Сахарный диабет 2 типа с гипергликемией"
    },
    "E11.21": {
        "description": "Type 2 diabetes mellitus with diabetic nephropathy",
        "ru": "Сахарный диабет 2 типа с поражением почек"
    },
    
    # Сердечно-сосудистые (I00-I99)
    "I10": {
        "description": "Essential (primary) hypertension",
        "ru": "Эссенциальная (первичная) гипертензия"
    },
    "I21.9": {
        "description": "Acute myocardial infarction, unspecified",
        "ru": "Острый инфаркт миокарда неуточнённый"
    },
    "I50.9": {
        "description": "Heart failure, unspecified",
        "ru": "Сердечная недостаточность неуточнённая"
    },
    
    # Травмы (S00-T88)
    "S72.001A": {
        "description": "Fracture of neck of right femur, initial encounter",
        "ru": "Перелом шейки правого бедра, первичное обращение",
        "7th_char": "A = Initial encounter"
    }
}

# 7-й символ для травм
seventh_character = {
    "A": "Initial encounter (первичное обращение)",
    "D": "Subsequent encounter (последующее наблюдение)",
    "S": "Sequela (последствия, отдалённые эффекты)"
}

```

### 2.4 Работа с ICD-10 в Python

```python

def parse_icd10_code(code: str) -> dict:
    """Разбирает структуру ICD-10 кода."""
    
    clean_code = code.replace(".", "")
    
    result = {
        "original": code,
        "chapter_letter": clean_code[0],
        "category": clean_code[0:3] if len(clean_code) >= 3 else None,
        "subcategory": clean_code[3:] if len(clean_code) > 3 else None
    }
    
    # Определение главы
    chapter_map = {
        "A": "Infectious diseases", "B": "Infectious diseases",
        "C": "Neoplasms", "D": "Neoplasms/Blood",
        "E": "Endocrine/Metabolic",
        "F": "Mental disorders",
        "G": "Nervous system",
        "H": "Eye/Ear",
        "I": "Circulatory system",
        "J": "Respiratory system",
        "K": "Digestive system",
        "L": "Skin",
        "M": "Musculoskeletal",
        "N": "Genitourinary",
        "O": "Pregnancy",
        "P": "Perinatal",
        "Q": "Congenital",
        "R": "Symptoms/Signs",
        "S": "Injuries", "T": "Injuries/Poisoning",
        "V": "External causes", "W": "External causes",
        "X": "External causes", "Y": "External causes",
        "Z": "Health status factors"
    }
    
    result["chapter"] = chapter_map.get(clean_code[0], "Unknown")
    
    return result

# Пример
code_info = parse_icd10_code("E11.65")
print(f"Code: {code_info['original']}")
print(f"Chapter: {code_info['chapter']}")
print(f"Category: {code_info['category']}")
print(f"Subcategory: {code_info['subcategory']}")

```

---

## 3. SNOMED CT — Клиническая Терминология

### 3.1 Особенности SNOMED CT

```python

snomed_features = {
    "ontology": "Не просто список кодов, а онтология с отношениями",
    "concepts": "~350,000 активных концепций",
    "relationships": "~1,500,000 отношений",
    "hierarchies": "19 top-level иерархий",
    "precision": "Более детальная чем ICD-10"
}

```

### 3.2 Иерархии SNOMED CT

```python

snomed_hierarchies = {
    "Clinical finding": {
        "count": "~130,000",
        "examples": ["Diabetes mellitus", "Hypertension", "Pain"]
    },
    "Procedure": {
        "count": "~65,000",
        "examples": ["Appendectomy", "Blood pressure measurement"]
    },
    "Body structure": {
        "count": "~35,000",
        "examples": ["Heart structure", "Lung structure"]
    },
    "Organism": {
        "count": "~35,000",
        "examples": ["Bacteria", "Viruses"]
    },
    "Substance": {
        "count": "~30,000",
        "examples": ["Drugs", "Chemicals"]
    },
    "Pharmaceutical product": {
        "count": "~20,000",
        "examples": ["Metformin", "Aspirin"]
    }
}

```

### 3.3 Примеры SNOMED CT кодов

```python

snomed_examples = {
    # Clinical Findings
    "73211009": {
        "term": "Diabetes mellitus",
        "fsn": "Diabetes mellitus (disorder)"
    },
    "44054006": {
        "term": "Type 2 diabetes mellitus",
        "fsn": "Type 2 diabetes mellitus (disorder)",
        "parent": "73211009"  # is-a Diabetes mellitus
    },
    "38341003": {
        "term": "Hypertensive disorder",
        "fsn": "Hypertensive disorder, systemic arterial (disorder)"
    },
    
    # Body Structures
    "80891009": {
        "term": "Heart",
        "fsn": "Heart structure (body structure)"
    },
    "39607008": {
        "term": "Lung",
        "fsn": "Lung structure (body structure)"
    },
    
    # Procedures
    "80146002": {
        "term": "Appendectomy",
        "fsn": "Excision of appendix (procedure)"
    }
}

```

### 3.4 Отношения в SNOMED CT

```

                    Disease (64572001)
                          │
                          │ is-a
                          ▼
               Endocrine disease (362969004)
                          │
                          │ is-a
                          ▼
               Diabetes mellitus (73211009)
                          │
        ┌─────────────────┼─────────────────┐
        │ is-a            │ is-a            │ is-a
        ▼                 ▼                 ▼
   Type 1 DM         Type 2 DM        Gestational DM
   (46635009)        (44054006)        (11687002)

```

### 3.5 SNOMED CT в FHIR

```json

{
  "resourceType": "Condition",
  "code": {
    "coding": [
      {
        "system": "http://snomed.info/sct",
        "code": "44054006",
        "display": "Type 2 diabetes mellitus"
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10",
        "code": "E11.9",
        "display": "Type 2 diabetes mellitus without complications"
      }
    ],
    "text": "Сахарный диабет 2 типа"
  }
}

```

---

## 4. LOINC — Лабораторные Коды

### 4.1 Структура LOINC

```

LOINC состоит из 6 частей:

Component - Property - Timing - System - Scale - Method

718-7: Hemoglobin - MCnc - Pt - Bld - Qn
       └─────────   └───   └─   └──   └─
       Что         Свойство Когда Где  Тип

Component: Hemoglobin (что измеряем)
Property:  MCnc (mass concentration - концентрация массы)
Timing:    Pt (point in time - момент времени)
System:    Bld (blood - кровь)
Scale:     Qn (quantitative - количественный)

```

### 4.2 Примеры LOINC кодов

```python

loinc_examples = {
    # Лабораторные анализы
    "718-7": {
        "name": "Hemoglobin",
        "long_name": "Hemoglobin [Mass/volume] in Blood",
        "unit": "g/dL или g/L",
        "system": "Blood"
    },
    "2345-7": {
        "name": "Glucose",
        "long_name": "Glucose [Mass/volume] in Serum or Plasma",
        "unit": "mg/dL или mmol/L",
        "system": "Serum/Plasma"
    },
    "2160-0": {
        "name": "Creatinine",
        "long_name": "Creatinine [Mass/volume] in Serum or Plasma",
        "unit": "mg/dL",
        "system": "Serum/Plasma"
    },
    "2951-2": {
        "name": "Sodium",
        "long_name": "Sodium [Moles/volume] in Serum or Plasma",
        "unit": "mmol/L",
        "system": "Serum/Plasma"
    },
    
    # Vital Signs
    "8480-6": {
        "name": "Systolic BP",
        "long_name": "Systolic blood pressure",
        "unit": "mmHg"
    },
    "8462-4": {
        "name": "Diastolic BP",
        "long_name": "Diastolic blood pressure",
        "unit": "mmHg"
    },
    "8867-4": {
        "name": "Heart rate",
        "long_name": "Heart rate",
        "unit": "/min или bpm"
    },
    "8310-5": {
        "name": "Body temperature",
        "long_name": "Body temperature",
        "unit": "°C или °F"
    },
    "2708-6": {
        "name": "Oxygen saturation",
        "long_name": "Oxygen saturation in Arterial blood",
        "unit": "%"
    }
}

```

### 4.3 LOINC в FHIR Observation

```python

from fhir.resources.observation import Observation

def create_lab_observation(patient_id: str, loinc_code: str, 
                          display: str, value: float, unit: str) -> dict:
    """Создаёт Observation с LOINC кодом."""
    
    return {
        "resourceType": "Observation",
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "Laboratory"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": loinc_code,
                "display": display
            }]
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        },
        "valueQuantity": {
            "value": value,
            "unit": unit,
            "system": "http://unitsofmeasure.org"
        }
    }

# Примеры
hemoglobin = create_lab_observation(
    patient_id="patient-123",
    loinc_code="718-7",
    display="Hemoglobin [Mass/volume] in Blood",
    value=14.5,
    unit="g/dL"
)

glucose = create_lab_observation(
    patient_id="patient-123",
    loinc_code="2345-7",
    display="Glucose [Mass/volume] in Serum or Plasma",
    value=95,
    unit="mg/dL"
)

```

---

## 5. Выбор системы кодирования

### 5.1 Когда использовать какую систему

| Задача | Система | Почему |
|--------|---------|--------|
| Billing/страхование | ICD-10 | Обязательно для оплаты |
| Статистика заболеваний | ICD-10 | Стандарт для отчётности |
| Детальная документация | SNOMED CT | Более точная терминология |
| Лабораторные результаты | LOINC | Стандарт для lab |
| Vital Signs | LOINC | Специфичные коды |
| Процедуры | SNOMED CT или CPT | Зависит от контекста |

### 5.2 Mapping между системами

```python
# SNOMED CT ↔ ICD-10 mapping
snomed_to_icd10 = {
    "44054006": "E11.9",   # Type 2 DM
    "38341003": "I10",     # Hypertension
    "22298006": "I21.9",   # MI
    "233604007": "J18.9",  # Pneumonia
    "13645005": "J44.9"    # COPD
}

def get_icd10_from_snomed(snomed_code: str) -> str | None:
    """Получает ICD-10 код для SNOMED CT концепции."""
    return snomed_to_icd10.get(snomed_code)

# Использование
icd10_code = get_icd10_from_snomed("44054006")
print(f"SNOMED 44054006 → ICD-10 {icd10_code}")  # E11.9

```

---

## 6. Практические примеры

### 6.1 Кодирование диагноза

```python

def code_diagnosis(diagnosis_text: str) -> dict:
    """
    Пример кодирования диагноза несколькими системами.
    В реальности используется NLP или ручной ввод.
    """
    
    # Простая демонстрация
    diagnosis_codes = {
        "диабет 2 типа": {
            "icd10": "E11.9",
            "snomed": "44054006",
            "display_icd10": "Type 2 diabetes mellitus without complications",
            "display_snomed": "Type 2 diabetes mellitus"
        },
        "гипертония": {
            "icd10": "I10",
            "snomed": "38341003",
            "display_icd10": "Essential (primary) hypertension",
            "display_snomed": "Hypertensive disorder"
        }
    }
    
    normalized = diagnosis_text.lower().strip()
    
    if normalized in diagnosis_codes:
        codes = diagnosis_codes[normalized]
        return {
            "text": diagnosis_text,
            "coding": [
                {
                    "system": "http://hl7.org/fhir/sid/icd-10",
                    "code": codes["icd10"],
                    "display": codes["display_icd10"]
                },
                {
                    "system": "http://snomed.info/sct",
                    "code": codes["snomed"],
                    "display": codes["display_snomed"]
                }
            ]
        }
    
    return {"text": diagnosis_text, "coding": []}

# Пример
result = code_diagnosis("Диабет 2 типа")
print(f"Текст: {result['text']}")
for coding in result['coding']:
    print(f"  {coding['system'].split('/')[-1]}: {coding['code']} - {coding['display']}")

```

### 6.2 Поиск LOINC для лабораторного теста

```python
# База LOINC кодов (упрощённая)
loinc_database = {
    "hemoglobin": ["718-7", "718-7", "30313-1"],
    "glucose": ["2345-7", "2339-0", "14749-6"],
    "creatinine": ["2160-0", "38483-4"],
    "sodium": ["2951-2", "2947-0"],
    "potassium": ["2823-3", "6298-4"],
    "wbc": ["6690-2", "26464-8"],
    "rbc": ["789-8", "26453-1"],
    "platelets": ["777-3", "26515-7"]
}

def find_loinc(test_name: str) -> list:
    """Находит LOINC коды для лабораторного теста."""
    
    normalized = test_name.lower().strip()
    
    for key, codes in loinc_database.items():
        if key in normalized or normalized in key:
            return codes
    
    return []

# Пример
codes = find_loinc("hemoglobin")
print(f"LOINC коды для hemoglobin: {codes}")

```

---

## 💡 Key Takeaways

- **ICD-10** — классификация для billing, статистики (~70,000 кодов)

- **SNOMED CT** — детальная клиническая терминология (~350,000 концепций)

- **LOINC** — стандарт для лабораторных наблюдений (~94,000 кодов)

- **Mapping** — возможно преобразование между системами

- **FHIR CodeableConcept** — поддерживает несколько кодировок одновременно

- **Выбор системы** зависит от use case (billing, документация, лаборатория)

---

## 🚀 Next Steps

**Следующие модули:**

- [05_EHR_Systems](../05_EHR_Systems/) — Системы электронных медицинских записей
- [06_Security_Privacy](../06_Security_Privacy/) — Безопасность и HIPAA

**Практика:**

1. Найдите ICD-10 код для распространённых заболеваний
2. Изучите иерархию SNOMED CT для конкретного диагноза
3. Используйте LOINC коды в FHIR Observation

---

## 📚 Additional Resources

- [ICD-10 Browser](https://icd.who.int/browse10/)
- [SNOMED CT Browser](https://browser.ihtsdotools.org/)
- [LOINC Search](https://loinc.org/search/)
- [UMLS (Unified Medical Language System)](https://www.nlm.nih.gov/research/umls/)

---





