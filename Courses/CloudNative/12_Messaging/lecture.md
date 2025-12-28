# Messaging: SQS, SNS, EventBridge

---

## 📋 Prerequisites

- Понимание distributed systems
- Базовые знания асинхронной обработки
- Знакомство с IAM

---

## 🎯 Learning Objectives

- Различать SQS, SNS и EventBridge
- Выбирать правильный сервис для use case
- Проектировать event-driven архитектуры
- Понимать паттерны интеграции

---

## 1. Обзор Messaging Services

### 1.1 Три основных сервиса

```

┌────────────────────────────────────────────────────────────────────┐
│              AWS Messaging Services                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  SQS (Simple Queue Service)                                        │
│  └── Message queues                                                │
│  └── Point-to-point                                                │
│  └── Decoupling, buffering                                         │
│                                                                    │
│  SNS (Simple Notification Service)                                 │
│  └── Pub/Sub messaging                                             │
│  └── Fan-out to multiple subscribers                               │
│  └── Push notifications                                            │
│                                                                    │
│  EventBridge                                                       │
│  └── Serverless event bus                                          │
│  └── Event routing with rules                                      │
│  └── Schema registry                                               │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 2. Amazon SQS

### 2.1 Queue Types

```python

sqs_queue_types = {
    "Standard Queue": {
        "throughput": "Nearly unlimited",
        "ordering": "Best-effort (may be out of order)",
        "delivery": "At-least-once (may be duplicated)",
        "use_case": "High throughput, order doesn't matter"
    },
    "FIFO Queue": {
        "throughput": "300 TPS (3000 with batching)",
        "ordering": "Guaranteed FIFO",
        "delivery": "Exactly-once processing",
        "use_case": "Order matters, no duplicates"
    }
}

for queue_type, details in sqs_queue_types.items():
    print(f"\n{queue_type}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

```

### 2.2 SQS Operations

```python

import boto3
import json

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/my-queue'

# Send message
sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps({'order_id': '12345', 'action': 'process'}),
    MessageAttributes={
        'Type': {'DataType': 'String', 'StringValue': 'Order'}
    }
)

# Receive messages (long polling)
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20,  # Long polling
    VisibilityTimeout=30
)

for message in response.get('Messages', []):
    # Process message
    body = json.loads(message['Body'])
    print(f"Processing: {body}")
    
    # Delete after successful processing
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )

```

### 2.3 Key Concepts

```

┌───────────────────────────────────────────────────────────────────┐
│                    SQS Key Concepts                               │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  VISIBILITY TIMEOUT                                               │
│  └── Message invisible to other consumers while being processed   │
│  └── Default: 30 seconds, Max: 12 hours                           │
│  └── If not deleted, message becomes visible again                │
│                                                                   │
│  LONG POLLING                                                     │
│  └── Wait for messages (reduces empty responses and cost)         │
│  └── WaitTimeSeconds: 1-20 seconds                                │
│                                                                   │
│  DEAD LETTER QUEUE (DLQ)                                          │
│  └── Messages that fail processing multiple times                 │
│  └── For debugging and manual intervention                        │
│                                                                   │
│  MESSAGE RETENTION                                                │
│  └── Default: 4 days, Max: 14 days                                │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

---

## 3. Amazon SNS

### 3.1 Pub/Sub Pattern

```

┌────────────────────────────────────────────────────────────────────┐
│                    SNS Pub/Sub                                     │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Publisher                                                         │
│      │                                                             │
│      ▼                                                             │
│  ┌─────────────────┐                                               │
│  │   SNS Topic     │                                               │
│  │  (order-events) │                                               │
│  └────────┬────────┘                                               │
│           │                                                        │
│     ┌─────┼─────┬─────────┬─────────┐                              │
│     ▼     ▼     ▼         ▼         ▼                              │
│  ┌─────┐┌─────┐┌─────┐ ┌─────┐ ┌─────────┐                         │
│  │ SQS ││ SQS ││Lambda│ │Email│ │HTTP/S   │                        │
│  │Queue││Queue││      │ │     │ │Endpoint │                        │
│  └─────┘└─────┘└─────┘ └─────┘ └─────────┘                         │
│                                                                    │
│  Supported Protocols:                                              │
│  • SQS, Lambda, HTTP/S, Email, SMS, Mobile Push, Firehose          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

### 3.2 SNS + SQS Fan-out

```python
# Fan-out pattern: один event → множество обработчиков

import boto3

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:123456789012:order-events'

# Publish to topic
response = sns.publish(
    TopicArn=topic_arn,
    Message=json.dumps({
        'order_id': '12345',
        'status': 'confirmed',
        'amount': 99.99
    }),
    MessageAttributes={
        'event_type': {'DataType': 'String', 'StringValue': 'OrderConfirmed'}
    }
)

# Message доставляется ВСЕМ подписчикам:
# • SQS queue для inventory service
# • SQS queue для shipping service
# • Lambda для analytics
# • Email notification
```

### 3.3 Message Filtering

```json

{
    "event_type": ["OrderConfirmed", "OrderShipped"],
    "amount": [{"numeric": [">=", 100]}],
    "customer_type": ["premium"]
}

```

---

## 4. Amazon EventBridge

### 4.1 Event Bus

```

