# Медицинская Терминология и Стандарты
## HL7, FHIR, ICD-10, SNOMED CT и DICOM

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
- Работать с HL7 v2 сообщениями и FHIR ресурсами
- Применять классификаторы ICD-10, SNOMED CT, LOINC
- Понимать структуру DICOM файлов медицинских изображений

---

## 1. Введение

Работа в Healthcare IT требует понимания медицинской терминологии и стандартов. В этом модуле мы изучим ключевые концепции и стандарты.

---

## 2. Базовая Медицинская Терминология

### 1.1 Основные термины

В медицинских информационных системах используются специфические термины, которые важно понимать для корректной работы с данными.

**Patient (Пациент)**
- Человек, который получает медицинскую помощь
- В системах имеет уникальный идентификатор (Medical Record Number, MRN)
- Связан с множеством других данных: визиты, диагнозы, назначения

**Пример:** Пациент John Doe, MRN: 123456789, связан с 15 визитами, 3 хроническими диагнозами, 5 активными назначениями лекарств.

**Encounter (Визит/Встреча)**
- Любое взаимодействие пациента с медицинским учреждением
- Типы: амбулаторный визит, госпитализация, экстренный визит, телемедицина
- Каждый encounter имеет дату/время начала и окончания, место, врача

**Пример:** Амбулаторный визит 15.03.2024, 10:00-10:30, кабинет 205, терапевт Dr. Smith.

**Diagnosis (Диагноз)**
- Определение заболевания или состояния пациента
- Кодируется стандартными кодами (ICD-10)
- Может быть: предварительный, подтвержденный, дифференциальный

**Пример:** E11.9 - Сахарный диабет 2 типа без осложнений, подтвержденный диагноз, с 2020 года.

**Procedure (Процедура)**
- Любое медицинское вмешательство: операция, обследование, манипуляция
- Также кодируется стандартными кодами (CPT, ICD-10-PCS)
- Имеет исполнителя, дату, место проведения

**Пример:** Удаление аппендикса, хирург Dr. Johnson, операционная №3, 2 часа, успешно завершена.

**Medication (Лекарство/Медикамент)**
- Лекарственный препарат для лечения или профилактики
- Включает: название, дозировку, форму выпуска, производителя
- Связан с назначениями (prescriptions) и введениями (administrations)

**Пример:** Метформин 500mg таблетки, 2 раза в день после еды, курс 3 месяца.

**Vital Signs (Жизненные показатели)**
- Базовые физиологические параметры:
  - Артериальное давление (BP): 120/80 mmHg
  - Пульс (HR): 72 уд/мин
  - Температура тела: 36.6°C
  - Частота дыхания (RR): 16/мин
  - Сатурация кислорода (SpO2): 98%
- Измеряются при каждом визите

**Allergy (Аллергия)**
- Непереносимость или аллергическая реакция на вещество
- Критически важно для безопасности: предотвращает назначение опасных препаратов
- Включает: аллерген, тип реакции, степень тяжести

**Пример:** Аллергия на пенициллин, реакция: анафилактический шок, степень: критическая → система ЗАПРЕТИТ назначение пенициллина.

**Observation (Наблюдение/Измерение)**
- Любые измеренные или наблюдаемые данные о пациенте
- Включает: лабораторные анализы, vital signs, клинические заметки
- Имеет: тип измерения, значение, единицы, референсный диапазон

**Пример:** Гемоглобин: 145 g/L (норма 130-160), дата анализа: 20.03.2024.

### 1.2 Типы медицинских данных

Медицинские данные в информационных системах организованы по категориям:

**Demographics (Демографические данные)**
- Идентификационная информация о пациенте
- Имя, фамилия, отчество
- Дата рождения (для расчета возраста)
- Пол (биологический и гендерная идентичность)
- Адрес, контактные телефоны, email
- Раса/этничность (для исследований и статистики)
- Семейное положение, занятость

**Clinical Data (Клинические данные)**
- Основная медицинская информация:
  - **Диагнозы**: текущие и прошлые заболевания
  - **Процедуры**: операции, обследования, манипуляции
  - **Медикаменты**: текущие и прошлые назначения
  - **Аллергии**: непереносимость препаратов и веществ
  - **Vital Signs**: регулярные измерения
  - **История болезни**: течение заболеваний
  - **Семейный анамнез**: наследственные заболевания

**Administrative Data (Административные данные)**
- Страховая информация (номер полиса, компания)
- Финансовые данные (billing, payments)
- Назначения (appointments)
- Направления к специалистам (referrals)
- Авторизации на процедуры

**Imaging Data (Данные медицинской визуализации)**
- Рентгеновские снимки (X-ray)
- Компьютерная томография (CT)
- Магнитно-резонансная томография (MRI)
- Ультразвуковые исследования (Ultrasound)
- ПЭТ-сканирование (PET)
- Каждое изображение с метаданными: дата, оборудование, настройки

**Laboratory Results (Лабораторные результаты)**
- Анализы крови (общий, биохимия, гормоны)
- Анализы мочи
- Микробиологические посевы
- Генетические тесты
- Каждый результат с: значением, единицами, референсным диапазоном

### 1.3 Идентификаторы в Healthcare

**Почему это важно:** В healthcare часто работают с данными из разных источников. Правильная идентификация критична для безопасности пациента.

**Medical Record Number (MRN)**
- Уникальный идентификатор пациента внутри одного учреждения
- Формат определяется учреждением
- Пример: MRN-2024-123456

**National Patient Identifier**
- В разных странах разные системы:
  - США: нет единого идентификатора (проблема!)
  - Великобритания: NHS Number (10 цифр)
  - Россия: СНИЛС (11 цифр)

**Problem List ID**
- Уникальный ID для каждой проблемы/диагноза пациента
- Позволяет отслеживать течение заболевания

**Пример сценария:**
```
Пациент John Doe поступил в Emergency Room:

- Проверка: MRN существует? → Да, найден
- Загрузка: аллергии, текущие медикаменты, прошлые диагнозы
- Врач видит: аллергия на пенициллин!
- Врач назначает: амоксициллин (содержит пенициллин)
- Система БЛОКИРУЕТ назначение с предупреждением
- Врач назначает альтернативный антибиотик
```

Это реальный пример того, как правильно структурированные данные спасают жизни!

---

## 2. HL7 — Health Level 7

### 2.1 Что такое HL7?

**HL7 (Health Level 7)** — международный стандарт для обмена, интеграции, совместного использования и извлечения электронной медицинской информации.

**Откуда название "Level 7"?**
- Ссылка на 7-й уровень модели OSI (Application Layer)
- HL7 работает на уровне приложений, определяя формат и структуру данных

**Зачем нужен HL7?**

Представьте больницу с десятками систем:

- Электронная медицинская карта (EMR)
- Лабораторная информационная система (LIS)
- Радиологическая система (RIS/PACS)
- Аптечная система
- Система биллинга

Без стандарта каждая интеграция — это уникальная разработка. HL7 решает эту проблему, предоставляя единый язык для обмена данными.

**Версии HL7:**

**HL7 v2.x (1988 - настоящее время)**
- Текстовый формат с разделителями (pipe-delimited)
- **Самый распространенный**: ~95% медицинских учреждений используют
- Легкий для парсинга, но гибкость привела к проблемам совместимости
- Актуальная версия: 2.9 (но 2.3, 2.4, 2.5 все еще широко используются)

**HL7 v3 (2005 - почти не используется)**
- XML-based, теоретически идеален
- Слишком сложный, громоздкий
- Дорогая имплементация
- Практически провалился в реальном мире

**FHIR (Fast Healthcare Interoperability Resources, 2014 - настоящее время)**
- Современный REST/JSON подход
- Легкий для разработчиков
- Быстро набирает популярность
- Будущее HL7 (подробнее в разделе 3)

### 2.2 HL7 v2 Структура

HL7 v2 сообщение состоит из сегментов (строк), каждый сегмент из полей, поля из компонентов.

**Пример реального HL7 v2 сообщения (госпитализация пациента):**

```
MSH|^~\&|SENDING_APP|SENDING_FACILITY|RECEIVING_APP|RECEIVING_FACILITY|20230101120000||ADT^A01|MSG123|P|2.5
EVN|A01|20230101120000|||USER123
PID|1||123456789^^^FACILITY^MR||Doe^John^Michael^^Jr^||19800101|M|||123 Main St^^New York^NY^10001^USA||555-1234|||M|Catholic|987654321
PV1|1|I|ICU^201^A|||DOC123^Smith^Jane^^^Dr||||SUR||||ADM|A0||||||||||||||||||||||||||20230101120000
```

**Разбор структуры по уровням:**

**Уровень 1: Segment (Сегмент)**
- Каждая строка — это отдельный сегмент
- Начинается с 3-х буквенного кода-идентификатора
- Заканчивается переводом строки (или CR)

```
MSH  → Message Header (заголовок сообщения)
EVN  → Event Type (тип события)
PID  → Patient Identification (идентификация пациента)
PV1  → Patient Visit (информация о визите)
```

**Уровень 2: Field (Поле)**
- Разделены символом `|` (pipe)
- Нумерация начинается с 1
- Пустое поле: `||` (два разделителя подряд)

```
PID|1||123456789||Doe^John^Michael||19800101|M|||
     ↑  ↑         ↑                 ↑        ↑
   PID-1 PID-2   PID-3            PID-5    PID-7  PID-8
```

**Уровень 3: Component (Компонент)**
- Разделены символом `^` (caret)
- Используются для составных данных (имя, адрес)

```
Doe^John^Michael^^Jr
 ↑   ↑    ↑      ↑ ↑
Фамилия  Отчество  Суффикс
    Имя    (пусто)
```

**Уровень 4: Subcomponent (Подкомпонент)**
- Разделены символом `&` (ampersand)
- Используются редко, для еще более детальных данных

```
123456789^^^FACILITY^MR
          ↑             ↑
     (разделители)   Тип ID
```

**Специальные символы (Encoding Characters):**

Определяются в сегменте MSH сразу после MSH:

```
MSH|^~\&|...
    ↑↑↑↑
    ||||→ & (subcomponent separator)
    |||→  \ (escape character)
    ||→   ~ (repetition separator)
    |→    ^ (component separator)
```

**Основные сегменты HL7 v2:**

