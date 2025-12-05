# DevOps и SRE
## От разработчика к инженеру надёжности

---

## 📚 О курсе

Этот курс охватывает все ключевые аспекты DevOps и Site Reliability Engineering — от философии и культуры до практических инструментов и процессов. Курс предназначен для опытных разработчиков и администраторов, которые хотят освоить современные практики операционной деятельности и обеспечения надёжности систем.

### Целевая аудитория

- Python-разработчики с опытом от 2-3 лет
- Системные администраторы, желающие перейти в DevOps/SRE
- Backend-инженеры, работающие с production-системами
- Team Leads, отвечающие за delivery и операции
- Все, кто хочет понимать современные практики эксплуатации

### Предварительные требования

- Уверенное владение Python
- Опыт администрирования Linux/Unix серверов
- Понимание сетей (TCP/IP, HTTP, DNS)
- Базовое знание контейнеров (Docker)
- Опыт работы с Git

---

## 🗺️ Структура курса

### Раздел 1: Основы и культура

| Модуль | Тема | Описание |
|--------|------|----------|
| [01_Intro](./01_Intro/) | Введение в DevOps | История, философия, культура, принципы DevOps и SRE |
| [02_Methodologies](./02_Methodologies/) | Методологии | Agile, Scrum, Kanban, ITIL и их роль в DevOps |
| [03_Processes](./03_Processes/) | Процессы DevOps | Жизненный цикл, планирование, регламенты |

### Раздел 2: CI/CD

| Модуль | Тема | Описание |
|--------|------|----------|
| [04_CI](./04_CI/) | Continuous Integration | Принципы CI, инструменты, best practices |
| [05_CD](./05_CD/) | Continuous Delivery/Deployment | CD pipeline, стратегии деплоя, релизы |

### Раздел 3: Инфраструктура

| Модуль | Тема | Описание |
|--------|------|----------|
| [06_IaC](./06_IaC/) | Infrastructure as Code | Terraform, Ansible, Pulumi, принципы IaC |
| [07_GitOps](./07_GitOps/) | GitOps | GitOps workflow, ArgoCD, Flux, configuration management |

### Раздел 4: Observability

| Модуль | Тема | Описание |
|--------|------|----------|
| [08_Monitoring](./08_Monitoring/) | Мониторинг | Prometheus, Grafana, системы мониторинга |
| [09_Observability](./09_Observability/) | Observability | Три столпа: логи, метрики, трейсы |

### Раздел 5: SRE и надёжность

| Модуль | Тема | Описание |
|--------|------|----------|
| [10_SRE](./10_SRE/) | Site Reliability Engineering | Принципы SRE, роль, практики Google |
| [11_ServiceLevels](./11_ServiceLevels/) | Service Levels | SLI, SLO, SLA, Error Budgets |
| [12_Incidents](./12_Incidents/) | Incident Management | On-call, инциденты, postmortems |

### Раздел 6: Метрики и развитие

| Модуль | Тема | Описание |
|--------|------|----------|
| [13_Metrics](./13_Metrics/) | Метрики DevOps | DORA metrics, измерение эффективности |
| [14_DevSecOps](./14_DevSecOps/) | DevSecOps | Безопасность в DevOps, shift left security |
| [15_Career](./15_Career/) | Карьера в DevOps/SRE | Роли, навыки, перспективы отрасли |

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                     DevOps & SRE Course                         │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │  Intro   │        │Methodolo-│        │ Processes│
    │  DevOps  │───────▶│   gies   │───────▶│  DevOps  │
    └──────────┘        └──────────┘        └──────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
         ┌─────────┐                    ┌─────────┐
         │   CI    │───────────────────▶│   CD    │
         └─────────┘                    └─────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
         ┌─────────┐                    ┌─────────┐
         │   IaC   │───────────────────▶│ GitOps  │
         └─────────┘                    └─────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
         ┌──────────┐                  ┌────────────┐
         │Monitoring│─────────────────▶│Observa-    │
         │          │                  │bility      │
         └──────────┘                  └────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │   SRE    │───────▶│ Service  │───────▶│Incidents │
    │          │        │  Levels  │        │          │
    └──────────┘        └──────────┘        └──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │ Metrics  │        │DevSecOps │        │ Career   │
    │ (DORA)   │        │          │        │          │
    └──────────┘        └──────────┘        └──────────┘
