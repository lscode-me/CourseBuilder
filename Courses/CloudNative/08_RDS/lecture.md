# RDS: Relational Database Service

---

## 📋 Prerequisites

- Базовые знания SQL и реляционных БД
- Понимание VPC и Security Groups
- Знакомство с концепциями HA

---

## 🎯 Learning Objectives

- Создавать и управлять RDS инстансами
- Настраивать Multi-AZ для высокой доступности
- Использовать Read Replicas для масштабирования
- Понимать Aurora и её преимущества

---

## 1. Введение в RDS

### 1.1 Что такое RDS

**Amazon RDS (Relational Database Service)** — управляемый сервис реляционных баз данных. AWS берёт на себя: установку, патчинг, бэкапы, репликацию, failover.

```python

rds_supported_engines = {
    "MySQL": {"versions": "5.7, 8.0", "port": 3306},
    "PostgreSQL": {"versions": "12-16", "port": 5432},
    "MariaDB": {"versions": "10.4-10.11", "port": 3306},
    "Oracle": {"versions": "19c, 21c", "port": 1521},
    "SQL Server": {"versions": "2017-2022", "port": 1433},
    "Aurora MySQL": {"versions": "MySQL 5.7, 8.0 compatible", "port": 3306},
    "Aurora PostgreSQL": {"versions": "PostgreSQL 12-16 compatible", "port": 5432}
}

print("RDS Supported Engines:")
for engine, details in rds_supported_engines.items():
    print(f"  • {engine}: {details['versions']}")

```

### 1.2 RDS vs Self-Managed

```

┌────────────────────────────────────────────────────────────────────┐
│              RDS vs Self-Managed Database                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Task                     Self-Managed    RDS                      │
│  ─────────────────────    ────────────    ───                      │
│  Hardware provisioning    You             AWS                      │
│  OS installation          You             AWS                      │
│  Database installation    You             AWS                      │
│  OS patching              You             AWS                      │
│  Database patching        You             AWS (maintenance window) │
│  Backups                  You             AWS (automated)          │
│  High availability        You             AWS (Multi-AZ)           │
│  Scaling storage          You             AWS (auto-scaling)       │
│  Monitoring               You             AWS (CloudWatch)         │
│  ─────────────────────                                             │
│  Schema design            You             You                      │
│  Query optimization       You             You                      │
│  Data                     You             You                      │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 2. Создание RDS Instance

### 2.1 Через CLI

```bash

aws rds create-db-instance \
    --db-instance-identifier mydb \
    --db-instance-class db.t3.medium \
    --engine postgres \
    --engine-version 16.1 \
    --master-username admin \
    --master-user-password 'SecurePassword123!' \
    --allocated-storage 100 \
    --storage-type gp3 \
    --storage-encrypted \
    --kms-key-id alias/aws/rds \
    --vpc-security-group-ids sg-12345678 \
    --db-subnet-group-name my-db-subnet-group \
    --backup-retention-period 7 \
    --preferred-backup-window "03:00-04:00" \
    --preferred-maintenance-window "Mon:04:00-Mon:05:00" \
    --multi-az \
    --publicly-accessible false \
    --tags Key=Environment,Value=production

```

### 2.2 DB Subnet Group

```bash
# RDS требует subnet group с subnets минимум в 2 AZ
aws rds create-db-subnet-group \
    --db-subnet-group-name my-db-subnet-group \
    --db-subnet-group-description "Subnets for RDS" \
    --subnet-ids subnet-1a subnet-1b subnet-1c

```

---

## 3. High Availability: Multi-AZ

### 3.1 Как работает Multi-AZ

```

