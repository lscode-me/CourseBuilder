# Cloud Native Development - Quiz
## Security

---

## Question 1: Shared Responsibility





За что отвечает КЛИЕНТ в Shared Responsibility Model?

A) IAM, шифрование данных, security groups

B) Hardware maintenance

C) Hypervisor patching

D) Физическая безопасность дата-центров

---

## Question 2: Least Privilege





Что означает принцип Least Privilege?

A) Запрет всех действий по умолчанию

B) Использование только AWS managed policies

C) Минимальные необходимые permissions для выполнения задачи

D) Минимум IAM пользователей

---

## Question 3: Secrets Management





Какой сервис рекомендуется для хранения database credentials с автоматической ротацией?

A) Secrets Manager

B) IAM

C) KMS

D) Parameter Store Standard

---

## Question 4: WAF





Какие атаки защищает WAF?

A) DDoS на сетевом уровне

B) SQL injection, XSS, application-layer attacks

C) Malware на EC2

D) Brute force на SSH

---

## Question 5: GuardDuty





Что делает GuardDuty?

A) Шифрует данные

B) Обнаруживает угрозы и подозрительную активность

C) Управляет firewall rules

D) Сканирует EC2 на уязвимости

---

## Question 6: Inspector




Что делает AWS Inspector?

A) Мониторит costs

B) Автоматический vulnerability scanning для EC2 и containers

C) Управляет IAM

D) Шифрует данные

---

## Question 7: Security Hub




Для чего используется Security Hub?

A) Только для IAM

B) Только для encryption

C) Только для logging

D) Централизованный security dashboard и findings aggregation

---

## Question 8: Macie




Что обнаруживает Amazon Macie?

A) Sensitive data (PII) в S3 buckets

B) DDoS attacks

C) SQL injection

D) Malware

---

## Question 9: KMS




Какие типы ключей в KMS?

A) Только symmetric

B) Только Customer managed

C) AWS managed, Customer managed, Customer provided

D) Только AWS managed

---

## Question 10: CloudTrail




Что логирует CloudTrail?

A) Только errors

B) API calls и management events в AWS account

C) Только S3

D) Только EC2

---

## Question 11: IAM Access Analyzer




Что делает IAM Access Analyzer?

A) Создаёт IAM roles

B) Мониторит costs

C) Удаляет старые роли

D) Находит ресурсы shared с external entities

---

## Question 12: Config Rules




Для чего используются AWS Config Rules?

A) Для continuous compliance checking resources

B) Для deployment

C) Для logging

D) Для billing

---

## Question 13: Network Firewall




Когда использовать AWS Network Firewall?

A) Для application layer

B) Для network-level filtering, IDS/IPS

C) Для DDoS

D) Для API protection

---

## Question 14: Shield Advanced




Что даёт Shield Advanced по сравнению со Standard?

A) DDoS cost protection, 24/7 DRT, advanced mitigation

B) Ничего

C) Только metrics

D) Только logging

---

## Question 15: IAM Policies




Какие типы IAM policies существуют?

A) Только custom

B) Identity-based, Resource-based, Permissions boundaries, SCPs

C) Только inline

D) Только managed

---

## Question 16: SCP




Что делают Service Control Policies в Organizations?

A) Ограничивают permissions во всех accounts organization

B) Создают ресурсы

C) Только для logging

D) Только для billing

---

## Question 17: Private CA




Для чего используется AWS Private CA?

A) Для public certificates

B) Для private PKI и internal certificates

C) Для SSH keys

D) Для API keys

---

## Question 18: Firewall Manager




Что делает AWS Firewall Manager?

A) Только для SGs

B) Создаёт firewalls

C) Centralized management security policies across accounts

D) Только для WAF

---

## Question 19: Detective




Что делает Amazon Detective?

A) Создаёт alerts

B) Только monitoring

C) Только logging

D) Investigates security findings с graph analysis

---

## Question 20: Zero Trust




Как реализовать Zero Trust в AWS?

A) IAM, Verified Access, private endpoints, encryption everywhere

B) VPN только

C) Shield только

D) Firewall только

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Клиент отвечает за "security IN the cloud": IAM, данные, encryption, network config. AWS — за "security OF the cloud". |
| 2 | C | Least Privilege: давать только те permissions, которые необходимы для выполнения конкретной задачи. |
| 3 | A | Secrets Manager имеет built-in rotation для RDS, Redshift, DocumentDB credentials. |
| 4 | B | WAF защищает от application-layer атак: SQL injection, XSS, OWASP Top 10. Shield — для DDoS. |
| 5 | B | GuardDuty анализирует CloudTrail, VPC Flow Logs, DNS logs для обнаружения угроз и аномалий. |
| 6 | B | Inspector: vulnerability scanning |
| 7 | D | Security Hub: centralized dashboard |
| 8 | A | Macie: PII detection в S3 |
| 9 | C | KMS: AWS managed, Customer managed, Customer provided |
| 10 | B | CloudTrail: API calls и events |
| 11 | D | Access Analyzer: finds external sharing |
| 12 | A | Config Rules: continuous compliance |
| 13 | B | Network Firewall: network-level IDS/IPS |
| 14 | A | Shield Advanced: DDoS cost protection, DRT |
| 15 | B | Identity, Resource, Boundaries, SCPs policies |
| 16 | A | SCPs: ограничения для всей organization |
| 17 | B | Private CA: internal certificates |
| 18 | C | Firewall Manager: centralized security policies |
| 19 | D | Detective: investigates with graph analysis |
| 20 | A | Zero Trust: IAM, Verified Access, private endpoints |

---
