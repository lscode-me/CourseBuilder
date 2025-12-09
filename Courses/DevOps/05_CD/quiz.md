# Continuous Delivery и Deployment - Quiz

Проверьте свои знания по CD, стратегиям развёртывания и feature flags.

---

## Question 1: CD vs Continuous Deployment







Чем Continuous Delivery отличается от Continuous Deployment?

A) В CD финальный деплой в production ручной, в Continuous Deployment — автоматический

B) CD не требует автоматических тестов

C) Continuous Deployment проще в реализации

D) Это одно и то же

---

## Question 2: Blue-Green Deployment







Какое главное преимущество Blue-Green deployment?

A) Мгновенный rollback

B) Требует меньше ресурсов

C) Автоматическое тестирование

D) Не требует load balancer

---

## Question 3: Canary Deployment







Что характеризует Canary deployment?

A) Весь трафик сразу идёт на новую версию

B) Две идентичные среды

C) Постепенное направление трафика на новую версию (10% → 25% → 50% → 100%)

D) Полный downtime при деплое

---

## Question 4: Rolling Update







Что происходит при Rolling Update в Kubernetes?

A) Требуется ручной restart каждого pod

B) Pods постепенно заменяются новыми версиями

C) Все pods останавливаются, затем запускаются новые

D) Создаётся копия всего cluster

---

## Question 5: Feature Flags







Для чего используются feature flags?

A) Для шифрования кода

B) Для логирования

C) Для мониторинга

D) Для включения/выключения функционала без деплоя

---

## Question 6: Feature Flag Types







Какой тип feature flag используется для A/B тестирования?

A) Permission toggle

B) Experiment toggle

C) Release toggle

D) Ops toggle

---

## Question 7: Database Migrations







Какой подход обеспечивает zero-downtime database migration?

A) Остановить приложение на время миграции

B) Expand-Contract pattern (добавить новое, мигрировать, удалить старое)

C) Использовать только NoSQL базы

D) Удалить таблицу и создать заново

---

## Question 8: Rollback







Когда следует выполнять rollback?

A) После каждого деплоя

B) Только по запросу менеджмента

C) Никогда — всегда делать forward fix

D) При error rate > threshold, критических сбоях, data corruption

---

## Question 9: Environment Parity







Что означает принцип Environment Parity?

A) Dev, staging и production environments должны быть максимально похожи

B) Environments должны быть в разных регионах

C) Все environments должны иметь одинаковые пароли

D) Использовать только один environment

---

## Question 10: Smoke Tests







Когда выполняются smoke tests?

A) Только в development

B) Перед написанием кода

C) Сразу после деплоя для проверки базовой работоспособности

D) Раз в месяц

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

A) Для dev/test environments или при несовместимых изменениях

B) Когда downtime недопустим

C) Всегда

D) Для production с высоким SLA

---

## Question 13: Build Once Deploy Many







Что означает принцип "Build Once, Deploy Many"?

A) Один artifact используется для всех environments (dev, staging, prod)

B) Деплоить только один раз

C) Использовать один сервер для всех сред

D) Собирать отдельный artifact для каждого environment

---

## Question 14: Configuration Management







Как правильно управлять конфигурацией для разных environments?

A) Хранить в коде в зашифрованном виде

B) Разделять config от кода, использовать environment variables

C) Создавать отдельную версию кода для каждого environment

D) Хардкодить в приложении

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

B) Размера Docker image

C) Количества пользователей

D) Метрик (error rate, latency) новой версии

---

## Question 17: Feature Flag Best Practices







Что следует делать со старыми feature flags?

A) Переименовывать

B) Дублировать

C) Оставлять навсегда

D) Удалять после полного rollout и стабилизации

---

## Question 18: Progressive Delivery







Что такое Progressive Delivery?

A) Ручной деплой

B) Постепенный rollout с автоматической проверкой метрик

C) Деплой без тестов

D) Деплой только по выходным

---

## Question 19: Liveness vs Readiness Probe







В чём разница между livenessProbe и readinessProbe?

A) Оба перезапускают pod

B) Оба только логируют

C) Это одно и то же

D) livenessProbe перезапускает pod при сбое, readinessProbe убирает из балансировки

---

## Question 20: Post-Deployment Verification







Что проверяется сразу после деплоя (0-5 минут)?

A) Финансовые показатели

B) Только логи

C) Error rate, response time, health endpoints

D) Количество пользователей за месяц

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | CD = всегда готовы к релизу (ручной trigger), Continuous Deployment = автоматический релиз |
| 2 | A | Blue-Green позволяет мгновенно переключить трафик обратно на blue при проблемах |
| 3 | C | Canary постепенно увеличивает трафик на новую версию, проверяя метрики |
| 4 | B | Rolling update постепенно заменяет pods, обеспечивая zero downtime |
| 5 | D | Feature flags позволяют включать/выключать функции без нового деплоя |
| 6 | B | Experiment toggle используется для A/B тестов с разными вариантами |
| 7 | B | Expand-Contract: добавляем новое → мигрируем → удаляем старое |
| 8 | D | Rollback при критических проблемах: высокий error rate, сбои, data issues |
| 9 | A | Environments должны быть похожи для предсказуемого поведения |
| 10 | C | Smoke tests проверяют базовую работоспособность сразу после деплоя |
| 11 | C | Blue-Green: instant rollback, но требует 2x ресурсов |
| 12 | A | Recreate приемлем для dev/test или при breaking changes |
| 13 | A | Один artifact проходит через все environments |
| 14 | B | Config отделён от кода, передаётся через env vars |
| 15 | C | readinessProbe определяет, готов ли pod к трафику |
| 16 | D | Canary анализирует метрики для принятия решения о rollout/rollback |
| 17 | D | Старые flags нужно удалять, иначе накапливается технический долг |
| 18 | B | Progressive delivery = постепенный rollout с автоматическими проверками |
| 19 | D | liveness = жив ли pod (restart), readiness = готов ли к трафику |
| 20 | C | Сразу после деплоя проверяем error rate, latency, health |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете CD. Переходите к IaC. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите deployment strategies и feature flags. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о Canary и Blue-Green. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все стратегии развёртывания. |

---