| Сегмент | Название | Назначение | Обязательность |
|---------|----------|------------|----------------|
| **MSH** | Message Header | Метаданные: отправитель, получатель, тип сообщения, версия | Обязательный |
| **EVN** | Event Type | Информация о событии: код, дата/время, ответственный | Часто обязательный |
| **PID** | Patient Identification | Идентификация пациента: MRN, имя, дата рождения, пол, адрес | Обязательный для пациентов |
| **PV1** | Patient Visit | Информация о визите: тип, локация, врач, дата поступления | Для визитов |
| **OBR** | Observation Request | Заказ на исследование: тип, приоритет, исполнитель | Для лабораторных/радиологических заказов |
| **OBX** | Observation Result | Результат наблюдения: тип, значение, единицы, диапазон | Для результатов |
| **AL1** | Allergy Information | Информация об аллергии: аллерген, тип реакции, степень | Для аллергий |
| **DG1** | Diagnosis | Диагноз: код ICD-10, тип, приоритет | Для диагнозов |

**Детальный разбор PID сегмента:**

```
PID|1||123456789^^^HOSPITAL^MR||Doe^John^Michael^^Jr^||19800101|M|||123 Main St^^New York^NY^10001^USA||555-1234|||M|Catholic|987654321
```

Поле за полем:

- **PID-1** (1): Set ID - порядковый номер
- **PID-2** (пусто): Patient ID (External) - внешний ID (устаревшее, не используется)
- **PID-3** (123456789^^^HOSPITAL^MR): Patient ID (Internal) - MRN пациента
  - 123456789 = номер
  - ^^^HOSPITAL = источник (facility)
  - ^MR = тип (Medical Record)
- **PID-4** (пусто): Alternate Patient ID (альтернативный ID)
- **PID-5** (Doe^John^Michael^^Jr^): Patient Name - имя пациента
  - Doe = фамилия
  - John = имя
  - Michael = отчество
  - (пусто) = префикс
  - Jr = суффикс
- **PID-7** (19800101): Date of Birth - дата рождения (YYYYMMDD)
- **PID-8** (M): Sex - пол (M=Male, F=Female, O=Other, U=Unknown)
- **PID-9**, **PID-10** (пусто): Race, Patient Alias (не указаны)
- **PID-11** (123 Main St^^New York^NY^10001^USA): Patient Address - адрес
  - 123 Main St = улица
  - (пусто) = дополнительная информация
  - New York = город
  - NY = штат
  - 10001 = почтовый индекс
  - USA = страна
- **PID-13** (555-1234): Phone Number - телефон
- **PID-16** (M): Marital Status - семейное положение (M=Married)
- **PID-17** (Catholic): Religion - религия
- **PID-18** (987654321): Patient Account Number - номер счета пациента

### 2.3 Типы сообщений HL7

HL7 сообщения классифицируются по типу события. Формат: `MessageType^TriggerEvent`

**ADT (Admission, Discharge, Transfer) — Управление пациентами:**

| Код | Событие | Описание | Пример использования |
|-----|---------|----------|----------------------|
| ADT^A01 | Admit/Visit | Поступление пациента (госпитализация) | Пациент поступил в стационар |
| ADT^A02 | Transfer | Перевод пациента в другое отделение | Из терапии в хирургию |
| ADT^A03 | Discharge | Выписка пациента | Пациент выписан домой |
| ADT^A04 | Register | Регистрация амбулаторного пациента | Пришел на прием к врачу |
| ADT^A08 | Update | Обновление информации о пациенте | Изменился адрес или телефон |
| ADT^A11 | Cancel Admit | Отмена госпитализации | Ошибочно зарегистрировали |
| ADT^A13 | Cancel Discharge | Отмена выписки | Пациент вернулся |
| ADT^A28 | Add Person | Добавление нового пациента в систему | Новый пациент |
| ADT^A31 | Update Person | Обновление демографических данных | Изменение имени, адреса |

**ORM (Order) — Назначения:**

| Код | Событие | Описание | Пример |
|-----|---------|----------|--------|
| ORM^O01 | Order Message | Назначение обследования/процедуры | Врач назначил анализ крови |
| ORM^O02 | Cancel Order | Отмена назначения | Отменили МРТ |
| ORM^O05 | Change Order | Изменение назначения | Изменили дозировку |

**ORU (Observation Result) — Результаты:**

| Код | Событие | Описание | Пример |
|-----|---------|----------|--------|
| ORU^R01 | Observation Result | Результаты лабораторных анализов | Готов общий анализ крови |
| ORU^R03 | Result with Order | Результат с информацией о заказе | Развернутый ответ |

**SIU (Scheduling) — Расписание:**

| Код | Событие | Описание | Пример |
|-----|---------|----------|--------|
| SIU^S12 | Notification of New Appointment | Новая запись на прием | Пациент записан к кардиологу |
| SIU^S13 | Notification of Appointment Rescheduling | Перенос приема | Прием перенесен на другой день |
| SIU^S15 | Notification of Appointment Cancellation | Отмена приема | Пациент отменил визит |

**MDM (Medical Document Management) — Документы:**

| Код | Событие | Описание | Пример |
|-----|---------|----------|--------|
| MDM^T02 | Document Status Change | Изменение статуса документа | Эпикриз подписан |
| MDM^T04 | Document Edit | Редактирование документа | Врач исправил описание |

**Примеры реальных сценариев:**

**Сценарий 1: Поступление в Emergency Room**

```
1. ADT^A04 → Регистрация пациента
2. ORM^O01 → Назначен общий анализ крови
3. ORM^O01 → Назначен рентген грудной клетки
4. ORU^R01 → Готов результат анализа крови
5. ORU^R01 → Готов рентген
6. ADT^A01 → Решено госпитализировать
7. ORM^O01 → Назначена антибиотикотерапия
```

**Сценарий 2: Амбулаторный визит**

```
1. SIU^S12 → Пациент записан на прием (неделю назад)
2. ADT^A04 → Пациент пришел, регистрация
3. ORM^O01 → Врач назначил анализ мочи
4. ADT^A03 → Пациент ушел
5. ORU^R01 → Через 2 дня готов анализ (отправлен пациенту)
```

**Сценарий 3: Изменение данных пациента**

```
1. ADT^A28 → Новый пациент создан с ошибкой в имени
2. ADT^A31 → Администратор исправил имя
3. ADT^A08 → Обновлен адрес (пациент переехал)
```

### 2.4 Парсинг HL7 в Python

Библиотека `python-hl7` — стандартный инструмент для работы с HL7 v2 сообщениями.

**Базовый парсинг:**

```python
import hl7

# Пример HL7 сообщения (обычно приходит как строка)
hl7_string = """MSH|^~\\&|SENDING_APP|FACILITY|RECEIVING_APP|FACILITY|20240315120000||ADT^A01|MSG001|P|2.5
EVN|A01|20240315120000
PID|1||123456789^^^HOSPITAL^MR||Doe^John^Michael^^Jr^||19800101|M|||123 Main St^^New York^NY^10001||555-1234
PV1|1|I|ICU^201^A|||DOC123^Smith^Jane^^^Dr||||SUR||||ADM|A0"""

# Парсинг сообщения
message = hl7.parse(hl7_string)

# Доступ к сегментам
msh = message.segment('MSH')  # Message Header
pid = message.segment('PID')  # Patient ID
pv1 = message.segment('PV1')  # Patient Visit

print(f"Message type: {msh[9]}")  # ADT^A01
print(f"Message ID: {msh[10]}")   # MSG001
```

**Работа с PID (Patient Identification):**

```python
# PID сегмент содержит информацию о пациенте
pid = message.segment('PID')

# Доступ к полям (индексация с 1, но python с 0, поэтому -1)
# PID-3: Patient ID
patient_id_field = pid[3]  # "123456789^^^HOSPITAL^MR"
# Получаем первый компонент (сам ID)
patient_id = str(patient_id_field[0])  # "123456789"

# PID-5: Patient Name (Фамилия^Имя^Отчество^^Суффикс)
patient_name_field = pid[5]
last_name = str(patient_name_field[0])   # "Doe"
first_name = str(patient_name_field[1])  # "John"
middle_name = str(patient_name_field[2]) # "Michael"
suffix = str(patient_name_field[4])      # "Jr"

full_name = f"{first_name} {middle_name} {last_name} {suffix}".strip()
print(f"Patient: {full_name}")  # "John Michael Doe Jr"

# PID-7: Date of Birth (YYYYMMDD)
dob = str(pid[7])  # "19800101"
# Преобразуем в читаемый формат
from datetime import datetime
dob_date = datetime.strptime(dob, '%Y%m%d')
print(f"DOB: {dob_date.strftime('%Y-%m-%d')}")  # "1980-01-01"

# Вычисляем возраст
age = (datetime.now() - dob_date).days // 365
print(f"Age: {age}")

# PID-8: Sex
sex = str(pid[8])  # "M"
sex_full = {"M": "Male", "F": "Female", "O": "Other", "U": "Unknown"}.get(sex, "Unknown")
print(f"Sex: {sex_full}")

# PID-11: Patient Address
address_field = pid[11]
street = str(address_field[0])      # "123 Main St"
city = str(address_field[2])        # "New York"
state = str(address_field[3])       # "NY"
zip_code = str(address_field[4])    # "10001"
print(f"Address: {street}, {city}, {state} {zip_code}")

# PID-13: Phone Number
phone = str(pid[13])  # "555-1234"
print(f"Phone: {phone}")
```

**Работа с результатами лабораторных анализов (OBX):**

