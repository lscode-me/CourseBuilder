# IAM: Identity and Access Management

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции облачных вычислений
- Знать структуру AWS (регионы, аккаунты)
- Иметь доступ к AWS аккаунту

**Recommended prior modules:**

- [Введение в облака](../01_Intro/)
- [Архитектура облаков](../03_Architecture/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять IAM пользователями, группами и ролями
- Писать и понимать IAM политики
- Применять принцип наименьших привилегий
- Настраивать SSO и Federation
- Использовать AWS Organizations для multi-account setup

---

## 1. Введение в IAM

### 1.1 Что такое IAM

**AWS Identity and Access Management (IAM)** — глобальный сервис для управления доступом к ресурсам AWS. IAM отвечает на два вопроса:

1. **Authentication (AuthN)**: Кто вы?
2. **Authorization (AuthZ)**: Что вам разрешено делать?

```

┌────────────────────────────────────────────────────────────────────┐
│                        IAM Overview                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐          │
│  │   Users     │     │   Groups    │     │    Roles    │          │
│  │  (people)   │     │ (of users)  │     │ (services)  │          │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘          │
│         │                   │                   │                  │
│         └───────────────────┼───────────────────┘                  │
│                             │                                       │
│                             ▼                                       │
│                    ┌─────────────────┐                             │
│                    │    Policies     │                             │
│                    │   (JSON docs)   │                             │
│                    │                 │                             │
│                    │ What actions    │                             │
│                    │ are allowed or  │                             │
│                    │ denied on which │                             │
│                    │ resources       │                             │
│                    └────────┬────────┘                             │
│                             │                                       │
│                             ▼                                       │
│                    ┌─────────────────┐                             │
│                    │  AWS Resources  │                             │
│                    │  (EC2, S3, RDS) │                             │
│                    └─────────────────┘                             │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 1.2 IAM — глобальный сервис

```python
# IAM не привязан к региону!

iam_characteristics = {
    "scope": "Global (не региональный)",
    "pricing": "Бесплатный",
    "limits": {
        "users_per_account": 5000,
        "groups_per_account": 300,
        "roles_per_account": 1000,
        "policies_per_account": 1500,
        "managed_policies_per_entity": 10
    }
}

print("IAM Characteristics:")
print(f"  Scope: {iam_characteristics['scope']}")
print(f"  Pricing: {iam_characteristics['pricing']}")
print(f"\nLimits:")
for limit, value in iam_characteristics['limits'].items():
    print(f"  {limit}: {value}")

```

**Output:**
```

IAM Characteristics:
  Scope: Global (не региональный)
  Pricing: Бесплатный

Limits:
  users_per_account: 5000
  groups_per_account: 300
  roles_per_account: 1000
  policies_per_account: 1500
  managed_policies_per_entity: 10

```

---

## 2. IAM Users и Groups

### 2.1 IAM Users

**IAM User** — это identity для человека или приложения, которому нужен long-term доступ к AWS.

```bash
# Создание IAM пользователя
aws iam create-user --user-name developer-alice

# Создание access keys для программного доступа
aws iam create-access-key --user-name developer-alice

# Добавление пользователя в группу
aws iam add-user-to-group --user-name developer-alice --group-name developers

# Включение console access
aws iam create-login-profile \
    --user-name developer-alice \
    --password "TempPassword123!" \
    --password-reset-required

```

### 2.2 IAM Groups

**IAM Group** — коллекция IAM пользователей. Политики, прикреплённые к группе, применяются ко всем её членам.

```bash
# Создание группы
aws iam create-group --group-name developers

# Прикрепление политики к группе
aws iam attach-group-policy \
    --group-name developers \
    --policy-arn arn:aws:iam::aws:policy/PowerUserAccess

# Список пользователей в группе
aws iam get-group --group-name developers

```

### 2.3 Best Practice: группы вместо прямых политик

```

┌────────────────────────────────────────────────────────────────────┐
│              User-Group-Policy Best Practice                        │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ❌ BAD: Политики напрямую к пользователям                        │
│                                                                     │
│  ┌─────┐  ┌─────┐  ┌─────┐                                        │
│  │Alice│  │ Bob │  │Carol│                                        │
│  └──┬──┘  └──┬──┘  └──┬──┘                                        │
│     │        │        │                                            │
│     ▼        ▼        ▼                                            │
│  Policy   Policy   Policy   ◄── Сложно управлять!                 │
│                                                                     │
│  ✅ GOOD: Политики через группы                                    │
│                                                                     │
│  ┌─────┐  ┌─────┐  ┌─────┐                                        │
│  │Alice│  │ Bob │  │Carol│                                        │
│  └──┬──┘  └──┬──┘  └──┬──┘                                        │
│     │        │        │                                            │
│     └────────┼────────┘                                            │
│              ▼                                                      │
│        ┌──────────┐                                                │
│        │Developers│  ◄── Группа                                    │
│        │  Group   │                                                │
│        └────┬─────┘                                                │
│             ▼                                                       │
│          Policy    ◄── Одна политика для всех                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

---

## 3. IAM Roles

### 3.1 Что такое Role

**IAM Role** — это identity с permissions, которую могут "принять" (assume) сервисы AWS, пользователи или внешние identity. Роли предоставляют временные credentials.

```python

role_use_cases = {
    "ec2_instance_role": {
        "description": "EC2 инстанс получает доступ к S3",
        "trusted_entity": "ec2.amazonaws.com",
        "example": "Приложение на EC2 читает файлы из S3"
    },
    "lambda_execution_role": {
        "description": "Lambda функция получает доступ к DynamoDB",
        "trusted_entity": "lambda.amazonaws.com",
        "example": "Lambda пишет данные в DynamoDB"
    },
    "cross_account_role": {
        "description": "Пользователь из другого аккаунта получает доступ",
        "trusted_entity": "arn:aws:iam::OTHER_ACCOUNT:root",
        "example": "Аудитор из аккаунта A читает логи в аккаунте B"
    },
    "federated_role": {
        "description": "Внешний identity provider (SAML/OIDC)",
        "trusted_entity": "SAML provider или OIDC provider",
        "example": "Сотрудник логинится через Okta"
    }
}

print("IAM Role Use Cases:\n")
for role_type, details in role_use_cases.items():
    print(f"📋 {role_type}")
    print(f"   {details['description']}")
    print(f"   Trusted: {details['trusted_entity']}")
    print()

```

**Output:**
```

IAM Role Use Cases:

📋 ec2_instance_role
   EC2 инстанс получает доступ к S3
   Trusted: ec2.amazonaws.com

📋 lambda_execution_role
   Lambda функция получает доступ к DynamoDB
   Trusted: lambda.amazonaws.com

📋 cross_account_role
   Пользователь из другого аккаунта получает доступ
   Trusted: arn:aws:iam::OTHER_ACCOUNT:root

📋 federated_role
   Внешний identity provider (SAML/OIDC)
   Trusted: SAML provider или OIDC provider

```

### 3.2 Создание роли для EC2

```json

// Trust Policy (кто может assume роль)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```

```bash
# Создание роли
aws iam create-role \
    --role-name EC2-S3-Access \
    --assume-role-policy-document file://trust-policy.json

# Прикрепление политики к роли
aws iam attach-role-policy \
    --role-name EC2-S3-Access \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Создание instance profile
aws iam create-instance-profile \
    --instance-profile-name EC2-S3-Access-Profile

# Добавление роли в instance profile
aws iam add-role-to-instance-profile \
    --instance-profile-name EC2-S3-Access-Profile \
    --role-name EC2-S3-Access

# Запуск EC2 с ролью
aws ec2 run-instances \
    --image-id ami-12345678 \
    --instance-type t3.micro \
    --iam-instance-profile Name=EC2-S3-Access-Profile

```

### 3.3 AssumeRole

```python

import boto3

def assume_role(role_arn: str, session_name: str) -> dict:
    """
    Получение временных credentials через AssumeRole
    """
    sts = boto3.client('sts')
    
    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name,
        DurationSeconds=3600  # 1 час (max 12 часов)
    )
    
    credentials = response['Credentials']
    
    return {
        'AccessKeyId': credentials['AccessKeyId'],
        'SecretAccessKey': credentials['SecretAccessKey'],
        'SessionToken': credentials['SessionToken'],
        'Expiration': credentials['Expiration']
    }

# Использование временных credentials
role_arn = "arn:aws:iam::123456789012:role/CrossAccountRole"
creds = assume_role(role_arn, "my-session")

# Создание клиента с временными credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    aws_session_token=creds['SessionToken']
)

```

---

## 4. IAM Policies

### 4.1 Структура политики

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3Read",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "192.168.1.0/24"
                }
            }
        }
    ]
}

