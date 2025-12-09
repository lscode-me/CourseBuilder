# AWS Lambda: Serverless Compute

---

## 📋 Prerequisites

- Понимание модели FaaS
- Базовые знания Python или Node.js
- Знакомство с IAM roles

---

## 🎯 Learning Objectives

- Создавать и деплоить Lambda функции
- Понимать триггеры и интеграции
- Оптимизировать производительность (cold start)
- Использовать Lambda в event-driven архитектурах

---

## 1. Введение в Lambda

### 1.1 Что такое Lambda

**AWS Lambda** — serverless compute сервис, запускающий код в ответ на события. Запущен в 2014 году, стал основой serverless движения.

```python
# Простейшая Lambda функция
def lambda_handler(event, context):
    """
    event: входные данные (JSON)
    context: runtime информация (request_id, timeout, memory)
    """
    name = event.get('name', 'World')
    
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
```

### 1.2 Характеристики

```python
lambda_limits = {
    "memory": "128 MB - 10,240 MB",
    "timeout": "1 second - 15 minutes",
    "deployment_package": "50 MB (zipped), 250 MB (unzipped)",
    "tmp_storage": "/tmp - 512 MB - 10,240 MB",
    "concurrent_executions": "1,000 (soft limit, can increase)",
    "payload_size": "6 MB (sync), 256 KB (async)",
    "env_variables": "4 KB total"
}

print("Lambda Limits:")
for limit, value in lambda_limits.items():
    print(f"  {limit}: {value}")
```

---

## 2. Триггеры Lambda

