# Docker Compose & Swarm
## Оркестрация многоконтейнерных приложений

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Уметь работать с Docker CLI
- Понимать сетевые режимы Docker
- Знать основы YAML

**Recommended prior modules:**
- [Docker](../08_Docker/)
- [Container Networking](../07_Networking/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать docker-compose.yml для многоконтейнерных приложений
- Использовать profiles, secrets и configs
- Настраивать Docker Swarm кластер
- Развёртывать сервисы в Swarm mode

---

## 1. Docker Compose — основы

### 1.1 Что такое Docker Compose

Docker Compose — инструмент для определения и запуска многоконтейнерных приложений.

```yaml
# docker-compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
  
  api:
    build: ./api
    environment:
      - DATABASE_URL=postgres://db/app
    depends_on:
      - db
  
  db:
    image: postgres:15
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

### 1.2 Compose CLI

```bash
# Запуск всех сервисов
docker compose up

# В фоновом режиме
docker compose up -d

# Только определённые сервисы
docker compose up web api

# Пересборка образов
docker compose up --build

# Остановка
docker compose down

# Остановка с удалением volumes
docker compose down -v

# Просмотр логов
docker compose logs -f

# Статус сервисов
docker compose ps

# Выполнение команды в сервисе
docker compose exec web sh
docker compose run --rm api python manage.py migrate
```

### 1.3 Версии Compose file

```yaml
# Compose V2 (без version, рекомендуется)
services:
  web:
    image: nginx

# Compose V1 (устарел)
version: "3.8"
services:
  web:
    image: nginx
```

---

## 2. Структура docker-compose.yml

### 2.1 Сервисы

```yaml
services:
  webapp:
    # Образ или сборка
    image: myapp:latest
    # ИЛИ
    build:
      context: ./app
      dockerfile: Dockerfile.prod
      args:
        - VERSION=1.0
    
    # Контейнер
    container_name: webapp
    hostname: webapp
    
    # Порты
    ports:
      - "8080:80"
      - "127.0.0.1:8443:443"
    
    # Переменные окружения
    environment:
      - NODE_ENV=production
      - API_KEY=${API_KEY}
    env_file:
      - .env
      - .env.production
    
    # Volumes
    volumes:
      - ./src:/app/src
      - app-data:/app/data
      - /etc/localtime:/etc/localtime:ro
    
    # Сеть
    networks:
      - frontend
      - backend
    
    # Зависимости
    depends_on:
      db:
        condition: service_healthy
    
    # Ресурсы
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          memory: 256M
    
    # Перезапуск
    restart: unless-stopped
    
    # Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### 2.2 Сети

```yaml
services:
  web:
    networks:
      - frontend
  
  api:
    networks:
      - frontend
      - backend
  
  db:
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  
  backend:
    driver: bridge
    internal: true  # Без доступа к интернету
  
  existing:
    external: true  # Использовать существующую сеть
    name: my-existing-network
```

### 2.3 Volumes

```yaml
services:
  db:
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro

volumes:
  db-data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /data/postgres
  
  nfs-data:
    driver: local
    driver_opts:
      type: nfs
      o: addr=192.168.1.100,rw
      device: ":/export/data"
```

---

## 3. Продвинутые возможности

### 3.1 Profiles

```yaml
services:
  web:
    image: nginx
    # Всегда запускается
  
  debug:
    image: busybox
    profiles:
      - debug
    # Только при docker compose --profile debug up
  
  test:
    image: node
    profiles:
      - test
      - ci
```

```bash
# Запуск с профилем
docker compose --profile debug up

# Несколько профилей
docker compose --profile debug --profile test up
```

### 3.2 Secrets

```yaml
services:
  web:
    image: nginx
    secrets:
      - db_password
      - source: api_key
        target: /run/secrets/api_key
        mode: 0400

secrets:
  db_password:
    file: ./secrets/db_password.txt
  
  api_key:
    environment: "API_KEY"  # Из переменной окружения
```

### 3.3 Configs

```yaml
services:
  web:
    image: nginx
    configs:
      - source: nginx_config
        target: /etc/nginx/nginx.conf

configs:
  nginx_config:
    file: ./nginx.conf
```

### 3.4 Extensions и YAML anchors

```yaml
# Базовая конфигурация
x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"

x-common: &common
  restart: unless-stopped
  logging: *default-logging

services:
  web:
    <<: *common
    image: nginx
  
  api:
    <<: *common
    image: myapi
    environment:
      - DEBUG=false
```

### 3.5 Условные зависимости

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
      migration:
        condition: service_completed_successfully

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
  
  migration:
    build: ./migration
    command: migrate up
    depends_on:
      db:
        condition: service_healthy
```

---

## 4. Примеры приложений

### 4.1 Веб-приложение с базой данных

```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - app-network

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data
    networks:
      - app-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
```

### 4.2 Development environment

```yaml
services:
  app:
    build:
      context: .
      target: development
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
      - "9229:9229"  # Debug port
    environment:
      - NODE_ENV=development
    command: npm run dev

  db:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_PASSWORD=devpass
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  adminer:
    image: adminer
    ports:
      - "8080:8080"
```

### 4.3 Microservices

```yaml
services:
  gateway:
    build: ./gateway
    ports:
      - "80:80"
    networks:
      - public
      - internal
    depends_on:
      - user-service
      - product-service

  user-service:
    build: ./services/user
    environment:
      - DB_HOST=user-db
    networks:
      - internal
    depends_on:
      - user-db

  user-db:
    image: postgres:15
    volumes:
      - user-data:/var/lib/postgresql/data
    networks:
      - internal

  product-service:
    build: ./services/product
    environment:
      - DB_HOST=product-db
    networks:
      - internal
    depends_on:
      - product-db

  product-db:
    image: mongo:6
    volumes:
      - product-data:/data/db
    networks:
      - internal

  message-queue:
    image: rabbitmq:3-management
    ports:
      - "15672:15672"
    networks:
      - internal

networks:
  public:
  internal:
    internal: true

volumes:
  user-data:
  product-data:
```

---

## 5. Docker Swarm

### 5.1 Что такое Swarm

Docker Swarm — встроенная оркестрация для кластера Docker хостов.

```
┌─────────────────────────────────────────────────────────┐
│                    Docker Swarm Cluster                  │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Manager   │  │   Manager   │  │   Manager   │     │
│  │   (Leader)  │  │             │  │             │     │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
│         │                │                │             │
│         └────────────────┼────────────────┘             │
│                          │                              │
│  ┌─────────────┐  ┌──────┴──────┐  ┌─────────────┐     │
│  │   Worker    │  │   Worker    │  │   Worker    │     │
│  │  ┌───────┐  │  │  ┌───────┐  │  │  ┌───────┐  │     │
│  │  │Task(s)│  │  │  │Task(s)│  │  │  │Task(s)│  │     │
│  │  └───────┘  │  │  └───────┘  │  │  └───────┘  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Инициализация Swarm

```bash
# Инициализация на первом manager
docker swarm init --advertise-addr 192.168.1.10

# Получение токена для workers
docker swarm join-token worker

# Получение токена для managers
docker swarm join-token manager

# Присоединение worker
docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Присоединение manager
docker swarm join --token SWMTKN-1-yyy 192.168.1.10:2377

# Список нод
docker node ls
```

**Output:**
```
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS
abc123 *                      manager1   Ready     Active         Leader
def456                        manager2   Ready     Active         Reachable
ghi789                        worker1    Ready     Active
jkl012                        worker2    Ready     Active
```

### 5.3 Services в Swarm

```bash
# Создание сервиса
docker service create \
    --name web \
    --replicas 3 \
    --publish 80:80 \
    nginx:alpine

# Список сервисов
docker service ls

# Информация о сервисе
docker service ps web

# Масштабирование
docker service scale web=5

# Обновление
docker service update --image nginx:latest web

# Rolling update
docker service update \
    --update-parallelism 2 \
    --update-delay 10s \
    --image nginx:1.25 \
    web

# Удаление
docker service rm web
```

### 5.4 Deploy в Swarm через Compose

```yaml
# docker-compose.yml для Swarm
services:
  web:
    image: nginx:alpine
    deploy:
      replicas: 3
      update_config:
        parallelism: 2
        delay: 10s
        failure_action: rollback
      rollback_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      placement:
        constraints:
          - node.role == worker
          - node.labels.zone == us-east
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
        reservations:
          memory: 128M
    ports:
      - "80:80"
    networks:
      - webnet

networks:
  webnet:
    driver: overlay
```

```bash
# Деплой stack в Swarm
docker stack deploy -c docker-compose.yml myapp

# Список stacks
docker stack ls

# Сервисы в stack
docker stack services myapp

# Удаление stack
docker stack rm myapp
```

### 5.5 Overlay Networks в Swarm

```bash
# Создание overlay network
docker network create --driver overlay --attachable myoverlay

# Шифрование трафика
docker network create --driver overlay --opt encrypted myoverlay-encrypted
```

### 5.6 Secrets в Swarm

```bash
# Создание secret
echo "mysecretpassword" | docker secret create db_password -

# Или из файла
docker secret create ssl_cert ./server.crt

# Использование в сервисе
docker service create \
    --name web \
    --secret db_password \
    --secret source=ssl_cert,target=/etc/ssl/server.crt \
    myapp
```

### 5.7 Configs в Swarm

```bash
# Создание config
docker config create nginx_conf ./nginx.conf

# Использование
docker service create \
    --name web \
    --config source=nginx_conf,target=/etc/nginx/nginx.conf \
    nginx
```

---

## 6. High Availability

### 6.1 Multi-manager setup

```bash
# Рекомендуется нечётное количество managers (3, 5, 7)
# для Raft consensus

# Promotion worker to manager
docker node promote worker1

# Demotion manager to worker
docker node demote manager2
```

### 6.2 Node labels

```bash
# Добавление label
docker node update --label-add zone=us-east worker1
docker node update --label-add type=gpu worker2

# Использование в placement constraints
docker service create \
    --name ml-service \
    --constraint 'node.labels.type == gpu' \
    ml-image
```

### 6.3 Drain и Availability

```bash
# Вывод ноды из обслуживания
docker node update --availability drain worker1

# Возврат
docker node update --availability active worker1

# Pause (не принимает новые tasks)
docker node update --availability pause worker1
```

---

## 7. Мониторинг и логирование

### 7.1 Логирование в Compose

```yaml
services:
  app:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    # ИЛИ
    logging:
      driver: syslog
      options:
        syslog-address: "udp://logs.example.com:514"
```

### 7.2 Просмотр логов

```bash
# Compose
docker compose logs -f web

# Swarm
docker service logs -f web

# Все сервисы stack
docker stack services myapp -q | xargs -I {} docker service logs -f {}
```

### 7.3 Healthchecks

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
```

---

## 8. Практические паттерны

### 8.1 Environment separation

```bash
# Базовый файл
# docker-compose.yml

# Override для development
# docker-compose.override.yml (автоматически применяется)

# Production override
# docker-compose.prod.yml
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

```yaml
# docker-compose.yml
services:
  web:
    image: myapp:${VERSION:-latest}

# docker-compose.override.yml (development)
services:
  web:
    build: .
    volumes:
      - .:/app
    environment:
      - DEBUG=true

# docker-compose.prod.yml
services:
  web:
    deploy:
      replicas: 3
    environment:
      - DEBUG=false
```

### 8.2 Wait for dependencies

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy
    command: ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]
