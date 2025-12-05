# GitOps
## Декларативное управление инфраструктурой через Git

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Пройти модуль [06_IaC](../06_IaC/) — Infrastructure as Code
- Понимать основы Kubernetes
- Знать Git workflow (branches, PRs, merges)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить принципы и преимущества GitOps
- Настроить GitOps workflow с ArgoCD
- Организовать структуру репозиториев для GitOps
- Применять best practices для GitOps в production

---

## 1. Что такое GitOps?

### 1.1 Определение

**GitOps** — операционный фреймворк, который использует Git как единственный источник истины (single source of truth) для декларативной инфраструктуры и приложений.

Термин введён компанией Weaveworks в 2017 году.

```
┌─────────────────────────────────────────────────────────────────┐
│                      GitOps Workflow                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Developer ──▶ Git Push ──▶ Git Repository                      │
│                                    │                             │
│                                    ▼                             │
│                            GitOps Operator                       │
│                           (ArgoCD, Flux)                         │
│                                    │                             │
│                          ┌─────────┴─────────┐                  │
│                          │  Reconciliation   │                  │
│                          │  Loop             │                  │
│                          └─────────┬─────────┘                  │
│                                    │                             │
│                                    ▼                             │
│                            Kubernetes Cluster                    │
│                                                                  │
│  Desired State (Git) ←──── Compare ────▶ Actual State (K8s)    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Ключевые принципы GitOps

```python
gitops_principles = {
    "declarative": {
        "description": "Вся система описана декларативно",
        "example": "Kubernetes manifests, Helm charts, Kustomize"
    },
    "versioned_and_immutable": {
        "description": "Desired state хранится в Git",
        "example": "Вся история изменений, возможность rollback через git revert"
    },
    "pulled_automatically": {
        "description": "Агенты автоматически применяют изменения",
        "example": "ArgoCD следит за репозиторием и синхронизирует"
    },
    "continuously_reconciled": {
        "description": "Агенты постоянно сравнивают desired и actual state",
        "example": "Если кто-то изменил вручную — будет восстановлено"
    }
}
```

### 1.3 Push vs Pull Model

**Push Model (традиционный CI/CD):**
```
┌─────────┐     ┌─────────┐     ┌─────────┐
│   CI    │────▶│   CD    │────▶│ Cluster │
│ (build) │     │(deploy) │     │         │
└─────────┘     └─────────┘     └─────────┘

Проблемы:
- CI системе нужны credentials к кластеру
- Drift между Git и actual state
- Нет continuous reconciliation
```

**Pull Model (GitOps):**
```
┌─────────┐     ┌─────────┐
│   CI    │────▶│   Git   │
│ (build) │     │  Repo   │
└─────────┘     └────┬────┘
                     │
              (watches)
                     │
                     ▼
              ┌─────────────┐     ┌─────────┐
              │ GitOps      │────▶│ Cluster │
              │ Operator    │     │         │
              │ (in-cluster)│◀────│         │
              └─────────────┘     └─────────┘
                     │
              (reconciles)

Преимущества:
- Credentials остаются в кластере
- Continuous reconciliation
- Self-healing
```

---

## 2. ArgoCD

### 2.1 Обзор ArgoCD

ArgoCD — декларативный GitOps continuous delivery tool для Kubernetes.

**Ключевые возможности:**
- Web UI для визуализации состояния
- CLI для автоматизации
- SSO integration
- Multi-cluster support
- Webhook support
- Rollback functionality

### 2.2 Установка ArgoCD

```bash
# Создание namespace
kubectl create namespace argocd

# Установка ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Получение начального пароля
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# Port-forward для доступа к UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Вход через CLI
argocd login localhost:8080
```

### 2.3 Application CRD

```yaml
# argocd/applications/myapp.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  
  source:
    repoURL: https://github.com/myorg/myapp-manifests.git
    targetRevision: main
    path: overlays/production
  
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  
  syncPolicy:
    automated:
      prune: true        # Удалять ресурсы, которых нет в Git
      selfHeal: true     # Восстанавливать при drift
      allowEmpty: false  # Не удалять всё если Git пуст
    
    syncOptions:
      - CreateNamespace=true
      - PruneLast=true
    
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### 2.4 App of Apps Pattern

