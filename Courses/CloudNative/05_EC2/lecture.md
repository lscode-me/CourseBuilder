# EC2: Elastic Compute Cloud

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать модели сервисов (IaaS)
- Знать основы IAM (роли для EC2)
- Иметь базовые знания Linux

**Recommended prior modules:**

- [IAM](../04_IAM/) — управление доступом
- [Модели сервисов](../02_ServiceModels/) — понимание IaaS

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Запускать и управлять EC2 инстансами
- Выбирать правильный тип инстанса для задачи
- Настраивать Auto Scaling Groups
- Понимать pricing models (On-Demand, Reserved, Spot)
- Работать с EBS volumes и AMIs

---

## 1. Введение в EC2

### 1.1 Что такое EC2

**Amazon Elastic Compute Cloud (EC2)** — это сервис виртуальных серверов в облаке. EC2 позволяет запускать виртуальные машины (instances) с различными конфигурациями CPU, памяти, storage и сети.

```python

ec2_key_concepts = {
    "Instance": "Виртуальный сервер",
    "AMI": "Amazon Machine Image — образ ОС",
    "Instance Type": "Конфигурация hardware (CPU, RAM)",
    "EBS": "Elastic Block Store — постоянные диски",
    "Security Group": "Виртуальный firewall",
    "Key Pair": "SSH ключи для доступа",
    "Elastic IP": "Статический публичный IP"
}

for concept, description in ec2_key_concepts.items():
    print(f"  {concept}: {description}")

```

**Output:**
```

  Instance: Виртуальный сервер
  AMI: Amazon Machine Image — образ ОС
  Instance Type: Конфигурация hardware (CPU, RAM)
  EBS: Elastic Block Store — постоянные диски
  Security Group: Виртуальный firewall
  Key Pair: SSH ключи для доступа
  Elastic IP: Статический публичный IP

```

### 1.2 История EC2

```

┌───────────────────────────────────────────────────────────────────┐
│                      EC2 Evolution                                │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  2006 ─── EC2 Beta Launch (только Linux, m1.small)                │
│  2008 ─── Windows support, Elastic IPs, Availability Zones        │
│  2009 ─── Reserved Instances, Auto Scaling, Load Balancing        │
│  2010 ─── Micro instances (free tier), Cluster instances          │
│  2012 ─── SSD-backed instances, HVM virtualization                │
│  2014 ─── T2 (burstable), R3 (memory), C4 (compute)               │
│  2017 ─── Nitro System (custom hypervisor)                        │
│  2018 ─── Graviton (ARM processors)                               │
│  2020 ─── Graviton2 (40% better price/performance)                │
│  2021 ─── Graviton3                                               │
│  2023 ─── Graviton4, Inf2 (ML inference)                          │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

---

## 2. Instance Types

### 2.1 Naming Convention

```

Instance Type: m5.2xlarge

  m   = Instance Family (General Purpose)
  5   = Generation (5th generation)
  2xlarge = Size

┌────────────────────────────────────────────────────────────────┐
│ Family │ Use Case                    │ Examples                │
├────────┼─────────────────────────────┼─────────────────────────┤
│   M    │ General Purpose             │ m7g, m6i, m5            │
│   C    │ Compute Optimized           │ c7g, c6i, c5            │
│   R    │ Memory Optimized            │ r7g, r6i, r5            │
│   T    │ Burstable (variable load)   │ t4g, t3, t2             │
│   I    │ Storage Optimized (NVMe)    │ i4i, i3                 │
│   P/G  │ GPU (ML, Graphics)          │ p5, p4d, g5             │
│   Inf  │ ML Inference               │ inf2, inf1               │
│   Trn  │ ML Training                │ trn1                     │
└────────────────────────────────────────────────────────────────┘

Suffixes:
  g = Graviton (ARM) - лучший price/performance
  i = Intel
  a = AMD
  d = NVMe SSD storage
  n = Enhanced networking

