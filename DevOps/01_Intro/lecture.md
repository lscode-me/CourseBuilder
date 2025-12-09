# Введение в DevOps
## История, философия и культура современных операций

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь опыт разработки (понимать цикл разработки ПО)
- Понимать базовые концепции системного администрирования
- Знать основы работы с Git и системами контроля версий

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить, что такое DevOps и чем он отличается от традиционных подходов
- Описать историю возникновения DevOps движения
- Применять модель CALMS для оценки DevOps зрелости
- Различать DevOps и SRE как дисциплины
- Идентифицировать ключевые принципы и практики DevOps

---

## 1. Что такое DevOps?

DevOps — это не инструмент, не должность и не отдел. DevOps — это **культура, набор практик и философия**, направленная на улучшение сотрудничества между командами разработки (Development) и эксплуатации (Operations).

### 1.1 Проблема, которую решает DevOps

Традиционно в IT-организациях существовало чёткое разделение:

**Development (Dev):**
- Пишут код
- Хотят быстрее выпускать новые фичи
- Измеряются скоростью разработки
- Цель: изменения

**Operations (Ops):**
- Поддерживают инфраструктуру
- Хотят стабильности
- Измеряются uptime и надёжностью
- Цель: стабильность

Это создаёт **конфликт интересов**: Dev хочет частых релизов, Ops хочет минимума изменений. Результат — «стена» между командами:

```
┌─────────────────────────────────────────────────────────────┐
│                    Традиционная модель                       │
├─────────────────────────┬───────────────────────────────────┤
│       Development       │           Operations              │
├─────────────────────────┼───────────────────────────────────┤
│ "Код работает на моей   │ "Мы не можем деплоить так        │
│  машине!"               │  часто — система нестабильна"    │
├─────────────────────────┼───────────────────────────────────┤
│ "Почему деплой занимает │ "Мы ждём approval от security,   │
│  3 недели?"             │  compliance, change management"  │
├─────────────────────────┼───────────────────────────────────┤
│ Цель: скорость          │ Цель: стабильность               │
└─────────────────────────┴───────────────────────────────────┘
                          │
                    "The Wall"
```

### 1.2 DevOps как мост

DevOps разрушает эту стену через:

1. **Общие цели** — обе команды отвечают за доставку ценности клиенту
2. **Общие инструменты** — единая цепочка от кода до продакшена
3. **Общую ответственность** — "You build it, you run it"
4. **Общие метрики** — все измеряются по бизнес-результатам

**Определение от Gene Kim (автор "The Phoenix Project"):**

> DevOps — это набор технических практик, культурных норм и архитектурных подходов, которые позволяют быстро и безопасно разрабатывать, тестировать и выпускать программное обеспечение.

---

## 2. История DevOps

### 2.1 Предпосылки (2000-2008)

**Agile Manifesto (2001):**
- Революция в разработке
- Короткие итерации, быстрая обратная связь
- Но... Agile остановился на границе с Operations

**Lean Manufacturing:**
- Принципы Toyota Production System
- Устранение waste, непрерывное улучшение
- Mary и Tom Poppendieck адаптировали для IT

**Web 2.0 компании:**
- Flickr, Google, Amazon — деплоили по 10+ раз в день
- Нужны были новые подходы к операциям

### 2.2 Рождение DevOps (2008-2009)

**Velocity Conference 2009:**

John Allspaw и Paul Hammond из Flickr представили доклад **"10+ Deploys Per Day: Dev and Ops Cooperation at Flickr"**. Это был переломный момент.

Ключевые идеи:

- Автоматизация инфраструктуры
- Shared version control
- One step build and deploy
- Feature flags
- Shared metrics
- IRC and IM robots (ChatOps)

**DevOpsDays Ghent 2009:**

Patrick Debois (разочарованный консультант) организовал первую конференцию DevOpsDays в Бельгии. Хэштег **#DevOps** в Twitter — так родился термин.

### 2.3 Развитие (2010-2015)

- **2010:** "Continuous Delivery" by Jez Humble — библия CD
- **2011:** "The Phoenix Project" by Gene Kim — DevOps для менеджеров
- **2013:** Docker — контейнеры становятся мейнстримом
- **2014:** Kubernetes — оркестрация контейнеров
- **2015:** "DevOps Handbook" — практическое руководство

