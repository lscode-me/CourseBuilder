# Continuous Integration
## Автоматизация сборки, тестирования и интеграции кода

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Пройти модуль [03_Processes](../03_Processes/) — Процессы DevOps
- Знать основы Git (branches, merge, pull requests)
- Иметь опыт написания тестов (unit tests)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить принципы и практики Continuous Integration
- Настроить CI pipeline с GitHub Actions или GitLab CI
- Применять trunk-based development
- Реализовать эффективную стратегию тестирования в CI
- Оптимизировать время выполнения CI pipeline

---

## 1. Что такое Continuous Integration?

### 1.1 Определение

**Continuous Integration (CI)** — практика частой интеграции изменений кода в общий репозиторий с автоматической проверкой каждого изменения.

```
Developer A ──┐
              │
Developer B ──┼──▶ Main Branch ──▶ Automated Build ──▶ Automated Tests
              │          │
Developer C ──┘          │
                         │
              Fast feedback ◀────────────────────────────┘
```

### 1.2 Ключевые принципы CI

**1. Единый source repository:**

- Весь код в одном месте
- Version control для всего (код, конфиги, скрипты)
- Main branch всегда готов к релизу

**2. Автоматизация сборки:**

- Один клик/команда для сборки
- Воспроизводимость на любой машине
- Никаких ручных шагов

**3. Автоматические тесты:**

- Каждый commit запускает тесты
- Быстрая обратная связь
- Тесты — часть pipeline, не опция

**4. Все коммитят в main ежедневно:**

- Маленькие частые изменения
- Интеграция как минимум раз в день
- Избегать долгоживущих веток

**5. Каждый commit собирается:**

- CI сервер мониторит репозиторий
- Автоматический build при каждом push
- Быстрое обнаружение проблем

**6. Исправление сломанного build — приоритет #1:**

- Сломанный build блокирует всю команду
- Максимум 10 минут на фикс или revert
- "Stop the line" культура

### 1.3 Преимущества CI

```python
# Сравнение: с CI vs без CI

comparison = {
    "integration_frequency": {
        "without_ci": "Раз в неделю/месяц (merge hell)",
        "with_ci": "Несколько раз в день"
    },
    "bug_detection": {
        "without_ci": "При ручном тестировании (дни/недели)",
        "with_ci": "В течение минут после commit"
    },
    "merge_conflicts": {
        "without_ci": "Большие, сложные конфликты",
        "with_ci": "Маленькие, легко решаемые"
    },
    "release_readiness": {
        "without_ci": "Долгий release cycle",
        "with_ci": "Всегда готовы к релизу"
    },
    "feedback_loop": {
        "without_ci": "Дни/недели",
        "with_ci": "Минуты"
    }
}
```

---

## 2. Branching Strategies

### 2.1 Trunk-Based Development

**Рекомендуемый подход для CI/CD:**

```
main ─────●─────●─────●─────●─────●─────●─────●─────▶
          │     │     │     │     │     │     │
          │     ├──○──┘     │     ├──○──┘     │
          │     │ (short    │     │ (short    │
          ├──○──┘  branch)  ├──○──┘  branch)  │
          │                 │                 │
    (direct commits        (direct commits   (direct commits
     to main OR             to main OR        to main)
     short branches)        short branches)
```

**Правила trunk-based:**

- Branches живут максимум 1-2 дня
- Merge в main минимум раз в день
- Feature flags для незавершённых фич
- Все изменения проходят CI до merge

### 2.2 GitHub Flow

**Упрощённый workflow:**

```
main ─────●─────●─────────────●─────────────●─────▶
          │                   │             │
          └──○──○──○──────────┘             │
              feature branch                │
              (PR + review + CI)            │
                                           │
                        └──○──○────────────┘
                            hotfix branch
```

**Шаги:**

1. Create branch from main
2. Make changes, commit
3. Open Pull Request
4. CI runs, code review
5. Merge to main
6. Deploy

### 2.3 GitFlow (для справки)

**Сложный workflow, менее подходит для CI/CD:**

