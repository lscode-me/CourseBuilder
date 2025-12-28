# Infrastructure as Code
## Декларативное управление инфраструктурой

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [05_CD](../05_CD/) — Continuous Delivery/Deployment
- Понимать основы облачных провайдеров (AWS/GCP/Azure)
- Иметь опыт работы с Linux и командной строкой

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы и преимущества Infrastructure as Code
- Выбрать между декларативным и императивным подходами
- Создавать инфраструктуру с помощью Terraform
- Управлять конфигурацией с помощью Ansible
- Применять best practices для IaC

---

## 1. Что такое Infrastructure as Code?

### 1.1 Определение

**Infrastructure as Code (IaC)** — практика управления инфраструктурой через машиночитаемые файлы конфигурации, а не через ручные процессы или интерактивные инструменты.

```

┌──────────────────────────────────────────────────────────────────┐
│                     Traditional vs IaC                           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Traditional:                                                    │
│  Admin ──▶ Click UI ──▶ Configure ──▶ Document ──▶ Hope it works │
│           │              │              │                        │
│           │              │              └── Often outdated       │
│           │              └── Not reproducible                    │
│           └── Error-prone, slow                                  │
│                                                                  │
│  Infrastructure as Code:                                         │
│  Dev ──▶ Write Code ──▶ Review ──▶ Apply ──▶ Version Control     │
│           │              │          │          │                 │
│           │              │          │          └── Full history  │
│           │              │          └── Automated, fast          │
│           │              └── Peer review                         │
│           └── Reproducible, testable                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

```

### 1.2 Преимущества IaC

```python

iac_benefits = {
    "reproducibility": {
        "description": "Одинаковая инфраструктура каждый раз",
        "example": "Создать точную копию production для staging"
    },
    "version_control": {
        "description": "История всех изменений",
        "example": "git log для инфраструктуры, rollback через git revert"
    },
    "documentation": {
        "description": "Код IS документация",
        "example": "Читаем Terraform файл — понимаем инфраструктуру"
    },
    "collaboration": {
        "description": "Code review для инфраструктуры",
        "example": "Pull request для добавления нового сервера"
    },
    "automation": {
        "description": "CI/CD для инфраструктуры",
        "example": "Автоматический apply при merge в main"
    },
    "disaster_recovery": {
        "description": "Быстрое восстановление",
        "example": "terraform apply — и вся инфраструктура снова работает"
    }
}

```

### 1.3 Declarative vs Imperative

**Declarative (Что мы хотим):**
```hcl
# Terraform (declarative)
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-12345678"
  instance_type = "t3.medium"
}

# "Я хочу 3 сервера t3.medium"
# Terraform сам разберётся, как это сделать
```

**Imperative (Как это сделать):**
```python
# Python script (imperative)
import boto3

ec2 = boto3.resource('ec2')

for i in range(3):
    ec2.create_instances(
        ImageId='ami-12345678',
        InstanceType='t3.medium',
        MinCount=1,
        MaxCount=1
    )

# "Создай сервер, потом ещё один, потом ещё"
# Мы описываем каждый шаг
```

**Сравнение:**

| Аспект | Declarative | Imperative |
|--------|-------------|------------|
| Описание | Что хотим | Как сделать |
| Idempotent | Да (по умолчанию) | Нужно реализовывать |
| State | Управляется инструментом | Ваша ответственность |
| Пример | Terraform, CloudFormation | Ansible, Python scripts |
| Learning curve | Проще для инфраструктуры | Требует программирования |

---

## 2. Terraform

### 2.1 Основы Terraform

Terraform — декларативный IaC инструмент от HashiCorp.

**Ключевые концепции:**

- **Provider** — плагин для взаимодействия с API (AWS, GCP, etc.)

- **Resource** — элемент инфраструктуры (сервер, база данных, etc.)

- **State** — текущее состояние инфраструктуры

- **Plan** — предварительный просмотр изменений

- **Apply** — применение изменений

### 2.2 Структура проекта

