# CI/CD в облаке

---

## 📋 Prerequisites

- Понимание Git
- Базовые знания DevOps
- Знакомство с контейнерами

---

## 🎯 Learning Objectives

- Понимать CI/CD pipeline
- Использовать AWS CI/CD сервисы
- Настраивать CodePipeline и CodeBuild
- Применять deployment strategies

---

## 1. CI/CD Концепции

### 1.1 Pipeline

```
┌────────────────────────────────────────────────────────────────────┐
│              CI/CD Pipeline                                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SOURCE          BUILD           TEST           DEPLOY             │
│  ──────          ─────           ────           ──────             │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │ Git     │───►│ Compile │───►│ Unit    │───►│ Staging │        │
│  │ push    │    │ Package │    │ tests   │    │         │        │
│  └─────────┘    │ Docker  │    │ Lint    │    └────┬────┘        │
│                 └─────────┘    │ SAST    │         │              │
│                                └─────────┘         │              │
│                                                    ▼              │
│                                              ┌─────────┐          │
│                                              │ Manual  │          │
│                                              │Approval │          │
│                                              └────┬────┘          │
│                                                   │               │
│                                                   ▼               │
│                                              ┌─────────┐          │
│                                              │ Prod    │          │
│                                              │ Deploy  │          │
│                                              └─────────┘          │
│                                                                     │
│  CI (Continuous Integration): Build → Test (automated)            │
│  CD (Continuous Delivery): Deploy to staging (automated)          │
│  CD (Continuous Deployment): Deploy to prod (automated, optional) │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 AWS CI/CD Services

```python
aws_cicd_services = {
    "CodeCommit": "Git repositories (being deprecated)",
    "CodeBuild": "Build and test code",
    "CodeDeploy": "Deploy to EC2, Lambda, ECS",
    "CodePipeline": "Orchestrate CI/CD pipeline",
    "CodeArtifact": "Package repository (npm, pip, maven)"
}

# Alternatives
third_party = {
    "Source": "GitHub, GitLab, Bitbucket",
    "Build": "GitHub Actions, GitLab CI, Jenkins",
    "Deploy": "ArgoCD, Flux (GitOps)"
}

print("AWS CI/CD Services:")
for service, description in aws_cicd_services.items():
    print(f"  • {service}: {description}")
```

---

## 2. AWS CodeBuild

### 2.1 buildspec.yml

```yaml
version: 0.2

env:
  variables:
    ENV: production
  parameter-store:
    DB_PASSWORD: /myapp/db-password
  secrets-manager:
    API_KEY: myapp/api-key

phases:
  install:
    runtime-versions:
      python: 3.11
    commands:
      - pip install -r requirements.txt
  
  pre_build:
    commands:
      - echo "Running pre-build steps..."
      - aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO
  
  build:
    commands:
      - echo "Building..."
      - python -m pytest tests/
      - docker build -t $ECR_REPO:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - docker push $ECR_REPO:$CODEBUILD_RESOLVED_SOURCE_VERSION
  
  post_build:
    commands:
      - echo "Build completed on $(date)"
      - printf '[{"name":"app","imageUri":"%s"}]' $ECR_REPO:$CODEBUILD_RESOLVED_SOURCE_VERSION > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json
    - appspec.yml
    - taskdef.json
  discard-paths: yes

cache:
  paths:
    - '/root/.cache/pip/**/*'
```

### 2.2 CodeBuild Project

```bash
aws codebuild create-project \
    --name my-build-project \
    --source type=GITHUB,location=https://github.com/user/repo \
    --environment type=LINUX_CONTAINER,computeType=BUILD_GENERAL1_SMALL,image=aws/codebuild/amazonlinux2-x86_64-standard:5.0,privilegedMode=true \
    --service-role arn:aws:iam::123456789012:role/codebuild-role \
    --artifacts type=S3,location=my-artifacts-bucket
```

---

## 3. AWS CodePipeline

### 3.1 Pipeline Structure

```yaml
# pipeline.yaml (CloudFormation)
Resources:
  Pipeline:
    Type: AWS::CodePipeline::Pipeline
    Properties:
      Name: my-app-pipeline
      RoleArn: !GetAtt PipelineRole.Arn
      
      Stages:
        - Name: Source
          Actions:
            - Name: GitHubSource
              ActionTypeId:
                Category: Source
                Owner: ThirdParty
                Provider: GitHub
                Version: '1'
              Configuration:
                Owner: my-org
                Repo: my-repo
                Branch: main
                OAuthToken: '{{resolve:secretsmanager:github-token}}'
              OutputArtifacts:
                - Name: SourceOutput
        
        - Name: Build
          Actions:
            - Name: CodeBuild
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: '1'
              Configuration:
                ProjectName: !Ref BuildProject
              InputArtifacts:
                - Name: SourceOutput
              OutputArtifacts:
                - Name: BuildOutput
        
        - Name: DeployStaging
          Actions:
            - Name: DeployECS
              ActionTypeId:
                Category: Deploy
                Owner: AWS
                Provider: ECS
                Version: '1'
              Configuration:
                ClusterName: staging-cluster
                ServiceName: my-service
              InputArtifacts:
                - Name: BuildOutput
        
        - Name: Approval
          Actions:
            - Name: ManualApproval
              ActionTypeId:
                Category: Approval
                Owner: AWS
                Provider: Manual
                Version: '1'
              Configuration:
                NotificationArn: !Ref ApprovalSNSTopic
        
        - Name: DeployProd
          Actions:
            - Name: DeployECS
              ActionTypeId:
                Category: Deploy
                Owner: AWS
                Provider: ECS
                Version: '1'
              Configuration:
                ClusterName: prod-cluster
                ServiceName: my-service
              InputArtifacts:
                - Name: BuildOutput