```

### 2.2 Размеры инстансов

```python
# T3 family sizes
t3_sizes = {
    "nano":    {"vcpu": 2, "memory_gb": 0.5, "price_hr": 0.0052},
    "micro":   {"vcpu": 2, "memory_gb": 1,   "price_hr": 0.0104},
    "small":   {"vcpu": 2, "memory_gb": 2,   "price_hr": 0.0208},
    "medium":  {"vcpu": 2, "memory_gb": 4,   "price_hr": 0.0416},
    "large":   {"vcpu": 2, "memory_gb": 8,   "price_hr": 0.0832},
    "xlarge":  {"vcpu": 4, "memory_gb": 16,  "price_hr": 0.1664},
    "2xlarge": {"vcpu": 8, "memory_gb": 32,  "price_hr": 0.3328},
}

print("T3 Instance Sizes (us-east-1):\n")
print(f"{'Size':<10} {'vCPU':<6} {'Memory':<10} {'$/hour':<10}")
print("-" * 40)
for size, specs in t3_sizes.items():
    print(f"{size:<10} {specs['vcpu']:<6} {specs['memory_gb']} GB{'':<5} ${specs['price_hr']:.4f}")

```

**Output:**
```

T3 Instance Sizes (us-east-1):

Size       vCPU   Memory     $/hour    
----------------------------------------
nano       2      0.5 GB     $0.0052
micro      2      1 GB       $0.0104
small      2      2 GB       $0.0208
medium     2      4 GB       $0.0416
large      2      8 GB       $0.0832
xlarge     4      16 GB      $0.1664
2xlarge    8      32 GB      $0.3328

```

### 2.3 Выбор типа инстанса

```python

use_case_recommendations = {
    "Web application": {
        "recommendation": "t3.medium или t3.large",
        "why": "Burstable, cost-effective для переменной нагрузки"
    },
    "Database": {
        "recommendation": "r6g.xlarge или r6i.xlarge",
        "why": "Memory optimized для кэширования данных"
    },
    "Batch processing": {
        "recommendation": "c6g.xlarge или c6i.xlarge",
        "why": "Compute optimized для CPU-intensive задач"
    },
    "ML Training": {
        "recommendation": "p4d.24xlarge или trn1.32xlarge",
        "why": "GPU/специализированные чипы для ML"
    },
    "Development/Testing": {
        "recommendation": "t3.micro (free tier) или t3.small",
        "why": "Дёшево, достаточно для разработки"
    }
}

print("Instance Type Recommendations:\n")
for use_case, rec in use_case_recommendations.items():
    print(f"📌 {use_case}")
    print(f"   → {rec['recommendation']}")
    print(f"   Why: {rec['why']}\n")

```

---

## 3. Pricing Models

### 3.1 Сравнение моделей

```

┌───────────────────────────────────────────────────────────────────┐
│                    EC2 Pricing Models                             │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ON-DEMAND                                                        │
│  ├── Оплата по часам/секундам                                     │
│  ├── Нет commitment                                               │
│  ├── Полная гибкость                                              │
│  └── Цена: базовая (100%)                                         │
│                                                                   │
│  RESERVED INSTANCES (RI)                                          │
│  ├── Commitment на 1 или 3 года                                   │
│  ├── Payment: All Upfront / Partial / No Upfront                  │
│  ├── Standard RI или Convertible RI                               │
│  └── Скидка: до 72% от On-Demand                                  │
│                                                                   │
│  SAVINGS PLANS                                                    │
│  ├── Commitment на $/hour usage                                   │
│  ├── Compute SP (любой instance, region, OS)                      │
│  ├── EC2 Instance SP (конкретная family в регионе)                │
│  └── Скидка: до 72% от On-Demand                                  │
│                                                                   │
│  SPOT INSTANCES                                                   │
│  ├── Неиспользуемая capacity AWS                                  │
│  ├── Может быть прервана с 2-min warning                          │
│  ├── Подходит для fault-tolerant workloads                        │
│  └── Скидка: до 90% от On-Demand                                  │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

### 3.2 Пример расчёта экономии

