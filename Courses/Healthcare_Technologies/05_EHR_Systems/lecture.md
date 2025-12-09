# Системы Электронных Медицинских Записей (EHR)
## Архитектура, интеграция и SMART on FHIR

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [01_Terminology](../01_Terminology/) — медицинская терминология
- Понимать основы HL7 и FHIR
- Иметь опыт работы с REST API

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять разницу между EHR и EMR системами
- Описывать архитектуру современной EHR системы
- Интегрировать приложения через HL7 интерфейсы
- Разрабатывать SMART on FHIR приложения

---

## 1. Введение

Electronic Health Record (EHR) системы — это цифровая версия медицинской карты пациента. В этом модуле мы рассмотрим архитектуру и функциональность современных EHR систем.

---

## 2. EHR vs EMR

| Характеристика | EMR | EHR |
|----------------|-----|-----|
| **Определение** | Electronic Medical Record | Electronic Health Record |
| **Scope** | Одна организация | Множество организаций |
| **Sharing** | Ограниченный | Широкий обмен |
| **Focus** | Clinical care | Holistic health |

**EMR** = Цифровая карта внутри одной клиники  
**EHR** = Полная медицинская история пациента, доступная везде

---

## 2. Архитектура EHR Системы

```
┌─────────────────────────────────────────────────┐
│            User Interface Layer                  │
│  (Web, Mobile, Desktop Client)                  │
└─────────────────────────────────────────────────┘
                     ↕
┌─────────────────────────────────────────────────┐
│         Application Services Layer               │
│  • Patient Management                            │
│  • Clinical Documentation                        │
│  • Order Entry (CPOE)                           │
│  • Clinical Decision Support (CDSS)             │
│  • Reporting & Analytics                        │
└─────────────────────────────────────────────────┘
                     ↕
┌─────────────────────────────────────────────────┐
│          Integration Layer                       │
│  • HL7 Interface Engine                         │
│  • FHIR API Gateway                             │
│  • DICOM Integration                            │
└─────────────────────────────────────────────────┘
                     ↕
┌─────────────────────────────────────────────────┐
│            Data Layer                            │
│  • Relational DB (Patient Demographics)         │
│  • Document Store (Clinical Notes)              │
│  • BLOB Storage (Images)                        │
└─────────────────────────────────────────────────┘
```

---

## 3. Ключевые Компоненты EHR

### 3.1 Patient Management

- Регистрация пациентов
- Demographics (имя, DOB, адрес)
- Insurance информация
- Master Patient Index (MPI) — уникальная идентификация

### 3.2 Clinical Documentation

- Progress notes
- History & Physical
- Discharge summaries
- Structured templates

### 3.3 Computerized Physician Order Entry (CPOE)

- Электронные назначения лекарств
- Лабораторные анализы
- Радиологические исследования
- Процедуры

### 3.4 Clinical Decision Support System (CDSS)

- Drug-drug interaction alerts
- Allergy checking
- Clinical guidelines
- Predictive analytics

### 3.5 Results Management

- Лабораторные результаты
- Radiology reports
- Pathology reports

---

## 4. Health Information Exchange (HIE)

### 4.1 Модели HIE

**Centralized (Консолидированная)**
```
Hospital A ──┐
Hospital B ──┼──→ Central Repository ←── Query
Hospital C ──┘
```

**Federated (Федеративная)**
```
Hospital A ←──┐
Hospital B ←──┼── Query Router
Hospital C ←──┘
```

**Hybrid**
```
Комбинация централизованной и федеративной моделей
```

### 4.2 Query Types

- **Patient Discovery** — найти пациента в сети
- **Document Query** — получить документы пациента
- **Document Retrieve** — скачать конкретный документ

---

## 5. Интеграция с Медицинским Оборудованием

### 5.1 HL7 MLLP (Minimal Lower Layer Protocol)

```python
import socket

def send_hl7_message(host, port, message):
    # HL7 MLLP framing
    START_BLOCK = b'\x0b'  # Vertical Tab
    END_BLOCK = b'\x1c'    # File Separator
    CARRIAGE_RETURN = b'\x0d'
    
    # Wrap message
    wrapped = START_BLOCK + message.encode() + END_BLOCK + CARRIAGE_RETURN
    
    # Send
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(wrapped)
    
    # Receive ACK
    response = sock.recv(4096)
    sock.close()
    
    return response
```

