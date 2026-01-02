# The Twelve-Factor App

---

## 📋 Prerequisites

- Опыт разработки веб-приложений
- Понимание концепций DevOps
- Знакомство с контейнеризацией

**Recommended prior modules:**

- [Cloud Native Intro](../18_CloudNativeIntro/)
- [Containers](../11_Containers/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять все 12 факторов при разработке
- Проектировать приложения для облака
- Избегать антипаттернов традиционной разработки
- Строить stateless, масштабируемые сервисы

---

## 1. Введение в 12-Factor App

### 1.1 Что это такое

**The Twelve-Factor App** — методология разработки SaaS-приложений, созданная инженерами Heroku в 2011 году. Эти принципы стали фундаментом Cloud Native разработки.

```python
twelve_factors = {
    1: "Codebase",
    2: "Dependencies", 
    3: "Config",
    4: "Backing Services",
    5: "Build, Release, Run",
    6: "Processes",
    7: "Port Binding",
    8: "Concurrency",
    9: "Disposability",
    10: "Dev/Prod Parity",
    11: "Logs",
    12: "Admin Processes"
}

print("The Twelve Factors:\n")
for num, factor in twelve_factors.items():
    print(f"  {num:2}. {factor}")
```

**Output:**
```
The Twelve Factors:

   1. Codebase
   2. Dependencies
   3. Config
   4. Backing Services
   5. Build, Release, Run
   6. Processes
   7. Port Binding
   8. Concurrency
   9. Disposability
  10. Dev/Prod Parity
  11. Logs
  12. Admin Processes
```

---

## 2. Factor I: Codebase

### One codebase tracked in revision control, many deploys

```
┌────────────────────────────────────────────────────────────────┐
│                    Factor I: Codebase                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ✅ CORRECT: One codebase → Many deploys                       │
│                                                                │
│         ┌──────────────┐                                       │
│         │   Git Repo   │                                       │
│         │  (codebase)  │                                       │
│         └──────┬───────┘                                       │
│                │                                               │
│     ┌──────────┼──────────┐                                    │
│     ▼          ▼          ▼                                    │
│  ┌─────┐   ┌─────┐   ┌─────┐                                   │
│  │ Dev │   │Stage│   │Prod │                                   │
│  └─────┘   └─────┘   └─────┘                                   │
│                                                                │
│  ❌ WRONG:                                                     │
│  • Разные репозитории для prod/dev                             │
│  • Копирование кода между серверами                            │
│  • Один репо для нескольких приложений (монорепо может быть ОК)│
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

```python
# Каждое приложение = один репозиторий
# Версия определяется тегами или коммитами

# Пример структуры

project_structure = """
my-api/
├── src/
│   ├── main.py
│   └── ...
├── tests/
├── Dockerfile
├── requirements.txt
├── .env.example      # Шаблон конфига (не secrets!)
└── README.md
"""
```

---

## 3. Factor II: Dependencies

### Explicitly declare and isolate dependencies

```python
# ❌ BAD: Implicit dependencies
# "У меня работает" — надежда на системные пакеты

# ✅ GOOD: Explicit dependencies

# requirements.txt (Python)

requirements = """
flask==3.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
redis==5.0.1
boto3==1.34.0
"""

# Или pyproject.toml с точными версиями

pyproject = """
[project]
dependencies = [
    "flask>=3.0.0,<4.0.0",
    "gunicorn>=21.0.0",
]
"""
```

```dockerfile
# Dockerfile с изолированными dependencies

FROM python:3.12-slim

WORKDIR /app

# Копируем и устанавливаем зависимости отдельно для кэширования

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

---

## 4. Factor III: Config

### Store config in the environment

```python
# ❌ BAD: Hardcoded config

DATABASE_URL = "postgresql://user:password@localhost/db"
API_KEY = "sk-12345secret"

# ❌ BAD: Config в коде с if/else для environments

if environment == "production":
    DATABASE_URL = "postgresql://prod-server/db"
else:
    DATABASE_URL = "postgresql://localhost/db"

# ✅ GOOD: Config из environment variables

import os

DATABASE_URL = os.environ["DATABASE_URL"]
API_KEY = os.environ["API_KEY"]
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
```

```yaml
# Kubernetes ConfigMap + Secrets

apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "INFO"
  CACHE_TTL: "3600"
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  DATABASE_URL: "postgresql://..."
  API_KEY: "sk-..."
```

```python
# Тест на 12-factor compliance: 
# Можете ли вы сделать codebase open-source 
# без раскрытия credentials?
```

---

## 5. Factor IV: Backing Services

### Treat backing services as attached resources

```
┌────────────────────────────────────────────────────────────────┐
│               Factor IV: Backing Services                      │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Backing Service = любой сервис, потребляемый по сети          │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Application                           │  │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                    │
│    ┌──────────┬───────────┼───────────┬──────────┐             │
│    ▼          ▼           ▼           ▼          ▼             │
│  ┌────┐   ┌──────┐   ┌───────┐   ┌───────┐   ┌──────┐          │
│  │ DB │   │Cache │   │ Queue │   │ SMTP  │   │ S3   │          │
│  │RDS │   │Redis │   │ SQS   │   │ SES   │   │      │          │
│  └────┘   └──────┘   └───────┘   └───────┘   └──────┘          │
│                                                                │
│  Принцип: Смена backing service = смена URL/credentials        │
│           Не требует изменения кода                            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

```python
# Приложение не должно знать, где работает backing service

# Development: локальный PostgreSQL

DATABASE_URL = "postgresql://localhost:5432/mydb"

# Production: RDS в AWS

DATABASE_URL = "postgresql://mydb.xxx.us-east-1.rds.amazonaws.com:5432/mydb"

# Код одинаковый:

from sqlalchemy import create_engine
engine = create_engine(os.environ["DATABASE_URL"])
```

---

## 6. Factor V: Build, Release, Run

### Strictly separate build and run stages

```
┌───────────────────────────────────────────────────────────────┐
│            Factor V: Build, Release, Run                      │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  BUILD STAGE                                                  │
│  ┌──────────────────────────────────────────────────────┐     │
│  │ Code + Dependencies → Build Artifact (Docker image)  │     │
│  │ • Компиляция                                          │    │
│  │ • Установка dependencies                              │    │
│  │ • Asset compilation                                   │    │
│  └────────────────────────────┬─────────────────────────┘     │
│                               ▼                               │
│  RELEASE STAGE                                                │
│  ┌──────────────────────────────────────────────────────┐     │
│  │ Build Artifact + Config → Release                     │    │
│  │ • Версионирование (v1.2.3, git sha)                  │     │
│  │ • Immutable — нельзя изменить                        │     │
│  │ • Можно откатить к предыдущему release               │     │
│  └────────────────────────────┬─────────────────────────┘     │
│                               ▼                               │
│  RUN STAGE                                                    │
│  ┌──────────────────────────────────────────────────────┐     │
│  │ Release → Running Processes                           │    │
│  │ • Запуск контейнеров                                 │     │
│  │ • Stateless execution                                │     │
│  └──────────────────────────────────────────────────────┘     │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

```yaml
# GitLab CI/CD пример

stages:
  - build
  - release
  - deploy

build:
  stage: build
  script:
    - docker build -t my-app:$CI_COMMIT_SHA .
    - docker push my-app:$CI_COMMIT_SHA

release:
  stage: release
  script:
    - docker tag my-app:$CI_COMMIT_SHA my-app:v1.2.3
    - docker push my-app:v1.2.3

deploy:
  stage: deploy
  script:
    - kubectl set image deployment/my-app app=my-app:v1.2.3
```

---

## 7. Factor VI: Processes

### Execute the app as one or more stateless processes

```python
# ❌ BAD: Stateful process

class BadApp:
    def __init__(self):
        self.user_sessions = {}  # State в памяти!
        self.cache = {}          # Потеряется при рестарте!
    
    def login(self, user_id):
        self.user_sessions[user_id] = {"logged_in": True}

# ✅ GOOD: Stateless process

class GoodApp:
    def __init__(self):
        self.redis = Redis(os.environ["REDIS_URL"])
        self.db = Database(os.environ["DATABASE_URL"])
    
    def login(self, user_id):
        # Session хранится в Redis
        self.redis.set(f"session:{user_id}", json.dumps({"logged_in": True}))
```

```
┌────────────────────────────────────────────────────────────────┐
│                  Stateless vs Stateful                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  STATELESS (12-factor)          STATEFUL (anti-pattern)        │
│  • Процесс можно убить          • Потеря данных при рестарте   │
│    и пересоздать                • Sticky sessions              │
│  • Горизонтальное               • Сложное масштабирование      │
│    масштабирование              • Один сервер = SPOF           │
│  • Any instance can             • Нужна сессионная             │
│    handle any request             аффинность                   │
│                                                                │
│  State хранится в:              State хранится в:              │
│  • База данных                  • Памяти процесса              │
│  • Redis/Memcached              • Локальной файловой системе   │
│  • S3                                                          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 8. Factor VII: Port Binding

### Export services via port binding

```python
# Приложение само экспортирует HTTP сервис
# Не зависит от внешнего web-сервера

# ✅ Flask с Gunicorn

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    # Development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Production: gunicorn -b 0.0.0.0:$PORT app:app
```

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Приложение слушает PORT

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

---

## 9. Factor VIII: Concurrency

### Scale out via the process model

```
┌────────────────────────────────────────────────────────────────┐
│              Factor VIII: Concurrency                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Масштабирование = добавление процессов, не threads            │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               Process Types                              │  │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │  │
│  │  web (HTTP requests)                                     │  │
│  │  ████████████████████████████████  x 10 instances       │   │
│  │                                                          │  │
│  │  worker (background jobs)                                │  │
│  │  ██████████████████  x 6 instances                      │   │
│  │                                                          │  │
│  │  scheduler (cron tasks)                                  │  │
│  │  ██  x 1 instance                                       │   │
│  │                                                          │  │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                │
│  Kubernetes: replicas: 10                                      │
│  ECS: desiredCount: 10                                         │
│  Heroku: web=10 worker=6                                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

```yaml
# Kubernetes Deployment с масштабированием

apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 10  # Горизонтальное масштабирование
  selector:
    matchLabels:
      app: myapp
      type: web
  template:
    spec:
      containers:
      - name: web
        image: myapp:v1.0
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: worker
spec:
  replicas: 6
  template:
    spec:
      containers:
      - name: worker
        image: myapp:v1.0
        command: ["python", "worker.py"]
```

---

## 10. Factor IX: Disposability

### Maximize robustness with fast startup and graceful shutdown

```python
import signal
import sys
from flask import Flask

app = Flask(__name__)

def graceful_shutdown(signum, frame):
    """Graceful shutdown handler"""
    print("Received shutdown signal, finishing current requests...")
    
    # 1. Перестать принимать новые запросы
    # 2. Дождаться завершения текущих
    # 3. Закрыть соединения с БД
    # 4. Выйти
    
    db.close()
    cache.close()
    sys.exit(0)

# Регистрируем обработчики сигналов

signal.signal(signal.SIGTERM, graceful_shutdown)
signal.signal(signal.SIGINT, graceful_shutdown)

# Fast startup
# • Минимизируйте работу при старте
# • Lazy initialization где возможно
# • Health check сразу после готовности
```

```yaml
# Kubernetes: Graceful shutdown

apiVersion: v1
kind: Pod
spec:
  terminationGracePeriodSeconds: 30  # Время на graceful shutdown
  containers:
  - name: app
    lifecycle:
      preStop:
        exec:
          command: ["/bin/sh", "-c", "sleep 5"]  # Время на drain
    readinessProbe:
      httpGet:
        path: /health
        port: 8000
      initialDelaySeconds: 5
      periodSeconds: 10
```

---

## 11. Factor X: Dev/Prod Parity

### Keep development, staging, and production as similar as possible

```python
# ❌ BAD: Разные backing services

dev_config = {
    "database": "sqlite:///local.db",      # SQLite в dev
    "cache": "memory",                      # In-memory cache
    "queue": None                           # Нет очереди
}

prod_config = {
    "database": "postgresql://...",         # PostgreSQL в prod
    "cache": "redis://...",                 # Redis
    "queue": "sqs://..."                    # SQS
}

# ✅ GOOD: Одинаковые сервисы везде
# docker-compose.yml для локальной разработки

docker_compose = """
version: '3.8'
services:
  app:
    build: .
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    environment:
      - POSTGRES_DB=app
      - POSTGRES_PASSWORD=postgres

  redis:
    image: redis:7
"""
```

```
┌────────────────────────────────────────────────────────────────┐
│                Three Gaps to Minimize                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  TIME GAP                                                      │
│  ❌ Dev → Prod: weeks                                          │
│  ✅ Dev → Prod: hours (CI/CD)                                  │
│                                                                │
│  PERSONNEL GAP                                                 │
│  ❌ Developers write, ops deploy                               │
│  ✅ Developers deploy their own code (DevOps)                  │
│                                                                │
│  TOOLS GAP                                                     │
│  ❌ SQLite in dev, PostgreSQL in prod                          │
│  ✅ Same tools everywhere (Docker Compose)                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 12. Factor XI: Logs

### Treat logs as event streams

```python
import logging
import sys

# ✅ GOOD: Логи в stdout

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

logger = logging.getLogger(__name__)

@app.route('/api/users/<user_id>')
def get_user(user_id):
    logger.info(f"Fetching user", extra={
        "user_id": user_id,
        "request_id": request.headers.get("X-Request-ID")
    })
    # ...

# ❌ BAD: Логи в файлы
# logging.FileHandler('/var/log/app.log')  # Где хранить в контейнере?
```

```
┌────────────────────────────────────────────────────────────────┐
│                   Log Aggregation                              │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  App → stdout → Container runtime → Log collector → Storage    │
│                                                                │
│  ┌─────┐     ┌─────────┐     ┌──────────┐     ┌───────────┐    │
│  │ App │ ──► │ Docker  │ ──► │FluentBit │ ──► │CloudWatch │    │
│  │     │     │ stdout  │     │/Fluentd  │     │/ELK/Loki  │    │
│  └─────┘     └─────────┘     └──────────┘     └───────────┘    │
│                                                                │
│  Приложение НЕ заботится о:                                    │
│  • Ротации логов                                               │
│  • Хранении логов                                              │
│  • Агрегации логов                                             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 13. Factor XII: Admin Processes

### Run admin/management tasks as one-off processes

```python
# Admin tasks выполняются как отдельные процессы
# В том же environment, что и основное приложение

# Примеры admin tasks:
# • Database migrations
# • Console/REPL
# • One-time scripts

# ❌ BAD: SSH на сервер и запуск скриптов
# ssh prod-server
# python manage.py migrate

# ✅ GOOD: Отдельный контейнер с той же средой
# kubectl exec -it deploy/myapp -- python manage.py migrate
# docker run --env-file .env myapp:v1.0 python manage.py migrate
```

```yaml
# Kubernetes Job для миграций

apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  template:
    spec:
      containers:
      - name: migration
        image: myapp:v1.0
        command: ["python", "manage.py", "migrate"]
        envFrom:
        - configMapRef:
            name: app-config
        - secretRef:
            name: app-secrets
      restartPolicy: Never
  backoffLimit: 1
```

---

## 14. Beyond Twelve Factors

### 14.1 Дополнительные факторы (2020+)

```python
additional_factors = {
    13: {
        "name": "API First",
        "description": "Design API before implementation"
    },
    14: {
        "name": "Telemetry",
        "description": "Metrics, tracing, health checks"
    },
    15: {
        "name": "Authentication/Authorization",
        "description": "Security as first-class concern"
    }
}
```

---

## 💡 Key Takeaways

1. **Codebase** — один репозиторий, много деплоев
2. **Dependencies** — явно объявляйте все зависимости
3. **Config** — конфигурация через environment variables
4. **Backing Services** — относитесь как к внешним ресурсам
5. **Build/Release/Run** — строго разделяйте этапы
6. **Processes** — stateless процессы
7. **Port Binding** — приложение само экспортирует сервис
8. **Concurrency** — масштабирование через процессы
9. **Disposability** — быстрый старт, graceful shutdown
10. **Dev/Prod Parity** — минимизируйте различия сред
11. **Logs** — потоки событий в stdout
12. **Admin Processes** — one-off задачи в том же environment

---

## 🚀 Next Steps

- [Microservices](../20_Microservices/)
- [Observability](../21_Observability/)

---

## 📚 Additional Resources

- [12factor.net](https://12factor.net/) — оригинальный манифест
- "Beyond the Twelve-Factor App" — книга Kevin Hoffman

---





