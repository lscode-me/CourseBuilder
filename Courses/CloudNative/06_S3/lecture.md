# S3: Simple Storage Service

---

## 📋 Prerequisites

- Понимание облачных сервисов
- Базовые знания IAM
- Знакомство с CLI

**Recommended prior modules:**

- [IAM](../04_IAM/) — для S3 bucket policies

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и управлять S3 buckets
- Выбирать правильный storage class
- Настраивать lifecycle policies
- Обеспечивать безопасность данных
- Использовать версионирование и репликацию

---

## 1. Введение в S3

### 1.1 Что такое S3

**Amazon Simple Storage Service (S3)** — объектное хранилище с практически неограниченной масштабируемостью. Запущен в марте 2006 года — первый публичный сервис AWS.

```python

s3_characteristics = {
    "durability": "99.999999999% (11 nines)",
    "availability": "99.99% (S3 Standard)",
    "max_object_size": "5 TB",
    "max_bucket_objects": "Unlimited",
    "pricing": "Pay for storage, requests, data transfer"
}

print("S3 Key Characteristics:")
for key, value in s3_characteristics.items():
    print(f"  {key}: {value}")

```

**Output:**
```

S3 Key Characteristics:
  durability: 99.999999999% (11 nines)
  availability: 99.99% (S3 Standard)
  max_object_size: 5 TB
  max_bucket_objects: Unlimited
  pricing: Pay for storage, requests, data transfer

```

### 1.2 Ключевые концепции

```

┌───────────────────────────────────────────────────────────────┐
│                    S3 Key Concepts                            │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  BUCKET                                                       │
│  ├── Контейнер для объектов                                   │
│  ├── Глобально уникальное имя                                 │
│  ├── Региональный ресурс                                      │
│  └── Flat structure (нет реальных папок)                      │
│                                                               │
│  OBJECT                                                       │
│  ├── Key: полный путь (folder/subfolder/file.txt)             │
│  ├── Value: данные (до 5 TB)                                  │
│  ├── Metadata: key-value pairs                                │
│  ├── Version ID (если версионирование включено)               │
│  └── Tags: для организации и billing                          │
│                                                               │
│  PREFIX                                                       │
│  └── "folder/" — логическая группировка по prefix             │
│                                                               │
└───────────────────────────────────────────────────────────────┘

```

---

## 2. Storage Classes

### 2.1 Обзор классов хранения

```python

storage_classes = {
    "S3 Standard": {
        "availability": "99.99%",
        "min_storage_duration": "None",
        "retrieval_fee": "None",
        "use_case": "Frequently accessed data",
        "price_gb_month": 0.023
    },
    "S3 Intelligent-Tiering": {
        "availability": "99.9%",
        "min_storage_duration": "None",
        "retrieval_fee": "None",
        "use_case": "Unknown access patterns",
        "price_gb_month": 0.023  # + monitoring fee
    },
    "S3 Standard-IA": {
        "availability": "99.9%",
        "min_storage_duration": "30 days",
        "retrieval_fee": "$0.01/GB",
        "use_case": "Infrequent access, quick retrieval",
        "price_gb_month": 0.0125
    },
    "S3 One Zone-IA": {
        "availability": "99.5%",
        "min_storage_duration": "30 days",
        "retrieval_fee": "$0.01/GB",
        "use_case": "Recreatable data, single AZ",
        "price_gb_month": 0.01
    },
    "S3 Glacier Instant": {
        "availability": "99.9%",
        "min_storage_duration": "90 days",
        "retrieval_fee": "$0.03/GB",
        "use_case": "Archive with instant access",
        "price_gb_month": 0.004
    },
    "S3 Glacier Flexible": {
        "availability": "99.99%",
        "min_storage_duration": "90 days",
        "retrieval_fee": "Varies by speed",
        "use_case": "Archive, 1-12 hour retrieval",
        "price_gb_month": 0.0036
    },
    "S3 Glacier Deep Archive": {
        "availability": "99.99%",
        "min_storage_duration": "180 days",
        "retrieval_fee": "Varies by speed",
        "use_case": "Long-term archive, 12-48 hours",
        "price_gb_month": 0.00099
    }
}

print("S3 Storage Classes (us-east-1 pricing):\n")
print(f"{'Class':<25} {'$/GB/month':<12} {'Use Case'}")
print("-" * 70)
for cls, details in storage_classes.items():
    print(f"{cls:<25} ${details['price_gb_month']:<10} {details['use_case'][:30]}")

```

