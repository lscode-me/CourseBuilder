# Основы сервисного менеджмента
## ITSM, ITIL и ключевые процессы управления IT-услугами

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать роль Customer & Services в IT-компании ([01_Intro](../01_Intro/))
- Знать базовые понятия: клиент, сервис, SLA
- Иметь опыт работы в IT-команде

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять концепции услуги и сервисной модели
- Применять базовые принципы ITIL в ежедневной работе
- Управлять инцидентами, проблемами и изменениями
- Формировать и контролировать SLA и OLA
- Использовать RACI-матрицу для распределения ответственности
- Правильно проводить эскалации (operational и executive)

---

## 1. Что такое услуга и сервис

### 1.1 Определение услуги

**Услуга (Service)** — способ предоставления ценности клиенту путём содействия в достижении его целей, без необходимости для клиента управлять специфическими затратами и рисками.

**Простыми словами:** Клиент получает результат, не вникая в то, как он достигается.

**Пример:**
```
Клиент хочет: Мобильное приложение для своих пользователей

Что клиент НЕ хочет делать:
- Нанимать и обучать разработчиков
- Покупать инфраструктуру
- Управлять процессом разработки
- Нести риски найма неподходящих специалистов

Что мы предоставляем как услугу:
- Готовую команду с нужными компетенциями
- Налаженные процессы разработки
- Инфраструктуру и инструменты
- Гарантии качества (SLA)
```

### 1.2 Сервисная модель

**Сервисная модель** описывает, как организована поставка услуг:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         СЕРВИСНАЯ МОДЕЛЬ                                │
└─────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│  SERVICE PROVIDER (Мы)                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │   People    │  │  Processes  │  │ Technology  │  │  Partners   │    │
│  │  (Команда)  │  │  (ITSM)     │  │ (Tools)     │  │ (Vendors)   │    │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘    │
└────────────────────────────────────────────────────────────────────────┘
                                │
                                │ SERVICE DELIVERY
                                ▼
┌────────────────────────────────────────────────────────────────────────┐
│  SERVICES                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐         │
│  │ Development     │  │ QA & Testing    │  │ DevOps          │         │
│  │ Team            │  │ Services        │  │ Support         │         │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘         │
└────────────────────────────────────────────────────────────────────────┘
                                │
                                │ VALUE
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  SERVICE CONSUMER (Клиент)                                              │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │  Business Outcomes: Быстрее выходить на рынок, снижать риски      │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Компоненты услуги

| Компонент | Описание | Пример |
|-----------|----------|--------|
| **Utility** (Полезность) | Что услуга делает | Разработка мобильного приложения |
| **Warranty** (Гарантия) | Как хорошо услуга это делает | SLA, качество, доступность |
| **Experience** (Опыт) | Как клиент воспринимает услугу | Коммуникация, удобство, отношения |

**Value = Utility + Warranty + Experience**

---

## 2. Введение в ITIL

### 2.1 Что такое ITIL

**ITIL (Information Technology Infrastructure Library)** — набор лучших практик управления IT-услугами. Это не стандарт, а framework, который можно адаптировать под нужды организации.

**Краткая история:**

- 1980-е: Создан правительством UK
- 1990-2000-е: ITIL v2 — широкое распространение
- 2007: ITIL v3 — сервисный жизненный цикл
- 2019: ITIL 4 — современный подход, интеграция с Agile/DevOps

### 2.2 ITIL 4: Ключевые концепции

**Четыре измерения управления услугами:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FOUR DIMENSIONS OF SERVICE MANAGEMENT                │
└─────────────────────────────────────────────────────────────────────────┘

                    ┌───────────────────────┐
                    │ Organizations & People│
                    │ (Культура, структура, │
                    │  компетенции)         │
                    └───────────┬───────────┘
                                │
      ┌─────────────────────────┼─────────────────────────┐
      │                         │                         │
      ▼                         ▼                         ▼
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│ Information & │       │    SERVICE    │       │ Partners &    │
│ Technology    │───────│    VALUE      │───────│ Suppliers     │
│ (Данные,      │       │   SYSTEM      │       │ (Вендоры,     │
│ инструменты)  │       │               │       │ партнёры)     │
└───────────────┘       └───────────────┘       └───────────────┘
                                │
                                │
                    ┌───────────┴───────────┐
                    │ Value Streams &       │
                    │ Processes             │
                    │ (Потоки создания      │
                    │  ценности)            │
                    └───────────────────────┘
