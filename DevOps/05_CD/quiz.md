# Continuous Delivery и Deployment - Quiz

Проверьте свои знания по CD, стратегиям развёртывания и feature flags.

---

## Question 1: CD vs Continuous Deployment

Чем Continuous Delivery отличается от Continuous Deployment?

A) Это одно и то же

B) В CD финальный деплой в production ручной, в Continuous Deployment — автоматический

C) Continuous Deployment проще в реализации

D) CD не требует автоматических тестов

---

## Question 2: Blue-Green Deployment

Какое главное преимущество Blue-Green deployment?

A) Требует меньше ресурсов

B) Мгновенный rollback

C) Не требует load balancer

D) Автоматическое тестирование

---

## Question 3: Canary Deployment

Что характеризует Canary deployment?

A) Весь трафик сразу идёт на новую версию

B) Постепенное направление трафика на новую версию (10% → 25% → 50% → 100%)

C) Две идентичные среды

D) Полный downtime при деплое

---

## Question 4: Rolling Update

Что происходит при Rolling Update в Kubernetes?

A) Все pods останавливаются, затем запускаются новые

B) Pods постепенно заменяются новыми версиями

C) Создаётся копия всего cluster

D) Требуется ручной restart каждого pod

---

## Question 5: Feature Flags

Для чего используются feature flags?

A) Для шифрования кода

B) Для включения/выключения функционала без деплоя

C) Для логирования

D) Для мониторинга

---

## Question 6: Feature Flag Types

Какой тип feature flag используется для A/B тестирования?

A) Release toggle

B) Experiment toggle

C) Ops toggle

D) Permission toggle

---

## Question 7: Database Migrations

Какой подход обеспечивает zero-downtime database migration?

A) Удалить таблицу и создать заново

B) Expand-Contract pattern (добавить новое, мигрировать, удалить старое)

C) Остановить приложение на время миграции

D) Использовать только NoSQL базы

---

## Question 8: Rollback

Когда следует выполнять rollback?

A) После каждого деплоя

B) При error rate > threshold, критических сбоях, data corruption

C) Только по запросу менеджмента

D) Никогда — всегда делать forward fix

---

## Question 9: Environment Parity

Что означает принцип Environment Parity?

A) Все environments должны иметь одинаковые пароли

B) Dev, staging и production environments должны быть максимально похожи

C) Использовать только один environment

D) Environments должны быть в разных регионах

---

## Question 10: Smoke Tests

Когда выполняются smoke tests?

A) Перед написанием кода

B) Сразу после деплоя для проверки базовой работоспособности

C) Раз в месяц

D) Только в development

---

## Question 11: Deployment Strategy Selection

Какую стратегию выбрать, если нужен быстрый rollback и допустимы двойные ресурсы?

A) Recreate

B) Rolling Update

C) Blue-Green

D) Canary

---

## Question 12: Recreate Strategy

Когда уместно использовать Recreate deployment strategy?

A) Для production с высоким SLA

B) Когда downtime недопустим

C) Для dev/test environments или при несовместимых изменениях

D) Всегда

---

## Question 13: Build Once Deploy Many

Что означает принцип "Build Once, Deploy Many"?

A) Собирать отдельный artifact для каждого environment

B) Один artifact используется для всех environments (dev, staging, prod)

C) Деплоить только один раз

D) Использовать один сервер для всех сред

---

## Question 14: Configuration Management

Как правильно управлять конфигурацией для разных environments?

A) Хардкодить в приложении

B) Разделять config от кода, использовать environment variables

C) Создавать отдельную версию кода для каждого environment

D) Хранить в коде в зашифрованном виде

---

## Question 15: Readiness Probe

Для чего используется readinessProbe в Kubernetes?

A) Для проверки, что pod жив

B) Для определения, готов ли pod принимать трафик

C) Для логирования

D) Для масштабирования

---

## Question 16: Canary Analysis

На основе чего Canary deployment принимает решение о продолжении или rollback?

A) Времени суток

B) Метрик (error rate, latency) новой версии

C) Количества пользователей

D) Размера Docker image

---

## Question 17: Feature Flag Best Practices

Что следует делать со старыми feature flags?

A) Оставлять навсегда

B) Удалять после полного rollout и стабилизации

C) Переименовывать

D) Дублировать

---

## Question 18: Progressive Delivery

Что такое Progressive Delivery?

A) Деплой только по выходным

B) Постепенный rollout с автоматической проверкой метрик

C) Ручной деплой

D) Деплой без тестов

---

## Question 19: Liveness vs Readiness Probe

В чём разница между livenessProbe и readinessProbe?

A) Это одно и то же

B) livenessProbe перезапускает pod при сбое, readinessProbe убирает из балансировки

C) Оба перезапускают pod

D) Оба только логируют

---

## Question 20: Post-Deployment Verification

Что проверяется сразу после деплоя (0-5 минут)?

A) Только логи

B) Error rate, response time, health endpoints

C) Финансовые показатели

D) Количество пользователей за месяц

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CD = всегда готовы к релизу (ручной trigger), Continuous Deployment = автоматический релиз |
| 2 | B | Blue-Green позволяет мгновенно переключить трафик обратно на blue при проблемах |
| 3 | B | Canary постепенно увеличивает трафик на новую версию, проверяя метрики |
| 4 | B | Rolling update постепенно заменяет pods, обеспечивая zero downtime |
| 5 | B | Feature flags позволяют включать/выключать функции без нового деплоя |
| 6 | B | Experiment toggle используется для A/B тестов с разными вариантами |
| 7 | B | Expand-Contract: добавляем новое → мигрируем → удаляем старое |
| 8 | B | Rollback при критических проблемах: высокий error rate, сбои, data issues |
| 9 | B | Environments должны быть похожи для предсказуемого поведения |
| 10 | B | Smoke tests проверяют базовую работоспособность сразу после деплоя |
| 11 | C | Blue-Green: instant rollback, но требует 2x ресурсов |
| 12 | C | Recreate приемлем для dev/test или при breaking changes |
| 13 | B | Один artifact проходит через все environments |
| 14 | B | Config отделён от кода, передаётся через env vars |
| 15 | B | readinessProbe определяет, готов ли pod к трафику |
| 16 | B | Canary анализирует метрики для принятия решения о rollout/rollback |
| 17 | B | Старые flags нужно удалять, иначе накапливается технический долг |
| 18 | B | Progressive delivery = постепенный rollout с автоматическими проверками |
| 19 | B | liveness = жив ли pod (restart), readiness = готов ли к трафику |
| 20 | B | Сразу после деплоя проверяем error rate, latency, health |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете CD. Переходите к IaC. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите deployment strategies и feature flags. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о Canary и Blue-Green. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все стратегии развёртывания. |

---