```

---

## 📋 Ключевые темы по модулям

| Модуль | Ключевые концепции |
|--------|-------------------|
| Intro | DevOps vs Ops, культура, CALMS, Three Ways |
| Methodologies | Agile Manifesto, Scrum, Kanban, ITIL v4 |
| Processes | Value Stream, планирование, ceremonies |
| CI | Trunk-based development, автоматизация сборки |
| CD | Blue-green, canary, feature flags, rollback |
| IaC | Declarative vs imperative, state management |
| GitOps | Single source of truth, reconciliation loop |
| Monitoring | Prometheus, Grafana, alerting |
| Observability | Logs, metrics, traces, корреляция |
| SRE | Toil, automation, capacity planning |
| Service Levels | SLI/SLO/SLA, error budgets, 9's |
| Incidents | On-call, severity, postmortems, blameless |
| Metrics | DORA, lead time, deployment frequency |
| DevSecOps | Shift left, SAST/DAST, supply chain |
| Career | Роли, навыки, тренды, сертификации |

---

## 📋 Формат модуля

Каждый модуль содержит:

```
XX_ModuleName/
├── lecture.md    # Основной материал лекции
└── quiz.md       # Вопросы для самопроверки
```

### Структура лекции

- **Prerequisites** — что нужно знать перед началом
- **Learning Objectives** — цели обучения
- **Основной материал** — теория с практическими примерами
- **Tools & Technologies** — обзор инструментов
- **Key Takeaways** — главные выводы
- **Next Steps** — что изучить дальше
- **Additional Resources** — книги, статьи, документация

### Quiz

- 15-20 вопросов с множественным выбором
- Практические сценарии
- Ответы с пояснениями

---

## ⏱️ Время прохождения

| Раздел | Модули | Время чтения | Время практики |
|--------|--------|--------------|----------------|
| Основы и культура | 1-3 | 3-4 часа | 2-3 часа |
| CI/CD | 4-5 | 3-4 часа | 4-5 часов |
| Инфраструктура | 6-7 | 3-4 часа | 5-6 часов |
| Observability | 8-9 | 3-4 часа | 4-5 часов |
| SRE и надёжность | 10-12 | 4-5 часов | 3-4 часа |
| Метрики и развитие | 13-15 | 3-4 часа | 2-3 часа |

**Общее время:** ~45-55 часов (включая практику)

---

## 🎓 После прохождения курса

Вы будете уметь:

✅ Понимать философию и культуру DevOps

✅ Выбирать и применять методологии (Scrum, Kanban, ITIL)

✅ Проектировать и настраивать CI/CD pipelines

✅ Описывать инфраструктуру как код (Terraform, Ansible)

✅ Внедрять GitOps практики

✅ Настраивать мониторинг и алертинг

✅ Применять принципы observability (logs, metrics, traces)

✅ Понимать роль и практики SRE

✅ Определять и отслеживать SLI/SLO/SLA

✅ Управлять инцидентами и проводить postmortems

✅ Измерять эффективность DevOps через DORA metrics

✅ Интегрировать безопасность в DevOps процессы

✅ Планировать карьеру в DevOps/SRE

---

## 📚 Рекомендуемые книги

### Фундаментальные

- **"The Phoenix Project"** by Gene Kim — бизнес-роман о DevOps трансформации
- **"The DevOps Handbook"** by Gene Kim et al. — практическое руководство
- **"Accelerate"** by Nicole Forsgren — научный подход к DevOps метрикам

### SRE

- **"Site Reliability Engineering"** by Google — библия SRE
- **"The Site Reliability Workbook"** by Google — практические упражнения
- **"Seeking SRE"** by David Blank-Edelman — сборник эссе от практиков

### Практика

- **"Infrastructure as Code"** by Kief Morris — IaC patterns
- **"Continuous Delivery"** by Jez Humble — CD principles
- **"Observability Engineering"** by Charity Majors — современный подход

### Процессы и культура

- **"Team Topologies"** by Matthew Skelton — организация команд
- **"The Unicorn Project"** by Gene Kim — продолжение Phoenix Project
- **"Release It!"** by Michael Nygard — паттерны надёжных систем

---

## 🛠️ Ключевые инструменты курса

### CI/CD
- GitHub Actions, GitLab CI, Jenkins
- ArgoCD, Flux

### Infrastructure
- Terraform, Pulumi
- Ansible, Chef

### Monitoring & Observability
- Prometheus, Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Jaeger, OpenTelemetry

### Platforms
- Kubernetes
- AWS, GCP, Azure

---

## 📝 Версия и обновления

**Версия:** 1.0  
**Дата создания:** Декабрь 2024  
**Последнее обновление:** Декабрь 2024

Курс поддерживается в актуальном состоянии. При обнаружении устаревшей информации создайте issue или pull request.

---