```

**Service Value System (SVS):**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SERVICE VALUE SYSTEM                                 │
└─────────────────────────────────────────────────────────────────────────┘

  DEMAND                                                           VALUE
     │                                                               ▲
     ▼                                                               │
┌─────────┐     ┌─────────────────────────────────────────────┐     │
│Opportun-│────▶│              SERVICE VALUE CHAIN            │─────┘
│ity/     │     │  Plan → Improve → Engage → Design →               │
│Demand   │     │  → Obtain/Build → Deliver & Support               │
└─────────┘     └─────────────────────────────────────────────      ┘
                                    ▲
                    ┌───────────────┴───────────────────────────────┐
                    │                                               │
            ┌───────────────┐               ┌───────────────┐
            │  GOVERNANCE   │               │   PRACTICES   │
            │  (Политики,   │               │  (ITSM        │
            │   принципы)   │               │   практики)   │
            └───────────────┘               └───────────────┘
                    │                                               │
                    └───────────────┬───────────────────────────────┘
                                    │
                          ┌─────────────────┐
                          │ CONTINUAL       │
                          │ IMPROVEMENT     │
                          │ (Постоянное     │
                          │  улучшение)     │
                          └─────────────────┘
```

### 2.3 Семь руководящих принципов ITIL 4

| Принцип | Описание | Применение |
|---------|----------|------------|
| **Focus on value** | Всё должно создавать ценность для стейкхолдеров | Каждое действие оцениваем: "Какую ценность это приносит клиенту?" |
| **Start where you are** | Не начинать с нуля, использовать существующее | Оценить текущие процессы перед изменениями |
| **Progress iteratively** | Маленькие итерации с обратной связью | Не пытаться внедрить всё сразу |
| **Collaborate** | Работать вместе через границы | Вовлекать клиента, команду, смежные отделы |
| **Think holistically** | Рассматривать систему целиком | Учитывать влияние на все части системы |
| **Keep it simple** | Делать только необходимое | Избегать over-engineering процессов |
| **Optimize & automate** | Автоматизировать после оптимизации | Сначала улучшить процесс, потом автоматизировать |

---

## 3. Основные процессы ITSM

### 3.1 Incident Management

**Инцидент** — незапланированное прерывание услуги или снижение её качества.

**Цель:** Восстановить нормальную работу услуги как можно быстрее, минимизируя влияние на бизнес.

**Жизненный цикл инцидента:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    INCIDENT LIFECYCLE                                   │
└─────────────────────────────────────────────────────────────────────────┘

 ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
 │Identifi-│───▶│  Log &  │───▶│Categori-│───▶│Prioriti-│───▶│ Initial │
 │ cation  │    │ Record  │    │   ze    │    │   ze    │    │Diagnosis│
 └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                                   │
                                                                   ▼
 ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────────────────────┐
 │ Closure │◀───│ Verify  │◀───│Resolution│◀───│ Investigation &        │
 │         │    │         │    │         │    │ Diagnosis / Escalation  │
 └─────────┘    └─────────┘    └─────────┘    └─────────────────────────┘
```

**Приоритизация инцидентов:**

```
Priority = Impact × Urgency

Impact: Масштаб влияния на бизнес
- High: Влияет на весь бизнес или критичную функцию
- Medium: Влияет на часть пользователей
- Low: Влияет на одного пользователя

