# FHIR — Fast Healthcare Interoperability Resources
## Современный стандарт обмена медицинскими данными

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Знать базовую медицинскую терминологию
- Понимать REST API и JSON
- Иметь опыт работы с HTTP-клиентами

**Recommended prior modules:**

- [01_Terminology](../01_Terminology/) — базовая терминология
- [02_HL7](../02_HL7/) — HL7 v2 (для понимания эволюции стандартов)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать архитектуру FHIR и структуру ресурсов
- Работать с FHIR API (CRUD операции, поиск)
- Использовать Python библиотеки для работы с FHIR
- Создавать и валидировать FHIR ресурсы

---

## 1. Введение в FHIR

### 1.1 Что такое FHIR?

**FHIR (Fast Healthcare Interoperability Resources)** — современный стандарт HL7 для обмена медицинскими данными через REST API.

```

┌─────────────────────────────────────────────────────────────────────────────┐
│                         Почему FHIR?                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  HL7 v2 проблемы:              FHIR решения:                                │
│  ─────────────────             ───────────────                              │
│  • Слишком гибкий              • Строгая структура ресурсов                 │
│  • Несовместимость             • Стандартный REST API                       │
│  • Сложный парсинг             • JSON/XML — привычные форматы               │
│  • Legacy формат               • Современный подход                         │
│                                                                             │
│  HL7 v3 проблемы:              FHIR решения:                                │
│  ─────────────────             ───────────────                              │
│  • Слишком сложный             • Простые ресурсы                            │
│  • Дорогая имплементация       • Легко начать                               │
│  • Всё или ничего              • Модульный подход                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

```

### 1.2 Ключевые особенности

```python

fhir_features = {
    "REST API": {
        "description": "Стандартные HTTP методы",
        "operations": ["GET", "POST", "PUT", "PATCH", "DELETE"],
        "example": "GET /Patient/123"
    },
    "JSON/XML": {
        "description": "Выбор формата данных",
        "json": "application/fhir+json",
        "xml": "application/fhir+xml"
    },
    "Resources": {
        "description": "Модульные строительные блоки",
        "count": "~150 типов ресурсов",
        "examples": ["Patient", "Observation", "Medication"]
    },
    "Extensions": {
        "description": "Расширяемость",
        "use_case": "Добавление custom полей"
    }
}

```

### 1.3 Версии FHIR

| Версия | Год | Статус |
|--------|-----|--------|
| DSTU1 | 2014 | Устаревшая |
| DSTU2 | 2015 | Legacy |
| STU3 | 2017 | Используется |
| **R4** | 2019 | **Рекомендуется для production** |
| R5 | 2023 | Новейшая |

---

## 2. FHIR Resources

### 2.1 Структура ресурса

```json

{
  "resourceType": "Patient",
  "id": "patient-123",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-03-15T10:00:00Z"
  },
  "identifier": [
    {
      "system": "http://hospital.org/patients",
      "value": "MRN-123456"
    }
  ],
  "name": [
    {
      "use": "official",
      "family": "Иванов",
      "given": ["Иван", "Петрович"]
    }
  ],
  "gender": "male",
  "birthDate": "1980-05-15"
}

```

### 2.2 Основные ресурсы

```python

fhir_resources = {
    "Administrative": {
        "Patient": "Демографические данные пациента",
        "Practitioner": "Медицинский работник",
        "Organization": "Медицинская организация",
        "Location": "Физическое место (палата, кабинет)"
    },
    "Clinical": {
        "Encounter": "Визит/госпитализация",
        "Condition": "Диагноз/состояние",
        "Observation": "Измерение (vital signs, лаб. результаты)",
        "Procedure": "Процедура/операция",
        "AllergyIntolerance": "Аллергия"
    },
    "Medications": {
        "Medication": "Описание лекарства",
        "MedicationRequest": "Назначение/рецепт",
        "MedicationAdministration": "Введение лекарства"
    },
    "Diagnostics": {
        "DiagnosticReport": "Диагностический отчёт",
        "ImagingStudy": "Исследование изображений"
    }
}

```

### 2.3 Пример Patient Resource

