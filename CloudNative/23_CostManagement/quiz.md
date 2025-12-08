# Cloud Native Development - Quiz
## Cost Management

---

## Question 1: Spot Instances

Какой discount можно получить с Spot instances?

A) До 30%
B) До 50%
C) До 90%
D) До 100%

---

## Question 2: Reserved vs Savings Plans

Какое преимущество Savings Plans над Reserved Instances?

A) Больше discount
B) Гибкость в выборе instance types и regions
C) Нет commitment
D) Только для EC2

---

## Question 3: S3 Storage Class

Какой storage class самый дешёвый для архивных данных?

A) Standard
B) Standard-IA
C) Glacier Instant
D) Glacier Deep Archive

---

## Question 4: Right-Sizing

Что такое right-sizing?

A) Увеличение размера instances
B) Соответствие ресурсов фактическому использованию
C) Использование только small instances
D) Удаление всех resources

---

## Question 5: Cost Visibility

Что необходимо для cost allocation по проектам/командам?

A) Budgets
B) Tags на ресурсах
C) Reserved Instances
D) Spot Instances

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Spot instances: до 90% discount, но могут быть прерваны с 2-минутным предупреждением. |
| 2 | B | Savings Plans позволяют менять instance type и region, сохраняя discount. RIs привязаны к конкретному типу. |
| 3 | D | Glacier Deep Archive: $0.00099/GB — самый дешёвый, но retrieval занимает 12-48 часов. |
| 4 | B | Right-sizing: выбор размера ресурсов соответственно фактическому использованию (CPU, memory, IOPS). |
| 5 | B | Tags (Environment, Project, Team) позволяют группировать расходы в Cost Explorer по нужным измерениям. |

---
