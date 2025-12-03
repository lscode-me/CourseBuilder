# Docker - Quiz

Проверьте свои знания по теме "Практическая работа с контейнерами".

---

## Question 1: Запуск контейнера

Какой флаг запускает контейнер в detached mode?

A) -i

B) -t

C) -d

D) -r

---

## Question 2: Port mapping

Как опубликовать порт 80 контейнера на порт 8080 только для localhost?

A) -p 8080:80

B) -p 127.0.0.1:8080:80

C) -p localhost:8080:80

D) -p 80:8080

---

## Question 3: ENTRYPOINT vs CMD

Что произойдёт при docker run myimage arg1, если Dockerfile содержит ENTRYPOINT ["echo"] CMD ["hello"]?

A) echo hello

B) echo arg1

C) arg1

D) hello arg1

---

## Question 4: Multi-stage builds

Какова главная цель multi-stage builds?

A) Ускорение сборки

B) Уменьшение размера финального образа

C) Улучшение безопасности

D) Параллельная сборка

---

## Question 5: Кеширование слоёв

Какой порядок инструкций оптимален для кеширования при сборке Python-приложения?

A) COPY . . → RUN pip install

B) RUN pip install → COPY . .

C) COPY requirements.txt . → RUN pip install → COPY . .

D) Порядок не влияет

---

## Question 6: Volumes vs Bind mounts

Какое преимущество volumes перед bind mounts?

A) Быстрее работают

B) Управляются Docker, работают на любой платформе

C) Занимают меньше места

D) Поддерживают больше файловых систем

---

## Question 7: docker exec

Как выполнить интерактивную команду sh в запущенном контейнере?

A) docker run -it container sh

B) docker exec -it container sh

C) docker attach container sh

D) docker start -it container sh

---

## Question 8: Логи контейнера

Какая команда показывает логи в реальном времени?

A) docker logs container

B) docker logs -f container

C) docker logs --live container

D) docker logs -r container

---

## Question 9: Resource limits

Как ограничить контейнер использованием 1.5 CPU?

A) --cpu=1.5

B) --cpus="1.5"

C) --cpu-limit=1.5

D) --max-cpu=1.5

---

## Question 10: Health check

Какой параметр HEALTHCHECK определяет интервал проверки?

A) --timeout

B) --interval

C) --period

D) --frequency

---

## Question 11: USER instruction

Для чего используется инструкция USER в Dockerfile?

A) Аутентификация при pull

B) Запуск процессов от указанного пользователя

C) Ограничение доступа к volume

D) Настройка SSH

---

## Question 12: .dockerignore

Что делает файл .dockerignore?

A) Игнорирует контейнеры

B) Исключает файлы из build context

C) Скрывает образы

D) Блокирует порты

---

## Question 13: docker inspect

Как получить только IP-адрес контейнера?

A) docker inspect --ip container

B) docker inspect -f '{{.NetworkSettings.IPAddress}}' container

C) docker ip container

D) docker network ip container

---

## Question 14: Restart policy

Какая restart policy перезапускает контейнер, кроме случая ручной остановки?

A) always

B) on-failure

C) unless-stopped

D) no

---

## Question 15: docker tag

Какая команда создаёт тег для push в registry?

A) docker tag myapp:1.0 registry/myapp:1.0

B) docker rename myapp:1.0 registry/myapp:1.0

C) docker copy myapp:1.0 registry/myapp:1.0

D) docker label myapp:1.0 registry/myapp:1.0

---

## Question 16: Read-only filesystem

Как запустить контейнер с read-only root filesystem?

A) --ro

B) --read-only

C) --readonly

D) --immutable

---

## Question 17: Capabilities

Как удалить все capabilities из контейнера?

A) --no-caps

B) --cap-drop=ALL

C) --capabilities=none

D) --drop-all-caps

---

## Question 18: Storage driver

Какой storage driver рекомендуется для Docker?

A) aufs

B) overlay2

C) devicemapper

D) vfs

---

## Question 19: docker system prune

Что удаляет docker system prune -a?

A) Только остановленные контейнеры

B) Все неиспользуемые данные (контейнеры, сети, образы, volumes)

C) Только dangling images

D) Только volumes

---

## Question 20: Build context

Что означает точка в команде docker build -t myapp .?

A) Текущая версия

B) Build context — текущая директория

C) Все файлы рекурсивно

D) Скрытые файлы

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | -d (detached) запускает контейнер в фоновом режиме |
| 2 | B | -p 127.0.0.1:8080:80 публикует только на localhost |
| 3 | B | ENTRYPOINT фиксирован (echo), arg1 заменяет CMD |
| 4 | B | Multi-stage позволяет исключить build tools из финального образа |
| 5 | C | Сначала requirements.txt для кеширования pip install |
| 6 | B | Volumes управляются Docker и независимы от хоста |
| 7 | B | docker exec -it выполняет команду в запущенном контейнере |
| 8 | B | -f (follow) показывает логи в реальном времени |
| 9 | B | --cpus="1.5" ограничивает использование CPU |
| 10 | B | --interval определяет интервал между проверками |
| 11 | B | USER задаёт пользователя для запуска процессов |
| 12 | B | .dockerignore исключает файлы из build context |
| 13 | B | -f с Go template извлекает конкретное поле |
| 14 | C | unless-stopped перезапускает, кроме ручной остановки |
| 15 | A | docker tag создаёт новый тег для образа |
| 16 | B | --read-only делает root filesystem read-only |
| 17 | B | --cap-drop=ALL удаляет все Linux capabilities |
| 18 | B | overlay2 — рекомендуемый storage driver |
| 19 | B | prune -a удаляет все неиспользуемые ресурсы |
| 20 | B | Точка указывает build context (текущую директорию) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете Docker. Переходите к Docker Compose. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Dockerfile и security. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про volumes и resource limits. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с Docker CLI и Dockerfile. |

---