```python
# Пример ORU^R01 сообщения с результатами
oru_message = """MSH|^~\\&|LAB|FACILITY|EMR|FACILITY|20240315143000||ORU^R01|LAB001|P|2.5
PID|1||123456789||Doe^John|||M
OBR|1||LAB-2024-001|CBC^Complete Blood Count|||20240315140000
OBX|1|NM|718-7^Hemoglobin^LN||145|g/L|135-175|N|||F
OBX|2|NM|787-2^WBC^LN||8.5|10*9/L|4.0-11.0|N|||F
OBX|3|NM|777-3^Platelets^LN||250|10*9/L|150-400|N|||F"""

message = hl7.parse(oru_message)

# OBR - Order/Request информация
obr = message.segment('OBR')
order_id = str(obr[3])  # "LAB-2024-001"
test_name = str(obr[4][1])  # "Complete Blood Count"
print(f"Test: {test_name} (Order: {order_id})")

# OBX - Результаты (может быть несколько)
# Используем segments() для получения всех OBX сегментов
obx_segments = [seg for seg in message if seg[0] == 'OBX']

print("\nResults:")
for obx in obx_segments:
    # OBX-3: Observation Identifier
    test_code = str(obx[3][0])       # "718-7"
    test_name = str(obx[3][1])       # "Hemoglobin"
    
    # OBX-5: Observation Value
    value = str(obx[5])              # "145"
    
    # OBX-6: Units
    units = str(obx[6])              # "g/L"
    
    # OBX-7: Reference Range
    ref_range = str(obx[7])          # "135-175"
    
    # OBX-8: Abnormal Flags
    abnormal_flag = str(obx[8])      # "N" (Normal)
    
    flag_text = {
        "N": "Normal",
        "L": "Low",
        "H": "High",
        "LL": "Critical Low",
        "HH": "Critical High"
    }.get(abnormal_flag, "")
    
    print(f"  {test_name}: {value} {units} (ref: {ref_range}) - {flag_text}")
```

**Создание HL7 сообщения:**

```python
from datetime import datetime

def create_adt_a04(patient_id, last_name, first_name, dob, sex):
    """Создает ADT^A04 сообщение (регистрация амбулаторного пациента)"""
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    msg_id = f"MSG{timestamp}"
    
    # Формируем сегменты
    msh = f"MSH|^~\\&|EMR|HOSPITAL|ADT|HOSPITAL|{timestamp}||ADT^A04|{msg_id}|P|2.5"
    evn = f"EVN|A04|{timestamp}"
    pid = f"PID|1||{patient_id}^^^HOSPITAL^MR||{last_name}^{first_name}||{dob}|{sex}"
    pv1 = f"PV1|1|O|OUTPATIENT||||DOC123^Doctor^Attending^^^MD"
    
    # Объединяем с переводом строки
    hl7_message = "\r".join([msh, evn, pid, pv1])
    
    return hl7_message

# Пример использования
new_patient = create_adt_a04(
    patient_id="999888777",
    last_name="Smith",
    first_name="Jane",
    dob="19920515",
    sex="F"
)

print(new_patient)
```

**Валидация HL7 сообщения:**

```python
def validate_hl7_message(hl7_string):
    """Базовая валидация HL7 сообщения"""
    errors = []
    
    try:
        message = hl7.parse(hl7_string)
    except Exception as e:
        return False, [f"Parse error: {e}"]
    
    # Проверка обязательных сегментов
    if not message.segment('MSH'):
        errors.append("Missing required MSH segment")
    
    msh = message.segment('MSH')
    
    # Проверка версии
    version = str(msh[12])
    if version not in ['2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9']:
        errors.append(f"Unsupported HL7 version: {version}")
    
    # Проверка типа сообщения
    msg_type = str(msh[9])
    if not msg_type:
        errors.append("Missing message type")
    
    # Для ADT сообщений требуется PID
    if msg_type.startswith('ADT') and not message.segment('PID'):
        errors.append("ADT message missing required PID segment")
    
    return len(errors) == 0, errors

# Пример использования
is_valid, validation_errors = validate_hl7_message(hl7_string)
if is_valid:
    print("✓ Valid HL7 message")
else:
    print("✗ Invalid HL7 message:")
    for error in validation_errors:
        print(f"  - {error}")
```

**Частые проблемы при работе с HL7:**

1. **Кодировка**: HL7 может быть в разных кодировках (UTF-8, Windows-1252)
2. **Разделители строк**: `\r`, `\n`, или `\r\n` — зависит от источника
3. **Пустые поля**: `||` vs `| |` — разные вещи
4. **Escape-последовательности**: `\F\` = `|`, `\S\` = `^`, `\T\` = `&`, `\R\` = `~`
5. **Повторяющиеся сегменты**: Может быть несколько OBX, AL1, DG1

---

## 3. FHIR — Fast Healthcare Interoperability Resources

### 3.1 Что такое FHIR?

**FHIR** (произносится "fire") — современный стандарт HL7 для обмена медицинскими данными через REST API. Это четвертое поколение стандартов HL7.

**Почему создали FHIR?**

HL7 v2 и v3 имели проблемы:

- HL7 v2: слишком гибкий → несовместимость между имплементациями
- HL7 v3: слишком сложный → дорого внедрять
- Оба: не подходят для мобильных приложений и современных веб-сервисов

FHIR решает эти проблемы, применяя современные веб-технологии:

**Ключевые преимущества FHIR:**

1. **RESTful API** — привычная архитектура для разработчиков
   - GET, POST, PUT, DELETE операции
   - HTTPS протокол
   - Стандартные HTTP status codes

2. **JSON или XML** — выбор формата данных
   - JSON для веб/мобильных приложений (легкий)
   - XML для enterprise систем (валидация через схемы)

3. **Модульная структура (Resources)** — строительные блоки
   - Каждый Resource — отдельная сущность (Patient, Observation, Medication)
   - Можно внедрять постепенно (не нужно все сразу)
   - Resources ссылаются друг на друга

4. **Простота для разработчиков**
   - Хорошая документация
   - Множество библиотек (Python, Java, C#, JavaScript)
   - Публичные тестовые серверы для экспериментов

5. **Расширяемость**
   - Можно добавлять свои поля через Extensions
   - Профили (Profiles) для специализации ресурсов

**FHIR Версии:**

- **DSTU1** (2014) — Draft Standard for Trial Use 1
- **DSTU2** (2015) — значительные изменения
- **STU3** (2017) — еще одна крупная ревизия
- **R4** (2019) — первый полный Release (текущий стандарт)
- **R5** (2023) — последняя версия с новыми возможностями

**Важно:** R4 — это стабильная версия, рекомендованная для production систем.

### 3.2 FHIR Resources

FHIR определяет ~150 типов ресурсов, организованных по категориям. Каждый Resource — это JSON/XML объект с определенной структурой.

**Категории Resources:**

**1. Foundation Resources (Базовые)**

| Resource | Описание | Основные поля |
|----------|----------|---------------|
| **Patient** | Демографические данные пациента | identifier, name, gender, birthDate, address, telecom |
| **Practitioner** | Медицинский работник (врач, медсестра) | identifier, name, qualification, specialty |
| **PractitionerRole** | Роль медработника в организации | practitioner, organization, code, specialty |
| **Organization** | Медицинская организация (больница, клиника) | identifier, name, type, address, telecom |
| **Location** | Физическое место (палата, кабинет, здание) | name, type, address, managingOrganization |
| **HealthcareService** | Услуга здравоохранения | providedBy, category, type, location |

**2. Clinical Resources (Клинические)**

| Resource | Описание | Когда используется |
|----------|----------|-------------------|
| **Encounter** | Визит/госпитализация | Любое взаимодействие пациента с медучреждением |
| **Observation** | Любое измерение или наблюдение | Vital signs, лабораторные анализы, клинические заметки |
| **Condition** | Диагноз/проблема/состояние | Заболевания, симптомы, травмы |
| **Procedure** | Процедура/операция/вмешательство | Хирургия, обследования, терапевтические процедуры |
| **AllergyIntolerance** | Аллергия или непереносимость | Аллергии на лекарства, продукты, вещества |
| **FamilyMemberHistory** | Семейный анамнез | Заболевания родственников |
| **ImagingStudy** | Исследование медицинской визуализации | Рентген, CT, MRI, УЗИ |
| **DiagnosticReport** | Диагностический отчет | Сводный отчет с результатами исследований |

**3. Medication Resources (Медикаменты)**

| Resource | Описание | Использование |
|----------|----------|---------------|
| **Medication** | Описание лекарства | Каталог медикаментов |
| **MedicationRequest** | Назначение/рецепт | Врач назначил лекарство |
| **MedicationAdministration** | Введение лекарства | Медсестра дала лекарство пациенту |
| **MedicationStatement** | Утверждение о приеме лекарства | Пациент сообщил, что принимает лекарство |
| **MedicationDispense** | Выдача лекарства | Аптека выдала лекарство |

**4. Workflow Resources (Управление процессами)**

| Resource | Описание | Пример |
|----------|----------|--------|
| **Appointment** | Запись на прием | Пациент записан к кардиологу на 15.03 в 10:00 |
| **AppointmentResponse** | Ответ на запись | Пациент подтвердил/отменил |
| **Schedule** | Расписание доступности ресурса | График работы врача |
| **Slot** | Слот в расписании | Свободное время для записи |
| **ServiceRequest** | Запрос на услугу/исследование | Направление на анализ, консультацию |
| **Task** | Задача/поручение | Назначить анализ, позвонить пациенту |

**5. Financial Resources (Финансовые)**

| Resource | Описание | Использование |
|----------|----------|---------------|
| **Coverage** | Страховое покрытие | Страховой полис пациента |
| **Claim** | Страховое требование | Запрос на оплату услуги |
| **Invoice** | Счет | Выставленный счет |
| **ChargeItem** | Оплачиваемая позиция | Конкретная услуга или товар |

**Связи между Resources:**

FHIR Resources ссылаются друг на друга через поле `reference`:

```
Patient
  ↓
Encounter (ссылка на Patient)
  ↓
Observation (ссылка на Encounter и Patient)
  ↓
DiagnosticReport (ссылка на Observation, Patient, Practitioner)
```

**Пример сети связей для одного визита:**

```
Patient: John Doe (id: patient-123)
  ↓ subject
Encounter: Emergency Visit (id: enc-456)
  ↓ encounter          ↓ participant
Observation: BP        Practitioner: Dr. Smith
  ↓ basedOn
ServiceRequest: Blood Test
  ↓ result
Observation: Hemoglobin Level
  ↓ part of
