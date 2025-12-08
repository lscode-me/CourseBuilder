# Cloud Native Development - Quiz
## Infrastructure as Code

---

## Question 1: IaC Benefit

Какое главное преимущество IaC?

A) Быстрее чем консоль
B) Воспроизводимость и version control
C) Дешевле
D) Не требует знания AWS

---

## Question 2: Terraform State

Где рекомендуется хранить Terraform state для team work?

A) Локально на компьютере
B) В Git репозитории
C) В S3 с DynamoDB для locking
D) В Terraform Cloud только

---

## Question 3: CloudFormation

Какая функция CloudFormation позволяет предварительно просмотреть изменения?

A) Drift Detection
B) Change Set
C) Stack Policy
D) Rollback

---

## Question 4: Terraform vs CloudFormation

Какое преимущество Terraform над CloudFormation?

A) Лучшая интеграция с AWS
B) Multi-cloud support
C) Автоматический rollback
D) Managed state

---

## Question 5: Best Practice

Как хранить secrets в IaC коде?

A) В переменных
B) В git (зашифрованные)
C) Не хранить, использовать SSM/Secrets Manager references
D) В outputs

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | IaC обеспечивает воспроизводимость (одинаковая инфраструктура везде) и version control (история изменений). |
| 2 | C | S3 для хранения + DynamoDB для locking предотвращает concurrent modifications. |
| 3 | B | Change Set показывает какие ресурсы будут созданы/изменены/удалены перед применением. |
| 4 | B | Terraform поддерживает AWS, GCP, Azure и 1000+ других провайдеров. CloudFormation — только AWS. |
| 5 | C | Secrets никогда не хранятся в коде. Используются references на SSM Parameter Store или Secrets Manager. |

---
