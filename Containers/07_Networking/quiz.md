# Container Networking - Quiz

Проверьте свои знания по теме "Сетевая подсистема контейнеров".

---

## Question 1: Дефолтный режим

Какой сетевой режим используется Docker по умолчанию?

A) host

B) bridge

C) none

D) overlay

---

## Question 2: veth pairs

Что такое veth pair?

A) Виртуальный роутер

B) Виртуальный Ethernet кабель между namespaces

C) Тип шифрования

D) DNS сервер

---

## Question 3: Host network

Какое преимущество даёт режим host network?

A) Лучшая изоляция

B) Максимальная производительность без NAT

C) Автоматический DNS

D) Overlay networking

---

## Question 4: Port mapping

Какая команда опубликует порт 80 контейнера на порт 8080 хоста?

A) docker run -p 80:8080 nginx

B) docker run -p 8080:80 nginx

C) docker run --port 8080=80 nginx

D) docker run -P 8080:80 nginx

---

## Question 5: User-defined networks

Какое преимущество user-defined networks перед default bridge?

A) Быстрее работает

B) Встроенный DNS для discovery по имени контейнера

C) Меньше потребление памяти

D) Поддержка IPv6

---

## Question 6: CNI

Что такое CNI?

A) Container Network Isolation

B) Container Network Interface

C) Container Name Index

D) Container Node Integration

---

## Question 7: Overlay networks

Для чего нужны overlay networks?

A) Шифрование трафика

B) Связь контейнеров на разных хостах

C) Ускорение локальной сети

D) Изоляция от интернета

---

## Question 8: VXLAN

На каком порту работает VXLAN по умолчанию?

A) 443

B) 8080

C) 4789

D) 2375

---

## Question 9: Internal network

Что особенного в internal network Docker?

A) Более высокая скорость

B) Контейнеры не имеют доступа к внешней сети

C) Шифрование трафика

D) Автоматическое масштабирование

---

## Question 10: docker0

Что такое docker0?

A) Первый контейнер

B) Виртуальный bridge для default network

C) DNS сервер Docker

D) Конфигурационный файл

---

## Question 11: Embedded DNS

На каком IP работает встроенный DNS Docker?

A) 127.0.0.1

B) 127.0.0.11

C) 172.17.0.1

D) 8.8.8.8

---

## Question 12: Network aliases

Для чего используются network aliases?

A) Шифрование имён

B) Несколько DNS имён для одного контейнера

C) Изоляция сетей

D) Мониторинг

---

## Question 13: Macvlan

Когда следует использовать macvlan driver?

A) Для overlay сетей

B) Когда контейнеру нужен IP из физической сети

C) Для изоляции контейнеров

D) Для DNS

---

## Question 14: iptables

Как Docker использует iptables?

A) Для DNS резолвинга

B) Для NAT и port forwarding

C) Для хранения данных

D) Для аутентификации

---

## Question 15: Container network mode

Как запустить контейнер в network namespace другого контейнера?

A) --network shared:other

B) --network container:other

C) --network=other

D) --net-alias other

---

## Question 16: Kubernetes CNI

Какой CNI plugin использует eBPF для высокой производительности?

A) Flannel

B) Calico

C) Cilium

D) Weave

---

## Question 17: Network isolation

Контейнеры в разных user-defined networks могут общаться?

A) Да, всегда

B) Нет, если не подключены к общей сети

C) Только через DNS

D) Только по IP

---

## Question 18: Диагностика

Какой инструмент лучше всего подходит для диагностики сети контейнера?

A) docker logs

B) docker stats

C) netshoot контейнер

D) docker info

---

## Question 19: Subnet

Какой параметр задаёт подсеть при создании Docker network?

A) --ip-range

B) --subnet

C) --network

D) --cidr

---

## Question 20: Multi-network

Можно ли подключить контейнер к нескольким сетям?

A) Нет

B) Да, через docker network connect

C) Только при создании

D) Только в Swarm mode

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Bridge — дефолтный сетевой режим Docker |
| 2 | B | veth pair — виртуальный Ethernet кабель, связывающий namespaces |
| 3 | B | Host network даёт максимальную производительность без NAT overhead |
| 4 | B | Формат: -p HOST:CONTAINER, поэтому -p 8080:80 |
| 5 | B | User-defined networks имеют встроенный DNS для discovery |
| 6 | B | CNI — Container Network Interface, стандарт для сетевых плагинов |
| 7 | B | Overlay networks позволяют контейнерам на разных хостах общаться |
| 8 | C | VXLAN использует UDP порт 4789 |
| 9 | B | Internal network не имеет доступа к внешним сетям |
| 10 | B | docker0 — виртуальный bridge для default bridge network |
| 11 | B | Встроенный DNS Docker работает на 127.0.0.11 |
| 12 | B | Network aliases позволяют одному контейнеру иметь несколько DNS имён |
| 13 | B | Macvlan даёт контейнеру IP из физической сети |
| 14 | B | Docker использует iptables для NAT и port forwarding |
| 15 | B | --network container:name делит network namespace |
| 16 | C | Cilium использует eBPF для networking и security |
| 17 | B | Контейнеры в разных сетях изолированы, нужна общая сеть |
| 18 | C | netshoot содержит все инструменты для сетевой диагностики |
| 19 | B | --subnet задаёт подсеть при создании сети |
| 20 | B | docker network connect подключает к дополнительным сетям |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете container networking. Переходите к Docker. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про CNI и overlay networks. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про сетевые режимы и DNS. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с разными сетевыми режимами Docker. |

---

