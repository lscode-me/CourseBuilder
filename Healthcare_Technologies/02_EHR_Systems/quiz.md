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

A) Clinical Patient Order Entry

B) Computerized Physician Order Entry

C) Computer Protocol for Orders

D) Clinical Processing of Orders

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

B) Хранить изображения

C) Обрабатывать платежи

D) Назначать лекарства

---

## Question 5: SMART on FHIR

SMART on FHIR это:

A) Протокол шифрования

B) Платформа для интеграции приложений с EHR

C) База данных

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

A) Язык программирования

B) Протокол передачи HL7 сообщений по TCP

C) База данных

D) Формат изображений

---

## Question 8: HIE модели

Какая модель HIE хранит все данные в центральном репозитории?

A) Federated

B) Centralized

C) Hybrid

D) Distributed

---

## Question 9: DICOM интеграция

Для получения медицинских изображений из PACS используется:

A) HTTP REST API

B) DICOM C-FIND и C-MOVE

C) FTP

D) Email

---

## Question 10: Clinical Documentation

Какой компонент EHR отвечает за progress notes и discharge summaries?

A) CPOE

B) CDSS

C) Clinical Documentation

D) Results Management

---

## Question 11: Drug-drug interaction

Какой компонент EHR проверяет drug-drug interactions?

A) Patient Management

B) CPOE

C) CDSS

D) Billing

---

## Question 12: EHR архитектура

Какой слой EHR отвечает за интеграцию с внешними системами?

A) User Interface Layer

B) Application Services Layer

C) Integration Layer

D) Data Layer

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

A) Document Query

B) Document Retrieve

C) Patient Discovery

D) Data Exchange

---

## Question 15: EHR Performance

Какое максимальное рекомендованное время отклика для критических операций в EHR?

A) 5 секунд

B) 2 секунды

C) 10 секунд

D) 30 секунд

---

## Answers

1. **B** - EHR для обмена между организациями
2. **B** - Computerized Physician Order Entry
3. **B** - Decision support (alerts, guidelines)
4. **A** - Обмен данными между организациями
5. **B** - Платформа для интеграции медицинских приложений с EHR
6. **B** - Уникальная идентификация пациентов в системе
7. **B** - Протокол передачи HL7 сообщений по TCP (Minimal Lower Layer Protocol)
8. **B** - Centralized модель хранит данные в центральном репозитории
9. **B** - DICOM C-FIND для поиска и C-MOVE для получения
10. **C** - Clinical Documentation отвечает за notes и summaries
11. **C** - CDSS (Clinical Decision Support System)
12. **C** - Integration Layer с HL7 Interface Engine и FHIR API Gateway
13. **B** - OAuth 2.0 для авторизации SMART приложений
14. **C** - Patient Discovery для поиска пациента
15. **B** - 2 секунды для критических операций
