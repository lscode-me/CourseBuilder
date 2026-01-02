# API Gateway

---

## 📋 Prerequisites

- Понимание REST API
- Знакомство с Lambda
- Базовые знания IAM

---

## 🎯 Learning Objectives

- Создавать REST и HTTP API
- Настраивать авторизацию
- Использовать throttling и caching
- Понимать различия типов API Gateway

---

## 1. Что такое API Gateway

### 1.1 Обзор

```
┌───────────────────────────────────────────────────────────────────┐
│              API Gateway                                          │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Clients                                                          │
│  (Web, Mobile, IoT)                                               │
│      │                                                            │
│      ▼                                                            │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    API Gateway                               │ │
│  │                                                              │ │
│  │  • Request routing                                          │  │
│  │  • Authentication & Authorization                           │  │
│  │  • Rate limiting & Throttling                               │  │
│  │  • Request/Response transformation                          │  │
│  │  • Caching                                                  │  │
│  │  • SSL termination                                          │  │
│  │  • API versioning                                           │  │
│  │                                                              │ │
│  └─────────────────────────────────────────────────────────────┘  │
│                        │                                          │
│        ┌───────────────┼───────────────┐                          │
│        ▼               ▼               ▼                          │
│    ┌────────┐     ┌────────┐     ┌────────┐                       │
│    │ Lambda │     │  ECS   │     │  HTTP  │                       │
│    │Function│     │Service │     │Backend │                       │
│    └────────┘     └────────┘     └────────┘                       │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 1.2 Типы API Gateway в AWS

```python
api_types = {
    "REST API": {
        "features": "Full feature set (caching, WAF, API keys, usage plans)",
        "latency": "Higher (~100ms overhead)",
        "pricing": "$3.50 per million requests",
        "use_case": "Public APIs, complex transformations"
    },
    "HTTP API": {
        "features": "Core features (OIDC, OAuth2, simpler)",
        "latency": "Lower (~10ms overhead)",
        "pricing": "$1.00 per million requests",
        "use_case": "Microservices, Lambda proxies, cost-sensitive"
    },
    "WebSocket API": {
        "features": "Bidirectional real-time communication",
        "use_case": "Chat, gaming, live updates"
    }
}

print("API Gateway Types:\n")
for api_type, details in api_types.items():
    print(f"{api_type}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()
```

---

## 2. REST API

### 2.1 Создание REST API

```bash
# Create REST API

aws apigateway create-rest-api \
    --name "OrderAPI" \
    --description "Order management API" \
    --endpoint-configuration types=REGIONAL

# Get root resource

ROOT_ID=$(aws apigateway get-resources \
    --rest-api-id $API_ID \
    --query 'items[?path==`/`].id' --output text)

# Create resource /orders

aws apigateway create-resource \
    --rest-api-id $API_ID \
    --parent-id $ROOT_ID \
    --path-part "orders"

# Create method

aws apigateway put-method \
    --rest-api-id $API_ID \
    --resource-id $RESOURCE_ID \
    --http-method POST \
    --authorization-type NONE
```

### 2.2 Lambda Integration

```python
# Lambda proxy integration - самый простой способ
# API Gateway передаёт весь request в Lambda

def lambda_handler(event, context):
    # event содержит всё: headers, body, path params, query params
    body = json.loads(event.get('body', '{}'))
    path_params = event.get('pathParameters', {})
    query_params = event.get('queryStringParameters', {})
    
    # Обработка
    order_id = create_order(body)
    
    # Формат ответа для API Gateway
    return {
        'statusCode': 201,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'order_id': order_id,
            'status': 'created'
        })
    }
```

### 2.3 Request/Response Mapping

```
# Mapping Templates (Velocity Template Language)
# Для не-proxy интеграций

# Request mapping (API Gateway → Backend)

{
    "orderData": {
        "id": "$input.params('orderId')",
        "items": $input.json('$.items'),
        "customerId": "$context.authorizer.claims.sub"
    }
}

# Response mapping (Backend → API Gateway)
#set($inputRoot = $input.path('$'))
{
    "orderId": "$inputRoot.id",
    "status": "$inputRoot.status",
    "createdAt": "$inputRoot.created_at"
}
```

---

## 3. HTTP API

### 3.1 Создание HTTP API

```bash
# HTTP API - проще и дешевле

aws apigatewayv2 create-api \
    --name "OrderAPI" \
    --protocol-type HTTP \
    --target "arn:aws:lambda:us-east-1:123456789012:function:orderHandler"

# Автоматически создаёт:
# - $default stage с auto-deploy
# - Lambda integration
# - Route $default для всех requests
```

### 3.2 Routes

```python
# HTTP API routes более гибкие

routes = {
    "GET /orders": "list_orders",
    "POST /orders": "create_order",
    "GET /orders/{orderId}": "get_order",
    "PUT /orders/{orderId}": "update_order",
    "DELETE /orders/{orderId}": "delete_order",
    "$default": "catch_all_handler"
}

# В Lambda получаем route key

def lambda_handler(event, context):
    route_key = event.get('routeKey')  # e.g., "GET /orders/{orderId}"
    path_params = event.get('pathParameters', {})
    order_id = path_params.get('orderId')
