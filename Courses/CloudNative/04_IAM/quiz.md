# Cloud Native Development - Quiz
## IAM: Identity and Access Management

Проверьте свои знания по теме "IAM".

---

## Question 1: IAM Scope







Какой scope имеет IAM в AWS?

A) Глобальный (один для всего аккаунта)

B) Привязан к VPC

C) Зависит от типа ресурса

D) Региональный (отдельный для каждого региона)

---

## Question 2: IAM Entities







Какой IAM entity предназначен для предоставления временных credentials сервисам AWS?

A) IAM User

B) IAM Policy

C) IAM Group

D) IAM Role

---

## Question 3: Policy Evaluation







Если у пользователя есть политика с Allow на s3:*, а на S3 bucket есть политика с Deny на s3:GetObject, что произойдёт при запросе GetObject?

A) Allow (identity policy побеждает)

B) Зависит от порядка создания политик

C) Ошибка конфликта политик

D) Deny (explicit deny всегда побеждает)

---

## Question 4: Best Practice для Users







Какой подход к назначению политик пользователям считается best practice?

A) Добавлять пользователей в группы и назначать политики группам

B) Использовать inline политики

C) Давать всем пользователям AdministratorAccess

D) Прикреплять политики напрямую к каждому пользователю

---

## Question 5: Root Account







Для каких действий рекомендуется использовать root account?

A) Закрытие аккаунта и восстановление IAM admin доступа

B) Запуск Lambda функций

C) Создание EC2 инстансов

D) Повседневное администрирование

---

## Question 6: Trust Policy







Что определяет Trust Policy роли?

A) Как долго действуют credentials роли

B) Какие действия разрешены роли

C) Какие ресурсы может использовать роль

D) Кто может принять (assume) эту роль

---

## Question 7: MFA Condition







Какое условие в политике требует наличия MFA?

A) `"aws:MFARequired": "true"`

B) `"iam:MFAEnabled": "true"`

C) `"aws:SecureTransport": "true"`

D) `"aws:MultiFactorAuthPresent": "true"`

---

## Question 8: Cross-Account Access







Как предоставить пользователю из аккаунта A доступ к ресурсам в аккаунте B?

A) Cross-account доступ невозможен в AWS

B) Использовать один и тот же access key в обоих аккаунтах

C) Создать IAM пользователя в аккаунте B с такими же credentials

D) Создать роль в аккаунте B с Trust Policy для аккаунта A

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

A) Cognito

B) Directory Service

C) IAM

D) STS (Security Token Service)

---

## Question 11: AWS Managed Policies







Какое преимущество AWS Managed Policies?

A) Не учитываются в лимитах политик

B) Можно редактировать их содержимое

C) Автоматически обновляются AWS при появлении новых сервисов

D) Работают быстрее customer managed policies

---

## Question 12: Instance Profile







Для чего нужен Instance Profile?

A) Для настройки сетевого профиля

B) Для связи IAM Role с EC2 инстансом

C) Для хранения профиля пользователя EC2

D) Для мониторинга производительности

---

## Question 13: Permission Boundary







Что делает Permission Boundary?

A) Устанавливает лимиты на количество политик

B) Даёт дополнительные разрешения

C) Ограничивает максимальные разрешения, которые может получить entity

D) Определяет границы VPC

---

## Question 14: Service Control Policies







Где применяются Service Control Policies (SCPs)?

A) К IAM группам

B) К AWS Organizations (аккаунтам и OU)

C) К EC2 инстансам

D) К отдельным IAM пользователям

---

## Question 15: OIDC Federation







Какой use case подходит для OIDC Federation?

A) Предоставление временных credentials для GitHub Actions

B) Создание постоянных IAM пользователей

C) Шифрование данных

D) Аутентификация сотрудников через корпоративный Active Directory

---

## Question 16: Policy Version







Какую версию следует указывать в IAM политиках?

A) "2008-10-17"

B) "2024-01-01"

C) "2012-10-17"

D) Версия не обязательна

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

A) Управление access keys

B) Анализ производительности IAM

C) Поиск ресурсов, доступных извне аккаунта, и генерация минимальных политик

D) Мониторинг стоимости IAM

---

## Question 19: Условия в политиках







Какое условие ограничивает доступ по IP-адресу?

A) `IpAddress`

B) `StringEquals`

C) `SourceIP`

D) `NetworkAddress`

---

## Question 20: IAM Identity Center







Что такое AWS IAM Identity Center (ранее AWS SSO)?

A) Централизованное управление доступом к нескольким AWS аккаунтам

B) Альтернатива IAM

C) Сервис для создания IAM пользователей

D) Сервис для шифрования

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | IAM — глобальный сервис. Пользователи, роли и политики доступны во всех регионах аккаунта. |
| 2 | D | IAM Role предоставляет временные credentials и может быть assumed сервисами AWS, пользователями или внешними identity. |
| 3 | D | Explicit Deny всегда побеждает. Если где-либо есть Deny — доступ запрещён, независимо от Allow в других политиках. |
| 4 | A | Best practice — организовывать пользователей в группы и назначать политики группам. Это упрощает управление. |
| 5 | A | Root account следует использовать только для задач, требующих root: закрытие аккаунта, изменение support plan, восстановление доступа. |
| 6 | D | Trust Policy определяет Principal, который может assume роль (например, ec2.amazonaws.com или другой аккаунт). |
| 7 | D | Условие `"aws:MultiFactorAuthPresent": "true"` требует, чтобы пользователь прошёл MFA аутентификацию. |
| 8 | D | Для cross-account доступа создаётся роль в целевом аккаунте с Trust Policy, разрешающей assume из исходного аккаунта. |
| 9 | C | Resource определяет ARN ресурсов, к которым применяется правило. Action — действия, Effect — Allow/Deny. |
| 10 | D | AWS STS (Security Token Service) отвечает за выдачу временных credentials через AssumeRole, AssumeRoleWithSAML и т.д. |
| 11 | C | AWS Managed Policies автоматически обновляются AWS при добавлении новых сервисов или действий. |
| 12 | B | Instance Profile — контейнер для IAM Role, который позволяет прикрепить роль к EC2 инстансу. |
| 13 | C | Permission Boundary ограничивает максимальные разрешения entity. Даже если политика даёт больше прав, boundary их урежет. |
| 14 | B | SCPs применяются в AWS Organizations к аккаунтам и Organizational Units для ограничения разрешений на уровне организации. |
| 15 | A | OIDC Federation идеально подходит для CI/CD систем (GitHub Actions, GitLab) для получения временных credentials без хранения секретов. |
| 16 | C | Всегда используйте версию "2012-10-17" — это актуальная версия языка политик с полной функциональностью. |
| 17 | A | Implicit Deny означает, что если нет явного Allow для действия, оно автоматически запрещено. |
| 18 | C | IAM Access Analyzer находит ресурсы, доступные извне аккаунта, и может генерировать минимальные политики на основе CloudTrail. |
| 19 | A | Условие `IpAddress` с ключом `aws:SourceIp` ограничивает доступ по IP-адресу источника запроса. |
| 20 | A | IAM Identity Center — централизованный сервис для управления доступом пользователей к нескольким AWS аккаунтам через единый портал. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете IAM. Переходите к следующему модулю. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Policy Evaluation Logic и Permission Boundaries. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы про роли и политики. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно про структуру политик. |

---

