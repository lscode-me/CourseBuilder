# Cloud Native Development - Quiz
## Cost Management

---

## Question 1: Spot Instances


Какой discount можно получить с Spot instances?

A) До 100%

B) До 90%

C) До 50%

D) До 30%

---

## Question 2: Reserved vs Savings Plans


Какое преимущество Savings Plans над Reserved Instances?

A) Только для EC2

B) Нет commitment

C) Гибкость в выборе instance types и regions

D) Больше discount

---

## Question 3: S3 Storage Class


Какой storage class самый дешёвый для архивных данных?

A) Standard-IA

B) Standard

C) Glacier Instant

D) Glacier Deep Archive

---

## Question 4: Right-Sizing


Что такое right-sizing?

A) Использование только small instances

B) Соответствие ресурсов фактическому использованию

C) Увеличение размера instances

D) Удаление всех resources

---

## Question 5: Cost Visibility


Что необходимо для cost allocation по проектам/командам?

A) Budgets

B) Reserved Instances

C) Tags на ресурсах

D) Spot Instances

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Spot instances: до 90% discount, но могут быть прерваны с 2-минутным предупреждением. |
| 2 | C | Savings Plans позволяют менять instance type и region, сохраняя discount. RIs привязаны к конкретному типу. |
| 3 | D | Glacier Deep Archive: $0.00099/GB — самый дешёвый, но retrieval занимает 12-48 часов. |
| 4 | B | Right-sizing: выбор размера ресурсов соответственно фактическому использованию (CPU, memory, IOPS). |
| 5 | C | Tags (Environment, Project, Team) позволяют группировать расходы в Cost Explorer по нужным измерениям. |

---
