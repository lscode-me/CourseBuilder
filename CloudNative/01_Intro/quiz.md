# Cloud Native Development - Quiz
## Введение в облачные вычисления

Проверьте свои знания по теме "Введение в облачные вычисления".

---

## Question 1: Характеристики облака по NIST


Какая из перечисленных характеристик НЕ является одной из пяти ключевых характеристик облачных вычислений по определению NIST?

A) Guaranteed 99.99% uptime

B) Broad network access

C) Measured service

D) On-demand self-service

---

## Question 2: История AWS


В каком году Amazon запустил первые публичные облачные сервисы (S3 и EC2)?

A) 2008

B) 2006

C) 2002

D) 2004

---

## Question 3: Преимущества облака


Какое из утверждений лучше всего описывает переход от CapEx к OpEx при использовании облака?

A) Капитальные затраты на оборудование заменяются операционными расходами по факту использования

B) Компании должны покупать оборудование, но могут использовать его в облаке

C) Операционные расходы полностью исчезают

D) Компании тратят больше денег, но получают лучший сервис

---

## Question 4: Доля рынка


Какой облачный провайдер имеет наибольшую долю рынка облачной инфраструктуры (по состоянию на 2024 год)?

A) Google Cloud Platform

B) Amazon Web Services

C) Microsoft Azure

D) Alibaba Cloud

---

## Question 5: Vendor Lock-in


Какой сервис AWS создаёт НАИБОЛЬШИЙ риск vendor lock-in из-за отсутствия прямых аналогов у других провайдеров?

A) RDS PostgreSQL (управляемая БД)

B) DynamoDB (NoSQL база данных)

C) S3-compatible storage

D) EC2 (виртуальные машины)

---

## Question 6: Deployment Models


Компания хочет хранить персональные данные клиентов в собственном дата-центре из-за требований регулятора, но использовать облако для обработки обезличенных данных. Какая модель развёртывания им подходит?

A) Private Cloud

B) Community Cloud

C) Hybrid Cloud

D) Public Cloud

---

## Question 7: Well-Architected Framework


Сколько столпов (pillars) в AWS Well-Architected Framework?

A) 6

B) 5

C) 4

D) 7

---

## Question 8: Well-Architected Pillars


Какой столп AWS Well-Architected Framework отвечает за принцип "Stop spending money on undifferentiated heavy lifting"?

A) Security

B) Performance Efficiency

C) Operational Excellence

D) Cost Optimization

---

## Question 9: История облаков


Какая компания первой предложила модель SaaS (Software as a Service) в современном понимании?

A) Amazon

B) Google

C) Salesforce

D) Microsoft

---

## Question 10: Elasticity vs Scalability


Чем эластичность (elasticity) отличается от масштабируемости (scalability)?

A) Масштабируемость только для уменьшения ресурсов

B) Эластичность требует ручного вмешательства

C) Это одно и то же

D) Эластичность — возможность автоматически масштабироваться вверх И вниз в зависимости от нагрузки

---

## Question 11: Resource Pooling


Что означает характеристика "Resource pooling" в определении облака?

A) Клиенты должны объединяться в группы для использования облака

B) Ресурсы провайдера объединены для обслуживания множества клиентов (multi-tenant)

C) Данные всех клиентов хранятся в одном месте без изоляции

D) Каждый клиент получает выделенные физические серверы

---

## Question 12: Выбор провайдера


Для какого сценария Google Cloud Platform будет наиболее подходящим выбором?

A) Государственная организация США с требованиями FedRAMP High

B) Компания с focus на Big Data и Machine Learning workloads

C) Стартап, которому нужен максимальный выбор managed services

D) Enterprise с existing Microsoft Active Directory

---

## Question 13: TCO Calculation


При расчёте TCO (Total Cost of Ownership) для миграции в облако, какой фактор часто НЕДООЦЕНИВАЮТ?

A) Стоимость поддержки AWS Support

B) Стоимость хранения данных

C) Стоимость compute ресурсов

D) Стоимость исходящего трафика (data transfer out)

---

## Question 14: Security Responsibility


В модели Shared Responsibility, за что отвечает КЛИЕНТ при использовании EC2?

A) Настройка Security Groups и патчинг ОС внутри инстанса

B) Безопасность глобальной сети AWS

C) Патчинг гипервизора

D) Физическая безопасность дата-центров

---

## Question 15: AWS CLI


Какая команда AWS CLI показывает информацию о текущих credentials (кто вы)?

A) `aws whoami`

B) `aws iam get-user`

C) `aws configure list`

