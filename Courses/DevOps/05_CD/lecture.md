# Continuous Delivery и Deployment
## Автоматизация релизов и стратегии развёртывания

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [04_CI](../04_CI/) — Continuous Integration
- Понимать Docker и контейнеризацию
- Иметь базовые знания о Kubernetes (опционально)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать Continuous Delivery и Continuous Deployment
- Проектировать deployment pipeline
- Применять различные стратегии развёртывания (blue-green, canary, rolling)
- Использовать feature flags для безопасных релизов
- Организовать rollback при проблемах

---

## 1. Continuous Delivery vs Continuous Deployment

### 1.1 Определения

**Continuous Delivery (CD):**
Практика, при которой код **всегда готов** к deployment в production. Финальный шаг (deploy в prod) выполняется **вручную** по решению бизнеса.

**Continuous Deployment:**
Расширение Continuous Delivery, где **каждое** успешное изменение **автоматически** деплоится в production.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           CI/CD Pipeline                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Commit ──▶ Build ──▶ Test ──▶ Package ──▶ Stage ──▶ Production              │
│    │         │        │         │          │           │                     │
│    └─────────┴────────┴─────────┴──────────┘           │                     │
│                    Continuous Integration               │                    │
│                                                         │                    │
│    └────────────────────────────────────────────────────┘                    │
│                    Continuous Delivery                                       │
│                    (manual approval)                    ▲                    │
│                                                         │                    │
│    └────────────────────────────────────────────────────┴──────────────────┐ │
│                    Continuous Deployment                                    ││
│                    (fully automated)                                        ││
└─────────────────────────────────────────────────────────────────────────────┘│
```

### 1.2 Выбор подхода

```python
def choose_cd_approach(context: dict) -> str:
    """Determine whether to use CD or Continuous Deployment."""
    
    # Continuous Deployment подходит когда:
    if all([
        context.get("comprehensive_test_coverage"),
        context.get("feature_flags_implemented"),
        context.get("automated_rollback"),
        context.get("strong_monitoring"),
        context.get("team_mature")
    ]):
        return "continuous_deployment"
    
    # Continuous Delivery с ручным approval когда:
    if any([
        context.get("regulatory_requirements"),  # Compliance
        context.get("business_approval_needed"),  # Marketing timing
        context.get("limited_test_coverage"),
        context.get("legacy_systems")
    ]):
        return "continuous_delivery"
    
    # По умолчанию начинаем с CD
    return "continuous_delivery"
```

### 1.3 Преимущества обоих подходов

| Continuous Delivery | Continuous Deployment |
|--------------------|-----------------------|
| Контроль timing релизов | Максимально быстрый feedback |
| Compliance-friendly | Минимум manual steps |
| Бизнес решает когда | Культура continuous improvement |
| Проще начать | Требует зрелой инфраструктуры |

---

## 2. Deployment Pipeline

### 2.1 Структура Pipeline

```yaml
# Полный CD pipeline

stages:
  - build          # Сборка artifact
  - test           # Все уровни тестирования
  - security       # Security scans
  - stage          # Deploy на staging
  - approve        # Manual gate (для CD)
  - production     # Deploy на production
  - verify         # Post-deploy verification
```

### 2.2 Пример полного Pipeline (GitHub Actions)

```yaml
# .github/workflows/cd.yml

name: CD Pipeline

on:
  push:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
      version: ${{ steps.version.outputs.version }}
    steps:
      - uses: actions/checkout@v4
      
      - name: Generate version
        id: version
        run: |
          VERSION=$(date +%Y%m%d)-$(git rev-parse --short HEAD)
          echo "version=$VERSION" >> $GITHUB_OUTPUT
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ steps.version.outputs.version }}
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run integration tests
        run: |
          docker run --rm \
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ needs.build.outputs.version }} \
            pytest tests/integration/

  security-scan:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ needs.build.outputs.version }}
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

  deploy-staging:
    needs: [build, test, security-scan]
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to staging
        run: |
          helm upgrade --install myapp ./helm \
            --namespace staging \
            --set image.tag=${{ needs.build.outputs.version }} \
            --set environment=staging \
            --wait --timeout=5m
      
      - name: Run smoke tests
        run: |
          ./scripts/smoke-tests.sh https://staging.example.com

  deploy-production:
    needs: [build, deploy-staging]
    runs-on: ubuntu-latest
    environment: 
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to production
        run: |
          helm upgrade --install myapp ./helm \
            --namespace production \
            --set image.tag=${{ needs.build.outputs.version }} \
            --set environment=production \
            --wait --timeout=5m
      
      - name: Verify deployment
        run: |
          ./scripts/verify-deployment.sh https://example.com
      
      - name: Notify success
        if: success()
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -H 'Content-type: application/json' \
            -d '{"text":"✅ Deployed ${{ needs.build.outputs.version }} to production"}'
      
      - name: Rollback on failure
        if: failure()
        run: |
          helm rollback myapp --namespace production
