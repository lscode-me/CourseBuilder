# Cloud Native Development
## Infrastructure as Code

---

## 📋 Prerequisites

- Базовые знания AWS сервисов
- Понимание YAML/JSON
- Опыт работы с CLI

---

## 🎯 Learning Objectives

- Понимать принципы IaC
- Использовать CloudFormation
- Знать основы Terraform
- Применять best practices

---

## 1. Что такое Infrastructure as Code

### 1.1 Принципы

```
┌────────────────────────────────────────────────────────────────────┐
│              Infrastructure as Code                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Manual Infrastructure                IaC                          │
│  ──────────────────────              ───                           │
│  • Click in console                  • Code in version control     │
│  • Hard to reproduce                 • Reproducible                │
│  • Documentation gets outdated       • Code IS documentation       │
│  • No audit trail                    • Git history = audit trail   │
│  • Error-prone                       • Automated, consistent       │
│  • Slow to scale                     • Scale easily                │
│                                                                     │
│  Key Principles:                                                   │
│  1. Declarative: describe WHAT, not HOW                           │
│  2. Idempotent: same result on repeated runs                      │
│  3. Version controlled: Git for infrastructure                    │
│  4. Self-documenting: code describes current state                │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 IaC Tools

```python
iac_tools = {
    "CloudFormation": {
        "provider": "AWS only",
        "language": "YAML/JSON",
        "state": "Managed by AWS",
        "best_for": "AWS-first teams"
    },
    "Terraform": {
        "provider": "Multi-cloud (AWS, GCP, Azure, etc.)",
        "language": "HCL (HashiCorp Configuration Language)",
        "state": "Local or remote (S3, Terraform Cloud)",
        "best_for": "Multi-cloud, complex infrastructure"
    },
    "AWS CDK": {
        "provider": "AWS only",
        "language": "TypeScript, Python, Java, Go, C#",
        "state": "Generates CloudFormation",
        "best_for": "Developers who prefer real code"
    },
    "Pulumi": {
        "provider": "Multi-cloud",
        "language": "TypeScript, Python, Go, C#",
        "state": "Pulumi Cloud or self-managed",
        "best_for": "Developers, multi-cloud"
    }
}

