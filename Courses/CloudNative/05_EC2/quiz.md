# Cloud Native Development - Quiz
## EC2: Elastic Compute Cloud

Проверьте свои знания по теме "EC2".

---

## Question 1: Instance Types


Что означает "m" в названии инстанса m5.xlarge?

A) Machine learning

B) Memory optimized

C) Micro instance

D) General purpose (balanced)

---

## Question 2: Graviton


Какое главное преимущество Graviton (ARM) инстансов?

A) Только для ML workloads

B) Только для Windows

C) Лучшее соотношение цена/производительность

D) Бесплатны в Free Tier

---

## Question 3: Spot Instances


Какова максимальная скидка на Spot Instances по сравнению с On-Demand?

A) До 30%

B) До 90%

C) До 50%

D) До 70%

---

## Question 4: EBS Types


Какой тип EBS volume рекомендуется для большинства workloads?

A) io2

B) st1

C) gp2

D) gp3

---

## Question 5: Auto Scaling


Что определяет Launch Template?

A) Health check интервал

B) Политики масштабирования

C) Количество инстансов в группе

D) Конфигурацию инстансов (AMI, type, user data)

---

## Question 6: Placement Groups


Какой тип Placement Group обеспечивает минимальную латентность?

A) Partition

B) Default

C) Spread

D) Cluster

---

## Question 7: Reserved Instances


На какой срок можно купить Reserved Instance?

A) 1 год или 3 года

B) 1 месяц или 1 год

C) Только 3 года

D) От 1 до 5 лет

---

## Question 8: Instance Metadata


По какому адресу доступен Instance Metadata Service?

A) http://169.254.169.254/latest/meta-data/

B) http://ec2.internal/metadata

C) http://aws.amazon.com/metadata

D) http://localhost/metadata

---

## Question 9: User Data


Когда выполняется User Data script?

A) Каждый час

B) Вручную администратором

C) При каждой перезагрузке

D) Только при первом запуске инстанса

---

## Question 10: AMI


Что НЕ включено в AMI?

A) Instance type

B) Операционная система

C) Конфигурация EBS

D) Установленное ПО

---

## Question 11: T-series Burstable


Как работает burstable performance в T-серии инстансов?

A) Подключается дополнительный CPU при нагрузке

B) CPU всегда работает на максимуме

C) Автоматически увеличивается размер инстанса

D) Накапливаются CPU credits, которые тратятся при высокой нагрузке

---

## Question 12: EBS Snapshots


Куда сохраняются EBS snapshots?

A) На другой EC2 инстанс

B) В Glacier

C) В S3 (managed AWS)

D) На тот же EBS volume

---

## Question 13: Security Groups


На каком уровне работают Security Groups для EC2?

A) На уровне региона

B) На уровне subnet

C) На уровне VPC

D) На уровне инстанса (ENI)

---

## Question 14: Savings Plans


Чем Compute Savings Plan отличается от EC2 Instance Savings Plan?

A) Ничем

B) EC2 Instance SP дешевле

C) Compute SP только для Lambda

D) Compute SP применяется к любым instance types и регионам

---

## Question 15: Auto Scaling Health Check


Какой тип health check рекомендуется при использовании ALB?

A) EC2

B) None

C) Custom

D) ELB

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | "M" означает General Purpose — сбалансированные ресурсы CPU и памяти. C = Compute, R = Memory, T = Burstable. |
| 2 | C | Graviton (ARM) инстансы обеспечивают до 40% лучшее price/performance по сравнению с x86 аналогами. |
| 3 | B | Spot Instances могут быть до 90% дешевле On-Demand, но могут быть прерваны. |
| 4 | D | gp3 рекомендуется вместо gp2 — позволяет настраивать IOPS и throughput независимо и стоит дешевле. |
| 5 | D | Launch Template определяет конфигурацию инстансов: AMI, instance type, security groups, user data и т.д. |
| 6 | D | Cluster Placement Group размещает все инстансы в одном rack, обеспечивая минимальную латентность (< 1ms). |
| 7 | A | Reserved Instances доступны на 1 год или 3 года. 3-летний срок даёт большую скидку. |
| 8 | A | IMDS доступен по адресу http://169.254.169.254/latest/meta-data/ изнутри инстанса. |
| 9 | D | User Data выполняется только при первом запуске инстанса (first boot). Для повторного выполнения нужны дополнительные настройки. |
| 10 | A | Instance type не включён в AMI. AMI содержит ОС, ПО, конфигурацию EBS, но размер выбирается при запуске. |
| 11 | D | T-инстансы накапливают CPU credits когда не используют полный CPU, и тратят их при burst нагрузке. |
| 12 | C | EBS snapshots хранятся в S3, управляемом AWS. Вы не видите их в своих S3 buckets. |
| 13 | D | Security Groups работают на уровне ENI (Elastic Network Interface), прикреплённого к инстансу. |
| 14 | D | Compute Savings Plan даёт гибкость: любой instance type, family, размер, регион, OS. EC2 Instance SP привязан к family в регионе. |
| 15 | D | При использовании ALB рекомендуется ELB health check — он проверяет реальную доступность приложения через target group. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете EC2. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Повторите pricing models и Auto Scaling. |
| **8-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про instance types и EBS. |
| **Менее 8 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

