# GitOps - Quiz

Проверьте свои знания по GitOps, ArgoCD и управлению конфигурациями.

---

## Question 1: Определение GitOps

Что является ключевым принципом GitOps?

A) Git используется только для кода приложений

B) Git — единственный источник истины для инфраструктуры и приложений

C) Deployment через SSH

D) Ручное управление кластером

---

## Question 2: Push vs Pull

Чем Pull модель GitOps отличается от традиционной Push модели?

A) Push быстрее

B) В Pull модели агент в кластере сам забирает изменения из Git

C) Pull не использует Git

D) Это одно и то же

---

## Question 3: ArgoCD

Что такое ArgoCD?

A) Система мониторинга

B) Декларативный GitOps continuous delivery tool для Kubernetes

C) База данных

D) CI система

---

## Question 4: Reconciliation

Что означает "continuous reconciliation" в GitOps?

A) Постоянный backup

B) Постоянное сравнение desired state (Git) с actual state (cluster)

C) Непрерывное тестирование

D) Постоянный мониторинг логов

---

## Question 5: Self-Healing

Что обеспечивает selfHeal в ArgoCD?

A) Автоматическое исправление ошибок в коде

B) Автоматическое восстановление ресурсов при drift (изменениях вне Git)

C) Мониторинг здоровья приложений

D) Backup базы данных

---

## Question 6: Application CRD

Что описывает Application CRD в ArgoCD?

A) Docker image

B) Связь между Git репозиторием и Kubernetes destination

C) Сетевые политики

D) Service mesh configuration

---

## Question 7: Kustomize

Для чего используется Kustomize в GitOps?

A) Для сборки Docker images

B) Для управления environment-specific конфигурациями (base + overlays)

C) Для мониторинга

D) Для backup

---

## Question 8: Secrets в GitOps

Как правильно хранить секреты в GitOps репозитории?

A) В plain-text в Secret manifest

B) В base64 encoding

C) Использовать Sealed Secrets или External Secrets (зашифрованные)

D) В README файле

---

## Question 9: App of Apps

Что такое "App of Apps" паттерн в ArgoCD?

A) Приложение с несколькими репликами

B) Родительское Application, которое управляет другими Applications

C) Multi-container pod

D) Микросервисная архитектура

---

## Question 10: Monorepo vs Polyrepo

Когда лучше использовать Monorepo для GitOps?

A) Никогда

B) Когда команда небольшая и нужна простота управления

C) Только для крупных компаний

D) Когда нет CI/CD

---

## Question 11: Prune

Что делает опция `prune: true` в ArgoCD syncPolicy?

A) Удаляет историю Git

B) Удаляет ресурсы из кластера, которых нет в Git

C) Очищает логи

D) Удаляет старые images

---

## Question 12: Image Updater

Для чего используется ArgoCD Image Updater?

A) Для сборки images

B) Для автоматического обновления image tags в Git при появлении новых версий

C) Для удаления images

D) Для сканирования уязвимостей

---

## Question 13: ApplicationSet

Что позволяет делать ApplicationSet?

A) Создавать Docker images

B) Генерировать множество Applications из шаблона

C) Управлять DNS

D) Настраивать firewall

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

B) Atomic commits, branch protection, PR reviews

C) Никогда не делать merge

D) Использовать только main branch

---

## Question 16: Drift

Что такое "drift" в контексте GitOps?

A) Сетевая задержка

B) Расхождение между desired state в Git и actual state в кластере

C) Ошибка в коде

D) Отсутствие интернета

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

A) Слой шифрования

B) Environment-specific настройки, накладываемые на base

C) Тип deployment

D) Сетевой протокол

---

## Question 19: Health Check

Как ArgoCD определяет health приложения?

A) Проверяет Git commits

B) Анализирует статус Kubernetes ресурсов (Ready, Progressing, etc.)

C) Пингует серверы

D) Читает логи

---

## Question 20: Rollback

Как выполнить rollback в GitOps?

A) Удалить кластер

B) git revert или указать предыдущую revision в ArgoCD

C) Перезапустить CI

D) Rollback невозможен

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | GitOps = Git as single source of truth для всей системы |
| 2 | B | Pull: агент в кластере сам забирает изменения (не CI push) |
| 3 | B | ArgoCD — GitOps CD tool для Kubernetes |
| 4 | B | Continuous reconciliation — постоянное сравнение и синхронизация |
| 5 | B | selfHeal автоматически восстанавливает при изменениях вне Git |
| 6 | B | Application связывает source (Git) с destination (K8s) |
| 7 | B | Kustomize: base + overlays для разных environments |
| 8 | C | Sealed Secrets или External Secrets для безопасного хранения |
| 9 | B | App of Apps — паттерн для управления множеством Applications |
| 10 | B | Monorepo хорош для небольших команд, проще управлять |
| 11 | B | prune удаляет orphaned ресурсы (которых нет в Git) |
| 12 | B | Image Updater автоматически обновляет tags в Git |
| 13 | B | ApplicationSet генерирует Applications из шаблонов |
| 14 | B | External Secrets синхронизирует секреты из внешних хранилищ |
| 15 | B | Atomic commits, branch protection, reviews — key practices |
| 16 | B | Drift = расхождение Git vs cluster |
| 17 | B | OutOfSync = actual ≠ desired |
| 18 | B | Overlay — env-specific настройки поверх base |
| 19 | B | ArgoCD анализирует статусы K8s ресурсов |
| 20 | B | Rollback через git revert или указание revision |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете GitOps. Переходите к мониторингу. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите secrets management и ApplicationSet. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте ArgoCD workflow и Kustomize. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы GitOps и примеры. |

---

