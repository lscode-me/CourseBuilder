# Kubernetes - Quiz

Проверьте свои знания по теме "Введение в оркестрацию контейнеров".

---

## Question 1: Минимальная единица


Что является минимальной единицей развёртывания в Kubernetes?

A) Container

B) Service

C) Pod

D) Deployment

---

## Question 2: Control Plane


Какой компонент хранит всё состояние кластера?

A) Scheduler

B) API Server

C) etcd

D) Controller Manager

---

## Question 3: kubelet


Какова роль kubelet?

A) Хранение конфигурации

B) Управление жизненным циклом Pods на ноде

C) Балансировка нагрузки

D) Маршрутизация трафика

---

## Question 4: Service Types


Какой тип Service создаёт внешний load balancer в cloud?

A) LoadBalancer

B) ClusterIP

C) NodePort

D) ExternalName

---

## Question 5: Deployment


Что обеспечивает Deployment?

A) Хранение данных

B) Декларативные обновления и ReplicaSet

C) Сетевую изоляцию

D) DNS резолвинг

---

## Question 6: kubectl apply


Что делает команда kubectl apply -f manifest.yaml?

A) Валидирует файл без применения

B) Удаляет ресурсы из файла

C) Показывает diff между файлом и кластером

D) Создаёт или обновляет ресурсы из файла

---

## Question 7: ConfigMap


Для чего используется ConfigMap?

A) Хранение образов

B) Хранение volumes

C) Хранение конфигурации (не секретной)

D) Хранение чувствительных данных

---

## Question 8: Secret


В каком формате хранятся данные в Secret по умолчанию?

A) Hashed

B) Base64 encoded

C) Encrypted

D) Plain text

---

## Question 9: Namespace


Как получить Pods из всех namespaces?

A) kubectl get pods *

B) kubectl get pods --all

C) kubectl get pods --global

D) kubectl get pods -A

---

## Question 10: Rolling Update


Какой параметр определяет максимальное количество недоступных Pods при обновлении?

A) updateBatch

B) minAvailable

C) maxUnavailable

D) maxSurge

---

## Question 11: Probes


Какой probe проверяет готовность Pod принимать трафик?

A) healthProbe

B) readinessProbe

C) livenessProbe

D) startupProbe

---

## Question 12: PersistentVolumeClaim


Что делает PersistentVolumeClaim?

A) Создаёт физическое хранилище

B) Шифрует данные

C) Запрашивает storage у PersistentVolume

D) Удаляет данные при удалении Pod

---

## Question 13: Labels и Selectors


Как Service находит Pods для маршрутизации?

A) По имени Pod

B) По namespace

C) По IP адресу

D) По selector, соответствующему labels

---

## Question 14: DNS в Kubernetes


Какой формат DNS имени для Service в namespace production?

A) service.production.svc.cluster.local

B) production.service.k8s

C) service.production.cluster

D) service.production

---

## Question 15: Ingress


Для чего используется Ingress?

A) Хранение секретов

B) Мониторинг

C) HTTP/HTTPS маршрутизация извне в кластер

D) Внутренняя маршрутизация между Pods

---

## Question 16: Resource limits


Как ограничить Pod использованием максимум 512Mi памяти?

A) limits.memory: 512Mi

B) maxMemory: 512Mi

C) resources.limits.memory: "512Mi"

D) memory: 512Mi

---

## Question 17: kubectl exec


Как выполнить интерактивную команду sh в Pod?

A) kubectl exec -it pod -- sh

B) kubectl shell pod

C) kubectl connect pod sh

D) kubectl run pod sh

---

## Question 18: ReplicaSet


Кто управляет ReplicaSet?

A) Deployment

B) kubelet

C) Service

D) Pod

---

## Question 19: Port Forward


Как прокинуть порт 8080 локально на порт 80 Pod'а?

A) kubectl proxy 8080:80 pod

B) kubectl tunnel 8080:80 pod

C) kubectl forward 8080:80 pod

D) kubectl port-forward pod/name 8080:80

---

## Question 20: Network Policy


Для чего используется NetworkPolicy?

A) Ограничение сетевого трафика между Pods

B) Шифрование трафика

C) Балансировка нагрузки

D) Настройка DNS

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Pod — минимальная единица развёртывания, может содержать несколько контейнеров |
| 2 | C | etcd — распределённое хранилище для всего состояния кластера |
| 3 | B | kubelet — агент на каждой ноде, управляет жизненным циклом Pods |
| 4 | A | LoadBalancer создаёт внешний LB в cloud-провайдерах |
| 5 | B | Deployment управляет ReplicaSet и обеспечивает декларативные обновления |
| 6 | D | apply создаёт ресурсы или обновляет существующие |
| 7 | C | ConfigMap хранит конфигурацию в виде key-value пар |
| 8 | B | Данные в Secret хранятся в base64 (не шифруются по умолчанию) |
| 9 | D | -A или --all-namespaces показывает ресурсы из всех namespaces |
| 10 | C | maxUnavailable определяет максимальное количество недоступных Pods |
| 11 | B | readinessProbe определяет готовность Pod принимать трафик |
| 12 | C | PVC запрашивает storage, который предоставляет PV |
| 13 | D | Service использует selector для поиска Pods по labels |
| 14 | A | Полный DNS: service.namespace.svc.cluster.local |
| 15 | C | Ingress обеспечивает HTTP/HTTPS маршрутизацию извне |
| 16 | C | resources.limits.memory: "512Mi" в spec контейнера |
| 17 | A | kubectl exec -it pod -- sh для интерактивной команды |
| 18 | A | Deployment создаёт и управляет ReplicaSet |
| 19 | D | kubectl port-forward pod/name localPort:podPort |
| 20 | A | NetworkPolicy ограничивает ingress/egress трафик между Pods |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете Kubernetes. Готовы к production! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Services и Storage. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про архитектуру и основные ресурсы. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с Minikube или kind. |

---