Urgency: Как быстро нужно решить
- High: Нужно решить немедленно
- Medium: Можно подождать несколько часов
- Low: Можно решить в рабочем порядке
```

**Матрица приоритетов:**

| Impact \ Urgency | High | Medium | Low |
|------------------|------|--------|-----|
| **High** | P1 (Critical) | P2 (High) | P3 (Medium) |
| **Medium** | P2 (High) | P3 (Medium) | P4 (Low) |
| **Low** | P3 (Medium) | P4 (Low) | P4 (Low) |

**Пример записи инцидента:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ INCIDENT RECORD                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ ID: INC-2024-0142                                                       │
│ Title: Mobile app login not working                                     │
│ Status: In Progress                                                     │
│                                                                         │
│ Impact: High (All mobile users affected)                                │
│ Urgency: High (Peak usage time)                                         │
│ Priority: P1 (Critical)                                                 │
│                                                                         │
│ Reported by: Client PM                                                  │
│ Assigned to: Backend Team                                               │
│ Created: 2024-12-10 14:30 UTC                                           │
│ SLA Target: 4 hours (Resolution)                                        │
│                                                                         │
│ Description:                                                            │
│ Users are unable to log in to the mobile application since 14:15.       │
│ Error message: "Authentication service unavailable"                     │
│                                                                         │
│ Updates:                                                                │
│ 14:35 - Assigned to Backend team, initial investigation started         │
│ 14:45 - Identified: Auth service pod crashed due to memory leak         │
│ 14:55 - Workaround applied: Restarted auth service pods                 │
│ 15:00 - Service restored, monitoring for stability                      │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Problem Management

**Проблема** — причина или потенциальная причина одного или нескольких инцидентов.

**Цель:** Минимизировать влияние инцидентов путём выявления и устранения их корневых причин.

**Incident vs Problem:**

| Аспект | Incident | Problem |
|--------|----------|---------|
| Фокус | Восстановить услугу БЫСТРО | Найти и устранить ПРИЧИНУ |
| Временной горизонт | Минуты-часы | Дни-недели |
| Результат | Workaround | Permanent fix |
| Пример | Перезапуск сервиса | Исправление memory leak |

**Жизненный цикл проблемы:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROBLEM LIFECYCLE                                    │
└─────────────────────────────────────────────────────────────────────────┘

  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐
  │  Problem      │    │  Problem      │    │    Root       │
  │  Detection    │───▶│  Logging      │───▶│    Cause      │
  │               │    │               │    │   Analysis    │
  └───────────────┘    └───────────────┘    └───────────────┘
                                                    │
                              ┌─────────────────────┘
                              ▼
                    ┌───────────────────┐
                    │  Known Error      │  ← Workaround задокументирован
                    │  Record           │
                    └─────────┬─────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
     ┌───────────────────┐          ┌───────────────────┐
     │ Change Request    │          │ Problem Closure   │
     │ (Permanent fix)   │          │ (If no fix needed)│
     └───────────────────┘          └───────────────────┘
```

**Root Cause Analysis (RCA) — методы:**

**1. 5 Whys (5 Почему):**
```
Проблема: Сервис авторизации упал

Why 1: Почему сервис упал?
→ Закончилась память

Why 2: Почему закончилась память?
→ Memory leak в новом коде

Why 3: Почему memory leak попал в production?
→ Не было обнаружено на тестировании

Why 4: Почему не обнаружено на тестировании?
→ Load testing не включает длительные тесты

Why 5: Почему нет длительных тестов?
→ Нет процесса soak testing

Root Cause: Отсутствие soak testing в pipeline
Action: Добавить 24-hour soak test перед production
```

**2. Fishbone Diagram (Ishikawa):**
```
                                    ┌─────────────────────┐
                                    │     ПРОБЛЕМА:       │
                                    │   Сервис упал       │
                                    └─────────────────────┘
                                              ▲
                    ┌─────────────────────────┼─────────────────────────────────────────┐
                    │                         │                                         │
            ┌───────┴───────┐         ┌───────┴───────┐         ┌───────┴───────┐
            │    PEOPLE     │         │   PROCESS     │         │  TECHNOLOGY   │
            │               │         │               │         │               │
            │ - Недостаточ- │         │ - Нет soak    │         │ - Memory leak │
            │   ный опыт    │         │   testing     │         │   в коде      │
            │ - Нет code    │         │ - Слабый      │         │ - Нет memory  │
            │   review      │         │   monitoring  │         │   limits      │
            └───────────────┘         └───────────────┘         └───────────────┘
```

### 3.3 Change Management

**Изменение (Change)** — добавление, модификация или удаление чего-либо, что может повлиять на услуги.

**Цель:** Максимизировать успешные изменения, минимизируя риски и негативное влияние на услуги.

**Типы изменений:**

| Тип | Описание | Approval | Пример |
|-----|----------|----------|--------|
| **Standard** | Низкий риск, pre-approved | Автоматический | Обновление minor версии библиотеки |
| **Normal** | Средний риск | CAB (Change Advisory Board) | Новая функциональность |
| **Emergency** | Срочное исправление критической проблемы | Emergency CAB | Hotfix P1 бага в production |

