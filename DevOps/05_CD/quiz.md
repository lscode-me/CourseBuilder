# Continuous Delivery и Deployment - Quiz

Проверьте свои знания по CD, стратегиям развёртывания и feature flags.

---

## Question 1: CD vs Continuous Deployment


Чем Continuous Delivery отличается от Continuous Deployment?

A) Это одно и то же

B) Continuous Deployment проще в реализации

C) В CD финальный деплой в production ручной, в Continuous Deployment — автоматический

D) CD не требует автоматических тестов

---

## Question 2: Blue-Green Deployment


Какое главное преимущество Blue-Green deployment?

A) Автоматическое тестирование

B) Не требует load balancer

C) Мгновенный rollback

D) Требует меньше ресурсов

---

## Question 3: Canary Deployment


Что характеризует Canary deployment?

A) Две идентичные среды

B) Постепенное направление трафика на новую версию (10% → 25% → 50% → 100%)

C) Весь трафик сразу идёт на новую версию

D) Полный downtime при деплое

---

## Question 4: Rolling Update


Что происходит при Rolling Update в Kubernetes?

A) Все pods останавливаются, затем запускаются новые

B) Создаётся копия всего cluster

C) Pods постепенно заменяются новыми версиями

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

A) Permission toggle

B) Release toggle

C) Ops toggle

D) Experiment toggle

---

## Question 7: Database Migrations


Какой подход обеспечивает zero-downtime database migration?

A) Остановить приложение на время миграции

B) Expand-Contract pattern (добавить новое, мигрировать, удалить старое)

C) Удалить таблицу и создать заново

D) Использовать только NoSQL базы

---

## Question 8: Rollback


Когда следует выполнять rollback?

A) Никогда — всегда делать forward fix

B) Только по запросу менеджмента

C) При error rate > threshold, критических сбоях, data corruption

D) После каждого деплоя

---

## Question 9: Environment Parity


Что означает принцип Environment Parity?

A) Использовать только один environment

B) Все environments должны иметь одинаковые пароли

C) Dev, staging и production environments должны быть максимально похожи

D) Environments должны быть в разных регионах

---

## Question 10: Smoke Tests


Когда выполняются smoke tests?

A) Сразу после деплоя для проверки базовой работоспособности

B) Раз в месяц

C) Перед написанием кода

D) Только в development

---

## Question 11: Deployment Strategy Selection


Какую стратегию выбрать, если нужен быстрый rollback и допустимы двойные ресурсы?

A) Canary

B) Rolling Update

C) Recreate

D) Blue-Green

---

## Question 12: Recreate Strategy


Когда уместно использовать Recreate deployment strategy?

A) Всегда

B) Когда downtime недопустим

C) Для dev/test environments или при несовместимых изменениях

D) Для production с высоким SLA

---

## Question 13: Build Once Deploy Many


Что означает принцип "Build Once, Deploy Many"?

A) Один artifact используется для всех environments (dev, staging, prod)

B) Использовать один сервер для всех сред

C) Деплоить только один раз

D) Собирать отдельный artifact для каждого environment

---

## Question 14: Configuration Management


Как правильно управлять конфигурацией для разных environments?

A) Разделять config от кода, использовать environment variables

B) Хардкодить в приложении

C) Создавать отдельную версию кода для каждого environment

D) Хранить в коде в зашифрованном виде

---

## Question 15: Readiness Probe


Для чего используется readinessProbe в Kubernetes?

A) Для масштабирования

B) Для логирования

C) Для определения, готов ли pod принимать трафик

D) Для проверки, что pod жив

---

## Question 16: Canary Analysis


На основе чего Canary deployment принимает решение о продолжении или rollback?

A) Времени суток

B) Метрик (error rate, latency) новой версии

C) Размера Docker image

D) Количества пользователей

---

## Question 17: Feature Flag Best Practices


Что следует делать со старыми feature flags?

A) Дублировать

B) Переименовывать

C) Удалять после полного rollout и стабилизации

D) Оставлять навсегда

---

## Question 18: Progressive Delivery


Что такое Progressive Delivery?

A) Деплой только по выходным

B) Постепенный rollout с автоматической проверкой метрик

C) Деплой без тестов

D) Ручной деплой

---

## Question 19: Liveness vs Readiness Probe


В чём разница между livenessProbe и readinessProbe?

A) livenessProbe перезапускает pod при сбое, readinessProbe убирает из балансировки

B) Оба только логируют

C) Оба перезапускают pod

D) Это одно и то же

---

## Question 20: Post-Deployment Verification


Что проверяется сразу после деплоя (0-5 минут)?

A) Только логи

B) Количество пользователей за месяц

C) Финансовые показатели

D) Error rate, response time, health endpoints

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | CD = всегда готовы к релизу (ручной trigger), Continuous Deployment = автоматический релиз |
| 2 | C | Blue-Green позволяет мгновенно переключить трафик обратно на blue при проблемах |
| 3 | B | Canary постепенно увеличивает трафик на новую версию, проверяя метрики |
| 4 | C | Rolling update постепенно заменяет pods, обеспечивая zero downtime |
| 5 | C | Feature flags позволяют включать/выключать функции без нового деплоя |
| 6 | D | Experiment toggle используется для A/B тестов с разными вариантами |
| 7 | B | Expand-Contract: добавляем новое → мигрируем → удаляем старое |
| 8 | C | Rollback при критических проблемах: высокий error rate, сбои, data issues |
| 9 | C | Environments должны быть похожи для предсказуемого поведения |
| 10 | A | Smoke tests проверяют базовую работоспособность сразу после деплоя |
| 11 | D | Blue-Green: instant rollback, но требует 2x ресурсов |
| 12 | C | Recreate приемлем для dev/test или при breaking changes |
| 13 | A | Один artifact проходит через все environments |
| 14 | A | Config отделён от кода, передаётся через env vars |
| 15 | C | readinessProbe определяет, готов ли pod к трафику |
| 16 | B | Canary анализирует метрики для принятия решения о rollout/rollback |
| 17 | C | Старые flags нужно удалять, иначе накапливается технический долг |
| 18 | B | Progressive delivery = постепенный rollout с автоматическими проверками |
| 19 | A | liveness = жив ли pod (restart), readiness = готов ли к трафику |
| 20 | D | Сразу после деплоя проверяем error rate, latency, health |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете CD. Переходите к IaC. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите deployment strategies и feature flags. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о Canary и Blue-Green. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все стратегии развёртывания. |

---

