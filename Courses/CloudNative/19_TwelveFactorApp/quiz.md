# Cloud Native Development - Quiz
## The Twelve-Factor App

---

## Question 1: Codebase





Что означает принцип "One codebase, many deploys"?

A) Каждый deploy имеет свой репозиторий

B) Нужно несколько веток для разных сред

C) Код копируется между серверами

D) Один репозиторий деплоится в разные среды (dev, staging, prod)

---

## Question 2: Config





Где должна храниться конфигурация по 12-factor?

A) В environment variables

B) В конфигурационных файлах в репозитории

C) В базе данных

D) В коде приложения

---

## Question 3: Backing Services





Как 12-factor app относится к базе данных?

A) База должна быть встроена в приложение

B) Как к внешнему подключаемому ресурсу (attached resource)

C) Как к части приложения

D) Только локальная база данных

---

## Question 4: Processes





Какой тип процессов требует 12-factor?

A) Long-running с persistent connections

B) Stateless без shared state между инстансами

C) Stateful с хранением сессий в памяти

D) Singleton процессы

---

## Question 5: Port Binding





Что означает принцип Port Binding?

A) Приложение само экспортирует HTTP сервис, слушая порт

B) Порты должны быть статически заданы

C) Приложение должно использовать порт 80

D) Нужен отдельный веб-сервер (Apache, nginx)

---

## Question 6: Build, Release, Run





Какой порядок этапов правильный?

A) Build → Release → Run

B) Run → Build → Release

C) Release → Build → Run

D) Build → Run → Release

---

## Question 7: Logs





Куда должны писаться логи по 12-factor?

A) В базу данных

B) В файлы на диске

C) В сетевой сокет

D) В stdout (стандартный вывод)

---

## Question 8: Dev/Prod Parity





Что НЕ является целью Dev/Prod Parity?

A) Разработчики деплоят свой код

B) Использовать SQLite в dev и PostgreSQL в prod

C) Использовать одинаковые backing services

D) Минимизировать время между разработкой и деплоем

---

## Question 9: Concurrency





Как масштабируется 12-factor app?

A) Добавлением RAM и CPU (вертикально)

B) Увеличением threads внутри процесса

C) Добавлением процессов/контейнеров (горизонтально)

D) Кэшированием всего в памяти

---

## Question 10: Disposability





Что означает Disposability?

A) Автоматическое удаление логов

B) Одноразовое использование

C) Быстрый запуск и graceful shutdown

D) Приложение можно удалить

---

## Question 11: Dependencies





Как должны управляться зависимости?

A) Загружаются при каждом запросе

B) Явно объявлены и изолированы (requirements.txt, package.json)

C) Установлены глобально на сервере

D) Скопированы вручную

---

## Question 12: Admin Processes





Как выполняются административные задачи (миграции)?

A) Как one-off процессы в том же environment

B) Через веб-интерфейс

C) SSH на сервер и ручной запуск

D) Отдельное приложение с другим кодом

---

## Question 13: Config Test





Какой тест проверяет правильность хранения конфигурации?

A) Используется YAML формат

B) Код работает без ошибок

C) Конфигурация в одном файле

D) Codebase можно сделать open-source без раскрытия credentials

---

## Question 14: Backing Service Change





Что нужно изменить для смены PostgreSQL на другой инстанс?

A) Все конфигурационные файлы

B) Пересобрать приложение

C) Только URL/credentials в environment

D) Код приложения

---

## Question 15: Stateless Principle





Где должно храниться состояние сессии пользователя?

A) Во внешнем хранилище (Redis, Database)

B) В cookies на клиенте (все данные)

C) В локальных файлах

D) В памяти процесса

---

## Question 16: Disposability




Что означает принцип Disposability?

A) Быстрый startup и graceful shutdown

B) Использовать disposable VMs

C) Удалять старый код

D) Удалять логи

---

## Question 17: Dev/Prod Parity




Почему важна Dev/Prod Parity?

A) Для экономии

B) Минимизация различий уменьшает bugs при deploy

C) Для compliance

D) Для security

---

## Question 18: Port Binding




Что означает Port Binding?

A) Использовать только порт 80

B) Binding к localhost

C) App export HTTP как service через port binding

D) Только HTTPS

---

## Question 19: Concurrency




Как масштабировать по принципу Concurrency?

A) Вертикально

B) Горизонтально через процессы (web, worker)

C) Через threads только

D) Через bigger instances

---

## Question 20: Build/Release/Run




Какие три стадии в Build, Release, Run?

A) Build (compile), Release (config), Run (execute)

B) Plan, Apply, Destroy

C) Code, Test, Deploy

D) Dev, Stage, Prod

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Один репозиторий — множество деплоев в разные среды. Различия только в конфигурации. |
| 2 | A | Конфигурация хранится в environment variables, не в коде или файлах репозитория. |
| 3 | B | База данных — attached resource, подключаемый через URL. Смена БД не требует изменения кода. |
| 4 | B | Процессы должны быть stateless — без shared state в памяти. State хранится во внешних сервисах. |
| 5 | A | Приложение само экспортирует HTTP (или другой) сервис, слушая порт. Не зависит от внешнего веб-сервера. |
| 6 | A | Build (компиляция) → Release (build + config) → Run (запуск процессов). |
| 7 | D | Логи пишутся в stdout. Система (Docker, K8s) собирает и агрегирует их. |
| 8 | B | SQLite в dev и PostgreSQL в prod — нарушение parity. Нужны одинаковые сервисы везде. |
| 9 | C | Горизонтальное масштабирование через добавление процессов/контейнеров. |
| 10 | C | Disposability = быстрый запуск (секунды) и graceful shutdown (обработка SIGTERM). |
| 11 | B | Зависимости явно объявлены в manifest (requirements.txt) и изолированы (virtualenv, container). |
| 12 | A | Admin tasks выполняются как one-off процессы в том же environment, с тем же кодом и конфигом. |
| 13 | D | Если можно сделать код open-source без раскрытия секретов — конфигурация правильно отделена. |
| 14 | C | Смена backing service = смена URL в environment variable. Код не меняется. |
| 15 | A | Состояние сессии хранится во внешнем хранилище (Redis, DB), не в памяти процесса. |
| 16 | A | Disposability: быстрый startup и graceful shutdown |
| 17 | B | Dev/Prod Parity минимизирует bugs при deploy |
| 18 | C | Port Binding: app экспортирует HTTP как service |
| 19 | B | Concurrency: горизонтально через процессы |
| 20 | A | Build (compile), Release (config), Run (execute) |

---

## Scoring Guide

| Результат | Оценка |
|-----------|--------|
| **14-15 (90-100%)** | 🏆 Отлично! |
| **11-13 (70-89%)** | ✅ Хорошо |
| **8-10 (50-69%)** | ⚠️ Удовлетворительно |
| **< 8 (<50%)** | 📚 Нужно повторить |

---

