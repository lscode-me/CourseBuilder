# Cloud Native Development - Quiz
## EC2: Elastic Compute Cloud

Проверьте свои знания по теме "EC2".

---

## Question 1: Instance Types

Что означает "m" в названии инстанса m5.xlarge?

A) Memory optimized

B) General purpose (balanced)

C) Machine learning

D) Micro instance

---

## Question 2: Graviton

Какое главное преимущество Graviton (ARM) инстансов?

A) Только для ML workloads

B) Лучшее соотношение цена/производительность

C) Только для Windows

D) Бесплатны в Free Tier

---

## Question 3: Spot Instances

Какова максимальная скидка на Spot Instances по сравнению с On-Demand?

A) До 30%

B) До 50%

C) До 70%

D) До 90%

---

## Question 4: EBS Types

Какой тип EBS volume рекомендуется для большинства workloads?

A) gp2

B) gp3

C) io2

D) st1

---

## Question 5: Auto Scaling

Что определяет Launch Template?

A) Количество инстансов в группе

B) Конфигурацию инстансов (AMI, type, user data)

C) Политики масштабирования

D) Health check интервал

---

## Question 6: Placement Groups

Какой тип Placement Group обеспечивает минимальную латентность?

A) Spread

B) Partition

C) Cluster

D) Default

---

## Question 7: Reserved Instances

На какой срок можно купить Reserved Instance?

A) 1 месяц или 1 год

B) 1 год или 3 года

C) Только 3 года

D) От 1 до 5 лет

---

## Question 8: Instance Metadata

По какому адресу доступен Instance Metadata Service?

A) http://localhost/metadata

B) http://169.254.169.254/latest/meta-data/

C) http://aws.amazon.com/metadata

D) http://ec2.internal/metadata

---

## Question 9: User Data

Когда выполняется User Data script?

A) При каждой перезагрузке

B) Только при первом запуске инстанса

C) Вручную администратором

D) Каждый час

---

## Question 10: AMI

Что НЕ включено в AMI?

A) Операционная система

B) Установленное ПО

C) Instance type

D) Конфигурация EBS

---

## Question 11: T-series Burstable

Как работает burstable performance в T-серии инстансов?

A) CPU всегда работает на максимуме

B) Накапливаются CPU credits, которые тратятся при высокой нагрузке

C) Автоматически увеличивается размер инстанса

D) Подключается дополнительный CPU при нагрузке

---

## Question 12: EBS Snapshots

Куда сохраняются EBS snapshots?

A) На тот же EBS volume

B) В S3 (managed AWS)

C) В Glacier

D) На другой EC2 инстанс

---

## Question 13: Security Groups

На каком уровне работают Security Groups для EC2?

A) На уровне VPC

B) На уровне subnet

C) На уровне инстанса (ENI)

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

A) EC2

B) ELB

C) Custom

D) None

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | "M" означает General Purpose — сбалансированные ресурсы CPU и памяти. C = Compute, R = Memory, T = Burstable. |
| 2 | B | Graviton (ARM) инстансы обеспечивают до 40% лучшее price/performance по сравнению с x86 аналогами. |
| 3 | D | Spot Instances могут быть до 90% дешевле On-Demand, но могут быть прерваны. |
| 4 | B | gp3 рекомендуется вместо gp2 — позволяет настраивать IOPS и throughput независимо и стоит дешевле. |
| 5 | B | Launch Template определяет конфигурацию инстансов: AMI, instance type, security groups, user data и т.д. |
| 6 | C | Cluster Placement Group размещает все инстансы в одном rack, обеспечивая минимальную латентность (< 1ms). |
| 7 | B | Reserved Instances доступны на 1 год или 3 года. 3-летний срок даёт большую скидку. |
| 8 | B | IMDS доступен по адресу http://169.254.169.254/latest/meta-data/ изнутри инстанса. |
| 9 | B | User Data выполняется только при первом запуске инстанса (first boot). Для повторного выполнения нужны дополнительные настройки. |
| 10 | C | Instance type не включён в AMI. AMI содержит ОС, ПО, конфигурацию EBS, но размер выбирается при запуске. |
| 11 | B | T-инстансы накапливают CPU credits когда не используют полный CPU, и тратят их при burst нагрузке. |
| 12 | B | EBS snapshots хранятся в S3, управляемом AWS. Вы не видите их в своих S3 buckets. |
| 13 | C | Security Groups работают на уровне ENI (Elastic Network Interface), прикреплённого к инстансу. |
| 14 | B | Compute Savings Plan даёт гибкость: любой instance type, family, размер, регион, OS. EC2 Instance SP привязан к family в регионе. |
| 15 | B | При использовании ALB рекомендуется ELB health check — он проверяет реальную доступность приложения через target group. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете EC2. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Повторите pricing models и Auto Scaling. |
| **8-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про instance types и EBS. |
| **Менее 8 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