```python

def calculate_monthly_cost(
    instance_type: str,
    hourly_rate: float,
    hours_per_month: int = 730
) -> dict:
    """Расчёт месячной стоимости по разным моделям"""
    
    on_demand = hourly_rate * hours_per_month
    
    # Примерные скидки
    ri_1yr_no_upfront = on_demand * 0.60     # 40% скидка
    ri_3yr_all_upfront = on_demand * 0.35    # 65% скидка
    spot_avg = on_demand * 0.30              # 70% скидка
    
    return {
        "instance_type": instance_type,
        "on_demand": round(on_demand, 2),
        "ri_1yr": round(ri_1yr_no_upfront, 2),
        "ri_3yr": round(ri_3yr_all_upfront, 2),
        "spot": round(spot_avg, 2)
    }

# m5.xlarge пример
costs = calculate_monthly_cost("m5.xlarge", 0.192)

print(f"Monthly cost for {costs['instance_type']}:")
print(f"  On-Demand:     ${costs['on_demand']}")
print(f"  RI 1yr:        ${costs['ri_1yr']} (save ${costs['on_demand'] - costs['ri_1yr']:.2f})")
print(f"  RI 3yr:        ${costs['ri_3yr']} (save ${costs['on_demand'] - costs['ri_3yr']:.2f})")
print(f"  Spot:          ${costs['spot']} (save ${costs['on_demand'] - costs['spot']:.2f})")

```

**Output:**
```

Monthly cost for m5.xlarge:
  On-Demand:     $140.16
  RI 1yr:        $84.1 (save $56.06)
  RI 3yr:        $49.06 (save $91.10)
  Spot:          $42.05 (save $98.11)

```

---

## 4. Launch и Management

### 4.1 Запуск инстанса через CLI

```bash
# Запуск EC2 инстанса
aws ec2 run-instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --instance-type t3.micro \
    --key-name my-key-pair \
    --security-group-ids sg-12345678 \
    --subnet-id subnet-12345678 \
    --iam-instance-profile Name=EC2-S3-Access \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=my-server},{Key=Environment,Value=dev}]' \
    --user-data file://bootstrap.sh

```

### 4.2 User Data (bootstrap script)

```bash
#!/bin/bash
# bootstrap.sh - выполняется при первом запуске

# Обновление системы
yum update -y

# Установка приложений
yum install -y docker nginx

# Запуск сервисов
systemctl enable docker nginx
systemctl start docker nginx

# Настройка приложения
aws s3 cp s3://my-bucket/app-config.json /etc/app/config.json

# Логирование
echo "Bootstrap completed at $(date)" >> /var/log/bootstrap.log

```

### 4.3 Instance Metadata Service (IMDS)

```bash
# Получение информации об инстансе изнутри
# IMDSv2 (рекомендуется - требует токен)

# Получение токена
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
    -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Использование токена
curl -H "X-aws-ec2-metadata-token: $TOKEN" \
    http://169.254.169.254/latest/meta-data/instance-id

curl -H "X-aws-ec2-metadata-token: $TOKEN" \
    http://169.254.169.254/latest/meta-data/instance-type

curl -H "X-aws-ec2-metadata-token: $TOKEN" \
    http://169.254.169.254/latest/meta-data/local-ipv4

# Получение IAM credentials (для роли)
curl -H "X-aws-ec2-metadata-token: $TOKEN" \
    http://169.254.169.254/latest/meta-data/iam/security-credentials/MyRole

```

---

## 5. Amazon Machine Images (AMI)

### 5.1 Типы AMI

```python

ami_types = {
    "AWS Managed": {
        "examples": ["Amazon Linux 2023", "Ubuntu", "Windows Server"],
        "maintained_by": "AWS",
        "updates": "Регулярные обновления"
    },
    "AWS Marketplace": {
        "examples": ["Bitnami stacks", "CIS hardened images"],
        "maintained_by": "Third-party vendors",
        "updates": "Зависит от vendor"
    },
    "Community AMIs": {
        "examples": ["Custom builds от сообщества"],
        "maintained_by": "Community",
        "updates": "Нет гарантий"
    },
    "Custom AMIs": {
        "examples": ["Your own golden images"],
        "maintained_by": "You",
        "updates": "Ваша ответственность"
    }
}

print("AMI Types:\n")
for ami_type, details in ami_types.items():
    print(f"  {ami_type}:")
    print(f"    Examples: {', '.join(details['examples'][:2])}")
    print(f"    Maintained by: {details['maintained_by']}\n")

```

### 5.2 Создание Custom AMI