```
main     ─────●───────────────────●───────────────▶
              │                   │
develop  ─────●─────●─────●───────●─────●─────▶
              │     │     │       │     │
feature  ─────○─────┘     │       │     │
                          │       │     │
release  ─────────────────○───────┘     │
                                        │
hotfix   ───────────────────────────────○──▶
```

**Недостатки GitFlow:**

- Долгоживущие ветки (develop, release)
- Сложность merge
- Медленный feedback loop
- Противоречит trunk-based development

### 2.4 Выбор стратегии

```python
def choose_branching_strategy(context: dict) -> str:
    """Recommend branching strategy based on context."""
    
    if context.get("team_size", 0) <= 5:
        if context.get("deployment_frequency") == "multiple_per_day":
            return "trunk-based"  # Best for CD
        return "github-flow"
    
    if context.get("multiple_versions_in_production"):
        return "gitflow"  # When you need version branches
    
    if context.get("ci_cd_maturity") == "high":
        return "trunk-based"
    
    return "github-flow"  # Safe default
```

---

## 3. CI Pipeline

### 3.1 Структура Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CI Pipeline                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌────────┐ │
│  │ Checkout│──▶│  Build  │──▶│  Lint   │──▶│  Test   │──▶│Artifact│ │
│  │   Code  │   │         │   │         │   │         │   │        │ │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘   └────────┘ │
│       │             │             │             │             │     │
│       │             │             │             │             │     │
│       ▼             ▼             ▼             ▼             ▼     │
│    < 30s         < 2min        < 1min       < 10min       < 1min    │
│                                                                     │
│  Total pipeline time target: < 15 minutes                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 GitHub Actions Example

```yaml
# .github/workflows/ci.yml

name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: "3.11"

jobs:
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: |
          pip install ruff mypy
      
      - name: Run Ruff (linter)
        run: ruff check .
      
      - name: Run Ruff (formatter)
        run: ruff format --check .
      
      - name: Run MyPy (type check)
        run: mypy src/

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    needs: lint  # Depends on lint passing
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
        run: |
          pytest --cov=src --cov-report=xml --cov-report=html
      
      - name: Upload coverage report
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml

  build:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: test
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          exit-code: '1'
          severity: 'CRITICAL,HIGH'
```

### 3.3 GitLab CI Example

```yaml
# .gitlab-ci.yml

stages:
  - lint
  - test
  - build
  - security

variables:
  PYTHON_VERSION: "3.11"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.pip-cache"

cache:
  paths:
    - .pip-cache/
    - .venv/

.python_setup: &python_setup
  image: python:${PYTHON_VERSION}
  before_script:
    - python -m venv .venv
    - source .venv/bin/activate
    - pip install --upgrade pip

lint:
  <<: *python_setup
  stage: lint
  script:
    - pip install ruff mypy
    - ruff check .
    - ruff format --check .
    - mypy src/

test:
  <<: *python_setup
  stage: test
  services:
    - postgres:15
  variables:
    POSTGRES_PASSWORD: postgres
    DATABASE_URL: postgresql://postgres:postgres@postgres:5432/test
  script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
    - pytest --cov=src --cov-report=xml
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

security_scan:
  stage: security
  image: 
    name: aquasec/trivy:latest
    entrypoint: [""]
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

---

## 4. Тестирование в CI

### 4.1 Test Pyramid

```
                    ┌─────────────┐
                   │    E2E      │  Slow, expensive
                   │   Tests     │  Few tests
                  ├─────────────┤
                 │  Integration  │  Medium speed
                │     Tests      │  More tests
               ├─────────────────┤
              │    Unit Tests     │  Fast, cheap
             │                    │  Many tests
            └──────────────────────┘
```

**Рекомендуемое соотношение:**

- Unit tests: 70%
- Integration tests: 20%
- E2E tests: 10%

### 4.2 Test Categories в CI

```python
# pytest markers для разных типов тестов

import pytest

# Unit test - быстрый, изолированный

@pytest.mark.unit
def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90

# Integration test - проверяет взаимодействие компонентов

@pytest.mark.integration
def test_order_service_creates_order(db_session):
    service = OrderService(db_session)
    order = service.create_order(user_id=1, items=[...])
    assert order.id is not None
    assert order.status == "pending"

