# Медицинские Классификаторы - Quiz

Проверьте свои знания по ICD-10, SNOMED CT и LOINC.

---

## Question 1: ICD-10 назначение



Для чего в первую очередь используется ICD-10?

A) Описание процедур

B) Классификация болезней и billing

C) Идентификация пациентов

D) Лабораторные результаты

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

A) SNOMED CT только для лабораторий

B) ICD-10 более детальный

C) SNOMED CT — онтология с отношениями между концепциями

D) SNOMED CT только для США

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

A) Страхования

B) Классификации болезней

C) Описания операций

D) Идентификации лабораторных наблюдений

---

## Question 6: LOINC 718-7



Что означает LOINC код 718-7?

A) Glucose

B) Creatinine

C) Sodium

D) Hemoglobin

---

## Question 7: ICD-10 глава E



Какие заболевания кодируются буквой E в ICD-10?

A) Инфекционные болезни

B) Эндокринные и метаболические

C) Глазные заболевания

D) Психические расстройства

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

B) Adult

C) Initial encounter

D) Ambulatory

---

## Question 10: SNOMED CT иерархия



Какая связь между кодами 44054006 (Type 2 DM) и 73211009 (Diabetes mellitus)?

A) 44054006 is-a 73211009

B) Они идентичны

C) Нет связи

D) 73211009 is-a 44054006

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

A) ~350,000

B) ~150,000

C) ~70,000

D) ~14,000

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

A) 38341003

B) 22298006

C) 44054006

D) 73211009

---

## Question 15: LOINC System URI



Какой URI используется для LOINC в FHIR?

A) http://hl7.org/fhir/loinc

B) http://snomed.info/sct

C) http://terminology.loinc.org

D) http://loinc.org

---

## Question 16: Выбор системы для billing



Какую систему кодирования обычно требуют для страхового возмещения?

A) LOINC

B) RxNorm

C) ICD-10

D) SNOMED CT

---

## Question 17: SNOMED CT FSN



Что такое FSN в SNOMED CT?

A) Federal Standard Nomenclature

B) Fully Specified Name

C) FHIR Standard Name

D) Fast Standard Number

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

A) SNOMED CT

B) CPT

C) LOINC

D) ICD-10

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | ICD-10 — стандарт для классификации болезней и billing |
| 2 | C | E11.9 — Type 2 diabetes mellitus without complications |
| 3 | C | SNOMED CT — онтология с is-a и другими отношениями |
| 4 | B | ~350,000 активных концепций в SNOMED CT |
| 5 | D | LOINC — стандарт для лабораторных и клинических наблюдений |
| 6 | D | 718-7 — Hemoglobin |
| 7 | B | E = Endocrine, nutritional and metabolic diseases |
| 8 | C | 6 частей: Component, Property, Timing, System, Scale, Method |
| 9 | C | A = Initial encounter (первичное обращение) |
| 10 | A | Type 2 DM is-a Diabetes mellitus (иерархия) |
| 11 | B | 8480-6 — Systolic blood pressure |
| 12 | C | ~70,000 кодов в ICD-10-CM |
| 13 | B | CodeableConcept поддерживает несколько систем кодирования |
| 14 | A | 38341003 — Hypertensive disorder (SNOMED CT) |
| 15 | D | http://loinc.org — официальный URI |
| 16 | C | ICD-10 требуется для billing и страхования |
| 17 | B | FSN = Fully Specified Name |
| 18 | B | I = Diseases of the circulatory system |
| 19 | B | 8867-4 — Heart rate |
| 20 | A | SNOMED CT — наиболее детальная клиническая терминология |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете медицинские классификаторы. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите различия между системами. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о ICD-10 и SNOMED CT. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите материал заново. |

---

