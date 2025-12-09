# GitOps - Quiz

Проверьте свои знания по GitOps, ArgoCD и управлению конфигурациями.

---

## Question 1: Определение GitOps







Что является ключевым принципом GitOps?

A) Deployment через SSH

B) Git используется только для кода приложений

C) Ручное управление кластером

D) Git — единственный источник истины для инфраструктуры и приложений

---

## Question 2: Push vs Pull







Чем Pull модель GitOps отличается от традиционной Push модели?

A) В Pull модели агент в кластере сам забирает изменения из Git

B) Push быстрее

C) Это одно и то же

D) Pull не использует Git

---

## Question 3: ArgoCD







Что такое ArgoCD?

A) CI система

B) База данных

C) Система мониторинга

D) Декларативный GitOps continuous delivery tool для Kubernetes

---

## Question 4: Reconciliation







Что означает "continuous reconciliation" в GitOps?

A) Непрерывное тестирование

B) Постоянное сравнение desired state (Git) с actual state (cluster)

C) Постоянный мониторинг логов

D) Постоянный backup

---

## Question 5: Self-Healing







Что обеспечивает selfHeal в ArgoCD?

A) Автоматическое восстановление ресурсов при drift (изменениях вне Git)

B) Автоматическое исправление ошибок в коде

C) Backup базы данных

D) Мониторинг здоровья приложений

---

## Question 6: Application CRD







Что описывает Application CRD в ArgoCD?

A) Docker image

B) Сетевые политики

C) Связь между Git репозиторием и Kubernetes destination

D) Service mesh configuration

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

A) В plain-text в Secret manifest

B) В base64 encoding

C) В README файле

D) Использовать Sealed Secrets или External Secrets (зашифрованные)

---

## Question 9: App of Apps







Что такое "App of Apps" паттерн в ArgoCD?

A) Приложение с несколькими репликами

B) Микросервисная архитектура

C) Родительское Application, которое управляет другими Applications

D) Multi-container pod

---

## Question 10: Monorepo vs Polyrepo







Когда лучше использовать Monorepo для GitOps?

A) Никогда

B) Только для крупных компаний

C) Когда команда небольшая и нужна простота управления

D) Когда нет CI/CD

---

## Question 11: Prune







Что делает опция `prune: true` в ArgoCD syncPolicy?

A) Удаляет историю Git

B) Очищает логи

C) Удаляет старые images

D) Удаляет ресурсы из кластера, которых нет в Git

---

## Question 12: Image Updater







Для чего используется ArgoCD Image Updater?

A) Для сканирования уязвимостей

B) Для удаления images

C) Для сборки images

D) Для автоматического обновления image tags в Git при появлении новых версий

---

## Question 13: ApplicationSet







Что позволяет делать ApplicationSet?

A) Создавать Docker images

B) Настраивать firewall

C) Генерировать множество Applications из шаблона

D) Управлять DNS

---

## Question 14: External Secrets







Что делает External Secrets Operator?

A) Шифрует трафик

B) Синхронизирует секреты из внешних хранилищ (AWS SM, Vault) в Kubernetes

C) Экспортирует секреты наружу

D) Удаляет секреты

---

## Question 15: Git Best Practices







Какой Git best practice важен для GitOps?

A) Atomic commits, branch protection, PR reviews

B) Коммитить всё в одном большом коммите

C) Использовать только main branch

D) Никогда не делать merge

---

## Question 16: Drift







Что такое "drift" в контексте GitOps?

A) Ошибка в коде

B) Сетевая задержка

C) Отсутствие интернета

D) Расхождение между desired state в Git и actual state в кластере

---

## Question 17: Sync Status







Что означает статус "OutOfSync" в ArgoCD?

A) Кластер выключен

B) Git репозиторий недоступен

C) Приложение работает нормально

D) Actual state отличается от desired state в Git

---

## Question 18: Overlay







Что такое "overlay" в Kustomize?

A) Сетевой протокол

B) Слой шифрования

C) Тип deployment

D) Environment-specific настройки, накладываемые на base

---

## Question 19: Health Check







Как ArgoCD определяет health приложения?

A) Проверяет Git commits

B) Анализирует статус Kubernetes ресурсов (Ready, Progressing, etc.)

C) Читает логи

D) Пингует серверы

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
| 1 | D | GitOps = Git as single source of truth для всей системы |
| 2 | A | Pull: агент в кластере сам забирает изменения (не CI push) |
| 3 | D | ArgoCD — GitOps CD tool для Kubernetes |
| 4 | B | Continuous reconciliation — постоянное сравнение и синхронизация |
| 5 | A | selfHeal автоматически восстанавливает при изменениях вне Git |
| 6 | C | Application связывает source (Git) с destination (K8s) |
| 7 | A | Kustomize: base + overlays для разных environments |
| 8 | D | Sealed Secrets или External Secrets для безопасного хранения |
| 9 | C | App of Apps — паттерн для управления множеством Applications |
| 10 | C | Monorepo хорош для небольших команд, проще управлять |
| 11 | D | prune удаляет orphaned ресурсы (которых нет в Git) |
| 12 | D | Image Updater автоматически обновляет tags в Git |
| 13 | C | ApplicationSet генерирует Applications из шаблонов |
| 14 | B | External Secrets синхронизирует секреты из внешних хранилищ |
| 15 | A | Atomic commits, branch protection, reviews — key practices |
| 16 | D | Drift = расхождение Git vs cluster |
| 17 | D | OutOfSync = actual ≠ desired |
| 18 | D | Overlay — env-specific настройки поверх base |
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