**Output:**
```

S3 Storage Classes (us-east-1 pricing):

Class                     $/GB/month   Use Case
----------------------------------------------------------------------
S3 Standard               $0.023      Frequently accessed data
S3 Intelligent-Tiering    $0.023      Unknown access patterns
S3 Standard-IA            $0.0125     Infrequent access, quick retrie
S3 One Zone-IA            $0.01       Recreatable data, single AZ
S3 Glacier Instant        $0.004      Archive with instant access
S3 Glacier Flexible       $0.0036     Archive, 1-12 hour retrieval
S3 Glacier Deep Archive   $0.00099    Long-term archive, 12-48 hours

```

---

## 3. Операции с S3

### 3.1 Создание bucket и загрузка

```bash
# Создание bucket
aws s3 mb s3://my-unique-bucket-name-12345

# Загрузка файла
aws s3 cp myfile.txt s3://my-bucket/folder/myfile.txt

# Загрузка директории
aws s3 sync ./local-folder s3://my-bucket/folder/

# Загрузка с указанием storage class
aws s3 cp largefile.zip s3://my-bucket/ --storage-class STANDARD_IA

# Multipart upload (автоматически для больших файлов)
# Рекомендуется для файлов > 100MB
aws s3 cp large-file.tar.gz s3://my-bucket/ \
    --expected-size 5368709120

```

### 3.2 Presigned URLs

```python

import boto3
from botocore.exceptions import ClientError

def generate_presigned_url(bucket: str, key: str, expiration: int = 3600) -> str:
    """
    Генерация presigned URL для временного доступа к объекту
    """
    s3_client = boto3.client('s3')
    
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=expiration  # секунды
        )
        return url
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Пример использования
url = generate_presigned_url('my-bucket', 'reports/report.pdf', 3600)
print(f"Download link (valid 1 hour): {url}")

```

---

## 4. Безопасность S3

### 4.1 Block Public Access

```bash
# Включение Block Public Access на уровне аккаунта (рекомендуется)
aws s3control put-public-access-block \
    --account-id 123456789012 \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# На уровне bucket
aws s3api put-public-access-block \
    --bucket my-bucket \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

```

### 4.2 Bucket Policy

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudFrontAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE"
                }
            }
        },
        {
            "Sid": "DenyInsecureTransport",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}

```

### 4.3 Encryption

```bash
# Server-side encryption (SSE-S3) - по умолчанию с 2023
# Все новые объекты автоматически шифруются

# SSE-KMS для управляемых ключей
aws s3 cp file.txt s3://my-bucket/ \
    --sse aws:kms \
    --sse-kms-key-id alias/my-key

# Bucket default encryption
aws s3api put-bucket-encryption \
    --bucket my-bucket \
    --server-side-encryption-configuration '{
        "Rules": [{
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyID": "alias/my-key"
            },
            "BucketKeyEnabled": true
        }]
    }'

```

---

## 5. Versioning и Lifecycle

### 5.1 Versioning

```bash
# Включение версионирования
aws s3api put-bucket-versioning \
    --bucket my-bucket \
    --versioning-configuration Status=Enabled

# Получение конкретной версии
aws s3api get-object \
    --bucket my-bucket \
    --key myfile.txt \
    --version-id "3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY" \
    output.txt

# Удаление версии (permanent)
aws s3api delete-object \
    --bucket my-bucket \
    --key myfile.txt \
    --version-id "3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY"

```

### 5.2 Lifecycle Policy

```json

{
    "Rules": [
        {
            "ID": "MoveToIAAfter30Days",
            "Status": "Enabled",
            "Filter": {
                "Prefix": "logs/"
            },
            "Transitions": [
                {
                    "Days": 30,
                    "StorageClass": "STANDARD_IA"
                },
                {
                    "Days": 90,
                    "StorageClass": "GLACIER"
                },
                {
                    "Days": 365,
                    "StorageClass": "DEEP_ARCHIVE"
                }
            ],
            "Expiration": {
                "Days": 2555
            },
            "NoncurrentVersionTransitions": [
                {
                    "NoncurrentDays": 30,
                    "StorageClass": "GLACIER"
                }
            ],
            "NoncurrentVersionExpiration": {
                "NoncurrentDays": 90
            }
        }
    ]
}

