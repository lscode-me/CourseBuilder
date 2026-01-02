# Data Services: Analytics и Streaming

---

## 📋 Prerequisites

- Понимание SQL
- Базовые знания data warehousing
- Знакомство с S3

---

## 🎯 Learning Objectives

- Различать OLTP и OLAP workloads
- Использовать Redshift для data warehousing
- Анализировать данные в S3 с Athena
- Обрабатывать streaming данные с Kinesis

---

## 1. OLTP vs OLAP

```
┌────────────────────────────────────────────────────────────────────┐
│              OLTP vs OLAP                                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  OLTP (Online Transaction Processing)                              │
│  ───────────────────────────────────                               │
│  • Short, simple queries                                           │
│  • High volume of transactions                                     │
│  • Row-based storage                                               │
│  • Examples: RDS, DynamoDB, Aurora                                 │
│  • Use case: E-commerce orders, banking                            │
│                                                                    │
│  OLAP (Online Analytical Processing)                               │
│  ─────────────────────────────────                                 │
│  • Complex queries, aggregations                                   │
│  • Large data scans                                                │
│  • Columnar storage                                                │
│  • Examples: Redshift, Athena, BigQuery                            │
│  • Use case: Business intelligence, reporting                      │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 2. Amazon Redshift

### 2.1 Архитектура

```
┌────────────────────────────────────────────────────────────────────┐
│              Redshift Architecture                                 │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Leader Node                                 ││
│  │  • Query planning & optimization                               ││
│  │  • Result aggregation                                          ││
│  │  • Client connections                                          ││
│  └───────────────────────────────────────────────────────────────┘ │
│                            │                                       │
│          ┌─────────────────┼─────────────────┐                     │
│          ▼                 ▼                 ▼                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ Compute Node │  │ Compute Node │  │ Compute Node │              │
│  │              │  │              │  │              │              │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │              │
│  │  │ Slice  │  │  │  │ Slice  │  │  │  │ Slice  │  │              │
│  │  │ Slice  │  │  │  │ Slice  │  │  │  │ Slice  │  │              │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                    │
│  • Columnar storage (compressed)                                   │
│  • Massively Parallel Processing (MPP)                             │
│  • Data distributed across slices                                  │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 2.2 Создание Cluster

```bash
aws redshift create-cluster \
    --cluster-identifier my-cluster \
    --node-type dc2.large \
    --number-of-nodes 2 \
    --master-username admin \
    --master-user-password 'SecurePass123!' \
    --db-name mydb \
    --vpc-security-group-ids sg-123 \
    --cluster-subnet-group-name my-subnet-group \
    --encrypted
```

### 2.3 Redshift Serverless

```python
# Redshift Serverless - автоматическое масштабирование

redshift_serverless_config = {
    "Workgroup": "my-workgroup",
    "Namespace": "my-namespace",
    "Base capacity": "32 RPU",  # Redshift Processing Units
    "Max capacity": "512 RPU",
    "Pricing": "Per-second billing based on compute used"
}

# Идеально для:
# - Variable workloads
# - Ad-hoc queries
# - Dev/test environments
```

### 2.4 Data Loading

```sql
-- COPY command - fastest way to load data
COPY orders
FROM 's3://my-bucket/orders/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
FORMAT AS PARQUET;

-- Manifest file for specific files
COPY orders
FROM 's3://my-bucket/manifest.json'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
MANIFEST;

-- Best practices:
-- • Use columnar formats (Parquet, ORC)
-- • Split large files into multiple smaller files
-- • Use compression (gzip, lzo)
-- • Match number of files to number of slices
```

---

## 3. Amazon Athena

### 3.1 Serverless SQL for S3