```

terraform/
├── main.tf           # Основные ресурсы
├── variables.tf      # Входные переменные
├── outputs.tf        # Выходные значения
├── providers.tf      # Конфигурация провайдеров
├── terraform.tfvars  # Значения переменных (не в git!)
├── backend.tf        # Конфигурация state backend
└── modules/          # Переиспользуемые модули
    ├── vpc/
    ├── ec2/
    └── rds/

```

### 2.3 Базовый пример

```hcl
# providers.tf
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
    
    # State locking
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "terraform"
      Project     = var.project_name
    }
  }
}

```

```hcl
# variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

variable "project_name" {
  description = "Project name for tagging"
  type        = string
}

variable "instance_count" {
  description = "Number of EC2 instances"
  type        = number
  default     = 2
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

```

```hcl
# main.tf
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Subnets
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-${count.index + 1}"
    Type = "public"
  }
}

# Security Group
resource "aws_security_group" "web" {
  name        = "${var.project_name}-web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instances
resource "aws_instance" "web" {
  count         = var.instance_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public[count.index % length(aws_subnet.public)].id
  
  vpc_security_group_ids = [aws_security_group.web.id]
  
  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }
  
  tags = {
    Name = "${var.project_name}-web-${count.index + 1}"
  }
}

# Data sources
data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

```

```hcl
# outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "instance_public_ips" {
  description = "Public IPs of web instances"
  value       = aws_instance.web[*].public_ip
}

output "instance_ids" {
  description = "Instance IDs"
  value       = aws_instance.web[*].id
}

```

### 2.4 Terraform Workflow

```bash
# 1. Инициализация (скачать провайдеры, настроить backend)
terraform init

# 2. Форматирование кода
terraform fmt -recursive

# 3. Валидация
terraform validate

# 4. План (предварительный просмотр)
terraform plan -out=tfplan

# 5. Применение изменений
terraform apply tfplan

# 6. Просмотр state
terraform state list
terraform state show aws_instance.web[0]

# 7. Удаление ресурсов
terraform destroy

```

### 2.5 Модули Terraform

```hcl
# modules/ec2-cluster/variables.tf
variable "name" {
  description = "Cluster name"
  type        = string
}

variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 2
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

variable "subnet_ids" {
  description = "Subnet IDs for instances"
  type        = list(string)
}

variable "security_group_ids" {
  description = "Security group IDs"
  type        = list(string)
}

```

```hcl
# modules/ec2-cluster/main.tf
resource "aws_instance" "this" {
  count         = var.instance_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = var.subnet_ids[count.index % length(var.subnet_ids)]
  
  vpc_security_group_ids = var.security_group_ids
  
  tags = {
    Name = "${var.name}-${count.index + 1}"
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

```

```hcl
# modules/ec2-cluster/outputs.tf
output "instance_ids" {
  value = aws_instance.this[*].id
}

output "private_ips" {
  value = aws_instance.this[*].private_ip
}

```

```hcl
# Использование модуля в main.tf
module "web_cluster" {
  source = "./modules/ec2-cluster"
  
  name               = "web"
  instance_count     = 3
  instance_type      = "t3.large"
  subnet_ids         = aws_subnet.public[*].id
  security_group_ids = [aws_security_group.web.id]
}

module "api_cluster" {
  source = "./modules/ec2-cluster"
  
  name               = "api"
  instance_count     = 2
  instance_type      = "t3.medium"
  subnet_ids         = aws_subnet.private[*].id
  security_group_ids = [aws_security_group.api.id]
}

```

---

## 3. Ansible

### 3.1 Основы Ansible

Ansible — инструмент для configuration management и automation. Использует SSH, не требует агента на целевых машинах.

**Ключевые концепции:**

- **Inventory** — список серверов

- **Playbook** — набор задач

- **Role** — переиспользуемый набор tasks, handlers, variables

- **Task** — единичное действие

- **Handler** — задача, выполняемая по событию

### 3.2 Структура проекта

