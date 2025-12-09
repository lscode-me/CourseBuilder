# CDN: CloudFront

---

## 📋 Prerequisites

- Понимание HTTP
- Знакомство с S3
- Базовые знания DNS

---

## 🎯 Learning Objectives

- Понимать как работает CDN
- Создавать CloudFront distributions
- Настраивать caching policies
- Защищать контент

---

## 1. Что такое CDN

### 1.1 Концепция

```
┌────────────────────────────────────────────────────────────────────┐
│              Content Delivery Network                               │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Without CDN:                                                      │
│  User (Tokyo) ────────── 200ms ──────────► Origin (US-East)       │
│                                                                     │
│  With CDN:                                                         │
│  User (Tokyo) ── 20ms ──► Edge (Tokyo) ── cached ──► Origin       │
│                                                                     │
│                                                                     │
│                    ┌─────────────────┐                             │
│                    │   Origin        │                             │
│                    │   (S3, ALB)     │                             │
│                    └────────┬────────┘                             │
│                             │                                      │
│           ┌─────────────────┼─────────────────┐                   │
│           │                 │                 │                   │
│           ▼                 ▼                 ▼                   │
│     ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│     │  Edge    │     │  Edge    │     │  Edge    │              │
│     │ (Tokyo)  │     │ (London) │     │ (Sydney) │              │
│     └────┬─────┘     └────┬─────┘     └────┬─────┘              │
│          │                │                │                      │
│          ▼                ▼                ▼                      │
│       Users            Users            Users                     │
│                                                                     │
│  Benefits:                                                         │
│  • Lower latency (content closer to users)                        │
│  • Reduced origin load                                            │
│  • DDoS protection                                                │
│  • SSL termination at edge                                        │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 CloudFront Infrastructure

```python
cloudfront_infrastructure = {
    "Edge Locations": {
        "count": "400+ locations globally",
        "function": "Cache content, serve users"
    },
    "Regional Edge Caches": {
        "count": "13 locations",
        "function": "Mid-tier cache, reduce origin fetches"
    },
    "Origin Shield": {
        "function": "Additional caching layer",
        "benefit": "Reduce origin load further"
    }
}

