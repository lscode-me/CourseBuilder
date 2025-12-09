# Медицинские Классификаторы - Quiz

Проверьте свои знания по ICD-10, SNOMED CT и LOINC.

---

## Question 1: ICD-10 назначение

Для чего в первую очередь используется ICD-10?

A) Лабораторные результаты

B) Классификация болезней и billing

C) Описание процедур

D) Идентификация пациентов

---

## Question 2: ICD-10 E11.9

Что означает код E11.9?

A) Инфаркт миокарда

B) Гипертония

C) Сахарный диабет 2 типа без осложнений

D) Пневмония

---

## Question 3: SNOMED CT

Что отличает SNOMED CT от ICD-10?

A) SNOMED CT только для США

B) SNOMED CT — онтология с отношениями между концепциями

C) ICD-10 более детальный

D) SNOMED CT только для лабораторий

---

## Question 4: SNOMED CT концепций

Сколько примерно активных концепций в SNOMED CT?

A) ~14,000

B) ~70,000

C) ~350,000

D) ~1,000,000

---

## Question 5: LOINC назначение

LOINC используется для:

A) Классификации болезней

B) Страхования

C) Идентификации лабораторных наблюдений

D) Описания операций

---

## Question 6: LOINC 718-7

Что означает LOINC код 718-7?

A) Glucose

B) Hemoglobin

C) Creatinine

D) Sodium

---

## Question 7: ICD-10 глава E

Какие заболевания кодируются буквой E в ICD-10?

A) Глазные заболевания

B) Эндокринные и метаболические

C) Психические расстройства

D) Инфекционные болезни

---

## Question 8: LOINC структура

Сколько частей в полном имени LOINC кода?

A) 3

B) 4

C) 6

D) 8

---

## Question 9: ICD-10 7-й символ

В травматологических кодах ICD-10, что означает "A" как 7-й символ?

A) Acute

B) Initial encounter

C) Ambulatory

D) Adult

---

## Question 10: SNOMED CT иерархия

Какая связь между кодами 44054006 (Type 2 DM) и 73211009 (Diabetes mellitus)?

A) Они идентичны

B) 44054006 is-a 73211009

C) 73211009 is-a 44054006

D) Нет связи

---

## Question 11: LOINC 8480-6

LOINC код 8480-6 используется для:

A) Heart rate

B) Systolic blood pressure

C) Temperature

D) Oxygen saturation

---

## Question 12: ICD-10-CM количество

Сколько примерно кодов в ICD-10-CM (USA version)?

A) ~14,000

B) ~70,000

C) ~150,000

D) ~350,000

---

## Question 13: FHIR CodeableConcept

Может ли FHIR CodeableConcept содержать несколько кодировок?

A) Нет, только одну

B) Да, можно включить ICD-10 и SNOMED CT одновременно

C) Только если они из одной системы

D) Только для лабораторных данных

---

## Question 14: Mapping

Какой SNOMED CT код соответствует ICD-10 I10 (Hypertension)?

A) 73211009

B) 38341003

C) 44054006

D) 22298006

---

## Question 15: LOINC System URI

Какой URI используется для LOINC в FHIR?

A) http://snomed.info/sct

B) http://loinc.org

C) http://terminology.loinc.org

D) http://hl7.org/fhir/loinc

---

## Question 16: Выбор системы для billing

Какую систему кодирования обычно требуют для страхового возмещения?

A) SNOMED CT

B) LOINC

C) ICD-10

D) RxNorm

---

## Question 17: SNOMED CT FSN

Что такое FSN в SNOMED CT?

A) Fast Standard Number

B) Fully Specified Name

C) Federal Standard Nomenclature

D) FHIR Standard Name

---

## Question 18: ICD-10 категория I

Какие заболевания кодируются буквой I в ICD-10?

A) Инфекционные болезни

B) Болезни системы кровообращения

C) Травмы

D) Психические расстройства

---

## Question 19: LOINC vital signs

Какой LOINC код для частоты сердечных сокращений (heart rate)?

A) 8480-6

B) 8867-4

C) 8310-5

D) 2708-6

---

## Question 20: Детальность терминологии

Какая система обеспечивает наиболее детальное клиническое описание?

A) ICD-10

B) SNOMED CT

C) LOINC

D) CPT

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | ICD-10 — стандарт для классификации болезней и billing |
| 2 | C | E11.9 — Type 2 diabetes mellitus without complications |
| 3 | B | SNOMED CT — онтология с is-a и другими отношениями |
| 4 | C | ~350,000 активных концепций в SNOMED CT |
| 5 | C | LOINC — стандарт для лабораторных и клинических наблюдений |
| 6 | B | 718-7 — Hemoglobin |
| 7 | B | E = Endocrine, nutritional and metabolic diseases |
| 8 | C | 6 частей: Component, Property, Timing, System, Scale, Method |
| 9 | B | A = Initial encounter (первичное обращение) |
| 10 | B | Type 2 DM is-a Diabetes mellitus (иерархия) |
| 11 | B | 8480-6 — Systolic blood pressure |
| 12 | B | ~70,000 кодов в ICD-10-CM |
| 13 | B | CodeableConcept поддерживает несколько систем кодирования |
| 14 | B | 38341003 — Hypertensive disorder (SNOMED CT) |
| 15 | B | http://loinc.org — официальный URI |
| 16 | C | ICD-10 требуется для billing и страхования |
| 17 | B | FSN = Fully Specified Name |
| 18 | B | I = Diseases of the circulatory system |
| 19 | B | 8867-4 — Heart rate |
| 20 | B | SNOMED CT — наиболее детальная клиническая терминология |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете медицинские классификаторы. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите различия между системами. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о ICD-10 и SNOMED CT. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите материал заново. |

---

