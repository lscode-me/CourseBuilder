# Docker - Quiz

Проверьте свои знания по теме "Практическая работа с контейнерами".

---

## Question 1: Запуск контейнера





Какой флаг запускает контейнер в detached mode?

A) -t

B) -i

C) -r

D) -d

---

## Question 2: Port mapping





Как опубликовать порт 80 контейнера на порт 8080 только для localhost?

A) -p 8080:80

B) -p 80:8080

C) -p 127.0.0.1:8080:80

D) -p localhost:8080:80

---

## Question 3: ENTRYPOINT vs CMD





Что произойдёт при docker run myimage arg1, если Dockerfile содержит ENTRYPOINT ["echo"] CMD ["hello"]?

A) hello arg1

B) echo arg1

C) echo hello

D) arg1

---

## Question 4: Multi-stage builds





Какова главная цель multi-stage builds?

A) Уменьшение размера финального образа

B) Ускорение сборки

C) Улучшение безопасности

D) Параллельная сборка

---

## Question 5: Кеширование слоёв





Какой порядок инструкций оптимален для кеширования при сборке Python-приложения?

A) COPY requirements.txt . → RUN pip install → COPY . .

B) Порядок не влияет

C) COPY . . → RUN pip install

D) RUN pip install → COPY . .

---

## Question 6: Volumes vs Bind mounts





Какое преимущество volumes перед bind mounts?

A) Управляются Docker, работают на любой платформе

B) Быстрее работают

C) Занимают меньше места

D) Поддерживают больше файловых систем

---

## Question 7: docker exec





Как выполнить интерактивную команду sh в запущенном контейнере?

A) docker exec -it container sh

B) docker run -it container sh

C) docker start -it container sh

D) docker attach container sh

---

## Question 8: Логи контейнера





Какая команда показывает логи в реальном времени?

A) docker logs -r container

B) docker logs container

C) docker logs -f container

D) docker logs --live container

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

B) --period

C) --frequency

D) --interval

---

## Question 11: USER instruction





Для чего используется инструкция USER в Dockerfile?

A) Ограничение доступа к volume

B) Настройка SSH

C) Аутентификация при pull

D) Запуск процессов от указанного пользователя

---

## Question 12: .dockerignore





Что делает файл .dockerignore?

A) Блокирует порты

B) Игнорирует контейнеры

C) Скрывает образы

D) Исключает файлы из build context

---

## Question 13: docker inspect





Как получить только IP-адрес контейнера?

A) docker inspect -f '{{.NetworkSettings.IPAddress}}' container

B) docker network ip container

C) docker ip container

D) docker inspect --ip container

---

## Question 14: Restart policy





Какая restart policy перезапускает контейнер, кроме случая ручной остановки?

A) unless-stopped

B) on-failure

C) no

D) always

---

## Question 15: docker tag





Какая команда создаёт тег для push в registry?

A) docker rename myapp:1.0 registry/myapp:1.0

B) docker tag myapp:1.0 registry/myapp:1.0

C) docker copy myapp:1.0 registry/myapp:1.0

D) docker label myapp:1.0 registry/myapp:1.0

---

## Question 16: Read-only filesystem





Как запустить контейнер с read-only root filesystem?

A) --immutable

B) --read-only

C) --ro

D) --readonly

---

## Question 17: Capabilities





Как удалить все capabilities из контейнера?

A) --cap-drop=ALL

B) --no-caps

C) --capabilities=none

D) --drop-all-caps

---

## Question 18: Storage driver





Какой storage driver рекомендуется для Docker?

A) devicemapper

B) aufs

C) overlay2

D) vfs

---

## Question 19: docker system prune





Что удаляет docker system prune -a?

A) Только остановленные контейнеры

B) Только dangling images

C) Все неиспользуемые данные (контейнеры, сети, образы, volumes)

D) Только volumes

---

## Question 20: Build context





Что означает точка в команде docker build -t myapp .?

A) Текущая версия

B) Все файлы рекурсивно

C) Скрытые файлы

D) Build context — текущая директория

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | -d (detached) запускает контейнер в фоновом режиме |
| 2 | C | -p 127.0.0.1:8080:80 публикует только на localhost |
| 3 | B | ENTRYPOINT фиксирован (echo), arg1 заменяет CMD |
| 4 | A | Multi-stage позволяет исключить build tools из финального образа |
| 5 | A | Сначала requirements.txt для кеширования pip install |
| 6 | A | Volumes управляются Docker и независимы от хоста |
| 7 | A | docker exec -it выполняет команду в запущенном контейнере |
| 8 | C | -f (follow) показывает логи в реальном времени |
| 9 | B | --cpus="1.5" ограничивает использование CPU |
| 10 | D | --interval определяет интервал между проверками |
| 11 | D | USER задаёт пользователя для запуска процессов |
| 12 | D | .dockerignore исключает файлы из build context |
| 13 | A | -f с Go template извлекает конкретное поле |
| 14 | A | unless-stopped перезапускает, кроме ручной остановки |
| 15 | B | docker tag создаёт новый тег для образа |
| 16 | B | --read-only делает root filesystem read-only |
| 17 | A | --cap-drop=ALL удаляет все Linux capabilities |
| 18 | C | overlay2 — рекомендуемый storage driver |
| 19 | C | prune -a удаляет все неиспользуемые ресурсы |
| 20 | D | Точка указывает build context (текущую директорию) |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете Docker. Переходите к Docker Compose. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы про Dockerfile и security. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы про volumes и resource limits. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Рекомендуется практика с Docker CLI и Dockerfile. |

---

