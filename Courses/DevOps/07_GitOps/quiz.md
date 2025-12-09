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

A) Pull не использует Git

B) Push быстрее

C) В Pull модели агент в кластере сам забирает изменения из Git

D) Это одно и то же

---

## Question 3: ArgoCD


Что такое ArgoCD?

A) Декларативный GitOps continuous delivery tool для Kubernetes

B) CI система

C) Система мониторинга

D) База данных

---

## Question 4: Reconciliation


Что означает "continuous reconciliation" в GitOps?

A) Постоянное сравнение desired state (Git) с actual state (cluster)

B) Постоянный backup

C) Постоянный мониторинг логов

D) Непрерывное тестирование

---

## Question 5: Self-Healing


Что обеспечивает selfHeal в ArgoCD?

A) Автоматическое восстановление ресурсов при drift (изменениях вне Git)

B) Backup базы данных

C) Мониторинг здоровья приложений

D) Автоматическое исправление ошибок в коде

---

## Question 6: Application CRD


Что описывает Application CRD в ArgoCD?

A) Service mesh configuration

B) Docker image

C) Связь между Git репозиторием и Kubernetes destination

D) Сетевые политики

---

## Question 7: Kustomize


Для чего используется Kustomize в GitOps?

A) Для управления environment-specific конфигурациями (base + overlays)

B) Для сборки Docker images

C) Для backup

D) Для мониторинга

---

## Question 8: Secrets в GitOps


Как правильно хранить секреты в GitOps репозитории?

A) В README файле

B) Использовать Sealed Secrets или External Secrets (зашифрованные)

C) В base64 encoding

D) В plain-text в Secret manifest

---

## Question 9: App of Apps


Что такое "App of Apps" паттерн в ArgoCD?

A) Родительское Application, которое управляет другими Applications

B) Multi-container pod

C) Приложение с несколькими репликами

D) Микросервисная архитектура

---

## Question 10: Monorepo vs Polyrepo


Когда лучше использовать Monorepo для GitOps?

A) Никогда

B) Когда нет CI/CD

C) Только для крупных компаний

D) Когда команда небольшая и нужна простота управления

---

## Question 11: Prune


Что делает опция `prune: true` в ArgoCD syncPolicy?

A) Удаляет старые images

B) Удаляет ресурсы из кластера, которых нет в Git

C) Удаляет историю Git

D) Очищает логи

---

## Question 12: Image Updater


Для чего используется ArgoCD Image Updater?

A) Для сборки images

B) Для удаления images

C) Для автоматического обновления image tags в Git при появлении новых версий

D) Для сканирования уязвимостей

---

## Question 13: ApplicationSet


Что позволяет делать ApplicationSet?

A) Управлять DNS

B) Настраивать firewall

C) Генерировать множество Applications из шаблона

D) Создавать Docker images

---

## Question 14: External Secrets


Что делает External Secrets Operator?

A) Удаляет секреты

B) Шифрует трафик

C) Экспортирует секреты наружу

D) Синхронизирует секреты из внешних хранилищ (AWS SM, Vault) в Kubernetes

---

## Question 15: Git Best Practices


Какой Git best practice важен для GitOps?

A) Использовать только main branch

B) Atomic commits, branch protection, PR reviews

C) Коммитить всё в одном большом коммите

D) Никогда не делать merge

---

## Question 16: Drift


Что такое "drift" в контексте GitOps?

A) Ошибка в коде

B) Отсутствие интернета

C) Расхождение между desired state в Git и actual state в кластере

D) Сетевая задержка

---

## Question 17: Sync Status


Что означает статус "OutOfSync" в ArgoCD?

A) Приложение работает нормально

B) Git репозиторий недоступен

C) Actual state отличается от desired state в Git

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

A) Анализирует статус Kubernetes ресурсов (Ready, Progressing, etc.)

B) Читает логи

C) Пингует серверы

D) Проверяет Git commits

---

## Question 20: Rollback


Как выполнить rollback в GitOps?

A) Перезапустить CI

B) git revert или указать предыдущую revision в ArgoCD

C) Удалить кластер

D) Rollback невозможен

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | GitOps = Git as single source of truth для всей системы |
| 2 | C | Pull: агент в кластере сам забирает изменения (не CI push) |
| 3 | A | ArgoCD — GitOps CD tool для Kubernetes |
| 4 | A | Continuous reconciliation — постоянное сравнение и синхронизация |
| 5 | A | selfHeal автоматически восстанавливает при изменениях вне Git |
| 6 | C | Application связывает source (Git) с destination (K8s) |
| 7 | A | Kustomize: base + overlays для разных environments |
| 8 | B | Sealed Secrets или External Secrets для безопасного хранения |
| 9 | A | App of Apps — паттерн для управления множеством Applications |
| 10 | D | Monorepo хорош для небольших команд, проще управлять |
| 11 | B | prune удаляет orphaned ресурсы (которых нет в Git) |
| 12 | C | Image Updater автоматически обновляет tags в Git |
| 13 | C | ApplicationSet генерирует Applications из шаблонов |
| 14 | D | External Secrets синхронизирует секреты из внешних хранилищ |
| 15 | B | Atomic commits, branch protection, reviews — key practices |
| 16 | C | Drift = расхождение Git vs cluster |
| 17 | C | OutOfSync = actual ≠ desired |
| 18 | B | Overlay — env-specific настройки поверх base |
| 19 | A | ArgoCD анализирует статусы K8s ресурсов |
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

