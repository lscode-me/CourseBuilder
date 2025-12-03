# Container Networking
## Сетевая подсистема контейнеров

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать Linux network namespaces
- Знать базовые концепции сетей (IP, routing, NAT)
- Иметь опыт работы с Docker или Podman

**Recommended prior modules:**
- [Linux Namespaces](../02_Namespaces/) — network namespace
- [Container Runtimes](../06_Runtimes/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснить модели сетевого взаимодействия контейнеров
- Настраивать сеть контейнеров через CNI plugins
- Создавать пользовательские сети в Docker и Podman
- Диагностировать сетевые проблемы контейнеров

---

## 1. Основы Container Networking

### 1.1 Сетевые требования контейнеров

Контейнеры нуждаются в сетевых возможностях:
- Изоляция сетевого стека (network namespace)
- Связь контейнеров между собой
- Связь с хост-системой
- Доступ к внешней сети (интернет)
- Публикация портов для внешнего доступа

### 1.2 Компоненты сетевой изоляции

```
┌─────────────────────────────────────────────────────────────┐
│                    Host Network Stack                        │
│                                                              │
│  eth0: 192.168.1.100                                        │
│  docker0: 172.17.0.1                                         │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Network Namespace                       │    │
│  │              (Container)                             │    │
│  │                                                      │    │
│  │  eth0 (veth): 172.17.0.2                            │    │
│  │  lo: 127.0.0.1                                       │    │
│  │                                                      │    │
│  │  Routing table, iptables, sockets                   │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│                    veth pair                                 │
│                         │                                    │
└─────────────────────────┴───────────────────────────────────┘
```

### 1.3 Сетевые примитивы Linux

| Примитив | Назначение |
|----------|------------|
| Network namespace | Изоляция сетевого стека |
| veth pair | Виртуальный Ethernet кабель |
| Bridge | Виртуальный коммутатор |
| VXLAN | Overlay сеть |
| iptables/nftables | Firewall и NAT |
| ip route | Маршрутизация |
| IPVS | Load balancing |

---

## 2. Сетевые режимы Docker

### 2.1 Bridge Network (default)

Дефолтный режим — контейнеры подключаются к виртуальному мосту:

```
┌──────────────────────────────────────────────────────────┐
│                          Host                             │
│                                                           │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│  │Container│    │Container│    │Container│              │
│  │   A     │    │   B     │    │   C     │              │
│  │172.17.0.2│   │172.17.0.3│   │172.17.0.4│             │
│  └────┬────┘    └────┬────┘    └────┬────┘              │
│       │              │              │                    │
│  ┌────┴──────────────┴──────────────┴────┐              │
│  │             docker0 bridge            │              │
│  │              172.17.0.1               │              │
│  └───────────────────┬───────────────────┘              │
│                      │                                   │
│                   iptables NAT                           │
│                      │                                   │
│               ┌──────┴──────┐                           │
│               │    eth0     │                           │
│               │192.168.1.100│                           │
│               └─────────────┘                           │
└──────────────────────────────────────────────────────────┘
```

```bash
# Запуск контейнера в bridge network
docker run -d --name web nginx

# Проверка сети
docker inspect web --format '{{.NetworkSettings.IPAddress}}'
```

**Output:**
```
172.17.0.2
```

```bash
# Проверка bridge на хосте
ip link show docker0
brctl show docker0
```

### 2.2 Host Network

Контейнер использует сетевой стек хоста напрямую:

```bash
# Запуск с host networking
docker run -d --name web --network host nginx

# Контейнер использует порты хоста напрямую
curl localhost:80
```

**Преимущества:**
- Максимальная производительность
- Нет NAT overhead

**Недостатки:**
- Нет сетевой изоляции
- Конфликты портов
- Меньше безопасности

### 2.3 None Network

Контейнер без сети (только loopback):

```bash
docker run -d --name isolated --network none alpine sleep 3600

docker exec isolated ip link
```

**Output:**
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
```

### 2.4 Container Network

Разделение network namespace с другим контейнером:

```bash
# Создаём первый контейнер
docker run -d --name main nginx

# Второй контейнер использует сеть первого
docker run --rm --network container:main alpine wget -qO- localhost:80
```

### 2.5 User-defined Networks

Создание собственных сетей с DNS и изоляцией:

```bash
# Создание сети
docker network create --driver bridge --subnet 10.10.0.0/16 mynetwork

# Запуск контейнеров в сети
docker run -d --name web --network mynetwork nginx
docker run -d --name app --network mynetwork alpine sleep 3600

# Контейнеры могут обращаться по имени (встроенный DNS)
docker exec app ping web
```

**Output:**
```
PING web (10.10.0.2): 56 data bytes
64 bytes from 10.10.0.2: seq=0 ttl=64 time=0.123 ms
```

---

## 3. Публикация портов

### 3.1 Port Mapping

```bash
# Публикация порта: host:container
docker run -d -p 8080:80 nginx

# Только localhost
docker run -d -p 127.0.0.1:8080:80 nginx

# Случайный порт хоста
docker run -d -p 80 nginx
docker port <container>
```

### 3.2 Как работает port publishing

```bash
# Docker создаёт правила iptables
sudo iptables -t nat -L -n | grep 8080
```

**Output:**
```
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:8080 to:172.17.0.2:80
```

```bash
# Проверка DOCKER chain
sudo iptables -t nat -L DOCKER -n --line-numbers
```

### 3.3 Port ranges

```bash
# Публикация диапазона портов
docker run -d -p 8080-8090:80-90 myapp

# UDP порты
docker run -d -p 53:53/udp dns-server
```

---

## 4. CNI — Container Network Interface

### 4.1 Что такое CNI

CNI — стандартный интерфейс для настройки сети контейнеров:

```
┌────────────────────────────────────────────────────────┐
│                Container Runtime                        │
│              (Kubernetes, Podman, etc.)                 │
└────────────────────────────┬───────────────────────────┘
                             │ CNI Protocol
                             ▼
┌────────────────────────────────────────────────────────┐
│                    CNI Plugin                           │
│      (bridge, macvlan, calico, flannel, etc.)          │
└────────────────────────────────────────────────────────┘
```

### 4.2 Структура CNI конфигурации

```json
{
    "cniVersion": "1.0.0",
    "name": "mynetwork",
    "type": "bridge",
    "bridge": "cni0",
    "isGateway": true,
    "ipMasq": true,
    "ipam": {
        "type": "host-local",
        "subnet": "10.88.0.0/16",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ]
    }
}
```

### 4.3 Основные CNI плагины

| Plugin | Назначение |
|--------|------------|
| bridge | L2 bridge networking |
| macvlan | Прямое подключение к физической сети |
| ipvlan | L2/L3 виртуализация |
| ptp | Point-to-point соединение |
| host-local | IPAM — локальное выделение IP |
| dhcp | IPAM — через DHCP |
| portmap | Port mapping (NAT) |
| firewall | iptables правила |

### 4.4 Использование CNI вручную

```bash
# Установка CNI плагинов
curl -LO https://github.com/containernetworking/plugins/releases/download/v1.3.0/cni-plugins-linux-amd64-v1.3.0.tgz
mkdir -p /opt/cni/bin
tar -xzf cni-plugins-linux-amd64-v1.3.0.tgz -C /opt/cni/bin

