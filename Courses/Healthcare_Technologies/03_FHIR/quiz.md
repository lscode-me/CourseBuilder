# FHIR - Quiz

Проверьте свои знания по стандарту FHIR.

---

## Question 1: FHIR расшифровка



Что означает FHIR?

A) Fast Healthcare Interoperability Resources

B) Federal Health Integration Requirements

C) Fast Health Information Records

D) Foundation for Healthcare IT Resources

---

## Question 2: Формат данных



Какие форматы данных поддерживает FHIR?

A) Только JSON

B) CSV и JSON

C) Только XML

D) JSON и XML

---

## Question 3: HTTP метод создания



Какой HTTP метод используется для создания нового ресурса?

A) GET

B) POST

C) PUT

D) PATCH

---

## Question 4: Reference формат



Как правильно указать ссылку на пациента в FHIR?

A) {"reference": "Patient/patient-123"}

B) {"id": "patient-123"}

C) {"Patient": "123"}

D) "patient-123"

---

## Question 5: Рекомендуемая версия



Какая версия FHIR рекомендуется для production?

A) STU3

B) R5

C) R4

D) DSTU2

---

## Question 6: Observation status



Какое значение status обязательно для финального результата?

A) done

B) finished

C) completed

D) final

---

## Question 7: Patient Resource



Какое поле Patient содержит идентификаторы (MRN, СНИЛС)?

A) id

B) identifier

C) name

D) meta

---

## Question 8: Поиск пациентов



Какой URL для поиска пациентов по фамилии "Иванов"?

A) GET /Patient/search?name=Иванов

B) GET /Patient?family=Иванов

C) POST /Patient/find

D) GET /Patient/Иванов

---

## Question 9: Bundle type



Какой тип Bundle используется для атомарных операций?

A) document

B) batch

C) collection

D) transaction

---

## Question 10: Vital Signs category



Какой код категории используется для vital signs?

A) laboratory

B) measurements

C) clinical

D) vital-signs

---

## Question 11: LOINC system



Какой URI системы используется для LOINC кодов?

A) http://hl7.org/fhir/loinc

B) http://terminology.loinc.org

C) http://loinc.org

D) http://snomed.info/sct

---

## Question 12: Content-Type



Какой Content-Type используется для FHIR JSON?

A) application/json

B) application/fhir+json

C) text/fhir-json

D) application/hl7-fhir

---

## Question 13: _include параметр



Для чего используется параметр _include?

A) Для включения связанных ресурсов в ответ

B) Для фильтрации результатов

C) Для пагинации

D) Для сортировки

---

## Question 14: Обновление ресурса



Какой HTTP метод для полного обновления ресурса?

A) POST

B) PUT

C) PATCH

D) UPDATE

---

## Question 15: meta.versionId



Что содержит поле meta.versionId?

A) Версию FHIR

B) Версию ресурса (для истории изменений)

C) ID создателя

D) Тип ресурса

---

## Question 16: Поиск по дате



Как найти пациентов, рождённых после 1980 года?

A) GET /Patient?birthdate>1980

B) GET /Patient?birthdate=after:1980

C) GET /Patient?birthdate=ge1980-01-01

D) GET /Patient?birth_date>=1980

---

## Question 17: CapabilityStatement



Как получить информацию о возможностях FHIR сервера?

A) GET /

B) GET /info

C) GET /metadata

D) GET /capabilities

---

## Question 18: Observation valueQuantity



Какое поле содержит числовое значение в Observation?

A) valueQuantity

B) value

C) result

D) measurement

---

## Question 19: resourceType



Какое поле определяет тип ресурса в JSON?

A) kind

B) resourceType

C) class

D) type

---

## Question 20: Пагинация



Какой параметр ограничивает количество результатов?

A) _limit

B) _count

C) _max

D) _size

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Fast Healthcare Interoperability Resources |
| 2 | D | FHIR поддерживает JSON и XML форматы |
| 3 | B | POST для создания (сервер назначает ID) |
| 4 | A | Правильный формат: {"reference": "Type/id"} |
| 5 | C | R4 — стабильная версия для production |
| 6 | D | status: "final" для завершённых результатов |
| 7 | B | identifier — массив идентификаторов |
| 8 | B | Параметр family для поиска по фамилии |
| 9 | D | transaction — атомарная операция (всё или ничего) |
| 10 | D | vital-signs — стандартная категория |
| 11 | C | http://loinc.org — официальный URI для LOINC |
| 12 | B | application/fhir+json — FHIR-специфичный тип |
| 13 | A | _include включает referenced ресурсы |
| 14 | B | PUT для полного обновления |
| 15 | B | versionId для версионирования ресурса |
| 16 | C | ge = greater or equal |
| 17 | C | /metadata возвращает CapabilityStatement |
| 18 | A | valueQuantity для числовых значений с единицами |
| 19 | B | resourceType определяет тип ресурса |
| 20 | B | _count ограничивает количество результатов |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете FHIR. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите API операции и поиск. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте лекцию о структуре ресурсов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите материал заново. |

---

