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

A) -p 127.0.0.1:8080:80

B) -p localhost:8080:80

C) -p 8080:80

D) -p 80:8080

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

A) Параллельная сборка

B) Улучшение безопасности

C) Ускорение сборки

D) Уменьшение размера финального образа

---

## Question 5: Кеширование слоёв







Какой порядок инструкций оптимален для кеширования при сборке Python-приложения?

A) Порядок не влияет

B) RUN pip install → COPY . .

C) COPY . . → RUN pip install

D) COPY requirements.txt . → RUN pip install → COPY . .

---

## Question 6: Volumes vs Bind mounts







Какое преимущество volumes перед bind mounts?

A) Занимают меньше места

B) Управляются Docker, работают на любой платформе

C) Быстрее работают

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

B) docker logs -f container

C) docker logs --live container

D) docker logs container

---

## Question 9: Resource limits







Как ограничить контейнер использованием 1.5 CPU?

A) --cpu=1.5

B) --cpu-limit=1.5

C) --max-cpu=1.5

D) --cpus="1.5"

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

A) Скрывает образы

B) Игнорирует контейнеры

C) Исключает файлы из build context

D) Блокирует порты

---

## Question 13: docker inspect







Как получить только IP-адрес контейнера?

A) docker ip container

B) docker inspect --ip container

C) docker inspect -f '{{.NetworkSettings.IPAddress}}' container

D) docker network ip container

---

## Question 14: Restart policy







Какая restart policy перезапускает контейнер, кроме случая ручной остановки?

A) on-failure

B) always

C) no

D) unless-stopped

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

A) --readonly

B) --ro

C) --read-only

D) --immutable

---

## Question 17: Capabilities







Как удалить все capabilities из контейнера?

A) --capabilities=none

B) --no-caps

C) --drop-all-caps

D) --cap-drop=ALL

---

## Question 18: Storage driver







Какой storage driver рекомендуется для Docker?

A) devicemapper

B) vfs

C) aufs

D) overlay2

---

## Question 19: docker system prune







Что удаляет docker system prune -a?

A) Только остановленные контейнеры

B) Все неиспользуемые данные (контейнеры, сети, образы, volumes)

C) Только volumes

D) Только dangling images

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
| 2 | A | -p 127.0.0.1:8080:80 публикует только на localhost |
| 3 | B | ENTRYPOINT фиксирован (echo), arg1 заменяет CMD |
| 4 | D | Multi-stage позволяет исключить build tools из финального образа |
| 5 | D | Сначала requirements.txt для кеширования pip install |
| 6 | B | Volumes управляются Docker и независимы от хоста |
| 7 | A | docker exec -it выполняет команду в запущенном контейнере |
| 8 | B | -f (follow) показывает логи в реальном времени |
| 9 | D | --cpus="1.5" ограничивает использование CPU |
| 10 | D | --interval определяет интервал между проверками |
| 11 | D | USER задаёт пользователя для запуска процессов |
| 12 | C | .dockerignore исключает файлы из build context |
| 13 | C | -f с Go template извлекает конкретное поле |
| 14 | D | unless-stopped перезапускает, кроме ручной остановки |
| 15 | B | docker tag создаёт новый тег для образа |
| 16 | C | --read-only делает root filesystem read-only |
| 17 | D | --cap-drop=ALL удаляет все Linux capabilities |
| 18 | D | overlay2 — рекомендуемый storage driver |
| 19 | B | prune -a удаляет все неиспользуемые ресурсы |
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