**Change процесс:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CHANGE PROCESS                                       │
└─────────────────────────────────────────────────────────────────────────┘

  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
  │ Request │───▶│ Assess  │───▶│ Approve │───▶│Implement│───▶│  Review │
  │ for     │    │ & Plan  │    │         │    │         │    │ & Close │
  │ Change  │    │         │    │         │    │         │    │         │
  └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
       │              │              │              │                        │
       ▼              ▼              ▼              ▼              ▼
  Описание,      Риски,         CAB,           Deploy,        PIR
  Причина,       Impact,        Manager,       Test,          (Post
  Urgency        Rollback       или Auto       Monitor        Implementation
                 plan                                         Review)
```

**Пример Change Request:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ CHANGE REQUEST                                                          │
├─────────────────────────────────────────────────────────────────────────┤
│ ID: CHG-2024-0089                                                       │
│ Title: Upgrade payment gateway API to v3                                │
│ Type: Normal                                                            │
│ Status: Pending Approval                                                │
│                                                                         │
│ Requested by: Tech Lead                                                 │
│ Implementation date: 2024-12-15 02:00 UTC (maintenance window)          │
│                                                                         │
│ DESCRIPTION:                                                            │
│ Upgrade payment gateway integration from API v2 to v3 to support        │
│ new payment methods and improve transaction speed.                      │
│                                                                         │
│ BUSINESS JUSTIFICATION:                                                 │
│ - v2 will be deprecated in Q1 2025                                      │
│ - v3 adds Apple Pay support (client request)                            │
│ - 20% faster transaction processing                                     │
│                                                                         │
│ RISK ASSESSMENT:                                                        │
│ - Risk Level: Medium                                                    │
│ - Impact: Payment processing for all users                              │
│ - Mitigation: Feature flag, staged rollout                              │
│                                                                         │
│ ROLLBACK PLAN:                                                          │
│ 1. Disable feature flag to route to v2                                  │
│ 2. Revert Kubernetes deployment to previous version                     │
│ 3. Verify all transactions go through v2                                │
│ 4. Rollback time: <15 minutes                                           │
│                                                                         │
│ TESTING:                                                                │
│ - Unit tests: ✓ Passed                                                 │
│ - Integration tests: ✓ Passed                                          │
│ - Staging environment: ✓ Verified                                      │
│ - Load test: ✓ 10K TPS achieved                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.4 Request Fulfillment

**Service Request** — запрос пользователя на информацию, совет, стандартное изменение или доступ к услуге.

**Цель:** Обеспечить канал для запросов пользователей и выполнять их эффективно.

**Примеры Service Requests:**

| Категория | Примеры |
|-----------|---------|
| Access | Доступ к системе, новый аккаунт, права |
| Information | Статус задачи, документация, отчёт |
| Standard Change | Добавление нового поля в форму |
| Provisioning | Новый сервер, окружение, лицензия |

**Request Fulfillment процесс:**

```
Request       Categorize      Fulfill       Verify        Close
Received  ───▶  & Route   ───▶  Request ───▶ & Accept ───▶ Request
    │             │               │            │             │
    └─────────────┴───────────────┴────────────┴─────────────┘
                               │
                     SLA Tracking & Updates
```

---

## 4. SLA и OLA

### 4.1 Service Level Agreement (SLA)

**SLA** — формальное соглашение между поставщиком услуг и клиентом, определяющее уровень сервиса.

**Компоненты SLA:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SLA STRUCTURE                                        │
└─────────────────────────────────────────────────────────────────────────┘

1. SERVICE DESCRIPTION
   - Что включено в услугу
   - Что НЕ включено (exclusions)

2. SERVICE HOURS
   - Часы предоставления услуги (24/7, 9-18, и т.д.)
   - Праздники и выходные

3. SERVICE LEVELS (Targets)
   - Availability: 99.9%
   - Response time: P1 <15 min, P2 <1 hour
   - Resolution time: P1 <4 hours, P2 <8 hours

4. REPORTING
   - Какие метрики отслеживаются
   - Частота отчётов (weekly, monthly)

5. PENALTIES/CREDITS
   - Что происходит при невыполнении SLA
   - Service credits, скидки

6. ESCALATION PROCEDURES
   - Кому звонить на каждом уровне
   - Временные рамки эскалации

7. REVIEW & AMENDMENT
   - Когда пересматривается SLA
   - Процесс внесения изменений
```

**Пример таблицы SLA:**

| Priority | Description | Response Time | Resolution Time | Target |
|----------|-------------|---------------|-----------------|--------|
| P1 | Critical | 15 min | 4 hours | 99% |
| P2 | High | 1 hour | 8 hours | 95% |
| P3 | Medium | 4 hours | 24 hours | 90% |
| P4 | Low | 8 hours | 72 hours | 85% |

