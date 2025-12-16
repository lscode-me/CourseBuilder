# Медицинские Классификаторы - Quiz

Проверьте свои знания по ICD-10, SNOMED CT и LOINC.

---

## Question 1: ICD-10 назначение

Для чего в первую очередь используется ICD-10?

A) Описание процедур

B) Лабораторные результаты

C) Классификация болезней и billing

D) Идентификация пациентов

---

## Question 2: ICD-10 E11.9

Что означает код E11.9?

A) Гипертония

B) Инфаркт миокарда

C) Сахарный диабет 2 типа без осложнений

D) Пневмония

---

## Question 3: SNOMED CT

Что отличает SNOMED CT от ICD-10?

A) SNOMED CT только для США

B) SNOMED CT только для лабораторий

C) ICD-10 более детальный

D) SNOMED CT — онтология с отношениями между концепциями

---

## Question 4: SNOMED CT концепций

Сколько примерно активных концепций в SNOMED CT?

A) ~70,000

B) ~350,000

C) ~14,000

D) ~1,000,000

---

## Question 5: LOINC назначение

LOINC используется для:

A) Описания операций

B) Классификации болезней

C) Идентификации лабораторных наблюдений

D) Страхования

---

## Question 6: LOINC 718-7

Что означает LOINC код 718-7?

A) Sodium

B) Glucose

C) Creatinine

D) Hemoglobin

---

## Question 7: ICD-10 глава E

Какие заболевания кодируются буквой E в ICD-10?

A) Глазные заболевания

B) Инфекционные болезни

C) Эндокринные и метаболические

D) Психические расстройства

---

## Question 8: LOINC структура

Сколько частей в полном имени LOINC кода?

A) 8

B) 4

C) 6

D) 3

---

## Question 9: ICD-10 7-й символ

В травматологических кодах ICD-10, что означает "A" как 7-й символ?

A) Adult

B) Initial encounter

C) Acute

D) Ambulatory

---

## Question 10: SNOMED CT иерархия

Какая связь между кодами 44054006 (Type 2 DM) и 73211009 (Diabetes mellitus)?

A) Нет связи

B) 44054006 is-a 73211009

C) 73211009 is-a 44054006

D) Они идентичны

---

## Question 11: LOINC 8480-6

LOINC код 8480-6 используется для:

A) Temperature

B) Systolic blood pressure

C) Oxygen saturation

D) Heart rate

---

## Question 12: ICD-10-CM количество

Сколько примерно кодов в ICD-10-CM (USA version)?

A) ~14,000

B) ~150,000

C) ~70,000

D) ~350,000

---

## Question 13: FHIR CodeableConcept

Может ли FHIR CodeableConcept содержать несколько кодировок?

A) Нет, только одну

B) Да, можно включить ICD-10 и SNOMED CT одновременно

C) Только для лабораторных данных

D) Только если они из одной системы

---

## Question 14: Mapping

Какой SNOMED CT код соответствует ICD-10 I10 (Hypertension)?

A) 44054006

B) 38341003

C) 22298006

D) 73211009

---

## Question 15: LOINC System URI

Какой URI используется для LOINC в FHIR?

A) http://snomed.info/sct

B) http://loinc.org

C) http://hl7.org/fhir/loinc

D) http://terminology.loinc.org

---

## Question 16: Выбор системы для billing

Какую систему кодирования обычно требуют для страхового возмещения?

A) SNOMED CT

B) RxNorm

C) ICD-10

D) LOINC

---

## Question 17: SNOMED CT FSN

Что такое FSN в SNOMED CT?

A) Fully Specified Name

B) Fast Standard Number

C) Federal Standard Nomenclature

D) FHIR Standard Name

---

## Question 18: ICD-10 категория I

Какие заболевания кодируются буквой I в ICD-10?

A) Инфекционные болезни

B) Психические расстройства

C) Травмы

D) Болезни системы кровообращения

---

## Question 19: LOINC vital signs

Какой LOINC код для частоты сердечных сокращений (heart rate)?

A) 8310-5

B) 8480-6

C) 2708-6

D) 8867-4

---

## Question 20: Детальность терминологии

Какая система обеспечивает наиболее детальное клиническое описание?

A) ICD-10

B) CPT

C) LOINC

D) SNOMED CT

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | ICD-10 — стандарт для классификации болезней и billing |
| 2 | C | E11.9 — Type 2 diabetes mellitus without complications |
| 3 | D | SNOMED CT — онтология с is-a и другими отношениями |
| 4 | B | ~350,000 активных концепций в SNOMED CT |
| 5 | C | LOINC — стандарт для лабораторных и клинических наблюдений |
| 6 | D | 718-7 — Hemoglobin |
| 7 | C | E = Endocrine, nutritional and metabolic diseases |
| 8 | C | 6 частей: Component, Property, Timing, System, Scale, Method |
| 9 | B | A = Initial encounter (первичное обращение) |
| 10 | B | Type 2 DM is-a Diabetes mellitus (иерархия) |
| 11 | B | 8480-6 — Systolic blood pressure |
| 12 | C | ~70,000 кодов в ICD-10-CM |
| 13 | B | CodeableConcept поддерживает несколько систем кодирования |
| 14 | B | 38341003 — Hypertensive disorder (SNOMED CT) |
| 15 | B | http://loinc.org — официальный URI |
| 16 | C | ICD-10 требуется для billing и страхования |
| 17 | A | FSN = Fully Specified Name |
| 18 | D | I = Diseases of the circulatory system |
| 19 | D | 8867-4 — Heart rate |
| 20 | D | SNOMED CT — наиболее детальная клиническая терминология |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете медицинские классификаторы. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите различия между системами. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о ICD-10 и SNOMED CT. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите материал заново. |

---

