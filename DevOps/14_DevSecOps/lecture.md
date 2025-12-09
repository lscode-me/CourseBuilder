# DevSecOps
## Безопасность в DevOps

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модули по CI/CD
- Понимать основы информационной безопасности
- Знать Docker и Kubernetes basics

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы DevSecOps
- Внедрить security проверки в CI/CD pipeline
- Использовать инструменты SAST, DAST, SCA
- Управлять секретами безопасно
- Внедрить Compliance as Code для автоматизации соответствия стандартам

---

## 1. Что такое DevSecOps?

### 1.1 Shift Left Security

**DevSecOps** = Development + Security + Operations

```
┌─────────────────────────────────────────────────────────────────┐
│                    Shift Left Security                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Traditional: Security проверки в конце                         │
│  ─────────────────────────────────────────────────────▶         │
│  Plan → Code → Build → Test → Deploy → Operate → Security       │
│                                                    ▲             │
│                                                    └── Дорого!   │
│                                                                  │
│  DevSecOps: Security на каждом этапе (Shift Left)               │
│  ─────────────────────────────────────────────────────▶         │
│  Plan → Code → Build → Test → Deploy → Operate                  │
│    ↑      ↑      ↑       ↑       ↑        ↑                     │
│    └──────┴──────┴───────┴───────┴────────┴── Security везде    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Принципы DevSecOps

```python
devsecops_principles = [
    "Security as Code — безопасность описана в коде",
    "Shift Left — проверки максимально рано",
    "Automate — автоматизация security checks",
    "Everyone is responsible — безопасность — ответственность всех",
    "Continuous — непрерывные проверки, не разовые"
]
```

---

## 2. Security в CI/CD Pipeline

### 2.1 Security Gates

```yaml
# Пример: security gates в GitHub Actions
name: Security Pipeline

on: [push, pull_request]

jobs:
  # 1. SAST - Static Application Security Testing
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Bandit (Python SAST)
        run: |
          pip install bandit
          bandit -r src/ -f json -o bandit-report.json
      
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/python

  # 2. SCA - Software Composition Analysis
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run pip-audit
        run: |
          pip install pip-audit
          pip-audit --requirement requirements.txt
      
      - name: Run Snyk
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # 3. Secret Scanning
  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # 4. Container Scanning
  container:
    runs-on: ubuntu-latest
    needs: [sast, sca, secrets]
    steps:
      - uses: actions/checkout@v4
      
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

  # 5. Infrastructure as Code Scanning
  iac:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform/
          framework: terraform
```

---

## 3. Security Testing Types

### 3.1 SAST (Static Application Security Testing)

```python
# Пример уязвимости, которую найдёт SAST
import subprocess

def run_command(user_input):
    # ❌ Command injection vulnerability
    subprocess.call(f"echo {user_input}", shell=True)

# ✅ Безопасная версия
def run_command_safe(user_input):
    subprocess.call(["echo", user_input])
```

**Инструменты SAST:**
- Bandit (Python)
- Semgrep (multi-language)
- SonarQube
- Checkmarx

### 3.2 DAST (Dynamic Application Security Testing)

```yaml
# DAST в CI/CD
- name: Start application
  run: docker-compose up -d

- name: Wait for app
  run: sleep 30

- name: Run OWASP ZAP
  uses: zaproxy/action-full-scan@v0.4.0
  with:
    target: 'http://localhost:8080'
    rules_file_name: '.zap/rules.tsv'
```

### 3.3 SCA (Software Composition Analysis)

```bash
# Проверка зависимостей Python
pip-audit --requirement requirements.txt

# Проверка npm packages
npm audit

# Использование Snyk
snyk test
```

### 3.4 Container Security

```dockerfile
# Безопасный Dockerfile

# ✅ Используем specific version, не latest
FROM python:3.11-slim-bookworm

# ✅ Non-root user
RUN useradd -m -s /bin/bash appuser
USER appuser

# ✅ Minimal packages
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

# ✅ Read-only filesystem где возможно
CMD ["python", "app.py"]
```

---

## 4. Secrets Management

### 4.1 Принципы

```python
secrets_best_practices = [
    "Никогда не хардкодить секреты в коде",
    "Никогда не коммитить секреты в Git",
    "Использовать secrets management tools",
    "Ротировать секреты регулярно",
    "Минимальные права доступа (least privilege)",
    "Audit logging для доступа к секретам"
]
```

### 4.2 Инструменты

```python
# HashiCorp Vault
import hvac

client = hvac.Client(url='https://vault.example.com')
client.token = os.environ.get('VAULT_TOKEN')

