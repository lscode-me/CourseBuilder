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

B) Локально на компьютере

C) В Git репозитории

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

C) Автоматический rollback

D) Managed state

---

## Question 5: Best Practice





Как хранить secrets в IaC коде?

A) В git (зашифрованные)

B) В переменных

C) Не хранить, использовать SSM/Secrets Manager references

D) В outputs

---

## Question 6: CDK




Что такое AWS CDK?

A) Cloud Database Kit

B) Определение инфраструктуры на языках программирования

C) CI/CD tool

D) Monitoring tool

---

## Question 7: SAM




Для чего используется AWS SAM?

A) Для VMs

B) Для контейнеров

C) Для serverless applications (Lambda, API Gateway, DynamoDB)

D) Для любой инфраструктуры

---

## Question 8: Drift Detection




Что такое Drift Detection в CloudFormation?

A) Performance monitoring

B) Cost analysis

C) Обнаружение manual changes в ресурсах

D) Security scan

---

## Question 9: Terraform Modules




Для чего используются Terraform Modules?

A) Только для variables

B) Для reusable infrastructure components

C) Только для outputs

D) Для state

---

## Question 10: Stack Sets




Что делают CloudFormation StackSets?

A) Только security

B) Только monitoring

C) Deploy stacks across multiple accounts/regions

D) Только backup

---

## Question 11: Pulumi




Чем Pulumi отличается от Terraform?

A) Не поддерживает state

B) Только для AWS

C) Использует настоящие языки программирования (не HCL)

D) Ничем

---

## Question 12: terraform plan




Что делает terraform plan?

A) Удаляет ресурсы

B) Применяет изменения

C) Инициализирует project

D) Показывает какие изменения будут сделаны (dry-run)

---

## Question 13: CloudFormation Parameters




Для чего используются Parameters?

A) Для input values при создании stack

B) Только для outputs

C) Для state

D) Для secrets

---

## Question 14: terraform import




Что делает terraform import?

A) Создаёт ресурсы

B) Импортирует существующие ресурсы в state

C) Удаляет ресурсы

D) Экспортирует state

---

## Question 15: Nested Stacks




Для чего используются Nested Stacks?

A) Для monitoring

B) Для billing

C) Для security

D) Для организации больших templates в reusable components

---

## Question 16: terraform workspace




Для чего используются Terraform Workspaces?

A) Для управления multiple environments с одним кодом

B) Для security

C) Для monitoring

D) Для IDE

---

## Question 17: cfn-lint




Что делает cfn-lint?

A) Мониторит ресурсы

B) Деплоит stacks

C) Валидирует CloudFormation templates

D) Шифрует templates

---

## Question 18: terraform.tfvars




Для чего используется terraform.tfvars?

A) Для providers

B) Для outputs

C) Для state

D) Для значений переменных

---

## Question 19: Outputs




Для чего используются Outputs в CloudFormation?

A) Только для logging

B) Для state

C) Только для secrets

D) Для экспорта значений для других stacks или просмотра

---

## Question 20: terraform destroy




Что делает terraform destroy?

A) Показывает план

B) Обновляет state

C) Создаёт ресурсы

D) Удаляет все управляемые ресурсы

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | IaC обеспечивает воспроизводимость (одинаковая инфраструктура везде) и version control (история изменений). |
| 2 | A | S3 для хранения + DynamoDB для locking предотвращает concurrent modifications. |
| 3 | C | Change Set показывает какие ресурсы будут созданы/изменены/удалены перед применением. |
| 4 | B | Terraform поддерживает AWS, GCP, Azure и 1000+ других провайдеров. CloudFormation — только AWS. |
| 5 | C | Secrets никогда не хранятся в коде. Используются references на SSM Parameter Store или Secrets Manager. |
| 6 | B | CDK — инфраструктура на языках программирования |
| 7 | C | SAM для serverless (Lambda, API Gateway, DynamoDB) |
| 8 | C | Drift Detection находит manual changes |
| 9 | B | Modules для reusable components |
| 10 | C | StackSets: deploy across accounts/regions |
| 11 | C | Pulumi использует настоящие языки |
| 12 | D | terraform plan показывает изменения (dry-run) |
| 13 | A | Parameters для input values |
| 14 | B | terraform import импортирует существующие ресурсы |
| 15 | D | Nested Stacks для организации templates |
| 16 | A | Workspaces для multiple environments |
| 17 | C | cfn-lint валидирует templates |
| 18 | D | terraform.tfvars для значений переменных |
| 19 | D | Outputs для экспорта значений |
| 20 | D | terraform destroy удаляет все ресурсы |

---