### 2.4 Зрелость (2016-настоящее время)

- **SRE книга от Google (2016)** — формализация практик
- **DORA metrics** — научный подход к измерению DevOps
- **GitOps (2017)** — декларативная инфраструктура
- **Platform Engineering (2022+)** — следующая эволюция

---

## 3. The Three Ways — философия DevOps

Gene Kim в "The Phoenix Project" сформулировал **Три Пути** — философские принципы DevOps:

### 3.1 The First Way: Flow (Systems Thinking)

**Принцип:** Оптимизируй поток работы слева направо (от Dev к Ops к клиенту).

```
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│ Dev  │───▶│Build │───▶│ Test │───▶│Deploy│───▶│Client│
└──────┘    └──────┘    └──────┘    └──────┘    └──────┘
            ───────────────────────────────────────────▶
                        Поток (Flow)
```

**Практики First Way:**
- Визуализация работы (Kanban board)
- Ограничение Work in Progress (WIP)
- Уменьшение размера batch
- Автоматизация повторяющихся задач
- Устранение bottlenecks

**Пример:**

```python
# Плохо: большой монолитный релиз раз в квартал
releases_per_year = 4
avg_changes_per_release = 500
risk_per_release = "HIGH"  # Много изменений = много рисков

# Хорошо: маленькие частые релизы
releases_per_year = 365  # Каждый день
avg_changes_per_release = 5
risk_per_release = "LOW"  # Мало изменений = легко откатить
```

### 3.2 The Second Way: Feedback (Amplify Feedback Loops)

**Принцип:** Создай и усиль петли обратной связи справа налево.

```
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│ Dev  │◀───│Build │◀───│ Test │◀───│Deploy│◀───│Client│
└──────┘    └──────┘    └──────┘    └──────┘    └──────┘
◀──────────────────────────────────────────────────────
                    Feedback Loop
```

**Практики Second Way:**
- Мониторинг и алертинг
- A/B тестирование
- Автоматические тесты
- Code review
- Postmortems без blame

**Пример: быстрая обратная связь в CI/CD:**

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run tests
        run: pytest --cov=app tests/
      
      - name: Lint
        run: ruff check .
      
      - name: Type check
        run: mypy app/
        
      # Feedback: результаты через 2-3 минуты после push
```

### 3.3 The Third Way: Continuous Learning

**Принцип:** Создай культуру экспериментирования и обучения.

**Практики Third Way:**
- Выделяй время на эксперименты (20% time)
- Делись знаниями (tech talks, документация)
- Blameless postmortems
- Game days / Chaos engineering
- Failure is a learning opportunity

**Пример: культура экспериментов**

```python
# Feature flags для безопасных экспериментов
from feature_flags import FeatureFlags

ff = FeatureFlags()

def get_recommendations(user_id: int) -> list:
    if ff.is_enabled("new_recommendation_algorithm", user_id):
        # Новый алгоритм — тестируем на 5% пользователей
        return new_ml_recommendations(user_id)
    else:
        # Старый проверенный алгоритм
        return legacy_recommendations(user_id)
