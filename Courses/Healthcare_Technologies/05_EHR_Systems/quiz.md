# EHR Systems - Quiz

Проверьте свои знания по системам электронных медицинских записей: архитектура, компоненты, HIE, SMART on FHIR.

---

## Question 1: EHR vs EMR

В чём основное отличие EHR от EMR?

A) EMR более современный

B) EHR предназначен для обмена между организациями

C) EHR дороже

D) Нет различий

---

## Question 2: CPOE

CPOE означает:

A) Clinical Processing of Orders

B) Clinical Patient Order Entry

C) Computerized Physician Order Entry

D) Computer Protocol for Orders

---

## Question 3: CDSS

Что делает CDSS?

A) Шифрует данные

B) Хранит медицинские документы

C) Выполняет billing

D) Предоставляет decision support (alerts, guidelines)

---

## Question 4: HIE

Health Information Exchange позволяет:

A) Обрабатывать платежи

B) Назначать лекарства

C) Хранить изображения

D) Обмениваться данными между организациями

---

## Question 5: SMART on FHIR

SMART on FHIR это:

A) База данных

B) Медицинское оборудование

C) Платформа для интеграции приложений с EHR

D) Протокол шифрования

---

## Question 6: Master Patient Index

MPI (Master Patient Index) используется для:

A) Scheduling appointments

B) Хранения лабораторных результатов

C) Уникальной идентификации пациентов в системе

D) Шифрования данных

---

## Question 7: HL7 MLLP

HL7 MLLP это:

A) База данных

B) Формат изображений

C) Язык программирования

D) Протокол передачи HL7 сообщений по TCP

---

## Question 8: HIE модели

Какая модель HIE хранит все данные в центральном репозитории?

A) Centralized

B) Hybrid

C) Federated

D) Distributed

---

## Question 9: DICOM интеграция

Для получения медицинских изображений из PACS используется:

A) HTTP REST API

B) Email

C) DICOM C-FIND и C-MOVE

D) FTP

---

## Question 10: Clinical Documentation

Какой компонент EHR отвечает за progress notes и discharge summaries?

A) Results Management

B) CPOE

C) Clinical Documentation

D) CDSS

---

## Question 11: Drug-drug interaction

Какой компонент EHR проверяет drug-drug interactions?

A) Billing

B) CDSS

C) Patient Management

D) CPOE

---

## Question 12: EHR архитектура

Какой слой EHR отвечает за интеграцию с внешними системами?

A) Integration Layer

B) Application Services Layer

C) Data Layer

D) User Interface Layer

---

## Question 13: SMART App

Для авторизации SMART on FHIR приложения используется:

A) Basic Authentication

B) Certificate

C) API Key

D) OAuth 2.0

---

## Question 14: Query Types

Какой тип HIE запроса используется для поиска пациента в сети?

A) Document Query

B) Patient Discovery

C) Data Exchange

D) Document Retrieve

---

## Question 15: EHR Performance

Какое максимальное рекомендованное время отклика для критических операций в EHR?

A) 30 секунд

B) 5 секунд

C) 10 секунд

D) 2 секунды

---

## Question 16: Federated HIE

В федеративной модели HIE данные:

A) Хранятся в центральном репозитории

B) Остаются в источниках, запросы маршрутизируются

C) Хранятся в облаке

D) Дублируются во всех организациях

---

## Question 17: Results Management

Results Management в EHR включает:

A) Только лабораторные результаты

B) Только назначения врача

C) Lab results, radiology reports, pathology reports

D) Billing информацию

---

## Question 18: HL7 MLLP Framing

Какие символы используются для framing в HL7 MLLP?

A) { и }

B) [ и ]

C) HTTP headers

D) Vertical Tab (0x0B) и File Separator (0x1C)

---

## Question 19: DICOM Metadata

Какие метаданные можно получить из DICOM файла?

A) SQL запросы

B) Только изображение

C) Только имя файла

D) PatientName, StudyDate, Modality

---

## Question 20: EHR Data Layer

Data Layer в EHR содержит:

A) Только UI компоненты

B) Только FHIR API

C) Только Integration Engine

D) Relational DB, Document Store, BLOB Storage

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | EHR для обмена между организациями |
| 2 | C | Computerized Physician Order Entry |
| 3 | D | Decision support (alerts, guidelines) |
| 4 | D | Обмен данными между организациями |
| 5 | C | Платформа для интеграции медицинских приложений с EHR |
| 6 | C | Уникальная идентификация пациентов в системе |
| 7 | D | Протокол передачи HL7 сообщений по TCP (MLLP) |
| 8 | A | Centralized модель хранит данные в центральном репозитории |
| 9 | C | DICOM C-FIND для поиска и C-MOVE для получения |
| 10 | C | Clinical Documentation отвечает за notes и summaries |
| 11 | B | CDSS (Clinical Decision Support System) |
| 12 | A | Integration Layer с HL7 Interface Engine и FHIR API Gateway |
| 13 | D | OAuth 2.0 для авторизации SMART приложений |
| 14 | B | Patient Discovery для поиска пациента |
| 15 | D | 2 секунды для критических операций |
| 16 | B | Federated модель не хранит данные централизованно |
| 17 | C | Results Management включает lab, radiology, pathology reports |
| 18 | D | START_BLOCK (0x0B) и END_BLOCK (0x1C) + CR |
| 19 | D | DICOM содержит PatientName, StudyDate, Modality |
| 20 | D | Data Layer содержит Relational DB, Document Store, BLOB Storage |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать лекцию. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