```

---

## 3. Deployment Strategies

### 3.1 Recreate (Big Bang)

Простейшая стратегия: остановить старую версию, запустить новую.

```
Version 1: ████████████████████ ──▶ Stop
                                    ↓
                              (Downtime)
                                    ↓
Version 2:                    Start ──▶ ████████████████████
```

**Плюсы:**

- Простота
- Никаких проблем совместимости версий

**Минусы:**

- Downtime
- Нет gradual rollout

**Когда использовать:**

- Dev/test environments
- Когда downtime допустим
- При incompatible changes (database schema)

### 3.2 Rolling Update

Постепенная замена instances одной версии на другую.

```
Time ──────────────────────────────────────────────▶

Pods: [v1] [v1] [v1] [v1]
      [v1] [v1] [v1] [v2] ← 1 pod updated
      [v1] [v1] [v2] [v2] ← 2 pods updated
      [v1] [v2] [v2] [v2] ← 3 pods updated
      [v2] [v2] [v2] [v2] ← Complete
```

```yaml
# Kubernetes Rolling Update

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1    # Максимум 1 pod недоступен
      maxSurge: 1          # Максимум 1 дополнительный pod
  template:
    spec:
      containers:
        - name: myapp
          image: myapp:v2
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
```

**Плюсы:**

- Zero downtime
- Gradual rollout
- Easy rollback

**Минусы:**

- Временно две версии одновременно
- Требует backward compatibility

### 3.3 Blue-Green Deployment

Две идентичные среды: Blue (текущая) и Green (новая).

```
┌─────────────────────────────────────────────────────────────┐
│                      Load Balancer                          │
│                           │                                 │
│              ┌────────────┴────────────┐                    │
│              │                         │                    │
│              ▼                         ▼                    │
│     ┌─────────────────┐       ┌─────────────────┐           │
│     │   Blue (v1)     │       │   Green (v2)    │           │
│     │   ACTIVE        │       │   STANDBY       │           │
│     │   100% traffic  │       │   0% traffic    │           │
│     └─────────────────┘       └─────────────────┘           │
│                                                             │
│  После тестирования Green:                                  │
│  Switch traffic: Blue 0% ↔ Green 100%                       │
└─────────────────────────────────────────────────────────────┘
```

```python
# Пример: Blue-Green switch с AWS ALB

import boto3

def switch_traffic(target_group_blue: str, target_group_green: str):
    """Switch traffic from blue to green."""
    elbv2 = boto3.client('elbv2')
    
    # Get listener
    listener_arn = get_listener_arn()
    
    # Update listener to point to green
    elbv2.modify_listener(
        ListenerArn=listener_arn,
        DefaultActions=[{
            'Type': 'forward',
            'TargetGroupArn': target_group_green
        }]
    )
    
    print(f"Traffic switched to green")

def rollback_to_blue(target_group_blue: str):
    """Instant rollback to blue environment."""
    elbv2 = boto3.client('elbv2')
    listener_arn = get_listener_arn()
    
    elbv2.modify_listener(
        ListenerArn=listener_arn,
        DefaultActions=[{
            'Type': 'forward',
            'TargetGroupArn': target_group_blue
        }]
    )
    
    print("Rolled back to blue")