# Читаем секрет
secret = client.secrets.kv.v2.read_secret_version(
    path='myapp/database'
)
db_password = secret['data']['data']['password']

# AWS Secrets Manager
import boto3

client = boto3.client('secretsmanager')
secret = client.get_secret_value(SecretId='myapp/database')
```

### 4.3 GitLeaks Configuration

```yaml
# .gitleaks.toml
title = "Gitleaks config"

[[rules]]
description = "AWS Access Key"
regex = '''AKIA[0-9A-Z]{16}'''
tags = ["key", "AWS"]

[[rules]]
description = "Generic API Key"
regex = '''(?i)(api[_-]?key|apikey|secret)['":\s]*['"]{0,1}[a-zA-Z0-9_-]{20,}'''
tags = ["key", "generic"]

[allowlist]
paths = [
    '''test/.*''',
    '''.*_test\.go'''
]
```

---

## 5. Security Policies as Code

### 5.1 OPA (Open Policy Agent)

```rego
# policy/kubernetes.rego

# Запрет privileged containers
deny[msg] {
    input.kind == "Deployment"
    container := input.spec.template.spec.containers[_]
    container.securityContext.privileged == true
    msg := sprintf("Container %v is privileged", [container.name])
}

# Требование resource limits
deny[msg] {
    input.kind == "Deployment"
    container := input.spec.template.spec.containers[_]
    not container.resources.limits
    msg := sprintf("Container %v missing resource limits", [container.name])
}

# Запрет latest tag
deny[msg] {
    input.kind == "Deployment"
    container := input.spec.template.spec.containers[_]
    endswith(container.image, ":latest")
    msg := sprintf("Container %v uses latest tag", [container.name])
}
```

### 5.2 Checkov для IaC

```yaml
# checkov scan
- name: Run Checkov
  run: |
    pip install checkov
    checkov -d terraform/ --framework terraform

# Пример проверки: S3 bucket encryption
# CKV_AWS_19: Ensure S3 bucket encryption is enabled
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
  
  # ✅ Encryption enabled
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
```

---

## 6. Runtime Security

### 6.1 Kubernetes Security

```yaml
# Pod Security Standards
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  
  containers:
    - name: app
      image: myapp:v1.0.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
      resources:
        limits:
          cpu: "500m"
          memory: "256Mi"
```

### 6.2 Network Policies

```yaml
# Разрешаем трафик только от определённых pods
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-network-policy
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - port: 8080
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - port: 5432
```

---

## 7. Security Metrics

```python
security_metrics = {
    "vulnerabilities": {
        "critical": "Count of critical vulns (target: 0)",
        "high": "Count of high vulns (target: < 5)",
        "time_to_remediate": "Days to fix vulnerabilities"
    },
    "compliance": {
        "policy_violations": "Number of policy violations",
        "scan_coverage": "% of code/images scanned"
    },
    "incidents": {
        "security_incidents": "Number of security incidents",
        "mttr_security": "Mean time to remediate security issues"
    }
}
```

---

## 8. Compliance as Code

### 8.1 Что такое Compliance as Code

**Compliance as Code** — практика описания, тестирования и применения compliance-требований в виде исполняемого кода.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Compliance as Code                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Manual Compliance (традиционный подход):                       │
│  ─────────────────────────────────────────────────────▶         │
│  Audit → Checklist → Manual Review → Report → Fix → Re-audit   │
│                      (месяцы работы, устаревшие данные)         │
│                                                                  │
│  Compliance as Code:                                            │
│  ─────────────────────────────────────────────────────▶         │
│  Define Rules → Automated Scan → Real-time Report → Auto-fix   │
│       ↑              ↑                ↑               ↑         │
│       └──────────────┴────────────────┴───────────────┘         │
│                   Continuous & Automated                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 Compliance Frameworks

```python
compliance_frameworks = {
    "SOC 2": {
        "description": "Security, Availability, Processing Integrity",
        "focus": "SaaS и cloud-сервисы",
        "controls": ["Access Control", "Encryption", "Monitoring", "Incident Response"]
    },
    "PCI DSS": {
        "description": "Payment Card Industry Data Security Standard",
        "focus": "Обработка платёжных данных",
        "controls": ["Network Security", "Data Protection", "Vulnerability Management"]
    },
    "HIPAA": {
        "description": "Health Insurance Portability and Accountability Act",
        "focus": "Медицинские данные (США)",
        "controls": ["PHI Protection", "Access Audit", "Encryption"]
    },
    "GDPR": {
        "description": "General Data Protection Regulation",
        "focus": "Персональные данные (EU)",
        "controls": ["Data Minimization", "Right to Erasure", "Consent Management"]
    },
    "ISO 27001": {
        "description": "Information Security Management",
        "focus": "Универсальный стандарт ИБ",
        "controls": ["Risk Assessment", "Security Policies", "Asset Management"]
    }
}
```

### 8.3 AWS Config Rules

```python
# AWS Config для автоматического compliance monitoring
import boto3

