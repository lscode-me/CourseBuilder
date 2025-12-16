# FHIR - Quiz

Проверьте свои знания по стандарту FHIR.

---

## Question 1: FHIR расшифровка

Что означает FHIR?

A) Foundation for Healthcare IT Resources

B) Federal Health Integration Requirements

C) Fast Health Information Records

D) Fast Healthcare Interoperability Resources

---

## Question 2: Формат данных

Какие форматы данных поддерживает FHIR?

A) Только JSON

B) JSON и XML

C) CSV и JSON

D) Только XML

---

## Question 3: HTTP метод создания

Какой HTTP метод используется для создания нового ресурса?

A) GET

B) POST

C) PATCH

D) PUT

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

A) DSTU2

B) R4

C) R5

D) STU3

---

## Question 6: Observation status

Какое значение status обязательно для финального результата?

A) done

B) final

C) finished

D) completed

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

A) GET /Patient?family=Иванов

B) GET /Patient/Иванов

C) GET /Patient/search?name=Иванов

D) POST /Patient/find

---

## Question 9: Bundle type

Какой тип Bundle используется для атомарных операций?

A) collection

B) batch

C) document

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

A) http://snomed.info/sct

B) http://loinc.org

C) http://terminology.loinc.org

D) http://hl7.org/fhir/loinc

---

## Question 12: Content-Type

Какой Content-Type используется для FHIR JSON?

A) application/hl7-fhir

B) application/json

C) text/fhir-json

D) application/fhir+json

---

## Question 13: _include параметр

Для чего используется параметр _include?

A) Для включения связанных ресурсов в ответ

B) Для пагинации

C) Для фильтрации результатов

D) Для сортировки

---

## Question 14: Обновление ресурса

Какой HTTP метод для полного обновления ресурса?

A) UPDATE

B) POST

C) PATCH

D) PUT

---

## Question 15: meta.versionId

Что содержит поле meta.versionId?

A) Версию FHIR

B) Тип ресурса

C) Версию ресурса (для истории изменений)

D) ID создателя

---

## Question 16: Поиск по дате

Как найти пациентов, рождённых после 1980 года?

A) GET /Patient?birthdate>1980

B) GET /Patient?birth_date>=1980

C) GET /Patient?birthdate=ge1980-01-01

D) GET /Patient?birthdate=after:1980

---

## Question 17: CapabilityStatement

Как получить информацию о возможностях FHIR сервера?

A) GET /capabilities

B) GET /

C) GET /info

D) GET /metadata

---

## Question 18: Observation valueQuantity

Какое поле содержит числовое значение в Observation?

A) result

B) value

C) valueQuantity

D) measurement

---

## Question 19: resourceType

Какое поле определяет тип ресурса в JSON?

A) kind

B) type

C) class

D) resourceType

---

## Question 20: Пагинация

Какой параметр ограничивает количество результатов?

A) _count

B) _max

C) _limit

D) _size

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Fast Healthcare Interoperability Resources |
| 2 | B | FHIR поддерживает JSON и XML форматы |
| 3 | B | POST для создания (сервер назначает ID) |
| 4 | A | Правильный формат: {"reference": "Type/id"} |
| 5 | B | R4 — стабильная версия для production |
| 6 | B | status: "final" для завершённых результатов |
| 7 | B | identifier — массив идентификаторов |
| 8 | A | Параметр family для поиска по фамилии |
| 9 | D | transaction — атомарная операция (всё или ничего) |
| 10 | D | vital-signs — стандартная категория |
| 11 | B | http://loinc.org — официальный URI для LOINC |
| 12 | D | application/fhir+json — FHIR-специфичный тип |
| 13 | A | _include включает referenced ресурсы |
| 14 | D | PUT для полного обновления |
| 15 | C | versionId для версионирования ресурса |
| 16 | C | ge = greater or equal |
| 17 | D | /metadata возвращает CapabilityStatement |
| 18 | C | valueQuantity для числовых значений с единицами |
| 19 | D | resourceType определяет тип ресурса |
| 20 | A | _count ограничивает количество результатов |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете FHIR. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите API операции и поиск. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте лекцию о структуре ресурсов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите материал заново. |

---