**Расчёт Availability:**

```
Availability = (Total Time - Downtime) / Total Time × 100%

Пример:
- Месяц = 30 дней = 720 часов
- Downtime = 43 минуты = 0.72 часа

Availability = (720 - 0.72) / 720 × 100% = 99.9%
```

**"Девятки" доступности:**

| Availability | Downtime/год | Downtime/месяц | Downtime/неделя |
|--------------|--------------|----------------|-----------------|
| 99% (two 9s) | 3.65 дня | 7.31 часа | 1.68 часа |
| 99.9% (three 9s) | 8.77 часа | 43.83 мин | 10.08 мин |
| 99.99% (four 9s) | 52.6 мин | 4.38 мин | 1.01 мин |
| 99.999% (five 9s) | 5.26 мин | 26.3 сек | 6.05 сек |

### 4.2 Operational Level Agreement (OLA)

**OLA** — внутреннее соглашение между подразделениями одной организации.

**SLA vs OLA:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SLA vs OLA                                           │
└─────────────────────────────────────────────────────────────────────────┘

                        ┌─────────────────┐
                        │     CLIENT      │
                        └────────┬────────┘
                                 │
                          SLA: 4 hours
                            resolution
                                 │
                        ┌────────▼────────┐
                        │   SERVICE DESK  │
                        │   (Front line)  │
                        └────────┬────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         │                       │                       │
    OLA: 30 min            OLA: 1 hour             OLA: 2 hours
    triage                 diagnosis               fix
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│   L1 Support    │   │   L2 Support    │   │   L3/Dev Team   │
└─────────────────┘   └─────────────────┘   └─────────────────┘