```

### 4.2 Элементы политики

```python

policy_elements = {
    "Version": {
        "description": "Версия языка политик",
        "values": ["2012-10-17", "2008-10-17"],
        "recommendation": "Всегда используйте 2012-10-17"
    },
    "Statement": {
        "description": "Массив правил",
        "required": True
    },
    "Sid": {
        "description": "Statement ID (опциональный идентификатор)",
        "required": False
    },
    "Effect": {
        "description": "Разрешить или запретить",
        "values": ["Allow", "Deny"]
    },
    "Principal": {
        "description": "Кому применяется (только для resource-based политик)",
        "examples": ["*", "arn:aws:iam::123456789012:user/Bob"]
    },
    "Action": {
        "description": "Какие действия",
        "examples": ["s3:GetObject", "ec2:*", "iam:Create*"]
    },
    "Resource": {
        "description": "На каких ресурсах",
        "examples": ["*", "arn:aws:s3:::bucket/*"]
    },
    "Condition": {
        "description": "При каких условиях (опционально)",
        "examples": ["IpAddress", "StringEquals", "DateGreaterThan"]
    }
}

print("Policy Elements:\n")
for element, details in policy_elements.items():
    print(f"{element}:")
    print(f"  {details['description']}")
    if 'values' in details:
        print(f"  Values: {details['values']}")