┌──────────────────────────────────────────────────────────────────┐
│                    RDS Multi-AZ Deployment                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Application                                                     │
│      │                                                           │
│      ▼                                                           │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              DNS Endpoint (mydb.xxx.rds.amazonaws.com)       ││
│  │              Points to Primary (automatic failover)          ││
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│            ┌──────────────┴──────────────┐                       │
│            │                             │                       │
│            ▼                             ▼                       │
│  ┌──────────────────┐         ┌──────────────────┐               │
│  │  AZ: us-east-1a  │         │  AZ: us-east-1b  │               │
│  │                  │         │                  │               │
│  │  ┌────────────┐  │         │  ┌────────────┐  │               │
│  │  │  PRIMARY   │  │ ──────► │  │  STANDBY   │  │               │
│  │  │  (active)  │  │  Sync   │  │  (passive) │  │               │
│  │  │            │  │  Repl   │  │            │  │               │
│  │  └────────────┘  │         │  └────────────┘  │               │
│  │                  │         │                  │               │
│  └──────────────────┘         └──────────────────┘               │
│                                                                  │
│  • Synchronous replication                                       │
│  • Automatic failover (60-120 seconds)                           │
│  • Same endpoint after failover                                  │
│  • Standby not accessible for reads                              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

```

### 3.2 Когда происходит Failover

```python

failover_triggers = [
    "Primary instance failure",
    "AZ failure",
    "DB instance type change",
    "OS patching during maintenance",
    "Manual failover (for testing)",
    "Rebooting with failover option"
]

print("Multi-AZ Failover Triggers:")
for trigger in failover_triggers:
    print(f"  • {trigger}")

# Тестирование failover
# aws rds reboot-db-instance --db-instance-identifier mydb --force-failover
```

---

## 4. Read Replicas

### 4.1 Как работают Read Replicas

```

┌────────────────────────────────────────────────────────────────────┐
│                    RDS Read Replicas                               │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Application                                                       │
│      │                                                             │
│      ├─── Writes ───► Primary DB (mydb.xxx.rds.amazonaws.com)      │
│      │                    │                                        │
│      │                    │ Async Replication                      │
│      │                    ▼                                        │
│      │              ┌─────────────┐                                │
│      │              │             │                                │
│      └─── Reads ───►│ Read        │ (mydb-replica.xxx.rds...)      │
│                     │ Replica 1   │                                │
│      └─── Reads ───►│             │                                │
│                     │ Read        │                                │
│                     │ Replica 2   │ (другой регион возможен)       │
│                     │             │                                │
│                     └─────────────┘                                │
│                                                                    │
│  Характеристики:                                                   │
│  • Asynchronous replication (eventual consistency)                 │
│  • До 15 Read Replicas для Aurora, 5 для других                    │
│  • Can be in different region (Cross-Region)                       │
│  • Can be promoted to standalone DB                                │
│  • Отдельный endpoint для каждой реплики                           │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

### 4.2 Создание Read Replica

```bash
# Создание Read Replica
aws rds create-db-instance-read-replica \
    --db-instance-identifier mydb-replica \
    --source-db-instance-identifier mydb \
    --db-instance-class db.t3.medium

# Cross-Region Replica
aws rds create-db-instance-read-replica \
    --db-instance-identifier mydb-eu-replica \
    --source-db-instance-identifier arn:aws:rds:us-east-1:123456789012:db:mydb \
    --db-instance-class db.t3.medium \
    --region eu-west-1

```

### 4.3 Read Replica vs Multi-AZ

```python

comparison = {
    "Purpose": {
        "Multi-AZ": "High Availability (failover)",
        "Read Replica": "Scalability (read traffic)"
    },
    "Replication": {
        "Multi-AZ": "Synchronous",
        "Read Replica": "Asynchronous"
    },
    "Readable": {
        "Multi-AZ": "No (standby only)",
        "Read Replica": "Yes"
    },
    "Failover": {
        "Multi-AZ": "Automatic",
        "Read Replica": "Manual promotion"
    },
    "Cross-Region": {
        "Multi-AZ": "No",
        "Read Replica": "Yes"
    }
}

print("Multi-AZ vs Read Replica:\n")
for aspect, values in comparison.items():
    print(f"  {aspect}:")
    print(f"    Multi-AZ: {values['Multi-AZ']}")
    print(f"    Read Replica: {values['Read Replica']}\n")

```

---

## 5. Amazon Aurora