```

### 8.3 Zero-downtime deployment

```yaml
services:
  web:
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first  # Сначала запустить новую, потом остановить старую
      rollback_config:
        parallelism: 1
        delay: 10s
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 30s
```

---

## 💡 Key Takeaways

- **Docker Compose** упрощает запуск многоконтейнерных приложений
- **depends_on с condition** обеспечивает правильный порядок запуска
- **Docker Swarm** предоставляет встроенную оркестрацию
- **Overlay networks** нужны для коммуникации между нодами
- **Secrets и configs** безопасно хранят чувствительные данные

---

## 🚀 Next Steps

**Related Modules:**
- [Kubernetes](../10_Kubernetes/) — продвинутая оркестрация

**Practice Ideas:**
1. Создайте многоконтейнерное приложение с Compose
2. Настройте 3-node Swarm cluster
3. Реализуйте zero-downtime deployment
4. Используйте profiles для разных окружений

**Going Deeper:**
- Traefik как ingress для Swarm
- Portainer для UI управления
- Kubernetes vs Swarm сравнение

---

## 📚 Additional Resources

**Documentation:**
- [Docker Compose](https://docs.docker.com/compose/)
- [Docker Swarm](https://docs.docker.com/engine/swarm/)
- [Compose file reference](https://docs.docker.com/compose/compose-file/)

**Tools:**
- [Portainer](https://www.portainer.io/) — UI для Docker/Swarm
- [Traefik](https://traefik.io/) — reverse proxy для контейнеров

**Articles:**
- [Docker Compose Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Swarm mode overview](https://docs.docker.com/engine/swarm/)

---