```bash
# 1. Настройте инстанс как нужно

# 2. Создайте AMI
aws ec2 create-image \
    --instance-id i-1234567890abcdef0 \
    --name "my-app-golden-image-v1.0" \
    --description "Pre-configured app server" \
    --no-reboot

# 3. Копирование AMI в другой регион (для DR)
aws ec2 copy-image \
    --source-region us-east-1 \
    --source-image-id ami-12345678 \
    --name "my-app-golden-image-v1.0" \
    --region eu-west-1

```

---

## 6. EBS (Elastic Block Store)

### 6.1 Типы EBS volumes

```

┌────────────────────────────────────────────────────────────────────┐
│                      EBS Volume Types                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  gp3 (General Purpose SSD) - РЕКОМЕНДУЕТСЯ                         │
│  ├── IOPS: 3,000 - 16,000 (настраивается отдельно)                 │
│  ├── Throughput: 125 - 1,000 MB/s                                  │
│  ├── Size: 1 GB - 16 TB                                            │
│  └── Use case: Boot volumes, development, web servers              │
│                                                                    │
│  gp2 (General Purpose SSD) - Legacy                                │
│  ├── IOPS: 3 IOPS/GB (burst to 3,000)                              │
│  ├── Size: 1 GB - 16 TB                                            │
│  └── Use case: Старые workloads (мигрируйте на gp3)                │
│                                                                    │
│  io2/io2 Block Express (Provisioned IOPS SSD)                      │
│  ├── IOPS: до 256,000                                              │
│  ├── Multi-attach support                                          │
│  └── Use case: Databases, latency-sensitive apps                   │
│                                                                    │
│  st1 (Throughput Optimized HDD)                                    │
│  ├── Throughput: 500 MB/s                                          │
│  ├── НЕ может быть boot volume                                     │
│  └── Use case: Big data, data warehouses, log processing           │
│                                                                    │
│  sc1 (Cold HDD)                                                    │
│  ├── Throughput: 250 MB/s                                          │
│  ├── Lowest cost                                                   │
│  └── Use case: Архивы, редко используемые данные                   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

### 6.2 EBS Snapshots

```bash
# Создание snapshot
aws ec2 create-snapshot \
    --volume-id vol-12345678 \
    --description "Daily backup $(date +%Y-%m-%d)"

# Создание volume из snapshot
aws ec2 create-volume \
    --snapshot-id snap-12345678 \
    --availability-zone us-east-1a \
    --volume-type gp3

# Копирование snapshot в другой регион
aws ec2 copy-snapshot \
    --source-region us-east-1 \
    --source-snapshot-id snap-12345678 \
    --destination-region eu-west-1

```

---

## 7. Auto Scaling

### 7.1 Компоненты Auto Scaling

```

┌───────────────────────────────────────────────────────────────────┐
│                    Auto Scaling Components                        │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────┐                                          │
│  │   Launch Template   │ ◄── AMI, instance type, user data        │
│  └──────────┬──────────┘                                          │
│             │                                                     │
│             ▼                                                     │
│  ┌─────────────────────┐                                          │
│  │  Auto Scaling Group │                                          │
│  │                     │                                          │
│  │  Min: 2             │ ◄── Минимум инстансов                    │
│  │  Max: 10            │ ◄── Максимум инстансов                   │
│  │  Desired: 4         │ ◄── Желаемое количество                  │
│  │                     │                                          │
│  │  AZs: 1a, 1b, 1c   │ ◄── Распределение по AZ                   │
│  │                     │                                          │
│  └──────────┬──────────┘                                          │
│             │                                                     │
│             ▼                                                     │
│  ┌─────────────────────┐                                          │
│  │  Scaling Policies   │                                          │
│  │                     │                                          │
│  │  • Target Tracking  │ ◄── CPU = 70%                            │
│  │  • Step Scaling     │ ◄── Rules based on metrics               │
│  │  • Scheduled        │ ◄── Scale at specific times              │
│  │                     │                                          │
│  └─────────────────────┘                                          │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

### 7.2 Пример Launch Template

```bash
# Создание Launch Template
aws ec2 create-launch-template \
    --launch-template-name my-app-template \
    --version-description "v1" \
    --launch-template-data '{
        "ImageId": "ami-12345678",
        "InstanceType": "t3.medium",
        "KeyName": "my-key",
        "SecurityGroupIds": ["sg-12345678"],
        "IamInstanceProfile": {
            "Arn": "arn:aws:iam::123456789012:instance-profile/MyProfile"
        },
        "UserData": "IyEvYmluL2Jhc2gKeXVtIHVwZGF0ZSAteQ==",
        "TagSpecifications": [{
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "my-app-server"}]
        }]
    }'

```