### 5.1 Что такое Aurora

**Amazon Aurora** — облачная реляционная БД, совместимая с MySQL и PostgreSQL, но с улучшенной производительностью и доступностью.

```

┌───────────────────────────────────────────────────────────────────┐
│                    Aurora Architecture                            │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│           ┌───────────────────────────────────────────┐           │
│           │            Aurora Cluster                  │          │
│           └───────────────────┬───────────────────────┘           │
│                               │                                   │
│          ┌────────────────────┼────────────────────┐              │
│          ▼                    ▼                    ▼              │
│     ┌─────────┐         ┌─────────┐         ┌─────────┐           │
│     │ Writer  │         │ Reader  │         │ Reader  │           │
│     │Instance │         │Instance │         │Instance │           │
│     └────┬────┘         └────┬────┘         └────┬────┘           │
│          │                   │                   │                │
│          └───────────────────┼───────────────────┘                │
│                              │                                    │
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │              Distributed Storage (6 copies, 3 AZs)            ││
│  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐                  │  │
│  │  │Copy│ │Copy│ │Copy│ │Copy│ │Copy│ │Copy│                  │  │
│  │  │ 1  │ │ 2  │ │ 3  │ │ 4  │ │ 5  │ │ 6  │                  │  │
│  │  │AZ-a│ │AZ-a│ │AZ-b│ │AZ-b│ │AZ-c│ │AZ-c│                  │  │
│  │  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘                  │  │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  • Storage auto-scales до 128 TB                                  │
│  • 6 copies across 3 AZs                                          │
│  • Self-healing storage                                           │
│  • До 15 read replicas                                            │
│  • Sub-10ms replica lag                                           │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

### 5.2 Aurora vs Standard RDS

```python

aurora_benefits = {
    "Performance": "5x MySQL, 3x PostgreSQL throughput",
    "Storage": "Auto-scaling 10GB-128TB, 6 copies",
    "Availability": "99.99%, instant failover (<30s)",
    "Read Replicas": "Up to 15 (vs 5 for standard)",
    "Replica Lag": "<10ms (vs seconds for standard)",
    "Backtrack": "Point-in-time recovery without restore",
    "Global Database": "Cross-region replication <1s lag",
    "Serverless": "Auto-scaling compute (v2)"
}

print("Aurora Benefits:")
for benefit, description in aurora_benefits.items():
    print(f"  ✓ {benefit}: {description}")

```

### 5.3 Aurora Serverless v2

```bash
# Aurora Serverless v2 - автомасштабирование compute
aws rds create-db-cluster \
    --db-cluster-identifier my-aurora-serverless \
    --engine aurora-postgresql \
    --engine-version 15.4 \
    --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=16 \
    --master-username admin \
    --master-user-password 'SecurePassword123!'

# ACU (Aurora Capacity Units): 0.5 - 128
# 1 ACU ≈ 2 GB RAM
# Масштабируется за секунды
```

---

## 6. Backup и Recovery

### 6.1 Automated Backups

```python

backup_features = {
    "Automated Backups": {
        "retention": "1-35 days",
        "timing": "Daily during backup window",
        "type": "Full daily + transaction logs",
        "storage": "S3 (managed by AWS)"
    },
    "Manual Snapshots": {
        "retention": "Until you delete",
        "timing": "On demand",
        "type": "Full snapshot",
        "storage": "S3"
    },
    "Point-in-Time Recovery": {
        "granularity": "Any second within retention period",
        "how": "Creates new DB instance",
        "rpo": "~5 minutes"
    }
}