```json

{
  "resourceType": "Patient",
  "id": "patient-123",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-03-15T10:00:00Z",
    "profile": ["http://hl7.org/fhir/StructureDefinition/Patient"]
  },
  "identifier": [
    {
      "use": "official",
      "type": {
        "coding": [{
          "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
          "code": "MR",
          "display": "Medical Record Number"
        }]
      },
      "system": "http://hospital.org/patients",
      "value": "MRN-123456"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "official",
      "family": "Иванов",
      "given": ["Иван", "Петрович"]
    },
    {
      "use": "nickname",
      "given": ["Ваня"]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "+7-999-123-4567",
      "use": "mobile"
    },
    {
      "system": "email",
      "value": "ivan@example.com"
    }
  ],
  "gender": "male",
  "birthDate": "1980-05-15",
  "address": [
    {
      "use": "home",
      "line": ["ул. Примерная, д. 10, кв. 5"],
      "city": "Москва",
      "postalCode": "123456",
      "country": "RU"
    }
  ],
  "generalPractitioner": [
    {
      "reference": "Practitioner/doc-456",
      "display": "Др. Смирнова Анна"
    }
  ]
}

```

### 2.4 Observation Resource

```json

{
  "resourceType": "Observation",
  "id": "bp-001",
  "status": "final",
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
      "code": "vital-signs",
      "display": "Vital Signs"
    }]
  }],
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "85354-9",
      "display": "Blood pressure panel"
    }]
  },
  "subject": {
    "reference": "Patient/patient-123"
  },
  "effectiveDateTime": "2024-03-15T10:30:00Z",
  "component": [
    {
      "code": {
        "coding": [{
          "system": "http://loinc.org",
          "code": "8480-6",
          "display": "Systolic blood pressure"
        }]
      },
      "valueQuantity": {
        "value": 120,
        "unit": "mmHg",
        "system": "http://unitsofmeasure.org",
        "code": "mm[Hg]"
      }
    },
    {
      "code": {
        "coding": [{
          "system": "http://loinc.org",
          "code": "8462-4",
          "display": "Diastolic blood pressure"
        }]
      },
      "valueQuantity": {
        "value": 80,
        "unit": "mmHg",
        "system": "http://unitsofmeasure.org",
        "code": "mm[Hg]"
      }
    }
  ]
}

```

---

## 3. FHIR API Operations

### 3.1 CRUD операции

```python
# FHIR REST API операции
fhir_operations = {
    "read": {
        "method": "GET",
        "url": "/Patient/123",
        "description": "Получить ресурс по ID"
    },
    "create": {
        "method": "POST",
        "url": "/Patient",
        "description": "Создать новый ресурс (ID назначит сервер)"
    },
    "update": {
        "method": "PUT",
        "url": "/Patient/123",
        "description": "Полное обновление ресурса"
    },
    "patch": {
        "method": "PATCH",
        "url": "/Patient/123",
        "description": "Частичное обновление"
    },
    "delete": {
        "method": "DELETE",
        "url": "/Patient/123",
        "description": "Удалить ресурс"
    },
    "search": {
        "method": "GET",
        "url": "/Patient?name=Иванов",
        "description": "Поиск ресурсов"
    }
}

```

### 3.2 Параметры поиска

```bash
# Поиск по имени
GET /Patient?name=Иванов
GET /Patient?given=Иван&family=Иванов

# Поиск по дате рождения
GET /Patient?birthdate=1980-05-15
GET /Patient?birthdate=ge1980-01-01    # greater or equal
GET /Patient?birthdate=lt1990-01-01    # less than

# Поиск по идентификатору
GET /Patient?identifier=MRN-123456
GET /Patient?identifier=http://hospital.org|MRN-123456

# Комбинированный поиск
GET /Patient?name=Иванов&gender=male&birthdate=ge1980-01-01

# Сортировка
GET /Patient?name=Иванов&_sort=birthdate
GET /Patient?name=Иванов&_sort=-birthdate  # descending

# Пагинация
GET /Patient?_count=20
GET /Patient?_count=20&_offset=40

# Include связанных ресурсов
GET /Observation?patient=123&_include=Observation:patient
GET /Patient/123?_revinclude=Observation:patient

```

### 3.3 Bundle и Transaction

```json

{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "request": {
        "method": "POST",
        "url": "Patient"
      },
      "resource": {
        "resourceType": "Patient",
        "name": [{"family": "Иванов", "given": ["Иван"]}]
      }
    },
    {
      "request": {
        "method": "POST",
        "url": "Observation"
      },
      "resource": {
        "resourceType": "Observation",
        "status": "final",
        "subject": {"reference": "Patient/123"},
        "code": {"coding": [{"code": "8480-6"}]},
        "valueQuantity": {"value": 120, "unit": "mmHg"}
      }
    }
  ]
}

```