```

**Output:**
```

Policy Elements:

Version:
  Версия языка политик
  Values: ['2012-10-17', '2008-10-17']

Statement:
  Массив правил

Sid:
  Statement ID (опциональный идентификатор)

Effect:
  Разрешить или запретить
  Values: ['Allow', 'Deny']

Principal:
  Кому применяется (только для resource-based политик)

Action:
  Какие действия

Resource:
  На каких ресурсах

Condition:
  При каких условиях (опционально)

```

### 4.3 Типы политик

```

┌────────────────────────────────────────────────────────────────────┐
│                      Types of IAM Policies                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. AWS Managed Policies                                           │
│     └── Созданы и управляются AWS                                 │
│     └── Пример: AmazonS3ReadOnlyAccess, PowerUserAccess           │
│     └── Автоматически обновляются AWS                             │
│                                                                     │
│  2. Customer Managed Policies                                       │
│     └── Созданы вами в вашем аккаунте                             │
│     └── Полный контроль                                           │
│     └── Можно прикрепить к нескольким identity                    │
│                                                                     │
│  3. Inline Policies                                                │
│     └── Встроены напрямую в user/group/role                       │
│     └── 1:1 связь с entity                                        │
│     └── Удаляются вместе с entity                                 │
│     └── Не рекомендуется (сложнее управлять)                      │
│                                                                     │
│  4. Resource-based Policies                                        │
│     └── Прикреплены к ресурсу (S3 bucket, SQS queue)             │
│     └── Определяют кто может обращаться к ресурсу                │
│     └── Содержат Principal                                        │
│                                                                     │
│  5. Permission Boundaries                                          │
│     └── Ограничивают максимальные разрешения                      │
│     └── Не дают разрешений сами по себе                          │
│     └── Используются для делегирования                            │
│                                                                     │
│  6. Service Control Policies (SCPs)                                │
│     └── Для AWS Organizations                                      │
│     └── Ограничивают разрешения на уровне аккаунтов              │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 4.4 Примеры политик

```json

// Политика для разработчика
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEC2DescribeAll",
            "Effect": "Allow",
            "Action": "ec2:Describe*",
            "Resource": "*"
        },
        {
            "Sid": "AllowEC2RunInstancesWithTag",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/Environment": "dev"
                }
            }
        },
        {
            "Sid": "AllowEC2ManageOwnInstances",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/Owner": "${aws:username}"
                }
            }
        }
    ]
}

```

```json

// S3 Bucket Policy (resource-based)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCrossAccountAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::OTHER_ACCOUNT_ID:root"
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ]
        }
    ]
}

```