```

ansible/
├── ansible.cfg           # Конфигурация
├── inventory/
│   ├── production.yml    # Production hosts
│   └── staging.yml       # Staging hosts
├── playbooks/
│   ├── site.yml          # Главный playbook
│   ├── webservers.yml
│   └── databases.yml
├── roles/
│   ├── common/
│   │   ├── tasks/
│   │   ├── handlers/
│   │   ├── templates/
│   │   └── defaults/
│   ├── nginx/
│   └── postgresql/
└── group_vars/
    ├── all.yml
    ├── webservers.yml
    └── databases.yml

```

### 3.3 Inventory

```yaml
# inventory/production.yml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
          ansible_host: 10.0.1.10
        web2.example.com:
          ansible_host: 10.0.1.11
      vars:
        http_port: 80
        
    databases:
      hosts:
        db1.example.com:
          ansible_host: 10.0.2.10
          postgresql_max_connections: 200
        db2.example.com:
          ansible_host: 10.0.2.11
          postgresql_max_connections: 100
      vars:
        postgresql_version: 15
        
  vars:
    ansible_user: ubuntu
    ansible_ssh_private_key_file: ~/.ssh/production.pem

```

### 3.4 Playbooks

```yaml
# playbooks/webservers.yml
---
- name: Configure web servers
  hosts: webservers
  become: true
  
  vars:
    app_name: myapp
    app_port: 8080
  
  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: true
        cache_valid_time: 3600
  
  roles:
    - common
    - nginx
    - role: app
      vars:
        app_env: production
  
  tasks:
    - name: Ensure app directory exists
      file:
        path: /var/www/{{ app_name }}
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'
    
    - name: Deploy application config
      template:
        src: templates/app.conf.j2
        dest: /etc/{{ app_name }}/config.yml
        owner: root
        group: root
        mode: '0644'
      notify: Restart app
    
    - name: Ensure app is running
      systemd:
        name: "{{ app_name }}"
        state: started
        enabled: true
  
  handlers:
    - name: Restart app
      systemd:
        name: "{{ app_name }}"
        state: restarted

```

### 3.5 Roles

```yaml
# roles/nginx/tasks/main.yml
---
- name: Install nginx
  apt:
    name: nginx
    state: present
  tags: nginx

- name: Configure nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Reload nginx
  tags: nginx

- name: Configure site
  template:
    src: site.conf.j2
    dest: /etc/nginx/sites-available/{{ site_name }}.conf
  notify: Reload nginx
  tags: nginx

- name: Enable site
  file:
    src: /etc/nginx/sites-available/{{ site_name }}.conf
    dest: /etc/nginx/sites-enabled/{{ site_name }}.conf
    state: link
  notify: Reload nginx
  tags: nginx

- name: Ensure nginx is running
  systemd:
    name: nginx
    state: started
    enabled: true
  tags: nginx

```

```yaml
# roles/nginx/handlers/main.yml
---
- name: Reload nginx
  systemd:
    name: nginx
    state: reloaded

- name: Restart nginx
  systemd:
    name: nginx
    state: restarted

```

```yaml
# roles/nginx/defaults/main.yml
---
nginx_worker_processes: auto
nginx_worker_connections: 1024
site_name: default
upstream_servers: []

```

```jinja2

{# roles/nginx/templates/site.conf.j2 #}
upstream {{ site_name }}_backend {
{% for server in upstream_servers %}
    server {{ server }};
{% endfor %}
}

server {
    listen 80;
    server_name {{ server_name }};
    
    location / {
        proxy_pass http://{{ site_name }}_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
    location /health {
        return 200 'OK';
        add_header Content-Type text/plain;
    }
}

```

### 3.6 Ansible Workflow

```bash
# Проверка синтаксиса
ansible-playbook playbooks/site.yml --syntax-check

# Dry run (check mode)
ansible-playbook playbooks/site.yml --check

# Запуск playbook
ansible-playbook -i inventory/production.yml playbooks/site.yml

# Только определённые теги
ansible-playbook playbooks/site.yml --tags "nginx"

# Только определённые хосты
ansible-playbook playbooks/site.yml --limit "web1.example.com"

# С дополнительными переменными
ansible-playbook playbooks/site.yml -e "app_version=2.0.0"

```

---

