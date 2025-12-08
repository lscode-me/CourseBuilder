# Cloud Native Development - Quiz
## IAM: Identity and Access Management

Проверьте свои знания по теме "IAM".

---

## Question 1: IAM Scope

Какой scope имеет IAM в AWS?

A) Региональный (отдельный для каждого региона)

B) Глобальный (один для всего аккаунта)

C) Зависит от типа ресурса

D) Привязан к VPC

---

## Question 2: IAM Entities

Какой IAM entity предназначен для предоставления временных credentials сервисам AWS?

A) IAM User

B) IAM Group

C) IAM Role

D) IAM Policy

---

## Question 3: Policy Evaluation

Если у пользователя есть политика с Allow на s3:*, а на S3 bucket есть политика с Deny на s3:GetObject, что произойдёт при запросе GetObject?

A) Allow (identity policy побеждает)

B) Deny (explicit deny всегда побеждает)

C) Зависит от порядка создания политик

D) Ошибка конфликта политик

---

## Question 4: Best Practice для Users

Какой подход к назначению политик пользователям считается best practice?

A) Прикреплять политики напрямую к каждому пользователю

B) Использовать inline политики

C) Добавлять пользователей в группы и назначать политики группам

D) Давать всем пользователям AdministratorAccess

---

## Question 5: Root Account

Для каких действий рекомендуется использовать root account?

A) Повседневное администрирование

B) Создание EC2 инстансов

C) Закрытие аккаунта и восстановление IAM admin доступа

D) Запуск Lambda функций

---

## Question 6: Trust Policy

Что определяет Trust Policy роли?

A) Какие действия разрешены роли

B) Какие ресурсы может использовать роль

C) Кто может принять (assume) эту роль

D) Как долго действуют credentials роли

---

## Question 7: MFA Condition

Какое условие в политике требует наличия MFA?

A) `"aws:MFARequired": "true"`

B) `"aws:MultiFactorAuthPresent": "true"`

C) `"iam:MFAEnabled": "true"`

D) `"aws:SecureTransport": "true"`

---

## Question 8: Cross-Account Access

Как предоставить пользователю из аккаунта A доступ к ресурсам в аккаунте B?

A) Создать IAM пользователя в аккаунте B с такими же credentials

B) Создать роль в аккаунте B с Trust Policy для аккаунта A

C) Использовать один и тот же access key в обоих аккаунтах

D) Cross-account доступ невозможен в AWS

---

## Question 9: Policy Elements

Какой элемент политики определяет "на каких ресурсах" применяется правило?

A) Action

B) Effect

C) Resource

D) Principal

---

## Question 10: AssumeRole

Какой AWS сервис используется для получения временных credentials через AssumeRole?

A) IAM

B) STS (Security Token Service)

C) Cognito

D) Directory Service

---

## Question 11: AWS Managed Policies

Какое преимущество AWS Managed Policies?

A) Можно редактировать их содержимое

B) Автоматически обновляются AWS при появлении новых сервисов

C) Работают быстрее customer managed policies

D) Не учитываются в лимитах политик

---

## Question 12: Instance Profile

Для чего нужен Instance Profile?

A) Для хранения профиля пользователя EC2

B) Для связи IAM Role с EC2 инстансом

C) Для настройки сетевого профиля

D) Для мониторинга производительности

---

## Question 13: Permission Boundary

Что делает Permission Boundary?

A) Даёт дополнительные разрешения

B) Ограничивает максимальные разрешения, которые может получить entity

C) Определяет границы VPC

D) Устанавливает лимиты на количество политик

---

## Question 14: Service Control Policies

Где применяются Service Control Policies (SCPs)?

A) К отдельным IAM пользователям

B) К IAM группам

C) К AWS Organizations (аккаунтам и OU)

D) К EC2 инстансам

---

## Question 15: OIDC Federation

Какой use case подходит для OIDC Federation?

A) Аутентификация сотрудников через корпоративный Active Directory

B) Предоставление временных credentials для GitHub Actions