# Пример: проверка encrypted S3 buckets
config_rule = {
    "ConfigRuleName": "s3-bucket-server-side-encryption-enabled",
    "Description": "Checks if S3 buckets have encryption enabled",
    "Source": {
        "Owner": "AWS",
        "SourceIdentifier": "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
    },
    "Scope": {
        "ComplianceResourceTypes": ["AWS::S3::Bucket"]
    }
}

# Custom rule для специфичных требований
custom_rule_lambda = """
def evaluate_compliance(configuration_item):
    # Проверка: RDS instance должен быть encrypted
    if configuration_item['resourceType'] == 'AWS::RDS::DBInstance':
        if not configuration_item['configuration'].get('storageEncrypted'):
            return 'NON_COMPLIANT'
    return 'COMPLIANT'
"""
```

```yaml
# Terraform: AWS Config Rules
resource "aws_config_config_rule" "s3_encryption" {
  name = "s3-bucket-encryption-check"

  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
  }

  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "ec2_imdsv2" {
  name = "ec2-imdsv2-check"

  source {
    owner             = "AWS"
    source_identifier = "EC2_IMDSV2_CHECK"
  }
}

resource "aws_config_config_rule" "rds_encryption" {
  name = "rds-storage-encrypted"

  source {
    owner             = "AWS"
    source_identifier = "RDS_STORAGE_ENCRYPTED"
  }
}
```

### 8.4 Cloud Custodian

```yaml
# Cloud Custodian — policy engine для cloud compliance
# policies/s3-compliance.yml

policies:
  # Найти S3 buckets без encryption
  - name: s3-encryption-check
    resource: s3
    filters:
      - type: bucket-encryption
        state: False
    actions:
      - type: notify
        to: ["security-team@company.com"]
        subject: "S3 Bucket without encryption detected"
      
  # Auto-remediation: включить encryption
  - name: s3-enable-encryption
    resource: s3
    filters:
      - type: bucket-encryption
        state: False
    actions:
      - type: set-bucket-encryption

  # Compliance: публичные buckets
  - name: s3-public-access-check
    resource: s3
    filters:
      - type: global-grants
    actions:
      - type: delete-global-grants
      - type: notify
        to: ["security-team@company.com"]
        subject: "Public S3 bucket remediated"
```

```bash
# Запуск Cloud Custodian
pip install c7n

# Проверка policies (dry-run)
custodian run --dryrun -s output policies/s3-compliance.yml

# Применение policies
custodian run -s output policies/s3-compliance.yml

# Генерация compliance report
custodian report -s output policies/s3-compliance.yml
```

### 8.5 Automated Compliance Reporting

```python
# Генерация compliance dashboard
from datetime import datetime

def generate_compliance_report(scan_results):
    """Генерация compliance report для аудиторов."""
    
    report = {
        "report_date": datetime.now().isoformat(),
        "framework": "SOC 2 Type II",
        "period": "Q4 2024",
        "summary": {
            "total_controls": len(scan_results),
            "compliant": sum(1 for r in scan_results if r["status"] == "COMPLIANT"),
            "non_compliant": sum(1 for r in scan_results if r["status"] == "NON_COMPLIANT"),
            "not_applicable": sum(1 for r in scan_results if r["status"] == "N/A")
        },
        "controls": []
    }
    
    for result in scan_results:
        control = {
            "control_id": result["control_id"],
            "description": result["description"],
            "status": result["status"],
            "evidence": result.get("evidence", []),
            "remediation": result.get("remediation"),
            "last_checked": result["timestamp"]
        }
        report["controls"].append(control)
    
    # Compliance score
    total = report["summary"]["total_controls"] - report["summary"]["not_applicable"]
    if total > 0:
        report["compliance_score"] = round(
            (report["summary"]["compliant"] / total) * 100, 2
        )
    
    return report