DiagnosticReport: Complete Blood Count
```

### 3.3 Пример FHIR Patient Resource

Рассмотрим детально структуру Patient Resource:

```json
{
  "resourceType": "Patient",
  "id": "patient-123",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-03-15T10:00:00Z",
    "profile": ["http://hl7.org/fhir/StructureDefinition/Patient"]
  },
  "text": {
    "status": "generated",
    "div": "<div>John Doe, Male, DOB: 1980-01-01</div>"
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
      "value": "123456789",
      "period": {
        "start": "2020-01-01"
      }
    },
    {
      "use": "secondary",
      "type": {
        "coding": [{
          "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
          "code": "SS",
          "display": "Social Security Number"
        }]
      },
      "system": "http://hl7.org/fhir/sid/us-ssn",
      "value": "999-88-7777"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "official",
      "family": "Doe",
      "given": ["John", "Michael"],
      "suffix": ["Jr"],
      "period": {
        "start": "1980-01-01"
      }
    },
    {
      "use": "nickname",
      "given": ["Johnny"]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "555-1234",
      "use": "home",
      "rank": 1
    },
    {
      "system": "phone",
      "value": "555-5678",
      "use": "mobile",
      "rank": 2
    },
    {
      "system": "email",
      "value": "john.doe@example.com",
      "use": "home"
    }
  ],
  "gender": "male",
  "birthDate": "1980-01-01",
  "_birthDate": {
    "extension": [{
      "url": "http://hl7.org/fhir/StructureDefinition/patient-birthTime",
      "valueDateTime": "1980-01-01T08:30:00-05:00"
    }]
  },
  "deceasedBoolean": false,
  "address": [
    {
      "use": "home",
      "type": "physical",
      "line": ["123 Main St", "Apt 4B"],
      "city": "New York",
      "state": "NY",
      "postalCode": "10001",
      "country": "USA",
      "period": {
        "start": "2020-01-01"
      }
    }
  ],
  "maritalStatus": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
      "code": "M",
      "display": "Married"
    }]
  },
  "contact": [
    {
      "relationship": [{
        "coding": [{
          "system": "http://terminology.hl7.org/CodeSystem/v2-0131",
          "code": "N",
          "display": "Next-of-Kin"
        }]
      }],
      "name": {
        "family": "Doe",
        "given": ["Jane"]
      },
      "telecom": [{
        "system": "phone",
        "value": "555-9999"
      }],
      "address": {
        "line": ["123 Main St", "Apt 4B"],
        "city": "New York",
        "state": "NY",
        "postalCode": "10001"
      }
    }
  ],
  "communication": [
    {
      "language": {
        "coding": [{
          "system": "urn:ietf:bcp:47",
          "code": "en-US",
          "display": "English (United States)"
        }]
      },
      "preferred": true
    },
    {
      "language": {
        "coding": [{
          "system": "urn:ietf:bcp:47",
          "code": "es",
          "display": "Spanish"
        }]
      },
      "preferred": false
    }
  ],
  "generalPractitioner": [
    {
      "reference": "Practitioner/pract-456",
      "display": "Dr. Jane Smith"
    }
  ],
  "managingOrganization": {
    "reference": "Organization/org-789",
    "display": "General Hospital"
  }
}
```

**Разбор ключевых полей:**

**resourceType** и **id**
- `resourceType`: всегда "Patient" для пациента
- `id`: уникальный идентификатор в системе (можно использовать в URL)

**meta** (Метаданные)
- `versionId`: версия ресурса (для истории изменений)
- `lastUpdated`: когда последний раз обновлялся
- `profile`: какому профилю соответствует (для валидации)

**identifier** (Идентификаторы)
- Массив идентификаторов (MRN, SSN, паспорт и т.д.)
- `system`: namespace для идентификатора (URL)
- `value`: сам идентификатор
- `use`: official, secondary, temp
- `type`: кодированный тип (MR, SS, DL и т.д.)

**name** (Имена)
- Массив имен (официальное, прозвище, девичья фамилия)
- `use`: official, usual, nickname, maiden
- `family`: фамилия
- `given`: массив имен (имя, отчество)
- `suffix`: массив суффиксов (Jr, Sr, III)
- `period`: период действия имени

**telecom** (Контакты)
- `system`: phone, fax, email, pager, url, sms
- `value`: значение контакта
- `use`: home, work, temp, mobile
- `rank`: приоритет (1 = highest)

**gender** (Пол)
- Значения: male, female, other, unknown
- Административный пол (для записи)

**birthDate** (Дата рождения)
- Формат: YYYY, YYYY-MM, или YYYY-MM-DD
- Можно добавить точное время через extension

**address** (Адреса)
- Массив адресов
- `use`: home, work, temp, old
- `type`: postal, physical, both
- `line`: массив строк адреса
- `city`, `state`, `postalCode`, `country`
- `period`: период действия адреса

**contact** (Контактные лица)
- Родственники, опекуны
- Relationship, имя, контакты, адрес

**generalPractitioner** (Лечащий врач)
- Ссылка на Practitioner resource
- Можно несколько врачей

**managingOrganization** (Управляющая организация)
- Ссылка на Organization
- Организация, которая ведет эту запись пациента

### 3.4 FHIR API Operations

FHIR использует стандартные REST операции для работы с ресурсами.

**CRUD Операции:**

| HTTP Method | Operation | URL | Описание |
|-------------|-----------|-----|----------|
| GET | read | `/Patient/123` | Получить конкретного пациента по ID |
| POST | create | `/Patient` | Создать нового пациента (ID назначит сервер) |
| PUT | update | `/Patient/123` | Обновить пациента (полная замена) |
| PATCH | patch | `/Patient/123` | Частичное обновление |
| DELETE | delete | `/Patient/123` | Удалить пациента |

**Search (Поиск):**

FHIR предоставляет мощные возможности поиска с множеством параметров.

**Поиск по имени:**
```
GET /Patient?name=John
GET /Patient?given=John&family=Doe
```

**Поиск по дате рождения:**
```
GET /Patient?birthdate=1980-01-01
GET /Patient?birthdate=ge1980-01-01    (greater or equal)
GET /Patient?birthdate=lt1990-01-01    (less than)
```

**Поиск по идентификатору:**
```
GET /Patient?identifier=123456789
GET /Patient?identifier=http://hospital.org/patients|123456789
```

**Поиск по полу:**
```
GET /Patient?gender=male
```

**Комбинированный поиск:**
```
GET /Patient?name=Doe&gender=male&birthdate=ge1980-01-01
```

**Сортировка:**
```
GET /Patient?name=John&_sort=birthdate
GET /Patient?name=John&_sort=-birthdate  (descending)
```

**Пагинация:**
```
GET /Patient?_count=20                    (20 results per page)
GET /Patient?_count=20&_offset=40         (skip first 40)
```

**Include (Включение связанных ресурсов):**
```
GET /Observation?patient=123&_include=Observation:patient
   → Вернет Observations и включит Patient resource
   
GET /Encounter?patient=123&_include=Encounter:practitioner
   → Вернет Encounters и включит Practitioners
   
GET /DiagnosticReport?patient=123&_include=DiagnosticReport:result
   → Вернет DiagnosticReports и включит Observations
```

**RevInclude (Обратное включение):**
```
GET /Patient/123?_revinclude=Observation:patient
   → Вернет Patient и все его Observations
   
GET /Patient/123?_revinclude=Encounter:patient
   → Вернет Patient и все его Encounters
```

**Chaining (Цепочки поиска):**
```
GET /Observation?subject.name=John
   → Найти Observations где пациент с именем John
   
GET /DiagnosticReport?result.code=718-7
   → Найти DiagnosticReports с Observations кода 718-7
```

**History (История изменений):**
```
GET /Patient/123/_history              → Вся история пациента
GET /Patient/123/_history/2            → Конкретная версия
GET /Patient/_history                  → История всех пациентов
GET /_history                          → История всех ресурсов
```

**Batch и Transaction:**

```json
POST /
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
        "name": [{"family": "Doe", "given": ["John"]}]
      }
    },
    {
      "request": {
        "method": "POST",
        "url": "Observation"
      },
      "resource": {
        "resourceType": "Observation",
        "subject": {"reference": "Patient/123"},
        "code": {"coding": [{"code": "8480-6"}]},
        "valueQuantity": {"value": 120, "unit": "mmHg"}
      }
    }
  ]
}
```

**Custom Operations:**

FHIR поддерживает кастомные операции через `$operation`:

```
GET /Patient/123/$everything
   → Получить ВСЕ данные пациента (Patient + Encounters + Observations + etc.)
   
POST /Patient/$match
   → Поиск дубликатов пациента
   
POST /Observation/$stats
   → Статистика по наблюдениям
```

### 3.5 Работа с FHIR в Python

Библиотека `fhir.resources` — удобный инструмент для работы с FHIR ресурсами в Python.

**1. Создание Patient Resource:**

```python
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address
from datetime import date

# Создание пациента с полной информацией
patient = Patient(
    identifier=[
        Identifier(
            use="official",
            system="http://hospital.org/patients",
            value="123456789"
        )
    ],
    active=True,
    name=[
        HumanName(
            use="official",
            family="Doe",
            given=["John", "Michael"],
            suffix=["Jr"]
        )
    ],
    telecom=[
        ContactPoint(
            system="phone",
            value="555-1234",
            use="home",
            rank=1
        ),
        ContactPoint(
            system="email",
            value="john.doe@example.com",
            use="home"
        )
    ],
    gender="male",
    birthDate=date(1980, 1, 1),
    address=[
        Address(
            use="home",
            type="physical",
            line=["123 Main St", "Apt 4B"],
            city="New York",
            state="NY",
            postalCode="10001",
            country="USA"
        )
    ]
)

# Конвертация в JSON
patient_json = patient.json()
print(patient_json)

# Конвертация в dict
patient_dict = patient.dict()
```

**2. Отправка на FHIR сервер:**

```python
import requests

FHIR_SERVER = "http://hapi.fhir.org/baseR4"  # Публичный тестовый сервер

def create_patient(patient: Patient):
    """Создает пациента на FHIR сервере"""
    response = requests.post(
        f"{FHIR_SERVER}/Patient",
        json=patient.dict(),
        headers={
            "Content-Type": "application/fhir+json",
            "Accept": "application/fhir+json"
        }
    )
    
    if response.status_code in [200, 201]:
        created_patient = Patient(**response.json())
        print(f"✓ Patient created with ID: {created_patient.id}")
        return created_patient
    else:
        print(f"✗ Error: {response.status_code}")
        print(response.text)
        return None

