# Docker Compose & Swarm - Quiz

Проверьте свои знания по теме "Оркестрация многоконтейнерных приложений".

---

## Question 1: docker compose up

Какой флаг запускает сервисы в фоновом режиме?

A) -d

B) -b

C) -f

D) --background

---

## Question 2: depends_on

Как дождаться готовности базы данных перед запуском приложения?

A) requires: db

B) depends_on: db: condition: service_healthy

C) wait_for: db

D) depends_on: [db]

---

## Question 3: Volumes в Compose

Как определить named volume в docker-compose.yml?

A) Volumes не поддерживаются в Compose

B) Только на верхнем уровне файла

C) Только в секции volumes сервиса

D) В секции volumes сервиса и на верхнем уровне файла

---

## Question 4: Networks

Какой тип сети используется для изоляции от интернета?

A) internal: true

B) driver: bridge

C) external: false

D) isolated: true

---

## Question 5: Profiles

Как запустить сервисы с профилем debug?

A) docker compose up debug

B) docker compose up --debug

C) docker compose --profile debug up

D) docker compose -p debug up

---

## Question 6: Environment variables

Как использовать переменную окружения из .env файла?

A) {{VAR_NAME}}

B) $VAR_NAME

C) ${VAR_NAME}

D) %VAR_NAME%

---

## Question 7: Swarm init

Какая команда инициализирует Swarm кластер?

A) docker swarm create

B) docker swarm init

C) docker init swarm

D) docker cluster init

---

## Question 8: Swarm replicas

Как масштабировать сервис до 5 реплик?

A) docker service scale web=5

B) docker service update --replicas=5 web

C) docker service replicas web 5

D) Оба B и C правильны

---

## Question 9: Overlay network

Для чего нужен overlay network в Swarm?

A) Для изоляции от интернета

B) Для шифрования данных

C) Для связи контейнеров на разных нодах

D) Для ускорения сети

---

## Question 10: Swarm secrets

Как создать secret в Swarm?

A) docker secret create name ./file

B) docker service secret create name ./file

C) docker swarm secret add name ./file

D) docker config create secret name ./file

---

## Question 11: Stack deploy

Какая команда деплоит stack из docker-compose.yml в Swarm?

A) docker compose deploy

B) docker stack deploy -c docker-compose.yml myapp

C) docker swarm deploy docker-compose.yml

D) docker service deploy -f docker-compose.yml

---

## Question 12: Node availability

Какое значение availability выводит ноду из обслуживания?

A) pause

B) disabled

C) inactive

D) drain

---

## Question 13: Update config

Какой параметр определяет количество одновременно обновляемых реплик?

A) batch_size

B) simultaneous

C) parallelism

D) concurrency

---

## Question 14: Extension fields

Как определить переиспользуемый блок конфигурации в Compose?

A) @name

B) &name

C) x-name

D) template-name

---

## Question 15: Healthcheck в Compose

Какой параметр определяет время ожидания перед первой проверкой?

A) wait_time

B) initial_delay

C) start_period

D) startup_delay

---

## Question 16: docker compose down

Какой флаг удаляет volumes при остановке?

A) --clean

B) -r

C) --remove-volumes

D) -v

---

## Question 17: Swarm managers

Какое рекомендуемое количество manager нод?

A) Чётное число

B) 2

C) Минимум 5

D) Нечётное число (3, 5, 7)

---

## Question 18: Rolling update order

Какой order запускает новый контейнер перед остановкой старого?

A) blue-green

B) rolling

C) new-first

D) start-first

---

## Question 19: Compose override

Какой файл автоматически применяется вместе с docker-compose.yml?

A) docker-compose.dev.yml

B) docker-compose.override.yml

C) docker-compose.local.yml

D) docker-compose.extra.yml

---

## Question 20: Placement constraints

Как ограничить сервис только worker нодами?

A) only_workers: true

B) placement: worker

C) node.role == worker

D) node.type == worker

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | -d (detached) запускает сервисы в фоновом режиме |
| 2 | B | condition: service_healthy ждёт прохождения healthcheck |
| 3 | D | Named volumes определяются и в сервисе, и на верхнем уровне |
| 4 | A | internal: true создаёт сеть без доступа к внешним сетям |
| 5 | C | --profile указывает профиль для запуска |
| 6 | C | ${VAR_NAME} — синтаксис для переменных в Compose |
| 7 | B | docker swarm init инициализирует Swarm кластер |
| 8 | D | Оба docker service scale и update --replicas работают |
| 9 | C | Overlay network позволяет контейнерам на разных хостах общаться |
| 10 | A | docker secret create name создаёт secret |
| 11 | B | docker stack deploy -c file name деплоит stack |
| 12 | D | drain перемещает все tasks с ноды |
| 13 | C | parallelism определяет количество одновременно обновляемых реплик |
| 14 | C | x- префикс для extension fields в Compose |
| 15 | C | start_period — время до первой проверки здоровья |
| 16 | D | -v удаляет named volumes |
| 17 | D | Нечётное число для Raft consensus (3, 5, 7) |
| 18 | D | start-first запускает новый контейнер перед остановкой старого |
| 19 | B | docker-compose.override.yml автоматически применяется |
| 20 | C | node.role == worker ограничивает placement |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете Compose и Swarm. Переходите к Kubernetes. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Swarm и deploy config. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про depends_on и networks. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с docker-compose.yml и Swarm. |

---


