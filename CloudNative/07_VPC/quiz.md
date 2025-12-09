# Cloud Native Development - Quiz
## VPC: Virtual Private Cloud

---

## Question 1: Что делает подсеть "public"?


A) Не имеет Security Groups

B) Имеет route к Internet Gateway в route table

C) Находится в первой AZ

D) Использует публичные IP адреса

---

## Question 2: Security Groups vs NACLs


Какое утверждение ВЕРНО?

A) Security Groups stateless, NACLs stateful

B) NACLs применяются к отдельным инстансам

C) Security Groups stateful, поддерживают только Allow rules

D) Security Groups работают на уровне subnet

---

## Question 3: NAT Gateway


Для чего нужен NAT Gateway?

A) Для исходящего интернет-трафика из private subnet

B) Для входящего трафика в private subnet

C) Для связи между VPC

D) Для DNS resolution

---

## Question 4: VPC Endpoints


Какой тип VPC Endpoint для S3 бесплатный?

A) Gateway Endpoint

B) PrivateLink

C) Все платные

D) Interface Endpoint

---

## Question 5: CIDR


Сколько IP адресов AWS резервирует в каждой подсети?

A) 5

B) 10

C) 3

D) 2

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Public subnet — это subnet с route 0.0.0.0/0 → Internet Gateway. |
| 2 | C | Security Groups stateful (ответы автоматически разрешены) и поддерживают только Allow rules. |
| 3 | A | NAT Gateway позволяет ресурсам в private subnet делать исходящие запросы в интернет. |
| 4 | A | Gateway Endpoints (S3, DynamoDB) бесплатны. Interface Endpoints платные. |
| 5 | A | AWS резервирует 5 IP: .0 (network), .1 (router), .2 (DNS), .3 (reserved), .255 (broadcast). |

---

