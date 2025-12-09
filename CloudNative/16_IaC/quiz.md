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

A) В S3 с DynamoDB для locking

B) В Git репозитории

C) Локально на компьютере

D) В Terraform Cloud только

---

## Question 3: CloudFormation


Какая функция CloudFormation позволяет предварительно просмотреть изменения?

A) Stack Policy

B) Drift Detection

C) Change Set

D) Rollback

---

## Question 4: Terraform vs CloudFormation


Какое преимущество Terraform над CloudFormation?

A) Лучшая интеграция с AWS

B) Multi-cloud support

C) Managed state

D) Автоматический rollback

---

## Question 5: Best Practice


Как хранить secrets в IaC коде?

A) В переменных

B) Не хранить, использовать SSM/Secrets Manager references

C) В outputs

D) В git (зашифрованные)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | IaC обеспечивает воспроизводимость (одинаковая инфраструктура везде) и version control (история изменений). |
| 2 | A | S3 для хранения + DynamoDB для locking предотвращает concurrent modifications. |
| 3 | C | Change Set показывает какие ресурсы будут созданы/изменены/удалены перед применением. |
| 4 | B | Terraform поддерживает AWS, GCP, Azure и 1000+ других провайдеров. CloudFormation — только AWS. |
| 5 | B | Secrets никогда не хранятся в коде. Используются references на SSM Parameter Store или Secrets Manager. |

---
