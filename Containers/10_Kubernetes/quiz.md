# Kubernetes - Quiz

Проверьте свои знания по теме "Введение в оркестрацию контейнеров".

---

## Question 1: Минимальная единица

Что является минимальной единицей развёртывания в Kubernetes?

A) Container

B) Pod

C) Deployment

D) Service

---

## Question 2: Control Plane

Какой компонент хранит всё состояние кластера?

A) API Server

B) Scheduler

C) etcd

D) Controller Manager

---

## Question 3: kubelet

Какова роль kubelet?

A) Балансировка нагрузки

B) Управление жизненным циклом Pods на ноде

C) Хранение конфигурации

D) Маршрутизация трафика

---

## Question 4: Service Types

Какой тип Service создаёт внешний load balancer в cloud?

A) ClusterIP

B) NodePort

C) LoadBalancer

D) ExternalName

---

## Question 5: Deployment

Что обеспечивает Deployment?

A) Хранение данных

B) Сетевую изоляцию

C) Декларативные обновления и ReplicaSet

D) DNS резолвинг

---

## Question 6: kubectl apply

Что делает команда kubectl apply -f manifest.yaml?

A) Удаляет ресурсы из файла

B) Создаёт или обновляет ресурсы из файла

C) Валидирует файл без применения

D) Показывает diff между файлом и кластером

---

## Question 7: ConfigMap

Для чего используется ConfigMap?

A) Хранение чувствительных данных

B) Хранение конфигурации (не секретной)

C) Хранение образов

D) Хранение volumes

---

## Question 8: Secret

В каком формате хранятся данные в Secret по умолчанию?

A) Plain text

B) Base64 encoded

C) Encrypted

D) Hashed

---

## Question 9: Namespace

Как получить Pods из всех namespaces?

A) kubectl get pods --all

B) kubectl get pods -A

C) kubectl get pods *

D) kubectl get pods --global

---

## Question 10: Rolling Update

Какой параметр определяет максимальное количество недоступных Pods при обновлении?

A) maxSurge

B) maxUnavailable

C) minAvailable

D) updateBatch

---

## Question 11: Probes

Какой probe проверяет готовность Pod принимать трафик?

A) livenessProbe

B) readinessProbe

C) startupProbe

D) healthProbe

---

## Question 12: PersistentVolumeClaim

Что делает PersistentVolumeClaim?

A) Создаёт физическое хранилище

B) Запрашивает storage у PersistentVolume

C) Удаляет данные при удалении Pod

D) Шифрует данные

---

## Question 13: Labels и Selectors

Как Service находит Pods для маршрутизации?

A) По имени Pod

B) По IP адресу

C) По selector, соответствующему labels

D) По namespace

---

## Question 14: DNS в Kubernetes

Какой формат DNS имени для Service в namespace production?

A) service.production

B) service.production.cluster

C) service.production.svc.cluster.local

D) production.service.k8s

---

## Question 15: Ingress

Для чего используется Ingress?

A) Внутренняя маршрутизация между Pods

B) HTTP/HTTPS маршрутизация извне в кластер

C) Хранение секретов

D) Мониторинг

---

## Question 16: Resource limits

Как ограничить Pod использованием максимум 512Mi памяти?

A) memory: 512Mi

B) limits.memory: 512Mi

C) resources.limits.memory: "512Mi"

D) maxMemory: 512Mi

---

## Question 17: kubectl exec

Как выполнить интерактивную команду sh в Pod?

A) kubectl run pod sh

B) kubectl exec -it pod -- sh

C) kubectl shell pod

D) kubectl connect pod sh

---

## Question 18: ReplicaSet

Кто управляет ReplicaSet?

A) Pod

B) Deployment

C) Service

D) kubelet

---

## Question 19: Port Forward

Как прокинуть порт 8080 локально на порт 80 Pod'а?

A) kubectl forward 8080:80 pod

B) kubectl port-forward pod/name 8080:80

C) kubectl proxy 8080:80 pod

D) kubectl tunnel 8080:80 pod

---

## Question 20: Network Policy

Для чего используется NetworkPolicy?

A) Настройка DNS

B) Ограничение сетевого трафика между Pods

C) Балансировка нагрузки

D) Шифрование трафика

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Pod — минимальная единица развёртывания, может содержать несколько контейнеров |
| 2 | C | etcd — распределённое хранилище для всего состояния кластера |
| 3 | B | kubelet — агент на каждой ноде, управляет жизненным циклом Pods |
| 4 | C | LoadBalancer создаёт внешний LB в cloud-провайдерах |
| 5 | C | Deployment управляет ReplicaSet и обеспечивает декларативные обновления |
| 6 | B | apply создаёт ресурсы или обновляет существующие |
| 7 | B | ConfigMap хранит конфигурацию в виде key-value пар |
| 8 | B | Данные в Secret хранятся в base64 (не шифруются по умолчанию) |
| 9 | B | -A или --all-namespaces показывает ресурсы из всех namespaces |
| 10 | B | maxUnavailable определяет максимальное количество недоступных Pods |
| 11 | B | readinessProbe определяет готовность Pod принимать трафик |
| 12 | B | PVC запрашивает storage, который предоставляет PV |
| 13 | C | Service использует selector для поиска Pods по labels |
| 14 | C | Полный DNS: service.namespace.svc.cluster.local |
| 15 | B | Ingress обеспечивает HTTP/HTTPS маршрутизацию извне |
| 16 | C | resources.limits.memory: "512Mi" в spec контейнера |
| 17 | B | kubectl exec -it pod -- sh для интерактивной команды |
| 18 | B | Deployment создаёт и управляет ReplicaSet |
| 19 | B | kubectl port-forward pod/name localPort:podPort |
| 20 | B | NetworkPolicy ограничивает ingress/egress трафик между Pods |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете Kubernetes. Готовы к production! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Services и Storage. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про архитектуру и основные ресурсы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с Minikube или kind. |

---


