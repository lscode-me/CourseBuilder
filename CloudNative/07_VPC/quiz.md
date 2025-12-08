# Cloud Native Development - Quiz
## VPC: Virtual Private Cloud

---

## Question 1: Что делает подсеть "public"?

A) Находится в первой AZ

B) Имеет route к Internet Gateway в route table

C) Использует публичные IP адреса

D) Не имеет Security Groups

---

## Question 2: Security Groups vs NACLs

Какое утверждение ВЕРНО?

A) Security Groups stateless, NACLs stateful

B) Security Groups работают на уровне subnet

C) Security Groups stateful, поддерживают только Allow rules

D) NACLs применяются к отдельным инстансам

---

## Question 3: NAT Gateway

Для чего нужен NAT Gateway?

A) Для входящего трафика в private subnet

B) Для исходящего интернет-трафика из private subnet

C) Для связи между VPC

D) Для DNS resolution

---

## Question 4: VPC Endpoints

Какой тип VPC Endpoint для S3 бесплатный?

A) Interface Endpoint

B) Gateway Endpoint

C) PrivateLink

D) Все платные

---

## Question 5: CIDR

Сколько IP адресов AWS резервирует в каждой подсети?

A) 2

B) 3

C) 5

D) 10

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Public subnet — это subnet с route 0.0.0.0/0 → Internet Gateway. |
| 2 | C | Security Groups stateful (ответы автоматически разрешены) и поддерживают только Allow rules. |
| 3 | B | NAT Gateway позволяет ресурсам в private subnet делать исходящие запросы в интернет. |
| 4 | B | Gateway Endpoints (S3, DynamoDB) бесплатны. Interface Endpoints платные. |
| 5 | C | AWS резервирует 5 IP: .0 (network), .1 (router), .2 (DNS), .3 (reserved), .255 (broadcast). |

---

