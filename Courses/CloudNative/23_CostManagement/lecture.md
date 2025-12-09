# Управление затратами

---

## 📋 Prerequisites

- Знакомство с AWS сервисами
- Понимание pricing моделей
- Базовые знания billing

---

## 🎯 Learning Objectives

- Понимать AWS pricing модели
- Оптимизировать затраты
- Использовать Reserved и Spot instances
- Настраивать мониторинг расходов

---

## 1. AWS Pricing Models

### 1.1 Основные модели

```
┌────────────────────────────────────────────────────────────────────┐
│              AWS Pricing Models                                     │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ON-DEMAND                                                         │
│  └── Pay per use, no commitment                                   │
│  └── Highest price, maximum flexibility                           │
│  └── Good for: unpredictable, short-term workloads                │
│                                                                     │
│  RESERVED (1 or 3 years)                                          │
│  └── Up to 72% discount                                           │
│  └── Commit to specific instance type/region                      │
│  └── Payment: All upfront, Partial, No upfront                    │
│  └── Good for: steady-state, predictable workloads                │
│                                                                     │
│  SAVINGS PLANS                                                     │
│  └── Flexible alternative to Reserved                             │
│  └── Commit to $/hour spend, not instance type                    │
│  └── Compute SP: EC2, Fargate, Lambda                             │
│  └── EC2 Instance SP: specific instance family                    │
│                                                                     │
│  SPOT INSTANCES                                                    │
│  └── Up to 90% discount                                           │
│  └── Can be interrupted with 2-min notice                         │
│  └── Good for: batch, CI/CD, fault-tolerant workloads             │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 Сравнение экономии

```python
# Example: m5.large in us-east-1
pricing_comparison = {
    "On-Demand": {"hourly": 0.096, "monthly": 70.08, "savings": "0%"},
    "Reserved 1yr No Upfront": {"hourly": 0.060, "monthly": 43.80, "savings": "37%"},
    "Reserved 3yr All Upfront": {"hourly": 0.040, "monthly": 29.20, "savings": "58%"},
    "Savings Plan 1yr": {"hourly": 0.060, "monthly": 43.80, "savings": "37%"},
    "Spot (avg)": {"hourly": 0.030, "monthly": 21.90, "savings": "69%"}
}

print("m5.large Pricing Comparison:\n")
for plan, details in pricing_comparison.items():
    print(f"{plan}:")
    print(f"  ${details['hourly']}/hour, ${details['monthly']}/month")
    print(f"  Savings: {details['savings']}\n")
```

---

## 2. Cost Optimization Strategies

### 2.1 Right-Sizing

```python
# Identify underutilized resources
right_sizing_targets = {
    "EC2": {
        "metric": "CPU utilization < 10%, Network < 5%",
        "action": "Downsize or terminate",
        "tools": ["AWS Compute Optimizer", "CloudWatch"]
    },
    "RDS": {
        "metric": "CPU < 10%, connections < 10%",
        "action": "Downsize instance class",
        "tools": ["Performance Insights", "CloudWatch"]
    },
    "EBS": {
        "metric": "IOPS usage < 20%",
        "action": "Change to gp3 or reduce IOPS",
        "tools": ["CloudWatch", "Cost Explorer"]
    }
}

# AWS Compute Optimizer recommendations
# Analyzes CloudWatch metrics and recommends:
# - Optimal instance types
# - Estimated savings
# - Performance risk
```

### 2.2 Architecture Optimizations

```
┌────────────────────────────────────────────────────────────────────┐
│              Cost-Efficient Architecture                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  INSTEAD OF                  CONSIDER                              │
│  ──────────                  ────────                              │
│  Always-on EC2              Auto Scaling (scale to 0)             │
│  EC2 for batch jobs         Lambda or Spot instances              │
│  Provisioned throughput     On-Demand capacity (DynamoDB)         │
│  Single AZ                  Multi-AZ only for prod                │
│  gp2 EBS                    gp3 (20% cheaper, better perf)        │
│  NAT Gateway                NAT Instance (for low traffic)        │
│  Multiple Load Balancers    Shared ALB with path routing          │
│  Cross-region data transfer CloudFront for distribution           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 2.3 Spot Instance Strategies

```python
# Spot Instance Best Practices
spot_strategies = {
    "Diversify": "Use multiple instance types and AZs",
    "Spot Fleet": "Request capacity across pools",
    "Interruption handling": "Save state, use checkpoints",
    "Mixed instances": "On-Demand + Spot in Auto Scaling Group"
}

# Auto Scaling Group with Spot
asg_mixed_config = {
    "InstancesDistribution": {
        "OnDemandBaseCapacity": 2,  # Always 2 On-Demand
        "OnDemandPercentageAboveBaseCapacity": 25,  # 25% On-Demand
        "SpotAllocationStrategy": "capacity-optimized",
        "SpotInstancePools": 4  # Diversify across 4 pools
    },
    "Overrides": [
        {"InstanceType": "m5.large"},
        {"InstanceType": "m5a.large"},
        {"InstanceType": "m4.large"},
        {"InstanceType": "m5n.large"}
    ]
}
```