Управление несколькими приложениями через одно родительское.

```yaml
# argocd/apps-of-apps/root.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: applications
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    targetRevision: main
    path: argocd/applications
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

```
gitops-config/
└── argocd/
    └── applications/
        ├── myapp.yaml
        ├── another-app.yaml
        ├── monitoring.yaml
        └── ingress.yaml
```

---

## 3. Структура репозиториев

### 3.1 Monorepo vs Polyrepo

**Monorepo (всё в одном):**
```
gitops-repo/
├── apps/
│   ├── app1/
│   │   ├── base/
│   │   └── overlays/
│   └── app2/
├── infrastructure/
│   ├── monitoring/
│   └── ingress/
└── clusters/
    ├── production/
    └── staging/
```

**Polyrepo (раздельные репозитории):**
```
app1-manifests/        # Manifests для app1
app2-manifests/        # Manifests для app2
infrastructure-repo/   # Общая инфраструктура
cluster-config/        # Конфигурация кластеров
```

### 3.2 Рекомендуемая структура

```
gitops-repo/
├── README.md
├── .github/
│   └── workflows/
│       └── validate.yaml      # CI для проверки manifests
│
├── apps/                       # Приложения
│   ├── app1/
│   │   ├── base/              # Базовые manifests
│   │   │   ├── kustomization.yaml
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   └── configmap.yaml
│   │   └── overlays/          # Env-specific
│   │       ├── development/
│   │       │   ├── kustomization.yaml
│   │       │   └── replica-count.yaml
│   │       ├── staging/
│   │       │   ├── kustomization.yaml
│   │       │   └── resources.yaml
│   │       └── production/
│   │           ├── kustomization.yaml
│   │           ├── replica-count.yaml
│   │           └── resources.yaml
│   │
│   └── app2/
│       └── ...
│
├── infrastructure/             # Общая инфраструктура
│   ├── monitoring/
│   │   ├── prometheus/
│   │   └── grafana/
│   ├── ingress/
│   │   └── nginx/
│   └── cert-manager/
│
└── clusters/                   # ArgoCD Applications per cluster
    ├── production/
    │   ├── apps.yaml
    │   └── infrastructure.yaml
    └── staging/
        ├── apps.yaml
        └── infrastructure.yaml
```

### 3.3 Kustomize для управления environments

```yaml
# apps/myapp/base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
  - configmap.yaml

commonLabels:
  app: myapp
```

```yaml
# apps/myapp/base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1  # Будет переопределено в overlay
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myapp:latest  # Будет заменено
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 200m
              memory: 256Mi
```

```yaml
# apps/myapp/overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
  - ../../base

images:
  - name: myapp
    newName: ghcr.io/myorg/myapp
    newTag: v2.3.1

replicas:
  - name: myapp
    count: 5

patches:
  - path: resources.yaml
    target:
      kind: Deployment
      name: myapp
```

```yaml
# apps/myapp/overlays/production/resources.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    spec:
      containers:
        - name: myapp
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
            limits:
              cpu: 1000m
              memory: 1Gi
```

---

## 4. GitOps Workflow

### 4.1 Development Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    GitOps Development Flow                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Developer creates feature branch                             │
│     └──▶ git checkout -b feature/new-feature                    │
│                                                                  │
│  2. Update manifests (image tag, config)                        │
│     └──▶ Update kustomization.yaml with new image tag           │
│                                                                  │
│  3. Create Pull Request                                          │
│     └──▶ PR triggers CI validation                              │
│                                                                  │
│  4. CI validates manifests                                       │
│     └──▶ kustomize build, kubeval, policy checks                │
│                                                                  │
│  5. Code review and approval                                     │
│     └──▶ CODEOWNERS review required                             │
│                                                                  │
│  6. Merge to main                                                │
│     └──▶ ArgoCD detects change                                  │
│                                                                  │
│  7. ArgoCD syncs to cluster                                      │
│     └──▶ New version deployed                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 CI Pipeline для GitOps репозитория

```yaml
# .github/workflows/validate.yaml
name: Validate Manifests