---

## 4. Работа с FHIR в Python

### 4.1 Библиотека fhir.resources

```bash

pip install fhir.resources requests

```

### 4.2 Создание ресурсов

```python

from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address
from datetime import date

# Создание пациента
patient = Patient(
    identifier=[
        Identifier(
            use="official",
            system="http://hospital.org/patients",
            value="MRN-123456"
        )
    ],
    active=True,
    name=[
        HumanName(
            use="official",
            family="Иванов",
            given=["Иван", "Петрович"]
        )
    ],
    telecom=[
        ContactPoint(
            system="phone",
            value="+7-999-123-4567",
            use="mobile"
        ),
        ContactPoint(
            system="email",
            value="ivan@example.com"
        )
    ],
    gender="male",
    birthDate=date(1980, 5, 15),
    address=[
        Address(
            use="home",
            line=["ул. Примерная, д. 10"],
            city="Москва",
            postalCode="123456",
            country="RU"
        )
    ]
)

# Конвертация в JSON
print(patient.json(indent=2))

```

### 4.3 FHIR Client

```python

import requests
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation

class FHIRClient:
    """Простой клиент для работы с FHIR сервером."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/fhir+json",
            "Content-Type": "application/fhir+json"
        })
    
    def create(self, resource) -> dict:
        """Создаёт ресурс на сервере."""
        resource_type = resource.resource_type
        response = self.session.post(
            f"{self.base_url}/{resource_type}",
            json=resource.dict()
        )
        response.raise_for_status()
        return response.json()
    
    def read(self, resource_type: str, resource_id: str) -> dict:
        """Читает ресурс по ID."""
        response = self.session.get(
            f"{self.base_url}/{resource_type}/{resource_id}"
        )
        response.raise_for_status()
        return response.json()
    
    def search(self, resource_type: str, **params) -> list:
        """Поиск ресурсов."""
        response = self.session.get(
            f"{self.base_url}/{resource_type}",
            params=params
        )
        response.raise_for_status()
        bundle = response.json()
        
        if 'entry' in bundle:
            return [entry['resource'] for entry in bundle['entry']]
        return []
    
    def update(self, resource) -> dict:
        """Обновляет ресурс."""
        resource_type = resource.resource_type
        response = self.session.put(
            f"{self.base_url}/{resource_type}/{resource.id}",
            json=resource.dict()
        )
        response.raise_for_status()
        return response.json()
    
    def delete(self, resource_type: str, resource_id: str):
        """Удаляет ресурс."""
        response = self.session.delete(
            f"{self.base_url}/{resource_type}/{resource_id}"
        )
        response.raise_for_status()

# Использование
client = FHIRClient("http://hapi.fhir.org/baseR4")

# Создание пациента
created = client.create(patient)
print(f"Created patient with ID: {created['id']}")

# Поиск пациентов
patients = client.search("Patient", family="Иванов")
print(f"Found {len(patients)} patients")

```

### 4.4 Создание Observation

```python

from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.quantity import Quantity
from fhir.resources.reference import Reference
from datetime import datetime

def create_vital_sign(patient_id: str, code: str, display: str,
                      value: float, unit: str) -> Observation:
    """Создаёт Observation для vital sign."""
    
    return Observation(
        status="final",
        category=[
            CodeableConcept(
                coding=[
                    Coding(
                        system="http://terminology.hl7.org/CodeSystem/observation-category",
                        code="vital-signs",
                        display="Vital Signs"
                    )
                ]
            )
        ],
        code=CodeableConcept(
            coding=[
                Coding(
                    system="http://loinc.org",
                    code=code,
                    display=display
                )
            ]
        ),
        subject=Reference(reference=f"Patient/{patient_id}"),
        effectiveDateTime=datetime.now(),
        valueQuantity=Quantity(
            value=value,
            unit=unit,
            system="http://unitsofmeasure.org"
        )
    )

# Создание vital signs
heart_rate = create_vital_sign(
    patient_id="patient-123",
    code="8867-4",
    display="Heart rate",
    value=72,
    unit="/min"
)

temperature = create_vital_sign(
    patient_id="patient-123",
    code="8310-5",
    display="Body temperature",
    value=36.6,
    unit="Cel"
)

print("Heart Rate:")
print(heart_rate.json(indent=2))

```

---

## 5. References и связи

