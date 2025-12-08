# Cloud Native Development - Quiz
## Security

---

## Question 1: Shared Responsibility

За что отвечает КЛИЕНТ в Shared Responsibility Model?

A) Физическая безопасность дата-центров
B) IAM, шифрование данных, security groups
C) Hypervisor patching
D) Hardware maintenance

---

## Question 2: Least Privilege

Что означает принцип Least Privilege?

A) Минимум IAM пользователей
B) Минимальные необходимые permissions для выполнения задачи
C) Использование только AWS managed policies
D) Запрет всех действий по умолчанию

---

## Question 3: Secrets Management

Какой сервис рекомендуется для хранения database credentials с автоматической ротацией?

A) Parameter Store Standard
B) Secrets Manager
C) KMS
D) IAM

---

## Question 4: WAF

Какие атаки защищает WAF?

A) DDoS на сетевом уровне
B) SQL injection, XSS, application-layer attacks
C) Brute force на SSH
D) Malware на EC2

---

## Question 5: GuardDuty

Что делает GuardDuty?

A) Сканирует EC2 на уязвимости
B) Обнаруживает угрозы и подозрительную активность
C) Управляет firewall rules
D) Шифрует данные

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Клиент отвечает за "security IN the cloud": IAM, данные, encryption, network config. AWS — за "security OF the cloud". |
| 2 | B | Least Privilege: давать только те permissions, которые необходимы для выполнения конкретной задачи. |
| 3 | B | Secrets Manager имеет built-in rotation для RDS, Redshift, DocumentDB credentials. |
| 4 | B | WAF защищает от application-layer атак: SQL injection, XSS, OWASP Top 10. Shield — для DDoS. |
| 5 | B | GuardDuty анализирует CloudTrail, VPC Flow Logs, DNS logs для обнаружения угроз и аномалий. |

---