---

## 5. Policy Evaluation Logic

### 5.1 Порядок оценки

```

┌────────────────────────────────────────────────────────────────────┐
│                   Policy Evaluation Logic                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Запрос от Principal                                               │
│         │                                                           │
│         ▼                                                           │
│  ┌──────────────────┐                                              │
│  │ 1. Explicit DENY │ ──► DENY найден? ──► DENIED                 │
│  │    anywhere?     │                                              │
│  └────────┬─────────┘                                              │
│           │ No                                                      │
│           ▼                                                         │
│  ┌──────────────────┐                                              │
│  │ 2. SCP Allow?    │ ──► Нет SCP Allow? ──► DENIED               │
│  │    (Organizations)│                                             │
│  └────────┬─────────┘                                              │
│           │ Yes                                                     │
│           ▼                                                         │
│  ┌──────────────────┐                                              │
│  │ 3. Resource-based│ ──► Allow с Principal ──► ALLOWED           │
│  │    policy Allow? │     и нет Deny                               │
│  └────────┬─────────┘                                              │
│           │ No                                                      │
│           ▼                                                         │
│  ┌──────────────────┐                                              │
│  │ 4. Permission    │ ──► Превышает boundary? ──► DENIED          │
│  │    Boundary?     │                                              │
│  └────────┬─────────┘                                              │
│           │ No                                                      │
│           ▼                                                         │
│  ┌──────────────────┐                                              │
│  │ 5. Identity-based│ ──► Allow найден? ──► ALLOWED               │
│  │    policy Allow? │                                              │
│  └────────┬─────────┘                                              │
│           │ No                                                      │
│           ▼                                                         │
│       DENIED (implicit deny)                                        │
│                                                                     │
│  KEY RULE: Explicit Deny > Allow > Implicit Deny                   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 5.2 Пример оценки

```python