Total OLA time: 30 min + 1 hour + 2 hours = 3.5 hours
SLA buffer: 4 hours - 3.5 hours = 30 min
```

**Пример OLA:**

| Team | Responsibility | Target Time |
|------|----------------|-------------|
| Service Desk | Log, categorize, initial triage | 30 min |
| L2 Support | Diagnosis, escalation decision | 1 hour |
| Backend Team | Investigation, fix development | 2 hours |
| DevOps | Deployment, verification | 30 min |

### 4.3 Как формировать SLA

**Шаги:**

1. **Понять потребности клиента:**
   - Какие процессы критичны?
   - Какое влияние имеет downtime?
   - Какие expectations у stakeholders?

2. **Оценить возможности:**
   - Что реально можем обеспечить?
   - Какие ресурсы нужны?
   - Исторические данные по инцидентам

3. **Определить метрики:**
   - Что измеряем?
   - Как измеряем?
   - Как отчитываемся?

4. **Согласовать условия:**
   - Что включено / исключено?
   - Penalties за несоблюдение?
   - Процесс review?

5. **Задокументировать:**
   - Формальный документ
   - Подписи обеих сторон
   - Версионирование

---

## 5. Service Catalogue

### 5.1 Что такое Service Catalogue

**Service Catalogue** — база данных или документ, содержащий информацию о всех услугах, доступных клиентам.

**Зачем нужен:**

- Клиенты знают, что доступно
- Стандартизация предложений
- Основа для SLA
- Упрощение продаж и onboarding

**Структура записи каталога:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ SERVICE CATALOGUE ENTRY                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│ Service Name: Dedicated Development Team                                │
│ Category: Professional Services                                         │
│ Status: Active                                                          │
│                                                                         │
│ DESCRIPTION:                                                            │
│ A dedicated team of engineers working exclusively on your project,      │
│ including developers, QA, and technical lead.                           │
│                                                                         │
│ SERVICE COMPONENTS:                                                     │
│ - Backend Development                                                   │
│ - Frontend Development                                                  │
│ - QA & Testing                                                          │
│ - Technical Leadership                                                  │
│ - Daily Standups                                                        │
│ - Sprint Planning & Review                                              │
│                                                                         │
│ SERVICE HOURS: 9:00-18:00 CET (Client timezone overlap)                 │
│                                                                         │
│ STANDARD SLA:                                                           │
│ - Response time: 2 hours (business hours)                               │
│ - Availability: 98% (excluding planned maintenance)                     │
│                                                                         │
│ PRICING MODEL: Time & Materials                                         │
│ TYPICAL TEAM SIZE: 3-10 engineers                                       │
│                                                                         │
│ DEPENDENCIES:                                                           │
│ - Client provides product requirements                                  │
│ - Client provides access to systems                                     │
│ - DevOps support (separate service)                                     │
│                                                                         │
│ CONTACT: Delivery Management Team                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. RACI и роли в предоставлении услуг

### 6.1 Что такое RACI

**RACI** — матрица распределения ответственности:

| Буква | Роль | Описание |
|-------|------|----------|
| **R** | Responsible | Выполняет работу |
| **A** | Accountable | Несёт ответственность за результат (только один!) |
| **C** | Consulted | Консультирует (двусторонняя коммуникация) |
| **I** | Informed | Информируется о результатах (односторонняя) |

### 6.2 Пример RACI для Incident Management

| Activity | DM | TL | Engineer | Client PM | Exec |
|----------|----|----|----------|-----------|------|
| Log incident | I | R | I | C | I |
| Initial diagnosis | I | A | R | I | - |
| Apply workaround | I | A | R | I | I |
| Communicate status | A/R | C | I | I | I |
| Permanent fix | C | A | R | I | I |
| Post-mortem | A | R | C | C | I |

**Правила RACI:**

- Каждая строка должна иметь ровно один "A"
- Должен быть хотя бы один "R"
- Минимизируйте количество "C" — много консультаций = медленные решения
- "I" не требует действий от человека

### 6.3 Типичные роли в сервисной модели

**На стороне Provider:**

| Роль | Ответственность |
|------|-----------------|
| Service Owner | Общая ответственность за услугу |
| Delivery Manager | Операционное управление командой |
| Technical Lead | Техническое руководство |
| Engineer | Выполнение работ |
| Service Desk | Первая линия контакта |

**На стороне Client:**

| Роль | Ответственность |
|------|-----------------|
| Business Owner | Бизнес-спонсор проекта |
| Product Owner | Определение требований |
| Project Manager | Координация со стороны клиента |
| End Users | Использование услуги |

---

## 7. Эскалации

### 7.1 Типы эскалаций

**Functional (Horizontal) Escalation:**

- К специалистам с нужной экспертизой
- L1 → L2 → L3
- Цель: Решить технически

**Hierarchical (Vertical) Escalation:**

- К руководству
- Engineer → TL → DM → Head of Delivery → CEO
- Цель: Получить ресурсы/решения/приоритет

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ESCALATION MATRIX                                    │
└─────────────────────────────────────────────────────────────────────────┘

FUNCTIONAL ESCALATION:
L1 Support ──▶ L2 Support ──▶ L3/Dev Team ──▶ Vendor/External

HIERARCHICAL ESCALATION:
Engineer ──▶ Tech Lead ──▶ DM ──▶ Head of Delivery ──▶ VP/CEO
                              │
                              ▼
                         Client PM ──▶ Client Director ──▶ Client VP
```

### 7.2 Когда эскалировать

**Operational Escalation (к руководителю):**

- SLA под угрозой
- Нужны дополнительные ресурсы
- Решение выходит за рамки полномочий
- Конфликт приоритетов

**Executive Escalation (к высшему руководству):**

- Критическое влияние на бизнес
- Риск потери клиента
- Репутационные риски
- Нужно решение на уровне C-level

### 7.3 Как правильно эскалировать

**Структура escalation message:**

```
Subject: [ESCALATION P1] Payment service down - Client XYZ

SITUATION:
- What happened: Payment service unavailable since 14:00 UTC
- Impact: All transactions blocked, ~$50K/hour revenue impact
- Duration: 2 hours and counting

CURRENT STATUS:
- Root cause identified: Database connection pool exhausted
- Workaround being applied
- ETA to restore: 30 minutes

ASK:
- Need approval for emergency change
- Request additional DBA support

NEXT UPDATE:
- Will provide update in 30 minutes or upon resolution
```

**Правила эскалации:**

1. Эскалировать рано, не поздно
2. Приходить с фактами, не эмоциями
3. Предлагать решение, не только проблему
4. Уведомлять всех stakeholders
5. Документировать всё

---

## 8. Практический пример: Симуляция инцидента

### 8.1 Сценарий

**Ситуация:** Пятница, 16:45. Клиент сообщает, что мобильное приложение не загружается.

### 8.2 Timeline инцидента

