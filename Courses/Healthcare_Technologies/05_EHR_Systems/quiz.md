# EHR Systems - Quiz

Проверьте свои знания по системам электронных медицинских записей: архитектура, компоненты, HIE, SMART on FHIR.

---

## Question 1: EHR vs EMR



В чём основное отличие EHR от EMR?

A) EHR дороже

B) EHR предназначен для обмена между организациями

C) EMR более современный

D) Нет различий

---

## Question 2: CPOE



CPOE означает:

A) Computerized Physician Order Entry

B) Clinical Processing of Orders

C) Computer Protocol for Orders

D) Clinical Patient Order Entry

---

## Question 3: CDSS



Что делает CDSS?

A) Хранит медицинские документы

B) Предоставляет decision support (alerts, guidelines)

C) Шифрует данные

D) Выполняет billing

---

## Question 4: HIE



Health Information Exchange позволяет:

A) Обмениваться данными между организациями

B) Обрабатывать платежи

C) Назначать лекарства

D) Хранить изображения

---

## Question 5: SMART on FHIR



SMART on FHIR это:

A) База данных

B) Протокол шифрования

C) Платформа для интеграции приложений с EHR

D) Медицинское оборудование

---

## Question 6: Master Patient Index



MPI (Master Patient Index) используется для:

A) Хранения лабораторных результатов

B) Уникальной идентификации пациентов в системе

C) Шифрования данных

D) Scheduling appointments

---

## Question 7: HL7 MLLP



HL7 MLLP это:

A) Формат изображений

B) База данных

C) Протокол передачи HL7 сообщений по TCP

D) Язык программирования

---

## Question 8: HIE модели



Какая модель HIE хранит все данные в центральном репозитории?

A) Distributed

B) Hybrid

C) Centralized

D) Federated

---

## Question 9: DICOM интеграция



Для получения медицинских изображений из PACS используется:

A) FTP

B) DICOM C-FIND и C-MOVE

C) Email

D) HTTP REST API

---

## Question 10: Clinical Documentation



Какой компонент EHR отвечает за progress notes и discharge summaries?

A) CDSS

B) CPOE

C) Results Management

D) Clinical Documentation

---

## Question 11: Drug-drug interaction



Какой компонент EHR проверяет drug-drug interactions?

A) CPOE

B) CDSS

C) Patient Management

D) Billing

---

## Question 12: EHR архитектура



Какой слой EHR отвечает за интеграцию с внешними системами?

A) User Interface Layer

B) Data Layer

C) Application Services Layer

D) Integration Layer

---

## Question 13: SMART App



Для авторизации SMART on FHIR приложения используется:

A) Basic Authentication

B) OAuth 2.0

C) API Key

D) Certificate

---

## Question 14: Query Types



Какой тип HIE запроса используется для поиска пациента в сети?

A) Patient Discovery

B) Document Retrieve

C) Data Exchange

D) Document Query

---

## Question 15: EHR Performance



Какое максимальное рекомендованное время отклика для критических операций в EHR?

A) 2 секунды

B) 30 секунд

C) 10 секунд

D) 5 секунд

---

## Question 16: Federated HIE



В федеративной модели HIE данные:

A) Дублируются во всех организациях

B) Хранятся в облаке

C) Хранятся в центральном репозитории

D) Остаются в источниках, запросы маршрутизируются

---

## Question 17: Results Management



Results Management в EHR включает:

A) Только лабораторные результаты

B) Lab results, radiology reports, pathology reports

C) Только назначения врача

D) Billing информацию

---

## Question 18: HL7 MLLP Framing



Какие символы используются для framing в HL7 MLLP?

A) [ и ]

B) Vertical Tab (0x0B) и File Separator (0x1C)

C) HTTP headers

D) { и }

---

## Question 19: DICOM Metadata



Какие метаданные можно получить из DICOM файла?

A) SQL запросы

B) PatientName, StudyDate, Modality

C) Только изображение

D) Только имя файла

---

## Question 20: EHR Data Layer



Data Layer в EHR содержит:

A) Только UI компоненты

B) Только Integration Engine

C) Только FHIR API

D) Relational DB, Document Store, BLOB Storage

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | EHR для обмена между организациями |
| 2 | A | Computerized Physician Order Entry |
| 3 | B | Decision support (alerts, guidelines) |
| 4 | A | Обмен данными между организациями |
| 5 | C | Платформа для интеграции медицинских приложений с EHR |
| 6 | B | Уникальная идентификация пациентов в системе |
| 7 | C | Протокол передачи HL7 сообщений по TCP (MLLP) |
| 8 | C | Centralized модель хранит данные в центральном репозитории |
| 9 | B | DICOM C-FIND для поиска и C-MOVE для получения |
| 10 | D | Clinical Documentation отвечает за notes и summaries |
| 11 | B | CDSS (Clinical Decision Support System) |
| 12 | D | Integration Layer с HL7 Interface Engine и FHIR API Gateway |
| 13 | B | OAuth 2.0 для авторизации SMART приложений |
| 14 | A | Patient Discovery для поиска пациента |
| 15 | A | 2 секунды для критических операций |
| 16 | D | Federated модель не хранит данные централизованно |
| 17 | B | Results Management включает lab, radiology, pathology reports |
| 18 | B | START_BLOCK (0x0B) и END_BLOCK (0x1C) + CR |
| 19 | B | DICOM содержит PatientName, StudyDate, Modality |
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

