# Cloud Native Development
## DynamoDB: NoSQL Database

---

## 📋 Prerequisites

- Понимание NoSQL концепций
- Базовые знания JSON
- Знакомство с IAM

---

## 🎯 Learning Objectives

- Проектировать DynamoDB таблицы и индексы
- Понимать partition key и sort key
- Использовать GSI и LSI
- Оптимизировать производительность и стоимость

---

## 1. Введение в DynamoDB

### 1.1 Что такое DynamoDB

**Amazon DynamoDB** — полностью управляемая NoSQL база данных с миллисекундной latency при любом масштабе. Запущена в 2012 году на основе опыта Amazon с Dynamo (внутренний сервис).

```python
dynamodb_features = {
    "Performance": "Single-digit millisecond latency",
    "Scalability": "Virtually unlimited throughput",
    "Availability": "99.999% SLA (Global Tables)",
    "Managed": "No servers to manage",
    "Serverless": "On-demand capacity mode",
    "Global": "Multi-region replication",
    "Security": "Encryption, IAM, VPC endpoints"
}

print("DynamoDB Key Features:")
for feature, description in dynamodb_features.items():
    print(f"  • {feature}: {description}")
```

### 1.2 When to Use DynamoDB

```python
good_fit = [
    "Key-value or document data",
    "High traffic with predictable patterns",
    "Session storage, user profiles",
    "Gaming leaderboards",
    "IoT data ingestion",
    "Shopping carts",
    "Real-time bidding",
    "Serverless applications"
]

not_a_fit = [
    "Complex joins and transactions across tables",
    "Ad-hoc SQL queries",
    "Small datasets where RDS is simpler",
    "OLAP/analytics workloads",
    "Blob storage (use S3)"
]

print("✅ Good fit for DynamoDB:")
for case in good_fit[:5]:
    print(f"  • {case}")

print("\n❌ Not ideal for:")
for case in not_a_fit[:3]:
    print(f"  • {case}")
```

---

## 2. Data Model

### 2.1 Core Concepts

```
┌────────────────────────────────────────────────────────────────────┐
│                    DynamoDB Data Model                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  TABLE                                                             │
│  └── Collection of Items (like rows)                               │
│                                                                     │
│  ITEM                                                              │
│  └── Collection of Attributes (like columns)                       │
│  └── Max size: 400 KB                                             │
│                                                                     │
│  PRIMARY KEY (required)                                            │
│  ├── Partition Key (PK) only                                      │
│  │   └── Single attribute                                         │
│  │   └── Hash-based distribution                                  │
│  │                                                                 │
│  └── Partition Key + Sort Key (PK + SK)                           │
│      └── Composite primary key                                     │
│      └── Items with same PK stored together, sorted by SK         │
│                                                                     │
│  EXAMPLE:                                                          │
│  ┌────────────┬────────────┬──────────┬──────────────┐            │
│  │ PK (user)  │ SK (order) │ product  │ amount       │            │
│  ├────────────┼────────────┼──────────┼──────────────┤            │
│  │ user123    │ order#001  │ widget   │ 29.99        │            │
│  │ user123    │ order#002  │ gadget   │ 49.99        │            │
│  │ user456    │ order#001  │ thing    │ 19.99        │            │
│  └────────────┴────────────┴──────────┴──────────────┘            │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 2.2 Partition Key Design

```python
# Partition Key определяет в какой partition попадёт item
# ВАЖНО: равномерное распределение!

# ❌ BAD: Hot partition
# PK = "status" (values: "active", "inactive")
# Результат: 2 partition для миллионов items

# ✅ GOOD: Equal distribution
# PK = "user_id" (unique per user)
# Результат: много partitions, равномерно

# ✅✅ BETTER: High cardinality with prefix
# PK = f"{tenant_id}#{user_id}"
```

---

## 3. Secondary Indexes

### 3.1 Global Secondary Index (GSI)

```
┌────────────────────────────────────────────────────────────────────┐
│                    Global Secondary Index                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  BASE TABLE                    GSI                                 │
│  PK: user_id                   PK: email                          │
│  SK: order_id                  SK: created_at                     │
│                                                                     │
│  ┌─────────┬─────────┐        ┌─────────────┬────────────┐        │
│  │ user_id │order_id │        │ email       │ created_at │        │
│  ├─────────┼─────────┤   ──►  ├─────────────┼────────────┤        │
│  │ u1      │ o1      │        │ a@test.com  │ 2024-01-01 │        │
│  │ u1      │ o2      │        │ a@test.com  │ 2024-01-02 │        │
│  │ u2      │ o1      │        │ b@test.com  │ 2024-01-01 │        │
│  └─────────┴─────────┘        └─────────────┴────────────┘        │
│                                                                     │
│  GSI Характеристики:                                              │
│  • Можно создать до 20 GSI на таблицу                            │
│  • Другой PK и/или SK                                             │
│  • Eventually consistent reads only                                │
│  • Отдельная capacity (своя RCU/WCU)                              │
│  • Можно создать после таблицы                                    │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Local Secondary Index (LSI)