```

**Плюсы:**

- Мгновенный switch
- Мгновенный rollback
- Полное тестирование перед switch

**Минусы:**

- Двойные ресурсы
- Сложность с stateful data

### 3.4 Canary Deployment

Постепенное направление трафика на новую версию.

```
┌─────────────────────────────────────────────────────────────┐
│                      Load Balancer                          │
│                           │                                 │
│         ┌─────────────────┼─────────────────┐               │
│         │                 │                 │               │
│         ▼                 ▼                 ▼               │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐        │
│  │ Version 1   │   │ Version 1   │   │ Version 2   │        │
│  │   Pod 1     │   │   Pod 2     │   │   Canary    │        │
│  │   45%       │   │   45%       │   │   10%       │        │
│  └─────────────┘   └─────────────┘   └─────────────┘        │
│                                                             │
│  Progression: 10% → 25% → 50% → 100%                        │
│  (based on metrics and time)                                │
└─────────────────────────────────────────────────────────────┘
```

```yaml
# Argo Rollouts Canary

apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        # 10% трафика на 5 минут
        - setWeight: 10
        - pause: {duration: 5m}
        
        # Проверка метрик
        - analysis:
            templates:
              - templateName: success-rate
            args:
              - name: service-name
                value: myapp
        
        # 25% на 10 минут
        - setWeight: 25
        - pause: {duration: 10m}
        
        # 50% на 15 минут
        - setWeight: 50
        - pause: {duration: 15m}
        
        # Полный rollout
        - setWeight: 100
        
      # Автоматический rollback при проблемах
      analysis:
        templates:
          - templateName: error-rate
        startingStep: 1
        args:
          - name: service-name
            value: myapp

---
# Шаблон анализа метрик

apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  args:
    - name: service-name
  metrics:
    - name: success-rate
      interval: 1m
      successCondition: result[0] >= 0.95
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{service="{{args.service-name}}",status=~"2.."}[5m]))
            /
            sum(rate(http_requests_total{service="{{args.service-name}}"}[5m]))
```

**Плюсы:**

- Минимальный риск
- Реальный production трафик
- Автоматический rollback по метрикам

**Минусы:**

- Сложность настройки
- Требует хорошего мониторинга
- Дольше, чем blue-green

### 3.5 Сравнение стратегий

| Strategy | Zero Downtime | Rollback Speed | Resource Cost | Complexity |
|----------|--------------|----------------|---------------|------------|
| Recreate | ❌ | Fast | Low | Low |
| Rolling | ✅ | Medium | Low | Medium |
| Blue-Green | ✅ | Instant | 2x | Medium |
| Canary | ✅ | Fast | +10-20% | High |

---

## 4. Feature Flags

### 4.1 Что такое Feature Flags

Feature flags (feature toggles) — техника, позволяющая включать/выключать функционал без деплоя.

```python
# Пример: простой feature flag

from typing import Optional

class FeatureFlags:
    def __init__(self, config: dict):
        self.flags = config
    
    def is_enabled(
        self, 
        flag_name: str, 
        user_id: Optional[str] = None,
        default: bool = False
    ) -> bool:
        flag = self.flags.get(flag_name)
        if flag is None:
            return default
        
        # Global flag
        if isinstance(flag, bool):
            return flag
        
        # Percentage rollout
        if "percentage" in flag:
            if user_id:
                # Consistent hashing для пользователя
                hash_value = hash(f"{flag_name}:{user_id}") % 100
                return hash_value < flag["percentage"]
        
        # User whitelist
        if "users" in flag and user_id:
            return user_id in flag["users"]
        
        return flag.get("enabled", default)

# Конфигурация

config = {
    "new_checkout_flow": {
        "enabled": True,
        "percentage": 25,  # 25% пользователей
        "users": ["beta_tester_1", "beta_tester_2"]  # Whitelist
    },
    "dark_mode": True,  # Для всех
    "experimental_search": False  # Выключено
}

flags = FeatureFlags(config)

# Использование

def get_checkout_page(user_id: str):
    if flags.is_enabled("new_checkout_flow", user_id):
        return render_new_checkout()
    else:
        return render_old_checkout()