### 5.1 Структура Reference

```python
# Способы указания reference
references = {
    "literal": {
        "reference": "Patient/patient-123"
    },
    "with_display": {
        "reference": "Patient/patient-123",
        "display": "Иванов Иван"
    },
    "logical": {
        "identifier": {
            "system": "http://hospital.org/patients",
            "value": "MRN-123456"
        }
    },
    "external": {
        "reference": "http://other-system.org/fhir/Patient/ext-123"
    }
}

```

### 5.2 Связи между ресурсами

```

Patient ←──────────────────────────────────────────────────────────┐
   │                                                                │
   │ subject                                                        │
   ▼                                                                │
Encounter ←───────────────────────────────────┐                    │
   │                                          │                    │
   │ encounter                                │ subject            │
   ▼                                          │                    │
Observation ──────────────────────────────────┴────────────────────┘
   │
   │ basedOn
   ▼
ServiceRequest
   │
   │ result
   ▼
DiagnosticReport

```

---

## 6. Публичные FHIR серверы

```python

public_fhir_servers = {
    "HAPI FHIR": {
        "url": "http://hapi.fhir.org/baseR4",
        "version": "R4",
        "description": "Тестовый сервер, данные могут быть удалены"
    },
    "Firely Server": {
        "url": "https://server.fire.ly/r4",
        "version": "R4",
        "description": "Тестовый сервер Firely"
    },
    "SMART Health IT": {
        "url": "https://r4.smarthealthit.org",
        "version": "R4",
        "description": "Sandbox с синтетическими данными"
    }
}

# Проверка доступности сервера
import requests

def check_fhir_server(base_url: str) -> dict:
    """Проверяет FHIR сервер через CapabilityStatement."""
    try:
        response = requests.get(
            f"{base_url}/metadata",
            headers={"Accept": "application/fhir+json"},
            timeout=10
        )
        if response.status_code == 200:
            cs = response.json()
            return {
                "status": "online",
                "fhir_version": cs.get("fhirVersion"),
                "software": cs.get("software", {}).get("name")
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Проверка
for name, info in public_fhir_servers.items():
    result = check_fhir_server(info["url"])
    print(f"{name}: {result['status']}")

```

---

## 7. Частые ошибки

### 7.1 Неправильный формат Reference

```python
# ❌ Неправильно
observation = Observation(
    subject="patient-123"  # Строка вместо Reference
)

# ✅ Правильно
observation = Observation(
    subject={"reference": "Patient/patient-123"}
)

```

### 7.2 Пропущенные обязательные поля

```python
# ❌ Неправильно — нет status
observation = Observation(
    code={"coding": [{"code": "718-7"}]},
    valueQuantity={"value": 14.5}
)

# ✅ Правильно
observation = Observation(
    status="final",  # Обязательно!
    code={"coding": [{"code": "718-7"}]},
    valueQuantity={"value": 14.5}
)

```

### 7.3 Неправильный формат даты

```python

from datetime import date

# ❌ Неправильно
patient = Patient(birthDate="15/05/1980")

# ✅ Правильно
patient = Patient(birthDate=date(1980, 5, 15))
# или
patient = Patient(birthDate="1980-05-15")

```

---

## 💡 Key Takeaways

- **FHIR** — современный REST/JSON стандарт для healthcare

- **Resources** — модульные строительные блоки (~150 типов)

- **REST API** — стандартные HTTP операции (GET, POST, PUT, DELETE)

- **References** — связи между ресурсами через `{"reference": "Type/id"}`

- **R4** — рекомендуемая версия для production

- **Публичные серверы** — доступны для тестирования и обучения

---

## 🚀 Next Steps

**Следующие модули:**

- [04_Standards](../04_Standards/) — ICD-10, SNOMED CT, LOINC
- [05_EHR_Systems](../05_EHR_Systems/) — Системы электронных медицинских записей

**Практика:**

1. Создайте Patient ресурс с полной информацией
2. Сделайте запросы к публичному FHIR серверу
3. Создайте Observation для vital signs
4. Реализуйте поиск пациентов по различным параметрам

---

## 📚 Additional Resources

- [FHIR Specification](https://www.hl7.org/fhir/)
- [FHIR R4 Resources](https://www.hl7.org/fhir/resourcelist.html)
- [fhir.resources Python Library](https://pypi.org/project/fhir.resources/)
- [HAPI FHIR Server](https://hapifhir.io/)

---





