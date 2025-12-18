# Cloud Native Development - Quiz
## EC2: Elastic Compute Cloud

Проверьте свои знания по теме "EC2".

---

## Question 1: Instance Types

Что означает "m" в названии инстанса m5.xlarge?

A) Memory optimized

B) Machine learning

C) Micro instance

D) General purpose (balanced)

---

## Question 2: Graviton

Какое главное преимущество Graviton (ARM) инстансов?

A) Бесплатны в Free Tier

B) Только для ML workloads

C) Лучшее соотношение цена/производительность

D) Только для Windows

---

## Question 3: Spot Instances

Какова максимальная скидка на Spot Instances по сравнению с On-Demand?

A) До 70%

B) До 90%

C) До 50%

D) До 30%

---

## Question 4: EBS Types

Какой тип EBS volume рекомендуется для большинства workloads?

A) gp3

B) io2

C) gp2

D) st1

---

## Question 5: Auto Scaling

Что определяет Launch Template?

A) Health check интервал

B) Политики масштабирования

C) Конфигурацию инстансов (AMI, type, user data)

D) Количество инстансов в группе

---

## Question 6: Placement Groups

Какой тип Placement Group обеспечивает минимальную латентность?

A) Spread

B) Default

C) Cluster

D) Partition

---

## Question 7: Reserved Instances

На какой срок можно купить Reserved Instance?

A) От 1 до 5 лет

B) Только 3 года

C) 1 месяц или 1 год

D) 1 год или 3 года

---

## Question 8: Instance Metadata

По какому адресу доступен Instance Metadata Service?

A) http://localhost/metadata

B) http://aws.amazon.com/metadata

C) http://ec2.internal/metadata

D) http://169.254.169.254/latest/meta-data/

---

## Question 9: User Data

Когда выполняется User Data script?

A) Вручную администратором

B) Каждый час

C) При каждой перезагрузке

D) Только при первом запуске инстанса

---

## Question 10: AMI

Что НЕ включено в AMI?

A) Конфигурация EBS

B) Операционная система

C) Instance type

D) Установленное ПО

---

## Question 11: T-series Burstable

Как работает burstable performance в T-серии инстансов?

A) Подключается дополнительный CPU при нагрузке

B) Автоматически увеличивается размер инстанса

C) CPU всегда работает на максимуме

D) Накапливаются CPU credits, которые тратятся при высокой нагрузке

---

## Question 12: EBS Snapshots

Куда сохраняются EBS snapshots?

A) На тот же EBS volume

B) На другой EC2 инстанс

C) В Glacier

D) В S3 (managed AWS)

---

## Question 13: Security Groups

На каком уровне работают Security Groups для EC2?

A) На уровне инстанса (ENI)

B) На уровне VPC

C) На уровне subnet

D) На уровне региона

---

## Question 14: Savings Plans

Чем Compute Savings Plan отличается от EC2 Instance Savings Plan?

A) Ничем

B) Compute SP применяется к любым instance types и регионам

C) EC2 Instance SP дешевле

D) Compute SP только для Lambda

---

## Question 15: Auto Scaling Health Check

Какой тип health check рекомендуется при использовании ALB?

A) Custom

B) None

C) ELB

D) EC2

---

## Question 16: Placement Groups

Какой placement group обеспечивает минимальную latency?

A) Partition

B) Spread

C) Default

D) Cluster

---

## Question 17: Instance Store

Что происходит с данными instance store при остановке EC2?

A) Сохраняются

B) Архивируются

C) Теряются

D) Переносятся в S3

---

## Question 18: Elastic IP

Сколько Elastic IP бесплатно на аккаунт?

A) 5 (если attached к running instance)

B) 1

C) 10

D) Неограниченно

---

## Question 19: Launch Template

Чем Launch Template лучше Launch Configuration?

A) Дешевле

B) Ничем

C) Работает быстрее

D) Поддерживает версионирование и mixing instance types

---

## Question 20: EC2 Hibernate

Что сохраняется при hibernate?

A) Только network state

B) RAM (в EBS), быстрый resume

C) Только диск

D) Ничего

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | "M" означает General Purpose — сбалансированные ресурсы CPU и памяти. C = Compute, R = Memory, T = Burstable. |
| 2 | C | Graviton (ARM) инстансы обеспечивают до 40% лучшее price/performance по сравнению с x86 аналогами. |
| 3 | B | Spot Instances могут быть до 90% дешевле On-Demand, но могут быть прерваны. |
| 4 | A | gp3 рекомендуется вместо gp2 — позволяет настраивать IOPS и throughput независимо и стоит дешевле. |
| 5 | C | Launch Template определяет конфигурацию инстансов: AMI, instance type, security groups, user data и т.д. |
| 6 | C | Cluster Placement Group размещает все инстансы в одном rack, обеспечивая минимальную латентность (< 1ms). |
| 7 | D | Reserved Instances доступны на 1 год или 3 года. 3-летний срок даёт большую скидку. |
| 8 | D | IMDS доступен по адресу http://169.254.169.254/latest/meta-data/ изнутри инстанса. |
| 9 | D | User Data выполняется только при первом запуске инстанса (first boot). Для повторного выполнения нужны дополнительные настройки. |
| 10 | C | Instance type не включён в AMI. AMI содержит ОС, ПО, конфигурацию EBS, но размер выбирается при запуске. |
| 11 | D | T-инстансы накапливают CPU credits когда не используют полный CPU, и тратят их при burst нагрузке. |
| 12 | D | EBS snapshots хранятся в S3, управляемом AWS. Вы не видите их в своих S3 buckets. |
| 13 | A | Security Groups работают на уровне ENI (Elastic Network Interface), прикреплённого к инстансу. |
| 14 | B | Compute Savings Plan даёт гибкость: любой instance type, family, размер, регион, OS. EC2 Instance SP привязан к family в регионе. |
| 15 | C | При использовании ALB рекомендуется ELB health check — он проверяет реальную доступность приложения через target group. |
| 16 | D | Cluster placement group минимизирует latency между instances |
| 17 | C | Instance store данные теряются при stop/terminate |
| 18 | A | 5 Elastic IP бесплатно если attached к running instance |
| 19 | D | Launch Template поддерживает версии и mixing instance types |
| 20 | B | Hibernate сохраняет RAM в EBS для быстрого resume |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете EC2. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Повторите pricing models и Auto Scaling. |
| **8-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про instance types и EBS. |
| **Менее 8 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---


