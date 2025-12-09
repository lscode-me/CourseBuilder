# Container Networking - Quiz

Проверьте свои знания по теме "Сетевая подсистема контейнеров".

---

## Question 1: Дефолтный режим





Какой сетевой режим используется Docker по умолчанию?

A) none

B) host

C) overlay

D) bridge

---

## Question 2: veth pairs





Что такое veth pair?

A) Виртуальный роутер

B) DNS сервер

C) Тип шифрования

D) Виртуальный Ethernet кабель между namespaces

---

## Question 3: Host network





Какое преимущество даёт режим host network?

A) Автоматический DNS

B) Overlay networking

C) Лучшая изоляция

D) Максимальная производительность без NAT

---

## Question 4: Port mapping





Какая команда опубликует порт 80 контейнера на порт 8080 хоста?

A) docker run -p 8080:80 nginx

B) docker run -P 8080:80 nginx

C) docker run -p 80:8080 nginx

D) docker run --port 8080=80 nginx

---

## Question 5: User-defined networks





Какое преимущество user-defined networks перед default bridge?

A) Меньше потребление памяти

B) Встроенный DNS для discovery по имени контейнера

C) Быстрее работает

D) Поддержка IPv6

---

## Question 6: CNI





Что такое CNI?

A) Container Name Index

B) Container Node Integration

C) Container Network Isolation

D) Container Network Interface

---

## Question 7: Overlay networks





Для чего нужны overlay networks?

A) Изоляция от интернета

B) Связь контейнеров на разных хостах

C) Шифрование трафика

D) Ускорение локальной сети

---

## Question 8: VXLAN





На каком порту работает VXLAN по умолчанию?

A) 2375

B) 4789

C) 443

D) 8080

---

## Question 9: Internal network





Что особенного в internal network Docker?

A) Более высокая скорость

B) Шифрование трафика

C) Контейнеры не имеют доступа к внешней сети

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

C) 8.8.8.8

D) 172.17.0.1

---

## Question 12: Network aliases





Для чего используются network aliases?

A) Мониторинг

B) Несколько DNS имён для одного контейнера

C) Изоляция сетей

D) Шифрование имён

---

## Question 13: Macvlan





Когда следует использовать macvlan driver?

A) Для изоляции контейнеров

B) Для DNS

C) Для overlay сетей

D) Когда контейнеру нужен IP из физической сети

---

## Question 14: iptables





Как Docker использует iptables?

A) Для аутентификации

B) Для DNS резолвинга

C) Для хранения данных

D) Для NAT и port forwarding

---

## Question 15: Container network mode





Как запустить контейнер в network namespace другого контейнера?

A) --network container:other

B) --network=other

C) --network shared:other

D) --net-alias other

---

## Question 16: Kubernetes CNI





Какой CNI plugin использует eBPF для высокой производительности?

A) Calico

B) Flannel

C) Cilium

D) Weave

---

## Question 17: Network isolation





Контейнеры в разных user-defined networks могут общаться?

A) Только через DNS

B) Да, всегда

C) Нет, если не подключены к общей сети

D) Только по IP

---

## Question 18: Диагностика





Какой инструмент лучше всего подходит для диагностики сети контейнера?

A) docker stats

B) netshoot контейнер

C) docker info

D) docker logs

---

## Question 19: Subnet





Какой параметр задаёт подсеть при создании Docker network?

A) --subnet

B) --cidr

C) --network

D) --ip-range

---

## Question 20: Multi-network





Можно ли подключить контейнер к нескольким сетям?

A) Да, через docker network connect

B) Только при создании

C) Только в Swarm mode

D) Нет

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Bridge — дефолтный сетевой режим Docker |
| 2 | D | veth pair — виртуальный Ethernet кабель, связывающий namespaces |
| 3 | D | Host network даёт максимальную производительность без NAT overhead |
| 4 | A | Формат: -p HOST:CONTAINER, поэтому -p 8080:80 |
| 5 | B | User-defined networks имеют встроенный DNS для discovery |
| 6 | D | CNI — Container Network Interface, стандарт для сетевых плагинов |
| 7 | B | Overlay networks позволяют контейнерам на разных хостах общаться |
| 8 | B | VXLAN использует UDP порт 4789 |
| 9 | C | Internal network не имеет доступа к внешним сетям |
| 10 | B | docker0 — виртуальный bridge для default bridge network |
| 11 | B | Встроенный DNS Docker работает на 127.0.0.11 |
| 12 | B | Network aliases позволяют одному контейнеру иметь несколько DNS имён |
| 13 | D | Macvlan даёт контейнеру IP из физической сети |
| 14 | D | Docker использует iptables для NAT и port forwarding |
| 15 | A | --network container:name делит network namespace |
| 16 | C | Cilium использует eBPF для networking и security |
| 17 | C | Контейнеры в разных сетях изолированы, нужна общая сеть |
| 18 | B | netshoot содержит все инструменты для сетевой диагностики |
| 19 | A | --subnet задаёт подсеть при создании сети |
| 20 | A | docker network connect подключает к дополнительным сетям |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете container networking. Переходите к Docker. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про CNI и overlay networks. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про сетевые режимы и DNS. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с разными сетевыми режимами Docker. |

---

