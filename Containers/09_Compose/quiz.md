# Docker Compose & Swarm - Quiz

Проверьте свои знания по теме "Оркестрация многоконтейнерных приложений".

---

## Question 1: docker compose up

Какой флаг запускает сервисы в фоновом режиме?

A) -b

B) -d

C) -f

D) --background

---

## Question 2: depends_on

Как дождаться готовности базы данных перед запуском приложения?

A) depends_on: [db]

B) depends_on: db: condition: service_healthy

C) wait_for: db

D) requires: db

---

## Question 3: Volumes в Compose

Как определить named volume в docker-compose.yml?

A) Только в секции volumes сервиса

B) В секции volumes сервиса и на верхнем уровне файла

C) Только на верхнем уровне файла

D) Volumes не поддерживаются в Compose

---

## Question 4: Networks

Какой тип сети используется для изоляции от интернета?

A) driver: bridge

B) internal: true

C) isolated: true

D) external: false

---

## Question 5: Profiles

Как запустить сервисы с профилем debug?

A) docker compose --profile debug up

B) docker compose -p debug up

C) docker compose up --debug

D) docker compose up debug

---

## Question 6: Environment variables

Как использовать переменную окружения из .env файла?

A) ${VAR_NAME}

B) $VAR_NAME

C) %VAR_NAME%

D) {{VAR_NAME}}

---

## Question 7: Swarm init

Какая команда инициализирует Swarm кластер?

A) docker swarm create

B) docker swarm init

C) docker cluster init

D) docker init swarm

---

## Question 8: Swarm replicas

Как масштабировать сервис до 5 реплик?

A) docker service replicas web 5

B) docker service scale web=5

C) docker service update --replicas=5 web

D) Оба B и C правильны

---

## Question 9: Overlay network

Для чего нужен overlay network в Swarm?

A) Для шифрования данных

B) Для связи контейнеров на разных нодах

C) Для ускорения сети

D) Для изоляции от интернета

---

## Question 10: Swarm secrets

Как создать secret в Swarm?

A) docker secret create name ./file

B) docker swarm secret add name ./file

C) docker service secret create name ./file

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

A) inactive

B) pause

C) drain

D) disabled

---

## Question 13: Update config

Какой параметр определяет количество одновременно обновляемых реплик?

A) concurrency

B) parallelism

C) batch_size

D) simultaneous

---

## Question 14: Extension fields

Как определить переиспользуемый блок конфигурации в Compose?

A) &name

B) x-name

C) template-name

D) @name

---

## Question 15: Healthcheck в Compose

Какой параметр определяет время ожидания перед первой проверкой?

A) initial_delay

B) start_period

C) wait_time

D) startup_delay

---

## Question 16: docker compose down

Какой флаг удаляет volumes при остановке?

A) -r

B) -v

C) --remove-volumes

D) --clean

---

## Question 17: Swarm managers

Какое рекомендуемое количество manager нод?

A) 2

B) Чётное число

C) Нечётное число (3, 5, 7)

D) Минимум 5

---

## Question 18: Rolling update order

Какой order запускает новый контейнер перед остановкой старого?

A) start-first

B) new-first

C) rolling

D) blue-green

---

## Question 19: Compose override

Какой файл автоматически применяется вместе с docker-compose.yml?

A) docker-compose.local.yml

B) docker-compose.override.yml

C) docker-compose.dev.yml

D) docker-compose.extra.yml

---

## Question 20: Placement constraints

Как ограничить сервис только worker нодами?

A) node.type == worker

B) node.role == worker

C) placement: worker

D) only_workers: true

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | -d (detached) запускает сервисы в фоновом режиме |
| 2 | B | condition: service_healthy ждёт прохождения healthcheck |
| 3 | B | Named volumes определяются и в сервисе, и на верхнем уровне |
| 4 | B | internal: true создаёт сеть без доступа к внешним сетям |
| 5 | A | --profile указывает профиль для запуска |
| 6 | A | ${VAR_NAME} — синтаксис для переменных в Compose |
| 7 | B | docker swarm init инициализирует Swarm кластер |
| 8 | D | Оба docker service scale и update --replicas работают |
| 9 | B | Overlay network позволяет контейнерам на разных хостах общаться |
| 10 | A | docker secret create name создаёт secret |
| 11 | B | docker stack deploy -c file name деплоит stack |
| 12 | C | drain перемещает все tasks с ноды |
| 13 | B | parallelism определяет количество одновременно обновляемых реплик |
| 14 | B | x- префикс для extension fields в Compose |
| 15 | B | start_period — время до первой проверки здоровья |
| 16 | B | -v удаляет named volumes |
| 17 | C | Нечётное число для Raft consensus (3, 5, 7) |
| 18 | A | start-first запускает новый контейнер перед остановкой старого |
| 19 | B | docker-compose.override.yml автоматически применяется |
| 20 | B | node.role == worker ограничивает placement |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете Compose и Swarm. Переходите к Kubernetes. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Swarm и deploy config. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про depends_on и networks. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с docker-compose.yml и Swarm. |

---