```

---

## 4. Deployment Strategies

### 4.1 Стратегии

```
┌────────────────────────────────────────────────────────────────────┐
│              Deployment Strategies                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ROLLING                                                           │
│  ───────                                                           │
│  [v1][v1][v1][v1] → [v2][v1][v1][v1] → [v2][v2][v1][v1] → [v2]x4  │
│  • Replace instances one by one                                   │
│  • Zero downtime                                                  │
│  • Mixed versions during rollout                                  │
│                                                                     │
│  BLUE/GREEN                                                        │
│  ──────────                                                        │
│  [BLUE: v1] ──── switch ────► [GREEN: v2]                         │
│  • Run two environments                                           │
│  • Instant rollback                                               │
│  • Higher cost (2x resources briefly)                             │
│                                                                     │
│  CANARY                                                            │
│  ──────                                                            │
│  [v1: 90%] [v2: 10%] → [v1: 50%] [v2: 50%] → [v2: 100%]          │
│  • Gradual traffic shift                                          │
│  • Monitor metrics between shifts                                  │
│  • Automatic rollback on errors                                   │
│                                                                     │
│  ALL-AT-ONCE                                                       │
│  ───────────                                                       │
│  [v1][v1][v1][v1] → [v2][v2][v2][v2]                              │
│  • Fastest, but risky                                             │
│  • Downtime during deploy                                         │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### 4.2 ECS Blue/Green with CodeDeploy

```yaml
# appspec.yml for ECS
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:us-east-1:123456789012:task-definition/my-task:1"
        LoadBalancerInfo:
          ContainerName: "web"
          ContainerPort: 8080
        PlatformVersion: "LATEST"

Hooks:
  - BeforeInstall: "LambdaFunctionToValidateBeforeInstall"
  - AfterInstall: "LambdaFunctionToValidateAfterInstall"
  - AfterAllowTestTraffic: "LambdaFunctionToValidateAfterTestTrafficStarts"
  - BeforeAllowTraffic: "LambdaFunctionToValidateBeforeAllowingProductionTraffic"
  - AfterAllowTraffic: "LambdaFunctionToValidateAfterAllowingProductionTraffic"
```

---

## 5. GitHub Actions для AWS

```yaml
# .github/workflows/deploy.yml
name: Deploy to AWS

on:
  push:
    branches: [main]

env:
  AWS_REGION: us-east-1
  ECR_REPOSITORY: my-app
  ECS_SERVICE: my-service
  ECS_CLUSTER: my-cluster

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2
      
      - name: Build, tag, and push image to Amazon ECR
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
      
      - name: Deploy to ECS
        uses: aws-actions/amazon-ecs-deploy-task-definition@v1
        with:
          task-definition: task-definition.json
          service: ${{ env.ECS_SERVICE }}
          cluster: ${{ env.ECS_CLUSTER }}
          wait-for-service-stability: true
```

---

## 6. Best Practices

```python
cicd_best_practices = [
    "Fast feedback: keep builds under 10 minutes",
    "Run tests in parallel",
    "Use caching (dependencies, Docker layers)",
    "Immutable artifacts (tagged Docker images)",
    "Environment parity (same infra for all envs)",
    "Automated rollback on failures",
    "Monitor deployments (metrics, alerts)",
    "Use feature flags for risky changes",
    "Trunk-based development (short-lived branches)",
    "Security scanning in pipeline (SAST, DAST, SCA)"
]

print("CI/CD Best Practices:")
for i, practice in enumerate(cicd_best_practices, 1):
    print(f"  {i}. {practice}")
```

---

## 💡 Key Takeaways

- **CI** — автоматический build и test при каждом commit
- **CD** — автоматический deploy до staging/prod
- **CodeBuild** — managed build service
- **CodePipeline** — orchestration of CI/CD stages
- **Blue/Green** — instant rollback, higher cost
- **Canary** — gradual rollout with monitoring

---

## 📚 Additional Resources

- [CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/)
- [CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/)
- [GitHub Actions for AWS](https://github.com/aws-actions)

---