```
┌────────────────────────────────────────────────────────────────────┐
│                    Lambda Triggers                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SYNCHRONOUS (Request-Response)                                    │
│  ├── API Gateway (HTTP)                                           │
│  ├── Application Load Balancer                                    │
│  ├── CloudFront (Lambda@Edge)                                     │
│  └── Cognito (User Pool triggers)                                 │
│                                                                     │
│  ASYNCHRONOUS (Fire-and-forget)                                   │
│  ├── S3 (object events)                                           │
│  ├── SNS (messages)                                               │
│  ├── EventBridge (events/schedules)                               │
│  ├── SES (email)                                                  │
│  └── CloudFormation (custom resources)                            │
│                                                                     │
│  POLL-BASED (Lambda polls source)                                 │
│  ├── SQS (messages)                                               │
│  ├── DynamoDB Streams                                             │
│  ├── Kinesis Data Streams                                         │
│  └── MSK (Kafka)                                                  │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 2.1 Пример: S3 Trigger

```python
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Обработка загруженного в S3 файла
    """
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
        print(f"Processing: s3://{bucket}/{key}")
        
        # Получаем объект
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        
        # Обрабатываем...
        process_file(content)
    
    return {'statusCode': 200}
```

---

## 3. Cold Start

### 3.1 Что такое Cold Start

```
┌────────────────────────────────────────────────────────────────────┐
│                    Cold Start vs Warm Start                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  COLD START (первый вызов или после idle)                         │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 1. Download code          │ 2. Start runtime │ 3. Init code  │ │
│  │    (from S3)              │    (Python/Node) │    (imports)  │ │
│  │    ~100-500ms             │    ~100-200ms    │    ~100ms+    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│  │                                                               │ │
│  │ 4. Execute handler                                            │ │
│  │    (your code)                                                │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  WARM START (повторный вызов, container reused)                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 4. Execute handler only (~10-100ms)                          │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  Cold start latency: 100ms - 5+ seconds (VPC, Java)               │
│  Warm start latency: 1-100ms                                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Оптимизация Cold Start

```python
# ❌ BAD: Imports внутри handler
def lambda_handler(event, context):
    import boto3  # Импорт при каждом вызове!
    import json
    # ...

# ✅ GOOD: Imports вне handler (один раз при cold start)
import boto3
import json

# Инициализация клиентов вне handler
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

def lambda_handler(event, context):
    # Используем уже инициализированные объекты
    response = table.get_item(Key={'id': event['id']})
    return response['Item']
```

### 3.3 Provisioned Concurrency

```bash
# Для критичных к latency функций
aws lambda put-provisioned-concurrency-config \
    --function-name my-function \
    --qualifier my-alias \
    --provisioned-concurrent-executions 10

# Теперь 10 warm instances всегда готовы
# Цена: ~$0.015/GB-hour + execution cost
```

---

## 4. Lambda Layers

```bash
# Layers — переиспользуемые библиотеки

# Создание layer
mkdir -p python/lib/python3.11/site-packages
pip install requests -t python/lib/python3.11/site-packages/
zip -r layer.zip python

aws lambda publish-layer-version \
    --layer-name my-dependencies \
    --zip-file fileb://layer.zip \
    --compatible-runtimes python3.11

# Использование layer
aws lambda update-function-configuration \
    --function-name my-function \
    --layers arn:aws:lambda:us-east-1:123456789012:layer:my-dependencies:1
```

---

## 5. Lambda + API Gateway

```python
# Lambda для REST API
import json

def lambda_handler(event, context):
    """
    API Gateway integration (REST API)
    """
    http_method = event['httpMethod']
    path = event['path']
    body = json.loads(event.get('body') or '{}')
    
    if http_method == 'GET' and path == '/users':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'users': []})
        }
    
    if http_method == 'POST' and path == '/users':
        # Create user
        return {
            'statusCode': 201,
            'body': json.dumps({'id': 'new-user-id'})
        }
    
    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Not found'})
    }
```

---

## 6. Pricing

```python
# Lambda pricing (us-east-1)
def calculate_lambda_cost(
    invocations_per_month: int,
    avg_duration_ms: int,
    memory_mb: int = 128
) -> float:
    """
    Расчёт месячной стоимости Lambda
    """
    # Free tier: 1M requests, 400,000 GB-seconds
    FREE_REQUESTS = 1_000_000
    FREE_GB_SECONDS = 400_000
    
    PRICE_PER_REQUEST = 0.0000002  # $0.20 per 1M
    PRICE_PER_GB_SECOND = 0.0000166667
    
    # Расчёт
    billable_requests = max(0, invocations_per_month - FREE_REQUESTS)
    
    gb_seconds = (invocations_per_month * (avg_duration_ms / 1000) * 
                  (memory_mb / 1024))
    billable_gb_seconds = max(0, gb_seconds - FREE_GB_SECONDS)
    
    cost = (billable_requests * PRICE_PER_REQUEST + 
            billable_gb_seconds * PRICE_PER_GB_SECOND)
    
    return round(cost, 2)

# Примеры
print("Lambda Monthly Cost Examples:")
print(f"  100K invocations, 100ms, 128MB: ${calculate_lambda_cost(100_000, 100, 128)}")
print(f"  1M invocations, 200ms, 256MB: ${calculate_lambda_cost(1_000_000, 200, 256)}")
print(f"  10M invocations, 500ms, 512MB: ${calculate_lambda_cost(10_000_000, 500, 512)}")
```

**Output:**
```
Lambda Monthly Cost Examples:
  100K invocations, 100ms, 128MB: $0.0
  1M invocations, 200ms, 256MB: $0.83
  10M invocations, 500ms, 512MB: $43.33
```

---

## 7. Best Practices

```python
best_practices = [
    "Минимизируйте deployment package size",
    "Инициализируйте SDK clients вне handler",
    "Используйте environment variables для config",
    "Настройте appropriate timeout и memory",
    "Используйте Layers для общих зависимостей",
    "Избегайте VPC если не нужно (cold start +)",
    "Используйте Provisioned Concurrency для низкой latency",
    "Мониторинг через CloudWatch Logs/X-Ray",
    "Dead Letter Queue для failed async invocations"
]
```

---

## 💡 Key Takeaways

- **Lambda** — serverless compute, pay per execution
- **Триггеры**: API Gateway, S3, SQS, EventBridge, etc.
- **Cold Start** — инициализация при первом вызове (оптимизируйте!)
- **Layers** — переиспользование библиотек между функциями
- **Limits**: 15 min timeout, 10 GB memory, 10 GB /tmp

---

## 📚 Additional Resources

- [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)
- [Lambda Power Tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning)

---

## 🚀 Next Steps

**Следующие модули:**
- [11_Containers](../11_Containers/) — ECS и EKS контейнеры
- [13_APIGateway](../13_APIGateway/) — API Gateway для Lambda

**Практика:**
1. Создайте Lambda функцию на Python/Node.js
2. Настройте триггер от S3 или API Gateway
3. Оптимизируйте cold start время