## 4. Terraform vs Ansible

### 4.1 Сравнение

| Аспект | Terraform | Ansible |
|--------|-----------|---------|
| Тип | Provisioning | Configuration Management |
| Подход | Declarative | Imperative (но декларативный синтаксис) |
| State | Да (terraform.tfstate) | Нет |
| Агент | Нет | Нет (SSH) |
| Идемпотентность | Встроенная | Зависит от модуля |
| Лучше для | Создание инфраструктуры | Настройка серверов |

### 4.2 Когда что использовать

```python

def choose_tool(task: str) -> str:
    """Choose between Terraform and Ansible."""
    
    terraform_tasks = [
        "create_cloud_resources",    # EC2, RDS, S3
        "manage_networking",          # VPC, subnets, routes
        "provision_kubernetes",       # EKS, GKE
        "setup_dns",                  # Route53, CloudFlare
        "manage_state",               # Нужно отслеживать ресурсы
    ]
    
    ansible_tasks = [
        "configure_servers",          # Install packages
        "deploy_applications",        # Copy files, restart services
        "manage_users",               # Create users, SSH keys
        "update_configs",             # Change configuration files
        "run_commands",               # Ad-hoc commands
    ]
    
    if task in terraform_tasks:
        return "terraform"
    elif task in ansible_tasks:
        return "ansible"
    else:
        return "both"  # Часто используются вместе

```

### 4.3 Интеграция Terraform + Ansible

```hcl
# Terraform создаёт инфраструктуру
resource "aws_instance" "web" {
  count         = 3
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.medium"
  
  tags = {
    Name = "web-${count.index + 1}"
    Role = "webserver"
  }
}

# Генерируем inventory для Ansible
resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tpl", {
    web_servers = aws_instance.web[*].public_ip
  })
  filename = "${path.module}/../ansible/inventory/terraform_hosts.yml"
}

# Запускаем Ansible после создания
resource "null_resource" "ansible" {
  depends_on = [aws_instance.web, local_file.ansible_inventory]
  
  provisioner "local-exec" {
    command = "ansible-playbook -i ../ansible/inventory/terraform_hosts.yml ../ansible/playbooks/webservers.yml"
    
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }
}

```

---

## 5. Best Practices

### 5.1 Version Control

```gitignore
# .gitignore для Terraform
*.tfstate
*.tfstate.backup
.terraform/
*.tfvars
!example.tfvars
crash.log
override.tf
override.tf.json
*_override.tf
*_override.tf.json
.terraformrc
terraform.rc

```

### 5.2 State Management

```hcl
# Удалённый state с locking
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"  # Locking
  }
}

```

```python
# State management best practices
state_best_practices = [
    "Всегда использовать remote state (S3, GCS, Azure Blob)",
    "Включить state locking (DynamoDB, GCS, Azure Blob)",
    "Шифровать state at rest",
    "Ограничить доступ к state (sensitive data!)",
    "Использовать workspaces или отдельные states для environments",
    "Регулярно делать backup state",
]

```

### 5.3 Secrets Management

```hcl
# ❌ Плохо: секреты в коде
resource "aws_db_instance" "db" {
  password = "supersecretpassword"  # НЕТ!
}

# ✅ Хорошо: секреты из Vault или переменных
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "production/db/password"
}

resource "aws_db_instance" "db" {
  password = data.aws_secretsmanager_secret_version.db_password.secret_string
}

# Или через переменные (передаются при запуске)
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true  # Скрыть в логах
}

resource "aws_db_instance" "db" {
  password = var.db_password
}

```

### 5.4 Модульность

```hcl
# Хорошая модульная структура
module "vpc" {
  source = "./modules/vpc"
  
  name        = "production"
  cidr_block  = "10.0.0.0/16"
  environment = "production"
}

module "web_cluster" {
  source = "./modules/ec2-cluster"
  
  name       = "web"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnet_ids
  
  instance_count = 3
  instance_type  = "t3.large"
}

module "database" {
  source = "./modules/rds"
  
  name       = "production-db"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
  
  instance_class = "db.r5.large"
  password       = var.db_password
}

```