D) `aws sts get-caller-identity`

---

## Question 16: Free Tier


Что из перечисленного НЕ входит в AWS Free Tier (12 месяцев)?

A) Unlimited data transfer between regions

B) 750 часов EC2 t2.micro в месяц

C) 25 GB DynamoDB storage

D) 5 GB S3 storage

---

## Question 17: Multi-Cloud Strategy


Какая основная причина для использования multi-cloud стратегии?

A) Снижение риска vendor lock-in и повышение отказоустойчивости

B) Multi-cloud проще в управлении

C) AWS требует использовать другие облака

D) Всегда дешевле использовать несколько провайдеров

---

## Question 18: Принципы облака


Какой принцип Well-Architected Framework рекомендует "Make frequent, small, reversible changes"?

A) Operational Excellence

B) Cost Optimization

C) Security

D) Reliability

---

## Question 19: AWS Regions


Почему AWS имеет несколько регионов по всему миру?

A) Регионы нужны только enterprise клиентам

B) Потому что один регион не может вместить всех клиентов

C) Для снижения latency, compliance, и disaster recovery

D) Только для соблюдения законодательства о данных

---

## Question 20: Первые шаги


Какое действие рекомендуется выполнить ПЕРВЫМ после создания нового AWS аккаунта?

A) Запустить EC2 инстанс

B) Включить MFA на root аккаунте и создать IAM пользователя для повседневной работы

C) Создать S3 bucket для хранения данных

D) Настроить VPC с публичными подсетями

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | NIST определяет 5 характеристик: on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service. Guaranteed uptime не является характеристикой по определению. |
| 2 | B | Amazon запустил S3 в марте 2006 и EC2 в августе 2006 года. |
| 3 | A | CapEx (капитальные затраты на оборудование) заменяются OpEx (операционные расходы) — платите только за использованные ресурсы. |
| 4 | B | AWS лидирует с долей ~32% рынка, Azure ~23%, GCP ~11%. |
| 5 | B | DynamoDB — уникальный NoSQL сервис без прямых аналогов. EC2 и S3 имеют совместимые альтернативы, RDS PostgreSQL — стандартная технология. |
| 6 | C | Hybrid Cloud позволяет комбинировать on-premise (для регулируемых данных) и public cloud (для обработки). |
| 7 | A | Well-Architected Framework имеет 6 столпов: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability. |
| 8 | D | Cost Optimization включает принцип не тратить деньги на "undifferentiated heavy lifting" — использовать managed services. |
| 9 | C | Salesforce запустила CRM как SaaS в 1999 году, став пионером этой модели. |
| 10 | D | Elasticity — способность автоматически масштабироваться ВВЕРХ при росте нагрузки и ВНИЗ при её снижении. Scalability — способность расти, но не обязательно автоматически или уменьшаться. |
| 11 | B | Resource pooling означает, что физические ресурсы провайдера разделяются между множеством клиентов (multi-tenancy) с изоляцией на логическом уровне. |
| 12 | B | GCP силён в Big Data (BigQuery) и ML (Vertex AI, TPU). Azure лучше для Microsoft стека, AWS — для breadth of services. |
| 13 | D | Data transfer out (исходящий трафик) часто недооценивают. AWS берёт ~$0.09/GB, что может составить значительную сумму при больших объёмах. |
| 14 | A | В Shared Responsibility клиент отвечает за security "in the cloud" — настройку Security Groups, патчинг ОС, управление доступом. AWS отвечает за security "of the cloud". |
| 15 | D | `aws sts get-caller-identity` показывает UserId, Account и ARN текущего principal. |
| 16 | A | Data transfer between regions платный. Free Tier включает: 750 hrs EC2, 5GB S3, 25GB DynamoDB, но не unlimited cross-region transfer. |
| 17 | A | Multi-cloud снижает зависимость от одного провайдера и повышает отказоустойчивость (DR в другом облаке). Это НЕ проще и не всегда дешевле. |
| 18 | A | "Make frequent, small, reversible changes" — принцип Operational Excellence для снижения риска и быстрого восстановления. |
| 19 | C | Регионы нужны для: низкой latency (близость к пользователям), compliance (данные в определённой юрисдикции), disaster recovery (географическое распределение). |
| 20 | B | Security first: включить MFA на root, создать IAM пользователя с нужными permissions. Никогда не использовать root для повседневной работы. |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили основы облачных вычислений. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы Well-Architected Framework и TCO. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы про историю облаков и модели развёртывания. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно разделы про характеристики NIST и преимущества облаков. |

---

