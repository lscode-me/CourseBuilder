# Cloud Native Development - Quiz
## IAM: Identity and Access Management

Проверьте свои знания по теме "IAM".

---

## Question 1: IAM Scope


Какой scope имеет IAM в AWS?

A) Глобальный (один для всего аккаунта)

B) Зависит от типа ресурса

C) Привязан к VPC

D) Региональный (отдельный для каждого региона)

---

## Question 2: IAM Entities


Какой IAM entity предназначен для предоставления временных credentials сервисам AWS?

A) IAM Policy

B) IAM Role

C) IAM User

D) IAM Group

---

## Question 3: Policy Evaluation


Если у пользователя есть политика с Allow на s3:*, а на S3 bucket есть политика с Deny на s3:GetObject, что произойдёт при запросе GetObject?

A) Deny (explicit deny всегда побеждает)

B) Ошибка конфликта политик

C) Allow (identity policy побеждает)

D) Зависит от порядка создания политик

---

## Question 4: Best Practice для Users


Какой подход к назначению политик пользователям считается best practice?

A) Прикреплять политики напрямую к каждому пользователю

B) Использовать inline политики

C) Давать всем пользователям AdministratorAccess

D) Добавлять пользователей в группы и назначать политики группам

---

## Question 5: Root Account


Для каких действий рекомендуется использовать root account?

A) Запуск Lambda функций

B) Повседневное администрирование

C) Закрытие аккаунта и восстановление IAM admin доступа

D) Создание EC2 инстансов

---

## Question 6: Trust Policy


Что определяет Trust Policy роли?

A) Кто может принять (assume) эту роль

B) Какие ресурсы может использовать роль

C) Какие действия разрешены роли

D) Как долго действуют credentials роли

---

## Question 7: MFA Condition


Какое условие в политике требует наличия MFA?

A) `"aws:MultiFactorAuthPresent": "true"`

B) `"iam:MFAEnabled": "true"`

C) `"aws:MFARequired": "true"`

D) `"aws:SecureTransport": "true"`

---

## Question 8: Cross-Account Access


Как предоставить пользователю из аккаунта A доступ к ресурсам в аккаунте B?

A) Cross-account доступ невозможен в AWS

B) Создать роль в аккаунте B с Trust Policy для аккаунта A

C) Использовать один и тот же access key в обоих аккаунтах

D) Создать IAM пользователя в аккаунте B с такими же credentials

---

## Question 9: Policy Elements


Какой элемент политики определяет "на каких ресурсах" применяется правило?

A) Action

B) Principal

C) Effect

D) Resource

---

## Question 10: AssumeRole


Какой AWS сервис используется для получения временных credentials через AssumeRole?

A) STS (Security Token Service)

B) IAM

C) Cognito

D) Directory Service

---

## Question 11: AWS Managed Policies


Какое преимущество AWS Managed Policies?

A) Работают быстрее customer managed policies

B) Автоматически обновляются AWS при появлении новых сервисов

C) Не учитываются в лимитах политик

D) Можно редактировать их содержимое

---

## Question 12: Instance Profile


Для чего нужен Instance Profile?

A) Для связи IAM Role с EC2 инстансом

B) Для мониторинга производительности

C) Для хранения профиля пользователя EC2

D) Для настройки сетевого профиля

---

## Question 13: Permission Boundary


Что делает Permission Boundary?

A) Определяет границы VPC

B) Устанавливает лимиты на количество политик

C) Даёт дополнительные разрешения

D) Ограничивает максимальные разрешения, которые может получить entity

---

## Question 14: Service Control Policies


Где применяются Service Control Policies (SCPs)?

A) К AWS Organizations (аккаунтам и OU)

B) К отдельным IAM пользователям

C) К EC2 инстансам

D) К IAM группам

---

## Question 15: OIDC Federation


Какой use case подходит для OIDC Federation?

A) Шифрование данных

B) Аутентификация сотрудников через корпоративный Active Directory

C) Предоставление временных credentials для GitHub Actions

