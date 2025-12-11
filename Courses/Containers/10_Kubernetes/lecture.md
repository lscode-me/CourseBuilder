# Kubernetes
## Введение в оркестрацию контейнеров

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь опыт работы с Docker
- Понимать Docker Compose и Swarm
- Знать основы сетевого взаимодействия контейнеров

**Recommended prior modules:**

- [Docker](../08_Docker/)
- [Docker Compose & Swarm](../09_Compose/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить архитектуру Kubernetes
- Создавать и управлять базовыми ресурсами (Pods, Deployments, Services)
- Настраивать конфигурацию через ConfigMaps и Secrets
- Понимать сетевую модель Kubernetes

---

## 1. Что такое Kubernetes

### 1.1 Kubernetes в двух словах

Kubernetes (K8s) — платформа для автоматизации развёртывания, масштабирования и управления контейнеризованными приложениями.

**Ключевые возможности:**

- Оркестрация контейнеров на кластере машин
- Автоматическое восстановление (self-healing)
- Горизонтальное масштабирование
- Service discovery и load balancing
- Автоматические rollouts и rollbacks
- Управление конфигурацией и секретами

### 1.2 Kubernetes vs Docker Swarm

| Аспект | Docker Swarm | Kubernetes |
|--------|--------------|------------|
| Сложность | Простой | Сложный |
| Масштабируемость | Средняя | Высокая |
| Экосистема | Ограниченная | Огромная |
| Learning curve | Низкая | Высокая |
| Production readiness | Да | Да (стандарт) |
| Managed services | Мало | AWS EKS, GKE, AKS |

### 1.3 История Kubernetes

| Год | Событие |
|-----|---------|
| 2003-2004 | Google создаёт Borg |
| 2013 | Google создаёт Omega |
| 2014 | Google открывает Kubernetes |
| 2015 | Kubernetes 1.0, создание CNCF |
| 2018 | Kubernetes становится "graduated" в CNCF |
| 2020+ | De-facto стандарт оркестрации |

---

## 2. Архитектура Kubernetes

### 2.1 Компоненты кластера

```

┌─────────────────────────────────────────────────────────────────┐
│                        Kubernetes Cluster                        │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                     Control Plane                            │ │
│  │                                                              │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │ │
│  │  │  API Server  │  │  Scheduler   │  │  Controller  │      │ │
│  │  │              │  │              │  │   Manager    │      │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │ │
│  │                                                              │ │
│  │  ┌──────────────┐  ┌──────────────┐                        │ │
│  │  │     etcd     │  │ Cloud        │                        │ │
│  │  │              │  │ Controller   │                        │ │
│  │  └──────────────┘  └──────────────┘                        │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              │                                    │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                      Worker Nodes                            │ │
│  │                                                              │ │
│  │  ┌──────────────────────┐  ┌──────────────────────┐        │ │
│  │  │       Node 1         │  │       Node 2         │        │ │
│  │  │  ┌────────────────┐  │  │  ┌────────────────┐  │        │ │
│  │  │  │    kubelet     │  │  │  │    kubelet     │  │        │ │
│  │  │  └────────────────┘  │  │  └────────────────┘  │        │ │
│  │  │  ┌────────────────┐  │  │  ┌────────────────┐  │        │ │
│  │  │  │   kube-proxy   │  │  │  │   kube-proxy   │  │        │ │
│  │  │  └────────────────┘  │  │  └────────────────┘  │        │ │
│  │  │  ┌────────────────┐  │  │  ┌────────────────┐  │        │ │
│  │  │  │Container Runtime│  │  │  │Container Runtime│  │        │ │
│  │  │  └────────────────┘  │  │  └────────────────┘  │        │ │
│  │  │  ┌─────┐ ┌─────┐    │  │  ┌─────┐ ┌─────┐    │        │ │
│  │  │  │ Pod │ │ Pod │    │  │  │ Pod │ │ Pod │    │        │ │
│  │  │  └─────┘ └─────┘    │  │  └─────┘ └─────┘    │        │ │
│  │  └──────────────────────┘  └──────────────────────┘        │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

```

### 2.2 Control Plane компоненты

**API Server (kube-apiserver)**
- Центральная точка управления
- RESTful API для всех операций
- Аутентификация и авторизация

**etcd**
- Распределённое key-value хранилище
- Хранит всё состояние кластера
- Критически важный компонент

**Scheduler (kube-scheduler)**
- Распределяет Pods по Nodes
- Учитывает ресурсы, affinity, taints

**Controller Manager**
- Запускает контроллеры (ReplicaSet, Deployment, etc.)
- Обеспечивает желаемое состояние

### 2.3 Node компоненты

**kubelet**
- Агент на каждой ноде
- Управляет жизненным циклом Pods
- Отвечает за healthchecks

**kube-proxy**
- Сетевой прокси на каждой ноде
- Реализует Services (iptables/IPVS)

**Container Runtime**
- containerd, CRI-O
- Запускает контейнеры

---

## 3. Основные ресурсы Kubernetes

### 3.1 Pod

Pod — минимальная единица развёртывания в Kubernetes.

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.25-alpine
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"

```

```bash
# Создание Pod
kubectl apply -f pod.yaml

# Список Pods
kubectl get pods

# Детальная информация
kubectl describe pod nginx-pod

# Логи
kubectl logs nginx-pod

# Exec в Pod
kubectl exec -it nginx-pod -- sh

# Удаление
kubectl delete pod nginx-pod

```

### 3.2 Multi-container Pod

```yaml

apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
    - name: app
      image: myapp:latest
      ports:
        - containerPort: 8080
      volumeMounts:
        - name: shared-data
          mountPath: /data
    
    - name: sidecar
      image: logging-agent:latest
      volumeMounts:
        - name: shared-data
          mountPath: /logs
  
  volumes:
    - name: shared-data
      emptyDir: {}

```

### 3.3 Deployment

Deployment управляет ReplicaSet и обеспечивает декларативные обновления.

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25-alpine
          ports:
            - containerPort: 80
          resources:
            requests:
              memory: "64Mi"
              cpu: "250m"
            limits:
              memory: "128Mi"
              cpu: "500m"
          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 15
            periodSeconds: 20
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0

```

```bash
# Применение
kubectl apply -f deployment.yaml

# Масштабирование
kubectl scale deployment nginx-deployment --replicas=5

# Обновление образа
kubectl set image deployment/nginx-deployment nginx=nginx:1.26-alpine

# История развёртываний
kubectl rollout history deployment/nginx-deployment

# Откат
kubectl rollout undo deployment/nginx-deployment

# Статус rollout
kubectl rollout status deployment/nginx-deployment

```

### 3.4 Service

Service обеспечивает стабильный endpoint для доступа к Pods.

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP

```

**Типы Service:**

| Type | Описание |
|------|----------|
| ClusterIP | Внутренний IP (default) |
| NodePort | Порт на каждой ноде |
| LoadBalancer | Внешний load balancer (cloud) |
| ExternalName | DNS CNAME |

```yaml
# NodePort Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080

---
# LoadBalancer Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80

```

### 3.5 ConfigMap и Secret

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "db.example.com"
  LOG_LEVEL: "info"
  config.json: |
    {
      "feature_flags": {
        "new_ui": true
      }
    }

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  # base64 encoded
  DATABASE_PASSWORD: cGFzc3dvcmQxMjM=
  API_KEY: c2VjcmV0a2V5

```

**Использование в Pod:**

```yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    spec:
      containers:
        - name: app
          image: myapp:latest
          env:
            # Из ConfigMap
            - name: DATABASE_HOST
              valueFrom:
                configMapKeyRef:
                  name: app-config
                  key: DATABASE_HOST
            # Из Secret
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: app-secret
                  key: DATABASE_PASSWORD
          # Все значения из ConfigMap
          envFrom:
            - configMapRef:
                name: app-config
          # Монтирование как файлы
          volumeMounts:
            - name: config-volume
              mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: app-config

```

---

## 4. Хранилище в Kubernetes

### 4.1 Volumes

```yaml

apiVersion: v1
kind: Pod
metadata:
  name: pod-with-storage
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - name: cache-volume
          mountPath: /cache
        - name: config-volume
          mountPath: /etc/config
          readOnly: true
  volumes:
    # EmptyDir - временное хранилище
    - name: cache-volume
      emptyDir: {}
    
    # ConfigMap как volume
    - name: config-volume
      configMap:
        name: app-config

```

### 4.2 PersistentVolume и PersistentVolumeClaim

```yaml
# persistentvolume.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /data/pv

---
# persistentvolumeclaim.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard

---
# Использование в Pod
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-pvc
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - name: data
          mountPath: /data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: my-pvc

```

---

## 5. Сеть в Kubernetes

### 5.1 Сетевая модель

**Kubernetes Network Model:**

- Каждый Pod получает уникальный IP
- Pods могут общаться напрямую без NAT
- Nodes могут общаться с Pods без NAT
- IP, который Pod видит — тот же, что видят другие

### 5.2 DNS в Kubernetes

```bash
# Формат DNS для Service
<service-name>.<namespace>.svc.cluster.local

# Примеры
nginx-service.default.svc.cluster.local
database.production.svc.cluster.local

# Внутри одного namespace можно использовать короткое имя
nginx-service

```

### 5.3 Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api
                port:
                  number: 8080
  tls:
    - hosts:
        - myapp.example.com
      secretName: tls-secret

```

### 5.4 Network Policies

```yaml

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - protocol: TCP
          port: 5432

```

---

## 6. kubectl — основные команды

### 6.1 Получение информации

```bash
# Nodes
kubectl get nodes
kubectl describe node <node-name>

# Pods
kubectl get pods
kubectl get pods -A              # All namespaces
kubectl get pods -o wide         # Больше информации
kubectl get pods -l app=nginx    # По label
kubectl get pods --watch         # Watch mode

# Deployments
kubectl get deployments
kubectl describe deployment nginx-deployment

# Services
kubectl get services
kubectl get svc

# Все ресурсы
kubectl get all

```

### 6.2 Создание и изменение

```bash
# Применение манифеста
kubectl apply -f manifest.yaml
kubectl apply -f ./manifests/

# Создание из командной строки
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80

# Редактирование
kubectl edit deployment nginx-deployment

# Patch
kubectl patch deployment nginx -p '{"spec":{"replicas":5}}'

```

### 6.3 Отладка

```bash
# Логи
kubectl logs pod-name
kubectl logs pod-name -c container-name   # Multi-container
kubectl logs -f pod-name                   # Follow
kubectl logs --previous pod-name           # Previous instance

# Exec
kubectl exec -it pod-name -- sh
kubectl exec pod-name -- cat /etc/config

# Port forward
kubectl port-forward pod/nginx 8080:80
kubectl port-forward svc/nginx-service 8080:80

# Debug
kubectl debug pod/nginx -it --image=busybox

```

### 6.4 Namespace management

```bash
# Создание namespace
kubectl create namespace production

# Установка default namespace
kubectl config set-context --current --namespace=production

# Ресурсы в namespace
kubectl get pods -n production
kubectl apply -f manifest.yaml -n production

```

---

## 7. Локальная разработка

### 7.1 Minikube

```bash
# Установка
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Запуск
minikube start

# Dashboard
minikube dashboard

# Сервисы
minikube service nginx-service

# Остановка
minikube stop

```

### 7.2 kind (Kubernetes in Docker)

```bash
# Установка
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Создание кластера
kind create cluster --name my-cluster

# С конфигурацией
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
EOF

# Удаление
kind delete cluster --name my-cluster

```

### 7.3 k3s (lightweight)

```bash
# Установка
curl -sfL https://get.k3s.io | sh -

# Проверка
sudo k3s kubectl get nodes

# Kubeconfig
sudo cat /etc/rancher/k3s/k3s.yaml

```

---

## 💡 Key Takeaways

- **Kubernetes** — стандарт оркестрации контейнеров в production

- **Pod** — минимальная единица, может содержать несколько контейнеров

- **Deployment** управляет ReplicaSet и обеспечивает rolling updates

- **Service** предоставляет стабильный endpoint для доступа к Pods

- **kubectl** — основной инструмент для работы с кластером

---

## 🚀 Next Steps

**Practice Ideas:**

1. Разверните приложение в Minikube или kind
2. Настройте Ingress с TLS
3. Реализуйте canary deployment
4. Настройте HPA (Horizontal Pod Autoscaler)

**Going Deeper:**

- Helm — пакетный менеджер для Kubernetes
- Operators — автоматизация сложных приложений
- Service Mesh (Istio, Linkerd)
- GitOps (ArgoCD, Flux)

---

## 📚 Additional Resources

**Documentation:**

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/)

**Learning:**

- [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [CKAD/CKA Certification](https://www.cncf.io/certification/)

**Tools:**

- [Lens](https://k8slens.dev/) — Kubernetes IDE
- [k9s](https://k9scli.io/) — Terminal UI
- [Helm](https://helm.sh/) — Package manager

---





