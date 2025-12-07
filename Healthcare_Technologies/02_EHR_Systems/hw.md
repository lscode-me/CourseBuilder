# EHR Systems - Задания

---

## Задание 1: Проектирование Database Schema

Спроектируйте базовую схему БД для EHR системы.

**Требования:**
- Таблицы: Patients, Encounters, Medications, Observations
- Relationships и foreign keys
- Indexes для производительности

---

## Задание 2: FHIR API Mock Server

Создайте простой FHIR сервер с Flask.

**Требования:**
- Endpoints: GET/POST /Patient
- In-memory хранилище
- FHIR-compliant JSON responses

---

## Задание 3: HL7 MLLP Receiver

Напишите HL7 MLLP сервер.

**Требования:**
- Слушать на TCP порту
- Парсить HL7 сообщения
- Отправлять ACK

---

## Задание 4: Clinical Decision Support

Реализуйте простое CDSS правило.

**Требования:**
- Проверка drug-drug interaction
- Allergy checking
- Вывести alerts

---

## Задание 5: HIE Query Router

Создайте федеративный HIE query router.

**Требования:**
- Запрос к нескольким источникам
- Агрегация результатов
- Обработка таймаутов

---

Happy coding! 🏥

