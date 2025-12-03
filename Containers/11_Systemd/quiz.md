# systemd-nspawn - Quiz

Проверьте свои знания по теме "systemd-контейнеры и машины".

---

## Question 1: Определение systemd-nspawn

Какой тип контейнеров создаёт systemd-nspawn?

A) Application containers — один процесс, без init системы

B) System containers — полная ОС с init системой

C) Виртуальные машины с полной эмуляцией hardware

D) Serverless функции

---

## Question 2: Сравнение с Docker

Какое главное отличие systemd-nspawn от Docker в плане образов?

A) systemd-nspawn использует OCI-совместимые образы

B) systemd-nspawn работает с директориями, tar-архивами и raw образами вместо layered images

C) systemd-nspawn скачивает образы из Docker Hub

D) systemd-nspawn использует OverlayFS слои как Docker

---

## Question 3: Запуск контейнера

Что делает флаг `-b` в команде `systemd-nspawn -b -D /var/lib/machines/debian`?

A) Запускает контейнер в background

B) Запускает boot sequence — init систему контейнера

C) Включает bridge networking

D) Создаёт bind mount

---

## Question 4: Директория машин

Какая директория является стандартным местом для хранения машин systemd-nspawn?

A) /var/containers/

B) /home/machines/

C) /var/lib/machines/

D) /etc/systemd/machines/

---

## Question 5: machinectl

Какая команда используется для просмотра списка запущенных машин?

A) `systemd-nspawn --list`

B) `machinectl list`

C) `nspawn-ctl ps`

D) `systemctl list-machines`

---

## Question 6: Сетевые режимы

Какой флаг создаёт virtual ethernet pair между хостом и контейнером?

A) `--network-bridge`

B) `--private-network`

C) `--network-veth`

D) `--network-host`

---

## Question 7: Конфигурационные файлы

Где должен располагаться файл конфигурации `.nspawn` для машины с именем "webserver"?

A) /var/lib/machines/webserver.nspawn

B) /etc/systemd/nspawn/webserver.nspawn

C) /etc/machines/webserver.conf

D) ~/.config/nspawn/webserver.nspawn

---

## Question 8: Capabilities

Какая команда запустит контейнер с дополнительной capability CAP_NET_ADMIN?

A) `systemd-nspawn --add-cap=NET_ADMIN -D /path`

B) `systemd-nspawn --capability=CAP_NET_ADMIN -D /path`

C) `systemd-nspawn --cap-add=NET_ADMIN -D /path`

D) `systemd-nspawn --grant=CAP_NET_ADMIN -D /path`

---

## Question 9: Bind mounts

Какой флаг используется для монтирования директории хоста в контейнер в режиме только для чтения?

A) `--mount-ro`

B) `--bind-readonly`

C) `--bind-ro`

D) `--read-bind`

---

## Question 10: Boot mode

Что произойдёт, если запустить `systemd-nspawn -D /var/lib/machines/debian` без флага `-b`?

A) Контейнер не запустится

B) Запустится интерактивный shell вместо init системы

C) Контейнер запустится в background

D) Будет выдана ошибка "Boot flag required"

---

## Question 11: Private network

Что делает флаг `--private-network`?

A) Создаёт veth pair к хосту

B) Подключает контейнер к bridge

C) Создаёт полностью изолированную сеть (только loopback)

D) Отключает сеть полностью

---

## Question 12: machinectl shell

Какая команда позволяет выполнить команду внутри запущенной машины "debian"?

A) `machinectl exec debian /bin/ls`

B) `machinectl shell debian /bin/ls`

C) `machinectl run debian /bin/ls`

D) `systemctl shell debian /bin/ls`

---

## Question 13: Volatile режим

Что означает опция `--volatile=yes`?

A) Контейнер будет автоматически удалён после остановки

B) Root filesystem будет overlay — изменения не сохраняются

C) Контейнер запустится в режиме высокой производительности

D) Логи будут храниться в памяти

---

## Question 14: Экспорт образа

Какая команда экспортирует машину "debian" в tar-архив?