# E2E test - проверяет весь flow

@pytest.mark.e2e
def test_user_can_complete_checkout(browser):
    browser.visit("/products")
    browser.click("Add to Cart")
    browser.click("Checkout")
    browser.fill("card_number", "4242...")
    browser.click("Pay")
    assert "Order confirmed" in browser.page_source

# Slow test marker

@pytest.mark.slow
def test_large_data_processing():
    # Этот тест занимает много времени
    result = process_million_records()
    assert result.success
```

### 4.3 CI Test Strategy

```yaml
# Оптимизированная стратегия тестирования
# .github/workflows/ci.yml

jobs:
  # Быстрые тесты - запускаются всегда
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run unit tests
        run: pytest -m "unit" --timeout=10
    timeout-minutes: 5

  # Integration тесты - запускаются на PR и main
  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v4
      - name: Run integration tests
        run: pytest -m "integration" --timeout=60
    timeout-minutes: 15

  # E2E тесты - только на main или scheduled
  e2e-tests:
    runs-on: ubuntu-latest
    needs: integration-tests
    if: github.ref == 'refs/heads/main' || github.event_name == 'schedule'
    steps:
      - uses: actions/checkout@v4
      - name: Run E2E tests
        run: pytest -m "e2e" --timeout=120
    timeout-minutes: 30
```

### 4.4 Flaky Tests

**Flaky test** — тест, который иногда проходит, иногда нет, без изменений в коде.

```python
# Пример flaky test

def test_api_response_time():
    start = time.time()
    response = requests.get("https://api.example.com/data")
    duration = time.time() - start
    
    # Flaky: зависит от сети, нагрузки сервера
    assert duration < 1.0  # Может fail при медленной сети

# Исправленная версия

def test_api_returns_valid_data():
    response = requests.get("https://api.example.com/data")
    
    # Проверяем функциональность, не performance
    assert response.status_code == 200
    assert "data" in response.json()
```

**Стратегия работы с flaky tests:**

```yaml
# Quarantine flaky tests

jobs:
  stable-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Run stable tests
        run: pytest -m "not flaky" --strict-markers

  flaky-tests:
    runs-on: ubuntu-latest
    continue-on-error: true  # Не блокируют pipeline
    steps:
      - name: Run flaky tests (quarantine)
        run: pytest -m "flaky" --reruns 3
```

---

## 5. Оптимизация CI Pipeline

### 5.1 Parallelization

```yaml
# Параллельное выполнение независимых jobs

jobs:
  lint:
    runs-on: ubuntu-latest
    # ...

  security-scan:
    runs-on: ubuntu-latest
    # Не зависит от lint, запускается параллельно
    # ...

  unit-tests:
    runs-on: ubuntu-latest
    # Параллельно с lint и security
    # ...

  # Интеграционные тесты ждут unit тесты
  integration-tests:
    needs: [lint, unit-tests]  # Зависимость
    runs-on: ubuntu-latest
```

**Параллельные тесты (test sharding):**

```yaml
# Разбиение тестов на части

test:
  runs-on: ubuntu-latest
  strategy:
    matrix:
      shard: [1, 2, 3, 4]
  steps:
    - name: Run test shard
      run: |
        pytest --shard-id=${{ matrix.shard }} --num-shards=4
```

### 5.2 Caching

```yaml
# Кэширование зависимостей

steps:
  - uses: actions/checkout@v4
  
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'  # Встроенное кэширование pip
  
  # Или явное кэширование
  - name: Cache pip packages
    uses: actions/cache@v4
    with:
      path: ~/.cache/pip
      key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
      restore-keys: |
        ${{ runner.os }}-pip-
  
  - name: Cache Docker layers
    uses: actions/cache@v4
    with:
      path: /tmp/.buildx-cache
      key: ${{ runner.os }}-buildx-${{ github.sha }}
      restore-keys: |
        ${{ runner.os }}-buildx-