### 7.3 Создание Auto Scaling Group

```bash

aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name my-app-asg \
    --launch-template LaunchTemplateName=my-app-template,Version='$Latest' \
    --min-size 2 \
    --max-size 10 \
    --desired-capacity 4 \
    --vpc-zone-identifier "subnet-1a,subnet-1b,subnet-1c" \
    --target-group-arns "arn:aws:elasticloadbalancing:..." \
    --health-check-type ELB \
    --health-check-grace-period 300

# Target Tracking Policy
aws autoscaling put-scaling-policy \
    --auto-scaling-group-name my-app-asg \
    --policy-name cpu-target-tracking \
    --policy-type TargetTrackingScaling \
    --target-tracking-configuration '{
        "TargetValue": 70.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "ASGAverageCPUUtilization"
        }
    }'

```

---

## 8. Placement Groups

```python

placement_group_types = {
    "cluster": {
        "description": "Все инстансы в одном rack",
        "latency": "Lowest (< 1ms)",
        "use_case": "HPC, ML training, low-latency apps",
        "availability": "Single point of failure"
    },
    "spread": {
        "description": "Каждый инстанс на отдельном hardware",
        "latency": "Normal",
        "use_case": "Critical applications, max availability",
        "availability": "Highest (max 7 instances per AZ)"
    },
    "partition": {
        "description": "Группы инстансов на разном hardware",
        "latency": "Normal",
        "use_case": "HDFS, Cassandra, Kafka",
        "availability": "High (up to 7 partitions per AZ)"
    }
}

print("Placement Group Types:\n")
for pg_type, details in placement_group_types.items():
    print(f"  {pg_type.upper()}:")
    print(f"    {details['description']}")
    print(f"    Use case: {details['use_case']}\n")

```

---

## 9. Common Pitfalls

### 9.1 Pitfall: Неправильный instance type

❌ **Проблема:**
```python
# "Возьмём самый большой для надёжности"
instance = "m5.24xlarge"  # $4.60/hr = $3,300+/month!

```

✅ **Решение:**
```python
# Начните с меньшего, мониторьте, масштабируйте
# 1. Начните с t3.medium
# 2. Смотрите CloudWatch metrics (CPU, Memory)
# 3. Увеличивайте если нужно

# Используйте AWS Compute Optimizer для рекомендаций
```

### 9.2 Pitfall: EBS не удаляется с инстансом

❌ **Проблема:**
```bash
# По умолчанию root EBS может сохраняться после terminate
# Забытые volumes = лишние расходы
```

✅ **Решение:**
```json

// В Launch Template
{
    "BlockDeviceMappings": [{
        "DeviceName": "/dev/xvda",
        "Ebs": {
            "DeleteOnTermination": true,
            "VolumeType": "gp3"
        }
    }]
}

```

---

## 💡 Key Takeaways

- **Instance Types** — выбирайте по workload (M-general, C-compute, R-memory, T-burstable)

- **Graviton (ARM)** — лучший price/performance для большинства workloads

- **Pricing** — комбинируйте On-Demand, Reserved, Spot для оптимизации

- **Auto Scaling** — используйте для эластичности и HA

- **EBS gp3** — рекомендуется вместо gp2, настраиваемые IOPS отдельно

- **AMIs** — создавайте golden images для быстрого и консистентного деплоя

---

## 🚀 Next Steps

**Следующие модули:**

- [S3](../06_S3/) — объектное хранилище
- [VPC](../07_VPC/) — сетевая инфраструктура

**Практические задания:**

1. Запустите t3.micro в Free Tier
2. Создайте custom AMI
3. Настройте Auto Scaling Group с Target Tracking
4. Сравните производительность gp2 vs gp3

---

## 📚 Additional Resources

**Documentation:**

- [EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)
- [Instance Types](https://aws.amazon.com/ec2/instance-types/)

**Tools:**

- [EC2 Instance Comparison](https://instances.vantage.sh/)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)

---