# Конфигурация
mkdir -p /etc/cni/net.d
cat > /etc/cni/net.d/10-mynet.conf << 'EOF'
{
    "cniVersion": "1.0.0",
    "name": "mynet",
    "type": "bridge",
    "bridge": "cni0",
    "isGateway": true,
    "ipMasq": true,
    "ipam": {
        "type": "host-local",
        "subnet": "10.22.0.0/16",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ]
    }
}
EOF

# Создание network namespace
ip netns add test-ns

# Вызов CNI плагина
CNI_PATH=/opt/cni/bin \
CNI_CONTAINERID=test-container \
CNI_NETNS=/var/run/netns/test-ns \
CNI_IFNAME=eth0 \
CNI_COMMAND=ADD \
/opt/cni/bin/bridge < /etc/cni/net.d/10-mynet.conf

# Проверка
ip netns exec test-ns ip addr
```

---

## 5. Overlay Networks

Overlay networks позволяют контейнерам на разных хостах общаться через L2.

### 5.1 VXLAN — основа overlay

```
┌───────────────────────────────────────────────────────────┐
│                        Host A                              │
│                                                            │
│  Container A1      Container A2                           │
│  ┌─────────┐       ┌─────────┐                           │
│  │10.0.0.2 │       │10.0.0.3 │                           │
│  └────┬────┘       └────┬────┘                           │
│       │                 │                                 │
│  ┌────┴─────────────────┴────┐                           │
│  │       VXLAN Interface     │                           │
│  │         vtep0             │                           │
│  └────────────┬──────────────┘                           │
│               │                                           │
│  ┌────────────┴──────────────┐                           │
│  │      eth0: 192.168.1.10   │                           │
│  └────────────┬──────────────┘                           │
└───────────────┼───────────────────────────────────────────┘
                │ UDP 4789 (VXLAN encap)
                │