┌───────────────────────────────────────────────────────────────────┐
│                    EventBridge                                    │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Event Sources                    Event Bus                       │
│  ┌──────────────┐               ┌─────────────────┐               │
│  │ AWS Services │──────────────►│                 │               │
│  │(EC2,S3,etc.) │               │   default or    │               │
│  └──────────────┘               │   custom bus    │               │
│  ┌──────────────┐               │                 │               │
│  │ Custom Apps  │──────────────►│    Rules:       │               │
│  │ (PutEvents)  │               │    ┌─────────┐  │               │
│  └──────────────┘               │    │ Rule 1  │──┼──► Lambda     │
│  ┌──────────────┐               │    │ Rule 2  │──┼──► SQS        │
│  │   SaaS       │──────────────►│    │ Rule 3  │──┼──► Step Func  │
│  │(Zendesk,etc.)│               │    └─────────┘  │               │
│  └──────────────┘               └─────────────────┘               │
│                                                                   │
│  Targets: Lambda, SQS, SNS, Step Functions, ECS, API Gateway,     │
│           Kinesis, CodePipeline, EventBridge (cross-account)      │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘

```

### 4.2 Event Pattern Rules

```python

import boto3

events = boto3.client('events')

# Создание rule
events.put_rule(
    Name='order-confirmed-rule',
    EventPattern=json.dumps({
        "source": ["com.myapp.orders"],
        "detail-type": ["OrderConfirmed"],
        "detail": {
            "amount": [{"numeric": [">=", 100]}]
        }
    }),
    State='ENABLED'
)

# Добавление target
events.put_targets(
    Rule='order-confirmed-rule',
    Targets=[
        {
            'Id': 'process-high-value-orders',
            'Arn': 'arn:aws:lambda:us-east-1:123456789012:function:processOrder'
        }
    ]
)

# Отправка события
events.put_events(
    Entries=[
        {
            'Source': 'com.myapp.orders',
            'DetailType': 'OrderConfirmed',
            'Detail': json.dumps({
                'order_id': '12345',
                'amount': 150.00,
                'customer_id': 'cust789'
            })
        }
    ]
)

```

### 4.3 Scheduler

```python
# EventBridge Scheduler для cron-подобных задач

scheduler = boto3.client('scheduler')

scheduler.create_schedule(
    Name='daily-report',
    ScheduleExpression='cron(0 9 * * ? *)',  # 9 AM UTC daily
    Target={
        'Arn': 'arn:aws:lambda:us-east-1:123456789012:function:generateReport',
        'RoleArn': 'arn:aws:iam::123456789012:role/scheduler-role'
    },
    FlexibleTimeWindow={'Mode': 'OFF'}
)

```

---

## 5. Выбор сервиса

```python

decision_guide = {
    "SQS": [
        "Decoupling between services",
        "Work queue for async processing",
        "Buffering requests",
        "Exactly-once processing (FIFO)"
    ],
    "SNS": [
        "Fan-out to multiple consumers",
        "Push notifications (email, SMS)",
        "Alert/notification system",
        "Combined with SQS for reliability"
    ],
    "EventBridge": [
        "Event-driven architecture",
        "Routing based on event content",
        "Integration with SaaS apps",
        "Schema registry needed",
        "Scheduled tasks (cron)"
    ]
}

print("When to use which service:\n")
for service, use_cases in decision_guide.items():
    print(f"{service}:")
    for case in use_cases:
        print(f"  • {case}")
    print()

```

---

## 6. Common Patterns

### 6.1 SNS + SQS для надёжности

```

┌────────────────────────────────────────────────────────────────────┐
│              SNS + SQS Pattern                                     │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Publisher                                                         │
│      │                                                             │
│      ▼                                                             │
│  ┌─────────┐                                                       │
│  │   SNS   │                                                       │
│  │  Topic  │                                                       │
│  └────┬────┘                                                       │
│       │                                                            │
│  ┌────┴────┐                                                       │
│  ▼         ▼                                                       │
│ SQS       SQS                                                      │
│Queue 1   Queue 2                                                   │
│  │         │                                                       │
│  ▼         ▼                                                       │
│Consumer  Consumer                                                  │
│  A         B                                                       │
│                                                                    │
│  Benefits:                                                         │
│  • Fan-out with persistence                                        │
│  • Each consumer processes at own pace                             │
│  • DLQ for failed messages                                         │
│  • Retry logic per consumer                                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

```

---

## 💡 Key Takeaways

- **SQS** — message queue, decoupling, async processing

- **SNS** — pub/sub, fan-out, notifications

- **EventBridge** — event bus, content-based routing, scheduler

- **SNS + SQS** — надёжный fan-out pattern

- **FIFO Queue** — когда порядок и exactly-once важны

- **Long Polling** — эффективнее и дешевле short polling

---

## 📚 Additional Resources

- [SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/)
- [SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/)
- [EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)

---

## 🚀 Next Steps

**Следующие модули:**

- [13_APIGateway](../13_APIGateway/) — API Gateway и интеграции
- [20_Microservices](../20_Microservices/) — Паттерны микросервисов

**Практика:**

1. Создайте SQS очередь и обработайте сообщения Lambda
2. Настройте SNS topic с email подпиской
3. Реализуйте event-driven архитектуру с EventBridge