on:
  pull_request:
    paths:
      - 'apps/**'
      - 'infrastructure/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Kustomize
        uses: imranismail/setup-kustomize@v2
      
      - name: Validate Kustomize builds
        run: |
          for dir in apps/*/overlays/*/; do
            echo "Validating $dir"
            kustomize build "$dir" > /dev/null
          done
      
      - name: Run kubeval
        uses: instrumenta/kubeval-action@master
        with:
          files: apps/*/overlays/*
      
      - name: Run Conftest (OPA policies)
        uses: instrumenta/conftest-action@master
        with:
          files: apps/*/overlays/*
          policy: policies/
```

### 4.3 Image Updater

Автоматическое обновление image tags.

```yaml
# ArgoCD Image Updater annotation
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  annotations:
    argocd-image-updater.argoproj.io/image-list: myapp=ghcr.io/myorg/myapp
    argocd-image-updater.argoproj.io/myapp.update-strategy: semver
    argocd-image-updater.argoproj.io/write-back-method: git
spec:
  # ...
```

---

## 5. Secrets Management в GitOps

### 5.1 Проблема секретов

```yaml
# ❌ Нельзя хранить секреты в Git!
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
data:
  password: c3VwZXJzZWNyZXQ=  # base64 encoded, NOT encrypted!
```

### 5.2 Решения

**1. Sealed Secrets:**
```yaml
# Зашифрованный секрет (можно хранить в Git)
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: db-credentials
spec:
  encryptedData:
    password: AgBy8hCi8...  # Зашифровано публичным ключом кластера
```

```bash
# Создание sealed secret
kubeseal --format yaml < secret.yaml > sealed-secret.yaml
```

**2. External Secrets Operator:**
```yaml
# Ссылка на секрет в AWS Secrets Manager
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: production/db/password
```

**3. SOPS (Mozilla):**
```yaml
# .sops.yaml — правила шифрования
creation_rules:
  - path_regex: .*secrets.*\.yaml$
    kms: arn:aws:kms:us-east-1:123456789:key/abc-123
    encrypted_regex: ^(data|stringData)$
```

```bash
# Шифрование
sops --encrypt secrets.yaml > secrets.enc.yaml

# ArgoCD расшифрует при sync (с плагином)
```

---

## 6. Multi-Cluster GitOps

### 6.1 Управление несколькими кластерами

```yaml
# clusters/production/apps.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-production
  namespace: argocd
spec:
  project: production
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    path: apps/myapp/overlays/production
  destination:
    server: https://production-cluster.example.com
    namespace: production
```

```yaml
# clusters/staging/apps.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-staging
  namespace: argocd
spec:
  project: staging
  source:
    repoURL: https://github.com/myorg/gitops-config.git
    path: apps/myapp/overlays/staging
  destination:
    server: https://staging-cluster.example.com
    namespace: staging
```

### 6.2 ApplicationSet

Генерация Applications из шаблонов.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: myapp
  namespace: argocd
spec:
  generators:
    - list:
        elements:
          - cluster: production
            url: https://production-cluster.example.com
            namespace: production
          - cluster: staging
            url: https://staging-cluster.example.com
            namespace: staging
  
  template:
    metadata:
      name: 'myapp-{{cluster}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/myorg/gitops-config.git
        targetRevision: main
        path: 'apps/myapp/overlays/{{cluster}}'
      destination:
        server: '{{url}}'
        namespace: '{{namespace}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

---

## 7. Best Practices

### 7.1 Git Best Practices

```python
gitops_git_best_practices = [
    "Atomic commits — один commit = одно логическое изменение",
    "Descriptive commit messages",
    "Branch protection на main",
    "Require PR reviews",
    "Squash commits при merge",
    "Подписывать commits (GPG)",
]
```

### 7.2 Repository Best Practices

```python
repo_best_practices = [
    "Отделять application repo от GitOps config repo",
    "Использовать Kustomize или Helm для environments",
    "Структурировать по apps → overlays → environments",
    "Документировать структуру в README",
    "Добавить CI для валидации manifests",
]
```

### 7.3 Security Best Practices

```python
security_best_practices = [
    "Никогда не хранить plain-text секреты в Git",
    "Использовать Sealed Secrets или External Secrets",
    "Ограничить permissions ArgoCD (least privilege)",
    "Включить audit logging",
    "Использовать RBAC в ArgoCD",
    "Регулярно ротировать credentials",
]
```

### 7.4 Operational Best Practices

```yaml
# Рекомендуемые настройки Application
spec:
  syncPolicy:
    automated:
      prune: true       # Удалять orphaned ресурсы
      selfHeal: true    # Исправлять drift
    
    syncOptions:
      - CreateNamespace=true
      - PruneLast=true  # Удалять в конце sync
      - ApplyOutOfSyncOnly=true  # Применять только изменённое
    
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
  
  # Health checks
  ignoreDifferences:
    - group: apps
      kind: Deployment
      jsonPointers:
        - /spec/replicas  # Игнорировать если HPA управляет
```

---

## 8. Troubleshooting

### 8.1 Общие проблемы

```python
common_issues = {
    "sync_failed": {
        "symptoms": "Application stuck in 'OutOfSync'",
        "causes": [
            "Invalid manifest",
            "Resource quota exceeded",
            "Image pull error",
            "RBAC issues"
        ],
        "solutions": [
            "Check ArgoCD UI for error details",
            "argocd app get <app-name>",
            "kubectl describe deployment <name>"
        ]
    },
    "drift_detected": {
        "symptoms": "Resources modified outside Git",
        "causes": [
            "Manual kubectl changes",
            "HPA modifying replicas",
            "Operators modifying resources"
        ],
        "solutions": [
            "Enable selfHeal",
            "Add ignoreDifferences for managed fields",
            "Document and prevent manual changes"
        ]
    }
}
```

### 8.2 Debugging Commands

```bash
# Проверить статус приложения
argocd app get myapp

# Посмотреть историю sync
argocd app history myapp

# Принудительный sync
argocd app sync myapp --force

# Rollback
argocd app rollback myapp <revision>

# Diff между Git и cluster
argocd app diff myapp

# Logs ArgoCD
kubectl logs -n argocd -l app.kubernetes.io/name=argocd-application-controller
```

---

## 💡 Key Takeaways

- **Git = Single Source of Truth**: Всё состояние системы описано в Git

- **Pull > Push**: Агенты в кластере pull изменения, а не CI push

- **Continuous Reconciliation**: Постоянное сравнение desired vs actual state

- **Secrets требуют особого внимания**: Sealed Secrets, External Secrets, SOPS

- **Структура репозитория важна**: Base + Overlays, чёткое разделение environments

---

## 🚀 Next Steps

**Related Modules:**
- [06_IaC](../06_IaC/) — Infrastructure as Code
- [08_Monitoring](../08_Monitoring/) — Мониторинг GitOps deployments

**Practice Ideas:**
1. Установите ArgoCD в локальный кластер (minikube/kind)
2. Создайте GitOps репозиторий с Kustomize overlays
3. Настройте автоматический sync с selfHeal

**Going Deeper:**
- ArgoCD documentation
- Flux documentation
- GitOps Working Group

---

## 📚 Additional Resources

**Documentation:**
- [ArgoCD](https://argo-cd.readthedocs.io/)
- [Flux](https://fluxcd.io/docs/)
- [Kustomize](https://kustomize.io/)

**Books & Guides:**
- "GitOps and Kubernetes" by Billy Yuen
- Weaveworks GitOps guides

**Tools:**
- [ArgoCD](https://argoproj.github.io/argo-cd/)
- [Flux](https://fluxcd.io/)
- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)
- [External Secrets Operator](https://external-secrets.io/)

---