┌───────────────┼───────────────────────────────────────────┐
│  ┌────────────┴──────────────┐                           │
│  │      eth0: 192.168.1.20   │                           │
│  └────────────┬──────────────┘                           │
│               │                                           │
│  ┌────────────┴──────────────┐                           │
│  │       VXLAN Interface     │                           │
│  │         vtep0             │                           │
│  └────┬─────────────────┬────┘                           │
│       │                 │                                 │
│  ┌────┴────┐       ┌────┴────┐                           │
│  │10.0.0.4 │       │10.0.0.5 │                           │
│  └─────────┘       └─────────┘                           │
│  Container B1      Container B2                           │
│                                                            │
│                        Host B                              │
└───────────────────────────────────────────────────────────┘
```

### 5.2 Docker Swarm Overlay

```bash
# Инициализация Swarm
docker swarm init

# Создание overlay network
docker network create --driver overlay --attachable myoverlay

# Контейнеры на разных нодах могут общаться
docker service create --name web --network myoverlay nginx
```

### 5.3 Kubernetes Network Plugins

**Популярные CNI для Kubernetes:**

| Plugin | Особенности |
|--------|-------------|
| Calico | BGP, Network Policies, высокая производительность |
| Flannel | Простота, VXLAN overlay |
| Cilium | eBPF, Security, Observability |
| Weave | Mesh, простая настройка |
| Canal | Flannel + Calico Network Policies |

---

## 6. Сетевые драйверы в деталях

### 6.1 Bridge Driver

```bash
# Создание bridge network с параметрами
docker network create \
    --driver bridge \
    --subnet 172.28.0.0/16 \
    --ip-range 172.28.5.0/24 \
    --gateway 172.28.5.254 \
    --opt "com.docker.network.bridge.name"="br-custom" \
    custom-bridge

# Проверка моста
brctl show br-custom
ip addr show br-custom
```

### 6.2 Macvlan Driver

Macvlan позволяет контейнерам получить IP из физической сети:

```bash
# Создание macvlan network
docker network create -d macvlan \
    --subnet=192.168.1.0/24 \
    --gateway=192.168.1.1 \
    -o parent=eth0 \
    macvlan-net

# Контейнер получит IP из сети 192.168.1.0/24
docker run -d --network macvlan-net --ip 192.168.1.50 nginx
```

**Когда использовать:**
- Legacy приложения, требующие реальный IP
- Прямой доступ из физической сети
- Минимальный overhead

### 6.3 IPvlan Driver

```bash
# IPvlan L2 mode (как macvlan, но один MAC)
docker network create -d ipvlan \
    --subnet=192.168.1.0/24 \
    -o parent=eth0 \
    -o ipvlan_mode=l2 \
    ipvlan-l2

# IPvlan L3 mode (роутинг)
docker network create -d ipvlan \
    --subnet=192.168.1.0/24 \
    -o parent=eth0 \
    -o ipvlan_mode=l3 \
    ipvlan-l3
```

---

## 7. DNS в контейнерах

### 7.1 Docker Embedded DNS

```bash
# В user-defined networks работает встроенный DNS
docker network create mynet

docker run -d --name web --network mynet nginx
docker run -d --name app --network mynet alpine sleep 3600

# DNS resolution по имени контейнера
docker exec app nslookup web
```

**Output:**
```
Server:		127.0.0.11
Address:	127.0.0.11:53

Non-authoritative answer:
Name:	web
Address: 172.18.0.2
```

### 7.2 DNS aliases

```bash
# Несколько DNS имён для контейнера
docker run -d --name db --network mynet \
    --network-alias database \
    --network-alias mysql \
    mysql:8

# Можно обращаться по любому алиасу
docker exec app ping database
docker exec app ping mysql
docker exec app ping db
```

### 7.3 Custom DNS

```bash
# Свои DNS серверы
docker run -d \
    --dns 8.8.8.8 \
    --dns 8.8.4.4 \
    --dns-search example.com \
    alpine

# Проверка
docker exec <container> cat /etc/resolv.conf
```

---

## 8. Сетевая безопасность

### 8.1 Network Isolation

```bash
# Контейнеры в разных сетях не видят друг друга
docker network create net-a
docker network create net-b

docker run -d --name a --network net-a alpine sleep 3600
docker run -d --name b --network net-b alpine sleep 3600

# Не смогут общаться
docker exec a ping b  # Fail: name not resolved
```

### 8.2 Internal Networks

```bash
# Сеть без доступа к внешнему миру
docker network create --internal internal-net

docker run -d --network internal-net alpine sleep 3600

# Нет доступа к интернету
docker exec <container> ping 8.8.8.8  # Fail
```

### 8.3 iptables и Docker

```bash
# Docker добавляет свои chains
sudo iptables -L -n | grep -A10 DOCKER

# Правила NAT
sudo iptables -t nat -L -n

# Отключение автоматического управления iptables
# /etc/docker/daemon.json
{
    "iptables": false
}
```

### 8.4 Firewall rules для контейнеров

```bash
# Запретить исходящий трафик для контейнера
# (требуется знание его veth интерфейса)
VETH=$(docker exec mycontainer cat /sys/class/net/eth0/iflink)
HOST_VETH=$(ip link | grep "^${VETH}:" | cut -d: -f2 | tr -d ' ')

