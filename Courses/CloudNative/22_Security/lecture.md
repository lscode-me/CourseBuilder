# Безопасность в облаке

---

## 📋 Prerequisites

- Базовые знания IAM
- Понимание networking
- Знакомство с шифрованием

---

## 🎯 Learning Objectives

- Понимать Shared Responsibility Model
- Применять принцип Least Privilege
- Защищать данные at rest и in transit
- Использовать security сервисы AWS

---

## 1. Shared Responsibility Model

### 1.1 Модель разделения ответственности

```
┌───────────────────────────────────────────────────────────────────┐
│              Shared Responsibility Model                          │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                    CUSTOMER RESPONSIBILITY                    ││
│  │                    "Security IN the Cloud"                    ││
│  │                                                               ││
│  │  • Customer data                                             │ │
│  │  • Platform, applications, IAM                               │ │
│  │  • Operating system, network, firewall config               │  │
│  │  • Client-side encryption                                    │ │
│  │  • Server-side encryption                                    │ │
│  │  • Network traffic protection                               │  │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                      AWS RESPONSIBILITY                       ││
│  │                    "Security OF the Cloud"                    ││
│  │                                                               ││
│  │  • Hardware / AWS Global Infrastructure                      │ │
│  │  • Regions, Availability Zones, Edge Locations              │  │
│  │  • Compute, Storage, Database, Networking (physical)        │  │
│  │  • Software: Hypervisor, Network                            │  │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  Managed Services shift more responsibility to AWS:               │
│  EC2: You manage OS, apps                                         │
│  RDS: AWS manages OS, DB patching                                 │
│  Lambda: AWS manages everything except code                       │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

---

## 2. Identity and Access Management

### 2.1 Least Privilege Principle

```python
# ❌ BAD: Overly permissive

bad_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": "*",
        "Resource": "*"
    }]
}

# ✅ GOOD: Least privilege