```

### 4.2 Типы Feature Flags

```python
feature_flag_types = {
    "release_toggle": {
        "description": "Скрыть незавершённую фичу",
        "lifetime": "Короткий (дни/недели)",
        "example": "Новый UI, который ещё в разработке"
    },
    "experiment_toggle": {
        "description": "A/B тесты",
        "lifetime": "Средний (недели/месяцы)",
        "example": "Тестирование нового алгоритма рекомендаций"
    },
    "ops_toggle": {
        "description": "Операционный контроль",
        "lifetime": "Долгий",
        "example": "Kill switch для нагруженной фичи"
    },
    "permission_toggle": {
        "description": "Доступ для определённых пользователей",
        "lifetime": "Постоянный",
        "example": "Premium features"
    }
}
```

### 4.3 Best Practices для Feature Flags

```python
# 1. Удаляйте старые flags

class FeatureFlagManager:
    def __init__(self):
        self.flags = {}
        self.flag_metadata = {}
    
    def register_flag(self, name: str, owner: str, expiry_date: str):
        """Register flag with metadata."""
        self.flag_metadata[name] = {
            "owner": owner,
            "created": datetime.now(),
            "expiry": expiry_date,
            "status": "active"
        }
    
    def get_stale_flags(self) -> list[str]:
        """Find flags that should be removed."""
        stale = []
        for name, meta in self.flag_metadata.items():
            if datetime.now() > meta["expiry"]:
                stale.append(name)
        return stale
    
    def cleanup_flags(self):
        """Remove old flags from code."""
        stale = self.get_stale_flags()
        for flag in stale:
            print(f"⚠️ Flag '{flag}' is stale. Owner: {self.flag_metadata[flag]['owner']}")

# 2. Используйте naming conventions

good_flag_names = [
    "enable_new_search_v2",      # Ясно что это
    "experiment_checkout_flow",   # Эксперимент
    "ops_disable_notifications",  # Operations toggle
]

bad_flag_names = [
    "flag1",        # Непонятно
    "temp",         # Слишком общее
    "john_feature"  # Не описательно
]

# 3. Тестируйте оба пути

def test_feature_with_flag_on():
    with feature_flag_override("new_feature", True):
        result = some_function()
        assert result == expected_new_behavior

def test_feature_with_flag_off():
    with feature_flag_override("new_feature", False):
        result = some_function()
        assert result == expected_old_behavior
```

### 4.4 Инструменты для Feature Flags

| Tool | Type | Pros | Cons |
|------|------|------|------|
| LaunchDarkly | SaaS | Полнофункциональный, SDKs | Цена |
| Unleash | Open Source | Self-hosted, бесплатно | Нужна инфраструктура |
| Flagsmith | Hybrid | Open Source + Cloud | Меньше features |
| Custom | DIY | Полный контроль | Время на разработку |

---

## 5. Database Migrations

### 5.1 Zero-Downtime Migrations

```python
# Проблема: добавление обязательной колонки
# ❌ Плохо: сломает старый код при деплое

ALTER TABLE users ADD COLUMN phone VARCHAR(20) NOT NULL;

# ✅ Хорошо: backward-compatible migration
# Step 1: Add nullable column

ALTER TABLE users ADD COLUMN phone VARCHAR(20) NULL;

# Step 2: Deploy new code that writes to phone
# ... wait for deployment ...

# Step 3: Backfill existing data

UPDATE users SET phone = 'unknown' WHERE phone IS NULL;

# Step 4: Make column NOT NULL

ALTER TABLE users ALTER COLUMN phone SET NOT NULL;
```

### 5.2 Expand-Contract Pattern

```
┌───────────────────────────────────────────────────────────────────┐
│                    Expand-Contract Migration                      │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Phase 1: EXPAND                                                  │
│  ┌─────────────────┐     ┌─────────────────┐                      │
│  │ Old Schema      │────▶│ Old + New Schema│                      │
│  │ (column: name)  │     │ (name + fname,  │                      │
│  └─────────────────┘     │  lname)         │                      │
│                          └─────────────────┘                      │
│  - Add new columns                                                │
│  - Keep old columns                                               │
│  - Write to both                                                  │
│                                                                   │
│  Phase 2: MIGRATE                                                 │
│  - Backfill new columns from old                                  │
│  - Deploy code reading from new                                   │
│  - Verify consistency                                             │
│                                                                   │
│  Phase 3: CONTRACT                                                │
│  ┌─────────────────┐     ┌─────────────────┐                      │
│  │ Old + New Schema│────▶│ New Schema      │                      │
│  │ (name, fname,   │     │ (fname, lname)  │                      │
│  │  lname)         │     │                 │                      │
│  └─────────────────┘     └─────────────────┘                      │
│  - Remove old columns                                             │
│  - Clean up code                                                  │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

