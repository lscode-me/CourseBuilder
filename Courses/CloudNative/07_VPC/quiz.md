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

A) Security Groups работают на уровне subnet

B) Security Groups stateful, поддерживают только Allow rules

C) NACLs применяются к отдельным инстансам

D) Security Groups stateless, NACLs stateful

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

A) 3

B) 2

C) 5

D) 10

---

## Question 6: NACL vs SG




Чем NACL отличается от Security Group?

A) Ничем

B) NACL stateful

C) NACL stateless, на уровне subnet, с Deny rules

D) Security Group на уровне VPC

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

A) Только Transit Gateway

B) Только Internet Gateway

C) Virtual Private Gateway + Customer Gateway

D) Только NAT Gateway

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

A) Шифрование трафика

B) Быстрее интернет

C) Private доступ к AWS сервисам без интернета

D) Публичный доступ к сервисам

---

## Question 14: Elastic Network Interface




Что такое ENI?

A) Load balancer

B) Тип storage

C) Виртуальная сетевая карта (с MAC, private IP, SG)

D) DNS сервис

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

A) Через DNS

B) Автоматически

C) Через firewall

D) Через route tables, associated с subnets

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

A) Для IPv4

B) Для исходящего IPv6 трафика без входящего

C) Для VPN

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

A) 5

B) 10

C) 100

D) Неограниченно

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Public subnet — это subnet с route 0.0.0.0/0 → Internet Gateway. |
| 2 | B | Security Groups stateful (ответы автоматически разрешены) и поддерживают только Allow rules. |
| 3 | A | NAT Gateway позволяет ресурсам в private subnet делать исходящие запросы в интернет. |
| 4 | A | Gateway Endpoints (S3, DynamoDB) бесплатны. Interface Endpoints платные. |
| 5 | C | AWS резервирует 5 IP: .0 (network), .1 (router), .2 (DNS), .3 (reserved), .255 (broadcast). |
| 6 | C | NACL stateless, на уровне subnet, поддерживает Deny rules |
| 7 | A | VPC Peering — private connectivity между VPCs |
| 8 | C | Transit Gateway для hub-and-spoke многих VPCs |
| 9 | B | Flow Logs записывают метаданные IP трафика |
| 10 | A | Bastion Host для безопасного SSH в private subnet |
| 11 | C | Site-to-Site VPN: VPG + Customer Gateway |
| 12 | A | Direct Connect — выделенное физическое соединение |
| 13 | C | PrivateLink — private доступ к сервисам |
| 14 | C | ENI — виртуальная сетевая карта |
| 15 | C | Secondary CIDR когда закончились IP |
| 16 | D | Routing через route tables associated с subnets |
| 17 | B | IPv6 — добавить IPv6 CIDR block к VPC |
| 18 | B | Egress-Only IGW для исходящего IPv6 без входящего |
| 19 | A | NACL правила по номеру, первое совпадение |
| 20 | A | Default лимит 5 VPC на регион |

---