```

### 5.3 Incremental Builds

```yaml
# Запуск только изменённых компонентов

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      backend: ${{ steps.changes.outputs.backend }}
      frontend: ${{ steps.changes.outputs.frontend }}
    steps:
      - uses: dorny/paths-filter@v2
        id: changes
        with:
          filters: |
            backend:
              - 'backend/**'
              - 'requirements.txt'
            frontend:
              - 'frontend/**'
              - 'package.json'

  test-backend:
    needs: detect-changes
    if: needs.detect-changes.outputs.backend == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Test backend
        run: pytest backend/

  test-frontend:
    needs: detect-changes
    if: needs.detect-changes.outputs.frontend == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Test frontend
        run: npm test
```

### 5.4 Target Pipeline Times

```python
# Целевые времена для CI pipeline

target_times = {
    "commit_to_feedback": "< 10 min",  # Идеально
    "acceptable": "< 15 min",
    "needs_optimization": "> 20 min",
    
    "stages": {
        "checkout": "< 30 sec",
        "install_deps": "< 2 min (with cache)",
        "lint": "< 1 min",
        "unit_tests": "< 5 min",
        "integration_tests": "< 10 min",
        "build": "< 3 min",
        "security_scan": "< 5 min"
    }
}

def diagnose_slow_pipeline(actual_times: dict) -> list[str]:
    """Identify stages that need optimization."""
    issues = []
    for stage, actual in actual_times.items():
        target = target_times["stages"].get(stage)
        if target and actual > parse_time(target):
            issues.append(f"{stage}: {actual} (target: {target})")
    return issues
```

---

## 6. Code Quality Gates

### 6.1 Quality Checks

```yaml
# Обязательные проверки качества

name: Quality Gates

on: [pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Для анализа изменений
      
      # Linting
      - name: Lint code
        run: ruff check . --output-format=github
      
      # Type checking
      - name: Type check
        run: mypy src/ --strict
      
      # Code coverage
      - name: Run tests with coverage
        run: pytest --cov=src --cov-fail-under=80
      
      # Security scan
      - name: Security scan
        run: bandit -r src/
      
      # Dependency check
      - name: Check dependencies
        run: pip-audit
```

### 6.2 Branch Protection Rules

```yaml
# Рекомендуемые настройки Branch Protection (GitHub)

branch_protection:
  main:
    required_status_checks:
      strict: true
      contexts:
        - lint
        - test
        - security-scan
    
    required_pull_request_reviews:
      required_approving_review_count: 1
      dismiss_stale_reviews: true
      require_code_owner_reviews: true
    
    required_linear_history: true
    
    restrictions:
      users: []
      teams: ["maintainers"]
```

### 6.3 CODEOWNERS

```
# .github/CODEOWNERS

# Default owners

* @team-leads

# Backend

/backend/ @backend-team
/backend/api/ @api-team @backend-team

# Infrastructure

/terraform/ @platform-team
/k8s/ @platform-team
/.github/workflows/ @platform-team

# Security-sensitive

/auth/ @security-team @backend-team
**/secrets* @security-team
```

---

## 7. CI Best Practices

### 7.1 Build Once, Deploy Many

```yaml
# Собираем artifact один раз, используем во всех environments

build:
  runs-on: ubuntu-latest
  outputs:
    image-tag: ${{ steps.build.outputs.tag }}
  steps:
    - name: Build and push
      id: build
      run: |
        TAG="${{ github.sha }}"
        docker build -t myapp:$TAG .
        docker push myapp:$TAG
        echo "tag=$TAG" >> $GITHUB_OUTPUT

deploy-staging:
  needs: build
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to staging
      run: |
        # Используем тот же image
        helm upgrade app ./chart --set image.tag=${{ needs.build.outputs.image-tag }}

deploy-production:
  needs: [build, deploy-staging]
  runs-on: ubuntu-latest
  environment: production  # Requires approval
  steps:
    - name: Deploy to production
      run: |
        # Тот же image, другой environment
        helm upgrade app ./chart --set image.tag=${{ needs.build.outputs.image-tag }}
```

### 7.2 Environment Variables

```yaml
# Правильное управление секретами

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      # Non-sensitive config
      APP_ENV: test
      LOG_LEVEL: debug
    
    steps:
      - name: Run tests
        env:
          # Secrets из GitHub Secrets
          DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
          API_KEY: ${{ secrets.TEST_API_KEY }}
        run: pytest

  # НИКОГДА не делать так:
  # run: echo "API_KEY=secret123" >> $GITHUB_ENV  # Плохо!
```

### 7.3 Notifications

```yaml
# Уведомления о статусе pipeline

notify:
  runs-on: ubuntu-latest
  needs: [test, build]
  if: always()  # Запускается всегда
  
  steps:
    - name: Notify Slack on failure
      if: failure()
      uses: slackapi/slack-github-action@v1
      with:
        channel-id: 'ci-alerts'
        payload: |
          {
            "text": "❌ CI Failed",
            "blocks": [
              {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "*CI Pipeline Failed*\n*Repo:* ${{ github.repository }}\n*Branch:* ${{ github.ref_name }}\n*Commit:* ${{ github.sha }}"
                }
              }
            ]
          }
      env:
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
```

### 7.4 Self-Hosted Runners

```yaml
# Когда использовать self-hosted runners