```python
# LSI: тот же Partition Key, другой Sort Key

lsi_characteristics = {
    "Same PK": "Partition Key должен совпадать с таблицей",
    "Different SK": "Sort Key может быть другим атрибутом",
    "Limit": "До 5 LSI на таблицу",
    "Creation": "Только при создании таблицы",
    "Consistency": "Supports strongly consistent reads",
    "Storage": "Shares partition with base table (10GB limit)"
}

# Пример: Orders table
# PK = customer_id
# SK = order_id (base table)
# LSI: SK = order_date (для query по дате)
```

---

## 4. Operations

### 4.1 Создание таблицы

```bash
aws dynamodb create-table \
    --table-name Orders \
    --attribute-definitions \
        AttributeName=customer_id,AttributeType=S \
        AttributeName=order_id,AttributeType=S \
        AttributeName=created_at,AttributeType=S \
    --key-schema \
        AttributeName=customer_id,KeyType=HASH \
        AttributeName=order_id,KeyType=RANGE \
    --global-secondary-indexes \
        "IndexName=created_at-index,KeySchema=[{AttributeName=customer_id,KeyType=HASH},{AttributeName=created_at,KeyType=RANGE}],Projection={ProjectionType=ALL}" \
    --billing-mode PAY_PER_REQUEST
```

### 4.2 CRUD Operations

```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

# CREATE
table.put_item(Item={
    'customer_id': 'cust123',
    'order_id': 'order456',
    'product': 'Widget',
    'amount': 29.99,
    'created_at': '2024-01-15T10:30:00Z'
})

# READ - GetItem (by primary key)
response = table.get_item(Key={
    'customer_id': 'cust123',
    'order_id': 'order456'
})
item = response.get('Item')

# READ - Query (by PK, optional SK condition)
response = table.query(
    KeyConditionExpression=Key('customer_id').eq('cust123') & Key('order_id').begins_with('order')
)
items = response['Items']

# UPDATE
table.update_item(
    Key={'customer_id': 'cust123', 'order_id': 'order456'},
    UpdateExpression='SET #s = :status',
    ExpressionAttributeNames={'#s': 'status'},
    ExpressionAttributeValues={':status': 'shipped'}
)

# DELETE
table.delete_item(Key={
    'customer_id': 'cust123',
    'order_id': 'order456'
})
```

### 4.3 Query vs Scan

```python
# Query: эффективный, использует индексы
# Requires: Partition Key + optional Sort Key condition

response = table.query(
    KeyConditionExpression=Key('customer_id').eq('cust123')
)
# O(items matching condition)

# Scan: читает ВСЮ таблицу, очень дорого!
# Avoid in production

response = table.scan(
    FilterExpression=Attr('status').eq('pending')
)
# O(all items in table) - плохо!

# ✅ Если нужен Scan-like запрос, создайте GSI
```

---

## 5. Capacity Modes

### 5.1 On-Demand vs Provisioned

```
┌────────────────────────────────────────────────────────────────────┐
│                    Capacity Modes                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ON-DEMAND                       PROVISIONED                       │
│  ─────────                       ───────────                       │
│  • Pay per request               • Pay for RCU/WCU per hour        │
│  • Auto scales instantly         • Manual or auto-scaling          │
│  • No capacity planning          • Capacity planning required      │
│  • Good for unpredictable        • Good for predictable workloads  │
│  • Higher per-request cost       • Lower cost at steady traffic    │
│                                                                     │
│  Pricing (us-east-1):                                              │
│  On-Demand:                                                        │
│    Write: $1.25 per million WRU                                    │
│    Read:  $0.25 per million RRU                                    │
│                                                                     │
│  Provisioned:                                                      │
│    WCU: $0.00065 per hour                                         │
│    RCU: $0.00013 per hour                                         │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 5.2 RCU/WCU Calculation

```python
def calculate_rcu(item_size_kb: float, reads_per_sec: int, 
                   strongly_consistent: bool = False) -> int:
    """Calculate required Read Capacity Units"""
    # 1 RCU = 1 strongly consistent read of 4KB/sec
    # 1 RCU = 2 eventually consistent reads of 4KB/sec
    
    read_units_per_item = max(1, int(item_size_kb / 4) + (1 if item_size_kb % 4 else 0))
    
    if strongly_consistent:
        return read_units_per_item * reads_per_sec
    else:
        return int(read_units_per_item * reads_per_sec / 2)