# Создаем пациента
created_patient = create_patient(patient)
```

**3. Чтение пациента:**

```python
def get_patient(patient_id: str):
    """Получает пациента по ID"""
    response = requests.get(
        f"{FHIR_SERVER}/Patient/{patient_id}",
        headers={"Accept": "application/fhir+json"}
    )
    
    if response.status_code == 200:
        patient = Patient(**response.json())
        return patient
    else:
        print(f"✗ Patient not found: {response.status_code}")
        return None

# Получаем пациента
patient = get_patient("123456")
if patient:
    print(f"Patient: {patient.name[0].given[0]} {patient.name[0].family}")
    print(f"DOB: {patient.birthDate}")
    print(f"Gender: {patient.gender}")
```

**4. Поиск пациентов:**

```python
def search_patients(family_name: str = None, given_name: str = None):
    """Поиск пациентов по имени"""
    params = {}
    if family_name:
        params['family'] = family_name
    if given_name:
        params['given'] = given_name
    
    response = requests.get(
        f"{FHIR_SERVER}/Patient",
        params=params,
        headers={"Accept": "application/fhir+json"}
    )
    
    if response.status_code == 200:
        bundle = response.json()
        
        # Bundle содержит массив entry с результатами
        if 'entry' in bundle:
            patients = []
            for entry in bundle['entry']:
                patient = Patient(**entry['resource'])
                patients.append(patient)
            return patients
        else:
            print("No patients found")
            return []
    else:
        print(f"✗ Search error: {response.status_code}")
        return []

# Поиск всех Doe
patients = search_patients(family_name="Doe")
for patient in patients:
    print(f"Found: {patient.name[0].given[0]} {patient.name[0].family}, ID: {patient.id}")
```

**5. Обновление пациента:**

```python
def update_patient(patient: Patient):
    """Обновляет существующего пациента"""
    if not patient.id:
        print("✗ Patient must have an ID to update")
        return None
    
    response = requests.put(
        f"{FHIR_SERVER}/Patient/{patient.id}",
        json=patient.dict(),
        headers={
            "Content-Type": "application/fhir+json",
            "Accept": "application/fhir+json"
        }
    )
    
    if response.status_code == 200:
        updated_patient = Patient(**response.json())
        print(f"✓ Patient updated: {updated_patient.id}")
        return updated_patient
    else:
        print(f"✗ Update error: {response.status_code}")
        return None

# Получаем пациента
patient = get_patient("123456")

# Обновляем телефон
patient.telecom[0].value = "555-9999"

# Сохраняем
update_patient(patient)
```

**6. Работа с Observation:**

```python
from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.quantity import Quantity
from fhir.resources.reference import Reference
from datetime import datetime

def create_blood_pressure_observation(patient_id: str, systolic: int, diastolic: int):
    """Создает наблюдение артериального давления"""
    
    observation = Observation(
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
                    code="85354-9",
                    display="Blood pressure panel"
                )
            ]
        ),
        subject=Reference(reference=f"Patient/{patient_id}"),
        effectiveDateTime=datetime.now(),
        component=[
            {
                "code": CodeableConcept(
                    coding=[
                        Coding(
                            system="http://loinc.org",
                            code="8480-6",
                            display="Systolic blood pressure"
                        )
                    ]
                ),
                "valueQuantity": Quantity(
                    value=systolic,
                    unit="mmHg",
                    system="http://unitsofmeasure.org",
                    code="mm[Hg]"
                )
            },
            {
                "code": CodeableConcept(
                    coding=[
                        Coding(
                            system="http://loinc.org",
                            code="8462-4",
                            display="Diastolic blood pressure"
                        )
                    ]
                ),
                "valueQuantity": Quantity(
                    value=diastolic,
                    unit="mmHg",
                    system="http://unitsofmeasure.org",
                    code="mm[Hg]"
                )
            }
        ]
    )
    
    # Отправляем на сервер
    response = requests.post(
        f"{FHIR_SERVER}/Observation",
        json=observation.dict(),
        headers={"Content-Type": "application/fhir+json"}
    )
    
    if response.status_code in [200, 201]:
        print(f"✓ Observation created: BP {systolic}/{diastolic}")
        return Observation(**response.json())
    else:
        print(f"✗ Error: {response.status_code}")
        return None

# Создаем observation
bp_obs = create_blood_pressure_observation("123456", 120, 80)
```

**7. Получение всех данных пациента:**

```python
def get_patient_everything(patient_id: str):
    """Получает все данные пациента используя $everything операцию"""
    response = requests.get(
        f"{FHIR_SERVER}/Patient/{patient_id}/$everything",
        headers={"Accept": "application/fhir+json"}
    )
    
    if response.status_code == 200:
        bundle = response.json()
        
        # Анализируем bundle
        print(f"Total resources: {bundle.get('total', 0)}")
        
        if 'entry' in bundle:
            resource_types = {}
            for entry in bundle['entry']:
                resource_type = entry['resource']['resourceType']
                resource_types[resource_type] = resource_types.get(resource_type, 0) + 1
            
            print("\nResources by type:")
            for resource_type, count in resource_types.items():
                print(f"  {resource_type}: {count}")
        
        return bundle
    else:
        print(f"✗ Error: {response.status_code}")
        return None