---

## 3. S3 Cost Optimization

### 3.1 Storage Classes

```python
s3_storage_classes = {
    "Standard": {
        "cost": "$0.023/GB",
        "use_case": "Frequently accessed data"
    },
    "Intelligent-Tiering": {
        "cost": "$0.023/GB + monitoring fee",
        "use_case": "Unknown access patterns"
    },
    "Standard-IA": {
        "cost": "$0.0125/GB",
        "use_case": "Infrequent access, quick retrieval"
    },
    "One Zone-IA": {
        "cost": "$0.01/GB",
        "use_case": "Reproducible infrequent data"
    },
    "Glacier Instant": {
        "cost": "$0.004/GB",
        "use_case": "Archive with ms retrieval"
    },
    "Glacier Flexible": {
        "cost": "$0.0036/GB",
        "use_case": "Archive, min-hours retrieval"
    },
    "Glacier Deep Archive": {
        "cost": "$0.00099/GB",
        "use_case": "Long-term archive, 12-48h retrieval"
    }
}

# Lifecycle policy example
lifecycle_policy = {
    "Rules": [{
        "ID": "archive-old-data",
        "Status": "Enabled",
        "Transitions": [
            {"Days": 30, "StorageClass": "STANDARD_IA"},
            {"Days": 90, "StorageClass": "GLACIER"},
            {"Days": 365, "StorageClass": "DEEP_ARCHIVE"}
        ],
        "Expiration": {"Days": 2555}  # Delete after 7 years
    }]
}
```

---

## 4. Monitoring и Alerting

### 4.1 AWS Cost Explorer

```python
# Cost Explorer queries
cost_queries = {
    "By Service": "Which services cost the most?",
    "By Tag": "Cost per team/project/environment",
    "Daily trend": "Is spending increasing?",
    "Forecasting": "Projected end-of-month cost",
    "Reserved utilization": "Are RIs being used?"
}

# Cost anomaly detection
# Automatically detects unusual spending
# Alerts via SNS/email
```

### 4.2 Budgets и Alerts

```bash
# Create budget alert
aws budgets create-budget \
    --account-id 123456789012 \
    --budget '{
        "BudgetName": "MonthlyBudget",
        "BudgetLimit": {"Amount": "1000", "Unit": "USD"},
        "TimeUnit": "MONTHLY",
        "BudgetType": "COST"
    }' \
    --notifications-with-subscribers '[{
        "Notification": {
            "NotificationType": "ACTUAL",
            "ComparisonOperator": "GREATER_THAN",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [{
            "SubscriptionType": "EMAIL",
            "Address": "alerts@example.com"
        }]
    }]'
```

---

## 5. Tagging Strategy

```python
# Required tags for cost allocation
required_tags = {
    "Environment": ["dev", "staging", "prod"],
    "Project": "Project or application name",
    "Team": "Owning team",
    "CostCenter": "Billing cost center",
    "Owner": "Email of responsible person"
}

# Tag policy enforcement
# AWS Organizations - Tag Policies
# AWS Config rule: required-tags

# Example tag policy
tag_policy = {
    "tags": {
        "Environment": {
            "tag_key": {"@@assign": "Environment"},
            "tag_value": {"@@assign": ["dev", "staging", "prod"]},
            "enforced_for": {"@@assign": ["ec2:instance", "rds:db"]}
        }
    }
}
```

---

## 6. FinOps Best Practices

```python
finops_practices = {
    "Visibility": [
        "Enable Cost Explorer",
        "Set up cost allocation tags",
        "Create per-team/project dashboards"
    ],
    "Optimization": [
        "Right-size resources monthly",
        "Use Savings Plans for baseline",
        "Spot for fault-tolerant workloads",
        "Delete unused resources"
    ],
    "Governance": [
        "Set budgets with alerts",
        "Review costs weekly",
        "Implement approval for large resources",
        "Automate cleanup of dev resources"
    ],
    "Culture": [
        "Make costs visible to engineers",
        "Include cost in architecture reviews",
        "Celebrate cost savings"
    ]
}

for pillar, practices in finops_practices.items():
    print(f"\n{pillar}:")
    for practice in practices:
        print(f"  • {practice}")
```

---

## 💡 Key Takeaways

- **Right-sizing** — match resources to actual usage
- **Reserved/Savings Plans** — 30-72% savings for steady workloads
- **Spot** — up to 90% savings for interruptible workloads
- **S3 Lifecycle** — automatically move to cheaper storage classes
- **Tagging** — essential for cost allocation and visibility
- **Budgets** — set alerts before overspending

---

## 📚 Additional Resources

- [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/)
- [Well-Architected Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)

---

## 🚀 Next Steps

**Следующие модули:**
- [24_MultiCloud](../24_MultiCloud/) — Multi-cloud costs
- [25_CaseStudies](../25_CaseStudies/) — Реальные кейсы оптимизации

**Практика:**
1. Настройте AWS Budgets с алертами
2. Проанализируйте Cost Explorer для anomalies
3. Создайте Savings Plan или Reserved Instances план