for tool, details in iac_tools.items():
    print(f"\n{tool}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
```

---

## 2. AWS CloudFormation

### 2.1 Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: My CloudFormation template

Parameters:
  Environment:
    Type: String
    AllowedValues: [dev, staging, prod]
    Default: dev
  
  InstanceType:
    Type: String
    Default: t3.micro

Mappings:
  RegionAMI:
    us-east-1:
      AMI: ami-0123456789abcdef0
    eu-west-1:
      AMI: ami-0987654321fedcba0

Conditions:
  IsProd: !Equals [!Ref Environment, prod]

Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      Tags:
        - Key: Name
          Value: !Sub '${Environment}-vpc'

  MyInstance:
    Type: AWS::EC2::Instance
    Condition: IsProd  # Only create in prod
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: !FindInMap [RegionAMI, !Ref 'AWS::Region', AMI]
      SubnetId: !Ref MySubnet

Outputs:
  VPCId:
    Description: VPC ID
    Value: !Ref MyVPC
    Export:
      Name: !Sub '${Environment}-VPCId'
```

### 2.2 Intrinsic Functions

```yaml
# Reference another resource or parameter
VPCId: !Ref MyVPC

# Get attribute of resource
PublicIP: !GetAtt MyInstance.PublicIp

# String substitution
Name: !Sub '${Environment}-${AWS::StackName}-bucket'

# Join strings
SecurityGroups: !Join [',', [!Ref SG1, !Ref SG2]]

# Conditional
InstanceType: !If [IsProd, m5.large, t3.micro]

# Import from another stack
VPCId: !ImportValue prod-VPCId

# Base64 encode (for UserData)
UserData: !Base64 |
  #!/bin/bash
  yum update -y
```

### 2.3 Deploy Stack

```bash
# Create stack
aws cloudformation create-stack \
    --stack-name my-app-stack \
    --template-body file://template.yaml \
    --parameters ParameterKey=Environment,ParameterValue=prod \
    --capabilities CAPABILITY_IAM

# Update stack
aws cloudformation update-stack \
    --stack-name my-app-stack \
    --template-body file://template.yaml

# Delete stack
aws cloudformation delete-stack --stack-name my-app-stack

# Create change set (preview changes)
aws cloudformation create-change-set \
    --stack-name my-app-stack \
    --template-body file://template.yaml \
    --change-set-name my-changes

aws cloudformation describe-change-set \
    --stack-name my-app-stack \
    --change-set-name my-changes
```

---

## 3. Terraform

### 3.1 Configuration

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
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.region
  
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
```

```hcl
# variables.tf
variable "environment" {
  type        = string
  description = "Environment name"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```

```hcl
# main.tf
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  
  tags = {
    Name = "${var.environment}-vpc"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "${var.environment}-public-${count.index + 1}"
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public[0].id
  
  tags = {
    Name = "${var.environment}-web"
  }
}

# outputs.tf
output "vpc_id" {
  value       = aws_vpc.main.id
  description = "VPC ID"
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### 3.2 Terraform Commands

```bash
# Initialize (download providers, configure backend)
terraform init

# Format code
terraform fmt

# Validate configuration
terraform validate

# Plan (preview changes)
terraform plan -out=tfplan

# Apply changes
terraform apply tfplan

# Destroy infrastructure
terraform destroy

# Import existing resource
terraform import aws_instance.web i-1234567890abcdef0

# Show state
terraform state list
terraform state show aws_vpc.main
```

### 3.3 Modules

```hcl
# modules/vpc/main.tf
variable "cidr_block" {}
variable "environment" {}

resource "aws_vpc" "main" {
  cidr_block = var.cidr_block
  tags = {
    Name = "${var.environment}-vpc"
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

# main.tf (root)
module "vpc" {
  source = "./modules/vpc"
  
  cidr_block  = "10.0.0.0/16"
  environment = var.environment
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"
  
  cluster_name    = "${var.environment}-cluster"
  cluster_version = "1.28"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids
}
```

---

## 4. CloudFormation vs Terraform

```python
comparison = {
    "State Management": {
        "CloudFormation": "AWS manages state",
        "Terraform": "You manage state (S3 + DynamoDB lock)"
    },
    "Multi-Cloud": {
        "CloudFormation": "AWS only",
        "Terraform": "AWS, GCP, Azure, etc."
    },
    "Language": {
        "CloudFormation": "YAML/JSON (verbose)",
        "Terraform": "HCL (more concise)"
    },
    "Drift Detection": {
        "CloudFormation": "Built-in",
        "Terraform": "terraform plan detects drift"
    },
    "Rollback": {
        "CloudFormation": "Automatic on failure",
        "Terraform": "Manual (apply previous state)"
    },
    "Learning Curve": {
        "CloudFormation": "AWS-specific, many AWS users know it",
        "Terraform": "Industry standard, transferable skill"
    }
}

print("CloudFormation vs Terraform:\n")
for aspect, values in comparison.items():
    print(f"{aspect}:")
    print(f"  CF: {values['CloudFormation']}")
    print(f"  TF: {values['Terraform']}\n")
```

---

## 5. Best Practices

```python
iac_best_practices = [
    "Version control ALL infrastructure code",
    "Use modules/nested stacks for reusability",
    "Implement CI/CD for infrastructure",
    "Use remote state with locking (Terraform)",
    "Never store secrets in code (use SSM/Secrets Manager)",
    "Use variables/parameters for environment-specific values",
    "Tag all resources for cost tracking",
    "Implement least privilege IAM",
    "Use change sets/plan before applying",
    "Document with README and comments"
]

print("IaC Best Practices:")
for i, practice in enumerate(iac_best_practices, 1):
    print(f"  {i}. {practice}")
```

---

## 💡 Key Takeaways

- **IaC** — infrastructure in version control, reproducible
- **CloudFormation** — AWS native, managed state
- **Terraform** — multi-cloud, industry standard
- **Modules** — reusable infrastructure components
- **State** — critical for Terraform, needs locking
- **Plan before apply** — always preview changes

---

## 📚 Additional Resources

- [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest)

---