```python
# Пример: переименование колонки (3 деплоя)

# Deploy 1: Add new column, write to both

class User(Base):
    __tablename__ = 'users'
    
    name = Column(String)      # Old
    full_name = Column(String) # New
    
    def set_name(self, value):
        self.name = value
        self.full_name = value  # Write to both

# Deploy 2: Read from new, write to both

class User(Base):
    name = Column(String)      # Old (deprecated)
    full_name = Column(String) # New (primary)
    
    @property
    def display_name(self):
        return self.full_name or self.name  # Prefer new

# Deploy 3: Remove old column

class User(Base):
    full_name = Column(String)  # Only new
    
    @property
    def display_name(self):
        return self.full_name
```

---

## 6. Rollback Strategies

### 6.1 Типы Rollback

```python
rollback_strategies = {
    "instant_rollback": {
        "description": "Немедленный откат на предыдущую версию",
        "when": "Blue-green deployment, feature flags",
        "time": "Секунды",
        "data_loss": "Нет (если stateless)"
    },
    "rolling_rollback": {
        "description": "Постепенный откат pods",
        "when": "Kubernetes rolling update",
        "time": "Минуты",
        "data_loss": "Нет"
    },
    "database_rollback": {
        "description": "Откат миграций базы данных",
        "when": "Schema changes",
        "time": "Зависит от размера данных",
        "data_loss": "Возможна"
    },
    "forward_fix": {
        "description": "Исправление проблемы новым деплоем",
        "when": "Проще чинить, чем откатывать",
        "time": "Минуты-часы",
        "data_loss": "Нет"
    }
}
```

### 6.2 Автоматический Rollback

```yaml
# Kubernetes: автоматический rollback при проблемах

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  annotations:
    # Сохранять историю для rollback
    kubernetes.io/change-cause: "Deploy v2.3.1"
spec:
  revisionHistoryLimit: 10  # Хранить 10 версий
  progressDeadlineSeconds: 600  # Таймаут на деплой
  
  template:
    spec:
      containers:
        - name: myapp
          image: myapp:v2.3.1
          
          # Если не отвечает - Kubernetes не отправит трафик
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
            failureThreshold: 3
          
          # Если не отвечает - Kubernetes перезапустит pod
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 20
            failureThreshold: 3
```

```bash
# Ручной rollback в Kubernetes

kubectl rollout undo deployment/myapp

# Rollback на конкретную версию

kubectl rollout undo deployment/myapp --to-revision=5

# История ревизий

kubectl rollout history deployment/myapp
```

### 6.3 Rollback Checklist

```markdown
# Rollback Decision Checklist

## Когда откатывать?

- [ ] Error rate > 5% (или ваш threshold)
- [ ] P99 latency > 2x baseline
- [ ] Critical functionality не работает
- [ ] Data corruption detected
- [ ] Security vulnerability discovered

## Перед rollback

- [ ] Собрать информацию об инциденте
- [ ] Уведомить команду в #incidents
- [ ] Оценить impact (сколько пользователей затронуто)

## Во время rollback

- [ ] Выполнить rollback команду
- [ ] Мониторить метрики
- [ ] Проверить восстановление сервиса

## После rollback

- [ ] Подтвердить стабилизацию
- [ ] Обновить incident timeline
- [ ] Запланировать RCA (Root Cause Analysis)
```

---

## 7. Environment Management

### 7.1 Environment Promotion

```
┌───────────────────────────────────────────────────────────────┐
│                  Environment Promotion Flow                   │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Development ──▶ Staging ──▶ Production                       │
│       │             │            │                            │
│       ▼             ▼            ▼                            │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐                      │
│  │ dev.    │   │ staging.│   │ app.    │                      │
│  │ example │   │ example │   │ example │                      │
│  │ .com    │   │ .com    │   │ .com    │                      │
│  └─────────┘   └─────────┘   └─────────┘                      │
│                                                               │
│  Same artifact: myapp:abc123                                  │
│  Different configs per environment                            │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 7.2 Environment Parity

```yaml
# Принцип: environments должны быть максимально похожи
# docker-compose.yml для локальной разработки