iptables -I DOCKER-USER -o $HOST_VETH -j DROP
```

---

## 9. Диагностика сети

### 9.1 Просмотр сетевой информации

```bash
# Информация о сетях
docker network ls
docker network inspect bridge

# Сеть контейнера
docker inspect --format '{{json .NetworkSettings.Networks}}' <container> | jq
```

### 9.2 Инструменты отладки

```bash
# Запуск контейнера с сетевыми инструментами
docker run --rm -it --network container:<target> \
    nicolaka/netshoot

# Внутри netshoot доступны: tcpdump, iftop, nmap, netstat, etc.
tcpdump -i eth0 -n
iftop -i eth0
ss -tulpn
```

### 9.3 tcpdump для контейнеров

```bash
# На хосте для трафика контейнера
CONTAINER_PID=$(docker inspect -f '{{.State.Pid}}' mycontainer)
nsenter -t $CONTAINER_PID -n tcpdump -i eth0 -n

# Или через Docker
docker run --rm --net container:mycontainer nicolaka/netshoot tcpdump -i eth0
```

### 9.4 Проверка связности

```bash
# Пинг между контейнерами
docker exec container1 ping container2

# HTTP запрос
docker exec container1 curl -v container2:80

# DNS lookup
docker exec container1 nslookup container2
docker exec container1 dig container2

# Traceroute
docker exec container1 traceroute container2
```

---

## 10. Практические примеры

### 10.1 Микросервисная архитектура

```bash
# Создаём сети для разных слоёв
docker network create frontend
docker network create backend
docker network create database

# Frontend доступен извне
docker run -d --name nginx \
    --network frontend \
    -p 80:80 \
    nginx

# API подключён к frontend и backend
docker run -d --name api \
    --network frontend \
    --network backend \
    myapi:latest

docker network connect backend api

# Database только в backend сети
docker run -d --name db \
    --network database \
    postgres

# Backend service подключён к backend и database
docker run -d --name worker \
    --network backend \
    myworker:latest

docker network connect database worker
```

### 10.2 Service Discovery pattern

```bash
# Несколько инстансов одного сервиса
docker network create app-net

for i in {1..3}; do
    docker run -d --name web-$i \
        --network app-net \
        --network-alias web \
        nginx
done

# Load balancing через DNS
docker run --rm --network app-net alpine \
    sh -c "for i in \$(seq 1 10); do nslookup web; done"

# Round-robin DNS вернёт разные IP
```

### 10.3 Мониторинг сетевого трафика

```bash
#!/bin/bash
# monitor_container_network.sh

CONTAINER=$1

if [ -z "$CONTAINER" ]; then
    echo "Usage: $0 <container_name>"
    exit 1
fi

# Получаем PID контейнера
PID=$(docker inspect -f '{{.State.Pid}}' $CONTAINER)

# Входим в network namespace и запускаем iftop
sudo nsenter -t $PID -n iftop -i eth0 -P
```

---

## 💡 Key Takeaways

- **Bridge** — дефолтный режим, подходит для большинства случаев
- **User-defined networks** предоставляют DNS и лучшую изоляцию
- **CNI** — стандартный интерфейс для сетевых плагинов
- **Overlay networks** нужны для multi-host коммуникации
- **Macvlan/IPvlan** — для интеграции с физической сетью

---

## 🚀 Next Steps

**Related Modules:**
- [Docker](../08_Docker/) — практическая работа с Docker
- [Docker Compose](../09_Compose/) — multi-container applications
- [Kubernetes](../10_Kubernetes/) — сеть в Kubernetes

**Practice Ideas:**
1. Создайте multi-tier приложение с изолированными сетями
2. Настройте macvlan для прямого доступа к контейнеру
3. Используйте netshoot для диагностики сетевых проблем
4. Исследуйте iptables правила, созданные Docker

**Going Deeper:**
- eBPF и Cilium для advanced networking
- Service Mesh (Istio, Linkerd)
- Network Policies в Kubernetes

---

## 📚 Additional Resources

**Documentation:**
- [Docker Networking](https://docs.docker.com/network/)
- [CNI Specification](https://github.com/containernetworking/cni/blob/master/SPEC.md)
- [Kubernetes Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)

**Tools:**
- [netshoot](https://github.com/nicolaka/netshoot) — сетевая отладка
- [ksniff](https://github.com/eldadru/ksniff) — tcpdump для Kubernetes

**Articles:**
- [Container Networking From Scratch](https://labs.iximiuz.com/tutorials/container-networking-from-scratch)
- [Deep Dive into Docker Networking](https://blog.docker.com/2016/12/understanding-docker-networking-drivers-use-cases/)

---