```
16:45 - Клиент сообщает о проблеме в Slack
        Action: Service Desk логирует инцидент
        
16:50 - Инцидент зарегистрирован как INC-2024-0200
        Priority: P1 (all users affected)
        Assigned: Backend Team
        SLA: Response 15 min ✓, Resolution 4 hours

16:55 - Initial response отправлен клиенту
        "We are aware of the issue and investigating"

17:00 - Первичная диагностика
        Finding: API Gateway returning 503 errors
        
17:10 - Root cause identified
        Finding: New deployment broke health check endpoint
        
17:15 - Workaround applied
        Action: Rollback to previous version
        
17:20 - Service restored
        Action: Verify with client
        
17:25 - Client confirms service working
        Action: Close incident, schedule post-mortem
```

### 8.3 Post-mortem

```
┌─────────────────────────────────────────────────────────────────────────┐
│ POST-INCIDENT REVIEW                                                    │
├─────────────────────────────────────────────────────────────────────────┤
│ Incident: INC-2024-0200                                                 │
│ Date: 2024-12-10                                                        │
│ Duration: 35 minutes                                                    │
│ Impact: Mobile app unavailable for all users                            │
│                                                                         │
│ TIMELINE:                                                               │
│ 16:30 - Deployment of version 2.3.1 completed                           │
│ 16:45 - First user reports received                                     │
│ 17:20 - Service restored via rollback                                   │
│                                                                         │
│ ROOT CAUSE:                                                             │
│ New health check endpoint /health/ready was not properly configured     │
│ in the Kubernetes deployment manifest. Load balancer marked all pods    │
│ as unhealthy.                                                           │
│                                                                         │
│ WHAT WENT WELL:                                                         │
│ - Fast incident detection (15 min)                                      │
│ - Quick rollback decision                                               │
│ - Good communication with client                                        │
│                                                                         │
│ WHAT COULD BE IMPROVED:                                                 │
│ - Health check was not tested in staging                                │
│ - No automated smoke test after deployment                              │
│ - Deployment happened at high-risk time (Friday afternoon)              │
│                                                                         │
│ ACTION ITEMS:                                                           │
│ 1. Add health check verification to staging tests (Owner: TL, Due: W1)  │
│ 2. Implement automated smoke tests post-deploy (Owner: DevOps, Due: W2) │
│ 3. Update deployment policy: no Friday deploys (Owner: DM, Due: Now)    │
│ 4. Add monitoring for health check failures (Owner: DevOps, Due: W1)    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 💡 Key Takeaways

- **Услуга** — это способ предоставления ценности клиенту без необходимости управлять затратами и рисками

- **ITIL 4** — современный framework с фокусом на value, collaboration и continual improvement

- **Incident Management** — восстановить услугу быстро; **Problem Management** — устранить причину навсегда

- **Change Management** защищает от рисков при внедрении изменений через оценку, approval и rollback plan

- **SLA** — обязательства перед клиентом; **OLA** — внутренние договорённости для выполнения SLA

- **RACI** обеспечивает ясность ответственности: один Accountable, один или более Responsible

- **Эскалация** — не признак слабости, а инструмент; эскалировать рано с фактами и планом

---

## 🚀 Next Steps

**Related Modules:**

- [03_Communication](../03_Communication/) — Коммуникации с клиентом
- [07_RiskManagement](../07_RiskManagement/) — Управление рисками и эскалациями

**Practice Ideas:**

1. Создайте SLA для текущего проекта с реалистичными метриками
2. Проведите RACI-workshop с командой для ключевых процессов
3. Практикуйте 5 Whys на последнем инциденте

**Going Deeper:**

- ITIL 4 Foundation Certification
- "The Phoenix Project" — роман о DevOps/ITSM трансформации
- "Visible Ops Handbook" — практическое руководство по ITSM

---

## 📚 Additional Resources

**Официальные ресурсы:**

- [ITIL 4 Foundation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) — официальная сертификация
- [ITIL 4 Practices Guide](https://www.axelos.com/resource-hub/practice-guide) — детальные гайды по практикам

**Книги:**

- "ITIL 4 Foundation" by AXELOS — официальный учебник
- "The Phoenix Project" by Gene Kim — must-read для понимания ITSM в контексте DevOps
- "IT Service Management Foundation Practice Questions" — для подготовки к сертификации

**Инструменты:**

- ServiceNow, Jira Service Management, Freshservice — для управления инцидентами
- PagerDuty, OpsGenie — для on-call и эскалаций
- Confluence — для документации SLA и процессов

---