A) `machinectl tar-export debian debian.tar.gz`

B) `machinectl export-tar debian debian.tar.gz`

C) `systemd-nspawn --export debian.tar.gz`

D) `nspawn export debian > debian.tar.gz`

---

## Question 15: systemd интеграция

Какой systemd unit отвечает за автозапуск машины "myserver"?

A) `systemd-nspawn-myserver.service`

B) `systemd-nspawn@myserver.service`

C) `machine-myserver.service`

D) `nspawn-myserver.service`

---

## Question 16: Journald

Какая команда показывает логи контейнера "debian" через journald?

A) `journalctl -u debian`

B) `journalctl --container=debian`

C) `journalctl -M debian`

D) `machinectl logs debian`

---

## Question 17: User namespaces

Какой флаг включает user namespace с автоматическим выбором UID/GID mapping?

A) `--private-users=pick`

B) `--user-namespace=auto`

C) `--userns=random`

D) `--map-users=auto`

---

## Question 18: .nspawn секции

Какая секция в .nspawn файле отвечает за настройку сети?

```ini
[???]
VirtualEthernet=yes
Bridge=br0
```

A) [Exec]

B) [Files]

C) [Network]

D) [Networking]

---

## Question 19: Клонирование машины

Какая команда создаст копию машины "debian" с именем "debian-test"?

A) `machinectl copy debian debian-test`

B) `machinectl clone debian debian-test`

C) `machinectl duplicate debian debian-test`

D) `cp -r /var/lib/machines/debian /var/lib/machines/debian-test`

---

## Question 20: Сравнение подходов

Для какого сценария systemd-nspawn подходит лучше, чем Docker?

A) Микросервисная архитектура с сотнями контейнеров

B) Запуск stateless приложений из Docker Hub

C) Тестирование systemd unit-файлов и системного ПО

D) Развёртывание в Kubernetes кластере

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | systemd-nspawn создаёт system containers с полной ОС и init системой (systemd), в отличие от application containers |
| 2 | B | systemd-nspawn работает напрямую с директориями, tar-архивами или raw disk images, без OCI layers и registry |
| 3 | B | Флаг `-b` (boot) запускает init систему контейнера, а не просто shell |
| 4 | C | `/var/lib/machines/` — стандартная директория для systemd-machined и systemd-nspawn |
| 5 | B | `machinectl list` показывает запущенные машины |
| 6 | C | `--network-veth` создаёт virtual ethernet pair: host0 в контейнере и ve-<name> на хосте |
| 7 | B | Файлы `.nspawn` располагаются в `/etc/systemd/nspawn/` |
| 8 | B | Правильный синтаксис: `--capability=CAP_NET_ADMIN` |
| 9 | C | `--bind-ro` создаёт read-only bind mount |
| 10 | B | Без `-b` запускается интерактивный shell (по умолчанию /bin/bash или /bin/sh) |
| 11 | C | `--private-network` создаёт изолированную сеть только с loopback интерфейсом |
| 12 | B | `machinectl shell <machine> <command>` выполняет команду в машине |
| 13 | B | `--volatile=yes` создаёт overlay над root filesystem, изменения не сохраняются после остановки |
| 14 | B | `machinectl export-tar` экспортирует машину в tar-архив |
| 15 | B | systemd использует template unit `systemd-nspawn@.service`, имя машины указывается после @ |
| 16 | C | `journalctl -M <machine>` показывает логи конкретной машины |
| 17 | A | `--private-users=pick` включает user namespace с автоматическим выбором свободного диапазона |
| 18 | C | Секция `[Network]` отвечает за сетевые настройки в .nspawn файлах |
| 19 | B | `machinectl clone` создаёт копию машины (образа) |
| 20 | C | systemd-nspawn идеален для тестирования systemd и системного ПО благодаря полной поддержке init системы |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили systemd-nspawn. Готовы использовать его в production! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы о сети и конфигурации. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о machinectl и .nspawn файлах. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно базовые команды и концепции. |

---

