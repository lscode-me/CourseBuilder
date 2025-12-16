# Continuous Delivery и Deployment - Quiz

Проверьте свои знания по CD, стратегиям развёртывания и feature flags.

---

## Question 1: CD vs Continuous Deployment

Чем Continuous Delivery отличается от Continuous Deployment?

A) В CD финальный деплой в production ручной, в Continuous Deployment — автоматический

B) CD не требует автоматических тестов

C) Это одно и то же

D) Continuous Deployment проще в реализации

---

## Question 2: Blue-Green Deployment

Какое главное преимущество Blue-Green deployment?

A) Мгновенный rollback

B) Не требует load balancer

C) Требует меньше ресурсов

D) Автоматическое тестирование

---

## Question 3: Canary Deployment

Что характеризует Canary deployment?

A) Весь трафик сразу идёт на новую версию

B) Постепенное направление трафика на новую версию (10% → 25% → 50% → 100%)

C) Полный downtime при деплое

D) Две идентичные среды

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

B) Для логирования

C) Для включения/выключения функционала без деплоя

D) Для мониторинга

---

## Question 6: Feature Flag Types

Какой тип feature flag используется для A/B тестирования?

A) Ops toggle

B) Experiment toggle

C) Permission toggle

D) Release toggle

---

## Question 7: Database Migrations

Какой подход обеспечивает zero-downtime database migration?

A) Expand-Contract pattern (добавить новое, мигрировать, удалить старое)

B) Удалить таблицу и создать заново

C) Остановить приложение на время миграции

D) Использовать только NoSQL базы

---

## Question 8: Rollback

Когда следует выполнять rollback?

A) Никогда — всегда делать forward fix

B) После каждого деплоя

C) Только по запросу менеджмента

D) При error rate > threshold, критических сбоях, data corruption

---

## Question 9: Environment Parity

Что означает принцип Environment Parity?

A) Environments должны быть в разных регионах

B) Использовать только один environment

C) Dev, staging и production environments должны быть максимально похожи

D) Все environments должны иметь одинаковые пароли

---

## Question 10: Smoke Tests

Когда выполняются smoke tests?

A) Перед написанием кода

B) Только в development

C) Раз в месяц

D) Сразу после деплоя для проверки базовой работоспособности

---

## Question 11: Deployment Strategy Selection

Какую стратегию выбрать, если нужен быстрый rollback и допустимы двойные ресурсы?

A) Rolling Update

B) Canary

C) Blue-Green

D) Recreate

---

## Question 12: Recreate Strategy

Когда уместно использовать Recreate deployment strategy?

A) Для production с высоким SLA

B) Для dev/test environments или при несовместимых изменениях

C) Когда downtime недопустим

D) Всегда

---

## Question 13: Build Once Deploy Many

Что означает принцип "Build Once, Deploy Many"?

A) Деплоить только один раз

B) Один artifact используется для всех environments (dev, staging, prod)

C) Собирать отдельный artifact для каждого environment

D) Использовать один сервер для всех сред

---

## Question 14: Configuration Management

Как правильно управлять конфигурацией для разных environments?

A) Хардкодить в приложении

B) Создавать отдельную версию кода для каждого environment

C) Разделять config от кода, использовать environment variables

D) Хранить в коде в зашифрованном виде

---

## Question 15: Readiness Probe

Для чего используется readinessProbe в Kubernetes?

A) Для логирования

B) Для определения, готов ли pod принимать трафик

C) Для масштабирования

D) Для проверки, что pod жив

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

A) Удалять после полного rollout и стабилизации

B) Дублировать

C) Переименовывать

D) Оставлять навсегда

---

## Question 18: Progressive Delivery

Что такое Progressive Delivery?

A) Ручной деплой

B) Деплой без тестов

C) Постепенный rollout с автоматической проверкой метрик

D) Деплой только по выходным

---

## Question 19: Liveness vs Readiness Probe

В чём разница между livenessProbe и readinessProbe?

A) Это одно и то же

B) livenessProbe перезапускает pod при сбое, readinessProbe убирает из балансировки

C) Оба только логируют

D) Оба перезапускают pod

---

## Question 20: Post-Deployment Verification

Что проверяется сразу после деплоя (0-5 минут)?

A) Error rate, response time, health endpoints

B) Количество пользователей за месяц

C) Финансовые показатели

D) Только логи

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | CD = всегда готовы к релизу (ручной trigger), Continuous Deployment = автоматический релиз |
| 2 | A | Blue-Green позволяет мгновенно переключить трафик обратно на blue при проблемах |
| 3 | B | Canary постепенно увеличивает трафик на новую версию, проверяя метрики |
| 4 | B | Rolling update постепенно заменяет pods, обеспечивая zero downtime |
| 5 | C | Feature flags позволяют включать/выключать функции без нового деплоя |
| 6 | B | Experiment toggle используется для A/B тестов с разными вариантами |
| 7 | A | Expand-Contract: добавляем новое → мигрируем → удаляем старое |
| 8 | D | Rollback при критических проблемах: высокий error rate, сбои, data issues |
| 9 | C | Environments должны быть похожи для предсказуемого поведения |
| 10 | D | Smoke tests проверяют базовую работоспособность сразу после деплоя |
| 11 | C | Blue-Green: instant rollback, но требует 2x ресурсов |
| 12 | B | Recreate приемлем для dev/test или при breaking changes |
| 13 | B | Один artifact проходит через все environments |
| 14 | C | Config отделён от кода, передаётся через env vars |
| 15 | B | readinessProbe определяет, готов ли pod к трафику |
| 16 | B | Canary анализирует метрики для принятия решения о rollout/rollback |
| 17 | A | Старые flags нужно удалять, иначе накапливается технический долг |
| 18 | C | Progressive delivery = постепенный rollout с автоматическими проверками |
| 19 | B | liveness = жив ли pod (restart), readiness = готов ли к трафику |
| 20 | A | Сразу после деплоя проверяем error rate, latency, health |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете CD. Переходите к IaC. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите deployment strategies и feature flags. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о Canary и Blue-Green. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все стратегии развёртывания. |

---