```

---

## 4. Authorization

### 4.1 Типы авторизации

```
┌───────────────────────────────────────────────────────────────────┐
│              Authorization Options                                │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  IAM Authorization                                                │
│  └── AWS Signature v4                                             │
│  └── For AWS services, internal APIs                              │
│                                                                   │
│  Lambda Authorizer                                                │
│  └── Custom auth logic in Lambda                                  │
│  └── JWT validation, database lookup                              │
│                                                                   │
│  Cognito Authorizer                                               │
│  └── JWT tokens from Cognito User Pools                           │
│  └── Best for user authentication                                 │
│                                                                   │
│  JWT Authorizer (HTTP API only)                                   │
│  └── Built-in JWT validation                                      │
│  └── OIDC providers (Auth0, Okta, etc.)                           │
│                                                                   │
│  API Keys                                                         │
│  └── For rate limiting, not security!                             │
│  └── Usage plans and quotas                                       │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 4.2 Lambda Authorizer

```python
def lambda_authorizer(event, context):
    token = event.get('authorizationToken', '').replace('Bearer ', '')
    method_arn = event['methodArn']
    
    try:
        # Validate token (JWT, database, etc.)
        claims = validate_token(token)
        
        return {
            'principalId': claims['sub'],
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': method_arn
                }]
            },
            'context': {
                'userId': claims['sub'],
                'role': claims.get('role', 'user')
            }
        }
    except Exception:
        raise Exception('Unauthorized')
```

### 4.3 JWT Authorizer (HTTP API)

```bash
# Создание JWT authorizer для HTTP API

aws apigatewayv2 create-authorizer \
    --api-id $API_ID \
    --authorizer-type JWT \
    --identity-source '$request.header.Authorization' \
    --name "cognito-auth" \
    --jwt-configuration \
        Issuer="https://cognito-idp.us-east-1.amazonaws.com/us-east-1_xxx",\
        Audience="client-id-here"
```

---

## 5. Throttling и Quotas

### 5.1 Rate Limiting

```python
throttling_config = {
    "Account Level": {
        "default": "10,000 requests/second",
        "burst": "5,000 requests",
        "note": "Soft limits, can request increase"
    },
    "Stage Level": {
        "description": "Per-stage throttling",
        "example": "1,000 req/s for dev, 10,000 for prod"
    },
    "Method Level": {
        "description": "Per-method throttling",
        "example": "POST /orders: 100 req/s"
    },
    "Usage Plans": {
        "description": "Per-client throttling with API keys",
        "example": "Free tier: 100 req/day, Premium: unlimited"
    }
}

# Usage Plan example
# aws apigateway create-usage-plan \
#     --name "FreeTier" \
#     --throttle burstLimit=10,rateLimit=5 \
#     --quota limit=1000,period=DAY
```

---

## 6. Caching (REST API only)

```python
caching_config = {
    "TTL": "300 seconds (default), 0-3600",
    "Capacity": "0.5GB - 237GB",
    "Per-key": "Cache by path params, query params, headers",
    "Invalidation": "API call or automatic on TTL expiry"
}

# Enable caching
# aws apigateway update-stage \
#     --rest-api-id $API_ID \
#     --stage-name prod \
#     --patch-operations \
#         op=replace,path=/cacheClusterEnabled,value=true \
#         op=replace,path=/cacheClusterSize,value=0.5
```

---

## 7. CORS

```python
# CORS для HTTP API (автоматически)

aws apigatewayv2 update-api \
    --api-id $API_ID \
    --cors-configuration \
        AllowOrigins="https://example.com",\
        AllowMethods="GET,POST,PUT,DELETE",\
        AllowHeaders="Content-Type,Authorization",\
        MaxAge=300

# Для REST API - нужен OPTIONS method или в Lambda response headers
```

---

## 8. Deployment и Stages

```bash
# Deploy to stage

aws apigateway create-deployment \
    --rest-api-id $API_ID \
    --stage-name prod \
    --description "Production deployment"

# Stage variables

aws apigateway update-stage \
    --rest-api-id $API_ID \
    --stage-name prod \
    --patch-operations \
        op=replace,path=/variables/lambdaAlias,value=PROD

# В Lambda integration: ${stageVariables.lambdaAlias}
```

---

## 💡 Key Takeaways

- **REST API** — full features, higher latency, $3.50/million

- **HTTP API** — simpler, lower latency, $1.00/million

- **Lambda proxy** — simplest integration, Lambda handles routing

- **JWT Authorizer** — built-in for HTTP API

- **Caching** — REST API only, reduces backend load

- **Usage Plans** — rate limiting per client with API keys

---

## 📚 Additional Resources

- [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/)
- [HTTP API vs REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)

---

## 🚀 Next Steps

**Следующие модули:**

- [14_CDN](../14_CDN/) — CloudFront и кеширование
- [22_Security](../22_Security/) — Безопасность API

**Практика:**

1. Создайте REST API с Lambda интеграцией
2. Настройте авторизацию через Cognito или Lambda Authorizer
3. Реализуйте rate limiting с Usage Plans