### 5.2 DICOM Integration

```python
import pydicom

# Чтение DICOM файла
ds = pydicom.dcmread("image.dcm")

# Метаданные
patient_name = ds.PatientName
study_date = ds.StudyDate
modality = ds.Modality  # CT, MRI, X-ray, etc

# Пиксельные данные
image = ds.pixel_array
```

---

## 6. FHIR в EHR Системах

### 6.1 SMART on FHIR

Платформа для интеграции медицинских приложений с EHR.

```javascript
// SMART on FHIR app launch
FHIR.oauth2.authorize({
  "client_id": "my_app",
  "scope": "patient/Patient.read patient/Observation.read"
}).then(function(client) {
  // Получить данные пациента
  client.request("Patient/" + client.patient.id).then(function(patient) {
    console.log(patient);
  });
});
```

---

## 7. Best Practices

### 7.1 Производительность

- **Caching** — кэшировать часто используемые данные
- **Pagination** — не загружать все записи сразу
- **Async processing** — фоновая обработка отчётов

### 7.2 Надёжность

- **High Availability** — нет downtime
- **Disaster Recovery** — бэкапы и failover
- **Data Integrity** — ACID транзакции

### 7.3 Usability

- **Intuitive UI** — врачи не IT-специалисты
- **Mobile access** — доступ с планшетов
- **Fast response** — <2 секунд для критических операций

---

## Резюме

- ✅ EHR vs EMR различия
- ✅ Архитектура EHR систем (многоуровневая)
- ✅ Ключевые компоненты: CPOE, CDSS, Results Management
- ✅ Health Information Exchange модели
- ✅ Интеграция с оборудованием (HL7 MLLP, DICOM)
- ✅ SMART on FHIR для приложений

---

## 🚀 Следующие Шаги

**Связанные модули:**
- [Medical Terminology](../01_Terminology/) — HL7, FHIR, ICD-10 стандарты
- [Security & Privacy](../03_Security_Privacy/) — HIPAA, GDPR и безопасность
- [Medical Imaging](../04_Medical_Imaging/) — DICOM и PACS системы

**Идеи для практики:**
1. **Database Schema** — проектирование схемы БД: Patients, Encounters, Medications, Observations
2. **FHIR API Mock Server** — простой FHIR сервер на Flask с endpoints GET/POST /Patient
3. **HL7 MLLP Receiver** — TCP сервер для приёма HL7 сообщений и отправки ACK
4. **CDSS Rule Engine** — проверка drug-drug interactions и allergy checking
5. **HIE Query Router** — федеративный запрос к нескольким источникам с агрегацией

---

## 📚 Дополнительные Ресурсы

**Open Source EHR системы:**
- [OpenEMR](https://www.open-emr.org/) — open source EHR система
- [OpenMRS](https://openmrs.org/) — open source medical record system

**SMART on FHIR:**
- [SMART Health IT](https://smarthealthit.org/) — документация и примеры
- [SMART App Gallery](https://gallery.smarthealthit.org/) — примеры SMART приложений

**HIE:**
- [Health Information Exchange](https://www.healthit.gov/topic/health-it-and-health-information-exchange-basics) — обзор от HealthIT.gov

---

## 💡 Key Takeaways

- **EHR ≠ EMR**: EHR охватывает данные из множества организаций, EMR — только одну
- **SMART on FHIR** — стандарт для безопасного запуска приложений внутри EHR
- **CDSS** — системы поддержки принятия решений, встроенные в EHR
- **HIE** — обмен данными между организациями (pull vs push модели)
- **Interoperability** — главная проблема Healthcare IT, FHIR её решает

---

## 🚀 Next Steps

**Следующие модули:**
- [03_Security_Privacy](../03_Security_Privacy/) — Безопасность и HIPAA
- [04_Medical_Imaging](../04_Medical_Imaging/) — Медицинские изображения и DICOM

**Практика:**
1. Изучите API документацию публичного EHR sandbox (Epic, Cerner)
2. Создайте простое SMART on FHIR приложение
3. Реализуйте HL7 MLLP receiver на Python