# Получаем все данные
everything = get_patient_everything("123456")
```

**8. Класс FHIR Client (обертка):**

```python
class FHIRClient:
    """Удобная обертка для работы с FHIR сервером"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/fhir+json",
            "Content-Type": "application/fhir+json"
        })
    
    def create(self, resource):
        """Создает ресурс"""
        resource_type = resource.resource_type
        response = self.session.post(
            f"{self.base_url}/{resource_type}",
            json=resource.dict()
        )
        response.raise_for_status()
        return type(resource)(**response.json())
    
    def read(self, resource_type: str, resource_id: str):
        """Читает ресурс"""
        response = self.session.get(
            f"{self.base_url}/{resource_type}/{resource_id}"
        )
        response.raise_for_status()
        
        # Динамически импортируем класс
        from fhir.resources import get_fhir_model_class
        ResourceClass = get_fhir_model_class(resource_type)
        return ResourceClass(**response.json())
    
    def update(self, resource):
        """Обновляет ресурс"""
        resource_type = resource.resource_type
        response = self.session.put(
            f"{self.base_url}/{resource_type}/{resource.id}",
            json=resource.dict()
        )
        response.raise_for_status()
        return type(resource)(**response.json())
    
    def delete(self, resource_type: str, resource_id: str):
        """Удаляет ресурс"""
        response = self.session.delete(
            f"{self.base_url}/{resource_type}/{resource_id}"
        )
        response.raise_for_status()
    
    def search(self, resource_type: str, **params):
        """Поиск ресурсов"""
        response = self.session.get(
            f"{self.base_url}/{resource_type}",
            params=params
        )
        response.raise_for_status()
        return response.json()

# Использование
client = FHIRClient("http://hapi.fhir.org/baseR4")

# Создание
patient = client.create(patient)

# Чтение
patient = client.read("Patient", "123456")

# Обновление
patient.name[0].given = ["Jane"]
patient = client.update(patient)

# Поиск
bundle = client.search("Patient", family="Doe", gender="female")
```

---

## 4. Другие Важные Стандарты

### 4.1 DICOM — Digital Imaging and Communications in Medicine

Стандарт для медицинских изображений.

```
DICOM файл содержит:

- Изображение (пиксельные данные)
- Метаданные (имя пациента, дата, тип снимка, оборудование)
```

### 4.2 ICD-10 — International Classification of Diseases

**ICD-10** — Международная классификация болезней, 10-я ревизия. Это стандартная система кодирования диагнозов, используемая по всему миру.

**История:**
- ICD-1 (1900) — 44 страницы
- ICD-10 (1990, внедрена в 1994-2015 в разных странах) — ~14,000 кодов
- ICD-11 (2022) — новейшая версия

**В USA используется ICD-10-CM (Clinical Modification):**
- ~70,000 кодов (значительно больше базовой ICD-10)
- Обязателен с October 1, 2015
- Для процедур используется ICD-10-PCS (Procedure Coding System)

**Структура кода ICD-10:**

```
E 11 . 65
↑ ↑↑  ↑↑
│ └──┴─ Детализация
└────── Категория (буква)

E     = Endocrine, nutritional and metabolic diseases (E00-E89)
11    = Type 2 diabetes mellitus
.65   = with hyperglycemia
```

**Примеры кодов с детальным разбором:**

**Сердечно-сосудистые заболевания (I00-I99):**

| Код | Диагноз | Детали |
|-----|---------|--------|
| I21.0 | Acute myocardial infarction | Инфаркт миокарда передней стенки |
| I21.1 | Acute myocardial infarction | Инфаркт нижней стенки |
| I21.9 | Acute myocardial infarction | Инфаркт неуточненной локализации |
| I10 | Essential (primary) hypertension | Эссенциальная гипертензия |
| I50.9 | Heart failure, unspecified | Сердечная недостаточность |

**Эндокринные заболевания (E00-E89):**

| Код | Диагноз | Детали |
|-----|---------|--------|
| E11.9 | Type 2 diabetes mellitus without complications | Диабет 2 типа без осложнений |
| E11.65 | Type 2 diabetes mellitus with hyperglycemia | Диабет 2 типа с гипергликемией |
| E11.21 | Type 2 diabetes mellitus with diabetic nephropathy | С поражением почек |
| E11.36 | Type 2 diabetes mellitus with diabetic cataract | С катарактой |
| E10.9 | Type 1 diabetes mellitus without complications | Диабет 1 типа |

**Респираторные заболевания (J00-J99):**

| Код | Диагноз | Детали |
|-----|---------|--------|
| J44.0 | COPD with acute lower respiratory infection | ХОБЛ с инфекцией |
| J44.1 | COPD with acute exacerbation | ХОБЛ с обострением |
| J44.9 | COPD, unspecified | ХОБЛ неуточненная |
| J18.9 | Pneumonia, unspecified organism | Пневмония неуточненная |
| J45.0 | Allergic (predominantly) asthma | Аллергическая астма |

**Травмы (S00-T88):**

| Код | Диагноз | Детали |
|-----|---------|--------|
| S72.001A | Fracture of unspecified part of neck of right femur, initial encounter | Перелом шейки бедра справа, первичный |
| S72.001D | Fracture of unspecified part of neck of right femur, subsequent encounter | Перелом шейки бедра справа, последующий визит |
| S72.001S | Fracture of unspecified part of neck of right femur, sequela | Перелом шейки бедра справа, последствия |

**Латеральность (Laterality):**
- 1 = Right (правый)
- 2 = Left (левый)
- 3 = Bilateral (двусторонний)
- 9 = Unspecified (неуточненный)

**7th Character (7-й символ для травм):**
- A = Initial encounter (первичное обращение)
- D = Subsequent encounter (последующее наблюдение)
- S = Sequela (последствия, отдаленные эффекты)

**Использование ICD-10:**

**1. Billing (Выставление счетов):**
```python
diagnosis_codes = ["E11.9", "I10", "E78.5"]
# Эти коды определяют, что будет оплачено страховкой
# E11.9 = Diabetes Type 2
# I10 = Hypertension
# E78.5 = Hyperlipidemia
```

**2. Статистика и исследования:**
```python
# Сколько пациентов с диабетом в больнице?
diabetes_codes = ["E10.*", "E11.*", "E13.*", "E14.*"]
# * означает все подкоды (E11.0, E11.1, E11.9 и т.д.)
```

**3. Clinical Decision Support:**
```python
def check_drug_interaction(patient_diagnoses, medication):
    """Проверка взаимодействия лекарства с диагнозами"""
    
    # Если у пациента диабет (E10-E14), нужно быть осторожным с кортикостероидами
    diabetes_codes = [code for code in patient_diagnoses if code.startswith('E1')]
    
    if diabetes_codes and medication == "Prednisone":
        return "WARNING: Corticosteroids can increase blood sugar"
    
    return "OK"
```

**Работа с ICD-10 в Python:**

```python
def parse_icd10_code(code: str):
    """Разбор ICD-10 кода"""
    
    # Удаляем точку если есть
    clean_code = code.replace('.', '')
    
    # Первый символ — категория (буква)
    category_letter = clean_code[0]
    
    # Следующие 2-3 цифры — основная категория
    if len(clean_code) >= 3:
        main_category = clean_code[1:3]
    else:
        main_category = None
    
    # Остальное — детализация
    if len(clean_code) > 3:
        subcategory = clean_code[3:]
    else:
        subcategory = None
    
    return {
        'category': category_letter,
        'main': main_category,
        'sub': subcategory,
        'original': code
    }

# Пример
code_info = parse_icd10_code("E11.65")
print(code_info)
# {'category': 'E', 'main': '11', 'sub': '65', 'original': 'E11.65'}

def match_icd10_pattern(code: str, pattern: str):
    """Проверка соответствия паттерну (с *)"""
    
    # Преобразуем паттерн в regex
    import re
    regex_pattern = pattern.replace('.', '\\.').replace('*', '.*')
    return bool(re.match(f"^{regex_pattern}$", code))

# Примеры
print(match_icd10_pattern("E11.65", "E11.*"))   # True
print(match_icd10_pattern("E11.65", "E1*"))     # True
print(match_icd10_pattern("E11.65", "I*"))      # False
```

### 4.3 SNOMED CT — Systematized Nomenclature of Medicine

**SNOMED CT** — самая комплексная и точная клиническая терминология в здравоохранении.

**Масштаб:**
- ~350,000+ активных концепций (concepts)
- ~1,000,000+ описаний (descriptions)
- ~1,500,000+ отношений (relationships)
- Обновляется дважды в год

**Что такое SNOMED CT?**

SNOMED CT — это не просто список кодов, это **онтология** — система с иерархическими отношениями между концепциями.

**Основные концепции (Top-level hierarchies):**

| Hierarchy | Примеры | Количество концепций |
|-----------|---------|---------------------|
| **Clinical finding** | Diseases, symptoms, signs | ~130,000 |
| **Procedure** | Surgeries, diagnostics | ~65,000 |
| **Body structure** | Anatomical parts | ~35,000 |
| **Organism** | Bacteria, viruses | ~35,000 |
| **Substance** | Drugs, chemicals | ~30,000 |
| **Pharmaceutical product** | Medications | ~20,000 |
| **Specimen** | Blood, tissue samples | ~2,000 |
| **Observable entity** | Measurements, assessments | ~7,000 |

**Структура кода:**

```
73211009  → Diabetes mellitus
↑↑↑↑↑↑↑↑
8-18 цифр (SCTID - SNOMED CT Identifier)
```

**Примеры с иерархией:**

```
Disease (64572001)
  ↓
  Endocrine disease (362969004)
    ↓
    Diabetes mellitus (73211009)
      ↓ is-a
      ├─ Type 1 diabetes mellitus (46635009)
      ├─ Type 2 diabetes mellitus (44054006)
      └─ Gestational diabetes mellitus (11687002)
```

**Отношения (Relationships):**

SNOMED CT использует отношения для связи концепций:

| Relationship | Описание | Пример |
|--------------|----------|--------|
| **is-a** | Иерархия | "Type 2 diabetes" is-a "Diabetes mellitus" |
| **finding-site** | Место находки | "Pneumonia" finding-site "Lung structure" |
| **causative-agent** | Причинный агент | "Pneumonia" causative-agent "Streptococcus pneumoniae" |
| **associated-morphology** | Морфология | "Myocardial infarction" associated-morphology "Infarct" |
| **procedure-site** | Место процедуры | "Appendectomy" procedure-site "Appendix" |

**Примеры кодов:**

**Clinical Findings (Клинические находки):**

| SCTID | Термин | FSN (Fully Specified Name) |
|-------|--------|----------------------------|
| 73211009 | Diabetes mellitus | Diabetes mellitus (disorder) |
| 44054006 | Type 2 diabetes mellitus | Type 2 diabetes mellitus (disorder) |
| 38341003 | Hypertensive disorder | Hypertensive disorder, systemic arterial (disorder) |
| 22298006 | Myocardial infarction | Myocardial infarction (disorder) |
| 233604007 | Pneumonia | Pneumonia (disorder) |

**Body Structures (Структуры тела):**

| SCTID | Термин | FSN |
|-------|--------|-----|
| 80891009 | Heart | Heart structure (body structure) |
| 39607008 | Lung | Lung structure (body structure) |
| 181414000 | Kidney | Kidney structure (body structure) |
| 181261002 | Stomach | Stomach structure (body structure) |

**Procedures (Процедуры):**

| SCTID | Термин | FSN |
|-------|--------|-----|
| 80146002 | Appendectomy | Excision of appendix (procedure) |
| 232717009 | Coronary artery bypass | Coronary artery bypass grafting (procedure) |
| 71388002 | Hip replacement | Total hip replacement (procedure) |

**Использование SNOMED CT:**

**1. Точное клиническое описание:**
```python
# В FHIR Condition resource
condition = {
    "code": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "44054006",
            "display": "Type 2 diabetes mellitus"
        }]
    },
    "bodySite": [{
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "181414000",
            "display": "Kidney structure"
        }]
    }]
}
```

**2. Поиск по иерархии:**
```python
def is_type_of_diabetes(snomed_code: str, diabetes_types: set):
    """Проверка, является ли код типом диабета"""
    # В реальности нужен доступ к SNOMED CT терминологическому серверу
    # Это упрощенный пример
    
    diabetes_hierarchy = {
        "73211009": "Diabetes mellitus",
        "44054006": "Type 2 diabetes mellitus",  # child of 73211009
        "46635009": "Type 1 diabetes mellitus",  # child of 73211009
        "11687002": "Gestational diabetes"       # child of 73211009
    }
    
    # Проверяем, является ли код диабетом или его подтипом
    return snomed_code in diabetes_hierarchy

# Использование
if is_type_of_diabetes("44054006", diabetes_types):
    print("This is a type of diabetes")
```

**3. Mappin g с ICD-10:**
```python
# SNOMED CT имеет официальные маппинги с ICD-10
snomed_to_icd10 = {
    "44054006": "E11.9",  # Type 2 DM → E11.9
    "38341003": "I10",     # Hypertension → I10
    "22298006": "I21.9"    # MI → I21.9
}
```

### 4.4 LOINC — Logical Observation Identifiers Names and Codes

**LOINC** — универсальная система кодирования лабораторных и клинических наблюдений.

**Масштаб:**
- ~94,000 кодов (2024)
- Включает: лабораторные тесты, vital signs, клинические документы, опросники
- Используется в >190 странах

**Зачем нужен LOINC?**

Проблема: одно и то же исследование имеет разные названия:

- "Hemoglobin"
- "Hgb"
- "Hb"
- "Hemoglobin, Blood"

LOINC решает это, давая уникальный код: **718-7**

**Структура кода:**

```
718-7
↑↑↑↑↑
Numeric code + check digit
```

**6 частей имени LOINC (LOINC Name Structure):**

```
Component - Property - Timing - System - Scale - Method

Hemoglobin - MCnc - Pt - Bld - Qn - Automated count
     ↑          ↑      ↑    ↑    ↑         ↑
  Что        Свойство Когда Где  Тип     Метод
```

| Part | Description | Examples |
|------|-------------|----------|
| **Component** | Что измеряем | Hemoglobin, Glucose, Creatinine |
| **Property** | Какое свойство | MCnc (mass concentration), CCnc (catalytic concentration) |
| **Timing** | Когда | Pt (point in time), 24H (24 hours) |
| **System** | Где/Образец | Bld (blood), Ur (urine), Ser (serum) |
| **Scale** | Тип результата | Qn (quantitative), Ord (ordinal), Nom (nominal) |
| **Method** | Метод | Automated, Manual, HPLC |

**Примеры кодов:**

**Laboratory Tests (Лабораторные анализы):**

| LOINC | Short Name | Full Name | Ref Range (example) |
|-------|------------|-----------|---------------------|
| 718-7 | Hemoglobin | Hemoglobin [Mass/volume] in Blood | 13.5-17.5 g/dL (male) |
| 2345-7 | Glucose | Glucose [Mass/volume] in Serum or Plasma | 70-100 mg/dL (fasting) |
| 2160-0 | Creatinine | Creatinine [Mass/volume] in Serum or Plasma | 0.7-1.3 mg/dL |
| 2951-2 | Sodium | Sodium [Moles/volume] in Serum or Plasma | 136-145 mmol/L |
| 2823-3 | Potassium | Potassium [Moles/volume] in Serum or Plasma | 3.5-5.0 mmol/L |

**Vital Signs:**

| LOINC | Short Name | Full Name | Typical Range |
|-------|------------|-----------|---------------|
| 8480-6 | Systolic BP | Systolic blood pressure | 90-120 mmHg |
| 8462-4 | Diastolic BP | Diastolic blood pressure | 60-80 mmHg |
| 8867-4 | Heart rate | Heart rate | 60-100 /min |
| 8310-5 | Body temperature | Body temperature | 36.5-37.5 °C |
| 2708-6 | Oxygen saturation | Oxygen saturation in Arterial blood | 95-100 % |
| 29463-7 | Body weight | Body weight | varies |
| 8302-2 | Body height | Body height | varies |

**Clinical Documents:**

| LOINC | Document Type |
|-------|---------------|
| 11488-4 | Consultation note |
| 18842-5 | Discharge summary |
| 34117-2 | History and physical note |
| 11506-3 | Progress note |

**Работа с LOINC в Python:**

```python
def parse_observation_with_loinc(observation_data):
    """Разбор наблюдения с LOINC кодом"""
    
    loinc_definitions = {
        "718-7": {
            "name": "Hemoglobin",
            "unit": "g/dL",
            "ref_range": {"male": (13.5, 17.5), "female": (12.0, 15.5)},
            "type": "quantitative"
        },
        "8480-6": {
            "name": "Systolic BP",
            "unit": "mmHg",
            "ref_range": (90, 120),
            "type": "quantitative"
        },
        "2345-7": {
            "name": "Glucose",
            "unit": "mg/dL",
            "ref_range": (70, 100),  # fasting
            "type": "quantitative"
        }
    }
    
    loinc_code = observation_data.get("code")
    value = observation_data.get("value")
    patient_gender = observation_data.get("patient_gender")
    
    if loinc_code not in loinc_definitions:
        return {"error": "Unknown LOINC code"}
    
    definition = loinc_definitions[loinc_code]
    
    # Определяем референсный диапазон
    ref_range = definition["ref_range"]
    if isinstance(ref_range, dict):  # gender-specific
        ref_range = ref_range.get(patient_gender, ref_range["male"])
    
    # Проверяем, в норме ли значение
    if definition["type"] == "quantitative":
        if value < ref_range[0]:
            flag = "L"  # Low
        elif value > ref_range[1]:
            flag = "H"  # High
        else:
            flag = "N"  # Normal
    else:
        flag = "N"
    
    return {
        "loinc": loinc_code,
        "name": definition["name"],
        "value": value,
        "unit": definition["unit"],
        "ref_range": ref_range,
        "flag": flag
    }

# Пример использования
result = parse_observation_with_loinc({
    "code": "718-7",
    "value": 14.5,
    "patient_gender": "male"
})

print(f"{result['name']}: {result['value']} {result['unit']}")
print(f"Reference range: {result['ref_range'][0]}-{result['ref_range'][1]}")
print(f"Flag: {result['flag']}")
# Output:
# Hemoglobin: 14.5 g/dL
# Reference range: 13.5-17.5
# Flag: N
```

**LOINC в FHIR:**

```python
from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding

# Создание Observation с LOINC кодом
observation = Observation(
    status="final",
    code=CodeableConcept(
        coding=[
            Coding(
                system="http://loinc.org",
                code="718-7",
                display="Hemoglobin [Mass/volume] in Blood"
            )
        ]
    ),
    valueQuantity={
        "value": 14.5,
        "unit": "g/dL",
        "system": "http://unitsofmeasure.org",
        "code": "g/dL"
    }
)
```

---

## 5. Interoperability в Healthcare

### 5.1 Уровни интероперабельности

```
Technical      → Физическая передача данных (TCP/IP)
    ↓
Syntactic      → Формат данных (HL7, FHIR)
    ↓
Semantic       → Значение данных (SNOMED, LOINC)
    ↓
Organizational → Workflow, политики
```

### 5.2 Health Information Exchange (HIE)

Обмен медицинской информацией между организациями.

**Модели:**
- **Centralized** — единая база данных
- **Federated** — запросы к распределённым системам
- **Hybrid** — комбинация

---

## 6. Практические Сценарии

### 6.1 Сценарий: Амбулаторный визит пациента

**Задача:** Реализовать полный цикл амбулаторного визита

**Шаги:**

1. **Регистрация пациента (если новый)**
2. **Создание записи на прием (Appointment)**
3. **Создание Encounter (визит)**
4. **Измерение vital signs (Observation)**
5. **Назначение анализов (ServiceRequest)**
6. **Получение результатов (Observation)**
7. **Постановка диагноза (Condition)**
8. **Назначение лекарств (MedicationRequest)**

**Реализация в FHIR:**

```python
from fhir.resources.patient import Patient
from fhir.resources.appointment import Appointment
from fhir.resources.encounter import Encounter
from fhir.resources.observation import Observation
from fhir.resources.servicerequest import ServiceRequest
from fhir.resources.condition import Condition
from fhir.resources.medicationrequest import MedicationRequest
from datetime import datetime

# 1. Создаем пациента (если нужно)
patient = Patient(
    identifier=[{"system": "http://hospital.org", "value": "MRN-123456"}],
    name=[{"family": "Smith", "given": ["John"]}],
    gender="male",
    birthDate="1975-05-15"
)
patient_id = "patient-123"  # После создания на сервере

# 2. Создаем запись на прием
appointment = Appointment(
    status="booked",
    serviceType=[{"text": "General Practice"}],
    start=datetime(2024, 3, 15, 10, 0),
    end=datetime(2024, 3, 15, 10, 30),
    participant=[
        {
            "actor": {"reference": f"Patient/{patient_id}"},
            "status": "accepted"
        },
        {
            "actor": {"reference": "Practitioner/doc-456"},
            "status": "accepted"
        }
    ]
)

# 3. Создаем Encounter (визит состоялся)
encounter = Encounter(
    status="finished",
    class_fhir={"code": "AMB", "display": "ambulatory"},
    subject={"reference": f"Patient/{patient_id}"},
    participant=[{
        "individual": {"reference": "Practitioner/doc-456"}
    }],
    period={
        "start": "2024-03-15T10:00:00Z",
        "end": "2024-03-15T10:30:00Z"
    }
)
encounter_id = "encounter-789"

# 4. Измеряем vital signs
bp_observation = Observation(
    status="final",
    category=[{"coding": [{"code": "vital-signs"}]}],
    code={"coding": [{"system": "http://loinc.org", "code": "85354-9"}]},
    subject={"reference": f"Patient/{patient_id}"},
    encounter={"reference": f"Encounter/{encounter_id}"},
    effectiveDateTime=datetime.now(),
    component=[
        {
            "code": {"coding": [{"system": "http://loinc.org", "code": "8480-6"}]},
            "valueQuantity": {"value": 145, "unit": "mmHg"}  # Повышенное!
        },
        {
            "code": {"coding": [{"system": "http://loinc.org", "code": "8462-4"}]},
            "valueQuantity": {"value": 95, "unit": "mmHg"}  # Повышенное!
        }
    ]
)

# 5. Врач видит повышенное давление, назначает анализы
lab_request = ServiceRequest(
    status="active",
    intent="order",
    code={"coding": [{"system": "http://loinc.org", "code": "24323-8", "display": "Comprehensive metabolic panel"}]},
    subject={"reference": f"Patient/{patient_id}"},
    encounter={"reference": f"Encounter/{encounter_id}"},
    authoredOn=datetime.now()
)

# 6. Через день приходят результаты анализов
glucose_observation = Observation(
    status="final",
    category=[{"coding": [{"code": "laboratory"}]}],
    code={"coding": [{"system": "http://loinc.org", "code": "2345-7", "display": "Glucose"}]},
    subject={"reference": f"Patient/{patient_id}"},
    valueQuantity={"value": 145, "unit": "mg/dL"},  # Elevated!
    referenceRange=[{"low": {"value": 70}, "high": {"value": 100}}]
)

# 7. На основе данных врач ставит диагноз
hypertension_condition = Condition(
    clinicalStatus={"coding": [{"code": "active"}]},
    verificationStatus={"coding": [{"code": "confirmed"}]},
    category=[{"coding": [{"code": "encounter-diagnosis"}]}],
    code={"coding": [
        {"system": "http://snomed.info/sct", "code": "38341003", "display": "Hypertension"},
        {"system": "http://hl7.org/fhir/sid/icd-10", "code": "I10"}
    ]},
    subject={"reference": f"Patient/{patient_id}"},
    onsetDateTime="2024-03-15"
)

diabetes_condition = Condition(
    clinicalStatus={"coding": [{"code": "active"}]},
    verificationStatus={"coding": [{"code": "provisional"}]},  # Требует подтверждения
    code={"coding": [
        {"system": "http://snomed.info/sct", "code": "44054006"},
        {"system": "http://hl7.org/fhir/sid/icd-10", "code": "E11.9"}
    ]},
    subject={"reference": f"Patient/{patient_id}"}
)

# 8. Назначаем лекарства
medication_request = MedicationRequest(
    status="active",
    intent="order",
    medicationCodeableConcept={"text": "Lisinopril 10mg"},
    subject={"reference": f"Patient/{patient_id}"},
    dosageInstruction=[{
        "text": "Take 1 tablet by mouth daily",
        "timing": {"repeat": {"frequency": 1, "period": 1, "periodUnit": "d"}},
        "doseAndRate": [{"doseQuantity": {"value": 10, "unit": "mg"}}]
    }]
)
```

### 6.2 Сценарий: Интеграция с лабораторной системой (HL7 v2 → FHIR)

**Задача:** Получить результаты анализов из лабораторной системы по HL7 v2, преобразовать в FHIR

```python
import hl7
from fhir.resources.observation import Observation
from fhir.resources.diagnosticreport import DiagnosticReport

# 1. Получаем HL7 v2 сообщение от лаборатории
hl7_message = """MSH|^~\\&|LAB|HOSPITAL|EMR|HOSPITAL|20240315143000||ORU^R01|LAB001|P|2.5
PID|1||MRN-123456||Smith^John||19750515|M
OBR|1||LAB-2024-001|CBC^Complete Blood Count|||20240315140000
OBX|1|NM|718-7^Hemoglobin^LN||14.5|g/dL|13.5-17.5|N|||F
OBX|2|NM|787-2^WBC^LN||8.5|10*9/L|4.0-11.0|N|||F
OBX|3|NM|777-3^Platelets^LN||250|10*9/L|150-400|N|||F"""

# 2. Парсим HL7
message = hl7.parse(hl7_message)
pid = message.segment('PID')
obr = message.segment('OBR')
obx_segments = [seg for seg in message if seg[0] == 'OBX']

# 3. Создаем FHIR Observations
observations = []
for obx in obx_segments:
    loinc_code = str(obx[3][0])
    loinc_display = str(obx[3][1])
    value = float(str(obx[5]))
    unit = str(obx[6])
    ref_range = str(obx[7])
    abnormal_flag = str(obx[8])
    
    obs = Observation(
        status="final",
        code={"coding": [{"system": "http://loinc.org", "code": loinc_code, "display": loinc_display}]},
        subject={"reference": "Patient/patient-123"},
        valueQuantity={"value": value, "unit": unit},
        interpretation=[{"coding": [{"code": abnormal_flag}]}] if abnormal_flag != "N" else None
    )
    observations.append(obs)

# 4. Создаем DiagnosticReport
diagnostic_report = DiagnosticReport(
    status="final",
    code={"coding": [{"system": "http://loinc.org", "code": str(obr[4][0])}]},
    subject={"reference": "Patient/patient-123"},
    result=[{"reference": f"Observation/{obs.id}"} for obs in observations]
)
```

### 6.3 Сценарий: Проверка drug-drug interactions

```python
def check_drug_interactions(current_medications, new_medication):
    """Проверка взаимодействия лекарств"""
    
    # Упрощенная база взаимодействий
    interactions = {
        ("Warfarin", "Aspirin"): {
            "severity": "high",
            "effect": "Increased bleeding risk"
        },
        ("Simvastatin", "Amlodipine"): {
            "severity": "moderate",
            "effect": "Increased risk of myopathy"
        },
        ("Metformin", "Contrast dye"): {
            "severity": "high",
            "effect": "Risk of lactic acidosis"
        }
    }
    
    warnings = []
    for current_med in current_medications:
        key = tuple(sorted([current_med, new_medication]))
        if key in interactions:
            warnings.append({
                "medications": key,
                "severity": interactions[key]["severity"],
                "effect": interactions[key]["effect"]
            })
    
    return warnings

# Использование
current_meds = ["Warfarin", "Lisinopril"]
new_med = "Aspirin"

warnings = check_drug_interactions(current_meds, new_med)
if warnings:
    print("⚠️ WARNINGS:")
    for w in warnings:
        print(f"  {w['severity'].upper()}: {w['medications']} - {w['effect']}")
```

---

## 7. Частые Ошибки и Как Их Избежать

### 7.1 Ошибки в HL7 v2

**1. Неправильная обработка escape-последовательностей**

❌ **Неправильно:**
```python
name = str(pid[5])  # "Doe^John\S\Smith"  → неправильно
```

✅ **Правильно:**
```python
def unescape_hl7(text):
    """Обработка escape-последовательностей"""
    return (text
        .replace('\\F\\', '|')
        .replace('\\S\\', '^')
        .replace('\\T\\', '&')
        .replace('\\R\\', '~')
        .replace('\\E\\', '\\'))

name = unescape_hl7(str(pid[5]))
```

**2. Игнорирование пустых полей**

❌ **Неправильно:**
```python
middle_name = str(pid[5][2])  # Может быть пустым → ""
if middle_name:  # Но "" это False!
    print(middle_name)
```

✅ **Правильно:**
```python
middle_name = str(pid[5][2]) if len(pid[5]) > 2 else None
if middle_name is not None and middle_name:
    print(middle_name)
```

**3. Предположение о версии HL7**

❌ **Неправильно:**
```python
# Предполагаем, что всегда 2.5
```

✅ **Правильно:**
```python
msh = message.segment('MSH')
version = str(msh[12])
print(f"HL7 version: {version}")  # Может быть 2.3, 2.4, 2.5...

# Адаптируем логику под версию
if version == "2.3":
    # В 2.3 некоторые поля в других позициях
    pass
```

### 7.2 Ошибки в FHIR

**1. Неправильные references**

❌ **Неправильно:**
```python
observation = Observation(
    subject="patient-123"  # Неправильный формат!
)
```

✅ **Правильно:**
```python
observation = Observation(
    subject={"reference": "Patient/patient-123"}
)
```

**2. Забывают обязательные поля**

❌ **Неправильно:**
```python
observation = Observation(
    code={"coding": [{"code": "718-7"}]},
    valueQuantity={"value": 14.5}
)
# Нет status! Обязательное поле
```

✅ **Правильно:**
```python
observation = Observation(
    status="final",  # Обязательно!
    code={"coding": [{"code": "718-7"}]},
    valueQuantity={"value": 14.5}
)
```

**3. Неправильная работа с датами**

❌ **Неправильно:**
```python
patient = Patient(
    birthDate="15/03/1980"  # Неправильный формат!
)
```

✅ **Правильно:**
```python
from datetime import date

patient = Patient(
    birthDate=date(1980, 3, 15)  # или "1980-03-15"
)
```

### 7.3 Ошибки с кодами

**1. Смешивание систем кодирования**

❌ **Неправильно:**
```python
condition = Condition(
    code={"coding": [
        {"system": "http://snomed.info/sct", "code": "E11.9"}  # Это ICD-10 код!
    ]}
)
```

✅ **Правильно:**
```python
condition = Condition(
    code={"coding": [
        {"system": "http://snomed.info/sct", "code": "44054006"},
        {"system": "http://hl7.org/fhir/sid/icd-10", "code": "E11.9"}
    ]}
)
```

**2. Игнорирование версий кодовых систем**

❌ **Неправильно:**
```python
# ICD-10 или ICD-10-CM? Разные коды!
```

✅ **Правильно:**
```python
# Явно указываем систему
{"system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "E11.65"}
```

### 7.4 Проблемы производительности

**1. N+1 запросы**

❌ **Неправильно:**
```python
# Получаем пациентов
patients = search_patients(family="Smith")

# Для каждого получаем observations (N запросов!)
for patient in patients:
    observations = get_observations(patient.id)
```

✅ **Правильно:**
```python
# Используем _include для одного запроса
response = requests.get(
    f"{FHIR_SERVER}/Patient?family=Smith&_revinclude=Observation:patient"
)
# Получаем пациентов И observations в одном запросе!
```

**2. Не используют пагинацию**

❌ **Неправильно:**
```python
# Пытаемся получить все 10,000 пациентов сразу
patients = search_patients()  # Timeout!
```

✅ **Правильно:**
```python
def get_all_patients():
    """Получение всех пациентов с пагинацией"""
    all_patients = []
    url = f"{FHIR_SERVER}/Patient?_count=100"
    
    while url:
        response = requests.get(url)
        bundle = response.json()
        
        # Добавляем пациентов из текущей страницы
        if 'entry' in bundle:
            for entry in bundle['entry']:
                all_patients.append(Patient(**entry['resource']))
        
        # Ищем ссылку на следующую страницу
        url = None
        if 'link' in bundle:
            for link in bundle['link']:
                if link.get('relation') == 'next':
                    url = link['url']
                    break
    
    return all_patients
```

---

## Резюме

- ✅ Базовая медицинская терминология
- ✅ HL7 v2 — legacy, pipe-delimited формат
- ✅ FHIR — современный REST/JSON стандарт
- ✅ DICOM — медицинские изображения
- ✅ ICD-10, SNOMED CT, LOINC — классификаторы и кодировки
- ✅ Interoperability — критически важна в healthcare

---

## 🚀 Следующие Шаги

**Связанные модули:**
- [EHR Systems](../02_EHR_Systems/) — системы электронных медицинских записей
- [Security & Privacy](../03_Security_Privacy/) — HIPAA, GDPR и безопасность данных
- [Medical Imaging](../04_Medical_Imaging/) — DICOM и обработка изображений

**Идеи для практики:**
1. **HL7 v2 Parser** — парсинг сообщения, извлечение Patient ID, Name, DOB, Gender
2. **FHIR Patient Resource** — создание ресурса с identifier, name, gender, birthDate, address
3. **FHIR API Client** — CRUD операции с FHIR сервером (POST/GET/PUT Patient)
4. **HL7 to FHIR Converter** — конвертация ADT сообщения в FHIR Patient
5. **FHIR Observation** — создание Blood Pressure observation с LOINC кодами

---

## 📚 Дополнительные Ресурсы

**Стандарты HL7:**
- [HL7 International](https://www.hl7.org/) — официальный сайт HL7
- [FHIR Specification](https://www.hl7.org/fhir/) — полная спецификация FHIR
- [FHIR Tutorial](https://www.hl7.org/fhir/overview.html) — введение в FHIR

**Python библиотеки:**
- [python-hl7](https://python-hl7.readthedocs.io/) — парсинг HL7 v2 сообщений
- [fhir.resources](https://pypi.org/project/fhir.resources/) — Python FHIR models
- [HAPI FHIR](https://hapifhir.io/) — open source FHIR сервер

**Классификаторы:**
- [ICD-10](https://www.icd10data.com/) — база ICD-10 кодов
- [SNOMED CT](https://www.snomed.org/) — систематизированная медицинская номенклатура
- [LOINC](https://loinc.org/) — коды для лабораторных наблюдений

**DICOM:**
- [DICOM Standard](https://www.dicomstandard.org/) — официальный стандарт DICOM

---

## 💡 Key Takeaways

- **HL7 v2** — legacy стандарт с pipe-delimited форматом, до сих пор широко используется
- **FHIR** — современный REST/JSON стандарт, будущее healthcare interoperability
- **ICD-10** — международная классификация диагнозов (~70,000 кодов)
- **SNOMED CT** — детальная клиническая терминология (~350,000 концепций)
- **DICOM** — стандарт для хранения и передачи медицинских изображений

---

## 🚀 Next Steps

**Следующие модули:**
- [02_EHR_Systems](../02_EHR_Systems/) — Системы электронных медицинских записей
- [03_Security_Privacy](../03_Security_Privacy/) — Безопасность и HIPAA

**Практика:**
1. Установите библиотеку python-hl7 и распарсите HL7 сообщение
2. Сделайте запрос к публичному FHIR серверу (test.fhir.org)
3. Найдите ICD-10 код для "Type 2 Diabetes Mellitus"

