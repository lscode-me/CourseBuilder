# GitOps - Quiz

Проверьте свои знания по GitOps, ArgoCD и управлению конфигурациями.

---

## Question 1: Определение GitOps

Что является ключевым принципом GitOps?

A) Git — единственный источник истины для инфраструктуры и приложений

B) Ручное управление кластером

C) Git используется только для кода приложений

D) Deployment через SSH

---

## Question 2: Push vs Pull

Чем Pull модель GitOps отличается от традиционной Push модели?

A) Это одно и то же

B) Pull не использует Git

C) В Pull модели агент в кластере сам забирает изменения из Git

D) Push быстрее

---

## Question 3: ArgoCD

Что такое ArgoCD?

A) База данных

B) Декларативный GitOps continuous delivery tool для Kubernetes

C) Система мониторинга

D) CI система

---

## Question 4: Reconciliation

Что означает "continuous reconciliation" в GitOps?

A) Постоянный мониторинг логов

B) Постоянное сравнение desired state (Git) с actual state (cluster)

C) Постоянный backup

D) Непрерывное тестирование

---

## Question 5: Self-Healing

Что обеспечивает selfHeal в ArgoCD?

A) Мониторинг здоровья приложений

B) Backup базы данных

C) Автоматическое восстановление ресурсов при drift (изменениях вне Git)

D) Автоматическое исправление ошибок в коде

---

## Question 6: Application CRD

Что описывает Application CRD в ArgoCD?

A) Сетевые политики

B) Service mesh configuration

C) Связь между Git репозиторием и Kubernetes destination

D) Docker image

---

## Question 7: Kustomize

Для чего используется Kustomize в GitOps?

A) Для backup

B) Для мониторинга

C) Для управления environment-specific конфигурациями (base + overlays)

D) Для сборки Docker images

---

## Question 8: Secrets в GitOps

Как правильно хранить секреты в GitOps репозитории?

A) Использовать Sealed Secrets или External Secrets (зашифрованные)

B) В plain-text в Secret manifest

C) В README файле

D) В base64 encoding

---

## Question 9: App of Apps

Что такое "App of Apps" паттерн в ArgoCD?

A) Микросервисная архитектура

B) Multi-container pod

C) Приложение с несколькими репликами

D) Родительское Application, которое управляет другими Applications

---

## Question 10: Monorepo vs Polyrepo

Когда лучше использовать Monorepo для GitOps?

A) Только для крупных компаний

B) Когда нет CI/CD

C) Никогда

D) Когда команда небольшая и нужна простота управления

---

## Question 11: Prune

Что делает опция `prune: true` в ArgoCD syncPolicy?

A) Очищает логи

B) Удаляет старые images

C) Удаляет ресурсы из кластера, которых нет в Git

D) Удаляет историю Git

---

## Question 12: Image Updater

Для чего используется ArgoCD Image Updater?

A) Для автоматического обновления image tags в Git при появлении новых версий

B) Для удаления images

C) Для сканирования уязвимостей

D) Для сборки images

---

## Question 13: ApplicationSet

Что позволяет делать ApplicationSet?

A) Генерировать множество Applications из шаблона

B) Настраивать firewall

C) Управлять DNS

D) Создавать Docker images

---

## Question 14: External Secrets

Что делает External Secrets Operator?

A) Экспортирует секреты наружу

B) Синхронизирует секреты из внешних хранилищ (AWS SM, Vault) в Kubernetes

C) Удаляет секреты

D) Шифрует трафик

---

## Question 15: Git Best Practices

Какой Git best practice важен для GitOps?

A) Коммитить всё в одном большом коммите

B) Никогда не делать merge

C) Использовать только main branch

D) Atomic commits, branch protection, PR reviews

---

## Question 16: Drift

Что такое "drift" в контексте GitOps?

A) Ошибка в коде

B) Отсутствие интернета

C) Сетевая задержка

D) Расхождение между desired state в Git и actual state в кластере

---

## Question 17: Sync Status

Что означает статус "OutOfSync" в ArgoCD?

A) Приложение работает нормально

B) Actual state отличается от desired state в Git

C) Git репозиторий недоступен

D) Кластер выключен

---

## Question 18: Overlay

Что такое "overlay" в Kustomize?

A) Environment-specific настройки, накладываемые на base

B) Слой шифрования

C) Тип deployment

D) Сетевой протокол

---

## Question 19: Health Check

Как ArgoCD определяет health приложения?

A) Анализирует статус Kubernetes ресурсов (Ready, Progressing, etc.)

B) Проверяет Git commits

C) Читает логи

D) Пингует серверы

---

## Question 20: Rollback

Как выполнить rollback в GitOps?

A) Rollback невозможен

B) Удалить кластер

C) git revert или указать предыдущую revision в ArgoCD

D) Перезапустить CI

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | GitOps = Git as single source of truth для всей системы |
| 2 | C | Pull: агент в кластере сам забирает изменения (не CI push) |
| 3 | B | ArgoCD — GitOps CD tool для Kubernetes |
| 4 | B | Continuous reconciliation — постоянное сравнение и синхронизация |
| 5 | C | selfHeal автоматически восстанавливает при изменениях вне Git |
| 6 | C | Application связывает source (Git) с destination (K8s) |
| 7 | C | Kustomize: base + overlays для разных environments |
| 8 | A | Sealed Secrets или External Secrets для безопасного хранения |
| 9 | D | App of Apps — паттерн для управления множеством Applications |
| 10 | D | Monorepo хорош для небольших команд, проще управлять |
| 11 | C | prune удаляет orphaned ресурсы (которых нет в Git) |
| 12 | A | Image Updater автоматически обновляет tags в Git |
| 13 | A | ApplicationSet генерирует Applications из шаблонов |
| 14 | B | External Secrets синхронизирует секреты из внешних хранилищ |
| 15 | D | Atomic commits, branch protection, reviews — key practices |
| 16 | D | Drift = расхождение Git vs cluster |
| 17 | B | OutOfSync = actual ≠ desired |
| 18 | A | Overlay — env-specific настройки поверх base |
| 19 | A | ArgoCD анализирует статусы K8s ресурсов |
| 20 | C | Rollback через git revert или указание revision |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете GitOps. Переходите к мониторингу. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите secrets management и ApplicationSet. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте ArgoCD workflow и Kustomize. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы GitOps и примеры. |

---