```

---

## 4. CALMS Framework

CALMS — это акроним, описывающий ключевые аспекты DevOps культуры:

### 4.1 Culture (Культура)

**Что это:** Общие ценности, доверие, сотрудничество между командами.

**Признаки здоровой культуры:**
- Dev и Ops работают в одной команде
- Общие on-call rotation
- Blameless postmortems
- Психологическая безопасность

**Anti-pattern:**
```
❌ "Это не мой код — я только деплою"
❌ "Operations не понимают наш код"
❌ "Developers не думают о production"
```

**Pattern:**
```
✅ "Мы вместе отвечаем за этот сервис"
✅ "Давайте разберёмся, как это предотвратить"
✅ "Что мы можем автоматизировать?"
```

### 4.2 Automation (Автоматизация)

**Что это:** Автоматизация всего, что может быть автоматизировано.

**Области автоматизации:**
- Build и packaging
- Testing (unit, integration, e2e)
- Deployment
- Infrastructure provisioning
- Monitoring и alerting
- Incident response

**Пример: автоматизация создания инфраструктуры**

```hcl
# Terraform: декларативное описание инфраструктуры
resource "aws_instance" "web" {
  count         = var.web_instance_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.medium"
  
  tags = {
    Name        = "web-${count.index}"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# Вместо ручного создания через консоль:
# 1. Открыть AWS Console
# 2. Выбрать EC2
# 3. Нажать Launch Instance
# 4. Выбрать AMI... и т.д.
```

### 4.3 Lean (Бережливость)

**Что это:** Принципы Lean manufacturing, адаптированные для IT.

**Ключевые концепции:**
- **Eliminate waste** — убрать всё, что не добавляет ценности
- **Small batches** — маленькие порции работы
- **Continuous improvement** — постоянное улучшение (Kaizen)
- **Pull system** — работа "вытягивается" по необходимости

**Типы waste в IT:**

| Waste | Пример |
|-------|--------|
| Частично сделанная работа | Фичи в ветках, которые не мержатся неделями |
| Extra features | "Золотое покрытие" — фичи, которые никто не просил |
| Relearning | Потеря знаний при уходе сотрудника |
| Handoffs | Передача задачи от Dev к QA к Ops |
| Delays | Ожидание code review, approval, ресурсов |
| Task switching | Постоянное переключение между задачами |
| Defects | Баги, найденные в production |

### 4.4 Measurement (Измерение)

**Что это:** Принятие решений на основе данных, а не интуиции.

**Что измерять:**
- Deployment frequency
- Lead time for changes
- Change failure rate
- Mean time to recovery (MTTR)
- Service availability
- Customer satisfaction

**Пример: дашборд DevOps метрик**

```python
# Сбор метрик deployment frequency
from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class Deployment:
    timestamp: datetime
    service: str
    environment: str
    success: bool
    
def calculate_deployment_frequency(
    deployments: list[Deployment],
    period_days: int = 30
) -> dict:
    """Calculate deployment frequency metrics."""
    cutoff = datetime.now() - timedelta(days=period_days)
    recent = [d for d in deployments if d.timestamp > cutoff]
    
    total = len(recent)
    successful = len([d for d in recent if d.success])
    
    return {
        "total_deployments": total,
        "successful_deployments": successful,
        "success_rate": successful / total if total > 0 else 0,
        "deployments_per_day": total / period_days,
        "period_days": period_days
    }
```

### 4.5 Sharing (Обмен знаниями)

**Что это:** Открытость, прозрачность, обмен знаниями и опытом.

**Практики sharing:**
- Internal tech talks
- Runbooks и документация
- Postmortem reviews
- Cross-team rotations
- Open source внутри компании (InnerSource)
- ChatOps — прозрачные операции в публичных каналах

**Пример: публичный postmortem**

```markdown
# Incident Postmortem: API Outage 2024-01-15

## Summary
API service was unavailable for 47 minutes due to database 
connection pool exhaustion.

## Timeline
- 14:32 - Alert fired: API error rate > 5%
- 14:35 - On-call engineer acknowledged
- 14:42 - Root cause identified: connection pool exhausted
- 14:55 - Mitigation applied: increased pool size
- 15:19 - Service fully recovered

## Root Cause
A slow query (introduced in deploy #4521) caused connections 
to be held longer than expected, exhausting the pool.

## Action Items
- [ ] Add query performance tests to CI
- [ ] Implement connection pool monitoring
- [ ] Add circuit breaker for database calls

## Lessons Learned
We need better visibility into database connection usage.
```

---

## 5. DevOps vs SRE

### 5.1 Site Reliability Engineering

SRE (Site Reliability Engineering) — это подход Google к операциям, описанный в книге "Site Reliability Engineering" (2016).

**Определение от Ben Treynor (создатель SRE в Google):**

> SRE is what happens when you ask a software engineer to design an operations team.

### 5.2 Сравнение

| Аспект | DevOps | SRE |
|--------|--------|-----|
| Происхождение | Сообщество (2009) | Google (2003) |
| Фокус | Культура и collaboration | Надёжность и engineering |
| Подход | Философия и практики | Конкретные методы и метрики |
| Метрики | DORA metrics | SLI/SLO/SLA |
| Автоматизация | Автоматизируй всё | Eliminate toil |
| On-call | Общая ответственность | Structured rotation |
| Error budget | Концептуально | Формализовано |

### 5.3 Как они соотносятся?

Google говорит: **"class SRE implements DevOps"**

```python
# Концептуально SRE — это конкретная реализация DevOps
class DevOps:
    """Abstract philosophy and culture."""
    
    def automate(self): 
        raise NotImplementedError
    
    def measure(self): 
        raise NotImplementedError
    
    def collaborate(self): 
        raise NotImplementedError


class SRE(DevOps):
    """Concrete implementation with specific practices."""
    
    def __init__(self):
        self.error_budget = ErrorBudget()
        self.slo = ServiceLevelObjective()
        self.toil_budget = 0.5  # Max 50% time on toil
    
    def automate(self):
        """Eliminate toil through software engineering."""
        return self.eliminate_toil()
    
    def measure(self):
        """Use SLIs, SLOs, and error budgets."""
        return self.slo.measure()
    
    def collaborate(self):
        """Shared ownership with dev teams."""
        return self.embed_with_dev_teams()
```

### 5.4 Когда что использовать?

**DevOps подходит когда:**
- Нужно улучшить collaboration между Dev и Ops
- Организация начинает трансформацию
- Фокус на culture change

**SRE подходит когда:**
- Нужны конкретные метрики надёжности
- Есть ресурсы на dedicated SRE team
- Требуется формализованный подход к reliability

**На практике:** большинство организаций используют элементы обоих подходов.

---

## 6. DevOps Anti-patterns

### 6.1 "DevOps Engineer" как роль

**Проблема:** Создание отдельной должности "DevOps Engineer" между Dev и Ops.

```
❌ Анти-паттерн:
Dev ──▶ DevOps Engineer ──▶ Ops
        (новая стена)
```

**Почему это плохо:**
- Создаёт новый silo вместо устранения старых
- DevOps становится чужой ответственностью
- Dev и Ops всё ещё не взаимодействуют

**Правильный подход:**
```
✅ Паттерн:
Dev + Ops = Одна команда с общей ответственностью
```

### 6.2 "Мы внедрили DevOps — купили Jenkins"

**Проблема:** Думать, что DevOps — это инструменты.

```python
# Это НЕ DevOps
tools = ["Jenkins", "Docker", "Kubernetes", "Terraform"]
devops_implemented = all(tool in our_stack for tool in tools)
# devops_implemented == True, но культура не изменилась

# Это DevOps
culture_changes = [
    "shared_responsibility",
    "blameless_postmortems",
    "continuous_learning",
    "fast_feedback"
]
devops_implemented = all(
    change in our_culture for change in culture_changes
)
```

### 6.3 "DevOps — это только автоматизация"

**Проблема:** Фокус только на технической автоматизации без культурных изменений.

**Симптомы:**
- Автоматизированный CI/CD, но команды всё ещё враждуют
- Тесты есть, но их игнорируют при срочных релизах
- Infrastructure as Code, но никто не делает code review

### 6.4 "NoOps — Operations больше не нужен"

**Проблема:** Мышление, что cloud и автоматизация полностью заменят Ops.

**Реальность:**
- Serverless всё ещё требует операционной экспертизы
- Cloud ≠ автоматическая надёжность
- Кто-то должен понимать инфраструктуру

---

## 7. DevOps в организации

### 7.1 Модели внедрения

**Модель 1: Embedded DevOps**
```
┌────────────────────────────────────────┐
│              Product Team              │
├──────────┬──────────┬─────────────────┤
│   Dev    │    QA    │   Ops/DevOps    │
│ (5 eng)  │ (1 eng)  │    (1 eng)      │
└──────────┴──────────┴─────────────────┘
```
- DevOps/Ops engineer встроен в каждую команду
- Полная автономия команды
- Подходит для организаций с сильной инженерной культурой

**Модель 2: Platform Team**
```
┌────────────────────────────────────────┐
│           Platform Team                │
│  (CI/CD, IaC, Monitoring, Security)   │
└───────────────────┬────────────────────┘
                    │ provides platform
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ Team A  │ │ Team B  │ │ Team C  │
   │ (Dev)   │ │ (Dev)   │ │ (Dev)   │
   └─────────┘ └─────────┘ └─────────┘
```
- Централизованная команда создаёт инструменты
- Product команды используют платформу
- Снижает cognitive load на dev teams

**Модель 3: SRE Team**
```
┌────────────────────────────────────────┐
│              SRE Team                  │
│    (Reliability, Scalability)          │
└───────────────────┬────────────────────┘
                    │ consults & embeds
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ Team A  │ │ Team B  │ │ Team C  │
   │ (Dev)   │ │ (Dev)   │ │ (Dev)   │
   └─────────┘ └─────────┘ └─────────┘
```
- SRE поддерживает критичные сервисы
- Консультирует dev teams по надёжности
- Модель Google

### 7.2 Зрелость DevOps

**Level 0: Ad-hoc**
- Ручные деплои
- Нет version control для инфраструктуры
- Silos между командами

**Level 1: Beginning**
- Базовый CI
- Частично автоматизированные деплои
- Начало collaboration

**Level 2: Intermediate**
- CI/CD для большинства сервисов
- Infrastructure as Code
- Мониторинг и алертинг

**Level 3: Advanced**
- Fully automated deployment pipeline
- Self-service инфраструктура
- Blameless culture
- Измерение DORA metrics

**Level 4: Elite**
- On-demand deployment
- Chaos engineering
- ML/AI для операций (AIOps)
- Continuous improvement culture

---

## 8. Бизнес-ценность DevOps

### 8.1 Исследование DORA

DORA (DevOps Research and Assessment) провела многолетнее исследование, которое показало корреляцию между DevOps практиками и бизнес-результатами.

**Ключевые метрики (DORA Four Keys):**

| Метрика | Elite | High | Medium | Low |
|---------|-------|------|--------|-----|
| Deployment frequency | On-demand | Daily-Weekly | Weekly-Monthly | Monthly-Yearly |
| Lead time for changes | < 1 hour | 1 day - 1 week | 1 week - 1 month | 1-6 months |
| Change failure rate | 0-15% | 16-30% | 16-30% | 16-30% |
| MTTR | < 1 hour | < 1 day | 1 day - 1 week | 1 week - 1 month |

### 8.2 ROI от DevOps

**Исследование показало, что Elite performers:**
- Деплоят в **208 раз чаще**
- Lead time в **106 раз короче**
- MTTR в **2604 раза быстрее**
- Change failure rate **7 раз ниже**

**Бизнес-результаты:**
- На **50%** больше вероятность превысить цели по прибыли
- На **2x** больше вероятность превысить цели по market share
- На **2x** выше продуктивность разработчиков

### 8.3 Как измерить прогресс

```python
# Пример расчёта DevOps ROI
from dataclasses import dataclass
from datetime import timedelta

@dataclass
class DevOpsMetrics:
    deployment_frequency_per_week: float
    lead_time: timedelta
    change_failure_rate: float
    mttr: timedelta
    
    def calculate_improvement(self, before: 'DevOpsMetrics') -> dict:
        return {
            "deployment_frequency_improvement": 
                self.deployment_frequency_per_week / before.deployment_frequency_per_week,
            "lead_time_improvement": 
                before.lead_time / self.lead_time,
            "failure_rate_improvement": 
                before.change_failure_rate / self.change_failure_rate,
            "mttr_improvement": 
                before.mttr / self.mttr
        }

# До внедрения DevOps
before = DevOpsMetrics(
    deployment_frequency_per_week=0.25,  # Раз в месяц
    lead_time=timedelta(days=90),
    change_failure_rate=0.30,
    mttr=timedelta(days=7)
)

# После внедрения DevOps
after = DevOpsMetrics(
    deployment_frequency_per_week=7,  # Ежедневно
    lead_time=timedelta(hours=4),
    change_failure_rate=0.05,
    mttr=timedelta(hours=1)
)

improvement = after.calculate_improvement(before)
print(f"Deployment frequency: {improvement['deployment_frequency_improvement']:.0f}x")
print(f"Lead time: {improvement['lead_time_improvement']:.0f}x faster")
print(f"Failure rate: {improvement['failure_rate_improvement']:.0f}x lower")
print(f"MTTR: {improvement['mttr_improvement']:.0f}x faster")
```

**Output:**
```
Deployment frequency: 28x
Lead time: 540x faster
Failure rate: 6x lower
MTTR: 168x faster
```

---

## 9. С чего начать?

### 9.1 Quick Wins

**Неделя 1-2: Visibility**
- Настроить базовый мониторинг
- Создать дашборд с ключевыми метриками
- Начать измерять deployment frequency

**Неделя 3-4: Version Control Everything**
- Инфраструктура в Git
- Конфигурация в Git
- Документация в Git

**Месяц 2: Basic Automation**
- Автоматизировать build
- Автоматизировать тесты
- Автоматизировать деплой на staging

**Месяц 3-6: Culture**
- Ввести blameless postmortems
- Начать cross-team collaboration
- Измерять и улучшать DORA metrics

### 9.2 Roadmap зрелости

```
      ┌─────────────────────────────────────────────────────┐
      │                  DevOps Roadmap                     │
      └─────────────────────────────────────────────────────┘
      
Q1    ┌──────────────────────────────────────────────────────
      │ • Version control для кода и конфигов
      │ • Базовый CI (build + test)
      │ • Мониторинг production
      └──────────────────────────────────────────────────────

Q2    ┌──────────────────────────────────────────────────────
      │ • Автоматический deployment на staging
      │ • Infrastructure as Code (базовый)
      │ • Алертинг и on-call процесс
      └──────────────────────────────────────────────────────

Q3    ┌──────────────────────────────────────────────────────
      │ • Continuous Deployment на production
      │ • Feature flags
      │ • Централизованное логирование
      └──────────────────────────────────────────────────────

Q4    ┌──────────────────────────────────────────────────────
      │ • SLI/SLO определены для сервисов
      │ • Chaos engineering эксперименты
      │ • Self-service платформа для разработчиков
      └──────────────────────────────────────────────────────
```

---

## 💡 Key Takeaways

- **DevOps — это культура, не инструменты**: Технологии важны, но без культурных изменений DevOps не работает

- **Three Ways**: Flow (оптимизация потока), Feedback (быстрая обратная связь), Continuous Learning (культура экспериментов)

- **CALMS**: Culture, Automation, Lean, Measurement, Sharing — основа DevOps практик

- **DevOps и SRE дополняют друг друга**: SRE — конкретная реализация DevOps с фокусом на надёжность

- **Измеримые результаты**: DORA metrics показывают, что elite performers значительно превосходят остальных

---

## 🚀 Next Steps

**Related Modules:**
- [02_Methodologies](../02_Methodologies/) — Agile, Scrum, Kanban и их роль в DevOps
- [04_CI](../04_CI/) — Continuous Integration на практике
- [10_SRE](../10_SRE/) — Глубокое погружение в Site Reliability Engineering

**Practice Ideas:**
1. Оцените текущую зрелость вашей организации по CALMS
2. Измерьте текущие DORA metrics для вашей команды
3. Проведите первый blameless postmortem

**Going Deeper:**
- "The Phoenix Project" — начните с этой книги
- Посмотрите "10+ Deploys Per Day" доклад (YouTube)
- Изучите State of DevOps Report от DORA

---

## 📚 Additional Resources

**Books:**
- "The Phoenix Project" by Gene Kim — бизнес-роман о DevOps
- "The DevOps Handbook" by Gene Kim et al. — практическое руководство
- "Accelerate" by Nicole Forsgren — научный подход к DevOps

**Articles & Reports:**
- [State of DevOps Report](https://dora.dev) — ежегодное исследование
- [Google SRE Books](https://sre.google/books/) — бесплатные книги от Google

**Videos:**
- [10+ Deploys Per Day: Dev and Ops Cooperation at Flickr](https://www.youtube.com/watch?v=LdOe18KhtT4) — исторический доклад
- [The Short History of DevOps](https://www.youtube.com/watch?v=o7-IuYS0iSE) — краткая история

**Communities:**
- [DevOpsDays](https://devopsdays.org/) — конференции по всему миру
- [SRE Weekly](https://sreweekly.com/) — еженедельная рассылка

---