C) Создание постоянных IAM пользователей

D) Шифрование данных

---

## Question 16: Policy Version

Какую версию следует указывать в IAM политиках?

A) "2008-10-17"

B) "2012-10-17"

C) "2024-01-01"

D) Версия не обязательна

---

## Question 17: Implicit Deny

Что такое Implicit Deny в IAM?

A) Явный запрет в политике

B) Отсутствие разрешения автоматически означает запрет

C) Запрет, унаследованный от группы

D) Временный запрет

---

## Question 18: Access Analyzer

Для чего используется IAM Access Analyzer?

A) Анализ производительности IAM

B) Поиск ресурсов, доступных извне аккаунта, и генерация минимальных политик

C) Управление access keys

D) Мониторинг стоимости IAM

---

## Question 19: Условия в политиках

Какое условие ограничивает доступ по IP-адресу?

A) `StringEquals`

B) `IpAddress`

C) `NetworkAddress`

D) `SourceIP`

---

## Question 20: IAM Identity Center

Что такое AWS IAM Identity Center (ранее AWS SSO)?

A) Сервис для создания IAM пользователей

B) Централизованное управление доступом к нескольким AWS аккаунтам

C) Сервис для шифрования

D) Альтернатива IAM

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | IAM — глобальный сервис. Пользователи, роли и политики доступны во всех регионах аккаунта. |
| 2 | C | IAM Role предоставляет временные credentials и может быть assumed сервисами AWS, пользователями или внешними identity. |
| 3 | B | Explicit Deny всегда побеждает. Если где-либо есть Deny — доступ запрещён, независимо от Allow в других политиках. |
| 4 | C | Best practice — организовывать пользователей в группы и назначать политики группам. Это упрощает управление. |
| 5 | C | Root account следует использовать только для задач, требующих root: закрытие аккаунта, изменение support plan, восстановление доступа. |
| 6 | C | Trust Policy определяет Principal, который может assume роль (например, ec2.amazonaws.com или другой аккаунт). |
| 7 | B | Условие `"aws:MultiFactorAuthPresent": "true"` требует, чтобы пользователь прошёл MFA аутентификацию. |
| 8 | B | Для cross-account доступа создаётся роль в целевом аккаунте с Trust Policy, разрешающей assume из исходного аккаунта. |
| 9 | C | Resource определяет ARN ресурсов, к которым применяется правило. Action — действия, Effect — Allow/Deny. |
| 10 | B | AWS STS (Security Token Service) отвечает за выдачу временных credentials через AssumeRole, AssumeRoleWithSAML и т.д. |
| 11 | B | AWS Managed Policies автоматически обновляются AWS при добавлении новых сервисов или действий. |
| 12 | B | Instance Profile — контейнер для IAM Role, который позволяет прикрепить роль к EC2 инстансу. |
| 13 | B | Permission Boundary ограничивает максимальные разрешения entity. Даже если политика даёт больше прав, boundary их урежет. |
| 14 | C | SCPs применяются в AWS Organizations к аккаунтам и Organizational Units для ограничения разрешений на уровне организации. |
| 15 | B | OIDC Federation идеально подходит для CI/CD систем (GitHub Actions, GitLab) для получения временных credentials без хранения секретов. |
| 16 | B | Всегда используйте версию "2012-10-17" — это актуальная версия языка политик с полной функциональностью. |
| 17 | B | Implicit Deny означает, что если нет явного Allow для действия, оно автоматически запрещено. |
| 18 | B | IAM Access Analyzer находит ресурсы, доступные извне аккаунта, и может генерировать минимальные политики на основе CloudTrail. |
| 19 | B | Условие `IpAddress` с ключом `aws:SourceIp` ограничивает доступ по IP-адресу источника запроса. |
| 20 | B | IAM Identity Center — централизованный сервис для управления доступом пользователей к нескольким AWS аккаунтам через единый портал. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете IAM. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Policy Evaluation Logic и Permission Boundaries. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы про роли и политики. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно про структуру политик. |

---

