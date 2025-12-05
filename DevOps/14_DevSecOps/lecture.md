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

## 💡 Key Takeaways

- **Shift Left**: Security проверки максимально рано в pipeline

- **Автоматизация**: SAST, DAST, SCA в CI/CD

- **Secrets Management**: Никогда не хардкодить секреты

- **Policy as Code**: OPA, Checkov для автоматической проверки

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

**Tools:**
- [Trivy](https://trivy.dev/) — Container/IaC scanner
- [Snyk](https://snyk.io/) — SCA
- [OWASP ZAP](https://www.zaproxy.org/) — DAST

**Certifications:**
- Certified Kubernetes Security Specialist (CKS)
- AWS Security Specialty

---