good_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::my-bucket/uploads/*",
        "Condition": {
            "StringEquals": {
                "aws:PrincipalTag/team": "backend"
            }
        }
    }]
}
```

### 2.2 IAM Best Practices

```python
iam_best_practices = [
    "Never use root account for daily operations",
    "Enable MFA for all users, especially privileged",
    "Use IAM roles instead of long-term credentials",
    "Apply least privilege - start with minimum permissions",
    "Use policy conditions (IP, time, MFA, tags)",
    "Rotate credentials regularly",
    "Use IAM Access Analyzer to identify overly permissive policies",
    "Set up CloudTrail for audit logging",
    "Use Service Control Policies (SCPs) in Organizations",
    "Implement permission boundaries for delegated admin"
]

print("IAM Best Practices:")
for i, practice in enumerate(iam_best_practices, 1):
    print(f"  {i}. {practice}")
```

### 2.3 IAM Roles для сервисов

```yaml
# Lambda execution role

LambdaRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
          Action: sts:AssumeRole
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    Policies:
      - PolicyName: S3Access
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - s3:GetObject
              Resource: !Sub 'arn:aws:s3:::${Bucket}/*'
```

---

## 3. Network Security

### 3.1 Defense in Depth

```
┌───────────────────────────────────────────────────────────────────┐
│              Network Security Layers                              │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Internet                                                         │
│      │                                                            │
│      ▼                                                            │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  AWS Shield / WAF (DDoS, application attacks)               │  │
│  └────────────────────────────────────────────────────────────┘   │
│      │                                                            │
│      ▼                                                            │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  CloudFront (SSL termination, geo-blocking)                 │  │
│  └────────────────────────────────────────────────────────────┘   │
│      │                                                            │
│      ▼                                                            │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  VPC                                                         │ │
│  │  ┌───────────────────────────────────────────────────────┐  │  │
│  │  │  Public Subnet (ALB, NAT Gateway)                     │  │  │
│  │  │  └── NACL: stateless firewall                        │  │   │
│  │  │  └── Security Group: stateful firewall               │  │   │
│  │  └───────────────────────────────────────────────────────┘  │  │
│  │  ┌───────────────────────────────────────────────────────┐  │  │
│  │  │  Private Subnet (EC2, RDS, Lambda)                    │  │  │
│  │  │  └── No direct internet access                        │  │  │
│  │  │  └── Security Group: only from ALB                   │  │   │
│  │  └───────────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 3.2 Security Groups

```python
# Security Group - stateful, allow rules only

sg_web = {
    "Inbound": [
        {"Port": 443, "Source": "0.0.0.0/0", "Description": "HTTPS from internet"},
        {"Port": 80, "Source": "0.0.0.0/0", "Description": "HTTP (redirect to HTTPS)"}
    ],
    "Outbound": [
        {"Port": "All", "Destination": "0.0.0.0/0", "Description": "Default allow all out"}
    ]
}

sg_app = {
    "Inbound": [
        {"Port": 8080, "Source": "sg-web", "Description": "Only from web tier"}
    ]
}

sg_db = {
    "Inbound": [
        {"Port": 5432, "Source": "sg-app", "Description": "Only from app tier"}
    ]
}
```

---

## 4. Data Protection

### 4.1 Encryption at Rest

```python
encryption_at_rest = {
    "S3": {
        "SSE-S3": "AWS managed keys",
        "SSE-KMS": "Customer managed KMS keys",
        "SSE-C": "Customer provided keys"
    },
    "EBS": "AES-256 encryption via KMS",
    "RDS": "Encryption at creation, KMS keys",
    "DynamoDB": "Encryption by default, KMS",
    "Secrets Manager": "Automatic encryption with KMS"
}

# Best practice: Use customer managed KMS keys (CMK)
# - Audit key usage in CloudTrail
# - Control key access via key policy
# - Enable automatic key rotation
```

### 4.2 Encryption in Transit

```python
# Always use TLS/HTTPS

encryption_in_transit = {
    "ALB/CloudFront": "TLS termination, ACM certificates",
    "API Gateway": "HTTPS only endpoint",
    "RDS": "SSL/TLS connections (rds.force_ssl)",
    "S3": "HTTPS endpoint, bucket policy to enforce",
    "Internal": "TLS between services (App Mesh, service mesh)"
}

# S3 bucket policy to enforce HTTPS

s3_ssl_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "EnforceHTTPS",
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:*",
        "Resource": ["arn:aws:s3:::my-bucket/*"],
        "Condition": {
            "Bool": {"aws:SecureTransport": "false"}
        }
    }]
}
```

---

## 5. Secrets Management

### 5.1 AWS Secrets Manager

```python
import boto3

secrets_client = boto3.client('secretsmanager')

# Create secret

secrets_client.create_secret(
    Name='myapp/database',
    SecretString=json.dumps({
        'username': 'admin',
        'password': 'SecurePass123!'
    })
)

# Retrieve secret

response = secrets_client.get_secret_value(SecretId='myapp/database')
secret = json.loads(response['SecretString'])

# Enable automatic rotation

secrets_client.rotate_secret(
    SecretId='myapp/database',
    RotationLambdaARN='arn:aws:lambda:...:function:rotation',
    RotationRules={'AutomaticallyAfterDays': 30}
)
```

### 5.2 Parameter Store vs Secrets Manager

```python
comparison = {
    "Secrets Manager": {
        "purpose": "Sensitive credentials with rotation",
        "rotation": "Built-in automatic rotation",
        "pricing": "$0.40/secret/month + API calls",
        "best_for": "Database passwords, API keys"
    },
    "Parameter Store": {
        "purpose": "Configuration and secrets",
        "rotation": "Manual (via Lambda)",
        "pricing": "Standard: Free, Advanced: $0.05/param/month",
        "best_for": "Config values, non-rotating secrets"
    }
}
```

---

## 6. Security Services

### 6.1 AWS Security Services

```python
security_services = {
    "GuardDuty": {
        "function": "Threat detection",
        "detects": "Unusual API calls, compromised instances, reconnaissance"
    },
    "Security Hub": {
        "function": "Security posture dashboard",
        "integrates": "GuardDuty, Inspector, IAM Access Analyzer"
    },
    "Inspector": {
        "function": "Vulnerability scanning",
        "scans": "EC2, ECR images, Lambda functions"
    },
    "WAF": {
        "function": "Web Application Firewall",
        "protects": "SQL injection, XSS, rate limiting"
    },
    "Shield": {
        "function": "DDoS protection",
        "tiers": "Standard (free), Advanced ($3000/month)"
    },
    "Macie": {
        "function": "Sensitive data discovery",
        "finds": "PII, credentials in S3"
    },
    "Config": {
        "function": "Configuration compliance",
        "tracks": "Resource configuration changes"
    }
}

print("AWS Security Services:")
for service, details in security_services.items():
    print(f"\n{service}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
```

### 6.2 WAF Rules

```python
# WAF rule examples

waf_rules = [
    "AWSManagedRulesCommonRuleSet",      # OWASP Top 10
    "AWSManagedRulesKnownBadInputsRuleSet",  # Known malicious inputs
    "AWSManagedRulesSQLiRuleSet",        # SQL injection
    "AWSManagedRulesLinuxRuleSet",       # Linux-specific attacks
    "Rate-based rule: 2000 requests/5min"  # DDoS protection
]

# Custom rule: Block specific IPs

custom_rule = {
    "Name": "BlockBadIPs",
    "Priority": 1,
    "Action": {"Block": {}},
    "Statement": {
        "IPSetReferenceStatement": {
            "ARN": "arn:aws:wafv2:...:ipset/bad-ips"
        }
    }
}
```

---

## 7. Compliance

```python
compliance_frameworks = {
    "SOC 2": "Security, availability, processing integrity",
    "HIPAA": "Healthcare data protection",
    "PCI DSS": "Payment card data security",
    "GDPR": "EU data protection",
    "ISO 27001": "Information security management"
}

# AWS Config Rules for compliance

config_rules = [
    "s3-bucket-public-read-prohibited",
    "encrypted-volumes",
    "iam-password-policy",
    "multi-region-cloudtrail-enabled",
    "rds-instance-public-access-check"
]
```

---

## 💡 Key Takeaways

- **Shared Responsibility** — AWS secures cloud, you secure IN cloud

- **Least Privilege** — minimum permissions needed

- **Defense in Depth** — multiple security layers

- **Encrypt Everything** — at rest and in transit

- **Secrets Manager** — for credentials with rotation

- **GuardDuty + Security Hub** — threat detection and posture

---

## 📚 Additional Resources

- [AWS Security Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/)

---

## 🚀 Next Steps

**Следующие модули:**

- [23_CostManagement](../23_CostManagement/) — Оптимизация затрат
- [24_MultiCloud](../24_MultiCloud/) — Multi-cloud security

**Практика:**

1. Включите GuardDuty и проанализируйте findings
2. Настройте Security Hub для compliance checks
3. Реализуйте secrets rotation через Secrets Manager