print("CloudFront Infrastructure:")
for component, details in cloudfront_infrastructure.items():
    print(f"\n{component}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
```

---

## 2. Создание Distribution

### 2.1 S3 Origin

```bash
# Create distribution with S3 origin
aws cloudfront create-distribution \
    --origin-domain-name my-bucket.s3.amazonaws.com \
    --default-root-object index.html

# С OAC (Origin Access Control) для private bucket
aws cloudfront create-origin-access-control \
    --origin-access-control-config \
        Name=my-oac,\
        SigningProtocol=sigv4,\
        SigningBehavior=always,\
        OriginAccessControlOriginType=s3
```

### 2.2 ALB/Custom Origin

```python
distribution_config = {
    "Origins": [{
        "DomainName": "api.example.com",
        "Id": "api-origin",
        "CustomOriginConfig": {
            "HTTPPort": 80,
            "HTTPSPort": 443,
            "OriginProtocolPolicy": "https-only",
            "OriginSSLProtocols": ["TLSv1.2"]
        }
    }],
    "DefaultCacheBehavior": {
        "TargetOriginId": "api-origin",
        "ViewerProtocolPolicy": "redirect-to-https",
        "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",  # CachingOptimized
        "AllowedMethods": ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"],
        "CachedMethods": ["GET", "HEAD"]
    }
}
```

---

## 3. Caching

### 3.1 Cache Key

```
┌────────────────────────────────────────────────────────────────────┐
│              Cache Key Components                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Default Cache Key:                                                │
│  └── URL path                                                      │
│                                                                     │
│  Optional additions:                                               │
│  ├── Query strings                                                 │
│  │   example.com/api?page=1&sort=date                             │
│  │                                                                 │
│  ├── Headers                                                       │
│  │   Accept-Language: en-US                                        │
│  │                                                                 │
│  └── Cookies                                                       │
│      session_id=abc123                                             │
│                                                                     │
│  Best practice: Minimize cache key for better hit ratio            │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Cache Policies

```python
cache_policies = {
    "CachingOptimized": {
        "description": "Maximum caching for static content",
        "ttl": {"default": 86400, "min": 1, "max": 31536000},
        "settings": "No query strings, no headers, no cookies"
    },
    "CachingDisabled": {
        "description": "No caching, always forward to origin",
        "use_case": "Dynamic content, API responses"
    },
    "CachingOptimizedForUncompressedObjects": {
        "description": "Like CachingOptimized but for non-gzip"
    }
}

# Custom cache policy
custom_policy = {
    "Name": "my-cache-policy",
    "DefaultTTL": 3600,
    "MinTTL": 0,
    "MaxTTL": 86400,
    "ParametersInCacheKeyAndForwardedToOrigin": {
        "QueryStringsConfig": {
            "QueryStringBehavior": "whitelist",
            "QueryStrings": {"Items": ["page", "limit"]}
        },
        "HeadersConfig": {
            "HeaderBehavior": "whitelist",
            "Headers": {"Items": ["Accept-Language"]}
        }
    }
}
```

### 3.3 TTL и Cache-Control

```python
# Origin может управлять кэшированием через headers
cache_control_examples = {
    "Cache-Control: max-age=3600": "Cache for 1 hour",
    "Cache-Control: no-cache": "Validate with origin before serving",
    "Cache-Control: no-store": "Never cache",
    "Cache-Control: public, max-age=31536000": "Cache for 1 year (static assets)",
    "Cache-Control: private, max-age=0": "No CDN caching, only browser"
}

# CloudFront использует:
# 1. Cache-Control: max-age (если есть)
# 2. Expires header (если нет max-age)
# 3. Default TTL из cache policy (если ничего нет)
```

---

## 4. Behaviors

### 4.1 Path-based Routing

```
┌────────────────────────────────────────────────────────────────────┐
│              Cache Behaviors                                        │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Path Pattern         Origin            Cache Policy               │
│  ─────────────        ──────            ────────────               │
│  /api/*               ALB               CachingDisabled            │
│  /static/*            S3 bucket         CachingOptimized (1 year)  │
│  /images/*            S3 bucket         CachingOptimized           │
│  Default (*)          S3 bucket         CachingOptimized           │
│                                                                     │
│  Order matters! More specific patterns first.                      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## 5. Security

### 5.1 HTTPS

```python
ssl_config = {
    "Viewer Protocol Policy": {
        "redirect-to-https": "Redirect HTTP to HTTPS",
        "https-only": "Only HTTPS, HTTP returns 403",
        "allow-all": "Both HTTP and HTTPS"
    },
    "Origin Protocol Policy": {
        "https-only": "CloudFront → Origin only HTTPS",
        "match-viewer": "Same protocol as viewer",
        "http-only": "CloudFront → Origin only HTTP"
    },
    "SSL Certificate": {
        "default": "*.cloudfront.net certificate",
        "custom": "ACM certificate for custom domain"
    }
}
```

### 5.2 OAC (Origin Access Control)

```python
# OAC для private S3 bucket
# Только CloudFront может читать из bucket

# S3 bucket policy
s3_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "AllowCloudFrontServicePrincipal",
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudfront.amazonaws.com"
        },
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::my-bucket/*",
        "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EXXX"
            }
        }
    }]
}
```

### 5.3 Signed URLs и Cookies

```python
import boto3
from botocore.signers import CloudFrontSigner
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import datetime

def rsa_signer(message):
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

# Create signed URL
key_pair_id = 'KXXX'
url = 'https://d111.cloudfront.net/private/video.mp4'
expire_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

cloudfront_signer = CloudFrontSigner(key_pair_id, rsa_signer)
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date
)
```

---

## 6. CloudFront Functions и Lambda@Edge

```
┌────────────────────────────────────────────────────────────────────┐
│              Edge Computing                                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                      CloudFront Functions    Lambda@Edge           │
│  ────────────────    ───────────────────    ───────────           │
│  Runtime              JavaScript             Node.js, Python       │
│  Execution time       < 1 ms                 5-30 seconds          │
│  Memory               2 MB                   128-10,240 MB         │
│  Network access       No                     Yes                   │
│  File system          No                     Yes (/tmp)            │
│  Pricing              $0.10/million          $0.60/million         │
│  Trigger points       Viewer request/resp    All 4 trigger points │
│                                                                     │
│  Use cases:                                                        │
│  CloudFront Functions: URL rewrites, header manipulation,         │
│                        redirects, simple auth                      │
│  Lambda@Edge: A/B testing, image optimization,                    │
│               authentication, geo-based routing                    │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 6.1 CloudFront Function Example

```javascript
// URL rewrite: /products/123 → /products.html?id=123
function handler(event) {
    var request = event.request;
    var uri = request.uri;
    
    // Rewrite clean URLs
    var match = uri.match(/^\/products\/(\d+)$/);
    if (match) {
        request.uri = '/products.html';
        request.querystring = { id: { value: match[1] } };
    }
    
    // Add security headers
    request.headers['x-frame-options'] = { value: 'DENY' };
    
    return request;
}
```

---

## 7. Invalidation

```bash
# Invalidate cached content
aws cloudfront create-invalidation \
    --distribution-id EXXX \
    --paths "/index.html" "/css/*" "/js/*"

# Wildcard invalidation
aws cloudfront create-invalidation \
    --distribution-id EXXX \
    --paths "/*"

# Pricing: First 1000 paths/month free, then $0.005/path
# Best practice: Use versioned filenames instead (app.v2.js)
```

---

## 💡 Key Takeaways

- **CDN** — caches content at edge locations globally
- **Cache Key** — minimize for better hit ratio
- **OAC** — secure access to private S3 buckets
- **Behaviors** — different caching for different paths
- **CloudFront Functions** — lightweight, < 1ms
- **Invalidation** — use versioned URLs instead when possible

---

## 📚 Additional Resources

- [CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)
- [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)

---

## 🚀 Next Steps

**Следующие модули:**
- [15_DataServices](../15_DataServices/) — Аналитические сервисы
- [23_CostManagement](../23_CostManagement/) — Оптимизация затрат

**Практика:**
1. Настройте CloudFront distribution для S3 bucket
2. Реализуйте кеширование с разными TTL
3. Добавьте CloudFront Function для redirect