# Пример результата сканирования
scan_results = [
    {
        "control_id": "CC6.1",
        "description": "Logical and physical access controls",
        "status": "COMPLIANT",
        "evidence": ["IAM policies", "MFA enabled", "Access logs"],
        "timestamp": "2024-12-08T10:00:00Z"
    },
    {
        "control_id": "CC6.7",
        "description": "Data encryption in transit and at rest",
        "status": "NON_COMPLIANT",
        "evidence": ["3 S3 buckets without encryption"],
        "remediation": "Enable SSE-S3 on buckets: logs-*, temp-*",
        "timestamp": "2024-12-08T10:00:00Z"
    }
]
```

### 8.6 Continuous Compliance Pipeline

```yaml
# GitHub Actions: Compliance Pipeline
name: Compliance Check

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM
  push:
    paths:
      - 'terraform/**'
      - 'policies/**'

jobs:
  compliance-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # IaC Compliance (Checkov)
      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform/
          framework: terraform
          output_format: json
          output_file_path: reports/checkov-report.json

      # Cloud Custodian
      - name: Run Cloud Custodian
        run: |
          pip install c7n
          custodian run -s reports/custodian policies/*.yml
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

      # AWS Config compliance status
      - name: Check AWS Config Compliance
        run: |
          aws configservice describe-compliance-by-config-rule \
            --output json > reports/aws-config-compliance.json
        env:
          AWS_REGION: us-east-1

      # Generate unified report
      - name: Generate Compliance Report
        run: python scripts/generate_compliance_report.py

      # Upload to S3 for auditors
      - name: Upload Reports
        run: |
          aws s3 cp reports/ s3://compliance-reports/$(date +%Y-%m-%d)/ --recursive

      # Notify on failures
      - name: Notify on Non-Compliance
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "⚠️ Compliance check failed! Review required.",
              "channel": "security-alerts"
            }
```

### 8.7 Compliance as Code Best Practices

```python
compliance_best_practices = [
    {
        "practice": "Version Control",
        "description": "Храните compliance rules в Git",
        "benefit": "Audit trail, review process, history"
    },
    {
        "practice": "Automated Scanning",
        "description": "Запускайте проверки в CI/CD и по расписанию",
        "benefit": "Real-time compliance status"
    },
    {
        "practice": "Auto-Remediation",
        "description": "Автоматическое исправление где возможно",
        "benefit": "Быстрое устранение violations"
    },
    {
        "practice": "Evidence Collection",
        "description": "Автоматический сбор evidence для аудита",
        "benefit": "Упрощение audit процесса"
    },
    {
        "practice": "Drift Detection",
        "description": "Мониторинг изменений конфигурации",
        "benefit": "Предотвращение compliance drift"
    },
    {
        "practice": "Exception Management",
        "description": "Документирование исключений в коде",
        "benefit": "Прозрачность, accountability"
    }
]

# Пример exception в коде
"""
# checkov:skip=CKV_AWS_19: Legacy bucket, migration planned Q1 2025
# Approved by: security-team, Ticket: SEC-1234
resource "aws_s3_bucket" "legacy_logs" {
  bucket = "legacy-logs-bucket"
}
"""
```

---

## 💡 Key Takeaways

- **Shift Left**: Security проверки максимально рано в pipeline

- **Автоматизация**: SAST, DAST, SCA в CI/CD

- **Secrets Management**: Никогда не хардкодить секреты

- **Policy as Code**: OPA, Checkov для автоматической проверки

- **Compliance as Code**: Автоматизация соответствия стандартам (SOC2, PCI DSS, HIPAA)

- **Everyone's responsibility**: Безопасность — задача всей команды

---

## 🚀 Next Steps

**Related Modules:**
- [04_CI](../04_CI/) — CI Pipeline security gates
- [15_Career](../15_Career/) — Security specialization

**Practice Ideas:**
1. Добавьте Trivy в ваш CI pipeline
2. Настройте GitLeaks pre-commit hook
3. Проведите audit зависимостей

---

## 📚 Additional Resources

**Security Tools:**
- [Trivy](https://trivy.dev/) — Container/IaC scanner
- [Snyk](https://snyk.io/) — SCA
- [OWASP ZAP](https://www.zaproxy.org/) — DAST

**Compliance as Code Tools:**
- [AWS Config](https://aws.amazon.com/config/) — AWS resource compliance
- [Cloud Custodian](https://cloudcustodian.io/) — Multi-cloud policy engine
- [Terraform Sentinel](https://www.hashicorp.com/sentinel) — Policy as Code for Terraform
- [Prowler](https://prowler.pro/) — AWS/Azure/GCP security & compliance

**Certifications:**
- Certified Kubernetes Security Specialist (CKS)
- AWS Security Specialty
- CompTIA Security+

---