def calculate_wcu(item_size_kb: float, writes_per_sec: int) -> int:
    """Calculate required Write Capacity Units"""
    # 1 WCU = 1 write of 1KB/sec
    write_units_per_item = max(1, int(item_size_kb))
    return write_units_per_item * writes_per_sec

# Example
print(f"Reading 100 items/sec (2KB each, eventually consistent): {calculate_rcu(2, 100)} RCU")
print(f"Writing 50 items/sec (3KB each): {calculate_wcu(3, 50)} WCU")
```

---

## 6. DynamoDB Streams

```
┌────────────────────────────────────────────────────────────────────┐
│                    DynamoDB Streams                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Application ──► DynamoDB Table ──► Stream ──► Lambda              │
│                       │                           │                │
│                       │                           ▼                │
│                       │                      Process changes       │
│                       │                      - Send notifications  │
│                       │                      - Update search index │
│                       │                      - Replicate to other DB│
│                       │                      - Analytics           │
│                       │                                            │
│  Stream Record Types:                                              │
│  • KEYS_ONLY: only the key attributes                             │
│  • NEW_IMAGE: entire item after modification                       │
│  • OLD_IMAGE: entire item before modification                      │
│  • NEW_AND_OLD_IMAGES: both before and after                      │
│                                                                     │
│  Retention: 24 hours                                               │
│  Ordering: per-partition key ordered                               │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 7. DAX (DynamoDB Accelerator)

```python
# DAX = in-memory cache for DynamoDB
# Reduces latency from milliseconds to microseconds

dax_features = {
    "Latency": "Microseconds (vs milliseconds)",
    "Compatibility": "API compatible with DynamoDB",
    "Caching": "Item cache + query cache",
    "Write-through": "Writes go to DAX → DynamoDB",
    "Scaling": "Up to 11 nodes in cluster",
    "Pricing": "Per node-hour"
}

# Когда использовать DAX:
# ✅ Read-heavy workloads
# ✅ Latency-sensitive applications
# ✅ Same items read repeatedly

# Когда НЕ использовать:
# ❌ Write-heavy workloads
# ❌ Strong consistency required
# ❌ Infrequent reads
```

---

## 8. Global Tables

```
┌────────────────────────────────────────────────────────────────────┐
│                    Global Tables                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│         us-east-1                        eu-west-1                 │
│    ┌─────────────────┐              ┌─────────────────┐           │
│    │   DynamoDB      │◄────────────►│   DynamoDB      │           │
│    │   Table         │  Multi-master│   Table         │           │
│    │   (replica)     │  Replication │   (replica)     │           │
│    └─────────────────┘              └─────────────────┘           │
│            ▲                                ▲                      │
│            │                                │                      │
│    US Users write/read              EU Users write/read           │
│                                                                     │
│  Характеристики:                                                   │
│  • Multi-master (read/write to any region)                        │
│  • Async replication (< 1 second typically)                       │
│  • Conflict resolution: last writer wins                          │
│  • 99.999% availability SLA                                       │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 9. Best Practices

```python
dynamodb_best_practices = [
    "Design for access patterns first, not data model",
    "Use composite keys (PK + SK) for flexibility",
    "Avoid hot partitions - distribute evenly",
    "Use sparse indexes (GSI on optional attributes)",
    "Prefer Query over Scan",
    "Use projections to minimize data transfer",
    "Enable TTL for auto-expiring data",
    "Use On-Demand for unpredictable, Provisioned for steady",
    "Consider DAX for read-heavy, low-latency needs",
    "Use DynamoDB Streams for event-driven patterns"
]
```

---

## 💡 Key Takeaways

- **DynamoDB** — managed NoSQL, single-digit ms latency
- **Partition Key** — determines data distribution (design carefully!)
- **GSI/LSI** — enable additional access patterns
- **Query > Scan** — always prefer Query for efficiency
- **On-Demand vs Provisioned** — choose based on traffic predictability
- **DAX** — microsecond latency cache
- **Global Tables** — multi-region, multi-master

---

## 📚 Additional Resources

- [DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/)
- [DynamoDB Design Patterns](https://www.youtube.com/watch?v=HaEPXoXVf2k) (AWS re:Invent)

---