services:
  app:
    build: .
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
      - REDIS_URL=redis://redis:6379
      - ENVIRONMENT=development
    depends_on:
      - db
      - redis

  db:
    image: postgres:15  # Та же версия, что в production
    environment:
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7  # Та же версия, что в production
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### 7.3 Configuration Management

```yaml
# Разделение config от кода
# config/production.yaml

database:
  host: ${DATABASE_HOST}
  port: 5432
  pool_size: 20
  ssl: true

redis:
  url: ${REDIS_URL}
  pool_size: 10

features:
  new_checkout: true
  dark_mode: false

logging:
  level: INFO
  format: json
```

```python
# Загрузка конфигурации

from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    database_host: str
    database_port: int = 5432
    database_pool_size: int = 10
    
    # Redis
    redis_url: str
    
    # Features
    feature_new_checkout: bool = False
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_prefix = ""

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

---

## 8. Deployment Verification

### 8.1 Smoke Tests

```python
# scripts/smoke_tests.py

import requests
import sys

def run_smoke_tests(base_url: str) -> bool:
    """Run basic smoke tests against deployed service."""
    tests = [
        ("Health check", f"{base_url}/health"),
        ("API endpoint", f"{base_url}/api/v1/status"),
        ("Static assets", f"{base_url}/static/app.js"),
    ]
    
    all_passed = True
    
    for name, url in tests:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✅ {name}: OK")
            else:
                print(f"❌ {name}: Status {response.status_code}")
                all_passed = False
        except Exception as e:
            print(f"❌ {name}: {e}")
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    base_url = sys.argv[1]
    success = run_smoke_tests(base_url)
    sys.exit(0 if success else 1)
```

### 8.2 Post-Deployment Monitoring

```python
# Что проверять после деплоя

post_deploy_checks = {
    "immediate": {  # 0-5 минут
        "error_rate": "< 1%",
        "response_time_p99": "< 500ms",
        "health_endpoint": "200 OK",
        "critical_endpoints": "responding"
    },
    "short_term": {  # 5-30 минут
        "error_rate_trend": "stable or decreasing",
        "memory_usage": "no leaks",
        "cpu_usage": "within baseline",
        "log_errors": "no new error types"
    },
    "medium_term": {  # 30 min - 4 hours
        "business_metrics": "normal",
        "user_complaints": "baseline",
        "database_performance": "stable"
    }
}
```

---

## 💡 Key Takeaways

- **Continuous Delivery vs Deployment**: Delivery = всегда готовы к релизу; Deployment = автоматический релиз

- **Выбор стратегии зависит от контекста**: Blue-green для быстрого rollback, Canary для минимизации риска

- **Feature flags — мощный инструмент**: Позволяют деплоить незавершённый код и контролировать rollout

- **Database migrations требуют особого внимания**: Expand-Contract pattern для zero-downtime

- **Rollback должен быть простым**: Если rollback сложный — пересмотрите архитектуру

---

## 🚀 Next Steps

**Related Modules:**

- [06_IaC](../06_IaC/) — Infrastructure as Code
- [07_GitOps](../07_GitOps/) — GitOps workflow
- [08_Monitoring](../08_Monitoring/) — Мониторинг deployments

**Practice Ideas:**

1. Реализуйте blue-green deployment для своего сервиса
2. Добавьте feature flags с постепенным rollout
3. Настройте автоматический rollback по метрикам

**Going Deeper:**

- "Continuous Delivery" by Jez Humble
- Argo Rollouts documentation
- LaunchDarkly feature flag patterns

---

## 📚 Additional Resources

**Books:**

- "Continuous Delivery" by Jez Humble & David Farley
- "Release It!" by Michael Nygard

**Tools:**

- [Argo Rollouts](https://argoproj.github.io/argo-rollouts/) — Progressive delivery для Kubernetes
- [Flagger](https://flagger.app/) — Automated canary deployments
- [LaunchDarkly](https://launchdarkly.com/) — Feature flag management

**Articles:**

- [Martin Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)
- [Deployment Strategies at Netflix](https://netflixtechblog.com/)

---