D) Создание постоянных IAM пользователей

---

## Question 16: Policy Version


Какую версию следует указывать в IAM политиках?

A) "2024-01-01"

B) Версия не обязательна

C) "2012-10-17"

D) "2008-10-17"

---

## Question 17: Implicit Deny


Что такое Implicit Deny в IAM?

A) Отсутствие разрешения автоматически означает запрет

B) Временный запрет

C) Запрет, унаследованный от группы

D) Явный запрет в политике

---

## Question 18: Access Analyzer


Для чего используется IAM Access Analyzer?

A) Поиск ресурсов, доступных извне аккаунта, и генерация минимальных политик

B) Управление access keys

C) Мониторинг стоимости IAM

D) Анализ производительности IAM

---

## Question 19: Условия в политиках


Какое условие ограничивает доступ по IP-адресу?

A) `StringEquals`

B) `NetworkAddress`

C) `IpAddress`

D) `SourceIP`

---

## Question 20: IAM Identity Center


Что такое AWS IAM Identity Center (ранее AWS SSO)?

A) Сервис для шифрования

B) Сервис для создания IAM пользователей

C) Альтернатива IAM

D) Централизованное управление доступом к нескольким AWS аккаунтам

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | IAM — глобальный сервис. Пользователи, роли и политики доступны во всех регионах аккаунта. |
| 2 | B | IAM Role предоставляет временные credentials и может быть assumed сервисами AWS, пользователями или внешними identity. |
| 3 | A | Explicit Deny всегда побеждает. Если где-либо есть Deny — доступ запрещён, независимо от Allow в других политиках. |
| 4 | D | Best practice — организовывать пользователей в группы и назначать политики группам. Это упрощает управление. |
| 5 | C | Root account следует использовать только для задач, требующих root: закрытие аккаунта, изменение support plan, восстановление доступа. |
| 6 | A | Trust Policy определяет Principal, который может assume роль (например, ec2.amazonaws.com или другой аккаунт). |
| 7 | A | Условие `"aws:MultiFactorAuthPresent": "true"` требует, чтобы пользователь прошёл MFA аутентификацию. |
| 8 | B | Для cross-account доступа создаётся роль в целевом аккаунте с Trust Policy, разрешающей assume из исходного аккаунта. |
| 9 | D | Resource определяет ARN ресурсов, к которым применяется правило. Action — действия, Effect — Allow/Deny. |
| 10 | A | AWS STS (Security Token Service) отвечает за выдачу временных credentials через AssumeRole, AssumeRoleWithSAML и т.д. |
| 11 | B | AWS Managed Policies автоматически обновляются AWS при добавлении новых сервисов или действий. |
| 12 | A | Instance Profile — контейнер для IAM Role, который позволяет прикрепить роль к EC2 инстансу. |
| 13 | D | Permission Boundary ограничивает максимальные разрешения entity. Даже если политика даёт больше прав, boundary их урежет. |
| 14 | A | SCPs применяются в AWS Organizations к аккаунтам и Organizational Units для ограничения разрешений на уровне организации. |
| 15 | C | OIDC Federation идеально подходит для CI/CD систем (GitHub Actions, GitLab) для получения временных credentials без хранения секретов. |
| 16 | C | Всегда используйте версию "2012-10-17" — это актуальная версия языка политик с полной функциональностью. |
| 17 | A | Implicit Deny означает, что если нет явного Allow для действия, оно автоматически запрещено. |
| 18 | A | IAM Access Analyzer находит ресурсы, доступные извне аккаунта, и может генерировать минимальные политики на основе CloudTrail. |
| 19 | C | Условие `IpAddress` с ключом `aws:SourceIp` ограничивает доступ по IP-адресу источника запроса. |
| 20 | D | IAM Identity Center — централизованный сервис для управления доступом пользователей к нескольким AWS аккаунтам через единый портал. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете IAM. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Policy Evaluation Logic и Permission Boundaries. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы про роли и политики. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно про структуру политик. |

---