def evaluate_policy_example():
    """
    Пример: Пользователь Bob пытается s3:GetObject на bucket-A
    """
    
    # Bob's identity policy
    identity_policy = {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": "*"
    }
    
    # bucket-A bucket policy
    bucket_policy = {
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::bucket-A/confidential/*"
    }
    
    # Оценка
    print("Scenario: Bob requests s3:GetObject on bucket-A/confidential/file.txt")
    print("\nEvaluation:")
    print("1. Check explicit DENY in any policy...")
    print("   → Bucket policy has DENY for s3:GetObject on confidential/*")
    print("   → RESULT: DENIED")
    print("\nNote: Even though Bob has s3:* Allow, explicit DENY wins!")

evaluate_policy_example()

```

**Output:**
```

Scenario: Bob requests s3:GetObject on bucket-A/confidential/file.txt

Evaluation:

1. Check explicit DENY in any policy...
   → Bucket policy has DENY for s3:GetObject on confidential/*
   → RESULT: DENIED

Note: Even though Bob has s3:* Allow, explicit DENY wins!

```

---

## 6. Принцип наименьших привилегий

### 6.1 Least Privilege Principle

```python
# ❌ BAD: Слишком широкие разрешения
bad_policy = {
    "Effect": "Allow",
    "Action": "*",
    "Resource": "*"
}

# ✅ GOOD: Только необходимые разрешения
good_policy = {
    "Effect": "Allow",
    "Action": [
        "s3:GetObject",
        "s3:PutObject"
    ],
    "Resource": [
        "arn:aws:s3:::my-app-uploads/*"
    ]
}

# ✅✅ BETTER: С условиями
better_policy = {
    "Effect": "Allow",
    "Action": [
        "s3:GetObject",
        "s3:PutObject"
    ],
    "Resource": [
        "arn:aws:s3:::my-app-uploads/${aws:PrincipalTag/team}/*"
    ],
    "Condition": {
        "StringEquals": {
            "s3:x-amz-acl": "private"
        }
    }
}

```

### 6.2 Инструменты для анализа

```bash
# IAM Access Analyzer — находит ресурсы, доступные извне
aws accessanalyzer create-analyzer \
    --analyzer-name my-analyzer \
    --type ACCOUNT

# IAM Policy Simulator — тестирует политики
aws iam simulate-principal-policy \
    --policy-source-arn arn:aws:iam::123456789012:user/Bob \
    --action-names s3:GetObject \
    --resource-arns arn:aws:s3:::my-bucket/file.txt

# Генерация политики на основе CloudTrail
aws accessanalyzer generate-policy \
    --policy-generation-details '{
        "cloudTrailDetails": {
            "trailArn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/my-trail",
            "startTime": "2024-01-01T00:00:00Z",
            "endTime": "2024-01-31T23:59:59Z"
        }
    }'

```

---

## 7. Multi-Factor Authentication (MFA)

### 7.1 Типы MFA

```python

mfa_types = {
    "virtual_mfa": {
        "description": "Приложения типа Google Authenticator, Authy",
        "cost": "Бесплатно",
        "security": "Good"
    },
    "hardware_mfa": {
        "description": "Физический токен (Gemalto, YubiKey)",
        "cost": "$20-50",
        "security": "Better"
    },
    "u2f_security_key": {
        "description": "FIDO U2F ключи (YubiKey)",
        "cost": "$20-50",
        "security": "Best"
    }
}

print("MFA Options:\n")
for mfa_type, details in mfa_types.items():
    print(f"  {mfa_type}:")
    print(f"    {details['description']}")
    print(f"    Cost: {details['cost']}, Security: {details['security']}")

```

**Output:**
```

MFA Options:

  virtual_mfa:
    Приложения типа Google Authenticator, Authy
    Cost: Бесплатно, Security: Good
  hardware_mfa:
    Физический токен (Gemalto, YubiKey)
    Cost: $20-50, Security: Better
  u2f_security_key:
    FIDO U2F ключи (YubiKey)
    Cost: $20-50, Security: Best

```

### 7.2 MFA условие в политике

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEC2OnlyWithMFA",
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            }
        }
    ]
}

```

---

## 8. Federation и SSO

### 8.1 SAML 2.0 Federation

```

┌────────────────────────────────────────────────────────────────────┐
│                    SAML 2.0 Federation Flow                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. User authenticates with Corporate IdP (Okta, AD FS)           │
│                                                                     │
│  ┌──────────┐         ┌──────────┐         ┌──────────┐           │
│  │   User   │ ──1──►  │Corporate │ ──2──►  │   AWS    │           │
│  │          │         │   IdP    │         │   STS    │           │
│  └──────────┘         └──────────┘         └──────────┘           │
│       │                    │                    │                  │
│       │                    │ SAML Assertion     │                  │
│       │                    └──────────────────► │                  │
│       │                                         │                  │
│       │           Temporary Credentials         │                  │
│       │◄────────────────────────────────────────┘                  │
│       │                                                            │
│       │  3. User accesses AWS with temp creds                     │
│       │                                                            │
│       ▼                                                            │
│  ┌──────────┐                                                      │
│  │   AWS    │                                                      │
│  │ Console/ │                                                      │
│  │   API    │                                                      │
│  └──────────┘                                                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 8.2 AWS IAM Identity Center (SSO)

```bash
# AWS IAM Identity Center (ранее AWS SSO)
# Централизованное управление доступом для всех AWS аккаунтов

# Настройка через AWS Console или Terraform
# 1. Включить IAM Identity Center
# 2. Подключить identity source (IdC directory, AD, external IdP)
# 3. Создать Permission Sets
# 4. Назначить пользователям доступ к аккаунтам
```

```python
# Permission Set пример
permission_set = {
    "name": "DeveloperAccess",
    "description": "Access for developers",
    "session_duration": "PT8H",  # 8 часов
    "managed_policies": [
        "arn:aws:iam::aws:policy/PowerUserAccess"
    ],
    "inline_policy": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Action": [
                    "iam:*",
                    "organizations:*"
                ],
                "Resource": "*"
            }
        ]
    }
}

```

### 8.3 OIDC Federation (для CI/CD)

```json

// Trust policy для GitHub Actions
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                },
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:myorg/myrepo:*"
                }
            }
        }
    ]
}

```

```yaml
# GitHub Actions workflow
name: Deploy to AWS
on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1
      
      - run: aws s3 ls  # Works with temporary credentials!

```

---

## 9. AWS Organizations и SCPs

### 9.1 Структура Organizations

```

┌────────────────────────────────────────────────────────────────────┐
│                    AWS Organizations Structure                      │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Root (Management Account)                                         │
│  │                                                                  │
│  ├── OU: Security                                                  │
│  │   ├── Account: Log Archive (centralized logs)                  │
│  │   └── Account: Security Tooling (GuardDuty, SecurityHub)       │
│  │                                                                  │
│  ├── OU: Infrastructure                                            │
│  │   ├── Account: Shared Services (DNS, AD)                       │
│  │   └── Account: Network (Transit Gateway)                       │
│  │                                                                  │
│  ├── OU: Workloads                                                 │
│  │   ├── OU: Production                                            │
│  │   │   ├── Account: Prod-App-A                                  │
│  │   │   └── Account: Prod-App-B                                  │
│  │   │                                                              │
│  │   └── OU: Development                                           │
│  │       ├── Account: Dev-App-A                                   │
│  │       └── Account: Dev-App-B                                   │
│  │                                                                  │
│  └── OU: Sandbox                                                   │
│      └── Account: Developer Sandbox                                │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

```

### 9.2 Service Control Policies (SCPs)

```json

// SCP: Запретить отключение CloudTrail
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCloudTrailDisable",
            "Effect": "Deny",
            "Action": [
                "cloudtrail:DeleteTrail",
                "cloudtrail:StopLogging",
                "cloudtrail:UpdateTrail"
            ],
            "Resource": "*"
        }
    ]
}

```

```json

// SCP: Разрешить только определённые регионы
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyRegionsExceptEU",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": [
                        "eu-west-1",
                        "eu-central-1"
                    ]
                }
            }
        }
    ]
}

```

---

## 10. Common Pitfalls

### 10.1 Pitfall: Использование root account

❌ **Проблема:**
```bash
# Вход в консоль как root@company.com
# Создание ресурсов от имени root
# Root credentials в приложениях
```

✅ **Решение:**
```bash
# 1. Включить MFA на root
# 2. Никогда не создавать access keys для root
# 3. Создать IAM пользователя для администрирования
# 4. Использовать root только для:
#    - Закрытие аккаунта
#    - Изменение support plan
#    - Восстановление IAM admin доступа
```

### 10.2 Pitfall: Слишком широкие политики

❌ **Проблема:**
```json

{
    "Effect": "Allow",
    "Action": "*",
    "Resource": "*"
}

```

✅ **Решение:**
```bash
# Используйте IAM Access Analyzer для генерации минимальных политик
aws accessanalyzer generate-policy --policy-generation-details ...

# Или начните с AWS managed policy и ограничьте
```

### 10.3 Pitfall: Long-lived credentials

❌ **Проблема:**
```python
# Access keys в коде или переменных окружения
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

```

✅ **Решение:**
```python
# Используйте IAM Roles для EC2, Lambda, ECS
# Используйте OIDC Federation для CI/CD
# Если нужны access keys - ротируйте регулярно

# Для локальной разработки - AWS CLI profiles
# ~/.aws/credentials
```

---

## 💡 Key Takeaways

- **IAM** — глобальный бесплатный сервис для управления доступом

- **Принцип наименьших привилегий** — давайте только необходимые разрешения

- **Roles > Users** — используйте роли для сервисов и cross-account доступа

- **Groups** — политики через группы, не напрямую к пользователям

- **MFA** — обязательно для root и привилегированных пользователей

- **Explicit Deny всегда побеждает** — любой Deny перекрывает Allow

---

## 🚀 Next Steps

**Следующие модули:**

- [EC2](../05_EC2/) — виртуальные серверы
- [VPC](../07_VPC/) — сетевая инфраструктура

**Практические задания:**

1. Создайте IAM пользователя с MFA
2. Создайте роль для EC2 с доступом к S3
3. Напишите политику с использованием условий
4. Настройте OIDC Federation для GitHub Actions

**Для углубления:**

- Изучите Permission Boundaries
- Настройте AWS Organizations с SCPs
- Попробуйте IAM Access Analyzer

---

## 📚 Additional Resources

**Documentation:**

- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)

**Tools:**

- [IAM Policy Simulator](https://policysim.aws.amazon.com/)
- [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

**Videos:**

- [AWS re:Invent: IAM Best Practices](https://www.youtube.com/results?search_query=aws+reinvent+iam+best+practices)

---




