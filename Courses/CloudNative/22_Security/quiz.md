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

B) Минимальные необходимые permissions для выполнения задачи

C) Использование только AWS managed policies

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

C) Сканирует EC2 на уязвимости

D) Управляет firewall rules

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Клиент отвечает за "security IN the cloud": IAM, данные, encryption, network config. AWS — за "security OF the cloud". |
| 2 | B | Least Privilege: давать только те permissions, которые необходимы для выполнения конкретной задачи. |
| 3 | A | Secrets Manager имеет built-in rotation для RDS, Redshift, DocumentDB credentials. |
| 4 | B | WAF защищает от application-layer атак: SQL injection, XSS, OWASP Top 10. Shield — для DDoS. |
| 5 | B | GuardDuty анализирует CloudTrail, VPC Flow Logs, DNS logs для обнаружения угроз и аномалий. |

---