```
┌────────────────────────────────────────────────────────────────────┐
│              Athena Architecture                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  User                                                              │
│    │                                                               │
│    │ SQL Query                                                     │
│    ▼                                                               │
│  ┌──────────────┐                                                  │
│  │   Athena     │ ◄─── AWS Glue Data Catalog (schema)              │
│  │              │                                                  │
│  └──────┬───────┘                                                  │
│         │                                                          │
│         │ Scan data                                                │
│         ▼                                                          │
│  ┌──────────────┐                                                  │
│  │     S3       │                                                  │
│  │  (data lake) │                                                  │
│  │              │                                                  │
│  │ ├── logs/    │                                                  │
│  │ ├── events/  │                                                  │
│  │ └── sales/   │                                                  │
│  └──────────────┘                                                  │
│                                                                    │
│  • No infrastructure to manage                                     │
│  • Pay per query ($5 per TB scanned)                               │
│  • Standard SQL (Presto/Trino)                                     │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Создание таблицы

```sql
-- Create external table in Athena
CREATE EXTERNAL TABLE logs (
    timestamp string,
    request_id string,
    user_id string,
    action string,
    latency_ms int
)
PARTITIONED BY (year string, month string, day string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS PARQUET
LOCATION 's3://my-bucket/logs/'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

-- Add partitions
MSCK REPAIR TABLE logs;  -- Auto-discover partitions

-- Or manually
ALTER TABLE logs ADD PARTITION (year='2024', month='01', day='15')
LOCATION 's3://my-bucket/logs/year=2024/month=01/day=15/';
```

### 3.3 Query Optimization

```python
athena_optimization = {
    "Use columnar formats": "Parquet, ORC - read only needed columns",
    "Partition data": "By date, region - scan only relevant partitions",
    "Compress data": "Reduce data scanned, lower cost",
    "Use LIMIT": "For exploration, add LIMIT clause",
    "Select specific columns": "Avoid SELECT *, list columns explicitly"
}

# Cost comparison:
# CSV 1TB → $5 (full scan)
# Parquet 1TB → ~$0.50 (columnar + compression)
# Parquet with partitions → ~$0.05 (scan only needed partitions)
```

---

## 4. Amazon Kinesis

### 4.1 Kinesis Services

```
┌───────────────────────────────────────────────────────────────────┐
│              Kinesis Family                                       │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Kinesis Data Streams                                             │
│  └── Real-time streaming data ingestion                           │
│  └── Custom consumers (Lambda, EC2, etc.)                         │
│  └── Retention: 24 hours - 365 days                               │
│                                                                   │
│  Kinesis Data Firehose                                            │
│  └── Load streaming data to destinations                          │
│  └── S3, Redshift, OpenSearch, HTTP                               │
│  └── Near real-time (60 seconds buffer)                           │
│  └── Automatic scaling, no management                             │
│                                                                   │
│  Kinesis Data Analytics                                           │
│  └── SQL or Apache Flink on streaming data                        │
│  └── Real-time analytics, aggregations                            │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 4.2 Kinesis Data Streams

```python
import boto3

kinesis = boto3.client('kinesis')

# Producer - send data

kinesis.put_record(
    StreamName='my-stream',
    Data=json.dumps({
        'event_type': 'page_view',
        'user_id': 'user123',
        'page': '/products/456',
        'timestamp': '2024-01-15T10:30:00Z'
    }),
    PartitionKey='user123'  # Determines shard
)

# Consumer - read data

response = kinesis.get_shard_iterator(
    StreamName='my-stream',
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST'
)
shard_iterator = response['ShardIterator']

records = kinesis.get_records(ShardIterator=shard_iterator, Limit=100)
for record in records['Records']:
    data = json.loads(record['Data'])
    print(f"Event: {data['event_type']}")
```

### 4.3 Kinesis Firehose

```python
# Firehose - easiest way to load streaming data to S3

firehose = boto3.client('firehose')

firehose.put_record(
    DeliveryStreamName='my-firehose',
    Record={
        'Data': json.dumps({
            'event': 'click',
            'user_id': 'user123'
        }) + '\n'  # Newline delimiter for JSON
    }
)

# Firehose automatically:
# • Buffers data (size or time based)
# • Converts format (JSON → Parquet)
# • Compresses data
# • Delivers to S3/Redshift/etc.
```

---

## 5. Сравнение

```python
comparison = {
    "Redshift": {
        "type": "Data Warehouse",
        "data_source": "Loaded into Redshift",
        "performance": "Sub-second for complex queries",
        "cost": "Per-hour (cluster) or per-compute (Serverless)",
        "best_for": "Regular BI, dashboards"
    },
    "Athena": {
        "type": "Query Service",
        "data_source": "S3 (in place)",
        "performance": "Seconds to minutes",
        "cost": "$5/TB scanned",
        "best_for": "Ad-hoc queries, data lake"
    },
    "Kinesis": {
        "type": "Streaming",
        "data_source": "Real-time events",
        "performance": "Sub-second latency",
        "cost": "Per shard hour + data",
        "best_for": "Real-time analytics, IoT"
    }
}

for service, details in comparison.items():
    print(f"\n{service}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
```

---

## 💡 Key Takeaways

- **Redshift** — data warehouse, complex analytics, sub-second

- **Athena** — serverless SQL on S3, pay per query

- **Kinesis Streams** — real-time ingestion, custom processing

- **Kinesis Firehose** — managed loading to destinations

- **Columnar formats** — critical for OLAP performance

- **Partitioning** — reduces data scanned and cost

---

## 📚 Additional Resources

- [Redshift Documentation](https://docs.aws.amazon.com/redshift/)
- [Athena User Guide](https://docs.aws.amazon.com/athena/)
- [Kinesis Developer Guide](https://docs.aws.amazon.com/kinesis/)

---

## 🚀 Next Steps

**Следующие модули:**

- [16_IaC](../16_IaC/) — Infrastructure as Code
- [21_Observability](../21_Observability/) — Мониторинг и логирование

**Практика:**

1. Выполните SQL запросы к S3 данным через Athena
2. Настройте Kinesis Data Stream для real-time данных
3. Создайте простой ETL pipeline с Glue