self_hosted_use_cases:
  - "Нужен доступ к internal resources"
  - "Специфическое hardware (GPU, ARM)"
  - "Compliance требования (данные не покидают сеть)"
  - "Большой объём CI (экономия на GitHub Actions minutes)"

# Пример использования

jobs:
  build:
    runs-on: self-hosted  # Вместо ubuntu-latest
    steps:
      - name: Build on internal server
        run: make build
```

---

## 8. Metrics и мониторинг CI

### 8.1 Ключевые метрики

```python
# CI Metrics

ci_metrics = {
    "pipeline_duration": {
        "description": "Время выполнения pipeline",
        "target": "< 15 min",
        "measurement": "P95 duration"
    },
    "success_rate": {
        "description": "Процент успешных builds",
        "target": "> 95%",
        "measurement": "successful / total"
    },
    "flaky_test_rate": {
        "description": "Процент flaky тестов",
        "target": "< 1%",
        "measurement": "flaky_failures / total_runs"
    },
    "queue_time": {
        "description": "Время ожидания в очереди",
        "target": "< 1 min",
        "measurement": "time from trigger to start"
    },
    "recovery_time": {
        "description": "Время до исправления сломанного build",
        "target": "< 30 min",
        "measurement": "time from failure to green"
    }
}
```

### 8.2 CI Dashboard

```yaml
# Пример: сбор метрик в Prometheus
# (Используя GitHub Actions webhook или custom action)

metrics:
  - name: ci_pipeline_duration_seconds
    type: histogram
    labels: [repository, branch, workflow, status]
    
  - name: ci_builds_total
    type: counter
    labels: [repository, branch, status]
    
  - name: ci_test_count
    type: gauge
    labels: [repository, test_type, status]
```

---

## 💡 Key Takeaways

- **CI = частая интеграция + автоматическая проверка**: Каждый commit проверяется автоматически

- **Trunk-based development**: Короткоживущие ветки, частые merge в main

- **Быстрый feedback**: Pipeline должен завершаться за 10-15 минут

- **Test pyramid**: Много unit тестов, меньше integration, мало E2E

- **Build once, deploy many**: Один artifact для всех environments

---

## 🚀 Next Steps

**Related Modules:**

- [05_CD](../05_CD/) — Continuous Delivery и Deployment
- [06_IaC](../06_IaC/) — Infrastructure as Code
- [14_DevSecOps](../14_DevSecOps/) — Безопасность в CI/CD

**Practice Ideas:**

1. Настройте CI pipeline для своего проекта
2. Добавьте параллельное выполнение тестов
3. Настройте branch protection rules
4. Измерьте и оптимизируйте время pipeline

**Going Deeper:**

- "Continuous Integration" by Paul Duvall
- GitHub Actions documentation
- Martin Fowler's CI article

---

## 📚 Additional Resources

**Documentation:**

- [GitHub Actions](https://docs.github.com/en/actions)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)

**Books:**

- "Continuous Integration" by Paul Duvall
- "Continuous Delivery" by Jez Humble

**Articles:**

- [Martin Fowler: Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)

---