### 5.5 Testing

```bash
# Terraform testing
# 1. Validate
terraform validate

# 2. Plan и сохранить
terraform plan -out=plan.tfplan

# 3. Проверить plan визуально или автоматически
# (используя tools вроде terraform-compliance, checkov)

# 4. Apply только проверенный plan
terraform apply plan.tfplan

```

```yaml
# CI для Terraform
name: Terraform

on:
  pull_request:
    paths:
      - 'terraform/**'

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0
      
      - name: Terraform Format
        run: terraform fmt -check -recursive
        working-directory: terraform
      
      - name: Terraform Init
        run: terraform init -backend=false
        working-directory: terraform
      
      - name: Terraform Validate
        run: terraform validate
        working-directory: terraform
      
      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform
          framework: terraform
      
      - name: Terraform Plan
        run: terraform plan -no-color
        working-directory: terraform
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

```

---

## 6. Другие инструменты IaC

### 6.1 Pulumi

IaC с использованием обычных языков программирования.

```python
# Pulumi с Python
import pulumi
import pulumi_aws as aws

# VPC
vpc = aws.ec2.Vpc(
    "my-vpc",
    cidr_block="10.0.0.0/16",
    tags={"Name": "my-vpc"}
)

# EC2 Instance
instance = aws.ec2.Instance(
    "web-server",
    instance_type="t3.medium",
    ami="ami-12345678",
    vpc_security_group_ids=[security_group.id],
    tags={"Name": "web-server"}
)

# Export outputs
pulumi.export("instance_ip", instance.public_ip)
pulumi.export("vpc_id", vpc.id)

```

### 6.2 CloudFormation (AWS)

```yaml
# AWS CloudFormation
AWSTemplateFormatVersion: '2010-09-09'
Description: Web server stack

Parameters:
  InstanceType:
    Type: String
    Default: t3.medium
    AllowedValues:
      - t3.small
      - t3.medium
      - t3.large

Resources:
  WebServer:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: ami-12345678
      Tags:
        - Key: Name
          Value: web-server

Outputs:
  InstanceId:
    Description: Instance ID
    Value: !Ref WebServer

```

### 6.3 Сравнение инструментов

| Tool | Language | State | Cloud Support | Learning Curve |
|------|----------|-------|---------------|----------------|
| Terraform | HCL | Remote | Multi-cloud | Medium |
| Pulumi | Python/TS/Go | Remote | Multi-cloud | Depends on lang |
| CloudFormation | YAML/JSON | AWS | AWS only | Medium |
| Ansible | YAML | No | Multi-cloud | Low |
| CDK | TypeScript/Python | CloudFormation | AWS | Medium |

---

## 💡 Key Takeaways

- **IaC = инфраструктура как код**: Версионирование, review, автоматизация

- **Declarative vs Imperative**: Terraform (что хотим) vs Ansible (как сделать)

- **State — критически важен**: Remote state + locking + encryption

- **Модульность**: Переиспользуемые модули для DRY

- **Terraform + Ansible вместе**: Terraform для provisioning, Ansible для configuration

---

## 🚀 Next Steps

**Related Modules:**

- [07_GitOps](../07_GitOps/) — GitOps workflow
- [05_CD](../05_CD/) — CD integration с IaC

**Practice Ideas:**

1. Создайте VPC + EC2 с Terraform
2. Напишите Ansible playbook для настройки веб-сервера
3. Настройте CI для проверки Terraform кода

**Going Deeper:**

- Terraform documentation
- Ansible Galaxy (roles)
- HashiCorp Learn

---

## 📚 Additional Resources

**Books:**

- "Infrastructure as Code" by Kief Morris
- "Terraform: Up & Running" by Yevgeniy Brikman

**Documentation:**

- [Terraform Registry](https://registry.terraform.io/)
- [Ansible Documentation](https://docs.ansible.com/)
- [Pulumi Documentation](https://www.pulumi.com/docs/)

**Certifications:**

- HashiCorp Certified: Terraform Associate
- Red Hat Certified Specialist in Ansible Automation

---