print("RDS Backup Options:")
for backup_type, details in backup_features.items():
    print(f"\n{backup_type}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

```

### 6.2 Восстановление

```bash
# Point-in-Time Recovery
aws rds restore-db-instance-to-point-in-time \
    --source-db-instance-identifier mydb \
    --target-db-instance-identifier mydb-restored \
    --restore-time "2024-01-15T10:30:00Z"

# Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier mydb-restored \
    --db-snapshot-identifier mydb-snapshot-20240115

```

---

## 7. Security

### 7.1 Encryption

```python

rds_security = {
    "Encryption at Rest": {
        "how": "AWS KMS (AES-256)",
        "applies_to": "Storage, backups, snapshots, replicas",
        "note": "Must enable at creation (cannot enable later)"
    },
    "Encryption in Transit": {
        "how": "SSL/TLS",
        "how_to_enforce": "rds.force_ssl parameter",
        "certificates": "AWS managed, auto-rotated"
    },
    "Network Security": {
        "vpc": "Deploy in private subnets",
        "security_groups": "Control inbound traffic",
        "no_public": "publicly-accessible = false"
    },
    "Authentication": {
        "password": "Master user password",
        "iam": "IAM Database Authentication",
        "secrets": "AWS Secrets Manager with rotation"
    }
}

```

### 7.2 IAM Database Authentication

```python

import boto3
import psycopg2

def get_iam_auth_token(host: str, port: int, user: str, region: str) -> str:
    """Generate IAM authentication token for RDS"""
    client = boto3.client('rds', region_name=region)
    token = client.generate_db_auth_token(
        DBHostname=host,
        Port=port,
        DBUsername=user,
        Region=region
    )
    return token

# Использование
host = "mydb.xxx.us-east-1.rds.amazonaws.com"
token = get_iam_auth_token(host, 5432, "iam_user", "us-east-1")

conn = psycopg2.connect(
    host=host,
    port=5432,
    database="mydb",
    user="iam_user",
    password=token,
    sslmode="require"
)

```

---

## 8. Performance Insights

```bash
# Включение Performance Insights
aws rds modify-db-instance \
    --db-instance-identifier mydb \
    --enable-performance-insights \
    --performance-insights-retention-period 7

# Performance Insights показывает:
# • Top SQL queries by load
# • Wait events
# • Database load over time
# • Recommendations
```

---

## 9. Pricing

```python

rds_cost_components = {
    "Instance hours": "Per hour, based on instance class",
    "Storage": "Per GB-month (gp3, io1, magnetic)",
    "I/O requests": "For io1/io2 volumes",
    "Backup storage": "Free up to total DB size, then per GB",
    "Data transfer": "Cross-AZ/region transfer",
    "Snapshots": "Per GB-month for manual snapshots"
}

# Примерные цены (us-east-1)
example_pricing = {
    "db.t3.medium": "$0.068/hour",
    "db.r6g.large": "$0.26/hour", 
    "gp3 storage": "$0.115/GB-month",
    "Multi-AZ": "2x instance cost"
}

print("RDS Pricing Components:")
for component, description in rds_cost_components.items():
    print(f"  • {component}: {description}")

```

---

## 10. Best Practices

```python

rds_best_practices = [
    "Используйте Multi-AZ для production",
    "Включите automated backups (7+ days retention)",
    "Используйте Read Replicas для read-heavy workloads",
    "Размещайте в private subnets",
    "Используйте Parameter Groups для тюнинга",
    "Мониторьте с Performance Insights",
    "Включите Enhanced Monitoring",
    "Используйте Secrets Manager для credentials",
    "Планируйте maintenance window на low-traffic время",
    "Рассмотрите Aurora для критичных workloads"
]

print("RDS Best Practices:")
for i, practice in enumerate(rds_best_practices, 1):
    print(f"  {i}. {practice}")

```

---

## 💡 Key Takeaways

- **RDS** — managed relational database (MySQL, PostgreSQL, etc.)

- **Multi-AZ** — high availability с synchronous replication

- **Read Replicas** — масштабирование чтения, async replication

- **Aurora** — cloud-native, 5x faster, auto-scaling storage

- **Security**: encryption at rest/transit, IAM auth, private subnets

- **Backups**: automated daily + PITR, manual snapshots

---

## 🚀 Next Steps

- [DynamoDB](../09_DynamoDB/) — NoSQL database
- [VPC](../07_VPC/) — network security

---

## 📚 Additional Resources

- [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/)
- [Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/)

---