```

---

## 6. Replication

### 6.1 Cross-Region Replication (CRR)

```json

{
    "Role": "arn:aws:iam::123456789012:role/S3ReplicationRole",
    "Rules": [
        {
            "ID": "ReplicateEverything",
            "Status": "Enabled",
            "Priority": 1,
            "Filter": {},
            "Destination": {
                "Bucket": "arn:aws:s3:::destination-bucket-eu",
                "StorageClass": "STANDARD_IA",
                "ReplicationTime": {
                    "Status": "Enabled",
                    "Time": {
                        "Minutes": 15
                    }
                }
            },
            "DeleteMarkerReplication": {
                "Status": "Enabled"
            }
        }
    ]
}

```

---

## 7. Performance Optimization

### 7.1 Оптимизация производительности

```python

performance_tips = {
    "Use S3 Transfer Acceleration": {
        "when": "Uploads/downloads from distant locations",
        "how": "bucket.s3-accelerate.amazonaws.com"
    },
    "Multipart Upload": {
        "when": "Files > 100MB",
        "how": "aws s3 cp автоматически или SDK"
    },
    "Byte-Range Fetches": {
        "when": "Нужна только часть большого файла",
        "how": "Range header в GET request"
    },
    "Prefix Distribution": {
        "when": "High request rates",
        "how": "Распределите ключи по разным prefixes"
    },
    "S3 Select": {
        "when": "Query data without downloading entire object",
        "how": "SQL queries on CSV, JSON, Parquet"
    }
}

print("S3 Performance Tips:\n")
for tip, details in performance_tips.items():
    print(f"📌 {tip}")
    print(f"   When: {details['when']}")
    print(f"   How: {details['how']}\n")

```

---

## 8. Event Notifications

```python
# S3 Event Notifications - триггеры для Lambda, SQS, SNS, EventBridge

event_types = [
    "s3:ObjectCreated:*",           # Любое создание
    "s3:ObjectCreated:Put",          # PUT
    "s3:ObjectCreated:Post",         # POST
    "s3:ObjectCreated:Copy",         # Copy
    "s3:ObjectRemoved:*",            # Любое удаление
    "s3:ObjectRemoved:Delete",       # Delete
    "s3:ObjectRestore:Completed",    # Glacier restore
    "s3:LifecycleExpiration:*",      # Lifecycle expiration
]

# Пример Lambda trigger для обработки загруженных изображений
lambda_handler_example = '''
def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Process uploaded image
        if key.endswith(('.jpg', '.png')):
            # Resize, generate thumbnails, etc.
            process_image(bucket, key)
'''

```

---

## 9. Common Pitfalls

### 9.1 Pitfall: Публичный bucket

❌ **Проблема:**
```bash
# Случайно сделали bucket публичным
# Утечка данных, compliance нарушения
```

✅ **Решение:**
```bash
# Всегда включайте Block Public Access
# Используйте presigned URLs для временного доступа
# Мониторьте с IAM Access Analyzer
```

### 9.2 Pitfall: Не учитывается стоимость запросов

❌ **Проблема:**
```python
# Много мелких GET/PUT запросов
# GET: $0.0004 per 1,000 requests
# PUT: $0.005 per 1,000 requests

# 100M GET запросов = $40/месяц только за запросы!
```

✅ **Решение:**
```python
# Батчинг операций
# Кэширование (CloudFront)
# S3 Select вместо полного download
```

---

## 💡 Key Takeaways

- **S3** — объектное хранилище с 11 девяток durability

- **Storage Classes** — выбирайте по частоте доступа (Standard → Glacier)

- **Lifecycle Policies** — автоматизируйте перемещение между классами

- **Security** — Block Public Access, encryption, bucket policies

- **Versioning** — для защиты от случайного удаления

- **Presigned URLs** — для временного доступа без credentials

---

## 🚀 Next Steps

- [VPC](../07_VPC/) — сетевая инфраструктура
- [CloudFront](../14_CDN/) — CDN для S3

---

## 📚 Additional Resources

- [S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)
- [S3 Pricing](https://aws.amazon.com/s3/pricing/)

---




