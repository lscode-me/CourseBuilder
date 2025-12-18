# Cloud Native Development - Quiz
## VPC: Virtual Private Cloud

---

## Question 1: Что делает подсеть "public"?

A) Имеет route к Internet Gateway в route table

B) Находится в первой AZ

C) Не имеет Security Groups

D) Использует публичные IP адреса

---

## Question 2: Security Groups vs NACLs

Какое утверждение ВЕРНО?

A) Security Groups работают на уровне subnet

B) Security Groups stateful, поддерживают только Allow rules

C) NACLs применяются к отдельным инстансам

D) Security Groups stateless, NACLs stateful

---

## Question 3: NAT Gateway

Для чего нужен NAT Gateway?

A) Для DNS resolution

B) Для входящего трафика в private subnet

C) Для исходящего интернет-трафика из private subnet

D) Для связи между VPC

---

## Question 4: VPC Endpoints

Какой тип VPC Endpoint для S3 бесплатный?

A) Все платные

B) Gateway Endpoint

C) PrivateLink

D) Interface Endpoint

---

## Question 5: CIDR

Сколько IP адресов AWS резервирует в каждой подсети?

A) 3

B) 2

C) 5

D) 10

---

## Question 6: NACL vs SG

Чем NACL отличается от Security Group?

A) NACL stateless, на уровне subnet, с Deny rules

B) Security Group на уровне VPC

C) Ничем

D) NACL stateful

---

## Question 7: VPC Peering

Что позволяет VPC Peering?

A) Private connectivity между VPCs (включая cross-region)

B) Только в одном регионе

C) Только для EC2

D) Автоматический routing

---

## Question 8: Transit Gateway

Когда использовать Transit Gateway вместо VPC Peering?

A) Для 2 VPCs

B) Для одного VPC

C) Для hub-and-spoke connectivity многих VPCs и on-premises

D) Transit Gateway устарел

---

## Question 9: Flow Logs

Что записывают VPC Flow Logs?

A) Содержимое трафика

B) Метаданные IP трафика (source/dest IP, ports, action)

C) Только DNS запросы

D) Только errors

---

## Question 10: Bastion Host

Для чего используется Bastion Host?

A) Для безопасного SSH доступа в private subnet

B) Для балансировки нагрузки

C) Для DNS

D) Для хранения данных

---

## Question 11: VPN

Какие компоненты нужны для Site-to-Site VPN?

A) Virtual Private Gateway + Customer Gateway

B) Только NAT Gateway

C) Только Transit Gateway

D) Только Internet Gateway

---

## Question 12: Direct Connect

Что такое AWS Direct Connect?

A) Выделенное физическое соединение к AWS

B) VPN соединение

C) Тип EC2

D) Интернет соединение

---

## Question 13: PrivateLink

Что обеспечивает AWS PrivateLink?

A) Быстрее интернет

B) Шифрование трафика

C) Публичный доступ к сервисам

D) Private доступ к AWS сервисам без интернета

---

## Question 14: Elastic Network Interface

Что такое ENI?

A) Виртуальная сетевая карта (с MAC, private IP, SG)

B) DNS сервис

C) Load balancer

D) Тип storage

---

## Question 15: Secondary CIDR

Когда добавляют secondary CIDR в VPC?

A) Никогда не нужно

B) Для шифрования

C) Когда закончились IP адреса в primary CIDR

D) Для DNS

---

## Question 16: Route Tables

Как работает routing в VPC?

A) Через route tables, associated с subnets

B) Через firewall

C) Автоматически

D) Через DNS

---

## Question 17: IPv6

Как включить IPv6 в VPC?

A) Автоматически включён

B) Добавить IPv6 CIDR block к VPC

C) Невозможно

D) Только в US regions

---

## Question 18: Egress-Only Internet Gateway

Для чего используется Egress-Only IGW?

A) Для VPN

B) Для IPv4

C) Для исходящего IPv6 трафика без входящего

D) Для S3

---

## Question 19: Network ACL Order

Как обрабатываются правила NACL?

A) По номеру правила (от низшего к высшему), первое совпадение

B) Случайно

C) По алфавиту

D) Все правила вместе

---

## Question 20: VPC Limits

Какой лимит VPC на регион по умолчанию?

A) 100

B) 5

C) 10

D) Неограниченно

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Public subnet — это subnet с route 0.0.0.0/0 → Internet Gateway. |
| 2 | B | Security Groups stateful (ответы автоматически разрешены) и поддерживают только Allow rules. |
| 3 | C | NAT Gateway позволяет ресурсам в private subnet делать исходящие запросы в интернет. |
| 4 | B | Gateway Endpoints (S3, DynamoDB) бесплатны. Interface Endpoints платные. |
| 5 | C | AWS резервирует 5 IP: .0 (network), .1 (router), .2 (DNS), .3 (reserved), .255 (broadcast). |
| 6 | A | NACL stateless, на уровне subnet, поддерживает Deny rules |
| 7 | A | VPC Peering — private connectivity между VPCs |
| 8 | C | Transit Gateway для hub-and-spoke многих VPCs |
| 9 | B | Flow Logs записывают метаданные IP трафика |
| 10 | A | Bastion Host для безопасного SSH в private subnet |
| 11 | A | Site-to-Site VPN: VPG + Customer Gateway |
| 12 | A | Direct Connect — выделенное физическое соединение |
| 13 | D | PrivateLink — private доступ к сервисам |
| 14 | A | ENI — виртуальная сетевая карта |
| 15 | C | Secondary CIDR когда закончились IP |
| 16 | A | Routing через route tables associated с subnets |
| 17 | B | IPv6 — добавить IPv6 CIDR block к VPC |
| 18 | C | Egress-Only IGW для исходящего IPv6 без входящего |
| 19 | A | NACL правила по номеру, первое совпадение |
| 20 | B | Default лимит 5 VPC на регион |

---


